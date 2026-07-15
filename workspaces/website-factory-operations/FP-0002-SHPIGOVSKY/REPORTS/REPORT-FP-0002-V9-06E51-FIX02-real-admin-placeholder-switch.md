# REPORT — FP-0002 V9-06E51-FIX02 REAL ADMIN PLACEHOLDER SWITCH

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | `X:` |
| Label | `AI WS` |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `8341f5690827df2c43d4f552132f9ca56426cfb7` |
| Staged files before | empty |
| WIP count only | ~829 short-status lines (foreign + FP-0002 product WIP) |
| Runtime/source canon detected | YES — runtime `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky`; source `workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS` |
| Previous FIX01 treated as insufficient | YES |
| Home frozen state untouched | YES |
| Services hub frozen visual untouched | YES |
| Sections preserved | YES |
| Services preserved except #78 real switch | YES |
| Commit allowed | NO |
| Result | PASS (remote/HEAD diverge + unpushed foreign commits noted; commit/push skipped per charter) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e51-fix02-real-admin-placeholder-switch-before-20260716-010437\` |
| DB dump | `mars_wp_fp0002.sql` (~3.75 MB); SHA256 `3FC254F58B424CB0…660676` |
| Theme backup/hash | `theme-shpigovsky\` tree hash `64032ea3…fb59979` |
| Plugin backup/hash | `plugin-shpigovsky-core\` tree hash `2c9c7786…0bec89ed` |
| ACF JSON backup/hash | `acf-json\` tree hash `068f600d…c454b00` |
| Postmeta exports before | `#78/#74/#314/#81/#85/#73/#77/#84` under `postmeta\` + layout-summary + `#78` content fingerprint |
| Frontend/admin snapshots before | 10 frontend routes under `snapshots\`; authenticated admin HTML under `snapshots\` / evidence |
| Result | PASS (mysqldump PROCESS tablespace warning non-fatal; dump usable) |

## 3. Real root cause

| Area | Actual issue | Proof | Fix | Result |
|---|---|---|---|---|
| Admin visible control | Radios rendered with bare `name="service_editor_role"` instead of `acf[field_fp02_service_editor_role]` | Pre-fix admin HTML chunk: hidden+radios used bare name; `acf[...]` count=0 for role inputs | Stop overwriting `$field['name']`/`$field['key']` in `prepare_editor_role_field` after `acf_prepare_field()` already built `acf[field_…]` | PASS |
| POST/save path | Browser Update posted role outside `$_POST['acf']`; ACF ignored change; meta stayed `placeholder` | Operator report; DOM audit; FIX01 false-positive used `acf_save_post`/meta only | Correct input names → ACF receives role; full form replay with `_acf_nonce` persists | PASS |
| Role/layout sync | FIX01 sync/guard/resolver helpers were OK but never received posted role from real admin | After FIX02 POST: role=`service`, layout=`service_general` even with stale layout in form | Kept FIX01 sync/guard; FIX02 unlocks them for real admin | PASS |
| Frontend resolver/cache | Followed stored role/layout; stub remained because meta never changed | FE before ~54KB placeholder; after ~112KB full service; no `placeholder-stack` | No resolver change required in FIX02 | PASS |

## 4. Implementation

| File/function | Before | After | Result | Notes |
|---|---|---|---|---|
| `ServiceLayoutGovernance::prepare_editor_role_field` | Forced `$field['name']='service_editor_role'` and `$field['key']=…` | Does not rewrite prepared name/key; only choices/type/label/wrapper | PASS | Source + runtime synced |
| File header comment | E51 / E51-FIX01 | + E51-FIX02 note | PASS | |
| Theme resolver / helpers | FIX01 role-wins | Unchanged | N/A | Still correct |
| ACF JSON | button_group choices include placeholder | Unchanged | N/A | |

## 5. Operator scenario validation

| Step | Expected | Actual | Result | Proof |
|---|---|---|---|---|
| Open #78 admin | shows Заглушка initially | checked=`placeholder`; acf-prefixed inputs=3; bare input names=0 | PASS | `v9-06e51-fix02-admin-78-edit-before-fix.html` |
| Select Услуга | control changed before save | form field set to `service` | PASS | form replay |
| Save/update | request accepted | HTTP 302 `message=1` | PASS | save-trace |
| Reload admin | still shows Услуга | checked=`service` | PASS | `admin-78-edit-after.html` |
| Meta after reload | service/service_general | `service` / `service_general` | PASS | meta-truth |
| Frontend #78 | full service content | HTTP 200; placeholder=N; ~112KB | PASS | frontend-78-after.html |
| Final state | Услуга | `service` / `service_general` | PASS | intentional for operator |

## 6. #78 content preservation

| Check | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| service_general fields | preserved | fingerprint hash match `f63a404a…` before/after | PASS | non-layout metas |
| hero fields | preserved | included in fingerprint | PASS | |
| images/repeaters | preserved | fingerprint unchanged | PASS | |
| post status/url/seo | unchanged | publish; same permalink | PASS | |

## 7. Non-placeholder validation

| Page/Route | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| #74 | full service | service/service_general; 200; no ph | PASS | |
| #314 | full service + child tiles | service; 200; no ph | PASS | |
| #81 | full service | service; 200 | PASS | |
| #85 | full service | service; 200 | PASS | |
| #73/#77/#84 | full sections | section/subdivision; 200 | PASS | |
| Home `/` | unchanged | 200 | PASS | HTTP only; freeze untouched |
| Services hub `/uslugi/` | unchanged | 200 | PASS | HTTP only |

## 8. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/uslugi/zavisimosti/` | 200 | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | |
| #78 depressiya | 200 | PASS | final Услуга |
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
| ServiceLayoutGovernance.php | WORDPRESS/plugins/.../ServiceLayoutGovernance.php | plugins/.../ServiceLayoutGovernance.php | YES | PASS | SHA256 `278BDB3F…BB4E1C` |
| v9-style.css | operator runtime CSS | same | YES | PASS | `11A45ABE…` vs FIX02 pre-backup |

## 10. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E51-FIX02-real-admin-placeholder-switch.md | created | PASS | this file |
| SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md | updated | PASS | FIX02 note + backup |
| SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md | updated | PASS | FIX02 sections untouched note |
| PROJECT-STATUS.md | updated | PASS | current phase FIX02; FIX01 marked false-positive |
| SOURCE-AUTHORITY.md | updated | PASS | FIX02 entry; FIX01 corrected |
| evidence CSVs | created | PASS | 10 required CSVs |

## 11. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local real admin placeholder switch bugfix; persistence handled separately |
| Push attempted | NO |

### Git classification (read-only `git status --short`)

| Class | Items |
|---|---|
| Intended FP-0002 E51-FIX02 source | `WORDPRESS/plugins/shpigovsky-core/src/Admin/ServiceLayoutGovernance.php` |
| #78 DB final state Услуга | runtime DB only (not git) |
| Docs/evidence/report | REPORT FIX02 + evidence `v9-06e51-fix02-*` + DOCS/PROJECT-STATUS/SOURCE-AUTHORITY updates |
| Existing uncommitted product (E46–E51) | prior FP-0002 REPORTS/WORDPRESS/DOCS WIP |
| Foreign WIP | MetaBOT / other workspace noise (~829 lines total); not touched |

## 12. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Operator visual glance still needed (automation used auth cookies + form replay, not Playwright GUI click) | low | mitigated | OPERATOR_REVIEW_REQUIRED — open `#78` admin and FE |
| Any future `prepare_field` rewriting ACF `name` | high | mitigated | FIX02 comment + parity model rule |
| E51-FIX01 false trust of meta simulation | medium | corrected | SOURCE-AUTHORITY + PROJECT-STATUS marked insufficient |
| Incomplete ACF POST without `_acf_nonce` | low | noted | Real browser send includes nonce; replay scripts must too |

## 13. Final verdict

PASS

V9-06E51-FIX02 Real admin placeholder switch:
COMPLETE

Previous FIX01 false-positive corrected:
PASS

Backup:
PASS

Real root cause identified:
PASS

Admin control save/reload:
PASS

Frontend changes after save:
PASS

#78 final state Услуга:
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

V9-06E51-FIX02 Real admin placeholder switch performed:
YES

Previous FIX01 treated as insufficient:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

Section pages touched:
NO

Service pages touched:
YES_ONLY_#78_REAL_SWITCH

#78 final state:
УСЛУГА

DB writes:
1 (real wp-admin Update for #78 role/layout; content metas unchanged fingerprint)

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

## Execution safety
- cwd: `X:\AI MARS`
- scope lock honored: yes (`X:\AI MARS` + `X:\MARS-Localhost` authorized runtime/backup)
- destructive ops: none
- protected zone touch: none
