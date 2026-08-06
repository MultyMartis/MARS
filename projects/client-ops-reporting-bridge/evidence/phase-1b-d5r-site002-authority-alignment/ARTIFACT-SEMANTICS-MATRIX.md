# ARTIFACT-SEMANTICS-MATRIX

Derived from SITE-002 monitor + runner source (read-only). Not inferred from filenames alone.

| Artifact | Writer / function | Lifecycle point | Written once / rewritten | Semantic purpose | Classification field | Calculation | Value kind | Authoritative for client notification? | Can legitimately differ? |
|----------|-------------------|-----------------|--------------------------|------------------|----------------------|-------------|------------|----------------------------------------|--------------------------|
| `monitor-classification.json` | Python `export_scheduled_artifacts` | End of successful scheduled export | Once per successful export (Python only) | Catalog **action** classification + supporting counts | `classification` | `classify_monitor_run` | onboarding/action classification (also encodes failure when monitor unhealthy) | **Yes — primary action authority** once consistent | Must match intended run-summary.classification; difference = emitter defect |
| `changed-summary.json` | Python `export_scheduled_artifacts` | Before classification JSON in same export | Once per successful export | Delta metrics (baseline/current/added/removed/page types) | **none** | Delta counters | catalog-delta metrics | Metrics authority only; cannot alone map OK/ATTENTION without classification | N/A for classification equality |
| `run-summary.json` | Python `export_scheduled_artifacts`, then **rewritten** by runner `Finish-Summary` | Python end-of-export; runner post-process | **Rewritten** by runner after monitor exit | Execution metadata (run_id, status, exit, duration, paths) + **intended duplicate** of classification | `classification` | Intended: same `classify_monitor_run` value; Actual after runner: often default `NO_ACTION_REQUIRED` on exit 0 | Intended: duplicate action classification + run health fields; Actual classification field: **corrupted wrapper default** | Run health/exit/duration **yes**; classification field **not trustworthy while bug exists** | Classification must not differ from monitor; difference is bug, not layer split |

## Answers to load-bearing question 3

`run-summary.classification` is **not** an independent “run healthy / no action” layer.

Evidence:

1. Python writes the identical variable into both files.
2. Hardening docs / tools README present one shared vocabulary for operator classification.
3. Corrupted artifacts retain monitor metrics (`onboarding_needs_count>0`) while classification says `NO_ACTION_REQUIRED`.
4. Quiet runs “match” only because default equals true quiet classification.
5. Candidate without runner merge markers preserves matching truthful `ONBOARDING_REQUIRED`.

Therefore `ONBOARDING_REQUIRED` vs `NO_ACTION_REQUIRED` means **inconsistent bug**, not “run healthy but onboarding required.”

## changed-summary role (question 4)

Supports metric consistency checks (`added_count`, URL counts, page types). Does **not** contain a classification field. Can corroborate onboarding pressure via counts / page types, but the correct repair is to stop corrupting `run-summary.classification`, not to invent a Client Ops rule that ignores run-summary equality while the emitter claims equality.
