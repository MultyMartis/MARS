# FP-0002 V6 Gallery Rejection Record

**Status:** append-only correction entry  
**Date:** 2026-06-23

## Operator rejection

| Field | Value |
|-------|-------|
| Rejected commit | `f0eadaf4ad4cc0c798d6c9fec6506061b20bc78c` |
| Gallery visual result | vertical image column |
| Horizontal Swiper track | not rendered |
| Desktop four-slide row | absent |
| Tablet/mobile peek | not visually present |
| Gallery boundary audit | contradictory (v1 gallery_end_y 3780 > next_section_start_y 3740) |
| Operator visual verdict | **REJECTED** |

## Correction entry (2026-06-23)

Repair task initiated on operator-canonical `src/` without git reset/revert.

| Field | Value |
|-------|-------|
| Root cause | `SWIPER_CSS_NOT_CONNECTED` — Sass emitted broken `@import '../../node_modules/swiper/...'` into built CSS; browser 404 |
| Repair status | `REPAIRED_PENDING_OPERATOR_REVIEW` |
| Prior success report | `OVERRULED_BY_OPERATOR` |

Historical review preserved: `reviews/main-content/FP-0002-V6-SECTION-03-LINKS-AND-GALLERY-REVIEW.md`
