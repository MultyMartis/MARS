# FP-0002 V9-06D9A Header Nav Computed Style Diff v1

**Date:** 2026-07-05  
**Task:** V9-06D9-A Visual Parity Audit  
**Evidence:** `validation/v9-06d9a-visual-parity-audit/header-nav-computed-style-diff.json`  
**Viewport:** 1440×900, deviceScaleFactor 1

## Executive finding

Computed CSS tokens on **matching nav items** (Отзывы, Статьи, Контакты) are **identical** between static and runtime. However:

1. **5/10 Inter font files return HTTP 404** on runtime (`/assets/fonts/inter/*.woff2` at site root).
2. **Navigation structure differs** — static uses V9 mega-menu; runtime uses flat WordPress primary menu.
3. Operator-perceived “thinner/paler” text is likely **partial font load failure** (synthesized glyphs) plus **missing hero contrast context**, not a CSS token mismatch on nav links.

## Computed style comparison (representative items)

| Item | Property | Static | Runtime | Match | Visual impact |
|------|----------|--------|---------|------:|---------------|
| header root | font-family | Inter, system-ui… | Inter, system-ui… | yes | Low if Inter loads |
| header root | font-weight | 300 | 300 | yes | — |
| header root | font-size | 18px | 18px | yes | — |
| header root | color | rgb(71, 83, 113) | rgb(71, 83, 113) | yes | — |
| nav Отзывы | font-size | 16px | 16px | yes | — |
| nav Отзывы | font-weight | 400 | 400 | yes | — |
| nav Отзывы | line-height | 20px | 20px | yes | — |
| nav Отзывы | letter-spacing | normal | normal | yes | — |
| nav Отзывы | color | rgb(71, 83, 113) | rgb(71, 83, 113) | yes | — |
| nav Отзывы | -webkit-font-smoothing | antialiased | antialiased | yes | — |
| nav Отзывы | opacity | 1 | 1 | yes | — |
| body | font-family | Inter… | Inter… | yes | **Misleading** — see font network |
| Inter woff2 (300) | network | 200 | **404** | no | **HIGH** — Cyrillic may synthesize |
| Inter woff2 (400 latin) | network | 200 | **404** | no | **HIGH** |
| Inter woff2 (500) | network | 200 | **404** | no | **HIGH** |
| Inter woff2 (400 cyrillic) | network | 200 | **404** at `/assets/` | no | **CRITICAL** |
| Inter woff2 (400 cyrillic) | theme path | n/a | **200** at theme URI | — | CSS not pointing here |

## Font file root cause

`v9-style.css` `@font-face` declarations use **absolute static-dist paths**:

```css
src: url("/assets/fonts/inter/inter-400.woff2") format("woff2");
```

Valid on V9 static (`dist/` served at domain root). **Invalid on WordPress** unless a root `/assets/` alias exists. Theme files exist at `wp-content/themes/shpigovsky/assets/fonts/inter/` but CSS does not reference them.

## Nav structure note

| Static V9 primary nav | Runtime WP primary nav |
|-----------------------|------------------------|
| Лечение и профилактика (mega) | Главная, Услуги, Специалисты… |
| Dropdown service columns | Flat links |

Items Главная, Услуги, Специалисты, О центре exist **only on runtime** — not comparable 1:1 with static.

## Recommended repair

**D9-B:** Rewrite `@font-face` URLs to theme-relative paths in source CSS build pipeline; deliver to runtime. Review WP menu vs V9 nav partial separately.

## Result

Header/nav typography parity: **PARTIAL** (computed tokens match; font delivery and nav structure fail)
