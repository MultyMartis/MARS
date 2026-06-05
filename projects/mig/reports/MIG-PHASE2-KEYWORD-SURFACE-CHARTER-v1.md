# MIG Phase 2 — Keyword Surface Intelligence Charter v1

**Status:** **charter** — architecture and planning only  
**Date:** 2026-06-06  
**Lane:** A — MIG Phase 2 Planning  
**Phase:** 2 — Keyword Surface Intelligence (Demand Surface)  
**Prior phase:** MIG MVP **COMPLETE** — [MIG-MVP-VALIDATION-FREEZE-v1.md](MIG-MVP-VALIDATION-FREEZE-v1.md)  
**Related (normative design, not superseded):** [../contracts/mig-keyword-intelligence-architecture-v1.md](../contracts/mig-keyword-intelligence-architecture-v1.md)  
**Validated market (Phase 1 evidence):** Грузотакси / Краснодар / проект Триумф

**This document delivers:** mission, scope, boundaries, Keyword Surface capability model, three-layer stack, evidence model, potential outputs, non-goals, readiness assessment, recommended next step.

**This document does not deliver:** runtime code, acquisition modules, Wordstat implementation, external API integration, ORCA semantics, SEO strategy, or Phase 1 redesign.

---

## Canonical boundary (normative)

> **MIG acquires reality. ORCA interprets reality.**

Phase 2 planning extends MIG from **Market Surface** (who appears in search) toward **Demand Surface** (what users search for) — **without** crossing into interpretation, strategy, or autonomous decisions.

---

## Mission

### What Phase 1 proved

MIG MVP answers:

> **What appears on the search results surface for declared queries, and what do acquired competitor pages show?**

Evidence: four validated sessions on Грузотакси Краснодар — SERP Acquisition, Competitor Discovery, Multi-Query Discovery, Website Acquisition, Landing Analysis v2, Comparison Matrix, Research Pack draft. See [MIG-MVP-VALIDATION-FREEZE-v1.md](MIG-MVP-VALIDATION-FREEZE-v1.md).

Phase 1 **Market Surface** is **supply-side visibility**: domains, entities, recurrence, landing facts — all grounded in captured SERP and HTTP snapshots.

### What Phase 2 must explore

MIG Phase 2 planning defines how MIG should understand **Demand Surface**:

> **What query language, modifiers, and demand signals were observable at capture time — independent of who ranked for them?**

Demand Surface is **not** «what should we target» (ORCA). It is the **structured record of search-demand evidence** that complements Market Surface without duplicating it.

### Phase 2 charter phase vs future implementation

| Gate | Content | Status in this charter |
|------|---------|------------------------|
| **Phase 2a — Planning (this document)** | Capability model, layer boundaries, evidence taxonomy, output sketches | **In scope** |
| **Phase 2b — Design contracts** | Schema stubs, pack section ids, manifest flags | **Next gate — not this charter** |
| **Phase 2c — Acquisition implementation** | Ingest adapters, registry writers, verify scripts | **Explicitly out of scope** |

**Normative:** Wordstat runtime, suggestion API clients, and external integrations are **not authorized** by this charter. They may appear only as **capability placeholders** in the model below.

---

## Scope

### In scope (Phase 2 planning)

| # | Work area | Boundary |
|---|-----------|----------|
| 1 | **Keyword Surface layer definition** | Capability model — what MIG would observe, not how it is fetched |
| 2 | **Demand Surface vs Market Surface** | Clear semantic split; no overlap with competitor/entity discovery |
| 3 | **Three-layer stack** | Keyword Surface → Market Surface → Website Intelligence |
| 4 | **Evidence model** | Keyword, demand, modifier, intent, frequency, trend evidence types with SAFE UNKNOWN discipline |
| 5 | **Potential outputs** | Draft artifact names only — no final schema lock-in |
| 6 | **Non-goals** | Explicit exclusions for ORCA, SEO, campaigns, Deep Research, runtime |
| 7 | **Readiness assessment** | Evidence-backed answer: may Phase 2 planning begin? |

### Out of scope (this charter and Phase 2a)

| Item | Reason |
|------|--------|
| Runtime / `run-mig-session.js` changes | Implementation gate |
| SERP re-fetch, Playwright, HTTP acquisition | Phase 1 proven path — frozen |
| Wordstat UI automation, API clients, CSV ingest | Acquisition — deferred |
| External suggestion/autocomplete APIs | Integration — deferred |
| JSON Schema registry files | Design gate |
| n8n graph changes | Operational gate |
| ORCA handoff bundle changes | Downstream consumer |
| Phase 1 artifact redesign | Freeze honored |

### Relationship to existing Keyword Intelligence architecture

[../contracts/mig-keyword-intelligence-architecture-v1.md](../contracts/mig-keyword-intelligence-architecture-v1.md) describes the **full acquisition channel** (registry, Wordstat snapshot shape, n8n hooks). **This charter narrows the immediate program:**

- Phase 2 **starts** with **architecture and capability boundaries** for Demand Surface.
- Implementation items in Keyword Intelligence §10.2 remain **future gates** — not authorized until a separate design/readiness decision.

---

## Boundaries

### Three-layer stack (normative)

```text
┌─────────────────────────────────────────────────────────────┐
│  KEYWORD SURFACE (Demand Surface)          ← Phase 2 focus  │
│  Observable query language, modifiers, demand signals       │
└───────────────────────────┬─────────────────────────────────┘
                            │ informs seed/query selection;
                            │ does NOT replace SERP capture
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  MARKET SURFACE (Supply Surface)           ← Phase 1 proven │
│  SERP entities, domains, recurrence, aggregators            │
└───────────────────────────┬─────────────────────────────────┘
                            │ shortlist drives acquisition;
                            │ does NOT interpret landing copy
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  WEBSITE INTELLIGENCE                      ← Phase 1 proven │
│  Snapshots, landing observations, comparison matrix         │
└─────────────────────────────────────────────────────────────┘
```

### Layer ownership matrix

| Concern | Keyword Surface | Market Surface | Website Intelligence |
|---------|-----------------|----------------|----------------------|
| **Primary question** | What phrases/modifiers/demand signals exist? | Who appears for which queries? | What do acquired pages show? |
| **Primary inputs** | Seeds, suggestions, related searches, Wordstat tables (future), operator imports | `serp_result.json`, multi-query index, competitor frequency | `website_snapshot.json`, landing observations |
| **Primary outputs** | Keyword registry, demand surface rollup, modifier/intent **drafts** | `competitors.json`, market-surface reports, shortlists | Comparison matrix, landing families, geo/phone/delivery flags |
| **Entity focus** | **Strings** (phrases) | **Domains / URLs / entities** | **Page-visible facts** |
| **Frequency / volume** | Raw signals as returned — **no interpretation** | Recurrence counts across queries — **structural only** | N/A (unless phrase appears on page) |
| **Clustering / intent labels** | **Forbidden** — draft surfaces only | **Forbidden** | **Forbidden** |
| **Ranking / strategy** | **Forbidden** | Shortlist ranking = recurrence evidence, not bid/SEO priority | Comparison columns = facts, not recommendations |

### Overlap prevention rules

| Rule | Detail |
|------|--------|
| **KS-01** | A **domain** or **competitor entity** belongs to **Market Surface** — never to Keyword Surface as primary object |
| **KS-02** | A **phrase** on a landing (title, H1) is **Website Intelligence** when sourced from snapshot; Keyword Surface may **reference** the same string only via cross-layer link with distinct `source_type` |
| **KS-03** | **Executed queries** in multi-query discovery are shared metadata — Market Surface owns **SERP outcome**; Keyword Surface owns **query string as demand evidence** |
| **KS-04** | **Related searches** on SERP: string → Keyword Surface; **clickable result URLs** → Market Surface |
| **KS-05** | **Comparison matrix** and **landing observations** remain Phase 1 artifacts — Phase 2 does not add keyword columns without separate charter |
| **KS-06** | **SAFE UNKNOWN** at each layer — missing demand data must not be inferred from market recurrence or landing copy |

### Upstream / downstream (planning)

| Direction | Relationship |
|-----------|--------------|
| **Research Request** | Supplies `queries.seed_queries[]` — primary demand anchor (Phase 1) |
| **Keyword Surface → Market Surface** | Expanded or refined query sets may **inform** future SERP runs — human-approved request only; no auto-expansion in MIG |
| **Market Surface → Website Intelligence** | Unchanged Phase 1 path: shortlist → acquisition → landing pass |
| **All layers → Research Pack** | Projections only; layer artifacts remain SoT per layer |
| **Research Pack → ORCA** | **Out of Phase 2 scope** — human approval required |

---

## Keyword Surface — capability model

**Definition:** Keyword Surface is the MIG layer that records **observable search-demand language** — phrases, modifiers, and attached numeric or ordinal signals — at capture time, without clustering, prioritization, or strategy.

### Capability categories (architecture only)

Each category is a **planned observation channel**. None are implemented by this charter.

#### 1. Seed and executed query registry

| Capability | Description | Phase 1 baseline | Phase 2 planning |
|------------|-------------|------------------|------------------|
| **Declared seeds** | Exact strings from Research Request | **Proven** — Query Set in pack | Formalize as demand evidence objects |
| **Executed queries** | Strings actually run in SERP capture | **Proven** — manifest `queries_executed` | Link to demand surface without duplicating SERP entities |

#### 2. Wordstat (placeholder — no implementation)

| Capability | Description | Status |
|------------|-------------|--------|
| **Frequency tables** | Shows, clicks, share as returned by provider | **Not captured** — `keyword_pass: false` in all MVP manifests |
| **Region-scoped demand** | Numeric signals per phrase + region | **Architecture placeholder** — manual export path evaluated in Keyword Intelligence v1; **not authorized here** |
| **Trend columns** | Period-over-period if present in export | **SAFE UNKNOWN** until capture method chartered |

**Normative:** Wordstat is a **named capability** in the model. **No** runtime, API, browser automation, or ingest adapter in Phase 2a.

#### 3. Search suggestions (placeholder)

| Capability | Description | Examples (Грузотакси pilot) |
|------------|-------------|----------------------------|
| **Autocomplete strings** | Ordered/unordered lists per seed + engine | «грузотакси краснодар недорого», «грузотакси краснодар цены» |
| **Single-depth rule** | No recursive expansion | Architecture constraint from Keyword Intelligence KI-03 |

#### 4. Related searches (placeholder)

| Capability | Description | Source |
|------------|-------------|--------|
| **SERP-visible refinements** | Strings shown in «people also search» blocks | Extract from captured SERP when present — **not re-fetched** |
| **Distinct from Market Surface** | Strings only — not result URLs | KS-04 |

#### 5. Modifier surfaces (taxonomy — draft)

Modifiers are **observable token patterns** attached to phrases — **not** interpreted intent classes.

| Modifier type | Description | Example tokens (pilot market) |
|---------------|-------------|-------------------------------|
| **Geo modifiers** | City, district, region tokens | «краснодар», «по краснодару» |
| **Service modifiers** | Service variant wording | «газель», «с грузчиками», «грузоперевозки» |
| **Commercial modifiers** | Price/cost/order language | «цена», «недорого», «заказать» |
| **Demand modifiers** | Urgency, scope, vehicle class | «срочно», «мебель», «квартира» — **observed in query set only** |
| **Intent modifiers** | Question / informational shape | «сколько стоит», «как заказать» — **shape only, no intent enum in MIG** |
| **Question modifiers** | Interrogative phrasing | «где», «сколько», «как» — lexical flag, not ORCA intent |

**Rule:** Modifier tags are **extracted or operator-declared observations**. Assigning «commercial intent» or «navigational» is **ORCA**.

#### 6. Cross-layer phrase channels (reference only)

| Channel | Owner | Notes |
|---------|-------|-------|
| **SERP organic titles/snippets** | Keyword Surface (string) + Market Surface (URL/position) | Dual provenance — KS-04 |
| **Page-visible phrases** | Website Intelligence primary | Keyword Surface may index with `source_type: page_visible` when chartered |
| **Ad headlines** | Market Surface (ad block) + optional string rollup | MVP: optional stub |

### Forbidden Keyword Surface capabilities (all Phase 2 planning)

| Forbidden | Owner |
|-----------|-------|
| Semantic clustering, «themes», head/tail classification | ORCA |
| Keyword prioritization for campaigns | ORCA |
| Query **generation** or auto-expansion inside MIG | Forbidden |
| Volume-based recommendations | ORCA |
| PPC / SEO structure | ORCA |
| Autonomous query execution | Forbidden — human request scope |

---

## Evidence model

Phase 2 planning adopts **layer-specific evidence types**. Each type records **what was observed**, **from where**, **when**, and **what is unknown**.

### Evidence type taxonomy

| Evidence type | Layer | Description | MVP status |
|---------------|-------|-------------|------------|
| **keyword_evidence** | Keyword Surface | Exact phrase string + provenance (seed, suggestion, related, wordstat row, page_visible) | Partial — seeds/executed in manifest only |
| **demand_evidence** | Keyword Surface | Composite: phrase + optional frequency + region + period | **Not captured** |
| **modifier_evidence** | Keyword Surface | Token or pattern attachment to a phrase — lexical, not semantic | **Not modeled** |
| **intent_evidence** | Keyword Surface | **Shape observations only** (question form, commercial token presence) — **not** intent classification | **Not modeled** |
| **frequency_evidence** | Keyword Surface | Raw numeric signal (shows, clicks, share) as returned | **Not captured** |
| **trend_evidence** | Keyword Surface | Time-series or period comparison if provider supplies columns | **SAFE UNKNOWN** |

### Evidence object fields (logical — no schema file)

| Field | Required | Meaning |
|-------|----------|---------|
| `evidence_id` | Yes | Stable within session |
| `evidence_type` | Yes | One of taxonomy above |
| `phrase` | When applicable | Exact captured string |
| `source_channel` | Yes | `seed`, `serp_executed`, `serp_related`, `suggestion`, `wordstat`, `page_visible`, `operator` |
| `capture_time` | Yes | ISO-8601 UTC |
| `region` / `locale` | Optional | Align with `scope.region` |
| `signal` | Optional | Raw frequency or trend payload — **uninterpreted** |
| `artifact_refs` | Yes | Pointers to SoT artifacts |
| `evidence_grade` | Yes | `operator` \| `provider` \| `extracted` |
| `safe_unknown` | Yes | Array — may be empty |

### SAFE UNKNOWN discipline (normative)

| Situation | Declaration |
|-----------|-------------|
| Keyword pass not run | «Search demand surface not captured — Keyword Surface pass not executed» |
| Wordstat not ingested | «Frequency evidence not captured for this session» |
| Suggestions not captured | «Autocomplete suggestion surface not captured» |
| Related searches absent on SERP | «SERP related-search block not present or not extracted» |
| Modifier extraction not run | «Modifier surface not derived — lexical modifiers unknown» |
| Trend columns missing | «Trend evidence not present in source export» |
| Region mismatch (future Wordstat) | «Demand region (X) ≠ scope.region (Y) — operator verification required» |

**Rules:**

1. **Never** infer frequency from SERP recurrence or landing prominence.
2. **Never** treat missing Wordstat as zero volume.
3. **Never** fill intent_evidence with ORCA intent enums.
4. Session-level and object-level `safe_unknown` **must** be explicit in pack projections when Phase 2 artifacts exist.

### Evidence vs interpretation

| Observation (MIG) | Interpretation (ORCA — excluded) |
|-------------------|----------------------------------|
| Phrase «грузотакси краснодар» with shows=12400 | «High-volume commercial head term» |
| Modifier token «недорого» on phrase | «Price-sensitive segment» |
| Related search string appears 12 times across exports | «Demand theme for content cluster» |
| Question form «сколько стоит грузотакси» | «Informational intent → FAQ page» |

---

## Outputs

**Potential artifacts only** — names and purpose sketches. **No final schema decisions** in this charter.

### Primary artifacts (Keyword Surface — future)

| Artifact (draft name) | Purpose | SoT role |
|-----------------------|---------|----------|
| `keyword_registry.json` | Canonical index of phrase evidence objects | **SoT** when pass exists |
| `keyword_surface.json` | Rollup by `surface_type` — convenience view | Optional; registry wins |
| `demand_surface_report.md` | Human-readable demand surface summary | Projection |
| `wordstat_snapshot.json` | Raw frequency table snapshot | SoT for Wordstat channel — **future** |
| `suggestions_snapshot.json` | Per-invocation suggestion list | SoT for suggestion channel — **future** |

### Draft projection surfaces (not clusters)

| Output (draft name) | Content sketch | Forbidden content |
|--------------------|----------------|-------------------|
| **Demand Surface Report** | Phrase counts by source channel; region/period statement; SAFE UNKNOWN block | Ranked «top keywords», strategy bullets |
| **Keyword Cluster Draft** | **Provisional groupings by shared tokens** — labeled `draft_unvalidated` | ORCA-ready clusters, campaign groups |
| **Intent Surface Draft** | Lexical shape flags (question, commercial token) per phrase | Intent taxonomy, funnel stage |
| **Modifier Surface Draft** | Geo/service/commercial token attachments | Persona labels, segment strategy |

### Research Pack sections (future projection ids)

Align with [../contracts/mig-keyword-intelligence-architecture-v1.md](../contracts/mig-keyword-intelligence-architecture-v1.md) §7 — to be activated only when Keyword Surface pass is chartered:

| Section id | When populated |
|------------|----------------|
| `keyword_observations` | Keyword Surface pass executed |
| `search_demand` | Any frequency evidence present |
| `frequency_signals` | Wordstat or numeric provider snapshot present |

**MVP today:** Query Set section only; demand gaps in SAFE UNKNOWN — unchanged.

### Operator-facing reports (optional)

| Report | Layer |
|--------|-------|
| `demand-surface-report.md` | Keyword Surface |
| `market-surface-report.md` | Market Surface — **exists** in pilot (`incoming/mig/pilots/triumph-gruzotaxi-krasnodar/`) |
| `market-leader-comparison-matrix.md` | Website Intelligence — **proven** |

---

## Non-Goals

Explicit exclusions for Phase 2 planning and all immediate follow-on until separately chartered:

| Non-goal | Rationale |
|----------|-----------|
| **SEO strategy** | ORCA / downstream — not acquisition |
| **ORCA integration** | Consumer of approved packs — no Phase 2 planning |
| **Campaign planning** | PPC structure, ad groups, bids — ORCA |
| **Content generation** | MetaBOT / Factory — external |
| **Deep Research** | Synthesis pass — separate architecture ([../contracts/mig-deep-research-architecture-v1.md](../contracts/mig-deep-research-architecture-v1.md)); not started in MVP |
| **Autonomous decisions** | Query expansion, auto re-run, unattended keyword capture — forbidden |
| **Wordstat runtime** | No API client, no browser bot, no CSV ingest in Phase 2a |
| **External APIs** | Suggestion APIs, third-party SEO APIs — not authorized |
| **Phase 1 redesign** | MVP freeze honored — [MIG-MVP-VALIDATION-FREEZE-v1.md](MIG-MVP-VALIDATION-FREEZE-v1.md) |
| **Intent clustering** | ORCA semantic work |
| **Keyword prioritization** | ORCA |
| **Production n8n deployment** | Operational gate — not planning |

---

## Readiness Assessment

### Question

**Is MIG Phase 1 sufficiently complete to begin planning Phase 2 (Keyword Surface Intelligence)?**

### Answer

**YES — with documented caveats.** Phase 1 MVP is **frozen and validated** on one market. Phase 2 **planning** (architecture only) may proceed without waiting for Wordstat, full query coverage, or ORCA.

### Evidence for readiness

| Criterion | Status | Evidence |
|-----------|--------|----------|
| End-to-end session spine proven | **Met** | Four sessions — freeze §Validated sessions |
| Market Surface operational | **Met** | Competitor discovery, multi-query, market-surface reports |
| Website Intelligence operational | **Met** | Landing v2, comparison matrix, geo/phone/delivery — freeze Validation Matrix |
| Query Set discipline exists | **Met** | `queries.seed_queries`, `queries_executed` in manifests — mqgt01 |
| Demand boundary honestly declared | **Met** | `keyword_pass: false`; SAFE UNKNOWN in freeze §Known Limitations |
| Phase 1 not blocked on keyword work | **Met** | Freeze explicitly excludes keyword pass — Phase 2 is additive |
| Architectural predecessor document | **Met** | [mig-keyword-intelligence-architecture-v1.md](../contracts/mig-keyword-intelligence-architecture-v1.md) |
| ORCA boundary documented | **Met** | [../boundaries.md](../boundaries.md) |

### Caveats (do not block planning; block implementation gates)

| Caveat | Impact on Phase 2 |
|--------|-------------------|
| **Single validated market** (Грузотакси Краснодар) | Modifier taxonomy examples are pilot-scoped; generalization **UNKNOWN** |
| **Partial query coverage** (8/11 — q05–q07 failed) | Demand surface examples incomplete for furniture/move intents |
| **No keyword artifacts in evidence** | Phase 2 planning cannot be validated by replay — design-only until capture chartered |
| **No approved research pack** | Operator approval workflow not proven — affects future handoff, not planning |
| **Keyword Intelligence doc includes implementation roadmap** | Phase 2a charter **supersedes execution timeline** — implementation deferred |

### Confidence

| Area | Level | Basis |
|------|-------|-------|
| Phase 1 complete for stated MVP scope | **B** | Freeze confidence summary |
| Safe to plan Demand Surface architecture | **B+** | Clear gap (`keyword_pass: false`); boundaries exist |
| Safe to implement acquisition immediately | **N/A** | **Not authorized** by this charter |

---

## Recommended Next Step

1. **Human review** of this charter — confirm three-layer boundaries and non-goals.
2. **Phase 2b gate:** Draft `MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md` in `contracts/` — normative capability ids (KS-CAP-*) without schemas.
3. **Extend Research Pack contract** (design stub) — register `keyword_observations`, `search_demand`, `frequency_signals` section ids; no pack builder changes.
4. **Pilot demand vocabulary pass (manual, human-only):** Operator annotates mqgt01 query set with modifier tags — validates taxonomy on real phrases **without** runtime.
5. **Defer** Wordstat ingest, suggestion API, and `keyword_registry.json` schema until Phase 2b readiness decision.

**Stop condition:** If planning blurs into clustering, SEO recommendations, or ORCA semantics — **stop** and split work per [../boundaries.md](../boundaries.md).

---

## Architecture decisions (charter phase)

| ID | Decision | Rationale |
|----|----------|-----------|
| **P2-KS-01** | Phase 2 begins with **architecture only** | User charter; MVP freeze honored |
| **P2-KS-02** | **Demand Surface** is the Phase 2 mission frame | Distinguishes from Phase 1 Market Surface |
| **P2-KS-03** | Three layers: Keyword → Market → Website | No overlap — KS-01..KS-06 |
| **P2-KS-04** | Wordstat is **named capability**, not implementation | SAFE UNKNOWN until separate gate |
| **P2-KS-05** | Modifier/intent surfaces are **draft projections** | Prevents ORCA bleed |
| **P2-KS-06** | Keyword Intelligence v1 remains **reference**, not execution auth | Implementation explicitly deferred |

---

## Related documents

| Document | Role |
|----------|------|
| [MIG-MVP-VALIDATION-FREEZE-v1.md](MIG-MVP-VALIDATION-FREEZE-v1.md) | Phase 1 evidence |
| [../contracts/mig-keyword-intelligence-architecture-v1.md](../contracts/mig-keyword-intelligence-architecture-v1.md) | Acquisition channel design (future) |
| [../boundaries.md](../boundaries.md) | MIG vs ORCA |
| [../contracts/mig-research-pack-contract-v0.md](../contracts/mig-research-pack-contract-v0.md) | Pack projections |
| [../contracts/mig-multi-query-discovery-design-v0.md](../contracts/mig-multi-query-discovery-design-v0.md) | Executed query model |
| [../OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) | MIG index |

---

*MIG Phase 2 Keyword Surface Intelligence Charter v1 · 2026-06-06 · architecture only · no runtime*
