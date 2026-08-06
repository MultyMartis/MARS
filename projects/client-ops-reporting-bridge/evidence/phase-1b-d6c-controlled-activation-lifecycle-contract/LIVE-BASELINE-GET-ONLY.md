# LIVE-BASELINE-GET-ONLY

**Token:** `D6C_LIVE_BASELINE_RECONFIRMED`

Method: GET-only (`_get-precheck.mjs`). No activation. No webhook. No Data Table mutation.

| Field | Expected | Observed |
|-------|----------|----------|
| active | false | false |
| nodes | 20 | 20 |
| executions | 34 | 34 |
| running | 0 | 0 |
| versionId | dc8746bf-df9c-425d-9b3f-4ace452ac5ef | match |
| Data Table columns | 15 | 15 |
| Data Table rows | 4 | 4 |
| Historical c84e29bf-… | FIRST_SEEN / ATTENTION / PENDING | match |
| D6A2 synthetic d6a2a001-… | FIRST_SEEN / OK / SENT | match |

Postcheck after offline implementation: unchanged (`D6C_NO_LIVE_MUTATIONS`).
