# REPORT — FP-0002 V9-06D.3 CONTENT MIGRATION PLANNING

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: 21bb20b956b927788d7a17318062b9db08db5cb3
- Remote HEAD: 21bb20b956b927788d7a17318062b9db08db5cb3
- Ahead: 0
- Behind: 0
- Foreign WIP: present, unstaged/untracked, excluded from scope
- Pre-existing staged files: 0
- Result: PASS

## 2. Authorization and scope

- Operator authorization: V9-06D.3 planning/audit only
- Runtime content writes: NOT AUTHORIZED / 0
- Database writes: NOT AUTHORIZED / 0
- V9 integration: NOT AUTHORIZED / NOT STARTED
- Menu changes: NOT AUTHORIZED / 0
- Redirects: NOT AUTHORIZED / 0
- Rewrite flush: NOT AUTHORIZED / NOT PERFORMED
- Planning docs: AUTHORIZED / CREATED
- Result: PASS

## 3. Current runtime inventory

- Pages: 23
- Services: 15
- Posts: 0
- Menus: 3 (Footer, Legal, Primary)
- Front page: 4
- Posts page: 19
- Service CPT: registered=True
- ACF groups: 13
- Options Page: registered ([{'slug': 'fp02-site-settings', 'registered': True, 'values_dumped': False}])
- WPilot write_enabled: False
- Result: PASS

## 4. V9 static inventory

- V9 routes found: 31
- V9 full pages: 9
- V9 placeholders: 18
- V9 legal/demo: 4
- V9 source inspected: YES
- V9 dist inspected: YES (no built HTML present)
- Result: PASS

## 5. Route-to-object migration matrix

| Object type | Count | Mapped | Ambiguous | Deferred | Result |
|---|---:|---:|---:|---:|---|
| PAGE | 10 | 10 | 0 | 0 | PASS |
| SERVICE | 15 | 15 | 0 | 0 | PASS |
| POST | 1 | 1 | 0 | 0 | PASS |
| POSTS_PAGE | 1 | 1 | 0 | 0 | PASS |
| LEGAL_PAGE | 4 | 4 | 0 | 4 | PASS |
| LEGACY_DEFERRED | 1 | 1 | 0 | 1 | PASS |

- Total routes: 31
- Mapped routes: 31
- Unmapped routes: 0
- Result: PASS

## 6. Page migration plan

- Pages kept as Pages: 15
- Existing Pages reused: all page-owned routes
- Pages needing first-wave ACF fill: Home, Services Hub, Contacts
- Legal/demo blockers: 4 legal pages
- Legacy `/specyalisty/`: Page ID 10 LEGACY_DEFERRED
- Page ambiguity: 0
- Result: PASS

## 7. Service migration plan

- Services total: 15
- Services mapped: 15
- Parent services: 3
- Child services: 12
- Alcohol special: SVC-ALKOGOL ID 74
- Placeholder services: 11
- First-wave Services: SVC-ZAVISIMOSTI, SVC-ALKOGOL, SVC-PSYCH, SVC-RPP
- Deferred Services: 0 (placeholders are wave-2 minimal, not deferred)
- Result: PASS

## 8. ACF field fill strategy

| Field group family | Groups | Covered | Wave 1 | Deferred | Result |
|---|---:|---:|---:|---:|---|
| Service | 4 | 4 | 2 groups partial | FAQ/relationships full later | PASS |
| Page | 6 | 6 | Home/Hub/Contacts | Institutional/Reviews/Legal | PASS |
| Blog Post | 1 | 1 | 0 | WAVE_4 | PASS |
| Site Options | 2 | 2 | 0 | later options micro-gate | PASS |

- Total ACF groups: 13
- Flexible Content: NOT_USED
- Unbounded repeaters: NOT_USED
- ACF Extended PRO usage: NOT_USED
- Options values planned for immediate write: NO
- Result: PASS

## 9. V9 section integration strategy

- Section types mapped: 14
- Template targets mapped: YES
- ACF data sources mapped: YES
- Static fallback strategy: Templates render empty/minimal states when ACF empty; no V9 HTML copied into the...
- First-wave integration priority: hero, services hub, alcohol signs, contacts, breadcrumbs, placeholder
- Runtime integration performed: NO
- Result: PASS

## 10. Minimal visual content seed plan

- Proposed next phase: V9-06D.4 MINIMAL CONTENT SEED FOR VISUAL ROUTE QA
- Objects in first writable wave: Pages 4/5/20 + Services 73/74/77/84
- Fields in first writable wave: minimal hero/intro/contacts fields only
- URLs for visual QA: 7 primary URLs listed in seed plan
- Production content: NOT in D.4 scope
- Rollback: DB dump required before writes
- Result: READY FOR OPERATOR REVIEW

## 11. Legacy / redirect / rewrite plan

- `/specyalisty/`: LEGACY_DEFERRED Page ID 10
- Canonical specialist route: `/uslugi/zavisimosti/specialistam/`
- Redirects immediate: NO
- Redirects deferred: YES
- Rewrite flush immediate: NO
- Rewrite flush deferred: YES
- Result: PASS

## 12. Future validation plan

- Object validation: DEFINED
- ACF validation: DEFINED
- URL validation: DEFINED
- Visual QA: DEFINED
- Rollback validation: DEFINED
- Result: PASS

## 13. Future rollback plan

- DB checkpoint: REQUIRED before D.4
- Object rollback: via DB restore
- ACF rollback: via DB restore
- Options rollback: via DB restore if written
- Media rollback: attachment ID list if uploads used
- Rewrite rollback: evaluate only if flush authorized later
- Result: PASS

## 14. Planning validation suites

| Suite | Passed | Failed | Skipped | Result |
|---|---:|---:|---:|---|
| preflight | 1 | 0 | 0 | PASS |
| runtime_readonly_inventory | 1 | 0 | 0 | PASS |
| v9_static_content_inventory | 1 | 0 | 0 | PASS |
| route_object_matrix | 1 | 0 | 0 | PASS |
| page_migration_plan | 1 | 0 | 0 | PASS |
| service_migration_plan | 1 | 0 | 0 | PASS |
| acf_field_fill_strategy | 1 | 0 | 0 | PASS |
| v9_section_integration_strategy | 1 | 0 | 0 | PASS |
| minimal_visual_content_seed_plan | 1 | 0 | 0 | PASS |
| legacy_redirect_rewrite_plan | 1 | 0 | 0 | PASS |
| future_validation_plan | 1 | 0 | 0 | PASS |
| future_rollback_plan | 1 | 0 | 0 | PASS |
| no_runtime_mutation | 1 | 0 | 0 | PASS |

- Total failures: 0
- Result: PASS

## 15. Documentation changes

| File | Action | Reason |
|---|---|---|
| WORDPRESS/reports/FP-0002-V9-06D3-CONTENT-MIGRATION-PLANNING-REPORT-v1.md | CREATE | Phase report |
| WORDPRESS/architecture/FP-0002-V9-06D3-* | CREATE | Planning matrices and plans |
| WORDPRESS/validation/v9-06d3-content-migration-planning/* | CREATE | Evidence |
| WORDPRESS/README.md | UPDATE | Status |
| WORDPRESS/SOURCE-AUTHORITY.md | UPDATE | Status |
| Forge FP-0002 README/status | UPDATE | Status |
| Forge OPERATIONAL-INDEX | UPDATE | Status |
| Website Factory OPERATIONAL-INDEX | UPDATE | Status |
| V9 operational status + intake gate | UPDATE | Status |

## 16. Git checkpoint

- Exact staged files: (filled at commit time)
- Runtime files staged: 0
- Runtime snapshots staged: 0
- Database dumps staged: 0
- External plugin files staged: 0
- Plugin ZIPs staged: 0
- Secrets staged: 0
- License keys staged: 0
- Foreign files staged: 0
- Commit: 0d0c7930f05092e60c50495338a1a63a4da960d9
- Commit hash: 0d0c7930f05092e60c50495338a1a63a4da960d9
- Report update commit: 21bb20b956b927788d7a17318062b9db08db5cb3
- Push: YES
- Local HEAD: 21bb20b956b927788d7a17318062b9db08db5cb3
- Remote HEAD: 21bb20b956b927788d7a17318062b9db08db5cb3
- Result: PASS

## 17. No-scope-drift audit

- Runtime files changed: 0
- Database writes: 0
- WordPress object writes: 0
- WPilot writes: 0
- V9 source changed: NO
- V9 dist changed: NO
- Theme/plugin source changed: NO
- Menus changed: 0
- Redirects created: 0
- Rewrite flush: NO
- Options changed: 0
- Plugin updates run: 0
- Plugin installs run: 0
- Plugin deletes run: 0
- ACF Extended PRO used: NO
- ACF Free activated: NO
- Unexpected changes: none in authorized scope

## 18. Final verdict

PASS

V9-06D.3: COMPLETE

Content migration planning: COMPLETE

Route mapping: 31_MAPPED

Page migration plan: COMPLETE

Service migration plan: 15_MAPPED

ACF fill strategy: COMPLETE

V9 section strategy: COMPLETE

Minimal visual content seed plan: READY

Legacy/redirect/rewrite plan: READY

Runtime writes: 0

Database writes: 0

WordPress object writes: 0

V9 integration: NOT STARTED

V9-06D.4: READY FOR OPERATOR REVIEW

## 19. Remaining blockers

- Operator authorization required before V9-06D.4 minimal content seed writes
- Legal DEMO tokens block production legal migration (WAVE_4)
- Rewrite flush still deferred pending HTTP proof in D.4 QA
- Options Page values not seeded (global CTA/contacts may be empty until authorized)

## 20. Recommended next action

CREATE_V9_06D4_MINIMAL_CONTENT_SEED_FOR_VISUAL_ROUTE_QA
