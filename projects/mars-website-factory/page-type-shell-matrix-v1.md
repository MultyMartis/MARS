# Website Factory Page-Type Shell Matrix v1

**Status:** **ACCEPTED**  
**Authority:** WF-R01.3.3 Wave S4  
**Date:** 2026-06-19  
**Parent charter:** [wf-r01-3-3-structural-shell-references-charter-v1.md](wf-r01-3-3-structural-shell-references-charter-v1.md)  
**Shell authority:** [global-shell-contract-v1.md](global-shell-contract-v1.md)  
**Scaffold authority:** [reference-scaffold-contract-v1.md](reference-scaffold-contract-v1.md)

**Classification:** documentation-layer normative matrix

**This matrix is not:** HTML template · scaffold implementation · Registry row · runtime behavior · coverage accrual by itself

**Honesty boundary:** Human-operated normative authority for shell and contextual slot applicability per registered `page_type`. **Not** proof that scaffolds exist for all page types. **Not** FILTERS/SEARCH implementation. **Not** G2 authorization.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **ACCEPTED** |
| **Publication wave** | WF-R01.3.3 Wave S4 — Page-Type Shell Matrix and Scaffold Contract Publication |
| **Consolidates** | WF-R01.3.3 charter §12 · Global Shell Contract §13 · Wave S2 BREADCRUMBS policy · Wave S3 PAGINATION policy |
| **Metrics impact** | **None** — RC **32/32** · RPC **17/32** · RSC **1/10 global; 1/1 LANDING** · SC **LANDING PASS** · PC **1/1 LANDING** unchanged |

---

## 2. Purpose

This matrix defines **shell region and contextual slot applicability** for each registered `page_type` in [PAGE-TYPE-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md).

It establishes:

1. Required, optional, policy-dependent, forbidden, and not-applicable shell surfaces per page type.
2. Separation of global shell (`HEADER_NAV`, `MAIN`, `FOOTER`, nested `LEGAL_LINKS`) from contextual slots (`BREADCRUMBS`, `PAGINATION`).
3. Future policy slots for `SEARCH` and `FILTERS` — **NOT IMPLEMENTED** in WF-R01.3.3; owned by WF-R01.3.4.
4. Binding input for Reference Scaffold validation per [reference-scaffold-contract-v1.md](reference-scaffold-contract-v1.md).

**Out of scope:** partial implementation · scaffold creation · Registry edits · new `page_type` codes · metric accrual.

---

## 3. Applicability Codes

One normative code set — **do not** mix legacy abbreviations in new operator REPORTs.

| Code | Meaning | Operator rule |
|------|---------|---------------|
| **REQ** | Required on reference scaffold when this `page_type` is in scope | Absence is a structural validation **FAIL** unless wave charter documents explicit waiver |
| **OPT** | Optional / minimal | Permitted absence when page-type policy documents minimal layout (e.g. conversion LANDING) |
| **POL** | Policy-dependent | Presence determined by project IA, list semantics, or hub design — must be declared in manifest / composition |
| **FORB** | Forbidden | Presence is a structural validation **FAIL** |
| **N/A** | Not applicable | Surface does not apply to this page type's semantics; absence is expected |

### Legacy crosswalk (charter / early docs only)

| Legacy | Normative v1 |
|--------|--------------|
| **O** (Obligatory) | **REQ** |
| **R** (Recommended) | **POL** (recommended stance documented in POL notes) |
| **P** (Policy-dependent) | **POL** |
| **—** (Not required) | **N/A** or **FORB** by exact semantics — see matrix notes |
| **OPT** | **OPT** (unchanged) |

---

## 4. Canonical Page-Type Set

Source: [PAGE-TYPE-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md) minimum v1 set (**10** types).

| `page_type` | Canonical name | Industry alias (informative) |
|-------------|----------------|------------------------------|
| `LANDING_PAGE` | Conversion landing | — |
| `HOME_PAGE` | Site home / hub entry | — |
| `SERVICE_PAGE` | Service money page | — |
| `CATEGORY_PAGE` | Category PLP | PLP-like |
| `PRODUCT_PAGE` | Product PDP | PDP-like |
| `ABOUT_PAGE` | About / company | — |
| `CONTACT_PAGE` | Contact hub | — |
| `FAQ_PAGE` | FAQ hub | — |
| `REVIEWS_PAGE` | Reviews / testimonials hub | — |
| `LEGAL_PAGE` | Legal document | — |

**Not in v1 minimum Registry:** `SEARCH_RESULTS_PAGE`, `ARTICLE_PAGE`, `BLOG_PAGE`, standalone `PLP`/`PDP` identities — use `CATEGORY_PAGE` / `PRODUCT_PAGE` when documenting catalog surfaces.

---

## 5. Shell and Contextual Surfaces

### Global shell regions

| Surface | Identity | Notes |
|---------|----------|-------|
| **HEADER_NAV** | F3 Tier A `block_id` | L0 global navigation |
| **MAIN** | Semantic region — **not** a Registry block | Exactly one `<main>` per document |
| **FOOTER** | F3 Tier A `block_id` | Site-level closing shell |
| **LEGAL_LINKS** | F3 Tier A `block_id` | L3 compliance cluster — **nested in FOOTER** when required |

### Contextual slots (Tier B layout-components or future Tier A)

| Surface | Identity | WF-R01.3.3 state |
|---------|----------|------------------|
| **BREADCRUMBS** | F3 Tier B layout-component | Reference partial **BUILT** (Wave S2) — not scaffold |
| **PAGINATION** | F3 Tier B layout-component | Reference partial **BUILT** (Wave S3) — not scaffold |
| **SEARCH slot** | Future Tier A `SEARCH` policy mount | **NOT IMPLEMENTED** — slot policy only |
| **FILTERS slot** | Future Tier A `FILTERS` policy mount | **NOT IMPLEMENTED** — slot policy only |

---

## 6. Page-Type Shell Matrix

**Legend:** REQ · OPT · POL · FORB · N/A — see §3.

| Page type | HEADER_NAV | MAIN | BREADCRUMBS | PAGINATION | FOOTER | LEGAL_LINKS | SEARCH slot | FILTERS slot |
|-----------|------------|------|-------------|------------|--------|-------------|-------------|--------------|
| `LANDING_PAGE` | OPT | REQ | N/A | FORB | REQ | REQ | N/A | N/A |
| `HOME_PAGE` | REQ | REQ | POL | POL | REQ | REQ | POL | N/A |
| `SERVICE_PAGE` | REQ | REQ | POL | N/A | REQ | REQ | N/A | N/A |
| `CATEGORY_PAGE` | REQ | REQ | REQ | REQ | REQ | REQ | POL | POL |
| `PRODUCT_PAGE` | REQ | REQ | REQ | N/A | REQ | REQ | POL | N/A |
| `ABOUT_PAGE` | REQ | REQ | REQ | N/A | REQ | REQ | N/A | N/A |
| `CONTACT_PAGE` | REQ | REQ | POL | N/A | REQ | REQ | N/A | N/A |
| `FAQ_PAGE` | REQ | REQ | POL | POL | REQ | REQ | POL | N/A |
| `REVIEWS_PAGE` | REQ | REQ | POL | POL | REQ | REQ | N/A | N/A |
| `LEGAL_PAGE` | REQ | REQ | POL | N/A | REQ | REQ | N/A | N/A |

### POL notes (binding interpretations)

| Page type | Surface | Stance |
|-----------|---------|--------|
| `LANDING_PAGE` | HEADER_NAV | **OPT (minimal)** — absence permitted only with documented minimal conversion policy |
| `LANDING_PAGE` | BREADCRUMBS | **N/A** — linear conversion surface; hierarchy trail not applicable |
| `LANDING_PAGE` | PAGINATION | **FORB** — list paging forbidden on conversion surface |
| `HOME_PAGE` | BREADCRUMBS | Recommended shallow hub trail — **POL** |
| `HOME_PAGE` | PAGINATION | Only when home exposes paginated grid — **POL** |
| `HOME_PAGE` | SEARCH slot | Query entry in header utility when site has search — **POL**; **not** implementation |
| `SERVICE_PAGE` | BREADCRUMBS | Recommended parent hub link — **POL** |
| `CATEGORY_PAGE` | BREADCRUMBS | Obligatory on PLP reference scaffold — **REQ** (charter O → REQ) |
| `CATEGORY_PAGE` | PAGINATION | Obligatory on PLP — **REQ** (charter O → REQ) |
| `CATEGORY_PAGE` | FILTERS slot | Expected on PLP under WF-R01.3.4 — **POL**; **not** implementation |
| `CATEGORY_PAGE` | SEARCH slot | Catalog search context — **POL**; typically header utility + results routing |
| `PRODUCT_PAGE` | BREADCRUMBS | Category → product trail — **REQ** |
| `PRODUCT_PAGE` | SEARCH slot | Header utility only — **POL** |
| `ABOUT_PAGE` | BREADCRUMBS | Internal corporate page — **REQ** |
| `CONTACT_PAGE` | BREADCRUMBS | Optional shallow trail — **POL** |
| `FAQ_PAGE` | BREADCRUMBS | Help hub — **POL** |
| `FAQ_PAGE` | PAGINATION | Only if FAQ hub is paginated — **POL** |
| `FAQ_PAGE` | SEARCH slot | FAQ/search hub overlap — **POL** |
| `REVIEWS_PAGE` | BREADCRUMBS | Social proof hub — **POL** |
| `REVIEWS_PAGE` | PAGINATION | Paginated review lists — **POL** |
| `LEGAL_PAGE` | BREADCRUMBS | Minimal trail — **POL** |
| `LEGAL_PAGE` | FOOTER / LEGAL_LINKS | Global footer + legal links on **other** routes remain **REQ**; legal document body is not marketing stack — [LEGAL-PAGE-CONTRACT-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/LEGAL-PAGE-CONTRACT-v1.md) |

### Planned / not in Registry v1 minimum (informative only)

When `SEARCH_RESULTS`-class routing is scaffolded under **WF-R01.3.4** (future Registry extension): HEADER_NAV **REQ**, BREADCRUMBS **POL**, PAGINATION **REQ**, FOOTER **REQ**, LEGAL_LINKS **REQ**, SEARCH slot **REQ** in results context, FILTERS slot **POL**. **Not** an active Registry identity in this matrix v1.

---

## 7. Surface Rules

### HEADER_NAV

| Rule | Specification |
|------|---------------|
| Default | **REQ** on all multi-page internal types except minimal `LANDING_PAGE` |
| Minimal LANDING | **OPT** — absence requires explicit page-type policy in manifest |
| Legal-only layouts | Not exempt from global shell on **other** routes; `LEGAL_PAGE` body may simplify — footer policy unchanged on site |
| Mega-menu | Variant inside HEADER_NAV — not separate shell region |

### MAIN

| Rule | Specification |
|------|---------------|
| All registered page types | **MAIN = REQ** — exactly one `<main>` per document |
| Content boundary | Page-specific blocks live inside MAIN only |
| Shell nesting | HEADER_NAV, FOOTER, standalone LEGAL_LINKS **must not** nest inside MAIN |

### BREADCRUMBS

Consolidates Wave S2 policy:

| Rule | Specification |
|------|---------------|
| LANDING | **N/A** — not integrated on LANDING reference |
| PLP / PDP / ABOUT | **REQ** on reference scaffolds when built |
| Other internal types | **POL** unless matrix row specifies **REQ** |
| Identity | Tier B layout-component — ≠ HEADER_NAV — ≠ page title |
| Reference partial | `components/breadcrumbs.html` — bounded host `breadcrumbs-reference.html` ≠ scaffold |

### PAGINATION

Consolidates Wave S3 policy:

| Rule | Specification |
|------|---------------|
| LANDING | **FORB** |
| CATEGORY_PAGE | **REQ** on PLP scaffold |
| HOME / FAQ / REVIEWS | **POL** — only with documented list semantics |
| SERVICE / PRODUCT / ABOUT / CONTACT / LEGAL | **N/A** — not list surfaces |
| Not inferred | PAGINATION **must not** become REQ solely because a page *could* host a list |
| Identity | Tier B — ≠ FILTERS — ≠ carousel — ≠ PROCESS stepper |
| Reference partial | `components/pagination.html` — bounded host `pagination-reference.html` ≠ scaffold |

### FOOTER and LEGAL_LINKS

| Rule | Specification |
|------|---------------|
| FOOTER | **REQ** on all page types in matrix except where OPT minimal LANDING policy documents otherwise for HEADER only — FOOTER remains **REQ** on LANDING reference |
| LEGAL_LINKS | When FOOTER **REQ**, LEGAL_LINKS **REQ** nested in FOOTER |
| Nesting | LEGAL_LINKS **must not** appear as sibling site-level footer |
| FOOTER ≠ LEGAL_LINKS | Footer shell includes secondary nav, contact summary, copyright; LEGAL_LINKS is compliance cluster |

### SEARCH slot (NOT IMPLEMENTED)

| Rule | Specification |
|------|---------------|
| Status | **NOT IMPLEMENTED** — policy mount points only |
| Typical placement | L0 HEADER_NAV utility zone (query entry); L2 MAIN results context on future search results surface |
| CATEGORY / catalog | Catalog search chrome — **POL** on `CATEGORY_PAGE`, `HOME_PAGE`, `FAQ_PAGE`, `PRODUCT_PAGE` |
| Slot ≠ implementation | Documenting **POL** does **not** claim SEARCH partial or RPC credit |

### FILTERS slot (NOT IMPLEMENTED)

| Rule | Specification |
|------|---------------|
| Status | **NOT IMPLEMENTED** — policy mount points only |
| Primary consumer | `CATEGORY_PAGE` — **POL** (expected under WF-R01.3.4) |
| Other types | **N/A** unless future charter assigns facet sidebar policy |
| Slot ≠ implementation | Documenting **POL** does **not** claim FILTERS partial or RPC credit |

---

## 8. Matrix Relationships (Binding)

```text
HEADER_NAV ≠ BREADCRUMBS
BREADCRUMBS ≠ page title
PAGINATION ≠ FILTERS
PAGINATION ≠ SEARCH
SEARCH slot ≠ SEARCH implementation
FILTERS slot ≠ FILTERS implementation tab
FOOTER ≠ LEGAL_LINKS
LEGAL_LINKS nested in FOOTER when FOOTER required
MAIN is a semantic region, not a Registry block
Bounded component host ≠ Reference Scaffold
Shell Contract ≠ Scaffold
This matrix ≠ Scaffold
```

This matrix **does not** create: partial · scaffold · RSC · SC · PC · runtime behavior.

---

## 9. Scaffold Validation Binding

Reference scaffolds **must** conform to this matrix plus [global-shell-contract-v1.md](global-shell-contract-v1.md) and [reference-scaffold-contract-v1.md](reference-scaffold-contract-v1.md).

Minimum checks derived from matrix:

| Check | Source |
|-------|--------|
| HEADER_NAV count | Matrix row for active `page_type` |
| MAIN count | Exactly **1** — all types |
| FOOTER / LEGAL_LINKS | Matrix row + nesting rule |
| BREADCRUMBS presence | REQ / POL / N/A / FORB per row |
| PAGINATION presence | REQ / POL / N/A / FORB per row |
| SEARCH / FILTERS slots | Policy notes only until WF-R01.3.4 |
| Forbidden surfaces | Absent on scaffold |

---

## 10. Coverage Accounting

| Action | RC | RPC | RSC | SC | PC |
|--------|----|----|-----|----|-----|
| Publish Page-Type Shell Matrix (S4) | **No** | **No** | **No** | **No** | **No** |

Current metrics (unchanged at S4):

| Dimension | Value |
|-----------|-------|
| **RC** | **32/32** |
| **RPC** | **17/32** |
| **RSC** | **1/10 global · 1/1 LANDING** |
| **SC** | **LANDING PASS** |
| **PC** | **1/1 LANDING** |

---

## 11. Relationship to Future Waves

| Wave | Relationship |
|------|--------------|
| **S4** | **This matrix** — publication complete |
| **S5** | Exit evaluation · handoff package includes this matrix + scaffold contract |
| **WF-R01.3.4** | FILTERS / SEARCH implementation · catalog scaffolds · may extend POL notes — **not** new matrix v1 rows without Registry charter |

---

## 12. Evidence Paths

| Artefact | Path |
|----------|------|
| This matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` |
| WF-R01.3.3 charter | `projects/mars-website-factory/wf-r01-3-3-structural-shell-references-charter-v1.md` |
| Wave S2 REPORT | `reports/wf-r01-3-3-wave-s2-breadcrumbs-v1.md` |
| Wave S3 REPORT | `reports/wf-r01-3-3-wave-s3-pagination-v1.md` |
| Wave S4 REPORT | `reports/wf-r01-3-3-wave-s4-shell-matrix-scaffold-contract-v1.md` |
| Page type registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` |
| LANDING scaffold (evidence) | `workspaces/website-factory-reference-v1/LANDING-SCAFFOLD-MANIFEST-v1.md` |

---

## 13. Decision

| Field | Value |
|-------|-------|
| **Decision** | **ACCEPTED** — Website Factory Page-Type Shell Matrix v1 is normative operator authority for shell and contextual slot applicability |
| **Wave** | WF-R01.3.3 Wave S4 — matrix publication |
| **Metrics** | **UNCHANGED** |
| **Next task** | **WF-R01.3.3 Wave S5 — Exit Evaluation and WF-R01.3.4 Handoff** |

---

*Matrix version: v1 · Authority: WF-R01.3.3 Wave S4 · T0: 2026-06-19*
