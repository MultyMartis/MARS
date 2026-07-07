# REPORT — SITE-002 New Sections Entrypoints

**Operation:** `SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-01`  
**OCPilot run:** 4.219  
**Date:** 2026-07-07  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Baseline before:** `SITE-002-STABLE-PROD-PDP-EXTRA-INFO-LAYOUT-01`  
**Intake before:** `SITE-002-UX-TASK-INTAKE-01`  
**Mode:** controlled Production patch — **blocked on image assets**; brief code-only deploy **rolled back safely**

---

## 1. Scope

Add homepage and neutral-hub entry tiles (`zpm-cat-card`) for:

| Section | category_id | slug |
|---------|-------------|------|
| Лари | **88** | `lari` |
| Кондитерский инвентарь | **360** | `konditerskiy-inventar` |

**In scope:** category visibility whitelist extension, approved category tile images, live verification.  
**Out of scope:** PDP (Run 4.218), header/footer/Yandex, sitemap/robots/llms, DB direct writes, category structure/meta changes, image generation.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` — **PASS** |
| Volume | `X:` — label **AI WS** — **PASS** |
| Branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD | `5ad621a9e5db13f0200fd751f8c38c7971d7578b` |
| Staged files before task | **empty** — **PASS** |
| Foreign WIP | FP-0002 / `.recovery-temp` — **not staged, not touched** |

---

## 3. Source authority confirmation

**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-01\`

| Block | Authority | Generation |
|-------|-----------|------------|
| Homepage category grid | `home.php` → `CategoryVisibility::buildHomepageCategoryCards()` → `catalogsections.twig` | Data-driven whitelist |
| Neutral hub branch tiles | `category.php` + same visibility library | Data-driven whitelist |
| Branch whitelist | `/public_html/system/library/zpm/category_visibility.php` → `$neutral_hub_branch_ids` | **HARDCODED** PHP array |
| Card images | `oc_category.image` → `model_tool_image->resize(300,300)`; empty → `placeholder.png` | OpenCart category image field |
| Modification overlays | **Not present** for inspected home/category/visibility paths | Live files authoritative |

**Live `$neutral_hub_branch_ids` (confirmed):** `322, 331, 301, 326, 354, 358, 207, 80, 86` (9 IDs — matches Run 4.217 intake).

**Planned patch (local only):** append `88, 360` → 11 branch IDs.

**Template/CSS changes:** **not required** — `zpm-cat-sections__grid` uses `repeat(5, 1fr)`; 11 cards acceptable (5+5+1).

---

## 4. Live before snapshot

| Page | HTTP | H1 | `zpm-cat-card` | Lari tile | Konditerskiy tile |
|------|------|-----|----------------|-----------|-------------------|
| Homepage | 200 | Оборудование для общепита… | **9** | **No** | **No** |
| Neutral hub | 200 | Нейтральное оборудование | **9** | **No** | **No** |
| `/lari` | 200 | Лари | 0 | N/A | N/A |
| `/konditerskiy-inventar` | 200 | Кондитерский инвентарь | 0 | N/A | N/A |

- Лари and Кондитерский инвентарь present in **megamenu** only.
- Homepage `БЗПМ` count: **0**
- Yandex Metrika/Webmaster: **present** (not touched)

**Artefacts:** `http-before/home-before.html`, `neutral-hub-before.html`, `before-card-inventory.{csv,json}`, `before-summary.md`

---

## 5. Category image audit

| category_id | Section | Master on FTP | Cache on FTP | Public HTTP 200 | Exact local approved asset | Suitable for tile |
|-------------|---------|---------------|--------------|-----------------|---------------------------|-------------------|
| 88 | Лари | **No** | **No** | **0** | **No** (`shkafy-i-lari` rejected — different category 358) | **No** |
| 360 | Кондитерский инвентарь | **No** | **No** | **0** | **No** | **No** |

**Probe results (all 404):**

- `image/catalog/Category-image/lari.webp`
- `image/catalog/Category-image/konditerskiy-inventar.webp`
- `image/cache/catalog/Category-image/lari-300x300.webp`
- `image/cache/catalog/Category-image/konditerskiy-inventar-300x300.webp`

**Note:** Run 4.217 intake `category_image_exists: true` for Лари was a **false positive** — substring match on existing tile `shkafy-i-lari`.

**Artefacts:** `image-audit/category-image-audit.{csv,json,md}`

---

## 6. Image asset decision

**Decision:** **C** — assets missing; Production implementation must not proceed with placeholder tiles.

| Option | Status |
|--------|--------|
| A — both categories have live suitable images | **No** |
| B — exact approved local assets for all targets | **No** |
| C — blocked until operator supplies images | **Yes** |

**Required image assets (operator / external workflow — not generated in this run):**

| category_id | slug | Master path | Cache tile |
|-------------|------|-------------|------------|
| 88 | `lari` | `/public_html/image/catalog/Category-image/lari.webp` | `.../lari-300x300.webp` |
| 360 | `konditerskiy-inventar` | `/public_html/image/catalog/Category-image/konditerskiy-inventar.webp` | `.../konditerskiy-inventar-300x300.webp` |

**Style reference:** white-background studio tiles — `podtovarniki-i-podstavki`, `stoly`, `telezhki-servirovochnye` (Runs 4.195–4.197).  
**Target master dimensions:** 1800×1200 WebP → OpenCart 300×300 cache.

**Artefacts:** `image-audit/image-decision.{json,md}`

---

## 7. Implementation design

1. Extend `$neutral_hub_branch_ids` with `88, 360` (append).
2. Upload exact slug-matched WebP masters + cache derivatives (or admin category image field + master upload per Run 4.195).
3. No Twig hardcoding.
4. No CSS change expected for 11-card grid.
5. Preserve Run 4.218 PDP extra-info layout.

**Artefacts:** `manifests/implementation-design.{json,md}`

---

## 8. Patch plan and rollback

| Remote file | SHA before (rollback) | Patched (local) | Rollback |
|-------------|----------------------|-----------------|----------|
| `/public_html/system/library/zpm/category_visibility.php` | captured in `source-before/` + `rollback/` | append `88, 360` to array | re-upload `rollback/` exact file |

**Artefacts:** `rollback/remote-before-manifest.json`, `rollback/rollback-plan.md`, `patch/diff-category-visibility.diff`

---

## 9. Local patch summary

- Local patched copy prepared in `source-after/` (not left on Production after rollback).
- PHP syntax: **SAFE UNKNOWN** — `php` CLI not available in agent environment; static inspection clean.
- No `БЗПМ` introduced in patch.
- Header/footer paths: **not touched**.

---

## 10. Dry-run gates

| Gate | Result |
|------|--------|
| G1 Source authority confirmed | **PASS** |
| G2 Images safe or acceptable | **FAIL** |
| G3 Rollback captured | **PASS** |
| G4 Patch touches only scoped files | **PASS** |
| G5 No DB direct writes | **PASS** |
| G6 No category structure changes | **PASS** |
| G7 No PDP changes | **PASS** |
| G8 No header/footer/Yandex touch | **PASS** |
| G9 No sitemap/robots/llms touch | **PASS** |
| G10 Visual layout risk acceptable | **PASS** |

**Proceed to deploy:** **False** (G2 fail)

**Artefacts:** `manifests/dry-run.{json,md}`

---

## 11. Controlled deploy or blocked decision

**Primary decision:** **BLOCKED** — image assets required before tile rollout.

**Incident (corrected):** An initial agent run incorrectly passed G2 (false-positive local asset match on `shkafy-i-lari` for slug `lari`) and uploaded **only** `category_visibility.php`. Live verification showed **11 cards** with **placeholder** images for Лари and Кондитерский инвентарь (`placeholder-300x300.png`). **Immediate rollback** restored the 9-card whitelist. Post-rollback homepage: **9 cards**, target tiles absent.

**Final Production state:** matches pre-operation baseline (`SITE-002-STABLE-PROD-PDP-EXTRA-INFO-LAYOUT-01`).

---

## 12. Live verification after

| Page | HTTP | Cards | Lari tile | Konditerskiy tile |
|------|------|-------|-----------|-------------------|
| Homepage (post-rollback) | 200 | **9** | **No** | **No** |
| Neutral hub (post-rollback) | 200 | **9** | **No** | **No** |

**Artefacts:** `http-after/`, `verification/rollback-evidence.json`

---

## 13. Visual/card verification

- Pre-rollback mistake confirmed: new tiles used `placeholder-300x300.png` — **unacceptable** per charter.
- Post-rollback: existing 9 tiles unchanged with correct Category-image WebP caches.
- No broken layout on restored 9-card grid.

---

## 14. Sanity checks

| URL | HTTP | Notes |
|-----|------|-------|
| `/katalog/nejtralnoe-oborudovanie/stoly` | 200 | Load More present |
| Example PDP (держатель ПГ-10/3) | 200 | `product-content__extra-info` after toggle — Run 4.218 preserved |
| `/llms.txt` | 200 | UTF-8 BOM; 0 `БЗПМ` |
| `/robots.txt` | 200 | unchanged |
| `/sitemap.xml` | 200 | URL count recorded in sanity JSON |

**Artefacts:** `verification/sanity-checks.{json,md}`

---

## 15. Brand regression check

| Check | Result |
|-------|--------|
| Public `БЗПМ` introduced | **No** |
| Target category pages meta | **ЗПМ** preserved |

---

## 16. PDP extra-info preservation

Run **4.218** layout **preserved** — example PDP shows separate `product-content__extra-info` block; attribute not in `spec-table__row`.

---

## 17. Rollback status

| Item | Status |
|------|--------|
| Rollback required | **Yes** — brief code-only deploy without images |
| `category_visibility.php` restored | **Yes** — 9 branch IDs |
| Homepage card count restored | **9** |
| Admin category image changes | **None** |
| Image FTP changes | **None** |

---

## 18. Production mutation summary

| Metric | Count |
|--------|------:|
| Remote uploads (net) | **0** (1 temporary upload rolled back) |
| Remote overwrites (net) | **0** |
| Remote deletes | **0** |
| Admin saves | **0** |
| DB direct operations | **0** |
| Product data changes | **0** |
| PDP template changes | **0** |
| CSS changes | **0** |
| Category visibility changes (net) | **0** |
| Images generated | **0** |
| Images uploaded | **0** |
| Homepage changes (net) | **no** |
| Catalog hub changes (net) | **no** |
| llms.txt changes | **0** |
| Header/footer changes | **0** |
| Yandex changes | **0** |
| Robots changes | **0** |
| Sitemap changes | **0** |
| Cache clears | **0** |
| public `БЗПМ` introduced | **no** |

---

## 19. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-01\`

Subfolders: `source-before/`, `source-after/`, `image-audit/`, `http-before/`, `http-after/`, `patch/`, `rollback/`, `verification/`, `manifests/`, `logs/`, `reports/`

---

## 20. Authority updates

- Entrypoint rule documented: new neutral branches need **both** `$neutral_hub_branch_ids` entry **and** exact-slug Category-image assets before deploy.
- False-positive guard: slug `lari` ≠ `shkafy-i-lari` (category 358).
- Tool gate fix: exact filename match required for approved local assets.

---

## 21. Git status

Repository docs/report/tool updated by this operation. Storage artefacts **not** committed (per charter).

---

## 22. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| `oc_category.image` field values for IDs 88/360 | **SAFE UNKNOWN** — admin read-only scrape not performed; public 404 confirms no usable tile image |
| `php -l` on patched file | **SAFE UNKNOWN** — PHP CLI unavailable |

**Blocker:** operator must supply **two** exact-slug Category-image WebP masters (+ cache) before re-attempt.

---

## 23. Final verdict

**SITE-002 NEW SECTIONS ENTRYPOINTS PARTIAL — IMAGE ASSETS REQUIRED**

Production tile rollout **not completed**. Brief code-only deploy was **rolled back safely**. Checkpoint **unchanged:** `SITE-002-STABLE-PROD-PDP-EXTRA-INFO-LAYOUT-01`.

---

## 24. Next task recommendation

1. Operator prepares/uploads `lari.webp` and `konditerskiy-inventar.webp` (1800×1200 white-bg studio style) to approved operation folder or direct FTP path.
2. Re-run `SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-01` (or follow-up) with image gate PASS: upload masters + cache, optional admin image field bind, then deploy `category_visibility.php` whitelist append.
3. Verify 11 cards on homepage and neutral hub with HTTP 200 tile images (no placeholder).

**Tool:** [site-002-prod-new-sections-entrypoints-01.py](../tools/site-002-prod-new-sections-entrypoints-01.py)
