# REPORT — SITE-001 WF-V3 Website Factory Compliance Audit v1

**Type:** Read-only compliance audit — **no fixes, no code changes**  
**Date:** 2026-06-14  
**Site:** SITE-001 — Автосалон СИБКАР  
**Workspace audited:** `workspaces/site-001-wf-v3/`  
**Restore point (pre-audit):** `wf-v3-pre-standardization-2026-06-14`  
**Auditor mode:** Maximum strictness — Factory rules v2026-06 treated as mandatory gate, not advisory

**Scope:** Website Factory frontend quality only. **Excluded:** OpenCart, SEO, content, banks (content/assets), photography, maps, CRM.

**Rule sources (canonical):**

| Layer | Document |
|-------|----------|
| WF-GRID | [WF-GRID-DISCIPLINE-v1.md](../../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) |
| WF-LAYOUT | [WF-LAYOUT-DISCIPLINE-v1.md](../../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) |
| Frontend Production | [frontend-production-rules-v0.md](../../../projects/mars-website-factory/frontend-production-rules-v0.md) |
| Invariants | [frontend-production-invariants-v1.md](../../../projects/mars-website-factory/frontend-production-invariants-v1.md) |
| Precision / Typography / Spacing | [frontend-precision-governance-v1.md](../../../projects/mars-website-factory/frontend-precision-governance-v1.md), [frontend-section-spacing-rule-v1.md](../../../projects/mars-website-factory/frontend-section-spacing-rule-v1.md), [typography-rhythm-governance.md](../../../projects/mars-website-factory/typography-rhythm-governance.md) |
| Design System | [DESIGN-SYSTEM-RULES-v1.md](../../../workspaces/website-factory-reference-v1/design-system/DESIGN-SYSTEM-RULES-v1.md) |
| Page / Block / Blueprint | [PAGE-IMPLEMENTATION-RULES-v1.md](../../../workspaces/website-factory-reference-v1/page-architecture/PAGE-IMPLEMENTATION-RULES-v1.md), [BLOCK-IMPLEMENTATION-RULES-v1.md](../../../workspaces/website-factory-reference-v1/block-registry/BLOCK-IMPLEMENTATION-RULES-v1.md), [BLUEPRINT-IMPLEMENTATION-RULES-v1.md](../../../workspaces/website-factory-reference-v1/blueprints/BLUEPRINT-IMPLEMENTATION-RULES-v1.md) |
| Production QA / Gulp QA | [PRODUCTION-QA-CHECKLIST-v1.md](../../../workspaces/website-factory-reference-v1/production-qa/PRODUCTION-QA-CHECKLIST-v1.md), [qa-checklist.md](../../../agents/frontend-gulp-agent/qa-checklist.md) |
| Project grid charter | [CONTAINER-GRID-DISCIPLINE-v1.md](../../../workspaces/site-001-wf-v3/docs/CONTAINER-GRID-DISCIPLINE-v1.md) |

**Build verification (this audit):** `npm run build` in `workspaces/site-001-wf-v3/` — **PASS** (exit 0; Sass `legacy-js-api` deprecation warning only).

**Visual alignment (WF-GRID-005):** **SAFE UNKNOWN** — pixel alignment at 1280/375 not re-run in this audit; structural DOM/SCSS evidence only.

---

## Executive summary

Unified workspace `site-001-wf-v3` — **сильный layout-прототип** после консолидации трёх поверхностей и прошлых WF-GRID / WF-LAYOUT итераций (hero, trust, credit, featured). **Container Layer** в HTML приведён к канону.

**Однако** проект **не соответствует** полному Factory stack v2026-06 как **эталон**:

- Нет **Project Production Standards** (Draft → Approval) — обязательный rank-1 SSOT.
- Нет **Foundation Demo Page**, **Design Calibration**, **Foundation QA REPORT** — shell-first gates пропущены.
- **Typography / Spacing / Components** системно расходятся с [frontend-precision-governance-v1.md](../../../projects/mars-website-factory/frontend-precision-governance-v1.md) и Operator Laws OL-01 / OL-05.
- **WF-LAYOUT** закрыт **не для всех зон** — banks, dealer-advantages, equipment, catalog shell без documented collapse; token drift в catalog layout.

**Standardization Pass сейчас заблокирован foundation-слоем**, не «косметикой».

---

## Итоговая таблица

| Блок | Вердикт | Кратко |
|------|---------|--------|
| **WF-GRID** | **PASS** | Section/container split корректен; единый контракт 1280/24 |
| **WF-LAYOUT** | **FAIL** | Часть зон без collapse authority; catalog token drift; banks/advantages/equipment |
| **Typography** | **FAIL** | Unitless line-height, letter-spacing, нет +4px law, нет SSOT type table |
| **Spacing** | **FAIL** | 4px-лadder ≠ Factory scale; нет mapped section-gap tokens |
| **Components** | **PARTIAL** | Кнопки/крошки OK; формы и badge/card — три параллельных системы |
| **Design System** | **PARTIAL** | Общий CSS/tokens, но cross-page drift controls и duplicated partial styles |
| **WF Readiness** | **NOT READY** | Не этalon WF v2026-06 |

### Финальный вердикт

## **B — Additional Foundation Work Required**

---

## Блок 1 — WF-GRID

**Вердикт: PASS**

### Что проверено

| Rule | Evidence | Status |
|------|----------|--------|
| WF-GRID-001 Section ≠ container | Все `<section>` / `<nav>` breadcrumbs / `<header>` / `<footer>` используют outer shell + inner `.wf-v3-container`. Контейнер **не** на корне section. Пример: `pdp-hero.html`, `header.html`, `featured-inventory.html` | **PASS** |
| WF-GRID-002 One page = one grid contract | `:root { --wf-v3-container-max: 1280px; --wf-v3-container-pad: 24px }` в `_utilities.scss`; SCSS tokens `$container-max` / `$container-pad` зеркалят значения | **PASS** |
| WF-GRID-003 Local width authority | `max-width: Nch` на subtitle/copy (`_homepage-hero.scss`, `_credit-block.scss`, `_financing-teaser.scss`) — задокументированы в [CONTAINER-GRID-DISCIPLINE-v1.md](../../../workspaces/site-001-wf-v3/docs/CONTAINER-GRID-DISCIPLINE-v1.md) как typography measure, не page grid | **PASS (documented)** |
| WF-GRID-004 Full-bleed | Section backgrounds / bands на outer layer; content в inner container | **PASS** |
| WF-GRID-005 QA alignment | Структурно header/hero/body/footer делят один wrapper-class. Pixel proof — **SAFE UNKNOWN** | **PASS (structural)** |

### Исключения / замечания (не FAIL)

| Item | Severity | Note |
|------|----------|------|
| `@media (max-width: 767px)` hardcoded в `_utilities.scss` | LOW | Дублирует `$mobile-max` из `_breakpoints.scss` — drift risk, не DOM violation |
| Catalog pagination `<nav>` без собственного container | INFO | Вложен в `.wf-v3-container` через `catalog-body.html` — grid authority сохранён |
| Legacy doc `docs/REPORT.md` всё ещь упоминает `65% / 35%` | LOW | **Documentation stale**; SCSS уже на `13fr / 7fr` — не runtime violation |

### Контейнеры — inventory

| Surface | Pattern |
|---------|---------|
| Header | `header` → band → `.wf-v3-container` ×2 (topbar + main) |
| Footer | `footer` → band → `.wf-v3-container` ×3 |
| Homepage / PDP / Catalog sections | `<section>` → `.wf-v3-container` |
| Breadcrumbs | `<nav>` → `.wf-v3-container` |

**WF GRID DISCIPLINE — PASS (structural; pixel QA SAFE UNKNOWN)**

---

## Блок 2 — WF-LAYOUT

**Вердикт: FAIL**

### PASS zones (documented authority)

| Zone | Type | File | Pattern |
|------|------|------|---------|
| PDP hero | L1 | `_pdp-hero.scss` | `13fr minmax(360px, 7fr)` + stack ≤1024px |
| Homepage hero | L2 | `_homepage-hero.scss` | `minmax(0, 7fr) minmax(480px, 5fr)` + search collapse |
| Trust strip | L5 | `_trust-row.scss` | `repeat(5, minmax(180px, 1fr))` + 2→1 col |
| Credit module | L4 | `_credit-block.scss` | `5fr 7fr` + stack ≤1024px; form 2→1 col ≤767px |
| Featured inventory | L3 | `_featured-inventory.scss` | `repeat(4, minmax(0, 1fr))` + documented N collapse |

### FAIL / NOT READY zones

| Zone | Violation | Rule | Evidence |
|------|-----------|------|----------|
| **Banks row** | `repeat(8, 1fr)` — no `minmax(0, 1fr)`; **no responsive collapse** | WF-LAYOUT-003, WF-LAYOUT-006 | `_banks.scss` L8–10 |
| **Dealer advantages** | `repeat(4, 1fr)` — no minmax floor; **no collapse** | WF-LAYOUT-003, WF-LAYOUT-006 | `_dealer-advantages.scss` L8–11 |
| **Equipment list** | `repeat(3, 1fr)` — desktop-only; **no collapse charter** | WF-LAYOUT-006 | `_equipment.scss` L7–11 |
| **Catalog body sidebar** | Local `$catalog-v02-sidebar-fr: 2fr` / `$catalog-v02-results-fr: 10fr` / `sidebar-min: 220px` **override** central tokens `$catalog-sidebar-fr: 3`, `$catalog-results-fr: 9`, `$catalog-sidebar-min: 260px` **without** `WF-LAYOUT-EXCEPTION` marker | WF-LAYOUT-008 | `_catalog-filters.scss` L4–6 vs `_tokens.scss` L71–74 |
| **Catalog results grid** | L3 `N=3` declared but **zero** `@include breakpoints` — no collapse | WF-LAYOUT-006 | `_catalog-results.scss` — full file |
| **Catalog body layout** | Sidebar + results shell — **no** `@media` collapse for sidebar stack | WF-LAYOUT-006 | `_catalog-filters.scss` `.wf-v3-catalog-body__layout` |
| **Header / footer chrome** | No responsive collapse for nav / footer grids | WF-LAYOUT-006 | `_header.scss`, `_footer.scss` — no breakpoint mixins |

### Hero / inventory / trust / finance — summary

| Area | Homepage | Catalog | PDP | Verdict |
|------|----------|---------|-----|---------|
| Hero | L2 PASS | N/A | L1 PASS | **PASS** |
| Inventory cards | L3 featured PASS | L3 results **no collapse** | N/A | **PARTIAL** |
| Trust | L5 PASS (shared `_trust-row.scss`) | L5 PASS (reuses trust-row) | L5 PASS | **PASS** |
| Finance | Teaser (simple band) | Teaser band | L4 credit PASS | **PARTIAL** (teasers not L4-modeled) |
| Responsive rules | Documented for hero/trust/featured | **SAFE UNKNOWN / missing** for catalog shell | Documented hero/trust/credit | **FAIL overall** |

### Percentage splits

SCSS **не** использует `%` tracks в hero (исправлено). **PASS** on WF-LAYOUT-007 for hero/credit.

**WF LAYOUT DISCIPLINE — FAIL** (banks, advantages, equipment, catalog shell/collapse, layout token drift)

---

## Блок 3 — Typography

**Вердикт: FAIL**

### Heading sizes & hierarchy

| Token | Value | Used for | Factory note |
|-------|-------|----------|--------------|
| `$font-size-display` | 38px | Homepage hero | OK as project token if SSOT-approved — **SSOT missing** |
| `$font-size-h1` | 30px | PDP title, catalog H1 | Hierarchy exists |
| `$font-size-h2` | 24px | Section titles | Consistent `.wf-v3-section-title` |
| `$font-size-h3` | 18px | Card titles, subheads | Consistent |
| `$font-size-body` | **15px** | Body default | **Not on Factory gap/type normalization scale** (expects px table + +4px LH) |

Logical heading order present on audited pages (single H1 per page in hero/heading blocks).

### Line-height / vertical rhythm

**Mandatory Factory rule:** `line-height = font-size + 4px` ([frontend-precision-governance-v1.md](../../../projects/mars-website-factory/frontend-precision-governance-v1.md) §3.1).

| Pattern | Occurrences | Verdict |
|---------|-------------|---------|
| `$line-height-body: 1.55` on 15px body | `_tokens.scss`, `_reset.scss` | **FAIL** — unitless ratio |
| `line-height: 1.2` on headings | `_utilities.scss`, `_pdp-hero.scss`, multiple sections | **FAIL** |
| `line-height: 1.05` / `1.1` / `1.15` on display | `_pdp-hero.scss`, `_credit-block.scss`, `_homepage-hero.scss` | **FAIL** — arbitrary decimals |
| Ad-hoc `14px` font in chips | `_catalog-chips.scss` L44 | **FAIL** — invented size |

### Letter-spacing

`$letter-spacing-tight: -0.02em`, `$letter-spacing-wide: 0.04em` and widespread `letter-spacing` on headings, labels, buttons — **forbidden default** per precision governance §4 unless named SSOT exception. **No exceptions documented.**

### Consistency

- Section title bar (`::before` 4×24px) — consistent pattern.
- Trust label vs body — two-tier type within strip — OK structurally.
- **No Production Standards type table** — cannot claim calibrated system.

**TYPOGRAPHY PRECISION (line-height = font-size + 4px) — FAIL**

---

## Блок 4 — Spacing System

**Вердикт: FAIL**

### Factory scale (OL-01 / precision §2)

**Required gap/margin/padding scale:** `5 · 10 · 20 · 30 · 40 · 50 · 70` (gaps) and `5 · 10 · 15 · 20 · 25 · 30 · 40 · 50 · 70 · 90` (margin/padding).

### Project scale (`_tokens.scss`)

**4px ladder:** `4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64 · 80` — **parallel system**, not mapped to Factory scale.

| Violation class | Examples |
|-----------------|----------|
| Non-scale values in active use | `$space-1: 4px`, `$space-2: 8px`, `$space-3: 12px`, `$space-7: 32px`, `$space-9: 48px`, `$space-10: 64px`, `$space-11: 80px` |
| Ad-hoc px | `padding: 2px` in `_inventory-card.scss`, `_catalog-chips.scss`, `_equipment.scss`; `margin-top: 1px` in `_trust-row.scss` |
| Section vertical padding unsystematic | Homepage hero `48px 0 64px`; featured `64px 0`; banks `64px 0 80px`; catalog heading `16px 0 20px` — **no** `section-gap-same-bg` / `section-gap-diff-bg` tokens |

### Section rhythm

| Check | Status |
|-------|--------|
| Same-bg single boundary rule | **Not mapped** — e.g. `benefits-row` (secondary bg + border) → `homepage-hero` (white) transition uses independent paddings |
| Diff-bg reset tokens | **Absent** from Production Standards |
| Mobile reduction rule | Partial — only where `@include breakpoints` exists; catalog/header/footer sections **not** covered |
| Global `section { padding }` anti-pattern | **Not present** — typed classes used |

**Project mapping requirement** ([frontend-section-spacing-rule-v1.md](../../../projects/mars-website-factory/frontend-section-spacing-rule-v1.md) §3): **MISSING** — no `section-gap-*` fields in approved SSOT.

---

## Блок 5 — Components

**Вердикт: PARTIAL**

### Buttons (`wf-v3-btn`)

| Check | Status |
|-------|--------|
| Primary / outline variants in `_utilities.scss` | **PASS** |
| Shared min-height baseline 46px | **PASS** |
| Credit submit `min-height: 50px` | **DRIFT** |
| Catalog filter submit uses small font, inherits 46px shell inconsistently | **PARTIAL** |
| Header CTA custom `padding-inline` / `min-width` | Acceptable component-internal |

### Cards (`wf-v3-inventory-card`)

| Check | Status |
|-------|--------|
| Shared partial markup catalog + featured | **PASS** |
| Base styles in `_inventory-card.scss` | **PASS** |
| **Duplicate** card block re-declared in `_featured-inventory.scss` L42+ | **FAIL consistency** |
| Catalog card density modifiers (`--catalog`) | **PASS** intent |

### Forms

| Context | Control height | Pattern |
|---------|----------------|---------|
| Homepage search | 46px | `.wf-v3-search__input` |
| Credit block | 48px | `.wf-v3-credit__input` |
| Catalog filters | 38px | `.wf-v3-catalog-filters__control` |

**Three parallel form systems** — no unified Factory form component. Labels: uppercase + letter-spacing in search/credit/catalog — inconsistent.

Credit form: submit button **inside** `<form>` — OK. Range slider present — OK for prototype.

### Badges

| Type | Location | Pattern |
|------|----------|---------|
| PDP hero badges | `.wf-v3-pdp-hero__badge` | Flex chip + icon |
| Inventory card badge | `.wf-v3-inventory-card__badge` | Absolute overlay, success color |

**No shared badge primitive** — two visual/semantic systems.

### Breadcrumbs

| Check | Status |
|-------|--------|
| Shared `.wf-v3-breadcrumbs` partial pattern | **PASS** |
| Container inside `<nav>` | **PASS** (WF-GRID) |
| PDP deep trail vs catalog shallow | **PASS** (content-appropriate) |
| Separator `>` character | Acceptable prototype |

---

## Блок 6 — Design System Consistency

**Вердикт: PARTIAL**

### Cross-surface matrix

| System element | Homepage | Catalog | PDP | Consistent? |
|----------------|----------|---------|-----|-------------|
| Container / tokens | ✓ | ✓ | ✓ | **YES** |
| Header / footer | shared partials | shared | shared | **YES** |
| Trust strip | `homepage-trust.html` | `catalog-trust.html` | `trust-row.html` | **HTML duplicated**; **SCSS shared** (`_trust-row.scss`) |
| Inventory card | featured grid | catalog grid | — | **SCSS duplicated** in featured |
| Search / filter forms | 4-col search | sidebar filters | — | **NO** — different heights, labels, density |
| Finance | financing-teaser | catalog-finance-teaser | credit-block L4 | **Three patterns** |
| Banks section | included | **absent** (by charter) | included | **Intentional IA gap** — breaks visual parity |
| Section title component | `.wf-v3-section-title` | catalog heading custom | PDP inline titles | **PARTIAL** |
| Breakpoints | 1024 / 767 | catalog layout desktop-only | 1024 / 767 on key zones | **NO** |

### Factory gates not satisfied

| Gate | Status |
|------|--------|
| Project Production Standards (Approved) | **MISSING** |
| Foundation Demo Page | **MISSING** |
| Design Calibration REPORT | **MISSING** |
| Foundation QA REPORT | **MISSING** |
| Layout Pattern Library charter for catalog sidebar | **Partial** — v0.2 comment only, conflicts with `_tokens.scss` |

Shared `main.css` proves **one build pipeline**, not **one design system**.

---

## Блок 7 — Website Factory Readiness

### Может ли проект считаться этalonной реализацией Website Factory v2026-06?

## **Нет — ещё не может.**

### Что уже этalon-grade (signal value)

1. **WF-GRID container discipline** — promoted rules originated here; consolidated HTML **implements** section/container split correctly.
2. **Core layout zones** — PDP L1 hero, Homepage L2 hero, L5 trust, L4 credit, L3 featured — **reference-quality** after layout conformance pass.
3. **Unified workspace** — single Gulp build, three pages, shared tokens file.
4. **Restore point** — `wf-v3-pre-standardization-2026-06-14` fixes defensible baseline.

### Что блокирует etalon status

| Blocker | Factory authority |
|---------|-------------------|
| No approved **Project Production Standards** | production-standards-governance-v1, shell-first protocol |
| Typography not on **+4px / px SSOT** | frontend-precision-governance-v1, OL-05 |
| Spacing not on **OL-01 scale** | frontend-precision-governance-v1, OL-01 |
| **WF-LAYOUT** incomplete on secondary zones | WF-LAYOUT-DISCIPLINE-v1 |
| **Component primitives** not normalized (forms, badges, cards) | frontend-visual-foundation-contract-v1 |
| **Foundation QA / Calibration** chain absent | frontend-foundation-qa-governance-v1 |
| Catalog responsive authority **SAFE UNKNOWN** | WF-LAYOUT-006, Gulp qa-checklist |
| Stale internal docs (`docs/REPORT.md` % hero) | Operator drift risk |

### Readiness class

| Class | Assessment |
|-------|------------|
| **Layout reference (partial)** | YES — hero/trust/credit/featured |
| **Grid reference** | YES — container layer |
| **Full Factory v2026-06 etalon** | **NO** |
| **Ready for Standardization Pass** | **NO** — verdict **B** |

---

## Production QA & Gulp Frontend Agent QA (structural)

| Checklist area | Result | Notes |
|----------------|--------|-------|
| Build / source-first | **PASS** | build exit 0; edits under `src/` |
| WF-GRID (qa-checklist) | **PASS (structural)** | Pixel matrix not re-run |
| WF-LAYOUT (qa-checklist) | **FAIL** | See Block 2 |
| RU typography / no word-splitting | **PARTIAL** | `&nbsp;` on numbers/units OK; no CSS word-break found; **no** ru-landing-qa-preset width run |
| Semantic HTML / landmarks | **PASS** | `<main>`, breadcrumbs `nav`, header/footer landmarks |
| Section consistency vs block registry | **NOT AUDITED** (architecture layer out of frontend-only scope partial) | Prototype charters exist under `projects/ocpilot/sites/site-001/governance/` |
| SAFE UNKNOWN items | Viewport meta `width=1440` / `1280` fixed — **responsive QA compromised** | homepage.html, catalog.html, pdp.html |

---

## Prior work vs current consolidated workspace

| Artifact | Claim | Audit note |
|----------|-------|------------|
| [SITE-001-WFV3-LAYOUT-CONFORMANCE-PASS-v1.md](SITE-001-WFV3-LAYOUT-CONFORMANCE-PASS-v1.md) | WF-LAYOUT PASS on **split prototypes** | Consolidated `site-001-wf-v3` inherits hero/trust/credit/featured fixes; **adds catalog** with new gaps |
| [CONTAINER-GRID-DISCIPLINE-v1.md](../../../workspaces/site-001-wf-v3/docs/CONTAINER-GRID-DISCIPLINE-v1.md) | Documents migration off container-on-section | **Verified** in current HTML |
| Restore point status | WF-GRID ACTIVE, WF-LAYOUT ACTIVE, standardization NOT STARTED | **Confirmed** by this audit |

---

## Recommended foundation sequence (audit-only — not executed)

Priority order for **B → A** transition:

1. **Draft + Approve Project Production Standards** — type table, spacing map, component heights, breakpoint SSOT.
2. **Normalize spacing tokens** to OL-01 scale (or document approved project override with decision IDs).
3. **Typography pass** — px line-heights (+4px rule), remove or charter letter-spacing.
4. **WF-LAYOUT closure** — banks, advantages, equipment, catalog shell/results collapse charters.
5. **Resolve catalog layout token drift** — single SSOT for sidebar fr/min or formal `WF-LAYOUT-EXCEPTION`.
6. **Component unification** — one form control spec, one badge spec, dedupe featured card SCSS.
7. **Foundation Demo + Calibration + Foundation QA REPORT** — then Standardization Pass.

---

## UNKNOWN / limits of this audit

| Item | Status |
|------|--------|
| Pixel grid alignment at 1280px / 375px | **SAFE UNKNOWN** — not browser-verified in this run |
| RU no-word-splitting at mandatory QA widths | **SAFE UNKNOWN** — CSS scan clean; preset not executed |
| OpenCart / SEO / content / bank assets | **Out of scope** per charter |
| Runtime / orchestration products | **Not claimed** — Gulp static prototype only |

---

## Git status (audit closeout)

Audit performed **read-only** on workspace + rule docs. Report file added under `projects/ocpilot/sites/site-001/reports/`. **No commit, no push.**

---

*SITE-001 WF-V3 Website Factory Compliance Audit v1 — documentation only; no code changes.*
