# MARS Website Factory - Project Drift Survivability Model

**Status:** **documented** - Website Factory model for human-supervised long-term drift survivability.  
**Not:** automated lifecycle engine, runtime drift monitor, permanent stability guarantee, or universal frontend maintenance law.

**Purpose:** define the layers that help a frontend project evolve without losing freeze-state integrity, continuity readability, architectural survivability, or identity traceability.

**Parent governance:** [temporal-evolution-governance.md](temporal-evolution-governance.md).  
**Drift taxonomy:** [evolution-drift-taxonomy.md](evolution-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/temporal-evolution-checklist.md`](../../agents/mars-forge/temporal-evolution-checklist.md).

---

## 1. Model Overview

Project drift survivability is the readable chain between:

```text
freeze-state layer
-> governed evolution layer
-> controlled override layer
-> iterative-change layer
-> long-term continuity layer
-> escalation / review layer
-> architectural survivability layer
```

The model exists because a frontend can remain locally correct while slowly losing the ability to explain how it got there, what identity it preserves, which frozen state governs it, and which changes are approved evolution rather than accumulated drift.

---

## 2. Survivability Layers

| Layer | Preserves | Failure signal |
|-------|-----------|----------------|
| **Freeze-state layer** | Baselines, frozen sections, approved snapshots, and the meaning of "locked." | Frozen scope is reopened or altered without traceable reason. |
| **Governed evolution layer** | Approved change paths from current state to next state. | Change is framed as "improvement" without lineage, authority, or impact review. |
| **Controlled override layer** | Exceptions remain bounded, justified, visible, and reversible where possible. | Overrides stack until exceptions become the hidden system. |
| **Iterative-change layer** | Small changes are reviewed for cumulative effect, not only local validity. | Every patch is reasonable alone, but the project identity changes over time. |
| **Long-term continuity layer** | Future operators can read the history, current state, and intended direction. | Current state requires memory, archaeology, or guesswork. |
| **Escalation / review layer** | Ambiguous divergence, freeze breaks, modernization, and identity risks reach HITL or checkpoint review. | Operators silently decide long-term direction through local edits. |
| **Architectural survivability layer** | Structure, ownership, dependencies, and conventions remain understandable under continued evolution. | Code and documentation work now but cannot absorb future scoped changes safely. |

---

## 3. Freeze-State Layer

Freeze-state preservation means a frozen scope remains a recognizable governance object after later work.

Review:

- What artifact or report established the freeze?
- What scope was frozen: page, section, block, breakpoint, component, source interpretation, design intent, QA state, or delivery candidate?
- What later changes touched the frozen scope directly or indirectly?
- Was the freeze preserved, reopened, superseded, branched, or invalidated?
- Are current operators able to identify the trusted baseline?

Freeze-state failure includes:

- "frozen" used as a status label without baseline;
- frozen sections edited through adjacent global styles;
- repeated hotfixes applied without unfreeze reason;
- old frozen screenshots treated as current authority after supersede;
- QA pass claimed without freeze impact review.

---

## 4. Governed Evolution Layer

Governed evolution allows change while preserving lineage and authority.

An evolution step is governed when it names:

- source or baseline;
- reason for change;
- approving authority or project rule;
- expected impact;
- affected governance layers;
- whether prior freeze, QA, or lineage is preserved or invalidated;
- follow-up checkpoint if risk remains.

Controlled divergence is allowed when the divergence is visible. It becomes drift when the project cannot explain why the current state differs from the trusted earlier state.

---

## 5. Controlled Override Layer

Overrides are survivable when they remain bounded and understandable over time.

| Override condition | Survivability posture |
|--------------------|----------------------|
| Temporary patch with owner, scope, and expiry/review note | Allowed with monitored risk. |
| Source-authorized exception that preserves identity | Allowed and documented as governed divergence. |
| Repeated local override for same root problem | Continuity checkpoint required. |
| Override copied into other sections without rationale | Drift risk. |
| Override becomes stronger than canonical token/component/path | Escalate. |

The risk is not one exception. The risk is **cumulative override pressure** that converts the system into a stack of exceptions.

---

## 6. Iterative-Change Layer

Iterative changes need accumulation review.

Review questions:

- How many changes have touched the same section, token, breakpoint, component, or source decision since freeze?
- Are the changes converging toward a clearer system or layering over unresolved structure?
- Did repeated small fixes create new visual, strategic, accessibility, implementation, or provenance inconsistencies?
- Are local improvements now contradicting the original design or business identity?
- Are temporary notes still temporary, or have they become unreviewed architecture?

**Rule:** local PASS does not imply cumulative PASS.

---

## 7. Long-Term Continuity Layer

Long-term continuity is present when a future operator can answer:

- What is the canonical current state?
- What previous state does it supersede or preserve?
- Which decisions are frozen, waived, deferred, or explicitly divergent?
- Which artifacts are active, stale, archived, or unknown-origin?
- Which governance findings remain open?
- Which changes were local fixes versus identity-changing evolution?
- Where should the next operator start without relying on memory?

Minimal continuity fields:

| Field | Purpose |
|-------|---------|
| **Baseline / freeze ref** | Identifies the state being preserved or superseded. |
| **Evolution reason** | Explains why change is happening now. |
| **Divergence summary** | Names what differs from the prior state. |
| **Authority** | Names source, HITL, or project rule that allows the change. |
| **Drift patterns** | Names taxonomy risks. |
| **Continuity checkpoint** | States whether cumulative review is needed, done, or deferred. |

---

## 8. Escalation / Review Layer

Long-term escalation is required when:

- freeze state cannot be identified;
- version lineage is ambiguous;
- local changes would materially alter identity;
- modernization changes conventions, tokens, structure, dependency strategy, or design language;
- override stacking keeps growing;
- governance fatigue appears in skipped checks or vague PASS language;
- patch history becomes the only explanation for behavior;
- reviewers disagree whether current state is approved evolution or drift.

Escalation should identify:

- what decision is needed;
- what baseline or source is affected;
- what risks continuation would create;
- whether the result should preserve, supersede, branch, rollback, or deprecate prior state.

---

## 9. Architectural Survivability Layer

Architectural survivability is the ability of the frontend to remain readable and safely modifiable after many changes.

It depends on:

- visible ownership of sections, components, tokens, partials, breakpoints, and behavior;
- controlled include / import dependencies;
- bounded overrides;
- deterministic rebuild expectations;
- source-lineage and freeze-state traceability;
- QA confidence that states proof boundaries;
- governance checkpoints that review accumulation.

Architectural survivability is not a promise that architecture will never change. It means change remains deliberate, readable, and governed.

---

## 10. Drift Visibility

Drift should be visible at three levels:

| Level | What to expose |
|-------|----------------|
| **Local** | The immediate file, section, breakpoint, state, or source decision affected. |
| **Cumulative** | Repeated changes, overrides, patches, or deviations around the same area. |
| **Identity** | Whether the project still expresses the approved design, business, architectural, and governance identity. |

If drift is accepted, report whether it is:

- temporary;
- approved divergence;
- monitored risk;
- deferred normalization;
- HITL-required;
- blocked;
- identity-changing and requiring new baseline.

---

## 11. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Freeze artifact is missing | Cannot establish the baseline. |
| Evolution authority is unclear | Cannot distinguish approved change from drift. |
| Override lifetime is unknown | Cannot know whether exception is temporary, accepted, or forgotten. |
| Cumulative edits are unreviewed | Cannot assess accumulation risk. |
| Historical traceability is weak | Cannot reconstruct the chain across versions or sessions. |
| Architectural owner is unclear | Cannot prove future safe modification path. |
| Modernization scope is undefined | Cannot know whether identity should be preserved, superseded, or intentionally changed. |

**Action:** record the missing layer, resolver, and disposition: continue with disclosure, continuity checkpoint required, HITL required, blocked, or monitored risk.

---

## 12. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Project Drift Survivability Model - freeze-state preservation, governed evolution, controlled overrides, iterative-change accumulation, long-term continuity, escalation/review, and architectural survivability; documentation only. |
