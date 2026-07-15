# REPORT — FP-0002 V9-06E52 GENERIC PAGES DEMO ACF SOT + PLACEHOLDER

## 1. Safety preflight

| Check | Value |
|---|---|
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `44c05c3b38adcc3b134a5110d73683f36af1fa5c` |
| Runtime/source canon detected | YES — FP-0002 `WORDPRESS/` + `http://shpigovsky.test` / `mars_wp_fp0002` |
| Backup created before writes | YES |
| Home frozen state untouched | YES |
| Services hub frozen visual untouched | YES |
| Service sections preserved | YES |
| Service pages preserved | YES |
| Commit allowed | NO |
| Result | PASS (HEAD ahead of origin; foreign WIP untouched; no commit/push) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e52-generic-pages-demo-acf-sot-placeholder-before-20260716-043220\` |
| DB dump | `db/mars_wp_fp0002.sql` (~3.90 MB); SHA256 `EC3BBFD9…CB1D53`; `--no-tablespaces` |
| Theme backup/hash | copied; tree SHA256 `8fb3b852…ae7bbe9` |
| Plugin backup/hash | copied; tree SHA256 `d77ca05f…010c982` |
| ACF JSON backup/hash | copied; tree SHA256 `b43d3d7e…695d2de` |
| Generic page exports | postmeta + post_content for 15 IDs under `meta/` |
| Frontend snapshots | generic×15 + controls (home/uslugi/sections/services/blog/specialists/o-centre/kontakty) under `frontend/` |
| Result | PASS |

## 3. Generic pages audit

| Category | Count | Notes |
|---|---:|---|
| Total normal pages reviewed | 25 | all WP `page` |
| Excluded pages | 10 | Home, posts, dedicated templates |
| Included generic pages | 15 | all `page-templates/generic.php` |
| Pages already had layout mode | 15 | E51 `page_layout_mode` present |
| Pages needed ACF seeding | 15 | content group missing before E52 |
| Pages already ACF SoT | 0 | before E52 |
| Hardcoded demo fallback found | YES | in `content-page.php` before E52 |
| Placeholder mode already present | YES (partial) | layout field + FE stub; no content SoT |

Audit CSVs: `v9-06e52-generic-pages-inventory.csv`, `v9-06e52-generic-pages-current-model-audit.csv`.

## 4. Implementation summary

| Area | Before | After | Result | Notes |
|---|---|---|---|---|
| Page layout mode | E51 field present | retained + clarified help | PASS | full / placeholder |
| Generic placeholder frontend | shell+H1 when placeholder | unchanged pattern | PASS | `generic.php` |
| Generic full frontend SoT | post_content + hardcoded demo | ACF `generic_page_*` | PASS | empty hides |
| Admin UX | layout only | + «Содержимое страницы»; hide classic clutter | PASS | featured image kept |
| Demo/current content seeding | n/a | 15/15 body seeded | PASS | page-specific post_content |
| Empty optional fields | demo inject | hide | PASS | `#14` probe |

## 5. Seeding result

| Page | Fields seeded | Existing preserved | Result | Notes |
|---|---:|---|---|---|
| #12–16, #1030, #1039, #1053–1056 | body | lead left empty | PASS | interim demo from post_content |
| #1031–1033, #1097 | body | lead left empty | PASS | specialist bios from post_content |
| All 15 | page_layout_mode → full where empty | — | PASS | no mass placeholder |

CSV: `v9-06e52-generic-pages-seeding.csv` (after meta-key fix wave).

## 6. Placeholder switch validation

| Page | Full → Placeholder | Placeholder frontend | Placeholder → Full | Final state | Result |
|---|---|---|---|---|---|
| #1039 Интервью и СМИ | PASS | shell+H1; ACF body preserved | PASS | full | PASS |

CSV: `v9-06e52-generic-placeholder-switch-validation.csv`.

## 7. Generic frontend validation

| Page/Route | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| 15 generic pages | 200, H1, full/ACF, no broken empty demo | 15/15 PASS | PASS | `data-content-source=acf` spot-check |
| Empty body `#14` temp | no demo inject | source=empty; demo NO | PASS | restored |

CSVs: `v9-06e52-generic-pages-frontend-validation.csv`, `v9-06e52-empty-field-hide-validation.csv`.

## 8. Regression validation

| Route | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| `/` | preserved | 200 | PASS | Home untouched |
| `/uslugi/` | preserved | 200 | PASS | hub untouched |
| Sections | preserved | 200; not placeholder | PASS | #73/#77/#84 |
| Services sample | preserved | 200; #315/#78 Услуга | PASS | role/variant checked |
| Blog/specialists/o-centre/contacts | 200 | 200 | PASS | |

CSV: `v9-06e52-regression-validation.csv` (15/15).

## 9. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result | Notes |
|---|---|---|---|---|---|
| generic.php | WORDPRESS/theme/... | themes/... | YES | PASS | |
| content-page.php | WORDPRESS/theme/... | themes/... | YES | PASS | |
| FieldGroups.php | WORDPRESS/plugins/... | plugins/... | YES | PASS | |
| EditorRestrictions.php | WORDPRESS/plugins/... | plugins/... | YES | PASS | |
| group_fp02_page_layout_mode.json | WORDPRESS/acf-json/... | wp-content/acf-json/... | YES | PASS | |
| group_fp02_page_generic_content.json | WORDPRESS/acf-json/... | wp-content/acf-json/... | YES | PASS | new |

CSV: `v9-06e52-source-runtime-sync.csv`.

## 10. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E52-generic-pages-demo-acf-sot-placeholder.md | created | PASS | this file |
| GENERIC-PAGES-ADMIN-PARITY-MODEL-v1.md | created | PASS | |
| SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md | updated | PASS | E52 note |
| PROJECT-STATUS.md | updated | PASS | |
| SOURCE-AUTHORITY.md | updated | PASS | |
| evidence CSVs | created | PASS | v9-06e52-* |

## 11. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Push attempted | NO |

## 12. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| First seed wrote value under field-key meta | Medium | Mitigated | Fix wave relocated to `generic_page_body` + `_generic_page_body` |
| Operator clears body but expects post_content | Low | Accepted | Classic editor hidden; ACF is SoT |
| Real wp-admin placeholder save for pages | Low | Watch | Service FIX02 path applies to ACF generally; validate in operator review |
| Institutional ACF group `#12–16` legacy | Low | Accepted | location still template/ID gated; generic content group is primary for generic.php |

## 13. Final verdict

PASS

V9-06E52 Generic pages demo ACF SoT + placeholder:
COMPLETE

Backup:
PASS

Generic pages audit:
PASS

ACF SoT model:
PASS

Demo/current content seeding:
PASS

Placeholder mode for normal pages:
PASS

Placeholder switch validation:
PASS

Frontend validation:
PASS

Regression:
PASS

Home preserved:
PASS

Services hub preserved:
PASS

Service sections preserved:
PASS

Service pages preserved:
PASS

Source/runtime sync:
PASS

Operator CSS preserved:
PASS

Git commit:
SKIPPED

No foreign project work:
PASS

Recommended next phase:
OPERATOR_REVIEW_REQUIRED

## 14. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 15. Final safety statement

Target folder:
X:\AI MARS

V9-06E52 Generic pages demo ACF SoT + placeholder performed:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

Service sections touched:
NO

Service pages touched:
NO

Generic pages touched:
YES

Placeholder mode for generic pages:
YES

DB writes:
~114 (seed + meta fix + placeholder switch + empty-field probe restore)

Source changes:
YES

Runtime delivery:
YES

WordPress changes:
YES

Media Library changes:
NO

Backup created:
YES

Git mutation:
NO

Git commit:
NO

Git push:
NO

Reset:
NO

Clean:
NO

Stash:
NO

Rebase:
NO

Foreign project work:
NO

Operator runtime CSS preserved:
YES

FP-0002 product contaminated:
NO

WPilot confused with OCPilot:
NO

Secrets committed:
0
