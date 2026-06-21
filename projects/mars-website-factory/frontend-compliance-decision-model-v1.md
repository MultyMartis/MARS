# MARS Website Factory — Frontend Compliance Decision Model v1

**Status:** **Canonical Foundation Authority** — documented **human-operated** decision engine for Website Factory frontend compliance verdicts.  
**Not:** runtime orchestration, automated decision engine, CI gate, linter, or parser.

**Purpose:** Close the post–Enforcement Pack logical gap: the system could **detect** violations and run **separate** checks (Compiled CSS, Inline Styles, Operator Laws, Authority Order, Exception Registry), but lacked a **single canonical route** from raw finding to gate verdict. Different auditors and agents could interpret the same case differently.

**Scope boundary:** Foundation governance documentation only. Does **not** modify FP-0002 workspace artefacts, Production Standards content, workspace files, or executable code.

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules)

**Peer authorities (detail — do not duplicate here):**

| Document | Role in decision route |
|----------|------------------------|
| [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) | Authority hierarchy ranks 1–6; Exception Registry §6; Authority Conflict Protocol §7 |
| [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) | Enforcement gates EG-01–EG-05; compliance audit methods |
| [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) | Foundation QA gate rollup |
| [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) | Domain-level checks DQ-01–DQ-12; matrix verdict §6 |
| [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) | REPORT shape; Layer A gate vocabulary; **COMPLIANCE DECISION MODEL** block |

**Honesty boundary:** This model is **documentation discipline**. It does **not** claim an in-repo automated decision engine unless a project explicitly adopts checklists as tooling.

---

## 1. Core principle — RAW VIOLATION ≠ FAIL

| Term | Definition |
|------|------------|
| **RAW VIOLATION** (synonym: **RAW FINDING**) | An **observed fact** — a measured or inspected value, pattern, or disposition that **may** conflict with an authority layer. A detection output only. **Not** a verdict. |
| **FAIL** | A **Compliance Verdict** or **Gate Verdict** emitted **only after** the full decision route (§2) completes. |

**Rule:** Emitting **FAIL** at detection time is **forbidden**. Operators and agents **must** record RAW FINDINGS first, then run Classification → Authority Resolution → Exception Resolution before assigning **FAIL**, **WAIVED**, **PASS**, **PASS WITH NOTES**, or **UNKNOWN**.

**Examples of RAW VIOLATION (not yet FAIL):**

- Compiled CSS contains `gap: 64px` — not on OL-01 scale.
- Inline `style="margin: 12px"` — not on allowlist.
- SSOT spacing token `64px` differs from OL-01 nearest scale value `70px`.

Each RAW VIOLATION **must** be classified before verdict assignment.

---

## 2. Decision route (six stages)

Every compliance finding **must** traverse these stages in order. Skipping a stage causes reporting drift.

```text
1. Detection
        ↓
2. Classification
        ↓
3. Authority Resolution
        ↓
4. Exception Resolution
        ↓
5. Compliance Verdict
        ↓
6. Gate Verdict
```

### Stage 1 — Detection

**Question:** What was observed in evidence?

**Inputs:** `src/scss/**`, `dist/*.css`, `dist/**/*.html`, Production Standards SSOT, design source measurements, allowlist hits.

**Output:** One or more **RAW VIOLATION** records — each with:

| Field | Content |
|-------|---------|
| **finding id** | Stable id — e.g. `RF-001` |
| **location** | File, selector, line, or HTML element |
| **observed value** | Literal measured or inspected value |
| **check source** | EG-01 · EG-02 · EG-03 · DQ-* · PF-* · discipline line |

**Verdict at this stage:** **none** — detection emits facts only.

---

### Stage 2 — Classification

**Question:** Which authority layers does this RAW VIOLATION touch?

For each RAW VIOLATION, classify against:

| Class | Meaning |
|-------|---------|
| **Rank 1 conflict** | Observed value **conflicts with** or **is absent from** **Project Production Standards** |
| **Rank 2 conflict** | Observed value **violates** **Approved Operator Law (OL-01–OL-07)** |
| **Rank 3+ conflict** | Violates Factory governance, layout discipline, matrix domain — **without** rank-1/2 conflict |
| **Allowlist disposition** | Inline style hit — **ALLOWED** · **FORBIDDEN** · **WAIVED** candidate |
| **Evidence gap** | Scope incomplete; build failed; source not inspectable |

**Output:** Classified RAW VIOLATION with `rank_1_status`, `rank_2_status`, `severity` (Critical / Major / Minor / Observation per matrix §5 where applicable).

---

### Stage 3 — Authority Resolution

**Question:** Given rank-1 vs rank-2 posture, does rank-1 **resolve** the conflict?

Apply [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) §2 and §7:

| Situation | AUTHORITY RESOLUTION |
|-----------|----------------------|
| No rank-1/rank-2 conflict; value lawful at both layers | **PASS** |
| Rank-1 value **matches** or **explicitly permits** observed value; rank-2 conflict remains | **FAIL** at authority layer — rank-1 **permits** but does **not** auto-waive OL without Exception Registry (see Stage 4) |
| Rank-1 **silent** (no token, no explicit permit) on observed value; rank-2 conflict | **FAIL** — map to OL scale or escalate HITL |
| Rank-1 **conflicts with** observed value (violates SSOT) | **FAIL** — rank-1 violation; Exception Registry does **not** repair SSOT breach |
| Conflict scope not reviewed | **UNKNOWN** |

**Critical rule (CASE A):** When observed value **violates both Rank 1 and Rank 2**, Authority Resolution is **FAIL** — Exception Registry **cannot** waive a rank-1 breach.

**Critical rule (CASE D):** When observed value **violates Rank 2 only** and Rank 1 is **silent**, Authority Resolution is **FAIL** — silence is **not** permission.

**Output:** Per-finding or rollup **AUTHORITY RESOLUTION — PASS | FAIL | WAIVED | UNKNOWN**.

Note: **WAIVED** at Authority Resolution appears **only** when rank-1 explicitly permits a rank-2 deviation **and** Stage 4 confirms complete Exception Registry (CASE C). Until Stage 4 completes, hold **FAIL** (pending exception), not **WAIVED**.

---

### Stage 4 — Exception Resolution

**Question:** For rank-1-permitted rank-2 deviations, is the Exception Registry **complete**?

Apply [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) §6 and [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) §4.

**Mandatory fields — missing any → EXCEPTION RESOLUTION FAIL (not WAIVED):**

| Field | Requirement |
|-------|-------------|
| **decision id** | Stable id |
| **owner** | Named Project Lead or Frontend Lead |
| **justification** | Why rank-1 value is required |
| **authority citation** | `Rank 1: …` overriding `Rank 2: OL-0N` |

| Situation | EXCEPTION RESOLUTION |
|-----------|---------------------|
| No rank-1/rank-2 deviation requiring registry | **PASS** (nothing to register) |
| Rank-1 permits rank-2 deviation; registry **absent or incomplete** | **FAIL** (CASE B) |
| Rank-1 permits rank-2 deviation; registry **complete** | **WAIVED** (CASE C) |
| Rank-1 and rank-2 both violated | **FAIL** — registry **not applicable** (CASE A) |
| Registry review not performed | **UNKNOWN** |

**Output:** **EXCEPTION RESOLUTION — PASS | FAIL | WAIVED | UNKNOWN**.

---

### Stage 5 — Compliance Verdict

**Question:** What is the **canonical compliance outcome** for this finding or finding set?

Roll up Stages 3–4 plus severity:

| Compliance Verdict | When |
|--------------------|------|
| **PASS** | No RAW VIOLATIONS; or all classified findings resolved **PASS** at authority and exception stages (CASE F) |
| **PASS WITH NOTES** | No Critical/Major blockers; Minor/Observation only; Lead ack on notes where required |
| **FAIL** | Any **FAIL** at Authority or Exception Resolution; rank-1 breach; rank-2 breach without complete registry; FORBIDDEN inline hit without waiver |
| **WAIVED** | Rank-1-permitted rank-2 deviation with **complete** Exception Registry; no concurrent rank-1 breach |
| **UNKNOWN** | Evidence insufficient to assert PASS or FAIL (CASE E) |

**Output:** **COMPLIANCE VERDICT — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN**.

**Rule:** **FAIL** appears here for the first time in the route — never at Detection.

---

### Stage 6 — Gate Verdict

**Question:** What Layer A gate line does this compliance rollup emit?

Map Compliance Verdict to enforcement gate vocabulary per [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §2:

| Gate | Compliance Verdict → Gate Verdict |
|------|-----------------------------------|
| **EG-01** Operator Law Compliance | Same vocabulary incl. **WAIVED** |
| **EG-02** Compiled CSS Compliance | Same vocabulary incl. **WAIVED** |
| **EG-03** Inline Style Compliance | Same vocabulary incl. **WAIVED** |
| **EG-04** Authority Conflict Status | **PASS** · **FAIL** · **WAIVED** · **UNKNOWN** only |
| **EG-05** ROOT COMPLIANCE | Rollup of EG-01–EG-04 + evidence chain — **PASS** · **FAIL** · **UNKNOWN** |

Gate Verdict feeds **Foundation QA**, **Production Verdict**, and **FINAL VERDICT** per reporting standard §5–§6.

**Output:** Canonical gate lines — e.g. `OPERATOR LAW COMPLIANCE — FAIL`.

---

## 3. Canonical decision table

Apply this table for **every** RAW FINDING through to gate emission:

| Step | Question | Output vocabulary |
|------|----------|-------------------|
| **Raw Finding** | What was observed? | RAW VIOLATION record(s) — **no verdict** |
| ↓ | | |
| **Authority Check** | Rank-1 vs rank-2 resolution | **PASS** · **FAIL** · **WAIVED**† · **UNKNOWN** |
| ↓ | | |
| **Exception Check** | Exception Registry complete? | **PASS** · **FAIL** · **WAIVED** · **UNKNOWN** |
| ↓ | | |
| **Compliance Verdict** | Canonical compliance outcome | **PASS** · **PASS WITH NOTES** · **FAIL** · **WAIVED** · **UNKNOWN** |
| ↓ | | |
| **Gate Verdict** | Layer A gate line | Per gate — see §2 Stage 6 |

† **WAIVED** at Authority Check only when Exception Check will confirm **WAIVED** — otherwise **FAIL** pending registry.

**REPORT block (mandatory when enforcement gates run):** [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) — **COMPLIANCE DECISION MODEL** subsection.

---

## 4. Reference cases (normative)

### CASE A — Violates Rank 1 and Rank 2

| Field | Value |
|-------|-------|
| **Detection** | Compiled CSS `gap: 64px`; SSOT requires `gap: 70px`; OL-01 scale excludes `64px` |
| **Classification** | Rank 1 conflict (≠ SSOT) **and** Rank 2 conflict (off OL-01 scale) |
| **Authority Resolution** | **FAIL** |
| **Exception Resolution** | **FAIL** — registry does not repair rank-1 breach |
| **Compliance Verdict** | **FAIL** |
| **Gate Verdict** | **OPERATOR LAW COMPLIANCE — FAIL** · **COMPILED CSS COMPLIANCE — FAIL** · **AUTHORITY CONFLICT STATUS — FAIL** |

---

### CASE B — Rank 2 violation; Rank 1 permits; no Exception Registry

| Field | Value |
|-------|-------|
| **Detection** | SSOT spacing token `64px` in compiled output; OL-01 nearest is `70px` |
| **Classification** | Rank 1 **permits** `64px` explicitly; Rank 2 conflict |
| **Authority Resolution** | **FAIL** — rank-1 permit does not auto-waive OL |
| **Exception Resolution** | **FAIL** — registry **absent** |
| **Compliance Verdict** | **FAIL** |
| **Gate Verdict** | **OPERATOR LAW COMPLIANCE — FAIL** · **AUTHORITY CONFLICT STATUS — FAIL** |

---

### CASE C — Rank 2 violation; Rank 1 permits; complete Exception Registry

| Field | Value |
|-------|-------|
| **Detection** | Same as CASE B — SSOT `64px` vs OL-01 |
| **Classification** | Rank 1 permits; Rank 2 conflict |
| **Authority Resolution** | **FAIL** → pending exception |
| **Exception Resolution** | **WAIVED** — all §6 mandatory fields present |
| **Compliance Verdict** | **WAIVED** |
| **Gate Verdict** | **OPERATOR LAW COMPLIANCE — WAIVED** · **COMPILED CSS COMPLIANCE — WAIVED** · **AUTHORITY CONFLICT STATUS — WAIVED** |

---

### CASE D — Rank 2 violation only; Rank 1 silent

| Field | Value |
|-------|-------|
| **Detection** | Compiled CSS `padding: 17px` — not on OL-01 scale; SSOT has no `17px` token |
| **Classification** | Rank 2 conflict; Rank 1 **silent** |
| **Authority Resolution** | **FAIL** — silence ≠ permission |
| **Exception Resolution** | **FAIL** — no rank-1 override to register |
| **Compliance Verdict** | **FAIL** |
| **Gate Verdict** | **OPERATOR LAW COMPLIANCE — FAIL** · **COMPILED CSS COMPLIANCE — FAIL** |

---

### CASE E — Check impossible; insufficient data

| Field | Value |
|-------|-------|
| **Detection** | Build failed; `dist/*.css` not produced |
| **Classification** | Evidence gap |
| **Authority Resolution** | **UNKNOWN** |
| **Exception Resolution** | **UNKNOWN** |
| **Compliance Verdict** | **UNKNOWN** |
| **Gate Verdict** | **COMPILED CSS COMPLIANCE — UNKNOWN** · **ROOT COMPLIANCE — UNKNOWN** |

---

### CASE F — No violations

| Field | Value |
|-------|-------|
| **Detection** | All inspected values on OL scale; SSOT match; no FORBIDDEN inline hits |
| **Classification** | No conflicts |
| **Authority Resolution** | **PASS** |
| **Exception Resolution** | **PASS** (nothing to register) |
| **Compliance Verdict** | **PASS** |
| **Gate Verdict** | **OPERATOR LAW COMPLIANCE — PASS** · **ROOT COMPLIANCE — PASS** (when peer gates PASS) |

---

## 5. Relationship to peer packs

| Peer | Relationship |
|------|--------------|
| **Authority Order** | Stages 3–4 implement §6 Exception Registry and §7 Authority Conflict Protocol — **no override** |
| **Enforcement Pack** | EG-01–EG-05 gates consume Stage 6 output — **no gate logic change** |
| **QA Matrix** | DQ-02a / DQ-02b domain verdicts feed Detection and Classification — matrix §6 rollup unchanged |
| **Reporting Standard** | Layer A vocabulary unchanged; adds **COMPLIANCE DECISION MODEL** REPORT block |
| **Failure Attribution Model** | Retrospective gate-failure route after confirmed escape — **does not** alter Stages 1–6 forward logic |
| **Foundation QA** | §6.13–6.17 gate lines are Stage 6 outputs for foundation scope |

**Non-goal:** This model does **not** replace severity taxonomy, PF-* numeric bands, or Design Completeness Layer C entity status.

---

## 6. Agent / operator stop rules

| Anti-pattern | Correct action |
|--------------|----------------|
| Emit **FAIL** at Detection | Record **RAW VIOLATION**; complete route |
| Treat rank-1 permit as **WAIVED** without registry | **FAIL** until Exception Registry complete |
| Treat rank-1 silence as permission | **FAIL** — map to OL or escalate HITL |
| Skip **COMPLIANCE DECISION MODEL** block in REPORT | Add block per reporting standard |
| Use **WAIVED** on non-enforcement gates | **WAIVED** enforcement gates only — use **PASS WITH NOTES** elsewhere |

---

## 7. Changelog

| Date | Change |
|------|--------|
| 2026-06-14 | v1 — Compliance Decision Model Pack: six-stage decision route; RAW VIOLATION semantics; CASE A–F; canonical decision table; closes post–Enforcement Pack verdict gap. |
