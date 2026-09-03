# RESULT-SUMMARY-v1

```json
{
  "text": "SERVER PG18 SCHEMA APPLY PASS \u2014 ISEO SALES READY FOR SHADOW DATA MIGRATION",
  "pg17_to_pg18": "PASS",
  "gates": {
    "preflight": "PASS-RESUME",
    "pre_dump": "ALREADY-DONE-PRIOR-RUN",
    "apply": "ALREADY-DONE-PRIOR-RUN",
    "upload": "PASS",
    "cleanup_synthetic": "PASS",
    "tests": "PASS",
    "inventory": "PASS",
    "post_dump": "PASS",
    "n8n_unchanged": "PASS",
    "resources": "HEALTHY"
  }
}
```

## Facts (sanitized)

```json
{
  "pre_dump": null,
  "post_dump": {
    "timestamp_utc": "20260903T074124Z",
    "database": "mars",
    "format": "plain sql gzip",
    "path": "/root/mars-backups/postgres/mars-post-app-schema-20260903T074124Z.sql.gz",
    "bytes": "10387"
  },
  "n8n_unchanged": {
    "id_unchanged": true,
    "started_unchanged": true,
    "restart_count": "0",
    "version_ok": true,
    "api_before": {
      "total": 36,
      "active": 7
    },
    "api_after": {
      "total": 36,
      "active": 7
    },
    "after_line": "NAME=/n8n_n8n_1 ID=d9446ed55dc171a6212538168ae17f6842329f077f2533c0b17d5c30c1965a9d IMAGE=sha256:22511cc8b434a9ce443b4ddb267a5c2cb1506ad1afc22ad60b28c5192f8f5b9e STATUS=running STARTED=2026-09-01T06:01:12.295522361Z RESTARTCOUNT=0"
  },
  "resources": {
    "classification": "HEALTHY",
    "raw_tail": "===FREE===\n               total        used        free      shared  buff/cache   available\nMem:           3.8Gi       1.2Gi       213Mi        28Mi       2.7Gi       2.6Gi\nSwap:          2.0Gi       268Ki       2.0Gi\n===SWAP===\nNAME      TYPE SIZE USED PRIO\n/swapfile file   2G 268K   -2\n===DF===\nFilesystem      Size  Used Avail Use% Mounted on\n/dev/sda2        79G   49G   27G  66% /\n===LOAD===\n 07:41:28 up 2 days,  1:40,  1 user,  load average: 0.33, 0.30, 0.27\n===STATS===\nctr=mars-postgres mem=33.9MiB / 3.824GiB cpu=0.32%\nctr=n8n_n8n_1 mem=1.106GiB / 3.824GiB cpu=0.40%\n"
  },
  "tests": {
    "_grant_membership.sql": "PASS",
    "fixtures/iseo_sales/synthetic_v1.sql": "PASS",
    "tests/iseo_sales/02_constraints.sql": "PASS",
    "tests/iseo_sales/03_permissions.sql": "PASS",
    "tests/iseo_sales/04_extended_local_validation.sql": "PASS",
    "tests/iseo_sales/05_inventory_and_explain.sql": "PASS"
  },
  "migration_role": null
}
```
