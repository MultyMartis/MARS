# SITE-001 WF-V2-W4 Final Surface Cleanup Execution v1

**Type:** Execution report — WF V2 Wave 4 Used PDP Final Surface Cleanup  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-WFV2-W4-2026-06-10  
**Canonical pre-write backup:** `pre-wfv2-w4-final-surface-cleanup-20260610-0447`

---

## Summary

WF-V2-W4 deployed to TEST: **final surface cleanup** — subtractive CSS pass removes excess backgrounds, borders, shadows, grey panels, and nested box surfaces accumulated across W5-C/W2/W2S waves. Twig hook `wfv2-surface-pdp` + WF-V2-W4 surface CSS block (~220 lines main + ~55 lines media). **8/8** URLs **PASS**. Modal **PASS**. No header/catalog leak. W3 layout order preserved.

---

## Pre-write artefacts

| Artefact | Status |
|----------|--------|
| [SITE-001-WFV2-W4-FINAL-SURFACE-CLEANUP-WRITE-CHARTER-v1.md](SITE-001-WFV2-W4-FINAL-SURFACE-CLEANUP-WRITE-CHARTER-v1.md) | **ACTIVE** |
| [SITE-001-WFV2-W4-FINAL-SURFACE-CLEANUP-CHANGE-REQUEST-v1.md](SITE-001-WFV2-W4-FINAL-SURFACE-CLEANUP-CHANGE-REQUEST-v1.md) | CR-SITE-001-WFV2-W4-2026-06-10 |
| [SITE-001-WFV2-W4-FINAL-SURFACE-CLEANUP-ROLLBACK-PLAN-v1.md](SITE-001-WFV2-W4-FINAL-SURFACE-CLEANUP-ROLLBACK-PLAN-v1.md) | **CREATED** |
| Backup `pre-wfv2-w4-final-surface-cleanup-20260610-0447` | **DONE** |

---

## Files modified (TEST FTP)

| File | Pre bytes | Post bytes | Delta |
|------|-----------|------------|-------|
| `product.twig` | 38,185 | 38,202 | +`wfv2-surface-pdp` class hook |
| `css/main.css` | 212,975 | 221,632 | +WF-V2-W4 surface block |
| `css/media.css` | 55,575 | 57,219 | +WF-V2-W4 responsive block |

**Not modified:** header, footer, PHP, JS, DB

**Working copy:** `.recovery-temp/site-001-wfv2-w4-work/`  
**Result JSON:** `.recovery-temp/site-001-wfv2-w4-result.json`  
**Execute script:** `.recovery-temp/site-001-wfv2-w4-execute.py`

---

## Surface changes (W4)

| Area | Before (W3 state) | After (W4) |
|------|-------------------|------------|
| Page stage | Grey `#f7f8fa` panel background | White `#ffffff` showroom |
| Hero | Nested gallery/panel surfaces | Unified transparent hero |
| Credit price | Grey mini-card `#f3f4f6` | Flat inline payment line |
| Specs grid | Bordered 4-col box | Divider list, no outer box |
| Equipment | Box rows with borders/shadows | Spec sheet rows, light dividers |
| Credit block | Residual widget chrome | Connected section, top divider only |
| CTA | Preserved | Red buttons kept, shadows removed |

---

## Verification (8 URLs)

| URL | HTTP | Markers | Leak | Result |
|-----|------|---------|------|--------|
| `/` | 200 | OK | none | **PASS** |
| `/about` | 200 | OK | none | **PASS** |
| `/contact/` | 200 | OK | none | **PASS** |
| `/cars/` | 200 | OK | none | **PASS** |
| `/cars/bmw/` | 200 | OK | none | **PASS** |
| `/auto/` | 200 | OK | none | **PASS** |
| `/auto/haval/` | 200 | OK | none | **PASS** |
| Used PDP | 200 | OK | none | **PASS** |

**Used PDP markers:** `wfv2-surface-pdp` ✓ · `wfv2-layout-pdp` ✓ · layout order preserved ✓

**Modal:** credit popup opens and closes — **PASS**

**CSS live:** `WF-V2-W4 Final Surface Cleanup` present in main.css + media.css

---

## QA screenshots

**Folder:** `projects/ocpilot/sites/site-001/qa/wfv2-w4-final-surface-cleanup-screenshots/`

| Phase | Desktop | Mobile |
|-------|---------|--------|
| before | `before-desktop-used-pdp-full.png`, `hero`, `offer-column`, `equipment`, `credit-block` | `before-mobile-*` (same labels) |
| after | `after-desktop-used-pdp-full.png`, `hero`, `offer-column`, `equipment`, `credit-block` | `after-mobile-*` (same labels) |

---

## Rollback

T1: restore 3 files from `pre-wfv2-w4-final-surface-cleanup-20260610-0447` + cache clear.  
Prior baseline: WF-V2-W3 (`pre-wfv2-w3-layout-recomposition-20260610-0413`).

---

## Overall

**WF-V2-W4 — PASS** (surface cleanup only; W3 layout intact)

**Commit / push / production:** NOT AUTHORIZED
