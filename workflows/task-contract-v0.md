# MARS — Task Contract v0 (planned)

**Status:** **planned** — **schema contract** for a **Task** in MARS. No JSON Schema file, no API, and no persistence format is mandated in v0. Fields are **normative** for design and for any future implementation.

**Version:** v0.

---

## 1. Purpose

A **Task** is the **atomic unit of work** the **Control Plane** can schedule and track on top of a **user/system prompt** and **plan** output. The Task Contract v0 **bundles** goal, scope, I/O, risk, **required agents**, **HITL**, and **signals** in one place so that **workflows**, **Agent Registry**, and **Agent Factory** paths stay **aligned**.

---

## 2. Required fields (v0)

| Field | Description |
|-------|-------------|
| **id** | Stable identifier for this task within a run (format TBD at implementation; must be **unique** in run scope in v0 intent). |
| **title** | Short human-readable label. |
| **goal** | What success means for this task, in one or two sentences. |
| **scope_in** | What is **in** scope (explicit). |
| **scope_out** | What is **out** of scope (prevents scope creep). |
| **inputs** | References and blobs the task consumes (user message, files, memory handles, prior step outputs). |
| **outputs** | Expected artifacts (docs, code, diffs, decisions, metrics handles). |
| **acceptance_criteria** | Checkable conditions for “done” (incl. validation hooks). |
| **constraints** | Time, cost, model class, data residency, no-external-API, etc. |
| **risk_level** | e.g. low / medium / high (enum TBD); drives **HITL** and **Security** treatment. |
| **required_agents** | **Agent** card **names** (from **Agent Registry**) that must participate or own the work. |
| **hitl_gates** | Where **human** approval is required (step ids or conditions); ties to **NEED HUMAN APPROVAL**. |
| **signals** | Set or list of **system signals** raised or to be raised for this task (see §3 and [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md)). **v0-allowed** **canonical** values: **UNKNOWN**, **SAFE UNKNOWN**, **NEED HUMAN APPROVAL**, **SECURITY RISK**, **STRUCTURE CHANGE**, **CONTEXT MIGRATION NEEDED**, **GIT CHECKPOINT NEEDED**, **NO GIT CHECKPOINT**. |

**SAFE UNKNOWN** may appear as a field **value** only in **documentation** for undecided fields, or as a **runtime signal** in `signals` per policy — do not conflate "not filled" with a silent default.

---

## 3. Signals field (v0)

The **signals** field is **for orchestration and observability**: it records **which** of the v0 system signals **apply** or **must be** emitted for this task. Full **canonical** definitions, **alias** policy, and per-signal **semantics** are in [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md).

- **UNKNOWN** — **Cannot** start or **cannot** continue until missing binding is resolved (e.g. missing **required agent** in registry with no **Agent Factory** path).
- **SAFE UNKNOWN** — Ambiguity permitted only under explicit, bounded policy.
- **NEED HUMAN APPROVAL** — **hitl_gates** must be **satisfied** before downstream steps.
- **SECURITY RISK** — **Security** / **Validator** / **Control Plane** must not proceed without **resolution** per `../control-plane/contract.md`.
- **STRUCTURE CHANGE** — **Plan** or **Task** must be **re-decomposed** (e.g. wrong **scope_in**, impossible **required_agents** set).
- **CONTEXT MIGRATION NEEDED** — **Context** / **memory** / **self-describe** **artifacts** need **rebuild** or **migration** before the run (or handoff) can be **trustworthy** (see dictionary).
- **GIT CHECKPOINT NEEDED** — A **git** **milestone** (commit / push per policy) is **warranted** for **audit** or **rollback**; **not** a default for **small** doc edits.
- **NO GIT CHECKPOINT** — **Explicit** **opt-out** of a **git** **checkpoint** for this work unit; use when “no commit” must be **visible** alongside **AGENTS.md** and **git-rules** defaults.

**Note:** A task may list **zero** or **several** signals; **Control Plane** is the **orchestrated** source of truth for **emission** when an implementation exists.

---

## 4. Relation to Agent Factory

If **required_agents** references a **name** that **does not** exist in the **Agent Registry** (or is **draft** only and policy forbids use):

- v0 **contract** allows a **structure** where the run **parks** with **STRUCTURE CHANGE** and/or **UNKNOWN** and a **product-defined** path invokes **Agent Builder** to **create** or **update** definitions and the **registry** (see `workflow-v0.md` §4).
- **No** v0 claim that this is automatic or implemented.

---

## 5. Example (illustrative only, not a runtime payload)

```text
id: "task-001"
title: "Harden public API"
goal: "List and fix critical API security gaps."
scope_in: "Read-only on repo, no prod deploy"
scope_out: "Mobile app, billing"
inputs: { "repo_ref": "...", "policy_ref": "..." }
outputs: { "report": "md", "diffs": "optional" }
acceptance_criteria: [ "Risks enumerated", "Patches proposed or SAFE UNKNOWN" ]
constraints: { "no_external_egress": true }
risk_level: "high"
required_agents: [ "Validator Agent", "Coding Agent" ]
hitl_gates: [ "before_any_patch_apply" ]
signals: [ "NEED HUMAN APPROVAL", "SECURITY RISK" ]
```

This block is **documentation**; v0 does **not** require YAML/JSON in-repo.
