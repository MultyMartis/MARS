# REPORT — SITE-002 Category Lari Reparent Discovery

**Operation:** `SITE-002-PROD-CATEGORY-LARI-REPARENT-DISCOVERY-01`  
**OCPilot run:** 4.234  
**Date:** 2026-07-09  
**Environment:** PRODUCTION read-only — https://bzpm.ru/  
**Baseline (unchanged):** `SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01`  
**Mode:** Read-only discovery — **no Production mutation**

---

## 1. Scope

Read-only discovery before reparenting category **Лари** from a direct child of **Нейтральное оборудование** to a child of **Шкафы и лари**, aligning site structure with 1C business grouping.

| Current (wrong) URL | Target URL |
|---------------------|------------|
| `/katalog/nejtralnoe-oborudovanie/lari` | `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari` |

**In scope:** HTTP snapshots, DB SELECT, FTP source download, sitemap/SEO/entrypoint analysis, 1C ownership assessment, implementation charter.  
**Out of scope:** DB writes, admin saves, redirects, cache clear, import/monitor runs.

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

## 3. Public HTTP snapshot

**14 URLs checked** — artefacts: `deployments/.../http-snapshots/`

### Primary paths

| URL | Status | Final URL | Canonical | H1 | Breadcrumbs |
|-----|--------|-----------|-----------|-----|-------------|
| `/.../lari` (current) | **200** | unchanged | `/.../lari` | Лари | Главная / Каталог / Нейтральное оборудование |
| `/.../shkafy-i-lari` | **200** | unchanged | `/.../shkafy-i-lari` | Шкафы и лари | Главная / Каталог / Нейтральное оборудование |
| `/.../shkafy-i-lari/lari` (target) | **200** | **resolves to `/.../lari`** | `/.../lari` | Лари | same as current — **no Шкафы и лари in trail** |

**Key finding:** Target nested URL is accepted but **SEO router normalizes to old flat path** because `parent_id=79` for category 88. No 301; internal rewrite to canonical old path.

### Child paths

| URL | Status | Final URL | Breadcrumbs |
|-----|--------|-----------|-------------|
| `/.../lari/skladskie-lari` | 200 | unchanged | … / Нейтральное оборудование / **Лари** |
| `/.../lari/proizvodstvennye-lari` | 200 | unchanged | … / Нейтральное оборудование / **Лари** |
| `/.../shkafy-i-lari/lari/skladskie-lari` | 200 | **→ `/.../lari/skladskie-lari`** | old trail |
| `/.../shkafy-i-lari/lari/proizvodstvennye-lari` | 200 | **→ `/.../lari/proizvodstvennye-lari`** | old trail |

### Regression

| URL | Status | БЗПМ hits |
|-----|--------|-----------|
| `/` | 200 | 0 |
| `/.../stoly` | 200 | 0 |
| `/sitemap.xml` | 200 | — |
| `/robots.txt` | 200 | — |
| `/llms.txt` | 200 | — |

All pages: `meta robots: index, follow`. No public **БЗПМ**.

---

## 4. DB category structure

**Prefix:** `oc_` · **6 SELECT queries** via SSH mysql (read-only)  
**Artefacts:** `deployments/.../db-readonly/`

### Confirmed category IDs

| category_id | Name | parent_id | Status | SEO keyword |
|-------------|------|-----------|--------|-------------|
| **79** | Нейтральное оборудование | 0 | 1 | `nejtralnoe-oborudovanie` |
| **88** | **Лари** | **79** | 1 | `lari` |
| **140** | Производственные | **88** | 1 | `proizvodstvennye-lari` |
| **141** | Складские | **88** | 1 | `skladskie-lari` |
| **358** | **Шкафы и лари** | **79** | 1 | `shkafy-i-lari` |
| **359** | Шкафы кухонные | **358** | 1 | (child of 358) |
| **86** | Стеллажи | 79 | 1 | `stellazhi` |
| **360** | Кондитерский инвентарь | 79 | 1 | `konditerskiy-inventar` |

**Correction vs task brief:** ID **86** = **Стеллажи**, not «Шкафы и лари». Шкафы и лари = **358**.

### Answers to discovery questions

1. Is `Лари` category_id **88**? — **YES**
2. Current `parent_id` for `Лари`? — **79** (Нейтральное оборудование)
3. category_id for `Шкафы и лари`? — **358**
4. Current `category_path` for 88? — **79 → 88** (Нейтральное → Лари)
5. Children under `Лари`? — **YES**: 140 Производственные, 141 Складские
6. Reparent requires `category_path` rebuild? — **YES** for 88, 140, 141 (and product URLs in sitemap)
7. SEO keywords category-scoped? — **YES** — single segment per category (`lari`, not full path)
8. Old URL from `category_path` + `seo_url`? — **YES**
9. New URL automatic after parent update? — **Expected YES** if OpenCart rebuilds path; keyword `lari` unchanged
10. Duplicate `lari` keyword conflict? — **NO** — only `category_id=88` → `lari`

### Product counts (direct)

| category_id | Active products |
|-------------|-----------------|
| 88 Лари | **4** |
| 140, 141, 358 | 0 |

---

## 5. SEO URL and category_path analysis

### Current path chains (`oc_category_path`)

| category_id | path sequence | Public path |
|-------------|---------------|-------------|
| 88 | 79 → 88 | `nejtralnoe-oborudovanie/lari` |
| 140 | 79 → 88 → 140 | `.../lari/proizvodstvennye-lari` |
| 141 | 79 → 88 → 141 | `.../lari/skladskie-lari` |
| 358 | 79 → 358 | `nejtralnoe-oborudovanie/shkafy-i-lari` |
| 359 | 79 → 358 → 359 | `.../shkafy-i-lari/shkafy-kuhonnye` |

### Target path chains (after reparent)

| category_id | Expected path sequence | Expected public path |
|-------------|------------------------|----------------------|
| 88 | 79 → 358 → 88 | `nejtralnoe-oborudovanie/shkafy-i-lari/lari` |
| 140 | 79 → 358 → 88 → 140 | `.../shkafy-i-lari/lari/proizvodstvennye-lari` |
| 141 | 79 → 358 → 88 → 141 | `.../shkafy-i-lari/lari/skladskie-lari` |

**SEO keyword records** (`oc_seo_url`) need **no keyword change** — only `category_path` hierarchy drives full URL assembly.

---

## 6. Source/FTP discovery

**9 files downloaded** (read-only) — `deployments/.../ftp-source/`

| File | Role | Needs change? |
|------|------|---------------|
| `category_visibility.php` | Whitelist `322,331,301,326,354,358,207,80,86,88,360` | **Maybe** — ID 88 as top-level branch tile; href should follow new path if dynamic |
| `home.php` | Homepage cards via CategoryVisibility | No static IDs |
| `category.php` | Hub/PLP controller + A→Я sort | No static lari IDs |
| `google_sitemap.php` | Dynamic sitemap | **No** — auto from DB |
| `seo_url.php` | URL routing | **No** |
| `import_1C.php` / `import_1C_process.php` | 1C import | **Review** — may update parent relations |
| `.htaccess` | Rewrites | **Redirect phase** — 301 rules needed |

---

## 7. Homepage/catalog/megamenu entrypoint analysis

### Homepage + `/katalog` + neutral hub

- **11 `zpm-cat-card` tiles** — whitelist-driven, sorted A→Я (Run 4.221)
- **Лари** present as **top-level** card → `/katalog/nejtralnoe-oborudovanie/lari`
- **Шкафы и лари** present as **separate top-level** card → `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari`
- Order: Зонты → … → Лари → … → Шкафы и лари

### `/katalog/nejtralnoe-oborudovanie`

- Both **Лари** and **Шкафы и лари** shown as **direct children** (same 11-card whitelist block)

### `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari`

- Page shows **hub whitelist cards** (11 neutral branches), not only children of 358
- **Лари** appears in card grid (wrong for target hierarchy)
- DB child of 358: **359 Шкафы кухонные** only

### After reparent — expected UI changes

| Surface | Expected change |
|---------|-----------------|
| Neutral hub cards | **Лари** tile href → new nested path; may remain in whitelist as marketing entry |
| Шкафы и лари PLP | **Лари** should appear as **child card** under 358 |
| Breadcrumbs on Лари PLP | Add **Шкафы и лари** segment |
| Megamenu | Category tree-driven sections should reflect new parent |

**Classification:** DB parent/path change **+ 301 redirects** required; whitelist ID 88 **may remain** if hrefs are dynamic; operator decision whether Лари stays as top-level marketing tile on homepage.

---

## 8. Sitemap/canonical/redirect analysis

**Sitemap:** 1408 URLs · dynamic `extension/feed/google_sitemap`

| Pattern | Present |
|---------|---------|
| Old `/.../lari` (category + products) | **YES** (7+ URLs) |
| Target `/.../shkafy-i-lari/lari` | **NO** |
| Old child `/lari/skladskie-lari`, `/lari/proizvodstvennye-lari` | **YES** |
| Target nested child paths | **NO** |

**Redirect behaviour today:** None. Nested target URLs silently resolve to old canonical paths.

### Redirect recommendations (not implemented)

| From | To | Type |
|------|-----|------|
| `/katalog/nejtralnoe-oborudovanie/lari` | `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari` | **301** |
| `/katalog/nejtralnoe-oborudovanie/lari/skladskie-lari` | `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/skladskie-lari` | **301** |
| `/katalog/nejtralnoe-oborudovanie/lari/proizvodstvennye-lari` | `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/proizvodstvennye-lari` | **301** |
| Product URLs under old `/lari/` prefix | Matching new nested prefix | **301** (pattern) |

**Strongly recommended** — old URLs are indexed and in sitemap.

---

## 9. 1C/import ownership assessment

**Classification:** **MIXED**

| Authority | Scope |
|-----------|-------|
| **1C import** | New categories/products, `product_to_category`, product SEO; uses `xml_id` map for categories |
| **OpenCart admin / MARS onboarding** | Manual SEO, demo branch structure, `category_visibility` whitelist |
| **Лари (88)** | Early catalog seed (2026-03-23) + Run 4.210/4.211 admin SEO; likely predates or parallels 1C group «Шкафы и лари» (358, 2026-07-05) |

**Risk:** `import_1C_process.php` references `parent_id` and `category_path` logic via `xml_ids['categories']`. If 1C XML defines Лари under Шкафы и лари, **next import may correct parent** — or **revert manual reparent** if XML still has flat hierarchy.

**SAFE UNKNOWN:** Exact 1C XML group parent for Лари GUID — not verified in this discovery (no import XML download). **Recommend:** inspect `import0_1.xml` group hierarchy before implementation.

**Recommended path:** **Hybrid (Option D)** — verify 1C XML → admin/DB reparent → 301 redirects → post-import monitor.

---

## 10. Target final state

| Field | Value |
|-------|-------|
| Лари category_id | **88** (unchanged) |
| Шкафы и лари category_id | **358** |
| Лари parent_id | **358** (was 79) |
| Лари children | **140**, **141** (unchanged parent 88) |
| Old URL | `/katalog/nejtralnoe-oborudovanie/lari` |
| New URL | `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari` |
| Breadcrumbs | Каталог / Нейтральное оборудование / **Шкафы и лари** / Лари |
| Canonical | `https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari` |
| Sitemap | Old paths drop; new nested paths appear (automatic) |
| Homepage whitelist | ID **88** may remain; tile href must point to new path |

---

## 11. Implementation strategy options

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A — DB migration** | UPDATE `parent_id`; rebuild `category_path`; verify SEO; redirects | Precise, scriptable | Path rebuild must be correct; bypasses admin validation |
| **B — OpenCart admin** | Change parent in admin UI | Native path rebuild | Manual; still needs redirects |
| **C — 1C-side** | Fix export hierarchy | Aligns source of truth | Depends on 1C team; timing |
| **D — Hybrid** (recommended) | 1C XML verify + admin/DB reparent + 301 + monitor | Lowest revert risk | More steps |

---

## 12. Recommended implementation charter

**Charter:** `deployments/.../implementation-charter/SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-CHARTER.{md,json}`

**Recommended:** Option **D (hybrid)**

1. Download/inspect current `import0_1.xml` — confirm Лари group parent in 1C.
2. Backup `oc_category`, `oc_category_path`, `oc_seo_url` rows for ids 88, 140, 141, 358, 359, 79.
3. Reparent via **OpenCart admin** (preferred) or controlled DB script: `88.parent_id = 358`.
4. Verify `category_path` rebuilt for 88, 140, 141.
5. Confirm `oc_seo_url` keywords unchanged; new public paths resolve 200.
6. Add **301 redirects** in `.htaccess` for old `/lari` tree (category + product pattern).
7. Verify homepage/hub card hrefs, breadcrumbs, canonical, sitemap.
8. Run **post-1C monitor** after next scheduled import (2026-07-10+).

---

## 13. Risks and no-go conditions

### Risks

- 1C import reverting `parent_id` on next daily run
- `category_path` cascade error for descendants 140/141
- ~4 product PDP URLs + category PLPs in sitemap under old path
- External links / search index on old flat `/lari` URL
- Homepage whitelist showing both Лари and Шкафы и лари as siblings after reparent
- OpenCart SEO cache stale paths

### No-go conditions

- 1C XML confirms flat parent and will overwrite reparent **without guard**
- `category_id` 88 mismatch (not the case — confirmed)
- Unresolved duplicate `lari` SEO keyword (not the case)
- Cannot safely rebuild `category_path`

---

## 14. Production mutation summary

| Action | Count |
|--------|------:|
| Remote uploads | 0 |
| Remote overwrites | 0 |
| Remote deletes | 0 |
| FTP writes | 0 |
| FTP reads/listings | 9 downloads |
| Admin saves | 0 |
| DB SELECTs | 6 |
| DB direct writes | 0 |
| Redirect changes | 0 |
| Category data changes | 0 |
| Cron/import runs | 0 |
| Monitor runs triggered | 0 |
| Cache clears | 0 |
| Local cleanup/delete/move | 0 |
| public БЗПМ introduced | no |

---

## 15. Storage artefacts

```
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\
  SITE-002-PROD-CATEGORY-LARI-REPARENT-DISCOVERY-01\
    http-snapshots\
    db-readonly\
    ftp-source\
    sitemap\
    entrypoints\
    seo-url\
    one-c\
    implementation-charter\
    manifests\operation.json
    logs\
```

---

## 16. Authority updates

- `OCPILOT-STATE.md` — Run 4.234 recorded
- `OPERATIONAL-INDEX.md` — Run 4.234 entry
- `production-profile.md` — discovery note
- `site-passport.md` — reparent discovery pending implementation
- `SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` — category hierarchy finding
- `tools/README.md` — discovery tool registered

**Checkpoint unchanged:** `SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01`

---

## 17. Git status

Selective commit of discovery report + authority docs + tool only. Storage artefacts not committed.

---

## 18. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Exact 1C XML parent for Лари GUID | **SAFE UNKNOWN** — inspect `import0_1.xml` before implementation |
| Whether 1C import will preserve manual reparent | **SAFE UNKNOWN** — monitor after next import |
| Operator decision: keep Лари as homepage top-level tile vs hub-only under 358 | **Operator decision required** |

---

## 19. Final verdict

**SITE-002 CATEGORY LARI REPARENT DISCOVERY COMPLETE — IMPLEMENTATION CHARTER READY**

---

## 20. Next task recommendation

**`SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01`** (Run 4.235 proposed):

1. Charter from `implementation-charter/SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-CHARTER.md`
2. Pre-step: read-only 1C XML group hierarchy for Лари
3. Execute reparent + redirects + verification per charter
4. Post-1C monitor gate on next import day
