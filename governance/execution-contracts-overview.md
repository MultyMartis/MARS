# MARS — Execution contracts overview

**Status:** **documented** — governance-only, **Phase S4**. **Not** runtime code, **not** orchestration, **not** a workflow engine, **not** autonomous planning.

**Purpose:** State what **execution contracts** mean in MARS: how work is **named**, **scoped**, **closed**, and **governed** in documentation and human-operated practice—without implying that any contract is **enforced** by an in-repo MARS process.

---

## 1. What an execution contract is (here)

An **execution contract** is a **governance semantics** agreement: the minimum shared meaning operators and contributors use so that **task**, **validation**, **artifact state**, and **reporting** do not drift into “fake runtime” narratives.

- Contracts **describe** expectations and boundaries.  
- They **do not** schedule work, queue jobs, or run agents.  
- They **do not** replace **human-in-the-loop (HITL)** judgment.

Canonical lightweight shapes live in:

- [task-envelope-standard.md](task-envelope-standard.md)  
- [execution-phase-model.md](execution-phase-model.md)  
- [validation-chain-semantics.md](validation-chain-semantics.md)  
- [artifact-lifecycle-rules.md](artifact-lifecycle-rules.md)  
- [execution-boundary-clarification.md](execution-boundary-clarification.md)

---

## 2. What execution contracts are **not**

| Not this | Why |
|----------|-----|
| **Runtime orchestration** | No in-repo MARS scheduler is asserted; see [execution-model.md](execution-model.md), [AGENTS.md](../AGENTS.md). |
| **Workflow engine semantics** | External engines (e.g. n8n) and doc workflows are **separate**; contracts do not imply engine state machines. |
| **Autonomous plans** | Plans and prompts are **human-directed** unless a **future** implementation exists and is **proven** in-tree. |
| **JSON/API truth** | Wire formats for a future runtime are **SAFE UNKNOWN** unless specified elsewhere with evidence. |

---

## 3. Relationship map (operational)

| Concept | Role in execution contracts |
|---------|------------------------------|
| **Task** | The bounded unit of intent: identity, scope, lane, constraints, expected outputs—see [task-envelope-standard.md](task-envelope-standard.md). Aligns with design-oriented [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md) without conflating **planned** schema with **today’s** handoff. |
| **Prompt** | **Human instructions** (and editor/agent prompts) that drive **Cursor**-layer execution; not automatically equal to a **governance** envelope or a **runtime** payload. |
| **Execution** | **Today:** human-operated edits and commands in Cursor (and related tools) per [execution-model.md](execution-model.md). **Future:** any other host is **planned** until proven. |
| **Report** | Mandatory **operational closure** when task rules require it: changed files, summary, git posture, **UNKNOWN** / **SECURITY RISK**—see [context-continuity-rules.md](context-continuity-rules.md), [AGENTS.md](../AGENTS.md). |
| **Validation** | **Meaning** of “validated” varies by layer—see [validation-chain-semantics.md](validation-chain-semantics.md). A **mention** of validation does **not** imply automation. |
| **Artifact** | Any durable output (doc, code, export, registry row). **Lifecycle** labels reduce drift—see [artifact-lifecycle-rules.md](artifact-lifecycle-rules.md). |
| **Lifecycle** | Human-recorded evolution (phases, deprecation, migration)—[execution-phase-model.md](execution-phase-model.md), [../logs/lifecycle-log.md](../logs/lifecycle-log.md) as **events**, not automatic state. |
| **Registry** | **Human-maintained** catalogs; registry presence ≠ runtime—[registry-architecture.md](registry-architecture.md), [runtime-registry-boundaries.md](runtime-registry-boundaries.md). |
| **SAFE UNKNOWN** | Explicit admission of missing evidence or binding; **not** a silent default—[AGENTS.md](../AGENTS.md), [system-signals-dictionary.md](system-signals-dictionary.md). |

---

## 4. Principles (S4 alignment)

1. **Human-executed** remains primary.  
2. **Cursor** remains the **documented** execution layer for repo work **today**.  
3. **REPORT** remains mandatory operational closure when required.  
4. **HITL** remains primary for approval and ambiguity.  
5. **Contracts** over implicit assumptions; **minimal** semantics over frameworks.  
6. **Documentation-first** stays active; governance does not imply shipped automation.

---

## 5. SAFE UNKNOWN

- Whether a **future** runtime will **enforce** any field of a task envelope automatically.  
- Exact mapping between **external** workflow payloads and MARS task IDs—only **as modeled** in docs until proven.
