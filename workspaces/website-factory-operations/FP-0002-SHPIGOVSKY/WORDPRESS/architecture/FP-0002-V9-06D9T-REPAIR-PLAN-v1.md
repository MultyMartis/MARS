# FP-0002 V9-06D9-T Repair Plan

**Phase:** V9-06D9-T  
**Date:** 2026-07-06

## Components

| Component | Planned repair | Safety |
|---|---|---|
| ACF key repair | Assign `field_fp02_options_*` keys to all options reviews fields | Page reviews group unchanged |
| Helper normalization | Map canonical + legacy subfield names in `shpigovsky_normalize_review_row()` | Read-only; no content mutation |
| Options meta | Update ACF reference meta; row migration only if frontend still FALLBACK | Preserve 10 rows text exactly |
| Runtime delivery | Copy helper + ACF JSON; `acf_import_field_group` for options group | Bounded copy only |
| Validation | Source mode OPTIONS; 10 reviews on Home and `/otzyvy/` | No rewrite/menu/media |

Evidence: `validation/v9-06d9t-reviews-options-key-fix-helper-normalization/repair-plan.json`
