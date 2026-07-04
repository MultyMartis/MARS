# REPORT — FP-0002 ROUTE-OWNERSHIP-INVESTIGATION

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: d123f85b9ce8aad90ff4c07895b67cfb124bda3d
- Remote HEAD: d123f85b9ce8aad90ff4c07895b67cfb124bda3d
- Ahead: 0
- Behind: 0
- Foreign WIP: present (unstaged; excluded from this task)
- Pre-existing staged files: 0
- Result: PASS

## 2. Authorization and scope

- Operator authorization: read-only diagnostics + documentation/evidence writes only
- Runtime writes: 0
- DB writes: 0
- Rewrite flush: NOT_PERFORMED
- Content/ACF writes: 0
- Menu changes: 0
- Redirects: 0
- Source changes: 0 (runtime and Git theme/plugin source not modified)
- Object create/delete: 0
- Result: PASS

## 3. Runtime identity

- Runtime: X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\
- Domain: http://shpigovsky.test/
- Theme: shpigovsky
- Shpigovsky Core: active
- Core mode: content_model
- Service CPT: registered (hierarchical, has_archive=false, rewrite slug=uslugi)
- Pages total: 23
- Services total: 15
- Posts total: 1 (matches prior reports; no post seed in D.4)
- Menus: 3
- ACF PRO: active
- ACF groups: 13
- Options Page: registered (fp02-site-settings)
- WPilot write_enabled: false
- Frontend: HTTP 200
- wp-admin: HTTP 302
- Result: PASS

## 4. Object route inventory

| Object | ID | Type | Status | Parent | Generated path | HTTP | Notes |
|---|---:|---|---|---|---|---:|---|
| Services Hub | 5 | page | publish | 0 | /uslugi/ | 200 | template services-hub.php |
| Historical Зависимости | 6 | page | publish | 5 | /uslugi/zavisimosti/ | 200 | legacy source page; collides with Service 73 |
| Зависимости | 73 | service | publish | 0 | /uslugi/zavisimosti/ | 200 | depth-level service |
| Лечение алкогольной зависимости | 74 | service | publish | 73 | /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | **404** | permalink MATCH; route FAIL |
| Психическое здоровье | 77 | service | publish | 0 | /uslugi/psihicheskoe-zdorovie/ | 200 | control |
| Расстройства пищевого поведения | 84 | service | publish | 0 | /uslugi/rasstroystva-pischevogo-povedeniya/ | 200 | control |

## 5. Rewrite matching diagnostics

- Rewrite rules count: 108
- Rewrite rules hash: bf3926c71b7b134708fa052f782c911dcc931dd61b1964a49b034d5b546c3a12
- Relevant rules found: 13 (uslugi/service patterns)
- Rule expected for Service 74: `^uslugi/([^/]+)/([^/]+)/?$`
- Actual query vars for Service 74: `post_type=service`, `service=lechenie-alkogolnoy-zavisimosti` (leaf only)
- Control URL comparison: depth-1 controls map `service={slug}` and resolve; depth-2 maps leaf only and fails hierarchical lookup
- Result: PASS (diagnosed)

## 6. WP request diagnostics

| URL | HTTP | is_404 | queried_object_id | post_type | matched_rule | matched_query | Result |
|---|---:|---:|---:|---|---|---|---|
| /uslugi/zavisimosti/ | 200 | no (HTTP) | 73 via get_page_by_path(service) | service (winning rule) | ^uslugi/([^/]+)/?$ | service=$matches[1] → zavisimosti | Service 73 wins; Page 6 also exists |
| /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | 404 | yes | null (leaf); 74 (full path lookup) | — | ^uslugi/([^/]+)/([^/]+)/?$ | service=$matches[2] → leaf only | FAIL |
| /uslugi/psihicheskoe-zdorovie/ | 200 | no | 77 | service | ^uslugi/([^/]+)/?$ | service=psihicheskoe-zdorovie | PASS control |
| /uslugi/rasstroystva-pischevogo-povedeniya/ | 200 | no | 84 | service | ^uslugi/([^/]+)/?$ | service=rasstroystva-pischevogo-povedeniya | PASS control |

## 7. Source code diagnostics

- Service CPT registration: `Service.php` — hierarchical, rewrite slug `uslugi`, has_archive false
- Service permalink filter: `post_type_link` builds full ancestor path — correct for Service 74
- Rewrite rule generation: custom top rules; depth-2 uses `service=$matches[2]` (leaf only) — **incorrect for hierarchical CPT lookup**
- Request resolver: none
- Template loader: `single-service.php` exists; not reached for Service 74
- Canonical redirect: filter present; does not apply because query never becomes singular service
- Depth-2 support: pattern present; query mapping wrong
- Result: PASS (diagnosed)

## 8. Database read-only diagnostics

- Object rows inspected: IDs 5, 6, 73, 74, 77, 84
- Duplicate slugs/paths: `zavisimosti` on Page 6 and Service 73; similar Page/Service pairs exist for other subdivisions (e.g. Page 7 / Service 77) but depth-1 still resolves
- Parent chains: 74 → 73 → 0 (valid)
- Page/Service collision: Page 6 / Service 73 on `/uslugi/zavisimosti/` CONFIRMED
- Service 74 object state: publish, parent 73, slug intact
- Result: PASS

## 9. Path collision analysis

- Page ID 6 path: /uslugi/zavisimosti/
- Service ID 73 path: /uslugi/zavisimosti/
- Current resolver: custom top depth-1 service rule → Service 73
- Effect on Service ID 74: not direct; parent resolves; leaf-only depth-2 mapping fails independently
- Blocking for D.5: Service 74 404 is the active blocker
- Result: CONFIRMED

## 10. Root cause classification

- Primary cause: **B. POST_TYPE_LINK_REWRITE_MISMATCH**
- Secondary causes: A. PAGE_SERVICE_PATH_COLLISION
- Evidence: leaf-only rewrite query var; full-path lookup returns 74; leaf lookup null; HTTP 404; permalink correct
- Why generated permalink is correct but HTTP is 404: `post_type_link` emits full path; rewrite injects leaf only; hierarchical CPT lookup requires parent/child path
- Why controls work: root services where leaf equals full hierarchy path
- Repair layer: rewrite rules (source `ServicePermalinks::register_rewrite_rules`) + authorized soft flush later
- Result: IDENTIFIED

## 11. Candidate repair options

| Option | Layer | Runtime writes later | Source changes later | Risk | Recommended |
|---|---|---:|---:|---|---:|
| Source resolver repair | request resolver | 0–1 flush | Yes | Medium | No |
| Rewrite rule repair | rewrite rules | rewrite_rules only | Yes | Low | **Yes** |
| Path ownership cleanup | ownership / migration | Page writes | No | Medium | Later |
| Change service parent/path model | object model | Object writes | Maybe | High | Rejected |
| Redirect workaround | redirect | Redirect writes | No | High drift | Rejected |

## 12. Recommended repair

- Recommended option: Rewrite rule repair (depth-2 `service=$matches[1]/$matches[2]`)
- Exact next micro-task: CREATE_REWRITE_RULE_REPAIR_MICRO_TASK
- Expected changes: source `ServicePermalinks.php` + contract doc; runtime soft flush only
- Required checkpoint: DB checkpoint before flush
- Required validation: Service 74 HTTP 200; hub/controls unchanged; no content drift
- Rollback: restore prior plugin source + rewrite_rules snapshot
- Result: DOCUMENTED (not applied)

## 13. D.5 readiness

**D5_BLOCKED_ROUTE_REPAIR_REQUIRED**

Service 74 remains HTTP 404 on an in-scope visual QA URL. Exclusion would weaken D.5. Repair must land first.

## 14. Validation suites

| Suite | Passed | Failed | Skipped | Result |
|---|---:|---:|---:|---|
| preflight | 1 | 0 | 0 | PASS |
| runtime-identity | 1 | 0 | 0 | PASS |
| object-route-inventory | 1 | 0 | 0 | PASS |
| rewrite-matching-diagnostics | 1 | 0 | 0 | PASS |
| wp-request-diagnostics | 1 | 0 | 0 | PASS |
| source-code-diagnostics | 1 | 0 | 0 | PASS |
| database-readonly-diagnostics | 1 | 0 | 0 | PASS |
| path-collision-analysis | 1 | 0 | 0 | CONFIRMED |
| root-cause-classification | 1 | 0 | 0 | IDENTIFIED |
| repair-options-validation | 1 | 0 | 0 | PASS |
| d5-readiness-validation | 1 | 0 | 0 | BLOCKED |
| no-runtime-mutation-validation | 1 | 0 | 0 | PASS |

- Total failures: 0
- Runtime mutations: 0
- Result: PASS

## 15. Documentation changes

| File | Action | Reason |
|---|---|---|
| WORDPRESS/reports/FP-0002-ROUTE-OWNERSHIP-INVESTIGATION-REPORT-v1.md | create | Investigation report |
| WORDPRESS/architecture/FP-0002-ROUTE-OWNERSHIP-ROOT-CAUSE-v1.md | create | Root cause |
| WORDPRESS/architecture/FP-0002-ROUTE-OWNERSHIP-REPAIR-OPTIONS-v1.md | create | Repair options |
| WORDPRESS/architecture/FP-0002-ROUTE-OWNERSHIP-RECOMMENDED-REPAIR-v1.md | create | Recommended repair |
| WORDPRESS/architecture/FP-0002-V9-06D5-READINESS-AFTER-ROUTE-INVESTIGATION-v1.md | create | D.5 readiness |
| WORDPRESS/validation/route-ownership-investigation/* | create | Evidence suites |
| WORDPRESS/README.md | update | Status |
| WORDPRESS/SOURCE-AUTHORITY.md | update | Status |
| Forge FP-0002 README/status | update | Status |
| Forge / Website Factory OPERATIONAL-INDEX | update | Status |
| V9 operational status / intake | update | Status |

## 16. Git checkpoint

- Exact staged files: (filled after commit)
- Runtime files staged: 0
- Runtime snapshots staged: 0
- Database dumps staged: 0
- External plugin files staged: 0
- Plugin ZIPs staged: 0
- Secrets staged: 0
- License keys staged: 0
- Foreign files staged: 0
- Commit: (filled after commit)
- Commit hash: (filled after commit)
- Push: (filled after push)
- Local HEAD: (filled after push)
- Remote HEAD: (filled after push)
- Result: (filled after push)

## 17. No-scope-drift audit

- Files changed: documentation/evidence only under authorized WORDPRESS/ and status index paths
- Runtime files changed: 0
- Database writes: 0
- WordPress content writes: 0
- ACF/meta writes: 0
- Rewrite flush: NOT_PERFORMED
- Menus changed: 0
- Redirects created: 0
- Object create/delete: 0
- V9 source changed: 0
- V9 dist changed: 0
- Theme/plugin source changed: 0
- Plugin updates run: 0
- Plugin installs run: 0
- Plugin deletes run: 0
- ACF Extended PRO used: 0
- Unexpected changes: 0

## 18. Final verdict

**PASS**

Route ownership investigation: COMPLETE

Service ID 74 root cause: IDENTIFIED

Service ID 74 route: STILL_404

Page ID 6 / Service ID 73 collision: CONFIRMED

Runtime mutations: 0

DB writes: 0

Rewrite flush: NOT_PERFORMED

Content/ACF writes: 0

Recommended repair: Rewrite rule repair (depth-2 full-path service query var)

V9-06D.5: BLOCKED

## 19. Remaining blockers

1. Service ID 74 HTTP 404 until rewrite rule repair is authorized, delivered, and soft-flushed.
2. Page ID 6 / Service ID 73 shared path ownership remains secondary debt (not D.5 primary blocker after repair of 74).

## 20. Recommended next action

**CREATE_REWRITE_RULE_REPAIR_MICRO_TASK**
