# REPORT — FP-0002 V9-06E29C-E35-FIX01 SELECTIVE PERSISTENCE

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | `X:` |
| Label | `AI WS` |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` (main worktree) |
| HEAD | `ebfaeb225a86d7c0b98ef446908b29c25a9e45df` |
| Upstream relation | ahead 14, behind 17 vs `origin/mars/canonical-post-recovery` |
| Main worktree staged files before | 0 |
| Main worktree WIP count only | ~709 (foreign monorepo WIP ignored) |
| FP-0002 changed/untracked count | ~400 |
| Merge/rebase state | NONE |
| Result | PASS |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e29c-e35-fix01-persistence-before-20260713-032549` |
| DB dump | `mars_wp_fp0002.sql` (2162029 bytes, `--no-tablespaces`) |
| Runtime theme backup/hash | `theme/` copy + `theme-sha256.txt` (631 files) |
| Runtime plugin backup/hash | `plugin/` copy + `plugin-sha256.txt` (21 files) |
| Runtime ACF JSON backup/hash | `acf-json/` copy + `acf-json-sha256.txt` (9 files) |
| Runtime uploads manifest | `uploads-media-manifest.txt` (104 files) |
| Result | PASS |

## 3. Runtime accepted-state evidence

| Evidence | Path | Rows/items | Result |
|---|---|---:|---|
| Route smoke | `X:\AI MARS STORAGE\exports\fp-0002-shpigovsky-persistence\v9-06e29c-e35-fix01-20260713-032549\route-smoke.csv` | 32/32 | PASS |
| Pages inventory | `pages-inventory.csv` | 25 | PASS |
| Services inventory | `services-inventory.csv` | 29 | PASS |
| Program pages | `program-pages.csv` | 4 | PASS |
| Specialists pages | `specialists-pages.csv` | 4 | PASS |
| Blog posts | `blog-posts.csv` | 6 | PASS |
| Media attachments summary | `media-attachments-summary.csv` | 26 | PASS |
| Trashed objects summary | `trashed-objects-summary.csv` | 39 | PASS |
| Accepted-state manifest | `accepted-state-manifest.md` | 1 | PASS |

## 4. Source authority audit

| Class | Count | Notes |
|---|---:|---|
| Include candidates | 130 | Slim allowlist after excluding full `architecture/` dump (690 files) |
| Excluded backup/runtime files | many | Localhost backups, STORAGE dumps, DB `.sql` |
| Foreign files ignored | ~309 | MetaBOT / OCPilot / other MARS WIP |
| Large/binary files reviewed | yes | Favicon PNGs small; placeholders SVG; no DB dumps |
| Secrets detected | 0 | No `.env` / `wp-config` / credentials staged |

## 5. Included files

| File | Status | Reason |
|---|---|---|
| `PROJECT-STATUS.md` | staged+committed | project status / source authority |
| `REPORTS/REPORT-FP-0002-V9-06E29C-E35-FIX01-selective-persistence.md` | staged+committed | E29C-E35 report / persistence report |
| `REPORTS/REPORT-FP-0002-V9-06E29C-excel-structure-completion-generic-pages-favicon.md` | staged+committed | E29C-E35 report / persistence report |
| `REPORTS/REPORT-FP-0002-V9-06E30-services-catalog-child-services-listing-controls.md` | staged+committed | E29C-E35 report / persistence report |
| `REPORTS/REPORT-FP-0002-V9-06E31-program-pages-direction-links-validation-relax.md` | staged+committed | E29C-E35 report / persistence report |
| `REPORTS/REPORT-FP-0002-V9-06E32-home-services-accordion-gallery-service-placeholder.md` | staged+committed | E29C-E35 report / persistence report |
| `REPORTS/REPORT-FP-0002-V9-06E33-FIX01-uslugi-sliders-match-home-gallery.md` | staged+committed | E29C-E35 report / persistence report |
| `REPORTS/REPORT-FP-0002-V9-06E33-service-image-admin-binding-placeholder-uslugi-slider.md` | staged+committed | E29C-E35 report / persistence report |
| `REPORTS/REPORT-FP-0002-V9-06E34-specialists-child-pages-auto-slider.md` | staged+committed | E29C-E35 report / persistence report |
| `REPORTS/REPORT-FP-0002-V9-06E35-FIX01-alcohol-article-image-restore.md` | staged+committed | E29C-E35 report / persistence report |
| `WORDPRESS/SOURCE-AUTHORITY.md` | staged+committed | project status / source authority |
| `WORDPRESS/acf-json/group_fp02_block_specialists.json` | staged+committed | ACF JSON source |
| `WORDPRESS/acf-json/group_fp02_page_home.json` | staged+committed | ACF JSON source |
| `WORDPRESS/acf-json/group_fp02_service_layout_hero.json` | staged+committed | ACF JSON source |
| `WORDPRESS/acf-json/group_fp02_service_structured_sections.json` | staged+committed | ACF JSON source |
| `WORDPRESS/architecture/FP-0002-V9-06E29B-FIX-ADMIN-UI-VALIDATION-v1.md` | staged+committed | E29B-FIX continuum docs |
| `WORDPRESS/architecture/FP-0002-V9-06E29B-FIX-EXACT-FIX-PLAN-v1.md` | staged+committed | E29B-FIX continuum docs |
| `WORDPRESS/architecture/FP-0002-V9-06E29B-FIX-FINAL-CONTRACT-v1.md` | staged+committed | E29B-FIX continuum docs |
| `WORDPRESS/architecture/FP-0002-V9-06E29B-FIX-FULL-BACKUP-v1.md` | staged+committed | E29B-FIX continuum docs |
| `WORDPRESS/architecture/FP-0002-V9-06E29B-FIX-IMPLEMENTATION-RESULT-v1.md` | staged+committed | E29B-FIX continuum docs |
| `WORDPRESS/architecture/FP-0002-V9-06E29B-FIX-PRE-FIX-DIAGNOSIS-v1.md` | staged+committed | E29B-FIX continuum docs |
| `WORDPRESS/architecture/FP-0002-V9-06E29B-FIX-ROLLBACK-INSTRUCTIONS-v1.md` | staged+committed | E29B-FIX continuum docs |
| `WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php` | staged+committed | plugin source E29C-E35 |
| `WORDPRESS/plugins/shpigovsky-core/src/Fields/RepeaterValidation.php` | staged+committed | plugin source E29C-E35 |
| `WORDPRESS/plugins/shpigovsky-core/src/Permalinks/ServicePermalinks.php` | staged+committed | plugin source E29C-E35 |
| `WORDPRESS/reports/FP-0002-V9-06E29B-FIX-OCENTRE-ADMIN-UI-FIELD-VISIBILITY-REPORT-v1.md` | staged+committed | E29B-FIX continuum docs |
| `WORDPRESS/theme/shpigovsky/assets/css/v9-style.css` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/assets/favicon/apple-touch-icon.png` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/assets/favicon/favicon-32x32.png` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/assets/favicon/favicon.ico` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/assets/favicon/favicon.svg` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/assets/images/blog-no-photo.svg` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/assets/images/service-placeholder.svg` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/assets/images/specialist-no-photo.svg` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/assets/js/v9-shell.js` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/functions.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/inc/admin-editor.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/inc/blog-helpers.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/inc/favicon.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/inc/home-helpers.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/inc/institutional-helpers.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/inc/program-direction-helpers.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/inc/reusable-blocks-helpers.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/inc/service-helpers.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/inc/services-hub-helpers.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/inc/services-hub-vendors.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/inc/v9-static-content.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/page-templates/generic.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/components/service-card.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/generic/content-page.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/home/articles-teaser.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/home/gallery.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/home/rehabilitation-program.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/home/specialists.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/home/treatment-prevention.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/institutional/about-program.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/institutional/clinic-landscape.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/institutional/founder-quote.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/service/alcohol-direct-v9/specialists.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/service/nature.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/service/program.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/service/subdivision-stack.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/services-hub/rehabilitation-program.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/theme/shpigovsky/template-parts/services-hub/service-group.php` | staged+committed | theme source E29C-E35 |
| `WORDPRESS/validation/v9-06e29c-e35-fix01-selective-persistence/accepted-state-manifest.md` | staged+committed | persistence evidence export copy |
| `WORDPRESS/validation/v9-06e29c-e35-fix01-selective-persistence/blog-posts.csv` | staged+committed | persistence evidence export copy |
| `WORDPRESS/validation/v9-06e29c-e35-fix01-selective-persistence/fp0002-source-status-at-backup.txt` | staged+committed | persistence evidence export copy |
| `WORDPRESS/validation/v9-06e29c-e35-fix01-selective-persistence/media-attachments-summary.csv` | staged+committed | persistence evidence export copy |
| `WORDPRESS/validation/v9-06e29c-e35-fix01-selective-persistence/pages-inventory.csv` | staged+committed | persistence evidence export copy |
| `WORDPRESS/validation/v9-06e29c-e35-fix01-selective-persistence/program-pages.csv` | staged+committed | persistence evidence export copy |
| `WORDPRESS/validation/v9-06e29c-e35-fix01-selective-persistence/route-smoke.csv` | staged+committed | persistence evidence export copy |
| `WORDPRESS/validation/v9-06e29c-e35-fix01-selective-persistence/services-inventory.csv` | staged+committed | persistence evidence export copy |
| `WORDPRESS/validation/v9-06e29c-e35-fix01-selective-persistence/specialists-pages.csv` | staged+committed | persistence evidence export copy |
| `WORDPRESS/validation/v9-06e29c-e35-fix01-selective-persistence/trashed-objects-summary.csv` | staged+committed | persistence evidence export copy |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_check_ptsr.py` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_compare_78_79.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_compare_http.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_debug_post79.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_debug_ptrs.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_debug_ptrs_filter.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_debug_ptrs_query.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_e29c_execute.py` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_e29c_probe.py` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_e29c_repair.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_e29c_repair_db.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_e29c_runner.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_e29c_trash_slug_repair.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_fix_ptrs_probe.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_list_services.py` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_meta_78_79.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_probe_deep_url.py` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/_runner_summary.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/execution-summary.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/http-validation.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/mutation-result.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/post-mutation-inventory.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/pre-mutation-inventory.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/probe-inventory.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/repair-db-result.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e29c-excel-structure-completion/trash-slug-repair.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e30-services-catalog-child-services-listing-controls/_e30_seed_runner.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e30-services-catalog-child-services-listing-controls/_e30_validate.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e30-services-catalog-child-services-listing-controls/e30-http-validation.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e30-services-catalog-child-services-listing-controls/e30-route-inventory-after.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e30-services-catalog-child-services-listing-controls/e30-seed-result.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e31-program-pages-direction-links-validation-relax/_e31_audit_probe.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e31-program-pages-direction-links-validation-relax/_e31_flush.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e31-program-pages-direction-links-validation-relax/_e31_inventory.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e31-program-pages-direction-links-validation-relax/_e31_runner.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e31-program-pages-direction-links-validation-relax/_e31_title_check.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e31-program-pages-direction-links-validation-relax/_e31_validate.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e31-program-pages-direction-links-validation-relax/_e31_validate_stdout.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e31-program-pages-direction-links-validation-relax/e31-http-validation.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e31-program-pages-direction-links-validation-relax/e31-mutation-result.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e32-home-services-accordion-gallery-placeholder/_e32_admin_recheck.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e32-home-services-accordion-gallery-placeholder/_e32_retire_nav_db.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e32-home-services-accordion-gallery-placeholder/_e32_retire_nav_field.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e32-home-services-accordion-gallery-placeholder/_e32_seed_and_validate.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e32-home-services-accordion-gallery-placeholder/e32-admin-recheck.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e32-home-services-accordion-gallery-placeholder/e32-nav-field-probe.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e32-home-services-accordion-gallery-placeholder/e32-nav-retire.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e32-home-services-accordion-gallery-placeholder/e32-validation.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e34-specialists-child-pages-auto-slider/_e34_audit.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e34-specialists-child-pages-auto-slider/_e34_find_service.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e34-specialists-child-pages-auto-slider/_e34_mutate.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e34-specialists-child-pages-auto-slider/_e34_service_probe.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e34-specialists-child-pages-auto-slider/_e34_validate.php` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e34-specialists-child-pages-auto-slider/e34-audit-before.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e34-specialists-child-pages-auto-slider/e34-mutation-result.json` | staged+committed | stage validation evidence |
| `WORDPRESS/validation/v9-06e34-specialists-child-pages-auto-slider/e34-validation.json` | staged+committed | stage validation evidence |

## 6. Excluded files

| File/pattern | Reason |
|---|---|
| `INCOMING/**` (`.fig`, design, video) | Design intake; not source authority product |
| `REPORTS/_fig_parse_temp/**`, `_fig_logo_extract/**` | Temp parse artefacts |
| `WORDPRESS/architecture/**` except E29B-FIX `*.md` | 690-file tree; out of E29C–E35 allowlist |
| Modified D9C/D9L/D9P reports | Pre-E29C; not in accepted stack |
| `validation/v9-06d*` / older `v9-06e0..e28` / chrome profiles / `node_modules` | Prior-stage / temp / huge |
| `validation/**/*.sql`, Localhost backups, STORAGE dump folders | Runtime/backup; not Git source |
| MetaBOT / OCPilot / iSEO / other workspaces | Foreign WIP |

## 7. Temp worktree / commit path

| Item | Value |
|---|---|
| Temp worktree used | YES |
| Temp worktree path | `X:\AI MARS STORAGE\git-sync-fp0002-e29c-e35-20260713-032549\repo` |
| Temp branch | `fp0002/v9-06e29c-e35-fix01-persistence-20260713-032549` |
| Base HEAD | `ebfaeb225a86d7c0b98ef446908b29c25a9e45df` |
| Clean before copy | YES (after skip-worktree on 19 long-path ghost deletions from Windows path limit) |
| Copy method | Exact-path `Copy-Item` from main dirty worktree → temp worktree |
| Staged files count | 130 |
| Staged files scope valid | YES |
| Commit attempted | YES |
| Commit hash | `bcd3dd7e366316f208810c553b46bc139687ceab` (tip `ff871ab4a6ece471430827bc192c1e5d74fb7f8c`) |
| Commit message | `FP-0002: persist v9 e29c-e35 local WordPress updates` |
| Push attempted | NO |

## 8. Patch fallback

| Item | Value |
|---|---|
| Patch bundle created | NO |
| Patch bundle path | — |
| Patch file | — |
| Commit skipped reason | N/A (commit created) |

## 9. Route smoke validation

| Route | Expected | HTTP | Result | Notes |
|---|---|---:|---|---|
| `/` | 200 | 200 | PASS | core  |
| `/uslugi/` | 200 | 200 | PASS | core  |
| `/blog/` | 200 | 200 | PASS | core  |
| `/specyalisty/` | 200 | 200 | PASS | core  |
| `/o-centre/` | 200 | 200 | PASS | core  |
| `/o-centre/programma-lecheniya/` | 200 | 200 | PASS | core  |
| `/kontakty/` | 200 | 200 | PASS | core  |
| `/otzyvy/` | 200 | 200 | PASS | core  |
| `/o-centre/programma-lecheniya/genotipirovanie/` | 200 | 200 | PASS | program  |
| `/o-centre/programma-lecheniya/neyropsihologicheskaya-korrektsiya/` | 200 | 200 | PASS | program  |
| `/o-centre/programma-lecheniya/psihokorrektsiya/` | 200 | 200 | PASS | program  |
| `/o-centre/programma-lecheniya/kinezioterapiya/` | 200 | 200 | PASS | program  |
| `/specyalisty/shipovsky/` | 200 | 200 | PASS | specialist  |
| `/specyalisty/kazakov/` | 200 | 200 | PASS | specialist  |
| `/specyalisty/kostyuk/` | 200 | 200 | PASS | specialist  |
| `/specyalisty/shapiguzova/` | 200 | 200 | PASS | specialist  |
| `/blog/nazvanie-stati/` | 200 | 200 | PASS | blog  |
| `/blog/yoga-v-terapii-abstinentnyy-sindrom/` | 200 | 200 | PASS | blog-e35  |
| `/blog/bos-terapiya-trenirovka-zon-mozga/` | 200 | 200 | PASS | blog-e35  |
| `/blog/genotipirovanie-pri-zavisimostyah/` | 200 | 200 | PASS | blog-e35  |
| `/blog/kak-prohodit-pervaya-konsultatsiya/` | 200 | 200 | PASS | blog-e35  |
| `/blog/sryvy-i-retsidivy-signal-k-korrektirovke/` | 200 | 200 | PASS | blog-e35  |
| `/uslugi/zavisimosti/` | 200 | 200 | PASS | service  |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | 200 | PASS | service  |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | 200 | PASS | service  |
| `/uslugi/zavisimosti/internet-zavisimost/` | 200 | 200 | PASS | service-canonical  |
| `/uslugi/genotipirovanie/` | 404 | 404 | PASS | expected-removed Not Found |
| `/uslugi/zavisimosti/lechenie-internet-zavisimosti/` | 404 | 404 | PASS | expected-removed Not Found |
| `/uslugi/zavisimosti/lechenie-opiumnoy-zavisimosti/` | 200 | 200 | PASS | service-opium  |
| `/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/` | 200 | 200 | PASS | service-narcotic-parent  |
| `/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/geroin/` | 200 | 200 | PASS | service-deep  |
| `/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/internet-zavisimost/` | 200 | 200 | PASS | service-canonical  |

## 10. Main worktree preservation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Main worktree staged files after | 0 | 0 | PASS |
| Foreign WIP untouched | yes | yes | PASS |
| No reset/rebase/stash/clean | yes | yes | PASS |
| No push | yes | yes | PASS |

## 11. Documentation updates

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E29C-E35-FIX01-selective-persistence.md | created | PASS | Full report |
| PROJECT-STATUS.md | updated | PASS | Points to E35-FIX01 + persistence |
| WORDPRESS/SOURCE-AUTHORITY.md | updated | PASS | E31/E33/E35 + persistence notes; no production claim |

## 12. Git result

COMMIT_CREATED

| Item | Value |
|---|---|
| Commit hash (content) | `bcd3dd7e366316f208810c553b46bc139687ceab` |
| Commit hash (tip) | `f77ee7ebde7e597107d3bdb20aa0215a20268cce` |
| Temp branch | `fp0002/v9-06e29c-e35-fix01-persistence-20260713-032549` |
| Patch bundle | — |
| Commit skipped reason | — |
| Push | NO |

## 13. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Main branch ahead/behind remote | medium | open | Separate reconciliation task; do not merge blindly |
| Commit lives only on temp branch / worktree | medium | accepted | Operator review before any merge/push |
| Windows long-path sparse checkout ghosts | low | mitigated | skip-worktree; files remain in base tree |
| Runtime DB/media not in Git | info | expected | Backup dump + inventories evidence persistence |
| Foreign WIP volume | medium | contained | Never staged |

## 14. Final verdict

PASS

V9-06E29C-E35-FIX01 selective persistence:
COMPLETE

Runtime accepted state evidenced:
PASS

Source authority audited:
PASS

Selective commit:
PASS

Patch fallback:
SKIPPED

Foreign WIP preserved:
PASS

Main worktree preserved:
PASS

No push:
PASS

No destructive Git:
PASS

Recommended next phase:
OPERATOR_REVIEW_PERSISTENCE_RESULT

## 15. Recommended next action

OPERATOR_REVIEW_PERSISTENCE_RESULT

## 16. Final safety statement

Target folder:
X:\AI MARS

V9-06E29C-E35-FIX01 selective persistence performed:
YES

Backup created:
YES

Runtime DB writes:
0

Source changes in main worktree:
YES

Temp worktree used:
YES

Git mutation:
YES

Git commit:
f77ee7ebde7e597107d3bdb20aa0215a20268cce (content bcd3dd7e366316f208810c553b46bc139687ceab)

Git branch:
fp0002/v9-06e29c-e35-fix01-persistence-20260713-032549

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

Main worktree staged files:
0

FP-0002 product contaminated:
NO

WPilot confused with OCPilot:
NO

Secrets committed:
0

## Execution safety
- cwd: `X:\AI MARS`
- scope lock honored: yes
- destructive ops: none
- protected zone touch: none
