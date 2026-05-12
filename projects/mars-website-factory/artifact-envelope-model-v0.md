# MARS Website Factory — Artifact Envelope Model v0

**Status:** **documentation only** — **normalized conceptual envelope** for declaring an artifact at a **stage boundary**. **Not** a mandatory JSON schema, **not** a wire protocol, **not** evidence of a serialization API or runtime validator in this repo.

**Version:** v0.

**Related:** [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md), [artifact-types-v0.md](artifact-types-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).

---

## 1. Purpose

Give prompts and REPORTs a **shared field vocabulary** so that each handoff names the same dimensions: identity, type, lifecycle states, stage endpoints, revision, approvals, QA, semantics, freeze, dependencies, lineage, payload location, author, and scope.

---

## 2. Minimum field set (v0)

| Field | Description |
|--------|-------------|
| **artifact_id** | Stable identifier for the logical artifact (project convention; see [artifact-types-v0.md](artifact-types-v0.md)). |
| **artifact_type** | Class from artifact types doc (e.g. Blueprint set, Design handoff, QA report). |
| **artifact_state** | Lifecycle state per [artifact-state-model-v0.md](artifact-state-model-v0.md) (e.g. `draft`, `in_review`, `approved`, `frozen`, `superseded`, `invalidated`, `archived`). |
| **source_stage** | Workflow stage **emitting** or **anchoring** this envelope (e.g. `WF_V0_S05_BLUEPRINT`). |
| **target_stage** | Stage **intended to consume** next (may differ from actual if rerouted). |
| **revision_id** | Scoped revision token (ties to [revision-semantics-v0.md](revision-semantics-v0.md)). |
| **approval_state** | HITL approval summary for governing gate(s): e.g. `none`, `pending`, `partial`, `conditional`, `approved`, `revoked`, `expired` per [approval-semantics-v0.md](approval-semantics-v0.md). |
| **qa_state** | Lane QA lifecycle per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) (e.g. `open`, `pass`, `fail`, `conditional`, `waived`, `stale`). |
| **semantic_state** | Semantic validity posture: `consistent`, `drift_suspected`, `invalidated`, `unknown` — aligned with [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md) / [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md). |
| **freeze_state** | `unfrozen`, `stage_frozen`, `release_frozen`, `semantic_frozen` (composite allowed) per [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md) and artifact state model. |
| **dependencies** | Declared upstream **artifact_id** / **revision_id** set (and optional semantic object ids) this artifact relied on when published. |
| **lineage** | Parent / supersede / rollback pointers per [artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md). |
| **payload_reference** | Where the body lives: path, doc anchor, bundle id — **project-specific**; **SAFE UNKNOWN** if only inline prose. |
| **created_by** | Human role and/or planned **agent_id** (documentation); never anonymous “system.” |
| **handoff_scope** | **scope_in** / **scope_out** for this transfer (pages, templates, cluster ids) — must align with approval scope. |

**Omitted fields:** treat as **SAFE UNKNOWN** only with explicit bounded assumption and HITL policy per [safe-unknown-boundary.md](safe-unknown-boundary.md).

---

## 3. Immutable vs mutable regions

| Region | Envelope behavior |
|--------|-------------------|
| **Immutable after publish class** | **artifact_id**, **revision_id**, **lineage.parent**, **created_by** (original), **source_stage** at time of first approved publish for that revision — must **not** be rewritten in place; corrections use **new revision** or **supersede** chain. |
| **Mutable with HITL / QA** | **approval_state**, **qa_state**, **freeze_state** transitions; **target_stage** when rerouted; **dependencies** when invalidation declared; **semantic_state** when drift or invalidation recorded. |
| **Mutable by operational edit** | **payload_reference** may change **only** when the artifact body is intentionally moved (e.g. file rename) — must emit **STRUCTURE CHANGE** or revision per governance, never silent path swap. |

---

## 4. Envelope supersede

When **artifact B** supersedes **artifact A** at the same logical role:

- **B.lineage.parent** → **A** (or chain head).
- **A.artifact_state** → `superseded` (per policy).
- Consumers must **stop** routing to **A** unless performing historical audit.

Supersede is **not** a silent overwrite of **A**’s body.

---

## 5. Orphan envelopes

An envelope is **orphan** when:

- **lineage** references a missing or deleted artifact record;
- **dependencies** list contains **artifact_id**s that do **not** resolve;
- **approval_state** claims inheritance from a **revoked** or **expired** approval without a new gate.

**Rule:** downstream consumption **blocked** until orphan is repaired (new lineage, dependency refresh, or HITL waiver with explicit risk).

---

## 6. Stale envelopes

An envelope is **stale** when its fields **contradict** current upstream truth, e.g.:

- **qa_state** still `pass` while upstream **revision_id** changed and [dependency-invalidation-v0.md](dependency-invalidation-v0.md) requires QA reset;
- **semantic_state** `consistent` while semantic freeze broke;
- **approval_state** `approved` after partial scope shrink without re-approval.

**Rule:** mark **qa_state** or dedicated **transfer_stale** flag in REPORT (v0: use **semantic_state** + REPORT narrative); **no** silent refresh.

---

## 7. Non-claims

- **Not** a JSON Schema file in-repo.
- **Not** automatic envelope validation.
- **Not** persistence in Runtime State Store unless a future contract says so (**SAFE UNKNOWN**).

---

## 8. Revision history

| Date | Change |
|------|--------|
| 2026-05-12 | **v0** — initial envelope model (documentation only). |
