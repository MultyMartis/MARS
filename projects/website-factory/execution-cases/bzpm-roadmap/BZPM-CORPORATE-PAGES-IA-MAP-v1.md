# BZPM Corporate Pages — IA Map v1

**Program:** BZPM Corporate Pages Program  
**Site:** SITE-002 (ЗПМ / BZPM) · TEST `https://zpm.new-site.space/`  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Policy:** MANUAL UI REFINEMENTS ARE CANONICAL  
**Date:** 2026-06-22  
**Status:** **IA / ARCHITECTURE PHASE — ACTIVE**

**Boundary:** Information architecture and ownership map only. This document does **not** authorize design, wireframes, mockups, implementation, deploy, TEST writes, or production changes.

**Parent program:** [BZPM-CORPORATE-PAGES-PROGRAM-v1.md](BZPM-CORPORATE-PAGES-PROGRAM-v1.md)  
**Research artifacts:** `projects/ocpilot/sites/site-002/reports/BZPM-M9.13` … `M9.18` forensic reports  
**Copy artifacts:** `projects/ocpilot/sites/site-002/copy/BZPM-M9.13` … `M9.18` PAGE-COPY files · [BZPM-COPY-STANDARDS-v1.md](BZPM-COPY-STANDARDS-v1.md)  
**Blueprint reference:** [BZPM-BLUEPRINT-v1.md](../bzpm-catalog-redesign/BZPM-BLUEPRINT-v1.md) — CP-01 single-owner rule

---

## Program phase

| Phase | Status | Evidence |
|-------|--------|----------|
| **Research** | **COMPLETE** | M9.13–M9.18 forensic reports registered 2026-06-22 |
| **IA / Architecture** | **READY** (this document) | Unified ownership map · cross-link rules · relationship structure |
| **Copy system** | **CLOSED** | M9.13–M9.18 PAGE-COPY substantively complete — operator sign-off pending (B8) — [BZPM-COPY-STANDARDS-v1.md](BZPM-COPY-STANDARDS-v1.md) |
| **Design Charter** | **DRAFT COMPLETE / APPROVAL OPEN** | Six charters v1 in [charters/](charters/) — all **PENDING OPERATOR APPROVAL** — [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md) |
| **Design Brief** | **DRAFT COMPLETE** | Six briefs v1 in [charters/](charters/) |
| **Design (visual)** | **NOT OPEN** | Requires operator-approved Design Charter per page |
| **Implementation** | **NOT READY** | Requires design charter + implementation charter per page |

**Contacts:** Delivered outside program — included in IA map for cross-link discipline only.

---

## Canonical URL registry

| ID | Page | URL (TEST) | Nav label |
|----|------|------------|-----------|
| **M9.13** | About Company | `/about` | О компании |
| **M9.14** | Delivery | `/delivery` | Доставка |
| **M9.15** | Payment | `/payment-methods` | Оплата |
| **M9.16** | Dealers | `/dealers` | Дилерам |
| **M9.17** | Warranty | `/guarantee` | Гарантия |
| **M9.18** | Custom Manufacturing | `/custom-equipment` | Оборудование на заказ |
| **—** | Contacts | `/contact/` | Контакты |

**URL notes (research-confirmed):**

- `/payment`, `/payment/` → **404** — canonical is `/payment-methods`
- `/garantiya`, `/warranty` → **not routed** — canonical is `/guarantee`
- `/izgotovlenie-pod-zakaz`, `/custom-manufacturing` → **404** — canonical is `/custom-equipment`

---

## Per-page IA

### M9.13 — About Company (`/about`)

#### Purpose

Primary owner of **entity narrative**: who ЗПМ is, factory identity, production footprint, OEM trust, geography of manufacturing. Anchors «кто вы?» objections from catalog and Commercial Trust surfaces.

#### Audience

- Owner / владелец бизнеса — trust before first deal
- Снабженец / закупщик — vendor legitimacy check
- Проектировщик — production capability and geography
- Дилер (secondary) — factory vs intermediary proof before channel terms

#### Primary Questions

| # | Question |
|---|----------|
| Q1 | Кто вы? Производитель или перекуп? |
| Q2 | Где находится производство и география поставок? |
| Q3 | Можно ли доверять заводу как OEM? |
| Q4 | Есть ли сертификация / соответствие / «Сделано в России»? |
| Q5 | Какова масштабность и специализация производства? |

#### Allowed Topics

- Company history and mission (bounded)
- Factory / workshop narrative
- Production geography and footprint (geo promo)
- Certificate / conformity promo (summary — not full doc dump)
- Video / media hero demonstrating production
- OEM proof strip linking to catalog trust assets
- High-level «why buy from manufacturer» — not SKU comparison

#### Forbidden Topics

| Topic | Primary owner |
|-------|---------------|
| Shipping regions, TK, lead times, freight | M9.14 Delivery |
| Payment methods, invoice, VAT, bank requisites | M9.15 Payment |
| Dealer discounts, territory, channel policy | M9.16 Dealers |
| Warranty term, RMA, service SLA | M9.17 Warranty |
| Custom process, TZ intake, engineering workflow | M9.18 Custom |
| Phone, email, address, legal requisites detail | Contacts |
| SKU specs, prices, availability | Catalog / PDP |

#### Cross-links

**Inbound:** Header · footer · mobile menu · Commercial Trust FAQ «кто вы» · homepage advantages (thematic — avoid duplicate depth) · M9.9 persona objections

**Outbound:** `/delivery` (shipping from factory) · `/guarantee` (service commitment summary) · `/custom-equipment` (production capability extension) · `/dealers` (channel vs direct) · `/contact/` · `/our-certification` (if conformity depth needed) · catalog hub

#### Evidence Assets

| Asset | Use on About |
|-------|--------------|
| Factory / workshop photos or video | Hero / main blocks |
| Geography map or production footprint image | Geo promo block |
| Certificate types (labeled, not full PDF wall) | Cert promo — link to PLP slider or `/our-certification` |
| «Сделано в России» badge fact | One labeled trust row — not ПП №719 legal substitute |
| Client / project logos | Only if operator provides |
| ATLAS entity facts (ИНН, legal name) | Summary only — full requisites on Contacts |

**Research:** [BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md)

---

### M9.14 — Delivery (`/delivery`)

#### Purpose

Primary owner of **logistics and shipping terms**: regions served, carriers, pickup points, freight model, shipment timing relative to order readiness. Answers «как и когда привезёте?»

#### Audience

- Снабженец / логист — regional delivery feasibility
- Закупщик — shipment documentation and timing
- Дилер — supply into partner region
- Owner — opening timeline and delivery to site

#### Primary Questions

| # | Question |
|---|----------|
| Q1 | Доставляете ли в мой регион? |
| Q2 | Какие способы доставки (ТК, самовывоз, заводская доставка)? |
| Q3 | Откуда отгружается (Барнаул, Москва)? |
| Q4 | Сроки доставки и зависимость от производства? |
| Q5 | Как оформляется отгрузка после оплаты? |
| Q6 | Крупногабарит / нестандарт — особые условия? |

#### Allowed Topics

- Regional coverage map or list
- Carrier / TK partnerships (named if attested)
- Warehouse / shipment points (Барнаул, Москва Басовская)
- Pickup instructions
- Delivery cost model (framework — not per-SKU calculator)
- Shipment after payment / production ready — **summary** with link to Payment
- Oversized / custom shipment notes — **summary** with link to Custom
- RMA return logistics — **summary** with link to Warranty

#### Forbidden Topics

| Topic | Primary owner |
|-------|---------------|
| Factory narrative, OEM identity | M9.13 About |
| Invoice, VAT, prepayment, bank details | M9.15 Payment |
| Dealer channel freight terms | M9.16 Dealers (summary + link here) |
| Warranty repair shipping / RMA detail | M9.17 Warranty |
| Custom engineering lead times | M9.18 Custom |
| Contact phones for sales | Contacts |
| Product lead time per SKU | PDP / catalog |

#### Cross-links

**Inbound:** Header · footer · mobile · PDP `deliveryText` (when populated) · PLP `.p-card__delivery` (when populated) · Commercial Trust FAQ «Доставка по РФ» · M9.9 delivery objections

**Outbound:** `/payment-methods` (ship after payment) · `/guarantee` (return path summary) · `/custom-equipment` (oversized) · `/dealers` · `/contact/` · catalog

#### Evidence Assets

| Asset | Use on Delivery |
|-------|-----------------|
| Shipment point addresses (Барнаул, Москва) | Factual anchors |
| TK / carrier logos or names | If operator attests |
| Regional coverage list or map | Primary proof |
| Delivery timeline bands | Operator-locked or «по согласованию» |
| Photo of warehouse / loading | Optional trust |

**Research:** [BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md)

---

### M9.15 — Payment (`/payment-methods`)

#### Purpose

Primary owner of **B2B payment and settlement mechanics**: cashless for legal entities, invoice flow, payment stages, VAT posture, closing documents framework. Answers «как платить и что получу после оплаты?»

#### Audience

- Закупщик / финконтроль — vendor onboarding and ERP
- Снабженец — invoice and prepayment gates
- Owner — payment path clarity without opaque B2B
- Дилер (secondary) — pointer to channel terms on Dealers

#### Primary Questions

| # | Question |
|---|----------|
| Q1 | Работаете с юрлицами по безналу? |
| Q2 | Как получить счёт на заказ / КП? |
| Q3 | Какой НДС / закрывающие документы? |
| Q4 | Предоплата и этапы (серия vs под заказ)? |
| Q5 | Срок действия счёта? |
| Q6 | Можно ли картой / физлицом? |
| Q7 | Когда начинается производство / отгрузка после оплаты? |

#### Allowed Topics

- Payment methods matrix (UL cashless, FL card policy, custom scenarios)
- Invoice request → issue → pay → produce/ship sequence
- VAT statement (operator-locked — e.g. 20% if attested)
- Closing document types (счёт, УПД, акт) — list not samples
- Prepayment framework for serial vs custom — **summary** + Custom link
- Dealer payment — **one-line** + Dealers link
- CTA to sales / Contacts for invoice request
- Distinction: quote-led B2B vs cart checkout (`cod` / `free_checkout`)

#### Forbidden Topics

| Topic | Primary owner |
|-------|---------------|
| Full bank requisites table | Contacts (if published) or operator charter |
| Dealer discount / deferral / channel commercial terms | M9.16 Dealers |
| TK regions and freight cost | M9.14 Delivery |
| Warranty claims | M9.17 Warranty |
| Custom engineering payment milestones detail | M9.18 Custom (cross-link) |
| Factory trust story | M9.13 About |
| SKU price | Catalog / PDP |

#### Cross-links

**Inbound:** Header · footer · mobile · M9.9 Q13 (planned PLP FAQ) · Commercial Trust «документы для закупки» (adjacent)

**Outbound:** `/delivery` (ship after pay) · `/dealers` (channel payment) · `/custom-equipment` (custom prepayment) · `/contact/` · catalog

#### Evidence Assets

| Asset | Use on Payment |
|-------|----------------|
| Payment flow diagram (process) | IA block — not design mockup |
| Document type checklist | Procurement proof |
| VAT / legal entity fact row | ATLAS-attested only |
| Sample invoice redacted | Only if operator provides |
| Bank requisites | **Only if operator charters publication** — else link Contacts |
| «No online card checkout» clarification | Align with runtime checkout evidence |

**Research:** [BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md)

---

### M9.16 — Dealers (`/dealers`)

#### Purpose

Primary owner of **dealer / wholesale / channel program**: partner types, commercial framework, territory policy, qualification, application intake, channel vs direct factory rules. Answers «почему выгодно работать с ЗПМ как партнёру?»

#### Audience

- Дилер / дистрибьютор HoReCa
- Региональный поставщик / торговая компания
- Интегратор / проектный партнёр
- Оптовый снабженец evaluating channel vs direct
- Корпоративный клиент comparing direct vs dealer path

#### Primary Questions

| # | Question |
|---|----------|
| Q1 | Это производитель? (trust transfer) |
| Q2 | Продаёте ли напрямую моим клиентам? |
| Q3 | Кто может стать партнёром? |
| Q4 | Какие скидки / условия / MOQ? |
| Q5 | Территория и конфликт каналов? |
| Q6 | Как подать заявку и что будет после? |
| Q7 | Маркетинговая поддержка и line card? |
| Q8 | Оплата, доставка, гарантия для партнёра? |

#### Allowed Topics

- Partner type matrix (дилер / опт / интегратор / проект)
- Channel policy (direct vs partner — operator-locked)
- Commercial framework summary (discounts, MOQ, deferral — operator input)
- Territory / exclusivity rules (operator input)
- Application form or CTA (primary intake — reconcile with PLP `blockdealersform`)
- Process: apply → qualify → КП / price list → onboard
- Proof strip: OEM summary, cert types, logistics summary, warranty summary — **links not duplicates**
- Marketing support inventory (operator input)
- Line card / assortment breadth facts

#### Forbidden Topics

| Topic | Primary owner |
|-------|---------------|
| Full factory story / video | M9.13 About |
| TK tables and regional freight detail | M9.14 Delivery |
| Invoice mechanics, VAT, bank requisites | M9.15 Payment |
| Warranty term, RMA process | M9.17 Warranty (summary + link) |
| Custom engineering workflow | M9.18 Custom |
| General sales contact cards | Contacts |
| Full certificate PDF gallery | PLP slider / About / `/our-certification` |

#### Cross-links

**Inbound:** Header · footer · mobile · PLP `zpm-dealers` block + form · M9.9 Q12 · M9.9 Option D «Партнёрство» · Payment bullet (should link)

**Outbound:** `/about` · `/payment-methods` · `/delivery` · `/guarantee` · `/custom-equipment` · `/contact/` · catalog

#### Evidence Assets

| Asset | Use on Dealers |
|-------|----------------|
| Partner type icons / segmentation | IA structure |
| Territory map or region list | If operator provides |
| Existing partner logos | If operator provides |
| OEM one-liner + About link | Trust strip |
| Cert type labels + deep link | Not full slider duplicate |
| Logistics 2-point summary + Delivery link | Барнаул + Москва |
| Warranty term summary + Guarantee link | Operator-locked term |
| Application form | Primary CTA — reconcile PLP duplicate |

**Research:** [BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md)

---

### M9.17 — Warranty (`/guarantee`)

#### Purpose

Primary owner of **warranty and post-sale service policy**: term, coverage, exclusions, claim process, channel routing, RMA logistics summary. Answers «что если сломается после покупки?»

#### Audience

- Закупщик / снабженец — tender and AVL compliance
- Owner — post-open risk reduction
- Дилер — warranty transfer to end client
- Производственник — equipment uptime and service path
- Сервис / эксплуатация — claim procedure

#### Primary Questions

| # | Question |
|---|----------|
| Q1 | Какой срок гарантии? |
| Q2 | С какой даты начинается? |
| Q3 | Что покрывается / не покрывается? |
| Q4 | Кто обслуживает — завод, дилер, СЦ? |
| Q5 | Как оформить рекламацию? |
| Q6 | Нужно ли везти оборудование? Кто платит доставку брака? |
| Q7 | Ремонт или замена — условия? |
| Q8 | Гарантия на custom / под заказ? |
| Q9 | Запчасти и постгарантийное обслуживание? |

#### Allowed Topics

- Warranty term strip (operator-locked)
- Start date definitions (shipment / sale / commissioning)
- Coverage matrix (body / components / electrics / consumables)
- Exclusions list (extend research baseline)
- Claim process steps with SLA chips (operator input)
- Channel routing: end customer vs dealer vs factory
- RMA logistics summary + Delivery link
- Custom / serial product class differences + Custom link
- Document pack for claim (накладная, талон, акт)
- Post-warranty paid service path (if offered)
- Cert vs warranty disclaimer

#### Forbidden Topics

| Topic | Primary owner |
|-------|---------------|
| Factory OEM narrative | M9.13 About |
| Outbound shipment to buyer | M9.14 Delivery |
| Payment for repair / spare parts invoicing | M9.15 Payment |
| Dealer program terms | M9.16 Dealers |
| Custom design approval workflow | M9.18 Custom |
| PDP passport download per SKU | PDP |
| General contact grid | Contacts (linked as fallback CTA) |

#### Cross-links

**Inbound:** Header · footer · mobile · PLP Commercial Trust «Гарантия производителя» (should link) · M9.9 Q7 · M9.16 partner warranty summary · PDP service card (currently inconsistent)

**Outbound:** `/dealers` · `/delivery` · `/custom-equipment` · `/contact/` · `/about` · catalog / PDP docs

#### Evidence Assets

| Asset | Use on Warranty |
|-------|----------------|
| Warranty term badge | Operator-locked |
| Coverage / exclusion tables | Policy proof |
| RMA process diagram | IA block |
| Sample warranty card / talon (redacted) | If operator provides |
| Service geography note | Operator input |
| Spare parts policy summary | Operator input |
| Link to conformity docs | `/our-certification` — not substitute for warranty |

**Research:** [BZPM-M9.17-WARRANTY-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.17-WARRANTY-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md)

---

### M9.18 — Custom Manufacturing (`/custom-equipment`)

#### Purpose

Primary owner of **custom / made-to-order equipment**: scope, product types, engineering process, intake requirements, commercial gates, differentiation from catalog SKUs. Answers «можете ли изготовить под мои требования и насколько это предсказуемо?»

#### Audience

- Снабженец / закупщик — custom capex and spec projects
- Технолог / инженер — parameters, materials, design responsibility
- Владелец предприятия / owner — non-standard fit and risk
- Интегратор пищевого производства
- Дилер with project clients

#### Primary Questions

| # | Question |
|---|----------|
| Q1 | Что можно заказать нестандартного? |
| Q2 | Как подать ТЗ / чертёж / эскиз? |
| Q3 | Как проходит согласование и производство? |
| Q4 | Сроки и этапы (КП → предоплата → изготовление)? |
| Q5 | Какая сталь / материалы / нагрузки? |
| Q6 | Кто проектирует — клиент или завод? |
| Q7 | Какая гарантия на нестандарт? |
| Q8 | Можно ли начать от каталожной модели? |
| Q9 | Документы (паспорт, декларация, as-built)? |

#### Allowed Topics

- Product type scope (tables, sinks, racks, neutral fabrications)
- Segment fit (HoReCa, bakery, meat/dairy plants)
- Process OL: intake → clarify → agree → produce → ship
- Parameter matrix (type, size, material, options)
- TZ / sketch / drawing intake checklist
- Design responsibility and approval rounds (operator input)
- Material spec (AISI grades — operator-locked)
- MOQ / minimum project size (operator input)
- Lead time bands (operator input)
- Bridge to catalog standard SKU as modification base
- Custom warranty summary + Guarantee link
- Payment prepayment summary + Payment link
- Oversized delivery + Delivery link
- Dealer / integrator path + Dealers link
- Primary CTA: custom brief / quote request

#### Forbidden Topics

| Topic | Primary owner |
|-------|---------------|
| Full factory tour narrative | M9.13 About |
| Standard TK freight tables | M9.14 Delivery |
| Full invoice / VAT policy | M9.15 Payment |
| Dealer margin framework | M9.16 Dealers |
| Full RMA legal text | M9.17 Warranty |
| SKU catalog listing | Catalog |
| Address / phone grid | Contacts |

#### Cross-links

**Inbound:** Header · footer · mobile (position #1 in corp strip) · M7.1 launch nav · M9.9 Q11 · Commercial Trust «На заказ» chip (should link) · search empty state (blueprint Scenario E — planned) · homepage production branch

**Outbound:** `/about` · `/payment-methods` · `/delivery` · `/guarantee` · `/dealers` · `/contact/` · `/our-certification` · catalog categories

#### Evidence Assets

| Asset | Use on Custom |
|-------|----------------|
| Parameter matrix table | Procurement anchor |
| TZ checklist block | Highest-value existing content |
| Process timeline | IA block |
| Production photos (custom examples) | If operator provides |
| Sanitized drawings | If operator provides |
| Material grade statement | Operator-locked |
| Case studies (anonymized) | If operator provides |
| Cert / conformity link | Not full About duplicate |

**Research:** [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md)

---

### Contacts (`/contact/`) — separate delivered workstream

#### Purpose

Primary owner of **reachable company identity**: address, phone, email, schedule, legal requisites summary, general inquiry form, map / directions. Operational contact surface — not commercial policy depth.

#### Audience

- Any visitor needing human contact
- Закупщик needing ИНН/КПП for vendor card
- Owner wanting callback or directions
- Fallback for all corp pages without dedicated CTA

#### Primary Questions

| # | Question |
|---|----------|
| Q1 | Как связаться (телефон, email, адрес)? |
| Q2 | График работы? |
| Q3 | Юридические реквизиты (ИНН/КПП)? |
| Q4 | Как добраться? |
| Q5 | Как отправить общий вопрос? |

#### Allowed Topics

- Contact cards (address, phone, email, schedule)
- Company summary card (compact facts)
- Legal requisites panel (ИНН/КПП — no bank unless chartered)
- General «Напишите нам» form
- Yandex map embed
- City popup sync (`CITY_DATA`)
- Route / directions CTA

#### Forbidden Topics

| Topic | Primary owner |
|-------|---------------|
| Payment policy depth | M9.15 Payment |
| Delivery regions / TK | M9.14 Delivery |
| Dealer program terms | M9.16 Dealers |
| Warranty RMA process | M9.17 Warranty |
| Custom engineering scope | M9.18 Custom |
| Factory narrative depth | M9.13 About |
| Bank details (unless operator re-charters) | M9.15 or operator decision |

#### Cross-links

**Inbound:** Header · footer · mobile · all corp pages (fallback CTA) · global modals

**Outbound:** `/about` (optional summary link) · catalog · corp pages as appropriate in form routing hints

#### Evidence Assets

| Asset | Use on Contacts |
|-------|-----------------|
| `zpm_logo.svg` | Summary card |
| FA contact icons | Card grid |
| Yandex map | Directions |
| ИНН/КПП facts | Requisites panel |
| City-aware hooks | `data-*` fields |

**Evidence:** [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md) · [SITE-002-CONTACTS-PAGE-POLISH-V1.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-POLISH-V1.md)

---

## Ownership matrix

Single primary owner per topic (CP-01). Secondary references = one-line summary + link only.

| Topic | Primary owner | Secondary references |
|-------|---------------|----------------------|
| Entity / factory identity | **About** | Dealers proof strip · Contacts summary · PLP Commercial Trust |
| Production geography | **About** | Delivery shipment points |
| Certificates / conformity (types) | **About** + `/our-certification` | PLP cert slider · Dealers summary · Custom link |
| «Сделано в России» fact | **About** (labeled) | Header badge · Dealers trust row |
| Logistics / shipping / regions | **Delivery** | Payment (ship after pay) · Dealers summary · Warranty (RMA return) · Custom (oversized) |
| Pickup / warehouse addresses | **Delivery** | Contacts (address card — different role: visit vs ship) |
| Payment methods / invoice flow | **Payment** | Custom prepayment · Dealers channel pointer |
| VAT / closing documents framework | **Payment** | Contacts (ИНН only today) |
| Bank requisites | **Payment** or **Contacts** *(operator charter)* | — |
| Dealer / opt / channel program | **Dealers** | Payment one-line · PLP dealer block |
| Territory / exclusivity | **Dealers** | — |
| Partner application intake | **Dealers** | PLP form — must reconcile duplicate |
| Warranty term / coverage | **Warranty** | Dealers summary · Custom class note · PLP trust benefit |
| RMA / claim process | **Warranty** | Delivery (return logistics) · Contacts (fallback) |
| Post-warranty service | **Warranty** | — |
| Custom scope / process / intake | **Custom** | About production proof · Payment scenario · Warranty class |
| Engineering / TZ requirements | **Custom** | — |
| Catalog SKU evaluation | **Catalog / PDP** | Custom «start from standard model» bridge |
| Phone / email / address / map | **Contacts** | All corp pages (fallback CTA) |
| General inquiry form | **Contacts** | Global modals (callback, question) |
| News / blog | **Blog** (`/blog/news`) | — |
| SKU price / stock / filters | **Catalog** | — |

---

## Page relationship map

### Catalog → Corporate Pages

```
                    ┌─────────────────────────────────────┐
                    │           CATALOG LAYER              │
                    │  Homepage · Hub · PLP · PDP · Search │
                    └─────────────────┬───────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
          ▼                           ▼                           ▼
   ┌──────────────┐           ┌──────────────┐           ┌──────────────┐
   │ Commercial   │           │ PLP blocks   │           │ PDP / Card   │
   │ Trust FAQ    │           │ dealers form │           │ micro-summaries│
   │ benefits     │           │ certificates │           │ deliveryText │
   └──────┬───────┘           └──────┬───────┘           └──────┬───────┘
          │                          │                          │
          │    secondary: one-line + deep link (CP-01)          │
          ▼                          ▼                          ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      CORPORATE PAGES (primary owners)                    │
├──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────┤
│ Custom   │ Payment  │ Delivery │ Dealers  │ Warranty │  About   │Contact│
│ M9.18    │ M9.15    │ M9.14    │ M9.16    │ M9.17    │ M9.13    │  —   │
│ /custom- │ /payment-│ /delivery│ /dealers │ /guarantee│ /about  │/contact│
│ equipment│ methods  │          │          │          │          │      │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────┘
```

**Catalog → Corp link rules:**

| Catalog surface | Target corp page | Rule |
|-----------------|------------------|------|
| Commercial Trust «Доставка по РФ» | Delivery | Summary + link |
| Commercial Trust «Гарантия производителя» | Warranty | Summary + link *(gap today)* |
| Commercial Trust «На заказ» | Custom | Summary + link *(gap today)* |
| PLP dealer block + form | Dealers | Form ownership TBD — corp page primary or PLP suppress |
| PLP certificates slider | About / `/our-certification` | Not full cert dump on Dealers |
| PDP `deliveryText` | Delivery | Populate or defer to link |
| M9.9 FAQ deep links | Respective corp owner | One primary URL per question class |
| Search empty → custom CTA | Custom | Blueprint Scenario E |

### Corporate Pages → Corporate Pages

```
                    ┌──────────────┐
                    │    About     │◄──── trust anchor for all
                    │   M9.13      │
                    └──────┬───────┘
                           │
     ┌─────────────────────┼─────────────────────┐
     │                     │                     │
     ▼                     ▼                     ▼
┌─────────┐         ┌───────────┐         ┌───────────┐
│ Custom  │◄───────►│  Payment  │◄───────►│ Delivery  │
│ M9.18   │         │  M9.15    │         │  M9.14    │
└────┬────┘         └─────┬─────┘         └─────┬─────┘
     │                    │                     │
     │    ┌───────────────┼───────────────┐     │
     │    │               │               │     │
     ▼    ▼               ▼               ▼     ▼
┌─────────────┐     ┌───────────┐     ┌─────────────┐
│  Warranty   │◄───►│  Dealers  │────►│  Contacts   │
│  M9.17      │     │  M9.16    │     │  (delivered)│
└─────────────┘     └───────────┘     └─────────────┘
```

**Cross-corp dependency chains (buyer journey):**

| Journey | Page sequence |
|---------|---------------|
| First B2B deal trust | About → Payment → Delivery → Contacts |
| Dealer onboarding | About → Dealers → Payment → Delivery → Warranty |
| Custom project | Custom → Payment → Delivery → Warranty → Contacts |
| Post-sale issue | Warranty → Delivery (return) → Contacts |
| Procurement file | Payment → Contacts (ИНН) → Delivery |

---

## Catalog secondary surface governance

| Surface | Must not duplicate | Allowed secondary content |
|---------|-------------------|---------------------------|
| PLP Commercial Trust | Full corp page body | One benefit line + URL |
| PDP commercial zone | Payment/Delivery/Warranty chapters | 1–2 sentences + link |
| PLP dealer form | Full dealer commercial framework | Form + «Подробнее» → Dealers |
| Header nav | — | Labels only — no policy text |
| Footer | — | Link list — no policy text |

---

## Phase gate assessment

| Phase | Verdict | Reasoning |
|-------|---------|-----------|
| **Research** | **COMPLETE** | All M9.13–M9.18 forensic reports exist in-repo with URL discovery, content audit, objection maps, and cross-link inventory |
| **IA / Architecture** | **READY** | This map defines purpose, audience, ownership, cross-links, and relationship structure for all 7 surfaces |
| **Copy** | **SUBSTANTIVELY COMPLETE** | Canonical PAGE-COPY reproducible; `Approved by: pending` on all six (B8) |
| **Design Charter** | **DRAFT COMPLETE / APPROVAL OPEN** | Six charters v1 in [charters/](charters/); operator approval pending on all |
| **Design Brief** | **DRAFT COMPLETE** | Six briefs v1 in [charters/](charters/) |
| **Design (visual)** | **NOT OPEN** | [BZPM-CORPORATE-PAGES-FINAL-PHASE-GATE-v1.md](BZPM-CORPORATE-PAGES-FINAL-PHASE-GATE-v1.md) verdict **NO** |
| **Implementation** | **NOT READY** | Research + IA ≠ implementation authorization; Contacts only page delivered; all M9.13–M9.18 implementation **not started** |

---

## Recommended next step

1. ~~**Per-page copy pass**~~ — **SUBSTANTIVELY COMPLETE** (M9.13–M9.18); operator sign-off pending (B8).
2. **Operator approval of Design Charters** — per [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md); **first approval: M9.13 About** charter v1.
3. **Resolve OQ clusters** affecting visual commitments (warehouse address, PLP dealer form, warranty term badge policy).
4. **Catalog cross-link pass** (documentation) — align Commercial Trust / M9.9 FAQ targets to IA owners before visual design.
5. **PLP dealer form reconciliation** — decide primary intake: corp page vs PLP block (document in program, not implement here).

**Explicit stop:** No wireframes · no mockups · no Twig/CSS/JS · no deploy.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-22 | **CREATED** — BZPM Corporate Pages IA Map v1; Research → IA phase gate; ownership matrix; relationship maps; per-page IA for M9.13–M9.18 + Contacts |
| 2026-06-22 | **UPDATED** — Copy artefact system registered; workflow IA → Copy → Design Charter; [BZPM-COPY-STANDARDS-v1.md](BZPM-COPY-STANDARDS-v1.md) |
| 2026-06-22 | **UPDATED** — Copy phase **CLOSED**; Design Charter **OPEN**; [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md) |
| 2026-06-22 | **RECONCILED** — Design Charter/Brief **DRAFT COMPLETE**; copy **SUBSTANTIVELY COMPLETE**; registry synced — [BZPM-CORPORATE-PAGES-PROGRAM-RECONCILIATION-v1.md](BZPM-CORPORATE-PAGES-PROGRAM-RECONCILIATION-v1.md) |

---

*BZPM Corporate Pages IA Map v1 — documentation only. No design or implementation authorized.*
