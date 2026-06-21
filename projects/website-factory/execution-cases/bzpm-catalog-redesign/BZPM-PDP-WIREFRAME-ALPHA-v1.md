# REPORT — BZPM PDP WIREFRAME ALPHA

**Execution case:** `bzpm-catalog-redesign`  
**Document:** `BZPM-PDP-WIREFRAME-ALPHA-v1`  
**Phase:** W6B — PDP Wireframe Alpha  
**Lane:** A (Website Factory)  
**Mode:** Wireframe — no UI, no design system, no branding, no implementation  
**Date:** 2026-06-09  
**Evidence base:** [BZPM-PDP-CONCEPT-ALPHA-v1](BZPM-PDP-CONCEPT-ALPHA-v1.md) · [BZPM-REDESIGN-ARCHITECTURE-v1](BZPM-REDESIGN-ARCHITECTURE-v1.md) · [BZPM-BLUEPRINT-v1](BZPM-BLUEPRINT-v1.md) · [BZPM-UX-STRUCTURE-v1](BZPM-UX-STRUCTURE-v1.md) · [BZPM-VISUAL-UX-PROTOTYPE-v1](BZPM-VISUAL-UX-PROTOTYPE-v1.md)

**Audit environment:** https://zpm.new-site.space/  
**Reference SKU:** ВМЦ-П3-2/500 (моечные ванны, серия ПРЕМИУМ-3)

**Rule:** This document defines **structure**, **hierarchy**, **screen composition**, and **decision flow** only. No colors, typography, CSS, Twig, JS, or OpenCart work.

---

## Section A — Wireframe Philosophy

### Зачем существует этот wireframe

`BZPM-PDP-WIREFRAME-ALPHA-v1` — первый разрешённый артефакт визуализации будущей PDP BZPM. Он переводит утверждённый концепт **«Серийная верификация»** (Concept Alpha) в **полную низкофиделити схему страницы**, которую stakeholder, дизайнер и инженер OCPilot могут читать без возврата к аудитам W0–W2.

Wireframe отвечает на один gate-вопрос: **может ли покупатель за 5–10 секунд понять серию, модель, пригодность, наличие и путь к альтернативам?** Если схема этого не поддерживает — wireframe считается проваленным.

### Чем wireframe отличается от текущей PDP

| Аспект | Текущая PDP | Wireframe Alpha |
|--------|-------------|-----------------|
| Роль страницы | Карточка одного SKU | Поверхность **верификации SKU внутри OEM-серии** |
| Серия | Только в breadcrumbs | **Series Context Block** на первом экране (USR-PDP-02) |
| Hero-свойства | 4 props (L×W×H×mass) | + category-critical props: секции, чаша, материал, конструкция |
| Спецификации | 2/3 вкладок скрыты при загрузке | **Minimum Spec Summary** default-visible; full spec — expand/tab |
| «Похожие товары» | Cross-family (котломойки на sink PDP) | **In-Series Alternatives** — только SKU той же серии |
| Placeholder / demo | Mini-description, AssuM logo | **Подавлены** в hero |
| Trust / commercial | Certificates, dealer form на deep scroll | Micro-signals compact; full blocks **suppressed** |

### Как wireframe выражает Concept Alpha

Концепт Alpha зафиксировал четыре tier информации и decision ladder. Wireframe **не переоткрывает** концепт — он **раскладывает** его в:

1. **Семь evaluation zones** (Blueprint Zones 0–6 → USR-PDP-00–21).
2. **Hero internal zones A–D** — composition rule для первого экрана.
3. **Fold boundary** — что до scroll, на первом scroll, на deep scroll.
4. **Mobile P1–P5** — decision-equivalent reorder (commercial first).
5. **Packaging decisions** — inline vs expand для Tier 2, без возврата к hidden-tab problem.

**Принцип:** visible packaging ≠ more data (P-05). Wireframe перераспределяет ownership существующих фактов, не изобретает backend-поля.

---

## Section B — Desktop Wireframe

**Viewport reference:** ~1280–1440px width (wireframe assumption; not a design breakpoint).  
**Block IDs:** USR-PDP-00–21 per [BZPM-UX-STRUCTURE-v1](BZPM-UX-STRUCTURE-v1.md).

### Full desktop schematic

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  [ SITE HEADER — out of page scope ]                                        │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  ZONE 0 — GLOBAL                                                            │
│  USR-PDP-00  Breadcrumb Block                                               │
│  Главная › Каталог › Нейтральное › Моечные ванны › ПРЕМИУМ-3 › [SKU]        │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  ZONE 1 — HERO (first screen boundary ends after USR-PDP-03)                │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  PRODUCT HERO — three-column composition                             │   │
│  │                                                                      │   │
│  │  ┌──────────────────┬────────────────────────┬───────────────────┐ │   │
│  │  │  ZONE A          │  ZONE B                │  ZONE D             │ │   │
│  │  │  Media             │  Identity + Series     │  Commercial Core    │ │   │
│  │  │  USR-PDP-06        │  USR-PDP-01             │  USR-PDP-03         │ │   │
│  │  │                    │  H1: Ванна моечная…    │  Статус: В наличии  │ │   │
│  │  │  [ product image ] │  Артикул: ВМЦ-П3-2/500  │  N шт.              │ │   │
│  │  │  (1+ images)       │  [ copy ]              │  Цена: XXX XXX ₽    │ │   │
│  │  │                    │                        │  Qty: [ - 1 + ]     │ │   │
│  │  │                    │  USR-PDP-02            │  [ В КОРЗИНУ ]  ◄◄  │ │   │
│  │  │                    │  Серия: ПРЕМИУМ-3       │                     │ │   │
│  │  │                    │  [ → все SKU серии ]   │  Lead time (if      │ │   │
│  │  │                    │  Tier: цельнотянутая     │  под заказ)         │ │   │
│  │  └──────────────────┴────────────────────────┴───────────────────┘ │   │
│  │                                                                      │   │
│  │  ZONE C — Fit Verification (full hero width, below 3-column row)    │   │
│  │  USR-PDP-04  Selected Properties                                     │   │
│  │  ┌────────────────────────────────────────────────────────────────┐  │   │
│  │  │  L: 1150 мм  │  W: 700 мм  │  H: 850 мм  │  Масса: XX кг     │  │   │
│  │  └────────────────────────────────────────────────────────────────┘  │   │
│  │  USR-PDP-05  Category-Critical Properties                            │   │
│  │  ┌────────────────────────────────────────────────────────────────┐  │   │
│  │  │  Секций: 2  │  Чаша: 500×400  │  AISI 304  │  Цельнотянутая   │  │   │
│  │  └────────────────────────────────────────────────────────────────┘  │   │
│  │  USR-PDP-07  Secondary Actions                                       │   │
│  │  [ Сравнить ]  [ В избранное ]  (labeled — not icon-only)           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ FIRST SCREEN FOLD LINE (desktop) ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  ZONE 2 — PRIMARY (default-visible — first meaningful scroll)               │
│                                                                             │
│  USR-PDP-08  Description Block                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Назначение · комплектация · ключевые отличия                        │   │
│  │  (structured prose — NOT placeholder mini-description)              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  USR-PDP-09  Minimum Spec Summary Block                    ◄── DEFAULT ON  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Ключевые параметры (5–8 строк)                                     │   │
│  │  ─────────────────────────────────────────────────────────────────  │   │
│  │  Количество секций      │  2                                        │   │
│  │  Материал               │  AISI 304                                 │   │
│  │  Тип конструкции        │  Цельнотянутая                            │   │
│  │  Вес нетто              │  XX кг                                    │   │
│  │  Вес брутто             │  XX кг                                    │   │
│  │  Габариты упаковки      │  XXX × XXX × XXX                          │   │
│  │  (rows NOT duplicated verbatim from Zone C without logistics value) │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  USR-PDP-19  Consultative CTA Block                         ◄── ELEVATED   │
│  [ Задать вопрос ]  [ Поможем подобрать ]                                   │
│                                                                             │
│  USR-PDP-10  Full Specifications Block                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  [ Характеристики ▼ ]  — collapsed by default; expand or tab        │   │
│  │  (20+ rows — complete technical record)                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  USR-PDP-11  Documents Entry Block                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Документы: [ PDF 1 ] [ PDF 2 ] [ Сертификат ]  — or empty state  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  ZONE 3 — SECONDARY (scroll-required — selection support)                   │
│                                                                             │
│  USR-PDP-12  In-Series Alternatives Block              ◄── REPLACES «Похожие»│
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Другие модели серии ПРЕМИУМ-3                                      │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐               │   │
│  │  │ sibling  │ │ sibling  │ │ sibling  │ │ sibling  │  (3–6 cards)  │   │
│  │  │ article  │ │ article  │ │ article  │ │ article  │               │   │
│  │  │ L×W×H    │ │ L×W×H    │ │ L×W×H    │ │ L×W×H    │               │   │
│  │  │ sects    │ │ sects    │ │ sects    │ │ sects    │               │   │
│  │  │ price    │ │ price    │ │ price    │ │ price    │               │   │
│  │  │ status   │ │ status   │ │ status   │ │ status   │               │   │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘               │   │
│  │  SCOPE RULE: same series ONLY — never cross-family here             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  USR-PDP-13  Compare Feedback Block                                         │
│  «Добавлено к сравнению · [ Перейти к сравнению ]»                         │
│                                                                             │
│  USR-PDP-14  Return-to-Series Block                                         │
│  [ ← Вернуться к серии ПРЕМИУМ-3 ]  (preserves filter state if any)        │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  ZONE 4 — REFERENCE (deep scroll)                                           │
│  USR-PDP-15  Full Documentation Block                                       │
│  USR-PDP-16  Extended Description Block (optional — collapse if long)       │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  ZONE 5 — RELATED (deprioritized — after in-series)                         │
│  USR-PDP-17  Cross-Family Related Block                                     │
│  Label: «Сопутствующее оборудование» — NOT «Похожие товары»                 │
│  (accessories / compatible only — valid relationships)                      │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  ZONE 6 — COMMERCIAL SUPPORT (conversion zone — may overlap first scroll)   │
│  USR-PDP-18  Commercial Detail Block                                          │
│  Lead time · доставка (summary + link) · [ Купить как дилер ]               │
│  USR-PDP-20  Trust Micro-Signals — «Сделано в России» · cert badge          │
│  USR-PDP-21  Legal Disclaimer — оферта / price disclaimer                   │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  [ SITE FOOTER ]                                                            │
└─────────────────────────────────────────────────────────────────────────────┘

SUPPRESSED ON PDP (never render):
  ✗ Misaligned «Похожие товары» (cross-family default position)
  ✗ Full dealer application form inline
  ✗ Full certificates slider
  ✗ Duplicate advantages grids
  ✗ In-page sibling SKU matrix (V-09)
  ✗ Placeholder mini-description in hero
  ✗ Demo brand logo (AssuM)
  ✗ Q&A community block
```

### Desktop block sequence (top to bottom)

```text
USR-PDP-00  Breadcrumb
USR-PDP-06  Media          ─┐
USR-PDP-01  Identity        │ Hero Zones A–D
USR-PDP-02  Series Context  │ (first screen)
USR-PDP-03  Commercial Core ─┘
USR-PDP-04  Selected Properties
USR-PDP-05  Category-Critical Properties
USR-PDP-07  Secondary Actions
USR-PDP-08  Description
USR-PDP-09  Minimum Spec Summary
USR-PDP-19  Consultative CTA
USR-PDP-10  Full Specifications (collapsed)
USR-PDP-11  Documents Entry
USR-PDP-12  In-Series Alternatives
USR-PDP-13  Compare Feedback
USR-PDP-14  Return-to-Series
USR-PDP-15  Full Documentation
USR-PDP-16  Extended Description
USR-PDP-17  Cross-Family Related
USR-PDP-18  Commercial Detail
USR-PDP-20  Trust Micro-Signals
USR-PDP-21  Legal Disclaimer
```

---

## Section C — Desktop Fold Analysis

### Fold zone definitions

| Zone | Scroll position | Wireframe boundary |
|------|-----------------|-------------------|
| **Before scroll** | First viewport — no meaningful scroll | Zone 0 + Hero (through USR-PDP-07) + top of USR-PDP-03 CTA visible |
| **First scroll** | One viewport down from fold | Zone 2 Primary: USR-PDP-08, 09, 19; top of USR-PDP-10 |
| **Deep scroll** | Two+ viewports | Zone 3–6: alternatives, reference, related, commercial detail |

**First screen fold line (desktop):** immediately below USR-PDP-07 Secondary Actions. USR-PDP-08 Description begins at or just below fold — buyer sees min spec summary within first meaningful scroll, not hidden in inactive tab.

---

### Before scroll — first viewport

**Visible blocks:**

| Block | Information shown |
|-------|-------------------|
| USR-PDP-00 | 4-level breadcrumb path |
| USR-PDP-06 | Product image (supporting — not information dominator) |
| USR-PDP-01 | H1, article code, copy affordance |
| USR-PDP-02 | Series name, link to series page, optional tier descriptor |
| USR-PDP-03 | Status, qty, price, qty selector, primary CTA |
| USR-PDP-04 | L×W×H×mass |
| USR-PDP-05 | Sections, bowl dims, material, construction |
| USR-PDP-07 | Labeled compare + favorites |

**5–10 second gate check:**

| Question | Answered by | Pass? |
|----------|-------------|-------|
| What series is this? | USR-PDP-02 | ✓ |
| What model is this? | USR-PDP-01 + USR-PDP-04 | ✓ |
| Is it suitable? | USR-PDP-05 (partial — full confirm needs scroll) | Partial |
| Is it available? | USR-PDP-03 | ✓ |
| What alternatives exist? | Not yet — **intentionally delayed** to Zone 3 | Deferred |

**Decision supported:** Correct series? · Correct model (dimensional)? · Available? — **three of five gates on first screen.**

**Intentionally delayed:**

- Full spec confirmation (USR-PDP-09/10) — first scroll
- In-series alternatives (USR-PDP-12) — deep scroll
- Cross-family related (USR-PDP-17) — deepest
- B2B delivery/dealer detail (USR-PDP-18) — first scroll or commercial zone end
- Consultation path (USR-PDP-19) — first scroll (elevated, not footer-only)

---

### First scroll — confirmation zone

**Visible blocks:**

| Block | Information shown |
|-------|-------------------|
| USR-PDP-08 | Назначение, комплектация, ключевые отличия |
| USR-PDP-09 | 5–8 key spec rows (default-visible) |
| USR-PDP-19 | Consultative CTA — «Задать вопрос» / «Поможем подобрать» |
| USR-PDP-10 | Full spec header + expand affordance (collapsed) |
| USR-PDP-11 | Document list or empty state |
| USR-PDP-18 | Lead time, delivery summary, dealer link (if not visible in hero) |

**Decision supported:** Correct specifications? · Need human help? · Documentation available?

**Intentionally delayed:**

- Complete 20+ row spec table — expand on demand (USR-PDP-10)
- Sibling SKU comparison — USR-PDP-12 below
- Extended marketing prose — USR-PDP-16 deep

**Packaging rule resolved (wireframe):** USR-PDP-08 and USR-PDP-09 are **inline default-visible** — not inactive tabs. USR-PDP-10 is **collapsed expand** below min summary. This prevents W1A-F-05 hidden-tab regression.

---

### Deep scroll — selection and reference

**Visible blocks:**

| Block | Information shown |
|-------|-------------------|
| USR-PDP-12 | 3–6 sibling SKU cards (same series) |
| USR-PDP-13 | Compare feedback state |
| USR-PDP-14 | Return-to-series with filter context |
| USR-PDP-15 | Full documentation package |
| USR-PDP-16 | Extended description (optional) |
| USR-PDP-17 | Cross-family accessories (labeled) |
| USR-PDP-20 | Trust micro-signals |
| USR-PDP-21 | Legal disclaimer |

**Decision supported:** Suitable alternative within series? · Continue browsing? · Procurement documentation? · Related equipment?

**Intentionally delayed:** Nothing critical remains — deep scroll is non-blocking for conversion if Tier 1–2 satisfied.

---

### Fold analysis summary

```text
BEFORE SCROLL     │ Series · Model · Availability · Fit subset
                  │ Gates: D3 · D6 partial · D7
──────────────────┼────────────────────────────────────────────
FIRST SCROLL      │ Specs confirm · Consult · Docs entry
                  │ Gates: D6 complete · D8 partial
──────────────────┼────────────────────────────────────────────
DEEP SCROLL       │ In-series alts · Reference · Cross-family
                  │ Gates: D6 alt · D9 compare
```

---

## Section D — Mobile Wireframe

**Rule:** Decision-equivalent information, not DOM parity (P-09). Commercial Core elevated to P1.

### Full mobile schematic — exact block order

```text
┌──────────────────────────┐
│  [ SITE HEADER ]         │
├──────────────────────────┤
│                          │
│  P4 (compact)            │
│  USR-PDP-00 Breadcrumb   │
│  Главная › … › ПРЕМИУМ-3 │
│                          │
│  ════════════════════════│
│  P1 — CRITICAL           │
│  ════════════════════════│
│                          │
│  USR-PDP-03              │  ◄◄◄ FIRST BLOCK
│  Commercial Core         │
│  ┌────────────────────┐  │
│  │ В наличии · N шт.  │  │
│  │ XXX XXX ₽          │  │
│  │ Qty [ - 1 + ]      │  │
│  │ [ В КОРЗИНУ ]      │  │
│  └────────────────────┘  │
│                          │
│  USR-PDP-02              │
│  Series Context          │
│  Серия: ПРЕМИУМ-3        │
│  [ → все SKU серии ]     │
│                          │
│  USR-PDP-01              │
│  ВМЦ-П3-2/500            │
│  H1 (abbreviated ok)     │
│  [ copy article ]        │
│                          │
│  USR-PDP-04 + USR-PDP-05 │
│  L 1150 · W 700 · H 850  │
│  2 сек · AISI 304        │
│  Цельнотянутая           │
│                          │
│  ════════════════════════│
│  P2 — HIGH               │
│  ════════════════════════│
│                          │
│  USR-PDP-07              │
│  [ Сравнить ]            │
│  [ В избранное ]         │
│  (labeled text)          │
│                          │
│  USR-PDP-09              │
│  Minimum Spec Summary    │
│  5–8 key rows            │
│  (default-visible)       │
│                          │
│  ════════════════════════│
│  P3 — MEDIUM             │
│  ════════════════════════│
│                          │
│  USR-PDP-12              │
│  In-Series Alternatives  │
│  ┌────────────────────┐  │
│  │ sibling card       │  │  horizontal scroll
│  │ article·dims·price │  │  or vertical stack
│  └────────────────────┘  │
│                          │
│  USR-PDP-19              │
│  [ Задать вопрос ]       │
│  [ Поможем подобрать ]   │
│                          │
│  USR-PDP-08              │
│  Description opening     │
│  (first 2–3 sentences)   │
│                          │
│  ════════════════════════│
│  P4 — LOWER              │
│  ════════════════════════│
│                          │
│  USR-PDP-10              │
│  Full Specifications     │
│  [ Развернуть ▼ ]        │
│                          │
│  USR-PDP-11 / USR-PDP-15 │
│  Documents               │
│                          │
│  USR-PDP-06              │
│  Media gallery           │
│  (deprioritized vs      │
│   desktop — P4)          │
│                          │
│  USR-PDP-13 Compare feed │
│  USR-PDP-14 Return link  │
│                          │
│  ════════════════════════│
│  P5 — COLLAPSE/SUPPRESS  │
│  ════════════════════════│
│                          │
│  USR-PDP-16 Extended desc │
│  USR-PDP-17 Cross-family │
│  USR-PDP-18 Commercial   │
│    detail (if not in P1) │
│  USR-PDP-20 Trust micro   │
│  USR-PDP-21 Legal         │
│  ✗ Certs slider          │
│  ✗ Dealer form           │
│                          │
├──────────────────────────┤
│  [ FOOTER ]              │
└──────────────────────────┘
```

### Mobile priority map (P1–P5)

| Priority | Blocks | Buyer question answered |
|----------|--------|------------------------|
| **P1** | USR-PDP-03, 02, 01, 04/05 | Available? · Right series? · Right SKU? · Fit? |
| **P2** | USR-PDP-07, 09 | Compare? · Key specs without tab? |
| **P3** | USR-PDP-12, 19, 08 | Alternatives? · Need help? · What is it for? |
| **P4** | USR-PDP-10, 11/15, 06, 13, 14 | Full specs · Docs · Visual confirm · Navigation |
| **P5** | USR-PDP-16, 17, 18, 20, 21 | Reference · Cross-family · Deep commercial |

### Mobile vs desktop reorder notes

| Block | Desktop position | Mobile position | Rationale |
|-------|------------------|-----------------|-----------|
| USR-PDP-03 Commercial | Hero Zone D (right column) | **P1 first** | MO-01: CTA must not wait for gallery scroll |
| USR-PDP-06 Media | Hero Zone A (left column) | **P4** | Visual confirm deferred; decision attrs first |
| USR-PDP-12 Alternatives | Zone 3 (deep) | **P3 elevated** | Mobile buyers need sibling path earlier than cross-family |
| USR-PDP-19 Consult | Zone 2 (first scroll) | **P3** | Elevated — not footer-only |

---

## Section E — Hero Composition

Hero = Zone 1 blocks USR-PDP-01 through USR-PDP-07 plus USR-PDP-06 and USR-PDP-03. Internal composition uses **four sub-zones A–D**.

### Hero layout model (desktop)

```text
┌────────────────────────────────────────────────────────────────┐
│  HERO COMPOSITION                                              │
│                                                                │
│  ROW 1 — three columns                                         │
│  ┌──────────────┬─────────────────────┬─────────────────────┐│
│  │  ZONE A      │  ZONE B             │  ZONE D             ││
│  │  Visual      │  Identity Gate      │  Commercial Gate    ││
│  │  Confirm     │  Series + SKU       │  Convert            ││
│  └──────────────┴─────────────────────┴─────────────────────┘│
│                                                                │
│  ROW 2 — full width                                            │
│  ┌──────────────────────────────────────────────────────────┐│
│  │  ZONE C — Fit Verification                                 ││
│  └──────────────────────────────────────────────────────────┘│
└────────────────────────────────────────────────────────────────┘
```

---

### Zone A — Visual Confirmation (USR-PDP-06)

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Visual identity confirmation — supporting, not dominator |
| **Inputs** | Product image(s) from CMS media |
| **Outputs** | Buyer confirms equipment appearance matches expectation |
| **Decision supported** | Correct model? (visual channel) |
| **Questions answered** | «Does this look like the equipment I expect?» |
| **Must NOT contain** | Misaligned related products; placeholder logos |

**Wireframe note:** Zone A occupies left column on desktop. Gallery footprint is assigned but **information priority** is lower than Zones B and D (WH-16 mitigation at IA level; layout height = design phase).

---

### Zone B — Identity + Series Gate (USR-PDP-01 + USR-PDP-02)

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Answer «what is this SKU?» and «am I in the right series?» — **key Alpha differentiator** |
| **Inputs** | H1 title; article code; copy affordance; series name; series page URL; optional one-line tier descriptor |
| **Outputs** | Unambiguous SKU ID; series affiliation visible without breadcrumb decode |
| **Decision supported** | Correct series? (D3 at SKU level) · Correct model? (identity) |
| **Questions answered** | «What model?» · «What article?» · «Which OEM series?» · «Is this ПРЕМИУМ-3, not ПРЕМИУМ or ЭКОНОМ?» |
| **Must NOT contain** | Placeholder mini-description; demo brand logo (AssuM) |

**Identity cluster rule (Concept Alpha):** USR-PDP-01 and USR-PDP-02 form one cognitive unit — «what this is and what series it belongs to».

---

### Zone C — Fit Verification (USR-PDP-04 + USR-PDP-05 + USR-PDP-07)

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Physical and functional fit check beyond price |
| **Inputs** | L×W×H×mass (USR-PDP-04); section count, bowl dims, material, construction (USR-PDP-05); compare + favorites toggles (USR-PDP-07) |
| **Outputs** | Structured fit snapshot; compare/wishlist action state |
| **Decision supported** | Correct model? (dimensional) · Correct specifications? (category-critical subset) · D9 compare path |
| **Questions answered** | «Will it fit my space?» · «How many sections?» · «What material/construction?» · «Can I compare?» |
| **ID-01 rule** | Hero props = decision subset only — not full spec table duplicate |

**Моечные ванны v1 minimum (USR-PDP-05):**

| Property | Example value |
|----------|---------------|
| Section count | 2 |
| Bowl dimensions | 500×400 мм |
| Material | AISI 304 |
| Construction | Цельнотянутая |

---

### Zone D — Commercial Gate (USR-PDP-03)

| Attribute | Definition |
|-----------|------------|
| **Purpose** | D7 availability and conversion — **highest decision weight in hero** |
| **Inputs** | Availability status; qty when in stock; price; qty selector; primary CTA; lead time when под заказ |
| **Outputs** | Purchase-ready state |
| **Decision supported** | Available? · Ready to purchase? |
| **Questions answered** | «In stock?» · «How many?» · «What price?» · «Can I order now?» |
| **Hierarchy rule** | Primary CTA (cart) = dominant action; lead time inline when под заказ |

**CTA hierarchy (wireframe resolution):**

```text
1. PRIMARY    [ В корзину ]           — USR-PDP-03
2. SECONDARY  [ Сравнить ]            — USR-PDP-07
3. TERTIARY   [ Задать вопрос ]       — USR-PDP-19 (Zone 2, first scroll)
4. QUATERNARY [ Купить как дилер ]    — USR-PDP-18 (link, not competing button)
```

---

### Hero composition — 5–10 second validation

```text
Second 0–2:  Zone B → «ПРЕМИУМ-3 · ВМЦ-П3-2/500»     → series + model
Second 2–4:  Zone C → «1150×700×850 · 2 сек · 304»   → suitability
Second 4–6:  Zone D → «В наличии · цена · CTA»       → availability
Second 6–8:  Zone A → visual confirm (parallel scan)
Second 8–10: Buyer decides: convert · scroll specs · seek alt
```

Alternatives (question 5) intentionally **outside hero** — USR-PDP-12 on first scroll (mobile P3) or deep scroll (desktop).

---

## Section F — Series Context Block

**Block:** USR-PDP-02  
**Role:** Explicit series gate — replaces breadcrumb-only series inference (WH-13).

### Information contract — what appears

| Field | Status | Source | Example |
|-------|--------|--------|---------|
| **Series name** | Mandatory | Taxonomy / series record | ПРЕМИУМ-3 |
| **Link to series listing** | Mandatory | Series page URL | «Все модели серии ПРЕМИУМ-3 →» |
| **One-line tier descriptor** | Optional (recommended) | Series content slot | «Цельнотянутые ванны премиум-класса» |
| **Construction type hint** | Optional | Series metadata | «Цельнотянутая конструкция» |

### Information contract — what does NOT appear

| Excluded | Why |
|----------|-----|
| Full series comparison prose (3–5 sentences) | Belongs on series page USR-SP-02 — not PDP hero |
| Nomenclature decoding legend | Out of v1 scope (D-02) |
| Sibling series chips (18-chip row) | Parent/series page navigation — not PDP |
| Cross-family series links | Zone 5 / USR-PDP-17 only — labeled |
| SKU matrix or variant picker | V-09 excluded |
| Marketing advantages | Commercial wallpaper — suppressed |

### How buyer confirms «I am inside the correct series»

```text
BUYER ARRIVES
  │
  ├─ from series page     → USR-PDP-02 confirms same series name as USR-SP-01 H1
  ├─ from parent grid     → USR-PDP-02 makes series label on card (USR-LC-07) explicit
  ├─ from search/article  → USR-PDP-02 + USR-PDP-01 article verify together
  └─ from breadcrumb only → USR-PDP-02 removes need to decode breadcrumb terminal
        │
        ▼
CHECK: «Это ПРЕМИУМ-3?»
  ├─ YES → continue to Zone C fit check
  └─ NO  → click series link → exit to USR-SP-06 grid OR adjacent series (USR-SP-04)
```

**Without taxonomy decoding:** Buyer sees **human-readable series name** + optional tier descriptor — not exploded article code (ВМЦ-П3 = ПРЕМИУМ-3 is inferred from series label, not legend table).

### Empty-state behaviour

| Condition | Wireframe behaviour |
|-----------|---------------------|
| Series name missing in CMS | **Block still renders** with breadcrumb-derived series name; flag content gap — do not hide block |
| Series page URL missing | Show series name **without link**; add content ops ticket |
| Tier descriptor empty | Omit descriptor line — series name + link sufficient |
| Wrong series assignment (data error) | Out of wireframe scope — content/ERP fix |

---

## Section G — Commercial Core

**Primary block:** USR-PDP-03 (hero)  
**Extended block:** USR-PDP-18 (Zone 6)  
**Supporting:** USR-PDP-19, USR-PDP-20, USR-PDP-21

### Hierarchy map (information only — no styling)

```text
COMMERCIAL HIERARCHY — descending decision weight

TIER 1 — HERO (USR-PDP-03)                    ◄◄◄ highest attention
├── Availability status (single zone)
│   └── «В наличии» + qty  OR  «Под заказ» + lead time inline
├── Price (single instance — CP-02)
├── Quantity selector
└── Primary CTA [ В корзину ]

TIER 2 — SECONDARY ACTIONS (USR-PDP-07)       ◄── same hero, lower weight
├── [ Сравнить ] (labeled)
└── [ В избранное ] (labeled)

TIER 3 — CONSULTATION (USR-PDP-19)            ◄── first scroll, elevated
├── [ Задать вопрос ]
└── [ Поможем подобрать ]

TIER 4 — B2B DETAIL (USR-PDP-18)              ◄── link-dominant, not form
├── Delivery summary + link → «Доставка»
├── Dealer path link → «Дилерам» / «Купить как дилер»
└── Lead time detail (if not in hero)

TIER 5 — TRUST + LEGAL (USR-PDP-20, 21)       ◄── lowest, non-blocking
├── «Сделано в России» micro-signal
└── Price disclaimer / оферта
```

### Field ownership rules

| Field | Primary surface | Secondary | Must NOT duplicate |
|-------|-----------------|-----------|-------------------|
| Price | USR-PDP-03 | USR-PDP-18 (reference only) | 3+ times on same view |
| Availability | USR-PDP-03 (single zone) | — | Second status zone in hero |
| Lead time | USR-PDP-03 when под заказ | USR-PDP-18 detail | Hidden when под заказ |
| Delivery | USR-PDP-18 summary + link | — | Empty placeholder span |
| Dealer form | Dedicated «Дилерам» page | USR-PDP-18 link | Full inline form on PDP |
| Consultation | USR-PDP-19 | Header nav | Footer-only placement |

### Compare and Favorite placement

Compare and Favorite live in **USR-PDP-07** (Zone C), not inside USR-PDP-03 — commercial core stays focused on conversion. Compare feedback renders in **USR-PDP-13** after action.

---

## Section H — Specification Strategy

### Three-layer spec model

```text
LAYER 1 — HERO SUBSET (Zone C)
  USR-PDP-04 + USR-PDP-05
  Decision props only: dims + category-critical
        │
        ▼
LAYER 2 — MINIMUM SPEC SUMMARY (Zone 2)
  USR-PDP-09
  5–8 rows: critical attrs + logistics — DEFAULT VISIBLE
        │
        ▼
LAYER 3 — FULL RECORD (Zone 2, collapsed)
  USR-PDP-10
  20+ rows — expand/tab — complete engineering record
        │
        ▼
LAYER 4 — DOCUMENTS (Zone 2 + Zone 4)
  USR-PDP-11 entry · USR-PDP-15 full package
```

### What belongs where

| Information | Layer | Block | Why |
|-------------|-------|-------|-----|
| L×W×H×mass | 1 Hero | USR-PDP-04 | Physical fit — 5-second check |
| Section count, bowl, material, construction | 1 Hero | USR-PDP-05 | Category fit beyond dims (WH-14) |
| Назначение, комплектация | 2 Primary | USR-PDP-08 | Functional fit — prose context |
| Вес нетто/брутто, упаковка | 2 Primary | USR-PDP-09 | Logistics — procurement needs |
| Category-critical attrs (repeat) | 2 Primary | USR-PDP-09 | Allowed **only** if paired with logistics rows — ID-01 |
| All remaining attributes (20+) | 3 Full | USR-PDP-10 | Engineering/tender — not first-screen payload |
| PDFs, certificates, drawings | 4 Docs | USR-PDP-11/15 | Tender path — discoverable from primary zone |

### What should never be duplicated

| Duplication pattern | Rule |
|---------------------|------|
| Same 4 dim rows in hero AND spec table header | **Forbidden** without differentiation — hero = snapshot, table = record |
| Section count in hero, min spec, AND full spec as identical rows | Hero + min spec may overlap **one row max** per attr; full spec owns complete set |
| Description in hero mini-field AND full description | Hero **suppresses** placeholder mini-desc; USR-PDP-08 owns description |
| Full spec table on listing card | **Forbidden** — CP-04 |
| Specs in inactive tab as only access path | **Forbidden** — W1A-F-05 regression |

### ID-01 governance (wireframe rule)

```text
USR-PDP-04/05 (hero)  →  decision subset — max 8 attribute rows
USR-PDP-09 (min spec) →  decision subset + logistics — 5–8 rows
                          MAY repeat 1–2 hero attrs IF accompanied by
                          net/gross weight, packaging — incremental value
USR-PDP-10 (full)     →  complete record — all rows, no omission
```

### Documents strategy

| Block | When | Behaviour |
|-------|------|-----------|
| USR-PDP-11 | Files exist | Inline document list in Zone 2 — visible without tab switch |
| USR-PDP-11 | No files | Empty state: «Документы для этого SKU уточняются» + USR-PDP-19 consult link |
| USR-PDP-15 | Files exist | Deep documentation in Zone 4 — duplicate access path OK (entry vs archive) |
| USR-PDP-15 | No files | Suppress Zone 4 docs block; USR-PDP-11 empty state sufficient |

---

## Section I — Alternatives Strategy

**Replaces:** current «Похожие товары» (W1A-F-06, priority #1 finding).  
**Primary block:** USR-PDP-12 In-Series Alternatives.

### In-Series Alternatives — definition

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Within-series SKU comparison — sizes, sections, Н variants |
| **Scope** | SKUs where `series_id` = current PDP series |
| **Position** | Zone 3 — after primary spec content; **before** USR-PDP-17 |
| **Label** | «Другие модели серии [ПРЕМИУМ-3]» — NOT «Похожие товары» |

### Selection rules (priority order)

```text
RULE 1 — SAME SERIES FIRST (mandatory)
  Include: all sibling SKUs in current series
  Sort: by relevance — dimension proximity → section count → price
  Max visible: 6 cards desktop · 3–4 mobile (scroll for more)
  Exclude: current SKU (self)

RULE 2 — SAME FAMILY SECOND (only via USR-PDP-14 / USR-PDP-17)
  NOT in USR-PDP-12 block
  Buyer exits via Return-to-Series → parent grid → different series

RULE 3 — CROSS-FAMILY (explicit rule only)
  Block: USR-PDP-17 Cross-Family Related
  Label: «Сопутствующее оборудование»
  Trigger: valid accessory/compatibility relation in CMS
  Never: default-prominent cross-family carousel
```

### Card content minimum (in-series alt card)

| Field | Mandatory |
|-------|-----------|
| Article code | ✓ |
| Short name | ✓ |
| L×W×H | ✓ |
| Section count | ✓ |
| Price | ✓ |
| Availability status | ✓ |
| Link to sibling PDP | ✓ |
| Series label | ✗ (redundant — block is series-scoped) |

### Empty-state behaviour

| Condition | Wireframe behaviour |
|-----------|---------------------|
| No sibling SKUs in series (single-SKU series) | **Suppress USR-PDP-12 block entirely** — do not render empty carousel |
| CMS relation returns cross-family items | **Filter out** — never display in USR-PDP-12; route to USR-PDP-17 if valid |
| CMS relation empty / broken (OQ-02) | Show USR-PDP-14 Return-to-Series only: «Смотреть все модели серии →» |
| Only 1 sibling | Show single card — no carousel padding |

### Cross-family legacy handling

| Legacy pattern | Wireframe decision |
|----------------|-------------------|
| «Похожие товары» = котломойки on sink PDP | **Removed** from default path |
| Merchandising pushback to retain | Reclassify as USR-PDP-17 with label «Сопутствующее» — Zone 5 only |
| Invalid relationships | Suppress block — do not render misaligned suggestions |

### Alternatives decision flow

```text
Buyer on PDP
  │
  ├─ Current SKU fits? → USR-PDP-03 convert
  │
  └─ Need different size/sections in SAME series?
        → USR-PDP-12 pick sibling → new PDP
        OR
        → USR-PDP-14 return to series grid with filters
        OR
        → USR-PDP-07 add siblings to compare

  Cross-series need?
        → USR-PDP-02 link to series page
        OR USR-PDP-14 return to parent/series listing
        → NEVER via USR-PDP-12
```

---

## Section J — Validation

### Against Concept Alpha

| Concept Alpha element | Wireframe expression | Status |
|----------------------|---------------------|--------|
| «Серийная верификация» philosophy | USR-PDP-02 + decision ladder in hero | **SATISFIED** |
| First screen must-haves (8 blocks) | All present in Section B fold | **SATISFIED** |
| Suppression list | Marked on schematic | **SATISFIED** |
| Tier 1–4 hierarchy | Fold analysis + spec strategy | **SATISFIED** |
| No sibling matrix (V-09) | Absent from wireframe | **SATISFIED** |
| Mobile commercial-first (P-09) | Section D P1 order | **SATISFIED** |

### Against Architecture

| Principle | Wireframe check | Status |
|-----------|----------------|--------|
| P-01 Product-database first | Single-SKU evaluation; browse upstream | **SATISFIED** |
| P-04 Information at decision point | 5–10 sec gate mapped | **SATISFIED** |
| P-05 Visible packaging ≠ more data | Inline min spec; no new fields | **SATISFIED** |
| P-06 No wasteful duplication | ID-01 rules in Section H | **SATISFIED** |
| P-07 Commercial contextual | Section G hierarchy | **SATISFIED** |
| CP-10 In-series before cross-family | Zone 3 before Zone 5 | **SATISFIED** |

### Against Blueprint

| Blueprint zone | USR blocks mapped | Status |
|----------------|-------------------|--------|
| Zone 0 | USR-PDP-00 | **SATISFIED** |
| Zone 1 Hero | USR-PDP-01–07, 06, 03 | **SATISFIED** |
| Zone 2 Primary | USR-PDP-08–11, 19 | **SATISFIED** |
| Zone 3 Secondary | USR-PDP-12–14 | **SATISFIED** |
| Zone 4 Reference | USR-PDP-15–16 | **SATISFIED** |
| Zone 5 Related | USR-PDP-17 | **SATISFIED** |
| Zone 6 Commercial | USR-PDP-18–21 | **SATISFIED** |

### Against UX Structure

| UX rule | Wireframe check | Status |
|---------|----------------|--------|
| UX-10 No in-page matrix | No matrix in schematic | **SATISFIED** |
| UX-13 Single availability zone | USR-PDP-03 only in hero | **SATISFIED** |
| UX-15 In-series alternatives primary | USR-PDP-12 before USR-PDP-17 | **SATISFIED** |
| UX-17 Consultative CTA elevated | USR-PDP-19 in first scroll | **SATISFIED** |
| UX-22 Labeled compare mobile | USR-PDP-07 labeled in mobile schematic | **SATISFIED** |

### 5–10 second primary question validation

| # | Question | Wireframe support | Pass |
|---|----------|-------------------|------|
| 1 | What series is this? | USR-PDP-02 first screen | **PASS** |
| 2 | What model is this? | USR-PDP-01 + USR-PDP-04 | **PASS** |
| 3 | Is it suitable? | USR-PDP-05 + USR-PDP-09 (first scroll) | **PASS** (partial on strict first viewport) |
| 4 | Is it available? | USR-PDP-03 | **PASS** |
| 5 | What alternatives exist? | USR-PDP-12 (first scroll mobile / deep desktop) | **PASS** (deferred by design) |

---

### Potential overload risks

| Risk | Description | Mitigation in wireframe |
|------|-------------|------------------------|
| Hero payload increase | Series + 8 props + commercial vs current 4 props | Zone C as single row; ID-01 dedup with min spec |
| CTA competition | Cart vs consult vs dealer | Section G 4-tier hierarchy — one primary CTA |
| Min spec + hero overlap | Same attrs repeated 3× | ID-01: logistics rows justify min spec repeat |
| Mobile P1 length | Commercial + series + props before scroll end | Accept per P-09; validate on device (OQ-09) |

### Mobile risks

| Risk | Description | Owner |
|------|-------------|-------|
| P1 stack too long | 4 blocks before scroll on small viewport | Design phase + OQ-09 device test |
| Media at P4 | Buyer may miss visual confirm | Accept — decision-equivalent tradeoff per G6 |
| In-series alts at P3 | Elevated vs desktop — may push specs down | Intentional per UX Structure G6 |

### Implementation risks

| Risk | Source | Wireframe notes |
|------|--------|-----------------|
| Tab vs inline packaging | Concept readiness #4 | **Resolved:** inline min spec + collapsed full spec |
| CMS relation for USR-PDP-12 | OQ-02 | May need relation type change from «Похожие» |
| Compare feedback UX | U-02 | USR-PDP-13 block reserved; behaviour IMPL-DEPENDENT |
| Block registry / PRJ-0009 | OQ-08 | 22 blocks — engineering maps USR-PDP-* to templates |
| Empty CMS fields | Concept risk | Empty states defined in Sections F, H, I |
| Gallery resize | WH-16 | Zone A assigned; height = design phase |

---

## Open Questions

Carried from approved artifacts — wireframe does not assume answers.

| ID | Question | Wireframe impact | Status |
|----|----------|------------------|--------|
| OQ-01 | Category-critical props for non-sink families? | USR-PDP-05 uses моечные ванны only | **OPEN** |
| OQ-02 | Backend rule for «Похожие товары»? | USR-PDP-12 needs series-scoped relation | **OPEN** |
| OQ-03 | `p-card__delivery` empty by design? | USR-PDP-18 delivery summary conditional | **OPEN** |
| OQ-04 | Populated compare table attributes? | USR-PDP-13 feedback only — compare page out of scope | **OPEN** |
| OQ-09 | Mobile P1 fit on common devices? | Section D order — needs device validation | **OPEN** |
| OQ-12 | Series descriptor copy ownership? | USR-PDP-02 optional tier line — content ops | **OPEN** |
| **WQ-01** | Desktop fold: is USR-PDP-08 above or below fold? | Wireframe places at fold boundary — design confirms | **NEW** |
| **WQ-02** | USR-PDP-12 card count: 4 vs 6 vs scroll? | Wireframe assumes 6 desktop / 3–4 mobile | **NEW** |
| **WQ-03** | USR-PDP-18 in P1 mobile or P5 only? | Wireframe: lead time in P1 hero; delivery detail P5 | **NEW** |

---

## Traceability

| Wireframe section | Primary source |
|-------------------|----------------|
| Wireframe Philosophy | Concept Alpha §Concept Philosophy, §Current vs Alpha |
| Desktop Wireframe | Visual Prototype PDP; UX Structure §F |
| Desktop Fold Analysis | Concept Alpha §First Screen; Visual Prototype attention map |
| Mobile Wireframe | UX Structure §G6; Blueprint §G6 |
| Hero Composition | Concept Alpha §First Screen grouping; Blueprint E-01–07 |
| Series Context Block | Concept Alpha USR-PDP-02; Architecture §E hero |
| Commercial Core | Blueprint Zone 6; Concept Alpha §Decision Flow |
| Specification Strategy | Concept Alpha Tier 2; Blueprint E-09/10; ID-01 |
| Alternatives Strategy | Concept Alpha §Decision Flow; Blueprint E-12; W1A-F-06 |
| Validation | Concept Alpha §Readiness; UX Structure §I |

---

## Document lineage

| Input | Role |
|-------|------|
| [BZPM-PDP-CONCEPT-ALPHA-v1](BZPM-PDP-CONCEPT-ALPHA-v1.md) | Direct source — approved for wireframe |
| [BZPM-UX-STRUCTURE-v1](BZPM-UX-STRUCTURE-v1.md) | Block sequence USR-PDP-00–21 |
| [BZPM-BLUEPRINT-v1](BZPM-BLUEPRINT-v1.md) | Zone contracts E-00–21 |
| [BZPM-VISUAL-UX-PROTOTYPE-v1](BZPM-VISUAL-UX-PROTOTYPE-v1.md) | ASCII schematic baseline |
| [BZPM-REDESIGN-ARCHITECTURE-v1](BZPM-REDESIGN-ARCHITECTURE-v1.md) | Principles P-01–P-10, ownership matrix |

**Next phase:** High-fidelity wireframes and visual design (designer handoff). Engineering block registry mapping (OCPilot / PRJ-0009).

---

*BZPM-PDP-WIREFRAME-ALPHA-v1 — low-fidelity wireframe only. No design. No UI kit. No branding. No CSS. No Twig. No JS. No implementation.*
