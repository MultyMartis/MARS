# EAR Mock E2E Flow v1

**Type:** Runtime orchestration milestone record  
**Phase:** Mock E2E Flow — first in-memory pipeline wiring  
**Date:** 2026-06-07  
**Engine:** [runtime/engines/ear_mock_e2e_engine.py](runtime/engines/ear_mock_e2e_engine.py)  
**State:** [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md)

---

## Purpose

Wire existing runtime skeleton components into a single **mock-only**, **in-memory** end-to-end flow:

```
Config → Contract Evidence → Candidate Snapshot → Validate Engine → Publish Engine → E2E Bundle
```

Orchestration only — no new business rules, no architecture contract changes, no live access.

---

## Flow

| Stage | Component | Output |
|-------|-----------|--------|
| 1 | `load_config()` or dict accept | Validated config |
| 2 | Mock listing → manifest → `build_contract_evidence_package()` | R2 `EvidencePackage` |
| 3 | `build_candidate_snapshot_package()` | R3 `SnapshotPackage` |
| 4 | `run_validate()` | R5 `ValidateEngineOutput` |
| 5 | `run_publish()` (`in_memory_path=True`) | R4 `PublishEngineOutput` |
| 6 | `E2EMockBundle` assembly | Bundle + `E2EFlowSummary` |

Upstream mock path reuses the same builders/validators as `--contract-evidence` / `--contract-snapshot` CLI flags. No `SFTPConnector` network calls.

---

## Inputs

| Input | Source | Notes |
|-------|--------|-------|
| Config dict or path | `runtime/configs/*.json` | Path validated via `load_config()` |
| Mock listing | `shared/mock_listing.py` | Fixed mock entries; no remote listing |
| Connector metadata | In-engine stub | `connector_status: success` only |
| Validate preconditions | R2/R3 structural validation results | Passed as `r2_structural_pass` / `r3_assembly_pass` |
| Publish HITL | Function kwargs | Default `hitl_approved=True` for mock success path |

Sample fixture: [runtime/configs/sample-r1-site-001.json](runtime/configs/sample-r1-site-001.json)

---

## Outputs

`E2EMockBundle` contains:

| Field | Type |
|-------|------|
| `config` | Resolved config dict (redacted-safe subset in `to_dict()`) |
| `evidence_package` | R2.1 `EvidencePackage` |
| `snapshot_package` | R3.1 `SnapshotPackage` |
| `validate_output` | R5 `ValidateEngineOutput` |
| `publish_output` | R4 `PublishEngineOutput` |
| `summary` | `E2EFlowSummary` — status, id linkage, boundary flags |

No filesystem persistence. No Store writes. No consumer registry execution.

---

## ID linkage

Verified in-engine after Publish:

| Link | Rule |
|------|------|
| Evidence → Snapshot | `evidence.identity.acquisition_id == snapshot.identity.acquisition_id` |
| Validate → Snapshot | `validation_result.audit.validated_snapshot_id == snapshot_id` |
| Report → Result | `validate_report.result_ref == validation_result.result_id` |
| Eligibility → Validate | `publish_eligibility.validation_result_ref` + `validate_report_ref` |
| Publish → Validate | `publish_result.validation_result_ref` + `publish_recommendation_ref` |
| Published snapshot → Validate | `published_snapshot.publication.validation_result_ref` |

Mock snapshot IDs use `snap-mock-{site_id}-{connector}` prefix (ID-R3-14 dry-run path).

---

## Limitations

| Boundary | Status |
|----------|--------|
| Live SFTP / network | **FORBIDDEN** — not invoked |
| Real R5 validation rules | **NOT IMPLEMENTED** — mock assessors only |
| Store persistence | **NOT PERFORMED** |
| Publish persistence | **NOT PERFORMED** |
| Consumer registry | **NOT IMPLEMENTED** |
| Quarantine expansion | **NOT PERFORMED** |
| Production snapshot IDs | **NOT USED** — mock prefix only |
| PILOT-001 / SITE-001 execution | **NOT AUTHORIZED** — config fixture only |
| CLI integration | **NOT ADDED** — engine callable from Python / `__main__` verification |

Config fixture echoes `site_id: SITE-001` as R1 sample shape only; flow remains mock/dry-run.

---

## Validation result

**Executed:** 2026-06-07  
**Command:** `py -3 engines/ear_mock_e2e_engine.py` (from `runtime/`)

| Check | Result |
|-------|--------|
| Config loaded | **PASS** — `sample-r1-site-001.json` |
| Evidence package created | **PASS** — `acq-mock-SITE-001-mock` |
| Candidate snapshot created | **PASS** — `snap-mock-SITE-001-sftp_readonly` |
| R2 structural validation | **PASS** |
| R3 assembly validation | **PASS** |
| Validate Engine | **PASS** — `validation_status: PASS` |
| Publish Engine | **SUCCESS** — `publish_result_state: SUCCESS` |
| ID linkage | **PASS** — `ids_linked: True` |
| Filesystem writes | **NONE** |
| Network access | **NONE** |
| Safe-unknown entries | **10** (expected on empty-scope mock path) |

---

## Next steps

1. Optional CLI flag `--mock-e2e` (only if human gate approves CLI surface expansion).
2. Negative-path fixtures (Validate FAIL, Publish BLOCKED/DEFERRED) as separate verification cases.
3. Store placement gate with mock Store adapter (still no production paths).
4. Human gate review before any live PILOT-001 authorization.
5. Real R5 assessors and R4 Store adapter — separate implementation phases.

---

## Boundary compliance

| Rule | Compliance |
|------|------------|
| No architecture contract edits | **YES** |
| No live access | **YES** |
| No SFTP execution | **YES** |
| No Store writes | **YES** |
| Orchestrate existing components only | **YES** |
| Standard library only (engine module) | **YES** |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Production snapshot ID algorithm | **SAFE UNKNOWN** — mock prefix only per `handoff_contract.py` |
| Real Store placement confirmation | **NOT EXERCISED** — bypassed via `in_memory_path=True` |
| Consumer visibility execution | **NOT EXERCISED** — logical grant in Publish skeleton only |
