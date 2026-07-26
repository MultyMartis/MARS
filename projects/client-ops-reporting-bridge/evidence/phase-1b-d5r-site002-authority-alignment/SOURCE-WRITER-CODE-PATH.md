# SOURCE-WRITER-CODE-PATH

Read-only trace. No monitor execution. No SITE-002 edits.

## Writers

### A. Python monitor — `site-002-prod-post-1c-catalog-onboarding-monitor-02.py`

| Step | Function / site | Responsibility |
|------|-----------------|----------------|
| 1 | `classify_monitor_run(...)` | Computes single `(classification, next_action)` from monitor health + delta + onboarding + hygiene |
| 2 | `main()` success path | Calls `classify_monitor_run`, writes deployment `reports/monitor-summary.json` |
| 3 | `export_scheduled_artifacts(...)` | When `--scheduled-run-dir` set, writes the three Client Ops authorities |

Order inside `export_scheduled_artifacts`:

1. `changed-summary.json` (delta metrics only; **no** classification field)
2. hygiene companions
3. `monitor-classification.json` with `classification` / `next_action` / counts
4. `run-summary.json` with the **same** `classification` / `next_action` plus run identity / exit / duration / counts

Intended invariant:  
`monitor-classification.classification == run-summary.classification` after Python export.

Exception path: on failure, may write a thin `run-summary.json` with `FAILURE_REVIEW_REQUIRED` only (no full trio). That path cannot produce `ONBOARDING_REQUIRED` vs `NO_ACTION_REQUIRED`.

### B. PowerShell runner — `site-002-post-1c-monitor-runner.ps1`

| Step | Function | Responsibility |
|------|----------|----------------|
| 1 | Create timestamped run dir; seed `$summary` | Runner metadata; `classification=$null` initially |
| 2 | Invoke Python with `--scheduled-run-dir $runDir` | Monitor writes full artifact family |
| 3 | On exit 0 | Set `$summary.status='success'`; leave classification unset |
| 4 | `Finish-Summary` | Default unset classification → `NO_ACTION_REQUIRED` (exit 0); merge monitor `run-summary.json`; **overwrite** merged keys with non-null runner `$summary` values; rewrite `run-summary.json` / `.md` |

Critical overwrite loop (conceptual):

1. Load monitor `run-summary.json` into merge map.
2. For each runner `$summary` key that is non-null, replace merge map value.
3. Because step 4 already defaulted `classification` / `next_action`, those runner defaults **replace** truthful monitor values.

`monitor-classification.json` is **not** rewritten by the runner.

## Conflict code path producing observed D5 pair

```
Python classify_monitor_run → ONBOARDING_REQUIRED
  → export_scheduled_artifacts writes both JSON files with ONBOARDING_REQUIRED
  → runner Finish-Summary defaults classification=NO_ACTION_REQUIRED (exit 0, unset)
  → merge overwrites run-summary.classification / next_action
  → final disk state:
       monitor-classification.json = ONBOARDING_REQUIRED
       run-summary.json.classification = NO_ACTION_REQUIRED
       run-summary metrics still show onboarding_needs_count / added_count from monitor
```

## Proof from D5R candidate re-read (same 3 labels)

| Candidate | Runner merge markers | monitor class | run class | Internal run metrics vs class |
|-----------|----------------------|---------------|-----------|-------------------------------|
| `site002-post-1c-run/2026-07-26_12-30-02` | `runner_script` present; runner default `next_action` | ONBOARDING_REQUIRED | NO_ACTION_REQUIRED | onboard=7, added=119 with NO_ACTION — **incoherent** |
| `site002-post-1c-run/2026-07-20_22-32-43` | runner merge present; runner default `next_action` | NO_ACTION_REQUIRED | NO_ACTION_REQUIRED | quiet run — **accidental match** |
| `site002-post-1c-run/2026-07-20_12-45-01` | **no** `runner_script` / local start markers | ONBOARDING_REQUIRED | ONBOARDING_REQUIRED | truthful monitor next_action preserved |

## Diagram

```text
sitemap/crawl inputs
        │
        ▼
classify_monitor_run ──► classification / next_action
        │
        ├──────────────► monitor-classification.json  (untouched by runner)
        │
        └──────────────► run-summary.json (Python)
                                │
                                ▼
                     Finish-Summary merge overwrite
                                │
                                ▼
                     run-summary.json (corrupted classification on action-required success)
```
