# WORKSTATION-CLEANUP-CLOSEOUT — 2026-08-25

**Operation:** `SITE-002-RETIRED-WORKSTATION-COMPONENTS-CLEANUP-01`  
**Site:** SITE-002 / https://bzpm.ru/  
**Canonical knowledge baseline:** `f27ebe80a6ba8252a97fd9003da271a3c2a8551a`  
**Evidence root:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-RETIRED-WORKSTATION-COMPONENTS-CLEANUP-01\`

## Exact removed tasks

| Task | Pre-state | Action |
|------|-----------|--------|
| `\MARS_SITE_002_Import_Completion_Poller` | Disabled / RETIRED | Deleted via `schtasks /Delete /F` |
| `\MARS_SITE_002_Client_Ops_Producer` | Disabled / RETIRED | Deleted via `schtasks /Delete /F` |

Task XML exports retained under evidence `scheduled-task-inventory/raw/`.

## Exact removed paths

| Path | Action |
|------|--------|
| `X:\AI MARS STORAGE\runtime-checkouts\client-ops-site-002-producer\repo` | Removed |
| `X:\AI MARS STORAGE\runtime-checkouts\client-ops-site-002-producer` (dedicated parent) | Removed |
| `X:\AI MARS STORAGE\runtime-state\client-ops-site-002-producer` | Removed (dedicated retired residue) |

## Preserved components

| Component | State |
|-----------|-------|
| `\MARS_SITE_002_Post_1C_Catalog_Monitor` | PRESENT / Enabled / Ready |
| `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` | PRESENT |
| Server Beget import cron / import wrapper / terminal / completion dispatcher | Untouched |
| Server watchdog / gateway | Untouched |
| n8n workflow `tkM4H0G0gM3q9Foi` | Untouched |
| n8n Data Table `H6VYhwz7RXZCBMmu` | Untouched |
| Telegram bot «Монитор bzpm.ru — MetaCODE» | Untouched |
| `CLIENT_OPS_DISPATCH_ENABLED` kill switch | Untouched |

## Unexpected findings

1. Dirty MAIN working tree at local HEAD was **diverged** from `origin/mars/canonical-post-recovery` and lacked `projects/ocpilot/sites/site-002/client-ops/` on disk. Docs closeout used a **clean worktree** from origin tip `f27ebe80`.
2. Retired poller/watchdog/dispatcher script **copies** remain inside the preserved monitor checkout; not scheduled; left in place (KEEP_HISTORICAL within KEEP tree).
3. Neighbor runtime-checkouts (`wpilot-vc-raw-html-p02`, `wpilot-vc-raw-html-p06`) untouched.

## Production mutation count

| Surface | Count |
|---------|------:|
| Server mutations | 0 |
| n8n mutations | 0 |
| Data Table mutations | 0 |
| Telegram sends | 0 |
| Manual imports | 0 |
| Watchdog mutations | 0 |
| Kill-switch changes | 0 |

## Final authority boundary

Normal SITE-002 1C Client Ops reporting remains **server-side authoritative**. The operator workstation is **not** required for production reporting. Optional Post_1C catalog hygiene monitor may continue locally; it is not Client Ops Telegram authority.
