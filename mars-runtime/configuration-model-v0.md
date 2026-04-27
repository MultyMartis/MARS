# Configuration Model v0

**Status:** documented — conceptual configuration model for MARS runtime planning. Documentation-only, with no executable config artifacts.

## 1. Purpose

- Define the major configuration domains required by planned MARS runtime behavior.
- Establish separation of configuration from source logic and runtime code paths.
- Provide consistent linkage between configuration domains and authoritative registries.

## 2. Configuration types (v0)

| Config type | Scope | Examples of governed concerns (conceptual) |
|-------------|-------|--------------------------------------------|
| `system_config` | Global runtime/system behavior | environment intent, execution posture, global safety defaults |
| `agent_config` | Agent-specific runtime behavior | role-level constraints, capability toggles, allowed operational modes |
| `tool_config` | Tool invocation behavior | policy flags, risk posture defaults, integration call behavior |
| `model_config` | Model invocation behavior | routing preferences, policy overlays, budget guardrails |

## 3. Core principles

1. **No hardcoding** — mutable operational parameters should not be embedded directly into business/runtime code paths.
2. **Separation from code** — configuration is a distinct concern, versioned and governed independently of implementation logic.
3. **Traceable ownership** — each config domain should map to a clear source-of-truth contract.
4. **Environment-aware posture** — config interpretation should remain compatible with environment separation rules.

## 4. Registry relations

- `agent_config` aligns with [../agents/registry.md](../agents/registry.md) as the agent identity and capability SoT.
- `tool_config` aligns with [../tools/registry.md](../tools/registry.md) and tool contracts.
- `model_config` aligns with [../models/model-registry-v0.md](../models/model-registry-v0.md) and model policy/routing contracts.
- `system_config` should remain consistent with governance-level SoT and runtime architecture contracts.

## 5. Normative rules (v0)

1. Configuration meaning must be documented before any implementation claims are made.
2. Configuration domains must not bypass security, approval, or risk controls.
3. Undefined config behavior is **SAFE UNKNOWN** until documented in an authoritative contract.
4. This file defines model-level categories only; no executable format is prescribed in v0.

## 6. Explicit non-goals

- No `.env`, YAML, JSON, TOML, or other real config files are introduced here.
- No runtime config loaders or parser logic are introduced.
- No binding to a specific config platform or deployment stack.

**Explicit statement:** **NO real config files in repo** are defined by this model.
