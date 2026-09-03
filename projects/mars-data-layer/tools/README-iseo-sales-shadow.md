# ISEO Sales Sheets → PG shadow tools

## Commands (from this directory)

```text
python iseo_sales_sheets_to_pg_shadow.py inventory
python iseo_sales_sheets_to_pg_shadow.py dry-run
python iseo_sales_sheets_to_pg_shadow.py apply
python iseo_sales_sheets_to_pg_shadow.py reconcile
python iseo_sales_sheets_to_pg_shadow.py prove-live
```

Orchestrator uploads `iseo_sales_shadow_worker.py` to VEESP, runs under sudo, downloads sanitized evidence to:

`../evidence/shadow-migration/iseo-sales-v1/`

## Authority

Sheets = authoritative. PostgreSQL = shadow only. No n8n cutover from these tools.
