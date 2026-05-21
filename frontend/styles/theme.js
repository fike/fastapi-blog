import { createSystem, defineConfig, defaultConfig } from "@chakra-ui/react";

const config = defineConfig({
  theme: {
    tokens: {
      fonts: {
        body: { value: `Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"` },
        heading: { value: `Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"` },
      },
      fontWeights: {
        normal: { value: 300 },
        medium: { value: 600 },
        bold: { value: 700 },
      },
      fontSizes: {
        xs: { value: "12px" },
        sm: { value: "14px" },
        md: { value: "16px" },
        lg: { value: "18px" },
        xl: { value: "20px" },
        "2xl": { value: "24px" },
        "3xl": { value: "28px" },
        "4xl": { value: "36px" },
        "5xl": { value: "48px" },
        "6xl": { value: "64px" },
      },
    },
    breakpoints: {
      sm: "40em",
      md: "52em",
      lg: "62em",
    },
  },
});

export const system = createSystem(defaultConfig, config);
export default system;
