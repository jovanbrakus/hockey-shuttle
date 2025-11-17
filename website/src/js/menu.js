// Hamburger Menu Component for The Boy Who Knew Me First Website

document.addEventListener('DOMContentLoaded', function() {
  // Create menu overlay and panel
  createMenuElements();

  // Attach event listeners
  attachMenuListeners();
});

function createMenuElements() {
  // Create overlay backdrop
  const overlay = document.createElement('div');
  overlay.id = 'menu-overlay';
  overlay.className = 'fixed inset-0 bg-black/80 z-[998] opacity-0 pointer-events-none transition-opacity duration-300';
  document.body.appendChild(overlay);

  // Create menu panel
  const menuPanel = document.createElement('div');
  menuPanel.id = 'menu-panel';
  menuPanel.className = 'fixed top-0 right-0 h-full w-[350px] sm:w-[400px] bg-gradient-to-b from-[rgba(26,35,50,0.98)] to-[rgba(45,74,110,0.98)] backdrop-blur-lg z-[999] transform translate-x-full transition-transform duration-350 ease-out shadow-2xl overflow-y-auto';

  menuPanel.innerHTML = `
    <div class="p-6">
      <!-- Close Button -->
      <button id="menu-close" class="flex items-center justify-center w-10 h-10 ml-auto text-white transition-all rounded-full hover:bg-white/10 hover:rotate-90">
        <span class="material-symbols-outlined text-2xl">close</span>
      </button>

      <!-- Logo/Title -->
      <div class="mt-4 mb-8 text-center">
        <h2 class="text-xl font-bold text-white uppercase tracking-wider">The Boy Who<br/>Knew Me First</h2>
      </div>

      <!-- Navigation Links -->
      <nav class="space-y-2">
        <a href="index.html" class="flex items-center gap-3 px-4 py-3 text-lg font-medium text-white transition-all rounded-lg hover:bg-white/10 hover:pl-6 hover:text-[#ff6b4a]">
          <span class="material-symbols-outlined">home</span>
          <span>Home</span>
        </a>

        <!-- Characters with submenu -->
        <div>
          <button id="characters-toggle" class="flex items-center justify-between w-full px-4 py-3 text-lg font-medium text-white transition-all rounded-lg hover:bg-white/10 hover:text-[#ff6b4a]">
            <div class="flex items-center gap-3">
              <span class="material-symbols-outlined">group</span>
              <span>Characters</span>
            </div>
            <span class="material-symbols-outlined transition-transform" id="characters-arrow">expand_more</span>
          </button>
          <div id="characters-submenu" class="hidden pl-8 mt-2 space-y-1">
            <a href="sophia-chen.html" class="block px-4 py-2 text-sm text-[#e0e0e0] transition-all rounded-lg hover:bg-white/10 hover:text-white hover:pl-6">
              Sophia Chen
            </a>
            <a href="ethan-price.html" class="block px-4 py-2 text-sm text-[#e0e0e0] transition-all rounded-lg hover:bg-white/10 hover:text-white hover:pl-6">
              Ethan Price
            </a>
            <a href="maya-foster.html" class="block px-4 py-2 text-sm text-[#e0e0e0] transition-all rounded-lg hover:bg-white/10 hover:text-white hover:pl-6">
              Maya Foster
            </a>
            <a href="jordan-nakamura.html" class="block px-4 py-2 text-sm text-[#e0e0e0] transition-all rounded-lg hover:bg-white/10 hover:text-white hover:pl-6">
              Jordan Nakamura
            </a>
            <a href="becca-martinez.html" class="block px-4 py-2 text-sm text-[#e0e0e0] transition-all rounded-lg hover:bg-white/10 hover:text-white hover:pl-6">
              Becca Martinez
            </a>
          </div>
        </div>

        <a href="episodes.html" class="flex items-center gap-3 px-4 py-3 text-lg font-medium text-white transition-all rounded-lg hover:bg-white/10 hover:pl-6 hover:text-[#ff6b4a]">
          <span class="material-symbols-outlined">menu_book</span>
          <span>Episodes</span>
        </a>

        <a href="world.html" class="flex items-center gap-3 px-4 py-3 text-lg font-medium text-white transition-all rounded-lg hover:bg-white/10 hover:pl-6 hover:text-[#ff6b4a]">
          <span class="material-symbols-outlined">public</span>
          <span>World</span>
        </a>

        <a href="books.html" class="flex items-center gap-3 px-4 py-3 text-lg font-medium text-white transition-all rounded-lg hover:bg-white/10 hover:pl-6 hover:text-[#ff6b4a]">
          <span class="material-symbols-outlined">auto_stories</span>
          <span>Suggested Books</span>
        </a>

        <a href="about.html" class="flex items-center gap-3 px-4 py-3 text-lg font-medium text-white transition-all rounded-lg hover:bg-white/10 hover:pl-6 hover:text-[#ff6b4a]">
          <span class="material-symbols-outlined">info</span>
          <span>About</span>
        </a>

        <a href="https://www.wattpad.com/story/403958141-the-boy-who-knew-me-first" target="_blank" class="flex items-center gap-3 px-4 py-3 text-lg font-medium transition-all rounded-lg bg-gradient-to-r from-[#ff6b4a] to-[#ff8c6b] hover:brightness-110 hover:scale-105 mt-4">
          <span class="material-symbols-outlined">open_in_new</span>
          <span>Read on Wattpad</span>
        </a>
      </nav>

      <!-- Social Media (placeholder) -->
      <div class="mt-auto pt-8 border-t border-white/10">
        <p class="text-xs text-center text-[#b0b0b0]">© 2025 The Boy Who Knew Me First</p>
      </div>
    </div>
  `;

  document.body.appendChild(menuPanel);
}

function attachMenuListeners() {
  const menuButton = document.querySelector('header button');
  const overlay = document.getElementById('menu-overlay');
  const menuPanel = document.getElementById('menu-panel');
  const closeButton = document.getElementById('menu-close');
  const charactersToggle = document.getElementById('characters-toggle');
  const charactersSubmenu = document.getElementById('characters-submenu');
  const charactersArrow = document.getElementById('characters-arrow');

  // Open menu
  if (menuButton) {
    menuButton.addEventListener('click', openMenu);
  }

  // Close menu
  if (closeButton) {
    closeButton.addEventListener('click', closeMenu);
  }

  if (overlay) {
    overlay.addEventListener('click', closeMenu);
  }

  // Toggle characters submenu
  if (charactersToggle) {
    charactersToggle.addEventListener('click', function() {
      charactersSubmenu.classList.toggle('hidden');
      charactersArrow.classList.toggle('rotate-180');
    });
  }

  // Close on ESC key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      closeMenu();
    }
  });
}

function openMenu() {
  const overlay = document.getElementById('menu-overlay');
  const menuPanel = document.getElementById('menu-panel');

  if (overlay && menuPanel) {
    overlay.classList.remove('opacity-0', 'pointer-events-none');
    overlay.classList.add('opacity-100');
    menuPanel.classList.remove('translate-x-full');
    menuPanel.classList.add('translate-x-0');

    // Prevent body scroll when menu is open
    document.body.style.overflow = 'hidden';
  }
}

function closeMenu() {
  const overlay = document.getElementById('menu-overlay');
  const menuPanel = document.getElementById('menu-panel');

  if (overlay && menuPanel) {
    overlay.classList.remove('opacity-100');
    overlay.classList.add('opacity-0', 'pointer-events-none');
    menuPanel.classList.remove('translate-x-0');
    menuPanel.classList.add('translate-x-full');

    // Restore body scroll
    document.body.style.overflow = '';
  }
}
