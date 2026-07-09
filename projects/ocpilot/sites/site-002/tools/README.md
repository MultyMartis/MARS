# SITE-002 Production read-only tools

Small site-specific helpers for Production capture and inspection. **Read-only by default.**

## Scripts

| Script | Purpose |
|--------|---------|
| `site-002-prod-readonly-capture.py` | FTP inventory + baseline download + HTTP checks (full capture) |
| `site-002-prod-http-capture.py` | HTTP-only checks when FTP unavailable |
| `site-002-prod-screenshots.py` | Playwright desktop/mobile screenshots |
| `site-002-prod-admin-readonly.py` | OpenCart admin read-only dashboard inspection |
| `site-002-prod-ftp-retry.py` | FTP retry — inventory + baseline download only (Run 4.171-R1) |
| `site-002-prod-ftp-path-verify.py` | FTP path model verification — read-only listing (Run 4.172) |
| `site-002-prod-text-change-01.py` | Exact single-file Production text deploy for `SITE-002-PROD-TEXT-CHANGE-01` |
| `site-002-prod-sort-az-01.py` | Exact single-controller Production catalog sort deploy for `SITE-002-PROD-SORT-AZ-01` |
| `site-002-prod-sort-menu-order-01.py` | Exact single-Twig Production catalog sort menu deploy for `SITE-002-PROD-SORT-MENU-ORDER-01` |
| `site-002-prod-cron-wrapper-01.py` | Parallel MARS 1C cron wrapper — legacy map, prepare, upload, verify for `SITE-002-PROD-CRON-WRAPPER-01` |
| `site-002-prod-cron-run-reports-01.py` | MARS 1C wrapper TXT reports — download, enhance, deploy, verify for `SITE-002-PROD-CRON-RUN-REPORTS-01` |
| `site-002-prod-cron-run-reports-duration-fix-01.py` | MARS 1C wrapper TXT duration fix — discover, patch, fixture, deploy, verify for `SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01` (Run 4.239) |
| `site-002-prod-post-1c-lari-reparent-and-duration-verification-01.py` | Read-only post-1C timing gate + verification harness for Lari reparent persistence and TXT Duration fix confirmation — `SITE-002-PROD-POST-1C-LARI-REPARENT-AND-DURATION-VERIFICATION-01` (Run 4.240) |
| `mars_1c_import_wrapper.php` | Patched MARS 1C wrapper mirror v1.1.1 — repo reference; deployed to `/storage/mars-tools/cron/` (Run 4.239) |
| `site-002-prod-cron-activation-preflight-01.py` | MARS 1C cron activation preflight — token config, DB readonly, gated manual run for `SITE-002-PROD-CRON-ACTIVATION-PREFLIGHT-01` |
| `site-002-prod-cron-manual-run-01.py` | MARS 1C controlled manual import run — wrapper gates, single `--run`, post-run verify for `SITE-002-PROD-CRON-MANUAL-RUN-01` |
| `site-002-prod-cron-beget-activate-01.py` | Beget 1C cron activation prep — wrapper recheck, cron command, panel instructions for `SITE-002-PROD-CRON-BEGET-ACTIVATE-01` |
| `site-002-prod-cron-beget-active-confirm-01.py` | Beget 1C cron active confirmation — wrapper recheck, operator cron evidence, Storage artefacts for `SITE-002-PROD-CRON-BEGET-ACTIVE-CONFIRM-01` |
| `site-002-prod-cron-reports-cleanup-01.py` | MARS 1C cron reports cleanup — list, backup, exact delete, verify for `SITE-002-PROD-CRON-REPORTS-CLEANUP-01` |
| `site-002-prod-cron-first-scheduled-run-verify-01.py` | First scheduled Beget 1C cron run verification — FTP report read, parse, site health for `SITE-002-PROD-CRON-FIRST-SCHEDULED-RUN-VERIFY-01` |
| `site-002-prod-neutral-parent-categories-rollout-01.py` | Neutral parent category tiles + WebP images — discover, deploy `category_visibility.php`, admin image fields for `SITE-002-PROD-NEUTRAL-PARENT-CATEGORIES-ROLLOUT-01` |
| `site-002-prod-neutral-category-images-white-bg-refresh-01.py` | White-background refresh for 3 neutral category tile images — audit, Composer+Pillow normalize, FTP master/cache overwrite for `SITE-002-PROD-NEUTRAL-CATEGORY-IMAGES-WHITE-BG-REFRESH-01` |
| `site-002-prod-neutral-category-image-polki-fix-01.py` | Single-category polki tile image fix (ID 331) — audit, Composer+Pillow normalize, FTP master/cache overwrite for `SITE-002-PROD-NEUTRAL-CATEGORY-IMAGE-POLKI-FIX-01` |
| `site-002-prod-load-more-01.py` | Multi-file Production catalog load-more deploy for `SITE-002-PROD-LOAD-MORE-01` |
| `site-002-prod-mail-recipients-discovery-01.py` | Read-only Production mail/recipient FTP discovery for `SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01` |
| `site-002-prod-seo-readiness-robots-01.py` | SEO readiness — non-product meta audit + single-file robots.txt deploy for `SITE-002-PROD-SEO-READINESS-ROBOTS-01` |
| `site-002-prod-yandex-codes-verify-01.py` | Read-only Yandex Metrika/Webmaster verification for `SITE-002-PROD-YANDEX-CODES-VERIFY-01` |
| `site-002-prod-html-body-duplicate-fix-01.py` | Single-file Production header.twig deploy — duplicate body/preloader fix for `SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01` |
| `site-002-prod-sitemap-enable-01.py` | Production sitemap enable + robots Sitemap directive for `SITE-002-PROD-SITEMAP-ENABLE-01` |
| `site-002-prod-seo-meta-fix-01.py` | Non-product SEO meta fix — crawl, controller/modification deploy, admin attempt for `SITE-002-PROD-SEO-META-FIX-01` |
| `site-002-prod-seo-meta-content-fix-01.py` | Non-product SEO meta **content** — copywriting, OpenCart admin SEO saves, verification for `SITE-002-PROD-SEO-META-CONTENT-FIX-01` |
| `site-002-prod-seo-information-meta-runtime-discovery-01.py` | Read-only information/blog/katalog meta runtime authority discovery for `SITE-002-PROD-SEO-INFORMATION-META-RUNTIME-DISCOVERY-01` |
| `site-002-prod-seo-information-meta-runtime-fix-01.py` | Information/blog/katalog meta runtime fix — controller patches + category admin SEO for `SITE-002-PROD-SEO-INFORMATION-META-RUNTIME-FIX-01` |
| `site-002-prod-seo-product-meta-generator-discovery-01.py` | Read-only product PDP meta generator discovery — live samples + FTP source for `SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-DISCOVERY-01` |
| `site-002-prod-seo-product-meta-generator-fix-01.py` | Product PDP meta runtime generator — single-controller deploy for `SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-FIX-01` |
| `site-002-prod-seo-product-meta-keywords-tune-01.py` | Product PDP meta keywords generator v1.1 tune — filter/cap keywords only for `SITE-002-PROD-SEO-PRODUCT-META-KEYWORDS-TUNE-01` |
| `site-002-prod-llms-txt-01.py` | Production llms.txt deploy — discovery, draft, single-file FTP upload, verification for `SITE-002-PROD-LLMS-TXT-01` |
| `site-002-prod-llms-txt-encoding-fix-01.py` | Production llms.txt UTF-8 BOM encoding fix — diagnose, backup, single-file reupload, optional `.htaccess` for `SITE-002-PROD-LLMS-TXT-ENCODING-FIX-01` |
| `site-002-prod-brand-zpm-remediation-01.py` | Public brand remediation — `БЗПМ`→`ЗПМ` in llms.txt, controllers, product generator, category admin SEO for `SITE-002-PROD-BRAND-ZPM-REMEDIATION-01` |
| `site-002-prod-seo-meta-final-inventory-01.py` | Read-only final public meta inventory + brand regression audit for `SITE-002-PROD-SEO-META-FINAL-INVENTORY-01` (Run 4.206) |
| `site-002-prod-seo-meta-edge-fix-01.py` | Deep sub-category PLP meta edge fix via admin category SEO for `SITE-002-PROD-SEO-META-EDGE-FIX-01` (Run 4.207) |
| `site-002-prod-seo-product-meta-generator-tune-02.py` | PDP keyword gap follow-up — classify Run 4.206 11 missing-keyword URLs; read-only `product.php` authority for `SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-TUNE-02` (Run 4.208) |
| `site-002-prod-sitemap-delta-audit-01.py` | Read-only sitemap delta audit — compare Run 4.206 baseline (1320) vs live (1377); classify added/removed URLs for `SITE-002-PROD-SITEMAP-DELTA-AUDIT-01` (Run 4.209) |
| `site-002-prod-catalog-new-branch-onboarding-01.py` | New 1C catalog branch onboarding — category PLP meta via admin category SEO for `SITE-002-PROD-CATALOG-NEW-BRANCH-ONBOARDING-01` (Run 4.210) |
| `site-002-prod-catalog-branch-onboarding-followup-01.py` | Deferred lari branch follow-up — parent-aware category_id resolution + admin category SEO for `SITE-002-PROD-CATALOG-BRANCH-ONBOARDING-FOLLOWUP-01` (Run 4.211) |
| `site-002-prod-post-1c-catalog-onboarding-monitor-01.py` | Read-only post-1C catalog onboarding monitor — sitemap delta, category onboarding needs, PDP sanity, brand/test markers for `SITE-002-PROD-POST-1C-CATALOG-ONBOARDING-MONITOR-01` (Run 4.212) |
| `site-002-prod-post-1c-catalog-onboarding-monitor-02.py` | Read-only post-1C catalog onboarding monitor repeat — baseline from Run 4.212; sitemap delta, category onboarding needs, PDP sanity, brand/test markers for `SITE-002-PROD-POST-1C-CATALOG-ONBOARDING-MONITOR-02` (Run 4.213) |
| `site-002-prod-sitemap-authority-discovery-01.py` | Read-only sitemap authority discovery — physical vs route, feed controller, data sources, 1C relationship, cache behavior, policy for `SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01` (Run 4.214) |
| `site-002-post-1c-monitor-runner.ps1` | Local scheduled runner — invokes read-only post-1C monitor; call-operator quoting for `X:\AI MARS` paths; logs under Storage `scheduled-monitors/post-1c/` (Run 4.215 / **4.216 fix**) |
| `install-site-002-post-1c-monitor-task.ps1` | Windows Task install — `MARS_SITE_002_Post_1C_Catalog_Monitor`; **disabled by default**; `-Enable -ConfirmEnable` for enabled task (Run 4.215) |
| `uninstall-site-002-post-1c-monitor-task.ps1` | Windows Task uninstall — exact task name only (Run 4.215) |
| `site-002-prod-ux-task-intake-01.py` | Read-only UX task intake — new section tiles + PDP «Дополнительные сведения» authority for `SITE-002-PROD-UX-TASK-INTAKE-01` (Run 4.217) |
| `site-002-prod-pdp-extra-info-attribute-layout-01.py` | Controlled Production PDP patch — move «Дополнительные сведения» out of specs table for `SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01` (Run 4.218) |
| `site-002-prod-new-sections-entrypoints-01.py` | New section entrypoint tiles — category visibility + Category-image gate for lari/konditerskiy for `SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-01` (Run 4.219) |
| `site-002-prod-new-sections-entrypoints-02.py` | Composer-only category images + entrypoint tiles deploy for lari/konditerskiy for `SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-02` (Run 4.220) |
| `site-002-prod-category-entrypoints-sort-az-01.py` | Category entrypoints A→Z display sort deploy for megamenu/homepage/neutral hub for `SITE-002-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01` (Run 4.221) |
| `site-002-prod-mail-system-discovery-01.py` | Read-only Production mail system discovery — forms HTTP crawl + FTP source map + redesign charters for `SITE-002-PROD-MAIL-SYSTEM-DISCOVERY-01` (Run 4.222) |
| `site-002-prod-mail-design-system-01.py` | Mail design system foundation — `ZpmMailRenderer`, fixtures, previews, gated single-file FTP deploy for `SITE-002-PROD-MAIL-DESIGN-SYSTEM-01` (Run 4.223) |
| `site-002-prod-mail-admin-forms-01.py` | Admin form mail redesign — anketa + renderer integration, service info, gated deploy + controlled test submit for `SITE-002-PROD-MAIL-ADMIN-FORMS-01` (Run 4.224) |
| `site-002-prod-mail-customer-forms-01.py` | Customer form confirmations + loading/abort UX — anketa + renderer + main.js + CSS, gated deploy + 2 controlled test submits for `SITE-002-PROD-MAIL-CUSTOMER-FORMS-01` (Run 4.226) |
| `site-002-post-1c-catalog-hygiene-review-01.py` | Read-only post-1C catalog hygiene review — added URL HTTP/meta/brand/duplicate audit after scheduled monitor for `SITE-002-POST-1C-CATALOG-HYGIENE-REVIEW-01` (Run 4.227) |
| `site-002-post-1c-garbage-marker-fixture-test.py` | Strict garbage marker fixture regression — local harness for `SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01` (Run 4.228) |
| `site-002-post-1c-import-logs-and-monitor-artifacts-audit-01.py` | Read-only post-1C import logs + monitor artifacts audit — FTP index/download, local inventory, Task Scheduler inspection for `SITE-002-POST-1C-IMPORT-LOGS-AND-MONITOR-ARTIFACTS-AUDIT-01` (Run 4.233) |
| `site-002-prod-category-lari-reparent-discovery-01.py` | Read-only category Lari reparent discovery — HTTP snapshots, DB SELECT, FTP source map, sitemap/entrypoint analysis, implementation charter for `SITE-002-PROD-CATEGORY-LARI-REPARENT-DISCOVERY-01` (Run 4.234) |
| `site-002-prod-category-lari-reparent-implementation-01.py` | Controlled category Lari reparent implementation — 1C gate, DB migration, FTP patches, HTTP verification for `SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01` (Run 4.235) |
| `site-002-prod-parent-category-tiles-lari-removal-01.py` | Parent Category Tiles adjustment — remove **88** from `$neutral_hub_branch_ids`, single-file FTP deploy, verification for `SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01` (Run 4.236) |
| `site-002-prod-contacts-url-routing-review-01.py` | Read-only contacts URL routing discovery — HTTP snapshots, DB SELECT, FTP source map, sitemap/links inventory for `SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01` (Run 4.237); Option E charter **rejected** by operator decision Run 4.238 — `/contact` canonical |
| `site-002-prod-category-lari-final-fix-01.py` | Final SEO/url fix wave — `seo_url`, `category_visibility`, `category.php`, htaccess redirects (Run 4.235 helper) |
| `site-002-prod-category-lari-seopath-cache-clear-01.py` | Scoped purge of `category.seopath` / `seo_pro` caches after reparent (Run 4.235 helper) |
| `site-002-prod-category-lari-seopro-patch-01.py` | Patch `seo_pro.php` `getPathByCategory()` to use `oc_category_path` (Run 4.235 helper) |
| `site-002-category-lari-reparent.sql` | Sanitized apply SQL plan (no credentials) |
| `site-002-category-lari-reparent-rollback.sql` | Sanitized rollback SQL plan (no credentials) |
| `site-002-prod-info-page-forms-discovery-01.py` | Read-only info page corp CTA form discovery — HTTP inventory + FTP source map + integration charter for `SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01` (Run 4.229) |
| `site-002-prod-info-page-forms-integration-01.py` | Info page corp CTA forms integration — 14-file deploy, mail extension, corp CTA JS handler, 5 controlled test submits for `SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01` (Run 4.230) |
| `site-002-prod-mail-customer-forms-delivery-confirmation-01.py` | Customer form email delivery confirmation — 1 controlled submit with operator mailbox, sanity checks, mailbox gate for `SITE-002-PROD-MAIL-CUSTOMER-FORMS-DELIVERY-CONFIRMATION-01` (Run 4.231) |
| *(documentation only)* | Run **4.232** customer inbox confirmation — `SITE-002-PROD-MAIL-CUSTOMER-FORMS-INBOX-CONFIRMATION-01`; operator verified mailbox delivery/design/no service info issue; no script; report at [../reports/SITE-002-PROD-MAIL-CUSTOMER-FORMS-INBOX-CONFIRMATION-01.md](../reports/SITE-002-PROD-MAIL-CUSTOMER-FORMS-INBOX-CONFIRMATION-01.md) |
| *(documentation only)* | Run **4.225** inbox confirmation — `SITE-002-PROD-MAIL-ADMIN-FORMS-INBOX-CONFIRMATION-01`; operator verified mailbox delivery/design; no script; report at [../reports/SITE-002-PROD-MAIL-ADMIN-FORMS-INBOX-CONFIRMATION-01.md](../reports/SITE-002-PROD-MAIL-ADMIN-FORMS-INBOX-CONFIRMATION-01.md) |
| `checkout_anketa_mail_admin_forms.php` | Patched `checkout/anketa.php` source for Run 4.224 (repo reference; superseded by customer-forms variant for Run 4.226) |
| `checkout_anketa_mail_customer_forms.php` | Patched `checkout/anketa.php` source for Run 4.226 — customer confirmations + admin mail (repo reference; superseded by info-page-forms variant for Run 4.230) |
| `checkout_anketa_info_page_forms.php` | Patched `checkout/anketa.php` source for Run 4.230 — dialogs 8–11 + extra fields (repo reference; deployed to Production) |
| `site-002-mail-design-system-preview-01.php` | Local preview generator for mail design system (no SMTP; uses fixtures + renderer) |
| `mail_renderer.php` | Shared `ZpmMailRenderer` source — deployed to Production `system/library/zpm/mail_renderer.php`; customer + admin render methods |
| `zpm-corp-cta-forms.js` | Corp CTA submit handler snippet merged into Production `main.js` (Run 4.230) |
| `zpm-corp-cta-success.css` | Inline success/error styles appended to Production `style.css` (Run 4.230) |

### Post-1C monitor scheduler notes (Run 4.216 / **4.228 hardening**)

- Runner supports repository paths with spaces (`X:\AI MARS`) via PowerShell call-operator invocation.
- Successful Windows Task `LastTaskResult` is **0**; **2** means runner/monitor execution failure — check `scheduled-monitors/post-1c/<timestamp>/run.stderr.log`.
- Per-run logs: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\scheduled-monitors\post-1c\`
- **Hardened artifact contract (Run 4.228):** each run folder includes `added-urls.*`, `removed-urls.*`, `sitemap-baseline.xml`, `sitemap-current.xml`, `hygiene-flags.*`, `monitor-classification.*`, `changed-summary.*`, UTF-8 `run.log`/`run.stderr.log`, and `run-summary` with `duration_seconds`, `classification`, `next_action`.
- **Strict garbage markers:** context-aware scan; no false positives on `/assets/img/demo/` or «Пример эксплуатации» doc links.
- **Classification:** `NO_ACTION_REQUIRED` | `HYGIENE_REVIEW_REQUIRED` | `ONBOARDING_REQUIRED` | `FAILURE_REVIEW_REQUIRED`.

## Dependencies

- Python 3.x (stdlib + `paramiko` optional for SFTP diagnostics)
- `playwright` (`python -m playwright install chromium`)

## Credentials

Reads **only** the `## PRODUCTION` section from:

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md
```

No credentials are embedded in scripts or logs.

## Safety

- Read-only scripts have no upload/delete/rename commands
- Does not download `config.php`, `admin/config.php`, `.env`
- Sanitizes admin session tokens in stored observations

`site-002-prod-text-change-01.py` is operation-specific for guarantee.twig. `site-002-prod-seo-readiness-robots-01.py` supports only `/public_html/robots.txt` upload with mandatory backup, deploy gates, and rollback manifests. Neither tool has delete or rename functions for unrelated paths.
