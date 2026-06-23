# FP-0002 V6 HOME SECTION 03 OPERATOR STABLE 01 — Restore Instructions

**Release ID:** `FP-0002-V6-HOME-SECTION-03-OPERATOR-STABLE-01`  
**Archive:** `C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-HOME-SECTION-03-OPERATOR-STABLE-01-SOURCE.zip`

## Restore steps

1. Extract archive to a clean directory.
2. Verify `CHECKSUMS-SHA256.txt` against extracted files.
3. Run `npm ci`.
4. Run `npm run build`.
5. Confirm `dist/index.html` contains `home-treatment-prevention` with clickable service links.
6. Confirm `fa-external-link-alt` icons render in Section 03 service rows.
7. Confirm no Google Fonts references in dist output.
8. Confirm exactly one project SCSS file: `src/scss/style.scss`.

## Frozen scope

Responsive shell, Hero, Section 01, Section 02, Section 03 with working service links and arrow icons, Footer, local Inter, current style foundation.

## Not in scope

Gallery, pre-reviews blocks beyond Section 03, Reviews.
