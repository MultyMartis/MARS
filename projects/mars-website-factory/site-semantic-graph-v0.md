# MARS Website Factory — Site Semantic Graph v0 (conceptual)

**Status:** **documentation only** — a **conceptual graph model** for talking about **meaning** across pages and clusters. **Not** a graph database, **not** a query engine, **not** persisted graph storage in MARS, **not** vector neighborhoods.

**Version:** v0.

**Related:** [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md), [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md), [reference-project-model-v0.md](reference-project-model-v0.md), [seo-intent-model-v0.md](seo-intent-model-v0.md), [semantic-object-model-v0.md](semantic-object-model-v0.md), [semantic-dependency-rules-v0.md](semantic-dependency-rules-v0.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).

---

## 1. What “graph” means here

**Nodes** (examples): pages, clusters, `service_entity`, key `faq_entity`, shared `proof_entity`, hub `navigation_entity` entries.

**Edges** (examples): **supports** (page → conversion goal), **competes_with** (page ↔ page SEO intent), **links_to** (internal), **inherits_geo_from** (page → cluster), **uses_proof** (section → proof_entity).

Edges exist **only when documented** in IA, Blueprint, or REPORT — there is **no** mandatory machine serialization in v0.

---

## 2. View themes

### 2.1 Page relationships

- Parent/child URL relationships, template families, shared sections.
- Used for **scope** of invalidation and QA reruns.

### 2.2 Authority flows

- Which artifact **wins** when two nodes disagree ([semantic-inheritance-v0.md](semantic-inheritance-v0.md)).
- **Authority flow** is **documentation routing** (Strategy → Blueprint → Design), not PKI or runtime auth.

### 2.3 GEO trees

- Region → city → location page hierarchies for `geo_object`.
- Used to spot **orphan** local pages or **widening** violations.

### 2.4 Service clusters

- `service_entity` nodes and their satellite FAQs, proofs, case pages.
- **Cluster QA** validates internal linking and intent separation.

### 2.5 SEO semantic neighborhoods

- Sets of pages sharing **topic proximity** per `seo_intent`; used for cannibalization checks ([seo-intent-model-v0.md](seo-intent-model-v0.md)).

### 2.6 Trust propagation (site view)

- Which pages consume which **shared trust** nodes (logos wall, compliance footer).

### 2.7 Navigation semantics

- Hub vs spoke, breadcrumb chains, **navigation_entity** edges.

### 2.8 Conversion relationships

- Funnel paths: awareness pages → consideration → conversion pages; **conversion_goal** edges.

### 2.9 Shared entities

- Global CTA destinations, phone numbers, form endpoints — **single source** nodes referenced by many pages.

---

## 3. Graph-level dynamics (documentation)

| Concept | Meaning |
|---------|---------|
| **Semantic graph invalidation** | When a node’s meaning changes, **documented** impacted edge types trigger QA/artifact invalidation ([semantic-dependency-rules-v0.md](semantic-dependency-rules-v0.md)). |
| **Graph drift** | Edges documented in IA no longer match implemented internal links or intents — **semantic drift** at site scale. |
| **Cluster QA** | QA episode treating a **cluster subgraph** as one scope ([reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md)). |
| **SAFE UNKNOWN for automation** | Any future tool that **reads** a site graph must not invent edges; unknown connectivity stays **UNKNOWN** / **SAFE UNKNOWN** until authored. |

---

## 4. Non-claims

- No **SPARQL**, **Gremlin**, **Neo4j**, or MARS-native graph store.
- No **embedding similarity** defining neighborhoods in v0.

---

*End of Site Semantic Graph v0.*
