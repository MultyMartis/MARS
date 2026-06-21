# SITE-001 W5-A Header Shell Recomposition Execution v1

**Type:** Execution report — W5-A Header Shell  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-W5A-2026-06-09  
**Backup:** `pre-w5a-header-shell-20260609-2251`

---

## Summary

W5-A deployed to TEST: **header DOM regroup** (contact rail + primary band + CTA cluster) + **W5-A CSS block** in `main.css` / `media.css`. W4.1 sticky **reverted** (`position: static`). Promo strip **inset** via sibling CSS. **8/8** verification URLs **PASS**. W4 Used PDP markers **preserved**. No PHP/JS/DB/product.twig changes.

Post-deploy fix: `header_cup` moved **after** primary band (homepage nav no longer below hero). CSS nav/CTA overlap patch applied.

---

## Pre-write artefacts

| Artefact | Status |
|----------|--------|
| [SITE-001-W5A-HEADER-SHELL-WRITE-CHARTER-v1.md](SITE-001-W5A-HEADER-SHELL-WRITE-CHARTER-v1.md) | **ACTIVE** |
| [SITE-001-W5A-HEADER-SHELL-CHANGE-REQUEST-v1.md](SITE-001-W5A-HEADER-SHELL-CHANGE-REQUEST-v1.md) | CR-SITE-001-W5A-2026-06-09 |
| [SITE-001-W5A-HEADER-SHELL-ROLLBACK-PLAN-v1.md](SITE-001-W5A-HEADER-SHELL-ROLLBACK-PLAN-v1.md) | **CREATED** |
| Backup `pre-w5a-header-shell-20260609-2251` | **DONE** — manifest present |

---

## Files modified (TEST FTP)

| File | Pre bytes | Post bytes | Delta |
|------|-----------|------------|-------|
| `header.twig` | 11,719 | 12,498 | DOM regroup — W5-A shell |
| `css/main.css` | 146,267 | 152,727 | +W5-A block (~258 lines) |
| `css/media.css` | 36,456 | 38,864 | +W5-A responsive block |

**Working copy:** `.recovery-temp/site-001-w5a-work/`  
**Result JSON:** `.recovery-temp/site-001-w5a-result.json`

---

## Twig architecture changes

| Zone | Before (W4.1) | After (W5-A) |
|------|---------------|--------------|
| Band 1 | `.singe_bar__wrap` toolbar — logo · address · phone · WA · callback | `.w5a-header__contact-rail` — address · hours · compact phone/WA |
| Band 2 | `<nav>` below toolbar / hero | `.w5a-header__primary-band` — logo anchor · centered nav · CTA cluster |
| Band 3 | `.lcd_display.header` separate sibling | **Unchanged DOM** — CSS inset integration into shell footer |
| `header_cup` | Between toolbar and nav | **After** primary band (inside `<header>`) |
| Tagline | Visible in toolbar logo | Present in DOM; **hidden** via W5-A CSS |

All links, menu items, phone, WhatsApp, callback targets **preserved verbatim**.

---

## CSS zones deployed

| Zone | Mechanism |
|------|-----------|
| W5-A-A | Static header — W4.1 sticky override |
| W5-A-B | Contact rail — compact support line |
| W5-A-C | Primary band — single graphite dealer block |
| W5-A-D | Centered navigation group |
| W5-A-E | CTA hierarchy — callback > phone > WhatsApp |
| W5-A-F | Inset promo — sibling `.lcd_display.header` shell footer |

W4.1 block **retained** (W4.1-D/E PDP rules preserved). W5-A rules **supersede** W4.1-A sticky and toolbar/nav seam.

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

**Live CSS:** W5-A block confirmed · W4.1 · W4 · W3UX-C1 · W3ATMOSPHERE present. Sticky override confirmed.

---

## W4 preservation (used PDP)

| Marker | Present |
|--------|---------|
| `w4-used-hero` | **YES** |
| `w4-used-trust-strip` | **YES** |
| `w4-used-credit` | **YES** |

---

## Screenshots

**Path:** `projects/ocpilot/sites/site-001/qa/w5a-header-shell-screenshots/`

| Phase | Pages | Viewports |
|-------|-------|-----------|
| Before | homepage, used_catalog, used_pdp, about | desktop + mobile |
| After | homepage, used_catalog, used_pdp, about | desktop + mobile |

Homepage `after-desktop` **retaken** after `header_cup` order fix.

---

## Operator HITL

**PENDING** — 3-second silhouette test (logo hidden) · visual impact rating vs W4.1 baseline.
