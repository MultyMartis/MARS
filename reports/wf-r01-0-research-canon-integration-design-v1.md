# REPORT — WF-R01.0 RESEARCH CANON INTEGRATION

**Program ID:** WF-R01.0 — Research Canon Integration  
**Date:** 2026-06-19  
**Mode:** program design only — **no implementation**, **no canon changes**, **no roadmap edits**  
**Parent program:** WF-R01 — FOUNDRY Registry Expansion Program (**CHARTERED**)

**Research inputs (this pass):**

| ID | Artifact |
|----|----------|
| RV-01 | [research/foundry/rv-01-production-vocabulary.md](../research/foundry/rv-01-production-vocabulary.md) |
| RV-02 | [research/foundry/rv-02-website-production-systems.md](../research/foundry/rv-02-website-production-systems.md) |
| RV-03 | [research/foundry/rv-03-pixel-factory.md](../research/foundry/rv-03-pixel-factory.md) |

**Authority context:** [wf-r01-registry-expansion-program-charter-v1.md](wf-r01-registry-expansion-program-charter-v1.md) · [wf-r01-1-v0-v1-binding-charter-v1.md](wf-r01-1-v0-v1-binding-charter-v1.md) · [wf-r01-2-structural-blocks-program-design-v1.md](wf-r01-2-structural-blocks-program-design-v1.md) · WF-A01/A02/VL3 charters · [foundry-registry-layer-audit-v1.md](foundry-registry-layer-audit-v1.md) · [foundry-system-wide-layer-audit-v1.md](foundry-system-wide-layer-audit-v1.md) · [foundry-capability-gap-audit-v1.md](foundry-capability-gap-audit-v1.md)

**Honesty boundary:** WF-R01.0 — **documentation program design** (human-operated). **Not** runtime, **not** registry content changes, **not** charter amendments in this artifact.

**Terminology:** **FOUNDRY** = **Website Factory** ecosystem (строка FOUNDRY как отдельный продукт/путь в repo **не найдена**).

---

## Executive Summary

Исследования RV-01, RV-02 и RV-03 выполнены и лежат в `research/foundry/`, но **не интегрированы** в канонический слой FOUNDRY. Параллельно WF-R01.2 и program design уже ссылаются на industry canon **без RV-файлов** (proxy audits). Это создаёт риск **Research Canon ≠ Foundry Canon**: операторы и агенты могут принимать решения по audit-proxy, не видя полного research evidence chain.

**Главный вывод WF-R01.0:** интеграция должна быть **селективной и tiered**, а не «скопировать research в charter». Из трёх исследований в **Foundry Vocabulary Canon** (как design target для WF-R01.x) целесообразно принять **семейную иерархию vocabulary** (RV-01 Tier A), **production stack layering** как reference architecture (RV-02 Tier A/B), и **разделение page/SERP reality** (RV-01 Tier A). RV-02 элементы **structured content models**, **cross-project libraries**, **token governance** и весь контур RV-03 **Pixel Factory orchestration** — **не** текущий vocabulary/registry canon; они относятся к **planned architecture** (WF-R01.4–R01.7, WF-A03) или **Reference Library**.

**Рекомендуемая роль WF-R01.0:** charter **integration program** между research artifacts и существующими subprograms WF-R01.1–R01.8 — без новых `block_id`, без registry rows, без WF-A03 scope creep.

**Блокирующий факт:** RV-исследования **не были** в repo на момент публикации [wf-r01-2-structural-blocks-program-design-v1.md](wf-r01-2-structural-blocks-program-design-v1.md) § Research Integration. WF-R01.0 закрывает этот пробел на уровне **authority mapping**, не implementation.

---

## Research Inventory

### RV-01 — Production Vocabulary Research

| Field | Content |
|-------|---------|
| **Scope** | Отраслевой canon site types, page types, block vocabulary (core/common/rare), commercial patterns, trust patterns, SEO content surfaces; gap analysis относительно Foundry (provisional, без registry dump). |
| **Ключевые выводы** | (1) Рынок использует **иерархические registry families**, не плоский словарь. (2) Minimal core site types: Landing, Corporate, Service Business, Ecommerce, Catalog/B2B, SaaS, Media/Publisher, Directory, Manufacturer, Healthcare, Education, Auto. (3) Structural primitives (header/nav, footer, search, filters, pagination, cards/lists) **важнее** marketing-heavy blocks. (4) Trust patterns — отдельный first-class слой. (5) FAQ/How-to **rich results deprecated** (Google 2026) — FAQ остаётся content page, не SERP tactic. (6) Атрибут maturity: standard / common / specialized / obsolete. |
| **Применимые выводы** | Семейная структура vocabulary; minimal canon first; structural-before-marketing priority; trust canon as registry family; page reality ≠ SERP reality; standard/common/specialized/obsolete attribute; SEO surfaces vs tactics split. Прямое усиление WF-R01.2 structural candidates, WF-R01.4 commercial patterns, WF-R01.5 SEO slice, WF-R01.7 Template-Art readiness. |
| **Неприменимые / отложенные** | Полный vertical coverage (real estate, restaurant, nonprofit, event, community, portfolio, marketplace) как **minimal canon** — отложить в expansion backlog (WF-R01 Extended / R01.8). Rare blocks (countdown, stock counter, quick order, calculator) — **не** vocabulary baseline. Operational pages (login, registration, confirmation) — приоритет **SAFE UNKNOWN** для v1 scope. Structured-data terminology как отдельный словарь — решение отложено. Конкретные FOUNDRY STATUS cells (Partial/Missing) — **provisional** без live registry verification pass. |
| **Confidence** | **High** на industry taxonomy и family separation (множественные platform sources). **Medium** на Foundry gap counts (brief-only inference в RV-01). **Medium-High** на structural priority (согласуется с тремя repo audits). |

---

### RV-02 — Website Production Systems Research

| Field | Content |
|-------|---------|
| **Scope** | Зрелые Website Production Systems: builders (Webflow, Framer, Builder.io, Wix Studio, Squarespace, Duda), CMS (WordPress, Shopify, HubSpot, Drupal), enterprise design systems (Carbon, Atlassian, SLDS, Material, Polaris); page-building architectures; content architecture; governance models. |
| **Ключевые выводы** | (1) Зрелые системы — **гибрид**: tokens → components → sections/blocks → templates → content models/relationships. (2) Editor layer = block/section-first; developer layer = component/schema-first. (3) **Canonical assets vs editorial instances** — повторяющийся invariant. (4) Без first-class content models + relationships система остаётся page assembly tool. (5) Governance (versioning, permissions, lifecycle states, constrained authoring) — prerequisite масштаба. (6) Marketplace/plugin ecosystem — **not needed** на текущем этапе Factory. |
| **Применимые выводы** | Пятислойный production stack как **reference architecture** (не product copy). Разделение blueprint/schema layer vs template vs block authoring — усиливает существующий layer-map и blueprint discipline. Lifecycle governance vocabulary (draft/preview/stable, deprecation) — reference для WF-R01.6 hygiene и block-quality-tiers. Constrained authoring concept — alignment с Forge modes + HITL. |
| **Неприменимые / отложенные** | Полноценные **structured content models** и **reference fields** как Factory runtime — **вне** WF-R01 vocabulary scope; semantic-relationship layer v0 уже doc-only, не implementation. **Cross-project shared libraries** как product — нет evidence в repo; Wave 6 curated-library — project-local. **Design token registry engine** — design system architecture-only (DG gaps OPEN). **Visual editor / unlimited canvas** — rejected as Factory direction. **Drupal-style entity engine** — reference only, not adoption target. |
| **Confidence** | **High** на layered stack invariant (cross-platform convergence). **Medium** на Foundry gap table inside RV-02 (self-stated: no internal FOUNDRY specs provided). **High** на alignment с documented Factory layers (registry, blueprint, frontend, validation) — partial overlap already exists. |

---

### RV-03 — Pixel Factory & AI Production Research

| Field | Content |
|-------|---------|
| **Scope** | Figma-to-code systems, extraction pipelines, pixel QA (Playwright, BackstopJS, Percy, Chromatic), production pipelines, failure classes, human-in-the-loop models; gap analysis for WF-A03. |
| **Ключевые выводы** | (1) Production-grade path = **orchestrator loop**, not one-shot generator: ingest → extract → map → generate → render → diff → fix → approve → merge. (2) Figma-native lane **приоритетнее** PNG/vision lane. (3) Component mapping к codebase — зрелый паттерн (Builder, Locofy). (4) Asset extraction must be **deterministic**. (5) Visual baselines + human approval — industry standard bar. (6) Failure classes: asset mismatch, component mismatch, text hallucination, ordering drift, layout drift, responsive drift, render drift. |
| **Применимые выводы** | Терминология failure classes — **crosswalk** к VL3 domains (IR-, AI-, VO-, TL-) и FP-0002 forensic taxonomy (Reference Library). HITL placement model (mapping, visual review, spatial correction, debug-after-signal) — alignment с operator-visual-approval-law и existing VL chain. **Separation:** RV-03 **не** расширяет Block Registry; оно описывает **delivery pipeline** для `PIXEL_PERFECT` mode. |
| **Неприменимые / отложенные** | Весь **Pixel Factory orchestration layer**, Vision Runtime, Screenshot Engine, Render Diff Engine, automated autofix — **WF-A03 only**, explicitly **DEFERRED**. Agentic codegen (v0, Lovable) as Factory core — **reject** as canon direction. PNG→HTML vision-first as primary lane — **secondary/deferred**. Repo sync automation — planned implementation, not doc canon. |
| **Confidence** | **High** на pipeline shape and QA bar (commercial + research consensus). **Low-Medium** на Foundry-specific gap (RV-03 notes VL3/FP-0002 not fully accessible in session). **High** that WF-A03 must not leak into WF-R01 registry work. |

---

## Production Vocabulary Candidates

Кандидаты для **Foundry Vocabulary Canon** — нормативный словарь и family rules, **не** registry rows. Внедрение — через будущие WF-R01.x charters после human sign-off.

### Production terms

| Candidate term / rule | Source | Canon tier | Notes |
|----------------------|--------|------------|-------|
| `registry_family` — Site Type → Page Type → Block → Commercial Pattern → Trust Pattern → SEO Surface | RV-01 | **A** | Hard rule для WF-R01 vocabulary normalization |
| `minimal_canon` vs `expansion_backlog` | RV-01 | **A** | Gates new IDs in R01.2+ |
| `standard` / `common` / `specialized` / `obsolete` (vocabulary maturity) | RV-01 | **A** | Attribute, not enum replacement for block categories |
| `structural_block` (shell + discovery) vs `content_block` | RV-01 + RV-02 + R01.2 design | **A** | Vocabulary boundary; implementation → WF-R01.2 |
| `production_mode` (`PIXEL_PERFECT` \| `TEMPLATE_ART`) | WF-A01 (existing) | **Already canon** | RV-01 does not override |
| `production_stack` (tokens → components → sections → templates → content) | RV-02 | **B** | Reference architecture label |
| `canonical_asset` vs `editorial_instance` | RV-02 | **B** | Maps to blueprint vs workspace instance |
| `pixel_factory_pipeline` (orchestration loop) | RV-03 | **C** (WF-A03) | Vocabulary only in Reference Library until WF-A03 charter |

### Validation terms

| Candidate | Source | Tier | Relation to existing canon |
|-----------|--------|------|---------------------------|
| `page_reality` vs `serp_reality` | RV-01 | **A** | Feeds WF-R01.5; FAQ rich result = obsolete tactic |
| `visual_baseline` / `render_diff` | RV-03 | **C** | WF-A02 explicit non-goal; WF-A03 deferred |
| `failure_class` (asset, component, text, ordering, layout, responsive, render drift) | RV-03 | **B** | Crosswalk to VL3 prefixes + FP-0002 — Reference Library |
| `COMPOSITION_VALIDATED` / VL3 domains | WF-A02 (existing) | **Already canon** | RV-03 aligns, does not replace |

### Composition terms

| Candidate | Source | Tier | Foundry status |
|-----------|--------|------|----------------|
| `commercial_pattern` (pattern_id layer) | RV-01 | **A** | Weak in repo (~1 pattern); WF-R01.4 target |
| `trust_pattern` (segment stacks: B2B, B2C, manufacturing, services, ecommerce) | RV-01 | **A** | Largest vocabulary gap per RV-01 |
| `hero` ≠ `header_nav` (shell separation) | RV-01 + layout-shell-governance | **A** | Already in repo governance; RV-01 reinforces |
| `section` / `block` / `module` / `pattern` disambiguation glossary | RV-01 + RV-02 | **B** | Reduce v0/v1 naming drift |

### Frontend terms

| Candidate | Source | Tier | Notes |
|-----------|--------|------|-------|
| Core block primitives: HEADER_NAV, FOOTER, SEARCH, FILTERS, BREADCRUMBS, PAGINATION, CARD_GRID, DETAIL_SPECS | RV-01 | **A** (vocabulary) | Registry IDs → WF-R01.2 only |
| Common blocks: FAQ, TESTIMONIALS, PRICING_TABLE, PROCESS_STEPS, RELATED_ITEMS | RV-01 | **B** | Many exist in v1 under different ids |
| `context_dependent` (search/filters/breadcrumbs required by site type) | RV-01 | **A** | Feeds SITE-TYPE-BLOCK-MATRIX semantics |

### Project terms

| Candidate | Source | Tier | Notes |
|-----------|--------|------|-------|
| Core site types (12-class minimal list) | RV-01 | **B** | v1 has 8 codes — mapping not 1:1; WF-R01.8 feed |
| Core page types (+pricing, blog_listing, search_results, location, policy, 404) | RV-01 | **A** (vocabulary) | PAGE-TYPE-REGISTRY-v1 has 10 — gap analysis input for R01.6 |
| `seo_surface` (product, category, service, location, article, case study, comparison, resource/pillar) | RV-01 | **B** | seo-architecture v2 partial coverage |
| Vertical site types (real estate, restaurant, …) | RV-01 | **C** | Expansion backlog only |

---

## Website Production Systems Findings

Сопоставление мировой практики (RV-02) с **документированным** состоянием FOUNDRY (audits + charters). **Не** утверждение runtime.

### Уже существует в Foundry (documented)

| World practice element | Foundry evidence | Maturity |
|------------------------|------------------|----------|
| Template-first delivery | Blueprint Layer v1, PAGE-TYPE-REGISTRY, Core 5 blueprints ACCEPTED | **Strong (doc)** |
| Block/section authoring surface (human) | Block Registry v1 (29 ids), reference partials (9), Gulp sections, Wave 4–6 extraction discipline | **Partial (impl)** |
| Production modes fidelity contract | WF-A01 `PIXEL_PERFECT` / `TEMPLATE_ART` | **Canon** |
| Validation layer chain | WF-A02 VL0–VL6, VL3a–f domains | **Canon (doc)** |
| Page architecture / IA | PAGE-TYPE-REGISTRY, SITE-TYPE-MATRIX, blueprints | **Strong (doc)** |
| SEO architecture (intent, contracts) | seo-architecture v2 ACCEPTED | **Strong (doc)** / weak content templates |
| Frontend production methodology | Waves 1–6, shell-first, grid/layout discipline, Forge overlay | **Strong (ops)** |
| Human governance (HITL, approval, freeze) | execution-semantics, operator-visual-approval-law, freeze-discipline | **Strong (doc)** |
| Blueprint/schema specification (doc) | BLOCK-CONTRACT, blueprint contracts, page-block-validation | **Strong (doc)** |
| Design-system architecture (doc) | design-system layer ACCEPTED; tokens implementation OPEN | **Architecture only** |
| Semantic relationship model (doc) | Semantic Relationship Layer v0 | **Doc only** |
| Artifact bus / validation runtime model (doc) | Phase 4 layers | **Doc only** |

### Отсутствует или слабо

| World practice element | Gap severity | RV source |
|------------------------|--------------|-----------|
| Unified vocabulary families (no level mixing) | **Critical** | RV-01 |
| Structural blocks in registry (HEADER_NAV, FILTERS, SEARCH) | **Critical** | RV-01 + audits |
| Trust pattern catalog | **High** | RV-01 |
| Commercial pattern library (≥4 patterns) | **High** | RV-01 + registry audit |
| Structured content models (schema ↔ entries) | **High** | RV-02 |
| Content relationships (reference, taxonomy) | **High** | RV-02 |
| Cross-project shared asset library (governed) | **Medium** | RV-02 |
| Design token operational SSOT | **Medium** | RV-02 |
| Component API (props/variants/slots) formal layer | **Medium** | RV-02 |
| Lifecycle governance per registry object | **Medium** | RV-02 |
| Reference implementation coverage (~31%) | **High** | Audits |
| v0↔v1 dual canon operational binding | **Critical** | Audits; WF-R01.1 ACCEPTED, B3–B8 pending |

### Принять (as canon direction, not implementation)

| Decision | Rationale |
|----------|-----------|
| **Registry family hierarchy** as vocabulary law | RV-01 + RV-02 convergence; stops ambiguous IDs |
| **Structural-before-marketing** expansion order | Audits Rank #3; Template-Art catalog honesty |
| **Trust + commercial pattern** as separate registry families | RV-01; WF-R01.4 program already scoped |
| **Minimal canon first** + explicit expansion backlog | Prevents vertical exotica dilution |
| **Page vs SERP separation** in SEO vocabulary | RV-01 Google deprecation facts |
| **Production stack** as reference architecture diagram | RV-02; aligns layer-map without new runtime |
| **Governance-before-scale** principle | RV-02; supports WF-R01.1 cutover discipline |

### Отклонить (for current Foundry canon)

| Proposal | Reject reason |
|----------|---------------|
| Unlimited canvas / single universal editor | Contradicts Factory blueprint + mode contracts |
| Marketplace / plugin ecosystem as near-term goal | RV-02 explicit; scope creep |
| Full CMS entity engine in v1 | RV-02; semantic layer v0 sufficient as doc |
| One-shot AI codegen as SSOT path | RV-03; FP-0002 false-green evidence |
| PNG-first vision pipeline as primary | RV-03; lower fidelity, higher HITL cost |
| Copying any single vendor's UX/model | RV-02 recommendation: extract invariants only |
| FAQ rich result as SEO promise | RV-01 obsolete tactic |

---

## Pixel Factory Findings

Отдельная зона: **WF-A03 Pixel Factory Expansion** ([roadmap.md](../projects/mars-website-factory/roadmap.md) — **DEFERRED**). Содержимое RV-03 **не должно** входить в текущий Foundry Registry/Vocabulary canon.

### Относится к WF-A03 (defer)

| RV-03 finding | WF-A03 scope item | Canon entry |
|---------------|-------------------|-------------|
| Orchestration loop (ingest→…→merge) | Pixel Factory orchestration layer | **Forbidden** until WF-A03 charter |
| Figma-native deterministic extraction lane | Vision / extraction layer | **Deferred** |
| PNG/vision secondary lane | Vision Layer | **Deferred** |
| Component mapping to codebase (automated) | Agent / mapping runtime | **Deferred** |
| Render lab + multi-width capture | Screenshot Engine | **Deferred** |
| Baseline diff engine (pixel/render) | Visual Diff / Pixel QA Runtime | **Deferred** |
| Automated autofix / repair loop | Agent Runtime | **Deferred** |
| Percy/Chromatic-class review automation | Pixel QA Runtime | **Deferred** |

### Может жить в Reference Library сейчас (не canon)

| Item | Purpose |
|------|---------|
| Failure class taxonomy (RV-03 § Failure Classes) | Crosswalk to VL3 + FP-0002 investigation |
| HITL checkpoint model (mapping, approval, spatial fix) | Operator training; aligns with existing laws |
| Tool landscape survey (Builder, Locofy, Anima, v0, …) | External research citation only |
| Industry QA tool patterns (Playwright, BackstopJS, …) | [visual-regression-workflow-v1.md](../projects/mars-website-factory/visual-regression-workflow-v1.md) already exists at doc level |

### Пересечение с текущим canon (уже есть — не дублировать в WF-A03)

| Existing Foundry canon | RV-03 overlap |
|------------------------|---------------|
| WF-A01 `PIXEL_PERFECT` mode contract | Defines *when* pixel fidelity applies |
| VL3 domains (IR, AI, VO, TL, AD) | Composition truth **before** codegen |
| pixel-fidelity-audit-rules-v1, design-source mapping governance | Human-operated fidelity gates |
| operator-visual-approval-law | Human approval gate |
| FP-0002 forensic failure classes | Proven escape patterns |

**Rule:** RV-03 **informs** WF-A03 charter draft later; **does not** authorize Vision Runtime or registry changes now.

---

## Canon Impact Matrix

| ID | Finding / artifact | Tier | Target canon home | Consumer subprogram |
|----|-------------------|------|-------------------|---------------------|
| C-01 | Registry family hierarchy | **A — Must Adopt** | Vocabulary Canon Charter (new, WF-R01.0 output) | WF-R01.1 binding glossaries; all R01.x |
| C-02 | minimal_canon + expansion_backlog rule | **A** | Vocabulary Canon Charter | WF-R01.2, R01.7, R01.8 |
| C-03 | standard/common/specialized/obsolete attribute | **A** | Vocabulary Canon Charter | WF-R01.6 hygiene |
| C-04 | Structural-before-marketing priority | **A** | Vocabulary Canon + reinforces R01.2 design | WF-R01.2, R01.3 |
| C-05 | Trust pattern family definition | **A** | Vocabulary Canon | WF-R01.4 (partial overlap) |
| C-06 | Commercial pattern family (distinct from blocks) | **A** | Vocabulary Canon | WF-R01.4 |
| C-07 | page_reality ≠ serp_reality | **A** | Vocabulary Canon + SEO slice | WF-R01.5 |
| C-08 | FAQ rich result obsolete (2026) | **A** | SEO Reference note | WF-R01.5 |
| C-09 | Core page type vocabulary gaps (pricing, blog_listing, search_results, …) | **A** (vocabulary) | PAGE-TYPE glossary annex | WF-R01.6 |
| C-10 | HEADER_NAV / SEARCH / FILTERS as vocabulary primitives | **A** (terms) | Structural vocabulary annex | WF-R01.2 (**not** new IDs here) |
| C-11 | Production stack 5-layer reference model | **B — Recommended** | Reference Library + layer-map cross-link | Architecture docs only |
| C-12 | canonical_asset vs editorial_instance | **B** | Reference Library | Blueprint / workspace discipline |
| C-13 | Governance lifecycle states (draft→stable→deprecated) | **B** | Reference Library | WF-R01.6, block-quality-tiers |
| C-14 | RV-03 failure class ↔ VL3 crosswalk | **B** | Reference Library | Validation ops, FP-0002 |
| C-15 | Extended vertical site types list | **C — Reference Only** | Research artifact | WF-R01.8 feed |
| C-16 | Rare ecommerce blocks (countdown, stock counter, …) | **C** | Research artifact | Future vertical charters |
| C-17 | Structured content models + relationships (full) | **C** (for now) | Research + semantic layer v0 pointer | Post–WF-R01 program |
| C-18 | Cross-project design libraries | **C** | Research artifact | Wave 6+ planning |
| C-19 | Pixel Factory orchestration pipeline | **C** | Research artifact → WF-A03 only | WF-A03 (deferred) |
| C-20 | Agentic codegen tools (v0, Lovable, Stitch) | **C** | Research artifact | WF-A03 evaluation input |

**Tier A adoption path:** publish **Foundry Vocabulary Canon Charter v1** (proposed WF-R01.0 deliverable phase 2) — **terminology and family rules only**, zero registry rows.

---

## Roadmap Impact

**Не менять roadmap.** Рекомендации — только cross-link citations при будущих editorial passes.

| Roadmap / program item | Recommended research link | Rationale |
|---------------------|---------------------------|-----------|
| **WF-R01** program charter + design | RV-01 (primary), RV-02 § Governance | Vocabulary normalization authority |
| **WF-R01.1** v0→v1 binding | RV-01 § Recommendations (family structure) | Terminology harmonization |
| **WF-R01.2** Structural Blocks | RV-01 § Block Vocabulary Core + Industry Canon | Replace proxy-only evidence note |
| **WF-R01.3** Reference Implementation Expansion | RV-01 structural priority | Prioritize partials order |
| **WF-R01.4** Commercial Pattern Library v0 | RV-01 § Commercial Patterns | Pattern catalog source list |
| **WF-R01.5** SEO Content Pattern Slice | RV-01 § SEO Content Patterns + deprecations | Page vs SERP rules |
| **WF-R01.6** Registry Hygiene | RV-01 family rules + RV-02 lifecycle | Role mapping completeness |
| **WF-R01.7** Template-Art Multi-Site-Type | RV-01 site/page matrices | Readiness matrix evidence |
| **WF-R01.8** Execution Case Feed | RV-01 vertical gaps | Lesson → vocabulary backlog |
| **WF-A01** Production Modes | RV-03 § HITL (reference only) | PIXEL_PERFECT pipeline context |
| **WF-A02** Validation Architecture | RV-03 failure classes (crosswalk doc) | VL3 alignment |
| **WF-A03** (when opened) | RV-03 (full artifact as primary SoT) | Operator reminder already requires research refresh |
| **Phase 2** Registries and contracts | RV-01 Vocabulary Registry Draft | Historical phase alignment |
| **OPERATIONAL-INDEX** Core Run | WF-R01.0 + research index row | Discoverability |

**Suggested index row (future editorial pass, not this task):**  
`Research Canon (RV-01–03)` → `research/foundry/` + `wf-r01-0-research-canon-integration-design-v1.md`

---

## Authority Model

### Tier definitions

| Authority class | Role | Mutability |
|-----------------|------|------------|
| **Research Artifact** | External/industry evidence, citations, provisional gap tables | Immutable snapshot; new version = new file |
| **Canonical Charter** | Binding rules operators must follow | Human sign-off; versioned |
| **Reference Library** | Non-binding patterns, crosswalks, architecture diagrams | Updated by charter pass |

### SoT assignment per research output

| Content domain | SoT class | Primary location (proposed) |
|----------------|-----------|----------------------------|
| Industry site/page/block lists | **Research Artifact** | `research/foundry/rv-01-production-vocabulary.md` |
| Vocabulary **family rules** + minimal canon policy | **Canonical Charter** (future) | `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` (**not created in this pass**) |
| Registry `site_type_code` / `block_id` rows | **Canonical Charter** (existing) | SITE-TYPE-REGISTRY-v1, BLOCK-REGISTRY-v1 + WF-R01.1 |
| Structural block **definitions** (pre-ID) | **Reference Library** until R01.2 ACCEPTED | `reports/wf-r01-2-structural-blocks-program-design-v1.md` |
| Production stack diagram | **Reference Library** | New: `projects/mars-website-factory/reference/production-systems-stack-v1.md` (**proposed**, not created) |
| Trust/commercial **pattern catalog content** | **Canonical Charter** (future) | WF-R01.4 deliverable |
| SEO page vs SERP rules | **Canonical Charter** (future) | WF-R01.5 + seo-architecture v2 |
| Pixel pipeline / tool survey | **Research Artifact** | `research/foundry/rv-03-pixel-factory.md` |
| Failure class crosswalk | **Reference Library** | `projects/mars-website-factory/reference/rv03-vl3-failure-crosswalk-v1.md` (**proposed**, not created) |
| WF-R01.0 integration decisions | **Canonical Charter** (program design) | **This document** |

### Authority flow (target state)

```text
Research Artifacts (RV-01, RV-02, RV-03)
        │
        ▼  synthesis + tiering (WF-R01.0)
        │
   ┌────┴────┐
   ▼         ▼
Vocabulary    Reference Library
Canon         (stack, crosswalks, industry tables)
Charter
   │
   ▼  feeds (no auto-promotion)
WF-R01.1–R01.8 subprogram charters
   │
   ▼
Registry rows / blueprints / ops index
```

**Hard rule:** Research Artifact **never** auto-promotes to registry row. Promotion path: WF-R01.0 tier A → Vocabulary Canon Charter → subprogram charter ACCEPTED → registry edit pass.

---

## Risks

| Risk | Severity | Mitigation (WF-R01.0 program) |
|------|----------|-------------------------------|
| **Research Canon ≠ Foundry Canon** drift continues | High | Publish authority model; tier matrix; link RV files from WF-R01.x |
| **Over-absorption** — copying full RV tables into registry | High | Tier A = rules only; rows stay in R01.2+ gated passes |
| **WF-A03 scope creep** via RV-03 | High | Explicit defer table; roadmap start conditions unchanged |
| **False Already Exists** from RV-01 provisional status | Medium | Require registry verification pass before STATUS claims |
| **Duplicate vocabulary** (pattern vs block vs seo surface) | Medium | Family hierarchy charter before new IDs |
| **RV-02 stack mistaken for runtime roadmap** | Medium | Reference Library labeling + honesty boundary |
| **Stale research** (Google FAQ deprecation, tools) | Medium | WF-A03 operator rule: refresh pass before A03; date stamps on RV files |
| **R01.2 design built on proxy without RV citation** | Low (closing) | Update R01.2 research note on next editorial pass |

---

## SAFE UNKNOWN

| Unknown | What would verify |
|---------|-------------------|
| Named **vocabulary steward** for canon charter | Human governance assignment |
| Exact 1:1 mapping RV-01 site types → v1 `site_type_code` (8 codes) | WF-R01.8 + mapping workshop |
| Whether `page_type` registry needs expansion rows vs glossary-only | WF-R01.6 hygiene charter |
| BREADCRUMBS / PAGINATION as `block_id` vs layout-component policy | WF-R01.2 operator decision |
| Depth of structured-data terminology in vocabulary canon | WF-R01.5 + SEO architecture owners |
| Operational pages (login, account, registration) in v1 scope | WF-R01.7 Template-Art charter |
| Live registry dump confirming RV-01 Partial/Missing counts | Registry audit re-run post–R01.1 B3 |
| Triumph v6 / OCPilot lessons formally indexed to RV vocabulary | WF-R01.8 execution feed |
| Timeline for **Foundry Vocabulary Canon Charter v1** publication | Human charter schedule |

---

## Recommended Next Step

1. **Human review** of this WF-R01.0 design — confirm Tier A set and authority model.
2. **Charter pass (separate task):** draft `foundry-vocabulary-canon-charter-v1.md` — Tier A rules only, **no registry IDs**.
3. **Reference Library pass (optional, parallel):** `production-systems-stack-v1.md` + `rv03-vl3-failure-crosswalk-v1.md` — Tier B, non-blocking.
4. **Editorial cross-links only:** add RV citations to WF-R01.2 design § Industry Canon and program design research section (human-approved micro-edit).
5. **Do not start:** WF-R01.2 implementation, new block_ids, WF-A03, registry file edits.

**WF-R01.0 program exit criterion (proposed):** Vocabulary Canon Charter v1 **ACCEPTED** + authority model registered in OPERATIONAL-INDEX + RV-01–03 cited from WF-R01 program charter.

---

*Design artifact: `reports/wf-r01-0-research-canon-integration-design-v1.md`*
