# REPORT — SITE-002 UX Task Intake: New Sections + PDP Extra Info

**Operation:** `SITE-002-PROD-UX-TASK-INTAKE-01`  
**OCPilot run:** 4.217  
**Date:** 2026-07-07  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Baseline:** `SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01`  
**Mode:** read-only intake — **no Production mutation**

---

## 1. Scope

Controlled read-only intake for two operator UX tasks:

1. **New sections** — prepare entry points (images + homepage/catalog tiles) for **Лари** and **Кондитерский инвентарь**.
2. **PDP attribute** — «Дополнительные сведения» behaves like mini-description inside specs table; future work moves it below `product-content__specs-toggle-wrap` without DB/data changes.

**Excluded:** all Production mutation, image generation, template/CSS patch, admin save, DB write, cache clear, header/footer/Yandex.

---

## 2. Operator backup confirmation

| Item | Status |
|------|--------|
| Beget full backup of current site state | **Confirmed by operator** before this task |
| Backup used as mutation permission | **No** — intake remained read-only |

---

## 3. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` — **PASS** |
| Volume | `X:` — label **AI WS** — **PASS** |
| Branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD (start) | `9c5d95104ffff5cb9e281d6872606c281bb2e10d` |
| Staged files before task | **empty** — **PASS** |
| Foreign WIP | FP-0002 / `.recovery-temp` — **not staged, not touched** |

---

## 4. Task 01 public page inventory

**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-UX-TASK-INTAKE-01\task-01-new-sections\`

| Page | HTTP | H1 | `zpm-cat-card` count | Lari/Konditerskiy on tile grid |
|------|------|-----|----------------------|--------------------------------|
| Homepage | 200 | Оборудование для общепита… | **9** | **No** |
| `/katalog` | 200 | Каталог оборудования… | 1 (neutral root) | Megamenu only |
| Neutral hub | 200 | Нейтральное оборудование | **9** | **No** |
| `/lari` | 200 | Лари | 0 | N/A (PLP) |
| `/lari/skladskie-lari` | 200 | Складские | 0 | N/A |
| `/lari/proizvodstvennye-lari` | 200 | Производственные | 0 | N/A |
| `/konditerskiy-inventar` | 200 | Кондитерский инвентарь | 0 | N/A |
| `/formy-konditerskie` | 200 | Формы кондитерские | 0 | N/A |

**Findings:**

- New branch PLPs are **live HTTP 200** with onboarded meta (Runs 4.210–4.211).
- **Лари** and **Кондитерский инвентарь** appear in **megamenu** HTML but are **absent** from homepage and neutral-hub `zpm-cat-card` grids (9 tiles each — same set as Run 4.195).
- Existing tile pattern: `zpm-cat-card` + `image/cache/catalog/Category-image/{slug}-300x300.webp`.
- `/katalog` root shows only neutral-equipment root card — new sections are reached via megamenu or direct URL, not catalog root tiles.

---

## 5. Task 01 source authority

**Storage:** `task-01-new-sections/source-authority-map.{csv,json,md}` + `source-readonly/`

| Block | Authority | Generation |
|-------|-----------|------------|
| Homepage category grid | `home.php` → `CategoryVisibility::buildHomepageCategoryCards()` → `catalogsections.twig` | Data-driven whitelist |
| Neutral hub branch tiles | `category.php` + same visibility library | Data-driven whitelist |
| Branch whitelist | `system/library/zpm/category_visibility.php` → `$neutral_hub_branch_ids` | **HARDCODED** PHP array |
| Tile markup | `sections/catalogsections.twig` | Twig `{% for %}` over `$data['categories']` |
| Modification overlays (home/category) | **Not present** on FTP for inspected paths | Live files authoritative |

**Current `$neutral_hub_branch_ids` (live):** `322, 331, 301, 326, 354, 358, 207, 80, 86` (9 IDs — matches 9 visible tiles).

**Category IDs for new parent tiles (from Runs 4.210–4.211):**

| Section | category_id |
|---------|-------------|
| Лари | **88** |
| Кондитерский инвентарь | **360** |

**Adding entry points** is likely **hybrid**: extend `neutral_hub_branch_ids` + upload **admin category images** (same pattern as Run 4.195). **Not** hardcoded Twig cards.

**Protected:** `header.twig` / `footer.twig` — **not inspected or touched**.

---

## 6. Task 01 image requirements

**Storage:** `task-01-new-sections/image-requirements.{csv,json,md}`, `image-production-plan.md`

| Section | Tile on home/hub | Image needed for entry |
|---------|------------------|------------------------|
| Лари (parent) | No | **Yes** — 300×300 WebP cache from category master |
| Кондитерский инвентарь (parent) | No | **Yes** |
| Складские / Производственные лари | No (child PLPs) | Optional — hub tiles use **parent** only |
| Формы кондитерские | No (child PLP) | Optional |

**Analogous reference:** `podtovarniki-i-podstavki-300x300.webp` (white-background studio style from Runs 4.196–4.197).

**Convention:** master `image/catalog/Category-image/{slug}.png` → cache `image/cache/catalog/Category-image/{slug}-300x300.webp`.

**No images generated in this intake.**

---

## 7. Task 01 implementation options

**Storage:** `implementation-options/task-01-new-sections-options.{md,json}`

| Option | Verdict |
|--------|---------|
| **A/C Hybrid** — branch IDs + admin images | **Recommended** (Run 4.195 precedent) |
| B — hardcoded Twig cards | **Not recommended** (duplicates data-driven system) |

**Future operation:** `SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-01`

---

## 8. Task 02 PDP observation

**Example URL:** operator PDP (держатель гастроёмкостей ПГ-10/3)

**Storage:** `task-02-extra-info/example-pdp-observation.{md,json}`, `example-pdp-dom-snippet.html`

| Field | Value |
|-------|-------|
| HTTP | **200** |
| Body classes | `page page--product category-root-79 category-parent-331` |
| «Дополнительные сведения» | **Present** in `spec-table__row` |
| Value length | **242** chars (multi-line prose) |
| Position | **Inside** specs table, **before** `product-content__specs-toggle-wrap` |
| Layout impact | Long prose row breaks compact key/value table rhythm |
| Specs toggle | Present (`data-product-specs-toggle`); wrap has `hidden` when collapsed |

Observed value matches operator example (AISI 430, стопор, крепление к полке ПН).

---

## 9. Task 02 source authority

**Storage:** `task-02-extra-info/source-authority-map.{csv,json,md}` + `source-readonly/`

| Layer | File | Status |
|-------|------|--------|
| Controller | `catalog/controller/product/product.php` | Downloaded — loads `getProductAttributes()`, sets `$data['attribute_groups']` |
| Model | `catalog/model/catalog/product.php` | Downloaded — `getProductAttributes()` grouped query |
| Twig shell | `product/product.twig` | Downloaded — delegates to `producthero` + `producttabs` |
| Spec table markup | **SAFE UNKNOWN exact partial** — live DOM in `product-content__specifications`; `producttabs.twig` not in this FTP pull; download required in implementation op |
| Modification overlays | `storage/modification/.../product.*` | **Absent** (550) — live paths authoritative |
| JS toggle | `main.js` — `.product-content__specs-toggle-wrap` | Existing capture confirms selector scope |

**Attribute flow:** `getProductAttributes()` → `$data['attribute_groups']` → Twig `spec-table` loop.

**Meta generator note:** `product.php` also uses `attribute_groups` for meta description/keywords — extraction for display must **not** remove attribute from meta helper inputs unless explicitly scoped to display-only filter.

---

## 10. Task 02 data scope

**Storage:** `task-02-extra-info/attribute-scope-sample.{csv,json,md}`

| Metric | Value |
|--------|-------|
| Sample method | Random 100 PDP URLs from live sitemap |
| Sample size | **100** |
| With «Дополнительные сведения» | **66** (**66%**) |
| Without | **34** |
| HTTP 200 | 100/100 |

Attribute is **widespread** — implementation must handle **all products dynamically** by exact attribute name match, not a fixed URL list.

Value previews are typically 80–250 char material/construction prose from 1C import.

---

## 11. Task 02 implementation options

**Storage:** `implementation-options/task-02-extra-info-options.{md,json}`

| Option | Verdict |
|--------|---------|
| **A — Controller extraction** | **Recommended** — filter from display `attribute_groups`; pass `$data['extra_info_attribute']`; render after toggle wrap |
| B — Twig-only skip | Possible but weaker for grouped structure |
| C — CSS-only hide | **Unacceptable** — wrong semantics |

**JS toggle impact:** Low if extra-info block is **outside** the collapsed `spec-table` region targeted by toggle.

**Future operation:** `SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01`

---

## 12. Future note: server-side monitor migration

**Storage:** `future-notes/server-side-monitor-migration-deferred.{md,json}`

| Item | Status |
|------|--------|
| Current | Local Windows Task Scheduler monitor (Runs 4.215–4.216) — **accepted** |
| Future | Move post-1C monitor to server-side runtime |
| Operation name | `SITE-002-PROD-SERVER-MONITOR-READINESS-01` |
| Status | **DEFERRED** — not part of current work |

---

## 13. Future task charters

**Storage:** `manifests/future-task-charters.{md,json}`

### A. SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01

Move «Дополнительные сведения» out of specs table into separate block below `product-content__specs-toggle-wrap`. No DB/admin/product data changes.

### B. SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-01

Add parent tile images + `category_visibility.php` branch IDs for Лари (88) and Кондитерский инвентарь (360). Verify home + neutral hub responsive layout. Depends on image assets.

---

## 14. Production mutation summary

| Operation | Count |
|-----------|------:|
| Remote uploads | 0 |
| Remote overwrites | 0 |
| Remote deletes | 0 |
| Remote renames | 0 |
| Admin saves | 0 |
| DB direct operations | 0 |
| Product PDP changes | 0 |
| Product generator changes | 0 |
| Category meta changes | 0 |
| Category structure changes | 0 |
| Category status changes | 0 |
| Category URL/slug changes | 0 |
| Images generated/uploaded | 0 |
| Homepage changes | 0 |
| Catalog changes | 0 |
| PDP template changes | 0 |
| llms.txt changes | 0 |
| Header/footer changes | 0 |
| Yandex.Metrika/Webmaster changes | 0 |
| Robots changes | 0 |
| Sitemap changes | 0 |
| Cron/import runs | 0 |
| Mail changes | 0 |
| Cache clears | 0 |
| Manual sitemap edits | 0 |

---

## 15. Storage artefacts

Root: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-UX-TASK-INTAKE-01\`

| Path | Contents |
|------|----------|
| `manifests/operation.json` | Operation manifest |
| `task-01-new-sections/` | Public inventory, source map, image requirements |
| `task-02-extra-info/` | PDP observation, source map, attribute scope sample |
| `implementation-options/` | Options A/B/C for both tasks |
| `future-notes/` | Server monitor deferred note |
| `source-readonly/` | FTP downloads (no secrets) |
| `http/` | Public HTML captures |
| `verification/intake-summary.json` | Run summary |

---

## 16. Authority updates

Repository docs updated: `OPERATIONAL-INDEX.md`, `OCPILOT-STATE.md`, `production-profile.md`, `site-passport.md`, `SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`, `tools/README.md`.

Audit baseline: `baselines/SITE-002-UX-TASK-INTAKE-01.md`

Tool: [site-002-prod-ux-task-intake-01.py](../tools/site-002-prod-ux-task-intake-01.py)

---

## 17. Git status

See commit wave — only scoped OCPilot docs/tool paths staged.

---

## 18. SAFE UNKNOWN / blockers

| Item | Notes |
|------|-------|
| Exact Twig partial for `spec-table` loop | Live markup in `product-content__specifications`; `producttabs.twig` not downloaded — fetch in implementation op |
| Whether category images already exist in admin for IDs 88/360 | No tile images on live home/hub — masters likely missing or not wired |
| Full-catalog attribute prevalence | Sample 66% — extrapolation reasonable; dynamic filter required |
| Modification cache for product PDP | Overlays absent on FTP — live files only |

**No blockers** for preparing implementation charters.

---

## 19. Final verdict

**SITE-002 UX TASK INTAKE COMPLETE — IMPLEMENTATION CHARTERS READY**

---

## 20. Next task recommendation

1. **Operator:** prepare/source white-background tile images for **Лари** and **Кондитерский инвентарь** (300×300 convention).
2. **Approve charter** `SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-01` when images ready.
3. **Approve charter** `SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01` — can proceed independently of images.

Checkpoint unchanged: `SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01`
