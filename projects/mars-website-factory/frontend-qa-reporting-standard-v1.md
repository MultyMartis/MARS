# MARS Website Factory — Frontend QA Reporting Standard v1

**Status:** **documented** — canonical **human-operated** REPORT shape for Frontend QA gates in Website Factory.  
**Not:** executable schema, parser, CI gate, or automated Production PASS engine.

**Version:** v1 (Frontend QA Integration Pack v2).

**Purpose:** Unify **REPORT structure**, **gate verdict vocabulary**, and **Production Verdict rollup** across Design Completeness, Frontend Design QA Matrix, Pixel Fidelity, foundation-stage peers, and downstream operator surfaces — without replacing lane-specific checklists.

**Extends (does not replace):** [reporting-standard-v0.md](reporting-standard-v0.md) — factory-wide REPORT header and lane variants remain valid; this doc is the **Frontend QA specialization**.

**Authority peers (detail lives in source docs):**

| Document | Gate / block owner |
|----------|-------------------|
| [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) | Design Completeness Audit |
| [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) | Frontend Design QA Matrix |
| [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) | Pixel Fidelity Audit |
| [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) | Design Calibration |
| [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | Foundation QA chain |
| [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) | Foundation QA consolidated checklist + PASS/FAIL |
| [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) | Discipline lines (grid, layout, typography precision) |
| [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) | Enforcement gates EG-01–EG-05; ROOT COMPLIANCE |
| [frontend-compliance-decision-model-v1.md](frontend-compliance-decision-model-v1.md) | RAW VIOLATION → Compliance Verdict → Gate Verdict route |
| [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md) | FAILURE EVENT → Expected Gate → Failure Cause → Attribution Verdict |
| [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) | Operator Visual Review gate; TECHNICAL PASS ≠ OPERATOR APPROVAL |
| [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) | RU commercial preset widths + typography |

**Integration audit:** [reports/frontend-qa-integration-pack-v2.md](reports/frontend-qa-integration-pack-v2.md).

---

## 1. Vocabulary layers (do not mix)

Frontend QA uses **five vocabulary layers**. Using the wrong layer in a gate line causes reporting drift.

### 1.1 Artifact lifecycle verdicts (Layer F — production mode)

**Authority:** [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md) §9 · [website-factory-validation-architecture-charter-v1.md](website-factory-validation-architecture-charter-v1.md) §5–§7 · FP-0002 FAIL-001 (false-green build).

Three-level model — **orthogonal** to gate verdict Layer A and **FINAL VERDICT — PRODUCTION PASS**:

| Term | Meaning | Typical evidence | False claim risk |
|------|---------|------------------|------------------|
| **BUILT** | Artifact **created** — compile succeeded | `npm run build` PASS; `dist/` exists | **HIGH** if called «production-ready» without VERIFIED |
| **VERIFIED** | Artifact **checked** per **production mode** rules | PIXEL: PF-* + render/text diff; TEMPLATE: semantic matrix + provenance | Medium — still needs operator sign-off |
| **PRODUCTION PASS** | Project/slice **meets mode requirements** after VERIFIED + mandatory gates + operator acceptance | **FINAL VERDICT** block (§6) | Low when full chain documented |

**Rules:**

- `npm run build` PASS ⇒ **BUILT** only — **never** VERIFIED or PRODUCTION PASS by default.
- **VERIFIED** requires mode-appropriate checklist per [operational-qa-entry-v1.md](operational-qa-entry-v1.md) Production Mode QA Router.
- **PRODUCTION PASS** (FINAL VERDICT) requires **VERIFIED** + Layer A gate rollups + **ROOT COMPLIANCE — PASS** + **OPERATOR VISUAL ACCEPT** where visual stage closes.
- Legacy «PASS» on build log without content check ⇒ map to **BUILT**, not VERIFIED (FP-0002 lesson).

**REPORT lines:**

```text
BUILD LIFECYCLE — BUILT
VERIFICATION LIFECYCLE — VERIFIED | NOT VERIFIED | UNKNOWN
```

**Boundaries:** Layer F applies to **artifact and slice lifecycle**. Layer A gate verdicts (**PASS**, **FAIL**, …) remain unchanged. **FINAL VERDICT — PRODUCTION PASS** is Layer F terminal state aligned with §6.

---

### 1.2 Gate and evidence layers (A–E)

| Layer | Purpose | Allowed values | Example line prefix |
|-------|---------|----------------|---------------------|
| **A — Gate verdict** | Rollup for a named QA gate | **PASS** · **PASS WITH NOTES** · **FAIL** · **UNKNOWN** · **WAIVED**† | `DESIGN COMPLETENESS AUDIT — …` |

† **WAIVED** — allowed **only** on enforcement gates where [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) and [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) §6–§7 define rank-1 override with complete Exception Registry. **WAIVED** is **not** a general substitute for **PASS WITH NOTES**.
| **B — Sub-check verdict** | Single check inside a gate | **PASS** · **FAIL** · **UNKNOWN** · **N/A** | `PF-03 SPACING — …` |
| **C — Entity / comparison status** | Registry row disposition (completeness only) | **MATCH** · **PARTIAL** · **MISSING** · **EXTRA** · **MISPLACED** | `COMPARISON — MATCH: (n) · …` |
| **D — Signal / escalation** | Evidence gap or HITL — **not** a gate PASS | **SAFE UNKNOWN** · **NEED HUMAN APPROVAL** · **STRUCTURE CHANGE** · **SECURITY RISK** | `SAFE UNKNOWN — PF-06 widths not tested` |
| **E — Operator visual acceptance** | Human visual decision — **not** a technical gate PASS | **PENDING** · **ACCEPT** · **REJECT** | `OPERATOR VISUAL ACCEPT — PENDING` |

**Rule:** Only **Layer A** values may appear in **Production Verdict** inputs (§6). **Layer E** is **mandatory** for visual stage closes — see §5.7; **Layer E** does **not** substitute for Layer A and **Layer A PASS does not imply Layer E ACCEPT**.  
**Rule:** **SAFE UNKNOWN** (Layer D) **must not** substitute for **UNKNOWN** (Layer A) when a gate was attempted but incomplete — use **UNKNOWN** on the gate line and cite Layer D in **SAFE UNKNOWN** section.

---

## 2. Canonical gate verdicts (Layer A)

All Frontend QA **gate rollup lines** use **exactly** these four tokens (case and spacing as shown):

| Verdict | Meaning | Production Verdict impact |
|---------|---------|---------------------------|
| **PASS** | Gate criteria met; no open Critical/Major blockers | Contributes **PRODUCTION PASS** when all required gates PASS |
| **PASS WITH NOTES** | No open Critical; Major explicitly waived or scheduled with Lead ack; Minor/Observation listed | Contributes **PRODUCTION PASS WITH NOTES** when all required gates are PASS or PASS WITH NOTES |
| **FAIL** | Open Critical; or Major without waiver; or mandatory peer FAIL | Blocks **PRODUCTION PASS** |
| **UNKNOWN** | Gate not executed, scope ambiguous, or evidence insufficient to assert PASS/FAIL | Blocks **PRODUCTION PASS** until re-run or HITL scope decision |
| **WAIVED** | Rank-1 authority override of Operator Law with **complete** Exception Registry — enforcement gates only | Contributes to **PRODUCTION PASS** or **PRODUCTION PASS WITH NOTES** when peer gates PASS; does **not** waive **ROOT COMPLIANCE** |

**Forbidden as gate verdicts:** `partial`, `conditional`, `pass with reservations`, `Partial PASS`, bare `SAFE UNKNOWN`, lowercase `pass` / `fail`.

---

## 3. Migration table (legacy → canonical)

Use this table when reading or emitting REPORT lines in older docs, examples, or operator notes.

| Legacy / drift term | Canonical gate verdict (Layer A) | Notes |
|---------------------|----------------------------------|-------|
| `partial` | **PASS WITH NOTES** | List exceptions in **NOTES** or gate-specific finding blocks |
| `Partial PASS` | **PASS WITH NOTES** | Requires Lead ack per source gate doc |
| `pass with reservations` | **PASS WITH NOTES** | Reservations = enumerated findings, not a fifth verdict |
| `conditional` (QA lane recommendation) | **PASS WITH NOTES** or **FAIL** | If blockers open → **FAIL**; if waived Major only → **PASS WITH NOTES** |
| `pass` / `fail` (lowercase) | **PASS** / **FAIL** | Normalize case in new REPORTs |
| Build log «15/15 PASS» without content verify | **BUILT** (Layer F) | **Not** VERIFIED — FP-0002 FAIL-001 |
| «Production ready» after `npm run build` only | **BUILT** | Requires **VERIFICATION LIFECYCLE — VERIFIED** per mode router |
| `SAFE UNKNOWN` (on a gate line) | **UNKNOWN** | Move evidence detail to **SAFE UNKNOWN** section (Layer D) |
| `NOT READY` (e.g. layout pattern library) | **UNKNOWN** or **FAIL** | **FAIL** if gate is mandatory for scope; **UNKNOWN** if gate not yet applicable |
| `N/A` | **N/A** (Layer B only) | Not a gate verdict — sub-check skipped |
| Entity `PARTIAL` (completeness comparison) | *(unchanged — Layer C)* | Stays in `COMPARISON` / findings — not a gate verdict |
| `Recommendation: pass` (qa-prompt-rules) | **PASS** | Map at REPORT normalization step |
| `Recommendation: fail` | **FAIL** | |
| `Recommendation: conditional` | **PASS WITH NOTES** | Unless Critical open → **FAIL** |

**Sub-check lines** (PF-*, TOKEN SPOT-CHECK, discipline lines): prefer **PASS** / **FAIL** / **UNKNOWN** / **N/A**. Legacy `partial (list)` on sub-checks → **FAIL** if blocking, else **PASS WITH NOTES** on the **parent gate** only; sub-check may stay **FAIL (list)** with findings.

---

## 4. Mandatory REPORT structure

Every Frontend QA REPORT (foundation or page/slice) **must** use this structure. It **extends** [reporting-standard-v0.md](reporting-standard-v0.md) §3 — factory sections still required where applicable.

### 4.1 Header

```text
# REPORT — <project> <scope> frontend QA
```

Examples:

- `# REPORT — FP-0002 foundation QA`
- `# REPORT — acme-landing home slice frontend QA`

### 4.2 Mandatory sections (order)

| # | Section | Required content |
|---|---------|------------------|
| 1 | **Scope** | Project, page/slice, viewport(s), standards version, audit date |
| 2 | **Build verification** | `npm run build` outcome or **UNKNOWN** with blocker |
| 3 | **Gate verdict blocks** | One block per executed gate (§5) |
| 4 | **Findings summary** | Severity rollup: Critical / Major / Minor / Observation counts |
| 5 | **Production Verdict** | **FINAL VERDICT** block (§6) — **mandatory** |
| 6 | **Created files** | Per reporting-standard-v0 |
| 7 | **Updated files** | Per reporting-standard-v0 |
| 8 | **SAFE UNKNOWN** | Layer D signals — bounded, sourced, resolvable |
| 9 | **Risks** | Open risks |
| 10 | **Git status** | `git status --short` post-edit |
| 11 | **Runtime exclusions** | Paths untouched |
| 12 | **Push status** | `not requested` unless explicitly pushed |

**QA-only runs** (no file edits): sections 6–7 may be `(none)`; sections 8–12 remain mandatory.

---

## 5. Mandatory gate verdict blocks

Emit **only gates executed for this scope**. Use canonical Layer A verdicts.

### 5.1 Foundation path (pre–Home Production)

Required when closing **Foundation QA** per [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) §6 and [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) Phase 5:

```text
DESIGN CALIBRATION — PASS | PASS WITH NOTES | FAIL | UNKNOWN
TOKEN SPOT-CHECK — PASS | FAIL | UNKNOWN | N/A
SECTION SPACING — PASS | FAIL | UNKNOWN | N/A
TYPOGRAPHY PRECISION (line-height = font-size + 4px) — PASS | FAIL | UNKNOWN | N/A
WF GRID DISCIPLINE — PASS | FAIL | UNKNOWN | N/A
WF LAYOUT DISCIPLINE — PASS | FAIL | UNKNOWN | N/A
RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | FAIL | UNKNOWN | N/A
  (grep evidence when executed: word-break: 0 · overflow-wrap: 0 · hyphens: 0 · letter-spacing: 0 in src/scss + dist/*.css)
OPERATOR LAW COMPLIANCE — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN
COMPILED CSS COMPLIANCE — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN
INLINE STYLE COMPLIANCE — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN
AUTHORITY CONFLICT STATUS — PASS | FAIL | WAIVED | UNKNOWN
FRONTEND DESIGN QA MATRIX (foundation subset) — PASS | PASS WITH NOTES | FAIL | UNKNOWN
PIXEL FIDELITY AUDIT — PASS | PASS WITH NOTES | FAIL | UNKNOWN | N/A
```

Then **COMPLIANCE DECISION MODEL** block (§5.5) — **mandatory** when EG-01–EG-04 gates are executed.

Then **ROOT COMPLIANCE** block (§5.4) — **mandatory** before Foundation QA PASS.

Detail blocks: follow [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) §4 and [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) § Audit execution summary.

**Design Completeness** on foundation slice: optional **Foundation slice** scope per [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) §11.1 — when run, include §5.2 block.

### 5.2 Page / slice production path (mandatory chain)

When closing a **page or block slice** before **Production PASS**:

```text
DESIGN COMPLETENESS AUDIT — PASS | PASS WITH NOTES | FAIL | UNKNOWN
SCOPE — page/slice: … · viewport(s): … · standards version: …
DESIGN ENTITY REGISTRY — version/id: … · rows: (n)
FRONTEND ENTITY REGISTRY — extracted: … · rows: (n)
COMPARISON — MATCH: (n) · MISSING: (n) · PARTIAL: (n) · EXTRA: (n) · MISPLACED: (n)
SEVERITY — Critical: (n) · Major: (n) · Minor: (n) · Observation: (n)
```

Then:

```text
FRONTEND DESIGN QA MATRIX — PASS | PASS WITH NOTES | FAIL | UNKNOWN
DOMAIN SUMMARY — DQ-01: PASS | FAIL | N/A · … · DQ-12: PASS | FAIL | N/A
SEVERITY — Critical: (n) · Major: (n) · Minor: (n) · Observation: (n)
PIXEL FIDELITY AUDIT — PASS | PASS WITH NOTES | FAIL | UNKNOWN | N/A
PF-01 TYPOGRAPHY — PASS | FAIL | UNKNOWN | N/A
PF-02 CONTAINER — PASS | FAIL | UNKNOWN | N/A
PF-03 SPACING — PASS | FAIL | UNKNOWN | N/A
PF-04 LAYOUT — PASS | FAIL | UNKNOWN | N/A
PF-05 COMPONENTS — PASS | FAIL | UNKNOWN | N/A
PF-06 RESPONSIVE — PASS | FAIL | UNKNOWN | N/A
PF-07 ASSETS — PASS | FAIL | UNKNOWN | N/A
WF GRID DISCIPLINE — PASS | FAIL | UNKNOWN | N/A
WF LAYOUT DISCIPLINE — PASS | FAIL | UNKNOWN | N/A
RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | FAIL | UNKNOWN | N/A
  (grep evidence when executed: word-break: 0 · overflow-wrap: 0 · hyphens: 0 · letter-spacing: 0 in src/scss + dist/*.css)
OPERATOR LAW COMPLIANCE — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN
COMPILED CSS COMPLIANCE — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN
INLINE STYLE COMPLIANCE — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN
AUTHORITY CONFLICT STATUS — PASS | FAIL | WAIVED | UNKNOWN
```

Then **COMPLIANCE DECISION MODEL** block (§5.5) — **mandatory** when EG-01–EG-04 gates are executed.

Then **ROOT COMPLIANCE** block (§5.4) — **mandatory** before Production PASS.

Finding line format (completeness): per [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) §10.2.

### 5.3 Compact operational pass (non-authoritative for Production PASS)

[operational-qa-entry-v1.md](operational-qa-entry-v1.md) compact pass **does not** replace §5.2. When used, normalize legacy line to:

```text
OPERATIONAL COMPACT QA — PASS | PASS WITH NOTES | FAIL | UNKNOWN
```

Map legacy `partial` → **PASS WITH NOTES**; legacy `SAFE UNKNOWN` on line → **UNKNOWN**.

### 5.4 ROOT COMPLIANCE (technical review — mandatory)

**Authority:** [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) §6.

Emit **after** **COMPLIANCE DECISION MODEL** (§5.5) and **before** **PRODUCTION VERDICT**. **PASS** on Foundation QA or **FINAL VERDICT — PRODUCTION PASS** is **forbidden** without **ROOT COMPLIANCE — PASS**.

```text
--- ROOT COMPLIANCE (technical review) ---
SOURCE SCSS/HTML REVIEWED — PASS | FAIL | UNKNOWN
COMPILED CSS REVIEWED (dist/*.css) — PASS | FAIL | UNKNOWN
COMPILED HTML REVIEWED (dist/**/*.html) — PASS | FAIL | UNKNOWN
AUTHORITY CONFLICTS DISPOSITIONED — PASS | FAIL | WAIVED | UNKNOWN
EXCEPTION REGISTRY COMPLETE — PASS | FAIL | UNKNOWN
ROOT COMPLIANCE — PASS | FAIL | UNKNOWN
--- END ROOT COMPLIANCE ---
```

| ROOT COMPLIANCE | When |
|-----------------|------|
| **PASS** | All sub-lines **PASS** or **WAIVED** where applicable; EG-01–EG-03 not **FAIL** |
| **FAIL** | Any sub-line **FAIL**; or enforcement gate **FAIL** without waiver |
| **UNKNOWN** | Build/evidence incomplete |

Optional **Exception Registry** subsection (required when any gate is **WAIVED**):

```text
EXCEPTION REGISTRY — (n) rows
| decision id | owner | OL overridden | authority citation |
```

### 5.5 COMPLIANCE DECISION MODEL (mandatory when enforcement gates run)

**Authority:** [frontend-compliance-decision-model-v1.md](frontend-compliance-decision-model-v1.md).

Emit **after** enforcement gate lines (EG-01–EG-04) and **before** **ROOT COMPLIANCE**. Summarizes the canonical decision route from RAW VIOLATION to gate verdict.

```text
--- COMPLIANCE DECISION MODEL ---
RAW FINDINGS — (n)
AUTHORITY RESOLUTION — PASS | FAIL | WAIVED | UNKNOWN
EXCEPTION RESOLUTION — PASS | FAIL | WAIVED | UNKNOWN
COMPLIANCE VERDICT — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN
--- END COMPLIANCE DECISION MODEL ---
```

| Line | When |
|------|------|
| **RAW FINDINGS — (n)** | Count of RAW VIOLATION records from Detection (§2 Stage 1) — **0** when CASE F |
| **AUTHORITY RESOLUTION** | Rollup of Stage 3 — worst finding wins (**FAIL** > **UNKNOWN** > **WAIVED** > **PASS**) |
| **EXCEPTION RESOLUTION** | Rollup of Stage 4 — **FAIL** if any required registry incomplete |
| **COMPLIANCE VERDICT** | Stage 5 outcome — must align with EG-01–EG-04 gate lines below |

**Rule:** **RAW FINDINGS — (n)** where **n > 0** does **not** imply **FAIL** — verdict follows the full route per decision model CASE A–F.

Optional per-finding detail (recommended when **n > 0**):

```text
RAW FINDING — RF-001 · location: … · observed: … · authority: FAIL · exception: FAIL · compliance: FAIL
```

### 5.6 FAILURE ATTRIBUTION (when confirmed violation escaped a gate)

**Authority:** [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md).

Emit **after** **COMPLIANCE DECISION MODEL** (§5.5) when investigating a **confirmed violation that passed beyond its expected capture point**, or during post-hoc / rollback audits. **Optional** on routine PASS closures — **mandatory** when **COMPLIANCE VERDICT — FAIL** is recorded and the defect progressed past an earlier gate, or when a post-hoc audit confirms a FAILURE EVENT.

```text
--- FAILURE ATTRIBUTION ---
FAILURE EVENT — YES | NO
EXPECTED GATE —
<gate>
FAILURE CAUSE —
<cause>
ATTRIBUTION VERDICT —
<owner>
--- END FAILURE ATTRIBUTION ---
```

| Line | When |
|------|------|
| **FAILURE EVENT — YES \| NO** | **YES** when a confirmed violation passed beyond Expected Capture Point; **NO** otherwise — omit remaining lines when **NO** |
| **EXPECTED GATE —** | First gate obligated to capture the violation class — e.g. `Design Calibration §5.7` · `Foundation QA §6.14` · `EG-02` · `DQ-02b` |
| **FAILURE CAUSE —** | **CHECK NOT EXECUTED** · **CHECK EXECUTED INCORRECTLY** · **AUTHORITY NOT CONSULTED** · **EXCEPTION NOT VERIFIED** · **REPORT DRIFT** · **PROCEEDED WITHOUT OPERATOR VISUAL REVIEW** · **UNKNOWN** |
| **ATTRIBUTION VERDICT —** | **Design Calibration** · **Foundation QA** · **Frontend Design QA Matrix** · **Pixel Fidelity Audit** · **Operator Review** · **Unknown** |

**Rule:** Attribution does **not** replace or reverse **COMPLIANCE VERDICT** or Layer A gate lines — investigative layer only.

Optional per-event detail (recommended when **FAILURE EVENT — YES**):

```text
FAILURE EVENT — FE-001 · detected: gap:16px · authority: OL-01 · expected: Design Calibration §5.7
```

### 5.7 OPERATOR VISUAL REVIEW (mandatory after visual stages)

**Authority:** [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md).

Emit **after** technical gate blocks and **before** **PRODUCTION VERDICT** on every REPORT that closes a **visual stage** (shell, header, footer, Visual Foundation, Design Calibration, Foundation QA, UI Demo, page/block slice, page QA close).

```text
--- OPERATOR VISUAL REVIEW ---
TECHNICAL PASS:
PASS | FAIL | UNKNOWN

OPERATOR VISUAL ACCEPT:
PENDING | ACCEPT | REJECT

OPERATOR ACTION REQUIRED:
YES | NO
--- END OPERATOR VISUAL REVIEW ---
```

| Line | When |
|------|------|
| **TECHNICAL PASS** | Rollup of build + executed technical/audit gates for this visual stage — **PASS** only when no open technical **FAIL** on scope |
| **OPERATOR VISUAL ACCEPT** | **PENDING** until operator opens page and decides; **ACCEPT** authorizes next visual stage; **REJECT** (= **REVISE**) blocks progression |
| **OPERATOR ACTION REQUIRED** | **YES** when **OPERATOR VISUAL ACCEPT — PENDING** or **REJECT**; **NO** only when **OPERATOR VISUAL ACCEPT — ACCEPT** or dated WAIVE recorded |

**Forbidden combinations:**

| State | Forbidden |
|-------|-----------|
| **OPERATOR VISUAL ACCEPT — PENDING** | **OPERATOR ACTION REQUIRED — NO** |
| **OPERATOR VISUAL ACCEPT — ACCEPT** | Next visual stage without operator having opened page |

**Rule:** **TECHNICAL PASS — PASS** does **not** set **OPERATOR VISUAL ACCEPT — ACCEPT**. Design Calibration PASS, Foundation QA PASS, Header PASS, Footer PASS, UI Demo PASS, and Page QA PASS are **technical only** per Operator Visual Approval Law §4.

**Agent closeout (FP-0002):** When **OPERATOR VISUAL ACCEPT — PENDING**, agent **must** instruct operator to open page, verify result, and supply decision — e.g. «Откройте страницу. Проверьте результат. Требуется решение оператора.»

---

## 6. Production Verdict (mandatory final block)

Every Frontend QA REPORT that claims closure of a **foundation gate** or **page/slice Production PASS** **must** end the gate section with:

```text
--- PRODUCTION VERDICT ---
DESIGN COMPLETENESS — PASS | PASS WITH NOTES | FAIL | UNKNOWN | N/A
OPERATOR LAW COMPLIANCE — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN | N/A
COMPILED CSS COMPLIANCE — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN | N/A
INLINE STYLE COMPLIANCE — PASS | PASS WITH NOTES | FAIL | WAIVED | UNKNOWN | N/A
AUTHORITY CONFLICT STATUS — PASS | FAIL | WAIVED | UNKNOWN | N/A
ROOT COMPLIANCE — PASS | FAIL | UNKNOWN
FRONTEND DESIGN QA MATRIX — PASS | PASS WITH NOTES | FAIL | UNKNOWN | N/A
PIXEL FIDELITY — PASS | PASS WITH NOTES | FAIL | UNKNOWN | N/A
FINAL VERDICT — PRODUCTION PASS | PRODUCTION PASS WITH NOTES | PRODUCTION BLOCKED | PRODUCTION UNKNOWN
--- END PRODUCTION VERDICT ---
```

### 6.1 FINAL VERDICT rules

| FINAL VERDICT | When |
|---------------|------|
| **PRODUCTION PASS** | All **required** gates for scope are **PASS** or permitted **WAIVED**; **ROOT COMPLIANCE — PASS**; build green; peer gates satisfied |
| **PRODUCTION PASS WITH NOTES** | No gate **FAIL**; at least one required gate **PASS WITH NOTES** or **WAIVED**; **ROOT COMPLIANCE — PASS**; Lead ack for waivers recorded |
| **PRODUCTION BLOCKED** | Any required gate **FAIL**; or **ROOT COMPLIANCE — FAIL** |
| **PRODUCTION UNKNOWN** | Any required gate **UNKNOWN**; or **ROOT COMPLIANCE — UNKNOWN**; or scope/build evidence incomplete |

**Foundation scope:** `DESIGN COMPLETENESS` may be **N/A** (foundation slice inventory not run). **FINAL VERDICT** still required.

**Page/slice scope:** `DESIGN COMPLETENESS` is **required** — not **N/A** — before matrix final **PASS**.

**Pipeline order (normative):**

```text
Design Completeness Audit
        ↓
Frontend Design QA Matrix
        ↓
Pixel Fidelity Audit
        ↓
PRODUCTION VERDICT (FINAL VERDICT)
```

**Forbidden:**

- **FINAL VERDICT — PRODUCTION PASS** with only matrix line and no completeness line on page/slice scope.
- **FINAL VERDICT — PRODUCTION PASS** when any required gate is **UNKNOWN**.
- **FINAL VERDICT — PRODUCTION PASS** when **ROOT COMPLIANCE** is not **PASS**.
- Using **PASS** on matrix to imply completeness or pixel fidelity PASS.

### 6.2 Example (canonical)

```text
--- PRODUCTION VERDICT ---
DESIGN COMPLETENESS — PASS
OPERATOR LAW COMPLIANCE — PASS
COMPILED CSS COMPLIANCE — PASS
INLINE STYLE COMPLIANCE — PASS
AUTHORITY CONFLICT STATUS — PASS
ROOT COMPLIANCE — PASS
FRONTEND DESIGN QA MATRIX — PASS
PIXEL FIDELITY — PASS WITH NOTES
FINAL VERDICT — PRODUCTION PASS WITH NOTES
--- END PRODUCTION VERDICT ---
```

---

## 7. Relationship to factory QA lanes

| Surface | Role vs this standard |
|---------|----------------------|
| [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) | Lane QA **recommendations** map to Layer A at REPORT normalization; does not override §6 Production Verdict |
| [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) | HITL / waiver / freeze — **PRODUCTION BLOCKED** until waiver recorded |
| [operational-qa-entry-v1.md](operational-qa-entry-v1.md) | Entry router — compact pass is supplementary |
| [reporting-standard-v0.md](reporting-standard-v0.md) §4.2–4.3 | Frontend implementation / QA REPORT variants must cite this doc for Production PASS claims |

---

## 8. Anti-patterns

| Anti-pattern | Correct action |
|--------------|----------------|
| Gate line `partial` | **PASS WITH NOTES** + enumerated notes |
| Gate line `SAFE UNKNOWN` | Gate **UNKNOWN** + Layer D section entry |
| Missing **PRODUCTION VERDICT** block | Add §6 block before closeout |
| **OPERATOR VISUAL ACCEPT — PENDING** with **OPERATOR ACTION REQUIRED — NO** | Set **OPERATOR ACTION REQUIRED — YES** per §5.7 |
| Technical PASS without **OPERATOR VISUAL REVIEW** on visual stage close | Add §5.7 block; **TECHNICAL PASS ≠ OPERATOR APPROVAL** |
| Matrix PASS without completeness (page scope) | Run completeness first or **PRODUCTION BLOCKED** |
| Sub-check PASS while parent gate FAIL | Parent gate **FAIL** wins |
| Inventing fifth gate verdict | Use **PASS WITH NOTES** only |

---

## 9. Non-claims

- This document does **not** ship a REPORT parser, linter, or storage layer.
- It does **not** automate Production PASS or HITL waiver.
- It does **not** replace checklist content in peer governance docs — only **shape** and **vocabulary** of REPORT output.

---

## 9.1 CSS Variable First Law + Universal Style Scale — Visual QA token fields

**Authority:** [css-variable-first-law-v1.md](css-variable-first-law-v1.md) · [universal-style-scale-law-v1.md](universal-style-scale-law-v1.md)

Every Visual QA report for SCSS-bearing stages must include:

```text
Core spacing tokens reused:
Core radius tokens reused:
Selector-specific tokens found:
Selector-specific tokens removed:
Selector-specific tokens remaining:
One-use tokens found:
One-use tokens removed:
One-use tokens remaining:
Alias chains found:
Alias chains removed:
Alias chains remaining:
Logical CSS properties found:
Logical CSS properties removed:
Logical CSS properties remaining:
Direct exact values:
New global tokens:
New shared component tokens:
Token admission result:
Tokens changed
Exceptions changed
Arbitrary values introduced: 0
Arbitrary values remaining: 0
Primary container reused:
Custom container exceptions:
Duplicate container rules found:
Duplicate container rules remaining:
Section rhythm owners:
Boundary spacing workarounds found:
Boundary spacing workarounds removed:
Boundary spacing workarounds remaining:
```

### One SCSS file + unified radius — mandatory report fields

**Authority:** [one-project-scss-file-law-v1.md](one-project-scss-file-law-v1.md) · [no-button-letter-spacing-law-v1.md](no-button-letter-spacing-law-v1.md)

Every frontend report for SCSS-bearing stages must include:

```text
Project SCSS entry:
Project SCSS files before:
Project SCSS files after:
Project partials found:
Project partials removed:
Project partials remaining:
Project @use/@import found:
Project @use/@import removed:
Project @use/@import remaining:
Cascade order:
Duplicate selectors found:
Duplicate selectors removed:
Duplicate selectors remaining:
--radius-main status:
--radius-full status:
Legacy radius tokens found:
Legacy radius tokens removed:
Legacy radius tokens remaining:
Component radius aliases found:
Component radius aliases removed:
Component radius aliases remaining:
--button-letter-spacing found:
--button-letter-spacing removed:
--button-letter-spacing remaining:
Button letter-spacing declarations found:
Button letter-spacing declarations removed:
Button letter-spacing declarations remaining:
```

### Universal button system — mandatory report fields

**Authority:** [universal-button-system-law-v1.md](universal-button-system-law-v1.md)

Every frontend report for SCSS-bearing stages must include:

```text
Buttons found:
Buttons migrated to `.btn`:
Button-like links migrated:
Legacy button systems found:
Legacy button systems removed:
Legacy button systems remaining:
`.btn` base status:
`.btn_dark` status:
`.btn--primary` status:
Block-specific geometry duplicates found:
Block-specific geometry duplicates removed:
Block-specific geometry duplicates remaining:
Button tokens reused:
New button tokens:
Button letter-spacing remaining:
Focus-visible status:
Disabled-state status:
```

Corrections must route through **existing core scale** or **documented exact geometry** — not block-specific token aliases, alias chains, logical shorthand properties, arbitrary px tuning, local container width, first/last-child boundary padding, **new project SCSS partials**, **legacy radius scale tokens**, **button letter-spacing tokens**, or **parallel button systems**.

---

## 10. Revision history

| Date | Change |
|------|--------|
| 2026-06-13 | **v1** — Frontend QA Reporting Standard; canonical gate verdicts; migration table; mandatory Production Verdict block; Integration Pack v2 companion audit. |
| 2026-06-14 | **v1.1** — Enforcement Pack v1: WAIVED gate verdict; OPERATOR LAW / COMPILED CSS / INLINE STYLE / AUTHORITY CONFLICT lines; ROOT COMPLIANCE §5.4; Production Verdict inputs expanded. |
| 2026-06-14 | **v1.2** — Compliance Decision Model Pack: mandatory **COMPLIANCE DECISION MODEL** block §5.5. |
| 2026-06-14 | **v1.3** — Failure Attribution Model Pack: **FAILURE ATTRIBUTION** block §5.6. |
| 2026-06-14 | **v1.4** — Operator Visual Approval Law: mandatory **OPERATOR VISUAL REVIEW** block §5.7; Layer E vocabulary. |
| 2026-06-22 | **v1.5** — CSS Variable First Law §9.1: mandatory token fields on Visual QA; arbitrary px correction prohibited. |
| 2026-06-22 | **v1.6** — Container + section rhythm mandatory report fields §9.1 |
| 2026-06-23 | **v1.7** — Universal Style Scale Law fields §9.1; selector token / alias chain / logical property audit lines |
| 2026-06-23 | **v1.8** — Universal Button System mandatory report fields §9.1 |
