# MARS — State Model (governance)

**Status:** **documented** — conceptual state machines and **allowed transitions** for **tasks**, **workflows (runs)**, and **agent definitions**. Does **not** require a running state store; aligns with `../workflows/execution-flow.md` and `../workflows/task-contract-v0.md`.

**Version:** v0.

---

## 1. Purpose

The **state model** unifies how **work** and **actor definitions** are described in **MARS** documentation:

- A **Task** (unit of work) has a **task state** relative to a run.  
- A **Workflow** here means the **orchestrated end-to-end run** following the v0 flow name (`execution-flow.md`): **not** a third parallel entity unless a product renames a “run” to “workflow instance.”  
- **Agent** entries in the registry have a **card lifecycle** distinct from a **task** instance.

---

## 2. Task states

**Context:** A **Task** is bound to a run per `../workflows/task-contract-v0.md`. The flow stages are: `prompt` → `task` → `plan` → `route` → `execute` → `validate` → `report` → `log`.

| State ID | Name | Meaning (governance) |
|----------|------|----------------------|
| T0 | **draft** | Request captured; **Task** not yet **bound** or not yet accepted by Control Plane semantics. |
| T1 | **ready** | **Task** **shape** accepted; **id**, **goal**, **scope**, **required_agents** (if known) are consistent enough to **plan** or queue **plan**. |
| T2 | **planning** | **Plan** in progress; **orchestration** may hold **proposed** decompositions. |
| T3 | **routed** | For current step(s), **Router** has produced **dispatch** targets; **not** yet completed **execute** for the step. |
| T4 | **executing** | **Dispatcher** has at least one **in-flight** step (model/tool/**agent** body). |
| T5 | **validating** | **validate** **stage** active; quality/policy checks before treating outputs as final. |
| T6 | **reporting** | Assembling user-facing or system **report**; may still have **HITL** on **release**. |
| T7 | **completed** | **Acceptance** satisfied; **concluded** for success path. |
| T8 | **failed** | **Unrecoverable** in current scope or policy **stop**; **error** and/or **signal** recorded. **May** transition to **T1/T2** only via explicit **re-scope** (see below). |
| T9 | **cancelled** | **Human** or system **aborted** before **completed**; no further work except audit. |
| T10 | **parked** | **Waiting** on external input: **UNKNOWN** resolution, **HITL**, or **Agent Factory** path. |

**Signals and cross-cutting:** A task may also carry **signals** (`../workflows/task-contract-v0.md` §3) **in parallel** to coarse states—e.g. **NEED HUMAN APPROVAL** while in **T4** or **T5**.

**Allowed task transitions (normative intent)**

| From | To | Condition / event |
|------|-----|-------------------|
| T0 | T1 | **Task** contract **accepted** (Control Plane *intent*). |
| T0 | T9 | **Abort** before bind. |
| T1 | T2 | **Planning** starts. |
| T1 | T10 | Missing **required** binding (e.g. **UNKNOWN** **required_agent**). |
| T2 | T3 | **Plan** **stable** for the next step. |
| T2 | T10 | **STRUCTURE CHANGE** / insoluble planning gap. |
| T2 | T1 | **Re-scope** of **Task** (explicit **structure** **change**). |
| T3 | T4 | **Dispatch** **issued** for step. |
| T3 | T10 | Route **failure**; wait for **policy** / **HITL**. |
| T4 | T3 | **Step** **done**; more steps **remain** in plan. |
| T4 | T5 | All **execute** steps for **validate** **batch** **ready**. |
| T4 | T8 | **Fatal** **execute** or **policy** break. |
| T4 | T10 | Gated **pause** (tool, approval). |
| T5 | T6 | **Validation** **passes** (or pass-with-waiver per policy). |
| T5 | T2 | **validate** **fails** → **replan** (**STRUCTURE CHANGE**). |
| T5 | T8 | **Unrecoverable** **validation** / **security** stop. |
| T6 | T7 | **Report** **emitted** and **acceptance_criteria** met. |
| T6 | T8 | **Cannot** satisfy **report** / **release** constraints. |
| T7, T8, T9 | — | **Terminal** (no default auto-advance; new **Task** is a **new** run slice). |
| T10 | T1–T5 | **Resume** when **blocker** cleared (re-enter appropriate phase). |
| T8 | T1 | **Explicit** **recovery** (new run / replan) — not silent auto-retry by default. |

**Note:** Exact **granularity** (per-step sub-state vs single task state) is an **implementation** choice; the **stages** in `execution-flow.md` remain the **vocabulary** anchor.

---

## 3. Workflow (run) states

Treat the **v0 end-to-end flow** as a **run** moving through the **same** **named** **stages** as the pipeline:

| Run state (alias) | Maps to `execution-flow` **stage** |
|-------------------|--------------------------------------|
| **ingesting** | **prompt** |
| **task_binding** | **task** |
| **planning** | **plan** |
| **routing** | **route** |
| **executing** | **execute** |
| **validating** | **validate** |
| **reporting** | **report** |
| **logging** | **log** |
| **terminal_ok** | Run **succeeded** after **log** (if logging is in scope for the run). |
| **terminal_fail** | Run **stopped** with **failure** signal. |

**Allowed run transitions (linear baseline)**

`ingesting` → `task_binding` → `planning` → `routing` → `executing` (may **loop** internal sub-steps) → `validating` → `reporting` → `logging` → `terminal_ok`.

**Non-linear allowed jumps**

| Event | Jump |
|-------|------|
| **Early** **rejection** | any → `terminal_fail` (policy/abort). |
| **HITL** / **park** | e.g. `executing` → *wait* (external), then resume same stage. |
| **Replan** | `validating` → `planning` (or `task_binding` if **Task** must **change**). |
| **Skip** **log** in minimal environments | `reporting` → `terminal_ok` **only** if product policy **explicitly** allows (otherwise **log** is **durable** **history** in **design**). |

**Relationship to **Task** state:** A **run** can carry **one** or **many** **Task**s in future designs; **v0** `task-contract-v0` focuses on a **single** **Task** focus—**orchestration** of **multiple** **Task**s is **TBD** without overloading this file.

---

## 4. Agent (registry card) states

Per `../agents/registry.md` **§2** (normative in v0):

| Status | Allowed transitions (documentation lifecycle) |
|--------|-----------------------------------------------|
| **planned** | → **draft** (editing), → **deprecated** (cancel idea), *future* → **active** only with **implementation** proof. |
| **draft** | → **planned** (stabilize), → **deprecated**, **or** stay **draft**. |
| **legacy-bridge** | → **planned** / **draft** / **deprecated** as the role **normalizes** or is **replaced**. |
| **active** | → **deprecated** (end-of-life); *avoid* silent rollback to **draft** without **governance** (human decision). |
| **deprecated** | *Terminal* for new routing; **read-only** except for **migration** notes. |

**Distinction:** This is the **definition** of an **agent role**, not the **Runtime** “agent process up/down” which would be a **separate** operational model when implemented ( **SAFE UNKNOWN** in v0 for process-level states ).

---

## 5. Consistency rules (governance)

1. **No silent DONE** if **validate** is required by **policy** and has not run.  
2. **Registry** must not show **active** for a **role** without team-defined **evidence** (per `../agents/registry.md`).  
3. **Signals** ( task **field** and **orchestration** ) must **not** be **dropped** when **transitioning** **across** **execution** **bridges** (see `execution-model.md`).

---

## 6. SAFE UNKNOWN

- Sub-states for **concurrent** **Task**s on one run — **not** fully specified.  
- **Idempotency** **keys** for state transitions at **implementation** — **TBD**.

---

## 7. Changelog (documentation)

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-04-27 | Initial state model. |
