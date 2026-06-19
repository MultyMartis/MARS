# REPORT — FOUNDRY VOCABULARY CANON CHARTER DESIGN

**Artifact ID:** Foundry Vocabulary Canon Charter — design pass (v1 target)  
**Date:** 2026-06-19  
**Mode:** charter **design only** — **no publication**, **no acceptance**, **no registry edits**, **no new IDs**  
**Parent program:** WF-R01.0 — Research Canon Integration · WF-R01 — FOUNDRY Registry Expansion Program (**CHARTERED**)

**Research inputs:**

| ID | Artifact |
|----|----------|
| RV-01 | [research/foundry/rv-01-production-vocabulary.md](../research/foundry/rv-01-production-vocabulary.md) |
| RV-02 | [research/foundry/rv-02-website-production-systems.md](../research/foundry/rv-02-website-production-systems.md) |
| RV-03 | [research/foundry/rv-03-pixel-factory.md](../research/foundry/rv-03-pixel-factory.md) |

**Authority context:** [wf-r01-0-research-canon-integration-design-v1.md](wf-r01-0-research-canon-integration-design-v1.md) · [wf-r01-registry-expansion-program-charter-v1.md](wf-r01-registry-expansion-program-charter-v1.md) · [wf-r01-1-v0-v1-binding-charter-v1.md](wf-r01-1-v0-v1-binding-charter-v1.md) · [wf-r01-2-structural-blocks-program-design-v1.md](wf-r01-2-structural-blocks-program-design-v1.md) · WF-A01/A02 charters · [projects/mars-website-factory/OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) · [projects/mars-website-factory/roadmap.md](../projects/mars-website-factory/roadmap.md)

**Honesty boundary:** этот документ — **design target** для будущего `foundry-vocabulary-canon-charter-v1.md`. **Не** runtime, **не** registry content, **не** charter amendment в силе.

**Терминология:** **FOUNDRY** = **Website Factory** ecosystem (строка FOUNDRY как отдельный продукт/путь в repo **не найдена**).

---

## Executive Summary

WF-R01.0 выявил критический разрыв: между **Research Canon** (RV-01–03) и **Registry** (SITE-TYPE, PAGE-TYPE, BLOCK, pattern libraries) отсутствует нормативный промежуточный слой — **Foundry Vocabulary Canon**. Без него операторы и агенты рискуют смешивать уровни абстракции (site type vs page type vs block vs pattern vs SEO tactic), принимать audit-proxy за industry evidence и продвигать research rows в registry без tiering.

**Цель design pass:** определить **семейства vocabulary**, их границы, модель связей, authority chain и ограничения на будущие registry — **без** создания `block_id`, `site_type_code`, `page_type` rows и **без** публикации charter.

**Главный вывод:** канон FOUNDRY должен содержать **шесть фундаментальных registry-aligned families** плюс **два внутрисемейных подтипа Block** и **глоссарий disambiguation**. Рекомендуемая иерархия (не линейная pipeline, а **constraint graph**):

```text
Site Type ──constrains──► Page Type ──composes──► Block (structural | content)
                              │                        │
                              │                        ├── Commercial Pattern (overlay)
                              │                        └── Trust Pattern (overlay)
                              └── maps to ──► SEO Surface (intent class; ≠ SERP tactic)
```

**Шесть families (Tier A — must adopt в charter):**

| # | Family | Registry home (existing/planned) | Canon role |
|---|--------|----------------------------------|------------|
| F1 | **Site Type** | SITE-TYPE-REGISTRY-v1 | Класс сайта / бизнес-модель |
| F2 | **Page Type** | PAGE-TYPE-REGISTRY-v1 | Класс URL / IA-роль |
| F3 | **Block** | BLOCK-REGISTRY-v1 | Переиспользуемая секция страницы |
| F4 | **Commercial Pattern** | Commercial Pattern Library | Композиционный коммерческий нарратив |
| F5 | **Trust Pattern** | Trust semantics + future catalog | Доказательный стек доверия |
| F6 | **SEO Surface** | seo-architecture v2 + PAGE-SEO contracts | Класс поисковой/контентной поверхности |

**Дополнительно (не families, но обязательный glossary в charter):** `structural_block` vs `content_block`; `page_reality` vs `serp_reality`; `minimal_canon` vs `expansion_backlog`; maturity attribute `standard | common | specialized | obsolete`.

**Authority flow (target):** Research → (WF-R01.0 tiering) → **Vocabulary Canon Charter** → subprogram charters (WF-R01.x) → Registry rows / Blueprint instances → Operational usage.

**Следующий шаг:** human review design → отдельный charter pass → `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` (Tier A rules only, zero registry rows).

---

## Vocabulary Families

### Sufficiency check

RV-01 фиксирует рыночные уровни: site type, page type, content/listing type, section/block/component, commercial pattern, trust pattern, SEO surface. RV-02 добавляет production-stack layers (tokens, components, templates, content models) — **не** vocabulary families, а **reference architecture** (Tier B). RV-03 описывает delivery pipeline — **вне** vocabulary canon.

| RV-01 level | FOUNDRY family | Verdict |
|-------------|----------------|---------|
| Site type | F1 Site Type | **Adopt** |
| Page type | F2 Page Type | **Adopt** |
| Content/listing type | F2 Page Type (+ glossary note) | **Absorb** — listing/detail различие через page type, не отдельное family |
| Section/block/component | F3 Block (+ glossary) | **Adopt** Block; component = implementation layer (glossary) |
| Commercial pattern | F4 Commercial Pattern | **Adopt** |
| Trust pattern | F5 Trust Pattern | **Adopt** |
| SEO surface | F6 SEO Surface | **Adopt** |

**Не включать как families (glossary / Reference Library only):**

| Term | Reason |
|------|--------|
| Production Mode (`PIXEL_PERFECT` / `TEMPLATE_ART`) | Orthogonal fidelity contract — **WF-A01 canon**, не vocabulary family |
| Blueprint | **Instance artifact**, не vocabulary term |
| Template / Layout Template | Display scaffold — maps to Blueprint + page architecture |
| Component (code) | Developer primitive — RV-02 stack layer |
| Design Token | Design-system layer — architecture doc, не registry family |
| Content Model / Entity | Post–WF-R01 semantic layer — Reference Library (Tier C) |
| Failure Class | Validation/delivery taxonomy — Reference Library crosswalk |
| SERP Tactic / Rich Result Type | Subordinate to `serp_reality` glossary; **not** SEO Surface |

**Достаточность:** шесть families + Block subtypes + glossary покрывают RV-01 Tier A без избыточного дробления. Отдельное family «Listing Type» избыточно при наличии `CATEGORY_PAGE`, `PRODUCT_PAGE`, `SEARCH_RESULTS_PAGE` в Page Type vocabulary.

### F1 — Site Type

**Определение:** классификация **целого сайта** по бизнес-цели, монетизации, SEO-позе и типичной IA.

**Canon tokens (v1 evidence):** `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE` (+ v0 legacy `landing`, `service_landing`, … — archive only per WF-R01.1).

**Minimal canon (RV-01 Tier A/B):** Landing, Corporate, Service Business, Ecommerce, Catalog/B2B, SaaS, Media/Publisher, Directory, Manufacturer, Healthcare, Education, Auto — **vocabulary list**, не mandate для немедленного расширения SITE-TYPE-REGISTRY (→ WF-R01.7/R01.8).

### F2 — Page Type

**Определение:** классификация **одной URL / page role** в IA — независимо от визуальной реализации.

**Canon tokens (v1 evidence):** 10 core codes in PAGE-TYPE-REGISTRY-v1 (`HOME_PAGE`, `LANDING_PAGE`, `SERVICE_PAGE`, `CATEGORY_PAGE`, `PRODUCT_PAGE`, `ABOUT_PAGE`, `CONTACT_PAGE`, `FAQ_PAGE`, `BLOG_ARTICLE_PAGE`, `LEGAL_PAGE`).

**Expansion vocabulary (glossary-only until WF-R01.6):** `PRICING_PAGE`, `BLOG_LISTING_PAGE`, `SEARCH_RESULTS_PAGE`, `LOCATION_PAGE`, `CASE_STUDY_PAGE`, `COMPARISON_PAGE`, `RESOURCE_PILLAR_PAGE`, `REGISTRATION_PAGE`, `CONFIRMATION_PAGE`, `ERROR_PAGE` — RV-01 core gaps.

### F3 — Block

**Определение:** каноническая **переиспользуемая секция** страницы с семантикой commercial/SEO/trust/UX и registry `block_id`.

**Subtypes (vocabulary boundary, not separate families):**

| Subtype | Definition | Examples (vocabulary terms, not IDs) |
|---------|------------|--------------------------------------|
| **Structural Block** | Shell + discovery + task-support; cross-page persistence | header/nav, search, filters, breadcrumbs, pagination |
| **Content Block** | Narrative, offer, proof body on a page band | hero, benefits, FAQ, pricing table, testimonials |

**Canon evidence:** BLOCK-REGISTRY-v1 (~29 `block_id`); structural gap documented in WF-R01.2 design.

### F4 — Commercial Pattern

**Определение:** переиспользуемая **композиционная логика** коммерческого повествования — copy structure, ethical constraints, interaction model — **distinct from** `block_id`.

**Canon evidence:** `scroll_process_timeline` (Commercial Pattern Library v1); RV-01 patterns (single-goal landing, message match, problem→solution→proof→CTA, …).

**Binding unit:** `pattern_id` (not `block_id`).

### F5 — Trust Pattern

**Определение:** переиспользуемый **стек доказательств** по сегменту (B2B, B2C, manufacturing, services, ecommerce) — **не** decorative block label.

**Canon evidence:** [trust-semantics-v0.md](../projects/mars-website-factory/trust-semantics-v0.md); site type `trust_model` fields; RV-01 segment stacks.

**Binding unit:** `trust_pattern_id` (future catalog) or **documented stack name** in blueprint until WF-R01.4/R01.5.

**Distinction from Block:** `TESTIMONIALS` block **implements** a trust pattern; trust pattern **prescribes** which proof elements and order apply to a segment.

### F6 — SEO Surface

**Определение:** класс **поисково-релевантной контентной поверхности** — intent, indexation role, honest schema candidacy — **не** SERP feature promise.

**Canon evidence:** seo-architecture v2 ACCEPTED; PAGE-SEO-CONTRACT-v1; RV-01 surfaces (product, category, service, location, article, case study, comparison, resource/pillar, policy, FAQ/help).

**Binding unit:** `seo_surface` label on page blueprint / PAGE-SEO contract (not necessarily a registry row).

**Hard rule:** `page_reality` (surface exists as content type) **≠** `serp_reality` (Google rich result eligibility). FAQ rich result = **obsolete tactic** (2026); FAQ **page** remains valid SEO Surface.

### Cross-cutting vocabulary attributes (all families)

| Attribute | Values | Scope |
|-----------|--------|-------|
| **maturity** | `standard` \| `common` \| `specialized` \| `obsolete` | Any term in any family |
| **canon tier** | `minimal_canon` \| `expansion_backlog` | Promotion gate for registry rows |
| **context_dependent** | boolean + site-type matrix ref | Blocks, some page types |

---

## Family Boundaries

### F1 — Site Type

| Dimension | Definition |
|-----------|------------|
| **Purpose** | Bind whole-project defaults: goals, SEO model, trust posture, typical pages, block shortlists, QA emphasis, HITL level |
| **Scope** | One primary `site_type_code` per project (hybrid = explicit primary + documented secondary) |
| **Ownership** | Site Type Registry steward; WF-R01.6 hygiene for role completeness |
| **Examples** | `CATALOG` — browse/compare, filters required; `LANDING` — single conversion surface |
| **Non-examples** | `FAQ` (page type); `HERO` (block); `product rich result` (SERP tactic); `PIXEL_PERFECT` (production mode) |
| **Common mistakes** | Using site type name for a single campaign URL; mixing `LANDING` site type with multi-page corporate IA without hybrid declaration; treating vertical (restaurant) as core site type before minimal canon stable |

### F2 — Page Type

| Dimension | Definition |
|-----------|------------|
| **Purpose** | Stable `page_type` for Page Architecture Contracts — what role this URL plays in IA |
| **Scope** | Per URL (or canonical variant); constrained by allowed site types matrix |
| **Ownership** | PAGE-TYPE-REGISTRY-v1; expansions via WF-R01.6 |
| **Examples** | `CATEGORY_PAGE` on `CATALOG`; `LANDING_PAGE` as `/` on `LANDING` site type |
| **Non-examples** | `Homepage section` (block composition); `LocalBusiness schema` (structured data property); `Pricing table` (block) |
| **Common mistakes** | Confusing `LANDING` site type with `LANDING_PAGE` page type; inventing page types without matrix update; using `page_type` field in handoff as free text |

### F3 — Block

| Dimension | Definition |
|-----------|------------|
| **Purpose** | Canonical reusable section identity for blueprints, compatibility matrices, reference partials |
| **Scope** | Registered `block_id`; composed in `section_order` on blueprints |
| **Ownership** | BLOCK-REGISTRY-v1; structural slice WF-R01.2; expansion WF-R01.3+ |
| **Examples** | `HERO`, `FAQ`, `PRODUCT_GRID`; structural: `HEADER_NAV`, `FILTERS`, `SEARCH` (vocabulary — IDs pending R01.2) |
| **Non-examples** | `scroll_process_timeline` (commercial pattern); `B2B trust stack` (trust pattern); `sticky CTA` as pattern vs `STICKY_CTA` block ambiguity without charter |
| **Common mistakes** | **HEADER ≠ HERO** (layout-shell-governance); absorbing filters into `PRODUCT_GRID`; creating block_id for every layout micro-component (breadcrumbs as block vs layout policy); marketing-heavy expansion before structural canon |

### F4 — Commercial Pattern

| Dimension | Definition |
|-----------|------------|
| **Purpose** | Reusable commercial narrative / interaction composition with ethical constraints |
| **Scope** | Pattern library; may span multiple blocks on a page |
| **Ownership** | Commercial Pattern Library; WF-R01.4 program |
| **Examples** | Single-goal landing; problem→solution→proof→CTA; scroll-driven process timeline |
| **Non-examples** | `PRICING` block alone (block, not pattern); `HERO` (block); SEO title formula (SEO Pattern Library — separate product module) |
| **Common mistakes** | Registering pattern as `block_id`; duplicating pattern semantics inside site type row without `pattern_id`; dark-pattern tactics as "patterns" |

### F5 — Trust Pattern

| Dimension | Definition |
|-----------|------------|
| **Purpose** | Segment-specific proof stack — what trust elements are industry-standard and in what priority |
| **Scope** | Applied per site type segment + page context; implemented via blocks |
| **Ownership** | Trust semantics docs; future Trust Pattern catalog (WF-R01.4 overlap) |
| **Examples** | B2B: logos + case metrics + security/compliance + contact; Ecommerce: reviews with counts + returns/shipping + payment cues |
| **Non-examples** | Single `TRUST` block row without stack semantics; fake aggregate ratings; `trust_model` field copy without block mapping |
| **Common mistakes** | Collapsing trust into one generic block; treating testimonials block as sufficient B2B trust; schema as substitute for visible proof |

### F6 — SEO Surface

| Dimension | Definition |
|-----------|------------|
| **Purpose** | Classify page's search/content role for honest SEO architecture — titles, internal linking, schema **candidates** |
| **Scope** | Per-page in blueprint / PAGE-SEO contract; may align 1:1 with page type but **not identical** (one page type, multiple surface intents) |
| **Ownership** | seo-architecture v2; WF-R01.5 SEO slice |
| **Examples** | `service` surface on `SERVICE_PAGE`; `category` surface on `CATEGORY_PAGE`; `faq_help` surface (content valid, rich result obsolete) |
| **Non-examples** | `FAQ rich result`; `How-to rich result`; keyword density rules; `block_id` |
| **Common mistakes** | Promising rich results on category/list pages; conflating SEO Surface with page type 1:1 always; treating FAQ as SERP tactic post-2026 deprecation |

### Glossary disambiguation (charter annex — mandatory)

| Term A | Term B | Rule |
|--------|--------|------|
| **section** | **block** | In Factory registry context, **block** = canonical `block_id`; **section** = authoring/layout word — map to `block_id` |
| **module** | **block** | HubSpot/CMS "module" ≈ block; do not create parallel ID namespace |
| **pattern** | **block** | If reusable narrative/composition → Commercial or Trust **Pattern**; if page section → **Block** |
| **component** | **block** | Code component (React/partial) **implements** block; component ≠ registry family |
| **template** | **blueprint** | Template = display scaffold class; Blueprint = per-page orchestration instance |
| **hero** | **header_nav** | Hero = content block; header/nav = structural shell — **never** merge |

---

## Relationship Model

### Primary model — constraint graph (recommended)

Линейная цепочка `Site Type → Page Type → Block → Pattern → SEO Surface` **упрощает** реальность. Рекомендуемая модель — **directed constraint graph**:

```text
                    ┌─────────────────┐
                    │   Site Type     │
                    │  (F1)           │
                    └────────┬────────┘
                             │ constrains allowed
                             ▼
                    ┌─────────────────┐
         ┌─────────│   Page Type     │─────────┐
         │         │  (F2)           │         │
         │         └────────┬────────┘         │
         │                  │ composes          │ maps to
         │                  ▼                   ▼
         │         ┌─────────────────┐  ┌──────────────┐
         │         │     Block       │  │ SEO Surface  │
         │         │  (F3)           │  │   (F6)       │
         │         │ structural │    │  └──────────────┘
         │         │ content    │    │
         │         └─────┬───────┘    │
         │               │            │
         │    overlays   │            │ informs (not dictates)
         ▼               ▼            ▼
┌──────────────┐  ┌──────────────┐   schema candidates
│  Commercial  │  │    Trust     │   (honest, content-backed)
│  Pattern(F4) │  │  Pattern(F5) │
└──────────────┘  └──────────────┘
```

**Edge semantics:**

| Edge | Meaning | Example |
|------|---------|---------|
| Site Type → Page Type | **Allowed matrix** | `CATALOG` requires `CATEGORY_PAGE`; forbids `LANDING_PAGE` as `/` |
| Page Type → Block | **Composition + validation matrix** | `CATEGORY_PAGE` requires structural `FILTERS` + `PRODUCT_GRID` |
| Block → Commercial Pattern | **Implementation** | `PROCESS` block may implement `step_by_step_process` pattern |
| Block → Trust Pattern | **Implementation** | `TESTIMONIALS` + `CASES` implement `b2b_proof_stack` |
| Page Type → SEO Surface | **Default mapping** (overridable) | `PRODUCT_PAGE` → `product` surface |
| SEO Surface ⊥ SERP tactic | **Orthogonal** | `faq_help` surface valid; FAQ rich result **obsolete** |

### Alternative models evaluated

| Model | Description | Verdict |
|-------|-------------|---------|
| **A — Strict linear stack** | Site→Page→Block→Pattern→SEO strictly ordered | **Reject** as sole model — patterns are overlays, SEO surface parallels page type |
| **B — Flat tag soup** | All terms in one namespace with tags | **Reject** — reproduces RV-01 "level mixing" risk |
| **C — Two parallel trees** | IA tree (site/page/block) + Marketing tree (patterns) + SEO tree | **Partial** — use as diagram only; operationally merge via blueprint |
| **D — RV-02 production stack as vocabulary** | tokens→components→sections→templates→content | **Reject** as vocabulary families — **Reference Library** architecture diagram only |
| **E — Constraint graph (recommended)** | Families with typed edges + glossary | **Adopt** |

### Blueprint and Registry positions in the graph

| Layer | Graph role | Vocabulary? |
|-------|------------|-------------|
| **Registry row** | Node instance with stable ID | Yes — belongs to exactly **one** family |
| **Blueprint** | **Composition artifact** referencing registry nodes | No — **operational instance** |
| **Reference partial** | Implementation evidence for a `block_id` | No — delivery artifact |
| **Site semantic graph** (v0 doc) | Cross-artifact relationships | No — semantic doc layer |

**Rule:** A blueprint **instantiates** vocabulary; it does not **define** new vocabulary terms without charter/registry pass.

### Structural vs content block ordering

On catalog surfaces, **structural-before-content** is a canon priority (RV-01 + audits):

```text
HEADER_NAV → BREADCRUMBS → [page intro content] → FILTERS → PRODUCT_GRID → PAGINATION → FOOTER
```

Structural blocks may be **forbidden** on `LANDING` URLs — absence is **policy**, not gap.

---

## Authority Model

### Authority classes

| Class | Role | Mutability | Examples |
|-------|------|------------|----------|
| **Research Artifact** | External/industry evidence, provisional gap tables | Immutable snapshot; new version = new file | RV-01, RV-02, RV-03 |
| **Vocabulary Canon Charter** | Binding **family rules**, glossary, tiering policy | Human sign-off; versioned | Target: `foundry-vocabulary-canon-charter-v1.md` |
| **Program / Subprogram Charter** | Scoped execution authority (WF-R01.x) | ACCEPTED / CHARTERED per pass | WF-R01.1 binding, WF-R01.2 design |
| **Registry** | Stable IDs + rows + matrices | Edit via gated subprograms only | SITE-TYPE-REGISTRY-v1, BLOCK-REGISTRY-v1 |
| **Blueprint Layer** | Per-page / per-site composition contracts | Project-scoped instances | PAGE-CONTRACT, page-blueprint-v0 |
| **Reference Library** | Non-binding patterns, stack diagrams, crosswalks | Editorial update | Production stack, RV-03↔VL3 failure crosswalk |
| **Operational Usage** | Project passports, reports, partials | Per-project | LOC-ZONE, reference-case artifacts |

### Source of Truth assignment

| Content domain | SoT class | Primary location |
|----------------|-----------|------------------|
| Industry site/page/block lists | **Research Artifact** | `research/foundry/rv-01-*.md` |
| Vocabulary family definitions + boundaries | **Vocabulary Canon Charter** (future) | `foundry-vocabulary-canon-charter-v1.md` |
| `site_type_code`, `block_id`, `page_type` rows | **Registry** | `workspaces/website-factory-reference-v1/**` |
| Structural block **policy** (pre-ID) | **Reference / Program design** until R01.2 ACCEPTED | `wf-r01-2-structural-blocks-program-design-v1.md` |
| Trust/commercial **pattern catalog content** | **Registry / Pattern Library** (future rows) | WF-R01.4 deliverable |
| SEO page vs SERP rules | **Vocabulary Canon** + **seo-architecture v2** | Charter glossary + seo-architecture |
| Production modes | **Canonical Charter** (existing) | WF-A01 — **orthogonal** to vocabulary |
| Validation layers | **Canonical Charter** (existing) | WF-A02 |
| Pixel pipeline / tool survey | **Research Artifact** | RV-03 — **WF-A03 only** |
| Per-project section order | **Blueprint / Operational** | Project blueprint artifacts |

### Authority flow (hard rules)

```text
Research Artifact
       │
       ▼ synthesis + tiering (WF-R01.0)
       │
  ┌────┴────────────────┐
  ▼                     ▼
Vocabulary Canon    Reference Library
Charter             (stack, crosswalks)
       │
       ▼ feeds — NO auto-promotion
Subprogram Charter (WF-R01.x ACCEPTED)
       │
       ▼ gated registry edit pass
Registry IDs / matrices
       │
       ▼ instantiate
Blueprint / operational artifacts
```

| Rule ID | Statement |
|---------|-----------|
| **AUTH-01** | Research Artifact **never** auto-promotes to registry row |
| **AUTH-02** | Vocabulary Canon **never** contains registry IDs as normative rows (examples may cite existing IDs illustratively) |
| **AUTH-03** | Registry row **must** declare exactly one vocabulary family |
| **AUTH-04** | Blueprint **references** registry; cannot mint IDs |
| **AUTH-05** | Operational usage **cannot** override ACCEPTED charter tier A rules without waiver/HITL |
| **AUTH-06** | WF-A01/A02 charters **unchanged** by vocabulary canon — harmonization via glossary only |

### Tiering policy (from WF-R01.0 — binding for charter draft)

| Tier | Meaning | Charter action |
|------|---------|----------------|
| **A — Must Adopt** | Family rules, minimal canon policy, structural/content split, page≠SERP | **In charter body** |
| **B — Recommended** | Production stack, canonical_asset vs instance, lifecycle glossary | **Reference Library** + charter cross-link |
| **C — Reference Only** | Vertical exotica, pixel orchestration, full content models | **Research / WF-A03** pointer only |

---

## Registry Implications

Vocabulary Canon **constrains** future registry work — it does **not** authorize edits in this pass.

### Family-to-registry mapping

| Family | Registry artifact | ID format | Current state (doc evidence) |
|--------|-------------------|-----------|------------------------------|
| F1 Site Type | SITE-TYPE-REGISTRY-v1 | `site_type_code` UPPER_SNAKE | 5–8 codes v1; v0 archive |
| F2 Page Type | PAGE-TYPE-REGISTRY-v1 | `page_type` UPPER_SNAKE | 10 core types |
| F3 Block | BLOCK-REGISTRY-v1 | `block_id` UPPER_SNAKE | ~29 ids; structural OPEN |
| F4 Commercial Pattern | Commercial Pattern Library | `pattern_id` snake_case | ~1 pattern |
| F5 Trust Pattern | *planned catalog* | `trust_pattern_id` | Semantics doc only |
| F6 SEO Surface | seo-architecture + PAGE-SEO | `seo_surface` snake_case | Partial coverage |

### Constraints on future registry rows

| Constraint ID | Rule | Consumer |
|---------------|------|----------|
| **REG-VOC-01** | No new ID without declared **family** | All WF-R01.x expansion |
| **REG-VOC-02** | No cross-family ID collision (same string in two families) | Registry hygiene R01.6 |
| **REG-VOC-03** | `minimal_canon` terms prioritized before `expansion_backlog` | R01.2, R01.7, R01.8 |
| **REG-VOC-04** | Structural blocks before marketing-heavy content blocks | R01.2, R01.3 |
| **REG-VOC-05** | Trust Pattern catalog entries **must not** duplicate `block_id` namespace | R01.4 |
| **REG-VOC-06** | Commercial Pattern **must not** register as `block_id` unless explicitly dual-published with charter waiver | R01.4 |
| **REG-VOC-07** | SEO Surface labels **must not** encode deprecated SERP tactics as promises | R01.5 |
| **REG-VOC-08** | Every registry row carries **maturity** attribute (`standard/common/specialized/obsolete`) | R01.6 |
| **REG-VOC-09** | `context_dependent` blocks require SITE-TYPE-BLOCK-MATRIX entry before ACCEPTED | R01.2, R01.6 |
| **REG-VOC-10** | Page type expansion prefers **glossary annex** first; rows require matrix + validation update | R01.6 |
| **REG-VOC-11** | Vertical site types (restaurant, real estate, …) = `expansion_backlog` until WF-R01.8 feed | R01.7, R01.8 |
| **REG-VOC-12** | Rare blocks (countdown, stock counter, calculator) = `specialized` minimum; not minimal canon | Post-R01 |

### Blueprint Layer implications

| Implication | Detail |
|-------------|--------|
| Blueprint fields reference **registry IDs** only | `site_type_code`, `page_type`, `block_id`, optional `pattern_id`, `seo_surface` |
| Blueprint **must not** introduce synonym IDs | Map via WF-R01.1 role mapping |
| PAGE-TYPE-VALIDATION-MATRIX **enforces** family edges | VL1 compatibility |
| Structural absence on LANDING **is valid** | Not AUTO-flagged as gap |

### WF-R01 subprogram alignment

| Subprogram | Vocabulary Canon feeds |
|------------|-------------------------|
| WF-R01.1 | Glossary harmonization (`site_type_id` legacy vs `site_type_code`) |
| WF-R01.2 | Structural vs content block definitions |
| WF-R01.3 | Implementation priority order |
| WF-R01.4 | Commercial + Trust pattern family boundaries |
| WF-R01.5 | SEO Surface vs SERP glossary |
| WF-R01.6 | Maturity attribute, role mapping completeness |
| WF-R01.7 | Minimal canon site/page matrices for Template-Art |
| WF-R01.8 | Execution lessons → expansion_backlog only |

---

## Research Alignment

### RV-01 — Production Vocabulary

| RV-01 finding | Canon disposition | Location |
|---------------|-------------------|----------|
| Registry family hierarchy | **Tier A — Canon** | § Vocabulary Families |
| Minimal canon first | **Tier A — Canon** | `minimal_canon` / `expansion_backlog` |
| standard/common/specialized/obsolete | **Tier A — Canon** | Maturity attribute |
| Structural-before-marketing | **Tier A — Canon** | Block subtype + REG-VOC-04 |
| Trust pattern first-class layer | **Tier A — Canon** | F5 family |
| Commercial patterns distinct from blocks | **Tier A — Canon** | F4 family |
| page_reality ≠ serp_reality | **Tier A — Canon** | F6 + glossary |
| FAQ rich result obsolete | **Tier A — Canon** | F6 obsolete tactic note |
| Core page type gaps (pricing, blog_listing, search_results, …) | **Tier A — Glossary annex** | F2 expansion vocabulary |
| Full vertical site type list | **Tier C — Reference Only** | expansion_backlog |
| Rare ecommerce blocks | **Tier C — Reference Only** | specialized maturity |
| FOUNDRY STATUS cells (Partial/Missing) | **Reference Only** | Provisional until registry verification pass |
| Operational pages (login, account) | **SAFE UNKNOWN** | Glossary candidate; scope decision deferred |

### RV-02 — Website Production Systems

| RV-02 finding | Canon disposition | Location |
|---------------|-------------------|----------|
| 5-layer production stack | **Tier B — Reference Library** | Not vocabulary family |
| canonical_asset vs editorial_instance | **Tier B — Glossary** | Blueprint vs workspace discipline |
| Governance lifecycle states | **Tier B — Reference Library** | Feeds R01.6 hygiene |
| Structured content models + relationships | **Tier C — Reference Only** | Post–WF-R01; semantic layer v0 pointer |
| Cross-project shared libraries | **Tier C — Reference Only** | Wave 6+ planning |
| Design token registry engine | **Tier C — Reference Only** | Design-system architecture |
| Unlimited canvas / marketplace ecosystem | **Rejected** | Non-goals |

### RV-03 — Pixel Factory

| RV-03 finding | Canon disposition | Location |
|---------------|-------------------|----------|
| Orchestration loop (ingest→merge) | **Tier C — WF-A03 only** | Non-goals |
| Failure class taxonomy | **Tier B — Reference Library** | Crosswalk to VL3 + FP-0002 |
| HITL checkpoint model | **Tier B — Reference Library** | Aligns with operator-visual-approval-law |
| Figma-native vs PNG lane priority | **Tier C — WF-A03** | Non-goals for vocabulary |
| Visual baseline / render diff terms | **Tier C — WF-A03** | WF-A02 explicit non-goal |

### Canon vs Reference Only — summary matrix

| In Vocabulary Canon Charter (Tier A) | Reference Only (not in charter body) |
|--------------------------------------|--------------------------------------|
| 6 family definitions + boundaries | Industry vendor tables (Webflow, Shopify, …) |
| Block structural/content subtypes | Full component API / props schema |
| minimal_canon / expansion_backlog policy | Cross-project library product design |
| maturity attribute enum | Drupal entity engine patterns |
| page_reality vs serp_reality | Pixel Factory orchestration stages |
| Glossary disambiguation (section/block/pattern) | Agentic codegen tool survey |
| Registry constraint rules REG-VOC-* | RV-01 provisional gap counts |

---

## Non-Goals

Следующее **явно не входит** в Foundry Vocabulary Canon Charter v1:

| # | Exclusion | Rationale |
|---|-----------|-----------|
| NG-01 | **Registry row creation or ID assignment** | WF-R01.x gated passes only |
| NG-02 | **Structural Blocks implementation** (reference partials) | WF-R01.2/R01.3 scope |
| NG-03 | **Registry Expansion execution** | WF-R01 program execution |
| NG-04 | **Blueprint generation automation** | No runtime claimed |
| NG-05 | **Pixel Factory orchestration** | WF-A03 DEFERRED; RV-03 Tier C |
| NG-06 | **Visual Diff / Screenshot Engine / Render Diff Runtime** | WF-A02/A03 non-goals |
| NG-07 | **Agent Runtime / orchestration** | Not documented as product |
| NG-08 | **SEO Formula Engine** (automated title/meta generation) | SEO Pattern Library ≠ vocabulary canon |
| NG-09 | **Structured content model schema** | RV-02 Tier C for v1 |
| NG-10 | **Design token operational SSOT** | Design-system architecture OPEN |
| NG-11 | **Machine-enforced vocabulary linter** | Human-operated discipline only |
| NG-12 | **Amendment to WF-A01/A02 charters** | Harmonization via glossary cross-links only |
| NG-13 | **Copying full RV tables into charter** | Tier A = rules, not research dump |
| NG-14 | **Third production mode token** | WF-A01 forbids undeclared modes |
| NG-15 | **Marketplace / plugin ecosystem vocabulary** | RV-02 rejected for current canon |

---

## Risks

| Risk | Severity | Mitigation in charter design |
|------|----------|------------------------------|
| **Research Canon ≠ Foundry Canon** drift | High | Authority model AUTH-01..06; tier matrix |
| **Over-absorption** — RV tables copied into registry | High | REG-VOC-03; minimal_canon gate |
| **Level mixing** persists (pattern registered as block) | High | Family boundaries + REG-VOC-05/06 |
| **Linear model oversimplification** misleads operators | Medium | Adopt constraint graph; document overlays |
| **Trust pattern remains implicit** in block names | High | F5 family + future catalog in R01.4 |
| **SEO Surface confused with SERP tactics** | High | page_reality ≠ serp_reality hard rule |
| **Structural canon delayed by marketing blocks** | High | REG-VOC-04; RV-01 priority |
| **False Already Exists** from provisional RV-01 status | Medium | No STATUS claims in charter; verification pass |
| **v0/v1 dual vocabulary** during cutover | Medium | WF-R01.1 binding; glossary legacy map |
| **WF-A03 scope creep** via RV-03 terms | High | Non-goals NG-05/06; Tier C labeling |
| **Charter publication without steward** | Medium | SAFE UNKNOWN; human assignment before ACCEPTED |
| **Blueprint synonyms bypass registry** | Medium | AUTH-04; VL1 compatibility |

---

## SAFE UNKNOWN

| Unknown | What would verify |
|---------|-------------------|
| Named **vocabulary steward** for canon charter | Human governance assignment |
| Exact 1:1 mapping RV-01 minimal site types → v1 `site_type_code` | WF-R01.8 + mapping workshop |
| Whether `PRICING_PAGE`, `SEARCH_RESULTS_PAGE`, etc. need registry rows vs glossary-only | WF-R01.6 hygiene charter |
| BREADCRUMBS / PAGINATION as `block_id` vs layout-component policy | WF-R01.2 operator decision |
| Trust Pattern catalog **binding unit** (`trust_pattern_id` vs segment stack names) | WF-R01.4 charter |
| Depth of structured-data terminology in vocabulary canon | WF-R01.5 + SEO architecture owners |
| Operational pages (login, registration, confirmation) in v1 scope | WF-R01.7 Template-Art charter |
| Live registry dump confirming RV-01 Partial/Missing counts | Registry audit re-run post–R01.1 B3 |
| Whether F6 SEO Surface gets standalone registry file or remains blueprint field | Architecture decision in R01.5 |
| Triumph v6 / OCPilot lessons indexed to vocabulary backlog | WF-R01.8 execution feed |
| Timeline for charter **ACCEPTED** publication | Human charter schedule |
| JSON Schema for maturity attribute on registry rows | R01.6 implementation |

---

## Recommended Next Step

1. **Human review** of this design — confirm six families, constraint graph model, and REG-VOC constraint set.
2. **Charter pass (separate task):** draft `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` — Tier A rules only, **zero registry rows**, **zero new IDs**.
3. **Optional parallel:** Reference Library items from WF-R01.0 (production-systems-stack-v1, rv03-vl3-failure-crosswalk-v1) — non-blocking.
4. **Editorial cross-links:** cite RV-01 in WF-R01.2 design § Industry Canon (human-approved micro-edit).
5. **Do not start:** registry file edits, WF-R01.2 implementation, WF-A03, charter ACCEPTED without sign-off.

**WF-R01.0 proposed exit criterion (unchanged):** Vocabulary Canon Charter v1 **ACCEPTED** + authority model in OPERATIONAL-INDEX + RV-01–03 cited from WF-R01 program charter.

---

**STOP — NO IMPLEMENTATION · NO REGISTRY CHANGES · NO NEW IDS · NO CHARTER PUBLICATION**

---

*Design artifact: `reports/foundry-vocabulary-canon-charter-design-v1.md`*
