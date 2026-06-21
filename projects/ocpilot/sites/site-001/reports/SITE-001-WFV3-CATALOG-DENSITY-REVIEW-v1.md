# REPORT — SITE-001 WF-V3 Catalog Density & Inventory Review v1

**Type:** Authority review — catalog perception & inventory density (audit only)  
**Date:** 2026-06-14  
**Site:** SITE-001 — Автосалон СИБКАР  
**Program:** Website Factory · WF-V3  
**Trigger:** HITL Review Catalog Prototype v0.1 — operator verdict **B (One More Catalog Iteration)**; причина — ощущение каталога и склада, **не** дизайн

**Explicit exclusions (honored):** No code · No workspace changes · No OpenCart · No new prototype version · No redesign · No commit implied

**Evidence sources (read-only):**

| Source | Path | Role |
|--------|------|------|
| Catalog prototype v0.1 | `workspaces/site-001-wf-v3-catalog-prototype/` | Implemented zones C0–C11 |
| Session report | `workspaces/site-001-wf-v3-catalog-prototype/docs/CATALOG-PROTOTYPE-v0.1-REPORT.md` | Build facts, self-test claims |
| Screenshots (1440×900) | `workspaces/site-001-wf-v3-catalog-prototype/screenshots/` | Visual evidence |
| Blueprint | [SITE-001-WFV3-CATALOG-BLUEPRINT-v1.md](SITE-001-WFV3-CATALOG-BLUEPRINT-v1.md) | Zone intent, N=3 authority |
| Discovery | [SITE-001-WFV3-CATALOG-DISCOVERY-v1.md](SITE-001-WFV3-CATALOG-DISCOVERY-v1.md) | Class B showroom, density targets |
| Charter | [SITE-001-WFV3-CATALOG-PROTOTYPE-CHARTER-v1.md](../governance/SITE-001-WFV3-CATALOG-PROTOTYPE-CHARTER-v1.md) | First-screen contract |
| Prior density audit (TEST) | [SITE-001-W3UX-DENSITY-AUDIT-v1.md](SITE-001-W3UX-DENSITY-AUDIT-v1.md) | Historical OC density baseline |

**Screenshot viewport:** 1440×900 (Playwright, `scripts/capture-screenshots.mjs`).

**Scope:** Inventory density · card grid · filter dominance · dealer psychology · zone hierarchy C3–C6. Цвета, типографика как brand system — **вне scope** (operator подтвердил: дизайн не причина).

---

## Executive Summary

Catalog Prototype v0.1 **грамотно наследует** WF-V3 shell (header, USP, tokens, card grammar) и **не** выглядит как Auto.ru / Avito. Однако **перceptual bar «реальный склад СИБКАР» не достигнут**: страница читается ближе к **курируемой витрине с небольшим видимым списком**, чем к **«у них много автомобилей»**.

Корневая причина — **не** visual direction, а **соотношение вертикальной массы фильтра, высоты карточки и числа машин в первом кадре**. Текст «Найдено **147** автомобилей» и USP «150+ в наличии» **не подкреплены** визуальной плотностью сетки.

Внутренний self-test прототипа («≥2 ряда карточек на first screen») формально **PASS** при 1440px, но **perceptual gap** для оператора остаётся — это согласуется с operator verdict **B**.

**Рекомендация итерации:** **B — лёгкая корректировка плотности** (spacing / grid count / filter visual weight), **без** переработки C0–C11 и **без** нового design language.

---

## 1. Inventory Density Audit

### 1.1 Вопрос

Создаёт ли каталог ощущение **«У них много автомобилей»** или **«Небольшой список объявлений»**?

### 1.2 Verdict

**Склоняется к «небольшой список» / «курируемая подборка»** — несмотря на корректный счётчик 147.

### 1.3 Обоснование

| Signal | Что видит пользователь | Эффект на восприятие масштаба |
|--------|------------------------|-------------------------------|
| **C3 count** | «Найдено 147 автомобилей» — одна строка muted text под H1 | Число **declarative**, не **demonstrative**; легко теряется после USP «150+» |
| **C6 grid mass** | N=3, крупные карточки (16:10 photo + расширенное body) | В кадре одновременно **мало силуэтов машин**; каждая карточка = «объект внимания», не «элемент потока» |
| **First viewport** | После C0–C3 (~280–300 px chrome) в правой колонке: chips + **~1 полный ряд + частичный второй** | Оценка: **3 полные + 2–3 частичные** машины ≈ **5–6** видимых позиций — для дилера со 150+ stock это **низкая визуальная доказательность** |
| **Pagination C7** | «Страница 1 из 17» — ниже fold на first paint | Масштаб ассортимента **не участвует** в первом впечатлении |
| **Filter CTA** | «Показать 147 автомобилей» в sidebar | Count дублируется в **filter zone**, не в **inventory zone** — усиливает «я ищу в базе», не «я на складе» |
| **Placeholder photos** | Studio silhouettes, generous padding | Уменьшают ощущение **заполненного реального лота** (прототипный артефакт; учитывать при HITL) |

**Contrast с mental model агрегатора:** Auto.ru / Avito при том же viewport показывают **8–12+ компактных карточек** — пользователь **видит массу**. Текущий WF-V3 catalog **сознательно не** копирует агрегатор, но **перекачивает** в сторону editorial/showroom — и теряет **dealer warehouse signal**.

**Contrast с mental model regional dealer:** СИБКАР = физический салон + реальный склад. Ожидание: «**стена машин**», compare-in-place, ощущение **изобилия без маркетплейс-шума**. Сейчас — «**галерея нескольких моделей**».

### 1.4 Числовая оценка (desktop 1440×900, sidebar layout)

Расчёт по tokens и SCSS (не runtime measure):

| Parameter | Value |
|-----------|-------|
| Inner container | ~1232 px |
| Results column (9fr) | ~892 px |
| Card width @ N=3 | ~284 px |
| Est. card height | ~320–340 px (16:10 photo + catalog body fields) |
| Cars fully visible row 1 | **3** |
| Partial row 2 | **~2–3** (верх карточек) |
| **Total first-screen inventory faces** | **~5–6** |

Для сравнения: W3UX audit на legacy TEST `/cars/` (4 cols, OC geometry) — **~4–6 partial above fold** при меньшей высоте chrome; WF-V3 **не выигрывает** по видимому количеству, хотя card quality выше.

---

## 2. Card Density Review

### 2.1 Authority: 3 карточки в ряд

Blueprint §4.3 и `$catalog-cols-desktop: 3` — **осознанный** выбор: compare 3 машин с readable photo + price; sibling к Homepage H4 N=4 при **более узкой** card width в sidebar layout.

### 2.2 Достаточно ли плотности @ N=3?

**Нет — для задачи «Digital Inventory Showroom» СИБКАР.**

| Criterion | N=3 assessment |
|-----------|----------------|
| Compare job (3 cars side-by-side) | **PASS** — ряд читается |
| Warehouse abundance signal | **FAIL** — мало рядов в viewport |
| Alignment с USP «150+ в наличии» | **WEAK** — verbal claim без visual echo |
| Charter first-screen («≥2 card rows») | **Borderline PASS** — 2-й ряд частичный, не «стена» |
| Card field stack (badge, specs, monthly, CTA) | **Adds height** — каждая карточка ~17–20% выше minimal tile |

**Вывод:** N=3 оптимизирует **качество сравнения одного ряда**, но **не** оптимизирует **ощущение масштаба склада** — именно то, что оператор отметил в HITL.

### 2.3 Сколько автомобилей на первом экране

| Viewport zone | Visible inventory |
|---------------|-------------------|
| Above catalog body (C0–C3) | **0** машин — только nav, USP, H1, count, sort |
| First screen incl. C4 sidebar + C6 | **~5–6** машин (3 full + partial row) |
| Full page scroll (screenshot) | **9** карточек (3×3 static fixture) |

Задача каталога (Discovery §2, Charter): **«витрина склада — сравнивать машины»**. Для compare — 3 в ряд достаточно. Для **«склад»** — first screen должен показывать **минимум 2 полных ряда (6+) без ощущения «конец списка»**; сейчас второй ряд **обрезан**, создавая subconscious «мало».

### 2.4 Сравнение: 3 в ряд vs 4 в ряд (analysis only)

| Dimension | **3 columns** (current) | **4 columns** (hypothesis) |
|-----------|-------------------------|----------------------------|
| Cars per row | 3 | 4 (+33% horizontal density) |
| Card width @ ~892px main | ~284 px | ~208 px |
| Photo height @ 16:10 | ~177 px | ~130 px |
| Est. rows in first ~570px grid area | ~1.6 | ~2.2–2.5 |
| **First-screen faces (est.)** | **~5–6** | **~8–10** |
| Compare readability | **Strong** — крупный силуэт, price scan | **Moderate** — still Class B, not OC tile |
| Homepage sibling parity | **Diverges** from H4 N=4 featured | **Aligns** with H4 grid grammar |
| Aggregator similarity risk | **Low** | **Low–medium** — if card stays tall, still dealer; if compacted too far → OC drift |
| Dealer «wall of cars» signal | **Weak** | **Stronger** without marketplace noise |

**Analysis conclusion:** Переход **3 → 4** в results column — **наиболее прямой рычаг** warehouse perception **без** redesign. Альтернатива/дополнение: **оставить N=3**, но **уменьшить vertical card stack** (~15–20% height) — discovery W3UX на TEST давал +1 row при той же col count.

**Не рекомендуется** в рамках лёгкой итерации: 5+ columns, infinite scroll, swiper — anti-patterns per charter.

---

## 3. Filter Dominance Review

### 3.1 Текущая модель

```text
C3  Page header (H1 + count + sort)
        ↓
C4  Filter sidebar (left, gray panel)  ║  C5 chips + C6 grid (right)
```

Layout: `L-sidebar + L-grid` — 3fr / 9fr, sidebar min 260px (`_catalog-filters.scss`, `_tokens.scss`).

### 3.2 Занимает ли фильтр слишком много внимания?

**Да — относительно автомобилей фильтр доминирует.**

| Factor | Observation | Weight impact |
|--------|-------------|---------------|
| **Surface** | `$color-surface-secondary` panel + border + padding | Filter = **отдельный объект**; cards on white — вторичный фон |
| **Title** | «Подбор автомобиля» @ `$font-size-h3` (18px bold) | **Parallel H-level** к card price — второй «заголовок страницы» после C3 H1 |
| **Vertical stack** | 5 fields + full-width outline CTA (Tier 1 + Tier 2 fields: КПП, Кузов) | Sidebar **~400–450 px** tall — **≈ высота 1.3–1.5 card rows** |
| **Horizontal share** | ~25% viewport width постоянно | Filter **always visible**; inventory **always compressed** |
| **C5 chips** | Demo state: 4 active chips + reset | **Extends filter narrative** into main column **before** first card row |
| **CTA color** | Red outline «Показать 147…» | Strong affordance in **filter zone**, not on inventory |

### 3.3 Filter vs Inventory attention ratio (qualitative)

| Zone | First-screen visual share (est.) | Job |
|------|----------------------------------|-----|
| C4 Filter sidebar | **~35–40%** of catalog-body attention | Narrow search |
| C5 Chips | **~5%** | Confirm criteria |
| C6 Grid | **~55–60%** | **Should be ~70%+** for showroom job |

Discovery anti-pattern: *«Красивые фильтры, но машин не видно»* — WF-V3 **не** zero-card (sidebar layout спасает), но **partially reproduces** filter-heavy first read из legacy TEST (Discovery §9.1).

### 3.4 Verdict

Filter **не ошибочен по функции** (P-05 search first-class), но **перегружен по visual mass** для Class B inventory page. Фильтр читается как **primary task** («подбери из базы»), inventory — **secondary** («вот несколько результатов»).

---

## 4. Dealer Psychology Review

### 4.1 Target mental model: СИБКАР regional dealer

| Should feel | Should NOT feel |
|-------------|-----------------|
| Региональный автосалон с **физическим складом** | Маркетплейс / классифайд |
| **150+ реальных авто** — можно приехать и выбрать | Бесконечная база частных объявлений |
| Curated quality + **substantial choice** | Boutique с 12 машинами |
| Dealer trust (проверка, trade-in, кредит) | Aggregator neutrality |
| Same brand shell as homepage / PDP | «Другой продукт» |

### 4.2 Current prototype mapping

| Aspect | Perception | Match |
|--------|------------|-------|
| Header / USP / footer | СИБКАР dealer shell | **Strong** |
| Card grammar (flat, red price, «Подробнее») | WF-V3 showroom, not OC swiper | **Strong** |
| Sidebar filter panel | Portal / classified **search UX** | **Medium drift** toward aggregator |
| Grid density | Premium gallery, **low volume** | **Weak** for warehouse |
| Trust C8 below fold | Dealer policy — correct placement | **OK** (not first-screen job) |
| Finance C9 | Secondary conversion — acceptable | **OK** |

### 4.3 Verdict

Прототип **успешно избегает** Auto.ru / Avito **visual noise** (no per-card swiper, no solid red card buttons, no reviews slider). Но **переборщил в showroom/editorial** и **недобрал dealer inventory psychology** — «**наш большой двор**, выбирай».

Operator diagnosis (**не дизайн, а каталог/склад**) **подтверждается**: tokens и brand **на месте**; **information architecture of abundance** — нет.

---

## 5. Catalog Hierarchy Review (C3–C6)

### 5.1 Intended hierarchy (Blueprint)

```text
C3  Category anchor + scale (count) + sort utility
C4  Search tool (supporting)
C5  Filter transparency (supporting)
C6  Core catalog moment — PRIMARY
```

### 5.2 Actual visual weight

| Zone | Intended weight | Actual weight | Delta |
|------|-----------------|---------------|-------|
| **C3** | High (H1 authority) | **High** — H1 30px + count | **OK** |
| **C4** | Medium (tool) | **High** — gray panel, h3 title, tall stack, red CTA | **Over-weight** |
| **C5** | Low–medium (when active) | **Medium** in demo — 4 chips consume main column header band | **Slightly high** for density review fixture |
| **C6** | **Highest** | **Medium** — shares row with C4; starts below chips; 3 wide cards | **Under-weight** |

### 5.3 Hierarchy defects (layout-level, not cosmetic)

1. **Dual headers:** C3 H1 «Каталог…» + C4 «Подбор автомобиля» — два конкурирующих **page intents**.
2. **Scale signal misplaced:** «147» в C3 muted; strongest count echo — в **filter CTA**, не над grid.
3. **Inventory starts second:** В правой колонке порядок C5 → C6 — filter story **продолжается** перед первой машиной.
4. **Vertical competition:** Sidebar filter height **matches or exceeds** visible grid height on first screen — баланс **50/50**, не **70/30** inventory-first.

### 5.4 Verdict

Иерархия зон **логически верна** в blueprint, но **визуально инвертирована**: C4 (+ C5) **поглощают** authority, которую C6 должна удерживать. C3 выполняет роль, но **не компенсирует** слабую grid mass ниже.

---

## 6. Recommendation

### 6.1 Options

| Option | Meaning | Fit |
|--------|---------|-----|
| **A** | Оставить как есть | **Reject** — противоречит operator HITL B; perceptual gap documented |
| **B** | Лёгкая корректировка плотности | **Select** — structure sound, levers localized |
| **C** | Серьёзная переработка каталога | **Reject** — нет оснований ломать C0–C11, tokens, sibling continuity |

### 6.2 Selected: **B — Лёгкая корректировка плотности**

**Почему не A:** Operator уже зафиксировал необходимость итерации; self-test PASS по «≥2 rows» **не закрывает** business perceptual bar.

**Почему не C:** Нет дефектов design language, container, header/footer, card component identity, или zone inventory C0–C11. Проблема — **density tuning** и **filter/inventory balance**, а не новая IA.

**Почему B:** Все рычаги — **spacing / column count / filter chrome weight / demo fixture state** — укладываются в charter constraint «no new design language» и sibling tests.

### 6.3 Suggested iteration levers (documentation only — not authorized implementation)

Priority order for next prototype pass:

| Priority | Lever | Expected effect |
|----------|-------|-----------------|
| **1** | Re-evaluate **N=4** in C6 results column (desktop) **or** compact card height ~15–20% @ N=3 | +1 full row first screen; stronger warehouse signal |
| **2** | Reduce C4 visual mass — lighter surface, smaller filter title, tighter field spacing | Shift attention **C4 → C6** |
| **3** | Strengthen C3 count as **inventory proof** (visual tie to grid, not filter CTA) | Declarative → demonstrative scale |
| **4** | HITL demo state: **unfiltered** entry + optional «filtered» variant | Chips bar should not dominate default density review |
| **5** | Confirm Tier 1-only filter height for first-screen calc | КПП/Кузов (Tier 2) increase sidebar height vs Tier 1 charter minimum |

**Out of scope for B:** sticky filter, accordion Tier 2, carousel, new tokens, mobile pass, backend binding.

---

## 7. Alignment with Prior Audits

| Prior work | Relation to this review |
|------------|-------------------------|
| W3UX Density Audit (TEST OC) | Diagnosed same root cause — **vertical inflation**, weak abundance — on **legacy** `/cars/` |
| W3UX Density Decision | CSS-first compaction **achievable**; WF-V3 prototype **inherits lesson** but applies clean-room card (taller by design) |
| Catalog Discovery §9 | Target: «2–3 card rows visible» — v0.1 **technically** near target, **perceptually** under-delivers |
| Catalog Blueprint N=3 | Authority stands for **compare**; this review flags **warehouse** tradeoff — operator iteration may **revisit N=4** without full redesign |

---

## UNKNOWN

| Item | Status |
|------|--------|
| Operator live review @ 1440px side-by-side with homepage/PDP | Pending — this review uses screenshots + SCSS |
| Real photo density vs placeholder silhouettes | **NOT VERIFIED** — may improve abundance ~5–10% perceptually |
| Mobile filter drawer impact | **SAFE UNKNOWN** — desktop-only v0.1 |
| Live inventory count 147 | Static placeholder per prototype report |

**SECURITY RISK:** None (static audit).

---

# Final Verdicts

## Inventory Density Verdict

**BELOW TARGET — reads as «curated short list», not «large dealer warehouse».**  
Text scale (147 / 150+) is present; **visual scale** (grid mass in first viewport) is insufficient for СИБКАР inventory psychology.

## Card Density Verdict

**N=3 is compare-optimal but warehouse-suboptimal.** First screen ~**5–6** visible cars @ 1440×900; target for dealer showroom **≥6 full faces, preferably 2+ complete rows**. **4 columns** or **~15–20% card height reduction @ N=3** — preferred levers for iteration B.

## Catalog Authority Verdict

**Structure and brand authority HOLD; inventory-zone authority is WEAK.**  
C4 filter (+ C5 in demo) **over-dominate** C6. Hierarchy C3–C6 is **logically correct, visually inverted**. Prototype remains **Class B sibling** to homepage/PDP — **not** aggregator — but **must rebalance** filter vs inventory mass to complete the «Digital Inventory Showroom» charter.

---

## Iteration Decision

# **B — Лёгкая корректировка плотности**

Без redesign, без новой версии design language, без перестройки C0–C11. Следующий шаг — **Catalog Prototype v0.2 density pass** (operator-chartered), не OpenCart integration.

---

*SITE-001 WF-V3 Catalog Density Review v1 — authority audit only; no implementation implied.*
