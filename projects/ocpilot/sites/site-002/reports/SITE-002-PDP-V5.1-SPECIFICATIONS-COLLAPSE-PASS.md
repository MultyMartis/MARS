# REPORT — PDP V5.1 SPECIFICATIONS COLLAPSE PASS

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Executed:** 2026-06-14  
**Mode:** Live capture → edit → FTP deploy → QA

---

## 1. Backup paths

| File | Backup | SHA256 (pre-change live) |
|------|--------|--------------------------|
| `producttabs.twig` | `projects/ocpilot/sites/site-002/backups/producttabs.twig.pre-pdp-specs-collapse-pass.bak` | `028e9a46ebedc764b9dbaafa8799c62c4194dcab183b94a94b3589ceb73c0171` |
| `style.css` | `projects/ocpilot/sites/site-002/backups/style.css.pre-pdp-specs-collapse-pass.bak` | `6583a1569aa612826571bae414e16b68151624b4bfe91ffb1150a7d3a541daca` |
| `main.js` | `projects/ocpilot/sites/site-002/backups/main.js.pre-pdp-specs-collapse-pass.bak` | `e1f545fe29e09f62837df2186652b00298fab6c30206d9ed16c3a828195b3a88` |

Capture manifest: `projects/ocpilot/sites/site-002/backups/pdp-specs-collapse-capture-20260614-122300.json`

---

## 2. Changed files (live FTP)

| Remote path | Local work copy |
|-------------|-----------------|
| `catalog/view/theme/default/template/product/producttabs.twig` | `projects/ocpilot/sites/site-002/pdp-specs-collapse-pass-work/producttabs.twig` |
| `assets/css/style.css` | `projects/ocpilot/sites/site-002/pdp-specs-collapse-pass-work/style.css` |
| `assets/js/main.js` | `projects/ocpilot/sites/site-002/pdp-specs-collapse-pass-work/main.js` |

Deploy manifest (final): `projects/ocpilot/sites/site-002/backups/pdp-specs-collapse-deploy-manifest-20260614-122532.json`

---

## 3. Twig changes

Внутри `.product-content__specifications.product-content__card` после `.spec-table` добавлена минимальная разметка кнопки:

- `.product-content__specs-toggle-wrap` (`hidden` по умолчанию)
- `button[data-product-specs-toggle]` с текстом и chevron
- `aria-expanded="false"`

Структура характеристик (`.spec-table` / `.spec-table__row`), описание, документы, product-help, related — **не изменялись**.

---

## 4. CSS changes

Scoped-блок только для PDP content:

- `.product-content__specifications.is-collapsible .spec-table` — `overflow: hidden`, `transition: max-height 0.3s ease`
- `.product-content__specs-toggle-wrap` / `.product-content__specs-toggle` — flex-кнопка с border/radius через `--border-color`, `--border-radius-form`, `--accent-color-01`
- `.product-content__specifications.is-expanded [data-product-specs-toggle-icon]` — rotate 180°
- `prefers-reduced-motion: reduce` — отключение transition

Без gradient overlay, масок, box-shadow, line-clamp, глобальных правок `.product-content__card`.

---

## 5. JS logic

Изолированный модуль `initProductSpecsCollapse()` в `main.js`:

- Scope: `.product-content__specifications` внутри `.product-content__main`
- Row selector: `.spec-table__row`
- Limits: desktop/tablet `>767px` → 8 строк; mobile `≤767px` → 5 строк
- Измерение collapsed height: `getBoundingClientRect()` первых N строк
- Inline `max-height` на `.spec-table`; state-классы на section
- Expand/collapse через `max-height` + `transitionend` → `max-height: none` в expanded
- Resize debounce 150ms; состояние expanded сохраняется; reload → collapsed
- Без localStorage

---

## 6. Desktop behavior

| Width | SPKB rows | Limit | Collapsed max-height | Toggle |
|-------|-----------|-------|----------------------|--------|
| 1920 | 22 | 8 | 275px | visible |
| 1440 | 22 | 8 | 275px | visible |
| 1366 | 22 | 8 | 275px | visible |
| 1280 | 22 | 8 | 275px | visible |
| 768 | 22 | 8 | 275px | visible |

При `rows ≤ 8` collapse отключается, кнопка скрыта.

---

## 7. Mobile behavior

| Width | SPKB rows | Limit | Collapsed max-height | Toggle |
|-------|-----------|-------|----------------------|--------|
| 576 | 22 | 5 | 160px | visible |
| 390 | 22 | 5 | 160px | visible |
| 375 | 22 | 5 | 160px | visible |
| 360 | 22 | 5 | 160px | visible |

При `rows ≤ 5` collapse отключается, кнопка скрыта.

**SAFE UNKNOWN:** отдельный PDP с ≤8 / ≤5 характеристик на live не проверен в этой сессии; логика disable при `rows <= limit` реализована в JS.

---

## 8. Scroll behavior

После клика toggle — `scrollTo({ behavior: 'smooth' })` к заголовку `.section-title__like-h3` блока характеристик.

Offset:

- sticky `[data-header-sticky].sticky` или `[data-header-mobilebar].sticky` → `height + 16px`
- иначе → `90px`

---

## 9. QA results

**Reference URLs:**

- SPKB: `/katalog/.../stol-tumba-spkb-18-7-vl5-1800h700h850` (22 rows)
- VMS: `/katalog/.../vanna-moechnaya-vms-p-2-600-1400h700h850` (21 rows)

| Check | Result |
|-------|--------|
| Collapse при rows > limit | PASS |
| 8 строк desktop / 5 mobile | PASS (max-height 275px / 160px) |
| Кнопка visible/hidden | PASS |
| Expand → «Скрыть характеристики», max-height none | PASS |
| Collapse → «Смотреть все характеристики» | PASS |
| Chevron rotate | PASS (CSS) |
| Horizontal overflow | PASS (none) |
| Description / documents | PASS |
| Related products | PASS |
| Cart `[data-cart-add]` | PASS |
| Category regression (view switcher) | PASS |
| product-help | N/A on live template (закомментирован в live `producttabs.twig`) |

QA JSON: `projects/ocpilot/sites/site-002/qa/pdp-specs-collapse-pass/pdp-specs-collapse-qa-result.json`

---

## 10. Screenshot paths

`projects/ocpilot/sites/site-002/qa/pdp-specs-collapse-pass/`

- `spkb-desktop-{1920,1440,1366,1280}.png`
- `spkb-mobile-{768,576,390,375,360}.png`
- `spkb-1440-expanded.png`, `spkb-1440-collapsed-after-toggle.png`
- `spkb-390-expanded.png`, `spkb-390-collapsed-after-toggle.png`
- `vms-desktop-1440.png`, `vms-mobile-390.png`
- `category-regression-1440.png`

---

## 11. Rollback procedure

1. Upload backups to FTP (`polygonws.beget.tech`, CWD `/` = public_html):
   - `backups/producttabs.twig.pre-pdp-specs-collapse-pass.bak` → `catalog/view/theme/default/template/product/producttabs.twig`
   - `backups/style.css.pre-pdp-specs-collapse-pass.bak` → `assets/css/style.css`
   - `backups/main.js.pre-pdp-specs-collapse-pass.bak` → `assets/js/main.js`
2. Clear `system/storage/cache/template/`
3. Verify SPKB PDP — specs block без collapse-кнопки, прежний вид

---

## 12. Git status

Repo work copies, backups, QA artefacts, deploy/capture manifests — **untracked** under `projects/ocpilot/sites/site-002/`.  
**Commit:** NO · **Push:** NO

---

## UNKNOWN / notes

- Twig template cache on deploy reported **0 files cleared** — if stale twig observed, operator should manually clear `system/storage/cache/template/`.
- Low-spec-count PDP not live-verified (disable path is code-complete only).
