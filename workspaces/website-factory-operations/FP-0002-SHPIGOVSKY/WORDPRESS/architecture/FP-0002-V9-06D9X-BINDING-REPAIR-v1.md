# FP-0002 V9-06D9-X — Binding Repair

**Phase:** V9-06D9-X  
**Date:** 2026-07-06

## Implementation

1. **DB migration** — 166 meta keys copied from `options_reviews_*` to `fp02-reviews_reviews_*`; first author now **Андрей, Москва** in both contexts.
2. **`reviews-helpers.php`** — Added `shpigovsky_get_reviews_resolved_options_context()`, read-order helpers, source mode tied to resolved context.
3. **`admin-options.php`** — Explicit `post_id => fp02-reviews`, `autoload => false`, `acf/pre_save_post` filter to prevent future saves to legacy `option` namespace.

## Post-repair

| Surface | First author | Source mode |
|---|---|---|
| Home `/` | Андрей, Москва | OPTIONS |
| `/otzyvy/` | Андрей, Москва | OPTIONS |
| DB fp02-reviews | Андрей, Москва | — |

Evidence: `validation/v9-06d9x-reviews-admin-to-frontend-binding-repair/binding-repair-result.json`
