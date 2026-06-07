# R4 — Readiness Review v1

**Type:** Program gate review — **no** Publish Engine implementation, **no** CLI, **no** Store adapter, **no** live pilot  
**Date:** 2026-06-07  
**Phase:** R4.9 — R4 Readiness Review  
**Charter:** [R4-IMPLEMENTATION-CHARTER-v1.md](R4-IMPLEMENTATION-CHARTER-v1.md) § R4.9  
**Prior gate:** [R4.8-PUBLISH-BOUNDARY-DECISION-v1.md](R4.8-PUBLISH-BOUNDARY-DECISION-v1.md) — **PASS WITH NOTES**; Human Gate **PASSED**  
**Decision companion:** [R4-READINESS-DECISION-v1.md](R4-READINESS-DECISION-v1.md)

**Explicit exclusions:** Publish Engine code, `ear_publish_engine.py`, `--publish-snapshot` CLI, Store publish-metadata persist adapter, R5 Validate execution, live SFTP, SITE-001 execution, OCPilot integration.

---

## Executive summary

R4 — EAR Publish Layer **architecture and contract engineering** is **complete with notes**. All required milestones R4.1–R4.8 have gate artefacts; R4 Charter and R4 Implementation Charter are closed; R4.1–R4.4 model modules exist in `runtime/shared/`; R4.5–R4.6 contracts are documented without dataclass modules; R4.7 Publish Engine architecture is defined without orchestrator code; R4.8 confirms clean R2/R3/R5/Consumer boundaries (VB-R4-01–18). No critical ownership violations were found.

**Upstream dependencies:** R2 **COMPLETE WITH NOTES** ([R2-READINESS-DECISION-v1.md](R2-READINESS-DECISION-v1.md)); R3 **COMPLETE WITH NOTES** ([R3-READINESS-DECISION-v1.md](R3-READINESS-DECISION-v1.md)); R5 **COMPLETE WITH NOTES** ([R5-READINESS-DECISION-v1.md](R5-READINESS-DECISION-v1.md)). Mock-path R3 candidate verified on `--contract-snapshot`; R5 bundle consumable via contract semantics (Validate Engine not implemented — mock bundle acceptable per A-R4-10).

**Recommendation:** **READY FOR R4 IMPLEMENTATION WITH NOTES** — R4 code work may be authorized after human gate; first slice: `publish_result_models.py` + `ear_publish_engine.py` skeleton per R4.7.

---

## Sources reviewed

| ID | Document | Role |
|----|----------|------|
| S-R4R-01 | [R4-CHARTER-v1.md](R4-CHARTER-v1.md) | Program mission, scope, R5→R4 boundary, quality freeze, consumer boundary |
| S-R4R-02 | [R4-IMPLEMENTATION-CHARTER-v1.md](R4-IMPLEMENTATION-CHARTER-v1.md) | Work packages R4.1–R4.9; implementation sequence |
| S-R4R-03 | [R4-DECISION-v1.md](R4-DECISION-v1.md) | Charter gate — APPROVED WITH NOTES |
| S-R4R-04 | [R4-IMPLEMENTATION-DECISION-v1.md](R4-IMPLEMENTATION-DECISION-v1.md) | Implementation charter gate — APPROVED WITH NOTES |
| S-R4R-05 | R4.1–R4.8 milestone models, contracts, decisions | Contract chain evidence |
| S-R4R-06 | [R4.8-PUBLISH-BOUNDARY-REVIEW-v1.md](R4.8-PUBLISH-BOUNDARY-REVIEW-v1.md) | VB-R4-01–18; ownership audit |
| S-R4R-07 | [R5-READINESS-REVIEW-v1.md](R5-READINESS-REVIEW-v1.md) | R5 dependency; R5.6 advisory input |
| S-R4R-08 | [R3-READINESS-REVIEW-v1.md](R3-READINESS-REVIEW-v1.md) | R3 validated snapshot input path |
| S-R4R-09 | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Program status |
| S-R4R-10 | `runtime/` modules (read-only inspection) | Implementation evidence |

**Runtime modules inspected (read-only):**

| Module | Evidence for |
|--------|--------------|
| `runtime/shared/published_snapshot_models.py` | R4.1 Published Snapshot contract |
| `runtime/shared/publish_state_models.py` | R4.2 publish lifecycle states |
| `runtime/shared/consumer_visibility_models.py` | R4.3 visibility grant semantics |
| `runtime/shared/publish_metadata_models.py` | R4.4 publish metadata fields |
| `runtime/shared/validation_result_models.py` | R5 input — unchanged by R4 |
| `runtime/validators/snapshot_package_validator.py` | No R4 Publish logic in R3 |
| `runtime/builders/snapshot_package_builder.py` | R3 candidate only — no Publish |
| `runtime/connectors/sftp_connector.py` | `--contract-snapshot` chain |

**Absent by design (not gaps for this review):**

| Expected future module | Status |
|------------------------|--------|
| `publish_result_models.py` | **NOT CREATED** — R4.5 contract only |
| `ear_publish_engine.py` | **NOT CREATED** — R4.7 architecture only |
| CLI `--publish-snapshot` | **NOT CREATED** — R4.7 future |
| Store publish metadata adapter | **NOT CREATED** — R4.7+ side effect |

---

## Milestone Matrix

| Milestone | Status | Notes |
|-----------|--------|-------|
| **R4.1** Published Snapshot Model | **COMPLETE** | [R4.1-PUBLISHED-SNAPSHOT-MODEL-v1.md](R4.1-PUBLISHED-SNAPSHOT-MODEL-v1.md); **PASS WITH NOTES**; `published_snapshot_models.py` — promotion not assembly; PS-INV-R4-01–05 |
| **R4.2** Publish State Model | **COMPLETE** | [R4.2-PUBLISH-STATE-MODEL-v1.md](R4.2-PUBLISH-STATE-MODEL-v1.md); **PASS WITH NOTES**; `publish_state_models.py` — stored_unpublished → published → superseded/archived |
| **R4.3** Consumer Visibility Model | **COMPLETE** | [R4.3-CONSUMER-VISIBILITY-MODEL-v1.md](R4.3-CONSUMER-VISIBILITY-MODEL-v1.md); **PASS WITH NOTES**; `consumer_visibility_models.py` — CB-R4-01–05 |
| **R4.4** Publish Metadata Model | **COMPLETE** | [R4.4-PUBLISH-METADATA-MODEL-v1.md](R4.4-PUBLISH-METADATA-MODEL-v1.md); **PASS WITH NOTES**; `publish_metadata_models.py` — `published_at`, `published_by`, `consumer_target` |
| **R4.5** Publish Result Contract | **COMPLETE** | [R4.5-PUBLISH-RESULT-CONTRACT-v1.md](R4.5-PUBLISH-RESULT-CONTRACT-v1.md); **PASS WITH NOTES**; SUCCESS / BLOCKED / DEFERRED; **no** `publish_result_models.py` |
| **R4.6** Publish Flow Contract | **COMPLETE** | [R4.6-PUBLISH-FLOW-CONTRACT-v1.md](R4.6-PUBLISH-FLOW-CONTRACT-v1.md); **PASS WITH NOTES**; G1–G6 gate sequence; dual HITL; PF-INV-R4-* |
| **R4.7** Publish Engine Architecture | **COMPLETE** | [R4.7-PUBLISH-ENGINE-ARCHITECTURE-v1.md](R4.7-PUBLISH-ENGINE-ARCHITECTURE-v1.md); **PASS WITH NOTES**; seven stages; **no** `ear_publish_engine.py` |
| **R4.8** Publish Boundary Review | **COMPLETE** | [R4.8-PUBLISH-BOUNDARY-REVIEW-v1.md](R4.8-PUBLISH-BOUNDARY-REVIEW-v1.md); **PASS WITH NOTES**; VB-R4-01–18; no critical R2/R3/R5 absorption |

**Program charters (prerequisites):**

| Artefact | Status |
|----------|--------|
| R4 Charter | **COMPLETE** — APPROVED WITH NOTES |
| R4 Implementation Charter | **COMPLETE** — APPROVED WITH NOTES |

---

## Dependency Review

### R5 Readiness (COMPLETE WITH NOTES)

| Check | Verdict | Evidence |
|-------|---------|----------|
| R5.1 `ValidationResult` available as R4 precondition input | **PASS** | `validation_result_models.py`; R4.6 Stage 2 |
| R5.6 `PublishEligibilityRecommendation` advisory contract defined | **PASS** | R5.6; R4 consumes — never emits |
| R5.8 boundary — R4 does not replace R5 Validate | **PASS** | VB-R5-10; R4.8 VB-R4-12 |
| R5 Validate Engine not implemented blocks R4 **architecture**? | **No** | A-R4-10 — mock R5 bundle acceptable for engineering |
| R5 debt (engine, report/eligibility dataclass modules) blocks R4 **architecture**? | **No** | R4 may mock R5 bundle for first engine slice |

### R3 Readiness (COMPLETE WITH NOTES)

| Check | Verdict | Evidence |
|-------|---------|----------|
| R3.1 `SnapshotPackage` is R4 primary publish target (read-only) | **PASS** | R4.1 `PublishedSnapshot.snapshot` citation |
| R3.5 candidate generator operational | **PASS** | `--contract-snapshot` CLI verification |
| R3.6 boundary — R3 assembly ≠ R4 Publish | **PASS** | VB-R3-01 → VB-R4-04; PE-INV-R4-09 |
| R3 debt (Store persist, bulk expansion) blocks R4 **architecture**? | **No** | Blocks live publish paths only; in-memory path chartered |

### R2 Readiness (COMPLETE WITH NOTES)

| Check | Verdict | Evidence |
|-------|---------|----------|
| R4 never reads quarantine as publish target | **PASS** | R4-CHARTER non-inputs; VB-R4-08 |
| R2 debt (quarantine persist) blocks R4 **architecture**? | **No** | R4 promotes validated snapshot only |

---

## Runtime State Review

### Mock-path verification (2026-06-07)

```text
py cli.py --config configs/sample-r1-site-001.json --contract-snapshot
  snapshot_id: snap-mock-SITE-001-sftp_readonly
  acquisition_id: acq-mock-SITE-001-mock
  site_id: SITE-001
  package_quality_level: 0
  validation: PASS
```

| Criterion | Assessment |
|-----------|------------|
| R4 Publish implemented | **No** — no engine, no `--publish-snapshot` |
| R3 candidate available as future R4 input (post-R5 Validate) | **Yes** — in-memory on contract path |
| R4 model modules exist without engine | **Yes** — R4.1–R4.4 dataclasses only |
| R5 bundle available for mock Publish engineering | **Yes** — contract semantics; engine may assemble mock bundle |
| R2/R3 validators unchanged | **Yes** — no Publish logic in R2/R3 code |
| R5 Validate implemented | **No** — prerequisite for real Publish; not architecture blocker |
| Network / live acquisition | **Disabled** — per program state |

---

## Mandatory answers

| # | Question | Answer |
|---|----------|--------|
| 1 | **Is R4 architecturally complete?** | **Yes, with notes** — all R4.1–R4.8 contracts and charters exist; Publish Engine, result dataclass module, CLI, and Store metadata adapter intentionally deferred |
| 2 | **Is R4 internally coherent?** | **Yes** — Charter → Implementation Charter → R4.1–R4.7 chain consistent; R4.7 seven stages map to R4.1–R4.6 contracts; Store ≠ Publish; recommendation ≠ execution |
| 3 | **Can implementation begin later?** | **Yes** — after R4.9 decision + human implementation gate; first slice: engine skeleton + `publish_result_models.py` per R4.7 |
| 4 | **Can R4 publish validated snapshots?** | **Yes, architecturally** — promotion model, flow gates, and engine scope support validated snapshot → published reference; **runtime execution not yet implemented** |
| 5 | **Can R4 support future SITE-001 publish flow?** | **Yes, architecturally** — consumes R5-validated snapshot + R5 bundle + operator HITL; **live** SITE-001 requires Execution Authorization + R2/R3/R5 debt resolution |
| 6 | **Can R4 support future OCPilot consumers?** | **Yes** — `consumer_target` (e.g. `ocpilot`); visibility grant + published `snapshot_id` citation; OCPilot owns intake execution post-Publish |
| 7 | **What remains outside R4?** | R5 Validate execution; R3 assembly; R2 evidence; consumer program execution; Store layout redesign; live SFTP/SITE-001; normative JSON Schema |
| 8 | **What debt remains?** | See § Outstanding Debt — engine code, result models, CLI, Store metadata adapter, consumer registry pointer encoding, supersession automation, inherited R2/R3/R5 debt for live paths |

---

## Readiness Criteria (IAC-R4-01–10)

Architecture-readiness criteria for R4.9 (distinct from post-implementation engineering acceptance in R4 Charter § Engineering acceptance).

| ID | Criterion | Assessment | Evidence / gap |
|----|-----------|------------|----------------|
| **IAC-R4-01** | Published Snapshot model complete | **SATISFIED** | R4.1; `published_snapshot_models.py`; PS-INV-R4-01–05; promotion not assembly |
| **IAC-R4-02** | Publish State lifecycle complete | **SATISFIED** | R4.2; `publish_state_models.py`; forbidden bypass transitions; consumer access column |
| **IAC-R4-03** | Consumer Visibility model complete | **SATISFIED** | R4.3; CB-R4-01–05; visibility grant ≠ credential handoff |
| **IAC-R4-04** | Publish Metadata model complete | **SATISFIED** | R4.4; three mandatory R4-owned fields; quality freeze only |
| **IAC-R4-05** | Publish Result contract complete | **SATISFIED** | R4.5; PR-INV-R4-01–08; SUCCESS / BLOCKED / DEFERRED |
| **IAC-R4-06** | Publish Flow contract complete | **SATISFIED** | R4.6; dual HITL; G1–G6; NOT_ELIGIBLE fail closed |
| **IAC-R4-07** | Publish Engine architecture complete | **SATISFIED** | R4.7; seven stages; prohibitions; no code required at R4.9 |
| **IAC-R4-08** | Boundary Review passed | **SATISFIED** | R4.8 **PASS WITH NOTES**; VB-R4-01–18 |
| **IAC-R4-09** | No critical ownership conflicts | **SATISFIED** | R4.8: no critical violation; DRIFT-R4-01–08 tracked as notes |
| **IAC-R4-10** | Ready for implementation phase | **SATISFIED WITH NOTES** | Architecture complete; code **not** started by design; human gate required before first engine PR |

**Summary:** 9/10 **SATISFIED**; 1/10 **SATISFIED WITH NOTES** (IAC-R4-10 — implementation phase authorized at architecture layer only).

### Post-implementation engineering acceptance (not evaluated at R4.9)

Per R4 Charter, these apply **after** code exists — correctly **NOT SATISFIED** today:

| ID | Criterion (Charter § Engineering acceptance) | Status |
|----|---------------------------------------------|--------|
| Charter IAC-R4-01 | Operator can execute Publish on validated snapshot with R5 bundle | **NOT SATISFIED** — no engine/CLI |
| Charter IAC-R4-02 | Published reference immutable; publish log records gate satisfaction | **NOT SATISFIED** — no engine |
| Charter IAC-R4-03 | Published quality matches R5 certified level — no inflation | **NOT SATISFIED** — no engine |
| Charter IAC-R4-04 | NOT_ELIGIBLE blocks default Publish — fail closed | **NOT SATISFIED** — contract only |
| Charter IAC-R4-05 | R4 does not re-validate or modify sections | **SATISFIED** — architecture; no Publish code |
| Charter IAC-R4-06 | Consumer intake possible only after Publish completes | **SATISFIED** — architecture; CB-R4-01–02 |

---

## Ownership Review

| Concern | Expected owner | Observed in R4 artefacts | Leak? |
|---------|----------------|--------------------------|-------|
| Evidence Package / quarantine | **R2** | Explicit non-input | **No** |
| Candidate snapshot assembly | **R3** | Read-only citation; forbidden mutation | **No** |
| EAR Validate / certification | **R5** | Precondition consume only | **No** |
| Quality certification L0–L3 | **R5** | R4 freeze only — no upgrade | **No** |
| Publish Eligibility Recommendation | **R5** emit | R4 consume — never emit | **No** |
| Publish execution | **R4** | R4.7 stages 4–7 | **No overlap** |
| Publish metadata | **R4** | R4.4 exclusive assignment | **No** |
| Consumer visibility grant | **R4** | R4.3 logical permission | **No** |
| Consumer intake / OCPilot Run 5 | **Consumer** | Forbidden in R4 scope | **No** |
| Store layout / stored-unpublished | **R1.8** | Precondition — no redesign | **No** |

**Ownership verdict:** **CLEAN WITH NOTES** — per R4.8; DRIFT-R4-01–08 are implementation-time risks, not architecture violations.

---

## Outstanding Debt

### Blocks implementation

| ID | Item | Notes |
|----|------|-------|
| — | *(none at architecture layer)* | R4.1–R4.8 complete; no architectural blocker for first engine slice |

### Does NOT block implementation (carry-forward)

| ID | Item | Owner | Notes |
|----|------|-------|-------|
| D-R4-01 | `publish_result_models.py` | R4.7+ code | R4.5 contract defined; dataclass deferred |
| D-R4-02 | `ear_publish_engine.py` | Post-R4.9 | R4.7 architecture only |
| D-R4-03 | `--publish-snapshot` CLI | R4.7 implementation | Flag name SAFE UNKNOWN |
| D-R4-04 | Store publish metadata persist adapter | Store adapter | DRIFT-R4-03; metadata only — not section tree |
| D-R4-05 | Consumer registry pointer physical encoding | R4.3/R4.7 | R1.8B OQ-04 — SAFE UNKNOWN |
| D-R4-06 | `publish_state` Store sidecar encoding | R4.2 implementation | SAFE UNKNOWN |
| D-R4-07 | Supersession automation — active default per site | Future | Architecture SAFE UNKNOWN |
| D-R4-08 | Operator NOT_ELIGIBLE override audit schema | Operator workflow | Exception path only |
| D-R4-09 | Atomic Publish + metadata write failure recovery | R4.7 implementation | SAFE UNKNOWN |
| D-R4-10 | Combined Store+Publish HITL enforcement | R4.6 / engine | DRIFT-R4-04 |
| D-R4-11 | In-memory validated path on production default | R4.7 | DRIFT-R4-08 — pilot-only recommended |
| D-R4-12 | Mock R5 bundle for contract-path Publish demo | R4 implementation | Until R5 engine exists |

### Blocks live execution only

| ID | Item | Source |
|----|------|--------|
| D-LIVE-01 | R5 Validate Engine not implemented | R5 debt — real Publish requires validated bundle |
| D-LIVE-02 | Contract-path Store persist (R3) | R3-READINESS |
| D-LIVE-03 | Quarantine persist (R2) | R2-READINESS |
| D-LIVE-04 | Bulk expansion HO-ALLOW-10 (R3) | R3-READINESS |
| D-LIVE-05 | Live SFTP / SITE-001 / PILOT-001 | Execution Authorization |
| D-LIVE-06 | Production `snapshot_id` algorithm | Live path |
| D-LIVE-07 | OCPilot consumer bulk copy to `project-sites\` | Consumer program + pointer encoding |

### Inherited from R2/R3/R5 (R4-adjacent)

| ID | Item | Source |
|----|------|--------|
| D-INH-01 | Quarantine index on disk | R2-READINESS |
| D-INH-02 | Contract-path Store persist | R3-READINESS |
| D-INH-03 | Validate Engine + `--validate-snapshot` | R5-READINESS |
| D-INH-04 | `publish_eligibility_models.py` / `validate_report_models.py` | R5-READINESS |

---

## Architecture Verdict

| Verdict | **R4 COMPLETE WITH NOTES** |
|---------|----------------------------|

| Question | Answer |
|----------|--------|
| Can R4 be considered **COMPLETE WITH NOTES**? | **Yes** — all R4.1–R4.8 milestones closed; charters complete; Publish Engine intentionally not started |
| Is EAR publish architecture closed at design layer? | **Yes** — R4.1–R4.8 + charters + boundary review form closed contract set |
| Can future R4 implementation work be authorized? | **Yes, with human gate** — R4.9 decision + operator approval before first Publish Engine code |
| Can R5 implementation proceed in parallel? | **Yes** — R4 does not block R5 engine; runtime order remains Validate → Publish |
| Can SITE-001 preparation continue? | **Yes, architecture/documentation** — live Publish remains **Execution Authorization** gated |

**Why COMPLETE WITH NOTES (not bare COMPLETE):** no Publish Engine or CLI yet; R4.5/R4.6 contract-only (no `publish_result_models.py`); inherited R2/R3/R5 debt for live paths; consumer registry pointer and Store metadata encoding SAFE UNKNOWN; human implementation gate still required per program pattern.

---

## Risks

| Risk | Severity | Classification | Mitigation |
|------|----------|----------------|------------|
| R4 implemented as Validate or R3 assembly | High | **Non-blocker** (design mitigated) | R4.8 VB-R4-*; stop conditions ST-IC-R4-01–03 |
| ELIGIBLE recommendation treated as auto-Publish | High | **Non-blocker** | R4.6 dual HITL; PF-INV-R4-* |
| Quality inflation at Publish | High | **Non-blocker** | PS-INV-R4-04; R4 freeze only |
| Stage 4 "Publish Assembly" conflated with R3 assembly | Medium | **Non-blocker** | DRIFT-R4-01; PE-INV-R4-09; N-R4.8-01 |
| Stage 2 gate verification conflated with R5 Validate | Medium | **Non-blocker** | DRIFT-R4-02; VB-R4-05 |
| stored-unpublished exposed to consumers | High | **Non-blocker** | CB-R4-02; R4.3 |
| PublishResult SUCCESS conflated with ValidationResult PASS | High | **Non-blocker** | PR-INV-R4-01; PR-INV-R4-05 |
| Live SITE-001 Publish without Validate/Store | Medium | **Blocker for live only** | D-LIVE-01/02; not architecture blocker |
| Dual HITL fatigue — operators skip Publish approval | Medium | **Non-blocker** | ST-IC-R4-10; PF-INV-R4-04 |

---

## SAFE UNKNOWN

| Topic | Status | Blocker? |
|-------|--------|----------|
| PublishResult serialization format | **SAFE UNKNOWN** | **Non-blocker** |
| `publish_state` Store encoding | **SAFE UNKNOWN** | **Non-blocker** for mock implementation |
| Consumer registry pointer location (EAR store vs OCPilot `project-sites\`) | **SAFE UNKNOWN** | **Non-blocker** |
| Physical publish metadata encoding (metadata/ vs acquisition-log/) | **SAFE UNKNOWN** | **Non-blocker** |
| Official JSON Schema for Publish artefacts | **Not in repo** | **Non-blocker** |
| Supersession automation — active default per site | **Architecture SAFE UNKNOWN** | **Non-blocker** |
| Operator override audit schema on NOT_ELIGIBLE | **Operator workflow** | **Non-blocker** |
| Atomic Publish + metadata write failure recovery | **SAFE UNKNOWN** | **Non-blocker** |
| `--publish-snapshot` CLI flag exact name | **SAFE UNKNOWN** | **Non-blocker** |
| 1:N `acquisition_id` → `snapshot_id` publish policy | **Architecture SAFE UNKNOWN** | **Non-blocker** |
| Whether R4 copies contract slice to consumer path vs reference only | **R1.8B hybrid model** | **Non-blocker** |
| In-memory validated snapshot on production Publish default | **Pilot-only recommended** | **Blocker for live only** |
| Production acquisition_id / snapshot_id algorithms | **SAFE UNKNOWN** | **Blocker for live only** |

---

## What remains outside R4

| Area | Owner / phase |
|------|---------------|
| R5 EAR Validate execution, quality certification, redaction review | **R5** |
| R3 snapshot assembly, section population | **R3** |
| R2 evidence generation, quarantine writes | **R2** |
| R1 acquisition / connector live execution | **R1** + Execution Authorization |
| Publish Engine orchestrator code | **Post-R4.9 implementation** |
| `--publish-snapshot` CLI | **Post-R4.9 implementation** |
| Store publish metadata write adapter | **R1.8 layout + R4 adapter** |
| Consumer program execution (OCPilot Run 5, baseline diff) | **Consumer programs** |
| Live SFTP / SITE-001 / PILOT execution | **Execution Authorization** |
| Normative JSON Schema files | **Architecture** |
| Unattended auto-Publish | **Non-goal** — operator HITL mandatory |
| Store layout redesign | **Frozen** R1.9 |

---

## Evidence index

| ID | Source |
|----|--------|
| E-R4R-01 | [R4-CHARTER-v1.md](R4-CHARTER-v1.md) through [R4.8-PUBLISH-BOUNDARY-DECISION-v1.md](R4.8-PUBLISH-BOUNDARY-DECISION-v1.md) |
| E-R4R-02 | [R5-READINESS-DECISION-v1.md](R5-READINESS-DECISION-v1.md) |
| E-R4R-03 | [R3-READINESS-DECISION-v1.md](R3-READINESS-DECISION-v1.md) |
| E-R4R-04 | `runtime/shared/published_snapshot_models.py` |
| E-R4R-05 | `runtime/shared/publish_state_models.py` |
| E-R4R-06 | `runtime/shared/consumer_visibility_models.py` |
| E-R4R-07 | `runtime/shared/publish_metadata_models.py` |
| E-R4R-08 | `runtime/connectors/sftp_connector.py` — `--contract-snapshot` |
| E-R4R-09 | CLI verification 2026-06-07 |

---

## Cross-references

| Document | Use |
|----------|-----|
| [R4-READINESS-DECISION-v1.md](R4-READINESS-DECISION-v1.md) | Gate decision |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Program status update |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation update |

---

## Truth statement

| Claim | Accurate? |
|-------|-----------|
| R4 all milestones R4.1–R4.8 closed | **Yes** |
| R4 Publish Engine implemented | **No** |
| R4 architecture sufficient for implementation authorization | **Yes, with notes** |
| Critical ownership violation found | **No** |
| R5 Validate Engine implemented | **No** |
| R4 program **COMPLETE WITH NOTES** at architecture layer | **Yes** — see decision companion |
| EAR publish architecture closed at design layer | **Yes** |
