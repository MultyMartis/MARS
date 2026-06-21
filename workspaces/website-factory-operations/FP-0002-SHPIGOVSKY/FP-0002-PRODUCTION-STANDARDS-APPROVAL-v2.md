# FP-0002 — Production Standards Approval v2

**Document type:** Engineering Standards — Production SSOT for layout  
**Audience:** Андрей — Project Lead / Frontend Lead  
**Not for:** PER-0010 (координатор) — coordinator facts integrated as inputs only  

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-13  

**ATLAS:** ORG-0008 · PRJ-0012 · WEB-SHPIG-01 · DOM-SHPIG-01  

**Phase:** Production Standards Approval — **не** Frontend Production  

**Upstream (read-only):**

| Input | Role |
|-------|------|
| [FP-0002-FRONTEND-NORMALIZATION-v1.md](FP-0002-FRONTEND-NORMALIZATION-v1.md) | Production normalization pass |
| [FP-0002-NUMERIC-DESIGN-RULES-v2.md](FP-0002-NUMERIC-DESIGN-RULES-v2.md) | Raw design numbers (24 PDF) |
| [FP-0002-DESIGN-APPROVAL-SHEET-v2.md](FP-0002-DESIGN-APPROVAL-SHEET-v2.md) | Coordinator behavior/content gate |
| Coordinator-provided design facts (Ольга, 2026-06-13) | Colors, font, typography, container, radius note |
| `INCOMING/02_CONTENT/Предварит структура и спрос.xlsx` | SEO/IA intake — **integrated** (§10–11) |
| [FP-0002-PAGE-INVENTORY-v1.md](FP-0002-PAGE-INVENTORY-v1.md) | Page baseline for intake cross-check (read-only) |

**Git status (до работы):** ветка `mars/post-cycle8-live-tests`, up to date с `origin`. Excel-файл в `INCOMING/02_CONTENT/` — **untracked** (`??`). Прочие изменения репозитория не затрагивались. Commit / push **не выполнялись**.

**Scope:** утверждение production-стандартов вёрстки. **Запрещено:** HTML, SCSS, JS, изменение Page Inventory, Block Inventory, WordPress Architecture, ACF Architecture.

**Supersedes:** [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v1.md](FP-0002-PRODUCTION-STANDARDS-APPROVAL-v1.md) — Excel intake §10–11; padding conflict §3.1/§3.3; partial container override `1160px` → **`1170px`** (coordinator-confirmed, unchanged).

---

# REPORT — FP-0002 PRODUCTION STANDARDS APPROVAL

## 1. Executive Summary

Обновлён инженерный документ **Production Standards Approval v2** — SSOT для статической вёрстки Shpigovsky.ru под стек HTML · SCSS · JS · Gulp · gulp-file-include.

**Источники решений (приоритет):**

1. **Coordinator-provided design facts** (Ольга) — цвета, Inter, типографика секций/body, контейнер 1170px, radius note.
2. **Frontend Normalization v1** — spacing, components, grid, line-heights, fallbacks.
3. **Numeric Design Rules v2** — raw evidence; не заменяет production layer.
4. **Production decisions** (Frontend Lead) — radius normalization, breakpoint 1024, UI fallbacks, placeholder policy.

**Ключевые production-решения:**

| Domain | Coordinator input | Production SSOT |
|--------|-------------------|-----------------|
| Font | Inter | **Inter** (Google Fonts, `font-display: swap`) |
| Container | 1170px | **`1170px`** max-width |
| Page background | `#DAE5F0` @ 70% | **`rgba(218, 229, 240, 0.7)`** over `#FFFFFF` base |
| Text | `#475371` | **`#475371`** primary text |
| Accent | `#B3261E` | **`#B3261E`** CTA/chrome accent |
| Section headings | 36/22 px, weight 500 | H2 tokens (desktop/mobile) |
| Body | 18/16 px, weight 300 | body default |
| Radius «30%» | ≈30% | **px-scale + pill + percent-only decorative** |
| Breakpoint | — | **`min-width: 1024px`** desktop layout |
| Spacing | — | **4px-base scale** (Normalization) |

**Excel intake:** файл `Предварит структура и спрос.xlsx` **найден** в `INCOMING/02_CONTENT/` (14 102 bytes, 2026-06-13 03:34:52). Листы `Структура` и `Спрос набросок` прочитаны; intake зафиксирован в §10–11. Page Inventory **не изменялся**.

**Padding conflict (v1):** `page-padding-x-desktop` **50px** в §3.1 vs **40px** в §3.3 — устранён: production SSOT = **40px** (Normalization v1, token `space-8`); см. §3.1, PD-13.

**Статус документа:** **READY FOR ANDREY APPROVAL** — внутренние противоречия v1 устранены; Excel intake выполнен.

---

## 2. Olga Decisions Integrated

Coordinator-provided design facts → production mapping.

| Parameter | Olga value | Production value | Status | Reason |
|-----------|------------|------------------|--------|--------|
| **Background** | `#DAE5F0`, 70% прозрачности | `bg-base: #FFFFFF`; `bg-page: rgba(218, 229, 240, 0.7)` | **APPROVED** | 70% — opacity слоя, не solid hex; CSS: полупрозрачный wash поверх белой базы; effective ≈ `#E5EDF5` |
| **Text** | `#475371` | `color-text-primary: #475371` | **APPROVED** | Coordinator-confirmed; заменяет Normalization `#3D3D3D` |
| **Accent** | `#B3261E` | `color-primary-accent: #B3261E` | **APPROVED** | Coordinator-confirmed; Δ1 к PDF `#B3261D` — принять coordinator |
| **Font** | Inter | `font-family-primary: 'Inter', system-ui, sans-serif` | **APPROVED** | Закрывает C-02 (Approval Sheet v1); Google Fonts self-hosted TBD в Production |
| **Section headings desktop** | 36px, weight 500 | `font-size-h2: 36px`; `font-weight-h2: 500` | **APPROVED** | Совпадает с PDF-dominant H2 |
| **Section headings mobile** | 22px, weight 500 | `font-size-h2-mobile: 22px`; `font-weight-h2: 500` | **APPROVED** | Coordinator override Normalization 32px; совпадает с mobile card-title cluster PDF |
| **Body desktop** | 18px, weight 300 | `font-size-body: 18px`; `font-weight-body: 300` | **APPROVED** | Coordinator elevates 18px to default body (Normalization: 16 default + 18 alt) |
| **Body mobile** | 16px, weight 300 | `font-size-body-mobile: 16px`; `font-weight-body: 300` | **APPROVED** | CONFIRMED mobile PDF dominant |
| **Container width** | 1170px | `container-max: 1170px` | **APPROVED** | Coordinator override Normalization 1160px; ближе к symmetric proposal 1171px (v2) |
| **Border radius** | «30% примерно» | px-scale (§7) | **APPROVED (normalized)** | Не применять 30% как универсальный CSS `border-radius` — см. §7 |

---

## 3. Layout Standards

### 3.1 Container

| Token | Value | Source | Notes |
|-------|-------|--------|-------|
| `container-max` | **1170px** | Olga | Единый max-width для typography + card grids |
| `page-padding-x-desktop` | **40px** | Normalization | Token `space-8`; symmetric viewport inset below overflow |
| `page-padding-x-mobile` | **20px** | Normalization | Symmetric; effective mobile content ≈ 340px @ 380 artboard |
| `artboard-ref-desktop` | 1437px | Numeric v2 | Reference only — not CSS |
| `artboard-ref-mobile` | 380px | Numeric v2 | Reference only; 390px artifact acknowledged |

### 3.2 Section types

| Type | Behavior | Inner constraint |
|------|----------|------------------|
| **Content sections** | Vertical stack; standard section gap | `container-max` 1170, centered |
| **Wide sections** | Background `100vw`; inner content aligned to container | Hero BLK-007, Guest CTA BLK-019, Program BLK-020, footer bands |
| **Full-bleed media** | Image/background edge-to-edge within wide shell | `radius-none` on flush edges |

### 3.3 Container model (production)

```
viewport (100%)
└─ bg-base #FFFFFF
   └─ bg-page rgba(218,229,240,0.7) [optional layer per section]
      └─ page-padding-x (40 desktop / 20 mobile)
         └─ container-max 1170 (margin: 0 auto)
            ├─ content column
            └─ card grids (gap 24)
```

### 3.4 Desktop layout behavior (≥ 1024px)

- Centered `container-max` 1170px.
- Multi-column CSS Grid for card families (3-up, 4-up per Block Inventory).
- Dual-row header: top bar (BLK-001) + main nav (BLK-002).
- Horizontal anchor nav (BLK-006) on G-SERVICE / About.
- Article desktop: TOC sidebar **280px** + `1fr` body (engineering placeholder — PG-009).
- No mobile sticky bar (BLK-004 inactive).

### 3.5 Mobile layout behavior (≤ 1023px)

- Single-column stack for all card grids.
- Sticky bottom CTA bar (BLK-004): **56px** bar height, **48px** min touch per action.
- Condensed header; top bar compressed.
- Anchor nav: horizontal scroll/chips — **implementation TBD** (SAFE UNKNOWN exact control).
- Article mobile: **strategy TBD** (Approval Sheet v2 §5) — engineering default in §13.

### 3.6 Grid defaults

| Context | Desktop cols | Mobile cols | Gap |
|---------|--------------|-------------|-----|
| Default card grids | 3 or 4 (per block) | 1 | **24px** |
| Form fields | 2 | 1 | **16px** |
| Article | TOC + body | 1 (stack) | **32px** (breadcrumb-to-content) |

At 1170px container, 3-col pitch ≈ **374px** per column (`(1170 − 2×24) / 3`).

---

## 4. Typography Standards

**Font family:** `Inter` — all UI and content unless future ADR splits article typography.

**Source:** Google Fonts (recommended); self-host in `src/fonts/` if Production requires offline build.

### 4.1 Production type scale

| Level | Desktop | Mobile | Weight | Line-height | Source | Notes |
|-------|---------|--------|--------|-------------|--------|-------|
| **H1 / Display** | 70px | 42px | 500* | 84px / 50px | Normalization | Hero BLK-007; *weight production default — PDF SAFE UNKNOWN |
| **H2 / Section** | 36px | 22px | **500** | 44px / 28px | **Olga** | Section block titles |
| **H2 alt** | 40px | 40px | 500 | 48px | Normalization | 404, service hero emphasis |
| **H3 / Card title** | 30px | 22px | 500 | 36px / 28px | Normalization | Mobile H3 = Olga section size — differentiate by context/semantics |
| **H3 alt** | 24px | 24px | 500 | 30px | Normalization | Steps, subsections |
| **H4** | 20px | 18px | 400 | 28px / 26px | Normalization | Lead labels, subheads |
| **Body** | **18px** | **16px** | **300** | 28px / 24px | **Olga** | Default paragraphs, FAQ answers |
| **Body small** | 16px | 16px | 300 | 24px | Normalization | Secondary dense copy when needed |
| **Small / UI** | 14px | 14px | 400 | 20px | Normalization | Meta, dates, captions |
| **Caption** | 12px | 12px | 400 | 16px | Normalization | Breadcrumbs, micro UI |
| **Button** | 16px | 16px | 500 | 20px | Normalization | CTA labels |
| **Form label** | 16px | 16px | 400 | 24px | **Production decision** | Align with field height 48px; not in Olga brief |
| **Quote** | 18px | 16px | 300 | 28px / 24px | Normalization | BLK-022 expert quote |

### 4.2 Typography decisions log

| ID | Decision | Rationale |
|----|----------|-----------|
| TY-01 | H1/H3/H4 from Normalization | Olga confirmed section + body only; hero/card hierarchy preserved from PDF evidence |
| TY-02 | Mobile H2 = 22px (Olga) | Overrides Normalization 32px; accepted as coordinator authority |
| TY-03 | Body desktop 18px primary | Olga makes 18px default; 16px retained as `body-sm` token |
| TY-04 | Inter weight 300 for body | Coordinator-specified; confirm font files include 300 |

---

## 5. Color Standards

### 5.1 Coordinator-confirmed

| Token | Hex / value | Role |
|-------|-------------|------|
| `color-bg-base` | `#FFFFFF` | Page base under wash |
| `color-bg-page` | `rgba(218, 229, 240, 0.7)` | Primary page/section wash |
| `color-text-primary` | `#475371` | Body, headings default |
| `color-primary-accent` | `#B3261E` | CTA, key actions, footer accent |

### 5.2 Production fallbacks (Normalization / engineering)

| Token | Hex | Role | Status |
|-------|-----|------|--------|
| `color-text-secondary` | `#8D9097` | Meta, footer secondary | Fallback — ESTIMATED PDF |
| `color-text-on-accent` | `#FFFFFF` | Labels on red CTA | Fallback — contrast |
| `color-primary-dark` | `#455069` | Header chrome, top bar text regions | Fallback — merge PDF cluster |
| `color-bg-elevated` | `#F1F5F9` | Card surfaces (solid — not transparent) | Fallback |
| `color-bg-footer` | `#E2E8EF` | Footer band | Fallback |
| `color-border-subtle` | `#C6CEDA` | Dividers | Fallback |
| `color-border-card` | `#CBD4E0` | Card borders | Fallback |
| `color-border-input` | `#BCC6D5` | Form fields | Fallback |
| `color-white` | `#FFFFFF` | Explicit white token | Production |
| `color-error` | `#B3261E` | Form error — reuse accent until dedicated | **Production placeholder** |
| `color-success` | `#2E7D52` | Form success | **Production placeholder** — not in PDF |

### 5.3 Color implementation notes

- Cards and inputs use **solid** `bg-elevated` / `#FFFFFF` — not 70% wash (readability).
- Coordinator `#DAE5F0` @ 70% **не заменяет** elevated surfaces; применяется к page shell и wide bands.
- Hover/focus/error/success interaction colors — engineering placeholders until visual pass (C-13).

---

## 6. Spacing Standards

### 6.1 Production spacing scale (4px base)

| Token | px | Token | px |
|-------|-----|-------|-----|
| `space-0` | 0 | `space-8` | 40 |
| `space-1` | 4 | `space-9` | 48 |
| `space-2` | 8 | `space-10` | 56 |
| `space-3` | 12 | `space-11` | 64 |
| `space-4` | 16 | `space-12` | 80 |
| `space-5` | 20 | `space-13` | 96 |
| `space-6` | 24 | `space-14` | 120 |
| `space-7` | 32 | `space-15` | 160 |
| | | `space-16` | 240 |

### 6.2 Applied spacing

| Context | Token | Value | Notes |
|---------|-------|-------|-------|
| **Base gap** (inline stacks) | `space-4` | 16px | Default vertical rhythm inside components |
| **Section gap** (standard) | `space-12` | 80px | Raw 72px → 80px (Normalization) |
| **Section gap** (medium) | `space-10` | 56px | Mid-page transitions |
| **Section gap** (band) | `space-16` | 240px | Full-bleed band transitions |
| **Card grid gap** | `space-6` | 24px | All card grids |
| **Card internal padding** | `space-6` | 24px | Card body inset |
| **Form field gap** | `space-4` | 16px | BLK-035 |
| **Breadcrumb-to-hero** | `space-7` | 32px | Wayfinding band |
| **Mobile adjustments** | — | — | Section gap may reduce to `space-11` (64px) on mobile where vertical scroll is extreme; default 80px unless block-specific override |

---

## 7. Radius Standards

### 7.1 Why not universal `border-radius: 30%`

Coordinator note «30% примерно» отражает **визуальную мягкость** углов в макете, не CSS-процент как единый токен.

**Причины:**

1. **CSS `%` radius** вычисляется от **собственных** width/height элемента → на кнопке, карточке и hero-блоке «30%» даст **разные** радиусы в пикселях.
2. **Production** требует **предсказуемые px-токены** для кнопок, инпутов, карточек и QA.
3. **Круглые/капсульные** элементы (аватары, pill-кнопки) — отдельные токены (`50%` / `999px`).
4. **Декоративные/медиа-формы** с органическими контурами — единственный допустимый контекст для `30%` или `50%`.

### 7.2 Production radius scale

| Token | Value | Usage |
|-------|-------|-------|
| `radius-none` | `0` | Full-bleed images, flush dividers |
| `radius-xs` | `4px` | Pagination chips, subtle tags |
| `radius-sm` | `8px` | **Buttons, inputs, FAQ panels** — primary UI |
| `radius-md` | `16px` | **Cards, large blocks** — coordinator «soft corner» intent |
| `radius-lg` | `24px` | Elevated panels, featured tiles (if visual pass confirms) |
| `radius-pill` | `999px` | Capsule buttons, chips |
| `radius-full` | `50%` | Specialist avatars BLK-026 |
| `radius-percent-decorative` | `30%` | **Only** approved decorative/media shapes — not buttons/cards/global |

### 7.3 Element mapping

| Element | Radius token | Notes |
|---------|--------------|-------|
| Primary button | `radius-sm` (8px) | Raw PDF 6px → unified 8px scale |
| Input / textarea | `radius-sm` (8px) | Match button family |
| Card | `radius-md` (16px) | Soft corners per coordinator intent; fallback `radius-sm` if strict PDF match required |
| FAQ panel | `radius-sm` (8px) | PDF 8px |
| Specialist avatar | `radius-full` | Circular |
| Hero decorative shapes | `radius-percent-decorative` | Case-by-case from assets |

---

## 8. Component Standards

### 8.1 Buttons

| Variant | Height | Padding-x | Min-width | Radius | Font | Behavior |
|---------|--------|-----------|-----------|--------|------|----------|
| Primary CTA | 44px | 32px | 280px | `radius-sm` | 16px / 500 | Filled `color-primary-accent`; hover: darken 8% engineering |
| Header callback | 40px | 24px | auto | `radius-sm` | 14px / 500 | Compact nav CTA — dims SAFE UNKNOWN |
| Text/link CTA | auto | — | — | — | 16px / 500 | Inline BLK-025 |
| Sticky mobile (×3) | 48px touch | `flex: 1` | — | — | 12px label | BLK-004; bar 56px total |

### 8.2 Inputs

| Field | Height | Padding | Border | Radius | Gap |
|-------|--------|---------|--------|--------|-----|
| Text / tel / email | 48px | 16px x / 12px y | 1px `border-input` | `radius-sm` | 16px vertical |
| Textarea | min 128px | 16px | 1px | `radius-sm` | 16px |
| Form label | — | — | — | — | 8px below label |

### 8.3 Cards

| Parameter | Value |
|-----------|-------|
| Padding | 24px |
| Border | 1px `border-card` |
| Radius | `radius-md` (16px) |
| Shadow | none (flat) |
| Grid gap | 24px |
| Service image aspect | 16:10 |

### 8.4 FAQ (BLK-034)

| Parameter | Value |
|-----------|-------|
| Item gap | 16px |
| Panel radius | 8px (`radius-sm`) |
| Chevron | 16px |
| Behavior | Accordion single-open — **pending coordinator** (Approval Sheet v2 §7 / C-10); engineering default: single-open |

### 8.5 Breadcrumbs (BLK-005)

| Parameter | Value |
|-----------|-------|
| Font | 12px caption |
| Gap to hero | 32px |
| Separator | `/` or design icon — icon source SAFE UNKNOWN |

### 8.6 Pagination (BLK-017)

| Parameter | Value |
|-----------|-------|
| Cell size | 40×40px |
| Radius | `radius-xs` (4px) on hover/active |
| Gap | 8px |

### 8.7 Header (BLK-001 + BLK-002)

| Layer | Behavior |
|-------|----------|
| Top bar | Region, генотипирование, hours, specialists link, phones |
| Main nav | Primary IA + callback CTA |
| Heights | **SAFE UNKNOWN** — stack measured in Production or design addendum |
| Desktop | Dual-row static (sticky TBD) |
| Mobile | Condensed; hamburger/menu pattern per mockup |

### 8.8 Footer (BLK-003)

| Parameter | Value |
|-----------|-------|
| Background | `color-bg-footer` |
| Layout | Multi-column desktop → stack mobile |
| Padding | `space-12` vertical (80px) engineering default |

### 8.9 Mobile sticky bar (BLK-004)

| Parameter | Value |
|-----------|-------|
| Bar height | 56px |
| Actions | Phone · Callback · Appointment — equal thirds |
| Icon size | 24px (estimated) |
| Position | `fixed` bottom; `z-index` TBD |
| Active | ≤ 1023px only |

---

## 9. Responsive Standards

### 9.1 Approach

| Decision | Value | Rationale |
|----------|-------|-----------|
| **CSS methodology** | **Desktop-first** media queries | PDF pack: desktop artboards primary; `max-width` overrides for mobile |
| **Layout switch** | **`1024px`** | Production decision; between mobile artboard 380 and desktop 1437; aligns gulp-starter project breakpoints |
| `breakpoint-desktop-min` | `min-width: 1024px` | Grid multi-column activates |
| `breakpoint-mobile-max` | `max-width: 1023px` | Single column + sticky bar |

### 9.2 Breakpoint reference (project scale)

Use when block-specific tuning required: **1440 · 1310 · 1199 · 1024 · 767 · 660 · 580 · 490 · 390 · 370**.

**Primary switch only `1024`** unless block evidence requires intermediate (tablet = mobile layout unless ADR says otherwise).

### 9.3 Strategies

| Viewport | Strategy |
|----------|----------|
| **Desktop** ≥ 1024px | Multi-column grids; full header; no sticky bar |
| **Tablet** 768–1023px | **Mobile layout** (single column, sticky bar) — no separate tablet artboard in PDF |
| **Mobile** ≤ 1023px | Single column; 20px padding; reference math from 380px artboard |
| **Min supported** | 320px |

### 9.4 Responsive debt (unchanged)

| Item | Impact |
|------|--------|
| PG-009 Article mobile | No mockup — strategy open |
| PG-008 Blog hub | Misnamed mobile file |
| Missing pages M-01…M-06 | Placeholder or defer |

---

## 10. Excel Structure Intake

**Source file:** `Предварит структура и спрос.xlsx`  
**Location:** `INCOMING/02_CONTENT/Предварит структура и спрос.xlsx`  
**Size:** 14 102 bytes  
**Modified:** 2026-06-13 03:34:52  
**Sheet:** `Структура` (53 rows × 5 columns: URL + levels 1–4)  
**Status:** **INTAKE COMPLETE** — 2026-06-13

**Search performed (2026-06-13):**

- `FP-0002-SHPIGOVSKY/INCOMING/02_CONTENT/` — **found**
- `FP-0002-SHPIGOVSKY/INCOMING/08_CLIENT_MATERIALS/` — empty (README only)
- `C:\AI MARS STORAGE\` — no duplicate

### 10.1 Already Covered (Page Inventory baseline)

| Excel node | Page Inventory | Match |
|------------|----------------|-------|
| `/` — Главная | FP-0002-PG-001 | ✓ Design Ready (Home v2) |
| `/uslugi/` — Услуги | FP-0002-PG-002 | ✓ Service Hub |
| `/uslugi/zavisimosti/` — Зависимости и пристрастия | FP-0002-PG-003 | ✓ Service Section (PDF example) |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | FP-0002-PG-004 | ✓ Service Leaf (PDF example) |
| Категории: Психическое здоровье, РПП | Page Inventory §4.2 | ✓ Visible in hub PDF |
| `/uslugi/genotipirovanie/` — Генотипирование | Page Inventory §4.3 + M-05 | ✓ Direction confirmed; URL now explicit |
| `/o-centre/` — О центре | FP-0002-PG-005 | ✓ About (single PDF) |
| `/otzyvy/` — Отзывы | FP-0002-PG-007 | ✓ Reviews Archive |
| `/blog/` — Статьи | FP-0002-PG-008 / PG-009 | ✓ Blog hub + article template |
| `/kontakty/` — Контакты | FP-0002-PG-006 | ✓ Contacts |
| `/pravovaya-informaciya-pilzovatelyu/` — Правовая информация | FP-0002-PG-010 | ✓ Legal Hub |
| `/specyalisty/` — Специалисты | M-01 | ✓ Missing Pages Register — URL confirmed |

### 10.2 New Structure Information (not in Page Inventory)

| # | Excel finding | Inventory gap | Notes |
|---|---------------|---------------|-------|
| N-01 | **4 уровня** в дереве услуг (URL depth до 4) | Inventory: 3 уровня (hub → section → leaf) | Под `лечение-наркотической-зависимости/` — 4 leaf: soli, matadon, geroin, lekarstva; под `лечение-поведенческой-зависимости/` — 4 leaf: ludomaniya, internet-zavisimost, sozavisimost, shopogolizm |
| N-02 | **Полный перечень leaf-услуг** (зависимости) | Inventory: только примеры | 3 section-level + 10+ leaf URLs в Excel |
| N-03 | **Психическое здоровье** — 6 leaf | Section в hub PDF only | depressiya, ptsr, emotsionalnoe-vygoranie, trevozhnye-rasstroystva, rasstroystva-sna, travma |
| N-04 | **РПП** — 3 leaf | Section в hub PDF only | anoreksiya, buliniya, kompulsivnoe-pereedanie |
| N-05 | **Генотипирование** — `/uslugi/genotipirovanie/` | M-05: формат страницы SAFE UNKNOWN | Standalone section URL; **не** подраздел другой категории — согласуется с PROJECT DECISION |
| N-06 | **Специалисты** — hub + 6 профилей | M-01: нет PDF | shipovsky, kazakov, kostyuk + placeholders 4–6 |
| N-07 | **О центре** — 6 подстраниц | PG-005: один PDF | o-nas, programma-lecheniya, galereya-o-dome, specialistam, rodstvennikam, intervyu-i-smi |
| N-08 | Placeholder rows `Название` | — | Зарезервированные слоты в Excel (зависимости ×2, псих. здоровье ×3) |
| N-09 | Typo URLs | — | `specyalisty` (не specialists); `pravovaya-informaciya-pilzovatelyu//` (двойной slash); trailing spaces в некоторых URL |

### 10.3 URL Information (confirmed slugs)

| Level | Pattern | Examples |
|-------|---------|------------|
| L0 | `/` | Home |
| L1 | `/uslugi/`, `/specyalisty/`, `/o-centre/`, `/otzyvy/`, `/blog/`, `/kontakty/`, `/pravovaya-informaciya-pilzovatelyu/` | Top nav IA |
| L2 services | `/uslugi/{section}/` | zavisimosti, psihicheskoe-zdorovie, rasstroystva-pischevogo-povedeniya, **genotipirovanie** |
| L3 services | `/uslugi/{section}/{leaf}/` | lechenie-alkogolnoy-zavisimosti, depressiya, anoreksiya, … |
| L4 services | `/uslugi/.../.../{sub-leaf}/` | soli, ludomaniya, … |
| L2 specialists | `/specyalisty/{slug}/` | shipovsky, kazakov, kostyuk |
| L2 about | `/o-centre/{sub}/` | o-nas, programma-lecheniya, … |
| L2 blog | `/blog/nazvanie-stati/` | Placeholder article slug |

**Domain:** `https://shpigovsky.ru/` — confirmed in Excel column A.

### 10.4 IA Impact (future architecture — intake only)

| Impact | Detail |
|--------|--------|
| Service depth | Production IA **глубже** PDF-шаблонов: до **4 URL-уровней** под «Зависимости» |
| Genotipirovanие | Параллельное направление с **собственным URL** `/uslugi/genotipirovanie/` — не вложено в zavisimosti/psihicheskoe/rpp |
| About expansion | «О центре» — **hub + 6 child pages**; PDF даёт только один экран |
| Specialists | **Отдельный раздел** с листингом и single-профилями — подтверждает M-01 |
| Placeholder slots | Excel содержит `Название` — финальный перечень услуг **не закрыт** |
| URL hygiene | Slug typos (`specyalisty`, `pilzovatelyu`, double `//`) — требуют SEO/ops нормализации **до** production deploy |

**Rule:** Excel intake **не** переписывает Page Inventory в данной задаче; divergences N-01…N-09 логируются для будущего IA charter.

### 10.5 Frontend Impact (layout / navigation)

| Area | Impact |
|------|--------|
| Header top bar | Ссылка «Генотипирование» → `/uslugi/genotipirovanie/` (подтверждённый slug) |
| Header top bar | Ссылка «Специалисты» → `/specyalisty/` — **nav target confirmed**; page design still missing (M-01) |
| Service hub cards | Количество карточек и deep links **> PDF examples** — hub grid must accommodate variable count |
| Breadcrumbs | 4-level service paths need **4 crumb segments** — шаблон PG-003/PG-004 может потребовать расширения |
| About nav | In-page / sub-nav для 6 подстраниц — **нет PDF**; placeholder или reuse G-ABOUT TBD |
| Genotyping card (Home v2) | Destination URL **может** указывать на `/uslugi/genotipirovanie/` — closes partial M-05 |
| Service leaf templates | PG-004 template applies to **all** L3/L4 leaves; no new block types required |

### 10.6 WordPress / SEO-only Impact (later)

| Area | Impact |
|------|--------|
| CPT / taxonomy | Service tree mapping: sections, leaves, sub-leaves |
| URL redirects | Normalize `specyalisty`, legal double-slash, trailing spaces |
| Content volume | 20+ service pages, 6 about sub-pages, 6 specialist profiles — **content entry scope** |
| Blog | `/blog/nazvanie-stati/` — placeholder slug pattern |
| Legal expansion | Single hub URL; sub-documents (M-03/M-04) still without separate Excel rows |
| Sitemap | Full URL list from Excel drives future sitemap generation |

---

## 11. Search Demand Intake

**Source sheet:** `Спрос набросок` (52 query rows + header)  
**Column:** `Частотность МСК` (Moscow search volume)  
**Status:** **INTAKE COMPLETE** — 2026-06-13

**Scope:** intake only — **не** создавать SEO-структуру, **не** менять Page Inventory.

### 11.1 Primary demand clusters

| Cluster | Anchor queries (МСК) | Volume range |
|---------|------------------------|--------------|
| **A — Addiction treatment (umbrella)** | лечение зависимости (2666), центр лечения зависимостей (266), профилактика и лечение зависимости (181), центр профилактики зависимостей (175) | 175–2666 |
| **B — Alcohol** | лечение алкогольной зависимости (567), лечение алкогольной зависимости москва (53), лечение зависимости от алкоголя (30) | 30–567 |
| **C — Narcotic / substance** | лечение наркотической зависимости (58), лечение солевой зависимости (7), лечение метадоновой зависимости (7), лечение героиновой зависимости (7), лечение лекарственной зависимости (12) | 7–58 |
| **D — Behavioral / game** | лечение игровой зависимости (157), лечение интернет зависимости (50), лудомания лечение зависимости (25), азартная зависимость лечение (17) | 17–157 |
| **E — Center / geo / commercial** | лечение зависимости москва (162), центр лечения зависимостей москва (17), цена лечения зависимости (31), стоимость лечения зависимостей (10) | 10–162 |
| **F — Program / method** | психотерапия лечение зависимости (29), программы лечения зависимостей (25), виды лечения зависимостей (29) | 25–29 |

**Observation:** 100% запросов в листе относятся к кластеру **зависимости / реабилитация**. Запросов по **психическому здоровью**, **РПП** или **генотипированию** в листе **нет**.

### 11.2 Primary services (demand-confirmed)

| Service (demand signal) | Excel structure URL | Demand volume |
|-------------------------|---------------------|---------------|
| Лечение алкогольной зависимости | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 567 (+ geo variants) |
| Лечение наркотической зависимости (+ sub-types) | `/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/` + L4 | 58 + 7 each sub |
| Лечение игровой зависимости | `/uslugi/zavisimosti/.../ludomaniya/` | 157 |
| Интернет-зависимость | `/uslugi/zavisimosti/.../internet-zavisimost/` | 50 |
| Лечение лекарственной зависимости | L4 `lekarstva` | 12 |
| Центр / стационар (umbrella) | Hub `/uslugi/` + home | 74–2666 |

### 11.3 Genotyping page confirmation

| Aspect | Status |
|--------|--------|
| URL in Excel `Структура` | **Confirmed:** `/uslugi/genotipirovanie/` |
| Standalone section (not nested) | **Confirmed** — level-2 under `/uslugi/` |
| Search demand in `Спрос набросок` | **Not present** — no genotyping queries in sheet |
| Page Inventory alignment | **Confirmed** direction (§4.3); M-05 partial close (URL known, design still missing) |

**Conclusion:** Страница генотипирования **подтверждена структурой Excel**, но **не подтверждена спросом** в данном листе. SEO приоритет генотипирования — **SAFE UNKNOWN** до расширения keyword research.

### 11.4 Service structure confirmation (demand ↔ structure)

| Structure block | Demand support |
|-----------------|----------------|
| `/uslugi/zavisimosti/` + alcohol leaf | **Strong** — top volumes |
| Narcotic L3 + L4 sub-leaves | **Moderate** — parent 58; sub-leaves 7–12 each |
| Behavioral L3 + L4 (game, internet, shopogolizm) | **Moderate–strong** — game 157, internet 50 |
| `/uslugi/psihicheskoe-zdorovie/` + 6 leaves | **No demand data** in sheet |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` + 3 leaves | **No demand data** in sheet |
| `/uslugi/genotipirovanie/` | **Structure yes; demand no** |

**Do not** create SEO structure or copy from this section.

---

## 12. Production Decisions

| Decision ID | Decision | Owner | Status | Impact |
|-------------|----------|-------|--------|--------|
| PD-01 | Font family **Inter** (Google Fonts) | Olga → Andrei | **Approved** | Typography SSOT; closes font blocker |
| PD-02 | Container **1170px** | Olga → Andrei | **Approved** | Replaces Normalization 1160px |
| PD-03 | Colors from Olga (`#DAE5F0` @ 70%, `#475371`, `#B3261E`) | Olga → Andrei | **Approved** | Color SSOT; elevated/border fallbacks retained |
| PD-04 | Typography from Olga (H2 36/22 w500; body 18/16 w300) | Olga → Andrei | **Approved** | H1/H3/H4 from Normalization |
| PD-05 | Spacing scale 4/8/12…240 | Normalization → Andrei | **Approved** | Single spacing SSOT |
| PD-06 | Radius normalization (px-scale; 30% decorative-only) | Andrei | **Approved** | Prevents invalid global `%` radius |
| PD-07 | Breakpoint **1024px** desktop-first | Andrei | **Approved** | Layout switch SSOT |
| PD-08 | Excel structure + search demand **intake complete** (§10–11) | Andrei | **Approved (intake)** | Does **not** rewrite Page Inventory; IA charter deferred |
| PD-09 | Frontend Production may use **placeholder/demo pages** where design missing | Andrei | **Approved** | M-01, M-02, M-05, M-06; legal sub-pages; about sub-pages (N-07) |
| PD-10 | Card radius **16px** (`radius-md`) for coordinator soft-corner intent | Andrei | **Approved** | Override Normalization 8px for cards only |
| PD-11 | Page background layered `rgba(218,229,240,0.7)` | Andrei | **Approved** | Implements 70% transparency correctly |
| PD-12 | Article TOC sidebar **280px** desktop placeholder | Normalization → Andrei | **Approved** | Until PG-009 mobile strategy closed |
| PD-13 | `page-padding-x-desktop` = **40px** (not 50px) | Andrei | **Approved** | Resolves v1 §3.1/§3.3 conflict; aligns Normalization `space-8`; v1 §3.1 50px was erroneous attribution |

---

## 13. Remaining Open Questions

| # | Question | Who decides | Blocks frontend start? |
|---|----------|-------------|------------------------|
| OQ-01 | Callback modal behavior (M-06) | Olga (Approval Sheet v2 §4) | **No** — implement tel: or stub modal; charter allows placeholder |
| OQ-02 | Review expand «Читать весь отзыв» (M-02) | Olga (Sheet v2 §7) | **No** — hide link or truncate in v1 |
| OQ-03 | Specialists page / nav links (M-01) | Olga (Sheet v2 §8) | **No** — stub `href="#"` or remove per coordinator |
| OQ-04 | Article mobile strategy (PG-009) | Olga (Sheet v2 §5) | **Partial** — blocks PG-009 mobile parity; desktop can proceed |
| OQ-05 | Icon source (SVG pack / sprite) | Ops + Andrei | **No** — inline SVG or placeholder icons in scaffold |
| OQ-06 | Logo / asset extraction from PDF | Ops + design | **No** for scaffold — **Yes** for pixel-perfect sign-off |
| OQ-07 | UI states (hover/focus/error/success) | Andrei + visual pass | **No** — engineering fallbacks in charter |
| OQ-08 | Home v2 duplicate blocks (UTP/hero) | Olga (Sheet v2 §2) | **No** — default: single instance (artifact assumption) |
| OQ-09 | Genotyping card destination (M-05) | Olga (Sheet v2 §3) | **Partially closed** | Excel confirms `/uslugi/genotipirovanie/`; design PDF still missing |
| OQ-10 | Contacts breadcrumb error | Olga (Sheet v2 §6) | **No** — fix to correct (engineering default) |
| OQ-11 | Header stack exact heights | Measure in Production | **No** — blocks precise offset only |
| OQ-12 | Excel structure + search demand | Olga + SEO lane | **Intake closed** in §10–11 — **IA charter still open** (4-level tree, about sub-pages, URL typos) |
| OQ-13 | PDF package in repo | Ops | **No** for token-based scaffold — **Yes** for final visual QA |
| OQ-14 | FAQ accordion single-open | Olga (C-10) | **No** — engineering default single-open |

---

## 14. Production Gate

### Question

Можно ли после этого документа запускать **FP-0002 FRONTEND PRODUCTION CHARTER**?

### Answer

**READY FOR FRONTEND PRODUCTION CHARTER**

**Conditions:**

1. **Андрей** подписывает этот документ (APPROVED / APPROVED WITH CORRECTIONS).
2. Production SSOT по токенам в §2–9 считается **замороженным** для charter; изменения — только через ADR + версия v2.
3. Открытые вопросы §13 **не блокируют** charter при policy PD-09 (placeholders).
4. Excel intake §10–11 **выполнен** — не блокер frontend scaffold; IA divergences (N-01…N-09) — отдельный SEO/IA трек.

### True blockers (none for charter — only for specific deliverables)

| Blocker | Scope | Mitigation |
|---------|-------|------------|
| PG-009 mobile | Article page mobile | Desktop-first; mobile strategy when Olga decides |
| Pixel-perfect QA | All pages | PDF package restore + asset extraction |
| SEO URL finality | Service leaf count, 4-level paths, URL typos | Excel intake done; **IA charter** for slug normalization |

### Not blockers

- Inter / colors / container / typography — **closed** via Olga facts + this document.
- Missing design pages — **placeholder policy** PD-09.
- Excel file — **intake complete**; IA rewrite still deferred per scope rule.

---

## 15. SAFE UNKNOWN

| # | Item | Impact | Verify by |
|---|------|--------|-----------|
| U-01 | ~~Excel absent~~ → **resolved v2** | §10–11 complete | — |
| U-02 | PDF package not in committed repo | Visual re-verification | Restore `INCOMING/01_DESIGN/` |
| U-03 | Header/top bar exact heights | Layout offset | Measure in Production |
| U-04 | Inter font-weight 300 availability | FOUT/render | Google Fonts load test |
| U-05 | Card radius 16px vs PDF 8px | Visual delta | Coordinator ack or revert to `radius-sm` |
| U-06 | `rgba` wash vs solid band sections | Section-type mapping | Per-block in Production |
| U-07 | Tablet-specific layout | None planned | 1024 switch only |
| U-08 | z-index stack (header/modal/sticky) | Layering | Production charter addendum |
| U-09 | Icon asset pipeline | Sprite vs inline | Asset intake |
| U-10 | Effective hex of 70% wash on non-white bases | Color consistency | Limit wash to white base |
| U-11 | Genotyping search demand | SEO priority | Extended keyword research beyond `Спрос набросок` |
| U-12 | Mental health / RPP demand | SEO priority | No queries in current Excel sheet |
| U-13 | Excel URL typos (`specyalisty`, `pilzovatelyu`, `//`) | Redirect/canonical | SEO/ops normalization before deploy |
| U-14 | About sub-pages (6) — no PDF | Layout template | Design charter or placeholder policy |
| U-15 | 4-level service breadcrumbs | PG-003/PG-004 template extension | Frontend Lead + IA charter |

---

## Approval record

| Field | Value |
|-------|-------|
| Document version | v2 |
| Supersedes | [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v1.md](FP-0002-PRODUCTION-STANDARDS-APPROVAL-v1.md) |
| Parent | FP-0002-FRONTEND-NORMALIZATION-v1 |
| Frontend Lead | Андрей — **PENDING SIGNATURE** |
| Approval outcome | ☐ APPROVED · ☐ APPROVED WITH CORRECTIONS · ☐ HOLD |
| Date | |

**v2 changes from v1:**

1. Excel intake §10–11 integrated from `INCOMING/02_CONTENT/Предварит структура и спрос.xlsx`.
2. Padding conflict resolved: `page-padding-x-desktop` = **40px** everywhere (PD-13).
3. SAFE UNKNOWN U-01 closed; U-11–U-15 added from Excel analysis.

**Corrections (if any):**

---

## Document control

| Field | Value |
|-------|-------|
| Version | v2 |
| Created | 2026-06-13 |
| Changed in this task | **Created:** `FP-0002-PRODUCTION-STANDARDS-APPROVAL-v2.md` from v1 + Excel sync + padding fix |
| Commit / push | Not performed |

---

**READY FOR FRONTEND PRODUCTION CHARTER**

*Engineering standards only. No Frontend Production, no code.*
