# FP-0002 V9-06D9-T ACF Key Repair

**Phase:** V9-06D9-T  
**Date:** 2026-07-06

## Key changes (options group only)

| Field name | Old key | New key |
|---|---|---|
| `reviews_enabled` | `field_fp02_reviews_enabled` | `field_fp02_options_reviews_enabled` |
| `reviews_section_heading` | `field_fp02_reviews_section_heading` | `field_fp02_options_reviews_section_heading` |
| `reviews_items` | `field_fp02_reviews_items` | `field_fp02_options_reviews_items` |
| `review_author` | `field_fp02_review_author` | `field_fp02_options_review_author` |
| `review_text` | `field_fp02_review_text` | `field_fp02_options_review_text` |
| `review_context` | `field_fp02_review_context` | `field_fp02_options_review_context` |
| `review_source` | `field_fp02_review_source` | `field_fp02_options_review_source` |
| `review_date` | `field_fp02_review_date` | `field_fp02_options_review_date` |
| `review_rating` | `field_fp02_review_rating` | `field_fp02_options_review_rating` |
| `review_visible` | `field_fp02_review_visible` | `field_fp02_options_review_visible` |
| `review_featured` | `field_fp02_review_featured` | `field_fp02_options_review_featured` |

Page group `group_fp02_page_reviews` unchanged. Post-sync: options repeater subfields are canonical; page repeater retains legacy names.

Evidence: `validation/v9-06d9t-reviews-options-key-fix-helper-normalization/acf-key-repair-result.json`, `acf-sync-result.json`
