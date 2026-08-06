# SITE002-SOURCE-CHANGE-BOUNDARY — D6DB

`D6DB_SITE002_MARKER_CHANGESET_MINIMAL`

## Included files (2)

### 1. `site-002-prod-post-1c-catalog-onboarding-monitor-02.py`
- Purpose: emit `run-complete.marker` after authoritative `run-summary.json` is written in `export_scheduled_artifacts`
- Marker schema: `site002-run-complete-marker-v1` with sanitized fields (run_id, finished_at, exit_code, classification)
- Construction: HEAD bytes + additive marker block only
- Explicitly excluded from commit: WT foreign baseline/category-path/expected-count hunks (not D6D marker work)
- Not copied from dirty runtime checkout

### 2. `site-002-post-1c-monitor-runner.ps1`
- Purpose: after merged `run-summary.json` write in `Finish-Summary`, emit the same completion marker
- Diff vs HEAD: +11 lines marker only
- No scheduler command change; no credential/URL/importer/DB logic change

## Excluded SITE-002 paths
- `tools/README.md` unrelated doc rows
- All `site-002-prod-category-lari-*` tools
- Runtime checkout WIP monitor-02.py
