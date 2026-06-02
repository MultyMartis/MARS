# R1 — Implementation Decision v1

**Type:** Human gate decision record — charter approval for R1 code  
**Date:** 2026-06-02  
**Charter:** [R1-IMPLEMENTATION-CHARTER-v1.md](R1-IMPLEMENTATION-CHARTER-v1.md)  
**Readiness:** **CONDITIONAL GO** — [R1-IMPLEMENTATION-READINESS-REVIEW-v1.md](R1-IMPLEMENTATION-READINESS-REVIEW-v1.md)

---

## Decision

| Field | Value |
|-------|-------|
| **Question** | May R1 implementation (code) begin? |
| **Outcome** | **PENDING HUMAN APPROVAL** |
| **Charter status** | **DRAFTED** — 2026-06-02 |
| **Meaning when approved** | R1 code work under `projects/ear-runtime/runtime/` may begin per [R1-IMPLEMENTATION-TASKS-v1.md](R1-IMPLEMENTATION-TASKS-v1.md) |
| **Does not authorize when approved** | Live SFTP to production, PILOT-001 Execution, snapshot publish, OCPilot runs |

---

## Conditions for approval

Human approver must confirm:

| ID | Condition | Status |
|----|-----------|--------|
| AP-01 | [R1-IMPLEMENTATION-CHARTER-v1.md](R1-IMPLEMENTATION-CHARTER-v1.md) reviewed and accepted | Pending |
| AP-02 | Python **3.12+**, **requirements.txt**, **paramiko**, CLI-first, external output — accepted | Documented in charter |
| AP-03 | R1/R2 boundary (`evidence_package_ref` stub) — accepted | Documented in charter |
| AP-04 | Default exclusions reference [EAR-DEFAULT-EXCLUSIONS-v1.md](../../shared/external-access-runtime/EAR-DEFAULT-EXCLUSIONS-v1.md) — accepted | Documented in charter |
| AP-05 | [R1-TEST-STRATEGY-v1.md](R1-TEST-STRATEGY-v1.md) — accepted (T0/T1 before live TEST) | Documented |
| AP-06 | PILOT-001 Execution is **not** implied | Acknowledged |
| AP-07 | Operator storage paths (`credential_ref`, bulk root) — resolved or explicitly waived with risk note | **SAFE UNKNOWN** for PILOT-001 until operator sign-off — **does not block R1 code**; **blocks live pilot** |

---

## Conditions that block live pilot (not R1 code)

| ID | Blocker | Owner |
|----|---------|-------|
| BL-01 | PILOT-001 Execution Authorization | Pilot governance |
| BL-02 | PILOT-001 human Approval in STATUS.md | Operator |
| BL-03 | Operator `credential_ref` and output root bindings | Operator |
| BL-04 | PILOT sub-charter §4 path placeholders | Operator |

R1 local/mock implementation may proceed after AP-01–AP-06 without BL-01–BL-04 resolved.

---

## On approval — state transitions

When human approver records approval below:

| Field | New value |
|-------|-----------|
| R1 charter | **APPROVED** |
| Implementation | **AUTHORIZED FOR R1 ONLY** |
| First task | **R1.1 Runtime skeleton** |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Update Implementation to **AUTHORIZED FOR R1 ONLY**; R1 remains **IMPLEMENTATION CHARTERED** until R1.1 starts |

When R1.1 first code lands:

| Field | New value |
|-------|-----------|
| Implementation | **IN PROGRESS** |
| Runtime code | **PARTIAL** (skeleton) |

---

## Approvals

| Role | Name | Date | Decision |
|------|------|------|----------|
| Charter authority (human) | _Pending_ | — | _Pending_ |
| Technical review | Documented 2026-06-02 | 2026-06-02 | Charter drafted |

---

## Rejection / hold

If human approver rejects or holds:

- Record reason and required charter amendments
- Implementation remains **NOT STARTED**
- Do not create `requirements.txt` or runtime code until re-submitted

---

## Truth statement

| Claim | Accurate? |
|-------|-----------|
| R1 implementation approved | **No** — pending human |
| This document alone authorizes coding | **No** |
| Charter drafting complete | **Yes** — 2026-06-02 |
| SFTP accessed | **No** |
