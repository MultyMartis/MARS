# SITE-001 WF-V2-W4 Final Surface Cleanup Change Request v1

**CR ID:** CR-SITE-001-WFV2-W4-2026-06-10  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST — `https://sibcar.new-site.space/`  
**Charter:** [SITE-001-WFV2-W4-FINAL-SURFACE-CLEANUP-WRITE-CHARTER-v1.md](SITE-001-WFV2-W4-FINAL-SURFACE-CLEANUP-WRITE-CHARTER-v1.md)

---

## Summary

Final surface cleanup for Used PDP after WF-V2-W3 layout recomposition. Subtractive CSS pass removes excess backgrounds, borders, shadows, grey panels, and nested box surfaces. Twig class hook only. No layout rebuild.

**Baseline:** WF-V2-W3 on TEST.

---

## Changes

| Task | Change |
|------|--------|
| **W4-01** | White showroom page — kill grey stage background |
| **W4-02** | Hero unified surface — no nested panels |
| **W4-03** | Offer column — remove mini-card chrome around price/payment/discounts |
| **W4-04** | Specs — divider list instead of bordered grid box |
| **W4-05** | CTA — flat chrome, preserve red buttons |
| **W4-06** | Trust strip — single light top divider |
| **W4-07** | Equipment — spec sheet rows, no grey box columns |
| **W4-08** | Credit — connected section, no floating dark card |
| **W4-09** | Layer 3 — minimal section chrome |

---

## Files touched

| Remote | Change type |
|--------|-------------|
| `catalog/view/theme/auto/template/product/product.twig` | Add `wfv2-surface-pdp` class hook |
| `css/main.css` | WF-V2-W4 surface cleanup block append |
| `css/media.css` | WF-V2-W4 responsive surface block append |

**Not modified:** header, footer, PHP, JS, DB.

---

## Risk

| Risk | Severity | Mitigation |
|------|----------|------------|
| Over-flattening hierarchy | Medium | Keep light dividers + red CTA |
| W3 layout regression | Low | W4 scoped to `.wfv2-surface-pdp`; no geometry changes |
| Catalog/header leak | Low | `.used_car_page` + negative marker verify |
| Modal/form break | Low | No JS/DOM logic changes |

---

## Rollback

T1: restore `product.twig`, `main.css`, `media.css` from `pre-wfv2-w4-final-surface-cleanup-*` + cache clear.

Prior baseline: WF-V2-W3 (`pre-wfv2-w3-layout-recomposition-20260610-0413`).
