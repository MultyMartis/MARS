# REPORT — WF-R01.3.3 WAVE S1 GLOBAL SHELL CONTRACT

**Artifact ID:** WF-R01.3.3 Wave S1 — Global Shell Contract Publication (v1)  
**Date:** 2026-06-19  
**Mode:** documentation-only wave — **no** implementation  
**Honesty boundary:** Human-operated normative contract publication. **Not** BREADCRUMBS/PAGINATION implementation. **Not** G2 authorization. **Not** coverage metric mutation.

---

## 1. Result

| Field | Value |
|-------|-------|
| **Status** | **COMPLETE** |
| **Contract decision** | Website Factory Global Shell Contract v1 **ACCEPTED / PUBLISHED** |
| **Contract path** | `projects/mars-website-factory/global-shell-contract-v1.md` |
| **WF-R01.3.3 state** | **ACCEPTED** · Wave **S1 COMPLETE** · subprogram **NOT COMPLETE** |
| **Metrics** | RC **32/32** · RPC **15/32** · RSC **1/10 global; 1/1 LANDING** · SC **LANDING PASS** · PC **1/1 LANDING** — **UNCHANGED** |
| **Next task** | **WF-R01.3.3 Wave S2 — BREADCRUMBS Reference Partial** |

**Naming decision:** Charter referenced `GLOBAL-SHELL-CONTRACT-v1.md` as equivalent; canonical path follows adjacent normative contracts in `projects/mars-website-factory/` (`frontend-visual-foundation-contract-v1.md`, `section-replacement-contract-v1.md`) — lowercase kebab-case `global-shell-contract-v1.md`.

---

## 2. Git Safety

| Item | Detail |
|------|--------|
| **Branch** | `mars/post-cycle8-live-tests` |
| **HEAD before task** | `b2e2980` — `foundry: accept WF-R01.3.3 structural shell charter` |
| **Staged files (at start)** | **None** |
| **Foreign WIP** | **Present** — MIG pilots, Triumph workspaces, `.recovery-temp`, OCPilot, unrelated edits — **excluded** |
| **Selective scope** | Contract + roadmap + OPERATIONAL-INDEX + this REPORT only |

---

## 3. Authority Reviewed

| Document | Path | Role |
|----------|------|------|
| WF-R01.3.3 charter | `projects/mars-website-factory/wf-r01-3-3-structural-shell-references-charter-v1.md` | Parent authority; shell stack §7; nav depth §8; matrix §12 |
| Charter pass REPORT | `reports/wf-r01-3-3-structural-shell-references-charter-pass-v1.md` | Acceptance evidence |
| Vocabulary Canon | `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` | F3 structural subtype |
| Coverage model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | Five dimensions; validation outcomes |
| LANDING completion | `projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md` | G1 shell bundle |
| G1 five-dimension exit | `reports/wf-r01-3-2-g1-five-dimension-exit-v1.md` | Verified shell order |
| Reference composition | `workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md` | LANDING shell evidence |
| LANDING scaffold manifest | `workspaces/website-factory-reference-v1/LANDING-SCAFFOLD-MANIFEST-v1.md` | RSC stub |
| LANDING page | `workspaces/website-factory-reference-v1/src/pages/index.html` | DOM order evidence |
| Block registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | HEADER_NAV, FOOTER, LEGAL_LINKS |
| Page type registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` | 10 minimum page types |
| Layout shell governance | `projects/mars-website-factory/layout-shell-governance.md` | HEADER ≠ HERO |
| Roadmap | `projects/mars-website-factory/roadmap.md` | Program sync |
| Operational index | `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Operator sync |

---

## 4. Duplicate Contract Check

| Field | Value |
|-------|-------|
| **Search terms** | `global shell`, `site shell`, `page shell`, `layout shell`, `Global Shell Contract`, `global-shell-contract` |
| **Existing contract** | **None** — glob `global-shell-contract*.md` → 0 files before S1 |
| **Drafts found** | Shell rules embedded in WF-R01.3.3 charter §7 and charter pass REPORT §8 — **superseded as standalone normative contract** by published artefact; not competing duplicates |
| **Related docs** | `layout-shell-governance.md`, `frontend-shell-first-start-protocol-v1.md` — complementary frontend governance; **not** Global Shell Contract |
| **Decision** | **CREATE** `global-shell-contract-v1.md` — no STOP condition |

---

## 5. Contract Identity

| Field | Value |
|-------|-------|
| **Name** | Website Factory Global Shell Contract |
| **Version** | v1 |
| **Status** | **ACCEPTED** |
| **Authority** | WF-R01.3.3 Wave S1 |
| **Classification** | documentation-layer normative contract |
| **Is not** | runtime component · CSS framework · HTML template · CMS integration · production deployment |

---

## 6. Global Shell Definition

| Field | Value |
|-------|-------|
| **Definition** | Site-level structural frame shared across one or more page types |
| **Canonical order** | `HEADER_NAV` → `MAIN` → `FOOTER` → `LEGAL_LINKS` nested in FOOTER |
| **Required regions** | `MAIN` (always); `FOOTER` + nested `LEGAL_LINKS` per matrix for most types |
| **Optional regions** | `HEADER_NAV` (OPT on `LANDING_PAGE`); contextual BREADCRUMBS/PAGINATION slots |
| **Site-level identity** | At most one site-level header/footer pair; exactly one MAIN |

---

## 7. Region Contracts

### HEADER_NAV

- F3 Structural Block · L0
- Brand, global primary nav, optional utility/contact, optional compact action, mobile entry
- ≠ HERO, BREADCRUMBS, FILTERS, SEARCH, footer nav
- Reference partial complete (WF-R01.3.2 Wave C2) — **not repeated**

### MAIN

- Semantic content region — **not** a Registry block
- Exactly one per document; page-specific composition inside
- LANDING evidence: HERO through CONTACTS in `<main id="main">`

### FOOTER

- F3 Structural Block
- Site closing shell, secondary nav, contact summary, brand summary, legal slot, copyright
- ≠ CONTACTS block, standalone LEGAL_LINKS, HEADER_NAV replacement
- Reference partial complete (Wave B1) — **not repeated**

### LEGAL_LINKS

- F3 Structural Block · L3 · composition owner = FOOTER
- Links only — not legal document body
- Reference partial complete (Wave B2) — nested via `data-composition-slot="legal_links"`

---

## 8. Shell vs Page Content

| Rule | Value |
|------|-------|
| **Boundary** | Shell = structural frame; page content = blocks inside MAIN |
| **Local semantic elements** | Card/article `<header>`/`<footer>` permitted — not global shell |
| **Duplicate prevention** | No second site-level header/footer; no LEGAL_LINKS as sibling footer |

**Verified:** FOOTER outside MAIN; LEGAL_LINKS inside FOOTER in reference workspace.

---

## 9. Navigation Depth Model

| Level | Role | Surfaces |
|-------|------|----------|
| **L0** | Global primary orientation | `HEADER_NAV` |
| **L1** | Section / category navigation | Hub tabs, mega-menu sections, `CATEGORIES` |
| **L2** | Contextual hierarchy / result-set | BREADCRUMBS, PAGINATION, FILTERS facets |
| **L3** | Utility / compliance | `LEGAL_LINKS`, footer secondary links |

---

## 10. Shell Slots

| Slot | Required state | Owner | Notes |
|------|----------------|-------|-------|
| header slot | Page-type dependent | Page scaffold | REQ except minimal LANDING |
| main slot | **REQ** | Page scaffold | Always exactly one |
| footer slot | Page-type dependent | Page scaffold | REQ for registered types in matrix |
| legal-links slot | Nested when FOOTER REQ | FOOTER | Not document-root sibling |
| breadcrumbs slot | Page-type dependent | MAIN top zone | S2 future implementation |
| pagination slot | Page-type dependent | MAIN bottom zone | S3 future implementation |
| search slot | WF-R01.3.4 | Header + results page | Not S1 scope |

**No formal SLOT-* Registry created** — descriptive contract names only per charter instruction.

---

## 11. Page-Type Applicability

| Page type | HEADER_NAV | MAIN | BREADCRUMBS | PAGINATION | FOOTER | LEGAL_LINKS |
|-----------|------------|------|-------------|------------|--------|-------------|
| `LANDING_PAGE` | OPT | REQ | — | FORB | REQ | REQ |
| `HOME_PAGE` | REQ | REQ | POL | POL | REQ | REQ |
| `SERVICE_PAGE` | REQ | REQ | POL | — | REQ | REQ |
| `CATEGORY_PAGE` | REQ | REQ | REQ | REQ | REQ | REQ |
| `ABOUT_PAGE` | REQ | REQ | REQ | — | REQ | REQ |
| `CONTACT_PAGE` | REQ | REQ | POL | — | REQ | REQ |
| `FAQ_PAGE` | REQ | REQ | POL | POL | REQ | REQ |
| `REVIEWS_PAGE` | REQ | REQ | POL | POL | REQ | REQ |
| `LEGAL_PAGE` | REQ | REQ | POL | — | REQ | REQ |
| `PRODUCT_PAGE` | REQ | REQ | REQ | — | REQ | REQ |

All codes from PAGE-TYPE-REGISTRY-v1 minimum 10. `SEARCH_RESULTS_PAGE` — planned note only; not Registry identity.

---

## 12. Responsive Contract

| Topic | Policy |
|-------|--------|
| **DOM order** | Semantic shell order preserved all viewports |
| **Mobile navigation** | Accessible trigger; state sync |
| **Footer adaptation** | Columns may stack; legal links may wrap |
| **Overflow** | No persistent horizontal shell overflow |
| **Sticky variation** | Allowed — not mandatory |
| **Breakpoints** | Project design system — **no** universal `1024px` mandate |

---

## 13. Accessibility Minimum

| Topic | Policy |
|-------|--------|
| **Landmarks** | One `<main>`; named nav regions |
| **Navigation labels** | `aria-label` or heading association |
| **Keyboard** | Shell controls operable |
| **ARIA** | Mobile toggle `aria-expanded` / `aria-controls` |
| **Focus** | Visible focus on interactive shell controls |
| **Text scaling** | Shell functional at increased text sizes |

**Not** a WCAG certification claim.

---

## 14. Asset and JavaScript Contract

| Topic | Policy |
|-------|--------|
| **Dependencies** | Shell may require CSS/JS |
| **Manifest** | Explicit listing in scaffold manifest |
| **Graceful fallback** | No JS must not hide critical MAIN content |
| **Initialization** | No double-init of shell modules |
| **Runtime boundary** | No shared Factory production runtime assumed |

---

## 15. Scaffold Integration Contract

| Topic | Policy |
|-------|--------|
| **Required mappings** | page identity, shell regions, MAIN composition, optional contextual slots, assets, JS, build/validation evidence |
| **Manifest requirements** | `{PAGE_TYPE}-SCAFFOLD-MANIFEST-v1.md` per coverage model |
| **Evidence requirements** | Build PASS + wave REPORT for RSC accrual |
| **Distinctions** | Shell Contract ≠ Scaffold ≠ Reference Composition ≠ Built page ≠ Verified page ≠ Production Pass |

---

## 16. Validation Contract

| Check | Expected result |
|-------|-----------------|
| Site-level HEADER_NAV count | 0 or 1 per page type |
| MAIN count | **1** |
| Site-level FOOTER count | 0 or 1 per page type |
| Shell DOM order | HEADER_NAV → MAIN → FOOTER |
| LEGAL_LINKS nesting | In FOOTER when required |
| Duplicate block identity | None at site level |
| Local card header/footer | **Not** errors |
| Build result | PASS for scaffold workspace |

**Outcomes:** BUILT ≠ STRUCTURALLY VALIDATED ≠ FIDELITY VERIFIED ≠ PRODUCTION PASS

---

## 17. Coverage Accounting

| Dimension | Value | Changed? |
|-----------|-------|----------|
| **RC** | **32/32** | **No** |
| **RPC** | **15/32** | **No** |
| **RSC** | **1/10 global; 1/1 LANDING** | **No** |
| **SC** | **LANDING PASS** | **No** |
| **PC** | **1/1 LANDING** | **No** |

**Confirmation:** Global Shell Contract publication does **not** add RPC, RSC, SC PASS, or PC PASS.

---

## 18. Allowed Variations

- Sticky/static HEADER_NAV
- Compact/expanded FOOTER; variable column count
- Desktop/mobile nav representations
- Optional utility bar or header action
- Minimal LANDING without full HEADER_NAV when matrix allows
- Project-specific class naming and CMS rendering

Must preserve semantic order, vocabulary identity, accessibility minimum, duplicate prevention, coverage evidence rules.

---

## 19. Forbidden Compositions

```text
FOOTER inside MAIN
HEADER_NAV inside HERO / HERO inside HEADER_NAV
LEGAL_LINKS as full legal page content
Two site-level headers or footers
BREADCRUMBS as HEADER_NAV
PAGINATION as PROCESS
SEARCH merged into HEADER_NAV without declaration
FILTERS as primary navigation
Documentation-only shell counted as scaffold coverage
Build PASS claimed as production acceptance
W2 re-implementation (HEADER_NAV, FOOTER, LEGAL_LINKS)
```

---

## 20. Future Wave Handoff

| Wave | Inputs from S1 |
|------|----------------|
| **S2** | Shell boundaries · breadcrumbs slot · L2 depth · validation minimum · coverage rules |
| **S3** | Shell boundaries · pagination slot · L2 depth · list surface rules |
| **S4** | Page-type matrix refinement · scaffold contract publication |
| **S5** | Exit evaluation · WF-R01.3.4 handoff |

---

## 21. Files Created

| File | Purpose |
|------|---------|
| `projects/mars-website-factory/global-shell-contract-v1.md` | ACCEPTED normative Global Shell Contract v1 |
| `reports/wf-r01-3-3-wave-s1-global-shell-contract-v1.md` | This Wave S1 REPORT |

---

## 22. Files Modified

| File | Change |
|------|--------|
| `projects/mars-website-factory/roadmap.md` | R01.3.3 row — S1 COMPLETE; contract link; next S2; changelog entry |
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Wave S1 state; contract link; metrics unchanged; next S2 |

---

## 23. Validation

| Check | Result |
|-------|--------|
| Contract structure (25 sections) | **PASS** |
| Document status = ACCEPTED | **PASS** |
| Shell order matches G1 evidence | **PASS** |
| FOOTER outside MAIN | **PASS** (reference verified) |
| LEGAL_LINKS inside FOOTER | **PASS** (reference verified) |
| Page types from Registry only | **PASS** — 10 minimum codes |
| No new block IDs | **PASS** |
| Registry unchanged | **PASS** |
| Reference workspace `src/` unchanged | **PASS** |
| Metrics unchanged | **PASS** |
| BREADCRUMBS not implemented | **PASS** |
| PAGINATION not implemented | **PASS** |
| S2 not started | **PASS** |
| G2 not authorized | **PASS** |
| Historical reports unchanged | **PASS** |
| No false claims in artefacts | **PASS** |

---

## 24. Git Result

| Item | Detail |
|------|--------|
| **Commit hash** | *(recorded at commit time below)* |
| **Commit message** | `foundry: publish WF-R01.3.3 global shell contract` |
| **Push result** | *(recorded at push time below)* |
| **Files committed** | 4 — contract, roadmap, OPERATIONAL-INDEX, wave REPORT |
| **No foreign lane confirmation** | **Confirmed** — selective paths only |

---

## 25. Final Status

```text
COMPLETE
```

---

## 26. Next Task

```text
WF-R01.3.3 Wave S2 — BREADCRUMBS Reference Partial
```

**Do not execute** in this pass.

---

## 27. Exact Evidence Paths

- `projects/mars-website-factory/global-shell-contract-v1.md`
- `reports/wf-r01-3-3-wave-s1-global-shell-contract-v1.md`
- `projects/mars-website-factory/wf-r01-3-3-structural-shell-references-charter-v1.md`
- `reports/wf-r01-3-3-structural-shell-references-charter-pass-v1.md`
- `projects/mars-website-factory/roadmap.md`
- `projects/mars-website-factory/OPERATIONAL-INDEX.md`
- `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md`
- `projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md`
- `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md`
- `projects/mars-website-factory/layout-shell-governance.md`
- `reports/wf-r01-3-2-g1-five-dimension-exit-v1.md`
- `workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md`
- `workspaces/website-factory-reference-v1/LANDING-SCAFFOLD-MANIFEST-v1.md`
- `workspaces/website-factory-reference-v1/src/pages/index.html`
- `workspaces/website-factory-reference-v1/src/partials/sections/header-nav.html`
- `workspaces/website-factory-reference-v1/src/partials/sections/footer.html`
- `workspaces/website-factory-reference-v1/src/partials/components/legal-links.html`
- `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md`
- `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md`

---

## 28. Stop Confirmation

```text
Wave S2: NOT STARTED
BREADCRUMBS: NOT IMPLEMENTED
PAGINATION: NOT IMPLEMENTED
WF-R01.3.4: NOT STARTED
G2 execution: NOT STARTED
Coverage metrics: UNCHANGED
Reference workspace src/: NOT MODIFIED
Production readiness: NOT CLAIMED
```

---

*Wave S1 artefact: `reports/wf-r01-3-3-wave-s1-global-shell-contract-v1.md`*
