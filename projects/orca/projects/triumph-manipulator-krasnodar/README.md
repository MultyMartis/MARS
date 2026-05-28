# Triumph Manipulator Krasnodar — ORCA Project Container v0

**project_id:** `triumph-manipulator-krasnodar`  
**Status:** Canonical navigation / identity / approval / registry / bridge layer (v0 initialization)

## What this is

First canonical ORCA **project container** for Triumph Manipulator (Краснодар / Краснодарский край). Operator-facing index: modes, gates, landing routes, and links into validated operational artifacts.

## What this is not

| Not | Detail |
|-----|--------|
| Runtime | No orchestration, no agents, no API |
| Search-pack SoT | Validated pack remains at [`projects/orca/ppc/triumph-manipulator/`](../../ppc/triumph-manipulator/) |
| Exporter home | Do not move or duplicate `exporter-cli`, `validation-cli`, campaign JSON, `runs/`, `handoff/` |
| Landing source | HTML/SCSS live in [`workspaces/triumph-manipulator-landing-v4/`](../../../../workspaces/triumph-manipulator-landing-v4/) |

## Layer role

| Layer | Path |
|-------|------|
| Identity & status | [`PROJECT.md`](PROJECT.md) |
| Landing URLs | [`landing-route-registry.json`](landing-route-registry.json) |
| Approval gates | [`approvals/approval-state-v0.md`](approvals/approval-state-v0.md) |
| Landing QA | [`landing-qa/v5-page01-landing-qa-v0.md`](landing-qa/v5-page01-landing-qa-v0.md) |
| Bridge links | [`bridge-links.md`](bridge-links.md) |

## Operator entry

1. Read [`PROJECT.md`](PROJECT.md) for current state and SAFE UNKNOWN.
2. Use [`bridge-links.md`](bridge-links.md) to reach validated pack, full-cycle, Factory, and tools.
3. Update gates only in [`approvals/`](approvals/) after human sign-off.

## Related contracts

- [`project-md-contract-v0.md`](../project-md-contract-v0.md)
- [`project-structure-contract-v0.md`](../project-structure-contract-v0.md)
