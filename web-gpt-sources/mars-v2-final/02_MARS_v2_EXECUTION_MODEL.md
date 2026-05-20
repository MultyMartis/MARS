# MARS v2 — Execution model

**Status:** **OPERATIONAL** (human + IDE today)

---

## Primary loop

```
Task / envelope (intent, scope, lane, constraints)
  → Prompt (Web-GPT packages; human approves)
  → Execute (Cursor / Codex on D:\AI MARS)
  → REPORT (# REPORT — <name>)
  → Validation (human meaning — who, what scope)
```

Web-GPT prepares; **does not** replace editor execution or git.

---

## Authority

| Owner | Role |
|-------|------|
| **Operator** | Approvals, secrets, lane, commits, HITL |
| **Cursor/Codex** | Filesystem edits in user environment |
| **Governance docs** | Vocabulary — not auto-enforcement |
| **External systems** | n8n, deploy, providers — outside MARS core claims |

---

## Today vs planned

| Surface | Today | Planned |
|---------|-------|---------|
| Repo edits | Cursor/Codex + human | Same until runtime evidenced |
| Task state | Editor + git + chat | Control plane (**planned**) |
| Multi-agent dispatch | Human reads agent cards | Runtime dispatcher (**planned**) |
| Bridge to runners | Concept + narrow R1 demos | Execution Bridge product (**planned**) |

**No** in-repo MARS daemon enforcing full prompt→validate→log chain.

---

## Task envelope (summary)

- Scope + **forbidden paths**
- **Lane** (A / B / Runtime)
- Expected outputs + REPORT requirement
- **SAFE UNKNOWN** fields explicit

Prompt text ≠ governance envelope ≠ future runtime payload.

---

## Validation (meaning, not automation)

| Layer | “Validated” may mean |
|-------|----------------------|
| Human | Checklist, sign-off |
| Editor | Local build/lint (evidence in REPORT) |
| Helper script | Hint under `tools/` — not enforcer |
| Future runtime | **SAFE UNKNOWN** until in-tree proof |

Factory “validation runtime” = **vocabulary**, not background service.

---

## Git discipline

- No commit/push/stage unless user orders.
- Never assume clean tree in new chat — require pasted `git status`.
- **GIT CHECKPOINT NEEDED** — rare major milestones only.

---

## SAFE UNKNOWN (execution)

- Future MARS runtime API wire format
- n8n in scope for a given program
- External payload ↔ MARS task ID mapping
