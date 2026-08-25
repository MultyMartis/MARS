# WORKSTATION-CLEANUP-MANIFEST — Pro: BZPM Production

**Input for a later controlled cleanup task. Do NOT delete in this phase.**

## Counts

- **DELETE candidates = 2** (Windows tasks) + related runtime producer checkout/state (see notes)
- **KEEP = 1** primary (Post_1C task) + server tool mirrors + this knowledge pack
- **UNKNOWN = 0** for named production tasks (filesystem detritus may need spot review at cleanup time)

## DELETE CANDIDATES

### D1 — `\MARS_SITE_002_Import_Completion_Poller`
- Disabled / non-authoritative: YES
- Authoritative replacement: server `mars_1c_completion_dispatch.php` → n8n → Telegram
- No production dependency: YES (reporting server-side)
- Safe removal validation: after delete, next scheduled/admin import still delivers Telegram without workstation

### D2 — `\MARS_SITE_002_Client_Ops_Producer`
- Disabled / non-authoritative: YES
- Authoritative replacement: server dispatcher + server watchdog
- No production dependency: YES
- Safe removal validation: watchdog + import alerts still work; no local producer process

### D3 (optional filesystem) — producer runtime-checkout / runtime-state under STORAGE
- Only after D2 task removal validated
- Prefer archive to `KEEP_HISTORICAL_ONLY` before purge
- Exact path list required in destructive charter

## KEEP

### K1 — `\MARS_SITE_002_Post_1C_Catalog_Monitor`
- Classification: `KEEP_OPTIONAL_HYGIENE`
- Decision: `POST_1C_MONITOR_KEEP_OPTIONAL_HYGIENE`

### K2 — Server-side Beget crons, PHP tools, n8n workflow, Data Table, Telegram bot
- Never part of workstation delete scope

### K3 — This `client-ops/` knowledge pack + D6G evidence
- Keep

## UNKNOWN

None for the three named Scheduled Tasks as of 2026-08-25 inventory.  
If cleanup discovers additional `*SITE*002*1C*` tasks, classify before delete.

## Cleanup charter must include

- Exact path/task list
- Dry-run
- Path validation
- Checkpoint/backup
- Explicit operator approval
- Post-action audit
