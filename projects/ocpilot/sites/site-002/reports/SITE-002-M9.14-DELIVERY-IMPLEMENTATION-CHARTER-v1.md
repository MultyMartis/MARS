# REPORT — SITE-002 M9.14 DELIVERY IMPLEMENTATION CHARTER

**Milestone:** M9.14 — Delivery / Доставка  
**Project:** OCPilot · SITE-002 (ЗПМ / BZPM)  
**Environment (TEST):** https://zpm.new-site.space/delivery  
**Branch:** `mars/canonical-post-recovery`  
**Authority:** `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01`  
**Version:** v1  
**Date:** 2026-06-28  
**Mode:** Documentation only — **no** OpenCart · **no** Twig/CSS/JS · **no** deploy · **no** FTP · **no** TEST writes

**Boundary:** Definitive implementation blueprint for the next coding task. This document authorizes **planning clarity only**; runtime changes require a separate implementation task after operator gates.

---

## 1. Authority

### 1.1 Primary sources (use only these)

| # | Artefact | Path | Role |
|---|----------|------|------|
| A1 | **PAGE COPY (canonical)** | [BZPM-M9.14-DELIVERY-PAGE-COPY-v1.1.md](../copy/BZPM-M9.14-DELIVERY-PAGE-COPY-v1.1.md) | All visible text — single copy authority |
| A2 | **Design Charter (approved authority per task)** | [BZPM-M9.14-DELIVERY-DESIGN-CHARTER-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.14-DELIVERY-DESIGN-CHARTER-v1.md) | Visual hierarchy, forbidden patterns, SC mapping |
| A3 | **Design Brief** | [BZPM-M9.14-DELIVERY-DESIGN-BRIEF-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.14-DELIVERY-DESIGN-BRIEF-v1.md) | Designer-facing priorities |
| A4 | **Visual Design / shared components** | [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md) § SC-01–SC-15 | Component registry and corp rhythm |
| A5 | **Implementation Preflight (COMPLETE per task authority)** | Synthesized from: forensic research · live `/delivery` capture · M9.13 preflight pattern · recovery closeout | Runtime surface facts — see §1.3 |
| A6 | **SITE-002 implementation patterns** | [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) · M9.13 / Contacts reports | Controller, Pageintro, deploy discipline |
| A7 | **Commercial Trust pattern** | [SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md](SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md) · `m9.8.9-commercial-trust-checkpoint-work/live-capture/` | CTA/form/card language reference |
| A8 | **Contacts implementation** | [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md) | Internal-page shell, `zpm-form`, spacing rhythm |
| A9 | **About restored authority** | [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md) | Live `/about` = legacy only; **not** M9.13 redesign |
| A10 | **Delivery surface analysis** | [BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md](BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md) · [m9.15-work/delivery-live-snippet.html](m9.15-work/delivery-live-snippet.html) | Current live structure and gaps |

### 1.2 Superseded — do not use

| Artefact | Reason |
|----------|--------|
| [BZPM-M9.14-DELIVERY-PAGE-COPY-v1.md](../copy/BZPM-M9.14-DELIVERY-PAGE-COPY-v1.md) | Superseded by v1.1 |
| M9.13 About redesign work copies (`m9.13-work/`) | **ARCHIVED** · operator rejected — not live authority |
| Generic CMS HTML inside live `zpm-seo` block | Replaced entirely by custom implementation |
| Research address «ул. Басовская, 14с2» | **CONFLICT** — copy v1.1 + live `CITY_DATA` use Никольское 204 |

### 1.3 Preflight synthesis (runtime facts)

| Fact | Evidence | Implementation implication |
|------|----------|----------------------------|
| URL `/delivery` resolves today | Live snippet, nav links | Preserve public URL; change route target only |
| Current route likely `information/information` + CMS `information_id` | Forensic §3.1 — **SAFE UNKNOWN** exact ID | Pre-implementation FTP capture must confirm; target route **`information/delivery`** |
| No `zpm-delivery-*` namespace on live | Forensic §3.3 | **New** scoped CSS block required |
| Body = generic `zpm-seo` prose + TK table hero bias | Live snippet L673–771 | Replace with structured sections; demote TK table |
| Pageintro = H1 only, **no lead** | Live snippet L665 | Add `$pageintro->description` with copy Lead |
| No FAQ, no form, no CTA on live | Live snippet | Full net-new bottom stack |
| No map embed on live delivery | Live snippet | **Forbidden** — maintain no map |
| Header/footer/nav unchanged | Live snippet | Out of scope except breadcrumb label |
| Form backend | Contacts pattern `action="#"` | Preserve — no new backend in M9.14 |
| Commercial Trust links to `/delivery` | Knowledge Map §14 | Secondary surface — do not duplicate trust block on page |

**SAFE UNKNOWN:** Standalone committed file titled «M9.14 Implementation Preflight report» was **not found in repo** at charter authoring time; preflight semantics above are derived from task-declared COMPLETE status plus corroborating captures listed in A5/A10.

### 1.4 Operator gates (do not conflate with charter completeness)

| Gate | Status | M9.14 impact |
|------|--------|--------------|
| B6 Design Charter approval | OPEN (header pending) | Task treats charter as authority input |
| B8 Copy sign-off | OPEN | Implementation uses copy v1.1 text |
| B1 МО warehouse address | OPEN | **Default:** copy v1.1 (Никольское 204); lock before deploy |
| B3 Dealers PLP form | OPEN | **No impact** on Delivery scope |

---

## 2. Final implementation architecture

### 2.1 Target render chain

```
GET /delivery
  └─ index.php → route information/delivery          [NEW — replaces generic information/information]
       └─ catalog/controller/information/delivery.php
            ├─ document: meta title, description, keywords, bodyClass page--inner
            ├─ Breadcrumbs → global chrome
            ├─ Pageintro → H1 «Доставка» + Lead (copy)
            └─ catalog/view/theme/default/template/information/delivery.twig
                 └─ <main class="main zpm-delivery-page">
                      ├─ [optional] trust strip OR org summary (mutually exclusive)
                      ├─ § shipment points (SC-05)
                      ├─ § organization frame (BLOCK 01)
                      ├─ § methods (BLOCK 03)
                      ├─ § timeline (BLOCK 04) — visual spine
                      ├─ § packaging (BLOCK 05)
                      ├─ § coverage (BLOCK 06)
                      ├─ § outcomes / documents (BLOCK 07)
                      ├─ § FAQ (BLOCK 08)
                      └─ § CTA + form (BLOCK 09 + FORM)
       └─ assets/css/style.css → appended zpm-delivery-* (~350–450 lines est.)
       └─ assets/js/main.js → init scoped FAQ accordion only if not global yet
```

**SEO URL migration:** Update `oc_seo_url` entry for keyword `delivery` from `information/information&information_id=…` to `information/delivery` during controller step. Confirm via preflight capture before edit.

### 2.2 Page feel (locked)

**Manufacturer logistics page** — process-dominant, not TK aggregator, not courier UX, not map geography hero. Align internal-page rhythm with Contacts (`page--inner`, breadcrumb → page-intro → `<main>`).

### 2.3 Section architecture (user-facing groups)

Full top-to-bottom order matches copy blocks. User-requested groups mapped below.

---

#### Hero (SC-01 shell + lead zone)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Immediate feasibility: «доставите в мой регион?» + two shipment origins + ship-after-pay context |
| **UX goal** | Answer Q1/Q3 in &lt;10s scan; Payment cross-link visible without leaving page |
| **Copy source** | Utility meta · Breadcrumb · H1 · Lead · optional Trust strip **OR** defer strip in favour of BLOCK 01 summary row (OQ-DC-D04 — pick **one**, not both) |
| **Reuse source** | Contacts / generic `page-intro` pattern ([Knowledge Map §15](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)); trust micro-labels → SC-03 idiom (new markup, Contacts spacing) |
| **Implementation notes** | H1 stays in `page-intro` via controller `Pageintro`; Lead in `$pageintro->description`; **no** hero media block; **no** map |
| **Dependencies** | `delivery.php` controller; `Pageintro` class; copy Lead inline link to `/payment-methods` |

---

#### Methods (BLOCK 01 + BLOCK 03)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Explain how delivery is organized and how buyer receives equipment |
| **UX goal** | Informational comparison (ТК vs 2× самовывоз vs oversized) — **not** checkout selector |
| **Copy source** | BLOCK 01 (org + summary row) · BLOCK 03 (H3 stack + microcopy) |
| **Reuse source** | SC-05 card idiom for method sub-blocks where useful; Contacts `section-title__like-h2` headings; `zpm-seo__table` responsive table pattern from live (scoped rename) |
| **Implementation notes** | BLOCK 01 body subordinate to summary row; H3 methods before TK table; no «Выбрать дelivery» buttons |
| **Dependencies** | Shipment points (BLOCK 02) should precede or immediately follow org summary — charter order: **points → org → methods** |

---

#### Timeline (BLOCK 04 — SC-04 owner on live)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Primary trust mechanism — predictable 7-step shipment path |
| **UX goal** | Full process scannable in &lt;20s desktop; steps 1–3 visible early on scroll |
| **Copy source** | BLOCK 04 table (7 steps) · step badge microcopy · timeline note · payment handoff link |
| **Reuse source** | **New shared component** `zpm-corp-timeline` / `zpm-delivery-timeline` — first live instantiation (Payment not yet built); vertical mobile / horizontal-or-vertical desktop per Contacts grid discipline |
| **Implementation notes** | Highest visual weight (5/5); numbered badges 1–7; step 1 links `/payment-methods`; **no** SLA day chips |
| **Dependencies** | CSS grid/flex; optional `aria-label` on `<ol>`; no JS required for static timeline |

---

#### Documents (BLOCK 05 + BLOCK 07)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Packaging preparedness + buyer outcome clarity (equipment + docs + responsibility) |
| **UX goal** | Reduce damage anxiety and document uncertainty; link-out to Payment/Warranty/Custom |
| **Copy source** | BLOCK 05 (4× H3) · BLOCK 07 (7-row outcome table) · trust disclaimer microcopy |
| **Reuse source** | SC-06 document checklist pattern — icon + title + one-line; Contacts list typography |
| **Implementation notes** | BLOCK 05 step 4 in timeline references this block — avoid duplicate prose; outcome rows as stacked cards ≤1024px |
| **Dependencies** | Inline SC-12 cross-links only |

---

#### Carriers (BLOCK 03 TK table — supporting tier)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Named carrier credibility — supporting reference, not page identity |
| **UX goal** | TK list readable but **subordinate** to timeline and shipment cards |
| **Copy source** | BLOCK 03 TK table (5 rows) · caption · cost note · non-exhaustive note |
| **Reuse source** | Live `zpm-seo__table` markup pattern — re-scope as `zpm-delivery-carriers__table` |
| **Implementation notes** | Text columns only — **no** logo column unless operator attests (OQ-DC-D05); position **after** H3 method sections |
| **Dependencies** | Responsive table → stacked rows on mobile |

---

#### FAQ (BLOCK 08 — SC-08)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Objection resolver after primary education |
| **UX goal** | Single-open accordion; 8 items exactly; short answers with owner links |
| **Copy source** | BLOCK 08 (8 Q&A) |
| **Reuse source** | **New** corp FAQ module — Commercial Trust FAQ grid is **not** accordion (forbidden reuse for this block) |
| **Implementation notes** | `<button aria-expanded aria-controls>` + panel ids; `data-accordion` on root; one open at a time; `prefers-reduced-motion` safe |
| **Dependencies** | New JS init in `main.js` or `modules/zpm-corp-accordion.js`; new `zpm-corp-faq*` CSS shared for future corp pages |

---

#### CTA (BLOCK 09 + FORM — SC-09 + SC-10)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Region-specific escalation — primary conversion |
| **UX goal** | One primary button zone at page bottom; phone/email support visible; form captures **region** (required) |
| **Copy source** | BLOCK 09 · FORM block · payment pointer microcopy |
| **Reuse source** | Commercial Trust `zpm-commercial-trust__card` + form wrap architecture; Contacts `zpm-form` field patterns |
| **Implementation notes** | Primary: «Задать вопрос по доставке»; `action="#"` `method="post"`; `data-mask="phone"` `data-validate="email"`; consent links `/privacy-policy`; optional `dialog=7` hidden field if site-wide CTA pattern requires — verify live Commercial Trust form at implementation preflight |
| **Dependencies** | No duplicate Contacts card grid; Fancybox callback modals unchanged |

---

#### Additional required sections (not in user short list — mandatory)

| Section | Copy | Component | Weight |
|---------|------|-----------|--------|
| **Shipment points** | BLOCK 02 | SC-05 two equal cards (Барнаул first, МО second) | Tier 1 (4/5) |
| **Russia coverage** | BLOCK 06 | SC-15 prose — 3 planning factors | Tier 2 (3/5) |

**Forbidden globally:** map embed · route animation · freight calculator · TK logo wall · «от N дней» chips · mid-page primary submit buttons · stock truck photos without operator asset · duplicate About/Payment/Dealer/Warranty bodies.

---

## 3. File map

Remote paths relative to TEST site root unless noted.

### 3.1 Controller

| File | Status | Reason | Responsibility | Approx. scope |
|------|--------|--------|----------------|---------------|
| `catalog/controller/information/delivery.php` | **NEW** | Custom corp page pattern (like `about.php`) | Meta SEO, breadcrumbs, Pageintro H1+lead, load delivery view | ~60–90 lines |
| `catalog/controller/information/information.php` | **Existing — untouched** | Generic CMS pages remain | — | — |

### 3.2 Route / SEO

| File / store | Status | Reason | Responsibility | Approx. scope |
|--------------|--------|--------|----------------|---------------|
| `oc_seo_url` row `keyword=delivery` | **MODIFIED** | Point `/delivery` → `information/delivery` | URL stability | 1 row SQL/admin |
| OpenCart admin Information entry (legacy CMS) | **Existing — orphaned after cutover** | Old HTML no longer rendered | Keep for rollback reference; do not delete without operator instruction | — |

### 3.3 Twig

| File | Status | Reason | Responsibility | Approx. scope |
|------|--------|--------|----------------|---------------|
| `catalog/view/theme/default/template/information/delivery.twig` | **NEW** | Full page body | All sections BLOCK 01–09 + FORM markup | ~350–500 lines |
| `catalog/view/theme/default/template/common/header.twig` | **Existing** | Renders breadcrumb + pageintro | No change expected | — |
| `catalog/view/theme/default/template/common/footer.twig` | **Existing** | Global chrome | No change | — |
| `catalog/view/theme/default/template/information/information.twig` | **Existing** | Generic CMS wrapper | Not used for `/delivery` after cutover | — |

**Optional partials (defer unless twig exceeds ~500 lines):**

| File | Status | Reason |
|------|--------|--------|
| `catalog/view/theme/default/template/sections/blockdeliveryform.twig` | **NEW (optional)** | Extract FORM if CTA section too large — mirror `blockanyquestionsform.twig` pattern |

### 3.4 CSS

| File | Status | Reason | Responsibility | Approx. scope |
|------|--------|--------|----------------|---------------|
| `assets/css/style.css` | **MODIFIED (append)** | Single canonical stylesheet on live | `zpm-delivery-page` namespace: layout, timeline, cards, table, FAQ, CTA | ~350–450 lines appended |
| `reports/m9.14-work/m9.14-delivery-page.css` | **NEW (repo work copy)** | Staging before append | Same rules — deploy source | mirror of append block |

**Do not create** separate CSS file on live — append to `style.css` per SITE-002 convention.

### 3.5 JS

| File | Status | Reason | Responsibility | Approx. scope |
|------|--------|--------|----------------|---------------|
| `assets/js/main.js` | **MODIFIED (minimal)** | FAQ accordion init | `initCorpAccordion()` or scoped delivery root listener | ~30–60 lines |
| `assets/js/modules/zpm-corp-accordion.js` | **NEW (preferred)** | Reusable SC-08 | Export init for FAQ + future corp pages | ~40–70 lines |

**Reuse unchanged:** phone mask, email validate, form submit hooks already in `main.js`.

### 3.6 Language

| File | Status | Reason | Responsibility | Approx. scope |
|------|--------|--------|----------------|---------------|
| `catalog/language/ru-ru/information/delivery.php` | **NEW (optional)** | Breadcrumb home text, error strings | `$_[` keys for controller | ~15 lines |
| Inline copy in twig/controller | **Alternative (allowed)** | Matches About/Contacts static copy approach | All BLOCK copy embedded | — |

**Recommendation:** Meta title/description in controller (like `about.php`); body copy in twig static — minimizes language file drift.

### 3.7 SEO / meta

| Location | Status | Content source |
|----------|--------|----------------|
| `delivery.php` → `$this->document->setTitle()` | **NEW** | Copy utility Meta title |
| `delivery.php` → `setDescription()` | **NEW** | Copy utility Meta description |
| `delivery.php` → `setKeywords()` | **NEW (optional)** | Trimmed keywords from copy / legacy live |
| OG tags | **Existing theme behaviour** | Verify theme auto-fills from document title — no change unless gap found at QA |

### 3.8 Assets

| Asset | Status | Reason |
|-------|--------|--------|
| Map / schematic image | **FORBIDDEN default** | OQ-DC-D02 — address cards only |
| Warehouse photo | **EXCLUDED default** | OQ-DC-D03 |
| TK logos | **FORBIDDEN default** | OQ-DC-D05 |
| FA Pro icons (`fad`) | **REUSE** | Timeline, cards, FAQ — same as Contacts/Commercial Trust |
| `decor-logo.svg` | **REUSE (optional)** | CTA card decor — Commercial Trust pattern |

### 3.9 Breadcrumbs

| Item | Source |
|------|--------|
| Markup | Global `Breadcrumbs` class via controller |
| Trail | Главная → Доставка |
| Template | `common/header.twig` — **no change** |

### 3.10 Forms

| Item | Spec |
|------|------|
| Location | Bottom CTA section inside `delivery.twig` |
| Classes | `zpm-form`, `zpm-form__*` — Contacts parity |
| Fields | name, phone, email, **region** (req), delivery_method (opt), order_details (opt), agree |
| Hooks | `data-mask="phone"`, `data-validate="email"`, `required` on mandatory |
| Backend | `action="#"` — unchanged posture |

### 3.11 Accordion

| Item | Spec |
|------|------|
| Markup hooks | `data-accordion`, `data-accordion-button`, `data-accordion-panel` |
| Count | 8 items |
| Behaviour | Single-open; toggle close on re-click |
| CSS namespace | `zpm-corp-faq` (shared) + `zpm-delivery-faq` (page scope) |

### 3.12 Repo work folder (implementation task)

| Path | Purpose |
|------|---------|
| `reports/m9.14-work/` | Work copies, live-capture, deploy script, QA HTML, manifest |
| `backups/*.pre-m9.14-delivery.bak` | Point rollback sources |
| `reports/m9.14-work/preflight-manifest.json` | SHA256 pre-deploy manifest (M9.13 pattern) |

---

## 4. Shared component matrix

| Component | Current source | Reuse as-is | Reuse with extension | Needs adaptation | Forbidden |
|-----------|----------------|-------------|----------------------|------------------|-----------|
| **Commercial Trust** | `blockcommercialtrust.twig` · `zpm-commercial-trust*` CSS | CTA card shell, form wrap, benefit grid idiom | Delivery CTA band adapts titles/copy | Decor logo, btn styles | Copying entire PLP trust block onto page; FAQ grid as corp FAQ |
| **Contacts** | `contact.twig` · `zpm-contact-*` CSS | `page--inner` rhythm, container padding, `zpm-form` fields, section titles | Spacing tokens match Contacts internal page | New delivery-specific sections | Full contact card grid; Yandex map embed |
| **About (live restored)** | `about.twig` legacy | Controller pattern (`information/about.php`) | Route migration pattern only | — | Any `zpm-about-*` from rejected redesign |
| **About (archived redesign)** | `m9.13-work/about.twig` | — | Proof card visual language reference only | Timeline/FAQ not present there | Using as live authority |
| **Timeline (SC-04)** | Design program spec only | — | — | **Create on M9.14** — first live corp timeline | Payment step chips with fake SLA |
| **Proof Cards (SC-05)** | M9.13 redesign `zpm-about-proof-card` (archived) | Icon+card anatomy idea | New `zpm-delivery-point-card` for shipment points | Equal two-card row | Reusing `zpm-about-proof-*` namespace on live |
| **FAQ (SC-08)** | Not implemented on SITE-002 | — | — | **Create** accordion module | Commercial Trust static FAQ grid |
| **CTA (SC-09)** | Commercial Trust + archived About CTA | Button hierarchy, phone/email inline pattern | Delivery-specific H2/body | Region-framed copy | Second primary CTA mid-page |
| **Forms (SC-10)** | Contacts `blockanyquestionsform.twig` | Core fields, consent, validation hooks | +region, +delivery_method, +order_details | Field IDs prefixed `delivery*` | New backend endpoint |
| **Buttons** | Global `btn btn_dark` | Primary/secondary/tertiary | — | — | Checkout-style method buttons |
| **Cards** | Contacts `zpm-contact-card` | Border/radius/shadow rhythm | Shipment point cards | Outcome rows | TK logo cards |
| **Spacing** | Contacts container: desktop 50px / mobile 10px | **Yes** — project default | Section vertical rhythm ~64–80px desktop | — | Random breakpoints outside project set |
| **Typography** | `section-title__like-h2`, `page-intro__title` | **Yes** | — | — | Marketing SLA chip typography |

---

## 5. Execution order

Exact implementation sequence — **do not skip stages**.

| Step | Stage | Deliverable | Stop gate |
|------|-------|-------------|-----------|
| **1** | **Preflight capture** | FTP/live capture: current `information.php` route ID, seo_url row, `style.css` SHA, generic twig | `preflight-manifest.json` written |
| **2** | **Backups** | `.bak` for any file that will be overwritten | 3+ backup files in `backups/` |
| **3** | **Controller** | `delivery.php` — meta, breadcrumbs, pageintro with Lead | PHP syntax OK |
| **4** | **Route / SEO** | Repoint `/delivery` → `information/delivery` | `/delivery` hits new controller (404 until twig) |
| **5** | **Twig skeleton** | `delivery.twig` — `<main class="zpm-delivery-page">` empty sections + landmarks | Page loads empty sections |
| **6** | **Hero / pageintro** | Lead in pageintro; optional trust strip **or** skip per OQ-DC-D04 | H1+lead visible; Payment link works |
| **7** | **Shipment points** | BLOCK 02 — two SC-05 cards | Addresses match copy v1.1 |
| **8** | **Organization** | BLOCK 01 — summary row + body | Summary scannable |
| **9** | **Methods** | BLOCK 03 — H3 stack without TK table yet | No checkout UX |
| **10** | **Timeline** | BLOCK 04 — 7 steps SC-04 | 7 steps present; dominant visual |
| **11** | **Packaging** | BLOCK 05 | Linked from step 4 conceptually |
| **12** | **Coverage** | BLOCK 06 — SC-15 prose | No map |
| **13** | **Documents / outcomes** | BLOCK 07 | 7 outcome rows |
| **14** | **Carriers** | BLOCK 03 TK table subsection | Subordinate styling |
| **15** | **FAQ** | BLOCK 08 — accordion markup + JS | 8 items; single-open |
| **16** | **CTA + form** | BLOCK 09 + FORM | Region field required |
| **17** | **CSS integration** | Append `zpm-delivery-*` to `style.css` | No duplicate rules |
| **18** | **JS integration** | Accordion init from `main.js` | No console errors |
| **19** | **Responsive pass** | 1440 · 1024 · 767 · 390 | No horizontal overflow |
| **20** | **SEO verify** | Title, description, canonical, breadcrumb | Matches copy utility |
| **21** | **QA** | Automated HTML checks + operator HITL viewports | Acceptance checklist §6 |
| **22** | **Deploy manifest** | SHA256 post-deploy + `qa-delivery.html` capture | Manifest committed to `m9.14-work/` |
| **23** | **Stable checkpoint** | Register `SITE-002-STABLE-LIVE-M9.14-DELIVERY-01` | Criteria §8 met |
| **24** | **Git checkpoint** | Repo documentation + work copies | Operator-requested only |

---

## 6. Acceptance checklist

Every item is **testable** on https://zpm.new-site.space/delivery after implementation.

### 6.1 Structure and copy

| # | Requirement | Test |
|---|-------------|------|
| C01 | H1 «Доставка» via page-intro | View source / visual |
| C02 | Lead paragraph present with Payment link | Click `/payment-methods` |
| C03 | Shipment points — 2 cards (Барнаул + МО) | Count cards; verify addresses |
| C04 | BLOCK 01 summary row visible | 4 micro-labels |
| C05 | Methods — ТК + 2× самовывоз + oversized H3 | Heading audit |
| C06 | **Timeline present** | Section exists |
| C07 | **7 steps** in timeline | Count `<li>` or step badges |
| C08 | Packaging section (BLOCK 05) | 4× H3 |
| C09 | Russia coverage (BLOCK 06) | Prose block present |
| C10 | Outcomes/documents (BLOCK 07) | 7 rows |
| C11 | **FAQ — 8 items** | Count accordion items |
| C12 | CTA H2 «Уточнить условия поставки для вашего региона» | Exact match |
| C13 | Form title «Запрос по доставке» | Present |
| C14 | **Region field required** | HTML `required` + validation message |
| C15 | All copy matches v1.1 (spot-check 10 strings) | Diff against copy doc |

### 6.2 Forbidden content

| # | Requirement | Test |
|---|-------------|------|
| F01 | **No map** embed (Yandex/Google/static route map) | DOM search `ymaps`, `iframe` map |
| F02 | **No Moscow street address conflict** — only copy v1.1 МО address (Никольское 204) | Text search «Басовская» = absent |
| F03 | No freight calculator UI | — |
| F04 | No «от N дней» SLA chips | — |
| F05 | No TK logo wall | — |
| F06 | No mid-page primary submit button | Single CTA zone |
| F07 | No duplicate Payment/About/Dealer/Warranty bodies | Link-only cross-refs |

### 6.3 Reuse and technical

| # | Requirement | Test |
|---|-------------|------|
| T01 | **Commercial Trust CTA architecture reused** | `zpm-commercial-trust__card` or documented equivalent |
| T02 | **Contacts form discipline** | `zpm-form`, mask, email validate, consent |
| T03 | **Accordion** single-open + `aria-expanded` | Keyboard + click |
| T04 | **No duplicate CSS** — single append block, no second delivery stylesheet | grep `zpm-delivery` file count on live |
| T05 | **No console errors** on load | Browser devtools |
| T06 | **No horizontal overflow** | 390 / 1024 / 1440 |
| T07 | Breadcrumb Главная → Доставка | Present |
| T08 | Meta title/description match copy utility | `<title>` + meta description |
| T09 | Header/footer/nav unchanged | Visual compare |
| T10 | `/delivery` HTTP 200 | curl -L |
| T11 | Twig cache cleared after deploy | Operator confirm |
| T12 | Commercial Trust PLP block still links `/delivery` | Sample PLP |

### 6.4 Responsive matrix

| Viewport | Checks |
|----------|--------|
| **Desktop ≥1440** | Timeline + 2-col cards; table readable |
| **Tablet 1024** | Cards stack; timeline readable; FAQ full width |
| **Mobile 390** | No overflow; accordion usable; form fields full width |

---

## 7. Rollback strategy

**Without implementation** — planned recovery path only.

### 7.1 Files affected (implementation task)

| Priority | Remote file |
|----------|-------------|
| P1 | `catalog/view/theme/default/template/information/delivery.twig` |
| P2 | `catalog/controller/information/delivery.php` |
| P3 | `assets/css/style.css` (append reversal) |
| P4 | `assets/js/main.js` or `modules/zpm-corp-accordion.js` |
| P5 | `oc_seo_url` delivery row |

### 7.2 Rollback order

1. Restore `oc_seo_url` → prior `information/information&information_id=…` target  
2. Delete or restore `delivery.php` from backup (if new file — remove)  
3. Delete or restore `delivery.twig` from backup  
4. Restore `style.css` from `backups/style.css.pre-m9.14-delivery.bak`  
5. Restore `main.js` if modified  
6. Clear `system/storage/cache/template/*`  
7. Verify `/delivery` renders legacy CMS content from `qa` capture baseline: `m9.15-work/delivery-live-snippet.html`

### 7.3 Rollback checkpoints

| Checkpoint | Trigger | Action |
|------------|---------|--------|
| **RB-0** | Pre-deploy | `preflight-manifest.json` SHA256 |
| **RB-1** | Controller/route broken | Revert seo_url + remove delivery.php only |
| **RB-2** | Visual/CSS failure | Restore twig + style.css |
| **RB-3** | JS regression | Restore main.js; keep static FAQ expanded as fallback |
| **RB-4** | Catastrophic | Operator Beget full backup |

### 7.4 Minimal recovery path

**Minimum files to restore legacy `/delivery`:** seo_url row + remove `delivery.twig` + remove `delivery.php` → generic information page returns.

---

## 8. Stable checkpoint criteria

**Checkpoint name:** `SITE-002-STABLE-LIVE-M9.14-DELIVERY-01`

Implementation becomes this checkpoint **when all are true**:

| # | Criterion |
|---|-----------|
| S1 | `/delivery` serves `information/delivery` custom template on live TEST |
| S2 | Acceptance checklist §6 — **all C**, **F**, **T** items PASS (operator HITL for visual where marked) |
| S3 | Deploy manifest with SHA256 pre/post stored in `reports/m9.14-work/` |
| S4 | Backups exist for every overwritten remote file |
| S5 | No scope bleed — header/footer/catalog/About/Contacts untouched |
| S6 | Baseline doc registered at `baselines/SITE-002-STABLE-LIVE-M9.14-DELIVERY-01.md` |
| S7 | Knowledge Map updated with § Delivery page entry |
| S8 | Operator gate B1 address uses locked canonical value OR documented copy v1.1 default with explicit operator ack |
| S9 | Recovery remains **CLOSED** — checkpoint is forward progress, not recovery reopen |

**Authority after checkpoint:** Supersedes M9.13-restored baseline **for `/delivery` page domain only** — catalog UX + About restored authority otherwise unchanged.

---

## 9. Risks

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R1 | МО address conflict (B1) propagates to Dealers later | **High** | Single canonical string in controller/twig constant; operator lock |
| R2 | seo_url mis-edit breaks `/delivery` | **High** | Preflight capture + RB-1 |
| R3 | TK table becomes visual hero (live regression) | **High** | CSS weight budget — timeline 5/5, table 2/5 |
| R4 | SC-04 first instantiation — Payment later diverges | **Medium** | Use shared `zpm-corp-timeline` namespace |
| R5 | FAQ accordion JS conflicts with mobile menu accordion | **Medium** | Scoped root init under `[data-delivery-faq]` |
| R6 | Form `action="#"` — no backend | **Low** | Same as Contacts — documented SAFE UNKNOWN |
| R7 | Legacy CMS information HTML orphaned | **Low** | Keep admin entry; do not delete |
| R8 | `style.css` drift vs repo backups | **Medium** | Live FTP capture at preflight — not old `.bak` alone |
| R9 | Operator gates B6/B8 still open at deploy time | **Medium** | Implementation task must record operator ack |
| R10 | Reintroducing map via BLOCK 02 optional image | **Medium** | Default cards-only — OQ-DC-D02 |

**SECURITY RISK:** Deploy scripts may contain FTP credentials — never commit credentials; use operator-local secrets only.

---

## 10. Ready for implementation

### 10.1 Architectural uncertainty closure

| Domain | Status |
|--------|--------|
| Page structure and block order | **CLOSED** |
| Component reuse vs new build | **CLOSED** |
| File touch list | **CLOSED** |
| Route strategy | **CLOSED** (`information/delivery`) |
| Visual hierarchy | **CLOSED** (process-dominant) |
| Forbidden patterns | **CLOSED** |
| Rollback path | **CLOSED** |
| QA criteria | **CLOSED** |

### 10.2 Remaining operator actions (not architectural)

| Item | Blocks coding? | Blocks deploy? |
|------|----------------|----------------|
| B1 МО address lock | No — use copy v1.1 default | **Yes** until locked |
| B6/B8 formal sign-off | No | Recommended before deploy |
| OQ-DC-D04 trust strip vs summary row | **Pick one at step 6** | No |

### 10.3 Final verdict

## **READY**

**Justification:** All implementation architecture decisions required to start the M9.14 coding task are documented. Route, file map, section mapping, component matrix, execution order, acceptance tests, rollback, and stable checkpoint are defined. No new UX was invented — all behaviour derives from copy v1.1, Design Charter, Design Program SC registry, and SITE-002 Contacts/Commercial Trust patterns.

**Next task:** M9.14 Delivery **implementation** — begin at Execution order step 1 (preflight capture). Do not deploy until acceptance checklist passes and operator addresses B1 for production parity.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-28 | **CREATED** — M9.14 Delivery Implementation Charter v1 |

---

*Documentation only. No OpenCart files were modified during this task.*
