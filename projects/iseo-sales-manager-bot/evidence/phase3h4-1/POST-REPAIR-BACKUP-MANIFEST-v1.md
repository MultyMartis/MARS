# POST-REPAIR BACKUP MANIFEST v1

**Location (private):** `...\runtime\backups\post-repair\`

| Artifact | Git? |
|---|---|
| Admin.dev.raw.json | NO |
| Operational.dev.raw.json | NO |
| Admin.dev.meta.json | hashes/node counts YES via evidence |
| Operational.dev.meta.json | YES via evidence |

## Rollback

Restore Admin Status jsCode to sha `2138ecea924042196fec246a67049bf0ad13cd6b0cf425950514ced61ee596ad` from pre-repair raw; optionally clear/re-set CONFIG cache keys; do not touch LEADS.
