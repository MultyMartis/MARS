# 05 — Agent system state (migration v0)

---

## Agent cards

- **Location:** `agents/cards/*-v0.md` (16 files at export time: intake, strategy, IA, blueprint, design, wireframe, QA lanes, validator integration, **gulp-frontend**, etc.).  
- **Maturity:** **v0 documentation** — role contracts, boundaries, vocabulary alignment with Website Factory.  
- **Not:** Running agent processes, registered MCP workers, or guaranteed LLM routing.

## Website Factory agents

- Cards correspond to **planned** specialist roles in capability map **C16** / Website Factory workflow stages.  
- **Usage today:** prompt + human session identity (“you are operating as X under contract Y”) — **not** an agent server.

## Validator role

- **Cross-cutting** checks: policy, task fit, structural guardrails (`qa-validation-model.md`, `validator-agent-integration-v0.md`).  
- **Implementation:** **SAFE UNKNOWN** whether one LLM call, checklist tool, or hybrid (`qa-validation-model.md`).

## Frontend Gulp Agent

- **Pack:** `agents/frontend-gulp-agent/` (`README.md`, `workflow.md`).  
- **Card:** `agents/cards/gulp-frontend-agent-v0.md`.  
- **Purpose:** **Lane A** Gulp/static site execution: partials, SCSS, build verification, REPORT discipline.  
- **Not:** Autonomous continuous build/deploy.

## Operational packs

- Frontend Gulp workflow references parallel chat mode.  
- Website Factory runbooks / templates define **human** operational packs.

## Reference vs runtime distinction

| Kind | Meaning |
|------|---------|
| **Reference** | Web-GPT markdown pack, architecture maps, imported legacy ideas |
| **Runtime** | Would be evidenced by long-running services, job queues, production orchestrator code **actually executing** MARS — **not** assumed from docs |

## Planned vs implemented distinction

- **Planned:** Control plane scheduling, tool enforcement, automated validation engines, full MetaBOT bridge.  
- **Implemented (partial evidence):** `mars-runtime/` contains **some** JS (adapters, tests) — treat as **experimental/partial**, not “MARS is live.”

## SAFE UNKNOWN boundaries

- Which agent roles are **instantiated** in a given user session (user choice).  
- Whether **Validator** automation lands before or after other QA.  
- Parity of **mars-runtime** adapters with external n8n/MetaBOT payloads.
