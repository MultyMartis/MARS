# FP-0002 V9-06D9A Home Hero Parity Audit v1

**Date:** 2026-07-05  
**Task:** V9-06D9-A Visual Parity Audit  
**Evidence:** `validation/v9-06d9a-visual-parity-audit/home-hero-parity-audit.json`

## Comparison

| Property | Static V9 | WordPress runtime |
|----------|-----------|-------------------|
| Selector | `section.hero.hero--home` | `section.hero.hero--home` |
| Media layer | `hero__media` present | **absent** |
| Background image | `hero-main.png` (2230×1246) | **none** |
| Image URL | `/assets/img/hero/hero-main.png` | n/a |
| Image HTTP status | 200 (static server) | n/a (not requested) |
| Overlay/panel | `.hero__panel` over photo | panel only, no photo behind |
| Hero height | 620px | 620px (same CSS box, empty) |
| Title | Шпиговский дом | Шпиговский дом |
| Tagline | Центр профилактики и лечения зависимостей | same (nbsp normalized) |
| CTA | Записаться на консультацию | Заказать звонок (D8-A options label) |

## Asset availability

- Static dist: `dist/assets/img/hero/hero-main.png` — **exists**
- Runtime theme: `assets/img/hero/hero-main.png` — **404 / not present**
- WP template expects ACF field `home_hero_slides[0].image` via `shpigovsky_acf_image_url()`
- D8-B: hero slide normalize **failed**; image **skipped**

## Likely root cause

**ACF_IMAGE_NOT_SEEDED** + **ASSET_NOT_DELIVERED** — template markup is correct but conditional `hero__media` block never renders without ACF image URL.

## Severity

**CRITICAL** — primary operator-reported visual gap.

## Recommended repair

**D9-C:** Authorize media upload of `hero-main.png`, seed `home_hero_slides`, optional theme static fallback when ACF empty.

## Result

Home hero parity: **FAIL**
