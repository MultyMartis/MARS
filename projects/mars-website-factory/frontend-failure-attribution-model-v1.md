# MARS Website Factory — Frontend Failure Attribution Model v1

**Status:** **Canonical Foundation Authority** — documented **human-operated** investigation model for Website Factory frontend gate failures.  
**Not:** runtime orchestration, automated root-cause engine, CI gate, linter, or postmortem automation.

**Purpose:** Close the post–Compliance Decision Model logical gap: the system could **detect** violations, **classify** them, **resolve authority**, and **emit compliance verdicts**, but lacked a **canonical route** from a **confirmed defect that escaped a gate** to answers for:

1. Where did the defect originate?
2. Which gate was **obligated** to stop it?
3. At which stage in the chain?
4. Why was it not stopped?
5. Which gate is considered **failed**?

**Scope boundary:** Foundation governance documentation only. Does **not** modify FP-0002 workspace artefacts, Production Standards content, workspace files, or executable code. Does **not** alter Enforcement Pack gate logic, Compliance Decision Model verdict routes, Authority Order ranks, or QA Matrix domain definitions.

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules)

**Peer authorities (detail — do not duplicate here):**

| Document | Role in attribution route |
|----------|---------------------------|
| [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) | Enforcement gates EG-01–EG-05; expected capture points for compiled CSS, inline style, Operator Law, authority conflict |
| [frontend-compliance-decision-model-v1.md](frontend-compliance-decision-model-v1.md) | Forward compliance route RAW VIOLATION → Gate Verdict — **input** to Stage 2 Authority Analysis |
| [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) | Foundation QA chain §6; downstream gates that may inherit upstream misses |
| [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) | Design Calibration §5.7 — first mandatory compiled CSS capture point |
| [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) | REPORT shape; **FAILURE ATTRIBUTION** block |
| [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) | **OPERATOR VISUAL REVIEW GATE**; failure cause **PROCEEDED WITHOUT OPERATOR VISUAL REVIEW** |
| [layout-spec-law-v1.md](layout-spec-law-v1.md) | **Layout Spec Gate**; failure class **VISUAL INTERPRETATION WITHOUT LAYOUT SPEC**; cause **LAYOUT SPEC SKIPPED** |
| [group-decomposition-law-v1.md](group-decomposition-law-v1.md) | **Group Decomposition Gate**; failure class **GROUP AGGREGATION BEFORE DECOMPOSITION** |
| [FP-0002-group-decomposition-lesson-v1.md](FP-0002-group-decomposition-lesson-v1.md) | Instance lesson — JPG test CONTACT BLOCK aggregation |
| [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) | **Clean Shell Gate**; failure class **PRE-LAYOUT-SPEC STARTER RESIDUE** |
| [FP-0002-clean-shell-lesson-v1.md](FP-0002-clean-shell-lesson-v1.md) | Instance lesson — beautiful starter vs empty shell |
| [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md) | **Brand Asset Detection Gate**; failure class **ASSET IDENTITY COLLISION**; cause **ASSET_IDENTITY_COLLISION** |
| [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) | Authority hierarchy; Exception Registry — consulted at Stage 2 |
| [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) | DQ-* domain checks — expected capture for matrix-scoped findings |

**Honesty boundary:** This model is **documentation discipline**. It does **not** claim an in-repo automated attribution engine unless a project explicitly adopts checklists as tooling.

---

## 1. Core principle — FAILURE EVENT

| Term | Definition |
|------|------------|
| **FAILURE EVENT** | A **confirmed violation** — a defect that **passed beyond** the gate that was **expected** to capture it. Not a hypothetical risk; not a RAW VIOLATION alone. A FAILURE EVENT exists only when evidence shows the violation was **present at or before** the expected capture point and the gate **did not stop** downstream progress. |
| **Expected Capture Point** | The **first gate in the Foundation or page QA chain** that **must** inspect the violation class per peer authority. See §3 Stage 3. |
| **Failed Gate** | The gate named at Expected Capture Point when a FAILURE EVENT is confirmed — the gate **obligated** to stop the violation and **did not**. |
| **Attribution Verdict** | The **accountable stage or role** that owns the Failed Gate miss — not blame on individuals unless operator review is the expected capture point. |

**Rule:** Attribution runs **after** a violation is **confirmed** (Compliance Verdict **FAIL** or **WAIVED** with registry gap, or post-hoc audit finding). It does **not** replace the Compliance Decision Model forward route.

**Rule:** When no violation is confirmed, emit **FAILURE EVENT — NO** in the REPORT block and **skip** Stages 3–5.

**Distinction from Compliance Decision Model:**

| Model | Direction | Question |
|-------|-----------|----------|
| **Compliance Decision Model** | Forward (at audit time) | Given this RAW VIOLATION, what is the correct Compliance Verdict and Gate Verdict? |
| **Failure Attribution Model** | Retrospective (after escape) | Given this **confirmed** violation that progressed, which gate failed and why? |

---

## 2. Investigation route (five stages)

Every FAILURE EVENT **must** traverse these stages in order. Skipping a stage causes attribution drift.

```text
1. Detection
        ↓
2. Authority Analysis
        ↓
3. Expected Capture Point
        ↓
4. Failure Cause
        ↓
5. Attribution Verdict
```

### Stage 1 — Detection

**Question:** What was found?

**Inputs:** Same evidence surfaces as Compliance Decision Model Stage 1 — `src/scss/**`, `dist/*.css`, `dist/**/*.html`, Production Standards SSOT, design measurements, REPORT history, gate verdict lines.

**Output:** Confirmed finding record — e.g. `gap: 16px` in compiled CSS on demo selector `.foundation-demo__grid`.

| Field | Content |
|-------|---------|
| **finding id** | Stable id — e.g. `FE-001` (Failure Event) or reuse `RF-*` from compliance route |
| **location** | File, selector, line, or HTML element |
| **observed value** | Literal measured or inspected value |
| **detection source** | Post-hoc audit · downstream QA · FP rollback review · operator report |

**Verdict at this stage:** Fact only — **not** attribution.

---

### Stage 2 — Authority Analysis

**Question:** What authority layers does this finding violate?

Run [frontend-compliance-decision-model-v1.md](frontend-compliance-decision-model-v1.md) Stages 2–4 **or** cite their completed outputs from the originating REPORT.

| Class | Example citation |
|-------|------------------|
| **Operator Law** | OL-01 gap scale |
| **Production Standards (Rank 1)** | Project spacing token |
| **Matrix domain** | DQ-02b compiled CSS vs SSOT |
| **Enforcement gate scope** | EG-01 · EG-02 · EG-03 · EG-04 |
| **Project Standard** | Approved Production Standards clause |
| **Evidence gap** | Build failed; scope incomplete |

**Output:** Authority citation list — e.g. `OL-01` · `DQ-02b` · `Project Standard §spacing`.

---

### Stage 3 — Expected Capture Point

**Question:** Which gate was **obligated** to stop this violation before it progressed further?

Apply the **first applicable** row from the capture-point table (§4). The Expected Capture Point is the **earliest** gate in the Foundation/page chain whose authority **includes** the violation class.

**Foundation chain order (normative):**

```text
Layout Spec Gate (per block — before HTML/CSS)
        ↓
Design Calibration (§5.7 compiled CSS spot-check)
        ↓
Foundation QA §6.1–6.12 (structure, matrix subset, pixel fidelity)
        ↓
Foundation QA §6.13–6.17 (EG-01–EG-05 enforcement rollup)
        ↓
Page QA chain (completeness → matrix → pixel fidelity → enforcement)
```

**Output:** Named gate — e.g. `Design Calibration §5.7` · `Foundation QA §6.14` · `EG-02` · `DQ-02b` · `Operator Review`.

**Rule:** If violation class is **compiled CSS / OL spacing**, Expected Capture Point is **Design Calibration §5.7** unless calibration was **N/A** (scope never reached calibration) — then next gate is **Foundation QA §6.14** or **EG-02**.

**Rule:** If violation class is **authority conflict / Exception Registry**, Expected Capture Point is **Foundation QA §6.16** · **EG-04** unless conflict was already visible at calibration OL check — then **Design Calibration §5.7** also applies.

---

### Stage 4 — Failure Cause

**Question:** Why did the Expected Capture Point gate not stop the violation?

| Failure Cause | When |
|---------------|------|
| **CHECK NOT EXECUTED** | Gate skipped; REPORT shows **UNKNOWN** or gate line absent; calibration or EG-02 not run though scope required it |
| **CHECK EXECUTED INCORRECTLY** | Gate ran but wrong evidence — e.g. source SCSS only, not `dist/*.css`; wrong selectors; stale build |
| **AUTHORITY NOT CONSULTED** | Rank-1 vs rank-2 resolution or OL scale not applied; Authority Order §6–§7 not followed |
| **EXCEPTION NOT VERIFIED** | Rank-1 permit assumed; Exception Registry not checked or incomplete |
| **REPORT DRIFT** | Gate line **PASS** or **WAIVED** contradicted by later evidence; COMPLIANCE DECISION MODEL block missing or misaligned |
| **PROCEEDED WITHOUT OPERATOR VISUAL REVIEW** | Visual stage closed; technical PASS recorded; **OPERATOR VISUAL REVIEW** block absent, **OPERATOR VISUAL ACCEPT — PENDING**, or agent did not require operator to open page per [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) §12 |
| **LAYOUT SPEC SKIPPED** | HTML/CSS for Header, Footer, Hero, block, or page started without filed Layout Spec or without operator **APPROVED** per [layout-spec-law-v1.md](layout-spec-law-v1.md) |
| **GROUP AGGREGATION BEFORE DECOMPOSITION** | Layout Spec or analysis uses abstract aggregates (CONTACT BLOCK, INFO AREA, etc.) without filed Group Decomposition with discrete GROUP-IDs per [group-decomposition-law-v1.md](group-decomposition-law-v1.md) |
| **ASSET_IDENTITY_COLLISION** | Logo or brand mark wired from FIG/design using **first image** or traversal heuristic; multiple brand hashes in file; wrong client mark in production path per [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md) |
| **UNKNOWN** | Insufficient REPORT history, missing evidence, or ambiguous gate execution — cannot assign cause with confidence |

**Output:** Exactly one primary **FAILURE CAUSE** token from the table above. Secondary causes may be listed in NOTES.

---

### Stage 5 — Attribution Verdict

**Question:** Who is considered the source of the gate failure?

Map Expected Capture Point + Failure Cause to accountable stage:

| Attribution Verdict | When |
|---------------------|------|
| **Design Calibration** | Expected Capture Point is Design Calibration §5.7 or calibration rollup |
| **Foundation QA** | Expected Capture Point is Foundation QA §6.* or EG-01–EG-05 at foundation close |
| **Frontend Design QA Matrix** | Expected Capture Point is DQ-* domain check; matrix gate owned the class |
| **Pixel Fidelity Audit** | Expected Capture Point is PF-* numeric band |
| **Operator Review** | Human Lead signed PASS despite open finding; HITL override without registry; **OPERATOR VISUAL REVIEW GATE** missed — see **PROCEEDED WITHOUT OPERATOR VISUAL REVIEW** |
| **Unknown** | Stage 4 cause **UNKNOWN**; or capture point cannot be determined |

**Output:** Single **ATTRIBUTION VERDICT** — names the **failed gate owner**, not the code author.

---

## 3. Canonical attribution table

Apply for **every** FAILURE EVENT:

| Step | Question | Output vocabulary |
|------|----------|-------------------|
| **Detection** | What was found? | Finding record — location + observed value |
| ↓ | | |
| **Authority Analysis** | What was violated? | OL-* · DQ-* · EG-* · Project Standard · Evidence gap |
| ↓ | | |
| **Expected Capture Point** | Which gate must stop this class? | Gate name — see §4 matrix |
| ↓ | | |
| **Failure Cause** | Why did the gate not stop it? | CHECK NOT EXECUTED · CHECK EXECUTED INCORRECTLY · AUTHORITY NOT CONSULTED · EXCEPTION NOT VERIFIED · REPORT DRIFT · PROCEEDED WITHOUT OPERATOR VISUAL REVIEW · **LAYOUT SPEC SKIPPED** · **PRE-LAYOUT-SPEC STARTER RESIDUE** · UNKNOWN |
| ↓ | | |
| **Attribution Verdict** | Who owns the failed gate? | Design Calibration · Foundation QA · Frontend Design QA Matrix · Pixel Fidelity Audit · **Layout Spec Gate** · **Clean Shell Gate** · Operator Review · Unknown |

**REPORT block (when FAILURE EVENT — YES):** [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) — **FAILURE ATTRIBUTION** subsection.

---

## 4. Failure Type → Expected Gate → Failure Cause → Attribution Verdict

Use the **first matching row** for Expected Capture Point. Refine Failure Cause and Attribution from Stage 4–5 evidence.

| Failure Type | Expected Gate | Typical Failure Cause | Attribution Verdict |
|--------------|---------------|----------------------|---------------------|
| OL-01 spacing in compiled CSS (`gap`, `margin`, `padding`) | Design Calibration §5.7 → EG-02 | CHECK NOT EXECUTED · CHECK EXECUTED INCORRECTLY | Design Calibration · Foundation QA |
| OL-01 spacing missed at calibration; caught only post–Foundation QA | Foundation QA §6.14 · EG-02 | CHECK NOT EXECUTED · CHECK EXECUTED INCORRECTLY | Foundation QA |
| Inline `style=""` outside allowlist | Foundation QA §6.15 · EG-03 | CHECK NOT EXECUTED | Foundation QA |
| Rank-1 vs rank-2 conflict; registry not verified | Foundation QA §6.16 · EG-04 | EXCEPTION NOT VERIFIED · AUTHORITY NOT CONSULTED | Foundation QA |
| Authority conflict visible at calibration; registry skipped | Design Calibration §5.7 · EG-04 | EXCEPTION NOT VERIFIED | Design Calibration · Foundation QA |
| ROOT COMPLIANCE **PASS** while sub-gate evidence incomplete | Foundation QA §6.17 · EG-05 | REPORT DRIFT · CHECK NOT EXECUTED | Foundation QA |
| DQ-02b SSOT vs compiled CSS mismatch | DQ-02b · EG-02 | CHECK EXECUTED INCORRECTLY · AUTHORITY NOT CONSULTED | Frontend Design QA Matrix · Foundation QA |
| PF-03 spacing band violation (numeric fidelity) | Pixel Fidelity PF-03 | CHECK NOT EXECUTED · CHECK EXECUTED INCORRECTLY | Pixel Fidelity Audit |
| WF-GRID / WF-LAYOUT discipline breach | Foundation QA §6.6–6.7 | CHECK NOT EXECUTED | Foundation QA |
| Gate **PASS** contradicted by later audit | Per violation class row above | REPORT DRIFT | Per Expected Capture Point owner |
| **Layout Spec Gate** | Composition structure unlike Visual SSOT; HTML without approved Layout Spec | **Layout Spec Gate** | **LAYOUT SPEC SKIPPED** | **Layout Spec Gate** |
| **FAILURE CLASS** | **VISUAL INTERPRETATION WITHOUT LAYOUT SPEC** — see [layout-spec-law-v1.md](layout-spec-law-v1.md) §7 | **Layout Spec Gate** | **LAYOUT SPEC SKIPPED** | **Layout Spec Gate** |
| **FAILURE CLASS** | **PRE-LAYOUT-SPEC STARTER RESIDUE** — starter demo / ui-demo / chrome present before Clean Shell + Layout Spec — see [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) | **Clean Shell Gate** | **PRE-LAYOUT-SPEC STARTER RESIDUE** | **Clean Shell Gate** |
| **Group Decomposition Gate** | Abstract group labels; merged address/phone/schedule; row correct but groups wrong | **Group Decomposition Gate** | **GROUP AGGREGATION BEFORE DECOMPOSITION** | **Group Decomposition Gate** |
| **FAILURE CLASS** | **GROUP AGGREGATION BEFORE DECOMPOSITION** — see [group-decomposition-law-v1.md](group-decomposition-law-v1.md) §2 | **Group Decomposition Gate** | **GROUP AGGREGATION BEFORE DECOMPOSITION** | **Group Decomposition Gate** |
| **Brand Asset Detection Gate** | Wrong client logo/mark wired; multi-brand FIG; first-image heuristic | **Brand Asset Detection Gate** · Mapping L-07 · DQ-08 / PF-07 if escaped | **ASSET_IDENTITY_COLLISION** | **Brand Asset Detection Gate** · Mapping QA |
| **FAILURE CLASS** | **ASSET IDENTITY COLLISION** — see [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md) | **Brand Asset Detection Gate** | **ASSET_IDENTITY_COLLISION** | **Brand Asset Detection Gate** |
| Visual stage progressed without operator visual acceptance | **OPERATOR VISUAL REVIEW GATE** | PROCEEDED WITHOUT OPERATOR VISUAL REVIEW | **Operator Review** |
| Build failed; `dist/*.css` absent; violation unobservable at audit time | EG-02 · ROOT COMPLIANCE | CHECK NOT EXECUTED | Foundation QA |
| Evidence insufficient to name capture point | — | UNKNOWN | Unknown |

---

## 5. Reference cases (normative)

### CASE A — OL-01 spacing; calibration skipped compiled CSS

| Field | Value |
|-------|-------|
| **Detection** | `gap: 16px` in `dist/*.css` — not on OL-01 scale |
| **Authority Analysis** | OL-01 |
| **Expected Capture Point** | Design Calibration §5.7 |
| **Failure Cause** | CHECK NOT EXECUTED — compiled CSS spot-check not performed |
| **Attribution Verdict** | Design Calibration |

---

### CASE B — Authority conflict; Exception Registry not verified

| Field | Value |
|-------|-------|
| **Detection** | Rank-1 SSOT permits `64px`; OL-01 conflict; no registry row |
| **Authority Analysis** | OL-01 · DQ-02b · EG-04 |
| **Expected Capture Point** | Foundation QA §6.16 · EG-04 |
| **Failure Cause** | EXCEPTION NOT VERIFIED |
| **Attribution Verdict** | Foundation QA |

---

### CASE C — Check ran on wrong evidence

| Field | Value |
|-------|-------|
| **Detection** | `gap: 16px` in compiled CSS; calibration REPORT claims PASS |
| **Authority Analysis** | OL-01 · EG-02 |
| **Expected Capture Point** | Design Calibration §5.7 |
| **Failure Cause** | CHECK EXECUTED INCORRECTLY — source SCSS reviewed; `dist/*.css` not inspected |
| **Attribution Verdict** | Design Calibration |

---

### CASE D — FP-0002 header composition without Layout Spec

| Field | Value |
|-------|-------|
| **Detection** | Implemented header radically unlike design composition |
| **Authority Analysis** | Layout Spec Law · composition structure |
| **Expected Capture Point** | **Layout Spec Gate** — before Header HTML (Phase C.1) |
| **Failure Cause** | **LAYOUT SPEC SKIPPED** |
| **Attribution Verdict** | **Layout Spec Gate** |

**Lesson:** [FP-0002-layout-spec-lesson-v1.md](FP-0002-layout-spec-lesson-v1.md)

---

### CASE E — FP-0002 beautiful starter residue before Clean Shell

| Field | Value |
|-------|-------|
| **Detection** | Workspace contained gulp-starter demo, foundation UI, or partial chrome before Layout Spec APPROVED |
| **Authority Analysis** | Canonical Clean Shell v1 · Layout Spec Law |
| **Expected Capture Point** | **Clean Shell Gate** — before Layout Spec (Phase B / Phase 0.5) |
| **Failure Cause** | **PRE-LAYOUT-SPEC STARTER RESIDUE** |
| **Attribution Verdict** | **Clean Shell Gate** |

**Lesson:** [FP-0002-clean-shell-lesson-v1.md](FP-0002-clean-shell-lesson-v1.md)

---

### CASE G — FP-0002 wrong brand logo from multi-brand FIG

| Field | Value |
|-------|-------|
| **Detection** | Header build used FIG node `1:880` (hash `de219c6e…`, Skinerica); correct chartered mark `1:6720` (hash `262f79db…`, Шпиговский дом) present in same file |
| **Authority Analysis** | L-07 Assets · C-09 · Brand Asset Detection Layer |
| **Expected Capture Point** | **Brand Asset Detection Gate** — before logo wired to `src/img/` or Header partial |
| **Failure Cause** | **ASSET_IDENTITY_COLLISION** — first discovered image node treated as logo |
| **Attribution Verdict** | **Brand Asset Detection Gate** |

**Failure class:** [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md)

---

### CASE F — Insufficient data

| Field | Value |
|-------|-------|
| **Detection** | Suspected OL violation; no calibration or Foundation QA REPORT archived |
| **Authority Analysis** | OL-01 (suspected) |
| **Expected Capture Point** | Unknown |
| **Failure Cause** | UNKNOWN |
| **Attribution Verdict** | Unknown |

---

## 6. Relationship to peer packs

| Peer | Relationship |
|------|--------------|
| **Compliance Decision Model** | Supplies Authority Analysis inputs; **does not** assign Failed Gate — attribution is **retrospective** only |
| **Enforcement Pack** | EG-01–EG-05 name Expected Capture Points for enforcement classes — **no gate logic change** |
| **Authority Order** | Stage 2 cites ranks and Exception Registry — **no override** |
| **QA Matrix** | DQ-* rows name matrix-scoped capture points — matrix §6 rollup unchanged |
| **Foundation QA** | §6 checklist defines downstream gates; attribution does **not** add new mandatory checks |
| **Design Calibration** | §5.7 is first compiled CSS capture point — calibration PASS criteria unchanged |
| **Layout Spec Law** | **Layout Spec Gate** is first composition capture point — before Header/Footer/block HTML |
| **Canonical Clean Shell** | **Clean Shell Gate** is first workspace baseline capture point — before Layout Spec |
| **Reporting Standard** | Adds **FAILURE ATTRIBUTION** block; Layer A gate vocabulary unchanged |

**Non-goal:** This model does **not** replace Compliance Verdict assignment, severity taxonomy, PF-* bands, or Production PASS rollup logic.

**When to run:** Post-hoc audits (e.g. FP-0002 rollback review), downstream defect discovery, ROOT CAUSE investigations, and any REPORT where **COMPLIANCE VERDICT — FAIL** or escaped **WAIVED** is confirmed after gate closure.

---

## 7. Agent / operator stop rules

| Anti-pattern | Correct action |
|--------------|----------------|
| Attribute before violation confirmed | Complete Compliance Decision Model route or confirm defect with evidence |
| Blame code author instead of Failed Gate | Attribution Verdict names **gate owner** (stage), not implementer |
| Skip Expected Capture Point lookup | Apply §4 table; cite gate authority |
| Emit attribution when FAILURE EVENT — NO | REPORT block: **FAILURE EVENT — NO** only |
| Use attribution to waive Compliance **FAIL** | Attribution is investigative — does **not** reverse verdicts |
| Duplicate Compliance Decision Model Stages 3–6 as attribution | Cite compliance outputs at Stage 2; attribution Stages 3–5 are **gate failure** only |

---

## 8. Changelog

| Date | Change |
|------|--------|
| 2026-06-14 | v1 — Failure Attribution Model Pack: FAILURE EVENT semantics; five-stage investigation route; failure cause taxonomy; canonical attribution table; CASE A–D; closes post–Compliance Decision Model investigation gap. |
| 2026-06-14 | v1.1 — Operator Visual Approval Law: failure cause **PROCEEDED WITHOUT OPERATOR VISUAL REVIEW**; Expected Capture Point **OPERATOR VISUAL REVIEW GATE**. |
| 2026-06-14 | v1.2 — Layout Spec Law: failure class **VISUAL INTERPRETATION WITHOUT LAYOUT SPEC**; cause **LAYOUT SPEC SKIPPED**; CASE D (FP-0002 header). |
| 2026-06-14 | v1.3 — Canonical Clean Shell v1: failure class **PRE-LAYOUT-SPEC STARTER RESIDUE**; CASE E (FP-0002 clean shell lesson). |
| 2026-06-15 | v1.4 — Group Decomposition Law: failure class **GROUP AGGREGATION BEFORE DECOMPOSITION**; cause token; §4 matrix rows. |
| 2026-06-17 | v1.5 — Asset Identity Collision: failure class **ASSET IDENTITY COLLISION**; cause **ASSET_IDENTITY_COLLISION**; CASE G (FP-0002 logo forensic). |
