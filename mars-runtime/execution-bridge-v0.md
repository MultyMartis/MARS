# MARS — Execution Bridge v0

**Status:** **documented** — **contract only**. This file defines the **documentation** boundary between the **Control Plane** (orchestration / routing / policy hooks) and **concrete execution** (human-in-the-loop tools, automation, APIs, scripts). It does **not** implement dispatch, adapters, queues, or runners. Per [../AGENTS.md](../AGENTS.md), **no** runnable execution bridge is claimed unless source code exists elsewhere in-repo.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

The **Execution Bridge** is the **normative surface** where **intent** from the Control Plane becomes **executor-specific work**: it names **inputs** supplied to an executor, **outputs** returned from execution, **failure** semantics, **signals** that must propagate, and **human-in-the-loop (HITL)** pause/resume points—without prescribing a programming language, process model, or vendor SDK.

**Boundary (documentation):**

- **Upstream:** [../control-plane/contract.md](../control-plane/contract.md) — orchestration, routing, policy hooks.
- **Downstream:** concrete **executors** (listed below). **Tools** (Stage 9) are **out of scope** for this v0 file except as a **future** attachment surface — see **§8**.

---

## 2. Supported executors (v0)

These are **categories** of execution endpoints the bridge must be able to **describe** in contracts and maps; **SAFE UNKNOWN:** which physical deployments, credentials, or endpoints apply in a given project is **not** fixed here.

| Executor category | Meaning (contract) |
|-------------------|---------------------|
| **Cursor** | Interactive **human-in-the-loop** work in the Cursor / IDE agent context (editor, terminals, MCP as configured). Aligns with **Stage 1** repo rules and **Phase 1** documentation stance. |
| **n8n** | Workflow automation **outside** the IDE — typically graph-based flows, webhooks, scheduled jobs. Bridge contract defines **payload** mapping to/from MARS task/run semantics **in documentation** only. |
| **API** | HTTP or RPC-style **service** invocation (internal or external). **SAFE UNKNOWN:** concrete OpenAPI routes, auth, rate limits — **not** specified in v0. |
| **Scripts** | Non-interactive **scripts** (shell, Python, etc.) invoked as execution steps. Same **input/output** envelope as other categories; isolation and sandboxing remain **security** / **guardrails** concerns. |

An implementation **may** support a subset; **unsupported** executor requests must surface **UNKNOWN** or **SAFE UNKNOWN** per [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md), not silent fallback.

---

## 3. Input contract

All executor-bound work **must** be describable using three conceptual bundles (field-level schemas are **out of scope** for Phase 1 unless adopted later).

### 3.1 Task

- **Identity:** stable **`task_id`** consistent with [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md).
- **Goal / scope:** aligns with task **scope_in**, **constraints**, **acceptance_criteria**, and **signals** carried on the task.
- **Bindings:** **required_agents**, registry references, and **UNKNOWN** conditions per task contract.

### 3.2 Plan

- **Decomposition:** ordered or graph-shaped **steps** consistent with [../workflows/workflow-v0.md](../workflows/workflow-v0.md) and [../workflows/execution-flow.md](../workflows/execution-flow.md).
- **Dispatch targets:** which **executor category** applies per step **when** specified; omissions yield **UNKNOWN** at execution time unless policy allows **SAFE UNKNOWN** bounded continuation.

### 3.3 Context

- **Correlation:** **`run_id`** (and optional correlation ids) — must align with durable state expectations in [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md).
- **Environment / policy:** references to **guardrails**, **approval gates**, **project_id** — see Control Plane and [../security/](../security/).
- **Attachments:** pointers to artefacts (paths, URIs) **without** mandating storage backend — **SAFE UNKNOWN** until concrete stores exist.

---

## 4. Output contract

Executor completion **must** be representable by the following **documentation** facets (implementation may serialize them differently).

| Facet | Meaning |
|-------|---------|
| **result** | Primary **payload**: content produced for the step (text, structured data, file references). May be **empty** on pure control steps. |
| **status** | Terminal **success** / **failure** / **partial** classification for the step **as executed** — must remain consistent with [../governance/state-model.md](../governance/state-model.md) when mapped to task/run states. |
| **artifacts** | **Named outputs** (files, logs, reports) **linked** to **`task_id`** / **`run_id`** for audit and replay narratives. |
| **signals** | Zero or more **canonical** **system signals** ([../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md)) **raised** or **preserved** by the step — **must not** be dropped at the bridge (see [../governance/state-model.md](../governance/state-model.md) §5). |

---

## 5. Failure modes

| Mode | Definition | Typical signal / outcome |
|------|------------|---------------------------|
| **Execution failure** | Executor returned **failure** **status** or **policy** denied the step (deterministic **FAIL** path). | **SECURITY RISK** if policy violation; otherwise step-level failure recorded; **STRUCTURE CHANGE** may follow if replan is required. |
| **Timeout** | Step **did not** complete within **allowed** duration (**SAFE UNKNOWN:** limits are product/runtime — **not** fixed here). | Treat as **failure** **unless** policy defines **retry**/**resume** — coordinate with future **Failure Handling Model** (Stage 8.5 P0 **TBD**). |
| **Unknown** | Outcome **cannot** be classified (lost callback, ambiguous API response, partial writes). | **UNKNOWN** or **SAFE UNKNOWN** with explicit **unknown** slice; **do not** assume success — **park** until resolved ([../governance/state-model.md](../governance/state-model.md) **T10** **parked** alignment). |

---

## 6. Required signals usage

Bridge documentation and future implementations **must**:

1. Use **only** canonical signal **names** from [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) §2 for cross-layer reporting (no informal synonyms in normative tables).
2. Emit **UNKNOWN** when a **required binding** is missing — e.g. executor not specified, credentials not resolved, **task_id** missing.
3. Emit **SAFE UNKNOWN** when proceeding **honestly** requires admitting **unverified** slices (e.g. external API behaviour not evidenced in-repo).
4. Emit **NEED HUMAN APPROVAL** at **gates** matching [../security/approval-gates.md](../security/approval-gates.md) and workflow **hitl_gates**.
5. Emit **SECURITY RISK** on policy escape or dangerous routing — **no** silent continuation.
6. Preserve **STRUCTURE CHANGE** when replanning must invalidate the current plan slice.

---

## 7. HITL interaction points

Human-in-the-loop is **expected** at least at:

- **Plan approval** — high-risk or wide-blast-radius plans ( **NEED HUMAN APPROVAL** ).
- **Executor handoff** — Cursor / operator **accepts** or **rejects** an execution package (documentation: **pause** → **resume** or **abort**).
- **Ambiguous failure** — **UNKNOWN** / **SAFE UNKNOWN** outcomes **park** the task ([../governance/state-model.md](../governance/state-model.md) **T10**) until a human or policy clarifies.
- **Release / ship** — reporting stage may block on approval before **terminal_ok**.

**SAFE UNKNOWN:** Exact UI or ticketing integration for HITL is **not** specified in v0.

---

## 8. Relations to other artefacts

| Artefact | Relation |
|----------|----------|
| **Control Plane** | Bridge **consumes** orchestration **intent** (routes, policy hooks) and **returns** execution outcomes **into** the orchestration story — [../control-plane/contract.md](../control-plane/contract.md). |
| **Workflows** | Bridge **steps** map to **workflow** stages and **task** lifecycle — [../workflows/workflow-v0.md](../workflows/workflow-v0.md), [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md), [../workflows/execution-flow.md](../workflows/execution-flow.md). |
| **Tools (future)** | **Stage 9** will define **tool** registry and permissions. Bridge v0 **does not** define tool invocation wire format; future docs **must** align **signals**, **guardrails**, and **executor** categories **without** contradicting this envelope. |
| **Interfaces (Self-*)** | **Self-Describe** / **Self-Check** / **Self-Audit** **reflect** whether execution claims match **documented** contracts — [../interfaces/](../interfaces/). **Self-Heal** v0 ([../interfaces/self-heal-v0.md](../interfaces/self-heal-v0.md)) provides **plan-only** recovery **plans** that may reference **bridge** failures **without** executing fixes. |
| **Runtime State Store** | Durable **execution** **state** (including checkpoint-friendly records) is defined in [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md); bridge **inputs/outputs** **must** **map** to **store** **fields** **where** **persistence** **is** **required**. |

---

## 9. SAFE UNKNOWN

- Concrete **wire formats**, **RPC** schemas, **n8n** node IDs, **Cursor** internal APIs — **not** specified.
- **Retry**, **idempotency keys**, **exact** **timeout** values — await **Failure Handling Model** and **Checkpoint / Resume Protocol** (Stage 8.5 P0 **TBD**).

---

## 10. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Execution Bridge v0** — purpose, executors, input/output contracts, failure modes, signals, HITL, relations. |

---

*End of Execution Bridge v0.*
