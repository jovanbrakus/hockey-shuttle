#!/bin/bash
# Generate all The Boy Who Knew Me First Season 1 episodes in all formats

EPISODES=(
    "series/hockey-shuttle/season-01/episode-01-returning-to-center-ice"
    "series/hockey-shuttle/season-01/episode-02-new-lines"
    "series/hockey-shuttle/season-01/episode-03-defensive-zone"
    "series/hockey-shuttle/season-01/episode-04-matchup"
    "series/hockey-shuttle/season-01/episode-05-storm-warning"
    "series/hockey-shuttle/season-01/episode-06-the-weight"
    "series/hockey-shuttle/season-01/episode-07-spring-training"
    "series/hockey-shuttle/season-01/episode-08-recruiting-season"
    "series/hockey-shuttle/season-01/episode-09-championship-weekend"
    "series/hockey-shuttle/season-01/episode-10-commence"
)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "🏒 The Boy Who Knew Me First - Season 1 Episode Generation"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

for episode in "${EPISODES[@]}"; do
    echo "📚 Generating: $episode"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    "$SCRIPT_DIR/generate-episode.sh" "$episode"
    echo ""
done

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ All ${#EPISODES[@]} episodes generated!"
echo "📁 Output location: output/"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
