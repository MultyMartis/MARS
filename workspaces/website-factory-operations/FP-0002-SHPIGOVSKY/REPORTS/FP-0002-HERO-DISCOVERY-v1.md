# REPORT — FP-0002 HERO DISCOVERY v1

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-15  
**Phase:** HERO DISCOVERY (analysis only)  
**Visual SSOT:** `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg`  
**UI DEMO reference:** `workspaces/fp-0002-shpigovsky-frontend/dist/desktop-ui-demo.html` (UI DEMO v1 — ACCEPTED)  
**Constraints respected:** HTML / SCSS / JS / Hero build — **NOT created**. Header / footer / shell / dist — **NOT touched**.

**Sources NOT used (per charter):** PDF · старые Layout Spec · старые Hero-гипотезы · Design Audit · BLOCK inventory labels as structure truth.

---

## 1. Hero Boundary

### START OF HERO

Нижняя кромка **второй строки header** (nav-строка с пунктами меню и иконкой поиска).  
Hero начинается **сразу под header**, без промежуточной полосы.

### END OF HERO

Верхняя кромка **следующей секции** — белый фон страницы, центрированный заголовок **«МНОГОПРОФИЛЬНОЕ…»** (начало intro/features-блока).  
Hero заканчивается **до** этого белого контентного блока.

### Что входит в Hero

| # | Элемент | Описание |
|---|---------|----------|
| 1 | **Hero Background Media** | Full-width фотография: белое классическое здание клиники с башней, зелёные деревья, небо, газон |
| 2 | **Overlay Card** | Центрированная белая панель со скруглёнными углами поверх фото |
| 3 | **Label** | Мелкий uppercase-текст в верхней части overlay |
| 4 | **Main Heading** | Крупный заголовок (название клиники) в центре overlay |
| 5 | **CTA Primary** | Красная кнопка в нижней части overlay |

### Что НЕ входит в Hero

| Элемент | Причина исключения |
|---------|-------------------|
| Header (logo, контакт, CTA header, nav, search) | Находится **выше** START OF HERO |
| Секция «МНОГОПРОФИЛЬНОЕ…» и далее | Начинается **ниже** END OF HERO — белый фон, H2, абзац, список, сетка 6 карточек |
| Footer | Нижняя часть страницы |
| Любые блоки mid-page / form / FAQ / gallery | Вне границ Hero |

---

## 2. Group Register

Декомпозиция Hero **сверху вниз, слева направо**. Каждая визуально отдельная сущность — отдельный GROUP-ID.

| GROUP-ID | Название | Позиция | Визуальное описание |
|----------|----------|---------|---------------------|
| **GROUP-01** | Hero Background Media | Full-width, под header → до белой секции | Фоновое фото здания клиники; занимает всю ширину Hero; контент overlay не перекрывает боковые зоны фото |
| **GROUP-02** | Overlay Card Container | Центр Hero, поверх GROUP-01 | Белая прямоугольная панель со скруглёнными углами; визуально полупрозрачная / светлая; содержит GROUP-03…05 |
| **GROUP-03** | Label | Верх overlay, по центру | Мелкий uppercase-текст над заголовком |
| **GROUP-04** | Main Heading | Середина overlay, по центру | Крупный display-заголовок (название клиники) |
| **GROUP-05** | CTA Primary | Низ overlay, по центру | Одна красная кнопка с белым uppercase-текстом |

**Итого групп в Hero:** 5 (GROUP-01 … GROUP-05)

**Не обнаружено в JPG (отдельных групп нет):**

- Secondary CTA
- Form / input fields
- Icon row / badges row
- Отдельный subtitle / description paragraph между GROUP-04 и GROUP-05
- Thumbnail / avatar / logo внутри overlay
- Breadcrumb / nav внутри Hero

---

## 3. Content Lock

| GROUP-ID | Тип контента | Lock status | Locked value |
|----------|--------------|-------------|--------------|
| **GROUP-01** | Media (image) | LOCKED (visual) | Фото здания клиники — asset identity / filename: **UNKNOWN** (см. §6) |
| **GROUP-02** | Container (no text) | — | N/A |
| **GROUP-03** | Label text | **LOCKED** | `ЧАСТНАЯ ПСИХИАТРИЧЕСКАЯ КЛИНИКА` |
| **GROUP-04** | Main Heading text | **LOCKED** | `КОРСАКОВ` |
| **GROUP-05** | CTA button text | **LOCKED** | `ЗАПИСАТЬСЯ НА ПРИЕМ` |

**Content Lock summary:** 3 текстовые группы — **LOCKED**. 1 медиа-группа — визуально идентифицирована, файл-источник — **UNKNOWN**.

---

## 4. Geometry Discovery

### Row / Column model (Hero section)

| Parameter | Value |
|-----------|-------|
| **ROW COUNT (section level)** | **1** — одна full-width горизонтальная полоса Hero |
| **COLUMN COUNT (section level)** | **1** — фон на всю ширину; overlay — одна центральная колонка |
| **ROW COUNT (inside overlay)** | **3** — label → heading → button (вертикальный stack) |
| **COLUMN COUNT (inside overlay)** | **1** — всё содержимое overlay центрировано по одной оси |

### Visual Flow

```
[Header — NOT Hero]
        ↓
┌─────────────────────────────────────────────────────────┐
│  GROUP-01 Hero Background Media (full-width photo)      │
│                                                         │
│              ┌─────────────────────────┐                │
│              │ GROUP-02 Overlay Card   │                │
│              │  GROUP-03 Label         │                │
│              │  GROUP-04 Main Heading  │                │
│              │  GROUP-05 CTA Primary   │                │
│              └─────────────────────────┘                │
│                                                         │
└─────────────────────────────────────────────────────────┘
        ↓
[White section «МНОГОПРОФИЛЬНОЕ…» — NOT Hero]
```

**Порядок чтения:** фон (full bleed) → центральная карточка → сверху вниз: label → heading → CTA.

### Area map

| Area | Содержимое |
|------|------------|
| **TOP AREA** | Верх фото: небо, крыша / верхняя часть здания |
| **BOTTOM AREA** | Низ фото: газон, нижняя часть здания |
| **LEFT AREA** | Левая часть фото: деревья, боковой фасад |
| **RIGHT AREA** | Правая часть фото: деревья, боковой фасад |
| **CENTER AREA** | Overlay card (GROUP-02) + весь текстовый/CTA контент |

### Container model (frontend decomposition)

| Layer | Role |
|-------|------|
| **L1 — Hero wrapper** | Full-width section band; задаёт высоту Hero и clipping фона |
| **L2 — Background layer** | GROUP-01: image cover/center, 100% ширины |
| **L3 — Overlay positioning layer** | Центрирование GROUP-02 поверх L2 (horizontal + vertical center в пределах Hero) |
| **L4 — Overlay card** | GROUP-02: внутренний padding; border-radius; фон панели |
| **L5 — Content stack** | GROUP-03, GROUP-04, GROUP-05 — vertical flow, center-aligned |

**Exact px values (height, overlay width, padding, radius, opacity):** **UNKNOWN** — не измерялись с JPG в этом этапе.

---

## 5. Component Inventory

Сравнение паттернов Hero с **UI DEMO v1** (`desktop-ui-demo.html`).

| Component type | Hero instance | UI DEMO v1 | Status |
|----------------|-----------------|------------|--------|
| **Typography — display H1** | GROUP-04 «КОРСАКОВ» (крупный display) | Section 01: H1 tier (70px / 500) | **EXISTS IN UI DEMO** (tier); hero-specific sizing unverified |
| **Typography — label / small uppercase** | GROUP-03 «ЧАСТНАЯ ПСИХИАТРИЧЕСКАЯ КЛИНИКА» | Section 01: caption / small-ui tiers | **EXISTS IN UI DEMO** (tier); uppercase label pattern not demo'd as standalone |
| **Typography — paragraph** | — | Section 01: paragraph | N/A in Hero |
| **Button — primary red CTA** | GROUP-05 «ЗАПИСАТЬСЯ НА ПРИЕМ» | Section 02: `.btn--primary` | **EXISTS IN UI DEMO** |
| **Button — secondary / outline** | — | Section 02 | N/A in Hero |
| **Forms** | — | Section 03 | N/A in Hero |
| **Cards — standard** | — | Section 05: `.card--simple/content/contact` | N/A in Hero |
| **Cards — hero overlay panel** | GROUP-02 (semi-transparent white panel over photo) | No hero overlay variant | **MISSING IN UI DEMO** |
| **Badges — pill** | — | Section 06: `.badge` | N/A in Hero |
| **Labels — text label (non-pill)** | GROUP-03 | No dedicated label component | **MISSING IN UI DEMO** (as distinct component) |
| **Hero Media — full-bleed background** | GROUP-01 | No hero media / background demo | **MISSING IN UI DEMO** |
| **Breadcrumb / accordion / tabs / alert** | — | Section 06 | N/A in Hero |

### Summary

| Status | Count | Items |
|--------|-------|-------|
| **EXISTS IN UI DEMO** | 3 | Primary button tier; H1 typography tier; small/caption typography tier |
| **MISSING IN UI DEMO** | 3 | Hero overlay card pattern; text label (non-pill); full-bleed hero background media |
| **N/A in Hero** | — | Forms, standard cards, badges, secondary buttons, UI chrome |

---

## 6. Unknown Register

Только реальные UNKNOWN по JPG. Без дополнений и SEO-интерпретаций.

| ID | Subject | Reason |
|----|---------|--------|
| **U-01** | Hero section height (px) | JPG не даёт pixel measure; только визуальная пропорция |
| **U-02** | Overlay card width / height / padding / border-radius (px) | Видна форма, точные размеры не измерены |
| **U-03** | Overlay background color / opacity | Визуально светлая полупрозрачная панель; exact rgba — не locked |
| **U-04** | Background image asset (filename, crop, focal point) | Фото идентифицировано визуально; исходный файл в репозитории не верифицирован в этом этапе |
| **U-05** | Mobile / tablet Hero layout | JPG — desktop full-page; адаптив Hero не показан |
| **U-06** | Exact font-size / line-height / weight в overlay vs v3 tokens | Тiers в UI DEMO есть; pixel-match Hero overlay не измерялся |
| **U-07** | CTA uppercase — CSS `text-transform` vs literal caps in copy | Текст на кнопке читается как uppercase (**LOCKED**); механизм рендера — **UNKNOWN** |

**NOT listed as UNKNOWN (confirmed absent or locked):**

- Hero subtitle / description line — **не видна** как отдельная группа в JPG
- Secondary CTA — **отсутствует**
- Form in Hero — **отсутствует**
- GROUP-03 / GROUP-04 / GROUP-05 copy — **LOCKED** (читается уверенно)

---

## 7. Implementation Readiness

| Gate | Answer |
|------|--------|
| **HERO DISCOVERY COMPLETE** | **YES** |
| **GROUP REGISTER COMPLETE** | **YES** |
| **CONTENT LOCK COMPLETE** | **YES** |
| **GEOMETRY DISCOVERY COMPLETE** | **YES** (с оговоркой: px-геометрия → UNKNOWN, см. §6) |
| **READY FOR HERO LAYOUT SPEC** | **YES** |
| **READY FOR HERO BUILD** | **NO** |

---

## 8. Final Verdict

Hero на `HOME-PAGE-FULL-MOCKUP.jpg` — **одна full-width полоса** с фоновым фото здания и **центрированной overlay-карточкой**, содержащей **3 текстовые сущности** (label, heading, CTA) и **5 визуальных групп** (GROUP-01 … GROUP-05).

Границы Hero однозначны: **под header nav-row** → **до белой секции «МНОГОПРОФИЛЬНОЕ…»**.

UI DEMO v1 покрывает **базовые tiers** (H1, small text, primary button), но **не покрывает** hero-specific паттерны: full-bleed background, overlay card, standalone text label.

Discovery завершён. **Hero Layout Spec / Hero Assembly Spec / Hero HTML / Hero SCSS — не создавать.** Ожидание решения оператора.

---

**STOP.**

---

## Git status

| Item | Value |
|------|-------|
| Commit / push | **Not performed** (default policy) |
| Changed files (this task) | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-HERO-DISCOVERY-v1.md` (created) |
| Build workspace | **Not modified** |
