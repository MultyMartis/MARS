# R3 Charter v1

**Type:** Program charter — **no** runtime code, **no** implementation, **no** persistence changes in this phase  
**Phase:** R3 — Snapshot Assembly Layer  
**Date:** 2026-06-05  
**Lane:** B — EAR Runtime Architecture  
**Prior phases:** R1 **COMPLETE**; R2 **COMPLETE WITH NOTES**; [R2-READINESS-REVIEW-v1.md](R2-READINESS-REVIEW-v1.md); [R2-READINESS-DECISION-v1.md](R2-READINESS-DECISION-v1.md) — **READY FOR R3 WITH NOTES**  
**Decision companion:** [R3-DECISION-v1.md](R3-DECISION-v1.md)  
**Architecture sources:** [shared/external-access-runtime/](../../shared/external-access-runtime/)

---

## Purpose

Formally charter **R3 — Snapshot Assembly Layer** before any R3 engineering work begins. R3 closes the gap between R2 contract-shaped Evidence Package and the OpenCart Snapshot Package defined in [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md), and establishes the authoritative contract between:

```text
R2 Evidence Package
        ↓
R3 Snapshot Assembly
        ↓
R5 Validate
        ↓
R4 Publish
```

**R3 delivers:** mission, scope, non-goals, Snapshot Package contract, identity continuity, ownership boundaries, R3→R5 boundary, success criteria, stop conditions — **charter only**.

**R3 does not deliver:** snapshot builder implementation, OpenCart section writers, Store persist changes, Validate automation, Publish, or consumer integration.

---

## Mission

### What is Snapshot Assembly?

**Snapshot Assembly** is the EAR runtime layer that **transforms** contract-shaped Evidence Package inputs (R2) into a **candidate OpenCart Snapshot Package** — a governed, inspectable section tree per [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md). Assembly is **structural population**, not acquisition, not certification, and not publish.

Per [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md): Validation **transforms** evidence into snapshot sections; R3 implements that transformation as **candidate** output. R3 is the **first layer authorized to create** Snapshot Package artefacts — but **not in this charter phase**.

### What problem does R3 solve?

| Problem (post-R2 state) | R3 target |
|-------------------------|-----------|
| Evidence is acquisition-internal — not consumer-shaped | OpenCart section tree (`metadata/`, `file-manifest/`, …) |
| R1.7 mock `SnapshotPackage` is flat, not spec-aligned | Candidate package matching OpenCart logical structure |
| R1.6 mock chain conflates evidence and snapshot fields | Assembly from `evidence_package_models.EvidencePackage` only |
| Partial acquisition has no snapshot honesty surface | `safe-unknown/` and `acquisition-log/` populated from scope echo and connector status |
| No `snapshot_id` at evidence stage | New snapshot identity at Store boundary |
| Consumers cannot consume raw evidence | Candidate snapshot ready for R5 Validate — still **unpublished** |

Without R3, EAR cannot produce the interface OCPilot and other consumers require; evidence would remain connector-oriented blobs with no governed OpenCart contract.

### Why can Evidence not be published directly?

| Reason | Authority |
|--------|-----------|
| **Audience mismatch** — evidence is for EAR Validation + operator; consumers require snapshot contract | EAR-EVIDENCE-PACKAGE-v1 |
| **Shape mismatch** — connector index ≠ OpenCart section tree | EAR-OPENCART-SNAPSHOT-SPEC-v1 |
| **Quality uncertified** — evidence carries `connector_status`, not `package_quality_level` | R2-CHARTER forbidden rules |
| **Secrets risk** — pre-redaction bulk may exist in quarantine | EAR-EVIDENCE-PACKAGE-v1; EAR-STORAGE-MODEL-v1 |
| **Lifecycle rule** — Acquire → **Validate** → Store → Publish; evidence is pre-contract | EAR-SNAPSHOT-LIFECYCLE-v1 |
| **Storage separation** — `{acquisition_id}/evidence/` ≠ `{acquisition_id}/snapshots/{snapshot_id}/` | R1.8C; R2.5 |

Evidence **must not** be renamed, merged, or published as Snapshot Package ([R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) HO-FORBID-04).

### Why does Snapshot exist?

Snapshot Package is the **stable, consumer-facing evidence interface** — metadata over bulk, explicit gaps, quality levels, and audit trail — without requiring live hosting access, credentials, or raw connector artefacts. It enables:

- Baseline diff and structural audit (OCPilot Run 5 model)
- Honest partial-run handling via `safe-unknown/`
- Immutable point-in-time reference after Store and Publish
- Separation of acquisition risk (quarantine) from consumer intake (published snapshot)

### Why is R3 separate from R2 and R5?

| Layer | Owns | Does not own |
|-------|------|--------------|
| **R2** | Evidence shape, identity binding, artifact index, quarantine layout, structural evidence validation, handoff inputs | OpenCart sections, `snapshot_id`, `package_quality_level` certification |
| **R3** | Candidate snapshot section assembly, identity continuity (`acquisition_id` → `snapshot_id`), `safe-unknown` propagation, Store-bound candidate generation | Evidence acquisition, quality certification, publish gates, consumer outputs |
| **R5** | Snapshot contract validation, quality level possession, publish readiness, redaction enforcement on candidate | Evidence structural checks (R2), section population (R3), Publish execution (R4) |

**Separation rationale:**

1. **R2 → R3:** Evidence is frozen at handoff; R3 **reads** evidence and **writes** snapshot sections — distinct ownership ([R2.6](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) HO-INV-12).
2. **R3 → R5:** R3 produces **candidate** snapshot; R5 **certifies** contract compliance and quality — assembly pass ≠ Validate pass ([R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md) VAL-INV-01).
3. **R5 → R4:** Validate approval ≠ Publish; R4 promotes stored snapshot to consumer reference only after HITL.

R3 is the **transformation layer** between acquisition-internal evidence and validation-gated consumer contract.

---

## Scope

### In scope (R3 program — charter defines; implementation follows R3 Implementation Charter)

| # | Work area | Boundary |
|---|-----------|----------|
| 1 | **EvidencePackage consumption** | Consume R2.1 `EvidencePackage` per R2.6 handoff inputs H-IN-01–H-IN-10; R2 structural eligibility required |
| 2 | **SnapshotPackage creation** | Candidate OpenCart Snapshot Package — logical section tree; **unpublished** |
| 3 | **OpenCart section assembly** | Populate sections per [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md) — transformations HO-ALLOW-01–HO-ALLOW-10 |
| 4 | **`safe-unknown` propagation** | Explicit gaps from scope echo, connector status, partial runs, missing artifacts — never silent omission |
| 5 | **Identity continuity** | `acquisition_id` → `snapshot_id`; `site_ref` → `site_id`; `connector_class` → metadata/acquisition-log |
| 6 | **Candidate snapshot generation** | Inspectable candidate workspace under `{output_root}/{acquisition_id}/snapshots/{snapshot_id}/` per R1.8 layout |
| 7 | **Snapshot storage model inputs** | Align candidate output with [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) and [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) — **no Store redesign** |
| 8 | **HandoffContract implementation charter** | Field-level mapping from evidence blocks to snapshot sections (R2.6 deferred code) |
| 9 | **R1.6 deprecation at snapshot boundary** | R3 assembly authoritative input = R2 model; legacy mock chain migration scoped in Implementation Charter |

### Allowed artifact types (charter phase)

| Artifact | R3 role |
|----------|---------|
| Charter documents (`R3-*`) | This phase |
| Snapshot assembly / builder **design** in Implementation Charter | Next gate |
| Mock-path candidate assembly | Consistent with R1 mock-only until pilot chartered |
| Section mapping tables (logical) | Per OpenCart spec — no normative schema files |

### Dependencies

| Predecessor | Requirement |
|-------------|-------------|
| R1 | **COMPLETE** — mock pipeline, connector skeleton, mock Store layout |
| R2 | **COMPLETE WITH NOTES** — R2.1–R2.7; handoff spec R2.6; `--contract-evidence` path |
| R1.7 | Snapshot model skeleton — **superseded at assembly boundary** by OpenCart spec |
| R1.8B/C | Storage contract and layout — **frozen**; R3 uses, does not redesign |
| Architecture | EAR-OPENCART-SNAPSHOT-SPEC-v1, EAR-OPENCART-QUALITY-MAPPING-v1, EAR-SNAPSHOT-CONTRACT-v1, EAR-SNAPSHOT-LIFECYCLE-v1 |

### Inputs

| Input | Source | R3 use |
|-------|--------|--------|
| **Contract-shaped `EvidencePackage`** | R2.1 / R2.7 | Primary transformation source |
| **R2 structural validation eligibility** | R2.4 `EvidencePackageValidator` | Gate: invalid evidence must not proceed to assembly |
| **Handoff inputs H-IN-01–H-IN-10** | [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) | Authoritative consumption set |
| **Quarantine path binding** | R2.5 `{output_root}/{acquisition_id}/evidence/` | Bulk reads for section expansion (mock: logical refs) |
| **OpenCart spec + quality mapping** | Architecture Phase 2A/2C | Section targets and Level 0–1 minimums |
| **Storage contract** | R1.8B | Candidate persist shape under `snapshots/{snapshot_id}/` |
| **Config echoes** | Via provenance/scope echo — not silent re-read | Traceability to R1.2 session |

### Outputs

| Output | Consumer | Notes |
|--------|----------|-------|
| **Candidate Snapshot Package** | R5 Validate; operator inspection | OpenCart section tree; **unpublished** |
| **`snapshot_id`** | Store layout; future R4 Publish | **New** at R3 Store boundary |
| **Identity Continuity Record** | R5, operator, acquisition-log | `acquisition_id` correlation preserved |
| **`safe-unknown/` section** | R5; consumers (post-Publish) | Honesty carriers from evidence |
| **HandoffContract code module** | R3 implementation | Mapping tables — deferred from R2.6 |
| **Assembly eligibility result** | Operator / pipeline | Distinct from R5 Validate pass |

### Explicit non-outputs

| Output | Owner |
|--------|-------|
| Validated / certified snapshot | **R5** |
| `package_quality_level` ≥ 1 **certification** | **R5** |
| Publish gate approval | **R5** + **R4** |
| Published snapshot reference | **R4** |
| Consumer reports / OCPilot Run 5 | Consumer programs |
| Evidence quarantine writes | **R2** (deferred persist) |
| Live acquisition artefacts | R1 + Execution Authorization |

---

## Non-Goals

Explicit exclusions for R3 (defer per R2 readiness notes and backlog):

| # | Non-goal | Owner / phase |
|---|----------|---------------|
| 1 | **Validate** — snapshot contract certification, quality possession automation | **R5** |
| 2 | **Publish** — consumer-visible snapshot promotion | **R4** |
| 3 | **Consumer outputs** — OCPilot reports, intake automation | Consumer programs |
| 4 | **Live acquisition** — connected Mode 2, remote reads beyond mock | Execution Authorization |
| 5 | **OCPilot integration** | OCPilot program |
| 6 | **SITE-001** / **PILOT-001** execution | Separate Execution Authorization |
| 7 | **SFTP live connector execution** | R1 beyond skeleton; pilot |
| 8 | **Store redesign** / R1.9 hardening changes | **Frozen** at R1.9 |
| 9 | **Persistence layout amendment** | R1.8C chartered — R3 uses existing `{acquisition_id}/snapshots/{snapshot_id}/` |
| 10 | **Level 2+ inventory completeness** as engineering target | Backlog § R3 non-goals; L1 candidate minimum |
| 11 | **Automatic Publish** without HITL | **R4** |
| 12 | **Evidence Package generation or mutation** | **R2** |
| 13 | **R2 quarantine persist** (IAC-03 debt) | R2 follow-on / R3-adjacent — not blocking charter |
| 14 | **Normative JSON Schema / ZIP layout files** | **SAFE UNKNOWN** |
| 15 | **Architecture redesign** | Amendment charter only |

Per [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R3: engineering target is **candidate Snapshot Level 1** with honest `safe-unknown` — not L2+ completeness or auto-Publish.

---

## Snapshot Package Contract

Normative source: [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md). **Contract classification only** — no spec redesign, no schema generation, no implementation in this charter.

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
| `package_quality_level` (candidate) | **Required** | **Level 0 honest default** until R5 certifies possession — R3 must not inflate |
| `bulk_root` (snapshot) | **Optional** | External snapshot bulk ref — ≠ evidence quarantine |
| Prior snapshot reference | **Optional** | Partial reruns (`p1`, `p2`) |
| Publish metadata (`published_at`, etc.) | **Future** / **R4** | Not at assembly |

### OpenCart section tree

| Section | Classification | Level 0 | Level 1 (R3 engineering target) | R3 assembly role |
|---------|----------------|---------|----------------------------------|------------------|
| **`metadata/`** | **Required** | Min identity set | + version claims, baseline refs | HO-ALLOW-02; platform/version from evidence + operator context |
| **`file-manifest/`** | **Required** (L1+) / **Optional** (L0 via safe-unknown) | Listed in safe-unknown if absent | Root folders, path list subset, version proof files | HO-ALLOW-05; expand from manifest artifact ref |
| **`theme-info/`** | **Required** (L1+) or **safe-unknown** | — | Active theme name or gap | HO-ALLOW-06; from artifact index / mock |
| **`extension-inventory/`** | **Optional** (L2+) | safe-unknown at L0–L1 | Not required for R3 L1 target | Future L2; placeholder safe-unknown at L1 |
| **`ocmod-inventory/`** | **Optional** (L2+) | safe-unknown at L0–L1 | Not required for R3 L1 target | Future L2; placeholder safe-unknown at L1 |
| **`database-metadata/`** | **Required** (L1+) or **safe-unknown** | — | Prefix + table list or gap | HO-ALLOW-06 |
| **`seo-structure/`** | **Required** (L1+) or **safe-unknown** | — | SEO flags or gap | HO-ALLOW-06 |
| **`environment/`** | **Required** | Always | `environment_class` or `UNKNOWN` | HO-ALLOW-07 |
| **`safe-unknown/`** | **Required** | Always | Residual + section-level gaps | HO-ALLOW-03, HO-ALLOW-04, HO-ALLOW-08, HO-ALLOW-09 |
| **`acquisition-log/`** | **Required** | Min approval + mode | Scope, channel, timestamps | HO-ALLOW-01 |

### Classification summary

| Classification | Sections / elements |
|----------------|---------------------|
| **Required (always on candidate)** | `metadata/` (min set), `environment/`, `safe-unknown/`, `acquisition-log/`, `snapshot_id`, contract ids |
| **Required (L1 target — or explicit safe-unknown)** | `file-manifest/`, `database-metadata/`, `seo-structure/`, `theme-info/` |
| **Optional** | `bulk_root`, prior snapshot ref, inline vs external manifest form, extended metadata claims |
| **Future (not R3 L1 target)** | L2+ full `extension-inventory/`, `ocmod-inventory/` population; comprehensive L3 manifest; publish metadata; normative schema files |

Per [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md): R3 assembles **candidate**; R5 certifies **possession** before honest level claim at Publish.

---

## Identity Continuity

Authoritative chain from [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) § Identity continuity — extended for R3 charter.

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
                    │
                    ▼  R5 Validate → R4 Publish
```

### Field mapping

| Evidence (R2) | Snapshot (R3) | Rule |
|---------------|---------------|------|
| `acquisition_id` | Folder correlation; optional `acquisition-log` reference | **Survives** — same value; binds acquisition tree |
| `site_ref` | `site_id` in metadata | **Transforms** — rename per OpenCart contract |
| `connector_class` | `acquisition-log` channel provenance; metadata context | **Survives** — may combine with `channel` |
| `channel` | `acquisition-log` | **Survives** |
| `started_at`, `completed_at` | `acquisition-log`; metadata acquisition date | **Survives** — claim semantics at Validate |
| `operator_approval_ref` | `operator_approval` | **Transforms** — field rename |
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

## Ownership Boundary

### Concern → Owner matrix

| Concern | R2 | R3 | R4 | R5 | Operator | Consumer |
|---------|----|----|----|----|----------|----------|
| Evidence Package shape | **Owns** | Reads | — | Reads (Validate input chain) | Inspects quarantine | **No access** |
| Evidence quarantine `{acquisition_id}/evidence/` | **Owns** write | Read bulk for assembly | — | Read for Validate | **Owns** external root | **No access** |
| Artifact index (logical) | **Owns** | Consumes | — | Validates adequacy | — | — |
| R2 structural validation | **Owns** | Requires pass | — | — | — | — |
| OpenCart section assembly | — | **Owns** | — | — | — | — |
| Candidate snapshot tree | — | **Owns** write | Reads stored | **Owns** certification | Inspects | **No access** until Publish |
| `snapshot_id` creation | — | **Owns** | References | Validates | — | References post-Publish |
| `package_quality_level` certification | Forbidden | Candidate L0 only | Matches validated | **Owns** | HITL override | Reads published claim |
| Snapshot Store persist | — | **Owns** candidate write per R1.8 layout | — | — | **Owns** external storage | — |
| Validate report / publish readiness | — | — | Input to Publish | **Owns** | HITL | — |
| Publish / consumer reference | — | — | **Owns** | Gates | Approves | **Owns** intake |
| Secrets / credentials | Never in git | Never in candidate sections | Never published | Enforces redaction | **Owns** secrets/ | Never receives |
| Live acquisition / SFTP | R1 skeleton | Forbidden | — | — | Pilot authorization | — |
| `safe-unknown` population | Scope/status carriers | **Owns** section assembly | — | **Owns** publish readiness review | Reviews | Consumes post-Publish |

### Overlap prevention

| Boundary | Rule |
|----------|------|
| R2 ↔ R3 | R2 **never** writes OpenCart sections or `snapshots/`; R3 **never** mutates evidence or quarantine index |
| R3 ↔ R5 | R3 **never** certifies quality or publish readiness; R5 **never** populates sections from raw connector output |
| R3 ↔ R4 | R3 **never** publishes; R4 **never** assembles sections |
| R3 ↔ R1.8 | R3 **uses** frozen Store layout — no redesign |
| R3 ↔ Operator | Operator owns external paths, approval refs, environment class declarations |

---

## R3 → R5 Boundary

### R3 creates candidate snapshot

R3 Snapshot Assembly produces a **candidate Snapshot Package**:

- OpenCart section tree populated per spec (L0 minimum + L1 targets with honest gaps)
- `snapshot_id` assigned at Store boundary
- `package_quality_level: 0` **by default** on candidate unless R5 has already run (ordering: assembly typically precedes Validate)
- Inspectable under `{output_root}/{acquisition_id}/snapshots/{snapshot_id}/`
- **Unpublished** — no consumer path, no Publish metadata

### R3 does NOT

| Prohibition | Owner |
|-------------|-------|
| **Assign `package_quality_level` ≥ 1 as certified claim** | **R5** — possession rules in [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| **Approve Publish** | **R4** + operator HITL |
| **Certify readiness** for consumer intake | **R5** + [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md) |
| **Perform consumer validation** (OCPilot rules, baseline diff execution) | **Consumer** programs |
| **Perform publish gating** | **R5** (Validate) then **R4** (Publish) |
| **Treat R2 structural pass as R5 Validate pass** | HO-INV-06 |
| **Treat assembly success as Publish approval** | HO-INV-07 |
| **Suppress `safe-unknown` when evidence partial/failed** | HO-FORBID-10 |
| **Enforce redaction policy on candidate** (full) | **R5** at Validate — R3 must not copy secrets into sections |

### Handoff from R3 to R5

| R3 output | R5 input |
|-----------|----------|
| Candidate section tree | Contract validation target |
| Candidate `package_quality_level: 0` | Starting point for possession assessment |
| `safe-unknown/` entries | Review for publish honesty |
| Identity continuity record | Audit correlation |
| Assembly eligibility result | Precondition — not Validate pass |

**Ordering note:** Architecture allows R5 to parallel R3 after R2 shape stable ([R2-CHARTER-v1.md](R2-CHARTER-v1.md) § SAFE UNKNOWN). Canonical pipeline for this charter:

```text
R2 Evidence → R3 Candidate Assembly → R5 Validate → Store (if not already) → R4 Publish
```

R5 and R3 both **read** evidence; neither **owns** quarantine. R3 **writes** candidate snapshot; R5 **certifies** it.

---

## Success Criteria

R3 **program** (Snapshot Assembly Layer charter) is **complete** when:

| ID | Criterion | Verification |
|----|-----------|--------------|
| SC-R3-01 | Mission answers: what Snapshot Assembly is, why evidence cannot publish directly, why R3 is separate from R2 and R5 | This charter § Mission |
| SC-R3-02 | Scope includes evidence consumption, section assembly, safe-unknown, identity continuity, candidate generation, storage inputs | § Scope |
| SC-R3-03 | Non-goals exclude Validate, Publish, live acquisition, OCPilot, SITE-001, Store redesign | § Non-Goals |
| SC-R3-04 | Snapshot Package Contract classified Required/Optional/Future without spec redesign | § Snapshot Package Contract |
| SC-R3-05 | Identity continuity documented: survives, transforms, R3-created fields | § Identity Continuity |
| SC-R3-06 | Ownership matrix prevents R2/R3/R5/R4 overlap | § Ownership Boundary |
| SC-R3-07 | R3→R5 boundary explicit — candidate only, no quality certification or publish gates | § R3 → R5 Boundary |
| SC-R3-08 | R3 Implementation Charter **READY** as next artifact | Gate transition |
| SC-R3-09 | R2 readiness notes N-R2R-01–N-R2R-05 reflected | § Dependencies; Non-Goals |
| SC-R3-10 | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) and [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) updated | Program navigation |

**Engineering acceptance (post-implementation — R3 Implementation Charter, not this document):**

| ID | Criterion | Source |
|----|-----------|--------|
| IAC-R3-01 | Candidate snapshot inspectable under Store layout | Backlog § R3 acceptance |
| IAC-R3-02 | Section tree complete for L1 target or honest `safe-unknown` | EAR-OPENCART-SNAPSHOT-SPEC-v1 |
| IAC-R3-03 | Identity continuity preserved (`acquisition_id`, `site_id`) | R2.6 |
| IAC-R3-04 | `safe-unknown` propagated from partial/failed evidence | HO-ALLOW-03/04 |
| IAC-R3-05 | Ready for R5 Validate — **not** Publish | R3→R5 boundary |
| IAC-R3-06 | Assembly from `evidence_package_models.EvidencePackage` | N-R2R-02 |

**Explicitly excluded from R3 success:** Publish execution, consumer intake, Level 2+ completeness, live acquisition.

---

## Stop Conditions

Stop or escalate **before** R3 implementation if:

| ID | Condition | Action |
|----|-----------|--------|
| ST-R3-01 | Charter scope includes **Publish** or consumer output generation | **STOP** — reclassify as R4 / consumer |
| ST-R3-02 | Charter scope includes **R5 Validate automation** as R3 deliverable | **STOP** — reclassify as R5 |
| ST-R3-03 | Charter attempts to **bypass Validate** — candidate marked publish-ready without R5 | **STOP** |
| ST-R3-04 | Charter requires **SITE-001**, **PILOT-001**, live SFTP, or connected acquisition | **STOP** — Execution Authorization |
| ST-R3-05 | Charter requires **Store / persistence redesign** contradicting R1.9 | **STOP** — architecture amendment |
| ST-R3-06 | Charter merges evidence quarantine into snapshot tree | **STOP** — HO-FORBID-03 |
| ST-R3-07 | Charter sets **`package_quality_level` ≥ 1** as assembly default without R5 | **STOP** — quality inflation |
| ST-R3-08 | Implementation proposed without **R3 Implementation Charter** + human gate | **STOP** — per R1/R2 gate pattern |
| ST-R3-09 | Charter attempts to **redesign R1/R2** evidence contracts | **STOP** — amendment charter |
| ST-R3-10 | Charter includes **OCPilot integration** | **STOP** — consumer program |
| ST-R3-11 | Snapshot bulk placed under **git workspace** or consumer paths pre-Publish | **STOP** — EAR-STORAGE-MODEL |

### Out-of-scope conditions (ongoing)

Work is **out of R3** if it matches any row in **Non-Goals** or:

- Certifies publish readiness or quality level possession
- Executes Validate gates or consumer baseline diff
- Enables network acquisition in R3 charter scope
- Mutates frozen Evidence Package after handoff
- Deletes evidence as condition of assembly (PC-08)

---

## Pipeline position

```text
Acquire (R1 connector / mock)
        ↓
Evidence Package (R2.1–R2.7)
        ↓
R2 structural validation (R2.4)
        ↓
╔═══════════════════════════════════════╗
║  R2.6 HANDOFF (read-only on evidence) ║
╚═══════════════════════════════════════╝
        ↓
R3 Snapshot Assembly — candidate OpenCart sections
        ↓
R5 Validate + human HITL
        ↓
Store (R1.8 mock — frozen layout)
        ↓
Publish (R4 — not in R3 scope)
        ↓
Consume (consumer programs)
```

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| R3 label confusion — engineers implement Validate or Publish as R3 | High | Mission + Non-Goals; R3→R5 boundary |
| Quality inflation at assembly (`package_quality_level` ≥ 1) | High | Candidate L0 default; R5 owns certification |
| R1.6 mock chain bypasses R2 handoff | Medium | N-R2R-02; deprecate at snapshot boundary |
| Evidence/snapshot tree merge | High | HO-FORBID-03; ownership matrix |
| Dual evidence models during R3 early work | Medium | R2.1 authoritative input |
| No quarantine on disk — section expansion lacks bulk | Low (mock) | Mock-first logical refs; D-R2-01 debt tracked |
| R5 vs R3 ordering ambiguity | Low | Pipeline position; parallel allowed with same inputs |
| Scope echo empty in sample config | Low | safe-unknown at assembly; R-R3-04 |
| Validate terminology collision (R2 vs EAR Validate) | Medium | Disambiguate in all R3 docs per T-03 |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Exact per-section field mapping (all OpenCart sections) | R3 Implementation Charter |
| Physical encoding (folder vs ZIP) for candidate persist | R1.8B SAFE UNKNOWN — logical tree normative |
| Official JSON Schema for snapshot package | Not in repo |
| 1:N `acquisition_id` → `snapshot_id` merge policy | Architecture SAFE UNKNOWN |
| Hybrid multi-package assembly | Future R2.8 |
| `HandoffRecord` / assembly sidecar serialization format | Not in repo |
| Whether R3 reads evidence from memory vs quarantine index only | Implementation choice |
| Production `snapshot_id` generation algorithm | Mock at R1.7; live **SAFE UNKNOWN** |
| Quarantine persist (IAC-03) timing relative to R3 | R2 debt — not charter blocker |
| R5 strict ordering before vs parallel with R3 assembly | Backlog allows parallel with risk acceptance |
| Level 2+ section population schedule | Future milestone beyond R3 L1 target |
| CLI runtime verification for R3 charter | Charter review only — no code |

---

## Planning notes (carried from R2)

| Note | Action |
|------|--------|
| N-R2R-01 | R3 Charter references R2.6 handoff and R2.4 validation boundary — **satisfied** |
| N-R2R-02 | R3 assembly consumes `evidence_package_models.EvidencePackage` — scoped in Implementation Charter |
| N-R2R-03 | Retain `--contract-evidence` until R3 chain wired |
| N-R2R-04 | Quarantine persist tracked as debt — not blocking R3 charter |
| N-R2R-05 | Do not delete R1.6 path without migration charter |

---

## Evidence index

| ID | Source |
|----|--------|
| C-R3-01 | [R2-READINESS-REVIEW-v1.md](R2-READINESS-REVIEW-v1.md) |
| C-R3-02 | [R2-READINESS-DECISION-v1.md](R2-READINESS-DECISION-v1.md) |
| C-R3-03 | [R2-CHARTER-v1.md](R2-CHARTER-v1.md) |
| C-R3-04 | [R2-IMPLEMENTATION-CHARTER-v1.md](R2-IMPLEMENTATION-CHARTER-v1.md) |
| C-R3-05 | [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) |
| C-R3-06 | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md) |
| C-R3-07 | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| C-R3-08 | [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) |
| C-R3-09 | [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) |
| C-R3-10 | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R3 |
| C-R3-11 | [R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md](R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md) |

---

## Cross-references

| Document | Use |
|----------|-----|
| [R3-DECISION-v1.md](R3-DECISION-v1.md) | Charter gate decision |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Program status |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation |
