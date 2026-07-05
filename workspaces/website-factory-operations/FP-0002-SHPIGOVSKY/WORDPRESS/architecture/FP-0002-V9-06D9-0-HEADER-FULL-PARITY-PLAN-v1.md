# FP-0002 V9-06D9-0 Header Full Parity Plan v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9-0-full-visual-port-charter/header-full-parity-plan.json`

## Executive summary

Static V9 header includes **Telegram, WhatsApp** (desktop) and **Telegram, WhatsApp, Max** (mobile/offcanvas) messenger icon buttons with `href="#"` placeholders. WordPress theme **already contains** `messenger-links.php` but runtime **omits** icons because `social_links` ACF option is empty (D8-A skip). Full **visual** parity can be achieved via source-only V9 placeholder fallback without inventing messenger URLs.

## Structure comparison

| Block | Static (`header.html`) | WP (`header.php` + partials) |
|-------|------------------------|------------------------------|
| Mobile bar | Logo, phone, messengers, menu toggle | Same structure — messengers omitted |
| Top line | Logo, address, schedule, 2 phones, messengers, callback | Same — messengers omitted |
| Bottom nav | Hardcoded V9 links + search | `wp_nav_menu` primary + search |
| Offcanvas | Nav + phones + 3 messengers + CTA | Nav + phones — messengers omitted |

## Messenger/icon audit (operator concern)

| Location | Static V9 | WP runtime | Gap |
|----------|-----------|------------|-----|
| Desktop `.site-header__messengers` | 2 icons (TG, WA) | absent | **ACF empty + early return** |
| Mobile `.mobile-header__messengers` | 3 icons (TG, WA, Max) | absent | same |
| Offcanvas `.offcanvas__messengers` | 3 icons | absent | same |
| Static URLs | `href="#"` placeholders | n/a | **No operator URLs needed for visual parity** |
| Production URLs | TBD | OPERATOR_DATA_REQUIRED | Seed `social_links` when operator supplies |

## Other header gaps

| Item | Static | WP | Repair |
|------|--------|-----|--------|
| Nav labels | Лечение и профилактика, Зависимости, О центре… | Главная, Услуги, Специалисты… | Menu seed or V9 fallback |
| Inter fonts | all 200 | 5/10 404 | `@font-face` path rewrite |
| Callback | Заказать звонок | Same (D8-A) | OK |
| Phones | 2 numbers | Seeded D8-A | OK |

## Suspected files

**WP:** `template-parts/navigation/messenger-links.php`, `inc/site-chrome.php`, `assets/css/v9-style.css`, `inc/assets.php`, `template-parts/navigation/primary-desktop.php`, `template-parts/navigation/offcanvas.php`

**Static:** `src/partials/layout/header.html`, `src/scss/layout/header.scss`

## Mutations required

| Type | Required |
|------|:--------:|
| Source-only (messengers with `#` fallback) | yes |
| DB/menu writes (nav parity) | yes |
| New site option fields | no |
| Runtime delivery | yes |
| Media upload | no (icons in theme) |
| Operator messenger URLs | optional (visual); required (production links) |

## Fallback policy

1. If `social_links` empty → render default V9 icon set with `href="#"` matching static authority.
2. If operator supplies URLs → seed `social_links`; links become functional.
3. **Do not invent** WhatsApp/Telegram/Max production URLs.

## Acceptance criteria

- Desktop and mobile messenger icon blocks visible
- Offcanvas messengers visible
- All Inter woff2 HTTP 200
- Nav typography uses real Inter (not synthesized)
- WP menu matches V9 link set (or documented acceptable fallback)

## Wave

**D9-B** — Header + fonts + global assets + messenger/icon parity

## Result

Header parity plan complete. Messenger repair required: **YES**.
