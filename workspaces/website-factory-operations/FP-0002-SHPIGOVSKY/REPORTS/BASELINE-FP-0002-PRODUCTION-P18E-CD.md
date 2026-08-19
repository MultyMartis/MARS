# BASELINE — FP-0002 PRODUCTION P18E-C/D

**Date:** 2026-08-19  
**Wave:** `PROD-P18E-C/D Cookie UI + Metrika Gating`  
**Evidence:** `REPORTS/evidence/prod-p18e-cd-cookie-ui-metrika-gating/`

## Runtime truth

- Public homepage emits no unconditional Yandex Metrika HTML before consent.
- Public cookie notice is visible for undecided / tampered / old-version states.
- Browser record key: `fp02_cookie_consent`.
- Current consent version: `1`.
- Cookie categories: `necessary`, `analytics`.
- Yandex Metrika source of truth remains `Настройки сайта → SEO и интеграции`.
- Dashboard/runtime meta now reports consent active and Metrika consent-gated.
- `blog_public=0`; indexing remains closed.

## Browser-state contract

- `UNDECIDED`
- `NECESSARY_ONLY`
- `ANALYTICS_ALLOWED`

Record schema:

- `version`
- `necessary`
- `analytics`
- `decided_at`

Validation:

- known keys only;
- `necessary=true` mandatory;
- strict boolean `analytics`;
- bounded integer version;
- bounded ISO timestamp;
- invalid/tampered payload => fail closed.

## Live QA summary

- Undecided: banner visible, no consent cookie, no `mc.yandex.ru` requests.
- Accept: cookie written with `analytics=true`, banner closes, Metrika loads.
- Necessary-only: cookie written with `analytics=false`, banner closes, no Metrika loads.
- Settings custom on/off: both flows verified.
- Contacts page no longer auto-loads Yandex map embed before consent.
- Revoke path writes `analytics=false`; post-revoke navigation stays analytics-free.
- JS disabled: no active Metrika requests.

## Production code target

- `shpigovsky-core` version: `0.3.18-p18e-cd`
- source ↔ production parity: exact touched files `MATCH`

## Still deferred

- Form-goal consent integration (`P18E-E`)
- Permanent footer/privacy reopen entry (`P18E-F`)
- Server-side consent evidence model
- Final Cookie Policy legal rewrite
