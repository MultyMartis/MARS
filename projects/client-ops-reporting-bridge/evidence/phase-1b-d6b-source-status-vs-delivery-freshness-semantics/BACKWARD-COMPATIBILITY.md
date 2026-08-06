# BACKWARD-COMPATIBILITY

**Token:** `D6B_BACKWARD_COMPATIBILITY_MODEL_DEFINED`

| Field | Role |
|-------|------|
| `normalized_status` | Canonical factual Client Ops status (OK/ATTENTION/FAILED/BLOCKED) |
| `source_status` | Source classification / authority label (unchanged meaning) |
| `stale` | Boolean age flag retained on ProcessResult + envelope.freshness |
| `delivery_eligibility` | **New canonical** evaluation-time gate |
| `summary_code=SOURCE_REPORT_STALE` | **Deprecated as factual rewrite**; no longer emitted solely for age |
| `distributable` | Now means customer-channel publishable (`FRESH_AND_ELIGIBLE` + non-BLOCKED) |

Compatibility does not reintroduce stale→BLOCKED conflation.

Historical Phase 0A docs that say `stale=true → BLOCKED` are superseded for this axis by D6B offline model; envelope schema shape unchanged.
