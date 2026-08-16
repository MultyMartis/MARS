# FP-0002 — MARS Production Connection Profile v1

**Wave:** PROD-P05-FU01 — WPilot upgrade / token / authenticated READ (**PASS**)  
**Profile ID:** `FP-0002-SHPIGOVSKY-PROD`  
**Date:** 2026-08-14  
**Status:** **COMPLETE — WPILOT 0.3.2-RC1 ACTIVE — AUTHENTICATED READ PROVEN — TOKEN STORED LOCALLY — WRITE DISABLED**  
**Rule:** Capabilities, paths, and authorization only — **no secret values**.

```text
FP-0002 MARS PRODUCTION CONNECTION COMPLETE
WPILOT 0.3.2-RC1 ACTIVE
AUTHENTICATED READ PROVEN
FILESYSTEM/DB/WP ADMIN PROVEN
PRODUCTION TOKEN STORED LOCALLY
WRITE DISABLED
DNS_CUTOVER = DEFERRED
```

This is the **main production connection entry point** for Shpigovsky on Beget.

---

## 1. Site identity

| Field | Value |
|-------|-------|
| Factory project | FP-0002 — Шпиговский |
| Site alias | `shpigovsky-production` |
| Current production URL | `http://shpigovsky.beget.tech/` |
| Future canonical domain | `shpigovsky.ru` |
| DNS cutover | **`DEFERRED`** |
| Hosting provider | Beget |
| Environment | PRODUCTION (pre-DNS-cutover; **post operator re-import**) |
| Project locus | `X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\` |
| Operator ownership | MetaCODE / MARS operator (human-supervised) |

---

## 2. Verified runtime paths

| Role | Path / URL | Class |
|------|------------|-------|
| HTTP working host | `http://shpigovsky.beget.tech/` | **VERIFIED** |
| WordPress `home` / `siteurl` | `http://shpigovsky.beget.tech` | **VERIFIED** |
| FTP/SSH account home | `/home/s/shpigovsky/shpigovsky.ru/public_html` | **VERIFIED** |
| Production WordPress docroot | `/home/s/shpigovsky/shpigovsky.ru/public_html` | **VERIFIED READ** |
| Theme | `wp-content/themes/shpigovsky` | FU02 SHA baseline |
| `shpigovsky-core` | `wp-content/plugins/shpigovsky-core` | FU02 |
| ACF JSON | `wp-content/acf-json` | FU02 |
| WPilot | `wp-content/plugins/metacode-wpilot` | **0.3.2 / 0.3.2-RC1** active; 32 files MATCH package; write **false** |
| Uploads | `wp-content/uploads` | exists / readable |
| WordPress core | `wp-includes/version.php` | **7.0.4** |

Filesystem: **SSH preferred**. WRITE closed by policy except the chartered P05 plugin replace (done).

---

## 3. Access surfaces (no secrets)

| Surface | Transport | Credential source (path only) | FU01 state |
|---------|-----------|-------------------------------|------------|
| Public HTTP | HTTP | N/A | READ **PROVEN** |
| WordPress Admin | HTTP admin UI (+ Beget `beget=begetok`) | `secrets.local.md` → WORDPRESS ADMIN | HTTP login **PROVEN**; Administrator **PROVEN** |
| WPilot REST | `wpilot/v1` + `X-WPilot-Token` | `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token` | Authenticated READ **PROVEN**; WRITE **DISABLED** |
| Filesystem | SSH preferred (FTP ok) | `secrets.local.md` | READ **PROVEN**; WRITE **CLOSED** |
| Database | **SSH_LOCAL_MYSQL** | `secrets.local.md` | SELECT **PROVEN**; WRITE **CLOSED** |
| DNS | Registrar / Beget DNS | N/A | **DEFERRED** |

Local credential root: `X:\AI MARS\local\sites\shpigovsky-production\` (gitignored `/local/`).

---

## 4. WPilot state

| Field | State |
|-------|-------|
| Plugin | present, **active** |
| Version | **`0.3.2`** |
| Release | **`0.3.2-RC1`** |
| Schema | **`0.2.0`** |
| REST namespace | **`wpilot/v1`** |
| vs baseline `0.3.2 / 0.3.2-RC1` | **CURRENT** |
| Bridge | **enabled** |
| `dev_confirmed` | **true** |
| Token | server hash + **local client file present** |
| Local token path | `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token` |
| Write | **disabled** |
| Emergency | **false** |
| Authenticated READ | **PROVEN** (2026-08-14) |
| Layer B pre-upgrade copy | `X:\AI MARS STORAGE\wpilot\evidence\fp-0002-shpigovsky\prod-p05\pre-upgrade-wpilot-0.3.0\` |
| Layer A (current post-reimport) | **OPERATOR CONFIRMED** |

Canonical package ZIP SHA `d55c19d6ea1a55cd145e9b67c42ca201c30e4356f08d8cf3932ef6a5ebc80934` (reverified FU01; installed).

---

## 5. Database identity

| Field | Value |
|-------|-------|
| Logical name | `shpigovsky_main` |
| Host (operational) | **`localhost`** via SSH tunnel |
| Prefix | **`fp02_`** |
| Charset / collation | **`utf8mb4` / `utf8mb4_unicode_ci`** |
| SELECT proven | **YES** |
| Write | **DISABLED** |
| Authority | **LIVE CONTENT / ADMIN AUTHORITY** |
| Preserve rule | **NO OLD DB RESTORE OR LOCAL DB OVERWRITE WITHOUT EXPLICIT OPERATOR APPROVAL** |

---

## 6. Authority split

| Surface | Authority |
|---------|-----------|
| Theme / `shpigovsky-core` / ACF JSON-PHP | `WORDPRESS/` = **CODE / SOURCE AUTHORITY** |
| Live HTML/behavior / product files on Beget | **LIVE RUNTIME TRUTH** |
| Pages/posts/ACF values/menus/media/SEO | **Current Beget DB** = **LIVE CONTENT / ADMIN STATE** |
| WPilot plugin files | **0.3.2-RC1 package** now live |
| Local `shpigovsky.test` | **LOCAL ACCEPTED REFERENCE** — must not auto-overwrite production |

---

## 7. Default safety posture

```text
WRITE AUTHORIZED = NO
WPILOT write_enabled = false
Filesystem write = disabled
DB write = disabled
DNS write = forbidden
NO OLD DB RESTORE WITHOUT OPERATOR APPROVAL
```

---

## 8. Related production docs

Evidence: `REPORTS/evidence/prod-p05-wpilot-upgrade-auth-gate/`  
Closeout: `REPORTS/REPORT-FP-0002-PROD-P05-FU01-WPILOT-AUTH-CLOSEOUT.md`  
Prior blocked P05: `REPORTS/REPORT-FP-0002-PROD-P05-WPILOT-UPGRADE-AUTH-GATE.md`

---

*Connection Profile v1 · PROD-P05-FU01 PASS · no secrets · write remains disabled.*
