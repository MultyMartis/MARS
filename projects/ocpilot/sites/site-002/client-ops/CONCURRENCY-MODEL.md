# SITE-002 — Concurrency / Locking Model

## Hard limits

```
MAX_SAFE_IMPORT_CONCURRENCY=1
MAX_SAFE_REPORT_CONCURRENCY=1
```

## Import

- Singleton lock around canonical runner.
- If manual and scheduled overlap: only one proceeds; other waits/fails safely — **never** parallel imports.

## Reporting

- Dedupe + sequential report handling; no concurrent uncontrolled producers.
- Retired Windows producer must stay disabled to avoid duplicate producers.

## Race boundaries

- File-arrival race (exchange incomplete when wrapper starts) → may contribute to missing offers — OPEN forensic.
- Stale backlog selection (oldest-first without freshness) — anti-pattern; do not revive.
