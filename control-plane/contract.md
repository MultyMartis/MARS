# MARS — Control Plane v0 (planned contract)

**Status:** **planned** — this document is a **contract specification** only. It does **not** describe running code, binaries, or deployed services. It exists to align design before implementation in later phases.

**Version:** v0 (initial contract snapshot; may be revised without implying prior implementation existed).

---

## 1. Purpose

The **Control Plane** is the MARS sublayer responsible for **orchestrating** work: turning accepted requests into ordered units of work, **routing** them to the right agents, models, and tools (via contracts to those layers), **managing** execution state and **handoffs** between units, and surfacing **signals** to interfaces and humans when judgment or policy intervention is required.

v0 names **responsibility boundaries** and **information contracts**; it does **not** fix technology choices (queue library, process model, etc.).

---

## 2. Responsibilities (v0)

| Area | v0 responsibility |
|------|-------------------|
| **Orchestration** | Maintain a single coherent “run” of a user/objective through planned steps, subject to policy. |
| **Decomposition** | Where applicable, break objectives into sub-tasks and ordered or conditional steps (planner output as **contracted artifacts**, not logic here). |
| **Routing** | Select target **Agent** / **Model** / **Tool** (by identity or class) for each step according to rules and runtime availability signals. |
| **Dispatch** | Request execution of a step on the chosen target; wait for or observe completion according to the dispatch contract. |
| **State** | Hold and update **orchestration state** (what step, what status, what inputs/outputs references) for the run. |
| **Handoff** | Coordinated transfer of context, objectives, and constraints from one active agent to another, without ad-hoc “hidden” handoffs. |
| **Signaling** | Propagate the **required signals** (see §6) to interfaces, observability, and humans as appropriate. |
| **Legacy alignment** | Preserve the **architectural role** once associated with **Main Brain** (see §7) in a form suitable for a multi-tenant, policy-aware runtime. |

All of the above are **obligations of the design**; **implementation** of each remains **out of scope** for this file.

---

## 3. Non-responsibilities (v0)

The Control Plane v0 **does not** by contract:

- **Implement** agents, LLM calls, tool execution, memory storage, or persistent RAG (those are **Agent**, **Model**, **Tool**, **Memory**, **Storage** layers as documented elsewhere).
- **Replace** **Interface** (UX/API) or **Security/Guardrails** (policy source of truth) — it **consumes** decisions and constraints from them where specified.
- **Guarantee** outcomes of external systems; it only defines how requests and state are **formed** and **routed**.
- **Define** database schemas, wire formats, or deployment topologies in v0.
- **Claim** that any of this exists in the repository: **SAFE UNKNOWN** applies to anything not yet backed by real code.

---

## 4. Input contract (v0)

*Abstract inputs* (concrete encodings TBD at implementation time):

1. **Session / run context**  
   - Identity and scope as provided by the stack (e.g. user, tenant, session id).  
   - Stated **objective** or **user message** to advance.

2. **Policy & capability envelope**  
   - What the caller is **allowed** to do (tools, models, max steps) from **Security** / product policy — **not** invented by the Control Plane alone.

3. **Capability inventory (opaque)**  
   - References to **registered** agents, models, tools, workflows the router may use (the registry lives outside this contract in **Agent/Tool/Model** concerns).

4. **External events** (optional)  
   - e.g. human approval granted/denied, tool completion callbacks — as defined when interfaces exist.

**v0 rule:** if mandatory inputs are missing, the Control Plane does **not** guess; it emits an appropriate **signal** (e.g. **UNKNOWN** or **SAFE UNKNOWN**), not a fabricated run.

---

## 5. Output contract (v0)

*Abstract outputs*:

1. **Run record (logical)**  
   - Ordered steps with status: planned / running / done / failed / blocked.  
   - Pointers to artifacts (transcripts, tool I/O) held in **Storage/Memory/observability** as per global architecture — v0 only requires **identifiability** of such pointers, not their format.

2. **Dispatch instructions**  
   - For each step, **who** to invoke (agent class, model route, tool id) and **what** payload slice is in scope, within policy.

3. **Handoff package** (when required)  
   - Structured handoff to the next **Agent** (objective, constraints, memory handles as allowed by policy).

4. **Signals**  
   - The required **v0 signals** in §6, propagated upward or to humans.

5. **No hidden side effects in v0**  
   - The contract does not authorize silent writes outside defined dispatch and agreed persistence paths.

---

## 6. Required signals (v0)

These names are **normative** for any future implementation claimable as “MARS Control Plane v0”:

| Signal | When to use |
|--------|-------------|
| **UNKNOWN** | A required fact is missing; the plane cannot continue without user/system input or a registered capability. |
| **SAFE UNKNOWN** | Uncertainty is acknowledged explicitly; the plane continues only if policy allows a bounded default or deferred resolution; **no** silent assumption of facts. |
| **NEED HUMAN APPROVAL** | A step requires explicit human sign-off (HITL, high-risk action, policy threshold). |
| **SECURITY RISK** | A policy violation, potential injection, or credential/scope issue is detected or suspected; must not proceed with the risky path without **Security** resolution. |
| **STRUCTURE CHANGE** | The run cannot proceed with the current plan (goal shift, unrecoverable branch); replan, scope change, or new decomposition may be **needed**; interfaces should handle **safely** without uncontrolled side effects. |

*Note:* this list is for **orchestration-level** control; other layers may define additional signals. Control Plane v0 must **not** conflate or swallow these.

---

## 7. Relation to legacy “Main Brain”

In the **imported and documented** architecture, **Main Brain** described a central locus of task decomposition, routing, and “brain” lifecycle behavior. The Control Plane v0 is the **successor *role*** in a normalized MARS design:

- **Same conceptual center** for: orchestration, routing, and coherent progress through a run.
- **Explicit** separation: **planner**, **router**, **dispatcher**, **state**, and **handoff** as first-class *contract* components (see `components.md`) — rather than a monolithic “brain” with vague boundaries.
- **Not** a claim that Main Brain *code* exists or is ported; legacy items remain **documented/legacy** until proven otherwise.
- **SAFE UNKNOWN** applies to any feature attributed to “Main Brain” in old docs that has no in-repo implementation.

---

## 8. Document set

- `README.md` — entry, status, and pointers.  
- `contract.md` — this file.  
- `components.md` — v0 **component** boundaries (still **planned**, not code).

**Implementation status (honest):** the `control-plane/` tree contains **no** source code; only this documentation. Runtime folders elsewhere remain **planned** unless the repository gains real artifacts.
