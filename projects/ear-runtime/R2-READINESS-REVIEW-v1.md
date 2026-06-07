# R2 — Readiness Review v1

**Type:** Engineering readiness assessment — **no** implementation, **no** generator/validator/persistence/snapshot changes  
**Phase:** R2 — Evidence Package Layer (closure gate before R3)  
**Date:** 2026-06-05  
**Decision companion:** [R2-READINESS-DECISION-v1.md](R2-READINESS-DECISION-v1.md)  
**Question:** Is R2 complete enough to close formally, and is EAR Runtime ready to enter **R3 Snapshot Assembly**?

**Explicit exclusions:** generator changes, validator changes, persistence changes, snapshot changes, runtime code changes, model changes, OpenCart sections, SITE-001, SFTP, acquisition, network.

---

## Purpose

Consolidate evidence from the full R2 chain (charter through R2.7 implementation) and assess:

1. Milestone completion (R2.1–R2.7)  
2. Runtime implementation coverage  
3. R1.6 vs R2 migration status  
4. R3 entry readiness  
5. R2 closure posture  
6. Outstanding debt (document only)

---

## Sources reviewed

| ID | Document | Role |
|----|----------|------|
| S-R2R-01 | [R2-CHARTER-v1.md](R2-CHARTER-v1.md) | Program mission, scope, non-goals, success criteria |
| S-R2R-02 | [R2-IMPLEMENTATION-CHARTER-v1.md](R2-IMPLEMENTATION-CHARTER-v1.md) | Engineering milestones E-01–E-07, IAC acceptance |
| S-R2R-03 | [R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md](R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md) | Pre-R2.7 coherence pass |
| S-R2R-04 | [R2.7-EVIDENCE-PACKAGE-GENERATOR-v1.md](R2.7-EVIDENCE-PACKAGE-GENERATOR-v1.md) | R2.7 implementation record |
| S-R2R-05 | [R2.7-EVIDENCE-PACKAGE-GENERATOR-DECISION-v1.md](R2.7-EVIDENCE-PACKAGE-GENERATOR-DECISION-v1.md) | R2.7 gate decision |
| S-R2R-06 | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Program status |
| S-R2R-07 | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation |
| S-R2R-08 | `runtime/` modules (read-only inspection) | Implementation evidence |

**Runtime modules inspected (read-only):**

| Module | Evidence for |
|--------|--------------|
| `runtime/shared/evidence_package_models.py` | R2.1 model |
| `runtime/builders/evidence_package_builder.py` | R2.7 generator, identity, artifact index |
| `runtime/validators/evidence_package_validator.py` | R2.4 structural validation |
| `runtime/connectors/sftp_connector.py` | CLI paths, dual R1.6/R2 wiring |
| `runtime/cli.py` | `--contract-evidence` vs `--mock-evidence` |
| `runtime/builders/snapshot_builder.py` | R1.6 dependency in snapshot chain |
| `runtime/builders/evidence_builder.py` | R1.6 legacy path |
| `runtime/shared/evidence_models.py` | R1.6 skeleton model |

---

## Milestone Status

| Milestone | Name | Status | Evidence |
|-----------|------|--------|----------|
| **R2.1** | Evidence Package Model | **DONE** | [R2.1-EVIDENCE-PACKAGE-MODEL-v1.md](R2.1-EVIDENCE-PACKAGE-MODEL-v1.md); `evidence_package_models.py` — `EvidencePackage`, `EvidenceIdentity`, `EvidenceArtifactIndex`, taxonomy constants |
| **R2.2** | Evidence Identity Review | **DONE** | [R2.2-EVIDENCE-IDENTITY-REVIEW-v1.md](R2.2-EVIDENCE-IDENTITY-REVIEW-v1.md); [R2.2-EVIDENCE-IDENTITY-DECISION-v1.md](R2.2-EVIDENCE-IDENTITY-DECISION-v1.md) — **PASS WITH NOTES**; binding rules documented; implemented in `evidence_package_builder._build_identity()` |
| **R2.3** | Evidence Artifact Index | **DONE** | [R2.3-EVIDENCE-ARTIFACT-INDEX-v1.md](R2.3-EVIDENCE-ARTIFACT-INDEX-v1.md); [R2.3-EVIDENCE-ARTIFACT-INDEX-DECISION-v1.md](R2.3-EVIDENCE-ARTIFACT-INDEX-DECISION-v1.md) — **PASS WITH NOTES**; `_build_artifact_index()` emits manifest + metadata entries |
| **R2.4** | Evidence Validation Boundary | **DONE** | [R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md); [R2.4-EVIDENCE-VALIDATION-DECISION-v1.md](R2.4-EVIDENCE-VALIDATION-DECISION-v1.md) — **PASS WITH NOTES**; `evidence_package_validator.py` implements R2-V-* subset |
| **R2.5** | Evidence Quarantine Layout | **DONE** (architecture) / **PARTIAL** (code) | [R2.5-EVIDENCE-QUARANTINE-LAYOUT-v1.md](R2.5-EVIDENCE-QUARANTINE-LAYOUT-v1.md); [R2.5-EVIDENCE-QUARANTINE-DECISION-v1.md](R2.5-EVIDENCE-QUARANTINE-DECISION-v1.md) — **PASS WITH NOTES**; layout **documented**; `EvidenceQuarantineLayout` writer **not implemented** (R2.7 § Known Limitations) |
| **R2.6** | Evidence → Snapshot Handoff | **DONE** (architecture) / **PARTIAL** (code) | [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md); [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-DECISION-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-DECISION-v1.md) — **PASS WITH NOTES**; `HandoffContract` **spec only** — no code module |
| **R2.7** | Evidence Package Generator | **DONE** | [R2.7-EVIDENCE-PACKAGE-GENERATOR-v1.md](R2.7-EVIDENCE-PACKAGE-GENERATOR-v1.md); [R2.7-EVIDENCE-PACKAGE-GENERATOR-DECISION-v1.md](R2.7-EVIDENCE-PACKAGE-GENERATOR-DECISION-v1.md) — **PASS WITH NOTES**; builder + validator + `--contract-evidence` wired |

**Architecture consolidation:** [R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md](R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md) — **PASS WITH NOTES**; R2 ready for generator (pre-R2.7).

**Summary:** All seven milestones have **completed review/decision artefacts**. R2.5 and R2.6 are **architecturally DONE** with **implementation debt** explicitly deferred per charter and R2.7 decision.

---

## Implementation Coverage

| Concern | Status | Evidence |
|---------|--------|----------|
| **EvidencePackage model (R2 contract)** | **Implemented** | `evidence_package_models.py` — frozen dataclasses, `to_dict()`, R2.3 taxonomy constants |
| **Identity binding** | **Implemented** | `evidence_package_builder._build_identity()` — `acquisition_id`, `site_ref`, `connector_class`; `build_mock_evidence_acquisition_id()` unifies with `persistence_contract.build_mock_acquisition_id()` |
| **Artifact index** | **Implemented** | `_build_artifact_index()` — manifest + metadata logical refs; `artifact_count` consistent |
| **Structural validation** | **Implemented** | `evidence_package_validator.validate_contract_evidence_package()` — identity, provenance, index, enums, forbidden keys, credential heuristic |
| **Quarantine contract** | **Partially implemented** | R2.5 layout **documented**; no `EvidenceQuarantineLayout` module; no `{acquisition_id}/evidence/` writes |
| **Handoff contract** | **Partially implemented** | R2.6 H-IN-* / HO-* rules **documented**; no `HandoffContract` code; `snapshot_builder.py` still consumes R1.6 `evidence_models.EvidencePackage` |
| **Generator** | **Implemented** | `build_contract_evidence_package()` — in-memory mock-first assembly |
| **CLI integration** | **Implemented** | `cli.py` `--contract-evidence` → `SFTPConnector.build_contract_evidence_package()` |
| **Migration status** | **Partially implemented** | Parallel paths: R2 `--contract-evidence` active; R1.6 `--mock-evidence`, `--mock-snapshot`, `--persist-mock-snapshot` unchanged |

### R2 Implementation Charter acceptance (IAC)

| ID | Criterion | Status | Notes |
|----|-----------|--------|-------|
| IAC-01 | Evidence inspectable and traceable to connector run | **PARTIAL** | R2 path traceable in memory via `--contract-evidence`; primary mock pipeline still R1.6 |
| IAC-02 | Evidence separable from published snapshot tree | **SATISFIED** | R2 model has no snapshot fields; architecture enforces sibling storage |
| IAC-03 | Mock path emits quarantine index under `{acquisition_id}/evidence/` | **NOT SATISFIED** | Explicitly deferred — R2.7 § Known Limitations; R2.5 persist milestone |
| IAC-04 | Mock snapshot Store remains Level 0 honest | **SATISFIED** | R1.8 persist path unchanged; no quality inflation |

---

## Migration Status

### What still depends on R1.6

| Consumer | R1.6 dependency | Evidence |
|----------|-----------------|----------|
| `--mock-evidence` | `evidence_builder.py` + `evidence_models.py` + `evidence_validator.py` | `sftp_connector.build_mock_evidence_package()` L188–189 |
| `--mock-snapshot` | R1.6 evidence → `snapshot_builder.build_snapshot_package()` | `sftp_connector.build_mock_snapshot_package()` L225–237; `snapshot_builder.py` imports `shared.evidence_models` |
| `--persist-mock-snapshot` | Full R1.6 chain through Store | `sftp_connector.persist_mock_snapshot_package()` L269–278 |
| `persistence_contract.DEFAULT_CREATED_FROM` | `"mock_evidence_package"` | Legacy label on persisted snapshots |

### What already uses R2

| Path | R2 usage | Evidence |
|------|----------|----------|
| `--contract-evidence` | Full R2.1 → R2.7 chain | `build_contract_evidence_package()` + `validate_contract_evidence_package()` |
| `acquisition_id` generation | R2.7 unified mock id | `build_mock_evidence_acquisition_id()` → `build_mock_acquisition_id()` |
| Model layer | Parallel R2 contract file | `evidence_package_models.py` coexists with `evidence_models.py` |

### Operational usability

| Question | Answer |
|----------|--------|
| Is R2 operationally usable? | **Yes, on isolated path** — `--contract-evidence` produces validated contract-shaped package in memory |
| Is R2 the default mock pipeline? | **No** — snapshot and persist chains still use R1.6 evidence |
| Does R1.6 block R3? | **No** — R3 Snapshot Assembly is chartered to consume R2 handoff inputs; R1.6 mock chain is legacy parallel path per R2.7 Migration Notes |

---

## R3 Readiness

### Can R3 start?

**Yes — R3 charter and planning may begin.** Required R2 **architecture contracts** are complete (R2.1–R2.6 + consolidation). Required R2 **implementation minimum** for R3 planning is satisfied: R2.1 model + R2.7 in-memory generator + R2.4 validator.

### Required R2 contracts for R3

| Contract | Status | Blocker? |
|----------|--------|----------|
| R2.1 `EvidencePackage` logical model | **Complete** | No |
| R2.2 identity binding rules | **Complete** | No |
| R2.3 artifact index taxonomy | **Complete** | No |
| R2.4 R2 vs R5 validation boundary | **Complete** | No |
| R2.5 quarantine layout spec | **Complete** (doc) | No for R3 charter; persist is R3/R2 follow-on |
| R2.6 handoff inputs (H-IN-*) and prohibitions (HO-FORBID-*) | **Complete** (doc) | No |
| R2.7 mock generator | **Complete** (in-memory) | No |

### Blockers

**None identified** that prevent R3 **charter** authorization. No architectural contradiction between R2 closure and R3 entry per backlog `R1 → R2 → R3`.

### Risks (carry to R3)

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R-R3-01 | Dual evidence models during R3 early work | Medium | R3 charter must name R2.1 as authoritative input; deprecate R1.6 at snapshot boundary |
| R-R3-02 | Snapshot builder still maps R1.6 fields (`site_id`, `quality_level`) | Medium | R3 implements new assembly from `evidence_package_models.EvidencePackage` |
| R-R3-03 | No quarantine on disk — R3 section expansion lacks bulk refs | Low (mock) | Mock-first R3 can use logical refs; quarantine persist tracked as debt |
| R-R3-04 | Scope echo mapping from `allowed_paths` — empty in sample config | Low | Documented SAFE UNKNOWN; R3 must not infer completeness |
| R-R3-05 | Validate terminology collision (R2 structural vs EAR Validate R5) | Medium | R3 docs must disambiguate per R2-ARCHITECTURE-CONSOLIDATION T-03 |

---

## Closure Assessment

| Question | Answer |
|----------|--------|
| Can R2 be considered **COMPLETE**? | **No** — IAC-03 (quarantine index persist) not satisfied; dual-model migration incomplete |
| Can R2 be considered **COMPLETE WITH NOTES**? | **Yes** |
| Can R2 be considered **NOT COMPLETE**? | **No** — all required milestones R2.1–R2.7 have gate decisions; deferred items are scoped and documented |

### Why COMPLETE WITH NOTES

1. **Architecture chain closed** — R2 Charter through R2.6 consolidation coherent; no contradictory ownership (R2-ARCHITECTURE-CONSOLIDATION-DECISION-v1).
2. **Required implementation milestones delivered** — R2.1 model, R2.4 validator code, R2.7 generator code exist in `runtime/`.
3. **Explicit deferrals are charter-aligned** — Quarantine persist (R2.5), HandoffContract code (R2.6 → R3), full pipeline migration (R2.7 Migration Notes) were never blocking items for R2.7 PASS WITH NOTES.
4. **Outstanding IAC-03** — Quarantine index on disk remains open debt; does not invalidate R2 architecture closure but prevents bare **COMPLETE**.

---

## Outstanding Debt

### Remaining R2 debt

| ID | Item | Owner | Notes |
|----|------|-------|-------|
| D-R2-01 | `EvidenceQuarantineLayout` writer — `{acquisition_id}/evidence/` index persist | R2.5+ / post-R2 | IAC-03; N-07 filenames SAFE UNKNOWN |
| D-R2-02 | `HandoffContract` code module | R3 | R2.6 spec complete; R2.7 N-R2.7-01 |
| D-R2-03 | Scope echo config fields (`approved_scope` / `attempted_scope`) | R1.2 / R2 | N-R2.7-03; current mapping from `allowed_paths` |
| D-R2-04 | ISO 8601 timestamp format validation | R2.4 boundary | Documented SAFE UNKNOWN at R2.7 |
| D-R2-05 | Hybrid merge / `leg_ref` (R2.8) | Future | Charter classification Future |
| D-R2-06 | Live connector generator path (R2.10) | Execution Authorization | Optional per charter |

### Migration debt

| ID | Item | Current state |
|----|------|---------------|
| D-MIG-01 | `--mock-snapshot` chain | Uses R1.6 `evidence_models.EvidencePackage` |
| D-MIG-02 | `--persist-mock-snapshot` chain | Uses R1.6 evidence through Store |
| D-MIG-03 | `snapshot_builder.py` input type | Imports `shared.evidence_models`, not `evidence_package_models` |
| D-MIG-04 | Dual CLI evidence flags | `--mock-evidence` (R1.6) and `--contract-evidence` (R2) coexist by design |

### Known limitations (from R2.7)

| Limitation | Documented in |
|------------|---------------|
| In-memory only — no quarantine persist | R2.7-EVIDENCE-PACKAGE-GENERATOR-v1.md |
| Mock `acquisition_id` only | R2.7 |
| Snapshot chain still R1.6 | R2.7 Migration Notes |
| No HandoffContract code | R2.7 |

### SAFE UNKNOWN (not solved)

| Topic | Status |
|-------|--------|
| `evidence_id` as package root identifier | Not in EAR-EVIDENCE-PACKAGE-v1; not introduced |
| Official JSON Schema / ZIP / dump formats | Not in repo |
| Exact `evidence/` index filenames (N-07) | Deferred to quarantine persist |
| Evidence checksum registry | Architecture SAFE UNKNOWN |
| Hybrid 1:N `acquisition_id` → `snapshot_id` | Architecture SAFE UNKNOWN |
| Production `acquisition_id` algorithm (live path) | SAFE UNKNOWN |
| R5 vs R3 ordering when parallel | Backlog allows parallel with risk acceptance |
| CLI runtime verification in this review | Python interpreter not confirmed in review environment — code inspection used |

---

## Recommendations

| # | Recommendation | Priority |
|---|----------------|----------|
| 1 | **Authorize R3 Charter** — reference R2.6 handoff and R2.4 validation boundary | High |
| 2 | **R3 first implementation task:** wire snapshot assembly from `evidence_package_models.EvidencePackage`; deprecate R1.6 at snapshot boundary | High |
| 3 | **Track quarantine persist** as R3-adjacent or R2 follow-on — resolve N-07 filenames before disk writes | Medium |
| 4 | **Retain R1.6 path** until R3 mock snapshot chain migrated — do not delete without charter | Medium |
| 5 | **R3/R5 planning** must cite R2.6 and R2.4 respectively (N-R2-CON-07) | Medium |
| 6 | **Disambiguate Validate** terminology in all R3 documents | Low |

---

## Evidence index

| ID | Source |
|----|--------|
| E-R2R-01 | [R2-CHARTER-v1.md](R2-CHARTER-v1.md) |
| E-R2R-02 | [R2-IMPLEMENTATION-CHARTER-v1.md](R2-IMPLEMENTATION-CHARTER-v1.md) § IAC-01–IAC-04 |
| E-R2R-03 | [R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md](R2-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md) |
| E-R2R-04 | [R2.7-EVIDENCE-PACKAGE-GENERATOR-v1.md](R2.7-EVIDENCE-PACKAGE-GENERATOR-v1.md) |
| E-R2R-05 | `runtime/builders/evidence_package_builder.py` |
| E-R2R-06 | `runtime/validators/evidence_package_validator.py` |
| E-R2R-07 | `runtime/connectors/sftp_connector.py` |
| E-R2R-08 | `runtime/builders/snapshot_builder.py` |
| E-R2R-09 | [EAR-RUNTIME-BACKLOG-v1.md](EAR-RUNTIME-BACKLOG-v1.md) — R1 → R2 → R3 dependency |

---

## Cross-references

| Document | Use |
|----------|-----|
| [R2-READINESS-DECISION-v1.md](R2-READINESS-DECISION-v1.md) | Gate decision |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Program status update |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation update |
