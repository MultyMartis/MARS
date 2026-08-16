# BASELINE — FP-0002 PRODUCTION POST-P13 (PROD-P14)

**Baseline ID:** `FP-0002-PROD-BASELINE-2026-08-17`  
**Established:** 2026-08-16/17 (UTC intake 2026-08-16T17:28Z)  
**Wave:** PROD-P14 Stabilization

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
| shpigovsky-core | `0.3.5-p14` |
| WPilot | 0.3.2 · writes disabled · bridge active (read) |
| siteurl/home | http://shpigovsky.beget.tech |
| blog_public | 0 |
| WP_ENVIRONMENT_TYPE | `local` (residue — Production/Beget runtime) |

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
- Local FP-0002 WORDPRESS = SOURCE AUTHORITY after P14 reconciliation  

## Parity

- Fresh intake: 705 local source-owned files walked  
- After operator drift canonization (`v9-style.css`, `content-page.php`) + P14 deploy: deployable MATCH  
- Accepted PROD_ONLY: `robots.txt` (+ empty `.gitkeep` placeholders)  
- Statement: **SOURCE ↔ PRODUCTION MATCH** for deployable FP-0002-owned code  

## Latest accepted wave

**P13 + P13-FU01** (operator + Olya UI acceptance)

## Backup

| Field | Value |
|-------|-------|
| Type | Full files + DB via SSH (tar.gz + mysqldump.gz) |
| Stamp | `20260816-173046` |
| Path | `X:\AI MARS STORAGE\backups\fp-0002\prod-p14-full-20260816-173046\` |
| DB size / SHA256 | 1198790 · `4a30c86afcbf0dd98a6e818e61020ad9fb6c142ee7babf10067fa3991a8bf51f` |
| Files size / SHA256 | 637254469 · `7f4d7ed8b56fca2447ae8371ef3055093b5d6ad074ada1b4bfcb6532a0d633e6` |
| Status | **PASS** |

## Git checkpoint

| Field | Value |
|-------|-------|
| Commit | `9a5f671cafece716635e6fb37b984bd9009261de` |
| Short | `9a5f671c` |
| Branch | `origin/mars/canonical-post-recovery` |
| Message | FP-0002: stabilize production baseline after P13/FU01 |
| Staged paths | 838 (FP-0002 scope; evidence runners / INCOMING / oversized zips excluded) |
| Clean worktree | `X:\AI MARS STORAGE\git-sync-fp0002-p14-20260816-173714\repo` |

## Open tails

See `REPORTS/OPEN-ITEMS-FP-0002-AFTER-P14.md` — P06, typography, SMTP, PRE-CUTOVER, domain/SSL, robots/indexing, sitemap submissions, final crawl.

## Required

`FP-0002 NEW PRODUCTION BASELINE ESTABLISHED`
