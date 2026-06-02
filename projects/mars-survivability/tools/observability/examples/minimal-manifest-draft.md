# Snapshot Manifest (DRAFT — for observability testing only)

## Identity

| Field | Value |
|-------|-------|
| **snapshot id** | `snap-20260524-120000-test-workspace-pre-test` |
| **workspace** | `C:\AI MARS\workspaces\_sandbox\test-workspace` |
| **timestamp** | `2026-05-24T12:00:00Z` |
| **operator** | `test-operator` |

## Context

| Field | Value |
|-------|-------|
| **reason** | G4 manifest cross-validator smoke test |
| **risk class** | MEDIUM RISK |

## Pre-operation state

```
Branch: main, working tree: clean (test)
```

## Git state

| Field | Value |
|-------|-------|
| **branch** | `main` |
| **HEAD** | `abc1234` |
| **working tree** | clean |

## Restore instructions

1. Stop AGENT.
2. Copy files from snapshot to target workspace.
3. Verify manually.

## Forbidden operations after snapshot

- git clean
- recursive delete
