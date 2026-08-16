# REPORT — FP-0002 PROD-P05-FU01 WPilot Auth Closeout

**Date:** 2026-08-14  
**Host:** `http://shpigovsky.beget.tech/`  
**Canonical domain:** `shpigovsky.ru` (`DNS_CUTOVER = DEFERRED`)  
**Evidence:** `REPORTS/evidence/prod-p05-wpilot-upgrade-auth-gate/` (`fu01-*`)  
**Layer B snapshot:** `X:\AI MARS STORAGE\wpilot\evidence\fp-0002-shpigovsky\prod-p05\pre-upgrade-wpilot-0.3.0\`  
**Local token (path only):** `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token`

```text
WPILOT 0.3.2-RC1 ACTIVE — NEW PRODUCTION TOKEN STORED LOCALLY — AUTHENTICATED MARS READ PROVEN — WRITE_ENABLED FALSE
FP-0002 MARS PRODUCTION CONNECTION COMPLETE — WPILOT 0.3.2-RC1 ACTIVE — AUTHENTICATED READ PROVEN — FILESYSTEM/DB/WP ADMIN PROVEN — PRODUCTION TOKEN STORED LOCALLY — WRITE DISABLED
```

---

## 1. Status

* **PASS**
* business/content writes: **0**
* WPilot package replacement count: **1**
* token generation count: **1**
* readiness flag mutations: **0** (dev_confirmed/bridge preserved through overwrite)
* operational telemetry: **YES** (`EXPECTED WPILOT OPERATIONAL TELEMETRY WRITE`)
* commit/push: **none**

---

## 2. WP Admin

Operator-confirmed `mars` password in `secrets.local.md` is usable. Independent HTTP login **PASS** (form hidden fields + no-redirect POST; Beget `beget=begetok`).

| Check | Result |
|-------|--------|
| Username | `mars` |
| Login | **PASS** — `WP ADMIN AUTHENTICATION PASS` |
| Administrator | **YES** (Users/Plugins capability surface) |
| Dashboard | **PASS** |
| Plugins | **PASS** — WPilot visible |
| WPilot screen | **PASS** (`admin.php?page=metacode-wpilot`) |
| Password printed | **NO** |
| Password reset / user edit | **not performed** |

Note: live `user_pass` uses `$wp$2y$` (WP 7 bcrypt wrapper). A naive phpass compare still reports MISMATCH; HTTP login is the authority for this gate.

---

## 3. Backup Gate

| Item | State |
|------|--------|
| Current post-reimport Layer A backup | **`OPERATOR CONFIRMED`** (files + database of current live state) |
| Archive downloaded by MARS | **NO** |
| Additional full-site backup created by MARS | **NO** |
| Narrow WPilot 0.3.0 rollback snapshot | **YES** — 27 files + MANIFEST; SHA match at copy; outside WordPress |
| Rollback ready | **YES** (Layer B plugin restore + operator Layer A) |

`CURRENT POST-REIMPORT LAYER A BACKUP = OPERATOR CONFIRMED`

---

## 4. Package Validation

| Field | Value |
|-------|--------|
| Version | **0.3.2** |
| Release | **0.3.2-RC1** |
| ZIP | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.2-rc1.zip` |
| Size | 74788 |
| Members | 32 |
| SHA-256 recomputed | `d55c19d6ea1a55cd145e9b67c42ca201c30e4356f08d8cf3932ef6a5ebc80934` |
| Expected | **MATCH** |

---

## 5. Upgrade Result

| Field | Value |
|-------|--------|
| Old | **0.3.0** (RELEASE_LABEL absent); 27 files; active; `write_enabled=false` |
| New | **0.3.2** / **0.3.2-RC1**; 32 files |
| Method | WP Admin → Plugins → Add New → Upload Plugin → Install Now → **Replace current with uploaded** |
| Overwrite prompt | seen; followed once |
| Activate CTA clicked | **false** (plugin remained active) |
| Deactivate first | **false** |
| Active after | **YES** (DB `active_plugins` + REST `/plugins`) |
| Filesystem parity vs ZIP | **32 MATCH** / production-only **0** / zip-only **0** |
| Other plugins / core / theme updates | **0** |

Option field `plugin_version` remains **0.3.0** (overwrite without `activate()` does not rewrite that option). Runtime truth is the plugin header / constants / REST plugin list: **0.3.2**. Schema stays **0.2.0** (correct for 0.3.2-RC1).

---

## 6. Post-Upgrade Health

| Surface | Result |
|---------|--------|
| `/` | 200 |
| `/o-centre/` | 200 |
| `/uslugi/` | 200 |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 200 (service leaf) |
| `/kontakty/` | 200 |
| PHP notices on those routes | **none observed** |
| Dashboard / Plugins / WPilot | **PASS** |
| `write_enabled` | **false** |
| `dev_confirmed` / `bridge_enabled` | **true** / **true** |
| `emergency_disabled` | **false** |

---

## 7. Token

Supported 0.3.2-RC1 method: WP Admin WPilot **safety** tab → `wpilot_action=generate_token` (nonce `wpilot_admin_action` / `wpilot_nonce`). `can_manage_token` does not require bridge/DEV/write. Plaintext shown once in Admin HTML; stored immediately to local file; not logged.

* reissue: **YES**
* count: **1**
* local path: `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token`
* gitignored `/local/`: **YES**
* exposed: **NO**
* second generation: **not performed**

`TOKEN STORED LOCALLY`

---

## 8. Readiness State

| Flag | After upgrade + token + READ |
|------|------------------------------|
| `dev_confirmed` | **true** |
| `bridge_enabled` | **true** |
| `write_enabled` | **false** |
| `emergency_disabled` | **false** |
| token | present (hash only on server) |

Readiness restore POST: **not required** (flags preserved). Write never enabled.

---

## 9. Authenticated Read

Unauthenticated `GET /wp-json/wpilot/v1/site-info` → **401 AUTH_MISSING** (not public).  
Authenticated requests use `X-WPilot-Token` against `wpilot/v1`.  
«Пространство восстановления» resolved live as page **1054** (`prostranstvo-vosstanovleniya`, publish) — not a hardcoded legacy ID.

| Route | Auth | HTTP | Sanitized result |
|-------|------|------|------------------|
| `/wp-json/wpilot/v1/site-info` | none | **401** | `AUTH_MISSING` — proves gated |
| `/wp-json/wpilot/v1/site-info` | token | **200** | WP **7.0.4** / PHP **8.3.20** / theme Shpigovsky / bridge true / write false |
| `/wp-json/wpilot/v1/themes` | token | **200** | Shpigovsky `0.3.0-d7a-shell` |
| `/wp-json/wpilot/v1/plugins` | token | **200** | 5 plugins; WPilot **0.3.2** |
| `/wp-json/wpilot/v1/pages` | token | **200** | 25 pages (limit 50) |
| `/wp-json/wpilot/v1/pages/1054` | token | **200** | publish; title_len 27; checksum prefix `sha256:8db0894c99e` |

Verdict: **`AUTHENTICATED READ CONNECTION TO MARS PROVEN`**

---

## 10. Telemetry

* expected telemetry writes: **YES** — `last_token_used_at` / `last_authorized_connection_at` = `2026-08-14 09:05:53` UTC; `last_authorized_endpoint` = `pages/1054`; `last_connection_status` = `success`
* classification: **`EXPECTED WPILOT OPERATIONAL TELEMETRY WRITE`**
* **BUSINESS/CONTENT WRITES = 0**

---

## 11. Write Safety

Independently verified after all authenticated reads:

`write_enabled=false`

**`WPILOT WRITE CLOSED AFTER READ GATE`**

No test post/page. No dry-run replace. Write not enabled.

---

## 12. Production Connection Status

| Surface | Read | Write |
|---------|------|-------|
| Public HTTP | **PROVEN** | n/a |
| Filesystem | **PROVEN** | **CLOSED** |
| DB SELECT | **PROVEN** | **CLOSED** |
| WordPress Admin | **PROVEN** (HTTP + Administrator) | task-specific only; none this wave except authorized WPilot Admin actions |
| WPilot authenticated REST | **PROVEN** | **DISABLED** |
| DNS | n/a | **FORBIDDEN / CUTOVER DEFERRED** |

---

## 13. Runtime Checkout

**DEFERRED** — `X:\AI MARS STORAGE\runtime-checkouts\fp-0002-shpigovsky-production\repo` not created.

Reason: no scheduled runtime task; policy does not require a checkout solely to close P05.

---

## 14. Migration Tails

Deferred unchanged (not modified):

* `.test` URL residue
* local-development site title
* `WP_DEBUG=true`
* `WP_ENVIRONMENT_TYPE=local`
* temporary `home` / `siteurl` (`http://shpigovsky.beget.tech`)
* HTTPS
* sitemap 404
* DNS cutover

---

## 15. Secret Safety

* token exposed: **0**
* password exposed: **0**
* tracked secrets: **0**
* cookies / nonces / DB credentials / private keys: **not stored in evidence**

---

## 16. Exact Files Changed

**Tracked (uncommitted; this wave)**

* `DOCS/PRODUCTION/FP-0002-MARS-PRODUCTION-CONNECTION-PROFILE-v1.md`
* `DOCS/PRODUCTION/FP-0002-PRODUCTION-ACCESS-MATRIX-v1.md`
* `DOCS/PRODUCTION/FP-0002-CREDENTIAL-REFERENCE-MAP-v1.md`
* `DOCS/PRODUCTION/FP-0002-WPILOT-CONNECTION-STATE-v1.md`
* `DOCS/PRODUCTION/FP-0002-WPILOT-INSTALL-READINESS.md`
* `DOCS/PRODUCTION/FP-0002-BEGET-BACKUP-ROLLBACK-MODEL-v1.md`
* `DOCS/PRODUCTION/FP-0002-PRODUCTION-SITE-PASSPORT-BEGET-v1.md`
* `PROJECT-STATUS.md`
* `REPORTS/REPORT-FP-0002-PROD-P05-FU01-WPILOT-AUTH-CLOSEOUT.md`
* `REPORTS/evidence/prod-p05-wpilot-upgrade-auth-gate/fu01-*` and helper scripts

**Local / STORAGE only (not Git)**

* `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token` — **TOKEN STORED LOCALLY**
* Layer B 0.3.0 snapshot unchanged (rollback source)

**Production product (authorized)**

* `wp-content/plugins/metacode-wpilot/` package replace **0.3.0 → 0.3.2-RC1**
* one WPilot token hash rotation
* WPilot operational telemetry timestamps from authenticated GET

---

## 17. Git

* commit: **none**
* push: **none**
* foreign WIP: **untouched**
* `git add` / stash / reset / clean / restore: **not used**
* token file ignored by `/local/`

Preflight: cwd `X:\AI MARS`, volume `AI WS`, branch `mars/canonical-post-recovery`. Existing staged foreign WIP + unpushed commits on branch were **not** modified.

---

## 18. Next Recommended Wave

Do **not** execute in this wave:

`PROD-P06 — Production Migration Tail Cleanup and Environment Normalization`

---

```text
FP-0002 MARS PRODUCTION CONNECTION COMPLETE — WPILOT 0.3.2-RC1 ACTIVE — AUTHENTICATED READ PROVEN — FILESYSTEM/DB/WP ADMIN PROVEN — PRODUCTION TOKEN STORED LOCALLY — WRITE DISABLED
```

## Execution safety

- cwd: `X:\AI MARS`
- scope lock honored: yes (`X:\AI MARS` docs/evidence; gitignored `local/tokens`; STORAGE Layer B read-only)
- destructive ops: none
- protected zone touch: production WPilot plugin replace (chartered); one token reissue; no `wp-config`; no DNS; write remained disabled
