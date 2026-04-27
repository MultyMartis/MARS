# MARS — Tool Workflow Integration v0

**Status:** **documented** — **contract only**. Defines **where** **tool** **invocations** **fit** in **end-to-end** **workflow** and **execution** **flow**, and **normative** **rules** for **treating** each **call** as **an** **explicit** **step** **routed** **through** the **Execution** **Bridge** **with** **checkpoint** **awareness**. **No** **scheduler,** **no** **MCP** **host** in-repo for Phase 1.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

- Align **workflow** **v0** **(runs,** **tasks,** **plans**)** with** [tool-execution-model-v0.md](tool-execution-model-v0.md) **and** [../workflows/execution-flow.md](../workflows/execution-flow.md) **so** **tool** **calls** **are** **not** **invisible** **or** **side** **branches** **bypassing** the **Control** **Plane** **/ bridge** **story.**
- State **unambiguously** **that** **a** **tool** **use** **is** **a** **first-class** **step** **in** the **orchestrated** **run** **with** **defined** **ordering** **relative** **to** **route,** **execute,** **validate,** **and** **checkpoint** **/ resume** **(documentation).**

---

## 2. How workflows call tools

- **At** **plan** **time** (per [../workflows/workflow-v0.md](../workflows/workflow-v0.md) **and** **Control** **Plane** **planner** **narrative** in [../control-plane/contract.md](../control-plane/contract.md)), **a** **step** **in** **the** **plan** **may** **name** **a** **`tool_id`**, **parameters** **or** **placeholders,** **and** **the** **agent** **(role)** **expected** **to** **perform** **or** **request** **that** **invocation,** **subject** **to** **[tool-agent-binding-v0.md](tool-agent-binding-v0.md).**
- **At** **run** **time,** the **orchestrator** **materializes** **that** **step** **into** **a** **Task**-**scoped** **dispatch** **decision** **(route** **then** **execute)**: **the** **tool** **is** **not** **invoked** **directly** **from** **unscoped** **LLM** **or** **ad** **hoc** **code** **paths** **bypassing** **the** **Execution** **Bridge** **(see** **§3).**
- **Outputs** of the **tool** **step** **re-enter** the **run** **state** **(results,** **errors,** **signals)** per [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) **and** [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) **as** **described** in [tool-execution-model-v0.md](tool-execution-model-v0.md).**

---

## 3. Where tool calls appear in the execution flow

- **Path** **reference** **(v0):** [../workflows/execution-flow.md](../workflows/execution-flow.md) **`prompt` → `task` → `plan` → `route` → `execute` → `validate` → `report` → `log`**.** **A** **tool** **call** **is** **a** **specialization** **of** **a** **step** **in** **the** **execute** **stage** **(or** **a** **dedicated** **substep** **immediately** **under** **execute** **in** **the** **orchestrator** **model)**, **after** **the** **router** **has** **bound** **the** **agent** **and** **cleared** **policy** **pre**-**conditions** **where** **applicable.**
- **Concretely** **(documentation):**
  - **After** **route** **(stage** **4)**: the **Control** **Plane** **selects** **an** **agent** **and** **optional** **tool** **(or** **defers** **tool** **to** **execute)**, **failing** **closed** if **[tool-agent-binding-v0.md](tool-agent-binding-v0.md),** **permissions,** **or** **[tool-validation-rules-v0.md](tool-validation-rules-v0.md)** **reject** **the** **combination.**
  - **During** **execute** **(stage** **5)**: **the** **invocation** **envelope** **is** **built** per [tool-contract-v0.md](tool-contract-v0.md) **and** **passed** **to** the **Execution** **Bridge** **per** [tool-execution-model-v0.md](tool-execution-model-v0.md) **§2.**
- **No** **parallel** **“** **hidden** **”** **tool** **path** **may** **be** **documented** **as** **conformant** **MARS** **v0** **if** it **omits** **this** **ordering** **without** **a** **governance**-**acknowledged** **exception** **(none** **in** **v0** **table** **).**

---

## 4. Normative rules

### 4.1 Tool call = explicit step

- **Every** **intended** **tool** **invocation** **must** **be** **represented** **as** **a** **named** **step** **(or** **idempotent** **re**-**execution** **of** **a** **named** **step)** **in** the **run** **plan** **/ state** **model** **visible** **to** **orchestration** **—** **not** **only** **as** **inline** **parameters** **to** **an** **undifferentiated** **“** **llm** **turn** **.”**
- **Ad** **hoc** **or** **implicit** **tool** **invocation** **(documentation)** **=** **non**-**conformant** **for** **v0** **unless** **later** **contracts** **define** **a** **tightly** **scoped** **exception** **(** **SAFE** **UNKNOWN** **for** **such** **exceptions** **in** **Phase** **1** **repo** **).**

### 4.2 Must pass through the Execution Bridge

- **All** **conformant** **tool** **executions** **flow** **through** **[../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md)** **per** [tool-execution-model-v0.md](tool-execution-model-v0.md) **§2** **—** **assembling** **Context,** **Task,** **Plan** **slice,** **and** **tool** **I/O** **envelope,** **emitting** **bridge**-**level** **facets** **(result,** **status,** **artifacts,** **signals)**.
- **Bypassing** the **bridge** **(e.g.** **direct** **MCP** **or** **HTTP** **from** **agent** **process** **without** **the** **documented** **envelope)** **is** **out** **of** **scope** **for** **v0** **compliance** **and** **increases** **[../security/threat-model-v0.md](../security/threat-model-v0.md)** **Category** **3** **(tool** **abuse)** **if** **done** **in** **a** **future** **runtime** **without** **a** **governed** **path.**

### 4.3 Must be checkpoint-aware

- **When** **policy** **or** **the** **[../storage/checkpoint-resume-protocol-v0.md](../storage/checkpoint-resume-protocol-v0.md)** **pairing** **requires** **a** **durable** **checkpoint** **at** **a** **tool** **boundary,** **the** **step** **(including** **`step`** **identifier** **in** **plan** **position** **)** **must** **align** **with** **the** **checkpoint** **/ resume** **protocol** **and** **Failure** **Model** per [tool-execution-model-v0.md](tool-execution-model-v0.md) **§4** **and** [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md).**
- **Resuming** a **run** **must** **re**-**enter** **through** the **documented** **orchestrator** + **bridge** **path,** **not** **re**-**invoke** **a** **tool** **by** **side** **channel** **without** **reconciling** **idempotency** **and** **state** **store** **rows.**

---

## 5. Relation to other artefacts

| Artefact | Relation |
|----------|----------|
| [../workflows/workflow-v0.md](../workflows/workflow-v0.md) | **Run** **/ stage** **semantics** **for** **embedding** **tool** **steps**. |
| [../workflows/execution-flow.md](../workflows/execution-flow.md) | **High-level** **flow** **stages;** **tool** **lives** **in** **execute** **(after** **route).** |
| [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) | **Mandatory** **transit** **for** **tool** **I/O** **and** **signals**. |
| [tool-execution-model-v0.md](tool-execution-model-v0.md) | **Bridge** **mapping,** **state** **store,** **checkpoints,** **failure** **delegation**. |
| [tool-validation-rules-v0.md](tool-validation-rules-v0.md) | **Pre**-**execute** **validation** **before** **bridge** **commit** **to** **side** **effects** **(where** **applicable** **).** |

---

## 6. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Tool** **Workflow** **Integration** **v0** **—** **plan** **/** **execute** **placement,** **bridge** **and** **checkpoint** **rules** **(Stage** **9.5**).** |

---

*End of MARS Tool Workflow Integration v0.*
