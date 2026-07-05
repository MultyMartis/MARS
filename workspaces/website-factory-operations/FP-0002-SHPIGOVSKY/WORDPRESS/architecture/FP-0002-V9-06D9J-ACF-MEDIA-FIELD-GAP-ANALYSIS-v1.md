# FP-0002 V9-06D9J ACF Media Field Gap Analysis v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9j-media-selection-upload-plan/acf-media-field-gap-analysis.json`, `home-page-media-acf-snapshot.json`

## Media fields in `group_fp02_page_home`

### home_hero_slides → subfield `image` (`field_fp02_home_hero_image`)

| Attribute | Value |
|-----------|-------|
| Type | image (repeater subfield) |
| Target | page #4 |
| Current DB | 1 row — title/text populated; **image empty** |
| Frontend | Theme fallback `assets/img/hero/hero-main.png` |
| Upload needed | **YES** |
| Seed needed | **YES** |
| Risk | MEDIUM |

### home_gallery_media → subfield `media` (`field_fp02_home_gallery_item_media`)

| Attribute | Value |
|-----------|-------|
| Type | repeater (title, text, image) |
| Target | page #4 |
| Current DB | **empty repeater** |
| Frontend | `shpigovsky_home_gallery_fallback_items()` — 4 theme webp slides |
| Upload needed | **YES** (4 images) |
| Seed needed | **YES** (4 rows + titles from fallbacks) |
| Risk | MEDIUM |

### home_reviews_teaser (deferred)

| Attribute | Value |
|-----------|-------|
| Type | repeater (title, text only — no image subfield) |
| Current DB | empty |
| Upload needed | **NO** for D9-K |
| Risk | HIGH if seeded without operator review |

## Fields with media_later=false (D9-H map)

All other D9-H Home fields seeded D9-I are text/repeater without image subfields. Section images (comfort, specialists, founder, etc.) remain **template hardcoded** — not in D9-K MVP unless schema extended in a future wave.
