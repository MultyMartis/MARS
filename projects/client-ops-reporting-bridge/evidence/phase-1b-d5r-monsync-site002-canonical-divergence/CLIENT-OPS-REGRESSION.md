# CLIENT-OPS-REGRESSION

Offline only. Live POST = **0**. Network calls from D4/D5 offline commands = **0**.

## D4 adapter

Command: `site002-adapter-dry-run --source <MOND run 2026-07-26_17-48-38>`

| Field | Value |
|-------|-------|
| validation_result | PASS |
| final_state | INTAKE_ACCEPTED |
| ok | true |
| network_calls | 0 |
| event_id | c84e29bf-79b1-5aea-98c4-9dc8d651fc96 |
| baseline_count | 1737 |

## D5 preview

Command: `site002-controlled-live --dry-run --preview-only --source <same>`

| Field | Value |
|-------|-------|
| final_state | D5_PREVIEW_READY |
| ok | true |
| network_calls | 0 |
| d5_charter_consumed | false |
| preview approved | true |

## D5R authority validator

`validate-client-ops-d5r-site002-authority-alignment.mjs` → `ok=true`, failures=[]

## Live GET-only sanity (no mutation)

| Item | Observed |
|------|----------|
| workflow active | false |
| nodes | 17 |
| executions (page) | 31 |
| running (status=running) | 0 |
| versionId | 3d2fd6fc-bc17-4e0f-b9e5-086c959afd29 |
| Data Table rows | 2 |
| event_id occurrences | 0 |
| mutations | 0 |

Note: one historical execution id 3410 has `finished=false` with `status=error` (stopped); not an active run.
