# REPORT — FP-0002 V9-06E45-FIX02 RENAME ALCOHOL SPECIAL LAYOUT

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | 8341f5690827df2c43d4f552132f9ca56426cfb7 |
| Staged files before | 0 |
| WIP count only | 778 (preflight snapshot; foreign WIP present) |
| Runtime/source canon detected | YES — FP-0002 source under `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS`; runtime `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky` |
| Home frozen state untouched | YES |
| Services hub frozen visual untouched | YES |
| Commit allowed | NO |
| Result | PASS (unpushed foreign metabot commits exist; out of scope — commit/push skipped) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e45-fix02-rename-alcohol-special-before-20260714-183309\` |
| DB dump | `db/mars_wp_fp0002.sql` SHA256=`63A06EBEE75646C9515439946BEB8E0B83539A2775EE8781551E6EB27235F075` (size 2736521; mysqldump PROCESS tablespace warning ignored, dump complete) |
| Theme backup/hash | `theme/shpigovsky` — 635 files; inventories/theme-sha256.txt |
| Plugin backup/hash | `plugin/shpigovsky-core` — 23 files; inventories/plugin-sha256.txt |
| ACF JSON backup/hash | `acf-json` — 10 files; inventories/acf-json-sha256.txt |
| Service ACF group export before | `exports/group_fp02_service_layout_hero.before.json` (+ runtime ACF JSON tree) |
| Service layout meta export before | `exports/service-layout-meta-before.tsv` (29 services) |
| Frontend snapshots before | home/hub/subdivision/alcohol/narcotic/depressiya/heroin `*-before.html` + route-smoke-before.csv |
| Result | PASS |

## 3. Reference audit

| Reference type | Count | Renamed | Kept as legacy alias | Kept as content | Notes |
|---|---:|---:|---:|---:|---|
| ACF choice / admin label / help | 6 | 6 | 0 | 0 | `service_general` + «Услуга»; alcohol_special removed from selectable choices |
| Resolver / map / sync data value | 8 | 5 | 3 | 0 | alias map + validation allowlist retain alcohol_special |
| Frontend slug / template checks | 12 | 10 | 2 | 0 | active slug `service-general`; helper accepts legacy `alcohol-special` |
| Partial/file names (alcohol-stack, alcohol-direct-v9) | 3 | 0 | 3 | 0 | risky rename avoided; comments updated |
| Page content «алкогольная зависимость» | 1+ | 0 | 0 | 1+ | topic of #74 — not layout label |
| Historical reports/validation JSON | many | 0 | 0 | 0 | skip historical report |

Evidence: `REPORTS/evidence/v9-06e45-fix02-alcohol-special-reference-audit.csv`

## 4. Technical layout rename

| Item | Before | After | Result | Notes |
|---|---|---|---|---|
| Active service stack value | alcohol_special | service_general | PASS | |
| Admin label | Алкогольная зависимость / alcohol_special wording | Услуга | PASS | ACF probe confirmed |
| Role service mapping | alcohol_special | service_general | PASS | ServiceLayoutGovernance::map_role_to_layout |
| Legacy alias | alcohol_special | supported | PASS | map + normalize on save + RepeaterValidation |

## 5. Data migration

| Metric | Count | Result | Notes |
|---|---:|---|---|
| Posts with alcohol_special before | 26 | PASS | service CPT meta only |
| Migrated to service_general | 26 | PASS | UPDATE joined to post_type=service |
| Posts with alcohol_special after | 0 | PASS | |
| Posts with service_general after | 26 | PASS | + 3 subdivision roots unchanged |
| #74 alcohol page migrated | yes | PASS | role service, override 0, layout service_general |

Evidence: `v9-06e45-fix02-layout-value-migration-plan.csv`, `...-results.csv`

## 6. Effective layout validation

| Case | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| role section (#73) | subdivision | subdivision | PASS | WP probe |
| role service (#74/#314/#78) | service_general / service-general | service_general → service-general | PASS | |
| legacy alcohol_special value | service_general alias | map → service-general | PASS | shpigovsky_map_acf_layout_to_variant |
| override selected service_general | service_general | N/A seed (override off) | PASS | choice present; sync path covers normalize |

## 7. Admin validation

| Page | ID | Role | Technical layout | Alcohol naming removed | Fields visible | Result |
|---|---:|---|---|---|---|---|
| Зависимости | 73 | section | subdivision | YES | section lead conditional | PASS |
| Alcohol page | 74 | service | service_general | YES | service stack; static by ID | PASS |
| Narcotic dependency | 314 | service | service_general | YES | child services settings | PASS |
| Depression | 78 | service | service_general | YES | service stack | PASS |

ACF choices probe: `alcohol_special` not selectable; `service_general` → «Услуга»; default `service_general`.

Evidence: `v9-06e45-fix02-admin-validation.csv`

## 8. Frontend validation

| Route | Expected stack | HTTP | Visual preserved | Result | Notes |
|---|---|---:|---|---|---|
| `/` | Home frozen | 200 | YES (Δ bytes +19 noise) | PASS | no PHP fatal |
| `/uslugi/` | Services hub frozen | 200 | YES (Δ bytes 0) | PASS | exact byte match vs before snapshot |
| `/uslugi/zavisimosti/` | subdivision | 200 | YES | PASS | body:subdivision |
| alcohol page | service_general | 200 | YES | PASS | body:leaf + service-general + legacy class; bordered info preserved |
| narcotic dependency | service_general + child block | 200 | YES | PASS | child-services cards present |
| depression/leaf | service_general | 200 | YES | PASS | |
| heroin child | service_general | 200 | YES | PASS | |

Evidence: `v9-06e45-fix02-frontend-validation.csv`

## 9. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| service-helpers.php | WORDPRESS/theme/.../inc/ | wp-content/themes/.../inc/ | YES | PASS |
| service-template-loader.php | WORDPRESS/theme/.../inc/ | wp-content/themes/.../inc/ | YES | PASS |
| ServiceLayoutGovernance.php | WORDPRESS/plugins/.../Admin/ | wp-content/plugins/.../Admin/ | YES | PASS |
| FieldGroups.php | WORDPRESS/plugins/.../Fields/ | wp-content/plugins/.../Fields/ | YES | PASS |
| group_fp02_service_layout_hero.json | WORDPRESS/acf-json/ | wp-content/acf-json/ | YES | PASS |
| Operator v9-style.css | (not modified this task) | runtime == FIX02 backup hash | YES | PASS |

Note: source-tree `v9-style.css` already differed from runtime before this task (foreign WIP). **Runtime operator CSS was not overwritten.**

## 10. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E45-FIX02-rename-alcohol-special-layout.md | created | PASS | this file |
| SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md | updated | PASS | FIX02 model |
| PROJECT-STATUS.md | updated | PASS | |
| WORDPRESS/SOURCE-AUTHORITY.md | updated | PASS | FIX02 section appended |
| v9-06e45-fix02-alcohol-special-reference-audit.csv | created | PASS | |
| v9-06e45-fix02-layout-value-migration-plan.csv | created | PASS | |
| v9-06e45-fix02-layout-value-migration-results.csv | created | PASS | |
| v9-06e45-fix02-admin-validation.csv | created | PASS | |
| v9-06e45-fix02-frontend-validation.csv | created | PASS | |

## 11. Git result

| Item | Value |
|---|---|
| Staged before | 0 |
| Staged after | 0 |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local technical layout rename; persistence handled separately |
| Push attempted | NO |

### Classification (read-only `git status --short`)

- **Intended FP-0002 E45-FIX02:** theme/plugin resolver+ACF+governance rename files; ACF JSON layout hero; DOCS governance; PROJECT-STATUS; SOURCE-AUTHORITY; FIX02 REPORT + evidence CSVs; ServiceLayoutGovernance.php (also from E45 wave, still untracked).
- **Runtime-only:** Localhost theme/plugin/acf-json delivery copies under `X:\MARS-Localhost\...` (outside git).
- **DB changes:** 26× `service_layout_variant` meta (`alcohol_special`→`service_general`) in `mars_wp_fp0002`.
- **Media changes:** none.
- **Docs/evidence:** FIX02 report + 5 evidence CSVs + governance/status/authority updates.
- **Foreign WIP:** large prior FP-0002 + other repo WIP (incl. home templates, unrelated ACF JSON, metabot unpushed commits); left untouched.

## 12. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Legacy partial filename `alcohol-stack.php` still alcohol-named | Low | Accepted | Optional later rename with dual include |
| Source `v9-style.css` diverges from runtime (pre-existing) | Medium | Contained | Do not overwrite operator CSS from divergent source |
| Stale cached ACF JSON on remote envs | Low | N/A local | After persistence, sync ACF JSON + migrate meta |
| Dual body class legacy marker | Low | Intentional | Remove `page-service-alcohol-special-legacy` after freeze |

## 13. Final verdict

PASS

V9-06E45-FIX02 Rename alcohol_special layout:
COMPLETE

Technical value rename:
PASS

Legacy alias:
PASS

Data migration:
PASS

Admin naming:
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

## 14. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 15. Final safety statement

Target folder:
X:\AI MARS

V9-06E45-FIX02 Rename alcohol_special layout performed:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

DB writes:
26

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
