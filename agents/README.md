# `agents`

**Routing:** Tier 0 = [AGENTS.md](../AGENTS.md); frontend lane = foundation map below + Factory [OPERATIONAL-INDEX](../projects/mars-website-factory/OPERATIONAL-INDEX.md) **Core Run** — not full registry scan.

## Purpose

MARS **Agent layer**: specialized agents, the **Agent Registry (catalog)**, and the **Agent Factory** (governed path to create or update **agent cards** via **Agent Builder**) — as in `web-gpt-sources/02_architecture.md` and `04_agents.md`.

## Agent Registry v0 (contract)

| File | Content |
|------|--------|
| `registry.md` | v0 **planned** contract: purpose of registry/catalog, **status** values, **required** card fields, **initial** agent list, **Control Plane** and **legacy** relations. |
| `agent-card-template.md` | **Template** for per-agent **cards** (all required v0 fields). |
| `../templates/agent-input-contract-template.md` | **Template** for **agent input contracts** (required / optional / forbidden inputs, outputs, validation, **SAFE UNKNOWN**, quarantine) — governance; see [../governance/agent-input-contracts.md](../governance/agent-input-contracts.md). |

## Agent Factory v0 (contract)

| File | Content |
|------|--------|
| `agent-factory-v0.md` | **Agent Factory** v0: **purpose**, **when** triggered, **can/cannot** create, **HITL** **gates**, relations to **Control Plane**, **Workflow**, **Registry**; **FlyCheck** / **Validator** for risky definitions; **allowed** outcomes. |
| `agent-builder-contract.md` | **Agent Builder** **inputs/outputs**, **checks** before create/update, **card** **fields**, **permissions** and **tool** **reviews**, **validation** and **changelog**; **SAFE UNKNOWN** and **NEED HUMAN APPROVAL**. |

**Status:** **Planned** — documentation only. No code, no registry service, no Factory build pipeline in this repository in this phase.

## Relation to MARS architecture

Implements the **Agent layer** *as specified in documentation*: the **Control Plane** **reads** the **registry** to route; **workflows** may **branch** to the **Factory** when **required_agents** are **missing**; **Security** and **Validator Agent** (legacy **FlyCheck** **successor**) constrain adoption — **when implemented**, not as a claim of current code.

## Canonical frontend foundation

**Single map (Gulp foundation + Forge overlay + Factory contracts):** [../governance/frontend-legacy-and-foundation-map-v0.md](../governance/frontend-legacy-and-foundation-map-v0.md) — do not re-derive from scattered READMEs.

| Layer | Entry |
|-------|--------|
| **Gulp foundation** | [`frontend-gulp-agent/`](frontend-gulp-agent/) (`gulp_frontend_agent`) |
| **Forge overlay** | [`mars-forge/`](mars-forge/) (`mars_forge_frontend_agent`) — defers to foundation when silent |
| **Factory session nav** | [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) **Core Run** |

## See also

- `../control-plane/contract.md` — orchestration, routing, and registry read relationship.  
- `../workflows/workflow-v0.md` — workflow and **Factory** handoff.  
- `../mars-runtime/architecture-map.md` — layer map.
