# EAR Stable Baseline — 2026-06

**Type:** Runtime program baseline freeze — documentation only  
**Baseline name:** `EAR-STABLE-BASELINE-2026-06`  
**Freeze date:** 2026-06-07  
**Authority:** Mock E2E Readiness Review PASS — [EAR-MOCK-E2E-READINESS-DECISION-v1.md](EAR-MOCK-E2E-READINESS-DECISION-v1.md)  
**State companion:** [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md)

---

## Purpose

This document marks the **first major transition point** from EAR architecture/runtime construction into **operational dry-run preparation**. It freezes the verified runtime foundation **before** any SITE-001 dry-run planning artefacts or live execution work begins.

**This baseline does not authorize live execution.**

---

## Baseline invariants

This baseline represents:

| Invariant | Meaning |
|-----------|---------|
| **Architecture freeze point** | R1–R5 architecture reviews and contracts closed per milestone decisions; no contract edits implied by this freeze |
| **Runtime foundation freeze point** | Mock-first runtime skeleton, builders, and engines verified through Mock E2E; in-memory path only |
| **Pre-live execution state** | Network access disabled; connector skeleton only; PILOT-001 **NOT AUTHORIZED** |

**Critical truth statement:**

> **Mock E2E PASS does not equal live readiness.**

Mock E2E proves orchestration wiring, ID linkage, and boundary separation on an in-memory happy path. It does **not** prove acquisition quality, Validate trust with real assessors, Store placement, credential resolution, or PILOT execution safety.

---

## Architecture status

| Field | Value |
|-------|-------|
| EAR Architecture Program | **COMPLETE** (frozen 2026-06-01) |
| Architecture source | [shared/external-access-runtime/](../../shared/external-access-runtime/) |
| Runtime Transition Freeze | **YES** — [freeze/EAR-RUNTIME-TRANSITION-v1/](../../shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/) |
| Runtime Engineering Charter | **APPROVED** — [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) |
| R1–R5 architecture closure | **COMPLETE** (R1 foundation; R2–R5 per readiness decisions with notes) |
| Mock E2E Readiness Review | **PASS** — **READY FOR SITE-001 DRY-RUN PLANNING WITH NOTES** |

---

## Runtime status

| Field | Value |
|-------|-------|
| Program | **STARTED** |
| Implementation scope | Foundation + connector skeleton + mock listing/manifest/evidence/snapshot + mock Store persist + R2/R3 contract paths + R4/R5 engine skeletons + Mock E2E |
| Network access | **DISABLED** |
| Live access | **FORBIDDEN** |
| Connector | **SKELETON ONLY** — no paramiko/network execution |
| Persistence | **IMPLEMENTED (mock Store only)** — R3 contract path not persisted |
| Validate Engine | **SKELETON ONLY** — mock assessors; always PASS on happy path |
| Publish Engine | **SKELETON ONLY** — in-memory path; Store adapter **NOT IMPLEMENTED** |
| Mock E2E | **IMPLEMENTED** — verification PASS on `sample-r1-site-001.json` |
| Pilots executed | **0** |
| Operational readiness | **READY FOR SITE-001 DRY-RUN PLANNING WITH NOTES** |

---

## Milestone matrix (R1–R5)

| Milestone | Name | Status | Notes |
|-----------|------|--------|-------|
| **R1** | SFTP Read-Only Connector | **COMPLETE** | R1.1–R1.9 **DONE**; connector **SKELETON ONLY**; listing/manifest/evidence/snapshot **MOCK ONLY**; mock Store persist **VERIFIED**; human decision gate [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md) reconciled via [R1-GATE-RECONCILIATION-v1.md](R1-GATE-RECONCILIATION-v1.md) — **OPEN** for live connector |
| **R2** | Evidence Package Generator | **COMPLETE WITH NOTES** | R2.1–R2.7 **DONE**; `--contract-evidence` in-memory path **IMPLEMENTED**; quarantine persist **DEFERRED**; R1.6 → R2 contract migration debt documented |
| **R3** | Snapshot Builder | **COMPLETE WITH NOTES** | R3.1–R3.7 **DONE**; `--contract-snapshot` in-memory path **IMPLEMENTED**; Store persist on contract path **NOT DONE**; bulk expansion debt; production snapshot ID algorithm **SAFE UNKNOWN** |
| **R4** | Snapshot Publisher | **COMPLETE WITH NOTES** | R4.1–R4.9 **DONE**; Publish Engine skeleton **IMPLEMENTED**; Store adapter **NOT IMPLEMENTED**; consumer registry execution **NOT EXERCISED** |
| **R5** | Validation Helpers | **COMPLETE WITH NOTES** | R5.1–R5.9 **DONE**; Validate Engine skeleton **IMPLEMENTED**; real category assessors (R5-V-*) **NOT IMPLEMENTED** |

### Milestone decision references

| Milestone | Readiness decision |
|-----------|-------------------|
| R1 | [R1.9-HARDENING-DECISION-v1.md](R1.9-HARDENING-DECISION-v1.md) — Store **PASS WITH NOTES**; foundation chain complete |
| R2 | [R2-READINESS-DECISION-v1.md](R2-READINESS-DECISION-v1.md) — **READY FOR R3 WITH NOTES** |
| R3 | [R3-READINESS-DECISION-v1.md](R3-READINESS-DECISION-v1.md) — **READY FOR R5 WITH NOTES** |
| R4 | [R4-READINESS-DECISION-v1.md](R4-READINESS-DECISION-v1.md) — **READY FOR R4 IMPLEMENTATION WITH NOTES** |
| R5 | [R5-READINESS-DECISION-v1.md](R5-READINESS-DECISION-v1.md) — **READY FOR R5 IMPLEMENTATION WITH NOTES** |

---

## Runtime implementation matrix

| Component | Status | Implementation | Scope / limitation |
|-----------|--------|----------------|-------------------|
| **Evidence Package Builder** | **IMPLEMENTED** | `runtime/builders/evidence_package_builder.py` | Mock-first contract path; `--contract-evidence`; in-memory only; R2.7 binding |
| **Candidate Snapshot Builder** | **IMPLEMENTED** | `runtime/builders/snapshot_package_builder.py` | Mock-first contract path; `--contract-snapshot`; in-memory only; R3.5 handoff |
| **Validate Engine** | **SKELETON IMPLEMENTED** | `runtime/engines/ear_validate_engine.py` | Seven-stage orchestration; mock assessors only; no filesystem writes; advisory eligibility only |
| **Publish Engine** | **SKELETON IMPLEMENTED** | `runtime/engines/ear_publish_engine.py` | Seven-stage orchestration; `in_memory_path=True` bypass; mock snapshot prefix gate; Store adapter absent |
| **Mock E2E Engine** | **IMPLEMENTED** | `runtime/engines/ear_mock_e2e_engine.py` | Config → R2 → R3 → R5 → R4 in-memory; verification PASS; happy path only in auto-verification |

---

## Implemented milestones (detailed)

### R1 foundation (R1.1–R1.9)

| ID | Milestone | Status |
|----|-----------|--------|
| R1.1 | Runtime Skeleton | **DONE** |
| R1.2 | Config Input Model | **DONE** |
| R1.3 | Connection Layer Skeleton | **DONE** |
| R1.4 | Remote Listing Model | **DONE** (mock only) |
| R1.5 | Manifest Builder Skeleton | **DONE** (mock only) |
| R1.6 | Evidence Package Model | **DONE** (mock only) |
| R1.7 | Snapshot Package Model | **DONE** (mock only) |
| R1.8 | Persistence Model | **DONE** (mock Store only) |
| R1.8A–R1.8E | Persistence design / verification | **DONE** |
| R1.9 | Store Hardening | **DONE** (**PASS WITH NOTES**) |

### R2 evidence layer (R2.1–R2.7)

| ID | Milestone | Status |
|----|-----------|--------|
| R2.1 | Evidence Package Model | **DONE** |
| R2.2 | Evidence Identity Review | **DONE** (**PASS WITH NOTES**) |
| R2.3 | Evidence Artifact Index | **DONE** (**PASS WITH NOTES**) |
| R2.4 | Evidence Validation Boundary | **DONE** (**PASS WITH NOTES**) |
| R2.5 | Evidence Quarantine Layout | **DONE** (**PASS WITH NOTES**; persist deferred) |
| R2.6 | Evidence → Snapshot Handoff | **DONE** (**PASS WITH NOTES**) |
| R2.7 | Evidence Package Generator | **DONE** (**PASS WITH NOTES**; implemented) |
| R2 | Readiness Review | **COMPLETE WITH NOTES** |

### R3 snapshot assembly (R3.1–R3.7)

| ID | Milestone | Status |
|----|-----------|--------|
| R3.1 | Snapshot Package Model | **DONE** (**PASS WITH NOTES**) |
| R3.2 | Snapshot Identity Layer | **DONE** (**PASS WITH NOTES**) |
| R3.3 | Section Assembly Rules | **DONE** (**PASS WITH NOTES**) |
| R3.4 | Safe Unknown Propagation | **DONE** (**PASS WITH NOTES**) |
| R3.5 | Candidate Snapshot Generator | **DONE** (**PASS WITH NOTES**; implemented) |
| R3.6 | Validation Boundary Review | **DONE** (**PASS WITH NOTES**) |
| R3 | Readiness Review | **COMPLETE WITH NOTES** |

### R5 validate layer (R5.1–R5.9)

| ID | Milestone | Status |
|----|-----------|--------|
| R5.1 | Validation Result Model | **DONE** (**PASS WITH NOTES**) |
| R5.2 | Validation Category Model | **DONE** (**PASS WITH NOTES**) |
| R5.3 | Quality Possession Model | **DONE** (**PASS WITH NOTES**) |
| R5.4 | Redaction Review Model | **DONE** (**PASS WITH NOTES**) |
| R5.5 | Validate Report Contract | **DONE** (**PASS WITH NOTES**; contract only) |
| R5.6 | Publish Eligibility Contract | **DONE** (**PASS WITH NOTES**; contract only) |
| R5.7 | Validate Engine Architecture | **DONE** (**PASS WITH NOTES**; skeleton implemented) |
| R5.8 | Validation Boundary Review | **DONE** (**PASS WITH NOTES**) |
| R5 | Readiness Review | **COMPLETE WITH NOTES** |

### R4 publish layer (R4.1–R4.9)

| ID | Milestone | Status |
|----|-----------|--------|
| R4.1 | Published Snapshot Model | **DONE** (**PASS WITH NOTES**) |
| R4.2 | Publish State Model | **DONE** (**PASS WITH NOTES**) |
| R4.3 | Consumer Visibility Model | **DONE** (**PASS WITH NOTES**) |
| R4.4 | Publish Metadata Model | **DONE** (**PASS WITH NOTES**) |
| R4.5 | Publish Result Contract | **DONE** (**PASS WITH NOTES**; contract only) |
| R4.6 | Publish Flow Contract | **DONE** (**PASS WITH NOTES**; contract only) |
| R4.7 | Publish Engine Architecture | **DONE** (**PASS WITH NOTES**; skeleton implemented) |
| R4.8 | Publish Boundary Review | **DONE** (**PASS WITH NOTES**) |
| R4 | Readiness Review | **COMPLETE WITH NOTES** |

### Mock E2E

| ID | Milestone | Status |
|----|-----------|--------|
| Mock E2E Flow v1 | [EAR-MOCK-E2E-FLOW-v1.md](EAR-MOCK-E2E-FLOW-v1.md) | **IMPLEMENTED** |
| Mock E2E Readiness Review | [EAR-MOCK-E2E-READINESS-REVIEW-v1.md](EAR-MOCK-E2E-READINESS-REVIEW-v1.md) | **PASS** |

---

## Implemented engines

| Engine | Module | Stage count | Authority |
|--------|--------|-------------|-----------|
| Validate Engine | `runtime/engines/ear_validate_engine.py` | 7 | Certification status + advisory publish eligibility |
| Publish Engine | `runtime/engines/ear_publish_engine.py` | 7 | Authoritative PublishResult + promotion artefacts |
| Mock E2E Engine | `runtime/engines/ear_mock_e2e_engine.py` | 5 (orchestration) | In-memory chain verification only |

---

## Implemented models

| Layer | Module(s) | Notes |
|-------|-----------|-------|
| R1 config / listing / manifest / evidence / snapshot | `config_loader.py`, `listing_models.py`, `manifest_models.py`, `evidence_models.py`, `snapshot_models.py` | Legacy mock pipeline |
| R1 persistence | `persistence_contract.py`, `snapshot_store.py` | Mock Store only |
| R2 contract evidence | `evidence_package_models.py` | Dataclasses + taxonomy constants |
| R3 contract snapshot | `snapshot_package_models.py`, `handoff_contract.py` | OpenCart section tree; identity rules |
| R5 validate | `validation_result_models.py`, `validation_category_models.py`, `quality_possession_models.py`, `redaction_review_models.py`, `validate_report_models.py`, `publish_eligibility_models.py` | Models + report/eligibility dataclasses |
| R4 publish | `published_snapshot_models.py`, `publish_state_models.py`, `consumer_visibility_models.py`, `publish_metadata_models.py`, `publish_result_models.py` | Full publish artefact set |

---

## Implemented contracts

| Contract | Document | Runtime binding |
|----------|----------|-----------------|
| Connector contract | `connector_contract.py` | R1.3 skeleton |
| Persistence / storage | [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) | Mock Store |
| R2 → R3 handoff | `handoff_contract.py` | ID-R3-14 mock prefix; production algorithm **SAFE UNKNOWN** |
| R2 evidence validation boundary | [R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md) | Structural validator only |
| R3 validation boundary | [R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md](R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md) | VB-R3-01–18 |
| R5 Validate Report | [R5.5-VALIDATE-REPORT-CONTRACT-v1.md](R5.5-VALIDATE-REPORT-CONTRACT-v1.md) | Eleven-section operator audit |
| R5 Publish Eligibility | [R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md](R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md) | Advisory only |
| R5 validation boundary | [R5.8-VALIDATION-BOUNDARY-REVIEW-v1.md](R5.8-VALIDATION-BOUNDARY-REVIEW-v1.md) | VB-R5-01–15 |
| R4 Publish Result | [R4.5-PUBLISH-RESULT-CONTRACT-v1.md](R4.5-PUBLISH-RESULT-CONTRACT-v1.md) | SUCCESS / BLOCKED / DEFERRED |
| R4 Publish Flow | [R4.6-PUBLISH-FLOW-CONTRACT-v1.md](R4.6-PUBLISH-FLOW-CONTRACT-v1.md) | G1–G6 gate sequence; dual HITL |
| R4 publish boundary | [R4.8-PUBLISH-BOUNDARY-REVIEW-v1.md](R4.8-PUBLISH-BOUNDARY-REVIEW-v1.md) | VB-R4-01–18 |

---

## Implemented reviews

| Review | Outcome | Date |
|--------|---------|------|
| R1 Implementation Readiness | **CONDITIONAL GO** | 2026-06-02 |
| R1.8E Persistence Verification | **PASS WITH NOTES** | 2026-06-04 |
| R1.9 Store Hardening | **PASS WITH NOTES** | 2026-06-04 |
| R2 Readiness Review | **READY FOR R3 WITH NOTES** | 2026-06-05 |
| R3 Readiness Review | **READY FOR R5 WITH NOTES** | 2026-06-06 |
| R5 Readiness Review | **READY FOR R5 IMPLEMENTATION WITH NOTES** | 2026-06-07 |
| R4 Readiness Review | **READY FOR R4 IMPLEMENTATION WITH NOTES** | 2026-06-07 |
| Mock E2E Readiness Review | **READY FOR SITE-001 DRY-RUN PLANNING WITH NOTES** | 2026-06-07 |

---

## Operational readiness

### Current state

**READY FOR SITE-001 DRY-RUN PLANNING WITH NOTES**

Operators may:

- Draft SITE-001 dry-run plan (operator checklist, HITL sequence, evidence bar)
- Reference `E2EMockBundle` / `E2EFlowSummary` shape in planning docs
- Run mock E2E verification locally (`py -3 engines/ear_mock_e2e_engine.py` from `runtime/`)
- Execute manual negative-path engine tests without live access

### NOT AUTHORIZED

| Action | Status |
|--------|--------|
| Live SFTP | **NOT AUTHORIZED** |
| Connected acquisition | **NOT AUTHORIZED** |
| Production snapshot IDs | **NOT AUTHORIZED** |
| PILOT-001 execution | **NOT AUTHORIZED** |
| Consumer publication / OCPilot intake execution | **NOT AUTHORIZED** |
| Interpret mock SUCCESS as live readiness | **FORBIDDEN** |

### Gate record at freeze

| Gate | Value |
|------|-------|
| PILOT-001 Execution Authorization | **NO** |
| Live access | **FORBIDDEN** |
| Network access | **DISABLED** |
| Mock E2E Readiness | **PASS** (planning scope only) |

---

## Known limitations

| ID | Limitation | Classification |
|----|------------|----------------|
| L-BL-01 | Connector is skeleton only — no network/paramiko execution | Live blocker |
| L-BL-02 | All acquisition inputs mock-only on contract path | Live blocker |
| L-BL-03 | Validate assessors are skeleton — empty findings always PASS on happy path | Near-term |
| L-BL-04 | Publish Store adapter not implemented; `in_memory_path=True` bypasses placement gate | Near-term |
| L-BL-05 | Mock E2E auto-verification covers happy path only | Near-term |
| L-BL-06 | CLI `--mock-e2e` flag not implemented — Python/`__main__` only | Near-term |
| L-BL-07 | R3 contract path not persisted to Store | Deferred |
| L-BL-08 | R2 quarantine persist deferred (R2.5) | Deferred |
| L-BL-09 | R1.6 legacy mock pipeline coexists with R2 contract path — migration debt | Deferred |
| L-BL-10 | R3 bulk section expansion not implemented | Deferred |
| L-BL-11 | R1 human implementation decision gate formally **OPEN** (reconciled for R1.1/R1.2) | Governance |
| L-BL-12 | 10 safe-unknown entries normal on mock path — not representative of live evidence bar | Informational |

---

## Live execution blockers

| Blocker | Required before live |
|---------|---------------------|
| PILOT-001 Execution Authorization | Human gate per [PILOT-GOVERNANCE-v1.md](../../shared/external-access-runtime/PILOT-GOVERNANCE-v1.md) |
| Live SFTP connector implementation | R1 connected acquisition |
| Credential vault / `credential_ref` resolution | Config no longer SAFE_UNKNOWN |
| Production snapshot ID algorithm | R3.2 live identity path |
| Real remote listing from SITE-001 | Connected acquisition |
| Real R5 category assessors (R5-V-*) | Meaningful Validate trust |
| R4 Store adapter + placement confirmation | Production Publish path |
| R1 human decision gate closure | Live connector authorization |
| SITE-001 dry-run plan + execution authorization | Separate gate from this baseline |

---

## SAFE UNKNOWN

| Topic | Status | Would verify by |
|-------|--------|-----------------|
| Production snapshot ID algorithm | **SAFE UNKNOWN** — declared not implemented in `handoff_contract.py` | R3.2 identity on live path |
| SITE-001 `credential_ref` resolution | **SAFE UNKNOWN** — placeholder in `sample-r1-site-001.json` | Operator credential vault audit |
| SITE-001 `remote_root` path | **SAFE UNKNOWN** — placeholder in fixture | PILOT preflight against TEST host |
| Real Store placement confirmation flow | **NOT EXERCISED** — bypassed via `in_memory_path=True` | R4 Store adapter integration test |
| Consumer visibility execution | **NOT EXERCISED** — logical grant in skeleton only | OCPilot intake integration |
| Live listing scope vs `excluded_paths` adequacy | **SAFE UNKNOWN** | Connected acquisition dry-run (when authorized) |
| Whether 10 safe-unknown entries meet Level 1 bar for SITE-001 live | **SAFE UNKNOWN** for live — mock artefact | Real evidence review post-acquisition |
| Negative-path E2E automated coverage | **PARTIAL** — Publish engine standalone smoke only | Mock E2E fixture expansion |

---

## Approved next phase

| Phase | Authorization | Deliverables |
|-------|---------------|--------------|
| **SITE-001 dry-run planning** | **AUTHORIZED** | Dry-run plan document; operator checklist; HITL sequence; evidence bar mapped to `E2EMockBundle` |
| Negative-path E2E fixtures | **AUTHORIZED** (implementation) | Validate FAIL, Publish BLOCKED/DEFERRED in mock verification |
| Optional `--mock-e2e` CLI | **AUTHORIZED** (human gate before merge) | CLI surface for mock E2E |
| Store placement mock adapter | **AUTHORIZED** (no production paths) | E2E Store gate sequence planning |
| Real R5 assessors + R4 Store adapter | **AUTHORIZED** (human gates) | Near-term before live Validate/Publish trust |
| Live SFTP / PILOT-001 / consumer publication | **NOT AUTHORIZED** | Requires separate execution authorization gates |

---

## Related freezes

| Freeze | Location | Relationship |
|--------|----------|--------------|
| EAR Architecture Program | [shared/external-access-runtime/](../../shared/external-access-runtime/) | Upstream — frozen 2026-06-01 |
| Runtime Transition | [shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/](../../shared/external-access-runtime/freeze/EAR-RUNTIME-TRANSITION-v1/) | Architecture → runtime handoff |
| Foundation Start v1 | [freeze/FOUNDATION-START-v1/](freeze/FOUNDATION-START-v1/) | Project placement — 2026-06-02 |
| **Stable Baseline 2026-06** | **This document** | Pre-live runtime foundation — 2026-06-07 |

---

## Truth statement

`EAR-STABLE-BASELINE-2026-06` freezes documented architecture and mock-first runtime wiring at Mock E2E Readiness PASS. It is a **planning and governance checkpoint**, not a live execution authorization. Any work after this baseline that enables network access, production IDs, PILOT execution, or consumer publication requires explicit human gates beyond this freeze.
