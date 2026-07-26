# RUNNER-CODE-PATH

## File

`projects/ocpilot/sites/site-002/tools/site-002-post-1c-monitor-runner.ps1`

## Pre-repair Finish-Summary defect

1. Seed `$summary.classification` / `$summary.next_action` as `$null`.
2. On monitor exit 0, leave classification unset.
3. Inside `Finish-Summary`, **before merge**, default:
   - exit 0 → `NO_ACTION_REQUIRED`
   - else → `FAILURE_REVIEW_REQUIRED`
4. Load Python-written `run-summary.json` into merge map.
5. Overwrite merge map with every non-null `$summary` key — including defaults from step 3.
6. Rewrite `run-summary.json` / `.md`.
7. Leave `monitor-classification.json` untouched → authority conflict.

Observed D5 conflict shape:

- `monitor-classification.json` = `ONBOARDING_REQUIRED`
- `run-summary.json` = `NO_ACTION_REQUIRED`

## Post-repair path

1. Update runner metadata (`exit_code`, duration, timestamps, status).
2. **Do not** default classification/next_action before merge.
3. `Merge-RunnerMetadataPreservingMonitorSemantics`:
   - start from runner metadata;
   - overlay monitor summary;
   - re-apply runner non-null keys **except** non-empty semantic keys `classification` / `next_action`.
4. `Complete-RunSummarySemanticDefaults` only if still empty:
   - prefer `monitor-classification.json`;
   - if summary present but class missing → `FAILURE_REVIEW_REQUIRED` (no silent OK);
   - else historical dry-run/no-artifact defaults.
5. Write merged JSON/MD.

## Helpers added

- `Test-NonEmptySemanticValue`
- `Merge-RunnerMetadataPreservingMonitorSemantics`
- `Complete-RunSummarySemanticDefaults`
