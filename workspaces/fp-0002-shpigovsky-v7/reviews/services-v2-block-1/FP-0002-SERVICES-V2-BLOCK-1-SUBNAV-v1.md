# FP-0002 — Services V2 Block 1 Subnav v1

**Date:** 2026-06-26

## Figma evidence

| Field | Desktop | Mobile |
| ----- | ------- | ------ |
| Container | `1:1367` (1172×34, gap 10) | `1:4665` Frame 20 (horizontal) |
| Items | `1:1368`–`1:1373` | `1:4666`–`1:4671` |
| Mobile behavior | Row | **Horizontal scroll** (row wider than viewport) |

## Labels (offline `symbolOverrides`)

| Order | Label | Width (desktop) |
| ----: | ----- | --------------- |
| 1 | Зависимости | 128 |
| 2 | Психическое здоровье | 204 |
| 3 | Пищевые расстройства | 210 |
| 4 | Программа | 113 |
| 5 | Условия центра | 147 |
| 6 | Вопрос/Ответ | 134 |

**Note:** Mobile instance `1:4668` contains typo `Пищевые расстроойсва` in `.fig`; desktop override used for production label.

## Semantic role

```text
CATEGORY_SHORTCUTS + MIXED_NAVIGATION
```

Implemented as `<nav><ul><li><a href="#…">` (not tabs).

## Destinations

| Label | Anchor | Confidence |
| ----- | ------ | ---------- |
| Зависимости | `#services-category-addictions-heading` | CONFIRMED (V1 section id) |
| Психическое здоровье | `#services-category-mental-health-heading` | CONFIRMED |
| Пищевые расстройства | `#services-category-eating-disorders-heading` | CONFIRMED |
| Программа | `#services-program` | CONFIRMED (anatomy `1:1610`, future block) |
| Условия центра | `#services-comfort` | INFERRED (comfort block `1:1665`) |
| Вопрос/Ответ | `#services-faq` | CONFIRMED (FAQ `1:1720`) |

## Active state

All tag instances share identical fill in offline parse — **no hub-page active tab** implemented.

## SAFE UNKNOWN

- Prototype URL targets beyond anchor map (not required for Block 1 page without lower sections)
- Genotyping not present in subnav (by Figma design)
