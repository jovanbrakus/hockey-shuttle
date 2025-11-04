#!/bin/bash

# Episodic Series Setup Script
# Usage: ./setup-series.sh "series-01-title-here"

if [ -z "$1" ]; then
    echo "Usage: ./setup-series.sh \"series-01-title-here\""
    exit 1
fi

SERIES_DIR="series/$1"

echo "🎬 Creating episodic series structure for: $1"

# Create main directory structure
mkdir -p "$SERIES_DIR"/{00-series-bible,01-world/{locations,systems},02-characters/{main-cast,recurring,guest-stars,families},10-visuals/{series-art,characters,marketing},11-production}

# Create Season 1 structure with 10 episodes
for i in {01..10}; do
    if [ "$i" = "10" ]; then
        ep_name="episode-$i-season-finale"
    else
        ep_name="episode-$i"
    fi
    mkdir -p "$SERIES_DIR/season-01/$ep_name"/{draft,visuals}
done

# Create season planning folder
mkdir -p "$SERIES_DIR/season-01/00-season-arc"

# Create series bible documents
cat > "$SERIES_DIR/00-series-bible/series-overview.md" << 'EOF'
# [Series Title] - Series Bible

## Core Concept
**Logline:** [One sentence that captures the entire series]
**Genre:** YA [genre]
**Tone:** [Dark/Light/Comedic/Dramatic]
**Comparison:** "It's like [Show A] meets [Show B]"

## Series Arc (Multi-Season Vision)
### Season 1: [Theme/Arc Title]
- Main conflict:
- Character journey:
- Ending:

### Season 2: [Theme/Arc Title]
- Escalation:
- New elements:
- Deeper mysteries:

### Season 3: [Theme/Arc Title]
- Ultimate stakes:
- Final transformations:
- Series resolution:

## World Rules
1. [Core rule that defines the world]
2. [Limitation that creates conflict]
3. [Unique element that sets it apart]

## Recurring Themes
- Identity and belonging
- Power and responsibility
- Truth vs. perception
- [Specific to your series]

## Target Audience
- Primary: Ages 14-18
- Secondary: YA readers who love binge-reading
- Appeal factors: [What draws them in]

## Unique Selling Points
- [What makes this series special]
- [Why readers will binge]
- [What they'll discuss online]
EOF

cat > "$SERIES_DIR/00-series-bible/season-plans.md" << 'EOF'
# Season Planning Overview

## Season 1: [Arc Title]
**Episodes:** 10
**Main Antagonist:** 
**Central Mystery:**
**Character Focus:**
**Ending:** Resolution with major cliffhanger

### Episode Progression
1. **Pilot** - World introduction, inciting incident
2. **Deepening** - Expand world, develop relationships
3. **First Victory** - Small win, false confidence
4. **Complication** - Things get worse
5. **Midseason Twist** - Game-changing revelation
6. **Aftermath** - Dealing with revelation
7. **Regrouping** - New plan, new hope
8. **Escalation** - Stakes rising
9. **Darkest Hour** - Everything falls apart
10. **Season Finale** - Climax and mega-cliffhanger

## Season 2: [Arc Title]
**New Elements:**
**Raised Stakes:**
**Character Evolution:**

## Season 3: [Arc Title]
**Final Conflict:**
**Ultimate Stakes:**
**Series Resolution:**
EOF

# Create world documents
cat > "$SERIES_DIR/01-world/world-overview.md" << 'EOF'
# World Overview

## Setting
**Where:** [City/Town/Region]
**When:** [Contemporary/Historical/Future]
**Scope:** [Local/National/Global/Universal]

## Key Locations
### Recurring Sets (Used Multiple Episodes)
1. **[Location Name]**
   - Purpose:
   - Atmosphere:
   - Significance:

2. **[Location Name]**
   - Purpose:
   - Atmosphere:
   - Significance:

### Episode-Specific Locations
- Listed per episode as needed

## World Rules
### Physical Rules
- [How the world works differently]

### Social Rules
- [Power structures]
- [Social hierarchies]

### Magical/Tech Rules (if applicable)
- [How the special element works]
- [Limitations]
- [Costs]

## Timeline
### Ancient History
- [Relevant backstory]

### Recent Past
- [Events affecting current story]

### Series Timeline
- Episode 1: [Date/Season]
- Episode 10: [Date/Season]
- Between seasons: [Time gap]
EOF

# Create character templates
cat > "$SERIES_DIR/02-characters/main-cast/protagonist.md" << 'EOF'
# [Protagonist Name]

## Series Overview
**Role:** Main protagonist
**Age:** [Age at series start]
**Appears:** Every episode

## Character Concept
**One-line description:**
**Archetype:**
**What makes them unique:**

## Physical Description
- Height/Build:
- Hair/Eyes:
- Distinguishing features:
- Style evolution:

## Personality
### Core Traits
- [Trait 1 with example]
- [Trait 2 with example]
- [Trait 3 with example]

### Strengths
-
-

### Flaws
-
-

### Fears
-
-

## Backstory
### Family
- Parents:
- Siblings:
- Key relationships:

### History
- Childhood:
- Trauma/Ghost:
- Secrets:

## Series Arc
### Season 1 Journey
- **Episode 1:** Starting point
- **Episode 5:** Midseason state
- **Episode 10:** Season end state

### Season 2 Journey
- Growth direction:
- New challenges:

### Season 3 Journey
- Ultimate transformation:
- Final state:

## Relationships
### [Character Name]
- Starting dynamic:
- Evolution:
- Key moments:

### [Character Name]
- Starting dynamic:
- Evolution:
- Key moments:

## Voice
### Speech Patterns
- Vocabulary:
- Catchphrases:
- Verbal tics:

### Internal Monologue
- Thought patterns:
- Self-perception:
- Running worries:

## Episode Moments
### Season 1 Highlights
- Episode 1:
- Episode 5:
- Episode 10:

## Growth Metrics
- What they want (external):
- What they need (internal):
- Lie they believe:
- Truth they'll learn:
EOF

# Create season arc planning
cat > "$SERIES_DIR/season-01/00-season-arc/season-outline.md" << 'EOF'
# Season 1 Overview

## Season Arc
**Title:** [Season Arc Title]
**Core Conflict:**
**Central Mystery:**
**Antagonist:**
**Stakes:**

## Three-Act Structure
### Act 1 (Episodes 1-3): Setup
- Introduce world and rules
- Establish character dynamics
- Launch central mystery
- First encounter with antagonist

### Act 2A (Episodes 4-6): Development
- Deepen relationships
- Complicate initial mystery
- Midseason revelation
- Power dynamics shift

### Act 2B (Episodes 7-9): Escalation
- Stakes get personal
- Betrayals and reveals
- Plans fall apart
- Rush toward finale

### Act 3 (Episode 10): Resolution
- Climactic confrontation
- Season mystery resolved
- Character arcs complete
- Mega-cliffhanger for Season 2

## Episode-by-Episode Breakdown

### Episode 1: [Title]
**Logline:**
**A-Plot:**
**B-Plot:**
**Cliffhanger Type:**

### Episode 2: [Title]
**Logline:**
**A-Plot:**
**B-Plot:**
**Cliffhanger Type:**

[Continue for all 10 episodes]

## Season Threads
### Mystery Thread
- Ep 1: Question introduced
- Ep 3: First clue
- Ep 5: Major revelation
- Ep 7: Misdirection
- Ep 10: Truth revealed

### Relationship Thread
- Ep 1: Meet
- Ep 4: Bond
- Ep 6: Test
- Ep 8: Break
- Ep 10: Transform

### Power Thread
- Ep 1: Discover
- Ep 3: Experiment
- Ep 5: Consequences
- Ep 8: Master
- Ep 10: Price
EOF

cat > "$SERIES_DIR/season-01/00-season-arc/cliffhanger-map.md" << 'EOF'
# Season 1 Cliffhanger Map

## Cliffhanger Variety Plan
1. **Episode 1:** Revelation - World bigger than expected
2. **Episode 2:** Arrival - Mysterious figure appears
3. **Episode 3:** Danger - First real threat
4. **Episode 4:** Betrayal - Trust shattered
5. **Episode 5:** Transformation - Game-changing event
6. **Episode 6:** Choice - Shocking decision
7. **Episode 7:** Loss - Something precious taken
8. **Episode 8:** Revelation - True enemy revealed
9. **Episode 9:** Danger - Everyone at risk
10. **Episode 10:** Mega - Resolution + Season 2 setup

## Cliffhanger Connections
- Episode 1 → 2: Direct continuation
- Episode 2 → 3: Time jump with consequences
- Episode 3 → 4: Aftermath focus
- Episode 4 → 5: Character reaction
- Episode 5 → 6: New world state
- Episode 6 → 7: Dealing with choice
- Episode 7 → 8: Investigation/hunt
- Episode 8 → 9: Preparation
- Episode 9 → 10: Race against time

## Setup Tracking
### Episode 1 Cliffhanger
- Setup moment: Page 10
- Misdirection: Page 35
- Foreshadowing: Page 55
- Reveal: Page 78-80

[Repeat for each episode]
EOF

# Create episode template
for i in {01..10}; do
    if [ "$i" = "10" ]; then
        ep_name="episode-$i-season-finale"
    else
        ep_name="episode-$i"
    fi
    
    cat > "$SERIES_DIR/season-01/$ep_name/outline.md" << EOF
# Episode $i: [Episode Title]

## Episode Info
**Season:** 1
**Episode:** $i
**Length:** 80 pages (20,000 words)
**POV:** [Character name]

## Episode Summary
**Logline:** [One sentence describing the episode]

## Three-Plot Structure
### A-Plot (60% - ~48 pages)
**Main Story:**
**Conflict:**
**Resolution:**

### B-Plot (25% - ~20 pages)
**Character Story:**
**Emotional Arc:**
**Growth:**

### C-Plot (15% - ~12 pages)
**Series Arc:**
**Mystery Advanced:**
**Setup for Future:**

## Four-Chapter Breakdown

### Chapter 1 (Pages 1-20): [Chapter Title]
**Cold Open (1-2):**
**Previously On (3):**
**Setup (4-15):**
**Complication (16-19):**
**Mini-cliff (20):**

### Chapter 2 (Pages 21-40): [Chapter Title]
**Development (21-30):**
**B-Plot Introduction (31-35):**
**Revelation (36-39):**
**Mini-cliff (40):**

### Chapter 3 (Pages 41-60): [Chapter Title]
**Escalation (41-50):**
**Convergence (51-55):**
**Crisis Point (56-59):**
**Mini-cliff (60):**

### Chapter 4 (Pages 61-80): [Chapter Title]
**Confrontation (61-70):**
**False Resolution (71-75):**
**Twist Setup (76-78):**
**Cliffhanger (79-80):**

## Cliffhanger
**Type:** [Revelation/Danger/Betrayal/etc.]
**Setup:** Page [X]
**Misdirection:** Page [Y]
**Reveal:** Page 79-80
**Impact:** [What changes]

## Continuity Notes
### From Previous Episodes
-
-

### For Future Episodes
-
-

## Key Dialogue
**Important Lines:**
-
-

## Visual Moments
**Scenes needing illustration:**
-
-
EOF

    # Create chapter templates
    for chapter in {1..4}; do
        cat > "$SERIES_DIR/season-01/$ep_name/draft/chapter-0$chapter.md" << EOF
# Episode $i - Chapter $chapter

## Chapter Info
**Pages:** $((($chapter-1)*20+1))-$(($chapter*20))
**Word Count Target:** ~5,000 words

---

[Chapter content begins here]

---

## Revision Notes
- [ ] Pacing checked
- [ ] Cliffhanger setup included
- [ ] Character voices consistent
- [ ] Plot threads advanced
EOF
    done
done

# Create production templates
cat > "$SERIES_DIR/11-production/series-metadata.yaml" << 'EOF'
# Series Metadata

series_title: Your Series Title
author: Your Name
genre: Young Adult [Genre]
status: In Development

seasons:
  - season: 1
    episodes: 10
    status: Planning/Writing/Complete
    release_schedule: Weekly/Biweekly/Monthly

episode_format:
  length: 80 pages
  word_count: 20000
  chapters: 4
  reading_time: "1-1.5 hours"

publishing:
  format: 
    - EPUB
    - PDF
    - Web Serial
  platforms:
    - Kindle Vella
    - Radish Fiction
    - Wattpad
    - Substack

visual_style:
  covers: Consistent series branding
  episode_art: Individual episode covers
  interior: Chapter illustrations optional
EOF

# Create README
cat > "$SERIES_DIR/README.md" << 'EOF'
# Episodic Series Project

## Structure Overview
This is an episodic YA series with:
- **10 episodes per season**
- **80 pages per episode**
- **Cliffhanger endings**
- **Binge-worthy pacing**

## Quick Start
1. Complete world-building in `01-world/`
2. Develop full cast in `02-characters/`
3. Plan Season 1 arc in `season-01/00-season-arc/`
4. Write episodes in order
5. Track cliffhangers carefully

## Episode Writing Process
1. Review season arc
2. Plan three plot threads (A/B/C)
3. Structure four 20-page chapters
4. Write draft with mini-cliffhangers
5. Engineer final cliffhanger
6. Check continuity
7. Generate episode cover

## Publishing Strategy
- Release Episode 1-3 together (hook readers)
- Then weekly/biweekly releases
- Season finale special release
- Complete season bundle

## Success Metrics
- [ ] Readers finish episodes in one sitting
- [ ] Cliffhangers generate discussion
- [ ] Binge-reading reported
- [ ] Demands for next season
- [ ] Fan theories circulating

Remember: You're creating Netflix for books!
EOF

echo "✅ Episodic series structure created successfully!"
echo ""
echo "📁 Directory structure:"
echo "   $SERIES_DIR/"
echo "   ├── 00-series-bible/     (Multi-season planning)"
echo "   ├── 01-world/           (Complete world-building)"
echo "   ├── 02-characters/      (Full cast development)"
echo "   ├── season-01/"
echo "   │   ├── 00-season-arc/  (Season planning)"
echo "   │   ├── episode-01/     (80-page episode)"
echo "   │   ├── episode-02/"
echo "   │   ├── ..."
echo "   │   └── episode-10-season-finale/"
echo "   ├── 10-visuals/         (Artwork and covers)"
echo "   └── 11-production/      (Publishing files)"
echo ""
echo "📝 Next steps:"
echo "1. Fill out series bible in 00-series-bible/"
echo "2. Build your world in 01-world/"
echo "3. Create full cast in 02-characters/"
echo "4. Plan Season 1 arc and cliffhangers"
echo "5. Write Episode 1 (remember: hook in 2 pages!)"
echo "6. Test with beta readers for binge factor"
echo ""
echo "💡 Pro tip: Write first 3 episodes before releasing any!"
