# ISEO-SU WPILOT INSTALL-ONLY EVIDENCE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-PHASE-6A-WPILOT-INSTALL-ONLY  
**Date (UTC evidence):** 2026-07-23 / operator session 2026-07-24  
**Site:** `https://i-seo.su/`  
**Decision:** **PHASE 6A — COMPLETE / WPILOT INSTALLED INACTIVE**

No secrets, credentials, cookies, nonces, or host account identifiers are recorded here.

---

## 1. Installation Status

| Field | Value |
|-------|-------|
| Status | **INSTALLED / INACTIVE** |
| Method | SFTP directory upload only (single method) |
| Plugin folder | `metacode-wpilot/` |
| Main file | `metacode-wpilot/metacode-wpilot.php` |
| Remote file count | **27 / 27** |
| SHA-256 mismatches | **0** |
| Activation | **NOT performed** |
| Rollback used | **No** |

---

## 2. Operator Approvals

| Gate | Approval string | Status |
|------|-----------------|--------|
| 4B-1 | `APPROVE ISEO-SU WPILOT PACKAGE ACCEPTANCE 4B-1` | Present in Phase 6A task charter |
| 4B-2 | `APPROVE ISEO-SU WPILOT COMPATIBILITY ACCEPTANCE 4B-2` | Present in Phase 6A task charter |
| 4B-3 | `CONFIRM ISEO-SU FRESH BEGET BACKUP FOR WPILOT 4B-3` | Present in Phase 6A task charter |
| 6A | Task charter `ISEO-SU-SITE-OPS-PHASE-6A-WPILOT-INSTALL-ONLY` (install-only; no activation) | Executed |

---

## 3. Backup Confirmation

| Field | Value |
|-------|-------|
| Required string | `CONFIRM ISEO-SU FRESH BEGET BACKUP FOR WPILOT 4B-3` |
| Session binding | Attested in **this exact Phase 6A** operator task message |
| Classification | **OPERATOR-ATTESTED** fresh full Beget backup for Phase 6A |
| Panel login by agent | **Not performed** (HOLD) |
| Independent panel timestamp capture | **Not available** to agent (SAFE UNKNOWN residual) |

---

## 4. Package Verification

| Field | Value |
|-------|-------|
| ZIP | `metacode-wpilot-v0.3.0-rc5.zip` |
| Storage path class | `X:\AI MARS STORAGE\wpilot\deploy-packages\` |
| Required SHA-256 | `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577` |
| Recomputed SHA-256 | `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577` |
| Match | **YES** |
| Root folder | exactly `metacode-wpilot/` |
| File count | 27 |
| Main file present | **YES** |
| Traversal / absolute / backslash paths | **NONE** |
| Secret-like entries | **NONE** |
| Nested duplicate plugin dir | **NONE** |
| Stale package used | **NO** (`metacode-wpilot-v0.3.0.zip` rejected) |

---

## 5. Pre-install Plugin Inventory

WordPress root (sanitized): `/home/[REDACTED]/[REDACTED]/i-seo.su/public_html`  
Plugins path (sanitized): `…/public_html/wp-content/plugins`

**Before upload (13 directories):**

- `advanced-custom-fields-pro-main`
- `akismet`
- `cyr2lat`
- `disable-gutenberg`
- `duplicate-page`
- `jetpack`
- `no-category-base-wpml`
- `rate-my-post`
- `simple-user-avatar`
- `wordpress-plugin-autoVersion-master`
- `wordpress-seo`
- `wp-optimize`
- `wp-simple-post-view`

WPilot / ghost matches before upload: **none**  
(`metacode-wpilot`, `metacode-wpilot-old`, `metacode-wpilot-backup`, `metacode-wpilot-v*`, `wpilot`, `wpilot-old` absent)

WordPress Admin plugins list via non-browser HTTP: **not reliably reachable** (no `#adminmenu`; residual Admin automation gap from Phase 2B). No WPilot text mention observed on returned page.

---

## 6. Installation Method

| Field | Value |
|-------|-------|
| Chosen method | **SFTP upload** of extracted `metacode-wpilot/` |
| WP Admin ZIP upload | **Not used** (cannot guarantee Admin automation; SFTP keeps plugin inactive by design) |
| Dual method | **Forbidden / not performed** |
| Local extract | Bounded under Git-ignored `local/sites/iseo-su-production/_phase6a-tmp/` |
| Activate clicked | **No** |

---

## 7. Remote Scope

| Field | Value |
|-------|-------|
| Expected addition | `…/wp-content/plugins/metacode-wpilot/**` only |
| Other production paths intentionally changed | **None** |
| `.htaccess` / `wp-config.php` / theme / static / other plugins | **Untouched** |
| Cache purge | **Not performed** |
| Database login | **Not performed** |

---

## 8. Installed File Inventory

| Check | Result |
|-------|--------|
| Remote file count | 27 |
| Local extract vs ZIP paths | identical set |
| Per-file SHA-256 vs local extract | **0 mismatches** |
| Plugin header name | `MetaCODE WPilot` |
| Plugin header Version field | `0.3.0` (RC5 package; header version string as shipped) |
| Token/secret-like files in folder | **None** |

---

## 9. WordPress Inactive-State Evidence

| Evidence | Result |
|----------|--------|
| Folder present on disk | **YES** |
| Activate action performed | **NO** |
| Public `/wp-json/` namespaces containing `wpilot` | **NONE** (13 namespaces; no WPilot routes) |
| Direct WPilot REST calls (`/wpilot/v1/...`) | **NOT performed** (charter forbid) |
| Admin Plugins row (inactive) | **NOT confirmed via Admin UI** (automation gap) |
| Inactive conclusion | **Filesystem present + not activated + WPilot REST namespace absent ⇒ inactive / not loaded** |

---

## 10. Frontend Regression Check

Representative public GETs **before** and **after** (all HTTP 200; no fatal/maintenance markers; gross render OK):

| Route | Before | After |
|-------|--------|-------|
| `/` | 200 OK | 200 OK |
| `/blog/` | 200 OK | 200 OK |
| `/services.html` | 200 OK | 200 OK |
| `/tariff-calc` | 200 OK | 200 OK |
| `/contacts.html` | 200 OK | 200 OK |

No sitewide crawl performed.

---

## 11. Admin Regression Check

| Check | Result |
|-------|--------|
| Non-browser Admin login automation | Remains unreliable (Phase 2B residual) |
| Settings saves | **None** |
| Plugin updates approved | **None** |
| Other plugins activated/deactivated | **None** |
| Theme changed | **None** |

---

## 12. Activation State

**INACTIVE / NOT ACTIVATED**

No activation hooks intentionally run. No intentional creation of `wpilot_backups` / `wpilot_audit_log`.

---

## 13. Token State

| Item | State |
|------|-------|
| WPilot token | **NOT CREATED** |
| Bridge | **NOT CONFIGURED** |
| Writes | **NOT AUTHORIZED / not enabled** |
| Local token file | **NOT CREATED** |

---

## 14. Rollback Readiness

| Item | State |
|------|-------|
| Exact-folder rollback path | `…/wp-content/plugins/metacode-wpilot/` |
| Rollback used this session | **No** |
| Beget full backup | Operator-attested for Phase 6A (4B-3) |
| Full restore required | **No** (install healthy) |

---

## 15. Deviations

1. WordPress Admin Plugins inactive-row not captured via HTTP client (known challenge/automation gap). Compensated with SFTP inventory + public REST namespace absence.  
2. Plan doc GATE 6A approval string `AUTHORIZE ISEO-SU WPILOT INSTALL-ONLY 6A` was operationalized via the explicit Phase 6A task charter rather than a separately echoed line.  
3. Post-install ghost matcher lists `metacode-wpilot` as the expected folder only — **no duplicate/ghost siblings**.

---

## 16. SAFE UNKNOWN

- Exact Beget panel backup timestamp/object ID (operator-attested; panel not opened by agent).  
- Exact Admin Plugins UI inactive badge (browser HITL).  
- Exact active/inactive matrix for the other 13 plugin directories (unchanged from Phase 2B/4B).  
- Whether any host-side file metadata (owner/mtime) differs from extract in ways not covered by content hash.

---

## 17. Stop Condition

**STOP before activation.**  

Plugin may remain installed only. No token, bridge, write enablement, WPilot REST smoke, database login, cache purge, unrelated production changes, or Git stage/commit/push from this task.

**Next gate (not authorized):** ISEO-SU-SITE-OPS — PHASE 6B WPILOT ACTIVATION-ONLY

---

*Install-only evidence v1 · Phase 6A · 2026-07-24.*
