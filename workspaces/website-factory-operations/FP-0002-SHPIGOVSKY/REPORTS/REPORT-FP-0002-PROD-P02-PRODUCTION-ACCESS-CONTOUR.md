# REPORT — FP-0002 PROD-P02 Production Access Contour

**Wave:** PROD-P02  
**Date:** 2026-08-13  
**Locus:** `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/`  
**Mode:** Access structure / credential storage / connection configuration preparation / MARS operational ownership  
**Connection:** **NOT AUTHORIZED** — no production contact this wave

```text
FP-0002 PRODUCTION ACCESS CONTOUR CREATED — OPERATOR CREDENTIAL ENTRY READY — NO PRODUCTION MUTATIONS PERFORMED
```

---

## 1. Status

| Item | Result |
|------|--------|
| Wave | **PASS** — contour created; operator credential entry ready |
| Production writes | **0** |
| DB writes | **0** |
| WP Admin writes | **0** |
| Filesystem writes (remote) | **0** |
| DNS / SSL | **0** |
| WPilot install / token / write | **0** |
| Commit / push | **0** |
| Staging of this wave | **0** |

Preflight: cwd `X:\AI MARS`; volume **AI WS**; branch `mars/canonical-post-recovery`. Foreign staged WIP under `projects/client-ops-reporting-bridge/` and other uncommitted FP-0002 product files — **untouched**. HEAD ≠ origin (pre-existing); not reconciled.

---

## 2. Precedents Reviewed

| Programme | What was used |
|-----------|----------------|
| Polygon `projects/polygon-ws-ru-site-ops/` | OPERATIONAL-INDEX; Connection Profile; Access Model; Playbook; Backup/Rollback; Protected Zones; Phase 2B0 local contour + FIX01 i-seo template alignment; P13 closeout |
| i-seo `projects/iseo-su-site-ops/` | Local Access Model; Setup Guide; Access Classification; Phase 2A bootstrap (canonical `site-profile.json` + `secrets.local.md` field names) |
| metallka `projects/metallka-ru-site-ops/` | Phase 2B0 bootstrap; Access Model; WPilot token local storage plan (`wpilot-prod-<slug>.token`) |
| WPilot `projects/wpilot/` | OPERATIONAL-INDEX; `local-storage-policy.md`; token root `local/tokens/`; FP-0002 reserved prod path already in P01 readiness |
| MARS local | Directory names under `local/sites/` and `local/tokens/` (filenames only). Other-site secret **values were not copied, printed, or summarized** |

---

## 3. Canonical Secret Model

Verified from repo + local structure (most recent aligned production Site Ops template = i-seo → Polygon FIX01; Database class later used on Polygon/metallka and required here):

| Element | Canonical |
|---------|-----------|
| Root | `X:\AI MARS\local\sites\<site-alias>\` |
| Site alias | hyphenated, `*-production` |
| Non-secret metadata | `site-profile.json` |
| Operator secrets | `secrets.local.md` (snake_case field names) |
| WPilot token | **separate** file `X:\AI MARS\local\tokens\wpilot-prod-<slug>.token` (plaintext token only; not in `secrets.local.md`) |
| `.env` for site ops | **Not** the Site Ops credential format (global `.env` ignore exists; unused here) |
| Ignore | root `.gitignore` line 13: `/local/` |
| Runtime loading | Operator/Cursor reads local files when a later gate authorizes connection; no MARS secret vault product |

Shpigovsky slug: **`shpigovsky-production`**.  
Reserved token: **`wpilot-prod-shpigovsky.token`** (matches P01 readiness; not `wpilot-prod-shpigovsky-ru.token`).

Beget panel password: **optional** (Polygon: FTP + WP Admin + DB/PMA sufficient; least privilege).

---

## 4. Shpigovsky Local Access Contour

Created (gitignored; **no values in this REPORT**):

| Path | Role |
|------|------|
| `X:\AI MARS\local\sites\shpigovsky-production\` | Local-only root |
| `X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md` | **ONE operator fill file** (`<OPERATOR_FILL>` placeholders) |
| `X:\AI MARS\local\sites\shpigovsky-production\site-profile.json` | Non-secret metadata + path refs |

**Not created:** `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token` (no fake token).

`git check-ignore -v` → `.gitignore:13:/local/` for secrets, profile, and reserved token path.  
`git ls-files` for the contour: **empty**.  
`git status --ignored`: `!! local/`.

---

## 5. Credentials Required

| Class | Fill now? | Notes |
|-------|-----------|-------|
| Hosting / Beget panel | **Optional** | Least privilege: site FTP/SFTP is enough. Master Beget password not required |
| Filesystem FTP/SFTP | **YES** | Protocol/host/port unknown until operator copies Beget card — not guessed |
| Filesystem SSH | Optional | Fill only if Beget SSH exists |
| Database | **YES** | READ-ONLY until mutation charter. Prefix: verify on Beget (do not assume `fp02_`) |
| WordPress Admin | **YES** | Do not create a user; do not login this wave |
| WPilot token | **NO** (later reconcile) | Reserved path only. Do not reuse `wpilot-local-shpigovsky.token` |
| SMTP / analytics / CRM / webhooks | **NO** | Optional future section; leave `<OPERATOR_FILL>` |

---

## 6. Credential Reference Map

Tracked (no secrets):  
`DOCS/PRODUCTION/FP-0002-CREDENTIAL-REFERENCE-MAP-v1.md`

Status now: Beget/FS/DB/WP Admin = `OPERATOR_FILL_REQUIRED`; WPilot token = `MISSING`; SMTP = do not fill now.

---

## 7. Production Access Matrix

Tracked: `DOCS/PRODUCTION/FP-0002-PRODUCTION-ACCESS-MATRIX-v1.md`

| Surface | Read | Write |
|---------|------|-------|
| Public HTTP | allowed (P01 proven) | n/a |
| WPilot | pending after token reconcile | **disabled** |
| Filesystem | after credential validation | **disabled** until exact-file charter |
| DB | after validation | **disabled** |
| WP Admin | inspection after credentials present | **task-specific only** |
| Beget panel | operator/manual | operator/manual; not agent default |
| DNS | n/a | **forbidden** until cutover |
| SMTP / cache / logs | unknown / observe | **denied** by default |

---

## 8. MARS Agent/System Responsibility

Tracked: `DOCS/PRODUCTION/FP-0002-AGENT-SYSTEM-RESPONSIBILITY-MAP-v1.md`

| System | Role |
|--------|------|
| **FP-0002 Site Ops** | Production state, passport, matrix, zones, reconciliation, deploy scopes |
| **WPilot** | REST inspect / bounded entity ops / auth gates / operation backups. Not FS/hosting/DNS/unrestricted DB |
| **Forge / AG-WP-001** | Methodology only. **NOT RUNTIME-ACTIVE**. Not production owner |
| **ROL** | Charter docs only — **not** a live connector |
| **EAR** | Skeleton/mock — **not** a live SFTP/DB connector |
| **FS/DB tooling** | Operator / Cursor tool-mediated site ops |
| **Runtime checkout** | Deferred clean path (below) |
| **Operator** | Fill local secrets; Beget HITL; backup confirm; never paste secrets into chat |

---

## 9. Production Connection Profile

| Field | Value |
|-------|-------|
| Path | `DOCS/PRODUCTION/FP-0002-MARS-PRODUCTION-CONNECTION-PROFILE-v1.md` |
| Status | Contour created; connection **not** authorized |
| Current host | `http://shpigovsky.beget.tech/` |
| Future host | `shpigovsky.ru` (`DNS_CUTOVER = DEFERRED`) |

---

## 10. Filesystem Policy

- Transport: FTP or SFTP (canonical class); SSH optional if present. **Not guessed.**  
- Write: disabled until exact-file deployment charter.  
- Workflow: FETCH CURRENT PROD → HASH → DIFF → BACKUP EXACT FILE → RECONCILE → EDIT SOURCE → EXACT UPLOAD → VERIFY → QA → ROLLBACK READY.  
- Never: full theme upload, WP-root mirror, uploads overwrite, broad sync, stale source, dirty-main deploy.

---

## 11. DB Policy

- Read: allowed after validation.  
- Write: forbidden until explicit task.  
- No SQL as substitute for WP Admin where a native surface exists.  
- Schema writes require full DB backup.  
- Later mutations must record backup, exact SQL/entity, before, after, rollback.

---

## 12. WordPress Admin Policy

Preferred owner for pages/posts, DB-owned ACF values, menus, media, forms, SEO metadata, plugin settings, plugin-owned redirects.

Admin credentials = capability, not standing mutation permission. Every mutation remains task-chartered. No new user / no password change this wave.

---

## 13. WPilot State

- Migrated install **present** (P01 public ping: bridge on, DEV confirmed, token generated, write off).  
- Version **SAFE UNKNOWN**.  
- Install/upgrade **deferred** (do not reinstall blindly).  
- Token reconciliation **deferred**.  
- Local prod token file **not created**.  
- Write **remains disabled**.

---

## 14. Runtime Checkout

| Field | Value |
|-------|-------|
| Created? | **DEFERRED** |
| Exact future path | `X:\AI MARS STORAGE\runtime-checkouts\fp-0002-shpigovsky-production\repo` |
| Derive from | `origin/mars/canonical-post-recovery` |
| Reason | No scheduled/runtime job for this site yet. Do not run from dirty `X:\AI MARS`. Secrets must not live in the checkout |

---

## 15. Secret Safety Validation

| Check | Result |
|-------|--------|
| Local contour gitignored | **YES** (`.gitignore:13:/local/`) |
| Tracked secrets | **0** |
| Exposed values in REPORT / tracked docs | **0** |
| Other-project secret values echoed | **0** (filenames/keys only) |
| Fake token created | **NO** |
| `git add` of local files | **NO** |
| Wave files in `git diff --cached` | **NO** |
| Lightweight secret-pattern scan (this wave tracked files) | **0 hits** |
| Placeholders in `secrets.local.md` | `<OPERATOR_FILL>` present; no invented credentials |

---

## 16. Operator Action

Open **this one file** locally (editor only — do not paste into chat):

```text
X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md
```

Optional non-secret metadata (no passwords):

```text
X:\AI MARS\local\sites\shpigovsky-production\site-profile.json
```

### Fill now — field NAMES only

**FTP OR SFTP (required for later FS validation):**  
`ftp_or_sftp_protocol`, `ftp_or_sftp_host`, `ftp_or_sftp_port`, `ftp_or_sftp_username`, `ftp_or_sftp_password`, `ftp_or_sftp_remote_root_or_initial_directory`, `ftp_passive_mode_if_ftp` (if FTP), `sftp_host_key_fingerprint_if_known` (if known)

**DATABASE (required for later DB read validation):**  
`db_host`, `db_port`, `db_name`, `db_user`, `db_password`, `db_table_prefix`, `db_charset`, `db_phpmyadmin_url`

**WORDPRESS ADMIN (required for later inspection):**  
`wordpress_username`, `wordpress_password`, `wordpress_role_note`, `wordpress_dedicated_mars_account`

**BEGET CONTROL PANEL (optional):**  
`beget_login_or_account_id`, `beget_password`, `beget_account_or_site_identifier`, `beget_2fa_note_without_backup_codes`, `beget_panel_url`, `beget_notes`

**SSH (optional):**  
`ssh_available`, `ssh_host`, `ssh_port`, `ssh_username`, `ssh_password_or_key_reference`, `ssh_key_path_if_any`, `ssh_known_host_fingerprint_if_known`

### Do not fill now

- WPilot token file  
- SMTP / analytics / CRM / webhook secrets  

Where to find values: comments inside `secrets.local.md` (Beget FTP/DB cards; WP Admin ≠ Beget panel).

Then reply **only**:

```text
ACCESS FILES FILLED
```

Do **not** paste credentials into ChatGPT / Cursor chat.

Next wave (separate): validate connectivity **without printing secrets**. Still no WPilot write, no install, no DNS, no commit unless separately chartered.

---

## Changed files (this wave)

**Local-only (gitignored):**

- `X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md`  
- `X:\AI MARS\local\sites\shpigovsky-production\site-profile.json`

**Tracked created** (`DOCS/PRODUCTION/` was already untracked from P01; this wave added):

- `DOCS/PRODUCTION/FP-0002-MARS-PRODUCTION-CONNECTION-PROFILE-v1.md`  
- `DOCS/PRODUCTION/FP-0002-PRODUCTION-ACCESS-MATRIX-v1.md`  
- `DOCS/PRODUCTION/FP-0002-CREDENTIAL-REFERENCE-MAP-v1.md`  
- `DOCS/PRODUCTION/FP-0002-AGENT-SYSTEM-RESPONSIBILITY-MAP-v1.md`  
- `DOCS/PRODUCTION/FP-0002-WPILOT-CONNECTION-STATE-v1.md`  
- `DOCS/PRODUCTION/FP-0002-SOURCE-PRODUCTION-AUTHORITY-v1.md`  
- `DOCS/PRODUCTION/FP-0002-DNS-CUTOVER-STATUS-v1.md`  
- `REPORTS/REPORT-FP-0002-PROD-P02-PRODUCTION-ACCESS-CONTOUR.md`

**Tracked updated:**

- `DOCS/PRODUCTION/FP-0002-PROTECTED-ZONES-BEGET-v1.md`  
- `DOCS/PRODUCTION/FP-0002-PRODUCTION-SITE-PASSPORT-BEGET-v1.md`  
- `DOCS/PRODUCTION/FP-0002-BEGET-PRODUCTION-CHANGE-MODEL-v1.md`  
- `DOCS/PRODUCTION/FP-0002-BEGET-BACKUP-ROLLBACK-MODEL-v1.md`  
- `DOCS/PRODUCTION/FP-0002-WPILOT-INSTALL-READINESS.md`  
- `WORDPRESS/SOURCE-AUTHORITY.md` (P02 addendum only; file already had uncommitted P01/historical tail vs HEAD)  
- `PROJECT-STATUS.md`  
- `README.md`  
- `INCOMING/04_ACCESS/README.md`

**Git:** no commit, no push, no `git add`. Foreign WIP unchanged.

**UNKNOWN:** Beget protocol/host/port/docroot/DB identity until operator fill; production WPilot version until later Admin reconcile.

**SECURITY RISK:** none introduced. Operator must not paste filled secrets into chat.

---

*PROD-P02 · PASS · operator fill ready · mutations 0.*
