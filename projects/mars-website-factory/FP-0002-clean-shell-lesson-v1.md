# FP-0002 — Clean Shell Lesson v1

**ID:** `FP-0002-CLEAN-SHELL-LESSON`  
**Status:** **documented** — Factory lesson from FP-0002 Shpigovsky.ru frontend operations.  
**Not:** retroactive fix of FP-0002 workspace artefacts; **not** modification of FP-0002 frontend code.

**Date:** 2026-06-14  
**Authority:** [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) — canonical starting state promoted from this incident.

**Read-only FP-0002 references:** [FP-0002-WORKSPACE-RESET-V2-REPORT.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-WORKSPACE-RESET-V2-REPORT.md) · [FP-0002-RESET-COMPLETE.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-RESET-COMPLETE.md) · [FP-0002-layout-spec-lesson-v1.md](FP-0002-layout-spec-lesson-v1.md).

---

## 1. What happened

During FP-0002 frontend production, the workspace started from (or accumulated) a **visually rich gulp-starter / foundation demo** — tokens, buttons, typography samples, and partial shell work — **before** a mandatory **Layout Spec** and **before** operator-approved composition.

The agent treated existing starter chrome and demo patterns as **implicit authority** and proceeded to Header implementation from **visual interpretation** rather than from an **APPROVED Layout Spec**.

Combined with [FP-0002-layout-spec-lesson-v1.md](FP-0002-layout-spec-lesson-v1.md), this produced **FP-0002 HEADER FAILURE**.

RESET V3 established **CANONICAL CLEAN SHELL V1** — a workspace where only **HEADER NOT STARTED / MAIN NOT STARTED / FOOTER NOT STARTED** is visible.

---

## 2. Root cause (systemic)

| Factor | Detail |
|--------|--------|
| **Beautiful starter residue** | Rich demo content invited reuse of wrong layout patterns |
| **Empty shell absent** | No enforced “agent has not started inventing” baseline |
| **Layout Spec skipped** | See [FP-0002-layout-spec-lesson-v1.md](FP-0002-layout-spec-lesson-v1.md) |
| **False sense of progress** | Tokens and demo SCSS present → operator and agent perceived foundation as “started” |

---

## 3. Core lesson (normative for Factory)

> **A beautiful starting template is more dangerous than an empty shell.**

| Shell type | Risk profile |
|------------|--------------|
| **Empty Clean Shell** | **Safe** — forces explicit Layout Spec and operator approval before chrome |
| **Beautiful starter / demo shell** | **Dangerous** — provokes agent to reuse old decisions without Layout Spec |

**Corollary:** If the screen looks boring, the agent has **not** started inventing. That is **desired state** until Layout Spec APPROVED.

---

## 4. v2 Factory response

| Action | Document |
|--------|----------|
| Canonical starting state | [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) |
| Composition gate (unchanged) | [layout-spec-law-v1.md](layout-spec-law-v1.md) |
| Roadmap integration | [website-factory-production-roadmap-v2-draft.md](website-factory-production-roadmap-v2-draft.md) — Phase B Clean Shell |
| Shell-first integration | [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) |
| Failure attribution | [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md) — **PRE-LAYOUT-SPEC STARTER RESIDUE** |

---

## 5. Changelog

| Date | Change |
|------|--------|
| 2026-06-14 | v1 — lesson filed from FP-0002 RESET V3; promotes Canonical Clean Shell v1. |
