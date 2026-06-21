# SITE-001 WF-V2-W2A PDP Anatomy Rebuild Change Request v1

**CR ID:** CR-SITE-001-WFV2-W2A-2026-06-10  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST — `https://sibcar.new-site.space/`  
**Charter:** [SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-WRITE-CHARTER-v1.md](SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-WRITE-CHARTER-v1.md)

---

## Summary

Rebuild Used PDP DOM anatomy per composition audit C-01, C-03, C-08, C-09, C-10, C-11. Twig restructuring + layout CSS only. No cosmetic pass. No header/catalog/homepage scope.

**Baseline:** WF-V2-W1 + WF-V2-W2 + WF-V2-W2S on TEST.

---

## Changes

| Task | Change |
|------|--------|
| **A / C-01** | Move H1 into commercial stage identity row; remove `w4-1-pdp-top` title band; eliminate mobile `page_title` duplicate |
| **B / C-03** | Commercial stage: Identity (H1+Status) → Hero Split (Gallery+Offer) → Trust Line |
| **C / C-08** | Relocate `lcd_display.product` below Equipment+Credit+Reviews |
| **D / C-09** | New `wfv2-pdp-layer3` grid: Equipment 60% · Credit 40% desktop |
| **E / C-10** | Reviews block after layer 3 |
| **F / C-11** | Remove `used_car__credit__slider` car image from credit panel |

---

## Files touched

| Remote | Change type |
|--------|-------------|
| `catalog/view/theme/auto/template/product/product.twig` | DOM reorder + `wfv2-anatomy-pdp` hook |
| `css/main.css` | WF-V2-W2A layout block append |
| `css/media.css` | WF-V2-W2A responsive layout block append |

**Not modified:** `header.twig` (backup only), PHP, JS, DB.

---

## Risk

| Risk | Severity | Mitigation |
|------|----------|------------|
| Twig nesting regression | Medium | Pre-write backup + 8-URL marker verify |
| Mobile title regression | Medium | Single H1 + anatomy CSS |
| Credit calculator layout without image column | Low | Grid reflow in layer3 credit column |
| `lcd_display` still visible mid-page | Low | DOM move below fold |

---

## Rollback

T1: restore `product.twig`, `main.css`, `media.css` from `pre-wfv2-w2a-pdp-anatomy-rebuild-*` + cache clear.

Prior baseline: WF-V2-W2S (`pre-wfv2-w2s-pdp-clean-20260610-0330`).

---

## Authorization

| Action | Status |
|--------|--------|
| Execute on TEST | **AUTHORIZED** (operator mandate 2026-06-10) |
| Commit / push | **NOT AUTHORIZED** |
| Production | **NOT AUTHORIZED** |

*CR-SITE-001-WFV2-W2A-2026-06-10*
