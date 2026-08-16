# SERVICE-RECORD-INVENTORY — PROD-P14

**Captured:** 2026-08-16T17:28Z (intake) / post-deploy 17:33Z  
**Host:** http://shpigovsky.beget.tech/  
**Future canonical:** shpigovsky.ru

| Surface | Classification | Notes |
|---------|----------------|-------|
| A. Dashboard MetaCODE / Состояние системы | CURRENT | Updated P14 widget `fp02_metacode_system_state`; baseline `FP-0002-PROD-BASELINE-2026-08-17`; no global notices |
| B. Site Settings (`fp02-site-settings*`) | CURRENT | Parent + General + Social + SEO/Integrations + reusable blocks |
| C. Activity Log | CURRENT | Table `fp02_user_activity_log` exists; schema option `fp02_activity_log_db_version=1`; retention code **8000**; row count ~50 after QA prune |
| D. Smart Search | CURRENT | REST `shpigovsky/v1/smart-search` responds; Admin under SEO/Integrations; option keys ACF-owned |
| E. SEO / Integrations | CURRENT | Native `/wp-sitemap.xml` LIVE; analytics/verification owner = Site Settings SEO |
| F. DOCX Publisher | CURRENT | Module class loaded; importer screen registered |
| G. Services CPT | CURRENT | `service` registered; publish count **31** |
| G. Specialists CPT | CURRENT | `specialist` registered; publish count **9**; rewrite `specyalisty` |
| H. Social / Messenger | CURRENT | Settings owner Site Settings → Social; FE header/footer wired |
| I. WPilot | CURRENT | Active **0.3.2**; write disabled; bridge read-only |
| J. Theme | CURRENT | Shpigovsky `0.3.0-d7a-shell` |
| J. shpigovsky-core | CURRENT | **0.3.5-p14** |
| K. Environment | STALE (P06) | `WP_ENVIRONMENT_TYPE=local` on production host; MU `mars-local-runtime.php` present; admin_email migration residue |
| L. Latest accepted wave | CURRENT | **P13 + P13-FU01** (operator/Olya UI acceptance) |
| M. Source ↔ production parity | CURRENT | Post-canonize deployable MATCH; verified P14 |
| Option `fp02_metacode_system_meta` | CURRENT | Operational meta for widget (baseline/parity/backup/git) |
| P08/P09/P10 “current state” labels in widget | OBSOLETE → REMOVED | Superseded by P14 widget sections |
| Activity Log QA rows FP02 FU01 HTTP* | OBSOLETE → REMOVED | ids 68–71 |
| FU01 QA posts #2028/#2029 | OBSOLETE | Already absent at cleanup time |
| Real Activity Log history (Olya edits) | CURRENT / RETAINED | Not deleted |
| Layer B / Storage backups | OPERATOR-ONLY / RETAINED | Not service records inside WP |
| robots.txt Sitemap append | PROD_ONLY / INTENTIONAL | Production-only; Disallow preserved |

## Required

`FP-0002 SERVICE RECORDS CURRENT`
