# The Boy Who Knew Me First - Website Build

This directory contains the built website files for "The Boy Who Knew Me First" book series.

## Directory Structure

```
website/build/
├── css/
│   ├── styles.css              # Base CSS framework with custom utilities
│   └── tailwind-config.js      # Tailwind CSS configuration
├── js/
│   └── (future JavaScript files)
├── images/
│   ├── bg-landing.png          # Landing page background (crossed equipment)
│   ├── series-cover.png        # Main series cover
│   ├── sophia-chen.png         # Character portrait
│   ├── ethan-price.png         # Character portrait
│   ├── bg-hockey.png           # Hockey atmosphere
│   ├── bg-badminton.png        # Badminton atmosphere
│   └── bg-romance.png          # Romance atmosphere
└── pages/
    └── index.html              # Landing page

```

## CSS Framework

The CSS framework is extracted from the templates and provides:

### Custom Utility Classes

- **`.text-shadow`** - Adds text shadow for better readability over backgrounds
- **`.box-shadow`** - Adds box shadow for depth on buttons and cards
- **`.glass-card`** - Semi-transparent card with backdrop blur (dark variant)
- **`.glass-card-light`** - Semi-transparent card with backdrop blur (light variant)
- **`.glass-card-dark`** - Semi-transparent card with backdrop blur (darker variant)
- **`.bg-fullscreen`** - Fixed full-screen background
- **`.bg-overlay`** - Gradient overlay for backgrounds
- **`.hover-lift`** - Lift effect on hover with shadow
- **`.character-card`** - Character card with hover animation
- **`.btn-primary`** - Primary button with gradient
- **`.btn-secondary`** - Secondary button with transparency

### Tailwind Configuration

Custom colors:
- **Primary**: `#ff6d4d` (coral/orange)
- **Primary Light**: `#ff8c6b`
- **Primary Dark**: `#ff6b4a`
- **Background Dark**: `#1a2332` (deep blue-gray)
- **Surface Dark**: `#2d4a6e` (medium blue)
- **Accent Warm**: `#ffa94d` (warm orange)
- **Accent Purple**: `#7c5295`

Font family:
- **Display/Body**: Plus Jakarta Sans

## Usage

### Adding the Framework to New Pages

1. **Include Tailwind CSS** (via CDN):
```html
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
```

2. **Include Google Fonts**:
```html
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet"/>
```

3. **Include Tailwind Config**:
```html
<script src="../css/tailwind-config.js"></script>
```

4. **Include Custom Styles**:
```html
<link rel="stylesheet" href="../css/styles.css"/>
```

### Full-Screen Background Pattern

```html
<!-- Background layer -->
<div class="fixed inset-0 z-0 h-screen w-screen bg-cover bg-center"
     style='background-image: linear-gradient(rgba(0, 0, 0, 0.3) 0%, rgba(0, 0, 0, 0.5) 100%), url("../images/bg-landing.png");'>
</div>

<!-- Content layer -->
<div class="relative z-10 flex min-h-screen w-full flex-col items-center overflow-x-hidden p-4 sm:p-6 md:p-8">
  <!-- Your content here -->
</div>
```

### Glass Morphism Cards

```html
<div class="rounded-xl border border-white/10 bg-[rgba(26,35,50,0.7)] p-6 backdrop-blur-md">
  <!-- Card content -->
</div>
```

### Character Cards

```html
<div class="group flex flex-col items-center gap-4 rounded-xl border border-white/10 bg-[rgba(45,74,110,0.6)] p-5 text-center backdrop-blur-md transition-transform duration-300 hover:-translate-y-2 hover:scale-105">
  <div class="h-24 w-24 rounded-full bg-cover bg-center"
       style='background-image: url("../images/character.png");'>
  </div>
  <div class="flex flex-col">
    <p class="text-lg font-bold leading-tight text-white">Character Name</p>
    <p class="text-sm font-normal leading-normal text-[#e0e0e0]">Character Tagline</p>
  </div>
</div>
```

### Buttons

Primary button:
```html
<button class="box-shadow flex cursor-pointer items-center justify-center overflow-hidden rounded-lg bg-gradient-to-r from-[#ff6b4a] to-[#ff8c6b] px-8 py-4 text-base font-semibold text-white transition-all hover:scale-105 hover:brightness-110">
  <span class="truncate">Button Text</span>
</button>
```

Secondary button:
```html
<button class="flex cursor-pointer items-center justify-center overflow-hidden rounded-lg bg-white/10 px-6 py-3 text-sm font-semibold text-white transition-colors hover:bg-white/20">
  <span class="truncate">Button Text</span>
</button>
```

### Hamburger Menu

```html
<header class="fixed top-0 right-0 z-50 p-4 md:p-6">
  <button class="flex h-[44px] w-auto cursor-pointer items-center justify-center gap-2 rounded-full px-4 text-white transition-transform hover:scale-105 hover:opacity-90">
    <span class="material-symbols-outlined text-shadow">menu</span>
    <span class="text-base font-medium text-shadow">Menu</span>
  </button>
</header>
```

## Design Principles

1. **Full-Screen Backgrounds**: Every page uses a full-screen atmospheric background with overlay
2. **Glass Morphism**: All content cards use semi-transparent backgrounds with backdrop blur
3. **Accessibility**: Minimum 44px touch targets, proper ARIA labels, keyboard navigation
4. **Responsive**: Mobile-first design with breakpoints at 768px (tablet), 1024px (desktop)
5. **Performance**: Optimized images, lazy loading where applicable
6. **Consistency**: Shared color palette, typography, and component styles across all pages

## Color Usage Guidelines

- **Primary (coral/orange)**: CTAs, important buttons, accent elements
- **Background Dark (deep blue)**: Main backgrounds for cards and overlays
- **Surface Dark (medium blue)**: Secondary cards and surfaces
- **Accent Warm (orange)**: Labels, badges, highlights
- **Accent Purple**: Alternative accent for variety
- **Text Light**: Body text on dark backgrounds

## Typography

- **Hero Headings**: 3rem - 6rem (clamp), font-weight 900, uppercase
- **Section Headings**: 1.875rem - 2.5rem (clamp), font-weight 700
- **Body Text**: 1.125rem, line-height 1.75
- **Small Text**: 0.875rem for metadata and labels

## Responsive Breakpoints

- **Mobile**: 320px - 767px (default, mobile-first)
- **Tablet**: 768px - 1023px
- **Desktop**: 1024px - 1439px
- **Large Desktop**: 1440px+

## Future Enhancements

- [ ] Add navigation menu (hamburger functionality)
- [ ] Create episode listing page
- [ ] Create character detail pages
- [ ] Add reading interface
- [ ] Implement download functionality (PDF/ePub)
- [ ] Add book recommendations page
- [ ] Create about page
- [ ] Add analytics integration
- [ ] Implement PWA features for offline reading

## Notes

- All images are stored in `/images/` directory
- Background images should be optimized for web (compressed)
- Character portraits can be generated or placeholder gradients
- The framework is designed to work with TailwindCSS via CDN for rapid prototyping
- For production, consider compiling Tailwind to reduce file size

## Credits

- Design framework: Based on Google Stitch generated templates
- Visuals: Generated using AI (stored in `/series/hockey-shuttle/10-visuals/`)
- Typography: Plus Jakarta Sans (Google Fonts)
- Icons: Material Symbols (Google Fonts)
