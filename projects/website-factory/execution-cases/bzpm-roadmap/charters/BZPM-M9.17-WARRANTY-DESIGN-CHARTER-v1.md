# BZPM M9.17 — Warranty — Design Charter v1

**Milestone:** M9.17 — Warranty / Гарантия  
**URL (TEST):** `/guarantee`  
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
| IA Map | [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](../BZPM-CORPORATE-PAGES-IA-MAP-v1.md) § M9.17 |
| Approved copy | [BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md) |
| Forensic research | [BZPM-M9.17-WARRANTY-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.17-WARRANTY-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) |
| Contacts reference surface | [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md) · [SITE-002-CONTACTS-PAGE-POLISH-V1.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-POLISH-V1.md) |
| Pattern precedent | [BZPM-M9.14-DELIVERY-DESIGN-CHARTER-v1.md](./BZPM-M9.14-DELIVERY-DESIGN-CHARTER-v1.md) · [BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md](./BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md) |

**Primary design question:** *Что произойдёт, если после покупки возникнет проблема с оборудованием?*

**Secondary design question:** *Останется ли производитель на связи после поставки?*

---

## 1. Purpose

### 1.1 Page mission

M9.17 `/guarantee` is the **primary owner of warranty and post-sale service policy** for SITE-002 — not a legal exclusions chapter, not a service-center directory, not a consumer-electronics warranty card, not a repair-company landing.

The page exists to **remove post-purchase uncertainty** for B2B equipment buyers: clarify **what happens when something breaks**, **who stays in contact**, **what documents to prepare**, and **how a claim moves from first message to resolution** — without inventing warranty months, SLAs, or channel policies the operator has not published.

Per forensic research Concept A («Service & Warranty Hub»): **process + accompaniment + document clarity**, not legal boilerplate or fear-based exclusion walls.

**Central charter constraint (from task brief):** This page does **not** exist to list warranty exclusions. Exclusions and verification cases are **supporting honesty** — never the page identity.

### 1.2 What this page is NOT

| Anti-goal | Reason |
|-----------|--------|
| Legal-document / contract chapter | Tender-grade legal text deferred to manager and supply documents |
| Exclusions-first policy page | BLOCK 04 is calm verification framing — not a warning wall |
| Service-center directory / ASC map | No attested authorized SC network (OQ-W04) |
| Repair-company aesthetics | ЗПМ is manufacturer — not third-party repair shop |
| Warranty-certificate hero | No numeric term badge without OQ-W01 unlock |
| Consumer electronics warranty style | B2B industrial equipment — not phone/tablet warranty card |
| Factory OEM tour | Production narrative → `/about` |
| Outbound shipment / TK tables | Owner: M9.14 Delivery |
| Payment / invoice mechanics | Owner: M9.15 Payment |
| Dealer program commercial terms | Owner: M9.16 Dealers |
| Custom engineering workflow | Owner: M9.18 Custom |

### 1.3 What this page IS

A **manufacturer service reassurance page**: scannable **5-step claim process** (SC-04), **document preparation checklist** (SC-06), **coverage framework without numeric term**, **calm verification cases** (not fear design), **outcome transparency** after claim, and a **single escalation path** to initiate service contact with equipment context.

---

## 2. Audience hierarchy

| Segment | Priority | What they need from design |
|---------|----------|----------------------------|
| **Закупщик / снабженец** | **Primary** | Tender/AVL posture: process exists, documents known, manufacturer reachable — without fake term months |
| **Владелец бизнеса** | **Primary** | Post-open risk reduction — «не останусь один с поломкой» |
| **Сервис / эксплуатация** | **Primary** | Claim procedure clarity — what to send, what happens next |
| **Производственник** | **Secondary** | Uptime path — who coordinates, not SC network map |
| **Дилер** | **Tertiary** | Channel routing summary + link to `/dealers` — not full partner policy here |

**Design implication:** Layout rewards **reassurance scan → process understand → documents prepare → escalate** — not legal dense prose, not exclusion anxiety, not term-badge marketing.

---

## 3. Conversion hierarchy

### 3.1 Primary

**Service claim initiation** — visitor submits **«Отправить обращение»** form (FORM) with **equipment_model** and **issue description** after understanding process and document expectations.

Success signal: buyer knows **what will happen** and **how to start** before manager call; form captures equipment identity for service routing.

**Parallel primary channel (not competing button):** Phone and email visible in BLOCK 03 step 1 and BLOCK 07 — attested service entry points per copy.

### 3.2 Secondary

**Contacts** — «Контакты» → `/contact/` when visitor needs address, requisites, or general inquiry beyond warranty scope (BLOCK 07).

### 3.3 Tertiary

**About** — «О компании и производстве» → `/about` when visitor still needs manufacturer legitimacy depth (BLOCK 07).

**Rule:** No catalog CTA on this page per approved copy v1 — conversion is **service escalation**, not SKU browsing. Tertiary links must not outrank primary form submit.

---

## 4. Trust hierarchy

Ranked by **post-purchase anxiety reduction** for equipment buyers.

| Rank | Trust signal | Source | Design role |
|------|--------------|--------|-------------|
| **T1** | **Transparent claim process** (обращение → информация → диагностика → решение → исполнение) | BLOCK 03 | Dominant visual — SC-04 timeline |
| **T2** | **Manufacturer stays in contact** — manager + specialists, not abandoned after sale | Lead; BLOCK 01; BLOCK 05 | Accompaniment framing — human service path |
| **T3** | **Document pack clarity** — what to prepare before/during claim | BLOCK 02 | SC-06 checklist — reduces friction |
| **T4** | **Coverage framework** (заводской дефект, эксплуатация по документации) | BLOCK 01 | Honest scope — **without numeric term badge** |
| **T5** | **Outcome transparency** — what buyer receives through the journey | BLOCK 05 | Predictability after escalation |
| **T6** | **Calm verification honesty** — when extra check needed, not accusatory | BLOCK 04 | Supporting — low fear visual weight |
| **T7** | **Channel routing honesty** (direct / dealer / custom) | FAQ 4–6; pointers | Links to Dealers, Custom — no fake SC map |
| **T8** | **Cert ≠ warranty disclaimer** | BLOCK 01 cert line | Prevents M9.9 misread — one line, not legal wall |
| **T9** | **Entity / production anchor** | BLOCK 01 summary row | Compact SC-03 variant — Барнаул, manufacturer |

**Explicitly subordinate (do not visual-promote without OQ unlock):**

- Warranty months badge («12 мес», «24 мес») — OQ-W01, OQ-W17
- SLA response/repair countdown chips — OQ-W06
- Authorized service center map — not attested
- Sample warranty talon thumbnail — OQ-W09
- Spare parts availability strip — OQ-W10
- Post-warranty service program badges — OQ-W12
- Replacement-guarantee chips — OQ-W08

---

## 5. Page role in buyer journey

### 5.1 Journey position

```
Catalog / PDP / PLP Commercial Trust «Гарантия производителя»
        │
        ▼
   ┌─────────┐
   │  ABOUT  │  (optional — manufacturer legitimacy)
   └────┬────┘
        │
   ┌────┴────────────────────────┐
   │                             │
   ▼                             ▼
PAYMENT                      DELIVERY
(deal documents)             (outbound logistics)
   │                             │
   └─────────────┬───────────────┘
                 │
                 ▼
          ┌─────────────┐
          │  WARRANTY   │  ◄── post-sale clarity (this page)
          └──────┬──────┘
                 │
    ┌────────────┼────────────┐
    │            │            │
    ▼            ▼            ▼
Contacts    Dealers       Custom
(fallback)  (channel)     (non-standard class)
```

### 5.2 Before this page

| Prior state | Typical entry | Page must do |
|-------------|---------------|--------------|
| Catalog trust hesitation | PLP Commercial Trust → `/guarantee` *(gap today)* | Answer «что если сломается?» without term badge |
| PDP service zone | PDP link «Условия гарантийной поддержки» | Consistent reassurance — no PDP term drift |
| Post-delivery anxiety | Delivery → Guarantee (return pointer inverse) | Separate outbound vs warranty-return logistics |
| Dealer end-client question | Dealers B09 summary → Guarantee | Authoritative depth — Dealers stays summary |
| M9.9 FAQ Q7 | «Какая гарантия и кто обслуживает?» | Primary answer surface |
| Tender / procurement file | Payment + About complete | Process + documents — not legal contract dump |

### 5.3 After this page

| Exit | When |
|------|------|
| FORM submit | Ready to report defect with model + description |
| Phone / email | Urgent breakdown; prefers voice |
| `/contact/` | General contact, requisites, directions |
| `/about` | Wants production/QC depth beyond service framing |
| `/delivery` | Outbound shipment context; RMA logistics handoff |
| `/dealers` | Purchased via partner — channel routing |
| `/custom-equipment` | Non-standard product class |
| `/payment-methods` | Deal payment docs — separate from claim |
| `/our-certification` | Conformity docs — not warranty substitute |
| PDP documents | Passport / declaration per SKU |

**Program note:** Warranty is **design order #4** — instantiates SC-04 (from Payment/Delivery), SC-06 document checklist, SC-10 form (+service fields); becomes composed summary on Dealers BLOCK 05 and PLP Commercial Trust secondary.

---

## 6. Relationship with sibling pages

CP-01 rule: **one primary owner per topic**. Warranty shows **one-line summary + text link** — never embedded foreign page body.

| Page | URL | Warranty relationship | Allowed on Warranty | Forbidden on Warranty |
|------|-----|----------------------|---------------------|----------------------|
| **About** | `/about` | Lead; BLOCK 01 pointer; CTA tertiary | Production/QC summary + link | Factory video, OEM narrative depth, cert promo gallery |
| **Payment** | `/payment-methods` | BLOCK 05 pointer | Deal payment/docs separate from claim — one line + link | Invoice/VAT, methods matrix, bank requisites |
| **Delivery** | `/delivery` | Lead; BLOCK 03 pointer; FAQ 3 | Outbound logistics + RMA handoff summary + link | TK tables, shipment points, freight model |
| **Dealers** | `/dealers` | BLOCK 02; FAQ 4; CTA microcopy | Channel routing summary + link | Discounts, territory, partner program terms |
| **Custom** | `/custom-equipment` | BLOCK 02; BLOCK 04; FAQ 5 | Non-standard class summary + link | TZ checklist, parameter matrix, upload form |
| **Contacts** | `/contact/` | BLOCK 05; BLOCK 07 tertiary | Fallback contact + requisites link | Full contact card grid, map embed duplicate |
| **Certification** | `/our-certification` | BLOCK 01 cert disclaimer | Labeled types + link — not warranty proof | Cert PDF wall |

**Warranty term badge ownership (charter lock — program blocker B2):**

| Decision | Detail |
|----------|--------|
| **Default** | **No numeric months** on page — copy SAFE UNKNOWN discipline |
| **OQ-W01 unlock** | Single operator-locked term may appear as **compact label** in BLOCK 01 — never hero badge without charter amendment |
| **OQ-W17 sync** | PDP/PLP chip must match corp page if term published — governance gate |
| **Live drift** | Work PDP «12 месяцев» vs corp page no months — **design must not invent term** |

**Contacts alignment:** FORM extends SC-10 with **equipment_model** (required), **purchase_date** (optional), **comment** (required issue description); consent, phone mask, success microcopy match delivered Contacts discipline.

---

## 7. Evidence hierarchy

### Level 1 — Must be visible without deep scroll (first ~2 viewports)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| Manufacturer accompaniment framing | H1 + Lead | SC-01 internal-page rhythm — align Contacts shell |
| **Claim process start** (steps 1–3 visible) | BLOCK 03 | SC-04 timeline — **dominant element** |
| **Coverage promise** (not exclusion) | BLOCK 01 intro + outcome table | Reassurance — manufacturer responsibility |
| Optional trust strip | MICROCOPY trust strip | 4 micro-labels — subordinate to H1+lead |
| About + Delivery links in lead | Lead | CP-01 inline — context only |

### Level 2 — Core proof stack (mid-page, scroll expected)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| Full 5-step claim process | BLOCK 03 | SC-04 timeline — complete sequence |
| Document preparation checklist | BLOCK 02 | SC-06 — outcome-first table |
| Coverage framework + summary row | BLOCK 01 | Outcome table + 4 micro-labels |
| Post-claim outcomes | BLOCK 05 | Outcome list — 6 rows |
| Verification cases (calm) | BLOCK 04 | Bulleted cases — **supporting weight** |
| Cert vs warranty disclaimer | BLOCK 01 one-line | Inline — not banner |

### Level 3 — Supporting context (lower visual weight)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| BLOCK 01 helper (term deferred to manager) | BLOCK 01 | Microcopy — no empty badge placeholder |
| Dealer / Custom pointers | BLOCK 02 body | Inline links |
| FAQ (8) | BLOCK 06 | SC-08 accordion — objection cleanup |
| Cross-links summary table | MICROCOPY optional | Footer-style link grid — lowest priority |
| Timeline note (no SLA on site) | BLOCK 03 | Prose — no countdown chips |
| Photo/video request | BLOCK 02; form helper | Text — no upload UI in MVP form |

---

## 8. Visual narrative

Narrative arc is **post-purchase accompaniment**, not legal defense or fear.

### Beginning — «Если что-то пойдёт не так — вы не один» (Utility → BLOCK 01)

| Beat | Content | Emphasis |
|------|---------|----------|
| Orient | Breadcrumb, H1, lead | SC-01 — manufacturer accompanies after purchase |
| Reassure | Lead + optional trust strip | ЗПМ принимает обращения; manager coordinates |
| **Scope** | BLOCK 01 coverage framework | What support **means** — outcome table, summary row |
| Honesty | BLOCK 01 helper + cert disclaimer | Term via manager; cert ≠ warranty |

**Beginning must answer: «Производитель останется на связи?» in <10 seconds of scan — without numeric term badge.**

### Middle — «Что подготовить и как это проходит» (BLOCK 02 → BLOCK 03)

| Beat | Content | Emphasis |
|------|---------|----------|
| Prepare | BLOCK 02 document checklist | SC-06 — **peak practical value in middle** |
| **Process** | BLOCK 03 claim timeline | **Peak visual — 5-step SC-04 path** |
| Verify | BLOCK 04 additional check cases | Calm honesty — subordinate, not warning wall |
| Receive | BLOCK 05 outcomes | What buyer gets through journey |

**Middle must answer IA Q4–Q5 (how to claim, who coordinates) without leaving page.**

### End — «Сообщите о неисправности» (BLOCK 06 → FORM)

| Beat | Content | Emphasis |
|------|---------|----------|
| Objections | BLOCK 06 FAQ | Term, dealer path, return, custom — SAFE UNKNOWN handling |
| Action | BLOCK 07 CTA + FORM | **Primary conversion zone** — service form endpoint |

**End must make «Отправить обращение» obvious; phone/email parallel support visible.**

---

## 9. Block importance map

Ranking for **all approved v1 copy blocks** (Critical / Important / Supporting).

| Block | Title | Rank | Rationale |
|-------|-------|------|-----------|
| Utility | Meta, breadcrumb | Supporting | Required shell — no visual competition |
| — | H1 + Lead | **Critical** | Post-purchase reassurance + cross-links |
| **01** | Что входит в гарантийную поддержку | **Critical** | Coverage framework — page identity (support, not exclusions) |
| **02** | Какие документы понадобятся | **Critical** | SC-06 checklist — claim readiness |
| **03** | Как происходит обращение по гарантии | **Critical** | Primary mental model — page spine |
| **04** | Когда может потребоваться дополнительная проверка | Important | Verification honesty — **must stay subordinate** |
| **05** | Что получает заказчик после обращения | Important | Outcome predictability — trust closer |
| **06** | FAQ | Important | Objection resolver — pre-CTA |
| **07** | CTA | **Critical** | Conversion band |
| FORM | Обращение по гарантии | **Critical** | Primary conversion instrument |
| MICRO | Trust strip | Important | Optional — accelerates scan if placed after lead |
| MICRO | Cross-links summary table | Supporting | Optional footer — CP-01 navigation aid |

---

## 10. Visual emphasis strategy

### 10.1 What MUST dominate visually

| Element | Why |
|---------|-----|
| BLOCK 03 SC-04 claim process (5 steps) | Answers primary question — «что произойдёт» |
| BLOCK 01 coverage outcome table + summary row | Manufacturer responsibility — not exclusion list |
| BLOCK 02 SC-06 document checklist | Practical claim readiness |
| BLOCK 07 + FORM | Conversion endpoint — service escalation |
| Lead accompaniment framing | «Останется ли производитель на связи» — immediate yes |
| BLOCK 05 outcome list | Predictability after claim |

### 10.2 What must NOT dominate visually

| Element | Why |
|---------|-----|
| BLOCK 04 verification / exclusion cases | Supporting honesty — fear-based design forbidden |
| «12 мес» / term badge | OQ-W01 — governance drift from PDP |
| SLA countdown / response-time chips | OQ-W06 — SAFE UNKNOWN |
| Authorized SC network map | Not attested |
| Red warning boxes / alert banners | Fear-based anti-pattern |
| Legal-document typography (dense articles, numbered clauses wall) | Service page, not contract |
| Warranty-certificate graphic hero | Consumer electronics anti-pattern |
| Repair-shop iconography (wrenches, hard hats as hero) | Repair-company aesthetics |
| Huge disclaimer blocks | Old live page legal boilerplate failure mode |
| BLOCK 06 FAQ as primary content | Accordion is cleanup, not hero |
| Sample talon PDF thumbnails | Operator asset required |

### 10.3 Visual weight budget (relative 1–5)

| Block | Tier | Weight | Notes |
|-------|------|--------|-------|
| **03** | Tier 1 — Anchor | **5** | Largest structured component — SC-04 owner |
| **01** | Tier 1 — Anchor | **4** | Outcome table + summary row — coverage frame |
| **02** | Tier 1 — Anchor | **4** | Document checklist — practical density |
| **07 + FORM** | Tier 1 — Anchor | **4** | CTA + form endpoint |
| **05** | Tier 2 — Support | **3** | Outcome list — 6 rows |
| **06** | Tier 2 — Support | **3** | 8-item accordion |
| **04** | Tier 2 — Support | **2** | Verification cases — **deliberately light** |
| Trust strip | Tier 2 — Support | **2** | 4 micro-labels — optional |
| Lead | Tier 1 | **3** | Sets frame — not longer than BLOCK 01 intro |
| Cross-links table | Tier 3 — Context | **1** | Optional — navigation only |

**Section rhythm:** BLOCK 04 must **not** visually compete with BLOCK 03 — verification follows process education, reads as «что может уточниться», not «почему вам откажут».

---

## 11. Warranty visualization philosophy

### 11.1 Charter decision — choose ONE dominant approach

| Approach | Verdict |
|----------|---------|
| A) Warranty term | **REJECTED as dominant** — OQ-W01 SAFE UNKNOWN; copy forbids unified months on site |
| **B) Service process** | **SELECTED — dominant** |
| C) Legal conditions | **REJECTED as dominant** — exclusions are supporting; legal wall is anti-goal |

### 11.2 Why Service process (B)

| Reason | Detail |
|--------|--------|
| Task brief | Page removes **uncertainty**, not publishes legal exclusions |
| Copy spine | BLOCK 03 is structured 5-step process — natural visual anchor |
| Program consistency | SC-04 locked on Payment (M9.15) and Delivery (M9.14) — fourth corp instantiation |
| Forensic Concept A | «Service & Warranty Hub» — process + routing + documents |
| SAFE UNKNOWN discipline | Process steps carry honesty without inventing term months or SLA chips |
| Anti-pattern avoidance | Legal/exclusion-first layout matches **failed live page** (generic boilerplate) |
| Secondary question | «Останется ли производитель на связи» — answered by **visible steps + outcomes**, not certificate |

### 11.3 Supporting roles (non-dominant)

| Approach | Role on page |
|----------|--------------|
| Warranty term | BLOCK 01 helper prose + FAQ 1 — **text only** until OQ-W01 unlock |
| Legal conditions | BLOCK 04 calm bullet list — **supporting**; cert disclaimer one-line in BLOCK 01 |

**Forbidden as visual spine:** Term badge hero, exclusions wall, legal article numbering, warranty certificate mockup.

---

## 12. Support model strategy

### 12.1 How support should be perceived

| Dimension | Design posture |
|-----------|----------------|
| **Actor** | **Manufacturer** (ООО ЗПМ) — manager + factory specialists — not anonymous call center |
| **Relationship** | **Accompaniment** after purchase — «проведём от обращения до решения» |
| **Channel honesty** | Direct, dealer, custom paths acknowledged — **no fake unified SC network** |
| **Tone** | Calm, operational, respectful — especially in BLOCK 04 verification |
| **Escalation** | Multiple entry points (phone, email, form) — **equal legitimacy**, form is primary designed CTA |
| **Anti-model** | Third-party repair shop, insurance claim adversarial UX, consumer RMA portal clone |

### 12.2 Visual language for support model

| Element | Treatment |
|---------|-----------|
| BLOCK 01 summary row | SC-03 variant — Производитель · Барнаул · Заводской дефект · Сопровождение |
| BLOCK 03 steps | Equal-weight SC-04 — manager visible in steps 1–2 |
| BLOCK 05 outcomes | Status communication emphasis — «промежуточные статусы», «объяснение решения» |
| Icons | Generic process icons — **not** repair-shop wrench hero, **not** legal scale |
| People photography | **Exclude** unless operator provides real service team/workshop photo |
| Dealer/custom pointers | Inline text links — no channel diagram until OQ-W04/W05 resolved |

### 12.3 Service geography

| Decision | Detail |
|----------|--------|
| SC map | **FORBIDDEN** — OQ-W15 SAFE UNKNOWN |
| Remote diagnostics | BLOCK 03 step 3 prose — «формат обсуждается» |
| Return logistics | FAQ 3 + Delivery link — individual agreement, not table |

---

## 13. Documents strategy

### 13.1 Role of documents on page

Documents are **claim enablers**, not legal intimidation. BLOCK 02 answers: «Что подготовить, чтобы нас услышали быстрее» — practical checklist, not compliance trap.

### 13.2 Visual importance

| Parameter | Decision |
|-----------|----------|
| Pattern | **SC-06 document checklist** — «что подготовить» + «зачем это нужно» |
| Layout | Responsive table → stacked rows ≤1024px |
| Visual weight | **Tier 1 (4/5)** — important but **subordinate to BLOCK 03 process (5/5)** |
| Placement | **Before** BLOCK 03 in copy order — prepare then proceed — design may visually bridge with connector microcopy |
| Sample talon / redacted docs | **FORBIDDEN** unless operator provides (OQ-W09) |
| Thumbnails | **FORBIDDEN** — text checklist only |
| PDP passport link | Helper text — link pattern to catalog docs zone |

### 13.3 Hierarchy within BLOCK 02

| Sub-block | Visual weight |
|-----------|---------------|
| Outcome-first checklist (6 rows) | **Dominant within BLOCK 02** |
| Body (lost docs reassurance) | Supporting prose — reduces anxiety |
| Dealer / Custom pointers | Inline links — tertiary |
| Photo/video note | Microcopy — no upload field in MVP form |

### 13.4 Should documents dominate?

| Decision | **Important — not page-wide dominant** |
|----------|----------------------------------------|
| Rationale | Documents **enable** the process — BLOCK 03 remains spine |
| Treatment | Checklist reads as «подготовка к шагу 2» of timeline — visual affinity to SC-04 step 2 |

---

## 14. Exclusions strategy

### 14.1 How exclusions should be shown

| Principle | Design rule |
|-----------|-------------|
| **Framing** | BLOCK 04 title: «дополнительная проверка» — not «когда гарантия не действует» (live page anti-pattern) |
| **Tone** | Calm framing note per copy — «обычная практика, а не отказ в лоб» |
| **Visual** | Simple bullet list — **no** red boxes, **no** warning icons, **no** «ВНИМАНИЕ» banners |
| **Weight** | Tier 2 (2/5) — **lowest** among content blocks |
| **Position** | **After** BLOCK 03 process — user understands path before edge cases |
| **Length** | Copy-provided 7 bullets — do not expand |
| **Post-warranty path** | One calm sentence — «платный ремонт если доступен» — no fear |

### 14.2 Should exclusions dominate?

| Decision | **NO — explicitly forbidden** |
|----------|-------------------------------|
| Rationale | Task brief: page does **not** exist to list exclusions |
| Live failure | Old page led with «Когда гарантия не действует» — **do not replicate hierarchy** |
| Competitive contrast | Abat maintenance/void conditions are explicit — ZPM copy chose calm verification framing instead |

### 14.3 Relationship to BLOCK 01 coverage

| Rule | Detail |
|------|--------|
| BLOCK 01 | States what support **includes** — positive frame |
| BLOCK 04 | States when **extra verification** may apply — negative cases without adversarial design |
| No duplicate | Exclusion bullets live **only** in BLOCK 04 — not repeated in BLOCK 01 table |

---

## 15. FAQ strategy

### 15.1 Role

FAQ is **objection resolver** for warranty edge cases — not primary education (BLOCK 01–05 own that).

### 15.2 Parameters

| Parameter | Decision |
|-----------|----------|
| Count | **8 items** — per approved copy; do not expand |
| Pattern | SC-08 single-open accordion |
| Position | After BLOCK 05, before BLOCK 07 |
| Visual weight | Important — **subordinate** to BLOCK 03 and BLOCK 02 |

### 15.3 Priority items (mobile density)

| Priority | FAQ | Why |
|----------|-----|-----|
| 1 | Срок гарантии? | Core Q1 — honest SAFE UNKNOWN, no badge in header |
| 2 | Какие документы? | Core Q2 — pointer to BLOCK 02 |
| 3 | Нужно ли везти на завод? | Core Q6 + Delivery link |
| 4 | Купил у дилера — куда? | Core channel routing |
| 5–8 | Remaining | Custom, who repairs, replace vs repair, start date |

### 15.4 Overlap discipline

FAQ must **not repeat** full BLOCK 03 timeline or BLOCK 02 checklist — short confirmatory answers with links to owners (Dealers, Delivery, Custom).

### 15.5 Forbidden FAQ patterns

- Accordion headers with «12 мес» chip
- Red «не гарантируется» labels in questions
- Embedded exclusion wall in answers
- SC map thumbnails

---

## 16. CTA strategy

### 16.1 Hierarchy (locked per copy v1)

| Priority | Element | Placement |
|----------|---------|-----------|
| **Primary** | «Отправить обращение» → form submit | BLOCK 07 + FORM only |
| **Secondary** | «Контакты» → `/contact/` | BLOCK 07 — subordinate |
| **Tertiary** | «О компании и производстве» → `/about` | BLOCK 07 — subordinate |
| **Support** | Phone `8 (3852) 72-18-90` · `info@bzpm.ru` | BLOCK 07 inline + BLOCK 03 step 1 |

**Note:** Copy v1 has no catalog secondary CTA — service page conversion stays **claim-focused**.

### 16.2 One CTA or multiple?

| Decision | **One primary button zone per page** |
|----------|--------------------------------------|
| Mid-page buttons | **FORBIDDEN** — no «Отправить обращение» before BLOCK 07 |
| Text links | Permitted in lead, process steps, BLOCK 02–05 — not button-styled |
| Phone as parallel CTA | Visible in BLOCK 07 and step 1 — support, not competing primary button |

### 16.3 Placement philosophy

CTA band **after FAQ** — user has consumed coverage, documents, process, verification honesty, outcomes, and residual objections.

FORM immediately follows CTA band (or integrated in same visual zone per SC-09).

**Micro pointer under CTA body:** Dealers — text link for partner channel (copy-provided).

---

## 17. Form strategy

### 17.1 Role

FORM is the **service claim intake instrument** — captures **equipment identity** and **defect description** for manager routing; not a generic callback form.

### 17.2 Relationship to Contacts

| Aspect | Warranty FORM | Contacts form |
|--------|---------------|---------------|
| Purpose | Warranty / defect report | General inquiry + requisites discovery |
| Unique fields | **equipment_model** (required), **purchase_date** (optional), **comment** (required — issue description) | No service fields |
| Shared | name, phone, email, consent, privacy link, submit states | SC-10 base |
| Photo upload | **Not in MVP form** — helper says manager requests after contact (OQ-W14) | — |
| Serial number | **Not separate field** — may appear in comment per copy | — |
| Success microcopy | Manager callback пн–пт 9–18 Барнаул | Same discipline |

### 17.3 Rules

| Rule | Detail |
|------|--------|
| Do not duplicate Contacts contact card grid above form | BLOCK 07 phone/email + summary row suffice |
| Do not embed photo upload without backend | OQ-W14 deferred — text-only MVP |
| **equipment_model** field prominence | Visually emphasized — service routing identity |
| purchase_date | Optional — reduces friction; helper explains |
| Backend | **SAFE UNKNOWN** — same `action="#"` posture as Contacts until implementation charter |
| Global modals | Do **not** substitute for dedicated form — live page failure mode |

### 17.4 Form scope creep guard (OQ-W14)

| MVP fields (locked) | Deferred unless operator unlocks |
|---------------------|----------------------------------|
| name, phone, email, equipment_model, purchase_date, comment, consent | serial_number field, photo upload, dealer_name, invoice_number |

---

## 18. Design risks

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R1 | **Term badge temptation** (PDP work copy «12 мес», Kroner benchmark) | **High** | No months without OQ-W01/W17; FAQ 1 prose only |
| R2 | **Exclusion wall drift** — BLOCK 04 visually dominates | **High** | §14 weight cap (2/5); calm framing mandatory |
| R3 | Live `/guarantee` generic `.zpm-seo` flat prose | **High** | New corp block system — process spine |
| R4 | **Claim drift** PLP / PDP / corp page inconsistent term | **Critical** | OQ-W17 governance; no invented badge |
| R5 | Form scope creep (serial, photo upload) | **Medium** | §17.4 MVP lock |
| R6 | Repair-company / SC directory aesthetic | **Medium** | Manufacturer service language only |
| R7 | Legal-document appearance (dense clauses) | **Medium** | Service page mode — H2 section discipline |
| R8 | Fear-based red warning boxes | **Medium** | Forbidden patterns §19 |
| R9 | Duplicate SC-04 fatigue vs Payment/Delivery | **Low** | 5 warranty-specific steps — shared component, distinct labels |
| R10 | Dealer channel FAQ without policy (OQ-W05) | **Medium** | Neutral copy — links to Dealers |
| R11 | Cert vs warranty confusion (M9.9) | **Medium** | BLOCK 01 disclaimer — one line |
| R12 | BLOCK 02 + FAQ 2 document overlap | **Low** | FAQ points to BLOCK 02 — no duplicate table |
| R13 | Long page (7 blocks + form) scroll fatigue | **Medium** | Tier weight map; section spacing |
| R14 | Production URL parity unknown (OQ-W20) | **Low** | Document at implementation |
| R15 | Trust strip + BLOCK 01 summary row duplicate | **Medium** | Use one or the other — not both heavy |

---

## 19. Forbidden patterns

| Pattern | Why forbidden |
|---------|---------------|
| **Legal-document appearance** — dense numbered articles, contract typography | Service reassurance page — not legal registry |
| **Huge disclaimer blocks** | Old live boilerplate; kills reassurance arc |
| **Red warning boxes** / alert banners on exclusions | Fear-based design — task brief forbids |
| **Fear-based design** — «гарантия аннулирована», skull icons, aggressive red | B2B accompaniment anti-pattern |
| **Service-center directory** / ASC map | Not attested (OQ-W04) |
| **Repair-company aesthetics** — wrench hero, workshop stock as identity | Manufacturer owns service coordination |
| **Warranty-card hero** — certificate graphic above fold | Consumer electronics style |
| **Consumer electronics warranty style** — term sticker, serial barcode scan UI | Industrial B2B equipment |
| **«12 мес» / term badge** without OQ-W01 unlock | Governance drift (R1, R4) |
| SLA countdown / response-time chips | OQ-W06 SAFE UNKNOWN |
| Sample talon PDF gallery | Operator asset required |
| Factory OEM video / story | Owner: About |
| TK / outbound shipment tables | Owner: Delivery |
| Invoice/VAT / bank detail | Owner: Payment / Contacts |
| Dealer discount / territory | Owner: Dealers |
| Custom TZ / parameter matrix | Owner: Custom |
| Multiple primary CTA buttons mid-page | §16.2 |
| Global modal as only claim path | Live page failure — dedicated form required |
| Autoplay process animation | UX noise + reduced-motion |
| Exclusion-first page hierarchy (H2 «когда не действует» above process) | Live page anti-pattern |
| ПП №719 / «Сделано в России» as warranty substitute | M9.9 semantics — disclaimer only |
| SKU grid or product cards | Owner: Catalog |

---

## 20. Success criteria

Operator judges Warranty design **successful** when:

| # | Criterion | Verification method |
|---|-----------|---------------------|
| S1 | Visitor answers central question: **что произойдёт, если сломается** | Operator scenario test |
| S2 | Secondary question answered: **производитель останется на связи** | Lead + BLOCK 01 + BLOCK 05 review |
| S3 | BLOCK 03 process scannable in **<20 seconds** desktop | Operator scan test |
| S4 | Page does **not** read as legal exclusions chapter or repair directory | Operator visual compare vs live `/guarantee` |
| S5 | BLOCK 04 verification visible but **subordinate** — no fear design | Design review |
| S6 | No numeric warranty months unless OQ-W01 unlocked | Governance check |
| S7 | No CP-01 violations — sibling topics are links only | Cross-link audit |
| S8 | FORM includes **equipment_model** + issue **comment**; consent matches Contacts | Side-by-side with `/contact/` |
| S9 | SC-04 / SC-06 / SC-08 / SC-10 variants instantiated per program registry | Design program check |
| S10 | One primary CTA zone — no mid-page submit | Design review |
| S11 | Mobile ≤1024px — checklist and process stack without horizontal scroll trap | Responsive check |
| S12 | PLP Commercial Trust «Гарантия производителя» target designed consistently | Catalog secondary doc |
| S13 | Design charter approved **before** wireframe/mockup work | Phase gate |
| S14 | Exclusions do **not** dominate visual hierarchy | Weight budget audit §10.3 |

---

## 21. Special requirement resolutions

### 21.1 Page feel — A / B / C

| Mode | Verdict |
|------|---------|
| A) Legal page | **REJECTED as dominant** — legal facts are supporting only |
| **B) Service page** | **SELECTED** |
| C) Warranty certificate | **REJECTED** — no certificate hero; term deferred to manager |

**Service page means:** operational accompaniment after purchase — visible process, document preparation, human contact path — visual language aligned with Payment/Delivery **operational corp mode**, not legal registry or consumer warranty card.

### 21.2 Should warranty duration dominate?

| Decision | **NO** |
|----------|--------|
| Rationale | OQ-W01 SAFE UNKNOWN; copy explicitly defers term to manager |
| Treatment | BLOCK 01 helper + FAQ 1 — prose only |
| OQ-W01 unlock | Compact text label in BLOCK 01 summary area — **never hero badge** without charter amendment |

### 21.3 Should exclusions dominate?

| Decision | **NO — explicitly forbidden** |
|----------|-------------------------------|
| Treatment | BLOCK 04 at weight 2/5; calm «дополнительная проверка» framing |
| Forbidden | Exclusion-first hierarchy, red warnings, «когда не действует» as H2 above process |

### 21.4 Should support process dominate?

| Decision | **YES — primary visual anchor** |
|----------|--------------------------------|
| BLOCK 03 | Highest visual weight (5/5) |
| Shared pattern | SC-04 — fourth corp instantiation after Payment, Delivery |

### 21.5 Should documents dominate?

| Decision | **Important — subordinate to process** |
|----------|----------------------------------------|
| BLOCK 02 weight | Tier 1 (4/5) — **below** BLOCK 03 (5/5) |
| Role | Enables step 2 of process — checklist, not page identity |

### 21.6 Trust strip placement

| Element | Placement decision |
|---------|-------------------|
| Trust strip (4 badges) | **Optional** — after lead, before BLOCK 01 |
| BLOCK 01 summary row (4 labels) | **Recommended** — within BLOCK 01 |
| Both together | **Avoid heavy duplication** — if trust strip used, summary row stays inline in BLOCK 01 without second badge row |

### 21.7 Shared components instantiated on Warranty

| ID | Component | Warranty blocks |
|----|-----------|----------------|
| SC-01 | Corp page shell | All |
| SC-03 | Trust row | BLOCK 01 summary row; optional MICRO trust strip |
| SC-04 | Process timeline | BLOCK 03 |
| SC-06 | Document checklist | BLOCK 02 |
| SC-07 | Matrix table | BLOCK 01 outcome table (variant) |
| SC-08 | FAQ accordion | BLOCK 06 |
| SC-09 | CTA band | BLOCK 07 |
| SC-10 | Corp inquiry form | FORM (+equipment_model variant) |
| SC-12 | Cross-link inline | Lead, body, CTA pointers |

**Warranty is primary owner** for service-claim form variant (SC-10 + equipment fields) — Dealers and Custom use different form extensions.

---

## 22. Open questions (operator lock)

| ID | Question | Impact | Default if unresolved |
|----|----------|--------|----------------------|
| OQ-DC-W01 | Publish warranty months on page? (OQ-W01) | BLOCK 01, PLP, PDP | **No numeric term** — manager prose |
| OQ-DC-W02 | PDP/PLP chip sync if term published (OQ-W17) | Cross-surface | **No chip** until unified operator lock |
| OQ-DC-W03 | Trust strip after lead — include? | First screen density | **Include** 4 micro-labels OR rely on BLOCK 01 summary row — not both heavy |
| OQ-DC-W04 | Redacted warranty talon sample (OQ-W09) | BLOCK 02 | **Exclude** — checklist text only |
| OQ-DC-W05 | Photo upload in form (OQ-W14) | FORM | **Exclude** — manager requests after contact |
| OQ-DC-W06 | Serial number dedicated field (OQ-W14) | FORM | **Exclude** — comment field sufficient |
| OQ-DC-W07 | Service model diagram — factory vs dealer (OQ-W04/W05) | BLOCK 01 / FAQ | **Prose + links** — no diagram |
| OQ-DC-W08 | PLP Commercial Trust link to `/guarantee` — design now? | Catalog secondary | **Defer** — documentation parallel |
| OQ-DC-W09 | Dedicated service email vs info@ (OQ-W13) | CTA | **info@bzpm.ru** per copy |
| OQ-DC-W10 | Legacy `.zpm-seo` guarantee page — new `zpm-warranty-*` namespace? | Implementation | Defer to implementation charter |
| OQ-DC-W11 | Cross-links summary table at page footer — include? | MICRO | **Optional** — lowest weight |
| OQ-DC-W12 | Privacy policy route `/privacy-policy` | Form consent | Verify at implementation — assumed per copy |

---

## 23. Design readiness verdict

| Dimension | Status | Notes |
|-----------|--------|-------|
| Copy | **READY** | v1 complete — operator approval header pending |
| IA | **READY** | CP-01 boundaries locked; Warranty = service policy owner |
| Charter | **READY FOR OPERATOR REVIEW** | This document |
| Assets | **PARTIAL** | No talon sample, no SC map; structural SC-04/SC-06 sufficient |
| OQ | **PARTIAL** | OQ-W01/W17 affect term visuals — explicit deferrals; form MVP locked |
| Visual design | **NOT READY** | Awaits operator charter approval |
| Implementation | **NOT READY** | Awaits design approval + implementation charter |
| Downstream unlock | **PARTIAL** | SC-04 process + SC-10 service form for Dealers composition; PLP trust link doc |

**Verdict:** M9.17 Warranty is **PARTIAL DESIGN READY** — charter pass complete; operator may approve charter and authorize **visual design phase** with **service-page / process-dominant** posture, document checklist as practical support, exclusions subordinate and calm, and explicit SAFE UNKNOWN deferrals (no term badge, no SLA chips, no SC map, no photo upload in MVP form).

**Program alignment:** Resolves design order #4; reuses SC-04/SC-06 from Payment/Delivery charters; prepares Dealers BLOCK 05 warranty summary composition.

**Explicit stop:** No wireframes · no mockups · no Twig/CSS/JS · no deploy.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-22 | **CREATED** — Design Charter v1; service-process-dominant visualization; service-page mode; exclusions/documents/term dominance resolutions; support model and document strategies; fear-based pattern forbiddance; CP-01 sibling relationships; form MVP scope |

---

*BZPM M9.17 Warranty Design Charter v1 — documentation only. No design, wireframes, mockups, or implementation authorized.*
