# `tools` — Tool Layer v0 (documentation)

## Purpose

**Tool Layer** contracts: function-calling surfaces, registry semantics, execution alignment with the **Execution Bridge**, and safety / approval alignment with **Security** and **governance** signals. Cross-ref [../web-gpt-sources/02_architecture.md](../web-gpt-sources/02_architecture.md) and [../web-gpt-sources/07_tools_models.md](../web-gpt-sources/07_tools_models.md) for broader architecture context.

## Documents (v0)

| File | Role |
|------|------|
| [registry.md](registry.md) | **Tool Registry** — row schema (`tool_id`, permissions, risk, side effects, approval), lifecycle, **planned** examples. |
| [tool-contract-v0.md](tool-contract-v0.md) | **Invocation envelope** — inputs/outputs, **signals**, failure-model and gate obligations. |
| [tool-execution-model-v0.md](tool-execution-model-v0.md) | **Execution** — bridge mapping, sync/async, runtime state / checkpoint / resume / logging split. |
| [tool-safety-model-v0.md](tool-safety-model-v0.md) | **Safety** — risk levels, **NEED HUMAN APPROVAL** / **SECURITY RISK** mapping, side-effect classes. |

## Relation to MARS architecture

Tools are invoked from **agents** and **orchestration** under **permissions** and **approval gates**; they may touch **Runtime State Store** execution facets or **memory** only as described in the linked contracts — **not** implemented in this Phase 1 documentation repository.

## Status

**planned** — **documentation only** ([../AGENTS.md](../AGENTS.md): no in-repo tool runtime, MCP host, or enforcement engine unless separate evidence exists). **Stage 9** progress is reflected in [../governance/master-build-map.md](../governance/master-build-map.md).
