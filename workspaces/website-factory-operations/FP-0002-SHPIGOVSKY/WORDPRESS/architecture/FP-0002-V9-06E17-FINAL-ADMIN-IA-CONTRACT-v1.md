# FP-0002 V9-06E17 — Final Admin IA Contract

**Evidence:** `validation/v9-06e17-site-settings-ia-skeleton/final-e17-admin-ia-contract.json`

## Active admin surfaces

| Surface | Slug | Fields | Status |
|---------|------|--------|--------|
| Настройки сайта | `fp02-site-settings` | — | Parent redirect |
| Общие настройки | `fp02-site-settings-general` | contacts + modal/CTA | **ACTIVE** |
| Повторяемые блоки | `fp02-site-settings-blocks` | — | Redirect parent |
| Block subpages (×12) | `fp02-block-*` | none | **SKELETON** |
| Отзывы (legacy) | `fp02-reviews` | reviews options | **ACTIVE** |

## Deferred to E18

- Field groups on block subpages
- Reviews relocation `fp02-reviews` → `fp02-block-reviews`
- Modal/CTA field split per E16 restructure plan
- Frontend renderer reads per block
