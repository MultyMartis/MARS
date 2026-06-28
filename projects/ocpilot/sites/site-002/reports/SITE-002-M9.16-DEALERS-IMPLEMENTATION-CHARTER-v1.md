# REPORT — SITE-002 M9.16 DEALERS IMPLEMENTATION CHARTER

**Milestone:** M9.16 — Dealers / Дилерам  
**Project:** OCPilot · SITE-002 (ЗПМ / BZPM)  
**Environment (TEST):** https://zpm.new-site.space/dealers  
**Branch:** `mars/canonical-post-recovery`  
**Authority:** `SITE-002-STABLE-LIVE-M9.17-WARRANTY-01` (+ M9.14 Delivery · M9.15 Payment · M9.13 About Restored for non-corp scope)  
**Version:** v1  
**Date:** 2026-06-28  
**Mode:** Documentation only — **no** OpenCart · **no** Twig/CSS/JS · **no** deploy · **no** FTP · **no** TEST writes

**Boundary:** Definitive implementation blueprint for the next coding task. This document authorizes **planning clarity only**; runtime changes require a separate implementation task after operator gates.

**Central page question:** «Почему дилеру выгодно и безопасно работать именно с производителем ЗПМ?»

**Governance lock (B3):** Standalone `/dealers` corp page is **in scope** of this charter. PLP `blockdealersform` reconciliation is **out of scope** — separate future task. B3 is a **governance blocker**, not an **implementation blocker** for the corp page.

---

## 1. Authority

### 1.1 Primary sources (use only these)

| # | Artefact | Path | Role |
|---|----------|------|------|
| A1 | **PAGE COPY (canonical)** | [BZPM-M9.16-DEALERS-PAGE-COPY-v1.1.md](../copy/BZPM-M9.16-DEALERS-PAGE-COPY-v1.1.md) | All visible text — single copy authority |
| A2 | **Design Charter** | [BZPM-M9.16-DEALERS-DESIGN-CHARTER-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.16-DEALERS-DESIGN-CHARTER-v1.md) | Visual hierarchy, forbidden patterns, SC mapping, manufacturer-partnership mode |
| A3 | **Design Brief** | [BZPM-M9.16-DEALERS-DESIGN-BRIEF-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.16-DEALERS-DESIGN-BRIEF-v1.md) | Designer-facing priorities |
| A4 | **Visual Design / shared components** | [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md) § SC-01–SC-15 | Component registry and corp rhythm |
| A5 | **Corporate Pages Program** | [BZPM-CORPORATE-PAGES-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-v1.md) · [IA Map § M9.16](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-IA-MAP-v1.md#m916--dealers-dealers) | CP-01 ownership · CP-08 dealer program owner |
| A6 | **Copy Standards** | [BZPM-COPY-STANDARDS-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-COPY-STANDARDS-v1.md) | Tone · SAFE UNKNOWN discipline |
| A7 | **Forensic Research** | [BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) · [m9.15-work/dealers-live-snippet.html](m9.15-work/dealers-live-snippet.html) | Live surface facts and gaps |
| A8 | **SITE-002 implementation patterns** | [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) §15–§21 | Pageintro, corp page discipline |
| A9 | **Delivery implementation (precedent)** | [SITE-002-M9.14-DELIVERY-IMPLEMENTATION-CHARTER-v1.md](SITE-002-M9.14-DELIVERY-IMPLEMENTATION-CHARTER-v1.md) · [SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md](SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md) | Route migration · timeline · FAQ · CTA pattern |
| A10 | **Payment implementation (precedent)** | [SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md](SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md) · [BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md) | SC-04 reuse · company field on corp form |
| A11 | **Warranty implementation (precedent)** | [SITE-002-M9.17-WARRANTY-IMPLEMENTATION-CHARTER-v1.md](SITE-002-M9.17-WARRANTY-IMPLEMENTATION-CHARTER-v1.md) · [SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md](SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md) | Latest corp page cutover pattern |
| A12 | **Commercial Trust pattern** | [SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md](SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md) · `m9.8.9-03-work/live-capture/blockdealersform.twig` | CTA/form language · PLP dealer surface reference (**not** modified in M9.16 scope) |
| A13 | **Contacts implementation** | [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md) | Internal-page shell · `zpm-form` · spacing rhythm |
| A14 | **site-passport** | [site-passport.md](../site-passport.md) | Operator order · blockers |
| A15 | **OCPILOT-STATE** | [OCPILOT-STATE.md](../../OCPILOT-STATE.md) | Program status |

### 1.2 Confirmed authority chain

| Layer | Status | Notes |
|-------|--------|-------|
| **PAGE-COPY v1.1** | **Authority input** | Operator approval header pending (B8) — implementation uses copy text as-is |
| **Design Charter v1** | **Authority input** | Operator approval pending (B6) — visual weight budget locked in charter |
| **Design Brief v1** | **Authority input** | Manufacturer-partnership mode · proof → benefits → process → form |
| **Forensic research** | **COMPLETE** | Live `/dealers` = generic `zpm-seo`; no form; PLP owns form today |
| **Patterns (M9.14–M9.17)** | **READY** | SC-04 timeline · SC-08 FAQ · SC-09/SC-10 CTA+form live on TEST |
| **Shared components** | **READY** | Contacts shell · Commercial Trust CTA card · `zpm-corp-timeline` · `zpm-corp-faq` |

### 1.3 Operator gates (do not conflate with charter completeness)

| Gate | Status | M9.16 impact |
|------|--------|--------------|
| B6 Design Charter approval | OPEN | Task treats Design Charter as authority input |
| B8 Copy sign-off | OPEN | Implementation uses copy v1.1 text |
| B1 МО warehouse address | OPEN | BLOCK 05 uses **region-only prose** per copy v1.1 — no street until lock |
| **B3 PLP dealer form vs `/dealers`** | **OPEN — governance only** | **Does not block** standalone corp page implementation; **does not authorize** PLP slimming in this task |

### 1.4 Preflight synthesis (runtime facts)

| Fact | Evidence | Implementation implication |
|------|----------|----------------------------|
| URL `/dealers` resolves today | `dealers-live-snippet.html` L662–714 | Preserve public URL; change route target only |
| Current route likely `information/information` + CMS `information_id` | Forensic §2.1 — **SAFE UNKNOWN** exact ID | Pre-implementation FTP capture must confirm; target route **`information/dealers`** |
| No `zpm-dealers-*` namespace on live | Contrast M9.14–M9.17 | **New** scoped CSS block required |
| Body = generic `zpm-seo` prose; mentions **СНГ** (legacy) | Live snippet L674–714 | Replace entirely; **do not** reintroduce СНГ — copy v1.1 is Russia-only |
| Pageintro = H1 «Дилерам» only, **no lead** | Live snippet L665 | Add `$pageintro->description` with copy Lead |
| **No form on corp page** — process step references missing form | Forensic G-DE01 | Full net-new FORM at page endpoint |
| PLP `blockdealersform` has working form (`dialog=7`) | `blockdealersform.twig` | Reference for handler — **unchanged** in M9.16 scope |
| No FAQ, no CTA band on live corp page | Live snippet | Full net-new bottom stack |
| Form backend | Contacts/Delivery/Payment pattern `action="#"` | Preserve — no new backend in M9.16 |
| Commercial Trust FAQ card links to `/dealers` | Knowledge Map §14 | Inbound cross-link — corp page must deliver depth |

### 1.5 SAFE UNKNOWN (charter-level)

| Topic | Status | Charter handling |
|-------|--------|------------------|
| OpenCart `information_id` for `dealers` | **SAFE UNKNOWN** | Capture at preflight; do not delete legacy CMS entry |
| Production `/dealers` parity | **SAFE UNKNOWN** | TEST-first; document at deploy |
| Channel policy depth (OQ-D01) | **SAFE UNKNOWN** | BLOCK 02 channel note prose only |
| Discount / MOQ / territory / marketing support (OQ-D03–D05, D09) | **SAFE UNKNOWN** | No badges; FAQ + helper prose |
| Partner logos / map / count (OQ-D13, D14) | **SAFE UNKNOWN** | **Exclude** — no assets in repo |
| PLP form reconciliation (OQ-D15 / **B3**) | **Governance OPEN** | Corp form canonical **on this page**; PLP change = **future task** |
| Dedicated dealer email (OQ-D16) | **Assumed** `info@bzpm.ru` | Per copy v1.1 |
| Privacy policy route | **Assumed** `/privacy-policy` | Verify at preflight |
| `dialog=7` on corp form vs generic handler | **SAFE UNKNOWN** | Verify live submit handler at preflight; default hidden `dialog=7` if PLP parity confirmed |
| Trust strip after lead (OQ-DC-DE04) | **OPEN** | Pick **one**: optional trust strip **or** OEM row — avoid badge fatigue |
| OEM trust row placement (OQ-DC-DE05) | **OPEN** | Default: after BLOCK 02 per Design Charter §20.6 |
| ИНН field in form (OQ-DC-DE06) | **CLOSED exclude** | Not in copy v1.1 |
| Visual design mockups | **NOT IN REPO** | Implementation follows Design Charter weight budget + copy structure |
| Partner matrix icons | **PARTIAL** | Use FA Pro `fad` tags per program — no custom icon pack attested |

### 1.6 Superseded — do not use

| Artefact | Reason |
|----------|--------|
| [BZPM-M9.16-DEALERS-PAGE-COPY-v1.md](../copy/BZPM-M9.16-DEALERS-PAGE-COPY-v1.md) | Superseded by v1.1 |
| Live generic `zpm-seo` dealers HTML (incl. СНГ geography) | Replaced entirely by custom implementation |
| Live pageintro H1-only «Дилерам» without lead | Superseded by copy v1.1 utility + lead |
| Kroner-style dealer directory / ИНN-in-form patterns | Not in approved copy |
| Franchise / MLM / recruitment landing patterns | Design Charter forbidden |

---

## 2. Final architecture

### 2.1 Page feel (locked)

**Manufacturer partnership page** — proof-dominant, not dealer recruitment landing, not franchise program, not lead-gen squeeze page. Commercial order: **Proof → Benefits → Process → Form**. Education blocks (01–05) carry **higher visual weight** than CTA+form zone (Design Charter §10.3).

**Corporate Pages language alignment:** Same operational corp mode as M9.14 Delivery, M9.15 Payment, M9.17 Warranty — SC-01 shell, SC-04 timeline, SC-08 accordion, SC-09/SC-10 CTA+form — **dealer-specific copy and partner semantics**, not mechanical page clone.

### 2.2 Target render chain

```
GET /dealers
  └─ index.php → route information/dealers          [NEW — replaces generic information/information]
       └─ catalog/controller/information/dealers.php
            ├─ document: meta title, description, keywords, bodyClass page--inner
            ├─ Breadcrumbs → global chrome
            ├─ Pageintro → H1 «Дилерам и оптовым партнёрам» + Lead (copy)
            └─ catalog/view/theme/default/template/information/dealers.twig
                 └─ <main class="main zpm-dealers-page">
                      ├─ [optional] trust strip (mutually exclusive with heavy OEM duplicate)
                      ├─ § BLOCK 01 — partner matrix (SC-13)
                      ├─ § BLOCK 02 — OEM proof / dealer advantages (page identity)
                      ├─ § BLOCK 03 — partner outcomes (SC-07)
                      ├─ § BLOCK 04 — cooperation process (SC-04)
                      ├─ § BLOCK 05 — supply chain + cross-links (SC-05 variant)
                      ├─ § BLOCK 06 — FAQ (SC-08)
                      └─ § BLOCK 07 + FORM — CTA + qualification form (SC-09 + SC-10)
       └─ assets/css/style.css → appended zpm-dealers-* (~420–520 lines est.)
       └─ assets/js/main.js → extend corp FAQ accordion with [data-dealers-faq]
```

**SEO URL migration:** Update `oc_seo_url` entry for keyword `dealers` from `information/information&information_id=…` to `information/dealers` during controller step. Confirm via preflight capture before edit.

### 2.3 Section architecture (implementation order)

Full top-to-bottom order matches copy blocks. User-facing groups mapped below.

---

#### Hero (SC-01 shell + lead zone)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Manufacturer partnership frame — «с кем я связываю репутацию?» in <15s scan |
| **UX goal** | Direct factory + Russia supply context; no recruitment headline |
| **Copy source** | Utility meta · Breadcrumb · H1 · Lead · optional Trust strip (MICRO) |
| **Shared component** | SC-01 — Contacts/Delivery/Payment `page-intro` pattern |
| **Visual weight** | Tier 1 (**3/5**) — frame, not hero media |
| **Reuse source** | [Knowledge Map §15](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md); Delivery `pageintro` controller pattern |
| **Implementation notes** | H1 in `page-intro` via controller `Pageintro`; Lead in `$pageintro->description`; **no** form in hero; **no** map; **no** СНГ |
| **Dependencies** | `dealers.php` controller; `Pageintro` class |

---

#### Who can become a dealer (BLOCK 01 — SC-13)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Partner self-qualification — «это про меня?» |
| **UX goal** | 5 partner types scannable; helper redirects direct buyers to Payment |
| **Copy source** | BLOCK 01 H2 · Intro · Partner matrix (5 rows) · Body · Helper |
| **Shared component** | **SC-13 Partner / segment matrix** — first live corp instantiation |
| **Visual weight** | Tier 1 (**4/5**) — important; **subordinate to BLOCK 02 (5/5)** |
| **Reuse source** | SC-07 table responsive stack idiom from Delivery outcomes; partner type tag labels from copy MICRO |
| **Implementation notes** | Table → stacked cards ≤1024px; icon + title + 2-line description; **no** per-type discount columns |
| **Dependencies** | New `zpm-dealers-matrix__*` CSS; FA Pro icons optional |

---

#### Dealer advantages (BLOCK 02 — OEM proof)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Primary page identity — why direct manufacturer partnership is safe |
| **UX goal** | Five H3 proof stack scannable in <20s desktop; channel note visible |
| **Copy source** | BLOCK 02 H2 · Intro · 5× H3 · About pointer · Channel note (microcopy) |
| **Shared component** | SC-03 OEM trust row (MICRO) — recommended after BLOCK 02 |
| **Visual weight** | Tier 1 (**5/5**) — **strongest block on page** |
| **Reuse source** | Delivery/Payment proof stack typography; Contacts section titles |
| **Implementation notes** | **No** discount badges; channel note = prose only; About link inline |
| **Dependencies** | OEM trust row: manufacturer · ИНН 2221237587 · Барнаул · About link |

---

#### Support — partner outcomes (BLOCK 03)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Tangible partner value without fake commercial tiers |
| **UX goal** | 6-row outcome table; helper on no public price list |
| **Copy source** | BLOCK 03 H2 · Intro · Outcome table · Body · Helper |
| **Shared component** | SC-07 matrix / outcome table |
| **Visual weight** | Tier 1 (**4/5**) |
| **Reuse source** | Delivery BLOCK 07 outcomes · Payment audience outcome rows |
| **Implementation notes** | Payment link in body — one line; **no** % margin visuals |
| **Dependencies** | Responsive table → stacked rows ≤1024px |

---

#### How cooperation works (BLOCK 04 — SC-04)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Predictable 5-step onboarding path |
| **UX goal** | Full process scannable in <20s; steps 1–3 visible early on scroll |
| **Copy source** | BLOCK 04 H2 · Intro · 5 process steps · Outcome note · Helper · Step badges |
| **Shared component** | **SC-04** `zpm-corp-timeline` — sixth corp instantiation (5 steps) |
| **Visual weight** | Tier 1 (**4/5**) |
| **Reuse source** | `zpm-corp-timeline` CSS from M9.14/M9.15/M9.17 |
| **Implementation notes** | Step 5 links Payment + Delivery; **no** SLA day chips; step 1 references form on **this page** |
| **Dependencies** | CSS grid/flex; `aria-label` on `<ol>` |

---

#### Support — supply chain & composed proof (BLOCK 05)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Channel model visualization + CP-01 cross-link summaries |
| **UX goal** | Simple 4-node vertical chain — **not** logistics map |
| **Copy source** | BLOCK 05 H2 · Intro · Chain diagram · Caption · Alt text · Body · Summary cross-links (3 rows) · Warranty pointer · Dealer logistics note |
| **Shared component** | SC-05 proof/chain variant · SC-12 cross-link inline |
| **Visual weight** | Tier 2 (**3/5**) |
| **Reuse source** | Delivery one-line shipment summary pattern; inline link table from copy |
| **Implementation notes** | MO warehouse = **«склад партнёра в Московской области»** only (B1); **no** street; **no** territory map |
| **Dependencies** | Links: `/delivery`, `/custom-equipment`, `/payment-methods`, `/guarantee` |

---

#### FAQ (BLOCK 06 — SC-08)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Objection resolver — MOQ, territory, docs, custom, start path |
| **UX goal** | Single-open accordion; **8 items exactly**; short answers with owner links |
| **Copy source** | BLOCK 06 (8 Q&A) |
| **Shared component** | **SC-08** `zpm-corp-faq` — extend accordion init |
| **Visual weight** | Tier 2 (**3/5**) — subordinate to BLOCK 02 and BLOCK 04 |
| **Reuse source** | Delivery/Payment/Warranty FAQ markup and CSS |
| **Implementation notes** | FAQ 1 points to BLOCK 01 — no duplicate matrix; `<button aria-expanded aria-controls>` |
| **Dependencies** | Extend `main.js`: add `[data-dealers-faq]` to corp accordion selector list |

---

#### CTA + Form (BLOCK 07 + FORM — SC-09 + SC-10 dealer variant)

| Attribute | Spec |
|-----------|------|
| **Purpose** | Qualification endpoint — informed escalation, not instant enrollment |
| **UX goal** | One primary button zone at page bottom; phone/email parallel support; form **below** education blocks visually |
| **Copy source** | BLOCK 07 · FORM block · Catalog + Payment microcopy pointers |
| **Shared component** | Commercial Trust `zpm-commercial-trust__card` + SC-10 `zpm-form` + **dealer qualification variant** |
| **Visual weight** | Tier 1 (**3/5** deliberate) — Critical presence, **lower than BLOCK 02** |
| **Reuse source** | Delivery/Payment CTA band; Payment company field; Contacts form hooks |
| **Implementation notes** | Primary: «Обсудить сотрудничество» → `#zpm-dealers-form`; `action="#"`; **no** website field; **no** mid-page submit buttons |
| **Dependencies** | Consent `/privacy-policy`; `data-mask="phone"` `data-validate="email"` |

### 2.4 Forbidden globally

Form-as-hero · form above fold · sticky form sidebar · mid-page primary CTA buttons · discount / MOQ / territory badges · partner logo wall · dealer territory map · franchise tier pyramids · MLM aesthetics · recruitment urgency banners · «станьте дилером сегодня» · duplicate About/Delivery/Payment/Warranty bodies · TK tables · bank requisites · cert PDF gallery · warranty term badge · SKU grid · СНГ geography · **PLP form changes in M9.16 scope**.

---

## 3. OpenCart architecture

### 3.1 Route

| Item | Value |
|------|-------|
| Public URL | `/dealers` (unchanged) |
| OpenCart route | `information/dealers` |
| Prior route (inferred) | `information/information&information_id=…` — confirm at preflight |
| SEO keyword | `dealers` |

### 3.2 Controller

| File | Status | Responsibility |
|------|--------|----------------|
| `catalog/controller/information/dealers.php` | **NEW** | Meta SEO, breadcrumbs, Pageintro H1+lead, load dealers view (~60–95 lines) |
| `catalog/controller/information/information.php` | **UNTOUCHED** | Generic CMS pages remain |

### 3.3 Twig

| File | Status | Responsibility |
|------|--------|----------------|
| `catalog/view/theme/default/template/information/dealers.twig` | **NEW** | All BLOCK 01–07 + FORM (~450–600 lines) |
| `catalog/view/theme/default/template/common/header.twig` | **UNTOUCHED** | Breadcrumb + pageintro |
| `catalog/view/theme/default/template/common/footer.twig` | **UNTOUCHED** | Global chrome |
| `catalog/view/theme/default/template/information/information.twig` | **UNTOUCHED** | Not used for `/dealers` after cutover |
| `catalog/view/theme/default/template/sections/blockdealersform.twig` | **UNTOUCHED** | PLP surface — **B3 future task** |

**Optional partial (defer if twig > ~600 lines):**

| File | Status | Reason |
|------|--------|--------|
| `catalog/view/theme/default/template/sections/blockdealerspageform.twig` | **NEW (optional)** | Extract FORM — mirror `blockanyquestionsform.twig` |

### 3.4 SEO

| Location | Content source |
|----------|----------------|
| `dealers.php` → `setTitle()` | Copy utility Meta title |
| `dealers.php` → `setDescription()` | Copy utility Meta description |
| `dealers.php` → `setKeywords()` | Optional — trim legacy live keywords; fix typo «илеры» if present |
| `oc_seo_url` row `keyword=dealers` | **MODIFIED** → `information/dealers` |
| OG tags | Existing theme behaviour — verify at QA |
| Breadcrumb | Главная → Дилерам |

### 3.5 CSS

| File | Status | Responsibility |
|------|--------|----------------|
| `assets/css/style.css` | **MODIFIED (append)** | `zpm-dealers-page` namespace (~420–520 lines) |
| `reports/m9.16-work/m9.16-dealers-page.css` | **NEW (repo work copy)** | Staging before append |

**Shared classes reused (not duplicated):** `zpm-corp-timeline`, `zpm-corp-faq__*`, `zpm-form__*`, `zpm-commercial-trust__*`, `section-title__like-h2`.

**Page-scoped classes (new):** `zpm-dealers-page`, `zpm-dealers-section`, `zpm-dealers-matrix`, `zpm-dealers-proof`, `zpm-dealers-outcomes`, `zpm-dealers-process`, `zpm-dealers-chain`, `zpm-dealers-crosslinks`, `zpm-dealers-faq`, `zpm-dealers-cta`, `zpm-dealers-trust-strip`, `zpm-dealers-oem-row`.

### 3.6 JS

| File | Status | Responsibility |
|------|--------|----------------|
| `assets/js/main.js` | **MODIFIED (minimal)** | Add `[data-dealers-faq]` to corp accordion init (~5–15 lines delta) |
| `reports/m9.16-work/m9.16-corp-accordion.js` | **NEW (repo staging)** | Updated selector list if extracted |

**Reuse unchanged:** phone mask, email validate, form submit hooks.

### 3.7 Form

| Item | Spec |
|------|------|
| Location | Bottom CTA section inside `dealers.twig` — id `zpm-dealers-form` |
| Classes | `zpm-form`, `zpm-form__*` — Contacts/Payment parity |
| Fields | **name** (req), **company** (req), **city** (req), **phone** (req), **email** (req), **comment** (opt), **agree** (req) |
| Excluded | **website** — removed v1.1; **ИНН** — not in copy |
| Hooks | `data-mask="phone"`, `data-validate="email"`, `required` on mandatory |
| Backend | `action="#"` — unchanged posture |
| Hidden | `dialog=7` — **if** preflight confirms PLP dealer handler parity (**SAFE UNKNOWN**) |
| Field IDs | Prefix `dealer*` or `dealers*` — consistent within page |
| Submit label | «Отправить заявку» |
| Success microcopy | Manager callback in office hours — **not** «вы приняты в программу» |

### 3.8 FAQ accordion

| Item | Spec |
|------|------|
| Root hook | `data-dealers-faq` + `data-accordion` |
| Item hooks | `data-accordion-button`, `data-accordion-panel` |
| Count | **8 items** |
| Behaviour | Single-open; toggle close on re-click |
| CSS namespace | `zpm-corp-faq` (shared) + `zpm-dealers-faq` (page scope) |

### 3.9 Cross-links (required)

| Target | On-page usage |
|--------|---------------|
| `/about` | BLOCK 02 pointer · OEM trust row · CTA secondary |
| `/payment-methods` | BLOCK 01 helper · BLOCK 03 body · BLOCK 04 step 5 · BLOCK 05 table · FAQ 6 · CTA microcopy |
| `/delivery` | Lead · BLOCK 04 step 5 · BLOCK 05 table · FAQ 3, 7 |
| `/guarantee` | BLOCK 05 one-line pointer |
| `/custom-equipment` | BLOCK 02 H3 · BLOCK 05 table · FAQ 4, 5 |
| `/contact/` | BLOCK 02 H3 · FAQ 6 · CTA tertiary |
| `/our-certification` | Optional «Сделано в России» badge link only |
| `/` | CTA catalog pointer |
| `/privacy-policy` | Form consent |

**Outbound from sibling pages (verify only — no edits in M9.16):** Payment bullet on dealers · Delivery/Warranty dealer pointers · Commercial Trust «Партнёрство» lane.

### 3.10 Language file (optional)

| File | Status |
|------|--------|
| `catalog/language/ru-ru/information/dealers.php` | **NEW (optional)** — breadcrumb strings |
| Inline copy in twig/controller | **Alternative (allowed)** — matches Delivery/Payment |

**Recommendation:** Meta in controller; body copy static in twig.

---

## 4. Shared components

### 4.1 Reuse matrix

| Component | Source | Reuse as-is | Adapt for Dealers | Create new | Forbidden |
|-----------|--------|-------------|-------------------|------------|-----------|
| **SC-01 Page shell** | M9.14–M9.17 | `page--inner`, pageintro rhythm | H1+lead copy | — | Hero form · recruitment hero |
| **SC-03 Trust row** | Delivery summary row | 4-label micro-row pattern | OEM trust row labels | Optional trust strip | Both strip + heavy OEM row |
| **SC-04 Timeline** | Delivery (7) · Payment (6) · Warranty (5) | `zpm-corp-timeline` CSS/structure | **5 dealer onboarding steps** | — | SLA chips |
| **SC-05 Chain variant** | Design program | Card/chain anatomy | 4-node vertical supply chain | **First live chain diagram** | Logistics map |
| **SC-07 Outcome table** | Delivery · Payment · Warranty | Responsive table/cards | BLOCK 03 six rows | — | Discount columns |
| **SC-08 FAQ accordion** | M9.14–M9.17 | `zpm-corp-faq__*` + JS | 8 dealer Q&A | — | Commercial Trust static FAQ grid |
| **SC-09 CTA band** | M9.14–M9.17 | Button hierarchy, phone/email | Dealer-specific H2/body | — | Mid-page primary CTA |
| **SC-10 Form** | Contacts · Payment | Core fields + consent | **+company +city** (both req) | Dealer qualification variant | website field · ИНН field |
| **SC-12 Cross-link inline** | M9.14–M9.17 | Text link pattern | BLOCK 02–05 summaries | — | Embedded sibling bodies |
| **SC-13 Partner matrix** | Design program | — | 5-type matrix | **First live corp instantiation** | Territory/discount columns |
| **Commercial Trust** | M9.8.9 PLP | CTA card shell, decor logo | Dealers titles/copy | — | Full PLP block on page · PLP form edit |
| **Contacts** | `/contact/` | `zpm-form` discipline | Dealer fields | — | Contact card grid · map |
| **Delivery** | M9.14 live | — | One-line + link table row | — | TK tables · shipment point cards |
| **Payment** | M9.15 live | Company field pattern | One-line partner payment pointer | — | Methods matrix · bank details |
| **Warranty** | M9.17 live | — | One-line pointer | — | Term badge · RMA process |

### 4.2 Create for the first time on SITE-002 (M9.16 scope)

| Item | Notes |
|------|-------|
| `dealers.php` controller | New corp page controller |
| `dealers.twig` | Full dealers body |
| `zpm-dealers-*` CSS block | Page namespace — appended to style.css |
| **SC-13 partner matrix** | First live responsive partner-type grid |
| **SC-05 supply chain diagram** | First live 4-node vertical chain (text + minimal icon) |
| SC-10 **dealer qualification variant** | First live **city required** on corp form (Payment has company only) |
| Optional `blockdealerspageform.twig` | Only if twig size warrants extract |

### 4.3 Cross-check vs Delivery, Payment, Warranty

| Dimension | Delivery | Payment | Warranty | **Dealers (M9.16)** |
|-----------|----------|---------|----------|---------------------|
| Page mode | Manufacturer logistics | Deal/payment process | Service reassurance | **Manufacturer partnership** |
| Dominant block | 7-step timeline + shipment points | 6-step timeline + methods | 5-step claim timeline | **BLOCK 02 OEM proof (5/5)** |
| Secondary spine | TK table (subordinate) | Proof cards + legal strip | Document checklist | **BLOCK 04 process (4/5)** |
| Form unique fields | region (req) | company (req) | equipment_model (req) | **company + city (req)** |
| Form visual weight vs education | CTA at bottom | CTA at bottom | CTA at bottom | **Form deliberately 3/5 — education 4–5/5** |
| FAQ count | 8 | 8 | 8 | **8** |
| CTA pattern | Commercial Trust card + form | Same | Same | Same |
| Cross-link discipline | Link-only to siblings | Link-only | Link-only | **Composition summaries only (CP-01)** |
| Forbidden bleed | map · calculator | bank widgets | term badge · ASC map | **discount map · franchise · form hero · PLP edit** |

**Unified Corporate Pages language:** Same section spacing (~64–80px desktop), container padding (50px desktop / 10px mobile), `section-title__like-h2`, corp timeline visual language, corp FAQ accordion, Commercial Trust CTA terminus — **distinct dealer/partner copy**, not template duplication.

**Dealer semantic preservation:** Page owns channel-partnership framing; does **not** copy Delivery logistics depth, Payment settlement detail, or Warranty RMA process — only honest one-line summaries + links.

---

## 5. File map

Remote paths relative to TEST site root unless noted.

### 5.1 NEW (remote + repo work copies)

| Path | Location | Reason |
|------|----------|--------|
| `catalog/controller/information/dealers.php` | Remote | Custom corp controller |
| `catalog/view/theme/default/template/information/dealers.twig` | Remote | Full page body |
| `reports/m9.16-work/dealers.php` | Repo | Work copy controller |
| `reports/m9.16-work/dealers.twig` | Repo | Work copy twig |
| `reports/m9.16-work/m9.16-dealers-page.css` | Repo | CSS staging |
| `reports/m9.16-work/m9.16-corp-accordion.js` | Repo | JS staging (optional) |
| `reports/m9.16-work/m916-dealers-deploy.py` | Repo | Deploy script |
| `reports/m9.16-work/m916-dealers-screenshots.py` | Repo | QA screenshot script |
| `reports/m9.16-work/preflight-manifest.json` | Repo | Pre-deploy SHA256 |
| `reports/m9.16-work/deploy-manifest.json` | Repo | Post-deploy SHA256 |
| `reports/m9.16-work/qa-dealers.html` | Repo | Live HTML capture |
| `baselines/SITE-002-STABLE-LIVE-M9.16-DEALERS-01.md` | Repo | Stable checkpoint (post-implementation) |
| `qa/m9.16-dealers-screenshots/*` | Repo | Viewport screenshots |
| `backups/dealers.php.pre-m9.16-dealers.bak` | Repo | Rollback |
| `backups/dealers.twig.pre-m9.16-dealers.bak` | Repo | Rollback |
| `backups/style.css.pre-m9.16-dealers.bak` | Repo | Rollback |
| `backups/main.js.pre-m9.16-dealers.bak` | Repo | Rollback |

### 5.2 MODIFIED

| Path | Location | Reason | Approx. scope |
|------|----------|--------|---------------|
| `assets/css/style.css` | Remote | Append `zpm-dealers-*` | ~420–520 lines |
| `assets/js/main.js` | Remote | Add `[data-dealers-faq]` to accordion init | ~5–15 lines |
| `oc_seo_url` row `keyword=dealers` | DB/admin | Route cutover | 1 row |

### 5.3 UNTOUCHED

| Path | Reason |
|------|--------|
| `catalog/controller/information/delivery.php` | Out of scope |
| `catalog/controller/information/payment.php` | Out of scope |
| `catalog/controller/information/guarantee.php` | Out of scope |
| `catalog/controller/information/about.php` | Out of scope |
| `catalog/view/theme/default/template/information/*.twig` (except new `dealers.twig`) | Out of scope |
| `catalog/view/theme/default/template/sections/blockdealersform.twig` | **B3 — future task** |
| `catalog/view/theme/default/template/sections/blockcommercialtrust.twig` | Out of scope |
| Header/footer/nav templates | Out of scope |
| Catalog/PLP/PDP templates | Out of scope |
| OpenCart admin Information entry (legacy CMS) | Orphaned after cutover — keep for rollback |

### 5.4 QA / backups discipline

| Item | Rule |
|------|------|
| Preflight | Live FTP capture **before** any remote write |
| Backups | One `.bak` per file overwritten |
| Manifest | SHA256 pre/post in `m9.16-work/` |
| Twig cache | Clear after deploy |
| Credentials | Deploy scripts — operator-local only; **never commit secrets** |

---

## 6. Execution order

Exact implementation sequence — **do not skip stages**.

| Step | Stage | Deliverable | Stop gate |
|------|-------|-------------|-----------|
| **1** | **Preflight capture** | FTP/live capture: current `information_id`, seo_url row, `style.css` SHA, `dealers-live-snippet.html` baseline | `preflight-manifest.json` written |
| **2** | **Backups** | `.bak` for any file that will be overwritten | 4 backup files in `backups/` |
| **3** | **Controller** | `dealers.php` — meta, breadcrumbs, pageintro with Lead | PHP syntax OK |
| **4** | **Route / SEO** | Repoint `/dealers` → `information/dealers` | `/dealers` hits new controller |
| **5** | **Twig skeleton** | `dealers.twig` — `<main class="zpm-dealers-page">` empty sections + landmarks | Page loads empty sections |
| **6** | **Hero / pageintro** | Lead in pageintro; optional trust strip per OQ-DC-DE04 | H1+lead visible; no СНГ |
| **7** | **Partner matrix** | BLOCK 01 — SC-13 (5 types) | Matrix stacks ≤1024px |
| **8** | **Dealer advantages** | BLOCK 02 — 5× H3 + channel note + About link | Dominant visual weight |
| **9** | **OEM trust row** | MICRO OEM row after BLOCK 02 (default OQ-DC-DE05) | ИНН + About link |
| **10** | **Partner outcomes** | BLOCK 03 — 6-row outcome table | No discount columns |
| **11** | **Cooperation process** | BLOCK 04 — 5-step SC-04 timeline | Step 1 references on-page form |
| **12** | **Supply chain + links** | BLOCK 05 — chain + 3-row cross-link table + warranty line | Region-only MO prose |
| **13** | **FAQ** | BLOCK 06 — accordion markup + JS hook | 8 items; single-open |
| **14** | **CTA + form** | BLOCK 07 + FORM — company + city required | Form at page endpoint only |
| **15** | **CSS integration** | Append `zpm-dealers-*` to `style.css` | Education blocks visually > form zone |
| **16** | **JS integration** | Extend accordion init for `[data-dealers-faq]` | No console errors |
| **17** | **Responsive pass** | 1440 · 1024 · 767 · 390 | No horizontal overflow |
| **18** | **SEO verify** | Title, description, breadcrumb, keywords cleanup | Matches copy utility |
| **19** | **Cross-link verify** | Inbound Commercial Trust + sibling page pointers | Links resolve HTTP 200 |
| **20** | **Dealer logic verify** | No recruitment patterns; no numeric commercial claims | Forbidden audit pass |
| **21** | **QA** | Automated HTML checks + operator HITL viewports | Acceptance checklist §7 |
| **22** | **Deploy manifest** | SHA256 post-deploy + `qa-dealers.html` | Manifest committed to `m9.16-work/` |
| **23** | **Stable checkpoint** | Register `SITE-002-STABLE-LIVE-M9.16-DEALERS-01` | Criteria §9 met |
| **24** | **Git checkpoint** | Repo documentation + work copies | Operator-requested |

**Explicitly excluded from steps:** PLP `blockdealersform` slimming · suppressing PLP form · Commercial Trust form field changes — register under **future B3 task**.

---

## 7. Acceptance checklist

Every item is **testable** on https://zpm.new-site.space/dealers after implementation.

### 7.1 Structure and copy (C01–C20)

| # | Requirement | Test |
|---|-------------|------|
| C01 | H1 «Дилерам и оптовым партнёрам» via page-intro | View source / visual |
| C02 | Lead paragraph present (manufacturer + Russia supply) | Text match copy |
| C03 | Lead **does not** mention СНГ | Text search «СНГ» = absent |
| C04 | BLOCK 01 — partner matrix (5 rows) | Count rows/types |
| C05 | BLOCK 01 helper links to `/payment-methods` | Click link |
| C06 | BLOCK 02 — five H3 OEM proof headings | Heading audit |
| C07 | BLOCK 02 channel note present | Text match |
| C08 | OEM trust row — manufacturer · ИНН · Барнаул · About | 4 labels |
| C09 | BLOCK 03 — outcome table (6 rows) | Count rows |
| C10 | BLOCK 03 helper — no public price list | Text present |
| C11 | **Cooperation process section exists** | BLOCK 04 landmark |
| C12 | **5 steps** in timeline | Count step badges |
| C13 | Step 5 links Payment + Delivery | Link audit |
| C14 | BLOCK 05 — 4-node supply chain | Text nodes present |
| C15 | BLOCK 05 cross-link table (3 rows) | Delivery · Custom · Payment |
| C16 | Warranty one-line pointer to `/guarantee` | Link works |
| C17 | **FAQ — 8 items** | Count accordion items |
| C18 | CTA H2 «Получить условия сотрудничества» | Exact match |
| C19 | Form title «Заявка на сотрудничество» | Present |
| C20 | All copy spot-check (10 strings) vs copy v1.1 | Diff against copy doc |

### 7.2 Dealer logic (D01–D10)

| # | Requirement | Test |
|---|-------------|------|
| D01 | Page reads as **manufacturer partnership** — not recruitment landing | Operator visual review |
| D02 | **Proof → benefits → process → form** visual order | Scroll + weight audit |
| D03 | BLOCK 02 visually **stronger** than form zone | CSS weight / operator HITL |
| D04 | **No** discount / MOQ / territory badges | DOM search |
| D05 | **No** partner count or logo wall | Visual |
| D06 | **No** franchise / MLM tier visuals | Visual |
| D07 | Channel policy = honest prose — no fake exclusivity map | Visual |
| D08 | Direct-buyer redirect to Payment in BLOCK 01 | Helper link |
| D09 | Form is **endpoint** — not above fold | Viewport 1440 above-fold audit |
| D10 | Success message — manager callback — not instant dealer acceptance | Text match |

### 7.3 Forbidden content (F01–F10)

| # | Requirement | Test |
|---|-------------|------|
| F01 | **No** territory / dealer map embed | DOM search map patterns |
| F02 | **No** discount % hero badges | — |
| F03 | **No** mid-page primary submit button | Single CTA zone |
| F04 | **No** duplicate About/Delivery/Payment/Warranty bodies | Link-only cross-refs |
| F05 | **No** TK tables or shipment point cards | Delivery scope only |
| F06 | **No** bank / VAT / payment method bodies | Payment scope only |
| F07 | **No** warranty term badge | Warranty scope only |
| F08 | **No** СНГ geography | Text search |
| F09 | **No** website field in form | Field audit |
| F10 | **No** ИНН field in form | Field audit |

### 7.4 FAQ (Q01–Q05)

| # | Requirement | Test |
|---|-------------|------|
| Q01 | FAQ accordion **single-open** | Click two headers |
| Q02 | `aria-expanded` toggles on buttons | DevTools / a11y |
| Q03 | `aria-controls` links button to panel id | Attribute audit |
| Q04 | Panels use `hidden` when closed | DOM state |
| Q05 | FAQ 1 points to matrix — does not duplicate full table | Text length check |

### 7.5 Accordion technical (A01–A03)

| # | Requirement | Test |
|---|-------------|------|
| A01 | Root `data-dealers-faq` present | Attribute on section |
| A02 | Re-click open item closes it | Click behaviour |
| A03 | No conflict with mobile menu accordion | Mobile nav still works |

### 7.6 Responsive (R01–R04)

| # | Requirement | Test |
|---|-------------|------|
| R01 | Desktop ≥1440 — matrix + proof stack readable | Screenshot |
| R02 | Tablet 1024 — matrix + outcome table stack | No overflow |
| R03 | Mobile 390 — FAQ usable, form full width | Screenshot |
| R04 | **No horizontal overflow** 390/1024/1440 | DevTools |

### 7.7 Console, overflow, ARIA (T01–T10)

| # | Requirement | Test |
|---|-------------|------|
| T01 | **No console errors** on load | Browser devtools |
| T02 | **Commercial Trust CTA architecture reused** | `zpm-commercial-trust__card` or equivalent |
| T03 | **Contacts form discipline** | `zpm-form`, mask, email validate, consent |
| T04 | **No duplicate CSS file** on live | Single `style.css` append |
| T05 | Breadcrumb Главная → Дилерам | Present |
| T06 | Meta title/description match copy utility | `<title>` + meta |
| T07 | Header/footer/nav unchanged | Visual compare |
| T08 | `/dealers` HTTP 200 | curl -L |
| T09 | Twig cache cleared after deploy | Operator confirm |
| T10 | Timeline `<ol>` has accessible label | `aria-label` or caption |

### 7.8 CTA, breadcrumbs, cross-links (X01–X08)

| # | Requirement | Test |
|---|-------------|------|
| X01 | Primary CTA «Обсудить сотрудничество» scrolls/submits to form | Click |
| X02 | Secondary CTA → `/about` | Link works |
| X03 | Tertiary CTA → `/contact/` | Link works |
| X04 | Phone `8 (3852) 72-18-90` and `info@bzpm.ru` in CTA zone | Present |
| X05 | **company field required** | HTML `required` |
| X06 | **city field required** | HTML `required` |
| X07 | comment field optional | No `required` |
| X08 | Consent links `/privacy-policy` | Present |

**Total checklist items: 60** (exceeds minimum 50).

---

## 8. Rollback

**Without implementation** — planned recovery path only.

### 8.1 Files affected (implementation task)

| Priority | Remote file |
|----------|-------------|
| P1 | `catalog/view/theme/default/template/information/dealers.twig` |
| P2 | `catalog/controller/information/dealers.php` |
| P3 | `assets/css/style.css` (append reversal) |
| P4 | `assets/js/main.js` (accordion selector delta) |
| P5 | `oc_seo_url` dealers row |

### 8.2 Rollback order

1. Restore `oc_seo_url` → prior `information/information&information_id=…` target  
2. Delete or restore `dealers.php` from backup (if new file — remove)  
3. Delete or restore `dealers.twig` from backup  
4. Restore `style.css` from `backups/style.css.pre-m9.16-dealers.bak`  
5. Restore `main.js` from `backups/main.js.pre-m9.16-dealers.bak`  
6. Clear `system/storage/cache/template/*`  
7. Verify `/dealers` renders legacy CMS content from `qa` capture baseline: `m9.15-work/dealers-live-snippet.html`

### 8.3 Rollback checkpoints

| Checkpoint | Trigger | Action |
|------------|---------|--------|
| **RB-0** | Pre-deploy | `preflight-manifest.json` SHA256 |
| **RB-1** | Controller/route broken | Revert seo_url + remove dealers.php only |
| **RB-2** | Visual/CSS failure | Restore twig + style.css |
| **RB-3** | JS regression | Restore main.js; static FAQ remains usable expanded |
| **RB-4** | Catastrophic | Operator Beget full backup |

### 8.4 Minimal recovery path

**Minimum files to restore legacy `/dealers`:** seo_url row + remove `dealers.twig` + remove `dealers.php` → generic information page returns.

**PLP rollback:** Not in M9.16 scope — `blockdealersform.twig` unchanged by design.

---

## 9. Stable checkpoint criteria

**Checkpoint name:** `SITE-002-STABLE-LIVE-M9.16-DEALERS-01`

Implementation becomes this checkpoint **when all are true**:

| # | Criterion |
|---|-----------|
| S1 | `/dealers` serves `information/dealers` custom template on live TEST |
| S2 | Acceptance checklist §7 — **all C, D, F, Q, A, R, T, X** items PASS (operator HITL for visual where marked) |
| S3 | Deploy manifest with SHA256 pre/post stored in `reports/m9.16-work/` |
| S4 | Backups exist for every overwritten remote file |
| S5 | No scope bleed — header/footer/catalog/PLP dealer form/About/Delivery/Payment/Warranty/Contacts untouched |
| S6 | Baseline doc registered at `baselines/SITE-002-STABLE-LIVE-M9.16-DEALERS-01.md` |
| S7 | Knowledge Map updated with §21 Dealers page entry |
| S8 | Corp qualification form live on `/dealers` with copy v1.1 field set (no website) |
| S9 | Education blocks visually dominate form zone per Design Charter weight budget |
| S10 | **B3 PLP reconciliation documented as OPEN** — not falsely marked closed |
| S11 | Recovery remains **CLOSED** — checkpoint is forward progress |

**Authority after checkpoint:** Supersedes prior generic `/dealers` CMS surface **for dealers page domain only** — M9.14/M9.15/M9.17 checkpoints otherwise unchanged.

---

## 10. Risks

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R1 | **Form-as-hero drift** — page reads as lead-gen landing | **Critical** | Weight budget §2.3; QA D03/D09 |
| R2 | **B3 scope creep** — PLP form edited during corp page task | **High** | Explicit UNTOUCHED list §5.3; separate future charter |
| R3 | seo_url mis-edit breaks `/dealers` | **High** | Preflight capture + RB-1 |
| R4 | **Inverted form ownership persists** — corp still formless after deploy | **Critical** | S8 checkpoint criterion; step 14 mandatory |
| R5 | Franchise / MLM aesthetic drift | **High** | Forbidden patterns §2.4; QA D06 |
| R6 | Discount badge temptation | **High** | OQ-D03 — no % visuals; QA D04 |
| R7 | Fake partner logos / map / counts | **High** | No assets — structural design only |
| R8 | **B1 MO address** street leaks into BLOCK 05 | **High** | Region-only prose until operator lock |
| R9 | Legacy **СНГ** copy reintroduced | **Medium** | Copy v1.1 Russia-only; QA C03/F08 |
| R10 | SC-13 matrix horizontal scroll trap mobile | **Medium** | Stack cards ≤1024px; QA R02 |
| R11 | FAQ accordion JS conflicts with mobile menu | **Medium** | Scoped `[data-dealers-faq]` root init |
| R12 | Trust strip + OEM row badge fatigue | **Medium** | OQ-DC-DE04 — pick one at step 6 |
| R13 | `style.css` drift vs repo backups | **Medium** | Live FTP capture at preflight |
| R14 | Operator gates B6/B8 open at deploy | **Medium** | Record operator ack in implementation report |
| R15 | **B3 governance confusion** — operator blocks corp ship waiting for PLP | **High** | Charter lock: B3 = governance blocker only; corp READY |
| R16 | Form `action="#"` / `dialog=7` handler mismatch | **Low** | Preflight verify; same as PLP if confirmed |
| R17 | Commercial Trust inbound link expects depth — page still thin | **Medium** | M9.16 closes CP-08 corp owner promise |
| R18 | Production URL parity unknown | **Low** | TEST-first; document at deploy |

**SECURITY RISK:** Deploy scripts may contain FTP credentials — never commit credentials; use operator-local secrets only.

---

## 11. Ready for implementation

### 11.1 Architectural uncertainty closure

| Domain | Status |
|--------|--------|
| Page structure and block order | **CLOSED** |
| Component reuse vs new build | **CLOSED** |
| File touch list | **CLOSED** |
| Route strategy | **CLOSED** (`information/dealers`) |
| Visual hierarchy (manufacturer-partnership) | **CLOSED** |
| Forbidden patterns | **CLOSED** |
| Form MVP fields | **CLOSED** |
| Rollback path | **CLOSED** |
| QA criteria | **CLOSED** |
| B3 PLP scope boundary | **CLOSED** (documented out of scope) |

### 11.2 Remaining operator actions (not architectural)

| Item | Blocks coding? | Blocks deploy? |
|------|----------------|----------------|
| B6/B8 formal sign-off | No | Recommended before deploy |
| B1 МО street address lock | No — region-only prose default | Recommended before production parity |
| **B3 PLP reconciliation** | **No** | **No** for corp page — separate task |
| OQ-DC-DE04 trust strip | Pick at step 6 | No |
| OQ-DC-DE05 OEM row placement | Default after BLOCK 02 | No |
| `dialog=7` confirmation | Verify at preflight step 1 | No |

### 11.3 Final verdict

## **READY**

**Justification:** All implementation architecture decisions required to start the M9.16 **standalone `/dealers`** coding task are documented. Route, file map, section mapping, component matrix, execution order, acceptance tests, rollback, and stable checkpoint are defined. Behaviour derives from copy v1.1, Design Charter, Design Program SC registry, and M9.14–M9.17 corp page patterns. **B3 does not block** corp page implementation — PLP integration remains a **separate governed task**.

**Next task:** M9.16 Dealers **implementation** — begin at Execution order step 1 (preflight capture). Do **not** modify PLP `blockdealersform.twig` in the same task unless operator opens a dedicated B3 charter.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-28 | **CREATED** — Implementation Charter v1; standalone `/dealers` scope; B3 governance boundary; 60-item acceptance checklist; cross-check vs Delivery/Payment/Warranty |

---

*SITE-002 M9.16 Dealers Implementation Charter v1 — documentation only. No OpenCart, Twig, CSS, JS, deploy, or PLP changes authorized by this file alone.*
