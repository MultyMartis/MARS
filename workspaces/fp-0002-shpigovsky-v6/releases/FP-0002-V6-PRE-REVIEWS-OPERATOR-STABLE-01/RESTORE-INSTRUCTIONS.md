# FP-0002 V6 PRE-REVIEWS OPERATOR STABLE 01 — Restore Instructions

**Release ID:** `FP-0002-V6-PRE-REVIEWS-OPERATOR-STABLE-01`  
**Archive:** `C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-PRE-REVIEWS-OPERATOR-STABLE-01-SOURCE.zip`

## Restore steps

1. Extract archive to a clean directory.
2. Verify `CHECKSUMS-SHA256.txt` against extracted files.
3. Run `npm ci`.
4. Run `npm run build`.
5. Confirm `dist/index.html` contains Gallery, Why-us, Staff photo, Feature grid, Clinic landscape.
6. Confirm `dist/index.html` does **not** contain `home-reviews`.
7. Confirm Gallery Swiper CSS link and one gallery instance initialize.
8. Confirm corrected pre-reviews images render without white margins.
9. Confirm exactly one project SCSS file: `src/scss/style.scss`.

## Frozen scope

Responsive shell, Hero, Section 01–03, Gallery, Why-us, Staff photo, Feature grid, Clinic landscape, Footer, local Inter, operator-canonical HTML/SCSS through pre-reviews.

## Not in scope

Reviews section, blocks after Reviews.
