# WF-R01.3 Post-G3 Lifecycle Decision v1

**Status:** **PUBLISHED** · **LIFECYCLE DECISION RECORDED**  
**Date:** 2026-06-22  
**Mode:** programme-lifecycle-decision-only · pilot-readiness-authorization-only · documentation-only  
**Honesty boundary:** Records post-G3 lifecycle decision after Gate G3 closure. **Not** Pilot Readiness implementation. **Not** pilot workspace creation. **Not** G4 start. **Not** WF-R01.3 programme closure. **Not** production readiness. **Not** debt resolution.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Programme** | **WF-R01.3** — Reference Implementation Expansion |
| **Lifecycle decision** | **PROCEED TO PILOT READINESS** |
| **G4 decision** | **DEFERRED · NOT STARTED** |
| **Programme state** | **OPEN** · **DESIGN** · **CONTINUES** |
| **Gate G3** | **CLOSED** · **PASS WITH RECORDED NON-BLOCKING DEBT** |
| **WF-R01.3.5** | **COMPLETE** |
| **Pilot Readiness stage** | **WF-PR01** — **AUTHORIZED · NOT STARTED** |
| **Decision task** | **COMPLETE** |
| **Next task** | **WF-PR01-A — Pilot Readiness Contract and First Pilot Launch Boundary** — **NOT STARTED** |

---

## 2. Programme Identity

| Field | Value |
|-------|-------|
| **Programme ID** | **WF-R01.3** |
| **Canonical name** | Reference Implementation Expansion |
| **Program parent** | **WF-R01** — FOUNDRY Registry Expansion Program (**CHARTERED**) |
| **Current lifecycle** | **OPEN** · **DESIGN** · **CONTINUES** |
| **Closed gate** | **G3** — ECOMMERCE + CORPORATE reference slice |
| **Deferred gate** | **G4** — Full Core reference |
| **New bounded stage** | **WF-PR01** — Website Factory Pilot Readiness |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| G3 formal evaluation | [wf-r01-3-g3-formal-evaluation-decision-v1.md](wf-r01-3-g3-formal-evaluation-decision-v1.md) | G3-F technical baseline — **unchanged** |
| G3 gate closure | [wf-r01-3-g3-gate-closure-decision-v1.md](wf-r01-3-g3-gate-closure-decision-v1.md) | Operator sign-off · G3 CLOSED · WF-R01.3.5 COMPLETE |
| G3 evidence pack | [wf-r01-3-g3-evidence-pack-v1.md](wf-r01-3-g3-evidence-pack-v1.md) | Evidence baseline |
| WF-R01.3.5 charter | [wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md](wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md) | G3 delivery scope |
| Post-G2 lifecycle (precedent) | [wf-r01-3-post-g2-lifecycle-decision-v1.md](wf-r01-3-post-g2-lifecycle-decision-v1.md) | Prior lifecycle decision pattern |
| G2 operator closure (precedent) | [wf-r01-3-g2-operator-sign-off-and-gate-closure-v1.md](wf-r01-3-g2-operator-sign-off-and-gate-closure-v1.md) | Operator sign-off precedent |
| Coverage Model | [wf-r01-3-1-coverage-model-charter-v1.md](wf-r01-3-1-coverage-model-charter-v1.md) | Five dimensions — **unchanged at closure** |
| Roadmap | [roadmap.md](roadmap.md) | Programme sync |
| OPERATIONAL-INDEX | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Operator entry |

---

## 4. Purpose

Determine post-G3 lifecycle direction after operator sign-off and Gate G3 closure. Authorize bounded Pilot Readiness planning without starting implementation, pilot workspace, or G4. **Does not** declare Website Factory production-ready.

---

## 5. Lifecycle Decision

```text
PROCEED TO PILOT READINESS

G4 DEFERRED
```

**Rationale:**

- G3 closed successfully;
- core architecture and reference coverage are sufficient for a bounded pilot;
- time pressure favours real-world validation;
- remaining G4 work is not required for the first limited frontend pilot;
- pilot findings should inform G4 prioritisation.

**Explicit non-selection:**

| Option | State |
|--------|-------|
| **Start G4 now** | **NOT SELECTED** — **DEFERRED** |
| **Close WF-R01.3 programme** | **NOT SELECTED** |
| **Declare production readiness** | **NOT SELECTED** |
| **Start pilot workspace without WF-PR01-A** | **NOT AUTHORIZED** |

---

## 6. Current State at Decision

| Field | Value |
|-------|-------|
| **Gate G3** | **CLOSED** · **PASS WITH RECORDED NON-BLOCKING DEBT** |
| **Gate G4** | **DEFERRED · NOT STARTED** |
| **RC** | **32/32** |
| **RPC** | **29/32** |
| **RSC** | **7/11** |
| **SC** | **LANDING PASS · CATALOG PASS · PROMO PASS** · corporate pilot with substitution debt · ECOMMERCE staging accepted for G3 |
| **PC** | **1/1 LANDING · 1/1 CATALOG corridor · 1/1 PROMO corridor** · ECOMMERCE **not accrued** |
| **Production readiness** | **NOT CLAIMED** |
| **Implementation** | **UNCHANGED** by lifecycle pass |

---

## 7. Pilot Readiness Identity — WF-PR01

| Field | Value |
|-------|-------|
| **Stage ID** | **WF-PR01** |
| **Name** | **Website Factory Pilot Readiness** |
| **Status** | **AUTHORIZED · NOT STARTED** |
| **Purpose** | Prepare one bounded test-production frontend project without claiming general production readiness |

**WF-PR01 is not:**

- a shipped pilot;
- a client workspace;
- G4;
- WF-R01.3 programme closure;
- Website Factory production-ready declaration.

---

## 8. First Pilot Boundary (Recommended)

| Field | Value |
|-------|-------|
| **Project class** | Bounded corporate or landing frontend project |
| **Input** | Approved desktop and mobile visual source — PNG, PDF, or Figma export |
| **Expected size** | One primary page or a small shared-page family |
| **Preferred initial scope** | **5–10 sections** · desktop + mobile · HTML / SCSS / JS / Gulp |
| **Out of scope (first validation pass)** | CMS integration · ecommerce runtime · personal account · payment · complex application logic |

Pilot may be a real client project, but must operate under operator approval gates. **No pilot input selected in this pass.**

---

## 9. Pilot Readiness Minimum Package (Required Before Workspace)

Before creating a pilot workspace, one Pilot Readiness package must define:

```text
intake contract
visual source authority
page inventory
block inventory
layout/numeric extraction
frontend workspace contract
text fidelity rules
asset policy
Russian typography rules
responsive contract
build contract
visual QA method
pixel-difference review
operator approval gates
Git/checkpoint policy
failure/rollback policy
pilot success criteria
```

**Package implementation:** **NOT AUTHORIZED in this pass** — owned by **WF-PR01-A**.

---

## 10. Pilot Success Boundary

**Pilot validates:**

```text
Can Website Factory produce a useful frontend result from a real visual source?

Can it preserve exact content and section structure?

Can it apply the operator frontend rules?

Can it build desktop and mobile consistently?

Can it expose visual deviations honestly?

Can an operator correct the result without rebuilding the architecture?
```

**Pilot does not prove:**

```text
universal production readiness
all site types
all CMS integrations
full autonomy
pixel-perfect guarantee
G4 completion
```

---

## 11. G4 Deferral

| Field | Value |
|-------|-------|
| **G4** | **DEFERRED · NOT STARTED** |
| **Reason** | Operator lifecycle decision selects Pilot Readiness first; G4 gaps remain documented in accepted debt register |
| **Re-entry** | G4 may resume after Pilot Readiness findings and separate operator decision — **not automatic** |

Remaining G4-oriented debt includes DELIVERY · CERTIFICATES · PARTNERS · ECOMMERCE PC · dedicated FEATURES/REVIEWS/MAP · RSC expansion · full Core blueprint set.

---

## 12. Next Task

**Single next task:**

```text
WF-PR01-A — Pilot Readiness Contract and First Pilot Launch Boundary
```

| Field | Value |
|-------|-------|
| **Nature** | Documentation-operational |
| **Creates pilot workspace?** | **No** — not until pilot input selected under WF-PR01-A |
| **Starts in this pass?** | **No** |

---

## 13. Documentation State

| Surface | State |
|---------|-------|
| **roadmap.md** | G3 **CLOSED** · WF-R01.3.5 **COMPLETE** · WF-PR01 **AUTHORIZED · NOT STARTED** · next **WF-PR01-A** |
| **OPERATIONAL-INDEX.md** | Synced |
| **WF-R01.3 parent** | **OPEN** · **DESIGN** · **CONTINUES** |

---

## 14. Evidence Paths

```text
projects/mars-website-factory/wf-r01-3-post-g3-lifecycle-decision-v1.md
projects/mars-website-factory/wf-r01-3-g3-gate-closure-decision-v1.md
projects/mars-website-factory/wf-r01-3-g3-formal-evaluation-decision-v1.md
reports/wf-r01-3-g3-operator-signoff-gate-closure-v1.md
projects/mars-website-factory/roadmap.md
projects/mars-website-factory/OPERATIONAL-INDEX.md
```

---

## 15. Final Status

```text
LIFECYCLE DECISION: PROCEED TO PILOT READINESS
G4: DEFERRED · NOT STARTED
WF-PR01: AUTHORIZED · NOT STARTED
WF-R01.3: OPEN · CONTINUES
WF-R01.3.5: COMPLETE
PILOT PROJECT: NOT STARTED
PRODUCTION READINESS: NOT CLAIMED
```

---

*Canonical lifecycle decision: `projects/mars-website-factory/wf-r01-3-post-g3-lifecycle-decision-v1.md` · v1 · 2026-06-22*
