# SOURCE-SELECTION-CONTRACT (D5 / Pattern B)

## Allowed

- Explicit completed SITE-002 post-1c run directory under sanitized root class `STORAGE/ocpilot/.../scheduled-monitors/post-1c/`
- Provenance: `REAL_EXISTING_SITE002_MONITOR_ARTIFACT`
- Formal full adapter dry-run (D4 path) before any live gate
- Max **3** candidates inspected for this charter
- Operator must approve a non-BLOCKED, non-stale, non-conflict preview before live phrases

## Required for live approval

1. Three authorities present and parseable: `monitor-classification.json`, `changed-summary.json`, `run-summary.json`
2. Classifications **MATCH** (no `SOURCE_ARTIFACT_CONFLICT`)
3. Not stale (`age_seconds <= STALE_AFTER_SECONDS=93600`) → no `SOURCE_REPORT_STALE`
4. Adapter outcome distributable for client-facing Telegram (not misleading BLOCKED wording for historically quiet OK runs)
5. Deterministic `event_id` unseen in Data Table
6. Preview decision: approved for live

## Forbidden

- `latest` / watch / auto-discovery / glob / path traversal
- Sanitized D4 fixtures as live real-source
- Scheduler connection or “run the scheduler” as next step
- Monitor execution without a separate repair charter
- Absolute Storage paths in Git evidence
- Live POST when any candidate fails pre-live safety

## D5 outcome under this contract

All 3 inspected candidates failed closed. **Selected for live: none.** Preview not approved.
