# Integration Surfaces v0

**Status:** documented — conceptual integration surfaces for runtime planning. Documentation-only, no configured live integrations.

## 1. Purpose

- Define the primary integration surface categories for MARS Stage 14 planning.
- Enforce a single execution boundary for integrations to avoid bypass paths.
- Align integration narrative with runtime bridge and tool-layer contracts.

## 2. Integration types (v0)

| Type | Typical role in planned architecture |
|------|--------------------------------------|
| `API` | Service-to-service invocation and external system interfaces. |
| `n8n` | Workflow automation and connector orchestration surface. |
| `scripts` | Controlled procedural adapters for bounded operational tasks. |
| `MCP-like tools (future)` | Structured tool protocol surfaces for managed invocation contexts. |

## 3. Normative rules (v0)

1. All integration invocations must pass through the Execution Bridge contract boundary.
2. Direct calls from orchestration or agents to external surfaces are disallowed in the conceptual model.
3. Integration paths must inherit tool-layer safety, permission, and approval expectations.
4. Undocumented integration behavior is **SAFE UNKNOWN** until specified in contract form.

## 4. Relation to other artefacts

- [execution-bridge-v0.md](execution-bridge-v0.md) — normative boundary for execution dispatch and outcomes.
- [../tools/README.md](../tools/README.md) and tool contracts — invocation semantics, safety model, validation and permissions.

## 5. Explicit non-goals

- No endpoint URLs, credentials, webhooks, or workflow IDs.
- No enabled MCP server bindings or runtime connectors.
- No executable script catalogs or deployment hooks.

**Explicit statement:** **NO real integrations configured** in this file.
