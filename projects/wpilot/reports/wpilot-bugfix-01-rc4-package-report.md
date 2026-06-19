# REPORT — WPilot BUGFIX-01 RC4 Package

**Date:** 2026-06-19  
**Scope:** Packaging only — deploy RC4 with BUGFIX-01 connection tracker fix  
**Constraints:** No runtime logic changes, no new endpoints, no deploy, no push, no Sprint 3

---

## 1. Source audit

**Plugin root:** `projects/wpilot/plugin/metacode-wpilot/`  
**Header version:** `0.3.0` (unchanged from RC3)

### BUGFIX-01 — connection tracker

| Check | Result | Evidence |
|-------|--------|----------|
| `last_authorized_connection_at` | **Present** | `class-wpilot-connection-tracker.php` const `KEY_AUTHORIZED_AT`; defaults in `class-wpilot-settings.php` |
| `last_authorized_endpoint` | **Present** | const `KEY_AUTHORIZED_ENDPOINT`; sanitized in settings |
| `record_success($endpoint)` | **Present** | Sets status, success_at, authorized_at, authorized_endpoint |
| `record_auth_failure` does not overwrite last success | **Confirmed** | Updates only `last_connection_failure_at` and `last_connection_failure_reason`; does **not** touch authorized keys or set status to `failed` |
| Status derivation | **Independent** | `derive_status()` returns `success` when `authorized_at` is set, even if failure metadata exists |

### Auth call sites

`class-wpilot-auth.php` → `validate_token_credentials()`:

- `TOKEN_REVOKED` / `AUTH_MISSING` / `AUTH_INVALID` → `record_auth_failure()`
- Valid token → `record_success( connection_endpoint_label( $request ) )`

### Admin UI labels

`class-wpilot-admin-page.php` (Overview + Connection tab):

- `Last successful connection` → `authorized_at`
- `Last endpoint` → `authorized_endpoint`
- `Last failure` / `Failure reason` → failure metadata (independent)

### Localization

| File | BUGFIX-01 strings |
|------|-------------------|
| `languages/metacode-wpilot.pot` | `Last successful connection`, `Last endpoint`, `Last failure`, `Failure reason` |
| `languages/metacode-wpilot-ru_RU.po` | Same msgids with Russian msgstr (e.g. «Последнее успешное подключение», «Последний endpoint») |
| `languages/metacode-wpilot-ru_RU.mo` | Compiled at package build time via `polib` from existing `.po` |

**Audit verdict:** Source tree contains complete BUGFIX-01 implementation. DEV stale state is explained by RC3 (pre-BUGFIX-01) still installed — not missing source code.

---

## 2. ZIP path

| Artifact | Path |
|----------|------|
| **Deploy ZIP** | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc4.zip` |
| **Inventory JSON** | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc4.inventory.json` |
| **Build helper** | `C:\AI MARS STORAGE\wpilot\deploy-packages\build-rc4-package.py` |

---

## 3. ZIP validation

| Check | Result |
|-------|--------|
| ZIP opens | **PASS** |
| `metacode-wpilot/metacode-wpilot.php` | **PASS** |
| `metacode-wpilot/includes/class-wpilot-connection-tracker.php` | **PASS** |
| `metacode-wpilot/languages/metacode-wpilot-ru_RU.mo` | **PASS** |
| Single root folder `metacode-wpilot/` | **PASS** |
| No nested `metacode-wpilot/metacode-wpilot/` | **PASS** (0 nested paths) |
| No versioned parent folder | **PASS** |
| No backslash paths | **PASS** |
| Secret scan | **PASS** (0 hits) |
| Tracker symbols in packaged file | **PASS** |
| **Overall** | **`valid: true`** |

Excluded from package: reports, docs, tokens, evidence, temp, backups, `.git`, secrets.

---

## 4. File count

| Metric | Value |
|--------|-------|
| **Files in ZIP** | **27** |
| **Size** | **54,857 bytes** |
| **RC3 comparison** | Same count (27); +786 bytes (BUGFIX-01 source + refreshed `.mo`) |

---

## 5. SHA256

```
ef151dde1d41a7ac8c1667695c3e396d106282a914baa504b54d58426a5f45a9
```

---

## 6. Manual install steps (operator)

1. WordPress admin → **Plugins**
2. **Deactivate** MetaCODE WPilot
3. **Delete** MetaCODE WPilot
4. **Upload** `metacode-wpilot-v0.3.0-rc4.zip` (from `C:\AI MARS STORAGE\wpilot\deploy-packages\`)
5. **Activate** MetaCODE WPilot
6. Re-enable **DEV bridge / write** toggles if they reset after reinstall
7. **Confirm token state** — re-issue token if reinstall cleared options
8. Run **read-only REST proof** with operator token file (e.g. `GET /wp-json/wpilot/v1/site-info` with `X-WPilot-Token`)
9. Open WPilot admin → **Connection** tab

### Expected after REST proof

| Field | Expected |
|-------|----------|
| Last successful connection | Filled (UTC timestamp) |
| Last endpoint | Filled (e.g. `site-info`) |
| Last failure | May remain populated if prior `auth_missing` occurred |
| Status | **Must not erase last success** — should show success when authorized_at exists |

Optional: repeat without token to confirm failure metadata updates independently without clearing success fields.

**Not performed in this task:** deploy to DEV, REST proof execution, token verification on live site.

---

## 7. Git status

Relevant repo state (`C:\AI MARS`) — packaging did **not** commit or push:

**Modified (tracked):**

- `projects/wpilot/plugin/metacode-wpilot/admin/class-wpilot-admin-page.php`
- `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-auth.php`
- `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-settings.php`
- (+ other wpilot docs/runtime paths from prior work)

**Untracked (includes BUGFIX-01 + i18n):**

- `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-connection-tracker.php`
- `projects/wpilot/plugin/metacode-wpilot/languages/` (`.pot`, `.po`, compiled `.mo`)
- `projects/wpilot/reports/wpilot-bugfix-01-report.md`
- `projects/wpilot/reports/wpilot-bugfix-01-rc4-package-report.md` (this file)

**Outside git (bulk storage):**

- `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc4.zip`
- `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc4.inventory.json`
- `C:\AI MARS STORAGE\wpilot\deploy-packages\build-rc4-package.py`

---

## 8. SAFE UNKNOWN

| Item | Status |
|------|--------|
| DEV install outcome after operator upload | **Not proven** — package built and validated locally only |
| Post-install Connection tab on live DEV | **Not proven** — requires operator steps 1–9 |
| ru_RU runtime UI on DEV | **Not proven** — `.mo` included; site locale must be `ru_RU` |
| Whether DEV options survive delete/reinstall | **Unknown** — token and bridge toggles may reset; operator must re-check |
| RC4 vs RC3 byte-level diff on DEV behavior | **Expected** BUGFIX-01 fix; not runtime-verified in this pass |

---

## 9. SECURITY RISK

| Risk | Level | Notes |
|------|-------|-------|
| Secrets in RC4 ZIP | **None detected** | Pattern scan clean on text assets |
| Token persistence in package | **None** | No token files packed |
| Operator token file handling | **Operational** | Step 8 uses local token file — do not commit or upload token to repo |
| Delete/reinstall data loss | **Low–medium** | WP options may reset; re-issue token if needed |
| `.mo` compile supply chain | **Low** | Compiled locally with `polib` from in-repo `.po`; no web converters |

**No deploy, no push, no Sprint 3 performed.**

---

## Changed / created files (this task)

| Action | Path |
|--------|------|
| Created | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc4.zip` |
| Created | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc4.inventory.json` |
| Created | `C:\AI MARS STORAGE\wpilot\deploy-packages\build-rc4-package.py` |
| Generated | `projects/wpilot/plugin/metacode-wpilot/languages/metacode-wpilot-ru_RU.mo` (compile artifact for packaging) |
| Created | `projects/wpilot/reports/wpilot-bugfix-01-rc4-package-report.md` |

**Runtime logic:** unchanged in this task.
