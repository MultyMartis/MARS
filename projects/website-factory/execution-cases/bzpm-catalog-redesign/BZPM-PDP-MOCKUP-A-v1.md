# REPORT — BZPM PDP MOCKUP A

**Execution case:** `bzpm-catalog-redesign`  
**Document:** `BZPM-PDP-MOCKUP-A-v1`  
**Phase:** W7 — PDP Mockup Exploration  
**Direction:** A — Conservative Evolution  
**Lane:** A (Website Factory)  
**Mode:** Visual direction exploration — no implementation  
**Date:** 2026-06-09  

**Source of truth (unchanged IA):**  
[BZPM-REDESIGN-ARCHITECTURE-v1](BZPM-REDESIGN-ARCHITECTURE-v1.md) · [BZPM-BLUEPRINT-v1](BZPM-BLUEPRINT-v1.md) · [BZPM-UX-STRUCTURE-v1](BZPM-UX-STRUCTURE-v1.md) · [BZPM-PDP-CONCEPT-ALPHA-v1](BZPM-PDP-CONCEPT-ALPHA-v1.md) · [BZPM-PDP-WIREFRAME-ALPHA-v1](BZPM-PDP-WIREFRAME-ALPHA-v1.md)

**Reference SKU:** ВМЦ-П3-2/500 (моечные ванны, серия ПРЕМИУМ-3)  
**Audit environment:** https://zpm.new-site.space/

**Rule:** Same block map (USR-PDP-00–21), same decision ladder, same zone sequence. **Visual packaging only** — layout weight, density rhythm, decorative footprint.

**Guiding question:** *«Что если текущий BZPM пересобрали правильно?»*

---

## Section A — Direction Philosophy

### Кому служит

| Профиль | Потребность |
|---------|-------------|
| **Текущий BZPM-покупатель** | Узнаваемая карточка товара без «революции интерфейса» |
| **Менеджмент / stakeholder** | Эволюция, а не смена DNA — низкий шок при презентации клиенту |
| **Снабженец с артикулом** | Привычная схема «фото слева — покупка справа» + исправленные пробелы Alpha |
| **Покупатель из серии** | Серия и fit-параметры видны, но не доминируют над привычной галереей |

### Зачем существует

Mockup A переводит Concept Alpha **«Серийная верификация»** в визуальный язык, **максимально близкий к текущей PDP BZPM**: двухколоночный hero, заметная галерея, buy box справа. Все архитектурные исправления (series context, category-critical props, min spec visible, in-series alternatives) **встроены**, но поданы как **естественное улучшение**, а не новый продуктовый паттерн.

### Главные сильные стороны

- **Узнаваемость:** layout читается как «наш сайт, только лучше»
- **Низкий stakeholder risk:** не требует объяснения радикальной смены паттерна
- **Умеренный прирост плотности:** +series line, +4 category-critical props, min spec без tab — без table-first overload
- **Сохранение медиа-якоря:** галерея остаётся визуально значимой — комфорт для визуально ориентированных покупателей
- **Плавный handoff:** дизайнер может эволюционировать существующую тему OpenCart, не строить новый visual system с нуля

### Главные риски

- **Недостаточная дифференциация от текущего:** исправления IA могут выглядеть «косметическими», если stakeholder ожидает «новый BZPM»
- **Галерея снова доминирует:** WH-16 (space-to-meaning mismatch) может частично сохраниться
- **Series context может быть пропущен:** если серия — одна строка под H1, слабее WH-13 mitigation, чем в Mockup B
- **First screen может не вместить fit verification:** классический tall gallery + buy box сжимает Zone C

---

## Section B — First Screen Mockup

**Viewport:** desktop ~1280–1440px  
**Fold line:** ниже USR-PDP-07 (как Wireframe Alpha), но **композиция ближе к текущему BZPM**

### Desktop schematic — first screen

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  [ SITE HEADER ]                                                            │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  USR-PDP-00  Breadcrumb                                                     │
│  Главная › Каталог › … › ПРЕМИУМ-3 › Ванна моечная …                        │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  HERO — «CLASSIC BZPM» two-column + compact fit strip                       │
│                                                                             │
│  ┌─────────────────────────────┬─────────────────────────────────────────┐│
│  │  USR-PDP-06  MEDIA           │  USR-PDP-01  IDENTITY                     ││
│  │  ┌─────────────────────┐    │  H1: Ванна моечная цельнотянутая …         ││
│  │  │                     │    │  Артикул: ВМЦ-П3-2/500  [ copy ]          ││
│  │  │   [ product image ] │    │                                           ││
│  │  │   familiar size     │    │  USR-PDP-02  SERIES (subtle line)         ││
│  │  │   ~40% width        │    │  Серия: ПРЕМИУМ-3 → все модели серии      ││
│  │  │                     │    │  (one line — not full band)               ││
│  │  │  [ thumb ][ thumb ] │    │  ─────────────────────────────────────    ││
│  │  └─────────────────────┘    │  USR-PDP-03  COMMERCIAL CORE              ││
│  │                              │  ┌───────────────────────────────────┐  ││
│  │                              │  │ ● В наличии · 3 шт.               │  ││
│  │                              │  │ 142 500 ₽                         │  ││
│  │                              │  │ Qty [ - 1 + ]                     │  ││
│  │                              │  │ [ В КОРЗИНУ ]          ◄◄ buy box │  ││
│  │                              │  └───────────────────────────────────┘  ││
│  │                              │  USR-PDP-07  [ Сравнить ] [ Избранное ]  ││
│  └─────────────────────────────┴─────────────────────────────────────────┘│
│                                                                             │
│  USR-PDP-04 + USR-PDP-05  FIT VERIFICATION — compact horizontal strip      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  L 1150 │ W 700 │ H 850 │ 68 кг │ 2 сек │ чаша 500×400 │ AISI 304 │   │   │
│  │  Цельнотянутая                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│  (single row — familiar «selected properties» pattern, extended)           │
│                                                                             │
│  ─ ─ ─ ─ ─ ─ ─ FIRST SCREEN FOLD (desktop) ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   │
└─────────────────────────────────────────────────────────────────────────────┘

VISUAL WEIGHT (Mockup A):
  Gallery ████████████░░░░░░░░  (high — like current BZPM)
  Buy box ████████████████░░░░  (high — familiar anchor)
  Series  ██████░░░░░░░░░░░░░░  (medium-low — line under title)
  Fit     ████████░░░░░░░░░░░░  (medium — one strip, not table)
```

### Отличия от Mockup B на first screen

| Element | Mockup A | Mockup B (contrast) |
|---------|----------|---------------------|
| Series context | Одна строка под H1 | Prominent band / header strip |
| Media | ~40% width, tall gallery | ~25% width, thumbnail-first |
| Fit verification | Horizontal chip strip | Dense attribute grid / table rows |
| Commercial | Classic right buy box | Integrated into data panel |
| Decorative space | Moderate whitespace | Minimal |

---

## Section C — PDP Structure Visualization

**Block sequence:** идентичен Wireframe Alpha — USR-PDP-00 → 21. Меняется только **visual rhythm**, не порядок зон.

### Desktop page flow

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ P1 ─ FIRST SCREEN                                                           │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ USR-PDP-00 Breadcrumb                                                   │ │
│ │ [ Gallery 40% ] [ Identity + Series line + Buy box ]                    │ │
│ │ USR-PDP-04/05 Fit strip (compact) · USR-PDP-07 actions                  │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────────────────┤
│ P2 ─ FIRST SCROLL (confirmation — familiar tab-adjacent feel)               │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ USR-PDP-08 Description (prose block — comfortable line length)           │ │
│ │ USR-PDP-09 Min Spec Summary (card-style, 5–8 rows — DEFAULT ON)         │ │
│ │ USR-PDP-19 Consultative CTA (inline strip, not hero-sized)              │ │
│ │ USR-PDP-10 Full Specs [ Характеристики ▼ ] collapsed                    │ │
│ │ USR-PDP-11 Documents entry                                              │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────────────────┤
│ P3 ─ DEEP SCROLL (selection support — standard e-commerce depth)            │
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ USR-PDP-12 In-Series Alternatives (card carousel — familiar «похожие»   │ │
│ │   slot, but scoped + relabeled)                                         │ │
│ │ USR-PDP-13 Compare feedback · USR-PDP-14 Return-to-series               │ │
│ │ USR-PDP-15/16 Reference · USR-PDP-17 Cross-family (labeled, below)      │ │
│ │ USR-PDP-18/20/21 Commercial detail · trust micro · legal                │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘

Priority legend:
  P1 = decision gate (series · model · availability · fit subset)
  P2 = spec confirmation + consult path
  P3 = alternatives · reference · B2B detail
```

### Mobile page flow

```text
┌──────────────────────────┐
│ P1 — CRITICAL            │
│ USR-PDP-03 Commercial    │  ◄◄ first (P-09 rule preserved)
│   price · status · CTA   │
│ USR-PDP-02 Series line   │  (compact — not full band)
│ USR-PDP-01 Article + H1  │
│ USR-PDP-04/05 Fit chips  │  (wrapped row, 2 lines max)
├──────────────────────────┤
│ P2 — HIGH                │
│ USR-PDP-07 Compare/fav   │
│ USR-PDP-09 Min spec       │
├──────────────────────────┤
│ P3 — MEDIUM              │
│ USR-PDP-12 In-series alts│
│ USR-PDP-19 Consult CTA   │
│ USR-PDP-08 Description   │
├──────────────────────────┤
│ P4 — LOWER               │
│ USR-PDP-06 Media         │  (elevated vs desktop — still P4)
│ USR-PDP-10 Full specs    │
│ Docs · compare feedback  │
├──────────────────────────┤
│ P5 — COLLAPSE            │
│ Cross-family · extended  │
│ commercial detail        │
└──────────────────────────┘

Mockup A mobile note: gallery deprioritized but **less aggressively**
than Mockup B — one hero image may peek above fold on large phones.
```

---

## Section D — Information Density

### Evaluation vs Current and Mockup B

| Metric | Current PDP | Mockup A | Mockup B |
|--------|-------------|----------|----------|
| **Density** | Low (4 hero props, tabs hide specs) | **Moderate** (+series, +4 critical, min spec visible) | High (table-first hero) |
| **Clarity** | Weak series/alternatives path | **Good** — familiar layout lowers learning cost | Very good for experts; steeper for casual |
| **Scan speed (expert)** | Fast for price/article only | **Good** — fit strip scannable in one row | **Fastest** — all attrs in grid |
| **Scan speed (new buyer)** | Slow (hidden tabs) | **Good** — visual anchors unchanged | Medium — less gallery guidance |
| **Procurement suitability** | Weak B2B near CTA | **Improved** — commercial detail + consult elevated | **Strong** — procurement panel integrated |

### Mockup A density profile

```text
Information layers visible without tab click:

  Current:  ~6 facts (title, article, 4 dims, price, status)
  Mockup A: ~14 facts (+ series, +4 critical, +compare labels)
  Mockup B: ~18+ facts (+ dense grid, + series band, + inline logistics hints)

Visual whitespace:

  Current:  HIGH (gallery void — WH-16)
  Mockup A: MEDIUM (gallery retained; strip uses space efficiently)
  Mockup B: LOW (decorative footprint reduced)
```

**Packaging rule preserved:** hero subset ≠ full spec table (ID-01). Mockup A keeps differentiation through **strip vs card vs collapsed table**, not duplication.

---

## Section E — Visual Character

**Derived from concept — not assumed.**

| Character label | How Mockup A expresses it |
|-----------------|---------------------------|
| **OEM** | Заводская номенклатура (артикул prominent), серия как строка, не marketplace brand |
| **Manufacturer** | Галерея оборудования сохраняет «заводской каталог» feel |
| **Industrial** | Присутствует через fit strip, но смягчено whitespace |
| **Technical** | Category-critical attrs visible, но в chip-row, не engineering table |
| **Procurement** | Buy box dominant; B2B detail на scroll — не hero clutter |
| **Engineering** | Min spec + collapsed full table — достаточно для ТЗ, без datasheet density |

**Overall feel:** *«Знакомый BZPM, наконец собранный правильно»* — evolution, not revolution.

**Not this direction:** marketplace (Trapeza-scale flatness), SaaS dashboard, consumer e-commerce lifestyle PDP.

---

## Section F — Risk Analysis

### Potential overload

| Risk | Severity | Mitigation in Mockup A |
|------|----------|------------------------|
| Fit strip + buy box + gallery compete | Medium | Single-row strip; no second column of attrs |
| Min spec + strip overlap (ID-01) | Low–Medium | Strip = snapshot; min spec adds logistics rows only |
| Mobile P1 stack length | Medium | Same as Wireframe Alpha; OQ-09 device test |

### Potential stakeholder resistance

| Risk | Likelihood | Notes |
|------|------------|-------|
| «Слишком похоже на текущее — зачем redesign?» | **Medium** | Need side-by-side with **current pain points** labeled |
| «Series line слишком мелкая» | Low–Medium | Stakeholder may push toward Mockup B band |
| Loss of misaligned «Похожие» merchandising | Low | In-series block occupies familiar carousel slot |

### Potential implementation complexity

| Area | Complexity | Reason |
|------|------------|--------|
| Theme evolution | **Low** | Extends existing 2-column PDP pattern |
| CMS blocks | Medium | Same 22 blocks as blueprint — registry mapping unchanged |
| Content fill | Medium | Series descriptor, min spec rows, in-series relations (OQ-02) |
| Mobile reorder | Medium | P-09 commercial-first — same as wireframe |

### Potential mobile risks

- Gallery at P4 may frustrate visual-first mobile buyers (accepted tradeoff per G6)
- Fit chip wrap on narrow screens — risk of 3+ lines before scroll (OQ-09)
- Series one-liner may truncate on small viewports — need ellipsis + link intact

---

## Section G — Comparison Matrix (direction snapshot)

| Criterion | Current | Mockup A | Mockup B |
|-----------|---------|----------|----------|
| Information Density | Low | **Moderate** | High |
| Series Visibility | Breadcrumb only | **Line under title** | Prominent band |
| SKU Validation | 4 dims | **Strip + 4 critical** | Dense grid |
| Procurement Support | Header only | **Elevated on scroll** | Integrated panel |
| Mobile Readability | CTA below gallery | **Commercial first** | Commercial + data first |
| Commercial Clarity | Good price/status | **Good + familiar buy box** | Excellent — unified panel |
| Stakeholder Risk | N/A (baseline) | **Low** | Medium |
| Implementation Risk | N/A | **Low–Medium** | Medium |

*Full matrix: [BZPM-PDP-MOCKUP-COMPARISON-v1](BZPM-PDP-MOCKUP-COMPARISON-v1.md)*

---

## Section H — When to Prefer Mockup A

**Prefer A when:**

- Client/stakeholder prioritizes **recognizability** over maximum density
- Rollout must feel like **fix**, not **replatform**
- Visual design budget assumes **theme evolution**, not new design system
- Buyer base mixes **visual confirmation** (gallery) with procurement — not expert-only
- First client-facing mockup should **minimize shock** before deeper iteration

**Test visually next (if A selected):**

1. Series line weight — one line vs subtle badge (still not full B band)
2. Gallery height vs fit strip — fold line on 1366×768
3. In-series carousel styling — familiar «похожие» slot with new label
4. Min spec card vs inline table — packaging without tab regression

---

## Traceability

| Mockup element | Source block |
|----------------|--------------|
| Two-column hero | Current BZPM pattern + Wireframe Zones A–D |
| Series line | USR-PDP-02 |
| Fit strip | USR-PDP-04 + USR-PDP-05 |
| Buy box | USR-PDP-03 |
| Min spec default-visible | USR-PDP-09 (W1A-F-05 fix) |
| In-series alternatives | USR-PDP-12 (W1A-F-06 fix) |

---

*BZPM-PDP-MOCKUP-A-v1 — visual direction exploration only. No UI kit. No CSS. No Twig. No JS. No OpenCart.*
