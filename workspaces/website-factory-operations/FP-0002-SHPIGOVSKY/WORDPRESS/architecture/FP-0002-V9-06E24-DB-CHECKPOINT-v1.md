# FP-0002 V9-06E24 DB Checkpoint

Fresh full dump before E24 hero CTA field/seed work.

| Item | Value |
|---|---|
| Wave | V9-06E24 |
| Checkpoint | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e24-hero-cta-button-text-per-entity-pre-20260707-212945` |
| Dump | `mars_wp_fp0002.sql` |
| SHA256 | `81F44938880CCB9188388FC0154F6C306A75C67E478967D35BBE21325D1399BA` |
| DB | `mars_wp_fp0002` / prefix `fp02_` |
| E22 baseline | `cad17f71` |

Restore:

```bash
mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e24-hero-cta-button-text-per-entity-pre-20260707-212945\mars_wp_fp0002.sql"
```

Evidence: `validation/v9-06e24-hero-cta-button-text-per-entity/db-checkpoint.json`
