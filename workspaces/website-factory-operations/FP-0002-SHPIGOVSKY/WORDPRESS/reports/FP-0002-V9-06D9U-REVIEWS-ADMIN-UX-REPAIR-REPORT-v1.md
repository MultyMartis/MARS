# FP-0002 V9-06D9U Reviews Admin UX Repair Report

**Phase:** V9-06D9-U  
**Date:** 2026-07-06  
**Verdict:** PASS

## Executive summary

Repaired Reviews admin UX after D9-T: removed Home `Reviews teaser` save blocker (theme-level suppression of plugin-local field), migrated 10 seeded review rows to canonical `review_*` option meta, and added top-level admin menu **Отзывы** (`fp02-reviews`). Frontend remains source mode **OPTIONS** with 10 reviews on Home and `/otzyvy/`.

## Safety preflight

- Volume: X / AI WS — PASS
- Branch: `mars/canonical-post-recovery` — PASS
- HEAD gate: D9-T ancestor `3a970507` verified; tip `c0d623da` (unrelated OCPilot) — PASS_WITH_NOTE
- Staged files: none — PASS

## Source changes

| File | Change |
|---|---|
| `theme/shpigovsky/inc/admin-options.php` | NEW — Reviews options page + Home teaser suppression |
| `theme/shpigovsky/functions.php` | require admin-options |
| `acf-json/group_fp02_site_options_reviews.json` | location → `fp02-reviews` |

## DB / runtime

- Checkpoint: `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d9u-reviews-admin-ux-repair-pre-20260706-013004/`
- Runtime delivery: 3 files (theme + ACF JSON)
- ACF sync: import + in-place location update on group ID 250
- Options meta migration: 10 rows, 40 canonical writes, 40 legacy keys removed

## Validation

| Area | Result |
|---|---|
| Home blocker removed | PASS |
| Reviews admin canonical fields | PASS |
| Top-level Reviews menu | PASS |
| Frontend regression | PASS (routes ALL_200, 10 slides) |
| Screenshots | PARTIAL (headless) |
| No-scope-drift | PASS |

## Evidence

`validation/v9-06d9u-reviews-admin-ux-repair/`

## Next step

CREATE_V9_06D9V_ADMIN_VISUAL_QA_TASK
