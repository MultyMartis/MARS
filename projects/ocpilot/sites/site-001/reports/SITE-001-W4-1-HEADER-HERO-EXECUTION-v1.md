# SITE-001 W4.1 Header & Hero Authority Execution v1

**Type:** Execution report — W4.1 Header & Hero Authority  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-W4-1-2026-06-09  
**Backup:** `pre-w4-1-stable-20260609-1506`

---

## Summary

W4.1 deployed to TEST: **header class additions** + **used PDP top wrapper** + **W4.1 CSS block** (W4.1-A…E) in `main.css` / `media.css`. All **9/9** verification URLs **PASS**. W4 Used PDP markers **preserved**. No PHP/JS/DB changes. Footer **not modified**.

---

## Pre-write artefacts

| Artefact | Status |
|----------|--------|
| [SITE-001-W4-STABLE-BACKUP-v1.md](SITE-001-W4-STABLE-BACKUP-v1.md) | **DONE** |
| [SITE-001-W4-1-HEADER-HERO-DESIGN-PLAN-v1.md](SITE-001-W4-1-HEADER-HERO-DESIGN-PLAN-v1.md) | **DONE** |
| [SITE-001-W4-1-HEADER-HERO-WRITE-CHARTER-v1.md](SITE-001-W4-1-HEADER-HERO-WRITE-CHARTER-v1.md) | **ACTIVE** |
| [SITE-001-W4-1-HEADER-HERO-CHANGE-REQUEST-v1.md](SITE-001-W4-1-HEADER-HERO-CHANGE-REQUEST-v1.md) | CR-SITE-001-W4-1-2026-06-09 |
| [SITE-001-W4-1-HEADER-HERO-ROLLBACK-PLAN-v1.md](SITE-001-W4-1-HEADER-HERO-ROLLBACK-PLAN-v1.md) | **CREATED** |
| Backup `pre-w4-1-stable-20260609-1506` | **DONE** |

---

## Files modified (TEST FTP)

| File | Pre bytes | Post bytes | Delta |
|------|-----------|------------|-------|
| `header.twig` | 11,653 | 11,719 | +3 classes on header/toolbar/nav |
| `product.twig` | 37,330 | 37,389 | +promo class + `w4-1-pdp-top` wrapper |
| `css/main.css` | 140,066 | 146,267 | +W4.1 block (~250 lines) |
| `css/media.css` | 35,060 | 36,456 | +W4.1 responsive block |
| `footer.twig` | — | — | **NOT MODIFIED** |

**Working copy:** `.recovery-temp/site-001-w4-1-work/`  
**Result JSON:** `.recovery-temp/site-001-w4-1-result.json`

---

## Twig changes

| Change | Detail |
|--------|--------|
| `w4-1-header` | class on `<header>` |
| `w4-1-header__toolbar` | class on `.singe_bar__wrap` (header only) |
| `w4-1-header__nav` | class on `<nav>` |
| `w4-1-promo-strip` | class on `.lcd_display.header` (product.twig) |
| `w4-1-pdp-top` | wrapper around breadcrumbs + desktop H1 |

All links, text, menu items, phone/WhatsApp values **preserved verbatim**.

---

## CSS zones deployed

| Zone | Mechanism |
|------|-----------|
| W4.1-A | Sticky unified header shell — toolbar/nav integration |
| W4.1-B | Red discipline — primary CTA elevation; demoted logo/phone red |
| W4.1-C | Promo strip — graphite band; uppercase text; red dot accent |
| W4.1-D | Used PDP top — breadcrumbs + H1 authority band |
| W4.1-E | Catalog/inner page top rhythm |

W4 Used PDP block (W4-A…I) **untouched**.

---

## Cache clear

| Action | HTTP |
|--------|------|
| cache_system | 200 |
| cache_modification | 200 |
| cache_image | 200 |
| modification_refresh | 200 |

---

## Verification matrix

| URL | HTTP | Pass |
|-----|------|------|
| `/` | 200 | **PASS** |
| `/about` | 200 | **PASS** |
| `/contact/` | 200 | **PASS** |
| `/cars/` | 200 | **PASS** |
| `/cars/bmw/` | 200 | **PASS** |
| `/auto/` | 200 | **PASS** |
| `/auto/haval/` | 200 | **PASS** |
| `/audi-a1-2012-s-probegom-149-000-km-799` | 200 | **PASS** (W4 preserved) |
| `/baic-bj40-new` | 200 | **PASS** |

**Live CSS:** W4.1 block confirmed · W3UX-C1 · W3ATMOSPHERE · W4 all present.

---

## W4 preservation (used PDP)

| Marker | Present |
|--------|---------|
| `w4-used-hero` | **YES** |
| `w4-used-trust-strip` | **YES** |
| `w4-used-credit` | **YES** |

---

## Screenshots

**Path:** `projects/ocpilot/sites/site-001/qa/w4-1-header-hero-screenshots/`

| Phase | Desktop | Mobile |
|-------|---------|--------|
| Before | homepage, used_pdp, used_catalog, about | homepage, used_pdp |
| After | homepage, used_pdp, used_catalog, about | homepage, used_pdp |

16 PNG files captured (2026-06-09 15:06–15:08).

---

## Overall

**Technical verification:** **PASS** — 9/9 URLs · live CSS · W4 preserved  
**Operator visual HITL:** **PENDING** — target 7/10 first-screen impact

*SITE-001 W4.1 Header & Hero Authority Execution v1 — TEST only; no commit; no push.*
