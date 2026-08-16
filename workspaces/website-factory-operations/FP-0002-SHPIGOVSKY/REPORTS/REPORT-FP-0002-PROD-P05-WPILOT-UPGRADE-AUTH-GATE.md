# REPORT — FP-0002 PROD-P05 WPilot Upgrade and Authenticated Read Gate

**Date:** 2026-08-14  
**Host:** `http://shpigovsky.beget.tech/`  
**Canonical domain:** `shpigovsky.ru` (`DNS_CUTOVER = DEFERRED`)  
**Evidence:** `REPORTS/evidence/prod-p05-wpilot-upgrade-auth-gate/`  
**Layer B snapshot:** `X:\AI MARS STORAGE\wpilot\evidence\fp-0002-shpigovsky\prod-p05\pre-upgrade-wpilot-0.3.0\`

```text
BLOCKED — WP ADMIN AUTHENTICATION FAILED DESPITE OPERATOR PASSWORD SYNC
OPERATOR ACTION REQUIRED — CREATE FRESH BEGET FILES + DB BACKUP
WPILOT PACKAGE 0.3.2-RC1 AUTHORITY CONFIRMED — NOT INSTALLED
WRITE_ENABLED FALSE — PACKAGE REPLACE STILL SAFE
NO PRODUCTION PRODUCT MUTATIONS
NO TOKEN REISSUE
NO COMMIT / NO PUSH
```

---

## 1. Status

* **BLOCKED**
* business/content mutations: **0**
* unrelated plugin/theme mutations: **0**
* WPilot package replacement count: **0**
* token reissue count: **0**
* WPilot readiness-setting mutations: **0**
* WPilot telemetry writes: **NO** (authenticated REST not called)
* commit/push: **none**

Desired end-state is **not** reached. Upgrade, token reissue, and authenticated MARS READ were **not** started.

Primary stop (charter §4):

`BLOCKED — WP ADMIN AUTHENTICATION FAILED DESPITE OPERATOR PASSWORD SYNC`

Independent second stop that would have blocked upgrade even after Admin PASS (charter §6):

`OPERATOR ACTION REQUIRED — CREATE FRESH BEGET FILES + DB BACKUP`

---

## 2. WP Admin Validation

| Check | Result |
|-------|--------|
| Username used | `mars` |
| Login form reachable | **YES** (not Beget antibot; `name="log"` / `name="pwd"` present) |
| HTTP login | **FAIL** (no `wordpress_logged_in` cookie; remains on `wp-login.php`) |
| Dashboard / Plugins / WPilot UI | **not reached** |
| DB user | `mars` ID **3**, registered `2026-08-14 08:00:13` |
| Administrator capability (DB) | **YES** |
| `secrets.local.md` `wordpress_password` vs live `user_pass` | **`password_matches_db_hash=false` (MISMATCH)** |
| Secrets password length | **22** (same length class as FU02) |
| Password / hash values printed | **NO** |

**Result:** not `WP ADMIN AUTHENTICATION PASS`.

No password reset attempted. No DB `user_pass` edit. No additional admin account created.

Likely cause class: local secrets value still does not match the recreated `mars` hash. Operator confirmation is recorded; independent hash check remains MISMATCH.

---

## 3. Backup Gate

| Item | State |
|------|--------|
| Documented Layer A | P01 operator-confirmed Beget files+DB (**post original migration**) |
| Layer A ID / timestamp | **SAFE UNKNOWN** |
| Current live state | **post-reimport** (PROD-P04-FU02 accepted 2026-08-14) |
| Does P01 backup cover current live DB/files? | **NO** (predates re-import) |
| Fresh post-reimport full Beget backup documented? | **NO** |
| Beget panel credentials | **MISSING** — cannot list panel backups independently |
| Narrow WPilot pre-upgrade snapshot | **YES** — 27 files, SHA match production, stored **outside** WordPress |
| Rollback readiness for plugin-only restore | Layer B snapshot **present**; Layer A for full-site **not current** |

Upgrade **not** performed. Restoring the P01 backup would roll the site back to **pre-reimport** content and would violate imported-content preservation.

---

## 4. Pre-Upgrade WPilot

| Field | Value |
|-------|--------|
| FS header / constants | **0.3.0**; `RELEASE_LABEL` **ABSENT** |
| Schema | **0.2.0** |
| Active | **yes** |
| `bridge_enabled` | **true** |
| `dev_confirmed` | **true** |
| `write_enabled` | **false** |
| `emergency_disabled` | **false** |
| Token | hash-only (`token_hash_len=63`); client plaintext **NO** |
| Production files | **27** |
| vs canonical 0.3.2-RC1 | MATCH **12** / DIVERGENT **15** / LOCAL_ONLY_NEWER **5** / PRODUCTION_ONLY **0** |
| Production-only modifications that would be lost | **NO** |
| Package replace safety | **SAFE** (revalidated) |

DIVERGENT / LOCAL_ONLY_NEWER are the expected 0.3.0 → 0.3.2-RC1 package delta (including privileged-persistence files not present on 0.3.0).

---

## 5. Upgrade

| Field | Value |
|-------|--------|
| Package | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.2-rc1.zip` |
| SHA-256 | `d55c19d6ea1a55cd145e9b67c42ca201c30e4356f08d8cf3932ef6a5ebc80934` — **MATCH** |
| Source authority | plugin Version **0.3.2** / `RELEASE_LABEL` **0.3.2-RC1** — **no material mismatch** |
| Method | WP Admin Upload Plugin — **not executed** |
| Result | **NOT PERFORMED** |

---

## 6. Post-Upgrade WPilot

Not applicable. Production remains **0.3.0** / schema **0.2.0** / active / write **false**. Frontend/Admin post-upgrade smoke **not run** (no upgrade).

---

## 7. Token Reissue

* performed: **NO**
* count: **0**
* local token path: `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token` — **not created**
* secret exposed: **NO**

---

## 8. Readiness State

Unchanged from post-reimport baseline (SELECT-only):

| Flag | Value |
|------|--------|
| `dev_confirmed` | **true** |
| `bridge_enabled` | **true** |
| `write_enabled` | **false** |
| `emergency_disabled` | **false** |

No readiness-flag mutations.

---

## 9. Authenticated READ Proof

Not attempted (stop before upgrade/token).

| Route | Auth | HTTP status | Sanitized result |
|-------|------|-------------|------------------|
| — | — | — | not executed |

Verdict: **not** `AUTHENTICATED READ CONNECTION TO MARS PROVEN`.

Exact blocker: WP Admin authentication FAIL (token reissue requires Admin generate_token). Secondary: missing post-reimport Layer A backup.

---

## 10. Operational Telemetry

* Authenticated reads **would** update connection tracker + `last_token_used_at` in `0.3.2-RC1` source (`WPilot_Auth::validate_token_credentials` / `require_read_access`) — classified as **EXPECTED WPILOT OPERATIONAL TELEMETRY WRITE** if/when READ is proven.
* This wave: **WPILOT OPERATIONAL TELEMETRY = NO**
* **BUSINESS/CONTENT WRITES = 0**

---

## 11. Write Safety

`write_enabled=false` before any mutation. Upgrade not started.

`WPILOT WRITE CLOSED AFTER READ GATE` — **N/A** (read gate not reached). Write remains **closed**.

---

## 12. Access Matrix

| Surface | This wave |
|---------|-----------|
| Public HTTP | READ **PROVEN** (prior FU02; not re-broken) |
| Filesystem | READ **PROVEN**; WRITE **CLOSED** / task-specific exact-file only |
| DB | SELECT **PROVEN**; WRITE **CLOSED** |
| WordPress Admin | HTTP **FAIL**; DB Administrator **PROVEN**; WRITE closed |
| WPilot | authenticated READ **NOT PROVEN**; WRITE **DISABLED** |
| DNS | WRITE **FORBIDDEN** / `CUTOVER DEFERRED` |

---

## 13. Runtime Checkout

**DEFERRED** — `X:\AI MARS STORAGE\runtime-checkouts\fp-0002-shpigovsky-production\repo` not created.

Reason: no scheduled runtime task; site not connected via authenticated WPilot READ; policy allows defer until a runtime job is chartered.

---

## 14. Migration Tails

Carried forward only (not fixed):

* `shpigovsky.test` residue
* local-development `blogname`
* `WP_DEBUG=true`
* `WP_ENVIRONMENT_TYPE=local`
* temporary `home` / `siteurl` (`http://shpigovsky.beget.tech`)
* sitemap 404
* HTTPS
* final DNS

---

## 15. Secret Safety

* token exposed: **0**
* passwords exposed: **0**
* tracked secrets: **0**
* cookies / nonces / DB password / private keys: **not stored**

---

## 16. Exact Files Changed

**Tracked (uncommitted)**

* `DOCS/PRODUCTION/FP-0002-MARS-PRODUCTION-CONNECTION-PROFILE-v1.md`
* `DOCS/PRODUCTION/FP-0002-PRODUCTION-ACCESS-MATRIX-v1.md`
* `DOCS/PRODUCTION/FP-0002-CREDENTIAL-REFERENCE-MAP-v1.md`
* `DOCS/PRODUCTION/FP-0002-BEGET-BACKUP-ROLLBACK-MODEL-v1.md`
* `DOCS/PRODUCTION/FP-0002-PRODUCTION-SITE-PASSPORT-BEGET-v1.md`
* `DOCS/PRODUCTION/FP-0002-WPILOT-INSTALL-READINESS.md`
* `DOCS/PRODUCTION/FP-0002-WPILOT-CONNECTION-STATE-v1.md`
* `PROJECT-STATUS.md`
* `REPORTS/REPORT-FP-0002-PROD-P05-WPILOT-UPGRADE-AUTH-GATE.md`
* `REPORTS/evidence/prod-p05-wpilot-upgrade-auth-gate/*`

**Local / STORAGE only (not Git)**

* `X:\AI MARS STORAGE\wpilot\evidence\fp-0002-shpigovsky\prod-p05\pre-upgrade-wpilot-0.3.0\` (plugin file copy + MANIFEST)
* token file **not** created

---

## 17. Git

* commit: **none**
* push: **none**
* foreign WIP: **untouched**
* `git add` / stash / reset / clean / restore: **not used**

Preflight: cwd `X:\AI MARS`, volume `AI WS`, branch `mars/canonical-post-recovery`. Existing staged foreign WIP + unpushed commits on branch were **not** modified.

---

## 18. Next Recommended Wave

Do **not** start P06. Resume **PROD-P05** only after **both** operator actions:

1. **WP Admin:** make `secrets.local.md` `wordpress_password` match the live `mars` password (independent hash check must become MATCH). Do not ask MARS to reset/edit the DB hash.
2. **Layer A:** create a **fresh Beget files + DB backup** of the **current post-reimport** production state and confirm it to MARS.

Then the same P05 charter remains valid: exact `0.3.2-RC1` ZIP SHA `d55c19d6…` via native Upload Plugin → Replace current; one token reissue to `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token`; authenticated GET only; keep `write_enabled=false`.

P06 (migration tail cleanup) stays **after** a successful P05.

```text
FP-0002 PROD-P05 BLOCKED — WP ADMIN HTTP STILL FAIL (SECRETS/DB HASH MISMATCH) — POST-REIMPORT LAYER A BACKUP NOT DOCUMENTED — WPILOT REMAINS 0.3.0 WRITE DISABLED — 0.3.2-RC1 PACKAGE CONFIRMED / REPLACE SAFE — NO UPGRADE / NO TOKEN / NO COMMIT
```

---

## Execution safety

- cwd: `X:\AI MARS`
- scope lock honored: yes (`X:\AI MARS` docs/evidence; STORAGE Layer B copy; gitignored `local/` read-only)
- destructive ops: none
- protected zone touch: production inspected read-only; no `wp-config` edit; no DNS; no WPilot settings/token/write; no plugin upload
