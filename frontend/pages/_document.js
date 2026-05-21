import NextDocument, { Html, Head, Main, NextScript } from "next/document";
import { GoogleFonts } from "next-google-fonts";

export default class MyDocument extends NextDocument {
  render() {
    return (
      <Html lang="en" suppressHydrationWarning>
        <GoogleFonts href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" />
        <Head />
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}
