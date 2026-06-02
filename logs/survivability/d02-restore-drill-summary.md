# Restore Drill Summary — D-02 Manual Restore

**Log id:** `drill-20260524-d02-restore-summary`  
**Timestamp:** `2026-05-24T19:20:00Z`  
**Severity:** INFO  
**Operator:** cursor-agent-d02-drill  
**Lane:** B  
**Related task / chat:** D-02 Real Manual Restore Drill

---

## Summary

First real human-operated restore drill completed. Drifted sandbox quarantined; clean tree restored manually from snapshot to new workspace. All mirrored files achieve hash parity with snapshot. No production impact. No git commit/push. No automation.

---

## Evidence

| Artifact | Path |
|----------|------|
| Quarantine | `workspaces/_quarantine/d01-survivability-drill-drifted/` |
| Restored workspace | `workspaces/_sandbox/d01-survivability-drill-restored/` |
| Snapshot (untouched) | `workspaces/_snapshots/snap-20260524-012224-d01-drill/` |
| Pre-restore analysis | `logs/rollback-history/d02-pre-restore-analysis.md` |
| Quarantine log | `logs/rollback-history/d02-quarantine-log.md` |
| Diff validation | `logs/rollback-history/d02-diff-validation.md` |
| Manifest validation | `logs/rollback-history/d02-manifest-validation.md` |
| Rollback map | `logs/rollback-history/d02-rollback-map-draft.json` |
| Human review | `projects/mars-survivability/reports/d02-human-operated-restore-review-v1.md` |
| Readiness | `projects/mars-survivability/reports/d02-survivability-readiness-v1.md` |

---

## Steps completed

| Step | Status | Severity notes |
|------|--------|----------------|
| 1 — Pre-restore analysis | DONE | WARNING — drift detected |
| 2 — Quarantine | DONE | INFO — move-only |
| 3 — Manual restore | DONE | INFO — selective copy |
| 4 — Diff validation | DONE | INFO — parity PASS |
| 5 — Manifest validation | DONE | INFO — WARNING acceptable |
| 6 — Rollback map draft | DONE | INFO |
| 7 — Operator review | DONE | INFO |
| 8 — Observability log | DONE | INFO |
| 9 — Readiness assessment | DONE | INFO |
| 10 — Report | DONE | INFO |

---

## Key findings

| Finding | Severity |
|---------|----------|
| Restored files match snapshot (hash) | INFO |
| Drift file excluded from restored tree | INFO |
| Partial mirror gap (index.html) | WARNING |
| Validator WARNINGs on drill snapshot | WARNING |
| Quarantine preserves full drift evidence | INFO |

---

## Survivability confidence

**Moderate-high** for documented human-operated sandbox restore.  
**Low** for automated/production enforcement (by design).

---

## Follow-up

- Human sign-off on D-02 reports
- Optional G5: production-scoped tabletop
- Archive or retain quarantine per operator decision

---

## SAFE UNKNOWN

- Real incident operator performance under stress
- Hook integration not in scope

---

*End of D-02 restore drill summary.*
