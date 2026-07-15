# REPORT — FP-0002 V9-06E46-FIX01 SERVICE SECTION HERO ADMIN SEPARATION

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | 8341f5690827df2c43d4f552132f9ca56426cfb7 |
| Staged files before | (empty) |
| WIP count only | 793 (foreign WIP present; not touched) |
| Runtime/source canon detected | YES — FP-0002 WORDPRESS + local shpigovsky runtime |
| Home frozen state untouched | YES (group Home still 74 fields; no Home ACF edits) |
| Services hub frozen visual untouched | YES (`/uslugi/` fingerprint match vs FIX01 pre-backup) |
| Commit allowed | NO |
| Result | PASS (unpushed commits exist on branch — no pull/rebase/push per charter) |

**Live revalidation (2026-07-14 ~22:15):** Admin groups for `#73`/`#77`/`#84` show separate `Service — Layout` + `Hero страницы услуги`; mixed title absent from active groups (5× DB `acf-disabled` only). `/uslugi/zavisimosti/` and `/uslugi/` fingerprints match FIX01 pre-backup; Home ACF still 74 fields; operator `v9-style.css` hash match; all regression routes HTTP 200. No additional DB/content writes in revalidation pass.

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e46-fix01-service-section-hero-admin-separation-before-20260714-214425\` |
| DB dump | `db\mars_wp_fp0002.sql` (~4.3 MB) |
| Theme backup/hash | `theme\shpigovsky` + `inventories\theme-sha256.txt` |
| Plugin backup/hash | `plugin\shpigovsky-core` + `inventories\plugin-sha256.txt` |
| ACF JSON backup/hash | `acf-json\` + `inventories\acf-json-sha256.txt` |
| Service ACF export before | `exports\group_fp02_service_layout_hero-before.json` + section parity export |
| #73 meta/admin export before | `inventories\postmeta-73-zavisimosti-before.json` + `admin-zavisimosti-before.json` |
| Frontend snapshots before | `snapshots\home|uslugi|zavisimosti-before.html` |
| Result | PASS |

## 3. Hero/layout group audit

| Field/group | Before | After | Meta preserved | Result | Notes |
|---|---|---|---|---|---|
| Layout block | Mixed `Service — Layout and Hero` | `Service — Layout` (`group_fp02_service_layout_hero`) | YES (group key kept) | PASS | Layout + hub/catalog subsection |
| Hero block | Same mixed group | `Hero страницы услуги` (`group_fp02_service_hero`) | YES (new group; field keys/names preserved) | PASS | Shared Раздел + Услуга |
| service_editor_role | In mixed group | In Layout only | YES | PASS | Label «Макет страницы услуги» |
| Hero fields | Mixed with layout | Hero group only | YES | PASS | eyebrow / H1 override / lead / media / CTA label+URL |
| DB duplicates | 5× publish Layout and Hero | `acf-disabled` | n/a | PASS | Soft-disable only; no service postmeta rewritten |

Evidence: `REPORTS/evidence/v9-06e46-fix01-service-hero-layout-group-audit.csv`

## 4. Admin/frontend recheck

| Order | Frontend block | Admin section/control | Source of truth | Status | Notes |
|---:|---|---|---|---|---|
| 1 | Hero | Hero страницы услуги | hero_* ACF | OK | Separated in FIX01 |
| 2 | Subnav | Раздел §2 + `section_nav_visible` | template anchors | INTENTIONAL_AUTOMATIC | |
| 3 | Dependencies / children | Раздел §3 + toggle | children CPT + chrome ACF | OK | |
| 4 | Nature | Раздел §4 + toggle | section_nature_* | OK | |
| 5 | Mid CTA | Раздел §5 + toggle | shared CTA | OK | Per-section copy → FIX02 if needed |
| 6 | Program | Раздел §6 + toggle | intros ACF + catalog | OK | |
| 7 | Stages | Раздел §7 + toggle | chrome ACF + theme defaults | OK / FIX02 for item bodies | |
| 8 | Approach / team-stats | Раздел §8 + toggle | section_approach_* | OK | |
| 9 | Clinic landscape | Раздел §9 + toggle | Home/shared | INTENTIONAL_AUTOMATIC | |
| 10 | Specialists | Раздел §10 + toggle | specialists pages | INTENTIONAL_AUTOMATIC | |
| 11 | Founder quote | Раздел §11 + toggle | shared template | INTENTIONAL_AUTOMATIC | |
| 12 | Comfort | Раздел §12 + toggle | Comfort options | INTENTIONAL_AUTOMATIC | |
| 13 | Reviews | Раздел §13 + toggle | reviews data | OK | |
| 14 | FAQ | Раздел §14 + FAQ repeater | heading + items | OK | |
| 15 | Final form | Раздел §15 + toggle | Final Form options | INTENTIONAL_AUTOMATIC | |

Evidence: `REPORTS/evidence/v9-06e46-fix01-zavisimosti-admin-frontend-recheck.csv`

## 5. Hardcoded HTML/text recheck

| Block | Hardcoded source remains | Should be editable | Action | Result | Notes |
|---|---|---|---|---|---|
| Nature / approach / program intros / FAQ heading / deps chrome | Theme fallbacks only | yes | already ACF | PASS | E46 |
| Stages chrome | fallback if empty | yes | already ACF | PASS | |
| Stages item bodies | theme `__()` defaults | partial | document | NEEDS_E46_FIX02 | Large modeling — not FIX01 |
| Leaf/alcohol templates | yes | yes | out of scope | OK | E47 / service general |
| Home reused blocks | shared | no | toggles | PASS | |

Evidence: `REPORTS/evidence/v9-06e46-fix01-service-section-hardcoded-recheck.csv`

## 6. Small fixes applied

| Fix | Scope | Result | Notes |
|---|---|---|---|
| Split Layout / Hero ACF groups | plugin FieldGroups + ACF JSON | PASS | Meta keys preserved |
| Update §1 hero notice | ServiceSectionParity | PASS | Points to Hero + Layout |
| Hub subsection message in Layout | layout group | PASS | Clarifies non-hero catalog fields |
| Soft-disable 5 DB mixed groups | mars_wp_fp0002 acf-field-group | PASS | Removes mixed UI label |
| RU labels Hero image / CTA URL | hero group | PASS | No meta rename |

## 7. Admin validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| #73 edit loads | yes | groups via ACF for post_id=73 | PASS |
| Layout block separate | yes | Service — Layout | PASS |
| Hero block separate | yes | Hero страницы услуги | PASS |
| Mixed label removed | yes | not in active groups | PASS |
| Hero fields populated | yes | lead+media=304+cta | PASS |
| Section fields remain | yes | 63 fields parity | PASS |
| Admin order logical | yes | Layout0 / Hero1 / Раздел2 | PASS |
| Save validation | no errors | no fatal | PASS |

Evidence: `REPORTS/evidence/v9-06e46-fix01-admin-validation.csv`

## 8. Frontend validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| `/uslugi/zavisimosti/` HTTP | 200 | 200 | PASS |
| Visual preserved | yes | fingerprint match vs FIX01 backup | PASS |
| Hero unchanged | yes | same snapshot length/hash | PASS |
| Section blocks unchanged | yes | content markers present | PASS |
| Frozen Home unchanged | yes | 74 fields; gallery slide order variance only | PASS |
| Frozen `/uslugi/` unchanged | yes | fingerprint match | PASS |

## 9. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/uslugi/zavisimosti/` | 200 | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | |
| `#314` narkoticheskaya | 200 | PASS | |
| `#74` alkogolnaya | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

Evidence: `REPORTS/evidence/v9-06e46-fix01-frontend-validation.csv`

## 10. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| FieldGroups.php | WORDPRESS/plugins/shpigovsky-core/src/Fields/ | wp-content/plugins/shpigovsky-core/src/Fields/ | YES | PASS |
| ServiceSectionParity.php | WORDPRESS/plugins/.../Fields/ | wp-content/plugins/.../Fields/ | YES | PASS |
| group_fp02_service_hero.json | WORDPRESS/acf-json/ | wp-content/acf-json/ | YES | PASS |
| group_fp02_service_layout_hero.json | WORDPRESS/acf-json/ | wp-content/acf-json/ | YES | PASS |
| group_fp02_service_section_parity.json | WORDPRESS/acf-json/ | wp-content/acf-json/ | YES | PASS |
| v9-style.css | (not modified) | runtime == FIX01 backup | YES | PASS |

## 11. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E46-FIX01-service-section-hero-admin-separation.md | created | PASS | this file |
| SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md | updated | PASS | Layout/Hero separation |
| PROJECT-STATUS.md | updated | PASS | |
| WORDPRESS/SOURCE-AUTHORITY.md | updated | PASS | |
| v9-06e46-fix01-service-hero-layout-group-audit.csv | created | PASS | |
| v9-06e46-fix01-zavisimosti-admin-frontend-recheck.csv | created | PASS | |
| v9-06e46-fix01-service-section-hardcoded-recheck.csv | created | PASS | |
| v9-06e46-fix01-admin-validation.csv | created | PASS | |
| v9-06e46-fix01-frontend-validation.csv | created | PASS | |

## 12. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty (no staging) |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local service section admin polish; persistence handled separately |
| Push attempted | NO |

### Git classification (read-only)

| Class | Paths / notes |
|---|---|
| Intended FP-0002 E46-FIX01 | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php`, `ServiceSectionParity.php`, `WORDPRESS/acf-json/group_fp02_service_*.json`, REPORTS/*, DOCS/*, PROJECT-STATUS.md, SOURCE-AUTHORITY.md |
| Runtime-only | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\...` (plugin/acf-json copies; not in AI MARS git) |
| DB changes | 5× `acf-field-group` → `acf-disabled` |
| Media | none |
| Docs/evidence | REPORT + evidence CSVs |
| Foreign WIP | remaining WIP under AI MARS (untouched) |

## 13. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Multiple legacy DB ACF group duplicates for other service groups (Structured Sections) | low | accepted residual | Optional later soft-disable cleanup; out of FIX01 |
| Stages item bodies still theme defaults | medium | documented | CREATE_V9_06E46_FIX02_TASK if operator wants full modeling |
| Hub/catalog fields still live under Layout group | low | accepted | Clear hub heading added; separate catalog group only if operator asks |
| Home gallery slide order variance in snapshot | low | unrelated | Not caused by FIX01; Home ACF untouched |

## 14. Final verdict

PASS

V9-06E46-FIX01 Service section hero/admin separation:
COMPLETE

Hero/layout separation:
PASS

Admin/frontend recheck:
PASS

Hardcoded recheck:
PASS

Small fixes:
PASS

Base page frontend preserved:
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

## 15. Recommended next action

OPERATOR_REVIEW_REQUIRED

(If stages item bodies / mid-CTA copy modeling required after review → CREATE_V9_06E46_FIX02_TASK. If section accepted → freeze path. Service general admin parity remains later.)

## 16. Final safety statement

Target folder:
X:\AI MARS

V9-06E46-FIX01 Service section hero/admin separation performed:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

DB writes:
5

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
