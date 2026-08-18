# BASELINE — FP-0002 PRODUCTION POST-P13 (PROD-P14) + P15 ENVIRONMENT CLEAN + P16 TYPOGRAPHY + P17 PRE-CUTOVER CONT1 + P17-FU02 + P18A LIVE DOMAIN + P18B DASHBOARD/INDEXING + P18C SMTP/FORMS + P18C-FU01 ADMIN MENU + P18C-FU02 MULTI-RECIPIENTS

**Baseline ID:** `FP-0002-PROD-BASELINE-2026-08-19-P18C-FU02`  
**Established:** 2026-08-16/17 (UTC intake 2026-08-16T17:28Z)  
**Wave:** PROD-P14 Stabilization  
**P15 extension:** 2026-08-16/17 — environment/migration cleanup (same baseline ID; P14 backup remains rollback authority)  
**P17 extension:** 2026-08-18 — legacy 301s + DNS/NS migration plan (NS not switched **in that wave**)  
**P17-FU02 extension:** 2026-08-18 — internal pre-cutover tails closed; READY FOR MANUAL NS SWITCH **at that time**  
**P18A extension:** 2026-08-18 — operator live-domain cutover canonized; legal demo banner owner fixed  
**P18B extension:** 2026-08-19 — MetaCODE Dashboard reality model + Admin indexing control; indexing remains CLOSED  
**P18C extension:** 2026-08-19 — SMTP/forms Admin foundation; `fp02_form_leads`; suppression ON until verified+activate  
**P18C-FU01 extension:** 2026-08-19 — SMTP/forms Admin page attached to the visible Site Settings parent  
**P18C-FU02 extension:** 2026-08-19 — multi-recipient Add/Remove UX; operator SMTP stored; not verified

## Runtime

| Field | Value |
|-------|-------|
| Live production domain (WordPress) | `https://shpigovsky.ru` (`home` / `siteurl`) |
| Public apex at P18A intake | **Legacy origin** still observed (`45.130.41.70` @8.8.8.8) — not WordPress |
| WordPress working host | `http://shpigovsky.beget.tech/` (inner routes) |
| Docroot | `/home/s/shpigovsky/shpigovsky.ru/public_html` |
| WordPress | 7.0.4 |
| PHP (CLI / php8.2 widget render) | 8.2.28 |
| PHP (web SAPI) | do not assume CLI; P18A dashboard once showed 8.3.20 |
| DB name (no secrets) | `shpigovsky_main` |
| DB prefix | `fp02_` |
| Theme | Shpigovsky `0.3.0-d7a-shell` |
| shpigovsky-core | `0.3.14-p18c-fu02` |
| WPilot | 0.3.2 · writes disabled · bridge active (read) |
| siteurl/home | `https://shpigovsky.ru` |
| blog_public | 0 |
| WP_ENVIRONMENT_TYPE | **production** (P15) |
| WP_DEBUG / DISPLAY / LOG | **false / false / false** (P15) |
| Mail | PRE-CUTOVER suppression MU owned by `mail.ops` until VERIFIED/ACTIVE. Admin: Настройки сайта → Почта и формы (multi-recipient Add/Remove after P18C-FU02). Sender `noreply@shpigovsky.ru`. Password write-only in `fp02_mailbox_auth` (autoload false; **CONFIGURED**). SMTP **CONFIGURED / NOT VERIFIED**. Leads: `fp02_form_leads` schema v1. |
| Typography | ONE owner `typography.russian` — render-time HTML-aware; DB content mutations 0 |
| Legal demo banner | `legal_demo_marker` explicit `0`/`1`; template does not hardcode DEMO |

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
- Local FP-0002 WORDPRESS = SOURCE AUTHORITY after P14/P15/P16 reconciliation  

## Parity

- P14: deployable MATCH after canonization  
- P15 touched source files: **3/3 MATCH** (core + dashboard + mail MU)  
- P16 touched source files: **6/6 MATCH** (core + typography module + dashboard + search-helpers)
- P18A touched source files: **7/7 MATCH** (theme legal helper/template/`functions.php`; core + dashboard + FieldGroups + EditorRestrictions)
- P18C touched source files: **14/14 MATCH** (core mail/leads/admin + MU + `v9-shell.js`)
- P18C-FU01 touched source files: **4/4 MATCH** (MailFormsSettings + OptionsPage + Dashboard + core bootstrap)
- P18C-FU02 touched source files: **8/8 MATCH** (MailOps + MailFormsSettings + Dashboard + ActivityLog + ConsultationHandler + core bootstrap + admin JS/CSS)

## Latest accepted wave

**P18C-FU02 Multiple recipients** — Add/Remove recipient UX; operator SMTP stored and **CONFIGURED / NOT VERIFIED**; suppression ON; indexing **CLOSED**; public apex still observed as Craftum.

## Backup

| Field | Value |
|-------|-------|
| P18C-FU02 exact-file snapshots | `deployment-packs/fp-0002/prod-p18c-fu02-layer-b-pre/` |
| P18C-FU01 exact-file snapshots | `deployment-packs/fp-0002/prod-p18c-fu01-layer-b-pre/` |
| P18C operator Beget backup | **FRESH BEGET BACKUP CONFIRMED BY OPERATOR** (pre-wave) |
| P18C exact-file snapshots | `deployment-packs/fp-0002/prod-p18c-layer-b-pre/` |
| P18B operator Beget backup | **FRESH BEGET BACKUP CONFIRMED BY OPERATOR** (timestamp not safely discovered) |
| P18B exact-file snapshots | `deployment-packs/fp-0002/prod-p18b-layer-b-pre/` |
| Type (last MARS full dump) | Full files + DB via SSH (tar.gz + mysqldump.gz) |
| Stamp | `20260816-173046` |
| Path | `X:\AI MARS STORAGE\backups\fp-0002\prod-p14-full-20260816-173046\` |
| Status | P14 dump exists; P18B relies on **operator Beget backup**, not a new MARS full dump |
| P15 exact-file/object snapshots | `deployment-packs/fp-0002/prod-p15-layer-b-pre/` + `prod-p15-db-snapshots/` + `prod-p15-debug-archive/` |
| P16 exact-file snapshots | `deployment-packs/fp-0002/prod-p16-layer-b-pre/` + `prod-p16-db-snapshots/` |
| P17 CONT1 `.htaccess` snapshots | `deployment-packs/fp-0002/prod-p17-cont1-layer-b-pre/` |
| P17-FU02 Layer B | `deployment-packs/fp-0002/prod-p17-fu02-layer-b-pre/` + `prod-p17-fu02-db-snapshots/` + obsolete tar |

## Git checkpoint

| Field | Value |
|-------|-------|
| P14 commit | `9a5f671cafece716635e6fb37b984bd9009261de` |
| P15 commit | `81912e7871bd45d75e8b02b288aaf0b6788744d6` |
| P16 commit | `35666e2bb98247072a7a7972d4271eaf8d5f36aa` |
| P17 commit | `1b7fb5c47b2c7acd88e4313e64a15f7e59069fa6` |
| P17-FU02 commit | `16706398f03825b054ce75c56e8af48ec4349329` |
| P18A commits | `d96dfce1f4d8e8d18ba026809923e1e1dbb067c6` · `95ade9bd4baa00f22a80c589e43c55d3ed586e8c` |
| P18B commits | see `REPORTS/evidence/prod-p18b-dashboard-indexing/GIT-CHECKPOINT.json` |
| Branch | `origin/mars/canonical-post-recovery` |

## Open tails

See `REPORTS/OPEN-ITEMS-FP-0002-AFTER-P18C-FU02.md` — operator remaining recipients → SMTP verification → forms delivery → public apex → WordPress → Olya indexing → sitemaps → crawl.

## P18B status

- MetaCODE Dashboard — **current operational surface** (no stale NS/future-host copy)
- Indexing Admin control — **LIVE**; production state **CLOSED**
- Public apex → WordPress — **not stable** (Craftum observed 2026-08-18 18:21Z five-shot)
- SMTP — **PENDING** (`noreply@shpigovsky.ru` mailbox exists)
- Legal DEMO banner — **follows `legal_demo_marker`** (P18A)

## P18A status

- Operator `home`/`siteurl` = `https://shpigovsky.ru` — **canonized, not reverted**
- NS — **Beget observed**
- Public apex → WordPress — **not yet** (legacy origin still public)
- SSL (WP origin) — **IN PROGRESS**
- Legal DEMO banner — **follows `legal_demo_marker`**
- Indexing — **CLOSED**
- SMTP — **PENDING**

## P17-FU02 status

- Internal pre-cutover readiness **GO**
- `mars-runtime/` **removed** (obsolete + public PHP risk)
- Webroot hygiene **PASS**
- Users/admin **CLEAN**
- Cutover DB/file plans **executable without discovery**
- NS **not** switched

## P15 environment-clean status

- Runtime classified as production on temporary Beget host  
- Local-runtime identity removed; mail/indexing intentionally deferred  
- Live frontend `.test`/localhost references cleared where safe  
- Final domain cutover **not** executed  

## P16 typography status

- ONE HTML-aware typography owner (`typography.russian`)  
- Render-time pipeline; DB content mutations **0**  
- Future Olya/DOCX content follows the same pipeline  
- Typography residual **closed**

## Required

`FP-0002 NEW PRODUCTION BASELINE ESTABLISHED` (P14)  
`FP-0002-PROD-BASELINE-2026-08-17` **+ P15 ENVIRONMENT CLEAN + P16 TYPOGRAPHY**
