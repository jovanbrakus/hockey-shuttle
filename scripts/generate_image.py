#!/usr/bin/env python3
"""
Image Generator using Google Gemini or Imagen models

This script generates images using Google's AI models (Gemini 2.5 Flash Image or Imagen 4.0).
Generated images are saved to the hockey-shuttle/10-visuals folder.

Usage:
    # Use Gemini (default)
    uv run scripts/generate_image.py --prompt "A hockey player on ice" --subfolder "characters" --filename "hockey_player.png"

    # Use Imagen 4.0
    uv run scripts/generate_image.py --prompt "A hockey player on ice" --subfolder "characters" --filename "hockey_player.png" --model imagen

    # Short form
    uv run scripts/generate_image.py -p "Sunset" -s "scenes" -f "sunset.png" -m imagen

Requirements:
    - GEMINI_API_KEY in .env file
    - google-generativeai package (for Gemini)
    - google-genai package (for Imagen)
    - python-dotenv package
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Optional

try:
    from dotenv import load_dotenv
except ImportError as e:
    print(f"❌ Error: python-dotenv not installed: {e}")
    print("\nInstall with: uv pip install python-dotenv")
    sys.exit(1)


def find_repo_root() -> Path:
    """Find the repository root directory."""
    current = Path.cwd()
    while current != current.parent:
        if (current / ".git").exists() or (current / "series").exists():
            return current
        current = current.parent
    return Path.cwd()


def load_api_key() -> str:
    """Load Gemini API key from .env file."""
    repo_root = find_repo_root()
    env_path = repo_root / ".env"

    # Load environment variables from .env file
    load_dotenv(dotenv_path=env_path)

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("❌ Error: GEMINI_API_KEY not found in .env file")
        print(f"\nPlease create a .env file at: {env_path}")
        print("Add the following line:")
        print("GEMINI_API_KEY=your_api_key_here")
        print("\nGet your API key from: https://makersuite.google.com/app/apikey")
        sys.exit(1)

    return api_key


def get_unique_filename(output_dir: Path, filename: str) -> Path:
    """
    Get a unique filename by adding suffix if file already exists.

    Args:
        output_dir: Directory where file will be saved
        filename: Desired filename

    Returns:
        Path object with unique filename
    """
    output_path = output_dir / filename

    # If file doesn't exist, return as-is
    if not output_path.exists():
        return output_path

    # Split filename into name and extension
    stem = output_path.stem
    suffix = output_path.suffix

    # Try adding numbers until we find a unique name
    counter = 1
    while True:
        new_filename = f"{stem}-{counter}{suffix}"
        new_path = output_dir / new_filename
        if not new_path.exists():
            print(f"ℹ️  File exists, using: {new_filename}")
            return new_path
        counter += 1


def generate_image_gemini(prompt: str, output_path: Path, api_key: str) -> bool:
    """Generate image using Gemini 2.5 Flash Image model."""
    try:
        import google.generativeai as genai
    except ImportError:
        print("❌ Error: google-generativeai package not installed")
        print("\nInstall with: uv pip install google-generativeai")
        return False

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash-image")
        response = model.generate_content(prompt)

        # Save the generated image
        image_found = False
        if hasattr(response, '_result') and hasattr(response._result, 'candidates'):
            candidate = response._result.candidates[0]
            if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                for part in candidate.content.parts:
                    if hasattr(part, 'inline_data') and part.inline_data:
                        with open(output_path, 'wb') as f:
                            if hasattr(part.inline_data, 'data') and part.inline_data.data:
                                f.write(part.inline_data.data)
                                image_found = True

        if not image_found:
            print("❌ No images were generated (possibly filtered by safety)")
            return False

        return True

    except Exception as e:
        print(f"❌ Error generating image with Gemini: {e}")
        return False


def generate_image_imagen(prompt: str, output_path: Path, api_key: str) -> bool:
    """Generate image using Imagen 4.0 model."""
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("❌ Error: google-genai package not installed")
        print("\nInstall with: uv pip install google-genai")
        return False

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_images(
            model='imagen-4.0-generate-001',
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
            )
        )

        # Save the generated image
        if response.generated_images and len(response.generated_images) > 0:
            generated_image = response.generated_images[0]

            with open(output_path, 'wb') as f:
                f.write(generated_image.image.image_bytes)

            return True
        else:
            print("❌ No images were generated (possibly filtered by safety)")
            return False

    except Exception as e:
        print(f"❌ Error generating image with Imagen: {e}")
        return False


def generate_image(
    prompt: str,
    subfolder: str,
    filename: str,
    model_type: str = "gemini",
    base_dir: Optional[Path] = None
) -> Path:
    """
    Generate an image using specified Google AI model.

    Args:
        prompt: Text description of the image to generate
        subfolder: Subdirectory within the visuals folder (e.g., 'characters', 'scenes')
        filename: Name for the output image file (should include extension)
        model_type: Either "gemini" or "imagen" (default: "gemini")
        base_dir: Optional base directory (defaults to hockey-shuttle/10-visuals)

    Returns:
        Path to the saved image file
    """
    # Set up output directory
    if base_dir is None:
        repo_root = find_repo_root()
        base_dir = repo_root / "series" / "hockey-shuttle" / "10-visuals"

    # Construct full output path with subfolder
    output_dir = base_dir / subfolder
    output_dir.mkdir(parents=True, exist_ok=True)

    # Ensure filename has an extension
    if not any(filename.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.webp']):
        filename = f"{filename}.png"

    # Get unique filename (won't overwrite existing)
    output_path = get_unique_filename(output_dir, filename)

    # Load API key
    api_key = load_api_key()

    # Determine model and print info
    model_name = "Gemini 2.5 Flash Image" if model_type.lower() == "gemini" else "Imagen 4.0"
    print(f"🎨 Generating image with prompt: '{prompt[:80]}{'...' if len(prompt) > 80 else ''}'")
    print(f"📝 Using model: {model_name}")

    # Generate based on model type
    success = False
    if model_type.lower() == "gemini":
        success = generate_image_gemini(prompt, output_path, api_key)
    elif model_type.lower() == "imagen":
        success = generate_image_imagen(prompt, output_path, api_key)
    else:
        print(f"❌ Unknown model type: {model_type}")
        print("   Valid options: 'gemini' or 'imagen'")
        sys.exit(1)

    if not success:
        sys.exit(1)

    # Load for verification
    from PIL import Image
    image = Image.open(str(output_path))

    print(f"✅ Image successfully generated and saved!")
    print(f"📂 Location: {output_path}")
    print(f"📏 Size: {image.size}")

    return output_path


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate images using Google Gemini or Imagen models",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use Gemini (default)
  %(prog)s --prompt "A hockey player scoring a goal" --subfolder "characters" --filename "hockey_goal.png"

  # Use Imagen 4.0
  %(prog)s --prompt "A hockey player" --subfolder "characters" --filename "hockey.png" --model imagen

  # Short form
  %(prog)s -p "City at sunset" -s "scenes" -f "city.png" -m imagen
        """
    )

    parser.add_argument(
        "-p", "--prompt",
        type=str,
        required=True,
        help="Text prompt describing the image to generate"
    )

    parser.add_argument(
        "-s", "--subfolder",
        type=str,
        required=True,
        help="Subfolder within hockey-shuttle/10-visuals (e.g., 'characters', 'scenes', 'artwork')"
    )

    parser.add_argument(
        "-f", "--filename",
        type=str,
        required=True,
        help="Output filename (e.g., 'image.png', 'photo.jpg')"
    )

    parser.add_argument(
        "-m", "--model",
        type=str,
        default="gemini",
        choices=["gemini", "imagen"],
        help="Model to use: 'gemini' (default) or 'imagen'"
    )

    parser.add_argument(
        "-b", "--base-dir",
        type=str,
        default=None,
        help="Custom base directory (default: hockey-shuttle/10-visuals)"
    )

    return parser.parse_args()


def main():
    """Main entry point for the script."""
    args = parse_args()

    # Convert base directory to Path if provided
    base_dir = Path(args.base_dir) if args.base_dir else None

    # Generate the image
    model_name = "Gemini 2.5 Flash Image" if args.model == "gemini" else "Imagen 4.0"
    print(f"\n{'='*60}")
    print(f"🖼️  {model_name} Generator")
    print(f"{'='*60}\n")

    output_path = generate_image(
        prompt=args.prompt,
        subfolder=args.subfolder,
        filename=args.filename,
        model_type=args.model,
        base_dir=base_dir
    )

    print(f"\n{'='*60}")
    print("✨ Generation Complete!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
