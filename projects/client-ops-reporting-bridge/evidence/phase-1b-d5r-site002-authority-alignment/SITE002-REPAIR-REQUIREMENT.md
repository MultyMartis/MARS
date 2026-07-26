# SITE002-REPAIR-REQUIREMENT

## Status

`SITE002_MONITOR_REPAIR_REQUIRED`

**D5R did not apply this repair.** SITE-002 locus contains pre-existing foreign/manual WIP. Future phase must reconcile WIP before edit.

## Primary file requiring repair

`projects/ocpilot/sites/site-002/tools/site-002-post-1c-monitor-runner.ps1`

Function: `Finish-Summary`

## Current writer logic (defect)

1. If `$summary.classification` is empty after monitor exit 0, set `NO_ACTION_REQUIRED`.
2. If `$summary.next_action` empty, set generic “Review run-summary.json and monitor-classification.json…”.
3. Load monitor-written `run-summary.json`.
4. Copy monitor properties into merge map.
5. Overwrite merge map with every non-null runner `$summary` value — including the defaults from steps 1–2.
6. Rewrite `run-summary.json` / `.md`.

`monitor-classification.json` is left truthful → disagreement.

## Required logic (design only)

1. Merge monitor `run-summary.json` first as base.
2. Add/override **runner-only metadata** keys (python path, timezone, local timestamps, runner_script, duration measured by runner, etc.).
3. **Never default or overwrite** `classification` / `next_action` when monitor already provided them.
4. Only set classification defaults when monitor summary is missing those fields (true runner-only failure/dry-run paths).
5. Prefer: if monitor classification present, it wins; runner must not invent `NO_ACTION_REQUIRED` on successful monitor completion.
6. Optionally assert `monitor-classification.json.classification == run-summary.classification` after write; fail the runner loudly on mismatch.

## Expected artifact changes after repair

| Case | monitor-classification | run-summary.classification | next_action |
|------|------------------------|----------------------------|-------------|
| Onboarding success | ONBOARDING_REQUIRED | ONBOARDING_REQUIRED | monitor next_action text |
| Quiet success | NO_ACTION_REQUIRED | NO_ACTION_REQUIRED | monitor next_action text |
| Monitor failure | FAILURE_REVIEW_REQUIRED (or absent monitor class) | FAILURE_REVIEW_REQUIRED | failure guidance |

## Python monitor

`site-002-prod-post-1c-catalog-onboarding-monitor-02.py` `export_scheduled_artifacts` already writes matching classifications. **No Python change required** for this root cause unless a follow-up audit finds a second defect.

## Tests needed (future SITE-002 charter)

1. Fixture: mock monitor-written run-summary with ONBOARDING_REQUIRED; runner Finish-Summary must preserve it.
2. Fixture: quiet NO_ACTION_REQUIRED preserved.
3. Fixture: missing monitor summary → runner may default.
4. Post-condition equality check vs `monitor-classification.json`.
5. Regression: duration/runner metadata still merged.

## Rollback boundary

- Touch only runner.ps1 (and README note).
- No Production mutation, no scheduler reinstall required if task already points at repo runner (Category A), but operator must confirm live task path after WIP reconciliation.
- Do not stage unrelated SITE-002 foreign WIP.

## Conflict with foreign WIP

SITE-002 currently shows unrelated modified/untracked tools, backups, reports. D5R-MON must inventory and exclude foreign WIP; edit only allowlisted runner path after explicit destructive/edit charter.

## Deploy / execute

No execution/deploy in D5R. Future repair charter decides whether one controlled monitor run is authorized to mint a fresh MATCH artifact.
