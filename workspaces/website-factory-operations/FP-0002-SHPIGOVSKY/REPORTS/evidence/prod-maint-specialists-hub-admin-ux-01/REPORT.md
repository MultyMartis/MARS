# FP-0002 — Specialists Hub Admin UX + Internal URL Audit 01

**Date (UTC):** 2026-08-24  
**Production:** https://shpigovsky.ru/  
**Core version after:** `0.3.27-specialists-hub-admin-ux`  
**Page:** #1030 `/specyalisty/` (Specialists Hub)

## Verdict

**PASS** — Admin critical error fixed at root cause; reusable-block enable/disable UX live; `/specialisty/` audited (no live internal links; no 301 added).

## Admin critical-error root cause

**Exact exception:**

`Error: Cannot access private property acf_field_checkbox::$_values`

**File:** `wp-content/plugins/acf-extended-pro/pro/includes/fields/field-checkbox.php` line 35  
**Context:** ACFE Pro 0.9.2.3 replaces ACF checkbox `render_field` and writes `$instance->_values` / `$_all_checked`. ACF Pro 6.8.5 made those properties **private**, so the Specialists Hub / generic-page reusable checkbox metabox fatals and WordPress shows the Russian critical-error message inside «Повторно используемые блоки».

**Fix owner:** project module `Shpigovsky\Core\Admin\AcfeCheckboxCompat` — when private `$_values` is detected, restore ACF core checkbox `render_field` (do not CSS-hide; do not vendor-patch ACFE as primary).

## Reusable-block enable/disable model

Extends existing `group_fp02_page_generic_content` (generic + specialists-hub):

| Field | Key | Role |
|-------|-----|------|
| `generic_page_reusable_blocks_enabled` | `field_fp02_generic_page_reusable_blocks_enabled` | true_false UI Вкл/Выкл (default 0) |
| `generic_page_reusable_blocks` | `field_fp02_generic_page_reusable_blocks` | checkbox; conditional on enable == 1 |

Frontend: `shpigovsky_page_reusable_blocks_enabled()` / `shpigovsky_get_page_reusable_block_keys()`  
Legacy BC: if enable meta absent but selection exists → still render (preserves older pages).

## `/specialisty/` audit

| Surface | Hits |
|---------|------|
| post_content | 0 |
| postmeta | 0 |
| options | 0 |
| nav menus | 0 |
| WORDPRESS theme/plugin source | 0 exact `/specialisty/` |

HTTP: `/specialisty/` → **404** (no Location redirect). Canonical remains `/specyalisty/` → 200.  
**LIVE internal links to `/specialisty/`:** **NONE FOUND.**  
Alias/301 remains **deferred**.

## QA (post-deploy)

- Checkbox + enable + notice render: no exception, no critical text
- Admin edit #1030: enable control present; conditional on selector; no critical in reusable section
- Enable OFF with stored selection: helpers empty; hub HTML without rehab block
- Enable ON + rehab: block renders; then meta restored to empty (no leftover QA content)
- Hub listing 200; `/specialisty/` still 404; `blog_public=1`

## Rollback

Layer-B copies of overwritten files under `layer-b-pre/`. Restore exact remote paths from deploy manifest `03-deploy-manifest.json`.

## Git note

Selective commit from worktree `wave/fp0002-specialists-hub-admin-ux-01` → `origin/mars/canonical-post-recovery`.
