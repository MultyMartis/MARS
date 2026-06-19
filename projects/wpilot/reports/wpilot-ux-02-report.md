# REPORT — WPilot UX-02

**Sprint:** Operator Dashboard + Connection Diagnostics + Admin IA  
**Scope:** Admin UX, connection metadata, localization, RC3 package — **no deploy, no live REST verification**  
**Date:** 2026-06-19  
**Plugin target:** `metacode-wpilot` v0.3.0-RC3

---

## 1. Token storage registration

Documented MARS Token Standard in:

| Document | Registration |
|----------|--------------|
| [local-storage-policy.md](../local-storage-policy.md) | Canonical root, DEV token file path, `X-WPilot-Token`, DEV site URL |
| [README.md](../README.md) | Operator-facing summary table |
| [runtime-local.example/tokens.example.json](../runtime-local.example/tokens.example.json) | Sanitized `dev-gktriumph` metadata example |

**Canonical paths (no token values recorded):**

- Storage: `C:\AI MARS\local\tokens\`
- DEV file: `C:\AI MARS\local\tokens\wpilot-dev-gktriumph.token`
- Header: `X-WPilot-Token`
- Site: `https://dev.gktriumph.ru`

---

## 2. Main menu migration

| Before | After |
|--------|-------|
| Settings → MetaCODE WPilot | Top-level **MetaCODE WPilot** (`dashicons-shield-alt`, `manage_options`, slug `metacode-wpilot`) |
| `options-general.php?page=metacode-wpilot` | `admin.php?page=metacode-wpilot` |

Legacy **Settings → MetaCODE WPilot** alias retained for bookmarks.

---

## 3. Dashboard redesign

Overview tab is compact — four sections only:

| Section | Fields |
|---------|--------|
| **Runtime** | Status, Version, Schema, Environment, Runtime Maturity |
| **Connection** | Last MARS Connection, Status, Last Success, Last Failure |
| **Safety** | Bridge, Write Readiness, DEV Confirmation |
| **Summary** | Proven Operations Count, Endpoints Count, Last Milestone |

No long tables, endpoint lists, or verbose descriptions on Overview.

---

## 4. Tab architecture

| Tab | Content |
|-----|---------|
| **Overview** | Compact operator dashboard |
| **Runtime** | Runtime status, surface counts, proven operations checklist |
| **Connection** | MARS connection diagnostics, token status, last token use |
| **Endpoints** | Full REST inventory (read / analysis / write) |
| **Safety** | Safety features, current state, bridge/token/emergency controls |
| **Diagnostics** | Milestone 001, plugin state, schema valid, token timestamps |

Navigation: WordPress `nav-tab-wrapper`; query arg `tab`.

---

## 5. Connection tracking implementation

**New class:** `includes/class-wpilot-connection-tracker.php`

**Persisted keys** (inside `wpilot_options`):

| Key | Allowed values |
|-----|----------------|
| `last_connection_status` | `never`, `success`, `failed` |
| `last_connection_success_at` | UTC timestamp |
| `last_connection_failure_at` | UTC timestamp |
| `last_connection_failure_reason` | `AUTH_MISSING`, `AUTH_INVALID`, `TOKEN_REVOKED` |

**Auth integration** (`class-wpilot-auth.php`):

- Successful token validation → `record_success()`
- Auth failures only → `record_auth_failure()` with safe codes
- Environment/readiness refusals are **not** recorded as connection failures

**Not stored:** token, headers, secrets, request payload.

---

## 6. Localization update

| File | Status |
|------|--------|
| `languages/metacode-wpilot.pot` | Updated — 111 msgids |
| `languages/metacode-wpilot-ru_RU.po` | Updated — UX-02 strings + Russian translations |
| `languages/metacode-wpilot-ru_RU.mo` | Compiled via `polib` |

**Locales:** `en_US` (source strings), `ru_RU` (PO/MO) via WordPress `load_plugin_textdomain()`.

Compile helper: `projects/wpilot/scripts/ux02-i18n-compile.py`

---

## 7. RC3 package

| Field | Value |
|-------|-------|
| **Path** | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc3.zip` |
| **Inventory** | `metacode-wpilot-v0.3.0-rc3.inventory.json` |
| **SHA-256** | `11feb7fa4f21ec96938caef7405d21add0dd12a8e01fc2eb025c8a179f93aef6` |
| **Size** | 53,971 bytes |
| **Files** | 27 |
| **Root** | `metacode-wpilot/` |

**Excluded:** reports, backups, tokens, secrets, `.git`.

Build helper: `projects/wpilot/scripts/ux02-build-rc3-package.py`

Release note: [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC3.md](../WPILOT-RELEASE-CANDIDATE-v0.3.0-RC3.md)

---

## 8. Files changed

| File | Action |
|------|--------|
| `plugin/metacode-wpilot/includes/class-wpilot-connection-tracker.php` | **Created** |
| `plugin/metacode-wpilot/includes/class-wpilot-auth.php` | Modified — connection tracking |
| `plugin/metacode-wpilot/includes/class-wpilot-settings.php` | Modified — connection option keys |
| `plugin/metacode-wpilot/admin/class-wpilot-admin-page.php` | Modified — menu + tabs + compact UX |
| `plugin/metacode-wpilot/admin/class-wpilot-admin-ui-model.php` | Modified — overview + connection labels |
| `plugin/metacode-wpilot/metacode-wpilot.php` | Modified — require connection tracker |
| `plugin/metacode-wpilot/languages/*` | Modified — POT, PO, MO |
| `local-storage-policy.md` | Modified — MARS token standard |
| `runtime-local.example/tokens.example.json` | Modified — dev-gktriumph example |
| `README.md` | Modified — token standard section |
| `WPILOT-RELEASE-CANDIDATE-v0.3.0-RC3.md` | **Created** |
| `reports/wpilot-ux-02-report.md` | **Created** |
| `scripts/ux02-i18n-compile.py` | **Created** (build helper) |
| `scripts/ux02-build-rc3-package.py` | **Created** (build helper) |

---

## 9. Git status

Run at task closeout — plugin and docs changes are **uncommitted** (no commit, no push per task).

---

## 10. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Live connection status on DEV | **UNKNOWN** — WPilot removed from `https://dev.gktriumph.ru`; operator will install RC3 manually |
| Connection tracking runtime proof | **UNKNOWN** until authenticated REST request after RC3 install |
| RC3 clean ZIP install proof | **UNKNOWN** — not executed in UX-02 |
| Tab UI on operator WordPress locale | **UNKNOWN** until manual admin review |

---

## 11. SECURITY RISK

| Risk | Mitigation |
|------|------------|
| Token file on local disk | Documented policy; gitignored `local/`; no token in repo or reports |
| Connection failure reason codes | Whitelist only (`AUTH_*`, `TOKEN_REVOKED`) — no payloads |
| Legacy Settings menu alias | Same capability gate (`manage_options`) |
| Generated token one-time display | Unchanged UX-01 behavior |

**No deploy performed. No push performed. Sprint 3 not started.**
