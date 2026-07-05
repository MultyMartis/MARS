# FP-0002 WordPress Source Authority

**Version:** v1  
**Date:** 2026-07-03  
**Task:** FW-07C-2C

---

## Canonical source decision

| Surface | Origin | Runtime match | Canonical source | Classification |
|---------|--------|---------------|------------------|----------------|
| Theme `shpigovsky` | V6 `theme-source/shpigovsky` + runtime deltas | DELIVERED TO LOCAL RUNTIME in V9-06D.1 rerun | `WORDPRESS/theme/shpigovsky/` | CANONICAL_CURRENT — ADOPTED — RUNTIME DELIVERED |
| Plugin `shpigovsky-core` | V6 `functionality-plugin/shpigovsky-core` + runtime deltas | DELIVERED TO LOCAL RUNTIME in V9-06D.1 rerun | `WORDPRESS/plugins/shpigovsky-core/` | CANONICAL_CURRENT — ADOPTED — CONTENT MODEL ACTIVE |
| ACF JSON | V6 empty state + V9-06C source generation | 13 JSON files delivered to local runtime in V9-06D.1 rerun | `WORDPRESS/acf-json/` | REGISTERED — RUNTIME DELIVERED |

## Historical surfaces

| Path | Classification |
|------|----------------|
| `workspaces/fp-0002-shpigovsky-v6/WORDPRESS/` | FOUNDATION_ORIGIN / HISTORICAL |
| Runtime `wp-content/themes/shpigovsky/` | RUNTIME_ONLY (deployment target) |
| Runtime `wp-content/plugins/shpigovsky-core/` | RUNTIME_ONLY (deployment target) |

Runtime was **not** silently treated as canonical. Foundation captured from runtime after hash comparison and provenance review (V9-05A adoption). V6 remains historical reference; drift documented.

## Source/runtime boundary

```text
Git source (editable)     →  Package (manifested ZIP)  →  Runtime (deploy only)
WORDPRESS/theme/...          shpigovsky-theme-foundation-*     wp-content/themes/shpigovsky/
WORDPRESS/plugins/...        shpigovsky-core-foundation-*      wp-content/plugins/shpigovsky-core/
WORDPRESS/acf-json/          fp-0002-acf-json-foundation-*     wp-content/acf-json/
```

## Excluded from source

- WordPress core
- WPilot plugin
- MU-plugins
- Uploads
- wp-config.php secrets
- Generated caches/logs
- V9 `src/` and `dist/` (separate authority)

## Secret audit

Foundation baseline scanned at capture; no secrets detected in theme/plugin source files.

## V9-06D7-F final route QA (2026-07-05)

Read-only QA PASS after D7-A–D7-E runtime deliveries. Evidence: `validation/v9-06d7f-final-route-qa/`. No runtime/source/DB mutations. Recommended next: D8 content seed planning.

## V9-06D8 content seed planning (2026-07-05)

Planning-only PASS. MVP content gap map, ACF/options field inventory, Olga admin UX plan, seed wave design (D8-A…G), content source map, and future seed mutation safety protocol documented in Git. Live runtime DB inventory unavailable at task time; D7-F and D4 evidence used. No runtime/source/DB/content/ACF/options mutations. Recommended next: D8-A site options seed. Evidence: `validation/v9-06d8-content-seed-planning/`.

## V9-06D8-A site options seed (2026-07-05)

D8-A initial run: planning gates PASS; apply BLOCKED (MySQL/HTTP unavailable). Resume apply **COMPLETE**: 11 site options seeded (LOCAL_MVP_PLACEHOLDER from V9 static); 5 fields skipped (operator/DO_NOT_SEED). DB checkpoint `v9-06d8a-site-options-seed-pre-20260705-033228`. Route smoke ALL_200. Options-only writes; no content/meta/menu/rewrite mutations. Local helper `_site_options_seed_runner.php` used but not committed. Evidence: `validation/v9-06d8a-site-options-seed/final-verdict-resume.json`. Report: `reports/FP-0002-V9-06D8A-SITE-OPTIONS-SEED-RESUME-REPORT-v1.md`.

## V9-06D8-B home content seed (2026-07-05)

D8-B **COMPLETE (PARTIAL PASS)**: Home page #4 ACF only — `home_advantages` (6 rows) and `home_faq_items` (5 rows) seeded from V9 static; `home_hero_slides` normalize failed (D4 seed retained). Gallery/reviews/blog/media skipped. DB checkpoint `v9-06d8b-home-content-seed-pre-20260704-204316`. Route smoke ALL_200. Home visual smoke PASS. No runtime/source/options/service/contacts writes. Local helper `_home_content_seed_runner.php` used but not committed. Evidence: `validation/v9-06d8b-home-content-seed/final-verdict.json`. Report: `reports/FP-0002-V9-06D8B-HOME-CONTENT-SEED-REPORT-v1.md`.

## V9-06D8-C services MVP content seed (2026-07-05)

D8-C **COMPLETE (PASS)**: Service CPT #73/#74/#77/#84 ACF only — 15 field writes (priority #74: intro_note, signs, programme, stages, FAQ; parents: programme/stages/FAQ). V9 traceable source; FAQ LOCAL_MVP_PLACEHOLDER. DB checkpoint `v9-06d8c-services-mvp-content-seed-pre-20260704-205431`. Route smoke ALL_200. Service 74 alcohol-special regression PASS. No runtime/source/home/hub/contacts/options writes. Local helper `_services_content_seed_runner.php` used but not committed. Evidence: `validation/v9-06d8c-services-mvp-content-seed/final-verdict.json`. Report: `reports/FP-0002-V9-06D8C-SERVICES-MVP-CONTENT-SEED-REPORT-v1.md`. Next: D8-D services hub content seed.

## V9-06D8-D services hub content seed (2026-07-05)

D8-D **COMPLETE (PASS)**: Services Hub page #5 ACF only — 2 field writes (`services_hub_intro` V9 heroLead; `services_hub_faq_items` 5 rows LOCAL_MVP_PLACEHOLDER from V9 `faq.html` items 2–6). Developer-only `services_hub_query_mode` / `services_hub_show_placeholders` unchanged. DB checkpoint `v9-06d8d-services-hub-content-seed-pre-20260704-210430`. Route smoke ALL_200. Hub visual smoke PASS. No runtime/source/home/service/contacts/options writes. Local helper `_services_hub_content_seed_runner.php` used but not committed. Evidence: `validation/v9-06d8d-services-hub-content-seed/final-verdict.json`. Report: `reports/FP-0002-V9-06D8D-SERVICES-HUB-CONTENT-SEED-REPORT-v1.md`. Next: D8-E contacts content seed.

## V9-06D8-E contacts content seed (2026-07-05)

D8-E **COMPLETE (PASS)**: Contacts page #20 ACF only — 3 field writes (`contacts_form_intro` V9 intro; `contacts_address` V9 Moscow consulting address; `contacts_blocks` 2 V9 location rows). `contacts_map_url`, `contacts_messengers`, `contacts_phones` skipped (operator URLs or D8-A options canonical). DB checkpoint `v9-06d8e-contacts-content-seed-pre-20260704-211441`. Route smoke ALL_200. Contacts visual smoke PASS. No runtime/source/home/hub/service/options writes. Local helper `_contacts_content_seed_runner.php` used but not committed. Evidence: `validation/v9-06d8e-contacts-content-seed/final-verdict.json`. Report: `reports/FP-0002-V9-06D8E-CONTACTS-CONTENT-SEED-REPORT-v1.md`. Next: D8-G post-seed QA.

## V9-06D8-G post-seed QA (2026-07-05)

D8-G **COMPLETE (PARTIAL PASS)**: Read-only post-seed QA after D8-A…E. Route matrix ALL_200; ACF integrity PASS; visual smoke 11/11 required screenshots PASS; admin usability PARTIAL (English ACF labels); no-scope-drift PASS. Zero DB/ACF/runtime/source mutations. Local helpers `_runner.py` / `_screenshots.mjs` used but not committed. Strict HEAD gate PASS_WITH_HEAD_NOTE (branch synced; +1 ancestor commit after D8-E). Readiness: **READY_FOR_OPERATOR_VISUAL_REVIEW**. Evidence: `validation/v9-06d8g-post-seed-qa/`. Report: `reports/FP-0002-V9-06D8G-POST-SEED-QA-REPORT-v1.md`. Next: operator visual review; optional D8-F admin UX repair.

## V9-06D9-A visual parity audit (2026-07-05)

D9-A **COMPLETE (FAIL)**: Read-only static V9 dist vs local WP runtime visual parity audit after operator visual review. Home section transfer FAIL (20 static vs 6 runtime sections). Hero parity FAIL (no `hero__media`; ACF image not seeded). Header/nav typography PARTIAL (computed tokens match on shared items; 5 Inter woff2 HTTP 404 at `/assets/fonts/`). Global font/asset parity FAIL. 18 comparable screenshots captured. Zero DB/ACF/runtime/source/theme/plugin/ACF JSON/V9 mutations. Local helper `_audit_runner.mjs` used but not committed. Strict HEAD gate PASS_WITH_HEAD_NOTE (required D8-G HEAD `4a22b701` is ancestor; actual `ed009cbb` +1 commit; branch synced 0/0). Evidence: `validation/v9-06d9a-visual-parity-audit/`. Report: `reports/FP-0002-V9-06D9A-VISUAL-PARITY-AUDIT-REPORT-v1.md`.

## V9-06D9-0 full V9 visual port charter (2026-07-05)

D9-0 **COMPLETE (PASS)**: Read-only full visual port charter reframing WP runtime as MVP skeleton upgrading to full V9 parity. Documents static/WP inventories, lightweight-vs-broken classification, header messenger parity (static `#` placeholders vs WP empty `social_links`), home 20-section transfer plan, asset/font/vendor plan, ACF/content/media requirements, implementation waves D9-B…H. Zero DB/ACF/runtime/source mutations. Strict HEAD gate PASS (`bc2b9c3c`). Evidence: `validation/v9-06d9-0-full-visual-port-charter/`. Report: `reports/FP-0002-V9-06D9-0-FULL-V9-VISUAL-PORT-CHARTER-REPORT-v1.md`. Next: **CREATE_V9_06D9B_HEADER_FONT_ASSET_MESSENGER_REPAIR_TASK** (recommended over D9-C hero-first).

## V9 implementation

V9 frontend HTML/CSS/JS integration is **NOT INCLUDED** in V9-06C. V9 frontend remains under `workspaces/fp-0002-shpigovsky-v9/`.

V9-06C adds WordPress content model source only: Shpigovsky Core CPT/permalink/ACF/admin/validation source and canonical ACF JSON under `WORDPRESS/acf-json/`. V9-06C.1 resolves the Shpigovsky Core source activation gate with `SHPIGOVSKY_CORE_MODE=content_model`. V9-06D.1 rerun delivered this source into local runtime and verified content model activation. Object skeleton is **COMPLETE** in the local FP-0002 runtime as V9-06D.2; content migration, redirects, rewrite flush, and V9 integration remain **NOT STARTED**.

## Operator-managed external plugin boundary

V9-06B.2 admits ACF PRO as an operator-managed external dependency. The installed plugin files under runtime wp-content/plugins/advanced-custom-fields-pro/ are **not** canonical source, are **not** copied into Git, and are **not** delivered by Forge filesystem packages.

ACF Extended PRO is also operator-managed, active, and classified separately, but not approved for FP-0002 use by default. ACF Free is inactive fallback only.

Forbidden for these dependencies: automatic update, replacement, deletion, package delivery, license handling, license bypass repair, source mirroring, and unattended remediation. See architecture/FP-0002-OPERATOR-MANAGED-EXTERNAL-PLUGINS-v1.md.



## V9-06C.1 activation gate

Delivery of the previous V9-06D.1 package was blocked by the old skeleton gate and is now superseded by V9-06C.1 source repair. The current canonical source is activation-ready for a separate V9-06D.1 rerun. V9-06C.1 did not change runtime files, database state, external plugins, or WordPress objects.


## V9-06D.1 rerun runtime delivery

Runtime delivery is complete for the local FP-0002 runtime only. The runtime remains a deployment target, not canonical editable source. External plugins remain operator-managed and were not delivered, updated, replaced, or modified.


## V9-06D.2 object skeleton

Local runtime object skeleton is complete: 15 Service CPT objects created, required Page templates reconciled, no content migration, no V9 integration, no menu changes, no redirects, and no rewrite flush. Runtime remains deployment target; Git source records documentation and evidence only.


## V9-06D.3 content migration planning

Content migration planning is complete in Git documentation only. No runtime content writes, no V9 integration, no menu/redirect/rewrite changes.


## V9-06D.4 RERUN minimal content seed

Local runtime minimal ACF/meta seed is complete for authorized Pages 4/5/20 and Services 73/74/77/84 only. Full production content migration, V9 integration, menus, redirects, and Options Page values remain not performed. Previous blocked D.4 attempt is preserved as historical evidence.

## REWRITE-FLUSH-MICRO-GATE

Soft rewrite flush performed in local runtime only (`rewrite_rules` option). Hard flush not used; `.htaccess` unchanged. Service 74 remains HTTP 404 with correct generated permalink (`FLUSH_NOT_SUFFICIENT`). No content, menu, redirect, plugin, or V9 source/dist changes. Runtime remains deployment target; Git source records documentation and evidence only.

## ROUTE-OWNERSHIP-INVESTIGATION

Read-only route ownership investigation complete. Root cause: `POST_TYPE_LINK_REWRITE_MISMATCH` (depth-2 rewrite leaf-only `service` query var). Page ID 6 / Service ID 73 path collision confirmed as secondary. No runtime writes, no rewrite flush, no source edits in this phase. Recommended next: rewrite rule repair micro-task. V9-06D.5 blocked until Service 74 resolves.

## REWRITE-RULE-REPAIR

Depth-2 rewrite query mapping repaired in canonical source `ServicePermalinks.php` (`service=$matches[1]/$matches[2]`) and delivered to local runtime. Soft rewrite flush performed under DB/plugin checkpoint. Service 74 HTTP 200. Contract §4.2 updated. Content/ACF/menus/redirects unchanged. Page 6 / Service 73 secondary debt remains. V9-06D.5 unblocked for visual route QA.

## V9-06D.5 visual route QA

Read-only visual route QA complete after rewrite repair. All required D.5 routes HTTP 200; Service 74 regression PASS; skeleton template/render baseline confirmed; screenshots under `validation/v9-06d5-visual-route-qa/screenshots/`. No runtime content/ACF/menu/redirect/source mutations. V9 integration and production content migration remain not started.

## V9-06D.6 template integration planning

Planning-only package complete (rerun after crash recovery). Maps V9 static blocks to theme templates/partials, ACF binding/fallbacks, waves D7-A…F, delivery/rollback, and risks. No theme/plugin/V9 source edits, no runtime delivery, no content/ACF writes. Next: V9-06D.7 global shell/asset integration source task (operator review; not authorized here).

## V9-06D7-A global shell asset source

Source-only global shell integration in `WORDPRESS/theme/shpigovsky/`: V9 CSS/JS/fonts/webfonts/shell images packaged from `workspaces/fp-0002-shpigovsky-v9/dist/`; header/footer/offcanvas/modal/scroll markup; enqueue via `inc/assets.php`. No runtime delivery, no DB/content/ACF/menu writes, no plugin or V9 src/dist edits. Validation: `validation/v9-06d7a-global-shell-asset-source/`. Next: V9-06D7-A runtime delivery task (operator review).


## V9-06D7-A runtime delivery

Canonical D7-A theme source delivered to local runtime `wp-content/themes/shpigovsky/` only. Additive/update copy; no deletes; no plugin/core/uploads/ACF JSON changes. Hash match 453/453. Runtime remains deployment target; Git canonical source unchanged post-delivery. Evidence: `validation/v9-06d7a-runtime-delivery/`.

## V9-06D7-B home template source

Source-only home template integration in `WORDPRESS/theme/shpigovsky/`: V9-compatible home template-parts, `inc/home-helpers.php`, intro-section front-page boundary, ACF read/fallback bindings. Theme version `0.4.0-d7b-home`. No runtime delivery, no DB/content/ACF writes, no plugin or V9 src/dist edits. Validation: `validation/v9-06d7b-home-template-source/`. Next: V9-06D7-B runtime delivery task (operator review; not authorized here).


## V9-06D7-B runtime delivery

Canonical D7-B home template source delivered to local runtime `wp-content/themes/shpigovsky/` only. Additive/update copy (1 ADD, 11 MODIFY); no deletes; no plugin/core/uploads/ACF JSON changes. Hash match 454/454. Runtime remains deployment target; Git canonical source unchanged post-delivery. Evidence: `validation/v9-06d7b-runtime-delivery/`.

## V9-06D7-C services hub template source

Source-only Services Hub integration in `WORDPRESS/theme/shpigovsky/`: V9-compatible hero, CPT-driven category hub groups, rehabilitation program, FAQ, shared final-form; `inc/services-hub-helpers.php`. Theme version `0.5.0-d7c-services-hub`. No runtime delivery, no DB/content/ACF writes, no plugin or V9 src/dist edits. Validation: `validation/v9-06d7c-services-hub-template-source/`. Next: V9-06D7-C runtime delivery task (operator review; not authorized here).


## V9-06D7-D service template source

Source-only Service single integration in `WORDPRESS/theme/shpigovsky/`: V9-compatible subdivision/leaf/alcohol stacks, `inc/service-helpers.php`, ACF layout variant routing with hierarchy/slug fallback, guarded section template-parts. Theme version `0.6.0-d7d-service-templates`. No runtime delivery, no DB/content/ACF writes, no plugin or V9 src/dist edits. Validation: `validation/v9-06d7d-service-template-source/`. Next: V9-06D7-D runtime delivery task (operator review; not authorized here).


## V9-06D7-D runtime delivery

Canonical D7-D Service template source (commit `c54c23d0`) delivered to local runtime `wp-content/themes/shpigovsky/` only. Additive/update copy; no deletes; no plugin/core/uploads/ACF JSON changes. Hash match verified post-delivery. Runtime remains deployment target; Git canonical source unchanged post-delivery. Evidence: `validation/v9-06d7d-runtime-delivery/`.

## V9-06D7-E contacts template source

Source-only Contacts page integration in `WORDPRESS/theme/shpigovsky/`: V9-compatible `contacts-map-body` and `contacts-rehabilitation-steps`, `inc/contacts-helpers.php`, ACF page field and site option read/fallback bindings. Theme version `0.7.0-d7e-contacts-template`. Runtime delivery performed 2026-07-05. Canonical D7-E source (commit `5a7eb400`) delivered to local runtime `wp-content/themes/shpigovsky/` only. Additive/update copy; no deletes; no plugin/core/uploads/ACF JSON changes. Hash match verified post-delivery. Evidence: `validation/v9-06d7e-runtime-delivery/`.


## V9-06D7-E runtime delivery

Canonical D7-E Contacts template source (commit `5a7eb400`) delivered to local runtime `wp-content/themes/shpigovsky/` only. Six theme files (2 ADD, 4 MODIFY). Hash match verified post-delivery. Runtime remains deployment target; Git canonical source unchanged post-delivery. Evidence: `validation/v9-06d7e-runtime-delivery/`.

## V9-06D9-B header/font/messenger repair (2026-07-05)

D9-B **PARTIAL PASS**: Inter `@font-face` paths rewritten to theme-relative `../fonts/inter/`; 6 WOFF2 files copied from V9 dist into theme source; messenger visual fallback (`href="#"`) when `social_links` empty. Bounded runtime delivery: 10 files to active `wp-content/themes/shpigovsky/` and charter `app/public/.../themes/shpigovsky/` (WordPress ABSPATH = project root). No DB/ACF/options/menu writes. Primary nav mega-menu deferred D9-B2. Evidence: `validation/v9-06d9b-header-font-asset-messenger-repair/`. Report: `reports/FP-0002-V9-06D9B-HEADER-FONT-ASSET-MESSENGER-REPAIR-REPORT-v1.md`. Next: D9-C home hero parity.

## V9-06D9-C home hero parity repair (2026-07-05)

D9-C **PASS**: Home hero media restored via theme asset fallback — `hero-main.png` copied from V9 static source into `theme/shpigovsky/assets/img/hero/`; `shpigovsky_get_home_hero_image_fallback()` added; `template-parts/home/hero.php` renders `hero__media` when ACF `home_hero_slides[0].image` empty (ACF wins when seeded). Bounded runtime delivery: 3 files to active theme only. No DB/ACF/options/menu writes; no media uploads to WP library. Hero image HTTP 200; route smoke ALL_200. Evidence: `validation/v9-06d9c-home-hero-parity-repair/`. Report: `reports/FP-0002-V9-06D9C-HOME-HERO-PARITY-REPAIR-REPORT-v1.md`. Next: D9-D home full section transfer.

## V9-06D9-D home main + footer static V9 transplant (2026-07-05)

D9-D **PASS**: Replaced MVP 6-section Home main with static V9 19-section orchestration; transplanted global footer from V9 static authority; hero CTA label fixed to `Записаться на консультацию`; 93 assets + vendors copied to theme source; bounded runtime delivery (~119 files). No DB/ACF/options/menu writes. Route smoke ALL_200; 19/19 home sections present. Strict HEAD gate PASS_WITH_HEAD_NOTE (required D9-C HEAD `2c576542` is ancestor; actual `0693c4b5` +1 unrelated commit; branch synced 0/0). Evidence: `validation/v9-06d9d-home-main-footer-static-v9-transplant/`. Report: `reports/FP-0002-V9-06D9D-HOME-MAIN-FOOTER-STATIC-V9-TRANSPLANT-REPORT-v1.md`. Next: D9-E slider/vendor parity.

## V9-06D9-E home slider / vendor / pagination repair (2026-07-05)

D9-E **PASS**: Repaired Home slider visual parity without Home main rewrite. Fixed specialists heading transplant typo (`Специалисты центра` / `specialists-heading`); fixed vendor CSS cascade order (swiper → fancybox → v9-style) so pagination dots match static V9 bordered style. Bounded runtime delivery: 2 theme files. No DB/ACF/options/menu writes. Route smoke ALL_200. Evidence: `validation/v9-06d9e-home-slider-vendor-pagination-repair/`. Report: `reports/FP-0002-V9-06D9E-HOME-SLIDER-VENDOR-PAGINATION-REPAIR-REPORT-v1.md`. Next: D9-F visual parity QA.

## V9-06D9-F home + footer visual parity QA (2026-07-05)

D9-F **PARTIAL PASS**: Read-only QA after D9-D/D9-E. Home 19/19 sections + order PASS; footer transplant PASS; D9-E slider/vendor/pagination verified PASS; assets + secondary routes ALL_200 PASS. One minor defect: `template-parts/home/faq.php` retains D9-D `comfort-heading` transplant typo (wrong id/aria + heading copy; duplicate id with comfort section). No runtime/source/DB/ACF mutations. ACF wiring NOT_READY until FAQ micro repair. Evidence: `validation/v9-06d9f-home-footer-visual-parity-qa/`. Report: `reports/FP-0002-V9-06D9F-HOME-FOOTER-VISUAL-PARITY-QA-REPORT-v1.md`. Next: D9-G micro visual repair.

## V9-06D9-G FAQ micro visual repair (2026-07-05)

D9-G **PASS**: Repaired FAQ heading contract in `template-parts/home/faq.php` — `aria-labelledby` and heading `id` restored to `faq-heading`; heading text restored to `Нас часто спрашивают`; duplicate `comfort-heading` id eliminated. Bounded runtime delivery: 1 theme file. No DB/ACF/options/menu writes. Post-repair Home FAQ parity PASS; comfort section unchanged; route smoke ALL_200. ACF editability readiness: READY. Evidence: `validation/v9-06d9g-micro-visual-repair-faq-heading/`. Report: `reports/FP-0002-V9-06D9G-FAQ-MICRO-VISUAL-REPAIR-REPORT-v1.md`. Next: D9-H ACF admin editability wiring.

## V9-06D9-H ACF admin editability wiring (2026-07-05)

D9-H **PASS**: Wired Home + Footer ACF schema and templates over D9-G static V9 transplant. Added 9 heading/lead fields to `group_fp02_page_home`; created `inc/home-fallbacks.php`; wired hero, recovery-intro, FAQ, gallery, feature-grid, section headings, final-form, footer CTA labels. Bounded runtime delivery: 14 files (13 theme + 1 ACF JSON). No DB/ACF value/options/menu writes. Post-implementation: 19/19 sections, FAQ contract, hero CTA, sliders/dots, routes ALL_200. Evidence: `validation/v9-06d9h-acf-admin-editability-wiring/`. Report: `reports/FP-0002-V9-06D9H-ACF-ADMIN-EDITABILITY-WIRING-REPORT-v1.md`. Next: D9-I controlled ACF seed.

## V9-06D9-I controlled ACF seed (2026-07-05)

D9-I **PASS**: Seeded 10 safe Home page #4 ACF fields from static V9 authority (`inc/home-fallbacks.php` + D9-H template fallbacks). DB checkpoint before writes. No source/theme/ACF JSON/options/menu changes; no media uploads. Post-seed: 19/19 sections, FAQ contract, hero CTA, routes ALL_200; admin fields populated for recovery intro, intro bands, section headings. Skipped: hero image, gallery media (D9-J), FAQ expansion (5 items D8-B), already-populated D8-B fields. Preflight strict HEAD gate PARTIAL (local +1 governance commit; remote at D9-H HEAD). Evidence: `validation/v9-06d9i-controlled-acf-seed/`. Report: `reports/FP-0002-V9-06D9I-CONTROLLED-ACF-SEED-REPORT-v1.md`. Next: D9-J media selection upload plan.

## V9-06D9-J media selection upload plan (2026-07-05)

D9-J **PASS**: Read-only media inventory and D9-K upload/seed plan. Inventoried 40 Home-related static/theme assets; WP Media Library empty (0 attachments); ACF gap documented for `home_hero_slides.image` (empty) and `home_gallery_media` (empty repeater). Classified 5 assets UPLOAD_AND_SEED_D9K (hero + 4 gallery). D9-K phased plan + rollback documented. Frontend baseline PASS (19 sections, theme fallbacks, routes ALL_200); 9 runtime screenshots captured; wp-admin screenshots skipped (auth). Zero DB/ACF/source/theme/runtime mutations. Strict HEAD gate PASS (`3d34449a`). Evidence: `validation/v9-06d9j-media-selection-upload-plan/`. Report: `reports/FP-0002-V9-06D9J-MEDIA-SELECTION-UPLOAD-PLAN-REPORT-v1.md`. Next: D9-K controlled media upload + ACF seed.

## V9-06D9-K controlled media upload + ACF seed (2026-07-05)

D9-K **PASS**: Uploaded 5 approved Home media files (hero-main.png + 4 gallery webp) to WP Media Library (attachments 89–93); seeded `home_hero_slides[0].image` and `home_gallery_media` (4 rows) on page #4. DB checkpoint before writes. Checksum parity with static V9 sources. Post-seed: frontend serves `/uploads/2026/07/` URLs; 19/19 sections; hero CTA; gallery pagination; routes ALL_200. No source/theme/ACF JSON/options/menu changes. Strict HEAD gate DEVIATION NOTED (required `6cb0b9df`; actual `f8f652fd` +1 governance commit; D9-J ancestor; local=remote). Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/`. Report: `reports/FP-0002-V9-06D9K-CONTROLLED-MEDIA-UPLOAD-ACF-SEED-REPORT-v1.md`. Next: D9-L admin editor / ACF visibility repair.

## V9-06D9-L admin editor / ACF visibility repair (2026-07-05)

D9-L **PASS**: Installed/activated official Classic Editor 1.7.0; disabled Gutenberg globally (`classic-editor-replace=classic`, `allow-users=disallow`); synced 13 existing ACF field groups from local JSON to DB (`wp acf json sync`) so Home #4 admin metaboxes register. DB checkpoint before writes. No source/theme/ACF JSON/content/media/options/menu changes beyond Classic Editor settings. Frontend regression PASS (19 sections, uploads, routes ALL_200). Authenticated wp-admin screenshots PARTIAL (headless login only). Evidence: `validation/v9-06d9l-admin-editor-acf-visibility-repair/`. Report: `reports/FP-0002-V9-06D9L-ADMIN-EDITOR-ACF-VISIBILITY-REPAIR-REPORT-v1.md`. Next: D9-M native page content cleanup.

## V9-06D9-M native page content cleanup (2026-07-05)

D9-M **PASS**: Cleared obsolete garbled native `post_content` on 13 template-managed pages (Home #4, Services Hub #5, institutional #11–16, Reviews #18, Contacts #20, legal #22–24). DB checkpoint before writes (`v9-06d9m-native-page-content-cleanup-pre-20260705-154624`). No ACF/source/theme/ACF JSON/media/options/menu writes. Frontend regression PASS (19 sections, uploads, routes ALL_200); Home #4 native editor empty; ACF fields intact. Ten pages deferred OPERATOR_REVIEW_REQUIRED (IDs 3, 6–10, 17, 19, 21, 25). Evidence: `validation/v9-06d9m-native-page-content-cleanup/`. Report: `reports/FP-0002-V9-06D9M-NATIVE-PAGE-CONTENT-CLEANUP-REPORT-v1.md`. Next: D9-N hide native editor for template pages.

## V9-06D9-N hide native editor for template-managed pages (2026-07-05)

D9-N **PASS**: Added theme admin UX helper (`inc/admin-editor.php`) to hide native Classic Editor content box on 13 allowlisted template-managed page IDs (D9-M cleaned pages). Retains native editor on operator-review pages (IDs 3, 6–10, 17, 19, 21, 25). No DB/ACF JSON/ACF value/content/media/options/menu writes. Bounded runtime delivery of 2 theme files. Frontend regression PASS (19 sections, uploads, routes ALL_200). Admin policy validation PASS via PHP helper; authenticated wp-admin screenshots PARTIAL (headless login screen). Evidence: `validation/v9-06d9n-hide-native-editor-template-pages/`. Report: `reports/FP-0002-V9-06D9N-HIDE-NATIVE-EDITOR-FOR-TEMPLATE-PAGES-REPORT-v1.md`. Next: D9-O reviews teaser required flag repair.

## V9-06D9-O ACF reviews teaser required flag repair (2026-07-05)

D9-O **PASS**: Confirmed `home_reviews_teaser` optional in canonical JSON and DB (`required=0`, `min=0`). Restored missing runtime `wp-content/acf-json/group_fp02_page_home.json` (D9-H delivery drift). DB checkpoint before reconcile. No Git ACF JSON edit, no ACF value/content/template writes. Frontend regression PASS (routes ALL_200, Home 19/19 sections). Live authenticated wp-admin save not re-tested (PHP CLI unavailable); empty-repeater validation simulated PASS. Evidence: `validation/v9-06d9o-acf-reviews-teaser-required-flag-repair/`. Report: `reports/FP-0002-V9-06D9O-ACF-REVIEWS-TEASER-REQUIRED-FLAG-REPAIR-REPORT-v1.md`. Next: D9-P admin UX QA.

## V9-06D9-P admin UX QA (2026-07-05)

D9-P **PARTIAL PASS**: Read-only admin UX QA after D9-L/M/N/O. Runtime gate PASS (theme shpigovsky, Classic Editor, ACF PRO, runtime JSON, attachments 89–93). Home #4: native editor hidden, ACF populated, `home_reviews_teaser` optional; save simulation PASS; live auth save OPERATOR_CONFIRMATION_REQUIRED. Managed pages #5/#20/#11 PASS; operator-review pages #3/#7/#17/#21 preserved PASS. Frontend regression PASS (7 routes ALL_200, Home 19/19 sections). Admin screenshots PARTIAL. Zero DB/source/ACF JSON/value/content/media/options/menu mutations. Local helpers `_d9p_runner.py` / `_d9p_runner.mjs` used but not committed. Strict HEAD gate PASS (`1ee0efd9`). Evidence: `validation/v9-06d9p-admin-ux-qa/`. Report: `reports/FP-0002-V9-06D9P-ADMIN-UX-QA-REPORT-v1.md`. Next: D9-Q reviews include planning.

## V9-06D9-P git scope drift disclosure (2026-07-05)

Mixed-scope commit `b8361aad`: 28 D9-P allowed paths + 3 OCPilot/SITE-002 paths with OCPilot-only commit message. OCPilot artefacts preserved as valid foreign project documentation; no history rewrite. FP-0002 corrective disclosure: `reports/FP-0002-V9-06D9P-GIT-SCOPE-DRIFT-AUDIT-REPORT-v1.md`; validation: `validation/v9-06d9p-git-scope-drift-audit/`. D9-Q baseline: corrective commit HEAD after this disclosure wave.

## V9-06D9-Q reviews include planning (2026-07-06)

D9-Q **PASS**: Read-only architecture planning. Audited current static Home reviews (`template-parts/home/reviews.php`), optional unwired `home_reviews_teaser`, dormant `group_fp02_page_reviews`, and V9 static authority. Recommended **Hybrid E** — ACF Options shared `reviews_items` on `fp02-site-settings` + shared include + static V9 fallback; deprecate `home_reviews_teaser` on Home admin in D9-R. Frontend smoke PASS (Home reviews 10 slides, routes ALL_200). Zero DB/source/ACF JSON/value/content/media/options/menu/runtime mutations. Strict HEAD gate PASS_WITH_HEAD_NOTE (tip `c188cd2e`, corrective `fae4cd07` ancestor). Evidence: `validation/v9-06d9q-reviews-include-planning/`. Report: `reports/FP-0002-V9-06D9Q-REVIEWS-INCLUDE-PLANNING-REPORT-v1.md`. Next: D9-R shared include source/schema implementation.

## V9-06D9-R reviews shared include implementation (2026-07-06)

D9-R **PASS**: Implemented Hybrid E — `inc/reviews-helpers.php`, shared `reviews-slider.php`, Home wrapper, `/otzyvy/` integration; ACF Options `group_fp02_site_options_reviews`; removed `home_reviews_teaser` from Home group (orphan meta preserved). DB checkpoint `v9-06d9r-reviews-shared-include-pre-20260706-003644`. Runtime delivery + `wp acf json sync` (14 groups). Static V9 fallback 10 slides preserved; routes ALL_200. Zero ACF value/content/media/menu writes. Local helper `_d9r_runner.py` used but not committed. Evidence: `validation/v9-06d9r-reviews-shared-include-implementation/`. Report: `reports/FP-0002-V9-06D9R-REVIEWS-SHARED-INCLUDE-IMPLEMENTATION-REPORT-v1.md`. Prior: D9-S seed below.

## V9-06D9-S controlled reviews options seed (2026-07-06)

D9-S **PARTIAL PASS**: DB checkpoint before seed. Wrote 3 ACF option fields + 10 review rows from static fallback. Home #4 meta unchanged. Frontend source mode remains **FALLBACK** due `field_fp02_reviews_items` collision (runtime subfields `author_label`/`text` vs helper `review_author`/`review_text`). Zero git source/theme/ACF JSON mutations. Evidence: `validation/v9-06d9s-controlled-reviews-options-seed/`. Report: `reports/FP-0002-V9-06D9S-CONTROLLED-REVIEWS-OPTIONS-SEED-REPORT-v1.md`. Repaired in D9-T below.

## V9-06D9-T reviews options key fix + helper normalization (2026-07-06)

D9-T **PASS**: Repaired ACF Options reviews field keys to unique `field_fp02_options_*` namespace; normalized `inc/reviews-helpers.php` for canonical + legacy D9-S subfield names; updated ACF reference meta (3 writes). DB checkpoint `v9-06d9t-reviews-options-key-fix-pre-20260706-010904`. Bounded runtime delivery (helper + ACF JSON) + `acf_import_field_group`. Seeded 10 reviews preserved; frontend source mode **OPTIONS** on Home and `/otzyvy/`; routes ALL_200. Evidence: `validation/v9-06d9t-reviews-options-key-fix-helper-normalization/`. Report: `reports/FP-0002-V9-06D9T-REVIEWS-OPTIONS-KEY-FIX-HELPER-NORMALIZATION-REPORT-v1.md`. Repaired in D9-U below.

## V9-06D9-U reviews admin UX repair (2026-07-06)

D9-U **PASS**: Theme `inc/admin-options.php` registers top-level **Отзывы** (`fp02-reviews`) and suppresses deprecated Home `home_reviews_teaser` (plugin-local field + `RepeaterValidation` max-rows). Canonical `options_*` meta migration for 10 seeded rows (`review_author`, `review_text`, …). `group_fp02_site_options_reviews` location → `fp02-reviews`. DB checkpoint `v9-06d9u-reviews-admin-ux-repair-pre-20260706-013004`. Frontend **OPTIONS** unchanged. Admin screenshots PARTIAL. Local helpers not committed. Evidence: `validation/v9-06d9u-reviews-admin-ux-repair/`. Report: `reports/FP-0002-V9-06D9U-REVIEWS-ADMIN-UX-REPAIR-REPORT-v1.md`. Next: D9-V admin visual QA.

## V9-06D9-V reviews admin + static layout reconciliation audit (2026-07-06)

D9-V **PARTIAL PASS**: Read-only audit reconciling D9-U claims vs operator verification vs static V9 authority. Confirmed: duplicate reviews in Site Settings (stale duplicate `group_fp02_site_options_reviews` DB post); empty **Отзывы** admin fields (helpers read `'option'`, admin screen uses `'fp02-reviews'`); `/otzyvy/` uses Home slider instead of static `reviews-archive` card list (`archive-list.php` still skeleton). Home slider matches static V9 Home. Strict HEAD gate PASS_WITH_HEAD_NOTE (`8a9d6e37`, D9-U ancestor `c3cbee9f`). Zero mutations. Evidence: `validation/v9-06d9v-reviews-admin-static-layout-reconciliation-audit/`. Report: `reports/FP-0002-V9-06D9V-REVIEWS-ADMIN-STATIC-LAYOUT-RECONCILIATION-AUDIT-REPORT-v1.md`. Next: D9-W combined admin + layout repair.

## V9-06D9-W reviews admin + archive layout repair (2026-07-06)

D9-W **PARTIAL PASS**: Combined repair per D9-V findings. Trashed 3 stale duplicate ACF field-group posts (kept ID 286 on `fp02-reviews`). Migrated 166 review option meta keys from `options_reviews_*` to `fp02-reviews_reviews_*`; restored 10 seeded rows from D9-S payload. Theme: `inc/reviews-helpers.php` reads `fp02-reviews` first; `/otzyvy/` archive list + rehabilitation requirements (no Home slider). DB checkpoint `v9-06d9w-reviews-admin-layout-repair-pre-*`. Bounded runtime delivery: 6 theme files. Zero ACF JSON/media/menu/rewrite changes. Frontend OPTIONS (10 items); routes ALL_200. Admin screenshots PARTIAL. Local helpers not committed. Evidence: `validation/v9-06d9w-reviews-admin-and-layout-repair/`. Report: `reports/FP-0002-V9-06D9W-REVIEWS-ADMIN-AND-LAYOUT-REPAIR-REPORT-v1.md`. Next: D9-X admin-to-frontend binding repair.

## V9-06D9-X reviews admin-to-frontend binding repair (2026-07-06)

D9-X **PASS**: Operator edit **Андрей, Москва** found in legacy `options_*` but frontend read stale `fp02-reviews_*` (Александр). DB checkpoint `v9-06d9x-reviews-binding-repair-pre-20260706-023410`. Synced 166 meta keys `options_reviews_*` → `fp02-reviews_reviews_*`. Theme: helper resolved-context tracking; admin explicit `post_id` + `acf/pre_save_post` save guard. Bounded runtime delivery: 2 theme files. Home + `/otzyvy/` first author **Андрей, Москва**; source **OPTIONS**; routes ALL_200; slider/archive layout unchanged. Zero ACF JSON/media/menu/rewrite changes. Admin screenshots PARTIAL. Local helpers not committed. Evidence: `validation/v9-06d9x-reviews-admin-to-frontend-binding-repair/`. Report: `reports/FP-0002-V9-06D9X-REVIEWS-ADMIN-TO-FRONTEND-BINDING-REPAIR-REPORT-v1.md`. Next: D9-Y admin visual QA.

## V9-06D9-Y reviews admin visual QA + closure (2026-07-06)

D9-Y **PASS**: Read-only closure after D9-X and operator manual verification. Captured operator confirmation («Проверил, всё хорошо. давай дальше»). Re-ran frontend route smoke (5 routes ALL_200; Home + `/otzyvy/` first author **Андрей, Москва**; source **OPTIONS**). Frontend screenshots captured (3/3); admin screenshots PARTIAL (auth required). Reviews admin/frontend chain **CLOSED**. Zero DB/source/theme/ACF JSON/runtime mutations. Strict HEAD gate PASS_WITH_HEAD_NOTE (`f125cf38`, D9-X ancestor). Evidence: `validation/v9-06d9y-reviews-admin-visual-qa-closure/`. Report: `reports/FP-0002-V9-06D9Y-REVIEWS-ADMIN-VISUAL-QA-CLOSURE-REPORT-v1.md`. Next: D9-Z WordPress readiness audit.
