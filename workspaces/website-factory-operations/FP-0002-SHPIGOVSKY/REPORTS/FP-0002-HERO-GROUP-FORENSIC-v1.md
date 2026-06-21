# REPORT — FP-0002 HERO GROUP FORENSIC v1

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-15  
**Phase:** HERO GROUP FORENSIC (analysis only)  
**Visual SSOT:** `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg`  
**Reference (comparison only):** `REPORTS/FP-0002-HERO-DISCOVERY-v1.md`  
**Constraints respected:** HTML / SCSS / JS / Hero build / Layout Spec / Assembly Spec — **NOT created**. Header / footer / shell / dist — **NOT touched**.

**Sources NOT used (per charter):** PDF · старые Hero-версии · Design Audit · BLOCK inventory · UI DEMO · предположения.

---

## 1. Hero Re-Scan

### Границы Hero (подтверждены по JPG)

| Boundary | Определение |
|----------|-------------|
| **START** | Нижняя кромка nav-строки header (пункты меню + поиск) |
| **END** | Верхняя кромка следующей секции — светлый фон, заголовок «Шпиговский дом — восстановление с уважением к личности» |

Границы Hero **совпадают** с Discovery v1. Сомнение оператора касалось **внутренней декомпозиции**, не границ.

### Визуальная картина Hero (re-scan)

Hero — **одна full-width полоса** с:

1. Фоновым фото здания (белая башня + красный кирпич, деревья).
2. Глобальным затемнением / десатурацией фото (overlay на всём background).
3. Центрированной **полупрозрачной карточкой** (frosted glass: surface + backdrop blur, скруглённые углы).
4. **CTA-кнопкой**, расположенной **ниже карточки**, **не внутри** неё.

### Ключевой вывод re-scan по GROUP-02

**GROUP-02 Overlay Card Container — не атомарная сущность.**

Визуально это **композит**:

- внешняя оболочка (card surface + backdrop blur),
- внутренний вертикальный content stack (label + heading).

Кроме того, Discovery v1 **ошибочно включал GROUP-05 (CTA) внутрь overlay**. По JPG CTA — **отдельный визуальный блок**, sibling карточки, с вертикальным зазором.

### Расхождение Content Lock с Discovery v1

| GROUP | Discovery v1 (LOCKED) | JPG (факт) |
|-------|----------------------|------------|
| GROUP-03 Label | `ЧАСТНАЯ ПСИХИАТРИЧЕСКАЯ КЛИНИКА` | `Центр профилактики и лечения зависимостей` |
| GROUP-04 Heading | `КОРСАКОВ` | `Шпиговский дом` |
| GROUP-05 CTA | `ЗАПИСАТЬСЯ НА ПРИЕМ` | `ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ` |

Content Lock Discovery v1 **не подтверждён** мокапом.

---

## 2. Visual Entity Scan

Проверка по `HOME-PAGE-FULL-MOCKUP.jpg`. Только визуально наблюдаемые сущности.

| Entity | Status | GROUP-ID / Note |
|--------|--------|-----------------|
| **CARD SURFACE** | **PRESENT** | **GROUP-02A** — полупрозрачная белая панель со скруглёнными углами |
| **CARD BACKDROP** | **PRESENT** | Часть GROUP-02A — blur фона за панелью (frosted glass); отдельной второй плоскости нет |
| **CARD SHADOW MASS** | **NOT PRESENT** | Тень под карточкой не читается; separation через opacity + blur |
| **CONTENT STACK** | **PRESENT** | **GROUP-02B** — вертикальный stack label → heading **внутри** карточки; отдельной «коробки» нет, но layout-сущность различима |
| **LABEL ROW** | **PRESENT** | **GROUP-03** — одна строка uppercase sans-serif белого текста |
| **HEADING ROW** | **PRESENT** | **GROUP-04** — один display serif заголовок |
| **CTA ROW** | **PRESENT** | **GROUP-05** — красная pill-кнопка; **вне** GROUP-02 |
| **DECORATIVE FRAME** | **NOT PRESENT** | — |
| **DECORATIVE BORDER** | **NOT PRESENT** | У карточки нет видимого stroke/border |
| **IMAGE OVERLAY** | **PRESENT** | **GROUP-01B** — глобальное затемнение / десатурация поверх фонового фото |
| **IMAGE FILTER** | **PRESENT** | Совпадает с GROUP-01B (не отдельный второй filter на карточке) |
| **IMAGE MASK** | **PRESENT** | **GROUP-01C** — hero-контейнер с rounded corners (clip/mask фото по периметру Hero) |
| **IMAGE CROP AREA** | **PRESENT** | Входит в GROUP-01 — full-bleed фото внутри Hero bounds |

**Не обнаружено (отдельных групп нет):**

- Secondary CTA
- Subtitle / description paragraph в Hero
- Icon row / badges
- Logo внутри overlay
- Form / input
- Breadcrumb в Hero

---

## 3. Aggregation Audit

| GROUP-ID | Название | Verdict | Содержит / Примечание |
|----------|----------|---------|------------------------|
| **GROUP-01** | Hero Background Media | **ATOMIC** (на уровне слоя) | Фото здания full-bleed; sub-layers: GROUP-01B overlay, GROUP-01C corner mask |
| **GROUP-01B** | Hero Background Image Overlay | **ATOMIC** | Тёмный/серый wash поверх всего фото |
| **GROUP-01C** | Hero Container Corner Mask | **ATOMIC** | Rounded corners hero-контейнера |
| **GROUP-02** | Overlay Card Container | **AGGREGATED** | Объединяет GROUP-02A + GROUP-02B; **не включает GROUP-05** |
| **GROUP-02A** | Card Surface | **ATOMIC** | Semi-transparent panel + backdrop blur |
| **GROUP-02B** | Card Content Stack | **AGGREGATED** (layout) | Содержит GROUP-03 + GROUP-04; отдельной визуальной «коробки» нет |
| **GROUP-03** | Label | **ATOMIC** | Одна текстовая строка |
| **GROUP-04** | Main Heading | **ATOMIC** | Один заголовок |
| **GROUP-05** | CTA Primary | **ATOMIC** | Одна кнопка; **sibling** GROUP-02, не child |

### Ответ на сомнение оператора

> GROUP-02 действительно одна сущность или содержит несколько отдельных групп?

**Содержит несколько отдельных групп.**

GROUP-02 в Discovery v1 был **over-aggregated**:

1. Смешал **card shell** (surface/backdrop) и **content stack** (label + heading) в одну «неделимую» группу.
2. Ошибочно относил **CTA** к содержимому overlay («содержит GROUP-03…05»).

---

## 4. Frontend Developer Test

**Вопрос:** сколько отдельных div-блоков верхнего уровня frontend-разработчик создал бы в Hero **до HTML-детализации**?

### Дерево (структурные div-блоки)

```
Hero (section root)
├─ Background Layer                    ← GROUP-01 + GROUP-01C (image + corner clip)
│  └─ Background Overlay               ← GROUP-01B (optional separate div)
├─ Content Wrapper (center stack)      ← positioning layer (не в Discovery v1)
│  ├─ Overlay Card                     ← GROUP-02 (AGGREGATED shell)
│  │  ├─ Label                         ← GROUP-03
│  │  └─ Main Heading                  ← GROUP-04
│  └─ CTA Primary                      ← GROUP-05 (вне card)
```

### Подсчёт top-level structural divs внутри Hero

| # | Block | Role |
|---|-------|------|
| 1 | `hero` (root) | Section band, height, overflow |
| 2 | `hero__background` | Image + corner mask |
| 3 | `hero__background-overlay` | Darkening wash (может быть ::after) |
| 4 | `hero__content` | Flex/grid centering wrapper |
| 5 | `hero__card` | GROUP-02A surface |
| 6 | `hero__cta` | GROUP-05 button wrapper |

**Итого:** **5–6** structural div-блоков (overlay на фото — div или pseudo-element).

**Текстовые узлы внутри card:** Label (GROUP-03), Heading (GROUP-04) — не отдельные top-level div Hero, но отдельные DOM-элементы.

### Отличие от дерева Discovery v1

Discovery v1:

```
Hero
├─ Background
└─ Overlay Card
   ├─ Label
   ├─ Heading
   └─ CTA          ← ОШИБКА: CTA не внутри card
```

Forensic v1:

```
Hero
├─ Background (+ overlay sub-layer)
├─ Content Wrapper
│  ├─ Overlay Card (surface only)
│  │  ├─ Label
│  │  └─ Heading
│  └─ CTA           ← sibling card
```

---

## 5. Group Register v2

Discovery v1 **не подтверждён**. Новый register:

| GROUP-ID | Название | Позиция | Визуальное описание | Parent |
|----------|----------|---------|---------------------|--------|
| **GROUP-01** | Hero Background Media | Full-width Hero band | Фото здания клиники, full bleed | Hero root |
| **GROUP-01B** | Hero Background Image Overlay | Поверх GROUP-01 | Глобальное затемнение / десатурация фото | GROUP-01 |
| **GROUP-01C** | Hero Container Corner Mask | Clip Hero bounds | Скруглённые углы hero-контейнера | GROUP-01 |
| **GROUP-02** | Overlay Card Container | Центр Hero | Aggregated container: surface + inner stack | Content wrapper |
| **GROUP-02A** | Card Surface | Центр Hero | Frosted glass panel: semi-transparent white + backdrop blur + radius | GROUP-02 |
| **GROUP-02B** | Card Content Stack | Внутри GROUP-02A | Vertical stack label → heading | GROUP-02 |
| **GROUP-03** | Label | Top of GROUP-02B | `Центр профилактики и лечения зависимостей` | GROUP-02B |
| **GROUP-04** | Main Heading | Middle of GROUP-02B | `Шпиговский дом` (serif display) | GROUP-02B |
| **GROUP-05** | CTA Primary | Below GROUP-02, centered | Red pill button `ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ` | Content wrapper (не GROUP-02) |

**Итого групп в Hero:** 9 registered IDs (GROUP-01, 01B, 01C, 02, 02A, 02B, 03, 04, 05)

**Content Lock v2 (JPG-only):**

| GROUP-ID | Lock |
|----------|------|
| GROUP-03 | **LOCKED** — `Центр профилактики и лечения зависимостей` |
| GROUP-04 | **LOCKED** — `Шпиговский дом` |
| GROUP-05 | **LOCKED** — `ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ` |
| GROUP-01 | **LOCKED (visual)** — asset filename: **UNKNOWN** |

---

## 6. Final Verdict

| Gate | Answer |
|------|--------|
| **DISCOVERY v1 CONFIRMED** | **NO** |
| **GROUP AGGREGATION FOUND** | **YES** |
| **GROUP REGISTER UPDATE REQUIRED** | **YES** |
| **READY FOR HERO LAYOUT SPEC** | **YES** |
| **READY FOR HERO BUILD** | **NO** |

### Причины отклонения Discovery v1

1. **GROUP-02 over-aggregated** — card surface + content stack сведены в одну «неделимую» группу.
2. **GROUP-05 misplaced** — CTA визуально **вне** overlay card.
3. **Content Lock неверен** — все три текстовые строки в Discovery v1 не совпадают с JPG.
4. **Пропущены визуальные sub-layers** — background image overlay (GROUP-01B), hero corner mask (GROUP-01C).

### Рекомендация оператору

Перед Hero Layout Spec принять **Group Register v2** и **Content Lock v2**. Discovery v1 считать **superseded** для Hero grouping и copy.

---

**STOP.**

Hero Layout Spec · Hero Assembly Spec · Hero Visual Scale Spec · Hero HTML · Hero SCSS — **не создавать**. Ожидание решения оператора.

---

## Git status

| Item | Value |
|------|-------|
| Commit / push | **Not performed** (default policy) |
| Changed files (this task) | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-HERO-GROUP-FORENSIC-v1.md` (created) |
| Build workspace | **Not modified** |
