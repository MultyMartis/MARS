# EAR Mock E2E — Readiness Review v1

**Type:** Runtime gate review — **no** implementation, **no** contract edits, **no** live access, **no** SITE-001 execution authorization  
**Date:** 2026-06-07  
**Phase:** Mock E2E Flow — readiness for SITE-001 dry-run **planning**  
**Flow record:** [EAR-MOCK-E2E-FLOW-v1.md](EAR-MOCK-E2E-FLOW-v1.md)  
**State:** [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md)  
**Decision companion:** [EAR-MOCK-E2E-READINESS-DECISION-v1.md](EAR-MOCK-E2E-READINESS-DECISION-v1.md)

**Explicit exclusions:** Live SFTP, Store writes, production snapshot IDs, PILOT-001 execution, OCPilot consumer execution, architecture contract changes, real R5 assessors, R4 Store adapter.

---

## Executive summary

The mock E2E runtime wires Config → R2 Evidence → R3 Candidate Snapshot → R5 Validate → R4 Publish into a single in-memory orchestration path. Verification on `sample-r1-site-001.json` **PASS**es with `validation_status: PASS`, `publish_result_state: SUCCESS`, and `ids_linked: True`. Boundaries are preserved: no network, no Store writes, mock listing only, skeleton assessors only.

**Recommendation:** **READY FOR SITE-001 DRY-RUN PLANNING WITH NOTES** — operators may draft dry-run checklists, operator HITL sequences, and evidence expectations using the mock E2E bundle shape; this does **not** authorize live acquisition or PILOT-001 execution.

---

## Sources reviewed

| ID | Source | Role |
|----|--------|------|
| S-E2ER-01 | [runtime/engines/ear_mock_e2e_engine.py](runtime/engines/ear_mock_e2e_engine.py) | Mock E2E orchestrator |
| S-E2ER-02 | [runtime/engines/ear_validate_engine.py](runtime/engines/ear_validate_engine.py) | R5 Validate skeleton |
| S-E2ER-03 | [runtime/engines/ear_publish_engine.py](runtime/engines/ear_publish_engine.py) | R4 Publish skeleton |
| S-E2ER-04 | [runtime/configs/sample-r1-site-001.json](runtime/configs/sample-r1-site-001.json) | SITE-001 shape fixture |
| S-E2ER-05 | [EAR-MOCK-E2E-FLOW-v1.md](EAR-MOCK-E2E-FLOW-v1.md) | Flow milestone record |
| S-E2ER-06 | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Program status |
| S-E2ER-07 | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation index |
| S-E2ER-08 | [shared/external-access-runtime/PILOT-001-SITE-001-ASSESSMENT-PLAN-v1.md](../../shared/external-access-runtime/PILOT-001-SITE-001-ASSESSMENT-PLAN-v1.md) | Pilot assessment context |

**Verification executed (this review):**

```
py -3 engines/ear_mock_e2e_engine.py   # from runtime/
→ ear_mock_e2e_engine verification: PASS
  snapshot_id: snap-mock-SITE-001-sftp_readonly
  acquisition_id: acq-mock-SITE-001-mock
  validation_status: PASS
  publish_result_state: SUCCESS
  ids_linked: True
  safe_unknown_count: 10
```

---

## Assessment matrix

| # | Question | Verdict | Notes |
|---|----------|---------|-------|
| 1 | Mock E2E complete enough for dry-run **planning**? | **YES WITH NOTES** | Full in-memory chain operational; planning artefacts (operator checklist, HITL sequence, evidence bar) can reference `E2EMockBundle` shape. Not sufficient for live dry-run **execution**. |
| 2 | R2 → R3 → R5 → R4 linkages consistent? | **YES** | Handoff via shared objects; preconditions propagated; R4 consumes R5 bundle read-only. |
| 3 | IDs linked correctly? | **YES** | `_verify_id_linkage` checks seven ref chains; verification `ids_linked: True`. |
| 4 | Validate and Publish outputs separated? | **YES** | Distinct dataclass bundles; R5 emits advisory eligibility; R4 emits authoritative PublishResult; dual HITL refs preserved. |
| 5 | Boundaries preserved? | **YES** | No network/Store in E2E; mock assessors; mock snapshot prefix; production path rejects mock IDs. |
| 6 | Missing before SITE-001 dry-run? | See § Missing for dry-run | Plan document, negative-path fixtures, credential/remote resolution, optional CLI. |
| 7 | Missing before live SITE-001 execution? | See § Missing for live | PILOT authorization, live SFTP, real assessors, Store adapter, production IDs. |
| 8 | Testable now without live access? | See § Testable now | Mock E2E, per-engine smoke, config validation, manual negative paths. |

---

## Linkage review

### Flow topology

```
Config (load_config / dict)
  ↓ mock listing → manifest
R2 EvidencePackage          ← build_contract_evidence_package + validate_contract_evidence_package
  ↓ acquisition_id handoff
R3 SnapshotPackage            ← build_candidate_snapshot_package + validate_candidate_snapshot_package
  ↓ snapshot_id + r2/r3 precondition flags
R5 ValidateEngineOutput       ← run_validate (7 stages, mock assessors)
  ↓ validation_result + validate_report + publish_eligibility_recommendation
R4 PublishEngineOutput        ← run_publish (7 stages, in_memory_path=True)
  ↓
E2EMockBundle + E2EFlowSummary
```

### Stage-by-stage linkage

| Transition | Input consumed | Output produced | Consistency |
|------------|----------------|-----------------|-------------|
| Config → R2 | `site_id`, `pilot_id`, `connector`, `mode`, `snapshot_target` | `EvidencePackage` | Config fields drive identity; connector metadata stub `{connector_status: success}` |
| R2 → R3 | `EvidencePackage` + R2 validation dict | `SnapshotPackage` | `evidence.identity.acquisition_id == snapshot.identity.acquisition_id` verified |
| R3 → R5 | `SnapshotPackage` + `target_certify_level` from `snapshot_target` | `ValidateEngineOutput` | `validated_snapshot_id`, report `snapshot_id`, eligibility `snapshot_id` aligned |
| R5 → R4 | Full R5 bundle + HITL kwargs | `PublishEngineOutput` | `validation_result_ref`, `publish_recommendation_ref`, `validate_report.result_ref` coherent |
| R4 promotion | R5 certified level | `PublishedSnapshot` | Frozen quality from R5 summary; `validation_result_ref` on publication record |

### ID linkage rules (verified in-engine)

| Link | Rule | Status |
|------|------|--------|
| Evidence → Snapshot | `acquisition_id` match | **PASS** |
| Validate → Snapshot | `validation_result.audit.validated_snapshot_id == snapshot_id` | **PASS** |
| Report → Result | `validate_report.result_ref == validation_result.result_id` | **PASS** |
| Eligibility → Validate | `validation_result_ref` + `validate_report_ref` | **PASS** |
| Publish → Validate | `publish_result.validation_result_ref` + `publish_recommendation_ref` | **PASS** |
| Published snapshot → Validate | `publication.validation_result_ref` | **PASS** |

Mock ID pattern: `snap-mock-{site_id}-{connector}` per [handoff_contract.py](runtime/shared/handoff_contract.py) ID-R3-14.

---

## Boundary review

### Mock E2E engine boundaries

| Boundary | Declared | Observed |
|----------|----------|----------|
| No network | Module docstring + summary flags | **COMPLIANT** — mock listing only |
| No Store writes | `store_writes: False` in summary | **COMPLIANT** — no persist calls |
| No SFTP execution | Upstream mock path only | **COMPLIANT** — `SFTPConnector` not invoked |
| No snapshot mutation | Read-only handoff | **COMPLIANT** — engines receive frozen packages |
| PILOT-001 not authorized | Config fixture shape only | **COMPLIANT** — `dry_run: true`, SAFE_UNKNOWN refs |

### R5 Validate engine boundaries

| Rule | Status |
|------|--------|
| Mock assessors only (empty category findings) | **COMPLIANT** |
| No Publish execution | **COMPLIANT** — emits advisory `PublishEligibilityRecommendation` only |
| No R2/R3 re-validation inside engine | **COMPLIANT** — preconditions consumed as flags |
| No filesystem writes | **COMPLIANT** |
| Boundary declaration on ValidateReport | **COMPLIANT** — `VALIDATE_REPORT_BOUNDARY_DECLARATION` |
| R3 L0 ≠ R5 certified L0 noted | **COMPLIANT** — explicit in possession assessment summary |

### R4 Publish engine boundaries

| Rule | Status |
|------|--------|
| Consumes R5 bundle; never re-Validates | **COMPLIANT** — `_verify_eligibility` read-only |
| Distinct Publish HITL from Validate sign-off | **COMPLIANT** — separate refs in audit |
| Mock snapshot rejected on production path | **COMPLIANT** — `_is_mock_snapshot_id` gate when `in_memory_path=False` |
| Store placement deferred without in-memory bypass | **COMPLIANT** — `store_placement_confirmed=False` + `in_memory_path=False` → DEFERRED |
| SUCCESS clears promotion refs; BLOCKED/DEFERRED null outputs | **COMPLIANT** |

### Validate vs Publish output separation

| Concern | R5 (Validate) | R4 (Publish) | Separation |
|---------|---------------|--------------|------------|
| Authoritative pass/fail for certification | `ValidationResult.summary.status` | — | R5 owns certification status |
| Publish gate recommendation | `PublishEligibilityRecommendation` (advisory) | Consumed, not re-emitted | One-way advisory |
| Publish attempt outcome | — | `PublishResult.publish_result_state` | R4 sole authority for SUCCESS/BLOCKED/DEFERRED |
| Operator HITL | Validate sign-off ref (passed through) | `operator_publish_approval_ref` | Dual HITL preserved |
| Promotion artefact | — | `PublishedSnapshot` + `PublishMetadata` | R4 only on SUCCESS |

---

## Testable now (no live access)

| Test | Command / method | Expected |
|------|------------------|----------|
| Mock E2E happy path | `py -3 engines/ear_mock_e2e_engine.py` | PASS; ids_linked True |
| Validate engine smoke | `py -3 engines/ear_validate_engine.py` | Implicit via E2E (no standalone `__main__`) |
| Publish engine smoke | `py -3 engines/ear_publish_engine.py` | SUCCESS, BLOCKED, DEFERRED paths |
| Config load | `load_config(sample-r1-site-001.json)` | Valid dict; SAFE_UNKNOWN fields accepted |
| R2 contract path | CLI `--contract-evidence` | In-memory EvidencePackage |
| R3 contract path | CLI `--contract-snapshot` | In-memory SnapshotPackage |
| ID linkage audit | `run_mock_e2e_flow(...).summary.id_linkage_notes` | Empty tuple on happy path |
| Negative Validate preconditions | `run_validate(snapshot, r3_assembly_pass=False)` | FAIL status |
| Negative Publish HITL | `run_publish(..., hitl_approved=False)` | DEFERRED |
| Negative Publish eligibility | NOT_ELIGIBLE recommendation | BLOCKED |
| Bundle serialization | `E2EMockBundle.to_dict()` | Redacted-safe config subset |

---

## Missing for SITE-001 dry-run planning

Dry-run **planning** = documenting operator steps, evidence checklist, and gate sequence without live access. The mock E2E runtime supports this; the following artefacts are **not yet present** but are planning deliverables, not runtime blockers:

| Gap | Impact on planning | Classification |
|-----|-------------------|----------------|
| SITE-001 dry-run plan document | Operators lack formal checklist referencing mock bundle fields | **Immediate** (planning artefact) |
| Negative-path E2E fixtures in mock engine verification | Only happy path auto-verified | **Immediate** |
| `--mock-e2e` CLI flag | Manual Python invocation only | **Near-term** |
| Store placement mock adapter in E2E chain | Cannot plan Store gate sequence end-to-end | **Near-term** |
| Real `credential_ref` / `remote_root` in config | Config uses SAFE_UNKNOWN placeholders | **Live-only blocker** for execution planning detail |
| R1 Implementation human decision gate open | Process gate for R1 live connector | **Near-term** (governance) |
| Production snapshot ID algorithm | Documented SAFE_UNKNOWN in handoff_contract | **Live-only blocker** |

**Not blockers for dry-run planning:** real R5 assessors, live SFTP, Store persist, consumer registry — explicitly out of mock E2E scope.

---

## Missing for live SITE-001 execution

| Requirement | Status | Classification |
|-------------|--------|----------------|
| PILOT-001 Execution Authorization | **NO** — architecture gate | **Live-only blocker** |
| Live SFTP connector (network/paramiko) | Skeleton only | **Live-only blocker** |
| Remote listing from SITE-001 | Mock only | **Live-only blocker** |
| Credential resolution (`credential_ref`) | SAFE_UNKNOWN | **Live-only blocker** |
| Production snapshot ID generation | SAFE_UNKNOWN algorithm | **Live-only blocker** |
| Real R5 category assessors (R5-V-* rules) | Not implemented | **Near-term** before meaningful Validate |
| R4 Store adapter + placement confirmation | Not implemented | **Near-term** before production Publish |
| Quarantine persist (R2.5) | Deferred | **Deferred** |
| Consumer registry / OCPilot intake execution | Not implemented | **Deferred** |
| Bulk section expansion (R3 debt) | Not implemented | **Deferred** |
| R1.6 → R2 contract path migration | Documented debt | **Deferred** |

---

## Work classification

### Immediate

- Author SITE-001 dry-run **plan** document (operator checklist, HITL sequence, evidence bar mapped to `E2EMockBundle` fields).
- Add negative-path verification cases to mock E2E (Validate FAIL, Publish BLOCKED/DEFERRED) — documentation/spec only in this review; implementation deferred.
- Reconcile R1 human decision gate before any live connector work.

### Near-term

- Optional `--mock-e2e` CLI surface (human gate required).
- Store placement mock adapter wired into E2E (still no production paths).
- Real R5 assessors (category rules R5-V-*).
- R4 Store adapter for validated snapshot placement.
- Config fixture with resolved non-secret remote scope (when operator provides).

### Live-only blockers

- PILOT-001 Execution Authorization.
- Live SFTP read-only acquisition against SITE-001.
- Credential vault / `credential_ref` resolution.
- Production snapshot ID algorithm implementation.
- Real remote listing and manifest from connected acquisition.

### Deferred

- Quarantine filesystem persist (R2.5).
- Consumer registry execution and OCPilot Run 5 audit.
- R3 bulk expansion and R1.6 legacy migration.
- Level 2/3 publish paths.

---

## Risks

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R-E2E-01 | Stakeholders confuse mock SUCCESS with live readiness | **High** | Decision explicitly scopes planning only; mock prefix on IDs; state file gates |
| R-E2E-02 | Empty assessors always PASS — false confidence in Validate | **Medium** | Document skeleton scope; real assessors required before live Validate trust |
| R-E2E-03 | `sample-r1-site-001.json` treated as execution authorization | **High** | Config is shape fixture; PILOT-001 gate remains NO |
| R-E2E-04 | Store placement bypass via `in_memory_path=True` masks production gate | **Medium** | Publish engine rejects mock IDs when `in_memory_path=False`; plan Store adapter before live |
| R-E2E-05 | 10 safe-unknown entries on mock path normalised as "expected" | **Low** | Document empty-scope mock behaviour; live path will differ |
| R-E2E-06 | R1 human decision gate still OPEN while mock E2E advances | **Medium** | Gate reconciliation tracked; no live connector until closed |

---

## SAFE UNKNOWN

| Topic | Status | Would verify by |
|-------|--------|-----------------|
| Production snapshot ID algorithm | **SAFE UNKNOWN** — `handoff_contract.py` declares not implemented | R3.2 identity implementation on live path |
| Real Store placement confirmation flow | **NOT EXERCISED** — bypassed via `in_memory_path=True` | R4 Store adapter + mock Store integration test |
| SITE-001 `credential_ref` resolution | **SAFE UNKNOWN** — config placeholder | Operator credential vault audit |
| SITE-001 `remote_root` path | **SAFE UNKNOWN** — config placeholder | PILOT preflight against TEST host |
| Consumer visibility execution | **NOT EXERCISED** — logical grant in skeleton only | OCPilot intake integration |
| Live listing scope vs excluded_paths adequacy | **SAFE UNKNOWN** | Connected acquisition dry-run (when authorized) |
| Whether 10 safe-unknown entries represent acceptable Level 1 bar for SITE-001 | **SAFE UNKNOWN** for live — mock path artefact | Real evidence review post-acquisition |

---

## Boundary compliance (review task)

| Rule | Compliance |
|------|------------|
| No architecture contract edits | **YES** |
| No implementation in this review | **YES** |
| No live access enabled | **YES** |
| No SFTP execution | **YES** |
| No Store writes | **YES** |
| No SITE-001 execution authorization | **YES** |

---

## Recommendation

**READY FOR SITE-001 DRY-RUN PLANNING WITH NOTES**

The mock E2E runtime is sufficient to support **planning** of operator dry-run procedures, evidence checklists, and gate sequences using the in-memory bundle shape. It is **not** sufficient for live dry-run execution, connected acquisition, or PILOT-001 authorization.
