# SITE-001 WF-V2-W2A PDP Anatomy Rebuild Execution v1

**Type:** Execution report — WF V2 Wave 2-A Used PDP Anatomy Rebuild  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-WFV2-W2A-2026-06-10  
**Canonical pre-write backup:** `pre-wfv2-w2a-pdp-anatomy-rebuild-20260610-0356`

---

## Summary

WF-V2-W2A deployed to TEST: **PDP anatomy rebuild** — commercial stage unified (H1+status+hero+trust), Layer 3 grid (Equipment 60% + Credit 40%), reviews relocated below Layer 3, `lcd_display.product` moved below fold, duplicate credit car image removed. Twig hook `wfv2-anatomy-pdp` + WF-V2-W2A layout CSS block (~95 lines main + ~35 lines media). **8/8** URLs **PASS**. Modal **PASS**. WF-V2-W1 header **unchanged**.

**Note:** First deploy attempt (0356 run) produced partial twig; corrected and redeployed in run `0401` using clean baseline from backup `0356`.

---

## Pre-write artefacts

| Artefact | Status |
|----------|--------|
| [SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-WRITE-CHARTER-v1.md](SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-WRITE-CHARTER-v1.md) | **ACTIVE** |
| [SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-CHANGE-REQUEST-v1.md](SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-CHANGE-REQUEST-v1.md) | CR-SITE-001-WFV2-W2A-2026-06-10 |
| [SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-ROLLBACK-PLAN-v1.md](SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-ROLLBACK-PLAN-v1.md) | **CREATED** |
| Design refs `01-sibcar-v2-concept.png` + `02-sibcar-v2-specification.png` | **VERIFIED** |
| Backup `pre-wfv2-w2a-pdp-anatomy-rebuild-20260610-0356` | **DONE** — clean W2S baseline (rollback anchor) |
| Backup `pre-wfv2-w2a-pdp-anatomy-rebuild-20260610-0401` | **DONE** — live snapshot before fix redeploy |

---

## Files modified (TEST FTP)

| File | Pre bytes (0356) | Post bytes | Delta |
|------|------------------|------------|-------|
| `product.twig` | 37,508 | 38,029 | anatomy DOM reorder |
| `css/main.css` | 207,020 | 209,691 | +WF-V2-W2A layout block |
| `css/media.css` | 53,279 | 54,111 | +WF-V2-W2A responsive block |

**Backed up, not modified:** `header.twig`  
**Not modified:** `footer.twig`, PHP, JS, DB

**Working copy:** `.recovery-temp/site-001-wfv2-w2a-work/`  
**Result JSON:** `.recovery-temp/site-001-wfv2-w2a-result.json`  
**Execute script:** `.recovery-temp/site-001-wfv2-w2a-execute.py`

---

## Task execution

### A / C-01 — Identity integration

| Item | Mechanism |
|------|-----------|
| H1 relocation | Single `<h1>` in `wfv2-pdp-identity-row` inside commercial stage |
| pdp-top | Breadcrumbs only — `page_title desck` removed |
| Mobile duplicate | `page_title mobile` removed — one title logic |

### B / C-03 — Commercial stage anatomy

| Item | Mechanism |
|------|-----------|
| Identity row | `wfv2-pdp-identity-row` — H1 + status badges |
| Hero split | `wfv2-pdp-hero-split` — gallery + offer stack |
| Trust line | `wfv2-pdp-trust-line` — condition/restrictions/accidents/VIN |

### C / C-08 — lcd_display.product

| Item | Mechanism |
|------|-----------|
| Removed from hero→equipment gap | DOM cut from commercial stage |
| Below fold | `wfv2-pdp-fold-below` after reviews zone |

### D / C-09 — Layer 3

| Item | Mechanism |
|------|-----------|
| Grid wrapper | `wfv2-pdp-layer3` — 3fr/2fr (≈60/40) desktop |
| Equipment column | `wfv2-pdp-layer3__equipment` |
| Credit column | `wfv2-pdp-layer3__credit` |
| Mobile | Single-column stack via media block |

### E / C-10 — Reviews position

| Item | Mechanism |
|------|-----------|
| Reviews zone | `wfv2-pdp-reviews-zone` after Layer 3 |

### F / C-11 — Credit image dedup

| Item | Mechanism |
|------|-----------|
| Hero duplicate | `used_car__credit__slider` removed from twig |
| CSS guard | `.wfv2-pdp-layer3 .used_car__credit__slider { display: none }` |

---

## Verification (8 URLs)

| Page | HTTP | Markers | Leak check | Result |
|------|------|---------|------------|--------|
| `/` | 200 | wfv2-header | no wfv2-anatomy-pdp | **PASS** |
| `/about` | 200 | wfv2-header | — | **PASS** |
| `/contact/` | 200 | wfv2-header + form | — | **PASS** |
| `/cars/` | 200 | catalog_item | no wfv2-anatomy-pdp | **PASS** |
| `/cars/bmw/` | 200 | search_wrap | — | **PASS** |
| `/auto/` | 200 | catalog_item | — | **PASS** |
| `/auto/haval/` | 200 | search_wrap | — | **PASS** |
| used PDP | 200 | wfv2-anatomy-pdp + layer3 + reviews-zone | anatomy order | **PASS** |

**PDP anatomy order checks:** trust → layer3 → reviews → lcd_fold · credit_slider absent — **PASS**

**CSS live:** main 209,691 bytes · WF-V2-W2A marker **YES** · WF-V2-W2S + W2 + W1 **YES**

---

## Interaction checks

| Check | Result |
|-------|--------|
| Credit modal opens | **PASS** |
| Modal closes (Escape) | **PASS** |

---

## Screenshots

**Path:** `projects/ocpilot/sites/site-001/qa/wfv2-w2a-pdp-anatomy-screenshots/`

| Set | Viewports | Labels |
|-----|-----------|--------|
| Before | desktop, tablet, mobile | used-pdp-full, commercial-stage, layer3-zone, reviews-zone |
| After | desktop, tablet, mobile | used-pdp-full, commercial-stage, layer3-zone, reviews-zone |

Before set captured from pre-W2A baseline run (`0356`). After set from corrected deploy (`0401`).

---

## Cache clear

System · modification · image · modification refresh — all **200**.

---

## UNKNOWN

| Item | Status |
|------|--------|
| Standalone file «SITE-001 PDP Composition Audit» in repo | **SAFE UNKNOWN** — scope applied from operator mandate C-01..C-11 |
| Operator visual HITL | **PENDING** |

---

## Status

**DONE** on TEST — automated verification **8/8 PASS**. Operator visual HITL **PENDING**.

*SITE-001 WF-V2-W2A PDP Anatomy Rebuild Execution v1 — TEST only; no commit; no push.*
