# ISEO-SU WPILOT ACTIVATION-ONLY EVIDENCE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-PHASE-6B-WPILOT-ACTIVATION-ONLY  
**Date:** 2026-07-24  
**Site:** `https://i-seo.su/`  
**Decision:** **PHASE 6B — COMPLETE / WPILOT ACTIVE SAFE DEFAULTS**

No secrets, credentials, cookies, nonces, plaintext tokens, or host account identifiers are recorded here.

---

## 1. Activation Status

| Field | Value |
|-------|-------|
| Status | **ACTIVE / SAFE DEFAULTS** |
| Method | WordPress Admin (Playwright headless Chromium; Beget JS cookie gate) |
| Plugin | MetaCODE WPilot |
| Plugin file | `metacode-wpilot/metacode-wpilot.php` |
| Version | **0.3.0** |
| Bulk actions | **Not used** |
| Other plugins activated/deactivated | **None** |
| Rollback used | **No** |

---

## 2. Operator Approval

| Gate | Approval string | Status |
|------|-----------------|--------|
| 6B activation | `APPROVE ISEO-SU WPILOT ACTIVATION 6B` | Present in Phase 6B task charter |
| Task charter | `ISEO-SU-SITE-OPS-PHASE-6B-WPILOT-ACTIVATION-ONLY` | Executed |

---

## 3. Backup Confirmation

| Field | Value |
|-------|-------|
| Required string | `CONFIRM ISEO-SU FRESH BEGET BACKUP FOR WPILOT 6B` |
| Session binding | Attested in **this exact Phase 6B** operator task message |
| Classification | **OPERATOR-ATTESTED** fresh full Beget backup for Phase 6B |
| Panel login by agent | **Not performed** (HOLD) |
| Independent panel timestamp capture | **SAFE UNKNOWN** residual |

---

## 4. Pre-activation State

| Check | Result |
|-------|--------|
| Phase 6A evidence | Accepted: installed inactive; 27/27; SHA-256 match; version 0.3.0 |
| SFTP plugin path | `wp-content/plugins/metacode-wpilot/metacode-wpilot.php` |
| Remote file count | **27** |
| Header version | **0.3.0** / Plugin Name MetaCODE WPilot |
| Duplicate WPilot folders | **None** (exactly one `metacode-wpilot`) |
| Plugin Admin state before | **inactive** (Plugins screen row classes `inactive`; Activate link present) |
| Local token file `wpilot-prod-iseo-su.token` | **Absent** |
| Public `wpilot` REST namespace before | **Absent** |
| Bridge / writes / token config | **Not performed** pre-activation |
| Frontend baseline `/`, `/blog/`, `/services.html`, `/tariff-calc`, `/contacts.html` | All **HTTP 200 / gross OK / no fatal / no maintenance** |
| Plugins screen | Loaded with `#adminmenu` after Admin login |

---

## 5. Activation Action

| Field | Value |
|-------|-------|
| Action | Clicked **Activate** only on `metacode-wpilot/metacode-wpilot.php` |
| Bulk activate | **No** |
| Settings saved during activation | **No** |
| Token generate clicked | **No** |
| Bridge enable clicked | **No** |
| Write enable clicked | **No** |

---

## 6. Plugin Active-State Evidence

| Check | Result |
|-------|--------|
| Plugins row after | `active`; Deactivate link present; Activate link absent |
| Display name | MetaCODE WPilot |
| Version line | Версия 0.3.0 \| Автор: MetaCODE |
| Newly active plugin files | only `metacode-wpilot/metacode-wpilot.php` |
| Other plugin active-set delta | **None** |
| PHP fatal / white screen | **Not observed** |
| Admin reachable after | **Yes** (`#adminmenu` present) |
| Public REST namespace after | `wpilot/v1` **registered** (passive `/wp-json/` index only) |
| WPilot route invocation | **None** (ping **not** called) |

---

## 7. Safe Defaults

Read-only inspection of `admin.php?page=metacode-wpilot` (no form submit).

| Visible label / status | Observed value |
|------------------------|----------------|
| Notice | Только DEV/test. Не включайте мост на production. |
| Overview — Мост | выключено |
| Overview — Готовность к записи | выключено |
| Overview — Подтверждение DEV | не подтверждено |
| Security — Мост включён | выключено |
| Security — Запись включена | выключено |
| Security — DEV/test подтверждён | не подтверждено |
| Security — Аварийное отключение | нет |
| Connection — Статус токена | не сгенерирован |
| Diagnostics — Состояние плагина | `disabled` |
| Diagnostics — schema valid | да |
| Diagnostics — Токен создан (UTC) | — |
| Diagnostics note | Browser automation / background jobs / autonomous behavior **not** part of this plugin |

No checkbox/field/token control was changed. No Save/Generate clicked.

---

## 8. Token State

| Surface | State |
|---------|-------|
| Local canonical path | `X:\AI MARS\local\tokens\wpilot-prod-iseo-su.token` — **NOT CREATED** |
| Admin token status | **не сгенерирован** |
| Token created UTC | — |
| Plaintext token in UI | **Not observed** |
| Token creation this phase | **NOT PERFORMED** |

---

## 9. Bridge State

| Surface | State |
|---------|-------|
| Bridge | **DISABLED** (`выключено`) |
| Auto-enable on activation | **No** |
| Bridge toggle clicked | **No** |

---

## 10. Write State

| Surface | State |
|---------|-------|
| Write readiness | **DISABLED** (`выключено`) |
| Auto-enable on activation | **No** |
| Write toggle clicked | **No** |

---

## 11. Activation Side Effects

| Effect | Classification |
|--------|----------------|
| Plugin options/defaults forced safe on activate | **Expected** (source: `WPilot_Settings::activate`) |
| Admin menu MetaCODE WPilot | **Present** |
| Public REST namespace `wpilot/v1` | **Registered** (passive index) |
| Frontend output injection | **Not observed** on representative routes |
| Unrelated plugin/theme/static/settings changes | **Not observed** |
| Cache purge | **Not performed** |
| Cron / background jobs from plugin | Admin diagnostics state no autonomous/background behavior in plugin |
| Settings form saves | **None** |

---

## 12. Frontend Regression

| URL | Status | Gross | Fatal | Maintenance | Visible WPilot output |
|-----|--------|-------|-------|-------------|------------------------|
| `/` | 200 | OK | No | No | No |
| `/blog/` | 200 | OK | No | No | No |
| `/services.html` | 200 | OK | No | No | No |
| `/tariff-calc` | 200 | OK | No | No | No |
| `/contacts.html` | 200 | OK | No | No | No |

---

## 13. Admin Regression

| Check | Result |
|-------|--------|
| wp-admin login (MARS account) | OK |
| Plugins screen | OK |
| WPilot settings screen | OK |
| Fatal / white screen | Not observed |

---

## 14. Database Effect Classification

| Object | Classification |
|--------|----------------|
| `{prefix}wpilot_backups` | **SAFE UNKNOWN** (no DB login; source expects creation on activate) |
| `{prefix}wpilot_audit_log` | **SAFE UNKNOWN** (no DB login; source expects creation on activate) |
| option `wpilot_options` | **EXPECTED CREATED/UPDATED BY ACTIVATION** (source-defined; Admin schema valid = да) |
| Direct phpMyAdmin / DB login | **Not performed** |

---

## 15. Rollback Readiness

| Method | Ready |
|--------|-------|
| Preferred: Deactivate in WP Admin | **Ready** (Deactivate link present) |
| Fallback: SFTP rename `metacode-wpilot/` → `metacode-wpilot.disabled-phase6b/` | **Ready** (not used) |
| Full Beget restore | Reserved for broader damage only |
| Used this session | **No** |

---

## 16. Deviations

1. Non-browser `requests` Admin login is blocked by Beget JS cookie gate (`beget=begetok`); activation used Playwright (authorized Admin login path).  
2. Public `wpilot/v1` namespace appears after activation (expected). **No route was invoked.**  
3. Install/rollback plan historical string `AUTHORIZE ISEO-SU WPILOT ACTIVATION-ONLY 6B` superseded for this session by charter strings `APPROVE ISEO-SU WPILOT ACTIVATION 6B` + backup `CONFIRM ISEO-SU FRESH BEGET BACKUP FOR WPILOT 6B`.

---

## 17. SAFE UNKNOWN

- Exact Beget backup panel object/timestamp for Phase 6B (operator-attested only).  
- Exact MySQL table physical existence without DB access.  
- PHP runtime version (unchanged).  
- Full historical active-plugin matrix beyond pre/post active-file sets captured this session.  
- Whether host forwards `X-WPilot-Token` (GATE 6D).

---

## 18. Stop Condition

At end of Phase 6B:

- plugin **may be active** — **is active**;  
- bridge **disabled**;  
- writes **disabled**;  
- token **not created**;  
- no WPilot route invocation;  
- no REST smoke;  
- no database login;  
- no cache purge;  
- no unrelated production changes;  
- no Git stage/commit/push;  
- wait for operator review.

Next gate (not authorized): **PHASE 6C WPILOT TOKEN CREATION-ONLY**.

---

*ISEO-SU WPilot activation-only evidence v1 · 2026-07-24 · PHASE 6B COMPLETE / ACTIVE SAFE DEFAULTS.*
