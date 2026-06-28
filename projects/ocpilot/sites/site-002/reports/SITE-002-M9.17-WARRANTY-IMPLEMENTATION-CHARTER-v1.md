# REPORT — SITE-002 M9.17 WARRANTY IMPLEMENTATION CHARTER

**Milestone:** M9.17 — Warranty / Гарантия  
**Project:** OCPilot · SITE-002 (ЗПМ / BZPM)  
**Environment (TEST):** https://zpm.new-site.space/guarantee  
**Branch:** `mars/canonical-post-recovery`  
**Authority:** `SITE-002-STABLE-LIVE-M9.15-PAYMENT-01` (+ M9.14 Delivery · M9.13 About Restored for non-corp scope)  
**Version:** v1  
**Date:** 2026-06-28  
**Mode:** Documentation only — **no** OpenCart · **no** Twig/CSS/JS · **no** deploy · **no** FTP · **no** TEST writes

**Boundary:** Definitive implementation blueprint for the next coding task. This document authorizes **planning clarity only**; runtime changes require a separate implementation task after operator gates.

**Central page question:** «Что произойдёт, если после покупки возникнет проблема с оборудованием?»

---

## 1. Authority

### 1.1 Primary sources (use only these)

| # | Artefact | Path | Role |
|---|----------|------|------|
| A1 | **PAGE COPY (canonical)** | [BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md](../copy/BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md) | All visible text — single copy authority |
| A2 | **Design Charter** | [BZPM-M9.17-WARRANTY-DESIGN-CHARTER-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.17-WARRANTY-DESIGN-CHARTER-v1.md) | Visual hierarchy, forbidden patterns, SC mapping, service-page mode |
| A3 | **Design Brief** | [BZPM-M9.17-WARRANTY-DESIGN-BRIEF-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.17-WARRANTY-DESIGN-BRIEF-v1.md) | Designer-facing priorities |
| A4 | **Visual Design / shared components** | [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md) § SC-01–SC-15 | Component registry and corp rhythm |
| A5 | **Corporate Pages Program** | [BZPM-CORPORATE-PAGES-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-v1.md) · [IA Map § M9.17](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-IA-MAP-v1.md#m917--warranty-guarantee) | CP-01 ownership · program order |
| A6 | **Copy Standards** | [BZPM-COPY-STANDARDS-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-COPY-STANDARDS-v1.md) | Tone · SAFE UNKNOWN discipline |
| A7 | **Forensic Research** | [BZPM-M9.17-WARRANTY-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](BZPM-M9.17-WARRANTY-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) · [m9.17-work/guarantee-live.html](m9.17-work/guarantee-live.html) | Live surface facts and gaps |
| A8 | **SITE-002 implementation patterns** | [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) §18–19 | Delivery/Payment corp page discipline |
| A9 | **Delivery implementation (precedent)** | [SITE-002-M9.14-DELIVERY-IMPLEMENTATION-CHARTER-v1.md](SITE-002-M9.14-DELIVERY-IMPLEMENTATION-CHARTER-v1.md) · [SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md](SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md) | Route migration · timeline · FAQ · CTA pattern |
| A10 | **Payment implementation (precedent)** | [SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md](SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md) · [BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md) | SC-04 reuse · corp accordion extension |
| A11 | **Commercial Trust pattern** | [SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md](SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md) | CTA/form/card language · PLP secondary link target |
| A12 | **Contacts implementation** | [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md) | Internal-page shell · `zpm-form` · spacing rhythm |
| A13 | **site-passport** | [site-passport.md](../site-passport.md) | Operator order · blockers |
| A14 | **OCPILOT-STATE** | [OCPILOT-STATE.md](../../OCPILOT-STATE.md) | Program status |

### 1.2 Operator authority

| Gate | Status | M9.17 impact |
|------|--------|--------------|
| B6 Design Charter approval | OPEN (header pending) | Task treats Design Charter as authority input |
| B8 Copy sign-off | OPEN | Implementation uses copy v1 text |
| B1 МО warehouse address | OPEN | **No impact** on Warranty scope (no MO address on page) |
| B3 Dealers PLP form | OPEN | **No impact** on Warranty scope |
| B2 Warranty term on site (OQ-W01/W17) | OPEN | **Default:** no numeric months on page |

### 1.3 Preflight synthesis (runtime facts)

| Fact | Evidence | Implementation implication |
|------|----------|----------------------------|
| URL `/guarantee` resolves today | Forensic §2.1 · `guarantee-live.html` | Preserve public URL; change route target only |
| Alternatives `/garantiya`, `/warranty` **not used** | Forensic §2.1 | Do not create alternate routes |
| Current route likely `information/information` + CMS `information_id` | Forensic §2.1 — **SAFE UNKNOWN** exact ID | Pre-implementation FTP capture must confirm; target route **`information/guarantee`** |
| No `zpm-warranty-*` namespace on live | Forensic §3 | **New** scoped CSS block required |
| Body = generic `zpm-seo` prose — exclusions-heavy legacy | `guarantee-live.html` | Replace with structured sections; **process-dominant**, not exclusion-first |
| Pageintro = H1 only, **no lead** | Live capture | Add `$pageintro->description` with copy Lead |
| No FAQ, no dedicated form, no CTA on live | Live capture | Full net-new bottom stack |
| No cross-links in body | Forensic §3.4 | Implement inline SC-12 links per copy |
| Form backend | Contacts/Delivery/Payment pattern `action="#"` | Preserve — no new backend in M9.17 |
| Commercial Trust PLP links to `/guarantee` | Copy MICRO · Knowledge Map §14 | Secondary surface — do not duplicate trust block on page |
| Delivery page links to `/guarantee` | M9.14 live twig | Inbound cross-link — Warranty must be consistent |

### 1.4 SAFE UNKNOWN (charter-level)

| Topic | Status | Charter handling |
|-------|--------|------------------|
| OpenCart `information_id` for `guarantee` | **SAFE UNKNOWN** | Capture at preflight; do not delete legacy CMS entry |
| Production `/guarantee` parity (OQ-W20) | **SAFE UNKNOWN** | TEST-first; document at deploy |
| Warranty term months (OQ-W01) | **SAFE UNKNOWN** | **No badge** — prose + FAQ 1 only |
| PDP/PLP «12 мес» chip sync (OQ-W17) | **SAFE UNKNOWN** | Out of M9.17 page scope unless operator unlocks B2 |
| Service model / ASC network (OQ-W04) | **SAFE UNKNOWN** | Prose + Dealers link — no SC map |
| Dealer end-client routing (OQ-W05) | **SAFE UNKNOWN** | FAQ 4 neutral copy |
| SLA response/repair days (OQ-W06) | **SAFE UNKNOWN** | BLOCK 03 timeline note — no countdown chips |
| RMA logistics payer (OQ-W07) | **SAFE UNKNOWN** | FAQ 3 + Delivery link |
| Replace vs repair policy (OQ-W08) | **SAFE UNKNOWN** | FAQ 7 — after diagnostics |
| Warranty talon sample (OQ-W09) | **SAFE UNKNOWN** | Text checklist only — no PDF thumbnail |
| Photo upload in form (OQ-W14) | **SAFE UNKNOWN** | **Exclude** from MVP form |
| Dedicated service email vs info@ | **Assumed** info@bzpm.ru | Per copy v1 |
| Privacy policy route | **Assumed** `/privacy-policy` | Verify at preflight |
| Trust strip vs BLOCK 01 summary row (OQ-DC-W03) | **OPEN** | Pick **one** at implementation step 6 — not both heavy |
| Cross-links summary table (OQ-DC-W11) | **OPEN** | Optional footer — lowest weight |

### 1.5 Superseded — do not use

| Artefact | Reason |
|----------|--------|
| Live generic `zpm-seo` guarantee HTML | Replaced entirely by custom implementation |
| Exclusion-first live hierarchy («Когда гарантия не действует» as page identity) | Design Charter forbids |
| Global modal-only claim path (`#zpmFbQuestion` without dedicated form) | Dedicated FORM required |
| PDP work-copy «12 месяцев» without operator lock | Governance drift — do not surface on corp page |
| Repair-company / ASC directory patterns | Not attested · anti-goal |

---

## 2. Implementation architecture

### 2.1 Page feel (locked)

**Manufacturer service reassurance page** — process-dominant, accompaniment framing, not legal exclusions chapter, not service-center directory, not consumer warranty card. Align internal-page rhythm with Delivery/Payment/Contacts (`page--inner`, breadcrumb → page-intro → `<main>`).

**Corporate Pages language alignment:** Same operational corp mode as M9.14 Delivery and M9.15 Payment — SC-01 shell, SC-04 timeline spine, SC-08 accordion, SC-09/SC-10 CTA+form — **warranty-specific copy and 5-step process**, not mechanical page clone.

### 2.2 Target render chain

```
GET /guarantee
  └─ index.php → route information/guarantee          [NEW — replaces generic information/information]
       └─ catalog/controller/information/guarantee.php
            ├─ document: meta title, description, keywords, bodyClass page--inner
            ├─ Breadcrumbs → global chrome
            ├─ Pageintro → H1 «Гарантия на оборудование» + Lead (copy)
            └─ catalog/view/theme/default/template/information/guarantee.twig
                 └─ <main class="main zpm-warranty-page">
                      ├─ [optional] trust strip (mutually exclusive with heavy duplicate)
                      ├─ § BLOCK 01 — warranty principles + coverage
                      ├─ § BLOCK 02 — documents checklist
                      ├─ § BLOCK 03 — claim procedure (SC-04 spine)
                      ├─ § BLOCK 04 — verification cases (exclusions — subordinate)
                      ├─ § BLOCK 05 — service outcomes
                      ├─ § BLOCK 06 — FAQ (SC-08)
                      └─ § BLOCK 07 + FORM — CTA + service claim form
       └─ assets/css/style.css → appended zpm-warranty-* (~380–480 lines est.)
       └─ assets/js/main.js → extend corp FAQ accordion with [data-warranty-faq]
```

**SEO URL migration:** Update `oc_seo_url` entry for keyword `guarantee` from `information/information&information_id=…` to `information/guarantee` during controller step. Confirm via preflight capture before edit.

### 2.3 Section architecture (user-facing groups)

Full top-to-bottom order matches copy blocks. User-requested groups mapped below.

---

#### Hero (SC-01 shell + lead zone)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Immediate reassurance: manufacturer accompanies after purchase; central question answered in <10s scan |
| **UX goal** | «Производитель останется на связи?» — yes, with About/Delivery context links |
| **Copy source** | Utility meta · Breadcrumb · H1 · Lead |
| **Shared component** | SC-01 — Contacts/Delivery/Payment `page-intro` pattern |
| **Visual weight** | Tier 1 (3/5) — frame, not hero media |
| **Reuse source** | [Knowledge Map §18–19](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md); Delivery `pageintro` controller pattern |
| **Implementation notes** | H1 in `page-intro` via controller `Pageintro`; Lead in `$pageintro->description`; **no** warranty certificate hero; **no** term badge; optional trust strip per OQ-DC-W03 |
| **Dependencies** | `guarantee.php` controller; `Pageintro` class; inline links `/about`, `/delivery` |

---

#### Warranty principles (BLOCK 01 — intro + body + summary row)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Define what warranty **support means** — manufacturer responsibility, accompaniment, not legal wall |
| **UX goal** | Positive coverage frame before process and documents |
| **Copy source** | BLOCK 01 H2 · Intro · Body · Summary row (4 micro-labels) · Helper · About pointer · Cert disclaimer |
| **Shared component** | SC-03 trust row variant (summary row); SC-07 outcome table variant |
| **Visual weight** | Tier 1 (4/5) |
| **Reuse source** | Delivery BLOCK 01 summary row; Payment legal entity strip idiom (compact labels) |
| **Implementation notes** | Summary row: Ответственный · Производство · Основание · Сопровождение; cert ≠ warranty one-line; **no** numeric term badge |
| **Dependencies** | Outcome table responsive stack ≤1024px |

---

#### Warranty coverage (BLOCK 01 — outcome table)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Scannable list of what buyer receives through warranty support journey |
| **UX goal** | 5-row outcome table readable without legal parsing |
| **Copy source** | BLOCK 01 outcome table (5 rows) |
| **Shared component** | SC-07 matrix table → stacked cards on mobile |
| **Visual weight** | Tier 1 (4/5) — within BLOCK 01, subordinate to intro |
| **Reuse source** | Delivery outcome rows (`zpm-delivery-outcome__*`); Payment proof card list anatomy |
| **Implementation notes** | Columns: Результат · Что это значит для вас; no SLA chips |
| **Dependencies** | Same section as principles — single BLOCK 01 landmark |

---

#### Documents (BLOCK 02 — required; supports claim readiness)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Practical checklist — what to prepare before/during claim |
| **UX goal** | «Что подготовить» before process step 2 |
| **Copy source** | BLOCK 02 H2 · Intro · Outcome-first list (6 rows) · Body · Dealer/Custom pointers · Helper |
| **Shared component** | **SC-06 document checklist** — fourth corp instantiation |
| **Visual weight** | Tier 1 (4/5) — **below** BLOCK 03 process (5/5) |
| **Reuse source** | Delivery document/outcome patterns; Payment proof cards checklist idiom |
| **Implementation notes** | Table → stacked rows ≤1024px; **no** talon PDF thumbnails; photo request = text only |
| **Dependencies** | Visual bridge to BLOCK 03 step 2 «Сбор информации» |

---

#### Claim procedure (BLOCK 03 — SC-04 owner)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Primary mental model — 5-step path from first message to resolution |
| **UX goal** | Full process scannable in <20s desktop; steps 1–3 visible early on scroll |
| **Copy source** | BLOCK 03 H2 · Intro · 5 process steps · Outcome note · Timeline note · Delivery pointer · Step badges |
| **Shared component** | **SC-04** `zpm-corp-timeline` — reuse from M9.14/M9.15 with warranty-specific labels |
| **Visual weight** | Tier 1 (**5/5**) — **page spine** |
| **Reuse source** | `zpm-corp-timeline` CSS from Delivery/Payment; extend step count to 5 |
| **Implementation notes** | Step 1 includes phone, form anchor, email; **no** SLA day chips; `aria-label` on `<ol>` |
| **Dependencies** | CSS grid/flex; no JS required for static timeline |

---

#### Warranty exclusions (BLOCK 04 — verification cases; calm honesty)

| Attribute | Spec |
|-----------|------|
| **Purpose** | When extra verification may apply — **not** page identity |
| **UX goal** | Calm bullet list; no fear design; subordinate to BLOCK 03 |
| **Copy source** | BLOCK 04 H2 · Intro · 7 bullets · Calm framing note · Helper |
| **Shared component** | Simple prose list — **no** dedicated SC; forbidden red alert pattern |
| **Visual weight** | Tier 2 (**2/5**) — deliberately light |
| **Reuse source** | Contacts list typography; **not** live exclusion-first hierarchy |
| **Implementation notes** | **No** red boxes · **no** warning icons · **no** «ВНИМАНИЕ» banners; position **after** BLOCK 03 |
| **Dependencies** | Must not visually compete with timeline |

---

#### Service (BLOCK 05 — post-claim outcomes)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Predictability after escalation — statuses, explanation, next step |
| **UX goal** | «Что получает заказчик» — 6 outcome rows |
| **Copy source** | BLOCK 05 H2 · Intro · Outcome list (6 rows) · Body · Payment/Contacts pointers |
| **Shared component** | SC-07 outcome list variant |
| **Visual weight** | Tier 2 (3/5) |
| **Reuse source** | Delivery BLOCK 07 outcomes; Payment audience outcome rows |
| **Implementation notes** | Emphasis on status communication; inline links only to Payment/Contacts |
| **Dependencies** | Follows BLOCK 04 — trust closer before FAQ |

---

#### FAQ (BLOCK 06 — SC-08)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Objection resolver — term, dealer path, logistics, custom, repair model |
| **UX goal** | Single-open accordion; 8 items exactly; short answers with owner links |
| **Copy source** | BLOCK 06 (8 Q&A) |
| **Shared component** | **SC-08** `zpm-corp-faq` — extend accordion init |
| **Visual weight** | Tier 2 (3/5) |
| **Reuse source** | Delivery/Payment FAQ markup and CSS — add `[data-warranty-faq]` scope |
| **Implementation notes** | `<button aria-expanded aria-controls>` + panel ids; one open at a time; `prefers-reduced-motion` safe |
| **Dependencies** | Extend `main.js` selector: `[data-delivery-faq], [data-payment-faq], [data-warranty-faq]` |

---

#### CTA + Form (BLOCK 07 + FORM — SC-09 + SC-10 service variant)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Service claim initiation — primary conversion at page bottom |
| **UX goal** | One primary button zone; phone/email parallel support; form captures equipment context |
| **Copy source** | BLOCK 07 · FORM block · Dealer pointer · Schedule microcopy |
| **Shared component** | Commercial Trust `zpm-commercial-trust__card` + SC-10 `zpm-form` + **service fields variant** |
| **Visual weight** | Tier 1 (4/5) |
| **Reuse source** | Delivery/Payment CTA band; Contacts form hooks |
| **Implementation notes** | Primary: «Отправить обращение»; `action="#"`; fields: name, phone, email, **equipment_model** (req), purchase_date (opt), **comment** (req); consent `/privacy-policy`; `data-mask="phone"` `data-validate="email"` |
| **Dependencies** | No duplicate Contacts card grid; no photo upload in MVP |

---

### 2.4 Forbidden globally

Map embed · ASC/service-center directory · warranty term hero badge («12 мес») without OQ-W01 · SLA countdown chips · red exclusion warning walls · legal article numbering as page spine · warranty certificate mockup hero · repair-shop wrench hero · mid-page primary submit · TK tables · payment requisites · dealer program terms · custom TZ matrix · sample talon PDF gallery · photo upload without backend · duplicate About/Delivery/Payment/Dealers bodies.

---

## 3. Final OpenCart architecture

### 3.1 Route

| Item | Value |
|------|-------|
| Public URL | `/guarantee` (unchanged) |
| OpenCart route | `information/guarantee` |
| Prior route (inferred) | `information/information&information_id=…` — confirm at preflight |
| SEO keyword | `guarantee` |

### 3.2 Controller

| File | Status | Responsibility |
|------|--------|----------------|
| `catalog/controller/information/guarantee.php` | **NEW** | Meta SEO, breadcrumbs, Pageintro H1+lead, load guarantee view (~60–90 lines) |
| `catalog/controller/information/information.php` | **UNTOUCHED** | Generic CMS pages remain |

### 3.3 Twig

| File | Status | Responsibility |
|------|--------|----------------|
| `catalog/view/theme/default/template/information/guarantee.twig` | **NEW** | All BLOCK 01–07 + FORM (~400–550 lines) |
| `catalog/view/theme/default/template/common/header.twig` | **UNTOUCHED** | Breadcrumb + pageintro |
| `catalog/view/theme/default/template/common/footer.twig` | **UNTOUCHED** | Global chrome |
| `catalog/view/theme/default/template/information/information.twig` | **UNTOUCHED** | Not used for `/guarantee` after cutover |

**Optional partial (defer if twig > ~550 lines):**

| File | Status | Reason |
|------|--------|--------|
| `catalog/view/theme/default/template/sections/blockwarrantyform.twig` | **NEW (optional)** | Extract FORM — mirror `blockanyquestionsform.twig` |

### 3.4 SEO

| Location | Content source |
|----------|----------------|
| `guarantee.php` → `setTitle()` | Copy utility Meta title |
| `guarantee.php` → `setDescription()` | Copy utility Meta description |
| `guarantee.php` → `setKeywords()` | Optional — from copy / legacy live |
| `oc_seo_url` row `keyword=guarantee` | **MODIFIED** → `information/guarantee` |
| OG tags | Existing theme behaviour — verify at QA |

### 3.5 CSS

| File | Status | Responsibility |
|------|--------|----------------|
| `assets/css/style.css` | **MODIFIED (append)** | `zpm-warranty-page` namespace (~380–480 lines) |
| `reports/m9.17-work/m9.17-warranty-page.css` | **NEW (repo work copy)** | Staging before append |

**Shared classes reused (not duplicated):** `zpm-corp-timeline`, `zpm-corp-faq__*`, `zpm-form__*`, `zpm-commercial-trust__*`, `section-title__like-h2`.

**Page-scoped classes (new):** `zpm-warranty-page`, `zpm-warranty-section`, `zpm-warranty-principles`, `zpm-warranty-coverage`, `zpm-warranty-docs`, `zpm-warranty-process`, `zpm-warranty-verification`, `zpm-warranty-outcomes`, `zpm-warranty-faq`, `zpm-warranty-cta`.

### 3.6 JS

| File | Status | Responsibility |
|------|--------|----------------|
| `assets/js/main.js` | **MODIFIED (minimal)** | Add `[data-warranty-faq]` to corp accordion init (~5–15 lines delta) |
| `reports/m9.17-work/m9.17-corp-accordion.js` | **NEW (repo staging)** | Updated selector list if extracted |

**Reuse unchanged:** phone mask, email validate, form submit hooks.

### 3.7 Form

| Item | Spec |
|------|------|
| Location | Bottom CTA section inside `guarantee.twig` |
| Classes | `zpm-form`, `zpm-form__*` — Contacts parity |
| Fields | name, phone, email, **equipment_model** (req), purchase_date (opt), **comment** (req), agree |
| Hooks | `data-mask="phone"`, `data-validate="email"`, `required` on mandatory |
| Backend | `action="#"` — unchanged posture |
| Field IDs | Prefix `warranty*` or `guarantee*` — consistent within page |

### 3.8 FAQ accordion

| Item | Spec |
|------|------|
| Root hook | `data-warranty-faq` + `data-accordion` |
| Item hooks | `data-accordion-button`, `data-accordion-panel` |
| Count | 8 items |
| Behaviour | Single-open; toggle close on re-click |
| CSS namespace | `zpm-corp-faq` (shared) + `zpm-warranty-faq` (page scope) |

### 3.9 Breadcrumbs

| Item | Source |
|------|--------|
| Markup | Global `Breadcrumbs` class via controller |
| Trail | Главная → Гарантия |
| Template | `common/header.twig` — **no change** |

### 3.10 Language file (optional)

| File | Status |
|------|--------|
| `catalog/language/ru-ru/information/guarantee.php` | **NEW (optional)** — breadcrumb strings |
| Inline copy in twig/controller | **Alternative (allowed)** — matches Delivery/Payment |

**Recommendation:** Meta in controller; body copy static in twig.

---

## 4. Shared component reuse

### 4.1 Matrix

| Component | Source page / artefact | Reuse as-is | Adapt for Warranty | Create new | Forbidden |
|-----------|------------------------|-------------|-------------------|------------|-----------|
| **SC-01 Page shell** | Contacts · Delivery · Payment | `page--inner`, pageintro rhythm | H1+lead copy | — | Hero media block |
| **SC-03 Trust row** | Delivery summary row | 4-label micro-row pattern | Warranty labels | Optional trust strip | Both strip + heavy summary |
| **SC-04 Timeline** | Delivery (7) · Payment (6) | `zpm-corp-timeline` CSS/structure | **5 warranty steps** | — | SLA chips |
| **SC-06 Doc checklist** | Design program | Table/stack pattern | 6 document rows | First live if not in Delivery | PDF thumbnails |
| **SC-07 Outcome table** | Delivery outcomes | Responsive table/cards | BLOCK 01 + BLOCK 05 | — | — |
| **SC-08 FAQ accordion** | Delivery · Payment | `zpm-corp-faq__*` markup + JS | 8 warranty Q&A | — | Commercial Trust static FAQ grid |
| **SC-09 CTA band** | Delivery · Payment | Button hierarchy, phone/email | Service-specific H2 | — | Mid-page primary CTA |
| **SC-10 Form** | Contacts | Core fields + consent | +equipment_model, +purchase_date, +comment | Service form variant | Photo upload MVP |
| **Commercial Trust** | M9.8.9 PLP | CTA card shell, decor logo | Warranty titles/copy | — | Full PLP block on page |
| **Contacts** | `/contact/` | `zpm-form` discipline | Service fields | — | Contact card grid, map |
| **About** | `/about` restored | — | Link only | — | Factory narrative depth |
| **Delivery** | M9.14 live | — | One-line outbound/RMA pointers | — | TK tables, shipment points |
| **Payment** | M9.15 live | — | One-line deal-docs pointer | — | Methods matrix, bank details |
| **Verification list** | — | List typography from Contacts | BLOCK 04 calm bullets | Simple list styles | Red warning boxes |

### 4.2 Create for the first time on SITE-002

| Item | Notes |
|------|-------|
| `guarantee.php` controller | New corp page controller |
| `guarantee.twig` | Full warranty body |
| `zpm-warranty-*` CSS block | Page namespace — appended to style.css |
| SC-10 **service form variant** | First live `equipment_model` required field |
| Optional `blockwarrantyform.twig` | Only if twig size warrants extract |

### 4.3 Cross-check vs Delivery and Payment

| Dimension | Delivery | Payment | Warranty (M9.17) |
|-----------|----------|---------|------------------|
| Page mode | Manufacturer logistics | Deal/payment process | **Manufacturer service reassurance** |
| Timeline steps | 7 | 6 | **5** |
| Timeline weight | 5/5 | 5/5 | **5/5** |
| Dominant secondary block | Shipment points + TK table | Payment methods + proof cards | **Document checklist + coverage table** |
| Exclusion/verification block | None (outcomes only) | Legal entity strip | **BLOCK 04 calm verification (2/5)** |
| Form unique field | region (req) | company (req) | **equipment_model (req)** |
| FAQ count | 8 | 8 | **8** |
| CTA pattern | Commercial Trust card + form | Same | Same |
| Forbidden bleed | map, TK hero | bank widgets, logistics | term badge, ASC map, fear exclusions |

**Unified Corporate Pages language:** Same section spacing (~64–80px desktop), container padding (50px desktop / 10px mobile), `section-title__like-h2`, corp timeline visual language, corp FAQ accordion, Commercial Trust CTA terminus — **distinct copy and warranty-specific process**, not template duplication.

---

## 5. File map

Remote paths relative to TEST site root unless noted.

### 5.1 NEW (remote + repo work copies)

| Path | Location | Reason |
|------|----------|--------|
| `catalog/controller/information/guarantee.php` | Remote | Custom corp controller |
| `catalog/view/theme/default/template/information/guarantee.twig` | Remote | Full page body |
| `reports/m9.17-work/guarantee.php` | Repo | Work copy controller |
| `reports/m9.17-work/guarantee.twig` | Repo | Work copy twig |
| `reports/m9.17-work/m9.17-warranty-page.css` | Repo | CSS staging |
| `reports/m9.17-work/m9.17-corp-accordion.js` | Repo | JS staging (optional) |
| `reports/m9.17-work/m917-warranty-deploy.py` | Repo | Deploy script |
| `reports/m9.17-work/m917-warranty-screenshots.py` | Repo | QA screenshot script |
| `reports/m9.17-work/preflight-manifest.json` | Repo | Pre-deploy SHA256 |
| `reports/m9.17-work/deploy-manifest.json` | Repo | Post-deploy SHA256 |
| `reports/m9.17-work/qa-guarantee.html` | Repo | Live HTML capture |
| `baselines/SITE-002-STABLE-LIVE-M9.17-WARRANTY-01.md` | Repo | Stable checkpoint (post-implementation) |
| `qa/m9.17-warranty-screenshots/*` | Repo | Viewport screenshots |
| `backups/guarantee.php.pre-m9.17-warranty.bak` | Repo | Rollback |
| `backups/guarantee.twig.pre-m9.17-warranty.bak` | Repo | Rollback |
| `backups/style.css.pre-m9.17-warranty.bak` | Repo | Rollback |
| `backups/main.js.pre-m9.17-warranty.bak` | Repo | Rollback |

### 5.2 MODIFIED

| Path | Location | Reason | Approx. scope |
|------|----------|--------|---------------|
| `assets/css/style.css` | Remote | Append `zpm-warranty-*` | ~380–480 lines |
| `assets/js/main.js` | Remote | Add `[data-warranty-faq]` to accordion init | ~5–15 lines |
| `oc_seo_url` row `keyword=guarantee` | DB/admin | Route cutover | 1 row |

### 5.3 UNTOUCHED

| Path | Reason |
|------|--------|
| `catalog/controller/information/delivery.php` | Out of scope |
| `catalog/controller/information/payment.php` | Out of scope |
| `catalog/controller/information/about.php` | Out of scope |
| `catalog/view/theme/default/template/information/delivery.twig` | Out of scope |
| `catalog/view/theme/default/template/information/payment.twig` | Out of scope |
| `catalog/view/theme/default/template/information/about.twig` | Out of scope |
| `catalog/view/theme/default/template/information/contact.twig` | Out of scope |
| Header/footer/nav templates | Out of scope |
| Catalog/PLP/PDP templates | Out of scope — PLP trust link update is separate task |
| OpenCart admin Information entry (legacy CMS) | Orphaned after cutover — keep for rollback |

### 5.4 QA / backups discipline

| Item | Rule |
|------|------|
| Preflight | Live FTP capture **before** any remote write |
| Backups | One `.bak` per file overwritten |
| Manifest | SHA256 pre/post in `m9.17-work/` |
| Twig cache | Clear after deploy |
| Credentials | Deploy scripts — operator-local only; **never commit secrets** |

---

## 6. Execution order

Exact implementation sequence — **do not skip stages**.

| Step | Stage | Deliverable | Stop gate |
|------|-------|-------------|-----------|
| **1** | **Preflight capture** | FTP/live capture: current `information_id`, seo_url row, `style.css` SHA, `guarantee-live.html` baseline | `preflight-manifest.json` written |
| **2** | **Backups** | `.bak` for any file that will be overwritten | 4 backup files in `backups/` |
| **3** | **Controller** | `guarantee.php` — meta, breadcrumbs, pageintro with Lead | PHP syntax OK |
| **4** | **Route / SEO** | Repoint `/guarantee` → `information/guarantee` | `/guarantee` hits new controller |
| **5** | **Twig skeleton** | `guarantee.twig` — `<main class="zpm-warranty-page">` empty sections + landmarks | Page loads empty sections |
| **6** | **Hero / pageintro** | Lead in pageintro; optional trust strip **or** skip per OQ-DC-W03 | H1+lead visible; About/Delivery links work |
| **7** | **Warranty principles + coverage** | BLOCK 01 — intro, outcome table, summary row, cert disclaimer | No term badge |
| **8** | **Documents** | BLOCK 02 — SC-06 checklist (6 rows) | Table stacks mobile |
| **9** | **Claim procedure** | BLOCK 03 — 5-step SC-04 timeline | 5 steps; dominant visual |
| **10** | **Warranty exclusions** | BLOCK 04 — calm verification bullets | Weight 2/5; no red alerts |
| **11** | **Service outcomes** | BLOCK 05 — 6 outcome rows | Payment/Contacts links only |
| **12** | **FAQ** | BLOCK 06 — accordion markup + JS hook | 8 items; single-open |
| **13** | **CTA + form** | BLOCK 07 + FORM — service fields | equipment_model required |
| **14** | **CSS integration** | Append `zpm-warranty-*` to `style.css` | Reuse corp timeline/faq; no duplicate rules |
| **15** | **JS integration** | Extend accordion init for `[data-warranty-faq]` | No console errors |
| **16** | **Responsive pass** | 1440 · 1024 · 767 · 390 | No horizontal overflow |
| **17** | **SEO verify** | Title, description, breadcrumb | Matches copy utility |
| **18** | **Cross-link verify** | Delivery inbound links still valid | `/guarantee` content matches copy pointers |
| **19** | **QA** | Automated HTML checks + operator HITL viewports | Acceptance checklist §7 |
| **20** | **Deploy manifest** | SHA256 post-deploy + `qa-guarantee.html` | Manifest committed to `m9.17-work/` |
| **21** | **Stable checkpoint** | Register `SITE-002-STABLE-LIVE-M9.17-WARRANTY-01` | Criteria §9 met |
| **22** | **Git checkpoint** | Repo documentation + work copies | Operator-requested |

---

## 7. Acceptance checklist

Every item is **testable** on https://zpm.new-site.space/guarantee after implementation.

### 7.1 Structure and copy (C01–C18)

| # | Requirement | Test |
|---|-------------|------|
| C01 | H1 «Гарантия на оборудование» via page-intro | View source / visual |
| C02 | Lead paragraph present with About + Delivery links | Click `/about`, `/delivery` |
| C03 | BLOCK 01 — coverage outcome table (5 rows) | Count rows |
| C04 | BLOCK 01 summary row (4 micro-labels) | Ответственный · Производство · Основание · Сопровождение |
| C05 | BLOCK 01 cert disclaimer one-line | Cert ≠ warranty |
| C06 | BLOCK 02 — document checklist (6 rows) | SC-06 present |
| C07 | **Claim procedure section exists** | BLOCK 03 landmark |
| C08 | **5 steps** in timeline | Count step badges |
| C09 | Step 1 includes phone, email, form reference | Text match |
| C10 | BLOCK 04 verification cases (7 bullets) | Count bullets |
| C11 | BLOCK 05 service outcomes (6 rows) | Count rows |
| C12 | **FAQ — 8 items** | Count accordion items |
| C13 | CTA H2 «Связаться по вопросу гарантии» | Exact match |
| C14 | Form title «Обращение по гарантии» | Present |
| C15 | **equipment_model field required** | HTML `required` |
| C16 | **comment (issue description) field required** | HTML `required` |
| C17 | purchase_date field optional | No `required` |
| C18 | All copy spot-check (10 strings) vs copy v1 | Diff against copy doc |

### 7.2 Warranty logic (W01–W08)

| # | Requirement | Test |
|---|-------------|------|
| W01 | **No unified warranty months** on page | No «12 мес» badge unless operator unlock |
| W02 | BLOCK 04 **subordinate** to BLOCK 03 visually | Design review / CSS weight |
| W03 | Process-dominant — not exclusion-first hierarchy | No «когда не действует» as top H2 |
| W04 | Manufacturer accompaniment framing in lead | Text present |
| W05 | Dealer channel pointer in BLOCK 02 / FAQ 4 | Link `/dealers` |
| W06 | Custom equipment pointer in BLOCK 02 / FAQ 5 | Link `/custom-equipment` |
| W07 | Delivery pointer for logistics context | Link `/delivery` in BLOCK 03 / FAQ 3 |
| W08 | Payment separated from claim (BLOCK 05) | Link `/payment-methods` only |

### 7.3 Forbidden content (F01–F08)

| # | Requirement | Test |
|---|-------------|------|
| F01 | **No ASC / service-center map** | DOM search map embeds |
| F02 | **No warranty term hero badge** | No «12 мес» / «24 мес» chip above fold |
| F03 | No red warning / alert exclusion boxes | Visual + class audit |
| F04 | No warranty certificate mockup hero | — |
| F05 | No repair-shop hero imagery | — |
| F06 | No mid-page primary submit button | Single CTA zone at bottom |
| F07 | No TK tables / shipment points | Delivery scope only |
| F08 | No bank/invoice/payment method bodies | Payment scope only |

### 7.4 FAQ (Q01–Q05)

| # | Requirement | Test |
|---|-------------|------|
| Q01 | FAQ accordion **single-open** | Click two headers |
| Q02 | `aria-expanded` toggles on buttons | DevTools / a11y |
| Q03 | `aria-controls` links button to panel id | Attribute audit |
| Q04 | Panels use `hidden` when closed | DOM state |
| Q05 | FAQ 1 answers term without inventing months | Text match copy |

### 7.5 Accordion technical (A01–A03)

| # | Requirement | Test |
|---|-------------|------|
| A01 | Root `data-warranty-faq` present | Attribute on section |
| A02 | Re-click open item closes it | Click behaviour |
| A03 | No conflict with mobile menu accordion | Mobile nav still works |

### 7.6 Responsive (R01–R04)

| # | Requirement | Test |
|---|-------------|------|
| R01 | Desktop ≥1440 — timeline + tables readable | Screenshot |
| R02 | Tablet 1024 — checklist/timeline stack | No overflow |
| R03 | Mobile 390 — FAQ usable, form full width | Screenshot |
| R04 | **No horizontal overflow** 390/1024/1440 | DevTools |

### 7.7 Console, overflow, ARIA (T01–T10)

| # | Requirement | Test |
|---|-------------|------|
| T01 | **No console errors** on load | Browser devtools |
| T02 | **Commercial Trust CTA architecture reused** | `zpm-commercial-trust__card` or equivalent |
| T03 | **Contacts form discipline** | `zpm-form`, mask, email validate, consent |
| T04 | **No duplicate CSS file** on live | Single `style.css` append |
| T05 | Breadcrumb Главная → Гарантия | Present |
| T06 | Meta title/description match copy utility | `<title>` + meta |
| T07 | Header/footer/nav unchanged | Visual compare |
| T08 | `/guarantee` HTTP 200 | curl -L |
| T09 | Twig cache cleared after deploy | Operator confirm |
| T10 | Timeline `<ol>` has accessible label | `aria-label` or visible caption |

### 7.8 Commercial Trust + cross-surface (X01–X03)

| # | Requirement | Test |
|---|-------------|------|
| X01 | Delivery page `/guarantee` links still valid | Sample Delivery FAQ |
| X02 | No full PLP Commercial Trust block duplicated on page | DOM |
| X03 | Phone `8 (3852) 72-18-90` and `info@bzpm.ru` in CTA | Present |

**Total checklist items: 54** (exceeds minimum 45).

---

## 8. Rollback

**Without implementation** — planned recovery path only.

### 8.1 Files affected (implementation task)

| Priority | Remote file |
|----------|-------------|
| P1 | `catalog/view/theme/default/template/information/guarantee.twig` |
| P2 | `catalog/controller/information/guarantee.php` |
| P3 | `assets/css/style.css` (append reversal) |
| P4 | `assets/js/main.js` (accordion selector delta) |
| P5 | `oc_seo_url` guarantee row |

### 8.2 Rollback order

1. Restore `oc_seo_url` → prior `information/information&information_id=…` target  
2. Delete or restore `guarantee.php` from backup (if new file — remove)  
3. Delete or restore `guarantee.twig` from backup  
4. Restore `style.css` from `backups/style.css.pre-m9.17-warranty.bak`  
5. Restore `main.js` from `backups/main.js.pre-m9.17-warranty.bak`  
6. Clear `system/storage/cache/template/*`  
7. Verify `/guarantee` renders legacy CMS content from `m9.17-work/guarantee-live.html` baseline

### 8.3 Rollback checkpoints

| Checkpoint | Trigger | Action |
|------------|---------|--------|
| **RB-0** | Pre-deploy | `preflight-manifest.json` SHA256 |
| **RB-1** | Controller/route broken | Revert seo_url + remove guarantee.php only |
| **RB-2** | Visual/CSS failure | Restore twig + style.css |
| **RB-3** | JS regression | Restore main.js; static FAQ remains usable expanded |
| **RB-4** | Catastrophic | Operator Beget full backup |

### 8.4 Minimal recovery path

**Minimum files to restore legacy `/guarantee`:** seo_url row + remove `guarantee.twig` + remove `guarantee.php` → generic information page returns.

---

## 9. Stable checkpoint criteria

**Checkpoint name:** `SITE-002-STABLE-LIVE-M9.17-WARRANTY-01`

Implementation becomes this checkpoint **when all are true**:

| # | Criterion |
|---|-----------|
| S1 | `/guarantee` serves `information/guarantee` custom template on live TEST |
| S2 | Acceptance checklist §7 — **all C, W, F, Q, A, R, T, X** items PASS (operator HITL for visual where marked) |
| S3 | Deploy manifest with SHA256 pre/post stored in `reports/m9.17-work/` |
| S4 | Backups exist for every overwritten remote file |
| S5 | No scope bleed — header/footer/catalog/About/Delivery/Payment/Contacts untouched |
| S6 | Baseline doc registered at `baselines/SITE-002-STABLE-LIVE-M9.17-WARRANTY-01.md` |
| S7 | Knowledge Map updated with §20 Warranty page entry |
| S8 | No numeric warranty term published unless operator B2/OQ-W01 explicitly unlocked and documented |
| S9 | BLOCK 04 verification remains visually subordinate to BLOCK 03 process |
| S10 | Recovery remains **CLOSED** — checkpoint is forward progress |

**Authority after checkpoint:** Supersedes prior generic `/guarantee` CMS surface **for warranty page domain only** — M9.14 Delivery + M9.15 Payment checkpoints otherwise unchanged.

---

## 10. Risks

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R1 | **Term badge drift** from PDP «12 мес» work copy | **High** | Charter lock — no months without OQ-W01; FAQ 1 prose only |
| R2 | **Exclusion wall** — BLOCK 04 dominates process | **High** | CSS weight cap 2/5; calm framing mandatory |
| R3 | seo_url mis-edit breaks `/guarantee` | **High** | Preflight capture + RB-1 |
| R4 | **PDP/PLP/corp term mismatch** (OQ-W17) | **Critical** | Document governance; no invented badge on corp page |
| R5 | Live legacy exclusion-first hierarchy replicated | **High** | Process spine BLOCK 03 at 5/5 |
| R6 | Form scope creep (photo upload, serial field) | **Medium** | §3.7 MVP lock — OQ-W14 deferred |
| R7 | FAQ accordion JS conflicts with mobile menu | **Medium** | Scoped `[data-warranty-faq]` root init |
| R8 | Trust strip + summary row duplicate density | **Medium** | OQ-DC-W03 — pick one at step 6 |
| R9 | `style.css` drift vs repo backups | **Medium** | Live FTP capture at preflight |
| R10 | Operator gates B6/B8 open at deploy | **Medium** | Record operator ack in implementation report |
| R11 | Delivery inbound links expect depth — page still generic | **Medium** | M9.17 closes cross-link promise |
| R12 | Form `action="#"` — no backend | **Low** | Same as Contacts/Delivery/Payment — documented SAFE UNKNOWN |
| R13 | Legacy CMS information HTML orphaned | **Low** | Keep admin entry; do not delete |
| R14 | SC-04 fatigue — fourth corp timeline | **Low** | Distinct 5-step warranty labels; shared CSS |
| R15 | Fear-based red styling on BLOCK 04 | **Medium** | Forbidden patterns §2.4; QA F03 |
| R16 | Production URL parity unknown (OQ-W20) | **Low** | TEST-first; document at deploy |

**SECURITY RISK:** Deploy scripts may contain FTP credentials — never commit credentials; use operator-local secrets only.

---

## 11. Ready for implementation

### 11.1 Architectural uncertainty closure

| Domain | Status |
|--------|--------|
| Page structure and block order | **CLOSED** |
| Component reuse vs new build | **CLOSED** |
| File touch list | **CLOSED** |
| Route strategy | **CLOSED** (`information/guarantee`) |
| Visual hierarchy (process-dominant) | **CLOSED** |
| Forbidden patterns | **CLOSED** |
| Form MVP fields | **CLOSED** |
| Rollback path | **CLOSED** |
| QA criteria | **CLOSED** |
| Cross-check vs Delivery/Payment | **CLOSED** |

### 11.2 Remaining operator actions (not architectural)

| Item | Blocks coding? | Blocks deploy? |
|------|----------------|----------------|
| B6/B8 formal sign-off | No | Recommended before deploy |
| B2/OQ-W01 warranty term publish | No — default no badge | **Yes** if term badge requested |
| OQ-DC-W03 trust strip vs summary row | **Pick one at step 6** | No |
| OQ-DC-W11 cross-links footer table | Optional at step 13 | No |

### 11.3 Final verdict

## **READY**

**Justification:** All implementation architecture decisions required to start the M9.17 coding task are documented. Route, file map, section mapping (Hero → principles → coverage → documents → claim procedure → verification/exclusions → service outcomes → FAQ → CTA+form), component matrix, execution order, 54 acceptance tests, rollback, and stable checkpoint are defined. Architecture aligns with M9.14 Delivery and M9.15 Payment Corporate Pages language while preserving warranty-specific process-dominant service posture per Design Charter and copy v1. No new UX invented beyond authority artefacts.

**Next task:** M9.17 Warranty **implementation** — begin at Execution order step 1 (preflight capture). Do not deploy until acceptance checklist passes and operator addresses B2 if term badge sync is required.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-28 | **CREATED** — M9.17 Warranty Implementation Charter v1 |

---

*Documentation only. No OpenCart files were modified during this task.*
