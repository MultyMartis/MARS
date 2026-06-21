# FP-0002 — Production Standards Approval v1

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
| `Предварит структура и спрос.xlsx` | SEO/IA intake — **SAFE UNKNOWN** (файл не найден в workspace) |

**Git status (до работы):** ветка `mars/post-cycle8-live-tests`, up to date с `origin`. Прочие изменения репозитория не затрагивались. Commit / push **не выполнялись**.

**Scope:** утверждение production-стандартов вёрстки. **Запрещено:** HTML, SCSS, JS, изменение Page Inventory, Block Inventory, WordPress Architecture, ACF Architecture.

**Supersedes (partial):** container `1160px` из Normalization → **`1170px`** (coordinator-confirmed).

---

# REPORT — FP-0002 PRODUCTION STANDARDS APPROVAL

## 1. Executive Summary

Создан инженерный документ **Production Standards Approval v1** — SSOT для статической вёрстки Shpigovsky.ru под стек HTML · SCSS · JS · Gulp · gulp-file-include.

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

**Excel intake:** файл `Предварит структура и спрос.xlsx` **не обнаружен** в `C:\AI MARS`, `C:\AI MARS STORAGE`, `FP-0002-SHPIGOVSKY/INCOMING/`. Разделы §10–11 зафиксированы как **SAFE UNKNOWN** с шаблоном intake.

**Статус документа:** ожидает подписи **Андрея** (Project Lead / Frontend Lead).

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
| `page-padding-x-desktop` | **50px** | Normalization | Symmetric viewport inset below overflow |
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
**Expected sheet:** `Структура`  
**Status:** **SAFE UNKNOWN — file not found in workspace**

**Search performed (2026-06-13):**

- `C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\` — no `.xlsx`
- `C:\AI MARS STORAGE\` — no match
- `FP-0002-SHPIGOVSKY/INCOMING/02_CONTENT/`, `08_CLIENT_MATERIALS/` — **Empty — Awaiting Intake**

**Required action:** place file in `INCOMING/08_CLIENT_MATERIALS/` or `INCOMING/02_CONTENT/` and re-run intake.

### 10.1 Intake template (pending file)

When file is available, record:

| Field | Value |
|-------|-------|
| New/clarified pages | TBD |
| Nesting levels | TBD |
| URL slugs | TBD |
| Divergence vs [FP-0002-PAGE-INVENTORY-v1.md](FP-0002-PAGE-INVENTORY-v1.md) | TBD |
| Frontend layout impact | TBD |
| WordPress/SEO-only impact | TBD |

### 10.2 SEO Structure Impact (preliminary — Page Inventory baseline only)

Without Excel, **only inventory-confirmed** frontend impact:

| Area | Page Inventory | Excel impact (when file arrives) |
|------|----------------|----------------------------------|
| Service tree depth | 3 levels + генотипирование parallel | May expand leaf count / URLs — **SEO/IA only** until design exists |
| Missing M-01 Specialists | No PDF | Excel may confirm URL — **nav link behavior** affects header |
| Missing M-05 Genotyping page | No PDF | Excel may confirm standalone URL — **card/hub links** |
| Legal expansion M-03/M-04 | Hub only in PDF | Excel likely **WordPress-only** first |
| Blog/articles | PG-008/009 confirmed | Excel may add article categories — **SEO later** |

**Rule:** Excel intake **does not** rewrite Page Inventory in this task; divergences logged for future IA charter.

---

## 11. Search Demand Intake

**Expected sheet:** `Спрос набросок`  
**Status:** **SAFE UNKNOWN — file not found**

### 11.1 Intake template (pending file)

| Field | Value |
|-------|-------|
| Primary demand themes | TBD |
| Query groups | TBD |
| Service pages confirmed by demand | TBD |
| Pages requiring future SEO attention | TBD |

### 11.2 Preliminary signals (Page Inventory + design only — not search data)

Until Excel arrives, **no search-demand claims**. Service categories visible in PDF mockups (not demand-validated):

- Зависимости и пристрастия
- Психическое здоровье
- РПП
- Генотипирование (parallel direction)

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
| PD-08 | Excel structure accepted as **future SEO/IA input** | Andrei | **Deferred** | File missing; no inventory rewrite |
| PD-09 | Frontend Production may use **placeholder/demo pages** where design missing | Andrei | **Approved** | M-01, M-02, M-05, M-06; legal sub-pages |
| PD-10 | Card radius **16px** (`radius-md`) for coordinator soft-corner intent | Andrei | **Approved** | Override Normalization 8px for cards only |
| PD-11 | Page background layered `rgba(218,229,240,0.7)` | Andrei | **Approved** | Implements 70% transparency correctly |
| PD-12 | Article TOC sidebar **280px** desktop placeholder | Normalization → Andrei | **Approved** | Until PG-009 mobile strategy closed |

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
| OQ-09 | Genotyping card destination (M-05) | Olga (Sheet v2 §3) | **No** — stub link until URL confirmed |
| OQ-10 | Contacts breadcrumb error | Olga (Sheet v2 §6) | **No** — fix to correct (engineering default) |
| OQ-11 | Header stack exact heights | Measure in Production | **No** — blocks precise offset only |
| OQ-12 | Excel structure + search demand | Olga + SEO lane | **No** for frontend scaffold — **Yes** for SEO charter |
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
4. Excel intake §10–11 **откладывается** на SEO/IA трек — не блокер frontend scaffold.

### True blockers (none for charter — only for specific deliverables)

| Blocker | Scope | Mitigation |
|---------|-------|------------|
| PG-009 mobile | Article page mobile | Desktop-first; mobile strategy when Olga decides |
| Pixel-perfect QA | All pages | PDF package restore + asset extraction |
| SEO URL finality | Service leaf count | Excel intake when file provided |

### Not blockers

- Inter / colors / container / typography — **closed** via Olga facts + this document.
- Missing design pages — **placeholder policy** PD-09.
- Excel file absent — **SEO deferral**, not frontend SSOT gap.

---

## 15. SAFE UNKNOWN

| # | Item | Impact | Verify by |
|---|------|--------|-----------|
| U-01 | `Предварит структура и спрос.xlsx` absent | §10–11 incomplete | Place file in INCOMING |
| U-02 | PDF package not in committed repo | Visual re-verification | Restore `INCOMING/01_DESIGN/` |
| U-03 | Header/top bar exact heights | Layout offset | Measure in Production |
| U-04 | Inter font-weight 300 availability | FOUT/render | Google Fonts load test |
| U-05 | Card radius 16px vs PDF 8px | Visual delta | Coordinator ack or revert to `radius-sm` |
| U-06 | `rgba` wash vs solid band sections | Section-type mapping | Per-block in Production |
| U-07 | Tablet-specific layout | None planned | 1024 switch only |
| U-08 | z-index stack (header/modal/sticky) | Layering | Production charter addendum |
| U-09 | Icon asset pipeline | Sprite vs inline | Asset intake |
| U-10 | Effective hex of 70% wash on non-white bases | Color consistency | Limit wash to white base |

---

## Approval record

| Field | Value |
|-------|-------|
| Document version | v1 |
| Supersedes | Normalization container 1160px (partial) |
| Parent | FP-0002-FRONTEND-NORMALIZATION-v1 |
| Frontend Lead | Андрей — **PENDING SIGNATURE** |
| Approval outcome | ☐ APPROVED · ☐ APPROVED WITH CORRECTIONS · ☐ HOLD |
| Date | |

**Corrections (if any):**

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Created | 2026-06-13 |
| Changed in this task | **Created:** `FP-0002-PRODUCTION-STANDARDS-APPROVAL-v1.md` |
| Commit / push | Not performed |

---

**READY FOR FRONTEND PRODUCTION CHARTER**

*Engineering standards only. No Frontend Production, no code.*
