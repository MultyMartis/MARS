# BZPM Corporate Pages — Program Reconciliation v1

**Program:** BZPM Corporate Pages Program  
**Site:** SITE-002 (ЗПМ / BZPM) · TEST `https://zpm.new-site.space/`  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Date:** 2026-06-22  
**Trigger:** Governance drift identified in [BZPM-CORPORATE-PAGES-FINAL-PHASE-GATE-v1.md](BZPM-CORPORATE-PAGES-FINAL-PHASE-GATE-v1.md) §2 governance drift table

**Boundary:** Documentation reconciliation only. **No** design · **no** wireframes · **no** mockups · **no** implementation · **no** deploy.

**Parent program:** [BZPM-CORPORATE-PAGES-PROGRAM-v1.md](BZPM-CORPORATE-PAGES-PROGRAM-v1.md)

---

## 1. Purpose

Synchronize program index documents with **in-repo artefact reality** after Final Phase Gate audit. Primary drift: program registries claimed **Design Charter not started** while six charter + six brief files already existed under `charters/`.

This pass **does not** constitute operator approval of copy or charters. It corrects **documentation truth** only.

---

## 2. Drift corrected

| Drift | Prior claim | Reconciled truth |
|-------|-------------|------------------|
| Design Charter existence | **Not started** (PROGRAM registry, IA map, Design Program, charters README) | **Draft complete** — six `*-DESIGN-CHARTER-v1.md` files; all **PENDING OPERATOR APPROVAL** |
| Design Brief existence | Not indexed | **Draft complete** — six `*-DESIGN-BRIEF-v1.md` files; M9.14 brief additionally **pending operator approval** |
| Charter folder | «Reserved — not created» (COPY-STANDARDS, charters README) | **Active** — [charters/README.md](charters/README.md) registry |
| Copy phase | **CLOSED / COPY COMPLETE** (program + IA) | **SUBSTANTIVELY COMPLETE** — full PAGE-COPY reproducible; all six headers `Approved by: pending` (blocker **B8** remains) |
| Design Program blocker B6 | «No per-page Design Charter files yet» | «Design Charters not operator-approved» |

**Not resolved by this pass (operator HITL still required):**

- **B6** — Charter operator approval on all six pages  
- **B8** — Copy formal sign-off (`Approved by` fields)  
- **B1** — МО warehouse address conflict  
- **B3** — PLP dealer form vs `/dealers` intake  
- **B9** — IA map operator approval record  

**Visual Design Phase:** remains **NOT OPEN** per Final Phase Gate verdict **NO**.

---

## 3. Files updated (reconciliation pass)

| File | Change |
|------|--------|
| [BZPM-CORPORATE-PAGES-PROGRAM-v1.md](BZPM-CORPORATE-PAGES-PROGRAM-v1.md) | Registry columns Design Charter + Design Brief; substantively complete copy; phase gate links |
| [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](BZPM-CORPORATE-PAGES-IA-MAP-v1.md) | Program phase + phase gate assessment |
| [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md) | Charter/brief registries; B6; readiness notes |
| [charters/README.md](charters/README.md) | Full twelve-file registry |
| [BZPM-COPY-STANDARDS-v1.md](BZPM-COPY-STANDARDS-v1.md) | Storage layout; cross-reference registry |
| [BZPM-PRODUCT-ROADMAP-v1.md](BZPM-PRODUCT-ROADMAP-v1.md) | § Corporate Pages Program |
| [site-passport.md](../../../ocpilot/sites/site-002/site-passport.md) | Corporate Pages section |
| [OCPILOT-STATE.md](../../../ocpilot/OCPILOT-STATE.md) | SITE-002 Corporate Pages row + evidence links |
| **This file** | Reconciliation record |

---

## 4. Per-page status matrix (authoritative post-reconciliation)

| ID | Page | Research | Copy (canonical) | Design Charter | Design Brief |
|----|------|----------|------------------|----------------|--------------|
| **M9.13** | About | **Complete** | v1.1 · COPY REFINEMENT · sign-off pending | v1 · draft complete · pending operator approval | v1 · draft complete |
| **M9.14** | Delivery | **Complete** | v1.1 · COPY REFINEMENT · sign-off pending | v1 · draft complete · pending operator approval | v1 · draft complete · brief pending operator approval |
| **M9.15** | Payment | **Complete** | v1 · COPY COMPLETE · sign-off pending | v1 · draft complete · pending operator approval | v1 · draft complete |
| **M9.16** | Dealers | **Complete** | v1.1 · COPY REFINED · sign-off pending | v1 · draft complete · pending operator approval | v1 · draft complete |
| **M9.17** | Warranty | **Complete** | v1 · COPY COMPLETE · sign-off pending | v1 · draft complete · pending operator approval | v1 · draft complete |
| **M9.18** | Custom | **Complete** | v1.1 · COPY REFINEMENT · sign-off pending | v1 · draft complete · pending operator approval | v1 · draft complete |

---

## 5. Design readiness matrix (program-level)

| Page | Copy ready | Charter ready | Brief ready | Design readiness | Blockers |
|------|------------|---------------|-------------|------------------|----------|
| M9.13 About | PARTIAL (sign-off) | PARTIAL (approval) | READY (draft) | **PARTIAL** | B6, B8, B4 (hero asset) |
| M9.14 Delivery | PARTIAL (sign-off) | PARTIAL (approval) | PARTIAL (brief approval) | **PARTIAL** | B6, B8, B1 (МО address) |
| M9.15 Payment | PARTIAL (sign-off) | PARTIAL (approval) | READY (draft) | **PARTIAL** | B6, B8, OQ deferrals |
| M9.16 Dealers | PARTIAL (sign-off) | PARTIAL (approval) | READY (draft) | **PARTIAL** | B6, B8, B3, B5 |
| M9.17 Warranty | PARTIAL (sign-off) | PARTIAL (approval) | READY (draft) | **PARTIAL** | B6, B8 |
| M9.18 Custom | PARTIAL (sign-off) | PARTIAL (approval) | READY (draft) | **PARTIAL** | B6, B8, B5 |

**Program design readiness:** **PARTIAL** — documentation stack sufficient for **operator charter review**; **insufficient** for program-wide Visual Design Phase **OPEN**.

---

## 6. Final program status (post-reconciliation)

| Phase | Status |
|-------|--------|
| Research | **COMPLETE** |
| IA / Architecture | **READY** (operator approval record pending — B9) |
| Copy system | **CLOSED** |
| Copy content | **SUBSTANTIVELY COMPLETE** (formal sign-off pending — B8) |
| Design Charter | **DRAFT COMPLETE / APPROVAL OPEN** |
| Design Brief | **DRAFT COMPLETE** |
| Visual Design | **NOT OPEN** |
| Implementation | **NOT READY** |

---

## 7. Recommended next step (unchanged from Final Phase Gate)

1. Operator HITL — approve canonical PAGE-COPY; update `Approved by` fields (**B8**).  
2. Operator decision — lock **B1** МО address.  
3. Operator decision — lock **B3** PLP vs corp dealer intake.  
4. Approve **M9.13 Design Charter v1** — first visual design authorization (**B6**).  
5. Conditional open: Visual Design Phase **for M9.13 only** after B8 + M9.13 charter approval.

**Explicit stop:** No wireframes · no mockups · no implementation.

---

## 8. Change log

| Date | Change |
|------|--------|
| 2026-06-22 | **CREATED** — Program reconciliation v1; drift table; per-page matrix; design readiness; registry sync record |

---

*BZPM Corporate Pages Program Reconciliation v1 — documentation only.*
