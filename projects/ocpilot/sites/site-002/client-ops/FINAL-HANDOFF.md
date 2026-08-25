# SITE-002 / BZPM — Final Handoff (1C Import + Client Ops)

**Status:** CANONICAL start-here for the accepted server-side Client Ops generation  
**Site:** SITE-002 · https://bzpm.ru/ · ocStore / OpenCart 3.0.3.9  
**Captured:** 2026-08-25  
**Authority:** this pack + D6G/D6G1/D6G1A/D6G1B evidence under `projects/client-ops-reporting-bridge/`

---

## If this Web-GPT conversation disappears — start here

1. Read this file.
2. Read [MASTER-OVERVIEW.md](MASTER-OVERVIEW.md).
3. Read [DOC-AUTHORITY-HIERARCHY.md](DOC-AUTHORITY-HIERARCHY.md).
4. Operate from [RUNTIME-AUTHORITY-MAP.md](RUNTIME-AUTHORITY-MAP.md) — **server-side is production authority**.
5. Do **not** enable retired Windows poller/producer tasks.
6. Do **not** delete workstation components until the cleanup manifest is executed in a separate charter.

---

## Canonical map (absolute paths)

| Topic | Path |
|-------|------|
| Master overview | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\MASTER-OVERVIEW.md` |
| Current architecture | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\CURRENT-PRODUCTION-ARCHITECTURE.md` |
| Runtime authority | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\RUNTIME-AUTHORITY-MAP.md` |
| 1C import contract | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\1C-IMPORT-CONTRACT.md` |
| Offers input state | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\OFFERS-INPUT-CURRENT-STATE.md` |
| Terminal / event model | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\TERMINAL-EVENT-MODEL.md` |
| Telegram contract | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\TELEGRAM-PRODUCT-CONTRACT.md` |
| Dedupe / delivery | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\DEDUPE-DELIVERY-CONTRACT.md` |
| Kill switch | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\KILL-SWITCH-CONTRACT.md` |
| Watchdog | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\WATCHDOG-CONTRACT.md` |
| Admin manual import | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\ADMIN-IMPORT-CONTRACT.md` |
| Concurrency | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\CONCURRENCY-MODEL.md` |
| Lessons learned | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\LESSONS-LEARNED.md` |
| Anti-patterns | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\ANTI-PATTERNS.md` |
| Reproduction playbook | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\REPRODUCE-1C-CLIENT-OPS-FOR-NEW-SITE.md` |
| Checklists | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\checklists\` |
| Runbooks | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\runbooks\` |
| Recovery | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\recovery\RECOVERY-GUIDE.md` |
| Current backend | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\CURRENT-STATE-BACKEND.md` |
| DB-first blueprint | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\DB-FIRST-SUCCESSOR-BLUEPRINT.md` |
| DB migration roadmap | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\DB-MIGRATION-ROADMAP.md` |
| Neutral template | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\PROJECT-NEUTRAL-CLIENT-OPS-TEMPLATE.md` |
| Agent brain | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\AGENT-BRAIN.md` |
| Workstation inventory | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\workstation-cleanup\WORKSTATION-COMPONENT-INVENTORY.md` |
| Cleanup manifest | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\workstation-cleanup\WORKSTATION-CLEANUP-MANIFEST.md` |
| Post_1C decision | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\workstation-cleanup\POST-1C-MONITOR-DECISION.md` |
| Deep research backlog | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\DEEP-RESEARCH-BACKLOG.md` |
| Knowledge inventory | `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\KNOWLEDGE-INVENTORY.md` |

### Stable evidence (do not rewrite as current truth)

| Evidence | Path |
|----------|------|
| D6G event-driven import | `X:\AI MARS\projects\client-ops-reporting-bridge\PHASE-1B-D6G-EVENT-DRIVEN-1C-IMPORT-REPORTING-AND-ADMIN-MANUAL-TRIGGER.md` |
| D6G1 server dispatch | `X:\AI MARS\projects\client-ops-reporting-bridge\PHASE-1B-D6G1-SCHEDULED-SILENCE-FORENSIC-SERVER-SIDE-DISPATCH-AND-WINDOWS-POLLER-REMOVAL.md` |
| D6G1A kill switch / hygiene | `X:\AI MARS\projects\client-ops-reporting-bridge\PHASE-1B-D6G1A-SERVER-WATCHDOG-SCHEDULING-WINDOWS-HYGIENE-AND-DISPATCH-KILL-SWITCH.md` |
| D6G1B natural acceptance | `X:\AI MARS\projects\client-ops-reporting-bridge\PHASE-1B-D6G1B-BEGET-WATCHDOG-CRON-VERIFICATION-AND-NATURAL-SCHEDULED-ACCEPTANCE.md` |
| Production readiness flags | `X:\AI MARS\projects\client-ops-reporting-bridge\evidence\phase-1b-d6g1b-watchdog-cron-and-natural-acceptance\PRODUCTION-READINESS.md` |
| Server tool sources | `X:\AI MARS\projects\ocpilot\sites\site-002\tools\mars_1c_*.php` |
| Storage terminals / monitors | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\` |

---

## One-paragraph truth

Normal SITE-002 1C Client Ops reporting is **server-side**: Beget import cron → `mars_1c_import_wrapper.php` → terminal → `mars_1c_completion_dispatch.php` → n8n workflow `tkM4H0G0gM3q9Foi` → Data Table `H6VYhwz7RXZCBMmu` → Telegram bot «Монитор bzpm.ru — MetaCODE». Operator workstation is **not** required for production reporting. Windows completion poller and old local producer are **retired**. Post_1C catalog monitor remains **optional hygiene** only.

---

## Next separate tasks (do not auto-start)

1. Controlled workstation cleanup from `workstation-cleanup/WORKSTATION-CLEANUP-MANIFEST.md` in `Pro: BZPM Production`.
2. Optional deep-research phase from `DEEP-RESEARCH-BACKLOG.md`.
3. Optional D6G2 offers-input root-cause forensic (still open at responsibility-boundary level).
