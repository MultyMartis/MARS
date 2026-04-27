# MARS — Resource / Concurrency Model v0

**Status:** documented — contract only. This file defines runtime resource and concurrency limits as planning contracts. **No real limiter exists in-repo.**

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

Prevent overload and unsafe execution growth by defining conceptual limits and policy outcomes for runs, tool calls, model calls, and memory pressure.

---

## 2. Limits (v0 contract)

| Limit | Meaning |
|-------|---------|
| `max_parallel_runs` | Upper bound on concurrently active runs in execution scope. |
| `max_tool_calls_per_run` | Ceiling for tool invocations within one run. |
| `max_model_calls_per_run` | Ceiling for model invocations within one run. |
| Memory usage (conceptual) | Non-numeric memory pressure boundary to prevent unbounded execution growth. |

---

## 3. Policy outcomes

| Outcome | Meaning |
|---------|---------|
| `ALLOW` | Request is within limits and may continue. |
| `DENY` | Request exceeds policy and must not proceed automatically. |
| `NEED HUMAN APPROVAL` | Request may proceed only after explicit human decision. |

---

## 4. Relations to other artefacts

| Artefact | Relation |
|----------|----------|
| [../models/cost-token-budget-v0.md](../models/cost-token-budget-v0.md) | Budget and quota outcomes must remain coherent with cost/token governance. |
| [../models/model-routing-v0.md](../models/model-routing-v0.md) | Model selection should consume quota state as a routing constraint. |
| [../tools/tool-execution-model-v0.md](../tools/tool-execution-model-v0.md) | Tool execution sequencing and retries should respect run-level quotas. |

---

## 5. Explicit non-claims

- No in-repo limiter service, admission controller, or enforcement middleware exists for v0.
- No claim is made that quota outcomes are currently enforced at runtime.

---

## 6. SAFE UNKNOWN

- Numeric defaults and per-project overrides are not fixed in this contract.
- Burst handling and fairness policies are unspecified.
- Integration with host/container-level limits is not defined in v0.

---

## 7. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-28 | Resource / Concurrency Model v0 authored (documentation-only limits and outcomes). |

---

*End of Resource / Concurrency Model v0.*
