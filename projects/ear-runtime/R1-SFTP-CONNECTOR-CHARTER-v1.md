# R1 SFTP Read-Only Connector Charter v1

**Type:** Planning charter — **not** implementation authorization  
**Date:** 2026-06-02  
**Backlog item:** R1 — First SFTP Read-Only Connector  
**Engineering charter:** [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md)  
**Authoritative acceptance:** [shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md § R1](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md#r1--first-sftp-read-only-connector)

---

## Purpose

Define the planning scope for **R1 — SFTP Read-Only Connector**: the first Mode 2 connected helper that performs read-only SFTP acquisition per frozen EAR connector contracts.

This charter authorizes **planning and readiness review only**. It does **not** authorize implementation, library selection, or live SFTP access.

---

## Context

| Field | Value |
|-------|-------|
| **Connector class** | SFTP Read-Only — [EAR-CONNECTOR-TYPES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-TYPES-v1.md) |
| **EAR mode** | Mode 2 — Connected Read-Only |
| **Reference path** | CON-L1-A — [EAR-CONNECTED-PATHS-v1.md](../../shared/external-access-runtime/EAR-CONNECTED-PATHS-v1.md) |
| **First pilot consumer** | PILOT-001 — SITE-001 (Автосалон СИБКАР) — when Execution separately authorized |
| **Architecture package** | [shared/.../pilots/PILOT-001-SITE-001-SFTP-READONLY/](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/) |

---

## Inputs

Per [EAR-CONNECTOR-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-CONTRACT-v1.md) — operator-supplied before connector may run:

| Input | Required | Notes |
|-------|----------|-------|
| `acquisition_id` | Yes | Correlates Request, Evidence, eventual snapshot |
| `site_ref` | Yes | e.g. `SITE-001` |
| `connector_class` | Yes | SFTP Read-Only |
| `channel` | Yes | Echo of approved channel for acquisition log |
| `ear_mode` | Yes | Must be `2` |
| `scope` | Yes | `sftp_root`, `allowed_paths`, `excluded_paths`; default exclusions per [EAR-DEFAULT-EXCLUSIONS-v1.md](../../shared/external-access-runtime/EAR-DEFAULT-EXCLUSIONS-v1.md) |
| `credential_ref` | Yes (connected) | Reference only — [EAR-CREDENTIAL-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-CREDENTIAL-BOUNDARY-v1.md) |
| `operator_approval_ref` | Yes | HITL record — non-secret |
| `quality_target` | Optional | Intended snapshot level — connector does not guarantee |

**Forbidden in inputs:** Raw passwords, private keys, session cookies in git-bound copies.

---

## Outputs

Per connector contract — on completion (success, partial, or failure with artefacts):

| Output | Description |
|--------|-------------|
| **Raw acquisition artefacts** | Files and metadata retrieved under scoped read-only plan — input for R2 |
| **Connector status** | Contract-shaped completion status |
| **Connector errors** | Fail-closed error records per [EAR-CONNECTOR-FAILURES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-FAILURES-v1.md) |
| **Connector warnings** | Non-blocking issues (e.g. path skipped, size limit) |

**Not R1 outputs:** Evidence Package (R2), candidate snapshot (R3), published snapshot (R4).

---

## Boundaries

### R1 owns

- Read-only SFTP session execution under human supervision
- Scoped transfer plan enforcement (`allowed_paths`, `excluded_paths`, default exclusions)
- Contract-shaped status, errors, warnings, and artefact references
- Fail-closed behavior on ambiguity or failure
- `credential_ref` resolution at runtime — credentials stay outside git

### R1 does not own

- Evidence Package assembly (R2)
- Snapshot build or publish (R3, R4)
- Validation gate logic (R5)
- OCPilot or consumer analysis
- Pilot Execution Authorization
- Architecture contract changes
- SSH shell, FTP, PMA, DB, or Hybrid coordinator connectors
- Write, delete, or mutate operations on remote host

---

## Success criteria (engineering)

R1 is **complete** when (future implementation review):

1. Connector completes a scoped read-only transfer plan under human supervision.
2. Outputs are contract-shaped per [EAR-CONNECTOR-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-CONTRACT-v1.md).
3. Failure behavior matches [EAR-CONNECTOR-FAILURES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-FAILURES-v1.md) — fail closed, logged status.
4. No credentials appear in git-bound artefacts.
5. Outputs are suitable as R2 input — **without** claiming snapshot publish or quality level.

**Planning success (this charter):** Purpose, inputs, outputs, boundaries, success criteria, and non-goals are documented. Status: **PLANNED**.

---

## Non-goals

| Non-goal | Notes |
|----------|-------|
| SSH shell access | Forbidden connector class |
| FTP / FTPS | Different connector class — not R1 |
| phpMyAdmin or DB connectors | Not SFTP Read-Only |
| Hybrid coordinator | Separate backlog item — future |
| Production host acquisition | PILOT-001 targets TEST environment first |
| Write operations | Mode 3 forbidden in v1 |
| Autonomous / scheduled runs | Human-operated only |
| Library or framework selection | Deferred to Implementation Readiness Review |
| Live SFTP access during planning | Requires Execution Authorization |

---

## Next gate

**R1 Implementation Readiness Review** — human-approved review that may authorize:

- Library selection
- Module layout under `runtime/connectors/`
- Test strategy (non-production)
- Credential binding procedure

Does **not** automatically authorize PILOT-001 Execution.

---

## Truth statement

R1 is **PLANNED** only. **No** connector code, SFTP client, or live access session exists. This document is a planning charter — not implementation.
