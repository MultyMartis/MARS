# REPORT — PRODUCT HERO COMMERCE CARD

**Site:** site-002 (zpm.new-site.space)  
**SKU QA:** SPKB-18/7-ВЛ5  
**Date:** 2026-06-09  
**Commit:** NO | **Push:** NO

---

## 1. Backup paths

| File | Path |
|------|------|
| producthero.twig (live pre-change) | `projects/ocpilot/sites/site-002/backups/producthero.twig.pre-commerce-card.bak` |
| style.css (live pre-change) | `projects/ocpilot/sites/site-002/backups/style.css.pre-commerce-card.bak` |

SHA256 before deploy:
- twig: `e4c05f4937a3eda76b93b672384d65314d887367db0108750c2202f97186827e`
- css: `029e0d3500269542f6230954c54addf7bdb4974666e3f5c9d38d0864fbb622aa`

---

## 2. Changed files

| Remote path | Local work copy |
|-------------|-----------------|
| `catalog/view/theme/default/template/product/producthero.twig` | `projects/ocpilot/sites/site-002/commerce-card-work/producthero.twig` |
| `assets/css/style.css` | `projects/ocpilot/sites/site-002/commerce-card-work/style.css` |

Deploy script: `projects/ocpilot/sites/site-002/commerce-card-work/commerce-card-deploy.py`

---

## 3. Existing hooks / forms found

### Быстрый заказ

**Dedicated hook:** **SAFE UNKNOWN** — на live и в шаблонах site-002 нет текста «Быстрый заказ» и отдельного modal id для quick order.

Найденные Fancybox-формы на PDP (footer, live HTML):
- `#zpmFbCallback` — «Заказать звонок», `dialog=2`, `data-fb-form="callback"`
- `#zpmFbQuestion` — «Задать вопрос», `dialog=1`
- `#zpmFbGetpriceProduct` — «Узнать цену», `dialog=3`

**Реализация кнопки «Быстрый заказ»:** подключена к существующему `#zpmFbCallback` (тот же паттерн, что в каталоге / mobile menu):

```html
<button type="button" class="btn btn_dark btn--primary"
  data-fancybox data-src="#zpmFbCallback" data-zpm-fb-mode="2">
  <span>Быстрый заказ</span>
</button>
```

Модалка при открытии показывает заголовок сайта «Заказать звонок» (не переименовывали — footer/modal не трогали).

### Задать вопрос

Найден рабочий hook в `producttabs.twig` (блок `product-help`):

```html
<button type="button" class="btn btn_dark"
  data-fancybox data-src="#zpmFbQuestion" data-zpm-fb-mode="2">
  Задать вопрос
</button>
```

Тот же паттерн использован в service-card.

---

## 4. Изменения в producthero.twig

Правая колонка `product-hero__col--commerce` перестроена в **2 карточки** внутри `product-hero__commerce`:

**Блок 1 — `product-hero__commerce-card`**
- Шапка `product-hero__commerce-head`: «Стоимость:»
- Тело `product-hero__commerce-body`:
  - цена (`price`, `priceold`, `priceproc`) — логика без изменений
  - наличие / сроки (`statusText`, `deliveryText`, `cancart`)
  - корзина (`data-cart-add`, `data-cart-qty`, plus/minus, `showrequest` / `#zpmFbGetpriceProduct`)

**Блок 2 — `product-hero__service-card`**
- Заголовок: «Сервис. Гарантии. Доставка.»
- 3 пункта с FA Pro: `fal fa-shield-check`, `fal fa-truck`, `fal fa-headset`
- Кнопки: «Быстрый заказ» (`#zpmFbCallback`), «Задать вопрос» (`#zpmFbQuestion`)

**Не тронуто:** media, identity, specs, SUPER_ATTS, gallery, wishlist/compare (`product-hero__other`), script `ask_tovar_*`.

---

## 5. Добавлено в style.css

Новый блок в конце файла (только разрешённые классы):

- `.product-hero__col--commerce .product-hero__commerce` — gap между карточками
- `.product-hero__commerce-card` — фон, скругление
- `.product-hero__commerce-head` — `var(--main-dark-color)`, белый текст
- `.product-hero__commerce-body` — padding, вертикальный stack
- `.product-hero__service-card` — вторая карточка
- `.product-hero__service-list` / `.product-hero__service-item` — список с иконками
- `.product-hero__service-actions` — колонка кнопок full-width

Без изменения глобальных шрифтов, letter-spacing, word-break, глобальных `.btn`.

---

## 6. Что НЕ трогали

- controller, config, DB, JS
- `producttabs.twig`, `relproducts.twig`, `header.twig`
- FA подключение, SUPER_ATTS
- левая / центральная колонки hero
- логика цены, корзины, qty, wishlist/compare
- gallery / Fancybox product group
- footer modals (только ссылки на существующие `#zpmFb*`)

---

## 7. QA results (SPKB-18/7-ВЛ5)

| # | Check | Result |
|---|-------|--------|
| 1 | 2 карточки в правой колонке | PASS |
| 2 | Шапка «Стоимость:» тёмная | PASS |
| 3 | Цена корректна | PASS (51 281 ₽) |
| 4 | Скидка: старая цена + % | PASS (60 330 ₽, -15%) |
| 5 | Наличие / сроки | PASS (Под заказ, 5–10 дней) |
| 6 | «В корзину» | PASS (markup + hooks) |
| 7 | Qty +/- | PASS (hooks intact) |
| 8 | Wishlist / compare | PASS |
| 9 | Gallery / Fancybox | PASS |
| 10 | Быстрый заказ → форма | PASS (`#zpmFbCallback`; dedicated hook SAFE UNKNOWN) |
| 11 | Задать вопрос → форма | PASS (`#zpmFbQuestion`) |
| 12 | JS errors | PASS (none captured) |
| 13 | PHP/Twig errors | PASS |
| 14 | Mobile layout | PASS (hero stacks); note: horizontal overflow flag on 390px (pre-existing site behaviour, not commerce-card specific) |

Verify JSON: `projects/ocpilot/sites/site-002/commerce-card-work/qa-verify.json`

---

## 8. Screenshot paths

| Viewport | Path |
|----------|------|
| Desktop 1440 | `projects/ocpilot/sites/site-002/qa/commerce-card/spkb-18-7-vl5-commerce-desktop-1440.png` |
| Mobile 390 | `projects/ocpilot/sites/site-002/qa/commerce-card/spkb-18-7-vl5-commerce-mobile-390.png` |

---

## 9. Rollback procedure

1. Восстановить live-файлы из backup через FTP:
   - `backups/producthero.twig.pre-commerce-card.bak` → `catalog/view/theme/default/template/product/producthero.twig`
   - `backups/style.css.pre-commerce-card.bak` → `assets/css/style.css`
2. Очистить кэш OpenCart: `system/storage/cache` и `system/storage/cache/template`
3. Проверить PDP SPKB-18/7-ВЛ5 — правая колонка возвращается к плоскому блоку без service-card

Готовый скрипт отката можно собрать по образцу `commerce-card-deploy.py` (upload backup bytes + `clear_cache()`).

---

## UNKNOWN / notes

- **Быстрый заказ:** отдельного hook/modal с таким названием на сайте нет; использован ближайший site-wide callback `#zpmFbCallback`. Если нужна отдельная форма quick order — потребуется новый modal в footer (вне scope этой задачи).
