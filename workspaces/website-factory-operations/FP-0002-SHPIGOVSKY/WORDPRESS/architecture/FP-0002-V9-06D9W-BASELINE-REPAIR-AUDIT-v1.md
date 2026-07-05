# FP-0002 V9-06D9-W — Baseline Repair Audit

**Phase:** V9-06D9-W  
**Date:** 2026-07-06  
**Mode:** Pre-repair baseline

## Findings (reproduced)

| Check | Result | Notes |
|---|---|---|
| Duplicate `group_fp02_site_options_reviews` DB posts | CONFIRMED | 4 publish posts (IDs 250, 262, 274, 286) |
| Top-level `fp02-reviews` admin empty | CONFIRMED | Data under `option`; `fp02-reviews` context empty |
| Home slider regression risk | NOT CONFIRMED | Home slider present; not repair target |
| `/otzyvy/` uses Home slider | CONFIRMED | `reviews__slider swiper` on archive page |
| Static V9 archive classes available in theme CSS | CONFIRMED | `reviews-archive`, `review-archive-card` in `v9-style.css` |
| Seeded review content recoverable | CONFIRMED | D9-S seed payload + D9-U checkpoint legacy meta |

Evidence: `validation/v9-06d9w-reviews-admin-and-layout-repair/baseline-repair-audit.json`
