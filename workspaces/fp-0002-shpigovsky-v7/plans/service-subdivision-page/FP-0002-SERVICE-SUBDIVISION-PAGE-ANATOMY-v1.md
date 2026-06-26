# FP-0002 Service Subdivision — Page Anatomy v1

Verified against `Spig_v1.2.fig` top-level section frames (not operator hypothesis alone).

## Desktop — `Услуга подраздел` (`1:3491`)

| Order | Block | Figma section | Node | Notes |
|------:|-------|---------------|------|-------|
| 1 | Header | inside `1 - Главный экран` | `1:da4` | Shared site chrome |
| 2 | Service-specific Hero | `1 - Главный экран` | `1:da4` | Inner hero + title/lead/CTA |
| 3 | Breadcrumbs / local nav | inside hero frame | — | Breadcrumb + services subnav pattern |
| 4 | Intro / definition | `2 - Дом - вступление` | `1:de6` | Page intro copy block |
| 5 | Rehabilitation stages | `Этапы процедуры` | `1:e05` | Numbered process cards |
| 6 | Primary services / conditions | `3- Услуги` | `1:e46` | Service list + «Природа зависимости» region |
| 7 | First dark CTA band | `С чего начать` | `1:e68` | Short band (168px) |
| 8 | Program + 4 directions | `Программа центра` | `1:e75` | First program block |
| 9 | Center / team + statistics | `С чего начать` | `1:e9c` | Large composite (1781px) |
| 10 | Supporting + exterior | `Программа центра` | `1:ec0` | Second program/center block |
| 11 | Specialists carousel | `Специаисты` | `1:efc` | Horizontal cards |
| 12 | Founder / expert quote | `Слово спецу` | `1:f21` | Quote block |
| 13 | Comfort / advantages | `преимущества` | `1:f31` | Gallery + copy |
| 14 | Reviews | `Отзывы` | `1:f63` | Program reviews |
| 15 | FAQ | `faq` | `1:f80` | Accordion |
| 16 | Final form | inside `faq` or adjacent | — | Confirm at Pass 1 from frame deep-read |
| 17 | Footer | `Подвал` (INSTANCE) | `1:f97` | Shared footer |
| 18 | Modal | not in frame export | — | Runtime `modal-consultation` |

## Mobile — `Услуга подраздел - моб` (`1:7096`)

| Order | Block | Figma section | Node | Notes |
|------:|-------|---------------|------|-------|
| 1 | Header + Hero | `Моби` | `1:1bb9` | Combined mobile hero shell |
| 2 | Intro / psych block | `Психические расстройствв` | `1:1bef` | Mobile-specific intro stack |
| 3 | Dependencies section | `Зависимости и пристрастия` | `1:1c0d` | Primary service content |
| 4 | First CTA | `С чего начать` | `1:1c35` | |
| 5 | Program | `Программа центра` | `1:1c41` | Stacked directions |
| 6 | Center / team composite | `С чего начать` | `1:1c62` | Different DOM order vs desktop |
| 7 | Approach / supporting | `Подход` | `1:1c8b` | Mobile-only named block |
| 8 | Specialists | `Специаисты` | `1:1cae` | Carousel/stack |
| 9 | Founder quote | `Слово спеца` | `1:1ce5` | |
| 10 | Comfort | `Комфорт, приватность` | `1:1cf8` | |
| 11 | Reviews | `Отзывы` | `1:1d29` | |
| 12 | FAQ | `faq` | `1:1d38` | |
| 13 | Footer | `Подвал моби` | `1:1d4e` | |

## Corrections vs initial hypothesis

- «Two information cards» live inside `3- Услуги` / `Этапы процедуры`, not standalone top-level frames
- Mobile anatomy is **not** a single-column copy of desktop — separate section names and order
- `Этапы процедуры` appears on desktop before `3- Услуги` (not after program heading)
