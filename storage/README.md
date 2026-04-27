# `storage`

## Purpose

Reserved for **persistence**: operational DBs, vector stores, file/object storage, audit and state — the **Storage Layer** in `web-gpt-sources/02_architecture.md` and `08_storage_rag.md`. Knowledge/RAG in the docs often **uses** this layer together with **Model** and **Memory**; RAG contract detail lives under `memory/` (see [../memory/rag-architecture-v0.md](../memory/rag-architecture-v0.md)) and [../governance/dependency-map.md](../governance/dependency-map.md).

## Status

**Documentation only** — no storage backend, database, object store, or vector database is **implemented** in this repository (Phase 1) unless evidenced by real adapters or code. See [../AGENTS.md](../AGENTS.md).

## Contract index (v0)

| Document | Role |
|----------|------|
| [storage-architecture-v0.md](storage-architecture-v0.md) | Storage types, pluggable backends, relation to memory and runtime state |
| [artifact-management-v0.md](artifact-management-v0.md) | What counts as an artifact, minimum fields, rules vs memory and logs |
| [runtime-state-store-v0.md](runtime-state-store-v0.md) | Execution-time durable state (Stage 8.5) |
| [checkpoint-resume-protocol-v0.md](checkpoint-resume-protocol-v0.md) | Checkpoint/resume semantics (Stage 8.5) |

## Relation to MARS architecture

Implements the **Storage Layer** via **adapters** in the target design. Does **not** by itself represent the full “Knowledge / RAG” feature area: pair with [../memory/](../memory/) and [../models/](../models/) contracts.
