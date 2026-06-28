# FP-0002 V8 O-Centre Subnav Map v1

**Source:** Spig_v1.2 INSTANCE «Тэг» nodes in hero `1:2186`  
**Partial (unchanged):** `internal-page-nav.html` — this document does not modify it.

| Order | Label | Target block | Proposed ID | Source | Status |
|---:|---|---|---|---|---|
| 1 | Кто мы | OC-B03 institutional narrative | `who-we-are` | 1:2241 | CONFIRMED label; ID proposed |
| 2 | Кого мы лечим | OC-B04 who-we-treat | `who-we-treat` | 1:2242 | CONFIRMED |
| 3 | Наш подход к лечению | OC-B06 program approach (`1:2341`) | `our-approach` | 1:2243 | CONFIRMED |
| 4 | Наша программа лечения | OC-B06 program directions (`1:2401`) | `our-program` | 1:2244 | CONFIRMED |
| 5 | Наш Дом | OC-B08 преимущества | `our-home` | 1:2245 | CONFIRMED |
| 6 | Специалисты | OC-B11 | `specialists` | 1:2246 | CONFIRMED |
| 7 | Отзывы | OC-B12 | `reviews` | 1:2247 | CONFIRMED |

## Notes

- Subnav does **not** include steps, comfort, FAQ, or final form — consistent with visible Figma tabs.
- «Наш Дом» maps to subnav label only; scroll target is `1:2440` преимущества section.
- Mobile: sticky behavior not explicitly extracted; defer to CF-003 responsive pattern.
- Production href: in-page `#anchor` only; no cross-page links in subnav.
- Frame `2 - Дом - вступление` is **not** a subnav target despite name similarity.

## Anchor validation

All seven labels map to real blocks in resolved composition except OC-B05 (steps) — **not in subnav**.

**Result:** RESOLVED
