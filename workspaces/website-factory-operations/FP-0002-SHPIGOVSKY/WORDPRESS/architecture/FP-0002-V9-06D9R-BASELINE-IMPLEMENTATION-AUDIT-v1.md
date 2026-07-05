# FP-0002 V9-06D9-R Baseline Implementation Audit

**Phase:** V9-06D9-R  
**Date:** 2026-07-06

## Summary

Pre-implementation audit confirmed static Home reviews (10 hardcoded Swiper slides), optional unwired `home_reviews_teaser` on Home ACF group, dormant `/otzyvy/` skeleton partials, and existing ACF Options architecture on `fp02-site-settings`.

## Before state

| Area | State |
|------|-------|
| Home reviews template | `template-parts/home/reviews.php` — 10 static slides inline |
| Shared partials | None under `template-parts/shared/` |
| Reviews helper | None |
| ACF Options reviews | No dedicated group |
| `home_reviews_teaser` | Present in Home group JSON; not wired to frontend |
| `home_reviews_heading` | Present; used by Home reviews heading |
| Reviews page | HTTP 200 skeleton; placeholder comments only |
| DB ACF groups | 13 groups before sync |

Evidence: `validation/v9-06d9r-reviews-shared-include-implementation/baseline-implementation-audit.json`
