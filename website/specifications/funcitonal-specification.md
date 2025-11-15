# Functional Specification: Book Website

## Overview
This document outlines the functional specifications for a book website that showcases the episodic YA novel series. The website features a visually rich, immersive design with full-screen background visuals on each page and a minimalist navigation approach.

## Design Philosophy

### Visual Approach
- Each page features a **full-screen background drawing/visual** generated using Gemini AI
- Background visuals should be **subtle and atmospheric**, not overly aggressive
- UI elements and content overlay on top of the background
- Consistent visual theme across all pages that reflects the book's tone and genre

### Navigation
- **NO always-present navigation bar**
- Instead: A **hamburger menu icon** with "Menu" text next to it
- The hamburger menu should be easily visible on all pages
- When clicked, it opens a menu overlay/sidebar with all available pages
- Clean, minimal navigation that doesn't distract from the immersive visuals

## Pages Structure

### 1. Home Page
**Purpose**: Landing page that captures visitors' attention and introduces the book series

**Key Elements**:
- Full-screen atmospheric background visual
- Book title and tagline prominently displayed
- Brief hook/teaser text (1-2 sentences)
- Call-to-action button: "Start Reading" or "Explore Episodes"
- Hamburger menu icon + "Menu" text (top-left or top-right corner)

**Content**:
- Hero section with title overlay
- Minimal, impactful text
- Visual should evoke the book's atmosphere (YA, dramatic, engaging)

---

### 2. About the Book
**Purpose**: Provide comprehensive information about the book series

**Key Elements**:
- Full-screen background visual (related to book themes)
- Content overlay with semi-transparent background for readability
- Book synopsis (2-3 paragraphs)
- Genre and target audience information
- Key themes and what makes this series unique
- Episodic format explanation

**Content**:
- Engaging description of the premise
- What readers can expect
- Episode release schedule (if applicable)
- Any awards or recognition

---

### 3. Characters
**Purpose**: Introduce main and supporting characters

**Key Elements**:
- Full-screen background visual (character-themed)
- Character cards/profiles overlaying the background
- Each character profile includes:
  - Character name
  - Brief description (personality, role in story)
  - Character illustration/portrait (if available)
- Interactive or scrollable character list

**Content**:
- Main protagonist(s)
- Key supporting characters
- Brief, spoiler-free descriptions
- Visual representations when possible

---

### 4. Episodes
**Purpose**: Display available episodes and provide reading access

**Key Elements**:
- Full-screen background visual (story/adventure themed)
- Episode grid/list overlay
- Each episode card shows:
  - Episode number
  - Episode title
  - Brief description/teaser
  - Publication date
  - "Read Now" button
  - Episode cover art thumbnail (if available)
- Clear indication of completed vs upcoming episodes

**Content**:
- All published episodes
- Teasers for upcoming episodes
- Reading progress tracking (optional)
- Links to reading platform (Wattpad, etc.)

---

### 5. Contact
**Purpose**: Enable readers to connect with the author

**Key Elements**:
- Full-screen background visual (connection/communication themed)
- Contact form overlay or contact information display
- Social media links
- Newsletter signup (if applicable)

**Content**:
- Contact form fields:
  - Name
  - Email
  - Message/Comments
  - Submit button
- Social media icons and links
- Email address (if sharing directly)
- Response time expectations

---

## Technical Requirements

### Responsive Design
- All pages must be fully responsive
- Background visuals should scale appropriately across devices
- Mobile: Hamburger menu especially important
- Desktop: Larger visual real estate for background images
- Tablet: Optimized layout for medium screens

### Navigation Menu
**Hamburger Menu Specifications**:
- Icon: Standard 3-line hamburger icon
- Label: "Menu" text displayed next to icon
- Position: Fixed position (e.g., top-right corner)
- Visibility: Always visible on all pages
- Color: Contrasts with background (white/dark depending on page)

**Menu Content**:
When opened, displays:
- Home
- About the Book
- Characters
- Episodes
- Contact

**Menu Behavior**:
- Smooth slide-in animation (from side)
- Click outside to close
- Close button within menu
- Overlay darkens background when open
- Maintains z-index above all page content

### Performance
- Optimized background images for fast loading
- Lazy loading for images below the fold
- Minimal JavaScript for smooth experience
- Progressive enhancement approach

### Accessibility
- Proper contrast ratios for text over background images
- Alt text for all images
- Keyboard navigation support
- Screen reader compatible
- ARIA labels for hamburger menu

---

## Color Scheme & Typography

### Colors
- Primary: To be determined based on book branding
- Text: High contrast for readability over backgrounds
- Menu overlay: Semi-transparent dark overlay
- Accent colors for CTAs and interactive elements

### Typography
- Headings: Bold, readable font (YA-appropriate)
- Body text: Clean, legible font
- Minimum font size: 16px for body text
- Proper line height for readability

---

## Content Management

### Updates
- Easy to update episode information
- Ability to add new episodes without code changes
- Simple content editing workflow

### Assets
- Background visuals generated via Gemini AI
- Character illustrations
- Episode cover art
- Book logo/branding assets

---

# Google Stitch - AI Designer Prompts

Below are the detailed prompts for Google Stitch AI Designer to generate each page of the website. These prompts are designed to create the full visual layout including the full-screen background visuals and overlaid UI elements.

## Page 1: Home Page

**Google Stitch Prompt:**

```
Create a modern, immersive landing page for a YA novel website with these specifications:

BACKGROUND:
- Full-screen atmospheric background illustration covering the entire viewport
- Visual theme: dramatic, moody, young adult fiction aesthetic with subtle hockey elements in the background
- Color palette: deep blues, purples, and dramatic lighting
- Style: subtle, not overly aggressive - atmospheric and cinematic
- The background should evoke mystery, youth, and intensity

LAYOUT & UI ELEMENTS:
- Top right corner: Hamburger menu icon (three horizontal lines) with "Menu" text next to it in white
- Center of screen: Large, bold book title "HOCKEY SHUTTLE" with dramatic typography
- Below title: Compelling tagline in smaller text (1-2 lines)
- Center-bottom: Call-to-action button "Start Reading" with hover effect
- All text should have subtle shadows or semi-transparent backgrounds for readability

DESIGN STYLE:
- Minimalist, modern design
- Glass morphism or subtle dark overlays for text containers
- Responsive layout that works on desktop and mobile
- Typography: Bold, contemporary fonts suitable for YA audience
- All interactive elements should have clear hover states

TECHNICAL:
- Mobile-first responsive design
- Background image should cover and center
- Z-index layering: background (0), content overlay (1), menu (2)
```

---

## Page 2: About the Book

**Google Stitch Prompt:**

```
Create an "About the Book" page for a YA novel website with these specifications:

BACKGROUND:
- Full-screen background illustration covering entire viewport
- Visual theme: action-oriented, showing abstract hockey rink elements, dramatic lighting, youthful energy
- Color palette: continuation of home page colors - blues, purples, dramatic contrasts
- Style: atmospheric but not distracting, allows content to be readable on top
- Evokes the episodic, binge-worthy nature of the story

LAYOUT & UI ELEMENTS:
- Top right corner: Hamburger menu icon with "Menu" text (consistent with home page)
- Main content area: Semi-transparent dark card/container (glass morphism effect) positioned center or slightly off-center
- Inside content container:
  - "About the Book" heading at top
  - Book synopsis text (2-3 paragraphs with proper spacing)
  - Section for genre and target audience info
  - Section highlighting episodic format
  - Key themes or unique selling points in bullet or card format

DESIGN STYLE:
- Content card with backdrop-blur effect or subtle gradient overlay
- Comfortable reading width (max-width ~800px)
- Generous padding and line height for readability
- Typography: Clear hierarchy with headings and body text
- Accent colors for highlighting key information

TECHNICAL:
- Responsive design that stacks on mobile
- Scrollable content if necessary
- Background image fixed or parallax effect
- Readable text contrast (WCAG AA compliant)
```

---

## Page 3: Characters

**Google Stitch Prompt:**

```
Create a "Characters" page for a YA novel website with these specifications:

BACKGROUND:
- Full-screen background illustration covering entire viewport
- Visual theme: character-focused atmosphere, hints of team/group dynamics, hockey arena atmosphere
- Color palette: consistent with site - blues, purples, with warmer accent tones
- Style: subtle and atmospheric, allows character cards to stand out
- Should feel dynamic but not overwhelming

LAYOUT & UI ELEMENTS:
- Top right corner: Hamburger menu icon with "Menu" text
- Page heading "Characters" near top with dramatic typography
- Character card grid layout (2-3 columns on desktop, 1 column on mobile)
- Each character card contains:
  - Character portrait placeholder or illustration area
  - Character name in bold
  - Role/description text (2-3 lines)
  - Semi-transparent background for card
- Cards have hover effects (slight scale or glow)

DESIGN STYLE:
- Grid or masonry layout for character cards
- Glass morphism or frosted glass effect on cards
- Consistent card sizing with rounded corners
- Cards should contrast with background but feel integrated
- Modern, clean typography
- Subtle shadows and depth effects

TECHNICAL:
- Responsive grid (3 columns → 2 columns → 1 column)
- CSS Grid or Flexbox layout
- Smooth hover transitions
- Scroll behavior: smooth scrolling for long character lists
- Cards maintain readability over background
```

---

## Page 4: Episodes

**Google Stitch Prompt:**

```
Create an "Episodes" page for a YA novel website with these specifications:

BACKGROUND:
- Full-screen background illustration covering entire viewport
- Visual theme: storytelling/adventure atmosphere, suggesting journey and progression
- Visual elements: abstract book pages, chapter breaks, or episodic progression imagery
- Color palette: site-consistent blues and purples with accent colors for CTAs
- Style: atmospheric, cinematic, suggests binge-worthy content

LAYOUT & UI ELEMENTS:
- Top right corner: Hamburger menu icon with "Menu" text
- Page heading "Episodes" with subtitle explaining the episodic format
- Episode grid/list layout (2 columns on desktop, 1 on mobile)
- Each episode card displays:
  - Episode number badge or label
  - Episode title in prominent text
  - Episode cover thumbnail (placeholder with subtle border)
  - Brief teaser/description (2-3 lines)
  - Publication date
  - "Read Now" button with clear CTA styling
  - Visual indicator for status (published/upcoming)

DESIGN STYLE:
- Cards with semi-transparent backgrounds
- Episode thumbnails with consistent aspect ratio
- Clear visual hierarchy within each card
- "Read Now" buttons with accent color and hover effects
- Published episodes: full opacity, clickable
- Upcoming episodes: slightly dimmed, labeled "Coming Soon"
- Modern card design with shadows and spacing

TECHNICAL:
- Responsive grid layout
- Lazy loading for episode thumbnails
- Filtering or sorting options (optional)
- Clear active/inactive states for buttons
- Maintains readability over background image
```

---

## Page 5: Contact

**Google Stitch Prompt:**

```
Create a "Contact" page for a YA novel website with these specifications:

BACKGROUND:
- Full-screen background illustration covering entire viewport
- Visual theme: connection and communication - abstract flowing lines, networked patterns, or open/welcoming atmosphere
- Color palette: site-consistent with slightly warmer tones to feel inviting
- Style: calm, approachable, atmospheric but not busy
- Should feel welcoming and accessible

LAYOUT & UI ELEMENTS:
- Top right corner: Hamburger menu icon with "Menu" text
- Center content area with semi-transparent container
- "Get in Touch" or "Contact" heading
- Contact form with fields:
  - Name input field (with label)
  - Email input field (with label)
  - Message textarea (larger, multi-line)
  - Submit button with accent color and hover effect
- Below or beside form:
  - Social media icons (horizontal row)
  - Each icon links to respective platform
  - Newsletter signup option (optional)

DESIGN STYLE:
- Clean, modern form design
- Input fields with clear borders or subtle backgrounds
- Form container with glass morphism or semi-transparent dark background
- Generous spacing between form elements
- Typography: welcoming and friendly
- Social icons: consistent size, with hover effects
- Visual feedback for form validation

TECHNICAL:
- Responsive layout (form stacks on mobile)
- Form validation (client-side)
- Clear focus states for accessibility
- Proper input types (email, text, textarea)
- Submit button with loading state
- Background maintains fixed position during scroll
```

---

## Hamburger Menu Component

**Google Stitch Prompt for Menu Overlay:**

```
Create a hamburger menu overlay component with these specifications:

TRIGGER ELEMENT (visible on all pages):
- Hamburger icon: three horizontal lines, clean and minimal
- Text label "Menu" displayed next to icon
- Position: fixed top-right corner (or top-left)
- Styling: white with subtle shadow for visibility over backgrounds
- Size: easily tappable (44px minimum touch target)
- Hover effect: slight scale or color change

MENU OVERLAY (when opened):
- Slide-in animation from the side (left or right)
- Full-height overlay panel (300-400px width on desktop)
- Background: semi-transparent dark overlay (rgba) with backdrop blur
- Close button (X icon) in top corner of menu panel

MENU CONTENT:
- Vertical list of navigation links:
  1. Home
  2. About the Book
  3. Characters
  4. Episodes
  5. Contact
- Each link:
  - Large, readable text
  - Generous padding (easy to click)
  - Hover effect (color change or underline)
  - Active page highlighted
- Consistent typography with site design

BEHAVIOR:
- Clicking outside menu closes it
- Backdrop darkens page content behind menu
- Smooth slide-in/out animations (300ms)
- Links are keyboard navigable
- Proper focus management for accessibility

TECHNICAL:
- Fixed positioning for menu icon
- Z-index: menu overlay above all page content
- Mobile-friendly (full-width on small screens)
- Accessible (ARIA labels, keyboard support)
- Responsive font sizes
```

---

## Design System Notes for Google Stitch

When implementing these pages in Google Stitch, ensure:

1. **Consistency**: All pages should share:
   - Same hamburger menu component
   - Consistent color palette
   - Unified typography system
   - Similar overlay/card effects
   - Matching animation timing

2. **Background Images**:
   - Use Gemini to generate atmospheric, subtle backgrounds
   - Ensure backgrounds don't overpower content
   - Consider dimming or overlay effects for text readability

3. **Accessibility**:
   - Maintain WCAG AA contrast ratios minimum
   - All interactive elements keyboard accessible
   - Proper heading hierarchy (h1, h2, h3)
   - Alt text for images

4. **Responsive Behavior**:
   - Mobile-first approach
   - Breakpoints: 768px (tablet), 1024px (desktop)
   - Touch-friendly sizing on mobile
   - Hamburger menu essential on all screen sizes

5. **Export Options**:
   - Export as HTML/Tailwind CSS or JSX
   - Can be further refined in Figma if needed
   - Ensure background images are optimized for web

---

## Implementation Notes

These Google Stitch prompts are designed to generate the initial UI designs. After generation:

1. Review each design for consistency
2. Adjust colors and spacing as needed
3. Replace placeholder content with actual book content
4. Generate actual background visuals using Gemini AI based on the themes described
5. Export code and integrate into your web framework
6. Add any additional interactivity or animations
7. Test responsiveness across devices
8. Optimize images and performance

The generated designs will serve as the foundation for the book website, providing both the visual aesthetics and functional layout needed for an engaging, immersive reading experience.
