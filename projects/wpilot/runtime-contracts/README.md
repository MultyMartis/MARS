# WPilot Runtime Contracts

**Status:** v1 documented (2026-06-19).  
**Purpose:** Bridge layer between Core Model v1 and plugin implementation. Not a Core Layer.

## Start here

- [WPILOT-RUNTIME-CONTRACTS-v1.md](WPILOT-RUNTIME-CONTRACTS-v1.md) — canonical Runtime Contracts pass (boundary, ChangeSet, Snapshot, Diff, operations, backup, DB, REST, proven mapping, recommendation).

## Related

| Layer | Path |
|-------|------|
| Core Model v1 | `../WPILOT-*-v1.md` |
| Core Architecture Review | [../WPILOT-CORE-ARCHITECTURE-REVIEW-v1.md](../WPILOT-CORE-ARCHITECTURE-REVIEW-v1.md) |
| Plugin MVP contracts (implementation detail) | [../plugin-mvp/](../plugin-mvp/) |
| Plugin source | [../plugin/metacode-wpilot/](../plugin/metacode-wpilot/) |

## Next stage

Per Runtime Contracts v1 §10: **Runtime Prototype** — implement plugin backup → scoped-replace → rollback on DEV; do not expand Core Model.
