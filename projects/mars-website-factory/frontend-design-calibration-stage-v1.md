# MARS Website Factory — Frontend Design Calibration Stage v1

**Status:** **documented** — mandatory **human-operated** stage between Visual Foundation and Foundation QA.  
**Not:** automated design diff tool, Figma plugin, CI gate, or replacement for Production Standards approval.

**Purpose:** Formalize the review pass where **Project Lead / Frontend Lead** confirms that implemented tokens on the Foundation Demo Page match **Project Production Standards** before Foundation QA closes and Home Production opens.

**Provenance:** FP-0002 Shpigovsky audit (2026-06-13) — token spot-check and visual reconciliation on foundation page were practiced but not named as a Factory stage. Evolution Pack v1 promotes this to system rules.

**Related:**

| Document | Role |
|----------|------|
| [production-standards-governance-v1.md](production-standards-governance-v1.md) | Draft + Approval gate (predecessor stages) |
| [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) | Mandatory demo page composition (predecessor stage output) |
| [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | Overall start gate protocol |
| [visual-reconciliation-layer.md](visual-reconciliation-layer.md) | FINDINGS vocabulary for calibration REPORT |
| [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) | Spacing token verification |
| [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) | RU projects — typography law check |
| [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) | Spacing scale + mandatory line-height pre-flight |

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules).

---

## 1. Stage position

### 1.1 Canonical Factory chain

```text
Production Standards Draft   ← authoring (Phase 0a)
        ↓
Production Standards Approval ← SSOT freeze (Phase 0b)
        ↓
      Shell              ← header / main / footer frame
        ↓
Visual Foundation        ← Foundation Demo Page composition
        ↓
Design Calibration       ← THIS STAGE
        ↓
  Foundation QA          ← formal gate + REPORT — [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md)
        ↓
 Home Production         ← PG-001 and downstream pages
        ↓
Design Completeness → Frontend Design QA Matrix (full) → Pixel Fidelity → Production PASS
```

**Page QA (post–Home):** [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) §11–12 · [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.2–§6.

### 1.2 What this stage is not

| Misread | Correction |
|---------|------------|
| Re-approval of Production Standards | Standards were approved in Phase 0; calibration **verifies implementation** |
| Full Home page design review | Scope is **foundation demo URL + shell** only |
| Replacement for Foundation QA | Calibration PASS is **input** to Foundation QA; QA still requires REPORT + checklist |
| Forge overlay phase | Forge may **reference** calibration findings; calibration is **Factory foundation** law |

---

## 2. Goal

Confirm that **implemented CSS/HTML on the Foundation Demo Page** faithfully expresses **approved Production Standards** — typography scale, color roles, radius tiers, spacing tokens, control heights, and section spacing samples — before multi-section Home complexity makes drift expensive to fix.

**Success criterion:** Lead can sign calibration with confidence that remaining work is **page composition**, not **token renegotiation**.

---

## 3. Inputs (entry criteria)

Stage **starts** only when **all** inputs are true:

| ID | Input | Source |
|----|-------|--------|
| IN-01 | **Production Standards** document approved | Project SSOT (signed / Lead ack) |
| IN-02 | **Shell** PASS — layout partials + foundation page entry in build | Shell stage deliverable |
| IN-03 | **Visual Foundation Contract** composition complete on demo URL | [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) §3 |
| IN-04 | **`npm run build` succeeds** | Build log (or SAFE UNKNOWN with explicit blocker) |
| IN-05 | **Desktop viewport** demo available ≥ project desktop breakpoint | Default 1024px |
| IN-06 | **Spacing demo labels** visible on page | Same-bg + diff-bg samples |

**Blocked start:** Missing §3 category on demo page → return to Visual Foundation; do not calibrate incomplete surface.

---

## 4. Outputs (exit artifacts)

| ID | Output | Consumer |
|----|--------|----------|
| OUT-01 | **Calibration RECORD** — inline in Foundation QA REPORT or standalone `# REPORT — <project> design calibration` | Foundation QA, audit trail |
| OUT-02 | **Token spot-check matrix** — standards clause → observed value → PASS/FAIL | Lead sign-off |
| OUT-03 | **Correction list** (if partial) — scoped fixes before Foundation QA | Engineering |
| OUT-04 | **Lead acknowledgment** — explicit PASS or waiver | Unblocks Foundation QA close |
| OUT-05 | **FINDINGS block** per [visual-reconciliation-layer.md](visual-reconciliation-layer.md) when visual ambiguity exists | REPORT standard |

**Recommended REPORT lines:**

```text
DESIGN CALIBRATION — PASS | partial (list) | FAIL
TOKEN SPOT-CHECK — PASS | partial (list) | FAIL
SECTION SPACING — PASS | partial | FAIL
```

For RU commercial projects add:

```text
RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial | FAIL | SAFE UNKNOWN
TYPOGRAPHY PRECISION (line-height = font-size + 4px) — PASS | partial (list) | FAIL | N/A (project exceptions documented)
LAYOUT PATTERN LIBRARY — PASS | partial (list LP-*) | NOT READY | N/A (foundation only)
```

---

## 5. Mandatory checks

Perform on **Foundation Demo Page** (+ shell header/footer as visible on same URL).

### 5.1 Typography calibration

| Check | Method |
|-------|--------|
| H1–H6 sizes, weights, line-heights | Compare computed styles vs Production Standards type table |
| **Line-height precision** | Default rows: `line-height = font-size + 4px` per [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §3 — or each exception named in standards |
| Body / secondary text | At least body default + one secondary tier |
| Forbidden typography (project-specific) | e.g. unauthorized `letter-spacing`, word-break rules — per standards law |
| RU projects | [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) spot-check |

### 5.2 Color and surface roles

| Check | Method |
|-------|--------|
| Primary text, accent, background wash | Token vs standards hex/rgba |
| Button primary / secondary / outline | Semantic roles match standards |
| Alert info/error colors | Distinct and readable |
| Card surface vs page background | Contrast acceptable per project policy |

### 5.3 Radius and control geometry

| Check | Method |
|-------|--------|
| Default card/section radius | Measure on card sample |
| Input/control radius | Measure on form sample |
| Circular/pill radius | If standards define (e.g. 999px) — verify on applicable control |
| Button heights | Primary + header CTA if separate |

### 5.4 Spacing and grid

| Check | Method |
|-------|--------|
| Container max-width and horizontal padding | Desktop + mobile |
| Same-bg spacing sample | Matches mapped token — no double-gap |
| Different-bg / band spacing sample | Matches mapped token |
| **Spacing scale compliance** | Gap/margin/padding on demo samples use [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §2 or project SSOT tokens — no ad-hoc px |
| WF Grid alignment | Header, demo content, footer share container contract — [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) |

### 5.5 Component behavior samples

| Check | Method |
|-------|--------|
| FAQ accordion / details | Open/close; single-open if required |
| Form validation state | Error visible without JS-only gate |
| Disabled button | Non-interactive appearance |
| Focus/hover | Keyboard focus visible on links and buttons |

### 5.6 Shell integration (on demo URL)

| Check | Method |
|-------|--------|
| Header desktop structure | Matches block charter / standards |
| Footer desktop structure | Column layout per standards |
| Mobile shell (if mobile pass claimed) | Header/footer/stack at ≤ mobile breakpoint |

---

## 6. PASS criteria

**Design Calibration PASS** when **all** apply:

| # | Criterion |
|---|-----------|
| P-01 | Every **mandatory check** in §5 executed with evidence (screenshot list or viewport table) |
| P-02 | **Token spot-check:** zero FAIL on **blocking** tokens (container, primary type scale, primary/accent colors, default radius tiers, primary button) |
| P-03 | **SECTION SPACING — PASS** or partial with **Lead-approved** exceptions documented |
| P-04 | **No Home blocks** present on foundation page or in premature page files |
| P-05 | **Lead acknowledgment** recorded (name/date in REPORT or signed checklist) |
| P-06 | **Build green** at time of calibration (or explicit SAFE UNKNOWN with rebuild before Foundation QA) |

**Partial PASS:** Allowed only with **written exception list** and Lead ack; each exception must cite standards clause and waiver reason. Foundation QA may still FAIL if exceptions exceed project policy.

---

## 7. FAIL criteria

**Design Calibration FAIL** if **any** trigger fires:

| ID | FAIL trigger | Required action |
|----|--------------|-----------------|
| F-01 | Missing Visual Foundation category | Return to Visual Foundation stage |
| F-02 | Blocking token drift (wrong container, wrong primary scale, wrong accent, wrong default radius) | Fix global styles — **no Home work** |
| F-03 | Spacing double-gap or unmapped inter-section rhythm | Apply [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) |
| F-04 | Typography law violation (forbidden CSS on RU project) | Remove violation before re-calibration |
| F-05 | Line-height drift — arbitrary px/decimals not in standards | Fix global type — cite [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) |
| F-06 | Home hero or PG-001 block leaked into foundation page | Remove leakage; re-run calibration |
| F-07 | Build broken / dist stale with no evidence | Rebuild; recalibrate |
| F-08 | Calibration skipped — Foundation QA attempted without OUT-01 | **STOP** — complete calibration first |
| F-09 | Standards doc not approved | Return to [production-standards-governance-v1.md](production-standards-governance-v1.md) Approval gate |

**Fail loop:** Fix → rebuild → re-calibrate → record new PASS in REPORT.

---

## 8. Agent / operator behavior

| Situation | Required response |
|-----------|-------------------|
| User requests Home while calibration open | **STOP** — cite stage chain §1.1 |
| Demo page complete but tokens untested | Run §5 checks; file calibration RECORD |
| Minor non-blocking drift (caption size, secondary radius on unused pattern) | Document as **partial** with Lead decision |
| Standards ambiguity discovered | Escalate HITL — **do not** invent tokens on Home |

---

## 9. Workflow alignment

| Factory artifact | Alignment |
|------------------|-----------|
| [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | Calibration sits after Visual Foundation content; Foundation QA follows calibration |
| [website-factory-workflow-v0.md](website-factory-workflow-v0.md) S11 | Pre-S11 **foundation sub-stages** — documentation addendum; does not rename S11 |
| [onboarding-flow-v1.md](onboarding-flow-v1.md) Path B | New workspace must pass calibration before first commercial section |
| FP-0002 instance docs | **Read-only** reference — not modified by Evolution Pack |

---

## 10. Changelog

| Date | Change |
|------|--------|
| 2026-06-13 | v1 — Design Calibration stage formalized; Evolution Pack v1. |
| 2026-06-13 | v1.1 — Stage chain: Production Standards Draft → Approval ([production-standards-governance-v1.md](production-standards-governance-v1.md)). |
| 2026-06-13 | v1.2 — Precision Governance: line-height pre-flight, spacing scale check, REPORT lines. |
