# Completion Dispatch

terminal.json → dispatch-inbox → Windows fetch/poller → `run-site-002-import-completion-dispatch.mjs` (exact run_id) → n8n webhook → Telegram → Data Table.

Idempotent: `{run_id}.delivered.json` marker + workflow event_id dedupe.
