# REPORT — M9.8.9 MINOR FIXES PACK #1 REGISTRATION

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Task:** Register M9.8.9 Minor Fixes Pack #1 as next active work package  
**Execution date:** 2026-06-19  
**Mode:** Documentation / roadmap registration only — **no** deploy · **no** FTP · **no** live file edits · **no** implementation

---

## 1. Documents updated

| File | Change |
|------|--------|
| [README.md](../README.md) | Active stage → M9.8.9; open bugs; next planned M9.8.9-06 |
| [site-passport.md](../site-passport.md) | Active stage, deferred M9.8 remainder, registration link |
| [OCPILOT-STATE.md](../../../OCPILOT-STATE.md) | SITE-002 focus, active stage, open bugs, registration evidence |
| [OPERATIONAL-INDEX.md](../../../OPERATIONAL-INDEX.md) | Run **4.141** + deliverables summary |
| [BZPM-PRODUCT-ROADMAP-v1.md](../../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md) | § M9.8.9 pack; M9.8 completion status; open bugs; change log |
| [SITE-002-M9.8.9-MINOR-FIXES-PACK-01-REGISTRATION.md](SITE-002-M9.8.9-MINOR-FIXES-PACK-01-REGISTRATION.md) | This report |

**Authority unchanged:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` — registration does not create a new baseline checkpoint.

---

## 2. Registered work package

**M9.8.9 — Большой пакет мелких доработок #1**

| ID | Task | Status | Risk | Gate |
|----|------|--------|------|------|
| **M9.8.9-01** | Wishlist / Compare Smart Tooltips | PLANNED | MEDIUM | — |
| **M9.8.9-02** | Megamenu Redesign / Overlay-Safe Audit | PLANNED / AUDIT FIRST | HIGH | Overlay audit |
| **M9.8.9-03** | Combined Certificates + Dealers Section | PLANNED / DESIGN FIRST | MEDIUM | Design |
| **M9.8.9-04** | Filter Scroll Offset Fix | PLANNED | MEDIUM | Depends M9.8.9-06 |
| **M9.8.9-05** | Footer Redesign | PLANNED / DESIGN FIRST | MEDIUM-HIGH | Design |
| **M9.8.9-06** | Filter Bug Investigation and Fix | **ACTIVE NEXT** / AUDIT FIRST | HIGH | Audit + approval |
| **M9.8.9-07** | Remove «Подкатегории» from Filter Sidebar | PLANNED | LOW-MEDIUM | — |
| **M9.8.9-08** | Per-Filter-Group Reset Button | PLANNED | MEDIUM | — |

---

## 3. Task scope summary

### M9.8.9-01 — Wishlist / Compare Smart Tooltips

Smart hover `title`/tooltips for wishlist and compare buttons:

- Add to wishlist / Remove from wishlist
- Add to compare / Remove from compare

**Must not break:** `.active` state; action tips «Добавлено / Удалено»; «Артикул скопирован» copy tip. Only one action tip visible at a time.

### M9.8.9-02 — Megamenu Redesign / Overlay-Safe Audit

Target: `#zpmCatalog`. Redesign catalog sections area. Audit and document overlay system rules (mega menu, mobile menu, search, cart dropdown, catalog filter overlay). Do not break existing overlay system.

### M9.8.9-03 — Combined Certificates + Dealers Section

Combine existing `<section class="certificates">` and `<section class="zpm-dealers">` into new Twig template. Desktop: certificates + short commercial text + dealer form in one compact screen. Do not remove old templates.

### M9.8.9-04 — Filter Scroll Offset Fix

After filter apply/update: scroll to `<section class="category">` with proper offset (same principle as PDP scroll offset, adapted for category page). **Depends on M9.8.9-06.**

### M9.8.9-05 — Footer Redesign

Serious footer redesign without rebuilding site from scratch.

### M9.8.9-06 — Filter Bug Investigation and Fix

**Critical bugs (operator-reported):**

- Filter does not work on category «Столы»
- Filter works on «Моечные ванны»
- Price slider: right handle moves left handle

**Workflow:** confirm bug → find cause → compare working vs broken category → prepare fix → **implement only after approval**.

### M9.8.9-07 — Remove «Подкатегории» Group from Filter Sidebar

Remove «Подкатегории» group from category filter sidebar only. Keep top subcategory chips above products.

### M9.8.9-08 — Per-Filter-Group Reset Button

Inside each `.flt__group-body`: local reset button that clears only that group's selections. Must not reset entire filter.

---

## 4. Priority order

| Order | ID | Rationale |
|------:|-----|-----------|
| **1** | **M9.8.9-06** | **ACTIVE NEXT** — critical filter failure + price slider bug; blocks scroll-offset fix |
| 2 | M9.8.9-07 | Low-medium risk; filter sidebar cleanup on related surface |
| 3 | M9.8.9-04 | Depends on M9.8.9-06 investigation outcome |
| 4 | M9.8.9-08 | Self-contained filter UX improvement |
| 5 | M9.8.9-01 | Medium risk; must preserve existing tip/action stack |
| 6 | M9.8.9-02 | High risk — overlay audit required before any megamenu change |
| 7 | M9.8.9-03 | Design-first; new combined template only |
| 8 | M9.8.9-05 | Design-first; broader layout scope |

**Next recommended task:** **M9.8.9-06** — Filter Bug Investigation and Fix (audit-first; no implementation without approval).

---

## 5. Risks

| Risk | Tasks | Mitigation |
|------|-------|------------|
| **HIGH** | M9.8.9-02, M9.8.9-06 | Audit-first gates; overlay rules doc before megamenu; category comparison before filter fix |
| **MEDIUM-HIGH** | M9.8.9-05 | Design-first; scope boundary — footer only, no full rebuild |
| **MEDIUM** | M9.8.9-01, 03, 04, 08 | Preserve existing behaviors; design approval; depend on M9.8.9-06 for scroll fix |
| **LOW-MEDIUM** | M9.8.9-07 | Sidebar-only change; do not touch top chips |

**Cross-cutting:** MANUAL UI / CSS / TWIG on live TEST remain canonical. Any implementation must live-capture scoped files before deploy.

**Deferred (not in M9.8.9):** M9.8.3 · M9.8.4 · M9.8.6 · M9.8.7 (EC-01) · M9.8.8 — remain on roadmap backlog.

---

## 6. Open bugs registry (updated)

| ID | Surface | Category | Issue |
|----|---------|----------|-------|
| EC-01 | Filter sidebar «Подкатегории» | 80 Моечные ванны | Empty subcategories still shown (M9.8.7) |
| M9.8.9-06 | Filter + price slider | «Столы» vs «Моечные ванны» | Filter broken on «Столы»; price slider handle coupling |

---

## 7. Implementation authorization

| Action | Authorized |
|--------|------------|
| Roadmap / OCPilot registration | **YES** (this task) |
| M9.8.9-06 live audit | **Next** — charter/approval for audit-only pass |
| M9.8.9 implementation (any) | **NO** — not authorized by this registration |
| Deploy / FTP / live edits | **NO** |

---

## 8. Git

| Item | Value |
|------|-------|
| Commit | **YES** — `Register SITE-002 M9.8.9 minor fixes pack 01` |
| Push | **YES** (per task charter) |
| Deploy | **NO** |
| FTP | **NO** |

---

*Registration complete — documentation only. No site modification.*
