# FP-0002 V9-06E19 Final Admin Visibility Contract v1

**Wave:** V9-06E19  
**Date:** 2026-07-08

## Menu path

`Настройки сайта` → flat siblings: **Общие настройки**, **Повторяемые блоки**, **Финальная форма**, **Специалисты**, **Отзывы**, **CTA-блоки**

## Option page slugs

| Page | Slug | post_id |
|------|------|---------|
| Общие настройки | `fp02-site-settings-general` | `option` |
| Повторяемые блоки | `fp02-site-settings-blocks` | — |
| Финальная форма | `fp02-block-final-form` | `fp02-block-final-form` |
| Специалисты | `fp02-block-specialists` | `fp02-block-specialists` |
| Отзывы (alias) | `fp02-block-reviews` | `fp02-reviews` |
| CTA-блоки | `fp02-block-cta-bands` | `fp02-block-cta-bands` |
| Отзывы (legacy) | `fp02-reviews` | `fp02-reviews` |

## Field groups

| Page | Group |
|------|-------|
| Финальная форма | `group_fp02_block_final_form` |
| Специалисты | `group_fp02_block_specialists` |
| CTA-блоки | `group_fp02_block_cta_bands` |
| Отзывы alias + legacy | `group_fp02_site_options_reviews` |

## Container behavior

`fp02-site-settings-blocks` shows info notice with Batch 1 links; no field groups attached.

## Deferred (E20+)

- Skeleton block subpages under `fp02-site-settings-blocks` (Batch 2+)
- Operator authenticated admin screenshots
- True visual nesting under **Повторяемые блоки** (WordPress limitation)

## Operator QA checklist

- [ ] Open **Настройки сайта** — see Batch 1 siblings in sidebar
- [ ] **Финальная форма** — fields visible, save works
- [ ] **Специалисты** — repeater visible
- [ ] **Отзывы** (under site settings) — same data as top-level **Отзывы**
- [ ] **CTA-блоки** — fields visible
- [ ] Top-level **Отзывы** still works
- [ ] Frontend routes unchanged
