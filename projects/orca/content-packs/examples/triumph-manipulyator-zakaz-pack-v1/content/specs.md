# Section — Specs (machine showcase)

**section_id:** `specs`  
**partial:** `v5-ppc/zakaz/screen-02-specs.html`  
**anchor:** `#specs`  
**priority:** P0

## Purpose

Second-screen **capability confirmation** — repeats hero numbers with machine photo and «одна конкретная техника» framing.

## Copy locks 🔒

| Element | Text |
|---------|------|
| Eyebrow | Параметры техники |
| H2 | Параметры нашей машины |
| Lead | Одна конкретная техника с понятными параметрами: перевозка, погрузка и подача без подмены после звонка. |
| Specs dl | Борт 5 т · Стрела 3 т · Вылет 14 м · Кузов 6.2×2.2 · Мин. заказ 2 ч |
| Ops line | Подходит для стройматериалов, бытовок, ФБС, арматуры, оборудования, контейнеров… в рамках 5 т / 3 т |
| CTA | Рассчитать стоимость |
| Micro | Ответим: подходит ли техника · сколько примерно будет стоить · когда возможна подача |

## PPC continuity

- Echoes ad callouts «Борт 5 т», description «стрела 3 т»
- **Strong** alignment with capability keywords

## Visual semantics

- `compactness_level: compact` — dl grid, not paragraph features
- Image: `second-screen-index-baseline.jpg` — operational context, not stock fleet

## Factory notes

- `machine-showcase` pattern shared with capability routes — zakaz uses index baseline asset
- CTA: modal/callback `data-cta-source=zakaz-specs-primary`

## Drift

| Allowed | Forbidden |
|---------|-----------|
| Layout tightening, image swap same semantics | Different tonnage, second machine, «автопарк» copy |
