# Hockey Shuttle - Website Functional Specification

## Project Overview

**Project Name:** Hockey Shuttle Fan Landing Page
**Type:** Static Website
**Purpose:** Provide an immersive entry point into the Hockey Shuttle book series universe for fans and new readers
**Target Audience:** Young Adult readers (ages 13-18), sports romance enthusiasts, fans of episodic series
**Version:** 1.0
**Date:** November 2025

---

## 1. Executive Summary

The Hockey Shuttle website is a comprehensive digital experience designed to immerse fans in the world of this YA sports romance series. The site will feature rich visual storytelling, character profiles, episode guides, online reading capabilities, and strategic affiliate marketing through book recommendations. The website prioritizes user experience, visual appeal, and conversion through Amazon affiliate links.

---

## 2. Core Objectives

### Primary Goals
1. **Immerse readers** in the Hockey Shuttle universe through high-quality photography and design
2. **Provide multiple reading options** (online HTML, downloadable PDF/ePub)
3. **Generate revenue** through Amazon affiliate book recommendations
4. **Build community** by serving as a central hub for series fans
5. **Convert visitors** into readers and encourage episode/season purchases

### Success Metrics
- Time on site (target: 5+ minutes average)
- Episode read-throughs (completion rate)
- Affiliate link click-through rate (target: 15%+)
- Download conversions (PDF/ePub)
- Return visitor rate

---

## 3. Website Structure & Navigation

### 3.1 Site Map

```
HOME (Landing Page)
│
├── CHARACTERS
│   ├── Sophia Chen
│   ├── Ethan Price
│   ├── Maya Foster
│   ├── Jordan Nakamura
│   └── Becca Martinez
│
├── EPISODES
│   ├── Season 1 Overview
│   ├── Episode 1: Returning to Center Ice
│   ├── Episode 2: New Lines
│   ├── Episode 3: Defensive Zone
│   ├── Episode 4: Matchup
│   ├── Episode 5: Storm Warning
│   ├── Episode 6: The Weight
│   ├── Episode 7: Spring Training
│   ├── Episode 8: Recruiting Season
│   ├── Episode 9: Championship Weekend
│   └── Episode 10: Commence
│
├── WORLD
│   ├── St. Paul's High School
│   ├── The Rinks (Hockey)
│   ├── Badminton Courts
│   ├── Winnipeg Locations
│   └── The Forks
│
├── SUGGESTED BOOKS
│   └── Curated recommendations with affiliate links
│
└── ABOUT
    ├── About the Series
    └── Contact
```

### 3.2 Global Navigation

**Hamburger Menu Navigation** (accessible from all pages)
- **Menu Trigger:** Easily visible hamburger menu icon (☰) with "Menu" text next to it
- **Position:** Fixed position (typically top-right or top-left corner)
- **Visibility:** Always visible on all pages, overlaying the background
- **Behavior:** When clicked, opens a slide-out menu panel or overlay
- **Menu Content:**
  - Home
  - Characters (with sub-navigation for individual characters)
  - Episodes (with season/episode list)
  - World (location pages)
  - Suggested Books
  - About (series info and contact)

**Right Sidebar** (persistent across all pages except Home)
- "Readers Also Love" section
- 4-6 book recommendations
- Amazon affiliate links
- Cover images
- Brief descriptions
- Call-to-action buttons

**Footer** (persistent)
- Quick Links
- Social Media
- Privacy Policy
- Affiliate Disclosure
- Copyright

---

## 4. Page-by-Page Specifications

### 4.1 HOME PAGE (Landing)

#### Purpose
Create an immediate emotional connection and immerse visitors in the Hockey Shuttle world.

#### Visual Design

**Full-Screen Background Visual:**
- **Entire page features a single full-screen background drawing/image** generated using Gemini AI
- Background covers full viewport (100vw x 100vh minimum)
- Visual theme: Atmospheric blend of hockey rink and badminton court elements with dramatic, moody lighting
- Style: Subtle and atmospheric, NOT overly aggressive - should enhance rather than overpower content
- Color palette: Deep blues, purples, warm accent tones suggesting youth, energy, and drama
- Background should be slightly dimmed or have overlay to ensure overlaid content remains readable

**Overlaid UI Elements:**
- **Top Corner:** Hamburger menu icon + "Menu" text (fixed position, high z-index)
- **Center Hero Section:**
  - Book title: "Hockey Shuttle" in bold, dramatic typography
  - Tagline: "Where ice meets court, and hearts collide"
  - Brief hook text (2-3 sentences)
  - CTA Button: "Start Reading Episode 1" (prominent, with contrast)
- **Character Preview Cards:** 5 character cards with semi-transparent backgrounds, arranged in grid
- **Episode Highlight Section:** Featured episode card with semi-transparent overlay
- All overlaid elements should have subtle backgrounds (glass morphism, semi-transparent dark overlays) for readability

- **Series Introduction Section:**
  - Brief 2-3 paragraph hook
  - "10 Episodes | Season 1" badge
  - Genre tags: YA, Sports Romance, Hockey, Badminton, Enemies-to-Lovers

- **Character Previews:**
  - 5 character cards with photos
  - Names and one-line descriptors
  - Hover effect reveals character quote
  - Links to full character pages

- **Latest Episode Highlight:**
  - Featured episode section
  - Cover art
  - Synopsis
  - "Read Now" CTA

#### Technical Requirements
- Responsive design (mobile-first)
- Lazy loading for images
- Parallax scrolling effects (optional)
- Fast load time (<3 seconds)
- SEO optimized

---

### 4.2 CHARACTER PAGES

#### Purpose
Deep character exploration to build emotional investment and understanding.

#### Individual Character Page Structure

**For Each Main Character:**
1. **Sophia Chen** - The Analytical Overthinker
2. **Ethan Price** - The Compartmentalized Performer
3. **Maya Foster** - The Direct Competitor
4. **Jordan Nakamura** - The Wry Observer
5. **Becca Martinez** - The Cracking Performance

#### Visual Design

**Full-Screen Background Visual:**
- **Entire page features a single full-screen background drawing/image** generated using Gemini AI
- Visual theme: Character-focused atmosphere with hints of their sport (hockey or badminton)
- Background should evoke the character's personality and energy
- Style: Atmospheric and subtle, allowing character content to stand out
- Color palette: Consistent with site theme, with character-specific accent colors
- Background slightly dimmed with overlay for content readability

#### Content Structure

**Overlaid Hero Section:**
- **Top Corner:** Hamburger menu icon + "Menu" text
- Large character portrait/action photo (with semi-transparent background card)
- Character name
- Descriptor tagline
- Key stats (age, sport, role in series)

**Character Profile (overlaid with semi-transparent containers):**
- **About:** 2-3 paragraphs character bio
- **Personality:** Key traits, communication style
- **Background:** Family, history, motivations
- **Sport:** Hockey or Badminton details, playing style
- **Relationships:** Connections to other characters (linked)
- **Character Arc:** Journey through Season 1 (spoiler-free for new readers)

**Visual Elements:**
- Photo gallery (3-5 images)
- Character quotes in callout boxes
- Scene excerpts featuring the character
- "Character Playlist" section (optional - songs that represent them)

**Related Episodes:**
- List of key episodes featuring this character
- Links to read those episodes

**Right Sidebar:**
- "Suggested Books" affiliate links (books with similar character types)

#### Technical Requirements
- Character comparison tool (optional feature)
- Shareable character quote cards
- Print-friendly version

---

### 4.3 EPISODES PAGES

#### 4.3.1 Season Overview Page

**Purpose:** Provide a visual episode guide and navigation hub.

**Full-Screen Background Visual:**
- **Entire page features a single full-screen background drawing/image** generated using Gemini AI
- Visual theme: Storytelling/journey atmosphere suggesting episodic progression and adventure
- Style: Atmospheric with subtle elements suggesting chapter breaks, story arcs, or timeline progression
- Color palette: Site-consistent blues and purples with accent colors
- Background dimmed with overlay for episode card readability

**Overlaid Content:**
- **Top Corner:** Hamburger menu icon + "Menu" text
- **Page Header:** "Season 1" title with tagline
- Season synopsis (2-3 paragraphs in semi-transparent container)
- **Episode grid/list** with semi-transparent cards containing:
  - Episode number and title
  - Cover art/header image thumbnail
  - 2-sentence synopsis
  - Word count / page estimate
  - Status badges (Available, Coming Soon, etc.)
  - Three CTAs per episode:
    - "Read Online"
    - "Download PDF"
    - "Download ePub"

**Visual Design:**
- Episode cards in grid layout (3 columns on desktop) with glass morphism effect
- Hover effects show more details
- Progress indicators for readers (if account system added later)
- All cards have subtle backgrounds for readability over the full-screen visual

---

#### 4.3.2 Individual Episode Pages

**Purpose:** Provide three reading/access options for each episode.

**Full-Screen Background Visual:**
- **Entire page features a single full-screen background drawing/image** generated using Gemini AI
- Visual theme: Episode-specific atmosphere reflecting the episode's key themes and mood
- Style: Atmospheric and cinematic, evoking the episode's emotional tone
- Color palette: Consistent with site, with episode-specific accents
- Background dimmed with overlay for content readability

**Episode Page Structure:**

**Overlaid Hero Section:**
- **Top Corner:** Hamburger menu icon + "Menu" text
- Episode cover art (large, in semi-transparent card)
- Episode number and title
- Episode tagline/hook
- Key episode info:
  - Word count
  - Estimated reading time
  - Publication date
  - Content warnings (if applicable)

**Episode Summary:**
- Spoiler-free synopsis (2-3 paragraphs)
- Key themes
- Chapter breakdown overview

**Reading Options Section (PROMINENT):**

1. **Read Online**
   - Large button: "Read in Browser"
   - Takes user to in-browser reading experience (see 4.3.3)

2. **Download PDF**
   - Button: "Download PDF"
   - Triggers download of formatted PDF file
   - File naming: `Hockey-Shuttle-S01E01-Returning-to-Center-Ice.pdf`

3. **Download ePub**
   - Button: "Download ePub"
   - Triggers download of ePub file for e-readers
   - File naming: `Hockey-Shuttle-S01E01-Returning-to-Center-Ice.epub`

**Additional Content:**
- Character appearances in this episode (with links)
- Location highlights
- Key quotes from episode
- "What Readers Are Saying" section (reviews/testimonials)
- Discussion prompts (for book clubs/fans)

**Episode Navigation:**
- "Previous Episode" / "Next Episode" buttons
- Back to Season Overview link

**Right Sidebar:**
- "Suggested Books" with affiliate links (books similar to this episode's themes)

---

#### 4.3.3 Online Reading Experience (HTML Reader)

**Purpose:** Provide comfortable, distraction-free online reading.

**Reading Interface Design:**

**Layout:**
- Clean, minimalist design
- Centered text column (optimal reading width: 600-700px)
- Ample white space
- Comfortable typography
  - Font: Serif for body text (Georgia, Merriweather, or similar)
  - Font size: 18-20px default
  - Line height: 1.6-1.8
  - Paragraph spacing

**Reader Controls:**
- **Top Bar (sticky):**
  - Episode title
  - Progress indicator (% read or chapter indicator)
  - Settings icon (opens reader preferences)
  - Exit/Close reader (returns to episode page)

- **Reader Settings Panel:**
  - Font size adjustment (+/-)
  - Font family options (3-4 choices)
  - Background color (White, Sepia, Dark mode)
  - Line spacing adjustment
  - Text width adjustment

**Navigation:**
- Chapter markers in sidebar or dropdown
- "Previous Chapter" / "Next Chapter" buttons at bottom
- Scroll progress indicator
- "Back to Top" button

**Content Structure:**
- Episode title page
- Chapter headings (clear hierarchy)
- Scene breaks (visual separators)
- Smooth scrolling

**Reading Experience Features:**
- Auto-save reading position (browser local storage)
- Shareable quote cards (highlight text to share)
- Reading time estimate at start
- "Finished this episode?" prompt with link to next episode

**Mobile Optimization:**
- Swipe gestures for chapter navigation
- Optimized for portrait reading
- Minimal chrome/UI when scrolling

**Technical Requirements:**
- Fast content loading
- Offline reading capability (PWA)
- Accessibility compliance (WCAG AA)
- Screen reader friendly
- Keyboard navigation support

---

### 4.4 WORLD PAGES

#### Purpose
Immerse readers in the Hockey Shuttle universe through rich location profiles.

**Full-Screen Background Visual (Location-Specific):**
- **Each location page features its own full-screen background drawing/image** generated using Gemini AI
- Visual theme: Location-specific atmosphere (e.g., hockey rink, school hallways, Winnipeg landmarks)
- Style: Atmospheric environmental visuals that transport viewers to the location
- Color palette: Consistent with site, with location-appropriate variations
- Background dimmed with overlay for content readability

#### Location Pages:

1. **St. Paul's High School**
   - **Background:** School exterior/interior atmosphere
   - **Top Corner:** Hamburger menu icon + "Menu" text
   - Overview and atmosphere (in semi-transparent card)
   - Photo gallery overlay
   - Key locations (cafeteria, library, etc.)
   - Social hierarchy explanation
   - Episodes set here (linked)

2. **The Rinks (Hockey)**
   - **Background:** Dramatic hockey rink atmosphere with ice and lighting
   - Bell MTS Iceplex details
   - Community rinks
   - Hockey culture at St. Paul's
   - Team info
   - Action photography overlaid

3. **Badminton Courts**
   - **Background:** Badminton court atmosphere with nets and lighting
   - Training facilities
   - Competition venues
   - Team culture
   - Sport explanation for non-fans

4. **Winnipeg Locations**
   - **Background:** The Forks or Winnipeg cityscape atmosphere
   - The Forks details
   - Neighborhoods
   - Local culture
   - Season/weather atmosphere

5. **World Overview**
   - **Background:** Composite atmosphere combining key visual elements
   - Timeline
   - Setting details
   - Cultural context
   - Sport seasons and competition schedules

**Visual Design:**
- Full-screen background specific to each location
- Overlaid content in semi-transparent containers
- Interactive map (optional) overlaid on background
- Image galleries with glass morphism effects
- "Featured in Episodes" links in cards
- All content maintains readability over backgrounds

---

### 4.5 SUGGESTED BOOKS PAGE

#### Purpose
Generate affiliate revenue while providing value to readers seeking similar content.

**Full-Screen Background Visual:**
- **Entire page features a single full-screen background drawing/image** generated using Gemini AI
- Visual theme: Literary/reading atmosphere with subtle book and library elements
- Style: Warm, inviting, and atmospheric - suggests discovery and reading joy
- Color palette: Warmer tones blended with site colors, cozy and welcoming
- Background dimmed with overlay for book card readability

**Page Structure:**

**Overlaid Hero Section:**
- **Top Corner:** Hamburger menu icon + "Menu" text
- Heading: "If You Love Hockey Shuttle..." (in semi-transparent card)
- Subheading: "You'll love these books too"
- Brief intro about why these books are recommended

**Book Recommendation Sections:**

Organize by categories:

1. **Sports Romance**
   - YA sports-focused romance novels
   - 6-8 recommendations

2. **Hockey Romances**
   - Specific hockey-themed books
   - 6-8 recommendations

3. **High School Drama**
   - Contemporary YA with similar settings
   - 6-8 recommendations

4. **Episodic Series**
   - Other binge-worthy series
   - 6-8 recommendations

5. **Character-Driven YA**
   - Books with similar deep character work
   - 6-8 recommendations

**Book Card Design (for each recommendation):**
- Book cover image (high quality)
- Title and author
- 2-3 sentence description
- Why Hockey Shuttle fans will love it
- Rating/accolades (if notable)
- "View on Amazon" button (affiliate link)
- Price display (if possible via Amazon API)

**Technical Requirements:**
- Amazon Associates affiliate links
- Link tracking for performance metrics
- Regular content updates (seasonal refreshes)
- Responsive grid layout (3-4 columns desktop, 1-2 mobile)

**Additional Features:**
- Filter/sort options (by genre, publication date, rating)
- "Most Popular" section
- "New Releases" section
- Newsletter signup for book recommendations

---

### 4.6 RIGHT SIDEBAR - "SUGGESTED BOOKS" (Global Element)

#### Purpose
Persistent monetization opportunity across all pages except homepage.

**Sidebar Specifications:**

**Placement:**
- Fixed position on right side (desktop)
- Scroll with page OR sticky positioning
- Bottom of page on mobile (or collapsible)

**Content:**
- Section heading: "Readers Also Love" or "Recommended for You"
- 4-6 book recommendations
- Compact book cards:
  - Small cover image (150-200px height)
  - Title (truncated if needed)
  - Author
  - Amazon affiliate link button

**Rotation Strategy:**
- Different books on different page types (character pages vs episode pages)
- Contextual recommendations when possible
  - Character pages: books with similar character types
  - Episode pages: books matching episode themes
  - World pages: books with similar settings

**Design:**
- Clean, not intrusive
- Clearly marked as recommendations
- Professional appearance
- Mobile-friendly collapse/expand

**Technical Requirements:**
- Easy content management for updating recommendations
- A/B testing capability for optimization
- Click tracking
- Affiliate link compliance (disclosure)

---

## 5. Content Requirements

### 5.1 Photography & Visual Assets

**Required Photo Categories:**

1. **Environment Photography (20-30 images minimum):**
   - Hockey rinks (various angles, lighting conditions)
   - Badminton courts (action shots, detail shots)
   - St. Paul's High School (exterior, hallways, classrooms, cafeteria)
   - Winnipeg locations (The Forks, bridges, city views)
   - Seasonal shots (fall/winter atmosphere)

2. **Character Imagery (15-20 images):**
   - Individual character portraits (5 main characters)
   - Action shots (sports scenes)
   - Interaction moments (2-3 characters together)
   - Emotional moments (close-ups)

3. **Episode Cover Art (10 images):**
   - Unique cover/header for each episode
   - Series branding consistent
   - Visually distinct per episode theme

**Image Specifications:**
- Format: JPG (photography), PNG (graphics/logos)
- Resolution: High-res for hero sections (1920px+ width)
- Optimization: Compressed for web without quality loss
- Alt text: Descriptive for accessibility
- File naming: Consistent, SEO-friendly

**Image Sources:**
- Stock photography (Unsplash, Pexels for commercial use)
- Custom photography (if budget allows)
- AI-generated art (MidJourney, Stable Diffusion)
- Illustration/graphic design elements

---

### 5.2 Written Content

**Required Text Content:**

1. **Series Overview** (500-700 words)
   - Hook for new readers
   - Premise explanation
   - What makes it unique
   - Target audience

2. **Character Bios** (300-500 words each × 5 characters)
   - Background
   - Personality
   - Motivations
   - Relationships
   - Character arc

3. **Episode Summaries** (200-300 words each × 10 episodes)
   - Spoiler-free synopsis
   - Key themes
   - Emotional hooks

4. **Location Descriptions** (200-400 words each × 5 locations)
   - Atmospheric description
   - Significance to story
   - Real-world context (for Winnipeg locations)

5. **Suggested Books** (100-150 words each × 30-40 books)
   - Book description
   - Why Hockey Shuttle fans will enjoy
   - Comparison points

6. **About/Author Content** (300-500 words)
   - Series genesis
   - Author bio
   - Writing process insights

**Writing Style Guidelines:**
- Voice: Engaging, enthusiastic, authentic
- Tone: Young adult appropriate, energetic
- POV: Mix of direct address to readers and descriptive
- SEO: Keyword optimization for discoverability
- Length: Concise but rich, scannable

---

### 5.3 Episode Files (HTML, PDF, ePub)

**For Each Episode:**

1. **HTML Version:**
   - Clean, semantic HTML5
   - Styled consistently with reading interface
   - Chapter divisions marked
   - Embedded in reading experience page

2. **PDF Version:**
   - Professional formatting
   - Cover page with episode art
   - Table of contents (if multiple chapters)
   - Page numbers
   - Header/footer with series branding
   - Print-optimized (if users want physical copies)
   - File size: Optimized (<5MB)

3. **ePub Version:**
   - Standard ePub3 format
   - Compatible with Kindle, Apple Books, etc.
   - Embedded fonts (if custom typography)
   - Metadata (title, author, series info)
   - Cover image
   - TOC navigation
   - Reflowable text

**Content Conversion:**
- Source: Markdown files from `/season-01/episode-XX/draft/`
- Generation: Automated build process
- Quality control: Manual review for formatting issues
- Updates: Version control for corrections

---

## 6. Technical Specifications

### 6.1 Technology Stack

**Recommended Static Site Generator:**
- **Option 1: Next.js** (with static export)
  - React-based
  - Great for complex interactions
  - Excellent performance
  - Easy deployment

- **Option 2: Gatsby**
  - React-based
  - Image optimization built-in
  - Rich plugin ecosystem
  - GraphQL for content queries

- **Option 3: Hugo**
  - Extremely fast build times
  - Simple templating
  - Markdown-native
  - Lightweight

**Frontend Technologies:**
- HTML5
- CSS3 (or Sass/SCSS)
- JavaScript (ES6+)
- CSS Framework: Tailwind CSS or custom
- Animation: GSAP or Framer Motion (optional)

**Reading Experience:**
- Progressive Web App (PWA) capabilities
- Service Worker for offline reading
- Local Storage for reading progress
- Web fonts: Google Fonts or similar

**File Generation:**
- Markdown to HTML: Marked.js or similar
- PDF Generation: Prince XML, WeasyPrint, or Pandoc
- ePub Generation: Pandoc or Calibre CLI
- Automation: Node.js scripts or Python

---

### 6.2 Hosting & Deployment

**Hosting Options:**
- **Netlify** (Recommended)
  - Free tier available
  - Automatic deployments
  - CDN included
  - Forms/functions support

- **Vercel**
  - Excellent for Next.js
  - Free tier
  - Great performance

- **GitHub Pages**
  - Free
  - Simple deployment
  - Good for basic static sites

**Domain:**
- Custom domain (e.g., hockeyshuttle.com)
- SSL certificate (automatic with Netlify/Vercel)

**CDN & Performance:**
- Global CDN for fast loading worldwide
- Image optimization and lazy loading
- Gzip/Brotli compression
- Caching strategies

---

### 6.3 Amazon Affiliate Integration

**Amazon Associates Setup:**
- Create Amazon Associates account
- Generate affiliate links for all book recommendations
- Link tracking tags for performance analysis
- Compliance with Amazon Associates terms

**Link Structure:**
- Format: `https://www.amazon.com/dp/ASIN?tag=YOUR-TAG-20`
- Tag management: Unique tags for different site sections (optional)
- Link cloaking: Optional URL shortening for cleaner look

**Legal Requirements:**
- Affiliate disclosure on every page with affiliate links
- Footer disclosure statement
- Dedicated Privacy Policy page
- Cookie consent (if implementing tracking)

**Performance Tracking:**
- Amazon Associates dashboard
- Google Analytics integration
- Conversion tracking
- Revenue reporting

---

### 6.4 Analytics & Tracking

**Google Analytics 4:**
- Page view tracking
- Event tracking:
  - Episode reads (HTML)
  - Downloads (PDF/ePub)
  - Affiliate link clicks
  - Navigation patterns
  - Time on page

**Custom Events:**
- Reading progress (25%, 50%, 75%, 100%)
- Chapter completion
- Character page visits
- Suggested book clicks

**Performance Monitoring:**
- Load time tracking
- Core Web Vitals
- Mobile vs desktop usage
- Bounce rate analysis

---

### 6.5 SEO & Discoverability

**On-Page SEO:**
- Meta titles (unique per page)
- Meta descriptions (compelling, keyword-rich)
- Header tags (H1, H2, H3 hierarchy)
- Alt text for all images
- Internal linking strategy
- URL structure (clean, descriptive)

**Technical SEO:**
- Sitemap.xml
- Robots.txt
- Schema.org markup (Book, Review schemas)
- Open Graph tags (social sharing)
- Twitter Card tags
- Canonical URLs

**Content SEO:**
- Keyword research and integration
  - Target: "YA hockey romance"
  - Target: "sports romance books"
  - Target: "hockey book series"
  - Target: "badminton YA books"
- Long-tail keywords in content
- FAQ sections (optional)

**Social Media Integration:**
- Shareable quote cards
- Social media buttons
- OG images for each page
- Twitter/Facebook previews optimized

---

### 6.6 Accessibility (WCAG 2.1 AA Compliance)

**Requirements:**
- Semantic HTML structure
- Keyboard navigation support
- Screen reader compatibility
- ARIA labels where needed
- Sufficient color contrast (4.5:1 minimum)
- Focus indicators
- Skip navigation links
- Alt text for all images
- Captions/transcripts for video (if added later)
- Resizable text (up to 200%)
- No content relying solely on color

**Testing:**
- WAVE accessibility checker
- axe DevTools
- Screen reader testing (NVDA, JAWS, VoiceOver)
- Keyboard-only navigation testing

---

### 6.7 Mobile Responsiveness

**Breakpoints:**
- Mobile: 320px - 767px
- Tablet: 768px - 1023px
- Desktop: 1024px - 1439px
- Large Desktop: 1440px+

**Mobile-First Design:**
- Touch-friendly interface (44px minimum tap targets)
- Simplified navigation (hamburger menu)
- Optimized images (responsive images, WebP format)
- Fast mobile performance (<3s load)
- Readable text without zooming
- Sticky headers (minimal)

**Testing:**
- Chrome DevTools device emulation
- Real device testing (iOS, Android)
- Various screen sizes
- Portrait and landscape orientations

---

## 7. User Experience (UX) Considerations

### 7.1 User Flows

**New Visitor Flow:**
1. Lands on homepage (hero image + tagline)
2. Scrolls through environment photos (immersion)
3. Reads series introduction
4. Explores character previews
5. Clicks "Start Reading Episode 1" CTA
6. Reads Episode 1 online OR downloads
7. Returns for Episode 2

**Returning Reader Flow:**
1. Lands on homepage
2. Navigates to Episodes page
3. Continues reading from saved position OR starts new episode
4. Clicks affiliate links in sidebar (passive discovery)
5. Downloads episode for offline reading

**Character Exploration Flow:**
1. Visits character page (from homepage or navigation)
2. Reads character bio
3. Views photo gallery
4. Clicks "Key Episodes" to read character-focused episodes
5. Explores related characters

**Book Discovery Flow:**
1. Discovers "Suggested Books" sidebar while reading
2. Clicks on intriguing recommendation
3. Views Amazon page (affiliate link)
4. Potentially purchases
5. Returns to continue reading Hockey Shuttle

---

### 7.2 Call-to-Action (CTA) Strategy

**Primary CTAs:**
- "Start Reading Episode 1" (homepage)
- "Read Online" (episode pages)
- "Download PDF" / "Download ePub" (episode pages)
- "Next Episode" (end of reading experience)

**Secondary CTAs:**
- "View on Amazon" (book recommendations)
- "Explore Character" (character cards)
- "Read This Episode" (character pages, world pages)
- "Back to Episodes" (navigation)

**CTA Design:**
- High contrast buttons
- Action-oriented copy
- Clear hierarchy (primary vs secondary)
- Consistent placement
- Mobile-optimized size

---

### 7.3 Reading Experience Optimization

**Reader Comfort:**
- Optimal line length (60-75 characters)
- Generous line spacing
- Comfortable font size (18-20px default)
- Clean, distraction-free layout
- Dark mode option for night reading
- Progress saving (resume where left off)

**Engagement Features:**
- Chapter preview (first paragraph of next chapter at end)
- Related character links (contextual)
- "Share favorite quote" functionality
- Reading time estimates
- Smooth chapter transitions

---

## 8. Content Management

### 8.1 Content Update Workflow

**Episode Publishing:**
1. Finalize episode content (Markdown source files)
2. Generate HTML, PDF, ePub versions
3. Create episode cover art
4. Write episode summary and metadata
5. Add episode to site structure
6. Update navigation/episode list
7. Deploy to hosting
8. Announce on social media

**Book Recommendations:**
- Monthly review and update cycle
- Replace underperforming affiliate links
- Add new releases
- Seasonal themes (holiday books, summer reads, etc.)

**Image Updates:**
- Quarterly refresh of homepage hero images
- New character photos as available
- Updated location photography

---

### 8.2 Version Control

**Git Repository:**
- GitHub or GitLab repository
- Organized folder structure:
  ```
  /website
    /src
      /pages
      /components
      /styles
      /images
      /content
        /episodes
        /characters
        /world
        /books
    /public
    /scripts
    /specifications
  ```

**Branching Strategy:**
- `main` branch (production)
- `develop` branch (staging)
- Feature branches for major updates
- Pull request workflow

---

## 9. Future Enhancements (Phase 2+)

### Potential Features:
- **User Accounts:** Save reading progress across devices
- **Comments/Reviews:** Reader discussions on episode pages
- **Email Newsletter:** Episode release notifications, book recommendations
- **Author Blog:** Behind-the-scenes content, writing process
- **Interactive Map:** Clickable Winnipeg map with story locations
- **Character Quizzes:** "Which Hockey Shuttle character are you?"
- **Fan Art Gallery:** Showcase reader-submitted artwork
- **Audio Versions:** Episodic audiobook integration
- **Merchandise Store:** T-shirts, bookmarks, posters (via print-on-demand)
- **Book Club Kit:** Discussion guides, downloadable materials
- **Exclusive Content:** Bonus scenes, character interviews for subscribers

---

## 10. Success Metrics & KPIs

### Key Performance Indicators:

**Traffic Metrics:**
- Unique visitors per month
- Page views per session
- Average time on site
- Bounce rate
- Return visitor rate

**Engagement Metrics:**
- Episode read completion rate
- Average reading time per episode
- Downloads (PDF/ePub) per episode
- Character page views
- World page exploration

**Conversion Metrics:**
- Affiliate link click-through rate (CTR)
- Amazon referral conversions
- Revenue per 1,000 visitors (RPM)
- Newsletter signups (if implemented)

**Content Performance:**
- Most popular episodes
- Most visited character pages
- Top-performing affiliate book recommendations
- Search engine rankings for target keywords

**Technical Performance:**
- Page load time (target: <3 seconds)
- Core Web Vitals scores
- Mobile usability score
- Accessibility score

---

## 11. Budget Considerations

### Estimated Costs:

**Development:**
- Static site development: $0 - $5,000 (DIY to professional)
- Design/branding: $0 - $2,000
- Photography/stock images: $0 - $500 (free stock + some paid)

**Hosting & Domain:**
- Domain registration: $10-15/year
- Hosting: $0-20/month (Netlify/Vercel free tier likely sufficient)
- CDN: Included in hosting

**Tools & Services:**
- Google Analytics: Free
- Amazon Associates: Free (commission-based)
- Font licenses (if custom): $0-200
- SSL certificate: Free (via hosting)

**Ongoing:**
- Content updates: Time investment
- Image refreshes: Minimal cost (stock photos)
- Maintenance: Minimal (static site)

**Total Estimated Initial Investment:** $10 - $7,700
**Ongoing Monthly Costs:** $0 - $20

---

## 12. Timeline & Milestones

### Phase 1: Foundation (Weeks 1-2)
- [ ] Finalize design mockups
- [ ] Choose technology stack
- [ ] Set up development environment
- [ ] Create basic site structure
- [ ] Design homepage and navigation

### Phase 2: Core Pages (Weeks 3-4)
- [ ] Build homepage with environment photos
- [ ] Create character page templates
- [ ] Develop episode listing page
- [ ] Build individual episode pages
- [ ] Implement reading experience (HTML reader)

### Phase 3: Content Integration (Weeks 5-6)
- [ ] Add all character content and images
- [ ] Upload all 10 episodes (HTML, PDF, ePub)
- [ ] Create world/location pages
- [ ] Populate suggested books page
- [ ] Set up Amazon affiliate links

### Phase 4: Features & Polish (Week 7)
- [ ] Implement right sidebar with affiliate links
- [ ] Add reader settings (font size, dark mode, etc.)
- [ ] Optimize images and performance
- [ ] Mobile responsiveness testing and fixes
- [ ] Accessibility audit and improvements

### Phase 5: Launch Preparation (Week 8)
- [ ] SEO optimization (meta tags, sitemaps, etc.)
- [ ] Set up Google Analytics
- [ ] Test all affiliate links
- [ ] Cross-browser testing
- [ ] Content proofreading
- [ ] Deploy to hosting (staging)

### Phase 6: Launch (Week 9)
- [ ] Final testing on staging
- [ ] Deploy to production
- [ ] Submit to search engines
- [ ] Social media announcement
- [ ] Monitor analytics and performance

### Post-Launch:
- [ ] Gather user feedback
- [ ] Monitor affiliate performance
- [ ] Iterate on design based on data
- [ ] Plan Phase 2 features

---

## 13. Risk Assessment & Mitigation

### Potential Risks:

1. **Low Traffic Initially**
   - **Mitigation:** SEO optimization, social media marketing, book community engagement

2. **Poor Affiliate Conversion**
   - **Mitigation:** A/B test book recommendations, ensure relevance, optimize placement

3. **High Bounce Rate**
   - **Mitigation:** Compelling hero section, fast load times, clear value proposition

4. **Mobile Performance Issues**
   - **Mitigation:** Mobile-first development, rigorous testing, image optimization

5. **Content Piracy (Episode Downloads)**
   - **Mitigation:** Watermarking PDFs/ePubs, acceptable risk for fan engagement

6. **Amazon Associates Account Suspension**
   - **Mitigation:** Follow all TOS guidelines, proper disclosures, quality content

7. **Browser Compatibility Issues**
   - **Mitigation:** Cross-browser testing, progressive enhancement, polyfills

---

## 14. Legal & Compliance

### Required Legal Pages:

1. **Privacy Policy**
   - Data collection practices
   - Cookie usage
   - Third-party services (Analytics, Amazon)
   - User rights

2. **Affiliate Disclosure**
   - Clear statement on all pages with affiliate links
   - FTC compliance
   - Example: "This site contains affiliate links. We may earn a commission on purchases made through these links at no additional cost to you."

3. **Terms of Use**
   - Content usage rights
   - Download terms for episodes
   - Limitation of liability

4. **Copyright Notice**
   - All content © [Year] Hockey Shuttle
   - Rights reserved statement

5. **Cookie Consent** (if EU traffic expected)
   - GDPR compliance
   - Cookie banner
   - Opt-in/opt-out options

---

## 15. Conclusion

The Hockey Shuttle website will serve as a comprehensive digital hub for fans, combining immersive visual storytelling, accessible reading options, and strategic monetization through affiliate marketing. By prioritizing user experience, mobile performance, and SEO best practices, the site is positioned to grow organically while generating passive revenue through thoughtfully curated book recommendations.

The modular, static site architecture ensures low maintenance costs, fast performance, and easy scalability as the series grows. With clear success metrics and a phased development approach, the website can launch efficiently and iterate based on real user data.

**Next Steps:**
1. Review and approve this functional specification
2. Select technology stack and begin design mockups
3. Source or create photography and visual assets
4. Begin Phase 1 development
5. Establish Amazon Associates account and prepare affiliate links

---

## 16. Appendices

### Appendix A: Technology Resources

**Static Site Generators:**
- Next.js: https://nextjs.org/docs/pages/building-your-application/deploying/static-exports
- Gatsby: https://www.gatsbyjs.com/
- Hugo: https://gohugo.io/

**Hosting Platforms:**
- Netlify: https://www.netlify.com/
- Vercel: https://vercel.com/
- GitHub Pages: https://pages.github.com/

**PDF/ePub Generation:**
- Pandoc: https://pandoc.org/
- Calibre: https://calibre-ebook.com/
- WeasyPrint: https://weasyprint.org/

**Amazon Associates:**
- Sign Up: https://affiliate-program.amazon.com/
- Documentation: https://affiliate-program.amazon.com/help/

---

### Appendix B: Competitive Analysis

**Similar Sites to Study:**
1. **Wattpad** - Reading experience UX
2. **Royal Road** - Episode/chapter navigation
3. **Kindle Unlimited Landing Pages** - Series presentation
4. **BookBub** - Book recommendation layout
5. **Goodreads** - Character/book organization

**Differentiators for Hockey Shuttle:**
- Higher quality photography (immersive environment)
- Cleaner, more modern design
- Multiple download formats (PDF + ePub)
- Integrated affiliate monetization
- Character-focused navigation

---

### Appendix C: Content Checklist

**Before Launch, Ensure:**
- [ ] All 10 episode HTML versions tested
- [ ] All 10 episode PDFs generated and checked
- [ ] All 10 episode ePubs generated and tested on devices
- [ ] 5 character pages complete with photos
- [ ] 20-30 environment photos uploaded and optimized
- [ ] 30-40 suggested books with affiliate links
- [ ] All metadata (titles, descriptions) written
- [ ] SEO keywords integrated naturally
- [ ] All images have alt text
- [ ] All links tested (internal and external)
- [ ] Privacy policy and legal pages published
- [ ] Contact information available
- [ ] 404 error page designed
- [ ] Favicon and app icons created
- [ ] Social media preview images set up

---

## 16. Google Stitch - AI Designer Page Prompts

This section provides detailed prompts for **Google Stitch - AI Designer** to generate each page of the Hockey Shuttle website. Google Stitch is Google's experimental AI-powered tool that converts text prompts into full UI designs with exportable code (HTML, Tailwind CSS, JSX, or Figma). Each prompt below describes the full visual layout including the full-screen background visual and overlaid UI elements.

### About Google Stitch
- **Tool URL:** https://stitch.withgoogle.com/
- **Capabilities:** Converts text prompts to UI designs using Gemini 2.5 Pro/Flash
- **Output Formats:** HTML, Tailwind CSS, JSX, or direct export to Figma
- **Generations:** 50/month with Gemini 2.5 Pro, 350/month with Gemini 2.5 Flash

### Design Consistency Notes
When using these prompts in Google Stitch, ensure:
1. **Consistent Navigation:** All pages share the same hamburger menu icon + "Menu" text component
2. **Color Palette:** Maintain consistent blues, purples, and accent colors across all pages
3. **Typography:** Use the same font families and hierarchy across the site
4. **Glass Morphism:** Apply consistent semi-transparent overlay effects for content cards
5. **Background Style:** All backgrounds should be atmospheric and subtle, not overly aggressive
6. **Accessibility:** Maintain WCAG AA contrast ratios for all text over backgrounds

---

### 16.1 Home Page (Landing) - Google Stitch Prompt

```
Create a modern, immersive landing page for a YA sports romance book series website called "Hockey Shuttle" with these specifications:

FULL-SCREEN BACKGROUND:
- Generate a full-screen (100vw x 100vh minimum) atmospheric background illustration
- Visual theme: Dramatic blend of hockey rink and badminton court elements
  - Subtle hockey ice surface with dramatic lighting
  - Abstract badminton net elements in background
  - Moody, cinematic atmosphere with depth
- Color palette: Deep blues (#1a2332, #2d4a6e), purples (#4a2d5c, #7c5295), dramatic lighting with warm accent tones (#ff6b4a, #ffa94d)
- Style: SUBTLE and ATMOSPHERIC - not overly aggressive
  - Should enhance content, not overpower it
  - Soft focus or slightly dimmed to allow text readability
  - Cinematic, youthful, energetic feel
- Add subtle dark overlay (rgba(0,0,0,0.3)) for text contrast

OVERLAID UI ELEMENTS:

Top Right Corner (Fixed Position):
- Hamburger menu icon (☰) three clean horizontal lines
- Text "Menu" next to icon in white
- Both should have subtle text shadow for visibility
- Minimum touch target: 44px x 44px
- Hover effect: slight scale (1.05) and opacity change

Center Hero Section:
- Large, bold title: "HOCKEY SHUTTLE"
  - Typography: Bold, modern sans-serif (700-900 weight)
  - Font size: 72-96px desktop, 48px mobile
  - Color: White with subtle text shadow
  - Letter spacing: slightly expanded
- Tagline below title: "Where ice meets court, and hearts collide"
  - Font size: 24-28px desktop, 18px mobile
  - Color: Light gray/white (#e0e0e0)
  - Elegant serif or clean sans-serif font
- Brief hook (2-3 sentences max) in semi-transparent card:
  - Background: rgba(26, 35, 50, 0.7) with backdrop blur
  - Padding: 24px
  - Border radius: 12px
  - Max width: 700px
  - Centered alignment
- Call-to-action button: "Start Reading Episode 1"
  - Background: Accent color gradient (#ff6b4a to #ff8c6b)
  - Color: White text
  - Padding: 16px 32px
  - Border radius: 8px
  - Font weight: 600
  - Hover effect: slight scale and brightness increase
  - Box shadow for depth

Character Preview Cards (Below Hero):
- 5 character cards in horizontal row (stack on mobile)
- Each card:
  - Semi-transparent background: rgba(45, 74, 110, 0.6) with backdrop blur
  - Padding: 20px
  - Border radius: 10px
  - Border: 1px solid rgba(255,255,255,0.1)
  - Character name in bold white text
  - One-line descriptor in light gray
  - Placeholder for character photo/portrait
  - Hover effect: slight lift with shadow and scale (1.03)

Featured Episode Section:
- Semi-transparent card: rgba(26, 35, 50, 0.8)
- Contains:
  - "Latest Episode" label
  - Episode cover art thumbnail
  - Episode title and number
  - Brief synopsis (2-3 lines)
  - "Read Now" button (secondary accent color)

TECHNICAL SPECIFICATIONS:
- Mobile-first responsive design
- Breakpoints: 768px (tablet), 1024px (desktop)
- Background: background-size: cover; background-position: center; background-attachment: fixed
- Z-index layering: background (0), content (1), hamburger menu (100)
- All interactive elements have clear hover states
- Smooth transitions (200-300ms)
- Typography hierarchy clearly defined
- Minimum font size: 16px for body text
```

---

### 16.2 Character Pages - Google Stitch Prompt

```
Create an immersive character profile page for the "Hockey Shuttle" book series with these specifications:

FULL-SCREEN BACKGROUND:
- Generate a full-screen atmospheric background illustration
- Visual theme: Character-focused atmosphere with their sport (hockey or badminton)
  - For hockey characters: Ice rink atmosphere with dramatic lighting, hockey stick/puck silhouettes
  - For badminton characters: Court atmosphere with net, shuttlecock, and lighting
  - Abstract, artistic representation - not literal photos
- Style: Atmospheric, moody, cinematic - allows character content to stand out
- Color palette: Site-consistent blues and purples with character-specific accent color
  - Example: Fiery orange/red for intense characters, cool teal for analytical characters
- Background should be dimmed (opacity 0.7-0.8) with dark overlay for readability

OVERLAID UI ELEMENTS:

Top Right Corner (Fixed):
- Hamburger menu icon (☰) + "Menu" text
- White with text shadow
- Minimum 44px touch target

Hero Section (Top of Page):
- Large semi-transparent card: rgba(26, 35, 50, 0.85) with backdrop blur
- Layout: Flexbox with image left, info right (stack on mobile)
- Character portrait placeholder:
  - 300px x 400px
  - Border radius: 12px
  - Subtle border: rgba(255,255,255,0.2)
  - Box shadow for depth
- Character information panel:
  - Character name: Large, bold, white text (48-60px)
  - Descriptor tagline: Italic, accent color, (20-24px)
  - Key stats grid:
    - Age, Sport, Role in series
    - Small cards with icons
    - Semi-transparent backgrounds

Character Profile Section:
- Content in scrollable semi-transparent containers
- Multiple sections with consistent card styling:
  - rgba(45, 74, 110, 0.7) backgrounds
  - 24px padding
  - 12px border radius
  - Margin between sections: 20px

Sections to include:
- **About:** 2-3 paragraphs bio
  - Comfortable reading width (max-width: 800px)
  - Line height: 1.8
  - Font size: 18px
- **Personality:** Bullet points or short paragraphs
- **Background:** Family, history, motivations
- **Sport:** Playing style details with sport icon
- **Relationships:** Grid of linked character cards (mini versions)
- **Character Arc:** Spoiler-free journey overview

Visual Elements:
- Photo gallery (3-5 images) in horizontal scrollable row
  - Image thumbnails: 200px x 250px
  - Border radius: 8px
  - Hover zoom effect
- Character quotes in callout boxes:
  - Distinctive styling with quotation marks
  - Italic text
  - Accent color border-left: 4px
  - Background: rgba(124, 82, 149, 0.3)

Related Episodes Links:
- List of episode cards
- Each card: Episode number, title, "Read" button
- Horizontal layout on desktop, stack on mobile

Right Sidebar (Desktop only):
- "Suggested Books" section
- 4-6 book recommendation cards
- Compact design: small cover + title + CTA

TECHNICAL SPECIFICATIONS:
- Responsive: mobile-first
- Scrollable content with smooth scrolling
- Sticky hamburger menu
- Clear typography hierarchy (h1, h2, h3, p)
- All content maintains WCAG AA contrast over background
- Hover states on all interactive elements
```

---

### 16.3 Episodes Season Overview Page - Google Stitch Prompt

```
Create an episode listing/overview page for "Hockey Shuttle" Season 1 with these specifications:

FULL-SCREEN BACKGROUND:
- Generate a full-screen atmospheric background illustration
- Visual theme: Storytelling and episodic journey
  - Abstract representation of book pages, chapter breaks, or story progression
  - Timeline or path suggesting episodic journey
  - Atmospheric with sense of adventure and progression
- Style: Cinematic, suggesting binge-worthy content
- Color palette: Blues (#1a2332, #2d4a6e), purples (#4a2d5c), with warm accent colors (#ffa94d)
- Background dimmed with overlay (opacity 0.7) for episode card readability

OVERLAID UI ELEMENTS:

Top Right Corner (Fixed):
- Hamburger menu icon (☰) + "Menu" text
- White with text shadow

Page Header:
- Semi-transparent hero card at top
- "Season 1" large heading (60-72px, bold, white)
- Subtitle/tagline: "10 Episodes | Complete Season" with season badge
- Season synopsis (2-3 paragraphs) in readable container:
  - Max-width: 900px
  - Background: rgba(26, 35, 50, 0.85)
  - Padding: 32px
  - Border radius: 16px
  - Centered on page

Episode Grid:
- Grid layout: 3 columns desktop, 2 columns tablet, 1 column mobile
- Gap between cards: 24px
- Each episode card specifications:

  Episode Card Design:
  - Semi-transparent background: rgba(45, 74, 110, 0.75) with backdrop blur
  - Padding: 24px
  - Border radius: 12px
  - Border: 1px solid rgba(255,255,255,0.1)
  - Box shadow: 0 4px 12px rgba(0,0,0,0.3)
  - Hover effect: Lift with increased shadow, scale(1.02), brightness increase

  Card Content:
  - Episode number badge (top-left corner):
    - Small circular or rounded rectangle badge
    - Accent color background
    - White text
  - Episode title: Bold, 24px, white
  - Episode cover thumbnail:
    - Aspect ratio: 16:9 or square
    - Border radius: 8px
    - Placeholder with subtle border
  - Brief teaser/description: 2-3 lines, light gray text
  - Metadata row:
    - Word count icon + number
    - Reading time estimate icon + time
    - Publication date
  - Status badge: "Available" (green) or "Coming Soon" (orange)
  - Three CTA buttons (stacked or horizontal):
    - "Read Online" - Primary accent color (#ff6b4a)
    - "Download PDF" - Secondary button
    - "Download ePub" - Secondary button
  - All buttons with icons and consistent styling

Visual Hierarchy:
- Episode 1 could be slightly larger or featured
- Completed episodes: full opacity
- Upcoming episodes: slightly dimmed (opacity 0.6)

TECHNICAL SPECIFICATIONS:
- CSS Grid layout with responsive breakpoints
- Lazy loading for episode thumbnails
- Smooth hover transitions (250ms ease)
- Accessible button states (focus, hover, active)
- Clear visual distinction between available and upcoming episodes
- Mobile: Cards full-width with good spacing
```

---

### 16.4 Individual Episode Page - Google Stitch Prompt

```
Create an individual episode detail page for "Hockey Shuttle" with these specifications:

FULL-SCREEN BACKGROUND:
- Generate a full-screen atmospheric background illustration
- Visual theme: Episode-specific mood and atmosphere
  - Reflects the episode's key themes (e.g., tension, romance, competition, revelation)
  - Could include sport elements, emotional atmosphere, or setting elements
  - Abstract and atmospheric interpretation
- Style: Cinematic, immersive, emotionally evocative
- Color palette: Consistent with site, with episode-specific mood colors
  - Tense episodes: Darker blues, deep purples, red accents
  - Romantic episodes: Warmer tones, soft purples, pink accents
  - Action episodes: Dynamic lighting, orange/yellow accents
- Background dimmed with overlay for content readability

OVERLAID UI ELEMENTS:

Top Right Corner (Fixed):
- Hamburger menu icon (☰) + "Menu" text

Hero Section:
- Large semi-transparent card: rgba(26, 35, 50, 0.9) with backdrop blur
- Centered layout, max-width: 1000px
- Episode cover art (large):
  - 600px x 400px on desktop
  - Border radius: 16px
  - Box shadow for depth
  - High-quality placeholder
- Episode metadata:
  - Episode number (small badge)
  - Episode title (large, bold, 48-60px, white)
  - Episode tagline/hook (italic, accent color, 20-24px)
- Key info row with icons:
  - Word count
  - Estimated reading time
  - Publication date
  - Content warnings (if applicable)
  - All in small cards with icons

Episode Summary Section:
- Semi-transparent card: rgba(45, 74, 110, 0.8)
- Padding: 32px
- Border radius: 12px
- Max-width: 900px, centered
- Content:
  - Spoiler-free synopsis (2-3 paragraphs)
  - Comfortable typography: 18px, line-height 1.8
  - Key themes as tags/badges
  - Chapter breakdown overview (collapsible list)

Reading Options Section (PROMINENT):
- Large, eye-catching section
- Heading: "Choose Your Reading Format"
- Three option cards in horizontal row (stack on mobile):

  1. Read Online Card:
     - Icon: Browser/screen icon
     - Large button: "Read in Browser"
     - Description: "Comfortable online reading experience"
     - Primary accent color (#ff6b4a)

  2. Download PDF Card:
     - Icon: PDF document icon
     - Large button: "Download PDF"
     - Description: "Print-friendly format"
     - Secondary styling

  3. Download ePub Card:
     - Icon: E-reader icon
     - Large button: "Download ePub"
     - Description: "For e-readers and tablets"
     - Secondary styling

  All cards:
  - Semi-transparent backgrounds
  - Padding: 24px
  - Border radius: 12px
  - Hover effect: lift and glow
  - Clear icons above buttons

Additional Content Sections:
- Character Appearances:
  - Mini character cards in horizontal row
  - Linked to character pages
  - Photos + names
- Location Highlights:
  - Tags or small cards with location names
- Key Quotes:
  - Stylized quote boxes with quotation marks
  - Accent color backgrounds
- What Readers Are Saying:
  - Review/testimonial cards
  - Star ratings, quote, reviewer name

Episode Navigation:
- Bottom of page
- Two large buttons:
  - "← Previous Episode" (left)
  - "Next Episode →" (right)
  - Disabled state if no prev/next
- "Back to Season Overview" link

Right Sidebar (Desktop):
- "Readers Also Love" section
- 4-6 book recommendations
- Amazon affiliate link cards

TECHNICAL SPECIFICATIONS:
- Responsive layout
- Large, accessible buttons for reading options
- Clear visual hierarchy
- Smooth scrolling
- All interactive elements have hover/focus states
- Downloadable files trigger on button click
- Mobile: Sidebar content moves to bottom
```

---

### 16.5 World/Location Pages - Google Stitch Prompt

```
Create location profile pages for the "Hockey Shuttle" universe with these specifications:

NOTE: Create separate variations for each location type:
- St. Paul's High School
- The Rinks (Hockey)
- Badminton Courts
- Winnipeg Locations
- World Overview

FULL-SCREEN BACKGROUND (Location-Specific):
- Generate a full-screen atmospheric background illustration specific to the location

For St. Paul's High School:
- Theme: School hallways, lockers, classroom atmosphere
- Style: Youthful, energetic, high school social dynamics
- Colors: Blues with warm school lighting accents

For The Rinks (Hockey):
- Theme: Ice rink atmosphere with dramatic lighting
- Style: Cold, intense, athletic
- Colors: Icy blues, bright rink lighting, dramatic shadows

For Badminton Courts:
- Theme: Indoor court with nets, shuttlecocks, court lines
- Style: Athletic, precise, competitive
- Colors: Warm court lighting, wood tones, blues

For Winnipeg Locations:
- Theme: The Forks, cityscape, bridges, winter atmosphere
- Style: Urban, seasonal, local culture
- Colors: City lights, seasonal colors (winter whites/blues)

For World Overview:
- Theme: Composite of all locations blended artistically
- Style: Comprehensive, interconnected world
- Colors: Full site palette

All backgrounds:
- Style: Atmospheric, immersive, location-specific
- Dimmed with overlay for text readability (opacity 0.7)

OVERLAID UI ELEMENTS:

Top Right Corner (Fixed):
- Hamburger menu icon (☰) + "Menu" text

Location Header:
- Large semi-transparent hero card
- Location name: Large, bold heading (60-72px, white)
- Subtitle/tagline describing the location
- Background: rgba(26, 35, 50, 0.9)
- Padding: 40px
- Border radius: 16px top

Location Overview Section:
- Semi-transparent card: rgba(45, 74, 110, 0.85)
- Overview text (2-4 paragraphs):
  - Atmospheric description
  - Significance to the story
  - Real-world context (for Winnipeg locations)
  - Comfortable typography: 18px, line-height 1.8
- Max-width: 900px, centered

Photo Gallery:
- Horizontal scrollable row of images
- Each image:
  - 350px x 250px
  - Border radius: 10px
  - Border: 1px solid rgba(255,255,255,0.2)
  - Hover effect: slight zoom
- Smooth horizontal scroll
- Scroll indicators (arrows) on desktop

Key Locations Sub-section (for St. Paul's):
- Grid of location cards (cafeteria, library, gym, etc.)
- Each card:
  - Small photo placeholder
  - Location name
  - Brief description
  - Semi-transparent background
  - 2-3 columns desktop, 1 column mobile

Featured Episodes Section:
- "Episodes Set Here" heading
- Grid of episode cards
- Each card links to episode page
- Contains: episode number, title, small cover, "Read" CTA

Interactive Map (Optional):
- If applicable, stylized map overlay
- Clickable location markers
- Semi-transparent map container
- Zoom/pan functionality

Additional Info Cards:
- Sport-specific details (for rinks/courts)
- Team information
- Cultural context
- Social hierarchy (for school)
- Each in its own semi-transparent card

TECHNICAL SPECIFICATIONS:
- Responsive layout
- Smooth scrolling for galleries
- Location-specific color accents
- All content in readable containers over background
- Mobile: Stack all sections vertically
- Gallery: Swipe gestures on mobile
```

---

### 16.6 Suggested Books Page - Google Stitch Prompt

```
Create a book recommendations page with affiliate links for "Hockey Shuttle" readers with these specifications:

FULL-SCREEN BACKGROUND:
- Generate a full-screen atmospheric background illustration
- Visual theme: Literary and reading atmosphere
  - Abstract bookshelf elements, soft library lighting
  - Cozy reading nook vibes
  - Pages, books, discovery themes
- Style: Warm, inviting, cozy, suggests reading joy and discovery
- Color palette: Warmer tones blended with site blues/purples
  - Warm browns (#4a3f35), soft golds (#d4af37), with site blues
  - Comfortable, welcoming atmosphere
- Background dimmed with overlay for book card readability

OVERLAID UI ELEMENTS:

Top Right Corner (Fixed):
- Hamburger menu icon (☰) + "Menu" text

Page Header:
- Large semi-transparent hero section
- Heading: "If You Love Hockey Shuttle..." (48-60px, white, bold)
- Subheading: "You'll love these books too" (24-28px, light gray)
- Brief intro paragraph (2-3 sentences):
  - Why these books are recommended
  - How recommendations are curated
  - Semi-transparent card background
  - Max-width: 800px, centered

Category Sections:
Create separate sections for each category with consistent styling:

Categories to include:
1. Sports Romance
2. Hockey Romances
3. High School Drama
4. Episodic Series
5. Character-Driven YA

For Each Category Section:
- Category heading (36-42px, white, bold) with accent underline
- Brief category description (1 sentence)
- Grid of book recommendation cards:
  - Layout: 3-4 columns desktop, 2 columns tablet, 1 column mobile
  - Gap: 24px between cards

Book Recommendation Card Design:
- Semi-transparent background: rgba(74, 63, 53, 0.75) with backdrop blur
- Padding: 20px
- Border radius: 12px
- Border: 1px solid rgba(255,255,255,0.15)
- Box shadow for depth
- Hover effect: Lift with scale(1.03) and brightness increase

Card Content:
- Book cover image:
  - Standard book cover aspect ratio (2:3)
  - Max-height: 300px
  - Border radius: 6px
  - Box shadow
  - Placeholder with subtle border
- Book title: Bold, 20-22px, white
- Author name: 16-18px, light gray, below title
- Description (2-3 sentences):
  - 14-16px, line-height 1.6
  - Light gray text
- "Why You'll Love It" callout:
  - Accent color background: rgba(212, 175, 55, 0.3)
  - Italic text
  - 1-2 sentences
  - Padding: 8px
  - Border-radius: 6px
- Rating/accolades (if applicable):
  - Star icons or badge
  - Small text, accent color
- "View on Amazon" button:
  - Accent color (#d4af37)
  - Full-width button
  - Icon: External link or shopping cart
  - Hover effect: Brightness increase
  - Clear affiliate link indicator

Additional Features:
- Filter/Sort Options (top of page):
  - Buttons: "All" | "Sports" | "Romance" | "YA" | "Series"
  - Active state styling
  - Horizontal row on desktop, dropdown on mobile

Featured Sections (Optional):
- "Most Popular This Month" - Highlighted section
- "New Releases" - Badge on recent books
- "Staff Picks" - Special styling

Newsletter Signup Card:
- Prominent card among book recommendations
- Heading: "Get Book Recommendations"
- Email input field
- Subscribe button
- Description of what subscribers get
- Accent color highlights

TECHNICAL SPECIFICATIONS:
- Responsive grid layout
- Lazy loading for book cover images
- Smooth filtering animations
- All affiliate links clearly marked
- Affiliate disclosure statement in footer
- External link icons on Amazon buttons
- Hover states on all interactive elements
- Mobile: Cards stack, maintain readability
```

---

### 16.7 About Page - Google Stitch Prompt

```
Create an "About" page for the "Hockey Shuttle" book series with these specifications:

FULL-SCREEN BACKGROUND:
- Generate a full-screen atmospheric background illustration
- Visual theme: Behind-the-scenes, creative writing, storytelling
  - Abstract typewriter, notebook, creative workspace elements
  - Blend of hockey/badminton elements with writing/creation themes
- Style: Artistic, creative, personal
- Color palette: Site-consistent blues and purples with warm creative accents
- Background dimmed with overlay for readability

OVERLAID UI ELEMENTS:

Top Right Corner (Fixed):
- Hamburger menu icon (☰) + "Menu" text

Page Header:
- Semi-transparent hero section
- "About Hockey Shuttle" heading (60-72px, white, bold)
- Centered layout

About the Series Section:
- Large semi-transparent card: rgba(26, 35, 50, 0.85)
- Max-width: 900px, centered
- Padding: 40px
- Border radius: 16px
- Content:
  - Series overview (3-5 paragraphs)
  - What makes it unique
  - Episode format explanation
  - Target audience
  - Series genesis story
  - Comfortable typography: 18px, line-height 1.8

Key Info Cards:
- Grid of info cards (2-3 columns desktop, 1 column mobile)
- Each card:
  - Semi-transparent background
  - Icon at top
  - Heading
  - Brief description
- Info to include:
  - "10 Episodes" - Episodic format
  - "YA Sports Romance" - Genre
  - "Free to Read" - Access info
  - "Multiple Formats" - PDF/ePub/Online

Contact Section:
- Semi-transparent card
- Heading: "Get in Touch"
- Contact form:
  - Name input field
  - Email input field
  - Message textarea
  - Submit button (accent color)
  - All fields with labels and placeholders
  - Clean, modern form styling
  - Input backgrounds: rgba(255,255,255,0.1)
  - Focus states with accent color borders
- OR contact information:
  - Email address
  - Social media links with icons
  - Links styled consistently

Social Media Links:
- Horizontal row of social icons
- Large, circular icons
- Platforms: Twitter/X, Instagram, TikTok, Wattpad, etc.
- Hover effect: Color fill with platform colors
- Consistent sizing: 50px x 50px

Newsletter Signup (Optional):
- Separate section
- Heading: "Stay Updated"
- Email input + Subscribe button
- Description of what subscribers get

TECHNICAL SPECIFICATIONS:
- Responsive layout
- Form validation (client-side)
- Clear focus states on inputs
- Accessible form labels
- Social links open in new tab
- Mobile: Stack all sections vertically
```

---

### 16.8 Hamburger Menu Component - Google Stitch Prompt

```
Create a hamburger menu navigation component for the "Hockey Shuttle" website with these specifications:

MENU TRIGGER (Visible on All Pages):
- Position: Fixed top-right corner (or top-left)
- Coordinates: top: 20px; right: 20px (or left: 20px)
- Z-index: 1000 (above all content)

Hamburger Icon:
- Three horizontal lines (☰)
- Each line: 24px width, 3px height
- Spacing between lines: 5px
- Color: White
- Hover effect:
  - Slight animation (lines shift slightly)
  - Opacity change or color shift
  - Cursor: pointer

Menu Text:
- Text "Menu" next to icon
- Font: 16-18px, bold
- Color: White
- Letter spacing: 1px
- Margin-left: 10px from icon

Combined Trigger:
- Total size: Minimum 44px x 44px (accessible touch target)
- Background: Semi-transparent rgba(26, 35, 50, 0.6) with backdrop blur (optional)
- Padding: 10px 16px
- Border-radius: 8px (optional)
- Text shadow for visibility over backgrounds
- Transition: all 0.3s ease

MENU OVERLAY (When Opened):

Backdrop:
- Full-screen overlay: 100vw x 100vh
- Background: rgba(0, 0, 0, 0.8)
- Z-index: 999
- Click to close menu
- Fade-in animation (300ms)

Menu Panel:
- Slide-in panel from right (or left)
- Width: 350px desktop, 280px mobile, or 100vw on small screens
- Height: 100vh
- Background: Linear gradient rgba(26, 35, 50, 0.98) to rgba(45, 74, 110, 0.98) with backdrop blur
- Box shadow: -4px 0 20px rgba(0,0,0,0.5) (if sliding from right)
- Z-index: 1000
- Slide-in animation: transform from translateX(100%) to translateX(0), 350ms ease-out

Menu Header:
- Close button (X icon):
  - Position: Top-right of menu panel
  - Size: 40px x 40px
  - Icon: ✕ or × symbol
  - Color: White
  - Hover: Accent color, slight rotation
  - Cursor: pointer
- "Hockey Shuttle" logo/text (optional):
  - Below close button
  - Centered or left-aligned
  - Margin-bottom: 30px

Navigation Links:
- Vertical list of links
- Padding: 20px on sides
- Each link:
  - Font size: 20-24px
  - Font weight: 500-600
  - Color: White
  - Padding: 16px 0
  - Border-bottom: 1px solid rgba(255,255,255,0.1) (optional)
  - Hover effect:
    - Color: Accent color (#ff6b4a or #ffa94d)
    - Padding-left: 10px (slight indent)
    - Transition: all 250ms ease
  - Active page: Accent color, bold

Link Structure:
1. Home
2. Characters
   - Optional sub-navigation (expandable):
     - Sophia Chen
     - Ethan Price
     - Maya Foster
     - Jordan Nakamura
     - Becca Martinez
3. Episodes
   - Optional sub-navigation (expandable):
     - Season 1 Overview
     - Episode 1-10 (collapsible list)
4. World
5. Suggested Books
6. About
7. Contact

Sub-Navigation (Optional):
- Expandable accordion
- Arrow icon (▶ or ▼) indicating expand/collapse
- Sub-items:
  - Font size: 16-18px (smaller than main)
  - Padding-left: 30px (indented)
  - Color: Light gray (#b0b0b0)
  - Hover: White with accent underline

Footer Elements (in Menu):
- Social media icons (bottom of menu):
  - Horizontal row
  - Small icons: 32px x 32px
  - Color: White, hover: Platform colors
  - Margin-top: auto (pushed to bottom)
- Copyright or tagline text:
  - Small, centered
  - Light gray color

ANIMATIONS & INTERACTIONS:
- Menu open:
  1. Backdrop fades in (300ms)
  2. Panel slides in from right (350ms, slight delay after backdrop)
  3. Links fade in staggered (each 50ms delay)
- Menu close:
  1. Panel slides out (300ms)
  2. Backdrop fades out (250ms, slight delay)
- Smooth transitions throughout
- Keyboard accessible: ESC key closes menu
- Focus trap: Tab navigation stays within menu when open
- Screen reader friendly: ARIA labels

TECHNICAL SPECIFICATIONS:
- Fixed positioning for trigger
- CSS transforms for animations
- Backdrop-filter for blur effects (with fallback)
- Accessible (WCAG AA)
- Keyboard navigation support (Tab, Esc, Enter)
- ARIA attributes:
  - aria-label="Main navigation menu"
  - aria-expanded="false/true"
  - role="navigation"
- Mobile responsive:
  - Full-width menu panel on small screens
  - Larger touch targets
  - Swipe to close (optional)
- Z-index management to ensure menu is always on top
```

---

### 16.9 Implementation Workflow with Google Stitch

**Step-by-Step Process:**

1. **Access Google Stitch**
   - Go to https://stitch.withgoogle.com/
   - Sign in with Google account
   - Choose Gemini model (2.5 Pro for detailed designs, 2.5 Flash for faster iterations)

2. **Generate Each Page**
   - Copy the appropriate prompt from sections 16.1-16.8
   - Paste into Google Stitch prompt field
   - Click "Generate" and wait for AI to create the design
   - Review the generated design

3. **Iterate and Refine**
   - If design needs adjustments, provide follow-up prompts:
     - "Make the background more subtle and less aggressive"
     - "Increase contrast for better text readability"
     - "Adjust the color palette to be more blue-dominant"
   - Regenerate until satisfied

4. **Export Options**
   - **HTML + Tailwind CSS:** For modern, utility-first styling
   - **JSX:** If using React/Next.js framework
   - **Figma:** For further design refinement and handoff
   - Choose export format based on your tech stack

5. **Background Image Generation**
   - Use Gemini AI (or MidJourney/DALL-E) to generate the actual background images
   - Prompts for backgrounds extracted from each page prompt
   - Export as high-resolution JPG/PNG (1920px+ width)
   - Optimize for web using tools like TinyPNG or ImageOptim

6. **Integration**
   - Take exported code from Google Stitch
   - Integrate into your static site framework (Next.js, Gatsby, Hugo, etc.)
   - Replace placeholder images with actual content
   - Add actual episode text, character bios, etc.
   - Integrate Amazon affiliate links

7. **Consistency Check**
   - Ensure hamburger menu component is identical across all pages
   - Verify color palette consistency
   - Check typography hierarchy matches across pages
   - Test responsive behavior on multiple devices

8. **Testing**
   - Cross-browser testing (Chrome, Firefox, Safari, Edge)
   - Mobile responsiveness testing
   - Accessibility testing (WCAG AA compliance)
   - Performance testing (page load times)

**Tips for Best Results:**
- Generate all pages in one session to maintain consistency
- Save all prompts and generated designs for future reference
- Use Stitch's iteration feature to refine designs
- Export to Figma for precise adjustments if needed
- Maintain a design system document for colors, fonts, spacing

---

**Document Version:** 1.0
**Last Updated:** November 15, 2025
**Author:** Hockey Shuttle Project Team
**Status:** Ready for Review and Approval
