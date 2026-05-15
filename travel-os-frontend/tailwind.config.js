/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: "class",
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "SF Pro Display", "system-ui", "sans-serif"],
      },
      colors: {
        os: {
          bg: "#020817",
          panel: "#0a0f1e",
          border: "#1e293b",
          accent: "#6366f1",
          accentHover: "#4f46e5",
          text: "#f8fafc",
          muted: "#94a3b8",
        },
      },
    },
  },
  plugins: [],
};
