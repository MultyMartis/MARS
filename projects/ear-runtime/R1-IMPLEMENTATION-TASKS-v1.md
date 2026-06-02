# R1 — Implementation Tasks v1

**Type:** Safe implementation task breakdown — **not** code, **not** execution  
**Date:** 2026-06-02  
**Charter:** [R1-IMPLEMENTATION-CHARTER-v1.md](R1-IMPLEMENTATION-CHARTER-v1.md)  
**Prerequisite:** Human approval per [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md)

**Rule:** Tasks are ordered for incremental, reviewable progress. Each task completes before the next begins unless explicitly waived with risk note. No live SFTP until R1.10 preflight and separate PILOT Execution Authorization.

---

## Task overview

| ID | Name | Depends on | Live SFTP |
|----|------|------------|-----------|
| R1.1 | Runtime skeleton | Charter approval | No |
| R1.2 | Config input model | R1.1 | No |
| R1.3 | SFTP connection test mode | R1.2 | Optional (operator TEST only) |
| R1.4 | Read-only listing | R1.3 | Optional (mock preferred) |
| R1.5 | Exclusion engine | R1.4 | No |
| R1.6 | Manifest builder | R1.5 | No |
| R1.7 | Evidence package writer | R1.6 | No |
| R1.8 | Failures / logging | R1.2 | No |
| R1.9 | Dry-run local test | R1.7, R1.8 | No |
| R1.10 | Pilot preflight | R1.9 | Operator TEST — **not** PILOT Execution |

---

## R1.1 — Runtime skeleton

**Goal:** Materialize chartered folder layout and CLI stub without connector logic.

**Deliverables:**

- `runtime/` subdirectories: `connectors/`, `shared/`, `validators/` (empty `__init__.py` or equivalent)
- `runtime/cli.py` — argument parser skeleton, exit code constants, no SFTP
- `requirements.txt` — paramiko pin (first dependency file — created in this task only after charter approval)
- README or inline doc: how to create venv and install

**Acceptance:**

- `python -m runtime.cli --help` runs without SFTP import side effects beyond declared deps
- No code outside `projects/ear-runtime/runtime/`
- [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) updated: Implementation **IN PROGRESS**

**Out of scope:** SFTP connection, secrets, live host.

---

## R1.2 — Config input model

**Goal:** Parse and validate Connector Input per [EAR-CONNECTOR-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-CONTRACT-v1.md).

**Deliverables:**

- Input schema / dataclass for required fields: `acquisition_id`, `site_ref`, `connector_class`, `channel`, `ear_mode`, `scope`, `credential_ref`, `operator_approval_ref`
- Validation: `ear_mode` must be `2`; forbidden secret fields rejected
- `runtime/shared/` or `runtime/validators/` input validator module

**Acceptance:**

- Valid fixture JSON passes validation
- Invalid mode, missing fields, embedded secrets in input JSON → fail closed with clear error
- Unit tests without network

**Out of scope:** Credential file reading, SFTP.

---

## R1.3 — SFTP connection test mode

**Goal:** CLI mode `test-connection` — verify `credential_ref` resolves and SFTP session opens read-only.

**Deliverables:**

- `runtime/connectors/sftp_readonly/` module skeleton
- Connection helper using paramiko — read-only session only
- CLI subcommand: `--mode test-connection`

**Acceptance:**

- Against mock/stub SFTP server: connection succeeds, returns status JSON fragment
- Invalid credential path → fail closed, no secret in stderr
- **Live TEST host:** only when operator explicitly runs — not CI default

**Out of scope:** Listing, download, pilot execution.

---

## R1.4 — Read-only listing

**Goal:** Root and recursive directory listing with metadata.

**Deliverables:**

- LIST/stat traversal from `scope.sftp_root`
- Respect `allowed_paths` boundary
- Metadata: path, size, mtime (minimum)
- Optional hash hook (policy flag — may defer hash computation to R1.6)

**Acceptance:**

- Mock tree: correct entry count and metadata
- Attempt to invoke write API in code path → absent or guarded; test asserts no write calls
- Scope outside `allowed_paths` → skip or fail per charter

**Out of scope:** File download, exclusion engine (R1.5).

---

## R1.5 — Exclusion engine

**Goal:** Apply default exclusions and operator `excluded_paths`.

**Deliverables:**

- Loader for defaults from [EAR-DEFAULT-EXCLUSIONS-v1.md](../../shared/external-access-runtime/EAR-DEFAULT-EXCLUSIONS-v1.md) (embedded list or config file in runtime — not architecture edit)
- Path matching: prefix and glob where applicable
- Exclusion summary for manifest metadata

**Acceptance:**

- Fixture tree with cache/logs/tmp paths → excluded from manifest
- Exclusion policy recorded in manifest metadata
- Tests per [R1-TEST-STRATEGY-v1.md](R1-TEST-STRATEGY-v1.md) exclusion cases

**Out of scope:** Pilot-specific overrides without operator input.

---

## R1.6 — Manifest builder

**Goal:** Produce `file-manifest.json` and `file-manifest.md`.

**Deliverables:**

- JSON manifest: entries, exclusion metadata, acquisition correlation
- MD summary: human-readable counts and policy notes
- Optional hashing per charter policy flag

**Acceptance:**

- Schema stable enough for R2 consumption (document fields in task PR)
- Empty scope → valid empty manifest with status note
- Format tests pass

**Out of scope:** Evidence Package assembly (R2).

---

## R1.7 — Evidence package writer

**Goal:** Write draft evidence folder structure to external output root.

**Deliverables:**

- Output layout under `--output-root/{acquisition_id}/`
- All chartered artefacts: acquisition-log, manifests, connector-status, safe-unknown (when applicable)
- `evidence_package_ref` stub in connector-status pointing to draft folder

**Acceptance:**

- Dry-run produces full artefact set on local filesystem
- No writes to git workspace except code
- Credential redaction test passes

**Out of scope:** R2 Evidence Package validation, snapshot build.

---

## R1.8 — Failures / logging

**Goal:** Fail-closed behavior and acquisition log.

**Deliverables:**

- Error/warning taxonomy mapping to [EAR-CONNECTOR-FAILURES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-FAILURES-v1.md)
- `acquisition-log.md` writer
- `connector-status.json` with `success` | `partial` | `failed` | `aborted`
- `read_only_attestation` field in status output

**Acceptance:**

- Simulated connection failure → `failed`, artefacts still written where possible
- Simulated scope violation → fail closed
- No secrets in log fixtures

**Out of scope:** External log aggregation product.

---

## R1.9 — Dry-run local test

**Goal:** End-to-end local test without live SFTP.

**Deliverables:**

- Mock SFTP server or filesystem-backed fake connector for CI/local
- Test suite covering: listing, exclusions, manifest, status, redaction
- Documented `pytest` or `python -m unittest` invocation

**Acceptance:**

- All [R1-TEST-STRATEGY-v1.md](R1-TEST-STRATEGY-v1.md) cases pass locally
- No network required for default test run

**Out of scope:** PILOT-001, production hosts.

---

## R1.10 — Pilot preflight

**Goal:** Operator checklist run against PILOT-001 TEST bindings — **not** full pilot execution.

**Deliverables:**

- Preflight checklist document or CLI `--mode preflight`
- Validates: input JSON template, credential_ref path exists (operator machine), output root writable, exclusions aligned with pilot sub-charter
- Preflight report artefact — no acquisition unless operator explicitly continues with Execution Authorization

**Acceptance:**

- Preflight fails clearly when PILOT bindings SAFE UNKNOWN
- Preflight does **not** imply PILOT-001 Execution Authorization
- Human sign-off required before any live acquisition run

**Out of scope:** PILOT-001 Execution, snapshot publish, OCPilot handoff.

---

## Implementation complete criteria

R1 implementation is **complete** when R1.1–R1.10 acceptance criteria pass and:

1. Connector completes scoped read-only plan under human supervision (TEST environment)
2. Outputs contract-shaped per connector contract (with R2 stub for `evidence_package_ref`)
3. No credentials in git-bound artefacts
4. [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) updated: R1 **IMPLEMENTED** (future milestone)

---

## Truth statement

This document defines tasks only. **No** code exists. **No** task has been executed.
