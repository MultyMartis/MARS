# SITE-001 Dry Run Execution v1

**Type:** Operator dry-run completion record — mock/in-memory path only  
**Site:** `SITE-001` (Автосалон СИБКАР)  
**Pilot:** `PILOT-001` — SFTP Read-Only, Mode 2, TEST, Snapshot Level 1  
**Run date:** 2026-06-07  
**Dry-run session id:** `dryrun-site001-20260607-001`  
**Operator:** `cursor-agent` (automated operator rehearsal)  
**Branch:** `mars/post-cycle8-live-tests`  
**Pre-dryrun tag:** `ear-pre-dryrun-2026-06`  
**Baseline tag:** `ear-stable-baseline-2026-06`  
**Plan:** [SITE-001-DRY-RUN-PLAN-v1.md](SITE-001-DRY-RUN-PLAN-v1.md)  
**Authorization:** [EXECUTION-AUTHORIZATION-DECISION-v1.md](EXECUTION-AUTHORIZATION-DECISION-v1.md) — **AUTHORIZED WITH NOTES** (HG-0)  
**Decision companion:** [SITE-001-DRY-RUN-DECISION-v1.md](SITE-001-DRY-RUN-DECISION-v1.md)

---

## Document boundary (mandatory)

| Rule | Status |
|------|--------|
| Live SFTP / connected acquisition | **NOT PERFORMED** |
| Credential resolution | **NOT PERFORMED** |
| Network activity | **NONE** |
| Production snapshot IDs | **NOT USED** — mock prefix only |
| Consumer / OCPilot publication | **NOT PERFORMED** |
| PILOT-001 execution authorization | **NO** (unchanged) |
| Dry run authorizes live pilot | **NO** |

**Truth statement:** This record documents **operator rehearsal** on the mock/in-memory path only. Success here is input to **HG-4 Execution Authorization Review** — not automatic live pilot approval.

---

## 1. Authorization and boundaries confirmed

| Boundary | Confirmed |
|----------|-----------|
| NO SFTP | **YES** — `SFTPConnector.connect()` not invoked |
| NO credentials | **YES** — `credential_ref: SAFE_UNKNOWN_EXTERNAL_REF` unresolved |
| NO network | **YES** — mock listing only; `network_access: false` in E2E summary |
| NO live acquisition | **YES** — contract R2/R3 mock path |
| NO consumer publication | **YES** — logical visibility grant only |
| HG-0 Dry Run Execution Authorization | **AUTHORIZED WITH NOTES** |
| PILOT-001 Execution Authorization | **NO** |

---

## 2. Commands executed

All commands run from `projects/ear-runtime/runtime/`. No network. No credential files opened.

### Phase 0 — Baseline review

| Step | Command / action | Result |
|------|------------------|--------|
| 0.1–0.3 | Read plan, authorization decision, baseline limitations | Acknowledged |
| 0.4 | Inspect `configs/sample-r1-site-001.json` | `dry_run: true`, `site_id: SITE-001`, `pilot_id: PILOT-001` |
| 0.5 | Session id assigned | `dryrun-site001-20260607-001` |

### Phase 1 — Config and upstream mock inputs

```
py -3 -c "… load_config('configs/sample-r1-site-001.json') …"
```

| Check | Observed |
|-------|----------|
| Config load | **PASS** |
| `dry_run` | `true` |
| `credential_ref` | `SAFE_UNKNOWN_EXTERNAL_REF` (unresolved) |
| `allowed_paths` | `[]` (empty — scope echo documented) |
| `excluded_paths` | 11 entries present |

### Phase 2 — R2 Evidence rehearsal

```
py -3 cli.py --config configs/sample-r1-site-001.json --contract-evidence
```

| Artefact | Observed |
|----------|----------|
| `acquisition_id` | `acq-mock-SITE-001-mock` |
| `site_ref` | `SITE-001` |
| `connector_class` | `sftp_readonly` |
| `artifact_count` | 2 |
| R2 structural validation | **PASS** |

### Phase 3 — R3 Snapshot rehearsal

```
py -3 cli.py --config configs/sample-r1-site-001.json --contract-snapshot
```

| Artefact | Observed |
|----------|----------|
| `snapshot_id` | `snap-mock-SITE-001-sftp_readonly` |
| `acquisition_id` continuity | `acq-mock-SITE-001-mock` (matches R2) |
| `safe_unknown_count` | 10 |
| `package_quality_level` | 0 (candidate / pre-Validate) |
| R3 assembly validation | **PASS** |

### Phase 4 — R5 Validate rehearsal

Via mock E2E orchestration and inline engine invocation:

```
py -3 engines/ear_mock_e2e_engine.py
```

| Artefact | Observed |
|----------|----------|
| `validation_status` | **PASS** |
| `PublishEligibilityRecommendation` | **ELIGIBLE** (advisory) |
| `validated_snapshot_id` | `snap-mock-SITE-001-sftp_readonly` |
| Validate Report sections | Eleven sections populated (summary, identity_review, structure_review, possession_review, quality_assessment, redaction_review, readiness_review, consistency_review, blockers, warnings, audit_trail) |
| Skeleton assessor limitation | Acknowledged — real R5-V-* rules **NOT IMPLEMENTED** |

### Phase 5 — Validate HITL sign-off (HG-1)

| Field | Value |
|-------|-------|
| Validate sign-off ref | `hitl:validate:dryrun-site001-20260607-001:cursor-agent` |
| Blockers reviewed | Empty on happy path |
| Warnings reviewed | Scope-echo warnings acknowledged (empty `allowed_paths`) |
| Eligibility advisory noted | ELIGIBLE — advisory only |
| Mock Store drill | **NOT PERFORMED** (optional; in-memory path sufficient) |

### Phase 6 — R4 Publish rehearsal

Happy path with HG-1 on record and `in_memory_path=True`:

| Artefact | Observed |
|----------|----------|
| `publish_result_state` | **SUCCESS** |
| `PublishedSnapshot` | Present; cites `validation_result_ref` |
| `PublishMetadata` | Present in bundle |
| Consumer visibility | **granted** (logical only — no OCPilot execution) |
| R4 re-Validation | **NOT performed** — boundary preserved |

### Phase 7 — Publish HITL approval (HG-2 / G4)

| Field | Value |
|-------|-------|
| Publish approval ref | `hitl:publish:dryrun-site001-20260607-001:cursor-agent` |
| Distinct from Validate sign-off | **YES** |
| Consumer handoff executed | **NO** |

### Phase 8 — Completion review

This document satisfies §9 exit artefact requirements.

---

## 3. Happy path — observed outputs

**Primary verification command:**

```
py -3 engines/ear_mock_e2e_engine.py
```

**Output:**

```
ear_mock_e2e_engine verification: PASS
  config: C:\AI MARS\projects\ear-runtime\runtime\configs\sample-r1-site-001.json
  snapshot_id: snap-mock-SITE-001-sftp_readonly
  acquisition_id: acq-mock-SITE-001-mock
  validation_status: PASS
  publish_result_state: SUCCESS
  ids_linked: True
  safe_unknown_count: 10
```

**Operator HITL path (explicit refs):**

```
py -3 -c "… run_mock_e2e_flow(…, validate_sign_off_ref='hitl:validate:…', operator_publish_approval_ref='hitl:publish:…') …"
```

| Expected | Observed |
|----------|----------|
| `validation_status: PASS` | **PASS** |
| `publish_result_state: SUCCESS` | **SUCCESS** |
| `ids_linked: True` | **True** |
| `network_access: false` | **false** |
| `store_writes: false` | **false** |

---

## 4. Artefact chain and ID linkage

| Link | Rule | Observed |
|------|------|----------|
| R2 → R3 | `acquisition_id` continuity | **PASS** — `acq-mock-SITE-001-mock` |
| R3 identity | Mock prefix `snap-mock-*` | **PASS** — `snap-mock-SITE-001-sftp_readonly` |
| R5 → R3 | `validated_snapshot_id` match | **PASS** |
| R5 bundle | `result_ref` / eligibility refs coherent | **PASS** |
| R4 → R5 | `validation_result_ref` + recommendation ref | **PASS** |
| Published snapshot → Validate | `publication.validation_result_ref` | **PASS** |
| Full chain | Evidence → Snapshot → Validate → Publish | **COMPLETE** |

**Artefact ids (happy path):**

| Field | Value |
|-------|-------|
| `acquisition_id` | `acq-mock-SITE-001-mock` |
| `snapshot_id` | `snap-mock-SITE-001-sftp_readonly` |
| `validation_result_ref` | `validate-snap-mock-SITE-001-sftp_readonly-{timestamp}` |
| `publish_result_state` | `SUCCESS` |

---

## 5. HITL checkpoints

| Gate | Ref | Status |
|------|-----|--------|
| **HG-0** Dry Run Execution Authorization | [EXECUTION-AUTHORIZATION-DECISION-v1.md](EXECUTION-AUTHORIZATION-DECISION-v1.md) | **AUTHORIZED WITH NOTES** (pre-run) |
| **HG-1** Validate sign-off | `hitl:validate:dryrun-site001-20260607-001:cursor-agent` | **RECORDED** |
| **HG-2** Publish approval (G4) | `hitl:publish:dryrun-site001-20260607-001:cursor-agent` | **RECORDED** |
| **HG-3** Pilot boundary acknowledgment | PILOT-001 **NOT AUTHORIZED** | **ACKNOWLEDGED** |
| **HG-4** Live pilot input review | — | **NOT STARTED** (post dry-run) |

---

## 6. Negative paths exercised

Executed via inline Python with `sys.path` set to runtime root (table-top + engine invocation per plan §6).

| ID | Scenario | Trigger | Expected | Observed |
|----|----------|---------|----------|----------|
| **NP-R3-FAIL** | R3 assembly fail → R5 | `r3_assembly_pass=False` | Validate **FAIL**; Publish blocked | `validation_status: FAIL`; `publish_result_state: BLOCKED` |
| **NP-R5-NE** | NOT_ELIGIBLE | `recommendation_state=NOT_ELIGIBLE` | Publish **BLOCKED** | `publish_result_state: BLOCKED` |
| **NP-HITL** | Missing Publish HITL | `hitl_approved=False` | **DEFERRED** | `publish_result_state: DEFERRED` |
| **NP-R2 / NP-R3 missing** | — | Not auto-exercised | STOP before downstream | **TABLE-TOP** — operator procedure documented in plan §6 |
| **NP-LIVE** | Forbidden live activity | — | **ABORT** | **NOT ATTEMPTED** — no SFTP, credentials, or network |

**Note:** `py -3 engines/ear_publish_engine.py` fails with `ModuleNotFoundError: No module named 'shared'` when run directly (missing runtime root on `sys.path`). Negative Publish paths were verified via inline invocation with path setup. **Not treated as execution-blocking** — workaround documented; no runtime code changed per dry-run restrictions.

---

## 7. Success criteria matrix (SC-DR-01–08)

| ID | Criterion | Result |
|----|-----------|--------|
| SC-DR-01 | Artifact chain complete | **PASS** |
| SC-DR-02 | ID continuity preserved | **PASS** |
| SC-DR-03 | Stage boundaries respected | **PASS** |
| SC-DR-04 | No forbidden live activity | **PASS** |
| SC-DR-05 | Human gates recorded | **PASS** |
| SC-DR-06 | Mock path explicit | **PASS** — mock listing + in-memory Publish |
| SC-DR-07 | Completion review authored | **PASS** — this document |
| SC-DR-08 | Pilot boundary stated | **PASS** — see §10 |

---

## 8. Boundary compliance

| Rule | Compliance |
|------|------------|
| No SFTP execution | **YES** |
| No credential resolution | **YES** |
| No network sockets | **YES** |
| No production snapshot IDs | **YES** — mock prefix only |
| No Store writes (in-memory path) | **YES** |
| No consumer publication | **YES** |
| No runtime code changes | **YES** |
| R4 did not re-Validate | **YES** |
| R5 did not Publish | **YES** — advisory eligibility only |

---

## 9. SAFE UNKNOWN encountered

| Topic | Status | Notes |
|-------|--------|-------|
| Production snapshot ID algorithm | **SAFE UNKNOWN** | Mock prefix only on dry-run path |
| SITE-001 `credential_ref` / `remote_root` | **SAFE UNKNOWN** | Fixture placeholders |
| Real Level 1 evidence bar | **SAFE UNKNOWN** | Skeleton assessors; 10 safe-unknown entries on mock path |
| Store placement confirmation | **NOT EXERCISED** | Bypassed via `in_memory_path=True` |
| Whether table-top negative paths satisfy HG-4 | **SAFE UNKNOWN** | Program owner review criteria |
| `ear_publish_engine.py` standalone `__main__` | **OBSERVED DEBT** | Requires runtime root on `sys.path`; mock E2E path unaffected |

---

## 10. Closure statement

**Dry Run does NOT authorize Live Pilot.**

PILOT-001 Execution Authorization remains **NO**. Connected SFTP acquisition, credential vault resolution, production snapshot IDs, real R5 assessors, R4 Store adapter, and consumer publication remain blocked until explicit future human gates (HG-4 → PILOT-001 Execution Authorization).

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-07 | **CREATED** — SITE-001 Dry Run Execution v1; mock/in-memory path; happy path PASS; negative paths exercised; HG-1/HG-2 recorded |
