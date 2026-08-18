# Forge WordPress — Change and release management standard v1

**ID:** FW-S-41  
**Status:** ACTIVE — OPERATIONS STANDARD  
**Date:** 2026-08-18  
**Evidence:** FP-0002 production waves (P07–P17); P14 baseline; not every typo is a charter

---

## 1. Change classes

| Class | Examples | Evidence |
|-------|----------|----------|
| **LOW** | Copy typo in a template string; CSS 2px; help text | Before/after screenshot or SHA; smoke the route |
| **MEDIUM** | New field; component behavior; plugin patch | Backup proportional; staging/safe check if available; QA pack subset; report |
| **HIGH** | CPT change; URL; forms; SEO owner; cache plugin; PHP | Full files+DB backup; written scope; rollback SHA; regression pack; acceptance |
| **CUTOVER** | Domain, NS, SSL, indexing, SMTP, home/siteurl | [LAUNCH SOP](../runbooks/FORGE-WORDPRESS-PRE-CUTOVER-AND-LAUNCH-SOP-v1.md) |

Every **MEDIUM+** change has: scope · before state · backup/rollback proportional to risk · implementation · QA · parity · acceptance · report/checkpoint.

LOW does not need a giant charter. CUTOVER always does.

---

## 2. Versioning (runtime truth)

Dashboard / system widget should expose enough to diagnose **what is deployed**:

| Signal | Rule |
|--------|------|
| Functionality plugin version | From plugin header / constant **in the deployed file** |
| Theme version | `style.css` Version header |
| Production wave / baseline id | named (e.g. P14) when used |
| Git SHA | only if actually recorded at deploy; **never invent** |
| WPilot plugin file vs option | do not treat option as file truth ([FW-RB-09](../runbooks/FORGE-WORDPRESS-WPILOT-PRODUCTION-STANDARD-v1.md)) |

**Avoid fake version values** not tied to runtime code.

---

## 3. Production baseline

A **baseline** is a known accepted state with:

- source hash / parity for product code  
- runtime identity (`WP_ENVIRONMENT_TYPE`, host, `home`/`siteurl`)  
- DB/content state reference (backup id)  
- Git SHA of the **canonical** checkpoint that matches deployed allowlist (or explicit drift note)  
- accepted open tails  

Take a baseline **before** major migration/cutover (P14-class). See [BACKUP](../runbooks/FORGE-WORDPRESS-BACKUP-ROLLBACK-STANDARD-v1.md).

---

*FW-S-41 v1.*
