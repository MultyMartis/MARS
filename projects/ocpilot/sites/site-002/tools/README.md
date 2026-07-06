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
