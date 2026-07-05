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
