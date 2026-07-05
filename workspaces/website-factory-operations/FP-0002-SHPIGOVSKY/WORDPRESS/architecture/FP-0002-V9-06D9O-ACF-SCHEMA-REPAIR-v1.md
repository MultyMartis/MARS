# FP-0002 V9-06D9O ACF Schema Repair v1

**Date:** 2026-07-05  
**Task:** V9-06D9-O

## Repair

| File/group | Field | Change | Result |
|------------|-------|--------|--------|
| `acf-json/group_fp02_page_home.json` (Git) | `home_reviews_teaser` | No edit — already `required: 0`, `min: 0` | PASS |
| DB `acf-field` post 128 | `home_reviews_teaser` | Idempotent reconcile — already `required=0`, `min=0` | PASS |
| Runtime `wp-content/acf-json/group_fp02_page_home.json` | group copy | Delivered from canonical; checksum match | PASS |

## Scope

- No field deletion
- No subfield changes
- No unrelated field `required` mutations

Evidence: `validation/v9-06d9o-acf-reviews-teaser-required-flag-repair/acf-schema-repair-result.json`
