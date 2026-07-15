# REPORT — FP-0002 V9-06E51 PLACEHOLDER LAYOUT MODE RESTORE

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | `X:` |
| Label | `AI WS` |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `8341f5690827df2c43d4f552132f9ca56426cfb7` |
| Staged files before | empty |
| WIP count only | ~825 short-status lines (foreign + FP-0002 product WIP) |
| Runtime/source canon detected | YES — runtime `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky`; source `workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS` |
| Home frozen state untouched | YES |
| Services hub frozen visual untouched | YES |
| Sections preserved | YES |
| Services preserved except #78 test | YES |
| Commit allowed | NO |
| Result | PASS (remote/HEAD diverge noted; commit/push skipped per charter) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e51-placeholder-layout-mode-restore-before-20260715-234500\` |
| DB dump | `mars_wp_fp0002.sql` (~3.6 MB); SHA256 `7BEE8C85…28C6` |
| Theme backup/hash | `theme-shpigovsky\` + `theme-shpigovsky.sha256manifest.txt` (637 files) |
| Plugin backup/hash | `plugin-shpigovsky-core\` + manifest (25 files) |
| ACF JSON backup/hash | `acf-json\` + manifest (13 files) |
| Uploads inventory/copy | `uploads-inventory.txt` (134 lines); inventory-only |
| Postmeta exports before | `#78/#74/#314/#81/#85/#73/#77/#84/#4/#5/#11/#12/#20/#1030` |
| Frontend snapshots before | 14 routes under `frontend\*-before.html` |
| Result | PASS (mysqldump PROCESS tablespace warning non-fatal; dump usable) |

## 3. Existing placeholder audit

| Location | Before | Reused | Action | Result | Notes |
|---|---|---|---|---|---|
| `service_editor_role` | section/service only (placeholder demoted E45-FIX01) | YES | restored **Заглушка** | PASS | Nest: Услуга\|Заглушка |
| `service_layout_variant=placeholder` | Legacy / mapped to leaf | YES | active stub stack | PASS | no longer leaf alias |
| Historical `placeholder-stack` | referenced in E11 inventory; file missing | YES | recreated true stub | PASS | H1 only |
| List column Заглушка | present | YES | kept | PASS | EditorRestrictions |
| Page shared layout | absent | NEW | `page_layout_mode` on generic.php | PASS | default full |
| Image `service-placeholder.svg` | image fallback | NO | untouched | N/A | name-only collision |

Evidence: `REPORTS/evidence/v9-06e51-placeholder-existing-mode-audit.csv`

## 4. Layout option implementation

| Area | Field/group | Before choices | After choices | Result | Notes |
|---|---|---|---|---|---|
| Services | `service_editor_role` / `group_fp02_service_layout_hero` | Раздел / Услуга | Раздел / Услуга / **Заглушка** | PASS | RU help: temporary stub; content preserved |
| Services technical | `service_layout_variant` | placeholder=Legacy | placeholder=**Заглушка** | PASS | still hidden; synced |
| Pages | `page_layout_mode` / `group_fp02_page_layout_mode` | n/a | Полная страница / Заглушка | PASS | generic.php only |
| Sections | same service selector | section | option available | PASS | `#73/#77/#84` remain section |

## 5. Placeholder frontend behavior

| Page | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| #78 Депрессия | header/nav/H1/footer only | HTTP 200; `<main>` = placeholder-stack with H1 «Депрессия»; no service blocks; child-services CSS gated off | PASS | URL unchanged |

## 6. #78 content preservation

| Check | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| ACF service content preserved | yes | 164 meta keys before/after; 71 hero/service_general keys stable | PASS | |
| Only layout meta changed | yes | 2 changed keys: `service_editor_role`, `service_layout_variant` (disallowed=0) | PASS | override stayed 0 |
| Post status unchanged | yes | publish | PASS | |
| URL unchanged | yes | `/uslugi/psihicheskoe-zdorovie/depressiya/` | PASS | |
| SEO/noindex unchanged | yes | no intentional change | PASS | |

Meta change: `service`/`service_general` → `placeholder`/`placeholder`.

## 7. Non-placeholder validation

| Page/Route | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| #74 | full service | 200 + service blocks | PASS | |
| #314 | full service | 200 + service blocks | PASS | |
| #81 | full service | 200 + service blocks | PASS | |
| #85 | full service | 200 + service blocks | PASS | |
| #73/#77/#84 | full sections | 200 + section content | PASS | placeholder option not selected |
| Home `/` | unchanged | 200 | PASS | freeze untouched |
| Services hub `/uslugi/` | unchanged | 200 | PASS | freeze untouched |

## 8. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/uslugi/zavisimosti/` | 200 | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | |
| #78 depressiya | 200 | PASS | placeholder |
| #74 alcohol | 200 | PASS | |
| #314 narko | 200 | PASS | |
| #81 trevoga | 200 | PASS | |
| #85 anoreksiya | 200 | PASS | |
| #75 profilaktika | 200 | PASS | |
| #79 ptsr | 200 | PASS | slug `ptsr` (not `ptrs`) |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

## 9. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result | Notes |
|---|---|---|---|---|---|
| FieldGroups.php | WORDPRESS/plugins/.../FieldGroups.php | wp-content/plugins/... | YES | PASS | |
| ServiceLayoutGovernance.php | WORDPRESS/plugins/... | wp-content/plugins/... | YES | PASS | |
| service-helpers.php | WORDPRESS/theme/... | themes/shpigovsky/... | YES | PASS | |
| service-template-loader.php | WORDPRESS/theme/... | themes/... | YES | PASS | |
| assets.php | WORDPRESS/theme/... | themes/... | YES | PASS | child CSS gate |
| placeholder-stack.php | WORDPRESS/theme/... (new) | themes/... | YES | PASS | |
| generic.php | WORDPRESS/theme/... | themes/... | YES | PASS | |
| group_fp02_service_layout_hero.json | WORDPRESS/acf-json/... | wp-content/acf-json/... | YES | PASS | |
| group_fp02_page_layout_mode.json | WORDPRESS/acf-json/... (new) | wp-content/acf-json/... | YES | PASS | |
| v9-style.css | (operator runtime) | themes/.../v9-style.css | N/A preserved | PASS | hash `11A45ABE…` =

pre-backup |

## 10. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E51-placeholder-layout-mode-restore.md | created | PASS | this file |
| SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md | updated | PASS | E51 note |
| SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md | updated | PASS | E51 availability note |
| SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md | updated | PASS | E51 model |
| PROJECT-STATUS.md | updated | PASS | |
| SOURCE-AUTHORITY.md | updated | PASS | |
| evidence CSVs | created | PASS | 8 files under `REPORTS/evidence/v9-06e51-*` |

## 11. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local placeholder layout mode restore; persistence handled separately |
| Push attempted | NO |

### Classification (read-only `git status --short`)

- Intended FP-0002 E51 source: theme/plugin/ACF JSON under `WORDPRESS/`; report/evidence/docs
- DB change for #78 placeholder mode: local runtime DB only (not git)
- Docs/evidence/report: `REPORTS/`, `DOCS/`, `PROJECT-STATUS.md`, `SOURCE-AUTHORITY.md`
- Existing uncommitted product changes from E46–E50: remain foreign-to-this-wave WIP
- Foreign WIP: MetaBOT / `.recovery-temp` / other projects — **not touched**

## 12. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Operators mass-enable Заглушка on demo catalog | Medium | Mitigated | option available; only #78 enabled for test |
| Nested parity field visibility depends on real role field | Low | Mitigated | nested restores real button_group (FIX02 group filter remains SoT) |
| Page stub limited to generic.php | Low | Accepted | dedicated templates excluded by design |
| Unpushed remote/HEAD diverge | Low | Accepted | charter forbids git reconciliation |

## 13. Final verdict

PASS

V9-06E51 Placeholder layout mode restore:
COMPLETE

Backup:
PASS

Layout option restored:
PASS

#78 placeholder test:
PASS

#78 content preserved:
PASS

Non-placeholder pages preserved:
PASS

Home preserved:
PASS

Services hub preserved:
PASS

Sections preserved:
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

V9-06E51 Placeholder layout mode restore performed:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

Section pages touched:
NO

Service pages touched:
YES_ONLY_#78_TEST

DB writes:
2

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
