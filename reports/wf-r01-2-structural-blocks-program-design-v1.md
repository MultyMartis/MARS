# REPORT — WF-R01.2 STRUCTURAL BLOCKS PROGRAM DESIGN

**Subprogram ID:** WF-R01.2 — Registry v1.1 Structural Blocks  
**Date:** 2026-06-19  
**Mode:** program design only — **no implementation**  
**Authority chain:** [wf-r01-registry-expansion-program-charter-v1.md](wf-r01-registry-expansion-program-charter-v1.md) · [foundry-registry-expansion-program-design-v1.md](foundry-registry-expansion-program-design-v1.md) · [wf-r01-1-v0-v1-binding-charter-v1.md](wf-r01-1-v0-v1-binding-charter-v1.md) (**ACCEPTED** T0 = 2026-06-19)

**Honesty boundary:** WF-R01.2 — **documentation and charter design** for a future registry v1.1 slice. **Not** runtime, **not** orchestration, **not** reference partial expansion (→ WF-R01.3), **not** new `block_id` rows in this artifact, **not** Blueprint Layer edits.

**Terminology:** **FOUNDRY** = **Website Factory** ecosystem (строка FOUNDRY как отдельный продукт/путь в repo **не найдена**).

---

## Executive Summary

WF-R01.1 (**ACCEPTED**) закрепил v1 как SSOT для новых `site_type_code` / `block_id`, но **Registry Implementation Cliff** остаётся главным bottleneck: **29** канонических `block_id`, **~9** reference partials (~**31%**), и **OPEN** structural gaps, которые три аудита неоднократно фиксировали как **HEADER_NAV**, **FILTERS**, **SEARCH**.

**Structural Blocks** — это слой **wayfinding, discovery и global shell**, отделённый от content/commercial/trust/SEO surfaces. Без канонических structural entities Blueprint Layer и PAGE-ARCHITECTURE **требуют** поверхности, которых Block Registry v1 **не содержит** ([BLOCK-REGISTRY-GAPS-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-GAPS-v1.md) §2–3; [BLOCK-GAPS-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md) §2).

**Рекомендация программы:** WF-R01.2 charter должен добавить **минимум +3** structural `block_id` (`HEADER_NAV`, `FILTERS`, `SEARCH`) + **policy-only** решения для breadcrumbs, pagination, thank-you и mega-menu variant — **без** vertical-specific ids (manufacturer/auto) в v1.1. Reference implementation и matrix updates — **WF-R01.3 / WF-R01.6**, не R01.2.

**Блокирующий контекст:** Template-Art **эффективно LANDING-only** до structural layer + reference Gate 2 ([foundry-capability-gap-audit-v1.md](foundry-capability-gap-audit-v1.md); WF-R01.7 interim policy — **pending**).

**Research:** RV-01 / RV-02 **не найдены** в repo — industry canon ниже построен на proxy audits + зафиксированных program-design findings; помечено **candidate**, не **approved**.

---

## Structural Vocabulary Definition

### Что такое Structural Blocks

**Structural Blocks** — reusable registry entities, описывающие **persistent shell** и **catalog discovery mechanics**: global navigation, search, filters, breadcrumbs, pagination, и иные **task-support** surfaces, которые:

1. **Пересекают** множество страниц или route groups (global или subtree-scoped).
2. **Не несут** primary commercial narrative (hero, benefits, pricing story).
3. **Не являются** trust proof или SEO editorial body.
4. **Обеспечивают** orientation, browse/compare/task completion в IA.

**Каноническая опора в repo:**

| Source | Structural signal |
|--------|-------------------|
| [layout-shell-governance.md](../projects/mars-website-factory/layout-shell-governance.md) | **HEADER ≠ HERO** — header/nav = shell layer, не content block |
| [BLOCK-CATEGORY-SYSTEM-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLOCK-CATEGORY-SYSTEM-v1.md) | Category `NAVIGATION` — **reserved**; `HEADER_NAV` **not in Core Library v1** |
| [BLOCK-REGISTRY-GAPS-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-GAPS-v1.md) | Blueprint requires header/nav, filters/search — **OPEN** without `block_id` |
| [wf-r01-1-v0-v1-binding-charter-v1.md](wf-r01-1-v0-v1-binding-charter-v1.md) | Role `nav_mega_or_primary` → `HEADER_NAV` (**PENDING** — WF-R01.2) |

**Conversion role (design default):** predominantly **SYSTEM** or **INFORMATIONAL** — structural blocks **support** conversion paths; они **не** primary conversion surfaces (исключение: search-as-entry on large catalogs).

### Отделение от других слоёв

| Layer | Definition | Examples in v1 canon | Relation to Structural |
|-------|------------|----------------------|------------------------|
| **Content Blocks** | Page sections carrying narrative, explanation, or offer story | `HERO`, `BENEFITS`, `FEATURES`, `PROCESS`, `FAQ`, `PRICING`, `SERVICES`, `ABOUT`, `TEAM` | Structural blocks **frame** content; **do not replace** hero/value sections |
| **Commercial Patterns** | Reusable **pattern_id** semantics (copy structure, ethical constraints, interaction model) — **separate catalog** | `scroll_process_timeline`, future `lead-form-v1`, `rfq-v1` ([foundry-registry-layer-audit-v1.md](foundry-registry-layer-audit-v1.md) § Commercial Pattern Library) | Patterns **compose inside** blocks (e.g. RFQ inside `LEAD_FORM`); **not** structural entities |
| **Trust Patterns** | Proof, credibility, social validation — **TRUST category** blocks | `TRUST`, `TESTIMONIALS`, `REVIEWS`, `CERTIFICATES`, `CASES` | Trust blocks are **content-band** proof; structural nav **must not** absorb trust copy |
| **SEO Surfaces** | Planning/contract layer for intent, indexation, meta — **seo-architecture/** v2 | SITE-TYPE-SEO-MAPPING-v2, PAGE-SEO-CONTRACT-v1, faceted SEO (**FUTURE**) | SEO governs **how** pages are indexed and titled; breadcrumbs/filters **intersect** SEO but structural charter **≠** SEO Pattern Library (→ WF-R01.5) |
| **Catalog product blocks** | Item/category presentation — **CATALOG category** | `CATEGORIES`, `CATEGORY_GRID`, `PRODUCT_GRID`, `PRODUCT_CARD` | **Adjacent but distinct:** product grids show **inventory**; FILTERS/SEARCH **operate on** grids — dependency, not duplication |
| **System shell (partial)** | Global chrome without full nav semantics | `FOOTER`, `LEGAL_LINKS`, layout `modal_callback` | **Overlap zone:** `FOOTER` exists in v1; **HEADER_NAV** missing — shell incomplete |

### Design rules (vocabulary boundary)

1. **One primary owner** per structural concern — e.g. PLP filtering **≠** `PRODUCT_GRID` markup; filters are **control surface**, grid is **result surface**.
2. **Structural blocks may be FORBIDDEN** on pure `LANDING` URLs (minimal nav) per site-type matrix — absence is **intentional**, not a gap.
3. **Layout components vs block_id:** breadcrumbs/pagination may remain **layout-component policy** if operator decision favors lighter registry — see Industry Canon § policy candidates.
4. **MEGA_MENU** — **variant** of `HEADER_NAV` (recommended) vs separate `block_id` — operator decision **deferred** to R01.2 charter pass, not this design.

---

## Industry Canon Candidates

**Evidence note:** RV-01 (Production Vocabulary Research) and RV-02 (Website Production Systems Research) **not found** in repo ([wf-r01-1-acceptance-pass-v1.md](wf-r01-1-acceptance-pass-v1.md) § Research Integration). Industry canon below = **candidate list** from world practice + audit proxy — **not approved** registry rows.

Frequency scale: **Universal** (>90% multi-page/catalog sites) · **Common** (50–90%) · **Contextual** (vertical or site-type specific) · **Emerging** (SaaS/app patterns; post-Core v1)

| Candidate | Purpose | Frequency | Site-type relevance |
|-----------|---------|-----------|----------------------|
| **HEADER_NAV** | Primary global navigation: brand, menu, utilities, mobile drawer | **Universal** | **Required:** PROMO, CATALOG, ECOMMERCE, CORPORATE · **Optional/minimal:** LANDING · **Extended:** MARKETPLACE (future) |
| **SEARCH** | Query entry, suggestions, results routing | **Common** | **Required:** CATALOG, ECOMMERCE · **Optional:** CORPORATE (large IA), PROMO · **Forbidden/default off:** LANDING |
| **FILTERS** | Faceted/refinement controls on PLP/list surfaces | **Common** | **Required:** CATALOG, ECOMMERCE · **Optional:** CORPORATE catalog subtree · **Forbidden:** LANDING, PROMO (default) |
| **BREADCRUMBS** | Hierarchical orientation + internal linking | **Common** | **Required:** CATALOG, ECOMMERCE, CORPORATE · **Optional:** PROMO · **Rare:** LANDING |
| **PAGINATION** | Paged navigation for long lists (PLP, reviews, news) | **Common** | **Required:** CATALOG, ECOMMERCE PLP · **Optional:** PROMO blog/news · **Contextual:** REVIEWS lists |
| **SORT_CONTROLS** | Sort order (price, date, relevance) | **Common** | CATALOG, ECOMMERCE — often **bundled with FILTERS** (variant vs split — see Duplicate Risk) |
| **MEGA_MENU** | Deep taxonomy flyout in header | **Contextual** | CATALOG, ECOMMERCE, CORPORATE, manufacturer — **variant of HEADER_NAV** (BZPM evidence) |
| **MOBILE_NAV_DRAWER** | Off-canvas menu | **Universal** (as behavior) | All multi-page types — **implementation variant** of HEADER_NAV, not separate id (recommended) |
| **UTILITY_NAV** | Account, cart icon, language, phone | **Common** | ECOMMERCE, CORPORATE — **composition inside HEADER_NAV** (recommended) |
| **SUB_NAV / TABS** | Section-level IA within hub | **Contextual** | CORPORATE, PROMO service hubs — **future** or page-type policy |
| **FACET_CHIPS** | Active filter summary | **Contextual** | CATALOG, ECOMMERCE — **FILTERS variant** |
| **RESULTS_META** | "Showing X of Y" / empty state | **Contextual** | CATALOG, ECOMMERCE — **FILTERS or PRODUCT_GRID notes** |
| **SKIP_LINK / A11Y_CHROME** | Accessibility jump links | **Universal** (best practice) | All — **layout/shell policy**, not block_id (recommended) |
| **THANK_YOU_SURFACE** | Post-conversion confirmation | **Common** | LANDING, ECOMMERCE — **page_type + block policy** vs dedicated id |
| **ORDER_STATUS / ACCOUNT_NAV** | Post-purchase/account IA | **Contextual** | ECOMMERCE, SAAS — **post-R01** / Extended types |
| **DEALER_LOCATOR** | Geo/dealer discovery | **Contextual** | Manufacturer, Auto — **vertical profile**, not Core v1.1 |
| **SPEC_TABLE** | B2B spec comparison | **Contextual** | Manufacturer — **compose** via `FEATURES` / `PRODUCT_CARD` + future vertical charter |
| **COMPARE_BAR** | Sticky compare tray | **Emerging** | CATALOG, ECOMMERCE — **post-R01** candidate |
| **STOCK_INDICATOR** | Inventory signal on cards | **Contextual** | ECOMMERCE — **PRODUCT_CARD notes**, not structural |

**Proxy research alignment (without RV files):**

- [foundry-capability-gap-audit-v1.md](foundry-capability-gap-audit-v1.md) Rank **#3** gap: HEADER_NAV, FILTERS, SEARCH, breadcrumbs, pagination
- [foundry-registry-expansion-program-design-v1.md](foundry-registry-expansion-program-design-v1.md) § Structural Blocks — **+3 minimum** + policy
- [website-factory-production-modes-charter-v1.md](../projects/mars-website-factory/website-factory-production-modes-charter-v1.md) — Template-Art SSOT = registries; structural absence **blocks** honest multi-type Template-Art

---

## Registry Impact

Per-candidate disposition against Block Registry v1 (29 ids) + documented gaps. Status vocabulary: **Already Exists** · **Missing** · **Duplicate Risk** · **Future**

| Candidate | Registry status | Notes |
|-----------|-----------------|-------|
| **HEADER_NAV** | **Missing** | OPEN in BLOCK-REGISTRY-GAPS §2; NAVIGATION category reserved empty; blueprints require global nav |
| **SEARCH** | **Missing** | OPEN; CATALOG/ECOMMERCE SITE-TYPE-REGISTRY **Included features** assume search |
| **FILTERS** | **Missing** | OPEN; PRODUCT_GRID notes "recommends filters (GAP)" |
| **BREADCRUMBS** | **Missing** (policy pending) | BLOCK-GAPS §2 — required in blueprints; **block_id vs layout-component** undecided |
| **PAGINATION** | **Missing** (policy pending) | PLP requirement documented; same policy fork as breadcrumbs |
| **MEGA_MENU** | **Future** (variant decision) | **Duplicate Risk** if separate id from HEADER_NAV — BZPM megamenu → prefer HEADER_NAV variant |
| **SORT_CONTROLS** | **Duplicate Risk** | Likely **FILTERS sub-variant** — separate id would fragment PLP control model |
| **MOBILE_NAV_DRAWER** | **Duplicate Risk** | Must not become second nav block_id — HEADER_NAV variant |
| **UTILITY_NAV** | **Duplicate Risk** | Cart/account/phone → HEADER_NAV composition or ECOMMERCE layout notes |
| **FOOTER** | **Already Exists** | `FOOTER` in v1; reference partial **implicit** only — implementation gap (R01.3) |
| **LEGAL_LINKS** | **Already Exists** | v1 block; footer-adjacent |
| **CTA / sticky** | **Already Exists** | `CTA` covers band + sticky; **not structural** — conversion/navigation hybrid; sticky is **not** HEADER |
| **CATEGORIES** | **Already Exists** | Taxonomy navigation — **adjacent** to HEADER_NAV (tree vs global menu) |
| **PRODUCT_GRID** | **Already Exists** | Result surface — **depends on** FILTERS/SEARCH when present |
| **CART** (icon/chrome) | **Duplicate Risk** | `CART` block = cart **page/flow**; mini-cart icon → HEADER_NAV utility composition |
| **THANK_YOU** | **Future** | Policy: page_type-only vs `THANK_YOU` block_id — post-lead/checkout |
| **DEALER_LOCATOR** | **Future** | Map + `LEAD_FORM` composition today; vertical charter post-R01 |
| **SPEC_TABLE** | **Future** | Manufacturer vertical — not v1.1 minimum |
| **COMPARE_BAR** | **Future** | Post-R01 catalog enhancement |

### Registry v1.1 scope recommendation (design)

| Tier | Items | R01.2 action |
|------|-------|--------------|
| **Tier A — Required new block_id** | `HEADER_NAV`, `FILTERS`, `SEARCH` | Charter + BLOCK-CONTRACT rows (**execution** in separate task after charter ACCEPTED) |
| **Tier B — Policy only** | BREADCRUMBS, PAGINATION, THANK_YOU, MEGA_MENU variant | Published policy doc; **no** new id unless policy selects block_id path |
| **Tier C — Explicitly excluded from v1.1** | SORT as separate id, DEALER_LOCATOR, SPEC_TABLE, COMPARE_BAR, ACCOUNT_NAV | WF-R01.8 vertical profiles / post-R01 charters |

### Matrix / blueprint impact (design — **no edits in this task**)

When Tier A is **ACCEPTED** (future charter):

- SITE-TYPE-BLOCK-MATRIX → **v3** (or v2.1 additive)
- PAGE-BLOCK-MAPPING — CATEGORY_PAGE, PRODUCT_PAGE, HOME_PAGE rows
- BLUEPRINT-BLOCK-MAPPING — CATALOG, ECOMMERCE, CORPORATE, PROMO
- BLOCK-DEPENDENCY-RULES — e.g. `PRODUCT_GRID` **recommends** `FILTERS`; `FILTERS` **requires** PLP context

---

## Site Type Impact

v1 Core 5 + operational verticals **MANUFACTURER** and **AUTO** (composition, not separate `site_type_code` per [foundry-registry-expansion-program-design-v1.md](foundry-registry-expansion-program-design-v1.md) § Registry Expansion).

Legend: **O** = Obligatory structural layer · **R** = Recommended · **—** = Not required / often forbidden · **P** = Policy-dependent

| Structural entity | LANDING | PROMO | CORPORATE | CATALOG | ECOMMERCE | MANUFACTURER* | AUTO* | MARKETPLACE** |
|-------------------|---------|-------|-----------|---------|-----------|---------------|-------|---------------|
| HEADER_NAV | — / minimal | **O** | **O** | **O** | **O** | **O** | **O** | **O** (Extended) |
| SEARCH | — | R | R | **O** | **O** | **O** | **O** | **O** |
| FILTERS | — | — | P (catalog subtree) | **O** | **O** | **O** | **O** | **O** |
| BREADCRUMBS | — | R | **O** | **O** | **O** | **O** | **O** | **O** |
| PAGINATION | — | P | P | **O** | **O** | **O** | **O** | **O** |
| MEGA_MENU variant | — | P | R | R | R | **O** | R | R |

\* **MANUFACTURER** = `CATALOG` + `CORPORATE` composition + vertical notes (BZPM proxy) — **no** dedicated v1 code.  
\** **MARKETPLACE** = Extended type — structural layer **concept only** until separate charter.

### Where structural layer is obligatory

| Site-type class | Obligatory structural minimum | Without it |
|-----------------|------------------------------|------------|
| **CATALOG / ECOMMERCE** | HEADER_NAV + FILTERS + SEARCH (+ breadcrumbs/pagination policy) | PLP/PDP **cannot be honestly blueprinted** — BZPM/Sibcar live delivery **≠** Factory canon |
| **PROMO / CORPORATE** | HEADER_NAV (+ breadcrumbs on deep IA) | Multi-page Template-Art **blocked** — navigation exists only as layout ad hoc |
| **LANDING** | None required (minimal header optional) | Current reference workspace **fits** — structural program **must not** force catalog chrome on LANDING |
| **MANUFACTURER / AUTO** | Same as CATALOG + often MEGA_MENU / dealer patterns | Factory vocabulary **missing** today — OCPilot paths **ahead** of registry |

### Extended types (SAAS, WEB_APPLICATION, MARKETPLACE)

Structural blocks from Core v1.1 **may apply** as **classification hints only** — Extended types explicitly **out of Core Library v1** ([SITE-TYPE-REGISTRY-v1.md](../workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md)). WF-R01.2 **does not** expand Extended type matrices.

---

## Template-Art Impact

Per [website-factory-production-modes-charter-v1.md](../projects/mars-website-factory/website-factory-production-modes-charter-v1.md): **`TEMPLATE_ART`** — Site Type + Block Registry = SSOT; visual from Factory foundations.

### Current effective scope

**LANDING-only** — 9 partials, **zero** structural block_ids, design tokens DG-01–04 OPEN ([foundry-capability-gap-audit-v1.md](foundry-capability-gap-audit-v1.md) §07).

### Structural blocks required for Template-Art beyond LANDING

| Target site_type | Structural prerequisites | WF-R01 subprogram |
|------------------|-------------------------|-------------------|
| **PROMO** | `HEADER_NAV` (+ optional SEARCH) | R01.2 Tier A; R01.3 W2–W3 partials |
| **CATALOG** | `HEADER_NAV`, `FILTERS`, `SEARCH` + breadcrumbs/pagination policy | R01.2 + R01.3 W4–W5 |
| **ECOMMERCE** | Above + utility nav (cart/account) composition | R01.2 + R01.3 W4–W6 |
| **CORPORATE** | `HEADER_NAV` + optional catalog subtree filters/search | R01.2 + R01.3 W7 |

### Template-Art readiness coupling (from program design)

| Gate | Template-Art effect |
|------|---------------------|
| **Before R01.2 ACCEPTED** | **LANDING-only** interim policy mandatory |
| **After R01.2 + M3 = 3/3** | CATALOG/PROMO **pilot** allowed (HITL) — vocabulary honest, partials may lag |
| **After R01.3 Gate 2 (M2 ≥ 63%)** | PROMO/CATALOG Template-Art **pilot-ready** |
| **After Gate 4** | ECOMMERCE/CORPORATE **pilot** (excluding ECOMMERCE legal E1–E4) |

**WF-R01.2 alone does not unlock** Template-Art multi-type production — reference coverage (R01.3) and R01.7 matrix **ACCEPTED** are **co-required**.

---

## Execution Case Impact

| Case | Structural entities that would help | Primary signal |
|------|-------------------------------------|----------------|
| **Triumph** (`triumph-manipulator-landing-v6/`) | Minimal `HEADER_NAV` (PPC landings); **not** FILTERS/SEARCH | LANDING/service landing — **validates Tier A optional path** for minimal nav; multi-page Triumph **would need** HEADER_NAV for PROMO-class honesty |
| **ISBD** (`isbd-care-landing/`) | Minimal header; no catalog chrome | Confirms LANDING structural **absence** is OK; FEATURES/REVIEWS are **content**, not structural |
| **BZPM** (OCPilot TEST; no Factory workspace) | **HEADER_NAV** (megamenu), **FILTERS**, **SEARCH**, breadcrumbs, pagination, PLP/PDP IA | **Strongest driver** for Tier A — live catalog **proves** structural surfaces; vocabulary **trapped outside** canon ([execution-cases-registry-v1.md](../projects/mars-website-factory/execution-cases-registry-v1.md)) |
| **FP-0002** (`fp-0002-shpigovsky-frontend/`) | **Not** primary block source — PIXEL_PERFECT / VL3 forensic | Informs **validation discipline** and Template-Art vs PIXEL boundary (R01.7); **negative evidence** for false-green — **does not** define structural catalog |
| **OCPilot SITE-001 (Sibcar / AUTO)** | Same as CATALOG: filters, search, PDP chrome, header nav | **Not verified** v1 binding — auto vertical **maps to** CATALOG structural set |

### Case → R01.2 design implications

1. **BZPM** — canonical **requirements trace** for Tier A; extraction **documentation-only** until R01.3 enrollment.
2. **Triumph** — do **not** over-fit structural scope from v6; selective HEADER_NAV notes for PROMO rollout only.
3. **FP-0002** — **exclude** from structural candidate sourcing; parallel VL3 track unchanged.

---

## Readiness Model

Gates for **structural layer introduction** — documentation and charter milestones; **not** implementation gates.

### Gate 0 — Vocabulary frozen (today → R01.2 design ACCEPTED)

| Criterion | Status |
|-----------|--------|
| WF-R01 **CHARTERED** | ✅ |
| WF-R01.1 binding **ACCEPTED** (B1) | ✅ |
| Structural vocabulary defined (this report) | ✅ (this artifact) |
| OPEN gaps documented | ✅ BLOCK-REGISTRY-GAPS, BLOCK-GAPS |
| Tier A/B/C scope split agreed | ⏳ pending human sign-off on this design |

**Exit:** Human ACCEPTED on WF-R01.2 program design → authorize **charter pass** (separate task).

### Gate 1 — Structural charter ACCEPTED (R01.2 execution design)

| Criterion | Target |
|-----------|--------|
| WF-R01.2 subprogram charter **ACCEPTED** | Tier A block_id **defined** in charter (not yet in registry until execution task) |
| Policy doc draft for Tier B (breadcrumbs, pagination, thank-you, mega_menu) | Published |
| Duplicate-risk resolutions documented (SORT, CART icon, mobile drawer) | Signed |
| SITE-TYPE-BLOCK-MATRIX v3 **charter scope** approved | Design complete |
| WF-R01.1 B3 STOP rule live | **Recommended** before registry row edits — minimum per program design |

**Metric:** **M3** baseline → charter path to **3/3 structural ids defined** ([foundry-registry-expansion-program-design-v1.md](foundry-registry-expansion-program-design-v1.md) § Success Metrics).

**Explicitly not Gate 1:** reference partials, npm build, curated library v2.

### Gate 2 — Structural registry live + matrix aligned (R01.2 execution complete)

| Criterion | Target |
|-----------|--------|
| Tier A rows in BLOCK-REGISTRY-v1.1 (or additive doc) | **ACCEPTED** |
| SITE-TYPE-BLOCK-MATRIX updated | Structural columns populated |
| PAGE-BLOCK-MAPPING + BLUEPRINT-BLOCK-MAPPING updated | OPEN gaps §2–3 **closed** |
| BLOCK-REGISTRY-GAPS OPEN → **CLOSED** for HEADER_NAV, FILTERS, SEARCH | Audit report |
| Template-Art honesty | CATALOG/PROMO **pilot vocabulary** unlocked (partials still R01.3) |

**Metric:** M3 = **3/3**; denominator for M2 becomes **32** (29 + 3 structural).

**Dependency:** Gate 2 registry edits require WF-R01.1 **B3 minimum** ([wf-r01-charter-pass-design-v1.md](wf-r01-charter-pass-design-v1.md) § WF-R01.2 Authorization Conditions).

### Gate sequencing diagram

```
Gate 0  Design ACCEPTED (this report)
   ↓
Gate 1  R01.2 Charter ACCEPTED + Tier B policy
   ↓
Gate 2  Registry v1.1 rows + matrices (execution task)
   ↓
[WF-R01.3]  Reference partials W2/W4 (HEADER_NAV, FILTERS, SEARCH…)
   ↓
[WF-R01.7]  Template-Art multi-type pilot readiness
```

---

## Program Boundaries

### In scope for WF-R01.2 (when chartered & executed)

| Item | Boundary |
|------|----------|
| Structural **vocabulary** and Tier A/B/C classification | ✅ |
| Charter for **+3 minimum** block_id: HEADER_NAV, FILTERS, SEARCH | ✅ |
| Policy decisions: breadcrumbs, pagination, thank-you, mega_menu variant | ✅ |
| Matrix/blueprint **design** for structural alignment | ✅ |
| Duplicate-risk disposition (SORT, utility nav, mobile drawer) | ✅ |
| Execution case **requirements trace** (BZPM, Sibcar) | ✅ |

### Explicitly **NOT** in WF-R01.2

| Exclusion | Routed to |
|-----------|-----------|
| **Pixel Factory / WF-A03** — Vision, Visual Diff, Pixel QA Runtime, Screenshot Engine, Agent Runtime | WF-A03 (**DEFERRED**) |
| **Reference partial HTML/SCSS** expansion | WF-R01.3 |
| **Commercial Pattern Library** expansion (`pattern_id` catalog) | WF-R01.4 |
| **SEO Content Pattern Slice** / SEO Formula Layer | WF-R01.5 |
| **Full BLOCK-CONTRACT hygiene** on legacy 26 entries | WF-R01.6 |
| **Template-Art Multi-Site-Type Charter** (readiness matrix ACCEPTED) | WF-R01.7 |
| **Execution case lesson index** | WF-R01.8 |
| **New site types** (Manufacturer, Auto as codes) | Out of scope — vertical profiles only |
| **Extended type** structural libraries (SAAS, MARKETPLACE, WEB_APPLICATION) | Separate future charter |
| **ECOMMERCE Legal Extension E1–E4** | Future ecommerce go-live charter |
| **Machine validation / CI / JSON Schema export** | Post-R01 / tooling S5 |
| **Blueprint Layer file edits** in design-only pass | Execution after charter ACCEPTED |
| **Triumph v6 / BZPM retrofits** | Explicit enrollment only |
| **Runtime, orchestration, agent automation** | Not claimed — Phase 1 doc only |

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| **Scope creep** — v1.1 becomes full catalog vertical library | **Critical** | Tier A = 3 ids only; Tier C explicit deferral |
| **TEMPLATE_ART on CATALOG** before Gate 2 | **Critical** | R01.7 LANDING-only interim; passport HITL |
| **MEGA_MENU as separate block_id** | **High** | Recommend HEADER_NAV variant; document in Tier B policy |
| **FILTERS vs SORT fragmentation** | **High** | Single PLP control owner — FILTERS with sort in notes |
| **BREADCRUMBS id vs layout policy paralysis** | **Medium** | Timeboxed operator decision in charter pass |
| **False "structural complete" after design ACCEPTED** | **Critical** | M3 measures **registry rows**, not this report |
| **BZPM OpenCart treated as Factory reference** | **High** | Vocabulary mining only; R01.8 enrollment |
| **v0 layout partials mixed into v1 blueprints** during R01.2 execution | **Critical** | WF-R01.1 STOP rule (B3) before row edits |
| **HEADER_NAV absorbs HERO** (HEADER = HERO violation) | **High** | Cite layout-shell-governance in BLOCK-CONTRACT notes |
| **Premature WF-A03** before structural Gate 2 | **Medium** | Roadmap DEFERRED + recommended R01 Gate 2+ precondition |

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| **RV-01 / RV-02** research artifacts in repo | **Not found** — industry canon = proxy + candidate list only |
| **RV-03** (Pixel Factory research) | **Not found** |
| **BREADCRUMBS / PAGINATION** — block_id vs layout-component | **Operator decision pending** |
| **MEGA_MENU** — variant vs separate id | **Operator decision pending** |
| **THANK_YOU** — dedicated block_id vs page_type-only | **Policy pending** |
| **WF-R01.1 B3–B8** implementation (STOP rule, banners, T_cutover) | **Pending** — B1 satisfied, B3–B8 not complete |
| **Human owner** WF-R01.2 sign-off | **Not fixed** in repo |
| **OCPilot SITE-001** v1 binding / production_mode | **Not verified** |
| **BZPM W3 blueprint** delivery date | **UNKNOWN** |
| **VL3 adoption** on Triumph v6 / ISBD | **Not audited** |
| **Faceted SEO** policy for FILTERS URL behavior | **FUTURE** — seo-architecture addendum |
| **JSON Schema** for new structural block_id | **NOT DEFINED** |
| **Automated matrix validation** | **NOT IMPLEMENTED** |

---

## Recommended Structural Candidates

### Tier A — Recommend for v1.1 charter (minimum +3)

| Priority | Candidate `block_id` | Rationale |
|----------|---------------------|-----------|
| **A1** | `HEADER_NAV` | Universal shell gap; blueprints OPEN; role `nav_mega_or_primary` PENDING; layout-shell-governance |
| **A2** | `FILTERS` | CATALOG/ECOMMERCE PLP **critical**; BZPM live evidence; PRODUCT_GRID dependency |
| **A3** | `SEARCH` | CATALOG/ECOMMERCE SITE-TYPE included feature; pairs with FILTERS |

### Tier B — Recommend policy resolution (charter pass, may omit block_id)

| Priority | Candidate | Recommended disposition |
|----------|-----------|------------------------|
| **B1** | BREADCRUMBS | **Prefer** layout-component policy for v1.1 **unless** SEO/matrix automation requires block_id — if block_id: single `BREADCRUMBS` |
| **B2** | PAGINATION | **Prefer** `PAGINATION` block_id **if** PLP matrix validation needed; else layout policy |
| **B3** | MEGA_MENU | **HEADER_NAV** variant (`mega_menu: true` in notes) — **not** separate id |
| **B4** | THANK_YOU | Page_type `ORDER_CONFIRMATION` + optional lightweight block — **defer** dedicated id to post-R01 |
| **B5** | SORT_CONTROLS | **FILTERS** sub-variant — **no** separate id |

### Tier C — Defer post-R01.2

`DEALER_LOCATOR`, `SPEC_TABLE`, `COMPARE_BAR`, `ACCOUNT_NAV`, `SUB_NAV`, standalone `UTILITY_NAV`, `FACET_CHIPS` as separate ids.

---

## Recommended Next Step

1. **Human review** this design report — confirm Tier A/B/C split and duplicate-risk dispositions.
2. **Complete WF-R01.1 P2–P5** (minimum **B3** STOP rule in OPERATIONAL-INDEX before registry row execution).
3. **Authorize WF-R01.2 charter pass** (separate task) — publish `wf-r01-2-structural-blocks-charter-v1.md` with ACCEPTED criteria mirroring Gate 1–2 above.
4. **Only after charter ACCEPTED:** execution task to add Tier A BLOCK-CONTRACT rows + matrix updates — **still no reference partials** (WF-R01.3).
5. **Parallel (non-blocking):** WF-R01.7 interim Template-Art LANDING-only policy in OPERATIONAL-INDEX if not yet published.

**STOP AFTER REPORT — NO IMPLEMENTATION — NO REGISTRY CHANGES — NO NEW BLOCK IDs — NO BLUEPRINT CHANGES**

---

*Design artifact: `reports/wf-r01-2-structural-blocks-program-design-v1.md`*  
*Evidence: wf-r01-registry-expansion-program-charter-v1.md, wf-r01-1-v0-v1-binding-charter-v1.md, foundry-registry-expansion-program-design-v1.md, foundry-registry-layer-audit-v1.md, foundry-system-wide-layer-audit-v1.md, foundry-capability-gap-audit-v1.md, BLOCK-REGISTRY-v1.md, BLOCK-REGISTRY-GAPS-v1.md, BLOCK-GAPS-v1.md, SITE-TYPE-REGISTRY-v1.md, website-factory-production-modes-charter-v1.md, execution-cases-registry-v1.md, layout-shell-governance.md.*
