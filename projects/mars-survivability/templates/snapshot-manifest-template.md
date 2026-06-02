# Snapshot Manifest

**Copy this file to:** `workspaces/_snapshots/<snapshot-id>/SNAPSHOT-MANIFEST.md`  
**Standard:** [../protocols/snapshot-manifest-standard-v1.md](../protocols/snapshot-manifest-standard-v1.md)

---

## Identity

| Field | Value |
|-------|-------|
| **snapshot id** | `snap-YYYYMMDD-HHMMSS-<workspace-slug>-<short-reason>` |
| **workspace** | `C:\AI MARS\workspaces\<name>` |
| **timestamp** | `YYYY-MM-DDTHH:MM:SSZ` |
| **operator** | `<name or handle>` |

---

## Context

| Field | Value |
|-------|-------|
| **reason** | `<why this snapshot exists>` |
| **risk class** | `SAFE` \| `LOW RISK` \| `MEDIUM RISK` \| `HIGH RISK` \| `CRITICAL` |
| **task / chat reference** | `<optional: lane, chat name, task id>` |
| **linked incident** | `<none \| path to logs/incidents/ or report>` |

---

## Pre-operation state

```
<paste or summarize factual state before planned operation>

Examples:
- Branch: main, HEAD: abc1234, working tree: clean
- Branch: feature/x, 12 modified files under src/, 3 untracked assets
- Known issue: header partial drift after_factory handoff
```

---

## Git state

| Field | Value |
|-------|-------|
| **branch** | `<branch name>` |
| **HEAD** | `<short hash>` |
| **working tree** | `clean` \| `dirty` — `<summary if dirty>` |
| **untracked included in snapshot** | `yes` \| `no` \| `partial — list paths` |

```
<paste git status excerpt if helpful>
```

---

## Restore instructions

1. Stop AGENT session on target workspace.  
2. Verify this manifest — snapshot id and workspace paths.  
3. `<step: selective copy paths from snapshot to workspace>`  
4. `<step: run build / smoke check>`  
5. `<step: diff verification>`  
6. Log restore in `logs/rollback-history/`.  

**Primary restore source paths:**

- `<path in snapshot tree>` → `<path in workspace>`

---

## Forbidden operations after snapshot

Until restore is verified **or** operation is confirmed successful and snapshot retired:

- [ ] `<e.g. no recursive delete on workspace>`  
- [ ] `<e.g. no git reset --hard>`  
- [ ] `<e.g. no workspace delete-and-recreate>`  
- [ ] `<e.g. no mass search-replace without new snapshot>`  

---

## Retention

| Tier | Value |
|------|-------|
| **retention tier** | `Active` \| `Reference` \| `Incident-linked` \| `Drill` |
| **review date** | `YYYY-MM-DD` |

---

## SAFE UNKNOWN

List anything that could **not** be verified at snapshot time. Do not fill with assumptions.

| Item | Status |
|------|--------|
| `<e.g. node_modules completeness>` | SAFE UNKNOWN \| verified |
| `<e.g. binary asset hash>` | SAFE UNKNOWN \| verified |
| `<e.g. deploy parity>` | SAFE UNKNOWN \| verified |

**If all fields verified:** write `None — all required fields verified at snapshot time.`

---

## Sign-off

| Field | Value |
|-------|-------|
| **manifest completed** | `YYYY-MM-DD` |
| **operator sign-off** | `<initials or name>` |

---

*End of template — delete instructional lines above Identity section when filing.*
