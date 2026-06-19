# REPORT — WF-R01.3.3 STRUCTURAL & SHELL REFERENCES CHARTER PASS

**Artifact ID:** WF-R01.3.3 — Structural & Shell References Charter Pass (v1)  
**Date:** 2026-06-19  
**Mode:** charter pass — documentation only; **no** implementation  
**Honesty boundary:** Human-operated charter acceptance. **Not** wave execution. **Not** G2 authorization. **Not** coverage metric mutation.

---

## 1. Result

| Field | Value |
|-------|-------|
| **Status** | **ACCEPTED** |
| **Charter decision** | WF-R01.3.3 Structural & Shell References Charter v1 **ACCEPTED** |
| **Charter path** | `projects/mars-website-factory/wf-r01-3-3-structural-shell-references-charter-v1.md` |
| **Parent track** | WF-R01.3 — Reference Implementation Expansion (**DESIGN**) |
| **Metrics** | RC **32/32** · RPC **15/32** · RSC **1/10 global; 1/1 LANDING** · SC **LANDING PASS** · PC **1/1 LANDING** — **UNCHANGED** |
| **Next task** | **WF-R01.3.3 Wave S1 — Global Shell Contract publication** |

---

## 2. Git Safety

| Item | Detail |
|------|--------|
| **Branch** | `mars/post-cycle8-live-tests` |
| **HEAD before task** | `929dbc0` — `foundry: select post-G1 reference expansion track` |
| **Previous unpushed commit status** | `929dbc0` was **ahead 1** of `origin/mars/post-cycle8-live-tests` at task start — pushed with charter commit |
| **Staged files (at start)** | **None** |
| **Foreign WIP** | **Present** — MIG pilots, Triumph workspaces, `.recovery-temp`, OCPilot, unrelated edits — **excluded** |
| **Selective scope** | Charter + roadmap + OPERATIONAL-INDEX + this REPORT only |

---

## 3. Authority Reviewed

| Document | Path | Role |
|----------|------|------|
| Operational index | `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Program state sync |
| Roadmap | `projects/mars-website-factory/roadmap.md` | WF-R01 subprogram table |
| Factory README | `projects/mars-website-factory/README.md` | Pack identity |
| WF-R01 program charter | `reports/wf-r01-registry-expansion-program-charter-v1.md` | Parent CHARTERED scope |
| WF-R01 program design | `reports/foundry-registry-expansion-program-design-v1.md` | R01.3.3 definition; wave map |
| Reference expansion design | `reports/wf-r01-3-reference-expansion-program-design-v1.md` | § WF-R01.3.3 deliverables |
| Post-G1 track selection | `reports/wf-r01-3-post-g1-track-selection-v1.md` | Selected 3.3; CHARTER PASS REQUIRED |
| Coverage model charter | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | G0–G4; five dimensions |
| LANDING completion charter | `projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md` | W2 bundle; §3.3 coordination |
| G1 five-dimension exit | `reports/wf-r01-3-2-g1-five-dimension-exit-v1.md` | Post-G1 metrics |
| Vocabulary Canon | `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` | F3 subtype rules |
| Structural blocks charter | `projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md` | Tier A/B; BREADCRUMBS/PAGINATION policy |
| Block registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | HEADER_NAV, FOOTER, LEGAL_LINKS, FILTERS, SEARCH |
| Core block library | `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md` | Block catalog |
| Block gaps | `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md` | Partial gaps |
| Page type registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` | 10 minimum page types |
| Site type registry | `workspaces/website-factory-reference-v1/site-type-registry/SITE-TYPE-REGISTRY-v1.md` | Core 5 site types |
| LANDING composition | `workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md` | Published shell |
| LANDING scaffold manifest | `workspaces/website-factory-reference-v1/LANDING-SCAFFOLD-MANIFEST-v1.md` | RSC stub |

---

## 4. Duplicate Charter Check

| Field | Value |
|-------|-------|
| **Search terms** | `wf-r01-3-3`, `structural-shell`, `shell-references`, `global-shell`, `breadcrumbs-pagination` |
| **Existing charter** | **None** before this pass — glob `wf-r01-3-3*` → 0 files |
| **Drafts found** | **None** |
| **Decision** | **CREATE** new ACCEPTED charter — no duplicate |

---

## 5. Identity

| Field | Value |
|-------|-------|
| **ID** | **WF-R01.3.3** |
| **Canonical name** | **Structural & Shell References** |
| **Parent** | **WF-R01.3** — Reference Implementation Expansion |
| **Previous state** | **DEFINED / DESIGN** (program design only) |
| **New state** | **ACCEPTED** (charter v1) · implementation **NOT STARTED** |

---

## 6. Inherited Completed Scope

| Item | State |
|------|-------|
| **HEADER_NAV** | **PARTIAL** — Wave C2 under WF-R01.3.2 |
| **FOOTER** | **PARTIAL** — Wave B1 |
| **LEGAL_LINKS** | **PARTIAL** — Wave B2 (nested in FOOTER) |
| **LANDING shell** | **PUBLISHED** — REFERENCE-COMPOSITION-v1 § Site-level shell |
| **Reference Composition** | **PUBLISHED** — LANDING PC **1/1** |
| **G1 evidence** | `reports/wf-r01-3-2-g1-five-dimension-exit-v1.md` |
| **Explicit no-repeat rule** | `W2 structural partial implementation is already complete. WF-R01.3.3 must not repeat W2.` |

**Inherited evidence paths:**

- `reports/wf-r01-3-2-wave-b1-footer-v1.md`
- `reports/wf-r01-3-2-wave-b2-legal-links-v1.md`
- `reports/wf-r01-3-2-wave-c2-header-nav-v1.md`
- `reports/wf-r01-3-2-g1-five-dimension-exit-v1.md`
- `workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md`
- `workspaces/website-factory-reference-v1/LANDING-SCAFFOLD-MANIFEST-v1.md`

---

## 7. Residual Scope

| Direction | Charter section |
|-----------|-----------------|
| Global shell contract | §7 |
| Navigation depth (L0–L3) | §8 |
| BREADCRUMBS policy | §9 |
| PAGINATION policy | §10 |
| Shell scaffold depth | §11 |
| Page-type shell matrix | §12 |
| Vocabulary boundaries | §13 |
| Coverage accounting | §14 |
| G2 relationship | §15 |
| Handoff to WF-R01.3.4 | §16 |
| Execution waves S1–S5 | §17 |

---

## 8. Global Shell Contract

| Rule | Value |
|------|-------|
| **Shell order** | `HEADER_NAV` → `MAIN` → `FOOTER` → `LEGAL_LINKS` nested in FOOTER |
| **Site-level semantics** | Global shell is not page content; single site-level header/footer per page |
| **Duplicate prevention** | Site-level shell must not be duplicated; card-level `<header>`/`<footer>` permitted |
| **Nested legal composition** | `LEGAL_LINKS` inside `FOOTER` bottom slot — not sibling site footer |

---

## 9. Navigation Depth Policy

| Level | Role | Surfaces |
|-------|------|----------|
| **L0** | Global primary navigation | `HEADER_NAV` |
| **L1** | Section/category navigation | Mega-menu sections, hub tabs, `CATEGORIES` |
| **L2** | Local/contextual navigation | BREADCRUMBS, PAGINATION, FILTERS facets, sidebar (future) |
| **L3** | Utility/compliance navigation | `LEGAL_LINKS`, footer secondary links |

**Surface split:** HEADER_NAV ≠ BREADCRUMBS ≠ PAGINATION ≠ FILTERS ≠ SEARCH — each owns distinct depth band per charter §8.

---

## 10. BREADCRUMBS Policy

| Field | Value |
|-------|-------|
| **Family** | F3 Structural Block — Tier B layout-component (no v1.1 `block_id` row) |
| **Purpose** | Hierarchical orientation; parent navigation; internal pages |
| **Page-type applicability** | O on CATEGORY/PRODUCT/ABOUT; R on hubs; — on LANDING_PAGE |
| **Boundaries** | ≠ HEADER_NAV; ≠ SEO Surface (F6); structured data = future composition |
| **Future T1+ criteria** | partial + SCSS + scaffold slot + build PASS + mapping + REPORT |

**Implementation in charter pass:** **FORBIDDEN**

---

## 11. PAGINATION Policy

| Field | Value |
|-------|-------|
| **Family** | F3 Structural Block — Tier B layout-component |
| **Purpose** | List paging on PLP/archive/search results |
| **Page-type applicability** | O on CATEGORY_PAGE; P on HOME/FAQ/REVIEWS; FORB on LANDING |
| **Boundaries** | ≠ FILTERS; ≠ SEARCH; ≠ STEPPER/PROCESS; ≠ carousel nav |
| **Future T1+ criteria** | Same six-point pattern as BREADCRUMBS |

**Implementation in charter pass:** **FORBIDDEN**

---

## 12. Shell Scaffold Contract

| Slot | Required |
|------|----------|
| Page identity | Yes |
| HEADER_NAV slot | Yes |
| MAIN content region | Yes |
| Optional BREADCRUMBS | Page-type dependent |
| Page-specific block sequence | Yes |
| Optional PAGINATION | List surfaces |
| FOOTER + LEGAL_LINKS composition | Yes |
| Asset/JS mapping | Yes |
| Build evidence | `npm run build` PASS |

**RSC accounting:** policy docs alone → **no** RSC; built scaffold + manifest + PASS → **+1** per `page_type`.

---

## 13. Page-Type Shell Matrix

| Page type | HEADER_NAV | BREADCRUMBS | PAGINATION | FOOTER | LEGAL_LINKS |
|-----------|------------|-------------|------------|--------|-------------|
| `LANDING_PAGE` | OPT | — | FORB | REQ | REQ |
| `HOME_PAGE` | REQ | POL (R) | POL (P) | REQ | REQ |
| `SERVICE_PAGE` | REQ | POL (R) | — | REQ | REQ |
| `CATEGORY_PAGE` | REQ | REQ (O) | REQ (O) | REQ | REQ |
| `PRODUCT_PAGE` | REQ | REQ (O) | — | REQ | REQ |
| `ABOUT_PAGE` | REQ | REQ (O) | — | REQ | REQ |
| `CONTACT_PAGE` | REQ | POL (R) | — | REQ | REQ |
| `FAQ_PAGE` | REQ | POL (R) | POL (P) | REQ | REQ |
| `REVIEWS_PAGE` | REQ | POL (R) | POL (P) | REQ | REQ |
| `LEGAL_PAGE` | REQ | POL (R) | — | REQ* | REQ* |

All `page_type` codes from PAGE-TYPE-REGISTRY-v1 minimum 10. `SEARCH_RESULTS_PAGE` — glossary/planned; deferred to WF-R01.3.4.

---

## 14. Coverage Contract

| Dimension | Value | Changed? |
|-----------|-------|----------|
| **RC** | **32/32** | **No** |
| **RPC** | **15/32** | **No** |
| **RSC** | **1/10** global · **1/1** LANDING | **No** |
| **SC** | **LANDING PASS** | **No** |
| **PC** | **1/1** LANDING | **No** |

**Future deltas (execution only):** BREADCRUMBS T1+ → potential **+1 RPC**; PAGINATION T1+ → potential **+1 RPC**; shell policy docs → **no** RPC/RSC.

**Confirmation:** metrics **unchanged** at charter T0.

---

## 15. G2 Relationship

| Field | Value |
|-------|-------|
| **Current G2 gap** | RPC **15/32** vs target **≥ 20/32** — gap **−5** |
| **WF-R01.3.3 contribution** | Shell policy prerequisite; BREADCRUMBS/PAGINATION readiness; scaffold contract; handoff to catalog track |
| **Explicit non-authorization** | `WF-R01.3.3 ACCEPTED ≠ G2 AUTHORIZED` |

---

## 16. Handoff to WF-R01.3.4

| Field | Value |
|-------|-------|
| **Inputs passed** | Global shell contract · nav depth · BREADCRUMBS/PAGINATION policy · scaffold contract · page-type matrix · coverage rules · unresolved S2/S3 items |
| **Dependencies** | WF-R01.3.3 **ACCEPTED** (satisfied) |
| **Excluded implementation** | FILTERS · SEARCH · catalog grids · PLP/PDP scaffolds · catalog compositions |

---

## 17. Execution Waves

| Wave | Purpose | Type | Expected evidence |
|------|---------|------|-------------------|
| **S1** | Global Shell Contract publication | Documentation | `GLOBAL-SHELL-CONTRACT-v1.md` + REPORT |
| **S2** | BREADCRUMBS reference partial | Implementation | partial + SCSS + slot + build PASS + REPORT |
| **S3** | PAGINATION reference partial | Implementation | partial + SCSS + list mapping + build PASS + REPORT |
| **S4** | Page-Type Shell Matrix + Scaffold Contract publication | Documentation | matrix/scaffold doc + REPORT |
| **S5** | Exit evaluation and handoff | Evaluation | five-dimension delta + 3.4 handoff REPORT |

**W2 partials not repeated.** Charter acceptance does not mark waves COMPLETE.

---

## 18. Files Created

| File | Purpose |
|------|---------|
| `projects/mars-website-factory/wf-r01-3-3-structural-shell-references-charter-v1.md` | ACCEPTED subprogram charter |
| `reports/wf-r01-3-3-structural-shell-references-charter-pass-v1.md` | This charter pass REPORT |

---

## 19. Files Modified

| File | Change |
|------|--------|
| `projects/mars-website-factory/roadmap.md` | R01.3.3 row **ACCEPTED**; changelog entry |
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` | WF-R01.3.3 state; next task pointer; last-updated footer |

---

## 20. Validation

| Check | Result |
|-------|--------|
| Charter structure (22 sections) | **PASS** |
| Registry vocabulary (canonical IDs) | **PASS** — no new `block_id` |
| Page-type identity from PAGE-TYPE-REGISTRY-v1 | **PASS** — 10 minimum codes only |
| Coverage consistency | **PASS** — no false RPC/RSC increase |
| No implementation | **PASS** — no HTML/SCSS/JS changes |
| No false G2 claims | **PASS** — staged diff scan clean |
| W2 not reopened | **PASS** |
| WF-R01.3.4 not started | **PASS** |
| Historical reports unchanged | **PASS** |

**Dangerous phrase scan (staged diff):** no matches for `G2 ACTIVE`, `G2 CLOSED`, `production-ready`, `implemented breadcrumbs`, `implemented pagination`, `WF-R01.3.3 COMPLETE`.

---

## 21. Git Result

| Item | Detail |
|------|--------|
| **Commit hash** | *(recorded at commit time below)* |
| **Commit message** | `foundry: accept WF-R01.3.3 structural shell charter` |
| **Push result** | `origin/mars/post-cycle8-live-tests` — non-force push |
| **Files committed** | 4 — charter, roadmap, OPERATIONAL-INDEX, charter pass REPORT |
| **No foreign lane confirmation** | **Confirmed** — selective paths only |

---

## 22. Final Status

```text
ACCEPTED
```

---

## 23. Next Task

```text
WF-R01.3.3 Wave S1 — Global Shell Contract publication
```

**Do not execute** in this pass.

---

## 24. Exact Evidence Paths

- `projects/mars-website-factory/wf-r01-3-3-structural-shell-references-charter-v1.md`
- `reports/wf-r01-3-3-structural-shell-references-charter-pass-v1.md`
- `projects/mars-website-factory/roadmap.md`
- `projects/mars-website-factory/OPERATIONAL-INDEX.md`
- `reports/wf-r01-3-post-g1-track-selection-v1.md`
- `reports/wf-r01-3-reference-expansion-program-design-v1.md`
- `reports/foundry-registry-expansion-program-design-v1.md`
- `reports/wf-r01-registry-expansion-program-charter-v1.md`
- `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md`
- `projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md`
- `reports/wf-r01-3-2-g1-five-dimension-exit-v1.md`
- `projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md`
- `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md`
- `reports/wf-r01-3-2-wave-b1-footer-v1.md`
- `reports/wf-r01-3-2-wave-b2-legal-links-v1.md`
- `reports/wf-r01-3-2-wave-c2-header-nav-v1.md`
- `workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md`
- `workspaces/website-factory-reference-v1/LANDING-SCAFFOLD-MANIFEST-v1.md`
- `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md`
- `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md`
- `workspaces/website-factory-reference-v1/block-registry/BLOCK-DEPENDENCY-RULES-v1.md`
- `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md`

---

## 25. Stop Confirmation

```text
WF-R01.3.3 implementation: NOT STARTED
BREADCRUMBS: NOT IMPLEMENTED
PAGINATION: NOT IMPLEMENTED
WF-R01.3.4: NOT STARTED
G2 execution: NOT STARTED
WF-A03 Pixel Factory: NOT STARTED
Coverage metrics: UNCHANGED
Production readiness: NOT CLAIMED
```

---

*Charter pass artefact: `reports/wf-r01-3-3-structural-shell-references-charter-pass-v1.md`*
