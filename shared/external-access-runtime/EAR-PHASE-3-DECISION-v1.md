# EAR Phase 3 Decision v1

**Phase:** 3 — Runtime Readiness Assessment  
**Date:** 2026-06-01  
**Type:** Human-operated go/no-go record (documentation only)  
**Full assessment:** [EAR-RUNTIME-READINESS-ASSESSMENT-v1.md](EAR-RUNTIME-READINESS-ASSESSMENT-v1.md)

---

## Decision

| Field | Value |
|-------|-------|
| **EAR runtime readiness (pilot charter authorization)** | **CONDITIONAL GO** |
| **Meaning** | EAR may proceed to author and approve the first **Connected Acquisition Connector Pilot Charter** under explicit human charter. **No** runtime implementation or live access is authorized by this decision alone. |

---

## Evidence

| Evidence class | Finding |
|--------------|---------|
| Phase 1 foundation | Mission, architecture, snapshot contract, security, modes — **complete** |
| Phase 2A | OpenCart snapshot spec, lifecycle, consumer guide — **complete** |
| Phase 2B | Workflow, publishing, storage, failure models, readiness gates — **complete** |
| Phase 2C | OpenCart acquisition design, paths, risks, quality mapping — **complete** |
| Phase 2D | Connector architecture, contract, types, evidence package, credential boundary, mapping, failures, Mode 2 reference — **complete** |
| Phase 2E | Offline + Connected tracks, paths, selection guide, OCPilot integration — **complete** |
| Implementation in repo | **None** — status honest |
| Readiness matrix | 15 READY · 3 PARTIAL · 0 NOT READY |

---

## Blockers

**Architectural blockers for Connector Pilot Charter:** **none**

**Conditions (non-blocking, must appear in pilot charter):**

1. Human charter naming site, environment, SFTP scope, quality target (recommended L1), consumer (e.g. OCPilot SITE-001).
2. Request-stage record (G0) — template may be embedded in charter (DD-2E-09).
3. Named external quarantine and bulk paths for pilot operator.
4. Waived-risks register for soft gaps (schema, automated validation, virus scan policy).
5. Explicit separation: pilot charter ≠ implementation sub-charter ≠ live access execution.

---

## Recommended first connector pilot

| Field | Value |
|-------|-------|
| **Class** | **SFTP Read-Only** |
| **Track** | Connected Acquisition (Mode 2) |
| **Reference path** | CON-L1-A in [EAR-CONNECTED-PATHS-v1.md](EAR-CONNECTED-PATHS-v1.md) |
| **Target snapshot level (honest)** | Level 1 for first pilot scope |
| **Deferred** | Hybrid (SFTP + PMA + Admin), SSH, ZIP Intake as Mode 2 pilot, PMA-only |

---

## Recommended next phase

| Step | Action |
|------|--------|
| **1** | **Connected Acquisition Pilot Charter** — scope, site, SFTP connector class, gates, waived risks, implementation sub-charter criteria |
| **2** | Human approval (HITL) of pilot charter |
| **3** | Only then: optional **implementation sub-charter** (still not implied by Phase 3) |

**Not next:** Runtime code, connector scripts, or SITE-001 live acquisition without separate explicit approval.

---

## Decision rationale (concise)

EAR documentation through Phase 2E provides a **closed architecture** for Mode 2 read-only connectors: channel → connector → evidence package → validation → snapshot → publish → consumer. Consumer separation, credential boundaries, failure semantics, and dual acquisition tracks are **frozen at documentation level**. Remaining gaps are **operational** (storage path naming, Request template, roadmap phase label alignment) and **implementation** (code, schemas, registry) — appropriately deferred to the pilot charter and sub-charter. **CONDITIONAL GO** reflects minor governance partials, not missing architecture.

---

## Approvals

| Role | Action |
|------|--------|
| Operator / human charter | Required to approve Connector Pilot Charter (next artifact) |
| This document | Records Phase 3 assessment outcome only — **not** pilot execution approval |

---

## SAFE UNKNOWN

- Calendar date for first pilot charter authoring — operator schedule.
- Whether implementation sub-charter places code in MARS repo vs external tooling root — charter decision.
