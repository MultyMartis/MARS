# R2 — Evidence Package Generator Implementation Charter v1

**Type:** Implementation engineering charter — **no** runtime code, **no** implementation, **no** persistence redesign in this document  
**Date:** 2026-06-04  
**Phase:** R2 — Evidence Package Layer (Evidence Package Generator)  
**Lane:** B — EAR Runtime Engineering  
**Prior gates:** R1 **COMPLETE**; [R2-CHARTER-v1.md](R2-CHARTER-v1.md) **COMPLETE**; [R2-DECISION-v1.md](R2-DECISION-v1.md) — **APPROVED WITH NOTES**  
**Decision companion:** [R2-IMPLEMENTATION-DECISION-v1.md](R2-IMPLEMENTATION-DECISION-v1.md)  
**Architecture sources:** [shared/external-access-runtime/](../../shared/external-access-runtime/)

---

## Charter identity

| Field | Value |
|-------|-------|
| **Authorizes** | R2 engineering scope, milestones, contracts, and deliverable definitions — **not** R3–R5 unless separately chartered |
| **Does not authorize** | Live acquisition, SFTP execution, SITE-001 / PILOT execution, OpenCart snapshot sections, Publish, OCPilot integration, Store redesign, JSON Schema normative files |
| **Human approver** | **Pending** — see [R2-IMPLEMENTATION-DECISION-v1.md](R2-IMPLEMENTATION-DECISION-v1.md) |
| **Program label** | **R2 — Evidence Package Generator** (not snapshot section expansion) |

---

## Mission

### Why R2 engineering exists

R1 closed a mock pipeline (`Config → Listing → Manifest → Evidence → Snapshot → Store`) with an in-memory `EvidencePackage` that **does not** satisfy [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md). Evidence quarantine under `{acquisition_id}/evidence/` was **defined** at R1.8C but **not persisted** ([R1.8E-PERSISTENCE-DECISION-v1.md](R1.8E-PERSISTENCE-DECISION-v1.md)).

R2 engineering translates the approved [R2-CHARTER-v1.md](R2-CHARTER-v1.md) into **executable scope** before coding: model alignment, identity, artifact index, evidence-boundary validation, quarantine layout, and **Evidence → Snapshot** handoff contract for R3.

### Pipeline position (engineering)

```text
Acquisition (R1 connector / mock)
        ↓
Evidence Package          ← R2 engineering scope
        ↓
EAR Validation            ← R5 + human HITL (not R2)
        ↓
Snapshot Package          ← R3
        ↓
Store (R1.8 mock)         ← frozen; R2 adds evidence/ only
```

Per [EAR-SNAPSHOT-LIFECYCLE-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-LIFECYCLE-v1.md): Validation **transforms** evidence into snapshot sections; evidence is **acquisition-internal** until that boundary.

### Gap R2 engineering closes (evidence-backed)

| R1 state | R2 engineering target |
|----------|------------------------|
| No `acquisition_id`, `site_ref`, `connector_class` on evidence model | Contract-aligned identity binding |
| No artifact index or scope echo | Logical index + approved vs attempted scope |
| No connector `success` / `partial` / `failed` on evidence | `EvidenceStatusModel` at evidence boundary |
| Evidence/snapshot conflated in mock chain | Explicit handoff contract; R3 owns sections |
| No `evidence/` on disk | `EvidenceQuarantineLayout` under R1.8C path |
| `quality_level` on R1.6 evidence | **Removed from evidence claims** — no `package_quality_level` at evidence stage |

---

## Engineering Scope

### In scope (R2 implementation — when human gate approves code)

| ID | Area | Engineering deliverable (contract / module names) |
|----|------|---------------------------------------------------|
| E-01 | Evidence Package Model | `EvidencePackage` logical model mapped to EAR-EVIDENCE-PACKAGE-v1; extends R1.6 |
| E-02 | Evidence Identity | Identity binding rules (`acquisition_id`, `site_ref`, `connector_class`, provenance timestamps) |
| E-03 | Evidence Artifact Index | `EvidenceArtifactIndex` — logical refs to manifest, exports, bulk paths |
| E-04 | Evidence Validation (R2 boundary) | `EvidencePackageValidator` — structural + honesty at evidence stage only |
| E-05 | Evidence Quarantine Layout | `EvidenceQuarantineLayout` — `{output_root}/{acquisition_id}/evidence/` index + external bulk refs |
| E-06 | Evidence → Snapshot Handoff | `HandoffContract` — inputs R3 may consume; forbidden R2 actions |
| E-07 | Evidence Package Generator (mock path) | `EvidencePackageGenerator` — assemble from mock/live connector output + acquisition metadata; **mock-first** per R1 discipline |

### Out of scope (explicit — same as R2 Charter)

| Item | Owner |
|------|-------|
| OpenCart sections (`file-manifest/`, `theme-info/`, etc.) | **R3** |
| `package_quality_level` ≥ 1 certification | **R3** + **R5** |
| Publish / consumer intake | **R4** |
| Validate helpers, publish gates, quality possession automation | **R5** |
| Live SFTP, SITE-001, PILOT execution | Execution Authorization |
| Store / snapshot tree redesign | **Frozen** R1.9 |
| Automated redaction product | Future / operator |
| Official JSON Schema / ZIP / dump formats | **SAFE UNKNOWN** |

### Code placement (when implementation authorized)

R2 code may extend **only** under:

```text
projects/ear-runtime/runtime/
```

Likely paths (chartered, not prescriptive filenames):

| Path | Role |
|------|------|
| `runtime/shared/evidence_models.py` | Replace/extend R1.6 skeleton |
| `runtime/builders/evidence_builder.py` | Generator assembly |
| `runtime/validators/evidence_validator.py` | R2-boundary validation |
| `runtime/persistence/` or `runtime/evidence/` | Quarantine index writer (external root only) |

**Forbidden:** `shared/external-access-runtime/` amendments without Architecture Amendment Charter; git-bound evidence bulk; consumer `project-sites\` quarantine.

---

## Work Breakdown

Minimum implementation milestones — ordered dependency chain.

| Milestone | Name | Classification | Depends on | Acceptance (engineering) |
|-----------|------|----------------|------------|--------------------------|
| **R2.1** | Evidence Package Model | **Required** | R1.6 model, EAR-EVIDENCE-PACKAGE-v1 | Logical `EvidencePackage` fields cover required contract categories; R1.6 gap fields mapped |
| **R2.2** | Evidence Identity | **Required** | R2.1, R1-CONTRACT-MAPPING, config | `acquisition_id`, `site_ref`, `connector_class`, provenance timestamps bound; session rules documented |
| **R2.3** | Evidence Artifact Index | **Required** | R2.1, R1.5 manifest chain | Index lists manifest ref, optional bulk refs; no OpenCart `file-manifest/` section |
| **R2.4** | Evidence Validation | **Required** | R2.1–R2.3 | `EvidencePackageValidator` enforces R2 validation boundary; fails closed on missing identity/status |
| **R2.5** | Evidence Quarantine Layout | **Required** | R1.8C layout, R2.3 | Index under `{output_root}/{acquisition_id}/evidence/`; bulk external; no secrets in git |
| **R2.6** | Evidence → Snapshot Handoff | **Required** | R2.1–R2.5, EAR-SNAPSHOT-LIFECYCLE-v1 | `HandoffContract` documents R3 inputs and R2 prohibitions |
| **R2.7** | Evidence Package Generator (mock) | **Required** | R2.1–R2.6, R1 mock pipeline | Mock path emits contract-shaped package + quarantine index; traceable to connector run |
| **R2.8** | Hybrid merge semantics | **Future** | Architecture hybrid coordinator | `leg_ref`, ordered package set — charter note only until architecture amendment |
| **R2.9** | Evidence checksum registry | **SAFE UNKNOWN** | EAR-EVIDENCE-PACKAGE-v1 § SAFE UNKNOWN | Not in R2.1–R2.7 unless architecture resolves |
| **R2.10** | Live connector generator path | **Optional** | R1 live connector + Execution Authorization | Deferred until pilot chartered; mock path is minimum |

### Work package classification summary

| Package | Classification |
|---------|----------------|
| R2.1 Evidence Package Model | **Required** |
| R2.2 Evidence Identity | **Required** |
| R2.3 Evidence Artifact Index | **Required** |
| R2.4 Evidence Validation | **Required** |
| R2.5 Evidence Quarantine Layout | **Required** |
| R2.6 Evidence → Snapshot Handoff | **Required** |
| R2.7 Generator (mock) | **Required** |
| Bulk refs / raw protocol artifacts | **Optional** (channel-dependent) |
| Hybrid merge | **Future** |
| `evidence_id` as package root identifier | **SAFE UNKNOWN** (not in EAR-EVIDENCE-PACKAGE-v1) |
| Retention durations, virus scan | **SAFE UNKNOWN** |

---

## Inputs

### Authoritative upstream (R1 → R2)

| Input | R1 artefact | Use in R2 |
|-------|-------------|-------------|
| **Operator config** | [R1.2-CONFIG-INPUT-MODEL-v1.md](R1.2-CONFIG-INPUT-MODEL-v1.md), `runtime/shared/config_loader.py`, `runtime/configs/*.json` | `output_root`, `site_id`→`site_ref`, `connector`→`connector_class`, `mode`→`ear_mode`, scope paths, `environment` |
| **Contract mapping** | [R1-CONTRACT-MAPPING-v1.md](R1-CONTRACT-MAPPING-v1.md) | `acquisition_id` generation, `operator_approval_ref`, channel derivation |
| **Listing** | [R1.4-REMOTE-LISTING-MODEL-v1.md](R1.4-REMOTE-LISTING-MODEL-v1.md), `listing_models.py`, `mock_listing.py` | Scope echo inputs (attempted paths); listing summary for artifact index |
| **Manifest** | [R1.5-MANIFEST-BUILDER-SKELETON-v1.md](R1.5-MANIFEST-BUILDER-SKELETON-v1.md), `manifest_models.py`, `manifest_builder.py` | Primary artifact index entry (`file-manifest` logical ref); entry/excluded counts |
| **Evidence skeleton** | [R1.6-EVIDENCE-PACKAGE-MODEL-v1.md](R1.6-EVIDENCE-PACKAGE-MODEL-v1.md), `evidence_models.py` | **Refactor target** — replace `site_id`/`quality_level` pattern with contract fields |
| **Connector output** | `sftp_connector.py` mock chain, future `connector-status.json` | Status, errors, warnings, manifest paths |
| **Persistence layout** | [R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md](R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md) | `{acquisition_id}/evidence/` sibling to `snapshots/` |
| **Storage contract** | [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) | External `output_root`; hybrid roles unchanged |
| **Snapshot model (boundary only)** | [R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md](R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md) | **Not** evidence input — defines what R2 must **not** pre-build |

### Architecture contracts (read-only inputs)

| Contract | Role |
|----------|------|
| [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) | Normative evidence semantics |
| [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) | Quarantine vs git vs consumer |
| [EAR-SNAPSHOT-LIFECYCLE-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-LIFECYCLE-v1.md) | Acquire → Validate boundary |
| [EAR-CONNECTOR-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-CONTRACT-v1.md) | Status, errors, warnings |
| [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) | R2 acceptance definition |

### Explicit non-inputs

| Artefact | Reason |
|----------|--------|
| Mock Store snapshot JSON (R1.8) | Snapshot persist is R3+ consumer of validated evidence |
| OpenCart section specs | R3 Snapshot Builder |
| OCPilot consumer paths | Downstream of Publish (R4) |
| PILOT/SITE credentials | Out of R2 engineering charter |

---

## Outputs

### Required deliverables (engineering)

| Deliverable | Description | Primary consumer |
|-------------|-------------|------------------|
| **EvidencePackage** | Logical model + serialization contract (no normative JSON Schema file) | R5 Validate, R3 Builder, operator inspection |
| **EvidencePackageValidator** | R2-boundary structural/honesty checks | CLI / operator pre-Validate |
| **EvidenceArtifactIndex** | Logical list of acquisition artefacts + optional bulk refs | Validate stage, operator |
| **EvidenceQuarantineLayout** | Path rules + index placement under `evidence/` | Operator external storage |
| **EvidenceStatusModel** | Connector-level `success` \| `partial` \| `failed` + error/warning carriers | R5, acquisition-log mapping (R3) |
| **HandoffContract** | Spec: evidence fields → R3 mapping inputs; R2 prohibitions | R3 Snapshot Builder charter |
| **EvidencePackageGenerator** | Assembles package from connector output + metadata (mock path minimum) | Pipeline Acquire stage |

### External artefacts (when implemented — not git)

| Artefact | Location |
|----------|----------|
| Evidence index (logical record) | `{output_root}/{acquisition_id}/evidence/` |
| Bulk refs | Operator external paths under quarantine |
| Connector status sidecar | Under acquisition session — exact filename **SAFE UNKNOWN** (N-07) |

### Explicit non-outputs

| Output | Owner |
|--------|-------|
| OpenCart section folders | R3 |
| `package_quality_level` ≥ 1 | R3 + R5 |
| Published snapshot reference | R4 |
| Validate report / publish gate checklist | R5 |
| `snapshots/{snapshot_id}/` content from R2 | **Forbidden** — R3 after Validate |

---

## Identity Model

**Contract only** — no JSON Schema. Normative fields per [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) and [R1-CONTRACT-MAPPING-v1.md](R1-CONTRACT-MAPPING-v1.md).

### Core identifiers

| Field | Required | Semantics | Relationship rules |
|-------|----------|-----------|-------------------|
| **`acquisition_id`** | **Yes** | Session correlation key for evidence + snapshots under one acquisition folder | Generated at session start (runtime); **one acquisition folder** per id under `{output_root}/`; may host **multiple** evidence packages only when hybrid merge is chartered (**Future**) |
| **`site_ref`** | **Yes** | Consumer registry site identity | Maps from R1.2 `site_id` at translation boundary; must be stable for all artefacts in session |
| **`connector_class`** | **Yes** | Connector type (e.g. `sftp_readonly`) | Maps from R1.2 `connector`; must match [EAR-CONNECTOR-TYPES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-TYPES-v1.md) |
| **`evidence_id`** | **SAFE UNKNOWN** | **Not** defined in EAR-EVIDENCE-PACKAGE-v1 | Do **not** introduce as package root id without architecture amendment; artifact index entries may use logical `ref` / `leg_ref` (**Future** hybrid) |

### Provenance and time

| Field | Required | Semantics |
|-------|----------|-----------|
| **`channel`** | **Yes** | Acquisition channel label (derived per contract mapping) |
| **`started_at`** | **Yes** | ISO 8601 session start |
| **`completed_at`** | **Yes** when terminal | ISO 8601 session end; required for completed runs |
| **`operator_approval_ref`** | **Yes** | Non-secret HITL / charter / pilot approval pointer |

### Status (evidence stage)

| Field | Required | Semantics |
|-------|----------|-----------|
| **`connector_status`** | **Yes** | `success` \| `partial` \| `failed` — honest acquisition outcome |
| **`errors`** | When applicable | Per connector contract |
| **`warnings`** | When applicable | Per connector contract |

### Scope echo

| Field | Required | Semantics |
|-------|----------|-----------|
| **Approved scope** | **Yes** | Paths/tables operator approved |
| **Attempted scope** | **Yes** | What connector actually tried |
| **Scope delta** | **Optional** | Explicit exclusions/skips for partial runs |

### Binding rules (engineering)

1. **One mock/live connector run** → **one** primary `EvidencePackage` unless hybrid merge is implemented (**Future**).
2. **`acquisition_id`** binds quarantine path and correlates to future `snapshot_id`(s) — **1:N snapshot per acquisition** policy remains **SAFE UNKNOWN**.
3. **`site_ref`** ≠ `snapshot_id` — snapshot identity is created at R3 Store boundary.
4. R1.6 fields `site_id`, `quality_level` on evidence are **deprecated** for R2 — `quality_level` on evidence must **not** imply snapshot quality.
5. Partial acquisition: `connector_status: partial` **must not** imply complete snapshot readiness.

---

## Validation Boundary

### R2 owns (Evidence Package Validator)

| Check class | Examples | Fail behavior |
|-------------|----------|---------------|
| **Identity completeness** | `acquisition_id`, `site_ref`, `connector_class` non-empty | Fail closed |
| **Provenance completeness** | `channel`, `started_at`, `operator_approval_ref` | Fail closed |
| **Scope echo presence** | Approved vs attempted scope recorded | Fail closed |
| **Artifact index** | At least one logical artefact ref (e.g. manifest) | Fail closed |
| **Connector status honesty** | Status enum valid; `failed`/`partial` not masked as success | Fail closed |
| **Errors/warnings shape** | Present when status requires per connector contract | Fail closed |
| **Evidence vs snapshot confusion** | No `snapshot_contract`, no `package_quality_level`, no OpenCart section payloads | Fail closed |
| **Storage policy** | No secret values in git-bound serialization; bulk refs opaque | Fail closed |

### R5 owns (Validation Helpers — not R2)

| Check class | Source |
|-------------|--------|
| Snapshot contract version (`ear-opencart-snapshot-v1`) | EAR-SNAPSHOT-LIFECYCLE-v1 Validate |
| **Quality level possession** (L0–L3 sections) | R5 + operator HITL |
| PII / secrets in **candidate snapshot** | R5, lifecycle Validate |
| **`safe-unknown` honesty** at snapshot publish readiness | R5 |
| **Publish gate** / readiness checklist | R5, EAR-READINESS-GATES |
| Validate report for **Publish allowed** | R5 |

### Overlap avoidance

| Concern | R2 | R5 |
|---------|----|----|
| Partial run visible | `connector_status` + scope echo | Snapshot-level `safe-unknown` + operator downgrade |
| Manifest paths exist | Artifact **ref** in index | `file-manifest/` section adequacy for Level 1+ |
| Operator approval | `operator_approval_ref` on evidence | `operator_approval` in snapshot metadata |
| Quality claims | **Forbidden** on evidence | **Required** at snapshot Validate |

R2 validation **passes** do **not** authorize Publish or imply `package_quality_level` ≥ 1.

---

## Evidence → Snapshot Boundary

### What R2 hands to R3 (HandoffContract inputs)

| Handoff input | Purpose for R3 |
|---------------|----------------|
| Contract-shaped **EvidencePackage** (logical) | Source for section assembly |
| **EvidenceArtifactIndex** | Locate manifest, exports, screenshots (refs) |
| **Scope echo** | Populate acquisition-log scope fields; honest `safe-unknown` |
| **Provenance block** | `acquisition-log` timestamps, channel, mode, approval ref |
| **Connector status + errors/warnings** | Partial run handling; no silent completeness |
| **Quarantine paths** | External bulk reads for manifest expansion — **not** consumer paths |
| **HandoffContract document** | Field-level mapping spec (R2.6 deliverable) |

Per [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md): Validation **transforms** evidence into snapshot sections — R3 implements transformation **after** R5/human Validate gate per backlog.

### What R2 must never do

| Prohibition | Source |
|-------------|--------|
| Write OpenCart section trees (`file-manifest/`, `theme-info/`, …) | R2 Charter non-goals; backlog R3 |
| Set or persist `package_quality_level` ≥ 1 | SC-05; evidence vs snapshot table |
| Write under `snapshots/{snapshot_id}/` | R1.8C sibling layout |
| Publish to consumer bulk | EAR-EVIDENCE-PACKAGE forbidden rule |
| Rename Evidence Package as Snapshot Package | EAR-EVIDENCE-PACKAGE vs snapshot |
| Merge evidence tree into snapshot tree | R1.8C, R2 Quarantine charter |
| Certify publish readiness | R5 + R4 |
| Expose evidence quarantine to consumers | EAR-STORAGE-MODEL consumer role |

### Store interaction (frozen)

| Rule | Detail |
|------|--------|
| R1.8 mock Store | Remains **Level 0** (`package_quality_level: 0`) until R3 validates possession |
| R2 persist scope | **`evidence/` only** — does not change snapshot 3-file mock honesty |
| PC-08 minimum | Evidence **must not** be deleted before Validate pass and successful Store of derived snapshot |

---

## Success Criteria

R2 **engineering program** (this charter) is **complete** when:

| ID | Criterion | Verification |
|----|-----------|--------------|
| ISC-01 | Work breakdown R2.1–R2.7 defined with Required/Optional/Future/SAFE UNKNOWN | This document § Work Breakdown |
| ISC-02 | Inputs traced to R1 artefacts and architecture contracts | § Inputs |
| ISC-03 | Outputs named (`EvidencePackage`, `EvidencePackageValidator`, etc.) | § Outputs |
| ISC-04 | Identity model contract without normative schema | § Identity Model |
| ISC-05 | R2 vs R5 validation boundary explicit | § Validation Boundary |
| ISC-06 | Evidence → Snapshot handoff explicit | § Evidence → Snapshot Boundary |
| ISC-07 | Planning notes N-01–N-07 carried | [R2-DECISION-v1.md](R2-DECISION-v1.md), [R2-IMPLEMENTATION-DECISION-v1.md](R2-IMPLEMENTATION-DECISION-v1.md) |
| ISC-08 | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) and [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) updated | Program navigation |

**R2 implementation acceptance** (post-code — separate milestone):

| ID | Criterion | Source |
|----|-----------|--------|
| IAC-01 | Evidence Package inspectable and traceable to connector run | Backlog § R2 acceptance |
| IAC-02 | Evidence separable from published snapshot tree | Backlog § R2 acceptance |
| IAC-03 | Mock path emits quarantine index under `{acquisition_id}/evidence/` | R1.8C + R2.5 |
| IAC-04 | Mock snapshot Store remains Level 0 honest | N-03 |

---

## Stop Conditions

Stop or escalate **before** R2 code merge if:

| ID | Condition | Action |
|----|-----------|--------|
| IST-01 | Implementation populates OpenCart snapshot sections in R2 | **STOP** — reclassify as R3 |
| IST-02 | Implementation enables live SFTP / SITE-001 / PILOT without authorization | **STOP** |
| IST-03 | Implementation adds Publish or OCPilot intake | **STOP** — R4 / consumer |
| IST-04 | Evidence quarantine under git workspace or consumer paths | **STOP** — EAR-STORAGE-MODEL |
| IST-05 | `package_quality_level` set on evidence or inflated at mock persist | **STOP** |
| IST-06 | No [R2-IMPLEMENTATION-DECISION-v1.md](R2-IMPLEMENTATION-DECISION-v1.md) human approval | **STOP** — per R1 gate pattern (N-06) |
| IST-07 | Persistence/Store redesign beyond `evidence/` index | **STOP** — R1.9 frozen |

---

## Planning notes (carried)

| Note | Action |
|------|--------|
| N-01 | Title work **R2 — Evidence Package Generator** |
| N-02 | File Manifest Expansion → **R3** |
| N-03 | Mock Store **Level 0** until R3 |
| N-04 | Publish / OCPilot → **R4** / consumer |
| N-05 | Live acquisition → Execution Authorization only |
| N-06 | Human gate on [R2-IMPLEMENTATION-DECISION-v1.md](R2-IMPLEMENTATION-DECISION-v1.md) before code |
| N-07 | Exact `evidence/` index filenames → resolve at R2.5 implementation; **SAFE UNKNOWN** until then |

---

## Evidence index

| ID | Source |
|----|--------|
| C-R2I-01 | [R2-CHARTER-v1.md](R2-CHARTER-v1.md) |
| C-R2I-02 | [R2-DECISION-v1.md](R2-DECISION-v1.md) |
| C-R2I-03 | [R2-PLANNING-REVIEW-v1.md](R2-PLANNING-REVIEW-v1.md) |
| C-R2I-04 | [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) |
| C-R2I-05 | [EAR-SNAPSHOT-LIFECYCLE-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-LIFECYCLE-v1.md) |
| C-R2I-06 | [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) |
| C-R2I-07 | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) |
| C-R2I-08 | [R1.6-EVIDENCE-PACKAGE-MODEL-v1.md](R1.6-EVIDENCE-PACKAGE-MODEL-v1.md) |
| C-R2I-09 | [R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md](R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md) |
| C-R2I-10 | [R1-CONTRACT-MAPPING-v1.md](R1-CONTRACT-MAPPING-v1.md) |

---

## Truth statement

| Claim | Accurate? |
|-------|-----------|
| R2 implementation code exists for contract-aligned evidence | **No** — charter only |
| This charter authorizes live SFTP / PILOT | **No** |
| This charter authorizes R3 snapshot sections | **No** |
| Human implementation approval recorded | **Pending** — [R2-IMPLEMENTATION-DECISION-v1.md](R2-IMPLEMENTATION-DECISION-v1.md) |
