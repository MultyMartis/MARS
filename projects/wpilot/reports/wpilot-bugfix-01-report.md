# REPORT — WPilot BUGFIX-01

**Scope:** Connection tracker independence, authorized endpoint metadata, Connection tab UX  
**Date:** 2026-06-19  
**Plugin target:** `metacode-wpilot` v0.3.0 (post-RC3)  
**Constraints:** No REST contract changes, no runtime behavior changes beyond diagnostics persistence, no Sprint 3

---

## 1. Problem statement

Before BUGFIX-01, `WPilot_Connection_Tracker::record_auth_failure()` overwrote `last_connection_status` to `failed`. A sequence such as:

1. `GET /site-info` with valid token → success recorded  
2. `GET /site-info` without token → `AUTH_MISSING` recorded  

…left the operator UI showing **failed** and hid the last successful connection. Success and failure were not independent.

Additionally, no endpoint label was persisted on successful auth, so the Connection tab could not show which route last authorized.

---

## 2. Audit — tracker API and call sites

### Class: `includes/class-wpilot-connection-tracker.php`

| Method | Role |
|--------|------|
| `record_success( $endpoint )` | Persist authorized connection timestamp + endpoint |
| `record_auth_failure( $reason_code )` | Persist failure timestamp + safe reason code only |
| `get_snapshot()` | Operator-facing read model for admin UI |

**Note:** There is no `record_failure()` symbol in the codebase. The actual failure entry point is `record_auth_failure()`.

### Call sites (`includes/class-wpilot-auth.php` → `validate_token_credentials()`)

| Condition | Tracker call |
|-----------|--------------|
| Empty `token_hash` | `record_auth_failure( TOKEN_REVOKED )` |
| Missing header token | `record_auth_failure( AUTH_MISSING )` |
| Invalid token | `record_auth_failure( AUTH_INVALID )` |
| Valid token | `record_success( connection_endpoint_label( $request ) )` |

`validate_token_credentials()` is invoked from:

- `require_read_access()` — read routes including `/site-info`, `/themes`, `/plugins`, `/pages`, …
- `require_dry_run_access()`
- `require_backup_access()` / `require_rollback_access()` / `require_scoped_replace_access()`

Environment/readiness refusals (`operational_readiness`, `WRITE_DISABLED`, schema errors) **do not** touch the connection tracker.

---

## 3. Route verification — target read endpoints

All four requested routes register via `register_read_route()` and pass through `guard_read()` → `WPilot_Auth::require_read_access()` → `validate_token_credentials()`:

| Route | Handler | Auth guard | `record_success()` on valid token |
|-------|---------|------------|-----------------------------------|
| `GET /wp-json/wpilot/v1/site-info` | `site_info` | `require_read_access` | **Yes** |
| `GET /wp-json/wpilot/v1/themes` | `themes` | `require_read_access` | **Yes** |
| `GET /wp-json/wpilot/v1/plugins` | `plugins` | `require_read_access` | **Yes** |
| `GET /wp-json/wpilot/v1/pages` | `pages` | `require_read_access` | **Yes** |

`GET /ping` is public (`permission_callback` = `__return_true`) and does not call the tracker.

---

## 4. Fix — independent success / failure storage

### New persisted option keys

| Key | Purpose |
|-----|---------|
| `last_authorized_connection_at` | UTC timestamp of last successful token validation |
| `last_authorized_endpoint` | Compact route label (e.g. `site-info`, `plugins`, `pages`, `themes`) |

Existing keys retained for backward compatibility:

| Key | BUGFIX-01 behavior |
|-----|-------------------|
| `last_connection_success_at` | Still updated on success (mirrors authorized timestamp) |
| `last_connection_failure_at` | Updated only on auth failure |
| `last_connection_failure_reason` | `AUTH_MISSING`, `AUTH_INVALID`, or `TOKEN_REVOKED` |
| `last_connection_status` | Updated to `success` on success; **no longer** set to `failed` on auth failure |

### Logic changes

**`record_success( $endpoint )`**

- Sets `last_authorized_connection_at`, `last_authorized_endpoint`, `last_connection_success_at`, `last_connection_status = success`
- Does **not** clear failure fields

**`record_auth_failure( $reason_code )`**

- Sets `last_connection_failure_at` and `last_connection_failure_reason` only
- Does **not** overwrite success / authorized fields
- Does **not** set `last_connection_status` to `failed`

**`get_snapshot()`**

- Returns `authorized_at`, `authorized_endpoint`, `failure_at`, `failure_reason`
- Falls back `authorized_at` ← `last_connection_success_at` for sites upgraded from RC3
- Derives `status`: `success` if any authorized timestamp exists; else `failed` if only failures; else `never`

**Endpoint label extraction** (`WPilot_Auth::connection_endpoint_label()`)

- Strips `wpilot/v1/` prefix from REST route
- Examples: `site-info`, `plugins`, `pages`, `themes`, `pages/42/structure`

---

## 5. Admin UI — вкладка «Подключение»

Connection and Overview tabs now show four independent diagnostics rows:

| Label (en_US) | ru_RU |
|---------------|-------|
| Last successful connection | Последнее успешное подключение |
| Last endpoint | Последний endpoint |
| Last failure | Последний сбой |
| Failure reason | Причина сбоя |

Empty endpoint / reason values render as `—`.

Token status and last token use rows remain on the Connection tab.

---

## 6. Changed files

| File | Change |
|------|--------|
| `includes/class-wpilot-connection-tracker.php` | Independent failure writes; new keys; endpoint sanitization; snapshot model |
| `includes/class-wpilot-auth.php` | Pass endpoint label to `record_success()` |
| `includes/class-wpilot-settings.php` | Defaults + sanitize for new option keys |
| `admin/class-wpilot-admin-page.php` | Connection + Overview tab field layout |
| `admin/class-wpilot-admin-ui-model.php` | Snapshot fields in overview payload |
| `languages/metacode-wpilot.pot` | New Connection tab strings |
| `languages/metacode-wpilot-ru_RU.po` | Russian translations for BUGFIX-01 labels |
| `reports/wpilot-bugfix-01-report.md` | This report |

---

## 7. What did NOT change

| Area | Status |
|------|--------|
| REST response envelopes | **Unchanged** |
| HTTP status codes / error codes | **Unchanged** |
| Route registration / handlers | **Unchanged** |
| Auth gate semantics | **Unchanged** (only diagnostics side effects adjusted) |
| Sprint 3 scope | **Not started** |

---

## 8. Verification checklist (manual)

On a DEV site with bridge + token enabled:

1. `GET /site-info` with valid token → Connection tab shows authorized timestamp + `site-info`.
2. `GET /plugins` with valid token → authorized timestamp updates; endpoint shows `plugins`.
3. `GET /themes` with valid token → endpoint shows `themes`.
4. `GET /pages` with valid token → endpoint shows `pages`.
5. `GET /site-info` **without** token → failure row shows `AUTH_MISSING`; **authorized timestamp and endpoint remain from step 1–4**.
6. `GET /site-info` with invalid token → failure reason `AUTH_INVALID`; success row unchanged.

**SAFE UNKNOWN:** Steps 1–6 were not executed in this documentation-only session (no live WP admin / REST session in this run).

---

## 9. Git status

Documentation + plugin source edits under `projects/wpilot/`; no commit performed (default policy).
