# Forge WordPress — Environment / Migration Standard v1

**ID:** FW-RB-05  
**Status:** ACTIVE  
**Date:** 2026-08-18  
**Class:** D  
**Evidence:** FP-0002 P15 (closes deferred P06 residue)

---

## Common residue (scan before pre-cutover)

| Residue | Action |
|---------|--------|
| `WP_ENVIRONMENT_TYPE=local` on live | Set `production` |
| `WP_DEBUG` / display | Off on production |
| `.test` URLs in content/options/HTML | Replace with current public host, then final host at cutover |
| `localhost` links | Remove |
| Staging host leftovers | Classify |
| Local mail suppression still labeled “local” | Reclassify PRE-CUTOVER; keep until SMTP |
| Old runtime notices / LOCAL MARS | Remove (AP-005) |
| Demo artifacts / lorem | Remove (AP-009) |
| Public debug.log | Archive off-webroot + truncate/remove |
| Migration scripts in webroot | [HYGIENE](../standards/FORGE-WORDPRESS-PUBLIC-WEBROOT-HYGIENE-GATE-v1.md) |
| Bootstrap admin users `@localhost.test` | Remove/replace |

---

## Checklist (print into the migration report)

- [ ] Environment type correct  
- [ ] Debug off  
- [ ] No live `.test` / localhost in HTML  
- [ ] Mail suppress owner documented  
- [ ] Indexing still closed if not final domain  
- [ ] home/siteurl match intended **current** host  
- [ ] Webroot hygiene PASS  
- [ ] Users CLEAN  

---

*FW-RB-05 v1.*
