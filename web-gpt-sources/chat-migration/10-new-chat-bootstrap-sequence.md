# 10 — New chat bootstrap sequence (migration v0)

Use this **exact order** when starting a **new** ChatGPT (or external) chat that must operate on MARS without losing discipline.

---

## 1. Initialization prompt

Send a short **charter** message, for example:

- Repo: **MARS** at `D:\AI MARS`.  
- Mode: **AGENT** or **advisory** per user.  
- Rules: **AGENTS.md** honesty — no runtime claims without file evidence; **SAFE UNKNOWN** for gaps; prefer **Russian** for user-facing text if user wants.  
- Git: **no commit/push/stage** unless user explicitly orders; never `git add .`.

---

## 2. Self-describe import

Paste **01-mars-system-overview.md** then **06-runtime-boundaries.md** then **07-safe-unknown-boundaries.md** (minimum truth bundle).

Optionally paste **02-current-operational-state.md** — or replace §2 with a **fresh** `git status` paste from the user.

---

## 3. Operational rules import

Paste **09-git-and-report-discipline.md** and the relevant slice of **04-governance-and-rules.md** (lane separation + anti-patterns).

If work is Website Factory–heavy, add **03** and **05**.

---

## 4. Continuity verification

The new chat must:

1. Ask for (or assume absence of) **current** `git status --short -uall`.  
2. Refuse to claim cleanliness or lane purity without that output.  
3. List **conflicts** if user pastes status showing mixed lanes.

---

## 5. Active lane verification

Explicitly record:

- **Active lane:** A / B / Runtime (only one primary per batch).  
- **Forbidden paths** for that lane (from `parallel-cursor-chat-work-mode-v0.md`).  
- **Next commit lane** (if any) — else “no commit planned.”

---

## 6. Begin work

Only after steps 1–5:

- Scope a **small** change set matching the lane.  
- Produce **REPORT** on exit if the user required a task deliverable.

---

## What the new chat **must** acknowledge

- MARS is **documentation-first**; runtime/orchestration are **not** assumed.  
- **HITL** applies to risky moves.  
- **Triumph + Website Factory + MetaBOT** are real **project threads** with different canonical folders.

## What the new chat **must NOT** assume

- No assumption of **scheduler**, **validator service**, or **auto-deploy**.  
- No assumption that **another chat** already committed or cleaned the tree.  
- No assumption that **`seo-content-agent/`** is canonical (use **metabot** pack).

## How it must behave

- **Evidence-first** answers; cite paths.  
- **Concise** operational steps; **structured** REPORT when closing tasks.  
- **Escalate** on wrong-lane detection instead of “fixing forward” silently.
