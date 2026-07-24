# ISEO-SU GLOBAL COMPONENT DEPENDENCY MAP v1

**Programme:** ISEO-SU-SITE-OPS  
**Date:** 2026-07-24  

## Header / topbar

| Surface | Implementation | Menu source | Contact/CTA |
|---------|----------------|-------------|-------------|
| Marketing HTML + `page-home.php` | Hardcoded header markup in each file/template | Hardcoded links | Hardcoded phones/messengers in markup |
| WP templates using `get_header()` | `header.php` + `template-parts/content-topbar.php` (+ mobile menu part) | Mixed: WP Primary location exists; topbar still hardcodes many `/services/...` and `/tariff-calc` links | Hardcoded in parts |

**Impact:** Global header tasks usually need **both** channels.

## Footer

| Surface | Implementation |
|---------|----------------|
| Marketing HTML / home template | Hardcoded footer |
| WP | `footer.php` + `template-parts/content-footer.php` |

Footer links include services, WhatsApp/Telegram, privacy/legal pages, YouTube.

## CSS

| Asset | Consumers | Blast radius |
|-------|-----------|--------------|
| `css/normalize.css` | marketing + home template | global marketing |
| `css/main.css` | marketing + home | **sitewide marketing look** |
| `css/media.css` | marketing + home | responsive marketing |
| `css/fonts.css` | as linked | fonts |
| Theme `style.css` + enqueued base styles | WP blog/tariff/offer | WP surfaces |
| libs owl/fancybox CSS | both families | carousels/lightboxes |

## JS

| Asset | Role | Blast radius |
|-------|------|--------------|
| `js/common.js` | forms, calculator, tariffs | **revenue-critical global** |
| `libs/jquery`, owl, fancybox, respond, html5shiv | UI libs | global |
| theme `js/script.js` | theme behaviors | WP |
| Rate My Post JS | blog ratings | blog |
| jquery.mask CDN | phone masks | forms |

Theme `functions.php` enqueues several docroot assets into WP (including `js/common.js`).

## Analytics / verification / scripts

| Kind | Notes |
|------|-------|
| Search verification files | `google*.html`, `yandex_*.html` at docroot — protect |
| Jetpack | Active — may inject scripts/features |
| Inline/third-party in HTML heads | Check both static and theme channels |
| Exact GA/Metrika IDs | Inspect per task; not fully inventoried here |

## Menus

| Source | Scope |
|--------|-------|
| WP menu «Меню 1» / Primary (`menu-1`) | WP chrome consumers of `wp_nav_menu` |
| Hardcoded topbar/footer links | Static + theme parts — **primary practical nav for marketing IA** |

## Contact details

Appear hardcoded in footers/topbars (phones, Telegram, WhatsApp, mailto). Changing “contacts globally” requires multi-file search across static HTML and theme parts — not a single WP option page identified.

## Shared dependency warning

Changing `css/main.css` or `js/common.js` affects:

- `/` (via `page-home.php`)
- nearly all marketing HTML
- WP surfaces that enqueue common.js
- calculator/tariff/forms behavior

Treat as **protected shared assets**.

---

*Global component dependency map v1 · 2026-07-24.*
