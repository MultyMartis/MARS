# FP-0002 V9-06D9-R Implementation Plan

**Phase:** V9-06D9-R  
**Date:** 2026-07-06

## Components

| Component | Planned change | Safety |
|-----------|----------------|--------|
| `inc/reviews-helpers.php` | CREATE — options read + static fallback | Read-only; no writes |
| `template-parts/shared/reviews-slider.php` | CREATE — shared markup | Preserves V9 classes |
| `template-parts/home/reviews.php` | UPDATE — thin wrapper | Fallback when options empty |
| `template-parts/reviews/reviews-section.php` | UPDATE — wire shared include | Reviews page context |
| `functions.php` | UPDATE — require helper | Minimal include only |
| `group_fp02_site_options_reviews.json` | CREATE — options schema | Schema only; no values |
| `group_fp02_page_home.json` | UPDATE — remove `home_reviews_teaser` | Orphan DB meta preserved |

## Fallback behavior

1. `reviews_enabled` false → hide section (no value seeded in D9-R; default visible).
2. Options `reviews_items` has visible rows → render from options.
3. Otherwise → static V9 10-slide fallback.

## Runtime delivery

Theme files (5) + ACF JSON (2) copied to local runtime; `wp acf json sync` after DB checkpoint.

Evidence: `validation/v9-06d9r-reviews-shared-include-implementation/implementation-plan.json`
