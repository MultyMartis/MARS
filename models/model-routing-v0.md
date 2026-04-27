# MARS — Model Routing v0

**Status:** **documentation only** — describes how the **Control Plane** / **Router** **should** choose among registered models **at design level**. **No** runtime router implementation is claimed in this repository ([../AGENTS.md](../AGENTS.md)).

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

- Define **inputs** and **outputs** of the **routing decision** so that orchestration docs, observability plans, and future code share one vocabulary.
- Specify **fallback** triggers and ordering **principles** without prescribing algorithms or services.

**SAFE UNKNOWN:** Latency SLAs, per-region routing, A/B experiment frameworks, and concrete scoring functions are **out of scope** for v0.

---

## 2. Relation to Control Plane / Router

- [../control-plane/contract.md](../control-plane/contract.md) owns **orchestration** vocabulary: **planner**, **router**, **dispatch**, **policy hooks**.
- **Model routing** is a **sub-function** of the **router** (or a dedicated **model-router** component **under** the same control-plane story): it turns **normalised routing inputs** into a **model decision** **before** an adapter invokes a provider.
- **Execution** **bridge** and **tool** steps remain governed by [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) and [../tools/tool-workflow-integration-v0.md](../tools/tool-workflow-integration-v0.md); **model routing** applies to **LLM** **steps**, not to **tool** **selection** — though **tool** outcomes may **feed back** into a **subsequent** routing pass.
- Failure handling behavior is defined in [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md).

---

## 3. Routing inputs (v0)

The router **should** supply or derive at least the following **inputs** for each model decision:

| Input | Description |
|-------|-------------|
| **task type** | From [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md) / orchestration envelope; drives **allowed_tasks** / **prohibited_tasks** checks. |
| **risk level** | Task- and/or run-level risk; intersects with [model-policy-v0.md](model-policy-v0.md) and [../security/approval-gates.md](../security/approval-gates.md). |
| **context size** | Estimated or measured size of the assembled prompt (tokens or normalised units); compared to **context_window** and [context-budget-policy-v0.md](context-budget-policy-v0.md). |
| **cost budget** | Outcome of [cost-token-budget-v0.md](cost-token-budget-v0.md) for the **run** / **project**; may **narrow** **cost_class** eligibility. |
| **required capabilities** | e.g. vision, JSON mode, embedding — must match registry **capabilities**. |
| **data policy** | Required minimum posture for the payload (e.g. `local_only`); compared to registry **data_policy**. |

Additional inputs (project defaults, agent profile, **SAFE UNKNOWN** until specified) may refine ordering but **must not** bypass **policy** or **budget** **DENY** paths.

---

## 4. Routing outputs (v0)

| Output | Description |
|--------|-------------|
| **selected model_id** | The **primary** choice from [model-registry-v0.md](model-registry-v0.md), or empty if none eligible. |
| **fallback chain** | Ordered list of **model_id** values for **degraded** continuation **after** **policy**-**consistent** re-checks per hop ([model-policy-v0.md](model-policy-v0.md) §7.4). |
| **rationale** | Human- or machine-readable **reason** for audit (documentation: **what** constraints dominated). |
| **signals** | Canonical signals per [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) where applicable (e.g. **NEED HUMAN APPROVAL**, **SAFE UNKNOWN**, **DENY** narrative — exact token set **must** follow dictionary). |

---

## 5. Fallback rules (v0)

| Condition | Expected behaviour (design) |
|-----------|----------------------------|
| **Provider unavailable** | Try **fallback_model_id** / chain entries that **still** satisfy **data_policy** and **task** rules; if none → **DENY** or **pause** with **signals** (not silent pick of arbitrary model). |
| **Policy denial** | **Do not** fallback to a **weaker**-**governance** model unless **explicitly** allowed for that denial class; default → **NEED HUMAN APPROVAL** or **DENY**. |
| **Context too large** | **Trim** per [context-budget-policy-v0.md](context-budget-policy-v0.md) **or** switch to a model with **larger** **context_window** **if** **policy** and **budget** allow; if still infeasible → **DENY** / **HITL**. |
| **Model output invalid** | **Do not** auto-switch to an **unrelated** “stronger” model without a **defined** recovery path (may pair with [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md)); **fallback** **only** along **approved** chain. |

---

## 6. Explicit non-goals (v0)

- **No** provider SDK or HTTP client specification.
- **No** load balancing or autoscaling narrative.
- **No** claim that routing is **implemented** anywhere in-repo.

---

## 7. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Model Routing v0** — control-plane relation, inputs/outputs, fallback rules, non-goals. |

---

*End of MARS Model Routing v0.*
