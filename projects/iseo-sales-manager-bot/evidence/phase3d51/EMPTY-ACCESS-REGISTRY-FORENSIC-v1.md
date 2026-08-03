# EMPTY ACCESS REGISTRY FORENSIC v1

**Captured:** 2026-08-03T16:58:19.993Z

| Component | Expected | Actual Before Repair | Result |
|---|---:|---:|---|
| ACCESS_CONTROL Admin active | 1 | 0 | FAIL |
| ACCESS_CONTROL moderator active | 1 | 0 | FAIL |
| ACCESS_CONTROL duplicate identities | 0 | 0 | PASS |
| Invalid roles | 0 | 0 | PASS |
| Invalid statuses | 0 | 0 | PASS |
| ACCESS_EVENTS malformed rows | 0 | 0 | PASS (seed events well-formed) |
| ACCESS_CONTROL data rows | ≥2 | 0 | FAIL — headers only |

**Root cause of empty ACCESS_CONTROL:** Phase 3D.5 bootstrap AppendAccess used `$json.appendAccess` after WriteHeaders, so the append body referenced the HTTP response instead of DiffData. Headers existed; identity rows did not. Runtime therefore authorized via CONFIG allowlists.

**CONFIG fallback state before repair:** admin_user_ids present (1); manager_action_user_ids present (2). Effective SoT was CONFIG, not ACCESS_CONTROL.
