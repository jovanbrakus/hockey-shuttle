#!/usr/bin/env python3
"""
Image Generator using Google Gemini 2.5 Flash (Nano Banana)

This script generates images using Google's Gemini API based on text prompts.
Generated images are saved to the output/images folder.

Usage:
    uv run scripts/generate_image.py --prompt "A hockey player on ice" --filename "hockey_player.png"
    uv run scripts/generate_image.py -p "Sunset over mountains" -f "sunset.png"

Requirements:
    - GEMINI_API_KEY in .env file
    - google-generativeai package
    - python-dotenv package
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Optional

try:
    import google.generativeai as genai
    from dotenv import load_dotenv
except ImportError as e:
    print(f"❌ Error: Required package not installed: {e}")
    print("\nInstall required packages with:")
    print("  uv pip install google-generativeai python-dotenv")
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


def generate_image(prompt: str, filename: str, output_dir: Optional[Path] = None) -> Path:
    """
    Generate an image using Google Gemini API based on the prompt.

    Args:
        prompt: Text description of the image to generate
        filename: Name for the output image file (should include extension)
        output_dir: Optional output directory (defaults to output/images)

    Returns:
        Path to the saved image file
    """
    # Set up output directory
    if output_dir is None:
        repo_root = find_repo_root()
        output_dir = repo_root / "output" / "images"

    output_dir.mkdir(parents=True, exist_ok=True)

    # Ensure filename has an extension
    if not any(filename.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.webp']):
        filename = f"{filename}.png"

    output_path = output_dir / filename

    # Load API key and configure
    api_key = load_api_key()
    genai.configure(api_key=api_key)

    print(f"🎨 Generating image with prompt: '{prompt}'")
    print(f"📝 Using model: Gemini 2.5 Flash (Nano Banana)")

    try:
        # Use Imagen 3 model for image generation
        # Note: Google's generative AI library uses imagen-3.0-generate-001 for image generation
        model = genai.ImageGenerationModel("imagen-3.0-generate-001")

        # Generate the image
        result = model.generate_images(
            prompt=prompt,
            number_of_images=1,
            safety_filter_level="block_few",
            person_generation="allow_adult",
        )

        # Save the first (and only) generated image
        if result.images:
            image = result.images[0]

            # Save the image
            image._pil_image.save(str(output_path))

            print(f"✅ Image successfully generated and saved!")
            print(f"📂 Location: {output_path}")
            print(f"📏 Size: {image._pil_image.size}")

            return output_path
        else:
            print("❌ No images were generated")
            sys.exit(1)

    except AttributeError:
        # Fallback: Use the standard generate method if ImageGenerationModel isn't available
        print("⚠️  Using alternative generation method...")
        try:
            # Try using the standard generative model with image output
            model = genai.GenerativeModel('gemini-2.5-flash')
            response = model.generate_content([
                prompt,
                "Generate a high-quality, detailed image based on this description."
            ])

            # For newer API versions, images might be in response.images
            if hasattr(response, 'images') and response.images:
                response.images[0].save(str(output_path))
                print(f"✅ Image successfully generated and saved!")
                print(f"📂 Location: {output_path}")
                return output_path
            else:
                print("❌ This model doesn't support image generation.")
                print("ℹ️  Note: Image generation with Gemini requires specific API access.")
                print("   You may need to use Google's Imagen API directly.")
                sys.exit(1)

        except Exception as e:
            print(f"❌ Error generating image: {e}")
            print("\nℹ️  Troubleshooting:")
            print("   1. Ensure your API key has image generation permissions")
            print("   2. Check if Imagen API is enabled in your Google Cloud project")
            print("   3. Verify you're using the correct model name")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Error generating image: {e}")
        print(f"\nError type: {type(e).__name__}")
        sys.exit(1)


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate images using Google Gemini 2.5 Flash API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --prompt "A hockey player scoring a goal" --filename "hockey_goal.png"
  %(prog)s -p "Futuristic city at sunset" -f "city.png"
  %(prog)s --prompt "Abstract art with blue and gold" --filename "abstract.jpg"
        """
    )

    parser.add_argument(
        "-p", "--prompt",
        type=str,
        required=True,
        help="Text prompt describing the image to generate"
    )

    parser.add_argument(
        "-f", "--filename",
        type=str,
        required=True,
        help="Output filename (e.g., 'image.png', 'photo.jpg')"
    )

    parser.add_argument(
        "-o", "--output-dir",
        type=str,
        default=None,
        help="Custom output directory (default: output/images)"
    )

    return parser.parse_args()


def main():
    """Main entry point for the script."""
    args = parse_args()

    # Convert output directory to Path if provided
    output_dir = Path(args.output_dir) if args.output_dir else None

    # Generate the image
    print(f"\n{'='*60}")
    print("🖼️  Gemini Image Generator (Nano Banana)")
    print(f"{'='*60}\n")

    output_path = generate_image(
        prompt=args.prompt,
        filename=args.filename,
        output_dir=output_dir
    )

    print(f"\n{'='*60}")
    print("✨ Generation Complete!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
