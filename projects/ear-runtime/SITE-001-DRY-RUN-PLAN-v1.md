# SITE-001 Dry Run Plan v1

**Type:** Operator procedure plan — **planning artefact only**  
**Site:** `SITE-001` (Автосалон СИБКАР)  
**Pilot:** `PILOT-001` — SFTP Read-Only, Mode 2, TEST, Snapshot Level 1  
**Baseline:** `EAR-STABLE-BASELINE-2026-06` — tag `ear-stable-baseline-2026-06`  
**Date:** 2026-06-07  
**Authority:** [EAR-MOCK-E2E-READINESS-DECISION-v1.md](EAR-MOCK-E2E-READINESS-DECISION-v1.md) — **READY FOR SITE-001 DRY-RUN PLANNING WITH NOTES**  
**State companion:** [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md)

---

## Document boundary (mandatory)

| Rule | Status |
|------|--------|
| This document authorizes dry-run **planning** | **YES** |
| This document authorizes dry-run **execution** | **NO** — separate human gate required |
| This document authorizes live SFTP / connected acquisition | **NO** |
| This document authorizes PILOT-001 execution | **NO** |
| Runtime code changes implied | **NO** |
| Credential usage implied | **NO** |
| Network activity implied | **NO** |

**Truth statement:** This plan defines the **complete operator procedure** for a **future** SITE-001 dry run using the existing EAR architecture on the **mock / in-memory path only**. Authoring this plan does **not** constitute execution.

---

## 1. Purpose

### Why the dry run exists

The SITE-001 dry run is the **first operator-scale rehearsal** of the EAR pipeline for PILOT-001 **without live access**. It exists to:

1. Prove that operators can walk the full **R2 → R3 → R5 → R4** artefact chain with correct **ID continuity**, **stage boundaries**, and **human gates**.
2. Produce a **documented operator record** (checklist completion, HITL sign-offs, artefact inspection) suitable for **Execution Authorization Review**.
3. Expose **procedure gaps**, **negative-path behaviour**, and **SAFE UNKNOWN** items before any connected acquisition is attempted.
4. Validate that the frozen baseline ([EAR-STABLE-BASELINE-2026-06.md](EAR-STABLE-BASELINE-2026-06.md)) supports operator rehearsal without reinterpretation as live readiness.

### Mock E2E vs Dry Run vs Live Pilot

| Dimension | Mock E2E | SITE-001 Dry Run | Live Pilot (PILOT-001) |
|-----------|----------|------------------|------------------------|
| **Primary actor** | Engine / developer verification | **Human operator** | Authorized operator + connected runtime |
| **Data path** | Fixed mock listing; in-memory only | Mock listing **or** pre-staged fixtures; in-memory **or** mock Store | Real SFTP read-only listing from TEST host |
| **Orchestration** | `ear_mock_e2e_engine.py` automated chain | Operator checklist; stage-by-stage review | Connected acquisition + full gate sequence |
| **HITL gates** | Default `hitl_approved=True` in engine kwargs | **Mandatory** Validate sign-off + Publish approval recorded | **Mandatory**; real evidence bar |
| **Credentials** | **None** — fixture placeholders | **None** — `credential_ref` remains unresolved | Vault-resolved `credential_ref` |
| **Network** | **Forbidden** | **Forbidden** | **Authorized** only after Execution Authorization |
| **Store writes** | **None** | Optional mock Store placement drill (no production paths) | R1.8 Store per charter |
| **Validate trust** | Skeleton assessors; happy-path PASS | Operator reviews Validate Report sections; negative paths exercised | Real R5 assessors (R5-V-*) required |
| **Outcome meaning** | Wiring verification | Operator readiness + procedure completeness | Architecture validation on real SITE-001 TEST |
| **Authorizes next phase** | Dry-run **planning** | Execution Authorization **Review input only** | Consumer handoff when Publish succeeds |

**Critical distinction:** Mock E2E **PASS** proves orchestration wiring. Dry Run **success** proves operator procedure and gate discipline. Neither authorizes Live Pilot.

---

## 2. Scope

### Included

| Area | Dry-run scope |
|------|---------------|
| Operator procedure | Full checklist §4 — baseline through completion review |
| Config fixture | [runtime/configs/sample-r1-site-001.json](runtime/configs/sample-r1-site-001.json) — shape only; `dry_run: true` |
| R2 contract evidence path | Mock listing → manifest → `EvidencePackage` via `--contract-evidence` or Mock E2E upstream |
| R3 candidate snapshot | `SnapshotPackage` via `--contract-snapshot` or Mock E2E upstream |
| R5 Validate bundle | `ValidateEngineOutput`: `ValidationResult`, `ValidateReport`, `PublishEligibilityRecommendation` |
| R4 Publish bundle | `PublishEngineOutput`: `PublishResult`, `PublishedSnapshot`, `PublishMetadata`, visibility grant (logical) |
| Human gates | Validate sign-off (pre-Publish); Publish approval (G4); pilot authorization boundary acknowledgment |
| ID linkage verification | `acquisition_id`, `snapshot_id`, R5 refs, R4 refs — per [EAR-MOCK-E2E-FLOW-v1.md](EAR-MOCK-E2E-FLOW-v1.md) |
| Negative-path rehearsal | Documented expected behaviour §6 — operator table-top or manual engine invocation |
| Completion record | Dry Run Completion Review artefact (operator-authored; template §9) |

### Explicitly NOT included

| Exclusion | Rationale |
|-----------|-----------|
| **NO SFTP** | Connector is skeleton only; L-BL-01 |
| **NO credentials** | `credential_ref: SAFE_UNKNOWN_EXTERNAL_REF` — no vault resolution |
| **NO live acquisition** | Connected Mode 2 requires PILOT-001 Execution Authorization |
| **NO production execution** | TEST connected path blocked until separate gate |
| **NO network activity** | Network access **DISABLED** per baseline |
| **NO production snapshot IDs** | Mock prefix `snap-mock-*` / `acq-mock-*` only on dry-run path |
| **NO consumer publication** | OCPilot intake execution out of scope |
| **NO site modification** | Read-only architecture; Mode 3 forbidden |
| **NO reinterpretation of mock SUCCESS** | Forbidden per baseline truth statement |

---

## 3. Preconditions

### Required architecture state

| Precondition | Evidence | Required state |
|--------------|----------|----------------|
| EAR Architecture Program | [shared/external-access-runtime/](../../shared/external-access-runtime/) | **COMPLETE** (frozen 2026-06-01) |
| Runtime Transition Freeze | [freeze/EAR-RUNTIME-TRANSITION-v1/](../../shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/) | **YES** |
| R1–R5 architecture closure | Readiness decisions R2–R5 | **COMPLETE WITH NOTES** |
| Mock E2E | [EAR-MOCK-E2E-FLOW-v1.md](EAR-MOCK-E2E-FLOW-v1.md) | **IMPLEMENTED**; verification **PASS** |
| Mock E2E Readiness | [EAR-MOCK-E2E-READINESS-DECISION-v1.md](EAR-MOCK-E2E-READINESS-DECISION-v1.md) | **READY FOR SITE-001 DRY-RUN PLANNING WITH NOTES** |

### Required baseline

| Item | Requirement |
|------|-------------|
| Baseline tag | `ear-stable-baseline-2026-06` |
| Baseline document | [EAR-STABLE-BASELINE-2026-06.md](EAR-STABLE-BASELINE-2026-06.md) — operator has read limitations § Known limitations |
| Runtime state | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) — R1 **COMPLETE**; R2–R5 **COMPLETE WITH NOTES** |
| This plan | [SITE-001-DRY-RUN-PLAN-v1.md](SITE-001-DRY-RUN-PLAN-v1.md) — **published** |

### Required human approvals (before dry-run **execution**)

| Gate | Status at plan publication | Notes |
|------|---------------------------|-------|
| Dry Run Plan approved | **This document** — planning complete | Does **not** authorize execution |
| Dry Run Execution Authorization | **NOT GRANTED** | Separate gate — not defined in this plan |
| PILOT-001 Execution Authorization | **NO** | Unchanged per baseline |
| R1 live connector authorization | **NO** — [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md) **OPEN** | Mock path only for dry run |

### Required documents (operator reading pack)

| # | Document | Purpose |
|---|----------|---------|
| 1 | [EAR-STABLE-BASELINE-2026-06.md](EAR-STABLE-BASELINE-2026-06.md) | Limitations and blockers |
| 2 | [SITE-001-DRY-RUN-PLAN-v1.md](SITE-001-DRY-RUN-PLAN-v1.md) | This procedure |
| 3 | [EAR-MOCK-E2E-FLOW-v1.md](EAR-MOCK-E2E-FLOW-v1.md) | Expected ID linkage and flow |
| 4 | [shared/.../PILOT-001-SITE-001-SFTP-READONLY/PILOT-CHARTER-v1.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/PILOT-CHARTER-v1.md) | Pilot identity and non-objectives |
| 5 | [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) | R2→R3 identity rules |
| 6 | [R5.5-VALIDATE-REPORT-CONTRACT-v1.md](R5.5-VALIDATE-REPORT-CONTRACT-v1.md) | Eleven-section Validate Report |
| 7 | [R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md](R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md) | Advisory eligibility |
| 8 | [R4.6-PUBLISH-FLOW-CONTRACT-v1.md](R4.6-PUBLISH-FLOW-CONTRACT-v1.md) | G1–G6 Publish Flow gates |
| 9 | [shared/external-access-runtime/PILOT-GOVERNANCE-v1.md](../../shared/external-access-runtime/PILOT-GOVERNANCE-v1.md) | Execution Authorization model |

---

## 4. Operator Checklist

**Execution order:** Config → **R2** → **R3** → **R5** → Validate HITL → **R4** → Publish HITL → Completion Review.

**Environment constraint:** All steps assume **mock / in-memory path**. Operator confirms **no network sockets**, **no credential files opened**, **no SFTPConnector.connect()** invoked.

### Phase 0 — Baseline and boundary review

| Step | Action | Pass criterion |
|------|--------|----------------|
| 0.1 | Confirm baseline tag `ear-stable-baseline-2026-06` and read [EAR-STABLE-BASELINE-2026-06.md](EAR-STABLE-BASELINE-2026-06.md) limitations | Operator acknowledges L-BL-01–L-BL-12 |
| 0.2 | Confirm PILOT-001 Execution Authorization = **NO** | Record gate state in completion review |
| 0.3 | Confirm dry-run execution authorization (if applicable) is **separate** from this plan | No conflation with live pilot |
| 0.4 | Open [runtime/configs/sample-r1-site-001.json](runtime/configs/sample-r1-site-001.json); verify `dry_run: true`, `site_id: SITE-001`, `pilot_id: PILOT-001` | Config shape matches fixture; credentials **not** resolved |
| 0.5 | Record operator identity and dry-run session id (operator-assigned) | Audit trail started |

### Phase 1 — Config and upstream mock inputs

| Step | Action | Pass criterion |
|------|--------|----------------|
| 1.1 | Load config via `load_config()` or accept validated dict | No ConfigValidationError; `dry_run` is `true` |
| 1.2 | Verify `excluded_paths` present; note `allowed_paths` empty on fixture | Scope echo expectations documented |
| 1.3 | Confirm acquisition inputs will use **mock listing only** (`build_mock_listing()`) | **NO** remote listing |
| 1.4 | Run R1 structural pre-checks if using CLI flags: listing → manifest validation | `{valid: true}` on mock path |

### Phase 2 — R2 Evidence Package (expected artefacts)

| Step | Action | Pass criterion |
|------|--------|----------------|
| 2.1 | Produce R2 `EvidencePackage` via contract generator (`build_contract_evidence_package`) | Package present in memory |
| 2.2 | Run R2 structural validation (`validate_contract_evidence_package`) | `valid: true`; errors empty |
| 2.3 | Inspect **Evidence Package** identity | See §5.1 — `acquisition_id`, `site_ref`, `connector_class` |
| 2.4 | Inspect **Artifact Index** | Mock artefacts indexed; quarantine layout **not** persisted (debt noted) |
| 2.5 | Record expected mock id pattern | e.g. `acq-mock-SITE-001-mock` per Mock E2E verification |
| 2.6 | **Stop condition:** R2 missing or structural fail | Proceed to §6 NP-R2; do **not** enter R3 |

### Phase 3 — R3 Candidate Snapshot (expected artefacts)

| Step | Action | Pass criterion |
|------|--------|----------------|
| 3.1 | Hand off R2 package via `handoff_contract` rules | `acquisition_id` continuity preserved |
| 3.2 | Produce R3 `SnapshotPackage` (`build_candidate_snapshot_package`) | Candidate snapshot present |
| 3.3 | Run R3 assembly validation (`validate_candidate_snapshot_package`) | `valid: true` |
| 3.4 | Inspect **Candidate Snapshot** identity | See §5.2 — `snapshot_id` mock prefix `snap-mock-*` |
| 3.5 | Review **Safe Unknown** entries | Count recorded (fixture expects ~10 on empty-scope mock); not treated as live evidence bar |
| 3.6 | Confirm `publish_state` concept = candidate / pre-Validate | No published state yet |
| 3.7 | **Stop condition:** R3 fail or id break | Proceed to §6 NP-R3; do **not** enter R5 |

### Phase 4 — R5 Validate (expected artefacts)

| Step | Action | Pass criterion |
|------|--------|----------------|
| 4.1 | Invoke Validate Engine (`run_validate`) with R2/R3 preconditions | `ValidateEngineOutput` returned |
| 4.2 | Inspect **ValidationResult** | See §5.3 — status PASS / PASS_WITH_NOTES / FAIL |
| 4.3 | Inspect **ValidateReport** — all **eleven sections** present | Per [R5.5-VALIDATE-REPORT-CONTRACT-v1.md](R5.5-VALIDATE-REPORT-CONTRACT-v1.md) |
| 4.4 | Inspect **PublishEligibilityRecommendation** | ELIGIBLE / ELIGIBLE_WITH_NOTES / NOT_ELIGIBLE — **advisory only** |
| 4.5 | Verify R5 refs link to same `snapshot_id` | `validated_snapshot_id` matches R3 |
| 4.6 | Operator acknowledges skeleton assessor limitation | Real R5-V-* rules **NOT IMPLEMENTED** |
| 4.7 | **Stop condition:** validation_status FAIL | Proceed to §6 NP-R3-FAIL; **no Publish entry** |

### Phase 5 — Validate HITL sign-off (human gate)

| Step | Action | Pass criterion |
|------|--------|----------------|
| 5.1 | Operator reads Validate Report Summary, Blockers, Warnings | Written acknowledgment |
| 5.2 | Operator records **Validate sign-off** ref (e.g. `hitl:validate:{session}:{operator}`) | Distinct from Publish approval |
| 5.3 | If FAIL or NOT_ELIGIBLE: **STOP** — no R4 | Fail-closed per R4.6 precondition |
| 5.4 | Optional: mock Store placement drill (R1.8 layout under `output_root`) | **Mock Store only**; not required for in-memory dry run |

### Phase 6 — R4 Publish (expected artefacts)

| Step | Action | Pass criterion |
|------|--------|----------------|
| 6.1 | Confirm Validate sign-off on record | Precondition before G1 |
| 6.2 | Invoke Publish Engine with `in_memory_path=True` | Store placement gate bypass **documented** — not production behaviour |
| 6.3 | Walk Publish Flow gates G1–G6 conceptually | See §7 Human Gates |
| 6.4 | Inspect **PublishResult** | See §5.4 — SUCCESS / BLOCKED / DEFERRED |
| 6.5 | On SUCCESS: inspect **PublishedSnapshot**, **PublishMetadata**, visibility grant (logical) | ID refs cite R5 bundle |
| 6.6 | Verify R4 did **not** re-run Validate | Boundary VB-R4 / VB-R5 preserved |
| 6.7 | **Stop condition:** Publish BLOCKED or missing HITL | Proceed to §6 NP-R4 / NP-HITL |

### Phase 7 — Publish HITL approval (human gate G4)

| Step | Action | Pass criterion |
|------|--------|----------------|
| 7.1 | Operator records **Publish approval** ref — distinct from Validate sign-off | e.g. `hitl:publish:{session}:{operator}` |
| 7.2 | Confirm Publish attempted only after G4 on default path | PF-INV-R4-03 satisfied |
| 7.3 | Acknowledge consumer visibility is **logical only** — no OCPilot execution | Baseline L-BL scope |

### Phase 8 — Dry Run completion review

| Step | Action | Pass criterion |
|------|--------|----------------|
| 8.1 | Verify full artefact chain complete per §8 Success Criteria | All mandatory checks PASS |
| 8.2 | Verify ID continuity preserved | `ids_linked` equivalent true |
| 8.3 | Verify **no forbidden live activity** occurred | Network/credentials/SFTP absent |
| 8.4 | Record SAFE UNKNOWN items encountered | §11 |
| 8.5 | Record negative paths exercised (if any) | §6 |
| 8.6 | Author **Dry Run Completion Review** record | §9 Exit Criteria |
| 8.7 | Explicit statement: **Dry Run does NOT authorize Live Pilot** | Mandatory closure text |

---

## 5. Expected Artefacts

### 5.1 R2 — Evidence Package

| Artefact | Producer | Consumer | Expected state (dry run) |
|----------|----------|----------|--------------------------|
| **EvidencePackage** | R2.7 `evidence_package_builder` | R3 handoff; R5 audit context | Present; structurally valid |
| **EvidenceIdentity** | R2 generator | R3 `acquisition_id` continuity | `site_ref` = SITE-001; mock `acquisition_id` |
| **EvidenceArtifactIndex** | R2 generator | R5 possession review (future) | Mock entries; no live file hashes |
| **R2 structural validation result** | `evidence_package_validator` | R5 precondition | `{valid: true}` on happy path |

### 5.2 R3 — Candidate Snapshot

| Artefact | Producer | Consumer | Expected state (dry run) |
|----------|----------|----------|--------------------------|
| **SnapshotPackage** (candidate) | R3.5 `snapshot_package_builder` | R5 Validate input | OpenCart section tree assembled |
| **SnapshotIdentity** | R3 generator | R4 G1; R5 audit | `snapshot_id` = `snap-mock-SITE-001-{connector}` |
| **SnapshotSafeUnknown** | R3 propagation | R5 Quality / Readiness sections | Entries present on mock path (~10 expected) |
| **R3 assembly validation result** | `snapshot_package_validator` | R5 precondition | `{valid: true}` on happy path |

### 5.3 R5 — Validation Bundle

| Artefact | Producer | Consumer | Expected state (dry run) |
|----------|----------|----------|--------------------------|
| **ValidationResult** | R5 Validate Engine | R4 G2; operator | PASS on happy path (skeleton) |
| **ValidateReport** | R5 Validate Engine | Validate HITL; R4 context | Eleven sections populated |
| **PublishEligibilityRecommendation** | R5 Validate Engine | R4 G3; operator | ELIGIBLE on happy path — **advisory** |
| **ValidateEngineOutput** | `ear_validate_engine` | R4 Publish Engine | Bundle with linked refs |

### 5.4 R4 — Publish Bundle

| Artefact | Producer | Consumer | Expected state (dry run) |
|----------|----------|----------|--------------------------|
| **PublishResult** | R4 Publish Engine | Operator; audit | SUCCESS on happy path with HITL |
| **PublishedSnapshot** | R4 Publish Engine | Consumer registry (logical) | Cites `validation_result_ref` |
| **PublishMetadata** | R4 Publish Engine | Store (future adapter) | Present in bundle; **not** written to production Store |
| **PublishState transition** | R4 engine (logical) | R4.2 model | stored_unpublished → published (in-memory) |
| **Consumer visibility grant** | R4 engine (logical) | OCPilot (future) | Logical grant only — **not executed** |
| **PublishEngineOutput** | `ear_publish_engine` | Completion review | Full bundle when SUCCESS |

### 5.5 Orchestration summary (optional cross-check)

| Artefact | Producer | Consumer | Expected state (dry run) |
|----------|----------|----------|--------------------------|
| **E2EMockBundle** | `ear_mock_e2e_engine` | Operator verification | All nested artefacts + `E2EFlowSummary` |
| **E2EFlowSummary** | Mock E2E engine | Completion review | `ids_linked: true`; `network_access: false`; `store_writes: false` |

---

## 6. Negative Paths

Expected **operator behaviour only** — no code changes in this plan.

| ID | Scenario | Trigger | Expected behaviour | Operator action |
|----|----------|---------|-------------------|-----------------|
| **NP-R2** | R2 missing | Generator error or empty package | **STOP** before R3; no snapshot | Log error; mark dry run **INCOMPLETE** |
| **NP-R2-FAIL** | R2 structural fail | Validator `{valid: false}` | **STOP**; quarantine path **not** auto-persisted (debt) | Document errors; do not hand off to R3 |
| **NP-R3** | R3 missing | Handoff rejected | **STOP** before R5 | Verify `acquisition_id` linkage |
| **NP-R3-FAIL** | R3 assembly fail | Validator `{valid: false}` | **STOP**; no Validate certification | Document assembly errors |
| **NP-R5-FAIL** | R3 fail → R5 | Enter Validate with failed R3 precondition | Validate **FAIL**; Publish **blocked** | No Validate sign-off; no R4 |
| **NP-R5-FAIL** | Validate FAIL | `validation_status: FAIL` | R4 G2 fail-closed; **PublishResult BLOCKED** if attempted | Operator rejects Publish; record blockers |
| **NP-R5-NE** | NOT_ELIGIBLE | `PublishEligibilityRecommendation` = NOT_ELIGIBLE | R4 G3 fail-closed | Advisory respected; no Publish on default path |
| **NP-R5-PWN** | PASS_WITH_NOTES | Validation with notes | Publish **may** proceed with documented notes | Validate sign-off includes note acknowledgment |
| **NP-R4-BLOCK** | Publish blocked | Missing G1 snapshot; mock id on production path flag | **PublishResult: BLOCKED** | Do not treat as SUCCESS |
| **NP-R4-DEF** | Publish deferred | Store placement pending (when mock adapter added) | **PublishResult: DEFERRED** | Retry after placement drill — still mock |
| **NP-HITL** | Missing HITL | Publish invoked without Validate sign-off or G4 approval | Engine / contract fail-closed | Record gate violation; dry run **FAIL** boundary check |
| **NP-LIVE** | Forbidden live activity | Credential load; SFTP connect; network | **ABORT** dry run | Incident record; baseline breach |

---

## 7. Human Gates

| Gate | Name | Owner | When | Dry-run requirement |
|------|------|-------|------|---------------------|
| **HG-0** | Dry Run Execution Authorization | Program owner | Before Phase 1 execution | **NOT GRANTED** by this plan |
| **HG-1** | Validate sign-off | Operator | After R5 bundle review; **before** R4 | Mandatory; recorded ref; distinct from Publish |
| **HG-2** | Publish approval (R4 G4) | Operator | Before Publish execution on default path | Mandatory; recorded ref |
| **HG-3** | Pilot authorization boundary | Operator | Completion review closure | Acknowledge PILOT-001 **NOT AUTHORIZED** |
| **HG-4** | Execution Authorization Review | Program owner | After successful dry run | Input to live pilot gate — **not automatic approval** |

### Validate sign-off checklist (HG-1)

Operator confirms review of:

1. ValidationResult status and summary  
2. ValidateReport § Blockers — empty or acknowledged  
3. ValidateReport § Warnings — reviewed  
4. PublishEligibilityRecommendation — advisory noted  
5. Skeleton assessor limitation acknowledged  

### Publish approval checklist (HG-2)

Operator confirms:

1. Validate sign-off on record (HG-1)  
2. G1–G3 conceptually satisfied  
3. Publish is **in-memory / mock** — not production Store  
4. Consumer handoff **not** executed  

---

## 8. Dry Run Success Criteria

Dry run is **successful** when **all** of the following are true:

| ID | Criterion |
|----|-----------|
| **SC-DR-01** | **Artifact chain complete** — EvidencePackage → SnapshotPackage → ValidateEngineOutput → PublishEngineOutput (or documented intentional stop at negative path) |
| **SC-DR-02** | **ID continuity preserved** — `acquisition_id` R2→R3; R5 `validated_snapshot_id` = R3 `snapshot_id`; R4 refs align |
| **SC-DR-03** | **Boundaries respected** — R4 did not re-Validate; R5 did not Publish; R2/R3 did not certify quality |
| **SC-DR-04** | **No forbidden live activity** — no network, no credentials, no SFTP, no production snapshot IDs |
| **SC-DR-05** | **Human gates recorded** — Validate sign-off and Publish approval refs captured (happy path) |
| **SC-DR-06** | **Mock path explicit** — operator record states mock listing + in-memory Publish |
| **SC-DR-07** | **Completion review authored** — §9 exit artefact exists |
| **SC-DR-08** | **Pilot boundary stated** — closure text: dry run ≠ live authorization |

**Not required for dry-run success:** Real acquisition quality; real R5 assessors; Store adapter; consumer execution; credential resolution.

---

## 9. Dry Run Exit Criteria

The dry run is **complete** when:

1. Operator checklist §4 Phases 0–8 finished or **stopped with documented negative path**.  
2. **Dry Run Completion Review** record exists containing:

| Field | Content |
|-------|---------|
| `dry_run_session_id` | Operator-assigned |
| `baseline_tag` | `ear-stable-baseline-2026-06` |
| `plan_version` | `SITE-001-DRY-RUN-PLAN-v1` |
| `config_fixture` | `sample-r1-site-001.json` |
| `path_mode` | `mock_in_memory` |
| `artefact_ids` | `acquisition_id`, `snapshot_id`, validation refs, publish refs |
| `success_criteria` | SC-DR-01–08 pass/fail matrix |
| `hitl_refs` | Validate sign-off + Publish approval refs |
| `negative_paths_exercised` | NP-* ids or `none` |
| `safe_unknown_encountered` | List from §11 |
| `operator_sign_off` | Identity + timestamp |
| `pilot_authorization` | **NO** — explicit |

3. [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) updated by program owner when execution occurs (not by this planning task).

**Exit does not grant:** PILOT-001 Execution Authorization, live SFTP, connected acquisition, or consumer publication.

---

## 10. Transition Matrix

```text
Mock E2E (engine verification)
        │
        │  PASS ≠ operator procedure proven
        ▼
SITE-001 Dry Run Plan (this document)          ← PLANNING AUTHORIZED
        │
        │  Plan alone ≠ execution
        ▼
Dry Run Execution Authorization (separate gate)  ← NOT GRANTED by this plan
        │
        ▼
SITE-001 Dry Run (operator rehearsal)          ← mock/in-memory only
        │
        │  Success = procedure + gates documented
        │  Dry Run ≠ Live Pilot authorization
        ▼
Execution Authorization Review                 ← human program gate
        │
        │  Reviews dry-run record + blockers + debt
        ▼
PILOT-001 Execution Authorization              ← NOT GRANTED until explicit YES
        │
        ▼
Connected Acquisition (TEST, SFTP read-only)   ← live path; credentials; network
```

| Transition | Authorizes live access? |
|------------|-------------------------|
| Mock E2E → Dry Run Plan | **NO** |
| Dry Run Plan → Dry Run Execution | **NO** (mock path only when authorized) |
| Dry Run Success → Execution Authorization Review | **NO** — review input only |
| Execution Authorization Review → PILOT-001 | **Only if explicit human YES** |
| PILOT-001 → Connected Acquisition | **YES** (within pilot charter scope) |

---

## 11. Required Reviews (planning gate)

### Architecture review

| Question | Finding |
|----------|---------|
| Does EAR architecture support SITE-001 dry run without live access? | **YES** — mock listing path, contract R2/R3, skeleton R5/R4, Mock E2E verified |
| Are R2/R3/R4/R5 boundaries preserved in procedure? | **YES** — checklist enforces stage order and fail-closed gates |
| Does procedure contradict frozen baseline? | **NO** — aligns with [EAR-STABLE-BASELINE-2026-06.md](EAR-STABLE-BASELINE-2026-06.md) |

### Ownership review

| Layer | Owner | Dry-run role |
|-------|-------|--------------|
| R1 config / mock inputs | R1 | Fixture + mock listing only |
| R2 evidence | R2.7 generator | Produces EvidencePackage |
| R3 snapshot | R3.5 generator | Produces candidate SnapshotPackage |
| R5 validate | R5.7 engine | Certification + advisory eligibility |
| R4 publish | R4.7 engine | PublishResult + promotion artefacts |
| Operator HITL | Human operator | Validate sign-off + Publish approval |
| Store | R1.8 (mock) | Optional drill; not required in-memory |

### R2 / R3 / R4 / R5 boundary review

| Boundary | Dry-run enforcement |
|----------|---------------------|
| R2 structural only | R5 owns quality certification |
| R3 assembly only | R5 owns Validate; R3 validator ≠ certification |
| R5 advisory eligibility | R4 G3 consumes; operator decides |
| R4 no re-Validation | Checklist step 6.6 |
| Dual HITL | HG-1 ≠ HG-2 per R4.6 |

### Pilot-readiness review

| Question | Answer |
|----------|--------|
| Can SITE-001 Dry Run be executed safely without live access? | **YES** — when Dry Run Execution Authorization granted; mock/in-memory path only; no credentials/network |
| What remains blocked? | Live SFTP; credential resolution; production IDs; real assessors; Store adapter; PILOT-001; OCPilot execution |
| What becomes available after Dry Run? | Documented operator record for **Execution Authorization Review**; optional negative-path fixture priorities; **not** live pilot |

---

## 12. SAFE UNKNOWN

| Topic | Status at plan time | Would verify by |
|-------|---------------------|-----------------|
| Dry Run Execution Authorization process | **SAFE UNKNOWN** — separate gate not yet chartered | Program owner charter |
| Production snapshot ID on live path | **SAFE UNKNOWN** | R3.2 live identity implementation |
| SITE-001 `credential_ref` / `remote_root` | **SAFE UNKNOWN** in fixture | Vault audit + TEST preflight |
| Real evidence bar for Level 1 | **SAFE UNKNOWN** for live | Post-acquisition Validate with real assessors |
| Store placement confirmation flow | **NOT EXERCISED** in in-memory dry run | R4 Store mock adapter drill |
| Dry Run Completion Review storage location | **SAFE UNKNOWN** | Operator runbook / `pilots/` folder policy |
| Whether table-top negative paths satisfy program | **SAFE UNKNOWN** | Execution Authorization Review criteria |

---

## 13. Related documents

| Document | Relationship |
|----------|--------------|
| [EAR-STABLE-BASELINE-2026-06.md](EAR-STABLE-BASELINE-2026-06.md) | Upstream baseline freeze |
| [EAR-MOCK-E2E-FLOW-v1.md](EAR-MOCK-E2E-FLOW-v1.md) | Reference orchestration |
| [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) | Runtime program mission |
| [PILOT-001 PILOT-CHARTER-v1.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/PILOT-CHARTER-v1.md) | Live pilot scope (future) |
| [PILOT-GOVERNANCE-v1.md](../../shared/external-access-runtime/PILOT-GOVERNANCE-v1.md) | Execution Authorization |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-07 | **CREATED** — SITE-001 Dry Run Plan v1; planning artefact only; execution **NOT AUTHORIZED** |
