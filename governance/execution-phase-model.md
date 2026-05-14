# MARS — Execution phase model

**Status:** **documented** — governance-only, **Phase S4**. **Operational semantics** for how work **may** be talked about over time. **Not** an automation state machine, **not** a runtime enum, **not** enforced transitions.

**Purpose:** Give a **minimal shared vocabulary** for phases so that **workflow semantic drift** and “where are we in the run?” confusion stay bounded—while keeping **human-only** paths legitimate.

---

## 1. Principles

- **Not all phases always exist** for every task. Skip irrelevant labels; do not invent ceremony.  
- **Phases may be human-only** (no tool, no queue, no state store).  
- **Phases describe narration and discipline**, not daemons or schedulers.  
- **REPORT** and **parallel Cursor chat** discipline remain authoritative for **closure** and **lanes**—[context-continuity-rules.md](context-continuity-rules.md), [parallel-cursor-chat-work-mode-v0.md](parallel-cursor-chat-work-mode-v0.md).

---

## 2. Minimal phase vocabulary (illustrative)

| Phase | Typical meaning (governance) |
|-------|------------------------------|
| **Intake** | Task received: rough goal, lane guess, obvious exclusions. May be a single message. |
| **Clarification** | Questions resolved or explicitly deferred as **SAFE UNKNOWN** with bounds. |
| **Stabilization** | Contracts/governance/indexes updated so the next session can re-ground—aligns with [stabilization-vs-expansion.md](stabilization-vs-expansion.md). |
| **Execution** | Humans and Cursor perform scoped edits/commands—**today’s** real execution layer per [execution-model.md](execution-model.md). |
| **Validation** | Applied **meanings** per [validation-chain-semantics.md](validation-chain-semantics.md)—often human review or checklist. |
| **Report** | Operational closure: `# REPORT — …`, changed files, git posture, UNKNOWNs—[AGENTS.md](../AGENTS.md). |
| **Checkpoint** | Optional **git** milestone when policy warrants—**not** default for small docs; see Web-GPT git rules and task instructions. |
| **Migration** | Context/repo/chat handoff package per [context-continuity-rules.md](context-continuity-rules.md); may add lifecycle line. |
| **Archival / deprecation** | Artifact or doc path marked historical or superseded—[artifact-lifecycle-rules.md](artifact-lifecycle-rules.md), [documentation-entropy-rules.md](documentation-entropy-rules.md). |

**Ordering:** **Not** strictly linear. Example: **Report** may follow **Validation**; **Clarification** may recur; **Stabilization** may precede or follow **Execution** depending on task type.

---

## 3. Alignment with existing lifecycle semantics

- **Lifecycle log** (`../logs/lifecycle-log.md`) records **events** and decisions; it does **not** replace contracts or auto-advance phases—[registry-source-of-truth.md](registry-source-of-truth.md).  
- **Workflow docs** under `../workflows/` describe **target** control-plane **flow**; this phase model is **governance vocabulary** for humans and **does not** claim those flows are **running**.  
- **Parallel chat:** one chat should not imply another chat’s phase; continuity is **artifact + REPORT**, not cross-chat sync.

---

## 4. Explicit non-claims

- **No** guarantee that any tool tracks these phases.  
- **No** implied orchestration between phases.  
- **No** requirement to log every phase for every micro-edit.

---

## 5. SAFE UNKNOWN

- Whether a **future** implementation will **persist** phase names per task run.  
- Exact 1:1 mapping from this vocabulary to any **external** ticket workflow columns.
