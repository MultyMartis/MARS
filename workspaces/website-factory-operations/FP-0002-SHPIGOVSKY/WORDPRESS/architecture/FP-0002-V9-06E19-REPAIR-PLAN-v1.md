# FP-0002 V9-06E19 Repair Plan v1

**Wave:** V9-06E19  
**Date:** 2026-07-08

## 1. Option page registration

| Page | parent_slug (before) | parent_slug (after) |
|------|----------------------|---------------------|
| Batch 1 blocks | `fp02-site-settings-blocks` | `fp02-site-settings` |
| Skeleton blocks | `fp02-site-settings-blocks` | unchanged (deferred) |
| Повторяемые блоки container | `fp02-site-settings` | unchanged; `redirect => false` + info notice |

## 2. Field group locations

No slug changes. Locations remain:

- `fp02-block-final-form`
- `fp02-block-specialists`
- `fp02-block-cta-bands`
- `fp02-block-reviews` (reviews alias)

## 3. Reviews compatibility

- Top-level `fp02-reviews` preserved
- Alias `post_id = fp02-reviews` unchanged
- Import `group_fp02_site_options_reviews.json` for dual location in DB

## 4. Runtime delivery

- `plugins/shpigovsky-core/src/Admin/OptionsPage.php` only

## 5. Validation

- ACF `acf_get_options_pages()` parent slug probe
- Frontend 8/8 routes HTTP 200
- Operator admin screenshots deferred to E20 QA
