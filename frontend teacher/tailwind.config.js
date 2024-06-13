/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{js,jsx,ts,tsx}", "./index.html"],
  theme: {
    extend: {},
    colors: {
      primary: "#0000FF",
      primary2: "#316DFF",
      primary3: "#74C4FE",
      primaryText: "#001445",
      primaryText2: "#316DFF",
      black: "#222222",
      neg: "#F24747",
      posit: "#3FFF52",
      white: "#F2F2F2",
      grey1: "#333333",
      grey2: "#666666",
      grey3: "#999999",
      grey4: "#CCCCCC",
      excelent: "#A0FC74",
      good: "#FFF173",
      satisfactory: "#F39D1A",
      unsatisfactory: "#FC7474",
      bad: "#C074FC",
      veryWhite: "#FFF",
      veryBlack: "#000",
    },
    fontFamily: {
      nunito: "Nunito",
      ptsans: "PT Sans",
    },
  },
  plugins: [],
};
