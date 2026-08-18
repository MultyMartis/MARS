# MARS-RUNTIME STATUS RESOLVED

| Field | Value |
|-------|--------|
| Path | `/home/s/shpigovsky/shpigovsky.ru/public_html/mars-runtime` |
| Owner | Leftover local MLI / MARS runtime scripts copied onto Beget with the WordPress tree. **Not** a WordPress module, **not** referenced by theme/plugin/MU, **not** in crontab. |
| Contents | `scripts/`: `populate-fp-0002-pages.php`, `fp0002-access-encoding-wpilot-task.php`, `validate-wpilot-readonly.ps1`, `create-foundation-002a-checkpoint.ps1`, `reset-to-foundation.ps1`, `backup-runtime.ps1` |
| Public | Directory 403; **PHP/PS1 files HTTP 200**. Populate script **executes on GET** (`wp_insert_post` / menu update). Encoding script dumps options JSON. |
| WP/theme/plugin refs | **0** |
| Scheduled MARS process | **0** (empty crontab) |
| Production need | **NO** |
| Secrets | Local-runtime bootstrap only; still a public executable surface |
| Classification | **C. OBSOLETE** + **D. SECURITY RISK** |
| Action | Exact tar snapshot then **removed** 2026-08-18 |

Snapshot: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p17-fu02-layer-b-pre\obsolete-webroot-snapshot\obsolete-webroot-20260818-101831.tar.gz`  
SHA-256: `199fd6bec8c4185ec6167ba94437048f629d32bd223886235a589f18e20e30c5`

Related: `public_html/app/` (Local nested theme residue) classified **C. OBSOLETE**, included in the same tar, removed. Not WP runtime.

**Incident:** GET `/mars-runtime/scripts/populate-fp-0002-pages.php` during exposure probe created 12 placeholder pages + 15 menu items and set `wp_page_for_privacy_policy` to 2049. Rolled back exactly (pages 2038–2049, menu items 2050–2064, privacy option restored to `3`). Smoke 200, no stub copy on live routes.

Post-removal: those PHP URLs return **404**.
