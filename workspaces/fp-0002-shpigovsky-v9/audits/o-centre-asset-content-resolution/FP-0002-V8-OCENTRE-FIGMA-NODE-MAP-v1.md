# FP-0002 V8 O-Centre Figma Node Map v1

**Canonical source:** `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig`  
**Fig SHA-256:** `bae5d91c74b5a22afc610f7c7845b9badc6b87ec8da85c5705ecf4eec4de3041`  
**Machine-readable:** `data/FP-0002-V8-OCENTRE-FIGMA-NODE-MAP.json`

## Page frames

| Frame | Node ID | Size |
|---|---|---|
| Desktop «О центре» | `1:2185` | 1437×12830 |
| Mobile «О центре - моб» | `1:5519` | 390×16586 |

## Block map

| Block | Desktop node | Mobile node | Text nodes | Image refs | Confidence |
|---|---|---|---|---:|---|
| OC-B01 Hero | `1:2186` | `1:5520` | `1:2230`–`1:2239`, tabs in hero | `1:2226` hero, `1:2190` logo | CONFIRMED |
| OC-B02 Subnav | `1:2241`–`1:2247` | (in mobile hero) | 7× INSTANCE «Тэг» | — | CONFIRMED |
| OC-B03 Institutional | `1:2279` «3- Услуги» | `1:5569` | `1:2282`–`1:2294` | section bg `1:2279` | CONFIRMED |
| OC-B04 Who we treat | `1:2310` «Этапы процедуры» | `1:5604` | `1:2323`–`1:2321` | — | CONFIRMED |
| OC-B05 Steps BLK-018 | — | — | — | — | UNRESOLVED |
| OC-B06 Program | `1:2341`, `1:2401` | `1:5629`, `1:5664` | program + approach texts | multiple | CONFIRMED |
| OC-B07 CTA band | `1:2328`, `1:2509` | `1:5617` | `1:2511` | `1:2511` | PROBABLE |
| OC-B08 Infrastructure | `1:2440` «преимущества» | `1:5697` «Комфорт, приватность» | `1:2442`–`1:2487` | 23 image nodes | CONFIRMED |
| OC-B09 Founder quote | `1:2301`–`1:2309` (inside `1:2279`) | `1:5569` | quote + attribution | — | CONFIRMED structure; quote body UNREADABLE |
| OC-B10 Comfort | (embedded in desktop `1:2440`) | `1:5697` | mobile-only frame name | shared with OC-B08 | PROBABLE |
| OC-B11 Specialists | `1:2512` | `1:5848` | instance overrides | `1:2524` etc. | CONFIRMED |
| OC-B12 Reviews | `1:2549` | `1:5903` | review instances | — | CONFIRMED |
| OC-B13 Final form | `1:2578` «faq» | `1:5918` | `1:2581`–`1:2592` | — | CONFIRMED |

## Desktop section order (direct children of `1:2185`)

1. `1:2186` — 1 - Главный экран  
2. `1:2248` — 2 - Дом - вступление (image-only; no extracted text)  
3. `1:2279` — 3- Услуги  
4. `1:2310` — Этапы процедуры  
5. `1:2328` — С чего начать  
6. `1:2341` — Программа центра (approach)  
7. `1:2401` — Программа центра (directions)  
8. `1:2440` — преимущества  
9. `1:2509` — С чего начать (guest visit)  
10. `1:2512` — Специаисты  
11. `1:2549` — Отзывы  
12. `1:2578` — faq  
13. Footer instance  

## Limitations

- Historical parse from `Шпиговский.fig` **not** used for node IDs.
- Mobile text extraction used frame names; full mobileSectionTexts not in extract — desktop texts cross-referenced where strings match.
- Frame `2 - Дом - вступление` has background hash only; narrative text lives in `3- Услуги`.

**Result:** Exact node IDs extracted for all major sections except BLK-018 steps (absent).
