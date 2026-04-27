# MARS — Quality Metrics v0

**Status:** **documented** — named quality metrics and intended semantics; not a dashboard, not a query, and not implemented telemetry in Phase 1.

**Version:** v0. Revisable per [governance/versioning-model.md](../governance/versioning-model.md) and [governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** Exact formulas, time windows, SLOs, and dimensional slices (project, model, tool) are TBD where not stated in another v0 SoT.

---

## 1. Purpose

Quality metrics are comparable counts or rates derived (when a runtime exists) from per-run and per-invocation artefacts. Intended inputs include [../observability/run-history-v0.md](../observability/run-history-v0.md), [../observability/event-model-v0.md](../observability/event-model-v0.md), [../observability/tool-call-log-v0.md](../observability/tool-call-log-v0.md), and for spend [../models/cost-token-budget-v0.md](../models/cost-token-budget-v0.md).

No metrics engine, dashboard, or exporter is implemented in v0.

---

## 2. Metrics (v0)

| Metric | Intended meaning (documentation) |
|--------|----------------------------------|
| task_success_rate | Fraction of Tasks or runs that end in success per [../workflows/workflow-v0.md](../workflows/workflow-v0.md). Denominator (which runs count) TBD with [../observability/event-model-v0.md](../observability/event-model-v0.md) when materialised. |
| hallucination_rate | Rate of unsupported factual assertions; scoring method TBD. Aligns with [evals-v0.md](evals-v0.md) (hallucination check) and RAG in [../memory/rag-architecture-v0.md](../memory/rag-architecture-v0.md). |
| validation_fail_rate | How often validations (tool, self-check) emit FAIL; ties to [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) and the validation_failed event type in [../observability/event-model-v0.md](../observability/event-model-v0.md). |
| approval_rate | Share of gated paths with a recorded human decision; see [../security/approval-gates.md](../security/approval-gates.md). What counts as a completed HITL path TBD. |
| retry_rate | Retries per run or per step; see [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md) for retry and duplicate-action hazards. |
| cost_per_run | Attributable cost or spend per run; [../models/cost-token-budget-v0.md](../models/cost-token-budget-v0.md) when attribution and collectors exist. |
| model_fallback_rate | How often the router in [../models/model-routing-v0.md](../models/model-routing-v0.md) takes a non-first choice or fallback; related to routing risks in [governance/risk-register.md](../governance/risk-register.md). |

---

## 3. Relation to observability and future telemetry

- v0 names semantics only; counters and SLOs are out of scope in Phase 1.
- A future telemetry layer (not in this repository in Phase 1) should read the event and log contracts. Divergent definitions of “success” or “completed HITL” are governance and risk material; see [governance/risk-register.md](../governance/risk-register.md).

---

*End of Quality Metrics v0.*
