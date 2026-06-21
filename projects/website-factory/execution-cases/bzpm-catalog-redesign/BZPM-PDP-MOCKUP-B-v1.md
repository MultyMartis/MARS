# REPORT — BZPM PDP MOCKUP B

**Execution case:** `bzpm-catalog-redesign`  
**Document:** `BZPM-PDP-MOCKUP-B-v1`  
**Phase:** W7 — PDP Mockup Exploration  
**Direction:** B — Industrial Procurement  
**Lane:** A (Website Factory)  
**Mode:** Visual direction exploration — no implementation  
**Date:** 2026-06-09  

**Source of truth (unchanged IA):**  
[BZPM-REDESIGN-ARCHITECTURE-v1](BZPM-REDESIGN-ARCHITECTURE-v1.md) · [BZPM-BLUEPRINT-v1](BZPM-BLUEPRINT-v1.md) · [BZPM-UX-STRUCTURE-v1](BZPM-UX-STRUCTURE-v1.md) · [BZPM-PDP-CONCEPT-ALPHA-v1](BZPM-PDP-CONCEPT-ALPHA-v1.md) · [BZPM-PDP-WIREFRAME-ALPHA-v1](BZPM-PDP-WIREFRAME-ALPHA-v1.md)

**Reference SKU:** ВМЦ-П3-2/500 (моечные ванны, серия ПРЕМИУМ-3)  
**Audit environment:** https://zpm.new-site.space/

**Rule:** Same block map (USR-PDP-00–21), same decision ladder, same zone sequence. **Visual packaging only** — density, series prominence, procurement-first composition.

**Guiding question:** *«Что если BZPM проектировали вокруг скорости выбора?»*

---

## Section A — Direction Philosophy

### Кому служит

| Профиль | Потребность |
|---------|-------------|
| **Снабженец / инженер** | Максимум decision data above fold; минимум decorative scroll |
| **Repeat buyer ЗПМ** | Быстрая верификация серии + артикула + параметров без «карточки магазина» |
| **B2B procurement** | Lead time, delivery, dealer path **рядом с данными**, не в footer |
| **Buyer из series grid (ПРЕМИУМ-3)** | Series context **как якорь страницы** — продолжение selection surface |

### Зачем существует

Mockup B выражает Concept Alpha **«Серийная верификация»** через **procurement-first visual language**: series context как header band, атрибуты в table-like grid, компактное медиа, commercial block встроен в data panel. IA и decision flow **идентичны** Wireframe Alpha — меняется **скорость сканирования** и **decorative footprint**.

### Главные сильные стороны

- **Maximum information efficiency:** больше decision facts на first screen без новых backend-полей (P-05)
- **Strong series visibility:** WH-13 закрывается визуально сильнее, чем в Mockup A
- **Procurement alignment:** B2B signals adjacent to conversion — WH-15, CV-01
- **Selection speed:** expert path article → verify → cart укорачивается (qualitative; no numeric claims)
- **Reduced gallery void:** WH-16 mitigation — media supporting, not dominating

### Главные риски

- **Stakeholder shock:** не похоже на текущий BZPM — может восприниматься как «чужой» интерфейс
- **Cognitive overload для casual buyer:** table density без привычной галереи
- **Brand warmth loss:** industrial density может ослабить «manufacturer catalog» feel для новых buyers
- **Mobile P1 length:** commercial + series band + attribute grid — OQ-09 critical

---

## Section B — First Screen Mockup

**Viewport:** desktop ~1280–1440px  
**Fold line:** ниже USR-PDP-07; **composition = data panel + compact media**

### Desktop schematic — first screen

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  [ SITE HEADER ]                                                            │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  USR-PDP-00  Breadcrumb (compact single line)                               │
│  Главная › … › ПРЕМИУМ-3 › ВМЦ-П3-2/500                                     │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  USR-PDP-02  SERIES CONTEXT BAND                              ◄◄◄ STRONG   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  СЕРИЯ: ПРЕМИУМ-3  │  Цельнотянутые ванны премиум-класса            │   │
│  │  [ → Все SKU серии (10) ]  │  См. также: ПРЕМИУМ · СТАНДАРТ         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  HERO — PROCUREMENT PANEL (data-first)                                      │
│                                                                             │
│  ┌────────┐  ┌──────────────────────────────────────────────────────────┐  │
│  │ USR-   │  │  USR-PDP-01  IDENTITY                                    │  │
│  │ PDP-06 │  │  H1: Ванна моечная цельнотянутая 2-секционная …           │  │
│  │ MEDIA  │  │  Артикул: ВМЦ-П3-2/500  [ copy ]  │  ЗПМ · OEM           │  │
│  │ ┌────┐ │  ├──────────────────────────────────────────────────────────┤  │
│  │ │img │ │  │  USR-PDP-04 + USR-PDP-05  FIT VERIFICATION GRID          │  │
│  │ │~25%│ │  │  ┌──────────────┬──────────────┬──────────────┬─────────┐ │  │
│  │ └────┘ │  │  │ L: 1150 мм   │ W: 700 мм    │ H: 850 мм    │ 68 кг   │ │  │
│  │ [+2]   │  │  ├──────────────┼──────────────┼──────────────┼─────────┤ │  │
│  │ thumbs │  │  │ Секций: 2    │ Чаша: 500×400│ AISI 304     │ Цельнот.│ │  │
│  │        │  │  └──────────────┴──────────────┴──────────────┴─────────┘ │  │
│  └────────┘  ├──────────────────────────────────────────────────────────┤  │
│              │  USR-PDP-03  COMMERCIAL + USR-PDP-07  (integrated row)   │  │
│              │  ┌────────────────────────────────────────────────────┐  │  │
│              │  │ ● В наличии · 3 шт.  │  142 500 ₽  │ Qty [1]        │  │  │
│              │  │ [ В КОРЗИНУ ]  │  [ Сравнить ]  │  [ Избранное ]   │  │  │
│              │  │ Доставка: от 3 дн. →  │  Купить как дилер →         │  │  │
│              │  └────────────────────────────────────────────────────┘  │  │
│              └──────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ─ ─ ─ ─ ─ ─ ─ FIRST SCREEN FOLD (desktop) ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   │
└─────────────────────────────────────────────────────────────────────────────┘

VISUAL WEIGHT (Mockup B):
  Series band ████████████████████  (highest — selection continuity)
  Fit grid    ████████████████░░░░  (high — table scan)
  Commercial  ████████████████░░░░  (high — inline panel)
  Media       ██████░░░░░░░░░░░░░░  (low — confirm only)
  Whitespace  ██░░░░░░░░░░░░░░░░░░  (minimal decorative)
```

### Отличия от Mockup A на first screen

| Element | Mockup A | Mockup B |
|---------|----------|----------|
| Series context | Subtle line under H1 | **Full-width band above hero** |
| Media | ~40% tall gallery | **~25% thumbnail + strip** |
| Fit verification | Horizontal chip strip | **2×4 attribute grid** |
| Commercial | Isolated buy box (right) | **Integrated procurement row** |
| B2B hints | Deferred to scroll | **Delivery + dealer inline** (USR-PDP-18 preview) |
| Adjacent series | Not on first screen | **Compact links in series band** |

---

## Section C — PDP Structure Visualization

### Desktop page flow

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ P1 ─ FIRST SCREEN                                                           │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ USR-PDP-00 Breadcrumb (compact)                                         │ │
│ │ USR-PDP-02 SERIES BAND ─────────────────────────────── dominant         │ │
│ │ [ thumb ] │ Identity │ FIT GRID │ Commercial+Actions row               │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────────────────┤
│ P2 ─ FIRST SCROLL (spec + consult — dense, minimal prose padding)           │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ USR-PDP-09 Min Spec Summary (table continuation — 5–8 rows) DEFAULT ON  │ │
│ │ USR-PDP-08 Description (compact — 3–4 lines visible, expand rest)       │ │
│ │ USR-PDP-19 Consultative CTA (text links — not large image block)        │ │
│ │ USR-PDP-10 Full Specs [ Развернуть все характеристики ▼ ]               │ │
│ │ USR-PDP-11 Documents (inline file list)                                 │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────────────────┤
│ P3 ─ DEEP SCROLL (alternatives elevated vs Mockup A desktop)                │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ USR-PDP-12 In-Series Alternatives (compact table/cards — 6 SKU)         │ │
│ │   columns: article · L×W×H · sects · price · status · [→]              │ │
│ │ USR-PDP-13 Compare · USR-PDP-14 Return-to-series                        │ │
│ │ USR-PDP-18 Commercial detail (expand if not fully in P1)                 │ │
│ │ USR-PDP-15/16 Reference · USR-PDP-17 Cross-family (minimal)             │ │
│ │ USR-PDP-20/21 Trust micro · legal (single line each)                    │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘

Mockup B structural emphasis:
  P2 starts with USR-PDP-09 (spec table feel) before long USR-PDP-08 prose
  P3 in-series block higher / denser than Mockup A carousel
```

### Mobile page flow

```text
┌──────────────────────────┐
│ P1 — CRITICAL            │
│ USR-PDP-03 Commercial    │  ◄◄ first block
│   status · price · CTA   │
│ USR-PDP-02 Series band   │  ◄◄ full width — 2 lines
│   ПРЕМИУМ-3 · link       │
│ USR-PDP-01 Article       │
│ USR-PDP-04/05 Attr grid  │  ◄◄ 2-col key-value pairs
│   (not chip strip)       │
│ Delivery/dealer one-liner│  (USR-PDP-18 preview)
├──────────────────────────┤
│ P2 — HIGH                │
│ USR-PDP-09 Min spec table│
│ USR-PDP-07 Compare/fav   │
├──────────────────────────┤
│ P3 — MEDIUM              │
│ USR-PDP-12 In-series     │  ◄◄ elevated vs Wireframe desktop
│   (horizontal / stack)   │
│ USR-PDP-19 Consult links │
│ USR-PDP-08 Desc (short)  │
├──────────────────────────┤
│ P4 — LOWER               │
│ USR-PDP-10 Full specs    │
│ USR-PDP-11/15 Docs        │
│ USR-PDP-06 Media strip   │  ◄◄ still P4 — smaller thumb row
├──────────────────────────┤
│ P5 — COLLAPSE            │
│ Cross-family · extended  │
│ desc · trust micro       │
└──────────────────────────┘
```

---

## Section D — Information Density

### Evaluation vs Current and Mockup A

| Metric | Current PDP | Mockup A | Mockup B |
|--------|-------------|----------|----------|
| **Density** | Low | Moderate | **High** |
| **Clarity** | Weak IA packaging | Good (familiar) | **Very good for experts**; harder for novices |
| **Scan speed (expert)** | Fast (price only) | Good | **Fastest** — grid + band |
| **Scan speed (new buyer)** | Slow | **Good** | Medium — less visual guidance |
| **Procurement suitability** | Weak | Improved | **Strongest** |

### Mockup B density profile

```text
Facts visible on first screen (no tab):

  Current:  ~6
  Mockup A: ~14
  Mockup B: ~18–20 (+ series band meta, + B2B one-liner, + grid structure)

Decorative footprint:

  Current:  HIGH void (gallery)
  Mockup A: MEDIUM
  Mockup B: LOW — every block earns decision weight

Scan pattern:

  Mockup B buyer reads top-down:
    Series band → Article → Grid → Commercial row
  (vs Mockup A: Gallery ∥ Identity/Buy ∥ Strip)
```

**ID-01 preserved:** grid = hero subset; USR-PDP-09 adds logistics rows; USR-PDP-10 = full record.

---

## Section E — Visual Character

**Derived from concept composition — not assumed.**

| Character label | How Mockup B expresses it |
|-----------------|---------------------------|
| **Procurement** | Commercial + delivery + dealer in one panel row |
| **Industrial** | Table grids, minimal prose, reduced lifestyle whitespace |
| **Technical** | Attribute grid reads as spec sheet fragment |
| **Engineering** | Min spec as table continuation; full spec expand |
| **OEM** | Series band + article — not marketplace brand hero |
| **Manufacturer** | ЗПМ OEM marker inline with identity — not third-party logo |

**Overall feel:** *«Инструмент выбора для снабжения»* — selection instrument, not shop window.

**Not this direction:** consumer lifestyle PDP, image-first fashion card, Trapeza marketplace density at taxonomy level (R-01 preserved — OEM series band, not functional chip replacement).

---

## Section F — Risk Analysis

### Potential overload

| Risk | Severity | Notes |
|------|----------|-------|
| First-screen attribute grid + series band + commercial | **High** | 18–20 facts before scroll — expert-friendly, novice-heavy |
| ID-01 overlap grid ↔ min spec | Medium | Must enforce logistics-only repeat in USR-PDP-09 |
| Multiple inline links (series, dealer, delivery) | Medium | CTA hierarchy from Wireframe §G must hold |

### Potential stakeholder resistance

| Risk | Likelihood | Notes |
|------|------------|-------|
| «Не похоже на наш сайт» | **High** | Primary resistance driver for Mockup B |
| «Слишком сухо / не продаёт» | Medium | Marketing may prefer Mockup A gallery |
| Pushback on shrinking gallery | Medium | WH-16 fix conflicts with emotional product presentation |

### Potential implementation complexity

| Area | Complexity | Reason |
|------|------------|--------|
| Theme change | **Medium–High** | New layout paradigm vs current 2-column |
| Responsive grid | Medium–High | Attribute grid reflow rules across breakpoints |
| Series band component | Medium | New visual block — same USR-PDP-02 data |
| Content density | Medium | Empty CMS fields collapse band — empty states critical |

### Potential mobile risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| P1 exceeds one viewport | **High** | OQ-09 mandatory; consider collapsible band |
| 2-col attr grid wraps to 6+ lines | High | Priority attrs only in P1; rest in P2 min spec |
| Media at P4 | Medium | Accept for procurement persona; test with stakeholders |
| Series band truncation | Medium | Series name + count mandatory; descriptor optional |

---

## Section G — Comparison Matrix (direction snapshot)

| Criterion | Current | Mockup A | Mockup B |
|-----------|---------|----------|----------|
| Information Density | Low | Moderate | **High** |
| Series Visibility | Breadcrumb only | Line under title | **Prominent band** |
| SKU Validation | 4 dims | Fit strip | **Dense grid** |
| Procurement Support | Header only | Elevated on scroll | **Integrated P1** |
| Mobile Readability | CTA below gallery | Commercial first | Commercial + band + grid |
| Commercial Clarity | Good price/status | Familiar buy box | **Unified panel** |
| Stakeholder Risk | N/A | Low | **Medium–High** |
| Implementation Risk | N/A | Low–Medium | **Medium–High** |

*Full matrix: [BZPM-PDP-MOCKUP-COMPARISON-v1](BZPM-PDP-MOCKUP-COMPARISON-v1.md)*

---

## Section H — When to Prefer Mockup B

**Prefer B when:**

- Primary persona = **снабженец / инженер / repeat B2B buyer**
- Stakeholder explicitly wants **«не как сейчас»** — visible break from broken current PDP
- Selection speed matters more than **gallery-led discovery**
- Series-first catalog strategy (W2-F-10 ПРЕМИУМ-3 benchmark) should **continue onto PDP**
- Client accepts **industrial visual language** for equipment catalog

**Test visually next (if B selected):**

1. Series band content tiers — mandatory vs optional lines (OQ-12)
2. Grid column count at 1280 / 1024 / 768 — when to collapse to min spec only
3. USR-PDP-18 split — how much B2B stays in P1 vs Zone 6
4. In-series block as **table vs cards** — procurement scan preference
5. Mobile band collapse — accordion vs sticky series chip

---

## Traceability

| Mockup element | Source block |
|----------------|--------------|
| Series band | USR-PDP-02 (+ optional adjacent series hint from USR-SP-04 pattern) |
| Fit grid | USR-PDP-04 + USR-PDP-05 |
| Integrated commercial row | USR-PDP-03 + USR-PDP-07 + partial USR-PDP-18 |
| Compact media | USR-PDP-06 (zone assigned; reduced footprint) |
| Table-style min spec | USR-PDP-09 |
| Dense in-series block | USR-PDP-12 |

---

*BZPM-PDP-MOCKUP-B-v1 — visual direction exploration only. No UI kit. No CSS. No Twig. No JS. No OpenCart.*
