# FP-0002 V9-06E20 Final Admin IA Contract

**Wave:** V9-06E20  
**Date:** 2026-07-08  
**Verdict:** PASS

## Настройки сайта (final)

| Menu item | Slug |
|-----------|------|
| Общие настройки | `fp02-site-settings-general` |
| Повторяемые блоки | `fp02-site-settings-blocks` |
| Финальная форма | `fp02-block-final-form` |
| Специалисты | `fp02-block-specialists` |
| CTA-блоки | `fp02-block-cta-bands` |

**Отзывы** is **not** under **Настройки сайта**.

## Top-level reviews (preserved)

| Item | Value |
|------|-------|
| Menu | Отзывы |
| Slug | `fp02-reviews` |
| post_id | `fp02-reviews` |
| Field group | `group_fp02_site_options_reviews` → location `fp02-reviews` |

## Frontend compatibility

Routes `/`, `/otzyvy/`, service pages — reviews and Batch 1 blocks unchanged. HTTP 200; marker **Андрей** present where expected.

## Operator QA checklist

- [ ] **Настройки сайта** has 5 items; no **Отзывы** under it
- [ ] Top-level **Отзывы** opens with repeater fields
- [ ] **Финальная форма**, **Специалисты**, **CTA-блоки** still editable
- [ ] Home and `/otzyvy/` show reviews
- [ ] No duplicate reviews admin entry
