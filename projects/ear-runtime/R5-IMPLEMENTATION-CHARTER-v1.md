# R5 — EAR Validate Implementation Charter v1

**Type:** Implementation engineering charter — **no** runtime code, **no** validator implementation, **no** Publish in this document  
**Date:** 2026-06-06  
**Phase:** R5 — EAR Validate Layer  
**Lane:** B — EAR Runtime Engineering  
**Prior gates:** R1 **COMPLETE**; R2 **COMPLETE WITH NOTES**; R3 **COMPLETE WITH NOTES**; [R5-CHARTER-v1.md](R5-CHARTER-v1.md) **COMPLETE**; [R5-DECISION-v1.md](R5-DECISION-v1.md) — **APPROVED WITH NOTES**  
**Decision companion:** [R5-IMPLEMENTATION-DECISION-v1.md](R5-IMPLEMENTATION-DECISION-v1.md)  
**Architecture sources:** [shared/external-access-runtime/](../../shared/external-access-runtime/)

---

## Charter identity

| Field | Value |
|-------|-------|
| **Authorizes** | R5 engineering scope, work packages R5.1–R5.9, Validation Result model, category ownership, quality possession certification, redaction review contract, Validate Report contract, Publish Eligibility recommendation contract, Validate Engine scope, R2/R3/R5 boundary verification, implementation sequence — **not** R4 Publish execution, snapshot assembly, evidence generation, or live acquisition |
| **Does not authorize** | Validate automation code, Publish execution, Store redesign, section population, OCPilot integration, SITE-001 / PILOT execution, live SFTP, normative JSON Schema files |
| **Human approver** | **Pending** — see [R5-IMPLEMENTATION-DECISION-v1.md](R5-IMPLEMENTATION-DECISION-v1.md) |
| **Program label** | **R5 — EAR Validate Layer** / Validation Helpers — **not** Publish or Snapshot Assembly |

---

## Mission

### Why R5 engineering exists

R3 closed with an operational **candidate** Snapshot Package on `--contract-snapshot` at honest `package_quality_level: 0` ([R3-READINESS-DECISION-v1.md](R3-READINESS-DECISION-v1.md)). R5 engineering translates the approved [R5-CHARTER-v1.md](R5-CHARTER-v1.md) into **executable scope** before any Validate code: contract models for certification outcomes, category ownership, possession concepts, redaction review, operator-facing reports, Publish eligibility recommendations, and boundary gates — producing **validated snapshot certification artefacts** distinct from R2/R3 eligibility results.

### What R5 engineering builds (conceptually)

**EAR Validate** certifies that a candidate snapshot satisfies contract, possession, redaction, and readiness requirements per architecture gates. R5 engineering defines **contracts and orchestration scope** — not acquisition, not assembly, not Publish.

```text
R3 Candidate Snapshot Package (package_quality_level: 0)
        ↓
R3 assembly eligibility (precondition — not R5)
        ↓
R5 EAR Validate                    ← R5 engineering scope
        ↓
ValidationResult + ValidateReport + Certified level + PublishEligibilityRecommendation
        ↓
Operator HITL (mandatory for pilot)
        ↓
R4 Publish                           ← not R5
```

### Gap R5 engineering closes (evidence-backed)

| Post-R3 state | R5 engineering target |
|---------------|------------------------|
| Candidate quality uncertified at L0 placeholder | Certified `package_quality_level` L0–L3 per possession assessment |
| No Validate report artefact | Operator-facing `ValidateReport` by category |
| No Publish readiness signal | `PublishEligibilityRecommendation` — recommendation only |
| R3 assembly pass conflated with certification | Distinct `ValidationResult` with PASS / PASS WITH NOTES / FAIL |
| No redaction enforcement on candidate | Redaction review model and findings contract |
| R2/R3/R5 terminology collision | Category model + boundary review milestone |

---

## Engineering Scope

### In scope (R5 implementation — when human gate approves code)

| ID | Area | Engineering deliverable |
|----|------|-------------------------|
| S-R5-01 | Validation Result Model | `ValidationResult` contract — PASS / PASS WITH NOTES / FAIL; relation to Publish recommendation |
| S-R5-02 | Validation Category Model | Authoritative categories: Identity, Structure, Possession, Quality, Redaction, Readiness, Consistency |
| S-R5-03 | Quality Possession Model | L0–L3 certification concepts; candidate L0 ≠ certified possession |
| S-R5-04 | Redaction Review Model | Secret/credential/unsafe-publication review ownership — no scanner design |
| S-R5-05 | Validate Report Contract | Operator-facing report sections — no format implementation |
| S-R5-06 | Publish Eligibility Contract | ELIGIBLE / ELIGIBLE WITH NOTES / NOT ELIGIBLE — R5 recommends; R4 decides |
| S-R5-07 | Validate Engine | Future orchestration scope — inputs, outputs, category dispatch |
| S-R5-08 | Validation Boundary Review | Verify R5 does not absorb R3 or R4 |
| S-R5-09 | R5 Readiness Review | Final gate before R5 code authorization |

### Out of scope (explicit)

| Item | Owner |
|------|-------|
| Snapshot assembly / section population | **R3** |
| Evidence generation / quarantine writes | **R2** |
| Acquisition / connector execution | **R1** + Execution Authorization |
| Publish execution / consumer reference | **R4** |
| Store layout redesign | **Frozen** R1.9 |
| R2 structural evidence re-validation (full duplicate) | **R2** — R5 reads evidence for consistency only |
| R3 assembly eligibility duplication as certification | **R3** — precondition only |
| Unattended production Validate gate | **Non-goal** per backlog |
| Automated redaction engine product | Future / operator policy |
| Normative JSON Schema / ZIP layout files | **SAFE UNKNOWN** |
| OCPilot integration | Consumer program |

### Code placement (when implementation authorized)

R5 code may extend **only** under:

```text
projects/ear-runtime/runtime/
```

Likely paths (chartered, not prescriptive filenames):

| Path | Role |
|------|------|
| `runtime/shared/validation_result_models.py` | ValidationResult, category enums, possession record contracts |
| `runtime/shared/validate_report_models.py` | ValidateReport, PublishEligibilityRecommendation contracts |
| `runtime/validators/ear_validate_engine.py` | Validate orchestrator — **R5.7 implementation** |
| `runtime/validators/validate_category_*.py` | Per-category assessors — **future after R5.1–R5.6** |

**Forbidden:** `shared/external-access-runtime/` amendments without Architecture Amendment Charter; consumer path writes; Publish metadata mutation; OpenCart section population; evidence quarantine mutation.

---

## Dependencies

| Predecessor | Requirement |
|-------------|-------------|
| R1 | **COMPLETE** — mock pipeline, Store layout frozen |
| R2 | **COMPLETE WITH NOTES** — R2.1 model, R2.4 boundary, `--contract-evidence` |
| R3 | **COMPLETE WITH NOTES** — R3.1 `SnapshotPackage`, R3.5 `--contract-snapshot`, R3.6 boundary |
| R5 Charter | **COMPLETE** — [R5-CHARTER-v1.md](R5-CHARTER-v1.md), [R5-DECISION-v1.md](R5-DECISION-v1.md) |
| Architecture | EAR-OPENCART-SNAPSHOT-SPEC-v1, EAR-OPENCART-QUALITY-MAPPING-v1, EAR-SNAPSHOT-CONTRACT-v1, EAR-READINESS-GATES-v1, EAR-SNAPSHOT-LIFECYCLE-v1 |

### Inherited assumptions (from R3 readiness — A-R5-01–10)

| ID | Assumption |
|----|------------|
| A-R5-01 | R3 delivers candidate at `package_quality_level: 0` — R5 owns certification ≥ 0 honest claim |
| A-R5-02 | R3 assembly pass **≠** R5 EAR Validate pass (VB-R3-01) |
| A-R5-03 | Empty L1 section + matching safe-unknown = valid R3 output — R5 certifies possession separately |
| A-R5-04 | Contract-path candidate may be in-memory — R5 must support memory and Store read |
| A-R5-05 | Mock `snapshot_id` dry-run only — R5 reads id, does not create |
| A-R5-06 | Quarantine bulk may be absent on disk — live Validate may depend on R2 persist follow-on |
| A-R5-07 | R5 targets R3.1 `SnapshotPackage` — not R1.7 flat model |
| A-R5-08 | R3 safe-unknown presence ≠ gap completeness for certify level (VB-R3-08) |
| A-R5-09 | R5 owns redaction, publish readiness, Validate report — none in R3 |
| A-R5-10 | Terminology: R2 structural / R3 assembly eligibility / R5 EAR Validate |

### R3 debt (non-blocking for implementation charter)

| Debt | R5 handling |
|------|-------------|
| Contract-path Store persist adapter | R5 may read in-memory candidate; Store marker **SAFE UNKNOWN** at R5.1 |
| Bulk expansion (HO-ALLOW-10) | May block **live** L1+ Validate — not charter blocker |
| R1.6 parallel mock path | R5 consumes R3.1 only — VB-R3-18 |

---

## Inputs

### Authoritative upstream (R3 → R5)

| Input | Source | R5 use |
|-------|--------|--------|
| **Candidate Snapshot Package** | R3.5 `build_candidate_snapshot_package()` / Store read | Primary validation target (I-R5-01) |
| **R3 assembly eligibility result** | `validate_candidate_snapshot_package()` | Precondition — not certification (I-R5-06) |
| **`safe-unknown/` section** | R3.4 propagation | Gap completeness review (I-R5-02) |
| **`acquisition-log/` section** | R3 assembly | Audit correlation (I-R5-03) |
| **Snapshot identity** | R3.2 | Identity category (I-R5-04) |
| **OpenCart section tree** | R3.1 aggregate | Structure, possession, consistency (I-R5-05) |
| **Evidence Package (read-only)** | R2.1 / quarantine | Provenance consistency — not R2 re-run (I-R5-07) |
| **R2 structural validation result** | `EvidenceValidationResult` when supplied | Precondition flag (I-R5-08) |
| **Identity Continuity Record** | R3 `build_identity_continuity_record()` | Audit sidecar (I-R5-09) |
| **Target certify level** | Operator / Request declaration | Possession assessment target (I-R5-11) |
| **Architecture gate definitions** | EAR-READINESS-GATES-v1 | Readiness category (I-R5-12) |

### Explicit non-inputs

| Artefact | Reason |
|----------|--------|
| Raw connector output | Pre-evidence — R1 |
| R3 assembly pass alone | Precondition ≠ Validate pass |
| R2 structural pass alone | Pre-handoff ≠ snapshot certification |
| Published snapshot reference | R4 downstream |
| Consumer paths | Post-Publish only |

---

## Outputs

### Required deliverables (engineering contracts)

| Deliverable | Description | Primary consumer |
|-------------|-------------|------------------|
| **ValidationResult** | Aggregate certification outcome — PASS / PASS WITH NOTES / FAIL | Operator; pipeline; R4 pre-check |
| **ValidateReport** | Operator-facing structured findings by category | Operator HITL; audit |
| **Certified `package_quality_level`** | L0–L3 possession-assessed honest claim | Store metadata; R4 Publish |
| **PublishEligibilityRecommendation** | ELIGIBLE / ELIGIBLE WITH NOTES / NOT ELIGIBLE | **R4** Publish; operator |
| **PossessionAssessmentRecord** | Section-level level satisfaction audit | Audit; post-Publish metadata |
| **RedactionFindings** | Secrets/PII blockers | Operator; R4 pre-Publish |
| **Validated snapshot state marker** | Candidate → validated lifecycle transition | Store — exact marker **SAFE UNKNOWN** at R5.1 |

### Explicit non-outputs

| Output | Owner |
|--------|-------|
| Published snapshot / consumer reference | **R4** |
| `published_at`, publish metadata | **R4** |
| OpenCart section population or mutation | **R3** |
| Evidence Package writes | **R2** |
| Automatic Publish without HITL | **Forbidden** |

---

## Work Breakdown

Authoritative R5 work packages — ordered dependency chain.

### R5.1 — Validation Result Model

| Field | Value |
|-------|-------|
| **Purpose** | Define the aggregate **ValidationResult** contract — the sole authoritative R5 certification outcome distinct from R2 `EvidenceValidationResult` and R3 assembly eligibility `{valid, errors}`. Establishes three outcome states and their semantic relation to Publish Eligibility Recommendation. |
| **Inputs** | [R5-CHARTER-v1.md](R5-CHARTER-v1.md) § Outputs O-R5-01; R2.4 VAL-INV-01; R3.6 VB-R3-01; N-R5-03 |
| **Outputs** | `ValidationResult` contract spec; outcome enum **PASS**, **PASS WITH NOTES**, **NOT ELIGIBLE** mapping to Publish recommendation; fields: `outcome`, `certified_quality_level`, `target_certify_level`, `category_summaries` (refs), `blocker_count`, `warning_count`, `precondition_flags` (R2/R3 pass supplied); distinct artefact ID |
| **Dependencies** | R5 Charter complete; R3.6 boundary documented |
| **Non-goals** | Validator implementation; rule IDs (R5-V-*); serialization format; Store persist of result |
| **Success criteria** | SC-R5.1-01: Three outcomes defined with mandatory disambiguation from R2/R3 results; SC-R5.1-02: PASS WITH NOTES ≠ Publish approval alone — requires operator HITL; SC-R5.1-03: FAIL blocks NOT ELIGIBLE recommendation; SC-R5.1-04: Relation to PublishEligibilityRecommendation documented (see § Validation Result ↔ Publish) |

#### ValidationResult outcome semantics (ownership only)

| Outcome | Meaning | Typical Publish Eligibility |
|---------|---------|----------------------------|
| **PASS** | All mandatory category checks satisfied for certified level; no blockers | **ELIGIBLE** (subject to operator HITL) |
| **PASS WITH NOTES** | Certified level achievable; non-blocking warnings or downgrade notes present | **ELIGIBLE WITH NOTES** |
| **FAIL** | Mandatory blocker present — possession uncertain, redaction failure, contract breach, or precondition not met | **NOT ELIGIBLE** |

**Critical invariant:** `ValidationResult.outcome` **≠** `PublishEligibilityRecommendation` — result certifies snapshot quality; recommendation advises R4. R5 **never** executes Publish (VAL-INV-02; VB-R3-02).

#### Validation Result ↔ Publish recommendation

```text
ValidationResult                    PublishEligibilityRecommendation
────────────────                    ────────────────────────────────
PASS                          →     ELIGIBLE (default mapping)
PASS WITH NOTES               →     ELIGIBLE WITH NOTES
FAIL                          →     NOT ELIGIBLE (fail closed)

Operator HITL required for ALL paths before R4 Publish (pilot non-goal override forbidden)
```

R5 emits **both** artefacts from Validate Engine (R5.7). R4 **reads** recommendation; operator **approves** Publish — Validate pass alone is insufficient (ST-R5-04).

---

### R5.2 — Validation Category Model

| Field | Value |
|-------|-------|
| **Purpose** | Define authoritative **validation categories** — ownership and purpose only. Each category scopes future R5-V-* rules without defining rules in this charter. |
| **Inputs** | [R5-CHARTER-v1.md](R5-CHARTER-v1.md) § Validation Categories; R2.4 ownership matrix; R3.6 category boundaries |
| **Outputs** | Category enumeration contract; per-category purpose, primary inputs, R2/R3/R5 owner column; category finding shape (id, severity, message — conceptual); overlap prevention table |
| **Dependencies** | R5.1 (result aggregates category summaries) |
| **Non-goals** | Per-category rule implementation; R5-V-* rule IDs; automated gate product |
| **Success criteria** | SC-R5.2-01: All seven categories chartered; SC-R5.2-02: Each category has single R5 owner; SC-R5.2-03: R2/R3 complementary checks documented — no duplication as certification; SC-R5.2-04: Terminology disambiguation retained (N-R5-07) |

#### Authoritative categories

| Category | Purpose | Primary inputs | R5 owns |
|----------|---------|----------------|---------|
| **Identity** | Snapshot and site identity integrity; contract version; acquisition correlation | I-R5-04, metadata, acquisition-log | **Yes** — R3 creates ids; R5 certifies correctness |
| **Structure** | OpenCart section tree completeness vs spec skeleton; forbidden field absence | I-R5-05, I-R5-01 | **Yes** — distinct from R3 assembly skeleton check |
| **Possession** | Section content adequacy for target certify level; corroboration where required | Section payloads, safe-unknown | **Yes** — exclusive owner |
| **Quality** | Map possession to L0–L3; downgrade paths; inflation detection | Quality mapping, target level, possession record | **Yes** — exclusive certifier |
| **Redaction** | Secrets/PII in candidate; pre-consumer path safety | Candidate serialization, bulk refs | **Yes** — R3 avoids copy; R5 enforces |
| **Readiness** | Gate G2–G4 checklist semantics; Publish eligibility inputs | Readiness gates, Validate findings | **Yes** — recommendation inputs; R4 executes Publish |
| **Consistency** | Evidence ↔ snapshot provenance alignment; identity continuity | I-R5-07, I-R5-03, continuity record | **Yes** — read-only evidence use |

---

### R5.3 — Quality Possession Model

| Field | Value |
|-------|-------|
| **Purpose** | Define **L0–L3** as R5 **certification concepts** — what possession means at Validate, distinct from R3 candidate assembly. Clarify that R3 `package_quality_level: 0` is an honest placeholder, **not** R5 certified possession. |
| **Inputs** | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md); R5-CHARTER § Quality Ownership; Q-INV-R5-01–05 |
| **Outputs** | Level definition table (L0–L3 names and minimum possession concepts); `PossessionAssessmentRecord` contract; downgrade policy; max certifiable level derivation (conceptual — **no scoring formulas**); candidate vs certified quality matrix |
| **Dependencies** | R5.2 (Quality category); R3.1 section model |
| **Non-goals** | Scoring formulas; weighted quality indexes; R3 section population rules; Publish level freeze (R4) |
| **Success criteria** | SC-R5.3-01: L0–L3 defined as certification concepts referencing quality mapping; SC-R5.3-02: R3 candidate L0 **≠** R5 certified level explicitly stated; SC-R5.3-03: Downgrade allowed; inflation forbidden; SC-R5.3-04: Only R5 may assign certified `package_quality_level` on Validate pass |

#### Level certification concepts (ownership only)

| Level | Name | R3 role | R5 certifies |
|-------|------|---------|--------------|
| **L0** | Identity only | Assembles min metadata, environment, acquisition-log, safe-unknown listing non-acquired sections | Identity, audit trail, honesty of gaps |
| **L1** | Identity + structure | Populates or gaps: file-manifest, database-metadata, seo-structure, theme-info | Version proof, manifest subset, DB/SEO/theme adequacy or honest safe-unknown |
| **L2** | + extensions | Optional placeholders / safe-unknown at R3 L1 target | extension-inventory, ocmod-inventory adequacy |
| **L3** | Full read-only audit | Not R3 L1 engineering target | Comprehensive manifest, residual safe-unknown only |

#### Candidate vs certified quality (mandatory)

| Stage | `package_quality_level` | Who sets | Meaning |
|-------|-------------------------|----------|---------|
| **R3 candidate** | **0** (default) | **R3** | Honest placeholder — **not** certification |
| **R5 Validate pass** | **0–3** (certified) | **R5** | Possession-assessed honest claim |
| **R4 Publish** | Frozen published claim | **R4** + operator | Must match R5 certified level — no inflation |

**Rule:** R3 candidate quality **0** means "uncertified assembly." R5 certified level **0** means "Validate confirmed L0 possession" — same numeric value, **different semantic stage** (VB-R3-06).

---

### R5.4 — Redaction Review Model

| Field | Value |
|-------|-------|
| **Purpose** | Define R5 **ownership** of redaction review on candidate snapshots — detecting risk of secret exposure, credential leakage, and unsafe publication **without** designing scanners or automated redaction engines. |
| **Inputs** | R5-CHARTER § Redaction; R2.4 PII/secrets at snapshot; R3.6 VB-R3-12; EAR-SNAPSHOT-LIFECYCLE-v1 Validate stage |
| **Outputs** | Redaction review scope contract; finding severity classes (blocker / warning — conceptual); review targets (candidate serialization, section payloads, bulk refs, metadata fields); fail-closed policy statement; explicit R3 "avoid copy" vs R5 "enforce review" boundary |
| **Dependencies** | R5.2 (Redaction category); R5.1 (FAIL on mandatory redaction blockers) |
| **Non-goals** | Secret scanner implementation; heuristic algorithms; automated redaction engine; evidence quarantine policy (R2) |
| **Success criteria** | SC-R5.4-01: Three review purposes chartered: secret detection, credential exposure, unsafe publication; SC-R5.4-02: Redaction blockers fail closed on Validate; SC-R5.4-03: R3 does not perform redaction enforcement — documented; SC-R5.4-04: Scan depth deferred to operator policy — noted as SAFE UNKNOWN |

#### Redaction review purposes (ownership only)

| Purpose | R5 responsibility |
|---------|-------------------|
| **Secret detection** | Identify patterns or known secret carriers in candidate snapshot serializations bound for consumer paths |
| **Credential exposure** | Flag credential-like values, live connection strings, or quarantine path leaks in snapshot sections |
| **Unsafe publication** | Determine candidate carries pre-redaction bulk or PII that must not proceed to R4 Publish recommendation |

---

### R5.5 — Validate Report Contract

| Field | Value |
|-------|-------|
| **Purpose** | Define the **operator-facing Validate Report** — required sections and semantic content. Distinct from R2 evidence validation output and R3 assembly eligibility messages. |
| **Inputs** | R5-CHARTER O-R5-02; EAR-READINESS-GATES-v1; backlog § R5 outputs |
| **Outputs** | `ValidateReport` contract; required section list; per-section content semantics; linkage to ValidationResult and categories; audit trail fields (snapshot_id, acquisition_id, validate_timestamp, operator_ref — conceptual) |
| **Dependencies** | R5.1, R5.2, R5.3, R5.4, R5.6 |
| **Non-goals** | Report serialization format (JSON/Markdown/HTML); UI product; file naming on disk; automated delivery |
| **Success criteria** | SC-R5.5-01: All required sections defined; SC-R5.5-02: Report distinguishes blockers vs warnings; SC-R5.5-03: Certified level and possession summary included; SC-R5.5-04: Publish Eligibility Recommendation referenced — not substituted |

#### Required report sections (contract only)

| Section | Content |
|---------|---------|
| **Summary** | ValidationResult outcome; certified `package_quality_level`; target certify level; precondition status (R2/R3 pass supplied) |
| **Identity** | Identity category findings; snapshot_id, site_id, contract ids |
| **Structure** | Structure category findings; section skeleton vs spec |
| **Possession** | Possession assessment by section; gaps vs target level |
| **Quality** | Certified level rationale; downgrade notes if target lowered |
| **Redaction** | Redaction findings; blocker/warning classification |
| **Readiness** | Gate G2–G4 checklist mapping; Publish Eligibility Recommendation |
| **Consistency** | Evidence ↔ snapshot alignment notes |
| **Blockers** | Aggregated mandatory failures — fail closed list |
| **Warnings** | Non-blocking notes supporting PASS WITH NOTES |
| **Audit** | Validate run metadata; evidence ref correlation; operator HITL placeholder |

---

### R5.6 — Publish Eligibility Contract

| Field | Value |
|-------|-------|
| **Purpose** | Define **Publish Eligibility Recommendation** — R5 advisory output consumed by R4 and operator. R5 **recommends**; R4 **decides** and executes Publish. |
| **Inputs** | R5-CHARTER § Publish Boundary; EAR-READINESS-GATES-v1 G2–G4; VAL-INV-02; N-R5-06 |
| **Outputs** | `PublishEligibilityRecommendation` contract; enum **ELIGIBLE**, **ELIGIBLE WITH NOTES**, **NOT ELIGIBLE**; mapping from ValidationResult; blocking reason list; explicit R5 prohibitions (no Publish execution) |
| **Dependencies** | R5.1 (outcome mapping); R5.5 (report Readiness section) |
| **Non-goals** | Publish execution; consumer path writes; `published_at` assignment; gate automation product |
| **Success criteria** | SC-R5.6-01: Three recommendation states defined; SC-R5.6-02: FAIL ValidationResult → NOT ELIGIBLE (fail closed); SC-R5.6-03: R5→R4 boundary explicit — recommendation ≠ Publish; SC-R5.6-04: Operator HITL mandatory before R4 acts (pilot) |

#### Recommendation semantics (ownership only)

| Recommendation | Meaning | R4 role |
|----------------|---------|---------|
| **ELIGIBLE** | No mandatory blockers; certified level acceptable for Publish consideration | R4 may proceed after operator approval |
| **ELIGIBLE WITH NOTES** | Publish consideration allowed with documented warnings/downgrades | R4 + operator review notes |
| **NOT ELIGIBLE** | Mandatory failure — redaction, possession, contract, or precondition | R4 **must not** Publish until re-Validate |

```text
R5 Validate Layer
  → PublishEligibilityRecommendation (advisory)
        ↓
Operator HITL (mandatory pilot)
        ↓
R4 Publish Layer (execution)
```

---

### R5.7 — Validate Engine

| Field | Value |
|-------|-------|
| **Purpose** | Define **future implementation scope** for the Validate orchestrator — entry gate, category dispatch, artefact emission. **No code** in this charter. |
| **Inputs** | R5.1–R5.6 contracts; R3.5 candidate path; R2.4 boundary; R3.6 invariants |
| **Outputs** | Validate Engine scope document; entry preconditions; processing pipeline (conceptual); output bundle: ValidationResult + ValidateReport + PublishEligibilityRecommendation + PossessionAssessmentRecord + RedactionFindings + certified level; CLI flag spec (e.g. `--validate-snapshot` — **future**); fail-closed behavior |
| **Dependencies** | R5.1–R5.6 complete; R3.5 candidate generator operational |
| **Non-goals** | Implementation code; per-category rule logic; Store validated-state persist; network I/O; Publish side effects |
| **Success criteria** | SC-R5.7-01: Inputs limited to chartered R5 input set; SC-R5.7-02: Outputs match O-R5-01–08; SC-R5.7-03: Entry gate rejects when R3 assembly eligibility fails; SC-R5.7-04: Does not re-implement R2-V-* or R3-V-* as certification |

#### Validate Engine scope (future implementation)

| Phase | Behavior |
|-------|----------|
| **Entry gate** | Require candidate SnapshotPackage; optional R3 assembly result must pass; optional R2 result flagged; reject R1.7 legacy model |
| **Precondition check** | Fail closed if R3 assembly eligibility not supplied or failed — VB-R3-01 entry |
| **Category dispatch** | Run Identity, Structure, Possession, Quality, Redaction, Readiness, Consistency assessors — **future R5-V-* rules** |
| **Aggregation** | Build ValidationResult from category outcomes |
| **Certification** | Assign certified `package_quality_level` via Quality/Possession models |
| **Report emission** | Build ValidateReport + PublishEligibilityRecommendation |
| **Side effects** | **None** on consumer paths, evidence, or Publish metadata |

```text
Inputs                          Validate Engine                 Outputs
────────                        ───────────────                 ───────
Candidate SnapshotPackage  →    entry gate                 →    ValidationResult
Optional EvidencePackage   →    category assessors         →    ValidateReport
Optional R2/R3 results     →    possession + redaction     →    PublishEligibilityRecommendation
Target certify level       →    aggregation                →    Certified package_quality_level
                               (no Publish, no assembly)
```

---

### R5.8 — Validation Boundary Review

| Field | Value |
|-------|-------|
| **Purpose** | Reserve milestone to **verify** R5 engineering and future implementation do not absorb R3 assembly or R4 Publish. Pattern: [R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md](R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md), [R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md). |
| **Inputs** | R5.1–R5.7 contracts; R3.6 VB-R3-01–18; R2.4 VAL-INV-01–14; implemented R3 validator classification |
| **Outputs** | R5.8 boundary review document; R2/R3/R5/R4 ownership matrix update; overlap verdict; invariants VB-R5-01+ (new); recommendations if creep detected |
| **Dependencies** | R5.1–R5.7 design complete; R5.7 scope documented |
| **Non-goals** | Validator code changes unless critical violation; architecture redesign |
| **Success criteria** | SC-R5.8-01: No R3 assembly checks reclassified as R5 certification; SC-R5.8-02: No Publish execution in R5 scope; SC-R5.8-03: No evidence generation in R5 scope; SC-R5.8-04: Quality certification only in R5 |

#### Boundary verification checklist

| Check | Expected owner |
|-------|----------------|
| OpenCart section population | **R3** |
| `package_quality_level: 0` candidate default | **R3** |
| `package_quality_level` L0–L3 certification | **R5** |
| Publish execution | **R4** |
| Evidence Package writes | **R2** |
| R2 structural validation | **R2** |
| R3 assembly eligibility | **R3** |
| Validate report + Publish recommendation emit | **R5** |

---

### R5.9 — R5 Readiness Review

| Field | Value |
|-------|-------|
| **Purpose** | **Final gate** before R5 code implementation authorization. Verify IAC-R5-01–06; document debt; update program state. |
| **Inputs** | All R5.1–R5.8 deliverables; mock-path candidate from `--contract-snapshot`; R5 Implementation Charter success criteria |
| **Outputs** | R5-READINESS-REVIEW-v1; R5-READINESS-DECISION-v1; updated [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) |
| **Dependencies** | R5.8 boundary review pass; R5.1–R5.7 contracts complete |
| **Non-goals** | Live pilot execution; R4 Publish implementation |
| **Success criteria** | SC-R5.9-01: All R5.1–R5.8 artefacts exist; SC-R5.9-02: IAC-R5-01–06 assessed; SC-R5.9-03: R5 code authorization decision recorded; SC-R5.9-04: Debt and SAFE UNKNOWN catalogued |

---

### Work package classification summary

| Package | Classification |
|---------|----------------|
| R5.1 Validation Result Model | **Required** |
| R5.2 Validation Category Model | **Required** |
| R5.3 Quality Possession Model | **Required** |
| R5.4 Redaction Review Model | **Required** |
| R5.5 Validate Report Contract | **Required** |
| R5.6 Publish Eligibility Contract | **Required** |
| R5.7 Validate Engine | **Required** (scope only — code after R5.9) |
| R5.8 Validation Boundary Review | **Required** |
| R5.9 R5 Readiness Review | **Required** |
| Per-category R5-V-* rules | **Future** — after R5.1–R5.6 |
| Validated Store state marker persist | **SAFE UNKNOWN** |
| `--validate-snapshot` CLI | **Future** — R5.7 implementation |
| Contract-path Store read adapter | **R3 debt** — parallel |

---

## Implementation Sequence

```text
R5.1 Validation Result Model
        ↓
R5.2 Validation Category Model
        ↓
R5.3 Quality Possession Model ────┐
R5.4 Redaction Review Model  ───┼── (parallel after R5.2)
        ↓                         │
R5.5 Validate Report Contract ←───┘
        ↓
R5.6 Publish Eligibility Contract
        ↓
R5.7 Validate Engine (scope)
        ↓
R5.8 Validation Boundary Review (parallel with late R5.7)
        ↓
R5.9 R5 Readiness Review
        ↓
Human gate → R5.1 code (Validation Result Model implementation)
```

**Note:** R5.3 and R5.4 may proceed in parallel after R5.2. R5.8 may start when R5.1–R5.7 contracts are draft-complete.

---

## Validation Boundary

**Terminology (mandatory):**

| Term | Program | Meaning |
|------|---------|---------|
| **R2 structural validation** | R2 | Evidence Package shape and honesty |
| **R3 assembly eligibility** | R3 | Candidate SnapshotPackage structural integrity |
| **R5 EAR Validate** | R5 | Snapshot contract certification, quality, redaction, publish readiness |

### R5 may verify (EAR Validate — certification)

| Check class | Category | Notes |
|-------------|----------|-------|
| Snapshot identity certification | Identity | Beyond R3 presence checks |
| Contract adequacy beyond skeleton | Structure | Section content vs spec |
| Level-specific section possession | Possession | Exclusive R5 |
| L0–L3 certification | Quality | Exclusive R5 |
| Candidate redaction review | Redaction | Exclusive R5 |
| Gate G2–G4 semantics | Readiness | Recommendation inputs |
| Evidence ↔ snapshot alignment | Consistency | Read-only evidence |

### R5 must not verify (owned elsewhere)

| Check class | Owner |
|-------------|-------|
| Evidence Package structural shape | **R2** |
| Evidence quarantine layout | **R2.5** |
| Candidate section population | **R3** |
| Candidate L0 default enforcement | **R3** |
| Publish execution | **R4** |
| Consumer delivery | **R4** + consumer programs |

### Overlap prevention (authoritative)

| Boundary | Rule |
|----------|------|
| R2 ↔ R5 | R5 reads evidence for consistency; does not re-implement R2-V-* except ingest sanity |
| R3 ↔ R5 | R3 never certifies; R5 never populates sections |
| R5 ↔ R4 | R5 recommends; R4 publishes |
| R5 ↔ Operator | Operator owns target level declaration, Validate/Publish sign-off |

---

## Engineering Acceptance (post-implementation — not this document)

| ID | Criterion | Source |
|----|-----------|--------|
| IAC-R5-01 | Operator can run Validate helpers on candidate snapshot | Backlog § R5 |
| IAC-R5-02 | Validate report distinguishes PASS / PASS WITH NOTES / FAIL with blockers | R5.1, R5.5 |
| IAC-R5-03 | Certified level honest per quality mapping | R5.3; EAR-OPENCART-QUALITY-MAPPING-v1 |
| IAC-R5-04 | Publish Eligibility Recommendation fail closed on mandatory failures | R5.6; EAR-READINESS-GATES-v1 |
| IAC-R5-05 | R5 does not execute Publish | R5-CHARTER § Publish Boundary |
| IAC-R5-06 | Consumes R3.1 `SnapshotPackage` — not R1.7 legacy | N-R5-02; A-R5-07 |

---

## Success Criteria

R5 **Implementation Charter** is **complete** when:

| ID | Criterion | Verification |
|----|-----------|--------------|
| SC-IC-R5-01 | All work packages R5.1–R5.9 defined with purpose, inputs, outputs, dependencies, non-goals, success criteria | § Work Breakdown |
| SC-IC-R5-02 | ValidationResult PASS / PASS WITH NOTES / FAIL defined; relation to Publish recommendation | § R5.1 |
| SC-IC-R5-03 | Seven validation categories chartered — ownership only | § R5.2 |
| SC-IC-R5-04 | L0–L3 possession concepts; R3 candidate L0 ≠ R5 certified | § R5.3 |
| SC-IC-R5-05 | Redaction review ownership — no scanner design | § R5.4 |
| SC-IC-R5-06 | Validate Report required sections defined | § R5.5 |
| SC-IC-R5-07 | Publish Eligibility ELIGIBLE / ELIGIBLE WITH NOTES / NOT ELIGIBLE; R5 recommends, R4 decides | § R5.6 |
| SC-IC-R5-08 | Validate Engine future scope — inputs/outputs, no code | § R5.7 |
| SC-IC-R5-09 | R5/R3/R4 boundaries preserved | § Validation Boundary; R5.8 reserved |
| SC-IC-R5-10 | R5.9 Readiness Review reserved as final gate | § R5.9 |
| SC-IC-R5-11 | N-R5-01–10 and A-R5-01–10 reflected | § Dependencies; Notes |
| SC-IC-R5-12 | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) and [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) updated | Program navigation |

---

## Stop Conditions

Stop or escalate **before** R5 code implementation if:

| ID | Condition | Action |
|----|-----------|--------|
| ST-IC-R5-01 | Implementation charter includes **Publish execution** as R5 deliverable | **STOP** — reclassify as R4 |
| ST-IC-R5-02 | Charter includes **snapshot assembly** or section writers | **STOP** — reclassify as R3 |
| ST-IC-R5-03 | Charter includes **evidence generation** or quarantine persist | **STOP** — reclassify as R2 |
| ST-IC-R5-04 | Quality certification assigned outside R5 | **STOP** — quality inflation |
| ST-IC-R5-05 | Validate Engine proposed with **runtime code** in this charter phase | **STOP** — charter is planning only |
| ST-IC-R5-06 | R5 absorbs R3 assembly eligibility as certification | **STOP** — VB-R3-01 violation |
| ST-IC-R5-07 | Publish recommendation conflated with Publish execution | **STOP** — VAL-INV-02 |
| ST-IC-R5-08 | SITE-001, PILOT-001, live SFTP required | **STOP** — Execution Authorization |
| ST-IC-R5-09 | Store redesign contradicting R1.9 | **STOP** — architecture amendment |
| ST-IC-R5-10 | Unattended Validate gate replacing operator HITL | **STOP** — backlog non-goal |

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| R5 label confusion — Validate implemented as Publish or assembly | High | Mission; Stop Conditions; R5.8 boundary review |
| R3 assembly pass treated as R5 pass | High | R5.1 preconditions; VB-R3-01; A-R5-02 |
| Quality inflation without possession review | High | R5.3; Q-INV-R5-* |
| R5 duplicates R2/R3 checks causing drift | Medium | R5.8; R2.4 / R3.6 references |
| Publish before redaction review | High | R5.4 fail closed; R5.6 NOT ELIGIBLE |
| Dual snapshot models (R1.7 vs R3.1) | Medium | N-R5-02; entry gate rejects legacy |
| In-memory candidate only — no Store path | Medium | A-R5-04; Validate Engine accepts memory |
| Validate terminology collision | Medium | Terminology § mandatory |
| PASS WITH NOTES misread as auto-Publish approval | Medium | R5.1; operator HITL mandatory |

---

## SAFE UNKNOWN

| Topic | Status | Owner |
|-------|--------|-------|
| Validate report serialization format | R5.5 implementation | R5.1+ code |
| Validated snapshot Store state marker | R5.7 / Store adapter | R5-adjacent |
| Per-category validation rule IDs (R5-V-*) | Post R5.2 | R5 rule milestones |
| Official JSON Schema for Validate artefacts | Not in repo | Architecture |
| ISO 8601 format enforcement on snapshot timestamps | Deferred | R5 or R3.7 |
| Redaction scan depth (heuristic vs full) | Operator policy | R5.4 implementation |
| Human HITL UI / workflow product | Outside runtime | Operator |
| Validated snapshot immutability beyond R1.9 | **SAFE UNKNOWN** | R5 marker only |
| Contract-path Store persist timing | R3 debt | R3-adjacent |
| Bulk expansion prerequisite for live L1+ Validate | HO-ALLOW-10 | R3 debt |
| 1:N acquisition_id → snapshot_id Validate policy | Architecture | Future |
| Whether empty safe-unknown valid at L3 residual-only | R5 certifies emptiness | R5.3 policy |
| `--validate-snapshot` CLI flag name | Implementation | R5.7 code |

---

## Planning notes (carried from R5 Charter)

| Note | Action |
|------|--------|
| N-R5-01 | Title work R5 — EAR Validate Layer — **satisfied** § Charter identity |
| N-R5-02 | Consume R3.1 via `--contract-snapshot` — **satisfied** § Dependencies; R5.7 entry gate |
| N-R5-03 | Distinct ValidationResult, ValidateReport — **satisfied** § R5.1, R5.5 |
| N-R5-04 | R3 assembly pass precondition only — **satisfied** § R5.7 entry gate |
| N-R5-05 | Human HITL mandatory — **satisfied** § R5.1, R5.6 |
| N-R5-06 | Fail closed on Publish recommendation — **satisfied** § R5.6 |
| N-R5-07 | Disambiguate R2/R3/R5 terms — **satisfied** § Validation Boundary |
| N-R5-08 | R5-V-* at implementation — **deferred** § R5.2 non-goals |
| N-R5-09 | Store persist + bulk expansion debt — **tracked** § Dependencies |
| N-R5-10 | Human implementation approval gate — **satisfied** § Charter identity |

---

## Evidence index

| ID | Source |
|----|--------|
| E-R5I-01 | [R5-CHARTER-v1.md](R5-CHARTER-v1.md) |
| E-R5I-02 | [R5-DECISION-v1.md](R5-DECISION-v1.md) |
| E-R5I-03 | [R3-READINESS-DECISION-v1.md](R3-READINESS-DECISION-v1.md) |
| E-R5I-04 | [R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md](R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md) |
| E-R5I-05 | [R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md) |
| E-R5I-06 | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md) |
| E-R5I-07 | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| E-R5I-08 | [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md) |
| E-R5I-09 | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R5 |

---

## Cross-references

| Document | Use |
|----------|-----|
| [R5-IMPLEMENTATION-DECISION-v1.md](R5-IMPLEMENTATION-DECISION-v1.md) | Implementation gate decision |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Program status |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation |
