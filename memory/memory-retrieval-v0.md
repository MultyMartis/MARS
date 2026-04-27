# MARS — Memory Retrieval v0

**Status:** documented — retrieval obligations and gating rules (design level only). This file does **not** define queries, embedding procedures, or ranking algorithms. No retrieval runtime is **claimed** per [../AGENTS.md](../AGENTS.md) unless evidenced in the repository.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** Latency targets, cache layers, and API shapes for read paths are TBD until implementation or a dedicated read contract v1+.

---

## 1. How memory is retrieved (v0 design dimensions)

| Dimension | Description |
|-------------|-------------|
| **By `project_id`** | Primary scope for project memory and any resource indexed under authoritative [../registry/project-registry.md](../registry/project-registry.md) — deny or return empty when id is not authorised (design intent). |
| **By `task_id`** | Narrowing reads to a current or historical Task for relevance (see [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md)) — must not pull unrelated episodes under a wrong task binding. |
| **By semantic relevance (future)** | Vector or RAG-style retrieval over indexable chunks; see [rag-architecture-v0.md](rag-architecture-v0.md); v0 has no mandatory vector implementation. |

**Rule:** all three may coexist in a retrieval plan (e.g. project scoping + task filter + top-k similarity) — order and composition are orchestrator or planner concerns (**SAFE UNKNOWN** at parameter level).

---

## 2. Normative gating: retrieval must respect

| Constraint | SoT and intent |
|------------|----------------|
| **Permissions** | [../security/permissions-v0.md](../security/permissions-v0.md) and agent / orchestrator rules — read must align with granted scopes (design; no enforcement engine in Phase 1 repo). |
| **Context budget** | [../models/context-budget-policy-v0.md](../models/context-budget-policy-v0.md) — how much and which slices of memory (and RAG, tool, introspection) enter a model prompt; over-full retrieval is a failure class at plan time. |
| **Data policy** | [memory-write-policy-v0.md](memory-write-policy-v0.md) (what was allowed to be written), [../models/model-policy-v0.md](../models/model-policy-v0.md) (model-facing data policy), [../governance/risk-register.md](../governance/risk-register.md) (PII, retention) — reads must not circumvent stated deletion, minimisation, or HITL requirements for sensitive slices (future enforcement). |

---

## 3. No retrieval implementation (explicit)

This v0 file intentionally omits implementation detail for fetching, joining, and re-ranking. A future read-side contract (or implementation) must map to this document and to [memory-lifecycle-v0.md](memory-lifecycle-v0.md) (what may be read at which age or validity state).

---

*End of MARS Memory Retrieval v0.*

