# FP-0002 V9-06D9U — Reviews Top-Level Menu

## Implementation

Theme `inc/admin-options.php` registers ACF options page:

| Property | Value |
|---|---|
| Menu label | Отзывы |
| Page title | Отзывы |
| Menu slug | `fp02-reviews` |
| Capability | `manage_options` |
| Icon | `dashicons-star-filled` |

`group_fp02_site_options_reviews` location updated to `fp02-reviews` (canonical JSON + `acf_update_field_group` on active DB group ID 250).

Site Settings no longer shows reviews group (no duplicate).

## Result

PASS
