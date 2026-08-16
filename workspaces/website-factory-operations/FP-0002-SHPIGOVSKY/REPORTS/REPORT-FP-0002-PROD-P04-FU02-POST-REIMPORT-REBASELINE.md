# REPORT — FP-0002 PROD-P04-FU02 Post-Reimport Production Rebaseline

**Date:** 2026-08-14  
**Host:** `http://shpigovsky.beget.tech/`  
**Canonical domain:** `shpigovsky.ru` (`DNS_CUTOVER = DEFERRED`)  
**Evidence:** `REPORTS/evidence/prod-p04-fu02-post-reimport-rebaseline/`  
**Prior baseline (historical):** `REPORTS/evidence/prod-p04-fu01-filesystem-baseline/` · `REPORTS/REPORT-FP-0002-PROD-P04-FU01-FILESYSTEM-BASELINE.md`

```text
OPERATOR RE-IMPORT ACCEPTED AS NEW PRODUCTION BASELINE
NEW BEGET DB = LIVE CONTENT / ADMIN AUTHORITY
BEGET FILESYSTEM = LIVE RUNTIME TRUTH
LOCAL WORDPRESS TREE = CODE / SOURCE AUTHORITY
PREVIOUS PROD-P04-FU01 = HISTORICAL PRE-REIMPORT BASELINE
NO OLD DB RESTORE OR LOCAL DB OVERWRITE WITHOUT EXPLICIT OPERATOR APPROVAL
REIMPORT PRODUCT CODE PARITY CLEAN
SSH/FTP/DB SELECT REVALIDATED
MARS WP ADMIN DB ROLE PROVEN — HTTP LOGIN BLOCKED (PASSWORD MISMATCH IN secrets.local.md)
WPILOT 0.3.0 WRITE DISABLED — PACKAGE REPLACE SAFE — TOKEN REISSUE REQUIRED
NO PRODUCTION PRODUCT MUTATIONS
NO COMMIT / NO PUSH
```

---

## 1. Status

* **PARTIAL**
* production mutations: **0**
* DB writes: **0**
* filesystem writes: **0**
* WP Admin writes: **0** (HTTP login not achieved; no saves)
* WPilot writes: **0** (`write_enabled=false`; no upgrade; no token reissue)
* commit/push: **none**

**Blocker (non-repair this wave):** WordPress Admin HTTP login for recreated user `mars` **FAIL** — `secrets.local.md` `wordpress_password` **does not match** DB `user_pass` hash (`password_matches_db_hash=false`). DB proves `mars` (ID 3, registered 2026-08-14) has **Administrator** capability.

Desired end-state for product/filesystem/DB baseline is **largely reached**. WP Admin HTTP inspection gate remains open until operator updates the local password to the recreated account value.

---

## 2. Access Revalidation

| Surface | Result |
|---------|--------|
| SSH | **PASS** (`shpigovsky_mars`) |
| FTP :21 | **PASS** (listing includes WordPress tree) |
| Real docroot | **`/home/s/shpigovsky/shpigovsky.ru/public_html`** — **PASS** (`wp-config.php` + theme readable) |
| Jail regression | **none observed** |
| DB SELECT (`SSH_LOCAL_MYSQL`) | **PASS** — `shpigovsky_main`, prefix `fp02_`, core tables present |
| WP Admin HTTP login | **FAIL** (password mismatch vs recreated hash) |
| WP Admin DB role | **PASS** — Administrator |

---

## 3. Runtime Identity

| Field | Current value |
|-------|----------------|
| WordPress core | **7.0.4** |
| PHP web | **PHP/8.3.20** (`X-Powered-By`) |
| Docroot | `/home/s/shpigovsky/shpigovsky.ru/public_html` |
| Active theme | `shpigovsky` |
| Active plugins | ACF Extended PRO, ACF PRO, Classic Editor, `metacode-wpilot`, `shpigovsky-core` |
| ACF JSON path | `wp-content/acf-json` (24 files) |
| `shpigovsky-core` | present / active |
| WPilot | **0.3.0** FS + DB; schema **0.2.0**; active; write **false** |
| Uploads | `{docroot}/wp-content/uploads` |
| `home` / `siteurl` | `http://shpigovsky.beget.tech` |
| `blogname` | `Шпиговский — локальная разработка` |
| `blogdescription` | empty |
| Permalinks | `/blog/%postname%/` (pretty routes still resolve for IA paths) |

---

## 4. New Filesystem Baseline

Local source: `WORDPRESS/` · Production: Beget docroot product surfaces.

| Surface | MATCH | intentional source-only | production-only | local-only | divergent |
|---------|------:|------------------------:|----------------:|-----------:|----------:|
| Theme `shpigovsky` | **660** (incl. 1 line-ending-only content match counted as MATCH) | 0 | **1** (`.BROKEN-MPEGTS.bak`) | 0 | **0** effective |
| `shpigovsky-core` | **25** | 0 | 0 | 0 | 0 |
| ACF JSON | **24** | **7** | 0 | 0 | 0 |

**Verdict:** `REIMPORT PRODUCT CODE PARITY CLEAN`

Notes:

* `assets/css/v9-style.css` — production SHA changed vs FU01 due to **CRLF→LF only**; normalized content **identical** to local source.
* `assets/video/sergey-shpigovsky-interview.mp4.BROKEN-MPEGTS.bak` — production-only migration artifact; **not** material product code.

---

## 5. Pre-vs-Post Reimport File Diff

Compared new manifest to `prod-p04-fu01-filesystem-baseline/production-source-parity-manifest.json`.

| Metric | Count |
|--------|------:|
| Unchanged production SHA | **708** |
| Changed production SHA | **1** (`v9-style.css` line endings) |
| Added on production | **1** (BROKEN-MPEGTS.bak) |
| Removed from production | **0** |
| Material product code changes (effective) | **0** |

* Code drift: **none material**  
* Verdict: **`REIMPORT PRODUCT CODE PARITY CLEAN`**  
* Olya signal: edits appear **DB/content-oriented**, not material PHP/JS/JSON/template filesystem drift (authorship still **SAFE UNKNOWN**).

---

## 6. New DB Baseline

| Field | Value |
|-------|-------|
| DB | `shpigovsky_main` |
| Prefix | `fp02_` |
| Charset / collation | `utf8mb4` / `utf8mb4_unicode_ci` |
| MySQL | `8.4.8-8-beget-1-2` |
| Core tables | present (10/10) |
| Published posts | 16 |
| Published pages | 25 |
| Published services | 29 |
| Revisions | 250 |
| All publish statuses | 857 |
| Attachments | 38 |
| Users | 3 (logins only: `mli_admin_fp0002`, `admin`, `mars`) |
| ACF field-group rows | 35 (unique titles 21) |
| Active theme | `shpigovsky` |
| WPilot | v0.3.0 / schema 0.2.0 / bridge on / write **off** / token hash present |

Authority transition recorded:

`CURRENT BEGET DB = LIVE CONTENT / ADMIN AUTHORITY`  
Prior PROD-P04 DB inventory = **historical only** — do not merge/restore without operator approval.

---

## 7. Imported Content Delta

| Signal | Result |
|--------|--------|
| Publish page/post counts vs prior P04 | pages **25→25**, posts publish **16→16**, all_publish **857→857** |
| ACF field-group rows | **39→35** (unique titles **22→21**) |
| Objects modified ≥ 2026-07-20 | **51** publish page/post/service rows (IDs+titles+timestamps in evidence) |
| Authorship | **AUTHORSHIP SAFE UNKNOWN** (no direct proof of “edited by Olya”) |
| Preservation | **Imported DB preserved as live authority** |

Classification used: `NEW/CHANGED SINCE PRIOR BASELINE` where timestamps warrant; otherwise present-in-new-DB. No claim of named author without proof.

---

## 8. Migration Residue

Needle: `shpigovsky.test`

| Metric | Count |
|-------:|
| Total occurrences (incl. revisions) | **262** |
| Objects (incl. revisions) | **259** |
| Non-revision objects | **41** |
| Non-revision occurrences | **41** |
| Revision objects / occurrences | **218 / 221** |
| Serialized (non-revision) | **0** |

Primary future correction scope: **41 non-revision objects** (postmeta-heavy; exclude revisions from primary fix). **No replacements this wave.**

---

## 9. Site / Environment Residue

| Item | Value | Class |
|------|-------|-------|
| `blogname` | «…локальная разработка» | migration residue |
| `blogdescription` | empty | OK for phase |
| `home` / `siteurl` | `http://shpigovsky.beget.tech` | final-domain deferred |
| `WP_DEBUG` | true | migration residue |
| `WP_ENVIRONMENT_TYPE` | local | migration residue |
| DB host model | localhost | correct for temporary production phase |
| Prefix / charset | `fp02_` / utf8 | correct for phase |

No fixes applied.

---

## 10. WP Admin

| Check | Result |
|-------|--------|
| Recreated account exists | **YES** (`mars`, ID 3, registered 2026-08-14) |
| Administrator capability (DB) | **YES** |
| HTTP login | **FAIL** — secrets password **MISMATCH** vs `$wp$` hash |
| Plugins/Themes/ACF/WPilot/General UI | **not re-inspected via HTTP** (login blocked) |
| Writes | **none** |

Marker: `MARS WP ADMIN ACCESS REBASELINED` — **DB role only**; HTTP inspection pending operator password sync in `secrets.local.md`.

---

## 11. WPilot

| Field | State |
|-------|-------|
| Installed FS version | **0.3.0** |
| DB plugin_version / schema | **0.3.0 / 0.2.0** |
| Current global baseline | **0.3.2 / 0.3.2-RC1** |
| Active | yes |
| `bridge_enabled` | true |
| `write_enabled` | **false** |
| `dev_confirmed` | true |
| `emergency_disabled` | false |
| Token | present **hash-only**; plain client token **NO**; local prod token file **NO** |
| Future auth | **`TOKEN REISSUE REQUIRED`** |
| REST | `wpilot/v1` |
| Package SHA | matches expected `d55c19d6…` |
| Upgrade safety | **SAFE** (no production-only WPilot mods) |
| Upgrade executed | **no** |

---

## 12. Public Frontend

All required routes smoke (Beget antibot cookie): **HTTP OK**; no visible PHP notices; no real broken shortcodes after refined check; theme CSS/JS present.

| Route | Status |
|-------|-------:|
| `/` | 200 |
| `/o-centre/` | 200 |
| `/o-centre/programma-lecheniya/` | 200 (program cards markup present) |
| `/o-centre/programma-lecheniya/prostranstvo-vosstanovleniya/` | 200 |
| `/uslugi/` | 200 |
| `/uslugi/zavisimosti/` | 200 |
| Comfort leaf (alcohol service) | 200 — comfort + Fancybox **yes** |
| `/kontakty/` | 200 |
| `/blog/` | 200 |
| `/otzyvy/` | 200 |
| search `?s=лечение` | 200 |
| invalid 404 probe | **404** |

---

## 13. Production Authority

Confirmed:

* `NEW BEGET DB = LIVE CONTENT / ADMIN AUTHORITY`
* `BEGET FILESYSTEM = LIVE RUNTIME TRUTH`
* `LOCAL WORDPRESS TREE = CODE / SOURCE AUTHORITY`
* `PREVIOUS PROD-P04-FU01 = HISTORICAL PRE-REIMPORT BASELINE`
* `NO OLD DB RESTORE OR LOCAL DB OVERWRITE WITHOUT EXPLICIT OPERATOR APPROVAL`
* All writes still **closed by policy**

---

## 14. Evidence

`REPORTS/evidence/prod-p04-fu02-post-reimport-rebaseline/`

* `production-source-parity-manifest.json`
* `production-db-baseline.json`
* `pre-vs-post-reimport-diff.json`
* `migration-residue-map.json`
* `wpilot-state.json`
* `frontend-route-matrix.json`
* plus: `access-revalidation.json`, `runtime-identity.json`, `environment-residue.json`, `acf-json-reconcile.json`, `wp-admin-rebaseline.json`, `wp-admin-password-check.json`, `imported-content-delta.json`, `content-inventory.json`, `recent-content-modified.json`, `material-css-drift-review.json`, `authority-transition.json`, `session-summary.json`

---

## 15. Secret Safety

* exposed values in tracked docs/evidence: **0**
* tracked secrets: **0**
* password hash values: **not printed**

---

## 16. Git

* commit: **none**
* push: **none**
* foreign WIP: **untouched** (preflight noted existing staged entries + unpushed commits on branch — not modified)

---

## 17. Next Wave

Not full green for Admin HTTP. Recommended sequence:

1. **Operator:** update `secrets.local.md` `wordpress_password` to the password set when recreating `mars` (or reset WP password and sync secrets). Re-run Admin login proof.
2. Then: **`PROD-P05 — WPilot 0.3.2-RC1 Exact Upgrade + Token Reissue + Authenticated READ Gate`**  
   (upgrade method remains **SAFE**; `write_enabled` must stay false; token reissue required).

Product code reconciliation for reimport: **not required** (`REIMPORT PRODUCT CODE PARITY CLEAN`).

```text
FP-0002 POST-REIMPORT PRODUCTION BASELINE ESTABLISHED — IMPORTED CONTENT PRESERVED AS LIVE DB AUTHORITY — FILESYSTEM/DB ACCESS REVALIDATED — WP ADMIN HTTP PENDING PASSWORD SYNC — READY FOR CONTROLLED WPILOT UPGRADE/AUTH GATE AFTER ADMIN CREDENTIAL FIX
```
