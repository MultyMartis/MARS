# FP-0002 V9-06E20 Baseline Reviews Alias Audit

**Wave:** V9-06E20  
**Date:** 2026-07-08

## A. Admin menu (before)

**Настройки сайта** branch (E19):

- Общие настройки (`fp02-site-settings-general`)
- Повторяемые блоки (`fp02-site-settings-blocks`)
- Финальная форма (`fp02-block-final-form`)
- Специалисты (`fp02-block-specialists`)
- **Отзывы alias** (`fp02-block-reviews`, `post_id=fp02-reviews`)
- CTA-блоки (`fp02-block-cta-bands`)

**Top-level:** Отзывы (`fp02-reviews`) — active, canonical storage.

## B. Field group

| Item | State |
|------|-------|
| Group | `group_fp02_site_options_reviews` |
| Locations | `fp02-reviews` + `fp02-block-reviews` (dual) |
| Source | PHP/JSON/DB all had dual location |

## C. Reviews data

| Item | Value |
|------|-------|
| Storage | `fp02-reviews` |
| Rows | 10 |
| Sample | Андрей, Москва |
| Options keys | 166 under `fp02-reviews_*` |

## D. Frontend

Reviews on `/`, `/otzyvy/`, service pages — bound to `fp02-reviews` context; no change required in E20.

## Risk assessment

Safe to remove alias registration and `fp02-block-reviews` field group location only. No data migration required.
