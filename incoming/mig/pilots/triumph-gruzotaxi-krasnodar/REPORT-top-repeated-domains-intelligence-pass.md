# REPORT — Top Repeated Domains Intelligence Pass

## Classification Review

Entity classification from `mig-20260604-mqgt01` competitor-frequency-table and competitors.json.

| Type | Count | Examples |
| --- | --- | --- |
| SERVICE_BRAND | 5 | gruzovichec.ru, krasnodar.gruzovichkof.ru, gruzotaxi-triumph.ru |
| AGGREGATOR | 2 | uslugi.yandex.ru, dostavka.yandex.ru, profi.ru |
| MARKETPLACE | 7 | m.avito.ru, youla.ru, auto.ru |
| DIRECTORY | 1 | 2gis.ru |
| PLATFORM | 3 | dostavista.ru, taxi.yandex.ru, dostavka.yandex.ru |
| CLIENT | 4 | perivoz.ru, krasnodar.bystraya-logistika.ru |

Full table: `session-mig-20260605-mlint01/entity-classification-proposal.md`

**Excluded from website pass (per task):** m.avito.ru, uslugi.yandex.ru, 2gis.ru, profi.ru, youla.ru, gazkrasnodar.ru, auto.ru, 23-autoretail.ru, auto.drom.ru, 23.autoretail.ru

## Market Leader Shortlist

Approved **5** SERVICE_BRAND domains with `rule_repeated_domain`:

- **gruzotaxi-triumph.ru** — 2 distinct queries; evidence rows: 4; id ref mig-20260604-mqgt01-c001
- **gruzovichec.ru** — 6 distinct queries; evidence rows: 6; id ref mig-20260604-mqgt01-c002
- **krasnodar.gruzovichkof.ru** — 7 distinct queries; evidence rows: 7; id ref mig-20260604-mqgt01-c006
- **krasnodar.taximaxim.ru** — 3 distinct queries; evidence rows: 3; id ref mig-20260604-mqgt01-c008
- **city-mobil.ru** — 3 distinct queries; evidence rows: 3; id ref mig-20260604-mqgt01-c019

Artifact: `session-mig-20260605-mlint01/market-leader-shortlist.json`

## Website Acquisition Results

| Metric | Value |
| --- | --- |
| Session | `mig-20260605-mlint01` |
| Planned snapshots | 5 |
| Captured | 5 |
| Status breakdown | {"success":5} |

Per-domain:

- **gruzotaxi-triumph.ru** — HTTP 200; status `success`; URL `https://gruzotaxi-triumph.ru/`; headings 11; offers 7; forms 2
- **gruzovichec.ru** — HTTP 200; status `success`; URL `https://gruzovichec.ru/`; headings 4; offers 3; forms 0
- **krasnodar.gruzovichkof.ru** — HTTP 200; status `success`; URL `https://krasnodar.gruzovichkof.ru/gruzovoe-taksi`; headings 2; offers 2; forms 1
- **krasnodar.taximaxim.ru** — HTTP 200; status `success`; URL `https://krasnodar.taximaxim.ru/gruzovie-perevozki/`; headings 0; offers 0; forms 0
- **city-mobil.ru** — HTTP 200; status `success`; URL `https://city-mobil.ru/krasnodar/gruz-taxi`; headings 2; offers 2; forms 0

## Landing Analysis Results

Analysis phase: `landing_analysis_v2` (schema 0.2)

### gruzotaxi-triumph.ru

- Families: OFFERS, PRICING, CTA, LEAD_CAPTURE, CONTACT_MODEL, SOCIAL_PROOF, TRUST, MARKETING_PATTERNS
- Top signals: OFFERS: Грузовое такси в Краснодаре; OFFERS: Цены на ГРУЗОВОЕ ТАКСИ; OFFERS: Заказать Грузовое такси; OFFERS: Есть ли грузчики?; OFFERS: Можно ли оформить предварительный заказ?
- Artifact: `landings/mig-20260605-mlint01-la001/landing_observation.json`

### gruzovichec.ru

- Families: PRICING, OFFERS, CTA, CONTACT_MODEL, TRUST, MARKETING_PATTERNS
- Top signals: PRICING: СРОЧНЫЙ ВЫЗОВ ГАЗЕЛИ ОТ 690 РУБ!; OFFERS: В АВТОПАРКЕ БОЛЕЕ 100 МАШИН; OFFERS: Грузоперевозки по Пензе и Пензенской области ; OFFERS: Через мобильное приложение цена ниже на 5-10%; PRICING: Груз такси от 690 руб.
- Artifact: `landings/mig-20260605-mlint01-la002/landing_observation.json`

### krasnodar.gruzovichkof.ru

- Families: OFFERS, DELIVERY_PROMISE, PRICING, CTA, CONTACT_MODEL, TRUST, MARKETING_PATTERNS
- Top signals: OFFERS: Грузовое такси в Краснодаре; DELIVERY_PROMISE: Вызвать грузовое такси в Краснодаре — подача за 15 минут!; PRICING: Рассчитать актуальную стоимость заказа Вы можете на сайте ил; CTA: 88003336747 → tel:88003336747; CTA: 84090392982 → tel:84090392982
- Artifact: `landings/mig-20260605-mlint01-la003/landing_observation.json`

### krasnodar.taximaxim.ru

- Families: OFFERS, PRICING, CTA, CONTACT_MODEL, MARKETING_PATTERNS
- Top signals: OFFERS: Когда водитель выполнит заказ, окончательная стоимость появи; PRICING: Когда водитель выполнит заказ, окончательная стоимость появи; CTA: +78619999999 → tel:+78619999999; CTA: telegram: taximaxim; CONTACT_MODEL: phone: +78619999999
- Artifact: `landings/mig-20260605-mlint01-la004/landing_observation.json`

### city-mobil.ru

- Families: OFFERS, PRICING, CTA, CONTACT_MODEL, TRUST, MARKETING_PATTERNS
- Top signals: OFFERS: В чем плюсы?; OFFERS: Удобнее через приложение; PRICING: Цена за перевозку указана сразу на экране Ответы на ваши воп; PRICING: Какая цена на грузоперевозку?; CTA: +7 495 222-22-22 → tel:+7495222-22-22
- Artifact: `landings/mig-20260605-mlint01-la005/landing_observation.json`

## Comparison Matrix

See `session-mig-20260605-mlint01/market-leader-comparison-matrix.md`

## New Groundtruth

Session `mig-20260605-mlint01` — separate from `mig-20260604-61b585` and `mig-20260604-mqgt01`.

| Artifact | Path |
| --- | --- |
| Shortlist | session-mig-20260605-mlint01/market-leader-shortlist.json |
| Website snapshots | session-mig-20260605-mlint01/website_snapshots.json |
| Landing observations | session-mig-20260605-mlint01/landing_observations.json |
| Research pack | session-mig-20260605-mlint01/research_pack.draft.md |
| Comparison matrix | session-mig-20260605-mlint01/market-leader-comparison-matrix.md |

## SERP vs Website Findings

**Visible from SERP alone:**

- **krasnodar.gruzovichkof.ru** — SERP titles/snippets only; recurrence 7 queries
- **gruzovichec.ru** — SERP titles/snippets only; recurrence 6 queries
- **krasnodar.taximaxim.ru** — SERP titles/snippets only; recurrence 3 queries
- **city-mobil.ru** — SERP titles/snippets only; recurrence 3 queries
- **gruzotaxi-triumph.ru** — SERP titles/snippets only; recurrence 2 queries

**Visible only after website acquisition:**

- **gruzotaxi-triumph.ru** — acquisition `success`; families: OFFERS, PRICING, CTA, LEAD_CAPTURE, CONTACT_MODEL, SOCIAL_PROOF, TRUST, MARKETING_PATTERNS
- **gruzovichec.ru** — acquisition `success`; families: PRICING, OFFERS, CTA, CONTACT_MODEL, TRUST, MARKETING_PATTERNS
- **krasnodar.gruzovichkof.ru** — acquisition `success`; families: OFFERS, DELIVERY_PROMISE, PRICING, CTA, CONTACT_MODEL, TRUST, MARKETING_PATTERNS
- **krasnodar.taximaxim.ru** — acquisition `success`; families: OFFERS, PRICING, CTA, CONTACT_MODEL, MARKETING_PATTERNS
- **city-mobil.ru** — acquisition `success`; families: OFFERS, PRICING, CTA, CONTACT_MODEL, TRUST, MARKETING_PATTERNS

**What changed:** Page-level headings, offer text, pricing strings, form/CTA elements, phone/email contacts, and trust phrases are now captured with HTML evidence refs. SERP provided title/snippet/position only.

## SAFE UNKNOWN

- Queries q05, q06, q07 not captured in source session — entities from those intents absent
- Actual dispatch pricing at order time (dynamic quotes) — only visible page text captured
- Human personalization / logged-in SERP variants
- Conversion performance, ad spend, fleet size — not observable from acquisition pass
- Whether SERP snippet prices match live page prices at capture time

## Readiness Assessment

MIG **now produces structured market intelligence beyond observation counts** for the approved shortlist: landing analysis v2 emits `observations[]` with families (offer, pricing, delivery_promise, trust, lead_capture), per-domain comparison matrix, and research pack intelligence cards.

**Limitation:** Intelligence remains **page-visible facts** at one URL per domain (homepage or SERP landing URL). No multi-page crawl, no ORCA interpretation, partial query coverage from source groundtruth.

**Verdict:** Useful **comparative landing intelligence** for market leaders — not yet full market intelligence (no keyword pass, no ads surface, no multi-page depth).

## Recommended Next Step

Human review of captured HTML under `session-mig-20260605-mlint01/snapshots/sites/` and comparison matrix; no automated strategy synthesis.

---

*Generated 2026-06-04T19:07:24.553Z · Lane A · session mig-20260605-mlint01*
