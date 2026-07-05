# FP-0002 V9-06D9-S Baseline Options Seed Audit

**Phase:** V9-06D9-S  
**Date:** 2026-07-06

## Summary

Pre-seed baseline confirmed empty reviews options, 10 static fallback items, and a runtime ACF field-key collision blocking D9-R subfield names.

## Baseline checks

| Check | Result | Notes |
|-------|--------|-------|
| `group_fp02_site_options_reviews` in DB | PASS | Options group registered |
| Canonical ACF JSON exists | PASS | `acf-json/group_fp02_site_options_reviews.json` |
| Site settings page | PASS | `fp02-site-settings` |
| `reviews_enabled` before | empty | null |
| `reviews_section_heading` before | empty | null |
| `reviews_items` count before | 0 | |
| Home source mode before | FALLBACK | 10 static slides |
| `/otzyvy/` source mode before | FALLBACK | |
| Static fallback count | 10 | From `reviews-helpers.php` |
| Existing options non-empty | NO | Seed allowed |
| Home #4 `home_reviews_teaser` | preserved | Orphan meta unchanged |

## Field-key collision (blocker for OPTIONS mode)

| Item | Value |
|------|-------|
| Colliding key | `field_fp02_reviews_items` |
| Groups | `group_fp02_page_reviews`, `group_fp02_site_options_reviews` |
| Runtime subfields | `author_label`, `text`, `metadata`, `source` |
| D9-R expected subfields | `review_author`, `review_text`, … |
| Helper reads | `review_author` / `review_text` only |

Evidence: `validation/v9-06d9s-controlled-reviews-options-seed/baseline-options-seed-audit.json`
