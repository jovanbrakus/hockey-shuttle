# Episode Generation Scripts

This directory contains scripts for generating various output formats from episode markdown files.

## Setup

Install dependencies using uv:

```bash
# From the repository root
uv sync
```

This will install:
- `markdown2` - Markdown to HTML conversion
- `python-docx` - DOCX generation with images
- `weasyprint` - PDF generation from HTML (optional)
- `ebooklib` - EPUB generation

## Usage

### Generate Episode Files

Generate combined episode files in multiple formats with inline images:

```bash
# Generate default formats (HTML, EPUB, DOCX) with images
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice

# Generate specific formats only
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice --formats html,docx

# Generate all formats including PDF
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice --formats html,epub,docx,pdf
```

### Command Options

- `episode_path` (required): Path to episode directory containing `draft/` folder with chapter markdown files
- `--formats`: Comma-separated list of formats to generate (options: `html`, `epub`, `docx`, `pdf`). Default: `html,epub,docx`
- `--output-dir`: Output directory path relative to repo root. Default: `output`
- `--with-images`: Include inline images in output (default: True)

## Episode Structure

The script expects episodes to follow this structure:

```
episode-XX-title/
├── outline.md           # Optional: Contains series/season metadata
└── draft/
    ├── chapter-01.md    # Required: Chapter markdown files
    ├── chapter-02.md
    ├── chapter-03.md
    └── chapter-04.md
```

### Chapter Markdown Format

Each chapter file should be standard markdown with an optional title:

```markdown
# Chapter Title

Chapter content here...

More content...
```

## Output

Generated files are placed in the `output/` directory (or custom directory if specified) with the naming convention:

```
output/
└── episode-01-returning-to-center-ice/           # Episode-specific subfolder
    ├── episode-01-returning-to-center-ice.html  # Styled HTML with images (119 KB)
    ├── episode-01-returning-to-center-ice.docx  # Word document with images (3.2 MB)
    ├── episode-01-returning-to-center-ice.epub  # E-reader format (64 KB)
    └── episode-01-returning-to-center-ice.pdf   # Print-ready PDF (optional)
```

## Examples

### Generate Episode 1 (default formats)
```bash
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice
```

Output:
```
📚 Processing: episode-01-returning-to-center-ice
   Hockey Shuttle - Season 1, Episode 1: Returning To Center Ice

✓ Found 4 chapters

✅ Generated HTML: output/episode-01-returning-to-center-ice/episode-01-returning-to-center-ice.html
✅ Generated DOCX: output/episode-01-returning-to-center-ice/episode-01-returning-to-center-ice.docx
✅ Generated EPUB: output/episode-01-returning-to-center-ice/episode-01-returning-to-center-ice.epub

✨ Done! Generated 3 files
📁 Output directory: output/episode-01-returning-to-center-ice/
```

### Generate HTML and DOCX only
```bash
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-02-new-lines --formats html,docx
```

### Generate all formats including PDF
```bash
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-03-defensive-zone --formats html,epub,docx,pdf
```

## Troubleshooting

### Missing Dependencies

If you see warnings about missing libraries:

```
⚠ Warning: weasyprint not installed. PDF generation skipped.
  Install with: uv pip install weasyprint
```

Run `uv sync` from the repository root to install all dependencies.

### No Chapter Files Found

If you see:
```
Error: No chapter files found in draft/
```

Ensure your episode directory has a `draft/` subdirectory containing `chapter-*.md` files.

### WeasyPrint Installation Issues

WeasyPrint requires system libraries. On macOS:

```bash
brew install pango
```

On Linux:
```bash
sudo apt-get install libpango-1.0-0 libpangocairo-1.0-0
```

## Batch Processing

To generate files for all episodes:

```bash
# From repository root - generate all episodes
for episode in series/hockey-shuttle/season-01/episode-*/; do
    ./scripts/generate-episode.sh "$episode"
done
```

Or create a batch script:

```bash
#!/bin/bash
# scripts/generate-all-episodes.sh

EPISODES=(
    "series/hockey-shuttle/season-01/episode-01-returning-to-center-ice"
    "series/hockey-shuttle/season-01/episode-02-new-lines"
    "series/hockey-shuttle/season-01/episode-03-defensive-zone"
    "series/hockey-shuttle/season-01/episode-04-matchup"
    "series/hockey-shuttle/season-01/episode-05-storm-warning"
    "series/hockey-shuttle/season-01/episode-06-the-weight"
    "series/hockey-shuttle/season-01/episode-07-spring-training"
    "series/hockey-shuttle/season-01/episode-08-recruiting-season"
    # Add episodes 9-10 when complete
)

for episode in "${EPISODES[@]}"; do
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Generating: $episode"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    ./scripts/generate-episode.sh "$episode"
    echo ""
done

echo "✅ All episodes generated!"
```

Make it executable and run:

```bash
chmod +x scripts/generate-all-episodes.sh
./scripts/generate-all-episodes.sh
```

## Output Styling

### HTML Styling

The HTML output includes embedded CSS for:
- Readable serif font (Georgia)
- Proper margins and line spacing
- Chapter headings with colored underlines
- Print-friendly media queries

### PDF Styling

PDF files inherit HTML styling via WeasyPrint, producing:
- Professional book-like formatting
- Proper page breaks
- Embedded fonts

### EPUB Styling

EPUB files include basic styling suitable for e-readers:
- Reflowable text
- Chapter navigation
- E-reader compatible formatting

## Advanced Usage

### Custom Styling

To customize HTML/PDF styling, edit the CSS in `generate_episode.py` within the `generate_html()` function.

### Adding Metadata

Episode metadata is automatically extracted from:
- Episode directory name (episode number and title)
- `outline.md` file (series name, season number)

### Cover Images

To add cover images to EPUBs, modify the `generate_epub()` function to include image files.

## Support

For issues or questions:
1. Check that all dependencies are installed: `uv sync`
2. Verify episode structure matches expected format
3. Review error messages for specific issues
4. Check system requirements for WeasyPrint

## License

Part of the Hockey Shuttle series project.
