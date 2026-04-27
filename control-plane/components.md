# MARS — Control Plane v0 components (planned)

**Status:** **planned** — **contract** descriptions only. No code, no interfaces on disk, no registries. Aligns with `contract.md` and the **Control Plane** layer in `web-gpt-sources/02_architecture.md`.

**Version:** v0 (snapshot of intended decomposition; not an implementation map).

Each component below is a **logical** role. One physical service could host multiple roles later; the contract still requires the **separation of concerns** at the design and observability level.

---

## 1. Orchestrator / Supervisor

| | |
|---|--|
| **Role** | Owns the **end-to-end run**: start, health of the run, when to stop, fail, or escalate, and which subordinate roles are activated. |
| **v0 contract** | The supervisor **does not** perform detailed planning of every micro-step; it **coordinates** **Planner**, **Router**, **Dispatcher**, **State Manager**, and **Handoff Manager** so a single run remains consistent. |
| **Boundaries** | **Does** enforce run-level invariants (policy envelope, max depth/steps as configured). **Does not** own LLM prompts or tool implementations. |
| **Signals** | Can emit **NEED HUMAN APPROVAL**, **SECURITY RISK**, **STRUCTURE CHANGE** when the run must pause or re-scope. |

---

## 2. Planner / Task Decomposer

| | |
|---|--|
| **Role** | Produces a **decomposition** of the current objective: sub-goals, ordered steps, dependencies, and optional conditions (HITL branches), as **plan artifacts**. |
| **v0 contract** | Input: objective + policy + optional memory handles. Output: a **versioned** plan (logical) the **State Manager** can store and the **Router** can consume. |
| **Boundaries** | **Does not** execute tools or call models directly; execution is **Dispatcher** + other layers. **Does not** silently override **Security** limits. If planning cannot proceed: **UNKNOWN** or **SAFE UNKNOWN** per `contract.md`. |
| **Signals** | **STRUCTURE CHANGE** when a plan must be discarded and rebuilt; **UNKNOWN** if inputs for planning are insufficient. |

---

## 3. Router

| | |
|---|--|
| **Role** | For a **ready** plan step, selects **where** the work goes: which **Agent** role, which **Model** path, or which **Tool** id (within policy and registry). |
| **v0 contract** | Input: step description + policy + availability hints (from opaque inventory). Output: a **dispatch target** + constraints slice for the next step. |
| **Boundaries** | **Does not** run the work; only **resolves** targets. If no target is valid, emit **UNKNOWN** (or **SAFE UNKNOWN** with explicit bounds). **Does not** store long-term state beyond what **State Manager** requires for routing idempotency. |
| **Signals** | **UNKNOWN** on missing capability; **SECURITY RISK** if routing would cross policy. |

---

## 4. Dispatcher

| | |
|---|--|
| **Role** | **Invokes** the selected target with the **dispatch payload** and **awaits** completion semantics (sync, async, callback) as defined by the platform. |
| **v0 contract** | Delivers **structured** invocations; records **outcome** handles for the **State Manager** (not raw secrets). |
| **Boundaries** | **Does not** re-plan; on failure, return control to **Orchestrator/Supervisor** and/or **Handoff** rules. **Does not** implement tools or model APIs inside this role. |
| **Signals** | Forwards or raises **NEED HUMAN APPROVAL** (if step requires it before dispatch), **SECURITY RISK** on tool/model policy issues. |

---

## 5. State Manager

| | |
|---|--|
| **Role** | System of record for **orchestration state** of the run: current step, statuses, idempotency keys, references to artifacts, last known plan version. |
| **v0 contract** | Persists or exposes state through paths agreed with **Storage/observability** (formats TBD). **Must** be consistent with a single run id. |
| **Boundaries** | **Does not** own business memory of the user (that is **Memory**); holds **orchestration** state only. **Does not** make policy decisions (reads policy outcomes). On ambiguous state: **UNKNOWN**. |
| **Signals** | **STRUCTURE CHANGE** if state and plan are irreconcilable after an external event. |

---

## 6. Handoff Manager

| | |
|---|--|
| **Role** | Produces and validates **handoff packages** when the active agent (or model session) must change, preserving objective, policy constraints, and allowed memory surface. |
| **v0 contract** | Input: from-state, to-state, and policy. Output: a **documented** handoff blob for the next **Agent** (or supervisor decision if handoff is rejected). |
| **Boundaries** | **Does not** embed arbitrary unbounded state from the prior hop if policy forbids. **Does not** bypass **Security** or **NEED HUMAN APPROVAL** if handoff is sensitive. |
| **Signals** | **NEED HUMAN APPROVAL** for sensitive handoffs; **SAFE UNKNOWN** when a minimal safe bundle is used per policy. |

---

## 7. Cross-component rules (v0)

1. **No monolithic “magic brain”** — the **Main Brain** legacy is absorbed as these named roles; observability and tests must be able to address them separately when implemented.  
2. **Signals** are not optional filters: any implementation claiming v0 must surface them per `contract.md` §6.  
3. **Unimplemented** behavior remains **out of scope**; until code exists, treat all interfaces as **planned** and use **SAFE UNKNOWN** when discussing behavior details.

---

## 8. Implementation honesty

Until the repository contains real Control Plane code in `control-plane/` (or a declared package elsewhere), this file describes **intention only** — not behavior.
