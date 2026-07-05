# FP-0002 V9-06D9J D9-K Media Upload Seed Plan v1

**Date:** 2026-07-05  
**Status:** PLANNED — NOT EXECUTED  
**Evidence:** `validation/v9-06d9j-media-selection-upload-plan/d9k-media-upload-seed-plan.json`

## Phases

### K1 — Checkpoint + dry-run

- Full DB checkpoint `mars_wp_fp0002` (mysqldump).
- Export `home-page-4-media-pre-values.json` (hero slides + gallery repeater).
- Operator review exact upload manifest (5 files, checksums, alt text, target fields).

### K2 — Upload attachments

| Source | WP filename | Title / alt | ACF target |
|--------|-------------|-------------|------------|
| `v9/src/img/hero/hero-main.png` | `hero-main.png` | Шпиговский дом — центр профилактики и лечения зависимостей | `home_hero_slides[0].image` |
| `v9/src/.../shpigovsky-gallery-01.webp` | same | Лечение зависимости от алкоголя | `home_gallery_media[0].media` |
| gallery-02 | same | Лудомания лечение зависимости | `[1].media` |
| gallery-03 | same | Лечение подростковой зависимости | `[2].media` |
| gallery-04 | same | Зависимость от постоянных покупок | `[3].media` |

Parent post: page #4 (optional). Expected visual impact: **SHOULD_MATCH_CURRENT_FALLBACK**.

### K3 — Seed ACF

- Set `home_hero_slides[0].image` to hero attachment ID (preserve existing title/text).
- Populate `home_gallery_media` with 4 rows: title/text from `shpigovsky_home_gallery_fallback_items()`, media = attachment IDs.

### K4 — Visual regression

Compare Home hero + gallery to D9-J baseline screenshots.

### K5 — Admin UX QA

Verify page #4 edit screen shows populated image fields; no broken pickers.

## Out of scope for D9-K MVP

Specialists repeater schema, comfort gallery ACF, video uploads, reviews teaser, non-Home pages.
