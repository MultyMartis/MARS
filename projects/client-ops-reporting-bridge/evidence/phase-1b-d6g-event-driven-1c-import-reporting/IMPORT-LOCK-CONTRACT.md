# Shared Import Lock

Path: `/storage/mars-tools/cron/mars_1c_import.lock`

JSON payload: pid, run_id, phase, trigger_source, started_at, site_id

Overlap: second launch rejected with «Импорт уже выполняется» — active import not terminated.

Stale recovery: only when age > 3600s AND process proven inactive (`posix_kill` 0).
