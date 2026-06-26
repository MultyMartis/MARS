# FP-0002-PG-004 — Figma Frame Registry v1

**Source:** `Spig_v1.2.fig` (SHA-256 `BAE5D91C74B5A22AFC610F7C7845B9BADC6B87EC8DA85C5705ECF4EEC4DE3041`)  
**Method:** offline `openfig-core` parse + PNG dimension/visual match

| Variant | Frame name | Node ID | Dimensions | Visual match |
| ------- | ---------- | ------- | ---------: | ------------ |
| Desktop | Услуга конечная | `1:1748` | 1437×13313 | EXACT — matches desktop PNG W×H; hero alcohol treatment; leaf upper copy; FAQ alcohol questions |
| Mobile | Услуга конечная - моб | `1:5078` | 380×18136 | EXACT — matches mobile PNG W×H; mobile hero + stacked leaf blocks |

## Rejected candidates

| Frame | Node ID | Dimensions | Reason |
| ----- | ------- | ---------: | ------ |
| Услуга подраздел | `1:3491` | 1437×13675 | Subdivision listing page — dependency rows, not leaf body |
| Услуга подраздел - моб | `1:7096` | 380×18101 | Mobile subdivision — wrong anatomy |

## Desktop direct children (Figma stack order)

| # | Section | Node | H |
|---|---------|------|--:|
| 1 | 1 - Главный экран | `1:1749` | 905 |
| 2 | 2 - Дом - вступление | `1:1816` | 761 |
| 3 | 3- Услуги | `1:1847` | 659 |
| 4 | С чего начать (CTA band) | `1:1867` | 168 |
| 5 | Этапы процедуры | `1:1880` | 635 |
| 6 | Программа центра | `1:1894` | 1837 |
| 7 | Программа центра (2) | `1:1954` | 1519 |
| 8 | С чего начать (team/stats) | `1:1993` | 1781 |
| 9 | Специаисты | `1:2029` | 561 |
| 10 | Слово спецу | `1:2066` | 511 |
| 11 | преимущества | `1:2082` | 1473 |
| 12 | Отзывы | `1:2132` | 429 |
| 13 | faq | `1:2161` | 1147 |
| 14 | Подвал | `1:2184` | 488 |

**Note:** PNG adjudication shows CTA band visually between bordered info block and «Признаки» heading — stack order vs painted order differs in upper page; GROUP 1 boundary follows PNG.

## Confidence

- Desktop: **HIGH**
- Mobile: **HIGH**
- Result: **EXACT_NODES_CONFIRMED**
