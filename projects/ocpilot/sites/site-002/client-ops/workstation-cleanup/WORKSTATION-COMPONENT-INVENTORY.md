# SITE-002 — Workstation Component Inventory (read-only)

Captured: 2026-08-25. **No deletes performed.**

Classification vocabulary:

`KEEP_REQUIRED` | `KEEP_OPTIONAL_HYGIENE` | `DELETE_RETIRED` | `DELETE_DUPLICATE` | `KEEP_HISTORICAL_ONLY` | `UNKNOWN_NEEDS_REVIEW`

## Windows Scheduled Tasks

### 1. `\MARS_SITE_002_Import_Completion_Poller`
- **TYPE:** Scheduled Task
- **ENABLED:** Disabled
- **LAST RUN / RESULT:** 2026-08-07 (failed historically)
- **PURPOSE:** Historical Windows completion polling → Client Ops (visible PowerShell era)
- **CURRENT AUTHORITY:** RETIRED
- **DEPENDENCIES:** FTP secrets / terminal visibility (broken path)
- **SAFE TO DELETE?** Yes later, after cleanup charter
- **REASON:** Replaced by server completion dispatcher
- **REPLACED BY:** `mars_1c_completion_dispatch.php` + n8n
- **DELETE PRECONDITIONS:** Server dispatch proven; task remains disabled; no production dependency
- **Classification:** `DELETE_RETIRED`

### 2. `\MARS_SITE_002_Client_Ops_Producer`
- **TYPE:** Scheduled Task
- **ENABLED:** Disabled
- **LAST RUN / RESULT:** 2026-08-07
- **PURPOSE:** Old local Client Ops producer / watchdog-scheduled PS1
- **CURRENT AUTHORITY:** RETIRED
- **DEPENDENCIES:** `X:\AI MARS STORAGE\runtime-state\client-ops-site-002-producer\`
- **SAFE TO DELETE?** Yes later
- **REASON:** Server-side reporting authority
- **REPLACED BY:** server dispatcher + watchdog
- **DELETE PRECONDITIONS:** Confirm no dual-write; server path healthy
- **Classification:** `DELETE_RETIRED`

### 3. `\MARS_SITE_002_Post_1C_Catalog_Monitor`
- **TYPE:** Scheduled Task
- **ENABLED:** Enabled / Ready
- **LAST RUN / RESULT:** 2026-08-25 ~12:30, result 0
- **PURPOSE:** Hidden/noninteractive catalog hygiene monitor (self-hide runner)
- **CURRENT AUTHORITY:** OPTIONAL_HYGIENE (not Client Ops Telegram authority)
- **DEPENDENCIES:** `site-002-post-1c-monitor-runner.ps1` under site tools / runtime-checkout
- **SAFE TO DELETE?** No (this phase); optional later only with hygiene replacement plan
- **REASON:** Still useful hygiene; not production Client Ops
- **REPLACED BY:** N/A for Client Ops; no full replacement required for reporting
- **DELETE PRECONDITIONS:** N/A for DELETE now
- **Classification:** `KEEP_OPTIONAL_HYGIENE`

## Filesystem / harness locations (inventory)

| Path | Type | Authority | Classification |
|------|------|-----------|----------------|
| `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` | Runtime checkout | OPTIONAL_HYGIENE support | `KEEP_OPTIONAL_HYGIENE` / review before delete |
| `X:\AI MARS STORAGE\runtime-checkouts\client-ops-site-002-producer\repo` | Runtime checkout | RETIRED producer | `DELETE_RETIRED` candidate (checkout) |
| `X:\AI MARS STORAGE\runtime-state\client-ops-site-002-producer\` | Locks/logs/tmp | RETIRED state | `DELETE_RETIRED` / `KEEP_HISTORICAL_ONLY` (prefer archive) |
| `X:\AI MARS\projects\ocpilot\sites\site-002\tools\*_poller*.ps1` (if present) | Scripts | RETIRED | `DELETE_RETIRED` or `KEEP_HISTORICAL_ONLY` in Git |
| `X:\AI MARS\projects\ocpilot\sites\site-002\tools\mars_1c_*.php` | Server tool mirrors | AUTHORITATIVE sources | `KEEP_REQUIRED` |
| `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\` | Storage evidence | HISTORICAL_EVIDENCE | `KEEP_HISTORICAL_ONLY` |

Repo script mirrors of retired pollers should remain in Git as **historical evidence** unless a separate docs cleanup removes them; prefer `KEEP_HISTORICAL_ONLY` for committed mirrors, `DELETE_RETIRED` for **live Windows tasks** and **runtime-state** detritus.
