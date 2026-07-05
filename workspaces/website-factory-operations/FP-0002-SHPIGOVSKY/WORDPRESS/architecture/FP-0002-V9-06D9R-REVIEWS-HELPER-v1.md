# FP-0002 V9-06D9-R Reviews Helper

**File:** `inc/reviews-helpers.php`

## Public functions

| Function | Purpose |
|----------|---------|
| `shpigovsky_get_reviews_fallback_items()` | Static V9 10-card demo set |
| `shpigovsky_get_reviews_items( $args )` | Options rows or fallback; supports `featured_only`, `limit` |
| `shpigovsky_get_reviews_heading( $fallback )` | Options heading → Home heading → fallback |
| `shpigovsky_reviews_enabled()` | Reads `reviews_enabled` option; defaults true when unset |

Never depends on `home_reviews_teaser`. Safe when ACF inactive.

Evidence: `validation/v9-06d9r-reviews-shared-include-implementation/reviews-helper-result.json`
