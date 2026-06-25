# BZPM M9.14 — Delivery — Design Charter v1

**Milestone:** M9.14 — Delivery / Доставка  
**URL (TEST):** `/delivery`  
**Program:** BZPM Corporate Pages Program  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Policy:** MANUAL UI REFINEMENTS ARE CANONICAL  
**Version:** v1  
**Status:** **DESIGN CHARTER — PENDING OPERATOR APPROVAL**  
**Date:** 2026-06-22  

**Boundary:** Design planning and visual-commitment rules only. This document does **not** authorize wireframes, mockups, HTML/CSS/JS, deploy, or TEST writes.

**Sources of truth:**

| Artefact | Path |
|----------|------|
| Design Program | [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](../BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md) |
| IA Map | [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](../BZPM-CORPORATE-PAGES-IA-MAP-v1.md) § M9.14 |
| Approved copy | [BZPM-M9.14-DELIVERY-PAGE-COPY-v1.1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.14-DELIVERY-PAGE-COPY-v1.1.md) |
| Forensic research | [BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md) |
| Contacts reference surface | [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md) · [SITE-002-CONTACTS-PAGE-POLISH-V1.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-POLISH-V1.md) |
| Pattern precedent | [BZPM-M9.13-ABOUT-COMPANY-DESIGN-CHARTER-v1.md](./BZPM-M9.13-ABOUT-COMPANY-DESIGN-CHARTER-v1.md) · [BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md](./BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md) |

**Primary design question:** *Как ЗПМ доставит оборудование до меня и насколько это безопасно и предсказуемо?*

**Secondary design question:** *Откуда отгрузят, как получить и что будет после оплаты?*

---

## 1. Purpose

### 1.1 Page mission

M9.14 `/delivery` is the **primary owner of logistics and shipping terms** for SITE-002 — not a transport-company directory, not a courier-service landing, not a marketplace shipping calculator.

The page exists to **remove logistics uncertainty** for B2B equipment buyers: clarify **where shipment originates**, **how receipt works**, **what happens after payment**, and **what the buyer receives** — without inventing route SLAs, freight prices, or carrier partnerships the operator has not attested.

Per forensic research: empty PLP `p-card__delivery` and sparse PDP `deliveryText` make this page a **conversion-critical fallback** — design must educate, not merely list carriers.

### 1.2 What this page is NOT

| Anti-goal | Reason |
|-----------|--------|
| Transport-company directory / TK aggregator | TK names are supporting reference — not page identity |
| Courier-service or last-mile consumer UX | B2B industrial equipment — not parcel tracking app |
| Marketplace / ecommerce shipping page | No per-SKU calculator, no checkout freight selector |
| Geography map marketing page | Russia coverage is prose + predictability — not map hero |
| Factory OEM story | Production narrative → `/about` |
| Payment / invoice mechanics chapter | Ship-after-pay is summary + link → `/payment-methods` |
| Warranty RMA legal chapter | Return logistics → `/guarantee` summary + link |
| Dealer channel freight policy | Channel terms → `/dealers` one line |

### 1.3 What this page IS

A **manufacturer logistics clarity page**: scannable **shipment-point anchors** (Барнаул + МО partner), honest **receipt-method comparison** (самовывоз vs ТК), **7-step shipment process** (SC-04), **packaging and document confidence**, and a **single escalation path** to clarify regional delivery.

---

## 2. Audience hierarchy

| Segment | Priority | What they need from design |
|---------|----------|----------------------------|
| **Снабженец / логист** | **Primary** | Regional feasibility, shipment points, TK path, documentation at handoff |
| **Закупщик** | **Primary** | Timing relative to payment/production, document pack, predictability before tender |
| **Владелец бизнеса** | **Secondary** | Opening timeline confidence — «доставите в мой город?» without opaque freight |
| **Дилер / региональный партнёр** | **Tertiary** | General shipment rules here; channel-specific terms → `/dealers` |

**Design implication:** Layout rewards **feasibility scan → process understand → method choose → escalate** — not carrier comparison shopping or map exploration.

---

## 3. Conversion hierarchy

### 3.1 Primary

**Delivery inquiry** — visitor submits **«Отправить запрос»** form (FORM) with **region** field after understanding shipment model and process.

Success signal: logistics user knows **whether delivery to their region is feasible** and **what to expect at handoff** before manager call; form captures region + optional method preference for routing.

### 3.2 Secondary

**Catalog exploration** — «Перейти в каталог» when buyer needs SKU selection before logistics planning (BLOCK 09).

### 3.3 Tertiary

**Contacts / requisites** — «Контакты и реквизиты» → `/contact/` for visit directions to Барнаул production site, schedule, or general inquiry.

**Rule:** Tertiary visible in CTA band but **must not** outrank primary form submit.

---

## 4. Trust hierarchy

Ranked by **logistics anxiety reduction** for equipment procurement.

| Rank | Trust signal | Source | Design role |
|------|--------------|--------|-------------|
| **T1** | **Predictable shipment process** (согласование → оплата → комплектация → упаковка → передача → документы → получение) | BLOCK 04 | Dominant visual — SC-04 timeline |
| **T2** | **Named shipment points** (Барнаул production + МО partner warehouse) | BLOCK 02 | SC-05 fact cards — factual anchors |
| **T3** | **Honest method posture** (самовывоз or ТК; buyer chooses; no fake SLA) | BLOCK 03 | Method comparison — informational, not checkout |
| **T4** | **Packaging and handoff preparedness** | BLOCK 05 | Reduces damage anxiety — manufacturer responsibility framing |
| **T5** | **Russia-wide coverage without «special regime»** | BLOCK 06 | Predictability prose — remote B2B is normal |
| **T6** | **Document and outcome clarity** | BLOCK 07 | What buyer receives — links to Payment/Warranty |
| **T7** | **Manager accompaniment on shipment stage** | Lead; BLOCK 01; FAQ | Human escalation — not tracking-app UX |
| **T8** | **TK reference list** (named carriers, non-exhaustive) | BLOCK 03 table | Supporting proof — **not** logo wall |

**Explicitly subordinate (do not visual-promote without OQ unlock):**

- Route-level delivery day counts
- «От 1 дня» marketing SLA (Commercial Trust — not verified for corp copy)
- Cargo insurance policy
- GOST / internal packaging standard badges
- TK partner logo grid
- Regional freight price table

---

## 5. Page role in buyer journey

### 5.1 Journey position

```
Catalog / PDP delivery micro-strip (often empty)
        │
        ▼
   ┌─────────┐
   │  ABOUT  │  (optional — factory geography context)
   └────┬────┘
        │
        ▼
   ┌─────────┐
   │ PAYMENT │  (ship-after-pay gate)
   └────┬────┘
        │
        ▼
   ┌─────────┐
   │DELIVERY │  ◄── logistics clarity (this page)
   └────┬────┘
        │
   ┌────┴────────────────────────┐
   │                             │
   ▼                             ▼
Contacts                    Warranty / Custom
(visit directions)          (oversized / RMA branches)
        │
        ▼
   Dealers (channel logistics pointer)
```

### 5.2 Before this page

| Prior state | Typical entry | Page must do |
|-------------|---------------|--------------|
| Payment understood | Payment → Delivery link | Assume pay-before-ship; skip invoice detail |
| Catalog hesitation | PLP/PDP empty delivery strip → header «Доставка» | Answer Q1 «доставите в мой регион?» fast |
| About trust established | About geo mention | Skip factory story — go operational logistics |
| Tender planning | Search «доставка ЗПМ регион» | Coverage + process without fake timelines |
| Dealer candidate | Dealers → Delivery | General rules; channel depth on Dealers |

### 5.3 After this page

| Exit | When |
|------|------|
| FORM submit | Needs region-specific routing, method advice, oversized consult |
| `/payment-methods` | Needs payment timing before ship (lead + FAQ 2) |
| `/contact/` | Needs visit to Барнаул, office schedule, legal requisites |
| `/guarantee` | Damage at receipt vs warranty claim routing (FAQ 8) |
| `/custom-equipment` | Oversized / non-standard logistics (BLOCK 03 H3, FAQ 6) |
| `/dealers` | Partner channel supply terms |
| `/about` | Wants production geography depth |
| `/` catalog | SKU selection before logistics question |
| Phone / email | Urgent shipment coordination |

**Program note:** Delivery is **design order #3** — instantiates SC-04 (from Payment), SC-05 shipment cards, SC-06 documents, SC-15 geography; becomes shared proof pattern for Dealers BLOCK 05 and Warranty RMA summary.

---

## 6. Relationship with sibling pages

CP-01 rule: **one primary owner per topic**. Delivery shows **one-line summary + text link** — never embedded foreign page body.

| Page | URL | Delivery relationship | Allowed on Delivery | Forbidden on Delivery |
|------|-----|----------------------|---------------------|----------------------|
| **About** | `/about` | BLOCK 06 cross-link | «Производство и география завода» one line + link | Factory video, OEM narrative, cert promo |
| **Payment** | `/payment-methods` | Lead; BLOCK 04 step 1; FAQ 2; CTA pointer | Ship-after-pay; payment handoff link | Invoice/VAT, methods matrix, bank requisites |
| **Warranty** | `/guarantee` | BLOCK 07 outcome row; FAQ 8 | RMA / damage routing summary + link | Term badge, claim process, SLA |
| **Dealers** | `/dealers` | BLOCK 06 dealer note | Channel logistics pointer + link | Discounts, territory, drop-ship policy |
| **Custom** | `/custom-equipment` | BLOCK 01; BLOCK 03 H3; FAQ 6 | Oversized summary + link | TZ checklist, parameter matrix, upload form |
| **Contacts** | `/contact/` | BLOCK 02 note | Visit directions to Барнаул; requisites link | Full contact card grid, map embed duplicate |
| **Certification** | `/our-certification` | — | Not primary on Delivery | Cert PDF gallery |

**МО warehouse address ownership (charter lock — program blocker B1):**

| Decision | Detail |
|----------|--------|
| **Conflict** | Copy v1.1 uses live `CITY_DATA`: пос. Никольское, 204 — vs research «ул. Басовская, 14с2» |
| **Charter default** | Design uses **copy v1.1 address** until operator locks canonical |
| **Single source** | One canonical МО address must propagate to Dealers BLOCK 05 before implementation |
| **Visual** | Both shipment cards equal structure — **no** «primary warehouse» map pin hierarchy until OQ resolved |

**Contacts alignment:** FORM extends SC-10 with **region** (required) + **delivery_method** + **order_details**; consent, phone mask, success microcopy match delivered Contacts discipline.

---

## 7. Evidence hierarchy

### Level 1 — Must be visible without deep scroll (first ~2 viewports)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| Russia delivery feasibility | Lead + BLOCK 01 summary row | H1 zone + lead — typographic clarity |
| **Two shipment points** (Барнаул + МО) | BLOCK 02 | SC-05 cards — **factual anchors in first screen or immediate scroll** |
| **Shipment process start** (steps 1–3 visible) | BLOCK 04 | SC-04 timeline — **dominant element** |
| Payment cross-link in lead | Lead | Inline link — ship-after-pay context |
| Optional trust strip | MICROCOPY trust strip | 3 micro-labels — subordinate to H1+lead |

### Level 2 — Core proof stack (mid-page, scroll expected)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| Full 7-step shipment process | BLOCK 04 | SC-04 timeline — complete sequence |
| Receipt methods (ТК + 2× самовывоз + oversized) | BLOCK 03 | H3 sections + comparison discipline |
| Packaging preparedness | BLOCK 05 | 4 H3 subsections — trust without GOST badges |
| Russia predictability framework | BLOCK 06 | SC-15 prose — 3 planning factors |
| Shipment documents / buyer outcomes | BLOCK 07 | Outcome list — 7 rows |
| TK reference table | BLOCK 03 | Text table — **supporting**, not hero |

### Level 3 — Supporting context (lower visual weight)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| BLOCK 01 organization prose | BLOCK 01 | Intro framing — subordinate to summary row |
| FAQ (8) | BLOCK 08 | SC-08 accordion — objection cleanup |
| Dealer / Custom / Warranty pointers | Body microcopy | Inline links only |
| Cost note (ТК calculates freight) | BLOCK 03 microcopy | Text — no price UI |
| Image caption (shipment points) | BLOCK 02 | Optional static graphic — not map hero |

---

## 8. Visual narrative

Narrative arc is **predictable manufacturer handoff**, not carrier marketing.

### Beginning — «Доставите ли вы и откуда?» (Utility → BLOCK 02)

| Beat | Content | Emphasis |
|------|---------|----------|
| Orient | Breadcrumb, H1, lead | SC-01 internal-page rhythm — align Contacts shell |
| Frame | Lead + optional trust strip | Russia supply; two points; manager accompaniment |
| **Anchors** | BLOCK 01 summary row + BLOCK 02 shipment cards | **Where shipment originates** — scan before deep scroll |
| Payment context | Lead link to Payment | Ship-after-pay — one line, not Payment duplicate |

**Beginning must answer Q1 (регион?) and Q3 (откуда отгрузка?) in <10 seconds of scan.**

### Middle — «Как это проходит и насколько безопасно?» (BLOCK 03 → BLOCK 07)

| Beat | Content | Emphasis |
|------|---------|----------|
| Methods | BLOCK 03 receipt options + TK table | How to receive — **informational comparison** |
| **Process** | BLOCK 04 shipment timeline | **Peak visual — predictable 7-step path** |
| Safety | BLOCK 05 packaging | Damage-risk reduction — manufacturer prep |
| Reach | BLOCK 06 Russia coverage | Predictability factors — not map exploration |
| Outcomes | BLOCK 07 what buyer receives | Document + responsibility clarity |

**Middle must answer Q2, Q4, Q5, Q6 from IA without leaving page (except Payment/Custom/Warranty depth links).**

### End — «Уточните для вашего региона» (BLOCK 08 → FORM)

| Beat | Content | Emphasis |
|------|---------|----------|
| Objections | BLOCK 08 FAQ | Regional, timing, TK choice, damage — honest SAFE UNKNOWN |
| Action | BLOCK 09 CTA + FORM | **Primary conversion zone** — region-specific inquiry |

**End must make «Задать вопрос по доставке» obvious; phone/email support visible.**

---

## 9. Block importance map

Ranking for **all approved v1.1 copy blocks** (Critical / Important / Supporting).

| Block | Title | Rank | Rationale |
|-------|-------|------|-----------|
| Utility | Meta, breadcrumb | Supporting | Required shell — no visual competition |
| — | H1 + Lead | **Critical** | Feasibility framing + Payment cross-link |
| **01** | Как организована доставка | Important | Organization frame + summary row — not page spine |
| **02** | Откуда осуществляется отгрузка | **Critical** | Shipment point anchors — SC-05 |
| **03** | Способы получения оборудования | **Critical** | Method comparison + TK reference |
| **04** | Как проходит отгрузка | **Critical** | Primary mental model — page spine |
| **05** | Как подготовлено оборудование к отправке | Important | Packaging trust — safety narrative |
| **06** | Доставка по России | Important | Coverage predictability — SC-15 |
| **07** | Что получает заказчик | Important | Outcome list — documents + responsibility |
| **08** | FAQ | Important | Objection resolver — pre-CTA |
| **09** | CTA | **Critical** | Conversion band |
| FORM | Запрос по доставке | **Critical** | Primary conversion instrument |
| MICRO | Trust strip | Important | Optional — accelerates scan if placed after lead |

---

## 10. Visual emphasis strategy

### 10.1 What MUST dominate visually

| Element | Why |
|---------|-----|
| BLOCK 04 SC-04 process timeline (7 steps) | Answers primary question — predictability and safety through known stages |
| BLOCK 02 SC-05 shipment point cards (2) | Answers «откуда» — factual anchors |
| BLOCK 03 method structure (ТК vs самовывоз) | Answers «как получить» — without checkout UX |
| BLOCK 05 packaging chapter | Answers «насколько безопасно» — manufacturer prep |
| BLOCK 09 + FORM | Conversion endpoint — region-specific escalation |
| Lead Russia + two-point framing | Immediate feasibility signal |

### 10.2 What must NOT dominate visually

| Element | Why |
|---------|-----|
| TK company table / logos | Supporting reference — not page identity |
| Geography map | No operator asset; prose suffices — anti map-heavy |
| BLOCK 01 long prose | Summary row carries scan; body is supporting |
| BLOCK 06 as map block | Predictability prose — not regional heatmap |
| Truck / warehouse stock photography | Asset rule — real photo only if operator provides |
| Route animation / delivery tracker UI | Courier-service anti-pattern |
| Freight price calculator | Not attested — forbidden |
| «От N дней» SLA chips | SAFE UNKNOWN — forbidden |
| BLOCK 08 FAQ as primary content | Accordion is cleanup, not hero |

### 10.3 Visual weight budget (relative 1–5)

| Block | Tier | Weight | Notes |
|-------|------|--------|-------|
| **04** | Tier 1 — Anchor | **5** | Largest structured component — SC-04 owner |
| **02** | Tier 1 — Anchor | **4** | Two equal shipment cards — Barnaul + МО |
| **03** | Tier 1 — Anchor | **4** | Methods — H3 stack + subordinate TK table |
| **09 + FORM** | Tier 1 — Anchor | **4** | CTA + form endpoint |
| **05** | Tier 2 — Support | **3** | Packaging trust — 4 H3 sections |
| **07** | Tier 2 — Support | **3** | Outcome list — 7 rows |
| **06** | Tier 2 — Support | **3** | Russia prose — SC-15 |
| **08** | Tier 2 — Support | **3** | 8-item accordion |
| **01** | Tier 2 — Support | **2** | Summary row > body prose |
| Trust strip | Tier 2 — Support | **2** | 3 micro-labels — optional |
| Lead | Tier 1 | **3** | Sets frame — not longer than process intro |
| TK table (within 03) | Tier 3 — Context | **2** | Text rows — no logo column |

**Section rhythm:** Avoid 9 equal-weight sections — Tier 1 blocks need clear vertical separation (Contacts internal-page spacing).

---

## 11. Logistics visualization philosophy

### 11.1 Charter decision — choose ONE dominant approach

| Approach | Verdict |
|----------|---------|
| A) Geography | **REJECTED as dominant** — coverage is prose (BLOCK 06); no map hero |
| **B) Process** | **SELECTED — dominant** |
| C) Transport companies | **REJECTED as dominant** — TK table is supporting reference only |

### 11.2 Why Process (B)

| Reason | Detail |
|--------|--------|
| Primary question alignment | Buyer anxiety is **predictability** — «что будет после оплаты и до получения на объекте» |
| Copy spine | BLOCK 04 is the longest structured evidence block (7 steps) — natural visual anchor |
| Program consistency | SC-04 locked on Payment (M9.15) — Delivery extends same corp mental model |
| Anti-aggregator | Process framing keeps **manufacturer** as actor — TK is handoff step, not page hero |
| SAFE UNKNOWN discipline | No route maps or day-count badges needed when process steps carry honesty |
| Forensic risk G-03 | Generic information template — process timeline gives hierarchy live page lacks |

### 11.3 Supporting roles (non-dominant)

| Approach | Role on page |
|----------|--------------|
| Geography | BLOCK 02 cards (point names) + BLOCK 06 prose — **supporting** |
| Transport companies | BLOCK 03 text table — **tertiary reference** |

**Forbidden as visual spine:** Map-first layout, TK logo grid, route animation, freight calculator.

---

## 12. Warehouse strategy

### 12.1 Two-point model

| Point | Copy role | Visual importance |
|-------|-----------|-------------------|
| **Барнаул — производство и основной склад** | Primary origin — manufacturing + majority shipments | **High** — first card in SC-05 pair; caption «Производство и основной склад» |
| **МО — склад партнёра** | Central region convenience — conditional routing | **High but equal card weight** — second card; caption «Склад партнёра для центрального региона» |

### 12.2 Barnaul vs Moscow region — dominance rule

| Decision | Detail |
|----------|--------|
| **Do warehouses dominate the page?** | **Important — not page-wide dominant** |
| Relative weight | Shipment cards (BLOCK 02) = Tier 1 (4/5) but **subordinate to BLOCK 04 process (5/5)** |
| Barnaul emphasis | Copy positions Barnaul as production origin — card order **Барнаул first** |
| МО emphasis | Equal card structure — **no** «satellite dot» minimization; partner warehouse is legitimate ship point |
| Map graphic | **Optional** static two-point schematic only if operator provides — default = **address cards only** |
| Contacts overlap | Барнаул visit/directions → Contacts link in BLOCK 02 note — **not** duplicate map embed |

### 12.3 Address conflict (operator lock required)

| Status | Charter handling |
|--------|------------------|
| МО: Никольское 204 (copy) vs Басовская 14с2 (research) | Design uses copy v1.1; flag OQ-DC-D01 |
| Implementation | **Blocked** on single canonical address before build |

---

## 13. Transport company strategy

### 13.1 How visible should the TK list be?

| Parameter | Decision |
|-----------|----------|
| Visibility | **Present — supporting tier** within BLOCK 03 |
| Format | **Text table** (5 rows) — company name, region, note column |
| Logo column | **FORBIDDEN** unless operator attests logo assets per carrier |
| Position | **After** H3 method sections — reads as «examples we use», not «choose your carrier here» |
| Caption | Per copy: «Транспортные компании, с которыми ЗПМ регулярно организует отправку» |

### 13.2 What role does TK list play?

| Role | Detail |
|------|--------|
| **Credibility signal** | Named carriers reduce «серый перевозчик» anxiety |
| **Not exhaustive directory** | Note microcopy: other TK possible by agreement |
| **Not pricing surface** | Cost note: ТК calculates — separate from factory |
| **Not tracking UI** | Tracking info comes **after** handoff — step 6 in BLOCK 04 |
| **FAQ reinforcement** | FAQ 5 confirms choice flexibility — accordion, not expanded table |

### 13.3 TK logos dominate?

| Decision | **NO** |
|----------|--------|
| Default | Prose table only |
| If operator supplies logos | Small monochrome marks in table — **max 5**, single row height — still subordinate to process |
| Forbidden | Logo wall, carrier carousel, «official partner» badges without legal attestation |

---

## 14. Delivery confidence strategy

How the page builds **safe and predictable** delivery confidence — trust mechanisms ranked.

| Rank | Mechanism | Design treatment |
|------|-----------|------------------|
| **1** | **Visible end-to-end process** | BLOCK 04 SC-04 — user sees full path before asking manager |
| **2** | **Named origin points** | BLOCK 02 cards — real addresses, role labels |
| **3** | **Packaging and prep narrative** | BLOCK 05 — manufacturer cares before handoff |
| **4** | **Outcome transparency** | BLOCK 07 — what arrives (equipment + docs + tracking info) |
| **5** | **Honest timing posture** | Timeline note + FAQ 2 — «по согласованию», no fake days |
| **6** | **Responsibility boundary clarity** | BLOCK 07 row + FAQ 8 — factory vs ТК vs warranty routing |
| **7** | **Russia-wide normalization** | BLOCK 06 — remote delivery is standard B2B |
| **8** | **Manager accompaniment** | Lead, BLOCK 01, form — human on shipment stage |
| **9** | **TK name familiarity** | BLOCK 03 table — supporting only |

**Confidence must NOT rely on:** map coverage shading, animated trucks, SLA countdowns, insurance badges, or freight price promises.

---

## 15. FAQ strategy

### 15.1 Role

FAQ is **objection resolver** for logistics edge cases — not primary education (BLOCK 02–07 own that).

### 15.2 Parameters

| Parameter | Decision |
|-----------|----------|
| Count | **8 items** — per approved copy; do not expand |
| Pattern | SC-08 single-open accordion |
| Position | After BLOCK 07, before BLOCK 09 |
| Visual weight | Important — **subordinate** to BLOCK 04 and BLOCK 02 |

### 15.3 Priority items (mobile density)

| Priority | FAQ | Why |
|----------|-----|-----|
| 1 | Доставляете ли в мой регион? | Core Q1 |
| 2 | Когда отгрузка после оплаты? | Core Q5 + Payment link |
| 3 | Самовывоз возможен? | Core Q2 — addresses |
| 4 | Кто оплачивает доставку? | Freight cost anxiety |
| 5 | Крупногабарит? | Core Q6 + Custom link |
| 6–8 | Remaining | TK choice, documents, damage |

### 15.4 Overlap discipline

FAQ must **not repeat** full BLOCK 04 timeline or BLOCK 02 address cards — short confirmatory answers with links to owners (Payment, Custom, Guarantee).

### 15.5 Forbidden FAQ patterns

- Accordion headers with «3–5 дней» chips
- Embedded TK pricing table in answers
- Map thumbnails per region

---

## 16. CTA strategy

### 16.1 Hierarchy (locked)

| Priority | Element | Placement |
|----------|---------|-----------|
| **Primary** | «Задать вопрос по доставке» → form submit | BLOCK 09 + FORM only |
| **Secondary** | «Перейти в каталог» | BLOCK 09 — subordinate |
| **Tertiary** | «Контакты и реквизиты» | BLOCK 09 link |
| **Support** | Phone `8 (3852) 72-18-90` · `info@bzpm.ru` | BLOCK 09 inline |

### 16.2 One CTA or multiple?

| Decision | **One primary button zone per page** |
|----------|--------------------------------------|
| Mid-page buttons | **FORBIDDEN** — no «Отправить запрос» before BLOCK 09 |
| Text links | Permitted in lead, process steps, BLOCK 03–07 — not button-styled |
| Phone as parallel CTA | Visible in BLOCK 09 — support, not competing primary button |

### 16.3 Placement philosophy

CTA H2 **«Уточнить условия поставки для вашего региона»** — region-specific framing matches FORM **region** field.

CTA band **after FAQ** — user has consumed anchors, process, methods, packaging, coverage, outcomes, and residual objections.

FORM immediately follows CTA band (or integrated in same visual zone per SC-09).

**Micro pointer under CTA body:** Payment — text link only (copy-provided).

---

## 17. Form strategy

### 17.1 Role

FORM is the **logistics escalation instrument** — captures **region** (required) and optional method/order context; not a generic callback form.

### 17.2 Relationship to Contacts

| Aspect | Delivery FORM | Contacts form |
|--------|---------------|---------------|
| Purpose | Regional delivery / shipment consultation | General inquiry + requisites discovery |
| Unique fields | **region** (required), delivery_method, order_details | No logistics fields |
| Shared | name, phone, email, consent, privacy link, submit states | SC-10 base |
| Success microcopy | Manager callback пн–пт 9–18 Барнаул | Same discipline |

### 17.3 Rules

| Rule | Detail |
|------|--------|
| Do not duplicate Contacts contact card grid above form | Shipment cards + phone in CTA suffice |
| Do not embed freight calculator | Not in copy |
| **region** field prominence | Visually emphasized — matches CTA H2 regional framing |
| delivery_method | Optional select/text — not required; reduces form friction |
| Backend | **SAFE UNKNOWN** — same `action="#"` posture as Contacts until implementation charter |

---

## 18. Design risks

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R1 | **МО address conflict** propagates to Dealers | **High** | OQ-DC-D01 operator lock; single canonical source |
| R2 | Method comparison mimics checkout / cart shipping step | **High** | Informational H3 layout — no «Выбрать доставку» buttons |
| R3 | TK table becomes de facto page hero (live page pattern) | **High** | §13 — prose table subordinate to BLOCK 04 |
| R4 | Map temptation without asset | **Medium** | SC-15 prose default; two-point cards only |
| R5 | Empty PLP delivery strip → high traffic, weak legacy template | **High** | Process + cards give hierarchy (forensic G-02, G-03) |
| R6 | Duplicate SC-04 fatigue vs Payment | **Medium** | 7 steps vs Payment 6 — different labels; shared component, distinct copy |
| R7 | BLOCK 03 + BLOCK 05 packaging overlap | **Medium** | BLOCK 04 step 4 points to BLOCK 05; visual dedup in design pass |
| R8 | «От 1 дня» marketing drift from homepage/Commercial Trust | **Medium** | Copy excludes — design must not reintroduce |
| R9 | Fake TK partner logos | **High** | Prose only unless operator attests |
| R10 | Long page (9 blocks + form) scroll fatigue | **Medium** | Tier weight map; section spacing |
| R11 | Form region field vs city popup (`CITY_DATA`) | **Low** | Implementation charter — no auto-conflict |
| R12 | Production URL parity unknown | **Low** | Document at implementation |

---

## 19. Forbidden patterns

| Pattern | Why forbidden |
|---------|---------------|
| **Map-heavy page** / Russia heatmap hero | Geography is supporting — no operator map asset |
| **Fake delivery map** / invented route lines | SAFE UNKNOWN — misleads regional feasibility |
| **Route animations** / moving truck SVG | Courier-service / aggregator aesthetic |
| **Truck stock photos** | Asset rule — real warehouse/loading only if operator provides |
| **Transport-company directory** as page spine | Anti-goal — page is not TK catalog |
| **Courier-service style** (tracking widget, parcel timeline) | B2B equipment — not last-mile consumer UX |
| **Marketplace logistics style** (seller ships, multi-vendor) | Single manufacturer — ЗПМ |
| **Ecommerce shipping page** (freight calculator, rate cards) | No per-SKU pricing attested |
| TK logo wall without attestation | Fake partner implication |
| «От N дней» / SLA countdown chips | SAFE UNKNOWN |
| Per-SKU delivery calculator | Owner: Catalog / PDP |
| Factory OEM video / story | Owner: About |
| Invoice/VAT / bank detail | Owner: Payment / Contacts |
| Warranty RMA process depth | Owner: Warranty |
| Dealer freight policy / territory map | Owner: Dealers |
| Custom engineering workflow | Owner: Custom |
| Multiple primary CTA buttons mid-page | §16.2 |
| Autoplay logistics animation | UX noise + reduced-motion |
| Drop-ship promises without OQ-D04 | Channel policy unknown |

---

## 20. Success criteria

Operator judges Delivery design **successful** when:

| # | Criterion | Verification method |
|---|-----------|---------------------|
| S1 | Visitor answers IA Q1–Q6 on-page (except Payment/Custom/Warranty depth) | Copy coverage audit vs IA map |
| S2 | Primary question answered: **как доставят + насколько предсказуемо/безопасно** | Operator scenario test |
| S3 | BLOCK 04 process scannable in **<20 seconds** desktop | Operator scan test |
| S4 | BLOCK 02 shipment points visually distinct and copy-accurate | Address audit vs canonical lock |
| S5 | Page does **not** read as transport aggregator or courier service | Operator visual compare |
| S6 | TK table present but **subordinate** to process and shipment cards | Design review |
| S7 | No CP-01 violations — sibling topics are links only | Cross-link audit |
| S8 | FORM includes required **region** field; consent matches Contacts | Side-by-side with `/contact/` |
| S9 | SC-04 / SC-05 / SC-06 instantiated per program registry | Design program check |
| S10 | One primary CTA zone — no mid-page submit | Design review |
| S11 | Mobile ≤1024px — method sections and cards stack without horizontal scroll trap | Responsive check |
| S12 | No fake map, route animation, or SLA day badges | Governance check |
| S13 | Design charter approved **before** wireframe/mockup work | Phase gate |

---

## 21. Special requirement resolutions

### 21.1 Page feel — A / B / C

| Mode | Verdict |
|------|---------|
| A) Logistics company | **REJECTED** — ЗПМ is not a ТК or 3PL |
| **B) Manufacturer logistics** | **SELECTED** |
| C) Transport aggregator | **REJECTED** — TK list is reference, not identity |

**Manufacturer logistics means:** factory originates shipment, prepares equipment, hands to carrier or buyer — visual language of **industrial B2B order fulfillment**, aligned with Payment operational mode.

### 21.2 Should warehouse locations dominate?

| Decision | **Important — not dominant** |
|----------|-------------------------------|
| Treatment | SC-05 two-card row — Tier 1 (4/5), **below** BLOCK 04 process (5/5) |
| Barnaul | First card order — production origin |
| МО | Equal card weight — partner warehouse legitimacy |

### 21.3 Should TK logos dominate?

| Decision | **NO** |
|----------|--------|
| Default | Text table in BLOCK 03 — Tier 3 (2/5) |
| Logos | Only if operator attests — small, subordinate |

### 21.4 Should geography dominate?

| Decision | **NO** |
|----------|--------|
| BLOCK 06 | SC-15 prose — predictability factors, not map |
| Russia coverage | Supporting confidence — remote is normal |

### 21.5 Should delivery process dominate?

| Decision | **YES — primary visual anchor** |
|----------|--------------------------------|
| BLOCK 04 | Highest visual weight (5/5) |
| Shared pattern | SC-04 — third corp instantiation after Payment |

### 21.6 Trust strip placement

| Element | Placement decision |
|---------|-------------------|
| Trust strip (3 badges) | **Optional** — after lead, before BLOCK 01; if used, subordinate to H1+lead |
| Summary row (BLOCK 01) | Inline micro-labels — can substitute for separate strip; **avoid duplicate** |

### 21.7 Shared components instantiated on Delivery

| ID | Component | Delivery blocks |
|----|-----------|----------------|
| SC-01 | Corp page shell | All |
| SC-04 | Process timeline | BLOCK 04 |
| SC-05 | Proof / fact cards | BLOCK 02 shipment points |
| SC-06 | Document checklist | BLOCK 05 H3 docs; BLOCK 07 outcomes |
| SC-08 | FAQ accordion | BLOCK 08 |
| SC-09 | CTA band | BLOCK 09 |
| SC-10 | Corp inquiry form | FORM (+region variant) |
| SC-12 | Cross-link inline | Lead, body, CTA pointers |
| SC-15 | Geography / coverage | BLOCK 06 |

**Delivery is primary owner** for SC-05 shipment-point cards and SC-15 coverage prose variant — Dealers BLOCK 05 composes links to this page.

---

## 22. Open questions (operator lock)

| ID | Question | Impact | Default if unresolved |
|----|----------|--------|----------------------|
| OQ-DC-D01 | Canonical МО warehouse address — Никольское 204 vs Басовская 14с2? | BLOCK 02, Dealers BLOCK 05 | **Copy v1.1** (Никольское 204) until operator lock |
| OQ-DC-D02 | Two-point schematic image for BLOCK 02? | Optional graphic | **Address cards only** — no map |
| OQ-DC-D03 | Warehouse / loading photo — operator asset? | BLOCK 02 optional image | **Exclude** — no stock trucks |
| OQ-DC-D04 | Trust strip after lead — include? | First screen density | **Include** 3 micro-labels OR BLOCK 01 summary row — not both |
| OQ-DC-D05 | TK logos — any attested carrier marks? | BLOCK 03 table | **Text only** |
| OQ-DC-D06 | Catalog secondary CTA URL — `/` vs hub | BLOCK 09 | `/` per copy note |
| OQ-DC-D07 | Drop-ship for dealers (OQ-D04 forensic) | FAQ / dealer note | Defer to Dealers — one-line pointer only |
| OQ-DC-D08 | Cargo insurance mention | Trust narrative | **Exclude** — not in copy |
| OQ-DC-D09 | `deliveryText` / PLP strip population — design coupling? | Catalog secondary | **Defer** — documentation parallel |
| OQ-DC-D10 | Legacy generic information template — new `zpm-delivery-*` namespace? | Implementation | Defer to implementation charter |
| OQ-DC-D11 | Privacy policy route `/privacy-policy` | Form consent | Verify at implementation — assumed per copy |

---

## 23. Design readiness verdict

| Dimension | Status | Notes |
|-----------|--------|-------|
| Copy | **READY** | v1.1 complete — operator approval header pending |
| IA | **READY** | CP-01 boundaries locked; Delivery = logistics owner |
| Charter | **READY FOR OPERATOR REVIEW** | This document |
| Assets | **PARTIAL** | No warehouse photo; no map; structural SC-04/SC-05 sufficient |
| OQ | **PARTIAL** | OQ-DC-D01 **blocks implementation** on МО address; charter can proceed with copy default |
| Visual design | **NOT READY** | Awaits operator charter approval |
| Implementation | **NOT READY** | Awaits design approval + implementation charter + address lock |
| Downstream unlock | **PARTIAL** | SC-05 shipment cards pattern for Dealers BLOCK 05 |

**Verdict:** M9.14 Delivery is **PARTIAL DESIGN READY** — charter pass complete; operator may approve charter and authorize **visual design phase** with **manufacturer-logistics / process-dominant** posture, shipment-point cards as factual anchors, TK table subordinate, and explicit deferrals (no map, no SLA chips, no TK logos by default).

**Program blocker note:** Resolve **OQ-DC-D01** (МО address) before implementation — first affected charter per Design Program B1.

**Explicit stop:** No wireframes · no mockups · no Twig/CSS/JS · no deploy.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-22 | **CREATED** — Design Charter v1; resolves manufacturer-logistics mode; process-dominant visualization; warehouse/TK/geography emphasis; delivery confidence ranking; CP-01 sibling relationships; program blocker B1 flagged |

---

*BZPM M9.14 Delivery Design Charter v1 — documentation only. No design, wireframes, mockups, or implementation authorized.*
