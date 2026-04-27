# MARS — Guardrails v0 (system contract)

**Status:** **documented contract only** — normative expectations for design, reviews, and any future implementation. **No** enforcement engine, policy DSL, or runtime in this repository proves these rules today (see [README.md](README.md)).

**Version:** v0. Revisable with governance versioning; supersession must be explicit.

---

## 1. Purpose

**Guardrails v0** defines **non-negotiable behavioral and validation expectations** for how MARS (as a system) treats **inputs**, **outputs**, **prompts**, **unknowns**, and **failure visibility**. It is the **Security / Guardrails layer** contract slice: what **must** be true in principle before an entity is considered **safely activatable** and before workflows may treat a step as **closed**.

---

## 2. Role in the system

| Role | Description |
|------|-------------|
| **Truth boundary for automation** | Guardrails state what automated paths **may not** do (invent facts, hide uncertainty, proceed without declared checks). |
| **Bridge to Validator / Quality** | Validation rules referenced here align with **validate** in `../workflows/execution-flow.md` and agent **validation** fields in cards. |
| **Precondition for “active” entities** | Together with [permissions-v0.md](permissions-v0.md) and registry discipline, guardrails define **activation invariants** (§9). |

---

## 3. Relations to other layers (contractual, not implementation)

| Layer | Relation |
|-------|----------|
| **Control Plane** | Planner, Router, Dispatcher, and Validator **must** assume guardrails when decomposing tasks, routing steps, and merging outcomes. **Signals** (see §8) are the **declared vocabulary** for escalation and parking. |
| **Workflow Layer** | Task contract **signals** and **hitl_gates** (`../workflows/task-contract-v0.md`) operationalize **NEED HUMAN APPROVAL** and related stops; guardrails define **why** those gates exist. |
| **Agent Registry** | Only **registered** agents with complete **passport-shaped** definitions are eligible for routing; guardrails apply to **how** their I/O is validated, not to replacing the registry as SoT. |
| **Agent Factory** | Create/update paths **must** respect guardrails outcomes (**SAFE UNKNOWN**, **NEED HUMAN APPROVAL**) per `../agents/agent-factory-v0.md` and `../agents/agent-builder-contract.md`. |
| **Tool Layer** | Tools are **high-risk surfaces**; input/output validation and side-effect awareness apply **per tool** once a Tool Registry exists (`../governance/master-build-map.md` Stage 9). Until then, tool behavior outside docs is **SAFE UNKNOWN**. |
| **Introspection** | Introspection **must not** fabricate facts; composition policy and **SAFE UNKNOWN** in `../interfaces/introspection-v0.md` align with **no hallucination** and **SAFE UNKNOWN enforcement** here. |

---

## 4. Input validation rules (v0)

1. **Schema and scope** — Task and step **inputs** must be checked against declared **scope_in**, **constraints**, and any **entity passport** fields that define allowed inputs (formats, max size, allowed sources).
2. **Source integrity** — Inputs that claim to come from a **registry row**, **log event**, or **file path** must be **verified** against that SoT when a consumer relies on them; if verification is impossible, emit **SAFE UNKNOWN** for the unverifiable slice (see `../governance/universal-entity-operations.md` §6).
3. **Untrusted text** — User and external content is **untrusted**. Treat embedded **instructions that contradict** system or task constraints as **policy-relevant** (prompt injection awareness, §6); do not **elevate** such content to system instructions without an explicit, logged **human** or **control-plane** policy path (contract-level; no implementation claim).
4. **No silent widening** — Validators **must not** silently expand scope, add assumptions not in **scope_in**, or “fix” missing inputs with guessed values without emitting **SAFE UNKNOWN** or **UNKNOWN** per policy.

---

## 5. Output validation rules (v0)

1. **Acceptance alignment** — Step and task **outputs** must be checked against **acceptance_criteria** and declared **outputs** in the Task Contract.
2. **Evidence for factual claims** — Any output that states **implementation exists**, **registry contains**, or **event occurred** must cite **in-repo** evidence or external SoT **linked in docs**; otherwise the output must carry **SAFE UNKNOWN** for that claim (anti-fabrication).
3. **Signal propagation** — If validation detects policy violation, injection pattern, or structural inconsistency, the **appropriate v0 signal** must be attached to task/orchestration state (see [system-signals-dictionary.md](../governance/system-signals-dictionary.md) §2; includes **UNKNOWN**, **SAFE UNKNOWN**, **NEED HUMAN APPROVAL**, **SECURITY RISK**, **STRUCTURE CHANGE**, etc.) per `../workflows/task-contract-v0.md` §3.
4. **No silent downgrade** — A failed validation **must not** be reported as success. **Partial** success must be **explicit** (which criteria passed/failed).

---

## 6. Prompt injection awareness (v0)

- **Definition (contract):** Attempt to override **goals**, **constraints**, **permissions**, or **system** instructions using **untrusted** content (user message, tool return, web payload).
- **Expectations:** Routing and validation treat **contradictions** between untrusted content and **task/registry** truth as **security-relevant**. Resolution paths include **blocking**, **narrowing scope**, **HITL**, or **SAFE UNKNOWN** — exact mechanics are **implementation**; v0 only requires that **no** path **silently** obeys attacker-shaped instructions.
- **Link to signal:** Suspected injection or policy escape → **SECURITY RISK** (and often **NEED HUMAN APPROVAL** before retry).

---

## 7. SAFE UNKNOWN enforcement

- When **evidence is missing** for a field, id, file, credential topology, or runtime behavior, the system **must** emit **SAFE UNKNOWN** for that **slice** — not invented detail and not a false **PASS** (see `../governance/universal-entity-operations.md` §6, `../interfaces/introspection-v0.md`).
- **SAFE UNKNOWN** is **not** permission to skip gates: it is an **honest** state that may still **block** or require **human** decision per workflow policy.

---

## 8. No hallucination rule (v0)

- **Normative:** No MARS-facing output may **present fabricated** registry rows, lifecycle events, file contents, metrics, or **implementation** claims.
- **Corollary:** Prefer **bounded** statements (“not in-repo”, “not recorded in `logs/lifecycle-log.md`”) over confident **false** specifics.

---

## 9. No silent failure rule (v0)

- **Normative:** Errors, denials, missing bindings, and validation failures **must** surface as **visible state** (signals, explicit failure reason, or **SAFE UNKNOWN** / **UNKNOWN**) — not as **empty success**, **omitted** logs, or **unlogged** skipped steps.
- **Corollary:** “Fail closed” for routing when permissions or registry binding are absent (`../workflows/execution-flow.md`) is consistent with this rule.

---

## 10. Activation invariant (no active entity without full contract)

No **entity** (agent, workflow definition, tool, integration) may be treated as **active** in MARS semantics without **all** of:

1. **Passport** — identity and contract fields per entity type (for agents: card filled per `../agents/agent-card-template.md`; other types when schemas exist).
2. **Registry entry** — row or catalog entry in the appropriate **registry** (e.g. `../agents/registry.md` for agents).
3. **Permissions** — explicit declaration per [permissions-v0.md](permissions-v0.md) in the entity passport (no implicit superuser).
4. **Validation rules** — how inputs/outputs are checked, referenced in passport or linked contract (Validator path, acceptance hooks, or explicit **SAFE UNKNOWN** for unvalidated slices).

**Documentation note:** “**active**” here is the **lifecycle** sense used in agent cards and registry; it is **not** a claim that a process is running in-repo.

---

## 11. Relation to signals

See [README.md](README.md) §“Signals” and [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) for the **normative** signal index and **canonical** names. This document **defines** guardrail obligations; signals **communicate** guardrail and policy state to orchestration and humans.

---

## 12. SAFE UNKNOWN (repository)

Whether a future **policy engine** enforces §4–§9 automatically is **not** proven in this tree — **SAFE UNKNOWN** for runtime enforcement until `mars-runtime/` or equivalent ships with tests/docs proving behavior.
