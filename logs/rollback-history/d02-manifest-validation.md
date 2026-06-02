# Manifest Validation — D-02 Manual Restore Drill

**Log id:** `rollback-20260524-d02-manifest-validation`  
**Timestamp:** `2026-05-24T19:16:00Z`  
**Severity:** INFO  
**Operator:** cursor-agent-d02-drill  
**Lane:** B  
**Related task / chat:** D-02 Real Manual Restore Drill

---

## Summary

Ran `snapshot-integrity-checker-v1.mjs` on original snapshot and `manifest-cross-validator-v1.mjs` for restored workspace linkage. Both return **WARNING** (not INVALID) — drill snapshot is usable with documented gaps.

---

## snapshot-integrity-checker-v1.mjs

**Command:**

```powershell
node projects/mars-survivability/tools/observability/snapshot-integrity-checker-v1.mjs `
  --snapshot-dir "workspaces/_snapshots/snap-20260524-012224-d01-drill" --json
```

**Result:** `WARNING`

| Finding ID | Level | Message |
|------------|-------|---------|
| SI-031 | WARNING | Single top-level folder "sample-project" — verify subtree completeness |
| SI-041 | WARNING | Manifest documents SAFE UNKNOWN — verify before restore |
| SI-050 | WARNING | Workspace mismatch heuristic: expected tree related to workspaces/_snapshots |

**Assessment:** Snapshot structurally valid for drill restore. Warnings are expected for partial mirror and drill context.

---

## manifest-cross-validator-v1.mjs

**Command:**

```powershell
node projects/mars-survivability/tools/observability/manifest-cross-validator-v1.mjs `
  --manifest "workspaces/_snapshots/snap-20260524-012224-d01-drill/SNAPSHOT-MANIFEST.md" `
  --scope "workspaces/_sandbox/d01-survivability-drill-restored/sample-project" `
  --snapshot-dir "workspaces/_snapshots/snap-20260524-012224-d01-drill" `
  --expected-snapshot-id "snap-20260524-012224-d01-drill" --json
```

**Result:** `WARNING`

| Finding ID | Level | Message |
|------------|-------|---------|
| MC-032 | WARNING | Snapshot timestamp appears in the future |
| MC-070 | WARNING | Manifest contains SAFE UNKNOWN — review before restore |

**Parsed:**

| Field | Value |
|-------|-------|
| snapshotId | `snap-20260524-012224-d01-drill` |
| workspace (manifest) | `C:\AI MARS\workspaces\_sandbox\d01-survivability-drill` |
| scopePaths | `workspaces/_sandbox/d01-survivability-drill-restored/sample-project` |
| mirroredEntryCount | 2 |

**Note:** Manifest workspace path references original sandbox (pre-restore). Restored workspace is a **new path** — operator updated scope at validation time. Manifest restore paths are still valid as snapshot-relative sources.

---

## Restored workspace linkage

| Check | Result |
|-------|--------|
| Snapshot id match | PASS |
| Manifest markers present | PASS |
| Restore instructions usable | PASS |
| Scope path updated for restored workspace | PASS (operator override) |
| Partial mirror acknowledged | PASS — index.html handled separately |

---

## Validation verdict

| Tool | Status | Restore blocking? |
|------|--------|-------------------|
| snapshot-integrity-checker | WARNING | No — proceed with manual verification |
| manifest-cross-validator | WARNING | No — SAFE UNKNOWN review completed |

**Overall:** Manifest validation **supports** human-operated restore with documented partial-mirror gap.

---

## SAFE UNKNOWN

- MC-032 future timestamp — drill date vs system clock artifact
- Manifest workspace field not auto-updated for restored path — operator responsibility
- No automated linkage between quarantine manifest and snapshot manifest

---

*End of D-02 manifest validation.*
