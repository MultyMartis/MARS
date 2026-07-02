# FP-0002 V9-04 Forge Capability Audit v1

**Date:** 2026-07-02

## Subsystem location

Canonical path: `projects/mars-website-factory/subsystems/forge-wordpress/`  
(Not `projects/forge-wordpress` — path alias absent.)

## AG-WP-001 status

| Layer | Status |
|-------|--------|
| Agent card / operation contracts | **DOCUMENTED** — 42 `wp.*` operations |
| Contract validator | **EXISTS** — `tools/validate-ag-wp-001-operation-contracts.mjs` |
| Tool bindings | **BOUND_NOT_IMPLEMENTED** |
| FW-07C-1 harness | **VALIDATED_LOCAL** — synthetic read-only only |
| FP-0002 runtime under harness | **NOT ADMITTED** |
| Theme integration (FW-06B) | **LOCKED** until intake + operator charter |
| Production mutations | **PROHIBITED** (`production_allowed: false`) |

## What Forge can consume now

- Approved frontend commit/tag (`fp-0002-v9-operator-approved-static-frontend-stable-01`)
- This intake pack (routes, templates, fields, acceptance)
- V9 `src/` + `dist/` as parity references
- AG-WP-001 operation contract validation (documentation layer)
- Generic handoff contract checklists

## What is documentation-only

- Most `wp.*` operation implementations
- WPilot binding for FP-0002
- Staging/production deploy operations
- Automated content migration runtime

## Required input artifacts (from handoff contract)

`project_id`, approved commit/tag, page inventory, component inventory, navigation map, forms/modal map, assets manifest, JS behavior map, legal pages, content ownership, plugin constraints.

## Risk boundaries

- `WP_INPUT_HANDOFF_INCOMPLETE` if intake pack missing
- `WP_CONTENT_MODEL_NOT_APPROVED` until operator accepts field architecture
- `WP_RUNTIME_PRODUCTION_DETECTED` blocks production targets
- Mutations require approval + rollback envelope per AG-WP-001 schema

**Do not claim Forge WordPress implementation runtime is production-ready.**
