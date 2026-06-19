# REPORT — WPilot BUGFIX-02 RC5

**Date:** 2026-06-19  
**Scope:** Fix connection success metadata persistence; package RC5  
**Constraints:** No REST contract changes, no new endpoints, no deploy, no push, no Sprint 3

---

## 1. Root cause confirmed

**Symptom:** After authenticated REST requests, `last_token_used_at` updated but `last_authorized_connection_at` and `last_authorized_endpoint` remained empty in admin UI.

**Mechanism:**

1. `validate_token_credentials()` calls `WPilot_Connection_Tracker::record_success()` which writes success metadata via `WPilot_Settings::update_options()`.
2. Immediately after, `require_read_access()` / `require_backup_access()` held a **stale** `$options` snapshot from the start of the request.
3. Those methods set `$options['last_token_used_at']` and passed the full stale array back through `WPilot_Settings::update_options( $options )`.
4. `WPilot_Settings::update_options()` merges with `wp_parse_args( $options, $current )` — keys present in the stale snapshot (including empty defaults for connection fields never loaded into that snapshot) overwrote the freshly persisted success metadata.

**Verdict:** Stale full-options write after `record_success()` — confirmed.

---

## 2. Code changes

### Modified

| File | Change |
|------|--------|
| `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-auth.php` | `require_read_access()` and `require_backup_access()` now call partial update only |

**Before (both methods):**

```php
$options['last_token_used_at'] = current_time( 'mysql', true );
WPilot_Settings::update_options( $options );
```

**After (both methods):**

```php
WPilot_Settings::update_options(
	array(
		'last_token_used_at' => current_time( 'mysql', true ),
	)
);
```

### Unchanged (by design)

| Area | Status |
|------|--------|
| `WPilot_Settings::update_options()` merge semantics | Unchanged |
| `WPilot_Connection_Tracker` | Unchanged |
| REST routes / endpoint behavior | Unchanged |
| Option key names | Unchanged |
| Localization (`.pot` / `.po` / `.mo`) | No code-driven changes |

---

## 3. Static validation

| Check | Result | Evidence |
|-------|--------|----------|
| `record_success()` still called on valid token | **PASS** | `class-wpilot-auth.php` line ~192: `WPilot_Connection_Tracker::record_success( self::connection_endpoint_label( $request ) )` |
| `record_auth_failure()` does not erase success metadata | **PASS** | `class-wpilot-connection-tracker.php` updates only `last_connection_failure_at` and `last_connection_failure_reason` |
| `last_token_used_at` still updates on read/backup access | **PASS** | Partial `update_options()` with `'last_token_used_at'` in both `require_read_access()` and `require_backup_access()` |
| No stale full `$options` write after `record_success()` | **PASS** | Zero `$options['last_token_used_at'] =` assignments remain in auth class |
| `require_dry_run_access()` unchanged | **PASS** | Does not update token metadata (intentional) |
| `require_rollback_access()` inherits backup fix | **PASS** | Delegates to `require_backup_access()` |

**Note:** Runtime proof on DEV requires operator install of RC5 (Part 5). Static review only in this task.

---

## 4. ZIP path

| Artifact | Path |
|----------|------|
| **Deploy ZIP** | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc5.zip` |
| **Inventory JSON** | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc5.inventory.json` |
| **Build helper** | `C:\AI MARS STORAGE\wpilot\deploy-packages\build-rc5-package.py` |

---

## 5. ZIP validation

| Check | Result |
|-------|--------|
| ZIP opens | **PASS** |
| `metacode-wpilot/metacode-wpilot.php` | **PASS** |
| `metacode-wpilot/includes/class-wpilot-auth.php` (BUGFIX-02) | **PASS** |
| `metacode-wpilot/includes/class-wpilot-connection-tracker.php` | **PASS** |
| `metacode-wpilot/languages/metacode-wpilot-ru_RU.mo` | **PASS** |
| Single root folder `metacode-wpilot/` | **PASS** |
| No nested `metacode-wpilot/metacode-wpilot/` | **PASS** |
| No versioned parent folder | **PASS** |
| No backslash paths | **PASS** |
| Secret scan | **PASS** (0 hits) |
| Auth partial `last_token_used_at` update (×2) | **PASS** |
| Auth stale `$options` token write | **PASS** (0) |
| **Overall** | **`valid: true`** |

| Metric | Value |
|--------|-------|
| **Files in ZIP** | **27** |
| **Size** | **54,863 bytes** |
| **SHA256** | `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577` |

Excluded from package: reports, docs, tokens, evidence, temp, backups, `.git`, secrets.

---

## 6. Git status

| Path | Status |
|------|--------|
| `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-auth.php` | **Modified** (BUGFIX-02) |
| `projects/wpilot/reports/wpilot-bugfix-02-rc5-report.md` | **Created** (this report) |
| `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc5.zip` | **Created** (outside git) |
| `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc5.inventory.json` | **Created** (outside git) |
| `C:\AI MARS STORAGE\wpilot\deploy-packages\build-rc5-package.py` | **Created** (outside git) |

**Commit / push:** Not performed (per task constraints).

---

## 7. SAFE UNKNOWN

| Item | Status |
|------|--------|
| DEV runtime proof after RC5 install | **UNKNOWN** — requires operator steps below; not executed in this task |
| Whether RC4 on DEV exhibited the bug in all endpoint paths | **UNKNOWN** — forensic analysis assumed read + backup guards; dry-run path intentionally does not set `last_token_used_at` |
| WordPress object-cache / persistent cache edge cases on `update_option` merge | **UNKNOWN** — fix relies on existing `WPilot_Settings::update_options()` merge; no cache-layer changes |

---

## 8. SECURITY RISK

| Risk | Level | Notes |
|------|-------|-------|
| Token or secret in ZIP | **None detected** | Secret scan: 0 hits |
| Expanded attack surface | **None** | Auth logic unchanged; only persistence write shape changed |
| Information disclosure | **Unchanged** | Same admin connection diagnostics fields |
| Operator token file path | **Low (operational)** | Token stored locally at `C:\AI MARS\local\tokens\wpilot-dev-gktriumph.token` — filesystem access control is operator responsibility |

---

## Operator install steps (post-package)

1. Deactivate **MetaCODE WPilot** on DEV
2. Delete plugin
3. Upload `metacode-wpilot-v0.3.0-rc5.zip` from `C:\AI MARS STORAGE\wpilot\deploy-packages\`
4. Activate
5. Enable DEV/test + bridge + write readiness if needed
6. Generate/rotate token if needed
7. Save token in `C:\AI MARS\local\tokens\wpilot-dev-gktriumph.token`
8. Run one authenticated REST call; verify admin **Last successful connection** and **Last endpoint** populate

**Deploy / push / Sprint 3:** Not started.
