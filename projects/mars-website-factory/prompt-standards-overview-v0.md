# MARS Website Factory — Prompt Standards Overview v0

**Status:** **documentation only** — **prompt discipline and operational architecture** for the Website Factory. **Not** a prompt engine, **not** a runtime, **not** an autonomous orchestrator, **not** a hidden system-prompt library, **not** evidence of agent execution in this repository.

**Version:** v0.

**Related:**

- Workflow: [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [workflow-map.md](workflow-map.md).
- Artifacts: [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md), [artifact-types-v0.md](artifact-types-v0.md).
- Honesty: [safe-unknown-boundary.md](safe-unknown-boundary.md), [`../../AGENTS.md`](../../AGENTS.md).
- Governance: [`../../governance/execution-model.md`](../../governance/execution-model.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md).
- Sibling prompt-standard docs: [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md), [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md), [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md), [reporting-standard-v0.md](reporting-standard-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md), [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md), [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md).

---

## 1. Purpose

The **Prompt Standards Layer v0** normalizes **how instructions are written, executed, and reported** across the Website Factory — for **humans operating Cursor**, for **planned specialist agents**, and for **future orchestrators**. It is the **operational interface** between **workflow stages**, **artifacts**, **QA**, and **HITL gates**.

This layer answers **operational** questions:

- What does a **well-formed prompt** look like in the factory?
- What is an **agent** allowed to assume vs **forbidden** to assume?
- How does **Cursor** execute a prompt **honestly** and **report** it?
- Where does **HITL** intervene and how is **escalation worded**?
- How is **SAFE UNKNOWN** signaled inside prompt and report bodies?
- How do **artifacts** transfer between stages **without scope drift**?

It does **not** answer **implementation** questions about runtime, schedulers, queues, dispatchers, or autonomous decision-making.

---

## 2. Why prompt standards matter

### 2.1 Orchestration requires normalization

The factory is **multi-stage** and **multi-role** ([website-factory-workflow-v0.md](website-factory-workflow-v0.md) §S01–S15). If each stage uses ad-hoc prose, downstream agents (or humans) must **re-interpret intent**, which:

- inflates clarification loops;
- breaks **artifact integrity** at handoff boundaries;
- weakens **QA traceability** (a finding cannot cite a stable instruction);
- silently expands or contracts **scope**;
- prevents future **Control Plane** routing per [`../../control-plane/contract.md`](../../control-plane/contract.md) from binding the same intent twice.

Normalized prompt structure (see [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md)) keeps **intent, scope, and constraints** comparable across stages and projects.

### 2.2 Trust depends on bounded prompts

A factory stage must produce **predictable, auditable** outputs. That requires:

- explicit **objective** (what counts as “done”);
- explicit **constraints** (what is forbidden);
- explicit **artifacts in / out** (what crosses the boundary);
- explicit **escalation rules** (when to stop and ask).

A prompt that omits these is **not** a factory prompt — it is a wish.

### 2.3 “One huge magical prompt” is forbidden

A single, sprawling, undifferentiated prompt that asks for **everything in one shot** is **not** acceptable in the factory. It:

- collapses workflow stages;
- destroys artifact boundaries;
- hides assumptions;
- defeats HITL gates;
- mixes documentation with runtime claims;
- forces fabrication when the agent runs out of evidence.

**v0 rule:** any factory request must be **decomposable** into stage-scoped, artifact-scoped, and QA-scoped prompts that respect [website-factory-workflow-v0.md](website-factory-workflow-v0.md). The orchestrator (today: a **human**) is responsible for that decomposition.

---

## 3. Relationship map

```text
                workflow stage
                      │
                      ▼
                 artifact(s)
                      │
                      ▼
                ┌──── prompt ────┐
                │ (structured)   │
                └─────┬──────────┘
                      ▼
                  execution
                  (Cursor / human)
                      │
                      ▼
                    report
                      │
                      ▼
                 QA / Validator
                      │
                      ▼
                   HITL gate
                      │
                      ▼
            artifact freeze / next stage
```

### 3.1 Workflow ↔ prompt

- Each **stage** ([website-factory-workflow-v0.md](website-factory-workflow-v0.md) S01–S15) is a **prompt boundary**.
- A prompt **does not** cross stages without an explicit handoff artifact ([artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md)).

### 3.2 Artifact ↔ prompt

- **`artifacts in`** = what the prompt is allowed to read or rely on.
- **`artifacts out`** = what the prompt must produce, named per [artifact-types-v0.md](artifact-types-v0.md).
- Prompts **must not** invent new artifact classes silently.

### 3.3 Report ↔ prompt

- Every prompt **must** define **reporting expectations** ([reporting-standard-v0.md](reporting-standard-v0.md)).
- The report is the **evidence** that the prompt was executed honestly.

### 3.4 HITL ↔ prompt

- HITL gates ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [workflow-map.md](workflow-map.md) §HITL checkpoints) **interrupt** prompt chains.
- A prompt **cannot** approve itself, freeze its own artifact, or waive its own blocker.

### 3.5 QA ↔ prompt

- QA prompts ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md)) are **separate** from production prompts.
- They consume artifacts and emit **QA result payloads** per [qa-result-payloads-v0.md](qa-result-payloads-v0.md).

---

## 4. Relationship to future orchestration / runtime

When (and **if**) a Control Plane, Execution Bridge, or runtime exists per [`../../governance/execution-model.md`](../../governance/execution-model.md) and [`../../mars-runtime/execution-bridge-v0.md`](../../mars-runtime/execution-bridge-v0.md):

- The same **prompt sections** (objective, scope, constraints, artifacts in/out, QA, escalation) become **task fields**.
- The same **report structure** ([reporting-standard-v0.md](reporting-standard-v0.md)) becomes **task output**.
- The same **HITL boundary** becomes **`hitl_gates`** on a Task Contract row.

**Until then**, prompt standards are **human-facing operational discipline**. Nothing here implies that a runtime parses these documents or enforces them automatically.

---

## 5. Honesty boundary (explicit non-claims)

This layer **does not**:

- ship a runtime prompt engine;
- guarantee any agent behavior (LLM outputs remain probabilistic);
- expose hidden system prompts that operate behind the user’s back;
- assume autonomous decision-making by any agent;
- imply Cursor enforces these standards beyond what the user/operator does;
- imply that planned factory agents ([agent-map.md](agent-map.md)) exist as live processes.

This layer **does**:

- define **vocabulary** and **structure** for instructions;
- define **expected agent behavior** in prose;
- define **report and escalation discipline**;
- align with **SAFE UNKNOWN** per [safe-unknown-boundary.md](safe-unknown-boundary.md) and `AGENTS.md`.

> **Prompts are operational interfaces, not AGI behavior contracts.** Any deviation between the prompt’s stated objective and what an LLM actually produces is **handled by QA, HITL, and reporting**, not assumed away.

---

## 6. Scope of this overview

| In scope | Out of scope |
|----------|--------------|
| Prompt structure semantics | Prompt-engine implementations |
| Agent behavioral expectations (prose) | LLM provider routing (see `../../models/`) |
| Cursor execution discipline for the factory | Cursor extension code / daemons |
| Report and escalation wording | Persisted state stores |
| HITL boundary semantics | Approval signing infrastructure |
| Artifact transfer rules between prompts | Wire formats for artifacts |
| QA prompt patterns | Automated visual regression engines |
| Frontend prompt discipline (source-first) | Build runners or CI provisioning |

---

## 7. Document set

| Document | Role |
|----------|------|
| [prompt-standards-overview-v0.md](prompt-standards-overview-v0.md) | **This file** — purpose, philosophy, non-claims. |
| [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) | Normalized sections, minimal vs production vs HITL vs QA vs frontend prompts. |
| [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md) | Behavioral rules for agents executing factory prompts. |
| [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md) | Prompt → execute → report loop in Cursor; safety rules. |
| [reporting-standard-v0.md](reporting-standard-v0.md) | Normalized REPORT format and lane variants. |
| [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md) | Mandatory HITL gates, escalation triggers. |
| [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md) | SAFE UNKNOWN behavior in prompts and reports. |
| [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) | How artifacts move between prompts/stages. |
| [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) | QA-specific prompt structure and evidence rules. |
| [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md) | Frontend-specific prompt discipline (Gulp-oriented). |

---

## 8. Operating principles (one-line summary)

1. **One stage, one prompt boundary.**
2. **No prompt without scope, constraints, and reporting expectations.**
3. **No fabrication. No silent assumptions. SAFE UNKNOWN if evidence is missing.**
4. **Artifacts crossing a prompt must be named.**
5. **HITL is never inside the agent — it is always outside.**
6. **A report is the only evidence that a prompt ran honestly.**
7. **Cursor executes prompts; it does not own the factory.**
8. **Documentation-first stays documentation-first until evidence says otherwise.**

---

## 9. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial prompt-standards overview (documentation only). |
