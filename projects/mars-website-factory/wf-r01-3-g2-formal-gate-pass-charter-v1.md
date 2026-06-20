# WF-R01.3 Gate G2 Formal Gate Pass Charter v1

**Subprogram lane:** WF-R01.3 — Reference Implementation Expansion  
**Gate ID:** **G2**  
**Version:** v1  
**Date:** 2026-06-20  
**Mode:** normative gate charter — **documentation and evaluation contract only**

**Honesty boundary:** This charter **authorizes and defines** formal Gate G2 evaluation procedure, criteria, evidence, and decision semantics. **Charter acceptance does not constitute Gate G2 PASS, G2 ACTIVE, G2 CLOSED, or remediation execution.**

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **ACCEPTED** |
| **Charter decision** | **ACCEPTED** — normative operator authority for Gate G2 formal evaluation |
| **Gate state after charter** | **CHARTERED** · **READY WITH BLOCKERS** · **NOT EVALUATED** · **NOT PASSED** · **NOT CLOSED** |
| **Implementation state** | **NOT STARTED** — no remediation authorized by this charter alone |
| **Coverage impact** | **None** — metrics frozen at charter snapshot (§25) |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Gate ID** | **G2** |
| **Canonical name** | **PROMO + CATALOG scaffold** |
| **Formal evaluation name** | **WF-R01.3 Gate G2 Formal Gate Pass** |
| **Parent programme** | **WF-R01.3** — Reference Implementation Expansion |
| **Program parent** | **WF-R01** — FOUNDRY Registry Expansion Program (**CHARTERED**) |
| **Gate level** | **WF-R01.3 readiness gate** (G0–G4 family) |
| **Gate type** | **Composite gate** — spans W3 PROMO partials, W4–W5 catalog corridor, PROMO/CATALOG scaffolds, SC/PC evidence, and formal gate REPORT |
| **Predecessor gate** | **G1 — CLOSED** ([wf-r01-3-2-g1-five-dimension-exit-v1.md](../../reports/wf-r01-3-2-g1-five-dimension-exit-v1.md)) |
| **Successor state (on PASS)** | **G3 planning corridor** · **WF-R01.3.5** charter eligibility · **WF-A03 recommended precondition satisfied** (not auto-start) |
| **Phase ID** | **No separate WF-R01.3.G2 subprogram ID** — G2 is a **gate**, not a chartered execution subprogram |
| **Charter path** | `projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md` |

**Charter / pass distinction (binding):**

```text
G2 charter acceptance ≠ G2 evaluation
G2 charter acceptance ≠ G2 PASS
G2 charter acceptance ≠ G2 CLOSED
G2 charter acceptance ≠ G2 ACTIVE
```

The word **Pass** in this charter title names the **charter pass artefact**, not an executed gate decision.

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| WF-R01 program charter | [wf-r01-registry-expansion-program-charter-v1.md](../../reports/wf-r01-registry-expansion-program-charter-v1.md) | Parent programme scope |
| WF-R01 program design | [foundry-registry-expansion-program-design-v1.md](../../reports/foundry-registry-expansion-program-design-v1.md) | Subprogram decomposition; wave map W3–W5 |
| WF-R01.3 program design | [wf-r01-3-reference-expansion-program-design-v1.md](../../reports/wf-r01-3-reference-expansion-program-design-v1.md) | G2 gate table; R01.3.4/3.5 dependencies |
| Coverage Model | [wf-r01-3-1-coverage-model-charter-v1.md](wf-r01-3-1-coverage-model-charter-v1.md) | **Binding** G2 criteria; Template-Art minimum sets; gate exit evidence |
| Post-G1 track selection | [wf-r01-3-post-g1-track-selection-v1.md](../../reports/wf-r01-3-post-g1-track-selection-v1.md) | G2 composite semantics; subprogram boundary |
| WF-R01.3.4 charter | [wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md](wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md) | G2 relationship; C8 readiness boundary |
| C8 exit / G2 readiness | [wf-r01-3-4-wave-c8-exit-g2-readiness-v1.md](../../reports/wf-r01-3-4-wave-c8-exit-g2-readiness-v1.md) | Current readiness snapshot; blocker inventory |
| G1 exit (precedent) | [wf-r01-3-2-g1-five-dimension-exit-v1.md](../../reports/wf-r01-3-2-g1-five-dimension-exit-v1.md) | Formal gate REPORT pattern |
| Global Shell Contract | [global-shell-contract-v1.md](global-shell-contract-v1.md) | SEARCH_RESULTS_PAGE planned note |
| Page-Type Shell Matrix | [page-type-shell-matrix-v1.md](page-type-shell-matrix-v1.md) | PROMO page-type shell surfaces |
| Reference Scaffold Contract | [reference-scaffold-contract-v1.md](reference-scaffold-contract-v1.md) | RSC accrual rules |
| Vocabulary Canon | [foundry-vocabulary-canon-charter-v1.md](foundry-vocabulary-canon-charter-v1.md) | SEARCH_RESULTS_PAGE glossary-only status |
| Block Registry | [BLOCK-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md) | 32 `block_id` SSOT |
| Block Gaps | [BLOCK-GAPS-v1.md](../../workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md) | W3 partial gaps |
| Page-Type Registry | [PAGE-TYPE-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md) | RSC denominator (10) |
| Site-Type Registry | [SITE-TYPE-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md) | PROMO / CATALOG site types |
| Roadmap | [roadmap.md](roadmap.md) | Programme sync |
| OPERATIONAL-INDEX | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Operator entry |

**Authority hierarchy for G2 criteria:** Coverage Model § Readiness Gates **>** WF-R01.3.4 charter §16 **>** C8 readiness REPORT **>** program design gate table. C8 is **readiness evidence**, not gate closure.

---

## 4. Purpose

Gate G2 exists to confirm that Reference Expansion has reached **minimum structural and compositional coverage** across the **PROMO** and **CATALOG** corridors such that the programme may advance without false production, Template-Art, or Factory-ready claims.

**G2 confirms:**

- RPC floor and primary W3–W5 deliverables per Coverage Model
- Required catalog and PROMO reference scaffolds where authority demands them
- Honest SC/PC state for LANDING + pilot PROMO/CATALOG corridors
- Operator-reviewed formal gate REPORT with five-dimension reconciliation

**G2 does not confirm:**

```text
production readiness
pixel-perfect fidelity
CMS integration
client deployment
runtime autonomy
full page-type coverage (RSC 10/10)
complete Website Factory
WF-R01.3 parent program COMPLETE
automatic WF-A03 start
```

---

## 5. Scope

### In scope

- Normative G2 criteria extraction and classification
- Hard / conditional / non-blocking debt taxonomy
- W3 PROMO, PROMO scaffold, CATALOG SC, SEARCH_RESULTS_PAGE policy
- Evidence package contract for formal evaluation
- Formal evaluation procedure and allowed decisions
- Remediation package definitions and dependency order
- Gate state model and handoff rules
- Coverage freeze at charter acceptance

### Out of scope

- G2 evaluation execution
- G2 PASS / CLOSED declaration
- W3 PROMO implementation
- PROMO scaffold implementation
- SEARCH_RESULTS_PAGE registration or scaffold creation
- Registry / Coverage Model / Vocabulary Canon mutation
- WF-R01.3.5 execution
- WF-A03 activation
- Metric accrual from this charter pass

---

## 6. Terminology

| Term | Definition |
|------|------------|
| **G2 readiness** | Preliminary assessment of programme proximity to formal gate pass — **not** a gate result |
| **G2 charter** | This document — normative contract of criteria, evidence, procedure, and decisions |
| **G2 remediation** | Separate authorized tasks closing missing gate criteria |
| **G2 evaluation** | Formal criterion-by-criterion audit under accepted charter |
| **G2 decision** | PASS · CONDITIONAL PASS · FAIL · DEFERRED · BLOCKED BY AUTHORITY |
| **G2 closure** | Recording accepted formal gate decision in roadmap and operational authority |

**Forbidden conflation:** charter ACCEPTED · readiness READY WITH BLOCKERS · evaluation COMPLETE · decision PASS.

---

## 7. Current Readiness Snapshot

**Snapshot date:** 2026-06-20 (charter acceptance)  
**Source:** [wf-r01-3-4-wave-c8-exit-g2-readiness-v1.md](../../reports/wf-r01-3-4-wave-c8-exit-g2-readiness-v1.md)

| Dimension | Value |
|-----------|-------|
| **RC** | **32/32** |
| **RPC** | **23/32** |
| **RSC** | **3/10 global** · **1/1 LANDING** · **1/1 CATEGORY_PAGE** · **1/1 PRODUCT_PAGE** |
| **SC** | **LANDING PASS** · **CATALOG PARTIAL** |
| **PC** | **1/1 LANDING corridor** · **1/1 CATALOG corridor** |

**Completed corridors (reference evidence):**

```text
FILTERS · SEARCH · CATEGORIES · CATEGORY_GRID · PRODUCT_GRID · PRODUCT_CARD
CATEGORY_PAGE scaffold · PRODUCT_PAGE scaffold
MANUFACTURER profile (P1 READY) · AUTO profile (P2 PARTIAL)
```

**Open blockers (C8):**

```text
W3 PROMO partials (SERVICES · TEAM · ABOUT)
PROMO money-page scaffolds
CATALOG SC PASS
SEARCH_RESULTS_PAGE authority gap
Dedicated G2 formal gate evaluation REPORT (absent)
```

**Readiness verdict:** **G2 READY WITH BLOCKERS** — numeric RPC criterion **SATISFIED**; composite gate **NOT CLOSED**.

This snapshot is **not** a gate result.

---

## 8. Gate State Model

### States

| State | Meaning |
|-------|---------|
| **UNCHARTERED** | No accepted G2 gate charter |
| **CHARTERED** | This charter ACCEPTED; evaluation contract published |
| **READY WITH BLOCKERS** | Readiness assessed; hard criteria remain open |
| **READY FOR EVALUATION** | All hard criteria evidenced; evaluation may open |
| **EVALUATION ACTIVE** | Formal gate audit in progress |
| **PASS** | Formal decision recorded — all hard criteria met |
| **CONDITIONAL PASS** | Reserved decision — **not binding-authorized** (§20) |
| **FAIL** | Formal decision — hard criteria not met after audit |
| **DEFERRED** | Evaluation postponed pending remediation |
| **BLOCKED BY AUTHORITY** | Normative conflict prevents honest evaluation |
| **CLOSED** | Decision recorded in roadmap / OPERATIONAL-INDEX |

### Legal transitions

```text
UNCHARTERED
  → CHARTERED                    (this charter pass)
  → READY WITH BLOCKERS          (C8 readiness; blockers remain)
  → remediation packages         (authorized separately)
  → READY FOR EVALUATION         (hard blockers cleared + evidence assembled)
  → EVALUATION ACTIVE            (formal evaluation task opened)
  → PASS | FAIL | DEFERRED | BLOCKED BY AUTHORITY | CONDITIONAL PASS*
  → CLOSED                       (roadmap/index sync + gate REPORT)

* CONDITIONAL PASS only if operator authority explicitly permits before evaluation (§20)
```

### Forbidden transitions

```text
CHARTERED → CLOSED without EVALUATION ACTIVE
READY WITH BLOCKERS → PASS
RPC ≥ 20/32 alone → CLOSED
WF-R01.3.4 COMPLETE → G2 CLOSED
Charter acceptance → G2 ACTIVE (execution lane)
```

### Current state

```text
CHARTERED
READY WITH BLOCKERS
NOT EVALUATED
NOT PASSED
NOT CLOSED
```

---

## 9. G2 Criteria

Extracted from binding authority only.

| Criterion ID | Criterion | Authority | Type | Current state |
|--------------|-----------|-----------|------|---------------|
| **G2-01** | RPC **≥ 20/32** | Coverage Model § Gate table G2; wf-r01-3-4 §16 | NUMERIC | **SATISFIED** — **23/32** |
| **G2-02** | `SERVICES` T1+ partial (W3) | Coverage Model G2 deliverables; program design W3 | STRUCTURAL | **OPEN** — BLOCK-GAPS Not implemented |
| **G2-03** | `TEAM` T1+ partial (W3) | Same | STRUCTURAL | **OPEN** |
| **G2-04** | `ABOUT` T1+ partial (W3) | Same | STRUCTURAL | **OPEN** |
| **G2-05** | `FILTERS` T1+ partial | Coverage Model G2; CATALOG minimum | STRUCTURAL | **SATISFIED** — C2 |
| **G2-06** | `SEARCH` T1+ partial | Same | STRUCTURAL | **SATISFIED** — C3 |
| **G2-07** | Catalog grids W5: `CATEGORIES`, `CATEGORY_GRID`, `PRODUCT_GRID`, `PRODUCT_CARD` | Coverage Model G2; program design W5 | STRUCTURAL | **SATISFIED** — C4A/C4B |
| **G2-08** | PLP scaffold (`CATEGORY_PAGE`) | Coverage Model G2 «PLP scaffold»; wf-r01-3-4 §663 | STRUCTURAL | **SATISFIED** — C5 |
| **G2-09** | PDP / catalog corridor scaffold (`PRODUCT_PAGE`) | C8 G2 audit; wf-r01-3-4 C6 | STRUCTURAL | **SATISFIED** — C6 |
| **G2-10** | PROMO money-page scaffold(s) | Coverage Model G2 «PROMO money-page scaffold»; PROMO minimum scaffolds § PROMO | STRUCTURAL | **OPEN** — no SERVICE/ABOUT/CONTACT scaffolds |
| **G2-11** | CATALOG SC pilot minimum | Coverage Model § CATALOG; wf-r01-3-4 §663 | COVERAGE | **PARTIAL** — SEARCH_RESULTS_PAGE gap |
| **G2-12** | PROMO SC pilot minimum | Coverage Model § PROMO; Template-Art matrix | COVERAGE | **OPEN** — W3 + scaffolds absent |
| **G2-13** | Catalog PC — Reference Composition published | Coverage Model § PC; C5/C6 compositions | COMPOSITIONAL | **SATISFIED** — corridor 1/1 |
| **G2-14** | PROMO PC — money-page compositions | Coverage Model § PROMO scaffolds + compositions | COMPOSITIONAL | **OPEN** |
| **G2-15** | Vertical profile binding (MANUFACTURER / AUTO) | wf-r01-3-4 charter §13; C7 | COMPOSITIONAL | **SATISFIED** — docs published |
| **G2-16** | `HEADER_NAV` T1+ structural | G2 / WF-A03 precondition chain; C2 | STRUCTURAL | **SATISFIED** |
| **G2-17** | `BREADCRUMBS` / `PAGINATION` integration | W4 integration; WF-R01.3.3 | STRUCTURAL | **SATISFIED** |
| **G2-18** | Build PASS in reference workspace | Coverage Model § Gate exit evidence | EVIDENCE | **SATISFIED** for catalog waves |
| **G2-19** | Five-dimension gate evaluation REPORT | wf-r01-3-4 §663–670; G1 precedent G1-7 | EVIDENCE | **OPEN** — no `wf-r01-3*g2*gate*` REPORT |
| **G2-20** | Operator gate sign-off | wf-r01-3-4 §562; C8 §365 | AUTHORITY | **OPEN** |
| **G2-21** | No unauthorized Registry expansion | wf-r01-3-4 §19; charter boundaries | AUTHORITY | **SATISFIED** at C8 |
| **G2-22** | WF-R01.7 interim Template-Art honesty | Coverage Model § Interim policy | QUALITY | **PARTIAL** — multi-type pilot blocked until G2 CLOSED |
| **G2-23** | Handoff package to WF-R01.3.5 / G3 corridor | Program design § R01.3.5 dependency | HANDOFF | **OPEN** — requires G2 CLOSED |

**Note on PROCESS:** Coverage Model PROMO minimum lists `PROCESS` as multi-page content. Wave map W3 assigns **SERVICES, TEAM, ABOUT** only. **PROCESS is not a separate G2-02..04 criterion** — it is **PROMO SC debt** tracked under G2-12 unless a future wave charter elevates it.

---

## 10. Criterion Classification

| Type | Criterion IDs |
|------|---------------|
| **NUMERIC** | G2-01 |
| **STRUCTURAL** | G2-02 – G2-10, G2-16, G2-17 |
| **COMPOSITIONAL** | G2-13 – G2-15 |
| **COVERAGE** | G2-11, G2-12 |
| **EVIDENCE** | G2-18, G2-19 |
| **AUTHORITY** | G2-20, G2-21 |
| **QUALITY** | G2-22 |
| **HANDOFF** | G2-23 |

---

## 11. Hard Blocking Criteria

Without **PASS** on all items below, Gate G2 **must not** receive **PASS** or **CLOSED**.

| ID | Criterion | Current |
|----|-----------|---------|
| G2-02 | `SERVICES` T1+ | OPEN |
| G2-03 | `TEAM` T1+ | OPEN |
| G2-04 | `ABOUT` T1+ | OPEN |
| G2-10 | PROMO money-page scaffold minimum | OPEN |
| G2-11 | CATALOG SC **PASS** | PARTIAL |
| G2-12 | PROMO SC **PASS** | OPEN |
| G2-14 | PROMO PC for money pages | OPEN |
| G2-19 | Dedicated formal gate evaluation REPORT | OPEN |
| G2-20 | Operator gate sign-off | OPEN |

**Already satisfied hard prerequisites (necessary but not sufficient alone):**

G2-01, G2-05 – G2-09, G2-13, G2-15 – G2-18, G2-21.

---

## 12. Conditional Criteria

Criteria that **may** justify **CONDITIONAL PASS** only if operator authority **explicitly permits** that decision class before evaluation.

| Finding | Authority | Default gate effect |
|---------|-----------|---------------------|
| **CONDITIONAL PASS decision class** | **Not explicitly authorized** in Coverage Model or WF-R01.3.4 for G2 | **SAFE UNKNOWN — FORMAL AUTHORITY DECISION REQUIRED** |
| **CATALOG SC PARTIAL** with SEARCH_RESULTS_PAGE unresolved | C8 Decision B; Coverage Model lists scaffold | **Blocks PASS** unless separate **Coverage Model amendment** or **registered page type + scaffold** under authority reconciliation |
| **AUTO profile P2** | C7 honest limits | **Non-blocking** — documented in gate REPORT |
| **PC corridor notation vs per-page_type literal** | C8 metric hygiene note | **Non-blocking** for G2 |

**Default evaluation mode:** binary **PASS / FAIL** mirroring G1 closure precedent unless operator publishes explicit CONDITIONAL PASS policy before evaluation opens.

---

## 13. Non-Blocking Debt

Documented follow-up **must not** block G2 **PASS** once hard criteria are met.

| Finding | Classification | Gate effect | Destination |
|---------|----------------|-------------|-------------|
| AUTO profile P2 — OCPilot binding unverified | Quality debt | None at G2 | WF-R01.8 enrollment |
| PC corridor shorthand vs Coverage Model literal | Metric hygiene | None at G2 | WF-R01.3.X |
| PROCESS partial not in W3 wave map | PROMO SC completeness debt | May affect G2-12 if evaluated strictly | W3 remediation or follow-on wave |
| WF-R01.7 Template-Art matrix pending | Parallel programme debt | None at G2 closure | WF-R01.7 |
| Foreign WIP on branch | Operator lane hygiene | None | Excluded from gate commits |

---

## 14. W3 PROMO Requirement

### What is W3?

**Wave W3** — program-design execution wave assigning PROMO multi-page block partials to Reference Expansion. Canonical W3 `block_id` set in wave map: **SERVICES, TEAM, ABOUT** ([wf-r01-3-reference-expansion-program-design-v1.md](../../reports/wf-r01-3-reference-expansion-program-design-v1.md) § Wave map).

**W3 is not limited to three HTML files in isolation** — it is the **G2 structural deliverable group** for PROMO content blocks. PROMO SC additionally expects **PROCESS** per Coverage Model § PROMO minimum — **cross-track debt** until remediated.

### W3 target table

| W3 target | Registry identity | Current reference state | G2 requirement |
|-----------|-------------------|-------------------------|----------------|
| Services block | `SERVICES` | BLOCK-GAPS: Not implemented | T1+ partial + wave REPORT + build PASS |
| Team block | `TEAM` | BLOCK-GAPS: Not implemented | T1+ partial + wave REPORT + build PASS |
| About block | `ABOUT` | BLOCK-GAPS: Not implemented | T1+ partial + wave REPORT + build PASS |
| Process block | `PROCESS` | T1+ partial **exists** (WF-R01.3.2 W1) | Already satisfied for partial; included in PROMO SC checklist |

**G2 hard requirement for W3 wave map:** **G2-02, G2-03, G2-04** — all **OPEN**.

**Remediation owner lane:** separate **W3 PROMO Reference Completion** task — **not** WF-R01.3.4 catalog lane.

---

## 15. PROMO Scaffold Requirement

### Applicable page types

From Coverage Model § PROMO minimum scaffolds (registered in PAGE-TYPE-REGISTRY-v1):

| `page_type` | Site-type consumer | Shell matrix |
|-------------|-------------------|--------------|
| `SERVICE_PAGE` | PROMO money page | [page-type-shell-matrix-v1.md](page-type-shell-matrix-v1.md) |
| `ABOUT_PAGE` | PROMO / corporate route | Same |
| `CONTACT_PAGE` | PROMO contact hub | Same |

### Required scaffolds for G2

| Authority layer | Requirement |
|-----------------|-------------|
| Coverage Model G2 gate table | «PROMO money-page scaffold» (singular) |
| Coverage Model § PROMO minimum | **`SERVICE_PAGE`, `ABOUT_PAGE`, `CONTACT_PAGE`** scaffolds |
| wf-r01-3-4 §663 | «PROMO scaffolds» plural per Coverage Model |

**Charter reconciliation:** G2 **PASS** requires **all three** registered PROMO primary money-page scaffolds with:

- Buildable reference page per [reference-scaffold-contract-v1.md](reference-scaffold-contract-v1.md)
- Published scaffold manifest
- Published Reference Composition (**G2-14**)
- Stub honesty where partials missing

**One scaffold alone is insufficient** for honest G2 closure against Coverage Model § PROMO minimum.

### Coverage implication

| Dimension | Expected accrual on remediation |
|-----------|--------------------------------|
| **RSC** | Up to **+3** global (SERVICE, ABOUT, CONTACT) if validated |
| **SC** | **PROMO PASS** when PROMO minimum set complete |
| **PC** | Up to **+3** page-type compositions |
| **RPC** | No change from scaffolds alone — W3 partials drive RPC |

### Current state

**RSC 3/10** — only LANDING, CATEGORY_PAGE, PRODUCT_PAGE. **No PROMO money-page scaffolds.**

---

## 16. CATALOG SC Requirement

### Current state

**CATALOG SC = PARTIAL** ([wf-r01-3-4-wave-c8-exit-g2-readiness-v1.md](../../reports/wf-r01-3-4-wave-c8-exit-g2-readiness-v1.md) §13)

### Required state for CATALOG SC PASS

Per Coverage Model § CATALOG minimum + C8 criterion audit:

| Criterion | State |
|-----------|-------|
| HEADER_NAV, SEARCH, FILTERS structural | PASS |
| CATEGORIES, CATEGORY_GRID, PRODUCT_GRID, PRODUCT_CARD | PASS |
| BREADCRUMBS, PAGINATION | PASS |
| FOOTER / LEGAL_LINKS shell | PASS |
| CATEGORY_PAGE scaffold | PASS |
| PRODUCT_PAGE scaffold | PASS |
| Vertical profile binding | PASS |
| **`SEARCH_RESULTS_PAGE` scaffold** | **FAIL** — no Registry row · no scaffold |
| Formal SC evaluation in gate REPORT | Required at evaluation |

### Missing evidence

1. **`SEARCH_RESULTS_PAGE` scaffold** — listed in Coverage Model CATALOG minimum; absent from PAGE-TYPE-REGISTRY minimum 10
2. **Operator resolution** — register page type + scaffold **or** amend Coverage Model under separate authority **or** documented exception policy (§17)

### Gate effect

**G2-11 hard blocker** — CATALOG SC **PASS** required for G2 **PASS** per wf-r01-3-4 §663–670.

---

## 17. SEARCH_RESULTS_PAGE Authority Policy

| Field | Value |
|-------|-------|
| **Coverage Model wording** | CATALOG minimum scaffolds include `` `SEARCH_RESULTS_PAGE` `` |
| **PAGE-TYPE-REGISTRY v1** | **Not in** minimum 10 registered types |
| **Vocabulary Canon** | `` `SEARCH_RESULTS_PAGE` `` = **expansion vocabulary (glossary-only until WF-R01.6)** |
| **WF-R01.3.4 charter** | Deferred — future extension; document route until row exists |
| **Global Shell Contract** | Planned reference note only — not active Registry identity |
| **C8 Decision B** | Future glossary candidate; **blocks CATALOG SC PASS**; **does not block WF-R01.3.4 exit** |

### G2 charter policy

| Question | Answer |
|----------|--------|
| Blocks G2 **PASS**? | **Yes** — via **G2-11 CATALOG SC PASS** until resolved |
| Separate authority reconciliation allowed? | **Yes** — remediation package G2-R3; may route through **WF-R01.6** hygiene |
| Is CATALOG SC PARTIAL sufficient for conditional gate? | **Only if** operator publishes explicit CONDITIONAL PASS policy — **default: No** |
| Is conditional gate authorized? | **SAFE UNKNOWN — FORMAL AUTHORITY DECISION REQUIRED** |
| Who may create page-type candidate? | **WF-R01.6** Blueprint & Registry Hygiene Pass territory — **not** G2 evaluation task |
| Must wait for WF-R01.6? | **Preferred** — not mandatory if dedicated reconciliation charter accepted first |
| Hard blocker or programme debt? | **Hard blocker for CATALOG SC PASS** · **programme debt for WF-R01.3.4 exit** (already transferred) |

**Forbidden in G2 evaluation without authority:** auto-creating PAGE-TYPE-REGISTRY row, scaffold, or Coverage Model edit during evaluation pass.

---

## 18. Evidence Package Contract

| Evidence | Required | Owner / source | Validation |
|----------|----------|----------------|------------|
| **G2 charter (this document)** | Yes | WF-R01.3 G2 charter pass | ACCEPTED status |
| **Criteria matrix** | Yes | §9 of this charter | All IDs mapped |
| **Current coverage snapshot** | Yes | C8 exit REPORT + git HEAD | Five dimensions stated |
| **Registry evidence** | Yes | BLOCK-REGISTRY-v1 · PAGE-TYPE-REGISTRY-v1 | Row counts unchanged unless authorized remediation |
| **Partial reference evidence** | Yes | `src/partials/` + wave REPORTs | T1+ inventory |
| **Scaffold manifests** | Yes | `*-SCAFFOLD-MANIFEST-v1.md` | Per reference-scaffold-contract |
| **Composition documents** | Yes | `*-REFERENCE-COMPOSITION-v1.md` | PC claims |
| **Build evidence** | Yes | `npm run build` exit 0 | Reference workspace |
| **SC / PC evaluation** | Yes | Coverage Model checklists | LANDING · PROMO · CATALOG |
| **Remaining-debt register** | Yes | Gate evaluation REPORT | Hard vs non-blocking |
| **Formal gate evaluation REPORT** | Yes | `reports/wf-r01-3-g2-formal-gate-pass-v1.md` (future) | Operator sign-off |
| **Roadmap / index updates** | Yes | roadmap.md · OPERATIONAL-INDEX.md | Gate state sync |
| **Git checkpoint** | Yes | Selective commit on evaluation pass | No foreign WIP |

---

## 19. Formal Evaluation Procedure

Remediation **forbidden** inside formal evaluation except where a **separately authorized** remediation task explicitly permits in-place fix (default: **forbidden**).

1. **Authority preflight** — confirm this charter ACCEPTED; no competing G2 charter; Registry/Coverage Model unchanged since readiness snapshot unless remediation REPORT says otherwise
2. **Git / state freeze** — record branch, HEAD, staged scope; exclude foreign WIP
3. **Evidence inventory** — assemble §18 package; mark missing items **FAIL** inputs
4. **Criterion-by-criterion audit** — evaluate G2-01..G2-23 with PASS/FAIL/PARTIAL/N/A; cite evidence paths
5. **Coverage reconciliation** — RC, RPC, RSC, SC, PC manual count; no unauthorized accrual
6. **Blocking-debt evaluation** — classify open items per §11–§13
7. **Gate decision** — select from §20; **default PASS only if all hard blockers PASS**
8. **Roadmap / index update** — sync gate state; **never** CLOSED without decision
9. **Selective Git checkpoint** — gate REPORT + index/roadmap only
10. **Handoff** — §26 successor or remediation destination

---

## 20. Allowed Gate Decisions

| Decision | Meaning | Required condition | Programme effect |
|----------|---------|-------------------|------------------|
| **PASS** | G2 hard criteria met | All §11 items PASS; G2-19 REPORT published; operator sign-off | G2 **CLOSED**; unlocks WF-R01.3.5 charter pass eligibility; WF-A03 **recommended precondition satisfied** (no auto-start); Template-Art **pilot** PROMO + CATALOG per Coverage Model |
| **CONDITIONAL PASS** | Partial gate with documented waivers | **Not binding-authorized** — requires explicit pre-evaluation operator policy | **SAFE UNKNOWN** — do not use to bypass §11 hard blockers without published waiver authority |
| **FAIL** | Audit complete; hard criteria not met | One or more §11 items FAIL after evidence review | G2 remains **NOT CLOSED**; remediation packages required; retest after remediation |
| **DEFERRED** | Evaluation not performed | Operator postpones evaluation | No gate state change beyond DEFERRED notation; remediation continues |
| **BLOCKED BY AUTHORITY** | Normative conflict | Irreconcilable Coverage Model vs Registry vs charter conflict without reconciliation path | Stop evaluation; authority reconciliation required (G2-R3 or WF-R01.6) |

---

## 21. Decision Semantics

### PASS

All hard blocking criteria (§11) evaluate **PASS**. Five-dimension metrics recorded. Formal REPORT published. Roadmap records **G2 — CLOSED**.

### CONDITIONAL PASS

**Reserved vocabulary only.** Binding authority for G2 does **not** define CONDITIONAL PASS (contrast: G1 used binary **G1 CLOSED** on all PASS). Before any CONDITIONAL PASS decision:

```text
SAFE UNKNOWN — FORMAL AUTHORITY DECISION REQUIRED
```

Operator must publish waiver scope, remaining debt, and forbidden claims **before** evaluation opens.

### FAIL

Evidence reviewed; one or more hard criteria **FAIL**. No G2 CLOSED. Destination: remediation packages §22.

### DEFERRED

Evaluation task aborted or not started. Gate remains **CHARTERED** / **READY WITH BLOCKERS**.

### BLOCKED BY AUTHORITY

Example trigger: SEARCH_RESULTS_PAGE irreconcilable without WF-R01.6 but evaluation forced to PASS — **stop** and route to G2-R3.

---

## 22. Remediation Packages

Proposed package IDs — **charter vocabulary** for separate tasks; **not executed** by this charter.

| Package | Purpose | Type | Gate criteria addressed | Implementation allowed |
|---------|---------|------|-------------------------|------------------------|
| **G2-R1** | W3 PROMO Reference Completion | Implementation + REPORT | G2-02, G2-03, G2-04; feeds G2-12 | `SERVICES`, `TEAM`, `ABOUT` partials only under future ACCEPTED wave charter |
| **G2-R2** | PROMO Money-Page Scaffold Completion | Implementation + REPORT | G2-10, G2-14, G2-12 | SERVICE/ABOUT/CONTACT scaffolds + compositions + manifests |
| **G2-R3** | SEARCH_RESULTS_PAGE Authority Reconciliation | Authority / doc | G2-11 prerequisite | Registry row **or** Coverage Model amendment **or** formal exception — **no** silent skip |
| **G2-R4** | CATALOG SC Completion or Exception Decision | Evaluation / authority | G2-11 | Depends on G2-R3 outcome; may include scaffold build if authority adds page type |
| **G2-R5** | Gate Evidence Assembly | Doc-only | G2-19, G2-18 | Inventory + preflight; **no** criterion fabrication |

**Preferred first package:** **G2-R1** — first hard blocker in dependency order (§23).

---

## 23. Remediation Dependencies

### Sequence

```text
G2-R1  W3 PROMO references (SERVICES · TEAM · ABOUT)
  → G2-R2  PROMO money-page scaffolds + compositions
  → coverage recalculation (RPC / RSC / SC / PC — in wave REPORTs)
  → G2-R3  SEARCH_RESULTS_PAGE authority reconciliation
  → G2-R4  CATALOG SC completion or formal exception
  → G2-R5  Gate evidence assembly
  → formal G2 evaluation (separate task — NOT this charter)
  → G2 decision → CLOSED
```

### Parallelizable work

| Track | May parallelize with |
|-------|---------------------|
| G2-R1 W3 partials | G2-R3 authority reconciliation (doc-only phase) |
| G2-R3 authority | G2-R1 if reconciliation stays doc-only |
| G2-R5 evidence assembly | Late remediation only — after R1–R4 evidence exists |

**Not parallelizable:** G2-R2 before G2-R1 (partial dependencies for honest PROMO scaffolds); G2-R4 before G2-R3 resolution path chosen; formal evaluation before G2-R5.

### Formal evaluation trigger

All §11 hard blockers **PASS** or explicitly waived under published CONDITIONAL PASS policy (if ever authorized).

---

## 24. Ownership and Approval

| Role | Assignment |
|------|------------|
| **Normative owner** | Website Factory operator governance (human-operated) |
| **Evidence owner** | Operator executing remediation / evaluation passes |
| **Evaluator** | Operator performing formal G2 evaluation task |
| **Approval authority** | Human operator sign-off recorded in formal gate REPORT |
| **Named steward** | **SAFE UNKNOWN — named steward not assigned** |
| **Who may record PASS / CLOSED** | Human operator via accepted formal gate evaluation REPORT + roadmap/index sync — **not** charter pass alone |
| **Human approval required** | **Yes** — mirroring G1 closure pattern |

---

## 25. Coverage Freeze

Charter acceptance **does not** change coverage metrics.

| Dimension | Frozen value |
|-----------|--------------|
| **RC** | **32/32** |
| **RPC** | **23/32** |
| **RSC** | **3/10 global** · **1/1 LANDING · 1/1 CATEGORY_PAGE · 1/1 PRODUCT_PAGE** |
| **SC** | **LANDING PASS · CATALOG PARTIAL** |
| **PC** | **1/1 LANDING · 1/1 CATALOG corridor** |

**No-accrual confirmation:** This charter pass awards **zero** RPC, RSC, SC, or PC credit.

---

## 26. Successor and Failure Handoff

### After G2 PASS

| Destination | Authority |
|-------------|-----------|
| **WF-R01.3.5** — Corporate & Commerce Reference Slices | Program design § R01.3.5 — depends on R01.3.4 Gate 2 minimum |
| **G3 planning corridor** | Coverage Model G3 RPC **29/32** target |
| **WF-A03** | **Recommended precondition satisfied** — **auto-start forbidden** |
| **Template-Art pilot** | PROMO + CATALOG per Coverage Model matrix |

### After CONDITIONAL PASS (if ever authorized)

Restrictions **must** be enumerated in operator policy — default **not authorized**. WF-R01.3.5 and WF-A03 remain **blocked** for waived criteria until debt closed.

### After FAIL

Return to remediation packages §22; repeat evaluation after evidence refresh; **no** roadmap G2 CLOSED.

### After DEFERRED

No successor unlock; next task = highest-priority open remediation package.

### After BLOCKED BY AUTHORITY

Route to **G2-R3** and/or **WF-R01.6**; evaluation retried only after reconciliation REPORT ACCEPTED.

---

## 27. Out of Scope

- G2 evaluation execution
- G2 PASS / CLOSED declaration in this pass
- W3 / PROMO / SEARCH_RESULTS implementation
- Registry, Coverage Model, Vocabulary Canon edits
- WF-R01.3.5, WF-A03, Pixel Factory
- Metric mutation
- Historical report rewrites

---

## 28. Acceptance Criteria

This charter is **ACCEPTED** because:

- [x] Canonical Gate G2 identity confirmed
- [x] No duplicate accepted G2 charter on disk
- [x] Full criteria extracted with authority citations
- [x] Hard / conditional / non-blocking classification published
- [x] W3, PROMO scaffold, CATALOG SC, SEARCH_RESULTS_PAGE policies defined
- [x] Evidence contract and evaluation procedure published
- [x] Decision model published with CONDITIONAL PASS honesty boundary
- [x] Remediation packages and order defined
- [x] Coverage freeze confirmed
- [x] Ownership defined or SAFE UNKNOWN stated
- [x] Successor / failure handoff defined
- [x] Charter acceptance separated from gate pass

---

## 29. Known Debt and SAFE UNKNOWN

| Item | Status |
|------|--------|
| CONDITIONAL PASS authorization for G2 | **SAFE UNKNOWN — FORMAL AUTHORITY DECISION REQUIRED** |
| Named steward | **SAFE UNKNOWN — named steward not assigned** |
| SEARCH_RESULTS_PAGE resolution path | **OPEN** — G2-R3 / WF-R01.6 |
| PROCESS in PROMO SC vs W3 scope | **Documented debt** — PROCESS partial exists; PROMO SC still OPEN |
| Single vs triple PROMO scaffold in G2 gate table wording | **Reconciled** — Coverage Model § PROMO minimum controls (§15) |

---

## 30. Evidence Paths

```text
projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md
reports/wf-r01-3-g2-formal-gate-pass-charter-pass-v1.md
projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md
projects/mars-website-factory/wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md
reports/wf-r01-3-4-wave-c8-exit-g2-readiness-v1.md
reports/wf-r01-3-reference-expansion-program-design-v1.md
reports/wf-r01-3-post-g1-track-selection-v1.md
reports/wf-r01-3-2-g1-five-dimension-exit-v1.md
projects/mars-website-factory/global-shell-contract-v1.md
projects/mars-website-factory/page-type-shell-matrix-v1.md
projects/mars-website-factory/reference-scaffold-contract-v1.md
projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md
projects/mars-website-factory/roadmap.md
projects/mars-website-factory/OPERATIONAL-INDEX.md
workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md
workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md
workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md
workspaces/website-factory-reference-v1/page-architecture/CATEGORY-PAGE-SCAFFOLD-MANIFEST-v1.md
workspaces/website-factory-reference-v1/page-architecture/PRODUCT-PAGE-SCAFFOLD-MANIFEST-v1.md
workspaces/website-factory-reference-v1/page-architecture/CATEGORY-PAGE-REFERENCE-COMPOSITION-v1.md
workspaces/website-factory-reference-v1/page-architecture/PRODUCT-PAGE-REFERENCE-COMPOSITION-v1.md
```

---

## 31. Decision

**Decision:** **ACCEPTED** — WF-R01.3 Gate G2 Formal Gate Pass Charter v1 is normative operator authority for future formal Gate G2 evaluation.

**Gate state after decision:**

```text
CHARTERED
READY WITH BLOCKERS
NOT EVALUATED
NOT PASSED
NOT CLOSED
```

**Next programme task (remediation — not executed here):**

```text
WF-R01.3 G2 Remediation — W3 PROMO Reference Completion Charter Pass
```

---

*Canonical gate charter: `projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md` · v1 · 2026-06-20*
