# REPORT — FP-0002 V9-06D.5 VISUAL ROUTE QA

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: e377ff4a72b3341e9b2ff6bc2dc532b84c79bdc2
- Remote HEAD: e377ff4a72b3341e9b2ff6bc2dc532b84c79bdc2
- Ahead: 0
- Behind: 0
- Foreign WIP: YES (unstaged; excluded)
- Pre-existing staged files: none
- Result: PASS

## 2. Authorization and scope

- Operator authorization: YES (read-only visual route QA + evidence/docs only)
- Runtime writes: 0
- DB writes: 0
- Rewrite flush: NOT_PERFORMED
- Content/ACF writes: 0
- Menu changes: 0
- Redirects: 0
- Source changes: 0 (theme/plugin/V9)
- Object create/delete: 0
- Screenshot/evidence writes: YES (approved Git evidence paths only)
- Result: PASS

## 3. Runtime identity

- Runtime: X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\
- Domain: http://shpigovsky.test/
- Theme: shpigovsky (0.2.0-skeleton)
- Shpigovsky Core: active
- Core mode: content_model
- Service CPT: registered (hierarchical, rewrite slug `uslugi`)
- Pages total: publish **22** / any-status **23** (prior publish=23; Page ID 3 privacy-policy is draft)
- Services total: **15**
- Posts total: publish **0** (prior publish=1; auto-draft only remains)
- Menus: 3 (Primary, Footer, Legal)
- ACF PRO: active
- ACF groups: 13
- Options Page: fp02-site-settings registered
- WPilot write_enabled: false
- Frontend: HTTP 200
- wp-admin: HTTP 302
- Result: PASS

## 4. Route HTTP / resolver validation

| Route | URL | Expected object | HTTP | Resolved object | Permalink match | Result |
|---|---|---|---:|---|---:|---|
| Home | `/` | Page 4 | 200 | page/4 | YES | PASS |
| Services Hub | `/uslugi/` | Page 5 | 200 | page/5 | YES | PASS |
| Зависимости | `/uslugi/zavisimosti/` | Service 73 | 200 | service/73 | YES | PASS |
| Алкоголь | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | Service 74 | 200 | service/74 | YES | PASS |
| Психическое здоровье | `/uslugi/psihicheskoe-zdorovie/` | Service 77 | 200 | service/77 | YES | PASS |
| РПП | `/uslugi/rasstroystva-pischevogo-povedeniya/` | Service 84 | 200 | service/84 | YES | PASS |
| Contacts | `/kontakty/` | Page 20 | 200 | page/20 | YES | PASS |

Optional: `/blog/` HTTP 200 (Page ID 19 / posts page placeholder state).

## 5. Template/render readiness

| Route | Template/family | Header | Footer | Main content | Hero/intro | Fatal errors | Result |
|---|---|---:|---:|---:|---:|---:|---|
| Home | front-page.php + home/* | YES | YES | YES | comment markers only | NO | PASS |
| Services Hub | page-templates/services-hub.php | YES | YES | YES | H1 «Услуги» | NO | PASS |
| Зависимости | single-service.php → leaf-stack | YES | YES | YES | inert comments | NO | PASS |
| Алкоголь | single-service.php → leaf-stack | YES | YES | YES | inert comments | NO | PASS |
| Психическое здоровье | single-service.php → leaf-stack | YES | YES | YES | inert comments | NO | PASS |
| РПП | single-service.php → leaf-stack | YES | YES | YES | inert comments | NO | PASS |
| Contacts | page-templates/contacts.php | YES | YES | YES | H1 «Контакты» | NO | PASS |

## 6. Desktop visual smoke

| Route | Screenshot | Above fold visible | Layout non-blank | Critical issue | Result |
|---|---|---:|---:|---|---|
| Home | screenshots/desktop-home.png | YES | YES | none | PASS |
| Services Hub | screenshots/desktop-services-hub.png | YES | YES | none | PASS |
| Зависимости | screenshots/desktop-service-zavisimosti.png | YES | YES | none (skeleton; no service H1) | PASS |
| Алкоголь | screenshots/desktop-service-alkogol.png | YES | YES | none (skeleton; no service H1) | PASS |
| Психическое здоровье | screenshots/desktop-service-psych.png | YES | YES | none (skeleton; no service H1) | PASS |
| РПП | screenshots/desktop-service-rpp.png | YES | YES | none (skeleton; no service H1) | PASS |
| Contacts | screenshots/desktop-contacts.png | YES | YES | none | PASS |

## 7. Mobile visual smoke

| Route | Screenshot | Above fold visible | No obvious horizontal overflow | Critical issue | Result |
|---|---|---:|---:|---|---|
| Home | screenshots/mobile-home.png | YES | YES (unstyled list) | none | PASS |
| Services Hub | screenshots/mobile-services-hub.png | YES | YES | none | PASS |
| Зависимости | screenshots/mobile-service-zavisimosti.png | YES | YES | none | PASS |
| Алкоголь | screenshots/mobile-service-alkogol.png | YES | YES | none | PASS |
| Психическое здоровье | screenshots/mobile-service-psych.png | YES | YES | none | PASS |
| РПП | screenshots/mobile-service-rpp.png | YES | YES | none | PASS |
| Contacts | screenshots/mobile-contacts.png | YES | YES | none | PASS |

## 8. Service 74 regression check

- URL: http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/
- HTTP: 200
- Resolved object: service/74
- Query var: `zavisimosti/lechenie-alkogolnoy-zavisimosti`
- Template: single-service.php → leaf-stack (default skeleton)
- Result: PASS

## 9. Page 6 / Service 73 path note

- Shared path: `/uslugi/zavisimosti/`
- Page ID 6 state: publish, generated path `/uslugi/zavisimosti/`
- Service ID 73 state: publish, generated path `/uslugi/zavisimosti/`
- Current resolver: Service 73 (HTTP 200)
- D.5 blocker: NO
- Later action: PATH_OWNERSHIP_CLEANUP_AFTER_TEMPLATE_INTEGRATION_PLANNING
- Result: DOCUMENTED_SECONDARY_DEBT

## 10. Source/template readiness

- front-page: skeleton orchestration; home parts inert
- services-hub: skeleton with H1 + placeholder notice
- single-service: skeleton; default leaf-stack; inert partials
- contacts: skeleton with H1 + contacts partials
- header/footer: present (unstyled lists)
- template-parts: present as V9-06B boundaries
- V9 integration status: NOT_STARTED
- Result: READY_BASELINE_SKELETON

## 11. Route readiness classification

| Route | Classification | Reason | Next need |
|---|---|---|---|
| Home | READY_FOR_V9_TEMPLATE_INTEGRATION | Non-blank skeleton baseline | V9 home integration |
| Services Hub | READY_FOR_V9_TEMPLATE_INTEGRATION | Non-blank skeleton + H1 | V9 services-hub integration |
| Зависимости | READY_FOR_V9_TEMPLATE_INTEGRATION | Service 73 resolves | V9 service template |
| Алкоголь | READY_FOR_V9_TEMPLATE_INTEGRATION | Service 74 resolves | V9 service template |
| Психическое здоровье | READY_FOR_V9_TEMPLATE_INTEGRATION | Service 77 resolves | V9 service template |
| РПП | READY_FOR_V9_TEMPLATE_INTEGRATION | Service 84 resolves | V9 service template |
| Contacts | READY_FOR_V9_TEMPLATE_INTEGRATION | Non-blank skeleton + H1 | V9 contacts integration |

Secondary for seeded routes: READY_FOR_CONTENT_MIGRATION_LATER.

## 12. Validation suites

| Suite | Passed | Failed | Skipped | Result |
|---|---:|---:|---:|---|
| preflight | 1 | 0 | 0 | PASS |
| runtime-identity | 1 | 0 | 0 | PASS |
| route-http-resolution | 7 | 0 | 0 | PASS |
| route-template-render-readiness | 7 | 0 | 0 | PASS |
| route-visual-smoke-desktop | 7 | 0 | 0 | PASS |
| route-visual-smoke-mobile | 7 | 0 | 0 | PASS |
| service-74-regression-check | 1 | 0 | 0 | PASS |
| page6-service73-path-note | 1 | 0 | 0 | PASS |
| source-template-readiness | 1 | 0 | 0 | PASS |
| screenshot-manifest | 14 | 0 | 0 | PASS |
| no-runtime-mutation-validation | 1 | 0 | 0 | PASS |
| d6-readiness-validation | 1 | 0 | 0 | PASS |

- Total failures: 0
- Runtime mutations: 0
- Result: PARTIAL PASS (visual/template gaps documented)

## 13. Documentation changes

| File | Action | Reason |
|---|---|---|
| WORDPRESS/reports/FP-0002-V9-06D5-VISUAL-ROUTE-QA-REPORT-v1.md | CREATE | D.5 report |
| WORDPRESS/architecture/FP-0002-V9-06D5-VISUAL-ROUTE-QA-RESULT-v1.md | CREATE | Result summary |
| WORDPRESS/architecture/FP-0002-V9-06D5-TEMPLATE-READINESS-MATRIX-v1.md | CREATE | Template matrix |
| WORDPRESS/architecture/FP-0002-V9-06D5-NEXT-PHASE-RECOMMENDATION-v1.md | CREATE | D.6 recommendation |
| WORDPRESS/architecture/FP-0002-PAGE6-SERVICE73-PATH-OWNERSHIP-NOTE-v1.md | CREATE | Secondary debt note |
| WORDPRESS/validation/v9-06d5-visual-route-qa/** | CREATE | Evidence suite + screenshots |
| WORDPRESS/README.md | UPDATE | Status |
| WORDPRESS/SOURCE-AUTHORITY.md | UPDATE | D.5 note |
| FP-0002-SHPIGOVSKY/PROJECT-STATUS.md | UPDATE | Status entry |
| Forge FP-0002 README | UPDATE | Stage |
| Forge OPERATIONAL-INDEX | UPDATE | Client pilot line |
| Website Factory OPERATIONAL-INDEX | UPDATE | FP-0002 line |
| V9 operational status | UPDATE | D.5 complete |
| V9 intake gate/status | UPDATE | D.5 gate |

## 14. Git checkpoint

See operator commit section in task closeout (documentation/evidence only).

## 15. No-scope-drift audit

- Runtime files changed: NO
- Database writes: 0
- WordPress content writes: 0
- ACF/meta writes: 0
- Rewrite flush: NOT_PERFORMED
- Menus changed: 0
- Redirects created: 0
- Object create/delete: 0
- V9 source changed: NO
- V9 dist changed: NO
- Theme/plugin source changed: NO
- Plugin updates/installs/deletes: 0
- ACF Extended PRO used: NO (present/active but not used by this task)
- Browser cache committed: NO
- Unexpected changes: NO

## 16. Final verdict

**PARTIAL PASS**

V9-06D.5 visual route QA: **COMPLETE**

Required routes: **ALL_200**

Service ID 74: **PASS**

Template/render readiness: **READY_BASELINE**

Desktop smoke: **PASS**

Mobile smoke: **PASS**

Runtime mutations: **0**

DB writes: **0**

Rewrite flush: **NOT_PERFORMED**

Content/ACF writes: **0**

Recommended next phase: **CREATE_V9_06D6_TEMPLATE_INTEGRATION_PLANNING_TASK**

V9-06D.6: **READY FOR OPERATOR REVIEW**

## 17. Remaining blockers

None blocking D.6 planning. Secondary debt: Page 6 / Service 73 path ownership (cleanup later). Visual gaps are expected skeleton state, not blockers.

## 18. Recommended next action

**CREATE_V9_06D6_TEMPLATE_INTEGRATION_PLANNING_TASK**
