# AF5F3FCA-DIFF-INVENTORY

Commit `af5f3fcae588cdf0631ae7b3a4b7b7d48f404ef6` — 10 files, +252 / −22.

| Path | Role | Required for runtime target? |
|------|------|------------------------------|
| `projects/ocpilot/sites/site-002/tools/site-002-prod-post-1c-catalog-onboarding-monitor-02.py` | Monitor baseline 1737 code | **YES** |
| `projects/ocpilot/sites/site-002/tools/README.md` | Tools index text | NO |
| `projects/ocpilot/sites/site-002/baselines/SITE-002-STABLE-PROD-POST-1C-MONITOR-BASELINE-1737-04.md` | Baseline note | NO |
| `projects/ocpilot/sites/site-002/reports/SITE-002-MONITOR-BASELINE-REFRESH-04.md` | Refresh report | NO |
| `projects/ocpilot/sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | Knowledge map | NO |
| `projects/ocpilot/sites/site-002/production-profile.md` | Profile text | NO |
| `projects/ocpilot/sites/site-002/site-passport.md` | Passport text | NO |
| `projects/ocpilot/OCPILOT-STATE.md` | OCPilot state | NO |
| `projects/ocpilot/OPERATIONAL-INDEX.md` | Index | NO |
| `projects/mars-infrastructure/runtime-checkouts.md` | Infra note | NO |

## Monitor hunk groups (runtime-required)

1. Baseline constants → `…BASELINE-1737-04` / `…REFRESH-04`
2. `ONBOARDED_CATEGORY_PATHS` updates (shkafy-i-lari / tech equipment paths)
3. Phase1 expected count / metadata → 1737 / Run 4.288
4. Phase2 baseline/delta reporting → 1737

## Runner / harness

`af5f3fca` did **not** change `site-002-post-1c-monitor-runner.ps1` and did **not** introduce the finish-summary harness.
