# REPORT — PDP CONTENT LAYOUT FIX

**Site:** SITE-002 (ЗПМ TEST)  
**Environment:** https://zpm.new-site.space/  
**Deployed at (UTC):** 2026-06-09T17:51:06  
**Commit:** NO | **Push:** NO

---

## 1. Backup paths

| File | Local backup |
|------|----------------|
| `catalog/view/theme/default/template/product/producttabs.twig` | `projects/ocpilot/sites/site-002/backups/producttabs.twig.pre-content-layout-fix.bak` |
| `assets/css/style.css` | `projects/ocpilot/sites/site-002/backups/style.css.pre-content-layout-fix.bak` |

Pre-deploy SHA256 (live capture):

| File | SHA256 |
|------|--------|
| `producttabs.twig` | `59b356333a15a971feeb494614de2e1b00e804d7092361cbba04d7d92afa9fe1` |
| `style.css` | `a9ab026205e91edfcf810eceb130e56e90c7310ac208f53275f61189231b74ae` |

Deploy manifest: `projects/ocpilot/sites/site-002/backups/content-layout-fix-deploy-manifest-20260609-175106.json`

---

## 2. Changed files

**Live (FTP):**

- `catalog/view/theme/default/template/product/producttabs.twig`
- `assets/css/style.css`

**Local work artifacts:**

- `projects/ocpilot/sites/site-002/content-layout-fix-work/producttabs.twig`
- `projects/ocpilot/sites/site-002/content-layout-fix-work/style.css`
- `projects/ocpilot/sites/site-002/content-layout-fix-work/content-layout-fix-deploy.py`
- `projects/ocpilot/sites/site-002/content-layout-fix-work/content-layout-fix-qa.py`
- `projects/ocpilot/sites/site-002/content-layout-fix-work/content-layout-fix-screenshot.py`
- `projects/ocpilot/sites/site-002/content-layout-fix-work/content-layout-fix-qa-result.json`

**Not touched (per scope):** `producthero.twig`, `product.php`, `config.php`, `header.twig`, `product.twig`, `relproducts.twig`, JS, DB, OCMOD.

---

## 3. Final Twig structure

```
product-content
└── container
    └── product-content__grid [--with-side if documents]
        ├── product-content__main
        │   ├── product-content__description     (if description)
        │   └── product-content__specifications    (always)
        ├── product-content__side                  (if documents)
        │   └── product-content__documents
        └── product-help                           (unchanged)
```

Removed: `product-content__top` (broken 70/30 + full-width specs below).

---

## 4. CSS selectors changed

Replaced block `SITE-002 — PDP product-content visual structure` with `SITE-002 — PDP product-content layout`:

| Selector | Purpose |
|----------|---------|
| `.product-content` | White section background (`#fff`), top padding |
| `.product-content__grid` | Base grid / gap |
| `.product-content__grid--with-side` | Desktop 7fr / 3fr columns |
| `.product-content__main` | Left column stack (description + specs) |
| `.product-content__side` | Right sidebar column |
| `.product-content .product-help` | Light bg only here (`var(--main-light-color)`), full-width row |
| `.product-content__card` | White card with border |
| `.product-content__specifications .spec-table` | Transparent inner table (no double fill) |
| `.product-content__documents .tabs__panel > ul.docs-list …` | Sidebar doc cards (horizontal row, type label, download icon) |

Removed: `.product-content__top` and its mobile `display: contents` hack.

Mobile (`max-width: 1024px`): single column; order — main → side → product-help.

---

## 5. Confirmation docs-list / file-type logic preserved

```html
<div class="tabs__panel is-active">
  <ul class="docs-list">
    <li class="docs-list__item">
      <a class="docs-list__link pdf" href="..." download><span>...</span></a>
    </li>
  </ul>
</div>
```

- `docs-list`, `docs-list__item`, `docs-list__link` — preserved
- Type class (`pdf`, `word`, `excel`, …) — preserved via `{{ d.type }}`
- `download` attribute — preserved
- `href` — preserved
- File icons via existing `::before` rules — preserved; overridden only layout (size, flex)
- Type label via scoped `span::after` (PDF/DOC/XLS/PNG/JPG)
- Download hint via scoped link `::after` (SVG arrow)

---

## 6. QA results

**URL:** SPKB-18/7-ВЛ5 — https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850

| # | Check | Result |
|---|-------|--------|
| 1 | White `product-content` background | PASS |
| 2 | Light bg only on `product-help` | PASS |
| 3 | Description left | PASS |
| 4 | Specs under description, same width | PASS |
| 5 | Documents right sidebar | PASS |
| 6 | Document card layout (not old tile) | PASS |
| 7 | `docs-list__link pdf` preserved | PASS |
| 8 | `href` preserved | PASS |
| 9 | `download` preserved | PASS |
| 10 | Tabs not returned | PASS |
| 11 | `product-help` visible | PASS |
| 12 | Related products visible | PASS |
| 13 | No PHP/Twig errors | PASS |
| 14 | No JS errors (page render) | PASS |
| 15 | Mobile vertical stack | PASS |

**Case C (no desc + docs):** PASS — specs in `product-content__main`, docs in sidebar.

**Cases B/D:** SAFE UNKNOWN — no live SKU in TEST catalog (557+ PDP scan).

Evidence: `projects/ocpilot/sites/site-002/content-layout-fix-work/content-layout-fix-qa-result.json`

**Overall:** PASS

---

## 7. Screenshot paths

| Viewport | Path |
|----------|------|
| SPKB 1440×900 | `projects/ocpilot/sites/site-002/qa/content-layout-fix/spkb-1440.png` |
| SPKB 390×844 | `projects/ocpilot/sites/site-002/qa/content-layout-fix/spkb-390.png` |
| VMS 1440×900 | `projects/ocpilot/sites/site-002/qa/content-layout-fix/vms-1440.png` |

---

## 8. Rollback procedure

1. Upload rollback backups to FTP (`polygonws.beget.tech`, account `polygonws_zpm`):
   - `backups/producttabs.twig.pre-content-layout-fix.bak` → `catalog/view/theme/default/template/product/producttabs.twig`
   - `backups/style.css.pre-content-layout-fix.bak` → `assets/css/style.css`
2. Clear Twig cache: delete files in `system/storage/cache/template/`.
3. Verify PDP SPKB-18/7-ВЛ5: returns to pre-fix layout (`product-content__top` + full-width specs below).
4. Or run `content-layout-fix-deploy.py` with rollback files swapped into work dir.

---

## Summary

Нижний блок PDP после hero исправлен: левая колонка 70% (описание + характеристики), правая 30% (документы-сайдбар), белый фон секции, светлый фон только у `product-help`. Документы оформлены горизонтальными карточками с иконкой типа и кнопкой скачивания. Логика `docs-list` и типов файлов сохранена.
