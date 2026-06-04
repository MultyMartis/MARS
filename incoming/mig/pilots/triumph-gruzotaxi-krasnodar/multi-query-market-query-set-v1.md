# Canonical market query set — MIG Multi-Query Groundtruth

**Pilot:** Триумф / Грузотакси / Краснодар  
**Starting point:** `грузотакси Краснодар`  
**Rule:** expand only by **direct commercial intent** (hire, dispatch, move, freight).

## Approved set (11 queries)

| ID | Query | Role | Rationale |
|----|-------|------|-----------|
| q01 | грузотакси Краснодар | primary | Core head term; Pilot #1 baseline |
| q02 | грузовое такси Краснодар | wording_variant | Synonym phrasing, same hire intent |
| q03 | газель Краснодар | supporting | Vehicle-class commercial query |
| q04 | грузоперевозки Краснодар | category_broad | Category-level freight |
| q05 | перевозка мебели Краснодар | supporting | Furniture move use case |
| q06 | квартирный переезд Краснодар | supporting | Apartment move use case |
| q07 | вызов газели Краснодар | commercial_variant | Dispatch / call wording |
| q08 | газель с грузчиками Краснодар | supporting | Vehicle + labor bundle |
| q09 | грузовое такси с грузчиками Краснодар | supporting | Service + labor bundle |
| q10 | грузоперевозки по Краснодару | geo_variant | Geo-qualified category |
| q11 | заказать газель Краснодар | commercial_variant | Order transactional |

Machine-readable: [multi-query-market-query-set-v1.json](multi-query-market-query-set-v1.json).

## Rejected from expansion pool

| Query | Reason |
|-------|--------|
| заказать грузотакси Краснодар | Duplicate surface vs q01 + q11 |
| недорогое грузотакси Краснодар | Price-only modifier (not in candidate charter) |
| грузотакси цена Краснодар | Price/informational lean |
| перевозка холодильника Краснодар | Narrow niche; not in user candidate list |
| газель Краснодар грузоперевозки | Redundant compound vs q03+q04 |

## Scope binding

- Engine: Yandex touch (`lr=35`)
- Device: mobile (Playwright iPhone 13)
- No Deep Research, ORCA, Website Factory in this pass
