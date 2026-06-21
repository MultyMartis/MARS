# FP-0002 — Frontend Foundation v1

**Document type:** Official Frontend Foundation (first release)  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-11  
**Coordinator:** PER-0010 — Ольга Дягилева  

**ATLAS:** ORG-0008 · PRJ-0012 · WEB-SHPIG-01 · DOM-SHPIG-01  

**Visual source of truth:** PDF-макеты в `INCOMING/01_DESIGN/` (Figma отсутствует — **PROJECT DECISION**).  
**Home canonical:** Home v2 (`2026-06-11-home-v2/`).

**Upstream inputs (read-only):**

| Input | Role |
|-------|------|
| FP-0002-PAGE-INVENTORY-v1.md | 11 страниц, G-SERVICE, Missing Pages Register |
| FP-0002-BLOCK-INVENTORY-v1.md | 40 Block ID, variant families, reuse tiers |
| FP-0002 DESIGN INTAKE AUDIT | Template discovery, reusable zones |
| FP-0002 HOME V2 INTAKE UPDATE | Canonical home order, генотипирование в preview |

**Companion artifact:** [FP-0002-NUMERIC-DESIGN-RULES-v1.md](FP-0002-NUMERIC-DESIGN-RULES-v1.md) — все числовые параметры; **требует согласования координатора до Frontend Production**.

**Scope:** производственная база для последующей реализации. **Не** вёрстка. **Не** Design System ради Design System.

**Out of scope (запреты charter):** Frontend Production, WordPress Architecture, ACF Architecture, Frontend Production Plan.

---

# REPORT — FP-0002 FRONTEND FOUNDATION

**Git status (до работы):** ветка `mars/post-cycle8-live-tests`, up to date с `origin`. `INCOMING/01_DESIGN/` — **untracked** (`??`). Новые артефакты Foundation — **untracked**. Прочие изменения репозитория не затрагивались. Commit / push **не выполнялись**.

**Evidence method:** Page/Block Inventory + pixel-sampling и text-layer анализ PDF (PyMuPDF) по desktop/mobile artboard; font-family из PDF **недоступны** (Type3 outlines).

---

## 1. Executive Summary

Создан **первый официальный Frontend Foundation** проекта FP-0002 (Shpigovsky.ru) — производственная база для статической фронтенд-реализации под стек **HTML · SCSS · JavaScript · jQuery · Gulp · gulp-file-include**.

| Метрика | Значение |
|---------|----------|
| Страниц (Page Inventory) | **11** |
| Блоков (Block Inventory) | **40** |
| Desktop artboard (PDF) | **1437 px** — единый сигнал |
| Mobile artboard (PDF) | **380 px** (основной); **390 px** — 1 файл |
| Подтверждённых component families | **7** (button, input, form, card, CTA, FAQ, navigation) |
| Numeric parameters document | **Создан** — [FP-0002-NUMERIC-DESIGN-RULES-v1.md](FP-0002-NUMERIC-DESIGN-RULES-v1.md) |
| Frontend Production | **ЗАПРЕЩЁН** до согласования Numeric Design Rules |

**Ключевые выводы:**

- Сайт — **компонентный long-scroll** с сильным shared-ядром (header, program, FAQ, form, specialists…) и page-role unique slots.
- **G-SERVICE** — единый flexible template (PG-002/003/004) с одним swap-slot контента.
- **Home v2** — единственная canonical главная; v1 superseded.
- PDF-only SoT: типографические **семейства** и **breakpoints** в макетах **не декларированы**; извлечены artboard-ширины, content margins, font-size scale, палитра-сигналы.
- Следующий обязательный шаг: **согласование Numeric Design Rules с PER-0010** → только после этого допускается Frontend Production.

---

## 2. Layout Foundation

Определения ниже — **по факту PDF-макетов**, без проектирования новых layout-систем.

### 2.1 Container model

| Layer | Role | Evidence | Status |
|-------|------|----------|--------|
| **Base / viewport shell** | Полная ширина artboard | Desktop PDF **1437 px**; mobile **380 px** | CONFIRMED (artboard) |
| **Content container** | Основная колонка текста и карточных сеток | Text-block margins: **~133 px** слева; content width **~1140–1170 px** на desktop (404, Home v2, Contacts, Blog hub) | CONFIRMED |
| **Wide container** | Секции с фоном на всю ширину artboard | Hero (BLK-007), Guest Visit CTA (BLK-019), Program (BLK-020), footer bands — фон до краёв artboard при сохранении внутреннего content inset | CONFIRMED (pattern) |
| **Mobile content inset** | Внутренняя колонка mobile | Margin **~29 px** слева, **~25 px** справа; content **~326 px** при artboard 380 px | CONFIRMED |

**SAFE UNKNOWN:** точная семантика «wide» vs «full-bleed» для каждой из 40 секций; pixel-perfect hero background crop.

### 2.2 Working areas (page regions)

| Area | Blocks | Layout behavior |
|------|--------|-----------------|
| **Global chrome** | BLK-001, 002, 003, 004 | Fixed header stack + footer; mobile sticky CTA overlay (BLK-004) |
| **Wayfinding band** | BLK-005, 006 | Breadcrumbs + horizontal anchor nav под hero на G-SERVICE / About |
| **Hero band** | BLK-007 (4 variants) | Full-width background; content inset в content container |
| **Marketing stack** | BLK-009…027 (home), shared tail G-SERVICE | Vertical section stack; alternating light background bands |
| **Archive / listing** | BLK-016, 028 + BLK-017 | Card grid + pagination |
| **Article reading** | BLK-029…033 | TOC sidebar + long-read column (desktop); mobile — **gap** |
| **Utility** | BLK-008, 039, 040 | Minimal or single-column narrative |

### 2.3 Grid type

| Context | Grid signal | Evidence |
|---------|-------------|----------|
| **Service / direction cards** | Multi-column card grid | BLK-010, 011 — карточки в ряд на desktop; single column stack на mobile PDF |
| **UTP / feature cards** | 3-up row → stack | BLK-009 (3 cards), BLK-014 (feature row) |
| **Specialists / reviews / articles** | Card grid, 3–4 columns desktop | BLK-026, 015, 027, 028 |
| **Program 4 directions** | 4-column numbered grid | BLK-020 — 01–04 |
| **Rehabilitation steps** | 4-step horizontal → vertical | BLK-018 |
| **FAQ + form** | Single column accordion; form 2-column fields desktop | BLK-034, 035 |
| **Article single** | 2-column: TOC + body | BLK-029 + BLK-030 (desktop only) |

**Grid type summary:** **CSS Grid / Flex hybrid** — card grids + vertical section stack. **Не** 12-column Bootstrap-style; точное число колонок → Numeric Rules.

**SAFE UNKNOWN:** gutter width, column count per breakpoint, asymmetric article TOC width.

### 2.4 Desktop layout specifics

- Artboard **1437 px** — единственный desktop frame во всех PDF.
- Long-scroll pages: Home v2 **~16809 px** высота (1 PDF-страница).
- Horizontal **in-page anchor navigation** (BLK-006) на service/about pages.
- **Dual header:** top bar (контакты, генотипирование, специалисты) + main nav + CTA «Заказать звонок».
- Card-heavy mid-page zones; expert opinion, program, FAQ — повторяющиеся ритмы.
- Pagination на archive pages (отзывы, блог).

### 2.5 Mobile layout specifics

- Artboard **380 px** (11 из 12 mobile PDF); **390 px** — один файл (**SAFE UNKNOWN** — intentional или export artifact).
- **Sticky bottom CTA bar** (BLK-004): телефон · заказать звонок · записаться — на всех mobile PDF кроме 404 pattern.
- Anchor nav → **вертикальный stack** или scrollable chips (**SAFE UNKNOWN** exact control).
- Card grids → **single column** (визуальный сигнал mobile PDF).
- Home v2 mobile scroll **~22883 px** — тот же порядок секций, что desktop v2.
- **PG-009 Article:** mobile PDF **отсутствует** — responsive debt.

---

## 3. Typography Foundation

Фиксация **фактических** стилей из PDF text-layer. Новые стили **не проектировались**.

### 3.1 Font families

| Role | Family | Status |
|------|--------|--------|
| All text | — | **SAFE UNKNOWN** — PDF использует Type3 outlined fonts; имена семейств не извлекаются |
| Cyrillic coverage | Required | CONFIRMED (весь контент RU) |

**Coordinator action:** подтвердить font files / Google / self-hosted источник до Production.

### 3.2 Typographic hierarchy (size-based, from PDF spans)

| Level | Desktop sizes (px, PDF points) | Mobile sizes (px) | Typical use (Block Inventory) | Status |
|-------|-------------------------------|-------------------|-------------------------------|--------|
| **Display / Hero H1** | **70** | **42** | BLK-007 Home hero headline | CONFIRMED (size) |
| **Section H2** | **36–42** | **32–42** | Section titles, 404 headline | CONFIRMED (size) |
| **Section H3 / card title** | **24–30** | **22–24** | Card headings, program titles | CONFIRMED (size) |
| **Subheading / lead** | **20–21** | **18–20** | Hero sub, expert name | CONFIRMED (size) |
| **Body** | **16–18** | **16–18** | Paragraphs, FAQ answers, article body | CONFIRMED (size) |
| **UI / nav / caption** | **13–15** | **13–15** | Top bar, breadcrumbs, meta, dates | CONFIRMED (size) |
| **Step numbers / accents** | **26** | **22** | BLK-018, BLK-020 numbering | ESTIMATED |

**SAFE UNKNOWN:** line-height per level, letter-spacing, font-weight names, quote-specific family.

### 3.3 Heading families

- **One sans family** (визуально) для hero, section titles, card titles — подтверждено визуально, не метаданными.
- **No separate serif** для article long-read в извлечённых сигналах.

### 3.4 Body text

- Primary body: **16–18 px** на desktop и mobile.
- Article long-read (BLK-030): тот же body scale + subheadings **20–24 px**.

### 3.5 Captions

- Meta: дата, время чтения, «повод обращения» — **13–14 px**.
- Breadcrumbs, top bar links — **13–15 px**.

### 3.6 Quote styles

| Pattern | Block | Signal |
|---------|-------|--------|
| Expert blockquote | BLK-022 | Indented quote + attribution «Сергей Шпиговский» |
| Review excerpt | BLK-015, 016 | Quotation marks, author line |
| Article pull-quote | BLK-030 | **SAFE UNKNOWN** — не выделен отдельным size в extraction |

**SAFE UNKNOWN:** border-left, italic, background для quote — требует visual pass координатора.

---

## 4. Color Foundation

Палитра извлечена **pixel-sampling** PDF (Home v2, service pages). Hex — **ближайшие** значения из rasterized export.

### 4.1 Primary colors

| Token (semantic) | Hex (signal) | Role | Status |
|------------------|--------------|------|--------|
| `primary-accent` | **#B3261D** | CTA buttons, ключевые action surfaces | CONFIRMED |
| `primary-dark` | **#455069** – **#444F68** | Top bar, header text, strong UI chrome | ESTIMATED |

### 4.2 Accent colors

| Token | Hex | Role | Status |
|-------|-----|------|--------|
| `accent-warm-gray` | **#9E9694** – **#988F8A** | Secondary text accents | ESTIMATED |
| `accent-slate` | **#57627D** | Links, interactive hints | ESTIMATED |

### 4.3 Text colors

| Token | Hex | Role | Status |
|-------|-----|------|--------|
| `text-primary` | **#3B3D3D** – **#3D403F** | Body, headings | ESTIMATED |
| `text-muted` | **#8D9097** | Footer secondary, meta | ESTIMATED |
| `text-on-primary` | **#FFFFFF** (inferred on red CTA) | Button labels | ESTIMATED |

### 4.4 Background colors

| Token | Hex | Role | Status |
|-------|-----|------|--------|
| `bg-page` | **#E3EAF2** – **#E4EBF3** | Page / section wash | CONFIRMED |
| `bg-section-alt` | **#F1F5F9** – **#F9FBFD** | Card surfaces, elevated panels | ESTIMATED |
| `bg-footer` | **#E1E7EF** – **#E2E8EF** | Footer band | ESTIMATED |

### 4.5 Border colors

| Token | Hex | Role | Status |
|-------|-----|------|--------|
| `border-subtle` | **#C6CEDA** – **#CBD4E0** | Card borders, dividers | ESTIMATED |
| `border-input` | **#BCC6D5** | Form fields | ESTIMATED |

**Project palette summary:** спокойная **blue-gray** база + **red** primary CTA + **slate** chrome. Полная token-таблица → Numeric Design Rules.

**SAFE UNKNOWN:** hover/focus/active color shifts; error/success form states.

---

## 5. Component Foundation

Семейства зафиксированы по **Block Inventory v1**. Это **taxonomy для Production**, не реализованные компоненты.

### 5.1 Button family

| Variant | Block / context | Visual signal |
|---------|-----------------|---------------|
| **Primary CTA** | BLK-007, 019, 025, 004 | Filled red (`#B3261D`), rounded rect |
| **Header callback** | BLK-002 | Compact CTA в main nav |
| **Text / link button** | Inline «Записаться на консультацию» | Text + optional underline |
| **Sticky mobile actions** | BLK-004 | 3-up icon+label bar |

**SAFE UNKNOWN:** hover, disabled, loading; modal trigger (M-06).

### 5.2 Input family

| Field | Block | Evidence |
|-------|-------|----------|
| Text | BLK-035 | «Ваше имя» |
| Tel | BLK-035 | «Телефон» |
| Email | BLK-035 | «Email» |
| Textarea | BLK-035 | «Ваш вопрос» / message |

**SAFE UNKNOWN:** label position, error state, checkbox/consent if required.

### 5.3 Form family

| Pattern | Block | Composition |
|---------|-------|-------------|
| **Contact «Остались вопросы»** | BLK-035 | Title + 4 fields + submit CTA; reused PG-001…004 |

### 5.4 Card family

| Card type | Blocks | Distinction |
|-----------|--------|-------------|
| **UTP value** | BLK-009 | Icon + title + short text; 3-up |
| **Service / direction** | BLK-010, 011 | Image + title + link; hub vs home preview |
| **Feature** | BLK-014 | Numeric highlight + label |
| **Specialist** | BLK-026 | Photo + name + role |
| **Review** | BLK-015, 016 | Quote + author + date + «повод» |
| **Article** | BLK-027, 028, 033 | Thumbnail + title + meta |
| **Program direction** | BLK-020 | Number 01–04 + title + description |
| **Step** | BLK-018 | Number + title + text |

### 5.5 CTA family

| Pattern | Block ID | Layout |
|---------|----------|--------|
| Inline consultation | BLK-025 | In-section button/link |
| Guest visit section | BLK-019 | Full-width band + headline + CTA |
| Mobile sticky trio | BLK-004 | Fixed bottom bar |
| Header callback | BLK-002 | Nav-level |

### 5.6 FAQ family

| Pattern | Block | Behavior |
|---------|-------|----------|
| **Accordion** | BLK-034 | «Нас часто спрашивают»; expand/collapse items |

**Note:** один accordion pattern; «compact vs full» — не отдельный variant (Block Inventory §5.1).

### 5.7 Navigation family

| Component | Block | Variants |
|-----------|-------|----------|
| Top bar | BLK-001 | Region, генотипирование, hours, specialists link, phones |
| Main nav | BLK-002 | Primary IA + callback CTA |
| Breadcrumbs | BLK-005 | Depth varies by page |
| Anchor nav | BLK-006 | Page-specific anchor set |
| Footer nav | BLK-003 | Multi-column (placeholder labels in mockup) |
| Mobile sticky | BLK-004 | Conversion bar |
| Pagination | BLK-017 | Numeric pages |

---

## 6. Responsive Foundation

### 6.1 Desktop characteristics (confirmed)

- Artboard width **1437 px** — все desktop PDF.
- Multi-column card grids.
- Dual-row header.
- Side-by-side patterns: FAQ+form proximity, article TOC+body, program 4-up.
- No mobile sticky bar.

### 6.2 Mobile characteristics (confirmed)

- Artboard **380 px** (dominant).
- Single-column stack для card grids.
- **BLK-004** sticky CTA present.
- Condensed header; top bar elements compressed.
- Home v2 section order **matches** desktop v2.

### 6.3 Adaptive signals (not breakpoints)

| Signal | Desktop | Mobile | Status |
|--------|---------|--------|--------|
| Artboard width | 1437 px | 380 px (390 px ×1) | CONFIRMED |
| Column collapse | Multi-column grids | Single column | CONFIRMED (pattern) |
| Sticky CTA | Absent | Present (BLK-004) | CONFIRMED |
| Anchor nav layout | Horizontal | **SAFE UNKNOWN** exact control |
| Article layout | TOC + body | **No mockup** | SAFE UNKNOWN |
| CSS breakpoint value | — | — | **SAFE UNKNOWN** |

**Rule:** breakpoints **не придумываются**. Для Production — только после согласования Numeric Design Rules / coordinator decision.

### 6.4 Responsive debt (from Page Inventory)

| Page | Gap |
|------|-----|
| PG-009 Article | No mobile PDF |
| PG-008 Blog hub | Mobile file misnamed (`Блог конечная - моб.pdf`) |
| M-01…M-06 | Missing screens |

---

## 7. Frontend Production Rules

Правила реализации под стек проекта. **Код не пишется** — только дисциплина. Базируется на MARS Website Factory [frontend-production-rules-v0.md](../../projects/mars-website-factory/frontend-production-rules-v0.md) с проектной спецификой.

### 7.1 Stack

| Layer | Technology | Role |
|-------|------------|------|
| Markup | HTML5 + semantic landmarks | `header`, `main`, `nav`, `footer`, `section` |
| Composition | **gulp-file-include** | `@@include` partials; entries in `src/pages/` |
| Styles | **SCSS** | Tokens → layout → sections → components |
| Behavior | **JavaScript** + **jQuery** (per project stack) | `data-*` hooks; FAQ accordion, anchor scroll, forms |
| Build | **Gulp** | Source → `dist/` pipeline |

### 7.2 Source-first

- Реализация только в **`src/`**; **`dist/`** — generated only.
- Запрещены ручные правки `dist/*`.

### 7.3 HTML / partials discipline

- Одна секция = один partial в `src/partials/sections/` (или project-equivalent).
- Layout chrome: `src/partials/layout/` — BLK-001…004, 003.
- **`block_id`** из Block Inventory → имя partial / SCSS файла (например `blk-007-page-hero`).
- Single logical **H1** per page context.
- `@@include` — только доверенные пути; без user-controlled include params.

### 7.4 SCSS discipline

- Entry: `src/scss/main.scss` → tokens, base, layout, sections.
- **Числовые значения** — только из согласованного [FP-0002-NUMERIC-DESIGN-RULES-v1.md](FP-0002-NUMERIC-DESIGN-RULES-v1.md) после approval.
- Секционная изоляция; без `!important` waves без HITL.
- RU typography: [russian-no-word-splitting-typography-v1.md](../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md) — **mandatory**.

### 7.5 JavaScript discipline

- Модули в `src/js/modules/`; entry `main.js`.
- Hooks: `data-component`, `data-accordion`, `data-anchor-nav` — документировать в handoff.
- **jQuery** — только где уже принят project stack; не дублировать vanilla+jQuery на одном hook.
- FAQ (BLK-034): native `<details>` **или** jQuery accordion — **один owner**; согласовать с coordinator.
- Idempotent init.

### 7.6 Gulp / build

- Pages assemble from `section_map` per Page Inventory block order.
- Build must succeed before REPORT claims.
- Windows EBUSY: delete dist **contents**, not root.

### 7.7 Block-to-production mapping

| Tier | Rule |
|------|------|
| Core Shared (7 blocks) | Implement once; include on all applicable pages |
| Shared (12 blocks) | Parametrize via include args / data attributes |
| Unique (21 blocks) | Page-specific partials |
| G-SERVICE | Single template + swap slot BLK-011/012/013 |

### 7.8 Forbidden until Numeric Rules approved

- Hard-coded spacing/color hex в section partials вне token file.
- Invented breakpoints.
- Frontend Production **any scope**.

### 7.9 Placeholder discipline

- Lorem / «Название раздела» / `/указать URL/` — **content placeholders**, не структурные изменения.
- Верстка по **component shape**, не по placeholder text.

---

## 8. Numeric Design Rules

Все числовые параметры вынесены в отдельный документ:

**[FP-0002-NUMERIC-DESIGN-RULES-v1.md](FP-0002-NUMERIC-DESIGN-RULES-v1.md)**

Каждый параметр помечен: **CONFIRMED** · **ESTIMATED** · **SAFE UNKNOWN**.

**Frontend Production запрещён** до подписания этого документа координатором.

---

## 9. Coordinator Review Required

Перечень для подтверждения **Ольгой (PER-0010)** до начала Frontend Production:

| # | Topic | Why |
|---|-------|-----|
| C-01 | **Numeric Design Rules v1** — все CONFIRMED/ESTIMATED значения | Production gate |
| C-02 | **Font families** — источник шрифтов (files / CDN) | PDF не содержит font names |
| C-03 | **Breakpoint value** между 380 и 1437 artboards | Не указан в макетах |
| C-04 | **Home v2 duplicates** — UTP ×2, hero bullet ×3: артефакт или задумка? | Влияет на content binding |
| C-05 | **Генотипирование card** (BLK-010) — target URL | IA / routing |
| C-06 | **Contacts breadcrumb** — reproduce bug или fix | PG-006 |
| C-07 | **Article mobile** — ждать макет или reuse desktop logic | PG-009 gap |
| C-08 | **Blog hub mobile file** — переименование `Блог конечная - моб.pdf` | PG-008 |
| C-09 | **Modal «Заказать звонок»** — scope M-06 | Header CTA behavior |
| C-10 | **FAQ accordion** — native details vs JS | Affects a11y + JS scope |
| C-11 | **Color hex approval** — especially ESTIMATED tokens | Visual fidelity |
| C-12 | **390 px mobile artboard** — один файл: принять или нормализовать | Responsive consistency |
| C-13 | **UI states** — hover, focus, error, loading | Не в PDF |
| C-14 | **Review expand** — «Читать весь отзыв» M-02 | BLK-015 behavior |

---

## 10. Readiness Check

### Готов ли проект к согласованию Frontend Foundation?

**Да.**

### Обоснование

1. **Page Inventory v1** и **Block Inventory v1** — prerequisites выполнены.
2. **Layout, typography, color, component, responsive** foundations зафиксированы по PDF с явными SAFE UNKNOWN.
3. **Numeric Design Rules v1** создан как отдельный approval artifact.
4. **Production rules** адаптированы под HTML/SCSS/JS/jQuery/Gulp stack.
5. **Home v2 canonical** — учтён во всех секциях.
6. **Coordinator Review Required** — перечень сформирован.

### Не является готовностью к вёрстке

- Frontend Production **заблокирован** до C-01 (Numeric Rules approval).
- Mobile gaps (PG-008, PG-009) — parallel debt, не блокер **согласования Foundation**.

### Вердикт этапа

**READY FOR COORDINATOR REVIEW**

---

## 11. SAFE UNKNOWN

| # | Question | Impact |
|---|----------|--------|
| U-01 | Font family names | Typography Production |
| U-02 | CSS breakpoint px value | Responsive Production |
| U-03 | Line-heights per type level | Vertical rhythm |
| U-04 | Border-radius / border-width systematic scale | Component fidelity |
| U-05 | Button / input exact dimensions | Touch targets |
| U-06 | Icon set source (SVG / FA / custom) | Asset pipeline |
| U-07 | Hover / focus / error UI states | Interaction CSS |
| U-08 | Grid gutter / column counts per section | Card layouts |
| U-09 | Wide vs content container per block | Section CSS |
| U-10 | Article TOC width ratio | PG-009 desktop |
| U-11 | Anchor nav mobile interaction | BLK-006 |
| U-12 | 390 vs 380 mobile artboard | One PDF file |
| U-13 | Design Intake / Home v2 reports — session only | Audit trail |
| U-14 | PDF package untracked in git | Evidence risk |

---

**DO NOT START FRONTEND PRODUCTION**

**Next step:** Согласование [FP-0002-NUMERIC-DESIGN-RULES-v1.md](FP-0002-NUMERIC-DESIGN-RULES-v1.md) с PER-0010.

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Supersedes | — (first official Frontend Foundation) |
| Upstream | FP-0002-PAGE-INVENTORY-v1 · FP-0002-BLOCK-INVENTORY-v1 |
| Companion | FP-0002-NUMERIC-DESIGN-RULES-v1 |
| Changed in this task | **Created:** `FP-0002-FRONTEND-FOUNDATION-v1.md` |
| Commit / push | Not performed |

*Foundation only. No Frontend Production, WordPress Architecture, ACF Architecture.*
