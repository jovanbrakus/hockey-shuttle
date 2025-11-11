# Wattpad Publishing Scripts

## Main Script: `compose_for_wattpad.py`

**Purpose:** Generate DOCX files with formatting and images for Wattpad publishing.

### Why DOCX?

DOCX files preserve formatting when copy-pasted into Wattpad:
- ✅ **Bold** and *italic* text work perfectly
- ✅ Inline images paste directly
- ✅ Line breaks and spacing preserved
- ✅ Scene breaks stay centered
- ✅ Zero manual reformatting needed

### Usage

```bash
# Generate DOCX files for an episode
uv run scripts/compose_for_wattpad.py series/hockey-shuttle/season-01/episode-01-returning-to-center-ice
```

### Output

Creates individual chapter DOCX files in `output/wattpad/<episode-name>/`:
- chapter-01.docx
- chapter-02.docx
- chapter-03.docx
- chapter-04.docx

Each file includes:
- Chapter header with episode info
- 3-4 inline images (automatically placed)
- Full chapter text with bold/italic formatting
- Scene breaks as centered * * *
- Chapter footer with vote/comment CTA

### Images Included

**Chapter 1:** Episode header, ice texture, empty rink
**Chapter 2:** Winnipeg winter, snow falling, parking lot reunion, frost window
**Chapter 3:** Shuttlecock, truck interior, coffee cup
**Chapter 4:** Empty rink, hockey puck, crossed equipment

### How to Use DOCX Files

1. Open DOCX file in Microsoft Word
2. Select All (Cmd+A / Ctrl+A)
3. Copy (Cmd+C / Ctrl+C)
4. Paste into Wattpad chapter editor
5. Publish!

---

## Other Scripts

**create_aesthetics_playlist.py** - Generates intro chapter with character grids and playlist

---

**Last Updated:** November 11, 2024
