# MARS Website Factory — Validation consistency model v0

**Status:** **documentation only** — **what “consistent” means** for validation across artifacts and governance objects. **Not** a consistency checker service.

**Version:** v0.

**Related:** [validation-evidence-model-v0.md](validation-evidence-model-v0.md), [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md), [cross-artifact-semantics-v0.md](cross-artifact-semantics-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [artifact-transfer-qa-rules-v0.md](artifact-transfer-qa-rules-v0.md), [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md).

---

## 1. Consistency dimensions

| Dimension | Question validation asks |
|-----------|---------------------------|
| **cross-artifact consistency** | Do blueprint, design, frontend, and QA payloads tell the same story for scoped fields? |
| **semantic consistency** | Do semantic objects (CTA, trust, SEO intent, nav, offer…) align per [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md)? |
| **approval consistency** | Do approvals cover the artifact revision actually under validation? Any revocation/supersede drift? |
| **QA consistency** | Do lane QA narratives agree on blocking vs non-blocking for overlapping scope, or is contradiction explicit? |
| **lineage consistency** | Does evidence reference the current lineage / envelope per [artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md)? |
| **freeze consistency** | Do proposed changes respect active freezes per [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md)? |
| **delivery consistency** | Does the delivery candidate bundle match approved artifacts per [delivery-bus-semantics-v0.md](delivery-bus-semantics-v0.md)? |

---

## 2. Contradiction handling

1. **Detect** — mark **conflicting** evidence per [validation-evidence-model-v0.md](validation-evidence-model-v0.md).
2. **Classify** — data error vs plan error vs external SoT conflict.
3. **Route** — **STRUCTURE CHANGE** if plan wrong; **NEED HUMAN APPROVAL** if tie-break needs product/legal; **SAFE UNKNOWN** if external verification pending.
4. **Record** — do not silently pick a winner.

---

## 3. Stale relationship handling

- When semantic relationships change (dependency edge, inheritance override), validations that assumed the old edge are **stale** — move to **invalidated** or force **revalidation** per [validation-lifecycle-v0.md](validation-lifecycle-v0.md).

---

## 4. Invalidation cascades

- **Upstream** artifact invalidation **should** trigger dependent invalidation per [dependency-invalidation-v0.md](dependency-invalidation-v0.md) and [artifact-transfer-semantics-v0.md](artifact-transfer-semantics-v0.md).
- **Cascade breadth** is **not** “always entire site” — bounded per execution semantics philosophy.

---

*Last updated: 2026-05-12.*
