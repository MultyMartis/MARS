# WF-R01.3.1 — Coverage Model & Metrics Charter v1

**Subprogram ID:** WF-R01.3.1 — Coverage Model & Metrics  
**Program parent:** WF-R01.3 — Reference Expansion Program (design: [wf-r01-3-reference-expansion-program-design-v1.md](../../reports/wf-r01-3-reference-expansion-program-design-v1.md))  
**Grandparent:** WF-R01 — FOUNDRY Registry Expansion Program (**CHARTERED**)  
**Version:** v1  
**Date:** 2026-06-19  
**Charter pass:** [wf-r01-3-1-coverage-model-charter-pass-v1.md](../../reports/wf-r01-3-1-coverage-model-charter-pass-v1.md)  
**Design basis:** [wf-r01-3-reference-expansion-program-design-v1.md](../../reports/wf-r01-3-reference-expansion-program-design-v1.md) § Coverage Model · § Readiness Gates · § Template-Art Impact

**Honesty boundary:** WF-R01.3.1 — **documentation and metrics charter** (human-operated). **Не** runtime, **не** orchestration, **не** reference partial creation, **не** registry row edits, **не** новые IDs.

**Терминология:** **FOUNDRY** = **Website Factory** ecosystem (строка FOUNDRY как отдельный продукт/путь в repo **не найдена**).

---

## Charter sign-off

| Field | Value |
|-------|-------|
| **Status** | **ACCEPTED** |
| **Acceptance state** | Five-dimension coverage model and G0–G4 readiness gates are **normative operator authority** for WF-R01.3 reporting; wave execution **not authorized** by this charter alone |
| **Authority state** | WF-R01.3.1 = **ACCEPTED** · WF-R01.3 program design = **DESIGN** (parent subprogram tracks remain design until individually chartered) · WF-R01 program = **CHARTERED** |
| **T0** | **2026-06-19** — date of ACCEPTED publication |
| **Owner** | Website Factory operator governance (human-operated sign-off via charter pass; **named steward SAFE UNKNOWN**) |
| **Prior state** | DESIGN — [wf-r01-3-reference-expansion-program-design-v1.md](../../reports/wf-r01-3-reference-expansion-program-design-v1.md) § Coverage Model |
| **Blocks** | All other WF-R01.3 tracks (R01.3.2–R01.3.5, R01.3.X) — metrics charter is **hard prerequisite** |

**ACCEPTED means:** RC/RPC/RSC/SC/PC definitions, denominator policy, reporting contract, G0–G4 gates, Template-Art minimum reference sets, and WF-A03 precondition semantics are **binding** for operator REPORTs and wave planning. **Does not** mean partials exist, gates are reached, curated-library v2 is published, or WF-R01.3 wave execution has started.

---

## Executive Summary

Три аудита FOUNDRY (Registry Layer, System-Wide Layer, Capability Gap) **единогласно** фиксируют bottleneck:

```text
Registry Coverage  >  Reference Coverage  >  Site Coverage
```

**Ошибка оператора:** сводить зрелость Factory к одной цифре «9/29 partials» или «29 blocks in registry». Registry completeness **≠** buildability **≠** Template-Art honesty.

**WF-R01.3.1** публикует **пятимерную coverage model** и **пять readiness gates (G0–G4)** как normative metrics charter для Reference Expansion Program. Модель:

1. **Разделяет** vocabulary completeness (RC) от implementation evidence (RPC, RSC, SC).
2. **Стандартизирует** denominator **32** = 29 Core `block_id` + 3 structural Tier A vocabulary terms (HEADER_NAV, FILTERS, SEARCH) post–WF-R01.2.
3. **Связывает** coverage gates с Template-Art readiness per `site_type_code`.
4. **Определяет** G2 как **recommended precondition** для WF-A03 Pixel Factory — не auto-start trigger.

**Explicit boundary:** ACCEPTED charter **≠** reference partial expansion. Code execution belongs to WF-R01.3.2–R01.3.5 wave charters.

---

## Coverage Dimensions

Five dimensions **must not** be collapsed into a single percentage in operator REPORTs.

### Dimension table

| Dimension | Symbol | Definition | Numerator | Denominator (in-scope) | Baseline (repo fact, 2026-06-19) |
|-----------|--------|------------|-----------|------------------------|----------------------------------|
| **Registry Coverage** | **RC** | Share of in-scope vocabulary with registry row + minimum BLOCK-CONTRACT | Defined `block_id` rows | In-scope set per program phase | **29/29** Core blocks documented; **0/3** structural rows (vocabulary only, WF-R01.2 ACCEPTED) |
| **Reference Partial Coverage** | **RPC** | Share of in-scope `block_id` with **T1+** partial in reference workspace | Partials with `npm run build` PASS | Same in-scope block set | **9/29** (~31%) Core only; **9/32** (~28%) if structural included |
| **Reference Scaffold Coverage** | **RSC** | Share of required `page_type` scaffolds per active site-type expansion wave | Scaffold pages with stub-declared honesty | PAGE-TYPE-REGISTRY required set per site type | **~1/10+** (LANDING index only — exact count **SAFE UNKNOWN**) |
| **Site Coverage** | **SC** | Share of `site_type_code` meeting Template-Art minimum reference set (§ Template-Art minimum sets) | Site types passing SC checklist | Core 5 (+ MANUFACTURER/AUTO **profiles**, not separate codes) | **1/5** Core (LANDING partial); **0/3** Extended |
| **Page Coverage** | **PC** | Share of in-scope `page_type` with published **Reference Composition** (doc) | Documented compositions | Primary + secondary pages per active wave | **Partial** — matrices exist; reference-target compositions **not published** |

### Reference artifact classes (metric binding)

| Artifact class | Primary metric | Location (reference workspace) |
|----------------|----------------|--------------------------------|
| Reference Partial | **RPC** | `src/partials/sections/` — 1:1 with `block_id` |
| Reference Scaffold | **RSC** | `src/pages/` — 1:1 with `page_type` |
| Reference Composition | **PC** | Expansion roadmap / mapping docs — doc only |
| Reference Blueprint-instance | **SC** (component) | Multi-page subtree + companion doc |

### Quality tier binding (RPC numerator)

Partial counts toward RPC **only** at **T1+**:

| Tier | Meaning | Counts in RPC? |
|------|---------|----------------|
| **T0** | Registry-only | **No** |
| **T1** | Reference partial + `npm run build` PASS | **Yes** |
| **T2** | Curated library + extraction report | **Yes** (still T1+ floor) |
| **T3** | Battle-tested in client workspace | **Yes** (quality label; RPC floor unchanged) |

**Rule:** no partial promoted without v1 `block_id` (WF-R01.1 B3 STOP policy when live).

### In-scope set evolution

| Phase | Denominator for RPC / RC | Notes |
|-------|--------------------------|-------|
| **Pre–WF-R01.2 Gate 2 (registry rows)** | **29** Core `block_id` | Structural terms exist in vocabulary only (WF-R01.2 ACCEPTED charter) |
| **Post–WF-R01.2 Gate 2 (registry rows)** | **32** = 29 + HEADER_NAV + FILTERS + SEARCH | **Preferred denominator** for all WF-R01.3 REPORTs after T0 |
| **Post–vertical charters** | 32 + future ids | **Out of WF-R01.3.1 v1 scope** — no new IDs |

**Denominator policy (binding):**

- Always pair numerator with explicit denominator in REPORTs.
- After T0, **prefer 32** when structural Tier A is in program scope.
- **9/29 (~31%)** and **9/32 (~28%)** are both valid if denominator is declared — **never** mix denominators in one comparison without label.

### Coverage inequality (design invariant)

```text
RC ≥ RPC ≥ RSC (per page) ≥ SC (per site type)
```

**Page Coverage (PC)** is **orthogonal** — compositions may reach **100%** while RPC is **28%** (planning ahead of code).

### Reporting contract

Every WF-R01.3 wave REPORT **must** state **all five dimensions** — never infer Factory readiness from RC alone.

| Misclaim | Corrective |
|----------|------------|
| «29 blocks in registry» → «Factory-ready» | Cite **RPC** and **SC** |
| «Reference workspace exists» → «CATALOG-ready» | Cite **RSC** for `CATEGORY_PAGE` + structural **RPC** |
| «Blueprint ACCEPTED» → «Template-Art allowed» | Cite **SC** + WF-R01.7 matrix (when ACCEPTED) |
| «9/29 partials» without denominator | Declare **29 vs 32** explicitly |

### Curated library alignment

`curated-library-index-v1.md` tracks **9 rows** with **v0 snake_case** names — **RPC operational view only**, not full coverage truth. Curated-library v2 (v1 `block_id` sync) — **spec deferred** to WF-R01.3.X; **not** required for this charter ACCEPTED.

---

## Readiness Gates

Gates G0–G4 are **human-operated program milestones** for WF-R01.3. **Not** machine CI gates. **Not** auto-unlock for WF-A03 (see § WF-A03 Relationship).

**Standard denominator:** **32** = 29 Core + 3 structural Tier A (WF-R01.2 vocabulary).

### Gate table

| Gate | Name | RPC target | Primary deliverables | Unlocks |
|------|------|------------|----------------------|---------|
| **G0** | Baseline | **9/32** (~28%) | Documented baseline; golden slice; 9 existing partials | LANDING Template-Art **HITL pilot** only |
| **G1** | LANDING + shell | **14/32** (~44%) | BENEFITS, PROCESS, TESTIMONIALS split; HEADER_NAV, FOOTER, LEGAL_LINKS partials; structural registry rows (WF-R01.2 Gate 2 execution) | Honest global shell; LANDING completion |
| **G2** | PROMO + CATALOG scaffold | **20/32** (~63%) | SERVICES, TEAM, ABOUT; FILTERS, SEARCH, catalog grids; PLP scaffold; PROMO money-page scaffold | Template-Art **pilot** PROMO + CATALOG; **WF-A03 recommended precondition** |
| **G3** | ECOMMERCE + CORPORATE slice | **29/32** (~91%) | CART, CHECKOUT, PAYMENT, DELIVERY; PARTNERS, CERTIFICATES, MAP, FEATURES, REVIEWS | ECOMMERCE staging HITL; CORPORATE pilot |
| **G4** | Full Core reference | **32/32** (100%) | Remaining shell partials; scaffold coverage for primary page types; blueprint-instances for Core 5 | Full Core SC (excl. ECOMMERCE legal E1–E4) |

**Current program position:** **G0** (baseline) — repo fact at charter T0.

### Gate math rules

| Check | Rule |
|-------|------|
| Monotonic RPC | G0 < G1 < G2 < G3 < G4 numerators (32 denominator fixed) |
| G0 | **9/32 (~28%)** — not 31% unless denominator 29 explicitly declared |
| G1 | **14/32 (~44%)** — conservative vs wave sum ~15; **acceptable** |
| G2 | **20/32 (~63%)** — may trail wave sum ~22 if stub policy / parallelization; **acceptable** with explicit stub declaration |
| G3 | **29/32 (~91%)** — holds if overlaps (FOOTER etc.) not double-counted |
| G4 | **32/32** — co-dependent on WF-R01.2 Gate 2 registry rows **and** T1+ partials |

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
| Composition doc | Updated Reference Composition tables for new page types (**PC**) |
| SC checklist | Per-site-type Template-Art minimum (§ Template-Art minimum sets) |
| Five-dimension snapshot | RC, RPC, RSC, SC, PC in wave REPORT |

---

## Template-Art Minimum Reference Sets

Reference Layer **directly bounds** Template-Art honesty (WF-A01: IA + Block Registry = SSOT in `TEMPLATE_ART`).

### Interim policy (mandatory until G2)

Passport must state **«TEMPLATE_ART — LANDING scope only»** for undeclared multi-type attempts (WF-R01.7 interim; parent program).

### Minimum sets (Core 4 — operator checklist)

Sets = **T1+ partials** required **plus** **Reference Composition** published **plus** scaffolds for primary `page_type`. Structural blocks require WF-R01.2 registry rows before Template-Art claims on catalog surfaces.

#### LANDING

| Category | Required `block_id` / artifacts |
|----------|--------------------------------|
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

### Template-Art readiness matrix (coverage-derived)

| site_type_code | G0 (today) | After G1 | After G2 | After G4 |
|----------------|------------|----------|----------|----------|
| **LANDING** | **Allowed** (HITL) | **Allowed** | **Allowed** | **Allowed** |
| **PROMO** | **Blocked** | **Blocked** | **Pilot** | **Allowed** |
| **CATALOG** | **Blocked** | **Blocked** | **Pilot** | **Allowed** (HITL) |
| **CORPORATE** | **Blocked** | **Blocked** | **Blocked** | **Pilot** |
| **ECOMMERCE** | **Blocked** | **Blocked** | **Blocked** | **Pilot** (no legal E1–E4) |

**Note:** Final Template-Art policy authority consolidates in **WF-R01.7** when ACCEPTED; this matrix is **coverage-derived minimum** until R01.7 supersedes with explicit operator sign-off.

### Additional Template-Art prerequisites (non-reference, parallel)

| # | Requirement | Owner |
|---|-------------|-------|
| 1 | v0→v1 binding enforced | WF-R01.1 |
| 2 | Structural vocabulary → registry rows | WF-R01.2 Gate 2 |
| 3 | Commercial pattern catalog v0 | WF-R01.4 |
| 4 | SEO content formulas | WF-R01.5 |
| 5 | Wireframe artifact contract | Post-R01 / parallel |
| 6 | Design token doc bind (DG-01) | Parallel Priority B |

---

## Execution Case Feed Roles

Execution cases **feed** reference expansion **without** modifying case workspaces in this charter. Method: extraction discipline + lesson index (WF-R01.8).

| Case | Workspace / status | Reference knowledge (mineable) | WF-R01.3 routing | Anti-patterns |
|------|-------------------|-------------------------------|------------------|---------------|
| **Triumph** | `triumph-manipulator-landing-v6/` — highest live evidence | LANDING blocks; faq/pricing/cases extractions; `scroll_process_timeline`; RU QA preset; PROMO multi-page patterns; PROCESS, BENEFITS, TEAM candidates | **W1, W3** partials; **W2** nav minimal; **R01.4** pattern | **Do not** auto-canonicalize full v6 tree |
| **ISBD** | `isbd-care-landing/` — client #2 | Care vertical LANDING; lighter Factory binding; FEATURES, REVIEWS; adoption/freeze pattern | **W7** FEATURES, REVIEWS; adoption validation template | Not a catalog/manufacturer source |
| **BZPM** | No Factory workspace; OCPilot TEST live | CATALOG/manufacturer: filters, megamenu, PLP/PDP, faceted UX, industry taxonomy, HEADER_NAV depth | **W4–W5** structural + catalog vocabulary (**doc-first**); enrollment **pending** | OpenCart delivery **≠** Factory reference; vocabulary mining **HITL only** |
| **FP-0002** | `fp-0002-shpigovsky-frontend/` — PIXEL_PERFECT stress | VL3 domains, false-green, Group/Layout laws, asset collision — **negative evidence** | **Not** primary block source; informs QA adoption parallel track; boundary Template-Art vs PIXEL | **Do not** promote FP-0002 sections to reference partials without PIXEL→TEMPLATE scope change |

### Case suitability tiers

| Tier | Cases | Use in coverage model |
|------|-------|----------------------|
| **Primary drivers** | Triumph, BZPM (vocabulary), ISBD | Wave prioritization; extraction sources for RPC growth |
| **Parallel discipline** | FP-0002 | Validation adoption — **must not inflate RPC** |
| **Pending enrollment** | BZPM Factory workspace, Sibcar (OCPilot SITE-001) | Post–G2 decisions |

**FP-0002 explicit boundary:** FP-0002 **must not** inflate RPC. It informs **WF-A02 adoption** and **operator visual approval law** — reference expansion proceeds from **TEMPLATE_ART-aligned** sources.

---

## WF-A03 Relationship

### Authority chain (current)

```text
WF-A01  Production Modes           ✅ Complete
WF-A02  Validation Architecture    ✅ Complete (+ VL3)
WF-R01  Registry Expansion         ◆ CHARTERED (R01.1 ACCEPTED, R01.2 ACCEPTED)
WF-R01.3 Reference Expansion       ◆ DESIGN (R01.3.1 ACCEPTED — metrics only)
WF-A03  Pixel Factory Expansion    ⏸ DEFERRED
```

### G2 as recommended precondition

**Verdict (binding):** WF-R01.3 **G2 reached** (RPC ≥ **20/32**, catalog scaffold exists, structural partials T1+ per program design) is the **correct recommended precondition** for WF-A03 Pixel Factory charter pass — aligned with [roadmap.md](roadmap.md) § WF-A03 deferred marker and parent WF-R01 program design.

| # | WF-R01.3 outcome | Rationale |
|---|------------------|-----------|
| 1 | **G2 reached** | WF-A03 on catalog/manufacturer without reference = **false-green at pixel layer** |
| 2 | **R01.3.1 metrics charter ACCEPTED** | Pixel diff needs stable `data-block-id` reference baselines |
| 3 | **Structural partials T1+** (HEADER_NAV, FILTERS, SEARCH) | VL3 composition domains assume shell/catalog surfaces **exist** |
| 4 | **TEMPLATE_ART readiness matrix** (WF-R01.7) aligned with SC | Avoid Pixel Factory on undeclared multi-type scope |
| 5 | **Curated library v2 spec** published | Visual regression needs v1-id stable reference row names |
| 6 | **Web-GPT Research Pass** (operator reminder) | External refresh — **not** replaceable by WF-R01.3 |

**What G2 does not do:** G2 **does not** auto-start WF-A03. Roadmap: **auto-start forbidden**; explicit operator charter pass required. Operator **waiver below G2** is **discouraged** but documentable per roadmap.

### What WF-R01.3 does not block

| Work | Notes |
|------|-------|
| VL3 adoption on PIXEL_PERFECT greenfield | FP-0002 parallel track |
| WF-R01.4 / R01.5 documentation slices | Parallel |
| Client delivery (Triumph, ISBD, OCPilot) | Outside reference canon — explicit |
| WF-A03 with **operator waiver** | Discouraged; requires explicit waiver record |

---

## Upstream authority alignment

| Charter | Relationship |
|---------|--------------|
| **Foundry Vocabulary Canon** | F3 Block subtype informs structural denominator; REG-VOC-04 catalog ordering aligns with RSC/RPC dependencies |
| **WF-R01** parent program | M2 metric = **RPC**; this charter normativizes M2 measurement |
| **WF-R01.1** v0→v1 binding | RPC partials require v1 `block_id`; curated v0 names ≠ coverage truth |
| **WF-R01.2** structural blocks | Tier A terms in denominator 32; registry rows Gate 2 co-required for G1 catalog honesty |
| **WF-A01** production modes | SC gates Template-Art claims; orthogonal to coverage symbols |
| **WF-A02 / VL3** | Consumes reference baselines; does not define coverage dimensions |
| **WF-A03** | **DEFERRED**; G2 = recommended precondition only |

---

## Non-goals (this charter)

- No reference partial creation
- No registry row edits or new IDs
- No curated-library v2 implementation
- No WF-R01.3 wave execution
- No WF-A03 charter or implementation
- No OPERATIONAL-INDEX edit (separate implementation pass if required)

---

## Risks

| Risk | Severity | Mitigation in this charter |
|------|----------|----------------------------|
| False «Factory-ready» from registry alone | Critical | Five-dimension REPORT contract |
| TEMPLATE_ART on CATALOG before structural partials | Critical | G2 gate + LANDING-only interim |
| v0 snake_case in curated library during waves | Critical | RPC operational view labeled; v2 spec deferred to R01.3.X |
| Gate math confusion (29 vs 32) | Medium | Denominator policy § In-scope set evolution |
| Stub scaffolds counted as SC pass | Medium | RSC honesty rule — stub declaration mandatory |
| WF-A03 started before G2 | Medium | Recommended precondition + no auto-start |
| FP-0002 inflating RPC | Medium | Explicit exclusion in § Execution Case Feed |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| **FOUNDRY** as named product/path | **Not found** |
| **WF-R01.3 human owner / steward** | **Not fixed** in repo |
| **Exact page_type count** for RSC denominator | PAGE-TYPE-REGISTRY-v1 — **not counted** at charter T0 |
| **BREADCRUMBS / PAGINATION** as `block_id` vs layout-component | WF-R01.2 policy — operator decision **documented**; affects RPC numerator for W4 |
| **MEGA_MENU** separate `block_id` | WF-R01.2 — **variant** preferred |
| **BZPM W3 blueprint** delivery date | **UNKNOWN** |
| **OCPilot SITE-001** Factory binding | **Not verified** in audits |
| **Curated library v2** timeline | Spec only — R01.3.X |
| **WF-R01.7** ACCEPTED matrix vs this coverage-derived matrix | R01.7 **pending** — interim matrix binding until R01.7 ACCEPTED |

---

*Charter artifact: `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md`*
