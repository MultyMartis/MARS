# FP-0002 V9-06D7E Contacts Post-Delivery Smoke Result v1

**Date:** 2026-07-05

## Route smoke

| Route | URL | HTTP | Expected | Header | Footer | CSS | JS | Result |
|---|---|---:|---|---:|---:|---:|---:|---|
| Home | http://shpigovsky.test/ | 200 | page #4 | True | True | True | True | PASS |
| Services Hub | http://shpigovsky.test/uslugi/ | 200 | page #5 | True | True | True | True | PASS |
| Parent Service — Зависимости | http://shpigovsky.test/uslugi/zavisimosti/ | 200 | service #73 | True | True | True | True | PASS |
| Child Service — Алкоголь | http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | 200 | service #74 | True | True | True | True | PASS |
| Parent Service — Психическое здоровье | http://shpigovsky.test/uslugi/psihicheskoe-zdorovie/ | 200 | service #77 | True | True | True | True | PASS |
| Parent Service — РПП | http://shpigovsky.test/uslugi/rasstroystva-pischevogo-povedeniya/ | 200 | service #84 | True | True | True | True | PASS |
| Contacts | http://shpigovsky.test/kontakty/ | 200 | page #20 | True | True | True | True | PASS |

## Contacts section render smoke

| Section/check | Present | Expected if empty/deferred | Result |
|---|---:|---|---|
| page_template_orchestration | True | required | PASS |
| contacts_root_class | True | required | PASS |
| contacts_body | True | required | PASS |
| location_cards | True | required | PASS |
| phone_row | True | omitted or fallback acceptable | PASS |
| messengers_social | False | omitted or fallback acceptable | PASS_OMITTED |
| map_figure | False | omitted or fallback acceptable | PASS_OMITTED |
| rehabilitation_steps | True | required | PASS |
| cta_band | True | required | PASS |
| modal_only_behavior | True | required | PASS |
| no_live_endpoint | True | modal-only consultation; no external form POST | PASS |
| no_external_api_key_in_html | True | no map API keys in rendered HTML | PASS |
| deferred_media_documented | True | map PNG and rehabilitation interior photo not packaged; omission expected | PASS |

## Home / Services Hub / Service stability

| Route | HTTP | Key marker | Header/footer/assets | Result |
|---|---:|---|---|---|
| home | 200 | site-main--front | True/True/True/True | PASS |
| services_hub | 200 | site-main--services-hub | True/True/True/True | PASS |
| service_73 | 200 | hero | True/True/True/True | PASS |
| service_74 | 200 | hero | True/True/True/True | PASS |
| service_77 | 200 | hero | True/True/True/True | PASS |
| service_84 | 200 | hero | True/True/True/True | PASS |

## Asset smoke

| Asset | Status |
|---|---|
| V9 CSS | PASS |
| V9 shell JS | PASS |
| Logo SVG | PASS |

## Service 74 regression

URL: http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ — HTTP 200 — variant alcohol-special — PASS

## No external API key runtime check

- API keys in HTML: []
- Live form endpoint: False
- Result: PASS

## Visual smoke

Screenshots: PASS — 14 captured.

## Deferred gaps (not blockers)

- Map PNG assets not packaged — map figure omitted
- Rehabilitation interior photo not packaged — photo bleed omitted
- Messengers may be omitted when site options unseeded

## Result

PASS
