# 01 — MARS system overview (migration v0)

## What MARS is

**MARS** (**Multi-Agent Runtime System**, рус. «Марс») is a **documentation-first** program to define a **controlled** multi-agent system: clear **control plane** vocabulary, **workflows**, **registries**, **governance**, **HITL** (human-in-the-loop), and **quality** posture — grounded in the Web-GPT source pack and in-repo governance.

The repository’s **declared role** (see `AGENTS.md`): **main documentation / design source for Phase 1**; **not** by default proof of a **running** multi-agent platform unless **source files** demonstrate it.

## What MARS is not

- **Not** a claim of shipped **production orchestration** in-repo without evidence.  
- **Not** a substitute for **human** approval on structural, security, or delivery-critical actions.  
- **Not** “agents” as **autonomous daemons** — agent **cards** and packs are **operational documentation** unless separately implemented.

## Current phase (evidence-based)

- **Phase 1 / governance-heavy documentation stage** with **Stage 16 pilot** documentation (Website Factory, MetaBOT pack, legacy SEO folder) described in `governance/master-build-map.md`.  
- **Runtime implementation:** governance text repeatedly states **absence** of full runtime; partial **experimental** code may exist under `mars-runtime/` — **SAFE UNKNOWN** per file until inspected.

## Architecture philosophy

- **Standard MAS terminology** mapped from legacy names (`web-gpt-sources/01_system.md`, terminology maps).  
- **Three-way split** (non-negotiable in `AGENTS.md`): **documented architecture** vs **planned implementation** vs **legacy imported** material.  
- **Control plane** concepts (orchestrator, tasks, validation) are **targets** for future systems; narrative alignment ≠ running code.

## Documentation-first

Contracts, registries, capability maps, and Website Factory layers are **Markdown semantics** — **not** executable workflow engines unless a separate codebase proves otherwise.

## Governance-first

**Master Build Map**, **dependency map**, **capability map**, **risk register**, **project registry**, and **parallel chat lane** rules define **what may change together** and **how to escalate**.

## Execution model (actual)

Today’s default execution path is:

**Human intent → Cursor (or similar) → file edits / commands → explicit REPORT → optional git (user-controlled).**

There is **no** in-repo obligation of an **always-on MARS process** supervising chats.

## HITL philosophy

Humans approve **plans**, **risky tool use**, **structural repo changes**, and **delivery** when runbooks require it. Automation **extends** the human; it does **not** silently own accountability.

## Artifact philosophy

Artifacts (strategies, blueprints, handoffs, QA payloads) are **traceable deliverables** with **state**, **approval**, and **revision** semantics in documentation — preparing for future persistence, **not** claiming a live artifact bus service.

## Website Factory purpose

**MARS Website Factory** (`projects/mars-website-factory/`) is the **strategic planned**, **documentation-first** static-site production methodology: stages, contracts, registries, runbooks, reference cases — **C16** in `governance/capability-map.md`. It **aligns** with future Control Plane; it is **not** claimed as a studio runtime.

## Frontend Gulp Agent purpose

**Operational pack** under `agents/frontend-gulp-agent/` plus card `agents/cards/gulp-frontend-agent-v0.md` — **Lane A** execution discipline for **Gulp/HTML/SCSS** workspaces (e.g. Triumph). **Not** an autonomous build bot.

## Validation philosophy

**Validator** role is **cross-cutting** in docs (`projects/mars-website-factory/qa-validation-model.md`, validation runtime **model** v0). **No** claim that an automated validator **engine** runs inside MARS by default.

## Operational methodology

**Prompt → plan → execute → validate → report** appears as **workflow narrative** (`workflows/execution-flow.md`, Website Factory workflow map). **Human** runs runbooks (e.g. R01–R15); sequences are **not** a scheduler.

## No-runtime honesty (explicit)

The following are **not** asserted as in-repo production facts unless proven per file:

| Not claimed | Meaning |
|-------------|---------|
| **No daemon** | No MARS supervisor process requirement. |
| **No scheduler** | No automated stage cron / queue worker for Website Factory. |
| **No autonomous orchestration** | No agent swarm routing jobs without human session scope. |
| **No hidden runtime** | Execution visibility = git + logs + REPORT; no shadow control plane. |
| **No fake agent autonomy** | “Agent” = role + prompts + cards unless code demonstrates otherwise. |

**Source of truth for agent honesty:** `AGENTS.md`, `.cursorrules`, Website Factory headers (“documentation only”).
