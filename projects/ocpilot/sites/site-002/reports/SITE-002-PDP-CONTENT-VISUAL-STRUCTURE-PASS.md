# REPORT — PDP CONTENT VISUAL STRUCTURE PASS

**Site:** SITE-002 (ЗПМ TEST)  
**Environment:** https://zpm.new-site.space/  
**Baseline:** `SITE-002-STABLE-PDP-V2-2026-06-09`  
**Deployed at (UTC):** 2026-06-09T17:11:58  
**Commit:** NO | **Push:** NO

---

## 1. Backup paths

| File | Local backup |
|------|----------------|
| `catalog/view/theme/default/template/product/producttabs.twig` | `projects/ocpilot/sites/site-002/backups/producttabs.twig.pre-content-visual-pass.bak` |
| `assets/css/style.css` | `projects/ocpilot/sites/site-002/backups/style.css.pre-content-visual-pass.bak` |

Pre-deploy SHA256 (live capture):

| File | SHA256 |
|------|--------|
| `producttabs.twig` | `bbe306680aaef8d5bd9f0d9d15bfeb86982f8865d7bc3706505639a874c45048` |
| `style.css` | `6a985fda511934c9a4f9761a99f841c7a759c5abe33cba72a4c5453fe3a24c61` |

Deploy manifest: `projects/ocpilot/sites/site-002/backups/content-visual-pass-deploy-manifest-20260609-171158.json`

---

## 2. Changed files

**Live (FTP):**

- `catalog/view/theme/default/template/product/producttabs.twig`
- `assets/css/style.css`

**Local work artifacts:**

- `projects/ocpilot/sites/site-002/content-visual-pass-work/producttabs.twig`
- `projects/ocpilot/sites/site-002/content-visual-pass-work/style.css`
- `projects/ocpilot/sites/site-002/content-visual-pass-work/content-visual-pass-deploy.py`
- `projects/ocpilot/sites/site-002/content-visual-pass-work/content-visual-pass-qa.py`
- `projects/ocpilot/sites/site-002/content-visual-pass-work/content-visual-pass-screenshot.py`
- `projects/ocpilot/sites/site-002/content-visual-pass-work/content-visual-pass-qa-result.json`

**Not touched (per scope):** `producthero.twig`, `product.php`, `config.php`, `header.twig`, `product.twig`, `relproducts.twig`, JS, DB, OCMOD.

---

## 3. Final Twig structure

```
product-content
└── container
    └── product-content__grid
        ├── product-content__top                    (if documents)
        │   ├── product-content__description        (if description)
        │   │   OR product-content__specifications  (if no description)
        │   └── product-content__documents          (if documents)
        │
        ├── product-content__description            (if description AND no documents)
        ├── product-content__specifications         (if description OR no documents)
        │
        └── product-help                            (unchanged)
```

Headings added: «Описание», «Технические характеристики», «Документы» (`section-title__like-h3`).

---

## 4. Conditional render matrix

| Case | description | documents | Render |
|------|-------------|-----------|--------|
| **A** | yes | yes | `top`: description 70% + documents 30% → `specifications` 100% |
| **B** | yes | no | `description` 100% → `specifications` 100% |
| **C** | no | yes | `top`: specifications 70% + documents 30% (no standalone specs below) |
| **D** | no | no | `specifications` 100% only |

Twig flags:

```twig
{% set has_desc = description|striptags|trim %}
{% set has_docs = documents %}
```

- `top` → `{% if has_docs %}`
- standalone `description` → `{% if has_desc and not has_docs %}`
- standalone `specifications` → `{% if has_desc or not has_docs %}`

---

## 5. CSS selectors added

Block appended to `style.css` (SITE-002 — PDP product-content visual structure):

| Selector | Purpose |
|----------|---------|
| `.product-content` | Section top padding (`var(--pad-y)`) |
| `.product-content__grid` | Vertical rhythm / mobile flex stack |
| `.product-content__top` | Desktop 7fr / 3fr grid |
| `.product-content__card` | Card border, radius, background, padding |
| `.product-content__documents .docs-list` | Vertical doc list in narrow column |

Mobile (`max-width: 1024px`): `product-content__grid` flex column; `product-content__top` `display: contents`; order — description → specifications → documents.

Uses existing tokens: `--border-color`, `--main-light-color`, `--radius-main`, `--pad-gap`, `--pad-y`.

No new font-size / font-family / letter-spacing / word-break / text-transform.

---

## 6. Confirmation docs-list logic preserved

Documents block keeps prior markup:

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
- Type class (`pdf`) — preserved
- `download` attribute — preserved
- `href` to `Product_DOCs/` — preserved
- `tabs__panel is-active` wrapper — kept so existing `.tabs__panel > ul.docs-list` CSS hooks remain valid

---

## 7. Tested URLs

| Case | URL |
|------|-----|
| **A** desc + docs | https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850 |
| **C** no desc + docs | https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-svarnye-premium/vanna-moechnaya-vms-p-2-600-1400h700h850 |
| **B** desc + no docs | **SAFE UNKNOWN** — no live SKU in TEST catalog (557+ PDP scan) |
| **D** no desc + no docs | **SAFE UNKNOWN** — no live SKU in TEST catalog (557+ PDP scan) |

---

## 8. QA results

| Check | Case A (SPKB) | Case C (VMS) |
|-------|---------------|--------------|
| PHP/Twig errors | PASS | PASS |
| `product-content` present | PASS | PASS |
| No `tabs js-tabs` | PASS | PASS |
| No `js-tabs` | PASS | PASS |
| Specs always visible | PASS | PASS |
| Description absent when empty | n/a | PASS |
| Documents absent when empty | n/a | n/a |
| docs-list preserved | PASS | PASS |
| `pdf` class + `download` | PASS | PASS |
| `product-help` visible | PASS | PASS |
| `rel-products` visible | PASS | PASS |
| Horizontal overflow @390px (SPKB) | PASS (`scrollWidth` 388 ≤ 390) | — |

**Twig branches B/D:** verified statically in template (`has_desc and not has_docs`, `not has_desc and not has_docs`); live URLs not available — **SAFE UNKNOWN**.

**Overall:** PASS (live cases A + C).

Evidence JSON: `projects/ocpilot/sites/site-002/content-visual-pass-work/content-visual-pass-qa-result.json`

---

## 9. Screenshot paths

| Viewport | Path |
|----------|------|
| SPKB 1440×900 | `projects/ocpilot/sites/site-002/qa/content-visual-pass/spkb-1440.png` |
| SPKB 390×844 | `projects/ocpilot/sites/site-002/qa/content-visual-pass/spkb-390.png` |
| VMS 1440×900 | `projects/ocpilot/sites/site-002/qa/content-visual-pass/vms-1440.png` |

---

## 10. Rollback procedure

1. Upload rollback backups to FTP (`polygonws.beget.tech`, account `polygonws_zpm`):
   - `backups/producttabs.twig.pre-content-visual-pass.bak` → `catalog/view/theme/default/template/product/producttabs.twig`
   - `backups/style.css.pre-content-visual-pass.bak` → `assets/css/style.css`
2. Clear Twig cache: delete files in `system/storage/cache/template/`.
3. Verify PDP: SPKB hero unchanged; lower block returns to pre-pass structure (flat sections without card grid).
4. Optional full PDP V2 rollback: use `SITE-002-STABLE-PDP-V2-2026-06-09` backup folder per `reports/SITE-002-STABLE-PDP-V2-2026-06-09.md`.

---

## Summary

Нижний блок PDP после hero приведён к утверждённой схеме: карточки с заголовками, desktop-сетка 70/30 для пары description/documents или specifications/documents, full-width характеристики ниже (кроме case C). Логика `docs-list` и блок `product-help` не изменены. Hero, commerce, gallery, related products — без изменений.
