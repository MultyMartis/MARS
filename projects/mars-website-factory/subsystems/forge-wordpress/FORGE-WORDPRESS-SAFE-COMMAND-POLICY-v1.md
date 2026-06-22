# Forge WordPress — Safe Command Policy v1

**Document type:** Command allowlist policy  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

Aligns with MARS Git rules, [FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md](FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md), and WPilot R0–R5 (Forge stops at R3).

---

## 1. Policy classes

| Class | Meaning |
|-------|---------|
| **AUTO** | Agent/operator may run without extra approval |
| **APPROVAL** | Explicit operator approval before run |
| **DEV-ONLY** | Local/staging target only |
| **WPILOT-ONLY** | Remote scoped operations — not Forge |
| **PROHIBITED** | Never in Forge WordPress surface |

---

## 2. Command classification

| Operation | Class | Notes |
|-----------|-------|-------|
| **Filesystem read** (list, cat, grep) | AUTO | Project scope |
| **File creation in project scope** | AUTO / APPROVAL | New theme files: AUTO; mass refactors: APPROVAL |
| **File deletion** | APPROVAL | Never bulk delete without review |
| **Git status / diff / log** | AUTO | Read-only |
| **Git add / commit** | APPROVAL | Per MARS git rules — human requests commit |
| **Git push** | APPROVAL | Explicit operator |
| **npm install** | APPROVAL | Dependency changes |
| **npm run build / gulp build** | AUTO | R1 |
| **Composer install** | APPROVAL | Lock changes |
| **PHP execution** (lint) | AUTO | `php -l` |
| **PHP execution** (arbitrary) | PROHIBITED | No unscoped scripts |
| **WP-CLI read** (`plugin list`, `option get`, `post list`) | AUTO | R0 |
| **WP-CLI write** (`plugin install`, `theme activate`) | DEV-ONLY + APPROVAL | Local only |
| **Database export** | DEV-ONLY + APPROVAL | Local; dumps to STORAGE |
| **Database import** | DEV-ONLY + APPROVAL | Local reset workflows |
| **search-replace** | DEV-ONLY + APPROVAL | Local URL migration only |
| **Plugin install** | DEV-ONLY + APPROVAL | Plugin register compliance |
| **Plugin activate** | DEV-ONLY + APPROVAL | |
| **Plugin delete** | DEV-ONLY + APPROVAL | |
| **Theme activate** | DEV-ONLY + APPROVAL | |
| **User operations** | DEV-ONLY + APPROVAL | Test users only |
| **Option changes** | DEV-ONLY + APPROVAL | Document in change log |
| **Cache flush** | AUTO | Local DEV only |
| **Production deploy** | PROHIBITED | WPilot / host panel |
| **Remote SSH/FTP** | WPILOT-ONLY | EAR boundary |
| **curl to production admin** | PROHIBITED | |
| **Arbitrary SQL** | PROHIBITED | |

---

## 3. Cursor agent constraints

| Rule | Enforcement |
|------|-------------|
| No production credentials | Never read `local/tokens` into reports |
| No `git push` without request | MARS default |
| No system-wide installs | Operator installs Local/PHP |
| Scoped paths | `workspaces/.../{FP-ID}/`, subsystem docs only unless chartered |

---

## 4. WPilot boundary commands

These are **WPILOT-ONLY** (reference — not Forge):

- `scoped-replace` on DEV
- Backup before apply
- Rollback execution
- Production-targeted REST via WPilot plugin

Forge **prepare_wpilot_handoff** produces artifacts; WPilot **applies**.

---

## Related

- [FORGE-WORDPRESS-COMMAND-AND-OPERATION-MODEL-v1.md](FORGE-WORDPRESS-COMMAND-AND-OPERATION-MODEL-v1.md)
- [projects/wpilot/WPILOT-RISK-CLASSES-v1.md](../../../wpilot/WPILOT-RISK-CLASSES-v1.md)

---

*Safe command policy v1 — human-operated.*
