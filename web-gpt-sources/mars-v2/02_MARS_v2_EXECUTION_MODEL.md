# MARS v2 — Execution model

**Status:** **OPERATIONAL** (human + IDE today) · **PLANNED** (future MARS runtime surfaces)

---

## Primary loop

```
Task / envelope (intent, scope, lane, constraints)
    → Prompt (Web-GPT packages; human approves)
    → Execute (Cursor / Codex on C:\AI MARS)
    → REPORT (closure: files, summary, git, UNKNOWN)
    → Validation (human meaning — who, what scope; not auto-orchestrator)
```

**Web-GPT** prepares instructions and context; **does not** replace editor execution or git.

---

## Human authority layer

| Owner | Responsibility |
|-------|----------------|
| **Operator / user** | Approvals, secrets, lane choice, final correctness, explicit commits |
| **Cursor/Codex** | Filesystem edits and commands in user-controlled environment |
| **Governance docs** | Shared vocabulary and boundaries — **not** auto-enforcement |
| **External systems** | n8n, providers, deploy pipelines — **outside** MARS core claims |

**HITL** remains primary for ambiguity, security stops, delivery acceptance, and scope expansion.

---

## Today vs planned

| Surface | Today | Planned |
|---------|-------|---------|
| Repo file changes | **Cursor/Codex** + human | Same until runtime evidenced |
| Task/workflow state store | Editor + git + chat | Control Plane / durable state (**planned**) |
| Multi-agent dispatch | Human reads agent cards | Runtime dispatcher (**planned**) |
| Integration orchestration | Optional external (n8n, etc.) | Execution Bridge instances (**concept**) |

**No** in-repo MARS **daemon** enforcing full `prompt → … → log` chain.

---

## Execution Bridge

**Status:** **BOUNDARY ONLY** (concept + contract markdown)

Translation/handoff between MARS task semantics and concrete runners (Cursor session, n8n webhook, future API). **Canonical contract SoT:** `mars-runtime/execution-bridge-v0.md`. Governance `execution-model.md` describes **intent**, not a shipped bridge product.

---

## Lane separation

See `00` and `governance/parallel-cursor-chat-work-mode-v0.md`:

- **Lane A** — production delivery (workspaces, client landings).
- **Lane B** — MARS core (governance, Factory, registries).
- Mixing lanes in one commit batch without explicit charter = operational risk.

---

## Task envelope (summary)

Bounded unit of intent (from S4 `task-envelope-standard.md`):

- Identity / correlation (as assigned by human)
- **Scope** and **forbidden paths**
- **Lane** (A / B / runtime task)
- Expected outputs and REPORT requirement
- **SAFE UNKNOWN** fields explicit, not defaulted

Prompt text ≠ automatic governance envelope ≠ future runtime payload.

---

## Git checkpoint discipline

| Rule | Status |
|------|--------|
| No commit/push/stage unless user orders | **OPERATIONAL** |
| Lane-separated commits when committing | **OPERATIONAL** |
| GIT CHECKPOINT NEEDED | Rare milestone only |
| Never assume clean tree in new chat | **OPERATIONAL** |

---

## Prompt → execute → report (Website Factory aligned)

Factory runbooks describe **human-driven** stage progression. Operational pattern:

1. Artifact-first prompts (no fabrication of approvals).
2. Cursor executes scoped filesystem work.
3. REPORT per `AGENTS.md` and Factory reporting standards (in-repo).

**Not:** autonomous stage scheduler or artifact bus transport.

---

## Validation chain (meaning, not automation)

| Layer | “Validated” may mean |
|-------|---------------------|
| Human review | Operator sign-off, checklist |
| Editor | Build/lint run locally (evidence in REPORT) |
| Optional helper | Hint script under `tools/` — **hints only** |
| Future runtime | **SAFE UNKNOWN** until proven in-tree |

Mention of “validation runtime” in Factory docs = **vocabulary**, not background service.

---

## SAFE UNKNOWN

- Wire format for future MARS runtime API.
- Whether n8n is in scope for a given program (optional by design).
- Exact mapping external workflow payload ↔ MARS task ID.
