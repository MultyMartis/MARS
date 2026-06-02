# R1 — SFTP Read-Only Connector Implementation Charter v1

**Type:** Implementation authorization charter — **not** implementation, **not** code, **not** SFTP access, **not** pilot execution  
**Date:** 2026-06-02  
**Backlog item:** R1 — First SFTP Read-Only Connector  
**Readiness:** **CONDITIONAL GO** — [R1-IMPLEMENTATION-READINESS-REVIEW-v1.md](R1-IMPLEMENTATION-READINESS-REVIEW-v1.md)  
**Planning charter:** [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md)  
**Requirements baseline:** [R1-IMPLEMENTATION-CHARTER-REQUIREMENTS-v1.md](R1-IMPLEMENTATION-CHARTER-REQUIREMENTS-v1.md)

---

## Charter identity

| Field | Value |
|-------|-------|
| **Authorizes** | R1 implementation planning and code **only** — not R2–R5 unless separately chartered |
| **Does not authorize** | Live SFTP, PILOT-001 Execution, snapshot publish, OCPilot analysis, production access |
| **Human approver** | **Pending** — see [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md) |
| **Target pilot (design)** | PILOT-001 / SITE-001 / Автосалон СИБКАР — TEST, Level 1 |
| **Reference path** | CON-L1-A — [EAR-CONNECTED-PATHS-v1.md](../../shared/external-access-runtime/EAR-CONNECTED-PATHS-v1.md) |

---

## R1 mission

Create an **SFTP Read-Only Connector** capable of collecting file-system evidence for **EAR Evidence Package** generation (R2 input).

The connector must support:

| Capability | Requirement |
|------------|-------------|
| Read-only connection | Mode 2 only; no remote write/delete/rename/upload |
| Root listing | List entries at `scope.sftp_root` |
| Recursive listing | Traverse scoped directory tree under read-only plan |
| Default exclusions | Apply [EAR-DEFAULT-EXCLUSIONS-v1.md](../../shared/external-access-runtime/EAR-DEFAULT-EXCLUSIONS-v1.md) plus operator `excluded_paths` |
| File metadata | Path, size, mtime (and other contract fields as applicable) per manifest |
| Optional hashing policy | Configurable hash algorithm for manifest entries — default policy documented in implementation |
| Acquisition log | Human-inspectable run log with correlation to `acquisition_id` |
| Failure reporting | Contract-shaped status, errors, warnings — fail closed |
| No writes | Local output to external storage only; no remote mutation |

**R1 does NOT:**

- Build final Snapshot (R3)
- Publish Snapshot (R4)
- Analyze OpenCart or invoke OCPilot
- Modify remote or local site files beyond writing acquisition artefacts to external output root
- Access database, admin panel, or SSH shell
- Perform write operations on remote host

---

## Runtime technical decisions

| Decision | Selection | Rationale |
|----------|-----------|-----------|
| **Python version** | **3.12+** | Aligns with current LTS support window; satisfies readiness gap G-01 (version pin); sufficient for CLI tooling and paramiko without legacy compatibility burden |
| **Packaging** | **`requirements.txt`** | Minimal, human-operated install path; no poetry/uv lock-in for v1; satisfies G-02 with lowest ceremony; operator runs `python -m venv` + `pip install -r requirements.txt` |
| **Execution style** | **CLI-first** | Matches [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) and HITL discipline — explicit operator invocation, inspectable args, exit codes |
| **SFTP library** | **paramiko** | Mature Python SFTP/SSH client; LGPL license acceptable for internal tooling; read-only session achievable via API discipline (no write calls); satisfies G-03 |
| **Output storage** | **External storage, not repository** | Per [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) — bulk acquisition artefacts and logs stay outside git; repo holds code and charter docs only |
| **Runtime mode** | **Human-operated** | No autonomous or scheduled runs in v1; operator supplies inputs, approves execution, reviews outputs |

---

## R1 scope

### In scope

| Item | Notes |
|------|-------|
| SFTP connection using external `credential_ref` | Resolve at runtime from operator path — never from git |
| Read-only directory traversal | LIST/stat under scoped plan |
| Exclusion rules | Defaults + operator scope |
| File manifest generation | JSON + human-readable MD — R2 input |
| Evidence package draft | Raw acquisition folder structure + manifest inputs — **not** full Evidence Package (R2) |
| Acquisition log | Per-run artefact in external output root |
| Fail-closed behavior | Ambiguity, scope violation, read-only violation → stop with status |
| Safe unknown reporting | Explicit `safe-unknown.md` when bindings or paths unresolved |

### Out of scope

| Item | Owner / notes |
|------|---------------|
| DB access | Not SFTP Read-Only |
| SSH shell | Forbidden connector class |
| phpMyAdmin | Not R1 |
| OpenCart admin | Not R1 |
| Snapshot publishing | R4 |
| OCPilot analysis | Consumer scope |
| File writes (remote) | Mode 3 forbidden |
| Remote delete / move / upload | Read-only violation |
| Cache reset | Operational write — forbidden |
| Product import | Forbidden |
| Controller / theme edits | Forbidden |

---

## Implementation boundaries

### Code placement

R1 may create code **only** under:

```
projects/ear-runtime/runtime/
```

**Future implementation paths** (chartered, not yet created):

| Path | Role |
|------|------|
| `runtime/cli.py` | CLI entrypoint |
| `runtime/connectors/` | Connector implementations (R1 SFTP first) |
| `runtime/shared/` | Config binding, logging helpers, common types |
| `runtime/validators/` | Input validation (R1 scope: connector input) |

**Forbidden code locations:**

- `shared/external-access-runtime/` — architecture only; amendments via Architecture Amendment Charter
- Repository root or unrelated `projects/` trees

### R1 vs R2 contract boundary

| Connector contract field | R1 behavior |
|--------------------------|-------------|
| Raw acquisition artefacts | **R1 produces** — external bulk root |
| `connector-status.json` | **R1 produces** — contract-shaped |
| `file-manifest.json` / `.md` | **R1 produces** — R2 input |
| `evidence_package_ref` | **R1 stub** — points to draft folder or `null` with note that R2 assembles full Evidence Package per [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) |
| Published snapshot | **Not R1** — R3/R4 |

---

## Expected outputs

R1 writes outputs to **operator-configured external output root** (not git). Expected artefacts per run:

| Artefact | Purpose |
|----------|---------|
| `acquisition-log.md` | Human-readable run summary — timestamps, scope, counts, status |
| `file-manifest.json` | Machine-readable manifest — R2 input |
| `file-manifest.md` | Human-readable manifest summary |
| `safe-unknown.md` | Present when unresolved bindings, skipped ambiguous paths, or partial scope |
| `connector-status.json` | Contract-shaped completion status |

**Forbidden in outputs:**

- Raw credentials (passwords, private keys, session tokens)
- Unredacted config secrets from remote files (if config paths included, redaction plan applies before any git-bound copy)

---

## Credential binding

| Rule | Detail |
|------|--------|
| Input | Connector accepts **`credential_ref` only** — path or URI to external secret material |
| Storage | Credentials **stay outside repo** — [EAR-CREDENTIAL-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-CREDENTIAL-BOUNDARY-v1.md) |
| PILOT-001 | CredentialProvider secrets path per pilot sub-charter §4 — **SAFE UNKNOWN** until operator sign-off; charter does not invent paths |
| Resolution | Runtime reads secret file at execution time; never copies to git |
| Logging | Logs record `credential_ref` identifier only — **never** secret values |
| Git | No passwords, keys, or dumps in commits |

---

## Default exclusions

**Authoritative source:** [shared/external-access-runtime/EAR-DEFAULT-EXCLUSIONS-v1.md](../../shared/external-access-runtime/EAR-DEFAULT-EXCLUSIONS-v1.md)

R1 exclusion engine applies defaults unless operator `scope.excluded_paths` or pilot binding adds stricter rules. Defaults include:

| Category | Paths / patterns |
|----------|------------------|
| Cache | `image/cache/`, `system/storage/cache/`, `cache/` |
| Logs | `system/storage/logs/`, `logs/`, `*.log` |
| Sessions | `system/storage/session/` |
| Uploads | `system/storage/upload/` |
| Temp | `tmp/`, `temp/` |
| Backups | `backup/`, `backups/` |
| VCS | `.git/` |
| Additional (architecture) | `system/storage/modification/`, `vqmod/vqcache/`, `node_modules/` |

Operator may add pilot-specific exclusions (e.g. bulk `image/` policy for Level 1) via scope — must not silently remove security-critical exclusions without risk register entry.

---

## CLI entrypoint (planned)

| Aspect | Planned binding |
|--------|-----------------|
| Entry | `python -m runtime.cli` or `runtime/cli.py` |
| Required args | `--input` (connector input JSON path), `--output-root` (external bulk root) |
| Modes | `test-connection`, `list`, `acquire` (dry-run default where applicable) |
| Exit codes | `0` success/partial with artefacts; non-zero fail-closed |

Detailed CLI spec deferred to R1.1 implementation task.

---

## Logging and failure reporting

| Aspect | Binding |
|--------|---------|
| Format | Structured text in `acquisition-log.md`; JSON status in `connector-status.json` |
| Fields | `acquisition_id`, `site_ref`, timestamps, path counts, exclusion summary, status |
| Secrets | Never logged |
| Failures | Map to [EAR-CONNECTOR-FAILURES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-FAILURES-v1.md) classes — `scope_violation`, `read_only_violation`, `connection_failed`, etc. |
| Status values | `success`, `partial`, `failed`, `aborted` |

---

## Governance gates acknowledged

| Gate | Status |
|------|--------|
| R1 Implementation Charter human approval | **Required before first R1 code merge** — see [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md) |
| PILOT-001 Execution Authorization | **Separate** — not implied by this charter |
| Architecture amendment | Required for contract changes — not runtime PR |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Updated when implementation starts |

---

## Related documents

| Document | Role |
|----------|------|
| [R1-IMPLEMENTATION-TASKS-v1.md](R1-IMPLEMENTATION-TASKS-v1.md) | Safe implementation task breakdown |
| [R1-TEST-STRATEGY-v1.md](R1-TEST-STRATEGY-v1.md) | Non-production test plan |
| [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md) | Human approval gate |
| [RUNTIME-STRUCTURE-v1.md](RUNTIME-STRUCTURE-v1.md) | Proposed layout |

---

## Truth statement

| Claim | Accurate? |
|-------|-----------|
| R1 code exists | **No** |
| This charter authorizes live SFTP | **No** |
| This charter authorizes PILOT-001 Execution | **No** |
| Human approval recorded | **Pending** — charter drafted 2026-06-02 |
