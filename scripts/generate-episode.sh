#!/bin/bash
# Wrapper script for generate_episode.py that sets up library paths for PDF generation

# Set library path for WeasyPrint PDF generation (macOS Homebrew)
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS with Homebrew
    if command -v brew &> /dev/null; then
        export DYLD_LIBRARY_PATH="$(brew --prefix)/lib:$DYLD_LIBRARY_PATH"
    fi
fi

# Run the Python script with all arguments passed through
uv run python "$(dirname "$0")/generate_episode.py" "$@"
