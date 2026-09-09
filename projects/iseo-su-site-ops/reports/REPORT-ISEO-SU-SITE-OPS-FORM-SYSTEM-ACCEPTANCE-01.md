# REPORT — ISEO-SU-SITE-OPS-FORM-SYSTEM-ACCEPTANCE-01

**Programme:** ISEO-SU-SITE-OPS  
**Task:** COMPLETE LIVE FORM SYSTEM ACCEPTANCE + GUARDED REPAIR 01  
**Date:** 2026-09-09  
**Live:** https://i-seo.su/  
**Status:** **COMPLETE** — all user-reachable form families verified; proven defects closed; isolated mail only; production test mails 0

## Summary

Production lead intake was inventoried (584 seeded URLs → **3744** classified lead surfaces / **10** families / **12** PHP handlers). Unique handler UI paths were submitted in a real browser. Isolated `test_mode` delivered to `im.work@mail.ru` only. Five proven defects were closed with minimal patches (`common.js`, career PHP, blog HTML, footer). `test_mode` restored **OFF**. Recipient authority remains `nikel007i33@yandex.ru`. SEO/menu/design/sitemap unchanged.

Operator-accepted homepage audit modal was not re-sent to production.

## Counts

| Metric | Value |
|--------|------:|
| Live form surfaces | 3744 |
| Static / modal / dynamic | 80 / 3594 / 70 |
| Form families | 10 |
| PHP handlers | 12 |
| JS file authority | `common.js` (29 send-id keys classified) |
| Surfaces structurally checked | 3744 |
| Unique PHP handlers mail-tested | 12 / 12 |
| Broken after | 0 |

## Defects closed this task

- Blog consent missing  
- Footer contact name hygiene (`cf_contact`; `cf_ontact` aliased in PHP)  
- Remaining relative `__FORM.php` AJAX URLs  
- Missing `preventDefault` on catch-all send clicks  
- Career live `#career__FORM_info` unbound + required file vs `serialize()`

## Calculators

SEO calculator (`/services/seo.html`) and tariff calculator (`/tariff-calc`) share `tarif-calc.php`. Both: calculate → reveal `.tariff-calc-request` → consent → POST `/callback__FORM.php` → success UI → isolated mail PASS. Recalc does not duplicate the form; after success the form fades out (no second mail).

## Artifacts

- Evidence: `ISEO-SU-FORM-SYSTEM-ACCEPTANCE-01-EVIDENCE-v1.md`  
- RU: `reports/ISEO-SU-FORM-SYSTEM-ACCEPTANCE-01-RU.md`  
- Inventory: `evidence/form-system-acceptance-01/live-form-inventory.csv`  
- Defects: `evidence/form-system-acceptance-01/defects.csv`  
- Backups: `X:\AI MARS\local\sites\iseo-su-production\_form-system-acceptance-01\`

## Git

Canonical sync via clean worktree from `origin/mars/canonical-post-recovery` (`1f090c0e`). Main workspace unpushed foreign WIP preserved (not staged).
