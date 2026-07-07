# REPORT — SITE-002 Category Entrypoints Sort А→Я

**Operation:** `SITE-002-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01`  
**OCPilot run:** 4.221  
**Date:** 2026-07-08  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Baseline before:** `SITE-002-STABLE-PROD-NEW-SECTIONS-ENTRYPOINTS-02`  
**Mode:** Controlled display-order patch only (no category data / image / admin / DB changes)

---

## 1. Scope

Sort visible category entrypoints **А → Я** by Russian category name on three surfaces:

| Surface | Authority |
|---------|-----------|
| Megamenu neutral-equipment children | `CategoryVisibility::prepareMegamenuCategories()` |
| Homepage `zpm-cat-card` grid | `CategoryVisibility::buildHomepageCategoryCards()` |
| Neutral hub `zpm-cat-card` grid | `category.php` hub branch loop → `hub_categories` |

**In scope:** PHP sort helper + controller/library calls; live verification.  
**Out of scope:** category names/slugs/IDs/structure/meta, images, PDP, header/footer/Yandex, sitemap/robots/llms, DB, admin.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` — **PASS** |
| Volume | `X:` — label **AI WS** — **PASS** |
| Branch | `mars/canonical-post-recovery` — **PASS** |
| Staged files before task | **empty** — **PASS** |
| Foreign WIP | FP-0002 / `.recovery-temp` — **not staged, not touched** |

---

## 3. Live before snapshot

| Page | HTTP | Cards | Order A→Я | Лари | Кондитерский инвентарь |
|------|------|-------|-----------|------|------------------------|
| Homepage | 200 | **11** | **No** (whitelist/manual) | Yes | Yes |
| Neutral hub | 200 | **11** | **No** | Yes | Yes |

**Before order (home/hub):** Подтоварники → Полки → Столы → Тележки сервировочные → Тележки-шпильки → Шкафы и лари → Зонты → Моечные → Стеллажи → Лари → Кондитерский инвентарь

**Artefacts:** `http-before/*`

---

## 4. Source authority discovery

| Surface | File | Method |
|---------|------|--------|
| Shared sort + homepage + megamenu | `/public_html/system/library/zpm/category_visibility.php` | `sortCategoriesByRussianName()`, `buildHomepageCategoryCards()`, `prepareMegamenuCategories()` |
| Neutral hub cards | `/public_html/catalog/controller/product/category.php` | `$is_hub` branch → `$data['hub_categories']` |
| Megamenu data prep | `/public_html/catalog/controller/common/header.php` | `prepareMegamenuCategories(unserialize($catlist), $this)` |

**Order before patch:** whitelist ID sequence in `$neutral_hub_branch_ids` (membership only; not display sort).  
**Modification overlays:** not present for touched live files.

**Artefacts:** `source-before/`, `manifests/source-authority-map.*`

---

## 5. Sort design

- Rule: Russian alphabet **А → Я** by visible category `name`
- Case-insensitive; trim whitespace; **Ё → Е**
- Whitelist `$neutral_hub_branch_ids` remains **membership-only** (11 IDs unchanged)
- Sort applied in PHP before Twig render
- `Collator('ru_RU')` when available; `strcmp` on normalized UTF-8 fallback

**Artefacts:** `manifests/sort-design.{md,json}`

---

## 6. Expected A→Я order

1. Зонты вытяжные  
2. Кондитерский инвентарь  
3. Лари  
4. Моечные ванны  
5. Подтоварники и подставки  
6. Полки настенные и настольные  
7. Стеллажи  
8. Столы  
9. Тележки сервировочные  
10. Тележки-шпильки и противни  
11. Шкафы и lари  

**Artefacts:** `verification/expected-*-order.csv`

---

## 7. Patch plan and rollback

| Remote file | Change |
|-------------|--------|
| `category_visibility.php` | Add Russian sort helper; sort homepage cards + megamenu children |
| `category.php` | Sort `hub_categories` after hub branch build |

Rollback: re-upload exact `source-before` copies.

**Artefacts:** `rollback/*`, `patch/diff-*.diff`

---

## 8. Local patch summary

| File | SHA before → after |
|------|-------------------|
| `category_visibility.php` | `0c6eada3…` → `13890f98…` |
| `category.php` | `441c5f82…` → `e1d4a694…` |

PHP syntax check: **PASS** (both files, `php -l`).

No `БЗПМ` introduced. Header/footer templates **not** edited.

---

## 9. Dry-run gates

All gates **PASS** (G1–G12). See `manifests/dry-run.json`.

---

## 10. Controlled deploy

| Metric | Value |
|--------|-------|
| Remote uploads | **2** exact files |
| Remote overwrites | **2** |
| Remote deletes | **0** |
| Upload SHA verify | **PASS** |

**Artefacts:** `verification/upload-manifest.*`, `verification/remote-after-sha.json`

---

## 11. Live verification after

| Page | HTTP | Cards | Order A→Я |
|------|------|-------|-----------|
| Homepage | 200 | **11** | **Yes** |
| Neutral hub | 200 | **11** | **Yes** |

---

## 12. Homepage card order verification

**PASS** — 11 cards; membership unchanged; order matches expected A→Я list; Лари and Кондитерский инвентарь present; images HTTP 200; no placeholders.

---

## 13. Neutral hub card order verification

**PASS** — same 11 links as homepage; order A→Я; images unchanged.

---

## 14. Megamenu order verification

**PASS** — live `zpm-catalog__tile-title` sequence on homepage HTML matches A→Я (11 neutral branches: Зонты → … → Шкафы и лари). Лари and Кондитерский инвентарь present.

**Note:** automated CSV extractor targeted legacy menu-link markup; megamenu verified via live tile titles in `home-after.html`.

---

## 15. Sanity checks

| URL | Result |
|-----|--------|
| `/katalog/nejtralnoe-oborudovanie/stoly` | 200; Load More **present** |
| PDP derzhatel sample | 200; `product-content__extra-info` **present** |
| `/llms.txt` | 200; UTF-8 BOM; **БЗПМ 0** |
| `/robots.txt` | 200 |
| `/sitemap.xml` | 200; **1377** URLs |

---

## 16. Brand regression check

Public **БЗПМ** count on homepage/hub/llms: **0**. Correct brand **ЗПМ** policy preserved.

---

## 17. PDP extra-info preservation

Run **4.218** layout preserved — separate `product-content__extra-info` block on sample PDP.

---

## 18. Rollback status

**Not required.** Rollback bundle ready under deployment storage `rollback/`.

---

## 19. Production mutation summary

| Category | Count / status |
|----------|----------------|
| Remote uploads | 2 exact files |
| Remote overwrites | 2 exact files |
| Remote deletes | 0 |
| Admin saves | 0 |
| DB direct operations | 0 |
| Category membership changes | **0** |
| Category display order changes | **yes** (3 surfaces) |
| Images generated/uploaded | 0 |
| PDP template changes | 0 |
| Header/footer changes | 0 |
| Yandex changes | 0 |
| Sitemap/robots/llms changes | 0 |
| Cache clears | 0 |
| public БЗПМ introduced | **no** |

---

## 20. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01\`

---

## 21. Authority updates

- Category entrypoints on megamenu, homepage, and neutral hub **must display А → Я** by Russian name.
- `$neutral_hub_branch_ids` remains membership whitelist only (11 IDs).
- Sort authority: `CategoryVisibility::sortCategoriesByRussianName()`.

---

## 22. Git status

Repository report/docs/checkpoint/tool updated; Storage artefacts not committed.

---

## 23. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Megamenu automated CSV parser | Legacy selector — tile markup verified manually in HTML |
| OpenCart modification cache refresh | Not required — live output updated without cache clear |

---

## 24. Final verdict

**SITE-002 CATEGORY ENTRYPOINTS SORT AZ COMPLETE — HOME HUB MEGAMENU VERIFIED**

---

## 25. Next task recommendation

- Optional: improve deploy-tool megamenu parser for `zpm-catalog__tile-title` markup.
- No further category entrypoint work unless new branches added to whitelist.

**Checkpoint issued:** `SITE-002-STABLE-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01`
