# Conversion evidence — V9-06E56-FU02

- Archive formats: TTF only (6 faces) + OFL.txt
- Checked local tools: fontTools (missing), brotli (missing), woff2_compress (missing), ttf2woff2/woff2 npm modules (missing), fontforge (missing)
- Online converters: forbidden by charter
- Result: serve local TTF as `libertinus-serif-regular.ttf` with `format("truetype")`
- Browser validation: HTTP 200, Content-Type `font/ttf`, `document.fonts.check('400 70px \"Libertinus Serif\"') === true`, no decoding errors
