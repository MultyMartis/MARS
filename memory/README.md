# `memory`

## Purpose

Reserved for **memory** subsystems: project, agent, workflow, user, semantic, and episodic memory, as sketched in the **Memory Layer** in `web-gpt-sources/02_architecture.md` and `06_memory.md`. RAG and knowledge freshness are specified here as **documentation** (Stage 11), not as running services.

## Status

**Documentation only** — no memory services, databases, vector stores, or RAG pipeline is **implemented** in this repository (Phase 1) unless evidenced. See [../AGENTS.md](../AGENTS.md).

## Contract index (v0)

| Document | Role |
|----------|------|
| [memory-write-policy-v0.md](memory-write-policy-v0.md) | When and how durable memory may be written (Stage 8.5) |
| [memory-types-v0.md](memory-types-v0.md) | Taxonomy: project, agent, workflow, user, semantic, episodic memory |
| [memory-retrieval-v0.md](memory-retrieval-v0.md) | How retrieval is scoped; permissions, context budget, data policy |
| [memory-lifecycle-v0.md](memory-lifecycle-v0.md) | Create, update, delete, expire, TTL, audit hooks |
| [rag-architecture-v0.md](rag-architecture-v0.md) | RAG components: ingestion, indexing, retrieval, ranking (no embedding spec) |
| [knowledge-freshness-v0.md](knowledge-freshness-v0.md) | Stale data, invalidation, update triggers vs lifecycle |

## Relation to MARS architecture

Implements the **Memory Layer** in design. Used by **Agents** and the **Control Plane**; may persist through **Storage** adapters when implemented. **No** backend / DB / vector DB is in-repo for v0.
