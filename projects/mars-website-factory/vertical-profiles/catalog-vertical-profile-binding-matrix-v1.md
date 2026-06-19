# Catalog Vertical Profile Binding Matrix v1

**Subprogram:** WF-R01.3.4 — Catalog & Vertical Profile References  
**Wave:** C7 — Vertical Profile Binding  
**Version:** v1  
**Date:** 2026-06-20  
**Status:** **PUBLISHED**

**Honesty boundary:** Cross-profile binding authority only. **Not** implementation. **Not** coverage accrual. **Not** G2 activation. **Not** CATALOG SC PASS.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Document status** | **PUBLISHED** |
| **Wave** | **C7 COMPLETE** (documentation) |
| **Profiles bound** | MANUFACTURER (**P1 READY**) · AUTO (**P2 PARTIAL**) |
| **Coverage metrics** | **UNCHANGED** |
| **CATALOG SC** | **PARTIAL** (unchanged — C8 evaluation pending) |
| **G2 overall** | **NOT ACTIVE / NOT CLOSED** |

---

## 2. Authority

| Document | Path | Role |
|----------|------|------|
| WF-R01.3.4 Charter | `projects/mars-website-factory/wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md` | Vertical Profile Policy §13 |
| Catalog Reference Inventory | `projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md` | Evidence classification |
| MANUFACTURER profile | `projects/mars-website-factory/vertical-profiles/manufacturer-catalog-profile-v1.md` | P1 binding |
| AUTO profile | `projects/mars-website-factory/vertical-profiles/auto-catalog-profile-v1.md` | P2 binding |
| Coverage Model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | SC/PC/RSC boundaries |
| Vocabulary Canon | `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` | F1–F6 unchanged |
| Block Registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | Canonical identities |
| Page-Type Registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` | Registered page types only |

---

## 3. Universal Contract

### Definition

```text
Vertical Profile = documented binding layer that adapts canonical Website Factory
references to recurring business-domain requirements.
```

### Universal catalog contract (immutable in C7)

| Target | Universal responsibility |
|--------|-------------------------|
| `FILTERS` | Faceted narrowing on listing surfaces — static reference |
| `SEARCH` | Catalog discovery form — not autocomplete backend |
| `CATEGORIES` | Taxonomy navigation — not facet logic |
| `CATEGORY_GRID` | Category hub card grid |
| `PRODUCT_GRID` | Product listing shell |
| `PRODUCT_CARD` | Listing card minimum + bounded variation hooks |
| `CATEGORY_PAGE` | PLP scaffold + composition |
| `PRODUCT_PAGE` | PDP scaffold + composition (minimal mode) |

### Universal contract lock table

| Canonical target | Universal responsibility | Vertical adaptation allowed | Forbidden adaptation |
|------------------|-------------------------|----------------------------|----------------------|
| `FILTERS` | Facet UI shell · static states | Facet group selection · label priority · industry dimensions inside block | New block_id · AJAX backend · merge into grid |
| `SEARCH` | Header/form discovery | Placeholder copy · scope hints | Autocomplete API · new SEARCH variant id |
| `CATEGORIES` | Nav tree / chips | Hierarchy depth notes · hub emphasis | Category = filter conflation |
| `CATEGORY_GRID` | Hub cards | Card field emphasis | Rename to CATALOG_GRID |
| `PRODUCT_GRID` | Listing container | Layout density notes | Embed card markup without PRODUCT_CARD |
| `PRODUCT_CARD` | Card anatomy minimum | Field priority overlays per profile | Profile-only fields as universal REQ |
| `CATEGORY_PAGE` | PLP shell stack | Block ordering within MAIN policy | New page type · shell redefinition |
| `PRODUCT_PAGE` | PDP shell + scaffold zones | Zone emphasis · trust/commercial policy | New gallery block_id in C7 |
| Shell partials | HEADER_NAV · FOOTER · BREADCRUMBS · PAGINATION | Integration only | Shell contract rewrite |
| Coverage dimensions | RC · RPC · RSC · SC · PC accounting | **None** | Profile doc accrual · SC PASS claim |

Vertical Profile **is not:** new site type · new page type · new block family · new Registry · design system · CMS module · runtime · production template.

---

## 4. Profile Status Model

| Status | Meaning |
|--------|---------|
| **P1 READY** | Sufficient verified evidence for reusable profile binding |
| **P2 PARTIAL** | Useful structural evidence; some fields/behaviors prototype-only or unverified |
| **SAFE UNKNOWN** | Insufficient evidence for binding claim |
| **DEFERRED** | Intentionally outside current programme scope |

**Rule:** Do **not** use `COMPLETE` for vertical profile unless referring to documentation wave completion — not runtime implementation.

| Profile | Status |
|---------|--------|
| **MANUFACTURER** | **P1 READY** |
| **AUTO** | **P2 PARTIAL** |

---

## 5. Cross-Profile Matrix

| Concern | Universal | MANUFACTURER | AUTO |
|---------|-----------|--------------|------|
| Category hierarchy | Taxonomy via `CATEGORIES` + breadcrumbs | type → family → series → model/SKU | make → model → year (prototype) |
| FILTERS | Facet shell | Technical · availability · series (**REC**) | make · model · year · price · mileage (**VERIFIED/PARTIAL**) |
| SEARCH | Form discovery | Standard | Standard |
| PRODUCT_CARD | Identity · image · detail action | SKU · specs · RFQ commercial | make · year · mileage · price (**profile-only**) |
| Commercial state | Presentation labels only | request price · lead time · MOQ | fixed price · sold (**PARTIAL**) |
| Availability | Badge/copy | production lead time · in stock | in stock · sold (**PARTIAL**) |
| Media | Scaffold placeholder (PDP) | technical diagrams (**composition**) | hero photo (**PARTIAL**) |
| Specifications | Scaffold-owned PDP zones | full spec groups (**REC**) | configuration summary (**PARTIAL**) |
| Trust | `TRUST` · `CERTIFICATES` optional | warranty · certs · dealer (**REC**) | dealer strip (**PARTIAL**) |
| Documents | **No block_id** | indicator policy · **SAFE UNKNOWN** | **N/A typical** |
| CTA/enquiry | `LEAD_FORM` | RFQ / request information | contact dealer (**VERIFIED** prototype) |
| Runtime | **None in reference** | **Forbidden** | **Forbidden** — live OC **UNVERIFIED** |

**Universalization guardrail:** AUTO vehicle fields **must not** migrate to universal PRODUCT_CARD/FILTERS requirements.

---

## 6. Block Binding Matrix

Summary across profiles (detail in profile docs §17):

| Canonical block | Universal | MANUFACTURER | AUTO |
|-----------------|-----------|--------------|------|
| `FILTERS` | PLP contract | **BOUND** P1 | **BOUND partial** P2 |
| `SEARCH` | Discovery | **BOUND** P1 | **BOUND** |
| `CATEGORIES` | Nav | **BOUND** P1 | **OPTIONAL** P2 |
| `CATEGORY_GRID` | Hub | **BOUND** P1 | **OPTIONAL** P2 |
| `PRODUCT_GRID` | Listing | **BOUND** P1 | **BOUND partial** P2 |
| `PRODUCT_CARD` | Card | **BOUND** P1 | **BOUND partial** P2 |
| `BREADCRUMBS` | PLP/PDP | **BOUND** | **BOUND** |
| `PAGINATION` | PLP | **BOUND** | **BOUND** |
| `LEAD_FORM` | CTA | **BOUND** RFQ | **BOUND** enquiry |
| `TRUST` | Trust | **REC** | **OPTIONAL partial** |
| `CERTIFICATES` | Trust | **OPT** | **SAFE UNKNOWN** |
| `FEATURES` | Info | **OPT** warranty | **Rare** |

No new `block_id` rows created in C7.

---

## 7. Page-Type Binding Matrix

| Page type | MANUFACTURER | AUTO | Binding status |
|-----------|--------------|------|----------------|
| `CATEGORY_PAGE` | **PRIMARY** — full PLP policy | **PRIMARY partial** — prototype PLP | **C7 scope** |
| `PRODUCT_PAGE` | **PRIMARY** — spec/commercial emphasis | **PRIMARY partial** — hero/commercial | **C7 scope** |
| `HOME_PAGE` | Contextual handoff | Contextual handoff | **Not designed in C7** |
| `SERVICE_PAGE` | Contextual handoff | Contextual handoff | **Not designed in C7** |
| `CONTACT_PAGE` | Dealer/contact destination | Dealer contact | **Not designed in C7** |
| `SEARCH_RESULTS_PAGE` | **Not in Page-Type Registry** | **Not in Page-Type Registry** | **Authority gap → C8** |

---

## 8. Attribute Comparison

| Attribute class | MANUFACTURER | AUTO | Universalization decision |
|-----------------|--------------|------|-------------------------|
| identity | SKU · model · series | make · model · trim | **Profile-specific** — no universal merge |
| technical / performance | rated specs | engine · powertrain | **Profile-specific** |
| dimensional | W×D×H | body type | **Profile-specific** |
| condition / usage | availability terms | mileage · condition | **Profile-specific** |
| configuration | modules · options | transmission · drive | **Profile-specific** |
| commercial | RFQ · lead time | list price | **Profile-specific** |
| document | datasheet indicator | N/A typical | **SAFE UNKNOWN** globally |
| dealer-programme | dealer terms | credit · trade-in | **SAFE UNKNOWN** — not universal |

**Attribute Registry:** possible future system — **not created in WF-R01.3.4 C7**.

---

## 9. Commercial State Comparison

| State | Universal support | MANUFACTURER | AUTO | Runtime needed |
|-------|-------------------|--------------|------|----------------|
| fixed price | Presentation | **Supported** | **Supported (PARTIAL)** | Yes for live pricing — **out of scope** |
| request price | Presentation | **Primary path** | N/A typical | CRM/backend — **out of scope** |
| available | Presentation | in stock · lead time | in stock (**PARTIAL**) | Inventory — **out of scope** |
| made to order | Presentation | **Supported** | N/A typical | ERP — **out of scope** |
| lead time | Presentation | **Supported** | N/A typical | — |
| sold / unavailable | Presentation | **Supported** | **PARTIAL** | — |
| on request | Presentation | **Supported** | OPT | — |
| credit / finance | **Not universal** | N/A | **SAFE UNKNOWN** | Finance API — **forbidden in C7** |
| trade-in | **Not universal** | N/A | **SAFE UNKNOWN** | — |
| reservation | **Not universal** | DEFERRED | **DEFERRED** | Payment — **forbidden in C7** |

Commercial states = **presentation policy** only.

---

## 10. Trust and Media Comparison

| Concern | Universal | MANUFACTURER | AUTO |
|---------|-----------|--------------|------|
| Trust blocks | `TRUST` · `CERTIFICATES` · `FEATURES` | certs · warranty · dealer (**REC**) | dealer strip (**PARTIAL**) |
| Documents | No `DOCUMENTS` block_id | indicator · **SAFE UNKNOWN** | N/A |
| PDP media | Scaffold-owned placeholder | diagrams · dimensions priority | hero · partial gallery |
| Gallery runtime | **Not implemented** | Deferred | Deferred |
| Trust backend | **Forbidden** | — | — |

---

## 11. Universalization Guardrails

1. Profile-specific fields **must not** become universal `PRODUCT_CARD` or `FILTERS` requirements without charter amendment.
2. Vertical profiles **must not** create `site_type_code` · page types · `block_id` rows.
3. Scaffold-owned PDP zones **must not** be reclassified as new canonical blocks in C7.
4. AUTO P2 evidence **must not** be cited as production validation.
5. MANUFACTURER B2B patterns **must not** be forced onto AUTO projects or vice versa.
6. Coverage metrics **must not** increase due to profile publication.
7. CATALOG SC **must not** auto-pass when profiles publish.

---

## 12. Evidence Limitations

| Profile | Limitation |
|---------|------------|
| **MANUFACTURER** | Document/gallery runtime gaps; no live TEST dependency for binding |
| **AUTO** | Prototype-only; live OC **UNVERIFIED**; credit/trade-in **SAFE UNKNOWN** |
| **Both** | No new client audit in C7; C1/C5/C6 evidence reused |
| **Enrollment** | BZPM/SIBCAR Factory enrollment remains **Pending** per charter |

### Source provenance classes

| Class | Use in C7 |
|-------|-----------|
| verified local execution evidence | MANUFACTURER primary |
| sanitized reference implementations | Universal partials C2–C6 |
| approved prototypes | AUTO primary |
| published Website Factory references | Contract baseline |

Client names appear **only** in evidence path sections — not in normative profile rules.

---

## 13. Coverage Boundary

Wave C7 documentation **does not change:**

```text
RC = 32/32
RPC = 23/32
RSC = 3/10 global
  - LANDING_PAGE = 1/1
  - CATEGORY_PAGE = 1/1
  - PRODUCT_PAGE = 1/1
SC:
  - LANDING = PASS
  - CATALOG = PARTIAL
PC:
  - LANDING corridor = 1/1
  - CATALOG corridor = 1/1
```

Vertical Profile documents: **do not add RPC · RSC · PC · SC dimension**.

C7 closes documentation gap: **vertical profile binding** — not CATALOG SC PASS.

---

## 14. C8 Handoff

**Next wave:** WF-R01.3.4 Wave C8 — Exit and G2 Readiness Evaluation

### Inputs for C8

| Input | State |
|-------|-------|
| MANUFACTURER profile | **P1 READY** — published |
| AUTO profile | **P2 PARTIAL** — published with limitations |
| Cross-profile matrix | **PUBLISHED** (this document) |
| Universal catalog references | Waves C2–C6 **COMPLETE** |
| Coverage metrics | **UNCHANGED** |
| CATALOG SC | **PARTIAL** — formal C8 evaluation required |
| G2 RPC criterion | **SATISFIED** (23/32 ≥ 20/32) |
| G2 overall | **NOT ACTIVE / NOT CLOSED** |

### Remaining gaps for C8

1. **CATALOG SC PASS** — not granted; evaluate against Coverage Model minimum set
2. **SEARCH_RESULTS_PAGE authority conflict** — Coverage Model mentions scaffold; Page-Type Registry has **no row** — reconciliation required
3. **G2 remaining criteria** — beyond RPC floor (structural T1+ completeness · catalog corridor evidence · gate REPORT)
4. **WF-R01.3.4 exit** — subprogram closure decision
5. **AUTO enrollment** — post–G2 per charter; not C7 scope

### C8 evaluation questions (non-exhaustive)

- Does published catalog reference set satisfy CATALOG SC minimum?
- Is SEARCH_RESULTS_PAGE a registry gap or coverage-model drift?
- Can G2 become ACTIVE without false production claims?
- Are vertical profiles sufficient for handoff to WF-R01.3.5 / enrollment decisions?

**C8 execution:** **NOT STARTED** in Wave C7.

---

## 15. Evidence Paths

| Artefact | Path |
|----------|------|
| MANUFACTURER profile | `projects/mars-website-factory/vertical-profiles/manufacturer-catalog-profile-v1.md` |
| AUTO profile | `projects/mars-website-factory/vertical-profiles/auto-catalog-profile-v1.md` |
| This matrix | `projects/mars-website-factory/vertical-profiles/catalog-vertical-profile-binding-matrix-v1.md` |
| C1 inventory | `projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md` |
| C1 REPORT | `reports/wf-r01-3-4-wave-c1-catalog-reference-inventory-v1.md` |
| C5 REPORT | `reports/wf-r01-3-4-wave-c5-category-page-scaffold-v1.md` |
| C6 decision | `projects/mars-website-factory/wf-r01-3-4-product-page-scope-decision-v1.md` |
| C6 REPORT | `reports/wf-r01-3-4-wave-c6-product-page-decision-v1.md` |
| SRC-BZPM-002 | `projects/ocpilot/sites/site-002/` |
| SRC-SIBCAR-001 | `workspaces/site-001-wf-v3/` |
| Reference workspace | `workspaces/website-factory-reference-v1/` |
| Wave C7 REPORT | `reports/wf-r01-3-4-wave-c7-vertical-profile-binding-v1.md` |

---

## 16. Decision

**Catalog Vertical Profile Binding Matrix v1 — PUBLISHED.**

Wave C7 documentation objectives satisfied:

- Vertical Profile defined and bounded
- MANUFACTURER + AUTO bindings published at honest status levels
- Universal contract locked
- Cross-profile · block · page-type matrices published
- Coverage unchanged · CATALOG SC remains PARTIAL
- C8 handoff prepared

**Forbidden claims:** WF-R01.3.4 COMPLETE · CATALOG SC PASS · G2 ACTIVE · G2 CLOSED · AUTO P1 READY · production-ready · vertical profiles implemented in runtime.
