# MARS — Event Model v0

**Status:** **documented** — contract for operational and execution-oriented events. Not a wire format, queue, or in-repo event store.

**Version:** v0. Revisable per [governance/versioning-model.md](../governance/versioning-model.md) and [governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** A future unified event bus (naming, ordering, delivery guarantees) is not defined here; v0 is field and type vocabulary for documentation and for pairing with [run-history-v0.md](run-history-v0.md) and [audit-trail-v0.md](audit-trail-v0.md).

---

## 1. Event purpose

Events record what occurred (or was decided) at a point in time, with a stable `event_id` and a `run_id` when applicable. They complement run history (aggregate per-run records) and the append-only governance [../logs/lifecycle-log.md](../logs/lifecycle-log.md) (process and map changes) by capturing fine-grained operational fact for troubleshooting, evaluation, and future automation.

No in-repo emission or storage of these events is implemented; Phase 1 remains documentation-only per [../AGENTS.md](../AGENTS.md).

---

## 2. Event fields (v0)

| Field | Meaning |
|-------|--------|
| **event_id** | Stable unique identifier for the event within the chosen operational scope (format TBD; documentation only in v0). |
| **timestamp** | When the event occurred; no NTP, skew, or timezone policy is specified in v0. |
| **run_id** | Correlates to [run-history-v0.md](run-history-v0.md); may be empty only if the event is not run-scoped, with reason documented. |
| **entity_id** | Primary subject of the event (e.g. task, agent, tool) using the same id vocabulary as the governing contract. |
| **event_type** | One of the v0 event types in §3. |
| **severity** | **Relative** importance for filtering and routing (e.g. info, warning, error) — exact enum TBD in v0. Where a named [system signal](../governance/system-signals-dictionary.md) applies, prefer `related_signal` over a generic level alone. |
| **description** | Human-readable summary; use SAFE UNKNOWN where evidence is missing ([../AGENTS.md](../AGENTS.md)). |
| **related_signal** | Optional canonical name from [governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) when the event reifies a system signal; use em dash (—) or omit if none. |

---

## 3. Event types (v0, closed set)

| event_type | Intended meaning |
|------------|------------------|
| **task_created** | A new task or runnable work unit was admitted, aligned with [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md). |
| **task_routed** | Control plane or orchestrator assigned route, stage, or next step, aligned with [../control-plane/contract.md](../control-plane/contract.md). |
| **agent_called** | An agent from [../agents/registry.md](../agents/registry.md) was invoked in run context. |
| **tool_called** | A tool from the Tool Layer was invoked; per-call details align with [tool-call-log-v0.md](tool-call-log-v0.md) and [../tools/tool-contract-v0.md](../tools/tool-contract-v0.md). |
| **model_selected** | A model routing or fallback choice was made, aligned with [../models/model-routing-v0.md](../models/model-routing-v0.md) and the registry. |
| **validation_failed** | A validation hurdle did not pass (e.g. tool validation, self-check) — see [../tools/tool-validation-rules-v0.md](../tools/tool-validation-rules-v0.md) and [../interfaces/self-check-v0.md](../interfaces/self-check-v0.md). |
| **approval_requested** | Human-in-the-loop path per [../security/approval-gates.md](../security/approval-gates.md). |
| **run_completed** | Run reached a successful terminal state per [../workflows/workflow-v0.md](../workflows/workflow-v0.md). |
| **run_failed** | Run failed or aborted per [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md). |

Extending this set is a governance and versioning action; see [governance/versioning-model.md](../governance/versioning-model.md) and record material changes in [../logs/lifecycle-log.md](../logs/lifecycle-log.md) where the master build map requires it.

---

## 4. Relation to lifecycle log

- **Lifecycle log** is append-only governance: stage gates, map changes, material adoptions ([../logs/lifecycle-log.md](../logs/lifecycle-log.md)).
- **Events** in this model are run- and operations-oriented. They are not a substitute for lifecycle log entries, though both may share project or registry identifiers in narrative.
- A single real-world event should not be double-owned without a documented rule for which log is SoT; ambiguity is a risk to record in [governance/risk-register.md](../governance/risk-register.md).

---

## 5. Relation to a future event bus

- A future bus or sink may accept payloads shaped like these fields; transport, ordering, replay, and schema version negotiation are out of scope for v0.
- Merging governance events and run events in one indistinguishable stream without separation criteria would undermine audit clarity — treat as a design risk until explicitly addressed.

---

*End of Event Model v0.*
