# POST-REPAIR BACKUP MANIFEST — Phase 3H.4

**Timestamp (UTC):** 2026-08-06T12:16:32.248Z

## Workflows

| Workflow | ID | active | nodes | sha256(raw private) |
|---|---|---|---|---|
| Operational.dev | xSnXPy8cEHoZw6xG | true | 45 | `acf309a73759bd2e79225ce15a7ee966ca45f19144ad7b5807d802cee1bf3761` |
| Admin.dev | wLrLp4WQHm1VJmxz | true | 85 | `daffa1babea4edd4989ab283393f489b4cf8449a02e6d366f4d09feba49ea377` |

## Patch markers

- Reminder Commands Phase 3H.4: true
- Status automatic poll wording: true
- Health probe wording: true
- Operational heartbeat v1.0: true
- Schedule interval minutes: 2

## Storage location (outside Git)

`X:\AI MARS STORAGE\git-sync-iseo-sm-phase3h4-20260806-185304\runtime\backups\post-repair\`

Raw exports and credentials are **not** committed.

## Rollback

1. Deactivate Operational.dev + Admin.dev  
2. PUT prior pre-repair raw exports (private Storage)  
3. Activate both  
4. Confirm node counts 45 / 85 and patch markers absent/present as required by operator charter  

## Soak

- T+0: 2026-08-06 19:15 Europe/Moscow  
- Earliest valid completion: 2026-08-08 19:15 Europe/Moscow  
- Phase 3I.1 blocked  
