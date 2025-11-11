#!/usr/bin/env python3
"""
Episode Generator for Hockey Shuttle Series

Generates PDF, HTML, EPUB, and DOCX formats from episode markdown files
with automatic inline image insertion.

Usage:
    uv run scripts/generate_episode.py <episode-path> [--formats pdf,html,epub,docx]

Example:
    uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice
    uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice --formats html,docx
"""

import argparse
import sys
from pathlib import Path
import markdown2
import re
from datetime import datetime

# Check for optional dependencies
try:
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False

try:
    from weasyprint import HTML
    PDF_AVAILABLE = True
except (ImportError, OSError):
    PDF_AVAILABLE = False

try:
    from ebooklib import epub
    EPUB_AVAILABLE = True
except ImportError:
    EPUB_AVAILABLE = False


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate PDF, HTML, EPUB, and DOCX from episode markdown files with images"
    )
    parser.add_argument(
        "episode_path",
        type=str,
        help="Path to episode directory"
    )
    parser.add_argument(
        "--formats",
        type=str,
        default="html,epub,docx",
        help="Comma-separated list of formats (html,epub,docx,pdf). Default: html,epub,docx"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="output",
        help="Output directory. Default: output"
    )
    parser.add_argument(
        "--with-images",
        action="store_true",
        default=True,
        help="Include images in output (default: True)"
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
    """Extract episode information from path."""
    episode_name = episode_path.name
    match = re.match(r"episode-(\d+)-(.+)", episode_name)

    if match:
        episode_num = int(match.group(1))
        episode_title = match.group(2).replace("-", " ").title()
    else:
        episode_num = "1"
        episode_title = episode_name

    return {
        "series": "Hockey Shuttle",
        "season": "1",
        "episode": episode_num,
        "title": episode_title,
        "full_title": f"Hockey Shuttle - Season 1, Episode {episode_num}: {episode_title}",
        "episode_slug": episode_name
    }


def read_chapter_files(episode_path: Path):
    """Read all chapter markdown files."""
    draft_dir = episode_path / "draft"

    if not draft_dir.exists():
        print(f"❌ Error: Draft directory not found at {draft_dir}")
        return []

    chapter_files = sorted(draft_dir.glob("chapter-*.md"))

    if not chapter_files:
        print(f"❌ Error: No chapter files found in {draft_dir}")
        return []

    chapters = []
    for chapter_file in chapter_files:
        try:
            content = chapter_file.read_text()

            # Extract chapter title
            title = None
            lines = content.split("\n")
            for line in lines[:10]:
                if line.startswith("# "):
                    title = line[2:].strip()
                    break

            chapters.append({
                "filename": chapter_file.name,
                "title": title,
                "content": content
            })
        except Exception as e:
            print(f"⚠️  Warning: Could not read {chapter_file}: {e}")

    return chapters


def get_image_map(repo_root: Path):
    """Create a map of available images for automatic insertion."""
    visuals_dir = repo_root / "series" / "hockey-shuttle" / "10-visuals"

    return {
        "episode_header": visuals_dir / "episode-headers" / "ep01-returning-to-center-ice.png",
        "sophia_portrait": visuals_dir / "characters" / "sophia-chen-athlete-v1.png",
        "ethan_portrait": visuals_dir / "characters" / "ethan-price-hockey-v1.png",
        "parking_lot_reunion": visuals_dir / "key-scenes" / "ep01-parking-lot-reunion.png",
        "winnipeg_winter": visuals_dir / "key-scenes" / "the-forks-winnipeg-winter.png",
        "empty_rink": visuals_dir / "atmospheric" / "empty-rink-golden-hour.png",
        "frost_window": visuals_dir / "atmospheric" / "frost-on-window.png",
        "snow_falling": visuals_dir / "atmospheric" / "snow-falling-night.png",
        "ice_texture": visuals_dir / "atmospheric" / "ice-texture-closeup.png",
        "truck_interior": visuals_dir / "atmospheric" / "truck-interior-dashboard.png",
        "coffee_cup": visuals_dir / "atmospheric" / "coffee-cup-winter.png",
        "shuttlecock": visuals_dir / "atmospheric" / "shuttlecock-in-flight.png",
        "hockey_puck": visuals_dir / "atmospheric" / "hockey-puck-closeup.png",
        "crossed_equipment": visuals_dir / "atmospheric" / "crossed-equipment.png",
        "two_paths": visuals_dir / "atmospheric" / "two-paths-snow.png",
    }


def combine_chapters(chapters: list, episode_info: dict, include_images: bool, repo_root: Path):
    """Combine all chapters into single markdown content with optional images."""
    combined = []

    # Title page
    combined.append(f"# {episode_info['full_title']}\n")
    combined.append("---\n")

    image_map = get_image_map(repo_root) if include_images else {}

    for i, chapter in enumerate(chapters, 1):
        # Chapter heading
        if chapter["title"]:
            combined.append(f"## Chapter {i}: {chapter['title']}\n")
        else:
            combined.append(f"## Chapter {i}\n")

        # Add episode header image at start of chapter 1
        if i == 1 and include_images and image_map.get("episode_header"):
            img_path = image_map["episode_header"]
            if img_path.exists():
                combined.append(f"\n![Episode Header]({img_path})\n")

        # Add chapter content
        content = chapter["content"]
        lines = content.split("\n")

        # Skip first line if it's a title
        if lines and lines[0].startswith("# "):
            lines = lines[1:]

        combined.append("\n".join(lines).strip())
        combined.append("")

        # Add chapter-specific images based on content/position
        if include_images:
            if i == 2 and image_map.get("parking_lot_reunion"):
                # Add reunion scene in chapter 2
                img_path = image_map["parking_lot_reunion"]
                if img_path.exists():
                    combined.append(f"\n![The Reunion]({img_path})\n")

        combined.append("---\n")

    return "\n".join(combined)


def generate_html(markdown_content: str, episode_info: dict, output_path: Path):
    """Generate HTML file from markdown with images."""
    html_content = markdown2.markdown(
        markdown_content,
        extras=['fenced-code-blocks', 'tables', 'break-on-newline']
    )

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{episode_info['full_title']}</title>
    <style>
        body {{
            font-family: Georgia, 'Times New Roman', serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }}
        h1, h2, h3 {{ color: #2c3e50; }}
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 2em auto;
            border-radius: 4px;
        }}
        hr {{
            border: none;
            border-top: 1px solid #bdc3c7;
            margin: 40px 0;
        }}
        @media print {{
            body {{ max-width: 100%; }}
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""

    output_path.write_text(html_doc, encoding='utf-8')
    return True


def generate_docx(markdown_content: str, episode_info: dict, output_path: Path, image_map: dict):
    """Generate DOCX file with inline images."""
    if not DOCX_AVAILABLE:
        print("⚠️  python-docx not installed. Install with: uv pip install python-docx")
        return False

    try:
        doc = Document()

        # Set document margins
        sections = doc.sections
        for section in sections:
            section.top_margin = Inches(1)
            section.bottom_margin = Inches(1)
            section.left_margin = Inches(1)
            section.right_margin = Inches(1)

        # Title page
        title = doc.add_heading(episode_info['full_title'], 0)
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Parse markdown and add to document
        lines = markdown_content.split("\n")
        in_paragraph = False
        current_para = None

        for line in lines:
            line = line.rstrip()

            # Check for image references
            img_match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', line)
            if img_match:
                alt_text = img_match.group(1)
                img_path = Path(img_match.group(2))
                if img_path.exists():
                    try:
                        doc.add_picture(str(img_path), width=Inches(6))
                        last_paragraph = doc.paragraphs[-1]
                        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        # Add caption
                        if alt_text:
                            caption = doc.add_paragraph(alt_text)
                            caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
                            caption.runs[0].italic = True
                        doc.add_paragraph()  # Spacing
                    except Exception as e:
                        print(f"⚠️  Could not add image {img_path}: {e}")
                continue

            # Headings
            if line.startswith("# "):
                doc.add_heading(line[2:], 1)
                in_paragraph = False
            elif line.startswith("## "):
                doc.add_heading(line[3:], 2)
                in_paragraph = False
            elif line.startswith("### "):
                doc.add_heading(line[4:], 3)
                in_paragraph = False
            # Horizontal rules
            elif line.strip() == "---":
                doc.add_page_break()
                in_paragraph = False
            # Empty lines
            elif not line.strip():
                in_paragraph = False
                current_para = None
            # Regular text
            else:
                if not in_paragraph or current_para is None:
                    current_para = doc.add_paragraph()
                    in_paragraph = True
                else:
                    current_para.add_run(" ")

                # Simple markdown parsing for bold and italic
                text = line
                # Handle bold
                text = re.sub(r'\*\*([^\*]+)\*\*', lambda m: m.group(1), text)
                # Handle italic
                text = re.sub(r'\*([^\*]+)\*', lambda m: m.group(1), text)

                run = current_para.add_run(text)

                # Apply styles based on original markdown
                if "**" in line:
                    run.bold = True
                if line.startswith("*") and not line.startswith("**"):
                    run.italic = True

        doc.save(output_path)
        return True

    except Exception as e:
        print(f"❌ Error generating DOCX: {e}")
        return False


def generate_epub(markdown_content: str, episode_info: dict, output_path: Path):
    """Generate EPUB file from markdown content."""
    if not EPUB_AVAILABLE:
        print("⚠️  ebooklib not installed. Install with: uv pip install ebooklib")
        return False

    try:
        # Create EPUB book
        book = epub.EpubBook()

        # Set metadata
        book.set_identifier(f"hockey-shuttle-s{episode_info['season']}-e{episode_info['episode']}")
        book.set_title(episode_info['full_title'])
        book.set_language('en')
        book.add_author('Hockey Shuttle Series')

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
        return True

    except Exception as e:
        print(f"❌ Error generating EPUB: {e}")
        return False


def generate_pdf(html_path: Path, output_path: Path):
    """Generate PDF file from HTML."""
    if not PDF_AVAILABLE:
        print("⚠️  WeasyPrint not available. Install with: uv pip install weasyprint")
        return False

    try:
        HTML(filename=str(html_path)).write_pdf(output_path)
        return True
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return False


def main():
    """Main execution function."""
    args = parse_args()

    repo_root = find_repo_root()
    episode_path = repo_root / args.episode_path

    if not episode_path.exists():
        print(f"❌ Error: Episode path not found: {episode_path}")
        sys.exit(1)

    # Extract episode info
    episode_info = extract_episode_info(episode_path)

    print(f"\n📚 Processing: {episode_info['episode_slug']}")
    print(f"   {episode_info['full_title']}\n")

    # Read chapters
    chapters = read_chapter_files(episode_path)

    if not chapters:
        sys.exit(1)

    print(f"✓ Found {len(chapters)} chapters\n")

    # Get image map
    image_map = get_image_map(repo_root) if args.with_images else {}

    # Combine chapters with images
    markdown_content = combine_chapters(chapters, episode_info, args.with_images, repo_root)

    # Set up output directory
    output_dir = repo_root / args.output_dir / episode_info['episode_slug']
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate requested formats
    formats = [f.strip().lower() for f in args.formats.split(',')]
    generated_files = []

    for fmt in formats:
        output_file = output_dir / f"{episode_info['episode_slug']}.{fmt}"

        if fmt == 'html':
            if generate_html(markdown_content, episode_info, output_file):
                print(f"✅ Generated HTML: {output_file}")
                generated_files.append(output_file)

        elif fmt == 'docx' or fmt == 'doc':
            if DOCX_AVAILABLE:
                if generate_docx(markdown_content, episode_info, output_file.with_suffix('.docx'), image_map):
                    print(f"✅ Generated DOCX: {output_file.with_suffix('.docx')}")
                    generated_files.append(output_file.with_suffix('.docx'))
            else:
                print(f"⚠️  Skipping DOCX: python-docx not installed")
                print(f"   Install with: uv pip install python-docx")

        elif fmt == 'epub':
            if EPUB_AVAILABLE:
                if generate_epub(markdown_content, episode_info, output_file):
                    print(f"✅ Generated EPUB: {output_file}")
                    generated_files.append(output_file)
            else:
                print(f"⚠️  Skipping EPUB: ebooklib not installed")
                print(f"   Install with: uv pip install ebooklib")

        elif fmt == 'pdf':
            # Generate HTML first if not already done
            html_file = output_dir / f"{episode_info['episode_slug']}.html"
            if not html_file.exists():
                generate_html(markdown_content, episode_info, html_file)

            if PDF_AVAILABLE:
                if generate_pdf(html_file, output_file):
                    print(f"✅ Generated PDF: {output_file}")
                    generated_files.append(output_file)
            else:
                print(f"⚠️  Skipping PDF: WeasyPrint not available")

        else:
            print(f"⚠️  Unknown format: {fmt}")

    print(f"\n✨ Done! Generated {len(generated_files)} files")
    print(f"📁 Output directory: {output_dir}\n")


if __name__ == "__main__":
    main()
