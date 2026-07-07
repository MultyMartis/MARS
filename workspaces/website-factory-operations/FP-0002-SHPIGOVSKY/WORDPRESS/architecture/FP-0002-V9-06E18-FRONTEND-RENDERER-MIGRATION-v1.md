# FP-0002 V9-06E18 — Frontend Renderer Migration

Evidence: `validation/v9-06e18-reusable-blocks-batch-1-fields/frontend-renderer-migration-result.json`

## New helper module

`theme/shpigovsky/inc/reusable-blocks-helpers.php` — block option reads and fallback chains.

## Migrated partials

| File | Change |
|------|--------|
| `components/final-form.php` | Block options → home → static |
| `home/specialists.php` | `shpigovsky_get_specialists_cards()` loop |
| `service/alcohol-direct-v9/specialists.php` | Shared specialists data source |
| `inc/service-helpers.php` | CTA band defaults from block options |

## Unchanged

- Reviews renderers (`reviews-helpers.php`, `reviews-slider.php`, `archive-list.php`)
- Legal, menu, privacy, service page content
