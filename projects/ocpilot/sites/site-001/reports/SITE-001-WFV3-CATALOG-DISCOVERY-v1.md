# REPORT — SITE-001 WF-V3 Catalog Discovery v1

**Type:** Catalog discovery — documentation only  
**Date:** 2026-06-14  
**Site:** SITE-001 — Автосалон СИБКАР  
**Program:** Website Factory · WF-V3  
**Mode:** Discovery / planning — **no implementation**

**Explicit exclusions (honored):** No HTML · No SCSS · No JS · No OpenCart · No OCPilot · No TEST · No FTP · No wireframes · No prototype · No workspace · No commit implied

**Binding authority (inherit — do not reinvent):**

- [SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md](../governance/SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md)
- [SITE-001-WFV3-HOMEPAGE-PROTOTYPE-CHARTER-v1.md](../governance/SITE-001-WFV3-HOMEPAGE-PROTOTYPE-CHARTER-v1.md)
- [SITE-001-WFV3-CLEAN-ROOM-DISCOVERY-v1.md](SITE-001-WFV3-CLEAN-ROOM-DISCOVERY-v1.md)
- [SITE-001-WFV3-HOMEPAGE-DISCOVERY-v1.md](SITE-001-WFV3-HOMEPAGE-DISCOVERY-v1.md)
- [SITE-001-WFV3-HOMEPAGE-BLUEPRINT-v1.md](SITE-001-WFV3-HOMEPAGE-BLUEPRINT-v1.md)
- [SITE-001-WFV3-PDP-CONCEPT-ANALYSIS-v1.md](SITE-001-WFV3-PDP-CONCEPT-ANALYSIS-v1.md)
- [SITE-001-WFV3-LAYOUT-CONFORMANCE-PASS-v1.md](SITE-001-WFV3-LAYOUT-CONFORMANCE-PASS-v1.md)

**Prototype evidence (card grammar — reference only, not new authority):**

- `workspaces/site-001-wf-v3-homepage-prototype/src/partials/sections/featured-inventory.html` — `wf-v3-inventory-card`
- `workspaces/site-001-wf-v3-pdp-prototype/` — frozen PDP zones Z0–Z10

**Related blueprint:** [SITE-001-WFV3-CATALOG-BLUEPRINT-v1.md](SITE-001-WFV3-CATALOG-BLUEPRINT-v1.md)

**Brand layer:** Brand Pack v1 accepted — `logo--original.png`, `logo--retina.png`, favicon pack. SVG / logo_white / rebrand **out of scope** for WF-V3.

---

## Executive Summary

Каталог `/cars/` в WF-V3 — **третий опорный экран** Class B **Digital Inventory Showroom**, замыкающий цепочку **Homepage → Catalog → PDP**. Это не отдельный продукт и не «страница фильтров OpenCart», а **много-машинная витрина склада**: посетитель сужает выбор, сравнивает карточки и переходит в PDP.

Discovery подтверждает: **Class B остаётся в силе** для каталога. Новый визуальный язык **запрещён**. Карточка каталога **расширяет** грамматику H4 Featured Inventory, не создаёт новую. PDP и Homepage прототипы (WF-GRID PASS · WF-LAYOUT PASS · Architecture Frozen) дают достаточную authority для catalog discovery.

---

# SECTION 1 — Catalog Purpose Discovery

## 1.1 Главная задача каталога СИБКАР

Каталог — **рабочая зона поиска и сравнения** реального инвентаря дилера, не промо-лендинг и не агрегатор чужих объявлений.

| Job | Описание |
|-----|----------|
| **Primary** | **Найти** автомобиль по критериям (марка · модель · бюджет · год · пробег) и **сузить** выбор до нескольких кандидатов |
| **Secondary** | **Сравнить** варианты в одной сетке — цена · пробег · год · ключевые характеристики без ухода в PDP |
| **Tertiary** | **Перейти** в карточку (PDP) выбранного авто — conversion depth |
| **Quaternary** | **Оценить ассортимент** — «у них достаточно машин в моём бюджете» |

Каталог **не** продаёт одну машину (это PDP). Каталог **не** заменяет Homepage как entry route. Каталог **принимает** трафик с Homepage (H3 search · H4 «Смотреть все») и **отдаёт** в PDP.

## 1.2 Приоритеты задач (ранжирование)

| Rank | Task | Rationale |
|------|------|-----------|
| **P0** | **Найти автомобиль** | Primary persona; clean-room §1.1; homepage P0 job downstream |
| **P1** | **Сравнить варианты** | Grid scan — price · mileage · year visible without click |
| **P2** | **Перейти в карточку (PDP)** | Natural next step after shortlist |
| **P3** | **Оценить ассортимент** | Result count · grid density · «реальный склад» |
| **P4** | **Повторно уточнить фильтры** | Iterative narrowing — secondary to first scan |
| **P5** | **Контакт / callback** | Support — header phone + footer; not per-card red CTAs |

**Anti-priority (не first screen):** reviews carousel · bank slider · promo blocks above results · per-card swiper galleries · CAPS discount marquees.

## 1.3 3-Second Test — каталог

### Метод

- Viewport desktop ≥ 1280px (aligned with PDP freeze)  
- Logo **скрыт**  
- Экспозиция **3 секунды**  
- Оценка: силуэт, цвет, типографика, композиция **first screen only**

### Ожидаемое восприятие (exact)

> **«Это витрина склада — можно сразу искать и сравнивать машины.»**

### Детализация first-screen read

| Signal | Expected perception |
|--------|---------------------|
| **Header silhouette** | Тот же dealer shell, что Homepage H0 / PDP Z0 — узнаваемый chrome |
| **Filter + results cluster** | Фильтры или активные критерии **и** фото машин с ценами видны без «где каталог?» |
| **Card grammar** | Плоские карточки, фото доминирует, цена красным акцентом — sibling к H4 и PDP Z4 |
| **Density** | Inventory showroom — несколько машин в кадре, не одна promo-карточка |
| **Locality** | Новосибирск / телефон в chrome — «реальный салон», не маркетплейс |

### FAIL sentences (anti-patterns)

| Sentence | Trigger |
|----------|---------|
| «Обычный каталог OpenCart с рамками и каруселями» | Bordered OC grid · swiper per card · filter buried below promo |
| «Красивые фильтры, но машин не видно» | Filter panel dominates · zero results visible on first screen |
| «Каталог объявлений без лица дилера» | No dealer shell · no trust · anonymous list |
| «Каждая карточка — мини-лендинг с тремя красными кнопками» | P-09 violation · competing CTAs per card |

### Relationship to sibling screens

| Screen | 3-second sentence |
|--------|-------------------|
| Homepage | «Современный автосалон — можно сразу искать машину» |
| **Catalog** | **«Витрина склада — можно сравнивать и выбирать»** |
| PDP | «Конкретная машина — цена ясна, проверка рядом» |

---

# SECTION 2 — Catalog Class Validation

## 2.1 Кандидат: Class B — Digital Inventory Showroom

| Criterion | Catalog fit |
|-----------|-------------|
| Primary job = find + compare used cars | **YES** — filter + results grid |
| 3-second test vs OC template | **YES** — composition must differ from TEST `catalog_item` + swiper pattern |
| Brand fit for regional mass-market | **YES** — не Class C premium gallery |
| Homepage + PDP alignment | **YES** — same class frozen on both screens |
| Operator mandate «заметно иначе» | **YES** — flat inventory cards vs legacy bordered carousel cards |

## 2.2 Три экрана — один продукт

| Screen | Stage | Class B role |
|--------|-------|--------------|
| **Homepage** | Inventory **entry** | Search + featured peek → route to catalog |
| **Catalog** | Inventory **browse** | Filter + grid + compare → route to PDP |
| **PDP** | **Single-vehicle** stage | Gallery + offer + trust → lead |

Общие элементы: one dealer shell (P-03), search/filters first-class (P-05), flat surfaces (P-07), one red CTA per zone (P-09), price accent (P-14), static header (P-11), shared tokens (`wf-v3-*`).

Class A **отклонён** — сохраняет OC catalog silhouette (bordered cards, filter-in-container OC pattern).  
Class C **отклонён** — editorial gallery density wrong for mass-market compare job.  
Class D **отклонён** — utility-only без dealer face.

## 2.3 Freeze statement

```text
SITE-001 Catalog = Class B — Digital Inventory Showroom
Inherits WF-V3 PDP + Homepage design authority — no new visual class
FROZEN for catalog discovery v1 — 2026-06-14
```

Изменение класса каталога = **authority review** (PDP freeze §3 Change gate).

---

# SECTION 3 — Information Architecture (Overview)

Полная зональная карта — в [SITE-001-WFV3-CATALOG-BLUEPRINT-v1.md](SITE-001-WFV3-CATALOG-BLUEPRINT-v1.md) (C0–C11).

| Zone | Name | Role |
|------|------|------|
| **C0** | Header stack | Shared partial — H0 / Z0 |
| **C1** | USP benefit row | Shared partial — H1 / Z1 |
| **C2** | Breadcrumbs | Orientation — Главная > Авто с пробегом [> Brand] |
| **C3** | Page header | H1 + result count + sort control |
| **C4** | Filter zone | Primary + advanced filters — conceptual only |
| **C5** | Active filters bar | Chips + reset — applied criteria visible |
| **C6** | Results grid | Inventory cards — core catalog moment |
| **C7** | Pagination | Navigate inventory pages |
| **C8** | Trust layer | Catalog-scoped dealer + inventory proof |
| **C9** | Financing teaser | Lightweight credit hook — secondary |
| **C10** | Footer | Shared partial — Z10 |

**Deliberately excluded from catalog v0.1 scope:** reviews slider (TEST legacy below grid), full bank carousel (footer + optional compact strip), homepage hero blocks.

---

# SECTION 4 — Inventory Strategy

## 4.1 Карточка автомобиля — design unit

**Component:** `wf-v3-inventory-card` — **extends** homepage H4 card; **does not** fork new card class.

| Layer | Homepage H4 (peek) | Catalog C6 (full) |
|-------|-------------------|-------------------|
| Photo | Single static image | Single static image (v0.1) — **no** per-card swiper |
| Title | Brand + model + year | Same format — must match PDP title stem |
| Price | Primary figure, red accent | Same + optional old price strikethrough |
| Meta chips | Year · mileage | Year · mileage + 1–2 spec chips max |
| Status | — | Optional «В наличии» badge |
| Credit hook | — | Optional «от X ₽/мес» — muted, not red CTA |
| CTA | Text link «Подробнее» | Same — **not** solid red per card (P-09) |

## 4.2 Обязательные данные — visibility tiers

### Primary (visible at grid scan — no hover required)

| Field | Rule |
|-------|------|
| **Photo** | Dominant — studio/lot flat stage, same asset standard as PDP gallery |
| **Title** | Brand + model + year — e.g. «Audi A1, 2012» |
| **Price** | Main figure — brand red accent (P-14) |
| **Year** | Meta chip |
| **Mileage** | Meta chip |
| **Link target** | Whole card or title + CTA → PDP |

### Secondary (supports compare — still on card face)

| Field | Rule |
|-------|------|
| **Old price** | Strikethrough if discount exists — same family as PDP offer |
| **Monthly from** | «от 12 208 ₽/мес» — small muted text |
| **Status badge** | «В наличии» — one badge max |
| **Spec chips** | Up to 2: e.g. КПП · объём · привод — not full PDP grid |

### Tertiary (PDP only — not on catalog card)

| Field | Rule |
|-------|------|
| Full spec grid (3×4) | PDP Z4 offer column |
| VIN check button | PDP Z4 |
| Vehicle trust strip items | PDP Z5 |
| Equipment list | PDP Z6 |
| Credit calculator form | PDP Z7 |
| Urgency badges («12 человек смотрят») | PDP Z3 — optional on catalog |

## 4.3 Grid density

| Viewport | Columns | Rationale |
|----------|---------|-----------|
| Desktop ≥ 1280px | **3** | Compare 3+ cars with readable photo + price; WF-LAYOUT L3 sibling to H4 N=4 at narrower card width |
| Tablet ≤ 1024px | **2** | Align with homepage featured collapse |
| Mobile ≤ 767px | **1** | Stack — filter collapses above |

**Prototype v0.1:** 6–9 static cards sufficient for grammar proof (pagination static).

## 4.4 CTA discipline on cards

- **One** interaction path per card: navigate to PDP  
- CTA = text link «Подробнее» or whole-card click — **not** «Купить в кредит» (reserved for PDP Z4)  
- **No** solid red button on every card — preserves P-09 for page-level zones only

---

# SECTION 5 — Filters Strategy (Conceptual Only)

**Scope:** taxonomy and UX intent only. **No** OpenCart · **No** JS · **No** implementation.

## 5.1 Filter tiers

### Tier 1 — Primary (always visible / first screen on desktop)

| Filter | Purpose | Homepage H3 parity |
|--------|---------|-------------------|
| **Марка** | Narrow by brand | ✓ same field |
| **Модель** | Dependent on brand | ✓ same field |
| **Цена от–до** | Budget constraint | ✓ same field |
| **Год от–до** | Age constraint | ✓ same field |

### Tier 2 — Secondary (expanded / «Расширенный поиск»)

| Filter | Purpose |
|--------|---------|
| **Пробег до** | Common used-car criterion |
| **КПП** | Manual / auto / robot / variator |
| **Тип кузова** | Sedan · hatch · SUV · etc. |
| **Топливо** | Petrol · diesel · hybrid |
| **Привод** | FWD · AWD · RWD |
| **Объём двигателя** | Range |

### Tier 3 — Tertiary (power-user / v0.2+)

| Filter | Purpose |
|--------|---------|
| **Мощность** | Range |
| **Число владельцев** | Trust compare |
| **Цвет** | Preference |
| **Состояние** | If inventory tagged |

## 5.2 Sort controls

| Sort option | Default |
|-------------|---------|
| **По умолчанию** (новые поступления / relevance) | **YES** — default |
| **Цена ↑ / ↓** | Common |
| **Год ↓ / ↑** | Common |
| **Пробег ↑** | Common |

Sort lives in **C3 page header** — not inside filter panel.

## 5.3 Active filters UX

- Applied criteria → **C5 chips bar** below filter zone  
- Each chip removable; «Сбросить все» clears to full catalog  
- Result count updates in **C3** («Найдено N автомобилей»)

## 5.4 Layout concept (desktop)

| Pattern | Direction |
|---------|-----------|
| **Sidebar filter** (left ~25–30%) + **results grid** (right) | Preferred — keeps filters persistent while scrolling results |
| **Alternative:** horizontal filter bar above grid | Acceptable if sidebar breaks WF-LAYOUT — operator HITL at prototype |

Mobile: filter = collapsible panel / drawer — **deferred** to responsive pass; desktop-first per freeze.

## 5.5 Scope boundary

- Default catalog scope = **авто с пробегом** (`/cars/`)  
- New cars (`/auto/`) = **separate catalog charter** — out of v0.1  
- Homepage H3 search submit → pre-fills Tier 1 filters on catalog landing

---

# SECTION 6 — Homepage → Catalog Alignment

## 6.1 Flow diagram

```text
Homepage H3 Search (brand · model · price · year)
        │
        ▼ submit «Найти автомобиль»
        │
Catalog C4 Filters (pre-filled from query)
        │
        ▼
Catalog C5 Active chips + C6 Results grid
        │
        ▼ card click «Подробнее»
        │
PDP Z3–Z4 (title · gallery · offer)
```

## 6.2 H4 Featured Inventory → Catalog

| Homepage H4 | Catalog destination |
|-------------|---------------------|
| Section title «Авто с пробегом в наличии» | C3 H1 «Каталог автомобилей с пробегом» (Phase 1 label family) |
| 4× `wf-v3-inventory-card` | C6 grid — **same card base**, catalog adds secondary fields |
| Link «Смотреть все →» | `/cars/` — unfiltered catalog entry |
| Card click | Same PDP URL as catalog card would use |

## 6.3 Shared partials (mandatory)

| Partial | Homepage | Catalog | PDP |
|---------|----------|---------|-----|
| Header | H0 | C0 | Z0 |
| USP row | H1 | C1 | Z1 |
| Footer | H10 | C10 | Z10 |
| Inventory card core | H4 | C6 | — (PDP is full stage) |
| Tokens / typography | `wf-v3-*` | `wf-v3-*` | `wf-v3-*` |

## 6.4 Composition continuity

Visitor leaving Homepage must feel: **same salon, deeper aisle** — not new site section. Header, USP, card photo stage, price red accent, and footer are **identical grammar**.

---

# SECTION 7 — Catalog → PDP Alignment

## 7.1 Field continuity map

| Catalog card field | PDP destination | Match rule |
|--------------------|-----------------|------------|
| Photo | Z4 gallery main image | Same vehicle asset / aspect treatment |
| Title «Audi A1, 2012» | Z3 H1 stem | PDP adds КПП · full mileage in title |
| Price 811 500 ₽ | Z4 offer price | **Exact match** — no catalog/PDP price drift |
| Old price (if shown) | Z4 strikethrough | Same figure |
| Year chip | Z4 specs grid «Год» | Same value |
| Mileage chip | Z3 title + Z4 specs «Пробег» | Same value |
| Monthly «от X ₽/мес» | Z4 «от X ₽/мес» | Same figure or catalog omits if PDP-only |
| Spec chips (КПП · fuel) | Z4 specs grid | Subset of PDP grid — no contradictions |
| «В наличии» badge | Z3 status badge | Consistent status |
| CTA «Подробнее» | — | Lands on same URL as card link |

## 7.2 Visual continuity

| Element | Rule |
|---------|------|
| Photo stage | `color-surface-studio` flat backdrop — card photo = gallery thumb grammar |
| Price typography | Same `$font-size-h3` / brand red role as PDP offer |
| Meta chips | Same muted small text as PDP spec labels (not values) |
| Border / surface | Flat card — max 2 depths (P-07); no nested OC `catalog_item` panels |

## 7.3 Deliberate PDP-only escalation

After click, PDP **adds depth** — not different brand:

- 65/35 gallery + offer (Z4)  
- Vehicle trust strip (Z5)  
- Equipment (Z6)  
- Credit calculator (Z7)  

Catalog card **teases**; PDP **confirms and converts**.

---

# SECTION 8 — Trust Model

## 8.1 Alignment principle

Catalog trust **extends** Homepage and PDP trust grammar — same tone (proof, not panic), same surfaces — **different proof scope**.

## 8.2 Trust hierarchy — three screens compared

| Tier | Homepage | **Catalog** | PDP |
|------|----------|-------------|-----|
| **T1 — Immediate** | Locality + phone in topbar (H0) | Same (C0) | Same (Z0) |
| **T2 — Inventory proof** | Featured 4 cards (H4) | **Result count + grid of priced cars (C3 + C6)** | Gallery + price (Z4) |
| **T3 — Structured proof** | Dealer strip (H5) | **Catalog trust strip (C8)** — dealer + inventory policy | Vehicle strip (Z5) |
| **T4 — USP facts** | Benefit row (H1) | Benefit row (C1) | Benefit row (Z1) |
| **T5 — Transaction** | Credit teaser (H7) | Optional teaser (C9) | Full calculator (Z7) |
| **T6 — Institutional** | Banks (H8) | Defer to footer / omit first pass | Banks (Z8) |
| **T7 — Contact** | Contact band + footer | Footer (C10) | Footer (Z10) |

## 8.3 Belongs on Catalog (C8 — catalog-specific)

- **Inventory scale signal** — «N автомобилей в наличии» in C3 (if count verifiable)  
- **Dealer verification** — same proof family as H5/Z5 but **dealer-level**: inspection program · no hidden fees · physical address · VIN policy at dealer level  
- **Filter transparency** — active chips show «мы не скрываем критерии»  
- **Real photos** — grid of actual inventory, not stock placeholders  

## 8.4 Belongs on Homepage only (not duplicated as primary on Catalog)

- Hero headline + search cluster (H2+H3)  
- Featured **curated** 4-card window  
- Expanded dealer advantages (H6)  
- Full homepage financing band (H7)  

## 8.5 Belongs on PDP only (not on Catalog cards)

- Vehicle-specific VIN report for **this** car  
- «12 человек смотрят» urgency  
- Full spec grid · equipment · credit form  
- Offer-column CTAs «Купить в кредит» · «Trade-in» · «Рассрочка»  

## 8.6 TEST anti-patterns (catalog trust)

| Legacy TEST pattern | WF-V3 direction |
|--------------------|-----------------|
| Reviews slider immediately below grid | **Remove** from catalog first screen path — trust via C8, not third-party widget |
| «VIN проверен» on every card with icon noise | Optional single badge max; full VIN flow on PDP |
| «* Цена при покупке в кredit» footnote on every card | Defer to PDP offer or one catalog footer note in C8 |

---

# SECTION 9 — Discovery Evidence Synthesis

## 9.1 Current state (TEST — negative reference only)

| Zone | Problem |
|------|---------|
| Filter block | OC form geometry · competes with header promo stack |
| Cards | `catalog_item` bordered · **swiper carousel per card** · nested price/VIN/btn |
| Below grid | Reviews widget · bank slider — distracts from inventory job |
| First screen | Filter heavy · weak «showroom grid» read |
| Perception | «OC catalog» — not Class B sibling to WF-V3 PDP |

## 9.2 Target state (WF-V3 — inherits Homepage + PDP)

| Zone | Direction |
|------|-----------|
| First screen | Filters + at least 2–3 card rows visible · flat inventory cards |
| Cards | Extend `wf-v3-inventory-card` — single photo · price dominant |
| Trust | C8 strip — dealer proof, not reviews carousel |
| Chrome | Shared header/footer/USP from frozen prototypes |
| Visual system | Same tokens as homepage + PDP prototypes |

## 9.3 Business truths preserved (P-19)

Brand **СИБКАР** · phone **+7 (383) 388-55-23** · address **ул. Богдана Хмельницкого 101** · menu labels · route `/cars/` · legal links — unchanged from Phase 1 freeze.

---

# SECTION 10 — Risks & Constraints

| Risk | Mitigation |
|------|------------|
| Catalog invents new card component | Mandate extend H4 `wf-v3-inventory-card` |
| Filter sidebar breaks WF-LAYOUT | Blueprint defines L-sidebar + L-grid; layout pass after prototype |
| Per-card swiper returns from TEST | Explicit anti-pattern · single photo v0.1 |
| Reviews/banks bloat catalog | Exclude from C0–C7; footer only |
| Price mismatch catalog ↔ PDP | Field continuity map §7.1 — static prototype uses same fixture data |
| No catalog concept PNG | Derive from homepage card + PDP tokens — same path as homepage discovery |
| Filter JS scope creep | Discovery = conceptual only; prototype v0.1 static filters OK |

---

# FINAL VERDICT

## **A — Ready For Catalog Prototype**

| Question | Answer |
|----------|--------|
| Is catalog purpose defined? | **YES** — §1 |
| Is Class B validated? | **YES** — §2 |
| Is IA defined? | **YES** — §3 + blueprint C0–C11 |
| Is inventory/card strategy defined? | **YES** — §4 |
| Are filters defined conceptually? | **YES** — §5 |
| Are Homepage and PDP alignments mapped? | **YES** — §6–§7 |
| Is trust model defined? | **YES** — §8 |
| Does catalog invent new visual class? | **NO** |
| Is PDP + Homepage authority sufficient? | **YES** — both prototypes frozen; card grammar exists |

### Why not B (Additional Discovery Required)

All nine task sections are addressed. Card grammar is proven in homepage prototype. Class B chain Homepage → Catalog → PDP is coherent. Remaining OPEN items (sidebar vs top filter layout, live inventory count copy) are **prototype HITL**, not discovery blockers.

### Preconditions before implementation (not blockers to verdict A)

| # | Precondition | Status |
|---|--------------|--------|
| 1 | Operator ratification of this discovery + blueprint | **OPEN** |
| 2 | Catalog Prototype Write Charter | **NOT CREATED** |
| 3 | Workspace (`workspaces/site-001-wf-v3-catalog-prototype/` or extend homepage workspace) | **NOT STARTED** |
| 4 | Sidebar vs horizontal filter geometry | **OPEN** — operator HITL at v0.1 |
| 5 | Shared partial extraction (header/footer/card) across 3 workspaces | **OPEN** — integration hygiene |

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| Live inventory count on TEST | **NOT VERIFIED** — affects C3 result count copy |
| Catalog concept PNG | **NONE** — derive from H4 card + PDP tokens (same as homepage path) |
| Brand sub-routes `/cars/{brand}/` | **IN SCOPE** as C2 breadcrumb variant — same C6 grid |
| Mobile filter drawer pattern | **SAFE UNKNOWN** — desktop-first; responsive deferred |
| Operator ratification verdict A | **SAFE UNKNOWN** — pending HITL |

**SECURITY RISK:** None (documentation only).

---

*SITE-001 WF-V3 Catalog Discovery v1 — discovery only; no implementation; no commit implied.*
