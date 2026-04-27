# MARS — Execution flow v0 (planned)

**Status:** **planned** — **documentation** of the end-to-end path. **No** scheduler, no queue, no real **log** service in this repository.

**Version:** v0. Flow name:

`prompt` → `task` → `plan` → `route` → `execute` → `validate` → `report` → `log`

---

## 1. Stages and responsibilities

| Stage | What happens (v0) | **Control Plane** (Control Core) | **Agents** | **Validation** | **Typical signals** |
|--------|--------------------|-----------------------------------|------------|-----------------|----------------------|
| **1. prompt** | A **user/system** request enters MARS (interface layer; not defined here as code). | Ingests **envelope** (objective, policy, context refs); may form or **propose** a **Task** draft. | **Documentation Agent** or others *may* normalize prompt → structured draft — **if** in **required_agents**. | Policy pre-checks **if** available. | **UNKNOWN** if **mandatory** policy/context is missing. |
| **2. task** | A **Task** is **bound** to the run per `task-contract-v0.md` (**id**, **goal**, **required_agents**, **signals** field). | **Authoritative** to **adopt** or **reject** the task **shape**; may emit **STRUCTURE CHANGE** to re-scope. | Usually **not** the executor yet; **Agent Builder** is **out-of-band** unless a **Factory** path is open. | — | **STRUCTURE CHANGE**, **UNKNOWN** (missing **required agents** in registry). |
| **3. plan** | **Decomposition** into steps (planner in **Control Plane** contract, `../control-plane/components.md` **Planner**). | **Plans**; stores **orchestration state** (**State Manager**). | Planning **specialist** agent *may* be used **if** registered and routed. | Plan vs **acceptance_criteria** sanity. | **SAFE UNKNOWN** if plan assumes unclear facts. **NEED HUMAN APPROVAL** for high-**risk_level** plan approval. |
| **4. route** | **Router** maps step → **agent** / model / tool per **Agent Registry** + **permissions**. | **Selects** targets; **fails** closed if disallowed. | *Not called* until **execute**; routing uses **card** metadata. | — | **UNKNOWN** (no capability), **SECURITY RISK** (policy violation on route). |
| **5. execute** | **Dispatcher** runs the step: **LLM** / **tool** / **agent** body. | **Dispatch**, await outcome, **update state**. | **Active** step **here** (e.g. **Coding Agent**, **Research Agent**). | Optional inline checks. | **SECURITY RISK** on tool/model denial; **NEED HUMAN APPROVAL** for gated tools. |
| **6. validate** | **Quality** and **policy** pass on the step or whole task. | Coordinates **Validator** path, merges results into **orchestration state**. | **Validator Agent** (legacy **FlyCheck** successor) **or** other validators per task. | **Yes** — primary **validation locus** for v0. | **STRUCTURE CHANGE** (fail → replan), **SAFE UNKNOWN** (evidence partial). |
| **7. report** | **User**-visible or system **conclusion** (transcript, summary, artifacts). | Assembles **report** from state + **outputs**; may trigger **HITL** for release. | **Documentation Agent** may help format. | **Acceptance_criteria** re-check. | **NEED HUMAN APPROVAL** for public release. |
| **8. log** | **Durable** **history**: traces, audit, run record — **Observability** (future). | Emits **run** record ids and **signal** history. | Correlation ids from agents/tools. | Audit trail of **validation** outcome. | Any signal may be **recorded** here. |

**Honesty:** Steps are **contractual**; **no** code path exists in `workflows/`.

---

## 2. Where the Control Plane acts (summary)

- **Entire** pipeline **orchestrated** by **Control Plane** in target design, especially: **after prompt** (task bind), **plan**, **route**, **execute (dispatch)**, and **assembling** **validate** + **report** + **log** hooks.
- **State Manager** and **Handoff Manager** (see `../control-plane/components.md`) support **task** and **agent** handoffs between **execute** substeps.

---

## 3. Where agents are **called**

- **Primarily** in **execute**, on routed steps, per **Agent Registry** roles in **required_agents** and **planner** output.
- **Optional** in **plan** and **report** (specialists).
- **Agent Builder (Agent Factory)** is **not** a normal **execute** hop for user tasks; it is a **gated** branch when the **Task** or **Control Plane** requires a **new** or **updated** **definition** (see `workflow-v0.md`).

---

## 4. Where validation **happens**

- **Main** v0 **validate** **stage** after (or interleaved with) **execute** substeps, typically via **Validator Agent** + **Security** policy and **acceptance_criteria** on the **Task**.
- **Earlier** **validation** may occur at **prompt** and **route** (policy) — **not** a substitute for **validate** for **work quality** claims.

---

## 5. Where **signals** are **generated** (v0)

| Signal | Typical **generation** points in the flow |
|--------|------------------------------------------|
| **UNKNOWN** | **Prompt** (missing input), **task** (unresolved **required_agents**), **route** (no target). |
| **SAFE UNKNOWN** | **Plan** (bounded assumptions), **validate** (partial evidence). |
| **NEED HUMAN APPROVAL** | **Plan** (high risk), **execute** (gated tool), **report** (release). **hitl_gates** on **Task**. |
| **SECURITY RISK** | **Prompt**–**execute** (policy, injection, scope); **validate** (failed policy). |
| **STRUCTURE CHANGE** | **Task** (cannot fit goal), **plan** (infeasible), **validate** (must replan). **Agent Factory** may follow (registry update) — **per product policy**, not v0 auto-behavior. |

**Agent Factory trigger:** if **required agent** is **absent** and the product allows **Builder** to run, **Control Plane** may set **STRUCTURE CHANGE** and/or **UNKNOWN** and **off-ramp** to a **registry**-update process — **documented** only in v0.

---

## 6. Cross-references

- `../governance/system-signals-dictionary.md` — **Canonical** v0 **system** **signal** names, **semantics**, and **alias** policy.
- `workflow-v0.md` — **Workflow Layer** and relations.
- `task-contract-v0.md` — **Task** fields and **signals** list.
- `../control-plane/contract.md` — **Control Plane** and **required signals** table.
- `../agents/registry.md` — **Agent** cards, **status**, **Agent Builder**.
