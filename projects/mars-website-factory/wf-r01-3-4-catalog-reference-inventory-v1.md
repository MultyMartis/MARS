# WF-R01.3.4 Catalog Reference Inventory v1

**Subprogram:** WF-R01.3.4 — Catalog & Vertical Profile References  
**Wave:** C1 — Catalog Reference Inventory and Source Selection  
**Version:** v1  
**Date:** 2026-06-19  
**Status:** **PUBLISHED**

**Honesty boundary:** Documentation and source-selection authority only. **Not** implementation. **Not** RPC/RSC/SC/PC accrual. **Not** G2 authorization. **Not** canonical enrollment of BZPM or SIBCAR as Factory reference until wave C2+ build evidence.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED** |
| **Wave** | **C1 COMPLETE** |
| **Implementation** | **NOT STARTED** |
| **Coverage metrics** | **UNCHANGED** — RC **32/32** · RPC **17/32** · RSC **1/10 global; 1/1 LANDING** · SC **LANDING PASS** · PC **1/1 LANDING** |
| **Next authorized wave** | **WF-R01.3.4 Wave C2 — FILTERS Reference Partial** |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Artefact ID** | WF-R01.3.4 Catalog Reference Inventory v1 |
| **Purpose** | Canonical catalog block inventory; bounded source universe; primary/secondary source decisions; block-to-source crosswalk; C2–C7 execution plan |
| **Charter authority** | [wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md](wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md) |
| **Wave C1 REPORT** | [wf-r01-3-4-wave-c1-catalog-reference-inventory-v1.md](../../reports/wf-r01-3-4-wave-c1-catalog-reference-inventory-v1.md) |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| WF-R01.3.4 charter | `projects/mars-website-factory/wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md` | Normative catalog wave authority |
| Charter pass | `reports/wf-r01-3-4-catalog-vertical-profile-references-charter-pass-v1.md` | ACCEPTED evidence |
| WF-R01.3.3 exit | `reports/wf-r01-3-3-exit-and-wf-r01-3-4-handoff-v1.md` | Starting metrics; inherited shell partials |
| WF-R01.3.3 handoff | `reports/wf-r01-3-3-to-wf-r01-3-4-handoff-v1.md` | Gap inventory; exclusions |
| Coverage model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | Five dimensions; G2 floor |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Inherited shell stack |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | CATEGORY/PRODUCT slot policy |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | RSC minimum |
| Vocabulary Canon | `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` | F3 structural rules |
| Block registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | Canonical `block_id` rows |
| Core block library | `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md` | Catalog inventory |
| Block gaps | `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md` | Open partial gaps |
| Page type registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` | CATEGORY_PAGE, PRODUCT_PAGE |
| Site type registry | `workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md` | CATALOG site type |

---

## 4. Scope

### In scope (Wave C1)

- Canonical identity lock for seven catalog `block_id` targets plus two page-type scaffold targets
- Bounded source universe audit (BZPM/SITE-002, SIBCAR/SITE-001, ISBD, Triumph, reference workspace)
- Primary/secondary source selection per target
- Source quality classification (Q0–Q3)
- Sanitization matrix
- Block-to-source crosswalk
- Wave C2–C7 readiness decisions
- Vertical profile evidence classification (MANUFACTURER, AUTO) — **no binding docs**

### Out of scope (Wave C1)

- HTML/SCSS/JS partials · scaffolds · compositions
- Registry row edits · new `block_id` · new page types
- Vertical Profile binding publication (Wave C7)
- Live BZPM/SIBCAR modification · OCPilot runtime changes
- Metric mutation · G2 activation

---

## 5. Canonical Target Inventory

| Identity | Family | Registry status | Current reference state | RPC status | Future RPC delta |
|----------|--------|-----------------|-------------------------|------------|------------------|
| `FILTERS` | F3 Structural — Tier A | Row **COMPLETE** (Gate 2) | Partial **absent** | **Not in 17/32** | **+1** if T1+ in C2 |
| `SEARCH` | F3 Structural — Tier A | Row **COMPLETE** | Partial **absent** | **Not in 17/32** | **+1** if T1+ in C3 |
| `CATEGORIES` | F1 Block — CATALOG | Row **COMPLETE** | Partial **absent** | **Not in 17/32** | **+1** if T1+ in C4 |
| `CATEGORY_GRID` | F1 Block — CATALOG | Row **COMPLETE** | Partial **absent** | **Not in 17/32** | **+1** if T1+ in C4 |
| `PRODUCT_GRID` | F1 Block — CATALOG | Row **COMPLETE** | Partial **absent** | **Not in 17/32** | **+1** if T1+ in C4 |
| `PRODUCT_CARD` | F1 Block — CATALOG | Row **COMPLETE** | Partial **absent** | **Not in 17/32** | **+1** if T1+ in C4 |
| `CATEGORY_PAGE` | Page type | Registry row **exists** | Scaffold **absent** | RSC **0/1 PLP** | **+1** global if validated in C5 |
| `PRODUCT_PAGE` | Page type | Registry row **exists** | Scaffold **absent** | RSC **0/1 PDP** | **+1** global if validated in C6 |

**Forbidden identities (not in Registry — not created):** `CATALOG_GRID` · `LISTING_CARD` · `SORT_CONTROLS` · `RESULTS_META` · `PRODUCT_LIST` · `SEARCH_RESULTS` (page type planned only).

**Production-name mapping:**

| Production name | Classification |
|-----------------|----------------|
| BZPM `category__sort` / sort menu | Layout concern inside **FILTERS** policy (sort sub-variant) |
| BZPM `category__view` grid/list switcher | Layout concern inside **PRODUCT_GRID** notes |
| BZPM `zpm-sub-cat-chips` | **CATEGORIES** navigation semantics |
| BZPM `zpm-qsearch` autocomplete layer | **Rejected** for SEARCH reference — backend/autocomplete coupling |
| SIBCAR `wf-v3-search` hero cluster | Catalog discovery helper — **not** canonical SEARCH block |
| PDP gallery / spec-table zones | **Composition zone** / **SAFE UNKNOWN** — no Registry `block_id` |

---

## 6. Source Universe

| Source ID | Project / site | Platform | Evidence path | Freshness | Verification | Scope | Client-specific | CMS coupling | Reusability |
|-----------|----------------|----------|---------------|-----------|--------------|-------|-----------------|--------------|-------------|
| **SRC-BZPM-002** | BZPM / SITE-002 | OpenCart + ZPM theme (Twig/CSS/JS) | `projects/ocpilot/sites/site-002/` | 2026-06 captures + stable baselines | **VERIFIED** (repo + checkpoint docs) | FILTERS · SEARCH · CATEGORIES · grids · cards · PLP/PDP shell | **High** — ZPM brand, Russian copy, dealer blocks | **High** — OC controllers, AJAX filters, profile resolver | **Strong** structure after sanitization |
| **SRC-SIBCAR-001** | SIBCAR / SITE-001 | WF-V3 Gulp prototype + OCPilot reports | `workspaces/site-001-wf-v3/` · `projects/ocpilot/sites/site-001/reports/` | 2026-06-14 restore point | **PARTIAL** — prototype only; live OC catalog **not** Factory-bound | AUTO filters · inventory card · catalog layout | **High** — dealer PII, brand assets | **Low** in prototype; live OC **UNVERIFIED** | **Secondary** vertical evidence |
| **SRC-STORAGE-001** | SIBCAR backup mirror | Gulp prototype backup | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001/` | 2026-06-14 | **VERIFIED** read-only mirror of WF-V3 | Same as SRC-SIBCAR-001 | Same | Low | Duplicate of monorepo prototype |
| **SRC-REF-WS** | Website Factory reference | Gulp starter | `workspaces/website-factory-reference-v1/` | Current | **VERIFIED** | Shell partials only — **no** catalog blocks | None | None | Target **output** workspace — not source |
| **SRC-ISBD** | ISBD Care Landing | Gulp / care vertical | `workspaces/isbd-care-landing/` | Registered case | **VERIFIED** | LANDING/PROMO — **no** catalog patterns | Care vertical | N/A | **Rejected** as catalog primary |
| **SRC-TRIUMPH** | Triumph manipulator | Gulp landing | `workspaces/triumph-manipulator-landing-v6/` | Registered case | **VERIFIED** | LANDING/PROMO only | Generic demo | N/A | **Rejected** as catalog primary |
| **SRC-RECOVERY** | Sanitized HTML captures | Audit snapshots | `.recovery-temp/` (e.g. `bzpm-neutral-cat.html`) | Mixed | **PARTIAL** | Supplementary forensic only | Mixed | Unknown | **Not** in final primary set |

**Enrollment note:** BZPM and SIBCAR remain **Pending** Factory enrollment per charter §14 — Wave C1 selects extraction sources only.

---

## 7. Source Quality Model

| Code | Meaning |
|------|---------|
| **Q3** | Strong reusable source — semantic HTML structure extractable with bounded sanitization |
| **Q2** | Usable with bounded adaptation — strip CMS/AJAX/client layers; static reference states |
| **Q1** | Partial evidence only — informs vertical notes or secondary patterns |
| **Q0** | Rejected / unsafe — secrets, inseparable backend, or wrong identity |
| **SAFE UNKNOWN** | Insufficient evidence — honest deferral |

---

## 8. FILTERS Sources

### BZPM findings

| Pattern | Path | Classification |
|---------|------|----------------|
| Facet sidebar form | `m9-phase1-tables-work/patch/.../sections/filterssidebar.twig` | **STRONG SOURCE** — semantic `<form>`, accordion facet groups, range, checkbox switches |
| Live capture (post M9.8.9-08A) | `reports/m9.8.9-08a-work/live-capture/.../filterssidebar.twig` | **STRONG SOURCE** — matches filter UX complete checkpoint |
| Mobile filter panel shell | `category-v2-view-switcher-work/category.twig` (`data-filter-sidebar`, `data-filter-open`) | **REUSABLE STRUCTURE** — mobile drawer host; separate from facet markup |
| Filter profile resolver | `m9-phase2-sinks-work/patch/system/library/zpm/filter_profile_resolver.php` | **CMS-COUPLED** — **reject** for reference port |
| AJAX filter JS | `reports/m9.8.9-03-work/live-capture/main.js` | **CMS-COUPLED** — **reject**; C2 uses static states only |

### Selection

| Field | Value |
|-------|-------|
| **Primary source** | **SRC-BZPM-002** — `filterssidebar.twig` (stable baseline M9.8.9-08A capture) + mobile shell from `category.twig` |
| **Secondary source** | **SRC-SIBCAR-001** — `workspaces/site-001-wf-v3/src/partials/sections/catalog-filters.html` (AUTO facet vocabulary only) |
| **Rejected** | BZPM `filter_profile_resolver.php` · AJAX filter endpoints · `.recovery-temp` unclean captures · Triumph/ISBD |
| **Quality** | **Q2** |
| **Readiness** | **READY WITH CONSTRAINTS** for C2 |

### Criterion evaluation

| Criterion | Result |
|-----------|--------|
| Semantic form | **PASS** — `<form class="flt__form">` |
| Facet groups | **PASS** — accordion sections with labels |
| Checkbox/radio patterns | **PASS** — switches + attribute checkboxes in twig |
| Range policy | **PASS** — dual-thumb range + numeric inputs |
| Active filters | **PARTIAL** — active state in markup; static demo required in C2 |
| Reset/apply controls | **PASS** — per-group reset (M9.8.9-08A) |
| Mobile trigger/panel | **PASS** — category sidebar dialog pattern |
| Accessibility | **PASS** — `aria-expanded`, `aria-label`, sr-only labels |
| CMS independence | **FAIL raw** — requires sanitization |
| Sanitization effort | **MEDIUM** |
| Reference readiness | **READY WITH CONSTRAINTS** |

---

## 9. SEARCH Sources

### BZPM findings

| Pattern | Path | Classification |
|---------|------|----------------|
| Header semantic search form | `reports/m9.8.9-06d-work/plp-stoly-after.html` L232–244 | **STRONG SOURCE** — `role="search"`, label, input, submit |
| Quick-search autocomplete overlay | Same file L250+ · `main.js` qsearch block | **CMS-COUPLED** — **reject** for reference |
| Mobile search panel | `plp-stoly-after.html` L592+ | **PARTIAL SOURCE** — panel chrome reusable; autocomplete **reject** |

### SIBCAR findings

| Pattern | Path | Classification |
|---------|------|----------------|
| Homepage hero inventory cluster | `site-001-wf-v3/.../homepage-hero.html` | **Wrong identity** — multi-select catalog discovery, not site SEARCH block |
| Header | `site-001-wf-v3/.../header.html` | **No SEARCH** utility present |

### Selection

| Field | Value |
|-------|-------|
| **Primary source** | **SRC-BZPM-002** — header search form extract from `plp-stoly-after.html` (form only; **no** qsearch autocomplete) |
| **Secondary source** | **SRC-BZPM-002** — mobile search panel chrome from same capture (static closed state) |
| **Rejected** | BZPM qsearch AJAX/autocomplete · SIBCAR hero cluster as SEARCH · ISBD · Triumph |
| **Quality** | **Q2** |
| **Readiness** | **READY WITH CONSTRAINTS** for C3 |

### Criterion evaluation

| Criterion | Result |
|-----------|--------|
| Semantic search form | **PASS** (header extract) |
| Accessible label | **PASS** |
| Input + submit | **PASS** |
| Clear policy | **PARTIAL** — reset link exists in overlay; static policy in C3 REPORT |
| Empty query policy | **SAFE UNKNOWN** in source — document in C3 |
| Placement variants | **PASS** — header utility + mobile panel |
| Mobile behavior | **PASS** (panel chrome) |
| Backend coupling | **FAIL** on full qsearch — **mitigated** by form-only extract |
| Autocomplete coupling | **Rejected layer** |
| Reference readiness | **READY WITH CONSTRAINTS** |

---

## 10. CATEGORIES Sources

### BZPM findings

| Pattern | Path | Classification |
|---------|------|----------------|
| Megamenu taxonomy | `backups/stable-baselines/SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE/files/.../megamenu.twig` | **STRONG SOURCE** — category tree navigation |
| Offcanvas catalog menu | Same baseline `offcanvasmenu.twig` | **SECONDARY SOURCE** |
| Subcategory chips on PLP | `category-v2-view-switcher-work/category.twig` L44–64 | **STRONG SOURCE** — mid-level category navigation |
| Subcategories inside filter sidebar | Removed M9.8.9-07 from filter block | **Correct boundary** — chips ≠ FILTERS |

### Selection

| Field | Value |
|-------|-------|
| **Primary source** | **SRC-BZPM-002** — megamenu.twig + subcategory chips (`category.twig`) |
| **Secondary source** | **SRC-SIBCAR-001** — `catalog-chips.html` (AUTO chip grammar) |
| **Rejected** | CATEGORY_GRID tile markup as CATEGORIES proof · filter sidebar category tree |
| **Quality** | **Q2** |
| **Readiness** | **READY WITH CONSTRAINTS** for C4A |

---

## 11. CATEGORY_GRID Sources

### BZPM findings

| Pattern | Path | Classification |
|---------|------|----------------|
| Homepage category tile grid | `m7.1-launch-mode-work/patch/.../catalogsections.twig` | **STRONG SOURCE** — tile grid with image/title/link |
| Megamenu tiles | megamenu.twig | **PARTIAL** — overlaps CATEGORIES; use as secondary layout reference only |
| Hub category cards | `m9.5-root-hub-work/patch/.../category.twig` | **PARTIAL** — hub PLP variant |

### Selection

| Field | Value |
|-------|-------|
| **Primary source** | **SRC-BZPM-002** — `catalogsections.twig` |
| **Secondary source** | BZPM hub `category.twig` child-category presentation |
| **Rejected** | PRODUCT_GRID cells · SIBCAR catalog-results (wrong identity) |
| **Quality** | **Q2** |
| **Readiness** | **READY WITH CONSTRAINTS** for C4A |

---

## 12. PRODUCT_GRID Sources

### BZPM findings

| Pattern | Path | Classification |
|---------|------|----------------|
| PLP result container | `category-v2-view-switcher-work/category.twig` — `category__grid`, topbar, pagination slot | **STRONG SOURCE** |
| Grid/list view switcher | Same file `data-category-view` | **Layout concern** — inside PRODUCT_GRID policy |
| Sort controls | Same file `category__sort` | **FILTERS sub-variant** — not separate block |
| Live HTML proof | `reports/m9.8.9-06d-work/plp-stoly-after.html` | **STRONG SOURCE** — assembled PLP |

### Selection

| Field | Value |
|-------|-------|
| **Primary source** | **SRC-BZPM-002** — `category.twig` layout + `plp-stoly-after.html` |
| **Secondary source** | **SRC-SIBCAR-001** — `catalog-body.html` + `catalog-results.html` grid wrapper |
| **Rejected** | Monolithic PLP HTML as single proof for all four block identities |
| **Quality** | **Q2** |
| **Readiness** | **READY WITH CONSTRAINTS** for C4B |

---

## 13. PRODUCT_CARD Sources

### BZPM findings

| Pattern | Path | Classification |
|---------|------|----------------|
| List card unit | `category-v2.1-list-card-commerce-work/productcard.twig` | **STRONG SOURCE** — media, SKU, status, price, CTA, compare/wishlist |
| Live card HTML | `plp-stoly-after.html` product-card sections | **STRONG SOURCE** |
| Cart micro-actions | `product-card__actions` | **PROJECT-SPECIFIC** — optional strip for universal minimum |

### SIBCAR findings

| Pattern | Path | Classification |
|---------|------|----------------|
| Inventory card | `site-001-wf-v3/.../catalog-results.html` — `wf-v3-inventory-card` | **SECONDARY** — AUTO fields (mileage, year, monthly payment) |

### Selection

| Field | Value |
|-------|-------|
| **Primary source** | **SRC-BZPM-002** — `productcard.twig` |
| **Secondary source** | **SRC-SIBCAR-001** — inventory card (vertical field vocabulary) |
| **Rejected** | OC `catalog_item` legacy pattern · per-card swiper galleries |
| **Quality** | **Q2** (primary) · **Q1** (AUTO secondary) |
| **Readiness** | **READY WITH CONSTRAINTS** for C4B |

**Universal minimum vs vertical additions:**

| Zone | Universal (MANUFACTURER proxy) | AUTO addition (C7 notes) |
|------|------------------------------|-------------------------|
| Media | Product image | Same |
| Title | Product name | Make/model/year |
| Attributes | SKU, dimensions | Mileage, transmission |
| Commercial | Price / request-price | Monthly payment teaser |
| Availability | In stock / preorder | Badge |
| CTA | Open PDP / RFQ | «Подробнее» |
| Compare/wishlist | Optional manufacturer pattern | De-emphasize per SIBCAR P-09 |

---

## 14. CATEGORY_PAGE Sources

### Shell region readiness (PLP)

| Region | Source state | Evidence |
|--------|--------------|----------|
| HEADER_NAV | **SOURCE READY** | Reference partial exists (WF-R01.3.2) |
| BREADCRUMBS | **SOURCE READY** | Reference partial exists (WF-R01.3.3 S2) |
| MAIN / page identity | **SOURCE READY** | BZPM `category.twig` section structure |
| CATEGORIES | **PARTIAL SOURCE** | Megamenu + subcategory chips |
| FILTERS | **PARTIAL SOURCE** | `filterssidebar.twig` — pending C2 partial |
| SEARCH | **PARTIAL SOURCE** | Header form extract — pending C3 partial |
| Result controls (sort/view) | **PARTIAL SOURCE** | BZPM topbar — bind inside FILTERS/PRODUCT_GRID |
| PRODUCT_GRID | **PARTIAL SOURCE** | BZPM `category__grid` — pending C4B |
| PRODUCT_CARD | **PARTIAL SOURCE** | BZPM `productcard.twig` — pending C4B |
| PAGINATION | **SOURCE READY** | Reference partial exists (WF-R01.3.3 S3) |
| FOOTER / LEGAL_LINKS | **SOURCE READY** | Reference partials exist (WF-R01.3.2) |
| Trust/commercial tail (certificates, dealers) | **Composition zone** | BZPM `category.twig` tail — **not** Registry blocks; stub in scaffold |

**Final decision:** **CATEGORY_PAGE READY WITH GAPS** — sufficient PLP shell evidence for C5 after C2–C4 partials; trust tail = composition honesty.

---

## 15. PRODUCT_PAGE Sources

### Shell region readiness (PDP)

| Region | Source state | Evidence |
|--------|--------------|----------|
| HEADER_NAV | **SOURCE READY** | Reference partial |
| BREADCRUMBS | **SOURCE READY** | Reference partial |
| Product identity / heading | **PARTIAL SOURCE** | BZPM `producthero.twig` |
| Media / gallery | **PARTIAL SOURCE** | BZPM `producthero.twig` · **SAFE UNKNOWN** dedicated gallery `block_id` |
| Commercial zone | **PARTIAL SOURCE** | BZPM commerce-card / producthero |
| Specifications | **PARTIAL SOURCE** | BZPM `w1b-work/producttabs.twig` — **composition zone** |
| Description | **PARTIAL SOURCE** | producttabs description section |
| CTA / lead form | **PARTIAL SOURCE** | Bind `CTA` / `LEAD_FORM` per charter |
| Related items | **SAFE UNKNOWN** | Optional `PRODUCT_GRID` reuse — no dedicated block |
| Trust | **Composition zone** | Site-specific |
| FOOTER / LEGAL_LINKS | **SOURCE READY** | Reference partials |
| SEARCH slot | **PARTIAL SOURCE** | Header utility — pending C3 |

**SIBCAR secondary:** `workspaces/site-001-wf-v3/src/partials/sections/pdp-hero.html` — AUTO zone anatomy (Z0–Z10 reports).

**Final decision:** **PDP SOURCE READY WITH GAPS** — C6 default **minimal PDP scaffold** path authorized; full PDP depth deferred per charter.

---

## 16. MANUFACTURER Vertical Evidence

| Field | Value |
|-------|-------|
| **Proxy source** | **SRC-BZPM-002** (industrial equipment catalog) |
| **Status** | **P1 READY** for Wave C7 binding doc |
| **Evidence** | Technical attributes in filters · SKU/article on cards · request-price / dealer flows · compare · certificates/dealer trust on PLP · spec tabs on PDP |
| **Gaps** | Document links · engineering drawing gallery — **composition zone** |

---

## 17. AUTO Vertical Evidence

| Field | Value |
|-------|-------|
| **Proxy source** | **SRC-SIBCAR-001** (`workspaces/site-001-wf-v3/`) |
| **Status** | **P2 PARTIAL** — prototype evidence only; live OpenCart catalog **UNVERIFIED** for Factory binding |
| **Evidence** | Inventory card fields · catalog filters · catalog discovery docs · PDP prototype zones |
| **Gaps** | Credit/trade-in depth · live filter backend · production URL coupling |
| **Live OC** | **SAFE UNKNOWN** — not required for C1; C7 may document prototype-only binding |

---

## 18. Sanitization Matrix

| Source | Remove client data | Remove CMS logic | Remove backend calls | Rename classes | Remove URLs | Remove credentials | Other |
|--------|-------------------|------------------|----------------------|----------------|-------------|-------------------|-------|
| **SRC-BZPM-002** | ZPM brand copy · real phones · dealer names · certificate images | OC twig vars · `filter_profile_resolver` · category.php query hooks | AJAX filter/search endpoints · qsearch API | Optional `zpm-` → neutral prefix in reference pass | Production TEST URLs · category hrefs | None found in selected twig | Strip compare/wishlist cart hooks or stub |
| **SRC-SIBCAR-001** | СИБКАР brand · Novosibirsk address · phone in header | N/A (static prototype) | Form actions → `#` | `wf-v3-` prefix acceptable in extract notes | Client paths | None in prototype | Use generic placeholder assets |
| **SRC-STORAGE-001** | Same as SIBCAR | Same | Same | Same | Same | Do not read `secrets/` folder | Mirror only |
| **SRC-RECOVERY** | **Mandatory** if ever used | **Mandatory** | **Mandatory** | **Mandatory** | **Mandatory** | Scan before use | **Not** selected primary |

**Forbidden transfer:** credentials · tokens · real PII · production URLs · client legal text · OpenCart controllers/models · WordPress functions · AJAX endpoints · tracking IDs.

---

## 19. Block-to-Source Crosswalk

| Target | Canonical identity | Primary source | Secondary source | Quality | Wave | Expected output |
|--------|-------------------|----------------|------------------|---------|------|-----------------|
| FILTERS | `FILTERS` | SRC-BZPM-002 `filterssidebar.twig` + mobile shell | SRC-SIBCAR-001 `catalog-filters.html` | Q2 | **C2** | T1+ partial + SCSS + bounded host + REPORT |
| SEARCH | `SEARCH` | SRC-BZPM-002 header form extract | SRC-BZPM-002 mobile panel chrome | Q2 | **C3** | T1+ partial + SCSS + bounded host + REPORT |
| CATEGORIES | `CATEGORIES` | SRC-BZPM-002 megamenu + subcat chips | SRC-SIBCAR-001 `catalog-chips.html` | Q2 | **C4A** | T1+ partial + REPORT |
| CATEGORY_GRID | `CATEGORY_GRID` | SRC-BZPM-002 `catalogsections.twig` | BZPM hub category cards | Q2 | **C4A** | T1+ partial + REPORT |
| PRODUCT_GRID | `PRODUCT_GRID` | SRC-BZPM-002 `category.twig` grid shell | SRC-SIBCAR-001 `catalog-body.html` | Q2 | **C4B** | T1+ partial + REPORT |
| PRODUCT_CARD | `PRODUCT_CARD` | SRC-BZPM-002 `productcard.twig` | SRC-SIBCAR-001 inventory card | Q2/Q1 | **C4B** | T1+ partial + REPORT |
| CATEGORY_PAGE | `CATEGORY_PAGE` | SRC-BZPM-002 PLP assembly | Reference shell partials | Q2 | **C5** | Scaffold page + manifest + composition |
| PRODUCT_PAGE | `PRODUCT_PAGE` | SRC-BZPM-002 PDP zones | SRC-SIBCAR-001 `pdp-hero.html` | Q2 | **C6** | Scope decision + minimal scaffold |
| MANUFACTURER profile | Vertical binding | SRC-BZPM-002 | — | Q2 | **C7** | Binding doc only |
| AUTO profile | Vertical binding | SRC-SIBCAR-001 | — | Q1 | **C7** | Binding doc (partial honesty) |

**Refined C4 plan:** **C4A** (CATEGORIES + CATEGORY_GRID) then **C4B** (PRODUCT_GRID + PRODUCT_CARD) — inventory proves identity separation and sanitization load.

---

## 20. Wave Readiness

| Wave | Status | Preconditions | Next action |
|------|--------|---------------|-------------|
| **C1** | **COMPLETE** | Charter ACCEPTED | This inventory |
| **C2** | **AUTHORIZED TO PROCEED** (preflight: sanitization checklist) | C1 inventory | FILTERS reference partial |
| **C3** | **AUTHORIZED TO PROCEED** (preflight: reject autocomplete) | C1 inventory | SEARCH reference partial |
| **C4A** | **AUTHORIZED TO PROCEED** | C1 inventory | CATEGORIES + CATEGORY_GRID partials |
| **C4B** | **AUTHORIZED TO PROCEED** | C4A recommended first | PRODUCT_GRID + PRODUCT_CARD partials |
| **C5** | **READY WITH PREFLIGHT** | C2–C4B partials + existing shell partials | CATEGORY_PAGE scaffold |
| **C6** | **AUTHORIZED** (decision-first) | C4B PRODUCT_CARD minimum | Minimal PDP scaffold decision |
| **C7** | **READY WITH PREFLIGHT** | C4–C6 evidence | Vertical binding docs |
| **C8** | **DEFERRED** | C2–C7 | G2 readiness evaluation |

---

## 21. Risks

| Risk | Severity | Affected wave | Mitigation |
|------|----------|---------------|------------|
| CMS coupling in BZPM filters/search JS | **HIGH** | C2, C3 | Static reference only; strip AJAX in wave REPORT |
| Client content leakage (ZPM/SIBCAR) | **HIGH** | C2–C7 | Sanitization matrix mandatory pre-extract |
| SEARCH/autocomplete conflation | **MEDIUM** | C3 | Primary = form-only extract; reject qsearch layer |
| Grid/card identity overlap | **MEDIUM** | C4 | Split C4A/C4B; separate bounded hosts |
| Mobile filter behavior complexity | **MEDIUM** | C2, C5 | Document drawer trigger; static open/closed states |
| Vertical overfitting (AUTO fields on universal card) | **MEDIUM** | C4B, C7 | Universal minimum first; vertical in C7 binding |
| PDP Registry gaps (gallery, specs) | **MEDIUM** | C6 | Stub honesty; no new `block_id` |
| False scaffold/RPC claims | **HIGH** | C5–C8 | Five-dimension REPORT per wave |
| Live TEST dependency | **LOW** | C2+ | Repo captures sufficient; no live required |
| Production secrets in STORAGE | **LOW** | C7 | Do not read `site-001/secrets/` |

---

## 22. SAFE UNKNOWN

| Item | Notes |
|------|-------|
| SIBCAR live OpenCart catalog HTML | Not audited in C1 — AUTO vertical uses prototype only |
| BZPM live TEST drift vs repo capture | Checkpoint registered 2026-06-19; re-capture optional in C2 preflight |
| SEARCH empty-query behavior | Document static policy in C3 — no backend |
| Dedicated PDP gallery `block_id` | Future Registry decision **prohibited** in C1 |
| SEARCH_RESULTS_PAGE row | Planned glossary only — route stub in Blueprint |
| Operator steward name | **SAFE UNKNOWN** per charter |
| Triumph catalog patterns | None found — correctly excluded |

---

## 23. Coverage Freeze

```text
RC  = 32/32          — UNCHANGED
RPC = 17/32          — UNCHANGED
RSC = 1/10; 1/1 LANDING — UNCHANGED
SC  = LANDING PASS   — UNCHANGED
PC  = 1/1 LANDING    — UNCHANGED
```

Wave C1 inventory and source selection **do not** add RPC, RSC, SC, or PC. Registry reference states **not** mutated to PARTIAL.

---

## 24. Decision

| Decision field | Value |
|----------------|-------|
| **C2 primary source** | **SRC-BZPM-002** — `filterssidebar.twig` (M9.8.9-08A stable capture) + mobile panel shell from `category.twig` |
| **C3 primary source** | **SRC-BZPM-002** — header `role="search"` form from `plp-stoly-after.html` (**no** autocomplete layer) |
| **C4 source set** | **C4A:** BZPM megamenu/chips + `catalogsections.twig` · **C4B:** BZPM `category.twig` grid + `productcard.twig` · SIBCAR secondary for AUTO vocabulary |
| **C5 base source** | BZPM PLP assembly (`category.twig` + live capture) integrated with existing shell partials |
| **C6 source decision** | **Minimal PDP scaffold** from BZPM `producthero.twig` + `producttabs.twig`; SIBCAR PDP hero as AUTO secondary; defer full PDP depth |
| **C7 evidence decision** | **MANUFACTURER P1 READY** (BZPM) · **AUTO P2 PARTIAL** (SIBCAR prototype) — binding docs only in C7 |
| **Next task** | **WF-R01.3.4 Wave C2 — FILTERS Reference Partial** |

**Single primary source rule:** Each ready target has exactly one primary source ID above. No competing primaries.

---

## 25. Evidence Paths

### Authority

- `projects/mars-website-factory/wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md`
- `reports/wf-r01-3-4-catalog-vertical-profile-references-charter-pass-v1.md`
- `reports/wf-r01-3-3-exit-and-wf-r01-3-4-handoff-v1.md`
- `reports/wf-r01-3-3-to-wf-r01-3-4-handoff-v1.md`
- `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md`
- `projects/mars-website-factory/global-shell-contract-v1.md`
- `projects/mars-website-factory/page-type-shell-matrix-v1.md`
- `projects/mars-website-factory/reference-scaffold-contract-v1.md`
- `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md`

### Registry

- `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md`
- `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md`
- `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md`
- `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md`
- `workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md`

### BZPM / SITE-002 (primary)

- `projects/ocpilot/sites/site-002/m9-phase1-tables-work/patch/catalog/view/theme/default/template/sections/filterssidebar.twig`
- `projects/ocpilot/sites/site-002/reports/m9.8.9-08a-work/live-capture/catalog__view__theme__default__template__sections__filterssidebar.twig`
- `projects/ocpilot/sites/site-002/category-v2-view-switcher-work/category.twig`
- `projects/ocpilot/sites/site-002/category-v2.1-list-card-commerce-work/productcard.twig`
- `projects/ocpilot/sites/site-002/m7.1-launch-mode-work/patch/catalog/view/theme/default/template/sections/catalogsections.twig`
- `projects/ocpilot/sites/site-002/backups/stable-baselines/SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE/files/catalog/view/theme/default/template/common/megamenu.twig`
- `projects/ocpilot/sites/site-002/reports/m9.8.9-06d-work/plp-stoly-after.html`
- `projects/ocpilot/sites/site-002/reports/m9.8.9-03-work/live-capture/main.js` (reject layer — cited for boundary)
- `projects/ocpilot/sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md`
- `projects/ocpilot/sites/site-002/fa-icon-work/producthero.twig`
- `projects/ocpilot/sites/site-002/w1b-work/producttabs.twig`
- `projects/ocpilot/sites/site-002/reports/SITE-002-CATEGORY-AUDIT-V1.md`
- `projects/ocpilot/sites/site-002/reports/SITE-002-CATEGORY-V2-VIEW-SWITCHER-DESIGN-PLAN.md`

### SIBCAR / SITE-001 (secondary)

- `workspaces/site-001-wf-v3/src/partials/sections/catalog-filters.html`
- `workspaces/site-001-wf-v3/src/partials/sections/catalog-chips.html`
- `workspaces/site-001-wf-v3/src/partials/sections/catalog-body.html`
- `workspaces/site-001-wf-v3/src/partials/sections/catalog-results.html`
- `workspaces/site-001-wf-v3/src/partials/sections/pdp-hero.html`
- `workspaces/site-001-wf-v3/src/pages/catalog.html`
- `projects/ocpilot/sites/site-001/reports/SITE-001-WFV3-CATALOG-DISCOVERY-v1.md`
- `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\wf-v3-master-restore-point-2026-06-14\` (mirror)

### Reference workspace (output target — not modified in C1)

- `workspaces/website-factory-reference-v1/src/partials/components/breadcrumbs.html`
- `workspaces/website-factory-reference-v1/src/partials/components/pagination.html`
- `workspaces/website-factory-reference-v1/src/partials/sections/header-nav.html`
- `workspaces/website-factory-reference-v1/src/partials/sections/footer.html`

### Rejected / non-primary

- `workspaces/isbd-care-landing/` — no catalog patterns
- `workspaces/triumph-manipulator-landing-v6/` — LANDING only
- `.recovery-temp/` — supplementary only; not primary

---

*Inventory version: v1 · Wave C1 · 2026-06-19 · PUBLISHED*
