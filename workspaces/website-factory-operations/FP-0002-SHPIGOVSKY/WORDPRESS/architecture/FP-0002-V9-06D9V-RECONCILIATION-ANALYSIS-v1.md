# FP-0002 V9-06D9V — Reconciliation Analysis

**Phase:** V9-06D9-V (read-only)  
**Date:** 2026-07-06

## Summary

D9-U commit `c3cbee9f` is technically present but **operator verification contradicts** D9-U PASS claims for admin UX and `/otzyvy/` layout. Frontend Home slider output is consistent with static V9 Home.

## Issue matrix

| Issue | Class | Root cause | Minimal repair |
|---|---|---|---|
| Duplicate reviews in Site Settings | ADMIN_DUPLICATE | Stale duplicate ACF field-group DB post | Remove duplicate; single `fp02-reviews` location |
| Empty Отзывы admin fields | ADMIN_EMPTY_FIELDS | Storage context `'option'` vs `'fp02-reviews'` | Migrate meta + update helpers |
| Home teaser blocker | HOME_BLOCKER | Plugin field + theme suppression | Verify suppression; not active blocker if filters load |
| Home "old slider" | FRONTEND_HOME_LAYOUT | N/A — matches static | No Home layout repair |
| `/otzyvy/` spacing/layout | FRONTEND_REVIEWS_PAGE_LAYOUT + CSS_SPACING + TEMPLATE_STRUCTURE | Slider wired instead of archive list | Implement archive-list; remove slider from reviews page |
| Admin vs frontend data | DATA_SOURCE | Same as empty admin fields | Unify ACF post_id in D9-W |

## D9-U vs operator

| D9-U claim | Operator | Audit |
|---|---|---|
| Reviews admin populated | Empty | **Operator confirmed** — API used wrong context |
| Site Settings duplicate removed | Still present | **Operator confirmed** — DB duplicate evidence |
| Frontend regression PASS | `/otzyvy/` broken spacing | **Partial** — Home OK; archive page wrong template |

## Evidence

`validation/v9-06d9v-reviews-admin-static-layout-reconciliation-audit/reconciliation-analysis.json`
