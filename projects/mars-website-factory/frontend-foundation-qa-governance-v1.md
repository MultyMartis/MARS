# MARS Website Factory — Frontend Foundation QA Governance v1

**Status:** **documented** — canonical **human-operated** governance layer for **Foundation QA** in Website Factory greenfield frontend.  
**Not:** runtime orchestration, CI gate, automated checker, or replacement for peer stage docs.

**Purpose:** Collect **Foundation QA** in one place. Behavior was previously distributed across Shell First Phase 5, Visual Foundation, Design Calibration, Precision Governance, and Frontend Design QA Matrix foundation subset. This document is the **governance router** — detail remains in peer authorities cited below.

**Authority order (canonical):** [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md)

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules)

**Related (peer detail — do not duplicate here):**

| Document | Role in Foundation QA |
|----------|------------------------|
| [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | Mandatory order Phases 0–5; blocks Home until Foundation QA PASS |
| [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) | Demo page composition checklist (IN-03 / 5.1) |
| [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) | Token implementation vs Production Standards (IN / 5.2) |
| [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) | Discipline lines: typography precision, WF-GRID, WF-LAYOUT, RU typography |
| [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) | Matrix foundation subset DQ-01–DQ-09, DQ-12 |
| [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) | Numeric variance peer detail on foundation URL |
| [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) | Mandatory REPORT shape + gate vocabulary §5.1 |
| [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) | Container / page grid law |
| [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) | Inner-zone layout law |

**Honesty boundary:** Foundation QA is **human-operated documentation discipline**. It does **not** claim an in-repo QA engine unless a project explicitly adopts checklists as tooling.

---

## 1. What Foundation QA is

**Foundation QA** is the formal gate that closes the **Frontend Foundation** sub-stage — after Shell, Visual Foundation, and Design Calibration — and **before Home Production** (PG-001) or other commercial page work.

It answers:

> **Is the project's foundation URL + shell lawful, complete, and faithful to approved Production Standards — so page-level production can proceed without token renegotiation?**

Foundation QA is **not**:

| Misread | Correction |
|---------|------------|
| Design Calibration | Calibration verifies tokens; Foundation QA **rolls up** calibration + discipline + matrix subset + REPORT |
| Full page Production PASS | Page path adds Design Completeness + full matrix + PF rollup — see §8 |
| Compact operational QA pass | [operational-qa-entry-v1.md](operational-qa-entry-v1.md) compact pass is post-build smoke — **not** Foundation QA authority |
| Mapping QA | Pre-Approval mapping gate — upstream of Shell |

---

## 2. Stage position (canonical chain segment)

```text
Production Standards Draft
        ↓
DESIGN → FRONTEND MAPPING QA
        ↓
Production Standards Approval
        ↓
Shell → Visual Foundation → Design Calibration
        ↓
Foundation QA                    ← THIS GATE
        ↓
Home Production
        ↓
Design Completeness Audit
        ↓
Frontend Design QA Matrix (full)
        ↓
Pixel Fidelity Audit
        ↓
Production PASS
```

**Upstream authority:** [production-standards-governance-v1.md](production-standards-governance-v1.md) · [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md)  
**Downstream page QA authority:** [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) · [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) §7

---

## 3. Inputs (entry criteria)

Foundation QA **starts** only when **all** inputs are true:

| ID | Input | Source | Blocks QA if missing |
|----|-------|--------|----------------------|
| IN-F01 | **Production Standards Approval** recorded | Project SSOT | **Yes** |
| IN-F02 | **Shell PASS** — header / main / footer in build | Shell stage | **Yes** |
| IN-F03 | **Visual Foundation Contract** complete on foundation demo URL | [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) §3 | **Yes** |
| IN-F04 | **Design Calibration PASS** (or approved PASS WITH NOTES) | [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) §6–7 | **Yes** |
| IN-F05 | **`npm run build` succeeds** | Build log or explicit UNKNOWN blocker | **Yes** |
| IN-F06 | **No Home page sections** implemented yet | Shell-first Phase 5.3 | **Yes** |
| IN-F07 | Foundation demo URL reachable at desktop breakpoint (default ≥1024px) | Operator evidence | **Yes** |
| IN-F08 | Mobile shell pass complete or explicitly scoped in REPORT | Shell-first Phase 4 | Partial — document UNKNOWN if deferred |

**Blocked start:** Return to the failing upstream stage; do not run Foundation QA on incomplete foundation surface.

---

## 4. Outputs (exit artifacts)

| ID | Output | Consumer |
|----|--------|----------|
| OUT-F01 | **`# REPORT — <project> foundation QA`** filed in repo | Lead ack; Home Production gate |
| OUT-F02 | **Foundation QA gate verdict** — PASS · PASS WITH NOTES · FAIL · UNKNOWN | Shell-first Phase 5 closure |
| OUT-F03 | **Discipline line set** (§6) with canonical Layer A vocabulary | [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.1 |
| OUT-F04 | **Lead acknowledgment** on Foundation QA PASS or approved PASS WITH NOTES | Unblocks Phase 6 / Home Production |

**Does not produce:** Production PASS for Home or inner pages — that requires §8 downstream gates.

---

## 5. PASS / FAIL semantics

### 5.1 Foundation QA gate verdict (rollup)

| Verdict | Meaning | Unblocks Home Production? |
|---------|---------|---------------------------|
| **PASS** | All mandatory checks (§6) PASS; no open Critical/Major blockers | **Yes** |
| **PASS WITH NOTES** | No Critical; Major explicitly waived or scheduled with Lead ack; Minor/Observation listed | **Yes** with documented notes |
| **FAIL** | Open Critical; Major without waiver; mandatory peer FAIL; missing §3 Visual Foundation category | **No** |
| **UNKNOWN** | Gate not fully executed; evidence insufficient; build UNKNOWN without HITL scope | **No** |

**Vocabulary:** Use Layer A gate verdicts per [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §2. Legacy `partial` → **PASS WITH NOTES**; `SAFE UNKNOWN` on gate line → **UNKNOWN**.

### 5.2 Foundation QA PASS (gate closure)

Foundation QA **PASS** requires **all** of:

1. IN-F01–IN-F07 satisfied (§3)
2. Mandatory checks (§6) — each **PASS** or parent gate **PASS WITH NOTES** with Lead ack on waivers
3. `# REPORT — <project> foundation QA` filed with **Production Verdict** block appropriate to foundation scope ([frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.1)
4. Lead acknowledgment recorded in REPORT or linked decision doc

### 5.3 Foundation QA FAIL (stop conditions)

Foundation QA **FAIL** when **any** mandatory check is **FAIL** without approved waiver, including but not limited to:

| Class | Examples |
|-------|----------|
| **Composition** | Missing Visual Foundation §3 category; demo page narrower than contract |
| **Calibration** | Design Calibration FAIL; token spot-check Critical drift vs SSOT |
| **Discipline** | WF-GRID or WF-LAYOUT FAIL; typography precision FAIL without documented exception |
| **Matrix subset** | Frontend Design QA Matrix foundation subset **FAIL** on Critical domain |
| **Process** | Home sections already implemented; Production Standards not approved |
| **Evidence** | No build log and no HITL UNKNOWN scope |

**Correction loop:** Fix upstream stage or code → re-run affected checks → new Foundation QA REPORT version.

---

## 6. Mandatory checks

Execute checks on **foundation demo URL + shell** unless noted. Detail authority lives in peer docs — this table is the **consolidated checklist**.

| # | Check | Authority | REPORT line (canonical) |
|---|-------|-----------|-------------------------|
| 6.1 | **Visual Foundation Contract** — all §3 categories present | [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) §5 | `VISUAL FOUNDATION CONTRACT — PASS \| PASS WITH NOTES \| FAIL \| UNKNOWN` |
| 6.2 | **Design Calibration** recorded | [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) | `DESIGN CALIBRATION — PASS \| PASS WITH NOTES \| FAIL \| UNKNOWN` |
| 6.3 | **Token spot-check** on demo vs Production Standards | Calibration §5 | `TOKEN SPOT-CHECK — PASS \| FAIL \| UNKNOWN \| N/A` |
| 6.4 | **Section spacing** tokens visible / mapped | [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) | `SECTION SPACING — PASS \| FAIL \| UNKNOWN \| N/A` |
| 6.5 | **Typography precision** (`line-height = font-size + 4px`) | [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §3.1 | `TYPOGRAPHY PRECISION (line-height = font-size + 4px) — PASS \| FAIL \| UNKNOWN \| N/A` |
| 6.6 | **WF-GRID discipline** — section ≠ container; one page grid contract | [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) | `WF GRID DISCIPLINE — PASS \| FAIL \| UNKNOWN \| N/A` |
| 6.7 | **WF-LAYOUT discipline** — no default `%` splits; LP-* or fr/minmax | [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) | `WF LAYOUT DISCIPLINE — PASS \| FAIL \| UNKNOWN \| N/A` |
| 6.8 | **RU typography / no word-splitting** (RU projects) | [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) · [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) | `RU TYPOGRAPHY / NO WORD-SPLITTING — PASS \| FAIL \| UNKNOWN \| N/A` |
| 6.9 | **Frontend Design QA Matrix — foundation subset** DQ-01–DQ-09, DQ-12 | [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) §7 | `FRONTEND DESIGN QA MATRIX (foundation subset) — PASS \| PASS WITH NOTES \| FAIL \| UNKNOWN` |
| 6.10 | **Pixel Fidelity Audit** on foundation scope (peer detail) | [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) | `PIXEL FIDELITY AUDIT — PASS \| PASS WITH NOTES \| FAIL \| UNKNOWN \| N/A` |
| 6.11 | **Build verification** | Shell-first Phase 3.1 | Build log in REPORT § Build verification |
| 6.12 | **No Home sections** | Shell-first Phase 5.3 | Scope statement in REPORT |

**Optional on foundation slice:** Design Completeness **Foundation slice** per [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) §11.1 — when run, include completeness gate block per reporting standard §5.2.

---

## 7. Agent / operator stop rules

| Condition | Action |
|-----------|--------|
| Operator requests Home before Foundation QA REPORT | **STOP** — execute Phases 0–5 per [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) |
| Design Calibration FAIL | **STOP** — correction loop; no Foundation QA rollup as PASS |
| WF-GRID or WF-LAYOUT FAIL | **STOP** — fix markup/CSS; cite discipline authority |
| Claim Foundation QA PASS without REPORT | **STOP** — file REPORT per §4 |
| Claim Production PASS for Home using only Foundation QA | **STOP** — page path requires §8 |

---

## 8. Relationship to page-level Production PASS

Foundation QA **closes the foundation sub-stage only**. After Home Production (or any page/block slice), operators must run the **page QA chain**:

```text
Page / block production
        ↓
Design Completeness Audit
        ↓
Frontend Design QA Matrix (full DQ-01–DQ-12)
        ↓
Pixel Fidelity Audit
        ↓
Production PASS
```

**Authority:** [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) §11–12 · [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.2–§6

Foundation QA matrix subset (§6.9) is **not** a substitute for full matrix at page closure.

---

## 9. QA surface routing

| Operator need | Start here |
|---------------|------------|
| Foundation QA checklist (this gate) | **This document** §6 |
| REPORT shape + vocabulary | [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.1 |
| Shell-first execution order | [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) |
| Post-build compact smoke (not Foundation QA) | [operational-qa-entry-v1.md](operational-qa-entry-v1.md) |
| Full Production PASS rollup | [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §6 |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-13 | v1 — Foundation Finalization Pack: consolidated Foundation QA governance layer; peer docs unchanged except lifecycle cross-links. |
