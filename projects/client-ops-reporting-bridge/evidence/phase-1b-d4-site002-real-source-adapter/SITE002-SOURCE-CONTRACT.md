# Canonical SITE002MonitorResult Contract

**Version:** `site002-monitor-result-v1`

## Required inputs (directory)

1. monitor-classification.json
2. changed-summary.json
3. run-summary.json

Incomplete set causes reject (ADAPTER_SOURCE_REJECTED / BLOCKED).

## Required machine fields

| Field | Source | Validation |
|-------|--------|------------|
| source_run_id | run-summary.run_id | non-empty string |
| observed_at | finished_at preferred else monitor timestamps | ISO-8601 |
| source_status | monitor classification | one of four supported values |
| baseline_count | changed baseline_url_count | non-negative int |
| current_count | changed current_url_count | non-negative int |
| added_urls | changed added_count | non-negative int |
| removed_urls | changed removed_count | non-negative int |
| onboarding_needed_count | prefer monitor | non-negative int |
| exit_code | run-summary | int when present |

Fail-closed: missing/unsupported/invalid/contradictory never map to OK. No fabricated metrics.
