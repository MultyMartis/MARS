# Observability Log — D-01 Drill

**Log id:** `observability-20260524-d01-drill`  
**Timestamp:** `2026-05-24T01:24:00Z`  
**Severity:** WARNING  
**Operator:** cursor-agent-d01-drill  
**Lane:** B  
**Related task / chat:** D-01 Sandbox Survivability Drill

## Summary

Four observability tools exercised. Manifest cross-validator and snapshot integrity checker returned WARNING (expected for drill). Registry drift linter returned DRIFT (pre-existing signal). Diff helper correctly flagged critical drift in recovery simulation paths.

## Evidence

- Report: `projects/mars-survivability/tools/observability/reports/d01-observability-results.md`
- Snapshot: `snap-20260524-012224-d01-drill`
- Recovery log: `logs/survivability/d01-recovery-simulation-log.md`

## Drift status

| Source | Status |
|--------|--------|
| registry-drift-linter | DRIFT (RD-030) |
| diff-report-helper (drill paths) | critical / driftSuspicion:true |
| manifest-cross-validator | WARNING |
| snapshot-integrity-checker | WARNING |

## Actions taken

- Validated drill manifest against scope lock
- Linted registry documentation drift
- Checked snapshot structure (relative path)
- Ran diff helper on synthetic drift path list

## Follow-up

- Document absolute-path bug in snapshot-integrity-checker (FP-O01)
- Reconcile RD-030 registry drift in separate human task

## SAFE UNKNOWN

- Full _snapshots/ scan not run (single snapshot dir only)

---

*End of observability log.*
