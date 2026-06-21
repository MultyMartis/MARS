# REPORT — FP-0002 HERO LAYOUT SPEC v1

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-15  
**Phase:** HERO LAYOUT SPEC (composition only — **not** assembly, **not** visual scale, **not** build)  
**Visual SSOT:** `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg`  
**Authority chain applied:** JPG → [FP-0002-HERO-DISCOVERY-v1.md](FP-0002-HERO-DISCOVERY-v1.md) → [FP-0002-HERO-GROUP-FORENSIC-v1.md](FP-0002-HERO-GROUP-FORENSIC-v1.md) (**FORENSIC > DISCOVERY** on conflict)  
**Constraints respected:** HTML / SCSS / JS / Hero build / Assembly Spec / Visual Scale Spec — **NOT created**. `desktop-shell.html` · `desktop-ui-demo.html` · header · footer · `dist` — **NOT touched**.

**Sources NOT used (per charter):** PDF · старые Hero Layout Spec · Design Audit · BLOCK inventory labels as structure truth · UI DEMO · предположения beyond authority chain.

---

## 1. Hero Boundary

### START OF HERO

Нижняя кромка **второй строки header** (nav-строка: пункты меню + иконка поиска).  
Hero начинается **сразу под header**, без промежуточной полосы.

**Authority:** Discovery v1 §1 · Forensic v1 §1 — **совпадают**.

### END OF HERO

Верхняя кромка **следующей секции** — светлый (белый) фон страницы, центрированный заголовок **«Шпиговский дом — восстановление с уважением к личности»** (начало intro/features-блока).  
Hero заканчивается **до** этого белого контентного блока.

**Authority:** Forensic v1 §1 (supersedes Discovery v1 label «МНОГОПРОФИЛЬНОЕ…» — тот текст **не** является маркером END OF HERO по JPG re-scan).

### Что входит в Hero

| # | GROUP / элемент | Описание |
|---|-----------------|----------|
| 1 | **GROUP-01** Hero Background Media | Full-width фотография здания клиники (белая башня, кирпич, деревья, небо, газон) |
| 2 | **GROUP-01B** Image Overlay | Глобальное затемнение / десатурация поверх всего фонового фото |
| 3 | **GROUP-01C** Image Mask | Скруглённые углы hero-контейнера (clip/mask фото по периметру Hero) |
| 4 | **GROUP-02** Overlay Card Container | Aggregated shell: surface + inner content stack |
| 5 | **GROUP-02A** Card Surface | Полупрозрачная панель (frosted glass: surface + backdrop blur + radius) |
| 6 | **GROUP-02B** Content Stack | Вертикальный stack внутри карточки |
| 7 | **GROUP-03** Label | Мелкий uppercase-текст в верхней части content stack |
| 8 | **GROUP-04** Main Heading | Крупный display serif-заголовок в середине content stack |
| 9 | **GROUP-05** CTA Primary | Красная pill-кнопка **ниже** карточки, на фоне фото |
| 10 | **Content Wrapper** (structural) | Позиционирование и центрирование GROUP-02 + GROUP-05 как единой вертикальной композиции |

### Что НЕ входит в Hero

| Элемент | Причина исключения |
|---------|-------------------|
| Header (logo, контакт, CTA header, nav, search) | **Выше** START OF HERO |
| Секция «Шпиговский дом — восстановление с уважением к личности» и далее | **Ниже** END OF HERO — белый фон, H2, абзац, список, сетка карточек |
| Footer | Нижняя часть страницы |
| Mid-page блоки (quote, programs, gallery, form, FAQ и т.д.) | Вне границ Hero |

---

## 2. Group Register v2

**Register v2 locked.** Discovery v1 register (5 групп, GROUP-02 включает CTA) — **superseded**.

Декомпозиция Hero **сверху вниз, слева направо**. Parent-иерархия по Forensic v1 §5.

| GROUP-ID | Название | Позиция | Визуальное описание | Parent |
|----------|----------|---------|---------------------|--------|
| **GROUP-01** | Hero Background Media | Full-width Hero band | Фото здания клиники, full bleed внутри Hero bounds | Hero root |
| **GROUP-01B** | Hero Background Image Overlay | Поверх GROUP-01 | Тёмный/серый wash на всём фоновом фото | GROUP-01 |
| **GROUP-01C** | Hero Container Corner Mask | Clip Hero bounds | Скруглённые углы hero-контейнера | GROUP-01 |
| **GROUP-02** | Overlay Card Container | Центр Hero | Aggregated container: GROUP-02A + GROUP-02B; **не включает GROUP-05** | Content wrapper |
| **GROUP-02A** | Card Surface | Центр Hero | Frosted glass panel: semi-transparent surface + backdrop blur + radius; **без** видимого stroke/border | GROUP-02 |
| **GROUP-02B** | Card Content Stack | Внутри GROUP-02A | Vertical stack label → heading; отдельной визуальной «коробки» нет — layout-сущность | GROUP-02 |
| **GROUP-03** | Label | Top of GROUP-02B | Одна строка uppercase sans-serif белого текста | GROUP-02B |
| **GROUP-04** | Main Heading | Middle of GROUP-02B | Один display serif заголовок | GROUP-02B |
| **GROUP-05** | CTA Primary | Below GROUP-02, centered | Красная pill-кнопка; **вне** GROUP-02A surface | Content wrapper |

**Итого registered IDs:** 9 (GROUP-01, 01B, 01C, 02, 02A, 02B, 03, 04, 05)

### Корректировки vs Discovery v1 (обоснование)

| Изменение | Обоснование (Forensic > Discovery) |
|-----------|-------------------------------------|
| Добавлены GROUP-01B, GROUP-01C | Визуально наблюдаемые sub-layers фона — пропущены в Discovery v1 |
| GROUP-02 split → GROUP-02A + GROUP-02B | Card surface (frosted shell) и content stack (label + heading) — различимые layout-сущности; Discovery v1 over-aggregated |
| GROUP-05 исключён из GROUP-02 | CTA визуально **вне** translucent card surface (см. §3) |
| Content wrapper явно в модели | Structural layer для sibling-позиционирования card + CTA — не был в Discovery v1 дереве |

**Не обнаружено в JPG (отдельных групп нет):** secondary CTA · subtitle/description paragraph · icon/badges row · logo внутри overlay · form/input · breadcrumb · decorative frame/border · отдельная card shadow mass.

---

## 3. CTA Relationship Decision

### Вопрос

CTA является:

- A) CHILD OF CARD  
- B) SIBLING OF CARD  
- C) UNKNOWN  

### Ответ

**B) SIBLING OF CARD**

### Evidence (JPG-only)

| # | Observation | Implication |
|---|-------------|-------------|
| E-01 | Полупрозрачная панель GROUP-02A (frosted surface) **заканчивается** непосредственно под GROUP-04 (heading) | Нижняя граница card surface **не** охватывает кнопку |
| E-02 | GROUP-05 (красная pill-кнопка) расположена **ниже** GROUP-02 с **видимым вертикальным зазором** | CTA не является содержимым card shell |
| E-03 | Кнопка визуально сидит **на фоновом фото** (GROUP-01), не на frosted panel | CTA не child GROUP-02A |
| E-04 | Label, Heading, CTA выровнены по **одной вертикальной оси** (center line) | Общий parent — content wrapper, не card-only nesting |
| E-05 | Forensic v1 re-scan: «CTA — отдельный визуальный блок, sibling карточки» | Подтверждает B |

**Discovery v1 ошибка (отклонена):** GROUP-05 внутри overlay card — **не подтверждается** JPG.

**DOM implication (layout-only, не HTML):** GROUP-02 и GROUP-05 — **siblings** под content wrapper; GROUP-05 **не** descendant GROUP-02.

---

## 4. Layout Model

Композиция только. **Без px. Без CSS. Без предположений** beyond authority chain.

### ROW COUNT

| Level | Count | Description |
|-------|-------|-------------|
| **Section (Hero root)** | **1** | Одна full-width горизонтальная полоса Hero |
| **Inside content wrapper** | **2** | Вертикальный stack: (1) overlay card · (2) CTA |
| **Inside GROUP-02B** | **2** | Вертикальный stack: (1) label · (2) heading |

### COLUMN COUNT

| Level | Count | Description |
|-------|-------|-------------|
| **Section (Hero root)** | **1** | Фон на всю ширину; overlay content — одна центральная колонка |
| **Inside overlay card** | **1** | Label + heading — одна центрированная ось |
| **Inside content wrapper** | **1** | Card + CTA — одна центрированная ось |

### VISUAL ZONES

| Zone | GROUP(s) | Role |
|------|----------|------|
| **BACKGROUND ZONE** | GROUP-01 + GROUP-01B + GROUP-01C | Full-bleed photo band; global wash; corner clip |
| **CENTER CONTENT ZONE** | Content wrapper → GROUP-02 + GROUP-05 | Центрированная вертикальная композиция поверх background |
| **CARD SURFACE ZONE** | GROUP-02A | Frosted panel — только label + heading внутри |
| **CTA ZONE** | GROUP-05 | Отдельная зона под card, на background |

**Area map (background photo, не overlay):**

| Area | Содержимое |
|------|------------|
| TOP | Небо, верх здания |
| BOTTOM | Газон, низ здания |
| LEFT / RIGHT | Деревья, боковые фасады |
| CENTER | Content wrapper (card + CTA) |

### CONTENT WRAPPER

- **Role:** позиционирование и центрирование GROUP-02 и GROUP-05 как **единой вертикальной композиции** поверх background.
- **Children:** GROUP-02 (overlay card container) · GROUP-05 (CTA) — **siblings**.
- **Not in Discovery v1** — добавлен по Forensic Frontend Developer Test.

### CARD POSITION

- **Horizontal:** center of Hero band (center line of page content area).
- **Vertical:** center of Hero band (card + CTA stack центрированы как группа в пределах Hero height).

### CTA POSITION

- **Horizontal:** center — совпадает с center line card.
- **Vertical:** **below** GROUP-02, с зазором между нижней кромкой card surface и верхней кромкой кнопки.
- **Layer:** на background photo (не на frosted panel).

### CENTER LINE

- Одна вертикальная ось: GROUP-03 (label) · GROUP-04 (heading) · GROUP-05 (CTA) — **все center-aligned** на одной оси.

### VERTICAL FLOW

```
[Header — NOT Hero]
        ↓
┌─────────────────────────────────────────────────────────┐
│  GROUP-01 Background (+ GROUP-01B wash, GROUP-01C clip) │
│                                                         │
│              ┌─────────────────────────┐                │
│              │ GROUP-02A Card Surface  │                │
│              │  GROUP-03 Label         │                │
│              │  GROUP-04 Heading       │                │
│              └─────────────────────────┘                │
│                      (gap)                              │
│              ┌─────────────────────────┐                │
│              │ GROUP-05 CTA            │                │
│              └─────────────────────────┘                │
│                                                         │
└─────────────────────────────────────────────────────────┘
        ↓
[White section «Шпиговский дом — восстановление…» — NOT Hero]
```

**Порядок чтения:** фон (full bleed) → центральная карточка (label → heading) → CTA под карточкой.

### Layer stack (composition, not CSS)

| Layer | Content |
|-------|---------|
| L0 | Hero root — section band, bounds, overflow |
| L1 | GROUP-01 background image |
| L2 | GROUP-01B image overlay (wash) |
| L3 | GROUP-01C corner mask (clip) |
| L4 | Content wrapper — centers card + CTA |
| L5 | GROUP-02A card surface |
| L6 | GROUP-02B content stack (GROUP-03, GROUP-04) |
| L7 | GROUP-05 CTA (sibling of GROUP-02, under L4) |

---

## 5. Frontend Tree

Фактическая структура Hero по Group Register v2 и CTA decision (layout tree — **не** HTML spec).

```
Hero (section root)
├─ Background Layer                         ← GROUP-01 + GROUP-01C (image + corner clip)
│  └─ Background Image Overlay              ← GROUP-01B (wash; may be pseudo in build — UNKNOWN)
└─ Content Wrapper                          ← structural; centers vertical stack
   ├─ Overlay Card                          ← GROUP-02 (aggregated shell)
   │  ├─ Card Surface                       ← GROUP-02A (frosted panel)
   │  └─ Content Stack                      ← GROUP-02B (layout entity)
   │     ├─ Label                           ← GROUP-03
   │     └─ Main Heading                    ← GROUP-04
   └─ CTA Primary                           ← GROUP-05 (sibling of Overlay Card)
```

**Отличие от Discovery v1 (отклонено):**

```
Hero
├─ Background
└─ Overlay Card
   ├─ Label
   ├─ Heading
   └─ CTA          ← ОШИБКА Discovery v1
```

**Structural div count (layout planning only):** Hero root · background · background-overlay · content wrapper · card surface · CTA wrapper — **5–6** top-level structural blocks (overlay wash — div или pseudo: **UNKNOWN** для build).

---

## 6. Frozen Decisions

Только реальные composition decisions зафиксированные в этом spec. Copy lock — authority Forensic v2 (JPG); assembly/scale — отдельные будущие документы.

| ID | Decision |
|----|----------|
| **FD-01** | **Hero START** — нижняя кромка header nav-row (BLK-002 bottom); без gap между header и Hero |
| **FD-02** | **Hero END** — верх белой секции с заголовком «Шпиговский дом — восстановление с уважением к личности»; Hero **не** включает intro/features block |
| **FD-03** | **CTA relation = SIBLING OF CARD (B)** — GROUP-05 **не** child GROUP-02 / GROUP-02A |
| **FD-04** | **GROUP-02** aggregates **only** GROUP-02A + GROUP-02B — **не** GROUP-05 |
| **FD-05** | **GROUP-02B** contains GROUP-03 + GROUP-04 — vertical stack label → heading |
| **FD-06** | **GROUP-01** background layer includes sub-layers GROUP-01B (wash) + GROUP-01C (corner mask) |
| **FD-07** | **Content wrapper** — mandatory structural parent of GROUP-02 and GROUP-05 for center-stack positioning |
| **FD-08** | **Group Register v2 locked** — 9 IDs (01, 01B, 01C, 02, 02A, 02B, 03, 04, 05); Discovery v1 register superseded |
| **FD-09** | **Section-level layout** — 1 row full-width band; 1 central content column for overlay stack |
| **FD-10** | **Center line** — label · heading · CTA share one vertical center axis |
| **FD-11** | **Vertical flow inside card** — label above heading only; **no** description paragraph between heading and card bottom |
| **FD-12** | **Card surface** — frosted glass (semi-transparent + blur); **no** visible decorative border/frame; **no** readable shadow mass |
| **FD-13** | **Absent in Hero** — secondary CTA · form · badges/icons row · breadcrumb · logo inside overlay |
| **FD-14** | **Content Lock v2 (JPG)** — GROUP-03: `Центр профилактики и лечения зависимостей` · GROUP-04: `Шпиговский дом` · GROUP-05: `ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ` |
| **FD-15** | Discovery v1 Content Lock (`КОРСАКОВ` / `ЧАСТНАЯ ПСИХИАТРИЧЕСКАЯ КЛИНИКА` / `ЗАПИСАТЬСЯ НА ПРИЕМ`) — **rejected** |

---

## 7. Safe Unknown

Только реальные UNKNOWN. Без фантазий.

| ID | Subject | Reason |
|----|---------|--------|
| **U-01** | Hero section height | JPG даёт пропорцию, не pixel measure |
| **U-02** | Overlay card width / height / internal padding / border-radius | Форма видна; exact dimensions не locked в authority chain |
| **U-03** | Card surface color / opacity / blur strength | Визуально frosted glass; exact values не locked |
| **U-04** | Gap between card bottom and CTA top | Зазор виден; exact measure — UNKNOWN |
| **U-05** | Background image asset (filename, crop, focal point) | Фото идентифицировано визуально; файл в репо не верифицирован в authority chain |
| **U-06** | Mobile / tablet Hero layout | JPG — desktop full-page; адаптив Hero не показан |
| **U-07** | Exact font-size / line-height / weight в overlay | Tiers не locked на этом этапе |
| **U-08** | CTA uppercase — CSS `text-transform` vs literal caps in copy | Текст читается uppercase; render mechanism — UNKNOWN |
| **U-09** | GROUP-01B implementation — separate div vs pseudo-element | Layout tree допускает оба; build choice — UNKNOWN |
| **U-10** | Exact END marker copy truncation | Forensic cites full H2 string; partial ellipsis в boundary table — cosmetic only; full string locked in FD-02 |

**NOT listed as UNKNOWN (confirmed absent or locked):**

- Hero subtitle / description line — **не видна** как отдельная группа  
- Secondary CTA — **отсутствует**  
- Form in Hero — **отсутствует**  
- CTA inside card — **rejected** (FD-03)  
- GROUP-03 / GROUP-04 / GROUP-05 copy — **LOCKED** (FD-14)

---

## 8. Implementation Readiness

| Gate | Answer |
|------|--------|
| **HERO LAYOUT SPEC COMPLETE** | **YES** |
| **GROUP REGISTER LOCKED** | **YES** (v2) |
| **CTA RELATION LOCKED** | **YES** (B — sibling of card) |
| **READY FOR HERO ASSEMBLY SPEC** | **YES** |
| **READY FOR HERO BUILD** | **NO** |

---

## 9. Final Verdict

Hero на `HOME-PAGE-FULL-MOCKUP.jpg` — **одна full-width полоса** с фоновым фото (sub-layers: global wash + corner mask), **центрированной frosted card** (label + heading only) и **CTA как sibling карточки** под ней на фоне фото.

**Group Register v2** (9 IDs) заменяет Discovery v1. **CTA relation B** зафиксирован с JPG evidence.

Hero Layout Spec завершён. **Hero Assembly Spec · Hero Visual Scale Spec · Hero HTML · Hero SCSS — не создавать.** Ожидание решения оператора.

---

**STOP.**

---

## Git status

| Item | Value |
|------|-------|
| Commit / push | **Not performed** (default policy) |
| Changed files (this task) | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-HERO-LAYOUT-SPEC-v1.md` (created) |
| Build workspace | **Not modified** |
