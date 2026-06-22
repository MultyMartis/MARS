# FP-0002 V6 HOME SECTION 02 OPERATOR STABLE 01 — Restore Instructions

**Release ID:** `FP-0002-V6-HOME-SECTION-02-OPERATOR-STABLE-01`  
**Archive:** `C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-HOME-SECTION-02-OPERATOR-STABLE-01-SOURCE.zip`

## Restore steps

1. Extract archive to a clean directory.
2. Verify `CHECKSUMS-SHA256.txt` against extracted files.
3. Run `npm ci`.
4. Run `npm run build`.
5. Confirm `dist/index.html` contains `home-recovery-intro`, `home-founder-quote`, and `founder-sergey-shpigovsky.png` in assets.
6. Confirm no Google Fonts references in dist output.
7. Confirm exactly one project SCSS file: `src/scss/style.scss`.

## Frozen scope

Responsive shell, Hero, operator-polished Section 01, Section 02 with exact Figma founder portrait (`FIG node 1:1212`), Footer, local Inter, current style foundation.

## Not in scope

Section 03+ main content beyond Section 02.
