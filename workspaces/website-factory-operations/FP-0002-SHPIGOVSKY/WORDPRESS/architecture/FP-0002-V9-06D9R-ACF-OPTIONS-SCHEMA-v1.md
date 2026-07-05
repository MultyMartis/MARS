# FP-0002 V9-06D9-R ACF Options Schema

**Group:** `group_fp02_site_options_reviews`  
**Location:** `options_page == fp02-site-settings`

## Fields

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `reviews_enabled` | true_false | 0 | Default 1 in schema only |
| `reviews_section_heading` | text | 0 | Fallback «Отзывы» |
| `reviews_items` | repeater (0–50) | 0 | Site-wide reviews source |

## Repeater subfields

`review_author`, `review_text`, `review_context`, `review_source`, `review_date`, `review_rating`, `review_visible`, `review_featured` — all optional.

No option values seeded in D9-R.

Evidence: `validation/v9-06d9r-reviews-shared-include-implementation/acf-options-schema-result.json`
