# Windows Task Postcheck

Captured from live Task Scheduler.

| Task | State | LastResult | Client Ops delivery dependency |
|---|---|---|---|
| MARS_SITE_002_Import_Completion_Poller | Disabled | 1 (stale) | No — DISABLED_AND_RETIRED |
| MARS_SITE_002_Client_Ops_Producer | Disabled | non-zero stale | No — DISABLED |
| MARS_SITE_002_Post_1C_Catalog_Monitor | Ready | 0 | Hygiene only — KEEP_WINDOWS_HIDDEN_NONINTERACTIVE |

## Post_1C runner

- Path: `site-002-post-1c-monitor-runner.ps1`
- D6G1A self-hide (`ShowWindow`) present
- Trigger: daily (not 2-minute PowerShell spam source)
- LastRun: 2026-08-12 14:25:25 +07; LastTaskResult: 0
- No evidence of recurring 2-minute nuisance pattern in current task definition

Gate: `D6G1B_WINDOWS_POPUP_POSTCHECK_PASS`

Raw: see `WINDOWS-TASKS-LIVE.json` in ops temp (copied fields below).

```json
[
  {
    "Name": "MARS_SITE_002_Client_Ops_Producer",
    "State": 1,
    "LastRun": "2026-08-07T13:28:28+07:00",
    "LastResult": 2147946720,
    "NextRun": "2026-08-13T13:00:00+07:00",
    "Actions": "powershell.exe -WindowStyle Hidden -NoProfile -ExecutionPolicy Bypass -File \"X:\\AI MARS STORAGE\\runtime-state\\client-ops-site-002-producer\\tmp\\run-site-002-no-import-watchdog-scheduled.ps1\""
  },
  {
    "Name": "MARS_SITE_002_Import_Completion_Poller",
    "State": 1,
    "LastRun": "2026-08-07T15:34:34+07:00",
    "LastResult": 1,
    "NextRun": "2026-08-13T11:50:50+07:00",
    "Actions": "powershell.exe -NoProfile -ExecutionPolicy Bypass -File \"X:\\AI MARS STORAGE\\runtime-state\\client-ops-site-002-producer\\tmp\\run-site-002-import-completion-poller-scheduled.ps1\""
  },
  {
    "Name": "MARS_SITE_002_Post_1C_Catalog_Monitor",
    "State": 3,
    "LastRun": "2026-08-12T14:25:25+07:00",
    "LastResult": 0,
    "NextRun": "2026-08-13T12:30:30+07:00",
    "Actions": "powershell.exe -NoProfile -ExecutionPolicy Bypass -File \"X:\\AI MARS STORAGE\\runtime-checkouts\\site-002-monitor\\repo\\projects\\ocpilot\\sites\\site-002\\tools\\site-002-post-1c-monitor-runner.ps1\""
  }
]
```
