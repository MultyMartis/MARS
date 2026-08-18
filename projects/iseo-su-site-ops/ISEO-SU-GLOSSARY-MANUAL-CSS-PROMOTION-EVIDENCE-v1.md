# ISEO-SU GLOSSARY MANUAL CSS PROMOTION EVIDENCE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-GLOSSARY-FINAL-INTEGRATION-AND-CLOSEOUT  
**Date:** 2026-08-18  
**Authority:** production operator manual edit after commit `f8126b03`

---

## 1. Operator Manual Change

After automated glossary hero alignment (`f8126b03`, production deploy stamp `20260818T062716Z`), the operator manually edited shared production CSS to tune glossary presentation. Production `css/main.css` mtime moved to **2026-08-18T06:47:41Z** (~20 minutes after hero theme upload). No theme PHP/CSS package in MARS contained these rules before this task.

## 2. Production Authority

| Field | Value |
|-------|-------|
| Authoritative file | docroot `css/main.css` |
| Public URL | `https://i-seo.su/css/main.css` |
| SFTP path | `./css/main.css` |
| Production SHA-256 | `8e1774ba8996ed3f8be33c6c9750c5db2db4752ff9c93bb54a46b0a5860f2580` |
| Bytes | **144736** |
| Direction | **production → canonical MARS source** (not overwrite production from stale repo) |

`css/media.css` and theme `style.css` were compared and **unchanged** relative to prior MARS snapshots for this task scope.

## 3. Files Compared

| File | Production | Prior MARS snapshot | Result |
|------|------------|---------------------|--------|
| `css/main.css` | live SFTP + HTTP | `_glossary-scratch/layout-fix/prod-css__main.css` (2026-07-24 layout-fix capture) | **manual delta present** |
| `css/media.css` | live | layout-fix capture | identical |
| `wp-content/themes/iseoblog/style.css` | live | `_glossary-scratch/theme-baseline/style.css` | identical |

Forensic receipt: `_glossary-scratch/final-integration/forensic-receipt.json`  
Bounded patch: `_glossary-scratch/final-integration/diff-main_vs_layout_fix.patch`

## 4. Bounded Diff

Only **`css/main.css`** changed. Total delta **+383 bytes** vs layout-fix snapshot (`1424631c…` → `8e1774ba…`).

| # | Selector / scope | Change summary | Glossary-only? |
|---|------------------|----------------|----------------|
| 1 | `.glossary-template-default .breadcrumbs` | `margin: 0 0 50px !important` | **yes** (single template body class) |
| 2 | `.post-type-archive-glossary #SecondScreen .content_block > form > p > label` | `display: block`; commented optional margin reset | **yes** (archive search label) |
| 3 | `.info_span` | new block: `display:block; margin-bottom:50px; color:rgba(161,161,170,1)` | **shared class**; supports glossary hero/archive description styling already using services `span` pattern |
| 4 | `.content ol, .content ul` | split margin: lists now `margin: 0 0 50px 0` | **shared**; affects WP `.content` surfaces using existing typography block |
| 5 | `main .content ol, main .content ul` | retains prior indented list margin `0 0 50px 50px` with `padding:0` | **shared** |

No changes to `page_scene*` core stack, rates, modalbox, calculator, or unrelated marketing selectors.

## 5. Promoted Changes

Canonical promotion path:

`projects/iseo-su-site-ops/production-source/css/main.css`

Post-promotion checksum matches production:

`8e1774ba8996ed3f8be33c6c9750c5db2db4752ff9c93bb54a46b0a5860f2580`

Production was **not** re-uploaded during this task (already correct operator version).

## 6. Unrelated Differences

| Item | Classification | Action |
|------|----------------|--------|
| `css/media.css` | unchanged vs prior snapshot | left untouched |
| `style.css` | unchanged vs theme baseline | left untouched |
| Pre-hero vs post-hero automated theme PHP | out of manual CSS scope | not mixed into CSS promotion |
| `/glossary/feed` link in archive HTML | WordPress feed discovery | not CSS; excluded from term-count validation |

## 7. Final Source / Production State

| Layer | State |
|-------|-------|
| Production `css/main.css` | operator manual version live |
| MARS `production-source/css/main.css` | **matches production SHA-256** |
| HTTP vs SFTP | identical checksum |
| Glossary hero PHP | unchanged in this task; remains services `page_scene` alignment from `f8126b03` |

## 8. Rollback

| Layer | Method |
|-------|--------|
| CSS only | restore remote `css/main.css` from pre-task operator backup or Beget full backup |
| MARS source | revert `production-source/css/main.css` to prior snapshot if needed |
| Evidence | keep this file + `diff-main_vs_layout_fix.patch` |

Do **not** restore layout-fix snapshot over production without operator approval — it would remove intentional glossary tuning.

---

*Manual CSS promotion evidence v1 · 2026-08-18.*
