# MARS — Storage Architecture v0

**Status:** documented — design contract only. This file classifies how MARS is intended to store, index, and manage data, artefacts, and indexable content in documentation form. It does **not** name a single shipped backend, API shape, or schema. Per [../AGENTS.md](../AGENTS.md), no storage adapter, database, or vector system is **claimed** unless the repository contains evidence of implementation.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** The concrete product backend (or backends), connection topology, replication, encryption at rest, and exact isolation boundaries are **not** fixed in this v0. Those choices remain **unknown** until a later contract or implementation is evidenced in-repo.

---

## 1. Purpose

- Give a shared vocabulary for **storage types** and **pluggable backends** so Memory, RAG, Runtime State, and artifact management docs do not silently assume one database or one vendor.
- Separate concerns: durable execution and governance surfaces (see [runtime-state-store-v0.md](runtime-state-store-v0.md), [../logs/lifecycle-log.md](../logs/lifecycle-log.md)) from long-lived knowledge and files — without prescribing implementation.
- Preserve optionality: teams may later adopt Google Sheets, a self-hosted database on a VPS, object storage, a vector index, or a hybrid split — the architecture must allow swapping or combining backends per policy and project needs.

---

## 2. Storage types (v0 taxonomy)

| Type | What it holds | Design role in MARS |
|------|---------------|---------------------|
| **Structured (DB)** | Rows, relations, queryable fields (e.g. runs, task state, registries, artifact metadata) | Authoritative tabular truth for correlators like `project_id`, `run_id`, `task_id` when a relational or document-DB model is chosen — in future implementation only. |
| **Semi-structured (JSON / documents)** | Config, manifests, per-run blobs, schematised JSON, lightweight doc stores | Flex at boundaries (bridge outputs, tool payload summaries, export packages) while keeping governance and validation rules in other contracts (not this file alone). |
| **File storage** | PDF, images, archives, generated reports, large binaries | Durable artefacts addressed by pointers (see [artifact-management-v0.md](artifact-management-v0.md)); not a substitute for state rows in [runtime-state-store-v0.md](runtime-state-store-v0.md) or append-only governance in the lifecycle log. |
| **Vector storage (embeddings)** | Embedding vectors and chunk metadata for similarity search / RAG | Retrieval index for semantic recall; normative RAG narrative in [../memory/rag-architecture-v0.md](../memory/rag-architecture-v0.md). No embedding or index implementation is claimed in Phase 1 unless evidenced. |

**Rule:** The same logical object (e.g. a “document”) may map to file bytes plus vector chunks plus row-level metadata — the architecture anticipates composition, not a single lump in one box.

---

## 3. Pluggable backends (v0 design intent, not a commitment)

MARS design rejects a single hardcoded backend as the only supported deployment. The following are plausible adapter targets; selection is governance- and project-driven (**SAFE UNKNOWN** until chosen and evidenced).

| Pattern | Intended use | Notes |
|---------|---------------|--------|
| **Google Sheets** | Light tabular sheets, small teams, human-visible or manual ops where acceptable | Not a claim of current integration; a future adapter would enforce permissions, quotas, and export rules. |
| **Self-hosted DB (VPS)** | Primary structured store on operator-controlled infrastructure | Candidate for authoritative state and artefact metadata; exact engine (SQL, document, etc.) — **SAFE UNKNOWN**. |
| **Hybrid** | e.g. VPS for authoritative data + object store for blobs + optional sheets or third-party vector | Default mental model for serious deployments: split by data class and risk. |

**Rule (normative for documentation):** any doc that assumes a specific backend must state that it is illustrative or one deployment option, or mark concrete wiring as **SAFE UNKNOWN** until the adapter exists in the repository or a linked governance row.

---

## 4. Relation to other MARS contracts

| Contract / surface | How Storage Architecture v0 relates |
|--------------------|--------------------------------------|
| **Runtime State Store** ([runtime-state-store-v0.md](runtime-state-store-v0.md)) | Execution-durability facets are not “storage types” defined in §2, but they use the same pluggability principle: a future store implementation backs those facets without implying all other MARS data lives in the same engine. |
| **Memory Layer** (see [../memory/README.md](../memory/README.md), [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md)) | Durable knowledge and memory items are stored via adapters conforming to the type rules here (structured + vector + file as appropriate); write authority stays in the Memory Write Policy. |
| **Artifact management** ([artifact-management-v0.md](artifact-management-v0.md)) | File and metadata storage for artefacts; pointers and fields in the artefact contract — not a second “logs” store. |
| **Execution Bridge** ([../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md)) | Bridge outputs and handoff may produce blobs or references that land in file or structured stores; mapping is governed by the Execution Bridge and Runtime State Store contracts, not a single hardcoded path. |

---

## 5. Normative rules (v0)

1. **No single hardcoded backend** in normative MARS docs as the only allowed system; portray adapters or **SAFE UNKNOWN** (see §3 and the preamble).
2. **Backend** is **SAFE UNKNOWN** until a concrete adapter or in-repo evidence proves it — per [../AGENTS.md](../AGENTS.md) honesty boundary.
3. **Distinguish** state (runtime), governance log (lifecycle), memory (write policy), RAG (rag-architecture v0), and artifacts (artifact management) when attributing data to a store type (§2).

---

*End of MARS Storage Architecture v0.*

