# REPORT — SITE-002 Neutral Parent Categories Rollout

**Operation:** `SITE-002-PROD-NEUTRAL-PARENT-CATEGORIES-ROLLOUT-01`  
**OCPilot run:** **4.195**  
**Date:** 2026-07-06  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Parent checkpoint:** `SITE-002-STABLE-PROD-CRON-SCHEDULED-RUN-01`  
**SEO baseline:** `SITE-002-STABLE-PROD-SITEMAP-01`  
**New checkpoint:** `SITE-002-STABLE-PROD-NEUTRAL-PARENT-CATEGORIES-01`

---

## 1. Scope

Roll out **four** new neutral parent categories (post–1C import) to homepage `zpm-cat-card` block and neutral hub cards; align `getNeutralHubBranchIds()` with live megamenu/catalog tile set; deploy category WebP masters; admin-bind `oc_category.image` for new branches. **Excluded:** SEO meta, PDP, cron/import, header/footer/Yandex, robots/sitemap.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace `X:\AI MARS` | PASS |
| Volume `AI WS` | PASS |
| Branch `mars/canonical-post-recovery` | PASS |
| Staged files before task | empty |
| Foreign WIP | excluded from commit |

---

## 3. New parent category inventory

After 1C import, megamenu/catalog dropdown (`zpm-catalog__tile`) already showed **9** branches with products; homepage/hub `zpm-cat-card` remained at **5** (hardcoded IDs).

| ID | Name | Slug | Products (megamenu) | Image before |
|---:|------|------|--------------------:|--------------|
| 331 | Полки настенные и настольные | `polki-nastennye-i-nastolnye` | 160 | placeholder |
| 354 | Тележки-шпильки и противни | `telezhki-shpilki-i-protivni` | 9 | placeholder |
| 358 | Шкафы и лари | `shkafy-i-lari` | 2 | placeholder |
| 86 | Стеллажи | `stellazhi` | 248 | placeholder |

**Not rolled out** (legacy/empty duplicates): `lari`, `podtovarniki`, `polki`, `shkafy`, `stoly-proizvodstvennye`, `telezhki` — zero-product or superseded slugs; remain hidden from hub list by `getTotalProducts()` filter.

IDs resolved from live `cat-list-header` cache (FTP read-only).

---

## 4. Tile authority map

| Surface | Authority | Changed |
|---------|-----------|---------|
| Homepage `zpm-cat-card` | `CategoryVisibility::buildHomepageCategoryCards()` | **yes** — via branch ID list |
| Neutral hub `zpm-cat-card` | `category.php` hub → `getNeutralHubBranchIds()` | **yes** — same list |
| Catalog megamenu `zpm-catalog__tile` | `cat-list-header` + `prepareMegamenuCategories()` | **no** — already dynamic |

Single file: `/public_html/system/library/zpm/category_visibility.php` — `$neutral_hub_branch_ids`.

---

## 5. Existing image style audit

| Spec | Value |
|------|-------|
| Master format | WebP |
| Master canvas | 1800×1200 (H=1200) |
| Storefront cache | 300×300 via OpenCart resize |
| Path | `image/catalog/Category-image/{slug}.webp` |
| Reference tiles | 5 existing branch WebPs (4–7 KB cache) |

---

## 6. Composer-only image generation

**Mode:** `COMPOSER_ONLY_NO_API` — Cursor Composer visual generation + local Pillow normalize. **No external OpenAI/DALL-E/API.**

| File | SHA-256 (prefix) | Bytes |
|------|------------------|------:|
| `stellazhi.webp` | `816a5919…` | 153960 |
| `polki-nastennye-i-nastolnye.webp` | `b418022b…` | 101968 |
| `shkafy-i-lari.webp` | `48db95ad…` | 142498 |
| `telezhki-shpilki-i-protivni.webp` | `ca23f935…` | 154276 |

**Operator note:** side-by-side visual HITL against M9.7B references recommended (image weight/detail differs from legacy 3D masters).

---

## 7. Implementation plan

1. Upload 4 WebP masters to `/public_html/image/catalog/Category-image/`
2. Patch `$neutral_hub_branch_ids` → `322, 331, 301, 326, 354, 358, 207, 80, 86` (megamenu live order)
3. Admin-save `oc_category.image` for categories 86, 331, 354, 358
4. HTTP verify home / katalog / neutral hub

---

## 8. Backup / before evidence

| Artefact | Location |
|----------|----------|
| Live `category_visibility.php` | Storage `…/backup/` + `rollback/` |
| HTML before | Storage `…/html-before/` |
| Tile diff (5 vs 9) | Storage `…/category-inventory/tile-diff.json` |

---

## 9. Dry-run

| Item | Before | After |
|------|-------:|------:|
| Homepage `zpm-cat-card` | 5 | 9 |
| Neutral hub `zpm-cat-card` | 5 | 9 |
| Remote deletes | 0 | 0 |

---

## 10. Deploy / admin actions

| Action | Result |
|--------|--------|
| FTP upload 4 images | PASS |
| FTP upload `category_visibility.php` | PASS |
| Admin image field 86, 331, 354, 358 | **4/4 PASS** (JS set hidden `#input-image` + save) |

---

## 11. Post-deploy verification

| Check | Result |
|-------|--------|
| Home HTTP 200, 9 cat cards | PASS |
| Hub HTTP 200, 9 cat cards | PASS |
| New images non-placeholder on home/hub | PASS |
| `/katalog` megamenu 9 tiles | PASS |
| Load-more PLP sample (`stoly`) | not re-run — unchanged scope |

Evidence: Storage `…/verification/post-deploy-verification.json`

---

## 12. Yandex / duplicate body preservation

| Check | Result |
|-------|--------|
| Yandex.Webmaster meta | present |
| Yandex.Metrika | present |
| Single `<body>` | 1 |
| header.twig / footer.twig | **not modified** |

---

## 13. Robots / sitemap preservation

| Resource | Result |
|----------|--------|
| robots.txt | 200, `Sitemap:` present |
| sitemap.xml | valid XML |

**No changes** by this operation.

---

## 14. Product/PDP exclusion proof

No `product.php`, PDP Twig, import, or product data touched. Scope limited to `category_visibility.php`, category images, and category admin image fields.

---

## 15. Rollback status

**Ready** — restore `rollback/category_visibility.php`; remove 4 new WebP files if needed; clear admin image fields for 86/331/354/358. **Not executed.**

---

## 16. Remote mutation summary

| Metric | Count |
|--------|------:|
| Remote uploads | 5 |
| Remote overwrites | 1 (`category_visibility.php`) |
| Remote new image files | 4 |
| Remote deletes | 0 |
| Remote renames | 0 |
| Admin saves (category image only) | 4 |
| DB direct operations | 0 |
| Header/footer changes | 0 |
| Yandex changes | 0 |
| Robots changes | 0 |
| Sitemap changes | 0 |
| SEO meta changes | 0 |
| Product/PDP changes | 0 |
| Cron/import changes | 0 |
| Mail changes | 0 |
| Cache clears | 0 |
| External image API calls | 0 |
| Image generation mode | **COMPOSER_ONLY_NO_API** |

---

## 17. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEUTRAL-PARENT-CATEGORIES-ROLLOUT-01\`

---

## 18. Authority updates

Checkpoint **`SITE-002-STABLE-PROD-NEUTRAL-PARENT-CATEGORIES-01`** issued. Docs/index updated (Run 4.195).

---

## 19. Git status

Repo docs + tool + report + baseline staged selectively. Storage artefacts **not** in git.

---

## 20. SAFE UNKNOWN / blockers

- Operator visual HITL on new WebP quality vs legacy M9.7 tiles — **recommended**, not blocking HTTP verification.
- Legacy empty slugs (`polki`, `lari`, …) remain in DB/sitemap but excluded from hub cards by product filter — **by design**.

---

## 21. Final verdict

**SITE-002 NEUTRAL PARENT CATEGORIES ROLLOUT COMPLETE — TILES AND IMAGES VERIFIED**

---

## 22. Next task recommendation

**SITE-002-PROD-SEO-INFORMATION-META-FIX-01** — resume non-product SEO meta chain after category structure stabilised.
