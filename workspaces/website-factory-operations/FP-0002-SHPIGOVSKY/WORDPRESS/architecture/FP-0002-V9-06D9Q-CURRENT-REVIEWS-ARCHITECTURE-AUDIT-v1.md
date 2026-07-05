# FP-0002 V9-06D9Q Current Reviews Architecture Audit v1

**Date:** 2026-07-06  
**Mode:** Read-only planning audit

Evidence: `validation/v9-06d9q-reviews-include-planning/current-reviews-architecture-audit.json`

---

## Summary

Home reviews **render correctly** today using **fully static V9 markup** in `template-parts/home/reviews.php`. Only the section heading is ACF-driven (`home_reviews_heading`). The Home admin field `home_reviews_teaser` exists but is **not wired to the frontend** — it was a mistaken ownership model and is now optional (D9-O).

A dedicated reviews page template and ACF group (`group_fp02_page_reviews`) exist in canonical source but theme partials are **skeleton placeholders**.

---

## Current state table

| Area | Current state |
|------|---------------|
| Home template | `template-parts/home/reviews.php` — 10 hardcoded Swiper slides |
| Data source (cards) | Static HTML transplant from V9 |
| Heading | ACF `home_reviews_heading` → fallback «Отзывы» |
| `home_reviews_teaser` | Present in Home ACF; 1 DB row; **not consumed by theme** |
| Reviews CPT | None |
| Reviews page ACF | `reviews_items` repeater on `page-templates/reviews.php` — not wired |
| `/otzyvy/` frontend | 200; skeleton comments only |
| V9 static authority | `fp-0002-shpigovsky-v9/src/partials/sections/reviews.html` — 10 cards |
| Site options pattern | `fp02-site-settings` — contacts + modal CTA groups active |

---

## Review card fields (V9)

| Field | Markup |
|-------|--------|
| Author | `reviews__author-name` |
| Rating | 5× star icons (fixed) |
| Text | `reviews__text` |
| Read more | `reviews__read-more-text` (presentational footer) |
| Section H2 | «Отзывы» |
| All link | `/otzyvy/` — «Смотреть отзывы» |

---

## Gaps driving D9-R

1. No shared reviews include — Home and future `/otzyvy/` cannot share one pool.
2. `home_reviews_teaser` clutters Home admin without frontend benefit.
3. Static demo testimonials appear as live content without operator-approved flag.
4. `group_fp02_page_reviews` duplicates field shape that should be global.

---

## Verdict

Audit **COMPLETE** — ready for architecture recommendation and D9-R implementation charter.
