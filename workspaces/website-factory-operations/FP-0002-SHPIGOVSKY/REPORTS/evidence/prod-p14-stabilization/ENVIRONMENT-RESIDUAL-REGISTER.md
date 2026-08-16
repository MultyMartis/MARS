# ENVIRONMENT-RESIDUAL-REGISTER — PROD-P14

Audit-only (P06 / cutover not executed).

| Item | Current | Class | Action in P14 |
|------|---------|-------|---------------|
| WP_ENVIRONMENT_TYPE | `local` (const) while host is Beget production | B. P06 | Widget warning only |
| wp_get_environment_type() | `local` | B. P06 | none |
| WP_DEBUG | true | B. P06 / E. INTENTIONAL interim | none |
| WP_DEBUG_DISPLAY | false | E. INTENTIONAL | none |
| WP_DEBUG_LOG | true | B. P06 | none |
| siteurl / home | http://shpigovsky.beget.tech | C. PRE-CUTOVER / D. FINAL | none |
| blogname | Шпиговский Дом | E. INTENTIONAL | none |
| admin_email | mli-fp0002@localhost.test | B. P06 | none |
| WPLANG | ru_RU | E. INTENTIONAL | none |
| blog_public | 0 (noindex) | C. PRE-CUTOVER / D. FINAL | none |
| robots.txt Disallow | present + Sitemap line | C/D + E | none (PROD_ONLY retained) |
| hardcoded beget.tech | expected pre-cutover | C/D | none |
| `.test` / localhost refs in config | migration residue | B. P06 | none |
| MU mars-local-runtime.php | present; Admin notices removed P13 | B. P06 | none |
| outbound mail suppression (MU) | likely present | B. P06 / SMTP gate | none |
| Future domain shpigovsky.ru | DNS deferred | D. FINAL CUTOVER | none |
| SSL / HTTPS | not cut over | D. FINAL | none |
| SMTP | not configured | FUTURE (SMTP wave) | none |

**SAFE NOW applied in P14:** none that change cutover semantics. Only service-record/widget text + proven QA Activity Log rows.

Do not collapse P06 into P14.
