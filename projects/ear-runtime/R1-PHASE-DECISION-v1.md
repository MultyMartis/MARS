# R1 — Phase Decision v1

**Phase:** EAR Runtime R1 — SFTP Read-Only Connector Implementation Readiness Review  
**Date:** 2026-06-02  
**Type:** Human-operated planning decision record (documentation only)  
**Deliverables:** [R1-IMPLEMENTATION-READINESS-REVIEW-v1.md](R1-IMPLEMENTATION-READINESS-REVIEW-v1.md), [R1-IMPLEMENTATION-DECISIONS-v1.md](R1-IMPLEMENTATION-DECISIONS-v1.md), [R1-IMPLEMENTATION-CHARTER-REQUIREMENTS-v1.md](R1-IMPLEMENTATION-CHARTER-REQUIREMENTS-v1.md)

---

## Decision

| Field | Value |
|-------|-------|
| **Outcome** | **CONDITIONAL GO** |
| **Meaning** | R1 **Implementation Charter** may be drafted and submitted for human approval |
| **Does not authorize** | Code, libraries, SFTP access, PILOT-001 Execution, snapshot publish |

---

## Evidence

| Evidence class | Finding |
|----------------|---------|
| Architecture contracts | **Complete** — connector, credential, evidence, snapshot, failures, storage, CON-L1-A |
| Runtime engineering charter | **APPROVED** — Python, CLI-first, human-operated, read-only |
| R1 planning charter | **DONE** — scope, I/O, boundaries documented |
| Implementation in repo | **None** — status honest |
| Readiness categories | 10 READY, 6 PARTIAL, 0 NOT READY |
| PILOT-001 alignment | Design-aligned; execution gates **not** satisfied (expected) |
| Inflated claims | **None** in review deliverables |

---

## Blockers

**Architectural blockers:** **none**

**Conditions (must be resolved in R1 Implementation Charter before coding):**

| ID | Condition |
|----|-----------|
| CON-01 | Pin Python minor version |
| CON-02 | Choose packaging strategy |
| CON-03 | Name SFTP library and read-only test approach |
| CON-04 | Document R1 session output vs full connector contract / R2 handoff |
| CON-05 | Fix operator storage bindings (or document waiver) for bulk and logs |
| CON-06 | Materialize or charter `runtime/connectors/` layout |

**Process (does not change R1 readiness outcome):**

| ID | Note |
|----|------|
| PROC-01 | PILOT-001 human Approval not recorded in STATUS.md |
| PROC-02 | PILOT-001 Execution **NOT AUTHORIZED** |

---

## Conditions

| Condition | Owner | When |
|-----------|-------|------|
| Author R1 Implementation Charter per requirements doc | Runtime engineering / operator | Before R1 code |
| Human sign-off on Implementation Charter | Charter authority | Before R1 code |
| Resolve CON-01–CON-06 in charter | Technical lead | Before R1 code |
| Update [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) when implementation starts | Operator | At implementation start |

---

## Recommended next phase

| Phase | Name | Scope |
|-------|------|-------|
| **Next** | **R1 Implementation Charter** | Human-approved charter satisfying [R1-IMPLEMENTATION-CHARTER-REQUIREMENTS-v1.md](R1-IMPLEMENTATION-CHARTER-REQUIREMENTS-v1.md) |
| **Then** | **R1 Implementation** (when charter approved) | Code under `runtime/connectors/` — still no live pilot without Execution Authorization |
| **Parallel (operator)** | PILOT-001 Approval / sub-charter sign-off | Unblocks future Execution — not required for R1 code charter alone |

**Not recommended as immediate next step:** Live SFTP to SITE-001, PILOT-001 Execution, OCPilot Run 5 completion claims, production access.

---

## Approvals

| Role | Action |
|------|--------|
| Readiness review documentation | Recorded 2026-06-02 — agent task closeout |
| Human charter authority | Required for R1 Implementation Charter approval |
| This document | Records readiness outcome only — **not** implementation approval |

---

## Truth statement

| Claim | Accurate? |
|-------|-----------|
| R1 readiness = implementation started | **No** |
| CONDITIONAL GO = SFTP allowed | **No** |
| Architecture amendment required for R1 | **No** |
