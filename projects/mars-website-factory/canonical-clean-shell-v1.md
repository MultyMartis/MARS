# MARS Website Factory — Canonical Clean Shell v1

**ID:** `CANONICAL-CLEAN-SHELL-V1`  
**Status:** **Canonical Foundation Authority** — mandatory **starting state** for all future Website Factory frontend workspaces.  
**Not:** runtime orchestration, automated workspace bootstrap, CI enforcement, or a gulp-starter template product.

**Date:** 2026-06-14  
**Provenance:** FP-0002 Shpigovsky.ru — RESET V3 COMPLETE; operator-approved clean shell on `desktop-shell.html`.  
**Scope boundary:** Website Factory **governance documentation only**. Does **not** modify FP-0002 workspace artefacts, frontend source code, or project working documents.

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules)

**Related (detail — do not duplicate here):**

| Document | Role |
|----------|------|
| [layout-spec-law-v1.md](layout-spec-law-v1.md) | Layout Spec Gate — unlocks Header/Footer HTML **after** Clean Shell |
| [group-decomposition-law-v1.md](group-decomposition-law-v1.md) | Group Decomposition Gate — discrete GROUP-IDs **before** Layout Spec |
| [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | Shell-first phase chain — Clean Shell precedes Phase 1 shell HTML |
| [website-factory-production-roadmap-v2-draft.md](website-factory-production-roadmap-v2-draft.md) | Phase B workspace creation — Clean Shell is mandatory baseline |
| [workspace-reset-governance.md](workspace-reset-governance.md) | Full-cycle restart — fresh tree must land on Clean Shell, not starter demo residue |
| [FP-0002-layout-spec-lesson-v1.md](FP-0002-layout-spec-lesson-v1.md) | Composition failure without Layout Spec |
| [FP-0002-clean-shell-lesson-v1.md](FP-0002-clean-shell-lesson-v1.md) | Instance lesson — beautiful starter vs empty shell |
| [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md) | Failure class **PRE-LAYOUT-SPEC STARTER RESIDUE** |

---

## 1. Definition — CANONICAL CLEAN SHELL V1

**Canonical Clean Shell V1** is a **clean starting frontend workspace** in which the visible page contains **only**:

```text
HEADER NOT STARTED

MAIN NOT STARTED

FOOTER NOT STARTED
```

**And nothing else.**

No interpreted chrome. No demo components. No inherited starter marketing blocks. No agent-invented layout.

The screen may look **boring**. That is **correct**.

---

## 2. Mandatory workspace contents

Every Factory frontend workspace at Clean Shell state **must** include:

| Element | Requirement |
|---------|-------------|
| **Build pipeline** | Gulp (or approved Factory template) — `npm install` + `npm run build` PASS |
| **`src/`** | Source tree — layout placeholders only until Layout Spec APPROVED |
| **`dist/`** | Build output — never hand-edited |
| **`reports/`** | Project REPORT folder or equivalent evidence path |
| **`backups/`** | Snapshot / stable-backup discipline per [workspace-reset-governance.md](workspace-reset-governance.md) · [freeze-discipline-v1.md](freeze-discipline-v1.md) |
| **`versions/`** | Version / milestone markers for operator recovery |
| **`desktop-shell.html`** | Shell entry page — **only** NOT STARTED markers in header / main / footer |

**Honesty boundary:** Folder names may vary by project charter; **semantic presence** of each element is mandatory. Missing element → **STOP** — workspace is not Clean Shell.

---

## 3. Forbidden until Layout Spec APPROVED

The following **must not exist** in `src/` or on the shell URL **before** operator **APPROVED** Layout Spec per [layout-spec-law-v1.md](layout-spec-law-v1.md):

| Category | Forbidden artefacts |
|----------|---------------------|
| **Shell chrome** | header html · footer html · navigation · logo · phones · cta · menu · mobile menu |
| **Pages** | hero · home · ui-demo |
| **Foundation demo** | tokens · buttons · forms · cards · faq · alerts |
| **Overlays** | modals · popups |

**Rule:** If any row above is present in source or visible on build output → workspace has **drifted from Clean Shell**. Agent **must stop** and reset or strip to Clean Shell before Layout Spec work.

**Unlock sequence:**

```text
Clean Shell (this document)
    ↓
Layout Spec (Header · Footer) — operator APPROVED
    ↓
Header / Footer HTML/CSS
    ↓
Operator Visual Review
```

---

## 4. Main principle — boring is correct

| Screen appearance | Meaning |
|-------------------|---------|
| **HEADER NOT STARTED** | Agent has **not** started inventing header chrome |
| **MAIN NOT STARTED** | Agent has **not** started inventing page content |
| **FOOTER NOT STARTED** | Agent has **not** started inventing footer chrome |

**If the screen looks boring:** that is **good**.

**Translation:** **AGENT HAS NOT STARTED INVENTING.**

A visually rich starter page, demo index, or pre-built UI library in the workspace is **not progress** — it is **risk**.

---

## 5. FP-0002 lesson — why Clean Shell exists

### 5.1 Old approach (failed)

```text
Design Audit → Foundation → Header
```

**Outcome:** [FP-0002 HEADER FAILURE](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-HEADER-MINI-AUDIT-v1.md)

| Root cause | Detail |
|------------|--------|
| **VISUAL INTERPRETATION WITHOUT LAYOUT SPEC** | Agent implemented header from internal reading of Visual SSOT |
| **LAYOUT SPEC SKIPPED** | No written composition decomposition before HTML/CSS |
| **Starter residue** | Beautiful gulp-starter / foundation demo content invited reuse of wrong patterns |

**Canonical law promoted from composition failure:** [layout-spec-law-v1.md](layout-spec-law-v1.md)  
**Canonical lesson — starter vs empty shell:** [FP-0002-clean-shell-lesson-v1.md](FP-0002-clean-shell-lesson-v1.md)

### 5.2 New order (normative for Factory)

```text
A0  Source Discovery
    ↓
A1  Design Audit
    ↓
    Operator Decisions
    ↓
    Clean Shell                    ← CANONICAL CLEAN SHELL V1 (this document)
    ↓
    Layout Spec
    ↓
    Operator Approval
    ↓
    Header
    ↓
    Visual Review
```

**Roadmap alignment:** [website-factory-production-roadmap-v2-draft.md](website-factory-production-roadmap-v2-draft.md) — Phase B lands on Clean Shell; Phase C follows Layout Spec gate.

---

## 6. Agent / operator stop rules

| Situation | Required response |
|-----------|-------------------|
| Workspace has starter demo home, ui-demo, or component SCSS before Layout Spec | **STOP** — strip to Clean Shell or fresh reset |
| Operator asks for Header before Layout Spec APPROVED | **STOP** — [layout-spec-law-v1.md](layout-spec-law-v1.md) |
| Screen shows real nav, logo, buttons, or hero | **STOP** — not Clean Shell |
| Build PASS but page is not three NOT STARTED markers | **STOP** — technical PASS ≠ Clean Shell compliance |
| Reset complete but residue from prior pass remains | **STOP** — [workspace-reset-governance.md](workspace-reset-governance.md) |

---

## 7. Adoption

| Field | Value |
|-------|-------|
| **Factory-wide mandatory** | **Yes** — all greenfield Website Factory frontend projects from 2026-06-14 promotion |
| **FP-0002 instance** | RESET V3 COMPLETE — read-only reference; **do not modify** FP-0002 workspace in promotion tasks |
| **Supersedes** | Implicit “start from rich gulp-starter demo” and “Foundation Demo before empty shell” orders |

---

## 8. Changelog

| Date | Change |
|------|--------|
| 2026-06-14 | v1 — CANONICAL CLEAN SHELL V1 promoted from FP-0002 RESET V3; mandatory empty shell before Layout Spec. |
