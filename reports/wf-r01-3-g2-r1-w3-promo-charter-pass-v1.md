# REPORT — WF-R01.3 G2-R1 W3 PROMO REFERENCE COMPLETION CHARTER PASS

**Artifact ID:** WF-R01.3 G2-R1 W3 PROMO Reference Completion Charter Pass (v1)  
**Date:** 2026-06-20  
**Branch:** `mars/post-cycle8-live-tests`  
**Mode:** charter pass — **documentation-only** · **not** W3 implementation · **not** G2 evaluation

---

## 1. Result

| Field | Value |
|-------|-------|
| **Status** | **COMPLETE** |
| **Charter decision** | **ACCEPTED** |
| **Charter path** | `projects/mars-website-factory/wf-r01-3-g2-r1-w3-promo-reference-completion-charter-v1.md` |
| **Package identity** | **G2-R1** — **W3 PROMO Reference Completion** |
| **W3 scope** | **SERVICES · TEAM · ABOUT** (`PROCESS` excluded — existing reference) |
| **RC** | **32/32** — **UNCHANGED** |
| **RPC** | **23/32** — **UNCHANGED** |
| **RSC** | **3/10 global** · **1/1 LANDING · 1/1 CATEGORY_PAGE · 1/1 PRODUCT_PAGE** — **UNCHANGED** |
| **SC** | **LANDING PASS · CATALOG PARTIAL** — **UNCHANGED** |
| **PC** | **1/1 LANDING corridor · 1/1 CATALOG corridor** — **UNCHANGED** |
| **Package state** | **CHARTERED · NOT IMPLEMENTED · NOT COMPLETE** |
| **G2 state** | **CHARTERED · READY WITH BLOCKERS · NOT EVALUATED · NOT PASSED · NOT CLOSED** |
| **Next task** | **WF-R01.3 G2-R1 W3-A — PROMO Source Inventory and Contract Confirmation** |

---

## 2. Git Safety

| Check | Result |
|-------|--------|
| **Branch** | `mars/post-cycle8-live-tests` |
| **HEAD before task** | `5f4d85b` — `docs: finalize WF-R01.3 G2 charter pass report git section` |
| **HEAD contains f3b7a79 and 5f4d85b** | **Confirmed** |
| **G2 charter remote state** | `origin/mars/post-cycle8-live-tests` at `5f4d85b` — G2 charter present |
| **Staged files (at start)** | **None** |
| **Foreign WIP** | **Present** — MIG pilots, EAR, OCPilot, Triumph workspaces, `.recovery-temp`, unrelated edits — **excluded** |
| **Selective scope** | G2-R1 charter · charter pass REPORT · roadmap · OPERATIONAL-INDEX |

---

## 3. Authority Reviewed

| Document | Path | Role |
|----------|------|------|
| G2 formal gate charter | `projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md` | Parent gate; G2-R1 definition |
| G2 charter pass REPORT | `reports/wf-r01-3-g2-formal-gate-pass-charter-pass-v1.md` | Readiness snapshot |
| WF-R01.3 program design | `reports/wf-r01-3-reference-expansion-program-design-v1.md` | Wave map W3 |
| WF-R01 program design | `reports/foundry-registry-expansion-program-design-v1.md` | Subprogram map |
| Post-G1 track selection | `reports/wf-r01-3-post-g1-track-selection-v1.md` | G2 composite semantics |
| Coverage Model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | RPC/RSC/SC/PC; G2 deliverables |
| Vocabulary Canon | `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` | F3 block family |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Shell order |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | PROMO page types |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | Scaffold vs host |
| Block Registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | 32 rows |
| Core Block Library | `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md` | Inventory |
| Block Gaps | `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md` | W3 gaps |
| Page-Type Registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` | RSC denominator |
| Site-Type Registry | `workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md` | PROMO / CORPORATE |
| C8 G2 readiness | `reports/wf-r01-3-4-wave-c8-exit-g2-readiness-v1.md` | Blocker inventory |
| Catalog inventory precedent | `projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md` | Q0–Q3 discipline |
| Roadmap | `projects/mars-website-factory/roadmap.md` | Programme sync |
| OPERATIONAL-INDEX | `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Operator entry |

---

## 4. Duplicate Charter Check

| Field | Value |
|-------|-------|
| **Search terms** | w3-promo · promo-reference-completion · services-team-about · g2-r1 · w3-charter · promo-block-reference |
| **Existing documents** | G2 charter §22 remediation table only; program design W3 wave map — **no prior accepted G2-R1 charter** |
| **Competing authority** | **None** |
| **Decision** | **PROCEED** — publish canonical G2-R1 charter |

| Artefact | Classification |
|----------|----------------|
| `wf-r01-3-g2-formal-gate-pass-charter-v1.md` §22 | **ACCEPTED** — parent remediation vocabulary |
| Program design W3 table | **DESIGN** — aligned |
| C8 G2 readiness REPORT | **REPORT** — complementary |
| Catalog reference inventory | **SOURCE INVENTORY** — precedent for W3-A |

---

## 5. Package Identity

| Field | Value |
|-------|-------|
| **Package ID** | **G2-R1** |
| **Canonical name** | **W3 PROMO Reference Completion** |
| **Parent programme** | **WF-R01.3** Reference Implementation Expansion |
| **Parent gate** | **G2** — PROMO + CATALOG scaffold |
| **Purpose** | Close G2-02..04 via T1+ partials for SERVICES, TEAM, ABOUT |
| **Charter/implementation distinction** | Charter ACCEPTED ≠ W3 built ≠ RPC accrued ≠ G2 PASS |

---

## 6. W3 Scope Confirmation

| Target | Registry identity | Included | Reason |
|--------|-------------------|----------|--------|
| **SERVICES** | `SERVICES` | **Yes** | W3 wave map; G2-02 OPEN |
| **TEAM** | `TEAM` | **Yes** | W3 wave map; G2-03 OPEN |
| **ABOUT** | `ABOUT` | **Yes** | W3 wave map; G2-04 OPEN |
| **PROCESS** | `PROCESS` | **No** | T1+ exists — WF-R01.3.2 Wave A2 |

---

## 7. Registry Preflight

| Target | Family | Tier | RC member | Current reference | RPC eligibility |
|--------|--------|------|-----------|-------------------|-----------------|
| **SERVICES** | F3 · COMPANY | T1+ target | Yes | Not implemented | **Eligible** on T1+ |
| **TEAM** | F3 · COMPANY | T1+ target | Yes | Not implemented | **Eligible** on T1+ |
| **ABOUT** | F3 · COMPANY | T1+ target | Yes | Not implemented | **Eligible** on T1+ |

**Verdict:** **IMPLEMENTATION ELIGIBLE** — no reconciliation STOP required.

---

## 8. Coverage Expectation

| Field | Value |
|-------|-------|
| **Before** | RC **32/32** · RPC **23/32** · RSC **3/10** · SC **LANDING PASS · CATALOG PARTIAL** · PC **1/1 · 1/1** |
| **Potential deltas** | RPC **+3** max (one per T1+ partial) |
| **Expected maximum** | RPC **26/32** if all three complete |
| **Charter freeze** | All dimensions **UNCHANGED** at charter acceptance |
| **No-double-count** | Variations, subsections, host, inventory, charter → **0** RPC |

---

## 9. Vocabulary Lock

### SERVICES

Registry: present service/product lines with drill-down to money pages. Charter lock: service directions collection; internal items only; excludes PROCESS, PRICING, FAQ, LEAD_FORM, CTA, catalog blocks.

### TEAM

Registry: leadership and staff presentation. Charter lock: member items with fictional data; excludes ABOUT narrative, CONTACTS, TESTIMONIALS, TRUST.

### ABOUT

Registry: entity narrative, history, mission. Charter lock: identity + narrative + highlights; not a container for TEAM/PROCESS/TRUST.

### PROCESS exclusion

`process.html` T1+ exists; PROMO SC debt remains for scaffolds; **not** G2-R1 implementation.

---

## 10. Block Boundary Matrix

Published in charter §12 — ownership split confirmed for service directions, people, company identity, workflow (`PROCESS`), proof (`TRUST`/cases), contacts, lead capture, CTA.

---

## 11. Site-Type Applicability

Published in charter §13 — SERVICES/ABOUT **REQ** on PROMO/CORPORATE; TEAM **OPT**; all **FORBIDDEN** on LANDING/CATALOG/ECOMMERCE per SITE-TYPE-BLOCK-MATRIX-v2.

---

## 12. Page-Type Applicability

Published in charter §14 — SERVICES on PROMO/CORPORATE HOME; ABOUT **REQ** on ABOUT_PAGE; TEAM **OPT** on ABOUT_PAGE; FORB on LANDING and catalog types.

---

## 13. Source Policy

- **Allowed:** Factory references, execution-case artefacts (Triumph v6 doc-first), sanitized locals, approved prototypes, research structure
- **Rejected:** client contacts, production URLs, real employee data/portraits, commercial claims, CMS/backend, unsanitized project naming
- **Sanitization:** fictional copy required for all three targets
- **Source quality model:** Q3 / Q2 / Q1 / Q0 / SAFE UNKNOWN — catalog inventory precedent

---

## 14. Source Inventory Requirement

- **Required output:** W3-A inventory v1 with per-target candidate, quality, reusable structure, rejected content
- **Candidate classes:** Triumph v6 (primary probe), Factory patterns (secondary)
- **Quality classification:** Q0–Q3 per target
- **Acceptance:** W3-A REPORT + inventory doc; metrics unchanged; contracts confirmed or amended in REPORT only

---

## 15. SERVICES Contract

Purpose: service directions on PROMO/CORPORATE. Semantic section + collection + ≥2 items with title/description. One variation canonicalized at implementation. No JS default. a11y/responsive minimum in charter §17.

---

## 16. TEAM Contract

Purpose: people/roles. Member collection + fictional names + placeholder portraits. Privacy policy binding. No profile-card Registry ID. No JS default.

---

## 17. ABOUT Contract

Purpose: org identity narrative. Lead + narrative + ≥2 highlights. Optional media/link. No embedded TEAM/PROCESS/TRUST. No JS default.

---

## 18. JavaScript Policy

Default **no JS** for all three. Forbidden: carousel-only, filtering, modals, network, analytics.

---

## 19. Bounded Host Strategy

**Option A selected** — single `promo-block-references.html` (future). Not scaffold; not RSC/PC/SC evidence; independent section hooks.

---

## 20. Registry and T1+ Contract

Mapping docs: BLOCK-REGISTRY, CORE-BLOCK-LIBRARY, BLOCK-GAPS. Evidence: partial + SCSS + host + build + REPORT + provenance. RPC +1 per complete target only. **No new IDs.**

---

## 21. Implementation Waves

| Wave | Purpose | Type | Expected output |
|------|---------|------|-----------------|
| **W3-A** | Source inventory | Doc | Inventory v1 + REPORT |
| **W3-B** | SERVICES partial | Implementation | T1+ partial + RPC +1 max |
| **W3-C** | TEAM partial | Implementation | T1+ partial + RPC +1 max |
| **W3-D** | ABOUT partial | Implementation | T1+ partial + RPC +1 max |
| **W3-E** | Exit / G2-R2 readiness | Doc | Exit REPORT |

**First wave:** **W3-A** — no published W3 inventory at charter T0.

---

## 22. G2-R1 Exit Criteria

SERVICES/TEAM/ABOUT **PARTIAL** T1+; RPC reconciled (max **26/32**); provenance; registry updated; build PASS; host validated; W3-E REPORT; G2-R2 readiness evaluated; G2 still not closed.

---

## 23. G2-R2 Handoff

Inputs: three partials + existing PROCESS + coverage snapshot. Remaining: SERVICE/ABOUT/CONTACT scaffolds, compositions, CONTACTS/LEAD_FORM money-page dependencies.

---

## 24. Files Created

| File | Purpose |
|------|---------|
| `projects/mars-website-factory/wf-r01-3-g2-r1-w3-promo-reference-completion-charter-v1.md` | Canonical G2-R1 charter |
| `reports/wf-r01-3-g2-r1-w3-promo-charter-pass-v1.md` | This charter pass REPORT |

---

## 25. Files Modified

| File | Change |
|------|--------|
| `projects/mars-website-factory/roadmap.md` | G2-R1 ACCEPTED row; next task W3-A |
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` | G2-R1 status sync |

---

## 26. Validation

| Check | Result |
|-------|--------|
| W3 identity | **PASS** — SERVICES + TEAM + ABOUT |
| Registry rows | **PASS** — three existing IDs |
| PROCESS exclusion | **PASS** |
| Vocabulary boundaries | **PASS** — no REG-VOC conflict |
| Applicability matrices | **PASS** — existing registries used |
| Source policy | **PASS** — no production transfer |
| Coverage freeze | **PASS** — unchanged |
| No implementation | **PASS** — no src/ edits |
| No false completion | **PASS** — no PARTIAL/COMPLETE claims for W3 |

---

## 27. Documentation State

| Item | State |
|------|-------|
| **roadmap** | G2-R1 **ACCEPTED** · **CHARTERED · NOT IMPLEMENTED** |
| **OPERATIONAL-INDEX** | Synced |
| **Package state** | **CHARTERED · NOT IMPLEMENTED · NOT COMPLETE** |
| **G2 state** | **READY WITH BLOCKERS · NOT EVALUATED** |
| **Next task** | **W3-A** |

---

## 28. Git Result

| Field | Value |
|-------|-------|
| **Commit hash** | *(populated after commit)* |
| **Commit message** | `foundry: accept G2-R1 W3 promo reference charter` |
| **Push result** | *(populated after push)* |
| **Files committed** | 4 selective paths only |
| **No foreign lane** | **Confirmed** at staging review |

---

## 29. Drift and Risks

| Severity | Finding | Effect | Destination |
|----------|---------|--------|-------------|
| Medium | No W3 source inventory yet | W3-B cannot start without W3-A | **W3-A** |
| Low | Triumph v6 auto-canonicalization risk | Wrong copy/scope if unsanitized | W3-A + extraction discipline |
| Low | PROCESS vs W3 scope confusion | Operator may duplicate work | Charter §8/§11 lock |
| Info | BZPM W3 blueprint date unknown | Secondary source uncertainty | W3-A SAFE UNKNOWN row |
| Info | PROMO SC still OPEN after G2-R1 | G2 not closable | **G2-R2** + G2 evaluation |

---

## 30. Final Status

```text
COMPLETE
```

---

## 31. Next Task

```text
WF-R01.3 G2-R1 W3-A — PROMO Source Inventory and Contract Confirmation
```

**Not executed in this pass.**

---

## 32. Exact Evidence Paths

```text
projects/mars-website-factory/wf-r01-3-g2-r1-w3-promo-reference-completion-charter-v1.md
reports/wf-r01-3-g2-r1-w3-promo-charter-pass-v1.md
projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md
reports/wf-r01-3-g2-formal-gate-pass-charter-pass-v1.md
projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md
projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md
reports/wf-r01-3-reference-expansion-program-design-v1.md
reports/foundry-registry-expansion-program-design-v1.md
reports/wf-r01-3-post-g1-track-selection-v1.md
projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md
reports/wf-r01-3-4-wave-c8-exit-g2-readiness-v1.md
workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md
workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md
workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md
workspaces/website-factory-reference-v1/block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md
workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md
workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md
workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md
projects/mars-website-factory/global-shell-contract-v1.md
projects/mars-website-factory/page-type-shell-matrix-v1.md
projects/mars-website-factory/reference-scaffold-contract-v1.md
projects/mars-website-factory/roadmap.md
projects/mars-website-factory/OPERATIONAL-INDEX.md
```

---

## 33. Stop Confirmation

```text
W3 implementation: NOT STARTED
SERVICES partial: NOT CREATED
TEAM partial: NOT CREATED
ABOUT partial: NOT CREATED
PROMO scaffolds: NOT CREATED
G2-R1 exit: NOT STARTED
G2 formal evaluation: NOT EXECUTED
G2 PASS: NOT GRANTED
Registry: NOT MODIFIED
Coverage metrics: UNCHANGED
Implementation files: NOT MODIFIED
Production readiness: NOT CLAIMED
```
