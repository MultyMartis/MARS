# MARS — Workflow Layer v0 (planned contract)

**Status:** **planned** — **contract** only. No engine, no workflow runtime, and no state store in this repository. Defines how **work** is structured and how it **relates** to the **Control Plane**, **Agent Registry**, and **Agent Factory (Agent Builder)**.

**Version:** v0 (design snapshot; not a shipped product layer).

---

## 1. Purpose of the Workflow Layer

The **Workflow Layer** describes **how tasks move through MARS** as **repeatable, inspectable patterns**: from a user or system **prompt** through **tasks**, **plans**, **routing**, **execution**, **validation**, and **reporting**, with a durable **log** story (see `execution-flow.md`).

v0 **does not** implement orchestration; the **Control Plane** (Control Core) **owns** orchestration **when it exists**. The Workflow Layer v0 **defines** the **semantic** stages, **handoffs**, and **contracts** (especially the **Task Contract v0** in `task-contract-v0.md`) that Control Plane and agents are expected to respect in a future implementation.

**Distinction (v0):**

- **Workflow Layer** = *what* a “run of work” **means** (stages, contracts, HITL gates, signals).
- **Control Plane** = *who* drives the run, **state**, **routing**, and **dispatch** to agents/models/tools (see `../control-plane/contract.md`).

---

## 2. Relation to Control Plane (Control Core)

- The **Control Plane** is the **orchestrator** in the target MARS design: it **interprets** a **Task** (or creates one from a **prompt** envelope), **plans** (or requests a plan), **routes** to **agent roles** from the **Agent Registry**, **dispatches** execution, and **aggregates** outcomes.
- The **Workflow Layer** v0 **aligns** those steps to a **single named execution flow** so that documentation, evals, and future code share one vocabulary: see `execution-flow.md`.
- **Control Plane** **acts** in: plan, route, execute (dispatch), and in **emitting** many **signals**; **Validation** in v0 is a **stage** that may be implemented by a **Validator Agent** and/or **Security** policy checks — see §4 in `execution-flow.md`.

**Registry read (v0 intent):** Control Plane **reads** the **Agent Registry** to resolve `required_agents` and **permissions**; it **must not** route to an undefined role without an explicit path (e.g. **Agent Factory** — see §5).

---

## 3. Relation to Agent Registry

- The **Agent Registry** (see `../agents/registry.md`) holds **agent cards** (identity, **status**, **permissions**, **limitations**).
- **Workflows** in v0 **do not** replace the registry; they **reference** **required agents** on each **Task** and expect the **Control Plane** to **match** task needs to **registry** entries.
- If a **required** role is **missing** or only **draft**, the run must **not** pretend the agent exists: use **UNKNOWN** or **STRUCTURE CHANGE** and optional **Agent Factory** path (§5).

---

## 4. Relation to Agent Factory (Agent Builder)

**Agent Factory** in v0 is the **design-time / out-of-run** or **gated** capability centered on the **Agent Builder** role (see `../agents/registry.md`): **create** or **update** **agent definitions** and **update the registry**.

- **Workflow** may **require** an **Agent Factory** step if a **Task** needs a **role** that is **not** in the registry or is **incompatible** (see `workflow-v0.md` + `task-contract-v0.md` `required_agents`).
- v0 **rule:** **“Workflow may trigger agent creation”** means **per contract** the Control Plane may **branch** to an **out-of-band** or **HITL-gated** **Agent Builder** process (documentation of new/updated **cards**), **not** that a live loop silently auto-spawns code.
- **SAFE UNKNOWN** if the product policy for “create agent on the fly” is not yet fixed.

**Terminology (v0):** **Control Core** = **Control Plane**; **Agent Factory** = process around **Agent Builder** + registry updates (no implementation in-repo).

---

## 5. System signals inside the workflow (summary)

Normative for v0; full usage per stage in `execution-flow.md` and `task-contract-v0.md` **signals** field:

| Signal | Workflow meaning (v0) |
|--------|------------------------|
| **UNKNOWN** | Task cannot advance: missing input, role, or binding. |
| **SAFE UNKNOWN** | Ambiguity is explicit; only bounded defaults or pauses are allowed. |
| **NEED HUMAN APPROVAL** | HITL **gate** before the next step (plan, expensive tool, etc.). |
| **SECURITY RISK** | Policy or threat surface blocks or constrains the path. |
| **STRUCTURE CHANGE** | Plan/task scope or decomposition must be **rebuilt** (replan, new task shape). |

---

## 6. Document set

| File | Role |
|------|------|
| `workflow-v0.md` | This file — **layer** purpose and relations. |
| `task-contract-v0.md` | **Task** field contract. |
| `execution-flow.md` | **prompt → … → log** with Control Plane / agents / validation / signals. |
| `README.md` | Index and **planned** status. |

**Implementation honesty:** `workflows/` contains **no** code; all behavior is **documented** as **planned**.
