# FP-0002 V6 FULL HOME OPERATOR STABLE 01 — Restore Instructions

**Release ID:** `FP-0002-V6-FULL-HOME-OPERATOR-STABLE-01`  
**Archive:** `C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-FULL-HOME-OPERATOR-STABLE-01-SOURCE.zip`

## Restore steps

1. Extract archive to a clean directory.
2. Verify `CHECKSUMS-SHA256.txt` against extracted files.
3. Run `npm ci`.
4. Run `npm run build`.
5. Confirm `dist/index.html` contains full home sections through `home-final-form`.
6. Confirm Gallery slides = 4, Reviews slides = 10 in source partials.
7. Confirm Gallery Swiper instances = 1, Reviews Swiper instances = 1.
8. Confirm Google Fonts = 0, local Inter present, `data-safe-unknown` = 0.
9. Confirm exactly one project SCSS file: `src/scss/style.scss`.

## Frozen scope

Header, Hero, Section 01–03, Gallery, Why-us, Staff photo, Feature grid, Clinic landscape, Reviews, Rehabilitation requirements, Rehabilitation program, Genotyping, Comfort, Videos, Specialists, Articles, FAQ, Final form, Footer, operator-canonical HTML/SCSS.
