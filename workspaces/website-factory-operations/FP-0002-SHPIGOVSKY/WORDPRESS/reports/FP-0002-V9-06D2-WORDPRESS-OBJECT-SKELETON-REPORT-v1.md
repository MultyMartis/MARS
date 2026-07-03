# REPORT — FP-0002 V9-06D.2 WORDPRESS OBJECT SKELETON

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: e7ded5e0f704dffd085117e6862fca4e500fd5c3
- Remote HEAD: e7ded5e0f704dffd085117e6862fca4e500fd5c3
- Ahead: 0
- Behind: 0
- Foreign WIP: present, unstaged/untracked, excluded from scope
- Pre-existing staged files: 0
- Result: PASS

## 2. Authorization and scope

- Operator authorization: V9-06D.2 WordPress object skeleton only
- Page skeleton: native Page existence/template reconciliation only
- Service skeleton: 15 `service` CPT skeleton objects
- Content migration: NOT AUTHORIZED / NOT PERFORMED
- V9 integration: NOT AUTHORIZED / NOT STARTED
- Menu changes: NOT AUTHORIZED / 0
- Redirects: NOT AUTHORIZED / 0
- Rewrite flush: NOT PERFORMED
- Result: PASS

## 3. Runtime identity

- Runtime: X:\MARS-Localhost\sites\wordpress\projects\shpigovsky
- Domain: http://shpigovsky.test/
- Theme: shpigovsky 0.2.0-skeleton
- Shpigovsky Core: active
- Core mode: content_model
- Service CPT: registered / hierarchical / archive disabled
- ACF PRO: active 6.8.5
- ACF groups: 13
- Options Page: registered
- WPilot: active
- WPilot write_enabled: false
- Frontend: HTTP 200
- wp-admin: HTTP 302 login redirect acceptable
- Result: PASS

## 4. Pre-object baseline

- Pages: 23
- Services: 0
- Posts: 1
- Menus: 3
- Front page: 4
- Posts page: 19
- Active plugins: 4
- Active theme: shpigovsky
- Users: 2
- Result: PASS

## 5. Checkpoint

- Name: v9-06d2-object-skeleton-pre-20260704-040407
- Root: X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d2-object-skeleton-pre-20260704-040407
- DB dump: created (1406689 bytes)
- Object baseline: X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d2-object-skeleton-pre-20260704-040407\wordpress-state\pre-object-baseline.json
- Rollback instructions: X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d2-object-skeleton-pre-20260704-040407\rollback\ROLLBACK-INSTRUCTIONS.md
- Secrets copied: 0
- Result: PASS

## 6. Dry-run object plan

| Action | Count | Result |
|---|---|---|
| CREATE_PAGE | 0 | PASS |
| RECONCILE_PAGE | 13 | PASS |
| CREATE_SERVICE | 15 | PASS |
| RECONCILE_SERVICE | 0 | PASS |
| SKIP_EXISTING | 2 | PASS |
| BLOCKED_DUPLICATE | 0 | PASS |
| BLOCKED_AMBIGUOUS | 0 | PASS |

- Planned Service count: 15
- Planned Page changes: 13 template-only reconciliations, 0 creates
- Menu changes planned: 0
- Option changes planned: 0
- Result: SAFE_TO_APPLY_WITH_DB_CHECKPOINT

## 7. Apply result

| Object type | Created | Reconciled | Skipped | Failed | Result |
|---|---|---|---|---|---|
| page | 0 | 13 | 2 | 0 | PASS |
| service | 15 | 0 | 0 | 0 | PASS |
| post | 0 | 0 | 1 | 0 | PASS |

- Created Page IDs: []
- Created Service IDs: [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]
- Modified existing Page IDs: [5, 11, 12, 13, 14, 15, 16, 18, 20, 3, 22, 23, 24]
- Modified existing Service IDs: []
- Posts created: 0
- Menus changed: 0
- Options changed: 0
- Result: PASS

## 8. Service object validation

| Registry ID | ID | Title | Slug | Parent | Path | Status | Result |
|---|---|---|---|---|---|---|---|
| SVC-ZAVISIMOSTI | 73 | Зависимости | zavisimosti | none | /uslugi/zavisimosti/ | publish | PASS |
| SVC-ALKOGOL | 74 | Лечение алкогольной зависимости | lechenie-alkogolnoy-zavisimosti | zavisimosti | /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | publish | PASS |
| SVC-PROFILAKTIKA | 75 | Профилактический анализ | profilakticheskiy-analiz | zavisimosti | /uslugi/zavisimosti/profilakticheskiy-analiz/ | publish | PASS |
| SVC-SPECIALISTAM-ZAV | 76 | Специалистам | specialistam | zavisimosti | /uslugi/zavisimosti/specialistam/ | publish | PASS |
| SVC-PSYCH | 77 | Психическое здоровье | psihicheskoe-zdorovie | none | /uslugi/psihicheskoe-zdorovie/ | publish | PASS |
| SVC-DEPRESSIYA | 78 | Депрессия | depressiya | psihicheskoe-zdorovie | /uslugi/psihicheskoe-zdorovie/depressiya/ | publish | PASS |
| SVC-PTRS | 79 | ПТСР | ptrs | psihicheskoe-zdorovie | /uslugi/psihicheskoe-zdorovie/ptrs/ | publish | PASS |
| SVC-VYGORANIE | 80 | Эмоциональное выгорание | emocionalnoe-vygoranie | psihicheskoe-zdorovie | /uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie/ | publish | PASS |
| SVC-TREVOGA | 81 | Тревожные расстройства | trevozhnye-rasstroystva | psihicheskoe-zdorovie | /uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/ | publish | PASS |
| SVC-SON | 82 | Расстройства сна | rasstroystva-sna | psihicheskoe-zdorovie | /uslugi/psihicheskoe-zdorovie/rasstroystva-sna/ | publish | PASS |
| SVC-TRAVMA | 83 | Травма | travma | psihicheskoe-zdorovie | /uslugi/psihicheskoe-zdorovie/travma/ | publish | PASS |
| SVC-RPP | 84 | Расстройства пищевого поведения | rasstroystva-pischevogo-povedeniya | none | /uslugi/rasstroystva-pischevogo-povedeniya/ | publish | PASS |
| SVC-ANOREKSIYA | 85 | Анорексия | anoreksiya | rasstroystva-pischevogo-povedeniya | /uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/ | publish | PASS |
| SVC-BULIMIYA | 86 | Нервная булимия | nervnaya-bulimiya | rasstroystva-pischevogo-povedeniya | /uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya/ | publish | PASS |
| SVC-KOMPULSIV | 87 | Компульсивное переедание | kompulsivnoe-pereedanie | rasstroystva-pischevogo-povedeniya | /uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/ | publish | PASS |

- Total Services: 15
- Extra Services: 0
- Missing Services: 0
- Max depth: 2
- Result: PASS

## 9. Page object validation

| Route/entity | ID | Title | Path | Template | Created/Reused | Result |
|---|---|---|---|---|---|---|
| ROUTE-01 | 4 | Главная | / | default | reused | PASS |
| ROUTE-02 | 5 | Услуги | /uslugi/ | page-templates/services-hub.php | reused | PASS |
| ROUTE-18 | 11 | О центре | /o-centre/ | page-templates/institutional.php | reused | PASS |
| ROUTE-19 | 12 | О нас | /o-centre/o-nas/ | page-templates/institutional.php | reused | PASS |
| ROUTE-20 | 13 | Программа лечения | /o-centre/programma-lecheniya/ | page-templates/institutional.php | reused | PASS |
| ROUTE-21 | 14 | Галерея о доме | /o-centre/galereya-o-dome/ | page-templates/institutional.php | reused | PASS |
| ROUTE-22 | 15 | Специалистам | /o-centre/specialistam/ | page-templates/institutional.php | reused | PASS |
| ROUTE-23 | 16 | Родственникам | /o-centre/rodstvennikam/ | page-templates/institutional.php | reused | PASS |
| ROUTE-24 | 18 | Отзывы | /otzyvy/ | page-templates/reviews.php | reused | PASS |
| ROUTE-25 | 19 | Статьи | /blog/ | default | reused | PASS |
| ROUTE-27 | 20 | Контакты | /kontakty/ | page-templates/contacts.php | reused | PASS |
| ROUTE-28 | 3 | Политика конфиденциальности | /privacy-policy/ | page-templates/legal.php | reused | PASS |
| ROUTE-29 | 22 | Пользовательское соглашение | /user-agreement/ | page-templates/legal.php | reused | PASS |
| ROUTE-30 | 23 | Согласие на обработку персональных данных | /consent-personal-data/ | page-templates/legal.php | reused | PASS |
| ROUTE-31 | 24 | Политика Cookie-файлов | /cookie-files-policy/ | page-templates/legal.php | reused | PASS |

- Services Hub: Page ID 5 / PAGE_OWNED
- Front page: ID 4
- Posts page: ID 19
- Legal pages: templates assigned, production legal content not generated
- Duplicate paths: 0
- Result: PASS

## 10. Permalink readiness

| Registry ID | Expected path | Generated path | HTTP checked | Result |
|---|---|---|---|---|
| SVC-ZAVISIMOSTI | /uslugi/zavisimosti/ | /uslugi/zavisimosti/ | false | PASS |
| SVC-ALKOGOL | /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | false | PASS |
| SVC-PROFILAKTIKA | /uslugi/zavisimosti/profilakticheskiy-analiz/ | /uslugi/zavisimosti/profilakticheskiy-analiz/ | false | PASS |
| SVC-SPECIALISTAM-ZAV | /uslugi/zavisimosti/specialistam/ | /uslugi/zavisimosti/specialistam/ | false | PASS |
| SVC-PSYCH | /uslugi/psihicheskoe-zdorovie/ | /uslugi/psihicheskoe-zdorovie/ | false | PASS |
| SVC-DEPRESSIYA | /uslugi/psihicheskoe-zdorovie/depressiya/ | /uslugi/psihicheskoe-zdorovie/depressiya/ | false | PASS |
| SVC-PTRS | /uslugi/psihicheskoe-zdorovie/ptrs/ | /uslugi/psihicheskoe-zdorovie/ptrs/ | false | PASS |
| SVC-VYGORANIE | /uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie/ | /uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie/ | false | PASS |
| SVC-TREVOGA | /uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/ | /uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/ | false | PASS |
| SVC-SON | /uslugi/psihicheskoe-zdorovie/rasstroystva-sna/ | /uslugi/psihicheskoe-zdorovie/rasstroystva-sna/ | false | PASS |
| SVC-TRAVMA | /uslugi/psihicheskoe-zdorovie/travma/ | /uslugi/psihicheskoe-zdorovie/travma/ | false | PASS |
| SVC-RPP | /uslugi/rasstroystva-pischevogo-povedeniya/ | /uslugi/rasstroystva-pischevogo-povedeniya/ | false | PASS |
| SVC-ANOREKSIYA | /uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/ | /uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/ | false | PASS |
| SVC-BULIMIYA | /uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya/ | /uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya/ | false | PASS |
| SVC-KOMPULSIV | /uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/ | /uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/ | false | PASS |

- Rewrite flush performed: NO
- Rewrite flush required later: NO for generated permalink readiness; HTTP route validation deferred
- Hub ownership: PAGE_OWNED
- Legacy /specyalisty/: PRE_EXISTING PAGE ID 10 UNCHANGED; NOT CREATED BY D.2
- Redirects: 0
- Result: PASS

## 11. ACF/meta skeleton

- Service registry IDs written: 15
- Service layout variants written: 15
- Skeleton status written: 15
- Production ACF content filled: 0
- Options values written: 0
- ACF Extended PRO used: NO
- Result: PASS

## 12. WordPress immutability audit

| Object/state | Before | After | Changed | Result |
|---|---|---|---|---|
| pages_total | 23 | 23 | false | PASS |
| services_total | 0 | 15 | true | PASS |
| posts_total | 1 | 1 | false | PASS |
| menus_total | 3 | 3 | false | PASS |
| menus_hash | ba46a8ec3af57b7b1e41a6356a07fad19adec6300a0c4cc7e9552dbda1139298 | ba46a8ec3af57b7b1e41a6356a07fad19adec6300a0c4cc7e9552dbda1139298 | false | PASS |
| front_page_option | 4 | 4 | false | PASS |
| posts_page_option | 19 | 19 | false | PASS |
| rewrite_rules_hash | 224bcae00dcb5d295717cbceba968d7bbe382172469142516f298f79f1590529 | 224bcae00dcb5d295717cbceba968d7bbe382172469142516f298f79f1590529 | false | PASS |
| active_plugins | 705db8c28ac78258eeee1e431e1d3e1374d169bd39901e1ed1884249a4bd74e7 | 705db8c28ac78258eeee1e431e1d3e1374d169bd39901e1ed1884249a4bd74e7 | false | PASS |
| active_theme | shpigovsky | shpigovsky | false | PASS |
| categories | 1 | 1 | false | PASS |
| tags | 0 | 0 | false | PASS |
| users | 2 | 2 | false | PASS |

## 13. WPilot verification

- site-info: PASS via WordPress bootstrap
- plugins: PASS via WordPress bootstrap
- themes: PASS via WordPress bootstrap
- pages/services: PASS via WordPress bootstrap
- write_enabled: false
- write operations: 0
- Result: PASS

## 14. Rollback readiness

- DB dump: X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d2-object-skeleton-pre-20260704-040407\database\mars_wp_fp0002-v9-06d2-pre.sql
- Created object list: 15 Services, 0 Pages
- Modified object list: 13 existing Page template meta values, 0 Services
- Restore procedure: object cleanup by created IDs or full DB restore from checkpoint SQL dump
- Rollback tested: false
- Rollback not executed reason: apply and validation succeeded
- Result: READY

## 15. Validation suites

| Suite | Passed | Failed | Skipped | Result |
|---|---|---|---|---|
| v9-06d2-object-skeleton | 25 | 0 | 0 | PASS |

- Total failures: 0
- Result: PASS

## 16. Documentation changes

| File | Action | Reason |
|---|---|---|
| WORDPRESS/reports/FP-0002-V9-06D2-WORDPRESS-OBJECT-SKELETON-REPORT-v1.md | created | final D.2 report |
| WORDPRESS/validation/v9-06d2-object-skeleton/*.json | created | validation evidence |
| WORDPRESS/architecture/FP-0002-V9-06D2-OBJECT-SKELETON-PLAN-v1.md | created | object skeleton plan/result |
| WORDPRESS/architecture/FP-0002-V9-06D2-SERVICE-OBJECT-REGISTRY-v1.json | created | service object registry |
| WORDPRESS/architecture/FP-0002-V9-06D2-PAGE-OBJECT-REGISTRY-v1.json | created | page object registry |
| WORDPRESS/architecture/FP-0002-V9-06D2-PERMALINK-READINESS-v1.md | created | permalink readiness |
| WORDPRESS/architecture/FP-0002-V9-06D2-ROLLBACK-PLAN-v1.md | created | rollback readiness |
| WORDPRESS/README.md / SOURCE-AUTHORITY.md / Forge status docs | updated | status alignment |

## 17. Git checkpoint

- Exact staged files: pending final staging
- Runtime files staged: 0
- Runtime snapshots staged: 0
- Database dumps staged: 0
- External plugin files staged: 0
- Plugin ZIPs staged: 0
- Secrets staged: 0
- License keys staged: 0
- Foreign files staged: 0
- Commit: pending final staging
- Commit hash: pending final staging
- Push: pending final staging
- Local HEAD: pending final staging
- Remote HEAD: pending final staging
- Result: pending final staging

## 18. No-scope-drift audit

- Runtime theme files changed: 0
- Runtime plugin files changed: 0
- External plugin files changed: 0
- Plugin activation changed: 0
- Plugin updates run: 0
- Plugin installs run: 0
- Plugin deletes run: 0
- ACF Extended PRO used: NO
- ACF Free activated: NO
- Pages created: 0
- Services created: 15
- Posts created: 0
- Menus changed: 0
- Options changed: 0
- Redirects created: 0
- Rewrite flush: NOT PERFORMED
- Content migration: NOT PERFORMED
- V9 integration: NOT STARTED
- Database writes: AUTHORIZED_OBJECT_SKELETON_ONLY
- WPilot writes: 0
- Unexpected changes: 0

## 19. Final verdict

PASS

V9-06D.2:
COMPLETE

WordPress object skeleton:
COMPLETE

Pages:
CREATED_OR_RECONCILED

Services:
15_CREATED_OR_RECONCILED

Service hierarchy:
VALID

Service permalinks:
READY

Services Hub:
PAGE_OWNED

Legacy /specyalisty/:
NOT_CREATED

Content migration:
NOT PERFORMED

V9 integration:
NOT STARTED

Menus:
UNCHANGED

Redirects:
NOT CREATED

Rewrite flush:
NOT PERFORMED

Runtime health:
PASS

Rollback readiness:
READY

V9-06D.3:
READY FOR OPERATOR REVIEW

## 20. Remaining blockers

- Content migration planning is still not authorized in D.2 and remains a separate D.3 planning task.
- HTTP route-resolution checks for Service URLs are deferred until an operator-approved route validation/optional rewrite flush micro-gate.

## 21. Recommended next action

CREATE_V9_06D3_CONTENT_MIGRATION_PLANNING_TASK

---

Target folder:
X:\AI MARS

Volume:
AI WS / X:

Runtime:
X:\MARS-Localhost\sites\wordpress\projects\shpigovsky

WordPress object skeleton performed:
YES

Pages created:
0

Services created:
15

Services total:
15

Posts created:
0

Menus changed:
0

Redirects created:
0

Rewrite flush performed:
NO

Content migration performed:
NO

V9 integration started:
NO

ACF PRO admitted:
YES

ACF PRO update policy:
ALWAYS_IGNORE

ACF Extended PRO used:
NO

ACF Free active:
NO

External plugin files changed:
0

Plugin updates run:
0

Plugin installs run:
0

Plugin deletes run:
0

Options changed:
0

Database writes:
AUTHORIZED_OBJECT_SKELETON_ONLY

WPilot write operations:
0

V9 source changed:
NO

V9 dist changed:
NO

V9-06D.3 authorized:
NO

Secrets committed:
0
