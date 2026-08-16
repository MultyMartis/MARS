# FP-0002 — Production Site Passport (Beget) v1

**Wave:** PROD-P01 onboarding; **updated PROD-P03–P04-FU02**; **updated PROD-P05-FU01** (WPilot 0.3.2-RC1 + authenticated READ)  
**Date:** 2026-08-14  
**Mutations:** P05-FU01 authorized WPilot package replace + one token reissue; business/content writes **0**

```text
CURRENT BEGET DB = LIVE CONTENT / ADMIN AUTHORITY
BEGET FILESYSTEM = LIVE RUNTIME TRUTH
LOCAL WORDPRESS TREE = CODE / SOURCE AUTHORITY
PREVIOUS PROD-P04-FU01 = HISTORICAL PRE-REIMPORT BASELINE
NO OLD DB RESTORE OR LOCAL DB OVERWRITE WITHOUT EXPLICIT OPERATOR APPROVAL
```

---

## Identity

| Field | Value | Evidence class |
|-------|-------|----------------|
| Temporary production URL | `http://shpigovsky.beget.tech/` | **VERIFIED** (public HTTP 200) |
| Canonical public domain | `shpigovsky.ru` | Operator-confirmed future host |
| DNS cutover status | **`DNS_CUTOVER = DEFERRED`** — DNS still on old hosting; do **not** treat `shpigovsky.ru` as Beget authority | Operator-confirmed |
| Environment | Beget production **pre-DNS-cutover** | Operator-confirmed + public probe |
| Working inspection host | `shpigovsky.beget.tech` = **CURRENT BEGET LIVE RUNTIME** | **VERIFIED** |
| Public site name (WP) | `Шпиговский — локальная разработка` | **VERIFIED** via `/wp-json/` + `<title>` — migration leftover naming |

---

## Hosting

| Field | Value | Evidence class |
|-------|-------|----------------|
| Provider | Beget | Operator-confirmed |
| Docroot | `/home/s/shpigovsky/shpigovsky.ru/public_html` | **VERIFIED READ (PROD-P04-FU01)** — FTP/SSH account `shpigovsky_mars` home is this docroot. Prior `beget.tech` placeholder jail **REMOVED / OBSOLETE**. Web host `shpigovsky.beget.tech` still **aliases** this WordPress site at the vhost layer. |
| Webserver | `nginx-reuseport/1.21.1` | **VERIFIED** (response `Server` header) |
| PHP | `PHP/8.3.20` | **VERIFIED** (`X-Powered-By`) |
| SSL / HTTPS on beget.tech | Not usable in this wave (HTTPS requests timed out) | **SAFE UNKNOWN** / unavailable from probe |
| HTTP→HTTPS redirect | Not observed on HTTP working host | **VERIFIED** (HTTP serves 200 without force-HTTPS) |
| WAF / ModSecurity | — | **SAFE UNKNOWN** |
| OPcache | — | **SAFE UNKNOWN** |
| Panel / account IDs | — | **SAFE UNKNOWN** (not requested) |

---

## WordPress

| Field | Value | Evidence class |
|-------|-------|----------------|
| Core version | **`7.0.4`** from `wp-includes/version.php`; `db_version` option **61833** | FS READ + DB SELECT (PROD-P04-FU02) |
| Home / siteurl | `http://shpigovsky.beget.tech` | **VERIFIED** (DB SELECT FU02) |
| Permalinks | Pretty IA routes resolve; option `permalink_structure` = `/blog/%postname%/` | **VERIFIED** (route smoke + DB) |
| REST index | `/wp-json/` **200** | **VERIFIED** (prior waves; not re-broken in FU02 frontend smoke) |
| Public namespaces (sample) | `wp/v2`, `oembed/1.0`, **`wpilot/v1`**, others | **VERIFIED** (prior) |
| Login route | `/wp-login.php`; user `mars` **Administrator**; HTTP login **PASS** (FU01) | **VERIFIED** |
| robots.txt | Default WP-style: `Disallow: /wp-admin/` + `Allow: admin-ajax` — **no** `noindex` for whole site | **VERIFIED** |
| Sitemaps | `/wp-sitemap.xml`, `/sitemap.xml`, `/sitemap_index.xml` → **404** theme 404 page | **VERIFIED** |

---

## Theme / plugin architecture

| Component | Local source known | Production verified |
|-----------|--------------------|---------------------|
| Theme `shpigovsky` | **LOCAL SOURCE KNOWN** under `WORDPRESS/theme/shpigovsky/` | **POST-REIMPORT FS BASELINE (FU02)** — content MATCH (incl. `v9-style.css` LF-normalized); 1 production-only `.BROKEN-MPEGTS.bak` artifact |
| Plugin `shpigovsky-core` | **LOCAL SOURCE KNOWN** version `0.3.3-v9-06e25a-source` | **FU02** — 25 MATCH; no divergent product files |
| ACF model | **LOCAL SOURCE KNOWN** (`WORDPRESS/acf-json/` + PHP) | **FU02** `wp-content/acf-json` — 24 MATCH; 7 documented intentional source-only |
| ACF PRO / other operator plugins | Operator-managed | Active (DB): ACF Extended PRO, ACF PRO, Classic Editor (+ core/WPilot) |
| WPilot `metacode-wpilot` | Source **0.3.2 / 0.3.2-RC1** | **FU01** active **0.3.2 / 0.3.2-RC1**; schema **0.2.0**; write **false**; local token present; authenticated READ **PROVEN** |

---

## DB / content

| Field | Value | Evidence class |
|-------|-------|----------------|
| Operator re-import | Full files + DB replaced on Beget with newer demo/staging version (incl. Olya content edits) | Operator-confirmed; FU02 rebaseline |
| Live content authority | **Current Beget WordPress DB** (supersedes prior PROD-P04 DB inventory) | **FU02** — `NO OLD DB RESTORE WITHOUT EXPLICIT OPERATOR APPROVAL` |
| Prior PROD-P04 / FU01 DB counts | Historical pre-reimport evidence only | Do not merge back |
| DB name / host | `shpigovsky_main` @ **localhost** (SSH-local) | **VERIFIED** SELECT (FU02) |
| Table prefix | **`fp02_`** | **VERIFIED** |
| Charset / collation | **`utf8mb4` / `utf8mb4_unicode_ci`** | **VERIFIED** |
| MySQL | **8.4.8-8-beget-1-2** | **VERIFIED** |
| Safe counts (FU02) | pages publish 25; posts publish 16; services publish 29; users 3; all_publish 857 | **VERIFIED** SELECT |

---

## Forms / mail

| Field | Value | Evidence class |
|-------|-------|----------------|
| Public form markup presence | Contacts and lead forms render on frontend | **PUBLIC BEHAVIOR MATCH** (no submit test) |
| SMTP / delivery | — | **SAFE UNKNOWN** |

---

## Cache

| Field | Value | Evidence class |
|-------|-------|----------------|
| Edge / page cache | No strong public cache identity beyond nginx | **SAFE UNKNOWN** |

---

## Backups

| Field | Value | Evidence class |
|-------|-------|----------------|
| Fresh full Beget files + DB backup after **original** migration | Exists (P01) | **`BACKUP CONFIRMED BY OPERATOR`** — **does not cover post-reimport live state** |
| Fresh post-reimport Layer A | Files + DB of current live state | **OPERATOR CONFIRMED** (FU01) |
| Backup ID / path / timestamp | — | **SAFE UNKNOWN** |
| Layer B WPilot 0.3.0 snapshot | STORAGE copy of plugin dir | `X:\AI MARS STORAGE\wpilot\evidence\fp-0002-shpigovsky\prod-p05\pre-upgrade-wpilot-0.3.0\` |

---

## Logs

| Field | Value | Evidence class |
|-------|-------|----------------|
| Application / PHP / access logs | — | **SAFE UNKNOWN** |

---

## SEO / temporary hostname risk

- Temporary host `shpigovsky.beget.tech` is publicly crawlable (`robots.txt` does not blanket-disallow).
- Site title still contains «локальная разработка».
- DNS for `shpigovsky.ru` remains on old hosting — dual-public presence risk until cutover charter.
- **No** robots/noindex mutation in this wave.

---

## Evidence

* Current P05: `REPORTS/evidence/prod-p05-wpilot-upgrade-auth-gate/`
* Report: `REPORTS/REPORT-FP-0002-PROD-P05-WPILOT-UPGRADE-AUTH-GATE.md`
* Post-reimport rebaseline: `REPORTS/evidence/prod-p04-fu02-post-reimport-rebaseline/`
* Historical pre-reimport FS baseline: `REPORTS/evidence/prod-p04-fu01-filesystem-baseline/`

---

## PROD-P02 access contour (pointers only)

| Item | Path |
|------|------|
| Connection profile (entry) | [FP-0002-MARS-PRODUCTION-CONNECTION-PROFILE-v1.md](FP-0002-MARS-PRODUCTION-CONNECTION-PROFILE-v1.md) |
| Access matrix | [FP-0002-PRODUCTION-ACCESS-MATRIX-v1.md](FP-0002-PRODUCTION-ACCESS-MATRIX-v1.md) |
| Credential map (no values) | [FP-0002-CREDENTIAL-REFERENCE-MAP-v1.md](FP-0002-CREDENTIAL-REFERENCE-MAP-v1.md) |
| Local-only secrets | `X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md` |
| Local-only metadata | `X:\AI MARS\local\sites\shpigovsky-production\site-profile.json` |
| Reserved WPilot token | `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token` (**present**, gitignored; no value in this passport) |
| Runtime checkout | `X:\AI MARS STORAGE\runtime-checkouts\fp-0002-shpigovsky-production\repo` — **DEFERRED** |
| P05 evidence | `REPORTS/evidence/prod-p05-wpilot-upgrade-auth-gate/` |
| P03 evidence | `REPORTS/evidence/prod-p03-production-access-validation/` |
| P04 evidence | `REPORTS/evidence/prod-p04-beget-access-repair/` |
| P04-FU01 evidence (historical pre-reimport) | `REPORTS/evidence/prod-p04-fu01-filesystem-baseline/` |
| P04-FU02 evidence (current) | `REPORTS/evidence/prod-p04-fu02-post-reimport-rebaseline/` |
