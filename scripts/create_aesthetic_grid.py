#!/usr/bin/env python3
"""
Create 3x3 Aesthetic Grid from Individual Images

This script takes 9 individual square images and combines them into a single
3x3 grid for Wattpad aesthetic collages.

Usage:
    uv run scripts/create_aesthetic_grid.py --character sophia
    uv run scripts/create_aesthetic_grid.py --character ethan
    uv run scripts/create_aesthetic_grid.py -c sophia --gap 20
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

try:
    from PIL import Image
except ImportError:
    print("❌ Error: Pillow not installed")
    print("\nInstall with: uv pip install Pillow")
    sys.exit(1)


def find_repo_root() -> Path:
    """Find the repository root directory."""
    current = Path.cwd()
    while current != current.parent:
        if (current / ".git").exists() or (current / "series").exists():
            return current
        current = current.parent
    return Path.cwd()


def create_grid(
    character: str,
    gap: int = 0,
    square_size: int = 1000,
    output_name: Optional[str] = None
) -> Path:
    """
    Create a 3x3 grid from individual character aesthetic images.

    Args:
        character: Either "sophia" or "ethan"
        gap: Gap between images in pixels (default: 0 for seamless)
        square_size: Size of each square in pixels (default: 1000)
        output_name: Optional custom output filename

    Returns:
        Path to the created grid image
    """
    repo_root = find_repo_root()
    aesthetics_dir = repo_root / "series" / "hockey-shuttle" / "10-visuals" / "aesthetics"
    character_dir = aesthetics_dir / character.lower()

    if not character_dir.exists():
        print(f"❌ Error: Character directory not found: {character_dir}")
        sys.exit(1)

    # Define the expected filenames in grid order
    if character.lower() == "sophia":
        filenames = [
            "1-badminton-racket.png",
            "2-study-scene.png",
            "3-ice-skating.png",
            "4-shuttlecock-motion.png",
            "5-sophia-portrait.png",  # CENTER
            "6-winnipeg-winter.png",
            "7-sports-tape.png",
            "8-science-stars.png",
            "9-court-shoes.png"
        ]
    elif character.lower() == "ethan":
        filenames = [
            "1-hockey-stick-blade.png",
            "2-physics-notebook.png",
            "3-ice-rink-night.png",
            "4-puck-impact.png",
            "5-ethan-portrait.png",  # CENTER
            "6-captain-c.png",
            "7-skate-sharpening.png",
            "8-textbook-tape.png",
            "9-winter-breath.png"
        ]
    else:
        print(f"❌ Error: Unknown character '{character}'")
        print("   Valid options: 'sophia' or 'ethan'")
        sys.exit(1)

    # Load all images
    print(f"\n{'='*60}")
    print(f"🎨 Creating {character.title()}'s Aesthetic Grid")
    print(f"{'='*60}\n")

    images = []
    for i, filename in enumerate(filenames, 1):
        img_path = character_dir / filename
        if not img_path.exists():
            print(f"❌ Missing image {i}: {filename}")
            print(f"   Expected at: {img_path}")
            sys.exit(1)

        try:
            img = Image.open(img_path)
            # Resize to exact square size
            img = img.resize((square_size, square_size), Image.Resampling.LANCZOS)
            images.append(img)
            print(f"✓ Loaded square {i}: {filename}")
        except Exception as e:
            print(f"❌ Error loading {filename}: {e}")
            sys.exit(1)

    # Calculate grid dimensions
    grid_size = (square_size * 3) + (gap * 2)

    # Create the grid canvas
    if gap > 0:
        # Use white background for gaps
        grid = Image.new('RGB', (grid_size, grid_size), 'white')
    else:
        # Seamless grid
        grid = Image.new('RGB', (grid_size, grid_size))

    print(f"\n📐 Grid size: {grid_size}x{grid_size}px")
    print(f"   Square size: {square_size}x{square_size}px")
    print(f"   Gap: {gap}px\n")

    # Paste images into grid
    print("🎨 Assembling grid...")
    for idx, img in enumerate(images):
        row = idx // 3
        col = idx % 3

        x = col * (square_size + gap)
        y = row * (square_size + gap)

        grid.paste(img, (x, y))
        position = f"[{row+1},{col+1}]"
        print(f"   ✓ Placed square {idx+1} at position {position}")

    # Save the grid
    output_dir = aesthetics_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    if output_name:
        output_filename = output_name if output_name.endswith('.png') else f"{output_name}.png"
    else:
        gap_suffix = f"-gap{gap}" if gap > 0 else ""
        output_filename = f"{character.lower()}-aesthetic-grid{gap_suffix}.png"

    output_path = output_dir / output_filename

    grid.save(output_path, 'PNG', quality=95)

    print(f"\n✅ Grid created successfully!")
    print(f"📂 Location: {output_path}")
    print(f"📏 Size: {grid.size[0]}x{grid.size[1]}px")

    return output_path


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Create 3x3 aesthetic grid from individual images",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create Sophia's grid (seamless)
  %(prog)s --character sophia

  # Create Ethan's grid with 20px gap
  %(prog)s --character ethan --gap 20

  # Short form
  %(prog)s -c sophia -g 10
        """
    )

    parser.add_argument(
        "-c", "--character",
        type=str,
        required=True,
        choices=["sophia", "ethan"],
        help="Character name: 'sophia' or 'ethan'"
    )

    parser.add_argument(
        "-g", "--gap",
        type=int,
        default=0,
        help="Gap between images in pixels (default: 0 for seamless)"
    )

    parser.add_argument(
        "-s", "--size",
        type=int,
        default=1000,
        help="Size of each square in pixels (default: 1000)"
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        help="Custom output filename"
    )

    return parser.parse_args()


def main():
    """Main entry point for the script."""
    args = parse_args()

    output_path = create_grid(
        character=args.character,
        gap=args.gap,
        square_size=args.size,
        output_name=args.output
    )

    print(f"\n{'='*60}")
    print("✨ Grid Assembly Complete!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
