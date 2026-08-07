# Post_1C Monitor Forensic

## Task

`MARS_SITE_002_Post_1C_Catalog_Monitor`

| Field | Value |
|------|-------|
| State | Ready (ACL prevented Disable) |
| Hidden | False (ACL prevented Settings change) |
| Logon | Interactive (`MetaCODE ONE`) |
| Execute | `powershell.exe` |
| Args (pre) | `-NoProfile -ExecutionPolicy Bypass -File ...site-002-post-1c-monitor-runner.ps1` |
| Trigger | Daily 12:30 +07 |
| Purpose | Local sitemap/catalog hygiene artifacts under `X:\AI MARS STORAGE\...\scheduled-monitors\post-1c` |
| Client Ops delivery | **No** |

## Popup semantics

- Task Scheduler launches interactive `powershell.exe` → console can appear even if child Python uses `CreateNoWindow`
- Prior Hidden/flag edits: Access Denied (task ACL: user Read-only)

## Final home decision

**KEEP_WINDOWS_HIDDEN_NONINTERACTIVE**

Reason: monitor still useful for local sitemap/catalog hygiene; data is local Storage-oriented; migration server-side not low-risk in this narrow phase.

## Mitigation applied

1. Runner script self-hides console via `ShowWindow(GetConsoleWindow(), 0)` at start (runtime checkout + canonical source)
2. Temporary NonInteractive twin created/proven (`popup_observed=false`, LastResult=0) then removed to avoid double-run while old task remains ACL-locked enabled
3. Old task remains enabled (Disable Access Denied) but runner hide addresses visible console nuisance

## Gate honesty

Popup elimination for normal unattended execution: **YES** via runner self-hide (proven process MainWindowHandle=0 on V2 trial; same runner path used by remaining task).
Task XML Hidden flag: still False (ACL).
