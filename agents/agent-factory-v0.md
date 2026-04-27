# MARS — Agent Factory v0 (planned contract)

**Status:** planned — contract for the **Agent Factory** process. No build service, no CI job, and no automatic code generation in this repository. **Agent Builder** is a **role** in the Agent Registry; the **Factory** is the governed process that proposes or updates **agent cards** and the **registry** when a runtime exists elsewhere.

**Version:** v0.

**Terminology:** **Control Core** = **Control Plane** (see `../control-plane/contract.md`).

---

## 1. Purpose

The **Agent Factory** is the design-time / gating path by which MARS can **introduce or change agent definitions** in a controlled way. It does not spawn live agents; it produces or revises **agent cards** (and, in a future implementation, bound implementations) that the **Agent Registry** holds, and the **Control Plane** reads for routing.

**Legacy:** the documented **Factory Engineer** role (see §10) maps to **Agent Builder** operating **within** the Agent Factory process.

---

## 2. When the Agent Factory is triggered (v0)

The Factory path is not the default for every run. v0 intends it when one or more of the following hold:

- A **Workflow** or **Task** requires an agent name that is **absent** from the Agent Registry, or the **card** is only **draft** and policy forbids use (**STRUCTURE_CHANGE** / **UNKNOWN** in workflow terms — see `../workflows/workflow-v0.md`).
- A product or operator **explicitly** requests a new or revised **agent definition** (out-of-run).
- The scope of an **existing** agent must change (new **tools**, **permissions**, or **risk** profile) and **governance** requires a Factory run before adoption.

The **Control Plane** may branch the orchestrated run to a **Factory** subprocess (human-driven in v0 documentation) when policy says so — not a silent auto-loop.

---

## 3. What the Factory can create (v0)

- Proposals for a **new** agent **card** (per `agent-card-template.md` and `registry.md`).
- Proposals for an **update** to an **existing** agent **card** (new version in **changelog**; same `name` with revised fields where allowed).
- Documentation of **required** **Validator** (FlyCheck successor) review for **risky** definitions (see §4, §8).
- Metadata for **registry** ingest (format TBD at implementation) — in v0 this means **files in the repo** or an agreed store, not an API in this directory.

The Factory **cannot** by itself set **active** in a way that **claims** production without implementation evidence and team process (see `registry.md` status rules).

---

## 4. What the Factory cannot create (v0)

- Executable agent runtimes, binaries, or undeclared side processes — out of scope for this **contract**; implementation belongs in future Agent / Tool / Model codebases.
- Ad-hoc agent identities that **bypass** **Security** / permissions / tool review.
- Production **active** **status** for a card without meeting registry honesty rules and without **Validator** sign-off for **non-trivial** risk (see §5, §8).
- Secrets or live **credentials** on **cards** — **forbidden** as card content; use Security-approved **secret** handles in a future design.

---

## 5. Required human approval gates (v0, normative intent)

HITL is **required** for at least:

- A **new** agent **card** with **non-trivial** **permissions** (broad data access, external **egress**, **admin** tools).
- **Any** increase in tool access, model capability, or **risk_level** on an existing card beyond policy **thresholds** (thresholds TBD; **NEED HUMAN APPROVAL** in workflow signals).
- Adoption of a **card** that the **Validator Agent** (legacy **FlyCheck** role) flags as failing validation requirements (see `agent-builder-contract.md`).

**NEED HUMAN APPROVAL** is the default **signal** for these Factory outcomes when automation cannot **prove** safety.

---

## 6. Relation to Control Plane

- The **Control Plane** **reads** the **registry** to route; it does **not** author cards on the **hot** execute path in v0 without a **Factory** handoff.
- When a run **requires a missing** role, the **Control Plane** may emit **UNKNOWN** / **STRUCTURE_CHANGE** and hand off to a **Factory** process (human/operator) that **produces** a proposal; after adoption (registry update), the **Control Plane** resumes **routing**.
- The **Control Plane** must not invent **registry** entries without the **Factory** / **governance** path when **policy** requires it.

---

## 7. Relation to Workflow Layer

- **Workflows** and **Task Contract v0** (`../workflows/task-contract-v0.md`) reference **required_agents**; if unmet, the **workflow** may **branch** to the Agent Factory (see `../workflows/execution-flow.md`, `workflow-v0.md`).
- Factory work is **usually** out-of-band **relative to** a single user **prompt**; resuming the **same** Task after a **registry** update is a new run segment in v0 semantics (**STRUCTURE_CHANGE** may **clear** old plan steps).

---

## 8. Relation to Agent Registry

- The **Registry** is the catalog of record for agent **cards** (`registry.md`).
- **Factory** outputs are **proposals** until **ingested**: a new **card** or a **card** update (with **changelog**).
- Ingestion is **governed**; **draft** → **planned** (or other **status**) transitions are **not** **automatic** **active** (see `registry.md` **status** values).
- **FlyCheck** (→ **Validator Agent**) **must** validate **risky** **agent** **definitions** **before** **adoption** (see `agent-builder-contract.md` and the **Validator** row in `registry.md`).

---

## 9. Allowed outcomes of a Factory / Builder run (v0)

| Outcome | Meaning |
|--------|--------|
| **New** agent **card** proposed | Full new **card** content ready for review / ingest. |
| **Existing** agent **card** **update** proposed | Delta or full **card** revision with **changelog**; not **live** until **accepted**. |
| **Reject** **agent** **creation** | No new **card**; reasons recorded (Security, duplication, unbounded scope). |
| **SAFE UNKNOWN** | **Requirements** **unclear**; no **card** change until clarified (or a bounded **draft** only, per policy). |
| **NEED HUMAN APPROVAL** | Non-trivial **permissions** / **tools** / **risk**; **human** gate before adoption (§5). |

**Implementation honesty:** this repository contains no Factory code; only this **contract**.

---

## 10. Document set (Agent layer)

| File | Role |
|------|------|
| `agent-factory-v0.md` | This file. |
| `agent-builder-contract.md` | Agent Builder inputs/outputs and checks. |
| `registry.md` | Registry and **status** values. |
| `agent-card-template.md` | **Card** fields. |
| `README.md` | Index. |

**Legacy:** **Factory Engineer** (documented) → **Agent Builder** + **Agent** **Factory** process; this is **not** a claim that legacy code exists in-repo.
