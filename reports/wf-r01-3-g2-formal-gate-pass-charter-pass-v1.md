# REPORT — WF-R01.3 GATE G2 FORMAL GATE PASS CHARTER PASS

**Artifact ID:** WF-R01.3 Gate G2 Formal Gate Pass Charter Pass (v1)  
**Date:** 2026-06-20  
**Branch:** `mars/post-cycle8-live-tests`  
**Mode:** charter pass — **documentation-only** · **not** G2 evaluation · **not** G2 closure

---

## 1. Result

| Field | Value |
|-------|-------|
| **Status** | **COMPLETE** |
| **Charter decision** | **ACCEPTED** |
| **Charter path** | `projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md` |
| **Canonical gate identity** | **G2** — **PROMO + CATALOG scaffold** (WF-R01.3 composite readiness gate) |
| **Gate state** | **CHARTERED** · **READY WITH BLOCKERS** · **NOT EVALUATED** · **NOT PASSED** · **NOT CLOSED** |
| **RC** | **32/32** |
| **RPC** | **23/32** |
| **RSC** | **3/10 global** · **1/1 LANDING · 1/1 CATEGORY_PAGE · 1/1 PRODUCT_PAGE** |
| **SC** | **LANDING PASS** · **CATALOG PARTIAL** |
| **PC** | **1/1 LANDING corridor** · **1/1 CATALOG corridor** |
| **Hard blockers** | W3 PROMO partials · PROMO scaffolds · CATALOG SC PASS · PROMO SC PASS · formal gate REPORT · operator sign-off |
| **Next task** | **WF-R01.3 G2 Remediation — W3 PROMO Reference Completion Charter Pass** |

---

## 2. Git Safety

| Check | Result |
|-------|--------|
| **Branch** | `mars/post-cycle8-live-tests` |
| **HEAD before task** | `541e9fd` — `foundry: complete WF-R01.3.4 catalog vertical references` |
| **HEAD contains 541e9fd** | **Confirmed** |
| **WF-R01.3.4 remote state** | `origin/mars/post-cycle8-live-tests` at `541e9fd` — **confirmed** |
| **Staged files (at start)** | **None** |
| **Foreign WIP** | **Present** — MIG pilots, EAR, OCPilot, Triumph workspaces, `.recovery-temp`, unrelated edits — **excluded** |
| **Selective scope** | G2 charter · charter pass REPORT · roadmap · OPERATIONAL-INDEX |

---

## 3. Authority Reviewed

| Document | Path | Role |
|----------|------|------|
| WF-R01 program charter | `reports/wf-r01-registry-expansion-program-charter-v1.md` | Parent programme |
| WF-R01 program design | `reports/foundry-registry-expansion-program-design-v1.md` | Subprogram map |
| WF-R01.3 program design | `reports/wf-r01-3-reference-expansion-program-design-v1.md` | G2 gate table · wave map W3–W5 |
| Post-G1 track selection | `reports/wf-r01-3-post-g1-track-selection-v1.md` | G2 composite semantics |
| Coverage Model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | Binding G2 criteria |
| Vocabulary Canon | `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` | SEARCH_RESULTS_PAGE glossary |
| WF-R01.3.3 charter | `projects/mars-website-factory/wf-r01-3-3-structural-shell-references-charter-v1.md` | Shell / Tier B |
| WF-R01.3.4 charter | `projects/mars-website-factory/wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md` | G2 relationship §16 |
| C8 exit / G2 readiness | `reports/wf-r01-3-4-wave-c8-exit-g2-readiness-v1.md` | Readiness snapshot |
| G1 exit | `reports/wf-r01-3-2-g1-five-dimension-exit-v1.md` | Formal gate REPORT precedent |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | SEARCH_RESULTS note |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | PROMO page types |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | RSC rules |
| Block Registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | 32 rows |
| Block Gaps | `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md` | W3 gaps |
| Core Block Library | `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md` | Catalog inventory |
| Page-Type Registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` | RSC denominator |
| Site-Type Registry | `workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md` | PROMO / CATALOG |
| Roadmap | `projects/mars-website-factory/roadmap.md` | Programme sync |
| OPERATIONAL-INDEX | `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Operator entry |

---

## 4. Duplicate Charter Check

| Field | Value |
|-------|-------|
| **Search terms** | wf-r01-3-g2 · g2-gate · gate-g2 · formal-gate-pass · g2-charter · g2-evaluation · g2-closure |
| **Existing documents** | C8 G2 readiness REPORT only; G1 exit REPORT; program design G2 table — **no prior accepted G2 charter** |
| **Competing authority** | **None** |
| **Decision** | **PROCEED** — publish canonical G2 charter |

| Artefact | Classification |
|----------|----------------|
| `wf-r01-3-4-wave-c8-exit-g2-readiness-v1.md` | **REPORT** — readiness; complementary |
| `wf-r01-3-1-coverage-model-charter-v1.md` § G2 | **ACCEPTED** — criteria source |
| `wf-r01-3-post-g1-track-selection-v1.md` § G2 | **REPORT** — design-only composite note |
| Program design G2 table | **DESIGN** — aligned with Coverage Model |

---

## 5. Gate Identity

| Field | Value |
|-------|-------|
| **Gate ID** | **G2** |
| **Canonical name** | **PROMO + CATALOG scaffold** |
| **Parent programme** | **WF-R01.3** Reference Implementation Expansion |
| **Gate purpose** | Confirm minimum PROMO + CATALOG reference coverage before advancing programme without false production claims |
| **Predecessor** | **G1 — CLOSED** |
| **Successor** | **G3** corridor · **WF-R01.3.5** (after G2 CLOSED) · WF-A03 recommended precondition |
| **Charter/pass distinction** | Charter ACCEPTED ≠ G2 evaluation ≠ G2 PASS ≠ G2 CLOSED |

G2 is a **composite gate** across WF-R01.3 tracks (W3 PROMO + W4–W5 catalog + scaffolds + SC/PC). It is **not** a separate WF-R01.3.X execution subprogram ID.

---

## 6. Current Readiness Snapshot

| Dimension | Value |
|-----------|-------|
| **RC** | **32/32** |
| **RPC** | **23/32** (G2 numeric floor **SATISFIED**) |
| **RSC** | **3/10** |
| **SC** | **LANDING PASS · CATALOG PARTIAL** |
| **PC** | **1/1 LANDING · 1/1 CATALOG corridor** |

**Completed corridors:** FILTERS · SEARCH · CATEGORIES · CATEGORY_GRID · PRODUCT_GRID · PRODUCT_CARD · CATEGORY_PAGE · PRODUCT_PAGE scaffolds · MANUFACTURER P1 · AUTO P2 · binding matrix.

**Open blockers:** W3 PROMO · PROMO scaffolds · CATALOG SC PASS · SEARCH_RESULTS_PAGE authority · formal gate REPORT · operator sign-off.

---

## 7. G2 Criteria

| ID | Criterion | Authority | Type | Current state |
|----|-----------|-----------|------|---------------|
| G2-01 | RPC ≥ 20/32 | Coverage Model § G2 | NUMERIC | **SATISFIED** 23/32 |
| G2-02 | SERVICES T1+ | Coverage Model · W3 | STRUCTURAL | **OPEN** |
| G2-03 | TEAM T1+ | Same | STRUCTURAL | **OPEN** |
| G2-04 | ABOUT T1+ | Same | STRUCTURAL | **OPEN** |
| G2-05 | FILTERS T1+ | Coverage Model · CATALOG | STRUCTURAL | **SATISFIED** |
| G2-06 | SEARCH T1+ | Same | STRUCTURAL | **SATISFIED** |
| G2-07 | Catalog grids W5 | Program design W5 | STRUCTURAL | **SATISFIED** |
| G2-08 | PLP / CATEGORY_PAGE scaffold | Coverage Model G2 | STRUCTURAL | **SATISFIED** |
| G2-09 | PRODUCT_PAGE scaffold | wf-r01-3-4 C6 | STRUCTURAL | **SATISFIED** |
| G2-10 | PROMO money-page scaffolds | Coverage Model § PROMO | STRUCTURAL | **OPEN** |
| G2-11 | CATALOG SC PASS | Coverage Model § CATALOG | COVERAGE | **PARTIAL** |
| G2-12 | PROMO SC PASS | Coverage Model § PROMO | COVERAGE | **OPEN** |
| G2-13 | Catalog PC | C5/C6 compositions | COMPOSITIONAL | **SATISFIED** |
| G2-14 | PROMO PC | Coverage Model § PROMO | COMPOSITIONAL | **OPEN** |
| G2-15 | Vertical profiles | wf-r01-3-4 C7 | COMPOSITIONAL | **SATISFIED** |
| G2-16 | HEADER_NAV T1+ | G2 precondition chain | STRUCTURAL | **SATISFIED** |
| G2-17 | BREADCRUMBS / PAGINATION | WF-R01.3.3 | STRUCTURAL | **SATISFIED** |
| G2-18 | Build PASS | Coverage Model gate evidence | EVIDENCE | **SATISFIED** (catalog) |
| G2-19 | Formal gate evaluation REPORT | wf-r01-3-4 §663 · G1 precedent | EVIDENCE | **OPEN** |
| G2-20 | Operator sign-off | wf-r01-3-4 §562 | AUTHORITY | **OPEN** |
| G2-21 | No unauthorized Registry expansion | wf-r01-3-4 §19 | AUTHORITY | **SATISFIED** |
| G2-22 | Template-Art interim honesty | Coverage Model | QUALITY | **PARTIAL** |
| G2-23 | Handoff to WF-R01.3.5 | Program design | HANDOFF | **OPEN** |

---

## 8. Criterion Classification

### Hard blockers

G2-02, G2-03, G2-04, G2-10, G2-11 (PASS required), G2-12, G2-14, G2-19, G2-20.

### Conditional criteria

CONDITIONAL PASS decision class — **SAFE UNKNOWN**. CATALOG SC PARTIAL + SEARCH_RESULTS_PAGE — blocks PASS unless authority reconciliation or explicit waiver policy.

### Non-blocking debt

AUTO P2 limits · PC corridor notation · PROCESS vs W3 scope note · WF-R01.7 pending · foreign WIP.

### Informational limitations

RPC numeric satisfaction alone is **insufficient** for G2 CLOSED (wf-r01-3-4 §557).

---

## 9. W3 PROMO Requirement

| Target | Registry identity | Current state | Required state |
|--------|-------------------|---------------|----------------|
| Services | `SERVICES` | Not implemented | T1+ partial + REPORT |
| Team | `TEAM` | Not implemented | T1+ partial + REPORT |
| About | `ABOUT` | Not implemented | T1+ partial + REPORT |
| Process | `PROCESS` | T1+ exists (W1) | Already satisfies partial leg of PROMO SC content |

W3 wave map = **SERVICES · TEAM · ABOUT** only. Full PROMO SC also references **PROCESS** — partial already built.

---

## 10. PROMO Scaffold Requirement

- **Applicable page types:** `SERVICE_PAGE`, `ABOUT_PAGE`, `CONTACT_PAGE` (PAGE-TYPE-REGISTRY-v1 · Coverage Model § PROMO)
- **Required scaffolds:** **All three** for honest G2 PASS against Coverage Model minimum (charter §15 reconciliation)
- **Composition requirement:** Reference Composition + scaffold manifest per [reference-scaffold-contract-v1.md](../projects/mars-website-factory/reference-scaffold-contract-v1.md)
- **Coverage implication:** RSC up to +3 · PROMO SC PASS · PC up to +3 compositions
- **Current state:** **None** — RSC remains 3/10 with catalog + LANDING only

---

## 11. CATALOG SC Requirement

- **Current state:** **PARTIAL**
- **Required state:** **PASS** per Coverage Model § CATALOG minimum
- **Missing evidence:** `` `SEARCH_RESULTS_PAGE` `` scaffold (Registry absent · glossary-only in Vocabulary Canon)
- **Gate effect:** **Hard blocker** for G2-11 / G2 PASS via wf-r01-3-4 §663–670

---

## 12. SEARCH_RESULTS_PAGE Policy

- **Coverage Model:** listed in CATALOG scaffold minimum
- **Registry state:** not in PAGE-TYPE-REGISTRY minimum 10
- **Programme authority:** WF-R01.6 hygiene territory; wf-r01-3.4 deferred
- **Classification:** C8 **Decision B** — future candidate
- **Gate effect:** blocks **CATALOG SC PASS** · blocks **G2 PASS** via G2-11 · **does not** retroactively block WF-R01.3.4 exit
- **Future destination:** G2-R3 authority reconciliation or WF-R01.6

---

## 13. Evidence Package Contract

| Evidence | Required | Source/owner | Validation |
|----------|----------|--------------|------------|
| G2 charter | Yes | This charter | ACCEPTED |
| Criteria matrix | Yes | Charter §9 | Cited |
| Coverage snapshot | Yes | C8 REPORT | Five dimensions |
| Registry evidence | Yes | BLOCK/PAGE registries | 32 rows · 10 page types |
| Partial evidence | Yes | reference-v1 partials + REPORTs | T1+ inventory |
| Scaffold manifests | Yes | page-architecture manifests | Contract compliance |
| Compositions | Yes | *-REFERENCE-COMPOSITION-v1.md | PC |
| Build evidence | Yes | npm run build | Exit 0 |
| SC/PC evaluation | Yes | Coverage Model checklists | Honest PASS/FAIL |
| Remaining-debt register | Yes | Future gate REPORT | §11–§13 |
| Formal gate REPORT | Yes | Future evaluation task | Operator sign-off |
| Roadmap/index | Yes | roadmap · OPERATIONAL-INDEX | Gate sync |
| Git checkpoint | Yes | Selective commit | No foreign lane |

---

## 14. Formal Evaluation Procedure

1. Authority preflight  
2. Git/state freeze  
3. Evidence inventory  
4. Criterion-by-criterion audit (G2-01..G2-23)  
5. Coverage reconciliation  
6. Blocking-debt evaluation  
7. Gate decision (default PASS only if §11 all PASS)  
8. Roadmap/index update  
9. Selective Git checkpoint  
10. Handoff to WF-R01.3.5 or remediation  

Remediation **forbidden** inside evaluation unless separately authorized.

---

## 15. Allowed Gate Decisions

| Decision | Meaning | Conditions | Programme effect |
|----------|---------|------------|------------------|
| **PASS** | G2 closed | All §11 PASS + REPORT + sign-off | WF-R01.3.5 eligible; WF-A03 precondition met (no auto-start) |
| **CONDITIONAL PASS** | Waiver path | **Not binding-authorized** | **SAFE UNKNOWN** |
| **FAIL** | Criteria unmet | Hard FAIL after audit | Remediation → retest |
| **DEFERRED** | Evaluation postponed | Operator choice | No CLOSED |
| **BLOCKED BY AUTHORITY** | Normative conflict | Unresolved SEARCH_RESULTS vs Coverage Model | G2-R3 / WF-R01.6 |

---

## 16. Gate State Model

- **States:** UNCHARTERED → CHARTERED → READY WITH BLOCKERS → READY FOR EVALUATION → EVALUATION ACTIVE → decision → CLOSED  
- **Legal transitions:** remediation between READY WITH BLOCKERS and READY FOR EVALUATION  
- **Current state:** **CHARTERED · READY WITH BLOCKERS · NOT EVALUATED · NOT PASSED · NOT CLOSED**  
- **Forbidden:** CHARTERED → CLOSED; READY WITH BLOCKERS → PASS; RPC alone → CLOSED  

---

## 17. Remediation Packages

| Package | Purpose | Gate criteria | Type | Current state |
|---------|---------|---------------|------|---------------|
| **G2-R1** | W3 PROMO references | G2-02–04 | Implementation | **Not started** |
| **G2-R2** | PROMO scaffolds | G2-10, G2-14, G2-12 | Implementation | **Not started** |
| **G2-R3** | SEARCH_RESULTS authority | G2-11 prereq | Authority | **Open debt** |
| **G2-R4** | CATALOG SC completion | G2-11 | Evaluation/authority | **Blocked on R3** |
| **G2-R5** | Evidence assembly | G2-19 | Doc-only | **Not started** |

---

## 18. Remediation Dependency Order

**Sequence:** G2-R1 → G2-R2 → coverage recalc → G2-R3 → G2-R4 → G2-R5 → formal evaluation  

**Parallelizable:** G2-R1 with G2-R3 doc-only phase  

**Evaluation trigger:** all §11 hard blockers PASS (or explicit waiver policy if ever authorized)

---

## 19. Ownership and Approval

- **Normative owner:** Website Factory operator governance (human-operated)
- **Evidence owner:** Operator executing passes
- **Evaluator:** Operator on formal evaluation task
- **Approval authority:** Human sign-off in gate REPORT
- **SAFE UNKNOWN:** named steward not assigned

---

## 20. Coverage Freeze

| Dimension | Value |
|-----------|-------|
| RC | 32/32 |
| RPC | 23/32 |
| RSC | 3/10 |
| SC | LANDING PASS · CATALOG PARTIAL |
| PC | 1/1 LANDING · 1/1 CATALOG corridor |

**No-accrual:** charter pass changed **zero** metrics.

---

## 21. Successor and Failure Handoff

### PASS

WF-R01.3.5 charter pass eligibility · G3 corridor · WF-A03 recommended precondition · Template-Art pilot PROMO + CATALOG.

### CONDITIONAL PASS

**Not binding-authorized** — restrictions would require pre-published operator policy.

### FAIL

Remediation packages §17; repeat evaluation after evidence refresh.

### DEFERRED

Continue highest-priority remediation.

### BLOCKED BY AUTHORITY

G2-R3 / WF-R01.6 reconciliation before retest.

---

## 22. Files Created

| File | Purpose |
|------|---------|
| `projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md` | Normative G2 gate charter |
| `reports/wf-r01-3-g2-formal-gate-pass-charter-pass-v1.md` | This charter pass REPORT |

---

## 23. Files Modified

| File | Change |
|------|--------|
| `projects/mars-website-factory/roadmap.md` | G2 charter ACCEPTED · gate state · next task |
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Sync footer · gate state · next task |

---

## 24. Validation

| Check | Result |
|-------|--------|
| Identity consistent | **PASS** |
| Criteria from authority | **PASS** |
| Blocker classification | **PASS** |
| SEARCH_RESULTS honesty | **PASS** — Decision B preserved |
| No gate execution | **PASS** |
| No metric mutation | **PASS** |
| No implementation | **PASS** |
| No false pass claims | **PASS** |

---

## 25. Documentation State

| Surface | State |
|---------|-------|
| **roadmap** | G2 charter **ACCEPTED** · gate **CHARTERED / NOT CLOSED** |
| **OPERATIONAL-INDEX** | Metrics unchanged · next remediation task |
| **Gate state** | CHARTERED · READY WITH BLOCKERS |
| **Coverage** | Frozen at C8 values |
| **Next task** | W3 PROMO Reference Completion Charter Pass |

---

## 26. Git Result

| Item | Detail |
|------|--------|
| **Commit hash** | `f3b7a79` |
| **Commit message** | `foundry: accept WF-R01.3 G2 formal gate charter` |
| **Push result** | `origin/mars/post-cycle8-live-tests` updated `541e9fd..f3b7a79` |
| **Files committed** | `projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md` · `reports/wf-r01-3-g2-formal-gate-pass-charter-pass-v1.md` · `projects/mars-website-factory/roadmap.md` · `projects/mars-website-factory/OPERATIONAL-INDEX.md` |
| **No foreign lane confirmation** | **Confirmed** — staged scope = 4 files only |

---

## 27. Drift and Risks

| Severity | Finding | Gate effect | Destination |
|----------|---------|-------------|-------------|
| **MEDIUM** | SEARCH_RESULTS_PAGE Coverage vs Registry gap | Blocks CATALOG SC PASS | G2-R3 |
| **MEDIUM** | W3 PROMO partials open | Blocks G2 closure | G2-R1 |
| **MEDIUM** | PROMO scaffolds absent | Blocks G2-10/12/14 | G2-R2 |
| **LOW** | CONDITIONAL PASS not in binding authority | Evaluation ambiguity | Operator policy before evaluation |
| **LOW** | Foreign WIP on branch | None if excluded | Operator lanes |

---

## 28. Final Status

**COMPLETE**

---

## 29. Next Task

**WF-R01.3 G2 Remediation — W3 PROMO Reference Completion Charter Pass**

Authorize W3 wave (`SERVICES`, `TEAM`, `ABOUT` partials) under programme naming discipline. **Do not execute** in this pass.

---

## 30. Exact Evidence Paths

```text
projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md
reports/wf-r01-3-g2-formal-gate-pass-charter-pass-v1.md
projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md
projects/mars-website-factory/wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md
projects/mars-website-factory/global-shell-contract-v1.md
projects/mars-website-factory/page-type-shell-matrix-v1.md
projects/mars-website-factory/reference-scaffold-contract-v1.md
projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md
projects/mars-website-factory/roadmap.md
projects/mars-website-factory/OPERATIONAL-INDEX.md
reports/wf-r01-3-4-wave-c8-exit-g2-readiness-v1.md
reports/wf-r01-3-reference-expansion-program-design-v1.md
reports/wf-r01-3-post-g1-track-selection-v1.md
reports/wf-r01-3-2-g1-five-dimension-exit-v1.md
workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md
workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md
workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md
```

---

## 31. Stop Confirmation

```text
G2 formal evaluation: NOT EXECUTED
G2 PASS: NOT GRANTED
G2 closure: NOT PERFORMED
Remediation implementation: NOT STARTED
SEARCH_RESULTS_PAGE: NOT CREATED
Registry: NOT MODIFIED
Coverage Model: NOT MODIFIED
Coverage metrics: UNCHANGED
Implementation files: NOT MODIFIED
Production readiness: NOT CLAIMED
```

---

*Charter pass artefact: `reports/wf-r01-3-g2-formal-gate-pass-charter-pass-v1.md` · v1 · 2026-06-20*
