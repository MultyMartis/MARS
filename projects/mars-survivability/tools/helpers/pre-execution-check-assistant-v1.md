# Pre-Execution Check Assistant (v1)

**Status:** **documented** — short operational flow before risky work.  
**Not:** automated gate, hook, or blocking service.

**Lane:** B — use before AGENT tasks with filesystem/git impact.

---

## 1. When to use

| Trigger | Examples |
|---------|----------|
| AGENT task | Any scoped edit, multi-file refactor |
| Risky workspace edit | Triumph v4/v5 `src/`, template workspace |
| Generator run | gulp, npm build, export CLI |
| Rebuild | dist regen, asset pipeline |
| Migration | Handoff, structure move (human-led) |
| Recovery | After incident — **ASK/plan first**, not AGENT destructive |

---

## 2. BEFORE checklist (operator)

Copy and fill; all **YES** or **N/A** required to proceed.

### A — Governance

| # | Check | YES / N/A / STOP |
|---|-------|------------------|
| 1 | Lane correct? (A factory / B survivability / scoped project) | |
| 2 | [safe-agent-task-template](../../templates/safe-agent-task-template-v1.md) pasted and filled? | |
| 3 | Risk class assigned per [agent-operation-risk-classes-v1.md](../../contracts/agent-operation-risk-classes-v1.md)? | |
| 4 | New chat needed? (long session / drift / recovery) → [chat-context-drift-protocol](../../protocols/chat-context-drift-protocol-v1.md) | |

### B — Scope

| # | Check | YES / N/A / STOP |
|---|-------|------------------|
| 5 | **Scope defined** — explicit ALLOWED PATHS list? | |
| 6 | `node scope-analyzer-v1.mjs` run on paths — acceptable labels? | |
| 7 | No **CROSS-WORKSPACE** without split task? | |
| 8 | **PROTECTED-ZONE-HIT** acknowledged or scope narrowed? | |

### C — Snapshot & rollback

| # | Check | YES / N/A / STOP |
|---|-------|------------------|
| 9 | **Snapshot exists** (or N/A for read-only SAFE)? MEDIUM+ → required | |
| 10 | `node snapshot-helper-v1.mjs` — manifest draft reviewed? | |
| 11 | **Rollback known** — snapshot id or git path documented in task? | |
| 12 | [rollback-advisor-v1.md](rollback-advisor-v1.md) read if recovery context? | |

### D — Commands & diff

| # | Check | YES / N/A / STOP |
|---|-------|------------------|
| 13 | Planned shell commands validated (`scoped-operation-validator-v1.mjs`)? | |
| 14 | Pre-change `git diff --stat` baseline recorded? ([diff-advisor-workflow](diff-advisor-workflow-v1.md)) | |
| 15 | Workspace **isolated** — cwd not repo root for destructive tests? | |

### E — Authority

| # | Check | YES / N/A / STOP |
|---|-------|------------------|
| 16 | [human-authority-protocol-v1.md](../../protocols/human-authority-protocol-v1.md) acknowledged? | |
| 17 | Human `APPROVED:` line for MEDIUM+ / destructive-adjacent ops? | |
| 18 | No autonomous cleanup/recovery expected from AGENT? | |

**Any STOP** → halt per [operational-halt-protocol-v1.md](../../protocols/operational-halt-protocol-v1.md).

---

## 3. Tool invocation quick reference

```powershell
Set-Location "C:\AI MARS\projects\mars-survivability\tools\helpers"

# Scope
node scope-analyzer-v1.mjs --paths "workspaces/foo/src/"

# Snapshot suggestion (does not copy files)
node snapshot-helper-v1.mjs -w "workspaces/foo" -o "pre-refactor header" -r MEDIUM

# Commands (from validator dir)
Set-Location "..\validator"
node scoped-operation-validator-v1.mjs -c "git status" -r SAFE
```

---

## 4. AFTER (post-execution reminder)

- Post diff review ([diff-advisor-workflow-v1.md](diff-advisor-workflow-v1.md) Workflow B)  
- REPORT with changed files + snapshot id  
- Rollback log if restore performed  

---

## 5. SAFE UNKNOWN

- Operator may waive snapshot with explicit written waive — document in REPORT.  
- Validator ALLOW does not replace this checklist.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | G3 — pre-execution check assistant v1 |

---

*End of Pre-Execution Check Assistant v1.*
