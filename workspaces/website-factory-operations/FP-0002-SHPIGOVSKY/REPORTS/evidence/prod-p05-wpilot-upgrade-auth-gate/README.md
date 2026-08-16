# Evidence — PROD-P05 WPilot Upgrade and Authenticated Read Gate

**Date:** 2026-08-14  
**Wave:** PROD-P05 (blocked) → **PROD-P05-FU01 PASS**  
**Mutations:** WPilot package replace **1**; token reissue **1**; business/content writes **0**

## FU01 sanitized artifacts

* `fu01-wp-admin-validation.json` — HTTP login **PASS**
* `fu01-wp-admin-auth-probe.json` — form/cookie class only (no secrets)
* `fu01-package-sha.json` — ZIP SHA MATCH
* `fu01-backup-gate.json` — Layer A **OPERATOR CONFIRMED**; Layer B rollback ready
* `fu01-pre-upgrade-invariants.json` — 0.3.0 active, write false
* `fu01-upgrade-result.json` — native overwrite success
* `fu01-post-upgrade-sha-manifest.json` — 32 MATCH vs package
* `fu01-post-upgrade-settings.json` / `fu01-readiness-state.json`
* `fu01-token-file-status.json` — exists / non-empty; **no token value**
* `fu01-authenticated-read-matrix.json` — route/status only
* `fu01-final-write-disabled.json`
* `fu01-smoke.json`
* `fu01-session-summary.json`

Helper scripts (`_p05_*.py`, `_p05_fu01_*.py`) — local probes; do not print secrets.

## P05 blocked-wave artifacts (historical)

* `package-identity.json`, `wp-admin-validation.json`, `wp-admin-auth-diagnosis.json`, pre-upgrade SHA/settings/Layer B, `backup-gate.json`, `token-file-status.json`, `session-summary.json`

## Layer B snapshot (outside production)

`X:\AI MARS STORAGE\wpilot\evidence\fp-0002-shpigovsky\prod-p05\pre-upgrade-wpilot-0.3.0\`

Never stored: plaintext token, passwords, cookies, nonces, DB password, private keys.
