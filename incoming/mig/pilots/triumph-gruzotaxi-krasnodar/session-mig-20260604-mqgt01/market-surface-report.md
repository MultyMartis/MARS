# REPORT — MIG Multi-Query Groundtruth Pilot

## Query Set

Approved **11** queries — see [multi-query-market-query-set-v1.md](multi-query-market-query-set-v1.md).

Executed: **8** / declared **11** (browser capture).

## Capture Coverage

| Metric | Value |
|--------|-------|
| Session ID | `mig-20260604-mqgt01` |
| Evidence root | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-multi-20260604/` |
| Query coverage | partial |
| Queries executed | q01, q02, q03, q04, q08, q09, q10, q11 |
| Queries missing | q05, q06, q07 |

## Competitor Frequency

| Domain | Distinct Queries | Appearances | Surface Types | Strength |
| --- | --- | --- | --- | --- |
| m.avito.ru | 8 | 9 | serp_organic, aggregator, marketplace_listing | multi_surface |
| uslugi.yandex.ru | 8 | 8 | serp_organic, aggregator | multi_surface |
| dostavka.yandex.ru | 7 | 7 | serp_organic, aggregator | multi_surface |
| krasnodar.gruzovichkof.ru | 7 | 7 | serp_organic | repeated |
| gruzovichec.ru | 6 | 6 | serp_organic | repeated |
| 2gis.ru | 5 | 5 | serp_organic, aggregator | multi_surface |
| profi.ru | 5 | 5 | serp_organic, aggregator | multi_surface |
| youla.ru | 4 | 4 | serp_organic, marketplace_listing | multi_surface |
| gruzotaxi-triumph.ru | 2 | 4 | serp_organic | repeated |
| krasnodar.taximaxim.ru | 3 | 3 | serp_organic | repeated |
| city-mobil.ru | 3 | 3 | serp_organic | repeated |
| taxi.yandex.ru | 2 | 2 | serp_organic, aggregator | multi_surface |
| perivoz.ru | 1 | 1 | serp_organic | single |
| gazkrasnodar.ru | 1 | 1 | serp_organic | single |
| auto.ru | 1 | 1 | serp_organic | single |
| 23-autoretail.ru | 1 | 1 | serp_organic | single |
| auto.drom.ru | 1 | 1 | serp_organic | single |
| 23.autoretail.ru | 1 | 1 | serp_organic | single |
| krasnodar.bystraya-logistika.ru | 1 | 1 | serp_organic | single |
| krasnodar.100gryzchikov.ru | 1 | 1 | serp_organic | single |
| dostavista.ru | 1 | 1 | serp_organic | single |
| krasnodar.rosstransco.com | 1 | 1 | serp_organic | single |

## Repeated Domains

- **gruzotaxi-triumph.ru** — queries: грузотакси Краснодар; грузовое такси Краснодар; recurrence: {"distinct_query_count":2,"query_ids":["q01","q02"]}
- **gruzovichec.ru** — queries: грузотакси Краснодар; грузовое такси Краснодар; газель Краснодар; газель с грузчиками Краснодар; грузовое такси с грузчиками Краснодар; заказать газель Краснодар; recurrence: {"distinct_query_count":6,"query_ids":["q01","q02","q03","q08","q09","q11"]}
- **m.avito.ru** — queries: грузотакси Краснодар; грузовое такси Краснодар; газель Краснодар; грузоперевозки Краснодар; газель с грузчиками Краснодар; грузовое такси с грузчиками Краснодар; грузоперевозки по Краснодару; заказать газель Краснодар; recurrence: {"distinct_query_count":8,"query_ids":["q01","q02","q03","q04","q08","q09","q10","q11"]}
- **uslugi.yandex.ru** — queries: грузотакси Краснодар; грузовое такси Краснодар; газель Краснодар; грузоперевозки Краснодар; газель с грузчиками Краснодар; грузовое такси с грузчиками Краснодар; грузоперевозки по Краснодару; заказать газель Краснодар; recurrence: {"distinct_query_count":8,"query_ids":["q01","q02","q03","q04","q08","q09","q10","q11"]}
- **dostavka.yandex.ru** — queries: грузотакси Краснодар; грузовое такси Краснодар; грузоперевозки Краснодар; газель с грузчиками Краснодар; грузовое такси с грузчиками Краснодар; грузоперевозки по Краснодару; заказать газель Краснодар; recurrence: {"distinct_query_count":7,"query_ids":["q01","q02","q04","q08","q09","q10","q11"]}
- **krasnodar.gruzovichkof.ru** — queries: грузотакси Краснодар; грузовое такси Краснодар; грузоперевозки Краснодар; газель с грузчиками Краснодар; грузовое такси с грузчиками Краснодар; грузоперевозки по Краснодару; заказать газель Краснодар; recurrence: {"distinct_query_count":7,"query_ids":["q01","q02","q04","q08","q09","q10","q11"]}
- **taxi.yandex.ru** — queries: грузотакси Краснодар; грузовое такси Краснодар; recurrence: {"distinct_query_count":2,"query_ids":["q01","q02"]}
- **krasnodar.taximaxim.ru** — queries: грузотакси Краснодар; грузовое такси с грузчиками Краснодар; грузоперевозки по Краснодару; recurrence: {"distinct_query_count":3,"query_ids":["q01","q09","q10"]}
- **2gis.ru** — queries: газель Краснодар; грузоперевозки Краснодар; газель с грузчиками Краснодар; грузовое такси с грузчиками Краснодар; заказать газель Краснодар; recurrence: {"distinct_query_count":5,"query_ids":["q03","q04","q08","q09","q11"]}
- **profi.ru** — queries: грузоперевозки Краснодар; газель с грузчиками Краснодар; грузовое такси с грузчиками Краснодар; грузоперевозки по Краснодару; заказать газель Краснодар; recurrence: {"distinct_query_count":5,"query_ids":["q04","q08","q09","q10","q11"]}
- **youla.ru** — queries: грузоперевозки Краснодар; газель с грузчиками Краснодар; грузоперевозки по Краснодару; заказать газель Краснодар; recurrence: {"distinct_query_count":4,"query_ids":["q04","q08","q10","q11"]}
- **city-mobil.ru** — queries: грузоперевозки Краснодар; грузовое такси с грузчиками Краснодар; грузоперевозки по Краснодару; recurrence: {"distinct_query_count":3,"query_ids":["q04","q09","q10"]}

## Aggregator Presence

- m.avito.ru (8 queries)
- uslugi.yandex.ru (8 queries)
- dostavka.yandex.ru (7 queries)
- taxi.yandex.ru (2 queries)
- 2gis.ru (5 queries)
- profi.ru (5 queries)

## Market Surface Findings

Evidence-only observations from **8** captured Yandex mobile SERPs (lr=35):

- Total discovered entities: **22**
- Cross-query repeated domains: **12**
- Entities seen on exactly one query: **10**
- Aggregator-tagged domains: **6**

## Single Query vs Multi Query

| Dimension | Pilot #1 (`mig-20260604-61b585`) | Multi-query (`mig-20260604-mqgt01`) |
|-----------|-----------------------------------|--------------------------------|
| Queries | 1 (`грузотакси краснодар`) | 8 |
| Competitors discovered | 9 | 22 |
| `rule_repeated_domain` | Inert (single SERP) | 12 entities |
| Discovery coverage block | Absent | Present |

## New Groundtruth

Domains in multi-query set **not** in Pilot #1 competitor list (15):

- gruzovichec.ru
- perivoz.ru
- gazkrasnodar.ru
- auto.ru
- 23-autoretail.ru
- auto.drom.ru
- 2gis.ru
- 23.autoretail.ru
- profi.ru
- youla.ru
- krasnodar.bystraya-logistika.ru
- city-mobil.ru
- krasnodar.100gryzchikov.ru
- dostavista.ru
- krasnodar.rosstransco.com

## Risks

- yabs promo hrefs may omit destination URL; normalization uses Path-line inference
- Headless Playwright ≠ logged-in human phone; personalization unknown
- No website/landing pass in this pilot (SERP-only groundtruth)

## SAFE UNKNOWN

- Queries not captured: q05, q06, q07

## Recommended Next Step

- Human review of screenshots under `evidence/serp-multi-20260604/captures/`
- Optional website pass on top repeated domains only
- Do not merge with Pilot #1 session folder

---

*Generated 2026-06-04T15:32:42.059Z*
