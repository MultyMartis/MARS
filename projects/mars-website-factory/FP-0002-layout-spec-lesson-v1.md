# FP-0002 — Layout Spec Lesson v1

**ID:** `FP-0002-LAYOUT-SPEC-LESSON`  
**Status:** **documented** — Factory lesson from FP-0002 Shpigovsky.ru frontend operations.  
**Not:** retroactive fix of FP-0002 header code; **not** modification of FP-0002 workspace artefacts.

**Date:** 2026-06-14  
**Authority:** [layout-spec-law-v1.md](layout-spec-law-v1.md) — canonical law promoted from this incident.

**Read-only FP-0002 references:** [FP-0002-HEADER-MINI-AUDIT-v1.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-HEADER-MINI-AUDIT-v1.md) · [FP-0002-DESIGN-AUDIT-v1.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-DESIGN-AUDIT-v1.md) · [website-factory-production-roadmap-v2-draft.md](website-factory-production-roadmap-v2-draft.md) §5.

---

## 1. What happened

During FP-0002 Phase C (Desktop Shell), the agent received **Visual SSOT** (design PDFs and prior audit artefacts) for the site header.

Instead of producing a **Layout Spec** — a written decomposition of zones, rows, grouping, and container model — the agent proceeded directly to **Header HTML/CSS**.

The implemented header was **radically unlike** the design composition (row structure, grouping, visual hierarchy).

---

## 2. Root cause (systemic)

| Factor | Detail |
|--------|--------|
| **Missing artifact** | No **Layout Spec** existed between Visual SSOT and implementation |
| **Agent path taken** | `Visual SSOT → internal interpretation → HTML/CSS` |
| **Not the cause** | PDF quality, Figma availability, or source file format |
| **Partial substitute failed** | Header Mini-Audit listed **content elements** (phones, nav labels) but did **not** lock **composition** (dual-row structure, zone grouping, row contents) |

---

## 3. Why detection was late

| Gate | Why it did not catch composition drift |
|------|----------------------------------------|
| **Design Audit (Phase A)** | Page/block inventory and gaps — not per-block layout decomposition |
| **Production Standards + Mapping QA** | Tokens and numeric mapping — not zone structure |
| **Shell-first protocol** | Enforces **order** (shell before Home) — not **composition spec** before Header code |
| **Build PASS** | Syntax and compile — not layout fidelity |
| **Enforcement Pack** | Compiled CSS / OL compliance — not composition model |
| **Operator Visual Approval Law** | Runs **after** implementation — correct gate, **too late** for prevention |
| **Pixel Fidelity** | Post-implementation numeric audit — not pre-code composition lock |

**Discovery mechanism:** Operator visual comparison (screenshots) — not upstream documentation gate.

---

## 4. Correct capture point

**Layout Spec Gate** — immediately **before** any Header HTML/CSS for Phase C.1.

Required sequence that would have prevented the failure:

```text
Visual SSOT
    ↓
Layout Spec (Header) — zones, 2 rows, grouping, container model, frozen decisions
    ↓
Operator APPROVED
    ↓
Header HTML/CSS
    ↓
Operator Visual Review (post-build)
```

---

## 5. Lesson (normative for Factory)

1. **Content audit ≠ Layout Spec.** Confirming nav labels and phone numbers does not substitute for composition decomposition.
2. **Visual SSOT alone is insufficient** for agents. Format (PDF/Figma/PNG) is irrelevant; **written Layout Spec + operator APPROVED** is mandatory.
3. **"I understood the design" is not a gate.** Only **APPROVED Layout Spec** unlocks HTML/CSS.
4. **Post-build operator review is necessary but not sufficient.** It catches failures **after** rework cost; Layout Spec Gate prevents **structural fantasy** before code.

---

## 6. v2 Factory response

| Action | Document |
|--------|----------|
| Canonical law | [layout-spec-law-v1.md](layout-spec-law-v1.md) |
| Roadmap integration | [website-factory-production-roadmap-v2-draft.md](website-factory-production-roadmap-v2-draft.md) — Phase C/F Layout Spec gates |
| Shell-first integration | [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) — Phase 0.6 / pre–Phase 1 |
| Failure attribution | [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md) — **LAYOUT SPEC SKIPPED** · **PRE-LAYOUT-SPEC STARTER RESIDUE** |

---

## 7. Changelog

| Date | Change |
|------|--------|
| 2026-06-14 | v1 — lesson filed from FP-0002 header failure; promotes Layout Spec Law. |
