# Admin Async Execution

Launch calls canonical wrapper `--enqueue`, returns promptly with run_id.

Status endpoint polled every 5s while active; button disabled while import_active.
