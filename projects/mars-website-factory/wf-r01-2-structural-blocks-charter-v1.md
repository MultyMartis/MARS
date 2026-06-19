# WF-R01.2 — Structural Blocks Layer Charter v1

**Subprogram ID:** WF-R01.2 — Registry v1.1 Structural Blocks Layer  
**Program parent:** WF-R01 — FOUNDRY Registry Expansion Program (**CHARTERED**)  
**Version:** v1  
**Date:** 2026-06-19  
**Charter pass:** [wf-r01-2-structural-blocks-charter-pass-v1.md](../../reports/wf-r01-2-structural-blocks-charter-pass-v1.md)  
**Design basis:** [wf-r01-2-structural-blocks-program-design-v1.md](../../reports/wf-r01-2-structural-blocks-program-design-v1.md)

**Honesty boundary:** WF-R01.2 — **documentation and vocabulary-layer charter** (human-operated). **Не** runtime, **не** orchestration, **не** reference partial expansion (→ WF-R01.3), **не** registry row edits in this artifact.

**Терминология:** **FOUNDRY** = **Website Factory** ecosystem (строка FOUNDRY как отдельный продукт/путь в repo **не найдена**).

---

## Charter sign-off

| Field | Value |
|-------|-------|
| **Status** | **ACCEPTED** |
| **Acceptance state** | Structural Blocks Layer **official FOUNDRY vocabulary authority**; registry v1.1 row promotion **not authorized** by this charter alone |
| **Authority state** | WF-R01.2 = **ACCEPTED** (subprogram layer charter) · WF-R01 program = **CHARTERED** (program **not ACTIVE** until subprogram execution P2+) |
| **T0** | **2026-06-19** — date of ACCEPTED publication |
| **Owner** | Website Factory operator governance (human-operated sign-off via charter pass; **named steward SAFE UNKNOWN**) |
| **Prior state** | DESIGN — [wf-r01-2-structural-blocks-program-design-v1.md](../../reports/wf-r01-2-structural-blocks-program-design-v1.md) |
| **Gate 0 (design)** | **Satisfied** — program design ACCEPTED via this charter pass |
| **Gate 1 (charter)** | **Satisfied** — this artifact |
| **Gate 2 (registry rows)** | **Not satisfied** — separate execution task; see § Registry Readiness Rules |

**ACCEPTED means:** Structural Blocks Layer is an **official part of FOUNDRY vocabulary** under Block Family (F3) → Structural Subtype. Tier A/B/C candidate dispositions, site-type impact, Template-Art prerequisites, and duplicate-risk rules are **binding** for future registry work. **Does not** mean `block_id` rows exist in BLOCK-REGISTRY-v1, reference partials exist, or SITE-TYPE-BLOCK-MATRIX is updated.

---

## Executive Summary

Registry Implementation Cliff остаётся главным bottleneck FOUNDRY: **29** канонических `block_id`, **~9** reference partials (~**31%**), и **OPEN** structural gaps — **HEADER_NAV**, **FILTERS**, **SEARCH** — задокументированы в BLOCK-REGISTRY-GAPS без registry rows.

**WF-R01.2 закрывает vocabulary gap, не registry gap.** Этот charter:

1. **Официально принимает** Structural Blocks Layer как часть FOUNDRY — подсемейство **F3 Block**, не отдельное vocabulary family.
2. **Фиксирует** определение, категории, границы и disposition кандидатов Tier A/B/C **без** создания registry rows.
3. **Согласует** слой с Vocabulary Canon (REG-VOC-04), Research Canon (RV-01–03), WF-A01 Template-Art SSOT, и WF-R01.1 v0→v1 binding.
4. **Определяет** условия Registry v1.1 readiness — что должно быть выполнено **до** первых structural `block_id` rows.

**Минимальный structural canon для будущей registry v1.1 promotion (vocabulary terms — not rows):** `HEADER_NAV`, `FILTERS`, `SEARCH`. Breadcrumbs и pagination — **layout-component policy** для v1.1. Mega-menu — **variant** of header/nav. Thank-you — **page_type policy**, не dedicated block в v1.1.

**Explicit boundary:** ACCEPTED charter **≠** registry expansion execution. Row edits require Gate 2 execution pass + WF-R01.1 **B3 minimum** (STOP rule).

---

## Structural Layer Definition

### What Structural Blocks are

**Structural Blocks** — reusable Block-family (F3) entities describing **persistent shell** and **catalog discovery mechanics**: global navigation, search, filters, breadcrumbs, pagination, and other **task-support** surfaces that:

1. **Span** multiple pages or route groups (global or subtree-scoped).
2. **Do not carry** primary commercial narrative (hero, benefits, pricing story).
3. **Are not** trust proof or SEO editorial body.
4. **Enable** orientation, browse/compare, and task completion in IA.

**Canonical repo anchors:**

| Source | Structural signal |
|--------|-------------------|
| [layout-shell-governance.md](layout-shell-governance.md) | **HEADER ≠ HERO** — header/nav = shell layer, not content block |
| [foundry-vocabulary-canon-charter-v1.md](foundry-vocabulary-canon-charter-v1.md) § F3 | Structural Block = Block subtype; examples: header/nav, search, filters, breadcrumbs, pagination |
| [BLOCK-CATEGORY-SYSTEM-v1.md](../../workspaces/website-factory-reference-v1/block-registry/BLOCK-CATEGORY-SYSTEM-v1.md) | Category `NAVIGATION` — **reserved**; structural ids **not in Core Library v1.0** |
| [BLOCK-REGISTRY-GAPS-v1.md](../../workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-GAPS-v1.md) | Blueprint requires header/nav, filters/search — **OPEN** without `block_id` |
| [wf-r01-1-v0-v1-binding-charter-v1.md](../../reports/wf-r01-1-v0-v1-binding-charter-v1.md) | Role `nav_mega_or_primary` → `HEADER_NAV` (**PENDING** registry row — WF-R01.2 execution) |

**Conversion role (default):** predominantly **SYSTEM** or **INFORMATIONAL** — structural blocks **support** conversion paths; they are **not** primary conversion surfaces (exception: search-as-entry on large catalogs).

### What Structural Blocks are not

| Misclassification | Correct home |
|-------------------|--------------|
| Separate vocabulary family (F7) | **Forbidden** — Structural = F3 subtype only |
| Commercial Pattern (F4) | Pattern composes **inside** blocks; not structural entity |
| Trust Pattern (F5) | Proof surfaces — content band, not shell |
| SEO Surface (F6) | Governs indexation intent; intersects breadcrumbs/filters but **≠** structural charter |
| Layout template / blueprint | Operational instance — references registry; does not mint IDs (AUTH-04) |
| Code component | Developer primitive — implements block; not registry family (RV-02) |

### Layer separation rules

| Layer | Definition | Examples in v1 canon | Relation to Structural |
|-------|------------|----------------------|------------------------|
| **Content Blocks** | Page sections carrying narrative, explanation, or offer story | `HERO`, `BENEFITS`, `FEATURES`, `PROCESS`, `FAQ`, `PRICING` | Structural blocks **frame** content; **do not replace** hero/value sections |
| **Commercial Patterns** | Reusable `pattern_id` semantics | `scroll_process_timeline`, future `rfq-v1` | Patterns **compose inside** blocks; **not** structural entities |
| **Trust Patterns** | Proof, credibility, social validation | `TRUST`, `TESTIMONIALS`, `REVIEWS`, `CASES` | Trust = content-band proof; nav **must not** absorb trust copy |
| **SEO Surfaces** | Planning layer for intent, indexation, meta | SITE-TYPE-SEO-MAPPING-v2, PAGE-SEO-CONTRACT-v1 | SEO governs **how** pages are indexed; structural charter **≠** SEO Pattern Library (→ WF-R01.5) |
| **Catalog product blocks** | Item/category presentation — CATALOG category | `CATEGORIES`, `CATEGORY_GRID`, `PRODUCT_GRID`, `PRODUCT_CARD` | Grids show **inventory**; FILTERS/SEARCH **operate on** grids — dependency, not duplication |
| **System shell (partial)** | Global chrome without full nav semantics | `FOOTER`, `LEGAL_LINKS` | **Overlap:** `FOOTER` exists in v1; **HEADER_NAV** missing — shell incomplete |

### Design rules (vocabulary boundary)

1. **One primary owner** per structural concern — PLP filtering **≠** `PRODUCT_GRID` markup; filters are **control surface**, grid is **result surface**.
2. **Structural blocks may be FORBIDDEN** on pure `LANDING` URLs (minimal nav) per site-type matrix — absence is **intentional**, not a gap (REG-VOC-04 companion policy).
3. **Layout components vs `block_id`:** breadcrumbs and pagination default to **layout-component policy** in v1.1 unless a future charter waives for matrix automation.
4. **MEGA_MENU** — **variant** of header/nav — **not** separate family or mandatory separate `block_id`.
5. **HEADER ≠ HERO** — structural charter **must not** merge shell navigation with hero content blocks.

### Catalog surface ordering (constraint graph)

Per Vocabulary Canon REG-VOC-04 and constraint graph:

```text
HEADER_NAV → BREADCRUMBS → [page intro] → FILTERS → PRODUCT_GRID → PAGINATION → FOOTER
```

Structural block absence on `LANDING` URLs is **policy**, not gap.

---

## Structural Categories

Structural candidates are grouped by **registry promotion tier** — vocabulary disposition only; **no rows created** by this charter.

### Category S1 — Global shell

| Vocabulary term | Purpose | v1.1 disposition |
|-----------------|---------|----------------|
| **HEADER_NAV** | Primary global navigation: brand, menu, utilities, mobile drawer | **Mandatory** — Tier A; future `block_id` promotion required for multi-page Template-Art honesty |
| **FOOTER** | Global footer chrome | **Already exists** in v1 (`FOOTER`); reference partial gap → WF-R01.3 |
| **MEGA_MENU** | Deep taxonomy flyout in header | **Deferred** as separate id — **HEADER_NAV variant** (`mega_menu` capability in notes) |
| **MOBILE_NAV_DRAWER** | Off-canvas menu behavior | **Implementation variant** of HEADER_NAV — **no** separate `block_id` |
| **UTILITY_NAV** | Account, cart icon, language, phone | **Composition inside HEADER_NAV** — **no** separate `block_id` |
| **SKIP_LINK / A11Y_CHROME** | Accessibility jump links | **Layout/shell policy** — **no** `block_id` |

### Category S2 — Discovery and refinement

| Vocabulary term | Purpose | v1.1 disposition |
|-----------------|---------|----------------|
| **SEARCH** | Query entry, suggestions, results routing | **Mandatory** — Tier A for CATALOG/ECOMMERCE |
| **FILTERS** | Faceted/refinement controls on PLP/list surfaces | **Mandatory** — Tier A for CATALOG/ECOMMERCE |
| **SORT_CONTROLS** | Sort order (price, date, relevance) | **FILTERS sub-variant** — **no** separate `block_id` |
| **FACET_CHIPS** | Active filter summary | **FILTERS sub-variant** — **no** separate `block_id` |
| **RESULTS_META** | "Showing X of Y" / empty state | **FILTERS or PRODUCT_GRID notes** — **no** separate `block_id` |

### Category S3 — Orientation and list navigation

| Vocabulary term | Purpose | v1.1 disposition |
|-----------------|---------|----------------|
| **BREADCRUMBS** | Hierarchical orientation + internal linking | **Optional** — **layout-component policy** for v1.1; block_id path reserved for future matrix-automation waiver only |
| **PAGINATION** | Paged navigation for long lists | **Optional** — **layout-component policy** for v1.1; same policy fork as breadcrumbs |

### Category S4 — Post-task and vertical-specific (deferred)

| Vocabulary term | Purpose | v1.1 disposition |
|-----------------|---------|----------------|
| **THANK_YOU_SURFACE** | Post-conversion confirmation | **Deferred** — `CONFIRMATION_PAGE` page_type policy; dedicated `block_id` post-R01.2 |
| **ORDER_STATUS / ACCOUNT_NAV** | Post-purchase/account IA | **Deferred** — post-R01 / Extended types |
| **DEALER_LOCATOR** | Geo/dealer discovery | **Deferred** — vertical profile (WF-R01.8); compose via `MAP` + `LEAD_FORM` today |
| **SPEC_TABLE** | B2B spec comparison | **Deferred** — manufacturer vertical; compose via `FEATURES` / `PRODUCT_CARD` |
| **COMPARE_BAR** | Sticky compare tray | **Deferred** — post-R01 catalog enhancement |
| **SUB_NAV / TABS** | Section-level IA within hub | **Deferred** — page-type or future policy |

### Tier summary (binding disposition)

| Tier | Items | Charter action | Registry action |
|------|-------|----------------|-----------------|
| **Tier A — Mandatory vocabulary** | HEADER_NAV, FILTERS, SEARCH | **ACCEPTED** as minimal structural canon for v1.1 | **Future** — execution task adds BLOCK-CONTRACT rows only after Gate 2 readiness |
| **Tier B — Policy resolution** | BREADCRUMBS, PAGINATION, MEGA_MENU variant, THANK_YOU policy | **ACCEPTED** — layout-component default; mega-menu = variant; thank-you = page_type | **No** new ids in v1.1 for Tier B unless future waiver charter |
| **Tier C — Explicitly excluded from v1.1** | SORT as separate id, DEALER_LOCATOR, SPEC_TABLE, COMPARE_BAR, ACCOUNT_NAV, standalone UTILITY_NAV | **Deferred** to WF-R01.8 / post-R01 | **Forbidden** in v1.1 scope |

### Duplicate-risk resolutions (binding)

| Risk | Resolution |
|------|------------|
| MEGA_MENU as separate `block_id` | **Forbidden** in v1.1 — HEADER_NAV variant only |
| FILTERS vs SORT fragmentation | Single PLP control owner — FILTERS with sort in notes |
| MOBILE_NAV_DRAWER as second nav id | HEADER_NAV implementation variant |
| CART icon vs `CART` block | Mini-cart → HEADER_NAV utility composition; `CART` = cart page/flow |
| HEADER_NAV absorbs HERO | **Forbidden** — cite layout-shell-governance in future BLOCK-CONTRACT notes |

---

## Vocabulary Alignment

### F3 Block subtype compliance (S1)

| Check | Verdict |
|-------|---------|
| Structural Block remains **Block Family → Structural Subtype** | **PASS** — not separate family F7 |
| Six vocabulary families unchanged | **PASS** — charter amends neither Vocabulary Canon nor family count |
| REG-VOC-04 structural-before-marketing | **PASS** — catalog ordering adopted in § Structural Layer Definition |
| REG-VOC-09 context_dependent matrix requirement | **ACKNOWLEDGED** — matrix update required **at Gate 2**, not this charter |
| hero vs header_nav glossary disambiguation | **PASS** — § Design rules rule 5 |
| Commercial/Trust pattern boundary | **PASS** — patterns do not register as structural entities |

### WF-R01.1 harmonization

| Item | Alignment |
|------|-----------|
| Role `nav_mega_or_primary` → HEADER_NAV | **Aligned** — PENDING until Gate 2 registry row |
| v1 = SSOT for new `block_id` | **Aligned** — no v0 structural pseudo-ids |
| STOP mixed v0/v1 IDs | **Required** before registry row execution (B3) |

### AUTH rule compliance

| Rule | Compliance |
|------|------------|
| AUTH-01 Research never auto-promotes | **PASS** — charter cites RV-01; no auto rows |
| AUTH-02 Canon/charter has no normative registry rows | **PASS** — vocabulary terms only |
| AUTH-04 Blueprint cannot mint IDs | **PASS** — stated in boundaries |
| AUTH-06 WF-A01/A02 unchanged | **PASS** — orthogonal citations only |

---

## Research Alignment

Research artifacts: [rv-01-production-vocabulary.md](../../research/foundry/rv-01-production-vocabulary.md) · [rv-02-website-production-systems.md](../../research/foundry/rv-02-website-production-systems.md) · [rv-03-pixel-factory.md](../../research/foundry/rv-03-pixel-factory.md)

### RV-01 — Production Vocabulary

| Finding | In charter (Tier A) | Reference only |
|---------|---------------------|----------------|
| Missing structural primitives (header/nav, search, filters, breadcrumbs, pagination) | **§ Structural Categories** — Tier A/B disposition | Full industry frequency tables |
| Structural-before-marketing priority | **§ Design rules**, catalog ordering | — |
| minimal_canon first | **Tier A = 3 terms** | Full minimal canon site/page lists |
| standard/common/specialized/obsolete attribute | **Acknowledged** for future BLOCK-CONTRACT rows | Per-term industry STATUS cells |
| Block Vocabulary gap counts (14 Partial / 13 Missing) | **Informs priority** — not replicated | Provisional RV-01 STATUS table |
| Vertical exotica deferral | **Tier C** | Marketplace, calculators, vehicle listings detail |
| page_reality ≠ serp_reality | **Orthogonal** — WF-R01.5; breadcrumbs valid without SERP promise | FAQ rich result deprecation detail |
| Full vertical site type list | — | **Tier C — Reference Only** |

### RV-02 — Website Production Systems

| Finding | In charter | Reference only |
|---------|------------|----------------|
| structural_block vs content_block boundary | **§ Structural Layer Definition** | — |
| 5-layer production stack | — | **Tier B — Reference Library** |
| canonical_asset vs editorial_instance | — | **Tier B — Glossary** |
| Structured content models | — | **Tier C** |
| Component (code) layer | **§ What Structural Blocks are not** | Full stack diagrams |

### RV-03 — Pixel Factory

| Finding | In charter | Reference only |
|---------|------------|----------------|
| Structural vocabulary | **Not in scope** — WF-A03 DEFERRED | — |
| Failure class taxonomy | **Cross-reference only** — VL3/FP-0002 | Full orchestration loop |
| HITL checkpoint model | **Acknowledged** for future partial implementation | Pixel pipeline terms |
| Visual diff / screenshot engine | — | **WF-A03 only — forbidden** |

---

## Site Type Impact

v1 Core 5 + operational vertical compositions **MANUFACTURER** and **AUTO** (not separate `site_type_code` per program design). **MARKETPLACE** = Extended type — classification hints only.

Legend: **O** = Obligatory structural layer · **R** = Recommended · **—** = Not required / often forbidden · **P** = Policy-dependent

| Structural capability | LANDING | PROMO | CORPORATE | CATALOG | ECOMMERCE | MANUFACTURER* | AUTO* | MARKETPLACE** |
|----------------------|---------|-------|-----------|---------|-----------|---------------|-------|---------------|
| HEADER_NAV | — / minimal | **O** | **O** | **O** | **O** | **O** | **O** | **O** (Extended) |
| SEARCH | — | R | R | **O** | **O** | **O** | **O** | **O** |
| FILTERS | — | — | P (catalog subtree) | **O** | **O** | **O** | **O** | **O** |
| BREADCRUMBS (layout policy) | — | R | **O** | **O** | **O** | **O** | **O** | **O** |
| PAGINATION (layout policy) | — | P | P | **O** | **O** | **O** | **O** | **O** |
| MEGA_MENU variant | — | P | R | R | R | **O** | R | R |

\* **MANUFACTURER** = `CATALOG` + `CORPORATE` composition + vertical notes — **no** dedicated v1 code.  
\** **MARKETPLACE** = Extended type — structural layer **concept only** until separate charter.

### Obligatory structural minimum by class

| Site-type class | Obligatory minimum | Without it |
|-----------------|-------------------|------------|
| **CATALOG / ECOMMERCE** | HEADER_NAV + FILTERS + SEARCH (+ breadcrumbs/pagination via layout policy) | PLP/PDP **cannot be honestly blueprinted** — live catalog delivery **≠** Factory canon |
| **PROMO / CORPORATE** | HEADER_NAV (+ breadcrumbs on deep IA via layout) | Multi-page Template-Art **blocked** — navigation exists only as layout ad hoc |
| **LANDING** | None required (minimal header optional) | Reference workspace **fits** — structural program **must not** force catalog chrome on LANDING |
| **MANUFACTURER / AUTO** | Same as CATALOG + often MEGA_MENU variant | Factory vocabulary **missing** today — OCPilot paths **ahead** of registry |

### Extended types (SAAS, WEB_APPLICATION, MARKETPLACE)

Core v1.1 structural vocabulary **may apply** as **classification hints only** — Extended types explicitly **out of Core Library v1** ([SITE-TYPE-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md)). WF-R01.2 **does not** expand Extended type matrices.

---

## Template-Art Impact

Per [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md): **`TEMPLATE_ART`** — Site Type + Block Registry = SSOT; visual from Factory foundations.

### Current effective scope

**LANDING-only** — 9 partials, **zero** structural `block_id` rows, design tokens DG-01–04 OPEN ([foundry-capability-gap-audit-v1.md](../../reports/foundry-capability-gap-audit-v1.md) §07).

### Structural capabilities required beyond LANDING

| Target `site_type_code` | Structural prerequisites (vocabulary) | WF-R01 subprogram |
|-------------------------|--------------------------------------|-------------------|
| **PROMO** | HEADER_NAV (+ optional SEARCH) | R01.2 Tier A; R01.3 W2–W3 partials |
| **CATALOG** | HEADER_NAV, FILTERS, SEARCH + breadcrumbs/pagination layout policy | R01.2 + R01.3 W4–W5 |
| **ECOMMERCE** | Above + utility nav (cart/account) in HEADER_NAV composition | R01.2 + R01.3 W4–W6 |
| **CORPORATE** | HEADER_NAV + optional catalog subtree filters/search | R01.2 + R01.3 W7 |

### Template-Art readiness coupling

| Gate | Template-Art effect |
|------|---------------------|
| **Before R01.2 ACCEPTED** | **LANDING-only** interim policy mandatory |
| **After R01.2 ACCEPTED** (this charter) | Vocabulary **honest** for structural layer; **still LANDING-only** for production until Gate 2 + R01.3 |
| **After Gate 2 (registry rows) + M3 = 3/3** | CATALOG/PROMO **pilot vocabulary** unlocked (partials may lag) |
| **After R01.3 Gate 2 (M2 ≥ 63%)** | PROMO/CATALOG Template-Art **pilot-ready** |
| **After R01.7 ACCEPTED** | Multi-type Template-Art policy matrix binding |

**WF-R01.2 ACCEPTED alone does not unlock** Template-Art multi-type production — reference coverage (R01.3) and R01.7 matrix **ACCEPTED** are **co-required**.

---

## Registry Readiness Rules

Gate 2 registry row promotion requires **all** conditions below. This charter satisfies **Gate 1 only**.

### Preconditions (hard)

| ID | Condition | Status at T0 |
|----|-----------|--------------|
| **R1** | WF-R01.2 charter **ACCEPTED** | ✅ **Satisfied** (this artifact) |
| **R2** | WF-R01.1 binding charter **ACCEPTED** (B1) | ✅ Satisfied |
| **R3** | WF-R01.1 **B3** STOP rule live in OPERATIONAL-INDEX | ⏳ **Pending** — recommended before row edits |
| **R4** | Separate **execution task** authorized (human charter pass or operator sign-off) | ⏳ **Not started** |
| **R5** | No mixed v0/v1 `block_id` in target blueprint/matrix artifacts | ⏳ Verify at execution |

### Execution deliverables (Gate 2 — not this pass)

| Deliverable | Owner | Notes |
|-------------|-------|-------|
| Tier A BLOCK-CONTRACT rows (`HEADER_NAV`, `FILTERS`, `SEARCH`) | WF-R01.2 execution | Additive to BLOCK-REGISTRY-v1.1 |
| SITE-TYPE-BLOCK-MATRIX update (v3 or v2.1 additive) | WF-R01.2 execution | Structural columns per § Site Type Impact |
| PAGE-BLOCK-MAPPING + BLUEPRINT-BLOCK-MAPPING updates | WF-R01.2 execution | Close BLOCK-REGISTRY-GAPS §2–3 |
| BLOCK-DEPENDENCY-RULES | WF-R01.2 execution | e.g. `PRODUCT_GRID` **recommends** `FILTERS` |
| BLOCK-REGISTRY-GAPS OPEN → CLOSED for Tier A | WF-R01.2 execution | Audit report evidence |
| Maturity + `context_dependent` attributes on new rows | WF-R01.6 hygiene | Per REG-VOC-08/09 |

### Success metric (program design)

**M3** baseline → charter path to **3/3** structural ids **defined in registry** (not merely in vocabulary charter). Denominator for M2 becomes **32** (29 + 3) after Gate 2.

### Explicitly not Gate 2

- Reference partial HTML/SCSS (WF-R01.3)
- npm build / curated library v2
- Blueprint Layer file automation
- VL3 validator implementation

### Gate sequencing

```text
Gate 0  Design ACCEPTED (program design report)
   ↓
Gate 1  R01.2 Charter ACCEPTED (this artifact)  ← current
   ↓
Gate 2  Registry v1.1 rows + matrices (execution task)
   ↓
[WF-R01.3]  Reference partials W2/W4
   ↓
[WF-R01.7]  Template-Art multi-type pilot readiness
```

---

## Non-Goals

This charter v1 does **not** authorize:

| # | Exclusion | Routed to |
|---|-----------|-----------|
| NG-01 | Registry row creation or `block_id` assignment | Gate 2 execution task |
| NG-02 | Reference partial HTML/SCSS expansion | WF-R01.3 |
| NG-03 | New `site_type_code` or `page_type` rows | WF-R01.6 / WF-R01.7 |
| NG-04 | Blueprint Layer file edits | Execution after Gate 2 |
| NG-05 | Commercial Pattern Library expansion | WF-R01.4 |
| NG-06 | SEO Content Pattern Slice | WF-R01.5 |
| NG-07 | Full BLOCK-CONTRACT hygiene on legacy 29 entries | WF-R01.6 |
| NG-08 | Template-Art Multi-Site-Type Charter ACCEPTED | WF-R01.7 |
| NG-09 | Pixel Factory / WF-A03 | **DEFERRED** |
| NG-10 | Agent Runtime / orchestration | Not claimed |
| NG-11 | Machine validation / CI / JSON Schema export | Post-R01 tooling |
| NG-12 | Triumph v6 / BZPM retrofits | Explicit enrollment only |
| NG-13 | New site types (Manufacturer, Auto as codes) | Vertical profiles WF-R01.8 |
| NG-14 | ECOMMERCE Legal Extension E1–E4 | Future ecommerce go-live charter |
| NG-15 | Amendment to WF-A01 / WF-A02 / Vocabulary Canon | Harmonization via glossary only |

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| **Scope creep** — v1.1 becomes full catalog vertical library | **Critical** | Tier A = 3 terms only; Tier C explicit deferral |
| **False "structural complete" after charter ACCEPTED** | **Critical** | M3 measures **registry rows**, not this charter |
| **TEMPLATE_ART on CATALOG** before Gate 2 | **Critical** | R01.7 LANDING-only interim; passport HITL |
| **MEGA_MENU as separate `block_id`** | **High** | Variant rule binding in § Duplicate-risk |
| **FILTERS vs SORT fragmentation** | **High** | Single PLP control owner |
| **HEADER_NAV absorbs HERO** | **High** | layout-shell-governance; BLOCK-CONTRACT notes at execution |
| **v0 layout partials mixed into v1 blueprints** during execution | **Critical** | WF-R01.1 STOP rule (B3) before row edits |
| **BZPM OpenCart treated as Factory reference** | **High** | Vocabulary mining only; R01.8 enrollment |
| **Premature WF-A03** before structural Gate 2 | **Medium** | Roadmap DEFERRED + R01 Gate 2+ precondition |
| **BREADCRUMBS layout policy blocks matrix automation** | **Medium** | Future waiver charter if automation required |

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| **Named steward** for WF-R01.2 | **Not fixed** in repo |
| **WF-R01.1 B3–B8** implementation (STOP rule, banners, T_cutover) | **Pending** — B1 satisfied |
| **T_cutover** calendar date | **Pending** P4 |
| **OCPilot SITE-001** v1 binding / production_mode | **Not verified** |
| **BZPM W3** blueprint delivery date | **UNKNOWN** |
| **Faceted SEO** policy for FILTERS URL behavior | **FUTURE** — seo-architecture addendum (WF-R01.5) |
| **JSON Schema** for new structural `block_id` | **NOT DEFINED** |
| **Automated matrix validation** | **NOT IMPLEMENTED** |
| **VL3 adoption** on Triumph v6 / ISBD | **Not audited** |
| **BREADCRUMBS/PAGINATION** future block_id waiver need | **Monitor** — layout policy default until matrix automation charter |
| **MARKETPLACE** dedicated structural matrix | **Requires** Extended type charter |

---

## Related documents

| Document | Role |
|----------|------|
| [wf-r01-registry-expansion-program-charter-v1.md](../../reports/wf-r01-registry-expansion-program-charter-v1.md) | Parent program — CHARTERED |
| [wf-r01-2-structural-blocks-program-design-v1.md](../../reports/wf-r01-2-structural-blocks-program-design-v1.md) | Design basis — Gate 0 |
| [foundry-vocabulary-canon-charter-v1.md](foundry-vocabulary-canon-charter-v1.md) | Upstream vocabulary — ACCEPTED |
| [wf-r01-1-v0-v1-binding-charter-v1.md](../../reports/wf-r01-1-v0-v1-binding-charter-v1.md) | v0→v1 binding — ACCEPTED |
| [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md) | WF-A01 — Template-Art SSOT |
| [website-factory-validation-architecture-charter-v1.md](website-factory-validation-architecture-charter-v1.md) | WF-A02 — VL1 consumes registry |
| [website-factory-vl3-domains-charter-v1.md](website-factory-vl3-domains-charter-v1.md) | VL3 — orthogonal |
| [roadmap.md](roadmap.md) | Factory architecture items |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Operator entry |

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Status | **ACCEPTED** |
| T0 | 2026-06-19 |
| Registry rows created | **0** |
| New IDs created | **0** |
| Subprogram | WF-R01.2 |

*Accepted charter artifact: `projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md`*
