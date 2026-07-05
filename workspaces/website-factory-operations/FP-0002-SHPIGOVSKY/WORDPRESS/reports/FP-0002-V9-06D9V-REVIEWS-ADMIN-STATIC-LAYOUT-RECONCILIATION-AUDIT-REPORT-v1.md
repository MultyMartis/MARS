# FP-0002 V9-06D9V Reviews Admin + Static Layout Reconciliation Audit Report

**Phase:** V9-06D9-V  
**Date:** 2026-07-06  
**Verdict:** PARTIAL PASS  
**Mode:** Read-only audit — no repair performed

## Executive summary

Operator findings after D9-U are **substantiated**. D9-U automated PASS validated `get_field(..., 'option')` and missed operator-visible admin and layout gaps.

| Operator finding | Audit result |
|---|---|
| Duplicate reviews in Site Settings | **CONFIRMED** — stale duplicate ACF field-group DB post (checkpoint evidence) |
| Empty top-level Отзывы admin | **CONFIRMED** — ACF storage context mismatch (`option` vs `fp02-reviews`) |
| Frontend "old slider" | **Partially explained** — Home slider matches static V9 Home; `/otzyvy/` wrongly uses same slider |
| `/otzyvy/` spacing/layout broken | **CONFIRMED** — archive-list never implemented; skeleton + slider instead of static card list |

**Recommended next phase:** `CREATE_V9_06D9W_REVIEWS_ADMIN_AND_LAYOUT_REPAIR_TASK`

## Safety preflight

| Check | Result |
|---|---|
| Volume X / AI WS | PASS |
| Branch mars/canonical-post-recovery | PASS |
| Local HEAD | `8a9d6e371d177ded6700960d34dc1cc790cbd308` |
| Remote HEAD | Same (synced) |
| D9-U ancestor c3cbee9f | PASS (ancestor) |
| Strict HEAD gate | **PASS_WITH_HEAD_NOTE** (tip advanced past c3cbee9f) |
| Staged files | None |
| Foreign WIP | Present — not staged |

## Key technical findings

### 1. Admin duplicate

Git JSON location is already `fp02-reviews`. D9-U checkpoint shows **two** DB posts with key `group_fp02_site_options_reviews`. Stale copy likely still targets `fp02-site-settings`.

### 2. Empty admin fields

Helpers and migrations use `get_field(..., 'option')`. Top-level **Отзывы** screen uses `fp02-reviews` post_id. Frontend can render 10 slides while admin appears empty.

### 3. `/otzyvy/` layout

Static V9 (`src/pages/otzyvy.html`) uses `reviews-archive-list.html` (vertical cards, `gap: var(--pad-gap)`). WP `page-templates/reviews.php` includes shared slider + skeleton `archive-list.php` placeholder.

## Documentation produced

- Report: this file
- Architecture: 7 docs under `architecture/FP-0002-V9-06D9V-*`
- Validation: 9 JSON files under `validation/v9-06d9v-reviews-admin-static-layout-reconciliation-audit/`

## No-scope-drift

PASS — documentation/evidence only; zero DB/source/theme/ACF/runtime mutations.

## Next step

See `architecture/FP-0002-V9-06D9V-FUTURE-D9W-REPAIR-PLAN-v1.md`
