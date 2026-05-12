# MARS Website Factory — Semantic Relationship Layer v0 — Overview

**Status:** **documentation only** — **conceptual semantic architecture** for Website Factory. This layer defines **how meaning is attributed, inherited, propagated, invalidated, frozen, and checked** across artifacts and site structure. **Not** a graph database, **not** a vector / embedding engine, **not** a MARS runtime module, **not** an orchestration daemon, **not** an autonomous semantic reasoner.

**Version:** v0.

**Related:** [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md), [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [semantic-object-model-v0.md](semantic-object-model-v0.md), [cross-artifact-semantics-v0.md](cross-artifact-semantics-v0.md), [semantic-dependency-rules-v0.md](semantic-dependency-rules-v0.md), [semantic-inheritance-v0.md](semantic-inheritance-v0.md), [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md), [site-semantic-graph-v0.md](site-semantic-graph-v0.md), [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md), [semantic-qa-rules-v0.md](semantic-qa-rules-v0.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).

---

## 1. Purpose

Provide a **single vocabulary** for:

- **Semantic consistency** — agreed meaning of CTAs, trust, SEO intent, conversion goals, offers, geo, services, FAQs, proofs, navigation across stages.
- **Cross-artifact semantics** — how those meanings are carried from Blueprint through Design, Frontend, QA, and Delivery **as documented obligations**, not as automatic data sync.
- **Dependency semantics** — which semantic edits **should** trigger which downstream invalidations and QA resets (aligns with [dependency-invalidation-v0.md](dependency-invalidation-v0.md); this layer adds **semantic-class** granularity).
- **Inheritance and propagation** — how defaults flow **site → cluster → page → section → component** and where overrides are allowed ([semantic-inheritance-v0.md](semantic-inheritance-v0.md)).
- **Site-level semantic architecture** — conceptual view of neighborhoods, authority, and clusters ([site-semantic-graph-v0.md](site-semantic-graph-v0.md)).

---

## 2. Core definitions

### 2.1 Semantic object

A **semantic object** is a **documented unit of meaning** with stable identity in factory prose (e.g. primary `cta_object` for a page, `trust_object` for a block, `seo_intent` slice). It is **not** a database row unless an external system materializes one; in this repository it is **contract vocabulary** only. Canonical set: [semantic-object-model-v0.md](semantic-object-model-v0.md).

### 2.2 Semantic relationship

A **semantic relationship** is a **declared** link between two semantic objects or between a semantic object and an artifact scope (e.g. “this CTA **supports** this conversion goal”, “this FAQ **grounds** this service entity”). Relationships are **authored or cited in artifacts and REPORTs** — there is **no** in-repo engine that materializes or traverses them automatically.

### 2.3 Semantic inheritance

**Semantic inheritance** is the **defaulting discipline**: when a child scope (page, section, component) does not restate a semantic field, it **inherits** the parent’s stated meaning. Inheritance is **policy in documentation and prompts**, not runtime field resolution. See [semantic-inheritance-v0.md](semantic-inheritance-v0.md).

### 2.4 Semantic propagation

**Semantic propagation** is the **expected narrative consequence** of a change: which downstream artifacts **should be reviewed or re-authored** so that meaning stays aligned. Propagation is **declared explicitly** (REPORT, invalidation notes); it does **not** imply background synchronization. Distinct from **inheritance** (defaults) and from **invalidation** (staleness declarations per [dependency-invalidation-v0.md](dependency-invalidation-v0.md)).

### 2.5 Semantic invalidation

**Semantic invalidation** is the **subset of invalidation** tied to meaning: when a semantic object changes, dependent QA lanes, approvals, and artifact revisions become **stale** for the affected scope. Uses the same honesty boundary as artifact invalidation — **explicit declaration**, no silent cascade.

### 2.6 Semantic authority

**Semantic authority** names **who or which artifact class** may define or change a semantic object for a scope (e.g. Strategy owns **seo_intent** hypotheses; Blueprint owns page-level binding; HITL owns post-freeze changes). Conflicts defer to [approval-semantics-v0.md](approval-semantics-v0.md) and [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md).

### 2.7 Semantic freeze

A **semantic freeze** is an agreement that a defined set of semantic objects **may not change** without a formal reopen path (ties to stage/artifact freeze in [stage-state-model-v0.md](stage-state-model-v0.md), [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md)).

### 2.8 Semantic drift

**Semantic drift** is **unintended divergence** of meaning between artifacts or scopes (e.g. Design shows one primary CTA while Frontend implements another). Drift is detected by **human review and QA evidence**, not by an automated diff engine in-repo.

### 2.9 Semantic consistency

**Semantic consistency** is the **goal state**: within a scope, semantic objects and relationships do not contradict governing artifacts and registries. **Consistency rules** and severities: [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md).

---

## 3. Explicit non-claims

| Topic | This layer does **not** claim |
|--------|-------------------------------|
| Storage | A graph DB, triple store, or vector index implementing these concepts. |
| Execution | Autonomous propagation, invalidation daemons, or workflow engines. |
| AI | That an LLM “understands” or “enforces” semantics beyond prompt-disciplined human execution. |
| Completeness | That every site ships with all semantic objects populated — gaps remain **SAFE UNKNOWN** per [safe-unknown-boundary.md](safe-unknown-boundary.md). |

---

## 4. Alignment with adjacent layers

| Adjacent layer | How Semantic Relationship Layer v0 relates |
|----------------|---------------------------------------------|
| Artifact Architecture | Semantic objects **live inside** artifact payloads and contracts; see [section-payload-model-v0.md](section-payload-model-v0.md), [artifact-types-v0.md](artifact-types-v0.md). |
| Execution Semantics | Invalidation, freeze, QA stale semantics **reuse** [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) — this layer **classifies** triggers by semantic object type. |
| Reference Project | Site/cluster/page graphs **reuse** [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md); [site-semantic-graph-v0.md](site-semantic-graph-v0.md) is the **meaning-oriented** reading, not a second persistence model. |

---

## 5. SAFE UNKNOWN

- **Machine validation** of semantic relationships (schemas, linters) — **not** specified in v0; treat as **SAFE UNKNOWN** until a future contract defines checks.
- **Tooling** that visualizes the conceptual site semantic graph — **external / optional**; not evidenced in this repo.

---

*End of Semantic Relationship Layer v0 — Overview.*
