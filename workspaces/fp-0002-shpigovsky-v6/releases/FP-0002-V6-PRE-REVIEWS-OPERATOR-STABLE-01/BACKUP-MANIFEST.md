# FP-0002 V6 PRE-REVIEWS OPERATOR STABLE 01 — Backup Manifest

**Release ID:** `FP-0002-V6-PRE-REVIEWS-OPERATOR-STABLE-01`  
**Scope:** Operator-canonical baseline through all pre-reviews sections with corrected image crops  
**NOT CANONICAL:** `dist/` — regenerate via `npm run build`  
**NOT IN SCOPE:** Reviews, blocks after Reviews

## Contents

- `src/` (pages, partials, scss, js, fonts, images)
- `gulpfile.js`
- `package.json`
- `package-lock.json`
- `RESTORE-INSTRUCTIONS.md`
- `CHECKSUMS-SHA256.txt`

## Validation targets

- Gallery slide count: 4
- Gallery Swiper instances: 1
- Reviews absent in snapshot
- Pre-reviews images cropped without white margins
