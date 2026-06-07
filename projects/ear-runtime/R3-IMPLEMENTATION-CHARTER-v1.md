# R3 — Snapshot Assembly Implementation Charter v1

**Type:** Implementation engineering charter — **no** runtime code, **no** snapshot builder, **no** persistence changes in this document  
**Date:** 2026-06-05  
**Phase:** R3 — Snapshot Assembly Layer  
**Lane:** B — EAR Runtime Engineering  
**Prior gates:** R1 **COMPLETE**; R2 **COMPLETE WITH NOTES**; [R3-CHARTER-v1.md](R3-CHARTER-v1.md) **COMPLETE**; [R3-DECISION-v1.md](R3-DECISION-v1.md) — **APPROVED WITH NOTES**  
**Decision companion:** [R3-IMPLEMENTATION-DECISION-v1.md](R3-IMPLEMENTATION-DECISION-v1.md)  
**Architecture sources:** [shared/external-access-runtime/](../../shared/external-access-runtime/)

---

## Charter identity

| Field | Value |
|-------|-------|
| **Authorizes** | R3 engineering scope, work packages R3.1–R3.7, Snapshot Package Model contract, identity continuity, safe-unknown strategy, R3/R5 validation boundary, implementation sequence — **not** R4 Publish, R5 Validate automation, or live acquisition |
| **Does not authorize** | Snapshot builder code, Store redesign, Validate automation, Publish, OCPilot integration, SITE-001 / PILOT execution, live SFTP, normative JSON Schema files |
| **Human approver** | **Pending** — see [R3-IMPLEMENTATION-DECISION-v1.md](R3-IMPLEMENTATION-DECISION-v1.md) |
| **Program label** | **R3 — Snapshot Assembly** / Snapshot Builder — **not** Validate or Publish |

---

## Mission

### Why R3 engineering exists

R2 closed contract-shaped Evidence Package generation (`--contract-evidence`, in-memory) with authoritative handoff spec [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md). Evidence remains **acquisition-internal** — connector-oriented blobs with logical index, not consumer-shaped OpenCart sections.

R3 engineering translates the approved [R3-CHARTER-v1.md](R3-CHARTER-v1.md) into **executable scope** before coding: Snapshot Package Model, identity continuity, section assembly rules, safe-unknown propagation, candidate generator, and R3/R5 boundary — producing a **candidate OpenCart Snapshot Package** per [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md).

### What Snapshot Assembly builds

**Snapshot Assembly** transforms R2 `EvidencePackage` inputs into a **candidate Snapshot Package** — a governed, inspectable OpenCart section tree. Assembly is **structural population**, not acquisition, not certification, and not publish.

```text
R2 Evidence Package (contract-shaped)
        ↓
R2 structural validation (R2.4 — eligibility gate)
        ↓
R2.6 HANDOFF (read-only consumption)
        ↓
R3 Snapshot Assembly          ← R3 engineering scope
        ↓
R5 Validate + human HITL      ← not R3
        ↓
Store (R1.8 frozen layout)
        ↓
R4 Publish                    ← not R3
```

### Gap R3 engineering closes (evidence-backed)

| Post-R2 state | R3 engineering target |
|---------------|------------------------|
| No OpenCart section tree from evidence | Candidate package matching logical OpenCart structure |
| R1.7 mock `SnapshotPackage` flat, not spec-aligned | Section tree per EAR-OPENCART-SNAPSHOT-SPEC-v1 |
| R1.6 mock chain conflates evidence and snapshot fields | Assembly from `evidence_package_models.EvidencePackage` only |
| Partial acquisition has no snapshot honesty surface | `safe-unknown/` and `acquisition-log/` populated from scope echo and connector status |
| No `snapshot_id` at evidence stage | New snapshot identity at Store boundary |
| Consumers cannot consume raw evidence | Candidate snapshot ready for R5 Validate — **unpublished** |

### Engineering target (backlog)

Per [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R3: **candidate Snapshot Level 1** with honest `safe-unknown` where evidence gaps exist — not Level 2+ completeness or auto-Publish.

---

## Engineering Scope

### In scope (R3 implementation — when human gate approves code)

| ID | Area | Engineering deliverable |
|----|------|-------------------------|
| S-01 | Snapshot Package Model | Logical OpenCart section tree contract; supersedes R1.7 flat model at assembly boundary |
| S-02 | Snapshot Identity Layer | `snapshot_id` creation; `acquisition_id` correlation; field transforms (`site_ref` → `site_id`, etc.) |
| S-03 | Section Assembly Rules | HO-ALLOW-01–HO-ALLOW-10 mapping tables; per-section population logic |
| S-04 | Safe Unknown Propagation | Gap detection; explicit `safe-unknown/` entries from evidence status, scope, artifact index |
| S-05 | HandoffContract module | Field-level evidence → snapshot mapping (deferred from R2.6) |
| S-06 | Candidate Snapshot Generator | Mock-path assembly from R2.7 output; inspectable candidate under Store layout |
| S-07 | Assembly Eligibility | Precondition checks (R2 structural pass required); distinct from R5 Validate pass |
| S-08 | R1.6 deprecation at boundary | R3 authoritative input = R2.1 model; legacy mock chain migration scoped |

### Out of scope (explicit)

| Item | Owner |
|------|-------|
| EAR Validate (snapshot contract certification, quality possession) | **R5** |
| `package_quality_level` ≥ 1 **certification** | **R5** |
| Publish gate approval / consumer reference | **R4** + **R5** |
| Consumer reports / OCPilot Run 5 | Consumer programs |
| Evidence quarantine writes / mutation | **R2** |
| Live acquisition / SFTP execution | Execution Authorization |
| Store / persistence layout redesign | **Frozen** R1.9 |
| Level 2+ full `extension-inventory/` / `ocmod-inventory/` population | Future milestone |
| Normative JSON Schema / ZIP layout files | **SAFE UNKNOWN** |
| OCPilot integration | OCPilot program |
| SITE-001 / PILOT-001 execution | Execution Authorization |

### Code placement (when implementation authorized)

R3 code may extend **only** under:

```text
projects/ear-runtime/runtime/
```

Likely paths (chartered, not prescriptive filenames):

| Path | Role |
|------|------|
| `runtime/shared/snapshot_package_models.py` | OpenCart section tree logical model (extends/supersedes R1.7) |
| `runtime/shared/handoff_contract.py` | Mapping tables — no I/O |
| `runtime/builders/snapshot_assembly_builder.py` | Candidate assembly orchestrator |
| `runtime/builders/section_assemblers/` | Per-section population (metadata, file-manifest, …) |
| `runtime/validators/assembly_eligibility_validator.py` | R3 internal preconditions — **not** R5 Validate |

**Forbidden:** `shared/external-access-runtime/` amendments without Architecture Amendment Charter; evidence quarantine mutation; git-bound snapshot bulk; consumer `project-sites\` paths pre-Publish.

---

## Dependencies

| Predecessor | Requirement |
|-------------|-------------|
| R1 | **COMPLETE** — mock pipeline, connector skeleton, mock Store layout |
| R2 | **COMPLETE WITH NOTES** — R2.1–R2.7; `--contract-evidence` path; R2.6 handoff spec |
| R1.7 | Snapshot model skeleton — **superseded at assembly boundary** by OpenCart spec |
| R1.8B/C | Storage contract and layout — **frozen**; R3 uses `{acquisition_id}/snapshots/{snapshot_id}/` |
| R1.9 | Store hardening — **frozen**; no redesign |
| Architecture | EAR-OPENCART-SNAPSHOT-SPEC-v1, EAR-OPENCART-QUALITY-MAPPING-v1, EAR-SNAPSHOT-CONTRACT-v1, EAR-SNAPSHOT-LIFECYCLE-v1, EAR-STORAGE-MODEL-v1 |

### R2 debt (non-blocking)

| Debt | R3 handling |
|------|-------------|
| Quarantine persist (IAC-03 / D-R2-01) | Mock-first logical refs; schedule R3-adjacent or parallel milestone |
| R1.6 mock path retention | Retain until R3 chain wired — no unsafe deletion (N-R3-04) |
| `HandoffContract` code deferred from R2.6 | **R3.5** deliverable |

---

## Inputs

### Authoritative upstream (R2 → R3)

| Input | Source | R3 use |
|-------|--------|--------|
| **Contract-shaped `EvidencePackage`** | R2.1 / R2.7 `evidence_package_models.py` | Primary transformation source (H-IN-01) |
| **`EvidenceIdentity`** | `identity` block | Folder correlation; metadata `site_id` mapping (H-IN-02) |
| **`EvidenceProvenance`** | `provenance` block | `acquisition-log` timestamps, channel, approval (H-IN-03) |
| **`EvidenceScopeEcho`** | `scope_echo` block | Scope + `safe-unknown` for gaps (H-IN-04) |
| **`EvidenceArtifactIndex`** | `artifact_index` + `artifacts[]` | Section expansion refs (H-IN-05) |
| **`EvidenceStatus`** | `status.connector_status` | Partial-run handling (H-IN-06) |
| **Errors and warnings** | `errors`, `warnings` | `safe-unknown` topics (H-IN-07) |
| **Quarantine path binding** | R2.5 `{output_root}/{acquisition_id}/evidence/` | Bulk reads for expansion — mock: logical refs (H-IN-08) |
| **R2 structural validation eligibility** | R2.4 `EvidencePackageValidator` | Gate: invalid evidence must not proceed (H-IN-09) |
| **HandoffContract spec** | R2.6 + R3.5 code module | Field-level mapping (H-IN-10) |

### Architecture contracts (read-only)

| Contract | Role |
|----------|------|
| [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md) | Normative section targets |
| [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) | Level 0–1 minimums; possession vs assembly |
| [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) | Candidate persist roles; no git bulk |
| [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) | Store layout under `snapshots/{snapshot_id}/` |

### Explicit non-inputs

| Artefact | Reason |
|----------|--------|
| R5 Validate report | Post-assembly |
| Published snapshot reference | R4 downstream |
| R1.6 `evidence_models` at assembly boundary | Deprecated — use R2.1 (N-R2R-02) |
| Live connector credentials | Operator secrets |
| OCPilot consumer paths | Publish handoff only |

---

## Outputs

### Required deliverables (engineering)

| Deliverable | Description | Primary consumer |
|-------------|-------------|------------------|
| **SnapshotPackageModel** | Logical OpenCart section tree contract | R3 builders, R5 Validate |
| **HandoffContract** | Evidence block → section mapping tables | R3 section assemblers |
| **SnapshotIdentityLayer** | `snapshot_id` generation; continuity record | Store layout, R5 audit |
| **SectionAssemblyRules** | HO-ALLOW-01–10 implementations | Per-section builders |
| **SafeUnknownPropagator** | Gap → `safe-unknown/` entry logic | R5 honesty review |
| **CandidateSnapshotGenerator** | Mock-path assembly orchestrator | CLI / operator inspection |
| **AssemblyEligibilityResult** | Precondition pass/fail — **not** Validate pass | Pipeline gate |

### External artefacts (when implemented — not git)

| Artefact | Location |
|----------|----------|
| Candidate section tree | `{output_root}/{acquisition_id}/snapshots/{snapshot_id}/` |
| Snapshot bulk (optional) | External snapshot bulk ref — ≠ evidence quarantine |
| Identity Continuity Record | Sidecar or embedded in `acquisition-log/` — format **SAFE UNKNOWN** |

### Explicit non-outputs

| Output | Owner |
|--------|-------|
| Validated / certified snapshot | **R5** |
| `package_quality_level` ≥ 1 certification | **R5** |
| Publish gate approval | **R5** + **R4** |
| Published snapshot reference | **R4** |
| Consumer reports | Consumer programs |
| Evidence quarantine mutation | **R2** |

---

## Work Breakdown

Authoritative R3 work packages — ordered dependency chain.

### R3.1 — Snapshot Package Model

| Field | Value |
|-------|-------|
| **Purpose** | Define logical OpenCart Snapshot Package structure — section tree, root identity fields, candidate quality default — without normative JSON Schema |
| **Inputs** | EAR-OPENCART-SNAPSHOT-SPEC-v1; EAR-SNAPSHOT-CONTRACT-v1; R1.7 (superseded reference) |
| **Outputs** | `SnapshotPackageModel` contract document + dataclass skeleton spec; section enumeration; Required/Optional/Future classification |
| **Owner** | R3 engineering |
| **Dependencies** | R3 Charter complete; OpenCart spec frozen |

### R3.2 — Snapshot Identity Layer

| Field | Value |
|-------|-------|
| **Purpose** | Implement identity continuity rules: `snapshot_id` creation, `acquisition_id` correlation, field transforms, drift prevention (ID-R3-01–ID-R3-05) |
| **Inputs** | R2.6 § Identity continuity; R1-CONTRACT-MAPPING-v1; R2.1 `EvidenceIdentity` |
| **Outputs** | Identity mapping contract; `snapshot_id` generation rules (mock algorithm); Identity Continuity Record spec |
| **Owner** | R3 engineering |
| **Dependencies** | R3.1 |

### R3.3 — Section Assembly Rules

| Field | Value |
|-------|-------|
| **Purpose** | Define per-section population rules from evidence blocks — HO-ALLOW-01–HO-ALLOW-10; L1 target sections with honest gap fallback |
| **Inputs** | R2.6 § Allowed transformations; EAR-OPENCART-SNAPSHOT-SPEC-v1 per-section specs; R2 artifact index taxonomy |
| **Outputs** | Section assembly rule tables; per-section input/output mapping; L1 vs L0 fallback matrix |
| **Owner** | R3 engineering |
| **Dependencies** | R3.1, R3.2, HandoffContract inputs from R2.6 |

### R3.4 — Safe Unknown Propagation

| Field | Value |
|-------|-------|
| **Purpose** | Define gap detection and `safe-unknown/` entry strategy — from connector status, scope echo, artifact status, missing sections — without inventing content or inflating quality |
| **Inputs** | R2.6 HO-ALLOW-03/04/08/09; EAR-OPENCART-SNAPSHOT-SPEC-v1 § safe-unknown; R2 `EvidenceStatus`, `EvidenceScopeEcho` |
| **Outputs** | Safe-unknown topic taxonomy; propagation rules; entry shape contract (topic, reason, impact, unblock hint) |
| **Owner** | R3 engineering |
| **Dependencies** | R3.1, R3.3 |

### R3.5 — HandoffContract + Candidate Snapshot Generator

| Field | Value |
|-------|-------|
| **Purpose** | Implement `HandoffContract` mapping module (deferred R2.6) and mock-path `CandidateSnapshotGenerator` orchestrating section assembly + Store-bound candidate output |
| **Inputs** | R2.7 `EvidencePackage` output; R3.1–R3.4 contracts; R1.8B Store layout |
| **Outputs** | `handoff_contract.py`; `snapshot_assembly_builder.py`; CLI flag spec (e.g. `--contract-snapshot`); candidate under `snapshots/{snapshot_id}/` |
| **Owner** | R3 engineering |
| **Dependencies** | R3.1–R3.4; R2.7 generator; R2.4 validator eligibility |

### R3.6 — Snapshot Validation Boundary Review

| Field | Value |
|-------|-------|
| **Purpose** | Document R3 internal assembly checks vs R5 Validate ownership — prevent overlap; define `AssemblyEligibilityValidator` scope |
| **Inputs** | R2.4 validation boundary pattern; R3 Charter § R3→R5 boundary; EAR-OPENCART-QUALITY-MAPPING-v1 |
| **Outputs** | R3/R5 boundary matrix; assembly eligibility check list; terminology disambiguation (R2 structural vs R5 EAR Validate) |
| **Owner** | R3 engineering |
| **Dependencies** | R3.1–R3.5 design complete |

### R3.7 — R3 Readiness Review

| Field | Value |
|-------|-------|
| **Purpose** | Close R3 implementation phase; verify IAC-R3-01–IAC-R3-06; authorize R5 charter entry or document debt |
| **Inputs** | All R3.1–R3.6 deliverables; mock-path candidate inspection |
| **Outputs** | R3-READINESS-REVIEW-v1; R3-READINESS-DECISION-v1; updated EAR-RUNTIME-STATE |
| **Owner** | R3 engineering + human gate |
| **Dependencies** | R3.5 implementation complete (mock path) |

### Work package classification summary

| Package | Classification |
|---------|----------------|
| R3.1 Snapshot Package Model | **Required** |
| R3.2 Snapshot Identity Layer | **Required** |
| R3.3 Section Assembly Rules | **Required** |
| R3.4 Safe Unknown Propagation | **Required** |
| R3.5 HandoffContract + Candidate Generator | **Required** |
| R3.6 Validation Boundary Review | **Required** |
| R3.7 R3 Readiness Review | **Required** |
| Quarantine persist (bulk on disk) | **Optional** / R3-adjacent — mock logical refs minimum |
| R1.6 path removal | **Future** — after R3 chain wired |
| Level 2+ section population | **Future** |
| Production `snapshot_id` algorithm | **SAFE UNKNOWN** — mock at implementation |
| Physical encoding (folder vs ZIP) | **SAFE UNKNOWN** — R1.8B logical tree normative |
| `HandoffRecord` sidecar format | **SAFE UNKNOWN** |
| 1:N `acquisition_id` → `snapshot_id` merge policy | **SAFE UNKNOWN** |

---

## Snapshot Package Model

Normative source: [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md). **Contract classification only** — no spec redesign, no schema generation.

### Logical package structure

```text
Snapshot/
├── metadata/
├── file-manifest/
├── theme-info/
├── extension-inventory/
├── ocmod-inventory/
├── database-metadata/
├── seo-structure/
├── environment/
├── safe-unknown/
└── acquisition-log/
```

### Package identity (root / metadata)

| Component | Classification | R3 role |
|-----------|----------------|---------|
| `snapshot_id` | **Required** | **Created by R3** at Store boundary |
| `snapshot_contract` (`ear-opencart-snapshot-v1`) | **Required** | Set on candidate assembly |
| `parent_contract` (`ear-snapshot-v1`) | **Required** | Set on candidate assembly |
| `site_id` (from `site_ref`) | **Required** | Identity continuity transform |
| `created_at` | **Required** | Assembly timestamp |
| `ear_mode` | **Required** | From config echo / provenance |
| `operator_approval` (from `operator_approval_ref`) | **Required** | Identity continuity transform |
| `package_quality_level` (candidate) | **Required** | **Level 0 honest default** — R3 must not inflate; R5 certifies possession |
| `bulk_root` (snapshot) | **Optional** | External snapshot bulk ref — ≠ evidence quarantine |
| Prior snapshot reference | **Optional** | Partial reruns (`p1`, `p2`) |
| Publish metadata (`published_at`, etc.) | **Future** / **R4** | Not at assembly |

### Section classification

| Section | Classification | L0 | L1 (R3 target) | R3 assembly role |
|---------|----------------|----|----------------|------------------|
| **`metadata/`** | **Required** | Min identity set | + version claims, baseline refs | HO-ALLOW-02 |
| **`file-manifest/`** | **Required** (L1+) / **safe-unknown** (L0) | Listed in safe-unknown if absent | Root folders, path subset, version proof files | HO-ALLOW-05 |
| **`theme-info/`** | **Required** (L1+) or **safe-unknown** | — | Active theme name or gap | HO-ALLOW-06 |
| **`extension-inventory/`** | **Optional** (L2+) | safe-unknown at L0–L1 | Placeholder safe-unknown at L1 — not populated | Future L2 |
| **`ocmod-inventory/`** | **Optional** (L2+) | safe-unknown at L0–L1 | Placeholder safe-unknown at L1 — not populated | Future L2 |
| **`database-metadata/`** | **Required** (L1+) or **safe-unknown** | — | Prefix + table list or gap | HO-ALLOW-06 |
| **`seo-structure/`** | **Required** (L1+) or **safe-unknown** | — | SEO flags or gap | HO-ALLOW-06 |
| **`environment/`** | **Required** | Always | `environment_class` or `UNKNOWN` | HO-ALLOW-07 |
| **`safe-unknown/`** | **Required** | Always | Residual + section-level gaps | HO-ALLOW-03/04/08/09 |
| **`acquisition-log/`** | **Required** | Min approval + mode | Scope, channel, timestamps | HO-ALLOW-01 |

### Classification summary

| Classification | Elements |
|----------------|----------|
| **Required (always on candidate)** | `metadata/` (min set), `environment/`, `safe-unknown/`, `acquisition-log/`, `snapshot_id`, contract ids |
| **Required (L1 target — or explicit safe-unknown)** | `file-manifest/`, `database-metadata/`, `seo-structure/`, `theme-info/` |
| **Optional** | `bulk_root`, prior snapshot ref, inline vs external manifest form, extended metadata claims |
| **Future (not R3 L1 target)** | L2+ full `extension-inventory/`, `ocmod-inventory/`; comprehensive L3 manifest; publish metadata; normative schema files |

### Required structures (conceptual — no implementation)

| Structure | Sections | Minimum fields (conceptual) |
|-----------|----------|----------------------------|
| **Root identity** | `metadata/` | `snapshot_id`, `snapshot_contract`, `parent_contract`, `site_id`, `created_at`, `ear_mode`, `operator_approval`, `package_quality_level: 0` |
| **Environment block** | `environment/` | `environment_class` (enum or `UNKNOWN`), optional `operator_assertion` |
| **Honesty block** | `safe-unknown/` | List of `{topic, reason, impact, unblock_hint?}` |
| **Audit block** | `acquisition-log/` | `approved_by`, `approved_at`, `ear_mode`, `channel`, `scope` |
| **Manifest block** | `file-manifest/` | Root folders, path list subset, or safe-unknown ref |
| **DB block** | `database-metadata/` | Prefix, table list, or safe-unknown ref |
| **SEO block** | `seo-structure/` | SEO enabled flag, or safe-unknown ref |
| **Theme block** | `theme-info/` | Active theme name, or safe-unknown ref |

---

## Identity Continuity Implementation

Authoritative chain from [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) § Identity continuity.

### Traceability map

```text
R1.2 Config
│  site_id ──────────────────────────────┐
│  connector ────────────────────────────┤
│  output_root, scope, ear_mode          │
└────────────────────────────────────────┘
                    │
                    ▼  Runtime session start
            acquisition_id  ← binds {acquisition_id}/ folder
                    │
                    ▼  R2 Evidence Package
        EvidenceIdentity { acquisition_id, site_ref, connector_class }
        + provenance, scope_echo, artifact_index, status
                    │
                    ▼  R2.6 HANDOFF (read-only)
                    │
                    ▼  R3 Snapshot Assembly
        snapshot_id  ← NEW at Store boundary
        site_id ← site_ref; metadata; package_quality_level (candidate L0)
                    │
                    ▼  R1.8 Store (frozen layout)
        {output_root}/{acquisition_id}/snapshots/{snapshot_id}/
```

### Field mapping

| Evidence (R2) | Snapshot (R3) | Rule |
|---------------|---------------|------|
| `acquisition_id` | Folder correlation; `acquisition-log` reference | **Survives** — same value; binds acquisition tree |
| `site_ref` | `site_id` in metadata | **Transforms** — rename per OpenCart contract |
| `connector_class` | `acquisition-log` channel provenance; metadata context | **Survives** — may combine with `channel` |
| `channel` | `acquisition-log` | **Survives** |
| `started_at`, `completed_at` | `acquisition-log`; metadata acquisition date | **Survives** |
| `operator_approval_ref` | `operator_approval`; `acquisition-log.approved_by` | **Transforms** — field rename |
| Approved / attempted scope | `acquisition-log` scope; `safe-unknown/` | **Transforms** — gaps explicit |
| `connector_status` | Informs `safe-unknown/` — not copied as root enum | **Honesty carrier** |
| Artifact index refs | Section content via expansion | **Transforms** — refs → section payloads |
| — | `snapshot_id` | **Created by R3** |
| — | `snapshot_contract`, `parent_contract` | **Created by R3** |
| — | `package_quality_level` (candidate) | **Created by R3** — L0 default; R5 certifies |
| — | `bulk_root` (snapshot) | **Created by R3** — must not alias evidence quarantine |

### What survives unchanged

- `acquisition_id` (immutable after evidence construction — ID-DRIFT-03)
- `connector_class`, `channel`, timestamps (semantic carry)
- Session folder binding under `{output_root}/{acquisition_id}/`

### What transforms

- `site_ref` → `site_id`
- `operator_approval_ref` → `operator_approval`
- Logical artifact refs → OpenCart section trees
- Scope echo → acquisition-log scope + safe-unknown entries
- Connector status/errors → safe-unknown topics

### What R3 creates (new identifiers)

| Identifier | Appears at | Must not appear on |
|------------|------------|-------------------|
| `snapshot_id` | R3 Store boundary | Evidence identity block |
| `snapshot_contract` / version fields | R3 candidate package | Evidence Package |
| `package_quality_level` (candidate) | R3 assembly | Evidence Package — R5 certifies |
| Snapshot `bulk_root` | Snapshot metadata | Evidence quarantine path |

### Identity drift prevention

| ID | Rule |
|----|------|
| ID-R3-01 | Do **not** store `snapshot_id` in evidence identity block |
| ID-R3-02 | Do **not** alias evidence quarantine as snapshot `bulk_root` |
| ID-R3-03 | `acquisition_id` **immutable** — R3 reads, does not mutate evidence |
| ID-R3-04 | 1:N `acquisition_id` → `snapshot_id` — **SAFE UNKNOWN**; each cycle gets new `snapshot_id` |
| ID-R3-05 | R3 assembly consumes R2.1 model — not R1.6 `evidence_models` at boundary |

---

## Safe Unknown Strategy

### Principle

Missing or unverified data **must** be explicit in `safe-unknown/`. Empty sections elsewhere **without** a corresponding safe-unknown entry is a contract violation ([EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md)).

R3 **must not** invent content, inflate quality, or hide missing data.

### Propagation pipeline

```text
Evidence gap sources                    R3 assembly                    Snapshot output
─────────────────────                   ───────────                    ───────────────
connector_status: partial/failed   →    detect incomplete scope   →    safe-unknown topic
scope_echo delta (attempted ≠ approved) → scope gap rule          →    safe-unknown + acquisition-log
artifact status: unknown/missing   →    HO-ALLOW-09               →    per-topic safe-unknown
missing manifest ref               →    HO-ALLOW-08               →    file-manifest safe-unknown
empty L1 section after expansion   →    HO-ALLOW-08               →    section-level safe-unknown
connector errors/warnings          →    HO-ALLOW-04               →    safe-unknown topics
environment not declared           →    HO-ALLOW-07 fallback      →    environment_class: UNKNOWN
```

### Gap source → safe-unknown mapping

| Evidence source | Safe-unknown topic (illustrative) | Rule ID |
|-----------------|-----------------------------------|---------|
| `connector_status: failed` | `acquisition_outcome` | HO-ALLOW-04 |
| `connector_status: partial` | `partial_acquisition` + per-section topics | HO-ALLOW-04 |
| Scope echo: path excluded | `file-manifest` or scoped topic | HO-ALLOW-03 |
| No DB artifact in index | `database-metadata` | HO-ALLOW-08 |
| No manifest artifact / empty expansion | `file-manifest` | HO-ALLOW-08 |
| Artifact `status: missing` | Per-artifact topic | HO-ALLOW-09 |
| No theme signal in artifacts | `theme-info` | HO-ALLOW-08 |
| No SEO/config signal | `seo-structure` | HO-ALLOW-08 |
| L2 sections not targeted (R3 L1) | `extension-inventory`, `ocmod-inventory` | Charter L1 target — placeholder honesty |

### Entry shape (conceptual)

Each `safe-unknown/` entry supports:

| Field | Required | Purpose |
|-------|----------|---------|
| `topic` | Yes | Section or concern identifier |
| `reason` | Yes | Why data is missing or unverified |
| `impact` | Yes | What consumer phases are blocked |
| `unblock_hint` | Optional | Procedure id — not implementation |

### Prohibitions

| ID | Prohibition |
|----|-------------|
| SU-FORBID-01 | Silent omission when section empty due to partial/failed evidence (HO-FORBID-10) |
| SU-FORBID-02 | Fabricating section content to avoid safe-unknown entry |
| SU-FORBID-03 | Treating `connector_status: success` as section completeness (HO-INV-09) |
| SU-FORBID-04 | Setting `package_quality_level` ≥ 1 to mask gaps (HO-FORBID-06) |
| SU-FORBID-05 | Copying secrets into safe-unknown entries |

### Candidate quality default

R3 sets `package_quality_level: 0` on candidate assembly. L1 **section targets** are populated where evidence permits; gaps become safe-unknown entries — **not** a Level 1 quality claim until R5 certifies possession ([EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md)).

---

## Validation Boundary

**Terminology:** **R2 structural validation** = evidence shape eligibility. **R5 EAR Validate** = snapshot contract certification + quality possession. R3 **assembly eligibility** = preconditions for assembly — distinct from both.

### R3 may verify internally (Assembly Eligibility)

| Check class | Examples | Fail behavior |
|-------------|----------|---------------|
| **R2 structural pass required** | `EvidencePackageValidator` eligibility flag present and pass | Fail closed — no assembly |
| **Handoff input completeness** | H-IN-01–H-IN-08 consumable | Fail closed |
| **Identity continuity** | `acquisition_id`, `site_ref` present; no `snapshot_id` on evidence | Fail closed |
| **Section tree skeleton** | Required sections present (may contain safe-unknown only) | Fail closed on missing required section **folder/logical block** |
| **No evidence mutation** | Read-only consumption verified | Fail closed |
| **Candidate quality default** | `package_quality_level: 0` on output | Fail closed if inflated |
| **Safe-unknown when gaps** | Partial/failed evidence produces entries | Fail closed if suppressed |
| **No quarantine alias** | Snapshot `bulk_root` ≠ evidence quarantine path | Fail closed |

### R5 owns exclusively (EAR Validate — not R3)

| Check class | Source |
|-------------|--------|
| Snapshot contract version compliance | EAR-SNAPSHOT-LIFECYCLE-v1 Validate |
| **Quality level possession** (L0–L3 sections adequate) | EAR-OPENCART-QUALITY-MAPPING-v1 |
| PII / secrets in candidate snapshot | R5 redaction enforcement |
| **`safe-unknown` publish readiness** review | R5 + operator HITL |
| **Publish gate** / readiness checklist | R5, EAR-READINESS-GATES |
| Validate report for **Publish allowed** | R5 |
| Baseline diff adequacy for consumer phases | R5 + consumer rules |

### Overlap prevention matrix

| Concern | R2 structural | R3 assembly | R5 Validate |
|---------|---------------|-------------|-------------|
| Evidence shape valid | **Owns** | Requires pass | Reads chain |
| OpenCart sections populated | — | **Owns** | Certifies adequacy |
| Partial run visible | `connector_status` | `safe-unknown/` population | Publish readiness review |
| Manifest paths exist | Artifact ref in index | `file-manifest/` expansion | Level 1+ possession |
| Quality claims | **Forbidden** | Candidate L0 only | **Owns** certification |
| Publish authorization | — | **Forbidden** | **Owns** gate input |

### Ordering

Canonical pipeline:

```text
R2 Evidence → R3 Candidate Assembly → R5 Validate → Store → R4 Publish
```

Architecture allows R5 parallel with R3 after R2 shape stable — handoff inputs identical; R3 **writes** candidate; R5 **certifies** it. R3 assembly pass ≠ R5 Validate pass (HO-INV-06). R2 structural pass ≠ R5 Validate pass (VAL-INV-01).

---

## Implementation Sequence

Order minimizes rework — contracts before builders, identity before sections, safe-unknown integrated with assembly rules.

```text
Phase A — Models & contracts (no I/O)
  R3.1 Snapshot Package Model
       ↓
  R3.2 Snapshot Identity Layer
       ↓
  R3.6 Validation Boundary Review (design — can draft parallel with A)

Phase B — Assembly rules
  R3.3 Section Assembly Rules
       ↓
  R3.4 Safe Unknown Propagation

Phase C — Integration
  R3.5 HandoffContract module
       ↓
  R3.5 Candidate Snapshot Generator (mock path)
       ↓
  CLI wiring (`--contract-snapshot` or equivalent)

Phase D — Closure
  R3.7 R3 Readiness Review
```

### Dependency rationale

| Step | Why first |
|------|-----------|
| **R3.1** | Section tree and classification anchor all downstream work |
| **R3.2** | `snapshot_id` and transforms required before metadata/acquisition-log assembly |
| **R3.3** | Per-section rules depend on model + identity field names |
| **R3.4** | Safe-unknown rules cross-cut sections — after section rules defined |
| **R3.5 HandoffContract** | Pure mapping module — no I/O; testable in isolation |
| **R3.5 Generator** | Orchestrates all above; depends on R2.7 output + R2.4 gate |
| **R3.6** | Boundary doc prevents Validate creep during R3.5 implementation |
| **R3.7** | Gates R5 charter entry |

### Parallel work (allowed with risk acceptance)

| Parallel track | Notes |
|----------------|-------|
| R3.6 boundary doc during R3.1–R3.4 | Recommended — prevents rework |
| R5 charter drafting during R3 | Architecture allows; R5 must reference HO-INV-06 |
| Quarantine persist (R2 debt) | R3-adjacent — mock logical refs unblock R3.5 |

### What remains for R4 and R5

| Phase | Scope |
|-------|-------|
| **R5** | Snapshot contract Validate; quality possession; redaction; publish readiness gate; Validate report |
| **R4** | Publish execution; consumer-visible snapshot promotion; HITL publish approval |
| **Future** | L2+ section population; live acquisition; hybrid multi-package; production snapshot_id algorithm |

---

## Success Criteria

R3 **engineering program** (this charter) is **complete** when:

| ID | Criterion | Verification |
|----|-----------|--------------|
| ISC-R3-01 | Mission and gap matrix documented | § Mission |
| ISC-R3-02 | Work packages R3.1–R3.7 defined with purpose, inputs, outputs, owner, dependencies | § Work Breakdown |
| ISC-R3-03 | Snapshot Package Model classified Required/Optional/Future without spec redesign | § Snapshot Package Model |
| ISC-R3-04 | Identity continuity: survives, transforms, created fields | § Identity Continuity |
| ISC-R3-05 | Safe-unknown strategy documented | § Safe Unknown Strategy |
| ISC-R3-06 | R3/R5 validation boundary explicit | § Validation Boundary |
| ISC-R3-07 | Implementation sequence with dependency rationale | § Implementation Sequence |
| ISC-R3-08 | R3 notes N-R3-01–N-R3-10 carried | § Planning notes |
| ISC-R3-09 | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) and [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) updated | Program navigation |
| ISC-R3-10 | [R3-IMPLEMENTATION-DECISION-v1.md](R3-IMPLEMENTATION-DECISION-v1.md) recorded | Human gate |

**R3 implementation acceptance** (post-code — R3.7):

| ID | Criterion | Source |
|----|-----------|--------|
| IAC-R3-01 | Candidate snapshot inspectable under Store layout | Backlog § R3 |
| IAC-R3-02 | Section tree complete for L1 target or honest `safe-unknown` | EAR-OPENCART-SNAPSHOT-SPEC-v1 |
| IAC-R3-03 | Identity continuity preserved (`acquisition_id`, `site_id`) | R2.6 |
| IAC-R3-04 | `safe-unknown` propagated from partial/failed evidence | HO-ALLOW-03/04 |
| IAC-R3-05 | Ready for R5 Validate — **not** Publish | R3→R5 boundary |
| IAC-R3-06 | Assembly from `evidence_package_models.EvidencePackage` | N-R2R-02 |

---

## Stop Conditions

Stop or escalate **before** R3 code merge if:

| ID | Condition | Action |
|----|-----------|--------|
| IST-R3-01 | Implementation includes R5 Validate automation as R3 deliverable | **STOP** — reclassify as R5 |
| IST-R3-02 | Implementation includes Publish or consumer output | **STOP** — R4 / consumer |
| IST-R3-03 | Candidate marked publish-ready without R5 | **STOP** — HO-INV-07 |
| IST-R3-04 | `package_quality_level` ≥ 1 set as assembly default | **STOP** — quality inflation |
| IST-R3-05 | Evidence quarantine merged into snapshot tree | **STOP** — HO-FORBID-03 |
| IST-R3-06 | Store / persistence redesign attempted | **STOP** — R1.9 frozen |
| IST-R3-07 | Live SFTP / SITE-001 / PILOT without Execution Authorization | **STOP** |
| IST-R3-08 | No [R3-IMPLEMENTATION-DECISION-v1.md](R3-IMPLEMENTATION-DECISION-v1.md) human approval | **STOP** — per R1/R2 gate pattern |
| IST-R3-09 | R1.6 path deleted before R3 chain wired | **STOP** — N-R3-04 |
| IST-R3-10 | Snapshot bulk under git workspace | **STOP** — EAR-STORAGE-MODEL |

---

## Planning notes (carried)

| Note | Action |
|------|--------|
| N-R3-01 | Title work **R3 — Snapshot Assembly** — not Validate or Publish |
| N-R3-02 | First implementation consumes `evidence_package_models.EvidencePackage` — deprecate R1.6 at boundary |
| N-R3-03 | Candidate `package_quality_level: 0` default until R5 certifies |
| N-R3-04 | Retain `--contract-evidence` and R1.6 mock paths until R3 chain wired |
| N-R3-05 | Quarantine persist (D-R2-01) — schedule R3-adjacent milestone |
| N-R3-06 | Implement `HandoffContract` code module — R3.5 |
| N-R3-07 | Disambiguate R2 structural vs R5 EAR Validate in all R3 docs |
| N-R3-08 | Per-section field mapping — resolved in R3.3 (was SAFE UNKNOWN at R3 Charter) |
| N-R3-09 | Live acquisition, SFTP, SITE-001 — Execution Authorization only |
| N-R3-10 | Human implementation approval gate — this charter does not bypass R1/R2 pattern |

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| R3 label confusion — engineers implement Validate or Publish as R3 | High | Mission + Non-Goals; § Validation Boundary |
| Quality inflation at assembly | High | Candidate L0 default; R5 owns certification |
| R1.6 mock chain bypasses R2 handoff | Medium | N-R3-02; R3.5 consumes R2.7 only |
| Evidence/snapshot tree merge | High | ID-R3-02; HO-FORBID-03 |
| No quarantine on disk — section expansion lacks bulk | Low (mock) | Mock logical refs; N-R3-05 debt tracked |
| Validate terminology collision | Medium | N-R3-07; § Validation Boundary |
| R5 vs R3 ordering ambiguity | Low | § Implementation Sequence; parallel allowed |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Physical encoding (folder vs ZIP) for candidate persist | R1.8B SAFE UNKNOWN — logical tree normative |
| Official JSON Schema for snapshot package | Not in repo |
| 1:N `acquisition_id` → `snapshot_id` merge policy | Architecture SAFE UNKNOWN |
| Hybrid multi-package assembly | Future R2.8 |
| `HandoffRecord` sidecar serialization format | Not in repo |
| Whether R3 reads evidence from memory vs quarantine index only | Implementation choice at R3.5 |
| Production `snapshot_id` generation algorithm | Mock at R3.2; live **SAFE UNKNOWN** |
| Quarantine persist timing relative to R3 | R2 debt — mock refs unblock R3.5 |
| Exact CLI flag name for contract snapshot path | Resolve at R3.5 implementation |
| Identity Continuity Record physical encoding | Resolve at R3.2/R3.5 |

---

## Evidence index

| ID | Source |
|----|--------|
| C-R3I-01 | [R3-CHARTER-v1.md](R3-CHARTER-v1.md) |
| C-R3I-02 | [R3-DECISION-v1.md](R3-DECISION-v1.md) |
| C-R3I-03 | [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) |
| C-R3I-04 | [R2-READINESS-DECISION-v1.md](R2-READINESS-DECISION-v1.md) |
| C-R3I-05 | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md) |
| C-R3I-06 | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| C-R3I-07 | [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) |
| C-R3I-08 | [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) |
| C-R3I-09 | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R3 |
| C-R3I-10 | [R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md](R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md) |

---

## Truth statement

| Claim | Accurate? |
|-------|-----------|
| R3 snapshot builder code exists | **No** — charter only |
| This charter authorizes live SFTP / PILOT | **No** |
| This charter authorizes R5 Validate or R4 Publish | **No** |
| Human implementation approval recorded | **Pending** — [R3-IMPLEMENTATION-DECISION-v1.md](R3-IMPLEMENTATION-DECISION-v1.md) |
