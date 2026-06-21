# FP-0002 — Frontend Normalization v1

**Document type:** Production Design System (normalization pass)  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-13  
**Coordinator:** PER-0010 — Ольга Дягилева  

**ATLAS:** ORG-0008 · PRJ-0012 · WEB-SHPIG-01 · DOM-SHPIG-01  

**Phase:** Frontend Normalization — **не** Frontend Production  

**Upstream (read-only):**

| Input | Role |
|-------|------|
| [FP-0002-FRONTEND-FOUNDATION-v1.md](FP-0002-FRONTEND-FOUNDATION-v1.md) | Layout, typography, color, component taxonomy |
| [FP-0002-NUMERIC-DESIGN-RULES-v2.md](FP-0002-NUMERIC-DESIGN-RULES-v2.md) | Raw Design Numbers (24 PDF extraction) |
| [FP-0002-DESIGN-APPROVAL-SHEET-v1.md](FP-0002-DESIGN-APPROVAL-SHEET-v1.md) | Coordinator decisions gate |
| PDF-макеты (24 файла) | Visual SoT — evidence in `REPORTS/fp0002-numeric-extraction-v2.json` |

**Evidence note:** PDF-пакет referenced in Foundation (`INCOMING/01_DESIGN/`) — **не присутствует в рабочей копии репозитория на момент нормализации**; все raw-значения взяты из v2 extraction JSON (полный прогон 24 PDF). Повторная pixel-верификация по файлам — **SAFE UNKNOWN** до восстановления пакета.

**Git status (до работы):** ветка `mars/post-cycle8-live-tests`, up to date с `origin`. Прочие изменения репозitorия не затрагивались. Commit / push **не выполнялись**.

**Scope:** перевод Raw Design Numbers → Production Design System. **Запрещено:** HTML, SCSS, JS, WordPress/ACF architecture, Frontend Production.

---

# REPORT — FP-0002 FRONTEND NORMALIZATION

## 1. Executive Summary

Numeric Validation (v2) зафиксировал **сырые** числа из 24 PDF. Website Factory для реализации требует **Production Numbers** — нормализованную, повторяемую систему с объяснёнными инженерными решениями.

**Метод нормализации:**

1. Сохранить **CONFIRMED** raw-значения, если они уже лежат на шкале 4/8 px или являются уникальными brand-сигналами (hero H1 70, accent `#B3261D`).
2. Схлопнуть **кластеры и альтернативы** (36/42 H2, 133/172 margins, 380/390 artboard) в меньшее число production-токенов.
3. Округлить **ESTIMATED** значения к ближайшему шагу production spacing scale, если визуальная дельта ≤ ~8 px.
4. Не проектировать «design grid 12 col» — только **инженерную сетку** для CSS Grid/Flex.

**Ключевые production-решения:**

| Domain | Raw signal (v2) | Production decision |
|--------|-----------------|---------------------|
| Desktop content width | 1020–1106 px cluster; symmetric proposal 1171 | **`1160 px`** max content |
| Desktop page inset | L172/R250 asymmetric median | **`40 px`** symmetric viewport padding |
| Mobile page inset | L41/R65 asymmetric | **`20 px`** symmetric |
| Section rhythm | mode 72 px | **`80 px`** standard section gap |
| Breakpoint | artboards 380 / 1437 only | **`1024 px`** layout switch (pending C-03) |
| Typography alts | H2 36+42, body 16+18 | **2-tier:** default + `alt` token each |
| Radius family | 6 + 8 mixed | **8 px** UI default; **0 / 4 / 12** scale |

**Статус:** Production Design System **готов к coordinator review**. Frontend Production Charter — **HOLD** до подписи Approval Sheet и закрытия content/behavior blockers.

---

## 2. Container Normalization

### 2.1 Artboards (reference frames — not CSS values)

| Parameter | Raw Value | Production Value | Reason |
|-----------|-----------|------------------|--------|
| Desktop design frame | **1437 px** | **1437 px** (reference only) | CONFIRMED во всех 12 desktop PDF; не используется как `max-width` — только как evidence frame |
| Mobile design frame | **380 px** (11 files) + **390 px** (1 file) | **380 px** (reference) | Нормализация 390→380: один export artifact (`О центре - моб.pdf`); production mobile math ведётся от 380; C-03/C-12 — подтверждение координатором |
| Wide / full-bleed band | **1437 / 380 px** (= artboard) | **`100vw`** shell | Full-width backgrounds (hero, program, guest CTA) — viewport-wide, inner content inset via container tokens |

### 2.2 Content container

| Parameter | Raw Value | Production Value | Reason |
|-----------|-----------|------------------|--------|
| Desktop content width (median cluster) | **1020 px** (CW median 1010; range 897–1034) | — | Кластер отражает asymmetric margins, не целевую колонку |
| Desktop content width (Contacts ref) | **1106 px** (L133 + R198) | — | Outlier-friendly symmetric ref; не доминирует в 11/12 файлах |
| Desktop symmetric proposal (v2 ‡) | **1171 px** (1437 − 2×133) | **`1160 px`** | Округление к 8 px grid; между median cluster и Contacts; делится на 4/8; стабильнее для card grids `(1160 − 2×24) / 3 ≈ 371` |
| Mobile content width (median) | **274 px** (range 233–312) | **`340 px`** effective | При symmetric **`20 px`** padding: 380 − 40 = 340; шире raw на ~66 px — осознанный trade-off: убираем asymmetric 41/65, улучшаем читаемость; визуально ближе к «одна колонка по центру» |
| Production container token | — | **`container-max: 1160px`** | Единый `$container-max` для text + card grids |

### 2.3 Margins & padding

| Parameter | Raw Value | Production Value | Reason |
|-----------|-----------|------------------|--------|
| Desktop margin-left (median) | **172 px** | — | Asymmetric с R250 — не production pattern |
| Desktop margin-right (median) | **250 px** | — | Текстовые bbox не равны CSS padding |
| Desktop margin-left (Contacts) | **133 px** | — | Использован только как anchor для symmetric math |
| Desktop viewport padding-x | implicit 133–172 | **`40 px`** | Symmetric inset при viewport < 1160+80; на 1440 viewport: (1440−1160)/2 = **140 px** auto-center — padding token применяется только ниже breakpoint overflow |
| Mobile margin-left (mode) | **41 px** | — | Asymmetric |
| Mobile margin-right (mode) | **65 px** | — | Asymmetric |
| Mobile padding-x | 41 / 65 | **`20 px`** | Ближайший production spacing token; symmetric; 20×2 на шкале 4 px |
| Article TOC column | SAFE UNKNOWN | **`280 px`** fixed sidebar + **`1fr`** body | Engineering placeholder для PG-009 desktop: ~24% of 1160; **не** design grid — требует C-07 + visual pass |

### 2.4 Container model (production)

```
viewport (100%)
└─ page-padding-x (40 desktop / 20 mobile)
   └─ container-max 1160 (centered)
      ├─ content column (typography, forms, FAQ)
      └─ card grids (CSS grid, gap 24)
wide sections: background 100vw + same inner container-max
```

---

## 3. Typography Normalization

**Правило:** не вводить новые уровни без причины. Alt-тokens сохраняют подтверждённые raw-роли (hero H2 42, card H3 24).

### 3.1 Desktop

| Level | Raw Value | Production Value | Reason |
|-------|-----------|------------------|--------|
| **H1 / Display** | **70 px** | **70 px** | CONFIRMED BLK-007; brand scale — не округлять |
| **H2 primary** | **36 px** (dominant) | **36 px** | CONFIRMED; section titles |
| **H2 alt** | **42 px** (404, service hero) | **40 px** | Нормализация 42→40: 8 px grid; сохраняет hero/404 emphasis без третьего H2 token |
| **H3 primary** | **30 px** | **30 px** | CONFIRMED card titles |
| **H3 alt** | **24 px** | **24 px** | CONFIRMED steps/subsections |
| **H4** | **20 px** | **20 px** | CONFIRMED subheading/lead labels |
| **Body** | **16 px** (primary count) | **16 px** | CONFIRMED default body |
| **Body large** | **18 px** | **18 px** | CONFIRMED secondary paragraphs |
| **Small** | **14 px** | **14 px** | CONFIRMED UI/meta |
| **Caption** | **13 px** | **12 px** | 13→12: шкала 4 px; delta 1 px negligible at meta size |
| **Button** | **16 px** (estimated) | **16 px** | Align with body; CTA legibility |
| **Quote** | **18 px** (estimated) | **18 px** | BLK-022 expert quote = body-large scale |
| **Step number** | **26 px** | **24 px** | 26→24: unify with H3 alt rhythm; decorative numerals |

### 3.2 Mobile

| Level | Raw Value | Production Value | Reason |
|-------|-----------|------------------|--------|
| **H1 / Display** | **42 px** | **42 px** | CONFIRMED |
| **H2 primary** | **32 px** (estimated dominant) | **32 px** | Section titles below hero |
| **H2 alt** | **42 px** (sparse) | **40 px** | Match desktop alt normalization |
| **H3** | **22 / 24 px** | **22 px** default, **24 px** alt | Keep both confirmed clusters |
| **H4** | **18–20 px** | **18 px** | Mobile lead/subhead consolidation |
| **Body** | **16 px** | **16 px** | CONFIRMED |
| **Body large** | **18 px** | **18 px** | CONFIRMED |
| **Small** | **14 px** | **14 px** | CONFIRMED |
| **Caption** | **13 px** | **12 px** | Same as desktop |
| **Button** | **16 px** | **16 px** | — |
| **Top bar micro** | **10 px** | **12 px** | 10→12: minimum readable UI; rare spans |

### 3.3 Line-height (production)

| Level | Raw (v2) | Production | Reason |
|-------|----------|------------|--------|
| H1 (70) | 85 (1.22) | **84 px** (1.2) | Round to 4 px; tight display |
| H2 (36) | 44 (1.22) | **44 px** (1.22) | Keep — already on scale |
| H2 alt (40) | 51 from 42 raw | **48 px** (1.2) | Matches heading ratio |
| H3 (30) | 36 (1.20) | **36 px** (1.2) | — |
| Body (16) | 20 (1.25) | **24 px** (1.5) | RU long-read + MARS typography discipline; raw 1.25 tight for production |
| Body large (18) | 22 (1.22) | **28 px** (~1.56) | Round 27→28 on 4 px grid |
| Small (14) | 17 | **20 px** | font-size + 6 ≈ readable UI |
| Caption (12) | 16 from 13 raw | **16 px** (1.33) | — |

**Font families:** остаётся **SAFE UNKNOWN** — нормализация не назначает шрифт (C-02).

---

## 4. Spacing Scale

### 4.1 Production spacing tokens (4 px base)

| Token | Value (px) | Typical use |
|-------|------------|-------------|
| `space-0` | **0** | flush edges, divider collapse |
| `space-1` | **4** | micro gaps, icon nudge |
| `space-2` | **8** | tight inline stacks |
| `space-3` | **12** | compact component internal |
| `space-4` | **16** | FAQ item gap, form field gap, card internal minimum |
| `space-5` | **20** | mobile page padding-x |
| `space-6` | **24** | card grid gutter, card padding, program column gap |
| `space-7` | **32** | breadcrumb-to-hero, subsection gaps |
| `space-8` | **40** | desktop page padding-x, component vertical rhythm |
| `space-9` | **48** | large in-section stacks |
| `space-10` | **56** | raw medium section cluster → kept |
| `space-11` | **64** | section internal major |
| `space-12` | **80** | **standard section gap** (raw 72→80) |
| `space-13` | **96** | hero-adjacent spacing |
| `space-14` | **120** | CTA band padding vertical |
| `space-15` | **160** | large band transitions |
| `space-16` | **240** | full-bleed section transitions (raw 250→240) |

### 4.2 Raw → production mapping (section rhythm)

| Raw (v2) | Production token | Reason |
|----------|------------------|--------|
| **72 px** (mode, 33 hits) | **`space-12` = 80 px** | Example rule: улучшает 8 px grid; +8 px delta imperceptible at section scale |
| **56 px** | **`space-10` = 56 px** | Already on scale |
| **32 px** | **`space-7` = 32 px** | Breadcrumb gap — confirmed cluster |
| **16 px** | **`space-4` = 16 px** | FAQ/form — keep |
| **250 px** band | **`space-16` = 240 px** | Background band transition |
| **788 px** XL boundary | **`640 px`** (`space-12`×8) | One-off hero/footer boundaries → nearest large modular step; avoid orphan 788 |

---

## 5. Radius Scale

### 5.1 Production radius tokens

| Token | Value | Usage |
|-------|-------|-------|
| `radius-none` | **0** | full-bleed images edge-to-edge, divider squares |
| `radius-xs` | **4** | pagination hover chips, subtle tags |
| `radius-sm` | **8** | **default UI:** buttons, inputs, cards, FAQ panels |
| `radius-md` | **12** | optional elevated cards (if visual pass confirms) — **fallback = sm** |
| `radius-full` | **50%** | specialist avatars BLK-026 |

### 5.2 Raw → production

| Element | Raw | Production | Reason |
|---------|-----|------------|--------|
| Primary button | **6 px** | **`radius-sm` 8 px** | Unify with cards/inputs; 6 not on 4 px scale |
| Input | **6 px** | **8 px** | Match button family |
| Card | **8 px** | **8 px** | Keep |
| FAQ panel | **8 px** | **8 px** | Keep |
| Avatar | **50%** | **50%** | Keep |

---

## 6. Grid Normalization

**Принцип:** инженерная CSS-система, не реконструкция Figma grid.

| Parameter | Raw | Production | Reason |
|-----------|-----|------------|--------|
| Production container | 1020–1171 range | **`1160 px`** | See §2 |
| Content container | = container-max | **`1160 px`** | Single column max for typography |
| Grid gutter | **24 px** | **`24 px`** (`space-6`) | CONFIRMED derived pitch; on scale |
| 3-column cards | pitch ~510 | **`repeat(3, 1fr)`** gap 24 | At 1160: column ≈ 371 px — within raw card width family |
| 4-column cards | pitch ~24 gap | **`repeat(4, 1fr)`** gap 24 | Program BLK-020, specialists BLK-026 |
| 2-column form | desktop 2-col | **`repeat(2, 1fr)`** gap 16 | Form BLK-035; field gap `space-4` |
| Mobile columns | **1** | **1** | CONFIRMED all mobile PDF |
| Grid behavior | hybrid stack | **CSS Grid** for card layouts; **Flex** for nav/header; **vertical stack** for long-scroll sections | Matches Foundation §2.3 without inventing 12-col |
| Breakpoint switch | none in PDF | **`min-width: 1024px`** desktop grid | Engineering default; **pending C-03** — documented as production recommendation, not final until signed |

### 6.1 Column counts (production)

| Context | Desktop cols | Mobile cols | Gap |
|---------|--------------|-------------|-----|
| UTP BLK-009 | 3 | 1 | 24 |
| Service preview BLK-010 | 4 | 1 | 24 |
| Service hub BLK-011 | 3 | 1 | 24 |
| Features BLK-014 | 3 | 1 | 24 |
| Specialists BLK-026 | 4 | 1 | 24 |
| Reviews preview BLK-015 | 3 | 1 | 24 |
| Articles BLK-028 | 3 | 1 | 24 |
| Program BLK-020 | 4 | 1 | 24 |
| Rehab steps BLK-018 | 4 | 1 | 24 |
| Form BLK-035 | 2 | 1 | 16 |

---

## 7. Component Normalization

### 7.1 Buttons

| Parameter | Raw | Production | Reason |
|-----------|-----|------------|--------|
| Primary height | **44 px** | **44 px** | Meets min touch; confirmed CTA scan |
| Primary padding-x | **32 px** | **32 px** | On scale |
| Primary padding-y | **12 px** | **12 px** | Derived — keep |
| Hero CTA width | **324 px** fixed | **`min-width: 280px`**, auto width | Fluid container; avoids overflow on narrow desktop |
| Inline CTA height | **44 px** | **44 px** | Same family |
| Header callback | SAFE UNKNOWN | **height 40 px**, **padding-x 24 px** | Compact nav — engineering default until BLK-002 measure |
| Sticky mobile bar | 33% × 3 | **`flex: 1`** each action | Equal thirds preserved |
| Sticky touch target | **48 px** estimated | **48 px** min-height | WCAG-aligned |
| Border width | 1 | **1 px** | Keep |

### 7.2 Inputs

| Parameter | Raw | Production | Reason |
|-----------|-----|------------|--------|
| Height | **48 px** | **48 px** | Matches form field scan |
| Padding-x | **16 px** | **16 px** | `space-4` |
| Padding-y | **12 px** | **12 px** | Vertical centering |
| Border | **1 px** | **1 px** | Keep |
| Radius | 6→ | **8 px** | Unified `radius-sm` |

### 7.3 Textarea

| Parameter | Raw | Production | Reason |
|-----------|-----|------------|--------|
| Min-height | **120 px** | **128 px** | 120→128: 8 px grid; +8 px negligible |
| Width | 100% | **100%** | — |

### 7.4 Cards

| Parameter | Raw | Production | Reason |
|-----------|-----|------------|--------|
| Internal padding | **24 px** | **24 px** | `space-6` |
| Border | **1 px** `#CBD4E0` | **1 px** | Keep token |
| Radius | **8 px** | **8 px** | — |
| Shadow | none/flat | **none** | CONFIRMED flat design |
| Service image aspect | **16:10** est. | **`16 / 10`** | Preserve derived ratio |

### 7.5 FAQ (BLK-034)

| Parameter | Raw | Production | Reason |
|-----------|-----|------------|--------|
| Item gap | **16 px** | **16 px** | `space-4` |
| Panel radius | **8 px** | **8 px** | — |
| Chevron icon | **16 px** | **16 px** | — |
| Behavior | — | accordion single-open | C-10 — implementation choice, not normalized size |

### 7.6 CTA patterns

| Pattern | Raw | Production | Reason |
|---------|-----|------------|--------|
| Guest visit band BLK-019 | full artboard | **100vw bg + container 1160** | Standard wide section |
| Inline BLK-025 | auto | **primary button** tokens | Reuse button family |
| Mobile sticky BLK-004 | bar height unknown | **56 px** bar height | Engineering: 48 touch + 8 padding; **pending visual** |
| Pagination BLK-017 | **40×40** | **40×40** | Keep square cells |

---

## 8. Color Review

**Вывод:** полный редизайн **не требуется**. Нормализация = **схлопнуть ESTIMATED дубликаты** к CONFIRMED anchors.

| Token | Raw (v2) | Production | Change? | Reason |
|-------|----------|------------|---------|--------|
| `primary-accent` | `#B3261D` | **`#B3261D`** | No | CONFIRMED CTA/footer |
| `primary-dark` | `#455069` / `#444F68` | **`#455069`** | **Yes** — merge | Single chrome token |
| `text-primary` | `#3B3D3D` | **`#3D3D3D`** | Minor | Average of cluster |
| `text-muted` | `#8D9097` | **`#8D9097`** | No | Keep ESTIMATED until C-11 |
| `text-on-primary` | `#FFFFFF` | **`#FFFFFF`** | No | Inferred contrast |
| `bg-page` | `#E3EAF2` / `#E4EBF3` | **`#E3EAF2`** primary, **`#E4EBF3`** alt | No | Both CONFIRMED — dual wash intentional |
| `bg-elevated` | `#F1F5F9` | **`#F1F5F9`** | No | Card surfaces |
| `bg-footer` | `#E2E8EF` | **`#E2E8EF`** | No | — |
| `border-subtle` | `#C6CEDA` | **`#C6CEDA`** | No | — |
| `border-card` | `#CBD4E0` | **`#CBD4E0`** | No | — |
| `accent-warm` | `#9E9694` | **`#9E9694`** | No | — |

**Hover / focus / error / success:** не в PDF — **не нормализованы**; production placeholders deferred to Frontend Production with C-13.

---

## 9. Production Tokens

Только production значения. Статус: **PRODUCTION** = ready for SCSS token file after gate open.

| Design Token | Value | Status |
|--------------|-------|--------|
| `artboard-ref-desktop` | 1437 | REFERENCE |
| `artboard-ref-mobile` | 380 | REFERENCE |
| `breakpoint-desktop-min` | 1024 | PRODUCTION (pending C-03) |
| `container-max` | 1160 | PRODUCTION |
| `page-padding-x-desktop` | 40 | PRODUCTION |
| `page-padding-x-mobile` | 20 | PRODUCTION |
| `grid-gap-default` | 24 | PRODUCTION |
| `grid-gap-form` | 16 | PRODUCTION |
| `section-gap-sm` | 32 | PRODUCTION |
| `section-gap-md` | 56 | PRODUCTION |
| `section-gap-lg` | 80 | PRODUCTION |
| `section-gap-band` | 240 | PRODUCTION |
| `font-size-h1-desktop` | 70 | PRODUCTION |
| `font-size-h1-mobile` | 42 | PRODUCTION |
| `font-size-h2` | 36 | PRODUCTION |
| `font-size-h2-alt` | 40 | PRODUCTION |
| `font-size-h3` | 30 | PRODUCTION |
| `font-size-h3-alt` | 24 | PRODUCTION |
| `font-size-h4` | 20 | PRODUCTION |
| `font-size-h4-mobile` | 18 | PRODUCTION |
| `font-size-body` | 16 | PRODUCTION |
| `font-size-body-lg` | 18 | PRODUCTION |
| `font-size-small` | 14 | PRODUCTION |
| `font-size-caption` | 12 | PRODUCTION |
| `font-size-button` | 16 | PRODUCTION |
| `font-size-quote` | 18 | PRODUCTION |
| `line-height-h1` | 84 | PRODUCTION |
| `line-height-h2` | 44 | PRODUCTION |
| `line-height-h2-alt` | 48 | PRODUCTION |
| `line-height-h3` | 36 | PRODUCTION |
| `line-height-body` | 24 | PRODUCTION |
| `line-height-body-lg` | 28 | PRODUCTION |
| `radius-none` | 0 | PRODUCTION |
| `radius-xs` | 4 | PRODUCTION |
| `radius-sm` | 8 | PRODUCTION |
| `radius-md` | 12 | PRODUCTION |
| `radius-full` | 50% | PRODUCTION |
| `button-height` | 44 | PRODUCTION |
| `button-padding-x` | 32 | PRODUCTION |
| `button-min-width` | 280 | PRODUCTION |
| `input-height` | 48 | PRODUCTION |
| `input-padding-x` | 16 | PRODUCTION |
| `textarea-min-height` | 128 | PRODUCTION |
| `card-padding` | 24 | PRODUCTION |
| `sticky-bar-height-mobile` | 56 | PRODUCTION |
| `pagination-cell` | 40 | PRODUCTION |
| `color-primary-accent` | #B3261D | PRODUCTION |
| `color-primary-dark` | #455069 | PRODUCTION |
| `color-text-primary` | #3D3D3D | PRODUCTION |
| `color-text-muted` | #8D9097 | PRODUCTION |
| `color-text-on-primary` | #FFFFFF | PRODUCTION |
| `color-bg-page` | #E3EAF2 | PRODUCTION |
| `color-bg-page-alt` | #E4EBF3 | PRODUCTION |
| `color-bg-elevated` | #F1F5F9 | PRODUCTION |
| `color-bg-footer` | #E2E8EF | PRODUCTION |
| `color-border-subtle` | #C6CEDA | PRODUCTION |
| `color-border-card` | #CBD4E0 | PRODUCTION |
| `color-accent-warm` | #9E9694 | PRODUCTION |
| `article-sidebar-width` | 280 | PRODUCTION (placeholder) |

---

## 10. Approval Impact

Сопоставление с [FP-0002-DESIGN-APPROVAL-SHEET-v1.md](FP-0002-DESIGN-APPROVAL-SHEET-v1.md):

| Sheet item | После нормализации | Статус |
|------------|-------------------|--------|
| **C-02** Font source | Не закрыт — tokens не включают font-family | **Остаётся для Ольги** |
| **C-03** Breakpoint | Production **рекомендует 1024**; требует подписи | **Pre-filled recommendation — решение Ольги** |
| **C-04** Home v2 duplicates | Не относится к numeric normalization | **Остаётся для Ольги** |
| **C-05** Генотипирование URL | Content/IA | **Остаётся для Ольги** |
| **C-06** Contacts breadcrumb | Content bug | **Остаётся для Ольги** |
| **C-07** Article mobile | Sidebar placeholder 280 px — не заменяет mobile mockup | **Остаётся для Ольги** |
| **C-08** Blog mobile filename | Ops | **Остаётся для Ольги** |
| **C-09** Modal callback | Behavior | **Остаётся для Ольги** |
| **C-10** FAQ accordion | Behavior | **Остаётся для Ольги** |
| **C-11** ESTIMATED colors | Normalization merge `#455069`; muted unchanged | **Частично подготовлено — финальное OK Ольги** |
| **C-14** Review expand | Behavior scope | **Остаётся для Ольги** |
| **C-15** Container padding | Normalization **рекомендует 1160 + symmetric padding** вместо 1171/1020/1106 | **Pre-filled recommendation — решение Ольги** |
| **390 vs 380** (§6 sheet) | Normalization → **380 reference** | **Pre-filled — подтверждение Ольги** |

**Закрыто нормализацией (не требует отдельного design decision, только ack):**

- Production spacing scale (§4)
- Production radius scale (§5)
- Grid gutter 24 / form gap 16
- Typography tier consolidation (alt tokens documented)
- Section gap 72→80 engineering choice
- Button/input radius unification 8 px

**Numeric Rules v2 approval:** нормализация **не заменяет** подпись v2; она **надстраивает** production layer. Coordinator подписывает Approval Sheet + ack этого документа.

---

## 11. Frontend Production Readiness

### Можно ли запускать Frontend Production Charter?

**Нет — HOLD.**

### Blockers (реальные)

| # | Blocker | Owner |
|---|---------|-------|
| B-01 | Approval Sheet **не подписан** (C-02…C-15) | PER-0010 |
| B-02 | **Font family** не назначен | C-02 |
| B-03 | **Breakpoint** production 1024 — не signed | C-03 |
| B-04 | **Container 1160** — production decision vs sheet options | C-15 |
| B-05 | **PG-009 mobile** — no mockup | C-07 |
| B-06 | **Modal M-06**, **review expand M-02** — behavior scope | C-09, C-14 |
| B-07 | **UI states** hover/focus/error | C-13 |
| B-08 | **Header stack heights** — SAFE UNKNOWN | measure in Production or design addendum |
| B-09 | **PDF package** not in repo — re-verification risk | ops / evidence restore |
| B-10 | **Icon asset source** — SAFE UNKNOWN | asset intake |

### После закрытия

1. Coordinator: Approval Sheet → APPROVED / APPROVED WITH CORRECTIONS  
2. Ack `FP-0002-FRONTEND-NORMALIZATION-v1.md` (или corrections inline)  
3. ADR entries in `DECISIONS.md`  
4. **Then** Frontend Production Charter allowed  

---

## 12. SAFE UNKNOWN

| # | Item | Impact |
|---|------|--------|
| U-01 | Font files / CDN | Cannot compile final typography |
| U-02 | PDF files absent from workspace | Cannot re-run visual diff |
| U-03 | Header/top bar exact heights | Layout offset calculations |
| U-04 | Sticky bar BLK-004 exact raw height | Normalized 56 px is engineering estimate |
| U-05 | Article TOC ratio desktop | 280 px placeholder |
| U-06 | Anchor nav mobile control BLK-006 | Interaction spec |
| U-07 | Hover/focus/error colors | Interaction CSS |
| U-08 | z-index stack | Layering |
| U-09 | Header callback button raw dims | Used 40×24 engineering default |
| U-10 | Intermediate breakpoints tablet | Only 380/1437 artboards — tablet is extrapolation |

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Supersedes | — (first normalization) |
| Parent | FP-0002-NUMERIC-DESIGN-RULES-v2 |
| Companion | FP-0002-DESIGN-APPROVAL-SHEET-v1 |
| Changed in this task | **Created:** `FP-0002-FRONTEND-NORMALIZATION-v1.md` |
| Commit / push | Not performed |

---

**READY FOR FINAL COORDINATOR REVIEW**

*Normalization only. No Frontend Production, no code.*
