# REPORT — PDP DOCUMENTS FINAL PASS

**Site:** SITE-002 (ЗПМ TEST)  
**Environment:** https://zpm.new-site.space/  
**Deployed at (UTC):** 2026-06-09T19:21:32Z  
**Commit:** NO | **Push:** NO

---

## 1. Backup paths

| File | Backup path |
|------|-------------|
| `producttabs.twig` | `projects/ocpilot/sites/site-002/backups/producttabs.twig.pre-documents-final-pass.bak` |
| `style.css` | `projects/ocpilot/sites/site-002/backups/style.css.pre-documents-final-pass.bak` |

**Pre-pass SHA256:**
- producttabs.twig: `86419148b5d10e75dd361de26e8e51a717c4db1f38769c1cfe0049bf5b661d2b`
- style.css: `21761371479795f75f98985c551cf3dd0f78abd348672d22409795ab1b68ccde`

---

## 2. Changed files

**Live (FTP deploy):**
- `catalog/view/theme/default/template/product/producttabs.twig`
- `assets/css/style.css`

**Local work copies:**
- `projects/ocpilot/sites/site-002/documents-final-pass-work/producttabs.twig`
- `projects/ocpilot/sites/site-002/documents-final-pass-work/style.css`

**Deploy manifest:** `projects/ocpilot/sites/site-002/backups/documents-final-pass-deploy-manifest-20260609-192132.json`

---

## 3. Twig changes (documents block)

- Sidebar `product-content__side` выводится **всегда**; grid всегда с `product-content__grid--with-side`.
- Заголовок: `<h2>Документы</h2>`.
- Убрана обёртка `tabs__panel`.
- **Если документы есть:** `ul.docs-list` с компактными строками:
  - `docs-list__link {{ d.type }}` + `href` + `download` (без изменений логики)
  - вложенные `docs-list__file-main` / `docs-list__file-title` / `docs-list__file-type`
  - `docs-list__download` с `fal fa-download`
  - мини-CTA `product-content__docs-note` со ссылкой «свяжитесь с нами» → `#zpmFbQuestion`
- **Если документов нет:** `product-content__docs-empty` с CTA «Запросить документы» → `#zpmFbQuestion`

---

## 4. CSS additions (documents only)

Локальные селекторы под компактную строку:

- `.product-content__documents h2`
- `.product-content__documents .docs-list` / `__item` / `__link`
- `.docs-list__file-main`, `__file-title`, `__file-type`, `__download`
- `.product-content__docs-note`, `.product-content__docs-empty`
- Иконки типов файлов через `::before` на `.docs-list__link.pdf|word|excel|png|jpg`
- Удалены старые tile-стили (`tabs__panel > ul.docs-list`, padding 30px, `docs-list__link > div`)

Mobile stack (`@media max-width: 1024px`) не изменялся.

---

## 5. Logic: documents exists / absent

| Состояние | Разметка |
|-----------|----------|
| `documents` не пуст | `docs-list` + `product-content__docs-note` |
| `documents` пуст | `product-content__docs-empty` |
| Оба случая | sidebar всегда виден, форма `#zpmFbQuestion` через Fancybox |

---

## 6. docs-list / file-type preserved

- `docs-list`, `docs-list__item`, `docs-list__link` — сохранены
- Класс типа из `{{ d.type }}` (pdf/word/excel/…) — сохранён
- `href="{{ d.filename }}"` и атрибут `download` — сохранены
- Иконка типа файла — через CSS `::before` по классу ссылки

---

## 7. QA results

### SPKB-18/7-ВЛ5 (live) — **PASS**

| Check | Result |
|-------|--------|
| PHP/Twig errors | PASS |
| `docs-list` preserved | PASS |
| `docs-list__link pdf` | PASS |
| `href` + `download` | PASS |
| Compact row + download icon | PASS |
| `product-content__docs-note` + contact hook | PASS |
| `product-help` + related | PASS |
| Mobile stack CSS | PASS |

### Товар без документов — **SAFE UNKNOWN**

557+ PDP URL ранее просканированы; live SKU без документов не найден. Ветка `{% else %}` проверена статически по Twig — PASS.

**QA JSON:** `projects/ocpilot/sites/site-002/documents-final-pass-work/documents-final-pass-qa-result.json`

---

## 8. Screenshot paths

- `projects/ocpilot/sites/site-002/qa/documents-final-pass/spkb-documents-1440.png`
- `projects/ocpilot/sites/site-002/qa/documents-final-pass/spkb-documents-390.png`
- `projects/ocpilot/sites/site-002/qa/documents-final-pass/spkb-content-1440.png`
- `projects/ocpilot/sites/site-002/qa/documents-final-pass/spkb-content-390.png`

---

## 9. Rollback procedure

1. Upload `backups/producttabs.twig.pre-documents-final-pass.bak` → `catalog/view/theme/default/template/product/producttabs.twig`
2. Upload `backups/style.css.pre-documents-final-pass.bak` → `assets/css/style.css`
3. Clear `system/storage/cache/template/` on FTP
4. Verify SPKB PDP documents block matches pre-pass state

**Post-deploy SHA256 (for reference):**
- producttabs.twig: `296537f678d2fc793eae85ab8b5b3bd707d995a3ab8aa67cac36def531a1abd8`
- style.css: `9c11a023d680fb70c59dffaf035c2dd01ffc78d17411e8f5f0924564968b392b`

---

**Git status:** новые untracked файлы в `backups/`, `documents-final-pass-work/`, `qa/documents-final-pass/` — commit не выполнялся.
