# SITE-001 W5-C Used PDP Execution v1

**Type:** Execution report — W5-C Used PDP Commercial Stage  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-W5C-2026-06-10  
**Backup:** `pre-w5c-commercial-stage-20260610-0002`

---

## Summary

W5-C deployed to TEST: **commercial stage wrapper** + **W5-C CSS block** (~370 lines main + ~110 lines media) + **twig class additions**. **8/8** URLs **PASS**. Modal interaction **PASS**. W5-A header **preserved**. W4 markers **preserved**.

---

## Pre-write artefacts

| Artefact | Status |
|----------|--------|
| [SITE-001-W5-STABLE-BACKUP-v1.md](SITE-001-W5-STABLE-BACKUP-v1.md) | **DONE** |
| [SITE-001-W5C-USED-PDP-COMMERCIAL-STAGE-DESIGN-PLAN-v1.md](SITE-001-W5C-USED-PDP-COMMERCIAL-STAGE-DESIGN-PLAN-v1.md) | **DONE** — safety **SAFE** |
| [SITE-001-W5C-USED-PDP-WRITE-CHARTER-v1.md](SITE-001-W5C-USED-PDP-WRITE-CHARTER-v1.md) | **ACTIVE** |
| Backup `pre-w5c-commercial-stage-20260610-0002` | **DONE** — manifest present |

---

## Files modified (TEST FTP)

| File | Pre bytes | Post bytes | Delta |
|------|-----------|------------|-------|
| `product.twig` | 37,389 | 37,479 | +`w5c-commercial-stage`, `w5c-equipment-grid`, `w5c-credit-panel`, `w5c-pdp-modal` |
| `css/main.css` | 156,101 | 173,031 | +W5-C block (~370 lines) |
| `css/media.css` | 41,521 | 44,591 | +W5-C responsive block |

**Not deployed:** `header.twig` (backed up only)

**Working copy:** `.recovery-temp/site-001-w5c-work/`  
**Result JSON:** `.recovery-temp/site-001-w5c-result.json`

---

## Task execution

### A — Commercial stage hero

| Item | Mechanism |
|------|-----------|
| Unified offer deck | `w5c-commercial-stage` wraps badges + hero + trust |
| Single scene | Gradient shell; hero card radius fused to trust strip bottom |
| Gallery | 480px crop under stage scope |

### B — Price / offer block

| Item | Mechanism |
|------|-----------|
| Price anchor | 52px / weight 800 under `.w5c-commercial-stage` |
| Credit secondary | Side card with border; demoted typography |
| Discount | 3-col mini-cards replacing flat strip |

### C — Trust / VIN strip

| Item | Mechanism |
|------|-----------|
| Trust cards | 4-col grid with pill status badges |
| VIN CTA | Solid red button; removed outline-only CRM look |

### D — Equipment block

| Item | Mechanism |
|------|-----------|
| Spec sheet | `w5c-equipment-grid` — 3-col, hover accent |
| Toggle | Pill «Показать всё» — existing `#toggleConfigBtn` preserved |

### E — Credit form block

| Item | Mechanism |
|------|-----------|
| Inset panel | White card on dark shell (`w5c-credit-panel`) |
| Inputs | 52px height, focus ring, premium submit |

### F — Modal form

| Item | Mechanism |
|------|-----------|
| Scope | `body.used_car_page` — no footer.twig edit |
| Targets | `#credit__FORM_popup`, `#tradein__FORM_popup`, `#installment__FORM_popup`, `#VIN_lead_popup` |
| Structure | Light shell, 28px padding zones, readable checkbox/legal |

**JS/PHP:** **NOT MODIFIED**

---

## Verification (8 URLs)

| Page | HTTP | Markers | Leak check | Result |
|------|------|---------|------------|--------|
| `/` | 200 | w5a-header-shell | no w5c | **PASS** |
| `/about` | 200 | w5a-header-shell | — | **PASS** |
| `/contact/` | 200 | w5a-header-shell | — | **PASS** |
| `/cars/` | 200 | catalog_item | no w5c | **PASS** |
| `/cars/bmw/` | 200 | search_wrap | — | **PASS** |
| `/auto/` | 200 | catalog_item | no w5c | **PASS** |
| `/auto/haval/` | 200 | search_wrap | — | **PASS** |
| used PDP | 200 | w5c-commercial-stage + w4-used-hero | — | **PASS** |

**CSS live:** main 173,031 bytes · W5-C marker **YES** · W5-A + W5-A-S **YES**

---

## Modal interaction

| Check | Result |
|-------|--------|
| Credit modal opens | **PASS** |
| Name field visible | **PASS** |
| Checkbox visible | **PASS** |
| Legal links present | **PASS** |
| Modal closes (Escape) | **PASS** |

---

## Screenshots

**Path:** `projects/ocpilot/sites/site-001/qa/w5c-used-pdp-commercial-stage-screenshots/`

| Set | Files |
|-----|-------|
| Before desktop | full-top, hero, trust, equipment, credit, modal |
| After desktop | full-top, hero, trust, equipment, credit, modal |
| Before mobile | hero, modal |
| After mobile | hero, modal |

---

## Cache clear

System · modification · image · modification refresh — all **200**.

---

## Status

**DONE** on TEST — automated verification **PASS**. Operator visual HITL **PENDING**.

*SITE-001 W5-C Used PDP Execution v1 — TEST only; no commit; no push.*
