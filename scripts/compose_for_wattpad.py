#!/usr/bin/env python3
"""
Wattpad Episode Composer for Hockey Shuttle Series

This script composes episodes from chapter markdown files into a format
suitable for Wattpad publishing. It can output individual chapters or
a combined episode file, optimized for mobile reading.

Usage:
    uv run scripts/compose_for_wattpad.py <episode-path> [--output-dir <dir>] [--combine]

Examples:
    # Generate separate chapters for Wattpad
    uv run scripts/compose_for_wattpad.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice

    # Generate combined episode file
    uv run scripts/compose_for_wattpad.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice --combine

    # Specify custom output directory
    uv run scripts/compose_for_wattpad.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice --output-dir wattpad-ready
"""

import argparse
import sys
import re
from pathlib import Path
from datetime import datetime


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Compose episodes for Wattpad publishing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "episode_path",
        type=str,
        help="Path to episode directory (e.g., series/hockey-shuttle/season-01/episode-01-returning-to-center-ice)"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="wattpad",
        help="Output directory relative to repo root. Default: wattpad"
    )
    parser.add_argument(
        "--combine",
        action="store_true",
        help="Combine all chapters into a single file instead of separate chapter files"
    )
    parser.add_argument(
        "--add-metadata",
        action="store_true",
        default=True,
        help="Add episode metadata header (enabled by default)"
    )
    parser.add_argument(
        "--word-count",
        action="store_true",
        help="Display word count for each chapter"
    )
    return parser.parse_args()


def find_repo_root():
    """Find the repository root directory."""
    current = Path.cwd()
    while current != current.parent:
        if (current / ".git").exists() or (current / "series").exists():
            return current
        current = current.parent
    return Path.cwd()


def extract_episode_info(episode_path: Path):
    """Extract episode information from path and outline."""
    # Parse episode name from path
    episode_name = episode_path.name
    match = re.match(r"episode-(\d+)-(.+)", episode_name)

    if match:
        episode_num = int(match.group(1))
        episode_title = match.group(2).replace("-", " ").title()
    else:
        episode_num = "?"
        episode_title = episode_name

    # Try to read outline for more info
    outline_path = episode_path / "outline.md"
    series_name = "Hockey Shuttle"
    season_num = "1"

    if outline_path.exists():
        content = outline_path.read_text()
        # Look for series and season info in outline
        series_match = re.search(r"\*\*Series\*\*:?\s*(.+)", content)
        season_match = re.search(r"\*\*Season\*\*:?\s*(\d+)", content)

        if series_match:
            series_name = series_match.group(1).strip()
        if season_match:
            season_num = season_match.group(1).strip()

    return {
        "series": series_name,
        "season": season_num,
        "episode": episode_num,
        "title": episode_title,
        "full_title": f"{series_name} - S{season_num}E{episode_num}: {episode_title}",
        "episode_slug": episode_name
    }


def read_chapter_files(episode_path: Path):
    """Read all chapter markdown files from the draft directory."""
    draft_dir = episode_path / "draft"

    if not draft_dir.exists():
        print(f"❌ Error: Draft directory not found at {draft_dir}")
        return []

    # Find all chapter files
    chapter_files = sorted(draft_dir.glob("chapter-*.md"))

    if not chapter_files:
        print(f"❌ Error: No chapter files found in {draft_dir}")
        return []

    chapters = []
    for chapter_file in chapter_files:
        try:
            content = chapter_file.read_text()

            # Extract chapter title if present
            title = None
            lines = content.split("\n")
            for line in lines[:10]:  # Check first 10 lines for title
                if line.startswith("# "):
                    title = line[2:].strip()
                    break

            # Calculate word count
            word_count = len(content.split())

            chapters.append({
                "filename": chapter_file.name,
                "title": title,
                "content": content,
                "word_count": word_count
            })
        except Exception as e:
            print(f"⚠️  Warning: Could not read {chapter_file}: {e}")

    return chapters


def format_for_wattpad(content: str, strip_markdown=True):
    """
    Format content for Wattpad.
    Wattpad supports basic formatting but works best with clean, simple text.
    """
    lines = content.split("\n")
    formatted_lines = []

    for line in lines:
        # Skip the main chapter title (will be added separately)
        if line.startswith("# ") and len(formatted_lines) == 0:
            continue

        # Convert heading levels (Wattpad prefers bold for subheadings)
        if line.startswith("## "):
            # Subheadings become bold
            formatted_lines.append(f"**{line[3:].strip()}**")
            formatted_lines.append("")  # Add spacing
        elif line.startswith("### "):
            # Sub-subheadings also become bold but smaller
            formatted_lines.append(f"**{line[4:].strip()}**")
            formatted_lines.append("")
        elif line.strip() == "---":
            # Scene breaks - Wattpad uses centered asterisks
            formatted_lines.append("")
            formatted_lines.append("* * *")
            formatted_lines.append("")
        else:
            # Keep the line as-is (Wattpad supports basic markdown like *italic* and **bold**)
            formatted_lines.append(line)

    return "\n".join(formatted_lines).strip()


def create_episode_header(episode_info: dict):
    """Create a metadata header for the episode."""
    header = f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{episode_info['series']}
Season {episode_info['season']} • Episode {episode_info['episode']}
"{episode_info['title']}"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
    return header


def create_chapter_header(chapter_num: int, chapter_title: str, episode_info: dict):
    """Create a header for individual chapter."""
    header = f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{episode_info['series']} - S{episode_info['season']}E{episode_info['episode']}
Chapter {chapter_num}
{chapter_title if chapter_title else ''}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
    return header


def create_chapter_footer(is_last_chapter=False):
    """Create a footer for chapters."""
    if is_last_chapter:
        footer = """

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Thank you for reading!

Don't forget to vote ⭐ if you enjoyed this episode!

What did you think? Leave a comment! 💬

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    else:
        footer = """

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

To be continued...

Don't forget to vote ⭐ and comment 💬

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    return footer


def compose_single_chapter(chapter: dict, chapter_num: int, episode_info: dict,
                          add_metadata: bool, is_last_chapter: bool):
    """Compose a single chapter for Wattpad."""
    parts = []

    # Add chapter header
    if add_metadata:
        parts.append(create_chapter_header(chapter_num, chapter["title"], episode_info))
    elif chapter["title"]:
        parts.append(f"# {chapter['title']}\n")

    # Add formatted content
    formatted_content = format_for_wattpad(chapter["content"])
    parts.append(formatted_content)

    # Add footer
    if add_metadata:
        parts.append(create_chapter_footer(is_last_chapter))

    return "\n".join(parts)


def compose_combined_episode(chapters: list, episode_info: dict, add_metadata: bool):
    """Combine all chapters into a single episode file."""
    parts = []

    # Add episode header
    if add_metadata:
        parts.append(create_episode_header(episode_info))

    # Add each chapter
    for i, chapter in enumerate(chapters, 1):
        is_last = (i == len(chapters))

        # Chapter divider
        if i > 1:
            parts.append("\n\n")

        # Chapter content
        chapter_content = compose_single_chapter(
            chapter, i, episode_info, add_metadata, is_last
        )
        parts.append(chapter_content)

    return "\n".join(parts)


def save_chapters_separately(chapters: list, episode_info: dict, output_dir: Path,
                             add_metadata: bool, show_word_count: bool):
    """Save each chapter as a separate file."""
    episode_dir = output_dir / episode_info['episode_slug']
    episode_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n📝 Composing {len(chapters)} chapters for Wattpad...")
    if show_word_count:
        print(f"\nWord counts:")

    for i, chapter in enumerate(chapters, 1):
        is_last = (i == len(chapters))

        # Compose chapter
        chapter_content = compose_single_chapter(
            chapter, i, episode_info, add_metadata, is_last
        )

        # Save to file
        output_file = episode_dir / f"chapter-{i:02d}.txt"
        output_file.write_text(chapter_content, encoding='utf-8')

        # Display info
        chapter_name = chapter["title"] if chapter["title"] else f"Chapter {i}"
        if show_word_count:
            print(f"  • {chapter_name}: {chapter['word_count']:,} words")

        print(f"✅ Saved: {output_file}")

    # Create a manifest file
    manifest_content = f"""Episode: {episode_info['full_title']}
Chapters: {len(chapters)}
Total Words: {sum(ch['word_count'] for ch in chapters):,}
Generated: {datetime.now().strftime("%B %d, %Y at %I:%M %p")}

Chapter Files:
"""
    for i in range(1, len(chapters) + 1):
        manifest_content += f"  {i}. chapter-{i:02d}.txt\n"

    manifest_file = episode_dir / "MANIFEST.txt"
    manifest_file.write_text(manifest_content, encoding='utf-8')
    print(f"✅ Saved manifest: {manifest_file}")

    return episode_dir


def save_combined_episode(chapters: list, episode_info: dict, output_dir: Path,
                         add_metadata: bool, show_word_count: bool):
    """Save all chapters combined into a single file."""
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n📝 Composing combined episode for Wattpad...")

    if show_word_count:
        print(f"\nWord counts:")
        for i, chapter in enumerate(chapters, 1):
            chapter_name = chapter["title"] if chapter["title"] else f"Chapter {i}"
            print(f"  • {chapter_name}: {chapter['word_count']:,} words")
        total_words = sum(ch['word_count'] for ch in chapters)
        print(f"\nTotal: {total_words:,} words")

    # Compose combined content
    combined_content = compose_combined_episode(chapters, episode_info, add_metadata)

    # Save to file
    safe_title = episode_info['episode_slug']
    output_file = output_dir / f"{safe_title}-complete.txt"
    output_file.write_text(combined_content, encoding='utf-8')

    print(f"\n✅ Saved combined episode: {output_file}")

    return output_file


def main():
    args = parse_args()

    # Find repo root and set up paths
    repo_root = find_repo_root()
    episode_path = repo_root / args.episode_path
    output_dir = repo_root / args.output_dir

    # Validate episode path
    if not episode_path.exists():
        print(f"❌ Error: Episode path not found: {episode_path}")
        sys.exit(1)

    # Extract episode information
    print(f"\n🏒 Processing: {episode_path.name}")
    episode_info = extract_episode_info(episode_path)
    print(f"   {episode_info['full_title']}")

    # Read chapter files
    chapters = read_chapter_files(episode_path)
    if not chapters:
        sys.exit(1)

    print(f"\n📚 Found {len(chapters)} chapters")

    # Compose for Wattpad
    if args.combine:
        output_file = save_combined_episode(
            chapters, episode_info, output_dir,
            args.add_metadata, args.word_count
        )
        print(f"\n✨ Combined episode ready for Wattpad!")
        print(f"   📁 {output_file}")
    else:
        output_dir_path = save_chapters_separately(
            chapters, episode_info, output_dir,
            args.add_metadata, args.word_count
        )
        print(f"\n✨ Individual chapters ready for Wattpad!")
        print(f"   📁 {output_dir_path}")

    print(f"\n💡 Tips for Wattpad:")
    print(f"   • Upload each chapter separately for best reader engagement")
    print(f"   • Use chapter titles to create compelling episode structure")
    print(f"   • Add a cover image (recommended size: 512x800px)")
    print(f"   • Encourage readers to vote ⭐ and comment 💬")
    print(f"   • Consider adding trigger warnings if needed")
    print(f"\n🎯 Ready to publish!\n")


if __name__ == "__main__":
    main()
