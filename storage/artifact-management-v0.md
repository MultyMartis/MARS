# MARS — Artifact Management v0

**Status:** documented — contract for artifact identity and rules; not a registry implementation or file API. Per [../AGENTS.md](../AGENTS.md), no object store, artifact database, or upload pipeline is **claimed** unless evidenced in the repository.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** Exact schema encoding, checksum algorithms, replication, and URI naming in a target backend are TBD until a machine contract or code exists.

---

## 1. What is an artifact (in MARS v0)

An **artifact** is a durable, retrievable output (or snapshot of output) that exists to be fetched, cited, or replayed after the run or task ends — separate from ephemeral log streams and separate from long-term “memory” facts (see §5).

| Category | Examples (illustrative) |
|----------|------------------------|
| **Reports** | Generated markdown, PDF, or structured report bodies or exports packaged as files |
| **Generated files** | Build-time or task-time files (code, data, diagrams) stored for auditors or downstream tools |
| **Exports** | Bundles (archives, CSV dumps, snapshot folders) for governance, migration, or handoff |
| **Snapshots** | Point-in-time copies of state or outputs (not a substitute for authoritative run state in the Runtime State Store unless explicitly so scoped in design) |

**Rule:** An object is treated as an artifact in design if and only if it is addressed for retrieval by a stable `artifact_id` (or successor id in a later schema) and `storage_location`.

---

## 2. Artifact fields (v0 minimum declarative set)

| Field | Meaning |
|-------|---------|
| **`artifact_id`** | Stable primary identifier for the artifact within the chosen naming / id regime (format — **SAFE UNKNOWN** until schema). |
| **`run_id`** | Associates the artifact to a workflow run. Omit or `—` only if a non-run artifact is explicitly in scope (e.g. manual upload governed elsewhere). |
| **`task_id`** | Binds to a Task when the artifact is task-scoped; optional or cross-task only where governance permits. |
| **`type`** | Class of content (e.g. report, export, snapshot, binary) — enables retrieval policy and retention (future). |
| **`storage_location`** | Opaque or governed address of the bytes (path, key, or logical name + store); concrete form — **SAFE UNKNOWN** per [storage-architecture-v0.md](storage-architecture-v0.md) (pluggable backends). |
| **`created_at`** | Time the artifact was fully committed (clock trust — **SAFE UNKNOWN** until runtime). |
| **`source`** | Provenance: which actor or component produced the artifact (agent id, human, tool, bridge step, or cited governance id). |

**Rule:** Any v1+ machine row or index for artifacts should at minimum be mappable to the concepts above; optional fields (checksum, content type, size, encryption hint) are out of v0 naming here.

---

## 3. Rules (normative v0)

1. **Retrievable** — For every recorded artifact, there shall exist (in design / future implementation) a defined way to obtain it or fail explicitly (not silent loss as success).
2. **Artifacts ≠ logs** — Stream-like execution traces, debug dumps, and append-only governance rows in [../logs/lifecycle-log.md](../logs/lifecycle-log.md) are not substitutes for artifact metadata; cross-reference by id if a governance event produces an artifact.
3. **Artifacts ≠ memory** — Long-term factual or episodic memory (see [../memory/memory-types-v0.md](../memory/memory-types-v0.md) and [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md)) is a separate governed category; a file can be cited as source in memory without being conflated with a memory row unless policy merges them explicitly.
4. **Pluggable location** — `storage_location` is not tied to a single vendor; [storage-architecture-v0.md](storage-architecture-v0.md) §3 applies.

---

## 4. Relation to other contracts

| Contract | Relation |
|----------|----------|
| **Execution Bridge** | Bridge emissions (results, file paths, handoff) are typical producers of artifact candidates; normative I/O is [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md). |
| **Runtime State Store** | Durable per-run and checkpoint artefacts may be referenced from store facets; [runtime-state-store-v0.md](runtime-state-store-v0.md) is the execution durability SoT; do not treat arbitrary file drops as state without a stated binding. |
| **Tools** ([../tools/](../tools/)) | Tool outputs (e.g. files, exports) may register as artifacts when governance and task scope require (see tool contracts, registry). |

---

*End of MARS Artifact Management v0.*

