# POST-CHANGE BACKUP MANIFEST — Phase 3H.7

**UTC:** 2026-08-10T08:29:54.476Z

Private raw exports: Storage `runtime/backups/post-patch/`.

## Verify
{
  "ops_nodes": 45,
  "admin_nodes": 87,
  "ops_active": true,
  "admin_active": true,
  "eh": true,
  "smr": true,
  "contract": true,
  "kb": true,
  "recent": true,
  "reopenField": true,
  "early": true,
  "pendingEdit": true,
  "pendingIf": true,
  "safe": true
}

## Rollback order
1. PUT Admin.dev from post-patch or pre-change raw
2. PUT Operational.dev Error Handler from pre-change if needed
