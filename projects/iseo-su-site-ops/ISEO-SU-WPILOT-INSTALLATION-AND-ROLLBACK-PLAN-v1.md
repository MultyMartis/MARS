# ISEO-SU WPILOT INSTALLATION AND ROLLBACK PLAN v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** PHASE 4B (plan) · PHASE 6A (GATE 6A executed) · **PHASE 6B (GATE 6B executed)**  
**Date:** 2026-07-24  
**Status:** GATE 6A **COMPLETE** (installed) · GATE 6B **COMPLETE** — plugin **ACTIVE / SAFE DEFAULTS**; later gates remain plan-only  
**Package:** `metacode-wpilot-v0.3.0-rc5.zip`  
**SHA-256:** `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577`

---

## Principles

1. **Separated gates only** — never combine upload + activation + token + smoke + write.  
2. Bridge and write must remain **off** after activation until a later explicit charter.  
3. Full **Beget backup** is mandatory before any production mutation gate.  
4. Plugin-level backups **do not** replace hosting backup.  
5. Hybrid protected zones remain out of WPilot mutation scope.

---

## GATE 4B-1 — PACKAGE ACCEPTANCE

| Field | Content |
|-------|---------|
| **Inputs** | Package audit; SHA-256; ACCEPTED MATCH evidence |
| **Operator approval string** | `APPROVE ISEO-SU WPILOT PACKAGE ACCEPTANCE 4B-1` |
| **Actions** | Record operator acceptance of exact ZIP + hash |
| **Prohibited** | Upload, activate, token, REST, ZIP rebuild |
| **PASS** | Operator confirms SHA-256 and forbids stale `v0.3.0.zip` |
| **Rollback** | N/A (documentation gate) |
| **Stop** | Any hash mismatch or desire to use non-rc5 ZIP |

---

## GATE 4B-2 — COMPATIBILITY ACCEPTANCE

| Field | Content |
|-------|---------|
| **Inputs** | Compatibility assessment; hybrid boundaries; incomplete PHP/version contract |
| **Operator approval string** | `APPROVE ISEO-SU WPILOT COMPATIBILITY ACCEPTANCE 4B-2` |
| **Actions** | Accept CONDITIONAL GO conditions; accept WPilot page-only scope |
| **Prohibited** | Install; reinterpret static HTML as WPilot targets |
| **PASS** | Operator accepts conditions in compatibility §12 |
| **Rollback** | N/A |
| **Stop** | Operator requires remediation first → Phase 4C |

---

## GATE 4B-3 — BACKUP CONFIRMATION

| Field | Content |
|-------|---------|
| **Inputs** | Fresh full Beget backup proof for the install session |
| **Operator approval string** | `CONFIRM ISEO-SU FRESH BEGET BACKUP FOR WPILOT 4B-3` |
| **Actions** | Operator creates/confirm full backup; record timestamp (no secrets) |
| **Prohibited** | Proceeding to 6A without fresh backup; relying only on plugin backups |
| **PASS** | Operator-attested fresh full backup for this session |
| **Rollback** | Hosting restore path known to operator |
| **Stop** | Backup unavailable or stale relative to session |
| **Phase 6A result** | **PASS** — operator string present in Phase 6A charter |

---

## GATE 6A — PLUGIN UPLOAD / INSTALL ONLY

| Field | Content |
|-------|---------|
| **Inputs** | 4B-1..4B-3 PASS; exact ZIP + SHA-256; SFTP or WP Admin upload charter |
| **Operator approval string** | `AUTHORIZE ISEO-SU WPILOT INSTALL-ONLY 6A` (operationalized via task `ISEO-SU-SITE-OPS-PHASE-6A-WPILOT-INSTALL-ONLY`) |
| **Actions** | Upload/install plugin files to `wp-content/plugins/metacode-wpilot/` only; verify single folder + main file; **do not activate** |
| **Prohibited** | Activation; token; REST authenticated calls; write enable; theme/core changes |
| **PASS** | One folder `metacode-wpilot/`; `metacode-wpilot.php` present; no ghost/stale duplicate; inactive |
| **Rollback** | Delete/rename exact plugin folder via SFTP; confirm plugins list; frontend smoke |
| **Stop** | Duplicate folders, wrong version, upload corruption, unexpected files |
| **Phase 6A result** | **PASS / COMPLETE** — SFTP install; 27/27 files; inactive; evidence in `ISEO-SU-WPILOT-INSTALL-ONLY-EVIDENCE-v1.md` |

### After upload / before activation checklist

- [x] Exactly one `metacode-wpilot` plugin directory  
- [x] Main file present  
- [x] No `metacode-wpilot-v0.3.0` ghost folder  
- [x] Not activated  
- [x] Frontend baseline unchanged  

---

## GATE 6B — ACTIVATION ONLY

| Field | Content |
|-------|---------|
| **Inputs** | 6A PASS; Admin access (prefer browser HITL); backup still valid |
| **Operator approval string** | `APPROVE ISEO-SU WPILOT ACTIVATION 6B` (+ session backup `CONFIRM ISEO-SU FRESH BEGET BACKUP FOR WPILOT 6B`) |
| **Actions** | Activate plugin; confirm bridge off / write off / no token; confirm Admin menu; optional public ping only if chartered |
| **Prohibited** | Token generate; bridge enable; write enable; dry-run/write REST; cache purge unless separate charter |
| **PASS** | Active plugin; defaults safe; frontend OK; Admin reachable |
| **Rollback** | Deactivate in Admin; else SFTP rename/delete plugin folder; DB restore only if tables/options damage proven |
| **Stop** | Fatal error, Admin lockout, frontend breakage, unexpected bridge-on |
| **Phase 6B result** | **PASS / COMPLETE** — active; bridge/writes off; token absent; evidence in `ISEO-SU-WPILOT-ACTIVATION-ONLY-EVIDENCE-v1.md` |

---

## GATE 6C — TOKEN CREATION ONLY

| Field | Content |
|-------|---------|
| **Inputs** | 6B PASS; token storage decision; Admin HITL |
| **Operator approval string** | `APPROVE ISEO-SU WPILOT TOKEN CREATION 6C` (+ fresh Beget backup confirm for 6C) |
| **Actions** | Generate token in Admin; store plaintext **only** in approved local token file; site metadata stores path/reference only |
| **Prohibited** | Pasting token into chat/docs/REPORT/git; enabling write; authenticated smoke beyond later gate; **original 6C also forbade bridge enable** |
| **PASS** | Token hash present in WP; local file created by operator; reference recorded without secret |
| **Rollback** | Revoke token in Admin; delete local token file if required |
| **Stop** | Token exposure; storage path non-canonical |
| **Phase 6C result** | **BLOCKED / NO TOKEN** — WPilot 0.3.0 refuses generate unless DEV confirmed + bridge enabled (`is_operationally_ready`). Live notice observed; bridge/writes left off. Evidence: `ISEO-SU-WPILOT-TOKEN-CREATION-EVIDENCE-v1.md` |
| **Remediation** | **WPilot RC6 packaged** (`can_manage_token`) — see Phase 4C REPORT. Do **not** improvise temporary DEV+bridge under original 6C. Next: **GATE 6C-R** update-only, then 6C retry. |

---

## GATE 6C-R — WPILOT REMEDIATION UPDATE-ONLY (next)

| Field | Content |
|-------|---------|
| **Inputs** | Phase 4C / RC6 package accepted; fresh Beget backup for update session |
| **Package** | `metacode-wpilot-v0.3.0-rc6.zip` |
| **SHA-256** | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| **Actions** | Update **only** the WPilot plugin package; verify version/release label / safe defaults |
| **Prohibited** | Token creation; bridge enable; write enable; REST; unrelated plugin/theme/core changes |
| **PASS** | RC6 installed/active; bridge/writes/`dev_confirmed` remain off; no token; no REST |
| **Rollback** | Restore prior RC5 plugin folder/package from backup; deactivate if needed |
| **Stop** | Hash mismatch; unexpected state change; any token/REST activity |

After 6C-R acceptance: retry **GATE 6C TOKEN CREATION-ONLY** under RC6 semantics (token without bridge).

---

## GATE 6D — NEGATIVE AUTH AND READ-ONLY SMOKE

| Field | Content |
|-------|---------|
| **Inputs** | 6C PASS; bridge/dev_confirmed policy for smoke charter |
| **Operator approval string** | `AUTHORIZE ISEO-SU WPILOT READ-ONLY SMOKE 6D` |
| **Actions** | Negative auth (missing/invalid token); then minimal authorized reads (ping/site-info/themes/plugins/pages as chartered) |
| **Prohibited** | write_enabled; dry-run; backups; rollback; scoped-replace; static file edits |
| **PASS** | Failures fail closed; authorized reads succeed; header forwarding confirmed or documented blocked |
| **Rollback** | Emergency disable / deactivate / revoke token as needed |
| **Stop** | WAF blocks; unexpected public data leak; bridge cannot stay controlled |

---

## GATE 6E — CONTROLLED WRITE SMOKE (later, optional)

| Field | Content |
|-------|---------|
| **Inputs** | Separate charter; unpublished draft WP page; fresh backup; 6D PASS |
| **Operator approval string** | `AUTHORIZE ISEO-SU WPILOT CONTROLLED-WRITE-SMOKE 6E` (future) |
| **Actions** | Explicit dry-run → backup → single scoped replace → rollback on designated page only |
| **Prohibited** | Homepage marketing templates; static HTML; ACF; forms; calculators; theme files |
| **PASS** | Checksums verify; rollback restores; audit rows present |
| **Rollback** | Plugin rollback + Beget restore if needed |
| **Stop** | Any mismatch, multiple matches, or hybrid boundary breach |

**Phase 4B does not authorize GATE 6E.**

---

## Minimum future rollback package (materials)

### Before installation

- Fresh full Beget backup confirmation  
- Exact ZIP + SHA-256  
- Current `wp-content/plugins/` inventory (no WPilot)  
- `active_plugins` evidence obtained safely under charter  
- Frontend screenshots / public smoke baseline  
- REST baseline (`/wp-json/` presence)  
- PHP error-log access plan (SFTP path known from 2B: `wp-content/debug.log` risk-aware)  
- Emergency SFTP deletion path for `wp-content/plugins/metacode-wpilot/`

### Activation rollback order

1. Deactivate via WordPress Admin if available  
2. Else rename/delete exact plugin folder by SFTP  
3. Restore DB only if activation created incompatible damage  
4. Validate frontend + Admin recovery  

GATE 6A rollback path remains ready but was **not** needed (install validated).  
GATE 6B Admin deactivate / SFTP rename rollback paths remain ready; **not** needed (activation validated with safe defaults).  
**Do not** execute GATE 6C+ without separate operator approval.

---

*Installation and rollback plan v1 · updated Phase 4C / RC6 remediation 2026-07-24 · GATE 6B complete; 6C blocked; 6C-R next.*
