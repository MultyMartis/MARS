# R1 — Test Strategy v1

**Type:** Test plan for R1 SFTP Read-Only Connector — **not** test code, **not** live SFTP by default  
**Date:** 2026-06-02  
**Charter:** [R1-IMPLEMENTATION-CHARTER-v1.md](R1-IMPLEMENTATION-CHARTER-v1.md)  
**Tasks:** [R1-IMPLEMENTATION-TASKS-v1.md](R1-IMPLEMENTATION-TASKS-v1.md)

**Principle:** First tests run **without live SFTP**. Mock or local fake tree validates core behavior before operator TEST host access.

---

## Test environment tiers

| Tier | Description | When |
|------|-------------|------|
| **T0 — Local unit** | Pure Python, no network | R1.2 onward — default CI/local |
| **T1 — Mock SFTP** | In-process or local mock server | R1.3–R1.9 |
| **T2 — Operator TEST host** | Real SFTP to PILOT-001 TEST | R1.3+ optional; R1.10 preflight — **human only** |
| **T3 — PILOT Execution** | Full pilot acquisition | **NOT R1 test scope** — separate Execution Authorization |

**Default gate:** T0 + T1 must pass before T2 is attempted.

---

## Test cases

### TC-01 — Local fake tree test

**Purpose:** Validate listing and manifest generation without network.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Create fixture directory tree mimicking OpenCart layout (admin, catalog, system/storage/…) | Fixture ready |
| 2 | Run connector against fake filesystem adapter or mock SFTP mapping fixture paths | Traversal completes |
| 3 | Inspect `file-manifest.json` | Entries match expected paths and metadata |
| 4 | Inspect `connector-status.json` | `success` or `partial` as appropriate |

**Tier:** T0/T1  
**Live SFTP:** No

---

### TC-02 — Exclusion test

**Purpose:** Default exclusions applied correctly.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Fixture includes paths under `image/cache/`, `system/storage/logs/`, `tmp/`, `.git/` | Present in fixture |
| 2 | Run acquisition/list against fixture | Excluded paths absent from manifest entries |
| 3 | Inspect manifest metadata | Exclusion policy documented |
| 4 | Add operator `excluded_paths` in input | Additional paths excluded |

**Reference:** [EAR-DEFAULT-EXCLUSIONS-v1.md](../../shared/external-access-runtime/EAR-DEFAULT-EXCLUSIONS-v1.md)

**Tier:** T0/T1  
**Live SFTP:** No

---

### TC-03 — Manifest format test

**Purpose:** R2-ready manifest structure.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Run manifest builder on known fixture | `file-manifest.json` valid JSON |
| 2 | Required fields present: acquisition correlation, entries array, exclusion metadata | Schema documented in implementation PR |
| 3 | `file-manifest.md` human summary matches JSON counts | Consistent |
| 4 | Empty allowed scope | Valid empty manifest, status explains |

**Tier:** T0  
**Live SFTP:** No

---

### TC-04 — Credential redaction test

**Purpose:** No secrets in logs or status artefacts.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Input JSON with `credential_ref` pointing to fixture secret file (test-only) | Resolved at runtime in test |
| 2 | Simulate connection failure and success paths | Logs contain ref id only |
| 3 | Grep acquisition-log, connector-status, stderr capture | No password/key material |
| 4 | Input JSON containing inline password field | Validation rejects before connect |

**Tier:** T0/T1  
**Live SFTP:** No

---

### TC-05 — Fail-closed test

**Purpose:** Errors stop safely with contract status.

| Case | Trigger | Expected |
|------|---------|----------|
| FC-01 | Invalid `ear_mode` (not 2) | Validation error, non-zero exit, no connect |
| FC-02 | Missing required input field | Fail before network |
| FC-03 | Connection refused (mock) | `failed` status, error class `connection_failed` |
| FC-04 | Path outside `allowed_paths` | `scope_violation` or skip policy per charter |
| FC-05 | Ambiguous `credential_ref` | Fail closed, `safe-unknown.md` or error record |

**Reference:** [EAR-CONNECTOR-FAILURES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-FAILURES-v1.md)

**Tier:** T0/T1  
**Live SFTP:** No

---

### TC-06 — No-write policy test

**Purpose:** Read-only enforcement — no remote mutation.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Code review checklist: no `put`, `rename`, `remove`, `mkdir` on SFTP client in acquire path | Absent or unreachable |
| 2 | Mock SFTP records invoked methods | Only read/list/stat allowed |
| 3 | If write API accidentally called in test double | `read_only_violation`, fail closed |
| 4 | Local output writes only under `--output-root` | No writes to repo or remote |

**Tier:** T0/T1 (+ static review)  
**Live SFTP:** No

---

## Optional extended tests (post R1.9)

| ID | Name | Tier | Notes |
|----|------|------|-------|
| TC-07 | Connection test mode | T1/T2 | `test-connection` subcommand |
| TC-08 | Partial acquisition | T1 | Some paths skipped → `partial` status |
| TC-09 | Hash policy flag | T0 | When enabled, manifest entries include hash |
| TC-10 | Large directory cap | T1 | Warning or stop per size policy if chartered |

---

## Test artefacts

| Artefact | Location |
|----------|----------|
| Fixture trees | `runtime/tests/fixtures/` (created in R1.9 — not yet) |
| Mock SFTP | `runtime/tests/mock_sftp/` or pytest plugin |
| Test results | Local only — not committed unless operator policy says otherwise |

---

## What this strategy does not cover

| Item | Reason |
|------|--------|
| PILOT-001 full execution | Separate Execution Authorization |
| R2 Evidence Package validation | R2 charter |
| Snapshot quality Level 1 proof | R3/R4 + OCPilot |
| Production host | Forbidden in R1 non-goals |
| Performance / load testing | Out of scope v1 |

---

## Acceptance for test strategy

Test strategy is **satisfied** when:

1. TC-01 through TC-06 implemented and passing at T0/T1
2. Default developer workflow documented (`pytest` or equivalent)
3. T2 runs documented as operator-only optional step
4. No test commits real credentials

---

## Truth statement

**No** test code exists. **No** live SFTP required for first tests. This document is plan only.
