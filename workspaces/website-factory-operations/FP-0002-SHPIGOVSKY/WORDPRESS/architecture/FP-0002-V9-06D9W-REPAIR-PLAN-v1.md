# FP-0002 V9-06D9-W — Repair Plan

**Phase:** V9-06D9-W  
**Date:** 2026-07-06

| Component | Planned repair | Safety |
|---|---|---|
| Duplicate cleanup | Trash stale duplicate ACF field-group posts; keep ID 286 on `fp02-reviews` | DB checkpoint; exact group key only |
| Admin storage context | Copy `options_reviews_*` meta to `fp02-reviews_reviews_*`; restore 10 rows from D9-S seed | No new content; seed payload only |
| Helper context | Read `fp02-reviews` first; skip empty normalized contexts; fallback `option` | Read-only theme change |
| Archive layout | Replace `/otzyvy/` slider with archive list + rehabilitation requirements | Home slider untouched |
| Validation | Admin populated rows; archive DOM; route smoke; source OPTIONS | No rewrite flush |

Evidence: `validation/v9-06d9w-reviews-admin-and-layout-repair/repair-plan.json`
