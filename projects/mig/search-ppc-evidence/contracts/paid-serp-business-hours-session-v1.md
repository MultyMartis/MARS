# Paid SERP — Business Hours Session Contract v1

**Mode:** `PAID SERP — BUSINESS HOURS`  
**Lifecycle stage:** SPPC-10

## Required session configuration

- `project_id`, `manifest_path`, `lifecycle_stage`, `lifecycle_action`
- `query_set`, `query_selection_rationale`
- `region`, `search_engine`, `device_profile`, `timezone`
- `allowed_local_collection_windows`, `weekday_policy`, `approved_exceptions`
- `requested_date`, `pause_policy`, `batch_policy`
- `captcha_policy` (default: `STOP_ON_CAPTCHA`)
- `stop_policy`, `capture_policy`, `landing_follow_policy`
- `output_path`

## Authorization

No session may start without lifecycle gate authorization via `mig-ppc-gate.mjs` / `authorizeAction`.

## Business-hours validation

Statuses: `WITHIN APPROVED BUSINESS-HOURS WINDOW`, `OUTSIDE APPROVED WINDOW`, `APPROVED EXCEPTION`, `TIMEZONE UNRESOLVED`, `WINDOW NOT CONFIGURED`

Blocker: `BLOCKED — PAID SERP BUSINESS-HOURS WINDOW NOT SATISFIED`

## Evidence honesty

| State | Meaning |
|-------|---------|
| ADS OBSERVED | Structured ad observations captured |
| NO ADS OBSERVED | Valid for exact query/timestamp/region/device only |
| CAPTCHA | Collection degraded; not complete |
| COLLECTION DEGRADED | Partial session with explicit degraded record |

## Execution receipt

Every run writes lifecycle execution receipt reference in session summary.
