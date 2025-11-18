// Google Analytics (gtag.js)
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-B5DQQMWNMW');

// Event tracking helpers
function trackDownload(filename, format) {
  gtag('event', 'download', {
    'event_category': 'Downloads',
    'event_label': filename,
    'file_format': format
  });
}

function trackWattpadClick(episodeName) {
  gtag('event', 'click', {
    'event_category': 'External Link',
    'event_label': 'Wattpad - ' + episodeName,
    'link_type': 'read_now'
  });
}

function trackCharacterView(characterName) {
  gtag('event', 'page_view', {
    'event_category': 'Character Pages',
    'event_label': characterName
  });
}
