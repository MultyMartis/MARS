# REPORT — WF-R01.3.4 WAVE C1 CATALOG REFERENCE INVENTORY AND SOURCE SELECTION

**Artifact ID:** WF-R01.3.4 Wave C1 — Catalog Reference Inventory and Source Selection (v1)  
**Date:** 2026-06-19  
**Mode:** documentation + read-only source audit — **no** implementation  
**Inventory:** [wf-r01-3-4-catalog-reference-inventory-v1.md](../projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md)

---

## 1. Result

| Field | Value |
|-------|-------|
| **Status** | **COMPLETE** |
| **Inventory decision** | Primary sources selected for all seven catalog `block_id` targets; PLP/PDP scaffold readiness classified; C4 split into **C4A/C4B** |
| **Inventory path** | `projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md` |
| **Coverage metrics** | RC **32/32** · RPC **17/32** · RSC **1/10 global; 1/1 LANDING** · SC **LANDING PASS** · PC **1/1 LANDING** — **UNCHANGED** |
| **C2 readiness** | **AUTHORIZED TO PROCEED** — READY WITH CONSTRAINTS (sanitization preflight) |
| **Next task** | **WF-R01.3.4 Wave C2 — FILTERS Reference Partial** |

---

## 2. Git Safety

| Item | Detail |
|------|--------|
| **Branch** | `mars/post-cycle8-live-tests` |
| **HEAD before task** | `b5abcb9` — `foundry: accept WF-R01.3.4 catalog vertical charter` |
| **Staged files (at start)** | **None** |
| **Foreign WIP** | **Present** — MIG pilots, Triumph workspaces, OCPilot edits, `.recovery-temp`, unrelated factory docs — **excluded** |
| **Selective scope** | Inventory · REPORT · roadmap · OPERATIONAL-INDEX only |

---

## 3. Authority Reviewed

| Document | Path | Role |
|----------|------|------|
| WF-R01.3.4 charter | `projects/mars-website-factory/wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md` | Normative wave authority |
| Charter pass | `reports/wf-r01-3-4-catalog-vertical-profile-references-charter-pass-v1.md` | ACCEPTED evidence |
| WF-R01.3.3 exit | `reports/wf-r01-3-3-exit-and-wf-r01-3-4-handoff-v1.md` | Starting metrics |
| WF-R01.3.3 handoff | `reports/wf-r01-3-3-to-wf-r01-3-4-handoff-v1.md` | Gap inventory |
| Coverage model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | Five dimensions |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Inherited shell |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | PLP/PDP slots |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | RSC minimum |
| Vocabulary Canon | `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` | F3 rules |
| Block registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | Canonical identities |
| Core block library | `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md` | Catalog inventory |
| Block gaps | `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md` | Open gaps |
| Page type registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` | CATEGORY/PRODUCT page types |
| Site type registry | `workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md` | CATALOG site type |
| Roadmap | `projects/mars-website-factory/roadmap.md` | Program sync |
| Operational index | `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Operator sync |

---

## 4. Canonical Target Inventory

| Target | Family | Registry identity | Current state | Coverage role |
|--------|--------|-------------------|---------------|---------------|
| FILTERS | F3 Tier A | `FILTERS` | Row COMPLETE; partial absent | RPC +1 candidate (C2) |
| SEARCH | F3 Tier A | `SEARCH` | Row COMPLETE; partial absent | RPC +1 candidate (C3) |
| CATEGORIES | F1 CATALOG | `CATEGORIES` | Row COMPLETE; partial absent | RPC +1 candidate (C4A) |
| CATEGORY_GRID | F1 CATALOG | `CATEGORY_GRID` | Row COMPLETE; partial absent | RPC +1 candidate (C4A) |
| PRODUCT_GRID | F1 CATALOG | `PRODUCT_GRID` | Row COMPLETE; partial absent | RPC +1 candidate (C4B) |
| PRODUCT_CARD | F1 CATALOG | `PRODUCT_CARD` | Row COMPLETE; partial absent | RPC +1 candidate (C4B) |
| CATEGORY_PAGE | Page type | `CATEGORY_PAGE` | Scaffold absent | RSC +1 candidate (C5) |
| PRODUCT_PAGE | Page type | `PRODUCT_PAGE` | Scaffold absent | RSC +1 candidate (C6) |

**No new `block_id` created.** Forbidden names mapped to layout/composition/SAFE UNKNOWN per inventory §5.

---

## 5. Source Universe

| Source | Project | Platform | Evidence path | Verification state |
|--------|---------|----------|---------------|-------------------|
| SRC-BZPM-002 | BZPM / SITE-002 | OpenCart + ZPM Twig | `projects/ocpilot/sites/site-002/` | **VERIFIED** |
| SRC-SIBCAR-001 | SIBCAR / SITE-001 | WF-V3 Gulp prototype | `workspaces/site-001-wf-v3/` | **PARTIAL** |
| SRC-STORAGE-001 | SIBCAR mirror | Backup | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001/` | **VERIFIED** read-only |
| SRC-REF-WS | Website Factory reference | Gulp | `workspaces/website-factory-reference-v1/` | **VERIFIED** — output target |
| SRC-ISBD | ISBD Care Landing | Gulp | `workspaces/isbd-care-landing/` | **VERIFIED** — no catalog |
| SRC-TRIUMPH | Triumph landing | Gulp | `workspaces/triumph-manipulator-landing-v6/` | **VERIFIED** — no catalog |
| SRC-RECOVERY | Audit captures | HTML snapshots | `.recovery-temp/` | **PARTIAL** — not primary |

---

## 6. Source Quality Model

| Code | Meaning |
|------|---------|
| Q3 | Strong reusable source |
| Q2 | Usable with bounded adaptation |
| Q1 | Partial evidence only |
| Q0 | Rejected / unsafe |
| SAFE UNKNOWN | Insufficient evidence |

---

## 7. BZPM Findings

### FILTERS

- **STRONG SOURCE:** `filterssidebar.twig` — semantic form, accordion facet groups, price/attribute ranges, availability switches, per-group reset (M9.8.9-08A).
- **REUSABLE STRUCTURE:** Mobile drawer shell in `category.twig` (`data-filter-sidebar`).
- **CMS-COUPLED / REJECTED:** `filter_profile_resolver.php`, AJAX filter JS in `main.js`.

### SEARCH

- **STRONG SOURCE:** Header `<form role="search">` in `plp-stoly-after.html`.
- **REJECTED:** `zpm-qsearch` autocomplete overlay + AJAX product/category lists in `main.js`.
- **PARTIAL:** Mobile search panel chrome (static states only).

### CATEGORIES

- **STRONG SOURCE:** `megamenu.twig` taxonomy navigation; subcategory chips in `category.twig`.
- **BOUNDARY:** Subcategories removed from filter sidebar (M9.8.9-07) — correct FILTERS ≠ CATEGORIES split.

### CATEGORY_GRID

- **STRONG SOURCE:** `catalogsections.twig` — homepage/hub category tile grid with image + title + link.

### PRODUCT_GRID

- **STRONG SOURCE:** `category.twig` — `category__grid` container, topbar, pagination integration, grid/list switcher (layout concern).
- **LIVE PROOF:** `plp-stoly-after.html` assembled PLP.

### PRODUCT_CARD

- **STRONG SOURCE:** `productcard.twig` — media, SKU, status, price, delivery, compare/wishlist, CTA.
- **PROJECT-SPECIFIC:** Cart micro-actions optional strip for universal reference.

### CATEGORY_PAGE

- **STRONG PLP shell evidence:** Full `category.twig` + existing reference shell partials (HEADER_NAV, BREADCRUMBS, PAGINATION, FOOTER).
- **Composition zones:** certificates/dealers tail blocks — not Registry identities.

### PRODUCT_PAGE

- **PARTIAL PDP evidence:** `producthero.twig`, `producttabs.twig` (description, key specs, full specs).
- **SAFE UNKNOWN:** Dedicated gallery block_id absent — stub honesty required in C6.

---

## 8. SIBCAR Findings

### Catalog/listing

- **VERIFIED prototype:** `catalog.html` + `catalog-body.html` layout (filters sidebar + results + pagination).
- **Discovery authority:** `SITE-001-WFV3-CATALOG-DISCOVERY-v1.md` — Class B inventory showroom semantics.

### Vehicle card

- **VERIFIED:** `catalog-results.html` — `wf-v3-inventory-card` with year, mileage, price, specs, monthly payment.
- **Secondary only** — AUTO vertical vocabulary; not universal PRODUCT_CARD primary.

### Search/filters

- **FILTERS secondary:** `catalog-filters.html` — static brand/price/year/transmission/body facets.
- **SEARCH:** Header lacks site search; homepage hero `wf-v3-search` is catalog discovery — **wrong identity** for SEARCH block.

### AUTO vertical

- **P2 PARTIAL:** Prototype + governance docs sufficient for C7 binding notes.
- **Live OpenCart catalog:** **SAFE UNKNOWN** — not audited; not blocking C2.

---

## 9. Other Sources

| Source | Target supported | Quality | Role |
|--------|------------------|---------|------|
| ISBD Care Landing | None (LANDING/PROMO) | Q0 for catalog | **Rejected** |
| Triumph v6 | None (LANDING) | Q0 for catalog | **Rejected** |
| Reference workspace | Shell partials only | N/A | Output host — not source |
| `.recovery-temp` captures | Supplementary forensic | Q1 | **Not** in primary set |

---

## 10. FILTERS Source Selection

| Field | Value |
|-------|-------|
| **Primary source** | **SRC-BZPM-002** — `filterssidebar.twig` (M9.8.9-08A live capture) + mobile panel from `category.twig` |
| **Secondary source** | **SRC-SIBCAR-001** — `catalog-filters.html` (AUTO facet vocabulary) |
| **Rejected sources** | BZPM filter resolver PHP · AJAX JS · ISBD · Triumph · recovery temp |
| **Quality** | **Q2** |
| **Constraints** | Strip OC twig vars; static states only; no AJAX; sanitize client copy |
| **C2 readiness** | **READY WITH CONSTRAINTS** — **AUTHORIZED TO PROCEED** |

---

## 11. SEARCH Source Selection

| Field | Value |
|-------|-------|
| **Primary source** | **SRC-BZPM-002** — header search form from `plp-stoly-after.html` (form-only; no autocomplete) |
| **Secondary source** | **SRC-BZPM-002** — mobile search panel chrome (static) |
| **Rejected sources** | BZPM qsearch AJAX layer · SIBCAR hero inventory cluster · ISBD · Triumph |
| **Quality** | **Q2** |
| **Constraints** | Autocomplete explicitly out of scope; empty-query policy documented in C3 |
| **C3 readiness** | **READY WITH CONSTRAINTS** — **AUTHORIZED TO PROCEED** |

---

## 12. Catalog Block Source Selection

| Target | Primary source | Secondary source | Quality | Risks |
|--------|----------------|------------------|---------|-------|
| CATEGORIES | BZPM megamenu + subcat chips | SIBCAR catalog-chips | Q2 | Megamenu vs nav tree scope in C4A REPORT |
| CATEGORY_GRID | BZPM catalogsections.twig | BZPM hub category cards | Q2 | Do not conflate with CATEGORIES partial |
| PRODUCT_GRID | BZPM category.twig grid shell | SIBCAR catalog-body | Q2 | Sort/view switcher = layout; not new block_id |
| PRODUCT_CARD | BZPM productcard.twig | SIBCAR inventory card | Q2 / Q1 | Vertical field bleed if AUTO fields copied blindly |

**C4 plan:** **C4A** then **C4B** — inventory-proven split.

---

## 13. CATEGORY_PAGE Readiness

| Region | Source state | Evidence |
|--------|--------------|----------|
| HEADER_NAV | SOURCE READY | Reference partial WF-R01.3.2 |
| BREADCRUMBS | SOURCE READY | Reference partial WF-R01.3.3 S2 |
| MAIN / heading | SOURCE READY | BZPM category.twig |
| CATEGORIES | PARTIAL SOURCE | Megamenu + chips — C4A |
| FILTERS | PARTIAL SOURCE | filterssidebar — C2 |
| SEARCH | PARTIAL SOURCE | Header form — C3 |
| Result controls | PARTIAL SOURCE | BZPM topbar |
| PRODUCT_GRID | PARTIAL SOURCE | category.twig — C4B |
| PRODUCT_CARD | PARTIAL SOURCE | productcard.twig — C4B |
| PAGINATION | SOURCE READY | Reference partial WF-R01.3.3 S3 |
| FOOTER / LEGAL_LINKS | SOURCE READY | Reference partials WF-R01.3.2 |
| Trust tail blocks | Composition zone | BZPM certificates/dealers — stub in scaffold |

**Final decision:** **CATEGORY_PAGE READY WITH GAPS** — C5 authorized after C2–C4B.

---

## 14. PRODUCT_PAGE Readiness

| Region | Source state | Evidence |
|--------|--------------|----------|
| Shell stack | SOURCE READY | Reference partials |
| BREADCRUMBS | SOURCE READY | Reference partial |
| Product identity / media | PARTIAL SOURCE | BZPM producthero.twig |
| Commercial zone | PARTIAL SOURCE | BZPM commerce-card patterns |
| Specifications / description | PARTIAL SOURCE | producttabs.twig — composition zone |
| CTA / lead | PARTIAL SOURCE | Charter bind to CTA/LEAD_FORM |
| Related items | SAFE UNKNOWN | Optional PRODUCT_GRID reuse |
| Gallery block | SAFE UNKNOWN | No Registry block_id |
| AUTO secondary | PARTIAL SOURCE | SIBCAR pdp-hero.html |

**Final decision:** **PDP SOURCE READY WITH GAPS** — C6 **minimal scaffold** path authorized.

---

## 15. Vertical Profile Evidence

### MANUFACTURER

| Field | Value |
|-------|-------|
| **Proxy** | SRC-BZPM-002 |
| **Status** | **P1 READY** |
| **Evidence** | Faceted industrial attributes · SKU/article · request-price · compare · certificates/dealer trust · PDP spec tabs |

### AUTO

| Field | Value |
|-------|-------|
| **Proxy** | SRC-SIBCAR-001 (prototype) |
| **Status** | **P2 PARTIAL** |
| **Evidence** | Inventory card grammar · catalog filters · discovery docs · PDP zones |
| **Deferral** | Live OC catalog binding **SAFE UNKNOWN** — C7 doc with prototype honesty |

**Vertical Profile binding docs:** **NOT CREATED** in C1 (Wave C7).

---

## 16. Sanitization Matrix

| Source | Client data | CMS logic | URLs | Secrets | Other |
|--------|-------------|-----------|------|---------|-------|
| SRC-BZPM-002 | Remove ZPM copy, phones, dealer names | Strip OC vars, PHP resolver, AJAX | Remove TEST URLs | None in selected twig | Optional strip compare/cart hooks |
| SRC-SIBCAR-001 | Remove СИБКАР brand, address, phone | N/A (static) | Generic placeholders | Do not use STORAGE secrets/ | Generic assets |
| SRC-STORAGE-001 | Same as SIBCAR | Same | Same | **Do not read secrets/** | Mirror only |

---

## 17. Block-to-Source Crosswalk

| Target | Identity | Primary source | Wave | Expected output |
|--------|----------|----------------|------|-----------------|
| FILTERS | `FILTERS` | BZPM filterssidebar.twig | C2 | T1+ partial + REPORT |
| SEARCH | `SEARCH` | BZPM header search form | C3 | T1+ partial + REPORT |
| CATEGORIES | `CATEGORIES` | BZPM megamenu + chips | C4A | T1+ partial + REPORT |
| CATEGORY_GRID | `CATEGORY_GRID` | BZPM catalogsections.twig | C4A | T1+ partial + REPORT |
| PRODUCT_GRID | `PRODUCT_GRID` | BZPM category.twig grid | C4B | T1+ partial + REPORT |
| PRODUCT_CARD | `PRODUCT_CARD` | BZPM productcard.twig | C4B | T1+ partial + REPORT |
| CATEGORY_PAGE | `CATEGORY_PAGE` | BZPM PLP assembly | C5 | Scaffold + manifest |
| PRODUCT_PAGE | `PRODUCT_PAGE` | BZPM PDP zones | C6 | Minimal scaffold decision |
| MANUFACTURER | Vertical | BZPM proxy | C7 | Binding doc |
| AUTO | Vertical | SIBCAR prototype | C7 | Partial binding doc |

---

## 18. Wave Readiness

| Wave | Status | Preconditions | Next action |
|------|--------|---------------|-------------|
| C1 | **COMPLETE** | Charter ACCEPTED | This REPORT |
| C2 | **AUTHORIZED TO PROCEED** | Sanitization preflight | FILTERS partial |
| C3 | **AUTHORIZED TO PROCEED** | Reject autocomplete in extract | SEARCH partial |
| C4A | **AUTHORIZED TO PROCEED** | C1 complete | CATEGORIES + CATEGORY_GRID |
| C4B | **AUTHORIZED TO PROCEED** | C4A recommended | PRODUCT_GRID + PRODUCT_CARD |
| C5 | **READY WITH PREFLIGHT** | C2–C4B | CATEGORY_PAGE scaffold |
| C6 | **AUTHORIZED** (decision-first) | C4B minimum | Minimal PDP scaffold |
| C7 | **READY WITH PREFLIGHT** | C4–C6 | Vertical binding docs |
| C8 | **DEFERRED** | C2–C7 | G2 evaluation |

---

## 19. Coverage Freeze

| Dimension | Value | Changed? |
|-----------|-------|----------|
| RC | 32/32 | **No** |
| RPC | 17/32 | **No** |
| RSC | 1/10; 1/1 LANDING | **No** |
| SC | LANDING PASS | **No** |
| PC | 1/1 LANDING | **No** |

**Confirmation:** Wave C1 made **no** coverage accrual and **no** Registry state mutation.

---

## 20. Risks and SAFE UNKNOWN

| Severity | Finding | Affected wave | Action |
|----------|---------|---------------|--------|
| HIGH | CMS/AJAX coupling in BZPM filters/search | C2, C3 | Static reference only |
| HIGH | Client content leakage | C2–C7 | Mandatory sanitization matrix |
| MEDIUM | SEARCH/autocomplete conflation | C3 | Form-only primary |
| MEDIUM | Grid/card identity overlap | C4 | C4A/C4B split |
| MEDIUM | PDP Registry gaps | C6 | Stub honesty |
| LOW | SIBCAR live OC unverified | C7 | Prototype-only AUTO binding |
| SAFE UNKNOWN | Dedicated PDP gallery block_id | C6 | No Registry change in C1 |

---

## 21. Files Created

| File | Purpose |
|------|---------|
| `projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md` | Canonical C1 inventory + source-selection decision |
| `reports/wf-r01-3-4-wave-c1-catalog-reference-inventory-v1.md` | This Wave C1 REPORT |

---

## 22. Files Modified

| File | Change |
|------|--------|
| `projects/mars-website-factory/roadmap.md` | R01.3.4 Wave C1 **COMPLETE**; changelog; next = Wave C2 |
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Wave C1 complete; metrics; next task; footer |

---

## 23. Validation

| Check | Result |
|-------|--------|
| Canonical identities only | **PASS** |
| Source paths exist | **PASS** |
| Source provenance documented | **PASS** |
| No implementation | **PASS** — `src/` reference workspace unchanged |
| No Registry mutation | **PASS** |
| No metric mutation | **PASS** |
| No G2 claims | **PASS** |
| Primary source singular per target | **PASS** |
| SAFE UNKNOWN honest | **PASS** |
| Live systems unchanged | **PASS** |
| OCPilot runtime unchanged | **PASS** |

---

## 24. Git Result

*(Recorded after selective commit)*

| Item | Detail |
|------|--------|
| **Commit hash** | *(see task closeout)* |
| **Commit message** | `foundry: publish WF-R01.3.4 catalog source inventory` |
| **Push result** | *(see task closeout)* |
| **Files committed** | 4 — inventory · REPORT · roadmap · OPERATIONAL-INDEX |
| **No foreign lane confirmation** | **Confirmed** (selective paths only) |

---

## 25. Final Status

```text
COMPLETE
```

---

## 26. Next Task

```text
WF-R01.3.4 Wave C2 — FILTERS Reference Partial
```

**Do not execute** in this pass.

---

## 27. Exact Evidence Paths

See inventory §25 — full list in [wf-r01-3-4-catalog-reference-inventory-v1.md](../projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md).

---

## 28. Stop Confirmation

```text
Wave C2: NOT STARTED
FILTERS: NOT IMPLEMENTED
SEARCH: NOT IMPLEMENTED
Catalog grids/cards: NOT IMPLEMENTED
CATEGORY_PAGE scaffold: NOT CREATED
PRODUCT_PAGE scaffold: NOT CREATED
Vertical Profile binding: NOT CREATED
G2 execution: NOT STARTED
Coverage metrics: UNCHANGED
Reference workspace src/: NOT MODIFIED
Production readiness: NOT CLAIMED
```

---

*Wave C1 REPORT · v1 · 2026-06-19*
