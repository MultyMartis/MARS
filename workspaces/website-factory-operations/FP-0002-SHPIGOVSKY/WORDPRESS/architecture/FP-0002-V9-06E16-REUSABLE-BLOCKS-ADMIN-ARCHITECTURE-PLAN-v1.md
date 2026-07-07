# FP-0002 V9-06E16 — Reusable Blocks Admin Architecture Plan

**Evidence:** `validation/v9-06e16-operator-qa-closure-reusable-blocks-clone-cleanup-audit/reusable-blocks-admin-architecture-plan.json`

## Admin menu IA

Parent **Настройки сайта** (`fp02-site-settings`) gains:

1. **Общие настройки** (`fp02-site-settings-general`) — contacts, global phone/email defaults.
2. **Повторяемые блоки** (`fp02-site-settings-blocks`, redirect parent) with subpages per block group.

## Principles

- One ACF options subpage per repeating block; no field sprawl on a single screen.
- Page/service hero and per-service CTA remain on page/CPT field groups.
- Relocate `fp02-reviews` under **Повторяемые блоки → Отзывы**; remove duplicate top-level menu after migration.
- Russian labels; retire English ACF group titles.
- Renderer reads new option context with legacy/V9 fallbacks when empty.

## Migration order (renderer)

1. Final form + reviews (existing partial admin)
2. Specialists repeater (new; seed from `v9-static-content.php`)
3. Header/footer split from general settings
4. CTA bands, comfort, founder quote, hero fallback map

## Backward compatibility

`shpigovsky_get_site_option` and reviews helpers must alias legacy keys during transition. Screenshot parity gate per block.
