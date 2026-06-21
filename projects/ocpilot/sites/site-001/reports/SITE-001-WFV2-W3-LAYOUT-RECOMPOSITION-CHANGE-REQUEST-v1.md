# SITE-001 WF-V2-W3 PDP Layout Recomposition Change Request v1

**CR ID:** CR-SITE-001-WFV2-W3-2026-06-10  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST — `https://sibcar.new-site.space/`  
**Charter:** [SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-WRITE-CHARTER-v1.md](SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-WRITE-CHARTER-v1.md)

---

## Summary

Recompose Used PDP geometry from catalog-like 50/50 hero into commercial showroom layout. Twig offer-column reorder + layout CSS only. No cosmetic pass.

**Baseline:** WF-V2-W2A on TEST.

---

## Changes

| Task | Change |
|------|--------|
| **W3-01** | Hero gallery ~68% · offer column ~32% desktop |
| **W3-02** | Used PDP container max-width 1780px; row padding 28px (scoped) |
| **W3-03** | Offer column DOM: pricing → CTA → specs → discounts |
| **W3-04** | Move characteristics below CTA group in twig |
| **W3-05** | Layer 3 flex column: equipment full-width, then credit full-width |
| **W3-06** | Preserve W2A reading zones; sequential flow enforced |

---

## Files touched

| Remote | Change type |
|--------|-------------|
| `catalog/view/theme/auto/template/product/product.twig` | Offer column DOM reorder + `wfv2-layout-pdp` hook |
| `css/main.css` | WF-V2-W3 layout block append |
| `css/media.css` | WF-V2-W3 responsive layout block append |

**Not modified:** header, footer, PHP, JS, DB.

---

## Risk

| Risk | Severity | Mitigation |
|------|----------|------------|
| Narrow offer column readability | Medium | 2-col specs grid; mobile full-width stack |
| Global container leak | Low | `.used_car_page` scoping only |
| W2A layer3 grid override | Low | W3 block after W2A in cascade |
| Twig nesting regression | Medium | Pre-write backup + marker verify |

---

## Rollback

T1: restore `product.twig`, `main.css`, `media.css` from `pre-wfv2-w3-layout-recomposition-*` + cache clear.

Prior baseline: WF-V2-W2A (`pre-wfv2-w2a-pdp-anatomy-rebuild-20260610-0401`).
