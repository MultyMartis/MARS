# MARS — Memory Lifecycle v0

**Status:** documented — state transitions and governance expectations for durable memory items. Not a persistence or scheduler implementation per [../AGENTS.md](../AGENTS.md).

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** Exact timestamps, job runners, and enforcement of TTL (wall clock, logical version, legal hold) are TBD until a runtime or compliance artefact exists in or outside the repo as governed.

---

## 1. Lifecycle operations (v0)

| Operation | Meaning in design |
|-----------|-------------------|
| **Create** | New memory item or first version, subject to [memory-write-policy-v0.md](memory-write-policy-v0.md) (metadata, scope, prohibited content). |
| **Update** | Append, supersede, or tombstone-linked revision (no silent in-place erasure of provenance per write policy and the append discipline analogy in [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) for knowledge). |
| **Delete** | Tombstone or governance-approved physical purge; legal or compliance retention holds override naive delete (see Memory Write Policy, Risk Register). |
| **Expire** | Logical or physical end-of-life by TTL or rule-driven eligibility; item ceases to be a candidate for default retrieval (may remain in audit or tombstone store as policy says). |

---

## 2. TTL concept (v0)

**Time-to-live (TTL)** is a documented (or schema-backed, future) end-or-revalidate horizon or rule for a memory class or row. It may be absolute (wall-time), per-version, or driven by legal, regulatory, or project agreements. Until implementation, TTL enforcement is design-only; omission on a row is not a v0 waiver if policy or a risk row requires a retention class.

**Relation to writes:** [memory-write-policy-v0.md](memory-write-policy-v0.md) §4 (TTL or retention metadata on writes).

---

## 3. Audit via lifecycle log (governance)

- Material changes to memory-affecting policy, schema-of-record, or bulk retention / invalidation (see [knowledge-freshness-v0.md](knowledge-freshness-v0.md) and [memory-write-policy-v0.md](memory-write-policy-v0.md) §7) may warrant an entry in [../logs/lifecycle-log.md](../logs/lifecycle-log.md) (append-only governance).
- Per-row audit (who read/wrote) in a dedicated audit store — **SAFE UNKNOWN** until a contract or implementation exists; the governance log captures governance-class events, not every byte of memory (see [../governance/state-model.md](../governance/state-model.md) and Risk Register on data / compliance).

---

## 4. Relations

| Contract | Relation |
|----------|----------|
| [memory-write-policy-v0.md](memory-write-policy-v0.md) | Normative on who may write, what metadata on create/update, and tombstone discipline. |
| [../governance/risk-register.md](../governance/risk-register.md) | Risks around unauthorised access, corruption, stale knowledge, data loss, and RAG hazards — lifecycle design must not contradict stated mitigations (documentation). |

---

*End of MARS Memory Lifecycle v0.*

