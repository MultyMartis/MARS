# VALIDATION — FP-0002 V9 Stable v1

**Wave:** V9-06E63  
**Date:** 2026-07-18 00:40:51

## Route matrix

Priority routes HTTP probe: **27/27 expected PASS** (26×200 + 1×404 intentional).  
Evidence: `REPORTS/evidence/v9-06e63-stable-v1-closeout/route-http-matrix-final.csv`

Includes: Home, Services hub + section + 3 services, O-centre + program hub + 4 children + gallery, Specialists + 2 children, Contacts, Blog + page/2 + single, Reviews pages 1–3, Search blank/results/empty, Legal privacy, intentional 404.

Search pagination: `/page/2/?s=а` → **200** (broad query; narrow queries may be single-page).

## Viewport matrix

Screenshots captured at 1440×900, 1024×768 (subset), 480×900, 370×812 for critical CSS-affected and priority routes.  
Evidence: `REPORTS/evidence/v9-06e63-stable-v1-closeout/screenshots/` (24 PNG).

## Overflow / console

| Check | Result |
|-------|--------|
| Horizontal overflow (probed) | **0** |
| Page errors | **0** |
| Console errors | 3× resource 404 attributed to intentional 404 route probes |
| PHP syntax lint (theme+plugin) | **0 failures / 183 files** |
| JS syntax `v9-shell.js` | **PASS** (node --check) |
| Duplicate HTML IDs (critical routes) | **0** groups |
| PHP warning/fatal in HTTP bodies | **0** |

## Admin

PHP/options presence: reviews **30** rows with **30** non-empty `review_uid`; demo Blog **10** (#1745–1754); treatment mini-description present on #1053.  
Detailed admin screenshots reused from E61/E62C evidence lineage (no admin UI mutation in E63).

## Evidence lineage

- Fresh E63 screenshots for CSS-affected Search/Home/Services/404/mobile
- Reused E62C/E62D/E62E packs for unchanged components

## SAFE UNKNOWN

- Full authenticated wp-admin browser matrix not re-run in E63 (code/admin fields unchanged in this wave except CSS/JS canonization)
- Exact third-party Yandex Maps network errors under restricted networks: not treated as product defect
