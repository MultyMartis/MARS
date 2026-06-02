# MARS — Chat migration pack (v0)

**Purpose:** A **human-operated** continuity bundle for pasting into a **new** ChatGPT (or other) chat so the assistant inherits MARS discipline without inventing a runtime.

**Philosophy:** **Evidence-first**, **documentation-first**, **operational-first** (post–Cycle 8). **Historical note:** older paste bundles used “governance-first” — superseded by [mars-operational-evolution-state-after-cycles-1-8-v0.md](../../governance/mars-operational-evolution-state-after-cycles-1-8-v0.md). This folder **summarizes** canonical sources; prefer [mars-v2/](../mars-v2/) for new Web-GPT chats.

---

## What each file is

| File | Role |
|------|------|
| [01-mars-system-overview.md](01-mars-system-overview.md) | Identity, phase, principles, explicit “not a daemon” boundary. |
| [02-current-operational-state.md](02-current-operational-state.md) | Lanes (A / B / Runtime), priorities, dirty-tree snapshot philosophy. |
| [03-website-factory-state.md](03-website-factory-state.md) | Website Factory v0: exists vs planned vs SAFE UNKNOWN. |
| [04-governance-and-rules.md](04-governance-and-rules.md) | Registries, Stage 16 / C16, anti-patterns, lane commits. |
| [05-agent-system-state.md](05-agent-system-state.md) | Agent cards, Validator, Frontend Gulp Agent — doc vs runtime. |
| [06-runtime-boundaries.md](06-runtime-boundaries.md) | What execution **is** today (human + Cursor + REPORT). |
| [07-safe-unknown-boundaries.md](07-safe-unknown-boundaries.md) | SAFE UNKNOWN rules and examples. |
| [08-active-projects-and-lanes.md](08-active-projects-and-lanes.md) | Project/lane classification table. |
| [09-git-and-report-discipline.md](09-git-and-report-discipline.md) | Git safety, REPORT skeleton, staging rules. |
| [10-new-chat-bootstrap-sequence.md](10-new-chat-bootstrap-sequence.md) | Exact order to onboard a new chat safely. |

---

## Loading order (recommended)

1. **01** — System overview (truth baseline).  
2. **02** — What is “now” operationally.  
3. **06** + **07** — Hard boundaries (no fantasy runtime + unknowns).  
4. **03** + **05** — Website Factory + agents (how work is *supposed* to flow).  
5. **04** + **09** — Governance + git/report discipline.  
6. **08** — Project map.  
7. **10** — Bootstrap sequence for the new session.

**Minimum viable paste:** **01**, **06**, **07**, **09**, **10** — then pull **03–05** when doing Factory work.

**Stabilization bridge:** After pasting, open **`AGENTS.md`** and use its **Phase S2–S7** pointer block as the canonical entry into **`governance/*`** for the newer stack (e.g. **survivability**, **execution-contract**, **tooling-boundary**, operational-experiment, and **reality-audit** layers). That material is **additional** context for operators and new chats; this pack stays a **shortcut summary**, not a substitute for those docs.

---

## Migration philosophy

- **Continuity-safe** means the new chat **re-reads** `git status`, **re-classifies** lanes, and **does not assume** another chat’s unstaged state.  
- **Operational** means prompts, REPORTs, explicit paths, and HITL — not background jobs.  
- **No staging** of this pack is implied; treat as documentation until the user asks otherwise.

**Canonical repo root:** `C:\AI MARS` (Windows path as used in project rules).
