# MARS — Run Lifecycle Model v0

**Status:** documented — contract only. This file defines run lifecycle states and transition semantics in documentation form. No lifecycle engine implementation is present in-repo.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

Define the canonical run lifecycle for execution-stage planning, including blocking points and failure-driven transitions.

---

## 2. Lifecycle states (v0)

- `created`
- `queued`
- `running`
- `waiting_approval`
- `retrying`
- `completed`
- `failed`
- `aborted`

Note:
Run lifecycle states and execution queue job states are not required to match one-to-one.
Run lifecycle represents the logical execution state of a run, while queue job status represents scheduling/execution state.
Mapping between them is performed via `run_id` and transition semantics, not enum equivalence.

---

## 3. Transition model (v0)

- State transitions are controlled by [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md) where failure/retry/abort semantics apply.
- Approval gates may block forward progress by moving/keeping a run in `waiting_approval` until a human decision exists.
- Retry transitions must remain bounded and policy-consistent with failure model contracts.

---

## 4. Relations to observability and state

| Artefact | Relation |
|----------|----------|
| [../observability/run-history-v0.md](../observability/run-history-v0.md) | Run lifecycle events should be reconstructable in run-history narratives. |
| [../observability/event-model-v0.md](../observability/event-model-v0.md) | Fine-grained transition events align with event model conventions. |
| [execution-queue-v0.md](execution-queue-v0.md) | Queue status and lifecycle states must stay semantically aligned. |
| [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) | Durable persistence anchor for lifecycle state transitions. |

---

## 5. Explicit non-claims

- No runtime state machine, transition guard code, or workflow runner is implemented in this repository for v0.
- No guarantee of live transition enforcement is claimed.

---

## 6. SAFE UNKNOWN

- Exact transition triggers, timers, and timeout values are unspecified.
- Multi-run coordination behavior and parent/child run hierarchy semantics are not fixed.
- Compensation semantics for partially executed side effects are not defined here.

---

## 7. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-28 | Run Lifecycle Model v0 authored (documentation-only states and transitions). |

---

*End of Run Lifecycle Model v0.*
