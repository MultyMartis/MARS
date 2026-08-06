# TEST-RESULTS

| Gate / check | Result |
|--------------|--------|
| D5R2_CANDIDATE_FRESH | PASS |
| D5R2_SOURCE_AUTHORITY_REVALIDATED | PASS |
| D5R2_CLEAN_RUNTIME_REVALIDATED | PASS |
| CLIENT_OPS_LIVE_BASELINE_MATCH | PASS |
| D5R2_EVENT_UNSEEN | PASS |
| D5R2_OFFLINE_PREVIEW_REVALIDATED | PASS |
| D5R2_SECURITY_GATE_PASS | PASS |
| D5R2_CHARTER_ARMED | PASS |
| Final pre-POST freshness | PASS (age 14920 ≤ 93600) |
| Live POST | EXECUTED once |
| HTTP 202 FIRST_SEEN | FAIL (HTTP 404) |
| n8n execution +1 | FAIL (31→31) |
| Data Table event row +1 | FAIL (0→0) |
| Telegram delivery | FAIL (0) |
| No retry / no replay | PASS |
| Runtime remains clean | PASS |
| Source immutable | PASS |
| Workflow remains inactive | PASS |
