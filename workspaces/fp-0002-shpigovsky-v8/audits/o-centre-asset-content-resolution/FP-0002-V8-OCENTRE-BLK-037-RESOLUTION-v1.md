# FP-0002 V8 O-Centre BLK-037 Resolution v1

**Inventory reference:** BLK-037 (institutional/infrastructure narrative)  
**Charter block:** OC-B08 (partial)  
**Figma authority:** Spig_v1.2 desktop frame `1:2440` «преимущества»

## Finding

On Spig_v1.2, BLK-037 content is **not** a separate top-level section. It is the **first narrative portion** of the unified `преимущества` frame (`1:2440`), together with BLK-038 imagery. Subnav label «Наш Дом» (`1:2245`) targets this section; there is **no** separate H2 «Наш Дом» in body copy.

## Resolution table

| Field | Value | Source | Confidence |
|---|---|---|---|
| Design title | преимущества | Frame `1:2440` | CONFIRMED |
| Heading | Место, где лечение начинается с ощущения безопасности | Text `1:2442` | CONFIRMED |
| Lead | Среда восстановления — это не декорация. Это часть работы… | Text `1:2446` | CONFIRMED |
| Bullet 1 | «Шпиговский Дом» расположен в ближнем Подмосковье… | Instance `1:2449` | CONFIRMED |
| Bullet 2 | Мы убеждены, что физическое движение и качество отдыха… | Instance `1:2456` | CONFIRMED |
| Bullet 3 | Клиенты размещаются в комфортных комнатах… | Instance `1:2463` | CONFIRMED |
| Bullet 4 | Повар готовит три раза в день… | Instance `1:2470` | CONFIRMED |
| Bullet 5 | Территория огорожена и находится под круглосуточным видеонаблюдением… | Instance `1:2477` | CONFIRMED |
| Brand typography | Шпиг / вскиЙ / дом / центр профилактики зависимостей | `1:2481`–`1:2487` | CONFIRMED |
| Images | 22 photo instances (этап) with distinct hashes | `desktopSectionImages.преимущества` | CONFIRMED refs; export PENDING |
| Desktop layout | Single tall section 1437×3621 with text + photo grid | Frame `1:2440` | CONFIRMED |
| Mobile layout | Frame «Комфорт, приватность» `1:5697` 390×4958 | mobileSections | PROBABLE |
| Relation to OC-B08 | Same frame as BLK-038 imagery | Anatomy | CONFIRMED |
| Relation to founder quote | Founder quote is **before** this section in `3- Услуги` (`1:2301`) | Section order | CONFIRMED |
| Separate from BLK-038 | Narrative copy only; photos shared in one frame | Figma anatomy | CONFIRMED |
| Order vs founder quote | Founder quote **precedes** infrastructure section | Desktop order | CONFIRMED |

## Status

**COPY RESOLVED** · **ASSETS PARTIAL (PENDING export)**

Implementation note (documentation only): one unique partial for OC-B08 is consistent with Figma; splitting BLK-037/038 into two partials would be **inventory-driven**, not Figma-driven.
