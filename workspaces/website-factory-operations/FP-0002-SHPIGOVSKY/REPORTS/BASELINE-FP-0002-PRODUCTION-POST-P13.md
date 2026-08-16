# BASELINE — FP-0002 PRODUCTION POST-P13 (PROD-P14) + P15 ENVIRONMENT CLEAN

**Baseline ID:** `FP-0002-PROD-BASELINE-2026-08-17`  
**Established:** 2026-08-16/17 (UTC intake 2026-08-16T17:28Z)  
**Wave:** PROD-P14 Stabilization  
**P15 extension:** 2026-08-16/17 — environment/migration cleanup (same baseline ID; P14 backup remains rollback authority)

## Runtime

| Field | Value |
|-------|-------|
| Production host | http://shpigovsky.beget.tech/ |
| Future canonical domain | shpigovsky.ru |
| Docroot | `/home/s/shpigovsky/shpigovsky.ru/public_html` |
| WordPress | 7.0.4 |
| PHP (web) | 8.3.20 (dashboard) |
| PHP (CLI probe) | 8.2.28 |
| DB name (no secrets) | `shpigovsky_main` |
| DB prefix | `fp02_` |
| Theme | Shpigovsky `0.3.0-d7a-shell` |
| shpigovsky-core | `0.3.6-p15` (was `0.3.5-p14` at P14 freeze) |
| WPilot | 0.3.2 · writes disabled · bridge active (read) |
| siteurl/home | http://shpigovsky.beget.tech |
| blog_public | 0 |
| WP_ENVIRONMENT_TYPE | **production** (P15) |
| WP_DEBUG / DISPLAY / LOG | **false / false / false** (P15) |
| Mail | PRE-CUTOVER suppression MU (`fp02-pre-cutover-mail-suppression.php`) |

## Content counts (publish)

| Entity | Count |
|--------|-------|
| service | 31 |
| specialist | 9 |
| post | 16 |
| page | 21 |

## Users (no secrets)

| Login | Role | Notes |
|-------|------|-------|
| admin | Administrator | Olya · ola4seo@yandex.ru |
| mars | Administrator | preserved |
| metacode | Administrator | metacode@polygon-ws.ru |
| mli_admin_fp0002 | — | removed (P13) |

## Authority

- Beget filesystem = LIVE RUNTIME TRUTH  
- Beget DB = LIVE CONTENT / SETTINGS / USER AUTHORITY  
- Local FP-0002 WORDPRESS = SOURCE AUTHORITY after P14/P15 reconciliation  

## Parity

- P14: deployable MATCH after canonization  
- P15 touched source files: **3/3 MATCH** (core + dashboard + mail MU)

## Latest accepted wave

**P15 environment cleanup** (closes deferred P06)

## Backup

| Field | Value |
|-------|-------|
| Type | Full files + DB via SSH (tar.gz + mysqldump.gz) |
| Stamp | `20260816-173046` |
| Path | `X:\AI MARS STORAGE\backups\fp-0002\prod-p14-full-20260816-173046\` |
| Status | **PASS** — remains current full rollback baseline for P15 |
| P15 exact-file/object snapshots | `deployment-packs/fp-0002/prod-p15-layer-b-pre/` + `prod-p15-db-snapshots/` + `prod-p15-debug-archive/` |

## Git checkpoint

| Field | Value |
|-------|-------|
| P14 commit | `9a5f671cafece716635e6fb37b984bd9009261de` |
| P15 commit | see P15 git evidence after clean-worktree push |
| Branch | `origin/mars/canonical-post-recovery` |

## Open tails

See `REPORTS/OPEN-ITEMS-FP-0002-AFTER-P15.md` — typography → PRE-CUTOVER → domain/SSL → SMTP → indexing → sitemap submissions → final crawl.

## P15 environment-clean status

- Runtime classified as production on temporary Beget host  
- Local-runtime identity removed; mail/indexing intentionally deferred  
- Live frontend `.test`/localhost references cleared where safe  
- Final domain cutover **not** executed  

## Required

`FP-0002 NEW PRODUCTION BASELINE ESTABLISHED` (P14)  
`FP-0002-PROD-BASELINE-2026-08-17` **+ P15 ENVIRONMENT CLEAN**
