# REPORT — FP-0002 V9-06E45-FIX03 SERVICE LAYOUT SELECTOR SIMPLIFICATION

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | 8341f5690827df2c43d4f552132f9ca56426cfb7 |
| Staged files before | 0 |
| WIP count only | 784 (foreign WIP present; untouched) |
| Runtime/source canon detected | YES — FP-0002 source `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS`; runtime `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky` |
| Home frozen state untouched | YES |
| Services hub frozen visual untouched | YES (whitespace-normalized exact equal) |
| Commit allowed | NO |
| Result | PASS (unpushed foreign metabot commits exist; out of scope — commit/push skipped) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e45-fix03-service-layout-selector-simplification-before-20260714-202448\` |
| DB dump | `db/mars_wp_fp0002.sql` SHA256=`208944966A5895590384A0E1F6FB20628D75861407EA9D6C0D400FA42C86DC9C` (size 4234080; mysqldump PROCESS tablespace warning ignored, dump complete) |
| Theme backup/hash | `theme/shpigovsky` — 635 files; `inventories/theme-sha256.txt` |
| Plugin backup/hash | `plugin/shpigovsky-core` — 23 files; `inventories/plugin-sha256.txt` |
| ACF JSON backup/hash | `acf-json` — 10 files; `inventories/acf-json-sha256.txt` |
| Service ACF group export before | `exports/group_fp02_service_layout_hero.before.json` (+ source copy) |
| Service layout meta export before | `exports/service-layout-meta-before.tsv` (29 services) |
| Service hierarchy inventory before | same TSV (ID/parent/children/role/layout/override) |
| Frontend snapshots before | `snapshots/*-before.html` + `route-smoke-before.csv` |
| Result | PASS |

## 3. Admin UX simplification

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| One visible layout block | ACF label `Макет страницы услуги` on `service_editor_role` | PASS | |
| First-level selector | `acf/prepare_field` keeps button_group Раздел/Услуга when depth=1 | PASS | |
| Nested auto-service notice | Field converted to message for depth≥2 | PASS | RU notice |
| Manual override hidden/removed | `prepare_field` returns false + CSS hide | PASS | meta retained |
| Technical dropdown hidden/removed | same for `service_layout_variant` + advanced heading | PASS | required cleared to 0 |
| Red-accent help | `.fp02-acf-notice-danger` on first-level help + nested notice lead | PASS | not scary; clear |

## 4. Depth-based layout logic

| Page level | UI behavior | Effective layout | Result | Notes |
|---|---|---|---|---|
| First-level service page | selector section/service | subdivision or service_general | PASS | helper `shpigovsky_get_service_depth` / `ServiceLayoutGovernance::get_service_depth` |
| Nested service page | automatic service notice | service_general | PASS | resolver forces depth≥2 → service-general |

## 5. Data cleanup / sync

| Group | Count | Role writes | Layout writes | Override writes | Result | Notes |
|---|---:|---:|---:|---:|---|---|
| First-level sections | 3 | 0 | 0 | 2 | PASS | `#77/#84` override empty→0; `#73` already 0 |
| First-level services | 0 | 0 | 0 | 0 | PASS | none today |
| Nested services | 26 | 1 | 1 | 25 | PASS | `#74` corrected section/subdivision→service/service_general; others mostly override empty→0 |

Applied posts with any write: **28**. Underscore ACF field-key metas synced on writes.

Evidence: `v9-06e45-fix03-layout-sync-results.csv`, `v9-06e45-fix03-service-depth-layout-plan.csv`

## 6. Admin validation

| Page | ID | Level | UI expected | UI actual | Role/layout | Result |
|---|---:|---:|---|---|---|---|
| Зависимости | 73 | first | selector visible | WP/ACF probe: label «Макет…»; depth=1 nested=no | section/subdivision | PASS |
| Психическое здоровье | 77 | first | selector visible | depth=1 | section/subdivision | PASS |
| РПП | 84 | first | selector visible | depth=1 | section/subdivision | PASS |
| Наркотическая зависимость | 314 | nested | auto-service notice | depth=2 nested=yes; override/variant fields prepare_field=false | service/service_general | PASS |
| Alcohol | 74 | nested | auto-service notice | depth=2; meta corrected | service/service_general | PASS |
| Depression | 78 | nested | auto-service notice | depth=2 | service/service_general | PASS |

Note: admin screens validated via WP bootstrap + ACF field definitions / prepare_field contracts (not browser screenshots). Technical fields still exist in definitions but are hidden from normal UI.

Evidence: `v9-06e45-fix03-admin-ui-validation.csv`

## 7. Frontend validation

| Route | Expected stack | HTTP | Result | Notes |
|---|---|---:|---|---|
| `/uslugi/` | services hub frozen | 200 | PASS | whitespace-collapsed exact equal vs before |
| `/` | Home frozen | 200 | PASS | whitespace-collapsed delta=21 noise |
| Зависимости | subdivision | 200 | PASS | body class subdivision |
| Психическое здоровье | subdivision | 200 | PASS | |
| РПП | subdivision | 200 | PASS | |
| Наркотическая зависимость | service_general + child block | 200 | PASS | child_block=True |
| Alcohol | service_general | 200 | PASS | intentional stack restore after meta correction |
| Depression | service_general | 200 | PASS | |
| /blog/, /specyalisty/, /o-centre/, /kontakty/ | regression | 200 | PASS | no fatal |

Evidence: `v9-06e45-fix03-frontend-validation.csv`

## 8. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| ServiceLayoutGovernance.php | WORDPRESS/plugins/.../Admin/ | wp-content/plugins/.../Admin/ | YES | PASS |
| EditorRestrictions.php | WORDPRESS/plugins/.../Admin/ | wp-content/plugins/.../Admin/ | YES | PASS |
| FieldGroups.php | WORDPRESS/plugins/.../Fields/ | wp-content/plugins/.../Fields/ | YES | PASS |
| service-helpers.php | WORDPRESS/theme/.../inc/ | wp-content/themes/.../inc/ | YES | PASS |
| admin-home-acf.css | WORDPRESS/theme/.../assets/css/ | wp-content/themes/.../assets/css/ | YES | PASS |
| group_fp02_service_layout_hero.json | WORDPRESS/acf-json/ | wp-content/acf-json/ | YES | PASS |
| Operator v9-style.css | (not modified) | runtime == FIX03 backup hash | YES | PASS |

## 9. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E45-FIX03-service-layout-selector-simplification.md | created | PASS | this file |
| SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md | updated | PASS | FIX03 depth model |
| PROJECT-STATUS.md | updated | PASS | |
| SOURCE-AUTHORITY.md | updated | PASS | FIX03 section appended |
| v9-06e45-fix03-service-depth-layout-plan.csv | created | PASS | |
| v9-06e45-fix03-admin-ui-validation.csv | created | PASS | |
| v9-06e45-fix03-layout-sync-results.csv | created | PASS | |
| v9-06e45-fix03-frontend-validation.csv | created | PASS | |

## 10. Git result

| Item | Value |
|---|---|
| Staged before | 0 |
| Staged after | 0 |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local service layout selector simplification; persistence handled separately |
| Push attempted | NO |

### Git classification (read-only)

**Intended FIX03 source changes:**

- `WORDPRESS/plugins/shpigovsky-core/src/Admin/ServiceLayoutGovernance.php` (?? untracked prior deliverable rewritten)
- `WORDPRESS/plugins/shpigovsky-core/src/Admin/EditorRestrictions.php` (M)
- `WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php` (M)
- `WORDPRESS/theme/shpigovsky/inc/service-helpers.php` (M)
- `WORDPRESS/theme/shpigovsky/assets/css/admin-home-acf.css` (??)
- `WORDPRESS/acf-json/group_fp02_service_layout_hero.json` (M)
- `DOCS/SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md` (??)
- `PROJECT-STATUS.md`, `WORDPRESS/SOURCE-AUTHORITY.md` (M)
- `REPORTS/REPORT-FP-0002-V9-06E45-FIX03-...md` + `REPORTS/evidence/v9-06e45-fix03-*.csv`

**Runtime-only:** mirrored under `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky` (not in git)

**DB changes:** `mars_wp_fp0002` service layout metas (28 posts touched)

**Media:** none

**Foreign WIP:** remaining ~784 lines / unrelated FP-0002/theme files / `.recovery-temp` / metabot — not staged, not touched

## 11. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| `#74` frontend stack changed after correcting mistaken section/subdivision meta | Medium | Mitigated | Expected; alcohol static copy still ID-gated; operator visual check on alcohol URL |
| Admin validated via WP/ACF probe not live browser screenshots | Low | Accepted | Operator open `#73` and `#314` edit screens once |
| ConvertTo-Json may reorder ACF JSON keys | Low | Accepted | Content verified; source↔runtime hash match |
| Nested pages cannot become subdivision from UI | Info | By design | Reparent to first-level if a page must be a section |

## 12. Final verdict

PASS

V9-06E45-FIX03 Service layout selector simplification:
COMPLETE

One-block admin UX:
PASS

Depth-based logic:
PASS

Manual override removal:
PASS

Data sync:
PASS

Frontend preserved:
PASS

Services hub frozen visual untouched:
PASS

Home frozen state untouched:
PASS

Regression:
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

## 13. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 14. Final safety statement

Target folder:
X:\AI MARS

V9-06E45-FIX03 Service layout selector simplification performed:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

DB writes:
28 posts (1 role + 1 layout + 27 override-ensure; ACF key refs on applied)

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

Rebase:
NO

Stash:
NO

Cleanup:
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
