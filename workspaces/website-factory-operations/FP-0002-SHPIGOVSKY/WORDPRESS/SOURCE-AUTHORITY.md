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

## V9-06D9-Z WordPress readiness audit (2026-07-06)

D9-Z **PARTIAL PASS**: Holistic read-only readiness audit after D9-L through D9-Y. Runtime/routes/frontend key surfaces **READY**; Reviews chain **CLOSED**; admin/ACF **PARTIAL** (auth-gated admin screenshots; 3 trashed duplicate ACF DB groups harmless); content/legal **NEEDS_OPERATOR_REVIEW** (D9-M deferred IDs 3,6–10,17,19,21,25 + legal templates #22–24). 8/8 key routes HTTP 200; 5 frontend + 3 admin (login gate) screenshots captured. Zero DB/source/theme/ACF JSON/runtime mutations. Strict HEAD gate **PASS** (`00c9db03`). WordPress stable checkpoint **NOT READY**. Evidence: `validation/v9-06d9z-wordpress-readiness-audit/`. Report: `reports/FP-0002-V9-06D9Z-WORDPRESS-READINESS-AUDIT-REPORT-v1.md`. Next: **CREATE_V9_06E0_LEGAL_NATIVE_CONTENT_REVIEW_TASK**.

## V9-06E0 Legal native content review (2026-07-06)

E0 **PASS**: Read-only legal/native content review. Classified 13 pages (IDs 3,6–10,17,19,21–25). Garbled WP privacy seed on ID 3 **CONFIRMED** (draft; SHA256 unchanged from D9-M). WP `wp_page_for_privacy_policy=25` **misaligned** with canonical slug `/privacy-policy/` (ID 3). Legal templates #22–24 **empty** (D9-M cleared); footer links live. No verified Shpigovsky authoritative legal copy in repo (V8/V9 demo only; MARS reference templates partial). 5/5 frontend screenshots PASS; 3/3 admin PARTIAL (login gate). Zero DB/source/theme/ACF JSON/runtime mutations. Strict HEAD gate **PASS_WITH_HEAD_NOTE** (`bbbe7054`, D9-Z ancestor). WordPress stable checkpoint **NOT READY**. Evidence: `validation/v9-06e0-legal-native-content-review/`. Report: `reports/FP-0002-V9-06E0-LEGAL-NATIVE-CONTENT-REVIEW-REPORT-v1.md`. Next: **OPERATOR_DECISION_REQUIRED** → E1 route/privacy repair, clear, authoritative copy seed.

## V9-06E1 Legal static copy seed (2026-07-06)

E1 **PASS**: Operator-authorized static V9 legal copy transfer. Extracted four body partials from `fp-0002-shpigovsky-v9/src/partials/sections/legal/content/`; seeded native `post_content` on pages #3, #22, #23, #24 (exact SHA256 match). Cleared garbled privacy seed on #3; published #3. Updated `wp_page_for_privacy_policy` 25→3. Page #25 preserved. Minimal template render repair: `document-page.php` outputs `the_content()`; `legal.php` V9 shell; `admin-editor.php` unhides #22–24. DB checkpoint `v9-06e1-legal-static-copy-seed-pre-20260706-035240`. Frontend legal routes 4/4 PASS. Admin screenshots PARTIAL (login gate). Zero ACF/menu/rewrite/plugin writes. Strict HEAD gate **PASS_WITH_HEAD_NOTE** (`29336f53`, E0 ancestor). Evidence: `validation/v9-06e1-legal-static-copy-seed/`. Report: `reports/FP-0002-V9-06E1-LEGAL-STATIC-COPY-SEED-REPORT-v1.md`. Superseded next step by E2.

## V9-06E2 Legal layout + menu alignment repair (2026-07-06)

E2 **PASS**: Removed legal width caps (`.legal-document__container` 900px, `.legal-document__body` 820px) in `theme/shpigovsky/assets/css/v9-style.css`; delivered to runtime. Footer legal menu: removed hub #21 item; four canonical legal links only. Primary menu aligned with static V9 (`header.html`): removed Home/Специалисты; added Зависимости; relabeled Лечение и профилактика. Page #21 set to draft (object preserved). Legal native content #3/#22/#23/#24/#25 unchanged. DB checkpoint `v9-06e2-legal-layout-menu-alignment-repair-pre-20260706-041056`. 8/8 screenshots PASS. Zero ACF/privacy/rewrite/plugin writes. Strict HEAD gate **PASS_WITH_HEAD_NOTE** (`b5be3413`, E1 ancestor). Evidence: `validation/v9-06e2-legal-layout-menu-alignment-repair/`. Report: `reports/FP-0002-V9-06E2-LEGAL-LAYOUT-MENU-ALIGNMENT-REPAIR-REPORT-v1.md`. Superseded next step by E3.

## V9-06E3 WordPress stable checkpoint (2026-07-06)

E3 **PASS**: Read-only stable checkpoint. Confirmed local runtime **STABLE_LOCAL** after D9 waves + E0→E2 legal chain. Routes/menus/footer/legal/reviews **READY**; admin **PARTIAL** (auth screenshots); 11 frontend screenshots PASS. Stable checkpoint **DECLARED** at commit `8c935957048c1f9b3d6ae1fee36ac3b5d2fcb222`. Zero DB/source/theme/ACF JSON/runtime mutations. Evidence: `validation/v9-06e3-wordpress-stable-checkpoint/`. Report: `reports/FP-0002-V9-06E3-WORDPRESS-STABLE-CHECKPOINT-REPORT-v1.md`.

## V9-06E4 services layout + shared background visual reconciliation audit (2026-07-06)

E4 **PASS**: Read-only audit substantiating operator post-E3 visual findings. Services hub `/uslugi/` uses wrong `hero--inner` partial (static authority: `services-inner-hero-v2`). Subdivision `/uslugi/zavisimosti/` correct hero type but `hero_media` empty. Shared backgrounds broken by CSS root paths `/assets/...` (404 on WP; assets present in theme). No source/theme/ACF/runtime mutations in E4. Evidence: `validation/v9-06e4-services-layout-shared-bg-visual-reconciliation-audit/`. Report: `reports/FP-0002-V9-06E4-SERVICES-LAYOUT-SHARED-BG-VISUAL-RECONCILIATION-AUDIT-REPORT-v1.md`. Next: **CREATE_V9_06E5_SERVICES_LAYOUT_SHARED_BG_REPAIR_TASK**.

## V9-06E5 services layout + shared background repair (2026-07-06)

E5 **PARTIAL PASS**: Theme source repairs for services hub hero/layout (`services-inner-hero-v2`, `page-uslugi-v2__main`, `services-category-section-v2`, `services-program-v2`), subdivision hero theme fallback (`service-subdivision-hero.webp`), subdivision stack extension (nature/team-stats/shared blocks), and CSS background path repair (`../img/...` in `v9-style.css`). Bounded runtime delivery: 16 theme files. DB writes: 0. Evidence: `validation/v9-06e5-services-layout-shared-bg-repair/`. Report: `reports/FP-0002-V9-06E5-SERVICES-LAYOUT-SHARED-BG-REPAIR-REPORT-v1.md`. Next: **CREATE_V9_06E6_OPERATOR_VISUAL_QA_TASK**.

## V9-06E6 service subdivision main layout repair (2026-07-06)

E6 **PARTIAL PASS**: Scoped repair for `/uslugi/zavisimosti/` main layout — added `page-service-subdivision-v1` body class (CSS scope fix), removed extra article wrapper, aligned dependencies/program/nature/team-stats markup to static V9 authority. Hero image and E5 shared backgrounds preserved. Bounded runtime delivery: 7 theme files. DB writes: 0. Evidence: `validation/v9-06e6-service-subdivision-main-layout-repair/`. Report: `reports/FP-0002-V9-06E6-SERVICE-SUBDIVISION-MAIN-LAYOUT-REPAIR-REPORT-v1.md`. Next: **CREATE_V9_06E7_OPERATOR_VISUAL_QA_TASK**.

## V9-06E7B Hero system finalization + scope reconciliation (2026-07-06)

E7B **PASS**: Finalized uncommitted E7 hero WIP. Theme: `hero-helpers.php` context registry, shared `services-inner-hero-v2` partial, institutional hero, ACF→fallback resolution. Project plugin: `hero_media` + hub/institutional hero fields in `FieldGroups.php` (**ACCEPTED_PROJECT_PLUGIN_SOURCE_CHANGE**). DB checkpoint `v9-06e7b-hero-system-finalization-pre-20260706-185846`. Media seed: attachments 302–305 on objects 4, 5, 73, **74** (alcohol ID corrected from erroneous 77). Runtime delivery: 11 theme + 1 plugin file. Frontend hero routes PASS; admin `hero_media` seeded PASS. Screenshots PARTIAL. Zero legal/reviews/menu/rewrite changes. Temp seed runners not committed. Evidence: `validation/v9-06e7b-hero-system-finalization-scope-reconciliation/`. Report: `reports/FP-0002-V9-06E7B-HERO-SYSTEM-FINALIZATION-SCOPE-RECONCILIATION-REPORT-v1.md`. Next: **CREATE_V9_06E8_OPERATOR_HERO_VISUAL_QA_TASK**.

## V9-06E8 static V9 content + main layout authority repair (2026-07-06)

E8 **PARTIAL PASS**: Static V9 content authority via `inc/v9-static-content.php` + template fallbacks. Services hub `/uslugi/` copy/CTA/program from `uslugi-v2.html`; contacts V9 layout (maps + photo); alcohol leaf full section stack from `usluga-konechnaya-v1.html`. 18 theme files; 0 DB writes; runtime delivered. E3 stable checkpoint invalidated for content parity. DB checkpoint `v9-06e8-static-v9-content-main-layout-authority-repair-pre-20260706-230100`. Evidence: `validation/v9-06e8-static-v9-content-main-layout-authority-repair/`. Report: `reports/FP-0002-V9-06E8-STATIC-V9-CONTENT-MAIN-LAYOUT-AUTHORITY-REPAIR-REPORT-v1.md`. Operator rejected E8 leaf layout gate (probe-only, no screenshots).

## V9-06E9 service leaf static V9 layout parity repair (2026-07-06)

E9 **PASS**: Corrective layout repair for alcohol service leaf. Removed `article.shpigovsky-service` wrapper; restored static V9 subnav anchors; program block uses V9 image fallback items; reviews/final-form section ids aligned. 7 theme files; 0 DB writes; runtime delivered; 14 screenshots captured. Program lorem remains V9 fixture/demo per static authority. Evidence: `validation/v9-06e9-service-leaf-static-v9-layout-parity-repair/`. Report: `reports/FP-0002-V9-06E9-SERVICE-LEAF-STATIC-V9-LAYOUT-PARITY-REPAIR-REPORT-v1.md`. Superseded next step by E10.

## V9-06E10 full backup + WordPress port root cause audit (2026-07-07)

E10 **PASS**: Read-only full backup + forensic root cause audit. No repair. Backup: `X:\AI MARS STORAGE\backups\fp-0002-shpigovsky\v9-06e10-root-cause-pre-audit-20260706-212334\` (theme, "589 files, plugin 20, DB dump 1.4MB, V9 src/dist hashes, 10 screenshots). **Root cause:** WordPress port uses D7-D semantic PHP reconstruction + home partial reuse — not direct static V9 HTML section-stack porting; E9 DOM probe PASS insufficient (section classes match but operator visual drift persists). Created governance contract v1 (10 rules). E3 stable checkpoint **remains invalidated**. Operator PNGs (`вёрстка.png`, `Вордпресс.png`) not in local workspace. 0 DB/source/theme/runtime mutations. HEAD note: E9 `7559f1ac` ancestor; actual `8764185d`. Evidence: `validation/v9-06e10-full-backup-wp-port-root-cause-audit/`. Report: `reports/FP-0002-V9-06E10-FULL-BACKUP-WP-PORT-ROOT-CAUSE-AUDIT-REPORT-v1.md`. Next: **CREATE_V9_06E11_STATIC_TO_WP_PAGE_CONTRACT_INVENTORY_TASK**.

## V9-06E11 static-to-WP page contract inventory (2026-07-07)

E11 **PASS**: Read-only page-by-page contract inventory before repair. **33** static V9 pages (`src/pages/`) + **31** WP routes inventoried with live HTTP/DB probes. Contracts: static-to-WP route mapping, section-stack (class-order + SEMANTIC_REBUILD classification per E10 governance), template provenance (alcohol-stack/leaf-stack BLOCKER/HIGH), content authority (EXACT_V9 vs DEMO vs NATIVE_LEGAL vs ADMIN_DYNAMIC). **16/16** screenshots PASS (static V9 dist + runtime pairs incl. demo subdivisions). Alcohol leaf `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` → **NEEDS_DIRECT_V9_REPLACEMENT** (E12 start). Home/hub/subdivision class stacks MATCH but content SEMANTIC_REBUILD underneath. 0 DB/source/theme/runtime mutations. HEAD note: E10 `a373e3fb` ancestor; actual `6a51da94`. Evidence: `validation/v9-06e11-static-to-wp-page-contract-inventory/`. Report: `reports/FP-0002-V9-06E11-STATIC-TO-WP-PAGE-CONTRACT-INVENTORY-REPORT-v1.md`. Next: **CREATE_V9_06E12_DIRECT_STATIC_PORT_REPAIR_ALCOHOL_LEAF_TASK**.

## V9-06E12 direct static V9 port repair — alcohol leaf (2026-07-07)

E12 **PASS**: Direct static V9 port for alcohol leaf. Replaced semantic ACF orchestration with `alcohol-direct-v9.php` section stack from `usluga-konechnaya-v1.html`. New direct partials: approach (staff image + V9 cards), stages (lead + support + guest CTA), FAQ (10 static V9 items). Hero admin `hero_media` preserved. **6** theme files; **0** DB writes; runtime delivered. **16/16** screenshots PASS; section-stack validation PASS (staff image, stages lead/support, 10 FAQ, program images). Regression routes 9/9 HTTP 200. E3 stable checkpoint **remains invalidated**. Evidence: `validation/v9-06e12-direct-static-v9-port-repair-alcohol-leaf/`. Report: `reports/FP-0002-V9-06E12-DIRECT-STATIC-V9-PORT-REPAIR-ALCOHOL-LEAF-REPORT-v1.md`. Next: **CREATE_V9_06E13_OPERATOR_ALCOHOL_LEAF_VISUAL_QA_TASK**.

## V9-06E13 alcohol leaf specialists block V9 parity repair (2026-07-07)

E13 **PASS**: Targeted repair of `Специалисты центра` on alcohol leaf. Root cause: Swiper vendor enqueued only on `is_front_page()` — slider uninitialized, oversized cards. **Removed** `home/specialists.php` reuse; added `alcohol-direct-v9/specialists.php` + `alcohol-direct-v9-vendors.php` + `shpigovsky_get_v9_specialists_cards()`. **5** theme files; **0** DB writes; runtime delivered. **16/16** screenshots PASS; Swiper JS/CSS confirmed on alcohol leaf. Home specialists unchanged. Evidence: `validation/v9-06e13-alcohol-leaf-specialists-block-v9-parity-repair/`. Report: `reports/FP-0002-V9-06E13-ALCOHOL-LEAF-SPECIALISTS-BLOCK-V9-PARITY-REPAIR-REPORT-v1.md`. Next: **CREATE_V9_06E14_SERVICE_ADMIN_FIELDS_SERVICE_TREE_DEMO_CONTENT_REPAIR**.

## V9-06E14 service admin fields + service tree demo content repair (2026-07-07)

E14 **PASS**: Added ACF field `service_short_description` (`Мини-описание`) for all service CPT objects; hub card text `.services-category-section-v2__service-text` now reads admin field → V9 static → DEMO fallback (grouped + flat modes). Dependencies tree: service **76** `specialistam` under `zavisimosti` **trashed** (canonical page **15** `/o-centre/specialistam/` unaffected); created demo leaves **314–316** (`narkoticheskaya-zavisimost`, `lekarstvennaya-zavisimost`, `povedencheskie-zavisimosti`); `profilakticheskiy-analiz` ordered last. Psych/eating subdivisions **77/84** confirmed `subdivision` layout + DEMO hero/intro seed. **2** theme files + **1** plugin file + **1** ACF JSON; **46** DB writes; DB checkpoint YES; runtime delivered. **10/10** screenshots PASS. Evidence: `validation/v9-06e14-service-admin-fields-service-tree-demo-content-repair/`. Report: `reports/FP-0002-V9-06E14-SERVICE-ADMIN-FIELDS-SERVICE-TREE-DEMO-CONTENT-REPAIR-REPORT-v1.md`. Next: **CREATE_V9_06E15_OPERATOR_SERVICE_TREE_VISUAL_QA_TASK**.

## V9-06E15 service mini-description source + subdivision sliders regression repair (2026-07-07)

E15 **PASS**: Operator E14 partial QA addressed. Root cause (mini-description): E14 EXACT_V9 seeded admin text identical to V9 static — operator perceived HTML source; hardened `shpigovsky_get_service_field` with post_meta fallback + `shpigovsky_resolve_service_mini_description_source`. Root cause (sliders): subdivision stack reuses home specialists/reviews but Swiper gated to home/alcohol only — added `inc/service-subdivision-vendors.php`. **3** theme files; **2** DB writes (restore probe markers); DB checkpoint YES; runtime delivered. Hub grouped **14/14** + flat **17/17** cards ACF_FIELD; `/uslugi/zavisimosti/` Swiper PASS. **11/11** screenshots PASS. Evidence: `validation/v9-06e15-service-mini-description-source-subdivision-sliders-regression-repair/`. Report: `reports/FP-0002-V9-06E15-SERVICE-MINI-DESCRIPTION-SOURCE-SUBDIVISION-SLIDERS-REGRESSION-REPAIR-REPORT-v1.md`. Next: **CREATE_V9_06E16_OPERATOR_SERVICE_TREE_VISUAL_QA_TASK**.

## V9-06E16 operator QA closure + reusable blocks / clone / cleanup architecture audit (2026-07-07)

E16 **PASS**: Documentation-only. Operator closed E15 QA (*«Всё что ты перечислил - я проверил и это ок»*). Pre-change backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e16-pre-admin-architecture-and-cleanup-audit-20260707-223340` (DB dump + snapshots + runtime/ACF hashes). Audited Site Settings IA (`fp02-site-settings` + `fp02-reviews`); inventory 14 reusable blocks; admin architecture + restructure plans; service duplicate design; obsolete pages audit (trash candidates IDs **9**, **21**, **25**; privacy canonical **ID 3** verified). **0** DB writes (dump export only); **0** source/theme/plugin/ACF changes; no page trash. HEAD note: E15 `a8d825b0` ancestor; actual `9c5d9510`. Evidence: `validation/v9-06e16-operator-qa-closure-reusable-blocks-clone-cleanup-audit/`. Report: `reports/FP-0002-V9-06E16-OPERATOR-QA-CLOSURE-REUSABLE-BLOCKS-CLONE-CLEANUP-AUDIT-REPORT-v1.md`. Next: **CREATE_V9_06E17_SITE_SETTINGS_IA_SKELETON_TASK**.

## V9-06E17 site settings IA skeleton (2026-07-07)

E17 **PASS**: Site Settings admin IA skeleton in `shpigovsky-core` — parent redirect, **Общие настройки** (`post_id=option`), **Повторяемые блоки** + 12 skeleton subpages; contacts/modal/CTA groups relocated to general subpage; top-level **Отзывы** unchanged. DB checkpoint `v9-06e17-site-settings-ia-skeleton-pre-20260707-235348`. **2** plugin + **2** ACF JSON; **0** DB writes; runtime delivered. Routes 8/8 PASS. Evidence: `validation/v9-06e17-site-settings-ia-skeleton/`. Report: `reports/FP-0002-V9-06E17-SITE-SETTINGS-IA-SKELETON-REPORT-v1.md`. Next: **CREATE_V9_06E18_REUSABLE_BLOCKS_BATCH_1_FIELDS_TASK**.

## V9-06E18 reusable blocks batch 1 fields (2026-07-08)

E18 **PASS**: Batch 1 reusable block fields — `group_fp02_block_final_form`, `group_fp02_block_specialists`, `group_fp02_block_cta_bands`; reviews alias via dual location + `post_id=fp02-reviews` on block subpage. Theme `inc/reusable-blocks-helpers.php`; renderer migration for final form, specialists (home + alcohol), CTA band defaults. DB checkpoint `v9-06e18-reusable-blocks-batch-1-fields-pre-20260708-001410`; batch 1 option seed only; reviews data preserved. **2** plugin + **7** theme + **4** ACF JSON; runtime delivered. Routes 8/8 PASS; frontend screenshots PASS; admin screenshots PARTIAL. Evidence: `validation/v9-06e18-reusable-blocks-batch-1-fields/`. Report: `reports/FP-0002-V9-06E18-REUSABLE-BLOCKS-BATCH-1-FIELDS-REPORT-v1.md`. Next: **CREATE_V9_06E19_OPERATOR_REUSABLE_BLOCKS_ADMIN_QA_TASK**.

## V9-06E19 reusable blocks admin visibility repair (2026-07-08)

E19 **PASS**: Corrective admin IA repair after operator E18 rejection. Root cause: Batch 1 option subpages registered under `fp02-site-settings-blocks` (WordPress 3rd-level menu — invisible). Fix: Batch 1 `parent_slug` → `fp02-site-settings`; container notice on **Повторяемые блоки**; reviews dual-location DB sync (**1** DB write). **1** plugin file; runtime delivered. Routes 8/8 PASS; ACF probe PASS; admin screenshots PARTIAL. Evidence: `validation/v9-06e19-reusable-blocks-admin-visibility-repair/`. Report: `reports/FP-0002-V9-06E19-REUSABLE-BLOCKS-ADMIN-VISIBILITY-REPAIR-REPORT-v1.md`. Next: **CREATE_V9_06E20_OPERATOR_REUSABLE_BLOCKS_ADMIN_QA_TASK**.

## V9-06E20 remove reviews alias from site settings (2026-07-08)

E20 **PASS**: Operator E19 QA correction — remove duplicate **Отзывы** from **Настройки сайта** (`fp02-block-reviews` alias); preserve top-level **Отзывы** (`fp02-reviews`) and all review data. **1** plugin file (`OptionsPage.php`); **1** ACF JSON (single location); **1** ACF metadata DB write; fresh DB dump checkpoint. Runtime delivered. Routes 7/7 PASS; admin registration probes PASS; admin screenshots PARTIAL. Evidence: `validation/v9-06e20-remove-reviews-alias-from-site-settings/`. Report: `reports/FP-0002-V9-06E20-REMOVE-REVIEWS-ALIAS-FROM-SITE-SETTINGS-REPORT-v1.md`. Next: **CREATE_V9_06E21_REUSABLE_BLOCKS_BATCH_2_FIELDS_TASK**.

## V9-06E21 reusable blocks batch 2 fields (2026-07-08)

E21 **PARTIAL PASS**: Batch 2 reusable block fields — `group_fp02_block_header`, `group_fp02_block_footer`, `group_fp02_block_hero_fallbacks`, `group_fp02_block_comfort`; direct children under **Настройки сайта** (Шапка, Подвал, Герои, Комфорт / преимущества). Renderer migration: header, footer, hero fallbacks, comfort + rehabilitation-requirements. **26** option fields seeded; **2** plugin + **6** theme + **4** ACF JSON (18 total JSON in tree); DB checkpoint `v9-06e21-reusable-blocks-batch-2-fields-pre-20260708-024557`. E20 IA preserved. Routes 9/9 PASS; screenshots PARTIAL. Evidence: `validation/v9-06e21-reusable-blocks-batch-2-fields/`. Report: `reports/FP-0002-V9-06E21-REUSABLE-BLOCKS-BATCH-2-FIELDS-REPORT-v1.md`. Next: **CREATE_V9_06E22_OPERATOR_REUSABLE_BLOCKS_ADMIN_QA_TASK**.

## V9-06E22 remove global heroes settings (2026-07-08)

E22 **PASS**: Operator E21 rejection follow-up — removed global `Герои` from **Настройки сайта** and `group_fp02_block_hero_fallbacks`; restored local/entity hero architecture (E7B `hero_media` + theme registry fallback). Preserved E21 Шапка/Подвал/Комфорт + Batch 1; top-level **Отзывы** unchanged. **2** plugin + **2** theme files; **1** ACF JSON deleted; **1** ACF metadata DB write; DB checkpoint `v9-06e22-remove-global-heroes-settings-pre-20260708-034456`. Runtime delivered. Routes 9/9 PASS; admin screenshots PARTIAL. Evidence: `validation/v9-06e22-remove-global-heroes-settings/`. Report: `reports/FP-0002-V9-06E22-REMOVE-GLOBAL-HEROES-SETTINGS-REPORT-v1.md`. Next: **CREATE_V9_06E24_HERO_CTA_BUTTON_TEXT_PER_ENTITY_TASK**.

## V9-06E24 hero CTA button text per entity (2026-07-08)

E24 **PASS**: Local hero CTA editability — field `hero_cta_label` (**Текст кнопки в hero-блоке**) on `group_fp02_page_home`, `group_fp02_page_services_hub`, `group_fp02_service_layout_hero`, `group_fp02_page_institutional`; helper `shpigovsky_get_local_hero_cta_label()`; **10** postmeta seeds; **1** plugin + **5** theme + **4** ACF JSON; DB checkpoint `v9-06e24-hero-cta-button-text-per-entity-pre-20260707-212945`. No global `Герои`. E22/E21 preserved. Routes 13/13 PASS. Evidence: `validation/v9-06e24-hero-cta-button-text-per-entity/`. Report: `reports/FP-0002-V9-06E24-HERO-CTA-BUTTON-TEXT-PER-ENTITY-REPORT-v1.md`. Next: **CREATE_V9_06E25_OPERATOR_HERO_CTA_QA_TASK**.

## V9-06E24-SYNC resolve remote divergence (2026-07-08)

E24-SYNC **PASS**: After `git fetch`, local and `origin/mars/canonical-post-recovery` already equal at tip `7d5a62da` (contains E24 `bb86fd1e`). No merge, rebase, reset, stash, clean, or force push. Historical operator-reported tip `5bd7d516` is dangling only. Foreign WIP preserved. Evidence: `validation/v9-06e24-sync-resolve-remote-divergence/`. Report: `reports/FP-0002-V9-06E24-SYNC-RESOLVE-REMOTE-DIVERGENCE-REPORT-v1.md`. Next: **CREATE_V9_06E25_OPERATOR_HERO_CTA_QA_TASK**.

## V9-06E24A service structured sections required field polish (2026-07-08)

E24A **PASS**: Operator admin polish — `Программа / условия` resolved to optional `programme_items` (`Пункты программы`) in `group_fp02_service_structured_sections`; explicit optional flags + `validate_optional_programme_items`; ACF JSON resync from PHP; **2** plugin + **1** ACF JSON; DB checkpoint `v9-06e24a-service-structured-sections-required-field-polish-pre-20260708T173446Z`. E24 `hero_cta_label` preserved; no global `Герои`. Routes 10/10 PASS; admin screenshots PARTIAL. Evidence: `validation/v9-06e24a-service-structured-sections-required-field-polish/`. Report: `reports/FP-0002-V9-06E24A-SERVICE-STRUCTURED-SECTIONS-REQUIRED-FIELD-POLISH-REPORT-v1.md`. Next: **CREATE_V9_06E25_SERVICE_DUPLICATE_FEATURE_TASK**.

## V9-06E25 service duplicate feature (2026-07-09)

E25 **PASS**: Admin row action `Дублировать` on `service` CPT — safe draft duplicate via `ServiceDuplicate` module; title suffix ` — копия`; ACF/postmeta + local hero (`hero_cta_label`, `hero_media`) copied by attachment ID reference; structured sections + FAQ copied; duplicate markers `_fp02_duplicated_*` wave `V9-06E25`; **3** plugin files; DB checkpoint `v9-06e25-service-duplicate-feature-pre-20260708T175440Z`; runtime delivered; routes 11/11 PASS; test duplicate draft ID **746** left as validation artifact; admin screenshots PARTIAL. E24/E24A preserved; no global `Герои`. Evidence: `validation/v9-06e25-service-duplicate-feature/`. Report: `reports/FP-0002-V9-06E25-SERVICE-DUPLICATE-FEATURE-REPORT-v1.md`. Operator follow-up: UI not visible in admin — see E25A.

## V9-06E25A service duplicate action visibility repair (2026-07-09)

E25A **PASS**: Corrective repair — dual root cause: (1) hierarchical `service` CPT requires `page_row_actions` not only `post_row_actions`; (2) literal `create_posts` capability blocked UI — fixed via CPT-mapped `user_can_duplicate()`. Added edit-screen side meta box `Дублирование` with button `Дублировать услугу`. E25 `duplicate_service()` copy logic preserved; **2** plugin files; DB checkpoint `v9-06e25a-service-duplicate-action-visibility-repair-pre-20260708T181800Z`; runtime delivered; routes 7/7 PASS; 0 DB writes; draft **746** preserved; admin screenshots 3/3 PASS. Evidence: `validation/v9-06e25a-service-duplicate-action-visibility-repair/`. Report: `reports/FP-0002-V9-06E25A-SERVICE-DUPLICATE-ACTION-VISIBILITY-REPAIR-REPORT-v1.md`. Next: **CREATE_V9_06E25_OPERATOR_SERVICE_DUPLICATE_QA_TASK**.

## V9-06E26 blog and other pages porting architecture audit (2026-07-09)

E26 **PASS**: Read-only architecture audit + implementation plan for `/o-centre/`, `/blog/`, blog singles, and supporting pages. Canonical blog route confirmed **`/blog/`** (not `/articles/`). Content model: standard WP **`post`** (no article CPT). Permalink GAP: runtime `/%postname%/` vs V9 target `/blog/%postname%/`. Templates skeleton-only (`home.php`, `single.php`, institutional hub missing 12 V9 sections). ACF `group_fp02_page_institutional` + `group_fp02_blog_post_article_meta` exist; WPilot metadata planned only. Waves E26A–E26D documented. **0** DB writes; **0** runtime delivery; **0** theme/plugin/ACF JSON changes. Read-only wp-load probe 2026-07-08. Draft **746** mismatch: E25A documented, E26 probe `get_post(746)=null` — verify before E27. Evidence: `validation/v9-06e26-blog-and-other-pages-porting-architecture-audit/`. Report: `reports/FP-0002-V9-06E26-BLOG-AND-OTHER-PAGES-PORTING-ARCHITECTURE-AUDIT-REPORT-v1.md`. Next: **CREATE_V9_06E26A_ABOUT_PAGE_WORDPRESS_ACF_PORT_TASK**.

## V9-06E26A about page WordPress ACF port (2026-07-09)

E26A **PASS**: Full `/o-centre/` hub port — 14-section V9 stack; extended `group_fp02_page_institutional` with hub-only `about_*` fields; 6 institutional partials + reused specialists/reviews/CTA/final-form; page **#11** ACF seed; local hero + `hero_cta_label` preserved; DB checkpoint `v9-06e26a-about-page-wordpress-acf-port-pre-20260709-115450`; bounded runtime delivery (theme + plugin + ACF JSON); regression 9/9 routes HTTP 200. Blog/permalink/global hero/reviews/legal/nav untouched. Evidence: `validation/v9-06e26a-about-page-wordpress-acf-port/`. Report: `reports/FP-0002-V9-06E26A-ABOUT-PAGE-WORDPRESS-ACF-PORT-REPORT-v1.md`. Next: **CREATE_V9_06E26A_OPERATOR_ABOUT_PAGE_QA_TASK**.

## V9-06E26A-POLISH infrastructure g5 decor logo (2026-07-09)

E26A-POLISH **PASS**: Operator QA polish — restored missing `comfort__gallery-item_decor` logo block as first child in `infrastructure-narrative__group--g5` on `/o-centre/`; static V9 reference `comfort-gallery-decor.html`; asset `img/branding/logo.svg` via `shpigovsky_asset_uri()`; **1** theme partial (`infrastructure-narrative.php`); bounded runtime delivery; regression routes HTTP 200. **0** DB writes; **0** ACF JSON changes; **0** plugin changes. Evidence: `validation/v9-06e26a-polish-infrastructure-g5-decor-logo/`. Report: `reports/FP-0002-V9-06E26A-POLISH-INFRASTRUCTURE-G5-DECOR-LOGO-REPORT-v1.md`. Next: **CREATE_V9_06E26B_BLOG_ARCHIVE_WORDPRESS_ACF_PORT_TASK**.

## V9-06E26B blog archive WordPress ACF port (2026-07-09)

E26B **PASS**: Full `/blog/` archive port — V9 section stack (`blog-archive`, lower CTA, expert quote); `group_fp02_blog_archive_settings` on page **#19**; 14 archive settings seeded; permalink `/blog/%postname%/` + rewrite flush; empty state at 0 posts; DB checkpoint `v9-06e26b-blog-archive-wordpress-acf-port-pre-20260709-131602`; bounded runtime delivery (theme + plugin + ACF JSON); regression 9/9 routes HTTP 200. Blog single/WPilot/global hero/reviews/legal/nav untouched; 0 posts created. Evidence: `validation/v9-06e26b-blog-archive-wordpress-acf-port/`. Report: `reports/FP-0002-V9-06E26B-BLOG-ARCHIVE-WORDPRESS-ACF-PORT-REPORT-v1.md`. Next: **CREATE_V9_06E26C_BLOG_SINGLE_TEMPLATE_WORDPRESS_ACF_PORT_TASK**.


E26D **PASS**: Demo blog article seeded — post ID `750` at `/blog/nazvanie-stati/`; archive card + single visual QA PASS; 0 source changes; no WPilot. Evidence: `validation/v9-06e26d-demo-blog-content-and-visual-qa/`. Report: `reports/FP-0002-V9-06E26D-DEMO-BLOG-CONTENT-AND-VISUAL-QA-REPORT-v1.md`. Next: **CREATE_V9_06E26D_OPERATOR_BLOG_VISUAL_QA_TASK**.
E26C **PASS**: Blog single template port — V9 `page-blog-article` stack for standard `post` at `/blog/{slug}/`; extended `group_fp02_blog_post_article_meta` (23 fields); TOC auto from h2/h3; optional conclusion/sources/FAQ/related/CTA; **14** theme files + **1** plugin file + **1** ACF JSON; DB checkpoint `v9-06e26c-blog-single-template-wordpress-acf-port-pre-20260709-134131`; bounded runtime delivery; archive regression PASS; `/blog/nazvanie-stati/` 404 at 0 posts; 0 DB writes; no published content seed. Evidence: `validation/v9-06e26c-blog-single-template-wordpress-acf-port/`. Report: `reports/FP-0002-V9-06E26C-BLOG-SINGLE-TEMPLATE-WORDPRESS-ACF-PORT-REPORT-v1.md`. Next: **CREATE_V9_06E26D_DEMO_BLOG_CONTENT_AND_VISUAL_QA_TASK**.

**Primary authority rule (E10/E11/E12/E13/E14):** Static V9 HTML (`fp-0002-shpigovsky-v9/src/` + `dist/`) is primary layout/copy authority. WordPress must achieve direct section-stack parity — not semantic PHP reconstruction. Hub mini-descriptions: admin field primary; V9 static secondary; DEMO explicit where no V9 page exists. No invented clinical copy.

## V9-06E26D-POLISH (2026-07-09)

- Encoding mojibake audit/fix: default category term repaired (2 DB rows).
- Report: `reports/FP-0002-V9-06E26D-POLISH-ENCODING-MOJIBAKE-AUDIT-AND-FIX-REPORT-v1.md`

## V9-06E27D page service ownership implementation (2026-07-10)

E27D **PASS**: Operator-authorized bounded DB implementation per E27C Option A. Fresh DB checkpoint `v9-06e27d-page-service-ownership-implementation-pre-20260709-183427` before writes. Primary menu item **#301** retargeted in-place via **custom_url_binding** (`_menu_item_type=custom`, `_menu_item_url=/uslugi/zavisimosti/`) — no longer references page **#6**. Legacy shadow pages **#6, #7, #8** moved to Trash via `wp_trash_post()` (not permanently deleted). Service CPT **#73/#77/#84/#74**, protected pages **#3/#4/#19**, demo post **#750** unchanged. **12/12** accepted routes HTTP 200; route ownership confirmed service **#73/#77/#84**. No redirects, permalink changes, rewrite flush, or source/runtime delivery. **4** DB writes (menu meta + 3 trash). Evidence: `validation/v9-06e27d-page-service-ownership-implementation/`. Report: `reports/FP-0002-V9-06E27D-PAGE-SERVICE-OWNERSHIP-IMPLEMENTATION-REPORT-v1.md`. Next: **CREATE_V9_06E28_FINAL_WORDPRESS_READINESS_QA_TASK**.

## V9-06E27C page service ownership decision (2026-07-10)

E27C **PASS**: Read-only ownership decision audit for pages **#6, #7, #8** vs service CPT **#73, #77, #84**. HTTP probes confirm **service CPT owns** all three conflicted subdivision routes (`postid-73/77/84`, `single-service` templates). Legacy pages are shadow DB duplicates (431 B generic copy, 0 ACF). Primary menu item **#301** still links page **#6** while route serves service **#73** — **menu_route_mismatch**. Recommendation: **Option A** — keep service CPT; E27D to retarget menu **#301** then trash pages **#6–#8**; no redirects or rewrite flush needed. Hub page **#5**, protected pages, demo **#750**, service **#73** child tree preserved. **0** DB writes; **0** mutations. Evidence: `validation/v9-06e27c-page-service-ownership-decision/`. Report: `reports/FP-0002-V9-06E27C-PAGE-SERVICE-OWNERSHIP-DECISION-REPORT-v1.md`. Superseded by E27D execution.

## V9-06E27B low-risk obsolete cleanup (2026-07-09)

E27B **PASS**: Operator-authorized Batch A cleanup per E27A plan. Fresh DB checkpoint `v9-06e27b-low-risk-obsolete-cleanup-pre-20260709-171947` before writes. **5** pages moved to Trash via `wp_trash_post()`: IDs **9, 10, 17, 21, 25** (4 publish + 1 draft → trash). Ownership debt pages **6, 7, 8** not touched. Protected **#3, #4, #19**, demo post **#750**, service **#73** unchanged. **10/10** accepted routes HTTP 200; **5/5** candidate routes HTTP 404. No menu/permalink/redirect/rewrite/source/runtime changes. Evidence: `validation/v9-06e27b-low-risk-obsolete-cleanup/`. Report: `reports/FP-0002-V9-06E27B-LOW-RISK-OBSOLETE-CLEANUP-REPORT-v1.md`. Next: **CREATE_V9_06E27C_PAGE_SERVICE_OWNERSHIP_DECISION_TASK** (completed in E27C).

## V9-06E27A obsolete pages cleanup read-only audit (2026-07-09)

E27A **PASS**: Read-only inventory of obsolete/placeholder/orphaned WP objects before final readiness QA. **41** objects audited (23 pages, 1 post, 17 services); **38** routes HTTP-probed; static V9 manifest compared. Batch A trash candidates: page IDs **9, 10, 17, 21, 25**. Ownership debt (operator decision): pages **6, 7, 8** vs service CPT at same paths; Primary menu still references page **#6**. Demo post **#750** classified **KEEP_DEMO_LOCAL**. E25 duplicate draft **#746** not present in current DB. **0** DB writes; **0** runtime/source mutations; **0** cleanup executed. Evidence: `validation/v9-06e27a-obsolete-pages-cleanup-read-only-audit/`. Report: `reports/FP-0002-V9-06E27A-OBSOLETE-PAGES-CLEANUP-READ-ONLY-AUDIT-REPORT-v1.md`. Superseded by E27B execution.


## V9-06E28 final WordPress readiness QA (2026-07-09)

E28 **COMPLETE (PASS / GO_WITH_MINOR_POLISH)**: Read-only final local WordPress readiness QA after E26A–E27D. 35 routes inventoried; 12 core accepted routes HTTP 200; menu `#301` → `/uslugi/zavisimosti/`; DB trash/options/objects validated; ACF/admin PARTIAL (o-centre institutional fields empty in DB, page renders); template/source/runtime PASS; frontend smoke PASS; forms NOT_SENT_BY_POLICY; blog/services/legal/trash/security PASS. Zero DB/source/runtime mutations. HEAD note: `84dd9b07` (+1 ahead of remote; baseline `60291b8e` ancestor). Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/`. Report: `reports/FP-0002-V9-06E28-FINAL-WORDPRESS-READINESS-QA-REPORT-v1.md`. Next: **CREATE_V9_06E29_OPERATOR_VISUAL_POLISH_TASK**.

E29A **PASS**: Read-only decision audit for five institutional child placeholder pages (#12–16) and `/o-centre/` page #11 admin parity. Remote artifact baseline @ `49ffdafe`. Placeholders exist for V9 manifest PLACEHOLDER IA + footer links; classification KEEP_PLACEHOLDER_FOR_LATER_PORT (E29C). Hub public PASS; admin PARTIAL at audit time — E26A `about_*` seeded (supersedes E28 legacy `institutional_*` empty probe); gaps identified: hero_media, founder/clinic static partials, shared block admin UX, lorem in about_program, child page content model. Zero DB/source/runtime mutations in E29A. Evidence: `validation/v9-06e29a-placeholder-pages-and-ocentre-admin-parity-decision-audit/`. Report: `reports/FP-0002-V9-06E29A-PLACEHOLDER-PAGES-AND-OCENTRE-ADMIN-PARITY-DECISION-AUDIT-REPORT-v1.md`.

E29B **PASS**: Bounded admin parity implementation for `/o-centre/` page #11 @ `ee6c8d8b`. First preserved on safety branch `safety/fp-0002-e29b-local-ee6c8d8b` during canonical divergence; integrated via V9-06E29B-R2 reconciliation. Full site backup + DB checkpoint pre-write. Seeded `hero_media` (attachment 753), founder quote fields, clinic landscape image; added ACF field definitions + template bindings (`institutional/founder-quote.php`, `institutional/clinic-landscape.php`); shared-block admin note on page #11. **6** theme/plugin source files + **1** ACF JSON; page #11 postmeta writes only; runtime delivered. `about_program_*` lorem unchanged (V9 authority also lorem — operator decision). Placeholders #12–16 preserved. Frontend + regression routes PASS. Evidence: `validation/v9-06e29b-ocentre-admin-parity-implementation/`. Report: `reports/FP-0002-V9-06E29B-OCENTRE-ADMIN-PARITY-IMPLEMENTATION-REPORT-v1.md`. Next: **CREATE_V9_06E29B_OPERATOR_OCENTRE_ADMIN_QA_TASK**.

E29B-FIX **PASS**: Admin UI field visibility repair for page #11. Root cause: stale ACF DB/JSON out of sync with `FieldGroups.php` (operator edit screen showed only hero + empty repeaters). Fix: export canonical group from PHP, reset-import ACF DB, sync source/runtime JSON; add hub overview + CTA/shared guidance messages; hide unused `institutional_content_sections` / `institutional_stages` on page #11. **2** source files (`FieldGroups.php`, `group_fp02_page_institutional.json`); runtime delivered; **0** page #11 postmeta writes; frontend parity PASS. Evidence: `validation/v9-06e29b-fix-ocentre-admin-ui-field-visibility/`. Report: `reports/FP-0002-V9-06E29B-FIX-OCENTRE-ADMIN-UI-FIELD-VISIBILITY-REPORT-v1.md`. Next: **CREATE_V9_06E29B_OPERATOR_OCENTRE_ADMIN_RECHECK_TASK**.

E29B-FIX2C **PARTIAL PASS**: ACF location rule repair + duplicate group cleanup. Root cause: invalid field conditional logic (`param: page`) hid hub `about_*` fields on page #11; **9** duplicate `group_fp02_page_institutional` DB rows polluted admin. Fix: split into `group_fp02_page_ocentre_hub` (page #11) and `group_fp02_page_institutional_child` (pages #12–16) with supported location rules; retire legacy group; DB cleanup + import. **3** source files (`FieldGroups.php`, hub/child ACF JSON); runtime delivered; **0** page #11 postmeta writes; frontend parity PASS; admin API PASS + HTML label evidence; operator screenshot recheck required. Evidence: `validation/v9-06e29b-fix2c-acf-location-rule-repair/`. Report: `reports/FP-0002-V9-06E29B-FIX2C-ACF-LOCATION-RULE-REPAIR-REPORT-v1.md`. Next: **CREATE_V9_06E29B_OPERATOR_OCENTRE_ADMIN_RECHECK_TASK**.

E29C **PASS**: Excel `Структура` structure completion + generic interim pages + favicon. Pre-write backup `v9-06e29c-structure-completion-pre-20260710T133633Z`. Added `page-templates/generic.php`, favicon pack + `inc/favicon.php`, depth-3 service permalink resolver; reconciled 41 Excel routes (HTTP 200); migrated o-centre children #12–16 to generic template; created `/o-centre/intervyu-i-smi/`, `/specyalisty/*`, deep service placeholders, `/uslugi/genotipirovanie/`; site icon attachment **1040**. **7** theme + **2** plugin source files; runtime delivered; **47** DB writes. Evidence: `validation/v9-06e29c-excel-structure-completion/`. Report: `reports/REPORT-FP-0002-V9-06E29C-excel-structure-completion-generic-pages-favicon.md`. Next: **CREATE_V9_06E29_FINAL_WORDPRESS_READINESS_GATE_TASK**.

## V9-06E30 services catalog child services + listing controls (2026-07-12)

E30 **PASS**: `/uslugi/` catalog hierarchy/display controls. Pre-write backup `v9-06e30-services-catalog-before-20260712-213642` (DB dump + theme/plugin/acf hashes). ACF fields `service_show_in_text_list`, `service_show_in_slider`, `service_slider_image` on `group_fp02_service_layout_hero`. Render: automatic markers from loop index; genotyping last via `menu_order=200`; clickable service names; CPT child inline wrap menus; gallery cards from slider-flagged services. Created 6 slider services (IDs 1046–1051). Operator runtime CSS preserved — CSS patched on runtime then synced runtime→source. Evidence: `validation/v9-06e30-services-catalog-child-services-listing-controls/`. Report: `REPORTS/REPORT-FP-0002-V9-06E30-services-catalog-child-services-listing-controls.md`. Next: **OPERATOR_REVIEW_REQUIRED**.

## V9-06E31 program pages + direction links + validation relax (2026-07-12)

E31 **PASS**: Program pages under `/o-centre/programma-lecheniya/` (`genotipirovanie`, `neyropsihologicheskaya-korrektsiya`, `psihokorrektsiya`, `kinezioterapiya`) as generic/pustyshka pages; Home rehabilitation direction links; service admin validation relax. Evidence: `validation/v9-06e31-program-pages-direction-links-validation-relax/`. Report: `REPORTS/REPORT-FP-0002-V9-06E31-program-pages-direction-links-validation-relax.md`. Local only — not production.

## V9-06E32 Home services accordion + Home gallery service links + placeholder (2026-07-13)

E32 **PASS**: Home accordion from service CPT tree; Home gallery as depth-1 service link slides; `service_show_on_home_gallery` admin flag (separate from `/uslugi/` `service_show_in_slider`); neutral `assets/images/service-placeholder.svg` fallback via `shpigovsky_get_service_image_or_placeholder()`. Retired broken Home ACF `home_service_nav_items` (PHP/JSON + DB field trash). Pre-write backup `v9-06e32-home-services-gallery-before-20260713-003442`. Operator runtime CSS preserved (preflight MATCH; additive CSS only). Git commit skipped (remote/HEAD mismatch + foreign WIP). Evidence: `validation/v9-06e32-home-services-accordion-gallery-placeholder/`. Report: `REPORTS/REPORT-FP-0002-V9-06E32-home-services-accordion-gallery-service-placeholder.md`. Next: **OPERATOR_REVIEW_REQUIRED**.

## V9-06E33 service image admin binding + `/uslugi/` slider (2026-07-13)

E33 **PASS**: Service image admin binding + placeholder fix + `/uslugi/` category slider. Report: `REPORTS/REPORT-FP-0002-V9-06E33-service-image-admin-binding-placeholder-uslugi-slider.md`. Local only.

## V9-06E33-FIX01 `/uslugi/` sliders match Home gallery (2026-07-13)

E33-FIX01 **PASS**: `/uslugi/` category sliders use Swiper pagination dots like Home gallery; no prev/next. Report: `REPORTS/REPORT-FP-0002-V9-06E33-FIX01-uslugi-sliders-match-home-gallery.md`. Local only.

## V9-06E34 specialists child pages + automatic slider (2026-07-13)

E34 **PASS**: Unique specialists from prior slider (4; Sergey duplicate removed) → child pages under `/specyalisty/` #1030 with `page-templates/generic.php`. Reused #1031–1033; created #1097 `shapiguzova`. Slider `shpigovsky_get_specialists_cards()` now queries published children (`menu_order`, title); card links to child permalinks; ACF `specialists_items` repeater retired from admin/render (message notice). Featured images sideloaded from theme assets. Pre-write backup `v9-06e34-specialists-pages-slider-before-20260713-020509`. Operator runtime CSS preserved (additive `.specialists__card-link` only). Git commit skipped (remote/HEAD mismatch + foreign WIP). Evidence: `validation/v9-06e34-specialists-child-pages-auto-slider/`. Report: `REPORTS/REPORT-FP-0002-V9-06E34-specialists-child-pages-auto-slider.md`. Next: **OPERATOR_REVIEW_REQUIRED**.

## V9-06E35 specialist no-photo + demo posts + Home articles (2026-07-13)

E35 **PASS** (local runtime): specialist no-photo placeholder; five demo blog posts; Home articles slider from real WP posts (dots / no prev-next). Runtime/DB content; source helpers under theme `blog-helpers` / `home` articles teaser. Local only — not production.

## V9-06E35-FIX01 alcohol article thematic image restore (2026-07-13)

E35-FIX01 **PASS**: post `#750` `/blog/nazvanie-stati/` featured image restored to Media Library attachment `#1106` (`article-alcohol-dependence.webp`). DB/media only for the fix; E35 demos keep blog no-photo. Report: `REPORTS/REPORT-FP-0002-V9-06E35-FIX01-alcohol-article-image-restore.md`. Local only.

## V9-06E29C–E35-FIX01 selective persistence (2026-07-13)

Selective Git persistence of accepted local WordPress source authority (theme/plugin/ACF + E29C–E35-FIX01 reports + small evidence). Prefer temp-worktree commit on branch `fp0002/v9-06e29c-e35-fix01-persistence-*` from local HEAD — **no push**, no main-worktree cleanup, foreign WIP preserved. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e29c-e35-fix01-persistence-before-20260713-032549\`. Export: `X:\AI MARS STORAGE\exports\fp-0002-shpigovsky-persistence\v9-06e29c-e35-fix01-20260713-032549\`. Report: `REPORTS/REPORT-FP-0002-V9-06E29C-E35-FIX01-selective-persistence.md`. **Not** a production deployment claim.

## V9-06E36 Home recovery life mobile (2026-07-13)

E36 **PASS** (local runtime, CSS-only): `.home-recovery-life` stages stack on mobile; no overflow at 360/390/430; decorative `::before` adapted (≤1310 opacity 0.28; ≤1024 0.22; ≤767 0.16); desktop contain/center/0.4 preserved. `recovery-life.php` unchanged. Report: `REPORTS/REPORT-FP-0002-V9-06E36-home-recovery-life-mobile.md`.

## V9-06E37 Home rehabilitation program direction mobile (2026-07-13)

E37 **PASS** (local runtime, CSS-only): `.home-rehabilitation-program__direction` column stack ≤767; image full-width `max-height:200px`; tighter padding; title `overflow-wrap`; «Подробнее» min-height 44px; desktop row preserved; E31 direction links preserved. `rehabilitation-program.php` unchanged. Report: `REPORTS/REPORT-FP-0002-V9-06E37-home-rehabilitation-program-direction-mobile.md`.

## V9-06E36–E37 selective persistence (2026-07-13)

Selective Git persistence of E36/E37 CSS-only mobile polish + stage reports + this status note. Temp-worktree commit chained from prior tip `f77ee7eb…` on branch `fp0002/v9-06e36-e37-mobile-polish-persistence-20260713-042025` — product commit `e8dc63da…`, annotate tip `5b4c0e04…` — **no push**, no main-worktree cleanup, foreign WIP preserved. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e36-e37-persistence-before-20260713-042025\`. Export: `X:\AI MARS STORAGE\exports\fp-0002-shpigovsky-persistence\v9-06e36-e37-20260713-042025\`. Report: `REPORTS/REPORT-FP-0002-V9-06E36-E37-selective-persistence.md`. **Not** a production deployment claim.

## V9-06E39 Home admin order + localization foundation (2026-07-14)

E39 **PASS** (local; Git commit skipped): Home ACF group `group_fp02_page_home` admin field order aligned to `front-page.php` Home partial sequence; Russian source strings wrapped with `__()` / text domain `shpigovsky-core`; plugin `load_plugin_textdomain` added; theme text domain already present (`shpigovsky` + `languages/shpigovsky.pot` foundation). ACF JSON + runtime plugin/JSON synced for Home. DB publish Home group `#639` field order/labels updated (duplicates trashed). Frontend Home preserved (20/20 section order; HTTP 200). No hosting/preview. Report: `REPORTS/REPORT-FP-0002-V9-06E39-home-admin-order-localization.md`. Evidence: `REPORTS/evidence/v9-06e39-*.csv`. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e39-home-admin-order-localization-before-20260714-001557\`.

## V9-06E40 Home admin editable blocks expansion (2026-07-14)

E40 **PASS** (local; Git commit skipped): Home ACF/admin expanded for frontend-canon blocks — recovery intro benefits repeater + toggle; treatment heading/lead; gallery display mode (`all`/`random`/`selected`, default random 12); why-us; staff + clinic landscape Media Library images; recovery-life content/stages; genotyping Home block; videos from Media Library repeater + toggle. Frontend partials/helpers render from ACF with static fallbacks. Home ACF DB publish group now `#1244` (55 fields); stale `#639`/`#1153` trashed. Source↔runtime hash match for changed plugin/theme/ACF JSON. Operator `v9-style.css` preserved. No hosting/preview. Report: `REPORTS/REPORT-FP-0002-V9-06E40-home-admin-editable-blocks-expansion.md`. Evidence: `REPORTS/evidence/v9-06e40-*.csv`. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e40-home-admin-editable-blocks-before-20260714-010957\`.

## V9-06E41 Home admin hero slider / toggles / recovery life (2026-07-14)

E41 **PASS** (local; Git commit skipped): Home admin section/block titles ~20px via scoped `.fp02-acf-section-title` + `admin-home-acf.css` (front page edit only); Hero frontend Swiper from `home_hero_slides` (2nd slide «Шпиговский дом 2» visible) with autoplay/arrows/dots settings; standalone `hero_media` retired/hidden (meta kept); Home visibility toggles for automated/external blocks (founder quote, treatment, gallery, reviews, rehab requirements/program, comfort, specialists, articles); recovery-life stage outer/inner markup + red month labels (`stage_label`, seeded 1–3 месяц). Home ACF DB publish group now `#1338` (70 top-level fields); stale `#1244` trashed. Source↔runtime hash match for changed deliverables. Operator CSS preserved (additive hero/recovery-life rules). No hosting/preview. Report: `REPORTS/REPORT-FP-0002-V9-06E41-home-admin-hero-toggles-recovery-life.md`. Evidence: `REPORTS/evidence/v9-06e41-*.csv`. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e41-home-admin-hero-toggles-recovery-life-before-20260714-015935\`.

## V9-06E41-FIX01 Hero height + rehab program intro (2026-07-14)

E41-FIX01 **PASS** (local; Git commit skipped): Multi-slide hero height restored — root cause was `.hero--home-slider { height:100% }` on the same element overriding `.hero--home { height:70vh }`; measured desktop height 620px at 1440×900 (responsive max-height). Home ACF fields `home_rehabilitation_program_head|lead|intro_1|intro_2` added, seeded from frontend, rendered with fallbacks; direction cards remain automatic. Admin notice HTML: phrase «из страниц программы лечения» bold/red with link to program page edit `#13`. Home group `#1338` now 74 top-level fields. Source↔runtime hash match. Operator CSS preserved (additive FIX01 rules). No hosting/preview. Report: `REPORTS/REPORT-FP-0002-V9-06E41-FIX01-hero-height-rehab-program-intro.md`. Evidence: `REPORTS/evidence/v9-06e41-fix01-*.csv`. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e41-fix01-hero-height-rehab-intro-before-20260714-024847\`.

## V9-06E42 Home freeze accepted (2026-07-14)

E42 **PASS** (local; Git commit skipped; **0 DB writes**; **no WordPress product changes**): Operator accepted Home as finished. Full freeze backup of runtime DB/theme/plugin/ACF JSON/uploads + inventories + Home snapshot + route smoke. Home admin/frontend validation PASS. Architecture model `DOCS/HOME-PAGE-ADMIN-PARITY-MODEL-v1.md`; freeze marker `REPORTS/FREEZE-FP-0002-V9-06E42-HOME-ACCEPTED.md`. **Home admin parity accepted/frozen** pending explicit change request. **Next planned scope:** page-type rollout (not Home product edits). Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e42-home-freeze-accepted-before-next-page-types-20260714-033407\`. Evidence: `X:\AI MARS STORAGE\exports\fp-0002-shpigovsky-home-freeze\v9-06e42-home-freeze-20260714-033407\`. Report: `REPORTS/REPORT-FP-0002-V9-06E42-home-freeze-admin-parity-summary.md`. E38–E41-FIX01 still eligible for a separate selective persistence charter.

## V9-06E43 Services hub admin parity (2026-07-14)

E43 **PASS** (local; Git commit skipped): Applied Home admin-parity model to Services hub `/uslugi/` (page #5, template `page-templates/services-hub.php`). Canonical ACF group `group_fp02_page_services_hub` publish `#1628` (38 fields, title «Страница — Услуги (хаб)»); duplicate groups `#175/#516/#610/#668` trashed. Local hero slider `services_hero_slides` preserves `services-inner-hero-v2` design (not Home hero); seeded first slide from current hero (media `#303`); multi-slide Swiper + autoplay/arrows/dots; one-slide hides nav. Non-repeated program/FAQ/secondary CTA editable; automated catalog/nav/founder/comfort/final-form controlled by toggles + RU/i18n notices with CPT/program links. Home freeze untouched (`#1338`, 74 fields). Operator `v9-style.css` preserved (additive E43 hero slider rules only). Source↔runtime hash match for changed PHP/JS/admin CSS/plugin; JSON exported. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e43-services-hub-admin-parity-before-20260714-040826\`. Report: `REPORTS/REPORT-FP-0002-V9-06E43-services-hub-admin-parity.md`. Model: `DOCS/SERVICES-HUB-ADMIN-PARITY-MODEL-v1.md`. Evidence: `REPORTS/evidence/v9-06e43-*.csv`. No hosting/preview.

## V9-06E43-FIX01 Services category intro/lead fields (2026-07-14)

E43-FIX01 **PASS** (local; Git commit skipped): `/uslugi/` category sections now use root service `service_short_description` (Мини-описание) for `.services-category-section-v2__intro` and new `service_category_section_lead` for `.services-category-section-v2__lead` (ACF conditional on `service_layout_variant == subdivision`). Roots `#73/#77/#84` seeded from prior V9 hardcoded intro/lead; frontend text identical. Helpers: `shpigovsky_resolve_services_hub_category_intro()` / `shpigovsky_resolve_services_hub_category_lead()` with V9/legacy fallback only when empty. Home freeze untouched (74 fields). Operator CSS untouched vs pre-backup. Source/runtime hash match for changed PHP/plugin/ACF JSON. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e43-fix01-services-category-intro-lead-before-20260714-044434\`. Report: `REPORTS/REPORT-FP-0002-V9-06E43-FIX01-services-category-intro-lead-fields.md`. Evidence: `REPORTS/evidence/v9-06e43-fix01-*.csv`.

## V9-06E44 Services hub freeze + layout variant governance (2026-07-14)

E44 **PASS** (local; Git commit skipped): Operator-accepted `/uslugi/` frozen (DB dump + theme/plugin/ACF JSON/uploads manifest + page/group/root exports + snapshot + route smoke). Layout audit of `service_layout_variant`: internal values kept; frontend-significant = `subdivision` + `alcohol_special`; `standard`/`extended`/`placeholder` map to leaf. Inventory 29 services; notable mismatches mid-sections `#314/#316` still `placeholder` (no auto-migrate). Safe admin help block + nesting mismatch warnings + clearer RU instructions; no selector removal; no value migration. Recommended **Option B**. Home freeze untouched (`#1338`, 74 fields). Operator `v9-style.css` untouched vs freeze backup. Source↔runtime hash match for E44 delivery files. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e44-services-hub-freeze-before-layout-governance-20260714-051559\`. Freeze: `REPORTS/FREEZE-FP-0002-V9-06E44-SERVICES-HUB-ACCEPTED.md`. Governance: `DOCS/SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md`. Report: `REPORTS/REPORT-FP-0002-V9-06E44-services-freeze-layout-variant-governance.md`.

## V9-06E45 Service layout Option B implementation (2026-07-14)

E45 **PASS** (local; Git commit skipped): Implemented Option B — editor-facing `service_editor_role` (Раздел услуг / Услуга / Заглушка), `service_layout_override_enabled`, reframed `service_layout_variant` as advanced «Технический шаблон». Module `ServiceLayoutGovernance` (save sync when override off; role warnings; list column). Seeded all 29 services: 3 section / 8 service / 18 placeholder; override only on alcohol `#74`; **0** mass technical layout writes; `#314/#316` mismatch preserved with warnings. Conditional: `service_category_section_lead` shows for role `section` OR layout `subdivision`. Frontend routes 200; helpers preserve subdivision / alcohol-special / leaf. Home freeze untouched (`#1338`, 74 fields). Operator `v9-style.css` unchanged vs E45 pre-backup. Source↔runtime hash match for E45 deliverables. DB writes: 30 (role+override metas). Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e45-service-layout-variant-implementation-before-20260714-163201\`. Report: `REPORTS/REPORT-FP-0002-V9-06E45-service-layout-variant-implementation.md`. Evidence: `REPORTS/evidence/v9-06e45-*.csv`. Governance updated: `DOCS/SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md`.

## V9-06E45-FIX01 Service layout model + child services (2026-07-14)

E45-FIX01 **PASS** (local; Git commit skipped): Operator two-type model — editor choices `section` (Раздел) / `service` (Услуга) only; `placeholder` demoted from primary UI. Override-off mapping: section→`subdivision`, service→`alcohol_special` (general service frontend stack). Effective resolver updated; alcohol V9 static copy gated to known alcohol `#74`. Child services tile block (`child-services.php` + CSS + ACF toggle/heading) before FAQ when published children exist. Seeded 29 services: roots `#73/#77/#84` section/subdivision; all other real services → service/alcohol_special/override off (incl. `#74`, `#314`, `#316`). Home freeze untouched; hub visual restored (child CSS scoped to `service` singular). Operator `v9-style.css` hash unchanged vs FIX01 backup. Source↔runtime match for FIX01 deliverables. DB field writes: role 18 + layout 25 + override 1 + child_enabled 26. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e45-fix01-service-layout-model-before-20260714-180233\`. Report: `REPORTS/REPORT-FP-0002-V9-06E45-FIX01-service-layout-model-and-child-services.md`. Evidence: `REPORTS/evidence/v9-06e45-fix01-*.csv`. Governance: `DOCS/SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md`.

## V9-06E45-FIX02 Rename alcohol_special → service_general (2026-07-14)

E45-FIX02 **PASS** (local; Git commit skipped): Technical layout rename — active value `service_general` (label «Услуга») replaces `alcohol_special` as the general service frontend stack. ACF choices no longer offer `alcohol_special`; resolver + validation + save sync keep it as legacy alias → `service-general`. Migrated 26 service `service_layout_variant` rows (`alcohol_special`→`service_general`); after=0 leftover. `#74` remains role service / override off / layout service_general; alcohol static V9 copy still gated by page ID/slug. Frontend routes 200; hub snapshot bytes unchanged; Home freeze untouched. Operator runtime `v9-style.css` hash matches FIX02 backup. Source↔runtime hash match for FIX02 deliverables. DB writes: 26 layout meta. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e45-fix02-rename-alcohol-special-before-20260714-183309\`. Report: `REPORTS/REPORT-FP-0002-V9-06E45-FIX02-rename-alcohol-special-layout.md`. Evidence: `REPORTS/evidence/v9-06e45-fix02-*.csv`. Governance: `DOCS/SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md`.

## V9-06E45-FIX03 Service layout selector simplification by depth (2026-07-14)

E45-FIX03 **PASS** (local; Git commit skipped): Depth-based one-block admin UX — first-level `Макет страницы услуги` (Раздел/Услуга); nested auto «Услуга» notice; `service_layout_override_enabled` + technical `service_layout_variant` + advanced heading hidden via `acf/prepare_field` (+ CSS). Helpers: `shpigovsky_get_service_depth()`; resolver forces nested → `service-general`. Data sync: 3 first-level sections kept; 26 nested forced service/service_general; notable correction `#74` mistaken section/subdivision → service/service_general. Home freeze untouched; `/uslugi/` whitespace-normalized equal to before snapshot. Operator `v9-style.css` unchanged. Source↔runtime hash match. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e45-fix03-service-layout-selector-simplification-before-20260714-202448\`. Report: `REPORTS/REPORT-FP-0002-V9-06E45-FIX03-service-layout-selector-simplification.md`. Evidence: `REPORTS/evidence/v9-06e45-fix03-*.csv`. Governance: `DOCS/SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md`.

## V9-06E47 Service general (Услуга) admin parity — Alcohol (2026-07-15)

E47 **PASS** (local; Git commit skipped): Started Услуга admin parity model for base `#74` Лечение алкогольной зависимости (`service_general`). New ACF group `group_fp02_service_general_parity` («Услуга — блоки страницы», 64 fields, FE order 1–18); helpers `service-general-helpers.php`; alcohol PHP static demos seeded into ACF; images `service_general_team_image`/`clinic_landscape`/`corridor` seeded `#1238/#1239/#1709`; opposite Раздел group filtered out by role via `acf/load_field_groups`; `#314/#78` image-only seed + specialists OFF preserve; FE reads ACF as normal SoT (emergency PHP/theme only). Home/`/uslugi/` freeze untouched; section model regression-free; operator runtime `v9-style.css` hash preserved (`C858903F…`). Source↔runtime hash match for delivered files. DB writes: 34 field seeds. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e47-service-general-admin-parity-alcohol-before-20260715-114038\`. Report: `REPORTS/REPORT-FP-0002-V9-06E47-service-general-admin-parity-alcohol.md`. Model: `DOCS/SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md`.

## V9-06E47-FIX01 Service general admin UX cleanup + legacy group separation (2026-07-15)

E47-FIX01 **PASS** (local; Git commit skipped): Cleaned Услуга admin UX for `#74` to Layout→Hero→«Услуга — блоки страницы». Extended `filter_service_parity_groups_by_role` to hide Structured Sections / FAQ / Relationships (and opposite Раздел) when `service_editor_role=service`; renamed layout group title to «Макет страницы услуги»; mirrored mid-cta `cta_*` into parity (meta keys preserved; no duplicate UI); soft-disabled 6 DB duplicate legacy ACF field-group posts. Alcohol and `/uslugi/` whitespace-normalized equal to FIX01 backup; Home residual = gallery random card order only (config untouched); `#73` Раздел model preserved (Structured kept for section CTA). Operator `v9-style.css` hash match. Source↔runtime hash match for FIX01 deliverables. DB writes: 6 (soft-disable). Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e47-fix01-service-general-admin-ux-cleanup-before-20260715-125222\`. Report: `REPORTS/REPORT-FP-0002-V9-06E47-FIX01-service-general-admin-ux-cleanup.md`. Evidence: `REPORTS/evidence/v9-06e47-fix01-*.csv`. Model: `DOCS/SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md`.

## V9-06E47-FIX02 Service general ACF render + metabox cleanup (2026-07-15)

E47-FIX02 **PASS** (local; Git commit skipped): Fixed «Услуга — блоки страницы» empty/non-rendering body on nested services (`#74` depth=2). Root cause: FIX03 `prepare_editor_role_field` converts `service_editor_role` to message/empty name for nested pages, while all 68 parity fields still used field-level `when_service` conditionals on that controller — ACF JS hid every field. Fix: `ServiceGeneralParity::when_service()` returns `0`; group-level role filter remains visibility SoT; synced ACF JSON. Also hide `revisionsdiv` / `postexcerpt` on service CPT via `EditorRestrictions`. Frontend alcohol/`/uslugi/` whitespace-normalized equal; Home gallery residual only; `#73` section model preserved; operator `v9-style.css` hash `C858903F…` preserved. Source↔runtime hash match. DB writes: 0. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e47-fix02-service-general-acf-render-before-20260715-133411\`. Report: `REPORTS/REPORT-FP-0002-V9-06E47-FIX02-service-general-acf-render.md`. Evidence: `REPORTS/evidence/v9-06e47-fix02-*.csv`. Model: `DOCS/SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md`.

## V9-06E47-FIX03 Service signs editorial read-more (2026-07-15)

E47-FIX03 **PASS** (local; Git commit skipped): Frontend enhancement for `service_general_signs_editorial` on service general signs block. `signs.php` read-more is a real button (`aria-controls`/`aria-expanded`, initially `hidden`); scoped CSS 5-line clamp via `--signs-editorial-clamp-height`; `v9-shell.js` `initServiceSignsReadMore` measures `scrollHeight` vs `lineHeight×5`, shows button only on overflow, smooth expands then hides button. Re-sync on fonts.ready/load/debounced resize. No admin field changes; DB writes 0; Media 0. Source↔runtime match for PHP/JS; operator `v9-style.css` dual-patched (hash drift retained). Home/`/uslugi/`/Раздел untouched. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e47-fix03-service-general-signs-readmore-before-20260715-160233\`. Report: `REPORTS/REPORT-FP-0002-V9-06E47-FIX03-service-signs-readmore.md`. Evidence: `REPORTS/evidence/v9-06e47-fix03-*.csv`.

## V9-06E47-FIX04 Service signs read-more toggle (2026-07-15)

E47-FIX04 **PASS** (local; Git commit skipped): Operator polish on FIX03 signs editorial — read-more becomes a proper toggle. `v9-shell.js` `initServiceSignsReadMore`: expand keeps button visible as «Скрыть» (`aria-expanded="true"`); second click smooth-collapses to 5-line clamp and restores «Читать больше»; resize recalculates overflow and preserves state when still overflowing. No CSS/PHP/admin/DB/media changes. Source↔runtime hash match for `v9-shell.js`; operator `v9-style.css` untouched (intentional hash drift retained). Home/`/uslugi/`/Раздел untouched. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e47-fix04-service-signs-readmore-toggle-before-20260715-170136\`. Report: `REPORTS/REPORT-FP-0002-V9-06E47-FIX04-service-signs-readmore-toggle.md`. Evidence: `REPORTS/evidence/v9-06e47-fix04-*.csv`.

## V9-06E47 Service general freeze — Услуга accepted (2026-07-15)

E47 freeze **PASS** (local; Git commit skipped; **0 DB writes**; **no WordPress product changes**): Operator accepted Услуга model after E47–FIX04 («Да всё гуд.»). Full freeze backup of runtime DB/theme/plugin/ACF JSON/uploads + postmeta/content for `#74/#314/#78/#73/#77/#84` + admin/frontend/read-more validation + source↔runtime hash sync. **Page type Услуга (`service_general`) is frozen** pending explicit change request. Home freeze / `/uslugi/` freeze / accepted Раздел model untouched; representative services preserved; operator `v9-style.css` drift preserved. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e47-service-general-freeze-accepted-before-next-phase-20260715-175228\`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E47-SERVICE-GENERAL-ACCEPTED.md`. Report: `REPORTS/REPORT-FP-0002-V9-06E47-service-general-freeze.md`. Evidence: `REPORTS/evidence/v9-06e47-service-general-freeze-*.csv`. Model: `DOCS/SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md`.

## V9-06E52 Generic pages demo ACF SoT + placeholder (2026-07-16)

E52 **PASS** (local; later included in E52–E53 closeout persistence): Ordinary pages with `page-templates/generic.php` (**15** included) — ACF SoT `group_fp02_page_generic_content` (`generic_page_lead` / `generic_page_body`); empty optional → hide (no hardcoded demo); `page_layout_mode` full/placeholder retained from E51; page-specific seed from `post_content`; placeholder switch validated on `#1039` (final `full`); empty-field hide PASS on `#14`; regression Home/Services hub/sections/services/blog/specialists/o-centre/contacts preserved; `#315`/`#78` remain **Услуга**; operator CSS `11A45ABE…` preserved; source↔runtime 6/6. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e52-generic-pages-demo-acf-sot-placeholder-before-20260716-043220\`. Report: `REPORTS/REPORT-FP-0002-V9-06E52-generic-pages-demo-acf-sot-placeholder.md`. Evidence: `REPORTS/evidence/v9-06e52-*.csv`. Model: `DOCS/GENERIC-PAGES-ADMIN-PARITY-MODEL-v1.md`.

## V9-06E53 Admin UX section styling (2026-07-16)

E53 **PASS** then **FREEZE ACCEPTED** (operator «Ну вот теперь гуд.»; freeze **0 DB writes**; admin CSS/UX only): Unified FP-0002 ACF admin visual layer — new `admin-fp02-acf.css`, enqueue on all `page`/`service` edit screens + FP02 Site Settings, `body.fp02-acf-admin`. Removes noisy internal ACF grey field dividers inside thematic blocks; keeps major separators on `.fp02-acf-section-title` + ACF postbox spacing. Generic pages previously missed admin CSS (pre-E53 gap). No ACF JSON/content/frontend product mutation. Admin visual 9/9; frontend regression 14/14; `#315`/`#78` remain **Услуга**/`service_general`; Home/hub/sections/services/generic freezes preserved; operator `v9-style.css` `11A45ABE…` preserved; source↔runtime match for delivered theme files. Pre-task backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e53-admin-ux-section-styling-before-20260716-051631\`. Freeze backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e53-admin-ux-section-styling-freeze-accepted-before-experience-pack-20260716-053214\`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E53-ADMIN-UX-ACCEPTED.md`. Reports: `REPORTS/REPORT-FP-0002-V9-06E53-admin-ux-section-styling.md`, `REPORTS/REPORT-FP-0002-V9-06E53-admin-ux-section-styling-freeze.md`. Evidence: `REPORTS/evidence/v9-06e53-*.csv`. Doc: `DOCS/ADMIN-UX-ACF-SECTION-STYLING-v1.md`.

## V9-06E58 Current baseline freeze before Figma visual audit (2026-07-16)

E58 **FREEZE PASS** (local; DB writes **0**; no visual-audit fixes): Operator manual CSS/template edits after E57-FIX02 treated as current visual canon. Runtime `v9-style.css` promoted into canonical source — protected SHA256 `307A111EB229BA16C8A388C8A83B18C257C80AE57648E1601C2FA0EBF1851E04`. Theme/plugin product-file source↔runtime parity PASS. Full backup `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e58-current-baseline-freeze-before-visual-audit-20260716-225434\` (DB dump SHA256 `77C609572BC3A72D42312839CB1CD990F95B369BA53FE8D6CD4C8F1C9A76D35B`). Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E58-CURRENT-BASELINE-BEFORE-VISUAL-AUDIT-ACCEPTED.md`. Bound: E53 + E54 + E54-FIX01 + E55 + E56 + E56-FU01 + E56-FU02 + E57 + E57-FIX01 + E57-FIX02 + operator manual edits. Status label: **V9-06E58 CURRENT BASELINE FROZEN BEFORE FIGMA VISUAL AUDIT**. Next: Figma visual layout audit findings only; **no production SMTP / no production readiness claim**.

## V9-06E52–E53 closeout + Forge Proger experience pack (2026-07-16)

Closeout **PASS** (scoped Git persistence under `FP-0002-SHPIGOVSKY/**` only; push-if-safe separate gate): Persists E52 generic ACF SoT + placeholder, E53 admin UX + freeze marker/evidence, FP docs (`PROJECT-STATUS.md`, `SOURCE-AUTHORITY.md`), and Forge Proger experience pack at `DOCS/FORGE-PROGER-EXPERIENCE-PACK/v9-06-batch-01/`. **Explicit:** experience pack is **documentation only** — **not** integrated into Forge Proger brains/rules/system prompts; **not** a global MARS authority update. No runtime DB product mutation in closeout docs wave; backups remain under `X:\MARS-Localhost\backups\...` (not committed). Recommended next: migrate Web-GPT chat to a fresh chat; later collect batch-02 experience before any brain upgrade charter.

## V9-06E38–E51 Git persistence (2026-07-16)

V9-06E38–E51 persistence **PASS** (local; **no push**; **0 DB writes**; **no WordPress product changes** during persistence): Selective exact-path Git commit on `mars/canonical-post-recovery` preserving accepted E38–E51 WordPress source authority — Home admin parity E38–E42; Services hub E43–E44; service layout/admin parity E45–E47; representative/full service rollout E48–E49 + `#315` FIX01; section demo ACF SoT E50; placeholder mode E51 + real admin switch FIX02; freeze markers and evidence CSVs. **470** FP-0002 paths committed; excluded INCOMING design binaries, validation chrome-profile caches, `__pycache__`, large zip/fig. Clean worktree add attempted but failed (`Could not reset index file`); used exact-path staging in main worktree instead. Runtime smoke before commit **19/19 PASS**; `#315`/`#78` **Услуга**/`service_general`; unintended placeholders **0**; operator CSS drift preserved. Report: `REPORTS/REPORT-FP-0002-V9-06E38-E51-persistence.md`. Evidence: `REPORTS/evidence/v9-06e38-e51-persistence-*.csv`. **Not** a production deployment claim.

## V9-06E49 Full service rollout freeze AFTER FIX01 (2026-07-16)

E49 freeze after FIX01 **PASS** (local; Git commit skipped; **0 DB writes**; **no WordPress product changes**): Freeze retry after E49-FIX01 restored `#315`. Full freeze backup of DB/theme/plugin/ACF JSON/uploads + postmeta/content for all 29 publish service CPT + frontend snapshots (35 routes) + inventory/admin/content/alcohol/FE/accepted/smoke/source↔runtime evidence. **29/29** inventory PASS; **26/26** individual services `service`/`service_general`; `#315` and `#78` **Услуга**; unintended placeholders **0**; no alcohol copy-paste 26/26; content 26/26; smoke 35/35; Home E42 / `/uslugi/` E44 / sections E50 / E51 Placeholder Mode preserved; operator CSS `11A45ABE…` preserved; source↔runtime PASS (CSS intentional drift). Freeze backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e49-full-service-rollout-freeze-accepted-after-fix01-before-next-phase-20260716-025224\`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E49-FULL-SERVICE-ROLLOUT-ACCEPTED-AFTER-FIX01.md`. Report: `REPORTS/REPORT-FP-0002-V9-06E49-full-service-rollout-freeze-after-fix01.md`. Evidence: `REPORTS/evidence/v9-06e49-freeze-after-fix01-*.csv`. Next: **CREATE_V9_06E38_E51_PERSISTENCE_TASK**.

## V9-06E49-FIX01 Restore #315 service layout (2026-07-16)

E49-FIX01 **PASS** (local; Git commit skipped): Restored freeze blocker `#315` Лечение лекарственной зависимости from `placeholder`/`placeholder` → `service`/`service_general` via real wp-admin form POST (E51-FIX02 ACF nonce path). Admin **Услуга**; FE full service (no `placeholder-stack`); content preserved (+4 empty ACF refs allowed); placeholder option still available; unintended individual placeholders **0**; controls/sections/Home/`/uslugi/` preserved; operator CSS `11A45ABE…`; no product PHP/theme source mutation. DB writes: **2** (role+layout). Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e49-fix01-restore-315-service-layout-before-20260716-023509\`. Report: `REPORTS/REPORT-FP-0002-V9-06E49-FIX01-restore-315-service-layout.md`. Evidence: `REPORTS/evidence/v9-06e49-fix01-*.csv`. Superseded next step by E49 freeze after FIX01.

## V9-06E49 Full service rollout freeze (2026-07-16)

E49 freeze **PARTIAL PASS** (local; Git commit skipped; **0 DB writes**; **no WordPress product changes**): Operator accepted E49 full service ACF rollout and requested freeze. Full freeze backup of DB/theme/plugin/ACF JSON/uploads + postmeta/content for all 29 publish service CPT + frontend snapshots (35 routes) + inventory/admin/content/alcohol/FE/accepted/smoke/source↔runtime evidence. Individual Услуга rollout frozen with **known exception `#315`** (at freeze time `placeholder`/`placeholder`; was `service`/`service_general` at E49; ACF content still present; not restored during freeze — charter forbade layout mutation). Superseded for `#315` state by **E49-FIX01**. `#78` remains **Услуга**; Home E42 / `/uslugi/` E44 / sections E50 / E51 Placeholder Mode preserved; no alcohol copy-paste 26/26; content 26/26; smoke 35/35; operator CSS `11A45ABE…` preserved; source↔runtime PASS (CSS intentional drift). Freeze backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e49-full-service-rollout-freeze-accepted-before-next-phase-20260716-021704\`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E49-FULL-SERVICE-ROLLOUT-ACCEPTED.md`. Report: `REPORTS/REPORT-FP-0002-V9-06E49-full-service-rollout-freeze.md`. Evidence: `REPORTS/evidence/v9-06e49-freeze-*.csv`.

## V9-06E51 Placeholder Mode freeze (2026-07-16)

E51 freeze **PASS** (local; Git commit skipped; **0 DB writes**; **no WordPress product changes**): Operator accepted E51-FIX02 («Да, теперь всё гуд»). Placeholder Mode (**Заглушка**) is **frozen** pending explicit change request. Accepted model: first-level Раздел|Услуга|Заглушка; nested Услуга|Заглушка; generic optional `page_layout_mode` default `full`; FE stub = header/nav/H1/footer; render-only; ACF preserved; real admin save requires `acf[field_…]` (FIX02). `#78` final **Услуга**/`service_general`; Home E42 / `/uslugi/` E44 / sections E50 / services `#74/#314/#81/#85` preserved; operator CSS drift preserved (`11A45ABE…`); source↔runtime sync PASS for E51-critical files. Freeze backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e51-placeholder-mode-freeze-accepted-before-next-phase-20260716-013604\`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E51-PLACEHOLDER-MODE-ACCEPTED.md`. Report: `REPORTS/REPORT-FP-0002-V9-06E51-placeholder-mode-freeze.md`. Evidence: `REPORTS/evidence/v9-06e51-freeze-*.csv`.

## V9-06E51-FIX02 Real admin placeholder switch (2026-07-16)

E51-FIX02 **PASS** (local; Git commit skipped): Operator rejected E51-FIX01 on real wp-admin (`#78` button did not keep Услуга; FE stayed stub). True root cause: `ServiceLayoutGovernance::prepare_editor_role_field` reset `$field['name']` after `acf_prepare_field()` had set it to `acf[field_fp02_service_editor_role]`, so radios posted bare `service_editor_role` outside `$_POST['acf']`. Fix: do not overwrite name/key. Validated with authenticated admin GET + full form POST (`_acf_nonce` + parsed fields); meta `service/service_general`; admin reload checked Услуга; FE full service (~112KB, no placeholder-stack); content fingerprint unchanged; final `#78` left **Услуга**. Home/`/uslugi`/sections/`#74/#314/#81/#85` preserved; operator CSS `11A45ABE…`; source↔runtime match. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e51-fix02-real-admin-placeholder-switch-before-20260716-010437\`. Report: `REPORTS/REPORT-FP-0002-V9-06E51-FIX02-real-admin-placeholder-switch.md`. Evidence: `REPORTS/evidence/v9-06e51-fix02-*.csv`. Superseded next step by E51 freeze.

## V9-06E51-FIX01 Placeholder manual switch persistence (2026-07-16)

E51-FIX01 **FALSE-POSITIVE for real wp-admin** (local meta/`acf_save_post` simulation looked PASS; operator real admin FAIL — superseded by FIX02): Attempted fix for Заглушка↔Услуга after E51. Partial causes addressed (resolver role-wins; layout sync on `update_value`; technical field kept hidden-but-present), but did **not** fix bare ACF input name posting. `#78` left placeholder after FIX01. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e51-fix01-placeholder-manual-switch-persistence-before-20260716-001214\`. Report: `REPORTS/REPORT-FP-0002-V9-06E51-FIX01-placeholder-manual-switch-persistence.md`. Evidence: `REPORTS/evidence/v9-06e51-fix01-*.csv`.

## V9-06E51 Placeholder layout mode restore (2026-07-15)

E51 **PASS** (local; Git commit skipped): Restored editor-facing **Заглушка** (`service_editor_role=placeholder` → technical `service_layout_variant=placeholder` → frontend `placeholder-stack.php` with H1 only). Nested services can choose Услуга|Заглушка (no longer forced message-only). Sync no longer demotes placeholder→service. Generic Content pages gain optional `page_layout_mode` (full/placeholder). Test enable `#78` only; content metas preserved (2 layout meta changes). Home/`/uslugi`/sections `#73/#77/#84` / services `#74/#314/#81/#85` full layouts preserved. Operator `v9-style.css` hash `11A45ABE…` preserved. Source↔runtime hash match for E51 deliverables. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e51-placeholder-layout-mode-restore-before-20260715-234500\`. Report: `REPORTS/REPORT-FP-0002-V9-06E51-placeholder-layout-mode-restore.md`. Evidence: `REPORTS/evidence/v9-06e51-*.csv`. Governance: `DOCS/SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md`. Next: **OPERATOR_REVIEW_REQUIRED**.

## V9-06E50 Service sections demo ACF SoT freeze (2026-07-15)

E50 freeze **PASS** (local; Git commit skipped; **no product redesign**; evidence DB writes **2** = temporary `#77` `section_nature_lead` clear+restore only): Operator accepted E50 («Всё гуд!»). Page type **Раздел** (`#73/#77/#84`, `group_fp02_service_section_parity`) is **frozen** pending explicit change request. Normal FE text SoT = page ACF; empty optional → hide/empty-safe; emergency helpers technical-only; `#73` ТЕСТ/000101 preserved; `#77/#84` section-specific headings; Home E42 / `/uslugi/` E44 / Услуга controls+E49 samples preserved; operator `v9-style.css` drift preserved (`11A45ABE…`); source↔runtime sync PASS for E50-critical files. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e50-service-sections-demo-acf-sot-freeze-accepted-before-next-phase-20260715-230201\`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E50-SERVICE-SECTIONS-DEMO-ACF-SOT-ACCEPTED.md`. Report: `REPORTS/REPORT-FP-0002-V9-06E50-service-sections-demo-acf-sot-freeze.md`. Evidence: `REPORTS/evidence/v9-06e50-freeze-*.csv`. Model: `DOCS/SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md`. Next: **CREATE_V9_06E49_FULL_SERVICE_ROLLOUT_FREEZE_TASK**.

## V9-06E50 Service sections demo ACF SoT (2026-07-15)

E50 **PASS** (local; Git commit skipped): Раздел pages `#73/#77/#84` — normal frontend text SoT is page ACF (seeded/demo/current); empty optional fields no longer inject hardcoded template demo; emergency PHP helpers retained technical-only; `#77/#84` section-specific headings/intros/nature/subnav (no dependency copy-paste); program catalogue images/shared automatic blocks kept; Home/`/uslugi` freeze untouched (Home gallery residual order only); service controls + E49 samples preserved; operator `v9-style.css` hash match vs E50 backup (`11A45ABE…`). Source↔runtime sync for section helpers/templates/plugin parity/ACF JSON. DB writes: 21. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e50-service-sections-demo-acf-sot-before-20260715-222858\`. Report: `REPORTS/REPORT-FP-0002-V9-06E50-service-sections-demo-acf-sot.md`. Evidence: `REPORTS/evidence/v9-06e50-*.csv`. Model: `DOCS/SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md`. Next: **OPERATOR_REVIEW_REQUIRED** / sections freeze.

## V9-06E49 Full service rollout (2026-07-15)

E49 **PASS** (local; Git commit skipped): Full remaining `service_general` ACF content rollout — **21** target pages. Page-title / parent-section / neutral DEMO seeds only — **no alcohol copy-paste** from `#74`. Controls `#74/#314/#78/#81/#85` validate-only (0 mutations); sections `#73/#77/#84` untouched; `#316` child tiles preserved; images `#1238/#1239/#1709` where empty. ACF field definitions / theme/plugin product files unchanged this wave. Home residual 8 B only; `/uslugi/`/sections/controls FE equal; admin 29/29 PASS; FE 26/26 PASS; alcohol scan 25/25 PASS; smoke 35/35 PASS. Operator `v9-style.css` runtime preserved (`11A45ABE…`). DB writes: 589. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e49-full-service-rollout-before-20260715-212933\`. Report: `REPORTS/REPORT-FP-0002-V9-06E49-full-service-rollout.md`. Evidence: `REPORTS/evidence/v9-06e49-*.csv`. Model: `DOCS/SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md`. Next: E49 freeze task.

## V9-06E48 Representative services rollout (2026-07-15)

E48 **PASS** (local; Git commit skipped): Staged ACF content rollout of accepted Услуга model to representatives `#74` (control), `#314` (child tiles), `#78` (ordinary nested), `#81` (psych), `#85` (RPP). Page-title/neutral DEMO seeds only — **no alcohol copy-paste** from `#74`. Existing meaningful values preserved; images `#1238/#1239/#1709` where empty; `#314` automatic children preserved. ACF field definitions / theme/plugin product files unchanged this wave. Home/`/uslugi/`/Раздел FE equal (Home gallery residual only); admin service groups = Layout→Hero→«Услуга — блоки»; section model intact. Operator `v9-style.css` hash matches E47 freeze (`11A45ABE…`). DB writes: 107. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e48-representative-services-rollout-before-20260715-203048\`. Report: `REPORTS/REPORT-FP-0002-V9-06E48-representative-services-rollout.md`. Evidence: `REPORTS/evidence/v9-06e48-*.csv`. Model: `DOCS/SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md`.

## V9-06E46-FIX05 Section demo data + no template fallback (2026-07-15)

E46-FIX05 **PASS** (local; Git commit skipped): Removed normal template-fallback SoT for Раздел pages — empty ACF fields on `#73/#77/#84` seeded from current FE demo/fallbacks; meaningful `#73` operator values preserved. Renamed section image fields to `section_team_image` / `section_corridor_image` (admin labels already Russian); seeded team `#1238` (reused Home staff ML id; Home meta untouched), corridor `#1709` (theme asset registered in ML), landscape `#1239` retained. Admin instructions cleaned (demo + emergency reserve wording). FE `team-stats.php` + `shpigovsky_section_image_or_asset_prefer()` read ACF first. Emergency PHP helpers remain for unseeded edge cases only. Home/`/uslugi/` freeze untouched; operator `v9-style.css` hash preserved. Source↔runtime hash match. DB writes: ~60 field seeds (+1 ML corridor attachment). Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e46-fix05-section-demo-data-no-template-fallback-before-20260715-004351\`. Report: `REPORTS/REPORT-FP-0002-V9-06E46-FIX05-section-demo-data-no-template-fallback.md`. Evidence: `REPORTS/evidence/v9-06e46-fix05-*.csv`.

## V9-06E46-FIX04 Section admin cleanup + landscape image (2026-07-15)

E46-FIX04 **PASS** (local; Git commit skipped): Hid `section_program_footer_label` from section parity admin (meta kept; FE fallback/stored via `program.php`). Added section-specific `section_clinic_landscape_image` + updated notice (no Home SoT). Seeded `#73/#77/#84` with Home attachment `#1239`. Updated `clinic-landscape.php` for section context; enhanced `shpigovsky_section_image_or_asset` ID support. Hid Classic Editor for service CPT (`admin-editor.php`). Home freeze / `/uslugi/` freeze untouched; operator `v9-style.css` hash preserved. Source↔runtime hash match. DB writes: 3 image seeds (+ field ref metas via `update_field`). Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e46-fix04-section-admin-cleanup-landscape-before-20260715-002138\`. Report: `REPORTS/REPORT-FP-0002-V9-06E46-FIX04-section-admin-cleanup-landscape.md`. Evidence: `REPORTS/evidence/v9-06e46-fix04-*.csv`.

## V9-06E46-FIX03 Section CTA cleanup + program fallback (2026-07-14)

E46-FIX03 **PASS** (local; Git commit skipped): Removed ineffective `5. CTA «Раздел услуги»` admin notice + `section_mid_cta_visible` toggle from `group_fp02_service_section_parity` (55 fields; sections renumbered 5–14). Mid-CTA frontend SoT remains Structured Sections `cta_*` + site phone; stack still loads mid-cta (legacy meta default ON). Program intro/footer: user values win; empty → FE demo/fallback only; partial repeater rows do not pad with demo; managed empty skips legacy fight. `#73` `section_program_intro_items` re-seeded from legacy intros (FE Lorem preserved); footer `… ТЕСТ` operator value kept. `#77/#84` not content-overwritten. Home templates hash-match backup; `/uslugi/` fingerprint match; operator `v9-style.css` match. Source↔runtime hash match. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e46-fix03-section-cta-program-fallback-before-20260714-234056\`. Report: `REPORTS/REPORT-FP-0002-V9-06E46-FIX03-section-cta-program-fallback.md`. Evidence: `REPORTS/evidence/v9-06e46-fix03-*.csv`.

## V9-06E46-FIX02 Service section repeaters + stages fix (2026-07-14)

E46-FIX02 **PASS** (local; Git commit skipped): Section admin polish on `#73` Зависимости — §3 label «Дочерние услуги»; §5 CTA «Раздел услуги»; nature text pairs → `section_nature_text_blocks` repeater; program intros → `section_program_intro_items`; stages items → `section_stages_items` (+ Home rehab-requirements pattern); fixed premature `?>` PHP leak in `template-parts/service/stages.php`. `#73` seeded from legacy metas; `#77/#84` no content overwrite (fallback). Home templates hash-unchanged vs backup; `/uslugi/` HTML fingerprint match; operator `v9-style.css` match. Source↔runtime hash match for FIX02 deliverables. DB writes: 6 new repeater meta keys on `#73`. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e46-fix02-section-repeaters-stages-before-20260714-225532\`. Report: `REPORTS/REPORT-FP-0002-V9-06E46-FIX02-service-section-repeaters-stages.md`. Evidence: `REPORTS/evidence/v9-06e46-fix02-*.csv`.

## V9-06E46-FIX01 Service section hero/layout admin separation (2026-07-14)

E46-FIX01 **PASS** (local; Git commit skipped): Separated mixed ACF group `Service — Layout and Hero` into **Service — Layout** (`group_fp02_service_layout_hero`, layout + hub/catalog flags) and **Hero страницы услуги** (`group_fp02_service_hero`, shared hero fields; meta keys preserved). Updated section parity §1 notice. Soft-disabled 5 duplicate DB `acf-field-group` posts still titled Layout and Hero. Admin/frontend recheck for `#73` Зависимости — blocks accounted; stages item bodies documented as FIX02 candidate. `/uslugi/zavisimosti/` fingerprint unchanged vs FIX01 backup; Home fields 74; `/uslugi/` fingerprint match; operator `v9-style.css` match. Source↔runtime hash match. DB writes: 5 (disable duplicate groups). Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e46-fix01-service-section-hero-admin-separation-before-20260714-214425\`. Report: `REPORTS/REPORT-FP-0002-V9-06E46-FIX01-service-section-hero-admin-separation.md`.

## V9-06E46 Service section admin parity — Зависимости (2026-07-14)

E46 **PASS** (local; Git commit skipped): Admin parity for service page type **Раздел** based on `#73` Зависимости. New ACF group `group_fp02_service_section_parity` (63 fields, frontend order via numbered notices). Migrated hardcoded nature/approach/program intros/stages chrome/dependencies chrome/FAQ heading to ACF with template fallbacks; 14 block toggles + RU source notices; `#73` seeded from current frontend; `#77/#84` toggles ON without overwriting content. Fixed `home/reviews.php` so `home_reviews_visible` applies only on front page. Home freeze untouched (74 fields); `/uslugi/` hub visual preserved; operator `v9-style.css` hash match vs E46 backup. Source↔runtime hash match for E46 deliverables. DB writes: 74 (seed metas). Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e46-service-section-admin-parity-zavisimosti-before-20260714-210729\`. Report: `REPORTS/REPORT-FP-0002-V9-06E46-service-section-admin-parity-zavisimosti.md`. Model: `DOCS/SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md`. Evidence: `REPORTS/evidence/v9-06e46-*.csv`.

