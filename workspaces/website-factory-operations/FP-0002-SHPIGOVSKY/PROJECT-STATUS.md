# FP-0002 — Project Status

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Last updated:** 2026-08-18 (PROD-P17 CONT1 **PASS** — PRE-CUTOVER redirects + DNS inventory)

**Current WordPress phase:** `FP-0002 PROD-P17 PRE-CUTOVER / CONT1` — **PASS**. `FP-0002 P17 PRE-CUTOVER NOW INCLUDES A VERIFIED LEGACY REDIRECT LAYER AND A COMPLETE NAMESERVER-MIGRATION PLAN`. Seven legacy 301s live on `http://shpigovsky.beget.tech/` (path-relative `.htaccess`, no future-host hardcode). `shpigovsky.ru` DNS inventoried (NS `ns1/ns2.hosting.reg.ru`, mail REG.RU hosting); Beget NS **not** switched. Core `0.3.8-p17`. Open tails: Beget zone prep → NS/SSL/siteurl → SMTP → indexing → sitemaps → crawl — `REPORTS/OPEN-ITEMS-FP-0002-AFTER-P17.md`. Report: `REPORTS/REPORT-FP-0002-PROD-P17-PRE-CUTOVER.md`. Evidence: `REPORTS/evidence/prod-p17-precutover/`. Git checkpoint pushed: `1b7fb5c47b2c7acd88e4313e64a15f7e59069fa6` on `origin/mars/canonical-post-recovery` (clean worktree; dirty main foreign WIP untouched). WPilot `write_enabled=false`.

**Prior WordPress phase:** `FP-0002 PROD-P16 TYPOGRAPHY RESIDUAL` — **PASS**. `PROD-P16 TYPOGRAPHY RESIDUAL COMPLETE — CURRENT LIVE WORDPRESS/ACF/WYSIWYG CONTENT NORMALIZED SAFELY WHERE APPROPRIATE — FUTURE EDITOR CONTENT USES ONE HTML-AWARE TYPOGRAPHY PIPELINE — URLS/HTML/SEO/SEARCH/TOC PRESERVED — FP-0002 READY FOR PRE-CUTOVER`. One owner: `RussianTypography` + `TypographyFilters` (`typography.russian`); render-time only; DB content mutations **0**; core `0.3.7-p16`; `6/6 SOURCE ↔ PRODUCTION MATCH`. Baseline `FP-0002-PROD-BASELINE-2026-08-17` extended with P16 typography section. Rollback: P14 full backup + `prod-p16-layer-b-pre` / `prod-p16-db-snapshots`. Report: `REPORTS/REPORT-FP-0002-PROD-P16-TYPOGRAPHY.md`. Evidence: `REPORTS/evidence/prod-p16-typography/`. Git checkpoint pushed: `35666e2bb98247072a7a7972d4271eaf8d5f36aa` on `origin/mars/canonical-post-recovery` (clean worktree; dirty main foreign WIP untouched). WPilot `write_enabled=false` / business writes **0**.

**Prior WordPress phase:** `FP-0002 PROD-P15 ENVIRONMENT / MIGRATION CLEANUP` — **PASS**. `PROD-P15 ENVIRONMENT CLEANUP COMPLETE — BEGET RUNTIME CORRECTLY CLASSIFIED AS PRODUCTION — LOCAL/TEST RUNTIME RESIDUE REMOVED WHERE SAFE — MAIL AND INDEXING INTENTIONALLY DEFERRED — FINAL DOMAIN CUTOVER NOT YET EXECUTED`. Closes deferred **P06**. `WP_ENVIRONMENT_TYPE=production`; debug off; MU mail suppression reclassified PRE-CUTOVER; live frontend `.test` URLs cleared; siteurl/home remain beget. Core `0.3.6-p15`. Baseline `FP-0002-PROD-BASELINE-2026-08-17` extended with P15 env-clean section. Rollback: P14 full backup + `prod-p15-layer-b-pre` / `prod-p15-db-snapshots`. Open tails (superseded by P16): typography → PRE-CUTOVER → domain/SSL → SMTP → indexing → sitemap submissions → final crawl — see `REPORTS/OPEN-ITEMS-FP-0002-AFTER-P15.md`. Report: `REPORTS/REPORT-FP-0002-PROD-P15-ENVIRONMENT-CLEANUP.md`. Evidence: `REPORTS/evidence/prod-p15-environment-cleanup/`. Git checkpoint pushed: `81912e7871bd45d75e8b02b288aaf0b6788744d6` on `origin/mars/canonical-post-recovery` (clean worktree; dirty main foreign WIP untouched). WPilot `write_enabled=false` / business writes **0**.

**Prior WordPress phase:** `FP-0002 PROD-P14 STABILIZATION / BASELINE / GIT CHECKPOINT` — **PASS**. `PROD-P14 STABILIZATION COMPLETE — CURRENT PRODUCTION REALITY CANONIZED — SERVICE RECORDS CURRENT — NEW BACKUP COMPLETE — NEW PRODUCTION BASELINE ESTABLISHED`. Operator + Olya accept current UI baseline. Fresh production intake reconciled (2 operator drifts canonized: `v9-style.css`, `content-page.php`). MetaCODE Dashboard v2 reflects baseline `FP-0002-PROD-BASELINE-2026-08-17`, wave **P13+P13-FU01**, parity MATCH, env warning for leftover `WP_ENVIRONMENT_TYPE=local` (widget-only — cleared in P15). Proven FU01 Activity Log QA rows removed (4). Full files+DB backup: `X:\AI MARS STORAGE\backups\fp-0002\prod-p14-full-20260816-173046\`. Core `0.3.5-p14`. WPilot `write_enabled=false` / business writes **0**. Report: `REPORTS/REPORT-FP-0002-PROD-P14-STABILIZATION.md`. Evidence: `REPORTS/evidence/prod-p14-stabilization/`. Git checkpoint pushed: `9a5f671cafece716635e6fb37b984bd9009261de` on `origin/mars/canonical-post-recovery` (clean worktree; dirty main foreign WIP untouched).

**Prior WordPress phase:** `FP-0002 PROD-P13-FU01 NATIVE SLUG UX` — **PASS** / **ACCEPTED**. Duplicate Admin «Постоянная ссылка» removed; canonical native permalink row for `service`/`specialist`. Exact **2** source files (`2/2 MATCH`). Report: `REPORTS/REPORT-FP-0002-PROD-P13-FU01-NATIVE-SLUG-UX.md`.

**Prior WordPress phase:** `FP-0002 PROD-P13 ADMIN / BLOG / SEO / NAV / iOS` — **PASS** / **ACCEPTED**. Users cleanup, Dashboard widget, DOCX, SEO meta, nav L2, socials, TOC, trackpad, iOS FIX02. Exact **41** files MATCH. Report: `REPORTS/REPORT-FP-0002-PROD-P13-ADMIN-BLOG-SEO-NAV-IOS.md`. Evidence: `REPORTS/evidence/prod-p13-admin-blog-seo-nav-ios/`.

**Prior WordPress phase:** `FP-0002 PROD-P12 UX / SLUGS / ACTIVITY LOG / iOS LIFEBUOY` — **PASS / PARTIAL**. `PROD-P12 TECHNICAL CLOSEOUT COMPLETE — OPERATOR/OLYA VISUAL + PHYSICAL IPHONE ACCEPTANCE PENDING`. Operator fresh Beget backup **ACKNOWLEDGED**. Exact-file/object rollback: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p12-layer-b-pre\` + `...\prod-p12-db-snapshots\`. Production intake: operator CSS drift in `v9-style.css` canonized; Olya content preserved. Tasks: Services CTA phone note LIVE; public CPT slug UX (`service`/`specialist`, `-copy-NN`, existing URLs untouched); nature text-blocks Admin-only (legacy demo fallthrough removed); Admin **Журнал действий** + table `fp02_user_activity_log`; lifebuoy WebKit/iOS-safe single transform ownership (physical iPhone pending — later **FAIL** on device, superseded by P13 FIX02). Exact **11** source files uploaded (`11/11 SOURCE ↔ PRODUCTION MATCH`). WPilot `write_enabled=false` / writes **0**. No commit/push. Report: `REPORTS/REPORT-FP-0002-PROD-P12-UX-SLUGS-ACTIVITY-IOS.md`. Evidence: `REPORTS/evidence/prod-p12-ux-slugs-log-ios/`.

**Prior WordPress phase:** `FP-0002 PROD-P11 SPECIALISTS CPT MIGRATION` — **PASS / PARTIAL**. `PROD-P11 TECHNICAL CLOSEOUT COMPLETE — OPERATOR VISUAL/ADMIN ACCEPTANCE PENDING`. Exact-file/object rollback: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p11-layer-b-pre\` + `...\prod-p11-db-snapshots\`. CPT `specialist` registered in `shpigovsky-core` (rewrite `specyalisty`, `has_archive=false`; hub page `#1030` preserved). Migrated IDs **1031/1032/1033/1097** in-place (`page`→`specialist`, parent→0); URLs unchanged HTTP 200. Cleared leftover `_wp_page_template` so `single-specialist.php` owns FE. ACF `group_fp02_specialist_profile` location → `post_type=specialist` (keys preserved). Smart Search + sitemap use CPT; no page duplicates. Fancybox Kostyuk PASS. Exact **12** source files uploaded (`12/12 SOURCE ↔ PRODUCTION MATCH`). WPilot `write_enabled=false` / writes **0**. No commit/push. Report: `REPORTS/REPORT-FP-0002-PROD-P11-SPECIALISTS-CPT-MIGRATION.md`. Evidence: `REPORTS/evidence/prod-p11-specialists-cpt-migration/`.

**Prior WordPress phase:** `FP-0002 PROD-P10 SEO INFRASTRUCTURE + SMART SEARCH ADMIN + INTEGRATIONS + TECHNICAL SEO AUDIT` — **PARTIAL PASS**. `PROD-P10 TECHNICAL CLOSEOUT COMPLETE — OPERATOR VISUAL/SEO ACCEPTANCE PENDING`. Exact-file rollback: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p10-layer-b-pre\`. Exact **10** source files uploaded (`10/10 SOURCE ↔ PRODUCTION MATCH`) + production-only `robots.txt` Sitemap append (Disallow:/ preserved). Native `/wp-sitemap.xml` LIVE (pages/posts/service/specialists). `YANDEX GENERAL PAGE/SERVICE FEED = NOT APPLICABLE UNDER CURRENT OFFICIAL SPEC` — XML sitemap used. Smart Search Admin settings under `Настройки сайта → SEO и интеграции` (code defaults preserve P09). Analytics/verification Admin fields LIVE (empty → no output). Technical SEO crawl 89 URLs; SAFE TECH FIX **1**. Temporary Smart Search option QA restored. DB lasting product writes **0**. WPilot `write_enabled=false` / writes **0**. No commit/push. Reports: `REPORTS/REPORT-FP-0002-PROD-P10-SEO-SEARCH-INTEGRATIONS.md`, `REPORTS/REPORT-FP-0002-PROD-P10-TECHNICAL-SEO-AUDIT.md`. Evidence: `REPORTS/evidence/prod-p10-seo-search-integrations/`.

**Prior WordPress phase:** `FP-0002 PROD-P09-FU01 MOBILE SMART SEARCH PARITY + OPERATOR CSS CANONIZATION` — **PASS**. `OPERATOR DESKTOP SMART SEARCH VISUAL ACCEPTED`. `OPERATOR CSS DRIFT PRESERVED AND CANONIZED` (`fp02-search.css` + local `v9-style.css`). `SMART SEARCH DESKTOP + MOBILE PARITY COMPLETE`. `SMART SEARCH LIVE SUGGESTIONS ACTIVE ON MOBILE OFFCANVAS`. Exact-file rollback: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p09-fu01-layer-b-pre\`. Exact **3** theme files uploaded; `3/3 SOURCE ↔ PRODUCTION MATCH`. Fancybox regression **PASS**. DB/Admin/ACF **0**. WPilot `write_enabled=false` / writes **0**. No commit/push. `PROD-P09 SMART SEARCH DESKTOP + MOBILE TECHNICAL CLOSEOUT COMPLETE — OPERATOR MOBILE VISUAL ACCEPTANCE PENDING`. Report: `REPORTS/REPORT-FP-0002-PROD-P09-SPECIALIST-FANCYBOX-SMART-SEARCH.md`. Evidence: `REPORTS/evidence/prod-p09-specialist-fancybox-smart-search/` (FU01-*).

**Prior WordPress phase:** `FP-0002 PROD-P09 SPECIALIST FANCYBOX + SMART SEARCH` — **PASS**. `PROD-P09 TECHNICAL CLOSEOUT COMPLETE — OPERATOR VISUAL ACCEPTANCE PENDING` (desktop later accepted in FU01). Operator override: `FULL BEGET FILES + DB BACKUP NOT REQUIRED FOR PROD-P09` → `P09 EXACT-FILE ROLLBACK MODE AUTHORIZED BY OPERATOR` (snapshots `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p09-layer-b-pre\`; not a global backup-policy change). Exact **6** theme files uploaded; `6/6 SOURCE ↔ PRODUCTION MATCH`. Fancybox: bind `.specialist-profile__certs-grid [data-fancybox]` → `SPECIALIST CERTIFICATE GALLERY FANCYBOX = PASS`. Smart search: REST `shpigovsky/v1/smart-search` + header panel groups → `SMART SEARCH LIVE — 3+ CHARACTER SUGGESTIONS GROUPED BY CONTENT TYPE`. DB/Admin/ACF **0**. WPilot `write_enabled=false` / writes **0**. No commit/push. Report: `REPORTS/REPORT-FP-0002-PROD-P09-SPECIALIST-FANCYBOX-SMART-SEARCH.md`. Evidence: `REPORTS/evidence/prod-p09-specialist-fancybox-smart-search/`.

**Prior WordPress phase:** `FP-0002 PROD-P08 UI / CONTENT SYSTEMS` — **PASS / PARTIAL**. `PROD-P08 TECHNICAL CLOSEOUT COMPLETE — OPERATOR VISUAL ACCEPTANCE PENDING`. Layer A: `CURRENT PRE-P08 LAYER A BACKUP = OPERATOR CONFIRMED`. Layer B: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p08-layer-b-pre\`. Exact **26** source files uploaded; `26/26 SOURCE ↔ PRODUCTION MATCH`. Workstreams: mobile non-Hero prev/next ≤767; WebKit-safe lifebuoy direct transform; Specialist ACF+template+migration (`#1031/#1032/#1033/#1097`); blog reading-time manual→auto@190 WPM; typography source+specialist (**broader DB WYSIWYG residual**). WPilot `write_enabled=false` / business writes **0**. No commit/push. Report: `REPORTS/REPORT-FP-0002-PROD-P08-UI-CONTENT-SYSTEMS.md`. Evidence: `REPORTS/evidence/prod-p08-ui-content-systems/`.

**Prior WordPress phase:** `FP-0002 PROD-P07-FU01-CONT2 EXACT-FILE DEPLOY` — **PASS**. `PROD-P07 TECHNICAL CLOSEOUT COMPLETE — FINAL OPERATOR VISUAL ACCEPTANCE PENDING`. `PROD-P07 FINAL ACCEPTANCE READY`. Beget IP unblock restored SSH/SFTP. Layer B: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p07-fu01-cont2-layer-b-pre\`. Exact 3 theme PHP files uploaded; `3/3 SOURCE ↔ PRODUCTION MATCH`. `/uslugi/` Lorem short-descs **9→0**, `DEMO —` **0**. Alcohol signs editorial + program Lorem omitted; 9 REAL signs + 10 REAL FAQ preserved. DB/Admin writes **0**. WPilot `write_enabled=false`. No commit/push. Report: `REPORTS/REPORT-FP-0002-PROD-P07-FU01-RESIDUAL-DEMO-LOREM-CLEANUP.md`. Evidence: `REPORTS/evidence/prod-p07-fu01-residual-demo-lorem-cleanup/`.


**Prior WordPress phase:** `FP-0002 PROD-P07 OLYA UX/ADMIN REFINEMENT` — **PASS / PARTIAL** then **CONDITIONALLY ACCEPTED**. Desktop program-card equal-height CSS; Guest Visit CTA restored in subdivision stages + guest helper; approach cards Admin/FE parity on `#73/#77/#84`; Generic Content reusable selector on `#13`; long-form Generic typography; targeted TEST/DEMO/Lorem cleanup. Layer B: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p07-layer-b-pre\`. Residuals handed to FU01. Report: `REPORTS/REPORT-FP-0002-PROD-P07-OLYA-UX-ADMIN-REFINEMENT.md`.

**Prior WordPress phase:** `FP-0002 PROD-P05-FU01 WPILOT AUTH CLOSEOUT` — **PASS**. WPilot **0.3.2 / 0.3.2-RC1** active (native Upload Plugin replace from 0.3.0). Authenticated REST READ **PROVEN**. Production token stored at gitignored `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token`. `write_enabled=false`. WP Admin HTTP **PASS** (`mars` Administrator). Filesystem READ + DB SELECT remain **PROVEN**. Current post-reimport Layer A backup **OPERATOR CONFIRMED**. Migration tails and DNS **deferred**. Runtime checkout **deferred**. **No commit/push.** Report: `REPORTS/REPORT-FP-0002-PROD-P05-FU01-WPILOT-AUTH-CLOSEOUT.md`.

**Prior WordPress phase:** `FP-0002 PROD-P05 WPILOT UPGRADE AND AUTHENTICATED READ GATE` — **BLOCKED** then closed by FU01. WP Admin HTTP then FAIL; post-reimport Layer A not yet confirmed; WPilot remained 0.3.0. Report: `REPORTS/REPORT-FP-0002-PROD-P05-WPILOT-UPGRADE-AUTH-GATE.md`.

**Prior WordPress phase:** `FP-0002 PROD-P04-FU02 POST-REIMPORT PRODUCTION REBASELINE` — **PARTIAL**. Operator full production re-import accepted as **new live baseline**. SSH/FTP/DB SELECT **PASS**; docroot `/home/s/shpigovsky/shpigovsky.ru/public_html` **PASS**. Product FS vs local: **`REIMPORT PRODUCT CODE PARITY CLEAN`**. WPilot **0.3.0**, write **false**. MARS `mars` Administrator in DB; HTTP Admin **FAIL**. Report: `REPORTS/REPORT-FP-0002-PROD-P04-FU02-POST-REIMPORT-REBASELINE.md`.

**Prior WordPress phase:** `FP-0002 PROD-P04-FU01 FILESYSTEM BASELINE` — **PASS** (now **HISTORICAL PRE-REIMPORT**). FTP/SSH home = real docroot; theme/core/ACF SHA baseline; WPilot FS 0.3.0; package replace SAFE. Report: `REPORTS/REPORT-FP-0002-PROD-P04-FU01-FILESYSTEM-BASELINE.md`.

**Prior WordPress phase:** `FP-0002 PROD-P04 BEGET ACCESS REPAIR` — **PARTIAL / OPERATOR ACTION REQUIRED** (superseded by FU01). SSH-local MySQL SELECT **PROVEN**; filesystem then still jailed to empty `beget.tech` placeholder. Report: `REPORTS/REPORT-FP-0002-PROD-P04-BEGET-ACCESS-REPAIR.md`.

**Prior WordPress phase:** `FP-0002 PROD-P03 PRODUCTION ACCESS VALIDATION` — **PARTIAL**. Operator `ACCESS FILES FILLED`. FTP/SSH auth **PASS** for `shpigovsky_mars`, but account is jailed to empty `shpigovsky.beget.tech/public_html` (Beget placeholder). Real WP docroot **`/home/s/shpigovsky/shpigovsky.ru/public_html`** exists and is **not readable** by this account. DB: name/user present; host/port/prefix **MISSING** at that time; remote 3306 OPEN; AUTH **FAIL** 1045. WP Admin **PASS** (`mars` / Administrator). WPilot **active 0.3.0 (OLDER)** vs baseline `0.3.2-RC1`; write **disabled**; token **CASE B** (hash only) — local prod token **not** created; authenticated READ **not** attempted (would mutate tracker). Public CSS/JS sample 5/5 **MATCH**. Runtime checkout **deferred**. **No production filesystem/DB/WPilot/DNS writes.** WP login may record core last_login/session. **No commit/push.** Next was P04 rebind + DB access repair. Report: `REPORTS/REPORT-FP-0002-PROD-P03-PRODUCTION-ACCESS-VALIDATION.md`.

**Prior WordPress phase:** `FP-0002 PROD-P01 BEGET READ-ONLY ONBOARDING` — **PARTIAL**. Operator migrated full local WordPress (files+DB) to Beget. Working production host: `http://shpigovsky.beget.tech/` (**LIVE RUNTIME TRUTH**). Canonical domain `shpigovsky.ru` = **`DNS_CUTOVER = DEFERRED`** (still old hosting — out of scope). Public route smoke PASS for core IA; V9-07A01 Program auto-source + Comfort gallery publicly verified; theme CSS/JS public hashes match source (`v9-style` `1CCC5A8F…`). Migration residues documented (hardcoded `shpigovsky.test` CTA links; title «локальная разработка»). Operator-confirmed Beget full files+DB backup exists. WPilot **already present** on Beget (public ping: bridge on / token-generated / write off; version SAFE UNKNOWN) — **not** installed by this wave. Current accepted package if upgrade needed: `metacode-wpilot` **0.3.2-RC1** ZIP SHA `d55c19d6…`. Docs: `DOCS/PRODUCTION/*`, `REPORTS/REPORT-FP-0002-PROD-P01-BEGET-READ-ONLY-ONBOARDING.md`, evidence `REPORTS/evidence/prod-p01-beget-read-only-onboarding/`. **Production mutations 0**; **no WPilot install/token/bridge/write by MARS**; **no commit**; **no push**. Next after P01: operator WP Admin WPilot version report → separate reconcile/upgrade gate (still pending; P02 only prepared access files).

**Prior WordPress phase:** `FP-0002 V9-07A01-FU01 RUNTIME CLEANUP + PRODUCTION UPLOAD PACK` — **PASS** (local cleanup + pack prepared); **no production connection/upload**; **no freeze**; **no commit**; **no push**. Removed orphan runtime Playwright `node_modules` + superseded interview MPEG-TS `.bak` (theme+uploads; bytes preserved in Stable v1/E63). Safety snapshot: `v9-07a01-fu01-cleanup-safety-20260723-222006`. Production pack (exact 14 files): `X:\AI MARS STORAGE\deployment-packs\fp-0002\v9-07a01-production-upload-20260723-222232\` (+ optional ZIP). Reports: `REPORTS/CLEANUP/REPORT-V9-07A01-FU01-RUNTIME-CLEANUP.md`, `REPORTS/DEPLOY/REPORT-V9-07A01-PRODUCTION-UPLOAD-PACK.md`. Source↔runtime theme/plugin MATCH; CSS `1CCC5A8F…` unchanged; DB writes **0**. **Note:** operator later migrated the **entire** local WordPress state to Beget — the 14-file A01 pack is not the sole production migration authority.

**Prior WordPress phase:** `FP-0002 V9-07A01 PROGRAM AUTO-SOURCE + COMFORT GALLERY FIX` — **PASS** (local validation); **operator review pending**; **no freeze**; **no commit**; **no push**. Post–Stable v1 correction (does not replace Stable v1 freeze). Operator CSS preserved; theme/plugin preflight MATCH. Program cards auto-source from parent `#13` children (title/permalink/`treatment_program_short_description`); O-centre `about_program_items` + service `programme_items` dormant for card content. Comfort Fancybox enqueued on `/uslugi/` + subdivision/leaf stacks; gallery open/nav/close/escape PASS. DB lasting writes **0** (reversible #1054 probe restored; `wp_cache_flush`). Backup: `v9-07a01-before-program-auto-source-comfort-gallery-fix-20260723-214353`. Report: `REPORTS/REPORT-FP-0002-V9-07A01-PROGRAM-AUTO-SOURCE-COMFORT-GALLERY-FIX.md`. Evidence: `REPORTS/evidence/v9-07a01-program-auto-source-comfort-gallery-fix/`. Ownership: `DOCS/TREATMENT-PROGRAM-AUTO-SOURCE-OWNERSHIP-v1.md`.

**Prior WordPress phase:** `FP-0002 V9 Stable v1 — LOCAL NEAR-PRODUCTION BASELINE FROZEN AND PUSHED` — **PASS** (closeout). Formulation: **Stable local near-production baseline**. Operator accepted. Operator CSS/JS canonized (`v9-style` **`1CCC5A8F…`**). Pre-release backup: `v9-06e63-before-stable-v1-closeout-20260718-003355`. Authoritative freeze: `v9-stable-v1-near-production-freeze-20260718-004137` (DB SHA256 `E38978E7D4FB2EAD…`). Release docs: `REPORTS/STABLE-V1/`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-STABLE-V1.md`. Report: `REPORTS/REPORT-FP-0002-V9-06E63-STABLE-V1-CLOSEOUT.md`. Evidence: `REPORTS/evidence/v9-06e63-stable-v1-closeout/`. **Public production deployment has not been performed.** Commit/push: via clean worktree to `origin/mars/canonical-post-recovery` Release commit `d1befe9b8bfc8688f2f286998ec048e6be49beb6` (see closeout report; push pending)..

**Prior WordPress phase:** V9-06E62E-FIX01 SEARCH WRAPPER + TRIGGER PLACEMENT — **PASS** (local validation); later included in Stable v1. Preflight source↔runtime drift **0**; operator `v9-style` **`C2246240…`** then superseded by E63 operator edits **`1CCC5A8F…`**. Search crumbs → `.internal-page-nav > .container > .breadcrumbs`; Search dropdown trigger desktop main Header only. Backup: `v9-06e62e-fix01-before-search-wrapper-trigger-placement-20260717-174720`. Report: `REPORTS/REPORT-FP-0002-V9-06E62E-FIX01-search-wrapper-trigger-placement.md`.
**Prior WordPress phase:** V9-06E62E 404 DECOR + WORDPRESS SEARCH — **PASS** (local validation); **operator review pending**; **no freeze**; **no commit**; **no push**. Operator CSS canonized (`v9-style` `18114D3C…` → **`C2246240…`** preserved; `fp02-404` runtime promoted then decor-width edit). Operator asset `404-decor.png` (670×425) installed; `404-visual.png` removed from active use/source/runtime. Header search dropdown + native WP search (`post`/`page`/`service`, 12/page); `search.php` + result cards + pagination + `noindex,follow`. DB writes: **0**. Backup: `v9-06e62e-before-404-decor-wordpress-search-20260717-173256`. Report: `REPORTS/REPORT-FP-0002-V9-06E62E-404-decor-wordpress-search.md`. Evidence: `REPORTS/evidence/v9-06e62e-404-decor-wordpress-search/`.

**Prior WordPress phase:** V9-06E62D Treatment Program Mini-Descriptions + 404 Figma Correction — **PASS** (local validation); **operator review pending**; **no freeze**; **no commit**; **no push**. Pre-wave operator theme/plugin drift **0**; `v9-style` **`18114D3C…`** preserved. New ACF group `group_fp02_treatment_program_child` (`page_parent==13`) field `treatment_program_short_description` / «Мини-описание»; seeded #1053–1056 from former hardcoded Home texts; helpers read page ACF (hardcoded body texts removed). 404 `fp02-404.css` retuned to Figma PNG metrics (typography `#475371` 32/20 desktop; spacing; button 262×53; PNG owns cutout radius). Exact-file delivery; no broad ACF sync. DB writes: seed + reversible edit/empty tests. Backup: `v9-06e62d-before-program-mini-descriptions-404-figma-correction-20260717-170730`. Report: `REPORTS/REPORT-FP-0002-V9-06E62D-program-mini-descriptions-404-figma-correction.md`. Evidence: `REPORTS/evidence/v9-06e62d-program-mini-descriptions-404-figma-correction/`.

**Prior WordPress phase:** V9-06E62C O-CENTRE CLEANUP + SERVICE ADMIN HIDE + STABLE REVIEW UID ANCHORS + FINAL REGRESSION — **PASS** (local validation); **operator review pending**; **no freeze**; **no commit**; **no push**. Pre-wave operator theme/plugin drift **0**; `v9-style` **`18114D3C…`** preserved. O-centre lead without span + new bullet field seeded; nested who-we-treat CTA → `<div class="program-cta-band">`; Service Structured Sections + Relationships hidden (`active:false` + filter); Reviews `review_uid` ×30 stable anchors; reorder test restored; 64 viewport screenshots PASS. DB writes: bullet seed + UIDs + reversible reorder. Backup: `v9-06e62c-before-ocentre-service-admin-review-anchor-final-regression-20260717-164734`. Report: `REPORTS/REPORT-FP-0002-V9-06E62C-ocentre-service-admin-review-anchor-final-regression.md`. Evidence: `REPORTS/evidence/v9-06e62c-ocentre-service-admin-review-anchor-final-regression/`. Demo Blog/Reviews remain pending production cleanup decision.

**Prior WordPress phase:** V9-06E62B BLOG/REVIEWS PAGINATION + SEO + SLIDER LINKS + DEMO CONTENT — **PASS** (local validation); **operator review pending**; **no freeze**; **no commit**; **no push**. Pre-wave operator drift **0**. Wave-additive CSS `E11627B9…` → **`18114D3C…`** (crumbs 16/22 preserved). Demo Blog thumbs `#1745–1754`; +20 demo Reviews (ACF options; total 30 / 3 pages); self-canonicals for Blog/Reviews pagination; slider «Читать весь отзыв» → archive anchors; Founder Quote ACF ownership seeded. Backup: `v9-06e62b-before-blog-reviews-pagination-seo-demo-content-20260717-162925`. Report: `REPORTS/REPORT-FP-0002-V9-06E62B-blog-reviews-pagination-seo-slider-links.md`. Evidence: `REPORTS/evidence/v9-06e62b-blog-reviews-pagination-seo-slider-links/`. E62C tails: O-centre deep validation, Service ACF cleanup, nested CTA, demo cleanup.

**Prior WordPress phase:** V9-06E62A 404 PAGE + INTERNAL BREADCRUMB WRAPPER + PHONE MASK — **PASS** (local validation); **operator review pending**; **no freeze**; **no commit**; **no push**. Operator CSS canonized (`v9-style` `DCB0C163…` → **`E11627B9…`**; crumbs 16/22 preserved). Figma 404 from `INCOMING/01_DESIGN/26.06.2026` PNG pair; Generic/Specialist `.internal-page-nav > .container > .breadcrumbs`; Triumph v6 vanilla phone mask `+7 (XXX) XXX-XX-XX`. DB writes: **0**. E61 tails retained open. Backup: `v9-06e62a-before-404-breadcrumb-wrapper-phone-mask-20260717-160948`. Report: `REPORTS/REPORT-FP-0002-V9-06E62A-404-breadcrumb-wrapper-phone-mask.md`. Evidence: `REPORTS/evidence/v9-06e62a-404-breadcrumb-wrapper-phone-mask/`.

**Prior WordPress phase:** V9-06E61 ADMIN CONTROLS + CONTACTS/BLOG/REVIEWS/O-CENTRE/HOME REFINEMENTS — **PARTIAL PASS** (local validation); **operator review pending**; **no freeze**; **no commit**; **no push**. Operator CSS/JS canonized from runtime then additive-only (`v9-style` `5E437875…` → `DCB0C163…`; breadcrumbs 16/22 preserved). Global breadcrumb toggles; Contacts multi-phone + messengers + empty crumb shell; Blog archive admin simplify + posts_per_page + 10 demo posts (#1745–1754); Reviews service relationship + 5-line expand + reviews_per_page; O-centre CTA-1/gallery removal + Home blocks reuse + red-line lead; Home dotted leaders already present. DB writes: settings seeds + demos. Backup: `v9-06e61-before-admin-controls-contacts-blog-reviews-ocentre-home-20260717-141747`. Report: `REPORTS/REPORT-FP-0002-V9-06E61-admin-controls-contacts-blog-reviews-ocentre-home.md`. Evidence: `REPORTS/evidence/v9-06e61-admin-controls-contacts-blog-reviews-ocentre-home/`.

**Prior WordPress phase:** V9-06E60-FIX01 EXACT BREADCRUMB/SUBNAV RESTORE + REVIEWS `/otzyvy/` FIGMA CORRECTION — **PASS** (local validation); **operator review pending**; **no freeze**; **no commit**; **no push**. Stable authority: E58 freeze backup `v9-06e58-current-baseline-freeze-before-visual-audit-20260716-225434` (`operator-edits` CSS `307A111E…`). Restored `.breadcrumbs` hover colors from E60 `accent-hover` → E58 `accent` (5 selectors); typography already matched E58 (14/18; blog ≤1024 8/12). `.services-page-subnav` already byte-identical to E58 (no rule change). Reviews archive names: `<h2>` → `<div class="review-archive-card__name">`; computed **18px / 24px**. Operator CSS preserved outside scope (`B60D01A4…` → `3F8163FF…`). DB writes: **0**. Backup: `v9-06e60-fix01-before-breadcrumb-subnav-reviews-correction-20260717-020758`. Report: `REPORTS/REPORT-FP-0002-V9-06E60-FIX01-breadcrumb-subnav-reviews.md`. Evidence: `REPORTS/evidence/v9-06e60-fix01-breadcrumb-subnav-reviews/`.

**Prior WordPress phase:** V9-06E60 NAV/BREADCRUMB TYPOGRAPHY AUDIT + PROGRAM CTA↔HOME CTA UNIFY + SERVICE-NAME LINKS + ACCENT HOVER — **PASS** (local validation); **operator review pending**; **no freeze**; **no commit**; **no push**. Operator CSS promoted (`v9-style` `C8AE0923299B…` → post-wave `B60D01A404FA…`). Task 00: no unwanted E58/E59 nav/breadcrumb typography changes found (16/20 nav; 14/18 crumbs; blog 8/12 Figma EXACT_GEOMETRY retained). `.program-cta-band` markup/CSS aligned to Comfort `.home-rehabilitation-requirements__cta-band` (wrap01/wrap02). Service names → permalink anchors. Title/nav hovers → `var(--color-accent-hover)` without underline where classified. DB writes: **0**. Backup: `v9-06e60-before-nav-breadcrumb-cta-service-links-20260717-015352`. Report: `REPORTS/REPORT-FP-0002-V9-06E60-nav-breadcrumb-cta-service-links.md`. Evidence: `REPORTS/evidence/v9-06e60-nav-breadcrumb-cta-service-links/`.

**Prior WordPress phase:** V9-06E59-FIX01 COMFORT GALLERY DECOR + CONTACTS ACF CLEANUP + FOOTER HOVER — **PASS** (local validation); **operator review pending**; **no freeze**; **no commit**; **no push**. Preflight: source↔runtime theme MATCH (operator CSS/HTML already canon; no promote). Comfort decor moved outside `.comfort__gallery` to `.comfort__gallery-decor` inside `.comfort__gallery-stage` (`display:contents` preserves visual grid). Obsolete Contacts page fields removed from ACF group/PHP: `contacts_address`, `contacts_map_url`, `contacts_blocks` (+ children); `contacts_locations` retained (2 rows); legacy postmeta dormant. Footer heading-link hover/focus → exact `color: var(--color-accent-hover)` only. Future task registered: Site Settings Admin IA Audit. DB writes: **0**. Backup: `v9-06e59-fix01-before-comfort-contacts-footer-corrections-20260717-013408`. Report: `REPORTS/REPORT-FP-0002-V9-06E59-FIX01-comfort-contacts-footer-corrections.md`. Evidence: `REPORTS/evidence/v9-06e59-fix01-comfort-contacts-footer-corrections/`. Future doc: `DOCS/FUTURE-TASK-SITE-SETTINGS-ADMIN-IA-AUDIT-AND-RU-UX-REBUILD-v1.md`.

**Prior WordPress phase:** V9-06E59 LAYOUT POLISH + CONTACTS MAPS + FOOTER LINKS + COMFORT CTA ADMIN PARITY — **PASS** (local validation); **operator review pending**; **no freeze**; **no commit**; **no push**. Latest operator CSS/HTML canonized from runtime (`v9-style` promoted `106D5BEB…` → post-wave `1AA1AAC8…`; operator rehab CTA band preserved). E58-VA-001 only: restored V9 `no-top-padding` utilities on Home staff/feature/landscape/why-us. Contacts page `#20`: new ACF repeater `contacts_locations` with validated Yandex Constructor embeds (2 seeded rows). Footer headings «Услуги» / «О центре» now link to `/uslugi/` and `/o-centre/`. Comfort Requirements reusable block (`fp02-block-comfort`): new `cta_lead_text` wired to `.home-rehabilitation-requirements__cta-lead-txt`. DB writes: **2 scopes** (`contacts_locations` on page 20; `cta_lead_text` option seed). Backup: `v9-06e59-before-layout-polish-maps-footer-comfort-admin-20260717-001046`. Report: `REPORTS/REPORT-FP-0002-V9-06E59-layout-polish-maps-footer-comfort-admin.md`. Evidence: `REPORTS/evidence/v9-06e59-layout-polish-maps-footer-comfort-admin/`.

**Prior WordPress phase:** V9-06E58 CURRENT BASELINE FROZEN BEFORE FIGMA VISUAL AUDIT — freeze + full backup + Git persistence **PASS**; Figma visual layout audit **COMPLETE (findings only)**; E58-FU01 decision pack complete; operator confirmed **E58-VA-001** for implementation in E59. Operator CSS protected (`v9-style` `307A111E…` at freeze; operator post-FU01 edits `106D5BEB…`). Backup: `v9-06e58-current-baseline-freeze-before-visual-audit-20260716-225434`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E58-CURRENT-BASELINE-BEFORE-VISUAL-AUDIT-ACCEPTED.md`. Audit report: `REPORTS/REPORT-FP-0002-V9-06E58-figma-visual-layout-audit.md`. Push: clean-worktree cherry-pick `29c07d21` on `origin/mars/canonical-post-recovery`. Findings: 0 CRITICAL / 1 HIGH / 4 MEDIUM / 3 LOW. **No production readiness / no production SMTP claim.**

**Prior WordPress phase:** V9-06E57-FIX02 Lifebuoy Start, Reveal, Easing and Rotation — **PASS** (local validation); later included in E58 freeze. Operator CSS was `2F7CC5AC…` then superseded by post-FIX02 operator manual edits (`307A111E…`). Lifebuoy motion tuning: top reveal ~50%; long-page max reveal ~80%; `easeOutCubic` + linear scale; rotation +≈20%. DB writes: **0**. Checkpoint: `v9-06e57-fix02-before-lifebuoy-start-reveal-easing-rotation-20260716-220628`. Report: `REPORTS/REPORT-FP-0002-V9-06E57-FIX02-lifebuoy-start-reveal-easing-rotation.md`. Evidence: `REPORTS/evidence/v9-06e57-fix02-lifebuoy-start-reveal-easing-rotation/`.

**Prior WordPress phase:** V9-06E57-FIX01 Lifebuoy Motion Refinement — **PASS** (local validation); **awaiting operator review**; **no freeze**; **no commit**; **no push**. Operator CSS preserved (`v9-style` `2F7CC5AC…`). Motion refinement on existing E57 lifebuoy only: base size ≈+30%; reveal up to ~70% (measured ~72% Home bottom); piecewise scale `1.00→1.20→0.72`; rotation −6°→+18° (short pages milder); reverse via same progress map; long/short threshold unchanged; reduced-motion freeze at t=0.28 unchanged. DB writes: **0**. Checkpoint: `v9-06e57-fix01-before-lifebuoy-motion-refinement-20260716-214936`. Report: `REPORTS/REPORT-FP-0002-V9-06E57-FIX01-lifebuoy-motion-refinement.md`. Evidence: `REPORTS/evidence/v9-06e57-fix01-lifebuoy-motion-refinement/`.

**Prior WordPress phase:** V9-06E57 Lifebuoy Global Background Parallax — **PASS** (local validation); **awaiting operator review**; **no freeze**; **no commit**; **no push**. Asset: `INCOMING/OPERATOR-ASSETS/E56/lifebuoy.webp` → `assets/img/decor/lifebuoy.webp` (byte-identical, 95568 B, SHA256 `B4F1C9F6…`). Global fixed decorative layer + scroll-progress parallax (`fp02-lifebuoy-parallax.css/js`); mount in `body-start.php`; operator `v9-style.css` preserved (`2F7CC5AC…`). Long/short page modes via `scrollable < max(2400, 4×vh)`; reduced-motion freeze at t=0.28. DB writes: **0**. Checkpoint: `v9-06e57-before-lifebuoy-global-parallax-20260716-212623`. Report: `REPORTS/REPORT-FP-0002-V9-06E57-lifebuoy-global-parallax.md`. Evidence: `REPORTS/evidence/v9-06e57-lifebuoy-global-parallax/`.

**Prior WordPress phase:** V9-06E56-FU02 Libertinus Serif — **PASS** (local validation); **awaiting operator review**; **no freeze**; **no commit**; **no push**. Archive used: `INCOMING/OPERATOR-ASSETS/E56/Libertinus_Serif.zip`. Selected asset: `assets/fonts/libertinus-serif/libertinus-serif-regular.ttf` (Regular / weight 400; TTF fallback — no local WOFF2 converter). Selectors: `.hero__title`, `.services-inner-hero-v2__title` (`font-family` only). Operator CSS preserved (pre-wave `v9-style` `0E1D29F1…` → after `2F7CC5AC…`). `lifebuoy.webp` reserved and untouched (consumed later in E57). DB writes: **0**. Checkpoint: `v9-06e56-fu02-before-libertinus-serif-20260716-210337`. Report: `REPORTS/REPORT-FP-0002-V9-06E56-FU02-libertinus-serif.md`. Evidence: `REPORTS/evidence/v9-06e56-fu02-libertinus-serif/`.

**Prior WordPress phase:** V9-06E56-FU01 Hero/Slider/Font follow-up — **PARTIAL PASS**; **awaiting operator review**; **no freeze**; **no commit**; **no push**. Operator manual CSS preserved (runtime `v9-style` `0003146F…` promoted → source, then additive FU01 → `0E1D29F1…`). Home hero empty-field demo fallback removed; Home hero mobile aspect-ratio aligned to operator `.services-inner-hero-v2__media` (≤767 cascade); service category gallery CSS display aligned to accepted Home gallery (JS already shared). Libertinus Serif was **WAITING_FOR_OPERATOR_ASSET** (completed in FU02). DB writes: **0**. Checkpoint: `v9-06e56-fu01-before-hero-slider-font-follow-up-20260716-191824`. Report: `REPORTS/REPORT-FP-0002-V9-06E56-FU01-hero-slider-font-follow-up.md`. Evidence: `REPORTS/evidence/v9-06e56-fu01-hero-slider-font-follow-up/`.

**Prior WordPress phase:** V9-06E56 Operator Refinements Batch 01 — **PARTIAL PASS**; **awaiting operator review**; **no freeze**; **no commit**; **no push**. Completed: footer OverSEO link; theme metadata+screenshot; unified local lead forms; three image replacements; Home interview video repair (MPEG-TS→MP4); floating Max messenger; gallery/articles slider CSS parity; Comfort admin menu split (same `post_id` storage). Waiting: Libertinus Serif font files (Task D) — later supplied and implemented in FU02. Operator manual CSS/HTML promoted from runtime then preserved (`v9-style` baseline after promote `D12B6348…`; after gallery tweak `BC7AB371…`). Backup: `v9-06e56-before-operator-refinements-batch-01-20260716-181633`. DB writes: footer credit URL option + attachment metadata (images/video); no lead CPT. Report: `REPORTS/REPORT-FP-0002-V9-06E56-operator-refinements-batch-01.md`. Evidence: `REPORTS/evidence/v9-06e56-operator-refinements-batch-01/`.

**Prior WordPress phase:** V9-06E55 Site Settings admin UX styling — **implementation complete**; **awaiting operator visual review**; admin-only visual scope; **DB writes = 0**; no freeze; no commit; no push. Extended E53 enqueue to `fp02-block-*` options screens; added `body.fp02-site-settings-admin` + options-page `.postbox` section/repeater styling (ACF options DOM differs from post edit `.acf-postbox`). Operator CSS `11A45ABE…` preserved; source↔runtime exact-file delivery (2 files). Backup: `v9-06e55-before-site-settings-admin-ux-20260716-162242`. Report: `REPORTS/REPORT-FP-0002-V9-06E55-site-settings-admin-ux.md`. Evidence: `REPORTS/evidence/v9-06e55-site-settings-admin-ux/`. Prior: V9-06E54-FIX01 floating header (awaiting acceptance).

**Prior WordPress phase:** V9-06E54-FIX01 Floating Header background + menu scroll — **implementation complete**; **awaiting operator visual acceptance**; no freeze; no commit; no push. Scoped fixes: floating header background `#e5ecf4`; `initOffcanvas()` scroll-lock preserves `scrollY` when Menu opens from floating header (no page jump). Operator CSS `11A45ABE…` preserved; source↔runtime exact-file delivery (2 files); DB writes **0**. Pre-fix backup: `v9-06e54-fix01-before-background-menu-scroll-fix-20260716-153527`. Report: `REPORTS/REPORT-FP-0002-V9-06E54-FIX01-floating-header-background-menu-scroll.md`. Evidence: `REPORTS/evidence/v9-06e54-fix01-floating-header/`. Prior: V9-06E54 floating header implemented (awaiting acceptance).

**Prior WordPress phase:** V9-06E52–E53 **CLOSEOUT** — E53 admin UX **FREEZE PASS** + E52–E53 scoped Git persistence + Forge Proger experience pack (**documentation only**; **not** integrated into Forge Proger brains/rules). Operator E53 accept: «Ну вот теперь гуд.» Freeze backup: `v9-06e53-admin-ux-section-styling-freeze-accepted-before-experience-pack-20260716-053214`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E53-ADMIN-UX-ACCEPTED.md`. Freeze report: `REPORTS/REPORT-FP-0002-V9-06E53-admin-ux-section-styling-freeze.md`. Experience pack: `DOCS/FORGE-PROGER-EXPERIENCE-PACK/v9-06-batch-01/` (INDEX + 9 docs). Frontend smoke at freeze 12/12 PASS; `#315`/`#78` remain full Услуга (no `placeholder-stack`); generic `#1039`/`#1031` remain `full`; operator CSS `11A45ABE…` preserved; source↔runtime PASS; freeze DB writes **0**. Next: **MIGRATE_WEBGPT_CHAT_TO_FRESH_CHAT**.

**Prior WordPress phase:** V9-06E53 Admin UX section styling **PASS** (local; later frozen in closeout; **0 DB writes**; admin CSS/UX only). Unified `admin-fp02-acf.css` + scoped enqueue for all `page`/`service` edit screens and FP02 Site Settings; `body.fp02-acf-admin`; remove noisy ACF internal field `border-top` inside thematic blocks; keep `.fp02-acf-section-title` major separators; generic pages now receive admin CSS (pre-E53 gap closed). Admin visual 9/9 PASS; frontend regression 14/14 PASS; `#315`/`#78` remain **Услуга**/`service_general`; Home E42 / hub E44 / sections E50 / services E49 / generic E52 preserved; operator CSS `11A45ABE…` preserved; source↔runtime PASS. Backup: `v9-06e53-admin-ux-section-styling-before-20260716-051631`. Report: `REPORTS/REPORT-FP-0002-V9-06E53-admin-ux-section-styling.md`. Evidence: `REPORTS/evidence/v9-06e53-*.csv`. Doc: `DOCS/ADMIN-UX-ACF-SECTION-STYLING-v1.md`.

**Prior WordPress phase:** V9-06E52 Generic pages demo ACF SoT + placeholder **PASS** (local; included in E52–E53 closeout persistence). Ordinary `generic.php` pages (15): ACF `group_fp02_page_generic_content` SoT (`generic_page_lead` / `generic_page_body`); empty optional → hide; hardcoded template demo removed from normal path; `page_layout_mode` full/placeholder (E51 field retained); seeded from page-specific `post_content`; placeholder switch validated on `#1039` (final `full`); empty-field hide PASS on `#14`; regression 15/15; Home E42 / `/uslugi/` E44 / sections E50 / services E49 / E51 service placeholder preserved; operator CSS `11A45ABE…` preserved; source↔runtime 6/6. Backup: `v9-06e52-generic-pages-demo-acf-sot-placeholder-before-20260716-043220`. Report: `REPORTS/REPORT-FP-0002-V9-06E52-generic-pages-demo-acf-sot-placeholder.md`. Evidence: `REPORTS/evidence/v9-06e52-*.csv`. Model: `DOCS/GENERIC-PAGES-ADMIN-PARITY-MODEL-v1.md`.

**Prior WordPress phase:** V9-06E38–E51 accepted WordPress source **Git persistence PASS** (local only; **no push**; **0 DB writes**; **no product mutation**). Selective exact-path commit on `mars/canonical-post-recovery` at HEAD `56e82a05…` before persistence wave; **470** FP-0002 paths staged (theme/plugin/ACF/reports/evidence/docs/validation); excluded INCOMING design binaries, chrome-profile caches, `__pycache__`, large zip/fig. Runtime smoke **19/19 PASS**; `#315`/`#78` **Услуга**/`service_general`; unintended placeholders **0**. Report: `REPORTS/REPORT-FP-0002-V9-06E38-E51-persistence.md`. Evidence: `REPORTS/evidence/v9-06e38-e51-persistence-*.csv`. Next: **OPERATOR_REVIEW_REQUIRED** / optional push charter.

**Prior WordPress phase:** V9-06E49 Full Service Rollout **FREEZE PASS AFTER FIX01** (local only; Git commit skipped; **0 DB writes**; **no product mutation**). Freeze retry after E49-FIX01 restored `#315`. Full freeze backup + inventory/admin/content/FE/regression validation of all publish service CPT. **29/29** inventory PASS; **26/26** individual services `service`/`service_general`; `#315` and `#78` **Услуга**; unintended placeholders **0**; smoke **35/35**; Home E42 / `/uslugi/` E44 / sections E50 / E51 Placeholder Mode preserved; no alcohol copy-paste 26/26; operator CSS `11A45ABE…` preserved; source↔runtime PASS (CSS intentional drift). Freeze backup: `v9-06e49-full-service-rollout-freeze-accepted-after-fix01-before-next-phase-20260716-025224`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E49-FULL-SERVICE-ROLLOUT-ACCEPTED-AFTER-FIX01.md`. Report: `REPORTS/REPORT-FP-0002-V9-06E49-full-service-rollout-freeze-after-fix01.md`. Evidence: `REPORTS/evidence/v9-06e49-freeze-after-fix01-*.csv`.

**Prior WordPress phase:** V9-06E49-FIX01 Restore `#315` service layout **PASS** (local only; Git commit skipped). Restored E49 freeze blocker `#315` Лечение лекарственной зависимости from `placeholder`/`placeholder` → `service`/`service_general` via real wp-admin form POST (`acf[field_…]` + `_acf_nonce`; E51-FIX02 path). Admin shows **Услуга**; FE full service (~113KB, no `placeholder-stack`); ACF content preserved (+4 empty ACF refs allowed); placeholder option still available; unintended placeholders among individual services **0**; controls `#78/#74/#314/#81/#85` + sections `#73/#77/#84` + Home/`/uslugi/` preserved; operator CSS `11A45ABE…` preserved; DB writes **2** (role+layout). Backup: `v9-06e49-fix01-restore-315-service-layout-before-20260716-023509`. Report: `REPORTS/REPORT-FP-0002-V9-06E49-FIX01-restore-315-service-layout.md`. Evidence: `REPORTS/evidence/v9-06e49-fix01-*.csv`.

**Prior WordPress phase:** V9-06E49 Full Service Rollout **FREEZE PARTIAL PASS** (local only; Git commit skipped; **0 DB writes**; **no product mutation**). Operator accepted E49 rollout and requested freeze. Freeze backup + inventory/admin/content/FE/regression validation of all publish service CPT. **25/26** individual services remained `service`/`service_general`; **`#315`** post-E49 drift to `placeholder`/`placeholder` (ACF content still present; not restored — charter forbade layout mutation). Superseded by E49-FIX01 restore. Freeze backup: `v9-06e49-full-service-rollout-freeze-accepted-before-next-phase-20260716-021704`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E49-FULL-SERVICE-ROLLOUT-ACCEPTED.md`. Report: `REPORTS/REPORT-FP-0002-V9-06E49-full-service-rollout-freeze.md`. Evidence: `REPORTS/evidence/v9-06e49-freeze-*.csv`.

**Prior WordPress phase:** V9-06E51 Placeholder Mode **FREEZE PASS** (local only; Git commit skipped). Operator accepted E51-FIX02 («Да, теперь всё гуд»). Frozen: layout mode **Заглушка** (first-level Раздел|Услуга|Заглушка; nested Услуга|Заглушка; generic optional `page_layout_mode` default `full`; FE stub = header/nav/H1/footer; render-only; ACF preserved; real admin save via `acf[field_…]`). `#78` final **Услуга** / `service_general`; Home E42 / `/uslugi/` E44 / sections E50 / services `#74/#314/#81/#85` preserved; operator CSS `11A45ABE…`; source↔runtime sync PASS (CSS intentional drift). Freeze DB writes: **0**. Freeze backup: `v9-06e51-placeholder-mode-freeze-accepted-before-next-phase-20260716-013604`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E51-PLACEHOLDER-MODE-ACCEPTED.md`. Report: `REPORTS/REPORT-FP-0002-V9-06E51-placeholder-mode-freeze.md`. Evidence: `REPORTS/evidence/v9-06e51-freeze-*.csv`.

**Prior WordPress phase:** V9-06E51-FIX02 Real admin placeholder switch **PASS** (local only; Git commit skipped). Operator rejected E51-FIX01 (admin button did not keep Услуга; frontend stayed stub). Real root cause: `prepare_editor_role_field` overwrote ACF prepared input `name` from `acf[field_fp02_service_editor_role]` back to bare `service_editor_role`, so Update posted outside `$_POST['acf']`. Fix: stop rewriting name/key. Validated via authenticated wp-admin form replay (`_acf_nonce` + full fields); `#78` final **Услуга** / `service_general`; frontend full service; content fingerprint unchanged; Home/`/uslugi`/sections/`#74/#314/#81/#85` preserved; operator CSS `11A45ABE…`. Backup: `v9-06e51-fix02-real-admin-placeholder-switch-before-20260716-010437`. Report: `REPORTS/REPORT-FP-0002-V9-06E51-FIX02-real-admin-placeholder-switch.md`. Evidence: `REPORTS/evidence/v9-06e51-fix02-*.csv`.

**Prior WordPress phase:** V9-06E51-FIX01 Placeholder manual switch persistence — **FALSE-POSITIVE for real wp-admin** (meta/`acf_save_post` simulation PASS; operator real admin FAIL). Superseded by FIX02.

**Prior WordPress phase:** V9-06E51 Placeholder / stub layout mode restore **PASS** (local only; Git commit skipped). Restored editor choice **Заглушка** (`service_editor_role=placeholder` → stack `placeholder`); nested pages can select Услуга|Заглушка; true frontend stub (header/nav/H1/footer only) via `placeholder-stack.php`; generic pages gain optional `page_layout_mode`; test-enabled `#78` Депрессия only; ACF content preserved; Home/`/uslugi`/sections/`#74/#314/#81/#85` full layouts preserved; operator CSS preserved (`11A45ABE…`). Backup: `v9-06e51-placeholder-layout-mode-restore-before-20260715-234500`. Report: `REPORTS/REPORT-FP-0002-V9-06E51-placeholder-layout-mode-restore.md`. Evidence: `REPORTS/evidence/v9-06e51-*.csv`. Governance: `DOCS/SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md`.

**Current WordPress phase (prior):** V9-06E50 Service sections (Раздел) demo ACF SoT **FREEZE PASS** (local only; Git commit skipped). Operator accepted E50 («Всё гуд!»). Frozen targets `#73/#77/#84`; ACF `group_fp02_service_section_parity`; normal FE text SoT = page ACF; empty optional → hide/empty-safe; emergency helpers technical-only; `#73` ТЕСТ/000101 preserved; `#77/#84` section-specific headings; Home E42 / `/uslugi/` E44 / Услуга controls+E49 samples preserved; operator CSS preserved (`11A45ABE…`). Freeze DB evidence writes: 2 (temp empty-field clear+restore; no lasting mutation). Freeze backup: `v9-06e50-service-sections-demo-acf-sot-freeze-accepted-before-next-phase-20260715-230201`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E50-SERVICE-SECTIONS-DEMO-ACF-SOT-ACCEPTED.md`. Report: `REPORTS/REPORT-FP-0002-V9-06E50-service-sections-demo-acf-sot-freeze.md`. Evidence: `REPORTS/evidence/v9-06e50-freeze-*.csv`. Model: `DOCS/SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md`. Next: **CREATE_V9_06E49_FULL_SERVICE_ROLLOUT_FREEZE_TASK**.

**Current WordPress phase (prior):** V9-06E50 Service sections (Раздел) demo ACF SoT **PASS** (local only; Git commit skipped). `#73/#77/#84` demo/current texts stored in ACF; normal hardcoded FE demo inject removed (empty → hide/empty-safe); emergency PHP helpers kept technical-only; `#77/#84` section-specific copy (no dependency paste); subnav labels from ACF; Home/`/uslugi` freeze untouched (Home gallery residual order only); services `#74/#314/#78/#81/#85` + E49 samples preserved; operator CSS preserved. DB writes: 21. Backup: `v9-06e50-service-sections-demo-acf-sot-before-20260715-222858`. Report: `REPORTS/REPORT-FP-0002-V9-06E50-service-sections-demo-acf-sot.md`. Evidence: `REPORTS/evidence/v9-06e50-*.csv`. Model: `DOCS/SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md`.

**Current WordPress phase (prior):** V9-06E49 Full service (Услуга) ACF content rollout **PASS** (local only; Git commit skipped). Seeded remaining 21 `service_general` pages with page-title/parent-section/neutral DEMO — **no alcohol copy-paste**; controls `#74/#314/#78/#81/#85` validate-only; sections `#73/#77/#84` untouched; ACF SoT; 589 DB writes; Home/`/uslugi`/Раздел/E47 freeze/E48 reps preserved; E47 field model unchanged; operator CSS preserved (`11A45ABE…`). Backup: `v9-06e49-full-service-rollout-before-20260715-212933`. Report: `REPORTS/REPORT-FP-0002-V9-06E49-full-service-rollout.md`. Evidence: `REPORTS/evidence/v9-06e49-*.csv`. Model: `DOCS/SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md`.

**Current WordPress phase (prior):** V9-06E48 Representative services (Услуга) ACF content rollout **PASS** (local only; Git commit skipped). Staged seed to `#74` (control), `#314` (child tiles), `#78` (ordinary nested), `#81` (psych), `#85` (RPP) with page-specific/neutral DEMO — **no alcohol copy-paste**; ACF SoT; 107 DB writes; Home/`/uslugi`/Раздел freeze preserved; E47 Услуга field model unchanged; operator CSS preserved. Backup: `v9-06e48-representative-services-rollout-before-20260715-203048`. Report: `REPORTS/REPORT-FP-0002-V9-06E48-representative-services-rollout.md`. Evidence: `REPORTS/evidence/v9-06e48-*.csv`. Model: `DOCS/SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md`.

**Current WordPress phase (prior):** V9-06E47 Service general (Услуга) freeze **PASS** (local only; Git commit skipped). Operator accepted E47-FIX04 («Да всё гуд.»). Full freeze backup of DB/theme/plugin/ACF JSON/uploads + postmeta/#74/#314/#78/#73/#77/#84 + frontend snapshots + admin/filter/read-more validation. Page type **Услуга** (`service_general`) is **frozen** pending explicit change request. Home/`/uslugi`/Раздел untouched; representative `#314/#78` preserved; operator CSS drift preserved. Backup: `v9-06e47-service-general-freeze-accepted-before-next-phase-20260715-175228`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E47-SERVICE-GENERAL-ACCEPTED.md`. Report: `REPORTS/REPORT-FP-0002-V9-06E47-service-general-freeze.md`. Model: `DOCS/SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md`.

**Current WordPress phase (prior):** V9-06E47-FIX04 Service signs editorial read-more toggle **PASS** (local only; Git commit skipped). Operator correction on FIX03: after expand, button stays visible as «Скрыть»; second click collapses to 5 lines and restores «Читать больше»; smooth max-height both ways; resize recalculates overflow. JS-only in `v9-shell.js`; no CSS/PHP/admin/DB writes. Validated alcohol `#74` tablet (native overflow + long-text sim + short-text sim); `#314/#78` no signs block; Home/`/uslugi/`/Раздел untouched; operator CSS untouched (hash drift preserved). Backup: `v9-06e47-fix04-service-signs-readmore-toggle-before-20260715-170136`. Report: `REPORTS/REPORT-FP-0002-V9-06E47-FIX04-service-signs-readmore-toggle.md`.

**Current WordPress phase (prior):** V9-06E47-FIX03 Service signs editorial 5-line clamp + «Читать больше» **PASS** (local only; Git commit skipped). Frontend-only: `.service-leaf-signs-v1__editorial` clamped to 5 lines when overflowing; `.service-leaf-signs-v1__read-more` is a real button shown only on overflow; smooth expand then hide. No admin/DB writes. Validated alcohol `#74` (desktop ≤5 lines hides button; tablet/mobile >5 lines clamp+expand); short-text sim without DB mutation; Home/`/uslugi/`/Раздел untouched; operator CSS dual-patched (hash drift preserved). Backup: `v9-06e47-fix03-service-general-signs-readmore-before-20260715-160233`. Report: `REPORTS/REPORT-FP-0002-V9-06E47-FIX03-service-signs-readmore.md`.

**Current WordPress phase (prior):** V9-06E47-FIX02 Service general ACF group render + metabox cleanup **PASS** (local only; Git commit skipped). Root cause: nested FIX03 converts `service_editor_role` → message/empty name, so field-level `when_service` conditionals hid all 68 fields in «Услуга — блоки страницы». Fix: disable field conditionals (group filter remains SoT); hide `revisionsdiv`/`postexcerpt` on service CPT. Alcohol/`/uslugi/` fingerprints equal; Home gallery residual only; section `#73` preserved; operator CSS unchanged (`C858903F…`). Backup: `v9-06e47-fix02-service-general-acf-render-before-20260715-133411`. Report: `REPORTS/REPORT-FP-0002-V9-06E47-FIX02-service-general-acf-render.md`.

**Current WordPress phase (prior):** V9-06E47-FIX01 Service general (Услуга) admin UX cleanup for `#74` **PASS** (local only; Git commit skipped). Hide legacy Structured/FAQ/Relationships (+ opposite Раздел) for role=Услуга; rename layout group to «Макет страницы услуги»; clean order Layout→Hero→«Услуга — блоки страницы»; mid-cta `cta_*` mirrored into parity (meta preserved); DB duplicate legacy ACF groups soft-disabled (6). Alcohol/`/uslugi/` fingerprints preserved; Home gallery order non-deterministic residual only; section model regression-free; operator runtime CSS unchanged (`C858903F…`). Backup: `v9-06e47-fix01-service-general-admin-ux-cleanup-before-20260715-125222`. Report: `REPORTS/REPORT-FP-0002-V9-06E47-FIX01-service-general-admin-ux-cleanup.md`. Model: `DOCS/SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md`.

**Current WordPress phase (prior):** V9-06E47 Service general (Услуга) admin parity for base page Лечение алкогольной зависимости `#74` **PASS** (local only; Git commit skipped). New ACF group `group_fp02_service_general_parity` («Услуга — блоки страницы», 64 fields, frontend order 1–18); alcohol PHP static → ACF with emergency-only fallbacks; service-specific images `service_general_team_image` / `clinic_landscape` / `corridor` seeded `#1238/#1239/#1709`; opposite Раздел group hidden by role filter; `#314/#78` images seeded without alcohol copy; Home/`/uslugi/` freeze untouched; section model regression-free; operator runtime CSS unchanged. Backup: `v9-06e47-service-general-admin-parity-alcohol-before-20260715-114038`. Report: `REPORTS/REPORT-FP-0002-V9-06E47-service-general-admin-parity-alcohol.md`. Model: `DOCS/SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md`.

**Current WordPress phase (prior):** V9-06E46-FIX05 section demo data + no template fallback **PASS** (local only; Git commit skipped). Seeded empty section ACF fields on `#73/#77/#84` from current FE fallbacks; `section_team_image` / `section_corridor_image` (seeded `#1238` / `#1709`); landscape `#1239` retained; admin wording no longer presents template/Home as normal SoT; emergency PHP fallbacks remain as safety net only. Home/`/uslugi/` freeze untouched; operator CSS unchanged. Backup: `v9-06e46-fix05-section-demo-data-no-template-fallback-before-20260715-004351`. Report: `REPORTS/REPORT-FP-0002-V9-06E46-FIX05-section-demo-data-no-template-fallback.md`. Model: `DOCS/SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md`.

**Current WordPress phase (prior):** V9-06E46-FIX04 Section admin cleanup + landscape image **PASS** (local only; Git commit skipped). Hid `Текст нижней ссылки программы` from section admin (meta kept; FE fallback/stored); added section-specific `section_clinic_landscape_image` (seeded #73/#77/#84 from Home #1239); updated clinic-landscape partial to prefer section field on Раздел pages; hid Classic Editor `#postdivrich` for service CPT. Home/`/uslugi/` freeze untouched; operator CSS unchanged. Backup: `v9-06e46-fix04-section-admin-cleanup-landscape-before-20260715-002138`. Report: `REPORTS/REPORT-FP-0002-V9-06E46-FIX04-section-admin-cleanup-landscape.md`. Model: `DOCS/SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md`.

**Current WordPress phase (prior):** V9-06E46-FIX03 Section CTA cleanup + program fallback **PASS** (local only; Git commit skipped). Removed ineffective admin § CTA «Раздел услуги» (toggle/meta kept legacy default-ON); renumbered sections 5–14; fixed program intro/footer demo fallback so user values win and empty→FE demo only; `#73` intro repeater re-seeded from legacy (FE preserved); `#77/#84` not overwritten; Home templates / `/uslugi/` freeze untouched; operator CSS unchanged. Backup: `v9-06e46-fix03-section-cta-program-fallback-before-20260714-234056`. Report: `REPORTS/REPORT-FP-0002-V9-06E46-FIX03-section-cta-program-fallback.md`. Model: `DOCS/SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md`.

**Current WordPress phase (prior):** V9-06E46-FIX02 Service section repeaters/stages **PASS** (local only; Git commit skipped). §3→«Дочерние услуги»; §5→CTA «Раздел услуги»; `section_nature_text_blocks` + `section_program_intro_items` + `section_stages_items` repeaters; fixed `stages.php` PHP leak; `#73` seeded; `#77/#84` compatible without overwrite; Home templates / `/uslugi/` freeze untouched; operator CSS unchanged. Backup: `v9-06e46-fix02-section-repeaters-stages-before-20260714-225532`. Report: `REPORTS/REPORT-FP-0002-V9-06E46-FIX02-service-section-repeaters-stages.md`. Model: `DOCS/SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md`.

**Current WordPress phase (prior):** V9-06E46-FIX01 Service section hero/admin separation **PASS** (local only; Git commit skipped). Split mixed `Service — Layout and Hero` into **Service — Layout** + **Hero страницы услуги** (`group_fp02_service_hero`); meta keys preserved; DB duplicate mixed groups soft-disabled; `#73` frontend fingerprint unchanged; Home 74 fields / `/uslugi/` freeze untouched. Backup: `v9-06e46-fix01-service-section-hero-admin-separation-before-20260714-214425`. Report: `REPORTS/REPORT-FP-0002-V9-06E46-FIX01-service-section-hero-admin-separation.md`.

**Current WordPress phase (prior):** V9-06E46 Service section (Раздел) admin parity for base page Зависимости `#73` **PASS** (local only; Git commit skipped). New ACF group `group_fp02_service_section_parity` (63 fields, frontend order 1–15); hardcoded nature/approach/program/stages/dependencies chrome → ACF with fallbacks; block toggles + source notices; `#73` seeded; `#77/#84` toggles ON with empty content (fallback); reviews home-toggle leak fixed. Home/`/uslugi/` freeze untouched; operator CSS unchanged. Backup: `v9-06e46-service-section-admin-parity-zavisimosti-before-20260714-210729`. Report: `REPORTS/REPORT-FP-0002-V9-06E46-service-section-admin-parity-zavisimosti.md`. Model: `DOCS/SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md`.

**Current WordPress phase (prior):** V9-06E45-FIX03 service layout selector simplification by depth **PASS** (local only; Git commit skipped). One admin block «Макет страницы услуги»: first-level selector Раздел/Услуга; nested auto «Услуга» notice; override + technical dropdown hidden. Depth helper + save sync; nested cleanup (incl. `#74` section/subdivision → service/service_general correction). Home/`/uslugi/` freeze unchanged (hub whitespace-normalized equal). Backup: `v9-06e45-fix03-service-layout-selector-simplification-before-20260714-202448`. Report: `REPORTS/REPORT-FP-0002-V9-06E45-FIX03-service-layout-selector-simplification.md`. Governance: `DOCS/SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md`.

**Current WordPress phase (prior):** V9-06E45-FIX02 Rename technical layout `alcohol_special` → `service_general` **PASS** (local only; Git commit skipped). Active technical value for Услуга stack is `service_general` (admin label «Услуга»). `alcohol_special` retained as resolver/save legacy alias only (not selectable). Migrated 26 service posts; `#74` → service_general with alcohol static copy still gated by page ID. Home `#1338` untouched; `/uslugi/` hub bytes unchanged. Backup: `v9-06e45-fix02-rename-alcohol-special-before-20260714-183309`. Report: `REPORTS/REPORT-FP-0002-V9-06E45-FIX02-rename-alcohol-special-layout.md`. Governance: `DOCS/SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md`.

**Current WordPress phase (prior):** V9-06E45-FIX01 Service layout model simplification + child services tile **PASS** (local only; Git commit skipped). Two editor types only (`Раздел` / `Услуга`); `placeholder` demoted from primary choices. Override-off mapping: section→`subdivision`, service→`alcohol_special` (general service stack). Alcohol static V9 copy gated to `#74`. Child services tile block before FAQ when published children exist. Roots `#73/#77/#84` remain sections. `#314/#316` set to service (not sections). Home `#1338` untouched; `/uslugi/` hub visual restored (child CSS scoped to service singular). Backup: `v9-06e45-fix01-service-layout-model-before-20260714-180233`. Report: `REPORTS/REPORT-FP-0002-V9-06E45-FIX01-service-layout-model-and-child-services.md`. Governance: `DOCS/SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md`.

**Current WordPress phase (prior):** V9-06E45 Service layout variant implementation (Option B) **PASS** (local only; Git commit skipped). Editor-facing `service_editor_role` (Раздел услуг / Услуга / Заглушка) + `service_layout_override_enabled` + reframed `service_layout_variant` as advanced technical template. Seeded 29 services (0 technical layout mass changes; alcohol `#74` override on). Mismatches `#314/#316` documented/warned, not auto-fixed. Frontend stacks preserved; Home `#1338` 74 fields untouched; `/uslugi/` hub routes 200. Backup: `v9-06e45-service-layout-variant-implementation-before-20260714-163201`. Report: `REPORTS/REPORT-FP-0002-V9-06E45-service-layout-variant-implementation.md`. Governance: `DOCS/SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md`.

**Current WordPress phase (prior):** V9-06E44 Services hub freeze + service layout variant governance **PASS** (local only; Git commit skipped). `/uslugi/` accepted state frozen (backup `v9-06e44-services-hub-freeze-before-layout-governance-20260714-051559`). Layout audit: ACF `service_layout_variant` keeps 5 internal values; frontend-significant = `subdivision` + `alcohol_special`; `standard`/`extended`/`placeholder` all map to leaf. Admin help block + nesting mismatch warnings added (no value migration). Recommended model **Option B**. Home freeze E42 untouched (74 fields). Report: `REPORTS/REPORT-FP-0002-V9-06E44-services-freeze-layout-variant-governance.md`. Freeze: `REPORTS/FREEZE-FP-0002-V9-06E44-SERVICES-HUB-ACCEPTED.md`. Governance: `DOCS/SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md`.

**Current WordPress phase (prior):** V9-06E43-FIX01 Services category intro/lead fields **PASS** (local only; Git commit skipped). Category sections on `/uslugi/` now read `.services-category-section-v2__intro` from root service `Мини-описание` (`service_short_description`) and `.services-category-section-v2__lead` from new `service_category_section_lead` (visible for `subdivision`). Root services `#73/#77/#84` seeded from prior V9 hardcoded copy; frontend visual preserved. Home freeze E42 untouched (74 fields). Report: `REPORTS/REPORT-FP-0002-V9-06E43-FIX01-services-category-intro-lead-fields.md`. Evidence: `REPORTS/evidence/v9-06e43-fix01-*.csv`. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e43-fix01-services-category-intro-lead-before-20260714-044434\`.

**Current WordPress phase (prior):** V9-06E43 Services hub (`/uslugi/`) admin parity **PASS** (local only; Git commit skipped). Applied Home admin-parity model to Services hub page #5: frontend block audit → ACF group `#1628` (`group_fp02_page_services_hub`, 38 fields, RU/i18n), local hero slider (`services_hero_slides`, services-inner-hero-v2 design preserved), non-repeated editable fields, toggles/settings for automated blocks, admin notices with source links. Home freeze E42 untouched (group `#1338`, 74 fields). Route smoke 9/9 PASS. Report: `REPORTS/REPORT-FP-0002-V9-06E43-services-hub-admin-parity.md`. Model: `DOCS/SERVICES-HUB-ADMIN-PARITY-MODEL-v1.md`. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e43-services-hub-admin-parity-before-20260714-040826\`.

**Current WordPress phase (prior):** V9-06E42 Home freeze + admin parity summary **PASS** (local only; Git commit skipped). Operator accepted Home as finished. Full local freeze backup + STORAGE evidence export; Home frontend/admin validation PASS; architecture model + freeze marker created. **Home page is frozen** pending explicit change request. Report: `REPORTS/REPORT-FP-0002-V9-06E42-home-freeze-admin-parity-summary.md`. Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E42-HOME-ACCEPTED.md`. Architecture: `DOCS/HOME-PAGE-ADMIN-PARITY-MODEL-v1.md`. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e42-home-freeze-accepted-before-next-page-types-20260714-033407\`. Evidence: `X:\AI MARS STORAGE\exports\fp-0002-shpigovsky-home-freeze\v9-06e42-home-freeze-20260714-033407\`.

**Current WordPress phase (prior):** V9-06E41-FIX01 Hero multi-slide height + Home rehab program intro admin fields **PASS** (local only; Git commit skipped). Fixed `.hero--home-slider` height collapse (must not override `.hero--home` 70vh); Home ACF fields for rehab head/lead/intro_1/intro_2 seeded from frontend; admin notice HTML with red/bold + link to program page edit. Report: `REPORTS/REPORT-FP-0002-V9-06E41-FIX01-hero-height-rehab-program-intro.md`. Evidence: `REPORTS/evidence/v9-06e41-fix01-*.csv`. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e41-fix01-hero-height-rehab-intro-before-20260714-024847\`.

**Current WordPress phase (prior):** V9-06E41 Home admin hero slider, automated block toggles, recovery life stage markup **PASS** (local only; Git commit skipped). Home admin section titles ~20px (scoped CSS); Hero multi-slide Swiper from `home_hero_slides` + autoplay/arrows/dots settings; standalone `hero_media` retired/hidden (meta kept); Home visibility toggles for automated/external blocks; recovery-life stage wrapper/inner + month labels. Report: `REPORTS/REPORT-FP-0002-V9-06E41-home-admin-hero-toggles-recovery-life.md`. Evidence: `REPORTS/evidence/v9-06e41-*.csv`. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e41-home-admin-hero-toggles-recovery-life-before-20260714-015935\`.

**Current WordPress phase (prior):** V9-06E40 Home admin editable blocks expansion **PASS** (local only; Git commit skipped). Home ACF expanded for recovery benefits, treatment heading/lead, gallery display modes, why-us, staff/landscape images, recovery-life, genotyping, and Media Library videos; frontend wired from ACF with fallbacks; RU i18n-ready labels. Report: `REPORTS/REPORT-FP-0002-V9-06E40-home-admin-editable-blocks-expansion.md`. Evidence: `REPORTS/evidence/v9-06e40-*.csv`. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e40-home-admin-editable-blocks-before-20260714-010957\`.

**Current WordPress phase (prior):** V9-06E39 Home admin order + localization foundation **PASS** (local; Git commit skipped). Home ACF admin field order aligned to `front-page.php` partial sequence; Home labels/instructions/notices wrapped in `shpigovsky-core` i18n (RU source strings); plugin `load_plugin_textdomain` + foundation POT files added. Frontend Home preserved (section order + HTTP 200). Report: `REPORTS/REPORT-FP-0002-V9-06E39-home-admin-order-localization.md`. Evidence: `REPORTS/evidence/v9-06e39-*.csv`. Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e39-home-admin-order-localization-before-20260714-001557\`.

**Current WordPress phase (prior):** V9-06E38 / E38-FIX01 Home admin parity + orphan hygiene **accepted locally** (not selectively persisted in this note). V9-06E36 + V9-06E37 Home mobile polish **PASS** + selective persistence checkpoint (`e93a4ca3…`). V9-06E29C–E35-FIX01 selective Git persistence **PASS** (temp branch tip `f77ee7eb…`).

## Active frontend workspace (V9)

| Field | Value |
|-------|-------|
| Workspace | `workspaces/fp-0002-shpigovsky-v9/` |
| Static baseline | `FP0002_V9_OPERATOR_APPROVED_STATIC_FRONTEND_STABLE_BASELINE_COMPLETE` |
| Intake pack | `FP0002_V9_FORGE_WORDPRESS_INTAKE_PACK_COMPLETE` |
| Intake gate (V9-05A) | `FP0002_V9_APPROVED_FRONTEND_INTAKE_APPROVED` |
| WordPress foundation | **ADOPTED** — prepared MLI site, not legacy discard |
| Phase | V9-05A complete → **V9-05B pre-implementation checkpoint** |
| Dist output | Clean-route static site in `dist/` (root-relative `/assets/...`) |
| Route manifest | `workspaces/fp-0002-shpigovsky-v9/tools/v9-route-manifest.json` (31 routes) |
| Forge intake pack | `workspaces/fp-0002-shpigovsky-v9/forge-intake/` |
| Intake tag | `fp-0002-v9-forge-wordpress-intake-pack-01` |
| Stable tag | `fp-0002-v9-operator-approved-static-frontend-stable-01` @ `a51376872fbfefb7d5f68a58b440c726d6cf3de3` |
| WordPress implementation | **Not started** |

## Phase 07C-B static package — SUPERSEDED

| Field | Value |
|-------|-------|
| Package | `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\FP-0002-V8-STATIC-CLIENT-DEMO-1-OPERATOR-REVIEW\` |
| Status | `SUPERSEDED_FAILED_STATIC_PACKAGING_NOT_FOR_FORGE_NOT_FOR_CLIENT` |
| Defect | Nested routes resolved `assets/...` relative to page depth — CSS/JS/fonts failed on nested URLs |
| Replacement | V9 workspace native `dist/` clean routes |
| Note | Package retained as historical evidence only — not Forge authority, not for client |

## Historical stable baseline (V8)

| Field | Value |
|-------|-------|
| Baseline | [FP-0002-V8-OPERATOR-APPROVED-FRONTEND-BASELINE-01.md](FP-0002-V8-OPERATOR-APPROVED-FRONTEND-BASELINE-01.md) |
| Tag | `fp-0002-v8-operator-approved-frontend-stable-01` |
| Parent | `eeab3d68` · `fp-0002-v8-blog-full-stable-01` |
| Recovery pack | `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\FP-0002-V8-OPERATOR-APPROVED-FRONTEND-STABLE-01\` |
| Next | Phase 07C-B static demo assembly (blocked on operator gate) · deferred operator polish · Forge WP |
| Phase 07B | [REPORT-FP-0002-V8-PHASE-07B-DOCUMENTATION-AND-LESSONS-LEARNED-v1.md](REPORT-FP-0002-V8-PHASE-07B-DOCUMENTATION-AND-LESSONS-LEARNED-v1.md) · [FP-0002-V8-IMPLEMENTATION-GUIDE-v1.md](FP-0002-V8-IMPLEMENTATION-GUIDE-v1.md) |
| Phase 07C-A | [REPORT-FP-0002-V8-PHASE-07C-A-EXCEL-DEMO-RECONCILIATION-v1.md](REPORT-FP-0002-V8-PHASE-07C-A-EXCEL-DEMO-RECONCILIATION-v1.md) · evidence `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\phase-07c-a-excel-demo-reconciliation\` · **operator gate pending** |

## ACTIVE TEMPORARY PRIORITY RULE

Before any FP-0002 frontend implementation, read:

[`FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md`](FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md)

- **Visual PASS:** OPERATOR ONLY
- **Commit before operator visual approval:** PROHIBITED
- **Mandatory report header:** REQUIRED
- **Web-GPT recovery source:** THIS PROTOCOL

## V8 workspace (2026-06-29)

| Field | Value |
|-------|-------|
| Workspace | `workspaces/fp-0002-shpigovsky-v8/` |
| Branch | `mars/canonical-post-recovery` |
| CF-011 dark CTA | COMPLETE — commit `4d98d6fb` |
| CF-012 program modifiers | COMPLETE — commit `9e8fa083` |
| Operator manual polish | OPERATOR_MANUAL_POLISH_CANONICAL |
| Visual authority | V8 working source post manual polish |
| CF-003–CF-012 | APPROVED |
| Next wave | CF-010 clinic landscape — **NOT STARTED** |
| Page-wide DOM gate | PASS |
| O-Centre | **STABLE_PREVIOUSLY_APPROVED** in operator baseline — historical audit [FP-0002-OCENTRE-VISUAL-AUDIT-STATUS-v1.md](FP-0002-OCENTRE-VISUAL-AUDIT-STATUS-v1.md) superseded by baseline |
| Priority visual protocol | **ACTIVE** — [FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md](FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md) |

## Workspace versions (2026-06-24)

| Workspace | Path | Lifecycle | Tag / parent |
|-----------|------|-----------|--------------|
| **V6** | `workspaces/fp-0002-shpigovsky-v6/` | **FROZEN_FALLBACK** | `fp-0002-v6-final-before-v7-operator-stable-01` |
| **V7** | `workspaces/fp-0002-shpigovsky-v7/` | **IMMUTABLE_STABLE_FALLBACK** | `fp-0002-v7-pre-final-polish-operator-stable-01` |
| **V8** | `workspaces/fp-0002-shpigovsky-v8/` | **OPERATOR_APPROVED_BASELINE** | `fp-0002-v8-operator-approved-frontend-stable-01` @ `eb47ebb` |

```text
V7 design authority: workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig
V7 design authority SHA-256: BAE5D91C74B5A22AFC610F7C7845B9BADC6B87EC8DA85C5705ECF4EEC4DE3041
Historical Figma (Шпиговский.fig): DO NOT USE FOR NEW WORK
Factory Figma rules: projects/mars-website-factory/figma-inspection-authority-rules-v1.md
package_001: COMPLETE_PENDING_OPERATOR_FINAL_REVIEW
package_001_phase_1_figma_rules: COMPLETE
package_001_phase_2_head: TECHNICALLY_COMPLETE
package_001_phase_3a_intro_content: COMPLETE
package_001_phase_3b_founder_quote_svg: COMPLETE
package_001_phase_3b_gallery_captions: COMPLETE
package_001_phase_3c_recovery_life: DESKTOP_COMPLETE
package_001_phase_3c_mobile: MOBILE_RESPONSIVE_DERIVED_COMPLETE
package_001_phase_4a_spacing_cleanup: COMPLETE
package_001_phase_9_global_polish: COMPLETE_PENDING_OPERATOR_FINAL_REVIEW
gallery_captions: POSITION_BELOW_IMAGE — COMPLETE
recovery_life: DESKTOP_COMPLETE / MOBILE_RESPONSIVE_DERIVED_COMPLETE
section_spacing_cleanup: COMPLETE
global_visual_polish: COMPLETE_PENDING_OPERATOR_FINAL_REVIEW

operator_manual_checkpoint:
  date: 2026-06-26
  status: COMPLETE
  committed: true
  pushed: true
  commit: 95b97adf

package_002: COMPLETE_PENDING_OPERATOR_REVIEW
external_link_svg: COMPLETE
hero_architecture: HOME_COMPLETE / INNER_PAGE_BASE_COMPLETE / MOBILE_RESPONSIVE_COMPLETE
slider_pagination: COMPLETE
home_videos: COMPLETE
faq_filler: COMPLETE_TEMPORARY_CONTENT
home_recovery_intro_text: FIGMA_EXACT_COMPLETE

operator_checkpoint_before_package_003:
  date: 2026-06-26
  status: NOT_REQUIRED
  backup_sha256: 3BE9ADAA1B35FD27DC5E4F0CAA3CFB34667A18B818511F4EC5A51247B37C0E75

package_003: TECHNICALLY_ACCEPTED
package_003_commit: c74bb04d
video_posters: REAL_VIDEO_FRAMES_COMPLETE
hero_container_gutters: COMPLETE
founder_quote_current_variant: variant-b
founder_quote_variant_a: PRESERVED_FALLBACK
founder_quote_variant_b: ACTIVE_ON_HOME
treatment_service_icons: COMPLETE

home_operator_manual_polish: ACCEPTED_AS_CURRENT_BASELINE
home_source_authority: OPERATOR_CANONICAL
home_visual_style_audit: COMPLETE
home_visual_baseline: DOCUMENTED
component_reuse_map: COMPLETE
source_universalization: NOT_STARTED
services_general_source_reconciliation: COMPLETE
services_general_design_mapping: COMPLETE
services_general_build_plan: COMPLETE
services_general_implementation_pass_1: COMPLETE_PENDING_OPERATOR_REVIEW
services_general_implementation_pass_2: COMPLETE_PENDING_OPERATOR_REVIEW
services_general_inner_hero: FINAL_ASSET_COMPLETE
services_general_reuse_section_order: COMPLETE
services_general_category_hubs: FOUR_IMPLEMENTED
services_general_unique_assets: FIGMA_EXPORT_COMPLETE
services_general_page: PASS_2_CATEGORY_HUBS_COMPLETE
services_general_clean_build: PASS
services_general_assets: FIGMA_EXPORT_COMPLETE
services_general_home_regression: NONE_DETECTED
services_general_content_safe_unknowns:
  - Genotyping hub lead paragraphs (Figma lorem only)
  - Mental health per-service descriptions (Figma lorem excluded)
  - Eating disorders per-service descriptions (Figma lorem excluded)
services_general_final_polish: COMPLETE_PENDING_OPERATOR_REVIEW
services_general_visual_parity: COMPLETE_WITH_DOCUMENTED_SAFE_UNKNOWNS
services_general_clean_build: PASS_WITH_CLEAN_DIST_ENVIRONMENT_CAVEAT
services_general_home_regression: NONE_DETECTED
services_general_untracked_asset_cleanup: PROBE_CLEANUP_COMPLETE_17_FILES_REMOVED
services_general_stable_freeze: NOT_STARTED
services_general_pass_2: COMPLETE_PENDING_OPERATOR_REVIEW
services_figma_mcp_connection: VERIFIED
services_figma_mcp_live_file_read: BLOCKED_NO_FILEKEY
services_figma_target_frames: VERIFIED_OFFLINE
services_page_anatomy: COMPLETE
services_breadcrumbs: IDENTIFIED
services_page_subnav: IDENTIFIED
services_v1_differential: COMPLETE
services_v2_decision: HYBRID_RECONSTRUCTION
services_v1: PRESERVED_FALLBACK
services_v2_strategy: HYBRID_RECONSTRUCTION
services_v2_block_1: ACCEPTED_WORKING_BASE
services_v2_block_2a: CORRECTED_AND_INTEGRATED
services_v2_block_2b: COMPLETE_PENDING_OPERATOR_REVIEW
services_v2_category_structure: COMPLETE
services_v2_category_content_fidelity: SUPERSEDED_BY_MOCKUP_COPY_PASS
services_v2_category_text_recovery: SUPERSEDED_BY_MOCKUP_COPY_PASS
services_v2_category_mockup_copy_population: COMPLETE
services_v2_runtime_content_population: COMPLETE
services_v2_empty_content_slots: ZERO
services_v2_visible_mockup_text_omissions: ZERO
services_v2_temporary_mockup_copy: PRESENT_AND_DOCUMENTED
services_v2_production_copy_replacement: FUTURE_SEPARATE_PASS
services_v2_true_visible_placeholders: 0
services_v2_premature_compaction: REMOVED_OR_CORRECTED
services_v2_category_geometry: CONTENT_DRIVEN
services_v2_mockup_copy_review: workspaces/fp-0002-shpigovsky-v7/reviews/services-v2-exact-mockup-copy/
services_v2_text_recovery_review: workspaces/fp-0002-shpigovsky-v7/reviews/services-v2-category-text-recovery/
services_v2_category_family: COMPLETE_PENDING_OPERATOR_POLISH
services_v2_mockup_copy_policy: ALL_VISIBLE_TEXT_INCLUDED
services_v2_hero_layout: CORRECTED_PENDING_OPERATOR_REVIEW
services_v2_gallery_media_height: NORMALIZED
services_v2_program_dom: BODY_BEFORE_MEDIA
services_v2_program_card_pattern: HOME_DIRECTION_STYLE_REUSED
services_v2_program: COMPLETE_PENDING_OPERATOR_REVIEW
services_v2_program_mockup_text: COMPLETE
services_v2_program_empty_content_slots: ZERO
services_v2_program_component: SERVICES_SPECIFIC_REUSABLE_PARTIAL
services_v2_root_tokens_added: ZERO
services_v2_program_item_descriptions: REMOVED_BY_OPERATOR_DECISION
services_v2_founder: HOME_FOUNDER_QUOTE_REUSED
services_v2_comfort: HOME_COMFORT_REUSED
services_v2_mid_page_cta: SECOND_PROGRAM_CTA_BAND_REUSED
services_v2_faq: HOME_FAQ_REUSED
services_v2_final_form: HOME_FINAL_FORM_REUSED
services_v2_lower_page_assembly: COMPLETE_PENDING_OPERATOR_REVIEW
services_v2_visible_mockup_text_policy: ACTIVE
services_v2_root_tokens_added: ZERO
services_v2_v1: PRESERVED_FALLBACK
services_v2_navigation_switch: NOT_STARTED
services_v2_founder_comfort_cta_superseded: SUPERSEDED_NOT_IN_RUNTIME
services_v2_final_assembly_review: workspaces/fp-0002-shpigovsky-v7/reviews/services-v2-final-lower-assembly/
services_v2_operator_acceptance: CONDITIONAL_ACCEPTED_REFERENCE
services_v2_reference_type: SERVICES_HUB_INTERNAL_PAGE
services_v2_lifebuoy_decor: REMOVED_BY_OPERATOR_DECISION
services_v2_detail_links: HOME_REHABILITATION_PATTERN_REUSED
services_v2_reference_baseline: READY_FOR_FREEZE
services_v2_canonical_switch: NOT_STARTED
services_v2_reference_freeze_review: workspaces/fp-0002-shpigovsky-v7/reviews/services-v2-reference-freeze/
service_subdivision_planning: workspaces/fp-0002-shpigovsky-v7/plans/service-subdivision-page/
service_subdivision_page: IN_IMPLEMENTATION
service_subdivision_pass_1_intro: REMOVED_BY_OPERATOR_DECISION
service_subdivision_primary: REMOVED_BY_OPERATOR_DECISION
service_subdivision_upper_structure: RECONSTRUCTED_FROM_FIGMA
service_subdivision_subnav_border: CANONICAL_EXISTING_TOKEN
service_subdivision_anchor_map: VALID
service_subdivision_pass_1: CORRECTED_AND_INTEGRATED
service_subdivision_intro_markup: SUPERSEDED_NOT_IN_RUNTIME
service_subdivision_optional_regions: CONDITIONAL_RENDERING_ENABLED
service_subdivision_primary_content: REMOVED_BY_OPERATOR_DECISION
service_subdivision_pass_2: COMPLETE
service_subdivision_nature: PRESERVED
service_subdivision_info_cards: PRESERVED
service_subdivision_first_cta: PRESERVED
service_subdivision_program: PRESERVED
service_subdivision_visible_mockup_text_policy: ACTIVE
service_subdivision_lifebuoy_decor: FORBIDDEN_ZERO
service_subdivision_root_tokens_added: ZERO
service_subdivision_pass_3: COMPLETE
service_subdivision_hero_inner_alignment: CANONICAL_CONTAINER_ALIGNED
service_subdivision_dependencies: IMPLEMENTED_FROM_FIGMA
service_subdivision_nature_lead: CANONICAL_EXISTING_PATTERN_REUSED
service_subdivision_team_stats: HOME_FEATURE_GRID_PATTERN_REUSED
service_subdivision_specialists: COMPLETE_PENDING_OPERATOR_REVIEW
service_subdivision_founder: COMPLETE_PENDING_OPERATOR_REVIEW
service_subdivision_comfort: COMPLETE_PENDING_OPERATOR_REVIEW
service_subdivision_reviews: COMPLETE_PENDING_OPERATOR_REVIEW
service_subdivision_faq: COMPLETE_PENDING_OPERATOR_REVIEW
service_subdivision_final_form: COMPLETE_PENDING_OPERATOR_REVIEW
service_subdivision_full_page: STRUCTURALLY_COMPLETE_PENDING_OPERATOR_REVIEW
service_subdivision_temporary_boundaries: ZERO
service_subdivision_pass_4: INTEGRATED_INTO_FINAL_LOWER_PASS
service_subdivision_final_lower_pass_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-subdivision-final-lower-pass/
service_subdivision_pass_3_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-subdivision-pass-3/
service_subdivision_stages: IMPLEMENTED
service_subdivision_second_cta: IMPLEMENTED
service_subdivision_approach: IMPLEMENTED
service_subdivision_center_visual: IMPLEMENTED
service_subdivision_pass_1_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-subdivision-pass-1/
service_subdivision_pass_2_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-subdivision-pass-2/
service_subdivision_png_group_1: COMPLETE
service_subdivision_png_group_2: COMPLETE
service_subdivision_cta_01: PNG_MATCH_COMPLETE
service_subdivision_program: PNG_MATCH_COMPLETE
service_subdivision_cta_02: PNG_MATCH_COMPLETE
service_subdivision_group_2_desktop: PASS
service_subdivision_group_2_mobile: PASS
service_subdivision_png_group_3: COMPLETE
service_subdivision_rehabilitation_stages: PNG_MATCH_COMPLETE
service_subdivision_rehabilitation_support: PNG_MATCH_COMPLETE
service_subdivision_group_3_desktop: PASS
service_subdivision_group_3_mobile: PASS
service_subdivision_png_group_4: COMPLETE
service_subdivision_team_center: PNG_MATCH_COMPLETE
service_subdivision_team_stats: PNG_MATCH_COMPLETE
service_subdivision_corridor_interior: PNG_MATCH_COMPLETE
service_subdivision_group_4_empty_media: ZERO
service_subdivision_group_4_artificial_blank_zones: ZERO
service_subdivision_group_4_desktop: PASS
service_subdivision_group_4_mobile: PASS
service_subdivision_remaining_groups: ZERO
service_subdivision_full_page: COMPLETE
service_subdivision_canonical_switch: NOT_STARTED
service_subdivision_second_cta: REMOVED_FROM_RUNTIME_PNG_AUTHORITY
service_subdivision_approach_v1: SUPERSEDED_NOT_IN_RUNTIME
service_subdivision_clinic_landscape: SECTION_SPECIFIC_IMAGE (section_clinic_landscape_image; theme fallback; Home no longer primary)
service_subdivision_program_template_garbage: ZERO
service_subdivision_dependencies_row_borders: REMOVED_BY_OPERATOR_DECISION
service_subdivision_final_corrections: COMPLETE
service_subdivision_build: PASS
service_subdivision_functional_qa: PASS
service_subdivision_regression_qa: PASS
service_subdivision_stable_source_backup: COMPLETE
service_subdivision_stable_tag: fp-0002-v7-service-subdivision-internal-page-reference-01
service_subdivision_reference_type: SERVICE_SUBDIVISION_INTERNAL_PAGE
service_subdivision_operator_status: CONDITIONALLY_ACCEPTED_REFERENCE
service_subdivision_navigation_switch: NOT_STARTED
service_subdivision_deploy: NOT_STARTED
fp0002_png_grouped_page_implementation_protocol: ACTIVE_REFERENCE_WORKFLOW
service_subdivision_final_reference_freeze_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-subdivision-final-reference-freeze/
next_page: FP-0002-PG-004-SERVICE-LEAF-INTERNAL-PAGE
next_phase: FP-0002-PG-004-SERVICE-LEAF-FULL-PAGE-OPERATOR-REVIEW
services_v2_reference: PRESERVED
service_leaf_page_id: FP-0002-PG-004
service_leaf_page_name: Услуга конечная
service_leaf_page_type: SERVICE_LEAF_INTERNAL_PAGE
service_leaf_source: src/pages/usluga-konechnaya-v1.html
service_leaf_group_1: COMPLETE
service_leaf_group_1_hero: PNG_MATCH_COMPLETE
service_leaf_group_1_navigation: PNG_MATCH_COMPLETE
service_leaf_group_1_intro: PNG_MATCH_COMPLETE
service_leaf_group_1_bordered_info: PNG_MATCH_COMPLETE_WITH_OPERATOR_DECOR_OVERRIDE
service_leaf_group_1_cta: PNG_MATCH_COMPLETE
service_leaf_lifebuoy_runtime: ZERO_BY_OPERATOR_OVERRIDE
service_leaf_group_1_desktop: PASS
service_leaf_group_1_mobile: PASS
service_leaf_group_2: COMPLETE
service_leaf_group_2_name: SIGNS_OF_ALCOHOL_DEPENDENCE_EDITORIAL
service_leaf_group_2_text_transcript: COMPLETE
service_leaf_group_2_content_fidelity: EXACT_VISIBLE_DESIGN_COPY
service_leaf_group_2_desktop: PASS
service_leaf_group_2_mobile: PASS
service_leaf_group_2_missing_text: ZERO
service_leaf_group_2_invented_copy: ZERO
service_leaf_group_2_template_garbage: ZERO
service_leaf_group_3: COMPLETE
service_leaf_group_3_name: TREATMENT_APPROACH_TEAM_AND_LANDSCAPE
service_leaf_group_3_desktop: PASS
service_leaf_group_3_mobile: PASS
service_leaf_group_4: COMPLETE
service_leaf_group_4_name: FOUR_DIRECTION_PROGRAM
service_leaf_group_4_desktop: PASS
service_leaf_group_4_mobile: PASS
service_leaf_group_5: COMPLETE
service_leaf_group_5_name: REHABILITATION_REQUIREMENTS_STAGES_AND_INTERIOR
service_leaf_group_5_desktop: PASS
service_leaf_group_5_mobile: PASS
service_leaf_group_6: COMPLETE
service_leaf_group_6_name: SHARED_LOWER_BLOCKS
service_leaf_group_6_desktop: PASS
service_leaf_group_6_mobile: PASS
service_leaf_remaining_groups: COMPLETE
service_leaf_full_page: COMPLETE_PENDING_OPERATOR_REVIEW
service_leaf_operator_wip_backup: COMPLETE
service_leaf_auto_polish: ACCEPTED_AS_PART_OF_CURRENT_CANONICAL_SOURCE
service_leaf_polish_reference: HOME_PLUS_SERVICE_SUBDIVISION_PLUS_SERVICES_V2
service_leaf_content_changed: NO
service_leaf_block_order_changed: NO
service_leaf_assets_changed: NO
service_leaf_operator_edits_preserved: YES
service_leaf_root_tokens_added: ZERO
service_leaf_stable_freeze: COMPLETE
service_leaf_desktop: PASS
service_leaf_mobile: PASS
service_leaf_functional_qa: PASS
service_leaf_regression_qa: PASS
service_leaf_noindex: ACTIVE
fp0002_operator_manual_edits: CANONICAL
fp0002_auto_polish: ACCEPTED_AS_PART_OF_CURRENT_CANONICAL_SOURCE
fp0002_four_template_baseline: CANONICAL_STABLE
fp0002_home_template: CANONICAL_STABLE
fp0002_services_hub_template: CANONICAL_STABLE
fp0002_service_subdivision_template: CANONICAL_STABLE
fp0002_service_leaf_template: CANONICAL_STABLE
fp0002_static_demo_site: PASS_4_FINAL_QA_COMPLETE
fp0002_static_demo_client_readiness: READY_FOR_DEPLOYMENT
fp0002_static_demo_overflow: ZERO_CONFIRMED
fp0002_static_demo_visual_readiness: READY_FOR_CLIENT_QA
fp0002_static_demo_excel_authority: CONFIRMED
fp0002_static_demo_page_registry: FINAL_58_PAGES
fp0002_static_demo_url_registry: FINAL_58_PAGES
fp0002_static_demo_title_h1_registry: FINAL_58_PAGES
fp0002_static_demo_navigation_registry: COMPLETE
fp0002_static_demo_placeholder_registry: FINAL_58_PAGES
fp0002_static_demo_generation: IMPLEMENTED
fp0002_static_demo_generated_pages: 58
fp0002_static_demo_template_pages: 12
fp0002_static_demo_placeholder_pages: 46
fp0002_static_demo_breadcrumbs: IMPLEMENTED
fp0002_static_demo_navigation: COMPLETE
fp0002_static_demo_full_navigation: COMPLETE
fp0002_static_demo_link_graph: COMPLETE
fp0002_static_demo_internal_404: ZERO
fp0002_static_demo_broken_anchors: ZERO
fp0002_static_demo_unexpected_orphans: ZERO
fp0002_static_demo_active_states: IMPLEMENTED
fp0002_static_demo_http_200: 58
fp0002_static_demo_asset_failures: ZERO
fp0002_static_demo_console_errors: ZERO
fp0002_static_demo_functional_qa: PASS
fp0002_static_demo_deploy_pack: V2_READY
fp0002_static_demo_deployment: NOT_PERFORMED_BY_TASK
fp0002_static_demo_composition: URGENT_V2_COMPLETE
fp0002_static_demo_primary_pages: 58
fp0002_static_demo_legacy_aliases: 1
fp0002_static_demo_dependencies_page: RENAMED_TO_ZAVISIMOSTI
fp0002_static_demo_genotipirovanie_route: LEGACY_ALIAS_ONLY
fp0002_static_demo_task_001_placeholders: 11_TARGETS_COMPLETE
fp0002_static_demo_task_002_placeholders: 4_UNIQUE_URLS_COMPLETE
fp0002_about_page: REUSE_FIRST_REBUILD_V3_IMPLEMENTED
fp0002_about_page_source: src/pages/o-centre-v1.html
fp0002_about_page_visual_donor_map: COMPLETE
fp0002_about_page_architecture: EXACT_COMPONENT_REUSE
fp0002_about_page_new_namespaces: ZERO
fp0002_about_page_preview: READY_FOR_OPERATOR_VISUAL_REVIEW
fp0002_about_page_registry_switch: NOT_STARTED
fp0002_about_page_route_switch: NOT_STARTED
fp0002_static_demo_v2: UNCHANGED
fp0002_deployment: UNCHANGED
fp0002_static_demo_client_url: NOT_ASSIGNED
fp0002_static_demo_deploy: NOT_STARTED
fp0002_static_demo_structure_source: CONFIRMED
fp0002_static_demo_planning_pack: workspaces/fp-0002-shpigovsky-v7/plans/static-client-demo/
fp0002_static_demo_generator: IMPLEMENTED
fp0002_canonical_templates: UNCHANGED
fp0002_placeholder_page_contract: READY
fp0002_wordpress: NOT_STARTED
fp0002_canonical_switch: NOT_STARTED
fp0002_navigation_switch: NOT_STARTED
fp0002_deploy: NOT_STARTED
fp0002_four_template_freeze_tag: fp-0002-v7-four-template-canonical-demo-baseline-01
service_leaf_group_1_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-leaf-group-1/
service_leaf_group_2_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-leaf-group-2/
service_leaf_group_3_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-leaf-group-3/
service_leaf_group_4_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-leaf-group-4/
service_leaf_full_page_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-leaf-remaining-page/
service_leaf_implementation: FULL_PAGE_ASSEMBLY_COMPLETE
service_leaf_canonical_switch: NOT_STARTED
service_leaf_navigation_switch: NOT_STARTED
service_leaf_deploy: NOT_STARTED
service_leaf_pass_opening_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-leaf-pass-opening/
service_leaf_planning_pack: workspaces/fp-0002-shpigovsky-v7/plans/service-leaf-page/
```

## Milestone (2026-06-23)

**FP-0002 WORDPRESS FOUNDATION CLOSURE (FW-06A.1)** — local runtime `shpigovsky.test` validated: direct domain PASS, `wp db check` PASS, Playwright foundation smoke PASS. Theme integration **LOCKED** until Frontend Production Pass and FW-06B.

## MLI-03R.1 post-reboot (2026-06-24)

After full Windows reboot, MySQL datadir/config drift broke DB connectivity. Remediation restored authoritative `my.ini`, loopback binding, and X Protocol disable. **No reinstall, no DB recreate, no password rotation.**

```text
FP-0002 WordPress foundation:
READY — POST-REBOOT VALIDATED

Evidence:
wp db check PASS; HTTP 200; Playwright 5/5; controlled MySQL restart PASS
Report: projects/mars-localhost-infrastructure/reports/MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md
```

---

## Phase

| Field | Value |
|-------|-------|
| **Phase** | **Foundation** |

---

## Website Factory status

| Field | Value |
|-------|-------|
| **Website Factory Status** | **Pre-Onboarding** |

Manifest enrollment (Playbook 01), registry enrollment (Playbook 02), and RT-G04 substrate (POC-01…POC-10) are **not started** for FP-0002.

---

## Production lanes

| Lane | Status |
|------|--------|
| **Frontend** | **V7 ACTIVE_DEVELOPMENT** — Package #001 complete pending operator final review (gallery captions below image, controlled polish) |
| **WordPress** | **Foundation READY — POST-REBOOT VALIDATED (MLI-03R.1)** — local runtime `shpigovsky.test`; theme integration **LOCKED** until Production Pass + FW-06B |
| **QA** | Not Started |
| **Delivery** | Not Started |

---

## Design and inventory

| Field | Value |
|-------|-------|
| **Design Materials** | Awaiting Intake |
| **Page Inventory** | **Updated** — `foundation/FP-0002-V6-PAGE-INVENTORY.md` in V6 workspace |
| **Block Inventory** | **Updated** — `reviews/services-page/reuse-only/FP-0002-HOME-BLOCK-INVENTORY-v1.md` |

---

## Services page status

| Field | Value |
|-------|-------|
| `services_foundation` | COMPLETE |
| `services_rejected_unique_implementation` | REVERTED (`25bfbce`) |
| `services_reuse_matrix` | COMPLETE |
| `services_page_mode` | REUSE_ONLY |
| `services_exact_reused_blocks` | header, program, founder, comfort, FAQ, final form, footer, modal |
| `services_new_unique_blocks` | 0 |
| `services_unimplemented_blocks` | hero, addictions, mental-health, eating-disorders |
| `services_unique_blocks` | REJECTED_AND_REVERTED |

---

## ATLAS linkage

| Check | Status |
|-------|--------|
| PRJ-0012 attested | **Yes** — AT-W3-SHPIG-01 |
| WEB-SHPIG-01 attested | **Yes** — AT-W4-SHPIG-01 |
| DOM-SHPIG-01 attested | **Yes** — AT-W5-SHPIG-01 |
| ORG-0008 attested | **Yes** — AT-W1D-SHPIG-01 |
| Factory manifest bind | **No** — pending onboarding |

---

## Intake

| Intake area | Status |
|-------------|--------|
| Structure | **Ready** — INCOMING/ scaffold created |
| Design materials | **Empty** — awaiting client/operator intake |
| Content | **Empty** |
| Access / hosting | **Empty** |

---

## Next gate

**Package #001** — implementation complete pending operator final visual review. WordPress theme integration **LOCKED** until operator sign-off + FW-06B.

---

*Status register only. Not a runtime state store.*


## 2026-07-04 — V9-06D.1 rerun runtime delivery

PASS: local WordPress runtime received canonical theme, Shpigovsky Core, and ACF JSON. Content model activation verified; service CPT registered; ACF groups and Options Page discoverable. WordPress object skeleton and V9 integration remain not started.


## 2026-07-04 — V9-06D.2 WordPress object skeleton

PASS: local WordPress runtime object skeleton created under checkpoint control. Services total: 15; Pages created: 0; Page templates reconciled: 13; Posts created: 0; Menus/options/redirects/rewrite flush unchanged. Content migration and V9 integration remain not started.


## 2026-07-04 — V9-06D.3 content migration planning

PASS: planning/audit only. 31 routes mapped; minimal visual content seed plan READY. Runtime content writes: 0.


## 2026-07-04 — V9-06D.4 RERUN minimal content seed for visual route QA

PARTIAL PASS: minimal ACF/meta seed applied to Pages 4/5/20 and Services 73/74/77/84 under DB checkpoint. Unauthorized writes: 0. Menus/options/redirects unchanged. Rewrite flush not performed. Service 74 HTTP 404 with matching generated permalink → REWRITE_FLUSH_MICRO_GATE_REQUIRED. Full content migration and V9 integration not performed.


## 2026-07-04 — REWRITE-FLUSH-MICRO-GATE

PARTIAL PASS: soft rewrite flush performed under DB checkpoint; `rewrite_rules` updated; `.htaccess` unchanged; content/ACF/menus/redirects/objects unchanged. Service 74 still HTTP 404 with matching generated permalink → FLUSH_NOT_SUFFICIENT. Next: route ownership / path conflict investigation.

## 2026-07-04 — ROUTE-OWNERSHIP-INVESTIGATION

PASS: read-only diagnostics. Primary cause POST_TYPE_LINK_REWRITE_MISMATCH (depth-2 rewrite maps leaf-only service query var; hierarchical lookup needs parent/child). Page 6 / Service 73 shared path CONFIRMED (secondary). Service 74 STILL_404. Runtime mutations 0. Next: CREATE_REWRITE_RULE_REPAIR_MICRO_TASK. V9-06D.5 BLOCKED.

## 2026-07-04 — REWRITE-RULE-REPAIR

PASS: depth-2 rewrite query repaired to `service=$matches[1]/$matches[2]`; source delivered to local runtime; soft flush under checkpoint. Service 74 HTTP 200 (resolved ID 74). Controls all 200. Content/ACF/menus/redirects unchanged. Page 6 / Service 73 secondary debt remains. V9-06D.5 UNBLOCKED. Next: V9-06D.5 visual route QA.

## 2026-07-04 — V9-06D.5 visual route QA

PARTIAL PASS: read-only visual route QA. All seven required routes HTTP 200; Service 74 regression PASS; header/footer/main present; desktop/mobile screenshots captured. Theme remains V9-06B skeleton (no V9 integration). Pages publish=22 (any-status=23; Page ID 3 draft). Posts publish=0 (prior=1). Page 6 / Service 73 secondary debt remains (not a D.5 blocker). Runtime mutations 0. Next: CREATE_V9_06D6_TEMPLATE_INTEGRATION_PLANNING_TASK.

## 2026-07-06 — V9-06D9-V reviews admin + static layout reconciliation audit

PARTIAL PASS: read-only audit. Operator post-D9-U findings confirmed: duplicate reviews in Site Settings; empty top-level Отзывы admin; /otzyvy/ layout mismatch (slider vs static archive list). Home slider matches static V9. D9-U committed but operator-unverified. Zero DB/source/theme/runtime mutations. Next: CREATE_V9_06D9W_REVIEWS_ADMIN_AND_LAYOUT_REPAIR_TASK.

## 2026-07-06 — V9-06E8 static V9 content + main layout authority repair

PARTIAL PASS: V9 static content/layout authority repair for `/uslugi/`, `/kontakty/`, alcohol service leaf. Theme `v9-static-content.php` + 17 template/helper updates; 0 DB writes; runtime delivered. E3 stable checkpoint invalidated. Automated route probe ALL_200. Next: CREATE_V9_06E9_OPERATOR_STATIC_PARITY_VISUAL_QA_TASK.

## V9-06E26D-POLISH (2026-07-09)

- Encoding mojibake audit/fix: default category term repaired (2 DB rows).
- Report: `reports/FP-0002-V9-06E26D-POLISH-ENCODING-MOJIBAKE-AUDIT-AND-FIX-REPORT-v1.md`







