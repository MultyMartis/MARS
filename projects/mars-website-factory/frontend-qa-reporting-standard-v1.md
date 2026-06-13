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
| [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) | RU commercial preset widths + typography |

**Integration audit:** [reports/frontend-qa-integration-pack-v2.md](reports/frontend-qa-integration-pack-v2.md).

---

## 1. Vocabulary layers (do not mix)

Frontend QA uses **four vocabulary layers**. Using the wrong layer in a gate line causes reporting drift.

| Layer | Purpose | Allowed values | Example line prefix |
|-------|---------|----------------|---------------------|
| **A — Gate verdict** | Rollup for a named QA gate | **PASS** · **PASS WITH NOTES** · **FAIL** · **UNKNOWN** | `DESIGN COMPLETENESS AUDIT — …` |
| **B — Sub-check verdict** | Single check inside a gate | **PASS** · **FAIL** · **UNKNOWN** · **N/A** | `PF-03 SPACING — …` |
| **C — Entity / comparison status** | Registry row disposition (completeness only) | **MATCH** · **PARTIAL** · **MISSING** · **EXTRA** · **MISPLACED** | `COMPARISON — MATCH: (n) · …` |
| **D — Signal / escalation** | Evidence gap or HITL — **not** a gate PASS | **SAFE UNKNOWN** · **NEED HUMAN APPROVAL** · **STRUCTURE CHANGE** · **SECURITY RISK** | `SAFE UNKNOWN — PF-06 widths not tested` |

**Rule:** Only **Layer A** values may appear in **Production Verdict** inputs (§6).  
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
FRONTEND DESIGN QA MATRIX (foundation subset) — PASS | PASS WITH NOTES | FAIL | UNKNOWN
PIXEL FIDELITY AUDIT — PASS | PASS WITH NOTES | FAIL | UNKNOWN | N/A
```

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
```

Finding line format (completeness): per [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) §10.2.

### 5.3 Compact operational pass (non-authoritative for Production PASS)

[operational-qa-entry-v1.md](operational-qa-entry-v1.md) compact pass **does not** replace §5.2. When used, normalize legacy line to:

```text
OPERATIONAL COMPACT QA — PASS | PASS WITH NOTES | FAIL | UNKNOWN
```

Map legacy `partial` → **PASS WITH NOTES**; legacy `SAFE UNKNOWN` on line → **UNKNOWN**.

---

## 6. Production Verdict (mandatory final block)

Every Frontend QA REPORT that claims closure of a **foundation gate** or **page/slice Production PASS** **must** end the gate section with:

```text
--- PRODUCTION VERDICT ---
DESIGN COMPLETENESS — PASS | PASS WITH NOTES | FAIL | UNKNOWN | N/A
FRONTEND DESIGN QA MATRIX — PASS | PASS WITH NOTES | FAIL | UNKNOWN | N/A
PIXEL FIDELITY — PASS | PASS WITH NOTES | FAIL | UNKNOWN | N/A
FINAL VERDICT — PRODUCTION PASS | PRODUCTION PASS WITH NOTES | PRODUCTION BLOCKED | PRODUCTION UNKNOWN
--- END PRODUCTION VERDICT ---
```

### 6.1 FINAL VERDICT rules

| FINAL VERDICT | When |
|---------------|------|
| **PRODUCTION PASS** | All **required** gates for scope are **PASS**; build green; peer gates (mapping, calibration for foundation) satisfied |
| **PRODUCTION PASS WITH NOTES** | No gate **FAIL**; at least one required gate **PASS WITH NOTES**; no open Critical; Lead ack for waivers recorded |
| **PRODUCTION BLOCKED** | Any required gate **FAIL** |
| **PRODUCTION UNKNOWN** | Any required gate **UNKNOWN**; or scope/build evidence incomplete |

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
- Using **PASS** on matrix to imply completeness or pixel fidelity PASS.

### 6.2 Example (canonical)

```text
--- PRODUCTION VERDICT ---
DESIGN COMPLETENESS — PASS
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
| Matrix PASS without completeness (page scope) | Run completeness first or **PRODUCTION BLOCKED** |
| Sub-check PASS while parent gate FAIL | Parent gate **FAIL** wins |
| Inventing fifth gate verdict | Use **PASS WITH NOTES** only |

---

## 9. Non-claims

- This document does **not** ship a REPORT parser, linter, or storage layer.
- It does **not** automate Production PASS or HITL waiver.
- It does **not** replace checklist content in peer governance docs — only **shape** and **vocabulary** of REPORT output.

---

## 10. Revision history

| Date | Change |
|------|--------|
| 2026-06-13 | **v1** — Frontend QA Reporting Standard; canonical gate verdicts; migration table; mandatory Production Verdict block; Integration Pack v2 companion audit. |
