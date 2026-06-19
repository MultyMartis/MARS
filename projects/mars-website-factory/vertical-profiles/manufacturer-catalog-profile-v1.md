# MANUFACTURER Catalog Vertical Profile v1

**Profile ID:** MANUFACTURER  
**Subprogram:** WF-R01.3.4 — Catalog & Vertical Profile References  
**Wave:** C7 — Vertical Profile Binding  
**Version:** v1  
**Date:** 2026-06-20  
**Status:** **P1 READY**

**Honesty boundary:** Documentation-only binding layer. **Not** a Registry row, **not** a site type, **not** runtime, **not** production theme, **not** CMS schema. Adapts canonical catalog references to recurring B2B manufacturer / industrial catalogue requirements.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Profile status** | **P1 READY** |
| **Evidence basis** | SRC-BZPM-002 — verified local execution evidence (C1 inventory §16) |
| **Binding publication** | Wave C7 — documentation only |
| **Implementation** | **NOT STARTED** — no reference partial mutation in C7 |
| **Registry ID** | **None** — `MANUFACTURER` = profile document identity only |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Canonical working identity** | **MANUFACTURER** |
| **Registry site_type_code** | **Does not exist** — profile binds to existing `CATALOG` site type + `CORPORATE` notes per charter §13 |
| **Scope** | Industrial equipment · technical products · production catalogues · B2B procurement · dealer-oriented catalogs |
| **Not limited to** | Single client · single product niche · single brand theme |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| WF-R01.3.4 Charter | `projects/mars-website-factory/wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md` | Vertical Profile Policy §13 |
| Catalog Reference Inventory | `projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md` | MANUFACTURER evidence §16 |
| Wave C1 REPORT | `reports/wf-r01-3-4-wave-c1-catalog-reference-inventory-v1.md` | P1 READY classification §15 |
| Wave C5 REPORT | `reports/wf-r01-3-4-wave-c5-category-page-scaffold-v1.md` | CATEGORY_PAGE scaffold evidence |
| Wave C6 decision | `projects/mars-website-factory/wf-r01-3-4-product-page-scope-decision-v1.md` | PRODUCT_PAGE scaffold zones |
| Block Registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | Canonical `block_id` only |
| Page-Type Registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` | CATEGORY_PAGE · PRODUCT_PAGE |

---

## 4. Evidence Level

| Class | State |
|-------|-------|
| **Verified local execution evidence** | SRC-BZPM-002 — faceted filters · SKU/article cards · request-price · compare · certificates/dealer trust · PDP spec tabs |
| **Published Website Factory references** | FILTERS · SEARCH · CATEGORIES · CATEGORY_GRID · PRODUCT_GRID · PRODUCT_CARD · CATEGORY_PAGE · PRODUCT_PAGE scaffolds (Waves C2–C6) |
| **Gaps (honest)** | Dedicated document block identity · engineering drawing gallery runtime — **composition zone / SAFE UNKNOWN** |
| **Live-site dependency** | **None required** for C7 binding |

---

## 5. Applicability

MANUFACTURER profile applies when a project needs:

- Deep technical attribute presentation on PLP and PDP
- B2B commercial states (request price · made to order · lead time)
- Dealer / procurement trust signals
- Hierarchical product taxonomy (type → family → series → model/SKU)
- Specification-first PDP emphasis

MANUFACTURER profile **does not** replace universal catalog contract. It selects field priorities and adaptation policies within existing canonical blocks and scaffold-owned zones.

---

## 6. Universal Contract Inheritance

Universal catalog contract (immutable identities):

```text
FILTERS · SEARCH · CATEGORIES · CATEGORY_GRID · PRODUCT_GRID · PRODUCT_CARD
CATEGORY_PAGE · PRODUCT_PAGE
```

Profile **must inherit** shell contract, scaffold contract, and Vocabulary Canon (F1–F6). Profile **may not**:

- Rename canonical identities
- Create hidden Registry rows
- Elevate optional universal fields to universal requirements without charter authority
- Change coverage accounting (RC · RPC · RSC · SC · PC)

---

## 7. Category Hierarchy Policy

Typical hierarchy levels (profile policy — **not** new page-type contract):

| Level | Example role | Binding |
|-------|--------------|---------|
| **type** | Equipment class | `CATEGORIES` navigation emphasis |
| **family** | Product line | `CATEGORIES` + breadcrumb context |
| **series** | Model range | Filter facet + card subtitle |
| **model / SKU** | Orderable unit | `PRODUCT_CARD` identity · PDP headline |

Depth varies by manufacturer IA. Profile documents expected levels; implementation chooses actual taxonomy per project review.

---

## 8. CATEGORY_PAGE Binding

| Zone / block | Universal role | MANUFACTURER adaptation |
|--------------|----------------|-------------------------|
| **HEADER_NAV** | Shell REQ | Standard — catalog discovery via embedded SEARCH |
| **BREADCRUMBS** | PLP REQ | Deep hierarchy trail (type → family → series) |
| **FILTERS** | PLP REQ | Technical facet priority (see §10) |
| **CATEGORIES** | PLP POL | Subcategory chips / megamenu context when shallow PLP |
| **PRODUCT_GRID** | PLP REQ | Spec-dense listing grid |
| **PRODUCT_CARD** | PLP REQ | Model/reference + key specs + commercial state (see §11) |
| **PAGINATION** | PLP REQ | Standard result paging |
| **TRUST** | PLP OPT | Certificates · manufacturer status · dealer conditions |

**Forbidden:** Merging FILTERS into PRODUCT_GRID; inventing `SORT_CONTROLS` block_id; AUTO vehicle fields on universal card.

---

## 9. PRODUCT_PAGE Binding

### Required profile zones (typical B2B manufacturer PDP)

| Zone | Treatment | Registry backing |
|------|-----------|------------------|
| Product identity | Model · SKU · series/family | Scaffold-owned (C6) |
| Key specifications | Above-fold spec summary | Scaffold-owned `<dl>` |
| Commercial summary | Price / request price / lead time | Scaffold-owned |
| Primary CTA | Request information · RFQ | `LEAD_FORM` |
| Breadcrumbs | Hierarchy context | `BREADCRUMBS` |

### Recommended profile zones

| Zone | Notes |
|------|-------|
| Full specification groups | Tabbed or grouped `<dl>` — BZPM spec-tabs pattern |
| Trust strip | Warranty · certification hints | `TRUST` · `CERTIFICATES` where applicable |
| Description | Long-form technical copy | Scaffold-owned |
| Documents indicator | Link list or badge — **no** `DOCUMENTS` block_id | Profile policy · composition zone |

### Optional zones

| Zone | Notes |
|------|-------|
| Compare affordance | Profile UX note — not universal PRODUCT_CARD field |
| Related products | No dedicated Registry block — defer |
| Engineering support CTA | Secondary enquiry path |

### Deferred zones

| Zone | Reason |
|------|--------|
| Dedicated media/gallery block | No Registry `block_id` — C6 scaffold-owned placeholder |
| Document download runtime | No `DOCUMENTS` Registry row |
| Inventory backend | CMS/runtime — out of profile scope |

---

## 10. FILTERS Priorities

Facet applicability for MANUFACTURER PLP (profile code set):

| Facet / dimension | Code | Notes |
|-------------------|------|-------|
| dimensions | **REC** | Common for equipment |
| material | **REC** | When product class uses materials |
| capacity | **REC** | Volume / throughput classes |
| performance | **REC** | Power · speed · output |
| installation type | **OPT** | Built-in · freestanding · wall |
| configuration | **OPT** | Variant axes inside facet groups |
| availability | **REC** | Stock · lead time · made to order |
| series | **REC** | Line / family narrowing |
| price range | **OPT** | When fixed price catalog exists |
| make / model / year | **N/A** | AUTO-specific — forbidden on MANUFACTURER universal binding |

**Legend:** REQ = required for typical profile QA · REC = recommended · OPT = optional · N/A = not applicable

Not all REC facets are mandatory on every PLP — project HITL selects subset.

---

## 11. PRODUCT_CARD Priorities

| Field priority | Rank | Universal? |
|----------------|------|------------|
| model / reference (SKU · article) | **1** | Profile emphasis — universal card supports identity slot |
| key technical attributes (2–4 specs) | **2** | Profile emphasis |
| commercial state (price · request price · lead time) | **3** | Profile emphasis |
| availability or production term | **4** | Profile emphasis |
| primary detail action | **5** | Universal pattern |
| request-price support | **6** | MANUFACTURER commercial policy |
| thumbnail / product image | **Present** | Universal minimum |

AUTO fields (mileage · VIN · body type) **forbidden** as MANUFACTURER card requirements.

---

## 12. Attribute Policy

| Attribute class | MANUFACTURER use |
|-----------------|------------------|
| identity attributes | SKU · article · model name · series |
| technical attributes | Rated specs · standards compliance |
| dimensional attributes | W×D×H · weight · connection sizes |
| performance attributes | Capacity · power · throughput |
| material attributes | Steel grade · coating · finish |
| configuration attributes | Options · modules · variants |
| commercial attributes | Price · MOQ · request-price flag |
| document attributes | Datasheet · manual · drawing — **indicator only** until Registry decision |

**Attribute Registry:** possible future system — **not created in WF-R01.3.4 C7**.

---

## 13. Commercial State Policy

| State | MANUFACTURER | Presentation |
|-------|--------------|--------------|
| fixed price | **Supported** | Show numeric price on card/PDP when available |
| request price | **Supported** | Primary B2B path — RFQ CTA |
| made to order | **Supported** | Badge + lead-time note |
| in stock | **Supported** | Availability badge |
| production lead time | **Supported** | Term display · not inventory backend |
| sold / unavailable | **Supported** | Disabled or alternate CTA |
| on request | **Supported** | Neutral commercial copy |

Commercial states are **presentation policy** — not backend inventory systems.

---

## 14. Media Policy

| Media priority | Rank | Runtime |
|----------------|------|---------|
| product overview | **1** | Scaffold-owned placeholder (C6) |
| dimensions | **2** | Profile QA checklist |
| connection points | **3** | Technical catalogue emphasis |
| configuration | **4** | Variant visualization |
| detail views | **5** | Gallery depth note |
| technical diagram | **6** | Composition zone |
| document preview | **7** | Link/badge — no gallery block_id |

**Exclusions:** Gallery runtime not implemented in reference workspace; profile does not change C6 scaffold-owned media status; separate media/gallery contract = future wave decision.

---

## 15. Trust and Documentation Policy

| Trust signal | Canonical identity | Binding |
|--------------|-------------------|---------|
| manufacturer status | `TRUST` | **REC** — badges · copy |
| technical documentation | **No `DOCUMENTS` block_id** | Profile requirement documented · binding **SAFE UNKNOWN** |
| warranty | `TRUST` · `FEATURES` | **REC** |
| certification | `CERTIFICATES` | **REC** when applicable |
| production capability | `TRUST` | **OPT** |
| delivery geography | `TRUST` | **OPT** |
| dealer conditions | `TRUST` | **REC** for dealer-oriented catalogs |
| engineering support | `LEAD_FORM` secondary | **OPT** |

Use only existing Registry identities: `TRUST` · `FEATURES` · `CERTIFICATES`. Do **not** create new block IDs for documents or engineering trust.

---

## 16. CTA and Enquiry Policy

| CTA type | Primary surface | Block |
|----------|-----------------|-------|
| Request price / RFQ | PRODUCT_CARD · PDP commercial zone | `LEAD_FORM` |
| Request information | PDP | `LEAD_FORM` |
| Contact dealer | PDP · optional PLP card | `LEAD_FORM` or link to `CONTACT_PAGE` |
| Add to cart | **N/A default** | ECOMMERCE track — not MANUFACTURER default |

Primary conversion path for MANUFACTURER: **enquiry / RFQ**, not checkout.

---

## 17. Block Binding Matrix

| Canonical block | Binding status | Profile adaptation | Evidence state | Notes |
|-----------------|----------------|--------------------|----------------|-------|
| `FILTERS` | **BOUND** | Technical facet groups · availability · series | **VERIFIED** (C2 partial) | Static reference only |
| `SEARCH` | **BOUND** | Header/catalog discovery | **VERIFIED** (C3 partial) | Form-only — no autocomplete |
| `CATEGORIES` | **BOUND** | Hierarchy navigation · subcat chips | **VERIFIED** (C4A partial) | |
| `CATEGORY_GRID` | **BOUND** | Hub category cards when hub PLP | **VERIFIED** (C4A partial) | |
| `PRODUCT_GRID` | **BOUND** | Spec-dense product listing shell | **VERIFIED** (C4B partial) | |
| `PRODUCT_CARD` | **BOUND** | SKU · specs · RFQ commercial | **VERIFIED** (C4B partial) | |
| `BREADCRUMBS` | **BOUND** | Deep hierarchy | **VERIFIED** (C5 scaffold) | Tier B partial |
| `PAGINATION` | **BOUND** | Standard PLP paging | **VERIFIED** (C5 scaffold) | Tier B partial |
| `LEAD_FORM` | **BOUND** | RFQ / request information | **VERIFIED** (C6 scaffold) | CATALOG applicable |
| `TRUST` | **BOUND** | Certificates · warranty · dealer | **VERIFIED** (Registry + partial) | POL on PLP |
| `CERTIFICATES` | **OPTIONAL** | Certification strip | **VERIFIED** (Registry row) | Use when product class requires |
| `FEATURES` | **OPTIONAL** | Warranty/feature bullets | **VERIFIED** (Registry row) | PDP support content |

---

## 18. Page-Type Binding Matrix

| Page type | Binding | Priority | Notes |
|-----------|---------|----------|-------|
| `CATEGORY_PAGE` | **PRIMARY** | **P1** | Full PLP stack — C7 primary scope |
| `PRODUCT_PAGE` | **PRIMARY** | **P1** | Minimal PDP + profile zone priorities |
| `HOME_PAGE` | **CONTEXTUAL** | Handoff | Catalog entry — not fully designed in C7 |
| `SERVICE_PAGE` | **CONTEXTUAL** | Handoff | Support/services adjacent to catalog |
| `CONTACT_PAGE` | **CONTEXTUAL** | Handoff | Dealer contact destination |

---

## 19. Required / Recommended / Optional

| Concern | Required | Recommended | Optional | Deferred |
|---------|----------|-------------|----------|----------|
| PLP FILTERS | At least one facet group | technical + availability + series | installation · configuration | backend AJAX |
| PLP PRODUCT_CARD | identity + detail action | specs + commercial state | compare hook | cart |
| PDP identity + specs | yes (scaffold-owned) | full spec groups | related products | gallery block_id |
| PDP commercial | commercial summary + CTA | lead time · MOQ | fixed price | inventory sync |
| Trust | — | TRUST + CERTIFICATES | dealer geography | document runtime |
| Media | overview placeholder | dimensions · diagrams | deep gallery | dedicated media block |

---

## 20. Runtime Exclusions

MANUFACTURER profile binding **does not** authorize:

- OpenCart / CMS filter resolver ports
- AJAX faceted search backends
- Inventory or ERP integration
- Document download CMS modules
- Client-specific ZPM theme reproduction
- Automatic production site generation

---

## 21. SAFE UNKNOWN

| Item | State |
|------|-------|
| Dedicated `DOCUMENTS` block_id | **SAFE UNKNOWN** — profile documents need; no Registry row |
| Engineering drawing gallery runtime | **SAFE UNKNOWN** — composition zone only |
| Related products block | **SAFE UNKNOWN** — no Registry row |
| Compare feature runtime | **DEFERRED** — UX note only |
| Live TEST URL fidelity | **Not required** — repo evidence sufficient |

---

## 22. Reuse Rules

**Allowed consumers:** future scaffold planning · composition field selection · filter/card field QA · PDP emphasis checklists · source-evaluation criteria.

**Forbidden uses:** automatic production generator · complete design brief without HITL · CMS/database schema · implementation without review · production-readiness proof · G2 closure claim.

---

## 23. Evidence Paths

| Class | Path |
|-------|------|
| Primary source proxy | `projects/ocpilot/sites/site-002/` (SRC-BZPM-002) |
| Inventory authority | `projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md` |
| Wave C1 vertical evidence | `reports/wf-r01-3-4-wave-c1-catalog-reference-inventory-v1.md` §15 |
| Reference partials | `workspaces/website-factory-reference-v1/src/partials/` (FILTERS · SEARCH · CATEGORIES · grids · cards) |
| CATEGORY_PAGE scaffold | `workspaces/website-factory-reference-v1/src/pages/category-page-reference.html` |
| PRODUCT_PAGE scaffold | `workspaces/website-factory-reference-v1/src/pages/product-page-reference.html` |
| Compositions | `workspaces/website-factory-reference-v1/page-architecture/CATEGORY-PAGE-REFERENCE-COMPOSITION-v1.md` · `PRODUCT-PAGE-REFERENCE-COMPOSITION-v1.md` |

**Sanitization:** No client brand copy · phones · production URLs · CMS PHP/JS in binding rules.

---

## 24. Decision

**MANUFACTURER Catalog Vertical Profile v1 — PUBLISHED at P1 READY.**

Sufficient verified evidence (SRC-BZPM-002 + Waves C2–C6 reference artefacts) supports reusable profile binding without new Registry identities, page types, or implementation changes in Wave C7.

**Next consumer:** Wave C8 — Exit and G2 Readiness Evaluation (profile inputs only — not G2 closure).
