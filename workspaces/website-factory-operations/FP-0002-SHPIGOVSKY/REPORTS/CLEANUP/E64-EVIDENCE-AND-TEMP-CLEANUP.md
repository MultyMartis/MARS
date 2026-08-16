# E64 Evidence and Temporary File Cleanup

## Policy applied

Keep Stable/E62*/E58 evidence packs and all Markdown reports. Delete only regenerable tooling deps under evidence.

## Deleted (exact allowlist)

| Path | Size | Reason |
|------|------|--------|
| `REPORTS/evidence/v9-06e54-fix01-floating-header/_probe/node_modules` | ~16.8 MB | Playwright deps; scripts retained |
| `REPORTS/evidence/v9-06e60-nav-breadcrumb-cta-service-links/node_modules` | ~16.8 MB | Playwright deps; screenshots/CSV retained |
| `REPORTS/evidence/v9-06e63-stable-v1-closeout/node_modules` | ~10.6 MB | Playwright deps; closeout evidence retained |

**Evidence reclaimed:** **46,281,900 bytes (~44.1 MB)**  
Evidence root: ~369.1 MB → ~324.8 MB

## Retained

- All Stable v1 / E63 closeout evidence artifacts (git metadata, matrices, screenshots)
- E62C / E62D / E62E / E58 evidence trees
- Admin HTML dumps (referenced / historical)
- `_tmp-shot.html` (referenced in E58 allowlist artifacts)
- Probe scripts (`capture-screenshots.mjs`, `_e63_shots.cjs`, `package.json`)

## Runtime temp

| Path | Action |
|------|--------|
| `wp-content/debug.log` (3.67 MB) | **DELETED** after size/mtime summary; no unique Stable blocker |
| `wp-content/cache` | Absent |
| `wp-content/upgrade` | Empty; left alone |
| uploads / theme / plugin / ACF JSON | **NOT touched** |

## Source-side junk

Found but **not deleted** (MANUAL_REVIEW):

- `WORDPRESS/theme/shpigovsky/assets/video/sergey-shpigovsky-interview.mp4.BROKEN-MPEGTS.bak` (~26 MB) — possible unique media recovery
- `WORDPRESS/validation/v9-06e56-operator-refinements/group_fp02_block_comfort.pre-split.json.bak`

See `E64-SOURCE-JUNK-MANUAL-REVIEW.txt`. Source deletion allowlist empty this wave.

## Storage exports

`X:\AI MARS STORAGE\exports\fp-0002-*` remain **MANUAL_REVIEW** (not in first-pass allowlist).
