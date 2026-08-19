# BASELINE — FP-0002 PRODUCTION P18E-A/B

**Date:** 2026-08-19  
**Wave:** `FP-0002 PROD-P18E-A/B COOKIE CONSENT FOUNDATION`

## Source-owned state

| Surface | State |
|---------|-------|
| Core plugin | `0.3.17-p18e-ab` |
| Consent owner | `Shpigovsky\Core\Privacy\PrivacyConsent` |
| Module registry | `privacy.consent` enabled in content model/runtime-delivered modes |
| Dashboard | truthfully reports `FOUNDATION READY / FRONTEND PENDING` |
| Activity Log | supports bounded cookie/privacy settings events |

## Production runtime state

| Surface | State |
|---------|-------|
| Public domain | `https://shpigovsky.ru/` serves WordPress |
| Indexing | `CLOSED` (`blog_public=0`) |
| Cookie banner | **NOT IMPLEMENTED** |
| Consent cookie auto-write | **ABSENT** on ordinary visitor GET |
| Yandex Metrika | still loads immediately (intentionally unchanged in this wave) |
| Form-goal runtime | unchanged |
| Cookie/privacy Admin | `Настройки сайта → Cookie и конфиденциальность` visible and persistent |
| Policy page owner | page `#24` (`cookie-files-policy`) |
| Policy page status | `CURRENT / NEEDS LEGAL CONTENT REVIEW` |

## Consent foundation contract

| Item | Value |
|------|-------|
| Categories | `necessary`, `analytics` |
| States | `UNDECIDED`, `NECESSARY_ONLY`, `ANALYTICS_ALLOWED` |
| Consent version | `1` |
| Browser record key | `fp02_cookie_consent` |
| Evidence model | browser-state foundation only |
| Server-side evidence store | deferred |
| Lifetime default | `365` days (product default, not legal requirement) |

## Evidence

- `REPORTS/evidence/prod-p18e-ab-consent-foundation/POST-DEPLOY-QA.json`
- `REPORTS/evidence/prod-p18e-ab-consent-foundation/PARITY-AFTER-DEPLOY.json`
- `REPORTS/evidence/prod-p18e-ab-consent-foundation/LEGAL-PROVIDER-RECHECK.md`
- `REPORTS/evidence/prod-p18e-ab-consent-foundation/CONSENT-CONTRACT-TEST.json`
