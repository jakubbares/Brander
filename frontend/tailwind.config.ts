import { type Config } from "tailwindcss";

export default {
  content: ["./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    fontFamily: {
      sans: ["Inter", "sans-serif"],
    },
    colors: {
      light: "#575757",
      lighter: "#B9AFAF"
    },
    extend: {
        backgroundImage: {
          'gradient': "url('/img/bg.png')",
      }
    },
  },
  plugins: [require("daisyui")],
  daisyui: {
    darkTheme: "light",
  },
} satisfies Config;
