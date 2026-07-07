# REPORT — FP-0002 V9-06E19 REUSABLE BLOCKS ADMIN VISIBILITY REPAIR

**Wave:** V9-06E19  
**Date:** 2026-07-08  
**Verdict:** PASS (admin screenshots PARTIAL)

## Summary

Repaired Batch 1 reusable block admin visibility. Root cause: WordPress 2-level menu limit — E18 registered block pages as children of `fp02-site-settings-blocks` (3rd level, invisible). Fix: register Batch 1 pages as direct children of `fp02-site-settings`. Synced reviews field group dual location for alias page. Frontend 8/8 routes PASS.

## 1. Safety preflight

| Check | Result |
|-------|--------|
| Volume X / AI WS | PASS |
| Branch mars/canonical-post-recovery | PASS |
| Local HEAD | `3b317910` (E18 ancestor PASS; note: ahead of required `ea7ffd12`) |
| Remote synced | PASS |
| Staged files | none |
| E18 ancestor | PASS |

## 2. Root cause

E18 field groups and option values were correct; admin IA registration placed Batch 1 under a submenu parent (`fp02-site-settings-blocks`), which WordPress does not render as a visible sidebar branch.

## 3. Repair

**Changed:** `plugins/shpigovsky-core/src/Admin/OptionsPage.php`

- Batch 1 `parent_slug` → `fp02-site-settings`
- Container `redirect => false` + navigation notice
- Reviews DB: imported dual-location JSON (1 DB write)

## 4. Validation

| Gate | Result |
|------|--------|
| ACF parent slug probe | PASS |
| Field groups active | PASS |
| Frontend 8/8 HTTP 200 | PASS |
| Admin screenshots | PARTIAL (login gate) |
| Old top-level Отзывы | PASS |

## 5. Evidence

`validation/v9-06e19-reusable-blocks-admin-visibility-repair/`

## 6. Next

**CREATE_V9_06E20_OPERATOR_REUSABLE_BLOCKS_ADMIN_QA_TASK**
