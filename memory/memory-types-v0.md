# MARS — Memory Types v0

**Status:** documented — taxonomy and separation rules for durable, recall-oriented knowledge in MARS design. This file does **not** define a database schema or service API. Per [../AGENTS.md](../AGENTS.md), no memory store is **claimed** unless implemented in-repo.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** Concrete encoding, sharding, and per-type physical store mapping remain TBD until a later schema or adapter contract exists.

---

## 1. Memory types (v0)

| Type | Scope and intent |
|------|------------------|
| **Project memory** | Knowledge tied to `project_id` (see [../registry/project-registry.md](../registry/project-registry.md)): goals, constraints, glossary, decisions that outlive a single run but are not global system config. |
| **Agent memory** | Per-role or per-agent-instance preferences, learned style, or local notes governed by passport / card and orchestration (see [../agents/registry.md](../agents/registry.md)). |
| **Workflow memory** | Patterns and outcomes at the level of a reusable workflow or graph (e.g. which sequence usually needs HITL) — design-time or durable, per [../workflows/workflow-v0.md](../workflows/workflow-v0.md). |
| **User memory** | End-user-scoped facts or preferences where a user identity is in scope and governed; subject to PII and compliance rules in [memory-write-policy-v0.md](memory-write-policy-v0.md) and [../governance/risk-register.md](../governance/risk-register.md). |
| **Semantic memory** | Facts, definitions, and curated knowledge intended for grounding and RAG (often chunked and vector-indexed in future — see [rag-architecture-v0.md](rag-architecture-v0.md)). |
| **Episodic memory** | Time-ordered or run-linked episodes (what happened, decisions, outputs as narrative or structured episodes), distinct from authoritative run state in the Runtime State Store unless explicitly the same by design. |

**Note:** “Memory” in this document means durable, recall-oriented knowledge governed by [memory-write-policy-v0.md](memory-write-policy-v0.md) — not every ephemeral in-context string (those fall under ephemeral context and [../models/context-budget-policy-v0.md](../models/context-budget-policy-v0.md) at assembly time).

---

## 2. Separation rules (v0)

1. **Not execution state** — [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) facets (`state`, `checkpoints`, `errors`, etc.) are out of this taxonomy; episodic memory may cite runs but must not silently replace resumable truth (see Memory Write Policy §2).
2. **Not governance log** — [../logs/lifecycle-log.md](../logs/lifecycle-log.md) is append-only governance; memory items are not a second copy of the same decision without linking by id (Memory Write Policy and project registry conventions).
3. **Not artifacts as such** — [../storage/artifact-management-v0.md](../storage/artifact-management-v0.md) addresses retrievable files/exports; an artifact may be a source for memory but is not by itself a memory row unless ingested as governed knowledge.
4. **Cross-type leak** — Prohibited in design narrative: user-level PII in unscoped “global” project memory, or unapproved secrets in any type — per [memory-write-policy-v0.md](memory-write-policy-v0.md) §3b.

---

## 3. Relation to Memory Write Policy v0

- All mutations (create, update, delete, tombstone) to durable content in this taxonomy are subject to [memory-write-policy-v0.md](memory-write-policy-v0.md) (allowed writers, metadata, prohibited content, retention).
- Type (project / agent / user / …) must be aligned with the policy row for `entity_id` / `project_id` and any task-bound write (task contract, permissions).
- RAG and vector-backed semantic memory also obey RAG and context docs in this folder; read [rag-architecture-v0.md](rag-architecture-v0.md) and [knowledge-freshness-v0.md](knowledge-freshness-v0.md).

---

*End of MARS Memory Types v0.*

