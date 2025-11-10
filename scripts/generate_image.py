#!/usr/bin/env python3
"""
Image Generator using Google Gemini 2.5 Flash (Nano Banana)

This script generates images using Google's Gemini API based on text prompts.
Generated images are saved to the hockey-shuttle/10-visuals folder.

Usage:
    uv run scripts/generate_image.py --prompt "A hockey player on ice" --subfolder "characters" --filename "hockey_player.png"
    uv run scripts/generate_image.py -p "Sunset over mountains" -s "scenes" -f "sunset.png"

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


def generate_image(prompt: str, subfolder: str, filename: str, base_dir: Optional[Path] = None) -> Path:
    """
    Generate an image using Google Gemini API based on the prompt.

    Args:
        prompt: Text description of the image to generate
        subfolder: Subdirectory within the visuals folder (e.g., 'characters', 'scenes')
        filename: Name for the output image file (should include extension)
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

    output_path = output_dir / filename

    # Load API key and configure
    api_key = load_api_key()
    genai.configure(api_key=api_key)

    print(f"🎨 Generating image with prompt: '{prompt}'")
    print(f"📝 Using model: Gemini 2.5 Flash (Nano Banana)")

    try:
        # Use Gemini 2.5 Flash Image model for image generation
        model = genai.GenerativeModel("gemini-2.5-flash-image")

        # Generate the image
        response = model.generate_content(prompt)

        # Save the generated image
        # The response contains both text and image parts
        image_found = False
        if hasattr(response, '_result') and hasattr(response._result, 'candidates'):
            candidate = response._result.candidates[0]
            if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                for part in candidate.content.parts:
                    # Check if this part contains inline image data
                    if hasattr(part, 'inline_data') and part.inline_data:
                        # The data is raw bytes, write it directly
                        with open(output_path, 'wb') as f:
                            # Make sure data attribute exists and has content
                            if hasattr(part.inline_data, 'data') and part.inline_data.data:
                                f.write(part.inline_data.data)
                                image_found = True
                            else:
                                print(f"⚠️  Warning: inline_data exists but no data attribute")

        if image_found:
            # Load for verification
            from PIL import Image
            image = Image.open(str(output_path))

            print(f"✅ Image successfully generated and saved!")
            print(f"📂 Location: {output_path}")
            print(f"📏 Size: {image.size}")

            return output_path
        else:
            print("❌ No images were generated")
            print(f"Response structure: {dir(response)}")
            if hasattr(response, '_result'):
                print(f"Result: {response._result}")
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
  %(prog)s --prompt "A hockey player scoring a goal" --subfolder "characters" --filename "hockey_goal.png"
  %(prog)s -p "Futuristic city at sunset" -s "scenes" -f "city.png"
  %(prog)s --prompt "Abstract art with blue and gold" --subfolder "artwork" --filename "abstract.jpg"
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
    print(f"\n{'='*60}")
    print("🖼️  Gemini Image Generator (Nano Banana)")
    print(f"{'='*60}\n")

    output_path = generate_image(
        prompt=args.prompt,
        subfolder=args.subfolder,
        filename=args.filename,
        base_dir=base_dir
    )

    print(f"\n{'='*60}")
    print("✨ Generation Complete!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
