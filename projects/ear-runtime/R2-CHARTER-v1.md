# R2 Charter v1

**Type:** Program charter — **no** runtime code, **no** implementation, **no** persistence changes in this phase  
**Phase:** R2 — Evidence Package Layer  
**Date:** 2026-06-04  
**Lane:** B — EAR Runtime Architecture  
**Prior phases:** R1 **COMPLETE**; [R2-PLANNING-REVIEW-v1.md](R2-PLANNING-REVIEW-v1.md); [R2-PLANNING-DECISION-v1.md](R2-PLANNING-DECISION-v1.md) — **APPROVED WITH NOTES**  
**Decision companion:** [R2-DECISION-v1.md](R2-DECISION-v1.md)  
**Architecture sources:** [shared/external-access-runtime/](../../shared/external-access-runtime/)

---

## Purpose

Formally charter **R2 — Evidence Package Layer** before any R2 engineering work begins. R2 closes the gap between R1.6 mock evidence skeleton and normative [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md), and defines the **Evidence → Snapshot** handoff boundary for R3.

**R2 delivers:** mission, scope, non-goals, evidence contract, quarantine charter, success criteria, stop conditions, and boundaries — **charter only**.

**R2 does not deliver:** OpenCart snapshot section population, live acquisition, Publish, or consumer integration.

---

## Mission

### Why R2 exists

EAR separates **acquisition-internal evidence** from **consumer-facing snapshots**. R1 delivered a mock pipeline (`Config → Listing → Manifest → Evidence → Snapshot → Store`) with an in-memory `EvidencePackage` that does **not** satisfy the architecture evidence contract ([R2-PLANNING-REVIEW-v1.md](R2-PLANNING-REVIEW-v1.md) § Evidence Package). R1.8 mock Store persists snapshots only; **evidence quarantine was explicitly deferred** ([R1.8E-PERSISTENCE-DECISION-v1.md](R1.8E-PERSISTENCE-DECISION-v1.md)).

Without R2, connectors and validation cannot rely on a governed, inspectable evidence shape; R3 cannot honestly assemble Level 1+ snapshot sections from validated inputs.

### Gap R2 closes

| Gap (R1 state) | R2 target (architecture) |
|----------------|--------------------------|
| Evidence lacks `acquisition_id`, artifact index, scope echo, connector status | Contract-aligned Evidence Package model and generator charter |
| Evidence/snapshot boundary blurred in mock pipeline | Explicit **Evidence → Snapshot** translation boundary (inputs to R3 only) |
| No evidence quarantine on disk | Evidence quarantine layout charter under `{acquisition_id}/evidence/` ([R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md](R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md)) |
| Partial acquisition may imply complete snapshot | Honest partial/failed status preserved at evidence stage |

### Pipeline connection (conceptual)

```text
Acquisition (connector / mock)
        ↓
Evidence Package          ← R2 scope (model, validation, quarantine charter, generator bounds)
        ↓
EAR Validation            ← R5 helpers + human HITL (not R2 implementation)
        ↓
Snapshot Package          ← R3 (OpenCart sections, quality levels)
        ↓
Store                     ← R1.8 done (mock Store); R2 does not redesign Store
```

Per [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md): Evidence is **acquisition-internal**, **pre-contract**, and **not** consumer input. Per [EAR-SNAPSHOT-LIFECYCLE-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-LIFECYCLE-v1.md): Validation **transforms** evidence into snapshot sections; Publish (R4) and Consume follow Store.

**Authoritative program label:** Architecture backlog **R2 = Evidence Package Generator** — **not** OpenCart snapshot section expansion ([EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R2).

---

## Scope

### In scope (R2 program — charter defines; implementation follows R2 Implementation Charter)

| # | Work area | Boundary |
|---|-----------|----------|
| 1 | **Evidence Package Model** | Logical structure mapping to [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md); extends R1.6 skeleton without claiming snapshot completeness |
| 2 | **Evidence Package Generator** | Assemble evidence from connector output (mock path first per R1 discipline) + acquisition metadata; traceable to connector run |
| 3 | **Evidence Package Validation** | Structural/honesty checks at evidence boundary (partial flags, required identity/provenance); **not** final `package_quality_level` certification (snapshot/R5) |
| 4 | **Evidence Quarantine Model** | Charter for `{output_root}/{acquisition_id}/evidence/` — external bulk, pre-redaction quarantine, no secrets in git ([EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md)) |
| 5 | **Evidence Metadata** | Provenance, scope echo, connector status, timestamps, operator approval ref |
| 6 | **Evidence Identity** | `acquisition_id`, `site_ref`, `connector_class` binding |
| 7 | **Evidence References** | Artifact index + optional bulk refs to external quarantine paths |
| 8 | **Evidence → Snapshot Boundary** | Specification of what validation/R3 may consume from evidence; **no** OpenCart section writers in R2 |

### Allowed artifact types (architecture)

| Artifact | R2 role |
|----------|---------|
| Charter documents (`R2-*`) | This phase |
| Evidence model / validator / generator **design** in Implementation Charter | Next gate |
| Mock-path evidence emission | Consistent with R1 mock-only until pilot chartered |
| Quarantine index layout (logical) | Operator-bound paths under `ear\store\` |

### Dependency

| Predecessor | Requirement |
|-------------|-------------|
| R1 | **COMPLETE** — mock pipeline, connector skeleton, mock Store |
| R1.8C | Evidence path `{acquisition_id}/evidence/` **defined** — persist deferred to R2 |
| Architecture freeze | [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md), [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) |

---

## Non-Goals

Explicit exclusions for R2 (defer per planning review and backlog):

| # | Non-goal | Owner / phase |
|---|----------|---------------|
| 1 | **OpenCart section expansion** — `file-manifest/`, `theme-info/`, `extension-inventory/`, `ocmod-inventory/`, `database-metadata/`, `seo-structure/`, dedicated `environment/` section tree | **R3** |
| 2 | **File Manifest Expansion** (path lists, hashes, baseline diff) | **R3** |
| 3 | **Snapshot quality level 1–3 claims** on persist | **R3** + **R5**; mock Store remains Level 0 until R3 validates possession |
| 4 | **Publish** / consumer intake / OCPilot consumption | **R4** + consumer programs |
| 5 | **OCPilot integration** implementation | OCPilot program |
| 6 | **SITE-001** / **PILOT-001** execution / live SFTP / connected Mode 2 acquisition | Separate Execution Authorization |
| 7 | **SFTP** live connector execution | R1 connector beyond skeleton; pilot |
| 8 | **Persistence redesign** / Store hardening changes | Closed at **R1.9** |
| 9 | **R3 Snapshot Builder** — candidate OpenCart package assembly | **R3** |
| 10 | **R4 Snapshot Publisher** | **R4** |
| 11 | **R5 Validation Helpers** — quality possession automation, publish gates | **R5** (may parallel R3 after R2 shape stable) |
| 12 | **Automated redaction engine** beyond chartered rules | Future / operator |
| 13 | **JSON Schema / ZIP layout / dump format** normative files | **SAFE UNKNOWN** per evidence spec |
| 14 | **Architecture redesign** | Amendment charter only |

Per backlog § R2 non-goals: no consumer publish; no final snapshot quality claim; no automated redaction policy product.

---

## Evidence Package Contract

Normative source: [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md). **Contract only** — no schema generation, no implementation in this charter.

### Minimum components

| Component | Classification | Notes |
|-----------|----------------|-------|
| **Identity:** `acquisition_id`, `site_ref`, `connector_class` | **Required** | R1.6 skeleton missing — gap per planning review |
| **Provenance:** channel, `started_at`, `completed_at`, `operator_approval_ref` | **Required** | Maps to acquisition-log inputs at Validate |
| **Scope echo:** approved vs attempted paths/tables | **Required** | Honesty for partial acquisition |
| **Artifact index:** logical list (manifest file, exports, screenshots as refs) | **Required** | Not full OpenCart `file-manifest/` |
| **Connector status:** success / partial / failed | **Required** | Failed legs must not imply complete snapshot |
| **Errors and warnings** | **Required when applicable** | Per connector contract |
| **Bulk references** | **Optional** | External paths; large files in quarantine |
| **Raw protocol artifacts** (listings, hashes, export files) | **Optional** | Channel-dependent |
| **Hybrid merge semantics** (`leg_ref`, ordered package set) | **Future** | Conceptual in evidence spec; charter notes only |
| **Evidence checksum registry before validation** | **SAFE UNKNOWN** | Evidence spec § SAFE UNKNOWN |
| **Retention period after successful publish** | **SAFE UNKNOWN** | PC-08 minimum through Store; durations not fixed |
| **Virus scan on ZIP evidence** | **SAFE UNKNOWN** | Policy not fixed |
| **Official JSON Schema** | **SAFE UNKNOWN** | Not in repo |

### Forbidden at evidence stage (target policy)

| Rule | Source |
|------|--------|
| Publishing to consumer bulk without validation pass | EAR-EVIDENCE-PACKAGE-v1 |
| Treating Evidence Package as Snapshot Package | EAR-EVIDENCE-PACKAGE-v1 vs snapshot contract |
| Certifying `package_quality_level` at evidence stage | Evidence vs snapshot table |

### Evidence vs Snapshot (boundary summary)

| Dimension | Evidence (R2) | Snapshot (R3+) |
|-----------|---------------|----------------|
| Audience | EAR Validation + operator | Consumers |
| Lifecycle | Acquire → Validate (then retire/archive) | Store → Publish → Consume → Archive |
| Completeness | May be partial | Gaps in `safe-unknown` at publish |
| Quality | Not certified | `package_quality_level` at publish |
| Storage | `{acquisition_id}/evidence/` quarantine | `{acquisition_id}/snapshots/{snapshot_id}/` Store |

---

## Evidence Quarantine Charter

Architecture evidence only — **no redesign**. Anchors: [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md), [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md), [R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md](R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md) § PC-08.

### Purpose

| Goal | Detail |
|------|--------|
| **Quarantine risk** | Raw/semi-raw exports inspected before consumer visibility |
| **Pre-redaction holding** | Secrets may exist pre-redaction in external quarantine only |
| **Decouple bulk from git** | Large downloads and extracts live external; package holds refs |
| **Support partial runs** | Failed connector legs remain visible in evidence, not silent in snapshot |

### Ownership

| Role | Responsibility |
|------|----------------|
| **Operator** | Creates/owns `C:\AI MARS STORAGE\ear\` subtree; placement policy; post-Publish evidence disposition |
| **EAR (R2 implementation)** | Writes evidence index and refs under chartered `evidence/` path; never git-bound secrets |
| **Consumer** | **No** access to evidence quarantine — published snapshot only (R4) |

### Lifecycle

| Phase | Evidence quarantine |
|-------|---------------------|
| **Acquire** | Created/updated by connector or mock generator |
| **Validate** | Read by EAR; mapped toward snapshot sections; redaction enforced before consumer paths |
| **Store** | Snapshot stored separately under `snapshots/{snapshot_id}/`; evidence **not** merged into snapshot tree |
| **Publish** | Evidence **not** published to consumers |
| **Consume** | Consumers see snapshot only |
| **Archive** | Evidence may archive with acquisition; retention durations **SAFE UNKNOWN** |

**Minimum rule (PC-08):** Evidence **must not** be deleted before Validate pass and successful Store of derived snapshot. Post-Store disposition = operator policy; **archive recommended** over immediate delete until Publish is recorded.

### Relationships

| Relation | Rule |
|----------|------|
| **To Store** | Sibling under `{acquisition_id}/`: `evidence/` ≠ `snapshots/{snapshot_id}/` |
| **To Snapshot** | Validation transforms evidence → snapshot sections; evidence package is **not** renamed as snapshot |
| **To Publish** | Publish promotes **snapshot** reference only; evidence stays acquisition-internal |

Exact folder file naming inside `evidence/` — **SAFE UNKNOWN** until R2 Implementation Charter (operator-bound).

---

## Success Criteria

R2 program (Evidence Package Layer) is **complete** when all measurable criteria hold:

| ID | Criterion | Verification |
|----|-----------|--------------|
| SC-01 | Evidence Package contract documented and mapped to R1.6 gap | This charter + Implementation Charter field mapping |
| SC-02 | Evidence quarantine path and lifecycle chartered under `ear\store\{acquisition_id}/evidence/` | R2 charter § Quarantine; aligns R1.8C |
| SC-03 | Evidence → Snapshot boundary explicit — no OpenCart section ownership in R2 | Non-goals + boundary table |
| SC-04 | R2 Implementation Charter **READY** with scoped generator, model, validation tasks | Next artifact |
| SC-05 | Mock Store remains **Level 0** honest (`package_quality_level: 0`) until R3 | No quality inflation at evidence stage |
| SC-06 | Planning notes N-01–N-06 from [R2-PLANNING-DECISION-v1.md](R2-PLANNING-DECISION-v1.md) reflected in charter | Non-goals and mission |
| SC-07 | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) and [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) updated | Program navigation |

**Engineering acceptance (post-implementation — R2 Implementation Charter, not this document):** Evidence Package is inspectable, traceable to connector run, and separable from published snapshot tree ([EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R2).

---

## Stop Conditions

Stop or escalate **before** R2 implementation if:

| ID | Condition | Action |
|----|-----------|--------|
| ST-01 | Charter scope expands to OpenCart section population (`file-manifest`, theme, DB, SEO, etc.) | **STOP** — reclassify as R3 |
| ST-02 | Charter requires live SFTP, SITE-001, or PILOT execution | **STOP** — require Execution Authorization |
| ST-03 | Charter requires Publish or OCPilot intake | **STOP** — R4 / consumer |
| ST-04 | Charter requires persistence/Store redesign contradicting R1.9 | **STOP** — architecture amendment |
| ST-05 | Evidence quarantine path placed under git workspace or consumer `project-sites\` | **STOP** — violates EAR-STORAGE-MODEL |
| ST-06 | Implementation proposed without R2 Implementation Charter + human gate | **STOP** — per [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md) pattern |

---

## Out-of-scope conditions (ongoing)

Work is **out of R2** if it matches any row in **Non-Goals** or:

- Claims `package_quality_level` ≥ 1 without R3 section possession
- Writes OpenCart section folders from evidence in R2 phase
- Connects to remote SITE or enables network acquisition in R2 charter scope
- Integrates OCPilot Run 5 or consumer reports paths

---

## R2 Boundaries

### Upstream (inputs)

| Input | Source |
|-------|--------|
| Connector output (mock or future live) | R1 pipeline, `manifest` chain |
| Acquisition metadata | Config: `acquisition_id`, `site_ref`, scope, mode, operator approval ref |
| Architecture contracts | EAR-EVIDENCE-PACKAGE-v1, EAR-STORAGE-MODEL-v1, EAR-SNAPSHOT-LIFECYCLE-v1 |

### Downstream (outputs to next phases)

| Output | Consumer |
|--------|----------|
| Contract-shaped Evidence Package (logical + quarantine index) | R5 Validate helpers; human Validate |
| Evidence → snapshot input mapping spec | **R3** Snapshot Builder |
| Quarantine layout on disk (when implemented) | Operator inspection; not consumers |

### Parallel / forbidden overlap

| Phase | Relationship to R2 |
|-------|-------------------|
| **R1.8 Store** | **Frozen** — R2 adds `evidence/` persist only; does not change snapshot 3-file mock honesty |
| **R3** | **Blocked** on stable R2 evidence shape per backlog `R1 → R2 → R3` |
| **R4 Publish** | **Forbidden** in R2 |
| **R5** | May parallel R3 after R2 stable — not part of R2 charter |

### Execution boundaries (charter phase)

| Boundary | Rule |
|----------|------|
| **This document** | Architecture and scope only |
| **Code** | **None** in R2 Charter phase |
| **Network** | **Disabled** until pilot chartered |
| **Git** | No evidence bulk, no secrets |
| **Human gate** | R2 Implementation requires separate Implementation Charter + approval |

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| R2 label confusion — engineers implement snapshot sections as R2 | High | Mission + Non-Goals; backlog citation |
| Quality level inflation at evidence or persist | High | SC-05; fail closed; Level 0 until R3 |
| Evidence/snapshot path collision | Medium | Quarantine charter sibling layout |
| Pilot pressure (SITE-001/SFTP) | Medium | Explicit non-goals ST-02 |
| Publish before Validate | Medium | R4 gated; evidence not published |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Official JSON Schema for evidence package | Not in repo |
| Exact files inside `evidence/` index (names, sidecar format) | R2 Implementation Charter |
| Evidence retention durations (days/months) | Operator policy; PC-08 minimum only |
| Evidence checksum registry before validation | Architecture SAFE UNKNOWN |
| Hybrid 1:N `acquisition_id` → `snapshot_id` merge policy | Architecture SAFE UNKNOWN |
| Virus scan policy on ZIP evidence | SAFE UNKNOWN |
| Whether R5 runs strictly before or parallel to R3 | Backlog allows parallel with risk acceptance |

---

## Evidence index

| ID | Source |
|----|--------|
| C-R2-01 | [R2-PLANNING-REVIEW-v1.md](R2-PLANNING-REVIEW-v1.md) |
| C-R2-02 | [R2-PLANNING-DECISION-v1.md](R2-PLANNING-DECISION-v1.md) |
| C-R2-03 | [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) |
| C-R2-04 | [EAR-SNAPSHOT-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-CONTRACT-v1.md) |
| C-R2-05 | [EAR-SNAPSHOT-LIFECYCLE-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-LIFECYCLE-v1.md) |
| C-R2-06 | [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) |
| C-R2-07 | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) |
| C-R2-08 | [R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md](R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md) |
| C-R2-09 | [R1.8E-PERSISTENCE-DECISION-v1.md](R1.8E-PERSISTENCE-DECISION-v1.md) |
| C-R2-10 | [R1.6-EVIDENCE-PACKAGE-MODEL-v1.md](R1.6-EVIDENCE-PACKAGE-MODEL-v1.md) |

---

## Cross-references

| Document | Use |
|----------|-----|
| [R2-DECISION-v1.md](R2-DECISION-v1.md) | Charter gate decision |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Program status |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation |
