# REPORT — FP-0002 PROD-P03 Production Access Validation

**Date:** 2026-08-13  
**Host:** `http://shpigovsky.beget.tech/`  
**Canonical domain:** `shpigovsky.ru` (`DNS_CUTOVER = DEFERRED`)  
**Evidence:** `REPORTS/evidence/prod-p03-production-access-validation/`

---

## 1. Status

* **PARTIAL**
* production mutations: **none** (no uploads, no SQL writes, no Admin saves, no WPilot option/token/flag changes, no DNS)
* DB writes: **0**
* WP Admin writes: **0** operator saves (WordPress core may record last_login/session as a login side effect)
* filesystem writes: **0**
* WPilot writes: **0** (authenticated REST not called)
* commit/push: **none**

Desired end-state is **not** fully reached: filesystem+DB WordPress read and WPilot authenticated READ remain closed.

---

## 2. Credential Validation

| Class | Completeness | Auth | Notes |
|-------|--------------|------|-------|
| Filesystem | **PRESENT** (FTP protocol/host/port/user/password/root) | **PASS** | Protocol **ftp** :21. Passive placeholder unused; PASV used. Configured initial dir 550 — actual jail is `/` |
| DB | **PARTIAL** — name/user/password PRESENT; host/port/prefix/charset **MISSING** | **FAIL** (1045) | See §5 |
| WP Admin | **PRESENT** | **PASS** | User `mars`. Beget antibot cookie `beget=begetok` required |
| SSH optional | Fields PRESENT (`available` flag still placeholder) | **PASS** | Same account/jail as FTP |
| Beget optional | **NOT REQUIRED / MISSING** | not attempted | Needed later to rebind FTP user + remote MySQL ACL |

No secret values in this report.

---

## 3. Production Runtime Paths

| Role | Path | Class |
|------|------|-------|
| Account-visible root (this FTP/SSH user) | `/home/s/shpigovsky/shpigovsky.beget.tech/public_html` | **VERIFIED** — Beget placeholder `index.php` + `cgi-bin` only |
| WordPress docroot | `/home/s/shpigovsky/shpigovsky.ru/public_html` | **VERIFIED** exists (`wp-config.php` stat 3329 B, 0600); **NOT READABLE** by `shpigovsky_mars` |
| wp-content | `{docroot}/wp-content` | **SAFE UNKNOWN** on FS (Permission denied) |
| Theme | expected `wp-content/themes/shpigovsky` | **VERIFIED** via public HTTP + Admin; FS unread |
| shpigovsky-core | expected `wp-content/plugins/shpigovsky-core` | **VERIFIED** active Admin; FS unread |
| ACF JSON | expected `wp-content/acf-json` | **SAFE UNKNOWN** on FS; Admin groups visible |
| WPilot | expected `wp-content/plugins/metacode-wpilot` | **VERIFIED** active Admin + REST; FS unread |
| uploads | expected `wp-content/uploads` | **SAFE UNKNOWN** on FS |

ACL on real docroot grants `shpigovsky` and `shpigovsky__shpigovsky3ru__6s` only — not `shpigovsky_mars`.

---

## 4. Filesystem Parity

Full inventory/SHA of theme, `shpigovsky-core`, ACF JSON, and WPilot plugin files: **not possible** (no read ACL).

Public HTTP sample (5 source-owned theme files): **5 MATCH / 0 divergent**.

| Classification | Count |
|----------------|------:|
| MATCH (public CSS/JS sample) | 5 |
| Known intentional source-only ACF JSON | not re-verified on disk (Admin shows PHP-registered groups including historical duplicates) |
| Production-only product files | **SAFE UNKNOWN** |
| Local-only | **SAFE UNKNOWN** |
| Divergent (hashed sample) | 0 |

Admin version strings:

* `shpigovsky-core` production = local `0.3.3-v9-06e25a-source` (**MATCH** label only)
* `metacode-wpilot` production **0.3.0** vs source **0.3.2 / 0.3.2-RC1** (**OLDER**)

Material drift that **is** known without FS: WPilot package generation; FTP user bound to the wrong Beget site folder; public `shpigovsky.test` CTA hrefs (content/theme residue — not repaired).

Do not copy in either direction. Future rule remains `PRODUCTION FETCH → RECONCILE → SOURCE CANON → DEPLOY` once FS read exists.

---

## 5. Production Database Identity

* host classification: secrets **MISSING**; convention probe `shpigovsky.beget.tech:3306` **TCP OPEN**
* DB name (from secrets, safe): `shpigovsky_main`
* prefix: **SAFE UNKNOWN** (not in secrets; wp-config unread)
* charset/collation: **SAFE UNKNOWN**
* WP tables / counts: **not queried** (AUTH FAIL 1045 from operator IP)
* SELECT proven: **NO**
* Likely cause: missing `db_host` and/or Beget remote-MySQL ACL does not allow this IP

No secrets/user data.

---

## 6. WordPress URL State

| Field | Value |
|-------|-------|
| `home` | `http://shpigovsky.beget.tech` |
| `siteurl` | `http://shpigovsky.beget.tech` |
| Temporary host alignment | **YES** — matches working Beget host |
| Final domain `shpigovsky.ru` | **DEFERRED** — not forced |
| REST base | `/wp-json/` · WPilot `wpilot/v1` |

Not a `shpigovsky.test` home/siteurl leftover. Hardcoded `.test` links remain in rendered HTML (see §7).

---

## 7. Migration Residue

Public HTML sample (5 routes): **9** `shpigovsky.test` occurrences.

| Page | Count | Ownership (public HTML) |
|------|------:|-------------------------|
| `/` | 7 | content/admin or theme hrefs (CTA / genotyping / services) |
| `/o-centre/` | 1 | specialists “all” link |
| `/uslugi/` | 1 | comfort gallery link |
| `/kontakty/` | 0 | — |
| `/wp-login.php` | 0 | — |

Representative safe fragments (no secrets): `http://shpigovsky.test/uslugi/zavisimosti/…`, `…/specyalisty/`, `…/o-centre/galereya-o-dome/`.

DB object-ID map: **not available** (SELECT blocked). Classification of DB rows remains **SAFE UNKNOWN** pending DB read.

Site title: `blogname` = **«Шпиговский — локальная разработка»**; `blogdescription` empty. Intended later correction — **not changed**.

Also visible in Admin (not mutated): Hello Dolly + Akismet active; duplicate ACF field-group titles (historical local pattern).

---

## 8. WP Admin

* auth: **PASS**
* role/capability class: **Administrator** (`mars`)
* inspection: Dashboard, Plugins, Themes, General Settings, Profile, Users (role only), WPilot screen, ACF Field Groups
* mutations: **none** (no save, no dismiss, no plugin/theme update)

Beget serves a JS cookie gate (`beget=begetok`) before the real login form.

---

## 9. WPilot Installed Version

| Field | Production | Current baseline |
|-------|------------|------------------|
| Version | **0.3.0** | **0.3.2** |
| Release | not `0.3.2-RC1` | **0.3.2-RC1** |
| Schema | **0.2.0** | **0.2.0** |
| REST namespace | **wpilot/v1** | **wpilot/v1** |
| Active | **yes** | — |

* source/package parity: **OLDER** (file SHA of production plugin **SAFE UNKNOWN**)
* ZIP `metacode-wpilot-v0.3.2-rc1.zip` SHA **reverified** `d55c19d6ea1a55cd145e9b67c42ca201c30e4356f08d8cf3932ef6a5ebc80934`
* upgrade needed: **YES**
* upgrade performed: **NO** — **STOP before upgrade**

`WPILOT UPGRADE NOT REQUIRED` does **not** apply.

---

## 10. WPilot Settings

From public ping (backend-public) + Admin version screen:

* bridge: **true**
* write: **false** (no `SAFETY BLOCKER — WRITE ENABLED`)
* dev_confirmed: **true**
* emergency: **false**
* token present: **yes** (generated / hash only)
* no secret value printed

Pre-existing Admin last failure `auth_missing` at `2026-08-12 20:09:14 UTC` — not caused by this wave.

---

## 11. WPilot Token Reconcile

```text
TOKEN ROTATION/REISSUE REQUIRED
```

CASE B: only `token_hash` is stored (`wp_hash_password`). No recoverable plaintext. Local prod file **not** created. Local DEV token **not** tested against production.

---

## 12. Authenticated READ Proof

* attempted: **NO**
* routes: none (public `GET /wp-json/wpilot/v1/ping` **200** is not proof)
* statuses: n/a
* site identity: public ping + `/wp-json/` name/url match Shpigovsky Beget host
* result: **NOT PROVEN**

Blockers: no client token; authenticated GET mutates connection tracker; installed version OLDER — stop before upgrade/auth.

Milestone `AUTHENTICATED READ CONNECTION TO MARS PROVEN` is **not** reached.

---

## 13. Runtime Checkout

* **deferred**
* path: `X:\AI MARS STORAGE\runtime-checkouts\fp-0002-shpigovsky-production\repo`
* branch/commit: n/a
* reason: P02 policy (no scheduled job yet) still applies; this FTP/SSH account cannot monitor the WP docroot; do not clone from dirty `X:\AI MARS`

---

## 14. Access Matrix

| Surface | Proven now |
|---------|------------|
| Public HTTP | READ yes |
| WP Admin | inspection yes; write no |
| FTP/SSH | auth yes; WP file read **no** |
| DB | SELECT **no** |
| WPilot | public ping yes; authenticated READ **no**; write **no** |
| Beget panel | not filled |
| DNS | write forbidden |

---

## 15. Production Filesystem Baseline

* manifest: `REPORTS/evidence/prod-p03-production-access-validation/production-filesystem-baseline.json`
* files counted: **5** (public HTTP only)
* parity verdict: **PARTIAL MATCH on hashed sample; full product baseline BLOCKED**

This is **not** yet a complete post-migration filesystem baseline.

---

## 16. SAFE UNKNOWN Remaining

* WordPress core exact version
* table prefix / charset / post/user counts
* DB locations of `shpigovsky.test` residues (IDs/meta keys)
* production theme/plugin/ACF JSON full SHA inventory
* production WPilot file hashes / RELEASE_LABEL beyond Admin `0.3.0`
* HTTPS/SSL on beget.tech
* SMTP, cache, cron, PHP OPcache
* whether web vhost for `shpigovsky.beget.tech` aliases `shpigovsky.ru/public_html` (HTTP serves WP while FTP jail does not)

---

## 17. Security / Secret Check

* secret values in report: **0**
* tracked secrets: **0**
* token exposed: **0**
* wp-config contents: **not read** (no ACL)

---

## 18. Exact Files Changed

**Tracked**

* `DOCS/PRODUCTION/FP-0002-PRODUCTION-ACCESS-MATRIX-v1.md`
* `DOCS/PRODUCTION/FP-0002-CREDENTIAL-REFERENCE-MAP-v1.md`
* `DOCS/PRODUCTION/FP-0002-MARS-PRODUCTION-CONNECTION-PROFILE-v1.md`
* `DOCS/PRODUCTION/FP-0002-PRODUCTION-SITE-PASSPORT-BEGET-v1.md`
* `DOCS/PRODUCTION/FP-0002-WPILOT-CONNECTION-STATE-v1.md`
* `DOCS/PRODUCTION/FP-0002-WPILOT-INSTALL-READINESS.md`
* `WORDPRESS/SOURCE-AUTHORITY.md`
* `PROJECT-STATUS.md`
* `REPORTS/REPORT-FP-0002-PROD-P03-PRODUCTION-ACCESS-VALIDATION.md`
* `REPORTS/evidence/prod-p03-production-access-validation/*`

**Local-only (paths only; gitignored `/local/`)**

* `X:\AI MARS\local\sites\shpigovsky-production\site-profile.json` (capability flags / last validation)
* helper scripts/status JSON under the same folder (not tracked)
* WPilot prod token file: **not created**

---

## 19. Git

* commit: **none**
* push: **none**
* foreign WIP: **untouched** (including pre-existing staged client-ops files)
* `git add` / stash / reset / clean / restore: **not used**

Preflight: cwd `X:\AI MARS`, volume `AI WS`, branch `mars/canonical-post-recovery`. Staged/unpushed foreign work existed before this wave and was not modified.

---

## 20. Next Recommended Wave

Primary (access failure blocking FS + DB):

**`PROD-P04 — Production Filesystem Account Rebind + DB Remote Access Repair`**

Operator (Beget panel / HITL):

1. Bind `shpigovsky_mars` (or issue the existing site FTP user) to `/home/s/shpigovsky/shpigovsky.ru/public_html`.
2. Fill `db_host` / `db_port` / `db_table_prefix` / `db_charset` in `secrets.local.md`.
3. Allowlist the operator IP for remote MySQL (1045 from this workstation).

Then, because WPilot is **outdated**:

**Exact-package upgrade gate** to `0.3.2-RC1` (ZIP SHA above) — **before** auth.

Then, because token client copy is unavailable:

**`WPilot Token Reissue / Auth Gate`** — generate once in Admin, store only at `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token`, prove GET `site-info` (accepting that current plugin writes connection metadata on success). Leave `write_enabled=false`.

Do **not** start migration-tail URL/title fixes until FS+DB read (or Admin-only content charter) exists.

---

## Execution safety

- cwd: `X:\AI MARS`
- scope lock honored: yes (`X:\AI MARS` docs/evidence + gitignored `X:\AI MARS\local\…`)
- destructive ops: none
- protected zone touch: production inspected read-only; no `wp-config` edit; no DNS; no WPilot write flag

---

*PROD-P03 · PARTIAL · no secrets · no commit · no push.*
