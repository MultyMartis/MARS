# MARS — Failure Handling Model v0

**Status:** **documented** — **contract only**. This file defines how MARS **documentation** classifies execution failures, which **recovery actions** are permitted, and the **normative rules** that bound retries, idempotency, structure changes, and security escalation. It does **not** implement schedulers, retry engines, or policy enforcement. Per [../AGENTS.md](../AGENTS.md), **no** runtime behaviour is claimed unless code elsewhere in the repository proves it.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

The **Failure Handling Model** is the **normative taxonomy** and **action matrix** for **execution failures**: how a run or step moves from **detected failure** to **retry**, **abort**, **fallback**, or **human-gated** continuation, and which **system signals** must be raised or preserved. It sits **between**:

- **[../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md)** — bridge **failure modes** and **output** facets (`status`, `signals`).
- **[../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md)** — durable **`errors`**, **`state`**, and **checkpoint** metadata that must **not** contradict this model.
- **[execution-flow.md](execution-flow.md)** — **where** in the pipeline (`prompt` → … → `log`) failures are **detected** and **surfaced**.

**Honesty:** All rules below are **design-time** contracts for authors and future orchestration; **SAFE UNKNOWN** applies to numeric limits, backoff shapes, and storage backends until specified in later artefacts or implementation.

---

## 2. Failure types (v0 taxonomy)

Each failure **instance** should be classifiable under **exactly one** primary type for reporting and persistence; **compound** situations choose the **type that blocks honest continuation** first (e.g. policy breach → **validation failure** / security path before retry).

| Type | Definition | Typical bridge / flow alignment |
|------|------------|----------------------------------|
| **Execution error** | Executor or worker returned **failure**, threw, or produced a **deterministic error** for the step (non-timeout). Maps to bridge **Execution failure** where policy did not classify it as security-first. | [execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) §5 **Execution failure**; [execution-flow.md](execution-flow.md) **execute** / **validate**. |
| **Timeout** | Step or call **did not complete** within an **allowed** duration (**SAFE UNKNOWN:** wall-clock limits are product/runtime — not fixed in v0). | Bridge §5 **Timeout**; treat as failure for state unless policy defines bounded retry/resume. |
| **Partial completion** | **Some** side effects or substeps **committed** while **others** did not; outcome **not** safely classifiable as full success or clean failure. | Bridge output **`status`** **partial**; risks **duplicate** work on naive retry — see **§5** idempotency. |
| **Dependency failure** | **Upstream** dependency of the step **failed** or became **unavailable** (registry, route target, external service, prerequisite artefact). Distinct from **execution error** inside the step body when the step never reached a valid execute surface. | [execution-flow.md](execution-flow.md) **route** / **task**; **UNKNOWN** when binding missing. |
| **Validation failure** | **Post-execute** or **gate** checks **rejected** outputs (quality, schema, policy, acceptance criteria). Includes **security** validation stops when the **primary** narrative is “validation said no.” | **validate** stage; may emit **STRUCTURE CHANGE** or **SECURITY RISK** per [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md). |

---

## 3. Actions (v0 vocabulary)

| Action | Meaning | Constraints (v0) |
|--------|---------|-------------------|
| **Retry** | Re-attempt the **same** or **equivalent** step after a failure, within **documented** limits. | **Must** respect **§4** (no infinite retry), **§5** (idempotency), and **§4** (STRUCTURE CHANGE / SECURITY RISK). **Backoff** and **jitter** — **SAFE UNKNOWN** until specified. |
| **Abort** | **Stop** the run or task on a **terminal** failure path; **no** further automated steps except **audit** / **report**. | Must align with [../governance/state-model.md](../governance/state-model.md) terminal task/run semantics; persisted **finalize** semantics per [runtime-state-store-v0.md](../storage/runtime-state-store-v0.md). |
| **Fallback** | Continue with a **declared alternate** plan, executor, or degraded path **without** claiming equivalence to the primary path. | **Must not** silently widen scope; **UNKNOWN** / **SAFE UNKNOWN** for unspecified fallbacks. |
| **Escalate** | **Pause** automation and route to **NEED HUMAN APPROVAL** (or governance process) before retry, resume, or fallback that would **materially** change risk posture. | Mandatory when **SECURITY RISK** is raised (**§4**); recommended for irreversible or high–blast-radius retries. |

---

## 4. Rules (normative v0)

1. **No infinite retry** — Every retry policy **must** declare a **maximum attempt count** (or **equivalent** cap). After exhaustion: **abort** or **escalate**, not unbounded loops.
2. **Idempotency awareness** — Before **retry** on **partial completion** or **timeout**, the orchestration design **must** assume **at-least-once** execution unless a step is **proven** idempotent; prefer **escalate** or **checkpointed resume** per [../storage/checkpoint-resume-protocol-v0.md](../storage/checkpoint-resume-protocol-v0.md) over blind duplicate execution.
3. **Respect STRUCTURE CHANGE** — When **STRUCTURE CHANGE** applies, **do not** “retry the same plan” as the default: **replan** or **re-scope** per [system-signals-dictionary.md](../governance/system-signals-dictionary.md) and [state-model.md](../governance/state-model.md); retries apply only to **valid** slices of the **new** structure where policy allows.
4. **SECURITY RISK → escalate** — Any **SECURITY RISK** emission **blocks** unattended **retry** / **fallback** that could **amplify** harm; **typical next action** is **escalate** with **NEED HUMAN APPROVAL** where gates exist ([../security/approval-gates.md](../security/approval-gates.md)). Align with [risk-register.md](../governance/risk-register.md) §7.

---

## 5. Idempotency and duplicate execution (design obligations)

- **Repeated execution must not corrupt state** — Retries and resumes **must** be designed against **append-only** and **superseding** record rules in [runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) §5–6.
- **Duplicate tool calls** — **Documented** controls (deduplication keys, idempotency tokens, or **explicit** human approval before second invocation) are **required** for gated or side-effecting tools when retry is allowed; **SAFE UNKNOWN** for concrete token format until Tool layer contracts exist.

---

## 6. Relation to other artefacts

| Artefact | Relation |
|----------|----------|
| [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) | Bridge **failure modes** and **output** **`signals`** are the **upstream** surface this model **refines** and **aligns** with (no contradiction). |
| [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) | **`errors`** classification and **recovery** narratives **persist** here; **checkpoints** pair with [checkpoint-resume-protocol-v0.md](../storage/checkpoint-resume-protocol-v0.md). |
| [execution-flow.md](execution-flow.md) | **Stage**-level **where** failures appear and **typical signals** (e.g. **execute**, **validate**). |
| [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) | **Canonical** names for **UNKNOWN**, **SAFE UNKNOWN**, **NEED HUMAN APPROVAL**, **SECURITY RISK**, **STRUCTURE CHANGE** on failure paths. |
| [../governance/state-model.md](../governance/state-model.md) | Task/run **transitions** on failure, **parked**, and **terminal** states. |
| [../governance/risk-register.md](../governance/risk-register.md) | **Hazards** (retry chaos, duplicate execution, inconsistent state) **trace** to this model’s mitigations. |
| [workflow-v0.md](workflow-v0.md), [task-contract-v0.md](task-contract-v0.md) | **Task** as central unit; **workflow** run semantics. |

---

## 7. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Failure Handling Model v0** — purpose, failure types, actions, normative rules, idempotency notes, cross-refs. |

---

*End of Failure Handling Model v0.*
