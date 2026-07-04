# REPORT — FP-0002 V9-06D.6 TEMPLATE INTEGRATION PLANNING RERUN

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: 2edcdf3c1021634dbe134db26c722c6e55d3f583
- Remote HEAD: 2edcdf3c1021634dbe134db26c722c6e55d3f583
- Ahead: 0 (at commit; was 3 at task start)
- Behind: 0
- Foreign WIP: YES (unstaged; excluded)
- Pre-existing staged files: none
- Result: PARTIAL_PASS_DEVIATION_NOTED (required HEAD 10eaffc2 is ancestor; at start local ahead 3 ORCA commits; before commit remote advanced and synced at 2edcdf3c)

## 2. Crash recovery carry-forward

- Crash recovery classification: D6_RECOVERABLE_RESUME_READY
- Cleanup required: NO
- Old Resume used: NO
- Old generator reused: NO
- Recovery evidence preserved: YES
- Result: PASS

## 3. Authorization and scope

- Operator authorization: YES (planning/docs only)
- Runtime writes: 0
- DB writes: 0
- Source changes: 0
- V9 src/dist changes: 0
- Content/ACF writes: 0
- Rewrite flush: NO
- Menus: 0
- Redirects: 0
- Object changes: 0
- Documentation/evidence writes: YES
- Result: PASS

## 4. Authority review

- D.6 crash recovery: PASS / D6_RECOVERABLE_RESUME_READY
- D.5 report: PARTIAL PASS
- D.4 report: PARTIAL PASS
- Rewrite repair report: PASS
- V9 static source: FOUND
- WordPress theme source: FOUND
- ACF source: FOUND (13 groups)
- Result: PASS

## 5. V9 static inventory

- Routes inspected: first-wave 7 + shared chrome
- Full pages found: home, uslugi, service templates, kontakty, plus blog/o-centre/otzyvy
- Placeholder pages found: psych/RPP parents and related leaves
- Shared components: header, footer, modal, breadcrumbs, CTA band
- CSS/SCSS assets: style.scss + FA vendor
- JS assets: main.js + Swiper/Fancybox/Inputmask
- Image/media references: content/services, rehabilitation-program, svg icons
- Build assumptions: gulp-file-include; root-relative /assets in dist
- Result: COMPLETE

## 6. WordPress source inventory

- Theme templates: front-page, page templates, single-service, home, page, single, index, search, 404
- Page templates: services-hub, contacts, institutional, reviews, legal
- Service templates: subdivision/leaf/alcohol stacks (inert)
- Header/footer: skeleton unstyled
- Template-parts: present as inert markers
- Assets enqueue: foundation.css only
- Plugin modules: content_model active; forms/migrations disabled
- ACF groups: 13
- Result: COMPLETE

## 7. Static-to-WordPress mapping

| Route/template | V9 source | WP template | Data source | ACF groups | Current gap | Proposed wave | Result |
|---|---|---|---|---|---|---|---|
| home | `src/pages/index.html` | `front-page.php` | ACF + post_title | group_fp02_page_home | inert home partials; no V9 CSS/JS; many V9 sections lack ded… | D7-B | PLANNED |
| services_hub | `src/pages/uslugi.html` | `page-templates/services-hub.php` | ACF + post_title | group_fp02_page_services_hub | H1 + placeholder only; no category hub markup; service cards… | D7-C | PLANNED |
| service_parent_zavisimosti | `src/pages/usluga-podrazdel-v1.html` | `single-service.php → subdivision-stack.php` | ACF + post_title | group_fp02_service_layout_hero, group_fp02_service_structured_sections, group_fp02_service_faq | layout variant not ACF-wired (defaults leaf); inert partials… | D7-D | PLANNED |
| service_child_alcohol | `src/pages/usluga-konechnaya-v1.html` | `single-service.php → alcohol-stack.php` | ACF + post_title | group_fp02_service_layout_hero, group_fp02_service_structured_sections, group_fp02_service_faq | seeded layout/hero/intro/signs but inert partials; alcohol-s… | D7-D | PLANNED |
| service_parent_psych | `src/pages/uslugi/psihicheskoe-zdorovie.html` | `single-service.php → subdivision-stack.php` | ACF + post_title | group_fp02_service_layout_hero | V9 is placeholder; minimal seed only; use subdivision + plac… | D7-D | PLANNED |
| service_parent_rpp | `src/pages/uslugi/rasstroystva-pischevogo-povedeniya.html` | `single-service.php → subdivision-stack.php` | ACF + post_title | group_fp02_service_layout_hero | V9 is placeholder; minimal seed only… | D7-D | PLANNED |
| contacts | `src/pages/kontakty.html` | `page-templates/contacts.php` | ACF + post_title | group_fp02_page_contacts | H1 + inert/minimal contacts partials; options not seeded… | D7-E | PLANNED |
| global_header | `src/partials/layout/header.html` | `header.php → template-parts/layout/header.php` | ACF + post_title | menus/options | unstyled skeleton list nav… | D7-A | PLANNED |
| global_footer | `src/partials/layout/footer.html` | `footer.php → template-parts/layout/footer.php` | ACF + post_title | group_fp02_site_options_contacts, group_fp02_site_options_modal_cta | unstyled skeleton footer; modal inert; forms disabled… | D7-A | PLANNED |

## 8. Component / asset integration plan

- Header/nav: D7-A port from V9; menus for links; offcanvas safe_static
- Footer: D7-A port; options-driven contacts with omit fallbacks
- Buttons: preserve V9 classes; no new tokens
- Modal/CTA: markup in D7-A; submit deferred
- CSS strategy: package V9 compiled CSS into theme assets; enqueue in assets.php
- JS strategy: safe static now; vendors adapted; forms deferred
- Images/media: theme package for chrome/first-wave; media library later
- Fallbacks: omit empty ACF sections; never fatal
- Result: COMPLETE

## 9. ACF binding plan

| Route/template | Fields needed | Fields existing | Gaps | Fallback | Migration need |
|---|---|---|---|---|---|
| Home | hero/nav/cta/faq/gallery | group_fp02_page_home | many V9 sections unmapped | omit empty | PARTIAL |
| Services Hub | intro/query/faq | group_fp02_page_services_hub | category hubs partial | title+intro+CPT query | PARTIAL |
| Service parent | layout/hero/intro | layout+structured | loader not wired | title+hero_lead | YES for zavisimosti |
| Service child | layout/hero/intro/signs | seeded on 74 | approach/reviews shared | omit empty | PARTIAL |
| Contacts | address/phones/form intro | seeded | options empty | seeded fields only | OPTIONS later |
| Site options | phone/address/modal | groups exist | not seeded | omit chrome bits | YES for chrome |

## 10. Integration wave plan

| Wave | Scope | Allowed source files later | Runtime delivery later | DB checkpoint later | Validation gate | Result |
|---|---|---|---:|---:|---|---|
| D7-A | Port V9 header/footer/nav chrome and enqueue V9 CS… | theme partials/assets | True | False | php lint | PLANNED |
| D7-B | Wire front-page.php and home partials to ACF with … | theme partials/assets | True | False | php lint | PLANNED |
| D7-C | Implement services-hub template with category hubs… | theme partials/assets | True | False | php lint | PLANNED |
| D7-D | Wire service layout variant from ACF; implement su… | theme partials/assets | True | False | php lint | PLANNED |
| D7-E | Wire contacts template to ACF; form markup only… | theme partials/assets | True | False | php lint | PLANNED |
| D7-F | Deliver theme package to local runtime; screenshot… | theme partials/assets | True | True | dry-run delivery | PLANNED |

## 11. Runtime delivery / rollback plan

- Source implementation gate: per-wave PHP lint + static validation + manifest
- Runtime delivery gate: dry-run, ADDITIVE_ONLY, hash match
- DB checkpoint required when: options/content/ACF writes occur (not for pure theme file delivery)
- Rollback for source: git revert wave commit
- Rollback for runtime files: restore pre-delivery backup of owned paths
- Rollback for DB: restore dump only if DB written
- Validation: visual smoke; no pixel-perfect claim
- Result: COMPLETE

## 12. Risk / blocker register

| Risk | Severity | Blocks next wave | Mitigation |
|---|---|---:|---|
| Page ID 6 / Service ID 73 shared path ownership debt | MEDIUM | False | Documented secondary debt; cleanup after template integration |
| Skeleton chrome currently unstyled | HIGH | True | D7-A global shell/assets first |
| Inert service template partials | HIGH | False | D7-D wires partials to ACF |
| Content minimal seed only | MEDIUM | False | Fallbacks; later migration waves |
| ACF fields may not fully cover V9 visual content | MEDIUM | False | Gap register; optional ACF gap-repair task if blocking |
| Static assets need theme asset packaging | HIGH | True | D7-A packages from V9 dist without editing V9 |
| Forms/modal behavior deferred | MEDIUM | False | Markup only; ConsultationHandler stays disabled |
| Legal/demo content not production ready | LOW | False | Outside first wave |

## 13. Next implementation recommendation

**CREATE_V9_06D7_GLOBAL_SHELL_ASSET_INTEGRATION_SOURCE_TASK**

Why: unstyled chrome and missing V9 assets block meaningful route integration; shell/assets must land first.

## 14. Validation suites

| Suite | Passed | Failed | Skipped | Result |
|---|---:|---:|---:|---|
| preflight | 1 | 0 | 0 | PARTIAL_PASS_DEVIATION_NOTED |
| authority-review | 1 | 0 | 0 | PASS |
| v9-static-inventory | 1 | 0 | 0 | PASS |
| wp-theme-source-inventory | 1 | 0 | 0 | PASS |
| acf-field-source-inventory | 1 | 0 | 0 | PASS |
| static-to-wp-template-matrix | 1 | 0 | 0 | PASS |
| component-asset-plan | 1 | 0 | 0 | PASS |
| acf-binding-plan | 1 | 0 | 0 | PASS |
| integration-wave-plan | 1 | 0 | 0 | PASS |
| runtime-delivery-rollback-plan | 1 | 0 | 0 | PASS |
| risk-blocker-register | 1 | 0 | 0 | PASS |
| next-implementation-recommendation | 1 | 0 | 0 | PASS |
| no-runtime-mutation | 1 | 0 | 0 | PASS |
| crash-recovery-preserved | 1 | 0 | 0 | PASS |
| final-verdict | 1 | 0 | 0 | PASS |

- Total failures: 0
- Runtime/source mutations: 0
- Result: PASS

## 15. Documentation changes

See commit file list. Architecture matrices, validation JSON, main report, status updates, crash recovery preserved.

## 16. Git checkpoint

See live REPORT section after commit/push.

## 17. No-scope-drift audit

- Runtime files changed: NO
- Database writes: 0
- WordPress content writes: 0
- ACF/meta writes: 0
- Rewrite flush: NO
- Menus changed: 0
- Redirects created: 0
- Object create/delete: 0
- V9 source changed: NO
- V9 dist changed: NO
- Theme/plugin source changed: NO
- Plugin updates/installs/deletes: 0
- ACF Extended PRO used: NO
- Old generator reused: NO
- Unexpected changes: none in forbidden scopes

## 18. Final verdict

**PASS**

V9-06D.6 template integration planning rerun: **COMPLETE**

Static-to-WP matrix: **COMPLETE**

ACF binding plan: **COMPLETE**

Integration waves: **COMPLETE**

Runtime delivery plan: **COMPLETE**

Runtime mutations: **0**

Source changes: **0**

Old generator reused: **NO**

Recommended next phase: **CREATE_V9_06D7_GLOBAL_SHELL_ASSET_INTEGRATION_SOURCE_TASK**

V9-06D.7: **READY FOR OPERATOR REVIEW**

## 19. Remaining blockers

- Operator authorization required before D.7 source implementation
- Preflight deviation: required HEAD superseded by unrelated ORCA commits already on remote; D.6 commit alone will be pushed
- Page 6 / Service 73 path debt remains secondary (does not block D.7-A)

## 20. Recommended next action

**CREATE_V9_06D7_GLOBAL_SHELL_ASSET_INTEGRATION_SOURCE_TASK**

---

Target folder:
X:\AI MARS

Volume:
AI WS / X:

Runtime:
X:\MARS-Localhost\sites\wordpress\projects\shpigovsky

V9-06D.6 planning rerun performed:
YES

Old Cursor Resume used:
NO

Old generator reused:
NO

Runtime writes:
0

Database writes:
0

Source changes:
0

V9 source changed:
NO

V9 dist changed:
NO

Theme/plugin source changed:
NO

Content writes:
0

ACF/meta writes:
0

Rewrite flush performed:
NO

Menus changed:
0

Redirects created:
0

Object create/delete:
0

Production content migration performed:
NO

Plugin updates run:
0

Plugin installs run:
0

Plugin deletes run:
0

WPilot write operations:
0

V9-06D.7 authorized:
NO

Secrets committed:
0
