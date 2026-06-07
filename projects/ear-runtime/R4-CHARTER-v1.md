# R4 Charter v1

**Type:** Program charter — **no** runtime code, **no** implementation, **no** publish engine, **no** CLI, **no** persistence implementation in this phase  
**Phase:** R4 — EAR Publish Layer  
**Date:** 2026-06-07  
**Lane:** B — EAR Runtime Architecture  
**Prior phases:** R1 **COMPLETE**; R2 **COMPLETE WITH NOTES**; R3 **COMPLETE WITH NOTES**; R5 **COMPLETE WITH NOTES**; [R5-READINESS-REVIEW-v1.md](R5-READINESS-REVIEW-v1.md); [R5-READINESS-DECISION-v1.md](R5-READINESS-DECISION-v1.md) — **READY FOR R5 IMPLEMENTATION WITH NOTES**; R5.9 architecture **APPROVED**  
**Decision companion:** [R4-DECISION-v1.md](R4-DECISION-v1.md)  
**Architecture sources:** [shared/external-access-runtime/](../../shared/external-access-runtime/)

---

## Purpose

Formally charter **R4 — EAR Publish Layer** before any R4 engineering work begins. R4 closes the gap between R5 **validated** snapshot certification and **consumer-visible** published snapshot reference per architecture gates.

**R4 delivers:** mission, scope, non-goals, authoritative inputs/outputs, publish lifecycle, Published Snapshot definition, ownership matrix, consumer boundary, R5→R4 boundary, success criteria, stop conditions — **charter only**.

**R4 does not deliver:** Publish automation implementation, Validate execution, snapshot assembly, evidence generation, acquisition, or consumer program integration.

---

## Mission

### Why R4 exists

EAR separates **acquisition-internal evidence** from **consumer-facing snapshots**, **candidate assembly** from **contract certification**, and **certification** from **consumer visibility**. R5 delivers Validate certification, quality possession, redaction review, and Publish Eligibility Recommendation — but **never** promotes a snapshot to consumer intake ([R5-CHARTER-v1.md](R5-CHARTER-v1.md) § Publish Boundary).

Without R4, EAR cannot:

- Execute the **Publish** gate between Store and Consume per [EAR-SNAPSHOT-LIFECYCLE-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-LIFECYCLE-v1.md)
- Produce a **consumer-visible** published snapshot reference per [EAR-SNAPSHOT-PUBLISHING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-PUBLISHING-v1.md)
- Record `published_at`, `published_by`, and `consumer_target` without mutating validated content
- Enforce that consumers intake **published** snapshots only — not candidates, quarantine, or stored-unpublished artefacts
- Satisfy Gate G4 (Publish → Consume) per [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md)
- Freeze the R5-certified `package_quality_level` as the published claim — no inflation at Publish

Per [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) § Store vs Publish: **Store** places validated artefacts immutably for operator/EAR use; **Publish** is the explicit gate that permits consumer intake. R4 owns the **Publish** half of that distinction; R5 owns **Validate**; R3 owns **candidate assembly**.

### Why Validate does not Publish

| Reason | Authority |
|--------|-----------|
| **Lifecycle separation** — Validate certifies contract compliance; Publish grants consumer visibility | EAR-SNAPSHOT-LIFECYCLE-v1; EAR-SNAPSHOT-PUBLISHING-v1 |
| **Different artefacts** — R5 emits `ValidationResult`, `ValidateReport`, `PublishEligibilityRecommendation`; R4 emits published reference and publish metadata | R5-CHARTER O-R5-01–08; R5.6 PE-INV-R5-01 |
| **Advisory vs execution** — R5 **recommends** Publish eligibility; R4 **executes** Publish after operator HITL | R5.6 § Recommendation semantics; VAL-INV-02 |
| **Quality ownership** — R5 **certifies** possession; R4 **freezes** certified level — does not re-assess | R5.3; Q-INV-R5-01–05 |
| **Redaction ownership** — R5 **enforces** redaction review on candidate; R4 **confirms** pre-Publish gate satisfied — does not re-scan | R5.4; VB-R5-12 |
| **Fail closed at wrong layer** — Validate failure blocks recommendation; Publish without Validate violates lifecycle | EAR-READINESS-GATES-v1; ST-R5-04 |
| **Operator HITL placement** — Validate sign-off and Publish approval are distinct human gates | Backlog § R5 non-goals; R5.6 SC-R5.6-04 |
| **Evidence chain** — Validate reads evidence for consistency; Publish promotes **snapshot only** — never quarantine bulk | R2.6 HO-FORBID-07, HO-FORBID-12 |

**Critical invariant:** R5 Validate pass **≠** Publish approval. R5 Publish Eligibility Recommendation **≠** Publish execution ([R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md](R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md) PE-INV-R5-01; VB-R3-02).

### Why Publish does not Validate

| Reason | Authority |
|--------|-----------|
| **Ownership** — Contract certification, quality possession, redaction review, and publish readiness assessment are **R5** exclusive | R5-CHARTER § Quality Ownership; VB-R5-07 |
| **Artefact stage** — R4 consumes **validated** snapshot outputs; re-validation at Publish would duplicate R5 and blur boundaries | R3.6 VB-R3-01; R5.8 VB-R5-01 |
| **No quality certification at Publish** — R4 freezes R5-certified level; assigning or upgrading quality at Publish is **forbidden** | R5.3 candidate vs certified matrix |
| **No section mutation** — R4 must not populate, modify, or repair OpenCart sections | R3 ownership; ST-R4 boundary |
| **No evidence access as authority** — R4 does not re-run R2 structural checks or read quarantine as publish target | R2.4 VAL-INV-01; R2.6 |
| **Gate semantics** — G2 (Validate → Store) and G3 inputs are R5 outputs; G4 (Publish → Consume) is R4 execution on **already validated** inputs | EAR-READINESS-GATES-v1 |
| **Terminology** — **R5 EAR Validate** certifies; **R4 Publish** promotes — distinct program labels | N-R3R-08; N-R5-07 |

**Critical invariant:** Publish **never** substitutes for Validate. NOT_ELIGIBLE recommendation **must** block default Publish path until re-Validate ([R5.6](R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md) PE-MAP-R5-01).

### Why consumer access begins only after R4

| Reason | Authority |
|--------|-----------|
| **Architecture rule** — Consumers consume **published snapshots only**; unpublished candidates and stored-unpublished trees are out of scope for intake | EAR-SNAPSHOT-PUBLISHING-v1 § Core rules |
| **Audience separation** — Store audience is operator/EAR; consumer audience requires explicit Publish gate | R1.8B § Store vs Publish |
| **Secrets risk** — Pre-Validate candidate may carry uncertified content; quarantine is never consumer input | EAR-EVIDENCE-PACKAGE-v1; EAR-STORAGE-MODEL-v1 |
| **Quality honesty** — Consumer reads **published** `package_quality_level` claim — frozen at Publish from R5 certification | EAR-OPENCART-QUALITY-MAPPING-v1 |
| **Immutability citation** — Published `snapshot_id` is consumer citation key; stored-unpublished id exists but **must not** be intake target | R1.8B § production snapshot_id |
| **OCPilot handoff** — Consumer programs (OCPilot) intake via published reference under `project-sites\` or equivalent — post-R4 | EAR-OPENCART-CONSUMER-GUIDE-v1 |
| **Lifecycle** — Acquire → Validate → Store → **Publish** → Consume; Consume has no valid entry before Publish | EAR-SNAPSHOT-LIFECYCLE-v1 |

**Critical invariant:** No consumer path write, registry pointer, or intake automation **before** R4 Publish completes with operator approval.

### Why R4 does not own quality

| Reason | Authority |
|--------|-----------|
| **Certification vs promotion** — Quality **possession** is assessed at Validate (R5); Publish **freezes** the certified claim — does not assess | R5.3; R5-CHARTER § Quality Ownership |
| **Inflation prevention** — Only R5 may assign certified `package_quality_level` L0–L3; R4 matching validated level is allowed; inflation is **forbidden** | Q-INV-R5-01–05; HO-FORBID-06 |
| **Semantic stages** — R3 candidate L0 (placeholder) ≠ R5 certified L0 (possession confirmed) ≠ R4 published L0 (frozen claim) | R5.3 § Candidate vs certified |
| **Possession rules live in R5** — Section adequacy, safe-unknown completeness for certify level, downgrade paths — all R5 | R5.2 Possession/Quality categories |
| **Publish answers visibility** — R4 answers *may this validated snapshot become consumer-visible?* not *what quality does it possess?* | R5.6 vs R4 mission |
| **Backlog alignment** — R4 engineering target is Publish gate + consumer reference; R5 owns Validate helpers and certification | EAR-RUNTIME-BACKLOG-v1 § R4 vs R5 |

**Critical invariant:** R4 **reads** certified `package_quality_level` from R5 outputs; R4 **must not** upgrade, recompute, or certify quality.

### Pipeline connection (authoritative)

```text
R2 Evidence Package
        ↓
R3 Candidate Snapshot Package
        ↓
R5 Validate
        ↓
Store (validated / stored-unpublished — R1.8 layout frozen)
        ↓
R4 Publish  ← this charter
        ↓
Consume (consumer programs)
```

**Authoritative program label:** Architecture backlog **R4 = Snapshot Publisher** — EAR Publish Layer; human HITL remains mandatory for pilot ([EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R4).

---

## Scope

### In scope (R4 program — charter defines; implementation follows R4 Implementation Charter)

| # | Work area | Boundary |
|---|-----------|----------|
| 1 | **Validated snapshot consumption** | Read stored or in-memory validated snapshot — **no mutation** of section content |
| 2 | **R5 artefact consumption** | `ValidationResult`, `ValidateReport`, `PublishEligibilityRecommendation` as Publish preconditions |
| 3 | **Operator Publish approval** | HITL gate — distinct from Validate sign-off |
| 4 | **Publish lifecycle definition** | State transitions: stored-unpublished → published → superseded/archived (conceptual) |
| 5 | **Published Snapshot definition** | Consumer-visible identity, metadata freeze, publish markers |
| 6 | **Consumer visibility rules** | Who may read what after Publish; what remains forbidden |
| 7 | **Publication ownership** | R4 vs R5 vs R3 vs operator vs consumer matrix |
| 8 | **Publish boundary** | R5→R4 handoff; R4→Consume handoff |
| 9 | **Publish metadata assignment** | `published_at`, `published_by`, `consumer_target` — R4 ownership |
| 10 | **Quality claim freeze** | Match R5 certified level — no inflation |

### Out of scope (explicit non-goals)

| # | Non-goal | Owner / phase |
|---|----------|---------------|
| 1 | **Evidence acquisition / generation** | **R2** + R1 |
| 2 | **Evidence quarantine writes** | **R2** |
| 3 | **Snapshot assembly / section population** | **R3** |
| 4 | **Candidate snapshot modification** | **Forbidden** — R4 reads validated artefact |
| 5 | **EAR Validate / contract certification** | **R5** |
| 6 | **Quality possession assessment / certification** | **R5** |
| 7 | **Redaction review / enforcement** | **R5** |
| 8 | **Validate report generation** | **R5** |
| 9 | **Publish Eligibility Recommendation emission** | **R5** |
| 10 | **Store layout redesign** | **Frozen** at R1.9 |
| 11 | **Consumer program execution** (OCPilot Run 5, baseline diff) | Consumer programs |
| 12 | **Unattended auto-Publish** | **Non-goal** — operator HITL mandatory |
| 13 | **Live SFTP / SITE-001 / PILOT execution** | Execution Authorization |
| 14 | **Normative JSON Schema / ZIP layout files** | **SAFE UNKNOWN** |
| 15 | **Architecture redesign** | Amendment charter only |

Per backlog § R4 non-goals: no OCPilot Run 5 execution; no auto-publish without HITL.

---

## Inputs

### Authoritative R4 input set

R4 Publish may consume **only** the following as primary publish targets and supporting gate context:

| # | Input | Source | R4 use |
|---|-------|--------|--------|
| I-R4-01 | **Validated Snapshot Package** | Store read `{output_root}/{acquisition_id}/snapshots/{snapshot_id}/` or in-memory post-Validate | Primary publish target — **read-only**; OpenCart section tree frozen at Validate |
| I-R4-02 | **`ValidationResult`** | R5.1 / Validate Engine | Publish precondition — outcome authority; fail closed on FAIL |
| I-R4-03 | **`ValidateReport`** | R5.5 | Operator audit context; Publish decision support — not re-validation |
| I-R4-04 | **`PublishEligibilityRecommendation`** | R5.6 | Advisory gate — NOT_ELIGIBLE blocks default Publish path |
| I-R4-05 | **Certified `package_quality_level`** | R5 `ValidationResult` / possession record | Freeze as published claim — **no upgrade** |
| I-R4-06 | **Snapshot identity** | R3.2 — `snapshot_id`, `site_id`, `acquisition_id` | Published reference keys; audit correlation |
| I-R4-07 | **Storage path binding** | R1.8B `{output_root}/{acquisition_id}/snapshots/{snapshot_id}/` | Confirm stored placement — **no layout redesign** |
| I-R4-08 | **Operator Publish approval** | Operator HITL | Mandatory gate — distinct from Validate sign-off |
| I-R4-09 | **`consumer_target` declaration** | Operator / config | Publish metadata — e.g. `ocpilot` |
| I-R4-10 | **Architecture gate definitions** | EAR-READINESS-GATES-v1 G3–G4 | Publish checklist semantics |

### Derived inputs (not separate ownership)

| Derived input | Derivation | Notes |
|---------------|------------|-------|
| Store publish_state (stored-unpublished) | R1.8B conceptual field | Precondition — snapshot stored before Publish per G3 |
| Prior published snapshot for site | Consumer registry / metadata | Supersession rules — **SAFE UNKNOWN** detail |
| Operator override record | HITL exception path on NOT_ELIGIBLE | Audited decision — does not retroactively change R5 artefacts |

### Explicit non-inputs (R4 must not treat as publish authority)

| Artefact | Reason | Owner |
|----------|--------|-------|
| Raw connector output / listing | Pre-evidence | R1 |
| Evidence Package / quarantine bulk | Not consumer publish target | R2 |
| Candidate snapshot without R5 Validate | Lifecycle violation | R5 |
| R3 assembly eligibility result alone | Precondition ≠ Validate pass | R3 |
| R2 structural pass alone | Pre-handoff ≠ snapshot certification | R2 |
| Unvalidated / stored-only snapshot without R5 bundle | Publish without Validate forbidden | R5 |
| Live credentials | External secrets | Operator |
| R5 redaction findings for re-scan | R5 already reviewed — R4 confirms gate only | R5 |

---

## Outputs

### Authoritative R4 output set

| # | Output | Consumer | Notes |
|---|--------|----------|-------|
| O-R4-01 | **Published Snapshot reference** | Consumer programs; operator registry | Consumer-visible identity + storage pointer |
| O-R4-02 | **Publish Result** | Operator; pipeline; audit | Success / blocked / deferred — distinct from ValidationResult |
| O-R4-03 | **Publish metadata** | Store metadata update; acquisition-log | `published_at`, `published_by`, `consumer_target` |
| O-R4-04 | **Frozen `package_quality_level`** | Consumer intake | Matches R5 certified level — **no inflation** |
| O-R4-05 | **Published snapshot state marker** | Store lifecycle | stored-unpublished → **published** transition |
| O-R4-06 | **Publish log / audit record** | Operator; governance | Gate satisfaction record; HITL refs |
| O-R4-07 | **Consumer visibility grant** | Registered consumers | Logical permission to begin Consume — not credential handoff |
| O-R4-08 | **Supersession record** | Operator; archive policy | When newer publish replaces active default — **SAFE UNKNOWN** detail |

### Explicit non-outputs

| Output | Owner |
|--------|-------|
| `ValidationResult` / Validate report | **R5** |
| `PublishEligibilityRecommendation` | **R5** |
| Certified quality assignment | **R5** |
| OpenCart section population or mutation | **R3** |
| Evidence Package writes | **R2** |
| Consumer reports / OCPilot Run 5 execution | Consumer programs |
| Automatic Publish without HITL | **Forbidden** |
| Live acquisition artefacts | R1 + Execution Authorization |

### R4 does not validate

R4 **never** re-runs contract certification, **never** assigns certified quality, **never** performs redaction review, **never** emits Validate report or Publish Eligibility Recommendation. R4 **reads** R5 outputs and **executes** Publish after operator approval ([EAR-SNAPSHOT-PUBLISHING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-PUBLISHING-v1.md)).

```text
R5 Validate
        ↓
ValidationResult + ValidateReport + PublishEligibilityRecommendation
        ↓
Operator HITL (Validate sign-off — mandatory for pilot)
        ↓
Operator HITL (Publish approval — mandatory for pilot)
        ↓
R4 Publish  ← R4 starts here
        ↓
Published Snapshot reference + publish metadata
        ↓
Consume
```

---

## Publish Lifecycle

Normative sources: [EAR-SNAPSHOT-LIFECYCLE-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-LIFECYCLE-v1.md), [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) § Store vs Publish, [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md).

### Lifecycle stages (R4 scope highlighted)

```text
Acquire (R1)
        ↓
Evidence Package (R2)
        ↓
Candidate Snapshot (R3)
        ↓
Validate (R5) ──fail──► reject / remediate — no Publish
        ↓ pass
Store (R1.8) — stored-unpublished
        ↓
╔═══════════════════════════════════════╗
║  R4 Publish (this charter)            ║
║  Operator HITL + R5 gate bundle       ║
╚═══════════════════════════════════════╝
        ↓
Published Snapshot — consumer may Consume
        ↓
Archive (superseded / retention policy)
```

### Publish state model (conceptual — charter only)

| State | Meaning | Consumer access | R4 role |
|-------|---------|-----------------|---------|
| **candidate** | R3 assembly output; uncertified | **None** | **Not R4** |
| **validated** | R5 pass; certification recorded | **None** | **Precondition** — R4 input stage |
| **stored-unpublished** | Immutable Store placement; Validate complete | **None** | **Precondition** — G3 satisfied |
| **published** | Publish gate executed; metadata set | **Allowed** — registered consumers | **R4 target state** |
| **superseded** | Newer published snapshot active for site | Historical cite only | **R4 records** — **SAFE UNKNOWN** automation |
| **archived** | Retention tier; not active default | Policy-dependent | Operator — R4 may emit pointer |

### State transition requirements

| Transition | Requirements | Owner |
|------------|--------------|-------|
| validated → stored-unpublished | R5 Validate pass; honest quality; no secrets; `snapshot_id` assigned | Store (R1.8) — may coincide with R3 persist |
| stored-unpublished → **published** | R5 bundle present; Publish Eligibility not NOT_ELIGIBLE (default); operator Publish HITL; storage confirmed | **R4** |
| **published** → superseded | Newer R4 Publish for same site; archive policy | **R4** + operator |
| candidate → published | **FORBIDDEN** — bypasses Validate | — |
| NOT_ELIGIBLE → published (default) | **FORBIDDEN** — requires operator audited override + typically re-Validate | HITL exception |

### Gate mapping (R4 execution)

| Gate | Upstream owner | R4 role |
|------|----------------|---------|
| **G1** Acquire → Validate | R1/R2/R3 | R4 **assumes satisfied** when R5 bundle present |
| **G2** Validate → Store | **R5** | R4 **requires** ValidationResult pass |
| **G3** Store → Publish | Operator storage confirmation | R4 **confirms** placement; executes Publish |
| **G4** Publish → Consume | **R4** | R4 **owns** execution; consumer intake after |

### Combined Store + Publish

Per [EAR-SNAPSHOT-PUBLISHING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-PUBLISHING-v1.md): operator may combine Store and Publish in one action **if both gate checklists satisfied**. R4 charter **allows** combined workflow conceptually; R1.8 implemented Store only — combined action remains operator/R4 future scope.

---

## Published Snapshot Definition

Normative sources: [EAR-SNAPSHOT-PUBLISHING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-PUBLISHING-v1.md), [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md), [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md).

### What Published Snapshot is

A **Published Snapshot** is the **same immutable OpenCart section tree** as the validated stored snapshot, plus **publish metadata** and **consumer visibility grant** — not a new assembly, not a re-validated copy, not evidence quarantine repackaged.

| Property | Definition |
|----------|------------|
| **Identity** | Same `snapshot_id` as validated stored snapshot — consumer citation key |
| **Content** | Frozen OpenCart sections from Validate — **R4 must not mutate** |
| **Quality claim** | `package_quality_level` frozen from R5 certified level |
| **Publish markers** | `published_at`, `published_by`, `consumer_target` added or updated in metadata / acquisition-log |
| **Visibility** | Registered consumers may begin intake via published reference |
| **Secrets** | **None** — credentials never in published tree |
| **Evidence** | **Not included** — acquisition-log audit only |

### Published vs validated vs candidate

| Dimension | Candidate (R3) | Validated (R5) | Published (R4) |
|-----------|----------------|----------------|----------------|
| **Quality claim** | L0 placeholder (uncertified) | R5 certified L0–L3 | Frozen published claim |
| **Consumer access** | **No** | **No** | **Yes** |
| **Publish metadata** | Absent | Absent | **Present** |
| **Section mutability** | R3 wrote once | Frozen at Validate | Frozen — R4 read-only |
| **Validate bundle required** | No | Self | **Yes** — precondition |

### Minimum published artefact (conceptual)

| Component | Required at Publish | Source |
|-----------|---------------------|--------|
| `snapshot_id` | **Yes** | R3.2 |
| `snapshot_contract` / `parent_contract` | **Yes** | R3.1 |
| `site_id` | **Yes** | R3 identity |
| `package_quality_level` (published) | **Yes** | R5 certified — frozen |
| OpenCart section tree | **Yes** | Validated snapshot — unchanged |
| `published_at` | **Yes** | **R4 assigns** |
| `published_by` / operator ref | **Yes** | **R4 records** |
| `consumer_target` | **Yes** | Operator declaration |
| `bulk_root` reference | When present on snapshot | Unchanged from Store |
| Consumer registry pointer | **Optional** | **SAFE UNKNOWN** encoding |

### Immutability rules (from R1.8B — R4 preserves)

| Rule | R4 behavior |
|------|-------------|
| Published `snapshot_id` is not mutated | R4 **never** edits section content in place |
| Corrections require new acquisition → new `snapshot_id` | R4 **does not** repair snapshots |
| In-place metadata edit after Publish discouraged | R4 sets publish metadata once at Publish |
| Mock ids forbidden in production publish | R4 **rejects** `snap-mock-*` on production path |

---

## Ownership Matrix

### Concern → Owner matrix (mandatory review: R2, R3, R5, R1.8B)

| Concern | R2 | R3 | R5 | R4 | Operator | Consumer |
|---------|----|----|----|----|----------|----------|
| Evidence Package | **Owns** | Reads | Reads (Validate) | — | Inspects quarantine | **No access** |
| Evidence quarantine | **Owns** write | Read for assembly | Read (Validate) | — | **Owns** external root | **No access** |
| Candidate snapshot assembly | — | **Owns** | Reads | — | Inspects | **No access** |
| R2 structural validation | **Owns** | Requires | Precondition | — | — | — |
| R3 assembly eligibility | — | **Owns** | Precondition | — | — | — |
| EAR Validate / certification | — | — | **Owns** | Input only | HITL Validate | — |
| `package_quality_level` certification | Forbidden | Candidate L0 | **Owns** | **Freezes** published | Override/downgrade at Validate | Reads published |
| Validate report | — | — | **Owns** | Input | Reviews | — |
| Publish Eligibility Recommendation | — | — | **Owns** emit | **Owns** consume | Reviews | — |
| Store layout / persist | — | Candidate write | Validated marker | Reads stored | **Owns** external storage | — |
| **Publish execution** | — | — | **Forbidden** | **Owns** | Approves | Receives |
| Publish metadata | — | — | — | **Owns** | Approves | Reads |
| Published snapshot reference | — | — | — | **Owns** | Approves | **Owns** intake |
| Redaction enforcement | Policy on evidence | Avoid copy | **Owns** review | Pre-Publish confirm only | Policy | Never secrets |
| Consumer delivery / OCPilot | — | — | — | Reference only | — | **Owns** execution |
| Archive / supersession | — | — | — | Records | Retention policy | Historical cite |

### R1.8B Store assumptions (R4 inherits — does not redesign)

| Assumption | R4 use |
|------------|--------|
| Layout `{output_root}/{acquisition_id}/snapshots/{snapshot_id}/` | Read validated snapshot; write publish metadata only |
| Store vs Publish distinction (G-09 resolved) | R4 executes Publish half |
| stored-unpublished valid terminal pre-Publish | R4 precondition |
| `publish_state` conceptual encoding | R4 sets published — exact encoding **SAFE UNKNOWN** |
| Mock ids never in production store/publish | R4 entry gate |
| Immutability write-once per `snapshot_id` | R4 **no section mutation** |
| Consumer cites `snapshot_id` only — not `acquisition_id` | R4 published reference |
| OCPilot `project-sites\` as consumer bulk intake | Post-Publish pointer — **SAFE UNKNOWN** whether R4 writes directly |

### Overlap prevention

| Boundary | Rule |
|----------|------|
| R2 ↔ R4 | R4 **never** reads quarantine as publish target; **never** generates evidence |
| R3 ↔ R4 | R4 **never** assembles or mutates sections; R3 **never** publishes |
| R5 ↔ R4 | R5 **recommends**; R4 **publishes**; R4 **never** validates or certifies |
| R4 ↔ Operator | Operator owns Publish HITL, `consumer_target`, external paths, override audit |
| R4 ↔ Consumer | R4 grants reference; consumer **owns** intake execution and reports |
| R4 ↔ R1.8 | R4 **uses** frozen Store layout — no redesign |

---

## Consumer Boundary

### What consumers may access (after R4 Publish only)

| Access | Allowed | Condition |
|--------|---------|-----------|
| Published snapshot reference | **Yes** | After R4 Publish + operator approval |
| Published `snapshot_id` citation | **Yes** | Immutable consumer key |
| OpenCart section tree (published) | **Yes** | Per contract version on intake |
| Published `package_quality_level` | **Yes** | Frozen R5 claim |
| `safe-unknown/` honesty block | **Yes** | Unchanged from validated snapshot |
| `bulk_root` opaque reference | **Yes** | No secrets |
| `acquisition-log` audit | **Yes** | How evidence was obtained |
| Live SITE credentials | **No** | Never |
| Evidence quarantine | **No** | R2 internal |
| Candidate / stored-unpublished snapshot | **No** | Pre-Publish |
| Validate report (internal) | **No** by default | Operator artefact — consumer may receive summary via policy **SAFE UNKNOWN** |
| Permission to initiate acquisition | **No** | Operator + EAR only |

### Consumer programs (out of R4 core)

| Program | Relationship to R4 |
|---------|-------------------|
| **OCPilot** | Consumes **published** snapshots; Run 5 baseline diff — **not** R4 deliverable |
| Future consumers | Register `consumer_target`; intake via published reference |

### Visibility rules (charter — not implementation)

| Rule ID | Rule |
|---------|------|
| CB-R4-01 | Consumer intake **must** reference published `snapshot_id` |
| CB-R4-02 | Unpublished stored snapshot **must not** appear in consumer registry as active |
| CB-R4-03 | Publish **must not** expose operator `secrets/` paths |
| CB-R4-04 | Consumer-side contract validation on intake is **distinct** from EAR Validate (R5) |
| CB-R4-05 | Re-acquisition requires new Request cycle — consumer does not pull live SITE |

---

## R5 → R4 Boundary

### Handoff diagram

```text
┌─────────────────────────────────────────────────────────┐
│  R5 Validate Layer                                       │
│  • Contract + quality + redaction assessment             │
│  • ValidationResult + ValidateReport                   │
│  • PublishEligibilityRecommendation (advisory)           │
│  • NEVER publishes                                       │
└───────────────────────────┬─────────────────────────────┘
                            │
                            ▼  R5 output bundle + Validate HITL
┌─────────────────────────────────────────────────────────┐
│  Store (R1.8 — frozen layout)                            │
│  • stored-unpublished validated snapshot                 │
└───────────────────────────┬─────────────────────────────┘
                            │
                            ▼  Publish HITL + gate check
┌─────────────────────────────────────────────────────────┐
│  R4 Publish Layer                                        │
│  • Reads validated snapshot + R5 bundle                  │
│  • Operator publish approval                             │
│  • Assigns publish metadata                              │
│  • Emits consumer-visible reference                      │
│  • NEVER re-validates or certifies quality               │
└───────────────────────────┬─────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│  Consume (consumer programs)                             │
└─────────────────────────────────────────────────────────┘
```

### R5 outputs → R4 inputs mapping

| R5 output | R4 consumption | R4 must not |
|-----------|----------------|-------------|
| `ValidationResult` | Precondition — FAIL blocks default Publish | Re-run certification |
| `ValidateReport` | Operator context for Publish decision | Regenerate report |
| `PublishEligibilityRecommendation` | Gate — NOT_ELIGIBLE blocks default | Emit recommendation |
| Certified `package_quality_level` | Freeze as published claim | Upgrade or reassess |
| Redaction findings | Confirm addressed — not re-scan | Own redaction review |
| Validated snapshot marker | Confirm lifecycle stage | Set Validate markers |

### R4 prohibitions at R5 boundary

| Prohibition | Authority |
|-------------|-----------|
| R4 **must not** execute Validate | R5 ownership |
| R4 **must not** emit Publish Eligibility Recommendation | R5.6 PE-INV-R5-01 |
| R4 **must not** assign certified quality | R5.3; VB-R5-07 |
| R4 **must not** publish on NOT_ELIGIBLE without audited operator override | R5.6; fail closed |
| R4 **must not** treat Validate pass as Publish approval alone | VAL-INV-02; separate HITL |
| R4 **must not** mutate candidate/validated section content | R3/R5 freeze |

### Recommendation → Publish decision flow

| PublishEligibilityRecommendation | Default R4 behavior | Operator override |
|----------------------------------|---------------------|-------------------|
| **ELIGIBLE** | May proceed after Publish HITL | — |
| **ELIGIBLE WITH NOTES** | May proceed after Publish HITL + note review | — |
| **NOT_ELIGIBLE** | **Block** default Publish | Audited override possible — does not change R5 artefacts |

---

## Success Criteria

R4 **program** (EAR Publish Layer charter) is **complete** when:

| ID | Criterion | Verification |
|----|-----------|--------------|
| SC-R4-01 | Mission answers: why R4 exists, why Validate does not Publish, why Publish does not Validate, why consumer access begins after R4, why R4 does not own quality | § Mission |
| SC-R4-02 | Scope lists Publish responsibilities and explicit non-goals — no Validate/assembly/evidence | § Scope |
| SC-R4-03 | Authoritative inputs I-R4-01–10 and non-inputs documented | § Inputs |
| SC-R4-04 | Outputs O-R4-01–08 documented; R4 does not validate stated | § Outputs |
| SC-R4-05 | Publish lifecycle and state model defined | § Publish Lifecycle |
| SC-R4-06 | Published Snapshot definition distinct from candidate/validated | § Published Snapshot Definition |
| SC-R4-07 | Ownership matrix covers R2, R3, R5, R1.8B assumptions | § Ownership Matrix |
| SC-R4-08 | Consumer boundary explicit — access after R4 only | § Consumer Boundary |
| SC-R4-09 | R5→R4 boundary explicit — recommendation ≠ Publish | § R5 → R4 Boundary |
| SC-R4-10 | R5 readiness notes and R5.6 contract reflected | § Inputs; R5 → R4 Boundary |
| SC-R4-11 | R4 Implementation Charter **READY** as next artifact | Gate transition |
| SC-R4-12 | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) and [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) updated | Program navigation |

**Engineering acceptance (post-implementation — R4 Implementation Charter, not this document):**

| ID | Criterion | Source |
|----|-----------|--------|
| IAC-R4-01 | Operator can execute Publish on validated snapshot with R5 bundle | Backlog § R4 acceptance |
| IAC-R4-02 | Published reference immutable; publish log records gate satisfaction | Backlog § R4 acceptance |
| IAC-R4-03 | Published quality matches R5 certified level — no inflation | EAR-OPENCART-QUALITY-MAPPING-v1 |
| IAC-R4-04 | NOT_ELIGIBLE blocks default Publish — fail closed | R5.6; EAR-READINESS-GATES-v1 |
| IAC-R4-05 | R4 does not re-validate or modify sections | This charter § Scope |
| IAC-R4-06 | Consumer intake possible only after Publish completes | EAR-SNAPSHOT-PUBLISHING-v1 |

**Explicitly excluded from R4 charter success:** Publish engine code, Validate implementation, Store redesign, live acquisition.

---

## Stop Conditions

Stop or escalate **before** R4 implementation if:

| ID | Condition | Action |
|----|-----------|--------|
| ST-R4-01 | Charter scope includes **Validate execution** or quality certification | **STOP** — reclassify as R5 |
| ST-R4-02 | Charter scope includes **snapshot assembly** or section writers | **STOP** — reclassify as R3 |
| ST-R4-03 | Charter scope includes **evidence generation** or quarantine persist | **STOP** — reclassify as R2 |
| ST-R4-04 | Charter allows **Publish without Validate** or without R5 bundle | **STOP** — violates lifecycle |
| ST-R4-05 | Charter assigns **quality certification** to R4 | **STOP** — quality inflation risk |
| ST-R4-06 | Charter allows **candidate snapshot mutation** at Publish | **STOP** — R3/R5 freeze violation |
| ST-R4-07 | Charter requires **SITE-001**, **PILOT-001**, live SFTP without authorization | **STOP** — Execution Authorization |
| ST-R4-08 | Charter requires **Store / persistence redesign** contradicting R1.9 | **STOP** — architecture amendment |
| ST-R4-09 | Charter replaces **human Publish HITL** with unattended auto-publish | **STOP** — backlog non-goal |
| ST-R4-10 | Implementation proposed without **R4 Implementation Charter** + human gate | **STOP** — per R1/R2/R3/R5 gate pattern |
| ST-R4-11 | Charter includes **OCPilot Run 5** as R4 deliverable | **STOP** — consumer program |
| ST-R4-12 | Publish bulk placed under **git workspace** without architecture charter | **STOP** — EAR-STORAGE-MODEL |
| ST-R4-13 | Charter conflates **Publish Eligibility Recommendation** with Publish execution | **STOP** — VAL-INV-02 |

### Out-of-scope conditions (ongoing)

Work is **out of R4** if it matches any row in **Non-Goals** or:

- Certifies contract compliance or quality possession
- Performs redaction review on snapshot content
- Populates OpenCart sections from evidence
- Generates or mutates Evidence Package
- Emits Validate report or Publish Eligibility Recommendation
- Enables network acquisition in R4 charter scope

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| R4 label confusion — engineers implement Validate or assembly as R4 | High | Mission + Non-Goals; R5→R4 boundary § |
| Publish before Validate or without R5 bundle | High | ST-R4-04; Inputs § non-inputs |
| Quality inflation at Publish without R5 certification | High | Mission § Why R4 does not own quality; ST-R4-05 |
| ELIGIBLE recommendation treated as auto-Publish | High | Separate Publish HITL; R5.6 SC-R5.6-04 |
| R4 mutates validated snapshot sections during Publish | High | Published Snapshot Definition; ST-R4-06 |
| Stored-unpublished snapshot exposed to consumers | High | Consumer Boundary CB-R4-02 |
| R4 re-implements R5 redaction or possession checks | Medium | Scope non-goals; R5 ownership matrix |
| Combined Store+Publish bypasses Validate HITL | Medium | Publish Lifecycle § combined action |
| OCPilot path confusion — R4 writes consumer bulk without Publish gate | Medium | R1.8B OQ-04; Consumer Boundary |
| Dual HITL fatigue — operators skip Publish approval | Medium | Stop conditions ST-R4-09 |
| Mock snapshot_id published to production registry | Medium | R1.8B mock boundary; immutability rules |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Exact Publish Result serialization format | R4 Implementation Charter |
| Published snapshot Store state marker / sidecar encoding | R4 Implementation Charter — `publish_state` field |
| Consumer registry pointer location (EAR store vs OCPilot `project-sites\`) | R1.8B OQ-04 — **SAFE UNKNOWN** |
| Whether R4 copies contract slice to consumer path vs reference only | R1.8B hybrid model |
| Physical encoding of publish metadata (metadata/ vs acquisition-log/) | R4 Implementation Charter |
| Official JSON Schema for Publish artefacts | Not in repo |
| Supersession automation — active default pointer per site | Architecture **SAFE UNKNOWN** |
| Operator override audit schema on NOT_ELIGIBLE | Operator workflow |
| Post-Publish recommendation / Validate artefact retention | Operator / governance policy |
| Publish notification webhooks | EAR-SNAPSHOT-PUBLISHING-v1 — not v1 |
| `--publish-snapshot` CLI flag exact name | R4 Implementation Charter |
| Atomic Publish + metadata write failure recovery | R4 Implementation Charter |
| 1:N `acquisition_id` → `snapshot_id` publish policy | Architecture **SAFE UNKNOWN** |
| Whether empty NOT_ELIGIBLE override requires re-Validate | Default yes — exception path operator policy |
| R4 strict ordering vs parallel design with R5 implementation | R5.9 allows R4 planning parallel — runtime order canonical |
| Contract-path Store read before Publish when candidate in-memory only | R3 debt — R4 must handle both |

---

## Planning notes (carried from R5)

| Note | Action |
|------|--------|
| N-R5R-01 | R4 Charter restates R5→R4 boundary — **satisfied** § R5 → R4 Boundary |
| N-R5R-02 | R4 planning may proceed parallel with R5 implementation — **satisfied** § Purpose |
| N-R5R-03 | R5.6 Publish Eligibility is advisory input — **satisfied** § Inputs I-R4-04 |
| N-R5R-04 | In-memory validated snapshot path — R4 design must support memory and Store read |
| N-R5R-05 | Human HITL mandatory for Validate and Publish — **satisfied** § Mission |
| N-R5R-06 | R4 does not implement Validate Engine — **satisfied** § Non-Goals |
| N-R5R-07 | Store persist debt (R3) — R4 precondition may assume stored or memory — **SAFE UNKNOWN** |
| N-R5R-08 | Terminology: R2 structural / R3 assembly / R5 Validate / R4 Publish — **satisfied** § Mission |

---

## Evidence index

| ID | Source |
|----|--------|
| C-R4-01 | [R5-READINESS-REVIEW-v1.md](R5-READINESS-REVIEW-v1.md) |
| C-R4-02 | [R5-READINESS-DECISION-v1.md](R5-READINESS-DECISION-v1.md) |
| C-R4-03 | [R5-CHARTER-v1.md](R5-CHARTER-v1.md) § Publish Boundary |
| C-R4-04 | [R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md](R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md) |
| C-R4-05 | [R5.8-VALIDATION-BOUNDARY-DECISION-v1.md](R5.8-VALIDATION-BOUNDARY-DECISION-v1.md) |
| C-R4-06 | [R3-CHARTER-v1.md](R3-CHARTER-v1.md) § Ownership Boundary |
| C-R4-07 | [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) § Store vs Publish |
| C-R4-08 | [EAR-SNAPSHOT-PUBLISHING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-PUBLISHING-v1.md) |
| C-R4-09 | [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md) |
| C-R4-10 | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R4 |

---

## Cross-references

| Document | Use |
|----------|-----|
| [R4-DECISION-v1.md](R4-DECISION-v1.md) | Charter gate decision |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Program status |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation |
