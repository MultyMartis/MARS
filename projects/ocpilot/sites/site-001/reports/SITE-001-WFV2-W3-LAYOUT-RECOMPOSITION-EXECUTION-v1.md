# SITE-001 WF-V2-W3 PDP Layout Recomposition Execution v1

**Type:** Execution report — WF V2 Wave 3 Used PDP Layout Recomposition  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-WFV2-W3-2026-06-10  
**Canonical pre-write backup:** `pre-wfv2-w3-layout-recomposition-20260610-0413`

---

## Summary

WF-V2-W3 deployed to TEST: **PDP layout recomposition** — hero geometry 68/32, showroom-width container (Used PDP scoped), offer column DOM reorder (price → payment → CTA → specs → discounts), Layer 3 vertical stack (equipment then credit). Twig hook `wfv2-layout-pdp` + WF-V2-W3 layout CSS block (~120 lines main + ~55 lines media). **8/8** URLs **PASS**. Modal **PASS**. No header/catalog/homepage leak.

---

## Pre-write artefacts

| Artefact | Status |
|----------|--------|
| [SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-WRITE-CHARTER-v1.md](SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-WRITE-CHARTER-v1.md) | **ACTIVE** |
| [SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-CHANGE-REQUEST-v1.md](SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-CHANGE-REQUEST-v1.md) | CR-SITE-001-WFV2-W3-2026-06-10 |
| [SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-ROLLBACK-PLAN-v1.md](SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-ROLLBACK-PLAN-v1.md) | **CREATED** |
| Backup `pre-wfv2-w3-layout-recomposition-20260610-0413` | **DONE** |

---

## Files modified (TEST FTP)

| File | Pre bytes | Post bytes | Delta |
|------|-----------|------------|-------|
| `product.twig` | 38,029 | 38,185 | offer column DOM reorder |
| `css/main.css` | 209,691 | 212,975 | +WF-V2-W3 layout block |
| `css/media.css` | 54,111 | 55,575 | +WF-V2-W3 responsive block |

**Not modified:** header, footer, PHP, JS, DB

**Working copy:** `.recovery-temp/site-001-wfv2-w3-work/`  
**Result JSON:** `.recovery-temp/site-001-wfv2-w3-result.json`  
**Execute script:** `.recovery-temp/site-001-wfv2-w3-execute.py`

---

## Container width audit (W3-02)

| Metric | Pre (W2A) | Post (W3) |
|--------|-----------|-----------|
| `.container` max-width (global base) | 1620px | 1620px (unchanged) |
| Used PDP `main > .container` max-width | 1620px (inherited) | **1780px** (scoped) |
| Used PDP `.row` horizontal padding | 50px × 2 | **28px × 2** |
| Effective content width (approx.) | ~1520px | **~1724px** (+13%) |

Scope: `.used_car_page` only — catalog/homepage unaffected.

---

## Task execution

### W3-01 — Hero dominance

| Item | Mechanism |
|------|-----------|
| Gallery column | `68%` width desktop (`62%` at ≤1199px) |
| Offer column | `32%` width desktop (`38%` at ≤1199px) |
| Gallery height | `min-height: 480px`; `height: min(50vw, 560px)` |
| Mobile | Full-width stack at ≤991px |

### W3-03 / W3-04 — Offer column hierarchy

| Order | Block | Twig hook |
|-------|-------|-----------|
| 1 | Price + monthly payment | `wfv2-pdp-offer-pricing` |
| 2 | CTA group | `wfv2-pdp-offer-cta` |
| 3 | Characteristics | `wfv2-pdp-offer-specs` |
| 4 | Discounts | `wfv2-pdp-offer-rest` |

DOM order verified live: pricing → CTA → specs → rest.

### W3-05 — Layer 3 sequential

| Item | Mechanism |
|------|-----------|
| Desktop layout | `flex-direction: column` overrides W2A 60/40 grid |
| Equipment | `order: 1`, full width |
| Credit | `order: 2`, full width |

### W3-06 — Reading path

Preserved W2A zones; W3 enforces: car → price → CTA → specs → discounts → trust → equipment → credit → reviews → banks → similar.

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

**Used PDP layout order:** pricing_before_cta ✓ · cta_before_specs ✓ · specs_before_rest ✓ · equipment_before_credit ✓

**Modal:** credit popup opens and closes — **PASS**

**CSS live:** `WF-V2-W3 PDP Layout Recomposition` present in main.css + media.css

---

## QA screenshots

**Folder:** `projects/ocpilot/sites/site-001/qa/wfv2-w3-layout-screenshots/`

| Phase | Desktop labels |
|-------|----------------|
| before | `before-desktop-used-pdp-full.png`, `hero`, `offer-column`, `equipment`, `credit-block` |
| after | `after-desktop-used-pdp-full.png`, `hero`, `offer-column`, `equipment`, `credit-block` |

Tablet + mobile variants captured for same labels.

---

## Rollback

T1: restore 3 files from `pre-wfv2-w3-layout-recomposition-20260610-0413` + cache clear.  
Prior baseline: WF-V2-W2A (`pre-wfv2-w2a-pdp-anatomy-rebuild-20260610-0401`).

---

## Overall

**WF-V2-W3 — PASS** (composition-only; no cosmetic additions)
