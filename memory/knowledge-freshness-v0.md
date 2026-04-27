# MARS — Knowledge Freshness v0

**Status:** documented — stale data, invalidation, and re-ingest triggers (design level). Not a crawler, cron, or ETL specification. No automation is **claimed** per [../AGENTS.md](../AGENTS.md) unless in-repo evidence exists.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** Event buses, poll intervals, and exact version tokens for “same source document” are TBD until a runtime or integration contract (Stage 15+ or adapters).

---

## 1. Stale data detection (conceptual)

- **Staleness** is a declared or computed state in which a memory item or RAG chunk (or set) is no longer a reliable or authorised source of grounding (by age, supersession, or upstream retraction).
- **Detection** approaches in future may include: explicit `valid_until`, governance tombstone, re-ingest hash mismatch, or HITL flag. v0 does not fix one mechanism.
- **Relation to** [memory-lifecycle-v0.md](memory-lifecycle-v0.md) (expire, delete): stale knowledge is a read-time or governance hazard; expiry is a durable end-of-life operation. They may be linked (e.g. stale → tombstone).

---

## 2. Update triggers (non-exhaustive v0 list)

| Trigger class | Intent |
|---------------|--------|
| **Source changed** | Upstream file or row updated that a chunk came from (requires traceability in ingestion design — **SAFE UNKNOWN** at wiring). |
| **Policy / governance change** | New retention, HITL reclassification, or jurisdiction rule — invalidate or re-score retrieval. |
| **Schema or model shift** | New embedding or chunker version in future may require re-index. |
| **Human or HITL signal** | “Do not use this knowledge” (quality, correctness). |

**Rule:** Triggers do not bypass [memory-write-policy-v0.md](memory-write-policy-v0.md); any new truth that enters durable memory or a RAG index still meets write rules.

---

## 3. Invalidation rules (v0)

1. Invalid or tombstoned knowledge must not be the default retrieved slice for RAG (design); if still retained for audit, it is marked as not-for-grounding (implementation detail TBD).
2. Re-ingest wins over silent in-place overwrites of provenance; new version or tombstone per [memory-lifecycle-v0.md](memory-lifecycle-v0.md) and [memory-write-policy-v0.md](memory-write-policy-v0.md) (append-first spirit).
3. **Cross-layer consistency:** if [../logs/lifecycle-log.md](../logs/lifecycle-log.md) records a governance change that affects durable knowledge, the RAG and memory narrative should acknowledge invalidation (see RAG and risk registers).

---

## 4. Relation to lifecycle log and memory lifecycle

- **[../logs/lifecycle-log.md](../logs/lifecycle-log.md)** — material policy or governance moves (STRUCTURE CHANGE, compliance) that affect knowledge value or eligibility.
- **[memory-lifecycle-v0.md](memory-lifecycle-v0.md)** — per-row create, update, delete, expire; knowledge freshness is the “is it good to read now?” lens above those operations.
- **Risk register** — stale knowledge, unauthorised access, RAG amplification (see [../governance/risk-register.md](../governance/risk-register.md)).

---

*End of MARS Knowledge Freshness v0.*

