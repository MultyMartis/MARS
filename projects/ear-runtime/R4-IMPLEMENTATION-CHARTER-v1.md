# R4 — EAR Publish Implementation Charter v1

**Type:** Implementation engineering charter — **no** runtime code, **no** publish engine implementation, **no** CLI, **no** persistence implementation in this document  
**Date:** 2026-06-07  
**Phase:** R4 — EAR Publish Layer  
**Lane:** B — EAR Runtime Engineering  
**Prior gates:** R1 **COMPLETE**; R2 **COMPLETE WITH NOTES**; R3 **COMPLETE WITH NOTES**; R5 **COMPLETE WITH NOTES**; [R4-CHARTER-v1.md](R4-CHARTER-v1.md) **COMPLETE**; [R4-DECISION-v1.md](R4-DECISION-v1.md) — **APPROVED WITH NOTES**  
**Decision companion:** [R4-IMPLEMENTATION-DECISION-v1.md](R4-IMPLEMENTATION-DECISION-v1.md)  
**Architecture sources:** [shared/external-access-runtime/](../../shared/external-access-runtime/)

---

## Charter identity

| Field | Value |
|-------|-------|
| **Authorizes** | R4 engineering scope, work packages R4.1–R4.9, Published Snapshot model, Publish state model, Consumer visibility model, Publish metadata ownership, Publish Result contract, Publish Flow contract, Publish Engine architecture scope, R5/R4 boundary verification, implementation sequence — **not** Validate execution, snapshot assembly, evidence generation, Store redesign, or live acquisition |
| **Does not authorize** | Publish automation code, Validate execution, quality certification, section population, quarantine mutation, OCPilot integration, SITE-001 / PILOT execution, live SFTP, normative JSON Schema files |
| **Human approver** | **Pending** — see [R4-IMPLEMENTATION-DECISION-v1.md](R4-IMPLEMENTATION-DECISION-v1.md) |
| **Program label** | **R4 — EAR Publish Layer** / Snapshot Publisher — **not** Validate or Snapshot Assembly |

---

## Mission

### Why R4 engineering exists

R5 closed with **validated snapshot certification artefacts** — `ValidationResult`, `ValidateReport`, `PublishEligibilityRecommendation`, certified `package_quality_level` — but **never** promotes a snapshot to consumer intake ([R5-CHARTER-v1.md](R5-CHARTER-v1.md) § Publish Boundary). R1.8 Store places validated snapshots immutably for operator/EAR use at **stored-unpublished** state ([R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) § Store vs Publish). R4 engineering translates the approved [R4-CHARTER-v1.md](R4-CHARTER-v1.md) into **executable scope** before any Publish code: contracts for published snapshot identity, publish lifecycle states, consumer visibility grants, publish metadata ownership, publish outcomes, HITL publish flow, and boundary gates — producing **consumer-visible published snapshot references** distinct from R5 certification artefacts.

### What R4 engineering builds (conceptually)

**EAR Publish** promotes a validated stored snapshot to consumer-visible state after operator HITL. R4 engineering defines **contracts and orchestration scope** — not acquisition, not assembly, not Validate, not quality assessment.

```text
R5 Validate bundle (ValidationResult + ValidateReport + PublishEligibilityRecommendation)
        ↓
Store — stored-unpublished validated snapshot (R1.8 layout frozen)
        ↓
Operator HITL (Validate sign-off — mandatory for pilot)
        ↓
Operator HITL (Publish approval — mandatory for pilot)
        ↓
R4 EAR Publish                    ← R4 engineering scope
        ↓
Published Snapshot reference + PublishResult + publish metadata
        ↓
Consume (consumer programs — not R4)
```

### Gap R4 engineering closes (evidence-backed)

| Post-R5 state | R4 engineering target |
|---------------|------------------------|
| Validated snapshot has no consumer visibility | Published Snapshot reference with visibility grant |
| No publish lifecycle state model | stored-unpublished → published → superseded/archived transitions |
| No publish metadata contract | `published_at`, `published_by`, `consumer_target` — R4 ownership |
| R5 recommendation conflated with Publish execution | Distinct `PublishResult` — never reuse `ValidationResult` |
| Store vs Publish distinction undocumented at engineering layer | Explicit Store ≠ Publish contracts per R1.8B G-09 |
| No HITL publish flow contract | Dual-gate flow: Validate HITL + Publish HITL |
| Consumer intake boundary undefined at implementation | Consumer visibility begins only after R4 Publish |

---

## Mandatory questions (explicit answers)

### What makes a snapshot published

A snapshot is **published** when **all** of the following are true:

| # | Condition | Owner |
|---|-----------|-------|
| 1 | R5 `ValidationResult` outcome is **PASS** or **PASS WITH NOTES** — not FAIL | R5 precondition; R4 confirms |
| 2 | R5 `PublishEligibilityRecommendation` is **ELIGIBLE** or **ELIGIBLE WITH NOTES** — default path (NOT_ELIGIBLE requires audited operator override) | R5 advisory; R4 gate |
| 3 | Validated snapshot exists — stored at R1.8 layout `{output_root}/{acquisition_id}/snapshots/{snapshot_id}/` **or** in-memory post-Validate with equivalent bundle | Store / R5 |
| 4 | **Operator Publish HITL approval** recorded — distinct from Validate sign-off | Operator |
| 5 | R4 Publish execution completes — assigns publish metadata and emits published reference | **R4** |
| 6 | `publish_state` transitions to **published** (conceptual — exact encoding R4.2) | **R4** |
| 7 | `published_at`, `published_by`, `consumer_target` set in metadata / acquisition-log | **R4** |
| 8 | Certified `package_quality_level` **frozen** from R5 — matches validated level, no inflation | **R4** freeze only |
| 9 | Consumer visibility grant issued for registered `consumer_target` | **R4** |
| 10 | Gate G4 (Publish → Consume) satisfied per [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md) | **R4** |

**Critical invariant:** Same immutable OpenCart section tree as validated stored snapshot — **plus** publish metadata and visibility grant. Not a new assembly. Not a re-validated copy ([R4-CHARTER-v1.md](R4-CHARTER-v1.md) § Published Snapshot Definition).

### What does not make a snapshot published

| Condition | Why not published |
|-----------|-------------------|
| R3 candidate assembly complete | Uncertified — no Validate |
| R3 assembly eligibility PASS | Precondition ≠ Validate pass |
| R2 structural validation PASS | Pre-handoff ≠ snapshot certification |
| R5 Validate PASS alone | Validate sign-off ≠ Publish approval (VAL-INV-02) |
| R5 `PublishEligibilityRecommendation` **ELIGIBLE** alone | Recommendation ≠ Publish execution (PE-INV-R5-01) |
| Store persist without Publish gate | stored-unpublished is valid terminal pre-Publish (R1.8B) |
| Operator storage confirmation alone | G3 satisfied ≠ G4 executed |
| Setting `consumer_target` in config without Publish | Metadata field assignment without gate |
| Copying snapshot tree to consumer path without Publish | Violates lifecycle — CB-R4-01 |
| Mock `snapshot_id` on production publish path | R1.8B mock boundary |
| Candidate → published bypass | **FORBIDDEN** — skips Validate |
| NOT_ELIGIBLE → published without audited override | Fail closed per R5.6 |
| R4 mutating sections then calling it "published" | Section mutation forbidden — ST-R4-06 |
| Evidence quarantine repackaged as snapshot | Not consumer publish target |

### Why Store ≠ Publish

| Dimension | **Store** | **Publish** |
|-----------|-----------|-------------|
| **Purpose** | Immutable placement of validated artefacts for operator/EAR | Explicit consumer visibility gate |
| **Audience** | Operator, EAR, backup policy | Registered consumers |
| **Prerequisite** | R5 Validate pass | R5 bundle + Store placement + Publish HITL |
| **Consumer access** | **None** — stored-unpublished is valid | **Required** for Consume |
| **Primary owner** | Operator bulk; EAR metadata refs | Operator HITL; **R4** publish metadata |
| **Outputs** | Immutable tree keyed by `snapshot_id`; `bulk_root` ref | Published reference; `published_at`, `consumer_target` |
| **R1.8 scope** | **In scope** — persist stored-unpublished | **Out of scope** — R4 |
| **Quality action** | Records R5 certified level | **Freezes** certified level — does not assess |

Per [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) § Task 5: Store is **terminal for R1.8** at stored-unpublished; Publish is **R4** responsibility. Combined Store+Publish in one operator action is **allowed conceptually** when both gate checklists satisfied — R4 charter inherits this; R1.8 implemented Store only.

### Why Publish does not create quality

| Reason | Authority |
|--------|-----------|
| **Certification vs promotion** — Quality possession assessed at Validate (R5); Publish **freezes** certified claim | R5.3; R4-CHARTER § Why R4 does not own quality |
| **Inflation prevention** — Only R5 assigns certified L0–L3; R4 matching validated level allowed; upgrade **forbidden** | Q-INV-R5-01–05 |
| **Semantic stages** — R3 candidate L0 ≠ R5 certified L0 ≠ R4 published L0 (frozen claim) | R5.3 § Candidate vs certified |
| **Possession rules live in R5** — Section adequacy, safe-unknown completeness, downgrade paths | R5.2 Quality/Possession categories |
| **Publish answers visibility** — R4 answers *may this validated snapshot become consumer-visible?* not *what quality does it possess?* | R5.6 vs R4 mission |
| **No re-assessment at Publish** — R4 reads `ValidationResult.certified_quality_level`; does not re-run possession checks | ST-R4-01 boundary |

**Critical invariant:** R4 **reads** certified level; R4 **must not** upgrade, recompute, or certify quality.

### Why consumer visibility begins only after Publish

| Reason | Authority |
|--------|-----------|
| **Architecture rule** — Consumers consume **published snapshots only** | EAR-SNAPSHOT-PUBLISHING-v1 § Core rules |
| **Audience separation** — Store audience is operator/EAR | R1.8B § Store vs Publish |
| **Secrets risk** — Pre-Validate candidate may carry uncertified content; quarantine never consumer input | EAR-EVIDENCE-PACKAGE-v1 |
| **Quality honesty** — Consumer reads **published** `package_quality_level` — frozen at Publish from R5 | EAR-OPENCART-QUALITY-MAPPING-v1 |
| **Immutability citation** — Published `snapshot_id` is consumer citation key | R1.8B § production snapshot_id |
| **Lifecycle** — Acquire → Validate → Store → **Publish** → Consume | EAR-SNAPSHOT-LIFECYCLE-v1 |
| **OCPilot handoff** — Consumer programs intake via published reference — post-R4 | EAR-OPENCART-CONSUMER-GUIDE-v1 |

**Critical invariant:** No consumer path write, registry pointer, or intake automation **before** R4 Publish completes with operator approval.

---

## Engineering Scope

### In scope (R4 implementation — when human gate approves code)

| ID | Area | Engineering deliverable |
|----|------|-------------------------|
| S-R4-01 | Published Snapshot Model | Consumer-visible identity contract — same `snapshot_id`, frozen sections, publish markers |
| S-R4-02 | Publish State Model | Lifecycle states and transitions — stored-unpublished → published → superseded/archived |
| S-R4-03 | Consumer Visibility Model | Who may read what after Publish; forbidden pre-Publish access |
| S-R4-04 | Publish Metadata Model | `published_at`, `published_by`, `consumer_target` — R4 ownership |
| S-R4-05 | Publish Result Contract | Success / blocked / deferred — distinct from ValidationResult |
| S-R4-06 | Publish Flow Contract | HITL publish flow; R5 bundle consumption; gate checklist |
| S-R4-07 | Publish Engine | Future orchestration scope — inputs, outputs, fail-closed behavior |
| S-R4-08 | Publish Boundary Review | Verify R4 does not absorb R5 Validate or R3 assembly |
| S-R4-09 | R4 Readiness Review | Final gate before R4 code authorization |

### Out of scope (explicit)

| Item | Owner |
|------|-------|
| EAR Validate / contract certification | **R5** |
| Quality possession assessment / certification | **R5** |
| Redaction review / enforcement | **R5** |
| Publish Eligibility Recommendation emission | **R5** |
| Snapshot assembly / section population | **R3** |
| Evidence generation / quarantine writes | **R2** |
| Acquisition / connector execution | **R1** + Execution Authorization |
| Store layout redesign | **Frozen** R1.9 |
| Consumer program execution (OCPilot Run 5) | Consumer programs |
| Unattended auto-Publish | **Non-goal** — operator HITL mandatory |
| Normative JSON Schema / ZIP layout files | **SAFE UNKNOWN** |

### Code placement (when implementation authorized)

R4 code may extend **only** under:

```text
projects/ear-runtime/runtime/
```

Likely paths (chartered, not prescriptive filenames):

| Path | Role |
|------|------|
| `runtime/shared/published_snapshot_models.py` | Published Snapshot reference contract — **R4.1 implementation** |
| `runtime/shared/publish_state_models.py` | Publish state enum and transition rules — **R4.2 implementation** |
| `runtime/shared/publish_metadata_models.py` | Publish metadata fields — **R4.4 implementation** |
| `runtime/shared/publish_result_models.py` | PublishResult contract — **R4.5 implementation** |
| `runtime/publishers/ear_publish_engine.py` | Publish orchestrator — **R4.7 implementation** |

**Forbidden:** `shared/external-access-runtime/` amendments without Architecture Amendment Charter; OpenCart section mutation; evidence quarantine mutation; Validate execution; quality certification logic; consumer program integration code.

---

## Dependencies

| Predecessor | Requirement |
|-------------|-------------|
| R1 | **COMPLETE** — mock pipeline, Store layout frozen at R1.9 |
| R2 | **COMPLETE WITH NOTES** — evidence model; R4 never reads quarantine as publish target |
| R3 | **COMPLETE WITH NOTES** — R3.1 `SnapshotPackage`; R4 reads validated artefact only |
| R5 | **COMPLETE WITH NOTES** — R5.1–R5.9 contracts; Validate Engine code **NOT IMPLEMENTED** |
| R4 Charter | **COMPLETE** — [R4-CHARTER-v1.md](R4-CHARTER-v1.md), [R4-DECISION-v1.md](R4-DECISION-v1.md) |
| Architecture | EAR-SNAPSHOT-PUBLISHING-v1, EAR-SNAPSHOT-LIFECYCLE-v1, EAR-READINESS-GATES-v1, R1.8B Store vs Publish |

### Inherited assumptions (from R4 Charter — A-R4-01–12)

| ID | Assumption |
|----|------------|
| A-R4-01 | R5 emits distinct bundle: ValidationResult + ValidateReport + PublishEligibilityRecommendation |
| A-R4-02 | R4 emits distinct artefact: PublishResult — never reuse ValidationResult |
| A-R4-03 | Validate pass + ELIGIBLE recommendation are preconditions — separate Publish HITL mandatory |
| A-R4-04 | Published snapshot is read-only promotion — no section mutation |
| A-R4-05 | Fail closed on NOT_ELIGIBLE per R5.6 — default block until re-Validate or audited override |
| A-R4-06 | R1.8 layout `{output_root}/{acquisition_id}/snapshots/{snapshot_id}/` frozen — no redesign |
| A-R4-07 | stored-unpublished valid pre-Publish terminal state |
| A-R4-08 | Mock `snapshot_id` dry-run only — production publish rejects `snap-mock-*` |
| A-R4-09 | Terminology: R2 structural / R3 assembly / R5 Validate / R4 Publish |
| A-R4-10 | R5 Validate Engine may not exist when R4 implementation starts — mock R5 bundle acceptable for engineering |
| A-R4-11 | Contract-path Store persist (R3 debt) — R4 must support stored and in-memory validated inputs |
| A-R4-12 | Consumer registry pointer location — resolve at R4.3/R4.7 — **SAFE UNKNOWN** at charter |

### R5/R3 debt (non-blocking for implementation charter)

| Debt | R4 handling |
|------|-------------|
| Validate Engine not implemented | R4 may use mock R5 bundle for contract/engine engineering |
| Contract-path Store persist adapter | R4 Publish design supports memory and Store read |
| Publish eligibility models not dataclass yet | R4.6 consumes R5.6 contract semantics — module deferred |
| Bulk expansion (HO-ALLOW-10) | May block **live** publish paths — not charter blocker |

---

## Inputs

### Authoritative upstream (R5 → Store → R4)

| Input | Source | R4 use |
|-------|--------|--------|
| **Validated Snapshot Package** | Store read or in-memory post-Validate | Primary publish target — **read-only** (I-R4-01) |
| **`ValidationResult`** | R5.1 | Precondition — FAIL blocks default Publish (I-R4-02) |
| **`ValidateReport`** | R5.5 | Operator audit context — not re-validation (I-R4-03) |
| **`PublishEligibilityRecommendation`** | R5.6 | Advisory gate — NOT_ELIGIBLE blocks default (I-R4-04) |
| **Certified `package_quality_level`** | R5 ValidationResult | Freeze as published claim (I-R4-05) |
| **Snapshot identity** | R3.2 — `snapshot_id`, `site_id`, `acquisition_id` | Published reference keys (I-R4-06) |
| **Storage path binding** | R1.8B layout | Confirm placement — no redesign (I-R4-07) |
| **Operator Publish approval** | Operator HITL | Mandatory gate (I-R4-08) |
| **`consumer_target` declaration** | Operator / config | Publish metadata (I-R4-09) |
| **Architecture gate definitions** | EAR-READINESS-GATES-v1 G3–G4 | Publish checklist (I-R4-10) |

### Explicit non-inputs

| Artefact | Reason |
|----------|--------|
| Raw connector output | Pre-evidence — R1 |
| Evidence Package / quarantine bulk | Not consumer publish target |
| Candidate snapshot without R5 Validate | Lifecycle violation |
| R3 assembly eligibility alone | Precondition ≠ Validate pass |
| R2 structural pass alone | Pre-handoff ≠ certification |
| Live credentials | External secrets |
| R5 redaction findings for re-scan | R5 already reviewed — R4 confirms gate only |

---

## Outputs

### Required deliverables (engineering contracts)

| Deliverable | Description | Primary consumer |
|-------------|-------------|------------------|
| **Published Snapshot reference** | Consumer-visible identity + storage pointer | Consumer programs; operator registry |
| **PublishResult** | Aggregate publish outcome — SUCCESS / BLOCKED / DEFERRED | Operator; pipeline; audit |
| **Publish metadata** | `published_at`, `published_by`, `consumer_target` | Store metadata; acquisition-log |
| **Frozen `package_quality_level`** | Matches R5 certified — no inflation | Consumer intake |
| **Published state marker** | stored-unpublished → **published** transition | Store lifecycle |
| **Publish log / audit record** | Gate satisfaction; HITL refs | Operator; governance |
| **Consumer visibility grant** | Logical permission for registered consumers | Consume stage |
| **Supersession record** | When newer publish replaces active default | Operator; archive — **SAFE UNKNOWN** detail |

### Explicit non-outputs

| Output | Owner |
|--------|-------|
| `ValidationResult` / ValidateReport | **R5** |
| `PublishEligibilityRecommendation` | **R5** |
| Certified quality assignment | **R5** |
| OpenCart section population or mutation | **R3** |
| Evidence Package writes | **R2** |
| Consumer reports / OCPilot Run 5 execution | Consumer programs |
| Automatic Publish without HITL | **Forbidden** |

---

## Work Breakdown

Authoritative R4 work packages — ordered dependency chain.

### R4.1 — Published Snapshot Model

| Field | Value |
|-------|-------|
| **Mission** | Define the **Published Snapshot** as a consumer-visible promotion of the validated stored snapshot — same immutable OpenCart section tree, plus publish metadata and visibility grant. Establish identity contract distinct from candidate (R3) and validated (R5) stages. |
| **Ownership** | **R4** owns Published Snapshot reference definition and consumer citation semantics. R3 owns section content (frozen). R5 owns certification artefacts (input). Operator approves Publish. Consumer owns intake execution. |
| **Inputs** | [R4-CHARTER-v1.md](R4-CHARTER-v1.md) § Published Snapshot Definition; [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md); EAR-OPENCART-SNAPSHOT-SPEC-v1; R5.3 candidate vs certified matrix |
| **Outputs** | `PublishedSnapshotReference` contract spec; identity fields: `snapshot_id`, `site_id`, `snapshot_contract`, `parent_contract`; frozen section tree citation; published quality claim field; immutability rules PS-INV-R4-01–05; published vs validated vs candidate comparison table |
| **Dependencies** | R4 Charter complete; R5.3 quality stage semantics; R3.2 identity layer |
| **Non-goals** | Section mutation; quality certification; Validate re-run; evidence inclusion; consumer path copy implementation; ZIP layout |
| **Success criteria** | SC-R4.1-01: Published Snapshot defined as promotion not assembly; SC-R4.1-02: Same `snapshot_id` as validated stored snapshot; SC-R4.1-03: Section mutability forbidden at Publish; SC-R4.1-04: Three-stage quality semantics (candidate / certified / published freeze) documented |

#### Published Snapshot identity (ownership only)

| Property | Definition |
|----------|------------|
| **Identity** | Same `snapshot_id` as validated stored snapshot — consumer citation key |
| **Content** | Frozen OpenCart sections from Validate — R4 read-only |
| **Quality claim** | `package_quality_level` frozen from R5 certified level |
| **Publish markers** | `published_at`, `published_by`, `consumer_target` — R4 assigns |
| **Visibility** | Registered consumers may begin intake via published reference |
| **Secrets** | **None** — credentials never in published tree |
| **Evidence** | **Not included** — acquisition-log audit only |

---

### R4.2 — Publish State Model

| Field | Value |
|-------|-------|
| **Mission** | Define authoritative **publish lifecycle states** and **transition requirements** for snapshots from candidate through archive. R4 owns transitions into **published**, **superseded**, and publish-side **archived** markers — not candidate or validated certification states. |
| **Ownership** | **R4** owns published/superseded/archived publish-state transitions. **R5** owns validated marker. **R3** owns candidate. **Store (R1.8)** owns stored-unpublished placement. **Operator** owns retention/archive policy. |
| **Inputs** | [R4-CHARTER-v1.md](R4-CHARTER-v1.md) § Publish Lifecycle; R1.8B § Store vs Publish state transitions; EAR-SNAPSHOT-LIFECYCLE-v1; EAR-READINESS-GATES-v1 G3–G4 |
| **Outputs** | Publish state enumeration contract; state meaning table; transition requirement matrix; forbidden transitions (candidate→published, NOT_ELIGIBLE→published default); `publish_state` conceptual field mapping — exact encoding **SAFE UNKNOWN** |
| **Dependencies** | R4.1 (published identity); R5.1 ValidationResult outcomes |
| **Non-goals** | Store persist adapter implementation; validated-state marker (R5); candidate assembly states (R3); automation of supersession |
| **Success criteria** | SC-R4.2-01: Six lifecycle states chartered (candidate, validated, stored-unpublished, published, superseded, archived); SC-R4.2-02: stored-unpublished → published requirements explicit; SC-R4.2-03: Forbidden bypass transitions documented; SC-R4.2-04: Consumer access column per state |

#### Publish state semantics (ownership only)

| State | Meaning | Consumer access | R4 role |
|-------|---------|-----------------|---------|
| **candidate** | R3 assembly output | **None** | **Not R4** |
| **validated** | R5 pass recorded | **None** | Precondition |
| **stored-unpublished** | Immutable Store placement | **None** | Precondition — G3 |
| **published** | Publish gate executed | **Allowed** — registered consumers | **R4 target** |
| **superseded** | Newer published active for site | Historical cite only | **R4 records** |
| **archived** | Retention tier | Policy-dependent | Operator + R4 pointer |

---

### R4.3 — Consumer Visibility Model

| Field | Value |
|-------|-------|
| **Mission** | Define **who may access what** after R4 Publish and what remains **forbidden** before Publish. Establish consumer boundary rules (CB-R4-*) for intake, citation, and forbidden paths. |
| **Ownership** | **R4** grants visibility reference. **Consumer programs** own intake execution and contract validation on intake. **Operator** owns external paths and policy. **R2** owns quarantine — never consumer-visible. |
| **Inputs** | [R4-CHARTER-v1.md](R4-CHARTER-v1.md) § Consumer Boundary; EAR-SNAPSHOT-PUBLISHING-v1; EAR-OPENCART-CONSUMER-GUIDE-v1; R1.8B audience separation |
| **Outputs** | Consumer access matrix (allowed / forbidden); visibility grant contract; CB-R4-01–05 rules; OCPilot relationship statement; pre-Publish forbidden list; consumer-side Validate distinction (CB-R4-04) |
| **Dependencies** | R4.1; R4.2 published state |
| **Non-goals** | OCPilot Run 5 implementation; consumer credential handoff; consumer registry physical location implementation; webhook notification |
| **Success criteria** | SC-R4.3-01: Consumer intake requires published `snapshot_id`; SC-R4.3-02: stored-unpublished must not appear as active consumer target; SC-R4.3-03: Quarantine and secrets paths forbidden; SC-R4.3-04: Visibility grant distinct from credential handoff |

#### Consumer access rules (mandatory)

| Rule ID | Rule |
|---------|------|
| CB-R4-01 | Consumer intake **must** reference published `snapshot_id` |
| CB-R4-02 | Unpublished stored snapshot **must not** appear in consumer registry as active |
| CB-R4-03 | Publish **must not** expose operator `secrets/` paths |
| CB-R4-04 | Consumer-side contract validation on intake is **distinct** from EAR Validate (R5) |
| CB-R4-05 | Re-acquisition requires new Request cycle — consumer does not pull live SITE |

---

### R4.4 — Publish Metadata Model

| Field | Value |
|-------|-------|
| **Mission** | Define **R4-owned publish metadata fields** — assignment semantics, ownership, immutability after Publish, and physical encoding options (conceptual). Clarify R4 vs R5 vs operator field ownership. |
| **Ownership** | **R4** owns `published_at`, `published_by`, `consumer_target` assignment at Publish. **R5** owns certification timestamps on Validate. **Operator** declares `consumer_target` and approves Publish. **R3/R5** own pre-publish metadata fields — unchanged by R4 except publish markers. |
| **Inputs** | R4-CHARTER O-R4-03; R1.8B optional publish metadata; EAR-SNAPSHOT-PUBLISHING-v1; I-R4-08, I-R4-09 |
| **Outputs** | Publish metadata field contract; assignment timing (at Publish only); immutability policy post-Publish; metadata vs acquisition-log placement options — **SAFE UNKNOWN** encoding; ownership matrix for metadata fields |
| **Dependencies** | R4.1; R4.2 published state |
| **Non-goals** | Store adapter write implementation; acquisition-log parser; consumer registry write; ISO 8601 enforcement product |
| **Success criteria** | SC-R4.4-01: Three mandatory publish fields defined; SC-R4.4-02: R4 does not own Validate timestamps; SC-R4.4-03: Post-Publish in-place metadata edit discouraged; SC-R4.4-04: `consumer_target` required at Publish |

#### Publish metadata fields (contract only)

| Field | Required at Publish | R4 assigns | Notes |
|-------|---------------------|------------|-------|
| `published_at` | **Yes** | **Yes** | Publish execution timestamp |
| `published_by` | **Yes** | **Yes** | Operator ref / HITL identity |
| `consumer_target` | **Yes** | **Yes** | e.g. `ocpilot` — operator declaration |
| `package_quality_level` (published) | **Yes** | **Freeze** | Copy from R5 certified — no upgrade |
| `snapshot_id` | **Yes** | **No** — cite only | From R3.2 — unchanged |
| `published_snapshot_ref` | **Optional** | **Yes** | Consumer registry pointer — **SAFE UNKNOWN** |

---

### R4.5 — Publish Result Contract

| Field | Value |
|-------|-------|
| **Mission** | Define the aggregate **PublishResult** contract — the sole authoritative R4 publish outcome distinct from R5 `ValidationResult` and operator HITL decisions. Establish outcome states and their relation to publish lifecycle transitions. |
| **Ownership** | **R4** owns PublishResult emission. **R5** owns ValidationResult — R4 never substitutes. **Operator** owns HITL approval record — referenced not embedded as certification. |
| **Inputs** | R4-CHARTER O-R4-02; N-R4-03 distinct artefact mandate; R5.1 outcome disambiguation pattern |
| **Outputs** | `PublishResult` contract spec; outcome enum **SUCCESS**, **BLOCKED**, **DEFERRED**; fields: `outcome`, `snapshot_id`, `published_at` (when success), `blocker_reasons`, `gate_checklist_status`, `operator_approval_ref`, `consumer_target`; distinct artefact ID PR-INV-R4-01 |
| **Dependencies** | R4.2 state model; R4.6 flow contract |
| **Non-goals** | Serialization format; Store persist of result; conflation with ValidationResult; Validate report regeneration |
| **Success criteria** | SC-R4.5-01: Three outcomes defined; SC-R4.5-02: BLOCKED on NOT_ELIGIBLE default path; SC-R4.5-03: PublishResult ≠ ValidationResult explicit; SC-R4.5-04: SUCCESS requires all gate checklist items satisfied |

#### PublishResult outcome semantics (ownership only)

| Outcome | Meaning | Typical cause |
|---------|---------|---------------|
| **SUCCESS** | Publish gate executed; metadata set; visibility grant issued | All preconditions + Publish HITL |
| **BLOCKED** | Publish not executed — fail closed | ValidationResult FAIL; NOT_ELIGIBLE; missing HITL; mock id on production |
| **DEFERRED** | Operator deferred decision — no state transition | HITL pending; storage unconfirmed |

**Critical invariant:** `PublishResult.outcome` **≠** `ValidationResult.outcome` — Publish records promotion; Validate records certification (PR-INV-R4-01).

---

### R4.6 — Publish Flow Contract

| Field | Value |
|-------|-------|
| **Mission** | Define the **HITL publish flow** — gate checklist, R5 bundle consumption order, dual HITL placement (Validate sign-off + Publish approval), NOT_ELIGIBLE override path, and combined Store+Publish conceptual workflow. |
| **Ownership** | **R4** owns flow contract and gate checklist semantics. **Operator** owns both HITL gates. **R5** owns recommendation emission — R4 consumes only. |
| **Inputs** | R4-CHARTER § R5 → R4 Boundary; R5.6 recommendation semantics; EAR-READINESS-GATES-v1 G1–G4; VAL-INV-02; PE-INV-R5-01 |
| **Outputs** | Publish flow diagram; gate checklist contract; HITL requirements table; recommendation → Publish decision mapping; operator override audit requirements; combined Store+Publish conditions |
| **Dependencies** | R4.5 PublishResult; R5.6 Publish Eligibility contract |
| **Non-goals** | HITL UI product; webhook automation; unattended auto-Publish; Validate flow (R5) |
| **Success criteria** | SC-R4.6-01: Dual HITL documented — Validate ≠ Publish approval; SC-R4.6-02: NOT_ELIGIBLE blocks default path; SC-R4.6-03: ELIGIBLE ≠ auto-Publish; SC-R4.6-04: Gate checklist G1–G4 mapped to R4 confirmation roles |

#### HITL publish flow (mandatory)

```text
R5 Validate
        ↓
ValidationResult + ValidateReport + PublishEligibilityRecommendation
        ↓
Operator HITL #1 — Validate sign-off (mandatory pilot)
        ↓
Store — stored-unpublished (may precede or coincide)
        ↓
Operator HITL #2 — Publish approval (mandatory pilot)
        ↓
R4 Publish execution
        ↓
PublishResult + Published Snapshot reference
        ↓
Consume (consumer programs)
```

#### Recommendation → Publish decision (default path)

| PublishEligibilityRecommendation | Default R4 behavior | Operator override |
|----------------------------------|---------------------|-------------------|
| **ELIGIBLE** | May proceed after Publish HITL | — |
| **ELIGIBLE WITH NOTES** | May proceed after Publish HITL + note review | — |
| **NOT_ELIGIBLE** | **BLOCK** — PublishResult BLOCKED | Audited override — does not change R5 artefacts |

---

### R4.7 — Publish Engine Architecture

| Field | Value |
|-------|-------|
| **Mission** | Define **future implementation scope** for the Publish orchestrator — entry gate, precondition verification, metadata assignment, visibility grant emission. **No code** in this charter. |
| **Ownership** | **R4** owns Publish Engine scope. **Forbidden:** Validate category dispatch, section writers, evidence generators, quarantine writers. |
| **Inputs** | R4.1–R4.6 contracts; R5.7 Validate Engine pattern; R1.8B Store read path; R3.5 in-memory path |
| **Outputs** | Publish Engine scope document; entry preconditions; processing pipeline (conceptual); output bundle: PublishResult + PublishedSnapshotReference + publish metadata + state marker + visibility grant; CLI flag spec (e.g. `--publish-snapshot` — **future**); fail-closed behavior |
| **Dependencies** | R4.1–R4.6 complete |
| **Non-goals** | Implementation code; Store adapter redesign; network I/O; Validate side effects; consumer bulk copy |
| **Success criteria** | SC-R4.7-01: Inputs limited to chartered R4 input set; SC-R4.7-02: Outputs match O-R4-01–08; SC-R4.7-03: Entry gate rejects without R5 bundle; SC-R4.7-04: No section mutation in pipeline |

#### Publish Engine scope (future implementation)

| Phase | Behavior |
|-------|----------|
| **Entry gate** | Require validated SnapshotPackage + R5 bundle; reject candidate-only; reject mock id on production path |
| **Precondition check** | ValidationResult not FAIL; PublishEligibility not NOT_ELIGIBLE (default); Store placement confirmed or memory path flagged |
| **HITL verification** | Require operator Publish approval ref — fail closed if absent (pilot) |
| **Metadata assignment** | Set `published_at`, `published_by`, `consumer_target`; freeze quality claim |
| **State transition** | Mark publish_state **published** — encoding per R4.2 |
| **Visibility grant** | Emit consumer visibility grant for registered target |
| **Result emission** | Build PublishResult + PublishedSnapshotReference |
| **Side effects** | **Metadata only** — no section mutation, no evidence, no Validate re-run |

```text
Inputs                          Publish Engine                  Outputs
────────                        ──────────────                  ───────
Validated SnapshotPackage  →    entry gate                 →    PublishResult
R5 bundle (3 artefacts)    →    precondition check         →    PublishedSnapshotReference
Operator Publish approval  →    metadata assignment        →    Publish metadata
consumer_target            →    state transition           →    Visibility grant
                               (no Validate, no assembly)
```

---

### R4.8 — Publish Boundary Review

| Field | Value |
|-------|-------|
| **Mission** | Reserve milestone to **verify** R4 engineering and future implementation do not absorb R5 Validate, R3 assembly, R2 evidence, or consumer program execution. Pattern: [R5.8-VALIDATION-BOUNDARY-REVIEW-v1.md](R5.8-VALIDATION-BOUNDARY-REVIEW-v1.md), [R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md](R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md). |
| **Ownership** | **R4.8** produces boundary review artefact. Does not reassign ownership — verifies matrix. |
| **Inputs** | R4.1–R4.7 contracts; R5.8 VB-R5-01–15; R3.6 VB-R3-01–18; R2.4 VAL-INV-01–14; R4-CHARTER ownership matrix |
| **Outputs** | R4.8 boundary review document; R2/R3/R5/R4/Consumer ownership matrix update; overlap verdict; invariants PB-R4-01+ (new); recommendations if creep detected |
| **Dependencies** | R4.1–R4.7 design complete; R4.7 scope documented |
| **Non-goals** | Publish engine code changes unless critical violation; architecture redesign; Validate implementation |
| **Success criteria** | SC-R4.8-01: No Validate execution in R4 scope; SC-R4.8-02: No quality certification in R4 scope; SC-R4.8-03: No section assembly in R4 scope; SC-R4.8-04: No evidence generation in R4 scope |

#### Mandatory boundary reviews (this milestone)

| Review | Expected verdict |
|--------|------------------|
| **R5 → R4 transition** | R5 recommends; R4 publishes; recommendation ≠ execution |
| **Published Snapshot ownership** | R4 owns reference + metadata; R3/R5 content frozen; no new assembly |
| **Consumer boundary** | Visibility after Publish only; CB-R4-01–05 satisfied |
| **Store vs Publish distinction** | Store precondition; Publish executes G4; stored-unpublished ≠ published |
| **HITL requirements** | Dual HITL mandatory pilot; auto-Publish forbidden |

#### Boundary verification checklist

| Check | Expected owner |
|-------|----------------|
| OpenCart section population | **R3** |
| EAR Validate / certification | **R5** |
| `package_quality_level` certification | **R5** |
| Quality claim freeze at Publish | **R4** |
| Publish execution | **R4** |
| Publish Eligibility Recommendation emit | **R5** |
| Evidence Package writes | **R2** |
| Store layout / stored-unpublished persist | **R1.8** — frozen |
| Consumer delivery / OCPilot Run 5 | **Consumer programs** |
| Publish metadata assignment | **R4** |

---

### R4.9 — R4 Readiness Review

| Field | Value |
|-------|-------|
| **Mission** | **Final gate** before R4 code implementation authorization. Verify IAC-R4-01–06; document debt; update program state. |
| **Ownership** | **R4.9** produces readiness review and decision artefacts. Does not authorize code without human gate. |
| **Inputs** | All R4.1–R4.8 deliverables; R4 Implementation Charter success criteria; mock R5 bundle availability |
| **Outputs** | R4-READINESS-REVIEW-v1; R4-READINESS-DECISION-v1; updated [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) |
| **Dependencies** | R4.8 boundary review pass; R4.1–R4.7 contracts complete |
| **Non-goals** | Live pilot execution; Validate Engine implementation; OCPilot integration |
| **Success criteria** | SC-R4.9-01: All R4.1–R4.8 artefacts exist; SC-R4.9-02: IAC-R4-01–06 assessed; SC-R4.9-03: R4 code authorization decision recorded; SC-R4.9-04: Debt and SAFE UNKNOWN catalogued |

---

### Work package classification summary

| Package | Classification |
|---------|----------------|
| R4.1 Published Snapshot Model | **Required** |
| R4.2 Publish State Model | **Required** |
| R4.3 Consumer Visibility Model | **Required** |
| R4.4 Publish Metadata Model | **Required** |
| R4.5 Publish Result Contract | **Required** |
| R4.6 Publish Flow Contract | **Required** |
| R4.7 Publish Engine Architecture | **Required** (scope only — code after R4.9) |
| R4.8 Publish Boundary Review | **Required** |
| R4.9 R4 Readiness Review | **Required** |
| Publish state Store encoding | **SAFE UNKNOWN** — R4.2 implementation |
| Consumer registry pointer write | **SAFE UNKNOWN** — R4.3/R4.7 |
| `--publish-snapshot` CLI | **Future** — R4.7 implementation |
| Contract-path Store read adapter | **R3 debt** — parallel |

---

## Implementation Sequence

```text
R4.1 Published Snapshot Model
        ↓
R4.2 Publish State Model
        ↓
R4.3 Consumer Visibility Model ────┐
R4.4 Publish Metadata Model   ───┼── (parallel after R4.2)
        ↓                          │
R4.5 Publish Result Contract  ←───┘
        ↓
R4.6 Publish Flow Contract
        ↓
R4.7 Publish Engine (scope)
        ↓
R4.8 Publish Boundary Review (parallel with late R4.7)
        ↓
R4.9 R4 Readiness Review
        ↓
Human gate → R4.1 code (Published Snapshot Model implementation)
```

**Note:** R4.3 and R4.4 may proceed in parallel after R4.2. R4.8 may start when R4.1–R4.7 contracts are draft-complete.

---

## Publish Boundary

**Terminology (mandatory):**

| Term | Program | Meaning |
|------|---------|---------|
| **Store** | R1.8 | Immutable validated snapshot placement — operator/EAR audience |
| **R5 EAR Validate** | R5 | Contract certification, quality, redaction, publish readiness recommendation |
| **R4 Publish** | R4 | Consumer visibility promotion — metadata + reference |
| **Consume** | Consumer programs | Intake execution post-Publish |

### R4 may execute (EAR Publish — promotion only)

| Action class | Notes |
|--------------|-------|
| Read validated snapshot — no mutation | Primary publish target |
| Consume R5 bundle as preconditions | ValidationResult, ValidateReport, PublishEligibilityRecommendation |
| Assign publish metadata | R4-owned fields only |
| Freeze certified quality claim | Match R5 — no inflation |
| Transition publish_state to published | Per R4.2 |
| Emit PublishedSnapshotReference | Consumer citation |
| Emit PublishResult | Distinct from ValidationResult |
| Grant consumer visibility | Logical permission — not credential handoff |
| Record supersession pointer | When newer publish exists — **SAFE UNKNOWN** automation |

### R4 must not execute (owned elsewhere)

| Action class | Owner |
|--------------|-------|
| EAR Validate / contract certification | **R5** |
| Quality possession assessment | **R5** |
| Redaction review | **R5** |
| Publish Eligibility Recommendation emission | **R5** |
| OpenCart section population or mutation | **R3** |
| Evidence Package writes / quarantine mutation | **R2** |
| Store layout redesign | **Frozen** R1.9 |
| Consumer program execution | **Consumer programs** |
| Acquisition / connector execution | **R1** |

### Overlap prevention (authoritative)

| Boundary | Rule |
|----------|------|
| R5 ↔ R4 | R5 recommends; R4 publishes; R4 never validates or certifies |
| R3 ↔ R4 | R3 assembles; R4 reads frozen sections — never mutates |
| R2 ↔ R4 | R4 never reads quarantine as publish target |
| R4 ↔ Store | R4 uses frozen layout — metadata write only at Publish |
| R4 ↔ Operator | Operator owns dual HITL, `consumer_target`, override audit |
| R4 ↔ Consumer | R4 grants reference; consumer owns intake execution |

---

## Mandatory reviews (consolidated)

### 1. R5 → R4 transition

| R5 output | R4 consumption | R4 must not |
|-----------|----------------|-------------|
| `ValidationResult` | Precondition — FAIL blocks default Publish | Re-run certification |
| `ValidateReport` | Operator context for Publish decision | Regenerate report |
| `PublishEligibilityRecommendation` | Gate — NOT_ELIGIBLE blocks default | Emit recommendation |
| Certified `package_quality_level` | Freeze as published claim | Upgrade or reassess |
| Redaction findings | Confirm addressed — not re-scan | Own redaction review |

### 2. Published Snapshot ownership

| Concern | Owner |
|---------|-------|
| OpenCart section content | **R3** wrote; **R5** certified freeze; **R4** read-only |
| Published reference identity | **R4** |
| Publish metadata | **R4** |
| Consumer intake execution | **Consumer programs** |
| Immutability per `snapshot_id` | Architecture — R4 preserves |

### 3. Consumer boundary

See § R4.3 — CB-R4-01–05. Consumer visibility **begins only after Publish**.

### 4. Store vs Publish distinction

See § Mandatory questions — Why Store ≠ Publish. Store satisfies G3; Publish executes G4.

### 5. HITL requirements

| Gate | Owner | Mandatory (pilot) |
|------|-------|-------------------|
| Validate sign-off | Operator | **Yes** |
| Publish approval | Operator | **Yes** |
| NOT_ELIGIBLE override | Operator + audit | Exception only |
| Auto-Publish without HITL | — | **Forbidden** |

---

## Engineering Acceptance (post-implementation — not this document)

| ID | Criterion | Source |
|----|-----------|--------|
| IAC-R4-01 | Operator can execute Publish on validated snapshot with R5 bundle | Backlog § R4 |
| IAC-R4-02 | Published reference immutable; publish log records gate satisfaction | Backlog § R4 |
| IAC-R4-03 | Published quality matches R5 certified level — no inflation | EAR-OPENCART-QUALITY-MAPPING-v1 |
| IAC-R4-04 | NOT_ELIGIBLE blocks default Publish — fail closed | R5.6; EAR-READINESS-GATES-v1 |
| IAC-R4-05 | R4 does not re-validate or modify sections | R4-CHARTER § Scope |
| IAC-R4-06 | Consumer intake possible only after Publish completes | EAR-SNAPSHOT-PUBLISHING-v1 |

---

## Success Criteria

R4 **Implementation Charter** is **complete** when:

| ID | Criterion | Verification |
|----|-----------|--------------|
| SC-IC-R4-01 | All work packages R4.1–R4.9 defined with mission, ownership, inputs, outputs, dependencies, non-goals, success criteria | § Work Breakdown |
| SC-IC-R4-02 | Published Snapshot defined as promotion — not assembly | § R4.1; Mandatory questions |
| SC-IC-R4-03 | Publish state model with forbidden bypass transitions | § R4.2 |
| SC-IC-R4-04 | Consumer visibility rules CB-R4-01–05 | § R4.3 |
| SC-IC-R4-05 | Publish metadata ownership — R4 fields only | § R4.4 |
| SC-IC-R4-06 | PublishResult distinct from ValidationResult | § R4.5 |
| SC-IC-R4-07 | HITL publish flow — dual gate documented | § R4.6 |
| SC-IC-R4-08 | Publish Engine future scope — no code | § R4.7 |
| SC-IC-R4-09 | R5/R3/R2 boundaries preserved | § Publish Boundary; R4.8 reserved |
| SC-IC-R4-10 | Mandatory questions explicitly answered | § Mandatory questions |
| SC-IC-R4-11 | Five mandatory reviews addressed | § Mandatory reviews |
| SC-IC-R4-12 | R4.9 Readiness Review reserved as final gate | § R4.9 |
| SC-IC-R4-13 | N-R4-01–12 reflected | § Dependencies; Planning notes |
| SC-IC-R4-14 | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) and [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) updated | Program navigation |

---

## Stop Conditions

Stop or escalate **before** R4 code implementation if:

| ID | Condition | Action |
|----|-----------|--------|
| ST-IC-R4-01 | Implementation charter includes **Validate execution** or quality certification | **STOP** — reclassify as R5 |
| ST-IC-R4-02 | Charter includes **snapshot assembly** or section writers | **STOP** — reclassify as R3 |
| ST-IC-R4-03 | Charter includes **evidence generation** or quarantine persist | **STOP** — reclassify as R2 |
| ST-IC-R4-04 | Charter allows **Publish without Validate** or without R5 bundle | **STOP** — violates lifecycle |
| ST-IC-R4-05 | Quality certification assigned to R4 | **STOP** — quality inflation |
| ST-IC-R4-06 | Publish Engine proposed with **runtime code** in this charter phase | **STOP** — charter is planning only |
| ST-IC-R4-07 | Publish recommendation conflated with Publish execution | **STOP** — VAL-INV-02 |
| ST-IC-R4-08 | SITE-001, PILOT-001, live SFTP required | **STOP** — Execution Authorization |
| ST-IC-R4-09 | Store redesign contradicting R1.9 | **STOP** — architecture amendment |
| ST-IC-R4-10 | Unattended auto-Publish replacing operator HITL | **STOP** — backlog non-goal |
| ST-IC-R4-11 | OCPilot Run 5 chartered as R4 deliverable | **STOP** — consumer program |
| ST-IC-R4-12 | Section mutation at Publish permitted | **STOP** — ST-R4-06 |

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| R4 label confusion — Publish implemented as Validate or assembly | High | Mission; Stop Conditions; R4.8 boundary review |
| Publish before Validate or without R5 bundle | High | ST-IC-R4-04; Entry gate R4.7 |
| Quality inflation at Publish | High | Mandatory questions; ST-IC-R4-05 |
| ELIGIBLE recommendation treated as auto-Publish | High | R4.6 dual HITL; SC-R4.6-03 |
| R4 mutates validated sections during Publish | High | R4.1 immutability; ST-IC-R4-12 |
| Stored-unpublished exposed to consumers | High | R4.3 CB-R4-02 |
| R4 re-implements R5 redaction or possession checks | Medium | Scope non-goals; R5 ownership |
| Combined Store+Publish bypasses Validate HITL | Medium | R4.6 flow — both gates required |
| Mock snapshot_id published to production | Medium | R4.7 entry gate; A-R4-08 |
| Dual HITL fatigue — operators skip Publish approval | Medium | ST-IC-R4-10 |

---

## SAFE UNKNOWN

| Topic | Status | Owner |
|-------|--------|-------|
| PublishResult serialization format | R4.5 implementation | R4.1+ code |
| `publish_state` Store encoding | R4.2 implementation | R4-adjacent |
| Consumer registry pointer location | R1.8B OQ-04 | R4.3/R4.7 |
| Physical publish metadata encoding (metadata/ vs acquisition-log/) | R4.4 implementation | R4 |
| Official JSON Schema for Publish artefacts | Not in repo | Architecture |
| Supersession automation — active default per site | Architecture | Future |
| Operator override audit schema on NOT_ELIGIBLE | Operator workflow | HITL |
| Atomic Publish + metadata write failure recovery | R4.7 implementation | R4 |
| `--publish-snapshot` CLI flag name | R4.7 implementation | R4 |
| 1:N acquisition_id → snapshot_id publish policy | Architecture | Future |
| Whether R4 copies contract slice to consumer path vs reference only | R1.8B hybrid model | R4.7 |
| Post-Publish Validate artefact retention | Operator / governance | Policy |

---

## Planning notes (carried from R4 Charter)

| Note | Action |
|------|--------|
| N-R4-01 | Title work R4 — EAR Publish Layer — **satisfied** § Charter identity |
| N-R4-02 | Consume R5 bundle — not R3 assembly result alone — **satisfied** § Inputs |
| N-R4-03 | Distinct PublishResult — **satisfied** § R4.5 |
| N-R4-04 | Separate Publish HITL — **satisfied** § R4.6 |
| N-R4-05 | Human HITL mandatory — **satisfied** § R4.6 |
| N-R4-06 | Fail closed on NOT_ELIGIBLE — **satisfied** § R4.6 |
| N-R4-07 | Disambiguate R5 Validate / R4 Publish — **satisfied** § Publish Boundary |
| N-R4-08 | Read-only promotion — **satisfied** § R4.1 |
| N-R4-09 | Consumer registry pointer — **tracked** § SAFE UNKNOWN |
| N-R4-10 | Human implementation approval gate — **satisfied** § Charter identity |
| N-R4-11 | Mock R5 bundle for engineering — **satisfied** § Dependencies |
| N-R4-12 | Stored and in-memory validated inputs — **satisfied** § R4.7 |

---

## Evidence index

| ID | Source |
|----|--------|
| E-R4I-01 | [R4-CHARTER-v1.md](R4-CHARTER-v1.md) |
| E-R4I-02 | [R4-DECISION-v1.md](R4-DECISION-v1.md) |
| E-R4I-03 | [R5-READINESS-DECISION-v1.md](R5-READINESS-DECISION-v1.md) |
| E-R4I-04 | [R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md](R5.6-PUBLISH-ELIGIBILITY-CONTRACT-v1.md) |
| E-R4I-05 | [R5.8-VALIDATION-BOUNDARY-DECISION-v1.md](R5.8-VALIDATION-BOUNDARY-DECISION-v1.md) |
| E-R4I-06 | [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) § Store vs Publish |
| E-R4I-07 | [EAR-SNAPSHOT-PUBLISHING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-PUBLISHING-v1.md) |
| E-R4I-08 | [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md) |
| E-R4I-09 | [R3-READINESS-DECISION-v1.md](R3-READINESS-DECISION-v1.md) |
| E-R4I-10 | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R4 |

---

## Cross-references

| Document | Use |
|----------|-----|
| [R4-IMPLEMENTATION-DECISION-v1.md](R4-IMPLEMENTATION-DECISION-v1.md) | Implementation gate decision |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Program status |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation |
