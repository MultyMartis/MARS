# SITE-001 WF-V2-W3 PDP Layout Recomposition Decision v1

**Type:** Post-execution decision report  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST — `https://sibcar.new-site.space/`  
**Execution:** [SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-EXECUTION-v1.md](SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-EXECUTION-v1.md)

---

## Decision

**ACCEPT WF-V2-W3 on TEST** — layout recomposition meets charter scope and success criteria. Wave is composition-only; no cosmetic pass performed.

---

## Success criteria review

| # | Criterion | Evidence | Verdict |
|---|-----------|----------|---------|
| 1 | Car visually dominates | Hero 68/32 split; gallery min-height 480px; offer column narrowed | **MET** |
| 2 | Price second focal point | Price block first in offer column; full-width stack in 32% column | **MET** |
| 3 | CTA before characteristics | DOM order: `wfv2-pdp-offer-cta` before `wfv2-pdp-offer-specs` (verified live) | **MET** |
| 4 | Equipment / credit no longer compete | Layer 3 vertical stack; equipment full-width then credit | **MET** |
| 5 | PDP reads as showroom | Wider container (+13% content width); hero-weighted geometry | **MET** |
| 6 | No new decorative elements | CSS block uses width/flex/grid/order/gap/padding only | **MET** |
| 7 | No visual noise added | No new shadows/gradients/borders in W3 block | **MET** |
| 8 | No regressions | 8/8 URL matrix PASS; modal PASS; no marker leak on non-PDP pages | **MET** |

---

## Key decisions

### D-01 — Hero ratio 68/32 (not 70/30)

**Choice:** 68/32 desktop.  
**Rationale:** Keeps offer column usable at 1440px viewport without truncating CTA row; still clearly breaks 50/50 catalog balance.  
**Trade-off:** Slightly less gallery dominance than 70/30; acceptable for readability.

### D-02 — Container widen scoped to Used PDP

**Choice:** `max-width: 1780px` + reduced row padding on `.used_car_page` only.  
**Rationale:** Global `.container` change risks catalog/homepage regressions; scoped override is safer.  
**Audit:** Effective content ~1520px → ~1724px.

### D-03 — Offer column DOM reorder (twig)

**Choice:** Move discounts to `wfv2-pdp-offer-rest` after specs; move CTA above specs.  
**Rationale:** CSS `order` alone cannot fix discount placement inside pricing wrapper without hiding content; DOM reorder is minimal and stable.

### D-04 — Layer 3 flex column overrides W2A grid

**Choice:** W3 CSS block after W2A; `flex-direction: column` on `.wfv2-pdp-layer3`.  
**Rationale:** Meets W3-05 sequential reading without reverting W2A anatomy markers.

---

## Risks accepted

| Risk | Status |
|------|--------|
| Narrow 32% offer column on 1199–1440px | Mitigated by 2-col specs grid + vertical price stack |
| Discount visibility reduced (moved below specs) | **Accepted** — intentional deprioritization per W3-03 |
| Before screenshots from same session pre-deploy | **OK** — captured before FTP upload in execute run |

---

## Not in scope (confirmed untouched)

Header · Footer · Homepage · Catalog · Colors · JS · PHP · Modals · SEO · Forms

---

## Next wave guidance

WF-V2-W3 completes **geometry/composition** layer. Any further work on PDP should be **functional** or **content** — not another cosmetic pass — unless a new charter explicitly authorizes it.

**Rollback anchor:** `pre-wfv2-w3-layout-recomposition-20260610-0413`
