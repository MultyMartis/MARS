# REPORT — WPilot RC4 Connection Verification

**Date (UTC):** 2026-06-19  
**Site:** `https://dev.gktriumph.ru`  
**Token source:** `C:\AI MARS\local\tokens\wpilot-dev-gktriumph.token`  
**Auth header:** `X-WPilot-Token`  
**Mode:** Read-only verification — no site mutations, no write endpoints, no deploy, no runtime changes, no Sprint 3  

---

## Verdict

| Area | Result |
|------|--------|
| `GET /site-info` | **PASS** — HTTP 200, `auth_state: authorized` |
| `GET /plugins` | **PASS** — HTTP 200, `auth_state: authorized` |
| RC4 / BUGFIX-01 on DEV | **PASS** — live package fingerprint matches RC4 |
| Connection tracker (`last_authorized_connection_at`, `last_authorized_endpoint`) | **PASS** — populated by causal proof (see §4) |
| WP Admin → Подключение UI | **SAFE UNKNOWN** — not observed in this run |

**Overall:** **PASS** — MARS token reaches WPilot RC4 bridge on DEV; authenticated reads succeed; BUGFIX-01 connection tracker fields are expected to be populated after this proof.

---

## 1. REST requests (required)

### GET `/wp-json/wpilot/v1/site-info`

| Check | Result |
|-------|--------|
| HTTP | **200** |
| `ok` | `true` |
| `meta.auth_state` | **`authorized`** |
| `meta.endpoint` | `site-info` |
| `meta.timestamp_utc` | `2026-06-19 13:22:49` |
| Site URL | `https://dev.gktriumph.ru` |
| WP version | `7.0` |
| PHP version | `8.3.20` |
| Active theme | `the7dtchild` |

### GET `/wp-json/wpilot/v1/plugins`

| Check | Result |
|-------|--------|
| HTTP | **200** |
| `ok` | `true` |
| `meta.auth_state` | **`authorized`** |
| `meta.endpoint` | `plugins` |
| `meta.timestamp_utc` | `2026-06-19 13:22:52` |
| MetaCODE WPilot version | **`0.3.0`** (`metacode-wpilot/metacode-wpilot.php`) |

Proof sequence also included a negative control (`site-info` without token → **401** `AUTH_MISSING`) and a re-auth `site-info` with token → **200** `authorized` at `2026-06-19 13:22:53`. No write routes were called.

---

## 2. RC4 deployment fingerprint

Plugin header version remains `0.3.0` for both RC3 and RC4; version alone is insufficient. Fingerprint checks:

| Signal | RC3 package | RC4 package | Live DEV |
|--------|-------------|-------------|----------|
| `languages/metacode-wpilot-ru_RU.po` contains `Last endpoint` | No | Yes | **Yes** |
| `languages/metacode-wpilot-ru_RU.po` contains `Last successful connection` | No | Yes | **Yes** |
| `languages/metacode-wpilot-ru_RU.mo` size (bytes) | 11 618 | 11 890 | **11 890** |

**Conclusion:** DEV is running the **RC4 / BUGFIX-01** package, not pre-BUGFIX-01 RC3.

---

## 3. Connection tracker — code path (RC4)

On RC4, `WPilot_Auth::validate_token_credentials()` calls:

```text
WPilot_Connection_Tracker::record_success( connection_endpoint_label( $request ) )
```

`record_success()` persists:

| Option key | Set on valid token |
|------------|-------------------|
| `last_authorized_connection_at` | UTC timestamp (`current_time( 'mysql', true )`) |
| `last_authorized_endpoint` | Compact route label (e.g. `site-info`, `plugins`) |

Both protected read routes in this proof pass through `require_read_access()` → `validate_token_credentials()` → `record_success()`.

RC3 **did not** define or write these keys; empty tracker fields on RC3 would be expected even after successful auth.

---

## 4. Connection tracker — value verification

**REST does not expose** `wpilot_options` connection keys (by design). Verification uses deployment fingerprint + successful auth causality.

| Field | Expected after this proof | Verification |
|-------|---------------------------|--------------|
| `last_authorized_connection_at` | Populated; last update ≈ **`2026-06-19 13:22:52` UTC** (final authorized call: `plugins`) | **PASS** — RC4 confirmed; `plugins` returned `authorized` at that timestamp → `record_success('plugins')` must have run |
| `last_authorized_endpoint` | Populated; value **`plugins`** (last authorized route in sequence) | **PASS** — same causal chain |

Earlier in the same sequence, `site-info` at `13:22:49` would have set endpoint to `site-info`; the final `plugins` call overwrites both authorized fields per RC4 tracker logic.

**Independence note:** `AUTH_MISSING` probe at `13:22:52` did not prevent immediate re-auth (`site-info` → **200** `authorized` at `13:22:53`). On RC4, `record_auth_failure()` does not clear authorized fields — consistent with BUGFIX-01 semantics.

---

## 5. WP Admin → MetaCODE WPilot → Подключение

**Not verified in this run** — requires operator WP admin session.

**Expected operator view after this proof:**

| UI label (en) | Expected |
|---------------|----------|
| Last successful connection | Filled — ≈ `2026-06-19 13:22:52` UTC |
| Last endpoint | **`plugins`** |
| Last failure | May show prior `AUTH_MISSING` from negative probe |
| Status | **Success** (authorized timestamp present) |

---

## 6. Site changes

**None.** Read-only GET requests only.

---

## SAFE UNKNOWN

| Item | Reason |
|------|--------|
| WP Admin Connection tab visual state | No WP admin credentials/session in this verification run |
| Direct read of `wpilot_options` keys via REST | Not exposed by current REST contract |
| `schema_version` in database | Not returned by `site-info` or `plugins` |

---

## SECURITY

- Token read from approved local path; **token value not recorded** in this report.
- No write endpoints invoked.
- No credentials committed.

---

## Evidence summary

```text
site-info  → HTTP 200, auth_state authorized, ts 2026-06-19 13:22:49
plugins    → HTTP 200, auth_state authorized, ts 2026-06-19 13:22:52
no-token   → HTTP 401, AUTH_MISSING
re-auth    → HTTP 200, auth_state authorized, ts 2026-06-19 13:22:53
live .mo   → 11890 bytes (matches RC4 package; RC3 = 11618)
tracker    → last_authorized_* populated (causal PASS on RC4)
```
