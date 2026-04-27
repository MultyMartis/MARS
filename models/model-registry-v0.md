# MARS — Model Registry v0

**Status:** **documentation only** — canonical **field vocabulary** and **lifecycle** semantics for registering LLM / embedding **candidates** in MARS. **No** runtime registry service, **no** provider configs, **no** API keys, **no** SDKs in this repository phase.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

- Give **one** documented place for **what** a “model row” means in MARS: identity, provider binding, capabilities, policy hooks, and lifecycle **status**.
- Separate **catalogue** (this registry) from **selection rules** ([model-policy-v0.md](model-policy-v0.md)), **routing** ([model-routing-v0.md](model-routing-v0.md)), **context assembly** ([context-budget-policy-v0.md](context-budget-policy-v0.md)), and **cost limits** ([cost-token-budget-v0.md](cost-token-budget-v0.md)).
- Treat **OpenRouter**, **OpenAI-compatible** HTTP APIs, and **local** runtimes as **examples** of **provider profiles** only — **not** as exclusive backends. Any concrete provider is an **adapter** concern **outside** this file until implementation exists and is evidenced in-repo ([../AGENTS.md](../AGENTS.md)).

**SAFE UNKNOWN:** Until a future implementation lands, **machine schema**, **storage backend**, **sync** from vendor catalogues, and **live endpoint** truth are **not** specified here.

---

## 2. Model registry fields (v0)

Each logical **model row** (whether stored as YAML, SQL, or other — **not** defined in v0) **should** be able to carry the following fields.

| Field | Description |
|-------|-------------|
| **model_id** | Stable MARS identifier for this row (e.g. `mars-model-openrouter-planned-001`). Used by policy, routing, budgets, and observability **narratives**; not necessarily equal to vendor `model` string. |
| **provider** | Provider **profile** or adapter key (e.g. `openrouter`, `openai_compatible`, `local_placeholder`). **Not** a claim that integration exists in-repo. |
| **model_name** | Vendor- or stack-facing model name / slug passed to an adapter when invoked (e.g. routing header or local server id). May duplicate external naming; **model_id** remains canonical for MARS. |
| **status** | Lifecycle state from **section 3** only. |
| **capabilities** | Structured or enumerated description of what the model is **documented** to support for planning: e.g. `chat`, `json_mode`, `vision`, `embedding`, `function_calling` — exact encoding **SAFE UNKNOWN** until a schema is adopted. |
| **allowed_tasks** | Task types or **tags** for which this model may be **considered** when policy and routing allow (design-time list). |
| **prohibited_tasks** | Task types or **tags** for which this model **must not** be selected regardless of capability claims (hard **DENY** in policy narrative). |
| **risk_level** | Coarse risk class for **governance** alignment (e.g. `low` / `medium` / `high`); must be **consistent** with [../security/approval-gates.md](../security/approval-gates.md) and [../governance/risk-register.md](../governance/risk-register.md) where cross-walked. |
| **cost_class** | Relative cost bucket for budgeting and routing **priorities** (e.g. `economy`, `standard`, `premium`); numeric pricing **out of scope** for v0 doc-only. |
| **context_window** | Declared maximum context length (tokens or provider-specific unit); used for **context-budget** and **routing** **feasibility** checks at design time. **SAFE UNKNOWN** if vendor does not publish a stable value. |
| **data_policy** | Declared handling posture for sensitive payloads (e.g. `no_training`, `unknown_retention`, `local_only`, `external_processed`); must align with [model-policy-v0.md](model-policy-v0.md) and [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) when memory or PII is in scope. |
| **fallback_model_id** | Optional pointer to another **model_id** for documented **degradation** paths (see [model-routing-v0.md](model-routing-v0.md)). Must not introduce cycles at design time. |

---

## 3. Status values (v0)

| Status | Meaning |
|--------|---------|
| **planned** | Named for roadmap / budgeting; **no** approval to use in production narratives. |
| **draft** | Under active documentation or registry review; not **approved**. |
| **approved** | Human or governance process accepts use **subject** to policy + routing + budgets. |
| **active** | May be selected by routing when all downstream checks pass (**documentation** sense; no runtime claim). |
| **deprecated** | Must not be selected for new work; retained for historical runs / audit only. |

---

## 4. Example entries (illustrative only)

All examples below use **status = `planned`** only. They are **not** endorsements, **not** live configuration, and **not** evidence of provider integration in this repository.

### 4.1 OpenRouter provider profile (planned)

| Field | Example value |
|-------|----------------|
| **model_id** | `mars-model-planned-openrouter-mixtral-8x7b` |
| **provider** | `openrouter` |
| **model_name** | `mistralai/mixtral-8x7b-instruct` *(placeholder vendor string)* |
| **status** | `planned` |
| **capabilities** | `chat`, `function_calling` *(claimed; verify before any implementation)* |
| **allowed_tasks** | `general_reasoning`, `code_assist_low_risk` |
| **prohibited_tasks** | `high_privilege_ops`, `raw_pii_processing` |
| **risk_level** | `medium` |
| **cost_class** | `standard` |
| **context_window** | `32768` *(illustrative; confirm with vendor docs when implementing)* |
| **data_policy** | `external_processed` — payloads leave the trust boundary; see [model-policy-v0.md](model-policy-v0.md) |
| **fallback_model_id** | `mars-model-planned-local-llamacpp-placeholder` |

### 4.2 OpenAI-compatible provider (planned)

| Field | Example value |
|-------|----------------|
| **model_id** | `mars-model-planned-oai-compat-generic-chat` |
| **provider** | `openai_compatible` |
| **model_name** | `gpt-4.1-mini` *(example only; any OpenAI-compatible server may map differently)* |
| **status** | `planned` |
| **capabilities** | `chat`, `json_mode` |
| **allowed_tasks** | `structured_output`, `summarization` |
| **prohibited_tasks** | `unsupervised_destructive_tool_planning` |
| **risk_level** | `medium` |
| **cost_class** | `economy` |
| **context_window** | `128000` *(illustrative)* |
| **data_policy** | `external_processed` |
| **fallback_model_id** | `mars-model-planned-openrouter-mixtral-8x7b` |

### 4.3 Local model placeholder (planned)

| Field | Example value |
|-------|----------------|
| **model_id** | `mars-model-planned-local-llamacpp-placeholder` |
| **provider** | `local_placeholder` |
| **model_name** | `llama.cpp-server-default` *(placeholder)* |
| **status** | `planned` |
| **capabilities** | `chat` |
| **allowed_tasks** | `offline_dev`, `low_sensitivity_scratch` |
| **prohibited_tasks** | `production_customer_data` *(unless future policy explicitly allows)* |
| **risk_level** | `low` *(for exfil via cloud provider — not a claim about local ops security)* |
| **cost_class** | `economy` |
| **context_window** | `8192` *(illustrative)* |
| **data_policy** | `local_only` *(design intent; actual air-gap **SAFE UNKNOWN** until deployment specified)* |
| **fallback_model_id** | `—` |

---

## 5. Relation to other artefacts

| Artefact | Relation |
|----------|----------|
| [model-policy-v0.md](model-policy-v0.md) | Consumes registry rows for **allowed** / **prohibited** bindings. |
| [model-routing-v0.md](model-routing-v0.md) | **reads_from** registry for candidate **model_id** lists and **fallback_model_id** chains. |
| [../control-plane/contract.md](../control-plane/contract.md) | Orchestration / router hooks assume a **catalogue** of routable models at design time. |
| [../governance/dependency-map.md](../governance/dependency-map.md) | Entity **`model_registry`** and edges to **control plane**, **policy**, **routing**, **risk**. |

---

## 6. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Model Registry v0** — purpose, fields, statuses, **planned-only** examples (OpenRouter, OpenAI-compatible, local placeholder). |

---

*End of MARS Model Registry v0.*
