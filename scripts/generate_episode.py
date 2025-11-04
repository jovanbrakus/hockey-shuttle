#!/usr/bin/env python3
"""
Episode Generator for Hockey Shuttle Series

This script generates PDF, HTML, and EPUB files from episode markdown files.
Usage: uv run scripts/generate_episode.py <episode-path> [--formats pdf,html,epub]

Example:
    uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice
    uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice --formats pdf,html
"""

import argparse
import sys
from pathlib import Path
import markdown2
import re
from datetime import datetime


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate PDF, HTML, and EPUB from episode markdown files"
    )
    parser.add_argument(
        "episode_path",
        type=str,
        help="Path to episode directory (e.g., series/hockey-shuttle/season-01/episode-01-returning-to-center-ice)"
    )
    parser.add_argument(
        "--formats",
        type=str,
        default="md,pdf,html,epub",
        help="Comma-separated list of formats to generate (md,pdf,html,epub). Default: all"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="output",
        help="Output directory relative to repo root. Default: output"
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
        "full_title": f"{series_name} - Season {season_num}, Episode {episode_num}: {episode_title}"
    }


def read_chapter_files(episode_path: Path):
    """Read all chapter markdown files from the draft directory."""
    draft_dir = episode_path / "draft"

    if not draft_dir.exists():
        print(f"Error: Draft directory not found at {draft_dir}")
        return []

    # Find all chapter files
    chapter_files = sorted(draft_dir.glob("chapter-*.md"))

    if not chapter_files:
        print(f"Error: No chapter files found in {draft_dir}")
        return []

    chapters = []
    for chapter_file in chapter_files:
        try:
            content = chapter_file.read_text()
            # Extract chapter title if present
            lines = content.split("\n")
            title = None
            for line in lines[:10]:  # Check first 10 lines for title
                if line.startswith("# "):
                    title = line[2:].strip()
                    break

            chapters.append({
                "filename": chapter_file.name,
                "title": title,
                "content": content
            })
        except Exception as e:
            print(f"Warning: Could not read {chapter_file}: {e}")

    return chapters


def combine_chapters(chapters, episode_info):
    """Combine all chapters into a single markdown document."""
    combined = []

    # Add title page
    combined.append(f"# {episode_info['full_title']}")
    combined.append("")
    combined.append("---")
    combined.append("")

    # Add each chapter
    for i, chapter in enumerate(chapters, 1):
        if chapter["title"]:
            combined.append(f"# Chapter {i}: {chapter['title']}")
        else:
            combined.append(f"# Chapter {i}")
        combined.append("")

        # Add chapter content (skip the title line if it exists)
        content = chapter["content"]
        lines = content.split("\n")

        # Skip first line if it's a title
        if lines and lines[0].startswith("# "):
            lines = lines[1:]

        combined.append("\n".join(lines).strip())
        combined.append("")
        combined.append("---")
        combined.append("")

    return "\n".join(combined)


def generate_html(markdown_content: str, episode_info: dict, output_path: Path):
    """Generate HTML file from markdown content."""
    # Convert markdown to HTML
    html_content = markdown2.markdown(markdown_content, extras=['fenced-code-blocks', 'tables', 'break-on-newline'])

    # Create complete HTML document
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{episode_info['full_title']}</title>
    <style>
        @page {{
            size: letter;
            margin: 1in;
        }}

        body {{
            font-family: Georgia, 'Times New Roman', 'Liberation Serif', serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
            background: #fafafa;
        }}

        h1 {{
            font-family: Georgia, 'Times New Roman', 'Liberation Serif', serif;
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
            margin-top: 40px;
            page-break-after: avoid;
        }}

        h2, h3 {{
            font-family: Georgia, 'Times New Roman', 'Liberation Serif', serif;
            color: #34495e;
            margin-top: 30px;
            page-break-after: avoid;
        }}

        p {{
            margin: 1em 0;
            text-align: justify;
            orphans: 3;
            widows: 3;
        }}

        hr {{
            border: none;
            border-top: 1px solid #bdc3c7;
            margin: 40px 0;
            page-break-after: always;
        }}

        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin: 20px 0;
            font-style: italic;
            color: #555;
        }}

        em {{
            font-style: italic;
        }}

        strong {{
            font-weight: bold;
        }}

        /* Prevent emoji font embedding */
        * {{
            font-variant-emoji: text;
        }}

        @media print {{
            body {{
                max-width: 100%;
                background: white;
                padding: 0;
            }}
        }}
    </style>
</head>
<body>
    {html_content}
    <hr>
    <footer style="text-align: center; color: #7f8c8d; margin-top: 40px;">
        <p>Generated on {datetime.now().strftime("%B %d, %Y")}</p>
    </footer>
</body>
</html>"""

    output_path.write_text(html_doc)
    print(f"✓ Generated HTML: {output_path}")


def generate_pdf(html_path: Path, output_path: Path):
    """Generate PDF file from HTML."""
    try:
        from weasyprint import HTML
        HTML(filename=str(html_path)).write_pdf(output_path)
        print(f"✓ Generated PDF: {output_path}")
    except ImportError:
        print("⚠ Warning: weasyprint not installed. PDF generation skipped.")
        print("  Install with: uv pip install weasyprint")
    except Exception as e:
        print(f"⚠ Warning: PDF generation failed: {e}")


def generate_markdown(markdown_content: str, episode_info: dict, output_path: Path):
    """Generate combined markdown file."""
    output_path.write_text(markdown_content)
    print(f"✓ Generated Markdown: {output_path}")


def generate_epub(markdown_content: str, episode_info: dict, output_path: Path):
    """Generate EPUB file from markdown content."""
    try:
        from ebooklib import epub

        # Create EPUB book
        book = epub.EpubBook()

        # Set metadata
        book.set_identifier(f"hockey-shuttle-s{episode_info['season']}-e{episode_info['episode']}")
        book.set_title(episode_info['full_title'])
        book.set_language('en')
        book.add_author('Generated from Hockey Shuttle Series')

        # Split into chapters
        chapters_content = markdown_content.split("---")
        epub_chapters = []

        for i, chapter_content in enumerate(chapters_content):
            if not chapter_content.strip():
                continue

            html_content = markdown2.markdown(chapter_content, extras=['fenced-code-blocks', 'tables'])

            # Create EPUB chapter
            c = epub.EpubHtml(
                title=f"Chapter {i}",
                file_name=f"chap_{i:02d}.xhtml",
                lang='en'
            )
            c.content = f"<html><body>{html_content}</body></html>"

            book.add_item(c)
            epub_chapters.append(c)

        # Add default NCX and Nav files
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())

        # Define CSS style
        style = '''
        body { font-family: Georgia, serif; line-height: 1.6; }
        h1 { color: #2c3e50; }
        p { text-align: justify; margin: 1em 0; }
        '''
        nav_css = epub.EpubItem(
            uid="style_nav",
            file_name="style/nav.css",
            media_type="text/css",
            content=style
        )
        book.add_item(nav_css)

        # Create spine
        book.spine = ['nav'] + epub_chapters

        # Write EPUB file
        epub.write_epub(output_path, book, {})
        print(f"✓ Generated EPUB: {output_path}")
    except ImportError:
        print("⚠ Warning: ebooklib not installed. EPUB generation skipped.")
        print("  Install with: uv pip install ebooklib")
    except Exception as e:
        print(f"⚠ Warning: EPUB generation failed: {e}")


def main():
    args = parse_args()

    # Find repo root and set up paths
    repo_root = find_repo_root()
    episode_path = repo_root / args.episode_path
    output_dir = repo_root / args.output_dir

    # Validate episode path
    if not episode_path.exists():
        print(f"Error: Episode path not found: {episode_path}")
        sys.exit(1)

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Extract episode information
    print(f"\n📚 Processing episode: {episode_path.name}")
    episode_info = extract_episode_info(episode_path)
    print(f"   {episode_info['full_title']}\n")

    # Read chapter files
    chapters = read_chapter_files(episode_path)
    if not chapters:
        sys.exit(1)

    print(f"Found {len(chapters)} chapters")

    # Combine chapters
    combined_markdown = combine_chapters(chapters, episode_info)

    # Create episode-specific subdirectory
    episode_output_dir = output_dir / episode_path.name
    episode_output_dir.mkdir(parents=True, exist_ok=True)

    # Determine output filename base
    safe_name = episode_path.name
    output_base = episode_output_dir / safe_name

    # Parse requested formats
    formats = [f.strip().lower() for f in args.formats.split(",")]

    # Generate Markdown (combined file)
    if "md" in formats:
        md_path = output_base.with_suffix(".md")
        generate_markdown(combined_markdown, episode_info, md_path)

    # Generate HTML first (needed for PDF)
    html_path = output_base.with_suffix(".html")
    if "html" in formats:
        generate_html(combined_markdown, episode_info, html_path)
    elif "pdf" in formats:
        # Still generate HTML for PDF conversion
        generate_html(combined_markdown, episode_info, html_path)

    # Generate PDF
    if "pdf" in formats:
        pdf_path = output_base.with_suffix(".pdf")
        generate_pdf(html_path, pdf_path)

    # Generate EPUB
    if "epub" in formats:
        epub_path = output_base.with_suffix(".epub")
        generate_epub(combined_markdown, episode_info, epub_path)

    # Clean up temporary HTML if not requested
    if "html" not in formats and "pdf" not in formats and html_path.exists():
        html_path.unlink()

    print(f"\n✅ Done! Output files in: {episode_output_dir}/")


if __name__ == "__main__":
    main()
