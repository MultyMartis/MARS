# Entity classification proposal

Rules-only, evidence from multi-query SERP (`mig-20260604-mqgt01`). No ATLAS dependency.

| Domain | Classification | Distinct Queries | Appearances | Surface Types | Evidence |
| --- | --- | --- | --- | --- | --- |
| m.avito.ru | MARKETPLACE | 8 | 9 | serp_organic, aggregator, marketplace_listing | competitors.json → mig-20260604-mqgt01-c003 |
| uslugi.yandex.ru | AGGREGATOR | 8 | 8 | serp_organic, aggregator | competitors.json → mig-20260604-mqgt01-c004 |
| dostavka.yandex.ru | PLATFORM | 7 | 7 | serp_organic, aggregator | competitors.json → mig-20260604-mqgt01-c005 |
| krasnodar.gruzovichkof.ru | SERVICE_BRAND | 7 | 7 | serp_organic | competitors.json → mig-20260604-mqgt01-c006 |
| gruzovichec.ru | SERVICE_BRAND | 6 | 6 | serp_organic | competitors.json → mig-20260604-mqgt01-c002 |
| 2gis.ru | DIRECTORY | 5 | 5 | serp_organic, aggregator | competitors.json → mig-20260604-mqgt01-c014 |
| profi.ru | AGGREGATOR | 5 | 5 | serp_organic, aggregator | competitors.json → mig-20260604-mqgt01-c016 |
| youla.ru | MARKETPLACE | 4 | 4 | serp_organic, marketplace_listing | competitors.json → mig-20260604-mqgt01-c017 |
| krasnodar.taximaxim.ru | SERVICE_BRAND | 3 | 3 | serp_organic | competitors.json → mig-20260604-mqgt01-c008 |
| city-mobil.ru | SERVICE_BRAND | 3 | 3 | serp_organic | competitors.json → mig-20260604-mqgt01-c019 |
| gruzotaxi-triumph.ru | SERVICE_BRAND | 2 | 4 | serp_organic | competitors.json → mig-20260604-mqgt01-c001 |
| taxi.yandex.ru | PLATFORM | 2 | 2 | serp_organic, aggregator | competitors.json → mig-20260604-mqgt01-c007 |
| perivoz.ru | CLIENT | 1 | 1 | serp_organic | competitors.json → mig-20260604-mqgt01-c009 |
| gazkrasnodar.ru | MARKETPLACE | 1 | 1 | serp_organic | competitors.json → mig-20260604-mqgt01-c010 |
| auto.ru | MARKETPLACE | 1 | 1 | serp_organic | competitors.json → mig-20260604-mqgt01-c011 |
| 23-autoretail.ru | MARKETPLACE | 1 | 1 | serp_organic | competitors.json → mig-20260604-mqgt01-c012 |
| auto.drom.ru | MARKETPLACE | 1 | 1 | serp_organic | competitors.json → mig-20260604-mqgt01-c013 |
| 23.autoretail.ru | MARKETPLACE | 1 | 1 | serp_organic | competitors.json → mig-20260604-mqgt01-c015 |
| krasnodar.bystraya-logistika.ru | CLIENT | 1 | 1 | serp_organic | competitors.json → mig-20260604-mqgt01-c018 |
| krasnodar.100gryzchikov.ru | CLIENT | 1 | 1 | serp_organic | competitors.json → mig-20260604-mqgt01-c020 |
| dostavista.ru | PLATFORM | 1 | 1 | serp_organic | competitors.json → mig-20260604-mqgt01-c021 |
| krasnodar.rosstransco.com | CLIENT | 1 | 1 | serp_organic | competitors.json → mig-20260604-mqgt01-c022 |

## Classification rules applied

- **SERVICE_BRAND** — registrable domain of a cargo-taxi / freight operator; organic SERP titles describe direct hire or regional service (not listing aggregation).
- **AGGREGATOR** — multi-provider directory (Yandex Uslugi, Profi, Yandex Delivery landing, taxi.yandex tariff pages).
- **MARKETPLACE** — classifieds / listings (Avito, Youla, auto sales).
- **DIRECTORY** — business map / org index (2GIS).
- **PLATFORM** — app-first dispatch platform (CityMobil/TaxiMaxim-style national apps; Dostavista).
- **CLIENT** — single-query or ambiguous local operator not in repeated market-leader set.
