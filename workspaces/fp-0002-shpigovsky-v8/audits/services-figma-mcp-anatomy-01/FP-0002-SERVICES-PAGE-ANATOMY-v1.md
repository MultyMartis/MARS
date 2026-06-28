# FP-0002 — Services Page Anatomy v1

**Date:** 2026-06-26  
**Target desktop frame:** `1:1310` (`Услуги хаб`)  
**Target mobile frame:** `1:4624` (`Услуги хаб - моб`)  
**Source:** offline visible-node parse of `Spig_v1.2.fig` + approved PNG 26.06.2026  
**MCP live pass:** pending cloud file access

## Page tree (desktop, visible order)

```text
Услуги хаб (1:1310)
├── 1 - Главный экран (1:1311)                    [INNER HERO SHELL + header + breadcrumbs + tabs]
│   ├── Хедер (1:1312)
│   ├── Group 6 / банер (1:1347)                  [media + overlay + inner hero content + CTA]
│   ├── Frame 81513852 (1:1360)                   [decorative accent]
│   ├── Хлебные крошки (1:1363)
│   └── Табы (1:1367)                             [page submenu — 6 Tag instances]
├── 3- Услуги (1:1405)                            [CATEGORY 1 — Зависимости и пристрастия]
├── 3- Услуги (1:1474)                            [CATEGORY 2 — Психическое здоровье]
├── 3- Услуги (1:1569)                            [CATEGORY 3 — Расстройства пищевого поведения]
├── Программа центра (1:1610)                     [PROGRAM]
├── Слово спецу (1:1649)                           [FOUNDER]
├── преимущества (1:1665)                         [COMFORT]
├── С чего начать (1:1715)                        [MID-PAGE CTA / info strip]
├── faq (1:1720)                                  [FAQ]
├── Подвал (1:1747)                               [FOOTER instance]
└── 3- Услуги (32:4586)                           [CATEGORY 4 — Генотипирование]
```

**Note:** `2 - Дом - вступление (1:1374)` exists in `.fig` child list but is **not visible** on approved PNG — excluded from implementation anatomy.

## Top-level component table

| Order | Component | Node ID | Type | Bounds | Visible | Parent | Probable role | Status |
| ----: | --------- | ------- | ---- | ------ | ------: | ------ | ------------- | ------ |
| 1 | Inner Hero block | `1:1311` | FRAME | 1441×905 | Yes | `1:1310` | Hero + chrome + breadcrumbs + tabs | FOUND_AS_INDEPENDENT_NODE |
| 2 | Breadcrumbs | `1:1363` | FRAME | 660×18 | Yes | `1:1311` | BLK-005 trail | FOUND_AS_NESTED_NODE |
| 3 | Page submenu | `1:1367` | FRAME | 1172×34 | Yes | `1:1311` | Category tab shortcuts | FOUND_AS_NESTED_NODE |
| 4 | Category 1 | `1:1405` | FRAME | 1437×1413 | Yes | `1:1310` | Addictions hub | FOUND_AS_INDEPENDENT_NODE |
| 5 | Category 2 | `1:1474` | FRAME | 1437×1698 | Yes | `1:1310` | Mental health hub | FOUND_AS_INDEPENDENT_NODE |
| 6 | Category 3 | `1:1569` | FRAME | 1437×804 | Yes | `1:1310` | Eating disorders (compact) | FOUND_AS_INDEPENDENT_NODE |
| 7 | Program | `1:1610` | FRAME | 1437×1519 | Yes | `1:1310` | 4-direction program grid | FOUND_AS_INDEPENDENT_NODE |
| 8 | Founder | `1:1649` | FRAME | 1440×511 | Yes | `1:1310` | Expert quote | FOUND_AS_INDEPENDENT_NODE |
| 9 | Comfort | `1:1665` | FRAME | 1437×1473 | Yes | `1:1310` | Gallery + copy | FOUND_AS_INDEPENDENT_NODE |
| 10 | Mid-page CTA | `1:1715` | FRAME | 1441×143 | Yes | `1:1310` | Dark contact strip | FOUND_AS_INDEPENDENT_NODE |
| 11 | FAQ | `1:1720` | FRAME | 1440×1517 | Yes | `1:1310` | Accordion FAQ | FOUND_AS_INDEPENDENT_NODE |
| 12 | Final form | — | — | — | Yes (PNG) | SAFE UNKNOWN node | Lead form before footer | SAFE_UNKNOWN (node id pending MCP) |
| 13 | Footer | `1:1747` | INSTANCE | 1440×488 | Yes | `1:1310` | Global footer | FOUND_AS_INDEPENDENT_NODE |
| 14 | Category 4 | `32:4586` | FRAME | 1437×528 | Yes | `1:1310` | Genotyping (compact) | FOUND_AS_INDEPENDENT_NODE |

## Mobile top-level (`1:4624`)

| Order | Component | Node ID | Bounds |
| ----: | --------- | ------- | ------ |
| 1 | Hero mobile | `1:4625` (`Моби`) | 380×637 |
| 2 | Category 1 | `1:4676` | 380×2491 |
| 3 | Category 2 | `1:4744` | 380×2835 |
| 4 | Category 3 | `1:4832` | 380×1483 |
| 5 | Program | `1:4880` | 380×2302 |
| 6 | Founder | `1:4913` | 380×790 |
| 7 | Comfort | `1:4932` | 380×2909 |
| 8 | Mid CTA | `1:4981` | 380×237 |
| 9 | FAQ | `1:4985` | 380×2261 |
| 10 | Footer | `1:5011` | 380×946 |

Genotyping appears as **last desktop section** (`32:4586`); mobile genotyping may be merged into category flow — **SAFE UNKNOWN** until MCP mobile subtree pass.
