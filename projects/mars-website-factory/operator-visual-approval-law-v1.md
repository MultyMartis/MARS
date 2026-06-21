# MARS Website Factory — Operator Visual Approval Law v1

**Status:** **Canonical Foundation Authority** — documented **human-operated** law for Website Factory frontend visual stages.  
**Not:** runtime orchestration, automated HITL gate, CI enforcement, or policy engine.

**Version:** v1  
**Date:** 2026-06-14

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules)

**Peer authorities (detail — do not duplicate here):**

| Document | Role |
|----------|------|
| [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) | Mandatory **OPERATOR VISUAL REVIEW** REPORT block |
| [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md) | Failure cause **PROCEEDED WITHOUT OPERATOR VISUAL REVIEW** |
| [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | Shell-first phase chain — visual stages |
| [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) | Foundation QA gate — technical vs operator separation |
| [website-factory-production-roadmap-v2-draft.md](website-factory-production-roadmap-v2-draft.md) | Production phase operator approval points |
| [layout-spec-law-v1.md](layout-spec-law-v1.md) | **Pre-implementation** composition gate — APPROVED Layout Spec before HTML/CSS |
| [governance/P0-VISUAL-GATES-v1.md](../../governance/P0-VISUAL-GATES-v1.md) | Cross-program P0 visual gates — complementary, not superseded |

**Honesty boundary:** This law is **documentation discipline**. It does **not** claim an in-repo automated operator-review gate unless a project explicitly adopts checklists as tooling.

---

## 1. Purpose

Close the **technical PASS vs operator approval** gap identified in FP-0002 and aligned with P0 Visual Gates: agents and technical QA can emit **PASS** on structure, build, compiled CSS, and audit gates while the operator has **not** opened the page, **not** confirmed visual outcome, and **not** authorized the next visual stage.

This law defines:

1. What **does not** count as operator visual approval.
2. The **mandatory flow** after every visual stage.
3. The **Screenshot Override Law** — operator perception priority over agent audit when evidence is supplied.
4. The **FP-0002 workflow violation** when an agent closes a visual stage without requiring operator page review.

**Non-goal:** This law does **not** replace Design Calibration logic, Pixel Fidelity logic, Production Standards, Enforcement Pack, Compliance Decision Model, or **Layout Spec Law** — it **adds** the operator visual gate layer **after** technical checks. **Layout Spec operator APPROVED** is a **separate pre-code gate** per [layout-spec-law-v1.md](layout-spec-law-v1.md).

---

## 2. Provenance (FP-0002 incident)

**Project:** FP-0002 Shpigovsky.ru (Website Factory operations workspace).

**Incident pattern (documented):**

| Symptom | Effect |
|---------|--------|
| Foundation / UI Demo built; technical gates PASS | Operator saw engineering progress but **no explicit visual review request** |
| Agent closed visual stages with REPORT only | Next stage authorized without operator opening the page |
| Operator later reported visual defects with screenshots | Defects contradicted prior technical PASS lines |
| False PASS on governance gates | M2 ROOT CAUSE AUDIT → PRE-M2 reset ([FP-0002-RESET-COMPLETE.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-RESET-COMPLETE.md)) |

**Lesson promoted to Factory law:** **Technical closure ≠ product acceptance.** Every visual stage requires a **separate operator visual decision** after technical checks — not inferred from audit PASS, calibration PASS, or Foundation QA PASS.

**Authority input:** FP-0002 Operator Visual Approval Law Review (2026-06-14) — promotion architecture; **not** modified by this document.

---

## 3. Definitions

| Term | Definition |
|------|------------|
| **Visual stage** | Any Factory frontend step that changes **operator-visible** layout, typography, spacing, shell, header, footer, foundation demo, UI demo, or page/block slice — including Design Calibration close, Foundation QA close, header/footer pass, page QA close, and per-block production delivery. |
| **Technical PASS** | Agent or audit gate reports **PASS**, **PASS WITH NOTES**, or **WAIVED** on structure, build, compiled CSS, matrix, pixel fidelity, or enforcement gates — **without** operator visual acceptance. |
| **Operator Visual Review** | Human operator opens the **live or built page** at the stated viewport(s), inspects the visual outcome, and emits **ACCEPT** or **REVISE**. |
| **Operator Visual ACCEPT** | Operator records **ACCEPT** — visual outcome approved for the scoped stage; next visual stage may proceed. |
| **Operator Visual REJECT** | Operator records **REVISE** (same semantic as REJECT in REPORT block) — correction required; next visual stage **forbidden**. |
| **OPERATOR VISUAL REVIEW GATE** | Mandatory stop after technical REPORT — operator decision required before next visual stage. **Does not** replace **Layout Spec Gate** — composition APPROVED before code per [layout-spec-law-v1.md](layout-spec-law-v1.md). |
| **Screenshot Override** | Operator supplies page observation and/or screenshot; operator finding **outranks** agent audit PASS for the reported defect. |

---

## 4. OPERATOR VISUAL APPROVAL LAW

The following **never** constitute operator visual approval. They are **technical or audit outcomes only**:

| Outcome | Operator approval? |
|---------|-------------------|
| **TECHNICAL PASS** | **No** |
| **DESIGN CALIBRATION PASS** | **No** |
| **FOUNDATION QA PASS** | **No** |
| **HEADER PASS** | **No** |
| **FOOTER PASS** | **No** |
| **UI DEMO PASS** | **No** |
| **PAGE QA PASS** | **No** |

**Rule:** Any REPORT line showing **PASS** on the above **does not** set **OPERATOR VISUAL ACCEPT — ACCEPT**. Operator visual acceptance is a **separate field** per [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.7.

**Rule:** **PRODUCTION PASS**, **FINAL VERDICT — PRODUCTION PASS**, and **Foundation QA PASS** are **technical rollup verdicts**. They **do not** substitute for **OPERATOR VISUAL ACCEPT — ACCEPT** when a visual stage is closing.

---

## 5. Mandatory Flow

After **any visual stage** completes implementation and build:

```text
BUILD
        ↓
TECHNICAL CHECK
        ↓
REPORT
        ↓
STOP
```

After **STOP**, **always**:

```text
OPERATOR VISUAL REVIEW REQUIRED
```

**Allowed operator decisions:**

| Decision | Meaning | Next visual stage |
|----------|---------|-------------------|
| **ACCEPT** | Visual outcome approved for scope | **Permitted** |
| **REVISE** | Visual correction required | **Forbidden** until re-review after fix |

**Rule:** Transition to the **next visual stage** is **forbidden** without an operator decision recorded as **OPERATOR VISUAL ACCEPT — ACCEPT** or an explicit dated **WAIVE** with Lead signature per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md).

**Rule:** When **OPERATOR VISUAL ACCEPT — PENDING**, **OPERATOR ACTION REQUIRED — YES** is **mandatory**. **OPERATOR VISUAL ACCEPT — PENDING** with **OPERATOR ACTION REQUIRED — NO** is **forbidden** (reporting contradiction).

---

## 6. Forbidden Behaviors

| Forbidden | Correct action |
|-----------|----------------|
| Authorize next visual stage on technical PASS alone | Wait for **OPERATOR VISUAL ACCEPT — ACCEPT** or dated WAIVE |
| Set **OPERATOR VISUAL ACCEPT — ACCEPT** without operator opening page | Operator must inspect live/built page |
| Set **OPERATOR ACTION REQUIRED — NO** while **OPERATOR VISUAL ACCEPT — PENDING** | Set **OPERATOR ACTION REQUIRED — YES** |
| Close visual stage REPORT without **OPERATOR VISUAL REVIEW** block | Add block per reporting standard §5.7 |
| Treat Design Calibration PASS as Foundation close for operator | Run separate operator review at each visual stage close |
| Treat agent audit PASS as override of operator screenshot finding | Apply §7 Screenshot Override Law |
| Complete visual stage without explicit operator review request text | Apply §7 FP-0002 workflow violation rule |

---

## 7. SCREENSHOT OVERRIDE LAW

**Priority order (normative):**

```text
Operator Visual Review
        >
Agent Audit
        >
Technical Checks
```

When the operator:

1. **Opened** the page (or reviewed built output at stated viewport),
2. **Reported** a visual problem, and
3. **Supplied** a screenshot or equivalent visual evidence,

the operator's finding **outranks** agent audit and technical PASS lines for that defect.

**Rule:** Even if all audits show **PASS**, the operator report **blocks** progression until **REVISE** items are resolved and re-reviewed, or an explicit dated **WAIVE** is recorded with scope limit.

**Rule:** Agents **must not** dismiss operator screenshot evidence by citing technical PASS alone.

---

## 8. Priority Order

When documents or REPORT lines conflict on visual acceptance:

| Rank | Authority |
|------|-----------|
| 1 | **Operator Visual Review** — **ACCEPT** / **REVISE** (this law) |
| 2 | **Screenshot Override** — operator evidence with screenshot (§7) |
| 3 | **Agent audit gates** — Design QA Matrix, Pixel Fidelity, Enforcement Pack |
| 4 | **Technical checks** — build, compiled CSS, ROOT COMPLIANCE |

This law **does not** override rank-1 **Production Standards** or **Operator Laws (OL-01–OL-07)** for numeric/token authority — it governs **who may authorize visual progression**, not token values.

---

## 9. Relationship To Existing Governance

| Peer | Relationship |
|------|--------------|
| **P0 Visual Gates** ([P0-VISUAL-GATES-v1.md](../../governance/P0-VISUAL-GATES-v1.md)) | P0-01 **Technical PASS != Visual PASS** — this law is the **Website Factory canonical** expression; P0 gates remain cross-program minimum |
| **Enforcement Pack** | Unchanged — technical gates; operator visual review runs **after** enforcement rollup |
| **Compliance Decision Model** | Unchanged — forward compliance route; operator visual review is **downstream** of gate verdicts |
| **Design Calibration** | Unchanged — calibration PASS is technical; operator visual review **required separately** at calibration close |
| **Pixel Fidelity** | Unchanged — PF-* numeric bands; operator may override perception via §7 |
| **Foundation QA** | Unchanged checklist — adds **operator visual review** as exit requirement per [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) |
| **Production Roadmap v2** | Phase operator approval points cite this law |

**Non-goal:** No new governance wave. No additional law documents beyond this canonical file.

---

## 10. Scope

**Applies to:**

- All Website Factory **greenfield frontend** projects using Shell-first protocol
- All **visual stage closes** — shell, header, footer, Visual Foundation, Design Calibration, Foundation QA, UI Demo, page/block production, page QA close
- All agents and operators filing Frontend QA REPORTs per [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md)

**Factory-wide mandatory:** **Yes** — for Website Factory frontend visual work unless project charter documents an explicit dated exception with Lead signature.

---

## 11. Non-Scope

This law **does not** apply to or modify:

| Excluded | Reason |
|----------|--------|
| **Enforcement Pack** gate logic | Technical layer — referenced, not changed |
| **Compliance Decision Model** | Verdict route — referenced, not changed |
| **Production Standards** content | SSOT tokens — not visual acceptance |
| **Design Calibration** checklist content | Token verification — operator review added separately |
| **Pixel Fidelity** numeric rules | Audit bands — not changed |
| **FP-0002 workspace artefacts** | Read-only provenance — not modified |
| **Frontend source code** | Governance only |
| **Non-visual waves** | Config, SEO meta, backend — unless wave claims visual impact |

---

## 12. Adoption

**Effective:** 2026-06-14 upon promotion to Website Factory governance.

**Mandatory REPORT block:** [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.7 — **OPERATOR VISUAL REVIEW**.

**Failure attribution:** [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md) — **PROCEEDED WITHOUT OPERATOR VISUAL REVIEW** at **OPERATOR VISUAL REVIEW GATE**.

**FP-0002 workflow violation (normative):**

If an agent completes a visual stage and **does not** require the operator to open the page, this is a **workflow violation**.

The agent **must** explicitly state (Russian or English equivalent):

```text
Откройте страницу.
Проверьте результат.
Требуется решение оператора.
```

Or equivalent unambiguous wording that:

1. Instructs the operator to **open** the page,
2. Instructs **visual verification**, and
3. States that **operator decision is required** before continuation.

**Silent closeout** after technical REPORT — without the above — is **PROCEEDED WITHOUT OPERATOR VISUAL REVIEW**.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-14 | v1 — Operator Visual Approval Law promotion from FP-0002 review; canonical Factory law. |
| 2026-06-14 | v1.1 — Peer pointer to Layout Spec Law — pre-code vs post-build operator gates distinguished. |
