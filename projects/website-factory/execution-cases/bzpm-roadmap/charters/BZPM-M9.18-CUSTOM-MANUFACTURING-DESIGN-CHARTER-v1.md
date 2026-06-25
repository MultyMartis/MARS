# BZPM M9.18 — Custom Manufacturing — Design Charter v1

**Milestone:** M9.18 — Custom Manufacturing / Оборудование на заказ  
**URL (TEST):** `/custom-equipment`  
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
| IA Map | [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](../BZPM-CORPORATE-PAGES-IA-MAP-v1.md) § M9.18 |
| Approved copy | [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md) |
| Forensic research | [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) |
| Contacts reference surface | [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md) · [SITE-002-CONTACTS-PAGE-POLISH-V1.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-POLISH-V1.md) |
| Pattern precedent | [BZPM-M9.13-ABOUT-COMPANY-DESIGN-CHARTER-v1.md](./BZPM-M9.13-ABOUT-COMPANY-DESIGN-CHARTER-v1.md) · [BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md](./BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md) · [BZPM-M9.17-WARRANTY-DESIGN-CHARTER-v1.md](./BZPM-M9.17-WARRANTY-DESIGN-CHARTER-v1.md) |

**Primary design question:** *Может ли этот завод изготовить нестандартное оборудование под мою задачу — и насколько предсказуемо это пройдёт?*

**Secondary design question:** *Что мне нужно передать, чтобы завод взял проект в работу, а не отмахнулся формой «пришлите ТЗ»?*

**Central charter constraint (from task brief):** This page must feel like **«производитель способен решить нестандартную задачу»** — not **«отправьте ТЗ и ждите расчёт»**. Process visibility, capability proof, and scope honesty dominate; the form is the **endpoint** of education, not the page identity.

---

## 1. Purpose

### 1.1 Page mission

M9.18 `/custom-equipment` is the **primary owner of custom / made-to-order neutral stainless-steel equipment** for SITE-002 — not a second catalog, not a tender portal, not an online configurator, not a generic SEO article.

The page exists to prove that **ЗПМ as manufacturer** can take a non-standard project from **task description → clarified requirements → agreed configuration → production → shipment** — with honest scope boundaries, without inventing lead times, prices, MOQ, or engineering SLAs the operator has not published.

Per forensic Concept A («Engineering Trust Hub») as refined by copy v1.1: **capability + process + requirements clarity + commercial gates via links**, not parameter calculator or empty brief form.

### 1.2 What this page is NOT

| Anti-goal | Reason |
|-----------|--------|
| Online configurator / price calculator | Calculator drift — no instant quote, no dimension sliders with price |
| Tender / procurement application portal | Not a multi-attachment RFP workflow or legal TZ registry |
| Technical specification dump | Universal steel-grade tables and engineering formulas deferred to КП |
| Engineering consultancy landing | Consultation is a **path inside** manufacturing capability — not page mode |
| Catalog PLP duplicate | BLOCK 03 is scope boundaries — not SKU grid |
| Factory tour / OEM story page | Production narrative depth → `/about` |
| Full payment / delivery / warranty chapters | Owners: M9.15, M9.14, M9.17 — summary + link only |
| Fake project portfolio | No stock case studies, no anonymized placeholder galleries |
| «Send TZ and wait» minimal page | Live page failure mode — form without proof stack |

### 1.3 What this page IS

A **manufacturer capability page** for custom neutral equipment: scannable **when-custom triggers** (BLOCK 01), **task-fit matrix** (BLOCK 02), **honest product scope** with catalog bridge (BLOCK 03), **OEM trust layer** (BLOCK 04), **8-step production process** (SC-04), **requirements checklist** (SC-06), **materials framework** without universal spec table (BLOCK 07), **outcome transparency** (BLOCK 08), **FAQ**, and a **single quote-request path** via SC-11 form at page endpoint.

---

## 2. Audience hierarchy

| Segment | Priority | What they need from design |
|---------|----------|----------------------------|
| **Технолог / инженер** | **Primary** | Scope fit, design responsibility, data checklist, process gates — can factory execute? |
| **Снабженец / закупщик** | **Primary** | Predictable OL, documents, payment/delivery pointers — tender-adjacent without tender UX |
| **Владелец предприятия** | **Primary** | Risk reduction — manufacturer responsibility, approval before production |
| **Интегратор пищевого производства** | **Secondary** | Scope matrix, dealer/channel pointer, repeat-order path |
| **Дилер с проектными клиентами** | **Tertiary** | Factory capability proof + link to `/dealers` — not partner terms here |

**Design implication:** Layout rewards **scope scan → capability trust → process understand → data prepare → quote request** — not form-first, not spec-dense, not catalog browsing.

---

## 3. Conversion hierarchy

### 3.1 Primary

**Custom brief submission** — visitor submits **«Отправить заявку на расчёт»** (SC-11 FORM) after understanding scope, process, and data expectations.

Success signal: visitor knows **what the factory can make**, **how the project will move**, and **what to send** before manager contact; form captures product type, task description, and region for routing.

**Parallel primary channel (not competing button):** Phone in site header (`8 (3852) 72-18-90`) and email (`info@bzpm.ru`) — attested per copy; visible in BLOCK 10 support zone.

### 3.2 Secondary

**Contacts** — «Контакты завода» → `/contact/` when visitor needs address, requisites, or general inquiry beyond custom scope (BLOCK 10).

### 3.3 Tertiary

**Catalog** — «Каталог серийных моделей» → `/` when visitor may start from series modification (BLOCK 03 bridge, BLOCK 10 tertiary).

**Rule:** Catalog CTA is **modification bridge**, not SKU shopping — must not outrank primary form submit. No mid-page catalog grids.

---

## 4. Trust hierarchy

Ranked by **non-standard manufacturing confidence** for B2B equipment buyers.

| Rank | Trust signal | Source | Design role |
|------|--------------|--------|-------------|
| **T1** | **Transparent end-to-end process** (заявка → уточнение → КП → согласование → оплата → изготовление → контроль → отгрузка) | BLOCK 05 | **Dominant visual** — SC-04 timeline (8 steps) |
| **T2** | **Approval gate before production** — parameters fixed in КП; no «цех по договорённости» | BLOCK 05 badge + BLOCK 04 H3 | Process integrity — «Согласование до производства» |
| **T3** | **Manufacturer capability, not broker** — own factory, responsibility for result | BLOCK 04 | OEM proof stack — SC-03 variant + production image |
| **T4** | **Honest scope boundaries** — neutral SS in profile; thermal/refrigeration out of scope | BLOCK 01 note; BLOCK 03 table | Prevents false expectations — labeled in/out table |
| **T5** | **Requirements clarity** — what data speeds quote; optional files listed | BLOCK 06 | SC-06 checklist — reduces «black box TZ» fear |
| **T6** | **Outcome predictability** — agreed configuration, documents, warranty pointer | BLOCK 08 | Outcome table — what buyer receives |
| **T7** | **Catalog modification bridge** — faster path from series base | BLOCK 03 microcopy | Link pattern — not second catalog |
| **T8** | **Materials framework** — steel agreed in КП, not universal published matrix | BLOCK 07 | Honest engineering boundary |
| **T9** | **Cert / conformity anchor** | BLOCK 04 proof strip | Labeled «Сделано в России» — link `/our-certification` |
| **T10** | **Sibling policy depth via links** | Payment, Delivery, Guarantee, Dealers | SC-12 — CP-01 summaries only |

**Explicitly subordinate (do not visual-promote without OQ unlock):**

- Lead-time countdown chips («от 14 дней») — OQ-DC-C03, OQ-DC-C04
- Price range bands / estimate calculator — OQ-DC-C19
- MOQ badge — OQ-DC-C02
- AISI grade universal table — OQ-DC-C08
- Case study gallery — OQ-DC-C16
- Sanitized drawing thumbnails — operator asset required
- Quote SLA badge — OQ-DC-C04
- 3D visualization promise — OQ-DC-C05

**Why the buyer should believe the factory can make non-standard equipment:**

1. **Visible production path** — eight named steps ending at shipment, not a single «мы изготовим» claim.  
2. **Manufacturer identity** — legal entity, Барнаул site, same production base as series catalog (BLOCK 04 + About link).  
3. **Scope honesty** — factory states what it **will** and **will not** take; refusal before production is explicit in FAQ 1.  
4. **Parameter lock before shop floor** — commercial and configuration gate is a designed visual beat, not buried prose.  
5. **Requirements checklist** — factory tells buyer how to start even without full drawings (BLOCK 06 friction-reduction note).  
6. **Outcome table** — buyer sees deliverable (product + docs + warranty path), not only intake form.

---

## 5. Page role in buyer journey

### 5.1 Journey position

```
Catalog / PDP — «нужен другой размер / комплектация»
        │
        ▼
   ┌─────────────┐
   │   CUSTOM    │  ◄── made-to-order capability (this page)
   └──────┬──────┘
          │
   ┌──────┼──────────────────────────────┐
   │      │                              │
   ▼      ▼                              ▼
About  Payment + Delivery            Guarantee
(OEM)  (commercial gates)          (custom class)
   │      │                              │
   └──────┴──────────┬───────────────────┘
                     ▼
              Contacts (fallback)
                     │
                     ▼
              Dealers (channel)
```

### 5.2 Before this page

| Prior state | Typical entry | Page must do |
|-------------|---------------|--------------|
| Header nav #1 | Strategic custom entry | Establish manufacturer capability in first screen |
| Catalog fit failure | PLP/PDP — size/config gap | Show scope + catalog bridge |
| M9.9 FAQ Q11 | «Делаете нестандарт?» | Primary answer surface |
| Commercial Trust «На заказ» | Catalog trust chip *(gap today)* | Consistent depth — no link drift |
| About custom pointer | Wants production proof | Deep custom process — not duplicate About body |
| Warranty custom class | FAQ 5 on Guarantee | Authoritative custom workflow depth |
| Dealer project client | Dealers pointer | Capability proof — Dealers stays channel terms |

### 5.3 After this page

| Exit | When |
|------|------|
| FORM submit | Ready to describe task with type + region |
| Phone / email | Urgent project; prefers voice |
| `/contact/` | Requisites, directions, general form |
| `/about` | Deeper OEM / factory narrative |
| `/payment-methods` | Prepayment / invoice rules for custom |
| `/delivery` | Oversized / regional shipment |
| `/guarantee` | Custom warranty conditions |
| `/dealers` | Partner channel for end client |
| `/our-certification` | Conformity depth |
| `/` catalog | Series modification starting point |

**Program note:** Custom is **design order #6** — extends SC-04 (sixth corp instantiation), SC-06, SC-09, SC-11; composes patterns from About (OEM), Payment (commercial gates), Delivery (shipment), Warranty (service class), Dealers (channel).

---

## 6. Relationship with sibling pages

CP-01 rule: **one primary owner per topic**. Custom shows **one-line summary + text link** — never embedded foreign page body.

| Page | URL | Custom relationship | Allowed on Custom | Forbidden on Custom |
|------|-----|----------------------|-------------------|---------------------|
| **About** | `/about` | BLOCK 04 H3; proof strip | OEM summary + link | Factory video hero, full trust facts table |
| **Payment** | `/payment-methods` | BLOCK 05 step 5; BLOCK 08; FAQ 6 | Prepayment summary + link | VAT %, bank table, methods matrix |
| **Delivery** | `/delivery` | BLOCK 05 step 8; BLOCK 08 | Shipment summary + link | TK tables, freight calculator |
| **Warranty** | `/guarantee` | BLOCK 08; FAQ 5, 8 | Custom class summary + link | Claim process, exclusion wall |
| **Dealers** | `/dealers` | BLOCK 10 microcopy | Channel pointer + link | Discounts, territory, partner logos |
| **Contacts** | `/contact/` | BLOCK 10 secondary | Fallback contact + link | Full contact card grid, map duplicate |
| **Certification** | `/our-certification` | BLOCK 04 proof strip | Labeled badge + link | Cert PDF wall |
| **Catalog** | `/` | BLOCK 01, 03, FORM | Text links to categories / SKU bridge | PLP grid, price cards, filters |

---

## 7. Evidence hierarchy

### Level 1 — Must be visible without deep scroll (first ~2 viewports)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| Custom scope + manufacturer framing | H1 + Lead | SC-01 internal-page rhythm — align Contacts shell |
| **When custom is needed** (trigger scan) | BLOCK 01 | Bullet triggers — scope qualification |
| **Process start** (steps 1–3 visible) | BLOCK 05 | SC-04 timeline — **dominant element begins** |
| Optional value chips | MICRO value chips | 3 micro-labels — subordinate to H1+lead |
| Scope boundary note | BLOCK 01 microcopy | Neutral SS only — catalog link for thermal |

### Level 2 — Core proof stack (mid-page, scroll expected)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| Full 8-step custom process | BLOCK 05 | SC-04 timeline — **peak visual** |
| Approval gate badge | BLOCK 05 microcopy | «Согласование до производства» — process integrity beat |
| Requirements checklist | BLOCK 06 | SC-06 — **peak practical density** |
| OEM capability layer | BLOCK 04 | H3 stack + proof strip + production image |
| Product scope groups | BLOCK 03 | Scope prose + in/out table — **not** product cards |
| Task-fit matrix | BLOCK 02 | SC-07 variant — 7-row table |
| Outcomes / deliverables | BLOCK 08 | Outcome table — 5 rows |

### Level 3 — Supporting context (lower visual weight)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| Materials framework | BLOCK 07 | Prose + H3s — no universal grade table |
| FAQ (8) | BLOCK 09 | SC-08 accordion — objection cleanup |
| Cross-links summary | MICRO optional | Footer-style link grid — lowest priority |
| Optional parameter companion table | MICRO BLOCK 06 companion | Compact SC-07 — subordinate to checklist |
| Timeline note (no SLA on site) | BLOCK 05 | Prose — no countdown chips |
| Dealer pointer | BLOCK 10 | One-line SC-12 |

---

## 8. Visual narrative

Narrative arc is **manufacturing confidence**, not intake bureaucracy.

### Beginning — «Есть ли у завода компетенция под мою задачу?» (Utility → BLOCK 01–03)

| Beat | Content | Emphasis |
|------|---------|----------|
| Orient | Breadcrumb, H1, lead | SC-01 — manufacturer makes to order in Барнаул |
| Qualify | BLOCK 01 when-custom triggers | Buyer self-selects — fits my case? |
| Scope | BLOCK 03 product groups + boundary table | Honest in/out — **not** catalog mimic |
| Bridge | BLOCK 03 catalog microcopy | Series modification path |

**Beginning must answer IA Q1 (что можно заказать?) in <15 seconds of scan — without form or price.**

### Middle — «Как завод ведёт проект и что подготовить» (BLOCK 04 → BLOCK 06)

| Beat | Content | Emphasis |
|------|---------|----------|
| Trust | BLOCK 04 why factory | OEM proof — manufacturer responsibility |
| **Process** | BLOCK 05 eight-step timeline | **Peak visual — SC-04 spine** |
| Gate | BLOCK 05 approval badge | Parameters locked before shop |
| Prepare | BLOCK 06 data checklist | SC-06 — enables step 1–2 of process |
| Specify | BLOCK 07 materials | Framework — values in КП |
| Receive | BLOCK 08 outcomes | What buyer gets — configuration + docs |

**Middle must answer IA Q2–Q6 without leaving page (except policy depth links).**

### End — «Опишите задачу — начнём расчёт» (BLOCK 09 → BLOCK 10 → FORM)

| Beat | Content | Emphasis |
|------|---------|----------|
| Objections | BLOCK 09 FAQ | Scope, design owner, warranty, timing — SAFE UNKNOWN handling |
| Action | BLOCK 10 CTA + SC-11 FORM | **Primary conversion zone** — quote request |

**End must make «Отправить заявку на расчёт» obvious after education; phone parallel support visible.**

---

## 9. Block importance map

Ranking for **all approved v1.1 copy blocks** (Critical / Important / Supporting).

| Block | Title | Rank | Rationale |
|-------|-------|------|-----------|
| Utility | Meta, breadcrumb | Supporting | Required shell — no visual competition |
| — | H1 + Lead | **Critical** | Capability framing + process promise |
| **01** | Когда требуется изготовление на заказ | **Critical** | Qualification — prevents wrong requests |
| **02** | Какие задачи помогает решать | Important | Task-fit matrix — technologist scan |
| **03** | Что можно изготовить | **Critical** | Scope owner — boundary honesty |
| **04** | Почему проектируют и производят на заводе | **Critical** | OEM trust — manufacturer proof |
| **05** | Как проходит работа над заказом | **Critical** | Primary mental model — page spine |
| **06** | Какие данные нужны для расчёта | **Critical** | SC-06 — intake without tender UX |
| **07** | Материалы и исполнение | Important | Engineering boundary — subordinate to process |
| **08** | Что получает заказчик | Important | Outcome predictability — trust closer |
| **09** | FAQ | Important | Objection resolver — pre-CTA |
| **10** | CTA | **Critical** | Conversion band |
| FORM | Заявка на расчёт | **Critical** | Primary conversion instrument |
| MICRO | Value chips | Important | Optional — accelerates scan if under lead |
| MICRO | Cross-links summary | Supporting | Optional footer — CP-01 navigation aid |

---

## 10. Visual emphasis strategy

### 10.1 What MUST dominate visually

| Element | Why |
|---------|-----|
| BLOCK 05 SC-04 process (8 steps) | Answers primary question — «как завод проведёт проект» |
| BLOCK 05 approval gate badge | Manufacturing discipline — no surprise production |
| BLOCK 04 OEM capability stack + production image | **Main competence proof** — factory, not form |
| BLOCK 06 SC-06 requirements checklist | Practical quote readiness — not TZ wall |
| BLOCK 03 scope boundary table | Honest specialization — trust via limits |
| BLOCK 10 + SC-11 FORM | Conversion endpoint — after education |
| BLOCK 08 outcome table | Predictability — what buyer receives |
| Lead + BLOCK 01 triggers | Immediate qualification |

### 10.2 What must NOT dominate visually

| Element | Why |
|---------|-----|
| SC-11 form above fold | Form-first = «отправьте ТЗ и ждите» anti-pattern |
| Parameter configurator UI | Calculator drift forbidden |
| Price / lead-time badges | OQ-DC-C03, C04, C19 — SAFE UNKNOWN |
| Product scope as SKU cards | Catalog conflict — BLOCK 03 is boundaries, not PLP |
| BLOCK 07 materials as spec datasheet | Technical overload — values in КП |
| Fake case study gallery | OQ-DC-C16 — no placeholder projects |
| Tender attachment multi-step wizard | Tender-form drift |
| DWG viewer / CAD embed | Over-engineering — upload field sufficient |
| BLOCK 09 FAQ as primary content | Accordion is cleanup, not hero |
| Universal steel grade matrix | Copy forbids — disclaimer in BLOCK 07 |
| Thermal / refrigeration upsell | Out of scope — BLOCK 01 note only |

### 10.3 Visual weight budget (relative 1–5)

| Block | Tier | Weight | Notes |
|-------|------|--------|-------|
| **05** | Tier 1 — Anchor | **5** | Largest structured component — SC-04 owner; 8 steps |
| **04** | Tier 1 — Anchor | **4** | OEM proof + image — competence evidence |
| **06** | Tier 1 — Anchor | **4** | Requirements checklist — subordinate to BLOCK 05 |
| **03** | Tier 1 — Anchor | **4** | Scope groups + boundary table |
| **10 + FORM** | Tier 1 — Anchor | **4** | CTA + SC-11 endpoint |
| **01** | Tier 1 — Anchor | **3** | Trigger list — first-screen qualification |
| **08** | Tier 2 — Support | **3** | Outcome table — 5 rows |
| **02** | Tier 2 — Support | **3** | Task matrix — 7 rows |
| **09** | Tier 2 — Support | **3** | 8-item accordion |
| **07** | Tier 2 — Support | **2** | Materials prose — deliberately light |
| Value chips | Tier 2 — Support | **2** | 3 micro-labels — optional |
| Lead | Tier 1 | **3** | Sets frame — not longer than BLOCK 01 intro |
| Cross-links table | Tier 3 — Context | **1** | Optional — navigation only |

**Section rhythm:** BLOCK 06 must read as **«подготовка к шагам 1–2»** of BLOCK 05 — visual affinity to SC-04, not standalone tender checklist. BLOCK 07 stays **below** process + checklist weight.

---

## 11. Custom manufacturing philosophy

### 11.1 Charter decision — choose ONE dominant approach

| Approach | Verdict |
|----------|---------|
| A) Technical specification page | **REJECTED as dominant** — invites spec-table overload, calculator drift, tender-form UX |
| B) Engineering consultation page | **REJECTED as dominant** — form/consultation-first; underweights production proof |
| **C) Manufacturer capability page** | **SELECTED — dominant** |

### 11.2 Why Manufacturer capability (C)

| Reason | Detail |
|--------|--------|
| Task brief | Page must prove factory **can solve** non-standard task — not collect TZ into void |
| Copy spine | BLOCK 04 OEM proof + BLOCK 05 eight-step process — natural capability narrative |
| Forensic Concept A | «Engineering Trust Hub» — proof + process + commercial predictability via links |
| IA Q1–Q3 | Scope and process are primary questions — spec depth (Q5) is supporting |
| Anti-pattern avoidance | Live page is flat `.zpm-seo` prose without CTA — capability stack fixes failure mode |
| Catalog relationship | Custom extends series manufacturing — capability page aligns with OEM identity |
| Program design order #6 | Reuses SC-04/SC-06 from Payment→Warranty chain — sixth instantiation with custom-specific steps |

### 11.3 Supporting roles (non-dominant)

| Approach | Role on page |
|----------|--------------|
| Technical specification | BLOCK 06 checklist + BLOCK 07 materials framework — **enabling**, not page identity |
| Engineering consultation | FORM + FAQ 2 — **entry path** after capability education; manager refines by phone |

**Forbidden as visual spine:** Parameter calculator, universal spec tables, tender upload portal, consultation-only hero with form above fold.

---

## 12. Core design decisions (summary lock)

| Decision | Charter lock |
|----------|--------------|
| **Page mode** | **Manufacturer capability page** — OEM proof + process + honest scope |
| **Visualization philosophy** | **Process-led evidence stack** — scannable steps and checklists; prose subordinate; no dashboard/calculator aesthetics |
| **Dominant trust mechanism** | **SC-04 eight-step process** + **approval-before-production gate** + **BLOCK 04 OEM proof** |
| **Role of process** | **Primary visual anchor (5/5)** — sixth corp SC-04 instantiation; custom-specific step labels |
| **Role of order parameters** | **SC-06 checklist + optional compact SC-07 companion** — aids step 1–2; **not** configurator fields |
| **Role of form** | **SC-11 endpoint (4/5)** — quote request after education; extends SC-10 consent discipline |
| **Role of files / attachments** | **Optional FORM field** — PDF/JPG/PNG/DWG ≤10 МБ per copy; degrade gracefully if backend not ready |
| **Role of cases / photos without assets** | **One production proof image** (BLOCK 04) — reuse About factory photo pattern if operator asset exists; **no** fake portfolio; case slots **excluded** until OQ-DC-C16 unlock |
| **Primary conversion** | **«Отправить заявку на расчёт»** — SC-11 form submit |

---

## 13. Process strategy (SC-04)

### 13.1 Role

BLOCK 05 is the **page spine** — the buyer's mental model of how the factory moves from inquiry to shipment.

### 13.2 SC-04 rules for Custom

| Rule | Detail |
|------|--------|
| Step count | **8 steps** — per approved copy; equal visual weight |
| Pattern | Numbered phased timeline — horizontal desktop / vertical ≤1024px |
| SLA chips | **FORBIDDEN** — timeline note prose only (OQ-DC-C03, C04) |
| Approval gate | Visual badge **«Согласование до производства»** — between timeline and BLOCK 06 or integrated in BLOCK 05 footer |
| Distinctiveness | Labels custom-specific — not copy-paste Payment/Delivery; shared SC-04 component shell only |
| Cross-links in steps | Steps 5, 8 — inline text links to Payment, Delivery — not embedded blocks |

### 13.3 Should process dominate?

| Decision | **YES — primary visual anchor** |
|----------|--------------------------------|
| BLOCK 05 weight | **5/5** — highest on page |
| Rationale | Capability is **proven through visible OL**, not claims |

---

## 14. Requirements / parameters strategy (SC-06, SC-07)

### 14.1 Role

BLOCK 06 answers: «Что передать, чтобы завод мог рассчитать» — practical checklist, not compliance trap or tender document list.

### 14.2 Visual importance

| Parameter | Decision |
|-----------|----------|
| Pattern | **SC-06 document/data checklist** — «данные» + «зачем нужны» |
| Layout | Responsive table → stacked rows ≤1024px |
| Visual weight | **Tier 1 (4/5)** — important but **subordinate to BLOCK 05 (5/5)** |
| Placement | **After** BLOCK 05 in copy order — process then prepare |
| Optional companion | MICRO parameter table — **Tier 2 (2/5)** if used; not duplicate of checklist |
| Sample drawing thumbnails | **FORBIDDEN** unless operator provides (OQ-DC-C16) |

### 14.3 Calculator / configurator guard

| Forbidden | Detail |
|-----------|--------|
| Dimension input sliders | Calculator drift |
| Live price estimate | OQ-DC-C19 |
| Required field matrix for all 9 parameters in FORM | Form scope creep — description textarea carries detail |
| «Конструктор заказа» UI | Tender/configurator anti-pattern |

### 14.4 Should parameters dominate?

| Decision | **Important — not page-wide dominant** |
|----------|----------------------------------------|
| Rationale | Parameters **enable** the process — BLOCK 05 remains spine |
| Treatment | Checklist reads as «подготовка к шагу 1–2» — visual connector to SC-04 |

---

## 15. Form strategy (SC-11)

### 15.1 Role

SC-11 is the **custom quote intake instrument** — captures **product type**, **task description**, and **region** for manager/engineering routing; not a generic callback form, not a full TZ portal.

### 15.2 Relationship to SC-10 / Contacts

| Aspect | Custom SC-11 | Contacts form |
|--------|--------------|---------------|
| Purpose | Custom quote / calculation request | General inquiry + requisites discovery |
| Unique fields | **product_type** (select), **task description** (textarea), **quantity**, **region** (required), **deadline**, **catalog SKU link**, **file upload** | No custom fields |
| Shared | name, phone, email, consent, privacy link, submit states | SC-10 base |
| Organization field | Optional — per copy | — |
| Backend upload | **SAFE UNKNOWN** — charter must allow degrade path (OQ-DC-C17) | — |
| Success microcopy | Manager callback in business hours | Same discipline |

### 15.3 Rules

| Rule | Detail |
|------|--------|
| Placement | **After** BLOCK 10 CTA band only — no mid-page form |
| Do not duplicate Contacts contact card grid | BLOCK 10 secondary link suffices |
| File upload optional | Per copy — not required for submit |
| Select prominence | Product type visually emphasized — routing identity |
| Degrade if no backend | Show field with helper «или отправьте на email» — **or** hide upload with copy-only helper per OQ-DC-C17 |
| Global modals | Do **not** substitute for dedicated SC-11 — live page failure mode |
| Do not require complete TZ | Copy: «можно начать с короткого описания» — form must stay low-friction |

### 15.4 Form scope creep guard

| MVP fields (locked per copy v1.1) | Deferred unless operator unlocks |
|-----------------------------------|----------------------------------|
| product_type, description, region, contact, phone, email, consent; optional: quantity, deadline, catalog link, organization, file | multi-file upload UI, serial fields, full TZ wizard, load calc inputs, steel grade picker, drawing approval workflow |

---

## 16. Files and attachments strategy

### 16.1 Role

File upload is **optional acceleration** for step 1 of process — not proof of tender seriousness, not mandatory gate.

### 16.2 Charter decisions

| Parameter | Decision |
|-----------|----------|
| Formats (copy-attested) | PDF, JPG, PNG, DWG — ≤10 МБ per file |
| Required? | **No** — per copy and BLOCK 06 helper |
| Multiple files | Copy allows one-by-one or archive via manager — **single file input MVP** unless OQ-DC-C17 unlocks multi |
| Visual treatment | Standard file input — **not** drag-drop zone hero |
| Without backend | **Degrade:** helper text to email `info@bzpm.ru` with subject hint; do not fake success upload |
| Security | Implementation charter owns virus scan, storage — **SAFE UNKNOWN** here |

### 16.3 Forbidden

- Mandatory drawing upload before submit  
- DWG inline viewer  
- «Прикрепите полное ТЗ» as required banner  
- Tender ZIP multi-document workflow  

---

## 17. Cases and photography strategy (asset gap)

### 17.1 Operator asset status

Per design program: production photos, sanitized drawings, case studies — **MISSING** / **BLOCKED**.

### 17.2 Charter decisions

| Asset | Treatment |
|-------|-----------|
| **Production proof image** (BLOCK 04) | **REQUIRED slot** — static factory/workshop photo; same discipline as About §15 static-first |
| **Case study gallery (0–3)** | **EXCLUDED** until OQ-DC-C16 operator provides permission + assets |
| **Sanitized drawing thumbnails** | **EXCLUDED** — text checklist only |
| **Before/after project photos** | **FORBIDDEN** as stock placeholders |
| **Segment icons** (HoReCa, bakery) | **Optional** — low weight; no fake client logos |

### 17.3 Without assets — what still proves competence

1. SC-04 process timeline (structural — no photo required)  
2. BLOCK 04 OEM prose + proof strip (SC-03 variant)  
3. BLOCK 03 scope honesty + catalog bridge  
4. BLOCK 06 requirements checklist  
5. Link to `/about` for deeper factory evidence  
6. **One** attested production image when operator supplies — not a gallery  

**Explicit rule:** Design **must not** use placeholder project photos, lorem case titles, or anonymized fake kitchens.

---

## 18. Catalog relationship strategy

### 18.1 Conflict guard

Custom page is **not** a second catalog. BLOCK 03 lists **scope groups in prose** — not product cards with prices.

### 18.2 Allowed catalog touchpoints

| Surface | Treatment |
|---------|-----------|
| BLOCK 01 note | Link to catalog for thermal/refrigeration series |
| BLOCK 03 groups | Text links to category hubs (столы, ванны) — **inline**, not grid |
| BLOCK 03 bridge | «Укажите артикул» — modification path |
| BLOCK 10 tertiary | Catalog CTA — subordinate button/link |
| FORM | Optional catalog SKU URL field |

### 18.3 Forbidden

- PLP-style product cards in BLOCK 03  
- Price display  
- Filter/sort UI  
- «Похожие товары» block  
- SKU count badges  

---

## 19. CTA strategy

### 19.1 Hierarchy (locked per copy v1.1)

| Priority | Element | Placement |
|----------|---------|-----------|
| **Primary** | «Отправить заявку на расчёт» → form submit | BLOCK 10 + FORM only |
| **Secondary** | «Контакты завода» → `/contact/` | BLOCK 10 — subordinate |
| **Tertiary** | «Каталог серийных моделей» → `/` | BLOCK 10 — subordinate |
| **Support** | Phone in header · `info@bzpm.ru` | BLOCK 10 reference + site chrome |

### 19.2 One CTA or multiple?

| Decision | **One primary button zone per page** |
|----------|--------------------------------------|
| Mid-page buttons | **FORBIDDEN** — no «Отправить заявку» before BLOCK 10 |
| Text links | Permitted in lead, process steps, BLOCK 03–08 — not button-styled |
| Phone as parallel CTA | Header + BLOCK 10 — support, not competing primary button |

### 19.3 Placement philosophy

CTA band **after FAQ** — user has consumed scope, capability, process, requirements, materials, outcomes, and residual objections.

FORM immediately follows CTA band (or integrated in same visual zone per SC-09).

---

## 20. FAQ strategy

### 20.1 Role

FAQ is **objection resolver** for custom edge cases — not primary education (BLOCK 01–08 own that).

### 20.2 Parameters

| Parameter | Decision |
|-----------|----------|
| Count | **8 items** — per approved copy; do not expand |
| Pattern | SC-08 single-open accordion |
| Position | After BLOCK 08, before BLOCK 10 |
| Visual weight | Important — **subordinate** to BLOCK 05 and BLOCK 06 |

### 20.3 Priority items (mobile density)

| Priority | FAQ | Why |
|----------|-----|-----|
| 1 | Изготовите ли нестандарт / отказ? | Core scope Q — honesty |
| 2 | Кто проектирует? | Core engineering Q |
| 3 | Модель из каталога + изменения? | Catalog bridge Q8 |
| 4 | Срок изготовления? | Core timing — SAFE UNKNOWN prose |
| 5–8 | Remaining | Docs, warranty, prepayment, misfit |

### 20.4 Overlap discipline

FAQ must **not repeat** full BLOCK 05 timeline or BLOCK 06 checklist — short confirmatory answers with links to owners (Payment, Guarantee, Delivery).

---

## 21. Shared components

### 21.1 Required components (task mandate)

| ID | Component | Custom blocks | Role |
|----|-----------|---------------|------|
| **SC-04** | Process timeline | BLOCK 05 | **Dominant** — 8-step custom OL |
| **SC-06** | Document / data checklist | BLOCK 06 | Requirements for quote — subordinate to SC-04 |
| **SC-09** | CTA band | BLOCK 10 | Pre-form conversion zone |
| **SC-11** | Custom brief form | FORM | Extended intake — owner M9.18 only |
| **SC-12** | Cross-link inline | Lead, BLOCK 03–08, BLOCK 10, MICRO | CP-01 one-line + link |

### 21.2 Additional components instantiated on Custom

| ID | Component | Custom blocks |
|----|-----------|---------------|
| SC-01 | Corp page shell | All |
| SC-03 | Trust row / proof strip | BLOCK 04 proof strip; optional MICRO value chips |
| SC-07 | Matrix table | BLOCK 02 task list; BLOCK 03 scope table; optional MICRO parameter companion |
| SC-08 | FAQ accordion | BLOCK 09 |

### 21.3 Custom-specific ownership

| Component | Ownership note |
|-----------|----------------|
| SC-11 | **Primary owner** M9.18 — Dealers/Warranty/About use SC-10 variants, not SC-11 |
| SC-04 | **Sixth instantiation** — after Payment, Delivery, Warranty, About (informational), Dealers |
| SC-06 | **Fourth instantiation** — after Payment, Warranty, Delivery; custom variant is «data for quote» not «documents for claim» |

### 21.4 Optional / excluded

| ID | Verdict |
|----|---------|
| SC-02 Hero / media | **Partial** — production image in BLOCK 04 only; no full hero video |
| SC-05 Proof cards | **Optional** — BLOCK 02 may use card variant of matrix; not required |
| SC-14 Cert promo | **Exclude as block** — proof strip link only in BLOCK 04 |

---

## 22. Design risks

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R1 | **Calculator drift** — dimension inputs, price hints, configurator UI | **Critical** | §14.3 forbidden patterns; no estimate badges |
| R2 | **Tender-form drift** — multi-doc upload, required TZ, legal field explosion | **High** | §15.4 MVP lock; optional file; short description OK |
| R3 | **Form-first page** — SC-11 above fold | **High** | §19.2 — CTA only after BLOCK 09 |
| R4 | **Lead-time / price promise chips** | **High** | OQ-DC-C03, C04, C19 — prose only in timeline note / FAQ |
| R5 | **Fake portfolio** — placeholder case studies | **High** | §17 — exclude until operator assets |
| R6 | **Technical spec overload** — BLOCK 07 as datasheet hero | **Medium** | Weight 2/5; disclaimer visible |
| R7 | **Catalog conflict** — BLOCK 03 reads as PLP | **High** | §18 — prose + links only |
| R8 | Live `.zpm-seo` flat prose page | **High** | New corp block system — process spine |
| R9 | **Longest corp page** — 10 blocks + heavy form scroll fatigue | **Medium** | Tier weight map §10.3; section spacing |
| R10 | **File upload without backend** — false confidence | **High** | §16 degrade path; OQ-DC-C17 |
| R11 | **SC-04 fatigue** — sixth timeline on site | **Low** | 8 custom-specific steps — shared shell, distinct labels |
| R12 | BLOCK 06 + FORM field duplication | **Medium** | Form captures summary; checklist educates — no duplicate 9-row form |
| R13 | Warranty custom class drift vs M9.17 | **Medium** | BLOCK 08 + FAQ 5 — link only; no term badge |
| R14 | Payment prepayment inconsistency | **Medium** | BLOCK 05 step 5 + FAQ 6 — link to Payment owner |
| R15 | Production photo missing | **Medium** | Static slot with caption; hide if no asset — no stock photo |
| R16 | Header nav #1 visibility — page under-delivers | **Medium** | Capability stack must satisfy strategic entry |
| R17 | Commercial Trust «На заказ» chip no link | **Low** | Catalog doc parallel — not design here |
| R18 | MO warehouse address in delivery copy cross-ref | **Low** | Region in FORM only — defer to M9.14 |

---

## 23. Forbidden patterns

| Pattern | Why forbidden |
|---------|---------------|
| **Online configurator / calculator** | Task brief anti-goal; R1 |
| **Instant quote / price range badge** | OQ-DC-C19 SAFE UNKNOWN |
| **Lead-time countdown chips** | OQ-DC-C03 SAFE UNKNOWN |
| **Tender portal UX** — multi-step RFP, required attachments wall | Tender-form drift |
| **«Прикрепите полное ТЗ» required gate** | Blocks low-friction start per copy |
| **SKU grid / product cards / prices** | Owner: Catalog — R7 |
| **Fake project gallery / case studies** | R5 — operator asset required |
| **Stock kitchen / factory photography** | Asset rule — real production only |
| **Universal AISI grade table** | Copy BLOCK 07 disclaimer |
| **DWG/CAD viewer embed** | Over-engineering |
| **Form above fold as hero** | «Отправьте ТЗ и ждите» anti-pattern |
| **Multiple primary CTA buttons mid-page** | §19.2 |
| **Global modal as only custom path** | Live page failure — dedicated SC-11 required |
| **Full factory tour video hero** | Owner: About |
| **TK / freight tables** | Owner: Delivery |
| **Invoice/VAT / bank detail** | Owner: Payment |
| **Dealer discount / territory** | Owner: Dealers |
| **Full RMA / warranty legal wall** | Owner: Warranty |
| **Thermal/refrigeration custom upsell** | Out of scope — BLOCK 01 note |
| **ПП №719 universal badge** | Cert disclaimer discipline |
| **Autoplay process animation** | UX noise + reduced-motion |
| **Parameter matrix as page hero** | Spec-page drift — checklist subordinate to process |

---

## 24. Success criteria

Operator judges Custom Manufacturing design **successful** when:

| # | Criterion | Verification method |
|---|-----------|---------------------|
| S1 | Visitor answers central question: **может ли завод изготовить под мою задачу** | Operator scenario test |
| S2 | Secondary question answered: **как пройдёт проект и что передать** | BLOCK 05 + BLOCK 06 review |
| S3 | BLOCK 05 process scannable in **<25 seconds** desktop | Operator scan test |
| S4 | Page does **not** read as calculator, tender form, or catalog PLP | Operator visual compare vs live `/custom-equipment` |
| S5 | BLOCK 04 capability visible but **process dominates** over form | Weight budget audit §10.3 |
| S6 | No lead-time / price badges unless OQ unlocked | Governance check |
| S7 | No CP-01 violations — sibling topics are links only | Cross-link audit |
| S8 | SC-11 includes **product_type** + **description** + **region**; consent matches Contacts | Side-by-side with `/contact/` |
| S9 | SC-04 / SC-06 / SC-09 / SC-11 / SC-12 instantiated per program registry | Design program check |
| S10 | One primary CTA zone — no mid-page submit | Design review |
| S11 | Mobile ≤1024px — checklist and 8-step process stack without horizontal scroll trap | Responsive check |
| S12 | BLOCK 03 visually distinct from catalog PLP | Operator visual compare |
| S13 | Design charter approved **before** wireframe/mockup work | Phase gate |
| S14 | Page feels like **manufacturer capability** — not «send TZ and wait» | Operator qualitative review |
| S15 | IA Q1–Q9 answerable from on-page content + links | IA coverage audit |

---

## 25. Open questions (operator lock)

### 25.1 File upload and intake

| ID | Question | Impact | Default if unresolved |
|----|----------|--------|----------------------|
| OQ-DC-C17 | File upload via site — backend ready? Multi-file? | SC-11 field visibility | **Show optional field** + email fallback helper |
| OQ-DC-C17b | Допустимые форматы beyond PDF/JPG/PNG/DWG? | Validation messages | **Copy list only** — manager for other formats |
| OQ-DC-C17c | Обязательность чертежей для submit? | Form validation | **Not required** — per copy v1.1 |
| OQ-DC-C17d | Max files / total size / virus scan policy? | Implementation | **Single file 10 МБ** per copy |

### 25.2 Commercial and timing

| ID | Question | Impact | Default if unresolved |
|----|----------|--------|----------------------|
| OQ-DC-C02 | Minimum order / MOQ? | FAQ, BLOCK 01 | **Exclude badge** — manager prose |
| OQ-DC-C03 | Lead time bands by complexity? | BLOCK 05, FAQ 7 | **Exclude chips** — «в КП» prose only |
| OQ-DC-C04 | Quote SLA — response time after TZ? | BLOCK 05 step 3 | **Exclude badge** — «зависит от сложности» |
| OQ-DC-C12 | Prepayment milestones for custom? | BLOCK 05 step 5 | **Link Payment** — no custom table |
| OQ-DC-C19 | Pricing factors or ranges on page? | Visual temptation | **Exclude** — factors in manager conversation only |

### 25.3 Engineering and materials

| ID | Question | Impact | Default if unresolved |
|----|----------|--------|----------------------|
| OQ-DC-C01 | Scope boundary — only neutral SS? | BLOCK 01, 03 | **Per copy v1.1** — neutral SS; thermal catalog-only |
| OQ-DC-C05 | Design owner — client vs factory vs both? | BLOCK 04, FAQ 2 | **Prose per copy** — no workflow diagram |
| OQ-DC-C06 | Revision rounds included? | FAQ | **Defer** — «в переписке и КП» |
| OQ-DC-C07 | Approval artifact before production? | BLOCK 05 gate | **КП confirmation** per copy — no sample PDF |
| OQ-DC-C08 | AISI grades / thickness policy published? | BLOCK 07 | **Exclude table** — disclaimer + КП |
| OQ-DC-C09 | Load engineering — factory calc or client TZ? | BLOCK 06 row 6 | **Prose** — clarify in согласование |
| OQ-DC-C11 | Documents delivered — passport, as-built drawing? | BLOCK 08, FAQ 4 | **Per copy** — request in КП |

### 25.4 Warranty, channel, evidence

| ID | Question | Impact | Default if unresolved |
|----|----------|--------|----------------------|
| OQ-DC-C10 | Custom warranty terms vs series? | BLOCK 08, FAQ 5 | **Link Guarantee** — no term badge |
| OQ-DC-C13 | Remake / on-site misfit policy? | FAQ 8 | **Prose per copy** — no fear design |
| OQ-DC-C15 | Dealer/integrator channel for custom? | BLOCK 10 | **One-line pointer** to Dealers |
| OQ-DC-C16 | Case studies / photo permission? | BLOCK 04 gallery | **Exclude gallery** — single production photo if supplied |
| OQ-DC-C16b | Sanitized drawings for publish? | BLOCK 06 | **Exclude thumbnails** |
| OQ-DC-C18 | Factory visit / inspection allowed? | FAQ expansion | **Defer** — not in copy v1.1 |
| OQ-DC-C20 | Catalog bridge — official «SKU X + modify» process? | BLOCK 03 | **Per copy** — artikul in form |

### 25.5 Design and implementation

| ID | Question | Impact | Default if unresolved |
|----|----------|--------|----------------------|
| OQ-DC-C21 | Value chips under lead — include? | First screen density | **Include** 3 chips OR rely on BLOCK 05 gate badge — not both heavy |
| OQ-DC-C22 | Optional parameter companion table — include? | BLOCK 06 density | **Include** at weight 2/5 if used |
| OQ-DC-C23 | Cross-links summary table at footer? | MICRO | **Optional** — lowest weight |
| OQ-DC-C24 | Legacy `.zpm-seo` — new `zpm-custom-*` namespace? | Implementation | Defer to implementation charter |
| OQ-DC-C25 | Production photo asset — reuse About or custom shoot? | BLOCK 04 | **Reuse About factory** if attested; else hide slot |
| OQ-DC-C26 | Privacy policy route `/privacy-policy` | Form consent | Verify at implementation — assumed per copy |
| OQ-DC-C27 | Dedicated `zakaz@` email vs `info@`? | Form fallback | **`info@bzpm.ru`** per copy |

---

## 26. Design readiness verdict

| Dimension | Status | Notes |
|-----------|--------|-------|
| Copy | **READY** | v1.1 complete — operator approval header pending |
| IA | **READY** | CP-01 boundaries locked; Custom = made-to-order owner |
| Charter | **READY FOR OPERATOR REVIEW** | This document |
| Assets | **PARTIAL** | No case studies, no sanitized drawings; production photo TBD (OQ-DC-C25) |
| OQ | **PARTIAL** | Upload backend, MOQ, lead bands, case permission — explicit deferrals |
| Visual design | **NOT READY** | Awaits operator charter approval |
| Implementation | **NOT READY** | Awaits design approval + implementation charter; SC-11 upload backend UNKNOWN |
| Downstream unlock | **N/A** | Custom is design order #6 — terminal corp page in program sequence |

**Verdict:** M9.18 Custom Manufacturing is **PARTIAL DESIGN READY** — charter pass complete; operator may approve charter and authorize **visual design phase** with **manufacturer-capability / process-dominant** posture, requirements checklist as practical enabler (not tender UX), form as educated endpoint, explicit SAFE UNKNOWN deferrals (no price/lead badges, no fake portfolio, no configurator), and SC-11 upload degrade path until backend confirmed.

**Program alignment:** Completes design order #6; sixth SC-04 instantiation; SC-11 primary owner locked; resolves calculator/tender/catalog conflict risks from forensic research.

**Explicit stop:** No wireframes · no mockups · no Twig/CSS/JS · no deploy.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-22 | **CREATED** — Design Charter v1; manufacturer-capability-dominant mode; process-led trust; SC-04/SC-06/SC-09/SC-11/SC-12 locks; calculator/tender/catalog drift forbiddance; file upload and asset-gap strategy; CP-01 sibling relationships; full OQ registry |

---

*BZPM M9.18 Custom Manufacturing Design Charter v1 — documentation only. No design, wireframes, mockups, or implementation authorized.*
