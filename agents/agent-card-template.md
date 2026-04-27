# MARS — Agent card template (v0, planned)

**Instructions:** Copy this template per agent. Fill all fields; use **SAFE UNKNOWN** where a fact is not yet fixed. **Do not** mark **active** without implementation evidence in-repo and team agreement (see `registry.md`).

---

## `name`
<!-- Unique catalog id, e.g. coding-agent, agent-builder -->


## `type`
<!-- e.g. specialist, builder, guard, support -->


## `status`
<!-- one of: planned | draft | legacy-bridge | active | deprecated -->


## `purpose`

<!-- 1 short paragraph. -->


## `responsibilities`

<!-- Bullet list: what this agent is meant to do. -->


## `non-responsibilities`

<!-- Bullet list: what it must not do. -->


## `inputs`

<!-- Contract-level description: what it accepts. -->


## `outputs`

<!-- Artifacts, messages, handoff payloads. -->


## `tools`

<!-- Tool ids, MCP, connectors — or "none (v0)". -->


## `permissions`

<!-- Model routes, data scopes, approval rules. -->


## `limitations`

<!-- Context, policy caps, known gaps. -->


## `workflow`

<!-- Typical place in a run: Control Plane step, HITL, after planner, etc. -->


## `validation`

<!-- How outputs are checked (Validator Agent, evals, tests). -->


## `changelog`

| Date (optional) | Change |
|----------------|--------|
| | |

---

## `legacy` (optional)

<!-- Map from legacy names (e.g. Factory Engineer → Agent Builder) or "none". -->


## Build Map

Per-agent lifecycle slice (v0). Complements the global Master Build Map (`governance/master-build-map.md`); keep this section on the card — no separate build-map file for v0.

- **stage:** <!-- `draft` | `planned` | `partial` | `ready` | `active` | `deprecated` -->

- **capabilities:** <!-- logical list of what this agent can do -->

- **implemented:** <!-- что реально подтверждено в repo (paths, tests, contracts); SAFE UNKNOWN if not evidenced -->

- **planned:** <!-- what is expected to be added -->

- **blocked:** <!-- blockers if any; else "none" -->

- **dependencies:** <!-- related systems: control-plane, tools, workflows, etc. -->

- **risks:** <!-- refs to `governance/risk-register.md` entries (ids or titles); SAFE UNKNOWN if not mapped -->

### Rule — agent cannot be `active` unless

All of the following must hold before **`status`** = `active` **or** this section’s **`stage`** = `active`:

1. **`build_map.stage`** = `active` (i.e. **stage** in this Build Map = `active`).
2. **Permissions** are defined (the **`permissions`** section above is concrete, not an unfilled placeholder).
3. **Registry entry** exists for this agent (`agents/registry.md`, matching **`name`**).
4. **Validation rules** exist (the **`validation`** section above documents how outputs are checked).
