# FP-0002 V9-06D9U — Repair Plan

| Component | Planned repair | Safety |
|---|---|---|
| Home blocker | Theme hide + POST strip for `field_fp02_home_reviews_teaser` | No plugin edits; orphan meta preserved |
| Canonical meta | Direct `options_*` migration to `review_*` subfields + ACF refs | Preserve 10 rows text exactly |
| Top-level menu | `acf_add_options_page` `fp02-reviews` + relocate ACF group | No frontend menu changes |
| Runtime | Copy theme + ACF JSON; ACF import + in-place location update | Bounded delivery |

## Result

PASS
