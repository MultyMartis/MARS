# FP-0002 V9-06E20 Reviews Alias Removal

**Wave:** V9-06E20  
**Date:** 2026-07-08  
**Result:** PASS

## Changes

### `OptionsPage.php`

- Removed `fp02-block-reviews` block registration from reusable block subpages.
- Removed from Batch 1 fielded slugs list.
- Removed alias-specific admin notice and `post_id` alias mapping.

### `group_fp02_site_options_reviews.json`

- Location reduced to `fp02-reviews` only.
- Description updated for E20 canonical state.

### Runtime DB

- `acf_update_field_group` — dual location → single `fp02-reviews` (metadata only).

## Unchanged

- Top-level **Отзывы** menu (`theme/shpigovsky/inc/admin-options.php`).
- All `fp02-reviews_*` option values.
- Frontend reviews renderers and routes.

## After state

| Item | Value |
|------|-------|
| Site Settings branch | 5 items (no Отзывы) |
| Top-level Отзывы | `fp02-reviews` |
| Field group locations | `fp02-reviews` only |
| Review rows | 10 |
