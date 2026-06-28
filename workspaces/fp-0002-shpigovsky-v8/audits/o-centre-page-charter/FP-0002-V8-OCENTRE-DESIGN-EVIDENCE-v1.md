# FP-0002 V8 O-Centre Design Evidence v1

**Date:** 2026-06-29
**Canonical design file:** `Spig_v1.2.fig` (not modified)
**Historical file:** `Шпиговский.fig` — not used as authority

---

## Figma page / frame identification

| Attribute | Desktop | Mobile |
|---|---|---|
| Figma canvas | Page 1 (top-level frames) | Page 1 |
| Frame name | **О центре** | **О центре - моб** |
| Forensic ID | PG-04 | PG-15 |
| Dimensions (W×H) | 1437 × 12830 | 390 × 16586 (content width 380 in child frames) |
| Nested frames (forensic) | 198 | (mobile page-like cluster) |
| PDF pairing | `О центре.pdf` (SOURCE-011) | `О центре - моб.pdf` (SOURCE-012, 390 px artifact) |

**Figma file path:** `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig`

---

## Desktop direct-child sections (parse evidence)

Source: `_fig_audit_page_sections_v2.json` — frame «О центре».

| Idx | Figma section name | W×H | Inventory BLK map (best fit) |
|---:|---|---|---|
| 1 | 1 - Главный экран | 1441×905 | BLK-007ˢ Service/About hero |
| 2 | 2 - Дом - вступление | 1437×761 | BLK-036 «Кто мы» (intro band) |
| 3 | 3- Услуги | 1437×1131 | BLK-036/who-we-treat narrative slot (category list — not services hub) |
| 4 | Этапы процедуры | 1440×598 | BLK-018 Rehabilitation steps |
| 5 | С чего начать | 1441×168 | BLK-019 CTA fragment / spacer |
| 6 | Программа центра | 1437×1837 | BLK-020 Program four directions |
| 7 | Программа центра | 1437×1519 | BLK-019 Guest visit CTA band (second program-related band) |
| 8 | преимущества | 1437×3621 | BLK-037 «Наш Дом» + BLK-038 Infrastructure (combined visual band) |
| 9 | С чего начать | 1441×107 | CTA spacer / divider |
| 10 | Специаисты | 1437×561 | BLK-026 Specialists preview |
| 11 | Отзывы | 1435×429 | BLK-015 Reviews preview |
| 12 | faq | 1440×366 | BLK-034 FAQ (**present in Figma; omitted from PG-005 inventory row**) |
| 13 | Подвал (INSTANCE) | 1440×488 | BLK-003 Footer |

**Not visible as top-level desktop sections:** BLK-005 breadcrumbs, BLK-006 in-page nav (expected inside hero/chrome band), BLK-022 founder/expert quote, BLK-023 comfort as separate label (likely inside «преимущества» / mobile «Комфорт»).

---

## Mobile direct-child sections (parse evidence)

Source: `_fig_audit_page_sections_v2.json` — frame «О центре - моб».

| Idx | Figma section name | W×H | Notes |
|---:|---|---|---|
| 1 | Моби | 380×604 | Mobile hero |
| 2 | Зависимости и пристрастия | 380×1914 | Who-we-treat / addictions narrative |
| 3 | Кого мы лечим | 380×1405 | Condition spectrum body |
| 4 | С чего начать | 380×303 | CTA band |
| 5 | Подход | 380×1848 | Treatment approach narrative |
| 6 | Программа центра | 380×2184 | Program block |
| 7 | Комфорт, приватность | 390×4958 | BLK-023 comfort mosaic |
| 8 | Специаисты | 380×514 | Specialists |
| 9 | Отзывы | 380×398 | Reviews |
| 10 | faq | 380×712 | FAQ |
| 11 | Подвал моби | 380×946 | Footer |

Mobile clarifies desktop merge: **comfort gallery is explicit**; **approach narrative** is a distinct band.

---

## Canonical inventory composition (PG-005)

From `FP-0002-BLOCK-INVENTORY-v1.md` — scroll order **without** global chrome duplication:

`005, 006, 007ˢ, 036, 037, 038, 020, 018, 022, 023, 026, 015, 019` (+ global 001, 002, 003, 004)

**Inventory vs Figma delta:**

| Item | Inventory | Figma desktop | Resolution |
|---|---|---|---|
| FAQ BLK-034 | Not listed on PG-005 row | Present (section 12) | **CONFLICT** — charter includes FAQ as Figma-confirmed tail; operator may approve omission |
| Final form BLK-035 | Not listed | Not in top-level sections | Likely not on About design |
| Founder BLK-022 | Listed | Not top-level named section | May be embedded in narrative bands — **UNRESOLVED placement** |
| Comfort BLK-023 | Listed | Named on mobile only | Desktop folded into «преимущества» |

---

## Existing exports / screenshots in repo

| Asset | Path | Use |
|---|---|---|
| Section parse JSON | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/_fig_audit_page_sections_v2.json` | Section order |
| Figma forensic | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-FIGMA-FORENSIC-TEST-v1.md` | Frame sizes |
| Design audit PG-005 | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-DESIGN-AUDIT-v1.md` | Block ID list |
| V8 `src/assets/design/` | **Not present** in V8 workspace | No local design folder exports |

**STORAGE evidence path (reserved, not populated in this task):** `C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\o-centre-charter-evidence\`

---

## Missing / conflicting design inputs

| Gap | Status |
|---|---|
| Fresh Figma node IDs for «О центре» frames | **UNRESOLVED** — use forensic names; re-parse Spig_v1.2.fig in asset prep if IDs needed |
| PDF copy extraction in git | **MISSING_SOURCE** in V8 tree — PDFs referenced by ops pack only |
| About subpage designs (6 URLs) | **NONE** — XLSX only (CF-006) |
| Desktop/mobile FAQ inclusion vs inventory | **CONFLICT** documented above |
| Exact hero image for About | **UNRESOLVED** — V7 WIP reused `services-hero.webp`; design may differ |
