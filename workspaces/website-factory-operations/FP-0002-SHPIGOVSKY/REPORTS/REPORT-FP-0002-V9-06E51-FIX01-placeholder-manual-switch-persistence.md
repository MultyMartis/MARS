# REPORT — FP-0002 V9-06E51-FIX01 PLACEHOLDER MANUAL SWITCH PERSISTENCE

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | `X:` |
| Label | `AI WS` |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `8341f5690827df2c43d4f552132f9ca56426cfb7` |
| Staged files before | empty |
| WIP count only | ~828 short-status lines (foreign + FP-0002 product WIP) |
| Runtime/source canon detected | YES — runtime `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky`; source `workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS` |
| Home frozen state untouched | YES |
| Services hub frozen visual untouched | YES |
| Sections preserved | YES |
| Services preserved except #78 switch cycle | YES |
| Commit allowed | NO |
| Result | PASS (remote/HEAD diverge + unpushed foreign commits noted; commit/push skipped per charter) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e51-fix01-placeholder-manual-switch-persistence-before-20260716-001214\` |
| DB dump | `mars_wp_fp0002.sql` (~3.7 MB); SHA256 `3113C705…3C090` |
| Theme backup/hash | `theme-shpigovsky\` + `theme-shpigovsky.sha256manifest.txt` (638 files) |
| Plugin backup/hash | `plugin-shpigovsky-core\` + manifest (25 files) |
| ACF JSON backup/hash | `acf-json\` + manifest (14 files) |
| Postmeta exports before | `#78/#74/#314/#81/#85/#73/#77/#84` under `postmeta\` |
| Frontend snapshots before | 10 routes under `frontend\*-before.html` + `smoke-before.tsv` |
| Result | PASS (mysqldump PROCESS tablespace warning non-fatal; dump usable) |

## 3. Root cause

| Area | Before | Root cause | Fix | Result |
|---|---|---|---|---|
| Manual switch placeholder→service | reverted / stub stuck | (1) Resolver treated `layout=placeholder` as authority even when `role=service` (`OR` early return). (2) Role-only `update_field` / partial saves did not sync technical layout until `acf/save_post`. (3) Technical `service_layout_variant` was removed from the form (`prepare`→`false`), so stale `placeholder` survived in meta. | Role wins in resolver; sync layout on `acf/update_value` for role; guard layout updates against visible role; keep technical field hidden-but-present and pre-aligned | PASS |
| Technical layout sync | incomplete on non-form paths | sync only on `acf/save_post` priority 20 | `sync_layout_when_role_updated` + `apply_role_layout_sync` + posted-role preference | PASS |
| Hidden/stale field overwrite | possible | hidden field omitted; stale meta / stale POST could fight role | `guard_layout_value_against_role` + `prepare_technical_layout_field` | PASS |

## 4. Save/sync implementation

| File/function | Before | After | Result | Notes |
|---|---|---|---|---|
| `ServiceLayoutGovernance::register` | save_post + prepare hides | + `update_value` role/layout guards; technical layout prepare | PASS | |
| `sync_layout_from_role_on_save` | `get_field` only | `get_effective_editor_role` (inflight/POST/meta) → `apply_role_layout_sync` | PASS | |
| `sync_layout_when_role_updated` | n/a | sync layout immediately when role written | PASS | |
| `guard_layout_value_against_role` | n/a | force layout to map(role) if mismatch | PASS | |
| `prepare_technical_layout_field` | `return false` | hidden wrapper + value aligned to role | PASS | |
| `shpigovsky_resolve_service_layout_variant` | `role\|\|layout` placeholder | explicit role wins first | PASS | |

## 5. #78 switch cycle validation

| Step | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| Start placeholder | role/layout placeholder | placeholder/placeholder; stub FE | PASS | |
| Save as Услуга | persists service/service_general | service/service_general; full FE | PASS | stale layout POST included |
| Frontend as Услуга | full service content | HTTP 200; no placeholder-stack; blocks present | PASS | |
| Save as Заглушка | persists placeholder/placeholder | placeholder/placeholder; stub FE | PASS | |
| Frontend as Заглушка | stub only | placeholder-stack + H1 | PASS | |
| Final state | Заглушка | placeholder/placeholder | PASS | |

## 6. #78 content preservation

| Check | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| service_general fields | preserved | fingerprint hash match; 219 non-layout keys | PASS | |
| hero fields | preserved | included in fingerprint | PASS | |
| images/repeaters | preserved | missing/added keys empty | PASS | |
| post status/url/seo | unchanged | publish; same permalink | PASS | |

## 7. Non-placeholder validation

| Page/Route | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| #74 | full service | service/service_general; 200 | PASS | |
| #314 | full service + child tiles | service; child-services YES; 200 | PASS | |
| #81 | full service | service; 200 | PASS | |
| #85 | full service | service; 200 | PASS | |
| #73/#77/#84 | full sections | section/subdivision; 200 | PASS | |
| Home `/` | unchanged | 200 | PASS | |
| Services hub `/uslugi/` | unchanged | 200 | PASS | |

## 8. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/uslugi/zavisimosti/` | 200 | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | |
| #78 depressiya | 200 | PASS | final placeholder |
| #74 alcohol | 200 | PASS | |
| #314 narko | 200 | PASS | |
| #81 trevoga | 200 | PASS | |
| #85 anoreksiya | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

## 9. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result | Notes |
|---|---|---|---|---|---|
| ServiceLayoutGovernance.php | WORDPRESS/plugins/.../ServiceLayoutGovernance.php | plugins/.../ServiceLayoutGovernance.php | YES | PASS | |
| service-helpers.php | WORDPRESS/theme/.../service-helpers.php | themes/.../service-helpers.php | YES | PASS | |
| v9-style.css | operator runtime CSS | same | YES | PASS | `11A45ABE…` vs pre-backup |

## 10. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E51-FIX01-placeholder-manual-switch-persistence.md | created | PASS | this file |
| SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md | updated | PASS | E51-FIX01 note; obsolete FIX03 message claim corrected |
| SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md | updated | PASS | E51-FIX01 persistence note |
| PROJECT-STATUS.md | updated | PASS | current phase E51-FIX01 |
| SOURCE-AUTHORITY.md | updated | PASS | E51-FIX01 entry |
| evidence CSVs | created | PASS | 8 files under `REPORTS/evidence/v9-06e51-fix01-*` |

## 11. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local placeholder manual switch bugfix; persistence handled separately |
| Push attempted | NO |

## 12. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Nested empty role still defaults to service on save sync | Low | Accepted | Depth model; explicit placeholder still persists |
| Gutenberg/JS form edge cases | Low | Mitigated | update_value + guard + resolver role-wins |
| DB change for #78 local only | Info | Accepted | Not in git |
| Remote HEAD diverge / unpushed foreign WIP | Process | Noted | No git reconciliation in this task |

## 13. Final verdict

PASS

V9-06E51-FIX01 Placeholder manual switch persistence:
COMPLETE

Backup:
PASS

Root cause identified:
PASS

Manual switch placeholder→service:
PASS

Manual switch service→placeholder:
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

V9-06E51-FIX01 Placeholder manual switch persistence performed:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

Section pages touched:
NO

Service pages touched:
YES_ONLY_#78_SWITCH_CYCLE

DB writes:
~20 (#78 role/layout switch-cycle + validation restores; layout/role metas only)

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
