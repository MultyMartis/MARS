# MARS — Cost / Token Budget v0

**Status:** **documentation only** — fields and **outcomes** for **limiting** model **usage** per **run** and **project**. **No** billing integration, **no** telemetry pipeline, **no** secrets or provider pricing keys in-repo ([../AGENTS.md](../AGENTS.md)).

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

- Make **cost** and **token** growth **explicit** in design so **uncontrolled** spend and **runaway** context are **risk-managed** ([../governance/risk-register.md](../governance/risk-register.md)).
- Tie **budget** checks to **model routing** ([model-routing-v0.md](model-routing-v0.md)) and **future** **observability** (Stage **12** — **not** specified as implementation here).

**SAFE UNKNOWN:** Currency, tax, regional pricing, **exact** token counting method per provider, and **real-time** quota backends are **out of scope** for v0.

---

## 2. Budget record fields (v0)

A **budget** **record** (per run, per project, or composite — encoding **SAFE UNKNOWN**) **should** be able to carry:

| Field | Description |
|-------|-------------|
| **project_id** | Authoritative project scope ([../registry/project-registry.md](../registry/project-registry.md)). |
| **run_id** | Workflow / execution run identifier ([../workflows/workflow-v0.md](../workflows/workflow-v0.md), [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md)). |
| **model_id** | Registry id ([model-registry-v0.md](model-registry-v0.md)) for the **call** or **aggregate** row. |
| **max_tokens_input** | Upper bound on **input** tokens for the **call** or **phase**. |
| **max_tokens_output** | Upper bound on **completion** tokens. |
| **max_cost_per_run** | Soft/hard cap on **normalised** cost units for the **run** (unit definition **SAFE UNKNOWN** until finance + provider adapters exist). |
| **max_cost_per_project** | Aggregate cap across runs for the **project** in a window (window **SAFE UNKNOWN**). |
| **escalation_threshold** | Level at which **WARN** or **NEED HUMAN APPROVAL** is emitted before a hard **DENY** (design-time threshold). |

---

## 3. Budget outcomes (v0)

| Outcome | Meaning |
|---------|---------|
| **ALLOW** | Within limits; proceed **subject** to other policy checks. |
| **WARN** | Approaching threshold; **may** proceed with **logged** / **observable** warning (**future** observability); **must** feed **risk** review if recurring. |
| **DENY** | **Must not** invoke model (or **must** **abort** **pending** call); emit canonical **signals** per [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md). |
| **NEED HUMAN APPROVAL** | **Human** decision required to **raise** caps, **switch** **cost_class**, or **continue** a **borderline** run ([../security/approval-gates.md](../security/approval-gates.md)). |

---

## 4. Relation to observability (future)

- Stage **12** **should** emit **per-call** **token** and **cost** **estimates** **into** an **observability** SoT **when** it exists — **not** evidenced in Phase **1** repo.
- **WARN** / **DENY** outcomes **should** be **correlatable** by **run_id** for **post**-**incident** review.

---

## 5. Relation to model routing

- **model_routing** **must** treat **cost budget** as an **input** ([model-routing-v0.md](model-routing-v0.md)); **routing** **must not** select a **model_id** that **violates** **max_tokens_input** / **context_window** **feasibility** or **max_cost_per_run** **eligibility**.
- If **only** **over-budget** models remain, outcome is **DENY** or **NEED HUMAN APPROVAL**, **not** silent override.

---

## 6. Relation to risk register

- **Uncontrolled** token/cost growth is a **named** **risk**; mitigations reference this document and [model-policy-v0.md](model-policy-v0.md).
- **Material** changes to caps or defaults **should** update [../governance/risk-register.md](../governance/risk-register.md) when **posture** shifts (**§3**).

---

## 7. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Cost / Token Budget v0** — fields, outcomes, relations to observability (future), routing, risk register. |

---

*End of MARS Cost / Token Budget v0.*
