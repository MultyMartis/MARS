# REQUIRED-RUNTIME-FILE-MATRIX

| Path | Origin authority | Local committed state | MAIN WT | Required merged state |
|------|------------------|-----------------------|---------|-----------------------|
| `.../site-002-prod-post-1c-catalog-onboarding-monitor-02.py` | `9c0272f6` @ `af5f3fca` / origin tip | `f2273b18` (regressive) | `2de8773c` (foreign WIP) | **origin blob `9c0272f6`** |
| `.../site-002-post-1c-monitor-runner.ps1` | `f699e5cc` (pre-repair) | `a96b7aef` @ `9a48e93b` | same as HEAD | **keep local repair `a96b7aef`** |
| `.../site-002-post-1c-monitor-runner-finish-summary-authority-regression.ps1` | absent | `a125ce31` @ `9a48e93b` | same as HEAD | **keep local harness `a125ce31`** |

## Classification

`MONITOR_BASELINE_DELTA_ISOLATABLE`

Only the monitor script requires origin materialization. Runner and harness must remain local accepted repair.
