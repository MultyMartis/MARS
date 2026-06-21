# REPORT — M9.8.9-10 PAGE INTRO DESCRIPTION REMOVAL

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`  
**Pass:** M9.8.9-10  
**Date:** 2026-06-21  
**PRE-TASK:** Knowledge Map · Stable Checkpoint · site-passport · README — read.

---

## 1. Root Source

### Render chain (forensic)

| Layer | File | Finding |
|-------|------|---------|
| **Output slot** | `catalog/view/theme/default/template/common/header.twig` | `{% if pageintro %}{{ pageintro }}{% endif %}` after breadcrumbs |
| **Document bridge** | `catalog/controller/common/header.php` | `$data['pageintro'] = $this->document->getPageintro()` |
| **HTML builder** | `Pageintro` class (`Pageintro::render()`) | Emits `<section class="page-intro">` with optional `<div class="page-intro__description">` when `description` non-empty |
| **Hub data source** | `catalog/controller/product/category.php` | When `$is_hub = $visibility->isNeutralHubCategory($category_id)` → hardcoded `$pageintro->description = 'Выберите тип нейтрального…'` (added M9.5 root-hub pass) |
| **Catalog root source** | `catalog/controller/product/katalog.php` | Separate hardcoded `$pageintro->description = "Для предприятий общественного питания…"` |

### Ruled out

| Candidate | Result |
|-----------|--------|
| `category.twig` | Does not render page-intro |
| SEO meta `description` | `<meta name="description">` only — unrelated |
| `$data['description']` (category body) | Separate block below grid — **not touched** |
| CMS category description field | Feeds `$data['description']`, not page-intro |
| Language files | No intro string found |
| Theme twig override per hub | No — logic in controller |

**Live pre-deploy evidence:** `.recovery-temp/m9.7a-hub-live.html` line 776; live fetch 2026-06-21 showed intro paragraph under H1 on hub.

---

## 2. Usage Map

| Page | URL | `page-intro__description` before | After M9.8.9-10 | Controller |
|------|-----|----------------------------------|-----------------|------------|
| Catalog root | `/katalog` | **Yes** — «Для предприятий…» | **Yes** (unchanged) | `katalog.php` |
| Neutral hub | `/katalog/nejtralnoe-oborudovanie` | **Yes** — hub navigation copy | **No** | `category.php` |
| Столы | `…/stoly` | No | No | `category.php` |
| Моечные ванны | `…/moechnye-vanny` | No | No | `category.php` |
| Подтоварники | `…/podtovarniki-i-podstavki` | No | No | `category.php` |
| Тележки | `…/telezhki-servirovochnye` | No (inferred — same branch logic) | No | `category.php` |
| Зонты | `…/zonty-vytyazhnye` | No (inferred) | No | `category.php` |
| PDP | product routes | No on sampled PLPs | No | not in scope |

Branch PLPs always had `$pageintro->description = ''` — `Pageintro::render()` omits the description div when empty.

---

## 3. Decision

**Variant B** — block is used on **at least one other route** (`/katalog` via `katalog.php`).

**Action:** targeted removal of hub intro text in `category.php` only. Do **not** remove global `Pageintro` render or twig markup.

---

## 4. Implementation

### Change

**File:** `catalog/controller/product/category.php`

**Before:**

```php
$pageintro = new Pageintro();
$pageintro->title = $data['heading_title'];
if ($is_hub) {
    $pageintro->description = 'Выберите тип нейтрального оборудования: …';
} else {
    $pageintro->description = '';
}
$this->document->setPageintro($pageintro->render());
```

**After:**

```php
$pageintro = new Pageintro();
$pageintro->title = $data['heading_title'];
$pageintro->description = '';
$this->document->setPageintro($pageintro->render());
```

- Not CSS / not `display:none` — render path receives empty description → no DOM node.
- H1, breadcrumbs, `$data['description']`, commercial trust, filters, pagination, grid — **unchanged**.

### Deploy

| Step | Status |
|------|--------|
| FTP capture (pre) | ✅ `reports/m9.8.9-10-work/live-capture/` |
| Backup | ✅ `backups/category.php.pre-m9.8.9-10-page-intro-description.bak` |
| Manifest + SHA256 verify | ✅ `manifest-post-20260621-125817.json` |
| Upload + post-verify | ✅ `deploy_ok: true` |
| Twig cache clear | Attempted — empty dir (no stale files) |

**SHA256:**

| Phase | Hash |
|-------|------|
| Pre | `7e5221b7df4f6e45782d7d2786b92ffe2ce0b0d8219e4e44c396650f9af424e6` |
| Post | `05bf86805989471c411a27d07fdc7bd5216a090b0592c5e4407d8aedd0040db2` |

---

## 5. QA Results

Automated HTML fetch: `reports/m9.8.9-10-work/qa-results.json`

| Page | `page-intro__description` | Pass |
|------|---------------------------|------|
| Neutral hub | **absent** | ✅ |
| `/katalog` | **present** (regression guard) | ✅ |
| Столы | absent | ✅ |
| Моечные ванны | absent | ✅ |
| Подтоварники | absent | ✅ |

**Hub snippet (post):** `<section class="page-intro">…<h1>…</h1></section>` — no description div.

**Operator visual QA:** pending — confirm spacing H1 → next block on hub at desktop/mobile.

---

## 6. Rollback

1. Restore `backups/category.php.pre-m9.8.9-10-page-intro-description.bak` → FTP `catalog/controller/product/category.php`
2. Verify SHA256 = `7e5221b7df4f6e45782d7d2786b92ffe2ce0b0d8219e4e44c396650f9af424e6`
3. Clear `system/storage/cache/template/`
4. Re-check hub shows intro paragraph

Deploy script (reverse): re-upload capture from `live-capture/catalog__controller__product__category.php`.

---

## 7. Changed Files

| Path | Action |
|------|--------|
| **Live FTP** `catalog/controller/product/category.php` | Patched (deployed) |
| `backups/category.php.pre-m9.8.9-10-page-intro-description.bak` | Created |
| `reports/m9.8.9-10-work/live-capture/catalog__controller__product__category.php` | Created |
| `reports/m9.8.9-10-work/catalog__controller__product__category.php.patched` | Created |
| `reports/m9.8.9-10-work/m9.8.9-10-deploy-run.py` | Created |
| `reports/m9.8.9-10-work/manifest-pre-20260621-125817.json` | Created |
| `reports/m9.8.9-10-work/manifest-post-20260621-125817.json` | Created |
| `reports/m9.8.9-10-work/qa-fetch.py` | Created |
| `reports/m9.8.9-10-work/qa-results.json` | Created |
| `knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | Updated — **§15 Page Intro Block** |
| `reports/SITE-002-M9.8.9-10-PAGE-INTRO-DESCRIPTION-REMOVAL.md` | This report |

**Git:** commit NO · push NO

---

## 8. Knowledge Updates

Added [Knowledge Map §15](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#15-page-intro-block-page-intro):

- Full render chain (controller → `Pageintro` → document → header.twig)
- Distinction: `$pageintro->description` vs `$data['description']` (category SEO body)
- Route map including `katalog.php` vs `category.php`
- M9.8.9-10 hub text removal registered

---

## 9. Risks

| Risk | Level | Mitigation |
|------|-------|------------|
| Catalog root intro accidentally removed | Low | `katalog.php` not in scope; QA confirmed present |
| Operator expects hub intro copy elsewhere | Low | Copy was UX-only; category SEO body unchanged |
| `$is_hub` branch looked removable entirely | N/A | `$is_hub` still drives hub layout / `hub_categories` — only pageintro branch simplified |
| `Pageintro` class source not in repo | Info | Class lives on hosting; behaviour inferred from live HTML + controller pattern |

---

*Deploy complete — awaiting operator visual QA on https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie*
