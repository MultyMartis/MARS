# R1 — Implementation Charter Requirements v1

**Type:** Preconditions for R1 implementation authorization — **not** an Implementation Charter and **not** implementation approval  
**Date:** 2026-06-02  
**Readiness result:** **CONDITIONAL GO** — [R1-IMPLEMENTATION-READINESS-REVIEW-v1.md](R1-IMPLEMENTATION-READINESS-REVIEW-v1.md)  
**Decisions baseline:** [R1-IMPLEMENTATION-DECISIONS-v1.md](R1-IMPLEMENTATION-DECISIONS-v1.md)

---

## Purpose

List **exactly** what a human-approved **R1 Implementation Charter** must contain before R1 **code implementation** may begin. Satisfying this checklist does **not** authorize PILOT-001 Execution or live SFTP.

---

## 1. Charter identity and scope

| Req ID | Requirement | Evidence basis |
|--------|-------------|----------------|
| C-01 | Names backlog item **R1** and references [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md) | Planning charter |
| C-02 | States charter authorizes **implementation planning and code** for R1 only — not R2–R5 unless explicitly included | [ENGINEERING-BOUNDARIES-v1.md](ENGINEERING-BOUNDARIES-v1.md) |
| C-03 | Repeats explicit **non-goals**: no SSH shell, FTP, PMA, DB, Hybrid, writes, Mode 3, production targeting, autonomous runs | R1 planning charter |
| C-04 | Human approver identity and date recorded | MARS HITL discipline |

---

## 2. Runtime and language bindings

| Req ID | Requirement | Evidence basis |
|--------|-------------|----------------|
| C-05 | **Python minor version** pinned (e.g. 3.11.x) with documented operator install expectation | Engineering charter — version was SAFE UNKNOWN |
| C-06 | **Packaging strategy** named (venv, pip-tools, poetry, uv, etc.) — single choice | Engineering charter deferral |
| C-07 | **CLI entrypoint** pattern documented (command name, required args, exit codes) | CLI-first decision |
| C-08 | **Repository layout** — materialize or charter-exempt paths under `runtime/connectors/` per [RUNTIME-STRUCTURE-v1.md](RUNTIME-STRUCTURE-v1.md) | Structure proposed only |

---

## 3. Connector contract conformance

| Req ID | Requirement | Evidence basis |
|--------|-------------|----------------|
| C-09 | Maps R1 **session output** fields to [EAR-CONNECTOR-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-CONTRACT-v1.md) — including how `evidence_package_ref` is satisfied (R1-only stub vs R2 handoff) | R1/R2 split — readiness review G-06 |
| C-10 | Implements Connector Input validation (required fields, `ear_mode` = 2, forbidden secret fields) | Connector contract |
| C-11 | Implements Connector Status values: `success`, `partial`, `failed`, `aborted` | Connector contract |
| C-12 | Implements error/warning classes per [EAR-CONNECTOR-FAILURES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-FAILURES-v1.md) — descriptive strings acceptable | Phase 2D contract |
| C-13 | **`read_only_attestation`** behavior documented and testable | Connector contract output |
| C-14 | Default exclusions applied per [EAR-DEFAULT-EXCLUSIONS-v1.md](../../shared/external-access-runtime/EAR-DEFAULT-EXCLUSIONS-v1.md) unless operator scope overrides with approval ref | R1 inputs |

---

## 4. Credential and storage bindings

| Req ID | Requirement | Evidence basis |
|--------|-------------|----------------|
| C-15 | **`credential_ref` resolution** procedure — external path only; no secrets in git | [EAR-CREDENTIAL-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-CREDENTIAL-BOUNDARY-v1.md) |
| C-16 | **Raw acquisition output location** (bulk root) — operator path or configurable binding outside repo | [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) |
| C-17 | Git exclusion rule restated: no passwords, keys, dumps, unredacted config in commits | Credential boundary |
| C-18 | PILOT-001 bindings may reference pilot sub-charter §4 — must not invent paths; **SAFE UNKNOWN** remains a **block** for live pilot until operator resolves | Pilot sub-charter |

---

## 5. SFTP library and read-only enforcement

| Req ID | Requirement | Evidence basis |
|--------|-------------|----------------|
| C-19 | **SFTP client library** named with license note | Deferred from readiness review |
| C-20 | Read-only enforcement design: no remote write/delete/rename; violation → `read_only_violation` / fail closed | [EAR-CONNECTOR-FAILURES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-FAILURES-v1.md) |
| C-21 | Scope enforcement: `sftp_root`, `allowed_paths`, `excluded_paths` — stop on `scope_violation` | R1 inputs |
| C-22 | Non-production test strategy (mock/stub host or operator TEST host) — **no** production | R1 non-goals |

---

## 6. Logging and failure reporting

| Req ID | Requirement | Evidence basis |
|--------|-------------|----------------|
| C-23 | **Logging strategy**: format (structured JSON or text), fields, no secret values | Engineering principles |
| C-24 | Per-run log artefact location (external or under `projects/ear-runtime/pilots/` when execution authorized) | Boundaries — run logs |
| C-25 | Failure reporting maps to connector status + error list; operator-facing summary without credentials | Connector failures |

---

## 7. Quality and pilot traceability

| Req ID | Requirement | Evidence basis |
|--------|-------------|----------------|
| C-26 | States R1 **does not** publish snapshots or claim Level 1 quality | R1 charter |
| C-27 | Traceability to **PILOT-001** / CON-L1-A / SITE-001 TEST documented — execution still separate gate | Pilot charter |
| C-28 | Acceptance criteria copied from [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R1 | Architecture backlog |

---

## 8. Governance gates (charter must acknowledge)

| Req ID | Requirement |
|--------|-------------|
| C-29 | **R1 Implementation Charter** human approval required before first merge of R1 code |
| C-30 | **PILOT-001 Execution Authorization** is a **separate** gate — not implied by R1 charter |
| C-31 | Architecture changes require **Architecture Amendment Charter** — not runtime PR |
| C-32 | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) updated when implementation actually starts |

---

## 9. Out of scope for Implementation Charter (do not require)

| Item | Reason |
|------|--------|
| OCPilot Run 5 execution | Consumer scope |
| R2–R5 implementation | Separate charters unless explicitly bundled with accepted risk |
| Org-wide vault product | SAFE UNKNOWN — accepted in Phase 3 |
| Machine-readable JSON Schema for connector contract | Architecture non-goal Phase 2D |

---

## Approval checklist (human)

Before marking R1 implementation **STARTED**:

- [ ] R1 Implementation Charter document exists and satisfies C-01–C-32
- [ ] Human approver recorded
- [ ] No item in §2–§6 remains **SAFE UNKNOWN** unless explicitly waived with risk note
- [ ] Operator confirms PILOT Execution is **not** implied

---

## Truth statement

This requirements document **does not** authorize implementation. It defines what must exist **before** implementation may begin.
