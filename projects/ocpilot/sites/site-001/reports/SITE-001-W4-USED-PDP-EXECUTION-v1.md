# SITE-001 W4 Used PDP Execution v1

**Type:** Execution report — W4 Used PDP Structural Visual Slice  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-W4-2026-06-09  
**Checkpoint:** `site-001-phase1-stable-2026-06`

---

## Summary

W4 deployed to TEST: **twig wrapper grouping** in `product.twig` + **scoped CSS block** (W4-A…W4-I) in `main.css` / `media.css`. All verification URLs **PASS**. No PHP/JS/DB changes.

---

## Pre-write artefacts

| Artefact | Status |
|----------|--------|
| [SITE-001-W4-USED-PDP-WRITE-CHARTER-v1.md](SITE-001-W4-USED-PDP-WRITE-CHARTER-v1.md) | **ACTIVE** |
| [SITE-001-W4-USED-PDP-CHANGE-REQUEST-v1.md](SITE-001-W4-USED-PDP-CHANGE-REQUEST-v1.md) | CR-SITE-001-W4-2026-06-09 |
| [SITE-001-W4-USED-PDP-ROLLBACK-PLAN-v1.md](SITE-001-W4-USED-PDP-ROLLBACK-PLAN-v1.md) | **CREATED** |
| [SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md](SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md) | **CREATED** |
| Backup `pre-w4-20260609` | **DONE** |

---

## Files modified (TEST FTP)

| File | Pre bytes | Post bytes | Delta |
|------|-----------|------------|-------|
| `catalog/view/theme/auto/template/product/product.twig` | 37 043 | 33 078 | +10 wrapper divs, 6 class additions |
| `css/main.css` | 129 060 | 139 328 | +W4 block (~450 lines) |
| `css/media.css` | 32 601 | 35 044 | +W4 responsive block |

**Working copy:** `.recovery-temp/site-001-w4-work/`  
**Result JSON:** `.recovery-temp/site-001-w4-result.json`

---

## Twig changes (used PDP only)

| Change | Detail |
|--------|--------|
| `w4-used-badges` | class on `short_btns` |
| `w4-used-hero` | wrapper around `.car_main_info` |
| `w4-used-hero__gallery` | class on photo column |
| `w4-used-hero__panel` | class on main column |
| `w4-used-hero__offer` | wraps price + discount |
| `w4-used-hero__specs` | wraps characteristics grid |
| `w4-used-hero__actions` | wraps CTA row |
| `w4-used-trust-strip` | class on VIN block |
| `w4-used-equipment` | class on configuration |
| `w4-used-credit` | class on credit section |

All twig variables, loops, modal IDs, forms, and inline scripts **preserved verbatim**.

---

## CSS zones deployed

| Zone | Mechanism |
|------|-----------|
| W4-A | Pill status badges |
| W4-B | Unified hero card shell |
| W4-C | Edge-to-edge gallery 440px crop |
| W4-D | Commercial offer band — 42px price, credit pill |
| W4-E | 4-col spec card grid |
| W4-F | Primary + outline CTA hierarchy |
| W4-G | Light premium trust strip |
| W4-H | Equipment 2-col scan tiles |
| W4-I | Credit panel — white inputs, styled submit |

All selectors scoped under `.used_car_page`.

---

## Cache clear

| Action | HTTP |
|--------|------|
| Modification refresh | 200 |
| System cache reset | 200 |
| Image cache reset | 200 |

---

## Verification (HTTP 2026-06-09)

| URL | HTTP | W4 markers | Regression |
|-----|------|------------|------------|
| `/audi-a1-2012-s-probegom-149-000-km-799` | 200 | **ALL PASS** (`w4-used-hero`, `w4-used-trust-strip`, `w4-used-credit`, `w4-used-badges`) | — |
| `/cars/` | 200 | — | **PASS** (no w4 leak) |
| `/cars/bmw/` | 200 | — | **PASS** |
| `/` | 200 | — | **PASS** |
| `/about` | 200 | — | **PASS** |
| `/contact/` | 200 | — | **PASS** |

**Overall:** **PASS**

---

## Screenshot checklist (operator HITL)

Automated HTTP verification confirms markup deployment. **Visual screenshots not captured in this session** — operator should capture:

| Viewport | Required shots |
|----------|----------------|
| Desktop 1440px | Full PDP; hero crop; equipment section; credit form |
| Tablet 768px | Hero stack; trust strip |
| Mobile 375px | Hero; CTA column; credit form |

Compare against pre-W4 baseline from backup session or prior operator captures.

---

## Scope compliance

| Check | Result |
|-------|--------|
| PHP changed | **NO** |
| JS logic changed | **NO** |
| DB changed | **NO** |
| SEO changed | **NO** |
| header/footer touched | **NO** |
| productnew.twig touched | **NO** |
| Production deployed | **NO** |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **EXECUTED** — W4 used PDP slice on TEST; verification 6/6 PASS |

*SITE-001 W4 Used PDP Execution v1 — TEST only; no commit; no push.*
