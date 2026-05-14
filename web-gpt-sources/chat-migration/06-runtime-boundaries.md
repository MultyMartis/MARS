# 06 — Runtime boundaries (migration v0)

---

## What **is** in scope today (no fantasy)

| Category | Description |
|----------|-------------|
| **Documentation** | `web-gpt-sources/`, `governance/`, `projects/mars-website-factory/`, `mars-runtime/*.md` contracts, etc. |
| **Methodology** | Runbooks, templates, lane discipline, REPORT format, HITL labels |
| **Governance** | Master build map, dependency map, capability map, registries, risk register |
| **Operational semantics** | Stage/artifact/approval/revision vocabulary — **human-executed** |

## What is **NOT** (unless proven file-by-file)

| Not this | Clarification |
|----------|----------------|
| **Runtime** | Not an always-on MARS kernel supervising work |
| **Orchestration engine** | No mandatory in-repo process routing tasks between agents |
| **Queue** | No claimed job queue executing Website Factory stages |
| **Scheduler** | No cron/worker driving stage transitions |
| **Autonomous validator** | No default background validation service |
| **Autonomous deployment system** | Deploy is human/external pipeline unless documented otherwise |

## Contracts vs code

- `mars-runtime/` may contain **design-time or experimental** **code** (e.g. adapters, tests). That is **JavaScript on disk**, not proof of **production orchestration**. Distinguish:
  - **“File exists”** ✅  
  - **“Fleet-wide runtime operational”** ❌ without evidence

## Current execution equation

```
Current execution = Human operator
                  + Cursor (or IDE) assistant
                  + Prompts / runbooks / contracts
                  + Explicit REPORT
                  + Git (explicit, lane-separated, user-approved commits)
```

**No daemon** is required for this equation. **No hidden runtime** replaces git history or REPORT.

## Website Factory alignment (honesty line)

Workflow docs **map** stages to future **Task** / Control Plane concepts **as narrative**. Reading the map **does not** spin up a workflow engine.

## Chat migration implication

A **new** ChatGPT chat has **zero** attachment to Cursor’s shell, git, or filesystem unless the user pastes status/output. The assistant must **not** assume repo state or running jobs.
