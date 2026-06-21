# WF-R01.3 G2-R2 PROMO Scaffold Preflight and Composition Decisions v1

**Package ID:** G2-R2 P1  
**Parent charter:** [wf-r01-3-g2-r2-promo-money-page-scaffold-completion-charter-v1.md](wf-r01-3-g2-r2-promo-money-page-scaffold-completion-charter-v1.md)  
**Date:** 2026-06-21  
**Mode:** documentation-only · preflight-only · composition-decision-only · implementation-authorization-only

**Honesty boundary:** This document **authorizes composition decisions and P2 gate only**. **Not** scaffold HTML. **Not** composition/manifest publication. **Not** RSC/PC accrual. **Not** PROMO SC PASS. **Not** G2 evaluation.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED** |
| **Preflight state** | **COMPLETE** |
| **Implementation state** | **NOT STARTED** |
| **Coverage impact** | **None** — RC/RPC/RSC/SC/PC frozen at P1 snapshot |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Artefact ID** | WF-R01.3 G2-R2 P1 — PROMO Scaffold Preflight and Composition Decisions v1 |
| **Canonical path** | `projects/mars-website-factory/wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md` |
| **Report** | [reports/wf-r01-3-g2-r2-p1-promo-scaffold-preflight-v1.md](../reports/wf-r01-3-g2-r2-p1-promo-scaffold-preflight-v1.md) |
| **Page types in scope** | `CONTACT_PAGE` · `ABOUT_PAGE` · `SERVICE_PAGE` |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| G2-R2 charter | `projects/mars-website-factory/wf-r01-3-g2-r2-promo-money-page-scaffold-completion-charter-v1.md` | Wave contract; PROMO corridor |
| G2-R2 charter pass | `reports/wf-r01-3-g2-r2-promo-money-page-scaffold-charter-pass-v1.md` | Charter acceptance evidence |
| G2 formal gate charter | `projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md` | Parent gate G2-10/12/14 |
| Coverage Model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | RSC/SC/PC rules |
| Vocabulary Canon | `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` | F3 block family |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Shell order |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | REQ/POL/N/A per type |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | RSC accrual chain |
| Page-Type Registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` | Registered page types |
| Block Registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | 32 `block_id` SSOT |
| Core Block Library | `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md` | Partial paths |
| Page-Block Mapping | `workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md` | REQUIRED/OPTIONAL/FORBIDDEN |
| C5/C6 precedent | `workspaces/website-factory-reference-v1/page-architecture/CATEGORY-PAGE-*` · `PRODUCT-PAGE-*` | Composition/manifest pattern |

**Hierarchy for composition conflicts:** PAGE-TYPE-REGISTRY + PAGE-BLOCK-MAPPING **>** Page-Type Shell Matrix **>** G2-R2 charter handoff notes.

---

## 4. Scope

### In scope

- Final preflight for three PROMO money-page scaffolds
- Canonical partial inventory and ID audit
- Per-page shell, block, scaffold-owned region, and composition decisions
- Fictional-content and form runtime boundary
- Page-level SCSS boundary policy
- Future composition/manifest/scaffold path plans
- P2 authorization; P3/P4 readiness (not authorization)
- RSC/PC/PROMO SC accounting lock

### Out of scope (binding)

- Scaffold HTML, page SCSS, composition docs, manifest docs
- Partial or Registry mutation
- RSC/PC accrual; PROMO SC evaluation
- P2–P5 implementation

---

## 5. Duplicate Check

| Search term | Result |
|-------------|--------|
| `g2-r2-p1` | **None** |
| `promo-scaffold-preflight` | **None** (this artefact is first) |
| `promo-composition-decisions` | **None** |
| `contact-page-composition` | **None** |
| `about-page-composition` | **None** |
| `service-page-composition` | **None** |

| Classification | Artefacts |
|----------------|-----------|
| **ACCEPTED PREFLIGHT** | **None** — no STOP |
| **COMPOSITION / MANIFEST / SCAFFOLD** | **None** for three PROMO page types |
| **COMPLEMENTARY** | C5 CATEGORY · C6 PRODUCT compositions/manifests/scaffolds |
| **LEGACY** | W3 bounded host `promo-block-references.html` — not RSC/PC evidence |

**Decision:** Proceed — no competing accepted P1 preflight; no reconciliation required for existing PROMO composition/manifest.

---

## 6. Page-Type Reconfirmation

| Page type | Registry row | Shell row | Block mapping | Scaffold state | RSC eligible |
|-----------|--------------|-----------|---------------|----------------|--------------|
| **CONTACT_PAGE** | **Yes** — PAGE-TYPE-REGISTRY § CONTACT_PAGE; allowed `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE` | **Yes** — Shell Matrix §6: HEADER_NAV REQ · MAIN REQ · BREADCRUMBS POL · FOOTER REQ · LEGAL_LINKS REQ · SEARCH/FILTERS/PAGINATION N/A | **Yes** — PAGE-BLOCK-MAPPING § CONTACT_PAGE | **None** — no `contact-page-reference.html` | **Yes** — when full RSC chain complete |
| **ABOUT_PAGE** | **Yes** — PAGE-TYPE-REGISTRY § ABOUT_PAGE; allowed `PROMO`, `CORPORATE` | **Yes** — Shell Matrix §6: HEADER_NAV REQ · MAIN REQ · BREADCRUMBS REQ · FOOTER REQ · LEGAL_LINKS REQ · SEARCH/FILTERS/PAGINATION N/A | **Yes** — PAGE-BLOCK-MAPPING § ABOUT_PAGE | **None** — no `about-page-reference.html` | **Yes** |
| **SERVICE_PAGE** | **Yes** — PAGE-TYPE-REGISTRY § SERVICE_PAGE; allowed `PROMO`, `CORPORATE` | **Yes** — Shell Matrix §6: HEADER_NAV REQ · MAIN REQ · BREADCRUMBS POL · FOOTER REQ · LEGAL_LINKS REQ · SEARCH/FILTERS/PAGINATION N/A | **Yes** — PAGE-BLOCK-MAPPING § SERVICE_PAGE | **None** — no `service-page-reference.html` | **Yes** |

**Preflight result:** **SCAFFOLD ELIGIBLE** — all three registered; no Registry reconciliation required.

---

## 7. Canonical Partial Inventory

| Block | Canonical path | Registry state | Reference state | Parameters | JS dependency | Readiness |
|-------|----------------|----------------|-----------------|------------|---------------|-----------|
| **HEADER_NAV** | `src/partials/layout/header.html` → `src/partials/sections/header-nav.html` | Tier A F3 | T1+ | **None** — bare `@@include` | `js/sections/header_nav.js` via lifecycle | **READY** |
| **BREADCRUMBS** | `src/partials/components/breadcrumbs.html` | Tier B layout-component | T1+ | **None** observed | **None** | **READY** |
| **BENEFITS** | `src/partials/sections/benefits.html` | F3 | T1+ | **None** | **None** | **READY** |
| **FAQ** | `src/partials/sections/faq.html` | F3 | T1+ | **None** | **None** — native `<details>` | **READY** |
| **LEAD_FORM** | `src/partials/sections/lead_form.html` | F3 | T1+ | **None** | `js/core/form.js` — mock submit when no endpoint | **READY WITH CONSTRAINTS** |
| **CTA** | `src/partials/sections/cta_band.html` | F3 | T1+ | **None** | **None** | **READY** |
| **SERVICES** | `src/partials/components/services.html` | F3 | PARTIAL / T1+ (W3-B) | **None** | **None** | **READY WITH CONSTRAINTS** — adjacent role only |
| **PROCESS** | `src/partials/sections/process.html` | F3 | T1+ | **None** | **None** | **READY** |
| **ABOUT** | `src/partials/components/about.html` | F3 | PARTIAL / T1+ (W3-D) | **None** | **None** | **READY WITH CONSTRAINTS** |
| **TEAM** | `src/partials/components/team.html` | F3 | PARTIAL / T1+ (W3-C) | **None** | **None** | **READY WITH CONSTRAINTS** |
| **TRUST** | `src/partials/sections/trust.html` | F3 | T1+ (narrowed) | **None** | **None** | **READY** |
| **CONTACTS** | `src/partials/sections/contact_block.html` | F3 | T1+ | **None** | **None** | **READY WITH CONSTRAINTS** — see §21 map anchor |
| **FOOTER** | `src/partials/sections/footer.html` | Tier A F3 | T1+ | **None** | **None** | **READY** |
| **LEGAL_LINKS** | nested in FOOTER → `src/partials/components/legal-links.html` | Tier A F3 | T1+ | **None** | **None** | **READY** |
| **FEATURES** | — | F3 row | **Not implemented** | — | — | **MISSING** — satisfied by BENEFITS on SERVICE_PAGE |
| **MAP** | — | F3 row | **Not implemented** | — | — | **N/A** — excluded from CONTACT scaffold |
| **HERO** | `src/partials/sections/hero.html` | F3 | T1+ | **None** | varies | **READY WITH CONSTRAINTS** — compact PAGE_IDENTITY substitute permitted |

**Include convention:** bare `@@include('../partials/...')` unless future wave documents parameters (catalog SEARCH/FILTERS precedent not required on PROMO scaffolds).

---

## 8. Include Parameter and ID Audit

| Partial | Hardcoded IDs / anchors | Parameters available | Multi-page reuse risk | Decision |
|---------|-------------------------|----------------------|----------------------|----------|
| **header-nav.html** | `#wf-header-nav-menu` | None | Low — one header per document | **Reuse as-is** |
| **breadcrumbs.html** | None — `aria-label` only | None | Low | **Reuse as-is** |
| **benefits.html** | `#benefits-title` | None | Low — unique suffix per block | **Reuse as-is** |
| **faq.html** | `#faq-title`; `<details>` without duplicate IDs | None | Low | **Reuse as-is** |
| **lead_form.html** | `#lead-form`, `#lead-name`, `#lead-phone`, `#lead-name-error`, `#lead-phone-error`, `#lead-phone-help` | None | **Medium** — duplicate IDs if **two** LEAD_FORM on same page | **One LEAD_FORM max per scaffold** — no blocking issue for approved compositions |
| **cta_band.html** | No heading ID | None | Low | **Reuse as-is** |
| **process.html** | `#process-title` | None | Low | **Reuse as-is** |
| **about.html** | `#about-title` | None | Low | **Reuse as-is** |
| **team.html** | `#team-title` | None | Low | **Reuse as-is** |
| **trust.html** | `#trust-title` | None | Low | **Reuse as-is** |
| **services.html** | `#services-title` | None | Low | **Reuse as-is** |
| **contact_block.html** | `#contact`, `#contact-title` | None | Low — one CONTACTS per page | **Reuse as-is**; map anchor external link — see §21 |
| **footer.html** | `#footer-nav-primary-title`, `#footer-nav-secondary-title`, `#footer-contacts-title` | None | Low — one footer per document | **Reuse as-is** |
| **legal-links.html** | None | None | Low | **Reuse as-is** |

**Parameter convention:** PROMO scaffolds use **parameterless** includes unless a future narrow partial-variation task authorizes IDs (not in G2-R2 scope).

**Blocking duplicate-ID problem:** **None** for approved single-instance block stacks.

**Scaffold variation without partial edit:** Page root classes (`wf-contact-page`, etc.) and page SCSS only.

---

## 9. CONTACT_PAGE Shell Decision

**Shell Matrix row (binding):**

| Surface | Code |
|---------|------|
| HEADER_NAV | **REQ** |
| MAIN | **REQ** |
| BREADCRUMBS | **POL** |
| PAGINATION | **N/A** |
| FOOTER | **REQ** |
| LEGAL_LINKS | **REQ** (nested in FOOTER) |
| SEARCH / FILTERS | **N/A** |

**BREADCRUMBS decision:** **INCLUDED** — aligns with C5/C6 internal-page structural pattern; POL does not forbid inclusion; shallow fictional trail supports orientation without implying mandatory production IA.

**Final shell:**

```text
HEADER_NAV → MAIN → FOOTER → LEGAL_LINKS (nested)
```

---

## 10. CONTACT_PAGE Block Decision

| Block / region | Authority state | Decision | Role |
|----------------|-----------------|----------|------|
| HEADER_NAV | REQUIRED | **Required** | Global shell |
| BREADCRUMBS | Tier B; shell POL | **Included** | Shallow trail |
| HERO | OPTIONAL | **Excluded** — use PAGE_IDENTITY | Compact header substitute |
| PAGE_IDENTITY | Scaffold-owned | **Required** | H1 + neutral lead |
| CONTACTS | REQUIRED | **Required** | NAP hub |
| LEAD_FORM | OPTIONAL | **Included (recommended)** | Presentation-only conversion |
| TRUST | Not listed | **Excluded** | Not required; keeps page focused |
| FAQ | Not listed | **Excluded** | Not required |
| CTA | Not primary | **Excluded** | Avoid duplicate conversion surface |
| MAP block | OPTIONAL block; not implemented | **Excluded** | No embed/API |
| CONTACT CONTEXT wrapper | Scaffold policy | **Not required** | CONTACTS + PAGE_IDENTITY sufficient |
| Commerce / catalog blocks | FORBIDDEN | **Excluded** | |

---

## 11. CONTACT_PAGE Scaffold-Owned Regions

| Region | Required | Content | Hook | Why not Registry block |
|--------|----------|---------|------|------------------------|
| **PAGE_IDENTITY** | **Yes** | One H1; short neutral lead | Page BEM (e.g. `wf-contact-page__identity`); **no** `data-block-id` | Substitutes optional HERO; C5 precedent |
| **main-inner wrapper** | **Yes** | Container + section rhythm | `<main class="wf-contact-page">` + inner `wf-container` | Layout only |
| **CONTACT CONTEXT** | **No** | — | — | CONTACTS partial owns contact copy |

---

## 12. CONTACT_PAGE Composition Decision

**Approved sequence:**

```text
HEADER_NAV

MAIN
├── BREADCRUMBS
├── scaffold-owned PAGE_IDENTITY
├── CONTACTS
└── LEAD_FORM

FOOTER
└── LEGAL_LINKS
```

| Category | Members |
|----------|---------|
| **Required blocks** | HEADER_NAV · CONTACTS · FOOTER · LEGAL_LINKS |
| **Included (recommended / POL)** | BREADCRUMBS · LEAD_FORM · PAGE_IDENTITY |
| **Optional (declined in v1 reference)** | TRUST · FAQ · HERO |
| **Excluded** | MAP · CTA · catalog/commerce · CONTACT CONTEXT wrapper |
| **Runtime** | No backend · no map embed · form mock-only |
| **Coverage role** | Feeds PROMO corridor composition; RSC on P2 completion only |

**Decision:** **CONTACT_PAGE COMPOSITION APPROVED FOR P2**

---

## 13. ABOUT_PAGE Shell Decision

**Shell Matrix row:**

| Surface | Code |
|---------|------|
| HEADER_NAV | **REQ** |
| MAIN | **REQ** |
| BREADCRUMBS | **REQ** |
| PAGINATION | **N/A** |
| FOOTER | **REQ** |
| LEGAL_LINKS | **REQ** |
| SEARCH / FILTERS | **N/A** |

**BREADCRUMBS decision:** **INCLUDED** — **REQ** per matrix; mandatory on ABOUT reference scaffold.

---

## 14. ABOUT_PAGE Block Decision

| Block | Mapping stance | Decision | Rationale |
|-------|----------------|----------|-----------|
| ABOUT | REQUIRED | **Required** | Primary narrative owner |
| TEAM | OPTIONAL | **Included** | Differentiates page composition from W3 bounded host |
| PROCESS | **FORBIDDEN** (summary matrix) | **Excluded** | Mapping authority overrides charter optional note |
| TRUST | OPTIONAL | **Included** | Lightweight proof; mapping allows |
| BENEFITS | OPTIONAL | **Excluded** | Not narrative-appropriate |
| CTA | OPTIONAL | **Excluded** | Avoid landing-style aggressiveness |
| LEAD_FORM | FORBIDDEN (primary) | **Excluded** | Mapping stance |
| SERVICES | FORBIDDEN on ABOUT | **Excluded** | No bounded-host stack |
| HERO | REQUIRED | **Excluded** — PAGE_IDENTITY substitute | C5/C6 compact policy |
| CASES / CERTIFICATES / PARTNERS | OPTIONAL | **Excluded** | No partial requirement for honest v1 reference |

**Narrative flow:** PAGE_IDENTITY → ABOUT → TEAM → TRUST

---

## 15. ABOUT_PAGE Composition Decision

**Approved sequence:**

```text
HEADER_NAV

MAIN
├── BREADCRUMBS
├── scaffold-owned PAGE_IDENTITY
├── ABOUT
├── TEAM
└── TRUST

FOOTER
└── LEGAL_LINKS
```

| Category | Members |
|----------|---------|
| **Required blocks** | HEADER_NAV · ABOUT · BREADCRUMBS · FOOTER · LEGAL_LINKS |
| **Included optional** | TEAM · TRUST |
| **Scaffold-owned** | PAGE_IDENTITY · main-inner wrapper |
| **Excluded** | PROCESS · LEAD_FORM · CTA · BENEFITS · SERVICES · commerce |

**Decision:** **ABOUT_PAGE COMPOSITION APPROVED** — **READY WITH CONSTRAINTS** (W3 PARTIAL partials; PROCESS excluded per mapping vs charter note)

---

## 16. SERVICE_PAGE Shell Decision

**Shell Matrix row:**

| Surface | Code |
|---------|------|
| HEADER_NAV | **REQ** |
| MAIN | **REQ** |
| BREADCRUMBS | **POL** |
| PAGINATION | **N/A** |
| FOOTER | **REQ** |
| LEGAL_LINKS | **REQ** |
| SEARCH / FILTERS | **N/A** |

**BREADCRUMBS decision:** **INCLUDED** — recommended parent hub link per POL notes.

---

## 17. SERVICE_PAGE Block Decision

| Block / region | Mapping / charter | Decision |
|----------------|-------------------|----------|
| PAGE_IDENTITY | Scaffold-owned; HERO substitute | **Required** |
| SERVICE_DETAIL_CONTEXT | Scaffold-owned; no Registry block | **Required** |
| BENEFITS | REQUIRED (or FEATURES) | **Required** — use BENEFITS |
| FEATURES | Not implemented | **Excluded** |
| FAQ | REQUIRED | **Required** |
| LEAD_FORM | REQUIRED | **Required** |
| CTA | REQUIRED | **Required** |
| PROCESS | OPTIONAL | **Included** — proof stack |
| TRUST | OPTIONAL | **Excluded** — keep stack bounded |
| SERVICES | Not on SERVICE_PAGE mapping; summary FORB | **Excluded** — see §19 |
| CASES | OPTIONAL | **Excluded** |
| Catalog/commerce | FORBIDDEN | **Excluded** |

**Approved sequence:**

```text
HEADER_NAV

MAIN
├── BREADCRUMBS
├── scaffold-owned PAGE_IDENTITY
├── scaffold-owned SERVICE_DETAIL_CONTEXT
├── BENEFITS
├── PROCESS
├── FAQ
├── CTA
└── LEAD_FORM

FOOTER
└── LEGAL_LINKS
```

**Decision:** **SERVICE_PAGE COMPOSITION APPROVED** — **READY WITH CONSTRAINTS**

---

## 18. SERVICE Detail Context Contract

| Field | Policy |
|-------|--------|
| **Ownership** | Scaffold-owned region inside SERVICE_PAGE reference only |
| **Allowed content** | Short service overview; 2–3 neutral paragraphs; one semantic subheading (h2/h3); optional neutral bullet list |
| **Forbidden content** | `data-block-id` · new Registry identity · pricing · calculator · embedded LEAD_FORM/FAQ/BENEFITS/PROCESS · related-services grid · workflow steps duplicating PROCESS |
| **Hook policy** | Page-scoped BEM wrapper (e.g. `wf-service-page__detail`); **no** `data-block-id` |
| **Coverage** | **No RPC** · **no RSC delta beyond page scaffold** · not a hidden `SERVICE_DESCRIPTION` block |

---

## 19. SERVICES Relationship Decision

**Decision:** **Option A — Excluded from first SERVICE_PAGE scaffold**

| Field | Value |
|-------|-------|
| **Included** | **No** |
| **Role if ever added** | Adjacent service directions only — post-detail navigation |
| **Placement** | After primary detail + required conversion stack |
| **Rationale** | Clear single-service focus; avoids collection/detail semantic conflict; mapping does not require SERVICES on SERVICE_PAGE; simpler P4 reference |

P4 may revisit Option B only via explicit composition amendment — **not** default for v1.

---

## 20. Partial Readiness

| Page type | Required partials ready | Constraints | Blocking gaps | Final readiness |
|-----------|-------------------------|-------------|---------------|-----------------|
| **CONTACT_PAGE** | HEADER_NAV · BREADCRUMBS · CONTACTS · LEAD_FORM · FOOTER · LEGAL_LINKS | CONTACTS partial contains external map **link** (not MAP block); fictional NAP in page meta vs partial demo tel | **None** | **READY** |
| **ABOUT_PAGE** | HEADER_NAV · BREADCRUMBS · ABOUT · TEAM · FOOTER · LEGAL_LINKS | ABOUT/TEAM PARTIAL/T1+; TRUST narrowed reference | **None** | **READY WITH CONSTRAINTS** |
| **SERVICE_PAGE** | HEADER_NAV · BREADCRUMBS · BENEFITS · PROCESS · FAQ · CTA · LEAD_FORM · FOOTER · LEGAL_LINKS | SERVICE_DETAIL_CONTEXT is scaffold-owned; FEATURES absent | **None** | **READY WITH CONSTRAINTS** |

---

## 21. Fictional Content Policy

All three scaffolds **must** use:

| Element | Policy |
|---------|--------|
| Organisation | Fictional name (e.g. "Example Organisation Ltd.") |
| Phone | Reserved format — e.g. `+1 555 010 0200` or `tel:+15550100200` |
| Email | `@example.com` — e.g. `hello@example.com` |
| Address | Fictional — e.g. `100 Example Street, Demo City` |
| Hours | Neutral demo hours |
| H1 / leads | Neutral reference copy |
| Form copy | Neutral; no production claims |
| Action links | `href="#"` unless partial already uses safe demo URLs |
| Meta | `robots noindex, nofollow` on reference pages |

**Forbidden:** real client names · real contacts · real addresses · production URLs · commercial guarantees · live form endpoints

**CONTACTS partial note:** Canonical `contact_block.html` ships demo `tel:+15551234567`, `hello@example.com`, and external map anchor to `https://maps.google.com/`. G2-R2 **does not** mutate partials. P2–P4 **accept canonical partial** as presentation reference; **MAP block/embed remains excluded**; external map **link** in partial is **known constraint** — not MAP block RPC.

---

## 22. Form and Runtime Decision

**LEAD_FORM runtime audit (`js/core/form.js`):**

| Check | Result |
|-------|--------|
| Default endpoint | `SUBMIT_ENDPOINT = null` |
| Submit path without endpoint | **`mockSubmit`** — local timeout; **no network** |
| Network path | Only when `data-form-endpoint` or non-`#` `action` set — **not** set on canonical partial |
| Validation | HTML5 + local field errors only |

**Decision:** **Reuse allowed** — presentation-only mock submit satisfies G2-R2 runtime boundary.

| Page type | Form include | Network | Decision |
|-----------|--------------|---------|----------|
| CONTACT_PAGE | LEAD_FORM once | **No** (mock) | **Approved** |
| ABOUT_PAGE | None | N/A | **N/A** |
| SERVICE_PAGE | LEAD_FORM once | **No** (mock) | **Approved** |

**Map / backend:** No map embed · no backend form · no CRM · no analytics in G2-R2 scaffolds.

---

## 23. Page-Level SCSS Boundaries

### CONTACT_PAGE

**Allowed:** page identity spacing; CONTACTS ↔ LEAD_FORM layout relationship; section rhythm; responsive stacking.

**Forbidden:** overriding canonical block internals; global resets; new design system; new global breakpoints; hiding required content.

### ABOUT_PAGE

**Allowed:** page identity spacing; ABOUT/TEAM/TRUST ordering rhythm; inter-block relationships.

**Forbidden:** same as above.

### SERVICE_PAGE

**Allowed:** page identity; service-detail-context typography/spacing; block sequence rhythm; BENEFITS/PROCESS/FAQ/CTA/LEAD_FORM relationships.

**Forbidden:** same as above; do not restyle PROCESS as service workflow replacement for SERVICE_DETAIL_CONTEXT.

---

## 24. Composition Document Plan

| Page type | Future path | P1 state |
|-----------|-------------|----------|
| CONTACT_PAGE | `workspaces/website-factory-reference-v1/page-architecture/CONTACT-PAGE-REFERENCE-COMPOSITION-v1.md` | **Planned — not created** |
| ABOUT_PAGE | `workspaces/website-factory-reference-v1/page-architecture/ABOUT-PAGE-REFERENCE-COMPOSITION-v1.md` | **Planned — not created** |
| SERVICE_PAGE | `workspaces/website-factory-reference-v1/page-architecture/SERVICE-PAGE-REFERENCE-COMPOSITION-v1.md` | **Planned — not created** |

**Future section structure (all three):** Status · Identity · Authority · Purpose · Shell · Block Sequence · Scaffold-Owned Regions · Required/Optional/Excluded Blocks · Content Policy · Runtime Boundary · Responsive Notes · Accessibility Notes · Coverage Role · Evidence Paths · Decision

**Publication timing:** P2 publishes CONTACT composition with scaffold; P3 ABOUT; P4 SERVICE — per G2-R2 charter waves.

---

## 25. Manifest Plan

| Page type | Future path | P1 state |
|-----------|-------------|----------|
| CONTACT_PAGE | `workspaces/website-factory-reference-v1/page-architecture/CONTACT-PAGE-SCAFFOLD-MANIFEST-v1.md` | **Planned — not created** |
| ABOUT_PAGE | `workspaces/website-factory-reference-v1/page-architecture/ABOUT-PAGE-SCAFFOLD-MANIFEST-v1.md` | **Planned — not created** |
| SERVICE_PAGE | `workspaces/website-factory-reference-v1/page-architecture/SERVICE-PAGE-SCAFFOLD-MANIFEST-v1.md` | **Planned — not created** |

**Manifest contents (future):** registered page type · source/dist paths · SCSS path · shell requirements · canonical includes · scaffold-owned regions · excluded blocks · build command · structural checks · coverage eligibility · limitations · Git evidence

---

## 26. Implementation Paths

| Page type | Source HTML | SCSS | Availability |
|-----------|-------------|------|--------------|
| CONTACT_PAGE | `src/pages/contact-page-reference.html` | `src/scss/pages/_contact-page-reference.scss` | **Free** — no competing files |
| ABOUT_PAGE | `src/pages/about-page-reference.html` | `src/scss/pages/_about-page-reference.scss` | **Free** |
| SERVICE_PAGE | `src/pages/service-page-reference.html` | `src/scss/pages/_service-page-reference.scss` | **Free** |

**Dist outputs (future):** `dist/contact-page-reference.html` · `dist/about-page-reference.html` · `dist/service-page-reference.html`

**SCSS import:** connect in `src/scss/style.scss` at implementation wave — not in P1.

---

## 27. Build and JavaScript Decision

| Policy | Detail |
|--------|--------|
| Build | Gulp multi-page — `npm run build` in reference workspace |
| dist | **Never** edited manually |
| New page JS | **Forbidden** by default |
| Reused JS | `lifecycle.js` · `form.js` · `header_nav.js` as required by included partials |
| Network | **Forbidden** in G2-R2 scaffolds |
| Map | **Forbidden** (embed/API) |

| Page type | Existing JS reused | New JS | Network | Decision |
|-----------|-------------------|--------|---------|----------|
| CONTACT_PAGE | lifecycle · form · header_nav | **None** | **No** | **Approved** |
| ABOUT_PAGE | lifecycle · header_nav | **None** | **No** | **Approved** |
| SERVICE_PAGE | lifecycle · form · header_nav | **None** | **No** | **Approved** |

---

## 28. RSC Accounting

| Field | Value |
|-------|-------|
| **Before G2-R2** | **RSC = 3/10** global |
| **P1 delta** | **0** |
| **P2 potential** | +1 CONTACT_PAGE if full chain |
| **P3 potential** | +1 ABOUT_PAGE |
| **P4 potential** | +1 SERVICE_PAGE |
| **Maximum after G2-R2** | **6/10** |

Accrual requires: source HTML · page SCSS · composition · manifest · build PASS · structural validation · wave REPORT · Git evidence.

---

## 29. PC Accounting

| Field | Value |
|-------|-------|
| **Unit** | **1/1 PROMO corridor** (atomic) |
| **Feeding artefacts** | Three page-type Reference Compositions |
| **P1 accrual** | **0** |
| **P2–P4 accrual** | **0** — corridor not partial |
| **P5 accrual** | Evaluate when all three compositions + scaffolds evidenced |

**Forbidden notation:** `1/3 PROMO` · `2/3 PROMO` · per-page PC units

---

## 30. PROMO SC Boundary

**PROMO SC = NOT PASSED** until P5 formal evaluation.

**P5 criteria inputs:**

- W3 multi-page blocks (SERVICES · TEAM · ABOUT) — **satisfied** (G2-R1)
- Three PROMO scaffolds + compositions + manifests
- RSC reconciled · PROMO PC accrued
- Build evidence · P5 REPORT

P1–P4 **do not** evaluate or pass PROMO SC.

---

## 31. P2 Authorization

| Gate | State |
|------|-------|
| CONTACT_PAGE registered | **Pass** |
| Shell decision final | **Pass** |
| Block sequence final | **Pass** |
| CONTACTS ready | **Pass** (with map-link constraint) |
| LEAD_FORM ready | **Pass** — mock runtime |
| Fictional contact policy final | **Pass** |
| Form runtime safe | **Pass** |
| Canonical paths free | **Pass** |
| Composition/manifest plan final | **Pass** |
| No new Registry identity | **Pass** |

**Decision:** **P2 CONTACT_PAGE IMPLEMENTATION AUTHORIZED**

P2 scope: `contact-page-reference.html` · `_contact-page-reference.scss` · CONTACT-PAGE composition · CONTACT-PAGE manifest · build PASS · P2 REPORT · selective Git commit.

---

## 32. P3 and P4 Readiness

### P3 ABOUT_PAGE

| Field | Value |
|-------|-------|
| **State** | **READY WITH CONSTRAINTS** |
| **Constraints** | W3 PARTIAL ABOUT/TEAM; PROCESS excluded per mapping; TRUST narrowed reference |
| **Authorization** | **Not granted by P1** — requires P3 wave charter execution after P2 complete |

### P4 SERVICE_PAGE

| Field | Value |
|-------|-------|
| **State** | **READY WITH CONSTRAINTS** |
| **Constraints** | SERVICE_DETAIL_CONTEXT scaffold-owned; SERVICES excluded; FEATURES gap covered by BENEFITS; highest semantic boundary risk |
| **Authorization** | **Not granted by P1** — requires P4 wave after P3 |

---

## 33. Known Risks and SAFE UNKNOWN

| Item | Status |
|------|--------|
| CONTACTS map external link in partial | **Constraint** — accept canonical partial; not MAP block |
| Charter PROCESS on ABOUT vs mapping FORB | **Resolved** — mapping wins; PROCESS excluded |
| Operator browser QA (G2-R1 debt) | **Non-blocking** — deferred |
| Named steward | **SAFE UNKNOWN** |
| G2 CONDITIONAL PASS authority | **SAFE UNKNOWN** — formal evaluation only |

---

## 34. Evidence Paths

```text
projects/mars-website-factory/wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md
reports/wf-r01-3-g2-r2-p1-promo-scaffold-preflight-v1.md
projects/mars-website-factory/wf-r01-3-g2-r2-promo-money-page-scaffold-completion-charter-v1.md
reports/wf-r01-3-g2-r2-promo-money-page-scaffold-charter-pass-v1.md
projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md
projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md
projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md
projects/mars-website-factory/global-shell-contract-v1.md
projects/mars-website-factory/page-type-shell-matrix-v1.md
projects/mars-website-factory/reference-scaffold-contract-v1.md
workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md
workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md
workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md
workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md
workspaces/website-factory-reference-v1/page-architecture/CATEGORY-PAGE-REFERENCE-COMPOSITION-v1.md
workspaces/website-factory-reference-v1/page-architecture/CATEGORY-PAGE-SCAFFOLD-MANIFEST-v1.md
workspaces/website-factory-reference-v1/src/pages/category-page-reference.html
workspaces/website-factory-reference-v1/src/js/core/form.js
workspaces/website-factory-reference-v1/src/partials/sections/contact_block.html
workspaces/website-factory-reference-v1/src/partials/sections/lead_form.html
projects/mars-website-factory/roadmap.md
projects/mars-website-factory/OPERATIONAL-INDEX.md
```

---

## 35. Decision

**Decision:** **PUBLISHED** — G2-R2 P1 preflight complete; composition decisions fixed for three PROMO money-page types; **P2 CONTACT_PAGE IMPLEMENTATION AUTHORIZED**; P3/P4 readiness declared; coverage **UNCHANGED**; implementation **NOT STARTED**.

**Next task:** **WF-R01.3 G2-R2 P2 — CONTACT_PAGE Scaffold** (execute only under P2 wave — not part of P1).
