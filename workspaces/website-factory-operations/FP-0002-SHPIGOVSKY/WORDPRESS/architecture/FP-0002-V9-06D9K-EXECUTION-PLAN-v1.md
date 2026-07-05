# FP-0002 V9-06D9-K — Execution Plan

**Phase:** V9-06D9-K  
**Date:** 2026-07-05  
**Scope:** 5 approved Home media files → WP Media Library → ACF seed on page #4

## Approved uploads

| File | Source | Target field | Metadata | Expected visual impact |
|---|---|---|---|---|
| hero-main.png | `fp-0002-shpigovsky-v9/src/img/hero/hero-main.png` | `home_hero_slides[0].image` | Title/alt: Шпиговский дом — центр… | SHOULD_MATCH_CURRENT_FALLBACK |
| shpigovsky-gallery-01.webp | `…/gallery/shpigovsky-gallery-01.webp` | `home_gallery_media[0].media` | Лечение зависимости от алкоголя | SHOULD_MATCH_CURRENT_FALLBACK |
| shpigovsky-gallery-02.webp | `…/gallery/shpigovsky-gallery-02.webp` | `home_gallery_media[1].media` | Лудомания лечение зависимости | SHOULD_MATCH_CURRENT_FALLBACK |
| shpigovsky-gallery-03.webp | `…/gallery/shpigovsky-gallery-03.webp` | `home_gallery_media[2].media` | Лечение подростковой зависимости | SHOULD_MATCH_CURRENT_FALLBACK |
| shpigovsky-gallery-04.webp | `…/gallery/shpigovsky-gallery-04.webp` | `home_gallery_media[3].media` | Зависимость от постоянных покупок | SHOULD_MATCH_CURRENT_FALLBACK |

Authority: D9-J `d9k-media-upload-seed-plan.json`

## ACF seed rules

1. **Hero:** Preserve D9-I slide title/text; set row 0 image attachment ID only.
2. **Gallery:** Seed exactly 4 repeater rows with `media` attachment IDs; titles from D9-J/static V9 fallbacks.

Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/execution-plan.json`
