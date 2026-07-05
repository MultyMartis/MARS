# FP-0002 V9-06D9-S Seed Plan

**Phase:** V9-06D9-S  
**Date:** 2026-07-06

## Planned values

| Field | Planned value | Source |
|-------|---------------|--------|
| `reviews_enabled` | `1` | D9-S charter |
| `reviews_section_heading` | `Отзывы` | Visible default heading |
| `reviews_items` | 10 rows | Static V9 fallback in `reviews-helpers.php` |

## Row mapping

Runtime write used legacy subfield names accepted by ACF (`author_label`, `text`, `metadata`, `source`) because `field_fp02_reviews_items` collides with `group_fp02_page_reviews`.

| Fallback key | Runtime write field | D9-R canonical field |
|--------------|---------------------|----------------------|
| author | `author_label` | `review_author` |
| text | `text` | `review_text` |
| context | `metadata` | `review_context` |
| source | `source` | `review_source` |
| rating | (default 5 on frontend) | `review_rating` |
| visible/featured | (implicit) | `review_visible`, `review_featured` |

All 10 rows: `review_visible=1`, `review_featured=1` equivalent; rating 5 via frontend normalizer when options path active.

Evidence: `validation/v9-06d9s-controlled-reviews-options-seed/seed-plan.json`
