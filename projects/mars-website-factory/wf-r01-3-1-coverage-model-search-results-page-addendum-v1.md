# WF-R01.3.1 Coverage Model — SEARCH_RESULTS_PAGE Addendum v1

**Parent charter:** [wf-r01-3-1-coverage-model-charter-v1.md](wf-r01-3-1-coverage-model-charter-v1.md)  
**Authority chain:** [wf-r01-3-g2-r3-search-results-page-authority-reconciliation-charter-v1.md](wf-r01-3-g2-r3-search-results-page-authority-reconciliation-charter-v1.md) **ACCEPTED** · [wf-r01-3-g2-r3-a1-search-results-registry-matrix-expansion-v1.md](wf-r01-3-g2-r3-a1-search-results-registry-matrix-expansion-v1.md)  
**Date:** 2026-06-21  
**Mode:** additive coverage authority — **documentation only**

**Honesty boundary:** This addendum **authorizes** RSC denominator reconciliation for `SEARCH_RESULTS_PAGE` Registry registration. **Does not** accrue RSC numerator, **does not** declare CATALOG SC PASS, **does not** create scaffold evidence.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED / ALIGNED** |
| **Parent Coverage Model** | **ACCEPTED** — unchanged except where this addendum explicitly amends |
| **Trigger** | G2-R3 A1 Registry expansion — `SEARCH_RESULTS_PAGE` registered in PAGE-TYPE-REGISTRY-v1 |

---

## 2. Problem Reconciled

Coverage Model § Template-Art minimum sets (CATALOG) **normatively lists** `` `SEARCH_RESULTS_PAGE` `` as required scaffold **before** PAGE-TYPE-REGISTRY-v1 minimum-10 row existed. G2-R3 charter §19 flagged **SAFE UNKNOWN** for global RSC denominator when expansion exceeds minimum 10.

This addendum **resolves** that SAFE UNKNOWN without rewriting the parent Coverage Model charter.

---

## 3. RSC Denominator Amendment (Binding)

### Global RSC denominator

| Phase | Denominator | Source |
|-------|-------------|--------|
| **Pre–G2-R3 A1** | **10** | PAGE-TYPE-REGISTRY-v1 minimum set |
| **Post–G2-R3 A1 registration** | **11** | Minimum 10 + registered expansion row `SEARCH_RESULTS_PAGE` |

**Rule:** Global RSC denominator equals the count of **registered** `page_type` rows in PAGE-TYPE-REGISTRY-v1 that are **RSC-eligible** (all registered Core page types unless explicitly waived by future charter).

**Binding interpretation:** Reference Scaffold Contract binding to **registered `page_type` denominator** applies. Registry row registration **expands** global RSC denominator **upon publication** — not upon scaffold completion.

### WF-R01.3 G2 baseline note

The historical **6/10** notation remains valid **only** for pre-A1 REPORTs. Post-A1 operator REPORTs **must** use **6/11** until numerator changes.

---

## 4. SEARCH_RESULTS_PAGE Coverage Contract

| Field | Value |
|-------|-------|
| **Registry status** | **REGISTERED / UNSCAFFOLDED** |
| **RSC eligibility** | **Yes** — counts in global RSC denominator |
| **RSC numerator accrual** | **No** until validated Reference Scaffold per Reference Scaffold Contract §18 |
| **CATALOG SC role** | **Required** — CATALOG minimum scaffold set (parent Coverage Model L222) |
| **CATALOG PC corridor** | **Excluded** — PC corridor remains `CATEGORY_PAGE` → `PRODUCT_PAGE` only |
| **Accrual timing** | **+1 RSC numerator** only after A3 scaffold validation chain — **not** at registration |
| **No-double-count** | Registration row ≠ scaffold evidence; partial blocks already in RPC are not re-counted |

---

## 5. Earned Numerator Rule (Frozen at A1)

| Dimension | Pre-A1 | Post-A1 | Delta |
|-----------|--------|---------|-------|
| **RSC numerator (earned)** | **6** | **6** | **0** |
| **RSC denominator** | **10** | **11** | **+1** |
| **RSC notation** | **6/10** | **6/11** | denominator only |
| **RC** | **32/32** | **32/32** | **0** |
| **RPC** | **26/32** | **26/32** | **0** |
| **SC CATALOG** | **PARTIAL** | **PARTIAL** | unchanged |
| **PC CATALOG corridor** | **1/1** | **1/1** | unchanged |

---

## 6. Per-Site-Type RSC Note

For **CATALOG** site-type expansion waves, the **required scaffold set** includes:

```text
CATEGORY_PAGE
PRODUCT_PAGE
SEARCH_RESULTS_PAGE
```

Global RSC notation remains **one denominator across all registered page types** — not a separate CATALOG-only fraction in operator REPORTs unless explicitly declared.

---

## 7. Relationship to WF-R01.6

WF-R01.6 remains **preferred** owner for bulk Registry hygiene. This addendum **does not** supersede WF-R01.6 for maturity attributes or unrelated expansion types. It **only** reconciles denominator behavior for the **single** G2-R3-authorized `SEARCH_RESULTS_PAGE` row.

---

## 8. Evidence Paths

```text
projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md
projects/mars-website-factory/wf-r01-3-1-coverage-model-search-results-page-addendum-v1.md
projects/mars-website-factory/reference-scaffold-contract-v1.md
projects/mars-website-factory/wf-r01-3-g2-r3-search-results-page-authority-reconciliation-charter-v1.md
workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md
```

---

*Addendum version: v1 · Authority: G2-R3 A1 · T0: 2026-06-21*
