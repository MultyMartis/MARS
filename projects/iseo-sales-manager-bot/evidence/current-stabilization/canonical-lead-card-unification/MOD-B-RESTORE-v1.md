# MOD-B-RESTORE-v1

| Field | Value |
|---|---|
| Restore completed | 2026-08-28T11:38:55Z |
| Evidence file | forensic/mod-b-restore.json |
| MOD_B status after restore | **active** |
| Graph integrity | pass (restored from pre-revoke snapshot) |
| MOD_B_ACCESS_FINAL == active | **1** |

## Isolation window

- Revoke: 11:07:19Z  
- Restore: 11:38:55Z  
- Duration: ~31 min

## Operator constraint

No live `/moderators` re-probe after closeout — restore attested from forensic only.
