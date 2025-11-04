# YA Writing System - Complete Package

## 📚 System Overview
A comprehensive system for writing Young Adult books and episodic series using AI agents.

## 📦 Package Contents

### 1. Configuration Files (`/config`)
- **claude.md** - Original book writing configuration
- **claude-episodic.md** - Episodic series configuration

### 2. Agent Files (`/agents`)

#### Core Writing Agents
- **story-architect.md** - Plot structure and pacing
- **character-psychologist.md** - Character development
- **world-builder.md** - Settings and world-building
- **prose-stylist.md** - Language and writing style
- **teen-culture-consultant.md** - Contemporary teen authenticity
- **emotional-choreographer.md** - Emotional beats and tension
- **developmental-editor.md** - Big-picture analysis

#### Specialist Agents
- **dialogue-coach.md** - Dialogue and character voices
- **romance-specialist.md** - Romantic subplots
- **sensitivity-reader.md** - Inclusive representation
- **authenticity-editor.md** - Eliminate AI patterns
- **visual-artist.md** - Cover and illustration prompts

#### Episodic Series Agents
- **episode-writer.md** - 80-page episode structure
- **cliffhanger-engineer.md** - Episode endings
- **continuity-tracker.md** - Series consistency

### 3. Scripts (`/scripts`)
- **setup-book.sh** - Initialize book project structure
- **setup-series.sh** - Initialize episodic series structure
- **book-builder.py** - Convert to EPUB/PDF with images

### 4. Guides (`/guides`)
- **book-production-guide.md** - Complete publishing guide

## 🚀 Quick Start

### For Traditional Books:
```bash
# 1. Make script executable
chmod +x scripts/setup-book.sh

# 2. Create new book project
./scripts/setup-book.sh "book-01-my-title"

# 3. Copy agents to Claude Code
# 4. Start writing with agents
```

### For Episodic Series:
```bash
# 1. Make script executable
chmod +x scripts/setup-series.sh

# 2. Create new series project
./scripts/setup-series.sh "series-01-my-series"

# 3. Use episodic agents for 80-page episodes
# 4. Focus on cliffhangers!
```

## 📁 Project Structure

### Traditional Book Structure:
```
books/book-01-title/
├── 00-planning/
├── 01-world/
├── 02-characters/
├── 03-plot/
├── 04-themes/
├── 05-research/
├── 06-drafts/
├── 07-revisions/
├── 08-marketing/
├── 09-admin/
├── 10-visuals/
└── 11-production/
```

### Episodic Series Structure:
```
series/series-01-title/
├── 00-series-bible/
├── 01-world/
├── 02-characters/
├── season-01/
│   ├── episode-01/
│   ├── episode-02/
│   └── episode-10-finale/
├── 10-visuals/
└── 11-production/
```

## 🎯 Using the Agents

### In Claude Code:
1. Copy all `.md` files from `/agents` to your project
2. Reference agents with commands like:
   - "Story Architect: Review my plot outline"
   - "Character Psychologist: Develop my protagonist"
   - "Visual Artist: Create cover prompts"
   - "Episode Writer: Structure Episode 1"

### Agent Specializations:

#### For Books (200-300 pages):
- Use traditional structure agents
- Focus on complete character arcs
- Single satisfying ending

#### For Episodes (80 pages):
- Use Episode Writer for structure
- Use Cliffhanger Engineer for endings
- Use Continuity Tracker for series consistency
- Create 10 episodes per season

## 🎨 Visual Assets

### Using Visual Artist:
1. Generate prompts with Visual Artist agent
2. Use prompts in MidJourney/Stable Diffusion
3. Save images to `/10-visuals/generated-art/`
4. Supported: JPG and PNG formats

### Image Categories:
- Cover art (1600x2400px minimum)
- Chapter illustrations
- Character portraits
- Maps and locations
- Marketing materials

## 📖 Book Production

### Using book-builder.py:
```bash
# Install dependencies
pip install ebooklib weasyprint pillow markdown2 pyyaml

# Initialize metadata
python scripts/book-builder.py books/book-01 --init

# Build book with images
python scripts/book-builder.py books/book-01

# Output: EPUB and PDF in /11-production/output/
```

## 💡 Key Features

### Traditional Books:
- Complete novel structure
- Character depth
- World-building
- Single narrative arc
- Traditional publishing ready

### Episodic Series:
- 80-page episodes (1-1.5 hour reads)
- Cliffhanger endings
- Multiple plot threads (A/B/C)
- 10 episodes per season
- Binge-worthy structure

## 📝 Writing Process

### Traditional Book:
1. Plan in `/00-planning`
2. Build world in `/01-world`
3. Develop characters in `/02-characters`
4. Outline in `/03-plot`
5. Draft in `/06-drafts/current`
6. Revise with agents
7. Generate visuals
8. Produce EPUB/PDF

### Episodic Series:
1. Create series bible
2. Build complete world
3. Design full cast
4. Plan Season 1 (10 episodes)
5. Write episodes in order
6. Engineer cliffhangers
7. Track continuity
8. Release strategically

## 🎯 Success Metrics

### For Books:
- Complete, satisfying story
- Deep character development
- Rich world-building
- Professional quality
- Market ready

### For Episodes:
- Read in one sitting
- Immediate next episode
- Discussion/theories
- Binge reading
- Demand for next season

## 📚 Agent Command Examples

```
# Planning
"Story Architect: Create three-act structure for my YA fantasy"

# Characters
"Character Psychologist: Design authentic teen protagonist"

# World
"World Builder: Create contemporary high school setting"

# Writing
"Prose Stylist: Polish my opening chapter"

# Episodes
"Episode Writer: Structure 80-page pilot episode"
"Cliffhanger Engineer: Create betrayal cliffhanger"

# Visuals
"Visual Artist: Generate cover prompt for YA romance"

# Review
"Developmental Editor: Evaluate market readiness"
"Authenticity Editor: Remove AI writing patterns"
```

## 🔧 Troubleshooting

### Missing Dependencies:
```bash
pip install -r requirements.txt
```

### File Permissions:
```bash
chmod +x scripts/*.sh
```

### Image Issues:
- Ensure images in `/10-visuals/generated-art/`
- Support JPG and PNG
- Cover must be named `cover.jpg` or `cover.png`

## 📧 Support

This system was created for comprehensive YA writing with AI assistance.
Each agent has specific expertise - use them in combination for best results.

Remember: 
- For books, focus on complete arcs
- For episodes, focus on cliffhangers
- Always maintain authenticity
- Test with beta readers

Happy writing! 📝✨
