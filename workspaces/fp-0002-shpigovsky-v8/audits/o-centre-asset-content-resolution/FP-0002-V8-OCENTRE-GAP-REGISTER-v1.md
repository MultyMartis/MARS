# FP-0002 V8 O-Centre Gap Register v1

**Task:** FP-0002 V8 O-Centre Asset + Content Resolution  
**Date:** 2026-06-29  
**Source authority:** `Spig_v1.2.fig` (canonical)  
**Extract:** `data/FP-0002-V8-OCENTRE-SPIG-V1-FIG-EXTRACT.json`

| Gap ID | Charter reference | Description | Severity | Source needed | Resolution status |
|---|---|---|---|---|---|
| OC-G01 | OC-B01 hero | Exact hero image fill vs existing V8 assets | Critical | Figma node `1:2226` | **RESOLVED** — `EXPORT_CANONICAL`; not `services-hero.webp` |
| OC-G02 | BLK-037 copy | Institutional/infrastructure narrative copy | Critical | `преимущества` section texts | **RESOLVED** — exact copy from Spig_v1.2 nodes `1:2442`–`1:2477` |
| OC-G03 | BLK-037 assets | Infrastructure photo grid | High | Figma image hashes in `преимущества` | **PARTIAL** — 22 photo refs catalogued; export **PENDING** |
| OC-G04 | BLK-038 copy | Second infrastructure band copy | Critical | Separate BLK-038 frame | **RESOLVED** — merged into single `преимущества` frame on desktop; no separate H2 «Наш Дом» |
| OC-G05 | BLK-038 assets | BLK-038 imagery | High | Same as OC-G03 | **PARTIAL** — shared with OC-G03; mobile «Комфорт, приватность» `1:5697` |
| OC-G06 | OC-B05 / BLK-018 | Rehabilitation steps block copy | Critical | Steps frame in O-Centre design | **BLOCKED** — frame «Этапы процедуры» holds who-we-treat; no BLK-018 steps in Spig_v1.2 O-Centre |
| OC-G07 | OC-B13 FAQ | FAQ accordion vs final form | Critical | Figma `faq` frame | **RESOLVED** — final consultation form only; **no** `faq.html` accordion |
| OC-G08 | OC-B02 subnav | Labels and section anchors | High | Subnav instances `1:2241`–`1:2247` | **RESOLVED** — 7 labels confirmed; anchor IDs proposed at implementation |
| OC-G09 | Image/source map | About-specific image provenance | High | Figma image hashes + repo assets | **PARTIAL** — hero resolved; 22 infrastructure photos catalogued |
| OC-G10 | OC-B09 founder quote | Quote body text | High | Node `1:2301` | **BLOCKED** — Lorem ipsum placeholder in canonical Figma |
| OC-G11 | OC-B06 program | Approach card copy | Medium | Program section nodes | **PARTIAL** — directions confirmed; approach cards contain Lorem ipsum |
| OC-G12 | Figma node IDs | Refresh node map from Spig_v1.2 | Medium | Fresh parse | **RESOLVED** — node map in `data/FP-0002-V8-OCENTRE-FIGMA-NODE-MAP.json` |

**Totals:** 12 gaps tracked · **Resolved:** 6 · **Partial:** 4 · **Blocked:** 2 · **Critical remaining:** OC-G06, OC-G10, OC-G03/05 exports
