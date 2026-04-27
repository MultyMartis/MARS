# MARS — RAG Architecture v0

**Status:** documented — component decomposition and interfaces to neighbours for RAG (Retrieval-Augmented Generation) in MARS. This file is **not** a retrieval, index, or embedding design with algorithms, configs, or vendors. No embedding stack, chunker, or vector database is **claimed** per [../AGENTS.md](../AGENTS.md) unless in-repo evidence exists.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** Index technology, dimensionality, re-embedding policy, and per-model embedding version binding are TBD until implementation or a dedicated RAG operations contract (v1+).

---

## 1. Purpose

- Ground model generations (see [../models/](../models/)) in verifiable, scoped, policy-admissible knowledge (semantic, episodic, or ingested docs) where orchestrator design chooses RAG.
- Isolate the RAG path from raw tool or unbounded logs, and from execution state durability, so governance (memory write, permissions, retention) stays intelligible.
- Respect budget and model routing so RAG is not a bypass of [../models/cost-token-budget-v0.md](../models/cost-token-budget-v0.md) or [../models/model-routing-v0.md](../models/model-routing-v0.md).

---

## 2. RAG components (v0)

| Component | Role (design) |
|-------------|---------------|
| **Document ingestion** | Bring source materials (files, URL-governed pulls, exports) into a governed processing pipeline: classification, PII/sensitivity, licensing (future), and append-only or versioned storage of derived chunks (implementation — **SAFE UNKNOWN**). |
| **Indexing** | Build or update search structures, including vector index metadata, without requiring a single index engine (see [../storage/storage-architecture-v0.md](../storage/storage-architecture-v0.md) — vector class). |
| **Retrieval** | Fetch candidate evidence (see [memory-retrieval-v0.md](memory-retrieval-v0.md) and [knowledge-freshness-v0.md](knowledge-freshness-v0.md)); must obey project, task, permission, and data policy (§2 in memory retrieval doc). |
| **Ranking** | Order, de-duplicate, and prune candidates for prompt inclusion; v0 omits algorithms. Ties to [../models/context-budget-policy-v0.md](../models/context-budget-policy-v0.md) (what fits the budget). |

**No embedding implementation** in this v0 file — by explicit omission. A future spec may name embedding families and `model_id` (see [../models/model-registry-v0.md](../models/model-registry-v0.md)).

---

## 3. Relations to other contracts

| Contract / layer | Relation |
|------------------|----------|
| [../models/context-budget-policy-v0.md](../models/context-budget-policy-v0.md) | Hard limit on in-prompt RAG and other slices; RAG that ignores this is non-conformant. |
| [../models/model-routing-v0.md](../models/model-routing-v0.md) + [../models/model-policy-v0.md](../models/model-policy-v0.md) | Which model receives RAG-grounded context; data, safety, and capability of that model must align with injected evidence (no unsafe fallbacks per Model Layer hazards in [../governance/risk-register.md](../governance/risk-register.md)). |
| [memory-write-policy-v0.md](memory-write-policy-v0.md) + [memory-lifecycle-v0.md](memory-lifecycle-v0.md) | What may enter the durable RAG or knowledge base (writes and deletes / expiry). |
| [../storage/storage-architecture-v0.md](../storage/storage-architecture-v0.md) | Where file- and vector-class bytes land in a pluggable backend narrative. |
| [../governance/dependency-map.md](../governance/dependency-map.md) + [../governance/risk-register.md](../governance/risk-register.md) | System-level links and RAG-specific risks (e.g. stale or poisoned knowledge). |

---

*End of MARS RAG Architecture v0.*

