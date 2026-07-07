# FP-0002 Canonical WordPress Source Surface

**Project:** FP-0002 — Шпиговский  
**Surface:** `WORDPRESS/`  
**Status:** V9-06E21 REUSABLE BLOCKS BATCH 2 FIELDS **PARTIAL PASS** — Batch 2 admin fields (Шапка, Подвал, Герои, Комфорт / преимущества) + renderer migration + seed; **4** ACF JSON; **2** plugin + **6** theme files; fresh DB checkpoint; runtime delivered; frontend 9/9 PASS; screenshots PARTIAL (Playwright/admin). NEXT: **CREATE_V9_06E22_OPERATOR_REUSABLE_BLOCKS_ADMIN_QA_TASK**
**Classification:** MVP SKELETON DOCUMENTED — FULL V9 VISUAL PARITY WAVE PLAN APPROVED

---

## Purpose

Git-tracked canonical source for WordPress theme, project plugin, and ACF JSON delivery to the local FP-0002 runtime.

## Authority

| Role | Path |
|------|------|
| **Canonical WordPress source** | `X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS\` |
| **Runtime deployment target** | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\` |
| **V9 frontend source (separate)** | `X:\AI MARS\workspaces\fp-0002-shpigovsky-v9\src\` |
| **V9 static output (separate)** | `X:\AI MARS\workspaces\fp-0002-shpigovsky-v9\dist\` |

The runtime is **not** the canonical editable source. Delivery flows: Git source → manifested package → bounded runtime apply.

## V9-06A / V9-06A.1 architecture (2026-07-03)

| Surface | Status |
|---------|--------|
| V9-06A | COMPLETE |
| V9-06A.1 | COMPLETE — reconciliation |
| WordPress architecture | **APPROVED** |
| Route classification | RECONCILED |
| Service entity registry | 15 VERIFIED |
| Service permalink contract | DEFINED |
| ACF Pro | **ADMITTED** as operator-managed external dependency (OD-001 / V9-06B.2) |
| BoundedMeta primary path | REJECTED |
| V9-06B | **COMPLETE** — theme + core skeleton |
| V9-06C | **COMPLETE — CONTENT MODEL SOURCE IMPLEMENTED** |
| V9-06C.1 | **COMPLETE — SOURCE ACTIVATION GATE RESOLVED** |
| Runtime changes | **AUTHORIZED FILE DELIVERY (V9-06D.1 rerun) + AUTHORIZED OBJECT SKELETON (V9-06D.2)** |
| WordPress source implementation | **CONTENT MODEL COMPLETE** |
| WordPress runtime implementation | **CONTENT MODEL ACTIVATED — 15 SERVICE OBJECTS CREATED / PAGE TEMPLATES RECONCILED** |
| FW-07C-2D | SUPERSEDED BY ARCHITECTURE-FIRST SEQUENCE (V9-06D) |

Authority: [architecture/FP-0002-WORDPRESS-ARCHITECTURE-v1.md](architecture/FP-0002-WORDPRESS-ARCHITECTURE-v1.md)

## Structure

```text
WORDPRESS/
  README.md
  SOURCE-AUTHORITY.md
  architecture/       # V9-06A design pack
  manifests/          # source and package manifests
  packages/           # built ZIP packages
  theme/shpigovsky/   # V9-06B skeleton theme
  plugins/shpigovsky-core/  # V9-06B skeleton plugin
  validation/         # V9-06B static validation
  reports/            # implementation reports
```

## Foundation classification

| Surface | Classification |
|---------|----------------|
| Theme | V9-06D7-E CONTACTS TEMPLATE RUNTIME DELIVERED — D7-E contacts stacks live in local runtime |
| Shpigovsky Core | V9-06D.2 CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE |
| ACF JSON | V9-06D9-R DELIVERED — 14 LOCAL JSON FILES; shared reviews options group added |

## Provenance

- **FOUNDATION_ORIGIN:** `workspaces/fp-0002-shpigovsky-v6/WORDPRESS/` (historical V6 surface)
- **CANONICAL_CURRENT:** this surface (adopted from prepared runtime foundation, FW-07C-2C)
- Runtime foundation preserved per V9-05A adoption register

## Delivery policy (FW-07C-2C)

- Mode: `ADDITIVE_ONLY` (proven)
- Overwrite: NOT AUTHORIZED
- Delete: NOT AUTHORIZED (except exact owned proof cleanup)
- Unknown files: FAIL CLOSED

See [SOURCE-AUTHORITY.md](SOURCE-AUTHORITY.md) and Forge delivery contract.

## V9-06B.2 ACF dependency admission

ACF PRO advanced-custom-fields-pro/acf.php v6.8.5 is admitted as an **operator-managed external dependency**. MARS may use its public APIs after admission but must not source, install, update, replace, delete, distribute, package, or manage licensing for it.

ACF Extended PRO acf-extended-pro/acf-extended.php v0.9.2.3 is classified separately as operator-managed and **not approved for FP-0002 use by default**. ACF Free remains installed but inactive and is not used while PRO is active.

Registry: architecture/FP-0002-OPERATOR-MANAGED-EXTERNAL-PLUGINS-v1.md.

## V9-06C content model source implementation

V9-06C implements the canonical WordPress content model in source only:

- `service` CPT source and `/uslugi/{service-path}/` permalink source are implemented in `plugins/shpigovsky-core/`.
- 13 ACF Pro field group definitions are implemented in source and canonical JSON is generated under `acf-json/`.
- Options Page, admin UX helpers, ACF dependency guards, and validation hooks are source implemented.
- Runtime delivery, WordPress object creation, database writes, rewrite flushing, ACF runtime DB registration, V9 HTML/CSS/JS integration, and runtime ACF JSON writes were not performed.

Report: `reports/FP-0002-V9-06C-CONTENT-MODEL-SOURCE-IMPLEMENTATION-REPORT-v1.md`.


## V9-06C.1 source activation gate resolution (2026-07-04)

V9-06D.1 runtime delivery was blocked before apply by the old `SHPIGOVSKY_CORE_SKELETON=true` source gate. V9-06C.1 resolves that source blocker with `SHPIGOVSKY_CORE_MODE=content_model` and an explicit module activation registry. Runtime writes: 0. WordPress object writes: 0.

Reports:

- `reports/FP-0002-V9-06C1-SOURCE-ACTIVATION-GATE-RESOLUTION-REPORT-v1.md`
- `reports/FP-0002-V9-06D1-RUNTIME-DELIVERY-CONTENT-MODEL-ACTIVATION-REPORT-v1.md` — historical blocked attempt, superseded by V9-06C.1 source fix
- `reports/FP-0002-V9-06D1-RERUN-RUNTIME-DELIVERY-CONTENT-MODEL-ACTIVATION-REPORT-v1.md` — V9-06D.1 rerun PASS; runtime code/model activation complete


## V9-06D.1 rerun runtime delivery (2026-07-04)

V9-06D.1 rerun delivered `theme/shpigovsky`, `plugins/shpigovsky-core`, and 13 `acf-json` files into the local runtime under checkpoint control. Service CPT, ACF local field groups, Options Page, admin hooks, validation hooks, and runtime health are verified. WordPress object creation, content migration, redirects, rewrite flush, plugin updates/install/deletes, and V9 integration remain not started.


## V9-06D.2 WordPress object skeleton (2026-07-04)

V9-06D.2 created the controlled WordPress object skeleton in the local FP-0002 runtime: 15 `service` CPT objects with registry metadata and hierarchy, 0 new Pages, 13 existing Page template assignments, 0 Posts, 0 menu changes, 0 option changes, 0 redirects, and no rewrite flush. Content migration and V9 integration remain not started.

Report: `reports/FP-0002-V9-06D2-WORDPRESS-OBJECT-SKELETON-REPORT-v1.md`.


## V9-06D.3 content migration planning (2026-07-04)

Planning-only phase complete: route/object matrices, ACF fill strategy, and minimal visual content seed plan. Runtime content writes: 0.

Report: `reports/FP-0002-V9-06D3-CONTENT-MIGRATION-PLANNING-REPORT-v1.md`.


## V9-06D.4 RERUN minimal content seed for visual route QA (2026-07-04)

Authorized minimal ACF/meta seed applied to Pages 4/5/20 and Services 73/74/77/84 under DB checkpoint control. Full content migration, V9 HTML/CSS/JS integration, menus, redirects, and Options Page values were not performed.

### REWRITE-FLUSH-MICRO-GATE (2026-07-04)

Soft rewrite flush performed under DB checkpoint (`wp rewrite flush`, no `--hard`, `.htaccess` unchanged). Options changed: `rewrite_rules` only. Service 74 generated permalink still matches expected path but HTTP remains **404** — classification `FLUSH_NOT_SUFFICIENT`. Report: [reports/FP-0002-REWRITE-FLUSH-MICRO-GATE-REPORT-v1.md](reports/FP-0002-REWRITE-FLUSH-MICRO-GATE-REPORT-v1.md).

### ROUTE-OWNERSHIP-INVESTIGATION (2026-07-04)

Read-only diagnostics complete. Primary cause: **POST_TYPE_LINK_REWRITE_MISMATCH** — depth-2 rewrite maps `service=$matches[2]` (leaf only) while hierarchical CPT lookup requires `parent/child`. Page ID 6 / Service ID 73 shared path **CONFIRMED** as secondary ownership debt, not the direct Service 74 404 mechanism. Recommended next: rewrite rule repair micro-task. V9-06D.5: **BLOCKED**. Runtime mutations: 0.

### REWRITE-RULE-REPAIR (2026-07-04)

Depth-2 rewrite query repaired to `service=$matches[1]/$matches[2]` in `ServicePermalinks.php`; delivered to local runtime; soft flush under checkpoint. Service 74 HTTP **200** (resolved ID 74). Controls all 200. Content/ACF/menus/redirects unchanged. V9-06D.5: **UNBLOCKED**. Report: [reports/FP-0002-REWRITE-RULE-REPAIR-REPORT-v1.md](reports/FP-0002-REWRITE-RULE-REPAIR-REPORT-v1.md).

### V9-06D.5 visual route QA (2026-07-04)

Read-only visual route QA after rewrite repair: all seven required routes HTTP **200**; Service 74 regression **PASS**; header/footer/main present; desktop/mobile screenshots captured; theme remains V9-06B skeleton (no V9 integration). Runtime mutations: **0**. Verdict: **PARTIAL PASS**. Report: [reports/FP-0002-V9-06D5-VISUAL-ROUTE-QA-REPORT-v1.md](reports/FP-0002-V9-06D5-VISUAL-ROUTE-QA-REPORT-v1.md).

### V9-06D.6 template integration planning (2026-07-04)

Planning-only rerun after Cursor crash recovery (`D6_RECOVERABLE_RESUME_READY`). Static→WP matrix, ACF binding, component/asset plan, integration waves D7-A…F, runtime delivery/rollback plan, and risk register complete. V9 integration and theme/plugin source changes: **NOT STARTED**. Next: `CREATE_V9_06D7_GLOBAL_SHELL_ASSET_INTEGRATION_SOURCE_TASK` (operator review). Report: [reports/FP-0002-V9-06D6-TEMPLATE-INTEGRATION-PLANNING-REPORT-v1.md](reports/FP-0002-V9-06D6-TEMPLATE-INTEGRATION-PLANNING-REPORT-v1.md). Crash recovery: [reports/FP-0002-V9-06D6-CURSOR-CRASH-RECOVERY-AUDIT-REPORT-v1.md](reports/FP-0002-V9-06D6-CURSOR-CRASH-RECOVERY-AUDIT-REPORT-v1.md).

Reports:

- `reports/FP-0002-V9-06D6-TEMPLATE-INTEGRATION-PLANNING-REPORT-v1.md` — D.6 planning PASS
- `reports/FP-0002-V9-06D6-CURSOR-CRASH-RECOVERY-AUDIT-REPORT-v1.md` — crash recovery PASS
- `reports/FP-0002-V9-06D5-VISUAL-ROUTE-QA-REPORT-v1.md` — D.5 visual route QA PARTIAL PASS
- `reports/FP-0002-REWRITE-RULE-REPAIR-REPORT-v1.md` — repair PASS
- `reports/FP-0002-ROUTE-OWNERSHIP-INVESTIGATION-REPORT-v1.md` — investigation PASS
- `reports/FP-0002-V9-06D4-RERUN-MINIMAL-CONTENT-SEED-FOR-VISUAL-ROUTE-QA-REPORT-v1.md` — rerun PASS/PARTIAL
- `reports/FP-0002-V9-06D4-MINIMAL-CONTENT-SEED-FOR-VISUAL-ROUTE-QA-REPORT-v1.md` — previous blocked attempt (HEAD mismatch), preserved
- `reports/FP-0002-REWRITE-FLUSH-MICRO-GATE-REPORT-v1.md` — flush micro-gate PARTIAL PASS


## V9-06D7-A runtime delivery

D7-A global shell/assets delivered to local runtime theme only. PHP lint PASS. Checkpoint + hash match PASS. Seven D.5 routes HTTP 200; Service 74 PASS; V9 CSS/JS enqueued. No DB/content/ACF/menu/redirect writes. Evidence: `validation/v9-06d7a-runtime-delivery/`. Next: D7-B home template source (operator review).


## V9-06D7-B runtime delivery

D7-B home template delivered to local runtime theme only. PHP lint PASS. Checkpoint + hash match PASS. Seven D.5 routes HTTP 200; Service 74 PASS; Home D7-B sections visible (8/20 V9 wave; optional sections omitted where ACF empty). No DB/content/ACF/menu/redirect writes. Evidence: `validation/v9-06d7b-runtime-delivery/`. Next: D7-C Services Hub template source (operator review).


## V9-06D7-C services hub template source

D7-C Services Hub template integrated in canonical theme source only. PHP lint PASS. CPT-driven category hub groups, hero, program block, FAQ, final-form. Founder-quote/comfort/genotyping/galleries deferred. No runtime delivery, no DB/content/ACF writes. Evidence: `validation/v9-06d7c-services-hub-template-source/`. Next: D7-C runtime delivery (operator review).


## V9-06D7-C runtime delivery

D7-C Services Hub template delivered to local runtime theme only. PHP lint PASS. Checkpoint + hash match PASS. Seven D.5 routes HTTP 200; Service 74 PASS; Services Hub core-wave sections visible (6/10 V9 wave; FAQ omitted where ACF empty; founder-quote/comfort/genotyping/galleries deferred). Home D7-B stability PASS. No DB/content/ACF/menu/redirect writes. Evidence: `validation/v9-06d7c-runtime-delivery/`. Next: D7-D service template source (operator review).


## V9-06D7-D runtime delivery

D7-D Service template delivered to local runtime theme only. PHP lint PASS. Checkpoint + hash match PASS. Seven D.5 routes HTTP 200; Services 73/74/77/84 core-wave sections visible; Service 74 alcohol-special markers detected; Home D7-B and Services Hub D7-C stability PASS. Deferred shared V9 blocks documented. No DB/content/ACF/menu/redirect writes. Evidence: `validation/v9-06d7d-runtime-delivery/`. Next: D7-E contacts template source (operator review).


## V9-06D7-E runtime delivery

D7-E Contacts template delivered to local runtime theme only. PHP lint PASS. Checkpoint + hash match PASS. Seven D.5 routes HTTP 200; `/kontakty/` renders D7-E contacts body, location cards, rehabilitation steps, CTA band (modal-only); map/messengers omitted where expected. Home D7-B, Services Hub D7-C, Service templates 73/74/77/84 stability PASS. No DB/content/ACF/menu/redirect writes. Evidence: `validation/v9-06d7e-runtime-delivery/`. Next: D7-F final route QA (operator review).


## V9-06D7-F final route QA (2026-07-05)

Read-only QA PASS after D7-A–D7-E. Seven first-wave routes HTTP 200; Service 74 regression PASS; known gaps EXPECTED_ONLY. No runtime/source/DB mutations. Evidence: `validation/v9-06d7f-final-route-qa/`. Next: D8 content seed planning.


## V9-06D8 content seed planning (2026-07-05)

Planning-only: MVP gap map, ACF/options inventory, Olga admin UX plan, seed waves D8-A…G, content source map, mutation safety protocol. Runtime inventory PARTIAL (live DB unavailable; D7-F/D4 evidence used). No runtime/source/DB mutations. Report: `reports/FP-0002-V9-06D8-CONTENT-SEED-PLANNING-REPORT-v1.md`. Evidence: `validation/v9-06d8-content-seed-planning/`. Next: D8-A site options seed (operator review).

## V9-06D8-D services hub content seed (2026-07-05)

D8-D Services Hub page #5 ACF only: `services_hub_intro` (V9 heroLead) and `services_hub_faq_items` (5 FAQ rows, LOCAL_MVP_PLACEHOLDER). Developer-only query/placeholder fields unchanged. DB checkpoint `v9-06d8d-services-hub-content-seed-pre-20260704-210430`. Route smoke ALL_200. Hub visual smoke PASS. No runtime/source/home/service/contacts/options writes. Evidence: `validation/v9-06d8d-services-hub-content-seed/`. Report: `reports/FP-0002-V9-06D8D-SERVICES-HUB-CONTENT-SEED-REPORT-v1.md`. Next: D8-E contacts content seed (operator review).

## V9-06D8-E contacts content seed (2026-07-05)

D8-E Contacts page #20 ACF only: `contacts_form_intro` (V9 intro), `contacts_address` (V9 Moscow consulting address), `contacts_blocks` (2 V9 location rows). Map/messengers/phones skipped (operator URLs or D8-A options canonical). DB checkpoint `v9-06d8e-contacts-content-seed-pre-20260704-211441`. Route smoke ALL_200. Contacts visual smoke PASS. No runtime/source/home/hub/service/options writes. Evidence: `validation/v9-06d8e-contacts-content-seed/`. Report: `reports/FP-0002-V9-06D8E-CONTACTS-CONTENT-SEED-REPORT-v1.md`. Next: D8-G post-seed QA (operator review).

## V9-06D8-G post-seed QA (2026-07-05)

D8-G **COMPLETE (PARTIAL PASS)**: Route matrix ALL_200; ACF integrity PASS; visual smoke PASS; admin usability PARTIAL. Readiness: **READY_FOR_OPERATOR_VISUAL_REVIEW**. Evidence: `validation/v9-06d8g-post-seed-qa/`. Report: `reports/FP-0002-V9-06D8G-POST-SEED-QA-REPORT-v1.md`. Next: operator visual review.

## V9-06D9-A visual parity audit (2026-07-05)

D9-A **COMPLETE (FAIL)**: Read-only static V9 vs WP runtime parity audit. Home: 20 static sections vs 6 runtime; hero image absent (ACF not seeded); 5/10 Inter font 404s (CSS root path bug); 18 screenshots captured. Zero DB/ACF/runtime/source mutations. Evidence: `validation/v9-06d9a-visual-parity-audit/`. Report: `reports/FP-0002-V9-06D9A-VISUAL-PARITY-AUDIT-REPORT-v1.md`.

## V9-06D9-0 full V9 visual port charter (2026-07-05)

D9-0 **COMPLETE (PASS)**: Read-only full visual port charter and repair wave plan. WP runtime interpreted as lightweight MVP skeleton (not catastrophic failure). Static V9 full inventory, WP current inventory, lightweight-vs-broken classification, header/messenger parity plan, home 20-section transfer plan, asset/font/vendor plan, ACF/content/media map, waves D9-B…H (+ optional D8-F). Messenger icons absent because D8-A skipped `social_links`; static V9 uses `href="#"` placeholders — D9-B can restore visuals without operator URLs. Zero DB/ACF/runtime/source mutations. Evidence: `validation/v9-06d9-0-full-visual-port-charter/`. Report: `reports/FP-0002-V9-06D9-0-FULL-V9-VISUAL-PORT-CHARTER-REPORT-v1.md`. Next: **CREATE_V9_06D9B_HEADER_FONT_ASSET_MESSENGER_REPAIR_TASK** (recommended).

## V9-06D9-E home slider / vendor / pagination repair (2026-07-05)

D9-E **PASS**: Specialists heading restored; vendor CSS cascade fixed (swiper → v9-style) for pagination dot parity; bounded runtime delivery (2 files). No DB/ACF writes. Route smoke ALL_200. Evidence: `validation/v9-06d9e-home-slider-vendor-pagination-repair/`. Report: `reports/FP-0002-V9-06D9E-HOME-SLIDER-VENDOR-PAGINATION-REPAIR-REPORT-v1.md`. Next: D9-F visual parity QA.

## V9-06D9-F home + footer visual parity QA (2026-07-05)

D9-F **PARTIAL PASS**: Read-only QA after D9-D/D9-E. Home 19/19 sections + order PASS; footer PASS; slider/vendor PASS; routes ALL_200. FAQ transplant typo in `faq.php` (MINOR_REPAIR_REQUIRED). Evidence: `validation/v9-06d9f-home-footer-visual-parity-qa/`. Report: `reports/FP-0002-V9-06D9F-HOME-FOOTER-VISUAL-PARITY-QA-REPORT-v1.md`. Next: D9-G micro visual repair.

## V9-06D9-G FAQ micro visual repair (2026-07-05)

D9-G **PASS**: Fixed FAQ heading/id/aria transplant typo in `template-parts/home/faq.php` (`comfort-heading` → `faq-heading`; heading text → Нас часто спрашивают); resolved duplicate `comfort-heading` id. Bounded runtime delivery (1 file). No DB/ACF/options/menu writes. Post-repair Home + route smoke ALL PASS. ACF editability readiness: READY. Evidence: `validation/v9-06d9g-micro-visual-repair-faq-heading/`. Report: `reports/FP-0002-V9-06D9G-FAQ-MICRO-VISUAL-REPAIR-REPORT-v1.md`. Next: **CREATE_V9_06D9H_ACF_ADMIN_EDITABILITY_WIRING_TASK**.

## V9-06D9-K controlled media upload + ACF seed (2026-07-05)

D9-K **PASS**: 5 Home media uploads + ACF seed on page #4 (hero image + 4 gallery rows). Attachments 89–93; DB checkpoint PASS; visual regression PASS; routes ALL_200. No source/theme/ACF JSON writes. Evidence: `validation/v9-06d9k-controlled-media-upload-acf-seed/`. Report: `reports/FP-0002-V9-06D9K-CONTROLLED-MEDIA-UPLOAD-ACF-SEED-REPORT-v1.md`. Next: D9-L admin editor / ACF visibility repair.

## V9-06D9-L admin editor / ACF visibility repair (2026-07-05)

D9-L **PASS**: Classic Editor installed/activated; Gutenberg disabled; 13 ACF groups synced from existing JSON to DB; Home #4 seeded values preserved; frontend regression PASS; routes ALL_200. No source/theme/ACF JSON/content writes. Evidence: `validation/v9-06d9l-admin-editor-acf-visibility-repair/`. Report: `reports/FP-0002-V9-06D9L-ADMIN-EDITOR-ACF-VISIBILITY-REPAIR-REPORT-v1.md`. Next: D9-M native page content cleanup.

## V9-06D9-M native page content cleanup (2026-07-05)

D9-M **PASS**: Cleared obsolete native `post_content` on 13 template-managed pages; DB checkpoint PASS; ACF values preserved; frontend regression PASS; routes ALL_200. Evidence: `validation/v9-06d9m-native-page-content-cleanup/`. Report: `reports/FP-0002-V9-06D9M-NATIVE-PAGE-CONTENT-CLEANUP-REPORT-v1.md`. Next: D9-N hide native editor for template pages.

## V9-06D9-N hide native editor for template-managed pages (2026-07-05)

D9-N **PASS**: Theme admin helper hides native Classic Editor box on 13 allowlisted template-managed pages; operator-review pages retain editor; bounded runtime delivery (2 theme files); frontend regression PASS; routes ALL_200; admin screenshots PARTIAL. No DB/ACF/content writes. Evidence: `validation/v9-06d9n-hide-native-editor-template-pages/`. Report: `reports/FP-0002-V9-06D9N-HIDE-NATIVE-EDITOR-FOR-TEMPLATE-PAGES-REPORT-v1.md`. Next: D9-O admin UX QA.

## V9-06D9-O ACF reviews teaser required flag repair (2026-07-05)

D9-O **PASS**: `home_reviews_teaser` optional; runtime ACF JSON restored; frontend regression PASS. Evidence: `validation/v9-06d9o-acf-reviews-teaser-required-flag-repair/`. Report: `reports/FP-0002-V9-06D9O-ACF-REVIEWS-TEASER-REQUIRED-FLAG-REPAIR-REPORT-v1.md`. Next: D9-P admin UX QA.

## V9-06D9-P admin UX QA (2026-07-05)

D9-P **PARTIAL PASS**: Read-only admin UX QA after D9-L/M/N/O. Home #4 ACF visible; native editor hidden; reviews teaser optional (simulation PASS); hero/gallery populated; managed pages PASS; operator-review pages preserved; frontend 19/19 sections routes ALL_200. Live authenticated Home save: OPERATOR_CONFIRMATION_REQUIRED. Admin screenshots PARTIAL (login on some screens). Zero DB/source/ACF JSON/value/content/media mutations. Evidence: `validation/v9-06d9p-admin-ux-qa/`. Report: `reports/FP-0002-V9-06D9P-ADMIN-UX-QA-REPORT-v1.md`. Next: D9-Q reviews include planning.

## V9-06D9-P git scope drift disclosure (2026-07-05)

D9-P Admin UX QA commit `b8361aad` was **mixed-scope**: 28 valid FP-0002 D9-P evidence/status files plus 3 unrelated OCPilot/SITE-002 files (`projects/ocpilot/OCPILOT-STATE.md`, `OPERATIONAL-INDEX.md`, `sites/site-002/reports/SITE-002-PRODUCTION-TASK-INTAKE-CATALOG-LOADMORE-1C-CRON.md`). Commit message described OCPilot only. OCPilot files classified as **valid foreign project documentation**; no rollback, delete, reset, or revert performed. Corrective documentation (Option C) preserves audit evidence in `reports/FP-0002-V9-06D9P-GIT-SCOPE-DRIFT-AUDIT-REPORT-v1.md` and `validation/v9-06d9p-git-scope-drift-audit/`. **D9-Q must start from the D9-P scope drift corrective commit HEAD.**

## V9-06D9-Q reviews include planning (2026-07-06)

D9-Q **PASS**: Read-only architecture planning. Recommended **Hybrid E** — ACF Options shared reviews on `fp02-site-settings` + shared theme include + static V9 fallback; deprecate `home_reviews_teaser` on Home admin in D9-R. Frontend smoke PASS. Zero DB/source/ACF JSON/value/runtime mutations. Evidence: `validation/v9-06d9q-reviews-include-planning/`. Report: `reports/FP-0002-V9-06D9Q-REVIEWS-INCLUDE-PLANNING-REPORT-v1.md`. Next: D9-R shared include source/schema implementation.

## V9-06D9-R reviews shared include implementation (2026-07-06)

D9-R **PASS**: Shared reviews architecture implemented — `inc/reviews-helpers.php`, `template-parts/shared/reviews-slider.php`, Home thin wrapper, `/otzyvy/` wired to shared include; ACF Options group `group_fp02_site_options_reviews` on `fp02-site-settings`; `home_reviews_teaser` removed from Home group JSON (orphan meta preserved). DB checkpoint before ACF sync. Bounded runtime delivery + `wp acf json sync` (14 groups). Static V9 10-slide fallback preserved; routes ALL_200. No reviews seed, no ACF value writes. Admin screenshots PARTIAL (headless). Evidence: `validation/v9-06d9r-reviews-shared-include-implementation/`. Report: `reports/FP-0002-V9-06D9R-REVIEWS-SHARED-INCLUDE-IMPLEMENTATION-REPORT-v1.md`. Prior: D9-S seed below.

## V9-06D9-S controlled reviews options seed (2026-07-06)

D9-S **PARTIAL PASS**: DB checkpoint `v9-06d9s-controlled-reviews-options-seed-pre-20260706-005734`. Seeded `reviews_enabled`, `reviews_section_heading`, 10 `reviews_items` rows from static V9 fallback (legacy runtime subfields `author_label`/`text`). Home #4 unchanged. Frontend still **FALLBACK** — `field_fp02_reviews_items` key collision with page reviews group; helper reads `review_author` not `author_label`. Zero source/theme/ACF JSON changes. Repaired in D9-T below.

## V9-06D9-T reviews options key fix + helper normalization (2026-07-06)

D9-T **PASS**: Unique `field_fp02_options_*` keys in `group_fp02_site_options_reviews.json`; helper normalization for legacy + canonical subfields; 3 ACF reference meta updates. DB checkpoint `v9-06d9t-reviews-options-key-fix-pre-20260706-010904`. Runtime delivery + ACF import. Source mode **OPTIONS**; 10 reviews on Home and `/otzyvy/`; `is_demo: false`. Evidence: `validation/v9-06d9t-reviews-options-key-fix-helper-normalization/`. Report: `reports/FP-0002-V9-06D9T-REVIEWS-OPTIONS-KEY-FIX-HELPER-NORMALIZATION-REPORT-v1.md`. Repaired in D9-U below.

## V9-06D9-U reviews admin UX repair (2026-07-06)

D9-U **PASS**: Home `Reviews teaser` blocker removed (theme suppresses plugin-local field); 10 rows migrated to canonical `review_*` option meta; top-level admin **Отзывы** (`fp02-reviews`). DB checkpoint `v9-06d9u-reviews-admin-ux-repair-pre-20260706-013004`. Frontend **OPTIONS** unchanged. Admin screenshots PARTIAL. Evidence: `validation/v9-06d9u-reviews-admin-ux-repair/`. Report: `reports/FP-0002-V9-06D9U-REVIEWS-ADMIN-UX-REPAIR-REPORT-v1.md`. Next: D9-V admin visual QA.

## V9-06D9-V reviews admin + static layout reconciliation audit (2026-07-06)

D9-V **PARTIAL PASS**: Read-only reconciliation audit. Operator findings after D9-U **substantiated**: duplicate Site Settings reviews module (stale duplicate ACF field-group DB post); empty top-level **Отзывы** admin (ACF storage context `option` vs `fp02-reviews` mismatch); `/otzyvy/` layout mismatch vs static V9 archive card list (WP uses Home slider + skeleton archive placeholder). Home slider matches static V9 Home authority. D9-U treated as committed but operator-unverified. Zero DB/source/theme/ACF JSON/runtime mutations. Screenshots NOT_CAPTURED (tooling). Evidence: `validation/v9-06d9v-reviews-admin-static-layout-reconciliation-audit/`. Report: `reports/FP-0002-V9-06D9V-REVIEWS-ADMIN-STATIC-LAYOUT-RECONCILIATION-AUDIT-REPORT-v1.md`. Next: D9-W combined admin + layout repair.

## V9-06D9-Z WordPress readiness audit (2026-07-06)

D9-Z **PARTIAL PASS**: Holistic read-only readiness audit after D9-L through D9-Y. Runtime/routes/frontend key surfaces **READY**; Reviews chain **CLOSED**; admin/ACF **PARTIAL**; content/legal **NEEDS_OPERATOR_REVIEW** at D9-Z time — subsequently repaired E0→E2. Evidence: `validation/v9-06d9z-wordpress-readiness-audit/`. Report: `reports/FP-0002-V9-06D9Z-WORDPRESS-READINESS-AUDIT-REPORT-v1.md`. Superseded by E3 stable checkpoint.

## V9-06E3 WordPress stable checkpoint (2026-07-06)

E3 **PASS**: Read-only stable checkpoint after E2. Runtime **STABLE_LOCAL**; routes 13/13 PASS; menus/footer/legal/reviews **READY**; admin editability **PARTIAL** (auth screenshots); 11/11 frontend screenshots PASS. Stable checkpoint **DECLARED** at commit `8c935957`. Zero DB/source/theme/ACF JSON/runtime mutations. Evidence: `validation/v9-06e3-wordpress-stable-checkpoint/`. Report: `reports/FP-0002-V9-06E3-WORDPRESS-STABLE-CHECKPOINT-REPORT-v1.md`.

## V9-06E4 services layout + shared background visual reconciliation audit (2026-07-06)

E4 **PASS**: Read-only visual reconciliation after operator manual pass post-E3. **MISMATCH_CONFIRMED** on `/uslugi/` (wrong `hero--inner` vs static `services-inner-hero-v2`; main/layout drift). **MISSING_CONFIRMED** hero image on `/uslugi/zavisimosti/` (`hero_media` empty; asset in theme). **MISSING_CONFIRMED** shared backgrounds (`final-form__band`, `program-cta-band`, `home-rehabilitation-requirements__cta-band`) — root cause **CSS_PATH** (`/assets/...` 404 on WP; files present in theme). 4/4 screenshots captured (runtime + static V9 reference). Zero DB/source/theme/ACF JSON/runtime mutations. Evidence: `validation/v9-06e4-services-layout-shared-bg-visual-reconciliation-audit/`. Report: `reports/FP-0002-V9-06E4-SERVICES-LAYOUT-SHARED-BG-VISUAL-RECONCILIATION-AUDIT-REPORT-v1.md`. Next: **CREATE_V9_06E5_SERVICES_LAYOUT_SHARED_BG_REPAIR_TASK**.

## V9-06E8 static V9 content + main layout authority repair (2026-07-06)

E8 **PARTIAL PASS**: Enforced static V9 template authority for `/uslugi/`, `/kontakty/`, alcohol service leaf layout. Added `inc/v9-static-content.php`; 18 theme files; 0 DB writes; runtime delivered. Hub content/CTA/program + contacts maps/photo + alcohol full leaf stack repaired. E3 stable checkpoint **invalidated** for content parity. Automated probe ALL_200. Operator visual QA deferred to E9. Evidence: `validation/v9-06e8-static-v9-content-main-layout-authority-repair/`. Report: `reports/FP-0002-V9-06E8-STATIC-V9-CONTENT-MAIN-LAYOUT-AUTHORITY-REPAIR-REPORT-v1.md`. Next: **CREATE_V9_06E9_OPERATOR_STATIC_PARITY_VISUAL_QA_TASK**.

## V9-06E17 site settings IA skeleton (2026-07-07)

E17 **PASS**: Site Settings admin IA skeleton. Parent `fp02-site-settings` redirect; **Общие настройки** (`fp02-site-settings-general`, `post_id=option`) with contacts + modal/CTA field groups relocated; **Повторяемые блоки** parent + 12 skeleton block subpages per E16 inventory; top-level **Отзывы** (`fp02-reviews`) unchanged. DB checkpoint `v9-06e17-site-settings-ia-skeleton-pre-20260707-235348`. **2** plugin + **2** ACF JSON; **0** DB writes; runtime delivered. Routes 8/8 HTTP 200. Evidence: `validation/v9-06e17-site-settings-ia-skeleton/`. Report: `reports/FP-0002-V9-06E17-SITE-SETTINGS-IA-SKELETON-REPORT-v1.md`. Next: **CREATE_V9_06E18_REUSABLE_BLOCKS_BATCH_1_FIELDS_TASK**.
