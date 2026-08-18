# Forge WordPress — Post-launch maintenance standard v1

**ID:** FW-RB-13  
**Status:** ACTIVE — OPERATIONS STANDARD  
**Date:** 2026-08-18  

Cadence **classes**, not a fake universal calendar. Hosting/operator contracts set actual dates.

---

## Checklist (rotate by class)

| Item | Class (typical) |
|------|-----------------|
| Backups exist and are restorable | frequent (host) + before HIGH changes |
| WordPress / plugin updates | [FW-RB-10](FORGE-WORDPRESS-PRODUCTION-UPDATE-SOP-v1.md) — not “update all” |
| Security / webroot hygiene | after any deploy; periodic scan for runners/logs |
| Broken links | after content waves / cutover |
| Forms delivery | after SMTP or DNS change; sample submit |
| SSL | after domain/DNS change; expiry watch |
| DNS | after mail/web changes |
| Sitemap / indexability | after public CPT changes |
| Disk / log growth | host; debug.log must not accumulate in webroot |
| Stale admin users | after staff change |
| WPilot state | write still false unless chartered |
| Production drift | hash intake before next code deploy |

---

*FW-RB-13 v1.*
