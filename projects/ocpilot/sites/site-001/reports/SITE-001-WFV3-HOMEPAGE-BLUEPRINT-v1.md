# REPORT — SITE-001 WF-V3 Homepage Blueprint v1

**Type:** Homepage information architecture blueprint — documentation only  
**Date:** 2026-06-11  
**Site:** SITE-001 — Автосалон СИБКАР  
**Program:** Website Factory · WF-V3  
**Mode:** Planning / blueprint — **no design, no CSS, no implementation**

**Explicit exclusions (honored):** No HTML · No SCSS · No JS · No OpenCart · No OCPilot · No TEST · No FTP · No visual styling · No prototype code · No commit implied

**Authority chain:**

- [SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md](../governance/SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md) — **primary**
- [SITE-001-WFV3-HOMEPAGE-PROTOTYPE-CHARTER-v1.md](../governance/SITE-001-WFV3-HOMEPAGE-PROTOTYPE-CHARTER-v1.md)
- [SITE-001-WFV3-HOMEPAGE-DISCOVERY-v1.md](SITE-001-WFV3-HOMEPAGE-DISCOVERY-v1.md)

**Principle:** Homepage and PDP = **two screens of the same product**. Shared header, footer, tokens, trust tone, CTA discipline.

---

# SECTION 4 — Information Architecture

## Proposed Homepage anatomy (top → bottom)

Каждый блок — **зона планирования**, не визуальный макет.

### H0 — Header stack

**Содержание:** Dark topbar (город, часы, телефон) + white main bar (logo, centered nav, red pill «Перезвоните мне»).

**Rationale:** P-03 one dealer shell. Идентичная грамматика PDP Z0. Посетитель узнаёт тот же chrome на `/` и на PDP. Static — no sticky (P-11). Phone в topbar = support contact без конкуренции red CTA.

**PDP equivalent:** Z0 — **shared partial**, no divergence.

---

### H1 — USP benefit row

**Содержание:** Light full-width band; ~5 icon+text items (напр. «Реальные авто на складе», «160-point check», «Кредит от 6,9%», trade-in hook, рассрочка).

**Rationale:** Тот же слой, что PDP Z1 — supporting trust + financing hook **без** marquee panic (P-04, P-10). На Homepage не доминирует над hero: тонкая полоса под nav, не третий promo ticker. Контент Phase 1 + concept analysis; не generic «10 лет на рынке».

**PDP equivalent:** Z1 — **same row grammar**, same copy family.

---

### H2 — Hero (inventory-first)

**Содержание:**

- Stable headline — inventory proposition (не rotating offer text)  
- Subline — locality / assortment hint (пробег + новые — secondary mention)  
- Vehicle photography in frame — real car(s), studio or lot quality  
- **One** primary red CTA in hero zone (см. §9)  
- Room for search overlap (§5)

**Rationale:** P-01 car first, P-02 inventory is hero. Заменяет carousel-first TEST hero — главный composition break. Headline отвечает «что я могу купить здесь?», не «какая акция сегодня?». Машина в кадре доказывает showroom, не marketing agency.

**Anti-pattern:** Full-width promo slider · abstract stock photo без авто · CAPS discount as H1.

**PDP equivalent:** Нет прямого аналога — Homepage hero = **entry stage**; PDP Z4 hero = **single-vehicle stage**. Shared: car photography dominance, flat canvas, typography scale.

---

### H3 — Search entry

**Содержание:** Filter/search module — марка, модель (или тип), ценовой диапазон, год; primary action «Найти» / «Показать авто».

**Rationale:** P-05 search first-class. Primary P0 job. Должен быть **на first screen** — overlapping hero bottom или immediately adjacent. Визуальный вес сопоставим с headline, не footer widget.

**PDP equivalent:** Нет на PDP (orientation via breadcrumbs Z2). Search = **homepage-only entry**; результат ведёт в catalog `/cars/`.

---

### H4 — Featured inventory

**Содержание:** Section heading («Авто с пробегом в наличии» или operator-approved Phase 1 label) + grid/row vehicle cards + text link «Смотреть все» → `/cars/`.

**Rationale:** P-02 — доказательство склада до ухода в каталог. Карточки = будущая catalog grammar (flat, photo dominant, price visible). Закрывает anxiety «красивый сайт без машин».

**PDP equivalent:** Z9 related links (inventory continuation) — Homepage featured = **multi-vehicle Z9 at entry scale**.

---

### H5 — Trust layer

**Содержание:** Horizontal proof strip — dealer-level verification (не vehicle-specific). ~4–5 items: inspection program, VIN/report policy, no hidden fees, physical address, years in market (только если Phase 1 verified).

**Rationale:** P-10 trust before promotion. Тот же **proof tone**, что PDP Z5 — icons + short labels на `surface-secondary`, не CAPS marquee. На Homepage — **dealer credibility**; на PDP Z5 — **vehicle credibility**. Одна trust grammar, разный scope.

**PDP equivalent:** Z5 trust row — **same visual grammar**, different proof objects.

---

### H6 — Dealer advantages (expanded)

**Содержание:** 3–4 advantage blocks — credit path, trade-in, inspection, «реальные авто на складе». Icon + title + one-line explanation. Flat surfaces, no card-in-card.

**Rationale:** Заменяет legacy `four_blocks` — тот же business content, **новая** Class B geometry. Supporting layer (P-2 priority) — **below** search and featured inventory. Не конкурирует с first screen. Конкретика из discovery: trade-in, кредит от X%, 160-point check, локальный адрес — не «лучший сервис в городе».

**PDP equivalent:** Z1 (compact) + частично Z6 equipment mindset (structured facts) — Homepage expands USP **below fold**.

---

### H7 — Financing entry band

**Содержание:** Lightweight credit / installment invitation — heading, rate hook, outlined secondary CTA «Условия кредита» + optional monthly example. **No** full calculator on homepage.

**Rationale:** P4 job (кредит) без дублирования PDP Z7. Secondary conversion — visitor ещё не выбрал машину. Full calculator остаётся на PDP после equipment (frozen). Red solid CTA **не** здесь если hero/header уже consumed primary red.

**PDP equivalent:** Z7 credit calculator — Homepage = **teaser**; PDP = **full module**.

---

### H8 — Partner banks strip

**Содержание:** «Партнёрские банки» + logo row (~6–8 partners).

**Rationale:** Credibility reinforcement — same as PDP Z8. На Homepage короче, без дублирования credit form. Reinforces financing path without merging into hero.

**PDP equivalent:** Z8 banks — **same grid grammar**, may use same partial with homepage spacing variant.

---

### H9 — Contact / callback band

**Содержание:** Address repeat, hours, phone, WhatsApp (if Phase 1 approved), outlined or secondary callback trigger. Optional map link.

**Rationale:** P5 contact — visitors ready to visit after inventory scan. Support CTA tier. Не primary red если зона уже исчерпала P-09 budget выше — использовать outlined callback или rely on footer.

**PDP equivalent:** Footer contact repeat (Z10) — Homepage band = **mid-page contact anchor** before footer.

---

### H10 — Footer

**Содержание:** Dark inverse — contact, catalog columns (новые / пробег), legal, red callback repeat.

**Rationale:** Brand continuity terminus. Frozen PDP Z10 — **shared partial**.

**PDP equivalent:** Z10 — **identical shell**.

---

## Section order summary

```text
H0  Header stack
H1  USP benefit row
H2  Hero (inventory-first)
H3  Search entry          ← first-screen cluster with H2
H4  Featured inventory
H5  Trust layer
H6  Dealer advantages
H7  Financing entry band
H8  Partner banks
H9  Contact band
H10 Footer
```

**Note:** H2+H3 form **first-screen cluster** — exact overlap geometry deferred to prototype v0.1, not blueprint amendment.

---

# SECTION 5 — Search-First Strategy

## Placement

| Rule | Definition |
|------|------------|
| **Viewport** | Visible without scroll on desktop ≥ 1280px |
| **Position** | Within hero cluster (H2) — bottom overlap or immediately below headline |
| **Relationship to hero** | Search + headline + car photo = **one composed first screen**, not search buried below carousel |

## Role

| Aspect | Definition |
|--------|------------|
| **Primary function** | Route to used inventory catalog `/cars/` with pre-selected filters |
| **User mental model** | «Я здесь, чтобы найти машину» — same as Class B 3-second sentence |
| **Not** | Decorative widget · nav-only «Авто с пробегом» link · site-wide Google box |

## Scope

| Field | Priority | Notes |
|-------|----------|-------|
| **Марка / модель** | P0 | Primary filter path |
| **Цена от–до** | P0 | Mass-market pragmatic filter |
| **Год** | P1 | Common used-car criterion |
| **Пробег** | P2 | Optional in v0.1 static shell |
| **КПП / топливо** | P3 | Defer to catalog filters |
| **New cars `/auto/`** | Secondary | Tab or link — not default search scope |

Default scope = **авто с пробегом** (primary persona). Prototype may use static fields — no backend (charter exclusion).

## Prominence

| Dimension | Requirement |
|-----------|-------------|
| **Visual weight** | Comparable to hero headline — largest interactive element on first screen |
| **Surface** | One elevation level allowed (P-08) — floating search card on canvas OK |
| **CTA inside search** | Submit = candidate for hero zone primary red **or** outlined if header callback owns red |
| **Competition** | Must not lose to carousel, promo text, or four-icon strip |

---

# SECTION 6 — Featured Inventory Strategy

## What to show

| Criterion | Rule |
|-----------|------|
| **Category** | Used cars only in v0.1 — primary persona |
| **Selection mix** | 2× popular brand + 1× value tier + 1× fresh arrival (business diversity) |
| **Card content** | Photo (dominant) · title (brand/model/year) · price · key spec chip (mileage or year) · link to PDP |
| **Photography** | Studio/lot quality — same asset realism standard as PDP gallery |

## How many

| Viewport | Count | Rationale |
|----------|-------|-----------|
| **Desktop first row** | **4 vehicles** | Fills ~1200–1400px container at catalog card width; proves assortment without catalog noise |
| **Optional second row** | +2 (6 total max) | Only if section remains below fold anchor — avoid first-screen crowding vs search |
| **Prototype v0.1** | **4 static cards** | Enough for grammar proof; operator HITL on card sibling feel vs PDP |

## Why

| Reason | Evidence |
|--------|----------|
| Inventory presence | Discovery §1.2 «реальный склад» |
| Bridge to catalog | Visitor sees price + photo before `/cars/` commitment |
| PDP grammar preview | Card → PDP Z4 is natural path |
| Anti-empty-showroom | Fails trust if homepage has search but no cars visible |

## Business purpose

Convert **browse intent** → **PDP depth** or **catalog filter**. Featured = curated **window**, not full inventory. «Смотреть все» → `/cars/` for full assortment. Operator may later wire CMS «featured» flag — out of prototype scope.

---

# SECTION 7 — Trust Model

## Alignment principle

Homepage trust **extends** PDP trust grammar — same tone (proof, not panic), same surface (`surface-secondary`), same flat tiles — **different proof objects**.

## Trust hierarchy (Homepage)

| Tier | Content | Placement |
|------|---------|-----------|
| **T1 — Immediate** | Locality (Новосибирск), phone in topbar | H0 |
| **T2 — First screen** | «Реальные авто на складе» in headline/subline + car photo | H2 |
| **T3 — Structured proof** | Dealer verification strip (inspection, VIN policy, no accidents policy at dealer level) | H5 |
| **T4 — USP facts** | 160-point check, credit rate, trade-in | H1, H6 |
| **T5 — Institutional** | Partner banks | H8 |
| **T6 — Contact proof** | Physical address, hours | H9, H10 |

## Proof hierarchy

| Level | Homepage | PDP |
|-------|----------|-----|
| **Dealer** | Address, years, inspection program, bank partners | Header locality, banks Z8 |
| **Inventory** | Featured cards with prices | Gallery + title Z3, Z4 |
| **Vehicle** | — | Trust row Z5 (report, condition, accidents, mileage) |
| **Transaction** | Credit teaser H7 | Full calculator Z7, offer CTAs Z4 |

## Belongs on Homepage

- Dealer-level verification strip (H5)  
- Locality + contact in header/footer  
- «Реальные авто» + featured inventory as inventory proof  
- Bank logos (financing credibility)  
- USP row (H1) — compact  

## Belongs only on PDP (not duplicated as primary on Homepage)

- Vehicle-specific trust items (VIN report for **this** car, mileage confirmed for **this** VIN)  
- Full spec grid  
- Equipment list Z6  
- Full credit calculator with term slider  
- Offer column price/discount lines for **one** vehicle  
- Status badges («12 человек смотрят», «В наличии» for specific SKU)

---

# SECTION 8 — Dealer Advantages

## What matters most (discovery-driven, not generic)

| Rank | Advantage | Why (evidence) |
|------|-----------|----------------|
| **1** | **Реальный склад / авто в наличии** | Primary job P-02; anti-marketplace anxiety |
| **2** | **Проверка / 160-point inspection** | Trust model §1.3; aligns PDP Z5 grammar |
| **3** | **Кредит / рассрочка от X%** | Secondary persona; PDP Z1/Z7 hook — Phase 1 verified rate only |
| **4** | **Trade-in** | Tertiary persona; PDP secondary CTA |
| **5** | **Локальный салон Новосибирск** | Geography trust — not «№1 в России» |
| **6** | **Партнёрские банки** | Z8 credibility — supporting, not hero |

## Avoid (generic dealership marketing)

| Ban | Reason |
|-----|--------|
| «Лучший автосалон города» | Unverified superlative |
| «10 лет безупречной работы» | Unless Phase 1 source doc |
| CAPS marquee discounts | P-04, legacy anti-pattern |
| Stock icons without business fact | Decoration without proof |
| Competing red promo buttons | P-09 |

## Content source

Phase 1 frozen copy · PDP benefit row labels · W3C services inventory · operator-verified claims only (P-19).

---

# SECTION 9 — CTA Model

## Tier definitions (aligned with PDP freeze)

| Tier | Treatment | Homepage usage |
|------|-----------|------------------|
| **Primary** | Solid red fill, white text, pill | **One per viewport zone** (P-09) |
| **Secondary** | White fill, red border, red text | Trade-in, credit conditions, catalog browse |
| **Support** | Text links, phone in topbar | «Смотреть все», nav links, footer links |

## Homepage CTA assignment by zone

| Zone | Primary red | Secondary | Support |
|------|-------------|-----------|---------|
| **H0 Header** | «Перезвоните мне» (frozen PDP) | — | Phone in topbar (not red fill) |
| **H2 Hero** | «Смотреть авто с пробегом» **OR** search submit «Найти» — **pick one** per prototype; not both solid red | Outlined «Trade-in» / «Кредит» if space | — |
| **H3 Search** | Submit button — **only if** hero did not take primary red | — | — |
| **H4 Featured** | — | — | Card links → PDP; «Смотреть все» text |
| **H7 Financing** | — | Outlined «Условия кредита» | Link to `/autocredit` |
| **H9 Contact** | — | Outlined callback | Phone, WhatsApp |
| **H10 Footer** | Red callback repeat (PDP frozen) | — | Legal text links |

## Red button rules (frozen alignment)

1. **Maximum one solid red filled action per viewport zone** (P-09).  
2. Red reserved for **price accent on cards** + **one primary action** — not scattered icons (P-14).  
3. Header callback red pill = **persistent primary** in header zone — hero must not add second red in same above-fold band unless header scrolls away (static header: treat header + hero as **one above-fold band** → **either** header callback **or** hero primary red visible as dominant — prototype decision: **header keeps red pill; hero primary = outlined «Смотреть авто» OR search submit red with callback demoted to outlined** — operator HITL at v0.1).  
4. Phone / WhatsApp = **never** solid red fill in competition with callback.  
5. Same CTA label family as PDP where applicable: «Купить в кредит» on PDP; homepage uses discovery-stage CTAs («Найти», «Смотреть авто с пробегом») — not «Купить» before vehicle selection.

**Blueprint recommendation:** Above-fold **single red** = search submit «Найти авто»; header callback → **outlined variant on homepage only** OR keep frozen red pill and search submit outlined — **requires operator HITL**; default inherit PDP = **red pill in header**, hero/search secondary outlined to preserve P-09 in combined first screen.

---

# SECTION 10 — Homepage vs PDP Alignment Table

| Homepage zone | Role | PDP zone | Shared language |
|---------------|------|----------|-----------------|
| **H0 Header stack** | Dealer identity, nav, contact | **Z0** | Identical partial — dark topbar, white nav, red callback |
| **H1 USP benefit row** | Compact dealer strengths | **Z1** | Same light band, ~5 items, no marquee |
| **H2 Hero** | Inventory entry, stable headline | **Z4** (partial) | Car-first photography, flat canvas, typography scale — **no** 65/35 offer column |
| **H3 Search** | Catalog entry | — | Homepage-only; catalog `/cars/` is downstream |
| **H4 Featured inventory** | Multi-car peek | **Z9** related | Card grammar → single-car Z4 on click |
| **H5 Trust layer** | Dealer verification | **Z5** | Same strip grammar; dealer vs vehicle proof |
| **H6 Dealer advantages** | Expanded USP | **Z1 + Z6 mindset** | Structured facts, checkmarks/icons, flat |
| **H7 Financing band** | Credit teaser | **Z7** | Teaser vs full calculator — same rate copy |
| **H8 Banks** | Partner logos | **Z8** | Same logo grid partial |
| **H9 Contact band** | Mid-page contact | **Z10** (partial) | Contact repeat before full footer |
| **H10 Footer** | Site map, legal | **Z10** | Identical partial |

### Shared design language checklist

| Element | Shared rule |
|---------|-------------|
| Class prefix | `wf-v3-*` |
| Typography | Inter stack, PDP v0.2 roles |
| Surfaces | Max 2 depths per zone; no card-in-card |
| Brand red | Price + one primary action per zone |
| Header/footer | Shared partials from PDP workspace |
| Trust tone | Proof labels, not CAPS promo |
| Photography | Vehicle-dominant, studio flat stage |

---

# SECTION 11 — Blueprint ASCII Wireframe

Desktop ≥ 1280px. Hierarchy only — no pixels, no color.

```text
+------------------------------------------------------------------+
| TOPBAR:  [city] [hours]                    [phone]             |
+------------------------------------------------------------------+
| NAV:     [LOGO]    Nav Nav Nav Nav Nav Nav          [Callback]   |
+------------------------------------------------------------------+
| USP:     (icon) Real stock  (icon) 160-check  (icon) Credit ...  |
+------------------------------------------------------------------+
|                                                                  |
|  HERO                                              [ car photo ] |
|  +---------------------------+                     [  or   ]   |
|  | HEADLINE: Inventory prop  |                     [ small  ]   |
|  | subline: locality hint    |                     [ fleet  ]   |
|  +---------------------------+                                   |
|  | SEARCH CARD               |                                   |
|  | [brand][model][price][go] |                                   |
|  +---------------------------+                                   |
|                                                                  |
+------------------------------------------------------------------+
| FEATURED:  "Avto s probegom v nalichii"          [smotret vse >] |
|  +--------+  +--------+  +--------+  +--------+                  |
|  | [photo]|  | [photo]|  | [photo]|  | [photo]|                  |
|  | title  |  | title  |  | title  |  | title  |                  |
|  | price  |  | price  |  | price  |  | price  |                  |
|  +--------+  +--------+  +--------+  +--------+                  |
+------------------------------------------------------------------+
| TRUST:   [proof1] [proof2] [proof3] [proof4] [proof5]            |
+------------------------------------------------------------------+
| ADVANTAGES:                                                      |
|  +-------------+  +-------------+  +-------------+               |
|  | icon        |  | icon        |  | icon        |               |
|  | credit      |  | trade-in    |  | inspection  |               |
|  +-------------+  +-------------+  +-------------+               |
+------------------------------------------------------------------+
| CREDIT TEASER:  headline + rate hook          [Usloviya kredita]   |
+------------------------------------------------------------------+
| BANKS:   [logo] [logo] [logo] [logo] [logo] [logo]                |
+------------------------------------------------------------------+
| CONTACT: address · hours · phone · [callback outlined]             |
+------------------------------------------------------------------+
| FOOTER (dark): contact | catalog cols | legal | [callback red]   |
+------------------------------------------------------------------+
```

---

# SECTION 12 — Success Criteria

## Operator-facing acceptance (future HITL)

| # | Criterion | Measurement |
|---|-----------|-------------|
| 1 | **3-second test** | Logo hidden · sentence = «современный автосалон — можно сразу искать машину» |
| 2 | **PDP sibling test** | Side-by-side Homepage + PDP — same brand, tokens, header/footer |
| 3 | **Inventory-first** | Search + car photo + featured cards on first screen path — no carousel |
| 4 | **Brand recognition** | Red accent disciplined; СИБКАР identity without legacy OC silhouette |
| 5 | **P-01..P-10** | Visibly satisfied on static prototype |
| 6 | **Composition delta vs TEST** | Obviously different anatomy — not color-only |
| 7 | **No new design language** | Zero divergence from PDP freeze without review |

## Failure signals

- Carousel-first hero returns  
- Search below fold only  
- four_blocks legacy geometry unchanged  
- Multiple red CTAs in first screen  
- Homepage and PDP headers/footers differ  
- Trust strip reads as promo marquee  

## Authorization

`VISUAL_ACCEPT` — operator HITL only (P0-05). No agent scores.

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| H2/H3 exact overlap geometry | **OPEN** — prototype v0.1 |
| Above-fold single-red resolution (header vs search) | **OPEN** — operator HITL |
| Featured vehicle CMS rules | **OPEN** — integration phase |
| Mobile stack order | **SAFE UNKNOWN** — after desktop ACCEPT |

**SECURITY RISK:** None (documentation only).

---

*SITE-001 WF-V3 Homepage Blueprint v1 — planning only; no design; no implementation; no commit implied.*
