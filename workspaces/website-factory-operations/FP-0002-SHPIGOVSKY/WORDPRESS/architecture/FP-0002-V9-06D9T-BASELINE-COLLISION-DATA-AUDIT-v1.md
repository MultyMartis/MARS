# FP-0002 V9-06D9-T Baseline Collision Data Audit

**Phase:** V9-06D9-T  
**Date:** 2026-07-06

## Root cause

`group_fp02_site_options_reviews` shared ACF field keys with `group_fp02_page_reviews`:

| Shared key | Options intent | Page group actual |
|---|---|---|
| `field_fp02_reviews_items` | `reviews_items` repeater | `reviews_items` repeater |
| `field_fp02_review_text` | `review_text` | `text` |
| `field_fp02_review_source` | `review_source` | `source` |

After D9-S seed, runtime options group resolved page-reviews subfields (`author_label`, `text`, `metadata`, `source`). D9-R helper read only canonical names → `shpigovsky_get_reviews_option_items()` returned 0 → frontend **FALLBACK**.

## Baseline counts

| Check | Before repair |
|---|---|
| Seeded `reviews_items` rows | 10 |
| Helper option items | 0 |
| Frontend source mode | FALLBACK |
| Home slides | 10 |
| `/otzyvy/` slides | 10 |

Evidence: `validation/v9-06d9t-reviews-options-key-fix-helper-normalization/baseline-collision-data-audit.json`
