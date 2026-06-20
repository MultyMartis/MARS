# WF-R01.3 G2-R1 W3 PROMO Source Inventory v1

**Remediation package:** G2-R1 — W3 PROMO Reference Completion  
**Wave:** W3-A — Source Inventory and Contract Confirmation  
**Parent gate:** G2 — PROMO + CATALOG scaffold  
**Version:** v1  
**Date:** 2026-06-20  
**Status:** **PUBLISHED**

**Honesty boundary:** Documentation and source-selection authority only. **Not** implementation. **Not** RPC/RSC/SC/PC accrual. **Not** G2 evaluation or G2 PASS. **Not** bounded-host or partial creation.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED** |
| **Wave** | **W3-A COMPLETE** |
| **Implementation** | **NOT STARTED** |
| **Coverage metrics** | **UNCHANGED** — RC **32/32** · RPC **23/32** · RSC **3/10 global; 1/1 LANDING · 1/1 CATEGORY_PAGE · 1/1 PRODUCT_PAGE** · SC **LANDING PASS · CATALOG PARTIAL** · PC **1/1 LANDING · 1/1 CATALOG corridor** |
| **W3-B authorization** | **W3-B IMPLEMENTATION AUTHORIZED** |
| **Next authorized wave** | **WF-R01.3 G2-R1 W3-B — SERVICES Reference Partial** |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Artefact ID** | WF-R01.3 G2-R1 W3 PROMO Source Inventory v1 |
| **Purpose** | Canonical PROMO W3 source inventory; bounded source universe; primary/secondary source decisions; contract confirmation; W3-B–W3-E execution preflight |
| **Charter authority** | [wf-r01-3-g2-r1-w3-promo-reference-completion-charter-v1.md](wf-r01-3-g2-r1-w3-promo-reference-completion-charter-v1.md) |
| **Wave W3-A REPORT** | [wf-r01-3-g2-r1-w3-a-promo-source-inventory-v1.md](../../reports/wf-r01-3-g2-r1-w3-a-promo-source-inventory-v1.md) |
| **Inventory precedent** | [wf-r01-3-4-catalog-reference-inventory-v1.md](wf-r01-3-4-catalog-reference-inventory-v1.md) |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| G2-R1 W3 charter | `projects/mars-website-factory/wf-r01-3-g2-r1-w3-promo-reference-completion-charter-v1.md` | Normative W3 scope, contracts, waves |
| G2-R1 charter pass | `reports/wf-r01-3-g2-r1-w3-promo-charter-pass-v1.md` | ACCEPTED evidence |
| G2 formal gate charter | `projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md` | Parent gate; G2-02..04 criteria |
| G2 charter pass | `reports/wf-r01-3-g2-formal-gate-pass-charter-pass-v1.md` | Readiness snapshot |
| Coverage Model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | RPC/RSC/SC/PC rules |
| Vocabulary Canon | `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` | F3 block family |
| Program design | `reports/wf-r01-3-reference-expansion-program-design-v1.md` | Wave map W3 |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Bounded host shell order |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | Shell slots |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | Scaffold vs bounded-host boundary |
| Block Registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | 32 `block_id` SSOT |
| Core Block Library | `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md` | Implementation inventory |
| Block Gaps | `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md` | W3 gap rows |
| Site-Type Block Matrix | `workspaces/website-factory-reference-v1/block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md` | Site-type applicability |
| Page-Block Mapping | `workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md` | Page-type applicability |
| Catalog inventory precedent | `projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md` | Q0–Q3 discipline |

---

## 4. Scope

### In scope (Wave W3-A)

- Registry reconfirmation for **SERVICES**, **TEAM**, **ABOUT**
- Competing partial check across canonical partial directories
- Bounded local source search and candidate classification
- Primary/secondary/rejected source selection per target
- Sanitization matrix
- Vocabulary and block-boundary contract confirmation
- Applicability reconciliation against matrices
- Canonical future paths and bounded-host strategy
- Implementation wave order and W3-B authorization gate
- TEAM/ABOUT readiness for W3-C / W3-D

### Out of scope (Wave W3-A)

- HTML/SCSS/JS partials · bounded host · registry edits
- RPC/RSC/SC/PC accrual · G2 evaluation · W3-B+ implementation
- External web research · production URL copy · real PII transfer
- Vocabulary Canon / Coverage Model edits

---

## 5. Source Quality Model

| Quality | Definition |
|---------|------------|
| **Q3** | Implemented, validated, reusable and sufficiently universal |
| **Q2** | Implemented or well-documented, structurally useful, but requires adaptation or sanitization |
| **Q1** | Prototype or partial evidence; useful only as corroboration |
| **Q0** | Weak, obsolete, incompatible or misleading source |
| **SAFE UNKNOWN** | Source relevance or authority cannot be confirmed |

**Rule:** Visual polish alone does not raise quality. Identity match and sanitization path required.

---

## 6. Search Boundary

### Included locations

| Class | Paths searched |
|-------|------------------|
| Website Factory reference workspace | `workspaces/website-factory-reference-v1/src/partials/` · `src/scss/` · `src/pages/` |
| Block registry and blueprints | `workspaces/website-factory-reference-v1/block-registry/` · `blueprints/PROMO-BLUEPRINT-v1.md` |
| Registered execution-case workspaces | `workspaces/triumph-manipulator-landing-v6/` · `workspaces/triumph-manipulator-landing-v2/` · `workspaces/triumph-manipulator-landing/` · `workspaces/isbd-care-landing/` (docs only — no PROMO W3 HTML) |
| Document-first execution case | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/` (block inventory, design audit — **no** shipped HTML for W3 targets) |
| Programme authority docs | `projects/mars-website-factory/` · `reports/wf-r01-3-*` |
| Triumph programme docs | `projects/triumph-manipulator-landing/V6-ACTIVE-STRUCTURE-MAP.md` · `V6-PAGE-ROLLOUT-PLAN.md` |

### Excluded locations

| Class | Reason |
|-------|--------|
| `.recovery-temp/` | Forensic snapshots; not approved source-ready artefacts |
| `incoming/mig/` production page dumps | Unsanitized client/production HTML |
| BZPM / OpenCart live captures | Catalog identity; CMS coupling; rejected for PROMO W3 |
| External websites | Task forbids external connection and new web research |

### Search terms used

`services` · `service directions` · `team` · `staff` · `experts` · `specialists` · `about` · `company` · `mission` · `history` · `capabilities` · `promo` · `corporate` · `segments` · `advantages` · `page-intro` · `BLK-010` · `BLK-026` · `BLK-036`

### Source count

| Target | Candidates evaluated | Selected primary | Selected secondary | Rejected |
|--------|---------------------|------------------|--------------------|----------|
| **SERVICES** | 6 | 1 | 2 | 3 |
| **TEAM** | 5 | 1 | 2 | 2 |
| **ABOUT** | 5 | 1 | 2 | 2 |

### No-external-research confirmation

**Confirmed.** All candidates resolved from in-repo paths only.

---

## 7. Registry Reconfirmation

| Target | Registry row | `block_id` | Family | RC member | Current reference | RPC eligible | Competing partial |
|--------|--------------|------------|--------|-----------|-------------------|--------------|-------------------|
| **SERVICES** | BLOCK-REGISTRY-v1 § SERVICES | `SERVICES` | F3 Content · **COMPANY** | **Yes** (32/32) | **Absent** — BLOCK-GAPS: Not implemented | **Yes** — upon T1+ evidence | **None** — no `services.html` in `src/partials/sections/` or `src/partials/components/` |
| **TEAM** | BLOCK-REGISTRY-v1 § TEAM | `TEAM` | F3 Content · **COMPANY** | **Yes** | **Absent** — BLOCK-GAPS: Not implemented | **Yes** — upon T1+ evidence | **None** — no `team.html` in canonical partial directories |
| **ABOUT** | BLOCK-REGISTRY-v1 § ABOUT | `ABOUT` | F3 Content · **COMPANY** | **Yes** | **Absent** — BLOCK-GAPS: Not implemented | **Yes** — upon T1+ evidence | **None** — no `about.html` in canonical partial directories |

**Preflight verdict:** **IMPLEMENTATION ELIGIBLE** for all three targets. **No competing accepted partial** found.

**Registry purpose summaries (unchanged):**

| `block_id` | Purpose |
|------------|---------|
| `SERVICES` | Present service/product lines with drill-down to money pages |
| `TEAM` | Leadership and staff presentation |
| `ABOUT` | Entity narrative, history, mission |

---

## 8. SERVICES Candidate Sources

| Source ID | Exact path | Type | Project status | Quality | Reusable structure | Rejected content | Sanitization | Suitability |
|-----------|------------|------|----------------|---------|-------------------|------------------|--------------|-------------|
| **SVC-CAND-01** | `workspaces/website-factory-reference-v1/src/partials/components/category-grid.html` | HTML partial | accepted / implemented | **Q3** | Semantic section; heading; `<ul>` card collection; item title; short description; optional decorative media slot; detail link; responsive card grid SCSS in `_category-grid.scss` | Catalog taxonomy semantics; `category_grid` block_id; item counts; PLP routing | Rebuild as `wf-services` namespace; remove count field or make non-catalog optional; fictional service names; `#` links | **primary** |
| **SVC-CAND-02** | `workspaces/website-factory-reference-v1/src/partials/sections/benefits.html` | HTML partial | accepted / implemented | **Q3** | Section header (eyebrow, title, lead); icon + title + description item grid; list semantics; long-text wrap patterns in `_benefits.scss` | Outcome/benefit framing; no detail link in current minimum | Retarget copy to service directions; optional add detail link per charter minimum | **secondary** |
| **SVC-CAND-03** | `workspaces/triumph-manipulator-landing-v2/src/partials/sections/segments-applications-grid.html` | HTML partial | implemented / client delivery | **Q2** | Header + lead; multi-card grid; per-item title; bullet sub-list; optional CTA link; responsive breakpoints in `_segments-applications-grid.scss` | Client service taxonomy; Russian commercial copy; segment photography; `#kontakty` anchors; 8-item scale | Replace all copy; neutral placeholders; strip nested bullet lists or collapse to short description; remove client images | **secondary** |
| **SVC-CAND-04** | `workspaces/triumph-manipulator-landing/src/partials/sections/advantages.html` | HTML partial | prototype / starter | **Q2** | Minimal `<ul>` service-like list; title + short paragraph per item | Generic starter demo copy; no media; no detail link; weak PROMO hub semantics | Full neutral rewrite; add optional icon/link in implementation | **rejected** (too weak as primary; keep as corroboration only) |
| **SVC-CAND-05** | `workspaces/triumph-manipulator-landing-v6/src/partials/sections/v5-ppc/zakaz/screen-02-tasks.html` | HTML partial | implemented / PPC | **Q0** | Task cluster grid — **wrong identity** (application tasks, not service directions) | Entire block — PROCESS / use-case semantics | N/A | **rejected** |
| **SVC-CAND-06** | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-BLOCK-INVENTORY-v1.md` (BLK-010, BLK-011, BLK-020) | Blueprint / report | document-first | **Q1** | Service preview grid IA; hub category grid; four-directions program layout — structural notes only | No HTML implementation in repo; client-specific medical taxonomy | Doc-first extraction only; cannot copy labels | **rejected** as implementation source (corroboration only) |

---

## 9. SERVICES Selection

| Field | Decision |
|-------|----------|
| **Primary source** | **SVC-CAND-01** — `category-grid.html` + `_category-grid.scss` |
| **Secondary sources** | **SVC-CAND-02** (`benefits.html` — header + compact icon grid variant) · **SVC-CAND-03** (`segments-applications-grid.html` — media-forward card corroboration) |
| **Rejected sources** | **SVC-CAND-04** (too minimal) · **SVC-CAND-05** (wrong block identity) · **SVC-CAND-06** (doc-only) · BZPM catalog grids (explicit charter rejection) · Triumph v6 PPC pages (no SERVICES block) |
| **Sanitization** | Strip catalog/count semantics; rebuild under `wf-services`; fictional service titles and descriptions; `#` detail links; no production URLs; no client brand |
| **Contract implications** | One canonical card-grid partial; ≥3 neutral items in bounded host; optional icon/media; optional detail link; no JS default |
| **Final quality** | **Q3** (primary path) |

---

## 10. TEAM Candidate Sources

| Source ID | Exact path | Type | Project status | Quality | Reusable structure | Rejected content | Sanitization | Suitability |
|-----------|------------|------|----------------|---------|-------------------|------------------|--------------|-------------|
| **TEAM-CAND-01** | `workspaces/website-factory-reference-v1/src/partials/sections/testimonials.html` | HTML partial | accepted / implemented | **Q2** | Section header; collection of person cards; avatar placeholder; name; role line; responsive grid in `_testimonials.scss`; missing-photo letter avatar pattern | Quote body; star rating; review source metadata; TESTIMONIALS block identity | Extract card anatomy only; remove quote/rating/footer; fictional names and roles; neutral portrait placeholders | **primary** |
| **TEAM-CAND-02** | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-BLOCK-INVENTORY-v1.md` (BLK-026) | Blueprint / report | document-first | **Q1** | Specialists cards grid: photo, name, role; 3–4 column responsive grid notes | No listing HTML; real specialist names in design audit; medical client context | Fictional personas only in implementation | **secondary** |
| **TEAM-CAND-03** | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-NUMERIC-DESIGN-RULES-v2.md` | Design rules doc | document-first | **Q1** | Avatar circular crop; 4→1 column collapse; card gap tokens | Not implementation evidence | Rebuild tokens in WF namespace | **secondary** |
| **TEAM-CAND-04** | `workspaces/triumph-manipulator-landing-v2/src/partials/sections/trust-reviews.html` | HTML partial | implemented / client | **Q0** | Review cards — **TESTIMONIALS** identity, not TEAM | Entire source for TEAM | N/A | **rejected** |
| **TEAM-CAND-05** | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/` snapshots | Production HTML dump | legacy / forensic | **Q0** | Unknown DOM — not approved | Real people; production URLs; client brands | N/A | **rejected** |

**Note:** No dedicated TEAM / staff / specialist **HTML partial** exists in any approved Website Factory or Triumph workspace. Primary path requires **structural extraction** from testimonials card anatomy, not wholesale block reuse.

---

## 11. TEAM Selection

| Field | Decision |
|-------|----------|
| **Primary source** | **TEAM-CAND-01** — `testimonials.html` card anatomy (avatar, name, role, expertise line) |
| **Secondary sources** | **TEAM-CAND-02** (BLK-026 grid semantics) · **TEAM-CAND-03** (responsive numeric rules) |
| **Rejected sources** | **TEAM-CAND-04** · **TEAM-CAND-05** · full `testimonials` block · carousel-only layouts · employee CRM data |
| **Privacy / sanitization** | **Fictional names, roles, expertise only.** No real portraits, phones, bios, or social links. Placeholder avatars with accessible `alt` (name + role). |
| **Contract implications** | Member collection; ≥3 items in host; optional profile action as `#`; no modal bios; no JS default |
| **Final quality** | **Q2** (primary — adaptation required to strip testimonial layers) |

---

## 12. ABOUT Candidate Sources

| Source ID | Exact path | Type | Project status | Quality | Reusable structure | Rejected content | Sanitization | Suitability |
|-----------|------------|------|----------------|---------|-------------------|------------------|--------------|-------------|
| **ABT-CAND-01** | `workspaces/website-factory-reference-v1/src/partials/sections/benefits.html` | HTML partial | accepted / implemented | **Q2** | Section header with eyebrow, title, lead; readable narrative lead pattern; container/wf-section conventions — **header + lead zone** reusable for ABOUT narrative shell | Benefits grid body — wrong semantic for ABOUT highlights unless reframed as fact chips | Rewrite all copy to organisation narrative; add separate highlights list (≥2 facts); optional neutral media column in implementation | **primary** |
| **ABT-CAND-02** | `workspaces/triumph-manipulator-landing-v2/src/partials/sections/page-intro.html` | HTML partial | prototype / starter | **Q2** | Minimal `<h1>` + lead paragraph pattern for internal/about-style pages | Page-level H1 semantics (ABOUT block uses section heading, not page H1 in partial host) | Demote to section heading in partial context; fictional company copy | **secondary** |
| **ABT-CAND-03** | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-BLOCK-INVENTORY-v1.md` (BLK-036–038) | Blueprint / report | document-first | **Q1** | About narrative trio: identity, facility story, infrastructure highlights | No HTML; client-specific medical claims | Fictional facts only | **secondary** |
| **ABT-CAND-04** | `workspaces/triumph-manipulator-landing-v6/src/partials/sections/screen-01-hero.html` | HTML partial | implemented / PPC | **Q0** | Hero conversion shell — **HERO** identity; mis-tagged `#about` anchor in legacy header only | Entire hero form/CTA stack | N/A | **rejected** |
| **ABT-CAND-05** | `workspaces/triumph-manipulator-landing-v2/src/pages/about.html` | Page scaffold | starter demo | **Q0** | Composes page-intro + advantages — **not** ABOUT block; mixes wrong blocks | Full page composition | N/A | **rejected** |

---

## 13. ABOUT Selection

| Field | Decision |
|-------|----------|
| **Primary source** | **ABT-CAND-01** — `benefits.html` header/lead shell + new highlights region (implementation synthesizes header pattern + facts list) |
| **Secondary sources** | **ABT-CAND-02** (`page-intro.html` — lead paragraph density) · **ABT-CAND-03** (BLK-036–038 narrative zones) |
| **Rejected sources** | **ABT-CAND-04** · **ABT-CAND-05** · embedded TEAM/PROCESS/TRUST · long SEO dumps · legal company registers |
| **Sanitization** | Fictional organisation name and facts; no trademarked claims; no real addresses; `#` on optional supporting link |
| **Contract implications** | Section heading + lead + short narrative + ≥2 highlights; optional neutral media; responsive stacked/split layout; no JS default |
| **Final quality** | **Q2** (primary — composite adaptation from validated partial conventions) |

---

## 14. Rejected Sources

| Source ID | Target | Path | Reason |
|-----------|--------|------|--------|
| SVC-CAND-05 | SERVICES | `triumph-manipulator-landing-v6/.../screen-02-tasks.html` | Use-case task grid — not service directions |
| SVC-CAND-06 | SERVICES | FP-0002 block inventory | Doc-only — no HTML |
| BZPM catalog grids | SERVICES | `projects/ocpilot/sites/site-002/` (charter default rejection) | Catalog PLP identity + CMS coupling |
| Triumph v6 active build | SERVICES · TEAM · ABOUT | `triumph-manipulator-landing-v6/src/pages/index.html` | PPC landing only — no PROMO multi-page W3 blocks ([V6-ACTIVE-STRUCTURE-MAP.md](../triumph-manipulator-landing/V6-ACTIVE-STRUCTURE-MAP.md)) |
| TEAM-CAND-04 | TEAM | `triumph-manipulator-landing-v2/.../trust-reviews.html` | TESTIMONIALS identity |
| TEAM-CAND-05 | TEAM | `incoming/mig/...` | Production dump — unsanitized PII risk |
| ABT-CAND-04 | ABOUT | `triumph-manipulator-landing-v6/.../screen-01-hero.html` | HERO / conversion block |
| ABT-CAND-05 | ABOUT | `triumph-manipulator-landing-v2/src/pages/about.html` | Page scaffold mixing unrelated blocks |
| `.recovery-temp/*` | All | Various | Unapproved forensic captures |

---

## 15. Sanitization Matrix

| Data/content type | Allowed | Required action |
|-------------------|---------|-----------------|
| Structural hierarchy | Yes | Normalize to charter minimum |
| CSS/layout idea | Yes | Rebuild in `wf-*` namespace |
| Client brand | No | Remove |
| Real employee data | No | Replace with fictional personas |
| Real portrait | No by default | Neutral placeholder or letter avatar |
| Production URL | No | Replace with `#` |
| Real commercial claim | No | Replace with neutral copy |
| CMS/backend logic | No | Reject source |
| Analytics/tracking | No | Reject |
| Project-specific classes | No | Rename to `wf-services` / `wf-team` / `wf-about` |
| Licensed media | Only if approved | Otherwise replace with neutral slot |
| Catalog item counts | No | Remove from SERVICES adaptation |
| Testimonial quotes/ratings | No | Strip when adapting TEAM from testimonials anatomy |

---

## 16. Vocabulary Contract Confirmation

**Authority check:** BLOCK-REGISTRY-v1 + G2-R1 charter §11–19 vs this inventory — **no conflict**. **STOP not required.**

### SERVICES

| Field | Confirmed contract |
|-------|-------------------|
| **Purpose** | Present service/product lines with drill-down to money pages |
| **Ownership** | Service directions / offerings collection |
| **Internal repeated unit** | Service item — title, short description, optional icon/media, optional detail link |
| **Required content** | Section heading; ≥2 service items; item title; short description |
| **Optional content** | Lead; decorative icon/media; detail link |
| **Excluded neighboring blocks** | PROCESS, PRICING, FAQ, LEAD_FORM, primary CTA, CASES, PRODUCT_GRID, catalog blocks |

### TEAM

| Field | Confirmed contract |
|-------|-------------------|
| **Purpose** | Leadership and staff presentation |
| **Ownership** | People / roles / expertise |
| **Internal repeated unit** | Member item — fictional name, role, short expertise, portrait placeholder |
| **Required content** | Section heading; ≥2 members; name; role; expertise; neutral portrait placeholder |
| **Optional content** | Lead; profile/contact action |
| **Excluded neighboring blocks** | ABOUT narrative, CONTACTS, TESTIMONIALS, PARTNERS, vacancies, TRUST, CERTIFICATES |

### ABOUT

| Field | Confirmed contract |
|-------|-------------------|
| **Purpose** | Entity narrative, history, mission |
| **Ownership** | Organisation identity / positioning / concise narrative |
| **Internal repeated unit** | Highlight/fact item (not separate `block_id`) |
| **Required content** | Section heading; lead; short narrative; ≥2 highlights/facts |
| **Optional content** | Neutral media; supporting link (not primary CTA band) |
| **Excluded neighboring blocks** | Full TEAM, PROCESS, TRUST, CERTIFICATES, FEATURES, CONTACTS, LEAD_FORM |

### PROCESS and neighboring blocks

| Block | W3 scope | Notes |
|-------|----------|-------|
| **PROCESS** | **Excluded** from G2-R1 implementation | Existing T1+ `process.html` — do not re-build |
| **FEATURES** | Separate owner | Product-style capabilities |
| **TRUST / TESTIMONIALS** | Separate owners | Proof and quotes — not TEAM/ABOUT substitutes |
| **CONTACTS / LEAD_FORM / CTA** | Separate owners | Optional links only inside W3 blocks |

---

## 17. Block Boundary Confirmation

| Concern | Canonical owner | Source extraction rule |
|---------|-----------------|------------------------|
| Service directions | **SERVICES** | Extract card/list collection only |
| Workflow steps | **PROCESS** | Reject order-steps / task-flow sources |
| People and roles | **TEAM** | Extract member card anatomy; reject quote/rating layers |
| Organisation narrative | **ABOUT** | Extract header/lead/narrative; reject hero conversion stacks |
| Proof and reassurance | **TRUST** / **CASES** / **TESTIMONIALS** | Do not import into W3 partials |
| Benefits | **BENEFITS** / **FEATURES** | Reuse layout conventions only — not block identity |
| Contact information | **CONTACTS** | Not embedded |
| Lead capture | **LEAD_FORM** | Not embedded |
| Commercial action band | **CTA** | Optional single link only |

---

## 18. Applicability Confirmation

### Site types (SITE-TYPE-BLOCK-MATRIX-v2)

| Block | Surface | Matrix state | Interpretation |
|-------|---------|--------------|----------------|
| **SERVICES** | LANDING | FORBIDDEN | N/A — not applicable |
| **SERVICES** | PROMO | **REQ** | Primary consumer |
| **SERVICES** | CATALOG | FORBIDDEN | N/A |
| **SERVICES** | ECOMMERCE | FORBIDDEN | N/A |
| **SERVICES** | CORPORATE | **REQ** | Solutions hub |
| **TEAM** | LANDING | FORBIDDEN | N/A |
| **TEAM** | PROMO | **OPT** | Optional on about route |
| **TEAM** | CATALOG | FORBIDDEN | N/A |
| **TEAM** | ECOMMERCE | FORBIDDEN | N/A |
| **TEAM** | CORPORATE | **OPT** | Optional |
| **ABOUT** | LANDING | FORBIDDEN | N/A |
| **ABOUT** | PROMO | **REQ** | Primary consumer |
| **ABOUT** | CATALOG | FORBIDDEN | N/A |
| **ABOUT** | ECOMMERCE | FORBIDDEN | N/A |
| **ABOUT** | CORPORATE | **REQ** | Company narrative |

**Extended site types (SAAS, WEB_APPLICATION, MARKETPLACE):** **SAFE UNKNOWN** for W3 minimum — reference partials target PROMO + CORPORATE Core matrix only.

**Drift:** None between charter §13 and matrix.

### Page types (PAGE-BLOCK-MAPPING-v1)

| Block | Surface | Matrix state | Interpretation |
|-------|---------|--------------|----------------|
| **SERVICES** | HOME_PAGE | **REQ*** | *PROMO/CORPORATE home only |
| **SERVICES** | LANDING_PAGE | FORB | N/A |
| **SERVICES** | SERVICE_PAGE | N/A | Money page — different stack |
| **SERVICES** | CATEGORY_PAGE / PRODUCT_PAGE | FORB | N/A |
| **SERVICES** | ABOUT_PAGE / CONTACT_PAGE | FORB | N/A |
| **TEAM** | HOME_PAGE | FORB | N/A |
| **TEAM** | ABOUT_PAGE | **OPT** | Optional composition |
| **TEAM** | Other registered types | FORB | Unless matrix amended |
| **ABOUT** | ABOUT_PAGE | **REQ** | Primary host page type |
| **ABOUT** | HOME_PAGE / SERVICE_PAGE / CONTACT_PAGE | FORB | N/A |

**Drift:** None between charter §14 and matrix.

**Implementation authorized:** Applicability does **not** block W3 reference partials.

---

## 19. Canonical Partial Paths

| Artefact | Future path | Notes |
|----------|-------------|-------|
| **SERVICES partial** | `workspaces/website-factory-reference-v1/src/partials/components/services.html` | Matches COMPANY collection convention (cf. `category-grid.html`) |
| **TEAM partial** | `workspaces/website-factory-reference-v1/src/partials/components/team.html` | Charter W3 path lock |
| **ABOUT partial** | `workspaces/website-factory-reference-v1/src/partials/components/about.html` | Charter W3 path lock |
| **SERVICES SCSS** | `workspaces/website-factory-reference-v1/src/scss/components/_services.scss` | |
| **TEAM SCSS** | `workspaces/website-factory-reference-v1/src/scss/components/_team.scss` | |
| **ABOUT SCSS** | `workspaces/website-factory-reference-v1/src/scss/components/_about.scss` | |
| **Bounded host** | `workspaces/website-factory-reference-v1/src/pages/promo-block-references.html` | Created in W3-B (initial) — not before |
| **SCSS import** | Add `@use 'components/services'` (and later team/about) to `src/scss/main.scss` after components block | Preserve contractual import order |
| **JS decision** | **None** for all three blocks (charter default) | |
| **Build** | `npm run build` in reference workspace — required per T1+ evidence contract | |

**Conflict check:** No existing files at these paths. **No conflict.**

---

## 20. Bounded Host Strategy

| Field | Decision |
|-------|----------|
| **Selected option** | **Option A — one combined PROMO block reference host** (charter §23) |
| **Future path** | `src/pages/promo-block-references.html` |
| **Creation timing** | **W3-B** creates host with **SERVICES** first; **W3-C** adds **TEAM**; **W3-D** adds **ABOUT** |
| **Composition (final)** | HEADER_NAV · MAIN → SERVICES · TEAM · ABOUT · FOOTER · LEGAL_LINKS |
| **Hook policy** | One `data-block-id` per block root; `aria-labelledby` per section; no nested block IDs on items |
| **Scaffold boundary** | Host is **not** HOME_PAGE / SERVICE_PAGE / ABOUT_PAGE / CONTACT_PAGE scaffold; **not** RSC/PC/PROMO SC evidence |
| **Coverage boundary** | Host counts toward **zero** RPC/RSC/SC/PC |

**Recommended root markup (implementation waves):**

```html
<section class="wf-services" data-block-id="services" aria-labelledby="services-title">
<section class="wf-team" data-block-id="team" aria-labelledby="team-title">
<section class="wf-about" data-block-id="about" aria-labelledby="about-title">
```

---

## 21. Implementation Wave Order

| Wave | Target | Readiness | Expected output |
|------|--------|-----------|-----------------|
| **W3-A** | Inventory + contract confirmation | **COMPLETE** | This document + W3-A REPORT |
| **W3-B** | **SERVICES** | **AUTHORIZED** | `services.html` + SCSS + bounded host (SERVICES only) + build PASS + REPORT |
| **W3-C** | **TEAM** | **READY WITH CONSTRAINTS** | `team.html` + SCSS + host hook + build PASS + REPORT |
| **W3-D** | **ABOUT** | **READY WITH CONSTRAINTS** | `about.html` + SCSS + host hook + build PASS + REPORT |
| **W3-E** | W3 exit + G2-R2 readiness | After W3-B/C/D | Five-dimension snapshot; handoff REPORT |

**Sequencing rationale:** SERVICES has strongest Q3 primary and simplest boundary; TEAM and ABOUT depend on shared host discipline established in W3-B; ABOUT composite is highest narrative risk — last.

**Batching:** Default **one block per pass** — **not** merged B+C+D.

---

## 22. W3-B Authorization

```text
W3-B IMPLEMENTATION AUTHORIZED
```

| Gate criterion | Status |
|----------------|--------|
| SERVICES Registry identity confirmed | **PASS** |
| SERVICES source quality ≥ Q2 | **PASS** — primary **Q3** |
| Universal contract confirmed | **PASS** |
| Canonical path confirmed | **PASS** |
| Sanitization rules confirmed | **PASS** |
| Bounded-host strategy confirmed | **PASS** |
| No vocabulary conflict | **PASS** |
| No new Registry identity required | **PASS** |

---

## 23. TEAM and ABOUT Readiness

| Target | Wave | State | Constraints |
|--------|------|-------|-------------|
| **TEAM** | W3-C | **READY WITH CONSTRAINTS** | No native TEAM HTML in repo; must strip testimonial layers from primary source; fictional data only |
| **ABOUT** | W3-D | **READY WITH CONSTRAINTS** | Composite implementation from benefits header pattern + new highlights region; no single Q3 monolithic source |

**Remaining unknowns:**

| Item | Status |
|------|--------|
| Triumph v6 as PROMO multi-page source | **Rejected for W3** — PPC-only active build |
| FP-0002 HTML artefacts for BLK-026 / BLK-036 | **SAFE UNKNOWN** — doc-first only; not blocking W3-C/D |
| Extended site types applicability | **SAFE UNKNOWN** — out of W3 minimum |

---

## 24. Coverage Boundary

| Dimension | Current (frozen) | After W3-D (potential max) | W3-A accrual |
|-----------|------------------|------------------------------|--------------|
| **RC** | **32/32** | **32/32** | **0** |
| **RPC** | **23/32** | **26/32** (if all three T1+) | **0** |
| **RSC** | **3/10** | **3/10** | **0** |
| **SC** | **LANDING PASS · CATALOG PARTIAL** | unchanged until G2-R2+ | **0** |
| **PC** | **1/1 LANDING · 1/1 CATALOG corridor** | unchanged | **0** |

**No-accrual confirmation:** W3-A awards **zero** coverage credit.

---

## 25. Known Risks and SAFE UNKNOWN

| Severity | Finding | Effect | Destination |
|----------|---------|--------|-------------|
| Medium | No dedicated TEAM/ABOUT HTML sources at Q3 | W3-C/D require adaptation from adjacent patterns | W3-C/D wave REPORTs |
| Low | Triumph v6 charter default primary probe **failed** | Factory-internal sources selected instead | This inventory |
| Low | SERVICES primary adapted from catalog card grid | Must enforce sanitization — no taxonomy/count semantics | W3-B implementation |
| Low | FP-0002 specialist/about blocks doc-only | Corroboration only | SAFE UNKNOWN until HTML exists |
| Low | Extended site types (SAAS, etc.) | Not in W3 minimum applicability proof | Future charter if needed |

---

## 26. Evidence Paths

```text
projects/mars-website-factory/wf-r01-3-g2-r1-w3-promo-reference-completion-charter-v1.md
reports/wf-r01-3-g2-r1-w3-promo-charter-pass-v1.md
projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md
reports/wf-r01-3-g2-formal-gate-pass-charter-pass-v1.md
projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md
projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md
reports/wf-r01-3-reference-expansion-program-design-v1.md
reports/wf-r01-3-post-g1-track-selection-v1.md
reports/foundry-registry-expansion-program-design-v1.md
projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md
projects/mars-website-factory/global-shell-contract-v1.md
projects/mars-website-factory/page-type-shell-matrix-v1.md
projects/mars-website-factory/reference-scaffold-contract-v1.md
workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md
workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md
workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md
workspaces/website-factory-reference-v1/block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md
workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md
workspaces/website-factory-reference-v1/src/partials/components/category-grid.html
workspaces/website-factory-reference-v1/src/scss/components/_category-grid.scss
workspaces/website-factory-reference-v1/src/partials/sections/benefits.html
workspaces/website-factory-reference-v1/src/scss/sections/_benefits.scss
workspaces/website-factory-reference-v1/src/partials/sections/testimonials.html
workspaces/website-factory-reference-v1/src/scss/sections/_testimonials.scss
workspaces/website-factory-reference-v1/src/pages/category-references.html
workspaces/website-factory-reference-v1/src/scss/main.scss
workspaces/triumph-manipulator-landing-v2/src/partials/sections/segments-applications-grid.html
workspaces/triumph-manipulator-landing-v2/src/scss/sections/_segments-applications-grid.scss
workspaces/triumph-manipulator-landing-v2/src/partials/sections/page-intro.html
workspaces/triumph-manipulator-landing/src/partials/sections/advantages.html
projects/triumph-manipulator-landing/V6-ACTIVE-STRUCTURE-MAP.md
projects/triumph-manipulator-landing/V6-PAGE-ROLLOUT-PLAN.md
workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-BLOCK-INVENTORY-v1.md
workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-NUMERIC-DESIGN-RULES-v2.md
projects/mars-website-factory/roadmap.md
projects/mars-website-factory/OPERATIONAL-INDEX.md
```

---

## 27. Decision

**Decision:** **PUBLISHED** — WF-R01.3 G2-R1 W3 PROMO Source Inventory v1 is normative operator authority for W3-B–W3-E source selection and contract preflight.

**Package state after inventory:**

```text
G2-R1 W3-A — COMPLETE
W3-B — AUTHORIZED (SERVICES)
W3-C — READY WITH CONSTRAINTS (TEAM)
W3-D — READY WITH CONSTRAINTS (ABOUT)
G2-R1 — CHARTERED · NOT IMPLEMENTED · NOT COMPLETE
```

**Next programme task (implementation — not executed here):**

```text
WF-R01.3 G2-R1 W3-B — SERVICES Reference Partial
```

---

*Canonical inventory: `projects/mars-website-factory/wf-r01-3-g2-r1-w3-promo-source-inventory-v1.md` · v1 · 2026-06-20*
