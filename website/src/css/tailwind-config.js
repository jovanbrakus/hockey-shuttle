// Tailwind CSS Configuration for The Boy Who Knew Me First Website
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "primary": "#ff6d4d",
        "primary-light": "#ff8c6b",
        "primary-dark": "#ff6b4a",
        "background-light": "#f8f6f5",
        "background-dark": "#1a2332",
        "surface-dark": "#2d4a6e",
        "surface-darker": "#1a2332",
        "accent-warm": "#ffa94d",
        "accent-purple": "#7c5295",
        "text-light": "#e0e0e0",
      },
      fontFamily: {
        "display": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
        "body": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
      },
      borderRadius: {
        "DEFAULT": "0.25rem",
        "lg": "0.5rem",
        "xl": "0.75rem",
        "2xl": "1rem",
        "full": "9999px"
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
        '100': '25rem',
        '112': '28rem',
        '128': '32rem',
      },
      maxWidth: {
        '8xl': '88rem',
        '9xl': '96rem',
      },
      zIndex: {
        '60': '60',
        '70': '70',
        '80': '80',
        '90': '90',
        '100': '100',
      }
    },
  },
}
