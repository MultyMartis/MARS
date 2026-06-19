# WPilot Release Candidate — v0.3.0-RC5

**Classification:** Release candidate specification — RC5 connection-proof freeze; no Sprint 3, no new endpoints.  
**Date:** 2026-06-19  
**Status:** RC5 installed on DEV — **live connection proof confirmed** (authenticated REST, connection tracking, admin diagnostics).  
**Plugin slug:** `metacode-wpilot`

---

## Version

| Field | Value |
|-------|-------|
| **Release label** | `v0.3.0-RC5` |
| **Plugin version** | `0.3.0` |
| **Schema version** | `0.2.0` |
| **Text domain** | `metacode-wpilot` |
| **REST namespace** | `wpilot/v1` |
| **Runtime maturity** | `proven_content_writes` |
| **Environment scope** | DEV only — human-supervised |

---

## RC5 Delta (vs RC3 / RC4)

| Area | Change |
|------|--------|
| **BUGFIX-02** | `require_read_access()` and `require_backup_access()` use partial `update_options()` for `last_token_used_at` — prevents stale full-options write from erasing `last_authorized_connection_at` and `last_authorized_endpoint` after `record_success()` |
| **Connection proof** | Live on DEV — Last Successful Connection and Last Endpoint populate in admin after authenticated REST |
| **MARS ↔ WPilot** | Token from `C:\AI MARS\local\tokens\wpilot-dev-gktriumph.token` reaches bridge |

**Inherited from RC3/RC4 (unchanged in RC5):**

- UX-02 operator dashboard (tabs, compact Overview)
- Connection tracker class (`class-wpilot-connection-tracker.php`)
- BUGFIX-01 independent success/failure metadata + endpoint labels
- MARS token standard in project docs
- Russian localization (PO/MO)

**Not in RC5 scope:** Sprint 3, new REST routes, schema version bump, production deploy.

---

## Package

| Field | Value |
|-------|-------|
| **ZIP path** | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc5.zip` |
| **Inventory** | `C:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc5.inventory.json` |
| **SHA-256** | `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577` |
| **Size** | 54,863 bytes |
| **Root folder** | `metacode-wpilot/` |
| **File count** | **27** (26 source + compiled `.mo`) |

### BUGFIX-02 modified file

- `includes/class-wpilot-auth.php` — partial `last_token_used_at` update only

---

## Connection Status Options

Stored inside `wpilot_options` (no separate secrets):

| Key | Values / purpose |
|-----|------------------|
| `last_connection_status` | `never` \| `success` \| `failed` |
| `last_connection_success_at` | UTC MySQL timestamp |
| `last_authorized_connection_at` | UTC MySQL timestamp of last successful token validation |
| `last_authorized_endpoint` | Compact route label (e.g. `site-info`, `plugins`) |
| `last_connection_failure_at` | UTC MySQL timestamp |
| `last_connection_failure_reason` | Safe codes: `AUTH_MISSING`, `AUTH_INVALID`, `TOKEN_REVOKED` |
| `last_token_used_at` | UTC MySQL timestamp (updated on read/backup access paths) |

**Never persisted:** token, headers, payloads, request bodies.

---

## Live Connection Proof (DEV)

| Check | Result |
|-------|--------|
| RC5 on `https://dev.gktriumph.ru` | **PASS** |
| Authenticated REST | **PASS** |
| Connection tracking | **PASS** |
| Admin Last Successful Connection | **PASS** |
| Admin Last Endpoint | **PASS** |
| BUGFIX-02 confirmed | **PASS** |

**Evidence reports:**

- [reports/wpilot-bugfix-02-rc5-report.md](reports/wpilot-bugfix-02-rc5-report.md)
- [reports/wpilot-state-freeze-2026-06-19.md](reports/wpilot-state-freeze-2026-06-19.md)
- Prior REST proofs: [reports/wpilot-rc3-connection-proof.md](reports/wpilot-rc3-connection-proof.md), [reports/wpilot-rc4-connection-verification.md](reports/wpilot-rc4-connection-verification.md)

---

## MARS Token Standard (operator docs)

| Field | Value |
|-------|-------|
| Storage root | `C:\AI MARS\local\tokens\` |
| DEV token file | `C:\AI MARS\local\tokens\wpilot-dev-gktriumph.token` |
| Auth header | `X-WPilot-Token` |
| DEV site | `https://dev.gktriumph.ru` |

Canonical policy: [local-storage-policy.md](local-storage-policy.md)

---

## Prior RC References

- [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md](WPILOT-RELEASE-CANDIDATE-v0.3.0-RC1.md) — UX-01 baseline package
- [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC3.md](WPILOT-RELEASE-CANDIDATE-v0.3.0-RC3.md) — UX-02 package (superseded for live DEV by RC5)
- [reports/wpilot-ux-02-report.md](reports/wpilot-ux-02-report.md) — UX-02 implementation
- [reports/wpilot-bugfix-01-report.md](reports/wpilot-bugfix-01-report.md) — RC4 tracker fix

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| RC5 clean ZIP install on disposable WordPress | **UNKNOWN** — TEST-01 remains PARTIAL |
| Exact RC5 proof timestamps | **UNKNOWN** — operator-confirmed; no dedicated RC5 connection report file |
| Sprint 3 readiness | **Not claimed** — freeze holds |
