# Visible PowerShell Forensic

## Proven source of regular visible console

**Task:** `\MARS_SITE_002_Import_Completion_Poller`

| Field | Value |
|------|-------|
| Trigger | Daily 11:50 +07, repeat every 2 minutes for 3 hours |
| Execute | `powershell.exe` |
| Arguments | `-NoProfile -ExecutionPolicy Bypass -File "...\run-site-002-import-completion-poller-scheduled.ps1"` |
| Nested | wrapper script launches another `powershell.exe` for the poller |
| Hidden setting | `False` |
| Logon | Interactive (`MetaCODE ONE`) |
| LastTaskResult today | `1` |
| Failure mode | `site-002-d6g-fetch-pending-terminals.py` could not parse PRODUCTION FTP fields (`Missing FTP fields`) |

This matches the operator report of a PowerShell window appearing regularly and vanishing quickly.

## Inventory

| task name | trigger | action | frequency | visible-console risk | last run (local) | last result | current necessity | final action |
|-----------|---------|--------|-----------|----------------------|------------------|-------------|-------------------|--------------|
| MARS_SITE_002_Import_Completion_Poller | 11:50+07 PT2M/3H | powershell poller | ~2 min in window | HIGH | 2026-08-07 15:34+07 | 1 | none after server dispatch | DISABLED_AND_RETIRED |
| MARS_SITE_002_Client_Ops_Producer | 13:00 daily | powershell → node watchdog | daily | medium | 2026-08-07 13:28+07 | 0x800710E0 / later functional | replaced by server watchdog | DISABLED (server-side primary) |
| MARS_SITE_002_Post_1C_Catalog_Monitor | 12:30+07 daily | powershell monitor | daily | residual (Hidden change access-denied) | 2026-08-07 13:28+07 | 0 | sitemap/catalog hygiene only | remains enabled |

## Gate

`D6G1_VISIBLE_POWERSHELL_SOURCE_PROVEN`
