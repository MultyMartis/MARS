# Drill Summary — D-01 Sandbox Survivability

**Log id:** `drill-20260524-d01-summary`  
**Timestamp:** `2026-05-24T01:35:00Z`  
**Severity:** INFO  
**Operator:** cursor-agent-d01-drill  
**Lane:** B  
**Related task / chat:** D-01 Sandbox Survivability Drill

## Summary

First real survivability drill completed entirely within `workspaces/_sandbox/`. All G0–G4 tooling flows exercised: snapshot discipline, validator, helpers, observability, and manual recovery simulation. No production workspaces modified. No git commit/push. No destructive ops outside sandbox.

## Evidence

| Artifact | Path |
|----------|------|
| Sandbox workspace | `workspaces/_sandbox/d01-survivability-drill/` |
| Snapshot | `workspaces/_snapshots/snap-20260524-012224-d01-drill/` |
| Validator report | `projects/mars-survivability/tools/validator/reports/d01-validator-results.md` |
| Helper reports | `projects/mars-survivability/tools/helpers/reports/d01-*` |
| Observability report | `projects/mars-survivability/tools/observability/reports/d01-observability-results.md` |
| Recovery simulation | `logs/survivability/d01-recovery-simulation-log.md` |
| Assessment | `projects/mars-survivability/reports/d01-operational-drill-assessment-v1.md` |

## Steps completed

| Step | Status |
|------|--------|
| 1 — Sandbox workspace | DONE |
| 2 — Mock snapshot | DONE |
| 3 — Validator flow | DONE |
| 4 — Snapshot helper | DONE |
| 5 — Scope analyzer | DONE |
| 6 — Observability flow | DONE |
| 7 — Recovery simulation | DONE (drift retained) |
| 8 — Operational logs | DONE |
| 9 — Assessment | DONE |

## Key findings

- Validator DENY path is strong for forbidden commands
- Sandbox Q-tier inherits parent zone friction (NEED_HUMAN / PROTECTED-ZONE-HIT)
- Observability tools useful but require relative repo paths on Windows
- Manual restore guidance is clear; no automated rollback in stack

## Survivability confidence

**Moderate-high** for documented human-operated flow. **Low** for automated enforcement (by design).

## Follow-up

- D-02: repeat with operator executing manual restore
- Registry reconciliation for RD-030
- Consider sandbox zone label exemption proposal

## SAFE UNKNOWN

- Hook/automation integration not in scope
- Untracked sandbox files — git baseline not established for drill tree

---

*End of D-01 drill summary.*
