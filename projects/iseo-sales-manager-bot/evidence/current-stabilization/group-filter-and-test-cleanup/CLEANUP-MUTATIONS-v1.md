# CLEANUP-MUTATIONS-v1

## Strategy

Model-safe archival on CLEAN: set `manager_status=processed` with `close_reason=legacy_synthetic_fixture_cleanup` and SYSTEM actor fields. Prefer **row_number** matching so duplicate CLEAN copies of the same `lead_id` are all archived.

Temp n8n workflows only (`__TMP_*`); Admin.dev not replaced by cleanup WF.

## Pass 1 (`lead_id` match)

- Updated ~49 unique proven pending IDs.
- Incomplete for multi-row duplicates (same `lead_id`).

## Pass 2 (`row_number` match)

| Field | Value |
|-------|-------|
| Contract | `iseo-legacy-synthetic-fixture-cleanup-by-row-v1.0` |
| mutated_rows | 23 |
| proven_pending_after | **0** |
| ok | true |

## Not done

- No SAFE_UNKNOWN / PRODUCTION_REAL status changes.
- No ACCESS / AI / reminder schedule / `last_window` / claims changes.
- No mass LEAD_EVENTS deletion.
- Full production CLEAN duplicate forensic deferred.
