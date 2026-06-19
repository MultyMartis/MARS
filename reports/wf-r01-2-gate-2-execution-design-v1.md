# REPORT — WF-R01.2 GATE 2 EXECUTION DESIGN

**Subprogram ID:** WF-R01.2 — Registry v1.1 Structural Blocks Layer  
**Program parent:** WF-R01 — FOUNDRY Registry Expansion Program (**CHARTERED**)  
**Version:** v1  
**Date:** 2026-06-19  
**Mode:** execution **design** — **no registry edits**, **no new IDs**, **no implementation**

**Authority consumed:**

| ID | Artifact | Status |
|----|----------|--------|
| Roadmap / index | [roadmap.md](../projects/mars-website-factory/roadmap.md) · [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) | Current |
| WF-R01.2 charter | [wf-r01-2-structural-blocks-charter-v1.md](../projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md) | **ACCEPTED** (Gate 1) |
| Gate 1 pass | [wf-r01-2-structural-blocks-charter-pass-v1.md](wf-r01-2-structural-blocks-charter-pass-v1.md) | Published |
| Program design | [wf-r01-2-structural-blocks-program-design-v1.md](wf-r01-2-structural-blocks-program-design-v1.md) | Gate 0 |
| Vocabulary | [foundry-vocabulary-canon-charter-v1.md](../projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md) | **ACCEPTED** |
| Coverage | [wf-r01-3-1-coverage-model-charter-v1.md](../projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md) · [wf-r01-3-0-coverage-baseline-snapshot-v1.md](wf-r01-3-0-coverage-baseline-snapshot-v1.md) | **ACCEPTED** / G0 |
| Reference waves | [wf-r01-3-2-landing-completion-wave-design-v1.md](wf-r01-3-2-landing-completion-wave-design-v1.md) · [wf-r01-3-reference-expansion-program-design-v1.md](wf-r01-3-reference-expansion-program-design-v1.md) | **DESIGN** |
| Binding | [wf-r01-1-v0-v1-binding-charter-v1.md](wf-r01-1-v0-v1-binding-charter-v1.md) | **ACCEPTED** |
| Research | [rv-01-production-vocabulary.md](../research/foundry/rv-01-production-vocabulary.md) · [rv-02-website-production-systems.md](../research/foundry/rv-02-website-production-systems.md) · [rv-03-pixel-factory.md](../research/foundry/rv-03-pixel-factory.md) | Published |

**Registry surfaces (read-only evidence, 2026-06-19):**

| Surface | Location |
|---------|----------|
| Block contract schema | `workspaces/website-factory-reference-v1/block-registry/BLOCK-CONTRACT-v1.md` |
| Block registry (29 rows) | `block-registry/BLOCK-REGISTRY-v1.md` |
| Site-type matrix | `block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md` |
| Page / blueprint mappings | `PAGE-BLOCK-MAPPING-v1.md` · `BLUEPRINT-BLOCK-MAPPING-v1.md` |
| Dependency rules | `BLOCK-DEPENDENCY-RULES-v1.md` |
| Category system | `BLOCK-CATEGORY-SYSTEM-v1.md` (NAVIGATION **reserved**, empty) |
| OPEN gaps | `BLOCK-REGISTRY-GAPS-v1.md` §2–3 |
| Blueprints | `blueprints/*-BLUEPRINT-v1.md` |

**Honesty boundary:** This document **designs** Gate 2 execution for official introduction of `HEADER_NAV`, `FILTERS`, and `SEARCH` into Registry v1.1. **Not** runtime, **not** reference partials (→ WF-R01.3), **not** row edits in this pass.

**Терминология:** **FOUNDRY** = **Website Factory** ecosystem (строка FOUNDRY как отдельный продукт/путь в repo **не найдена**).

---

## Executive Summary

WF-R01.2 Gate 1 (**ACCEPTED**) зафиксировал Structural Blocks Layer как **F3 Block → Structural Subtype** и Tier A vocabulary (`HEADER_NAV`, `FILTERS`, `SEARCH`) **без** registry rows. Gate 2 — **отдельный execution pass**, который переводит три vocabulary terms в **канонические BLOCK-CONTRACT rows** и синхронизирует matrices / blueprint mappings.

**Блокирующий контекст:** WF-R01.3.2 (LANDING Completion Wave) **жёстко зависит** от Gate 2 для honest `HEADER_NAV` RPC/RC claims. FILTERS/SEARCH rows могут быть созданы **раньше** partials (R01.3.4 W4), но **не** раньше Gate 2 execution authorization.

**Рекомендуемая модель execution:**

```text
Preconditions (R1–R5) verified
    ↓
Single execution pass — additive Registry v1.1 slice
    ├── 3 × BLOCK-CONTRACT rows (HEADER_NAV, FILTERS, SEARCH)
    ├── Matrix v2.1 additive (or v3 if operator prefers version bump)
    ├── PAGE-BLOCK-MAPPING + BLUEPRINT-BLOCK-MAPPING updates
    ├── BLOCK-DEPENDENCY-RULES + BLOCK-CATEGORY-SYSTEM population
    ├── PRODUCT_GRID dependency note closure
    └── BLOCK-REGISTRY-GAPS §2–3 OPEN → CLOSED (Tier A only)
    ↓
Gate 2 completion REPORT + M3 = 3/3 + RC denominator → 32
```

**Scope lock:** Tier A only — **3 rows**, **0** new `block_id` beyond charter vocabulary. MEGA_MENU, SORT_CONTROLS, BREADCRUMBS, PAGINATION — **вне** Gate 2 rows (charter Tier B policy).

**Explicit non-goals (this design):** reference partial HTML/SCSS, npm build, curated-library v2, JSON Schema export, VL3 automation, Blueprint Layer prose rewrites beyond mapping tables.

---

## Structural Contracts

### G2-1 — BLOCK-CONTRACT field requirements per structural block

Authoritative schema: [BLOCK-CONTRACT-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLOCK-CONTRACT-v1.md) — **11 mandatory fields** per `block_id`. Gate 2 execution **must** populate all 11 for each Tier A row.

#### Universal fields (all three blocks)

| Field | Gate 2 requirement |
|-------|-------------------|
| `block_id` | Pre-declared vocabulary terms only — `HEADER_NAV`, `FILTERS`, `SEARCH` — **no minting** |
| `block_name` | Human operator label (see per-block table) |
| `block_category` | `NAVIGATION` — populates currently **reserved empty** category in BLOCK-CATEGORY-SYSTEM-v1 |
| `purpose` | 1–3 sentences; shell vs discovery semantics per WF-R01.2 § Structural Layer Definition |
| `conversion_role` | One primary from BLOCK-CONVERSION-ROLES-v1 |
| `allowed_site_types` | Subset of Core 5; matrix is authoritative override |
| `allowed_page_types` | Subset of PAGE-TYPE-REGISTRY-v1; global shell blocks may use **global scope note** in `notes` |
| `required_or_optional` | Registry default before matrix override |
| `dependencies` | Hard (`requires`) + soft (`recommends`) per BLOCK-DEPENDENCY-RULES-v1 |
| `exclusions` | Forbidden pairings — cite charter duplicate-risk rules |
| `notes` | Variants, HITL, layout-shell-governance, WF-R01.1 role bindings |

#### WF-R01.6 / Vocabulary Canon extensions (mandatory at Gate 2)

Per [foundry-vocabulary-canon-charter-v1.md](../projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md) REG-VOC-08/09 and charter § Registry Readiness Rules:

| Extension attribute | Requirement |
|---------------------|-------------|
| **`maturity`** | RV-01-aligned: `standard` \| `common` \| `specialized` — stored in `notes` until R01.6 formalizes column |
| **`context_dependent`** | `true` for all three — **SITE-TYPE-BLOCK-MATRIX row required before row is ACCEPTED** |
| **`structural_subtype`** | `true` — F3 subtype marker in `notes` (not separate family) |
| **`vocabulary_source`** | `WF-R01.2 ACCEPTED charter` + RV-01 citation |
| **`reference_partial`** | `PENDING — WF-R01.3` until T1+ partial exists |

#### Per-block contract design (execution target values)

##### `HEADER_NAV`

| Field | Design value |
|-------|--------------|
| **block_name** | Header / primary navigation |
| **block_category** | `NAVIGATION` |
| **purpose** | Global shell navigation: brand anchor, primary menu, utility slots (account/cart/phone/language), mobile drawer — **persistent across route groups**; enables orientation and IA traversal without carrying page narrative |
| **conversion_role** | `SYSTEM` |
| **allowed_site_types** | `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`; `LANDING` — **contextual minimal** (document in matrix, not full catalog chrome) |
| **allowed_page_types** | All Core page types where Blueprint applies global shell — explicit list: `HOME_PAGE`, `LANDING_PAGE`, `SERVICE_PAGE`, `CATEGORY_PAGE`, `PRODUCT_PAGE`, `ABOUT_PAGE`, `CONTACT_PAGE`, `FAQ_PAGE`, `REVIEWS_PAGE`, `LEGAL_PAGE` |
| **required_or_optional** | `Contextual` (registry default) |
| **dependencies** | **recommends** `FOOTER` + `LEGAL_LINKS` for production shell pair; **requires** Blueprint global shell zone; **requires** [layout-shell-governance.md](../projects/mars-website-factory/layout-shell-governance.md) — **HEADER ≠ HERO** |
| **exclusions** | **Forbidden** absorption of `HERO` content; **Forbidden** as separate ids: `MEGA_MENU`, `MOBILE_NAV_DRAWER`, `UTILITY_NAV`, `SKIP_LINK` — documented as variants/composition in `notes` |
| **notes** | `maturity: standard` (RV-01 Core); `context_dependent: true`; `mega_menu: variant` (not separate block_id); `utility_nav: composition` (cart icon ≠ `CART` page block); WF-R01.1 role `nav_mega_or_primary` → this id; reference partial **PENDING** R01.3.3 W2 |

##### `FILTERS`

| Field | Design value |
|-------|--------------|
| **block_name** | Filters / refinement controls |
| **block_category** | `NAVIGATION` |
| **purpose** | Faceted and refinement controls on PLP/list surfaces — **control surface** operating on inventory views; distinct from `PRODUCT_GRID` **result surface** |
| **conversion_role** | `INFORMATIONAL` |
| **allowed_site_types** | `CATALOG`, `ECOMMERCE`; `CORPORATE` — catalog subtree only; **excluded** `LANDING`, `PROMO` |
| **allowed_page_types** | `CATEGORY_PAGE` (primary); `HOME_PAGE` when catalog hub exposes filterable grid; utility route groups per Blueprint |
| **required_or_optional** | `Contextual` |
| **dependencies** | **requires** `PRODUCT_GRID` or list context on page; **recommends** `CATEGORIES` taxonomy; **recommends** `HEADER_NAV` (shell); sort order = **sub-variant in notes** (`SORT_CONTROLS` forbidden as id); facet chips / results meta = FILTERS notes |
| **exclusions** | **Forbidden** on `LANDING`, `PROMO`; **Forbidden** merge into `PRODUCT_GRID` markup; **Forbidden** separate `SORT_CONTROLS`, `FACET_CHIPS`, `RESULTS_META` ids |
| **notes** | `maturity: common` (RV-01 context-dependent Core); `context_dependent: true`; faceted SEO URL behavior → **WF-R01.5 FUTURE**; BZPM evidence = vocabulary mining only; reference partial **PENDING** R01.3.4 W4 |

##### `SEARCH`

| Field | Design value |
|-------|--------------|
| **block_name** | Site / catalog search |
| **block_category** | `NAVIGATION` |
| **purpose** | Query entry (header field, overlay, or dedicated surface), suggestions, and routing to results — discovery primitive for large IA and catalog findability |
| **conversion_role** | `INFORMATIONAL` |
| **allowed_site_types** | `CATALOG`, `ECOMMERCE` (obligatory); `PROMO`, `CORPORATE` (recommended); **forbidden/default off** `LANDING` |
| **allowed_page_types** | Global shell (all multi-page types above); results host page — `SEARCH_RESULTS_PAGE` **glossary/planned** (see SAFE UNKNOWN); until page_type row exists, document `/search/` route in Blueprint notes |
| **required_or_optional** | `Contextual` |
| **dependencies** | **recommends** `HEADER_NAV` (typical placement); **recommends** `PRODUCT_GRID` on results pages; **pairs with** `FILTERS` on catalog surfaces (soft, not hard requires) |
| **exclusions** | **Forbidden** as primary conversion surface on `LANDING`; **Forbidden** duplication of `CATEGORIES` tree navigation semantics |
| **notes** | `maturity: common` (RV-01); `context_dependent: true`; RV-01 flags Search Results as **Missing** page type — R01.3.4 scaffold; reference partial **PENDING** R01.3.4 W4 |

#### Contract validation checklist (per row, documentation-level)

| Check | HEADER_NAV | FILTERS | SEARCH |
|-------|------------|---------|--------|
| Unique `block_id` | ✓ | ✓ | ✓ |
| NAVIGATION category assignment | ✓ | ✓ | ✓ |
| Conversion role assigned | ✓ | ✓ | ✓ |
| SITE-TYPE-BLOCK-MATRIX row | **Required** | **Required** | **Required** |
| PAGE-BLOCK-MAPPING stances | **Required** | **Required** | **Required** |
| BLUEPRINT-BLOCK-MAPPING stances | **Required** | **Required** | **Required** |
| Dependency closure (existing ids only) | ✓ | ✓ | ✓ |
| `maturity` + `context_dependent` in notes | ✓ | ✓ | ✓ |

#### Legacy row hygiene (in-scope for Gate 2)

| Existing row | Gate 2 side-effect |
|--------------|-------------------|
| `PRODUCT_GRID` | Update `dependencies` / `notes`: replace «recommends filters (GAP)» → **recommends** `FILTERS` |
| `FOOTER` | No category change; confirm shell ordering note in BLOCK-REGISTRY-GAPS closure |

---

## Vocabulary Alignment

### G2-2 — Relations to Vocabulary Canon (HEADER_NAV, MEGA_MENU, SEARCH, FILTERS)

Structural entities remain **F3 Block → Structural Subtype** — not F7, not Commercial Pattern (F4), not Trust (F5), not SEO Surface (F6).

#### Entity relationship model

```text
F3 Block Family
└── Structural Subtype
    ├── HEADER_NAV (block_id) ──variant──► MEGA_MENU (vocabulary only)
    │                      ──variant──► MOBILE_NAV_DRAWER
    │                      ──composition──► UTILITY_NAV (cart/account/phone)
    ├── SEARCH (block_id)
    └── FILTERS (block_id) ──sub-variant──► SORT_CONTROLS, FACET_CHIPS, RESULTS_META
```

#### Canon rule mapping

| Vocabulary Canon rule | Gate 2 alignment |
|----------------------|------------------|
| **REG-VOC-04** structural-before-marketing | BLOCK-CONTRACT `notes` + PAGE ordering: `HEADER_NAV` → [layout breadcrumbs] → `FILTERS` → `PRODUCT_GRID` → [layout pagination] → `FOOTER` |
| **REG-VOC-05/06** pattern ≠ block | `scroll_process_timeline`, `rfq-v1` etc. stay F4 — **not** structural rows |
| **REG-VOC-08** maturity on every row | `standard` (HEADER_NAV), `common` (FILTERS, SEARCH) in notes |
| **REG-VOC-09** context_dependent → matrix | All three `context_dependent: true`; matrix update **same pass** as rows |
| **hero vs header_nav** glossary | HEADER_NAV `exclusions` cite HEADER ≠ HERO; no `HERO` dependency |
| **AUTH-01/02** research/charter ≠ auto rows | Gate 2 is **explicit execution** — RV-01 informs `maturity`, not auto-promotion |

#### Cross-entity disposition table

| Term | Relationship to HEADER_NAV | Relationship to SEARCH | Relationship to FILTERS | Registry action Gate 2 |
|------|---------------------------|------------------------|-------------------------|------------------------|
| **MEGA_MENU** | **Variant** — `mega_menu: true` in HEADER_NAV notes | — | — | **No row** |
| **MOBILE_NAV_DRAWER** | **Variant** — implementation | — | — | **No row** |
| **UTILITY_NAV** | **Composition inside** HEADER_NAV | — | — | **No row** |
| **SEARCH** | Soft recommends (typical co-placement) | — | Soft pair on catalog | **Row** |
| **FILTERS** | Independent shell vs PLP context | Soft pair | — | **Row** |
| **BREADCRUMBS** | Independent (layout policy Tier B) | — | — | **No row** v1.1 |
| **PAGINATION** | — | — | Adjacent list nav (layout policy) | **No row** v1.1 |
| **CATEGORIES** | Adjacent IA (tree vs global menu) | Distinct discovery | FILTERS requires list context | Existing row — no change |
| **PRODUCT_GRID** | — | Results surface | FILTERS **control** vs grid **result** | Update dependency note |
| **CART** | Mini-cart = HEADER_NAV utility; `CART` = page flow | — | — | No new row |

#### WF-R01.1 binding harmonization

| v0 role / legacy | v1 `block_id` | Gate 2 action |
|------------------|---------------|---------------|
| `nav_mega_or_primary` | `HEADER_NAV` | Row + notes binding |
| Layout `header.html` ad-hoc | `HEADER_NAV` partial (R01.3) | **Not** Gate 2 — reference only |
| Blueprint «Filters / Search» labels | `FILTERS`, `SEARCH` | Close BLOCK-REGISTRY-GAPS §2 |

#### RV-01 / RV-02 / RV-03 alignment

| Research | Gate 2 use |
|----------|------------|
| **RV-01** | HEADER_NAV = Core **standard** Missing→row; FILTERS/SEARCH = **common** context-dependent; structural-before-marketing ordering |
| **RV-02** | structural_block vs content_block boundary in `purpose` / `exclusions` — no code-layer claims |
| **RV-03** | **No** structural vocabulary — orthogonal; Gate 2 does not unlock WF-A03 |

---

## Matrix Impact

### G2-3 — Matrices and registry artifacts requiring update

Gate 2 execution is **one coherent pass** — matrix drift between artifacts is **forbidden**.

#### Primary matrices (mandatory)

| Artifact | Version strategy | Change summary |
|----------|------------------|----------------|
| **SITE-TYPE-BLOCK-MATRIX-v2** | **v2.1 additive** (recommended) or **v3** (if operator wants structural milestone version) | Add 3 rows × 5 Core site types per charter § Site Type Impact |
| **PAGE-BLOCK-MAPPING-v1** | In-place additive section + per-page updates | Global shell stances; `CATEGORY_PAGE` FILTERS; SEARCH global + results |
| **BLUEPRINT-BLOCK-MAPPING-v1** | In-place additive | CATALOG/ECOMMERCE/PROMO/CORPORATE structural REQUIRED/OPTIONAL |
| **BLOCK-DEPENDENCY-RULES-v1** | In-place additive § Structural | New rules + PRODUCT_GRID closure |
| **BLOCK-CATEGORY-SYSTEM-v1** | In-place — populate NAVIGATION | Assign HEADER_NAV, FILTERS, SEARCH |
| **BLOCK-REGISTRY-v1** | **v1.1 additive** (3 new sections) | Tier A BLOCK-CONTRACT instances |
| **BLOCK-REGISTRY-GAPS-v1** | Gap closure audit | §2 Blueprint → CLOSED Tier A; §3 where applicable |

#### Secondary artifacts (same pass or immediate follow-up)

| Artifact | Change |
|----------|--------|
| **BLOCK-CONVERSION-ROLES-v1** | Register three ids under SYSTEM / INFORMATIONAL |
| **CORE-BLOCK-LIBRARY-v1** | Add Structural Layer subsection (3 ids) |
| **BLOCK-REGISTRY-AUDIT-v1** | Note v1.1 structural promotion — audit trail |
| **BLOCK-GAPS-v1** | Close «header/nav», «filters/search» implementation gap labels → registry **done**, partials **OPEN** |
| **BLUEPRINT-COMPARISON-MATRIX-v1** | Align Filters/search row with block_id (currently checkmark without id) |
| **SITE-TYPE-REGISTRY-v1** | **No new site_type_code** — verify Included features text references registry rows post-Gate 2 |

#### SITE-TYPE-BLOCK-MATRIX — proposed stances (binding design)

Legend: **R** = REQUIRED · **O** = OPTIONAL · **F** = FORBIDDEN · **P** = Policy-dependent / minimal

| block_id | LANDING | PROMO | CATALOG | ECOMMERCE | CORPORATE |
|----------|---------|-------|---------|-----------|-----------|
| **HEADER_NAV** | P (minimal) | **R** | **R** | **R** | **R** |
| **SEARCH** | F | O | **R** | **R** | O |
| **FILTERS** | F | F | **R** | **R** | P (catalog subtree) |

**LANDING `P` semantics:** optional minimal header chrome — **not** catalog SEARCH/FILTERS; aligns with charter «structural absence intentional».

#### PAGE-BLOCK-MAPPING — key page_type updates

| page_type | HEADER_NAV | FILTERS | SEARCH |
|-----------|------------|---------|--------|
| `LANDING_PAGE` | OPTIONAL (minimal) | FORBIDDEN | FORBIDDEN |
| `HOME_PAGE` | REQUIRED (multi-page types) | OPTIONAL (catalog home) | OPTIONAL |
| `SERVICE_PAGE` | REQUIRED | FORBIDDEN | OPTIONAL |
| `CATEGORY_PAGE` | REQUIRED | **REQUIRED** | OPTIONAL (PLP context) |
| `PRODUCT_PAGE` | REQUIRED | FORBIDDEN | OPTIONAL |
| `ABOUT_PAGE` / `CONTACT_PAGE` / `FAQ_PAGE` | REQUIRED | FORBIDDEN | OPTIONAL |
| `LEGAL_PAGE` | REQUIRED | FORBIDDEN | FORBIDDEN |
| `SEARCH_RESULTS` (planned) | REQUIRED | OPTIONAL | **REQUIRED** (host) |

#### BLUEPRINT-BLOCK-MAPPING — key blueprint updates

| Blueprint | HEADER_NAV | FILTERS | SEARCH |
|-----------|------------|---------|--------|
| **LANDING** | OPTIONAL (minimal) | FORBIDDEN | FORBIDDEN |
| **PROMO** | **REQUIRED** (global) | FORBIDDEN | OPTIONAL |
| **CATALOG** | **REQUIRED** (global) | **REQUIRED** (PLP) | **REQUIRED** |
| **ECOMMERCE** | **REQUIRED** | **REQUIRED** | **REQUIRED** |
| **CORPORATE** | **REQUIRED** | OPTIONAL (subtree) | OPTIONAL |

#### BLOCK-DEPENDENCY-RULES — new rules (design)

| Subject | Rule |
|---------|------|
| `HEADER_NAV` | **recommends** `FOOTER`, `LEGAL_LINKS`; **forbidden** merge with `HERO` |
| `FILTERS` | **requires** `PRODUCT_GRID` on same page (PLP); **recommends** `CATEGORIES` |
| `SEARCH` | **recommends** `HEADER_NAV`; on results page **recommends** `PRODUCT_GRID` or list module |
| `PRODUCT_GRID` | **recommends** `FILTERS` when filterable PLP (update existing GAP note) |
| `PRODUCT_CARD` | unchanged — PDP does not require FILTERS |

#### Metrics impact

| Metric | Pre–Gate 2 | Post–Gate 2 |
|--------|------------|-------------|
| **M3** (structural ids in registry) | 0/3 | **3/3** |
| **RC** denominator | 29 (+3 vocabulary-only) | **32/32** Core+structural rows |
| **RPC** denominator | 9/32 (~28%) preferred | Unchanged until R01.3 partials |
| **BLOCK-REGISTRY-GAPS** Tier A | OPEN | **CLOSED** (audit evidence) |

---

## Blueprint Impact

### G2-4 — Blueprint surfaces touched

Gate 2 **does not** rewrite Blueprint narrative prose by default — it **closes the mapping gap** between Blueprint human labels and `block_id`. Operator may add cross-links in a **hygiene pass** (WF-R01.6).

#### Blueprint documents — mapping impact

| Blueprint file | Current structural signal | Gate 2 action |
|----------------|--------------------------|---------------|
| [CATALOG-BLUEPRINT-v1.md](../workspaces/website-factory-reference-v1/blueprints/CATALOG-BLUEPRINT-v1.md) | Global: Header/nav · PLP: Filters; `/search/` route | Map to `HEADER_NAV`, `FILTERS`, `SEARCH`; no cart/checkout change |
| [ECOMMERCE-BLUEPRINT-v1.md](../workspaces/website-factory-reference-v1/blueprints/ECOMMERCE-BLUEPRINT-v1.md) | Global: Header/nav · PLP: Filters | Same structural trio REQUIRED |
| [PROMO-BLUEPRINT-v1.md](../workspaces/website-factory-reference-v1/blueprints/PROMO-BLUEPRINT-v1.md) | Global: Header/nav | `HEADER_NAV` REQUIRED; SEARCH optional |
| [CORPORATE-BLUEPRINT-v1.md](../workspaces/website-factory-reference-v1/blueprints/CORPORATE-BLUEPRINT-v1.md) | Mega/primary nav | `HEADER_NAV` REQUIRED; mega = variant note |
| [LANDING-BLUEPRINT-v1.md](../workspaces/website-factory-reference-v1/blueprints/LANDING-BLUEPRINT-v1.md) | Header (minimal) | `HEADER_NAV` OPTIONAL/minimal; reclassify triggers unchanged |

#### Blueprint system artifacts

| Artifact | Gate 2 touch |
|----------|--------------|
| [BLUEPRINT-BLOCK-MAPPING-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLUEPRINT-BLOCK-MAPPING-v1.md) | **Primary** — add structural columns/rows |
| [BLUEPRINT-COMPARISON-MATRIX-v1.md](../workspaces/website-factory-reference-v1/blueprints/BLUEPRINT-COMPARISON-MATRIX-v1.md) | Filters/search row → cite `block_id` |
| [BLUEPRINT-GAPS-v1.md](../workspaces/website-factory-reference-v1/blueprints/BLUEPRINT-GAPS-v1.md) | Note: structural **registry** closed; partial variants still OPEN |
| [BLUEPRINT-SYSTEM-v1.md](../workspaces/website-factory-reference-v1/blueprints/BLUEPRINT-SYSTEM-v1.md) | Cross-link only if operator chooses sync pass |

#### Page architecture (readiness, not full expansion)

| Surface | Gate 2 relationship |
|---------|----------------------|
| [CORE-PAGE-ARCHITECTURES-v1.md](../workspaces/website-factory-reference-v1/page-architecture/CORE-PAGE-ARCHITECTURES-v1.md) | Implicit structural zones → cite block_id in operator notes |
| [PAGE-GAPS-v1.md](../workspaces/website-factory-reference-v1/page-architecture/PAGE-GAPS-v1.md) | `SEARCH_RESULTS_PAGE` may remain glossary-only — **SAFE UNKNOWN** |
| [PAGE-BLOCK-MAPPING-v1.md](../workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md) | **Primary** page-level stances |

#### What Gate 2 does **not** change in Blueprint Layer

- Route trees (`/search/`, category URLs) — already in CATALOG blueprint
- Reclassification rules (LANDING → CATALOG on filters)
- ECOMMERCE legal E1–E4
- BREADCRUMBS / PAGINATION — remain **layout-component policy** (Tier B)

---

## Site Type Impact

### G2-5 — Impact on LANDING, PROMO, CATALOG, CORPORATE, ECOMMERCE

#### Summary matrix (post–Gate 2 registry honesty)

| Site type | HEADER_NAV | SEARCH | FILTERS | Template-Art effect (registry layer only) |
|-----------|------------|--------|---------|-------------------------------------------|
| **LANDING** | P — minimal optional | F | F | Vocabulary allows minimal shell; **no** catalog chrome forced |
| **PROMO** | **R** | O | F | Multi-page IA **blueprintable** at registry level; partials still R01.3 |
| **CATALOG** | **R** | **R** | **R** | PLP/PDP **honest** at BLOCK-CONTRACT level; RPC still blocked until R01.3.4 |
| **ECOMMERCE** | **R** (+ utility composition in notes) | **R** | **R** | Above + cart/account utilities in HEADER_NAV notes — not new ids |
| **CORPORATE** | **R** | O | P (catalog subtree) | Deep IA + optional catalog subtree filters/search |

#### Obligatory structural minimum (registry truth)

| Class | Post–Gate 2 minimum | Without Gate 2 |
|-------|---------------------|----------------|
| **CATALOG / ECOMMERCE** | HEADER_NAV + FILTERS + SEARCH rows + matrix **R** | BLOCK-REGISTRY-GAPS §2 **OPEN** — dishonest blueprints |
| **PROMO / CORPORATE** | HEADER_NAV **R** | Navigation exists only as layout ad hoc |
| **LANDING** | None **required** | Current reference workspace **valid** |

#### Vertical compositions (no new `site_type_code`)

| Profile | Gate 2 inheritance |
|---------|-------------------|
| **MANUFACTURER** | CATALOG + CORPORATE matrix + MEGA_MENU variant on HEADER_NAV notes |
| **AUTO** | CATALOG set; FILTER variants in notes only |
| **MARKETPLACE** (Extended) | **Out of Core matrix** — classification hints only per charter |

#### Catalog surface ordering (constraint graph — unchanged)

```text
HEADER_NAV → [BREADCRUMBS layout] → [page intro] → FILTERS → PRODUCT_GRID → [PAGINATION layout] → FOOTER
```

Gate 2 rows **encode** FILTERS and HEADER_NAV positions; breadcrumbs/pagination stay layout policy.

---

## Reference Expansion Impact

### G2-6 — Impact on WF-R01.3.2, WF-R01.3.3, WF-R01.3.4

#### Dependency overview

```text
WF-R01.2 Gate 2 (registry rows)
    │
    ├──► WF-R01.3.2 G1 — HEADER_NAV row required for honest RC/RPC (Wave C)
    │         FOOTER/LEGAL_LINKS — no Gate 2 dependency
    │         FILTERS/SEARCH — out of 3.2 scope
    │
    ├──► WF-R01.3.3 — shell partials; HEADER_NAV depth; residual policy
    │         Overlap: FOOTER/LEGAL_LINKS may complete in 3.2
    │
    └──► WF-R01.3.4 G2 — FILTERS, SEARCH partials (W4)
              Requires HEADER_NAV T1+ from 3.2/3.3
              Requires Gate 2 rows for all three before honest catalog RPC
```

#### WF-R01.3.2 — LANDING Completion Wave

| Aspect | Gate 2 impact |
|--------|---------------|
| **Wave C (HEADER_NAV)** | **Hard dependency** — C1 registry row before C2 partial (WF-R01.1 B3) |
| **Parallel policy** | Gate 2 row authoring **may run parallel** with Wave A/B (BENEFITS, FOOTER) |
| **G1-6 criterion** | HEADER_NAV registry row **or** explicit waiver — Gate 2 satisfies row path |
| **RC target** | G1 may claim **32/32** RC if all three structural rows done; minimum **HEADER_NAV** for shell honesty |
| **FILTERS/SEARCH** | **Out of scope** 3.2 — rows may be pre-authored in Gate 2 without partials |

#### WF-R01.3.3 — Structural & Shell References (DESIGN in parent program)

| Aspect | Gate 2 impact |
|--------|---------------|
| **Scope shift** | If 3.2 completes FOOTER/LEGAL_LINKS, 3.3 focuses on **HEADER_NAV depth**, breadcrumbs/pagination layout policy, global shell scaffold |
| **BLOCK-CONTRACT** | 3.3 partial work **consumes** Gate 2 rows — does not recreate ids |
| **MEGA_MENU** | Remains HEADER_NAV variant in notes — BZPM depth mining in 3.3/3.4 doc-first |

#### WF-R01.3.4 — Catalog & Vertical Profile References (DESIGN in parent program)

| Aspect | Gate 2 impact |
|--------|---------------|
| **W4 deliverables** | FILTERS, SEARCH partials — **blocked** without Gate 2 rows |
| **G2 gate (20/32 RPC)** | Structural **RPC** for FILTERS/SEARCH counts toward G2 only **after** rows + T1+ partials |
| **PLP scaffold** | Composition `HEADER_NAV → … → FILTERS → PRODUCT_GRID` requires all three registry rows |
| **BZPM feed** | Vocabulary mining — rows must exist before Factory claims equivalence |
| **SEARCH_RESULTS_PAGE** | Scaffold may expose need for page_type charter — **orthogonal** to Gate 2 block rows |

#### Coverage metrics coupling

| Dimension | Gate 2 alone | Gate 2 + R01.3 partials |
|-----------|--------------|---------------------------|
| **RC** | **+3** (→ 32/32) | unchanged |
| **RPC** | **+0** (no partials) | +1 per T1+ partial |
| **SC** | Enables honest **claims** | Requires WF-R01.7 + checklist |
| **M3** | **3/3** | unchanged |

---

## Gate 2 Completion Criteria

### G2-7 — Gate 2 Completion Criteria

#### Preconditions (hard — must be satisfied before row edits)

| ID | Condition | Design status |
|----|-----------|---------------|
| **R1** | WF-R01.2 charter **ACCEPTED** | ✅ Satisfied |
| **R2** | WF-R01.1 binding charter **ACCEPTED** (B1) | ✅ Satisfied |
| **R3** | WF-R01.1 **B3** STOP rule live in OPERATIONAL-INDEX | ⏳ **Pending** — **recommended hard gate** |
| **R4** | Separate execution task authorized (this design → operator sign-off → execution pass) | ⏳ **This document** — authorization follows human review |
| **R5** | No mixed v0/v1 `block_id` in target blueprint/matrix artifacts | ⏳ Verify at execution start |

#### Execution deliverables (all required for Gate 2 **COMPLETE**)

| # | Deliverable | Acceptance evidence |
|---|-------------|---------------------|
| **D1** | Three BLOCK-CONTRACT rows in BLOCK-REGISTRY-v1.1: `HEADER_NAV`, `FILTERS`, `SEARCH` | Registry diff; all 11 fields + maturity/context_dependent notes |
| **D2** | SITE-TYPE-BLOCK-MATRIX updated (v2.1 or v3) — 3×5 stances | Matrix agrees with charter § Site Type Impact |
| **D3** | PAGE-BLOCK-MAPPING-v1 updated — global shell + CATEGORY_PAGE | CATEGORY_PAGE FILTERS **REQUIRED** |
| **D4** | BLUEPRINT-BLOCK-MAPPING-v1 updated — 5 Core blueprints | CATALOG/ECOMMERCE structural trio **REQUIRED** |
| **D5** | BLOCK-DEPENDENCY-RULES-v1 — structural section + PRODUCT_GRID fix | Dependency closure audit |
| **D6** | BLOCK-CATEGORY-SYSTEM-v1 — NAVIGATION populated (3 ids) | Category no longer empty reserved |
| **D7** | BLOCK-REGISTRY-GAPS-v1 — §2 Tier A **OPEN → CLOSED** | Gap audit REPORT |
| **D8** | WF-R01.1 role `nav_mega_or_primary` → `HEADER_NAV` **no longer PENDING** | Binding table update in execution REPORT |
| **D9** | Gate 2 completion REPORT published | M3, RC, five-dimension snapshot |
| **D10** | **Zero** new `block_id` beyond Tier A vocabulary | Charter scope lock |

#### Success metrics

| Metric | Target |
|--------|--------|
| **M3** | **3/3** structural ids **in registry** |
| **RC** | **32/32** (29 Core + 3 structural) |
| **RPC** | Unchanged until WF-R01.3 — **do not** claim implementation |
| **BLOCK-REGISTRY-GAPS** | HEADER_NAV, FILTERS, SEARCH — **CLOSED** |

#### Explicitly **not** Gate 2 complete

| Exclusion | Routed to |
|-----------|-----------|
| Reference partials (HEADER_NAV, FILTERS, SEARCH HTML/SCSS) | WF-R01.3.2 / 3.3 / 3.4 |
| `npm run build` PASS for structural partials | WF-R01.3 waves |
| BREADCRUMBS / PAGINATION `block_id` | Tier B layout policy |
| MEGA_MENU separate row | **Forbidden** |
| Template-Art multi-type production unlock | WF-R01.7 + R01.3 G2+ |
| JSON Schema / CI matrix validation | Post-R01 tooling |
| OPERATIONAL-INDEX / roadmap status bump | Optional hygiene in same pass — **not** gate blocker |

#### Recommended execution sequencing (single pass internal order)

```text
1. Pre-flight: R3 B3 verify · R5 v0/v1 scan · backup pointer
2. BLOCK-REGISTRY-v1.1 — add 3 contract sections
3. BLOCK-CATEGORY-SYSTEM + BLOCK-CONVERSION-ROLES
4. SITE-TYPE-BLOCK-MATRIX
5. BLUEPRINT-BLOCK-MAPPING + PAGE-BLOCK-MAPPING (same PR/pass — consistency check)
6. BLOCK-DEPENDENCY-RULES + PRODUCT_GRID note fix
7. BLOCK-REGISTRY-GAPS closure + CORE-BLOCK-LIBRARY pointer
8. Gate 2 completion REPORT · M3 · RC 32/32
```

#### Authorization model

| Step | Actor |
|------|-------|
| Design review (this document) | Operator / governance |
| Execution authorization | Human charter pass or operator sign-off (**R4**) |
| Row edits | Single WF-R01.2 Gate 2 **execution** task |
| HITL on faceted SEO / mega-menu depth | Deferred — notes only at Gate 2 |

---

## Risks

| Risk | Severity | Mitigation in Gate 2 design |
|------|----------|----------------------------|
| **False «structural complete»** after rows without partials | Critical | REPORT must cite **RPC** unchanged; M3 ≠ M2 |
| **HEADER_NAV before B3 STOP** | Critical | R3 precondition; mixed v0/v1 halt |
| **MEGA_MENU minted as separate id** | High | Charter forbidden; notes-only variant |
| **FILTERS merged into PRODUCT_GRID** | High | Separate rows; dependency graph |
| **Matrix / blueprint drift** | High | Single pass; cross-artifact consistency check |
| **Scope creep** — Tier B ids in Gate 2 | Critical | D10 scope lock; BREADCRUMBS waiver separate |
| **TEMPLATE_ART CATALOG** claimed on RC alone | Critical | SC/RPC still blocked until R01.3.4 |
| **BZPM OpenCart → Factory false equivalence** | High | Rows = vocabulary; BZPM mining doc-only |
| **SEARCH_RESULTS_PAGE orphan** | Medium | PAGE-BLOCK-MAPPING notes + R01.3.4 scaffold |
| **Faceted SEO policy absent** | Medium | WF-R01.5 FUTURE note on FILTERS row |
| **Gate 2 delayed blocks R01.3.2 G1** | Medium | Parallel row authoring; waiver path documented in 3.2 |

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| **Named WF-R01.2 Gate 2 steward** | **Not fixed** in repo |
| **WF-R01.1 B3–B8** full implementation | **Pending** — B3 minimum for execution |
| **Matrix version bump: v2.1 vs v3** | **Operator choice** at execution |
| **`SEARCH_RESULTS_PAGE` in PAGE-TYPE-REGISTRY** | **Not verified** — `/search/` in CATALOG blueprint only |
| **JSON Schema for structural rows** | **NOT DEFINED** (R01.6) |
| **Automated matrix validation** | **NOT IMPLEMENTED** |
| **Faceted SEO URL policy for FILTERS** | **FUTURE** — WF-R01.5 |
| **OCPilot SITE-001 v1 binding** | **Not verified** |
| **BZPM W3 blueprint delivery date** | **UNKNOWN** |
| **WF-R01.3.3 / 3.4 separate ACCEPTED charters** | **Not published** — parent R01.3 remains DESIGN |
| **Whether Gate 2 execution requires separate ACCEPTED pass** | **Recommended yes** per R01.1/R01.2 pattern — follows this design review |
| **T_cutover** calendar date | **Pending** WF-R01.1 P4 |
| **VL3 structural surface validators** | **Not implemented** — WF-A02 doc only |

---

## Recommended Next Step

1. **Operator review** this Gate 2 execution design — confirm BLOCK-CONTRACT values, matrix stances, and completion criteria D1–D10.
2. **Unblock R3:** implement WF-R01.1 **B3** STOP rule minimum in OPERATIONAL-INDEX before registry row execution.
3. **Authorize WF-R01.2 Gate 2 execution pass** (separate task) — apply D1–D10 in one coherent registry edit pass.
4. **Parallel (non-blocking for rows):** WF-R01.3.2 Wave A/B may continue; coordinate Wave C with Gate 2 completion.
5. **Pre-author optional:** all three structural rows in one Gate 2 pass even if FILTERS/SEARCH partials wait for R01.3.4.
6. **Publish** Gate 2 completion REPORT with M3 = 3/3, RC = 32/32, and explicit RPC unchanged statement.
7. **Do not** start FILTERS/SEARCH T1+ partials until rows exist and R01.3.4 wave is authorized.

**STOP AFTER REPORT — NO REGISTRY CHANGES — NO NEW IDS — NO IMPLEMENTATION**

---

*Design artifact: `reports/wf-r01-2-gate-2-execution-design-v1.md`*  
*Authority: `projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md` (ACCEPTED, Gate 1)*
