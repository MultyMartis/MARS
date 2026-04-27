# MARS — Checkpoint / Resume Protocol v0

**Status:** **documented** — **contract only**. This file defines **checkpoint** records and **resume** rules so interrupted execution can continue **without** silent loss or contradiction of durable state. It does **not** specify a database product, WAL format, or runner implementation. Per [../AGENTS.md](../AGENTS.md), **no** checkpoint store or resume engine is claimed unless code exists in-repo.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

Enable **resume** of **interrupted** execution (crash, timeout, HITL pause, policy park) by:

- Declaring a **minimum logical checkpoint structure** aligned with [runtime-state-store-v0.md](runtime-state-store-v0.md) **`checkpoints`** facet.
- Binding **resume** to **last valid checkpoint**, **pre-resume validation**, and **SAFE UNKNOWN** when the stored picture is **inconsistent**.
- Pairing with [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md) for **retry** vs **resume** vs **abort** after failures.

---

## 2. Checkpoint structure (v0 logical fields)

Each **checkpoint** record is **immutable** once written (**append**), per [runtime-state-store-v0.md](runtime-state-store-v0.md) §3–6. **SAFE UNKNOWN:** physical serialization, compression, encryption.

| Field | Description |
|-------|-------------|
| **`task_id`** | Stable task identifier per [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md). |
| **`run_id`** | Correlates all records for one run; format **SAFE UNKNOWN** until Run ID model (Stage 8.5 P1 backlog). |
| **`step`** | **Logical** step index or **step identifier** within the plan (align [../workflows/workflow-v0.md](../workflows/workflow-v0.md) / [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) **Plan** decomposition). |
| **`state_snapshot`** | **Slice** of **task**/**run** **state** and **any** **data** required to **reconstruct** “what was true at commit time” **without** mutating prior committed facts — must remain **consistent** with [../governance/state-model.md](../governance/state-model.md). |
| **`timestamp`** | Ordering and audit (**logical** or wall-clock; **SAFE UNKNOWN** for clock skew policy). |

Implementations **may** add opaque **`checkpoint_id`**, **`parent_checkpoint_id`**, executor id, or trace correlation — **without** dropping the **minimum** fields above.

---

## 3. Resume rules (normative v0)

1. **Resume from last valid checkpoint** — On resume, the **authoritative** continuation point is the **latest** checkpoint that passes **§4** validation. If **none** validate: **do not** assume a step completed; surface **SAFE UNKNOWN** or **UNKNOWN** per [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md).
2. **Validation before resume** — Before re-entering **execute**, verify: **`task_id`/`run_id`** consistency; **`step`** still exists in current plan or **STRUCTURE CHANGE** has been applied; **`state_snapshot`** does not contradict **append-only** history in the store; **policy** / **approval** gates still allow continuation.
3. **SAFE UNKNOWN if inconsistent state** — If checkpoints, results stream, or errors **contradict** each other, or **partial completion** cannot be ordered: **do not** auto-resume into **execute**; **park**, **escalate**, or **abort** per [failure-model-v0.md](../workflows/failure-model-v0.md).

**Checkpoint boundaries** — **Where** checkpoints are **required** vs **optional** aligns with **workflow** stages and **Execution Bridge** handoffs; **SAFE UNKNOWN** for per-product minimum frequency until workflow-specific addenda tighten it.

---

## 4. Idempotency rules (v0)

1. **Repeated execution must not corrupt state** — Resume **replays** from a **validated** checkpoint **must** use **append** / **supersede** patterns per [runtime-state-store-v0.md](runtime-state-store-v0.md) §5–6, not in-place erasure of committed facts.
2. **Duplicate tool calls must be controlled** — Same obligation as [failure-model-v0.md](../workflows/failure-model-v0.md) §5: idempotency tokens, deduplication, or **escalation** before a second side-effecting invocation when replay could **double** external effects.

---

## 5. Relation to other artefacts

| Artefact | Relation |
|----------|----------|
| [runtime-state-store-v0.md](runtime-state-store-v0.md) | **SoT** for **`checkpoints`** facet and **lifecycle** operations **checkpoint** / **update** / **finalize**. |
| [../governance/state-model.md](../governance/state-model.md) | **T10 parked**, **resume** transitions, terminal states **must** agree with **`state_snapshot`** semantics. |
| [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md) | **Retry** vs **resume** vs **abort**; **partial completion** and **SECURITY RISK** handling. |
| [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) | **Pause** / **resume** points and **output** mapping into stored **results**/**errors**. |
| [../workflows/workflow-v0.md](../workflows/workflow-v0.md) | Run **stages** and **plan** shape for **`step`** interpretation. |

---

## 6. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Checkpoint / Resume Protocol v0** — purpose, checkpoint structure, resume and idempotency rules, cross-refs. |

---

*End of Checkpoint / Resume Protocol v0.*
