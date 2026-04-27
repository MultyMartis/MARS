# MARS — Execution Queue / Job System v0

**Status:** documented — contract only. This document defines the queue and job model for runtime planning. **No queue implementation exists in-repo.**

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

Define the asynchronous execution layer that can hold and sequence execution jobs across runs and tasks in a documentation-first, implementation-neutral way.

---

## 2. Job fields (v0 contract)

Each queue job is represented by the following fields:

| Field | Meaning |
|-------|---------|
| `job_id` | Stable unique job identifier inside the queue domain. |
| `run_id` | Correlation key to the run lifecycle and runtime state records. |
| `task_id` | Task-level binding to workflow/task contracts. |
| `priority` | Relative precedence used for priority override on top of FIFO. |
| `status` | One of: `queued`, `running`, `failed`, `completed`. |
| `retry_count` | Number of retry attempts already consumed for this job. |
| `max_retries` | Maximum allowed retries before dead-letter handling. |
| `created_at` | Creation timestamp for ordering, traceability, and audit narratives. |
| `updated_at` | Last status/metadata update timestamp. |

Note:
Queue job status is not equivalent to run lifecycle state.
Queue reflects execution scheduling, while run lifecycle reflects overall execution progress.
Alignment between them is achieved via `run_id` correlation and transition rules, not identical status values.

---

## 3. Queue behavior

### 3.1 Ordering model

- Baseline ordering is **FIFO**.
- A **priority override** may reorder eligible jobs when policy and queue rules permit.
- FIFO remains the default among jobs with equivalent priority.

### 3.2 Retry model

- Retry behavior is governed by [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md).
- `retry_count` increments on retry transitions until `max_retries` is reached.
- Retry outcomes and transitions must stay consistent with failure taxonomy and signals.

### 3.3 Dead-letter concept

- If a job remains failed after `max_retries`, it moves to a **dead-letter** state/area in the conceptual model.
- Dead-letter handling exists as a contract concept in v0; storage/backing mechanism is not specified.

---

## 4. Relations to other artefacts

| Artefact | Relation |
|----------|----------|
| [execution-bridge-v0.md](execution-bridge-v0.md) | Queue jobs carry bridge-bound execution intent and outcomes. |
| [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) | Queue state and transitions must map to durable runtime state records. |
| [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md) | Retries, terminal failure, and escalation rules derive from failure model semantics. |

---

## 5. Explicit non-claims

- No in-repo queue worker, broker, scheduler, or adapter is provided in v0.
- No claim is made that queue processing is currently executable in this repository.

---

## 6. SAFE UNKNOWN

- Backend choice (in-memory, Redis, MQ, DB queue, etc.) is not defined.
- Delivery semantics (at-most-once, at-least-once, exactly-once) are not fixed in v0.
- Visibility timeout, lease model, and fairness strategy are unspecified.

---

## 7. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-28 | Execution Queue / Job System v0 authored (documentation-only contract, no implementation claim). |

---

*End of Execution Queue / Job System v0.*
