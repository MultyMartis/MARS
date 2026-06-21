# WF-R01.3 G2-R2 PROMO Money-Page Scaffold Completion Charter v1

**Remediation package ID:** **G2-R2**  
**Parent gate:** **G2** — PROMO + CATALOG scaffold ([wf-r01-3-g2-formal-gate-pass-charter-v1.md](wf-r01-3-g2-formal-gate-pass-charter-v1.md))  
**Parent programme:** **WF-R01.3** — Reference Implementation Expansion  
**Program parent:** **WF-R01** — FOUNDRY Registry Expansion Program (**CHARTERED**)  
**Version:** v1  
**Date:** 2026-06-21  
**Mode:** normative remediation charter — **documentation and wave contract only**

**Honesty boundary:** This charter **authorizes and defines** G2-R2 remediation procedure, PROMO money-page scaffold scope, contracts, waves, and exit criteria. **Charter acceptance does not constitute scaffold implementation, G2-R2 COMPLETE, RSC/PC accrual, PROMO SC PASS, G2 evaluation, or G2 PASS.**

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **ACCEPTED** |
| **Charter decision** | **ACCEPTED** — normative operator authority for G2-R2 PROMO money-page scaffold completion |
| **Package state after charter** | **CHARTERED** · **NOT IMPLEMENTED** · **NOT COMPLETE** |
| **Implementation state** | **NOT STARTED** — no scaffolds authorized by this charter alone |
| **Coverage impact** | **None** — metrics frozen at charter snapshot (§31–§32) |
| **G2 gate state** | **CHARTERED** · **READY WITH BLOCKERS** · **NOT EVALUATED** · **NOT PASSED** · **NOT CLOSED** |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Package ID** | **G2-R2** |
| **Canonical name** | **PROMO Money-Page Scaffold Completion** |
| **Formal charter name** | **WF-R01.3 G2-R2 PROMO Money-Page Scaffold Completion Charter v1** |
| **Parent programme** | **WF-R01.3** — Reference Implementation Expansion |
| **Parent gate** | **G2** |
| **Predecessor remediation** | **G2-R1** — W3 PROMO Reference Completion (**COMPLETE WITH MINOR DEBT**) |
| **Successor remediation** | **G2-R3** — SEARCH_RESULTS_PAGE Authority Reconciliation |
| **Gate criteria addressed** | **G2-10** (PROMO money-page scaffolds) · **G2-14** (PROMO PC) · feeds **G2-12** (PROMO SC) |
| **Charter path** | `projects/mars-website-factory/wf-r01-3-g2-r2-promo-money-page-scaffold-completion-charter-v1.md` |

**Charter / implementation distinction (binding):**

```text
G2-R2 charter acceptance ≠ scaffold implementation
G2-R2 charter acceptance ≠ G2-R2 COMPLETE
G2-R2 charter acceptance ≠ RSC accrual
G2-R2 charter acceptance ≠ PC accrual
G2-R2 charter acceptance ≠ PROMO SC PASS
G2-R2 charter acceptance ≠ G2 evaluation
G2-R2 charter acceptance ≠ G2 PASS
```

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| G2 formal gate charter | [wf-r01-3-g2-formal-gate-pass-charter-v1.md](wf-r01-3-g2-formal-gate-pass-charter-v1.md) | Parent gate; G2-R2 package §22; PROMO scaffold §15 |
| G2 charter pass REPORT | [wf-r01-3-g2-formal-gate-pass-charter-pass-v1.md](../../reports/wf-r01-3-g2-formal-gate-pass-charter-pass-v1.md) | Readiness snapshot |
| G2-R1 W3 charter | [wf-r01-3-g2-r1-w3-promo-reference-completion-charter-v1.md](wf-r01-3-g2-r1-w3-promo-reference-completion-charter-v1.md) | Predecessor; G2-R2 handoff §29 |
| G2-R1 W3-E exit | [wf-r01-3-g2-r1-w3-e-exit-g2-r2-readiness-v1.md](../../reports/wf-r01-3-g2-r1-w3-e-exit-g2-r2-readiness-v1.md) | G2-R2 readiness preflight |
| Coverage Model | [wf-r01-3-1-coverage-model-charter-v1.md](wf-r01-3-1-coverage-model-charter-v1.md) | PROMO minimum § Template-Art; RSC/SC/PC rules |
| Vocabulary Canon | [foundry-vocabulary-canon-charter-v1.md](foundry-vocabulary-canon-charter-v1.md) | F3 block family |
| WF-R01.3 program design | [wf-r01-3-reference-expansion-program-design-v1.md](../../reports/wf-r01-3-reference-expansion-program-design-v1.md) | Wave map; PROMO scaffolds |
| WF-R01 program design | [foundry-registry-expansion-program-design-v1.md](../../reports/foundry-registry-expansion-program-design-v1.md) | Subprogram decomposition |
| Post-G1 track selection | [wf-r01-3-post-g1-track-selection-v1.md](../../reports/wf-r01-3-post-g1-track-selection-v1.md) | G2 composite semantics |
| Global Shell Contract | [global-shell-contract-v1.md](global-shell-contract-v1.md) | Shell order |
| Page-Type Shell Matrix | [page-type-shell-matrix-v1.md](page-type-shell-matrix-v1.md) | Per-type shell REQ/POL |
| Reference Scaffold Contract | [reference-scaffold-contract-v1.md](reference-scaffold-contract-v1.md) | RSC accrual chain |
| Page-Type Registry | [PAGE-TYPE-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md) | Registered page types |
| Block Registry | [BLOCK-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md) | 32 `block_id` SSOT |
| Core Block Library | [CORE-BLOCK-LIBRARY-v1.md](../../workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md) | Partial inventory |
| Block Gaps | [BLOCK-GAPS-v1.md](../../workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md) | Gap rows |
| Site-Type Block Matrix | [SITE-TYPE-BLOCK-MATRIX-v2.md](../../workspaces/website-factory-reference-v1/block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md) | Site-type applicability |
| Page-Block Mapping | [PAGE-BLOCK-MAPPING-v1.md](../../workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md) | Page-type block stances |
| CATEGORY scaffold precedent | [CATEGORY-PAGE-REFERENCE-COMPOSITION-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/CATEGORY-PAGE-REFERENCE-COMPOSITION-v1.md) · [CATEGORY-PAGE-SCAFFOLD-MANIFEST-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/CATEGORY-PAGE-SCAFFOLD-MANIFEST-v1.md) | C5 composition/manifest pattern |
| PRODUCT scaffold precedent | [PRODUCT-PAGE-REFERENCE-COMPOSITION-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/PRODUCT-PAGE-REFERENCE-COMPOSITION-v1.md) · [PRODUCT-PAGE-SCAFFOLD-MANIFEST-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/PRODUCT-PAGE-SCAFFOLD-MANIFEST-v1.md) | C6 composition/manifest pattern |
| Roadmap | [roadmap.md](roadmap.md) | Programme sync |
| OPERATIONAL-INDEX | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Operator entry |

**Authority hierarchy for G2-R2 contracts:** PAGE-TYPE-REGISTRY-v1 + PAGE-BLOCK-MAPPING-v1 **>** Page-Type Shell Matrix **>** Coverage Model § PROMO **>** G2 formal gate charter §15 **>** G2-R1 handoff notes.

---

## 4. Purpose

G2-R2 exists to close the **PROMO money-page scaffold gap** — the three missing reference scaffolds that block **G2-10**, **G2-14**, and honest progress toward **G2-12** (PROMO SC).

**G2-R2 confirms:**

- Canonical PROMO money-page set = **`SERVICE_PAGE` + `ABOUT_PAGE` + `CONTACT_PAGE`**
- Registry and shell preflight for three registered page types
- Per-page scaffold minimum, composition contract, and manifest contract
- Scaffold-owned region policy and semantic boundaries (especially SERVICE_PAGE detail vs SERVICES collection)
- Form/contact runtime boundary and fictional-content policy
- Partial readiness inventory and W3 reuse policy
- Implementation waves, dependency order, and RSC/PC/PROMO SC accounting contracts
- Exit criteria and G2-R3 handoff inputs

**G2-R2 does not confirm:**

```text
scaffold HTML exists
composition documents published
manifest documents published
RSC 6/10
PROMO SC PASS
PROMO PC accrued
G2 evaluation or G2 PASS
production readiness
client deployment
CMS templates
live routing
```

---

## 5. Scope

### In scope

- Three registered PROMO money-page types: `SERVICE_PAGE`, `ABOUT_PAGE`, `CONTACT_PAGE`
- Reference scaffolds in `workspaces/website-factory-reference-v1/src/pages/`
- Per-page Reference Composition documents in `page-architecture/`
- Per-page Scaffold Manifest documents in `page-architecture/`
- Page-level SCSS in `src/scss/pages/`
- Structural validation, build evidence, wave REPORTs
- RSC / PC / PROMO SC accounting in exit wave only
- G2-R2 exit REPORT and G2-R3 handoff evaluation

### Out of scope

- Production pages, client design, pixel-perfect fidelity
- CMS templates, backend forms, live routing, deployment
- Registry / Coverage Model / Vocabulary Canon mutation
- New `block_id` rows or new page types
- `SEARCH_RESULTS_PAGE` (G2-R3)
- G2 formal evaluation (G2-R5)
- Metric accrual from this charter pass

---

## 6. Out of Scope

Explicit exclusions (binding):

| Exclusion | Reason |
|-----------|--------|
| Bounded-host-only evidence | `promo-block-references.html` is W3 evidence — not RSC/PC |
| LANDING_PAGE re-scaffold | Already RSC 1/1 LANDING |
| CATALOG scaffolds | G2-R4 / existing C5–C6 |
| MAP block / map API | CONTACT_PAGE — presentation NAP only; no embed |
| FEATURES partial creation | Use `BENEFITS` on SERVICE_PAGE per mapping; no new block wave in G2-R2 unless separate charter |
| PROCESS re-build | Pre-existing T1+ partial — include on scaffolds only when mapping allows |
| G2 closure | Requires G2-R3–R5 + formal evaluation |

---

## 7. Current State

**Snapshot date:** 2026-06-21 (charter acceptance)  
**Source:** [wf-r01-3-g2-r1-w3-e-exit-g2-r2-readiness-v1.md](../../reports/wf-r01-3-g2-r1-w3-e-exit-g2-r2-readiness-v1.md)

| Dimension | Value |
|-----------|-------|
| **RC** | **32/32** |
| **RPC** | **26/32** |
| **RSC** | **3/10 global** · **1/1 LANDING** · **1/1 CATEGORY_PAGE** · **1/1 PRODUCT_PAGE** |
| **SC** | **LANDING PASS** · **CATALOG PARTIAL** · **PROMO NOT PASSED** |
| **PC** | **1/1 LANDING corridor** · **1/1 CATALOG corridor** |

**W3 partials (G2-R1 complete):** `SERVICES` · `TEAM` · `ABOUT` — **PARTIAL / T1+**

**PROMO scaffolds:** **absent** for all three page types

**G2-R1 state:** **COMPLETE WITH MINOR DEBT** (operator browser QA deferred — non-blocking)

This snapshot is **not** a gate result.

---

## 8. Package Relationship to G2

| Field | Value |
|-------|-------|
| **G2 state** | **CHARTERED** · **READY WITH BLOCKERS** · **NOT EVALUATED** · **NOT PASSED** · **NOT CLOSED** |
| **G2-R1** | **COMPLETE WITH MINOR DEBT** — closes G2-02/03/04 |
| **G2-R2 addresses** | G2-10 · G2-14 · feeds G2-12 |
| **G2-R2 does not close** | G2-11 (CATALOG SC) · G2-19/20 (formal evaluation) · G2 overall |
| **Remediation sequence** | G2-R1 → **G2-R2** → G2-R3 → G2-R4 → G2-R5 → formal evaluation |

---

## 9. Page-Type Registry Preflight

| Page type | Registered | Current scaffold | RSC eligible | Shell authority | Block mapping |
| --------- | ---------- | ---------------- | ------------ | --------------- | ------------- |
| **SERVICE_PAGE** | **Yes** — PAGE-TYPE-REGISTRY § SERVICE_PAGE; `PROMO`, `CORPORATE` | **None** | **Yes** — when scaffold + composition + manifest + validation complete | [page-type-shell-matrix-v1.md](page-type-shell-matrix-v1.md) §6 row | PAGE-BLOCK-MAPPING § SERVICE_PAGE |
| **ABOUT_PAGE** | **Yes** — PAGE-TYPE-REGISTRY § ABOUT_PAGE; `PROMO`, `CORPORATE` | **None** | **Yes** | Same matrix §6 row | PAGE-BLOCK-MAPPING § ABOUT_PAGE |
| **CONTACT_PAGE** | **Yes** — PAGE-TYPE-REGISTRY § CONTACT_PAGE; `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE` | **None** | **Yes** | Same matrix §6 row | PAGE-BLOCK-MAPPING § CONTACT_PAGE |

**Preflight result:** **SCAFFOLD ELIGIBLE** for all three — no Registry row creation required.

---

## 10. PROMO Corridor Definition

**Source:** Coverage Model § Template-Art minimum sets · PROMO; G2 charter §15

### Corridor members

| Member | Role |
|--------|------|
| `SERVICE_PAGE` | Service money page |
| `ABOUT_PAGE` | Company / trust page |
| `CONTACT_PAGE` | Contact hub |

### Scaffold minimum

- **3/3** registered PROMO primary money-page scaffolds required for honest G2 closure against Coverage Model § PROMO minimum
- **One scaffold alone is insufficient** (G2 charter §15 reconciliation)

### Composition minimum

- **One `*-REFERENCE-COMPOSITION-v1.md` per page type** (C5/C6 precedent)
- Compositions document block sequence, scaffold-owned regions, and runtime exclusions

### RSC relationship

- Each validated scaffold may accrue **+1** global RSC (10-type denominator)
- Potential delta: **+3** → **6/10** maximum if all three complete

### PC relationship

- **Unit of accrual:** **PROMO corridor** — notation **`1/1 PROMO corridor`**
- **Feeding artefacts:** three page-type Reference Compositions (SERVICE · ABOUT · CONTACT)
- **Accrual rule:** corridor unit accrues only when **all three** compositions are **PUBLISHED** with matching scaffold evidence (CATALOG corridor precedent: corridor = composite pilot minimum, not single-page shorthand)
- **Double-count policy:** each page-type composition is **not** a separate global PC unit; they compose one PROMO corridor unit under G2-14
- **Charter pass accrual:** **zero**

### PROMO SC relationship

- **PROMO SC PASS** requires Coverage Model PROMO minimum: LANDING set + multi-page blocks (**SERVICES, TEAM, ABOUT, PROCESS**) + **three scaffolds** + shell minimum
- **G2-R2 responsibility:** scaffolds + compositions + manifests + build/validation evidence
- **Outside G2-R2:** `PROCESS` already exists; PROMO SC evaluated only in **G2-R2 P5** exit wave — **not** at charter acceptance

---

## 11. Shell Matrix

Extracted from [page-type-shell-matrix-v1.md](page-type-shell-matrix-v1.md) §6 (binding codes: REQ · POL · N/A · FORB).

| Shell element | SERVICE_PAGE | ABOUT_PAGE | CONTACT_PAGE |
| ------------- | ------------ | ---------- | ------------ |
| **HEADER_NAV** | REQ | REQ | REQ |
| **MAIN** | REQ | REQ | REQ |
| **BREADCRUMBS** | POL | REQ | POL |
| **PAGE_IDENTITY** | — (scaffold-owned; not a matrix row) | — | — |
| **SEARCH** slot | N/A | N/A | N/A |
| **FILTERS** slot | N/A | N/A | N/A |
| **PAGINATION** | N/A | N/A | N/A |
| **FOOTER** | REQ | REQ | REQ |
| **LEGAL_LINKS** | REQ (nested in FOOTER) | REQ | REQ |

**POL notes (binding):**

- `SERVICE_PAGE` BREADCRUMBS — recommended parent hub link (**POL**)
- `ABOUT_PAGE` BREADCRUMBS — internal corporate page (**REQ**)
- `CONTACT_PAGE` BREADCRUMBS — optional shallow trail (**POL**)

---

## 12. Page-Block Mapping

Source: [PAGE-BLOCK-MAPPING-v1.md](../../workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md). **Matrix state** = mapping stance. **Reference state** from CORE-BLOCK-LIBRARY-v1.

### SERVICE_PAGE

| Block | Matrix state | Current reference state | Scaffold role |
| ----- | ------------ | ----------------------- | ------------- |
| HEADER_NAV | REQUIRED | T1+ — `sections/header-nav.html` | Global shell |
| BREADCRUMBS | — (Tier B layout-component) | T1+ — `components/breadcrumbs.html` | **POL** — include on scaffold |
| HERO | REQUIRED | T1+ — `sections/hero.html` | **Compact alternative:** scaffold-owned PAGE_IDENTITY may substitute per §15 |
| BENEFITS | REQUIRED (or FEATURES) | T1+ — `sections/benefits.html` | Scope / capabilities — **use BENEFITS** (`FEATURES` partial absent) |
| FEATURES | REQUIRED (or BENEFITS) | **Not implemented** | **Exclude** — satisfied by BENEFITS |
| FAQ | REQUIRED | T1+ — `sections/faq.html` | Service objections |
| LEAD_FORM | REQUIRED | T1+ — `sections/lead_form.html` | Primary conversion |
| CTA | REQUIRED | T1+ — `sections/cta_band.html` | Contextual action |
| PROCESS | OPTIONAL | T1+ — `sections/process.html` | Proof stack — recommended |
| TRUST | OPTIONAL | T1+ — `sections/trust.html` | Proof stack — optional |
| CASES | OPTIONAL | T1+ — `sections/cases.html` | Optional proof |
| SERVICES | — (not listed) | PARTIAL — `components/services.html` | **Optional adjacent** — related directions only (§16) |
| FOOTER | REQUIRED | T1+ — `sections/footer.html` | Global shell |
| LEGAL_LINKS | REQUIRED | T1+ — `components/legal-links.html` | Nested in FOOTER |
| FILTERS · PRODUCT_GRID · CATEGORIES · CART | FORBIDDEN | N/A | **Exclude** |

### ABOUT_PAGE

| Block | Matrix state | Current reference state | Scaffold role |
| ----- | ------------ | ----------------------- | ------------- |
| HEADER_NAV | REQUIRED | T1+ | Global shell |
| BREADCRUMBS | — (Tier B) | T1+ | **REQ** per shell matrix |
| HERO | REQUIRED | T1+ | **Compact alternative:** scaffold-owned PAGE_IDENTITY permitted |
| ABOUT | REQUIRED | PARTIAL / T1+ — `components/about.html` | Company narrative — **required** |
| TEAM | OPTIONAL | PARTIAL / T1+ — `components/team.html` | Recommended for honest ABOUT_PAGE composition |
| TRUST | OPTIONAL | T1+ | Optional proof |
| CERTIFICATES · CASES · PARTNERS | OPTIONAL | CASES T1+; others registry-only | Optional — exclude if no partial |
| CTA | OPTIONAL | T1+ | Soft conversion — optional |
| LEAD_FORM | FORBIDDEN (primary) | T1+ exists | **Exclude as primary** — CTA optional only |
| PROCESS | — (not listed) | T1+ | Optional supporting context — not required by mapping |
| FOOTER · LEGAL_LINKS | REQUIRED | T1+ | Global shell |
| Commerce blocks | FORBIDDEN | N/A | **Exclude** |

### CONTACT_PAGE

| Block | Matrix state | Current reference state | Scaffold role |
| ----- | ------------ | ----------------------- | ------------- |
| HEADER_NAV | REQUIRED | T1+ | Global shell |
| BREADCRUMBS | — (Tier B) | T1+ | **POL** — include recommended |
| HERO | OPTIONAL | T1+ | **Compact alternative:** scaffold-owned PAGE_IDENTITY preferred |
| CONTACTS | REQUIRED | T1+ — `sections/contact_block.html` | NAP hub — **required** |
| LEAD_FORM | OPTIONAL | T1+ | Recommended — presentation only (§19) |
| MAP | OPTIONAL | **Not implemented** | **Exclude** — no map embed/API |
| FAQ | — (not listed) | T1+ | Optional supporting — not required |
| TRUST | — (not listed) | T1+ | Optional supporting context |
| FOOTER · LEGAL_LINKS | REQUIRED | T1+ | Global shell |
| FILTERS · commerce | FORBIDDEN | N/A | **Exclude** |

---

## 13. Scaffold-Owned Region Policy

Scaffold-owned regions **do not** receive `data-block-id`, Registry rows, or RPC credit.

| Region | Applicable page type | Why scaffold-owned | Hook policy | Coverage effect |
| ------ | -------------------- | ------------------ | ----------- | --------------- |
| **PAGE_IDENTITY** | All three | Compact h1 + intro; substitutes full HERO when documented; C5 precedent | Page-scoped BEM classes only (e.g. `wf-service-page__identity`); **no** `data-block-id` | **None** on RPC/RSC |
| **service-detail-context** | SERVICE_PAGE | No canonical single-service detail block; avoids SERVICES semantic conflict | Wrapper + neutral fictional copy; **no** Registry id | **None** |
| **company-narrative-bridge** | ABOUT_PAGE | Optional glue between ABOUT and TEAM without new block | Optional wrapper between canonical includes | **None** |
| **contact-support-context** | CONTACT_PAGE | Optional intro between identity and CONTACTS | Optional wrapper | **None** |
| **main-inner / layout wrapper** | All three | Page layout grouping (container, spacing) | Page root class on `<main>` + inner container | **None** |

**Rules:**

- Document every scaffold-owned region in composition + manifest
- Do not duplicate block ownership (e.g. do not wrap ABOUT inside a second ABOUT-like region)
- Tier B **BREADCRUMBS** remains a canonical partial include — not scaffold-owned

---

## 14. Universal Scaffold Contract

Each PROMO money-page scaffold **must** satisfy [reference-scaffold-contract-v1.md](reference-scaffold-contract-v1.md):

| Requirement | Detail |
|-------------|--------|
| Registered page type | One of `SERVICE_PAGE` · `ABOUT_PAGE` · `CONTACT_PAGE` |
| Source HTML page | `src/pages/*-page-reference.html` |
| Valid shell order | HEADER_NAV → MAIN → FOOTER → LEGAL_LINKS nested |
| One MAIN | Exactly one `<main id="main">` |
| Canonical block includes | Registry `block_id` partials via `@@include` |
| Composition document | `*-REFERENCE-COMPOSITION-v1.md` **PUBLISHED** |
| Scaffold manifest | `*-SCAFFOLD-MANIFEST-v1.md` **PUBLISHED** |
| Page SCSS | `src/scss/pages/_*-page-reference.scss` connected in build |
| Build PASS | `npm run build` exit 0 in reference workspace |
| Structural validation | Operator checklist per Reference Scaffold Contract |
| Wave REPORT | Per implementation wave |
| Git evidence | Selective commit; no foreign WIP |

**Not required:** final visual design · production content · CMS · backend · live routing · pixel-perfect fidelity · WCAG certification

---

## 15. SERVICE_PAGE Contract

### Shell sequence

```text
HEADER_NAV

MAIN
├── BREADCRUMBS (POL)
├── scaffold-owned PAGE_IDENTITY
├── scaffold-owned service-detail-context
├── BENEFITS
├── PROCESS (recommended)
├── FAQ
├── CTA
├── LEAD_FORM
├── SERVICES (optional — adjacent directions only)

FOOTER
└── LEGAL_LINKS
```

### Required blocks

HEADER_NAV · BENEFITS (satisfies BENEFITS|FEATURES rule) · FAQ · LEAD_FORM · CTA · FOOTER · LEGAL_LINKS

### Recommended blocks

BREADCRUMBS · PROCESS · TRUST

### Optional blocks

SERVICES (adjacent only) · CASES

### Scaffold-owned regions

PAGE_IDENTITY · service-detail-context · main layout wrapper

### HERO / PAGE_IDENTITY policy

PAGE-BLOCK-MAPPING requires **HERO**. Reference scaffolds may use **scaffold-owned PAGE_IDENTITY** (compact h1 + intro) following CATEGORY_PAGE C5 precedent — documented in composition as **compact money-page header** fulfilling HERO stance without `sections/hero.html` include.

### Exclusions

FILTERS · catalog blocks · FORBIDDEN commerce · FEATURES partial (use BENEFITS) · SERVICES as primary detail body

---

## 16. SERVICE_PAGE Semantic Boundaries

**Binding distinction:**

```text
SERVICES  = collection of service directions (hub / grid)
SERVICE_PAGE = single service or service-direction money page
```

| Concern | Rule |
|---------|------|
| Primary detail body | **scaffold-owned service-detail-context** — neutral fictional service description |
| SERVICES block on SERVICE_PAGE | **Optional** — role = related / adjacent service directions navigation; **not** primary detail |
| No new block_id | Do not create SERVICE_DETAIL or similar |
| W3 partial reuse | `components/services.html` via canonical include only when optional adjacent band included |

---

## 17. ABOUT_PAGE Contract

### Shell sequence

```text
HEADER_NAV

MAIN
├── BREADCRUMBS (REQ)
├── scaffold-owned PAGE_IDENTITY
├── ABOUT
├── TEAM (recommended)
├── PROCESS (optional supporting)
├── TRUST (optional)
├── CTA (optional)

FOOTER
└── LEGAL_LINKS
```

### Required blocks

HEADER_NAV · ABOUT · FOOTER · LEGAL_LINKS · BREADCRUMBS

### Recommended blocks

TEAM · TRUST · CTA

### Optional blocks

PROCESS · CASES

### Scaffold-owned regions

PAGE_IDENTITY · optional company-narrative-bridge · main layout wrapper

### Composition rule

ABOUT_PAGE **must** be a **page composition** (ABOUT + supporting blocks), **not** a bounded-host-style ABOUT-only strip. TEAM recommended to differentiate from W3 bounded host.

### Exclusions

LEAD_FORM as primary · commerce blocks · FEATURES as ABOUT substitute

---

## 18. CONTACT_PAGE Contract

### Shell sequence

```text
HEADER_NAV

MAIN
├── BREADCRUMBS (POL)
├── scaffold-owned PAGE_IDENTITY
├── CONTACTS
├── LEAD_FORM (recommended)
├── TRUST (optional supporting)
├── FAQ (optional)

FOOTER
└── LEGAL_LINKS
```

### Required blocks

HEADER_NAV · CONTACTS · FOOTER · LEGAL_LINKS

### Recommended blocks

BREADCRUMBS · LEAD_FORM · scaffold-owned PAGE_IDENTITY

### Optional blocks

TRUST · FAQ · HERO compact via PAGE_IDENTITY

### Map policy

**MAP block excluded** — no map embed, tile API, or geo widget. NAP via CONTACTS partial only.

### Exclusions

MAP · backend submission · live address/phone/email · CTA as primary (optional only)

---

## 19. Form and Contact Runtime Boundary

| Layer | Policy |
|-------|--------|
| **Presentation** | Reuse existing `LEAD_FORM` partial; static fields; native labels; existing local form behavior |
| **Contact data** | Neutral fictional organisation; `href="#"`; no PII |
| **Allowed** | Existing `js/core/form.js` / section scripts already bound to partial |
| **Forbidden** | Real submission endpoint · CRM · email sending · analytics · captcha · map API · network requests · live NAP |

**Binding:** form presentation may be reused; backend capability is **out of scope** for G2-R2.

---

## 20. Fictional Content Policy

All G2-R2 scaffolds use:

- Neutral page titles and meta descriptions
- Neutral breadcrumbs
- Fictional organisation context
- Fictional service / team / contact details
- `href="#"` for action links
- `robots noindex, nofollow` on reference pages

**Forbidden:** real client names · real contact details · real prices · real addresses · production URLs · commercial claims

---

## 21. Existing Partial Readiness

| Block | Registry state | Reference state | Relevant page types | Readiness |
| ----- | -------------- | --------------- | ------------------- | --------- |
| HEADER_NAV | Tier A | T1+ | All | **READY** |
| BREADCRUMBS | Tier B layout-component | T1+ | All | **READY** |
| HERO | F3 | T1+ | All (optional if PAGE_IDENTITY) | **READY WITH CONSTRAINTS** — compact policy applies |
| BENEFITS | F3 | T1+ | SERVICE_PAGE | **READY** |
| FEATURES | F3 | **Not implemented** | SERVICE_PAGE | **MISSING** — use BENEFITS per mapping |
| FAQ | F3 | T1+ | SERVICE · CONTACT (opt) | **READY** |
| CTA | F3 | T1+ | SERVICE · ABOUT (opt) | **READY** |
| LEAD_FORM | F3 | T1+ | SERVICE · CONTACT | **READY WITH CONSTRAINTS** — presentation only |
| PROCESS | F3 | T1+ | SERVICE · ABOUT (opt) | **READY** |
| SERVICES | F3 | PARTIAL / T1+ | SERVICE (opt) | **READY WITH CONSTRAINTS** — adjacent role only |
| ABOUT | F3 | PARTIAL / T1+ | ABOUT_PAGE | **READY WITH CONSTRAINTS** — W3 partial |
| TEAM | F3 | PARTIAL / T1+ | ABOUT_PAGE | **READY WITH CONSTRAINTS** — W3 partial |
| TRUST | F3 | T1+ | All (opt) | **READY** |
| CONTACTS | F3 | T1+ | CONTACT_PAGE | **READY** |
| FOOTER | F3 | T1+ | All | **READY** |
| LEGAL_LINKS | F3 | T1+ | All | **READY** |
| MAP | F3 | Not implemented | CONTACT (opt) | **N/A** — excluded |

**Blocking gaps:** **None** — mandatory blocks have T1+ partials or approved substitutes (BENEFITS for FEATURES; PAGE_IDENTITY for HERO).

---

## 22. Reuse Policy

### Allowed

- Canonical `@@include` of existing partials
- Include parameters where build discipline supports variation (e.g. search variation on catalog — not required on PROMO)
- Page wrapper classes and scoped page SCSS
- Documented composition rules for optional bands

### Forbidden

- Copying partial markup inline into page source
- Page-specific duplicate partials
- Renaming canonical blocks
- New hooks for single-scaffold convenience
- Modifying partials solely for one scaffold without separate necessity

### W3 partial reuse

| Partial | Reuse on |
|---------|----------|
| `services.html` | SERVICE_PAGE optional adjacent band only |
| `team.html` | ABOUT_PAGE recommended |
| `about.html` | ABOUT_PAGE required |

**No new block IDs** in G2-R2.

---

## 23. Composition Contract

Each page type requires:

```text
workspaces/website-factory-reference-v1/page-architecture/<PAGE-TYPE>-REFERENCE-COMPOSITION-v1.md
```

| Path | Page type |
|------|-----------|
| `SERVICE-PAGE-REFERENCE-COMPOSITION-v1.md` | SERVICE_PAGE |
| `ABOUT-PAGE-REFERENCE-COMPOSITION-v1.md` | ABOUT_PAGE |
| `CONTACT-PAGE-REFERENCE-COMPOSITION-v1.md` | CONTACT_PAGE |

**Required contents:** page identity · shell sequence · canonical blocks · scaffold-owned wrappers · required/optional/excluded sections · source provenance · runtime exclusions · coverage role · stub honesty boundary

**Naming precedent:** C5 CATEGORY · C6 PRODUCT

**Publication:** P1 wave may publish composition **before** scaffold HTML; PC accrues only at corridor completion (§10).

---

## 24. Manifest Contract

Each page type requires:

```text
workspaces/website-factory-reference-v1/page-architecture/<PAGE-TYPE>-SCAFFOLD-MANIFEST-v1.md
```

**Required contents:** page type · source path · dist path · shell requirements · included canonical blocks · scaffold-owned regions · excluded blocks · build command · validation checks · coverage eligibility · known limitations · Git evidence · stub honesty declaration

**Naming precedent:** [CATEGORY-PAGE-SCAFFOLD-MANIFEST-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/CATEGORY-PAGE-SCAFFOLD-MANIFEST-v1.md)

---

## 25. Source and SCSS Paths

| Page type | Source path | SCSS path | Composition | Manifest |
|-----------|-------------|-----------|-------------|----------|
| SERVICE_PAGE | `src/pages/service-page-reference.html` | `src/scss/pages/_service-page-reference.scss` | `SERVICE-PAGE-REFERENCE-COMPOSITION-v1.md` | `SERVICE-PAGE-SCAFFOLD-MANIFEST-v1.md` |
| ABOUT_PAGE | `src/pages/about-page-reference.html` | `src/scss/pages/_about-page-reference.scss` | `ABOUT-PAGE-REFERENCE-COMPOSITION-v1.md` | `ABOUT-PAGE-SCAFFOLD-MANIFEST-v1.md` |
| CONTACT_PAGE | `src/pages/contact-page-reference.html` | `src/scss/pages/_contact-page-reference.scss` | `CONTACT-PAGE-REFERENCE-COMPOSITION-v1.md` | `CONTACT-PAGE-SCAFFOLD-MANIFEST-v1.md |

**Dist outputs:** `dist/service-page-reference.html` · `dist/about-page-reference.html` · `dist/contact-page-reference.html`

**Not created in charter pass.**

---

## 26. JavaScript Policy

| Rule | Detail |
|------|--------|
| Default | **No new page-specific JavaScript** |
| Allowed | Reuse existing modules required by included partials (header_nav · form · faq accordion if present) |
| Forbidden | Form backend · map · tabs · carousel · modal · remote loading · router · network · analytics |

---

## 27. Accessibility Minimum

Each scaffold must satisfy:

- One H1 per page
- Valid heading hierarchy
- One MAIN landmark
- Landmark order (header → main → footer)
- Breadcrumbs semantics where included
- Form labels on LEAD_FORM fields
- Keyboard access and visible `:focus-visible`
- Logical reading order
- No duplicate IDs
- No JS-only mandatory content
- Text scaling without persistent horizontal overflow

**Not claimed:** WCAG certification

---

## 28. Responsive Minimum

Verify at: desktop · tablet · mobile · long title · long copy · missing optional media · many blocks · single optional block · form width · navigation wrapping

Use existing project breakpoint discipline — **no new global breakpoints**.

---

## 29. Implementation Waves

| Wave | Purpose | Type | Expected output |
|------|---------|------|-----------------|
| **G2-R2 P1** | PROMO Scaffold Preflight and Composition Decisions | Doc | Three composition docs (draft→published) · P1 REPORT · metrics **UNCHANGED** |
| **G2-R2 P2** | CONTACT_PAGE Scaffold | Implementation | `contact-page-reference.html` + SCSS + manifest + build PASS + REPORT; RSC **+1** if validated |
| **G2-R2 P3** | ABOUT_PAGE Scaffold | Implementation | `about-page-reference.html` + SCSS + manifest + build PASS + REPORT; RSC **+1** if validated |
| **G2-R2 P4** | SERVICE_PAGE Scaffold | Implementation | `service-page-reference.html` + SCSS + manifest + build PASS + REPORT; RSC **+1** if validated |
| **G2-R2 P5** | PROMO Exit and SC/PC Evaluation | Doc / exit | Five-dimension reconciliation · PROMO SC evaluation · PC corridor · G2-R2 exit REPORT · G2-R3 handoff |

### Wave sequencing rules

- **P1 before P2** — compositions authorize scaffold block sequences
- **P2 → P3 → P4** — dependency order (§30); max **one scaffold per implementation pass**
- **P5 after** all three scaffolds or explicit FAIL
- **Do not merge** scaffolds into one pass

### Parallelization

| Track | May parallelize |
|-------|-----------------|
| G2-R3 authority reconciliation (doc-only) | With G2-R2 P2–P4 |
| G2-R2 scaffolds | **Not** parallel — one page type per pass |

---

## 30. Dependency Order

| Order | Page type | Rationale |
|-------|-----------|-----------|
| **1st scaffold** | **CONTACT_PAGE** | Simplest required block stack; validates contact/form boundary early |
| **2nd scaffold** | **ABOUT_PAGE** | Reuses W3 ABOUT + TEAM partials; moderate complexity |
| **3rd scaffold** | **SERVICE_PAGE** | Highest semantic boundary risk (SERVICES vs detail); BENEFITS/FEATURES resolution |

**Exit dependency:** P5 requires P2 + P3 + P4 complete (or documented FAIL)

**RSC accrual:** per scaffold wave on validation — not at charter pass

**PC accrual:** P5 only — when all three compositions + scaffolds evidenced

---

## 31. RSC Accounting

| Field | Value |
|-------|-------|
| **Before G2-R2** | **3/10** global |
| **Potential deltas** | SERVICE_PAGE **+1** · ABOUT_PAGE **+1** · CONTACT_PAGE **+1** |
| **Potential maximum** | **6/10** |
| **Accrual chain** | registered page type + source HTML + composition + manifest + build PASS + structural validation + wave REPORT + Git evidence |
| **No-double-count** | Bounded host · composition-only · manifest-only · variation ≠ new RSC |
| **Charter pass** | **+0** |

---

## 32. PC Accounting

| Field | Value |
|-------|-------|
| **Coverage Model rule** | PC = published Reference Composition evidence; orthogonal to RPC |
| **G2-14 unit** | **PROMO corridor** — **`1/1 PROMO corridor`** |
| **Feeding artefacts** | Three page-type compositions |
| **Expected notation after full success** | PC **1/1 LANDING · 1/1 CATALOG corridor · 1/1 PROMO corridor** |
| **Accrual timing** | **G2-R2 P5** exit wave only — not per-scaffold |
| **Partial accrual** | **Forbidden** — corridor unit is atomic |
| **Charter pass** | **+0** · PC **UNCHANGED** |

---

## 33. PROMO SC Contract

| Criterion | Required evidence | G2-R2 responsibility |
| --------- | ----------------- | ---------------------- |
| W3 multi-page blocks | SERVICES · TEAM · ABOUT T1+ (G2-R1) | **Input satisfied** — not re-built |
| PROCESS block | `process.html` T1+ | **Input satisfied** — include where mapping allows |
| SERVICE_PAGE scaffold | Buildable reference page + manifest | **G2-R2 P4** |
| ABOUT_PAGE scaffold | Buildable reference page + manifest | **G2-R2 P3** |
| CONTACT_PAGE scaffold | Buildable reference page + manifest | **G2-R2 P2** |
| Compositions | Three PUBLISHED composition docs | **P1 + per-scaffold sync** |
| Manifests | Three PUBLISHED manifest docs | **P2–P4** |
| HEADER_NAV full shell | T1+ partial | **Reuse** — satisfied |
| PROMO PC | 1/1 PROMO corridor | **P5** evaluation |
| Build evidence | npm run build PASS | **Each scaffold wave** |
| Formal exit evaluation | G2-R2 P5 REPORT | **P5** — not charter |

**PROMO SC PASS** declared only in **P5** — **not** at charter acceptance.

---

## 34. Exit Criteria

G2-R2 **COMPLETE** only when **all** true:

| Criterion | Required state |
|-----------|----------------|
| SERVICE_PAGE scaffold | Complete · validated |
| ABOUT_PAGE scaffold | Complete · validated |
| CONTACT_PAGE scaffold | Complete · validated |
| Compositions | All three **PUBLISHED** |
| Manifests | All three **PUBLISHED** |
| Builds | All PASS |
| Structural validations | All PASS |
| RSC | Reconciled in P5 REPORT (potential **6/10**) |
| PC | PROMO corridor evaluated in P5 |
| PROMO SC | Evaluated in P5 (PASS or honest OPEN) |
| G2 impact | Documented — G2 still **NOT CLOSED** |
| Exit REPORT | Published |
| G2-R3 readiness | Evaluated |

---

## 35. G2 Handoff

**Successor:** **G2-R3 — SEARCH_RESULTS_PAGE Authority Reconciliation**

### Handoff payload (from G2-R2 P5)

| Item | Destination |
|------|-------------|
| PROMO scaffold evidence | G2-R5 evidence assembly |
| PROMO composition evidence | G2-14 closure check |
| RSC / PC / PROMO SC snapshot | Formal gate evaluation |
| Remaining CATALOG blocker | G2-R4 |
| G2-11 SEARCH_RESULTS_PAGE gap | **G2-R3** |

G2-R2 **does not** execute G2-R3.

---

## 36. Known Debt and SAFE UNKNOWN

| Item | Status |
|------|--------|
| Operator browser QA (W3-C/W3-D) | **Non-blocking** — deferred from G2-R1 |
| FEATURES partial absent | **Resolved** — use BENEFITS on SERVICE_PAGE |
| MAP block absent | **By design** — excluded from CONTACT scaffold |
| PC partial accrual semantics | **Resolved** — atomic PROMO corridor at P5 |
| Triumph v6 as scaffold source | **Rejected** — PPC-only; use reference partials |
| Named steward | **SAFE UNKNOWN** — named steward not assigned |
| CONDITIONAL PASS for G2 | **SAFE UNKNOWN** — formal authority decision required per G2 charter |

---

## 37. Evidence Paths

```text
projects/mars-website-factory/wf-r01-3-g2-r2-promo-money-page-scaffold-completion-charter-v1.md
reports/wf-r01-3-g2-r2-promo-money-page-scaffold-charter-pass-v1.md
projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md
reports/wf-r01-3-g2-r1-w3-e-exit-g2-r2-readiness-v1.md
projects/mars-website-factory/wf-r01-3-g2-r1-w3-promo-reference-completion-charter-v1.md
projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md
projects/mars-website-factory/page-type-shell-matrix-v1.md
projects/mars-website-factory/reference-scaffold-contract-v1.md
workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md
workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md
workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md
workspaces/website-factory-reference-v1/page-architecture/CATEGORY-PAGE-REFERENCE-COMPOSITION-v1.md
workspaces/website-factory-reference-v1/page-architecture/CATEGORY-PAGE-SCAFFOLD-MANIFEST-v1.md
projects/mars-website-factory/roadmap.md
projects/mars-website-factory/OPERATIONAL-INDEX.md
```

---

## 38. Decision

**Decision:** **ACCEPTED** — WF-R01.3 G2-R2 PROMO Money-Page Scaffold Completion Charter v1 is normative operator authority for G2-R2 remediation execution waves.

**Package state after decision:**

```text
CHARTERED
NOT IMPLEMENTED
NOT COMPLETE
```

**First implementation task (binding):**

```text
WF-R01.3 G2-R2 P1 — PROMO Scaffold Preflight and Composition Decisions
```

**Charter acceptance is not implementation authorization for P2–P5** — each wave executes under this charter with wave-specific REPORT evidence.
