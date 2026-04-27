# `workflows`

## Purpose

MARS **Workflow layer**: how **tasks** move through the system — pipelines, graphs, runbooks, and **human-in-the-loop** (HITL), as in `web-gpt-sources/02_architecture.md` and `05_workflows.md`.

## Workflow v0 (contract)

| File | Content |
|------|--------|
| `workflow-v0.md` | **Workflow Layer v0**: purpose; relations to **Control Plane** (Control Core), **Agent Registry**, **Agent Factory (Agent Builder)**; **signals** summary. |
| `task-contract-v0.md` | **Task Contract v0**: **id**, **title**, **goal**, **scope_in** / **scope_out**, I/O, **acceptance_criteria**, **constraints**, **risk_level**, **required_agents**, **hitl_gates**, **signals**. |
| `execution-flow.md` | **prompt → task → plan → route → execute → validate → report → log**; where **Control Plane**, **agents**, **validation**, and **signals** act. |
| `failure-model-v0.md` | **Failure** **Handling** **Model** v0: failure classes, **signals**, persistence expectations, and links to state / checkpoint / recovery (documentation only). |

**Status:** **Planned** — documentation only. No workflow engine, no state machine implementation in this directory.

## Relations

- **Control Plane** — orchestrates the flow; see `../control-plane/contract.md`.
- **Agent Registry** — `required_agents` resolve against `../agents/registry.md`.
- **Agent Builder** — out-of-run / gated path to add or update **agent** definitions when the run **STRUCTURE** or registry **gaps** require it (see `workflow-v0.md`).

## See also

- `../mars-runtime/architecture-map.md` — repository vs layers.
