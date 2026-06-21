# SITE-001 W4.1 Header & Hero Authority Design Plan v1

**Type:** Pre-implementation design plan — header & hero authority slice  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Baseline:** W4 Used PDP accepted · W3UX-C1 active · W3ATMOSPHERE active

---

## 1. Current problem

| Issue | Detail |
|-------|--------|
| Old auto salon template feel | Header reads as stacked legacy bars — white toolbar, dark nav, red promo ticker — not one dealership shell |
| Competing red zones | Logo tagline border, callback CTA, nav hover red, phone icon red, promo marquee red background — all shout equally |
| Fragmented header | `singe_bar__wrap`, `nav`, and `lcd_display.header` feel like four separate layers fighting for attention |
| Weak PDP entry | Used PDP top (breadcrumbs + H1) disconnected from header authority; W4 hero improvements start below a generic OpenCart title block |

---

## 2. Target

| Goal | Mechanism |
|------|-----------|
| Stronger first impression | Sticky unified header shell with toolbar + nav as one premium automotive frame |
| Cleaner header | Reduced padding noise; single shadow; nav/toolbar visual seam |
| Authoritative top area | Used PDP breadcrumbs + H1 in dedicated `w4-1-pdp-top` band aligned with new header tone |
| Premium automotive feeling | Graphite nav gradient; controlled red on primary CTA only; demoted legacy red accents |
| Less visual noise | Promo strip integrated as subtle graphite band — not legacy red ticker banner |

**Target visual impact:** **7/10** on first screen (homepage + used PDP).

---

## 3. What may change

| Area | Allowed change |
|------|----------------|
| Header visual styling | Sticky shell, toolbar/nav integration, logo sizing, CTA elevation |
| Top/nav styling | Nav height, hover underline discipline, typography weight |
| Promo strip styling | `.lcd_display.header` — graphite band, uppercase text, red dot accent |
| PDP top treatment | `w4-1-pdp-top` wrapper — breadcrumbs + H1 authority band |
| Hero spacing | Tighten gap between PDP title block and W4 hero badges |
| Twig classes/wrappers | `header.twig`: `w4-1-header`, `w4-1-header__toolbar`, `w4-1-header__nav` · `product.twig`: `w4-1-promo-strip`, `w4-1-pdp-top` |

**CSS zones:** W4.1-A (shell) · W4.1-B (red discipline) · W4.1-C (promo) · W4.1-D (PDP top) · W4.1-E (catalog rhythm)

---

## 4. What must NOT change

| Area | Status |
|------|--------|
| Texts, menu items, URLs | **Frozen** |
| Logo file | **Frozen** |
| Phone / WhatsApp values | **Frozen** |
| Forms logic | **Frozen** |
| PHP, JS, DB | **Forbidden** |
| SEO | **Frozen** |
| Footer structure | **Frozen** (footer.twig not in allow-list) |
| W4 Used PDP work | **Preserve** — all `w4-used-*` wrappers and CSS untouched |
| Mobile menu logic | **Frozen** — CSS-only mobile adjustments |

---

## 5. Files allowed

| File | Change type |
|------|-------------|
| `catalog/view/theme/auto/template/common/header.twig` | Class additions on `<header>`, toolbar, `<nav>` |
| `catalog/view/theme/auto/template/product/product.twig` | Promo class + PDP top wrapper |
| `css/main.css` | Append W4.1 block after W4 end marker |
| `css/media.css` | Append W4.1 responsive block |

**footer.twig:** restore point included in backup; modify only if regression-safe color compatibility required (expected: **NO**).

---

## 6. Markup additions

| Addition | Location |
|----------|----------|
| `w4-1-header` | `<header>` element |
| `w4-1-header__toolbar` | `.singe_bar__wrap` inside header (not offcanvas) |
| `w4-1-header__nav` | `<nav>` inside header |
| `w4-1-promo-strip` | `.lcd_display.header` in product.twig |
| `w4-1-pdp-top` | Wrapper around breadcrumbs + desktop H1 |

---

## 7. Regression guard

- W4 CSS selectors remain under `.used_car_page` — W4.1 does not override W4-A…W4-I rules
- Verification matrix: 9 URLs (see execution report)
- W4 markers on used PDP must remain present post-deploy

---

## 8. Implementation gate

| Prerequisite | Status |
|--------------|--------|
| Stable backup `pre-w4-1-stable-*` | Required before write |
| Write charter | **DONE** |
| Change request | **DONE** |
| Rollback plan | **DONE** |
| Design plan (this doc) | **DONE** |

*SITE-001 W4.1 Header & Hero Authority Design Plan v1 — implementation follows this spec.*
