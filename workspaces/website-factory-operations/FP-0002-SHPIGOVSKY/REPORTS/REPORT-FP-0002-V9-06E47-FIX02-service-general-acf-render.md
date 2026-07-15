# REPORT — FP-0002 V9-06E47-FIX02 SERVICE GENERAL ACF RENDER FIX

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | 8341f5690827df2c43d4f552132f9ca56426cfb7 |
| Staged files before | (empty) |
| WIP count only | ~809–810 (foreign WIP left untouched) |
| Runtime/source canon detected | YES — FP-0002 `WORDPRESS/` + local `http://shpigovsky.test` |
| Home frozen state untouched | YES (gallery random card order residual only; no Home config/code writes) |
| Services hub frozen visual untouched | YES (`/uslugi/` whitespace-normalized equal) |
| Section model untouched/regression-free | YES (`#73` Раздел visible; Услуга hidden) |
| Commit allowed | NO |
| Result | PASS (HEAD ahead of origin — MetaBOT docs; no commit/push) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e47-fix02-service-general-acf-render-before-20260715-133411\` |
| DB dump | `db/mars_wp_fp0002.sql` (~3.24MB; SHA256 `181FCE7BCA72C32785047210108A9F522F58F94D41A797694B43584B1FCB97AB`; `--no-tablespaces`) |
| Theme backup/hash | copied; aggregate md5 `d2cfe37b32306f3b2da40bdd9d2e1ee0` |
| Plugin backup/hash | copied; aggregate md5 `3f16c89944eb6932668a558133ec3c98` |
| ACF JSON backup/hash | copied; aggregate md5 `39ff9f576ee6f40053207883ca0bcd26` |
| Admin/metabox inventory before | `admin/admin-groups-74-before.json` |
| Base + representative meta exports before | `meta/postmeta-74-314-78-73-before.tsv` |
| Frontend snapshots before | `/`, `/uslugi/`, zavisimosti, alcohol, `?p=314`, `?p=78`, `?p=73` |
| Result | PASS |

## 3. Root cause

| Area | Finding | Fix | Result | Notes |
|---|---|---|---|---|
| ACF group render | Nested `#74` (depth=2): FIX03 converts `service_editor_role` → `message` with empty `name`. All 68 parity fields had `when_service` conditionals on that field → ACF JS hid every field while group title still showed. | `ServiceGeneralParity::when_service()` returns `0`; rely on `filter_service_parity_groups_by_role` | PASS | Confirmed via WP_ADMIN bootstrap |
| Field definitions | 68 top-level fields; no duplicate keys; defs valid | Preserve fields; clear conditionals in PHP+JSON | PASS | count stays 68 |
| ACF filters | FIX01 role filter correctly keeps parity for Услуга | Keep | PASS | not the bug |
| Admin JS/CSS/postbox | Empty body was conditional-driven, not collapsed preference alone | Conditional removal | PASS | |

## 4. Admin metabox cleanup

| Metabox | Before | After | Scope | Result | Notes |
|---|---|---|---|---|---|
| Редакция / revisionsdiv | visible | hidden | service CPT | PASS | `EditorRestrictions::remove_irrelevant_metaboxes` |
| Отрывок / postexcerpt | visible | hidden | service CPT | PASS | same |
| Classic editor | hidden | hidden | service CPT | PASS | theme `admin-editor.php` |
| Other boxes | title/permalink/sidebar/attributes/featured as needed | unchanged intent | service CPT | PASS | blog/pages not targeted |

## 5. Service general group visibility

| Check | Expected | Actual | Result |
|---|---|---|---|
| Group visible | yes | yes | PASS |
| Group expands/openable | yes | fields no longer all-hidden by conditional | PASS |
| Fields render | yes | 68 fields, `conditional_logic=0` | PASS |
| Field count | expected 68 or documented | 68 | PASS |
| Repeaters visible | yes | signs/bordered/approach/program/stages/support/FAQ | PASS |
| CTA fields visible | yes | cta_title/text/button_label/target | PASS |

## 6. Admin validation #74

| Check | Expected | Actual | Result |
|---|---|---|---|
| #74 edit loads | yes | groups resolve via WP bootstrap | PASS |
| Layout visible | yes | Макет страницы услуги | PASS |
| Hero visible | yes | Hero страницы услуги | PASS |
| Услуга group usable | yes | 68 fields, 0 conditionals | PASS |
| Legacy groups hidden | yes | yes | PASS |
| Редакция hidden | yes | yes | PASS |
| Отрывок hidden | yes | yes | PASS |
| Save validation | no errors | no admin fatal introduced; no DB meta mutation | PASS |

## 7. Representative admin validation

| Page | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| #314 | service group usable | usable (parity visible, cond=0) | PASS | nested same pattern |
| #78 | service group usable | usable | PASS | |
| #73 | section model preserved | section visible; Услуга hidden | PASS | |

## 8. Frontend validation

| Route | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| Alcohol URL | 200 unchanged | 200; whitespace-normalized equal | PASS | 131425 bytes |
| #314 URL | 200 unchanged | 200 equal | PASS | |
| #78 URL | 200 unchanged | 200 equal | PASS | |
| #73 Section URL | 200 unchanged | 200 equal | PASS | |

## 9. Frozen pages validation

| Page | Expected | Actual | Result |
|---|---|---|---|
| Home `/` | unchanged | HTTP 200; gallery card order residual; no Home writes | PASS |
| Services hub `/uslugi/` | unchanged | whitespace-normalized equal | PASS |

## 10. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/uslugi/zavisimosti/` | 200 | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | |
| alcohol `#74` | 200 | PASS | unchanged |
| `#314` | 200 | PASS | |
| depression `#78` | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

## 11. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| ServiceGeneralParity.php | WORDPRESS/plugins/.../ServiceGeneralParity.php | wp-content/plugins/.../ServiceGeneralParity.php | YES | PASS |
| EditorRestrictions.php | WORDPRESS/plugins/.../EditorRestrictions.php | wp-content/plugins/.../EditorRestrictions.php | YES | PASS |
| group_fp02_service_general_parity.json | WORDPRESS/acf-json/ | wp-content/acf-json/ | YES | PASS |
| v9-style.css (operator) | runtime | runtime vs FIX01 backup | YES `C858903F…` | PASS |

## 12. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E47-FIX02-service-general-acf-render.md | created | PASS | this file |
| SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md | updated | PASS | FIX02 visibility rule |
| PROJECT-STATUS.md | updated | PASS | |
| SOURCE-AUTHORITY.md | updated | PASS | E47-FIX02 entry |
| v9-06e47-fix02-acf-render-diagnostics.csv | created | PASS | |
| v9-06e47-fix02-admin-metabox-inventory.csv | created | PASS | |
| v9-06e47-fix02-service-general-field-visibility.csv | created | PASS | |
| v9-06e47-fix02-admin-validation.csv | created | PASS | |
| v9-06e47-fix02-frontend-validation.csv | created | PASS | |

## 13. Git result

| Item | Value |
|---|---|
| Staged before | (empty) |
| Staged after | (empty) |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local service general ACF render fix; persistence handled separately |
| Push attempted | NO |

### Git classification (read-only)

| Class | Paths |
|---|---|
| Intended FP-0002 E47-FIX02 | `ServiceGeneralParity.php`, `EditorRestrictions.php`, `acf-json/group_fp02_service_general_parity.json`, `DOCS/SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md`, `PROJECT-STATUS.md`, `SOURCE-AUTHORITY.md`, `REPORTS/evidence/v9-06e47-fix02-*`, `WORDPRESS/validation/v9-06e47-fix02-*`, this REPORT |
| Runtime-only | delivered plugin/acf-json copies under `X:\MARS-Localhost\…\shpigovsky` |
| DB changes | none (0 writes) |
| Media changes | none |
| Docs/evidence | REPORT + CSV evidence as above |
| Foreign WIP | large unrelated `M`/`??` under MetaBOT, `.recovery-temp`, other FP lanes — not staged |

## 14. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Operator must hard-refresh `/wp-admin` if browser cached ACF field defs | low | mitigated | Soft reload; ACF JSON modified bumped |
| SectionParity still uses field-level `when_section` | low | accepted | Sections are depth-1 so role stays button_group; revisit if nested sections appear |
| CPT still lists excerpt/revisions in `supports` | info | accepted | Metaboxes removed; supports left intact (no architectural CPT change) |
| Home gallery random order differs between snapshots | info | not a FIX02 regression | Gallery display mode residual; Home config untouched |

## 15. Final verdict

PASS

V9-06E47-FIX02 Service general ACF render fix:
COMPLETE

ACF group render/open fix:
PASS

Field visibility:
PASS

Metabox cleanup:
PASS

Base service frontend preserved:
PASS

Representative services preserved:
PASS

Section accepted model preserved:
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

## 16. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 17. Final safety statement

Target folder:
X:\AI MARS

V9-06E47-FIX02 Service general ACF render fix performed:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

Section accepted model touched:
NO

DB writes:
0

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
