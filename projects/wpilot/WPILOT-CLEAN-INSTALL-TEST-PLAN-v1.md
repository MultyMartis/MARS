# WPilot Clean Install Test Plan — v1

**Classification:** Test procedure — documentation only.  
**Date:** 2026-06-19  
**Target release:** `metacode-wpilot` v0.3.0-RC1 (baseline Variant B — checkpoint `8c67478` + UX-01)  
**Execution status:** **Not performed** (OPS-02)

**Complements:** [WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md](WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md) (operator checklist form).

---

## Purpose

Establish a reproducible procedure to prove WordPress **ZIP-based clean install** of WPilot RC1 on a **disposable** WordPress instance — without FTP file drops, without mixing old checkpoint ZIP with UX-01 bootstrap.

Success path advances release status from **B — RC Ready** to **C — Clean Install Proven**.

---

## Preconditions

| Requirement | Detail |
|-------------|--------|
| Disposable WordPress | Fresh install or resettable VM/container; not production |
| PHP | Compatible with plugin (7.4+ typical; match DEV if possible) |
| MySQL/MariaDB | Standard WP DB |
| Admin access | `manage_options` user |
| RC1 package | Fresh ZIP built from Variant B tree — **not** legacy `metacode-wpilot-v0.3.0.zip` (22 files) |
| Optional `.mo` | Required only if ru_RU localization step is in scope |
| REST client | `curl`, Postman, or equivalent |
| Test page | At least one published `page` post for backup/write tests |

**Out of scope:** production host, multisite, autonomous agents, Sprint 3 features.

---

## Test Environment Setup

### Step 0 — Prepare package

1. Source tree: `projects/wpilot/plugin/metacode-wpilot/` (25 files).
2. (Optional, for ru_RU step) Compile `.mo` — see [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md](WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md) localization section.
3. Build ZIP with root folder `metacode-wpilot/` containing all RC1 files.
4. Record ZIP SHA-256 and file count (expect 25, or 26 with `.mo`).

**Expected:** ZIP opens; `metacode-wpilot/metacode-wpilot.php` present; no secrets inside archive.

---

## Procedure

### 1. Disposable WordPress

**Action:**

- Provision clean WordPress (local Docker, staging subdomain, or resettable install).
- Confirm no prior `metacode-wpilot` plugin directory exists.
- Note site URL, WP version, PHP version, locale.

**Expected result:**

- WP admin loads.
- Plugins list does not contain MetaCODE WPilot.
- Database has no `{prefix}wpilot_*` tables.

**Fail criteria:** Residual plugin files or tables from prior install.

---

### 2. ZIP Install

**Action:**

- WP Admin → Plugins → Add New → Upload Plugin.
- Select RC1 ZIP (`metacode-wpilot-v0.3.0-RC1.zip` or operator-named equivalent).
- Click Install Now.

**Expected result:**

- Install succeeds without PHP fatal errors.
- Plugin directory: `wp-content/plugins/metacode-wpilot/`
- File count on disk: **25** (or 26 with `.mo`).
- Present: `admin/class-wpilot-admin-ui-model.php`, `languages/metacode-wpilot.pot`, `languages/metacode-wpilot-ru_RU.po`.

**Fail criteria:**

- Missing `class-wpilot-admin-ui-model.php` (fatal on activation).
- File count = 22 (wrong package — legacy checkpoint ZIP).

---

### 3. Activate

**Action:**

- Activate **MetaCODE WPilot** from Plugins screen.

**Expected result:**

- Activation succeeds.
- No PHP warnings/fatals in debug log (if `WP_DEBUG` enabled).
- Settings → WPilot menu entry appears (or equivalent admin menu slug).

**Fail criteria:** White screen, fatal `require`, or missing admin menu.

---

### 4. Verify Tables

**Action:**

- Inspect database (phpMyAdmin, `wp db query`, or admin tooling).
- Confirm tables after first `plugins_loaded` (activation triggers schema path).

**Expected result:**

| Object | Expected |
|--------|----------|
| `{prefix}wpilot_backups` | Exists with expected columns |
| `{prefix}wpilot_audit_log` | Exists with expected columns |
| `wpilot_options` (or options row) | Schema version `0.2.0` marker present |

**Fail criteria:** Missing tables; schema version mismatch.

---

### 5. Verify REST

**Action:**

1. `GET /wp-json/wpilot/v1/ping` — no auth.
2. In admin: enable bridge, confirm DEV/test, generate token.
3. `GET /wp-json/wpilot/v1/site-info` with header `X-WPilot-Token: <token>`.
4. Confirm route discovery: 12 routes under `wpilot/v1`.

**Expected result:**

| Call | Expected |
|------|----------|
| `/ping` | `200` — bridge status payload |
| `/site-info` (with token) | `200` — site metadata, version `0.3.0` |
| Write routes without write_enabled | Refusal per auth guards (not 404) |

**Fail criteria:** 404 on registered routes; namespace missing; version mismatch.

---

### 6. Verify Dashboard

**Action:**

- Open WPilot settings admin page.
- Inspect Runtime Status, Proven Operations, REST inventory panels (UX-01).

**Expected result:**

| UI element | Expected value |
|------------|----------------|
| Version | `0.3.0` |
| Schema Version | `0.2.0` |
| Runtime Maturity | `proven_content_writes` |
| Environment | `DEV` |
| REST Endpoints | 8 read + 1 analysis + 3 proven write |
| Warning notice | v0.3.0 capability summary (not read-only-only claim) |

**Fail criteria:** Legacy read-only-only copy; missing UX-01 panels; maturity not displayed.

---

### 7. Verify Localization

**Action:**

**7a — Foundation (always):**

- Confirm `load_plugin_textdomain` active (plugin loads without error).
- Confirm `languages/metacode-wpilot.pot` and `metacode-wpilot-ru_RU.po` on disk.

**7b — Russian runtime (only if `.mo` compiled and site locale = `ru_RU`):**

- Set site language to Russian.
- Reload WPilot admin page.
- Confirm at least one known string renders in Russian (e.g. Runtime Status panel label).

**Expected result:**

| Condition | Expected |
|-----------|----------|
| `en_US` or no `.mo` | English UI strings via `__()` — functional |
| `ru_RU` + `.mo` present | Russian strings from compiled catalog |
| `ru_RU` + no `.mo` | English fallback — **known gap**, not install failure |

**Fail criteria:** Textdomain mismatch; fatal on missing `languages/` directory.

**Note:** Absent `.mo` is a **non-blocking gap** for RC Ready; blocks full ru_RU localization proof only.

---

### 8. Verify Backup

**Action:**

- Pick test `page` ID (e.g. ID `1` or any published page).
- `POST /wp-json/wpilot/v1/pages/{id}/backups` with valid token, DEV guards satisfied.
- Record `operation_id`, `backup_id`, checksum from response.

**Expected result:**

- `200` success envelope.
- Row in `{prefix}wpilot_backups`.
- Audit event in `{prefix}wpilot_audit_log`.
- Checksum prefix `sha256:`.

**Fail criteria:** 500; no DB row; missing audit entry.

---

### 9. Verify Rollback

**Action:**

- Using backup from step 8 (or create fresh backup first).
- Optionally apply scoped replace on test page (DEV + write_enabled).
- `POST /wp-json/wpilot/v1/pages/{id}/rollback` with `backup_id` and `approval_ref`.

**Expected result:**

- `200` success envelope.
- `post_content` restored to backup snapshot.
- `rollback_verified` audit event.
- Checksum validation passed in response meta.

**Fail criteria:** Content not restored; verification failed; missing audit trail.

---

## Pass / Fail Summary

| Step | Pass advances |
|------|---------------|
| 1–3 | ZIP install path viable |
| 4 | Schema bootstrap on clean WP |
| 5 | REST surface intact |
| 6 | UX-01 admin surface present |
| 7 | i18n foundation (and ru_RU if `.mo` tested) |
| 8–9 | Proven write services on clean install |

**Full pass (steps 1–9):** Release status → **C — Clean Install Proven**

**Partial pass (1–6, 8–9 without ru_RU):** RC viable; localization gap documented.

---

## Evidence Capture

Record for each run:

| Field | Example |
|-------|---------|
| Test date | 2026-06-19 |
| WP version | 6.x |
| PHP version | 8.x |
| Site URL | `https://staging.example.invalid` |
| ZIP file hash | SHA-256 |
| ZIP file count | 25 / 26 |
| Git baseline | `8c67478` + UX-01 commit hash |
| Locale tested | `en_US` / `ru_RU` |
| Test page ID | `69` |
| Operator | name |

Store evidence outside git per [local-storage-policy.md](local-storage-policy.md) if payloads are large.

---

## Abort Conditions

Stop test and file incident if:

- Fatal error on activation.
- Schema tables not created.
- REST namespace not registered.
- Backup or rollback returns persistent 500 on clean DB.
- ZIP contains secrets or wrong file inventory.

---

## Related Documents

| Document | Role |
|----------|------|
| [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md](WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md) | RC specification |
| [reports/wpilot-ops-02-report.md](reports/wpilot-ops-02-report.md) | OPS-02 report |
| [WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md](WPILOT-CLEAN-INSTALL-CHECKLIST-v1.md) | Checklist form |

---

## Document Status

| Field | Value |
|-------|-------|
| Version | v1 test plan |
| Executed | No |
| Replaces dev-install-checklist-v0 | No — complements for RC1 |
