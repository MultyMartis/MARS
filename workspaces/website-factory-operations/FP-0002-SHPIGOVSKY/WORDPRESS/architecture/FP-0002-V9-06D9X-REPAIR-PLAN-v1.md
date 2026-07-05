# FP-0002 V9-06D9-X — Repair Plan

**Phase:** V9-06D9-X  
**Date:** 2026-07-06

| Component | Planned repair | Safety |
|---|---|---|
| DB options context migration | Copy `options_reviews_*` → `fp02-reviews_reviews_*` preserving Андрей | Checkpoint before write |
| `inc/reviews-helpers.php` | Keep fp02-reviews-first read order; track resolved context | Read-only helper |
| `inc/admin-options.php` | Explicit `post_id`; `acf/pre_save_post` force fp02-reviews | Admin save path only |
| Templates | No change — already use helper | Layout preserved |

Canonical context: **`fp02-reviews`**. Legacy `option` remains empty-canonical fallback only.

Evidence: `validation/v9-06d9x-reviews-admin-to-frontend-binding-repair/repair-plan.json`
