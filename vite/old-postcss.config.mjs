module.exports = {
  plugins: {
    tailwindcss: {
      config: {
        content: [
          "./pages/**/*.{js,ts,jsx,tsx}",
          "./components/**/*.{js,ts,jsx,tsx}",
        ],
        plugins: [
          require("@tailwindcss/typography"),
          require("@tailwindcss/forms"),
        ],
      },
    },
    autoprefixer: {},
  },
};