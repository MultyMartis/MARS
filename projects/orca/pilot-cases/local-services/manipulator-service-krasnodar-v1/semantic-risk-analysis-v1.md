# Semantic Risk Analysis v1

## Boundary

This is a conservative semantic QA simulation. It is not a live keyword export, not automatic clustering, and not validated advertising structure.

## Broad-Query Risks

- `грузоперевозки` can attract non-crane freight, movers, courier delivery, and intercity logistics.
- `аренда спецтехники` is too broad and may include excavators, cranes, loaders, lifts, and equipment rental.
- `доставка` without cargo type can leak into courier, food, retail, and supplier delivery intent.

## Irrelevant Cargo Intent

- Household moving without heavy cargo.
- Intercity freight forwarding.
- Parcel or courier delivery.
- Passenger transport.
- Container or warehouse logistics unrelated to crane-truck dispatch.

## Equipment Confusion

- `кран` may mean truck crane, tower crane, faucet repair, or crane operator jobs.
- `манипулятор` may also refer to robotics, computer input devices, medical equipment, or job titles.
- `эвакуатор с манипулятором` may be adjacent but operationally different if the business does not handle vehicles.

## Mixed Service Risks

- Loader labor queries may require people, not equipment.
- Construction material delivery may belong to suppliers, not transport contractors.
- Equipment rental queries may expect self-use rental rather than operated service.

## Low-Commercial-Intent Phrases

- `что такое манипулятор`
- `виды манипуляторов`
- `сколько весит манипулятор`
- `права на манипулятор`
- `работа водитель манипулятора`

## Geo Ambiguity

Krasnodar city, Krasnodar Krai, nearby settlements, and intercity routes may carry different availability and pricing assumptions. Geo modifiers must be separated before reuse.

## Negative Keyword Candidates

- `работа`, `вакансия`, `обучение`, `права`, `купить`, `продажа`, `ремонт джойстика`, `робот`, `медицинский`, `игровой`, `своими руками`.

## SAFE UNKNOWN

Negative keyword lists require live query review. These risks are hypotheses and may over-filter useful traffic if applied without human validation.
