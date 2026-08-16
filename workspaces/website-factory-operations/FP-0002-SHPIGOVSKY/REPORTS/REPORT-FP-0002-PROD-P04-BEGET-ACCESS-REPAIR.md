# REPORT — FP-0002 PROD-P04 Beget Access Repair

**Date:** 2026-08-13  
**Host:** `http://shpigovsky.beget.tech/`  
**Canonical domain:** `shpigovsky.ru` (`DNS_CUTOVER = DEFERRED`)  
**Evidence:** `REPORTS/evidence/prod-p04-beget-access-repair/`

```text
OPERATOR ACTION REQUIRED — FILESYSTEM ACCESS REBIND
PRODUCTION DB SELECT PROVEN — SSH_LOCAL_MYSQL
REAL WORDPRESS FILESYSTEM READ NOT PROVEN
NO PRODUCTION PRODUCT MUTATIONS
NO COMMIT / NO PUSH
```

---

## 1. Status

* **PARTIAL / OPERATOR ACTION REQUIRED**
* hosting access changes: **none by agent** (Beget panel credentials not filled; FTP directory cannot be changed from this contour)
* production file changes: **0**
* DB writes: **0**
* WordPress writes: **0**
* WPilot writes: **0** (token not reissued; `write_enabled=false`)
* commit/push: **none**

Desired end-state is **not** fully reached: real WordPress filesystem READ remains blocked by account jail. Production DB SELECT **is** proven.

---

## 2. Beget Domain → Filesystem Mapping

| Item | Result |
|------|--------|
| Temporary host | `http://shpigovsky.beget.tech/` — **CURRENT LIVE RUNTIME** (HTTP serves WordPress; `home`/`siteurl` match) |
| Actual WordPress root | `/home/s/shpigovsky/shpigovsky.ru/public_html` |
| `shpigovsky.beget.tech` filesystem folder | `/home/s/shpigovsky/shpigovsky.beget.tech/public_html` — Beget placeholder (`index.php` + `cgi-bin` only) |

**Mapping classification:** `WEB_VHOST_ALIAS_TO_SHPIGOVSKY_RU_SITE` + `SEPARATE_PLACEHOLDER_FILESYSTEM_FOR_BEGET_TECH`.

This is **not** a filesystem mirror. The technical hostname is attached at the **webserver/vhost** layer to the `shpigovsky.ru` WordPress site. The `beget.tech` site resource remains an empty default site. The MARS FTP/SSH user was bound to that **wrong site resource**.

Existing ACL on the real docroot (names only): `shpigovsky` (account owner) and `shpigovsky__shpigovsky3ru__6s` (Beget site-scoped FTP user). `shpigovsky_mars` is **not** on that ACL.

---

## 3. Filesystem Credential

| Field | Value |
|-------|-------|
| Protocol | FTP :21 (configured) + SSH :22 (same account) |
| User | `shpigovsky_mars` |
| Authentication | **PASS** (FTP and SSH) |
| Actual root | `/home/s/shpigovsky/shpigovsky.beget.tech/public_html` |
| WordPress tree | **NOT READABLE** |
| Result | `FILESYSTEM AUTH = PROVEN` / `REAL WORDPRESS FILE ACCESS = BLOCKED BY ACCOUNT BINDING / JAIL` |

No password.

Beget KB: additional FTP accounts get their directory **at creation**. After creation the panel only allows SSH on/off, password change, or delete — **no directory edit**. Rebinding `shpigovsky_mars` therefore means **create new** (preferred) or **delete + recreate**.

---

## 4. Operator Action

**Required for filesystem only.** Database operator action: **NONE**.

Do **not** paste passwords into chat. After the change, reply: `FILESYSTEM ACCESS REBOUND`.

### Exact Beget UI path

1. Open **https://cp.beget.com/ftp**  
   (Панель управления Beget → **FTP** / «Управление FTP-аккаунтами»).
2. In the **lower table of sites**, select the row for **`shpigovsky.ru`**  
   (directory class `shpigovsky.ru` / `public_html`).  
   **Do not** use the row **`shpigovsky.beget.tech`**.

### Exact change (preferred)

3. Click the **create FTP account** button opposite **`shpigovsky.ru`**.
4. Login suffix: e.g. `marswp` → resulting user `shpigovsky_marswp`.  
   Do **not** reuse `shpigovsky_mars` unless you first delete it (Beget cannot change an existing FTP user’s directory).
5. Directory: the prefilled **`shpigovsky.ru` site root** (`…/shpigovsky.ru/public_html`).
6. **Enable SSH** (needed for SFTP and for the already-proven SSH-local MySQL path from a correctly bound account).
7. Set/generate a password. Do not use the Beget master-account password.

### Alternatives (only if preferred)

* **A.** Delete `shpigovsky_mars` and recreate it bound to `shpigovsky.ru` with SSH on.  
* **B.** Reset the password of existing site user `shpigovsky__shpigovsky3ru__6s` (already on the real docroot ACL) and use that account.

### Local fields to update

Enter values only in:

`X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md`

| Field | What to put |
|-------|-------------|
| `ftp_or_sftp_username` | new (or rebound) username |
| `ftp_or_sftp_password` | new password |
| `ftp_or_sftp_remote_root_or_initial_directory` | new jail; keep the old `/shpigovsky.beget.tech/public_html/` marked **OBSOLETE** |
| `ssh_username` | same user |
| `ssh_password_or_key_reference` | same password |
| `ssh_available` | `yes` |

Do **not**:

* open remote MySQL or add the operator IP (SSH-local SELECT already works);
* change DNS / SSL / site title / WPilot / content;
* paste credentials into chat.

---

## 5. Production WordPress Paths

| Role | Path | FS read |
|------|------|---------|
| Docroot | `/home/s/shpigovsky/shpigovsky.ru/public_html` | **NO** (exists; ACL deny) |
| Theme | `{docroot}/wp-content/themes/shpigovsky` | **NO** (HTTP/Admin/DB identity **YES**) |
| `shpigovsky-core` | `{docroot}/wp-content/plugins/shpigovsky-core` | **NO** (active in DB `active_plugins`) |
| ACF JSON | `{docroot}/wp-content/acf-json` | **NO** |
| WPilot | `{docroot}/wp-content/plugins/metacode-wpilot` | **NO** (active **0.3.0**) |
| Uploads | `{docroot}/wp-content/uploads` | **NO** |

`wp-config.php` exists (3329 B, mode 0600, owner `shpigovsky`) and is **not readable**. Safe DB metadata was taken from **SELECT**, not from wp-config.

---

## 6. DB Connection Model

**`SSH_LOCAL_MYSQL`**

Why:

* Beget default is **localhost-only** DB access (KB + Polygon/OCPilot precedents).
* P03 remote `shpigovsky.beget.tech:3306` was TCP-open but auth **1045** from the operator IP — that does **not** prove the password is wrong.
* OCPilot SITE-001: Beget 1045 for external hosts is expected without allowlisting.
* This wave: SSH as `shpigovsky_mars` → tunnel to `127.0.0.1:3306` → SELECT **PASS** as `shpigovsky_main@localhost`.
* Least privilege: **do not** expose remote MySQL or add an operator IP.

Rejected: `REMOTE_MYSQL` (unnecessary public exposure). phpMyAdmin left as operator/manual fallback (`https://dream.beget.com/phpMyAdmin`).

---

## 7. DB Read Proof

* **PASS** — `PRODUCTION DB SELECT PROVEN`
* prefix: **`fp02_`**
* charset / collation: **`utf8mb4` / `utf8mb4_unicode_ci`**
* MySQL: **8.4.8-8-beget-1-2** on `dream.beget.ru` (`@@port` 3307 internal; tunnel used 3306)
* database: `shpigovsky_main`
* core WP tables: **10/10 present** (`options`, `posts`, `postmeta`, `users`, `usermeta`, `terms`, `term_taxonomy`, `term_relationships`, `comments`, `commentmeta`)
* table count: **14**
* counts: posts_all **1085**; publish posts **16**; publish pages **25**; all publish **857**; users **3**
* ACF field-group rows: **39** (22 unique titles; historical duplicates present)
* WPilot options (no token/hash values): version **0.3.0**, schema **0.2.0**, bridge **on**, write **off**, emergency **off**, `dev_confirmed` **true**, token hash **present/redacted**

Active plugins (DB `active_plugins`): ACF Extended PRO, ACF PRO, Classic Editor, `metacode-wpilot`, `shpigovsky-core`. P03 Admin also visually noted Akismet + Hello Dolly — not re-opened this wave; DB option is the SELECT authority here.

---

## 8. WordPress Identity

| Field | Value |
|-------|-------|
| `home` | `http://shpigovsky.beget.tech` |
| `siteurl` | `http://shpigovsky.beget.tech` |
| `blogname` | `Шпиговский — локальная разработка` |
| `blogdescription` | empty |
| Theme | `shpigovsky` / `shpigovsky` |
| `db_version` | `61833` |
| Exact WP core string | **SAFE UNKNOWN** (wp-includes unread) |

Temporary-domain state: **aligned**. Final domain `shpigovsky.ru` remains **DEFERRED**. Do not change.

Future migration-tail (not this wave): replace leftover `shpigovsky.test` URLs in content/ACF; later change `blogname`; DNS cutover is a separate charter.

---

## 9. Migration Residue

Needle: `shpigovsky.test` (includes `http://shpigovsky.test`).

| Scope | Objects | Occurrences |
|-------|--------:|------------:|
| All targeted rows (incl. revisions) | **155** | **158** |
| Non-revision (fix-relevant) | **43** | **46** |
| Revisions (can ignore for public HTML) | **112** | **112** |

Non-revision by storage:

| Storage | Count | Serialized |
|---------|------:|:----------:|
| `fp02_postmeta` URL/ACF fields | 36 objects | 1 (`section_nature_text_blocks` on service `#73`) |
| `fp02_posts.post_content` | 5 | 0 |
| `fp02_options` | 2 | 0 |

Material non-revision owners (later fix, **no mutation now**):

* Page `#4` Главная — `home_genotyping_link_url`, `home_why_us_items_{0-3}_url`
* Services `#73/#74/#75/#77–87/#314–316/#1011–1013/#1016–1019/#1047–1051` — `*_approach_more_url` / genotyping URL
* Options: `fp02-block-comfort_comfort_all_link_url`, `fp02-block-specialists_specialists_all_link_url`
* Post `#750` (blog) — 4 hits in `post_content`
* ACF field posts `#1510/#1645/#1647/#1658` — default-value residue in `post_content`

`home` / `siteurl` are **not** `.test` leftovers.

---

## 10. Production Filesystem Parity

Full SHA inventory: **BLOCKED** (docroot unread).

| Class | Count |
|-------|------:|
| MATCH | **SAFE UNKNOWN** on disk; P03 public CSS/JS sample **5 MATCH / 0 divergent** |
| Known intentional source-only ACF JSON | **8** documented in `REPORTS/ACF-SOURCE-RUNTIME-DISPOSITION-FP-0002-V9-STABLE-V1.md` — **not** classified as migration defects |
| Production-only | **SAFE UNKNOWN** |
| Local-only | **SAFE UNKNOWN** |
| Divergent | **SAFE UNKNOWN** |

Material known drift without FS: WPilot package **0.3.0 vs 0.3.2-RC1**; FTP user bound to the wrong site; `shpigovsky.test` content residue; `blogname` still «локальная разработка».

Do not sync.

---

## 11. WPilot

| Field | Value |
|-------|-------|
| Installed version | **0.3.0** (Admin P03 + DB option P04) |
| Schema | **0.2.0** |
| Current baseline | **0.3.2 / 0.3.2-RC1** |
| Exact package | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.2-rc1.zip` |
| SHA | `d55c19d6ea1a55cd145e9b67c42ca201c30e4356f08d8cf3932ef6a5ebc80934` (P03 reverified) |
| Production plugin file inventory | **NOT READABLE** |
| Upgrade delta known | **PACKAGE YES / PRODUCTION FILES NO** |
| Upgrade performed | **NO** |
| Token reissued | **NO** |
| Recommended upgrade method | Native WP Admin **Replace current with uploaded** (Polygon P07 precedent; no deactivate/reactivate) |

`write_enabled=false` at all times. P05 must not start until filesystem READ exists (to verify the replaced plugin files).

---

## 12. Access Matrix

| Surface | READ | WRITE |
|---------|------|-------|
| Public HTTP | proven | n/a |
| WP Admin | inspection proven (P03) | closed |
| FTP/SSH | auth proven; WP files **closed** | closed |
| DB | **SELECT proven** (`SSH_LOCAL_MYSQL`) | closed |
| WPilot authenticated REST | not proven | closed (`write_enabled=false`) |
| Beget panel | not filled | operator HITL for FTP rebind only |
| DNS / SSL | n/a | forbidden |
| Remote MySQL | not used | not opened |

---

## 13. Secret Safety

* exposed values: **0**
* tracked secrets: **0**
* token / token_hash printed in tracked artifacts: **0**
* wp-config copy: **0**
* DB dump: **0**

Local-only `secrets.local.md` updated with non-secret DB metadata (`localhost` / `3306` / `fp02_` / `utf8mb4`). Password fields unchanged.

---

## 14. Exact Docs/Evidence Changed

**Tracked**

* `DOCS/PRODUCTION/FP-0002-PRODUCTION-ACCESS-MATRIX-v1.md`
* `DOCS/PRODUCTION/FP-0002-CREDENTIAL-REFERENCE-MAP-v1.md`
* `DOCS/PRODUCTION/FP-0002-MARS-PRODUCTION-CONNECTION-PROFILE-v1.md`
* `DOCS/PRODUCTION/FP-0002-PRODUCTION-SITE-PASSPORT-BEGET-v1.md`
* `PROJECT-STATUS.md`
* `REPORTS/REPORT-FP-0002-PROD-P04-BEGET-ACCESS-REPAIR.md`
* `REPORTS/evidence/prod-p04-beget-access-repair/*`

**Local-only (gitignored `/local/`)**

* `X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md` (DB host/port/prefix/charset + obsolete FTP-root note)
* `X:\AI MARS\local\sites\shpigovsky-production\site-profile.json` (capability flags / last validation)

---

## 15. Git

* no commit
* no push
* foreign WIP untouched (including pre-existing staged `projects/client-ops-reporting-bridge/` files)
* `git add` / stash / reset / clean / restore: **not used**

Preflight: cwd `X:\AI MARS`, volume `AI WS`, branch `mars/canonical-post-recovery`. Staged/unpushed foreign work existed before this wave and was not modified.

---

## 16. Next Wave

**Do not start PROD-P05 yet.**

Missing operator action (filesystem only):

```text
FILESYSTEM ACCESS REBIND
Beget → https://cp.beget.com/ftp
Create (or recreate) a dedicated FTP+SSH user on the shpigovsky.ru row
Bind to …/shpigovsky.ru/public_html
Update secrets.local.md locally
Reply: FILESYSTEM ACCESS REBOUND
```

After that, the same PROD-P04 scope may be rerun to prove WordPress filesystem READ + SHA baseline. Only then:

`PROD-P05 — WPilot 0.3.2-RC1 Exact Upgrade + Token Reissue + Authenticated READ Gate`

Final desired state is **not** reached:

`FP-0002 REAL BEGET WORDPRESS FILESYSTEM READ PROVEN` — **NO**  
`PRODUCTION DB SELECT PROVEN` — **YES**  
`FULL SOURCE/PRODUCTION BASELINE KNOWN` — **NO** (FS unread)  
`READY FOR EXACT WPILOT UPGRADE/AUTH GATE` — **NO** (blocked on filesystem READ)

---

## Execution safety

- cwd: `X:\AI MARS`
- scope lock honored: yes (`X:\AI MARS` docs/evidence + gitignored `X:\AI MARS\local\…`)
- destructive ops: none
- protected zone touch: production inspected read-only; no `wp-config` edit; no DNS; no WPilot write flag; no remote MySQL exposure

---

*PROD-P04 · PARTIAL / OPERATOR ACTION REQUIRED · no secrets · no commit · no push.*
