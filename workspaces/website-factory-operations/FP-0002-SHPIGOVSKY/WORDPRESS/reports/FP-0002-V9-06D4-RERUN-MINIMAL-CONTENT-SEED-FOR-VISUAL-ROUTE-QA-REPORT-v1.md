# REPORT — FP-0002 V9-06D.4 RERUN MINIMAL CONTENT SEED FOR VISUAL ROUTE QA

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: 1b0fba0e854071d635766e3912802c38b860bf43
- Remote HEAD: 1b0fba0e854071d635766e3912802c38b860bf43
- Ahead: 0
- Behind: 0
- Foreign WIP: present, unstaged/untracked, excluded from scope
- Pre-existing staged files: 0
- Result: **PASS**

## 2. Authorization and scope

- Operator authorization: V9-06D.4 RERUN minimal content seed for visual route QA only
- Required HEAD: 1b0fba0e854071d635766e3912802c38b860bf43
- Authorized Pages: 4, 5, 20
- Authorized Services: 73, 74, 77, 84
- Runtime content writes: **AUTHORIZED MINIMAL SEED ONLY**
- Full content migration: NOT AUTHORIZED / NOT PERFORMED
- V9 integration: NOT AUTHORIZED / NOT STARTED
- Menu changes: NOT AUTHORIZED / 0
- Redirects: NOT AUTHORIZED / 0
- Rewrite flush: NOT PERFORMED
- Options Page values: NOT AUTHORIZED / UNCHANGED
- Result: PASS

## 3. Runtime identity

- Runtime: X:\MARS-Localhost\sites\wordpress\projects\shpigovsky
- Domain: http://shpigovsky.test/
- Theme: shpigovsky
- Shpigovsky Core: active
- Core mode: content_model
- Service CPT: registered
- Services total: 15
- Authorized Pages exist: YES (4, 5, 20)
- Authorized Services exist: YES (73, 74, 77, 84)
- ACF PRO: active
- ACF groups: 13
- Options Page: registered (fp02-site-settings)
- WPilot write_enabled: false
- Frontend: HTTP 200
- wp-admin: HTTP 302
- Result: **PASS**

## 4. Pre-write baseline

| Object | ID | Type | Path | Content hash | ACF/meta state | Result |
|---|---:|---|---|---|---|---|
| Home | 4 | page | / | present | ACF empty; no migration meta | CAPTURED |
| Services Hub | 5 | page | /uslugi/ | present | ACF empty; no migration meta | CAPTURED |
| Contacts | 20 | page | /kontakty/ | present | ACF empty; no migration meta | CAPTURED |
| Зависимости | 73 | service | /uslugi/zavisimosti/ | present | skeleton meta; ACF content empty | CAPTURED |
| Лечение алкогольной зависимости | 74 | service | /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | present | skeleton meta; ACF content empty | CAPTURED |
| Психическое здоровье | 77 | service | /uslugi/psihicheskoe-zdorovie/ | present | skeleton meta; ACF content empty | CAPTURED |
| Расстройства пищевого поведения | 84 | service | /uslugi/rasstroystva-pischevogo-povedeniya/ | present | skeleton meta; ACF content empty | CAPTURED |

Global baseline:

- Pages: 23
- Services: 15
- Posts: 0
- Menus: 3
- Front page: 4
- Posts page: 19
- Options snapshot: captured (show_on_front/page_on_front/page_for_posts/permalink_structure/rewrite_rules hash)
- Active plugins: 4 (ACF PRO, ACF Extended PRO, WPilot, Shpigovsky Core)
- Active theme: shpigovsky
- Result: **PASS**

Evidence: `validation/v9-06d4-minimal-content-seed-rerun/pre-write-baseline.json`

## 5. Checkpoint

- Name: v9-06d4-rerun-minimal-content-seed-pre-20260704-054146
- Root: X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d4-rerun-minimal-content-seed-pre-20260704-054146
- DB dump: database/mars_wp_fp0002-v9-06d4-rerun-pre.sql (1,404,384 bytes)
- Object baseline: object-baseline/authorized-object-baseline.json
- Rollback instructions: rollback/ROLLBACK-INSTRUCTIONS.md
- Secrets copied: 0
- Result: **PASS**

## 6. Dry-run seed plan

| Object | ID | Planned fields | Native fields | ACF/meta fields | Risk | Result |
|---|---:|---|---:|---:|---|---|
| Home | 4 | hero/nav/cta + migration meta | 0 | 6 | LOW | PASS |
| Services Hub | 5 | intro/query/placeholders + meta | 0 | 5 | LOW | PASS |
| Contacts | 20 | address/phones/form intro + meta | 0 | 5 | LOW | PASS |
| Зависимости | 73 | layout/hero + meta | 0 | 5 | LOW | PASS |
| Алкоголь | 74 | layout/hero/intro/signs + meta | 0 | 7 | LOW | PASS |
| Психическое здоровье | 77 | layout/hero + meta | 0 | 5 | LOW | PASS |
| РПП | 84 | layout/hero + meta | 0 | 5 | LOW | PASS |

- Planned object count: 7
- Unauthorized objects: 0
- Menu changes planned: NO
- Options changes planned: NO
- Redirects planned: NO
- Rewrite flush planned: NO
- V9 HTML copy planned: NO
- Result: **SAFE_TO_APPLY_WITH_DB_CHECKPOINT**

## 7. Apply result

| Object | ID | Native writes | ACF/meta writes | Failed writes | Result |
|---|---:|---:|---:|---:|---|
| Home | 4 | 0 | 6 | 0 | PASS |
| Services Hub | 5 | 0 | 5 | 0 | PASS |
| Contacts | 20 | 0 | 5 | 0 | PASS |
| Зависимости | 73 | 0 | 5 | 0 | PASS |
| Алкоголь | 74 | 0 | 7 | 0 | PASS |
| Психическое здоровье | 77 | 0 | 5 | 0 | PASS |
| РПП | 84 | 0 | 5 | 0 | PASS |

- Pages modified: 3
- Services modified: 4
- Posts modified: 0
- Menus changed: 0
- Options changed: 0
- Rewrite flush: NOT PERFORMED
- Result: **PASS**

## 8. Authorized object validation

| Object | ID | Slug unchanged | Parent unchanged | Status unchanged | Fields as planned | Result |
|---|---:|---:|---:|---:|---:|---|
| Home | 4 | YES | YES | YES | YES | PASS |
| Services Hub | 5 | YES | YES | YES | YES | PASS |
| Contacts | 20 | YES | YES | YES | YES | PASS |
| Зависимости | 73 | YES | YES | YES | YES | PASS |
| Алкоголь | 74 | YES | YES | YES | YES | PASS |
| Психическое здоровье | 77 | YES | YES | YES | YES | PASS |
| РПП | 84 | YES | YES | YES | YES | PASS |

## 9. ACF/meta seed validation

- ACF fields written: YES (authorized objects only)
- Native content fields written: NO
- Skeleton/migration status: minimal_seed / MINIMAL_SEED
- Production content: NO
- ACF Extended PRO used: NO
- Options values written: NO
- Result: **PASS**

## 10. Global immutability audit

| Object/state | Before | After | Changed | Result |
|---|---:|---:|---:|---|
| Pages total | 23 | 23 | NO | PASS |
| Services total | 15 | 15 | NO | PASS |
| Posts total | 0 | 0 | NO | PASS |
| Menus | 3 | 3 | NO | PASS |
| front page option | 4 | 4 | NO | PASS |
| posts page option | 19 | 19 | NO | PASS |
| active plugins | 4 | 4 | NO | PASS |
| active theme | shpigovsky | shpigovsky | NO | PASS |
| categories | unchanged | unchanged | NO | PASS |
| tags | unchanged | unchanged | NO | PASS |
| users | unchanged | unchanged | NO | PASS |
| rewrite rules hash | unchanged | unchanged | NO | PASS |

## 11. Route QA readiness

| URL | Expected object | HTTP status | Generated permalink match | Result |
|---|---|---:|---:|---|
| / | Page 4 | 200 | YES | PASS |
| /uslugi/ | Page 5 | 200 | YES | PASS |
| /uslugi/zavisimosti/ | Service 73 | 200 | YES | PASS |
| /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | Service 74 | 404 | YES | REWRITE_FLUSH_MICRO_GATE_REQUIRED |
| /uslugi/psihicheskoe-zdorovie/ | Service 77 | 200 | YES | PASS |
| /uslugi/rasstroystva-pischevogo-povedeniya/ | Service 84 | 200 | YES | PASS |
| /kontakty/ | Page 20 | 200 | YES | PASS |

- Rewrite flush required: YES (Service 74 HTTP only)
- Rewrite flush performed: NO
- Result: **PARTIAL**

## 12. WPilot verification

- site-info: PASS via WordPress bootstrap
- plugins: PASS via WordPress bootstrap
- themes: PASS via WordPress bootstrap
- pages/services: PASS via WordPress bootstrap
- write_enabled: false
- write operations: 0
- Result: **PASS**

## 13. Rollback readiness

- DB dump: X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d4-rerun-minimal-content-seed-pre-20260704-054146\database\mars_wp_fp0002-v9-06d4-rerun-pre.sql
- Modified object list: 4, 5, 20, 73, 74, 77, 84
- Modified field list: see seeded object registry / dry-run plan
- Restore procedure: restore local DB from checkpoint SQL dump
- Rollback tested: NO
- Rollback not executed reason: apply succeeded
- Result: **READY**

## 14. Validation suites

| Suite | Passed | Failed | Skipped | Result |
|---|---:|---:|---:|---|
| preflight | 1 | 0 | 0 | PASS |
| runtime-identity | 1 | 0 | 0 | PASS |
| pre-write-baseline | 1 | 0 | 0 | PASS |
| checkpoint | 1 | 0 | 0 | PASS |
| dry-run-seed-plan | 1 | 0 | 0 | PASS |
| apply-seed-result | 1 | 0 | 0 | PASS |
| authorized-object-validation | 1 | 0 | 0 | PASS |
| acf-seed-validation | 1 | 0 | 0 | PASS |
| global-immutability-validation | 1 | 0 | 0 | PASS |
| route-qa-readiness-validation | 0 | 0 | 0 | PARTIAL |
| wpilot-readonly-validation | 1 | 0 | 0 | PASS |
| rollback-readiness | 1 | 0 | 0 | READY |
| no-scope-drift-validation | 1 | 0 | 0 | PASS |

- Total failures: 0 (route QA PARTIAL only due to deferred rewrite flush micro-gate)
- Rewrite micro-gate required: YES
- Result: **PARTIAL PASS**

## 15. Documentation changes

| File | Action | Reason |
|---|---|---|
| reports/FP-0002-V9-06D4-RERUN-MINIMAL-CONTENT-SEED-FOR-VISUAL-ROUTE-QA-REPORT-v1.md | CREATE | Rerun report |
| reports/FP-0002-V9-06D4-MINIMAL-CONTENT-SEED-FOR-VISUAL-ROUTE-QA-REPORT-v1.md | PRESERVE | Previous blocked attempt |
| validation/v9-06d4-minimal-content-seed-rerun/* | CREATE | Evidence suite |
| architecture/FP-0002-V9-06D4-RERUN-* | CREATE | Apply plan, registry, URL list, rollback, rewrite status |
| WORDPRESS/README.md | UPDATE | Status |
| WORDPRESS/SOURCE-AUTHORITY.md | UPDATE | Status |
| Forge / V9 status indexes | UPDATE | Operational status |

## 16. Git checkpoint

- Exact staged files: V9-06D.4 rerun documentation/evidence/status only (30 files)
- Runtime files staged: NO
- Runtime snapshots staged: NO
- Database dumps staged: NO
- External plugin files staged: NO
- Plugin ZIPs staged: NO
- Secrets staged: NO
- License keys staged: NO
- Foreign files staged: NO
- Commit: FP-0002: seed minimal WordPress content for route QA
- Commit hash: 998dc71d0f27287addfdb55d87dd634c6eecffd0
- Push: YES (normal, no force)
- Local HEAD: 998dc71d0f27287addfdb55d87dd634c6eecffd0
- Remote HEAD: 998dc71d0f27287addfdb55d87dd634c6eecffd0
- Result: PASS

## 17. No-scope-drift audit

- Runtime files changed: NO
- Database writes: AUTHORIZED_MINIMAL_SEED_ONLY
- WordPress object writes: 7 authorized objects
- Unauthorized object writes: 0
- WPilot writes: 0
- V9 source changed: NO
- V9 dist changed: NO
- Theme/plugin source changed: NO
- Menus changed: NO
- Redirects created: NO
- Rewrite flush: NO
- Options changed: NO
- Plugin updates run: 0
- Plugin installs run: 0
- Plugin deletes run: 0
- ACF Extended PRO used: NO
- ACF Free activated: NO
- Production content migrated: NO
- Unexpected changes: none

## 18. Final verdict

**PARTIAL PASS**

V9-06D.4 rerun:
COMPLETE

Minimal content seed:
COMPLETE

Authorized Pages:
3_MODIFIED

Authorized Services:
4_MODIFIED

Unauthorized object writes:
0

Route QA readiness:
PARTIAL

Rewrite flush:
MICRO_GATE_REQUIRED

Content migration:
MINIMAL_SEED_ONLY

V9 integration:
NOT STARTED

Menus:
UNCHANGED

Redirects:
NOT CREATED

Options Page values:
UNCHANGED

Runtime health:
PASS

Rollback readiness:
READY

V9-06D.5:
BLOCKED pending rewrite flush micro-gate decision for Service 74 HTTP route

## 19. Remaining blockers

1. Service 74 path returns HTTP 404 while generated permalink is correct — requires authorized rewrite flush micro-gate.
2. Historical Page ID 6 also occupies `/uslugi/zavisimosti/`; service/page path ownership should be reviewed in a later cleanup/redirect phase (not D.4).

## 20. Recommended next action

REWRITE_FLUSH_MICRO_GATE
