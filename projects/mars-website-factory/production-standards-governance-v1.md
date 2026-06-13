# MARS Website Factory — Production Standards Governance v1

**Status:** **documented** — mandatory **Factory-level** governance for Project Production Standards authorship, approval, freeze, and change control.  
**Not:** runtime schema, automated token linter, CI gate, or project-specific token values.

**Purpose:** Formalize the **pre-Shell** stage pair where every Website Factory Gulp project must **draft**, **review**, and **approve** a Project Production Standards document before any HTML/SCSS/JS work begins.

**Provenance:** FP-0002 Shpigovsky audit (2026-06-13) — `FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md` demonstrated a repeatable pattern (normalization → draft → Lead corrections → approval → freeze) that existed only at project level. This document promotes the **mechanism** to Factory system rules; FP-0002 instance docs remain **read-only** reference.

**Authority order (canonical):** [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) — Project Production Standards = **rank 1**; Approved Operator Laws = **rank 2**; this doc = **rank 3** process for rank-1 authorship.

**Related:**

| Document | Role |
|----------|------|
| [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) | Canonical 6-layer frontend decision hierarchy + OL-01–OL-07 |
| [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | Start gate — Phase 0 maps to Draft + Approval |
| [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) | Section spacing tokens — mandatory category in standards doc |
| [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) | Requires approved standards before Visual Foundation |
| [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) | Verifies **implementation** — not re-approval of standards |
| [frontend-production-rules-v0.md](frontend-production-rules-v0.md) | Operator rules — points here for standards gate |
| [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) | Grid token mapping obligation |
| [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) | Layout zone mapping obligation |
| [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) | Factory spacing/type precision — normalization defaults for Draft |
| [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md) | LP-01–LP-08 pattern obligation in C-11 |
| [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) | Multi-source extraction layers; layout chain; **DESIGN → FRONTEND MAPPING QA** before Approval |

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules).

**Project instance (read-only):** [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) — **do not edit** for Factory evolution.

---

## 1. Canonical stage chain (Factory v1)

```text
Production Standards Draft
        ↓
DESIGN → FRONTEND MAPPING QA   ← mapping completeness (design-source-to-frontend-mapping-governance-v1)
        ↓
Production Standards Approval
        ↓
Shell
        ↓
Visual Foundation
        ↓
Design Calibration
        ↓
Foundation QA
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

**Downstream page QA (post–Home):** [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) §11–12 · [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) §7 · [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) · [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.2–§6.

| Stage | Blocks Shell / HTML if missing |
|-------|--------------------------------|
| **Production Standards Draft** | **Yes** — no approval without draft |
| **Production Standards Approval** | **Yes** — no Shell without approval |
| Shell onward | Per [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) |

**Legacy alias:** Older docs used a single node **«Production Standards»** — that node is now **split** into Draft + Approval for clarity. Approval status is the gate; draft is the authoring phase.

---

## 2. Purpose (detailed)

Answer three questions with zero ambiguity:

1. **What** must every project document before frontend code?
2. **Who** approves it and with what evidence?
3. **When** is the standards SSOT frozen, and **how** may it change?

Project Production Standards is the **per-project SSOT** for token values (layout, typography, colors, spacing, radius, responsive behavior, components, assets, interaction defaults). Factory documents define **categories and process**; the project document defines **px/hex/token truth**.

---

## 3. Stage A — Production Standards Draft

### 3.1 Goal

Produce a **complete draft** Project Production Standards document covering all mandatory categories (§8) with traceable inputs — ready for Lead review.

### 3.2 Inputs

| ID | Input | Source | Required |
|----|-------|--------|----------|
| IN-D01 | **Frontend Handoff** or equivalent scope pack | S10 / project charter | **Yes** for greenfield |
| IN-D02 | **Design pack** (Figma export, PDF, PNG) or coordinator design facts | Design lane / client | Partial — placeholders per project policy |
| IN-D03 | **Frontend Normalization** pass (if design pack exists) | Engineering | Recommended |
| IN-D04 | **Numeric design rules** or raw measurements | Design evidence | Recommended |
| IN-D05 | **Site type** + block inventory context | Registry / IA | Recommended |
| IN-D06 | Factory mandatory rules | [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md), WF-GRID, WF-LAYOUT, [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) | **Yes** |

### 3.3 Outputs

| ID | Output | Consumer |
|----|--------|----------|
| OUT-D01 | **Project Production Standards Draft** (`<PROJECT>-PRODUCTION-STANDARDS-DRAFT-vN.md` or equivalent) | Approval stage |
| OUT-D02 | **Production Decisions** table (conflicts resolved, coordinator → production mapping) | Approval review |
| OUT-D03 | **Open Questions** list with blocker / non-blocker classification | Approval review |
| OUT-D04 | **SAFE UNKNOWN** register (assumptions requiring later verification) | Charter / QA |

### 3.4 Draft exit criteria

Draft is **ready for Approval** when:

- All **mandatory categories** (§8) have at least one row or explicit **TBD + policy** (not silent omission).
- Section spacing mapped per [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md).
- Conflicts between sources documented in Production Decisions — not hidden in prose.
- Document version number assigned (`v1`, `v2`, …).

**Draft does not block Shell** — only **Approval** does.

---

## 4. Stage B — Production Standards Approval

### 4.1 Goal

Obtain **Lead sign-off** on the draft as **project production SSOT** — frozen for Shell and downstream foundation work.

### 4.2 Inputs

| ID | Input | Source |
|----|-------|--------|
| IN-A01 | Production Standards **Draft** meeting §3.4 exit criteria | Draft stage |
| IN-A02 | Lead review window (corrections, questions) | HITL |
| IN-A03 | Factory mandatory rules cross-check | This doc §8 |

### 4.3 Outputs

| ID | Output | Consumer |
|----|--------|----------|
| OUT-A01 | **Approved Project Production Standards** (`<PROJECT>-PRODUCTION-STANDARDS-APPROVAL-vN.md` or equivalent) | Shell, Visual Foundation, Design Calibration, Charter |
| OUT-A02 | **Approval record** — status, approver, date, version | REPORT, audit trail |
| OUT-A03 | **Production Gate** verdict — READY / NOT READY for Shell | Operator, agent |

### 4.4 Approval exit criteria

Approval **PASS** when:

- **Approval Authority** (§5) has signed or acknowledged in REPORT.
- Status field set to one of: `APPROVED`, `APPROVED WITH CORRECTIONS`, `CONDITIONAL` (with explicit conditions).
- All **blocker-class** open questions resolved or waived with HITL.
- Document version **frozen** per §10.

**Shell / HTML work starts only after Approval PASS.**

---

## 5. Approval Authority

| Role | Responsibility |
|------|----------------|
| **Project Lead / Frontend Lead** | Final approval authority for production token SSOT |
| **Engineering (Frontend Lead delegate)** | Draft authorship, normalization, conflict resolution proposals |
| **Design coordinator / client** | Input facts — **not** production SSOT unless escalated to Lead |

**HITL rule:** No agent or operator may treat a draft as approved without explicit Lead acknowledgment in the standards doc or `# REPORT — <project> production standards approval`.

**Coordinator boundary:** Coordinator-provided design facts integrate as **inputs**; production mapping and numeric normalization remain **engineering + Lead** domain unless charter assigns otherwise.

---

## 6. Required Sections (mandatory categories)

Every Project Production Standards document (draft or approved) **must** include sections covering these **categories**. Values are **project-specific**; categories are **Factory-mandatory**.

| # | Category | Must define | Factory cross-ref |
|---|----------|-------------|-------------------|
| **C-01** | **Layout** | Container max-width, page padding (desktop/mobile), section types (content / wide / full-bleed) | WF-GRID-002 |
| **C-02** | **Typography** | Font family/loading, H1–H6 scale (desktop + mobile), body/lead/caption, weights, line-heights; default **`line-height = font-size + 4px`** or named exceptions per [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §3; RU projects: [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) | [typography-rhythm-governance.md](typography-rhythm-governance.md) |
| **C-03** | **Colors** | Text, background, accent, semantic roles (link, error, border); opacity/wash rules if used | — |
| **C-04** | **Spacing** | Base scale mapped to [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §2 gap/margin-padding scales (or documented project override in Production Decisions) | — |
| **C-05** | **Section spacing** | Same-background gap, different-background gap, mobile overrides | [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) |
| **C-06** | **Radius** | Default, control/input, circular/pill tiers | — |
| **C-07** | **Responsive** | Desktop/mobile breakpoint(s), collapse rules, artboard references (non-CSS) | [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) |
| **C-08** | **Components** | Buttons (primary/secondary/text), form controls (height, border, focus), tables, quotes — at token/pattern level | — |
| **C-09** | **Assets** | Logo, favicon, icon pipeline policy, font delivery (CDN/self-host), placeholder policy | — |
| **C-10** | **Interaction rules** | Accordion default (single-open etc.), hover/focus parity intent, sticky/modal layering policy (or defer to charter) | Progressive enhancement in AGENTS.md |
| **C-11** | **Grid / layout discipline** | Token names for `--container-max`, `--container-pad`; layout zone models (hero split, card grids); LP-01–LP-08 per [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md) | WF-GRID, WF-LAYOUT |
| **C-12** | **Production decisions** | Source priority table; conflict resolutions | — |
| **C-13** | **Open questions** | Blocker vs non-blocker classification | — |
| **C-14** | **SAFE UNKNOWN** | Assumptions + verify-by plan | — |
| **C-15** | **Approval record** | Status, approver, date, version | §5 |
| **C-16** | **Production gate** | READY / NOT READY for Shell; conditions | §11 |

**Optional project sections** (not Factory-mandatory): Excel/SEO intake, page inventory cross-check, project-specific block charters — include when project charter requires; do not omit C-01–C-16.

---

## 7. Change Control

| Change type | Allowed when | Process |
|-------------|--------------|---------|
| **Typo / clarity** in draft | Before approval | Edit draft; bump patch note |
| **Token value change** after approval | Only via governance | New document version (`vN+1`); ADR or written Lead decision; **re-run Design Calibration** if Shell/Foundation already built |
| **New mandatory Factory category** | Factory doc amendment | Existing projects **map on next charter revision** — no retroactive claim |
| **Emergency hotfix in code** | Production incident | **Forbidden** as SSOT change — patch code **and** file standards amendment in same REPORT |

**Rule:** Code and standards doc must not diverge. If code changes a token, standards version must increment or REPORT must flag **STRUCTURE CHANGE**.

---

## 8. Superseding Rules

| Rule | Behavior |
|------|----------|
| **Version chain** | `vN+1` explicitly **supersedes** `vN` in document header |
| **Single SSOT** | Only **one** approved version is active at a time |
| **Draft vs approved** | Draft never supersedes approved; Approval doc supersedes prior Approval |
| **Factory vs project** | **Project Production Standards (rank 1)** supersede Factory governance and Operator Laws on token conflict — see [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) §2 |
| **Project vs ad-hoc code** | Approved project standards supersede ad-hoc code comments and unstated agent choices |
| **Industry / agent vs Factory** | Industry Best Practice and Agent Preference **never** override ranks 1–4 — authority-order doc §2 |
| **Design pack vs standards** | After approval, **standards** supersede raw PDF/Figma numbers for production |
| **FP-0002 instance** | FP-0002 v3 remains its own SSOT — **not** superseded by this Factory doc |

---

## 9. Freeze Rules

| Event | SSOT state |
|-------|------------|
| Draft complete, not approved | **Mutable** — iterate freely |
| **Approval PASS** | **Frozen** for Shell + Visual Foundation + Design Calibration |
| Post–Foundation QA Home work | Frozen unless §7 change control triggered |
| Charter signed referencing standards vN | Charter binds to **vN** until amended |

**Freeze meaning:** Implementers treat approved values as **law** for foundation work. Design Calibration **verifies** implementation against frozen standards — it does **not** reopen token negotiation without §7 process.

---

## 10. Production Gate (Shell entry)

### Question

May **Shell** stage (HTML layout partials, foundation page entry) begin?

### Answer template

| Verdict | Condition |
|---------|-----------|
| **READY FOR SHELL** | Approval PASS (§4.4); all C-01–C-11 populated or explicitly waived with HITL; section spacing mapped |
| **NOT READY** | Draft only; missing mandatory categories; blocker open questions; no Lead ack |

**Downstream gates unchanged:** Shell PASS → Visual Foundation → Design Calibration → Foundation QA → Home ([frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md)).

---

## 11. Agent / operator behavior

| Situation | Required response |
|-----------|-------------------|
| User: «Сверстай главную» / «Start Home» | **STOP** — verify Approval PASS exists; else redirect to Draft → Approval → foundation chain |
| No standards doc | **STOP** — start Draft stage; cite this doc |
| Draft exists, not approved | **STOP** — route to Lead for Approval; no HTML |
| Approved standards exist + foundation REPORT | May proceed per shell-first protocol |
| Token mismatch on demo page | Design Calibration correction loop — **not** silent standards edit |

**REPORT heading (Approval):**

```text
# REPORT — <project> production standards approval
```

Include: version, approver, READY/NOT READY, open questions, link to standards doc path.

---

## 12. Workflow stage alignment

| Factory layer | This governance |
|---------------|-----------------|
| **Pre-S11 / Frontend Foundation** | Draft + Approval = **Phase 0** in [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) |
| **S10 Handoff** | Should reference `production_standards_approved: true|false` (recommended field) |
| **S11 Frontend Production** | Page blocks only after foundation chain; standards required at Phase 0 |

---

## 13. Changelog

| Date | Change |
|------|--------|
| 2026-06-13 | v1 — created from FP-0002 audit; splits Production Standards into Draft + Approval; defines mandatory categories C-01–C-16. |
| 2026-06-13 | v1.1 — Precision Governance Pack cross-refs: C-02 line-height, C-04 spacing scale, C-11 layout pattern requirement. |
| 2026-06-13 | v1.2 — [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) cross-ref; §8 superseding rules aligned to 6-layer hierarchy. |
