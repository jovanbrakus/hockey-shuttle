# Episode Generation Scripts

This directory contains scripts for generating various output formats from episode markdown files.

## Setup

Install dependencies using uv:

```bash
# From the repository root
uv sync
```

This will install:
- `markdown` - Markdown to HTML conversion
- `weasyprint` - PDF generation from HTML
- `ebooklib` - EPUB generation

## Usage

### Generate Episode Files

Generate MD, PDF, HTML, and EPUB files from an episode directory:

```bash
# Generate all formats (MD, PDF, HTML, EPUB)
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice

# Generate specific formats only
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice --formats md,html

# Generate markdown only (combined single file)
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice --formats md

# Specify custom output directory
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice --output-dir my-output
```

### Command Options

- `episode_path` (required): Path to episode directory containing `draft/` folder with chapter markdown files
- `--formats`: Comma-separated list of formats to generate (options: `md`, `pdf`, `html`, `epub`). Default: all formats
- `--output-dir`: Output directory path relative to repo root. Default: `output`

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
├── episode-01-returning-to-center-ice.md    # Combined markdown file
├── episode-01-returning-to-center-ice.pdf
├── episode-01-returning-to-center-ice.html
└── episode-01-returning-to-center-ice.epub
```

## Examples

### Generate Episode 1 (all formats)
```bash
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice
```

Output:
```
📚 Processing episode: episode-01-returning-to-center-ice
   Hockey Shuttle - Season 1, Episode 1: Returning To Center Ice

Found 4 chapters
✓ Generated Markdown: output/episode-01-returning-to-center-ice.md
✓ Generated HTML: output/episode-01-returning-to-center-ice.html
✓ Generated PDF: output/episode-01-returning-to-center-ice.pdf
✓ Generated EPUB: output/episode-01-returning-to-center-ice.epub

✅ Done! Output files in: output/
```

### Generate Markdown only (combined single file)
```bash
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-02-new-lines --formats md
```

### Generate PDF only
```bash
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-02-new-lines --formats pdf
```

### Generate HTML and EPUB
```bash
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-03-defensive-zone --formats html,epub
```

### Generate Markdown and HTML (no EPUB/PDF)
```bash
uv run scripts/generate_episode.py series/hockey-shuttle/season-01/episode-04-matchup --formats md,html
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
# From repository root
for episode in series/hockey-shuttle/season-01/episode-*/; do
    uv run scripts/generate_episode.py "$episode"
done
```

Or create a batch script:

```bash
#!/bin/bash
# scripts/generate_all.sh

EPISODES=(
    "series/hockey-shuttle/season-01/episode-01-returning-to-center-ice"
    "series/hockey-shuttle/season-01/episode-02-new-lines"
    "series/hockey-shuttle/season-01/episode-03-defensive-zone"
    # Add more episodes...
)

for episode in "${EPISODES[@]}"; do
    echo "Generating $episode..."
    uv run scripts/generate_episode.py "$episode"
done

echo "All episodes generated!"
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
