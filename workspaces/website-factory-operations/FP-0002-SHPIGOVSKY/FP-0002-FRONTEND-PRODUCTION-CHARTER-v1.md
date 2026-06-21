# FP-0002 — Frontend Production Charter v1

**Document type:** Frontend Production Charter — производственный контракт  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-13  
**Frontend Lead:** Андрей  

**ATLAS:** ORG-0008 · PRJ-0012 · WEB-SHPIG-01 · DOM-SHPIG-01  

**Назначение:** этот документ — **производственный контракт** Frontend Production для FP-0002. Это **не** техническое ТЗ, **не** Design System ради Design System, **не** WordPress/ACF Architecture.

**Upstream SSOT (read-only):**

| Input | Role |
|-------|------|
| [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) | Production SSOT — токены, layout, typography law |
| [FP-0002-FRONTEND-START-SEQUENCE-v1.md](FP-0002-FRONTEND-START-SEQUENCE-v1.md) | Обязательная последовательность foundation → Home |
| [FP-0002-FRONTEND-FOUNDATION-v1.md](FP-0002-FRONTEND-FOUNDATION-v1.md) | Layout/component taxonomy по PDF |
| [FP-0002-FRONTEND-NORMALIZATION-v1.md](FP-0002-FRONTEND-NORMALIZATION-v1.md) | Normalization pass (superseded по токенам v3) |
| [FP-0002-PAGE-INVENTORY-v1.md](FP-0002-PAGE-INVENTORY-v1.md) | 11 page types, Missing Pages Register |
| [FP-0002-BLOCK-INVENTORY-v1.md](FP-0002-BLOCK-INVENTORY-v1.md) | 40 Block ID, G-SERVICE, Home v2 composition |

**Factory protocols:**

| Rule | Document |
|------|----------|
| Shell-first start | [frontend-shell-first-start-protocol-v1.md](../../../projects/mars-website-factory/frontend-shell-first-start-protocol-v1.md) |
| Section spacing | [frontend-section-spacing-rule-v1.md](../../../projects/mars-website-factory/frontend-section-spacing-rule-v1.md) |
| RU typography | [russian-no-word-splitting-typography-v1.md](../../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md) |

**Git status (до работы):** ветка `mars/post-cycle8-live-tests`, up to date с `origin`. Папка `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/` — **untracked** (`??`). Commit / push **не выполнялись**.

**Scope charter:** фиксация производственного контракта. **Запрещено:** HTML, SCSS, JS, commit, push, изменение Page Inventory, Block Inventory, WordPress Architecture, ACF Architecture.

---

# REPORT — FP-0002 FRONTEND PRODUCTION CHARTER

## Executive Summary

Создан и оформлен **Frontend Production Charter v1** — производственный контракт статической фронтенд-реализации Shpigovsky.ru.

Charter фиксирует обязательства исполнителя, SSOT, правила вёрстки, протоколы Foundation First и Shell First, QA Gates, последовательность deliverables и stop conditions. Все числовые и методологические решения берутся из **Production Standards Approval v3** (APPROVED WITH ANDREY CORRECTIONS, 2026-06-13).

**Ключевые контрактные решения:**

| Решение | Значение |
|---------|----------|
| Production SSOT | Production Standards **v3** |
| Первая рабочая страница | `ui-demo.html` — **не** Home |
| Home (PG-001) | **Запрещена** до Foundation QA PASS |
| Container | **1170px** |
| Padding | **40px** desktop / **20px** mobile |
| Font | **Inter** |
| Radius | **30px** default · **10px** inputs · **999px** circular |
| CSS methodology | **Desktop-first** |
| Min viewport | **320px** |
| Breakpoint switch | **1024px** |

**Вердикт:** charter **READY FOR FOUNDATION PRODUCTION** (Phase 1+). Gulp workspace creation — следующий исполнительный шаг вне scope данного документа.

---

## Charter Scope

**В scope charter:**

- Производственный контракт: scope, стек, SSOT, правила вёрстки, протоколы, QA, deliverables, reports, stop conditions
- Утверждённая последовательность Phase 0–8
- Сопоставление с upstream-документами и фиксация конфликтов
- Placeholder policy для missing design pages (PD-09)

**Вне scope charter:**

- Написание HTML / SCSS / JS
- Создание Gulp workspace (авторизуется charter, но не выполняется в данной задаче)
- Изменение Page Inventory, Block Inventory
- WordPress Architecture, ACF Architecture, SEO/IA charter
- Commit / push

---

## Conflicts Found

Конфликты между charter и ранее созданными документами. **Автоматическое исправление upstream-документов не выполнялось.**

| ID | Конфликт | Источники | Решение charter | Блокирует production? |
|----|----------|-----------|-----------------|----------------------|
| **CF-01** | **Container width** | Normalization v1: **1160px** · Production Standards v3: **1170px** (Olga) | **1170px** — SSOT = v3 (PD-02). Normalization v1 остаётся evidence layer; токен `container-max` в коде = 1170 | **No** |
| **CF-02** | **Border radius** | Normalization v1: **8px** default (`radius-sm`) · v3: **30/10/999px** | **30/10/999px** — SSOT = v3 (PD-06, PD-10). Шкала 4/8/12/16/24 deprecated | **No** |
| **CF-03** | **Body typography** | Normalization v1: body **16px** default · v3: body **18/16 w300** (Olga) | **18/16 w300** — SSOT = v3 (PD-04) | **No** |
| **CF-04** | **Mobile H2** | Normalization v1: **32px** · v3: **22px w500** (Olga) | **22px w500** — SSOT = v3 (TY-02) | **No** |
| **CF-05** | **Text color** | Normalization v1: `#3D3D3D` · v3: `#475371` (Olga) | `#475371` — SSOT = v3 | **No** |
| **CF-06** | **Page background** | Normalization v1: solid `#E3EAF2` · v3: `rgba(218,229,240,0.7)` over `#FFFFFF` | Layered wash — SSOT = v3 (PD-11) | **No** |
| **CF-07** | **Frontend Production gate** | Foundation v1 §8: «Production **запрещён** до Numeric Rules» · Normalization v1 §11: charter **HOLD** | **v3 APPROVED** закрывает gate. Numeric Rules v2 = evidence only; charter действует | **No** |
| **CF-08** | **Service tree depth** | Page Inventory v1: **3 уровня** (hub → section → leaf) · Excel intake (v3 §10): **4 уровня** под «Зависимости» | G-SERVICE template + breadcrumb extension до L4; IA charter — отдельный трек (N-01) | **No** для foundation |
| **CF-09** | **About scope** | Page Inventory: **1 PDF** (PG-005) · Excel N-07: **6 подстраниц** | PG-005 template first; sub-pages = placeholder / reuse G-ABOUT tail | **No** для foundation |
| **CF-10** | **Avatar radius token** | Normalization v1: `radius-full` **50%** · v3: `radius-pill` **999px** | **999px** для circular elements — SSOT = v3; семантически эквивалентно | **No** |
| **CF-11** | **Global styles vs shell order** | Start Sequence: Step 5 Global styles **после** header/footer desktop · логически styles частично нужны раньше | Charter Phase 5 = global styles **после** desktop header/footer (Phase 3–4), **до** mobile (Phase 6). Минимальные reset/vars допустимы в Phase 1 для shell markup | **No** — engineering sequencing |
| **CF-12** | **Genotyping page** | Page Inventory M-05: design **missing** · Excel: URL `/uslugi/genotipirovanie/` **confirmed** | Card/nav links → confirmed URL; page = placeholder per PD-09 | **No** для scaffold |

---

## No Conflicts Found

Следующие домены **согласованы** между charter, Production Standards v3, Start Sequence v1 и обязательными upstream-документами:

| Domain | Aligned value | Sources |
|--------|---------------|---------|
| Font family | **Inter** | v3, Start Sequence |
| Desktop padding | **40px** | v3 PD-13, Normalization `space-8`, Start Sequence |
| Mobile padding | **20px** | v3, Normalization, Start Sequence |
| Breakpoint | **1024px**, desktop-first | v3 PD-07, Start Sequence |
| Min viewport | **320px** | v3 §9.3 |
| Typography restrictions | `letter-spacing` / `word-break` / `overflow-wrap` / `hyphens` **forbidden** (any value) | v3 §4.3 PD-14, PD-15 · OL-06 |
| Section spacing | Factory rule + v3 §6.2 (same-bg 80px single boundary, mobile 64px, band 240px) | v3, Start Sequence |
| Shell-first before Home | Mandatory Phase 0–7 before Phase 8 | v3 §16, Start Sequence, Factory protocol |
| Foundation demo page | `ui-demo.html` — not `index.html` | Start Sequence Step 1 |
| First Home block forbidden | BLK-007 и PG-001 marketing blocks до Foundation QA | Start Sequence, Block Inventory |
| Page count | **11** page types | Page Inventory |
| Block count | **40** Block ID | Block Inventory |
| Home canonical | Home **v2** | Page Inventory, Block Inventory |
| G-SERVICE template | PG-002/003/004 — единый каркас, swap-slot 011/012/013 | Block Inventory §6 |
| Stack | HTML · SCSS · JS · jQuery · Gulp · gulp-file-include | Foundation v1 §7.1 |
| Source-first | `src/` only; `dist/` generated | Foundation v1 §7.2 |
| Placeholder policy | Missing design pages не блокируют scaffold (PD-09) | v3 §12, §13 |

---

## Files Created

| File | Action |
|------|--------|
| `FP-0002-FRONTEND-PRODUCTION-CHARTER-v1.md` | **Created / formatted** — производственный контракт v1 |

**Не создано / не изменено:** HTML, SCSS, JS, Page Inventory, Block Inventory, git commits.

---

## Readiness Status

| Gate | Status |
|------|--------|
| Production Standards v3 approved | **PASS** — 2026-06-13 |
| Charter v1 issued | **PASS** |
| Foundation production (Phase 1+) | **READY** |
| Home page production (Phase 8) | **BLOCKED** — until Foundation QA PASS |
| Gulp workspace | **NOT STARTED** — authorized by charter, out of scope данной задачи |
| Pixel-perfect client sign-off | **OPEN** — PDF untracked, asset extraction TBD |

---

# CHARTER — FP-0002 FRONTEND PRODUCTION

## 1. Scope работ

### 1.1 В scope Frontend Production

| Область | Описание |
|---------|----------|
| **Foundation** | Shell, typography/UI demo, header/footer desktop + mobile, global styles, Foundation QA |
| **Home** | FP-0002-PG-001 Home v2 — 17 content blocks по Block Inventory §2.3 (после Foundation QA) |
| **Core pages** | PG-002…PG-011 по Page Inventory — desktop-first, mobile per PDF |
| **Shared chrome** | BLK-001…004, BLK-003 footer — Core Shared blocks |
| **G-SERVICE** | Единый template PG-002/003/004 с swap-slot BLK-011/012/013 |
| **Placeholder pages** | M-01, M-05, M-03/M-04 — engineering stubs per PD-09 |

### 1.2 Вне scope Frontend Production (настоящий charter)

- WordPress theme development
- ACF field architecture
- Backend / CMS integration
- SEO copywriting, content entry at scale
- IA charter (4-level URLs, slug normalization)
- Изменение Page Inventory / Block Inventory

### 1.3 Visual SoT

- **24 PDF-макета** в `INCOMING/01_DESIGN/` — PDF-only SoT (PROJECT DECISION)
- Figma **не используется**
- Home **v2** canonical; Home v1 superseded

### 1.4 Deliverable inventory

| Type | Count | Reference |
|------|-------|-----------|
| Page types | **11** | Page Inventory v1 |
| Block ID | **40** | Block Inventory v1 |
| Missing pages (parallel) | **6** | M-01…M-06 |

---

## 2. Используемый стек

| Layer | Technology | Contract rule |
|-------|------------|---------------|
| Markup | **HTML5** + semantic landmarks | `header`, `main`, `nav`, `footer`, `section` |
| Composition | **gulp-file-include** | `@@include` partials; entries in `src/pages/` |
| Styles | **SCSS** | Desktop-first; tokens from v3 only in `utils/_vars.scss` |
| Behavior | **JavaScript** + **jQuery** | `data-*` hooks; modules in `src/js/modules/` |
| Build | **Gulp** | `src/` → `dist/`; **никогда** не править `dist/` вручную |

**Source-first:** реализация только в `src/`. Build must succeed before REPORT claims PASS.

**Block mapping:** `block_id` из Block Inventory → имя partial / SCSS файла (например `blk-007-page-hero`).

---

## 3. Production SSOT

### 3.1 Иерархия источников (при конфликте)

1. **Production Standards Approval v3** — **единственный production SSOT** для токенов, layout, typography law
2. **Frontend Start Sequence v1** — порядок foundation deliverables
3. **Block Inventory v1** — состав блоков, scroll order, reuse tiers
4. **Page Inventory v1** — page types, Missing Pages Register
5. **Frontend Foundation v1** — taxonomy, component families (read-only context)
6. **Frontend Normalization v1** — evidence layer; **superseded** по токенам, где расходится с v3
7. **Numeric Design Rules v2** — raw PDF evidence; **не** заменяет v3

### 3.2 Заморозка SSOT

Изменения production-токенов после подписи charter — **только** через ADR + новая версия Production Standards / Charter. Ad-hoc правки в коде без документа — **нарушение контракта**.

### 3.3 Официальные production-токены (contract freeze)

| Token | Value | Decision ref |
|-------|-------|--------------|
| `container-max` | **1170px** | PD-02 |
| `page-padding-x-desktop` | **40px** | PD-13 |
| `page-padding-x-mobile` | **20px** | Normalization + v3 |
| `font-family-primary` | **Inter** | PD-01 |
| `radius-default` | **30px** | PD-06 |
| `radius-control` | **10px** | PD-06 |
| `radius-pill` | **999px** | PD-06 |
| `breakpoint-desktop-min` | **1024px** | PD-07 |
| `breakpoint-mobile-max` | **1023px** | PD-07 |
| `min-viewport` | **320px** | v3 §9.3 |
| `color-text-primary` | **#475371** | PD-03 |
| `color-primary-accent` | **#B3261E** | PD-03 |
| `color-bg-page` | **rgba(218, 229, 240, 0.7)** over `#FFFFFF` | PD-11 |
| `font-size-h2` / mobile | **36px** / **22px**, weight **500** | PD-04 |
| `font-size-body` / mobile | **18px** / **16px**, weight **300** | PD-04 |

---

## 4. Обязательные правила вёрстки

### 4.1 Container model

```
viewport (100%)
└─ bg-base #FFFFFF
   └─ bg-page rgba(218,229,240,0.7) [per section policy]
      └─ page-padding-x (40 desktop / 20 mobile)
         └─ container-max 1170 (margin: 0 auto)
            ├─ content column
            └─ card grids (gap 24)
```

### 4.2 Section types

| Type | Behavior |
|------|----------|
| **Content sections** | Vertical stack; `container-max` 1170 centered |
| **Wide sections** | Background `100vw`; inner content aligned to container |
| **Full-bleed media** | Edge-to-edge within wide shell; `radius-none` on flush edges |

### 4.3 HTML / partials discipline

- Одна секция = один partial в `src/partials/sections/` (или project-equivalent)
- Layout chrome: `src/partials/layout/` — BLK-001…004, BLK-003
- Single logical **H1** per page context
- **`@@include`** — только доверенные пути
- **HEADER ≠ HERO** — BLK-007 никогда не является частью header partial

### 4.4 SCSS discipline

- Числовые значения — **только** из v3 tokens в `utils/_vars.scss`
- Секционная изоляция; без `!important` waves без Lead approval
- Desktop-first media queries

### 4.5 Placeholder discipline

- Lorem / «Название раздела» / stub URLs — **content placeholders**, не структурные изменения
- Верстка по **component shape**, не по placeholder text
- Missing design pages (M-01…M-06) — stub или defer per PD-09

---

## 5. Foundation First Protocol

**Определение:** никакая page-level production (включая Home) не начинается до завершения foundation pipeline и прохождения Foundation QA Gate.

### 5.1 Обязательства

| Rule | Contract |
|------|----------|
| First page entry | **`ui-demo.html`** — Foundation Demo Page |
| `index.html` (Home) | **Запрещён** до Phase 7 PASS |
| Home blocks in codebase | BLK-007, BLK-009, BLK-010 и прочие PG-001 sections — **запрещены** до Phase 7 |
| Foundation QA REPORT | Обязателен в `FP-0002-SHPIGOVSKY/REPORTS/` |
| Lead waiver | Единственное исключение из stop condition SC-01 |

### 5.2 Foundation deliverables (minimum)

- Shell: `header` + `main` + `footer`
- Typography + UI demo visible on demo URL
- Desktop header (BLK-001 + BLK-002) + footer (BLK-003)
- Global styles matching v3
- Mobile header/footer + BLK-004 sticky bar
- Foundation QA checklist PASS

---

## 6. Shell First Protocol

**Factory protocol:** [frontend-shell-first-start-protocol-v1.md](../../../projects/mars-website-factory/frontend-shell-first-start-protocol-v1.md)

### 6.1 Shell composition

```text
┌─────────────────────────────────────────┐
│  BLK-001  Header Top Bar                │
├─────────────────────────────────────────┤
│  BLK-002  Header Main Nav + Callback CTA│
├─────────────────────────────────────────┤
│              <main>                     │
│   (Foundation Demo → future page blocks)│
├─────────────────────────────────────────┤
│  BLK-003  Site Footer                   │
└─────────────────────────────────────────┘
     BLK-004 Mobile Sticky Bar (≤1023px, fixed bottom)
```

### 6.2 Shell rules

| Rule | Detail |
|------|--------|
| Shell before content | Header/footer partials exist before page-specific sections |
| No Home hero in shell | BLK-007 **не** в foundation shell |
| Component split | BLK-001, BLK-002 — `partials/components/`; wrapper — `partials/layout/header.html` |
| Build gate | `npm run build` must include layout partials |

### 6.3 Partials creation order

1. `head.html`
2. `header-top-bar.html` (BLK-001)
3. `header-main-nav.html` (BLK-002)
4. `header.html` (wrapper)
5. `footer.html` (BLK-003)
6. `ui-demo.html` page shell
7. `mobile-sticky-bar.html` (BLK-004) — Phase 6

---

## 7. Desktop First Policy

| Decision | Value | Contract |
|----------|-------|----------|
| CSS methodology | **Desktop-first** | Base styles target desktop |
| Layout activation | `min-width: 1024px` | Multi-column grids activate |
| Mobile overrides | `max-width: 1023px` | Single column + sticky bar |
| Tablet 768–1023px | **Mobile layout** | No separate tablet artboard |
| Primary breakpoint | **1024px only** | Intermediate breakpoints — только при block evidence |

**Запрещено:** mobile-first base styles без Lead approval.

---

## 8. Typography Rules

### 8.1 Font

- **Inter** — all UI and content
- Source: Google Fonts recommended; `font-display: swap`
- Weights required: **300**, **400**, **500**

### 8.2 Production type scale (contract subset)

| Level | Desktop | Mobile | Weight |
|-------|---------|--------|--------|
| H1 Display | 70px | 42px | 500 |
| H2 Section | 36px | 22px | **500** |
| H3 Card title | 30px | 22px | 500 |
| Body | **18px** | **16px** | **300** |
| Button | 16px | 16px | 500 |

Полная шкала — v3 §4.1.

### 8.3 Typography restrictions (Lead-approved — HARD LAW)

**Запрещено без отдельного решения Project Lead:**

| Property | Status |
|----------|--------|
| `letter-spacing` | **Forbidden** — any value |
| `word-break` | **Forbidden** — any value |
| `overflow-wrap` | **Forbidden** — any value |
| `hyphens` | **Forbidden** — any value |

**Detection:** property presence in `src/scss/**` or compiled CSS = **FAIL**. Fix overflow via layout (`min-width: 0`, containers, grid) — see [russian-no-word-splitting-typography-v1.md](../../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md) §1.2–§1.3.

---

## 9. Section Spacing Rules

**Factory rule:** [frontend-section-spacing-rule-v1.md](../../../projects/mars-website-factory/frontend-section-spacing-rule-v1.md)

### 9.1 FP-0002 token map

| Context | Token | Value | Rule |
|---------|-------|-------|------|
| Same-background gap | `section-gap-same-bg` | **80px** | **Single boundary only** — not top+bottom full stack |
| Different-background gap | `section-gap-diff-bg` | **80px** default | Surface role change; may use **56px** mid transitions |
| Band transition | `section-gap-band` | **240px** | Full-bleed / major band |
| Section padding Y | `section-padding-y-default` | **80px** | Inner top/bottom standard sections |
| Card grid gap | `space-6` | **24px** | All card grids |
| Form field gap | `space-4` | **16px** | BLK-035 |
| Mobile inter-section | `section-gap-mobile` | **64px** | Default mobile reduction |

### 9.2 Exceptions

Header (BLK-001/002), footer (BLK-003), mobile sticky (BLK-004) — **do not** inherit generic `section-gap`.

### 9.3 Contract rule

**Do not infer** inter-section gaps from one PDF block — use tokens above only.

---

## 10. Radius Rules

### 10.1 Lead-approved radius system

| Token | Value | Usage |
|-------|-------|-------|
| `radius-default` | **30px** | Buttons, cards, blocks, panels, FAQ shells |
| `radius-control` | **10px** | Input, textarea, select, form controls only |
| `radius-pill` | **999px** | Circular elements, capsule chips, pill buttons |
| `radius-none` | `0` | Full-bleed images, flush dividers |

### 10.2 Deprecated (do not use on new work)

`radius-xs` 4px · `radius-sm` 8px · `radius-md` 16px · `radius-lg` 24px — replaced by Lead v3 decision.

### 10.3 Element mapping

| Element | Radius |
|---------|--------|
| Primary button | **30px** |
| Header callback | **30px** |
| Input / textarea / select | **10px** |
| Card | **30px** |
| FAQ panel | **30px** |
| Specialist avatar | **999px** |
| Pagination chip | **10px** or **30px** (control-sized → 10px) |

---

## 11. Responsive Rules

### 11.1 Breakpoints

| Token | Value |
|-------|-------|
| Desktop min | `min-width: 1024px` |
| Mobile max | `max-width: 1023px` |
| Min supported viewport | **320px** |

### 11.2 Layout strategies

| Viewport | Strategy |
|----------|----------|
| Desktop ≥ 1024px | Multi-column grids; full header; no sticky bar |
| Mobile ≤ 1023px | Single column; 20px padding; BLK-004 active |
| Tablet 768–1023px | Mobile layout |

### 11.3 Reference scale (block-specific tuning only)

1440 · 1310 · 1199 · 1024 · 767 · 660 · 580 · 490 · 390 · 370 — use only when block evidence requires.

### 11.4 Responsive debt (logged, not foundation blockers)

| Item | Impact |
|------|--------|
| PG-009 Article mobile | No mockup — desktop first |
| PG-008 Blog hub | Misnamed mobile file |
| M-01…M-06 | Placeholder or defer |

---

## 12. QA Gates

### 12.1 Foundation QA Gate (mandatory before Home)

**Home production forbidden until PASS** (or explicit Lead waiver).

| # | Criterion | Evidence |
|---|-----------|----------|
| G-01 | `npm run build` succeeds | Build log in REPORT |
| G-02 | `ui-demo.html` renders in `dist/` | File exists |
| G-03 | Shell: header + main + footer on demo page | Visual / DOM |
| G-04 | **No** Home blocks (BLK-007, 009, 010…) in codebase | Code review |
| G-05 | Typography demo H1–H6 per v3 §4.1 | Screenshot desktop |
| G-06 | UI demo: buttons, forms, FAQ, card | Screenshot |
| G-07 | Spacing demo labels present | Screenshot |
| G-08 | Header desktop ≥1024px structure | QA viewport |
| G-09 | Footer desktop multi-column | QA viewport |
| G-10 | Mobile header + footer ≤1023px | QA viewport |
| G-11 | BLK-004 sticky bar mobile only | QA viewport |
| G-12 | Token spot-check: 1170 · 40/20 · 30/10/999 · colors | vs v3 |
| G-13 | `SECTION SPACING — PASS \| partial \| FAIL` | Factory rule |
| G-14 | `RU TYPOGRAPHY / NO WORD-SPLITTING — PASS \| partial \| FAIL` | §8.3 |
| G-15 | Lead acknowledgment | Sign-off |

### 12.2 Per-page QA (after Foundation)

Each page/block delivery: build PASS + REPORT + **STOP for approval** before next block.

### 12.3 Fail actions

| Fail | Action |
|------|--------|
| Token drift | Fix global styles — no Home work |
| Shell incomplete | Complete Phase 1–4 before Phase 5–6 |
| Spacing double-gap | Apply Factory same-bg single-boundary rule |
| Home block leaked | Remove from `ui-demo` / pages |
| Typography violation | Remove forbidden properties |

---

## 13. Deliverable Sequence

### 13.1 Утверждённая последовательность Phase 0–8

| Phase | Name | Scope | Deliverable | Blocks Home? |
|-------|------|-------|-------------|--------------|
| **0** | **Production Standards** | SSOT freeze | Production Standards v3 **APPROVED** | Yes — **closed** |
| **1** | **Shell** | Layout frame | `header` + `main` + `footer` partials; `ui-demo.html` entry — **not** Home | **Yes** |
| **2** | **Typography + UI Demo Page** | Foundation content in `main` | H1–H6, body, lists, links, buttons, form fields, quote, spacing samples | **Yes** |
| **3** | **Desktop Header** | BLK-001 + BLK-002 | Dual-row header desktop ≥1024px | **Yes** |
| **4** | **Desktop Footer** | BLK-003 | Footer multi-column desktop | **Yes** |
| **5** | **Global Styles** | Tokens + base | Inter, colors, radius 30/10/999, spacing scale, default content styles | **Yes** |
| **6** | **Mobile Header/Footer** | Responsive shell | Condensed header, footer stack, BLK-004 sticky, mobile spacing 64px | **Yes** |
| **7** | **Foundation QA** | Verification | `# REPORT — FP-0002 foundation QA` · checklist PASS · Lead ack | **Yes** until PASS |
| **8** | **Home Page Production** | PG-001 | Home v2 blocks per Block Inventory — **only after Phase 7 PASS** | Allowed after Phase 7 |

### 13.2 Phase 2 — UI Demo minimum content

| # | Demo section | v3 ref |
|---|--------------|--------|
| 1 | Headings H1–H4 + alt tokens | §4.1 |
| 2 | Body 18/16 w300 · body-sm · caption | §4.1 |
| 3 | Links · lists · blockquote | §4.1 |
| 4 | Buttons: primary 44px · header callback 40px | §8.1 |
| 5 | Form fields radius **10px** | §8.2 |
| 6 | Card radius **30px** | §8.3 |
| 7 | FAQ accordion demo | §8.4 |
| 8 | Spacing labels: same-bg 80 · band 240 · mobile 64 | §6.2 |

### 13.3 Phase 8 — Home block order (scroll order, post-QA)

BLK-007ᴴ → 009 → 022 → 010 → 014 → 015 → 018 → 019 → 020 → 021 → 023 → 024 → 026 → 027 → 034 → 035 (+ BLK-004 verify).

Shell blocks BLK-001/002/003 — already in place; not re-implemented.

### 13.4 Post-Home page order (recommended)

PG-002 → PG-004 → PG-003 → PG-005 → PG-006 → PG-007 → PG-008 → PG-009 (desktop) → PG-010 → PG-011.

---

## 14. Report Requirements

### 14.1 Foundation QA REPORT (Phase 7)

**Path:** `FP-0002-SHPIGOVSKY/REPORTS/FP-0002-FOUNDATION-QA-REPORT.md` (или эквивалент)

**Обязательные секции:**

| Section | Content |
|---------|---------|
| Build evidence | `npm run build` log / exit code |
| Viewport evidence | Screenshot list: desktop ≥1024px · mobile ≤1023px |
| Token spot-check | Container 1170 · padding 40/20 · radius 30/10/999 · Inter · colors vs v3 |
| `SECTION SPACING` | PASS \| partial \| FAIL |
| `RU TYPOGRAPHY / NO WORD-SPLITTING` | PASS \| partial \| FAIL \| SAFE UNKNOWN |
| Checklist G-01…G-15 | Per-row status |
| Lead acknowledgment | Sign-off field |

### 14.2 Per-block / per-page REPORT

Each production slice after Foundation:

- Build PASS evidence
- Block ID / Page ID reference
- Screenshot desktop + mobile (where applicable)
- Open questions logged as SAFE UNKNOWN
- **STOP** — await approval before next slice

### 14.3 REPORT format convention

```markdown
# REPORT — FP-0002 [slice name]

## Executive Summary
## Deliverables
## QA Results
## Open Items
## Readiness Status
```

---

## 15. Stop Conditions

### 15.1 Hard stops (production must halt)

| ID | Condition | Action |
|----|-----------|--------|
| **SC-01** | Foundation QA **not PASS** | **Stop** all Home / PG-001 work |
| **SC-02** | `index.html` or Home blocks created before Phase 7 | **Remove** · revert to shell-only |
| **SC-03** | Token drift from v3 SSOT without ADR | **Stop** · fix tokens before continuing |
| **SC-04** | `letter-spacing` / `word-break` / `overflow-wrap` / `hyphens` detected in source or compiled CSS | **Remove** · fix via layout + HTML typograph |
| **SC-05** | Manual edits in `dist/` | **Revert** · fix in `src/` only |
| **SC-06** | Build failure | **Stop** · no REPORT PASS claims |
| **SC-07** | Page Inventory / Block Inventory modified without charter | **Escalate** to Lead |

### 15.2 Soft stops (log and continue with PD-09)

| ID | Condition | Mitigation |
|----|-----------|------------|
| **SC-08** | Missing design page (M-01…M-06) | Placeholder / stub |
| **SC-09** | Header exact heights unknown (OQ-11) | Engineering placeholders |
| **SC-10** | PDF not in git | Continue token-based; pixel QA deferred |
| **SC-11** | Coordinator Design Approval Sheet v2 unsigned | Engineering defaults per PD-09 |

### 15.3 Approval stops (cadence)

After each block/page slice in Phase 8+: **STOP for Lead approval** before next block.

### 15.4 Waiver

Only **Frontend Lead (Андрей)** may issue explicit waiver for SC-01. Waiver must be documented in REPORT.

---

## Approval record

| Field | Value |
|-------|-------|
| Document version | **v1** |
| Parent SSOT | FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3 |
| Frontend Lead | Андрей |
| Charter status | **ISSUED** |
| Date | **2026-06-13** |

---

## Document control

| Field | Value |
|-------|-------|
| Version | **v1** |
| Created | 2026-06-13 |
| Changed in this task | **Created / formatted:** `FP-0002-FRONTEND-PRODUCTION-CHARTER-v1.md` |
| Commit / push | Not performed |

---

*Frontend Production Charter only. No code, no SCSS, no JS, no inventory changes.*
