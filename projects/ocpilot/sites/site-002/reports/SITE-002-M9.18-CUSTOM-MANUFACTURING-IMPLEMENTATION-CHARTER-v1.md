# REPORT — SITE-002 M9.18 CUSTOM MANUFACTURING IMPLEMENTATION CHARTER

**Milestone:** M9.18 — Custom Manufacturing / Оборудование на заказ  
**Project:** OCPilot · SITE-002 (ЗПМ / BZPM)  
**Environment (TEST):** https://zpm.new-site.space/custom-equipment  
**Branch:** `mars/canonical-post-recovery`  
**Authority:** `SITE-002-STABLE-LIVE-M9.16-DEALERS-01` (+ M9.14 Delivery · M9.15 Payment · M9.17 Warranty · M9.13 About Restored for non-corp scope)  
**Version:** v1  
**Date:** 2026-06-28  
**Mode:** Documentation only — **no** OpenCart · **no** Twig/CSS/JS · **no** deploy · **no** FTP · **no** TEST writes

**Boundary:** Definitive implementation blueprint for the final Corporate Pages Program coding task. This document authorizes **planning clarity only**; runtime changes require a separate implementation task after operator gates.

**Central page question:** «Какие нестандартные изделия ЗПМ может изготовить, как происходит работа и как начать проект?»

**Page positioning (locked):** Manufacturer capability page — **not** a service catalog, **not** a technical specification article, **not** a КП/tender form portal. Visual order: **Capability → Process → Requirements → Outcome → Form**.

---

## 1. Authority

### 1.1 Primary sources (use only these)

| # | Artefact | Path | Role |
|---|----------|------|------|
| A1 | **PAGE COPY (canonical)** | [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md](../copy/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md) | All visible text — single copy authority |
| A2 | **Design Charter** | [BZPM-M9.18-CUSTOM-MANUFACTURING-DESIGN-CHARTER-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.18-CUSTOM-MANUFACTURING-DESIGN-CHARTER-v1.md) | Visual hierarchy, forbidden patterns, SC mapping, manufacturer-capability mode |
| A3 | **Design Brief** | [BZPM-M9.18-CUSTOM-MANUFACTURING-DESIGN-BRIEF-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.18-CUSTOM-MANUFACTURING-DESIGN-BRIEF-v1.md) | Designer-facing priorities |
| A4 | **Visual Design / shared components** | [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md) § SC-01–SC-15 | Component registry and corp rhythm |
| A5 | **Corporate Pages Program** | [BZPM-CORPORATE-PAGES-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-v1.md) · [IA Map § M9.18](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-IA-MAP-v1.md#m918--custom-manufacturing-custom-equipment) | CP-01 ownership · program terminal page |
| A6 | **Copy Standards** | [BZPM-COPY-STANDARDS-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-COPY-STANDARDS-v1.md) | Tone · SAFE UNKNOWN discipline |
| A7 | **Forensic Research** | [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) · `m9.18-work/custom-equipment-live.html` (preflight target) | Live surface facts and gaps |
| A8 | **SITE-002 implementation patterns** | [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) §18–22 | Delivery/Payment/Warranty/Dealers corp page discipline |
| A9 | **Delivery implementation (precedent)** | [SITE-002-M9.14-DELIVERY-IMPLEMENTATION-CHARTER-v1.md](SITE-002-M9.14-DELIVERY-IMPLEMENTATION-CHARTER-v1.md) · [SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md](SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md) | Route migration · timeline · FAQ · CTA pattern |
| A10 | **Payment implementation (precedent)** | [SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md](SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md) | SC-04 reuse · commercial gates |
| A11 | **Warranty implementation (precedent)** | [SITE-002-M9.17-WARRANTY-IMPLEMENTATION-CHARTER-v1.md](SITE-002-M9.17-WARRANTY-IMPLEMENTATION-CHARTER-v1.md) · [SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md](SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md) | Latest corp cutover · inbound custom links |
| A12 | **Dealers implementation (precedent)** | [SITE-002-M9.16-DEALERS-IMPLEMENTATION-CHARTER-v1.md](SITE-002-M9.16-DEALERS-IMPLEMENTATION-CHARTER-v1.md) · [SITE-002-M9.16-DEALERS-IMPLEMENTATION.md](SITE-002-M9.16-DEALERS-IMPLEMENTATION.md) | Company field on corp form · OEM proof stack |
| A13 | **Commercial Trust pattern** | [SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md](SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md) | CTA/form/card language · PLP «На заказ» secondary surface |
| A14 | **Contacts implementation** | [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md) | Internal-page shell · `zpm-form` · spacing rhythm |
| A15 | **site-passport** | [site-passport.md](../site-passport.md) | Operator order · blockers |
| A16 | **OCPILOT-STATE** | [OCPILOT-STATE.md](../../OCPILOT-STATE.md) | Program status |

### 1.2 Operator authority

| Gate | Status | M9.18 impact |
|------|--------|--------------|
| B6 Design Charter approval | OPEN (header pending) | Task treats Design Charter as authority input |
| B8 Copy sign-off | OPEN | Implementation uses copy v1.1 text |
| B1 МО warehouse address | OPEN | **No impact** — no street address on Custom page |
| B3 Dealers PLP form | OPEN | **No impact** — Custom page only; dealer pointer = link |

### 1.3 Preflight synthesis (runtime facts)

| Fact | Evidence | Implementation implication |
|------|----------|----------------------------|
| URL `/custom-equipment` resolves today | Forensic §1.1 | Preserve public URL; change route target only |
| Alternatives `/izgotovlenie-pod-zakaz`, `/custom-manufacturing` **not used** | Forensic §1.1 | Do not create alternate routes |
| Current route likely `information/information` + CMS `information_id` | Forensic §1.1 — **SAFE UNKNOWN** exact ID | Pre-implementation FTP capture must confirm; target route **`information/custom_equipment`** |
| Nav position **#1** in corp strip | Forensic §1.2 | Page must deliver strategic depth — not SEO stub |
| No `zpm-custom-*` namespace on live | Forensic §2 | **New** scoped CSS block required |
| Body = generic `zpm-seo` prose — no CTA, no form | Forensic §2–3 | Replace with structured sections; process-dominant |
| Pageintro = H1 only, **no lead** | Live capture inference | Add `$pageintro->description` with copy Lead |
| Inbound links from Delivery, Payment, Warranty, Dealers | M9.14–M9.17 live twig | Custom page must satisfy cross-link promise |
| Form backend | Contacts/Delivery/Payment pattern `action="#"` | Preserve — **no** new backend, **no** CRM, **no** upload MVP |
| Commercial Trust «На заказ» chip | M9.8.9 — link depth **gap** on live | Custom page = authoritative depth; PLP link update = separate task |

### 1.4 SAFE UNKNOWN (charter-level)

| Topic | Status | Charter handling |
|-------|--------|------------------|
| OpenCart `information_id` for `custom-equipment` | **SAFE UNKNOWN** | Capture at preflight; do not delete legacy CMS entry |
| Production `/custom-equipment` parity (OQ-C20 prod) | **SAFE UNKNOWN** | TEST-first; document at deploy |
| Lead-time bands / quote SLA (OQ-DC-C03, C04) | **SAFE UNKNOWN** | **No countdown chips** — timeline note + FAQ 7 prose only |
| Price range / calculator (OQ-DC-C19) | **SAFE UNKNOWN** | **Exclude** — no estimate UI |
| MOQ badge (OQ-DC-C02) | **SAFE UNKNOWN** | **Exclude** |
| File upload backend (OQ-DC-C17) | **SAFE UNKNOWN** | **No upload field** — `drawings` = optional text note; email fallback in helper |
| Production photo asset (OQ-DC-C25) | **SAFE UNKNOWN** | BLOCK 04 image slot — reuse About factory if attested; else hide slot |
| Case study gallery (OQ-DC-C16) | **SAFE UNKNOWN** | **Exclude** — no placeholder portfolio |
| AISI grade universal table (OQ-DC-C08) | **SAFE UNKNOWN** | BLOCK 07 prose + disclaimer only |
| Custom warranty term months | **SAFE UNKNOWN** | Link `/guarantee` — no term badge |
| Privacy policy route | **Assumed** `/privacy-policy` | Verify at preflight |
| Dedicated `zakaz@` email | **Assumed** `info@bzpm.ru` | Per copy v1.1 MICRO |
| Value chips vs approval gate badge (OQ-DC-C21) | **OPEN** | Pick **one** heavy first-screen accent at step 6 — not both |

### 1.5 Copy vs charter form lock (task authority)

Copy v1.1 FORM block lists `product_type` select, `region`, `quantity`, `deadline`, `catalog link`, and **file upload**. This charter **locks MVP form** per implementation task authority:

| Charter field | Copy mapping | Notes |
|---------------|--------------|-------|
| **company** (req) | FORM «Организация» | Required per charter; optional in copy — charter wins |
| **contact** (req) | «Контактное лицо» | |
| **phone** (req) | «Телефон» | `data-mask="phone"` |
| **email** (req) | «E-mail» | `data-validate="email"` |
| **project_description** (req) | «Описание задачи» + guidance for type/region/size | Placeholder/helper carries copy checklist hints |
| **drawings** (opt) | Copy file-upload intent → **text note only** | «Есть чертёж/фото — опишите или укажите в примечании» |
| **notes** (opt) | Quantity, deadline, catalog SKU — **collapsed here** | Optional catch-all |

**Excluded from MVP:** file upload UI · multi-file wizard · product_type `<select>` · CRM routing · price calculator · `dialog=` handler design beyond Contacts parity.

### 1.6 Superseded — do not use

| Artefact | Reason |
|----------|--------|
| [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.md](../copy/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.md) | Superseded by v1.1 |
| Live generic `zpm-seo` custom-equipment HTML | Replaced entirely by custom implementation |
| Concept B «Minimal Brief only» | Rejected in forensic research — insufficient for nav #1 |
| Concept C «Project Type Matrix as page spine» | Rejected as dominant — matrix is supporting only (BLOCK 02) |
| Online configurator / tender portal patterns | Design Charter forbidden |
| Global modal-only custom path (`#zpmFbQuestion` without dedicated form) | Dedicated FORM required |
| SC-11 file-upload-first intake (design program label) | Charter uses **SC-10** Contacts pattern — no upload MVP |
| Fake case study gallery / stock kitchen photos | Asset rule |

---

## 2. Implementation architecture

### 2.1 Page feel (locked)

**Manufacturer capability page** — process-dominant with outcome second, not catalog PLP, not engineering datasheet, not «send TZ and wait» form-first page. Align internal-page rhythm with Delivery/Payment/Warranty/Dealers/Contacts (`page--inner`, breadcrumb → page-intro → `<main>`).

**Visual hierarchy (locked):**

| Rank | Element | Weight |
|------|---------|--------|
| **1** | BLOCK 05 — 8-step process timeline (SC-04) | **5/5** — page spine |
| **2** | BLOCK 08 — project outcomes (SC-07) | **3–4/5** — second emphasis |
| **3** | BLOCK 04 — OEM capability proof | **4/5** — competence evidence |
| **4** | BLOCK 06 — requirements checklist | **4/5** — subordinate to timeline |
| **5** | BLOCK 03 — scope boundaries | **4/5** — honest specialization |
| **6** | BLOCK 10 + FORM | **4/5** — endpoint only |

### 2.2 Target render chain

```
GET /custom-equipment
  └─ index.php → route information/custom_equipment     [NEW — replaces generic information/information]
       └─ catalog/controller/information/custom_equipment.php
            ├─ document: meta title, description, keywords, bodyClass page--inner
            ├─ Breadcrumbs → global chrome
            ├─ Pageintro → H1 «Оборудование на заказ» + Lead (copy)
            └─ catalog/view/theme/default/template/information/custom_equipment.twig
                 └─ <main class="main zpm-custom-page">
                      ├─ [optional] value chips (MICRO — 3 labels)
                      ├─ § LANDMARK 01 — Hero zone (pageintro — external)
                      ├─ § LANDMARK 02 — when custom needed (BLOCK 01 + BLOCK 02)
                      ├─ § LANDMARK 03 — what we can make (BLOCK 03 + BLOCK 04 OEM)
                      ├─ § LANDMARK 04 — process timeline (BLOCK 05 SC-04)
                      ├─ § LANDMARK 05 — customer requirements (BLOCK 06 + BLOCK 07)
                      ├─ § LANDMARK 06 — project outcomes (BLOCK 08)
                      ├─ § LANDMARK 07 — FAQ (BLOCK 09 SC-08)
                      └─ § LANDMARK 08 — CTA + FORM (BLOCK 10 + SC-09/SC-10)
       └─ assets/css/style.css → appended zpm-custom-* (~480–580 lines est.)
       └─ assets/js/main.js → extend corp FAQ accordion with [data-custom-faq]
```

**SEO URL migration:** Update `oc_seo_url` entry for keyword `custom-equipment` from `information/information&information_id=…` to `information/custom_equipment` during controller step. Confirm via preflight capture before edit.

### 2.3 Section architecture — eight landmarks + copy blocks

User-facing landmarks map to copy blocks. Supporting blocks stay **inside** their landmark — not separate nav-level sections.

---

#### LANDMARK 01 — Hero (SC-01 shell + lead zone)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Immediate capability frame: manufacturer makes neutral SS to order in Барнаул |
| **UX goal** | Answers «может ли завод взять мой проект?» in <15s — without form |
| **Copy source** | Utility meta · Breadcrumb · H1 · Lead · optional value chips (MICRO) |
| **Shared component** | **SC-01** — Contacts/Delivery corp `page-intro` pattern |
| **Visual weight** | Tier 1 (**3/5**) — frame, not hero media |
| **Implementation notes** | H1 + Lead in `Pageintro`; optional 3 value chips under lead (OQ-DC-C21); **no** form above fold; **no** price/lead badges |
| **Dependencies** | `custom_equipment.php` controller; `Pageintro` class |

---

#### LANDMARK 02 — Когда требуется изготовление на заказ

| Attribute | Spec |
|-----------|------|
| **Purpose** | Self-qualification — when catalog SKU is insufficient |
| **UX goal** | Trigger scan — buyer knows if custom path applies |
| **Copy source** | BLOCK 01 (full) + BLOCK 02 task matrix (supporting) |
| **Shared component** | SC-07 matrix — BLOCK 02 task list (7 rows) |
| **Visual weight** | Tier 1 (**3/5**) BLOCK 01 · Tier 2 (**3/5**) BLOCK 02 |
| **Implementation notes** | BLOCK 01 bullets + scope boundary microcopy (neutral SS only); catalog link for thermal; BLOCK 02 table stacks ≤1024px |
| **Dependencies** | Inline links `/` catalog |

---

#### LANDMARK 03 — Что можем изготовить

| Attribute | Spec |
|-----------|------|
| **Purpose** | Honest product scope — boundaries, not second catalog |
| **UX goal** | «Что можно заказать» without PLP mimic |
| **Copy source** | BLOCK 03 (scope groups + in/out table) + BLOCK 04 (OEM trust layer) |
| **Shared component** | SC-07 scope table · **SC-05** proof strip + production image (BLOCK 04) · SC-03 trust row variant |
| **Visual weight** | Tier 1 (**4/5**) BLOCK 03 · Tier 1 (**4/5**) BLOCK 04 |
| **Implementation notes** | Prose scope groups with inline category links — **no** SKU cards; in/out table labeled; BLOCK 04 H3 stack + proof strip + **one** production image slot; «Сделано в России» badge → `/our-certification` |
| **Dependencies** | About `/about` link; image hide if no attested asset |

---

#### LANDMARK 04 — Как проходит работа (SC-04 owner — page spine)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Primary mental model — inquiry to shipment |
| **UX goal** | Full 8-step process scannable in <25s desktop; steps 1–3 visible early |
| **Copy source** | BLOCK 05 H2 · Intro · 8 process steps · Timeline note · Approval gate badge · Payment/Delivery inline links |
| **Shared component** | **SC-04** `zpm-corp-timeline` — **sixth corp instantiation**; 8 custom-specific steps |
| **Visual weight** | Tier 1 (**5/5**) — **dominant page element** |
| **Reuse source** | `zpm-corp-timeline` CSS from M9.14–M9.17; extend step count to **8** |
| **Implementation notes** | Badge «Согласование до производства»; **no** SLA day chips; `aria-label` on `<ol>`; steps 5+8 link Payment/Delivery |
| **Dependencies** | CSS grid/flex; no JS required for static timeline |

---

#### LANDMARK 05 — Что потребуется от заказчика

| Attribute | Spec |
|-----------|------|
| **Purpose** | Practical data checklist — enables timeline steps 1–2 |
| **UX goal** | «Что передать для расчёта» without tender UX |
| **Copy source** | BLOCK 06 (9-row checklist + helpers) + BLOCK 07 materials (supporting prose) |
| **Shared component** | SC-07 checklist table variant (BLOCK 06) · optional MICRO parameter companion table (weight 2/5) |
| **Visual weight** | Tier 1 (**4/5**) BLOCK 06 · Tier 2 (**2/5**) BLOCK 07 |
| **Implementation notes** | Checklist reads as «подготовка к шагам 1–2» — visual affinity to SC-04; friction-reduction note; **no** universal steel grade table; BLOCK 07 disclaimer visible |
| **Dependencies** | Table → stacked rows ≤1024px |

---

#### LANDMARK 06 — Результат проекта

| Attribute | Spec |
|-----------|------|
| **Purpose** | Predictability — what buyer receives |
| **UX goal** | Outcome table — **second visual emphasis** on page |
| **Copy source** | BLOCK 08 H2 · Intro · 5 outcome rows · document/warranty/delivery pointers |
| **Shared component** | **SC-07** outcome table |
| **Visual weight** | Tier 1 (**3–4/5**) — deliberate second anchor after timeline |
| **Reuse source** | Delivery/Warranty outcome row anatomy |
| **Implementation notes** | 5 rows; links to `/payment-methods`, `/guarantee`, `/delivery` only — not embedded bodies |
| **Dependencies** | Responsive stack ≤1024px |

---

#### LANDMARK 07 — FAQ (SC-08)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Objection resolver — scope, design owner, timing, warranty, misfit |
| **UX goal** | Single-open accordion; 8 items exactly |
| **Copy source** | BLOCK 09 (8 Q&A) + footer microcopy |
| **Shared component** | **SC-08** `zpm-corp-faq` |
| **Visual weight** | Tier 2 (**3/5**) |
| **Reuse source** | Delivery/Payment/Warranty/Dealers FAQ — add `[data-custom-faq]` scope |
| **Implementation notes** | `<button aria-expanded aria-controls>`; one open at a time; FAQ must not repeat full timeline |
| **Dependencies** | Extend `main.js` selector list |

---

#### LANDMARK 08 — CTA + Form (SC-09 + SC-10)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Quote request initiation — primary conversion at page bottom |
| **UX goal** | One primary button zone after education; phone parallel in header |
| **Copy source** | BLOCK 10 · FORM titles/helpers (adapted to charter fields) · Dealer pointer |
| **Shared component** | Commercial Trust `zpm-commercial-trust__card` + **SC-09** CTA band + **SC-10** `zpm-form` |
| **Visual weight** | Tier 1 (**4/5**) — endpoint, not page identity |
| **Implementation notes** | Primary: «Отправить заявку на расчёт»; `action="#"`; **no** mid-page submit; secondary `/contact/`; tertiary catalog `/` |
| **Dependencies** | Contacts form hooks; consent `/privacy-policy` |

---

### 2.4 Forbidden globally

Configurator/calculator · price/lead-time badges · tender multi-upload portal · SKU grid/PLP cards in BLOCK 03 · fake case gallery · DWG viewer embed · form above fold · mid-page primary submit · universal AISI table hero · thermal/refrigeration custom upsell · full Payment/Delivery/Warranty/Dealers bodies · TK tables · bank requisites · ASC map · CRM integration · file upload MVP.

---

## 3. Final OpenCart architecture

### 3.1 Route

| Item | Value |
|------|-------|
| Public URL | `/custom-equipment` (unchanged) |
| OpenCart route | `information/custom_equipment` |
| Prior route (inferred) | `information/information&information_id=…` — confirm at preflight |
| SEO keyword | `custom-equipment` |

### 3.2 Controller

| File | Status | Responsibility |
|------|--------|----------------|
| `catalog/controller/information/custom_equipment.php` | **NEW** | Meta SEO, breadcrumbs, Pageintro H1+lead, load view (~70–100 lines) |
| `catalog/controller/information/information.php` | **UNTOUCHED** | Generic CMS pages remain |

### 3.3 Twig

| File | Status | Responsibility |
|------|--------|----------------|
| `catalog/view/theme/default/template/information/custom_equipment.twig` | **NEW** | All landmarks BLOCK 01–10 + FORM (~550–700 lines est.) |
| `common/header.twig` / `footer.twig` | **UNTOUCHED** | Global chrome |
| `information/information.twig` | **UNTOUCHED** | Not used for `/custom-equipment` after cutover |

**Optional partial (defer if twig > ~700 lines):**

| File | Status | Reason |
|------|--------|--------|
| `catalog/view/theme/default/template/sections/blockcustomform.twig` | **NEW (optional)** | Extract FORM — mirror other corp form partials |

### 3.4 SEO

| Location | Content source |
|----------|----------------|
| `custom_equipment.php` → `setTitle()` | Copy utility Meta title |
| `custom_equipment.php` → `setDescription()` | Copy utility Meta description |
| `oc_seo_url` row `keyword=custom-equipment` | **MODIFIED** → `information/custom_equipment` |
| OG tags | Existing theme behaviour — verify at QA |

### 3.5 CSS

| File | Status | Responsibility |
|------|--------|----------------|
| `assets/css/style.css` | **MODIFIED (append)** | `zpm-custom-page` namespace (~480–580 lines) |
| `reports/m9.18-work/m9.18-custom-page.css` | **NEW (repo work copy)** | Staging before append |

**Shared classes reused:** `zpm-corp-timeline`, `zpm-corp-faq__*`, `zpm-form__*`, `zpm-commercial-trust__*`, `section-title__like-h2`.

**Page-scoped classes (new):** `zpm-custom-page`, `zpm-custom-section`, `zpm-custom-triggers`, `zpm-custom-scope`, `zpm-custom-oem`, `zpm-custom-process`, `zpm-custom-requirements`, `zpm-custom-materials`, `zpm-custom-outcomes`, `zpm-custom-faq`, `zpm-custom-cta`.

### 3.6 JS

| File | Status | Responsibility |
|------|--------|----------------|
| `assets/js/main.js` | **MODIFIED (minimal)** | Add `[data-custom-faq]` to corp accordion init (~5–15 lines delta) |
| `reports/m9.18-work/m9.18-corp-accordion.js` | **NEW (repo staging)** | Updated selector list if extracted |

### 3.7 Form (SC-10 — Contacts pattern)

| Item | Spec |
|------|------|
| Location | Bottom CTA section inside `custom_equipment.twig` |
| Classes | `zpm-form`, `zpm-form__*` — Contacts parity |
| Fields (MVP) | **company**, **contact**, **phone**, **email**, **project_description** (all req); **drawings**, **notes** (opt text) |
| Hooks | `data-mask="phone"`, `data-validate="email"`, `required` on mandatory |
| Backend | `action="#"` — unchanged posture |
| Upload | **FORBIDDEN** in MVP — drawings = textarea/note; helper mentions `info@bzpm.ru` |
| Field IDs | Prefix `custom*` — consistent within page |

### 3.8 FAQ accordion

| Item | Spec |
|------|------|
| Root hook | `data-custom-faq` + `data-accordion` |
| Item hooks | `data-accordion-button`, `data-accordion-panel` |
| Count | **8 items** |
| Behaviour | Single-open; toggle close on re-click |
| CSS namespace | `zpm-corp-faq` (shared) + `zpm-custom-faq` (page scope) |

### 3.9 Breadcrumbs

| Item | Source |
|------|--------|
| Trail | Главная → Оборудование на заказ |
| Template | `common/header.twig` — **no change** |

---

## 4. Shared component reuse

### 4.1 Matrix

| Component | Source page / artefact | Reuse as-is | Adapt for Custom | Create new | Forbidden |
|-----------|------------------------|-------------|------------------|------------|-----------|
| **SC-01 Page shell** | Contacts · M9.14–M9.17 | `page--inner`, pageintro rhythm | H1+lead copy | — | Hero media block |
| **SC-03 Trust row** | Delivery · Dealers | Micro-row / proof strip pattern | BLOCK 04 proof strip | Optional value chips | Both chips + heavy gate badge |
| **SC-04 Timeline** | M9.14–M9.17 | `zpm-corp-timeline` CSS/structure | **8 custom steps** | — | SLA chips |
| **SC-05 Proof cards** | About · Dealers | Proof strip anatomy | BLOCK 04 production image slot | — | Fake portfolio cards |
| **SC-07 Matrix table** | Delivery outcomes | Responsive table/cards | BLOCK 02, 03, 06, 08 tables | — | PLP product cards |
| **SC-08 FAQ accordion** | M9.14–M9.17 | `zpm-corp-faq__*` + JS | 8 custom Q&A | — | FAQ as page hero |
| **SC-09 CTA band** | M9.14–M9.17 | Button hierarchy | Custom H2 + helpers | — | Mid-page primary CTA |
| **SC-10 Form** | Contacts · Payment · Dealers | Core fields + consent | +project_description variant | Custom field set | Upload · CRM · calculator |
| **Commercial Trust** | M9.8.9 PLP | CTA card shell | Custom titles | — | Full PLP block on page |
| **Contacts** | `/contact/` | `zpm-form` discipline | Charter field lock | — | Contact card grid, map |
| **Delivery** | M9.14 live | — | Step 8 + BLOCK 08 pointer | — | TK tables |
| **Payment** | M9.15 live | — | Step 5 + BLOCK 08 pointer | — | Methods matrix |
| **Warranty** | M9.17 live | — | BLOCK 08 + FAQ 5 pointer | — | Claim process body |
| **Dealers** | M9.16 live | — | BLOCK 10 one-line pointer | — | Partner terms body |
| **About** | `/about` restored | — | BLOCK 04 OEM link | — | Factory video hero |

### 4.2 Create for the first time on SITE-002 (this milestone)

| Item | Notes |
|------|-------|
| `custom_equipment.php` controller | New corp page controller |
| `custom_equipment.twig` | Longest corp body — all landmarks |
| `zpm-custom-*` CSS block | Page namespace — appended to style.css |
| SC-10 **custom project form variant** | `project_description` + `drawings` note fields |
| BLOCK 04 production proof image slot | Static image discipline — hide if no asset |

### 4.3 Cross-check vs sibling corp pages

| Dimension | Delivery | Payment | Warranty | Dealers | **Custom (M9.18)** |
|-----------|----------|---------|----------|---------|---------------------|
| Page mode | Logistics | Commercial gates | Service reassurance | Partnership | **Manufacturer capability** |
| Timeline steps | 7 | 6 | 5 | 5 | **8** |
| Timeline weight | 5/5 | 5/5 | 5/5 | 4/5 | **5/5** |
| Second emphasis | Shipment points | Methods matrix | Doc checklist | OEM proof | **Outcome table** |
| Form unique fields | region | company | equipment_model | company+city | **project_description** |
| FAQ count | 8 | 8 | 8 | 8 | **8** |
| Forbidden bleed | map, TK | bank widgets | term badge, ASC | franchise, map | calculator, tender, PLP |

**Program completion note:** M9.18 is the **terminal** Corporate Pages Program implementation milestone. After stable checkpoint, corp implementation phase for M9.13–M9.18 (excluding About restoration) is **complete** — pending operator gates B6/B8 only for formal sign-off.

---

## 5. File map

Remote paths relative to TEST site root unless noted.

### 5.1 NEW (remote + repo work copies)

| Path | Location | Reason |
|------|----------|--------|
| `catalog/controller/information/custom_equipment.php` | Remote | Custom corp controller |
| `catalog/view/theme/default/template/information/custom_equipment.twig` | Remote | Full page body |
| `reports/m9.18-work/custom_equipment.php` | Repo | Work copy controller |
| `reports/m9.18-work/custom_equipment.twig` | Repo | Work copy twig |
| `reports/m9.18-work/m9.18-custom-page.css` | Repo | CSS staging |
| `reports/m9.18-work/m9.18-corp-accordion.js` | Repo | JS staging (optional) |
| `reports/m9.18-work/m918-custom-deploy.py` | Repo | Deploy script |
| `reports/m9.18-work/m918-custom-screenshots.py` | Repo | QA screenshot script |
| `reports/m9.18-work/preflight-manifest.json` | Repo | Pre-deploy SHA256 |
| `reports/m9.18-work/deploy-manifest.json` | Repo | Post-deploy SHA256 |
| `reports/m9.18-work/qa-custom-equipment.html` | Repo | Live HTML capture |
| `reports/m9.18-work/custom-equipment-live.html` | Repo | Preflight baseline capture |
| `baselines/SITE-002-STABLE-LIVE-M9.18-CUSTOM-01.md` | Repo | Stable checkpoint (post-implementation) |
| `qa/m9.18-custom-screenshots/*` | Repo | Viewport screenshots |
| `backups/custom_equipment.php.pre-m9.18-custom.bak` | Repo | Rollback |
| `backups/custom_equipment.twig.pre-m9.18-custom.bak` | Repo | Rollback |
| `backups/style.css.pre-m9.18-custom.bak` | Repo | Rollback |
| `backups/main.js.pre-m9.18-custom.bak` | Repo | Rollback |

### 5.2 MODIFIED

| Path | Location | Reason | Approx. scope |
|------|----------|--------|---------------|
| `assets/css/style.css` | Remote | Append `zpm-custom-*` | ~480–580 lines |
| `assets/js/main.js` | Remote | Add `[data-custom-faq]` to accordion init | ~5–15 lines |
| `oc_seo_url` row `keyword=custom-equipment` | DB/admin | Route cutover | 1 row |

### 5.3 UNTOUCHED

| Path | Reason |
|------|--------|
| `catalog/controller/information/delivery.php` | Out of scope |
| `catalog/controller/information/payment.php` | Out of scope |
| `catalog/controller/information/guarantee.php` | Out of scope |
| `catalog/controller/information/dealers.php` | Out of scope |
| `catalog/controller/information/about.php` | Out of scope |
| All sibling corp twig files | Out of scope |
| `catalog/view/theme/default/template/information/contact.twig` | Out of scope |
| Header/footer/nav templates | Out of scope |
| Catalog/PLP/PDP templates | Out of scope — PLP trust chip link = separate task |
| `blockdealersform.twig` | B3 governance — out of scope |
| OpenCart admin Information entry (legacy CMS) | Orphaned after cutover — keep for rollback |

### 5.4 QA / backups discipline

| Item | Rule |
|------|------|
| Preflight | Live FTP capture **before** any remote write |
| Backups | One `.bak` per file overwritten |
| Manifest | SHA256 pre/post in `m9.18-work/` |
| Twig cache | Clear after deploy |
| Credentials | Deploy scripts — operator-local only; **never commit secrets** |

---

## 6. Execution order

Exact implementation sequence — **24 steps** — do not skip stages.

| Step | Stage | Deliverable | Stop gate |
|------|-------|-------------|-----------|
| **1** | **Preflight capture** | FTP/live capture: `information_id`, seo_url row, `style.css` SHA, `custom-equipment-live.html` | `preflight-manifest.json` written |
| **2** | **Backups** | `.bak` for any file that will be overwritten | 4 backup files in `backups/` |
| **3** | **Controller** | `custom_equipment.php` — meta, breadcrumbs, pageintro with Lead | PHP syntax OK |
| **4** | **Route / SEO** | Repoint `/custom-equipment` → `information/custom_equipment` | URL hits new controller |
| **5** | **Twig skeleton** | `custom_equipment.twig` — `<main class="zpm-custom-page">` empty landmarks | Page loads empty sections |
| **6** | **Hero / pageintro** | Lead in pageintro; optional value chips **or** skip per OQ-DC-C21 | H1+lead visible |
| **7** | **When custom needed** | BLOCK 01 triggers + scope note | Neutral SS boundary present |
| **8** | **Task matrix** | BLOCK 02 — 7-row SC-07 table | Stacks mobile |
| **9** | **What we can make** | BLOCK 03 scope groups + in/out table | **No** SKU cards |
| **10** | **OEM capability** | BLOCK 04 — H3 stack + proof strip + image slot | About/cert links work |
| **11** | **Process timeline** | BLOCK 05 — **8-step SC-04** + approval badge | **Dominant visual** — 5/5 |
| **12** | **Requirements checklist** | BLOCK 06 — 9-row checklist + helpers | Visual bridge to timeline |
| **13** | **Materials** | BLOCK 07 — prose + disclaimer | Weight 2/5 — no grade table |
| **14** | **Project outcomes** | BLOCK 08 — 5 outcome rows | Second emphasis anchor |
| **15** | **FAQ** | BLOCK 09 — accordion markup + JS hook | 8 items; single-open |
| **16** | **CTA + form** | BLOCK 10 + FORM — charter field lock | **No** upload field |
| **17** | **CSS integration** | Append `zpm-custom-*` to `style.css` | Timeline dominates; outcomes second |
| **18** | **JS integration** | Extend accordion init for `[data-custom-faq]` | No console errors |
| **19** | **Responsive pass** | 1440 · 1024 · 767 · 390 | No horizontal overflow |
| **20** | **SEO verify** | Title, description, breadcrumb | Matches copy utility |
| **21** | **Cross-link verify** | Delivery/Payment/Warranty/Dealers inbound links | Content matches pointers |
| **22** | **QA** | Automated HTML checks + operator HITL viewports | Acceptance checklist §7 |
| **23** | **Deploy manifest** | SHA256 post-deploy + `qa-custom-equipment.html` | Manifest in `m9.18-work/` |
| **24** | **Stable checkpoint** | Register `SITE-002-STABLE-LIVE-M9.18-CUSTOM-01` | Criteria §9 met |

---

## 7. Acceptance checklist

Every item is **testable** on https://zpm.new-site.space/custom-equipment after implementation.

### 7.1 Structure and copy (C01–C20)

| # | Requirement | Test |
|---|-------------|------|
| C01 | H1 «Оборудование на заказ» via page-intro | View source / visual |
| C02 | Lead paragraph present with process promise | Text match copy |
| C03 | BLOCK 01 — when-custom triggers (5+ bullets) | Count bullets |
| C04 | BLOCK 01 scope note — neutral SS only | Thermal → catalog link |
| C05 | BLOCK 02 — task matrix (7 rows) | Count rows |
| C06 | BLOCK 03 — scope groups (5 prose groups) | Present |
| C07 | BLOCK 03 in/out boundary table | 3+ rows each column |
| C08 | BLOCK 04 — OEM H3 stack (5 H3s) | Count H3s |
| C09 | BLOCK 04 proof strip — 3 labels | Производство · Сертификация · Каталог |
| C10 | **Process section exists** | BLOCK 05 landmark |
| C11 | **8 steps** in timeline | Count step badges |
| C12 | Approval gate badge «Согласование до производства» | Present |
| C13 | BLOCK 06 checklist (9 rows) | Count rows |
| C14 | BLOCK 07 materials disclaimer — no universal grade table | DOM audit |
| C15 | BLOCK 08 outcomes (5 rows) | Count rows |
| C16 | **FAQ — 8 items** | Count accordion items |
| C17 | CTA H2 «Получить расчёт изделия под ваш объект» | Exact match |
| C18 | Form title «Заявка на расчёт» | Present |
| C19 | All copy spot-check (10 strings) vs copy v1.1 | Diff against copy doc |
| C20 | Optional value chips — if used, exactly 3 | Chip count |

### 7.2 Process and hierarchy (P01–P10)

| # | Requirement | Test |
|---|-------------|------|
| P01 | **Timeline visually dominates** page (5/5) | Design review / CSS weight |
| P02 | **Outcomes table second emphasis** (3–4/5) | Visual compare vs form |
| P03 | Process-dominant — not form-first | No submit above BLOCK 10 |
| P04 | BLOCK 06 reads as prep for steps 1–2 | Proximity / caption |
| P05 | Step 5 links `/payment-methods` | Click test |
| P06 | Step 8 links `/delivery` | Click test |
| P07 | BLOCK 08 warranty pointer `/guarantee` | Link present |
| P08 | BLOCK 04 About link `/about` | Link present |
| P09 | Catalog bridge in BLOCK 03 | Link `/` present |
| P10 | **No SLA / lead-time countdown chips** | DOM search |

### 7.3 Forbidden content (F01–F10)

| # | Requirement | Test |
|---|-------------|------|
| F01 | **No price calculator / configurator UI** | DOM search sliders/estimate |
| F02 | **No file upload input** | No `<input type="file">` |
| F03 | No SKU grid / product cards with prices | BLOCK 03 audit |
| F04 | No fake case study gallery | DOM |
| F05 | No tender multi-step wizard | DOM |
| F06 | No mid-page primary submit button | Single CTA zone |
| F07 | No universal AISI grade matrix hero | BLOCK 07 |
| F08 | No TK tables / shipment points body | Delivery scope only |
| F09 | No bank/invoice/payment method bodies | Payment scope only |
| F10 | No dealer discount / territory terms body | Dealers scope only |

### 7.4 Form (M01–M08)

| # | Requirement | Test |
|---|-------------|------|
| M01 | **company field required** | HTML `required` |
| M02 | **contact field required** | HTML `required` |
| M03 | **phone field required** + mask hook | `data-mask="phone"` |
| M04 | **email field required** + validate hook | `data-validate="email"` |
| M05 | **project_description required** | HTML `required` |
| M06 | drawings field optional (text only) | No file input |
| M07 | notes field optional | No `required` |
| M08 | Consent checkbox + `/privacy-policy` link | Present |

### 7.5 FAQ (Q01–Q05)

| # | Requirement | Test |
|---|-------------|------|
| Q01 | FAQ accordion **single-open** | Click two headers |
| Q02 | `aria-expanded` toggles on buttons | DevTools |
| Q03 | `aria-controls` links button to panel id | Attribute audit |
| Q04 | Root `data-custom-faq` present | Attribute on section |
| Q05 | FAQ 1 answers scope honesty | Text match copy |

### 7.6 Responsive (R01–R04)

| # | Requirement | Test |
|---|-------------|------|
| R01 | Desktop ≥1440 — 8-step timeline readable | Screenshot |
| R02 | Tablet 1024 — tables/timeline stack | No overflow |
| R03 | Mobile 390 — FAQ + form full width | Screenshot |
| R04 | **No horizontal overflow** 390/1024/1440 | DevTools |

### 7.7 Console, overflow, ARIA (T01–T10)

| # | Requirement | Test |
|---|-------------|------|
| T01 | **No console errors** on load | Browser devtools |
| T02 | **Commercial Trust CTA architecture reused** | `zpm-commercial-trust__card` or equivalent |
| T03 | **Contacts form discipline** | `zpm-form`, mask, email validate, consent |
| T04 | **No duplicate CSS file** on live | Single `style.css` append |
| T05 | Breadcrumb Главная → Оборудование на заказ | Present |
| T06 | Meta title/description match copy utility | `<title>` + meta |
| T07 | Header/footer/nav unchanged | Visual compare |
| T08 | `/custom-equipment` HTTP 200 | curl -L |
| T09 | Twig cache cleared after deploy | Operator confirm |
| T10 | Timeline `<ol>` has accessible label | `aria-label` or visible caption |

### 7.8 Cross-surface (X01–X06)

| # | Requirement | Test |
|---|-------------|------|
| X01 | Delivery page custom links still valid | Sample inbound link |
| X02 | Payment page custom links still valid | Sample inbound link |
| X03 | Warranty page custom links still valid | Sample inbound link |
| X04 | Dealers FAQ custom link still valid | Sample inbound link |
| X05 | Phone `8 (3852) 72-18-90` referenced in CTA context | Present |
| X06 | No full PLP Commercial Trust block duplicated | DOM |

**Total checklist items: 63** (exceeds minimum 55).

---

## 8. Rollback

**Without implementation** — planned recovery path only.

### 8.1 Files affected (implementation task)

| Priority | Remote file |
|----------|-------------|
| P1 | `catalog/view/theme/default/template/information/custom_equipment.twig` |
| P2 | `catalog/controller/information/custom_equipment.php` |
| P3 | `assets/css/style.css` (append reversal) |
| P4 | `assets/js/main.js` (accordion selector delta) |
| P5 | `oc_seo_url` custom-equipment row |

### 8.2 Rollback order

1. Restore `oc_seo_url` → prior `information/information&information_id=…` target  
2. Delete or restore `custom_equipment.php` from backup (if new file — remove)  
3. Delete or restore `custom_equipment.twig` from backup  
4. Restore `style.css` from `backups/style.css.pre-m9.18-custom.bak`  
5. Restore `main.js` from `backups/main.js.pre-m9.18-custom.bak`  
6. Clear `system/storage/cache/template/*`  
7. Verify `/custom-equipment` renders legacy CMS content from `custom-equipment-live.html` baseline

### 8.3 Rollback checkpoints

| Checkpoint | Trigger | Action |
|------------|---------|--------|
| **RB-0** | Pre-deploy | `preflight-manifest.json` SHA256 |
| **RB-1** | Controller/route broken | Revert seo_url + remove custom_equipment.php only |
| **RB-2** | Visual/CSS failure | Restore twig + style.css |
| **RB-3** | JS regression | Restore main.js; static FAQ remains usable |
| **RB-4** | Catastrophic | Operator Beget full backup |

### 8.4 Minimal recovery path

**Minimum files to restore legacy `/custom-equipment`:** seo_url row + remove `custom_equipment.twig` + remove `custom_equipment.php` → generic information page returns.

---

## 9. Stable checkpoint criteria

**Checkpoint name:** `SITE-002-STABLE-LIVE-M9.18-CUSTOM-01`

Implementation becomes this checkpoint **when all are true**:

| # | Criterion |
|---|-----------|
| S1 | `/custom-equipment` serves `information/custom_equipment` custom template on live TEST |
| S2 | Acceptance checklist §7 — **all C, P, F, M, Q, R, T, X** items PASS (operator HITL for visual where marked) |
| S3 | Deploy manifest with SHA256 pre/post stored in `reports/m9.18-work/` |
| S4 | Backups exist for every overwritten remote file |
| S5 | No scope bleed — header/footer/catalog/About/Delivery/Payment/Warranty/Dealers/Contacts untouched |
| S6 | Baseline doc registered at `baselines/SITE-002-STABLE-LIVE-M9.18-CUSTOM-01.md` |
| S7 | Knowledge Map updated with §22 Custom Manufacturing page entry |
| S8 | BLOCK 05 timeline remains visually dominant (5/5); BLOCK 08 outcomes second (3–4/5) |
| S9 | No calculator, upload, or price/lead badges unless operator explicitly unlocks OQ |
| S10 | Recovery remains **CLOSED** — checkpoint is forward progress |
| S11 | **Corporate Pages Program implementation phase** for M9.14–M9.18 marked **COMPLETE** on TEST (About restoration separate) |

**Authority after checkpoint:** Supersedes prior generic `/custom-equipment` CMS surface **for custom manufacturing domain only** — sibling corp checkpoints otherwise unchanged.

**Program completion:** After S11, operator may treat Corporate Pages Program **implementation-фаза** as **завершённая** pending formal B6/B8 sign-off.

---

## 10. Risks

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R1 | **Calculator drift** — dimension sliders, live estimate | **Critical** | §2.4 forbidden; QA F01 |
| R2 | **Form-first page** — CTA above fold | **High** | §6 step 16 placement; QA P03 |
| R3 | **Tender-form drift** — upload required, field explosion | **High** | Charter form lock §1.5; QA F02 |
| R4 | seo_url mis-edit breaks `/custom-equipment` | **High** | Preflight + RB-1 |
| R5 | **Catalog conflict** — BLOCK 03 reads as PLP | **High** | Prose + links only; QA F03 |
| R6 | **Longest corp page** — scroll fatigue | **Medium** | Tier weight map §2.1; section spacing |
| R7 | **Inbound link debt** — M9.14–M9.17 promise shallow page | **High** | Full landmark stack; cross-link QA X01–X04 |
| R8 | Nav #1 visibility — page under-delivers | **High** | 8-step timeline + OEM proof mandatory |
| R9 | Production photo missing | **Medium** | Hide slot; no stock photo — OQ-DC-C25 |
| R10 | Fake portfolio placeholders | **High** | §2.4; QA F04 |
| R11 | Lead-time / price promise chips | **High** | OQ-DC-C03/C04/C19 — prose only |
| R12 | FAQ accordion JS conflicts | **Medium** | Scoped `[data-custom-faq]` init |
| R13 | `style.css` drift vs repo backups | **Medium** | Live FTP capture at preflight |
| R14 | Operator gates B6/B8 open at deploy | **Medium** | Record operator ack in implementation report |
| R15 | Copy FORM vs charter field mismatch | **Medium** | §1.5 lock documented; helper text bridges |
| R16 | SC-04 fatigue — sixth timeline | **Low** | 8 custom-specific labels; shared CSS shell |
| R17 | Warranty custom class drift | **Medium** | Link only — no term badge |
| R18 | Form `action="#"` — no backend | **Low** | Same as Contacts — documented SAFE UNKNOWN |
| R19 | Legacy CMS information HTML orphaned | **Low** | Keep admin entry; do not delete |
| R20 | Production URL parity unknown | **Low** | TEST-first |

**SECURITY RISK:** Deploy scripts may contain FTP credentials — never commit credentials; use operator-local secrets only.

---

## 11. Ready for implementation

### 11.1 Architectural uncertainty closure

| Domain | Status |
|--------|--------|
| Page structure and 8 landmarks | **CLOSED** |
| Copy block → landmark mapping | **CLOSED** |
| Component reuse vs new build | **CLOSED** |
| File touch list | **CLOSED** |
| Route strategy | **CLOSED** (`information/custom_equipment`) |
| Visual hierarchy (timeline 5/5, outcomes second) | **CLOSED** |
| Forbidden patterns | **CLOSED** |
| Form MVP fields (no upload) | **CLOSED** |
| Rollback path | **CLOSED** |
| QA criteria (63 items) | **CLOSED** |
| Cross-check vs M9.14–M9.17 | **CLOSED** |
| Program terminal milestone role | **CLOSED** |

### 11.2 Remaining operator actions (not architectural)

| Item | Blocks coding? | Blocks deploy? |
|------|----------------|----------------|
| B6/B8 formal sign-off | No | Recommended before deploy |
| OQ-DC-C21 value chips vs gate badge | **Pick one at step 6** | No |
| OQ-DC-C25 production image asset | No — hide slot if missing | No |
| OQ-DC-C03/C04 lead bands | No — default prose | **Yes** if chips requested |
| PLP Commercial Trust chip → `/custom-equipment` link | No | Separate task |

### 11.3 Final verdict

## **READY**

**Justification:** All implementation architecture decisions required to start the M9.18 coding task are documented. Route, file map, eight-landmark section mapping (Hero → when custom → what we make → **8-step process** → requirements → **outcomes** → FAQ → CTA+form), component matrix (SC-01/04/05/07/08/09/10), 24-step execution order, 63 acceptance tests, rollback, stable checkpoint, and Corporate Pages Program completion criteria are defined. Architecture aligns with M9.14–M9.17 Corporate Pages language while preserving manufacturer-capability / process-dominant posture per Design Charter and copy v1.1. Form locked to Contacts pattern without upload/CRM/calculator per task authority.

**Next task:** M9.18 Custom Manufacturing **implementation** — begin at Execution order step 1 (preflight capture).

**Program note:** Upon stable checkpoint `SITE-002-STABLE-LIVE-M9.18-CUSTOM-01`, Corporate Pages Program **implementation-фаза** for planned corp pages (M9.14–M9.18) is **complete on TEST** — formal program closure pending operator B6/B8.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-28 | **CREATED** — M9.18 Custom Manufacturing Implementation Charter v1 |

---

*Documentation only. No OpenCart files were modified during this task.*
