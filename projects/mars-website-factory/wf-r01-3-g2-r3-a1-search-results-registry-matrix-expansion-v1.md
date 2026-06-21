# WF-R01.3 G2-R3 A1 SEARCH_RESULTS_PAGE Registry and Matrix Expansion v1

**Remediation wave:** **G2-R3 A1**  
**Parent charter:** [wf-r01-3-g2-r3-search-results-page-authority-reconciliation-charter-v1.md](wf-r01-3-g2-r3-search-results-page-authority-reconciliation-charter-v1.md) **ACCEPTED**  
**Date:** 2026-06-21  
**Mode:** authority / registry / matrix expansion — **documentation only**

**Honesty boundary:** A1 **registers** `SEARCH_RESULTS_PAGE` and aligns matrices. **Does not** create scaffold, **does not** accrue RSC numerator, **does not** declare CATALOG SC PASS, **does not** execute A2/A3.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED / ALIGNED** |
| **Outcome** | **OUTCOME A — ALIGNED EXPANSION COMPLETE** |
| **Package state** | G2-R3 **A1 COMPLETE** · package **NOT COMPLETE** |
| **Implementation** | Registry + matrices aligned · scaffold **ABSENT** |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Wave ID** | **G2-R3 A1** |
| **Canonical page type** | **`SEARCH_RESULTS_PAGE`** |
| **Parent gate** | **G2** |
| **Predecessor** | G2-R3 charter pass **ACCEPTED** |
| **Successor** | **G2-R3 A2 — SEARCH_RESULTS_PAGE Reference Preflight** |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| G2-R3 charter | [wf-r01-3-g2-r3-search-results-page-authority-reconciliation-charter-v1.md](wf-r01-3-g2-r3-search-results-page-authority-reconciliation-charter-v1.md) | Option A · A1 wave authorization §25 |
| G2-R3 charter pass | [wf-r01-3-g2-r3-search-results-authority-charter-pass-v1.md](../../reports/wf-r01-3-g2-r3-search-results-authority-charter-pass-v1.md) | Authority outcome B |
| G2 formal gate charter | [wf-r01-3-g2-formal-gate-pass-charter-v1.md](wf-r01-3-g2-formal-gate-pass-charter-v1.md) | G2-11 · G2-21 · SEARCH policy §17 |
| Coverage Model | [wf-r01-3-1-coverage-model-charter-v1.md](wf-r01-3-1-coverage-model-charter-v1.md) | CATALOG minimum scaffolds L222 |
| Coverage addendum | [wf-r01-3-1-coverage-model-search-results-page-addendum-v1.md](wf-r01-3-1-coverage-model-search-results-page-addendum-v1.md) | Denominator reconciliation |
| Vocabulary Canon | [foundry-vocabulary-canon-charter-v1.md](foundry-vocabulary-canon-charter-v1.md) | F2 expansion vocabulary |
| Vocabulary addendum | [foundry-vocabulary-search-results-page-addendum-v1.md](foundry-vocabulary-search-results-page-addendum-v1.md) | Glossary → registered promotion |
| Reference Scaffold Contract | [reference-scaffold-contract-v1.md](reference-scaffold-contract-v1.md) | RSC accrual · registered denominator |
| Global Shell Contract | [global-shell-contract-v1.md](global-shell-contract-v1.md) | Planned shell note (informative input) |
| Page-Type Shell Matrix | [page-type-shell-matrix-v1.md](page-type-shell-matrix-v1.md) | Shell row mutation target |
| PAGE-TYPE-REGISTRY | [PAGE-TYPE-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md) | Registry mutation target |
| PAGE-BLOCK-MAPPING | [PAGE-BLOCK-MAPPING-v1.md](../../workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md) | Block stance mutation target |
| SITE-TYPE-BLOCK-MATRIX | [SITE-TYPE-BLOCK-MATRIX-v2.md](../../workspaces/website-factory-reference-v1/block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md) | CATALOG cross-reference |

---

## 4. Scope

### In scope (executed)

- Mutation authority audit
- RSC denominator decision + Coverage addendum
- Vocabulary activation addendum
- PAGE-TYPE-REGISTRY row (one)
- Shell Matrix row
- Page-Block Mapping promotion (planned → normative)
- Site-Type Block Matrix cross-reference
- Coverage accounting reconciliation
- A2 readiness determination

### Out of scope (forbidden)

- Scaffold · composition · manifest · HTML/SCSS/JS
- RSC numerator accrual
- CATALOG SC PASS
- G2 evaluation · G2 PASS
- A2 · A3 · G2-R4 execution

---

## 5. Duplicate Check

| Check | Result |
|-------|--------|
| Existing Registry row | **None** before A1 |
| Draft Registry row | **None** |
| Accepted denominator addendum | **None** before A1 — **created in A1** |
| Competing matrix row | Planned/glossary only — **promoted** |
| WF-R01.6 deferred task | WF-R01.6 **DESIGN** — G2-R3 A1 **explicit authorized alternative** |
| Prior A1 artefact | **None** |

**Decision:** Proceed — no duplicate registration.

---

## 6. Mutation Authority

| Authority source | Allows mutation | Requires addendum | Defers to WF-R01.6 | Notes |
| ---------------- | --------------- | ----------------- | ------------------ | ----- |
| G2-R3 charter §19 · §25 | **Yes** — A1 wave | Denominator: **Yes** | **Preferred** not mandatory | A1 explicitly listed |
| G2 charter §17 · §21 | **Yes** — via G2-R3 | Coverage if denominator changes | Partial — page-type creation territory | G2-21 requires explicit wave |
| Coverage Model v1 | **Indirect** — lists scaffold | **Yes** for 10→11 | No | CATALOG L222 pre-registers requirement |
| Reference Scaffold Contract | **Yes** — registered denominator | Align with Coverage | No | Binding to Registry count |
| Vocabulary Canon | **Glossary-only until WF-R01.6** | **Vocabulary addendum** | Default owner | A1 = authorized exception |
| WF-R01.6 programme | Bulk hygiene | — | **Default** for unrelated expansions | **Not** blocking single G2-R3 row |
| WF-R01.2 NG-03 | New page_type rows | — | WF-R01.6 / WF-R01.7 | G2-R3 A1 = dedicated expansion charter |

**Result:** **AUTHORIZED IN G2-R3 A1** with Coverage + Vocabulary addenda.

---

## 7. Current Page-Type Count

| Page type | Registered | RSC eligible | Scaffold complete |
| --------- | ---------- | ------------ | ----------------- |
| `LANDING_PAGE` | Yes | Yes | **Yes** |
| `HOME_PAGE` | Yes | Yes | No |
| `SERVICE_PAGE` | Yes | Yes | **Yes** |
| `CATEGORY_PAGE` | Yes | Yes | **Yes** |
| `PRODUCT_PAGE` | Yes | Yes | **Yes** |
| `ABOUT_PAGE` | Yes | Yes | **Yes** |
| `CONTACT_PAGE` | Yes | Yes | **Yes** |
| `FAQ_PAGE` | Yes | Yes | No |
| `REVIEWS_PAGE` | Yes | Yes | No |
| `LEGAL_PAGE` | Yes | Yes | No |
| **`SEARCH_RESULTS_PAGE`** | **Yes (A1)** | **Yes** | **No** |

| Measure | Value | Source |
|---------|-------|--------|
| Total registered page types | **11** | PAGE-TYPE-REGISTRY-v1 post-A1 |
| Minimum v1 baseline | **10** | Registry header |
| Expansion rows | **1** | `SEARCH_RESULTS_PAGE` |
| RSC-eligible | **11** | All registered types |
| Scaffold complete | **6** | LANDING · CATEGORY · PRODUCT · CONTACT · ABOUT · SERVICE |
| Global RSC notation | **6/11** | Coverage addendum |

---

## 8. RSC Denominator Authority

| # | Question | Answer | Evidence |
|---|----------|--------|----------|
| 1 | `10` fixed baseline denominator? | **Pre-A1 only** | Operational history 6/10 |
| 2 | `10` minimum programme target? | **Yes** — minimum Registry set | PAGE-TYPE-REGISTRY header |
| 3 | Denominator = registered RSC-eligible count? | **Yes** post-addendum | Reference Scaffold Contract · Coverage addendum |
| 4 | Denominator changes only via addendum? | **Yes** when expanding beyond 10 | G2-R3 charter §19 |
| 5 | Candidates in denominator before scaffold? | **Yes** when registered | Reference Scaffold Contract |
| 6 | Registry row auto-expands denominator? | **Yes** — with Coverage addendum | This A1 + addendum |
| 7 | Denominator expands after scaffold only? | **No** | Contradicts registered denominator binding |
| 8 | Denominator fixed inside WF-R01.3? | **10 baseline fixed** · expansion requires addendum | G2-R3 §19 |

| Interpretation | Supporting authority | Contradiction | Decision |
| -------------- | -------------------- | ------------- | -------- |
| Dynamic registry denominator | Reference Scaffold Contract · Coverage Model CATALOG list | G2-R3 default "remains 10" | **Selected** — resolved via addendum |
| Fixed 10 forever | G2-R2 10-type accrual notes | Coverage Model lists unregistered scaffold | **Rejected** without addendum |
| Addendum required | G2-R3 §19 · §448 | — | **Required — created** |
| WF-R01.6 only | Vocabulary Canon · G2 §461 | G2-R3 A1 explicit path | **Rejected** for this row |

---

## 9. Denominator Decision

**Selected model:** **DYNAMIC REGISTRY DENOMINATOR** (MODEL 1) — authorized by Coverage addendum.

```text
Pre-A1:  RSC = 6/10
Post-A1: RSC = 6/11
Earned numerator delta: 0
```

**Rationale:** Coverage Model already normatively required `SEARCH_RESULTS_PAGE` scaffold for CATALOG SC while Registry lacked the row. Reference Scaffold Contract binds RSC denominator to registered page types. Fixed 10 with an 11th registered type would contradict Registry/Coverage alignment. G2-R3 charter required Coverage addendum for 10→11 — addendum published in A1.

---

## 10. Coverage Addendum Decision

| Field | Value |
|-------|-------|
| **Required** | **Yes** |
| **Authorized in A1** | **Yes** |
| **Path** | [wf-r01-3-1-coverage-model-search-results-page-addendum-v1.md](wf-r01-3-1-coverage-model-search-results-page-addendum-v1.md) |
| **Effect** | Denominator **10 → 11** on registration · numerator frozen at **6** · no accrual at registration |

---

## 11. Page-Type Identity Contract

| Field | Value |
|-------|-------|
| **Canonical name** | `SEARCH_RESULTS_PAGE` |
| **Family / site types** | CATALOG · ECOMMERCE · CORPORATE (catalog subtree) |
| **Registry status** | **REGISTERED / UNSCAFFOLDED** |
| **RSC role** | Denominator member · numerator **not earned** |
| **PC role** | **Excluded** from CATALOG PC corridor |
| **SC role** | **Required** for CATALOG SC |
| **CATEGORY_PAGE distinction** | Taxonomy PLP vs query-driven results host |
| **Reference state** | **No scaffold** · **No composition** · **No manifest** |

---

## 12. Registry Change

| Field | Value |
|-------|-------|
| **Path** | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` |
| **Row added** | **`SEARCH_RESULTS_PAGE`** — one canonical row |
| **Existing rows affected** | **None** — no identity changes |
| **Validation** | Single expansion row · no alias rows · mapping table updated |

---

## 13. Shell Matrix Contract

| Element | State | Rationale |
| ------- | ----- | --------- |
| HEADER_NAV | REQ | Global shell — all catalog internal types |
| MAIN | REQ | Semantic region — all page types |
| BREADCRUMBS | POL | Query-aware shallow trail — G2-R3 §14 |
| SEARCH slot | REQ | Results-host query entry — G2-R3 minimum contract |
| FILTERS slot | POL | Optional refinement — Page-Block Mapping |
| PAGINATION | REQ | List surface — G2-R3 §21 |
| FOOTER | REQ | Global shell |
| LEGAL_LINKS | REQ | Nested in FOOTER when FOOTER REQ |
| Query identity · sort · empty | Scaffold-owned | No shell matrix column — no block_id |

---

## 14. Shell Matrix Change

| Field | Value |
|-------|-------|
| **Path** | `projects/mars-website-factory/page-type-shell-matrix-v1.md` |
| **Change** | Added `SEARCH_RESULTS_PAGE` row · updated §4 canonical set · superseded planned-only note |
| **Validation** | One row · codes REQ/POL only · no new columns |

---

## 15. Page-Block Mapping Contract

| Block/region | Identity | Stance | Role |
| ------------ | -------- | ------ | ---- |
| Search input | `SEARCH` | REQUIRED | Query entry on results host |
| Result listing | `PRODUCT_GRID` · `PRODUCT_CARD` | REQUIRED | Results list |
| Pagination | `PAGINATION` | REQUIRED | Tier B layout-component |
| Filters | `FILTERS` | OPTIONAL | Refinement |
| Breadcrumbs | `BREADCRUMBS` | OPTIONAL | POL trail |
| Global shell | `HEADER_NAV` · `FOOTER` · `LEGAL_LINKS` | REQUIRED | Shell |
| Query summary | *(none)* | SCAFFOLD-OWNED | A2/A3 gap |
| Result count | *(none)* | SCAFFOLD-OWNED | A2/A3 gap |
| Sort | *(none)* | SCAFFOLD-OWNED | Presentation-only |
| Empty state | *(none)* | SCAFFOLD-OWNED | A2 authority gap |

---

## 16. Page-Block Mapping Change

| Field | Value |
|-------|-------|
| **Path** | `workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md` |
| **Change** | Promoted `SEARCH_RESULTS (planned)` → normative `SEARCH_RESULTS_PAGE` section |
| **Validation** | No new block_id rows · scaffold-owned gaps explicit |

---

## 17. Site-Type Block Matrix Change

| Field | Value |
|-------|-------|
| **Required change** | **Cross-reference only** — no new block_id rows |
| **Exact scope** | CATALOG § page-type host note → PAGE-BLOCK-MAPPING |
| **Result** | Site-type block stances unchanged · applicability documented |

---

## 18. Vocabulary Decision

| Field | Value |
|-------|-------|
| **Addendum required** | **Yes** |
| **Path** | [foundry-vocabulary-search-results-page-addendum-v1.md](foundry-vocabulary-search-results-page-addendum-v1.md) |
| **Effect** | `SEARCH_RESULTS_PAGE` promoted from expansion glossary to registered F2 |

---

## 19. CATALOG Corridor Lock

```text
SEARCH_RESULTS_PAGE is NOT a CATALOG PC corridor member.
CATALOG PC = 1/1 (CATEGORY_PAGE → PRODUCT_PAGE) — UNCHANGED.
```

---

## 20. CATALOG SC Relationship

```text
SEARCH_RESULTS_PAGE is REQUIRED for CATALOG SC (Coverage Model L222).
CATALOG SC = PARTIAL — unchanged (no scaffold evidence).
```

---

## 21. Reference State

```text
SEARCH_RESULTS_PAGE = REGISTERED / UNSCAFFOLDED
```

Not: PARTIAL · T1+ · SCAFFOLD COMPLETE · RSC EARNED.

---

## 22. Coverage Accounting

| Dimension | Pre-A1 | Post-A1 | Delta |
|-----------|--------|---------|-------|
| **RC** | 32/32 | 32/32 | 0 |
| **RPC** | 26/32 | 26/32 | 0 |
| **RSC** | 6/10 | **6/11** | denominator +1 · numerator 0 |
| **SC** | LANDING PASS · CATALOG PARTIAL · PROMO PASS | unchanged | 0 |
| **PC** | 1/1 · 1/1 · 1/1 | unchanged | 0 |

**Accrual boundary:** Registry registration **≠** RSC evidence.

---

## 23. Cross-Document Consistency

| Decision | Registry | Shell | Mapping | Site Matrix | Coverage | Vocabulary |
| -------- | -------- | ----- | ------- | ----------- | -------- | ---------- |
| REGISTERED / UNSCAFFOLDED | ✓ | ✓ | ✓ | ✓ cross-ref | ✓ | ✓ |
| RSC 6/11 | ✓ | — | — | — | ✓ | — |
| CATALOG SC required | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| Not PC corridor | ✓ | — | — | — | ✓ | ✓ |
| No scaffold / no RSC +1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

**Result:** **PASS** — no contradictions.

---

## 24. A2 Readiness

| Input | State |
|-------|-------|
| Registered page type | **Yes** |
| Shell row | **Yes** |
| Block mapping | **Yes** |
| Site-type applicability | **Yes** (cross-ref) |
| Coverage contract | **Yes** (addendum) |
| Runtime boundary | G2-R3 charter §22 |
| Known gaps | Query identity · empty state · sort — scaffold-owned |

**Decision:** **A2 AUTHORIZED**

---

## 25. Known Debt and SAFE UNKNOWN

| Item | Status |
|------|--------|
| Scaffold implementation | **Deferred** — A3 |
| Empty-state block_id promotion | **Deferred** — A2 preflight |
| Browser QA | **Deferred** — not A1 scope |
| WF-R01.6 bulk hygiene | **Still DESIGN** — unrelated expansions |

---

## 26. Evidence Paths

```text
projects/mars-website-factory/wf-r01-3-g2-r3-a1-search-results-registry-matrix-expansion-v1.md
projects/mars-website-factory/wf-r01-3-1-coverage-model-search-results-page-addendum-v1.md
projects/mars-website-factory/foundry-vocabulary-search-results-page-addendum-v1.md
reports/wf-r01-3-g2-r3-a1-search-results-registry-matrix-expansion-v1.md
workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md
projects/mars-website-factory/page-type-shell-matrix-v1.md
workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md
workspaces/website-factory-reference-v1/block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md
projects/mars-website-factory/roadmap.md
projects/mars-website-factory/OPERATIONAL-INDEX.md
```

---

## 27. Decision

| Field | Value |
|-------|-------|
| **A1 status** | **PUBLISHED / ALIGNED** |
| **Expansion** | **COMPLETE** |
| **Next wave** | **G2-R3 A2 — SEARCH_RESULTS_PAGE Reference Preflight** |
| **G2-R3 package** | A1 complete · **NOT COMPLETE** |
| **G2 gate** | **READY WITH BLOCKERS** · **NOT EVALUATED** |
