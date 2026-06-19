# REPORT — WF-R01.3 REFERENCE EXPANSION PROGRAM DESIGN

**Subprogram ID:** WF-R01.3 — Reference Expansion Program  
**Program parent:** WF-R01 — FOUNDRY Registry Expansion Program (**CHARTERED**)  
**Version:** v1  
**Date:** 2026-06-19  
**Mode:** проектирование программы — **без implementation**

**Authority:** [wf-r01-registry-expansion-program-charter-v1.md](wf-r01-registry-expansion-program-charter-v1.md) · [foundry-registry-expansion-program-design-v1.md](foundry-registry-expansion-program-design-v1.md) · [wf-r01-1-v0-v1-binding-charter-v1.md](wf-r01-1-v0-v1-binding-charter-v1.md) · [wf-r01-2-structural-blocks-charter-v1.md](../projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md) · [foundry-vocabulary-canon-charter-v1.md](../projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md)

**Audits:** [foundry-registry-layer-audit-v1.md](foundry-registry-layer-audit-v1.md) · [foundry-system-wide-layer-audit-v1.md](foundry-system-wide-layer-audit-v1.md) · [foundry-capability-gap-audit-v1.md](foundry-capability-gap-audit-v1.md)

**Research:** [rv-01-production-vocabulary.md](../research/foundry/rv-01-production-vocabulary.md) · [rv-02-website-production-systems.md](../research/foundry/rv-02-website-production-systems.md) · [rv-03-pixel-factory.md](../research/foundry/rv-03-pixel-factory.md)

**Honesty boundary:** WF-R01.3 — **documentation and program design** for controlled reference-layer expansion. **Не** runtime, **не** orchestration, **не** создание partials, **не** registry row edits, **не** новые IDs.

**Терминология:** **FOUNDRY** = **Website Factory** ecosystem (строка FOUNDRY как отдельный продукт/путь в repo **не найдена**).

---

## Executive Summary

Три аудита FOUNDRY (Registry Layer, System-Wide Layer, Capability Gap) **единогласно** фиксируют один bottleneck:

```text
Registry Coverage  >  Reference Coverage  >  Site Coverage
```

Registry знает **29** канонических `block_id` (+ **3** structural vocabulary terms из WF-R01.2, ещё **без rows**). Reference workspace реализует **9** partials (~**31%** partial coverage). Factory **не может честно собрать** blueprint-обещания для CATALOG, CORPORATE, ECOMMERCE и multi-page PROMO — даже в режиме `TEMPLATE_ART`.

**WF-R01.3** проектирует программу **расширения Reference Layer** — слоя реализационных артефактов между Registry (vocabulary SSOT) и client workspaces. Цель: закрыть **composition truth gap** без смешения с registry expansion (WF-R01.2), pattern catalogs (WF-R01.4), или Pixel Factory (WF-A03).

**Ключевые решения дизайна:**

| Решение | Суть |
|---------|------|
| **Четыре типа reference-артефактов** | Partial · Scaffold · Composition · Blueprint-instance — разные гранулярности, разные метрики |
| **Пятимерная coverage model** | Registry · Partial · Scaffold · Site · Page — не сводить к одной цифре |
| **Четыре readiness gates** | G0→G4 с denominator **32** (29 Core + 3 structural Tier A) — **планировочные** пороги, не machine gates |
| **MANUFACTURER / AUTO** | Vertical **composition profiles** поверх `CATALOG` + `CORPORATE` — **не** новые `site_type_code` в рамках WF-R01.3 |
| **TEMPLATE_ART** | Минимальные reference sets per Core 4 types; interim **LANDING-only** до Gate 2 |
| **WF-A03** | **DEFERRED**; WF-R01.3 Gate 2+ — **recommended precondition**, не auto-start |

**Explicit non-goals:** создание partials, registry rows, curated-library v2 implementation, enrollment execution cases, WF-A03 charter.

---

## Reference Model

Reference Layer — **реализационный мост** между Registry vocabulary и operable Factory assembly. Четыре артефактных класса **не взаимозаменяемы**.

### Layer placement

```text
Registry row (block_id / site_type_code)     ← vocabulary SSOT (WF-R01.1, WF-R01.2)
        │
        ▼ instantiates (blueprint / matrix)
Blueprint (site-type planning artifact)      ← composition plan (не reference layer)
        │
        ▼ evidenced by
┌───────┴───────────────────────────────────────────────┐
│              REFERENCE LAYER (WF-R01.3)                  │
│  Composition (doc) → Scaffold (page) → Partial (block)  │
│  Blueprint-instance (site-type slice in reference ws)   │
└─────────────────────────────────────────────────────────┘
        │
        ▼ adopted into
Client workspace (_template-client-v1, pilot, delivery)
```

### Reference Partial

| Field | Definition |
|-------|------------|
| **What** | **Block-level** implementation evidence for exactly **one** canonical `block_id` |
| **Form** | `partials/sections/{block_id}.html` + matching SCSS (+ optional scoped JS) in `website-factory-reference-v1/` |
| **Binding** | 1:1 with `block_id`; `data-block-id` hook; maps to BLOCK-CONTRACT semantics |
| **Quality** | Tier T0–T3 per program design (T0 = registry-only; T1 = build pass; T2 = curated + extraction report; T3 = battle-tested in client workspace) |
| **Not** | Page assembly; multi-block narrative; commercial `pattern_id`; blueprint document |

**Current baseline (repo fact):** 9 partials — `hero`, `social_proof`, `pricing`, `lead_form`, `cta_band`, `contact_block`, `sticky_cta`, `faq`, `cases` — mapping to registry terms `HERO`, `TRUST`/`SOCIAL_PROOF` (undisposed split), `PRICING`, `LEAD_FORM`, `CTA`, `CONTACTS`, `FAQ`, `CASES` + sticky CTA as module.

**Disposition note:** `social_proof.html` currently **collapses** `TRUST` and `TESTIMONIALS` — WF-R01.3 waves must treat split as **reference hygiene**, not registry change.

### Reference Scaffold

| Field | Definition |
|-------|------------|
| **What** | **Page-level** assembly skeleton demonstrating IA role + block stack for one `page_type` |
| **Form** | Reference workspace page entry (`src/pages/{page}.html`) wiring layout shell + ordered `@@include` of partials (or documented stubs where partial missing) |
| **Binding** | 1:1 with `page_type` (from PAGE-TYPE-REGISTRY-v1), constrained by site-type blueprint |
| **Purpose** | Prove **assembly path** before all partials reach T1; expose dependency order (structural → content → conversion) |
| **Honesty rule** | Scaffold **must** declare which includes are **stub** vs **T1+ partial** — no silent placeholder marketing copy in production claims |
| **Not** | A partial; not a client deliverable; not PIXEL_PERFECT design evidence |

**Examples (planned, not implemented):**

| Scaffold | page_type | Minimum block stack |
|----------|-----------|---------------------|
| `catalog-plp-scaffold` | `CATEGORY_PAGE` | HEADER_NAV → BREADCRUMBS → FILTERS → PRODUCT_GRID → PAGINATION → FOOTER |
| `promo-services-scaffold` | `SERVICE_PAGE` | HEADER_NAV → HERO → SERVICES → PROCESS → CTA → FOOTER |
| `corporate-about-scaffold` | `ABOUT_PAGE` | HEADER_NAV → ABOUT → TEAM → PARTNERS → FOOTER |

### Reference Composition

| Field | Definition |
|-------|------------|
| **What** | **Documentation artifact** — ordered `block_id` stack for a `page_type` or blueprint slice, with stance (REQUIRED/OPTIONAL/FORBIDDEN) |
| **Form** | Markdown table or matrix row — lives in reference expansion roadmap, PAGE-BLOCK-MAPPING crosswalk, or per-wave charter |
| **Binding** | Many compositions per site type; derived from PAGE-BLOCK-MAPPING + BLUEPRINT-BLOCK-MAPPING (registry SSOT) |
| **Purpose** | Plan waves **before** code; measure **Page Coverage** independently of partial existence |
| **Not** | Implementation; not a new vocabulary ID; does not override registry matrices |

**Distinction from Blueprint:** Site-type **Blueprint** (e.g. `LANDING-BLUEPRINT-v1`) = planning SSOT for whole project IA. **Reference Composition** = **one page's** block stack as reference implementation target.

### Reference Blueprint (instance)

| Field | Definition |
|-------|------------|
| **What** | **Site-type slice** in reference workspace demonstrating end-to-end blueprint → pages → blocks → build |
| **Form** | Minimal multi-page subtree in `website-factory-reference-v1/` + companion doc naming which blueprint ACCEPTED row it instantiates |
| **Binding** | 1:1 with Core `site_type_code` blueprint (LANDING, PROMO, CATALOG, …) at **reference-demo** fidelity |
| **Purpose** | Operator proof that Factory can **assemble** a site type — not merely list blocks in registry |
| **Not** | Replacement for canonical blueprint markdown in `blueprints/`; not client delivery |

**Naming discipline:** Use **«Reference Blueprint-instance»** or **«reference site slice»** in prose to avoid collision with vocabulary canon term **Blueprint** (operational planning artifact).

### Cross-artifact dependency rules

| Rule | Enforcement |
|------|-------------|
| Partial **cannot** promote to T2 curated without v1 `block_id` (WF-R01.1) | Human STOP rule |
| Scaffold **cannot** claim Template-Art readiness if >50% of REQUIRED stack is stub | Gate honesty |
| Composition **precedes** scaffold for new page types | Wave planning order |
| Blueprint-instance **requires** ≥1 scaffold per primary `page_type` of that site type | Site Coverage metric |
| Structural partials (HEADER_NAV, FILTERS, SEARCH) **block** catalog blueprint-instance | WF-R01.2 vocabulary + WF-R01.3 W4 |

### Summary comparison

| Artifact | Granularity | Primary metric | Typical location |
|----------|-------------|----------------|------------------|
| **Reference Partial** | 1 `block_id` | Partial Coverage | `src/partials/sections/` |
| **Reference Scaffold** | 1 `page_type` | Scaffold Coverage | `src/pages/` |
| **Reference Composition** | 1 page stack (doc) | Page Coverage (doc) | Expansion roadmap / mapping |
| **Reference Blueprint-instance** | 1 `site_type_code` slice | Site Coverage | Multi-page reference subtree + doc |

---

## Coverage Model

**Ошибка:** сводить зрелость Factory к одной цифре «9/29». Registry completeness **≠** buildability.

### Dimensions

| Dimension | Symbol | Definition | Numerator | Denominator (in-scope) | Current baseline (repo) |
|-----------|--------|------------|-----------|------------------------|-------------------------|
| **Registry Coverage** | **RC** | Share of in-scope vocabulary with registry row + minimum BLOCK-CONTRACT | Defined `block_id` rows | In-scope set per program phase | **29/29** Core blocks documented; **0/3** structural rows (vocabulary only, WF-R01.2) |
| **Reference Partial Coverage** | **RPC** | Share of in-scope `block_id` with T1+ partial in reference workspace | Partials with `npm run build` PASS | Same in-scope block set | **9/29** (~31%) Core only; **9/32** (~28%) if structural included |
| **Reference Scaffold Coverage** | **RSC** | Share of required `page_type` scaffolds per site type | Scaffold pages (stub-declared) | PAGE-TYPE-REGISTRY required set per site type | **~1/10+** (LANDING index only — **SAFE UNKNOWN** exact page_type count) |
| **Site Coverage** | **SC** | Share of `site_type_code` meeting Template-Art minimum reference set | Site types passing SC checklist | Core 5 (+ profiles for MANUFACTURER/AUTO) | **1/5** Core (LANDING partial); **0/3** Extended |
| **Page Coverage** | **PC** | Share of in-scope `page_type` with published Reference Composition | Documented compositions | Primary + secondary pages per active site-type expansion wave | **Partial** — matrices exist; reference-target compositions **not published** |

### In-scope set evolution

| Phase | Denominator for RPC | Notes |
|-------|---------------------|-------|
| **Pre–WF-R01.2 Gate 2** | 29 Core `block_id` | Structural terms exist in vocabulary only |
| **Post–WF-R01.2 Gate 2** | **32** = 29 + HEADER_NAV + FILTERS + SEARCH | Aligns with parent program M1/M2 |
| **Post–vertical charters** | 32 + future ids | **Out of WF-R01.3 v1 scope** — no new IDs |

### Coverage inequality (design invariant)

```text
RC ≥ RPC ≥ RSC (per page) ≥ SC (per site type)
```

**Page Coverage (PC)** is **orthogonal** — compositions can be documented at **100%** while RPC is **31%** (planning ahead of code).

### Reporting contract

Every WF-R01.3 wave REPORT **must** state all five dimensions — never «registry complete» from RC alone.

| Misclaim | Corrective |
|----------|------------|
| «29 blocks in registry» → «Factory-ready» | Cite RPC and SC |
| «Reference workspace exists» → «CATALOG-ready» | Cite RSC for CATEGORY_PAGE + structural RPC |
| «Blueprint ACCEPTED» → «Template-Art allowed» | Cite SC + WF-R01.7 matrix |

### Curated library alignment

`curated-library-index-v1.md` tracks **9 rows** with **v0 snake_case** names — **Partial Coverage operational view** only. WF-R01.3 design targets **curated-library v2** (documentation) with v1 `block_id` sync — **implementation deferred** to wave execution, not this design pass.

---

## Readiness Gates

Gates — **human-operated program milestones** for WF-R01.3. **Not** machine CI gates. Denominator **32** = 29 Core + 3 structural Tier A (per WF-R01.2 charter vocabulary).

### Gate table

| Gate | Name | RPC target | Primary deliverables | Unlocks |
|------|------|------------|----------------------|---------|
| **G0** | Baseline | **9/32** (~28%) | Documented baseline; golden slice; 9 partials | LANDING Template-Art **HITL pilot** only |
| **G1** | LANDING + shell | **14/32** (~44%) | BENEFITS, PROCESS, TESTIMONIALS split; HEADER_NAV, FOOTER, LEGAL_LINKS partials; structural rows in registry (WF-R01.2 execution) | Honest global shell; LANDING completion |
| **G2** | PROMO + CATALOG scaffold | **20/32** (~63%) | SERVICES, TEAM, ABOUT; FILTERS, SEARCH, catalog grids; PLP scaffold; PROMO money-page scaffold | Template-Art **pilot** PROMO + CATALOG; WF-A03 precondition (**recommended**) |
| **G3** | ECOMMERCE + CORPORATE slice | **29/32** (~91%) | CART, CHECKOUT, PAYMENT, DELIVERY; PARTNERS, CERTIFICATES, MAP, FEATURES, REVIEWS | ECOMMERCE staging HITL; CORPORATE pilot |
| **G4** | Full Core reference | **32/32** (100%) | Remaining shell explicit partials; scaffold coverage for primary page types; blueprint-instances for Core 5 | Full Core SC (excl. ECOMMERCE legal E1–E4) |

### Gate math verification

| Check | Verdict |
|-------|---------|
| **9/29 vs 9/32** | Parent program used **9/29** when structural not in registry denominator. WF-R01.3 **standardizes on 32** post–R01.2 vocabulary. G0 = **9/32 (~28%)**, not 31% — both valid if denominator explicit |
| **14/32 (~44%)** | W1 (+3: BENEFITS, PROCESS, TESTIMONIALS) + W2 (+3: HEADER_NAV, FOOTER, LEGAL_LINKS) + split disposition ≈ **15**; **14** is conservative planning target — **acceptable** |
| **20/32 (~63%)** | W3 (+3) + W4 (+4 structural/list) + W5 (+4 catalog) ≈ **22** from G0; **20** implies parallelization or staged stubs — **acceptable** with explicit stub policy |
| **29/32 (~91%)** | W6 (+4 ecommerce) + W7 (+5 mixed) ≈ **18** new from G2 — math holds if overlaps (FOOTER etc.) not double-counted |
| **32/32** | Requires WF-R01.2 structural rows **and** partials — **co-dependent** |

**Correction vs informal «9/29»:** Always pair numerator with denominator in REPORTs. After WF-R01.2 Gate 2, **prefer 32**.

### Gate dependencies (cross-program)

```text
WF-R01.1 B3 (STOP rule) ──────────────────────────┐
WF-R01.2 Gate 2 (structural registry rows) ─────┼──► WF-R01.3 G1 minimum
WF-R01.3 wave N build PASS ───────────────────────┘
WF-R01.7 Template-Art matrix ACCEPTED ────────────► SC claims for multi-type
WF-R01.4 ≥4 pattern_id ───────────────────────────► conversion surfaces in scaffolds
```

### Gate exit evidence (per gate)

| Evidence type | Required |
|---------------|----------|
| RPC count | Manual count `src/partials/sections/` vs in-scope set |
| Build PASS | `npm run build` in reference workspace after each wave |
| Extraction REPORT | Wave 5–6 discipline for T2+ promotions |
| Composition doc | Updated Reference Composition tables for new page types |
| SC checklist | Per-site-type Template-Art minimum (§ Template-Art Impact) |

---

## Site Type Priority

### Registry vs vertical profiles

| site_type_code | Registry home | WF-R01.3 role |
|----------------|---------------|---------------|
| LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE | Core 5 — SITE-TYPE-REGISTRY-v1 | Primary expansion targets |
| MARKETPLACE | Extended 3 | **Out of Core reference scope** — classification only |
| **MANUFACTURER** | **Not a v1 `site_type_code`** | **Vertical profile:** `CATALOG` + `CORPORATE` + B2B notes |
| **AUTO** | **Not a v1 `site_type_code`** | **Vertical profile:** `CATALOG` + dealer/commerce notes |

### Per-type assessment

| Type | Current readiness | Required reference set (minimum) | Expansion priority | Primary wave |
|------|-------------------|----------------------------------|--------------------|--------------|
| **LANDING** | **RPC ~69%** of LANDING stack (9 partials cover core conversion path); SC **partial** | HERO, BENEFITS, PROCESS, TRUST/TESTIMONIALS, PRICING, FAQ, CASES, CTA, LEAD_FORM, CONTACTS, FOOTER, LEGAL_LINKS | **P0 — complete** | W1, W2 |
| **PROMO** | Blueprint ACCEPTED; RPC **low**; no reference blueprint-instance | LANDING set + SERVICES, TEAM, ABOUT, multi-page scaffolds (SERVICE_PAGE, ABOUT_PAGE) | **P1** | W3 |
| **CATALOG** | Blueprint ACCEPTED; **no** structural partials; BZPM evidence **outside** Factory | HEADER_NAV, SEARCH, FILTERS, CATEGORIES, CATEGORY_GRID, PRODUCT_GRID, PRODUCT_CARD, BREADCRUMBS, PAGINATION, FOOTER + PLP/PDP scaffolds | **P1** (ties PROMO) | W4, W5 |
| **CORPORATE** | Blueprint ACCEPTED; shallow; hybrid IA | HEADER_NAV, ABOUT, TEAM, PARTNERS, CERTIFICATES, MAP, SERVICES, CONTACTS, LEGAL_LINKS, FOOTER + route-group scaffolds | **P2** | W7 |
| **ECOMMERCE** | Blueprint ACCEPTED; legal E1–E4 **FUTURE**; commerce chain registry-only | CATALOG set + CART, CHECKOUT, PAYMENT, DELIVERY + utility page scaffolds | **P3** (staging only) | W6 |
| **MANUFACTURER** (profile) | **NR** Factory pipeline; BZPM proxy | CATALOG reference set + CORPORATE trust blocks + RFQ/`lead-form-v1` pattern surface (doc); spec-table **post-R01** | **P1** (via CATALOG) | W4–W5 + R01.4 |
| **AUTO** (profile) | OCPilot SITE-001; **unverified** Factory binding | CATALOG set + vehicle PDP composition notes + FILTER variants; no new vertical `block_id` | **P2** (via CATALOG) | W4–W5 + R01.8 |
| **MARKETPLACE** | Extended — concept only | **Deferred** — requires extended architecture charter beyond WF-R01 | **P4 — out of scope** | — |

### Priority sequence (recommended)

```text
P0  LANDING completion (G1)
    ↓
P1  CATALOG corridor + MANUFACTURER profile (G2)  ║  PROMO money-page (G2)
    ↓
P2  CORPORATE slice + AUTO profile (G3)
    ↓
P3  ECOMMERCE chain staging (G3–G4)
    ↓
P4  MARKETPLACE — explicit charter only
```

### Readiness labels (honest)

| Label | Meaning |
|-------|---------|
| **Reference-ready** | SC checklist pass for `TEMPLATE_ART` at declared gate |
| **Pilot** | Scaffold exists; >1 stub or mandatory HITL per block |
| **Blocked** | Missing structural vocabulary rows or RPC below gate |
| **Ad-hoc only** | Delivery proven outside Factory (BZPM, Sibcar) — not SC |

---

## Template-Art Impact

Per WF-A01: in `TEMPLATE_ART`, **IA + Block Registry = SSOT**; visual from Factory foundations. Reference Layer **directly bounds** Template-Art honesty.

### Interim policy (mandatory until G2)

Passport must state **«TEMPLATE_ART — LANDING scope only»** for undeclared multi-type attempts (parent program WF-R01.7 interim).

### Minimum reference sets (Core 4)

Sets = **T1+ partials** required **plus** **Reference Composition** published **plus** scaffolds for primary `page_type`. Structural blocks require WF-R01.2 registry rows before Template-Art claims.

#### LANDING

| Category | Required `block_id` / artifacts |
|----------|-------------------------------|
| **Conversion** | HERO, BENEFITS, CTA, LEAD_FORM, PRICING (if offer), STICKY_CTA (module) |
| **Trust** | TRUST and/or TESTIMONIALS, CASES, FAQ |
| **Contact** | CONTACTS, MAP (optional) |
| **Shell** | FOOTER, LEGAL_LINKS; HEADER_NAV minimal |
| **Composition** | `LANDING_PAGE` stack documented |
| **Gate** | **G1** for production Template-Art; **G0** HITL pilot today |

#### PROMO

| Category | Required |
|----------|----------|
| **LANDING minimum** | Full LANDING set |
| **Multi-page** | SERVICES, TEAM, ABOUT, PROCESS |
| **Scaffolds** | `SERVICE_PAGE`, `ABOUT_PAGE`, `CONTACT_PAGE` |
| **Shell** | HEADER_NAV full |
| **Gate** | **G2 pilot** |

#### CATALOG

| Category | Required |
|----------|----------|
| **Structural** | HEADER_NAV, SEARCH, FILTERS |
| **Catalog content** | CATEGORIES, CATEGORY_GRID, PRODUCT_GRID, PRODUCT_CARD |
| **Orientation** | BREADCRUMBS, PAGINATION (partial or layout policy per WF-R01.2) |
| **Trust** | TRUST, FAQ (optional) |
| **Scaffolds** | `CATEGORY_PAGE`, `PRODUCT_PAGE`, `SEARCH_RESULTS_PAGE` |
| **Shell** | FOOTER, LEGAL_LINKS |
| **Gate** | **G2 pilot** (scaffold); **G3** for broader SC |

#### CORPORATE

| Category | Required |
|----------|----------|
| **Structural** | HEADER_NAV |
| **Corporate content** | ABOUT, TEAM, PARTNERS, CERTIFICATES, SERVICES |
| **Trust** | CASES, TESTIMONIALS, MAP |
| **Legal** | LEGAL_LINKS, FOOTER |
| **Scaffolds** | `ABOUT_PAGE`, `CONTACT_PAGE`, hybrid route-group note |
| **Gate** | **G3 pilot** |

### Template-Art readiness matrix (target)

| site_type_code | G0 today | After G1 | After G2 | After G4 |
|----------------|----------|----------|----------|----------|
| LANDING | **Allowed** (HITL) | **Allowed** | **Allowed** | **Allowed** |
| PROMO | **Blocked** | **Blocked** | **Pilot** | **Allowed** |
| CATALOG | **Blocked** | **Blocked** | **Pilot** | **Allowed** (HITL) |
| CORPORATE | **Blocked** | **Blocked** | **Blocked** | **Pilot** |
| ECOMMERCE | **Blocked** | **Blocked** | **Blocked** | **Pilot** (no legal E1–E4) |

### Additional Template-Art prerequisites (non-reference, parallel)

| # | Requirement | Owner subprogram |
|---|-------------|------------------|
| 1 | v0→v1 binding enforced | WF-R01.1 |
| 2 | Structural vocabulary → registry rows | WF-R01.2 |
| 3 | Commercial pattern catalog v0 | WF-R01.4 |
| 4 | SEO content formulas | WF-R01.5 |
| 5 | Wireframe artifact contract | Post-R01 / parallel |
| 6 | Design token doc bind (DG-01) | Parallel Priority B |

---

## Execution Case Feed

Execution cases **feed** reference expansion **without** modifying case workspaces in this design pass. Method: **extraction discipline** + **lesson index** (WF-R01.8).

### Case → reference contribution matrix

| Case | Workspace / status | Reference knowledge (mineable) | WF-R01.3 routing | Anti-patterns |
|------|-------------------|-------------------------------|------------------|---------------|
| **Triumph** | `triumph-manipulator-landing-v6/` — highest live evidence | LANDING blocks: faq, pricing, cases extractions; `scroll_process_timeline`; RU QA preset; PROMO multi-page patterns; PROCESS, BENEFITS, TEAM candidates | **W1, W3** partials; **W2** nav minimal; **R01.4** pattern | **Do not** auto-canonicalize full v6 tree; client authority parallel to LOC |
| **ISBD** | `isbd-care-landing/` — client #2 | Care vertical LANDING; lighter Factory binding; FEATURES, REVIEWS, adoption/freeze pattern | **W7** FEATURES, REVIEWS; adoption validation template | Not a catalog/manufacturer source |
| **BZPM** | No Factory workspace; OCPilot TEST live | CATALOG/manufacturer: filters, megamenu, PLP/PDP, faceted UX, industry taxonomy, HEADER_NAV depth | **W4–W5** structural + catalog vocabulary (**doc-first**); enrollment **pending** W3 blueprint | OpenCart delivery **≠** Factory reference; vocabulary mining **HITL only** |
| **FP-0002** | `fp-0002-shpigovsky-frontend/` — PIXEL_PERFECT stress | VL3 domains, false-green, Group/Layout laws, asset collision — **negative evidence** | **Not** primary block source; informs QA adoption parallel track; boundary Template-Art vs PIXEL | **Do not** promote FP-0002 sections to reference partials without PIXEL→TEMPLATE scope change |

### Feed workflow (design)

```text
Execution case evidence
        │
        ▼  extraction discipline (neutralized, data-block-id, REPORT)
Candidate partial / composition note
        │
        ▼  WF-R01.1 v1 block_id binding check
Reference wave charter (per block)
        │
        ▼  npm run build + QA
T1+ partial → T2 curated (optional)
        │
        ▼  WF-R01.8 lesson row (closed loop)
```

### Case suitability tiers

| Tier | Cases | Use |
|------|-------|-----|
| **Primary drivers** | Triumph, BZPM (vocabulary), ISBD | Wave prioritization |
| **Parallel discipline** | FP-0002 | Validation adoption — not RPC |
| **Pending enrollment** | BZPM Factory workspace, Sibcar (OCPilot SITE-001) | Post–G2 decisions |

### FP-0002 explicit boundary

FP-0002 **must not** inflate RPC. It informs **WF-A02 adoption** and **operator visual approval law** — reference expansion proceeds from **TEMPLATE_ART-aligned** sources (Triumph, ISBD, BZPM doc mining).

---

## Program Structure

WF-R01.3 decomposes into **five subprograms** + **one cross-cutting metrics track**. All **design-only** in this pass.

```
WF-R01.3  Reference Expansion Program
│
├── WF-R01.3.1  Coverage Model & Metrics Charter
├── WF-R01.3.2  LANDING Completion Track
├── WF-R01.3.3  Structural & Shell References
├── WF-R01.3.4  Catalog & Vertical Profile References
├── WF-R01.3.5  Corporate & Commerce Reference Slices
└── WF-R01.3.X  Gates, Reporting & Curated Library v2 Spec (cross-cutting)
```

### WF-R01.3.1 — Coverage Model & Metrics Charter

| Field | Value |
|-------|-------|
| **Goal** | Publish normative five-dimension coverage model (this document § Coverage Model) as operator charter |
| **Deliverables** | Metrics definitions RC/RPC/RSC/SC/PC; REPORT template; misclaim corrective table; denominator policy (29 vs 32) |
| **Dependency** | WF-R01.1 ACCEPTED |
| **Blocks** | All other R01.3 tracks |

### WF-R01.3.2 — LANDING Completion Track

| Field | Value |
|-------|-------|
| **Goal** | Close LANDING RPC gaps; TRUST/TESTIMONIALS disposition; reach **G1** |
| **Deliverables** | Wave W1 partials (BENEFITS, PROCESS, TESTIMONIALS split); LANDING Reference Composition; updated golden slice pointer |
| **Dependency** | R01.3.1; WF-R01.1 B3 |
| **Evidence** | Triumph extractions |
| **Target** | RPC **≥14/32** |

### WF-R01.3.3 — Structural & Shell References

| Field | Value |
|-------|-------|
| **Goal** | First T1+ structural partials after WF-R01.2 registry rows |
| **Deliverables** | Wave W2 (HEADER_NAV, FOOTER, LEGAL_LINKS); global shell scaffold; layout-component policy for BREADCRUMBS/PAGINATION |
| **Dependency** | **WF-R01.2 Gate 2** (registry rows); R01.3.2 parallel allowed for FOOTER |
| **Evidence** | reference-v1 layout; BZPM nav patterns (**doc**) |
| **Target** | Structural RPC **3/3**; contributes to G1 |

### WF-R01.3.4 — Catalog & Vertical Profile References

| Field | Value |
|-------|-------|
| **Goal** | CATALOG corridor + MANUFACTURER/AUTO **profiles** (composition docs + scaffolds) |
| **Deliverables** | W4–W5 partials; PLP/PDP scaffolds; vertical profile docs (no new `site_type_code`); BZPM lesson crosswalk |
| **Dependency** | R01.3.3; WF-R01.2 structural rows |
| **Evidence** | BZPM audits; Sibcar notes via R01.8 |
| **Target** | RPC **≥20/32** (G2); SC pilot CATALOG |

### WF-R01.3.5 — Corporate & Commerce Reference Slices

| Field | Value |
|-------|-------|
| **Goal** | CORPORATE slice + ECOMMERCE chain staging |
| **Deliverables** | W6–W7 partials; corporate scaffolds; ecommerce utility scaffolds; blueprint-instance docs for Core types |
| **Dependency** | R01.3.4 Gate 2 minimum |
| **Evidence** | ISBD (CORPORATE-light); blueprint chains |
| **Target** | RPC **≥29/32** (G3) → **32/32** (G4) |

### WF-R01.3.X — Gates, Reporting & Curated Library v2 Spec

| Field | Value |
|-------|-------|
| **Goal** | Cross-cutting gate sign-off, wave REPORT standard, curated-library v2 **spec** (v1 `block_id` names) |
| **Deliverables** | Gate checklist G0–G4; integration with M2 parent metrics; sync discipline with `registry-sync-discipline-v1.md` |
| **Dependency** | R01.3.1 |
| **Parallel** | All waves |

### Wave map (execution order design)

| Wave | Blocks (vocabulary terms) | Subprogram | Gate contribution |
|------|---------------------------|------------|-------------------|
| **W1** | BENEFITS, PROCESS, TESTIMONIALS | R01.3.2 | G1 |
| **W2** | HEADER_NAV, FOOTER, LEGAL_LINKS | R01.3.3 | G1 |
| **W3** | SERVICES, TEAM, ABOUT | R01.3.2 / PROMO | G2 |
| **W4** | FILTERS, SEARCH, BREADCRUMBS, PAGINATION | R01.3.4 | G2 |
| **W5** | CATEGORIES, CATEGORY_GRID, PRODUCT_GRID, PRODUCT_CARD | R01.3.4 | G2 |
| **W6** | CART, CHECKOUT, PAYMENT, DELIVERY | R01.3.5 | G3 |
| **W7** | FEATURES, REVIEWS, CERTIFICATES, PARTNERS, MAP | R01.3.5 | G3–G4 |

### Relationship to parent WF-R01 subprograms

| Parent | WF-R01.3 relationship |
|--------|----------------------|
| **R01.1** Binding | **Hard prerequisite** — v1 `block_id` on all partials |
| **R01.2** Structural | **Hard prerequisite** for W4+ and catalog Template-Art |
| **R01.4** Commercial patterns | Informs conversion surfaces inside scaffolds — parallel |
| **R01.5** SEO slice | Informs page compositions — parallel |
| **R01.6** Registry hygiene | TRUST/TESTIMONIALS disposition — coordinates with W1 |
| **R01.7** Template-Art | **Consumer** of SC metrics from R01.3 |
| **R01.8** Execution cases | **Feeder** — prioritization input |

---

## WF-A03 Relationship

### Authority chain (current)

```text
WF-A01  Production Modes           ✅ Complete
WF-A02  Validation Architecture    ✅ Complete (+ VL3)
WF-R01  Registry Expansion         ◆ CHARTERED (R01.1 ACCEPTED, R01.2 ACCEPTED charter)
WF-R01.3 Reference Expansion       ◆ DESIGN (this document)
WF-A03  Pixel Factory Expansion    ⏸ DEFERRED
```

### What WF-A03 is

Per roadmap: Vision Layer, Visual Diff, Pixel QA Runtime, Screenshot Engine, Agent Runtime — **visual verification** stack for `PIXEL_PERFECT` portfolio. **Not** composition vocabulary.

### What WF-R01.3 must complete before WF-A03 (recommended)

| # | WF-R01.3 outcome | Rationale |
|---|------------------|-----------|
| 1 | **G2 reached** (RPC ≥63%, catalog scaffold exists) | WF-A03 on catalog/manufacturer without reference = **false-green at pixel layer** |
| 2 | **R01.3.1 metrics charter ACCEPTED** | Pixel diff needs stable `data-block-id` reference baselines |
| 3 | **Structural partials T1+** (HEADER_NAV, FILTERS, SEARCH) | VL3 composition domains assume shell/catalog surfaces **exist** |
| 4 | **TEMPLATE_ART readiness matrix** (WF-R01.7) aligned with SC | Avoid Pixel Factory on undeclared multi-type scope |
| 5 | **Curated library v2 spec** published | Visual regression needs v1-id stable reference row names |
| 6 | **Web-GPT Research Pass** (operator reminder) | External refresh — **not** replaceable by WF-R01.3 |

### What WF-R01.3 does **not** block

| Work | Notes |
|------|-------|
| VL3 adoption on PIXEL_PERFECT greenfield | FP-0002 parallel track |
| WF-R01.4 / R01.5 documentation slices | Parallel |
| Client delivery (Triumph, ISBD, OCPilot) | Outside reference canon — explicit |
| WF-A03 with **operator waiver** | Roadmap allows explicit waiver below G2 — **discouraged** |

### Sequencing diagram

```text
Reference Expansion (WF-R01.3)
  G0 ──► G1 (LANDING+shell) ──► G2 (catalog scaffold) ──► G3/G4
                                      │
                                      ▼ recommended precondition
                            WF-A03 Pixel Factory charter pass
                                      │
                                      ▼
                            Vision / Visual Diff / Pixel QA runtime (doc)
```

### RV-03 alignment

[rv-03-pixel-factory.md](../research/foundry/rv-03-pixel-factory.md) research informs WF-A03 scope. WF-R01.3 **feeds** WF-A03 with **reference baselines**; it **does not** implement pixel tooling.

---

## Risks

| Risk | Severity | Mitigation in WF-R01.3 design |
|------|----------|-------------------------------|
| **False «Factory-ready» from registry alone** | Critical | Five-dimension coverage in every REPORT; SC separate from RC |
| **TEMPLATE_ART on CATALOG before structural partials** | Critical | G2 gate; WF-R01.7 interim LANDING-only |
| **v0 snake_case in curated library during waves** | Critical | R01.3.X v2 spec; WF-R01.1 STOP rule |
| **BZPM/Sibcar lessons trapped in OCPilot silos** | High | R01.3.4 doc-first mining + R01.8 index; HITL enrollment |
| **Reference expansion without build validation** | High | `npm run build` per wave — mandatory evidence |
| **Triumph v6 mistaken as full PROMO/CORPORATE reference** | Medium | Explicit W1/W3 scope; extraction discipline |
| **Stub scaffolds counted as SC pass** | Medium | Stub declaration rule in scaffold definition |
| **WF-A03 started before G2** | Medium | Roadmap DEFERRED + recommended precondition in this design |
| **TRUST/TESTIMONIALS split breaks curated rows** | Medium | Coordinate W1 with R01.6 disposition |
| **ECOMMERCE pilot before Legal E1–E4** | High | G3 staging-only; not R01.3 exit requirement |
| **Gate math confusion (29 vs 32 denominator)** | Medium | R01.3.1 charter — explicit denominator policy |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| **FOUNDRY** as named product/path | **Not found** — Website Factory ecosystem used |
| **WF-R01.3 human owner / steward** | **Not fixed** in repo |
| **Exact page_type count** for RSC denominator | PAGE-TYPE-REGISTRY-v1 — **not counted** in this design pass |
| **BREADCRUMBS / PAGINATION** as `block_id` vs layout-component | WF-R01.2 policy — **operator decision pending** |
| **MEGA_MENU** separate `block_id` vs HEADER_NAV variant | WF-R01.2 — **variant** preferred; BZPM evidence **unevaluated** in Factory reference |
| **BZPM W3 blueprint** delivery date | **UNKNOWN** |
| **OCPilot SITE-001** `production_mode` + v1 binding | **Not verified** in audits |
| **VL3 adoption rate** on Triumph v6 / ISBD | **Not audited** |
| **Curated library v2** implementation timeline | Spec only in this design |
| **Manufacturer / Auto** as future Extended `site_type_code` | **Undecided** — profiles suffice for WF-R01.3 |
| **SPEC_TABLE, DEALER_LOCATOR** block vocabulary | **Post-R01** vertical charters |
| **Revenue / throughput metrics** | **No evidence** in repo |
| **Whether WF-R01.3 subprogram charters require separate ACCEPTED passes** | **Assumed yes** per R01.1/R01.2 pattern — **not explicitly confirmed** for R01.3 |

---

## Recommended Next Step

1. **Operator review** of this design document — confirm gate thresholds (G0–G4), site-type priority, and Template-Art minimum sets.
2. **Charter pass WF-R01.3.1** (Coverage Model & Metrics) — ACCEPTED status before any wave execution.
3. **Unblock WF-R01.2 Gate 2** (structural registry rows) in parallel with **R01.3.2** LANDING completion — R01.3.3/W4 **blocked** without rows.
4. **Publish baseline metrics snapshot** (RC/RPC/RSC/SC/PC) as first R01.3.X REPORT — denominator **32** declared.
5. **Do not** start WF-A03 charter until **G2 recommended precondition** met or explicit operator waiver recorded.

**STOP** — no implementation, no partial creation, no registry changes in this pass.

---

*Design artifact: `reports/wf-r01-3-reference-expansion-program-design-v1.md`*
