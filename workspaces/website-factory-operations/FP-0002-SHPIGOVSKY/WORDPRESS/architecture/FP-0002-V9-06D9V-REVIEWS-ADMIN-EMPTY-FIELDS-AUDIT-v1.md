# FP-0002 V9-06D9V — Reviews Admin Empty Fields Audit

**Phase:** V9-06D9-V (read-only)  
**Date:** 2026-07-06

## Finding

Operator report **CONFIRMED**: top-level **Отзывы** admin (`fp02-reviews`) shows empty review fields.

## Storage context mismatch

| Layer | Post ID / prefix | Reads data? |
|---|---|---|
| Theme helpers (`reviews-helpers.php`) | `'option'` → `options_reviews_*` | Yes — 10 rows via CLI probe in D9-U |
| D9-S/T/U seed & migration | `'option'` | Writes to generic options |
| ACF admin screen `fp02-reviews` | `'fp02-reviews'` → `options_fp02-reviews_*` | No — empty UI |

ACF custom options pages use the menu slug as storage post ID. Data migrated to generic `'option'` does not automatically appear on `fp02-reviews`.

## D9-U evidence contradiction

- `canonical-options-meta-migration-result.json`: **PARTIAL** — empty admin author after migration, source mode FALLBACK
- `post-repair-admin-validation.json`: **PASS** — 10 rows via `get_field(..., 'option')`

Automated PASS validated API reads from `'option'`, not operator-visible `fp02-reviews` screen population.

## Frontend vs admin

- **Frontend** can show 10 slider slides (OPTIONS or FALLBACK) while **admin** appears empty.
- Operator cannot edit seeded content from intended **Отзывы** menu.

## Minimal D9-W repair

1. DB checkpoint.
2. Migrate/copy canonical `review_*` meta to `fp02-reviews` storage namespace (or re-save via `update_field(..., 'fp02-reviews')`).
3. Update `shpigovsky_get_reviews_option_items()` and related calls to use `'fp02-reviews'` consistently.
4. Validate: admin shows 10 editable rows; frontend source mode **OPTIONS**; Home #4 save unaffected.

## Evidence

`validation/v9-06d9v-reviews-admin-static-layout-reconciliation-audit/reviews-admin-empty-fields-audit.json`
