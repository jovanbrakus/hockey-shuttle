#!/usr/bin/env python3
"""Check metadata for all PDF and ePub files in downloads folder."""

import subprocess
import os
from pathlib import Path

downloads_dir = Path("/Users/jovan/personal/book-series/website/src/downloads")

print("=" * 80)
print("PDF METADATA ANALYSIS")
print("=" * 80)

pdf_files = sorted(downloads_dir.glob("*.pdf"))
for pdf_file in pdf_files:
    print(f"\n📄 {pdf_file.name}")
    print("-" * 80)

    result = subprocess.run(
        ["exiftool", str(pdf_file)],
        capture_output=True,
        text=True
    )

    # Filter relevant metadata
    for line in result.stdout.split('\n'):
        if any(keyword in line for keyword in ['Author', 'Creator', 'Producer', 'Title', 'Subject', 'Keywords', 'PDF Version']):
            print(f"  {line.strip()}")

print("\n" + "=" * 80)
print("EPUB METADATA ANALYSIS")
print("=" * 80)

epub_files = sorted(downloads_dir.glob("*.epub"))
for epub_file in epub_files:
    print(f"\n📚 {epub_file.name}")
    print("-" * 80)

    # ePub files are ZIP archives, check content.opf file
    result = subprocess.run(
        ["unzip", "-p", str(epub_file), "EPUB/content.opf"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        # Extract metadata from OPF file
        for line in result.stdout.split('\n'):
            if any(tag in line for tag in ['<dc:creator', '<dc:title', '<dc:publisher', '<dc:contributor', '<meta name="generator']):
                print(f"  {line.strip()}")
    else:
        print("  [Could not read ePub metadata]")

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Total PDFs analyzed: {len(pdf_files)}")
print(f"Total ePubs analyzed: {len(epub_files)}")
