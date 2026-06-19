# REPORT — FOUNDRY REGISTRY EXPANSION PROGRAM DESIGN

**Program ID:** WF-R01  
**Дата:** 2026-06-19  
**Режим:** проектирование программы — **без implementation**  
**База:** [foundry-registry-layer-audit-v1.md](foundry-registry-layer-audit-v1.md) · [foundry-system-wide-layer-audit-v1.md](foundry-system-wide-layer-audit-v1.md) · [foundry-capability-gap-audit-v1.md](foundry-capability-gap-audit-v1.md) · [roadmap.md](../projects/mars-website-factory/roadmap.md) · [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) · Foundation v1 stack (`workspaces/website-factory-reference-v1/`)

**Терминология:** строка **FOUNDRY** в репозитории **не найдена** как отдельный продукт или путь. В этом отчёте **FOUNDRY** = **Website Factory** — документированная human-operated методология + governance + ограниченный набор build workspaces. См. SAFE UNKNOWN.

**Honesty boundary:** WF-R01 — **documentation and reference-implementation program** (human-operated charters, registry hygiene, partial expansion). **Не** runtime, **не** orchestration, **не** agent automation, **не** machine-enforced validation.

---

## Executive Summary

WF-A01 (Production Modes) и WF-A02 (Validation Architecture + VL3 Domains) **завершены**. Три аудита (Registry Layer, System-Wide Layer, Capability Gap) **единогласно** фиксируют главный bottleneck FOUNDRY: **Registry Implementation Cliff** — канон v1 обещает больше, чем reference workspace и операционные артефакты могут собрать.

**Текущее состояние (факты из repo):**

| Показатель | Значение |
|------------|----------|
| Block Registry v1 `block_id` | **29** (ACCEPTED, documentation) |
| Reference partials | **9** (~**31%**) |
| Site Type Registry v1 | **8** типов (Core 5 + Extended 3) |
| Core Blueprints | **5/5** ACCEPTED |
| Commercial Pattern Library | **~1** documented pattern |
| SEO Architecture v2 | ACCEPTED; SEO Pattern Library (registries.md §4) — **absent** |
| Dual canon | v0 (snake_case, 10 site types, 16 blocks) vs v1 (UPPER_SNAKE, 8 types, 29 blocks) |
| Template-Art effective scope | **LANDING-only** (partial) |
| WF-A03 Pixel Factory | **DEFERRED** |

**Решение программы:** WF-R01 становится **следующим крупным направлением** FOUNDRY — **до** WF-A03. Цель — снять **composition truth gap**: один канонический namespace, structural blocks для catalog surfaces, расширение reference implementation, минимальные pattern/SEO slices, честная Template-Art multi-site-type policy.

**WF-R01 не заменяет** WF-A03. Pixel Factory остаётся **DEFERRED** до отдельного Web-GPT Research Pass и только когда primary bottleneck = **visual verification**, а не отсутствие block vocabulary.

---

## Program Scope

### Что входит в WF-R01

| Область | Содержание |
|---------|------------|
| **v0 → v1 Operational Binding** | Единый канон `site_type_code` / `block_id` для новых задач; mapping charter; banner policy на legacy v0 |
| **Registry v1.1 — Structural Blocks** | Charter для `HEADER_NAV`, `FILTERS`, `SEARCH`; policy для breadcrumbs, pagination, thank-you surfaces |
| **Block Registry hygiene** | Full BLOCK-CONTRACT на 29 entries; TRUST/TESTIMONIALS disposition; operator label → `block_id` map |
| **Reference Implementation Expansion** | Поэтапное наращивание partials в `website-factory-reference-v1/` (9 → 20 → 29+) |
| **Commercial Pattern Library v0** | Каталог `pattern_id` (documentation): lead-form-v1, rfq-v1, scroll_process_timeline, … |
| **SEO Content Pattern Slice** | Title/description formula templates per `page_type` — **documentation only**, без generation engine |
| **Blueprint Layer alignment** | Cross-links seo-architecture v2; human label → block_id; `project.blueprint.yaml` schema (doc) |
| **Site Type readiness notes** | Core 5 readiness matrix update; v0-only types → v1 composition rules |
| **Template-Art expansion charter** | LANDING-only → multi-site-type **policy** и preconditions |
| **Execution case vocabulary feed** | Triumph, ISBD, BZPM, FP-0002 → registry lessons index (documentation table) |
| **Success metrics & gates** | Измеримые критерии завершения подпрограмм |
| **Roadmap registration** | WF-R01 как WF-Axx-adjacent program item в roadmap (charter pass) |

### Что **не** входит в WF-R01

| Исключение | Обоснование | Куда отложено |
|------------|-------------|---------------|
| **Pixel Factory (WF-A03)** | Vision Layer, Visual Diff, Pixel QA Runtime, Screenshot Engine — **не закрывают** registry cliff | WF-A03 после Research Pass |
| **Vision Layer** | Visual verification automation | WF-A03 explicit non-goal until chartered |
| **Runtime Automation** | Phases 6–7 roadmap; MARS factory engine | Planned implementation — no repo evidence |
| **Agent Runtime** | 16/18 agents = planned; Control Plane routing | Не расширять agents до registry truth |
| **Machine-enforced validation / CI gates** | WF-A02 = documentation; automation = FUTURE | Отдельный charter post-WF-R01 |
| **ECOMMERCE Legal Extension E1–E4** | High for ecommerce go-live; не блокирует registry v1.1 | Charter при production intent ecommerce |
| **Extended Type Blueprints** (SAAS, MARKETPLACE, WEB_APPLICATION) | By design v1 out of Core | Per-type architecture charter |
| **Registry JSON Schema export** | Tooling readiness S5 boundary | Priority C — post WF-R01 core |
| **Design token kit / Figma/CSS export** | DG-01–04 OPEN; architecture-only DS | Parallel Priority B — не блокер R01.1–R01.3 |
| **Wireframe artifact contract v1** | Closes blueprint→design cliff for Template-Art | WF-R01 Phase 4 tail или post-R01 |
| **Strategy memo contract v1** | Upstream; LANDING ships без него | Priority B parallel |
| **MARS orchestration / artifact bus runtime** | Phase 4 doc only | Phases 6–7 |

### Граничные условия (explicit)

- WF-R01 работает **только** на уровне **human-operated** charters и **controlled** reference partial expansion.
- **Triumph v6** и другие live workspaces **не ретрофитятся** автоматически — только по explicit extraction/enrollment charter.
- **OCPilot / OpenCart** delivery paths **не мигрируют** в Factory canon без enrollment decision.
- **Не** создавать новую governance wave — targeted operational gaps per [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](../workspaces/website-factory-reference-v1/WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) discipline.

---

## Program Structure

WF-R01 декомпозируется на **8 подпрограмм** + **1 cross-cutting track** (metrics & enrollment).

```
WF-R01  FOUNDRY Registry Expansion Program
│
├── WF-R01.1  v0 → v1 Operational Binding Charter
├── WF-R01.2  Registry v1.1 — Structural Blocks
├── WF-R01.3  Reference Implementation Expansion
├── WF-R01.4  Commercial Pattern Library v0
├── WF-R01.5  SEO Content Pattern Slice
├── WF-R01.6  Blueprint & Registry Hygiene Pass
├── WF-R01.7  Template-Art Multi-Site-Type Charter
├── WF-R01.8  Execution Case → Registry Vocabulary Feed
└── WF-R01.X  Metrics, Gates & Roadmap Registration (cross-cutting)
```

### WF-R01.1 — v0 → v1 Operational Binding Charter

**Цель:** устранить drift XD-01 (Critical) — один namespace для новых задач.

**Deliverables (documentation):**

- Binding charter: v1 = canonical for `site_type_code`, `block_id`, Blueprint references
- v0 → v1 mapping table (best-effort composition rules; **не** claim 1:1 for all rows)
- Operator STOP rule: mixed IDs on v1 Blueprint = blocking defect
- Banner policy for v0 docs (Wave 4–6 ops: curated-library, block-quality-tiers, agent cards)
- Passport field guidance: cite v1 codes in new LOC-ZONE rows

**Dependency:** none (program entry gate)  
**Blocks:** все остальные подпрограммы (semantic foundation)

### WF-R01.2 — Registry v1.1 — Structural Blocks

**Цель:** закрыть OPEN gaps HEADER_NAV, FILTERS, SEARCH ([BLOCK-REGISTRY-GAPS-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-GAPS-v1.md) §2–3).

**Deliverables:**

- Registry v1.1 charter document (extends v1, **не** replaces)
- New `block_id` entries + BLOCK-CONTRACT rows
- SITE-TYPE-BLOCK-MATRIX-v3 (or v2.1 additive)
- PAGE-BLOCK-MAPPING updates for PLP/PDP/global shell
- Policy docs: BREADCRUMBS, PAGINATION (block_id vs layout-component decision)
- BLUEPRINT-BLOCK-MAPPING alignment for CATALOG, ECOMMERCE, CORPORATE

**Dependency:** WF-R01.1 (canonical namespace)  
**Unblocks:** CATALOG Template-Art honesty, BZPM vocabulary, manufacturer/auto surfaces

### WF-R01.3 — Reference Implementation Expansion

**Цель:** поднять reference partial coverage с **9/29** к поэтапным gate **20/29** → **29/29+** (29 Core + structural v1.1).

**Deliverables:**

- Reference expansion roadmap (ordered block list per wave)
- Partial HTML + SCSS in `website-factory-reference-v1/src/`
- Curated library index **v2** (v1 `block_id`, supersedes v0 naming in ops)
- Extraction reports per block (Wave discipline)
- TRUST vs TESTIMONIALS code disposition

**Dependency:** WF-R01.1; WF-R01.2 for structural partials  
**Parallel:** WF-R01.4, WF-R01.5 (documentation slices)

### WF-R01.4 — Commercial Pattern Library v0

**Цель:** оформить **отдельный** pattern_id catalog (не VF_* visual registry, не governance prose).

**Deliverables:**

- `commercial-pattern-library-v0.md` (or reference-v1/patterns/) with minimum set:
  - `scroll_process_timeline` (reuse existing doc)
  - `lead-form-v1`
  - `rfq-v1`
  - `sticky-cta-mobile-v1`
- Per-pattern: intent, copy_structure, ethical_constraints, interaction_model, analytics placeholder
- Cross-link to Blueprint `conversion_requirements`
- Update registries.md §3 honesty (1 pattern → catalog v0)

**Dependency:** WF-R01.1  
**Does not include:** A/B automation, analytics runtime

### WF-R01.5 — SEO Content Pattern Slice

**Цель:** закрыть gap «SEO Architecture strong / SEO content absent» без generation engine.

**Deliverables:**

- `seo-content-patterns-v0.md` — title/description/H1 **formula templates** per `page_type`
- Cross-link seo-architecture v2 as planning SSOT
- Faceted SEO addendum stub for CATALOG (FUTURE content charter pointer)
- Deprecate wording «SEO Pattern Library (planned)» in operational cross-links **via charter pass**

**Dependency:** WF-R01.1  
**Does not include:** meta generation, schema automation, keyword architecture engine

### WF-R01.6 — Blueprint & Registry Hygiene Pass

**Цель:** full BLOCK-CONTRACT on 29 entries; blueprint human labels → `block_id`; machine schema doc.

**Deliverables:**

- BLOCK-REGISTRY-v1 hygiene completion (26 abbreviated → full fields)
- Operator mapping table: Blueprint labels («Social proof») → TRUST / TESTIMONIALS
- `project.blueprint.yaml` format specification (documentation — BLUEPRINT-GAPS G6)
- BLOCK-REGISTRY-GAPS closure report for alignment chain

**Dependency:** WF-R01.1; benefits from WF-R01.2  
**Parallel with:** WF-R01.3 waves

### WF-R01.7 — Template-Art Multi-Site-Type Charter

**Цель:** formalize transition LANDING-only → multi-site-type **preconditions**.

**Deliverables:**

- Template-Art readiness matrix per Core 5 `site_type_code`
- Explicit **LANDING-only** interim policy until gates met
- Preconditions checklist: structural blocks + reference coverage % + pattern/SEO slices
- Passport `production_mode` + `site_type_code` binding rules for TEMPLATE_ART

**Dependency:** WF-R01.2, WF-R01.3 (minimum Phase 2 gates)  
**Consumer:** OCPilot Site-001 trajectory, new greenfield intake

### WF-R01.8 — Execution Case → Registry Vocabulary Feed

**Ц目标:** normalize project silos into registry vocabulary (documentation index).

**Deliverables:**

- `execution-case-registry-lessons-v1.md` — table: case × layer × block/pattern/lesson
- Enrollment recommendations: BZPM W3, FP-0002 LOC, Sibcar binding
- **No** automatic canon merge — HITL per row

**Dependency:** WF-R01.1  
**Feeds:** WF-R01.2, WF-R01.3 prioritization

---

## v0 → v1 Binding

### Объём проблемы

| Dimension | v0 (legacy) | v1 (canon) | Risk |
|-----------|-------------|------------|------|
| Site types | 10 (`landing`, `service_landing`, …) | 8 (`LANDING`, …) | No 1:1 mapping; geo/seo/ai types absent as v1 codes |
| Block IDs | 16 snake_case | 29 UPPER_SNAKE | Ops Wave 4–6 curated library uses v0 |
| Blueprints | page-blueprint-contract-v0 | reference-v1/blueprints/ | Workflow v0 cites v0 registries |
| Agent cards | site-type-registry-v0 refs | Should cite v1 | False compatibility in intake |
| SEO | «SEO Pattern Library planned» | seo-architecture v2 ACCEPTED | Stale cross-links |

**Affected surfaces (confirmed in audits):**

- `curated-library-index-v1.md`, `block-quality-tiers-v1.md`
- `website-factory-workflow-v0.md`, `page-blueprint-contract-v0.md`
- Agent cards under `agents/cards/`
- `registries.md` §3–§4 wording
- Triumph case artifacts (`page-blueprint-v0.md`)

### Приоритет

**Priority A — program entry gate (WF-R01.1).** Без binding любое расширение registry **умножает** drift.

### Критерии завершения WF-R01.1

| # | Criterion | Verification |
|---|-----------|--------------|
| B1 | Binding charter **ACCEPTED** (human sign-off) | Charter doc in repo |
| B2 | v0→v1 mapping table published | Covers all 10 v0 site types + 16 v0 blocks |
| B3 | STOP rule in OPERATIONAL-INDEX Core Run row | Operator-visible |
| B4 | New task template cites v1 only | Onboarding / passport guidance |
| B5 | Banner on v0 registries: «legacy — do not use for new work» | v0 files unchanged except banner **via charter pass** |
| B6 | Zero **new** artifacts using v0 IDs post-cutover date | REPORT audit on pilot projects |

**Explicit non-goals for R01.1:** mass retrofit Triumph v6; delete v0 files; automated ID linter.

### v0-only site type composition rules (design direction)

| v0 type | v1 composition (proposed) | Status |
|---------|---------------------------|--------|
| `landing` | `LANDING` | Direct |
| `service_landing` | `LANDING` or `PROMO` (HITL) | Composition rule |
| `promo_site` | `PROMO` | Direct |
| `corporate_site` | `CORPORATE` | Direct |
| `catalog_site` | `CATALOG` | Direct |
| `ecommerce` | `ECOMMERCE` | Direct |
| `geo_landing` | `LANDING` + geo SEO notes | Extended composition |
| `seo_landing` | `LANDING` or `PROMO` + SEO program notes | Extended composition |
| `ai_visibility_page` | `LANDING` + content program notes | Extended composition |
| `hybrid_commercial` | Multi `site_type_code` per route group | CORPORATE charter pattern |

---

## Registry Expansion

### Site Type Registry

**Current:** 8 types ACCEPTED; Core 5 production targets; Extended 3 concept-only.

| Phase | Work | Outcome |
|-------|------|---------|
| R01-P1 | Binding + readiness matrix refresh | Honest Core 5 labels: LANDING **Ready (doc+ref)**; others **Partial** |
| R01-P2 | v0 composition rules documented | geo/seo/service types mappable without new v1 codes |
| R01-P3 | Manufacturer / Auto **vertical profiles** (documentation) | **Not** new site_type — CATALOG+CORPORATE + vertical notes |
| R01-P4 | Extended type touch-only | SAAS/MARKETPLACE — classification unchanged; **out of scope** |

**Not in WF-R01:** adding 9th Core type for Manufacturer or Auto (requires separate registry charter).

### Block Registry

**Current:** 29 Core `block_id`; ~31% reference coverage; structural gaps OPEN.

| Phase | Work | Target count |
|-------|------|--------------|
| R01-P1 | Hygiene — full BLOCK-CONTRACT | 29 entries complete |
| R01-P2 | v1.1 structural blocks | +3 minimum (`HEADER_NAV`, `FILTERS`, `SEARCH`); +policy for breadcrumbs/pagination |
| R01-P3 | Matrix v2.1/v3 | All blocks × Core 5 updated |
| R01-P4 | Reference partials | 9 → 20 → 29+ |

**Priority block waves for reference (ordered):**

1. **LANDING completion:** BENEFITS, PROCESS, CTA variants clarity  
2. **PROMO money-page:** SERVICES, TEAM, ABOUT, TESTIMONIALS split  
3. **CATALOG corridor:** CATEGORIES, CATEGORY_GRID, PRODUCT_GRID, PRODUCT_CARD + structural  
4. **ECOMMERCE chain:** CART, CHECKOUT, PAYMENT, DELIVERY (registry exists; partials lag)  
5. **CORPORATE trust:** PARTNERS, CERTIFICATES, MAP  
6. **Shell:** FOOTER, LEGAL_LINKS explicit partials  

### Commercial Pattern Library

| Phase | Deliverable |
|-------|-------------|
| R01-P1 | Pattern catalog v0 file + registries.md honesty fix |
| R01-P2 | Blueprint G5 closure — pattern_id ↔ conversion_requirements map |
| R01-P3 | RFQ vs LEAD_FORM variant policy (same block_id vs pattern split) |

**Boundary:** VF_* in VISUAL-PATTERN-REGISTRY remains **design architecture**, not Commercial Pattern Library.

### SEO Pattern Layer

| Layer | Status | WF-R01 action |
|-------|--------|---------------|
| SEO Architecture v2 | ACCEPTED | Cross-link as SSOT; no duplicate library |
| SEO Pattern Library (registries.md) | Absent | **Replace** with seo-content-patterns-v0 slice |
| Title/meta/schema templates | Absent | Formula templates per page_type |
| Faceted SEO | FUTURE | Stub + pointer in CATALOG blueprint notes |

### Blueprint Layer

| Phase | Work |
|-------|------|
| R01-P1 | Human label → block_id operator map |
| R01-P2 | BLUEPRINT-BLOCK-MAPPING update for v1.1 blocks |
| R01-P3 | `project.blueprint.yaml` schema (doc) |
| R01-P4 | ECOMMERCE utility pages alignment (cart/checkout in PAGE-TYPE scope) |

**Extended type blueprints:** explicitly **deferred** beyond WF-R01.

---

## Structural Blocks

### Анализ необходимости

Blueprints и PAGE-ARCHITECTURE **требуют** global/catalog structural surfaces, но Core 29 **не содержит** соответствующих `block_id` ([BLOCK-GAPS-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md)).

| Class | Proposed `block_id` | Required by | WF-R01 action |
|-------|-------------------|-------------|---------------|
| **HEADER_NAV** | `HEADER_NAV` | All Core 5 blueprints (global shell) | **Charter v1.1 — Required** |
| **FILTERS** | `FILTERS` | CATALOG, ECOMMERCE PLP | **Charter v1.1 — Required** |
| **SEARCH** | `SEARCH` | CATALOG, ECOMMERCE, CORPORATE (large IA) | **Charter v1.1 — Required** |
| **BREADCRUMBS** | `BREADCRUMBS` or layout policy | CATALOG, ECOMMERCE, CORPORATE | Policy decision in v1.1 — block_id vs layout component |
| **PAGINATION** | `PAGINATION` | PLP, REVIEWS | Policy decision — likely block_id for PLP |
| **CATALOG SURFACES** | CATEGORIES, CATEGORY_GRID, PRODUCT_GRID, PRODUCT_CARD | CATALOG, ECOMMERCE | Registry **exists** — reference partials **missing** (R01.3) |
| **MANUFACTURER SURFACES** | No dedicated id | BZPM proxy | Compose: CATALOG + CORPORATE + `rfq-v1` pattern + spec-table **future** |
| **CORPORATE SURFACES** | ABOUT, TEAM, PARTNERS, SERVICES | CORPORATE, PROMO | Registry exists — partials missing |
| **AUTO SURFACES** | No vertical site_type | Sibcar / OCPilot | Map to CATALOG + filters + PDP; vertical profile doc only |
| **THANK_YOU** | `THANK_YOU` or page_type-only | LANDING, ECOMMERCE conversion | v1.1 policy — post-checkout / post-lead |
| **MEGA_MENU** | Sub-variant of HEADER_NAV? | BZPM megamenu evidence | **Operator decision** — variant vs separate id |
| **SPEC_TABLE** | Future | Manufacturer B2B | **Post-R01** — catalog vertical charter |
| **DEALER_LOCATOR** | Future | Auto | **Post-R01** — auto vertical charter |

### Surface class → site type readiness (post-R01 target)

| Surface class | LANDING | PROMO | CATALOG | ECOMMERCE | CORPORATE |
|---------------|---------|-------|---------|-----------|-----------|
| HEADER_NAV | Optional/minimal | Required | Required | Required | Required |
| FILTERS | FORBIDDEN | FORBIDDEN | Required | Required | Optional (catalog subtree) |
| SEARCH | FORBIDDEN | Optional | Required | Required | Optional |
| CATALOG grid/card | FORBIDDEN | FORBIDDEN | Required | Required | Optional |
| CORPORATE about/team | FORBIDDEN | Optional | FORBIDDEN | FORBIDDEN | Required |

**Verdict:** WF-R01.2 **обязателен** для честного CATALOG/CORPORATE/Manufacturer/Auto **Factory vocabulary**; без него Template-Art на catalog = **false completeness**.

---

## Reference Implementation Strategy

### Baseline

| Metric | Current | Source |
|--------|---------|--------|
| Registry `block_id` | 29 | BLOCK-REGISTRY-v1 |
| Reference partials | 9 | `src/partials/sections/` |
| Coverage | **31%** | Registry Layer Audit |
| Implemented | hero, social_proof, pricing, lead_form, cta_band, contact_block, sticky_cta, faq, cases | repo |
| Structural | 0 | BLOCK-GAPS |

### Target trajectory

```
Gate 0 (today)     9 / 29   (~31%)  LANDING subset battle-tested
Gate 1 (R01-P2)   14 / 32  (~44%)  + structural v1.1 + LANDING completion (BENEFITS, PROCESS)
Gate 2 (R01-P3)   20 / 32  (~63%)  + PROMO money-page + CATALOG scaffold
Gate 3 (R01-P4)   29 / 32  (~91%)  + ECOMMERCE chain + CORPORATE slice
Gate 4 (R01-P5)   32 / 32  (100%)  + remaining shell explicit partials
```

*Denominator 32 = 29 Core + 3 structural v1.1.*

### Wave plan (WF-R01.3)

| Wave | Blocks | Site type focus | Evidence source |
|------|--------|-----------------|-----------------|
| **W1** | BENEFITS, PROCESS, TESTIMONIALS (split from TRUST) | LANDING | Triumph extractions |
| **W2** | HEADER_NAV, FOOTER, LEGAL_LINKS | Global shell | reference-v1 layout + BZPM nav patterns (doc) |
| **W3** | SERVICES, TEAM, ABOUT | PROMO | Triumph multi-page |
| **W4** | FILTERS, SEARCH, BREADCRUMBS, PAGINATION | CATALOG | BZPM audit vocabulary |
| **W5** | CATEGORIES, CATEGORY_GRID, PRODUCT_GRID, PRODUCT_CARD | CATALOG | BZPM + reference scaffold |
| **W6** | CART, CHECKOUT, PAYMENT, DELIVERY | ECOMMERCE | Blueprint chain only (staging HITL) |
| **W7** | FEATURES, REVIEWS, CERTIFICATES, PARTNERS, MAP | Mixed | ISBD / CORPORATE |

### Quality tiers (reuse block-quality-tiers discipline)

| Tier | Meaning | Gate |
|------|---------|------|
| **T0** | Registry-only | Documentation |
| **T1** | Reference partial + build pass | reference-v1 npm run build |
| **T2** | Curated library + extraction report | Wave 6 discipline |
| **T3** | Battle-tested in client workspace | Triumph/ISBD/BZPM enrollment |

**Rule:** no block promoted to T3 without WF-R01.1 v1 `block_id`.

### TRUST / TESTIMONIALS disposition

- **Option A (recommended):** split partials; `social_proof.html` → TRUST; new `testimonials.html`
- **Option B:** single partial with documented variant map  
Decision gate: WF-R01.6 hygiene pass sign-off.

---

## Template-Art Expansion

### Current state

Per WF-A01: `TEMPLATE_ART` — IA + Block Registry = SSOT; visual from Factory foundations.

**Effective reality (Capability Audit):** **LANDING-only** — 9 partials, no structural blocks, design tokens DG-01–04 OPEN.

### Transition requirements: LANDING-only → multi-site-type

| # | Requirement | Subprogram |
|---|-------------|------------|
| 1 | v0→v1 binding enforced | R01.1 |
| 2 | Structural blocks in registry | R01.2 |
| 3 | Reference coverage ≥ **63%** (Gate 2) for PROMO/CATALOG scaffolds | R01.3 |
| 4 | Template-Art readiness matrix **ACCEPTED** | R01.7 |
| 5 | Commercial pattern catalog v0 for conversion surfaces | R01.4 |
| 6 | SEO content formulas for page types in scope | R01.5 |
| 7 | Explicit passport: `production_mode=TEMPLATE_ART` + `site_type_code` | WF-A01 (existing) |
| 8 | Wireframe artifact contract (markdown section map) | **Post-R01 Phase 4** or parallel |
| 9 | Design token documentation bind (DG-01) | Parallel Priority B |

### Readiness matrix (target)

| site_type_code | Today | After WF-R01 Gate 2 | After WF-R01 Gate 4 |
|----------------|-------|---------------------|---------------------|
| `LANDING` | **Allowed** (HITL) | **Allowed** | **Allowed** |
| `PROMO` | **Blocked** | **Pilot** (HITL) | **Allowed** |
| `CATALOG` | **Blocked** | **Pilot** (scaffold) | **Allowed** (HITL) |
| `ECOMMERCE` | **Blocked** | **Blocked** | **Pilot** (no legal E1–E4) |
| `CORPORATE` | **Blocked** | **Blocked** | **Pilot** |

**Interim policy (mandatory until Gate 2):** passport must state **«TEMPLATE_ART — LANDING scope only»** for undeclared multi-type attempts.

---

## Execution Case Usage

### Case inventory

| Case | Workspace / status | Primary vocabulary contribution | WF-R01 fit |
|------|-------------------|--------------------------------|------------|
| **Triumph** | `triumph-manipulator-landing-v6/` — highest live evidence | LANDING blocks, faq/pricing/cases extractions, `scroll_process_timeline`, RU QA preset, PROMO multi-page patterns | **R01.3 W1, W3** — reference extractions; **R01.4** pattern reuse; **not** auto-canonicalize v6 without enrollment |
| **ISBD** | `isbd-care-landing/` — client #2 | LANDING care vertical, adoption/freeze pattern, lighter Factory binding | **R01.3 W7** — FEATURES/REVIEWS; adoption validation template |
| **BZPM** | No Factory workspace; OCPilot TEST live | CATALOG/manufacturer: filters, megamenu, PLP/PDP, faceted UX, industry taxonomy | **R01.2, R01.3 W4–W5** — structural + catalog vocabulary; **R01.8** lesson feed; W3 blueprint **pending** |
| **FP-0002** | `fp-0002-shpigovsky-frontend/` — PIXEL_PERFECT stress | VL3 domains, false-green, Group/Layout laws, **negative evidence** | **Parallel track** — VL3 adoption (**not** registry expansion); informs **R01.7** (Template-Art vs PIXEL boundary); **not** primary block source |
| **FP-0001** | LOC-ZONE enrolled | MOC/SOC substrate, partial Factory track closeout | **R01.8** operations vocabulary |
| **OCPilot SITE-001 (Sibcar)** | Auto dealer TEST — **not verified** in audits | Auto/catalog CSS-only direction, PDP stabilization | **R01.8** auto vertical profile; enrollment decision post-R01.2 |

### Case → subprogram routing

| Subprogram | Primary cases | Secondary |
|------------|---------------|-----------|
| R01.1 Binding | All — STOP on mixed IDs in new work | FP-0002 (document v0 artifacts risk) |
| R01.2 Structural | BZPM, Sibcar | Triumph (minimal nav) |
| R01.3 Reference | Triumph, ISBD | BZPM (PLP patterns as **doc** reference) |
| R01.4 Commercial | Triumph (`scroll_process_timeline`) | BZPM (RFQ flows) |
| R01.5 SEO | Triumph RU preset | BZPM catalog SEO notes |
| R01.7 Template-Art | OCPilot Site-001 trajectory | ISBD |
| R01.8 Lessons index | All six rows | — |

### Cases **not** suitable as WF-R01 primary drivers

- **FP-0002** — PIXEL_PERFECT forensic; use for validation discipline, **not** block registry SSOT
- **BZPM live OpenCart** — delivery evidence **≠** Factory reference; vocabulary mining only with HITL
- **Triumph v6 full tree** — client authority parallel to FP-0001; selective extraction only

---

## Success Metrics

### Primary metrics

| Metric ID | Name | Baseline | Gate 2 target | Gate 4 target | Measurement |
|-----------|------|----------|---------------|---------------|-------------|
| **M1** | Registry block coverage (doc) | 29/29 defined | 32/32 with v1.1 | 32/32 full CONTRACT | BLOCK-REGISTRY audit |
| **M2** | Reference partial coverage | 9/29 (31%) | 20/32 (63%) | 32/32 (100%) | Count `src/partials/sections/` |
| **M3** | Structural block presence | 0/3 | 3/3 chartered + partial | 3/3 T1+ | BLOCK-REGISTRY v1.1 |
| **M4** | v0 drift incidents (new work) | Unmeasured | 0 post-cutover | 0 | REPORT audit / passport review |
| **M5** | Commercial pattern catalog | 1 | ≥4 pattern_id | ≥6 pattern_id | Pattern library file |
| **M6** | SEO content formulas | 0 page types | ≥6 page types | 10 page types | seo-content-patterns-v0 |
| **M7** | Core site type Template-Art readiness | 1/5 (LANDING partial) | 2/5 (LANDING+PROMO pilot) | 4/5 (excl. ECOMMERCE legal) | R01.7 matrix |
| **M8** | Blueprint hygiene | PARTIAL labels | Operator map complete | project.blueprint.yaml doc | R01.6 sign-off |
| **M9** | Execution case lesson index | 0 | 1 table ≥4 cases | Closed loop enrollment | R01.8 doc |
| **M10** | Curated library v1 id drift | v0 names | v2 v1 ids published | Sync with reference | curated-library-index |

### Secondary metrics (monitoring)

| Metric | Purpose |
|--------|---------|
| Reference workspace build success | npm run build after each wave |
| BLOCK-REGISTRY-GAPS OPEN count | Trend to zero for in-scope gaps |
| FALSE «registry complete» REPORT flags | Operator discipline |
| VL3 adoption on new PIXEL greenfield | Parallel WF-A02 — not R01 core |

### Program completion criteria (WF-R01 exit)

WF-R01 considered **Complete** when **all** true:

1. WF-R01.1 binding charter **ACCEPTED** + B6 zero new v0 IDs  
2. WF-R01.2 structural blocks **ACCEPTED** in registry v1.1  
3. **M2 ≥ 63%** (Gate 2) **and** catalog scaffold partials exist  
4. WF-R01.4 pattern catalog v0 **published** (≥4 patterns)  
5. WF-R01.5 SEO content slice **published** (≥6 page types)  
6. WF-R01.7 Template-Art readiness matrix **ACCEPTED**  
7. WF-R01.8 lesson index **published**  
8. Roadmap updated with WF-R01 **Complete** + WF-A03 preconditions re-evaluated  

**Not required for R01 exit:** WF-A03 start; 100% reference coverage (Gate 4 may continue as WF-R01.3 maintenance); ECOMMERCE legal extension.

---

## Roadmap Position

### Current WF-Axx chain

```
WF-A01  Production Modes Contract     ✅ Complete (2026-06-17)
WF-A02  Validation Architecture       ✅ Complete (2026-06-17/18)
        + VL3 Domains Pass 02
WF-A03  Pixel Factory Expansion       ⏸ DEFERRED (Research Pass required)
```

### Proposed chain

```
WF-A02  Validation Architecture       ✅ Complete
   ↓
WF-R01  Registry Expansion Program    ◄── NEXT (this program)
   ↓
[Parallel] VL3 adoption discipline     ◄── FP-0002 lessons; not blocked on R01
   ↓
WF-A03  Pixel Factory Expansion       ⏸ DEFERRED until:
        • WF-R01 Gate 2+ achieved OR explicit operator waiver
        • Web-GPT Research Pass complete
        • Primary bottleneck = visual verification (PIXEL_PERFECT portfolio)
   ↓
[Future] WF-A04? Blueprint Machine Layer / Agent operationalization  — SAFE UNKNOWN naming
   ↓
Phases 6–7  Runtime / automation       — blocked on MARS runtime evidence
```

### Positioning vs roadmap phases 0–7

| Roadmap phase | Relationship to WF-R01 |
|---------------|------------------------|
| Phase 1 Registries v0 | **Superseded partially** — R01.1 binding clarifies v1 canon |
| Phase 5 Cursor-assisted production | **Enabled** by reference expansion |
| Phase 6–7 Runtime/automation | **Not started** — R01 explicitly excludes |

### Recommended roadmap.md addition (charter pass — not in this task)

| ID | Name | Status | Precondition |
|----|------|--------|--------------|
| **WF-R01** | Registry Expansion Program | **Proposed → Active** | WF-A01 + WF-A02 complete |
| **WF-A03** | Pixel Factory Expansion | **DEFERRED** | WF-R01 Gate 2+ **recommended** |

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| False «registry complete» after ACCEPTED labels | **Critical** | M2 reference coverage in every REPORT; capability audit vocabulary |
| v0 ID creep during R01 waves | **Critical** | R01.1 STOP rule; curated library v2 |
| TEMPLATE_ART on CATALOG before structural blocks | **Critical** | R01.7 interim LANDING-only policy |
| BZPM/Sibcar lessons never enter canon | **High** | R01.8 lesson index + enrollment charter |
| Reference expansion without build validation | **High** | npm run build gate per wave |
| Registry v1.1 scope creep (mega_menu, spec_table, …) | **Medium** | v1.1 = 3 structural + policy only; vertical ids post-R01 |
| Triumph v6 mistaken as full PROMO reference | **Medium** | Explicit extraction scope in R01.3 waves |
| WF-A03 started early | **Medium** | Roadmap DEFERRED marker + R01 exit criteria |
| Governance bloat from 8 subprograms | **Medium** | OPERATIONAL-INDEX single Core Run row for R01 |
| ECOMMERCE pilot before Legal E1–E4 | **High** | Staging-only HITL; not R01 exit requirement |
| Operator COMPLETE gate never signed | **Low** | Timeboxed phases with REPORT closeout |

---

## SAFE UNKNOWN

- **FOUNDRY** как именованный продукт/путь — **не обнаружен**; программа относится к Website Factory ecosystem.
- Единый **owner** WF-R01 (human) — **не зафиксирован** в прочитанных документах.
- **OCPilot SITE-001** `production_mode` и v1 binding — **не verified**.
- **BZPM W3 blueprint** delivery date — **UNKNOWN**.
- **VL3 adoption rate** Triumph v6 / ISBD — **не аудирован**.
- **BREADCRUMBS / PAGINATION** — block_id vs layout-component — **operator decision pending**.
- **MEGA_MENU** — variant of HEADER_NAV vs separate id — **operator decision pending**.
- **Manufacturer / Auto** as future Extended `site_type_code` vs composition — **undecided**.
- **Registry JSON Schema** timeline — **not defined**.
- **WF-A04+** naming for Blueprint Machine Layer — **SAFE UNKNOWN**.
- Revenue/throughput metrics — **no evidence** in repo.
- Whether **Knowledge Center** mirror is fresh — **UNKNOWN** (out-of-git).

---

## Recommended WF-R01 Sequence

### Phase 1 — Registry truth & binding (Months 1–2)

**Goal:** stop drift; establish honest vocabulary.

| Step | Subprogram | Deliverables |
|------|------------|--------------|
| 1.1 | **R01.1** | v0→v1 binding charter ACCEPTED |
| 1.2 | **R01.6** (partial) | Operator label → block_id map; v0 banners policy |
| 1.3 | **R01.7** (interim) | LANDING-only Template-Art policy published |
| 1.4 | **R01.8** (kickoff) | Execution case lesson index v0.1 |
| 1.5 | **R01.X** | Metrics baseline recorded (M1–M10) |

**Exit gate:** B1–B6 satisfied; zero new v0 IDs on pilot intake.

---

### Phase 2 — Structural registry & LANDING completion (Months 2–3)

**Goal:** v1.1 structural blocks + LANDING reference completeness.

| Step | Subprogram | Deliverables |
|------|------------|--------------|
| 2.1 | **R01.2** | HEADER_NAV, FILTERS, SEARCH chartered |
| 2.2 | **R01.3 W1–W2** | BENEFITS, PROCESS, shell partials |
| 2.3 | **R01.4** | Commercial pattern catalog v0 (≥4 patterns) |
| 2.4 | **R01.5** | SEO content formulas (≥6 page types) |
| 2.5 | **R01.6** | BLOCK-CONTRACT hygiene on 29 entries |

**Exit gate:** M3 = 3/3; M2 ≥ 44%; structural blocks in matrix.

---

### Phase 3 — PROMO + CATALOG scaffold (Months 3–5)

**Goal:** Gate 2 reference coverage; catalog vocabulary honest.

| Step | Subprogram | Deliverables |
|------|------------|--------------|
| 3.1 | **R01.3 W3–W5** | PROMO + CATALOG partials |
| 3.2 | **R01.7** (update) | Template-Art readiness matrix — PROMO/CATALOG pilot |
| 3.3 | **R01.8** | BZPM + Triumph lessons merged |
| 3.4 | **R01.6** | BLUEPRINT-BLOCK-MAPPING v1.1 alignment |
| 3.5 | **Parallel** | VL3 mandatory on new PIXEL_PERFECT (WF-A02) |

**Exit gate:** M2 ≥ 63%; M7 ≥ 2/5 site types pilot-ready.

---

### Phase 4 — ECOMMERCE + CORPORATE depth & program close (Months 5–8)

**Goal:** Gate 4 coverage; WF-R01 exit; WF-A03 re-evaluation.

| Step | Subprogram | Deliverables |
|------|------------|--------------|
| 4.1 | **R01.3 W6–W7** | ECOMMERCE chain + CORPORATE slice partials |
| 4.2 | **R01.6** | `project.blueprint.yaml` schema doc |
| 4.3 | **R01.7** (final) | Template-Art matrix Gate 4 |
| 4.4 | **R01.8** | FP-0002 / Sibcar enrollment decisions documented |
| 4.5 | **R01.X** | WF-R01 completion REPORT; WF-A03 precondition review |
| 4.6 | **Optional** | Wireframe artifact contract v1 (if Template-Art demand) |

**Exit gate:** WF-R01 exit criteria (§ Success Metrics) met; roadmap WF-A03 note updated.

---

**STOP AFTER REPORT — NO IMPLEMENTATION — NO DOCUMENT CHANGES (кроме этого артефакта)**

---

*Program design artifact: `reports/foundry-registry-expansion-program-design-v1.md`*  
*Evidence: foundry-registry-layer-audit-v1.md, foundry-system-wide-layer-audit-v1.md, foundry-capability-gap-audit-v1.md, website-factory-reference-v1 foundation stack, mars-website-factory OPERATIONAL-INDEX + roadmap + WF-A01/A02 charters.*
