# BZPM Product Roadmap v1

**Program:** Website Factory  
**Execution case:** BZPM  
**Document role:** Canonical planning document for future BZPM work  
**Status:** Post M9.8.9 Catalog UX Complete 01 — **M9.8.9 Minor Fixes Pack #1** active · **Corporate Pages Program** open — Research **COMPLETE** · IA **READY**  
**Date:** 2026-06-22 (Corporate Pages Program — Research → IA phase gate)  
**Authority:** Repository evidence + SITE-002 TEST checkpoint `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI` + operator feedback (Алексей)

**Boundary:** Documentation and planning only. This roadmap does **not** authorize implementation, OpenCart changes, UX changes, or code work.

**Related execution cases (distinct scopes):**

| Case folder | Scope | Relationship to this roadmap |
| --- | --- | --- |
| `bzpm-market-intelligence/` | W1–W3Y market intelligence | Input — MI foundation complete; informs M13 |
| `bzpm-catalog-redesign/` | W0–W4 catalog audit & redesign research (2026-06-08) | Input — audit findings and strategy themes; separate decision log (D-01…R-05) |
| `bzpm-roadmap/` | Product planning & milestone sequencing | **This document** — canonical forward plan |

---

# Executive Summary

BZPM (ORG-0005 ЗПМ · PRJ-0009 Каталог-платформа bzpm.ru) has completed **Market Intelligence Foundation** (W1–W3Y) and **Presentation Pack** packaging. A formal product roadmap did **not** exist in the repository before this document.

**This roadmap v1 establishes:**

1. **Ten approved strategic decisions** (ROAD-001…ROAD-010) from post-W3Y planning — preserved outside chat history.
2. **Thirteen milestones** (M1–M13) in required execution order — from completed MI through Catalog UX Intelligence Program.
3. **Prioritized backlog** (HIGH / MEDIUM / LOW) derived from approved decisions.
4. **Decision log** with ID, date, source, and status for every roadmap item.

**Immediate forward path (documentation gates first):**

- Complete **M3 Roadmap Formalization** (this deliverable).
- Execute **M4 Git Checkpoint** and **M5 Backup Milestone** before catalog implementation waves.
- Run **M6 Catalog Architecture Audit**, then **M7 Launch Mode** and **M8 TEST Cleanup** as launch prerequisites.
- Filter-system work (**M9–M11**) follows launch-mode stabilization.
- **M12 Catalog View #3** and **M13 Catalog UX Intelligence Program** are downstream — blocked until Presentation Pack + Roadmap + Backup are complete.

**Not in scope of this roadmap:** W4 Competitor Intelligence (MI program continuation), OpenCart/OCPilot delivery, or automatic promotion of catalog-redesign mockups to implementation.

---

# Current State

## Program position

| Dimension | State | Evidence |
| --- | --- | --- |
| **Market Intelligence** | W1–W3Y **complete and approved** | `BZPM-MARKET-INTELLIGENCE-MASTER-REPORT-v1.md`; `BZPM-OPERATOR-INSIGHTS-v1.md` |
| **Registry** | 126 canonical entities; 46 approved | `BZPM-COMPETITOR-REGISTRY-v2.md` |
| **Presentation Pack** | Excel packaging **complete** (2026-06-14) | `presentation-pack/EXPORT-REPORT.md` — operator distribution / executive review may continue |
| **Product roadmap** | **Created** by this document | `bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md` |
| **Catalog redesign research** | W0–W4 documentation complete (2026-06-08) | `bzpm-catalog-redesign/` — strategy approved; implementation not chartered |
| **Live audit environment** | `https://zpm.new-site.space/` (SITE-002 TEST) | OCPilot delivery — **authority** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`; **MANUAL UI REFINEMENTS ARE CANONICAL** |
| **Production** | `https://bzpm.ru/` (WEB-ZPM-01) | ATLAS / catalog-redesign README |
| **OCPilot delivery (SITE-002)** | M7.1–M9.8.9 catalog cluster **complete** on TEST; **Corporate Pages Program** **OPEN** — Research **COMPLETE** · IA **READY** | Active: remaining M9.8.9 tasks; corp pages design charter; M10 **not authorized** |

## What is known

- BZPM ≠ SITE-001 (SIBCAR); OCPilot OpenCart workflows do **not** apply (D-06, R-04).
- Website Factory = primary delivery lane for BZPM catalog work.
- Native Benchmark Group captured in W3Y: УЗНМ, КЛЕН, Unitorg, Trapeza, Kobor, Комплекс Трейд.
- Operator-derived investigation markers (FIM-W3Y-001…007) exist for filter UX, dual-column listings, view switchers, information density.

## SAFE UNKNOWN

| Topic | Notes |
| --- | --- |
| Production CMS / stack (PRJ-0009) | Not documented in MARS repo |
| Operator Manual Review Notes (2026-06-14) | Cited in W3Y authority; **not committed in-repo** |
| BZPM MI Methodology v1 / W1 Market Mapping Report | Not found in-repo |
| Exact TEST artifact inventory on staging/production | Requires M6/M8 audit |
| Parent category population beyond Neutral Equipment | Launch Mode (ROAD-001) addresses visual behavior until populated |

---

# Market Intelligence Status

## Completed waves

| Wave | Name | Status | Primary artifact |
| --- | --- | --- | --- |
| W1 | Market Mapping | Approved | Referenced in Master Report §8; full W1 report **SAFE UNKNOWN** in-repo |
| W2 | Competitor Discovery | Approved | 80-candidate universe |
| W2.5 | Competitor Prioritization | Approved | Core Research Set — 46 entities |
| W3 | Competitor Registry | Approved | COMP-BZPM-001…046 |
| W3R | Regional Reinforcement | Approved | 38 regional rows |
| W3S | SERP Visibility Expansion | Approved | 27 new SERP domains |
| W3X | Registry Consolidation | Approved | `BZPM-COMPETITOR-REGISTRY-v2.md` + Master Report v1 |
| W3Y | Operator Insight Capture | Approved | `BZPM-OPERATOR-INSIGHTS-v1.md` |

## Presentation Pack (M2)

| Deliverable | Status |
| --- | --- |
| `BZPM-MI-DASHBOARD.xlsx` | Generated |
| `BZPM-COMPETITOR-REGISTRY.xlsx` | Generated |
| `BZPM-CORE-RESEARCH-SET.xlsx` | Generated |
| `BZPM-OPERATOR-INSIGHTS.xlsx` | Generated |
| `BZPM-MANUAL-REVIEW-CHECKLIST.xlsx` | Generated |
| `BZPM-MI-PACKAGE-SUMMARY.xlsx` | Generated |

**Packaging status:** Complete per `EXPORT-REPORT.md` (2026-06-14). Milestone M2 remains **in progress** until operator confirms executive review / archive handoff complete.

## MI program items not blocking this product roadmap

- W4 Competitor Intelligence — prerequisite operator capture fulfilled by W3Y; deep intelligence **deferred** to M13 track.
- 13 Review Required tier flags within approved registry.
- Expansion queue triage (21 Strong + 22 Possible candidates).
- Optional registry expansion wave (COMP-BZPM-047+).

---

# Approved Strategic Decisions

Decisions ROAD-001…ROAD-010 are **approved** for BZPM product planning. They supersede informal chat-only agreement and are independent of the 2026-06-08 catalog-redesign decision log (D-01…R-05).

## ROAD-001 — Launch Mode: Neutral Equipment Only

**Decision:** Site launch must visually operate as **Catalog = Neutral Equipment** until other parent categories are populated.

**Implication:** Navigation, catalog root, and category landing behavior present Neutral Equipment as the effective primary catalog scope. Empty or stub parent categories must not appear as peer launch surfaces.

**Milestone:** M7

---

## ROAD-002 — TEST Cleanup

**Decision:** Remove **test products**, **test attributes**, and **test filters** from all user-facing surfaces.

**Implication:** Staging and production user-visible catalog, filters, PDP, and search must not expose TEST nomenclature or placeholder attribute/filter definitions.

**Milestone:** M8

---

## ROAD-003 — Filter Profile System

**Decision:** Support **category-level filter profiles**.

**Implication:** Each category (or category family) can define which filters apply, their order, and visibility rules — not a single global filter panel for all catalog branches.

**Milestone:** M9

---

## ROAD-004 — Subcategory Filter Profiles

**Decision:** Support **category overrides** at subcategory level.

**Example:** Neutral Equipment → Washing Baths may use a different filter profile than Neutral Equipment → Undercounter Stands.

**Implication:** Filter profile inheritance: parent profile as default; subcategory may override or extend.

**Milestone:** M9 (foundation) · refined in M11

---

## ROAD-005 — Dynamic Filter Visibility

**Decision:** Hide **empty filters**, **unused filters**, and **irrelevant filters** dynamically based on category context and available product data.

**Implication:** Filter panel shows only filters with meaningful selection value for the current category/subcategory result set.

**Milestone:** M10

---

## ROAD-006 — Filter Groups

**Decision:** Introduce **grouped filters** with named sections.

**Example groups:**

- Price & Availability
- Dimensions
- Construction
- Materials
- Additional Parameters

**Implication:** Filter UI uses semantic grouping; group membership is profile-configurable per ROAD-003/004.

**Milestone:** M11

---

## ROAD-007 — Primary vs Secondary Filters

**Decision:** Support **Primary Filters** (always visible / above fold in filter panel) and **Additional Filters** (expandable or secondary panel).

**Implication:** Category profiles assign filter priority tier; aligns with УЗНМ simplified-filter benchmark observation (FIM-W3Y-001).

**Milestone:** M11

---

## ROAD-008 — Native Benchmark Group

**Decision:** Record as ongoing catalog UX references:

| Company | URL | Registry ID |
| --- | --- | --- |
| УЗНМ | https://zavod-uznm.ru/ | COMP-BZPM-007 |
| КЛЕН | https://www.klenmarket.ru/ | COMP-BZPM-012 |
| ГК Юниторг | https://www.unitorg.ru/ | CAN-EXP-005 |
| Trapeza | https://www.trapeza.ru/ | COMP-BZPM-011 |
| Kobor | https://kobor.ru/ | CAN-EXP-003 |
| Комплекс Трейд | https://kompleks-trade.ru/ | CAN-EXP-004 |

**Implication:** Benchmark group is a **reference set** for catalog UX intelligence — not a blueprint for direct copy (cf. catalog-redesign D-03: Trapeza = reference, not blueprint).

**Milestone:** Ongoing input to M11, M12, M13

---

## ROAD-009 — Catalog View #3

**Decision:** Investigate **Unitorg-style dual-column listing layout** as a candidate catalog view mode.

**Implication:** Research and specification only in M12; implementation decision deferred until M6 architecture audit and M9–M11 filter foundation are understood.

**Evidence link:** FIM-W3Y-002; W3Y dual-column catalog card observation on CAN-EXP-005.

**Milestone:** M12

---

## ROAD-010 — Catalog UX Intelligence Program

**Decision:** Planned **after** all of the following are complete:

1. Presentation Pack (M2)
2. Roadmap Update (M3)
3. Backup Milestone (M5)

**Implication:** Structured competitor-informed catalog UX research program — distinct from completed MI waves W1–W3Y and distinct from 2026-06-08 catalog-redesign audit pack. Uses Native Benchmark Group and operator insights as inputs.

**Milestone:** M13

---

# Active Priorities

Ordered by milestone sequence and launch criticality.

| Priority | Item | Milestone | Decision |
| --- | --- | --- | --- |
| 1 | Roadmap formalization | M3 | — |
| 2 | Git checkpoint | M4 | Survivability gate |
| 3 | Backup milestone | M5 | Survivability gate |
| 4 | Catalog architecture audit | M6 | Prerequisite for filter + launch work |
| 5 | Launch Mode — Neutral Equipment Only | M7 | ROAD-001 |
| 6 | TEST cleanup | M8 | ROAD-002 |
| 7 | Filter profile system (incl. subcategory overrides) | M9 | ROAD-003, ROAD-004 |
| 8 | Presentation Pack executive closeout | M2 | Operator handoff |

---

# Future Priorities

| Item | Milestone | Decision | Prerequisite |
| --- | --- | --- | --- |
| Dynamic filter visibility | M10 | ROAD-005 | M9 |
| Filter UX improvements (groups + primary/secondary) | M11 | ROAD-006, ROAD-007 | M9, M10 |
| Catalog View #3 investigation | M12 | ROAD-009 | M6; M9–M11 context |
| Catalog UX Intelligence Program | M13 | ROAD-010 | M2 + M3 + M5 |
| Native benchmark monitoring | Ongoing | ROAD-008 | W3Y artifacts |
| W4 Competitor Intelligence (MI program) | MI track | Master Report §9 | Operator expansion triage |
| Registry expansion (COMP-BZPM-047+) | MI track | Master Report §9 | Operator approval |

---

# Deferred Work

| Item | Reason | Revisit trigger |
| --- | --- | --- |
| **W1E Product Taxonomy Audit** | Deferred 2026-06-08 (D-01) — insufficient ROI at redesign phase | Operator charter or nomenclature-blocking launch issue |
| **Full nomenclature decoding** | Rejected current-phase deliverable (D-02, R-02) | New market evidence requiring OEM legend pages |
| **Large-scale catalog restructuring** | Premature before strategy formalization (R-03) | M6 audit + ROAD-001 launch validation |
| **OCPilot / OpenCart workflows** | BZPM ≠ SITE-001 (R-04) | New evidence PRJ-0009 runs OpenCart |
| **Direct Trapeza blueprint copy** | Different business model (R-01, D-03) | Never — reference only |
| **Catalog View #3 implementation** | Investigation only until M12 completes | M12 specification approval |
| **Catalog UX Intelligence Program execution** | ROAD-010 sequencing gate | M2 + M3 + M5 complete |
| **13 Review Required MI tier flags** | Non-blocking for product roadmap | MI operator review cycle |
| **Expansion queue triage (43 candidates)** | Awaiting operator decisions | MI W4+ or M13 intake |

---

# Risks

| ID | Risk | Severity | Mitigation |
| --- | --- | --- | --- |
| RSK-01 | **Strategic decisions existed only in chat** before this roadmap | High | ROAD-001…010 formalized here; decision log below |
| RSK-02 | **Operator Manual Review Notes not in-repo** | Medium | W3Y capture in `BZPM-OPERATOR-INSIGHTS-v1.md`; operator may append W3Y.1 |
| RSK-03 | **TEST data on user-facing surfaces** | High | M8 TEST Cleanup (ROAD-002) before launch |
| RSK-04 | **Empty parent categories at launch** | High | M7 Launch Mode (ROAD-001) |
| RSK-05 | **Production stack SAFE UNKNOWN** | Medium | M6 Catalog Architecture Audit must document actual CMS/filter stack |
| RSK-06 | **Parallel documentation tracks** (catalog-redesign 2026-06-08 vs MI 2026-06-14 vs this roadmap) | Medium | Cross-reference allowed; this roadmap = canonical **forward** plan |
| RSK-07 | **Filter complexity scope creep** | Medium | Sequence M9 → M10 → M11; profile system before UX polish |
| RSK-08 | **Benchmark conflation with blueprint** | Medium | ROAD-008 reference-only; D-03 preserved |
| RSK-09 | **MI W4 vs M13 Catalog UX Intelligence overlap** | Low | W4 = competitor intelligence; M13 = catalog UX program — separate charters |
| RSK-10 | **No git checkpoint before implementation waves** | High | M4 required before M6+ implementation planning |

---

# Milestones

Required sequence. Status as of roadmap v1 creation (2026-06-14).

| ID | Name | Status | Description | Key outputs / gates |
| --- | --- | --- | --- | --- |
| **M1** | Market Intelligence Foundation | **Completed** | W1, W2, W2.5, W3, W3R, W3S, W3X, W3Y | Registry v2; Master Report v1; Operator Insights v1 |
| **M2** | Presentation Pack | **In progress** | Excel packaging and executive review layer | 6 workbooks; README; EXPORT-REPORT — packaging complete; operator handoff TBD |
| **M3** | Roadmap Formalization | **Completed** | Canonical product roadmap | This document |
| **M4** | Git Checkpoint | **Planned** | Repository survivability checkpoint before implementation waves | Human git checkpoint per MARS git-rules |
| **M5** | Backup Milestone | **Planned** | Backup / restore baseline before catalog implementation | ATLAS backup procedure reference; operator-verified snapshot |
| **M6** | Catalog Architecture Audit | **Planned** | Document live catalog architecture: categories, attributes, filters, TEST inventory, stack | Audit report; input to M7–M11 |
| **M7** | Launch Mode | **Planned** | Neutral Equipment Only launch behavior | ROAD-001 implementation charter |
| **M8** | TEST Cleanup | **Planned** | Remove test products, attributes, filters from user-facing surfaces | ROAD-002 verification checklist |
| **M9** | Filter Profile System | **Planned** | Category-level and subcategory override filter profiles | ROAD-003, ROAD-004 |
| **M10** | Dynamic Filter Visibility | **Planned** | Hide empty / unused / irrelevant filters | ROAD-005 |
| **M11** | Filter UX Improvements | **Planned** | Filter groups + primary vs secondary filters | ROAD-006, ROAD-007 |
| **M12** | Catalog View #3 | **Planned** | Investigate Unitorg-style dual-column listing layout | ROAD-009 research spec |
| **M13** | Catalog UX Intelligence Program | **Planned** | Structured catalog UX intelligence using benchmark group + MI artifacts | ROAD-010 program charter |

### Milestone dependency chain

```
M1 (done) → M2 (in progress) → M3 (done) → M4 → M5
                                              ↓
                                    M6 → M7 → M8 → M9 → M10 → M11 → M12 → M13
```

**ROAD-010 gate:** M13 may not start until **M2 + M3 + M5** are complete. M3 is satisfied by this document.

---

# OCPilot Delivery Track — SITE-002 (TEST)

Delivery lane for BZPM catalog on OpenCart TEST (`zpm.new-site.space`). Distinct from MI milestones M1–M3; execution evidence under `projects/ocpilot/sites/site-002/`.

## Authority

| Rule | Value |
| --- | --- |
| **Checkpoint** | `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` |
| **MANUAL UI REFINEMENTS ARE CANONICAL** | Operator manual CSS, Twig, UX edits on live TEST override older M9.x deploy snapshots |
| **Conflict resolution** | If M9.x documentation contradicts current TEST → source of truth = live TEST on `zpm.new-site.space` |

## Completed (TEST)

| Phase | Name | Status | Evidence |
| --- | --- | --- | --- |
| M7.1 | Launch Mode | **Complete** | `SITE-002-M7.1-LAUNCH-MODE-IMPLEMENTATION.md` |
| M8 | TEST Cleanup (Wave 1 + 2) | **Complete** | `SITE-002-M8.3-WAVE1-TEST-CLEANUP.md` · `SITE-002-M8.3-WAVE2-TEST-CLEANUP.md` |
| M9 | Filter Profile System (301/80/322/207/326) | **Complete** | `SITE-002-STABLE-M9-COMPLETE.md` |
| M9.5 | Root Hub Mode (cat 79) | **Complete** | `SITE-002-M9.5-ROOT-HUB-IMPLEMENTATION.md` |
| M9.7 | Category Images + Megamenu Cleanup | **Complete** | `REPORT-BZPM-M9.7C-IMAGE-DEPLOY-MEGAMENU-CLEANUP.md` |
| — | Homepage Neutral Branches | **Complete** | `REPORT-BZPM-HOMEPAGE-CATEGORY-SECTION-NEUTRAL-BRANCHES.md` |
| — | Manual UI Refinement | **Complete** | `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI.md` |

## Active stage — M9.8 UX Polish Pack

**Status:** Partially complete on TEST (M9.8.1 · M9.8.2 · M9.8.5 + operator manual PLP polish). Remaining M9.8 items **deferred** — superseded for active work by **M9.8.9** (2026-06-19).

**Basis:** Operator feedback (Алексей) + EC-01 from [REPORT-BZPM-EMPTY-CATEGORY-FINAL-AUDIT.md](../../../ocpilot/sites/site-002/reports/REPORT-BZPM-EMPTY-CATEGORY-FINAL-AUDIT.md).  
**Mode:** Research and task preparation unless explicitly chartered for implementation. **No implementation authorized** by this roadmap section alone.

| ID | Task | Type | Status | Basis | Scope |
| --- | --- | --- | --- | --- | --- |
| **M9.8.1** | PDP Gallery Compact | Research | **Complete** (TEST) | Алексей — PDP page | Thumbnails below main image; reduced whitespace; more useful PDP area |
| **M9.8.2** | PDP Lightbox Constraints | Research | **Complete** (TEST) | Алексей — lightbox UX | Constrained lightbox viewport; no fullscreen scale |
| **M9.8.3** | Homepage Hero Compression | Research | **Deferred** | Алексей — homepage | Reduce hero height; show first category row without clipping |
| **M9.8.4** | PLP Density Optimization | Research | **Deferred** (partial via manual polish) | Алексей — catalog list | Lower card height; reduce vertical gaps; increase catalog density |
| **M9.8.5** | Products Per Page Selector | Task prep | **Complete** (TEST) | Алексей — PLP pagination | Selector options: **10 / 20 / 50 / 100** products per page |
| **M9.8.6** | UltraWide Catalog Layout | Research | **Deferred** | Operator discussion | Two list-view cards per row on wide screens |
| **M9.8.7** | EC-01 Filter Cleanup | **Bug fix** (charter required) | **Open** | Empty-category audit | Branch **80 Моечные ванны** — filter sidebar: hide subcategories with no active products |
| **M9.8.8** | PDP Thumbnail Rail Research | Research only | **Deferred** | UX pattern study | Vertical compact thumbnail rail (Alibaba-style); no implementation |

## Active stage — M9.8.9 Minor Fixes Pack #1

**Registered:** 2026-06-19  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Registration report:** [SITE-002-M9.8.9-MINOR-FIXES-PACK-01-REGISTRATION.md](../../../ocpilot/sites/site-002/reports/SITE-002-M9.8.9-MINOR-FIXES-PACK-01-REGISTRATION.md)  
**Mode:** Documentation registration only — **no implementation authorized** by this section alone.

| ID | Task | Status | Risk | Gate | Scope |
| --- | --- | --- | --- | --- | --- |
| **M9.8.9-01** | Wishlist / Compare Smart Tooltips | PLANNED | MEDIUM | — | Hover `title`/tooltips: Add/Remove wishlist; Add/Remove compare. Must not break `.active`, action tips «Добавлено/Удалено», «Артикул скопирован». Only one action tip visible at a time. |
| **M9.8.9-02** | Megamenu Redesign / Overlay-Safe Audit | PLANNED / AUDIT FIRST | HIGH | Audit | Target `#zpmCatalog` — redesign catalog sections area. Audit overlay rules: mega menu, mobile menu, search, cart dropdown, catalog filter overlay. Do not break overlay system. |
| **M9.8.9-03** | Combined Certificates + Dealers Section | PLANNED / DESIGN FIRST | MEDIUM | Design | New combined Twig from `<section class="certificates">` + `<section class="zpm-dealers">`. Desktop: certificates + short commercial text + dealer form in one compact screen. Do not remove old templates. |
| **M9.8.9-04** | Filter Scroll Offset Fix | PLANNED | MEDIUM | — | After filter apply: scroll to `<section class="category">` with proper offset (PDP scroll-offset principle). Depends on **M9.8.9-06**. |
| **M9.8.9-05** | Footer Redesign | PLANNED / DESIGN FIRST | MEDIUM-HIGH | Design | Serious footer redesign without full site rebuild. |
| **M9.8.9-06** | Filter Bug Investigation and Fix | **ACTIVE NEXT** / AUDIT FIRST | HIGH | Audit + approval | Filter broken on «Столы»; works on «Моечные ванны». Price slider: right handle moves left handle. Confirm → find cause → compare categories → prepare fix → implement only after approval. |
| **M9.8.9-07** | Remove «Подкатегории» from Filter Sidebar | PLANNED | LOW-MEDIUM | — | Remove «Подкатегории» group from filter sidebar only. Keep top subcategory chips above products. |
| **M9.8.9-08** | Per-Filter-Group Reset Button | PLANNED | MEDIUM | — | Local reset inside each `.flt__group-body`; resets only that group's selections; must not reset entire filter. |

### M9.8.9 recommended sequence

| Priority | ID | Rationale |
| --- | --- | --- |
| 1 | **M9.8.9-06** Filter Bug Investigation | **ACTIVE NEXT** — critical filter failure on «Столы» + price slider bug; blocks M9.8.9-04 |
| 2 | **M9.8.9-07** Remove «Подкатегории» sidebar group | Low-medium risk; filter UX cleanup; related surface |
| 3 | **M9.8.9-04** Filter Scroll Offset Fix | Depends on M9.8.9-06 root-cause clarity |
| 4 | **M9.8.9-08** Per-group reset | Self-contained filter UX improvement |
| 5 | **M9.8.9-01** Wishlist / Compare tooltips | Medium risk; must preserve existing tip stack |
| 6 | **M9.8.9-02** Megamenu redesign | High risk — overlay audit required first |
| 7 | **M9.8.9-03** Certificates + Dealers | Design-first; new template only |
| 8 | **M9.8.9-05** Footer redesign | Design-first; medium-high scope |

### Open bugs (post M9.7D)

| ID | Surface | Branch / category | Issue |
| --- | --- | --- | --- |
| **EC-01** | Filter sidebar «Подкатегории» | 80 Моечные ванны | Subcategories with 0 active products still shown (M9.8.7) |
| **M9.8.9-06** | Category filter + price slider | «Столы» (broken) vs «Моечные ванны» (works) | Filter does not work on «Столы»; price slider right handle moves left handle — audit first |

**M10** (dynamic filter visibility per ROAD-005) remains **not authorized**.

---

## Corporate Pages Program

**Registered:** 2026-06-22  
**Status:** **OPEN** — Research **COMPLETE** · IA / Architecture **READY** · Copy system **REGISTERED**  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Program doc:** [BZPM-CORPORATE-PAGES-PROGRAM-v1.md](BZPM-CORPORATE-PAGES-PROGRAM-v1.md)  
**IA map:** [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](BZPM-CORPORATE-PAGES-IA-MAP-v1.md)  
**Copy standard:** [BZPM-COPY-STANDARDS-v1.md](BZPM-COPY-STANDARDS-v1.md)  
**Registration report:** [REPORT-BZPM-CORPORATE-PAGES-PROGRAM-REGISTRATION.md](../../../ocpilot/sites/site-002/reports/REPORT-BZPM-CORPORATE-PAGES-PROGRAM-REGISTRATION.md) · [Copy system report](../../../ocpilot/sites/site-002/reports/REPORT-BZPM-COPY-SYSTEM-REGISTRATION.md)

**Research:** M9.13–M9.18 **complete**  
**Copy content:** **Not started** — PAGE-COPY v1 shells registered  
**Design / Implementation:** **Not started** — **not authorized**

| ID | Page | URL (TEST) | Research | IA | Copy | Implementation |
|----|------|------------|----------|-----|------|----------------|
| **M9.13** | About Company | `/about` | **Complete** | Mapped | Registered | Not started |
| **M9.14** | Delivery | `/delivery` | **Complete** | Mapped | Registered | Not started |
| **M9.15** | Payment | `/payment-methods` | **Complete** | Mapped | Registered | Not started |
| **M9.16** | Dealers | `/dealers` | **Complete** | Mapped | Registered | Not started |
| **M9.17** | Warranty | `/guarantee` | **Complete** | Mapped | Registered | Not started |
| **M9.18** | Custom Manufacturing | `/custom-equipment` | **Complete** | Mapped | Registered | Not started |

**Research artifacts:**

- [BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md)
- [BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md)
- [BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md)
- [BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md)
- [BZPM-M9.17-WARRANTY-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.17-WARRANTY-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md)
- [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md)

**PAGE-COPY artifacts (v1 shells — copy not started):**

- [BZPM-M9.13-ABOUT-COMPANY-PAGE-COPY-v1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.13-ABOUT-COMPANY-PAGE-COPY-v1.md)
- [BZPM-M9.14-DELIVERY-PAGE-COPY-v1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.14-DELIVERY-PAGE-COPY-v1.md)
- [BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md)
- [BZPM-M9.16-DEALERS-PAGE-COPY-v1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.16-DEALERS-PAGE-COPY-v1.md)
- [BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md)
- [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.md)

### Separate completed workstream — Contacts

| Field | Value |
|-------|--------|
| **Page** | Contacts |
| **URL** | `/contact/` |
| **Status** | **Delivered** |
| **Program** | **Separate completed workstream** — **not** Corporate Pages Program |
| **Reason** | Implemented 2026-06-21 before program registration; outside M9.13–M9.18 research series |
| **Evidence** | [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md) |

**Mode:** Documentation registration only — **no** corporate page implementation authorized by this section.

---

# Backlog

Backlog items map to milestones and ROAD decisions. **No implementation authorized** by backlog presence alone.

## HIGH

| ID | Title | ROAD / Milestone | Notes |
| --- | --- | --- | --- |
| BL-H01 | Git checkpoint before catalog implementation waves | M4 | Survivability gate |
| BL-H02 | Backup milestone | M5 | Required before M6+ per ROAD-010 sequencing |
| BL-H03 | Catalog architecture audit | M6 | Document stack, category tree, attribute/filter model, TEST inventory |
| BL-H04 | Launch Mode — Neutral Equipment Only | ROAD-001 · M7 | Launch visual scope |
| BL-H05 | TEST cleanup — products, attributes, filters | ROAD-002 · M8 | User-facing surface hygiene |
| BL-H06 | Filter profile system — category level | ROAD-003 · M9 | Foundation for all filter work |
| BL-H07 | Subcategory filter profile overrides | ROAD-004 · M9 | Washing Baths vs Undercounter Stands pattern |
| BL-H08 | Presentation Pack executive closeout | M2 | Confirm archive / management review complete |

## MEDIUM

| ID | Title | ROAD / Milestone | Notes |
| --- | --- | --- | --- |
| BL-M01 | Dynamic filter visibility | ROAD-005 · M10 | Empty / unused / irrelevant filter hiding |
| BL-M02 | Filter groups (Price, Dimensions, Construction, Materials, Additional) | ROAD-006 · M11 | Semantic grouping |
| BL-M03 | Primary vs Additional filters | ROAD-007 · M11 | Priority tier in filter panel |
| BL-M04 | Native Benchmark Group — reference monitoring | ROAD-008 | Feed M11, M12, M13; no direct copy |
| BL-M05 | Catalog View #3 — Unitorg dual-column investigation | ROAD-009 · M12 | Spec only; FIM-W3Y-002 |
| BL-M06 | Resolve 13 MI Review Required tier flags | MI track | Master Report §9 |
| BL-M07 | Cross-link catalog-redesign findings to M6 audit | M6 | W0–W2 findings register; avoid re-audit |

## LOW

| ID | Title | ROAD / Milestone | Notes |
| --- | --- | --- | --- |
| BL-L01 | Catalog UX Intelligence Program charter | ROAD-010 · M13 | After M2 + M3 + M5 |
| BL-L02 | W4 Competitor Intelligence (MI continuation) | MI track | P1 cohort per Master Report |
| BL-L03 | Expansion queue triage (21 Strong + 22 Possible) | MI track | COMP-BZPM-047+ assignment |
| BL-L04 | W1E Product Taxonomy Audit | Deferred D-01 | Operator charter required |
| BL-L05 | Operator Manual Review Notes commit (W3Y.1) | MI track | Close SAFE UNKNOWN on verbatim notes |
| BL-L06 | Registry / execution-cases-registry update for `bzpm-roadmap` | M4 | Register new case folder in Factory registry |

---

# Decision Log

All approved roadmap items. Status **Approved** unless noted.

| ID | Decision summary | Date | Source | Status |
| --- | --- | --- | --- | --- |
| **ROAD-001** | Launch Mode: Catalog = Neutral Equipment Only until other parent categories populated | 2026-06-14 | W3X/W3Y strategic planning discussion | Approved |
| **ROAD-002** | TEST Cleanup: remove test products, test attributes, test filters from user-facing surfaces | 2026-06-14 | W3X/W3Y strategic planning discussion | Approved |
| **ROAD-003** | Filter Profile System: category-level filter profiles | 2026-06-14 | W3X/W3Y strategic planning discussion | Approved |
| **ROAD-004** | Subcategory Filter Profiles: category overrides (e.g. Washing Baths vs Undercounter Stands) | 2026-06-14 | W3X/W3Y strategic planning discussion | Approved |
| **ROAD-005** | Dynamic Filter Visibility: hide empty, unused, irrelevant filters | 2026-06-14 | W3X/W3Y strategic planning discussion | Approved |
| **ROAD-006** | Filter Groups: Price & Availability, Dimensions, Construction, Materials, Additional Parameters | 2026-06-14 | W3X/W3Y strategic planning discussion | Approved |
| **ROAD-007** | Primary vs Secondary Filters: Primary Filters + Additional Filters | 2026-06-14 | W3X/W3Y strategic planning discussion | Approved |
| **ROAD-008** | Native Benchmark Group: УЗНМ, КЛЕН, Unitorg, Trapeza, Kobor, Комплекс Трейд | 2026-06-14 | W3Y operator insights + W3X/W3Y strategic planning | Approved |
| **ROAD-009** | Catalog View #3: investigate Unitorg-style dual-column listing layout | 2026-06-14 | W3Y FIM-W3Y-002 + W3X/W3Y strategic planning | Approved |
| **ROAD-010** | Catalog UX Intelligence Program: after Presentation Pack + Roadmap Update + Backup Milestone | 2026-06-14 | W3X/W3Y strategic planning discussion | Approved |

### Roadmap meta-decisions

| ID | Decision summary | Date | Source | Status |
| --- | --- | --- | --- | --- |
| **RMETA-001** | Create `bzpm-roadmap/` as canonical BZPM product planning case | 2026-06-14 | BZPM Product Roadmap Audit task | Approved |
| **RMETA-002** | This document supersedes informal chat-only BZPM forward planning | 2026-06-14 | BZPM Product Roadmap Audit task | Approved |
| **RMETA-003** | Catalog-redesign decision log (D-01…R-05) remains valid for audit-phase decisions; ROAD-001…010 govern forward product plan | 2026-06-14 | Repository evidence — two scopes | Approved |

### Change log

| Date | Change |
| --- | --- |
| 2026-06-14 | **CREATED** — BZPM Product Roadmap v1; initial decision log ROAD-001…010; milestones M1–M13; backlog BL-H/M/L |
| 2026-06-17 | **UPDATED** — SITE-002 authority freeze → `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI`; MANUAL UI CANONICAL; **M9.8 UX Polish Pack** (M9.8.1–M9.8.8); EC-01 registered; OCPilot delivery track section added |
| 2026-06-22 | **UPDATED** — **Corporate Pages Program** registered (M9.13–M9.18); M9.13/M9.14 research artifacts; Contacts excluded as separate delivered workstream |
| 2026-06-22 | **UPDATED** — Corporate Pages Research phase **COMPLETE** (M9.15–M9.18); IA map [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](BZPM-CORPORATE-PAGES-IA-MAP-v1.md); M9.17 URL `/guarantee` |
| 2026-06-22 | **UPDATED** — Copy artefact system **REGISTERED**; [BZPM-COPY-STANDARDS-v1.md](BZPM-COPY-STANDARDS-v1.md); M9.13–M9.18 PAGE-COPY v1 shells |
| 2026-06-19 | **UPDATED** — Authority `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`; M9.8.1/2/5 marked complete; **M9.8.9 Minor Fixes Pack #1** (M9.8.9-01…08) registered as active work package; M9.8.9-06 filter bugs added to open bugs |

---

*BZPM Product Roadmap v1 — documentation only. No implementation authorized.*
