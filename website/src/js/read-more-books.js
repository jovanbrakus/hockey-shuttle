/**
 * Read More Books - Displays random books from similar-books.js in the sidebar
 */

// Function to get random items from array
function getRandomBooks(arr, count) {
  const shuffled = [...arr].sort(() => 0.5 - Math.random());
  return shuffled.slice(0, count);
}

// Function to render book cards
function renderReadMoreBooks() {
  const container = document.getElementById('read-more-books');
  if (!container || typeof similarBooks === 'undefined') return;

  const randomBooks = getRandomBooks(similarBooks, 5);

  container.innerHTML = randomBooks.map(book => `
    <div class="flex items-start gap-4">
      <div class="h-24 w-16 shrink-0 rounded bg-cover bg-center"
           style="background-image: url('../images/book-covers/${book.cover}')"
           alt="${book.title} cover"></div>
      <div class="flex flex-col">
        <h4 class="font-bold leading-tight text-white">${book.title}</h4>
        <p class="mt-1 text-sm leading-snug text-text-subtle">${book.description}</p>
        <a class="mt-2 text-sm font-semibold text-primary hover:underline"
           href="${book.amazonLink}"
           target="_blank"
           rel="noopener noreferrer">Read now</a>
      </div>
    </div>
  `).join('');
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', renderReadMoreBooks);
