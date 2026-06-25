# BZPM M9.15 — Payment — Design Charter v1

**Milestone:** M9.15 — Payment / Оплата  
**URL (TEST):** `/payment-methods`  
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
| IA Map | [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](../BZPM-CORPORATE-PAGES-IA-MAP-v1.md) § M9.15 |
| Approved copy | [BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md) |
| Forensic research | [BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](../../../ocpilot/sites/site-002/reports/BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) |
| Contacts reference surface | [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md) · [SITE-002-CONTACTS-PAGE-POLISH-V1.md](../../../ocpilot/sites/site-002/reports/SITE-002-CONTACTS-PAGE-POLISH-V1.md) |
| Pattern precedent | [BZPM-M9.13-ABOUT-COMPANY-DESIGN-CHARTER-v1.md](./BZPM-M9.13-ABOUT-COMPANY-DESIGN-CHARTER-v1.md) |

**Primary design question:** *Как происходит оплата и какие документы я получу?*

**Secondary design question:** *Можно ли безопасно работать с этим поставщиком как юридическое лицо?*

---

## 1. Purpose

### 1.1 Page mission

M9.15 `/payment-methods` is the **primary owner of B2B payment and settlement mechanics** for SITE-002 — not a payment gateway page, not a bank requisites dump, not a checkout explainer dressed as ecommerce.

The page exists to **remove financial uncertainty** for procurement buyers: clarify the **invoice-led path**, the **document trail**, and the **post-payment handoff** — without inventing commercial terms the operator has not published.

Per forensic research Concept A (B2B Payment Process Hub) with embedded proof layer: **process + proof**, not requisites alone.

### 1.2 What this page is NOT

| Anti-goal | Reason |
|-----------|--------|
| Consumer ecommerce checkout / card payment landing | Catalog is quote-led; runtime checkout = `cod`, `free_checkout` only |
| Bank requisites reference sheet | Primary bank block owner is Contacts **or** operator charter (OQ-P01) — not default hero |
| Legal contract / tender compliance chapter | Contract depth deferred to manager; no fake legal wall |
| Duplicate of Delivery logistics | Ship-after-pay is summary + link only |
| Dealer commercial terms page | Channel payment → `/dealers` one line |
| Factory trust story | Entity proof is compact row — depth on `/about` |
| SKU pricing or cart UX | Owner: Catalog / PDP |

### 1.3 What this page IS

An **operational clarity page** for B2B settlement: scannable **6-step process**, honest **methods posture** (безнал primary; no online card in catalog), **document checklist** for бухгалтерия, and a **single escalation path** to request счёт / КП.

---

## 2. Audience hierarchy

| Segment | Priority | What they need from design |
|---------|----------|----------------------------|
| **Закупщик / финконтроль** | **Primary** | ERP onboarding: юрлицо, документы, НДС posture (without fake %), счёт path |
| **Снабженец** | **Primary** | Invoice gates, prepayment framework, ship-after-pay clarity, multi-SKU RFQ flow |
| **Владелец бизнеса** | **Secondary** | End-to-end path without opaque B2B; no online-pay false promise |
| **Дилер / оптовик** | **Tertiary** | Pointer to channel terms — not full payment policy here |

**Design implication:** Layout rewards **process scan → methods confirm → documents verify → escalate** — not financial marketing or legal dense prose.

---

## 3. Conversion hierarchy

### 3.1 Primary

**Invoice / КП request** — visitor submits **«Запросить счёт или КП»** form (FORM) with **organization** field after consuming process + documents proof.

Success signal: procurement user understands path **before** call; form captures payer identity for manager routing.

### 3.2 Secondary

**Catalog exploration** — «Перейти в каталог» when buyer needs SKU selection before RFQ (BLOCK 07).

### 3.3 Tertiary

**Contacts / requisites verification** — «Контакты и реквизиты» → `/contact/` for ИНН/КПП/address when vendor card build is the immediate need.

**Rule:** Tertiary visible in CTA band but **must not** outrank primary form submit.

---

## 4. Trust hierarchy

Ranked by **procurement decision weight** for payment anxiety reduction.

| Rank | Trust signal | Source | Design role |
|------|--------------|--------|-------------|
| **T1** | **Transparent B2B process** (заявка → КП → счёт → оплата → подтверждение → отгрузка) | BLOCK 01 | Dominant visual — SC-04 timeline |
| **T2** | **Invoice-led model; no online card checkout in catalog** | BLOCK 01 helper; BLOCK 02 note | Visible early — anti-mismatch with runtime |
| **T3** | **Document trail** (КП, счёт, закрывающие, отгрузочные) | BLOCK 04 | SC-06 checklist — procurement proof |
| **T4** | **Entity legitimacy** (ООО ЗПМ, ИНН) | BLOCK 04 H3; entity trust row | Compact — link to Contacts for depth |
| **T5** | **Manager accompaniment** | Lead; BLOCK 03; FAQ | Human escalation — not SLA chips |
| **T6** | **Post-payment visibility** (what happens after pay) | BLOCK 03 | Bridges anxiety gap before Delivery |
| **T7** | **Cross-page honesty** (Delivery, Dealers, Custom pointers) | Lead; BLOCK 07 microcopy | CP-01 links — not embedded foreign bodies |

**Explicitly subordinate (do not visual-promote without OQ unlock):**

- НДС 20% numeric badge (OQ-P02)
- Bank р/с / БИК table (OQ-P01)
- Prepayment % chips (OQ-P03)
- Invoice validity day countdown (OQ-P04)
- Deferral / отсрочка tiers (OQ-P05)

---

## 5. Page role in B2B journey

### 5.1 Journey position

```
Catalog RFQ / Commercial Trust «документы для закупки»
        │
        ▼
   ┌─────────┐
   │  ABOUT  │  (optional — entity trust first)
   └────┬────┘
        │
        ▼
   ┌─────────┐
   │ PAYMENT │  ◄── settlement clarity (this page)
   └────┬────┘
        │
   ┌────┴────────────┐
   │                 │
   ▼                 ▼
DELIVERY          Contacts
(ship after pay)  (ИНН / vendor card)
        │
        ▼
   Custom / Dealers
   (scenario branches)
```

### 5.2 Before this page

| Prior state | Typical entry | Page must do |
|-------------|---------------|--------------|
| Catalog hesitation | PLP/PDP → header «Оплата» | Confirm B2B безнал path |
| About trust established | About → Payment | Skip factory story — go operational |
| Delivery research | Delivery link back | Reinforce pay-before-ship without duplicating TK tables |
| Tender / vendor card build | Search «реквизиты ЗПМ» | Entity facts + Contacts link — not full bank wall by default |

### 5.3 After this page

| Exit | When |
|------|------|
| FORM submit | Ready to request счёт / КП with organization named |
| `/delivery` | Needs ship points, TK, pickup after payment understood |
| `/contact/` | Needs ИНН/КПП panel, map, general contact |
| `/dealers` | Channel payment terms |
| `/custom-equipment` | Custom prepayment / milestone questions |
| `/about` | Still unsure about manufacturer legitimacy |
| `/` catalog | SKU selection before RFQ |
| Phone / email | Urgent invoice or VAT clarification |

**Program note:** Payment is **design order #2** — locks SC-04 process timeline, SC-06 document checklist, SC-07 methods matrix, entity trust row for Delivery, Custom, Dealers, Warranty reuse.

---

## 6. Relationship with sibling pages

CP-01 rule: **one primary owner per topic**. Payment shows **one-line summary + text link** — never embedded foreign page body.

| Page | URL | Payment relationship | Allowed on Payment | Forbidden on Payment |
|------|-----|---------------------|-------------------|---------------------|
| **About** | `/about` | BLOCK 05 one-line pointer | «Кто производит» summary + link | Factory video, OEM narrative, cert promo depth |
| **Delivery** | `/delivery` | Lead; BLOCK 01 step 6; BLOCK 03; BLOCK 07 pointer | Ship-after-pay; handoff link | TK tables, regional freight, warehouse address conflict detail |
| **Warranty** | `/guarantee` | Microcopy pointer only | One-line «Гарантия» link | Term badge, RMA process, SLA |
| **Dealers** | `/dealers` | BLOCK 02 H3; BLOCK 05 row; FAQ 5; CTA pointer | «Канальные условия» one line + link | Discounts, deferral framework, territory |
| **Custom** | `/custom-equipment` | BLOCK 01 step 2; BLOCK 03; FAQ 6 | Custom prepayment summary + link | TZ checklist, parameter matrix, upload form |
| **Contacts** | `/contact/` | Lead; BLOCK 04 H3; entity row; CTA tertiary | ИНН/КПП/ОГРН summary + link | Full contact card grid, map embed, messenger row |
| **Certification** | `/our-certification` | — | Not primary on Payment | Cert PDF gallery |

**Bank requisites ownership (charter lock):**

| Decision | Detail |
|----------|--------|
| **Default** | **Contacts** owns published ИНН/КПП/ОГРН; **bank р/с in invoice** or on request |
| **Payment BLOCK 04** | Lists entity facts for vendor card + **link to Contacts** — not duplicate bank table |
| **OQ-P01 unlock** | If operator publishes full bank on-site — **one canonical surface** only; other page links |

**Contacts alignment:** Form extends SC-10 with **company** field (required); consent, phone mask, success microcopy match delivered Contacts discipline.

---

## 7. Evidence hierarchy

### Level 1 — Must be visible without deep scroll (first ~2 viewports)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| B2B invoice-led positioning | Lead + BLOCK 01 helper | H1 zone + lead — typographic clarity |
| **6-step payment process** (abbreviated scan) | BLOCK 01 | SC-04 timeline — **dominant element** |
| **No online card checkout** | BLOCK 02 note; BLOCK 01 helper | Visible in first screen or top of BLOCK 02 — not FAQ-only |
| Optional trust strip | MICROCOPY trust strip | 4 micro-labels after lead — **subordinate to process** |

### Level 2 — Core proof stack (mid-page, scroll expected)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| Payment methods matrix / summary table | BLOCK 02 | SC-07 table → stacked cards ≤1024px |
| Post-payment chain | BLOCK 03 | Compact **4-row chain** — not second full timeline |
| Document checklist | BLOCK 04 | SC-06 — outcome-first table/checklist |
| Entity trust row | MICROCOPY entity row | SC-03 variant — 4 labels, link to Contacts |
| ИНН/КПП/ОГРН for vendor card | BLOCK 04 H3 | Structured fact list — not requisites panel clone |

### Level 3 — Supporting context (lower visual weight)

| Evidence | Copy source | Visual commitment |
|----------|-------------|-------------------|
| Audience segment matrix | BLOCK 05 | SC-13 grid — lighter than BLOCK 02 |
| FAQ (8) | BLOCK 06 | SC-08 accordion — objection cleanup |
| Dealer / Custom / Delivery pointers | Body microcopy | Inline links only |
| ЭДО note | BLOCK 04 helper | Text — no operator logo |
| Reassurance note (order changes) | BLOCK 03 | Microcopy — low emphasis |

---

## 8. Visual narrative

Narrative arc is **operational certainty**, not financial persuasion.

### Beginning — «Как у вас устроена оплата?» (Utility → BLOCK 01)

| Beat | Content | Emphasis |
|------|---------|----------|
| Orient | Breadcrumb, H1, lead | SC-01 internal-page rhythm — align Contacts shell |
| Position | Lead + optional trust strip | B2B безнал; manager-led; links to Contacts + Delivery |
| **Mental model** | BLOCK 01 process timeline | **Peak visual — 6 equal-weight steps** |
| Anti-checkout | BLOCK 01 helper text | Catalog = RFQ, not card pay |

**Beginning must answer: «Это нормальный B2B-счёт или серый перекуп?» in <10 seconds of scan.**

### Middle — «Чем платить и что получу на бумагах?» (BLOCK 02 → BLOCK 04)

| Beat | Content | Emphasis |
|------|---------|----------|
| Methods | BLOCK 02 matrix + H3 sections | Безнал primary; FL/dealer honest subordination |
| After pay | BLOCK 03 chain | Closes «чёрный ящик» — link to Delivery |
| Documents | BLOCK 04 checklist + requisites H3 | Procurement file — **peak proof density in middle** |
| Entity | Entity trust row (placement: after BLOCK 04 or with lead) | Compact verification |

**Middle must answer IA Q1–Q4, Q7 without leaving page (except bank depth on Contacts).**

### End — «Запросите счёт» (BLOCK 05 → FORM)

| Beat | Content | Emphasis |
|------|---------|----------|
| Fit | BLOCK 05 audience | Segmentation — who invoice model serves |
| Objections | BLOCK 06 FAQ | VAT, deferral, partial pay — honest SAFE UNKNOWN handling |
| Action | BLOCK 07 CTA + FORM | **Primary conversion zone** — form is visual endpoint |

**End must make «Запросить счёт или КП» obvious; phone/email support visible.**

---

## 9. Block importance map

Ranking for **all approved v1 copy blocks** (Critical / Important / Supporting).

| Block | Title | Rank | Rationale |
|-------|-------|------|-----------|
| Utility | Meta, breadcrumb | Supporting | Required shell — no visual competition |
| — | H1 + Lead | **Critical** | B2B positioning + cross-links |
| **01** | Как проходит оплата заказа | **Critical** | Primary mental model — page spine |
| **02** | Какие способы оплаты доступны | **Critical** | Methods truth + no-online-card clarity |
| **03** | Что происходит после оплаты | **Important** | Anxiety bridge to Delivery |
| **04** | Какие документы получает заказчик | **Critical** | Procurement / бухгалтерия proof |
| **05** | Для кого подходит такой формат | Supporting | Audience matrix — segmentation |
| **06** | FAQ | Important | Objection resolver — pre-CTA |
| **07** | CTA | **Critical** | Conversion band |
| FORM | Запрос счёта | **Critical** | Primary conversion instrument |
| MICRO | Trust strip | Important | Optional — accelerates scan if placed after lead |
| MICRO | Entity trust row | Important | Compact legitimacy — subordinate to process |

---

## 10. Visual emphasis strategy

### 10.1 What MUST dominate visually

| Element | Why |
|---------|-----|
| BLOCK 01 SC-04 process timeline (6 steps) | Answers primary question — «как происходит оплата» |
| BLOCK 02 «безнал по счёту» + summary table | Confirms default B2B instrument |
| «Нет онлайн-оплаты в каталоге» clarification | Prevents checkout expectation mismatch (G-P01) |
| BLOCK 04 document checklist | Answers «какие документы» |
| BLOCK 07 + FORM | Conversion endpoint |
| BLOCK 03 post-payment chain | Reduces post-pay uncertainty |

### 10.2 What must NOT dominate visually

| Element | Why |
|---------|-----|
| Full bank requisites table | OQ-P01 locked; Contacts or invoice owns |
| НДС 20% badge | OQ-P02 — forbidden without unlock |
| Credit card icons / payment logos | Consumer ecommerce anti-pattern |
| BLOCK 05 audience matrix | Supporting segmentation only |
| BLOCK 02 FL / dealer H3 sections | Honest but subordinate paths |
| Promo banners / discount emphasis | Not B2B settlement page |
| Fake finance icons (Visa/Mastercard wall) | Misleading — no gateway |
| Repeated «менеджер уточнит» without structure | Old live page failure mode |
| BLOCK 06 FAQ as primary content | Accordion is cleanup, not hero |

### 10.3 Visual weight budget (relative 1–5)

| Block | Tier | Weight | Notes |
|-------|------|--------|-------|
| **01** | Tier 1 — Anchor | **5** | Largest structured component on page |
| **02** | Tier 1 — Anchor | **4** | Table/cards — clear безнал primary row |
| **04** | Tier 1 — Anchor | **4** | Checklist density — audit-like |
| **07 + FORM** | Tier 1 — Anchor | **4** | CTA + form endpoint |
| **03** | Tier 2 — Support | **3** | Shorter chain — distinct from BLOCK 01 |
| **06** | Tier 2 — Support | **3** | 8-item accordion |
| Trust strip | Tier 2 — Support | **2** | Optional — 4 equal micro-labels |
| Entity trust row | Tier 2 — Support | **2** | SC-03 — after lead or post BLOCK 04 |
| **05** | Tier 3 — Context | **2** | SC-13 grid — 5 segments |
| Lead | Tier 1 | **3** | Sets frame — not longer than process intro |

**Section rhythm:** Avoid 7 equal-weight sections — Tier 1 blocks need clear vertical separation (Contacts internal-page spacing).

---

## 11. Process visualization philosophy (BLOCK 01)

### 11.1 Charter decision — choose ONE pattern

| Pattern | Verdict |
|---------|---------|
| **Numbered step timeline (SC-04)** | **SELECTED — primary and only owner for BLOCK 01** |
| Calendar / date timeline | **REJECTED** — no SLA dates in copy; SAFE UNKNOWN |
| Process table | **REJECTED for BLOCK 01** — table reserved for methods (BLOCK 02) and documents (BLOCK 04) |
| Process cards grid | **REJECTED for BLOCK 01** — cards dilute sequence semantics |
| Gantt / phase bands | **REJECTED** — implies locked durations |

### 11.2 SC-04 rules for Payment

| Rule | Detail |
|------|--------|
| Step count | **6** — per copy; equal visual weight |
| Labels | Short badges: Заявка · Согласование · Счёт · Оплата · Подтверждение · Отгрузка |
| Orientation | Desktop: horizontal phased timeline preferred; Mobile ≤1024px: **vertical stack** with connecting line |
| Duration chips | **FORBIDDEN** — timeline note is prose only («зависят от состава заказа») |
| Artifacts | Step titles may imply КП/счёт — **no document thumbnails** |
| Cross-links | Step 2 → Custom; Step 6 → Delivery — inline text links in step body |
| Shared component | **Locks corp pattern** for M9.14, M9.17, M9.18, M9.16 |

### 11.3 BLOCK 03 relationship

BLOCK 03 uses a **compact 4-row status chain** (Оплата → Подтверждение → Производство/комплектация → Отгрузка) — **not** a second SC-04 timeline.

Visual language: lighter weight, subordinate, reads as «zoom-in on steps 4–6 aftermath» — prevents duplicate timeline fatigue.

---

## 12. Documents strategy (BLOCK 04)

### 12.1 Presentation pattern

| Parameter | Decision |
|-----------|----------|
| Pattern | **SC-06 document checklist** — document name + «когда и зачем» column |
| Layout | Responsive table → stacked rows ≤1024px |
| Sample PDFs | **FORBIDDEN** unless operator provides redacted samples |
| Thumbnails | **FORBIDDEN** — text checklist only |
| УПД / счёт-фактура naming | Prose per copy — **no invented doc type guarantees** |

### 12.2 Hierarchy within BLOCK 04

| Sub-block | Visual weight |
|-----------|---------------|
| Document checklist (5 rows) | **Dominant within BLOCK 04** |
| Body (договор / тендер) | Supporting prose |
| H3 «Реквизиты для проверки контрагента» | **Secondary** — fact list + Contacts link |
| ЭДО helper | Tertiary microcopy |

### 12.3 Requisites subsection — dominate or not?

| Decision | **Do NOT dominate** |
|----------|---------------------|
| Rationale | Page removes **uncertainty about process and documents**, not replaces Contacts requisites panel |
| Treatment | ИНН/КПП/ОГРН as **scannable fact rows** inside BLOCK 04 H3 |
| Bank details | **Not on page by default** — «в счёте» + manager request |
| CTA | «Контакты и юридические реквизиты» link — always present |

---

## 13. Audience matrix strategy (BLOCK 05)

### 13.1 Visual importance

| Parameter | Decision |
|-----------|----------|
| Component | SC-13 partner/segment matrix variant |
| Grid | 2–3 columns desktop; single column mobile |
| Card weight | **Supporting** — Tier 3; lighter than BLOCK 02 table |
| Icons | Generic segment icons permitted — no client logos |
| Dealer row | Includes link to `/dealers` — not expanded |

### 13.2 Placement philosophy

BLOCK 05 sits **after** process + methods + documents proof — answers «это про меня?» for visitors who need segmentation confirmation before FAQ/CTA.

**Do not** place BLOCK 05 above BLOCK 01 — persona matrix before process violates narrative arc.

### 13.3 Dominance rule

If mobile space is constrained, BLOCK 05 may compress to **stacked list** without icons — preserve copy, reduce chrome.

---

## 14. FAQ strategy

### 14.1 Role

FAQ is **objection resolver** for finance/procurement edge cases — not primary education (BLOCK 01–04 own that).

### 14.2 Parameters

| Parameter | Decision |
|-----------|----------|
| Count | **8 items** — per approved copy; do not expand |
| Pattern | SC-08 single-open accordion |
| Position | After BLOCK 05, before BLOCK 07 |
| Visual weight | Important — **subordinate** to BLOCK 01 and BLOCK 04 |

### 14.3 Priority items (mobile density)

| Priority | FAQ | Why |
|----------|-----|-----|
| 1 | Юрлица и безнал? | Core Q1 |
| 2 | НДС в счёте? | Core Q3 — no fake % in accordion header |
| 3 | Срок действия счёта? | Core Q5 |
| 4 | Когда производство после оплаты? | Core Q7 + Delivery link |
| 5–8 | Remaining | Deferral, partial pay, closing docs, FL |

### 14.4 Overlap discipline

FAQ must **not repeat** full BLOCK 01 timeline or BLOCK 04 checklist — short confirmatory answers with links to owners (Dealers, Delivery, Custom).

### 14.5 Forbidden FAQ patterns

- Accordion headers with «НДС 20%» chip
- Countdown «оплатите за N дней»
- Card payment «да/нет» icon row

---

## 15. CTA strategy

### 15.1 Hierarchy (locked)

| Priority | Element | Placement |
|----------|---------|-----------|
| **Primary** | «Запросить счёт или КП» → form submit | BLOCK 07 + FORM only |
| **Secondary** | «Перейти в каталог» | BLOCK 07 — subordinate |
| **Tertiary** | «Контакты и реквизиты» | BLOCK 07 link |
| **Support** | Phone `8 (3852) 72-18-90` · `info@bzpm.ru` | BLOCK 07 inline |

### 15.2 One CTA or multiple?

| Decision | **One primary button zone per page** |
|----------|--------------------------------------|
| Mid-page buttons | **FORBIDDEN** — no «Запросить счёт» before BLOCK 07 |
| Text links | Permitted in lead, process steps, BLOCK 03–04 — not button-styled |
| Phone as parallel CTA | Visible in BLOCK 07 — support, not competing primary button |

### 15.3 Placement philosophy

CTA band **after FAQ** — user has consumed process, methods, documents, audience fit, and residual objections.

FORM immediately follows CTA band (or integrated in same visual zone per SC-09).

**Micro pointers under CTA body:** Delivery + Dealers — text links only (copy-provided).

---

## 16. Form strategy

### 16.1 Role

FORM is the **procurement escalation instrument** — captures **organization** identity for invoice routing; not a generic callback form.

### 16.2 Relationship to Contacts

| Aspect | Payment FORM | Contacts form |
|--------|--------------|---------------|
| Purpose | Счёт / КП / payment consultation | General inquiry + requisites discovery |
| Unique field | **company** (required) | No company field |
| Shared | name, phone, email, consent, privacy link, submit states | SC-10 base |
| comment placeholder | Order composition, VAT, documents, payment terms | General question |
| Success microcopy | Manager callback пн–пт 9–18 Барнаул | Same discipline |

### 16.3 Rules

| Rule | Detail |
|------|--------|
| Do not duplicate Contacts contact card grid above form | Entity row + link suffices |
| Do not embed requisites form fields (ИНН input) | Not in copy — manager handles |
| Backend | **SAFE UNKNOWN** — same `action="#"` posture as Contacts until implementation charter |
| Field prominence | **company** field visually emphasized — procurement identity |

---

## 17. Trust strategy — ranked sources

What creates «можно ли безопасно работать как юрлицо» — ranked for design emphasis.

| Rank | Trust source | Design treatment |
|------|--------------|------------------|
| **1** | **Process transparency** | BLOCK 01 timeline — dominant |
| **2** | **Document framework** | BLOCK 04 checklist — what buyer receives |
| **3** | **Honest payment instrument posture** | BLOCK 02 — безнал primary; no fake online pay |
| **4** | **Legal entity facts** | Entity row + BLOCK 04 H3 — ИНН path |
| **5** | **Manager accompaniment** | Lead, BLOCK 03, form intro — human, not chatbot |
| **6** | **Cross-links to About / Contacts** | Verification escape hatches |

**Not ranked as visual trust shortcuts:**

- Bank table (unless OQ-P01)
- VAT % badge (unless OQ-P02)
- Payment provider logos
- Dealer discount hints

---

## 18. Special requirement resolutions

### 18.1 Dominant page mode — A / B / C

| Mode | Verdict |
|------|---------|
| A) Financial | **REJECTED** — not a treasury/banking page |
| B) **Operational** | **SELECTED — dominant** |
| C) Legal | **REJECTED as dominant** — legal facts are supporting proof only |

**Operational mode means:** step sequence, handoffs, document timing, and post-pay status — visual language of **industrial B2B order flow** (cf. Abat-ural process reference in research), not fintech UI.

Legal and financial facts appear as **structured rows inside operational chapters** — never as hero.

### 18.2 Should requisites block dominate?

| Decision | **NO** |
|----------|--------|
| Default | ИНН/КПП/ОГРН in BLOCK 04 H3 — **secondary** to document checklist |
| Bank | Not on page unless OQ-P01 unlocks single canonical surface |
| Primary requisites CTA | Link to `/contact/` |

### 18.3 Should payment methods dominate?

| Decision | **NO — important but subordinate to process** |
|----------|-----------------------------------------------|
| BLOCK 02 weight | Tier 1 (4/5) but **below** BLOCK 01 (5/5) |
| Visual order | Process first, methods second — locked in copy hierarchy |

### 18.4 Should process dominate?

| Decision | **YES — primary visual anchor** |
|----------|--------------------------------|
| BLOCK 01 | Highest visual weight on page |
| Above-fold goal | Process start + lead positioning visible without scroll on common desktop viewports |
| Shared pattern | SC-04 becomes reference for corp program step #2 |

### 18.5 Trust strip and entity row placement

| Element | Placement decision |
|---------|-------------------|
| Trust strip (4 badges) | **Optional** — after lead, before BLOCK 01; if used, subordinate to H1+lead |
| Entity trust row (4 labels) | **Recommended** — after BLOCK 04 or integrated at end of BLOCK 04; alternative: after lead if trust strip omitted |
| Both together | **Avoid** — pick one compact strip + entity row max; prevents badge fatigue |

### 18.6 Shared components instantiated on Payment

| ID | Component | Payment blocks |
|----|-----------|----------------|
| SC-01 | Corp page shell | All |
| SC-03 | Trust row | Entity trust row (MICRO) |
| SC-04 | Process timeline | BLOCK 01 |
| SC-06 | Document checklist | BLOCK 04 |
| SC-07 | Matrix table | BLOCK 02 summary table |
| SC-08 | FAQ accordion | BLOCK 06 |
| SC-09 | CTA band | BLOCK 07 |
| SC-10 | Corp inquiry form | FORM (+company variant) |
| SC-12 | Cross-link inline | Lead, body, CTA pointers |
| SC-13 | Segment matrix | BLOCK 05 |

**Payment is primary owner** for SC-04, SC-06, SC-07 (methods variant) — downstream pages instantiate, do not redesign.

---

## 19. Design risks

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R1 | VAT 20% badge temptation (ATLAS attested, OQ-P02 locked) | **High** | No % on page; FAQ/copy prose only |
| R2 | Methods matrix mimics checkout UX | **High** | Informational table — no «Оплатить» buttons |
| R3 | Card payment claim vs `cod`/`free_checkout` runtime | **High** | BLOCK 02 note prominent; align all surfaces |
| R4 | Bank requisites pressure from procurement users | **Medium** | Contacts link + «в счёте»; OQ-P01 decision |
| R5 | Duplicate timeline (BLOCK 01 vs BLOCK 03) | **Medium** | SC-04 vs compact chain — distinct patterns |
| R6 | Live `/payment-methods` generic `.zpm-seo` flat prose | **Medium** | New corp block system — not SEO article layout |
| R7 | Delivery overlap on ship-after-pay | **Medium** | BLOCK 03 summary + link; no TK content |
| R8 | Form +company validation drift vs Contacts | **Low** | Implementation charter — mask parity |
| R9 | Trust strip + entity row + BLOCK 04 H3 triple entity | **Medium** | §18.5 — limit redundant strips |
| R10 | «По согласованию» visual emptiness | **Medium** | Process structure compensates; no fake numeric chips |
| R11 | Dealer page payment duplication | **Low** | One-line + link discipline |
| R12 | Production URL parity unknown | **Low** | Document at implementation |

---

## 20. Forbidden patterns

| Pattern | Why forbidden |
|---------|---------------|
| Consumer ecommerce checkout look | Catalog is RFQ-led B2B |
| Credit-card marketing hero / card brand wall | No online acquirer attested |
| Online payment focus / «Оплатить картой» primary button | OQ-P06; runtime mismatch |
| Promo banners / discount emphasis | Owner: Dealers / catalog promos |
| Retail UX (cart steps, payment method icons row) | Anti-goal |
| Fake finance icons (Visa, Mastercard, Mir decorative) | Misleading trust |
| Full bank requisites without OQ-P01 unlock | Contacts single-owner |
| НДС 20% chip without OQ-P02 unlock | Governance drift |
| Invoice validity countdown timer | SAFE UNKNOWN — no invented SLA |
| Prepayment % badges | OQ-P03 locked |
| Sample invoice PDF gallery | Operator asset required |
| SKU price cards | Owner: Catalog |
| TK / freight tables | Owner: Delivery |
| Warranty term / RMA detail | Owner: Warranty |
| Factory OEM video / story | Owner: About |
| Dealer discount tiers | Owner: Dealers |
| Multiple primary CTA buttons mid-page | §15.2 |
| H5/H6 deep heading stack (live page anti-pattern) | Corp section H2 discipline |
| Blockquote SEO preamble as hero | Lead replaces |
| Autoplay payment animation | UX noise |
| ЭДО operator logo without attestation | SAFE UNKNOWN |

---

## 21. Success criteria

Operator judges Payment design **successful** when:

| # | Criterion | Verification method |
|---|-----------|---------------------|
| S1 | Visitor answers IA Q1–Q7 on-page (except bank depth — Contacts) | Copy coverage audit vs IA map |
| S2 | BLOCK 01 process scannable in **<15 seconds** desktop | Operator scan test |
| S3 | «Нет онлайн-оплаты в каталоге» visible without opening FAQ | Above-fold or BLOCK 02 top review |
| S4 | BLOCK 04 reads as «документы для бухгалтерии» checklist | Operator review |
| S5 | No CP-01 violations — sibling topics are links only | Cross-link audit |
| S6 | Form includes required **company** field; consent matches Contacts | Side-by-side with `/contact/` |
| S7 | SC-04 timeline pattern locked for reuse on Delivery/Warranty/Custom/Dealers | Design program registry check |
| S8 | One primary CTA zone — no mid-page submit | Design review |
| S9 | Page feels **operational**, not fintech or legal contract | Operator visual compare |
| S10 | Mobile ≤1024px — methods table stacks without horizontal scroll trap | Responsive check |
| S11 | No numeric VAT/prepayment/invoice-day badges without OQ unlock | Governance check |
| S12 | B2B buyer understands invoice path **without sales call** for standard case | Operator scenario test |
| S13 | Design charter approved **before** wireframe/mockup work | Phase gate |

---

## 22. Open questions (operator lock)

| ID | Question | Impact | Default if unresolved |
|----|----------|--------|----------------------|
| OQ-DC-P01 | Publish full bank requisites on Payment, Contacts, or neither? (OQ-P01) | BLOCK 04 / Contacts | **Neither on page** — invoice + Contacts ИНН only |
| OQ-DC-P02 | Publish НДС 20% visually? (OQ-P02) | Badge temptation | **No %** — prose + manager per copy |
| OQ-DC-P03 | Trust strip above BLOCK 01 — include? | First screen density | **Include** — 4 micro-labels after lead |
| OQ-DC-P04 | Entity trust row — after lead or after BLOCK 04? | Scan order | **After BLOCK 04** if trust strip used; else after lead |
| OQ-DC-P05 | Catalog secondary CTA URL — `/` vs hub | BLOCK 07 | `/` per copy note |
| OQ-DC-P06 | Legacy `.zpm-seo` payment page — new `zpm-payment-*` namespace? | Implementation | Defer to implementation charter |
| OQ-DC-P07 | Redacted sample invoice — any operator asset? | BLOCK 04 | **Exclude** — checklist text only |
| OQ-DC-P08 | PLP Commercial Trust payment FAQ card — design now or defer? | Catalog secondary | **Defer** — documentation parallel; not page body |
| OQ-DC-P09 | ЭДО — any operator branding allowed? | BLOCK 04 helper | **Text only** |
| OQ-DC-P10 | Form backend routing — same as Contacts modal? | FORM | Defer to implementation charter |

---

## 23. Design readiness verdict

| Dimension | Status | Notes |
|-----------|--------|-------|
| Copy | **READY** | v1 complete — operator approval header pending |
| IA | **READY** | CP-01 boundaries locked; Payment = settlement owner |
| Charter | **READY FOR OPERATOR REVIEW** | This document |
| Assets | **PARTIAL** | No sample invoice; structural SC-04/SC-06 sufficient |
| OQ | **PARTIAL** | OQ-P01–P02 affect requisites/VAT visuals — explicit deferrals |
| Visual design | **NOT READY** | Awaits operator charter approval |
| Implementation | **NOT READY** | Awaits design approval + implementation charter |
| Downstream unlock | **PARTIAL** | SC-04/SC-06/SC-07 pattern lock enables M9.14+ charters |

**Verdict:** M9.15 Payment is **PARTIAL DESIGN READY** — charter pass complete; operator may approve charter and authorize **visual design phase** with operational-dominant posture, process-first layout, and explicit SAFE UNKNOWN deferrals (no VAT %, no bank table by default).

**Explicit stop:** No wireframes · no mockups · no Twig/CSS/JS · no deploy.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-22 | **CREATED** — Design Charter v1; resolves operational vs financial/legal mode; process timeline (SC-04); requisites/methods dominance; documents checklist; CTA/form strategy; shared component ownership for program step #2 |

---

*BZPM M9.15 Payment Design Charter v1 — documentation only. No design, wireframes, mockups, or implementation authorized.*
