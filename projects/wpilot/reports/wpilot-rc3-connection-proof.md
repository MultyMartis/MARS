# REPORT — WPilot RC3 Connection Proof

**Date (UTC):** 2026-06-19  
**Site:** `https://dev.gktriumph.ru`  
**Token source:** `C:\AI MARS\local\tokens\wpilot-dev-gktriumph.token`  
**Auth header:** `X-WPilot-Token`  
**Mode:** Read-only verification — no site mutations  

---

## Verdict

| Area | Result |
|------|--------|
| REST connectivity (3 endpoints) | **PASS** |
| Token acceptance | **PASS** |
| Plugin version `0.3.0` | **PASS** |
| Schema version `0.2.0` | **PARTIAL** — not returned by requested REST routes; inferred from installed plugin `0.3.0` (RC3 ships schema `0.2.0`) |
| WP Admin → Подключение UI | **SAFE UNKNOWN** — not observed in this run (no WP admin session) |

**Overall REST proof:** **PASS** — MARS token reaches WPilot RC3 bridge on DEV and authenticated reads succeed.

---

## 1. REST requests

### GET `/wp-json/wpilot/v1/ping`

| Check | Result |
|-------|--------|
| HTTP | **200** |
| Token required | No (`auth_state`: `not-required`) |
| `ok` | `true` |
| Plugin slug | `metacode-wpilot` |
| Bridge | `bridge_enabled: true`, `write_enabled: true`, `state: token-generated` |
| Timestamp (UTC) | `2026-06-19 12:30:18` |

### GET `/wp-json/wpilot/v1/site-info`

| Check | Result |
|-------|--------|
| HTTP | **200** |
| Token accepted | Yes (`meta.auth_state`: `authorized`) |
| `ok` | `true` |
| Site URL | `https://dev.gktriumph.ru` |
| WP version | `7.0` |
| PHP version | `8.3.20` |
| Active theme | `the7dtchild` |
| Timestamp (UTC) | `2026-06-19 12:30:18` |

### GET `/wp-json/wpilot/v1/plugins`

| Check | Result |
|-------|--------|
| HTTP | **200** |
| Token accepted | Yes (`meta.auth_state`: `authorized`) |
| `ok` | `true` |
| **MetaCODE WPilot version** | **`0.3.0`** |
| Plugin file | `metacode-wpilot/metacode-wpilot.php` |
| Timestamp (UTC) | `2026-06-19 12:30:19` |

---

## 2. Token gate (negative controls)

| Request | HTTP | Error code |
|---------|------|------------|
| `site-info` without token | **401** | `AUTH_MISSING` |
| `site-info` with invalid token | **401** | `AUTH_INVALID` |

Confirms the bridge enforces token auth on protected read routes.

---

## 3. Version checks

| Field | Expected | Observed | Status |
|-------|----------|----------|--------|
| Plugin version | `0.3.0` | `0.3.0` in `/plugins` data | **PASS** |
| Schema version | `0.2.0` | Not exposed on `ping`, `site-info`, or `plugins` | **PARTIAL** |

**Schema note:** `schema_version` is stored in `wpilot_options` and shown in WP Admin → **Runtime** tab (`WPilot_Constants::SCHEMA_VERSION` = `0.2.0` for plugin `0.3.0`). None of the three proof endpoints return this field. Installed plugin version `0.3.0` matches RC3 packaging where schema remains `0.2.0` per [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC3.md](../WPILOT-RELEASE-CANDIDATE-v0.3.0-RC3.md).

---

## 4. Connection tracker (indirect)

RC3 records successful auth via `WPilot_Connection_Tracker::record_success()` inside `WPilot_Auth::validate_token_credentials()` on each valid token use.

Authenticated requests in this proof (`site-info`, `plugins`) should have updated:

| Option key | Expected after proof |
|------------|----------------------|
| `last_connection_status` | `success` |
| `last_connection_success_at` | UTC timestamp ≈ `2026-06-19 12:30:18`–`12:30:19` |

---

## 5. WP Admin → MetaCODE WPilot → Подключение

**Not verified in this run** — requires operator login to `https://dev.gktriumph.ru/wp-admin/`.

**Expected after this proof (operator check):**

| UI field | Expected |
|----------|----------|
| Last MARS Connection | Filled (status label) |
| Status | **Success** |
| Last Success | Filled (UTC timestamp matching REST proof window) |

**Operator action:** Open **MetaCODE WPilot → Подключение** and confirm the three fields above. No further REST calls required unless timestamps drift.

---

## 6. Site changes

**None.** Read-only GET requests only.

---

## SAFE UNKNOWN

| Item | Reason |
|------|--------|
| WP Admin Connection tab visual state | No WP admin credentials/session in this verification run |
| Persisted `wpilot_options.schema_version` in database | Not readable via the three proof endpoints |
| RC3 ZIP install lineage | REST proves live `0.3.0` runtime; clean ZIP install proof is a separate checklist |

---

## SECURITY

- Token file used from approved local path; **token value not recorded** in this report.
- No write endpoints invoked.
- No credentials committed.

---

## Evidence summary

```
ping         → HTTP 200, bridge active
site-info    → HTTP 200, auth_state authorized
plugins      → HTTP 200, MetaCODE WPilot 0.3.0
no-token     → HTTP 401, AUTH_MISSING
bad-token    → HTTP 401, AUTH_INVALID
```
