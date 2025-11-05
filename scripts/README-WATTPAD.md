# Wattpad Episode Composer

A Python script for composing Hockey Shuttle episodes into a format optimized for Wattpad publishing.

## Features

- ✅ Formats episodes for Wattpad's mobile-friendly reading experience
- ✅ Supports individual chapter files or combined episodes
- ✅ Adds episode/chapter metadata headers
- ✅ Converts markdown formatting to Wattpad-compatible style
- ✅ Includes reader engagement prompts (votes, comments)
- ✅ Generates manifest files with word counts
- ✅ Handles scene breaks and formatting automatically

## Usage

### Generate Individual Chapters (Recommended for Wattpad)

```bash
uv run scripts/compose_for_wattpad.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice
```

This creates separate `.txt` files for each chapter in the `wattpad/` directory.

### Generate Combined Episode

```bash
uv run scripts/compose_for_wattpad.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice --combine
```

This creates a single file with all chapters combined.

### Show Word Counts

```bash
uv run scripts/compose_for_wattpad.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice --word-count
```

### Custom Output Directory

```bash
uv run scripts/compose_for_wattpad.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice --output-dir my-wattpad-files
```

## Output Structure

### Individual Chapters Mode (Default)

```
output/wattpad/
└── episode-01-returning-to-center-ice/
    ├── chapter-01.txt
    ├── chapter-02.txt
    ├── chapter-03.txt
    ├── chapter-04.txt
    └── MANIFEST.txt
```

### Combined Mode

```
output/wattpad/
└── episode-01-returning-to-center-ice-complete.txt
```

## Wattpad Formatting

The script automatically:

1. **Headers** - Converts to bold text for mobile readability
2. **Scene Breaks** - Uses centered asterisks (* * *)
3. **Metadata** - Adds episode/chapter information with decorative borders
4. **Footers** - Includes engagement prompts (vote ⭐ and comment 💬)
5. **Chapter Titles** - Formatted as decorative headers

## Publishing Tips

When uploading to Wattpad:

1. **Upload chapters separately** for better reader engagement
2. **Add a cover image** (recommended size: 512x800px)
3. **Use descriptive tags** (#YA #Romance #Hockey #Sports)
4. **Write a compelling description**
5. **Add trigger warnings** if needed
6. **Engage with readers** in comments
7. **Maintain a consistent posting schedule**

## Example Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hockey Shuttle - S1E1
Chapter 1
Chapter 1: Then
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Age 9 - Millbrook Community Rink - March**

The ice was perfect that morning.

Sophia Chen knew ice the way other kids knew their favorite books...

[... chapter content ...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

To be continued...

Don't forget to vote ⭐ and comment 💬

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `episode_path` | Path to episode directory | Required |
| `--output-dir` | Custom output directory | `output/wattpad` |
| `--combine` | Combine all chapters into one file | `false` |
| `--add-metadata` | Add episode/chapter headers | `true` |
| `--word-count` | Display word counts | `false` |

## Manifest File

Each episode generates a `MANIFEST.txt` file containing:

- Episode title and metadata
- Number of chapters
- Total word count
- Generation timestamp
- List of chapter files

Example:

```
Episode: Hockey Shuttle - S1E1: Returning To Center Ice
Chapters: 4
Total Words: 18,621
Generated: November 05, 2025 at 10:15 AM

Chapter Files:
  1. chapter-01.txt
  2. chapter-02.txt
  3. chapter-03.txt
  4. chapter-04.txt
```

## Batch Processing

To process all episodes in a season:

```bash
# Process each episode individually
for ep in series/hockey-shuttle/season-01/episode-*/; do
    uv run scripts/compose_for_wattpad.py "$ep" --word-count
done
```

## See Also

- `generate_episode.py` - Generate PDF, HTML, and EPUB formats
- `generate-episode.sh` - Shell script for episode generation
- `generate-all-episodes.sh` - Batch process all episodes

## Support

For issues or questions about the Wattpad composer, check the main project README or open an issue on GitHub.

---

**Happy Publishing! 🏒✨**
