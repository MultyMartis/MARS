# R5 Charter v1

**Type:** Program charter — **no** runtime code, **no** implementation, **no** validator code, **no** Publish in this phase  
**Phase:** R5 — EAR Validate Layer  
**Date:** 2026-06-06  
**Lane:** B — EAR Runtime Architecture  
**Prior phases:** R1 **COMPLETE**; R2 **COMPLETE WITH NOTES**; R3 **COMPLETE WITH NOTES**; [R3-READINESS-REVIEW-v1.md](R3-READINESS-REVIEW-v1.md); [R3-READINESS-DECISION-v1.md](R3-READINESS-DECISION-v1.md) — **READY FOR R5 WITH NOTES**  
**Decision companion:** [R5-DECISION-v1.md](R5-DECISION-v1.md)  
**Architecture sources:** [shared/external-access-runtime/](../../shared/external-access-runtime/)

---

## Purpose

Formally charter **R5 — EAR Validate Layer** before any R5 engineering work begins. R5 closes the gap between R3 **candidate** Snapshot Package and **certified** snapshot contract compliance, quality possession, and publish readiness per architecture gates.

**R5 delivers:** mission, scope, non-goals, authoritative inputs/outputs, quality ownership, validation category charter, R5→R4 publish boundary, success criteria, stop conditions — **charter only**.

**R5 does not deliver:** Validate automation implementation, Publish execution, snapshot assembly, evidence generation, acquisition, or consumer integration.

---

## Mission

### Why R5 exists

EAR separates **acquisition-internal evidence** from **consumer-facing snapshots**, and further separates **candidate assembly** from **contract certification**. R3 delivers an OpenCart section tree with honest `package_quality_level: 0` default — structural population, not certification ([R3-CHARTER-v1.md](R3-CHARTER-v1.md) § R3 → R5 Boundary).

Without R5, EAR cannot:

- Certify that a candidate snapshot satisfies [EAR-SNAPSHOT-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-CONTRACT-v1.md) and [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md)
- Assign honest `package_quality_level` L0–L3 per [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md)
- Enforce redaction before consumer paths
- Produce a Validate report and Publish eligibility recommendation for R4 and operator HITL
- Fail closed on uncertainty per [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md)

Per [EAR-SNAPSHOT-LIFECYCLE-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-LIFECYCLE-v1.md): **Validate** transforms evidence into governed snapshot sections and certifies contract compliance before Store/Publish. R5 owns the **certification** half of that stage; R3 owns **assembly**.

### Why R3 pass is insufficient

| Reason | Authority |
|--------|-----------|
| **Different artefact stage** — R3 produces **candidate**; R5 certifies **validated** | R3.6 Store Boundary Review — three snapshot states |
| **Assembly eligibility ≠ contract adequacy** — R3 checks skeleton presence; R5 checks section possession for level claims | [R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md](R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md) VB-R3-01, VB-R3-07 |
| **Quality uncertified at assembly** — R3 enforces `package_quality_level: 0`; R5 assigns certified level | HO-FORBID-06; R3-V-07 |
| **Safe-unknown presence ≠ completeness** — R3 proves gaps were not suppressed; R5 reviews adequacy for certify level | VB-R3-08 |
| **No redaction enforcement** — R3 must not copy secrets; R5 enforces redaction policy on candidate | R2.4 § R5 Scope; VB-R3-12 |
| **No publish readiness** — R3 explicit non-output; R5 owns Validate report and gate G2–G4 inputs | R3 charter non-goals |
| **Evidence chain not re-certified** — R2 pass is pre-handoff; R5 may read evidence for provenance consistency | VAL-INV-01; HO-INV-06 |

**Critical invariant:** R3 assembly pass **≠** R5 Validate pass ([R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md) VAL-INV-01; [R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md](R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md) VB-R3-01).

### Why Publish must not bypass Validate

| Reason | Authority |
|--------|-----------|
| **Lifecycle rule** — Acquire → **Validate** → Store → Publish; no consumer handoff without Validate | EAR-SNAPSHOT-LIFECYCLE-v1 |
| **Secrets risk** — pre-redaction bulk may exist in quarantine; candidate may carry PII until R5 redaction review | EAR-EVIDENCE-PACKAGE-v1; EAR-STORAGE-MODEL-v1 |
| **Quality inflation** — Publish without Validate could expose uncertified level claims to consumers | EAR-OPENCART-QUALITY-MAPPING-v1 |
| **Fail closed** — ambiguous validation blocks Publish, not best-effort intake | EAR-READINESS-GATES-v1 |
| **Evidence not consumer input** — Publish promotes **snapshot** only; Validate is mandatory transform gate | R2.6 HO-FORBID-07, HO-FORBID-12 |
| **Operator HITL** — Validate/Publish transitions require human authority | EAR-READINESS-GATES-v1 § Gate philosophy |

R4 **Publish** consumes R5 **recommendation** — it does **not** substitute for Validate ([R2.4](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md) VAL-INV-02).

### Pipeline connection (authoritative)

```text
R2 Evidence Package
        ↓
R3 Candidate Snapshot Package
        ↓
R5 Validate  ← this charter
        ↓
R4 Publish
        ↓
Consume (consumer programs)
```

**Authoritative program label:** Architecture backlog **R5 = Validation Helpers** — EAR Validate Layer; human HITL remains mandatory for pilot ([EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R5).

---

## Scope

### In scope (R5 program — charter defines; implementation follows R5 Implementation Charter)

| # | Work area | Boundary |
|---|-----------|----------|
| 1 | **Candidate snapshot validation** | Contract compliance on R3.1 `SnapshotPackage` — stored or in-memory candidate |
| 2 | **Contract compliance assessment** | OpenCart spec + parent snapshot contract — adequacy, not assembly |
| 3 | **`package_quality_level` certification** | L0–L3 possession per quality mapping — **only** R5 may certify |
| 4 | **L0/L1/L2/L3 possession assessment** | Section-level possession rules — charter defines ownership; rules in Implementation Charter |
| 5 | **`safe-unknown` interpretation** | Completeness and honesty review for declared certify level — distinct from R3 propagation |
| 6 | **Redaction review** | PII/secrets detection policy on candidate snapshot — enforcement before consumer paths |
| 7 | **Publish readiness assessment** | Gate G2–G4 checklist semantics per readiness gates — **recommendation only** |
| 8 | **Validation report generation** | Distinct artefact: pass/fail/partial, blockers, certified level, Publish eligibility |
| 9 | **Evidence provenance chain read** | Read-only correlation with R2 evidence for consistency — **not** R2 structural re-validation |
| 10 | **Validated snapshot state definition** | Lifecycle stage between candidate and published — charter only |

### Out of scope (explicit non-goals)

| # | Non-goal | Owner / phase |
|---|----------|---------------|
| 1 | **Evidence generation** | **R2** |
| 2 | **Evidence persistence / quarantine writes** | **R2** |
| 3 | **Snapshot assembly / section population** | **R3** |
| 4 | **Candidate `package_quality_level: 0` default** | **R3** |
| 5 | **Acquisition / connector execution** | **R1** + Execution Authorization |
| 6 | **Publish execution** | **R4** |
| 7 | **Consumer delivery / OCPilot intake** | **R4** + consumer programs |
| 8 | **Store layout redesign** | **Frozen** at R1.9 |
| 9 | **R2 structural evidence validation** | **R2** — R5 reads evidence, does not replace R2 validator |
| 10 | **R3 assembly eligibility checks** | **R3** — preconditions only, not duplicated as certification |
| 11 | **Unattended production gate** | **Non-goal** per backlog — human Validate sign-off for pilot |
| 12 | **Automated redaction engine product** | Future / operator policy beyond chartered rules |
| 13 | **Normative JSON Schema / ZIP layout files** | **SAFE UNKNOWN** |
| 14 | **Architecture redesign** | Amendment charter only |
| 15 | **Live SFTP / SITE-001 / PILOT execution** | Execution Authorization |

Per backlog § R5 non-goals: no governance enforcement product; no replacement of human Validate sign-off for pilot.

---

## Inputs

### Authoritative R5 input set

R5 Validate may consume **only** the following as primary validation targets and supporting context:

| # | Input | Source | R5 use |
|---|-------|--------|--------|
| I-R5-01 | **Candidate Snapshot Package** | R3.5 `build_candidate_snapshot_package()` / Store read | Primary validation target — OpenCart section tree |
| I-R5-02 | **`safe-unknown/` section** | R3.4 propagation | Gap completeness review for certify level; honesty vs silent omission |
| I-R5-03 | **`acquisition-log/` section** | R3 assembly from R2 provenance | Audit correlation; scope and channel consistency |
| I-R5-04 | **Snapshot identity** | R3.2 — `snapshot_id`, `site_id`, `acquisition_id`, contract ids | Identity category validation; drift prevention |
| I-R5-05 | **OpenCart section tree** | R3.1 aggregate — all 10 sections | Structure, possession, consistency categories |
| I-R5-06 | **R3 assembly eligibility result** | `validate_candidate_snapshot_package()` when supplied | Precondition — candidate structurally eligible for R5 input |
| I-R5-07 | **Evidence Package (read-only)** | R2.1 / quarantine index | Provenance chain; connector status vs snapshot honesty — **not** re-run R2 validator |
| I-R5-08 | **R2 structural validation result** | `EvidenceValidationResult` when supplied | Precondition flag — invalid evidence undermines Validate context |
| I-R5-09 | **Identity Continuity Record** | R3 `build_identity_continuity_record()` when present | Audit sidecar — correlation only |
| I-R5-10 | **Storage path binding** | `{output_root}/{acquisition_id}/snapshots/{snapshot_id}/` when stored | Store layout verification input — **no** layout redesign |
| I-R5-11 | **Target certify level** | Operator / Request declaration | Possession assessment target — may downgrade, not inflate |
| I-R5-12 | **Architecture gate definitions** | EAR-READINESS-GATES-v1, EAR-OPENCART-READINESS-CHECKLIST-v1 | Readiness category charter inputs |

### Derived inputs (not separate ownership)

| Derived input | Derivation | Notes |
|---------------|------------|-------|
| Evidence quarantine refs | R2 artifact index + `{acquisition_id}/evidence/` | Read-only for redaction/corroboration — not consumer paths |
| Prior snapshot reference | Snapshot metadata when partial rerun | Inheritance rules at Validate — **SAFE UNKNOWN** detail |
| Operator approval | `metadata.operator_approval` | Distinct from evidence `operator_approval_ref` — R5 validates snapshot field |

### Explicit non-inputs (R5 must not treat as validation authority)

| Artefact | Reason | Owner |
|----------|--------|-------|
| Raw connector output / listing | Pre-evidence; not snapshot contract | R1 |
| Evidence quarantine bulk as publish target | Not consumer input | R4 |
| R1.7 flat `SnapshotPackage` (legacy mock) | Not R3 contract path — migration debt | R1.7 |
| Published snapshot reference | Downstream of R4 | R4 |
| Consumer `project-sites\` paths | Post-Publish only | R4 |
| R3 assembly success alone | Precondition ≠ Validate pass | R3 |
| R2 structural pass alone | Pre-handoff ≠ snapshot certification | R2 |
| Live credentials | External secrets | Operator |
| OCPilot baseline diff execution | Consumer program | OCPilot |

---

## Outputs

### Authoritative R5 output set

| # | Output | Consumer | Notes |
|---|--------|----------|-------|
| O-R5-01 | **Validation Result** | Operator; pipeline; R4 pre-check | Pass / fail / partial; distinct from R2/R3 eligibility results |
| O-R5-02 | **Validate Report** | Operator HITL; audit trail | Structured findings by validation category; blockers and warnings |
| O-R5-03 | **Certified `package_quality_level`** | Store metadata update; R4 Publish | L0–L3 — **only** output that may change quality from candidate L0 |
| O-R5-04 | **Publish Eligibility Recommendation** | **R4** Publish; operator | Allowed / blocked / conditional — **recommendation only** |
| O-R5-05 | **Gate checklist status** | Operator | G1–G4 semantics mapped to findings — not gate automation product |
| O-R5-06 | **Redaction findings** | Operator; R4 pre-Publish | Secrets/PII blockers — fail closed |
| O-R5-07 | **Validated snapshot state marker** | Store lifecycle | Candidate → **validated** transition — exact marker **SAFE UNKNOWN** at charter |
| O-R5-08 | **Possession assessment record** | Audit; consumer (post-Publish via snapshot metadata) | Which sections satisfied which level requirements |

### Explicit non-outputs

| Output | Owner |
|--------|-------|
| Published snapshot / consumer reference | **R4** |
| `published_at`, publish metadata | **R4** |
| OpenCart section population or mutation | **R3** |
| Evidence Package writes | **R2** |
| Consumer reports / OCPilot Run 5 execution | Consumer programs |
| Automatic Publish without HITL | **Forbidden** |

### R5 does not publish

R5 **never** writes to consumer paths, **never** sets publish metadata, **never** promotes snapshot to consumer-visible reference. R5 emits **Publish Eligibility Recommendation** only; **R4** executes Publish after operator approval ([EAR-SNAPSHOT-PUBLISHING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-PUBLISHING-v1.md)).

```text
R5 Validate
        ↓
Validation Result + Validate Report + Certified level + Publish Eligibility Recommendation
        ↓
Operator HITL (mandatory for pilot)
        ↓
R4 Publish  ← R5 stops here
```

---

## Quality Ownership

Normative source: [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md). **Ownership only** — possession rules deferred to R5 Implementation Charter.

### Candidate vs certified quality

| Stage | `package_quality_level` | Who sets | Meaning |
|-------|-------------------------|----------|---------|
| **R3 candidate assembly** | **0** (default) | **R3** | Honest placeholder — **not** certification |
| **R5 Validate pass** | **0–3** (certified) | **R5** | Possession-assessed honest claim |
| **R4 Publish** | Frozen published claim | **R4** + operator | Must match R5 certified level — no inflation |

**Rule:** R3 may create candidate quality **0** only. **Only R5** may certify possession and assign certified `package_quality_level` ≥ 0 for Validate/Store/Publish chain (HO-FORBID-06; VB-R3-06).

### Level ownership matrix

| Level | Name | R3 role | R5 role |
|-------|------|---------|---------|
| **L0** | Identity only | Assembles min metadata, environment, acquisition-log, safe-unknown listing all non-acquired sections | **Certifies** L0 possession — identity, audit, honesty |
| **L1** | Identity + structure | Populates or gaps: file-manifest, database-metadata, seo-structure, theme-info | **Certifies** L1 possession — version proof, manifest subset, DB/SEO/theme adequacy or honest safe-unknown |
| **L2** | + extensions | Optional placeholders / safe-unknown at R3 L1 target | **Certifies** L2 possession — extension-inventory, ocmod-inventory adequacy |
| **L3** | Full read-only audit | Not R3 L1 engineering target | **Certifies** L3 possession — comprehensive manifest, residual safe-unknown only |

### Possession principles (charter — not rules)

| Principle | Owner |
|-----------|-------|
| **Possess** = collected, assembled, **and accepted at Validate** | **R5** certifies |
| **Honest claim** = published level matches Validate outcome; gaps in safe-unknown | **R5** enforces at Validate; **R4** freezes at Publish |
| **Downgrade allowed** | **R5** + operator — target level may be lowered; inflation forbidden |
| **Max level from possession** | **R5** — quality mapping matrix is normative input |
| **Partial acquisition** | Connector status informs safe-unknown; **R5** determines max certifiable level |

### Quality inflation prevention

| ID | Rule | Authority |
|----|------|-----------|
| Q-INV-R5-01 | R3 `package_quality_level: 0` **≠** R5 certified level | VB-R3-06 |
| Q-INV-R5-02 | Populated section **≠** level possession without R5 assessment | VB-R3-07 |
| Q-INV-R5-03 | Manifest ref in evidence index **≠** L1 file-manifest possession | VAL-INV-04, VAL-INV-12 |
| Q-INV-R5-04 | `connector_status: success` **≠** snapshot completeness | VAL-INV-05 |
| Q-INV-R5-05 | R5 **fail closed** on Publish when possession uncertain | EAR-READINESS-GATES-v1 |

---

## Validation Categories

R5 organizes Validate work into **categories** — each defines **ownership and purpose** only. **No implementation rules** in this charter; rule IDs belong in R5 Implementation Charter.

### Category overview

| Category | Purpose | Primary inputs | R5 owns |
|----------|---------|----------------|---------|
| **Identity** | Snapshot and site identity integrity; contract version; acquisition correlation | I-R5-04, metadata, acquisition-log | **Yes** — R3 creates ids; R5 certifies correctness |
| **Structure** | OpenCart section tree completeness vs spec skeleton; forbidden field absence | I-R5-05, I-R5-01 | **Yes** — distinct from R3 assembly skeleton check |
| **Possession** | Section content adequacy for target level; corroboration where required | Section payloads, safe-unknown | **Yes** — exclusive owner |
| **Quality** | Map possession to L0–L3; downgrade paths; inflation detection | Quality mapping, target level | **Yes** — exclusive certifier |
| **Redaction** | Secrets/PII in candidate; pre-consumer path safety | Candidate serialization, bulk refs | **Yes** — R3 avoids copy; R5 enforces |
| **Readiness** | Gate G2–G4 checklist semantics; Publish eligibility | Readiness gates, Validate findings | **Yes** — recommendation; R4 executes Publish |
| **Consistency** | Evidence ↔ snapshot provenance alignment; identity continuity | I-R5-07, I-R5-03, continuity record | **Yes** — read-only evidence use |

### Category boundaries (overlap prevention)

| Category | R2 owns | R3 owns | R5 owns |
|----------|---------|---------|---------|
| **Identity** | Evidence identity block | `snapshot_id` creation; site_ref→site_id | Snapshot identity certification; operator_approval on metadata |
| **Structure** | Evidence shape | Candidate section skeleton; assembly eligibility | Contract adequacy beyond skeleton |
| **Possession** | Artifact index ref presence | Section population or explicit safe-unknown | Level-specific section adequacy |
| **Quality** | **Forbidden** on evidence | Candidate L0 only | L0–L3 certification |
| **Redaction** | Evidence serialization policy | Must not copy secrets into sections | Candidate redaction review |
| **Readiness** | — | — | Validate report; Publish eligibility recommendation |
| **Consistency** | Connector status honesty | safe-unknown propagation | Evidence↔snapshot semantic alignment |

### Terminology (mandatory disambiguation)

Per N-R3R-08 / N-R3-07:

| Term | Program | Meaning |
|------|---------|---------|
| **R2 structural validation** | R2 | Evidence Package shape and honesty |
| **R3 assembly eligibility** | R3 | Candidate SnapshotPackage structural integrity |
| **R5 EAR Validate** | R5 | Snapshot contract certification, quality, redaction, publish readiness |
| **R5 pass** | R5 | Validate certification — **≠** R3 pass |
| **Publish approval** | R4 + operator | **≠** R5 pass alone |

---

## Publish Boundary

### R5 → R4 relationship

```text
┌─────────────────────────────────────────────────────────┐
│  R5 Validate Layer                                       │
│  • Contract + quality + redaction assessment             │
│  • Certified package_quality_level                       │
│  • Validate Report                                       │
│  • Publish Eligibility Recommendation                    │
│  • NEVER publishes                                       │
└───────────────────────────┬─────────────────────────────┘
                            │
                            ▼  Recommendation + HITL
┌─────────────────────────────────────────────────────────┐
│  R4 Publish Layer                                        │
│  • Reads validated snapshot + R5 recommendation          │
│  • Operator publish approval                             │
│  • Consumer-visible reference promotion                  │
│  • Publish metadata (published_at, etc.)                 │
└─────────────────────────────────────────────────────────┘
```

### Gate mapping (conceptual — R5 input to R4)

| Gate | R5 role | R4 role |
|------|---------|---------|
| **G1** Acquire → Validate | R5 may assume G1 satisfied when candidate + acquisition-log present; R5 does not run acquisition | — |
| **G2** Validate → Store | **R5 owns** pass/fail semantics | Store write may follow G2 — layout frozen R1.8 |
| **G3** Store → Publish | **R5 contributes** readiness findings | R4 confirms storage placement |
| **G4** Publish → Consumer | **R5 emits** Publish Eligibility Recommendation | **R4 owns** execution |

### R5 prohibitions at Publish boundary

| Prohibition | Authority |
|-------------|-----------|
| R5 **must not** execute Publish | R4 ownership |
| R5 **must not** write consumer paths | EAR-STORAGE-MODEL-v1 |
| R5 **must not** set `published_at` / publish markers | R4 ownership |
| R5 **must not** bypass operator HITL for pilot | Backlog § R5 non-goals |
| Validate pass **≠** Publish approval | VAL-INV-02; VB-R3-02 |
| Failed/blocked R5 **must** block Publish recommendation | EAR-READINESS-GATES-v1 fail closed |

---

## Ownership Boundary

### Concern → Owner matrix

| Concern | R2 | R3 | R5 | R4 | Operator | Consumer |
|---------|----|----|----|----|----------|----------|
| Evidence Package | **Owns** | Reads | Reads (Validate chain) | — | Inspects quarantine | **No access** |
| Candidate snapshot assembly | — | **Owns** | Reads | — | Inspects | **No access** |
| R2 structural validation | **Owns** | Requires | — | — | — | — |
| R3 assembly eligibility | — | **Owns** | Precondition | — | — | — |
| EAR Validate / certification | — | — | **Owns** | Input | HITL | — |
| `package_quality_level` certification | Forbidden | Candidate L0 | **Owns** | Matches validated | Override/downgrade | Reads published |
| Validate report | — | — | **Owns** | Input | Reviews | — |
| Publish eligibility recommendation | — | — | **Owns** emit | **Owns** act | Approves | — |
| Publish execution | — | — | **Forbidden** | **Owns** | Approves | Receives |
| Redaction enforcement (snapshot) | Policy on evidence | Avoid copy | **Owns** review | Pre-Publish check | Policy | Never secrets |
| Live acquisition | R1 skeleton | Forbidden | — | — | Authorization | — |

### Overlap prevention

| Boundary | Rule |
|----------|------|
| R2 ↔ R5 | R5 **reads** evidence for consistency; **does not** re-implement R2-V-* checks except ingest sanity |
| R3 ↔ R5 | R3 **never** certifies; R5 **never** populates sections |
| R5 ↔ R4 | R5 **recommends**; R4 **publishes** |
| R5 ↔ Operator | Operator owns external paths, final Validate/Publish sign-off, target level declaration |

---

## Success Criteria

R5 **program** (EAR Validate Layer charter) is **complete** when:

| ID | Criterion | Verification |
|----|-----------|--------------|
| SC-R5-01 | Mission answers: why R5 exists, why R3 pass insufficient, why Publish must not bypass Validate | § Mission |
| SC-R5-02 | Scope lists all eight R5 responsibilities and explicit non-goals | § Scope |
| SC-R5-03 | Authoritative inputs I-R5-01–12 and non-inputs documented | § Inputs |
| SC-R5-04 | Outputs O-R5-01–08 documented; R5 does not publish stated | § Outputs |
| SC-R5-05 | Quality ownership L0–L3 — R3 candidate L0; R5 sole certifier | § Quality Ownership |
| SC-R5-06 | Validation categories defined with ownership — no implementation rules | § Validation Categories |
| SC-R5-07 | Publish boundary R5→Recommendation→R4 explicit | § Publish Boundary |
| SC-R5-08 | R3 readiness notes N-R3R-01–08 reflected | § Mission; Terminology |
| SC-R5-09 | R2.4 / R3.6 validation boundaries referenced — no overlap | § Category boundaries |
| SC-R5-10 | R5 Implementation Charter **READY** as next artifact | Gate transition |
| SC-R5-11 | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) and [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) updated | Program navigation |

**Engineering acceptance (post-implementation — R5 Implementation Charter, not this document):**

| ID | Criterion | Source |
|----|-----------|--------|
| IAC-R5-01 | Operator can run Validate helpers on candidate snapshot | Backlog § R5 acceptance |
| IAC-R5-02 | Validate report distinguishes pass/fail/partial with blockers | Backlog § R5 outputs |
| IAC-R5-03 | Certified level honest per quality mapping | EAR-OPENCART-QUALITY-MAPPING-v1 |
| IAC-R5-04 | Publish Eligibility Recommendation fail closed on mandatory failures | EAR-READINESS-GATES-v1 |
| IAC-R5-05 | R5 does not execute Publish | This charter § Publish Boundary |
| IAC-R5-06 | Consumes R3.1 `SnapshotPackage` — not R1.7 legacy | N-R3R-03 |

**Explicitly excluded from R5 charter success:** Validator code, Publish implementation, Store redesign, live acquisition.

---

## Stop Conditions

Stop or escalate **before** R5 implementation if:

| ID | Condition | Action |
|----|-----------|--------|
| ST-R5-01 | Charter scope includes **Publish execution** as R5 deliverable | **STOP** — reclassify as R4 |
| ST-R5-02 | Charter scope includes **snapshot assembly** or section writers | **STOP** — reclassify as R3 |
| ST-R5-03 | Charter scope includes **evidence generation** or quarantine persist | **STOP** — reclassify as R2 |
| ST-R5-04 | Charter allows **Publish without Validate** or R3 pass as Publish gate | **STOP** — violates lifecycle |
| ST-R5-05 | Charter assigns **`package_quality_level` ≥ 1 certification to R3** | **STOP** — quality inflation |
| ST-R5-06 | Charter requires **SITE-001**, **PILOT-001**, live SFTP, or connected acquisition | **STOP** — Execution Authorization |
| ST-R5-07 | Charter requires **Store / persistence redesign** contradicting R1.9 | **STOP** — architecture amendment |
| ST-R5-08 | Charter replaces **human Validate HITL** with unattended production gate | **STOP** — backlog non-goal |
| ST-R5-09 | Implementation proposed without **R5 Implementation Charter** + human gate | **STOP** — per R1/R2/R3 gate pattern |
| ST-R5-10 | Charter attempts to **redesign R1/R2/R3** contracts | **STOP** — amendment charter |
| ST-R5-11 | Charter includes **OCPilot integration** as R5 deliverable | **STOP** — consumer program |
| ST-R5-12 | Validate bulk placed under **git workspace** or consumer paths | **STOP** — EAR-STORAGE-MODEL |

### Out-of-scope conditions (ongoing)

Work is **out of R5** if it matches any row in **Non-Goals** or:

- Populates OpenCart sections from evidence
- Executes Publish or writes consumer references
- Generates or mutates Evidence Package
- Certifies quality at R3 assembly boundary
- Enables network acquisition in R5 charter scope

---

## Pipeline position

```text
Acquire (R1 connector / mock)
        ↓
Evidence Package (R2.1–R2.7)
        ↓
R2 structural validation (R2.4)
        ↓
R2.6 HANDOFF (read-only on evidence)
        ↓
R3 Snapshot Assembly — candidate OpenCart sections
        ↓
R3 assembly eligibility (R3 validator)
        ↓
╔═══════════════════════════════════════╗
║  R5 EAR Validate (this charter)       ║
║  Certification + Validate Report      ║
║  Publish Eligibility Recommendation   ║
╚═══════════════════════════════════════╝
        ↓
Store (validated state — R1.8 layout frozen)
        ↓
R4 Publish + operator HITL
        ↓
Consume (consumer programs)
```

**Ordering note:** Architecture allows R5 helpers to be **designed** in parallel with late R3 work once R2 shape stable ([R2-CHARTER-v1.md](R2-CHARTER-v1.md) § SAFE UNKNOWN). **Canonical runtime order** for certification: R3 candidate **then** R5 Validate **then** R4 Publish.

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| R5 label confusion — engineers implement Publish or assembly as R5 | High | Mission + Non-Goals; Publish Boundary § |
| R3 assembly pass treated as Validate pass | High | SC-R5-01; VB-R3-01; terminology § |
| Quality inflation at Validate without possession review | High | Quality Ownership; Q-INV-R5-* |
| R5 duplicates R2 structural checks causing drift | Medium | Inputs § — read evidence, don't replace R2 |
| R5 duplicates R3 assembly eligibility as certification | Medium | Category boundaries; R3.6 reference |
| Publish before redaction review | High | Redaction category; fail closed |
| Unattended gate bypassing operator HITL | High | Non-goals ST-R5-08 |
| In-memory candidate only — no Store path for Validate | Medium | N-R3R-04; IAC-R5-06 notes |
| Dual snapshot models (R1.7 vs R3.1) during R5 early work | Medium | N-R3R-03; consume R3.1 only |
| Validate terminology collision (R2/R3/R5) | Medium | Terminology § mandatory in all R5 docs |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Exact Validate report serialization format | R5 Implementation Charter |
| Validated snapshot Store state marker / sidecar | R5 Implementation Charter |
| Per-category validation rule IDs (R5-V-*) | R5 Implementation Charter — **not** this charter |
| Official JSON Schema for Validate report | Not in repo |
| ISO 8601 format enforcement on snapshot timestamps | R3.6 / R5 Implementation — deferred |
| R5 strict ordering vs parallel design with R3 | Backlog allows parallel **design**; runtime cert order canonical |
| Whether R5 reads candidate from memory vs Store only | N-R3R-04 — both allowed at implementation |
| Production redaction scan depth (heuristic vs full) | Operator policy; charter notes fail closed |
| Human HITL UI / workflow product | Outside runtime — checklist helpers only |
| Validated snapshot immutability rules beyond R1.9 | **SAFE UNKNOWN** — R5 may define marker only |
| Gate automation vs checklist reminders | Backlog: helpers not autonomous gate |
| Contract-path Store persist adapter timing | R3 debt — R5-adjacent |
| Bulk expansion prerequisite for live L1+ Validate | HO-ALLOW-10 not implemented — N-R3R-07 |
| 1:N `acquisition_id` → `snapshot_id` Validate policy | Architecture SAFE UNKNOWN |
| Hybrid multi-package Validate | Future R2.8 |
| Whether empty `safe-unknown` ever valid at L3 | R5 certifies emptiness — policy at implementation |
| OCPilot-specific Validate extensions | Consumer program — not R5 core |

---

## Planning notes (carried from R3)

| Note | Action |
|------|--------|
| N-R3R-01 | R5 Charter restates VB-R3-01 — R3 pass ≠ R5 pass — **satisfied** § Mission |
| N-R3R-02 | R5 owns quality, redaction, publish readiness, Validate report — **satisfied** § Scope |
| N-R3R-03 | R5 consumes R3.1 `SnapshotPackage` — **satisfied** § Inputs; IAC-R5-06 |
| N-R3R-04 | In-memory candidate acceptable until Store adapter — **satisfied** § SAFE UNKNOWN |
| N-R3R-05 | Retain `--contract-evidence` / `--contract-snapshot` — standing; not R5 charter scope |
| N-R3R-06 | Do not delete R1.6 without migration — standing |
| N-R3R-07 | Store persist + bulk expansion — R5-adjacent debt |
| N-R3R-08 | Disambiguate R2/R3/R5 Validate terms — **satisfied** § Terminology |

---

## Evidence index

| ID | Source |
|----|--------|
| C-R5-01 | [R3-READINESS-REVIEW-v1.md](R3-READINESS-REVIEW-v1.md) |
| C-R5-02 | [R3-READINESS-DECISION-v1.md](R3-READINESS-DECISION-v1.md) |
| C-R5-03 | [R3-CHARTER-v1.md](R3-CHARTER-v1.md) § R3 → R5 Boundary |
| C-R5-04 | [R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md](R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md) |
| C-R5-05 | [R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md) |
| C-R5-06 | [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) |
| C-R5-07 | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md) |
| C-R5-08 | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| C-R5-09 | [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md) |
| C-R5-10 | [EAR-SNAPSHOT-LIFECYCLE-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-LIFECYCLE-v1.md) |
| C-R5-11 | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R5 |

---

## Cross-references

| Document | Use |
|----------|-----|
| [R5-DECISION-v1.md](R5-DECISION-v1.md) | Charter gate decision |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Program status |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation |
