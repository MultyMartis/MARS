# Forge WordPress — Production update SOP v1

**ID:** FW-RB-10  
**Status:** ACTIVE — OPERATIONS STANDARD  
**Date:** 2026-08-18  

**Do not** click “update all” as an operating standard.

---

## A. Plugins / theme (routine)

1. **Inventory** — [DEPENDENCY-REGISTER](../templates/FORGE-WORDPRESS-DEPENDENCY-REGISTER-TEMPLATE-v1.md) + plugin screen  
2. **Changelog / risk** — breaking PHP, Admin UI, FE assets  
3. **Backup** — proportional ([FW-RB-03](FORGE-WORDPRESS-BACKUP-ROLLBACK-STANDARD-v1.md)); full files+DB before HIGH  
4. **Staging / safe validation** where available  
5. **Exact update scope** — named plugins/versions only  
6. **Smoke** — [REGRESSION-PACK](../standards/FORGE-WORDPRESS-REGRESSION-PACK-v1.md) subset  
7. **Rollback evidence** — previous versions + backup id  

---

## B. WordPress core / PHP

Separate **routine security** (minor WP) from **major-version migration** (WP 6.x→7, PHP 8.1→8.3).

| Step | Routine security | Major migration |
|------|------------------|-----------------|
| Compatibility check | plugin/theme “tested up to” | PHP compatibility + WAD |
| Backup | yes | full files+DB **required** |
| Plugin/theme support | spot-check | block on unknown |
| PHP version | host panel aligned | raise PHP only after plugin PASS |
| Fatal / error log | check after | check after |
| Smoke | Home + Admin + forms | full regression pack |
| Rollback | host backup | documented restore drill |

---

*FW-RB-10 v1.*
