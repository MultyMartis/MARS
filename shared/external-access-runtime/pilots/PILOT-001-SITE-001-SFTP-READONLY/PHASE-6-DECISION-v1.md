# PILOT-001 — Phase 6 Decision v1

**Phase:** 6 — Implementation Sub-Charter  
**Date:** 2026-06-01  
**Type:** Human-operated planning decision record (documentation only)  
**Deliverables:** [IMPLEMENTATION-SUBCHARTER-v1.md](IMPLEMENTATION-SUBCHARTER-v1.md), [EXECUTION-PREPARATION-PLAN-v1.md](EXECUTION-PREPARATION-PLAN-v1.md)

---

## Current readiness state

| Dimension | State |
|-----------|-------|
| **EAR Foundation (Phases 1–3)** | **COMPLETE** — Phase 3 **CONDITIONAL GO** |
| **EAR Runtime Readiness** | **CONDITIONAL GO** (documentation assessment — **no** runtime in repo) |
| **PILOT-001 charter** | **AUTHORIZED** (Phase 4) — Charter stage active |
| **PILOT-001 Implementation Readiness (Phase 5)** | **CONDITIONAL GO** |
| **PILOT-001 Implementation Sub-Charter (Phase 6)** | **DRAFTED** — boundaries and preparation plan authored; **not** human-authorized |
| **PILOT-001 Execution** | **NOT AUTHORIZED** |
| **Implementation code in repo** | **None** — status honest |
| **Execution readiness (live access)** | **NOT READY** — checklist §7 of sub-charter |

**Phase 6 meaning:** Operational boundaries and execution **preparation** documentation exist. This **does not** advance lifecycle to Implementation or Execution in [STATUS.md](STATUS.md) without human gates.

---

## Decision summary

| Field | Value |
|-------|-------|
| **Phase 6 outcome** | **DONE** (documentation deliverables complete) |
| **Implementation Sub-Charter authorization** | **PENDING** — requires Operator Approval + human §10 sign-off + §4 resolution |
| **Execution readiness claim** | **Forbidden** — not made by Phase 6 |

---

## Remaining unknowns

| ID | Unknown | Blocks |
|----|---------|--------|
| U-01 | Human **Operator Approval** date and approver | Implementation Authorization |
| U-02 | `credential_ref` external path | Execution preflight |
| U-03 | `sftp_root`, `allowed_paths`, `excluded_paths` | Execution preflight |
| U-04 | Quarantine, evidence, snapshot, publish, bulk paths | Execution preflight |
| U-05 | Read-only SFTP account on TEST host | Execution |
| U-06 | Validate owner, `operator_approver` | Validate planning / Execution |
| U-07 | Redaction plan for sensitive paths | Live acquisition |
| U-08 | Implementation artifact location (MARS repo vs external tooling) | Implementation work |
| U-09 | Date of Implementation Authorization sign-off | Implementation work |
| U-10 | Whether Execution will be chartered for PILOT-001 | Live acquisition |

**Repo rule:** Items marked **SAFE UNKNOWN** in [IMPLEMENTATION-SUBCHARTER-v1.md](IMPLEMENTATION-SUBCHARTER-v1.md) §4 and §7 are **not** resolved by Phase 6 authoring.

---

## Approval requirements (before Execution)

| Order | Requirement | Owner |
|-------|-------------|-------|
| 1 | Record **Operator Approval** in [STATUS.md](STATUS.md) | Charter authority |
| 2 | Resolve §4 operational paths (or document waivers in risk register) | Operator technical lead |
| 3 | **Implementation Authorization** — sub-charter §10 sign-off | Charter authority + technical lead |
| 4 | Satisfy [IMPLEMENTATION-SUBCHARTER-REQUIREMENTS-v1.md](IMPLEMENTATION-SUBCHARTER-REQUIREMENTS-v1.md) checklist | Operator |
| 5 | Optional: implementation task charter (connector) — **separate** | Human |
| 6 | **Execution Authorization** — explicit HITL | Charter authority |
| 7 | Preflight §6 + execution readiness §7 — mandatory items **YES** where required | Operator |
| 8 | Phase 7 **Execution Preparation Review** | Operator / assessor |

---

## Evidence (Phase 6)

| Evidence class | Finding |
|----------------|---------|
| Implementation Sub-Charter | **Drafted** — identity, boundaries, paths, approval model, preflight, checklist |
| Execution Preparation Plan | **Complete** — five stages, no execution detail |
| Requirements traceability | Aligns with [IMPLEMENTATION-SUBCHARTER-REQUIREMENTS-v1.md](IMPLEMENTATION-SUBCHARTER-REQUIREMENTS-v1.md) structure |
| Governance consistency | Matches [PILOT-GOVERNANCE-v1.md](../../PILOT-GOVERNANCE-v1.md) lifecycle |
| Runtime / connector / SFTP access | **None** — honest |
| Inflated readiness claims | **None** |

---

## Recommended next phase

| Phase | Name | Scope |
|-------|------|-------|
| **7** | **Execution Preparation Review** | Human review: sub-charter vs requirements; resolve or waive U-01–U-10; decide whether to grant Implementation Authorization and/or Execution Authorization; **no** mandatory live access in Phase 7 unless separately chartered |

**Not recommended as Phase 7 default:** Connector implementation, live SITE-001 acquisition, snapshot publish, OCPilot Run 5 completion claims, production access.

**After Phase 7 (operator-dependent):** Optional implementation phase under Implementation Authorization; optional Execution under separate HITL.

---

## Risks (Phase 6 close)

| Risk | Mitigation in Phase 6 docs |
|------|---------------------------|
| Treating drafted sub-charter as Execution approval | §10 pending; STATUS unchanged for Execution |
| Filling §4 with invented paths | Placeholders only — SAFE UNKNOWN |
| Scope creep to Level 2+ or Hybrid | Charter §4 + sub-charter §3.2 restated |
| Secrets in git | Credential boundary + PF-03 / ER-04 |
| Premature Run 5 completion claim | Consumer handoff planning only |

---

## Approvals

| Role | Action |
|------|--------|
| Phase 6 documentation | Recorded 2026-06-01 — agent task closeout |
| Human charter authority | Required for Operator Approval and sub-charter §10 |
| This document | Records Phase 6 outcome only — **not** Implementation or Execution approval |

---

## Truth statement

| Claim | Accurate? |
|-------|-----------|
| Phase 6 authorizes Execution | **No** |
| Phase 6 creates runtime | **No** |
| PILOT-001 ready for live SFTP | **No** |
| All sub-charter requirements operator-met | **No** — G-03 and §4 pending |
