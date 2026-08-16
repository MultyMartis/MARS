# RELEASE MANIFEST — FP-0002 V9 Stable v1

| Field | Value |
|-------|-------|
| Human label | FP-0002 V9 Stable v1 |
| Release code | FP-0002-V9-STABLE-V1 |
| Status | STABLE / NEAR-PRODUCTION |
| Formulation | **Stable local near-production baseline** |
| Release wave | V9-06E63 |
| Date/time | 2026-07-18 00:40:51 |
| Canonical source | `X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS\` |
| Local runtime | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky` |
| Runtime URL | http://shpigovsky.test/ |
| Database | `mars_wp_fp0002` / prefix `fp02_` |
| Branch | `mars/canonical-post-recovery` |
| Source commit before release (dirty main HEAD) | `7443c4e9256101a95d756b5a3c01cd4e827f0713` |
| Canonical remote HEAD before release | `29c07d210169ff273d69e7b5f9000d84c1c097b1` |
| Final release commit | d1befe9b8bfc8688f2f286998ec048e6be49beb6 |
| Remote push state | 9d5dcc285eb45c827231bfe89c7611fb84e850d2 |
| Pre-release backup | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e63-before-stable-v1-closeout-20260718-003355` |
| Authoritative freeze | X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-stable-v1-near-production-freeze-20260718-004137 |
| Protected operator CSS | `v9-style.css` SHA256 `1CCC5A8F1150BC696186E0F8D4546B7D55A1895BFA3C77DD50A32204B09A7BA9` |
| Operator search CSS | `fp02-search.css` SHA256 `8DD6E89F3B7373623CD3BB8718E9DE0BF883A24B892AB5E6D767B7D244C01F94` |
| Operator shell JS | `v9-shell.js` SHA256 `2B9507D013C14BC0C3B5F4C52932DC59D1782E0511C7E5B003D20B97FE7A8800` |
| Pre-release DB dump SHA256 | `2665C889D4EA2476782EE2DF5C3F7D33B3FACB20D86FF6A9123C26B24DFBCACC` |

## Scope included

All accepted FP-0002 WordPress work through V9-06E62E-FIX01, plus operator manual CSS/JS edits canonized in E63.

## Major features (accepted)

- Full V9 theme shell, Home, Services hub/sections/services, O-centre, Specialists, Contacts, Blog, Reviews
- Floating header, lifebuoy, local fonts (Libertinus), forms (local accept flow)
- 404 decor + native WordPress Search baseline
- Admin ACF UX, Site Settings, pagination/SEO for Blog/Reviews
- Treatment program mini-descriptions

## Explicit non-claims

- Not published to public production domain
- SMTP / production mail not configured
- Demo Blog/Reviews not production-cleaned
- Production indexing/analytics not configured

## Rollback

1. Restore authoritative Stable v1 freeze backup (Phase F path).
2. Restore DB from freeze SQL dump.
3. Redeploy theme/plugin/ACF from freeze snapshot or Git release commit.








