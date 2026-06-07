# R2 — Architecture Consolidation Review v1

**Type:** Final architectural consistency review — **no** implementation, **no** generator, **no** validator, **no** persistence, **no** model changes  
**Phase:** R2 Architecture Consolidation (pre-R2.7)  
**Date:** 2026-06-05  
**Decision companion:** [R2-ARCHITECTURE-CONSOLIDATION-DECISION-v1.md](R2-ARCHITECTURE-CONSOLIDATION-DECISION-v1.md)  
**Chain reviewed:** [R2-CHARTER-v1.md](R2-CHARTER-v1.md), [R2-IMPLEMENTATION-CHARTER-v1.md](R2-IMPLEMENTATION-CHARTER-v1.md), [R2.1-EVIDENCE-PACKAGE-MODEL-v1.md](R2.1-EVIDENCE-PACKAGE-MODEL-v1.md), [R2.2-EVIDENCE-IDENTITY-REVIEW-v1.md](R2.2-EVIDENCE-IDENTITY-REVIEW-v1.md), [R2.3-EVIDENCE-ARTIFACT-INDEX-v1.md](R2.3-EVIDENCE-ARTIFACT-INDEX-v1.md), [R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md), [R2.5-EVIDENCE-QUARANTINE-LAYOUT-v1.md](R2.5-EVIDENCE-QUARANTINE-LAYOUT-v1.md), [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md)  
**Model reviewed (read-only):** `runtime/shared/evidence_package_models.py`

---

## Purpose

Perform a **final consolidation pass** over the complete R2 architecture chain before **R2.7 Evidence Package Generator** implementation begins. This is consistency verification only — not audit, redesign, governance, or new architecture.

**Explicit exclusions:** generator, validator implementation, persistence, runtime code, model edits, snapshot changes, OpenCart sections, SITE-001, SFTP, acquisition, network.

---

## Executive summary

| Question | Answer |
|----------|--------|
| Is R2 architecture coherent? | **Yes** — single evidence contract, sibling storage, explicit handoff, R2/R5 validation split |
| Is R2 internally consistent? | **Yes, with documented minor drift** — see Terminology Review § mismatches |
| Is R2 ready for generator work (R2.7)? | **Yes** — architecture consolidation **PASS WITH NOTES** |
| Unresolved items | Documented under Blind Spots and Recommendations — none block R2.7 charter |

---

## Terminology Review

### Authoritative terms (consistent across chain)

| Term | Definition (consolidated) | Primary authority |
|------|---------------------------|-------------------|
| **Evidence Package** | Acquisition-internal, pre-contract logical aggregate (`EvidencePackage`) | EAR-EVIDENCE-PACKAGE-v1; R2.1 |
| **Evidence Identity** | Three-field tuple: `acquisition_id`, `site_ref`, `connector_class` | R2.2; `EvidenceIdentity` |
| **Artifact Index** | Logical list of acquisition artefacts (`EvidenceArtifactIndex` / `EvidenceArtifact`) | R2.3 |
| **Evidence Status** | Package-level `connector_status` (`success` \| `partial` \| `failed`) on `EvidenceStatus` | R2.1; R2.3 ART-ST-* |
| **Quarantine** | External `{output_root}/{acquisition_id}/evidence/` — pre-redaction holding | R2.5; R1.8C PC-04 |
| **Handoff** | R2.6 boundary — read-only consumption bundle for R3; evidence ownership retained | R2.6 |
| **Snapshot** | Post-Validate governed package under `snapshots/{snapshot_id}/` | R1.7; R2.6 |
| **Validate** | **Two meanings — context-dependent, not contradictory:** (1) R2 structural gate on evidence; (2) EAR Validate stage (R5 + human HITL) on candidate snapshot | R2.4; EAR-SNAPSHOT-LIFECYCLE-v1 |
| **Publish** | R4 — promotes **snapshot** reference only; evidence never published | R2-CHARTER; R2.5 Q-INV-02 |
| **Consumer** | Read-only **published** snapshot; no quarantine access | EAR-STORAGE-MODEL; R2.5 |

### Per-artifact vs package status (resolved — not drift)

| Layer | Field | Values | Documented in |
|-------|-------|--------|---------------|
| Package | `EvidenceStatus.connector_status` | `success`, `partial`, `failed` | R2.1, R2.3 ART-ST-01 |
| Artifact | `EvidenceArtifact.status` | `present`, `missing`, `partial`, `skipped`, `unknown` | R2.3 |

**Assessment:** Intentional dual-layer status model; ART-ST-01 prevents enum overlap.

### Reported mismatches (terminology drift)

| ID | Mismatch | Documents | Severity | Resolution owner |
|----|----------|-----------|----------|------------------|
| T-01 | **`EvidenceStatusModel`** (Implementation Charter) vs **`EvidenceStatus`** (R2.1 model / code) | R2-IMPLEMENTATION-CHARTER § Outputs; `evidence_package_models.py` | Low | Treat `EvidenceStatus` as implementation name; update charter reference at convenience — **not blocking** |
| T-02 | **`evidence_models.py`** listed as R2 code placement vs **`evidence_package_models.py`** as actual R2.1 deliverable | R2-IMPLEMENTATION-CHARTER § Code placement | Low | R2.1 chose parallel file; R1.6 retained for mock until R2.7 — **documented** in R2.1 |
| T-03 | **Validate** label used for both R2 pre-gate and lifecycle Validate stage | R2-CHARTER pipeline diagram; R2.4; R2.6 | Medium (collision **risk**) | R2.4/R2.6 disambiguate; R2.7/R5 docs must use "R2 structural validation" vs "EAR Validate (R5)" |
| T-04 | **R2.4 milestone name** = "Evidence Validation" in Work Breakdown but R2.4 deliverable = **boundary review**; validator **code** = separate "R2.4 code milestone" | R2-IMPLEMENTATION-CHARTER § Work Breakdown; R2.4 doc | Medium (numbering) | R2.7 may implement validator alongside generator; no architectural contradiction |
| T-05 | **`scope_delta`** optional in Implementation Charter Identity Model — **absent** from R2.1 `EvidenceScopeEcho` | R2-IMPLEMENTATION-CHARTER L251; R2.1 | Low | Derivable from approved vs attempted; optional field not required at model layer — **SAFE UNKNOWN** whether to add |
| T-06 | **`completed_at`** — Implementation Charter: required **when terminal**; R2.1 model: always present as `str` (no Optional) | R2-IMPLEMENTATION-CHARTER; R2.4 R2-V-04; model | Low | R2.4 validator enforces conditional semantics; model allows empty string until R2.7 generator policy |
| T-07 | R1.6 mock uses **`site_id` / `connector` / `quality_level`** vs R2 contract **`site_ref` / `connector_class`** | R1.6 vs R2.1–R2.2 | Medium (operational) | Dual-model until R2.7 migration — **expected**, not architecture drift |

### No mismatch found

| Term pair | Status |
|-----------|--------|
| Evidence Package vs Snapshot Package | **Consistent** — separate contracts, storage, lifecycle |
| Quarantine vs Store | **Consistent** — sibling layout |
| Handoff vs transformation | **Consistent** — R2.6 HO-ALLOW-* / HO-FORBID-* |
| Publish vs Consume | **Consistent** — R4/R5 vs consumer read-only |
| `artifact_ref` vs `snapshot_id` | **Consistent** — separate identity layers |

---

## Ownership Review

### Authoritative ownership matrix (consolidated)

| Concern | Owner | R2 role | Overlap? |
|---------|-------|---------|----------|
| Evidence Package logical model | **R2** | R2.1 `EvidencePackage` | None |
| Evidence identity binding | **R2** (R2.7 generator) | R2.2 rules | None |
| Artifact index taxonomy | **R2** | R2.3 constants | None |
| R2 structural validation | **R2** (`EvidencePackageValidator` — not yet coded) | R2.4 boundary | None with R5 if boundary honored |
| Quarantine layout + index persist | **R2** (R2.7+) | R2.5 charter | None with R1.9 Store |
| Evidence → Snapshot handoff spec | **R2** | R2.6 `HandoffContract` (doc only) | None — R3 consumes read-only |
| OpenCart section assembly | **R3** | R2 **forbidden** | Clear |
| Snapshot `snapshot_id`, sections | **R3** | Created at Store boundary | None |
| `package_quality_level` certification | **R5** (+ R3 candidate assembly) | R2 **forbidden** | Clear |
| EAR Validate stage / publish gates | **R5** + human HITL | R2 pass ≠ R5 pass | Clear per R2.4 |
| Publish to consumers | **R4** | R2 **forbidden** | Clear |
| External storage root, disposition | **Operator** | EAR writes index under chartered path | None |
| Consumer intake | **Consumer programs** (OCPilot) | Published snapshot only | Clear |

### Overlaps detected

| ID | Overlap | Assessment |
|----|---------|------------|
| O-01 | R2 checks manifest **ref** in index; R5 checks `file-manifest/` **section adequacy** | **Intentional layered check** — R2.4 overlap table; not contradictory |
| O-02 | `operator_approval_ref` (evidence) vs `operator_approval` (snapshot) | **Intentional rename at boundary** — R2.4; R2.6 identity continuity |
| O-03 | R5 may parallel R3 after R2 stable | **Ordering ambiguity**, not ownership overlap — SAFE UNKNOWN |

### Gaps detected

| ID | Gap | Severity | Owner |
|----|-----|----------|-------|
| G-01 | `EvidencePackageValidator` **not implemented** | Expected | R2.4 code / R2.7 |
| G-02 | `HandoffContract` **code module not implemented** | Expected | R2.7 prep |
| G-03 | `EvidenceQuarantineLayout` **code module not implemented** | Expected | R2.7 |
| G-04 | R5 Validation Helpers charter **not yet written** | Future | R5 planning — R2.4 recommends reference to R2.4 boundary |
| G-05 | R3 Snapshot Builder charter **not yet written** | Future | R3 planning — R2.6 recommends cite R2.6 |

### Contradictory ownership

**None found** across R2–R5, Operator, Consumer when R2.4 ownership matrix and R2.5 ownership table are taken as authoritative.

---

## Lifecycle Review

### Canonical pipeline (consolidated)

```text
Acquire (R1 connector / mock)
        ↓
Evidence Package (R2.1–R2.7)
        ↓
R2 structural validation (R2.4 code — not yet implemented)
        ↓
R2.6 HANDOFF BOUNDARY (read-only bundle for R3)
        ↓
R3 Snapshot Builder — section assembly
        ↓
EAR Validate — R5 + human HITL
        ↓
Store (R1.8 mock — frozen; snapshots/{snapshot_id}/)
        ↓
Publish (R4 — not implemented)
        ↓
Consume (consumers — published snapshot only)
        ↓
Archive (operator policy)
```

### Transition verification

| Transition | Contract | Missing contract? | Circular dependency? |
|------------|----------|-------------------|----------------------|
| Acquire → Evidence | Connector/mock output + metadata → `EvidencePackage` | Generator spec R2.7 — **expected gap** | None |
| Evidence → R2 validate | R2-V-* checks (R2.4) | Validator code — **expected gap** | None |
| R2 validate → Handoff | HO-INV-13: invalid evidence blocks assembly | HandoffRecord format SAFE UNKNOWN | None |
| Handoff → R3 assembly | H-IN-01–H-IN-10; HO-ALLOW-* | Per-section mapping deferred R3 | None |
| R3 → R5 Validate | Evidence as provenance input + candidate snapshot | R5 charter TBD | None |
| Validate → Store | R1.8 mock 3-file persist | Frozen — no R2 change | None |
| Store → Publish | R4 backlog | R4 not started — **expected** | None |
| Publish → Consume | EAR-SNAPSHOT-PUBLISHING-v1 | Architecture only | None |
| Any → Archive | Operator policy; PC-08 minimum for evidence | Fixed durations SAFE UNKNOWN | None |

### PC-08 minimum (evidence retention)

**Consistent** across R2-CHARTER, R2.5, R1.8C: evidence **must not** be deleted before Validate pass **and** successful Store of derived snapshot.

### Lifecycle invariant chain (cross-milestone)

| Invariant family | Milestones | Consistent? |
|------------------|------------|-------------|
| VAL-INV-* (validation) | R2.4, R2.6 HO-INV-* | **Yes** |
| Q-INV-* (quarantine) | R2.5, R2.6 HO-FORBID-* | **Yes** |
| ART-INV-* (artifact index) | R2.3, R2.4 R2-V-* | **Yes** |
| INV-* (identity) | R2.2, R2.6 ID-DRIFT-* | **Yes** |

**Circular dependencies:** **None detected.**

---

## Identity Review

### Identifier trace (consolidated)

| Identifier | Origin | Owner | Mutable after package freeze? | Drift risk |
|------------|--------|-------|-------------------------------|------------|
| `acquisition_id` | Runtime session start | EAR generator (R2.7) | **No** (INV-06) | **Medium** — mock persist helper may diverge (R2.2 R-R2.2-04) |
| `site_ref` | R1.2 `site_id` mapping | R2 identity block | **No** | Low |
| `connector_class` | R1.2 `connector` mapping | R2 identity block | **No** | Low |
| `artifact_ref` | Generator / connector | Per index entry | **No** on logical package | Low — quarantine persist may map logical→storage |
| `snapshot_id` | R3 Store boundary | R3 | N/A on evidence | **Prevented** — ID-DRIFT-01 |
| `evidence_id` | — | **SAFE UNKNOWN** — do not introduce | — | **High** if engineers add convenience id |

### Duplication

| Check | Result |
|-------|--------|
| Identity fields duplicated per artifact | **No** — R2.3 |
| `snapshot_id` on evidence model | **No** — model inspection |
| `package_quality_level` on evidence | **No** — forbidden consistently |
| `site_id` on R2 model | **No** — R2.1 exclusion |

### Unsafe mutations (forbidden — consistent)

| Mutation | Authority |
|----------|-----------|
| Change identity after `EvidencePackage` construction | INV-06; HO-FORBID-05 |
| Delete evidence as handoff condition | HO-FORBID-02; Q-INV-03 |
| Rename evidence as snapshot | HO-FORBID-04; VAL-INV-09 |
| Alias quarantine path as snapshot `bulk_root` | HO-FORBID-14; ID-DRIFT-04 |

---

## Storage Review

### Canonical layout (consistent R1.8C → R2.5)

```text
{output_root}/                          ← default: C:\AI MARS STORAGE\ear\store\
    └── {acquisition_id}/
            ├── evidence/               ← R2 quarantine (R2.5)
            └── snapshots/
                  └── {snapshot_id}/    ← R1.8 mock Store (frozen)
```

### Visibility matrix

| Path | Operator | EAR (R2+) | R3 | R5 Validate | R4 Publish | Consumer |
|------|----------|-----------|-----|-------------|------------|----------|
| `evidence/` | Read/write policy | Write index (**Future**) | Read bulk | Read | **No** | **No** |
| `snapshots/{snapshot_id}/` | Read | Read (R1.8) | Write | Read | Read source | **After Publish only** |
| Git workspace | **Forbidden** for evidence bulk | **Forbidden** | — | — | — | — |
| OCPilot `project-sites\` | — | **Forbidden** at Store | — | — | Handoff | Consumer rules |

### Hidden conflicts

| Potential conflict | Finding |
|--------------------|---------|
| Evidence merged into snapshot tree | **Forbidden** — Q-INV-07; consistent |
| Evidence under git | **Forbidden** — Q-INV-06; ST-05 |
| Consumer reads quarantine via wrong `bulk_root` | **Risk documented** — HO-FORBID-14; mitigation in R2.6 |
| R2 changes R1.9 snapshot persist | **Forbidden** — IST-07; R2 adds `evidence/` only |
| Two `acquisition_id` sources in mock run | **Drift risk** — `build_mock_acquisition_id()` vs future evidence generator |

**Assessment:** No hidden storage conflicts in architecture; one **operational drift risk** (mock acquisition_id unification) deferred to R2.7.

---

## Validation Review

### R2 vs R5 boundary (consolidated from R2.4)

| Dimension | R2 (`EvidencePackageValidator`) | R5 (Validation Helpers) |
|-----------|--------------------------------|-------------------------|
| Input | `EvidencePackage` | Evidence (read) + candidate Snapshot Package |
| Checks | Structural + honesty at evidence boundary | Contract, quality L0–L3, redaction, publish gates |
| Output meaning | Safe input to Validate transform | Publish readiness / Validate report |
| Quality claims | **Forbidden** | **Required** at snapshot Validate |
| Pass implies Publish | **No** — VAL-INV-02 | Gate-dependent |

### Overlap prevention

| Concern | R2 | R5 | Overlap? |
|---------|----|----|----------|
| Partial run visible | `connector_status`, scope echo, artifact status | Snapshot `safe-unknown` | **Complementary** |
| Manifest | Index ref | Section adequacy L1+ | **Layered** — intentional |
| Operator approval | `operator_approval_ref` | `operator_approval` in snapshot metadata | **Rename at boundary** |
| Filesystem / hashes | Ref only (R2-V-15) | Section-level rules | **No overlap** |

### Consumer readiness

Owned by **R5 + R4** — R2 explicitly does not certify consumer readiness (R2.4, VAL-INV-02).

**Assessment:** Validation ownership is **internally consistent**; primary risk is **implementation drift** if engineers put R5 checks in R2 validator (mitigated by R2.4 R2-V-* catalog).

---

## Model Alignment Review

**File:** `runtime/shared/evidence_package_models.py` (read-only inspection)

### Structure vs R2.1

| Element | Charter / R2.1 | Code | Aligned? |
|---------|----------------|------|----------|
| `EvidenceIdentity` | 3× `str` | L34–47 | **Yes** |
| `EvidenceProvenance` | 4× `str`, no datetime parsing | L50–64 | **Yes** |
| `EvidenceScopeEcho` | approved + attempted tuples | L68–79 | **Yes** |
| `EvidenceArtifact` | type, ref, status | L82–99 | **Yes** |
| `EvidenceArtifactIndex` | count + artifacts | L102–113 | **Yes** |
| `EvidenceStatus` | `connector_status` only | L116–125 | **Yes** |
| `EvidencePackage` | aggregate + warnings/errors | L128–149 | **Yes** |
| Frozen dataclasses | Required | `frozen=True` | **Yes** |
| No validation in model | R2.1 L140 | Module docstring | **Yes** |

### R2.2 identity alignment

| Check | Result |
|-------|--------|
| No `evidence_id` | **Absent** |
| No `site_id`, `snapshot_id`, `package_quality_level` | **Absent** |
| `to_dict()` keys match field names | **Yes** |

### R2.3 artifact index alignment

| Check | Result |
|-------|--------|
| `ARTIFACT_TYPE_*` constants | L17–24 — **Present** |
| `ARTIFACT_STATUS_*` constants | L26–31 — **Present** |
| `CONNECTOR_STATUS_*` constants | L12–15 — **Present** |
| Docstring: opaque ref, no I/O | L82–87, module header | **Yes** |

### R2.4 validation targets

| Model element | R2-V checks implied | Supported? |
|---------------|---------------------|------------|
| All blocks present on aggregate | R2-V-01–R2-V-23 | **Yes** |
| Constants for enum allow-lists | R2-V-13, R2-V-16, R2-V-17 | **Yes** |
| Empty scope tuples default | R2-V-07 SAFE UNKNOWN | **Yes** — validator policy TBD |

### R2.5 quarantine alignment

| Check | Result |
|-------|--------|
| No quarantine path fields on model | **Correct** — path derived from `acquisition_id` + config |
| `artifact_ref` accommodates future storage pointer | Docstring L86 | **Yes** |

### R2.6 handoff alignment

| Check | Result |
|-------|--------|
| Handoff unit = full `EvidencePackage` | **Yes** |
| No `snapshot_id` on model | **Yes** |
| `to_dict()` not snapshot contract | **Yes** |

### Model gaps (documentation only — not blocking R2.7)

| Gap | Notes |
|-----|-------|
| Optional `scope_delta` field | Charter optional; not in model — derivable |
| Conditional `completed_at` | Model always has field; semantic enforcement in validator/generator |
| No `leg_ref` on artifacts | **Future** R2.8 — consistent |

**Conclusion:** Model remains **aligned** with R2.2–R2.6; **no model change required** for consolidation pass.

---

## Blind Spots

Documented only — **not solved** in this review.

| ID | Blind spot | Status | Collision risk |
|----|------------|--------|----------------|
| B-01 | `evidence_id` as package root identifier | **SAFE UNKNOWN** | High if introduced without amendment |
| B-02 | Exact `evidence/` index filenames (N-07) | **SAFE UNKNOWN** | Medium at R2.7 persist |
| B-03 | Production `acquisition_id` generation algorithm | **Partial** (mock helper only) | Medium at live path |
| B-04 | Mock `acquisition_id` divergence (evidence vs persist layout) | **Known** — R2.2 R-R2.2-04 | Medium at R2.7 |
| B-05 | Scope echo minimum cardinality (empty tuples) | **SAFE UNKNOWN** | Low — may mislead operators |
| B-06 | ISO 8601 format validation on timestamps | **SAFE UNKNOWN** | Low |
| B-07 | R5 strict ordering vs parallel with R3 | **SAFE UNKNOWN** | Low — handoff inputs identical either way |
| B-08 | 1:N `acquisition_id` → `snapshot_id` / hybrid merge | **SAFE UNKNOWN** / **Future** R2.8 | Medium for multi-leg acquisitions |
| B-09 | Evidence checksum registry before validation | **SAFE UNKNOWN** | Low |
| B-10 | Retention durations post-PC-08 | **SAFE UNKNOWN** | Low — operator policy |
| B-11 | Virus scan on ZIP evidence | **SAFE UNKNOWN** | Low |
| B-12 | R1.6 mock pipeline bypasses R2 model until R2.7 | **Known dual-model** | Medium — CLI still emits R1.6 shape |
| B-13 | `HandoffRecord` / `EvidenceValidationResult` serialization format | **SAFE UNKNOWN** | Low at R2.7 |
| B-14 | Whether R3 reads evidence from memory vs quarantine index only | **SAFE UNKNOWN** | Low — implementation choice |
| B-15 | Structured warning → `artifact_ref` link | **SAFE UNKNOWN** | Low |

---

## Recommendations

| ID | Recommendation | Owner | Priority |
|----|----------------|-------|----------|
| R-R2-CON-01 | Proceed to **R2.7 Evidence Package Generator** — architecture consolidation supports entry | R2.7 | **Now** |
| R-R2-CON-02 | Unify mock `acquisition_id` between evidence generator and `build_mock_acquisition_id()` at R2.7 | R2.7 | High |
| R-R2-CON-03 | Implement `EvidencePackageValidator` per R2-V-* — distinct from R5; may ship with R2.7 | R2.7 / R2.4 code | High |
| R-R2-CON-04 | Resolve N-07 index filename(s) at generator/persist — do not invent without note | R2.7 | High |
| R-R2-CON-05 | Migrate mock CLI off R1.6 `evidence_models.py` when generator lands | R2.7 | High |
| R-R2-CON-06 | Implement `HandoffContract` + `EvidenceQuarantineLayout` as contract modules (no I/O first) | R2.7 prep | Medium |
| R-R2-CON-07 | R3 charter must cite R2.6; R5 charter must cite R2.4 boundary | R3 / R5 planning | Medium |
| R-R2-CON-08 | Use terminology **"R2 structural validation"** vs **"EAR Validate (R5)"** in all R2.7+ docs | R2.7 | Medium |
| R-R2-CON-09 | Document empty scope echo mock policy at R2.7 | R2.7 | Low |
| R-R2-CON-10 | Do **not** add `evidence_id` without Architecture Amendment Charter | — | Standing |
| R-R2-CON-11 | Optional: align Implementation Charter `EvidenceStatusModel` → `EvidenceStatus` naming | Docs hygiene | Low |

---

## Risks

| Risk | Severity | Mitigation (already in chain) |
|------|----------|-------------------------------|
| R2 label confusion — snapshot sections implemented as R2 | High | R2-CHARTER non-goals; consolidation confirms |
| Quality inflation at evidence stage | High | VAL-INV-03; SC-05 |
| Evidence/snapshot path collision | Medium | Q-INV-01; sibling layout |
| R1.6 vs R2.1 dual-model drift in mock CLI | Medium | R-R2-CON-05 |
| R2 pass treated as Publish approval | High | VAL-INV-02; HO-INV-07 |
| Engineers add `evidence_id` | High | INV-02; B-01 |
| Validate terminology collision (R2 vs R5) | Medium | R-R2-CON-08 |

---

## SAFE UNKNOWN (consolidated)

| Topic | Status |
|-------|--------|
| Official JSON Schema for evidence package | **SAFE UNKNOWN** |
| Exact files inside `evidence/` (N-07) | **SAFE UNKNOWN** |
| `evidence_id` as package root | **SAFE UNKNOWN** — do not introduce |
| Hybrid merge / `leg_ref` / multi-package | **Future** R2.8 |
| 1:N `acquisition_id` → `snapshot_id` | **SAFE UNKNOWN** |
| Production `acquisition_id` algorithm | **SAFE UNKNOWN** (mock partial) |
| Scope echo minimum cardinality | **SAFE UNKNOWN** |
| ISO 8601 enforcement | **SAFE UNKNOWN** |
| R5 vs R3 ordering | **SAFE UNKNOWN** |
| Evidence checksum registry | **SAFE UNKNOWN** |
| Retention durations / virus scan | **SAFE UNKNOWN** |
| `HandoffRecord` serialization | **SAFE UNKNOWN** |

---

## Evidence index (consolidation)

| ID | Source |
|----|--------|
| E-R2-CON-01 | [R2-CHARTER-v1.md](R2-CHARTER-v1.md) |
| E-R2-CON-02 | [R2-IMPLEMENTATION-CHARTER-v1.md](R2-IMPLEMENTATION-CHARTER-v1.md) |
| E-R2-CON-03 | [R2.1-EVIDENCE-PACKAGE-MODEL-v1.md](R2.1-EVIDENCE-PACKAGE-MODEL-v1.md) |
| E-R2-CON-04 | [R2.2-EVIDENCE-IDENTITY-REVIEW-v1.md](R2.2-EVIDENCE-IDENTITY-REVIEW-v1.md) |
| E-R2-CON-05 | [R2.3-EVIDENCE-ARTIFACT-INDEX-v1.md](R2.3-EVIDENCE-ARTIFACT-INDEX-v1.md) |
| E-R2-CON-06 | [R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md) |
| E-R2-CON-07 | [R2.5-EVIDENCE-QUARANTINE-LAYOUT-v1.md](R2.5-EVIDENCE-QUARANTINE-LAYOUT-v1.md) |
| E-R2-CON-08 | [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) |
| E-R2-CON-09 | `runtime/shared/evidence_package_models.py` |

---

## Truth statement

| Claim | Accurate? |
|-------|-----------|
| R2 architecture chain reviewed end-to-end | **Yes** |
| R2 internally consistent with documented minor drift | **Yes** |
| Model aligned with R2.2–R2.6 without code change | **Yes** |
| R2.7 generator blocked by consolidation gaps | **No** |
| Consolidation introduces new architecture | **No** |
