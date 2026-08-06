# CLIENT-OPS-COMPATIBILITY

## Adapter contract

D4/D5 fail-closed on `SOURCE_ARTIFACT_CONFLICT` remains correct and **must not** be weakened.

Emitter repair restores future equality:

`monitor-classification.classification == run-summary.classification`

(and next_action where applicable) for successful completed artifact families **after runtime deploy**.

## Historical candidates (unchanged)

| Candidate event_id | Role |
|--------------------|------|
| `e30ef970-7ea1-561b-ac2d-411201ba04c8` | Candidate 1 conflict evidence (ONBOARDING vs NO_ACTION) |
| `b819e684-8a5e-5793-8b91-4543b43fa52f` | Candidate 2 |
| `9244a403-12cb-5424-80d8-c65cfa22db3c` | Candidate 3 |

Raw historical artifacts not rewritten.

## Live GET-only (this phase)

| Check | Result |
|-------|--------|
| Workflow `tkM4H0G0gM3q9Foi` active | false |
| nodes | 17 |
| versionId | `3d2fd6fc-bc17-4e0f-b9e5-086c959afd29` |
| executions | 31 |
| running (status=running) | 0 |
| Data Table `H6VYhwz7RXZCBMmu` columns/rows | 15 / 2 |
| mutations | 0 |

## D5 charter

`UNUSED` — `charter_consumed=false`, `real_http_requests=0`
