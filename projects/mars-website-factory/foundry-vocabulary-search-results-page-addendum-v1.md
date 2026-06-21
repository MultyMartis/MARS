# Foundry Vocabulary Canon — SEARCH_RESULTS_PAGE Activation Addendum v1

**Parent charter:** [foundry-vocabulary-canon-charter-v1.md](foundry-vocabulary-canon-charter-v1.md)  
**Authority chain:** [wf-r01-3-g2-r3-search-results-page-authority-reconciliation-charter-v1.md](wf-r01-3-g2-r3-search-results-page-authority-reconciliation-charter-v1.md) **ACCEPTED** · G2-R3 A1 Registry expansion  
**Date:** 2026-06-21  
**Mode:** additive vocabulary authority — **documentation only**

**Honesty boundary:** Promotes `SEARCH_RESULTS_PAGE` from expansion glossary to **registered Page Type (F2)** identity. **Does not** imply scaffold readiness, RSC accrual, or CATALOG SC PASS.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED / ALIGNED** |
| **Activation path** | **G2-R3 A1** — explicit wave authorization (alternative to deferred WF-R01.6 bulk hygiene) |

---

## 2. Activation

| Term | Prior state (Vocabulary Canon F2) | Post-A1 state |
|------|----------------------------------|---------------|
| **`SEARCH_RESULTS_PAGE`** | Expansion vocabulary — glossary-only until WF-R01.6 | **Registered Page Type (F2)** — PAGE-TYPE-REGISTRY-v1 row |

Other expansion vocabulary terms (`PRICING_PAGE`, `BLOG_LISTING_PAGE`, …) remain **glossary-only until WF-R01.6**.

---

## 3. Definitions

### SEARCH_RESULTS_PAGE

**Definition:** Query-driven results listing surface — distinct URL/page role hosting search query context, result summary, product/results grid, and list controls.

**Not:** `CATEGORY_PAGE` variation · taxonomy-bound PLP · embedded search chrome on PLP alone.

### CATEGORY_PAGE distinction

| Aspect | CATEGORY_PAGE | SEARCH_RESULTS_PAGE |
|--------|---------------|---------------------|
| **Binding** | Taxonomy / category hub | User query / search query |
| **Primary listing** | Category-scoped PLP | Query-scoped results |
| **SEARCH block role** | Optional discovery on PLP | **Required** on results host |
| **PC corridor** | **Member** | **Not a member** |
| **CATALOG SC** | Required scaffold | Required scaffold |

### Query state

Query identity display (static fictional query in reference layer) is **scaffold-owned** — no canonical `block_id`. **`SEARCH` block** owns query entry UI.

### Listing state

Result listing semantics owned by **`PRODUCT_GRID`** (+ **`PRODUCT_CARD`**) on the results host per Page-Block Mapping.

### Empty state

Zero-hit / no-results presentation is **scaffold-owned variation** — no registered `EMPTY_STATE` `block_id` at A1.

### Variation relationship

**Not** a state of `CATEGORY_PAGE`. Filtered category PLP = `CATEGORY_PAGE` + `FILTERS` state — separate identity.

---

## 4. Registry Binding

Canonical code: **`SEARCH_RESULTS_PAGE`**  
Registry path: `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md`

**Forbidden aliases as separate rows:** `SEARCH_PAGE` · `RESULTS_PAGE` · `SEARCH_LISTING_PAGE`

---

## 5. Evidence Paths

```text
projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md
projects/mars-website-factory/foundry-vocabulary-search-results-page-addendum-v1.md
workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md
```

---

*Addendum version: v1 · Authority: G2-R3 A1 · T0: 2026-06-21*
