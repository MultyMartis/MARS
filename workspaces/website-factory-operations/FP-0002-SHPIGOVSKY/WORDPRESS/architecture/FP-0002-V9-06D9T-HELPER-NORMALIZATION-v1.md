# FP-0002 V9-06D9-T Helper Normalization

**Phase:** V9-06D9-T  
**Date:** 2026-07-06

## Normalization mapping

| Output | Priority chain |
|---|---|
| author | `review_author` → `author_label` → `author` |
| text | `review_text` → `text` |
| context | `review_context` → `metadata` |
| source | `review_source` → `source` |
| date | `review_date` → `date` |
| rating | `review_rating` → `rating` (default 5) |
| visible | `review_visible` → `visible` (default true) |
| featured | `review_featured` → `featured` (default true) |

## Source mode detector

`shpigovsky_get_reviews_source_mode()` returns:

- **DISABLED** — `reviews_enabled` explicitly false
- **OPTIONS** — at least one visible normalized options row
- **FALLBACK** — otherwise

Post-repair runtime probe: OPTIONS, 10 option rows, `is_demo: false`.

Evidence: `validation/v9-06d9t-reviews-options-key-fix-helper-normalization/helper-normalization-result.json`
