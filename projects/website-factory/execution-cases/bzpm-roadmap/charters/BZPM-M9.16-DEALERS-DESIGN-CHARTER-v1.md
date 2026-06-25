# BZPM M9.16 — Dealers — Design Charter v1

**Milestone:** M9.16 — Dealers / Дилерам  
**URL (TEST):** `/dealers`  
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
| IA Map | [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](../BZPM-CORPORATE-PAGES-IA-MAP-v1.md) § M9.16 |
| Approved copy | [BZPM-M9.16-DEALERS-PAGE-COPY-v1.1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.16-DEALERS-PAGE-COPY-v1.1.md) |
| Forensic research | [BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) |
| Contacts reference surface | [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md) · [SITE-002-CONTACTS-PAGE-POLISH-V1.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-POLISH-V1.md) |
| Pattern precedent | [BZPM-M9.13-ABOUT-COMPANY-DESIGN-CHARTER-v1.md](./BZPM-M9.13-ABOUT-COMPANY-DESIGN-CHARTER-v1.md) · [BZPM-M9.14-DELIVERY-DESIGN-CHARTER-v1.md](./BZPM-M9.14-DELIVERY-DESIGN-CHARTER-v1.md) · [BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md](./BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md) · [BZPM-M9.17-WARRANTY-DESIGN-CHARTER-v1.md](./BZPM-M9.17-WARRANTY-DESIGN-CHARTER-v1.md) |

**Primary design question:** *Почему дилеру выгодно и безопасно работать именно с производителем ЗПМ?*

**Explicitly NOT the primary question:**

- «Как стать дилером за 30 секунд»
- «Заполните форму»

---

## 1. Purpose

### 1.1 Page mission

M9.16 `/dealers` is the **primary owner of dealer / wholesale / channel partnership framing** for SITE-002 — not a franchise recruitment landing, not an MLM partner program page, not a lead-generation squeeze page, not a discount marketing poster.

The page exists to **remove channel-partnership uncertainty** for B2B partners evaluating OEM supply: clarify **who ЗПМ is as a manufacturer**, **why direct factory contact is safer than intermediary chains**, **what a partner can realistically expect**, and **how cooperation begins** — without inventing discount tiers, territory maps, partner counts, or marketing support inventories the operator has not attested.

Per forensic research Concept A (Channel Partnership Hub) with Partner Type Matrix slice from Concept C — adapted to **manufacturer partnership** posture, not Kroner-style «dealer-only channel» recruitment.

**Central charter constraint (from task brief):** This page answers **«почему выгодно и безопасно»** before it asks for an application. The qualification form is the **endpoint** of a trust-and-clarity journey — not the page identity.

### 1.2 What this page is NOT

| Anti-goal | Reason |
|-----------|--------|
| Dealer recruitment campaign / «станьте дилером сегодня» landing | Task brief forbids lead-gen landing aesthetics |
| Franchise / MLM partner program page | No franchise model attested; no tier pyramid visuals |
| Discount / margin marketing poster | OQ-D03 SAFE UNKNOWN — no public % tiers |
| Giant form above the fold | Form follows education — not hero |
| Factory tour duplicate | Production depth → `/about` |
| Logistics / TK directory | Owner: M9.14 Delivery |
| Invoice / VAT / bank chapter | Owner: M9.15 Payment |
| Warranty legal / RMA chapter | Owner: M9.17 Warranty |
| Custom engineering workflow | Owner: M9.18 Custom |
| Partner logo wall without assets | No attested partner logos in repo |
| Territory map without evidence | OQ-D05, OQ-D13 SAFE UNKNOWN |

### 1.3 What this page IS

A **manufacturer partnership clarity page**: scannable **partner-type segmentation** (SC-13), **OEM proof and direct-factory value** (BLOCK 02), **partner outcome table** (BLOCK 03), **5-step onboarding process** (SC-04), **production-to-partner supply chain summary** (BLOCK 05), honest **FAQ**, and a **qualification form** at the page endpoint — composing trust summaries from About, Payment, Delivery, and Warranty via links, not duplication.

---

## 2. Audience hierarchy

| Segment | Priority | What they need from design |
|---------|----------|----------------------------|
| **Дилер / дистрибьютор HoReCa** | **Primary** | OEM legitimacy, channel safety (not being undercut), predictable cooperation path |
| **Региональный поставщик / торговая компания** | **Primary** | Self-qualification via matrix, logistics reach, document pack for resale |
| **Оптовый снабженец** | **Primary** | Direct factory contact vs intermediary; order/document clarity |
| **Интегратор / проектный партнёр** | **Secondary** | Custom path pointer, specification support, project lane in matrix |
| **Корпоративный клиент (channel comparison)** | **Tertiary** | Pointer to direct purchase on Payment — helper text in BLOCK 01 |

**Design implication:** Layout rewards **self-qualification → manufacturer trust → outcome clarity → process predictability → escalate** — not discount hunting, not territory-map exploration, not form-first capture.

---

## 3. Conversion hierarchy

### 3.1 Primary

**Partnership qualification** — visitor submits **«Отправить заявку»** form (FORM) after understanding manufacturer partnership value, partner fit, and cooperation process.

Success signal: partner arrives at form **already trusting OEM legitimacy** and **understanding next steps** — form captures company profile for manager qualification, not cold lead spam.

**Parallel primary channel (not competing button):** Phone and email visible in BLOCK 07 — attested sales entry points per copy.

### 3.2 Secondary

**About depth** — «О компании и производстве» → `/about` when visitor needs factory narrative before applying (BLOCK 07).

### 3.3 Tertiary

**Contacts** — «Контакты» → `/contact/` for requisites, directions, or general inquiry (BLOCK 07).

**Catalog** — microcopy pointer to browse assortment before partnership discussion — subordinate text link only.

**Rule:** Form is **endpoint**, not hero. Tertiary links must not outrank primary form submit in the CTA zone — but **education blocks must visually dominate** everything above the CTA band.

---

## 4. Trust hierarchy

Ranked by **channel-partnership anxiety reduction** for dealer evaluation.

| Rank | Trust signal | Source | Design role |
|------|--------------|--------|-------------|
| **T1** | **Manufacturer legitimacy** — собственное производство, юрлицо-производитель, не посредник | BLOCK 02; OEM trust row | Dominant early proof — answers O1 |
| **T2** | **Direct factory relationship safety** — единый источник информации, документы, стабильный ассортимент | BLOCK 02 H3 stack | Reputation-risk reduction for partner |
| **T3** | **Partner outcomes** — what partner receives (КП, счета, docs, logistics support) | BLOCK 03 outcome table | Benefit clarity without fake discounts |
| **T4** | **Predictable cooperation process** — заявка → знакомство → формат → работа | BLOCK 04 | SC-04 timeline — reduces outcome opacity |
| **T5** | **Supply chain clarity** — завод → партнёр → конечный заказчик | BLOCK 05 chain diagram | Channel model visualization |
| **T6** | **Composed operational proof** — logistics, payment, warranty summaries + links | BLOCK 05 cross-link table | CP-01 composition from M9.13–M9.17 |
| **T7** | **Honest commercial boundaries** — «условия индивидуально», no public MOQ/% | BLOCK 03 helper; FAQ 2 | Prevents false promise distrust |
| **T8** | **Channel policy honesty** — direct + partner network; details individual | BLOCK 02 note | Answers O2 partially — OQ-D01 deferred |
| **T9** | **Entity facts** — ИНН, Барнаул, manufacturer name | OEM trust row | SC-03 variant — link to About |

**Explicitly subordinate (do not visual-promote without OQ unlock):**

- Discount % / margin tiers (OQ-D03)
- MOQ / minimum order badges (OQ-D04)
- Territory / exclusivity map (OQ-D05)
- Partner count claims («N дилеров по России»)
- Marketing support inventory icons (OQ-D09)
- Warranty term months badge (OQ-D12 / OQ-W01)
- SLA response chips (OQ-D08)
- Existing partner logos / case studies (OQ-D13, OQ-D14)

---

## 5. Page role in buyer journey

### 5.1 Journey position

```
PLP dealer block / M9.9 FAQ Q12 / Commercial Trust «Партнёрство»
        │
        ▼
   ┌─────────┐
   │  ABOUT  │  (recommended prior — OEM anchor)
   └────┬────┘
        │
        ▼
   ┌─────────┐
   │ DEALERS │  ◄── channel partnership clarity (this page)
   └────┬────┘
        │
   ┌────┴────────────────────────────────────┐
   │                                         │
   ▼                                         ▼
PAYMENT + DELIVERY + WARRANTY          Custom (project lane)
(transaction + logistics + service)    (integrator path)
        │
        ▼
   Contacts (fallback / requisites)
```

### 5.2 Before this page

| Prior state | Typical entry | Page must do |
|-------------|---------------|--------------|
| PLP `zpm-dealers` block + form | High intent — clicked «Подробнее» | Deliver **more depth than PLP** — not less action |
| Header «Дилерам» | Exploratory channel research | Establish manufacturer partnership in first screen |
| Payment bullet (dealer pointer) | Needs channel payment context | One-line satisfied — depth on Dealers |
| M9.9 Role E objections | Fear of direct sales conflict | Channel note in BLOCK 02 — honest, not map |
| About → Dealers | Factory trust established | Skip factory tour — go partnership economics |

### 5.3 After this page

| Exit | When |
|------|------|
| FORM submit | Qualified interest — ready for manager conversation |
| `/about` | Needs production / cert depth before applying |
| `/payment-methods` | Needs B2B settlement detail |
| `/delivery` | Needs logistics / shipment points |
| `/guarantee` | Needs warranty transfer to end client |
| `/custom-equipment` | Project / integrator non-standard path |
| `/contact/` | Requisites, directions, general inquiry |
| `/` catalog | Assortment evaluation before partnership |
| Phone / email | Prefers voice qualification |

**Program note:** Dealers is **design order #5** — composes SC-03, SC-04, SC-05, SC-12, SC-13 from About/Payment/Delivery/Warranty charters; must not redesign those patterns.

---

## 6. Relationship with sibling pages

CP-01 rule: **one primary owner per topic**. Dealers shows **one-line summary + text link** — never embedded foreign page body.

| Page | URL | Dealers relationship | Allowed on Dealers | Forbidden on Dealers |
|------|-----|---------------------|-------------------|---------------------|
| **About** | `/about` | BLOCK 02 pointer; OEM trust row; CTA secondary | Factory/production summary + link | Factory video, full cert promo, geo map, history |
| **Payment** | `/payment-methods` | BLOCK 03 body; BLOCK 04 step 5; BLOCK 05 table; FAQ 6 | B2B invoice path summary + link | Methods matrix, VAT %, bank requisites |
| **Delivery** | `/delivery` | Lead; BLOCK 05 table; FAQ 3, 7 | Two-point shipment summary + link | TK tables, regional freight, address conflict detail |
| **Warranty** | `/guarantee` | BLOCK 05 one-line | Manufacturer warranty summary + link | Term badge, RMA process, SLA |
| **Custom** | `/custom-equipment` | BLOCK 02 H3; BLOCK 05 table; FAQ 5 | Made-to-order summary + link | TZ checklist, parameter matrix, upload form |
| **Contacts** | `/contact/` | BLOCK 02 H3; FAQ 6; CTA tertiary | ИНН path + link | Full contact card grid, map embed |
| **Certification** | `/our-certification` | MICRO pointer | Cert type labels + link | PDF wall, full slider duplicate |

**PLP dealer form ownership (charter lock — program blocker B3 / OQ-D15):**

| Decision | Detail |
|----------|--------|
| **Primary intake** | **`/dealers` corp page FORM** — per CP-08 and copy v1.1 |
| **PLP `blockdealersform` (`dialog=7`)** | **Secondary surface** — must slim to compact CTA + «Подробнее» → `/dealers` once corp page ships |
| **Reconciliation rule** | One qualification field set — corp form is canonical; PLP must not host richer or conflicting form |
| **Forensic gap** | Live corp page has **no form**; PLP has form — inverted ownership; implementation must fix |
| **Field parity** | Corp form: name, company, city, phone, email, comment — no website field (removed v1.1) |

**МО warehouse address (program blocker B1):**

| Decision | Detail |
|----------|--------|
| **Conflict** | Copy uses Никольское 204 (M9.14 alignment) vs research Басовская 14с2 |
| **Charter default** | Design uses **copy v1.1 prose** («склад партнёра в Московской области») — no street in BLOCK 05 unless operator locks |
| **Propagation** | Single canonical address from M9.14 charter before implementation |

**Contacts alignment:** FORM extends SC-10 with **company** (required), **city** (required), **comment** (optional qualification context); consent, phone mask, success microcopy match delivered Contacts discipline.

---

## 7. Evidence hierarchy

### Level 1 — Must be visible without deep scroll (first ~2 viewports)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| Manufacturer partnership framing | H1 + Lead | SC-01 internal-page rhythm — align Contacts shell |
| **OEM / direct factory positioning** | Lead + BLOCK 02 intro | Answers primary question — typographic clarity |
| **Partner self-qualification start** | BLOCK 01 matrix (visible rows) | SC-13 — «подхожу ли я» scan |
| Optional trust strip | MICROCOPY trust strip | 4 micro-labels — subordinate to H1+lead |
| OEM trust row | MICROCOPY OEM row | SC-03 variant — manufacturer + ИНН + About link |

### Level 2 — Core proof stack (mid-page, scroll expected)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| Why direct from manufacturer (5 H3) | BLOCK 02 | Structured proof stack — **peak OEM argument density** |
| Partner outcomes table (6 rows) | BLOCK 03 | Outcome table — benefit clarity without % |
| Onboarding process (5 steps) | BLOCK 04 | SC-04 timeline — cooperation predictability |
| Supply chain diagram | BLOCK 05 | Simple vertical chain — not logistics map |
| Cross-page summary table | BLOCK 05 | 3-row link table — Delivery, Custom, Payment |
| Channel interaction note | BLOCK 02 microcopy | Honest channel policy — prose only |

### Level 3 — Supporting context (lower visual weight)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| BLOCK 01 matrix body + helper | BLOCK 01 | Direct-buyer redirect to Payment |
| BLOCK 03 helper (no public price list) | BLOCK 03 | Commercial honesty microcopy |
| BLOCK 04 outcome note + helper | BLOCK 04 | SLA deferred — office hours only |
| FAQ (8) | BLOCK 06 | SC-08 accordion — objection cleanup |
| Warranty pointer | BLOCK 05 one-line | Link only — no term badge |
| «Сделано в России» badge | MICRO optional | Labeled + link — not ПП №719 substitute |

---

## 8. Visual narrative

Narrative arc is **manufacturer partnership evaluation**, not recruitment urgency.

### Beginning — «С кем я связываю репутацию?» (Utility → BLOCK 01–02)

| Beat | Content | Emphasis |
|------|---------|----------|
| Orient | Breadcrumb, H1, lead | Direct factory + Russia supply — not «join program» |
| Trust scan | Optional trust strip + OEM trust row | Manufacturer micro-facts — SC-03 |
| Fit | BLOCK 01 partner matrix | **Self-qualification** — who this is for |
| **OEM proof** | BLOCK 02 why direct | **Peak trust argument** — production, docs, assortment |

**Beginning must answer: «Это производитель? Безопасно ли работать напрямую?» in <15 seconds of scan.**

### Middle — «Что я получу и как это устроено?» (BLOCK 03 → BLOCK 05)

| Beat | Content | Emphasis |
|------|---------|----------|
| Outcomes | BLOCK 03 partner benefits table | Concrete partner results — not discount tiers |
| Process | BLOCK 04 onboarding timeline | SC-04 — predictable path to cooperation |
| Chain | BLOCK 05 supply diagram + cross-links | Factory → partner → end client; composed proof links |

**Middle must answer IA Q3, Q6, Q8 (partner types, application path, payment/delivery/warranty pointers) without duplicating sibling pages.**

### End — «Обсудить сотрудничество» (BLOCK 06 → FORM)

| Beat | Content | Emphasis |
|------|---------|----------|
| Objections | BLOCK 06 FAQ | MOQ, territory, docs, custom — SAFE UNKNOWN handling |
| Action | BLOCK 07 CTA + FORM | **Qualification endpoint** — form follows education |

**End must make «Обсудить сотрудничество» feel like **informed escalation**, not «заполните форму за 30 секунд».**

---

## 9. Block importance map

Ranking for **all approved v1.1 copy blocks** (Critical / Important / Supporting).

| Block | Title | Rank | Rationale |
|-------|-------|------|-----------|
| Utility | Meta, breadcrumb | Supporting | Required shell — no visual competition |
| — | H1 + Lead | **Critical** | Manufacturer partnership frame |
| **01** | Кому подойдёт сотрудничество | **Critical** | SC-13 partner matrix — self-qualification |
| **02** | Почему партнёры работают напрямую с производителем | **Critical** | OEM proof + channel safety — page identity |
| **03** | Что получает партнёр | **Critical** | Outcome table — benefit clarity |
| **04** | Как начинается сотрудничество | **Critical** | SC-04 process — predictability |
| **05** | Как связаны дилеры, производство и логистика | Important | Supply chain + composed cross-links |
| **06** | FAQ | Important | Objection resolver — pre-CTA |
| **07** | CTA | **Critical** | Conversion band |
| FORM | Заявка на сотрудничество | **Critical** | Qualification instrument — endpoint only |
| MICRO | Trust strip | Important | Optional — accelerates OEM scan |
| MICRO | OEM trust row | Important | SC-03 — compact entity proof |

---

## 10. Visual emphasis strategy

### 10.1 What MUST dominate visually

| Element | Why |
|---------|-----|
| BLOCK 02 OEM / direct-manufacturer H3 stack | Answers primary question — partnership safety |
| BLOCK 01 SC-13 partner matrix | Self-qualification — reduces wrong leads |
| BLOCK 03 outcome table | Tangible partner value without fake commercial tiers |
| BLOCK 04 SC-04 onboarding process | Predictable cooperation path |
| BLOCK 02 channel note (direct + partner) | Top dealer fear — channel conflict |
| OEM trust row (ИНН, manufacturer, About link) | Fast OEM verification |

### 10.2 What must NOT dominate visually

| Element | Why |
|---------|-----|
| FORM above the fold / form-as-hero | Anti-goal — recruitment landing forbidden |
| Discount badges / % tiers | OQ-D03 SAFE UNKNOWN |
| Partner logo wall | No attested assets |
| Territory / dealer map | OQ-D05, OQ-D13 — no evidence |
| «Станьте дилером сегодня» urgency banners | Franchise recruitment anti-pattern |
| Giant CTA button before BLOCK 04 | Form is endpoint — not opening |
| BLOCK 06 FAQ as primary content | Accordion is cleanup, not hero |
| Marketing support icon grid | OQ-D09 — not in copy |
| BLOCK 05 as logistics map | Summary + links only — Delivery owns depth |
| Partner count statistics | Forbidden — no attested data |

### 10.3 Visual weight budget (relative 1–5)

| Block | Tier | Weight | Notes |
|-------|------|--------|-------|
| **02** | Tier 1 — Anchor | **5** | Strongest OEM / safety argument block |
| **01** | Tier 1 — Anchor | **4** | Partner matrix — segmentation clarity |
| **03** | Tier 1 — Anchor | **4** | Outcome table — partner value |
| **04** | Tier 1 — Anchor | **4** | SC-04 process — fifth corp instantiation |
| **07 + FORM** | Tier 1 — Anchor | **3** | CTA + form — **deliberately below education blocks** |
| **05** | Tier 2 — Support | **3** | Chain diagram + link table — composition |
| **06** | Tier 2 — Support | **3** | 8-item accordion |
| Trust strip | Tier 2 — Support | **2** | 4 micro-labels — optional |
| OEM trust row | Tier 2 — Support | **2** | SC-03 — after lead or end of BLOCK 02 |
| Lead | Tier 1 | **3** | Sets frame — shorter than BLOCK 02 |
| H1 | Tier 1 | **3** | Clear — not slogan-styled recruitment headline |

**Section rhythm:** Education blocks (01–05) carry **higher visual weight than form zone**. FORM tier is Critical for presence but **weight 3/5** — not 5/5. Prevents lead-gen landing read.

---

## 11. Dealer visualization philosophy

### 11.1 Charter decision — choose ONE

| Approach | Verdict |
|----------|---------|
| A) Benefits-first | **REJECTED as dominant** — benefits without OEM proof reads as recruitment marketing |
| B) Partnership program | **REJECTED as dominant** — implies franchise/MLM program aesthetics |
| **C) Manufacturer partnership** | **SELECTED — dominant** |

### 11.2 Why Manufacturer partnership (C)

| Reason | Detail |
|--------|--------|
| Task brief | Page must feel like **manufacturer partnership** — not dealer recruitment campaign |
| Primary question | «Почему выгодно и безопасно» requires **OEM legitimacy first**, commercial benefits second |
| Copy spine | BLOCK 02 is longest proof block — factory, docs, assortment, custom path |
| ZPM model | Factory sells direct **and** through partners (copy) — not Kroner dealer-only channel |
| Forensic recommendation | Concept A (Channel Partnership Hub) with matrix slice — OEM aggregation + links |
| Program position | Design order #5 — **composition page** composing About/Payment/Delivery/Warranty summaries |
| Anti-patterns | Benefits-first (A) without proof → generic promises; Partnership program (B) → franchise landing |

### 11.3 Supporting roles (non-dominant)

| Approach | Role on page |
|----------|--------------|
| Benefits-first (A) | BLOCK 03 outcome table — **supporting** — concrete outcomes after OEM proof |
| Partnership program (B) | BLOCK 01 matrix + BLOCK 04 process — **structural** — segmentation and onboarding, not «program tiers» visuals |

**Forbidden as visual spine:** Discount tier pyramid, franchise steps, partner count hero, recruitment urgency, form-first layout.

---

## 12. Commercial philosophy

### 12.1 Dominance order (locked)

| Order | Element | Page blocks | Design role |
|-------|---------|-------------|-------------|
| **1** | **Proof** | BLOCK 02, OEM trust row, BLOCK 05 links | Manufacturer legitimacy + composed operational proof |
| **2** | **Benefits** | BLOCK 03 outcome table | What partner receives — bounded, no % |
| **3** | **Process** | BLOCK 04 SC-04, BLOCK 05 chain | How cooperation starts and flows |
| **4** | **Form** | BLOCK 07 + FORM | Qualification endpoint — after 1–3 |

**Rule:** Visual hierarchy must follow **proof → benefits → process → form**. Never invert to **form → benefits → proof** (lead-gen pattern).

### 12.2 What commercial elements are explicitly subordinate

| Element | Treatment |
|---------|-----------|
| Discounts / margin | **Absent from visuals** — FAQ 2 + helper prose only |
| MOQ | FAQ honest answer — no badge |
| Territory / exclusivity | FAQ 3 — prose; no map |
| Price list / line card | «После заявки» — BLOCK 03 helper |
| Marketing support | **Not in copy** — no icon grid |
| Deferral / partner payment | Link to Payment — one line |

---

## 13. Qualification strategy

### 13.1 Role of the qualification form

| Dimension | Decision |
|-----------|----------|
| **Purpose** | Manager qualification — company profile, region, work direction — not instant dealer signup |
| **Position** | **Page endpoint** — after BLOCK 01–06 education |
| **Visual identity** | SC-10 extension — same discipline as Payment/About forms — not standalone «application portal» |
| **Title framing** | «Заявка на сотрудничество» — cooperation discussion, not «Регистрация дилера» |
| **Submit label** | «Отправить заявку» — not «Стать дилером» |
| **CTA H2** | «Получить условия сотрудничества» — conditions follow conversation, not form auto-grant |

### 13.2 Form must NOT dominate

| Rule | Detail |
|------|--------|
| Above-fold form | **FORBIDDEN** |
| Form in hero | **FORBIDDEN** |
| Form column beside matrix | **FORBIDDEN** — recruitment landing pattern |
| Sticky form sidebar | **FORBIDDEN** |
| Mid-page «Отправить заявку» buttons | **FORBIDDEN** — one primary button zone (BLOCK 07) |
| PLP duplicate as primary | **FORBIDDEN** after corp page ships — OQ-D15 lock |

### 13.3 Field strategy

| Field | Role |
|-------|------|
| company (required) | B2B identity — emphasized visually |
| city (required) | Regional qualification — supports territory discussion without map |
| comment (optional) | Partner type self-identification — placeholder guides (дилер, опт, проект) |
| name, phone, email | Standard SC-10 — Contacts parity |
| website | **Excluded** per copy v1.1 |
| ИНН | **Not in copy** — Kroner benchmark deferred; manager collects at qualification |

### 13.4 Post-submit expectation

Success message sets **manager callback in office hours** — not «вы приняты в программу». No instant dealer status UI.

---

## 14. Partner-type strategy

### 14.1 Role of partner matrix (BLOCK 01)

| Dimension | Decision |
|-----------|----------|
| **Purpose** | Self-qualification — «это про меня?» — reduces wrong-audience applications |
| **Component** | SC-13 — 5 partner types in responsive grid |
| **Visual weight** | Tier 1 (4/5) — **important but subordinate to BLOCK 02 OEM proof (5/5)** |
| **Placement** | Early page — immediately after lead — before deep OEM chapter |
| **Format** | Table → stacked cards ≤1024px; icon + title + 2-line description per copy columns |
| **Tags** | MICRO partner type labels (dealer, wholesale, project, integrator, trading) |

### 14.2 Should partner matrix dominate?

| Decision | **Important — not page-wide dominant** |
|----------|----------------------------------------|
| Rationale | Matrix answers **who** — BLOCK 02 answers **why manufacturer** (primary question) |
| Order | Matrix **before** BLOCK 02 in copy — design may give BLOCK 02 slightly higher visual weight |
| Overlap | FAQ 1 echoes matrix — accordion short answer, not duplicate table |

### 14.3 Matrix vs commercial tiers

| Rule | Detail |
|------|--------|
| No per-type discount columns | OQ-D02 unresolved — single application path |
| No territory column | Would imply published policy |
| Helper text | Direct buyers → Payment — audience redirect |

---

## 15. CTA strategy

### 15.1 Hierarchy (locked per copy v1.1)

| Priority | Element | Placement |
|----------|---------|-----------|
| **Primary** | «Обсудить сотрудничество» → scroll/submit to FORM | BLOCK 07 + FORM only |
| **Secondary** | «О компании и производстве» → `/about` | BLOCK 07 — subordinate |
| **Tertiary** | «Контакты» → `/contact/` | BLOCK 07 link |
| **Support** | Phone `8 (3852) 72-18-90` · `info@bzpm.ru` | BLOCK 07 inline |
| **Micro** | Catalog, Payment pointers | Text links under CTA body |

### 15.2 One CTA or multiple?

| Decision | **One primary button zone per page** |
|----------|--------------------------------------|
| Mid-page buttons | **FORBIDDEN** — no «Обсудить сотрудничество» before BLOCK 07 |
| Text links | Permitted in BLOCK 02–05, FAQ — not button-styled |
| Phone as parallel CTA | Visible in BLOCK 07 — support, not competing primary button |
| PLP form CTA | Secondary surface — routes to corp page for depth |

### 15.3 Placement philosophy

CTA band **after FAQ** — user has consumed matrix, OEM proof, outcomes, process, supply chain summary, and residual objections.

Primary button label emphasizes **discussion of cooperation** — not instant enrollment.

FORM immediately follows CTA band (or integrated in same visual zone per SC-09).

---

## 16. FAQ strategy

### 16.1 Role

FAQ is **objection resolver** for channel edge cases — not primary education (BLOCK 01–05 own that).

### 16.2 Parameters

| Parameter | Decision |
|-----------|----------|
| Count | **8 items** — per approved copy; do not expand |
| Pattern | SC-08 single-open accordion |
| Position | After BLOCK 05, before BLOCK 07 |
| Visual weight | Important — **subordinate** to BLOCK 02 and BLOCK 04 |

### 16.3 Priority items (mobile density)

| Priority | FAQ | Why |
|----------|-----|-----|
| 1 | Кто может стать партнёром? | Core Q3 — pointer to BLOCK 01 |
| 2 | Минимальные объёмы? | Core Q4 — commercial honesty |
| 3 | По всей России? | Core Q5 + Delivery link |
| 4 | Проект клиента? | Integrator lane |
| 5 | Как начать? | Core Q6 — process pointer |
| 6–8 | Remaining | Custom, docs, availability |

### 16.4 Overlap discipline

FAQ must **not repeat** full BLOCK 01 matrix, BLOCK 03 table, or BLOCK 04 timeline — short confirmatory answers with links to owners (Payment, Delivery, Custom, Contacts).

### 16.5 Forbidden FAQ patterns

- Accordion headers with discount % chips
- «Эксклюзивная территория» promises in headers
- Embedded partner map in answers
- «Станьте дилером» CTA inside accordion panels

---

## 17. Design risks

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R1 | **Form-as-hero** — page reads as lead-gen landing | **Critical** | §13 — form weight 3/5; education blocks dominate |
| R2 | **PLP/corp form split** — inverted ownership (live forensic G-DE01) | **Critical** | OQ-D15 lock — corp primary; PLP slim after ship |
| R3 | **Commercial void** — page feels thin without logos/discounts | **High** | Proof + outcome + process compensate; no fake social proof |
| R4 | **Franchise / MLM aesthetic drift** | **High** | Forbidden patterns §18; manufacturer partnership mode |
| R5 | **Discount badge temptation** | **High** | OQ-D03 — no % visuals |
| R6 | **Trust strip bloat** — 4+ composed facts + OEM row + BLOCK 05 table | **Medium** | Max one compact strip + OEM row; BLOCK 05 table is 3 links |
| R7 | **BLOCK 01 vs FAQ 1 overlap** | **Low** | FAQ points to matrix — no duplicate |
| R8 | **About duplication** in BLOCK 02 | **Medium** | BLOCK 02 = channel economics; About = factory story — one-line pointer |
| R9 | **МО address conflict** propagates from Delivery | **High** | Program blocker B1 — prose only until lock |
| R10 | **Partner matrix vs benefits table redundancy** | **Medium** | Matrix = who; BLOCK 03 = what you get — distinct semantics |
| R11 | **Generic `.zpm-seo` scaffold** (live page) | **High** | New corp block system — dedicated namespace at implementation |
| R12 | **Channel policy gap** (OQ-D01) | **High** | BLOCK 02 note — honest individual discussion; no fake policy map |
| R13 | **Warranty term badge temptation** on BLOCK 05 pointer | **Medium** | Link only — OQ-D12 / OQ-W01 |
| R14 | **Kroner benchmark pressure** (ИНН in form, dealer list) | **Medium** | Copy chose manager-led qualification — charter respects |
| R15 | **Long page without hierarchy** — 7 blocks + form | **Medium** | Tier weight map; section spacing |

---

## 18. Forbidden patterns

| Pattern | Why forbidden |
|---------|---------------|
| **Franchise style** — tier badges, «уровни партнёра», gold/silver/platinum | No franchise model attested |
| **MLM aesthetics** — pyramid diagrams, downline language, recruitment trees | Anti-goal — manufacturer partnership |
| **Giant discount badges** — «до −30%», «выгодные условия» hero | OQ-D03 SAFE UNKNOWN |
| **Fake exclusivity** — «эксклюзивный дилер региона» without OQ-D05 | Misleading territory promise |
| **Partner count claims** — «более N партнёров», statistics wall | OQ-D13 — no attested data |
| **Dealer map without evidence** — Russia heatmap, occupied territories | OQ-D05, OQ-D13 |
| **Logo walls without assets** — fake partner carousel | No operator logos in repo |
| **«Become dealer today» landing style** — urgency banners, countdown, hero form | Task brief explicit anti-goal |
| **Lead generation page** — form above fold, single-column squeeze | Form is endpoint |
| **Dealer recruitment campaign** — stock handshakes, «присоединяйтесь к сети» | Manufacturer partnership mode |
| **Marketing support icon grid** without inventory | OQ-D09 — not in copy |
| **Published MOQ / price list badges** | OQ-D03, OQ-D04 |
| **Warranty term chip** on summary strip | Owner: M9.17 — OQ-W01 |
| **Full factory video/story** | Owner: About |
| **TK / freight tables** | Owner: Delivery |
| **Bank / VAT panel** | Owner: Payment / Contacts |
| **Cert PDF gallery** | Owner: `/our-certification` |
| **SKU grid / catalog cards** | Owner: Catalog |
| **Multiple primary CTA buttons mid-page** | §15.2 |
| **ПП №719 / unlabeled «Сделано в России»** as channel guarantee | Labeled fact + link only |
| **Duplicate PLP dealer form** as co-primary without reconciliation | OQ-D15 |
| **Case study gallery** without operator assets | OQ-D14 |
| **Competitor comparison table** | OQ-D18 — not in copy |

---

## 19. Success criteria

Operator judges Dealers design **successful** when:

| # | Criterion | Verification method |
|---|-----------|---------------------|
| S1 | Visitor answers primary question: **почему выгодно и безопасно работать с производителем ЗПМ** | Operator scenario test — dealer persona |
| S2 | Page does **not** read as franchise recruitment, MLM, or lead-gen landing | Operator visual compare vs Kroner/Klen patterns |
| S3 | BLOCK 02 OEM proof scannable in **<20 seconds** desktop | Operator scan test |
| S4 | Partner self-qualifies via BLOCK 01 matrix before reaching form | User flow review |
| S5 | Form is **endpoint** — education blocks visually dominate form zone | Weight budget audit §10.3 |
| S6 | No numeric commercial claims (%, MOQ, territory) without OQ unlock | Governance check |
| S7 | No CP-01 violations — sibling topics are links/summaries only | Cross-link audit |
| S8 | FORM fields match copy v1.1 (no website); consent matches Contacts | Side-by-side with `/contact/` |
| S9 | PLP reconciliation documented — corp form primary | OQ-D15 implementation check |
| S10 | IA Q1–Q8 addressed via copy blocks + links | Copy coverage audit |
| S11 | SC-04 / SC-08 / SC-10 / SC-13 instantiated per program registry | Design program check |
| S12 | One primary CTA button zone — no mid-page submit | Design review |
| S13 | Mobile ≤1024px — matrix and outcome table stack without horizontal scroll trap | Responsive check |
| S14 | No fake partner logos, maps, or count claims | Asset honesty check |
| S15 | Design charter approved **before** wireframe/mockup work | Phase gate |

---

## 20. Special requirement resolutions

### 20.1 Should discounts dominate?

| Decision | **NO — explicitly forbidden** |
|----------|-------------------------------|
| Rationale | OQ-D03 SAFE UNKNOWN; discount-led page = recruitment campaign anti-pattern |
| Treatment | «Условия обсуждаются индивидуально» — prose in BLOCK 03 helper, FAQ 2 |

### 20.2 Should form dominate?

| Decision | **NO** |
|----------|--------|
| Rationale | Task brief: NOT «заполните форму»; form is qualification endpoint |
| Treatment | FORM visual weight 3/5; blocks 01–04 at 4–5/5 |

### 20.3 Should partner matrix dominate?

| Decision | **Important — not dominant over OEM proof** |
|----------|---------------------------------------------|
| Treatment | BLOCK 01 at 4/5; BLOCK 02 at 5/5 — matrix supports, OEM proof leads |

### 20.4 Should OEM proof dominate?

| Decision | **YES — primary visual anchor within proof layer** |
|----------|-----------------------------------------------------|
| Treatment | BLOCK 02 + OEM trust row carry strongest weight; answers manufacturer safety |

### 20.5 Should dealer process dominate?

| Decision | **Important — subordinate to proof, parallel to benefits** |
|----------|----------------------------------------------------------|
| Treatment | BLOCK 04 at 4/5 — process is commercial philosophy #3, not #1 |
| Shared pattern | SC-04 — fifth corp instantiation; equal step weight, no SLA chips |

### 20.6 Trust strip placement

| Element | Placement decision |
|---------|-------------------|
| Trust strip (4 badges) | **Optional** — after lead, before BLOCK 01 |
| OEM trust row (4 labels) | **Recommended** — after BLOCK 02 or end of lead zone |
| Both together | **Avoid badge fatigue** — if trust strip used, OEM row integrates into BLOCK 02 footer |

### 20.7 BLOCK 05 supply chain diagram

| Parameter | Decision |
|-----------|----------|
| Format | Simple **vertical 4-node chain** — text + optional minimal icon |
| Not a map | **FORBIDDEN** — logistics map aesthetic |
| Cross-link table | 3 rows — text links — subordinate to chain |
| Warranty line | One-line pointer — no term badge |

### 20.8 Shared components instantiated on Dealers

| ID | Component | Dealers blocks |
|----|-----------|----------------|
| SC-01 | Corp page shell | All |
| SC-03 | Trust row | OEM trust row (MICRO); optional trust strip |
| SC-04 | Process timeline | BLOCK 04 |
| SC-05 | Proof / fact cards | BLOCK 05 chain variant (composition, not shipment cards) |
| SC-07 | Matrix table | BLOCK 01 partner matrix; BLOCK 03 outcome table |
| SC-08 | FAQ accordion | BLOCK 06 |
| SC-09 | CTA band | BLOCK 07 |
| SC-10 | Corp inquiry form | FORM (+company, +city variant) |
| SC-12 | Cross-link inline | BLOCK 02–05, CTA pointers |
| SC-13 | Partner / segment matrix | BLOCK 01 |

**Dealers is composition consumer** — reuses SC-04 from Payment charter; does not own new shared patterns except partner-matrix + supply-chain diagram semantics.

---

## 21. Open questions (operator lock)

| ID | Question | Impact | Default if unresolved |
|----|----------|--------|----------------------|
| OQ-DC-DE01 | Channel policy: direct vs dealer protection (OQ-D01) | BLOCK 02 note depth | **Copy v1.1** — individual discussion prose |
| OQ-DC-DE02 | PLP form suppress vs slim (OQ-D15) | Catalog + corp intake | **Corp primary**; PLP link + optional minimal capture |
| OQ-DC-DE03 | Canonical МО warehouse address (B1) | BLOCK 05 prose | **Region only** — no street until M9.14 lock |
| OQ-DC-DE04 | Trust strip after lead — include? | First screen density | **Include** 4 micro-labels OR omit if OEM row sufficient |
| OQ-DC-DE05 | OEM trust row placement — after lead vs after BLOCK 02? | Scan order | **After BLOCK 02** — proof follows argument |
| OQ-DC-DE06 | Add ИНН field to form (Kroner benchmark)? | FORM | **Exclude** — not in copy v1.1 |
| OQ-DC-DE07 | Partner logos / case studies (OQ-D13, D14) | Social proof block | **Exclude** — no assets |
| OQ-DC-DE08 | Territory map ever publishable? | Visual commitment | **Exclude** — prose only |
| OQ-DC-DE09 | Marketing support section if OQ-D09 resolved? | New block | **Defer** — requires copy amendment + charter v2 |
| OQ-DC-DE10 | Dedicated dealer email (OQ-D16) | CTA routing | **info@bzpm.ru** per copy |
| OQ-DC-DE11 | Legacy `.zpm-seo` dealers page — new `zpm-dealers-*` namespace? | Implementation | Defer to implementation charter |
| OQ-DC-DE12 | Privacy policy route `/privacy-policy` | Form consent | Verify at implementation — assumed per copy |
| OQ-DC-DE13 | СНГ in geography (OQ-D17) — live legacy mentions СНГ | Copy alignment | **Russia only** per copy v1.1 — do not reintroduce СНГ |

---

## 22. Design readiness verdict

| Dimension | Status | Notes |
|-----------|--------|-------|
| Copy | **READY** | v1.1 complete — operator approval header pending |
| IA | **READY** | CP-01 boundaries locked; Dealers = channel program owner |
| Charter | **READY FOR OPERATOR REVIEW** | This document |
| Assets | **BLOCKED** | No partner logos, territory map, marketing kit — structural design only |
| OQ | **PARTIAL** | OQ-D01, D03, D05, D15 affect visuals — explicit deferrals |
| Upstream charters | **READY** | About, Payment, Delivery, Warranty charters exist — composition unlocked |
| Visual design | **NOT READY** | Awaits operator charter approval |
| Implementation | **NOT READY** | Awaits design approval + OQ-D15 + B1 address lock |

**Verdict:** M9.16 Dealers is **PARTIAL DESIGN READY** — charter pass complete; operator may approve charter and authorize **visual design phase** with **manufacturer-partnership** posture, **proof → benefits → process → form** commercial order, partner matrix and OEM proof dominant over form, and explicit SAFE UNKNOWN deferrals (no discounts, no map, no logos, no partner counts).

**Program alignment:** Resolves design order #5; composes trust summaries from M9.13–M9.17; documents PLP form reconciliation (B3).

**Explicit stop:** No wireframes · no mockups · no Twig/CSS/JS · no deploy.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-22 | **CREATED** — Design Charter v1; manufacturer-partnership visualization; proof→benefits→process→form commercial order; qualification/form subordination; partner matrix strategy; PLP reconciliation lock; forbidden recruitment/franchise patterns; special question resolutions |

---

*BZPM M9.16 Dealers Design Charter v1 — documentation only. No design, wireframes, mockups, or implementation authorized.*
