# FP-0002 EXECUTION BRAIN v1

**Document type:** Execution aggregation layer — FP-0002 M2 pass  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-14  
**Status:** **documented** — aggregation only; **does not** create new authority  

**Scope:** Human-operated execution guide for the **next M2 Foundation pass** (Charter Phases 1–7 / Start Sequence Steps 1–7).  
**Not:** runtime, CI, automated enforcement, new governance, or replacement for rank-1 SSOT.

**Supersedes:** Nothing. This doc **aggregates** existing authority — it does **not** override it.

---

## 1. Purpose

### 1.1 Что это

**FP-0002 EXECUTION BRAIN** — единая стартовая точка для агента или оператора перед **новым M2 проходом** (Foundation production: shell → typography/UI demo → header/footer → global styles → mobile shell → Design Calibration → Foundation QA).

Документ собирает правила из:

- Project SSOT (FP-0002 ops)
- Website Factory Governance (Foundation packs, post–M2 audit)
- Lessons learned первого уничтоженного M2 прохода

### 1.2 Что агрегирует

| Класс | Примеры |
|-------|---------|
| **Rank-1 SSOT** | Production Standards v3, Charter, Start Sequence |
| **Rank-2 Operator Laws** | OL-01–OL-07 |
| **Rank-3 Factory gates** | Shell-first, Mapping, Calibration, Foundation QA, Enforcement |
| **Post-audit packs** | EG-01–EG-05, Compliance Decision Model, Failure Attribution |
| **Project snapshot** | PRE-M2 restore state (2026-06-14) |

### 1.3 Что НЕ переопределяет

| Нельзя | Почему |
|--------|--------|
| Менять токены v3 | Rank 1 — только ADR + новая версия SSOT |
| Создавать новые Operator Laws | Rank 2 — только Factory authority-order |
| Заменять gate verdict vocabulary | Reporting standard + Enforcement Pack |
| Авторизовать M2 без operator charter | Reset report: новый M2 spec + Lead authorization required |
| Claim PASS без ROOT COMPLIANCE | Enforcement Pack §6 — hard rule |

**Правило цитирования:** каждый тезис ниже ссылается на authority source. Если source отсутствует → **UNKNOWN**.

---

## 2. Canonical Authority Order

**Только FP-0002-relevant hierarchy.** Полная версия — Factory doc.

**Authority:** [frontend-production-authority-order-v1.md](../../../projects/mars-website-factory/frontend-production-authority-order-v1.md)

| Rank | Layer | FP-0002 instance / role |
|------|-------|-------------------------|
| **1** | **Project Production Standards** | [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) — **APPROVED WITH ANDREY CORRECTIONS** (2026-06-13). Единственный SSOT для px, hex, radius, breakpoints, typography law. |
| **2** | **Approved Operator Laws** | OL-01–OL-07 в authority-order §3. Spacing scale, layout pattern first, typography precision, RU HTML typography. |
| **3** | **Website Factory Governance** | Shell-first, Mapping, Calibration, Foundation QA, Precision, Section spacing, Enforcement, Compliance Decision, Failure Attribution. |
| **4** | **Layout Pattern Library** | WF-GRID, WF-LAYOUT, LP-* — pick named patterns; no ad-hoc `%` splits. **Note:** v3 не содержит formal LP-* IDs — naming debt (Mapping QA §11.1). |
| **5** | **Industry Best Practice** | Advisory only — mobile-first defaults, rem stacks, Lighthouse heuristics **не** override desktop-first v3. |
| **6** | **Agent Preference** | **Forbidden as override** — «cleaner look», «modern», agent rounding. |

**Critical conflict (FP-0002):** Rank 1 **wins** over Rank 2 on same property — **но** rank-1 value, violating OL, **требует Exception Registry** до WAIVED/PASS на EG-01/02/04. Rank-1 permit ≠ auto-waive OL.

**Authority:** authority-order §6–§7 · [website-factory-enforcement-pack-v1.md](../../../projects/mars-website-factory/website-factory-enforcement-pack-v1.md) §4–§5

---

## 3. Project Snapshot

**Authority:** [REPORTS/FP-0002-RESET-COMPLETE.md](REPORTS/FP-0002-RESET-COMPLETE.md) · [FP-0002-FRONTEND-PRODUCTION-CHARTER-v1.md](FP-0002-FRONTEND-PRODUCTION-CHARTER-v1.md)

### 3.1 Стартовое состояние (после rollback, 2026-06-14)

| Check | State |
|-------|-------|
| **PRE-M2 restored** | **YES** — snapshot `WEBSITE-FACTORY-FP-0002-PRE-M2-SNAPSHOT-2026-06-13-v1` |
| **Production Standards v3** | **APPROVED WITH ANDREY CORRECTIONS** |
| **Mapping QA** | **PASS WITH NOTES** — [FP-0002-DESIGN-FRONTEND-MAPPING-QA-RECORD-v1.md](FP-0002-DESIGN-FRONTEND-MAPPING-QA-RECORD-v1.md) |
| **Charter v1** | **ISSUED** — READY FOR FOUNDATION PRODUCTION |
| **First M2 pass** | **DESTROYED** — M2 artifacts removed from frontend + ops |
| **Factory Governance (post-audit)** | **RETAINED** — Enforcement, Compliance Decision, Failure Attribution packs in `projects/mars-website-factory/` |
| **Home page (PG-001)** | **FORBIDDEN** until Foundation QA PASS (Phase 7) |

### 3.2 Что существует

| Area | Evidence |
|------|----------|
| **Ops documentation** | Charter, v3 SSOT, Start Sequence, Foundation v1, Page/Block Inventory, Mapping QA, Normalization, Numeric Rules, Design Approval Sheet, Excel intake refs, 24 PDF design pack in `INCOMING/01_DESIGN/` (per reset report) |
| **Frontend workspace** | `workspaces/fp-0002-shpigovsky-frontend/` — **M1 scaffold only** |
| **M1 frontend files** | `ui-demo.html`, `ui-demo-shell.html` placeholder, layout partials skeleton, `_variables.scss` placeholder comment `// Production tokens — wired in M2+`, empty component barrel |
| **Build** | M1 builds successfully (`npm ci` + `npm run build` verified at reset) |
| **Foundation Governance packs** | Enforcement, Compliance Decision, Failure Attribution — Factory level |

### 3.3 Чего не существует

| Missing | Impact |
|---------|--------|
| **M2 Foundation Demo implementation** | Phases 1–7 code **not started** |
| **FP-0002-M2-FOUNDATION-DEMO-SPEC-v1.md** | Removed from active ops — **new spec required** under updated governance + operator authorization |
| **Wired production tokens in SCSS** | `_variables.scss` = M1 placeholder |
| **Foundation component SCSS** | `_buttons`, `_cards`, `_forms`, etc. — deleted at reset |
| **`fd-sec-*` foundation demo sections** | Deleted at reset |
| **Design Calibration REPORT** | Not filed |
| **Foundation QA REPORT** | Not filed |
| **Exception Registry for rank-1 vs OL conflicts** | **Not created** — critical for M2 PASS under new Enforcement |
| **Archived M2 QA REPORT with `dist/*.css` grep** | **UNKNOWN** — not found in repo; violations reconstructed from audit provenance |

### 3.4 Stale register warning

**Authority:** [PROJECT-STATUS.md](PROJECT-STATUS.md) (2026-06-11)

`PROJECT-STATUS.md` показывает **Pre-Onboarding / Not Started** — **устарел** относительно фактического PRE-M2 restore. Для execution использовать **RESET-COMPLETE + Charter + v3**, не PROJECT-STATUS.

---

## 4. Production Standards Summary

**Authority:** [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) §2–§9

Только то, что агент **обязан** знать для M2. Полная таблица — в SSOT.

### 4.1 Container

| Token | Value | Notes |
|-------|-------|-------|
| `container-max` | **1170px** | Olga override; not 1160 |
| `page-padding-x-desktop` | **40px** | PD-13; not 50px |
| `page-padding-x-mobile` | **20px** | |
| Model | viewport → bg-base → optional bg-page wash → padding → container 1170 centered | §3.3 |

### 4.2 Typography

| Tier | Desktop | Mobile | Weight | Line-height |
|------|---------|--------|--------|-------------|
| H1 Display | 70px | 42px | 500 | 84 / 50 |
| H2 Section | **36px** | **22px** | **500** | 44 / 28 |
| Body | **18px** | **16px** | **300** | 28 / 24 |
| Button | 16px | 16px | 500 | 20 |

**Hard law (Lead v3):** `letter-spacing`, `word-break`, `overflow-wrap`, `hyphens` — **forbidden** (any value; property presence = FAIL) without separate Lead approval + Exception Registry.

**Authority:** v3 §4.3 · [russian-no-word-splitting-typography-v1.md](../../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md)

### 4.3 Spacing (project 4px-base scale)

| Token | px | Common use |
|-------|-----|------------|
| `space-4` | 16 | Form field gap, inline stacks |
| `space-6` | 24 | Card grid gap, card padding |
| `space-7` | 32 | Breadcrumb-to-hero |
| `space-8` | 40 | Page padding desktop |
| `space-11` | 64 | Mobile inter-section default |
| `space-12` | 80 | Section gap same-bg, section padding Y |
| `space-16` | 240 | Band transition |

**Factory rule:** same-bg = **single boundary only** (not top+bottom double stack).

**Authority:** v3 §6.2 · [frontend-section-spacing-rule-v1.md](../../../projects/mars-website-factory/frontend-section-spacing-rule-v1.md)

**⚠ Rank-1 vs Rank-2:** 16px, 24px, 12px, 8px, 32px **есть в v3**, но **не на OL-01 scale** — см. §7 и Exception Registry.

### 4.4 Radius

| Token | Value | Usage |
|-------|-------|-------|
| `radius-default` | **30px** | Buttons, cards, panels, FAQ |
| `radius-control` | **10px** | Inputs, textarea, select only |
| `radius-pill` | **999px** | Circular avatars, pills |
| `radius-none` | 0 | Full-bleed flush edges |

**Deprecated:** 4/8/12/16/24 px radius scale — **do not use**.

### 4.5 Colors (coordinator-confirmed core)

| Token | Value |
|-------|-------|
| `color-text-primary` | `#475371` |
| `color-primary-accent` | `#B3261E` |
| `color-bg-base` | `#FFFFFF` |
| `color-bg-page` | `rgba(218, 229, 240, 0.7)` over white |

Elevated/border/footer — engineering fallbacks in v3 §5.2.

### 4.6 Layout

| Rule | Value |
|------|-------|
| Card grids | 3 or 4 col desktop; 1 col mobile; **gap 24px** |
| Form fields | 2 col desktop → 1 col mobile; **gap 16px** |
| Article desktop | TOC **280px** + `1fr` (placeholder) |
| Wide sections | Background 100vw; inner content in container |

### 4.7 Desktop-first

| Rule | Value |
|------|-------|
| Methodology | **Desktop-first** |
| Layout switch | **`min-width: 1024px`** desktop · **`max-width: 1023px`** mobile |
| Tablet 768–1023 | **Mobile layout** (no separate tablet artboard) |
| Min viewport | **320px** |

**Authority:** v3 §9 · [FP-0002-FRONTEND-START-SEQUENCE-v1.md](FP-0002-FRONTEND-START-SEQUENCE-v1.md)

---

## 5. Operator Laws Summary

**Authority:** [frontend-production-authority-order-v1.md](../../../projects/mars-website-factory/frontend-production-authority-order-v1.md) §3

Кратко — **только действие**.

| Law | Action |
|-----|--------|
| **OL-01 Spacing Scale** | **Gap** only: 5 · 10 · 20 · 30 · 40 · 50 · 70 px. **Margin/padding** only: 5 · 10 · 15 · 20 · 25 · 30 · 40 · 50 · 70 · 90 px. Map design to **nearest** — no arbitrary values. |
| **OL-02 Percentage Padding** | Allowed: 5% · 10% · 15% · 20% · 30% — large volumetric containers only. **Not** grid column splits. |
| **OL-03 Layout Pattern First** | Name LP-* / WF zone → apply pattern → place content. **Forbidden:** layout by eye. |
| **OL-04 No Arbitrary Grid Splits** | **Forbidden:** 65/35, 70/30, 60/40 % splits. Use `fr`, `minmax`, `repeat`, approved LP-*. |
| **OL-05 Typography Precision** | Default: `line-height = font-size + 4px`. **Project SSOT named tiers win** when both define same token. |
| **OL-06 No Word Breaking** | **Forbidden:** `letter-spacing`, `word-break`, `overflow-wrap`, `hyphens` — **any value**; property presence in CSS = FAIL — unless direct operator instruction + Exception Registry. |
| **OL-07 Russian HTML Typography** | Typograph headings/body/buttons/links/cards/forms. **Do not typograph:** meta, code, class names, URLs, JSON-LD. |

---

## 6. Mapping Rules

**Authority:** [design-source-to-frontend-mapping-governance-v1.md](../../../projects/mars-website-factory/design-source-to-frontend-mapping-governance-v1.md) · [FP-0002-DESIGN-FRONTEND-MAPPING-QA-RECORD-v1.md](FP-0002-DESIGN-FRONTEND-MAPPING-QA-RECORD-v1.md)

### 6.1 Правильный перенос

| Rule | Behavior |
|------|----------|
| **Measure first, normalize second** | Raw px from PDF → record → map to OL-01 or rank-1 token with PD/C-12 citation |
| **Mandatory chain** | Design Source → WF-GRID → WF-LAYOUT → LP-* → HTML — **no Design→HTML shortcut** |
| **1:1 typography transfer default** | Observed sizes enter type table before normalization |
| **Rank-1 after Approval** | Implementation follows **v3**, not raw PDF numbers |
| **Eight layers L-01–L-08** | All attempted; absent = UNKNOWN, not blank |
| **Documented deltas** | Olga/coordinator overrides (1170, 18px body, 30px radius) — in PD-01…PD-17 |

### 6.2 Дрейф (forbidden)

| Drift type | Examples |
|------------|----------|
| **Aesthetic override** | «Looks cleaner / modern / better» |
| **Agent resizing** | Change type sizes for hierarchy balance |
| **Silent spacing** | Invent px not in SSOT or OL scale |
| **Design→HTML shortcut** | Skip WF-GRID / WF-LAYOUT / LP-* |
| **Invented states** | Hover/active not in source without C-10 policy |
| **Invented mobile** | Mobile layout when source absent |
| **Placeholder assets in SSOT** | Fake logos/icons without HITL |

**Authority:** mapping-governance §6 · [beautification-drift-governance.md](../../../projects/mars-website-factory/beautification-drift-governance.md)

### 6.3 UNKNOWN policy

| Situation | Required action |
|-----------|-----------------|
| Source silent | **SAFE UNKNOWN** — no production guess |
| Missing mobile artboard | Mark responsive UNKNOWN; desktop-first proceed where allowed |
| Missing hover/focus | C-10 UNKNOWN or Factory default **with Lead ack** |
| Missing asset | L-07 blocker or TBD — not SVG/CSS fake |
| Cannot cite rank 1–5 | **STOP** — HITL |

**Authority:** mapping-governance §7 · v3 §15 SAFE UNKNOWN register

### 6.4 FP-0002 Mapping QA status

**DESIGN → FRONTEND MAPPING QA — PASS WITH NOTES**

Written exceptions: LP-* IDs not in v3; L-07 assets UNKNOWN; procedural retroactive timing. **Does not block M2** at token-scaffold level.

---

## 7. M2 Implementation Rules

**M2 = Foundation production pass** — Charter Phases 1–7 / Start Sequence Steps 1–7. **Not** Home page.

**Authority:** [FP-0002-FRONTEND-START-SEQUENCE-v1.md](FP-0002-FRONTEND-START-SEQUENCE-v1.md) · [FP-0002-FRONTEND-PRODUCTION-CHARTER-v1.md](FP-0002-FRONTEND-PRODUCTION-CHARTER-v1.md) §13 · [frontend-shell-first-start-protocol-v1.md](../../../projects/mars-website-factory/frontend-shell-first-start-protocol-v1.md)

### 7.1 M2 MUST

| # | Rule |
|---|------|
| M-MUST-01 | Await **operator authorization** + **new M2 spec** under post-audit governance before coding |
| M-MUST-02 | Use **`ui-demo.html`** as foundation entry — **not** `index.html` / Home |
| M-MUST-03 | Implement Start Sequence Steps **1→7 in order** |
| M-MUST-04 | Wire **all v3 tokens** from SSOT — container 1170, padding 40/20, Inter, colors, radius 30/10/999 |
| M-MUST-05 | **Desktop-first** CSS — `min-width: 1024px` for grid activation |
| M-MUST-06 | Build shell: header (BLK-001+002) + main + footer (BLK-003) before page complexity |
| M-MUST-07 | Render **Visual Foundation Contract** categories on demo URL inside `main` |
| M-MUST-08 | Run **Design Calibration** with **COMPILED CSS SPOT-CHECK** on `dist/*.css` before Foundation QA |
| M-MUST-09 | Inspect **`src/scss/**` AND `dist/*.css` AND `dist/**/*.html`** for every enforcement gate |
| M-MUST-10 | Record **Exception Registry** for **every** rank-1 value that violates OL-01 **before** claiming WAIVED or PASS on EG-01/02/04 |
| M-MUST-11 | Run full **Compliance Decision Model** route (Detection → Gate Verdict) — **never FAIL at detection** |
| M-MUST-12 | Emit **ROOT COMPLIANCE — PASS** only when EG-01–04 satisfied |
| M-MUST-13 | File `# REPORT — FP-0002 foundation QA` with Layer A gate lines per reporting standard |
| M-MUST-14 | **STOP for Lead approval** after each production slice |
| M-MUST-15 | Edit **`src/` only** — never hand-edit `dist/` |
| M-MUST-16 | Follow layout chain: WF-GRID → WF-LAYOUT → LP-* (infer from Normalization §6 + v3 §3 if LP IDs absent) |
| M-MUST-17 | Apply RU typography law — typograph HTML; fix overflow via layout not word-break |
| M-MUST-18 | Show spacing demo labels: same-bg 80px, band 240px, mobile 64px |

### 7.2 M2 MUST NOT

| # | Rule |
|---|------|
| M-MUST-NOT-01 | **Start Home (PG-001)** or BLK-007/009/010 before Foundation QA PASS |
| M-MUST-NOT-02 | **Create `index.html`** as Home before Phase 7 |
| M-MUST-NOT-03 | Use **mobile-first** base styles without Lead approval |
| M-MUST-NOT-04 | Use **deprecated radius** 4/8/12/16/24 px scale |
| M-MUST-NOT-05 | Declare **`letter-spacing` / `word-break` / `overflow-wrap` / `hyphens`** in CSS (any value) |
| M-MUST-NOT-06 | **Invent spacing** for «visual improvement» — every px cites v3 token or OL scale |
| M-MUST-NOT-07 | Use **arbitrary grid % splits** (65/35, etc.) |
| M-MUST-NOT-08 | **Validate source SCSS only** — compiled CSS inspection **mandatory** |
| M-MUST-NOT-09 | Emit **PASS / PRODUCTION PASS** without **ROOT COMPLIANCE — PASS** |
| M-MUST-NOT-10 | Treat **rank-1 permit as auto-WAIVED OL** without complete Exception Registry |
| M-MUST-NOT-11 | Treat **rank-1 silence as permission** for off-scale values |
| M-MUST-NOT-12 | **Modify** Page Inventory, Block Inventory, WordPress/ACF architecture |
| M-MUST-NOT-13 | **Reuse** destroyed first-pass M2 spec (`FP-0002-M2-FOUNDATION-DEMO-SPEC-v1.md`) as authority |
| M-MUST-NOT-14 | Change production tokens without ADR + new SSOT version |
| M-MUST-NOT-15 | Skip **Design Calibration** and go straight to Foundation QA PASS claim |
| M-MUST-NOT-16 | Use **inline `style=""`** outside allowlist |
| M-MUST-NOT-17 | Infer inter-section gaps from one PDF block — use v3 §6.2 tokens only |

### 7.3 Things That Already Failed Once

Реальные ошибки первого M2 прохода (FP-0002 M2 ROOT CAUSE AUDIT + historical validation).

**Authority:** [website-factory-enforcement-pack-v1.md](../../../projects/mars-website-factory/website-factory-enforcement-pack-v1.md) §1 · Foundation Historical Failure Validation (2026-06-14) · M2 Demo Spec (removed — provenance only)

| Failure | What happened | Correct action for new M2 |
|---------|---------------|---------------------------|
| **`gap: 16px` in compiled CSS** | Passed review — not on OL-01 gap scale | Inspect `dist/*.css`; CASE B → FAIL without Exception Registry |
| **`grid-gap` / `column-gap: 16px`** | Same | EG-02 mandatory |
| **`gap: 24px` (card grids)** | SSOT permits (`space-6`) but OL-01 gap scale excludes 24 | Exception Registry **before** WAIVED |
| **`margin-bottom: 24px`** | Off OL-01 margin scale | Map or register exception |
| **`padding: 24px` (cards)** | Rank-1 permits; OL conflict unregistered | Exception Registry |
| **`padding: 16px` (inputs)** | Rank-1 permits; OL conflict unregistered | Exception Registry |
| **`padding: 12px`** | Not on OL-01; rank-1 silent | CASE D → FAIL — map to 10 or 15 |
| **`gap: 8px` / `margin-bottom: 8px`** | Not on OL-01 | CASE D → FAIL — map to 5 or 10 |
| **`gap: 32px`** | Not on OL-01 gap scale; weak SSOT token naming | Map to 30 or 40, or register |
| **No Exception Registry** | Rank-1/OL conflicts treated as implicit PASS | Complete §6 fields per authority-order |
| **Source-only validation** | SCSS looked compliant; compiled CSS had violations | **COMPILED CSS SPOT-CHECK** at Calibration §5.7 |
| **Foundation QA PASS without ROOT COMPLIANCE** | Structural checks green; enforcement gaps hidden | EG-05 blocks PASS |
| **False PASS on token presence** | Tokens declared in source; wrong values in output | DQ-02a **and** DQ-02b separate checks |
| **Authority conflict not resolved** | v3 4px-base scale vs OL-01 scale — silent coexistence | AUTHORITY CONFLICT STATUS gate |

---

## 8. Enforcement Rules

**Authority:** [website-factory-enforcement-pack-v1.md](../../../projects/mars-website-factory/website-factory-enforcement-pack-v1.md)

### 8.1 Gates EG-01 – EG-05

| Gate | Question | Sources (both when build green) |
|------|----------|--------------------------------|
| **EG-01** Operator Law Compliance | OL-01–OL-07 obeyed unless valid rank-1 exception? | `src/scss/**` + `dist/*.css` |
| **EG-02** Compiled CSS Compliance | Compiled output matches OL + SSOT? | **`dist/*.css`** primary — **not substitutable** by source review |
| **EG-03** Inline Style Compliance | Inline `style=""` outside allowlist? | `dist/**/*.html` + `src/**/*.html` |
| **EG-04** Authority Conflict Status | Rank-1 vs rank-2 resolved with Exception Registry? | SSOT diff vs OL |
| **EG-05** ROOT COMPLIANCE | Full evidence chain complete? | Rollup of EG-01–04 + source review |

**Verdict vocabulary:** PASS · PASS WITH NOTES · FAIL · **WAIVED** (enforcement gates only) · UNKNOWN

### 8.2 ROOT COMPLIANCE (mandatory)

**Hard rule:** Foundation QA PASS or **FINAL VERDICT — PRODUCTION PASS** is **impossible** when:

- ROOT COMPLIANCE — **FAIL** or **UNKNOWN**
- Any EG-01–04 — **FAIL** (without approved waiver path)

| Sub-check | Blocks ROOT PASS if |
|-----------|---------------------|
| Source SCSS/HTML | Not reviewed when build green |
| Compiled CSS | EG-02 FAIL or UNKNOWN |
| Compiled HTML | EG-03 FAIL or UNKNOWN |
| Authority conflicts | EG-04 FAIL or UNKNOWN |
| Exception registry | Any conflict lacks mandatory fields |

### 8.3 Exception Registry (before WAIVED)

**Mandatory fields — missing any → FAIL, not WAIVED:**

| Field | Content |
|-------|---------|
| decision id | e.g. `C-12-EX-001` or PD row |
| owner | Named Lead / Frontend Lead |
| justification | Why rank-1 value required |
| authority citation | `Rank 1: FP-0002 v3 §…` overriding `Rank 2: OL-0N` |

**Storage:** v3 §12 Production Decisions extension, change-control appendix, or QA REPORT Exception Registry subsection.

**Authority:** authority-order §6 · enforcement-pack §4

---

## 9. Compliance Decision Rules

**Authority:** [frontend-compliance-decision-model-v1.md](../../../projects/mars-website-factory/frontend-compliance-decision-model-v1.md)

**Core principle:** **RAW VIOLATION ≠ FAIL.** FAIL only after full 6-stage route.

### 9.1 Route (summary)

```text
1. Detection        → RAW VIOLATION (no verdict)
2. Classification   → rank_1 / rank_2 / allowlist / evidence gap
3. Authority Resolution
4. Exception Resolution
5. Compliance Verdict → first FAIL/WAIVED/PASS here
6. Gate Verdict     → EG-01…EG-05 lines
```

### 9.2 CASE A–F summary

| Case | Situation | Compliance Verdict |
|------|-----------|-------------------|
| **A** | Violates **Rank 1 and Rank 2** | **FAIL** — registry cannot repair SSOT breach |
| **B** | Rank 1 **permits**; Rank 2 conflict; **no** Exception Registry | **FAIL** |
| **C** | Rank 1 permits; Rank 2 conflict; **complete** Exception Registry | **WAIVED** |
| **D** | Rank 2 violation only; Rank 1 **silent** | **FAIL** — silence ≠ permission |
| **E** | Build failed / evidence incomplete | **UNKNOWN** |
| **F** | No violations | **PASS** |

**FP-0002 critical pattern:** v3 tokens 16px/24px = **CASE B** unless Exception Registry complete — **not** CASE F.

---

## 10. Failure Attribution Rules

**Authority:** [frontend-failure-attribution-model-v1.md](../../../projects/mars-website-factory/frontend-failure-attribution-model-v1.md)

**When to run:** After confirmed defect escaped a gate — post-hoc audit, rollback review, downstream QA finding.

### 10.1 Route (summary)

```text
1. Detection           → confirmed finding (FAILURE EVENT)
2. Authority Analysis  → cite OL / SSOT / EG / DQ
3. Expected Capture Point → earliest gate obligated to stop it
4. Failure Cause       → why gate did not stop
5. Attribution Verdict → gate owner (not code author)
```

### 10.2 Failure causes

| Cause | Meaning |
|-------|---------|
| **CHECK NOT EXECUTED** | Gate skipped or absent from REPORT |
| **CHECK EXECUTED INCORRECTLY** | Wrong evidence — e.g. source only, not `dist/*.css` |
| **AUTHORITY NOT CONSULTED** | OL scale / authority order not applied |
| **EXCEPTION NOT VERIFIED** | Rank-1 permit assumed; registry not checked |
| **REPORT DRIFT** | Gate PASS contradicted by later evidence |
| **UNKNOWN** | Insufficient REPORT history |

### 10.3 FP-0002 historical attribution (first M2)

| Violation class | Expected Capture Point | Primary Failure Cause | Attribution |
|-----------------|------------------------|----------------------|-------------|
| OL spacing in compiled CSS | Design Calibration §5.7 → EG-02 | CHECK EXECUTED INCORRECTLY | **Design Calibration** |
| Rank-1/OL without registry | Foundation QA §6.16 → EG-04 | EXCEPTION NOT VERIFIED | **Foundation QA** |
| ROOT PASS with bad sub-gates | Foundation QA §6.17 → EG-05 | REPORT DRIFT | **Foundation QA** |

---

## 11. M2 Readiness Checklist

Перед началом M2 coding. **Yes/No.**

| # | Criterion | Y/N |
|---|-----------|-----|
| R-01 | Production Standards v3 **APPROVED WITH ANDREY CORRECTIONS** | ☐ |
| R-02 | Charter v1 **ISSUED** | ☐ |
| R-03 | Mapping QA **PASS WITH NOTES** recorded | ☐ |
| R-04 | PRE-M2 frontend restored — M1 scaffold only, no M2 artifacts | ☐ |
| R-05 | Operator **authorization** for new M2 pass received | ☐ |
| R-06 | **New M2 spec** drafted under post-audit governance (not destroyed v1 spec) | ☐ |
| R-07 | Agent read **this Execution Brain** + cited rank-1 SSOT | ☐ |
| R-08 | Agent understands **rank-1 vs OL-01 conflict** requires Exception Registry | ☐ |
| R-09 | Agent understands **compiled CSS inspection** is mandatory | ☐ |
| R-10 | Design pack available locally (`INCOMING/01_DESIGN/` per reset) | ☐ |
| R-11 | Frontend workspace path confirmed: `workspaces/fp-0002-shpigovsky-frontend/` | ☐ |
| R-12 | **Home page work explicitly forbidden** until Phase 7 | ☐ |

**M2 Readiness PASS:** R-01–R-04 **Yes** + R-05–R-06 **Yes** (operator) + R-07–R-12 **Yes**.

**Note:** R-05/R-06 are **operator gates** — agent must not self-authorize M2 start.

**Authority:** [REPORTS/FP-0002-RESET-COMPLETE.md](REPORTS/FP-0002-RESET-COMPLETE.md) §6

---

## 12. M2 Completion Checklist

Перед входом в **Design Calibration** close-out and **Foundation QA**. **Yes/No.**

| # | Criterion | Y/N |
|---|-----------|-----|
| C-01 | Start Sequence Steps **1–6** complete (shell through mobile) | ☐ |
| C-02 | `npm run build` succeeds | ☐ |
| C-03 | `dist/ui-demo.html` exists — **no** Home in `dist/` | ☐ |
| C-04 | Visual Foundation Contract §3 categories visible on demo URL | ☐ |
| C-05 | No BLK-007 / PG-001 blocks in codebase | ☐ |
| C-06 | Token spot-check: 1170 · 40/20 · 30/10/999 · Inter · v3 colors | ☐ |
| C-07 | Section spacing demo labels present (80 / 240 / 64 mobile) | ☐ |
| C-08 | RU typography law respected — no forbidden properties | ☐ |
| C-09 | WF-GRID discipline — section ≠ container | ☐ |
| C-10 | WF-LAYOUT discipline — no default `%` splits | ☐ |
| C-11 | **Design Calibration** executed incl. **COMPILED CSS SPOT-CHECK** | ☐ |
| C-12 | EG-01 Operator Law — source + compiled — verdict recorded | ☐ |
| C-13 | EG-02 Compiled CSS — `dist/*.css` inspected — verdict recorded | ☐ |
| C-14 | EG-03 Inline Style — HTML inspected — verdict recorded | ☐ |
| C-15 | EG-04 Authority Conflict — registry complete or PASS — verdict recorded | ☐ |
| C-16 | EG-05 ROOT COMPLIANCE — **PASS** | ☐ |
| C-17 | Compliance Decision Model block in REPORT | ☐ |
| C-18 | `# REPORT — FP-0002 foundation QA` filed | ☐ |
| C-19 | Lead acknowledgment on Foundation QA | ☐ |

**M2 Completion PASS:** All C-01–C-19 **Yes**. C-16 **must be Yes** — no waiver on ROOT COMPLIANCE.

**Authority:** [frontend-foundation-qa-governance-v1.md](../../../projects/mars-website-factory/frontend-foundation-qa-governance-v1.md) §5.2 · Charter §12 G-01–G-15

---

## 13. Forbidden Behaviors

Свод **всех запретов** для M2 агента. Каждый пункт traceable to authority.

| # | Forbidden | Authority |
|---|-----------|-----------|
| F-01 | **Agent preference** as override | authority-order rank 6 |
| F-02 | **Cleaner look / modern look / visual improvement** rationale | mapping-governance §6 · beautification-drift |
| F-03 | **Spacing beautification** — invent px for aesthetics | OL-01 · precision-governance §1 |
| F-04 | **Unapproved line-height** — unitless ratios hiding px cadence | OL-05 · PF-01 |
| F-05 | **Arbitrary grid split** — 65/35, 70/30, eyeball columns | OL-04 |
| F-06 | **Source-only validation** — skip `dist/*.css` | enforcement-pack §3.2 · calibration §5.7 |
| F-07 | **PASS without ROOT COMPLIANCE** | enforcement-pack §6 |
| F-08 | **FAIL at detection time** — skip Compliance Decision route | compliance-decision-model §1 |
| F-09 | **Rank-1 permit = auto-WAIVED OL** without registry | compliance-decision-model CASE B |
| F-10 | **Rank-1 silence = permission** | compliance-decision-model CASE D |
| F-11 | **Mobile-first** base without Lead approval | v3 §9 · charter §7 |
| F-12 | **`letter-spacing` / `word-break` / `overflow-wrap` / `hyphens`** in source or compiled CSS (any value) | v3 §4.3 PD-14/15 · OL-06 |
| F-13 | **Home / index.html / BLK-007** before Foundation QA | charter SC-01/02 · start-sequence step 8 gate |
| F-14 | **Design→HTML shortcut** — skip WF-GRID/LAYOUT/LP | mapping-governance §4.1 |
| F-15 | **Manual `dist/` edits** | charter · production-rules source-first |
| F-16 | **Deprecated radius scale** 4/8/12/16/24 | v3 §7 |
| F-17 | **Infer section gaps from one PDF block** | v3 §6.2 · section-spacing-rule |
| F-18 | **Invent hover/focus/active** without source or C-10 policy | mapping-governance §7 |
| F-19 | **Modify Page/Block Inventory** without charter | charter SC-07 |
| F-20 | **Reuse destroyed M2 spec** as authority | reset-complete §3 |
| F-21 | **Token drift without ADR** | charter §3.2 |
| F-22 | **Inline styles** outside allowlist | enforcement-pack EG-03 |
| F-23 | **Claim PASS on DQ-02a alone** — ignore DQ-02b Operator Law | design-qa-matrix DQ-02a/b |
| F-24 | **Skip Design Calibration** before Foundation QA | shell-first Phase 4b |
| F-25 | **Blame implementer** in attribution instead of failed gate | failure-attribution-model §7 |

---

## 14. One Page Execution Summary

**Если прочитать только этот раздел** — минимум для FP-0002 M2.

### What M2 is

Foundation production: **`ui-demo.html`** shell + typography/UI demo + header/footer desktop/mobile + global v3 tokens → Design Calibration → Foundation QA. **Not Home.**

### Authority in one line

**v3 SSOT (rank 1) → OL-01–07 (rank 2) → Factory gates (rank 3).** Agent preference never wins.

### Numbers that matter

1170 container · 40/20 padding · Inter · 30/10/999 radius · desktop-first @1024 · H2 36/22 w500 · body 18/16 w300 · card gap 24 · section gap 80 single-boundary.

### The trap that killed first M2

v3 **allows** 16px and 24px as project tokens — OL-01 **does not**. Implementing v3 values without **Exception Registry** → **CASE B → FAIL** under current Enforcement. First pass got **false PASS** because QA checked **source SCSS**, not **`dist/*.css`**, and skipped registry.

### Execution sequence

1. Confirm operator auth + new M2 spec  
2. Wire v3 tokens in `src/scss` (M1 placeholder → production)  
3. Steps 1–6 Start Sequence — shell → demo → header/footer → globals → mobile  
4. `npm run build`  
5. Design Calibration + **COMPILED CSS SPOT-CHECK** on `dist/*.css`  
6. Complete Exception Registry for all rank-1/OL conflicts **or** map to OL nearest with Lead record  
7. Run EG-01–05 → Compliance Decision Model → ROOT COMPLIANCE **PASS**  
8. File Foundation QA REPORT + Lead ack  
9. **Only then** — Home (Phase 8) with separate charter slice  

### Stop conditions

- No ROOT COMPLIANCE PASS → **no Foundation QA PASS**  
- No Foundation QA PASS → **no Home**  
- Any forbidden property detected → remove before continue  
- Cannot cite authority for a value → **STOP HITL**  

### Evidence rule

**Green build + green source ≠ PASS.** Inspect compiled CSS and HTML every gate cycle.

---

## LESSONS LEARNED FROM FIRST M2 FAILURE

| # | Lesson | Evidence source | Required behavior in new M2 |
|---|--------|-----------------|------------------------------|
| L-01 | Foundation could PASS on **structure + token presence** while **compiled CSS violated OL** | enforcement-pack §1 provenance | EG-02 mandatory on `dist/*.css` |
| L-02 | **`gap: 16px`** in compiled output — historical flagship violation | failure-attribution CASE A/C · historical validation V-01 | Inspect compiled; CASE B without registry = FAIL |
| L-03 | **`margin-bottom: 24px`** and **`padding: 24px`** off OL-01 margin scale | historical validation V-03–V-05 | Separate margin/padding OL check |
| L-04 | **`padding: 12px`**, **`gap: 8px`**, **`gap: 32px`** — rank-1 silent off-scale | historical validation V-07–V-09 | CASE D — map to OL or STOP |
| L-05 | **Rank-1 SSOT permit ≠ OL auto-waive** — 16px/24px are CASE B, not PASS | compliance-decision-model CASE B | Exception Registry before WAIVED |
| L-06 | **Exception Registry absent** — implicit rank-1 win treated as PASS | authority-order §6 · enforcement-pack §4 | 4 mandatory fields per conflict |
| L-07 | **Source-only SCSS review** masked compiled violations | failure-attribution CHECK EXECUTED INCORRECTLY | Calibration §5.7 COMPILED CSS SPOT-CHECK |
| L-08 | **ROOT COMPLIANCE PASS** claimed without sub-gate evidence | enforcement-pack §6 · historical validation rollup | EG-05 blocks PASS |
| L-09 | **DQ-02a SSOT PASS** did not imply **DQ-02b OL PASS** | design-qa-matrix DQ-02a/b split | Run both checks independently |
| L-10 | **Design Calibration** was Expected Capture Point for spacing escapes | failure-attribution-model §4 | First compiled CSS gate in chain |
| L-11 | **AUTHORITY CONFLICT STATUS** not verified at Foundation QA | historical validation secondary attribution | EG-04 mandatory |
| L-12 | **False PASS** cheaper to prevent at Calibration than fix at Home | shell-first gap 2026-06-14 | No Home until Phase 7 |
| L-13 | First M2 spec **`FP-0002-M2-FOUNDATION-DEMO-SPEC-v1.md`** invalidated — do not reuse | reset-complete §3 | New spec under post-audit governance |
| L-14 | **RAW VIOLATION emitted as FAIL** caused verdict drift | compliance-decision-model §1 | Full 6-stage route always |
| L-15 | **Aesthetic/agent spacing habits** (16/24 as «nice numbers») conflict with OL even when v3 names them | precision-governance · OL-01 | Document every rank-1/OL delta explicitly |

**Evidence boundary (UNKNOWN):** Archived M2 QA REPORT with literal `dist/*.css` grep **not found in repo**. Lessons L-02–L-04 reconstructed from Enforcement Pack provenance + historical validation simulation + removed M2 Demo Spec references. Logic is **documented**, not re-run on live M2 code.

---

## Document control

| Field | Value |
|-------|-------|
| Version | **v1** |
| Created | 2026-06-14 |
| Type | Aggregation layer only |
| Modifies authority | **No** |
| Commit / push | Not performed |

---

*Execution Brain only. No code. No M2 implementation. No frontend changes.*
