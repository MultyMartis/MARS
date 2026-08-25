# WORKSTATION-CLEANUP-MANIFEST — Pro: BZPM Production

**Status:** CLOSED — executed by `SITE-002-RETIRED-WORKSTATION-COMPONENTS-CLEANUP-01`  
**Cleanup date:** 2026-08-25  
**Evidence:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-RETIRED-WORKSTATION-COMPONENTS-CLEANUP-01\`  
**Closeout:** [WORKSTATION-CLEANUP-CLOSEOUT-2026-08-25.md](WORKSTATION-CLEANUP-CLOSEOUT-2026-08-25.md)

## Counts (post-cleanup)

- **REMOVED = 2** Windows Scheduled Tasks + producer runtime checkout + dedicated runtime-state
- **KEEP = 1** primary (Post_1C task) + server tool mirrors + this knowledge pack
- **UNKNOWN = 0** for named production tasks

## REMOVED (was DELETE candidates)

### D1 — `\MARS_SITE_002_Import_Completion_Poller`
- **Post-cleanup state:** REMOVED (task no longer exists)
- Pre-delete: Disabled / non-authoritative
- Authoritative replacement: server `mars_1c_completion_dispatch.php` → n8n → Telegram
- XML export retained in cleanup evidence `scheduled-task-inventory/raw/`

### D2 — `\MARS_SITE_002_Client_Ops_Producer`
- **Post-cleanup state:** REMOVED (task no longer exists)
- Pre-delete: Disabled / non-authoritative
- Authoritative replacement: server dispatcher + server watchdog
- XML export retained in cleanup evidence `scheduled-task-inventory/raw/`

### D3 — producer runtime-checkout / runtime-state under STORAGE
- **Removed path:** `X:\AI MARS STORAGE\runtime-checkouts\client-ops-site-002-producer\repo` (parent directory also removed; dedicated)
- **Removed residue:** `X:\AI MARS STORAGE\runtime-state\client-ops-site-002-producer\`
- Reference forensic: no enabled Scheduled Task / service / process dependency after D1/D2 removal
- Historical textual references remain in Git evidence (KEEP_HISTORICAL) — not live runtime

## KEEP (unchanged)

### K1 — `\MARS_SITE_002_Post_1C_Catalog_Monitor`
- Classification: `KEEP_OPTIONAL_HYGIENE`
- Decision: `POST_1C_MONITOR_KEEP_OPTIONAL_HYGIENE`
- **Post-cleanup state:** PRESENT / Enabled / Ready (preserved)
- Associated checkout: `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` — PRESERVED

### K2 — Server-side Beget crons, PHP tools, n8n workflow, Data Table, Telegram bot
- Never part of workstation delete scope
- **Mutations this wave:** 0

### K3 — This `client-ops/` knowledge pack + D6G evidence
- Keep

## Unexpected residue

- Retired poller/watchdog/dispatcher PS1 **copies** remain inside the preserved `site-002-monitor` checkout (historical mirrors; not scheduled). Left in place to avoid touching the KEEP monitor tree.
- No unexpected extra Windows Scheduled Tasks matching SITE-002 / Client Ops terms.

## Post-cleanup workstation state

- Local Client Ops producer / completion poller: **gone**
- Optional Post_1C hygiene monitor: **preserved**
- Production Client Ops authority: **server-side only** (workstation not required)
