# REPORT — BZPM W8 HI-FI PDP CONCEPT ALPHA

**Execution case:** `bzpm-catalog-redesign`  
**Document:** `BZPM-PDP-HIFI-ALPHA-v1`  
**Phase:** W8 — Hi-Fi PDP Concept Alpha  
**Lane:** A (Website Factory)  
**Mode:** High-Fidelity Concept — no implementation  
**Date:** 2026-06-09  

**Approved visual blend:** **70% Mockup B** (primary base) · **30% Mockup A** (visual moderation)

**Source of truth (unchanged IA):**  
[BZPM-PDP-MOCKUP-B-v1](BZPM-PDP-MOCKUP-B-v1.md) · [BZPM-PDP-MOCKUP-A-v1](BZPM-PDP-MOCKUP-A-v1.md) · [BZPM-PDP-WIREFRAME-ALPHA-v1](BZPM-PDP-WIREFRAME-ALPHA-v1.md) · [BZPM-PDP-CONCEPT-ALPHA-v1](BZPM-PDP-CONCEPT-ALPHA-v1.md)

**Reference SKU:** Ванна моечная ВМЦ-П3-2/500 (моечные ванны, серия ПРЕМИУМ-3)  
**Audit environment:** https://zpm.new-site.space/

**Rule:** Stakeholder-facing visual concept only. No OpenCart. No Twig. No CSS. No JS. No design system tokens. No new architecture. No audit reopening.

**Blend formula:** *«Инструмент выбора для снабжения»* (B) с *«узнаваемым BZPM, наконец собранным правильно»* (A).

---

## Visual Principles

### Зачем страница выглядит именно так

Hi-Fi Alpha — первый **реалистичный** визуальный артефакт будущей PDP BZPM. Он отвечает на вопрос stakeholder: *«Как это будет выглядеть в жизни, а не в wireframe?»*

Концепт строится на утверждённом направлении **70/30**:

| Источник | Доля | Что даёт |
|----------|------|----------|
| **Mockup B** | 70% | Series band, data-first hero, attribute grid, integrated commercial row, table-continuity min spec, procurement scan speed |
| **Mockup A** | 30% | Узнаваемая buy box, чуть крупнее медиа, мягче whitespace в prose-зонах, carousel-slot для in-series alts, chip-подписи в grid |

**Формула ощущения:** OEM-заводской каталог с инженерной плотностью — но не ERP-таблица и не marketplace-карточка.

### Визуальный язык (описательно)

| Слой | Принцип | Как выражено в Alpha |
|------|---------|----------------------|
| **Палитра** | Нейтрально-промышленная | Фон страницы — светло-серый (#F4F5F7 аналог); контентные панели — белые карточки с тонкой границей; акцент — фирменный синий BZPM для CTA и series band; статус «В наличии» — сдержанный зелёный, не marketplace-badge |
| **Типографика** | Техническая иерархия | H1 — 24–28px, semi-bold, тёмно-графитовый; артикул — monospace-adjacent (tabular), 14px, средний контраст; метки атрибутов — 11–12px uppercase tracking; значения — 14–15px medium; цена — 28–32px bold, единственный крупный commercial signal |
| **Плотность** | Высокая, но с дыханием | Grid и band от B; межблочные отступы и prose padding от A — не «сухой datasheet» |
| **Формы** | Промышленная геометрия | Скругление 4–6px (не consumer 12px+); series band — full-width panel; buy box — отдельная карточка с лёгкой тенью (от A) |
| **Медиа** | Подтверждение, не декор | ~30% ширины hero (между B 25% и A 40%); 1 главное фото + 2–3 thumb — не lifestyle gallery void |

### Чем Hi-Fi Alpha отличается от текущей PDP BZPM

| Аспект | Текущая PDP | Hi-Fi Alpha |
|--------|-------------|-------------|
| **Первое впечатление** | «Карточка товара в интернет-магазине» | «Страница верификации SKU в серии ПРЕМИУМ-3» |
| **Серия** | Только в breadcrumb | **Series Context Band** — первая смысловая зона после навигации |
| **Hero** | Большая галерея + 4 габарита | Компактное фото + **8 decision-атрибутов** в grid + отдельная buy box |
| **Спецификации** | 2/3 вкладок скрыты | Min Spec Summary **виден сразу** на первом scroll |
| **Альтернативы** | «Похожие» — котломойки | **In-Series Alternatives** — только ПРЕМИУМ-3 |
| **Placeholder** | Mini-description, demo logo | **Подавлены** |
| **B2B** | Footer / deep scroll | Delivery + dealer **preview** рядом с CTA |

### Чего концепт намеренно избегает

- Marketplace feel (Trapeza-scale flatness, brand index, lifestyle imagery)
- ERP feel (full-screen spreadsheet, ERP column headers)
- Procurement software feel (multi-panel dashboard, filter sidebars on PDP)
- Corporate brochure feel (hero marketing prose, advantages grid, cert slider)

### Сохранённые structural invariants

Без изменения IA и decision flow Wireframe Alpha:

- Series Context · Fit Verification · Commercial Core · Min Spec Summary · In-Series Alternatives
- Block map USR-PDP-00–21
- Mobile P1–P5 reorder (commercial first)
- ID-01 dedup rules (hero subset ≠ full spec)

---

## Desktop Concept

**Viewport:** 1366×768 (primary review) · 1440px (design reference)  
**Content width:** ~1200px centered · 24px page gutters

### Page composition — full scroll map

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ SITE HEADER (existing — out of scope)                                       │
│ Logo · Каталог · Поиск · Дилерам · Корзина                                   │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ USR-PDP-00  BREADCRUMB — 13px, muted gray, single line                      │
│ Главная › Каталог › Нейтральное › Моечные ванны › ПРЕМИУМ-3 › ВМЦ-П3-2/500  │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ USR-PDP-02  SERIES CONTEXT BAND                              ◄── 70% from B │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ bg: light steel-blue tint · left accent bar 3px brand blue              │ │
│ │                                                                         │ │
│ │ СЕРИЯ  ПРЕМИУМ-3          Цельнотянутые ванны премиум-класса          │ │
│ │ [ Все модели серии (10) → ]     См. также: ПРЕМИУМ · СТАНДАРТ          │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ HERO PANEL — white card, 16px padding, subtle border                        │
│                                                                             │
│ ┌────────────────┬──────────────────────────────────────────────────────────┐│
│ │ USR-PDP-06     │ USR-PDP-01  IDENTITY                                     ││
│ │ MEDIA ~30%     │                                                          ││
│ │ (30% from A)   │ H1: Ванна моечная цельнотянутая 2-секционная             ││
│ │                │      500×400 мм, левая/правая чаша                       ││
│ │ ┌────────────┐ │                                                          ││
│ │ │            │ │ Артикул  ВМЦ-П3-2/500  [⧉ копировать]   ЗПМ · OEM      ││
│ │ │  product   │ │                                                          ││
│ │ │  photo     │ ├──────────────────────────────────────────────────────────┤│
│ │ │  4:3 ratio │ │ USR-PDP-04 + USR-PDP-05  FIT VERIFICATION GRID  ◄── B   ││
│ │ │            │ │ ┌────────────┬────────────┬────────────┬────────────┐    ││
│ │ └────────────┘ │ │ L          │ W          │ H          │ Масса      │    ││
│ │ [▪][▪][▪] thumbs│ │ 1150 мм    │ 700 мм     │ 850 мм     │ 68 кг      │    ││
│ │                │ ├────────────┼────────────┼────────────┼────────────┤    ││
│ │                │ │ Секций     │ Чаша       │ Материал   │ Конструкция│    ││
│ │                │ │ 2          │ 500×400    │ AISI 304   │ Цельнотян. │    ││
│ │                │ └────────────┴────────────┴────────────┴────────────┘    ││
│ │                │ labels: 11px caps gray · values: 15px dark · chip borders ││
│ └────────────────┴──────────────────────────────────────────────────────────┘│
│                                                                             │
│ ┌─────────────────────────────┬─────────────────────────────────────────────┐│
│ │ USR-PDP-03  BUY BOX         │ USR-PDP-07 + USR-PDP-18 preview            ││
│ │ (30% from A — isolated card)│ (70% from B — integrated row)             ││
│ │ ┌─────────────────────────┐ │                                             ││
│ │ │ ● В наличии · 3 шт.     │ │ [ Сравнить ]  [ В избранное ]             ││
│ │ │                         │ │ Доставка: от 3 дн. →  ·  Купить как дилер →││
│ │ │ 142 500 ₽               │ │                                             ││
│ │ │ Кол-во  [ −  1  + ]     │ │                                             ││
│ │ │                         │ │                                             ││
│ │ │ [  В КОРЗИНУ  ]  ◄◄CTA  │ │                                             ││
│ │ │ full-width brand blue   │ │                                             ││
│ │ └─────────────────────────┘ │                                             ││
│ └─────────────────────────────┴─────────────────────────────────────────────┘│
│                                                                             │
│  ─ ─ ─ ─ ─ ─ ─ FIRST SCREEN FOLD (1366×768) ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ ZONE 2 — FIRST SCROLL                                                         │
│                                                                             │
│ USR-PDP-09  MINIMUM SPEC SUMMARY — table continuation, DEFAULT VISIBLE      │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ Ключевые параметры                                                      │ │
│ │ ─────────────────────────────────────────────────────────────────────  │ │
│ │ Количество секций     │  2                                              │ │
│ │ Материал              │  AISI 304                                       │ │
│ │ Тип конструкции       │  Цельнотянутая                                  │ │
│ │ Вес нетто             │  65 кг                                          │ │
│ │ Вес брутто            │  72 кг                                          │ │
│ │ Габариты упаковки     │  1200 × 750 × 900 мм                            │ │
│ │ Гарантия              │  24 мес.                                        │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ USR-PDP-08  DESCRIPTION — comfortable prose (30% from A)                  │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ Моечная ванна цельнотянутая двухсекционная для профессиональных         │ │
│ │ кухонь, столовых и пищеблоков. Левая и правая чаша 500×400 мм.           │ │
│ │ Комплектация: ванна, сифон, крепёжный комплект. Ключевое отличие        │ │
│ │ серии ПРЕМИУМ-3 — цельнотянутая конструкция без сварных швов в чаше.    │ │
│ │ [ Показать полностью ▼ ]                                                │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ USR-PDP-19  CONSULTATIVE CTA — inline text links, not hero banner         │
│ [ Задать вопрос ]   [ Поможем подобрать ]                                   │
│                                                                             │
│ USR-PDP-10  FULL SPECS — collapsed                                          │
│ [ Характеристики — развернуть все 24 параметра ▼ ]                          │
│                                                                             │
│ USR-PDP-11  DOCUMENTS                                                       │
│ 📄 Паспорт ВМЦ-П3.pdf   📄 Сертификат соответствия.pdf                      │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ ZONE 3 — DEEP SCROLL                                                          │
│                                                                             │
│ USR-PDP-12  IN-SERIES ALTERNATIVES — hybrid B density + A carousel slot     │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ Другие модели серии ПРЕМИУМ-3                                           │ │
│ │ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │ │
│ │ │ thumb    │ │ thumb    │ │ thumb    │ │ thumb    │ │ thumb    │  →    │ │
│ │ │ВМЦ-П3-1/5│ │ВМЦ-П3-2/6│ │ВМЦ-П3-3/5│ │ВМЦ-П3-2/7│ │ВМЦ-П3-1/6│       │ │
│ │ │1150×600  │ │1400×700  │ │1150×700  │ │1400×850  │ │1150×600  │       │ │
│ │ │1 сек     │ │2 сек     │ │3 сек     │ │2 сек     │ │1 сек     │       │ │
│ │ │98 200 ₽  │ │156 800 ₽ │ │178 400 ₽ │ │189 500 ₽ │ │94 100 ₽  │       │ │
│ │ │● В налич.│ │● Под зак.│ │● В налич.│ │● В налич.│ │● В налич.│       │ │
│ │ └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘       │ │
│ │ horizontal scroll · card width ~200px · familiar «похожие» footprint    │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ USR-PDP-14  [ ← Вернуться к серии ПРЕМИУМ-3 ]                               │
│ USR-PDP-17  Сопутствующее оборудование (2 cards, labeled, deprioritized)    │
│ USR-PDP-20/21  Trust micro · legal one-liners                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Proportions and spacing (desktop)

| Zone | Width / height | Notes |
|------|----------------|-------|
| Series band | 100% content · ~56–64px height | Full-width tint panel; mandatory series name + link |
| Hero card | 100% · ~420–480px total | Fits in one viewport with breadcrumb + band on 1366×768 |
| Media column | ~30% (~360px at 1200) | Between B 25% and A 40% — moderation |
| Data column | ~70% | Identity + grid + buy row |
| Fit grid | 4×2 cells · ~36px row height | B structure; A chip-like cell borders |
| Buy box | ~280–320px wide · right-aligned in hero footer row | A isolation — visually distinct white card |
| Min spec table | 100% · 7 rows visible | B table-continuity |
| In-series cards | 5 visible + scroll · 200px card | A carousel familiarity; B data density per card |

### Real content examples (ВМЦ-П3-2/500)

| Field | Value in concept |
|-------|------------------|
| H1 | Ванна моечная цельнотянутая 2-секционная 500×400 мм, левая/правая чаша |
| Article | ВМЦ-П3-2/500 |
| Series | ПРЕМИУМ-3 |
| Series descriptor | Цельнотянутые ванны премиум-класса |
| Sibling count | 10 SKU in series |
| Dimensions | L 1150 × W 700 × H 850 мм |
| Mass | 68 кг |
| Sections | 2 |
| Bowl | 500×400 мм |
| Material | AISI 304 |
| Construction | Цельнотянутая |
| Price | 142 500 ₽ |
| Stock | В наличии · 3 шт. |
| Delivery preview | от 3 дн. |
| Siblings shown | ВМЦ-П3-1/500, ВМЦ-П3-2/600, ВМЦ-П3-3/500, ВМЦ-П3-2/700, ВМЦ-П3-1/600 |

*Values illustrative from audit/CMS context — final numbers = content ops.*

### Visual weight distribution (Hi-Fi Alpha)

```text
Series band   ████████████████████  highest — selection continuity (B)
Fit grid      ████████████████░░░░  high — engineering scan (B)
Buy box       ████████████████░░░░  high — isolated card (A moderation)
Commercial    ██████████████░░░░░░  high — price + CTA dominant
Media         ██████████░░░░░░░░░░  medium — larger than B, smaller than A
Description   ██████░░░░░░░░░░░░░░  medium — first scroll, comfortable (A)
In-series     ████████░░░░░░░░░░░░  medium-high — elevated cards (blend)
```

---

## Mobile Concept

**Viewport:** 375×667 (iPhone SE class) · 390×844 (primary modern)  
**Touch targets:** min 44px height for CTA and actions

### Mobile composition — priority blocks

```text
┌──────────────────────────────┐
│ SITE HEADER (compact)        │
├──────────────────────────────┤
│ USR-PDP-00 Breadcrumb        │
│ … › ПРЕМИУМ-3 › ВМЦ-П3-2/500 │
│ 12px · truncated middle    │
├──────────────────────────────┤
│ ══ P1 CRITICAL ══            │
│                              │
│ USR-PDP-03 COMMERCIAL  ◄◄ 1st│
│ ┌──────────────────────────┐ │
│ │ ● В наличии · 3 шт.      │ │
│ │ 142 500 ₽                │ │
│ │ [ −  1  + ]              │ │
│ │ [    В КОРЗИНУ    ]      │ │
│ │ sticky optional — TBD    │ │
│ └──────────────────────────┘ │
│                              │
│ USR-PDP-02 SERIES BAND       │
│ ┌──────────────────────────┐ │
│ │ СЕРИЯ ПРЕМИУМ-3           │ │
│ │ Цельнотянутые ванны…      │ │
│ │ [ Все модели (10) → ]     │ │
│ └──────────────────────────┘ │
│ 2 lines max · B band · A pad │
│                              │
│ USR-PDP-01 IDENTITY          │
│ ВМЦ-П3-2/500  [⧉]            │
│ H1 (2 lines, 20px)           │
│                              │
│ USR-PDP-04/05 FIT GRID       │
│ ┌───────────┬───────────┐    │
│ │ L 1150    │ W 700     │    │
│ │ H 850     │ 68 кг     │    │
│ ├───────────┼───────────┤    │
│ │ 2 сек     │ 500×400   │    │
│ │ AISI 304  │ Цельнот.  │    │
│ └───────────┴───────────┘    │
│ 2-col key-value · B grid     │
│                              │
│ Доставка от 3 дн. →         │
│ Купить как дилер →          │
├──────────────────────────────┤
│ ══ P2 HIGH ══                │
│ [ Сравнить ] [ Избранное ]   │
│                              │
│ USR-PDP-09 Min Spec (5 rows) │
│ key-value stack · default on │
├──────────────────────────────┤
│ ══ P3 MEDIUM ══              │
│                              │
│ USR-PDP-12 In-Series Alts    │
│ ┌────────┐ ┌────────┐ →     │
│ │ sibling│ │ sibling│ scroll │
│ │ card   │ │ card   │       │
│ └────────┘ └────────┘       │
│                              │
│ USR-PDP-19 Consult links     │
│ USR-PDP-08 Desc (3 lines)    │
├──────────────────────────────┤
│ ══ P4 LOWER ══               │
│ USR-PDP-10 Full specs ▼      │
│ USR-PDP-11 Documents         │
│                              │
│ USR-PDP-06 MEDIA             │
│ ┌──────────────────────────┐ │
│ │ hero image — full width  │ │
│ │ 16:9 crop                │ │
│ │ [▪][▪][▪] thumb strip    │ │
│ └──────────────────────────┘ │
│ A moderation: one image may  │
│ peek if P1 fits on 390×844   │
├──────────────────────────────┤
│ ══ P5 COLLAPSE ══            │
│ Cross-family · extended desc │
│ Trust micro · legal          │
└──────────────────────────────┘
```

### Mobile first-screen priorities

| Priority | Block | Rationale |
|----------|-------|-----------|
| **1** | Commercial Core | MO-01: CTA before gallery scroll |
| **2** | Series band | WH-13: series visible without breadcrumb decode |
| **3** | Article + H1 | SKU identity for search/article arrivals |
| **4** | Fit grid | WH-14: category-critical beyond 4 dims |
| **5** | B2B one-liner | WH-15 preview — not full Zone 6 |

### Mobile moderation from Mockup A

- Series band keeps **2-line comfortable padding** — not compressed single-line strip
- On **390×844+** devices, optional **peek of hero image** between fit grid and P2 fold (A gallery warmth — not P1)
- In-series block uses **horizontal card carousel** (familiar thumb + article pattern) not stacked table
- Buy box remains **full-width isolated card** with clear CTA — not flat inline-only

### Mobile commercial visibility

```text
Above fold on 390×844 (target):
  ✓ Price · status · qty · CTA
  ✓ Series name + link
  ✓ Article
  ✓ 8 fit attributes (2×4 grid)
  ~ Delivery/dealer links (may touch fold)
  ✗ Full min spec — P2
  ✗ Gallery — P4 (or peek on tall phones)
```

---

## First Screen Review

### Visible information map (desktop, 1366×768)

| # | Block | Visible fact | Decision support |
|---|-------|--------------|------------------|
| 1 | Breadcrumb | Path to ПРЕМИУМ-3 | Navigation context |
| 2 | Series band | ПРЕМИУМ-3 · descriptor · 10 SKU link · adjacent series | **D3: Correct series?** |
| 3 | Media | Product photo + 3 thumbs | Visual confirm (parallel) |
| 4 | H1 + article | Full name · ВМЦ-П3-2/500 · copy | **D6: Correct model?** |
| 5 | Fit grid | 8 attributes | **D6 partial: Suitable?** |
| 6 | Buy box | Status · qty · price · CTA | **D7: Available?** |
| 7 | Actions + B2B | Compare · fav · delivery · dealer | D9 path · B2B preview |

**Approx. decision-useful facts on first screen:** ~16–18 (between Mockup A ~14 and B ~20 — blend target)

### Information hierarchy (descending weight)

```text
TIER 1 — IMMEDIATE (0–3 sec)
  Series band name «ПРЕМИУМ-3»
  Article «ВМЦ-П3-2/500»
  Price «142 500 ₽»
  Status «В наличии»

TIER 2 — VERIFICATION (3–6 sec)
  Fit grid 8 cells
  H1 full product name
  Primary CTA

TIER 3 — CONFIRMATION (6–10 sec)
  Product photo
  Delivery/dealer links
  Compare / favorites
  Series sibling count link
```

### Expected user scan path

**Persona A — снабженец с артикулом:**

```text
Article (verify) → Series band (confirm ПРЕМИУМ-3) → Fit grid (dims) → Price/CTA → Cart
Time: ~5–8 sec
```

**Persona B — инженер из series grid:**

```text
Series band (continuity) → Fit grid (sections, bowl, material) → Min spec scroll → Compare alt
Time: ~8–12 sec
```

**Persona C — новый покупатель:**

```text
Photo (recognition) → H1 → Series band (what line?) → Fit grid → Price → Scroll desc
Time: ~10–15 sec
```

### 5–10 second gate check

| Question | Answered on first screen? | Block |
|----------|---------------------------|-------|
| What series? | **Yes** | USR-PDP-02 band |
| What model? | **Yes** | USR-PDP-01 + USR-PDP-04 |
| Is it suitable? | **Partial** — full confirm needs min spec scroll | USR-PDP-05 grid |
| Is it available? | **Yes** | USR-PDP-03 |
| What alternatives? | **Deferred** — intentional | USR-PDP-12 below fold |

**Gates closed on first screen:** 3.5 of 5 (same as Wireframe Alpha; packaging denser than Mockup A)

### Fold boundary

- **Above fold:** USR-PDP-00 through USR-PDP-07 + USR-PDP-18 preview
- **First pixel below fold:** USR-PDP-09 Min Spec Summary header
- **Design intent:** buyer sees spec confirmation **within first scroll gesture**, not hidden tab

---

## Current vs Alpha

### Side-by-side — first screen

```text
CURRENT BZPM PDP                    HI-FI ALPHA
─────────────────────               ─────────────────────
Breadcrumb only series              Breadcrumb + SERIES BAND

┌──────────┬──────────┐            ┌────┬─────────────────┐
│          │ H1       │            │img │ H1 + article    │
│ GALLERY  │ mini-desc│            │30% │ FIT GRID 4×2    │
│ ~45%     │ placeholder│          │    ├─────────────────┤
│          │ ┌──────┐ │            │    │ BUY BOX │ actions│
│          │ │ BUY  │ │            └────┴─────────────────┘
│          │ └──────┘ │
└──────────┴──────────┘
L W H mass (4 only)                 8 attrs + series + B2B preview

[Описание][Характеристики][▼]       Min spec VISIBLE on scroll
tabs — 2/3 hidden                   No inactive tab regression

«Похожие товары»                    «Другие модели серии ПРЕМИУМ-3»
(cross-family)                      (in-series only)
```

### Comparison matrix

| Criterion | Current PDP | Hi-Fi Alpha | Delta |
|-----------|-------------|-------------|-------|
| **Information density** | Low — ~6 facts, specs in tabs | **High-moderate** — ~16–18 facts first screen | +170% visible decision data |
| **Series visibility** | Breadcrumb terminal only | **Prominent band** + sibling link | WH-13 addressed |
| **Commercial clarity** | Good price/CTA; B2B absent near CTA | **Buy box isolated** + delivery/dealer preview | WH-15 partial fix at P1 |
| **SKU validation** | 4 dims | **8 attrs in grid** | WH-14 addressed |
| **Decision speed (expert)** | Fast price; slow fit | **Fast series + fit + price** in one viewport | Mockup B speed, A familiarity |
| **Decision speed (novice)** | Slow tab discovery | Moderate — grid + photo peek | Better than B alone |
| **Recognizability** | Baseline | **Moderate-high** — buy box + carousel slot from A | Lower shock than pure B |
| **Gallery void (WH-16)** | High void | **Reduced** — 30% not 45% | Mitigated, not eliminated |

### Qualitative stakeholder read

| Stakeholder question | Answer in Hi-Fi Alpha |
|---------------------|----------------------|
| «Что изменилось?» | Серия на первом экране; 8 параметров вместо 4; specs без вкладок; правильные альтернативы |
| «Почему изменилось?» | PDP = верификация SKU в серии, не карточка одного артикула |
| «Это всё ещё BZPM?» | Да — заводская номенклатура, OEM-серии, B2B CTA; не marketplace |
| «Это слишком радикально?» | Меньше шока чем pure B — buy box и carousel узнаваемы |

### Density visualization

```text
FIRST-SCREEN PAYLOAD (relative)

Current       ████░░░░░░░░░░░░░░░░  ~30%
Mockup A      ████████░░░░░░░░░░░░  ~65%
Hi-Fi Alpha   ████████████░░░░░░░░  ~75%   ← 70/30 blend
Mockup B      ██████████████░░░░░░  ~90%

RECOGNIZABILITY (relative)

Current       ████████████████░░░░  high (but broken IA)
Mockup A      ████████████████████  highest
Hi-Fi Alpha   ██████████████░░░░░░  good
Mockup B      ████████░░░░░░░░░░░░  lower
```

---

## Risks

### What still needs validation

| ID | Risk / question | Why it matters | Suggested validation |
|----|-----------------|----------------|----------------------|
| **V-01** | Fold line on 1366×768 with real header | Band + grid + buy box may push fit grid below fold on short laptops | Screenshot test with production header height |
| **V-02** | 70/30 blend perception | Stakeholder may want more A (gallery) or more B (density) | Side-by-side workshop: Alpha vs pure A vs pure B |
| **V-03** | Series band empty states | Empty descriptor collapses band awkwardly | Test with 3 CMS content tiers |
| **V-04** | Mobile P1 viewport overflow | Band + grid + commercial on 375×667 | OQ-09 device test — mandatory |
| **V-05** | In-series card data completeness | Sibling cards need L×W×H, sections, price, status per SKU | Content ops audit for ПРЕМИУМ-3 series |
| **V-06** | Non-sink families (OQ-01) | Grid columns differ for столы / тепловое | Placeholder concept pass before rollout |
| **V-07** | Compare table attributes (OQ-04) | Compare button visible; populated compare UX unknown | U-02 — out of W8 scope |
| **V-08** | CMS relation for siblings (OQ-02) | In-series block depends on series-scoped relation | Engineering spike |

### What may overload the page

| Overload vector | Severity | Mitigation in Alpha |
|-----------------|----------|---------------------|
| Series band + grid + buy box on first screen | **Medium–High** | A buy box isolation creates visual pause; band is one line of actions max |
| 8 grid cells + 7 min spec rows overlap | Medium | ID-01: min spec adds logistics only (net/gross, packaging) |
| B2B links competing with CTA | Low–Medium | Dealer/delivery = text links, not buttons; CTA = sole filled button |
| In-series carousel + cross-family below | Low | Cross-family suppressed to 2 cards, labeled «Сопутствующее» |
| Mobile P1 stack (5 blocks) | **High** | Collapsible series descriptor on <390px — design option, not decided |

### What depends on real content

| Content slot | Block | If empty |
|--------------|-------|----------|
| Series descriptor | USR-PDP-02 | Band shows name + link only — acceptable |
| Category-critical props | USR-PDP-05 | Grid cells show «—» — **unacceptable** for launch; content gate |
| Min spec rows | USR-PDP-09 | Block collapses to «Характеристики уточняются» + consult CTA |
| Sibling relations | USR-PDP-12 | Block suppressed; USR-PDP-14 return-to-series only |
| Product images | USR-PDP-06 | Placeholder equipment silhouette — not demo logo |
| Documents | USR-PDP-11 | Empty state + consult link |
| Delivery summary | USR-PDP-18 | Link hidden if no data (OQ-03) |

### Stakeholder-facing risks

| Risk | Likelihood | Notes |
|------|------------|-------|
| «Слишком плотно для наших клиентов» | Medium | A moderation intentional — workshop can shift to 60/40 |
| «Галерея слишком мала» | Medium | 30% vs current 45% — trade for WH-16 |
| «Series band — лишнее» | Low | Core Alpha differentiator — non-negotiable in concept |
| «Похожие товары исчезли» | Low–Medium | Merchandising brief: in-series replaces, cross-family demoted |

---

## Readiness

### Concept readiness checklist

| Criterion | Status | Notes |
|-----------|--------|-------|
| IA / block map unchanged | **READY** | USR-PDP-00–21 preserved |
| Decision flow unchanged | **READY** | Wireframe Alpha ladder intact |
| 70/30 blend documented | **READY** | B base + A moderation explicit |
| Real SKU content examples | **READY** | ВМЦ-П3-2/500 throughout |
| Desktop first-screen composition | **READY** | Proportions + fold boundary defined |
| Mobile priority map | **READY** | P1–P5 with commercial first |
| Current vs Alpha comparison | **READY** | Stakeholder diff articulated |
| Risks and content dependencies | **READY** | Validation list for W8.1/W9 |
| Implementation handoff | **NOT IN SCOPE** | No CSS/Twig/JS — designer Figma next |
| Final design approval | **PENDING** | Human evaluation gate |

### Recommended next steps (post-review)

| # | Step | Owner |
|---|------|-------|
| 1 | Stakeholder review session — «что изменилось / почему / ощущение BZPM» | Website Factory + client |
| 2 | Fold-line photography — 1366×768, 375×667 with production header | Design |
| 3 | Figma hi-fi mockup from this brief (single direction) | Design |
| 4 | Blend ratio adjustment if needed (60/40 or 80/20) | Workshop decision |
| 5 | OQ-02 engineering spike for in-series relations | OCPilot |
| 6 | Content ops: series descriptor + min spec rows for ПРЕМИУМ-3 pilot | Content |

### Gate question for stakeholder

> **«Если завтра PDP BZPM выглядел так — это ближе к желаемому будущему каталога ЗПМ, чем текущая страница?»**

Если **да** → proceed to Figma refinement (W8.1) and pilot SKU implementation planning.  
Если **частично** → adjust blend ratio or single element (band weight, gallery size, in-series format).  
Если **нет** → return to Mockup A or B pure direction — not architecture.

---

## Traceability

| Hi-Fi element | Primary source | Blend note |
|---------------|----------------|------------|
| Series band | Mockup B USR-PDP-02 | 70% — full band |
| Fit grid 4×2 | Mockup B USR-PDP-04/05 | 70% — table structure |
| Buy box isolation | Mockup A USR-PDP-03 | 30% — separate card |
| Media ~30% | Blend | Between A 40% / B 25% |
| Integrated B2B row | Mockup B USR-PDP-18 preview | 70% |
| Min spec table | Mockup B USR-PDP-09 | 70% |
| Description padding | Mockup A USR-PDP-08 | 30% |
| In-series carousel | Mockup A USR-PDP-12 slot | 30% — B data per card |
| Mobile commercial P1 | Wireframe Alpha P-09 | 100% — invariant |
| Block sequence | Wireframe Alpha | 100% — invariant |

---

## Document lineage

| Input | Role |
|-------|------|
| [BZPM-PDP-MOCKUP-B-v1](BZPM-PDP-MOCKUP-B-v1.md) | Primary visual base (70%) |
| [BZPM-PDP-MOCKUP-A-v1](BZPM-PDP-MOCKUP-A-v1.md) | Visual moderation (30%) |
| [BZPM-PDP-WIREFRAME-ALPHA-v1](BZPM-PDP-WIREFRAME-ALPHA-v1.md) | Structural baseline |
| [BZPM-PDP-CONCEPT-ALPHA-v1](BZPM-PDP-CONCEPT-ALPHA-v1.md) | Concept «Серийная верификация» |
| [BZPM-PDP-MOCKUP-COMPARISON-v1](BZPM-PDP-MOCKUP-COMPARISON-v1.md) | Hybrid path rationale |

---

*BZPM-PDP-HIFI-ALPHA-v1 — high-fidelity concept for stakeholder review only. Not final design. Not implementation.*
