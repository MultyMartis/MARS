# FOUNDRY Vocabulary Canon Charter v1

**Status:** **ACCEPTED** — canonical Source of Truth for **Foundry vocabulary families**, boundaries, and registry promotion rules.  
**Not:** runtime, registry content, orchestration, agent automation, or machine-enforced vocabulary linter.

**Version:** v1  
**Date:** 2026-06-19  
**Charter pass:** [foundry-vocabulary-canon-charter-pass-v1.md](../../reports/foundry-vocabulary-canon-charter-pass-v1.md)  
**Design basis:** [foundry-vocabulary-canon-charter-design-v1.md](../../reports/foundry-vocabulary-canon-charter-design-v1.md) · [wf-r01-0-research-canon-integration-design-v1.md](../../reports/wf-r01-0-research-canon-integration-design-v1.md)

**Honesty boundary:** This charter defines **terminology and family rules only**. It does **not** create registry rows, assign IDs, or authorize registry expansion. Promotion to registry requires gated WF-R01.x subprogram passes.

**Terminology:** **FOUNDRY** = **Website Factory** ecosystem (строка FOUNDRY как отдельный продукт/путь в repo **не найдена**).

---

## Executive Summary

FOUNDRY operates between **Research Artifacts** (RV-01–03) and **Registry rows** (`site_type_code`, `page_type`, `block_id`, pattern libraries). Without a normative intermediate layer, operators and agents risk **level mixing** — treating site types as page types, blocks as patterns, SEO tactics as content surfaces, or audit proxies as industry evidence.

**This charter closes that gap.** It establishes:

1. **Six vocabulary families** (F1–F6) aligned to existing or planned registry homes.
2. **Family boundaries** and a mandatory **glossary disambiguation** annex.
3. A **constraint graph** (not a strict linear pipeline) relating families.
4. An **authority model** with hard promotion rules from research → canon → subprogram → registry.
5. **Registry constraint rules** (REG-VOC-*) that govern future WF-R01.x expansion — without executing it.

**Relationship to upstream charters:**

| Charter | Relationship |
|---------|--------------|
| **WF-A01** Production Modes | **Orthogonal** — `PIXEL_PERFECT` / `TEMPLATE_ART` are fidelity contracts, not vocabulary families |
| **WF-A02** Validation Architecture | **Consumes** registry vocabulary at VL1; does not define families |
| **VL3 Domains** | **Orthogonal** — composition/extract validation; crosswalk via Reference Library only |
| **WF-R01** Registry Expansion | **Downstream consumer** — subprograms R01.1–R01.8 execute registry edits gated by this canon |
| **WF-R01.1** v0→v1 Binding | **Harmonizes** legacy field names (`site_type_id` → `site_type_code`); does not amend this charter |

**Authority flow:**

```text
Research Artifact (RV-01, RV-02, RV-03)
       │
       ▼ synthesis + tiering (WF-R01.0)
       │
  ┌────┴────────────────┐
  ▼                     ▼
Vocabulary Canon    Reference Library
Charter (this doc)  (stack, crosswalks)
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

---

## Vocabulary Families

### Sufficiency

Six families cover industry production vocabulary (RV-01 Tier A) without redundant subdivision. **Listing Type** is absorbed into **Page Type** (`CATEGORY_PAGE`, `PRODUCT_PAGE`, `SEARCH_RESULTS_PAGE`). **Component** (code) and **Design Token** are implementation layers — glossary only, not families.

| # | Family | Registry home | Binding unit |
|---|--------|---------------|--------------|
| **F1** | **Site Type** | SITE-TYPE-REGISTRY-v1 | `site_type_code` |
| **F2** | **Page Type** | PAGE-TYPE-REGISTRY-v1 | `page_type` |
| **F3** | **Block** | BLOCK-REGISTRY-v1 | `block_id` |
| **F4** | **Commercial Pattern** | Commercial Pattern Library | `pattern_id` |
| **F5** | **Trust Pattern** | Trust semantics + future catalog | `trust_pattern_id` (future) |
| **F6** | **SEO Surface** | seo-architecture v2 + PAGE-SEO contracts | `seo_surface` label |

### F1 — Site Type

**Definition:** Classification of the **whole site** by business goal, monetization, SEO posture, and typical IA.

**Purpose:** Bind whole-project defaults — goals, SEO model, trust posture, typical pages, block shortlists, QA emphasis, HITL level.

**Scope:** One primary `site_type_code` per project (hybrid = explicit primary + documented secondary).

**Non-examples:** `FAQ` (page type); `HERO` (block); `product rich result` (SERP tactic); `PIXEL_PERFECT` (production mode).

### F2 — Page Type

**Definition:** Classification of **one URL / page role** in IA — independent of visual implementation.

**Purpose:** Stable `page_type` for Page Architecture Contracts.

**Scope:** Per URL; constrained by allowed site types matrix.

**Non-examples:** Homepage section (block composition); `LocalBusiness schema` (structured data property); pricing table (block).

**Expansion vocabulary (glossary-only until WF-R01.6):** `PRICING_PAGE`, `BLOG_LISTING_PAGE`, `SEARCH_RESULTS_PAGE`, `LOCATION_PAGE`, `CASE_STUDY_PAGE`, `COMPARISON_PAGE`, `RESOURCE_PILLAR_PAGE`, `REGISTRATION_PAGE`, `CONFIRMATION_PAGE`, `ERROR_PAGE`.

### F3 — Block

**Definition:** Canonical **reusable page section** with commercial/SEO/trust/UX semantics and registry `block_id`.

**Subtypes (vocabulary boundary — not separate families):**

| Subtype | Definition | Examples (vocabulary terms, not IDs) |
|---------|------------|----------------------------------------|
| **Structural Block** | Shell + discovery + task-support; cross-page persistence | header/nav, search, filters, breadcrumbs, pagination |
| **Content Block** | Narrative, offer, proof body on a page band | hero, benefits, FAQ, pricing table, testimonials |

**Non-examples:** `scroll_process_timeline` (commercial pattern); B2B trust stack (trust pattern).

### F4 — Commercial Pattern

**Definition:** Reusable **commercial narrative composition** — copy structure, ethical constraints, interaction model — **distinct from** `block_id`.

**Purpose:** Pattern library entries spanning multiple blocks on a page.

**Binding unit:** `pattern_id` (not `block_id`).

**Non-examples:** `PRICING` block alone; SEO title formula (SEO Pattern Library — separate product module).

### F5 — Trust Pattern

**Definition:** Reusable **proof stack** by segment (B2B, B2C, manufacturing, services, ecommerce) — **not** a decorative block label.

**Purpose:** Prescribe which proof elements and order apply to a segment; implemented via blocks.

**Distinction from Block:** `TESTIMONIALS` block **implements** a trust pattern; trust pattern **prescribes** stack semantics.

**Binding unit:** `trust_pattern_id` (future catalog) or documented stack name in blueprint until WF-R01.4/R01.5.

### F6 — SEO Surface

**Definition:** Class of **search-relevant content surface** — intent, indexation role, honest schema candidacy — **not** SERP feature promise.

**Purpose:** Classify page search/content role for honest SEO architecture.

**Scope:** Per-page in blueprint / PAGE-SEO contract; may align with page type but **not identical** (one page type, multiple surface intents).

**Hard rule:** `page_reality` (surface exists as content type) **≠** `serp_reality` (Google rich result eligibility). FAQ rich result = **obsolete tactic** (2026); FAQ **page** remains valid SEO Surface.

### Cross-cutting attributes (all families)

| Attribute | Values | Scope |
|-----------|--------|-------|
| **maturity** | `standard` \| `common` \| `specialized` \| `obsolete` | Any term in any family |
| **canon tier** | `minimal_canon` \| `expansion_backlog` | Promotion gate for registry rows |
| **context_dependent** | boolean + site-type matrix ref | Blocks, some page types |

### Explicitly not vocabulary families

| Term | Canonical home |
|------|----------------|
| Production Mode (`PIXEL_PERFECT` / `TEMPLATE_ART`) | WF-A01 charter |
| Blueprint | Instance artifact — operational layer |
| Template / Layout Template | Display scaffold — maps to Blueprint |
| Component (code) | Developer primitive — RV-02 stack layer |
| Design Token | Design-system architecture |
| Content Model / Entity | Reference Library (Tier C) |
| Failure Class | Reference Library crosswalk |
| SERP Tactic / Rich Result Type | Glossary under `serp_reality`; not SEO Surface |

---

## Family Boundaries

### Block vs Pattern

| Question | If yes → |
|----------|----------|
| Is it a reusable **page section** with registry identity? | **Block** (F3) |
| Is it a reusable **narrative/composition logic** spanning blocks? | **Commercial Pattern** (F4) or **Trust Pattern** (F5) |

**Rule:** Commercial and Trust patterns **must not** register as `block_id` unless explicitly dual-published with charter waiver (REG-VOC-06).

### Commercial vs Trust

| Dimension | Commercial Pattern (F4) | Trust Pattern (F5) |
|-----------|-------------------------|---------------------|
| **Focus** | Offer narrative, conversion logic, ethical interaction | Proof stack, credibility, segment-specific evidence |
| **Examples** | Single-goal landing; problem→solution→proof→CTA | B2B: logos + case metrics + compliance; Ecommerce: reviews + returns |
| **Mistake** | Dark-pattern tactics labeled as patterns | Collapsing trust into one generic `TRUST` block |

### SEO Surface vs Page Type

| Dimension | Page Type (F2) | SEO Surface (F6) |
|-----------|----------------|------------------|
| **Question answered** | What **IA role** does this URL play? | What **search/content class** does this page represent? |
| **Relationship** | Default mapping exists (e.g. `PRODUCT_PAGE` → `product` surface) | Overridable; not 1:1 mandatory |
| **Mistake** | Using page type as SERP promise | Encoding deprecated rich results as surface labels |

### Blueprint vs Vocabulary

| Layer | Role | Defines vocabulary? |
|-------|------|---------------------|
| **Registry row** | Node instance with stable ID | Yes — belongs to exactly **one** family |
| **Blueprint** | Composition artifact referencing registry nodes | **No** — operational instance |
| **Reference partial** | Implementation evidence for a `block_id` | No — delivery artifact |

**Rule:** A blueprint **instantiates** vocabulary; it does **not** define new vocabulary terms without charter/registry pass (AUTH-04).

### Glossary disambiguation (mandatory)

| Term A | Term B | Rule |
|--------|--------|------|
| **section** | **block** | In Factory registry context, **block** = canonical `block_id`; **section** = authoring word — map to `block_id` |
| **module** | **block** | HubSpot/CMS "module" ≈ block; do not create parallel ID namespace |
| **pattern** | **block** | Reusable narrative/composition → Commercial or Trust **Pattern**; page section → **Block** |
| **component** | **block** | Code component **implements** block; component ≠ registry family |
| **template** | **blueprint** | Template = display scaffold class; Blueprint = per-page orchestration instance |
| **hero** | **header_nav** | Hero = content block; header/nav = structural shell — **never** merge |

---

## Constraint Graph

Linear chain `Site Type → Page Type → Block → Pattern → SEO Surface` **oversimplifies** reality. FOUNDRY uses a **directed constraint graph**:

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

| Edge | Meaning |
|------|---------|
| Site Type → Page Type | **Allowed matrix** — e.g. `CATALOG` requires `CATEGORY_PAGE`; forbids `LANDING_PAGE` as `/` |
| Page Type → Block | **Composition + validation matrix** |
| Block → Commercial/Trust Pattern | **Implementation** — block may implement pattern |
| Page Type → SEO Surface | **Default mapping** (overridable) |
| SEO Surface ⊥ SERP tactic | **Orthogonal** — `faq_help` surface valid; FAQ rich result **obsolete** |

**Structural-before-content ordering** on catalog surfaces:

```text
HEADER_NAV → BREADCRUMBS → [page intro] → FILTERS → PRODUCT_GRID → PAGINATION → FOOTER
```

Structural block absence on `LANDING` URLs is **policy**, not gap.

---

## Authority Model

### Authority classes

| Class | Role | Mutability |
|-------|------|------------|
| **Research Artifact** | External/industry evidence, provisional gap tables | Immutable snapshot; new version = new file |
| **Vocabulary Canon Charter** | Binding **family rules**, glossary, tiering policy | Human sign-off; versioned — **this document** |
| **Program / Subprogram Charter** | Scoped execution authority (WF-R01.x) | ACCEPTED / CHARTERED per pass |
| **Registry** | Stable IDs + rows + matrices | Edit via gated subprograms only |
| **Blueprint Layer** | Per-page / per-site composition contracts | Project-scoped instances |
| **Reference Library** | Non-binding patterns, stack diagrams, crosswalks | Editorial update |
| **Operational Usage** | Project passports, reports, partials | Per-project |

### Source of Truth assignment

| Content domain | SoT class | Primary location |
|----------------|-----------|------------------|
| Industry site/page/block lists | **Research Artifact** | `research/foundry/rv-01-production-vocabulary.md` |
| Vocabulary family definitions + boundaries | **Vocabulary Canon Charter** | **This document** |
| `site_type_code`, `block_id`, `page_type` rows | **Registry** | `workspaces/website-factory-reference-v1/**` |
| Production modes | **Canonical Charter** | WF-A01 — **orthogonal** |
| Validation layers | **Canonical Charter** | WF-A02 + VL3 |
| Pixel pipeline / tool survey | **Research Artifact** | RV-03 — **WF-A03 only** |

### Hard rules

| Rule ID | Statement |
|---------|-----------|
| **AUTH-01** | Research Artifact **never** auto-promotes to registry row |
| **AUTH-02** | Vocabulary Canon **never** contains registry IDs as normative rows (illustrative citations only) |
| **AUTH-03** | Registry row **must** declare exactly one vocabulary family |
| **AUTH-04** | Blueprint **references** registry; cannot mint IDs |
| **AUTH-05** | Operational usage **cannot** override ACCEPTED charter Tier A rules without waiver/HITL |
| **AUTH-06** | WF-A01/A02 charters **unchanged** by vocabulary canon — harmonization via glossary only |

### Tiering policy

| Tier | Meaning | Charter action |
|------|---------|----------------|
| **A — Must Adopt** | Family rules, minimal canon policy, structural/content split, page≠SERP | **In charter body** |
| **B — Recommended** | Production stack, canonical_asset vs instance, lifecycle glossary | **Reference Library** + charter cross-link |
| **C — Reference Only** | Vertical exotica, pixel orchestration, full content models | **Research / WF-A03** pointer only |

---

## Registry Rules

This charter **constrains** future registry work. It does **not** authorize edits in this pass.

### Family-to-registry mapping

| Family | Registry artifact | ID format |
|--------|-------------------|-----------|
| F1 Site Type | SITE-TYPE-REGISTRY-v1 | `site_type_code` UPPER_SNAKE |
| F2 Page Type | PAGE-TYPE-REGISTRY-v1 | `page_type` UPPER_SNAKE |
| F3 Block | BLOCK-REGISTRY-v1 | `block_id` UPPER_SNAKE |
| F4 Commercial Pattern | Commercial Pattern Library | `pattern_id` snake_case |
| F5 Trust Pattern | *planned catalog* | `trust_pattern_id` |
| F6 SEO Surface | seo-architecture + PAGE-SEO | `seo_surface` snake_case |

### Constraint rules (REG-VOC-*)

| ID | Rule |
|----|------|
| **REG-VOC-01** | No new ID without declared **family** |
| **REG-VOC-02** | No cross-family ID collision (same string in two families) |
| **REG-VOC-03** | `minimal_canon` terms prioritized before `expansion_backlog` |
| **REG-VOC-04** | Structural blocks before marketing-heavy content blocks |
| **REG-VOC-05** | Trust Pattern catalog entries **must not** duplicate `block_id` namespace |
| **REG-VOC-06** | Commercial Pattern **must not** register as `block_id` unless explicitly dual-published with charter waiver |
| **REG-VOC-07** | SEO Surface labels **must not** encode deprecated SERP tactics as promises |
| **REG-VOC-08** | Every registry row carries **maturity** attribute |
| **REG-VOC-09** | `context_dependent` blocks require SITE-TYPE-BLOCK-MATRIX entry before ACCEPTED |
| **REG-VOC-10** | Page type expansion prefers **glossary annex** first; rows require matrix + validation update |
| **REG-VOC-11** | Vertical site types = `expansion_backlog` until WF-R01.8 feed |
| **REG-VOC-12** | Rare blocks (countdown, stock counter, calculator) = `specialized` minimum |

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

| Finding | Disposition |
|---------|-------------|
| Registry family hierarchy | **Tier A — Canon** (§ Vocabulary Families) |
| minimal_canon / expansion_backlog | **Tier A — Canon** |
| standard/common/specialized/obsolete | **Tier A — Canon** |
| Structural-before-marketing | **Tier A — Canon** (Block subtypes + REG-VOC-04) |
| Trust pattern first-class layer | **Tier A — Canon** (F5) |
| Commercial patterns distinct from blocks | **Tier A — Canon** (F4) |
| page_reality ≠ serp_reality | **Tier A — Canon** (F6 + glossary) |
| FAQ rich result obsolete | **Tier A — Canon** |
| Core page type gaps | **Tier A — Glossary annex** (F2 expansion vocabulary) |
| Full vertical site type list | **Tier C — Reference Only** |
| Rare ecommerce blocks | **Tier C — Reference Only** |
| FOUNDRY STATUS cells (Partial/Missing) | **Reference Only** — provisional until registry verification |
| Operational pages (login, account) | **SAFE UNKNOWN** |

**Source:** [research/foundry/rv-01-production-vocabulary.md](../../research/foundry/rv-01-production-vocabulary.md)

### RV-02 — Website Production Systems

| Finding | Disposition |
|---------|-------------|
| 5-layer production stack | **Tier B — Reference Library** |
| canonical_asset vs editorial_instance | **Tier B — Glossary** |
| Governance lifecycle states | **Tier B — Reference Library** |
| Structured content models + relationships | **Tier C — Reference Only** |
| Cross-project shared libraries | **Tier C — Reference Only** |
| Design token registry engine | **Tier C — Reference Only** |
| Unlimited canvas / marketplace ecosystem | **Rejected** |

**Source:** [research/foundry/rv-02-website-production-systems.md](../../research/foundry/rv-02-website-production-systems.md)

### RV-03 — Pixel Factory

| Finding | Disposition |
|---------|-------------|
| Orchestration loop (ingest→merge) | **Tier C — WF-A03 only** |
| Failure class taxonomy | **Tier B — Reference Library** (VL3 + FP-0002 crosswalk) |
| HITL checkpoint model | **Tier B — Reference Library** |
| Figma-native vs PNG lane priority | **Tier C — WF-A03** |
| Visual baseline / render diff terms | **Tier C — WF-A03** |

**Source:** [research/foundry/rv-03-pixel-factory.md](../../research/foundry/rv-03-pixel-factory.md)

---

## Non-Goals

This charter v1 does **not** authorize:

| # | Exclusion |
|---|-----------|
| NG-01 | Registry row creation or ID assignment |
| NG-02 | Structural Blocks implementation (reference partials) |
| NG-03 | Registry Expansion execution |
| NG-04 | Blueprint generation automation |
| NG-05 | Pixel Factory orchestration (WF-A03 DEFERRED) |
| NG-06 | Visual Diff / Screenshot Engine / Render Diff Runtime |
| NG-07 | Agent Runtime / orchestration |
| NG-08 | SEO Formula Engine |
| NG-09 | Structured content model schema |
| NG-10 | Design token operational SSOT |
| NG-11 | Machine-enforced vocabulary linter |
| NG-12 | Amendment to WF-A01/A02 charters |
| NG-13 | Copying full RV tables into charter body |
| NG-14 | Third production mode token |
| NG-15 | Marketplace / plugin ecosystem vocabulary |

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Research Canon ≠ Foundry Canon drift | High | AUTH-01..06; tier matrix |
| Over-absorption — RV tables copied into registry | High | REG-VOC-03; minimal_canon gate |
| Level mixing (pattern registered as block) | High | Family boundaries + REG-VOC-05/06 |
| Linear model oversimplification | Medium | Constraint graph model |
| Trust pattern remains implicit in block names | High | F5 family; WF-R01.4 catalog |
| SEO Surface confused with SERP tactics | High | page_reality ≠ serp_reality |
| Structural canon delayed by marketing blocks | High | REG-VOC-04 |
| False Already Exists from provisional RV-01 status | Medium | No STATUS claims in charter |
| v0/v1 dual vocabulary during cutover | Medium | WF-R01.1 binding; glossary legacy map |
| WF-A03 scope creep via RV-03 terms | High | Non-goals NG-05/06; Tier C labeling |
| Blueprint synonyms bypass registry | Medium | AUTH-04; VL1 compatibility |

---

## SAFE UNKNOWN

| Unknown | What would verify |
|---------|-------------------|
| Named **vocabulary steward** for canon charter | Human governance assignment |
| Exact 1:1 mapping RV-01 minimal site types → v1 `site_type_code` | WF-R01.8 + mapping workshop |
| Whether expansion page types need registry rows vs glossary-only | WF-R01.6 hygiene charter |
| BREADCRUMBS / PAGINATION as `block_id` vs layout-component policy | WF-R01.2 operator decision |
| Trust Pattern catalog binding unit | WF-R01.4 charter |
| Depth of structured-data terminology in vocabulary canon | WF-R01.5 + SEO architecture owners |
| Operational pages (login, registration, confirmation) in v1 scope | WF-R01.7 Template-Art charter |
| Live registry dump confirming RV-01 Partial/Missing counts | Registry audit re-run post–R01.1 B3 |
| Whether F6 SEO Surface gets standalone registry file or remains blueprint field | Architecture decision in R01.5 |
| Triumph v6 / OCPilot lessons indexed to vocabulary backlog | WF-R01.8 execution feed |
| JSON Schema for maturity attribute on registry rows | R01.6 implementation |

---

## Related documents

| Document | Role |
|----------|------|
| [wf-r01-registry-expansion-program-charter-v1.md](../../reports/wf-r01-registry-expansion-program-charter-v1.md) | Parent program — CHARTERED |
| [wf-r01-1-v0-v1-binding-charter-v1.md](../../reports/wf-r01-1-v0-v1-binding-charter-v1.md) | v0→v1 binding — ACCEPTED |
| [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md) | WF-A01 — orthogonal |
| [website-factory-validation-architecture-charter-v1.md](website-factory-validation-architecture-charter-v1.md) | WF-A02 |
| [website-factory-vl3-domains-charter-v1.md](website-factory-vl3-domains-charter-v1.md) | VL3 domains |
| [roadmap.md](roadmap.md) | Factory architecture items |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Operator entry |

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Status | **ACCEPTED** |
| Created | 2026-06-19 |
| Runtime | **Not claimed** |
| Registry rows | **Zero** — charter pass verified |
| Commit / push | Not performed by default |

---

*Canonical SoT for FOUNDRY vocabulary families F1–F6. Human-operated documentation only.*
