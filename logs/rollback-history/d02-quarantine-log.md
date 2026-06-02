# Quarantine Log — D-02 Manual Restore Drill

**Log id:** `rollback-20260524-d02-quarantine`  
**Timestamp:** `2026-05-24T19:12:00Z`  
**Severity:** INFO  
**Operator:** cursor-agent-d02-drill  
**Lane:** B  
**Related task / chat:** D-02 Real Manual Restore Drill

---

## Summary

Drifted D-01 sandbox workspace moved to quarantine per quarantine-first discipline. Original snapshot untouched. No delete operations — move-only preservation.

---

## Evidence

| Field | Value |
|-------|-------|
| **Source path** | `C:\AI MARS\workspaces\_sandbox\d01-survivability-drill\` |
| **Quarantine path** | `C:\AI MARS\workspaces\_quarantine\d01-survivability-drill-drifted\` |
| **Linked snapshot** | `workspaces/_snapshots/snap-20260524-012224-d01-drill/` |
| **Trigger** | Drifted — intentional D-01 simulation retained as evidence |
| **Operation** | `Move-Item` (human-operated, PowerShell) |

---

## Actions taken

1. Created `workspaces/_quarantine/` directory (first quarantine use in repo)
2. Moved entire drifted sandbox tree to quarantine target
3. Created `QUARANTINE-MANIFEST.md` inside quarantine folder
4. Did **not** modify snapshot
5. Did **not** delete any files

---

## Quarantined contents

```
workspaces/_quarantine/d01-survivability-drill-drifted/
├── README.md
├── QUARANTINE-MANIFEST.md          (created at quarantine time)
└── sample-project/
    ├── config/settings.json        (drifted)
    ├── docs/overview.md            (unchanged)
    ├── docs/suspicious-spread.md   (drift artifact)
    └── src/app.js, styles.css, index.html
```

---

## Post-quarantine state

| Location | Status |
|----------|--------|
| `workspaces/_sandbox/d01-survivability-drill/` | **Removed** (moved to quarantine — not deleted) |
| `workspaces/_snapshots/snap-20260524-012224-d01-drill/` | **Untouched** |
| Next step | Manual restore to `workspaces/_sandbox/d01-survivability-drill-restored/` |

---

## Follow-up

- Execute manual selective restore from snapshot
- Diff validation: restored vs snapshot vs quarantine
- Retain quarantine until D-02 assessment complete

---

## SAFE UNKNOWN

- Quarantine folder naming uses drill-specified slug, not `q-YYYYMMDD-...` protocol format — acceptable for sandbox drill
- Git state at quarantine time — files untracked

---

*End of D-02 quarantine log.*
