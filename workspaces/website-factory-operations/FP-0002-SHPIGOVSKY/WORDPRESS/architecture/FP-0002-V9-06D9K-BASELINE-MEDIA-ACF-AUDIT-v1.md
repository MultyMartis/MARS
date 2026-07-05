# FP-0002 V9-06D9-K — Baseline Media / ACF Audit

**Phase:** V9-06D9-K  
**Date:** 2026-07-05  
**Page:** Home #4

## Pre-write state

| Area | Before state | Notes |
|---|---|---|
| Media Library attachments | 0 | Empty per D9-J inventory |
| `home_hero_slides` | 1 row; title/text seeded (D9-I); image empty | Theme fallback hero active |
| `home_gallery_media` | 0 rows | Theme fallback gallery (4 images) active |
| Frontend hero URL | `/themes/shpigovsky/assets/img/hero/hero-main.png` | Fallback |
| Frontend gallery URLs | 4× theme gallery webp | Fallback |
| Route smoke | ALL_200 (7 routes) | Verified at gate |

Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/baseline-media-acf-audit.json`

## Post-write summary

After D9-K: 5 attachments created (IDs 89–93); hero and gallery ACF fields populated; frontend serves `/uploads/2026/07/` URLs with checksum parity to static V9 sources.
