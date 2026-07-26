# REGRESSION-TEST-RESULTS

**Command:**

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File `
  "projects/ocpilot/sites/site-002/tools/site-002-post-1c-monitor-runner-finish-summary-authority-regression.ps1"
```

**Result:** `11/11 PASS`

| Case | Result | Detail |
|------|--------|--------|
| ONBOARDING | PASS | `ONBOARDING_REQUIRED` + `SYNTHETIC_ONBOARDING_ACTION` preserved despite runner `NO_ACTION_REQUIRED` default temptation |
| NO_ACTION | PASS | preserved |
| HYGIENE | PASS | preserved |
| FAILURE | PASS | preserved |
| next_action | PASS | `SYNTHETIC_ONBOARDING_ACTION` preserved |
| missing → monitor-classification | PASS | `ONBOARDING_REQUIRED` from companion JSON |
| missing fail-safe | PASS | `FAILURE_REVIEW_REQUIRED` (no silent OK) |
| no monitor summary failure | PASS | runner failure class kept |
| metadata enrichment | PASS | duration / human / runner_finished_at present |
| syntax | PASS | parser errors=0 |
| temp not Storage | PASS | temp under Local\Temp |

## Semantic overwrite verdict

`RUN_SUMMARY_SEMANTIC_OVERWRITE_FIXED`
