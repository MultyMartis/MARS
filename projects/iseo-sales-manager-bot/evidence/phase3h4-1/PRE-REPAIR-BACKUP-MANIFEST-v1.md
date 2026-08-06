# PRE-REPAIR BACKUP MANIFEST v1

**Location (private):** `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3h41-20260806-200401\runtime\backups\pre-repair\`

| Artifact | Contents | Git? |
|---|---|---|
| Admin.dev.raw.json | Full Admin export | NO |
| Operational.dev.raw.json | Full Ops export | NO |
| Admin.dev.sanitized-meta.json | id/active/nodeCount/hashes | manifest only |
| Operational.dev.sanitized-meta.json | id/active/nodeCount/hashes | manifest only |
| CONFIG-interest.sanitized.json | allowlisted CONFIG keys | NO values with PII |
| production-truth.sanitized.json | PROD_LEAD_1 lifecycle summary | aliases only |

## Hashes (pre-repair)

- Status sha256: `2138ecea924042196fec246a67049bf0ad13cd6b0cf425950514ced61ee596ad`
- Admin nodes: 85 · active true
- Ops nodes: 45 · active true

## Rollback

1. Deactivate Admin + Ops
2. PUT Admin from pre-repair raw backup
3. Reactivate Admin + Ops
4. Do **not** rewrite LEADS / LEAD_EVENTS
