# SITE-001 W3ATMOSPHERE-01A Visual Preview v1

**Type:** Pre-execution visual preview — operator decision aid (read-only)  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Wave:** W3ATMOSPHERE-01A — Visual Preview (no implementation)  
**Inputs:** [SITE-001-W3COLOR-01-DISCOVERY-v1.md](SITE-001-W3COLOR-01-DISCOVERY-v1.md) · active layers W3-V · W3V2 · W3UX-C1

**Explicit exclusions:** No FTP · No CSS/Twig/HTML edits · No admin · No cache ops · No site modification

**Purpose:** Показать оператору, **как именно** изменится ощущение сайта при выполнении W3ATMOSPHERE-01, **до** написания CSS.

---

## Executive summary

Сейчас СИБКАР на TEST читается как **OpenCart-шаблон с листами A4 на почти белом столе**: белые карточки, резкая тёмная полоса навигации, плоский чёрный футер, красные акценты «в лоб». Предыдущие волны (W3-V, W3V2, W3UX-C1) добавили токены и частично унифицировали карточки, но **атмосферной системы нет** — фон почти сливается с карточками, тёмные зоны плоские, legacy-правила конкурируют с override-блоком.

**W3ATMOSPHERE-01** (execution wave, ещё не авторизован) переводит сайт в режим **«автосалон на мягком graphite-neutral холсте»**: страница получает глубину, белые блоки начинают «лежать» на поверхности, header/footer становятся premium shell, карточки — единым языком offer cards, формы — dealership lead UI. Layout, текст, поля, колонки, CTA-порядок и W3UX-C1 density **не трогаются**.

**Ожидаемое субъективное изменение для обычного пользователя:** **да, заметно** — особенно на главной, в каталоге и в футере. Это не «другой сайт», но переход от «шаблонный магазин» к «салон с отделкой» будет виден без сравнения скриншотов.

---

## Palette direction (execution base)

| Role | Token / value | Роль в ощущении |
|------|---------------|-----------------|
| Canvas | `#EEF1F5` | Прохладный stone-фон — «стена салона», не белая бумага |
| Card | `#FFFFFF` | Чистые offer-поверхности на фоне |
| Raised | `#FAFBFC` | Панели инструментов (фильтры) — не merchandise |
| Sunken / chips | `#E4E8ED` | Вдавленные метки, теги, внутренние полоски |
| Graphite main | `#2F343E` | Nav, footer, тёмные band — тёплый charcoal, не чёрный |
| Graphite deep | `#1A1D24` | Тонкие швы, акцентные линии — без «дешёвого реза» |
| Brand red | `#9E0202` | Сохраняется; CTA и ключевые акцents |
| Brand red hover | `#BA0000` | Hover без neon glow |
| Success green | `#1F8A4C` | Stock/tags — вместо neon `#00AA00` |
| Border | `rgba(47, 52, 62, 0.10)` | Мягкий graphite outline |
| Shadow | soft graphite only | Единая глубина; без blue-grey legacy hover |

---

## Zone previews

### 1. Global canvas

| Field | Description |
|-------|-------------|
| **Current look** | Body `#F7F8FA` — на 1–2% темнее белого; глаз не различает фон и карточку. Страница = плоский лист с белыми прямоугольниками. Секции не «утоплены» и не «приподняты» — всё на одном уровне. |
| **Target look** | Body `#EEF1F5` — прохладный blue-grey stone. Белые карточки и header bar **отрываются** от фона на arm's length. Между секциями появляется ощущение **слоя**: canvas → card → content. Опциональные section bands `#F4F6F9` на homepage — мягкие «полосы зала», не новые блоки. |
| **What changes visually** | Сразу видна **глубина страницы**: каталог перестаёт быть «белым на белом»; фильтр и карточки различимы по уровню; scroll feels like moving по оформленному интерьеру, а не по PDF. Контраст canvas↔card ~5% luminance вместо ~1–2%. |
| **What does NOT change** | Ширина container, padding секций, порядок блоков, grid catalog, W3UX-C1 card height/density на `/cars/`. |
| **Expected visual impact** | **8/10** — самое заметное sitewide изменение одной переменной |
| **Risk** | Низкий. Риск «слишком серо» на некоторых мониторах — mitigated тем, что cards остаются pure white |

---

### 2. Header

| Field | Description |
|-------|-------------|
| **Current look** | Белая верхняя полоса (logo, phone, callback) — «остров» с тонкой тенью. Ниже — **резкий срез** в flat dark nav `#21242B` с near-black border `rgb(16,18,21)`. Ощущение: два нес related слоя, discount retail. |
| **Target look** | **Premium shell:** белый top bar остаётся L2-картой, но получает чуть сильнее separation shadow + hairline inset highlight — «стеклянная кромка». Nav — **мягкий graphite gradient** `#353A45` → `#2F343E`, верхний seam `rgba(255,255,255,0.05)` вместо чёрного реза. Brand red `#9E0202` на CTA с soft red depth на hover — акцент **на тёмном фоне**, не кричащий. |
| **What changes visually** | Header перестаёт «ломаться» на две части. Верх = светлый reception desk; nav = continuous dark band с volume. Scroll duplicate bars получают тот же язык. Subtitle логотипа приглушается — меньше конкуренции с красными кнопками. |
| **What does NOT change** | DOM header, количество CTA, порядок logo/phone/callback, пункты меню, offcanvas structure, sticky behavior. |
| **Expected visual impact** | **7/10** — видно на каждой странице |
| **Risk** | Средний: gradient на nav может выглядеть «грязно» если legacy borders не purged — discovery требует full literal purge |

---

### 3. Footer

| Field | Description |
|-------|-------------|
| **Current look** | Flat dark mass `#21242B` / `--w3v2-dark-main`. Тяжёлые **10px near-black** borders сверху/снизу. Заголовки секций с chalky white dividers. Legal text тем же белым — «стена текста». |
| **Target look** | **Premium graphite atmosphere:** vertical gradient `#353A45` → `#272B33` — «потолок светлее, пол темнее». Seams → 1px `rgba(236,238,242,0.10)`. Legal → muted `#A8AEB8`; ссылки читаемее на тёмном. Декоративная **2px brand red line** под logo zone (CSS pseudo, без markup). Footer CTA — soft shadow на красном. |
| **What changes visually** | Footer перестаёт быть «тяжёлым чёрным прямоугольником». Появляется **глубина и иерархия текста**: важное светлее, legal отступает. Бренд red — тонкий accent, не крик. Сайт заканчивается «обложкой», не «обрубом». |
| **What does NOT change** | Колонки, accordion legal (если есть), все ссылки и тексты, формы в footer, высота/stack structure — **no collapse**, no removal. |
| **Expected visual impact** | **7/10** — особенно на scroll-to-bottom |
| **Risk** | Низкий при structure freeze. Средний если gradient + legacy 10px border coexist — execution must purge |

---

### 4. Catalog cards

| Field | Description |
|-------|-------------|
| **Current look** | White OpenCart cards: `1px rgb(208,208,208)` border, mixed radius (4px legacy vs 10–12px W3V2 subset), hover с **blue-grey** shadow `rgba(55,76,96,0.4)` — чужой hue. Price red legacy `rgb(170,3,3)`. Stock green neon. На `/cars/` W3UX-C1 density active — компактнее, но surface language тот же. |
| **Target look** | **Vehicle offer cards:** white `#FFFFFF` on canvas, border `rgba(47,52,62,0.10)`, radius 12px unified, **graphite shadow stack** rest/hover. Image container — neutral tone без yellow cast. Price/CTA — brand red system `#9E0202` / muted `#B82424` for large price text. Hover = shadow-md + border-hover, **без** чужого blue glow. |
| **What changes visually** | Каталог читается как **витрина автомobile offers**, не OC product grid. Карточки «парят» над canvas; hover cohesive. four_blocks-level inconsistency исчезает в card group. Пользователь чувствует **единый салон**, не collage шаблонов. |
| **What does NOT change** | Card layout, grid columns, image aspect, text content, price typography **sizes**, W3UX-C1 spacing/height on `.used_catalog`, swiper structure. |
| **Expected visual impact** | **8/10** на `/cars/` и homepage catalog blocks |
| **Risk** | Средний: dual CSS layer — без purge часть cards останется legacy |

---

### 5. Forms

| Field | Description |
|-------|-------------|
| **Current look** | CMS-style: white inputs on white/near-white, flat grey borders, focus = **red neon glow** `0 0 10px rgb(170,3,3)`. Lead bands (`.fancy_form_block`) = flat dark `#21242B` + bg image — «второй footer». Popup forms mix dark/light variants. |
| **Target look** | **Dealership lead forms:** inputs on `#FAFBFC` or white with soft border; focus = **3px soft red ring** `rgba(158,2,2,0.18)` без neon. Primary buttons — red + `--w3color-shadow-cta`. Form containers — L2 depth (shadow-sm) отделяют форму от canvas. Dark lead bands — refined graphite + subtle gradient overlay, не flat slab. |
| **What changes visually** | Формы перестают выглядить «админкой OpenCart». Focus calm и premium. Filter/search panel (L2-alt raised) **визually distinct** от product cards — пользователь понимает «инструмент поиска» vs «товар». |
| **What does NOT change** | Field count, labels, validation, submit logic, form placement, popup triggers. |
| **Expected visual impact** | **6/10** — заметно при interaction (focus, submit) |
| **Risk** | Низкий. Dark form bands — средний если bg image fights gradient |

---

### 6. Partner banks / advantage cards / service cards

| Field | Description |
|-------|-------------|
| **Current look** | Partner banks: large white pads, logo centered, minimal depth. **four_blocks:** legacy 4px radius, grey border, **no shadow** — явный pre-W3V2. Service/two-col blocks inconsistent with catalog card group. |
| **Target look** | **Consistent premium card language:** все L2 family — white surface, 12px radius, graphite border, shadow-sm, hover shadow-md. Banks logos sit in **defined card frame**, not empty white tile. Advantages finally match catalog/reviews. |
| **What changes visually** | Homepage и about перестают «проваливаться» в legacy corner. Блок преимуществ выглядит **частью той же витрины**, что и catalog. Partner slider — professional grid, не placeholder tiles. |
| **What does NOT change** | Logo images, advantage text/icons, column count, slider behavior, content order. |
| **Expected visual impact** | **7/10** на `/` и `/about` |
| **Risk** | Низкий. Highest ROI: four_blocks migration (discovery rank #3) |

---

### 7. PDP widgets

| Field | Description |
|-------|-------------|
| **Current look** | Many white blocks on grey-ish canvas: photo column, info column, discount widget, credit block, VIN — **fragments without shared atmosphere**. Dark credit/VIN bands = same flat nav chrome. Discount white island inside column. |
| **Target look** | **Same blocks, clearer surface separation:** columns get subtle L2 treatment where W3V2 already partial; discount/credit/VIN aligned to L1/L2/L3 levels. Canvas uplift makes white widgets **read as panels on stone floor**. Dark bands = same graphite gradient language as nav/footer — not duplicate footer feel. |
| **What changes visually** | PDP less «склеен из кусков OC». Widget boundaries visible through **atmosphere only** — пользователь easier scans sections without reading headings. Price block hierarchy **unchanged** but sits on cleaner stage. |
| **What does NOT change** | PDP hero layout, CTA order/flex, price hierarchy, photo gallery structure, flex order, commercial block sequence (W3VIS rollback preserved). |
| **Expected visual impact** | **5/10** — заметно при внимательном просмотре PDP; меньше чем catalog/footer |
| **Risk** | Средний «invisible improvement» zone — без canvas + card unification эффект слабее |

---

### 8. Mobile atmosphere

| Field | Description |
|-------|-------------|
| **Current look** | Same template compressed: white cards edge-to-edge feeling, harsh nav/footer cuts, legacy 4px on some cards, W3UX-C1 tighter cards on `/cars/`. Offcanvas nav flat dark. |
| **Target look** | **Same layout, finished visually:** canvas contrast stronger on small screens (cards «float»). Header shadow + nav gradient parity. Touch targets unchanged; card radius/shadow unified. Offcanvas matches nav gradient tokens. Footer gradient + muted legal improve scroll-end on phone. |
| **What changes visually** | Mobile перестаёт feel like «desktop squeezed» — **same breakpoints**, но surface system complete. Catalog on phone = stacked offer cards on stone background, not white stack on white. |
| **What does NOT change** | Breakpoints, hamburger behavior, W3UX-C1 mobile card height (+7% per W3UX-C1 decision), tap targets, column collapse rules, offcanvas item list. |
| **Expected visual impact** | **6/10** mobile / **7/10** if user compares before/after side-by-side |
| **Risk** | Low. Shadow performance on low-end devices — soft shadows only, no heavy blur |

---

## A. Before / After description table

| Zone | Before (operator language) | After (operator language) |
|------|---------------------------|----------------------------|
| **Global canvas** | Белый лист; карточки не отделены от фона | Stone-grey «пол салона»; белые блоки лежат на поверхности |
| **Header** | Белый top + резкий чёрный nav cut | Floating white reception + smooth graphite nav band |
| **Footer** | Плоская чёрная масса, heavy legal | Layered graphite gradient, muted legal, brand accent |
| **Catalog cards** | OC white boxes, mixed borders/hover | Unified offer cards, graphite depth, cohesive hover |
| **Forms** | CMS flat inputs, red neon focus | Dealership calm focus ring, raised tool panels |
| **Banks / advantages / service** | Flat tiles, four_blocks legacy | One premium card language sitewide |
| **PDP widgets** | White fragments on grey | Same layout, clearer panel separation |
| **Mobile** | Compressed template | Same grid, finished surfaces |

---

## B. Top 10 visible changes the operator should notice immediately

1. **Страница стала «глубже»** — фон заметно не белый; карточки отрываются от canvas.
2. **Header/nav** — исчез резкий чёрный шов между белой полосой и меню.
3. **Footer** — gradient вместо flat black; legal text менее агрессивен.
4. **Каталог** — карточки выглядят как витрина авто, не OC products; hover без blue tint.
5. **four_blocks / advantages** — наконец совпадают с catalog cards (radius, shadow).
6. **Filter/search panel** — чуть другой surface (raised grey-white), отличим от карточек.
7. **Тёмные band** (credit, lead form, slider overlay) — graphite family, не «второй footer».
8. **Focus на inputs** — soft ring вместо red glow.
9. **Stock/tags green** — спокойный `#1F8A4C` вместо neon.
10. **Partner bank tiles** — framed cards, не пустые белые подложки.

---

## C. Top 10 things explicitly NOT changed

1. **Layout / DOM / Twig** — zero structural edits.
2. **W3UX-C1 catalog density** — `.used_catalog` spacing/height preserved.
3. **PDP hero** — no unified hero wrapper (W3VIS lesson).
4. **CTA order and flex order** — commercial hierarchy untouched.
5. **Price typography sizes** — atmosphere only, not hierarchy wave.
6. **Footer columns, links, legal text content** — no collapse, no removal.
7. **Navigation items and header CTA count** — positions frozen.
8. **Form fields and validation logic** — visual skin only.
9. **Card grid density and column counts** — no spacing wave.
10. **Content, images, copy** — no editorial changes.

---

## D. Risk of «invisible improvement»

### Will this be visibly different for a normal user?

**Honest answer: YES — for most pages, YES without A/B screenshot.**

| Audience | Expected perception |
|----------|---------------------|
| **Casual visitor (first glance)** | «Сайт стал аккуратнее / дороже» — mainly canvas + header/footer + catalog. **Likely notices** on homepage and `/cars/`. |
| **Returning operator** | **Will notice** immediately — background, footer, card consistency. |
| **PDP-only visitor** | **Moderate** — improvement real but subtler (5/10); hero/CTA unchanged limits drama. |
| **Mobile user** | **Yes** — canvas contrast and card float more obvious on small screens. |

### Invisible-improvement risks

| Risk | Mitigation in execution |
|------|-------------------------|
| Canvas change too subtle on calibrated displays | `#EEF1F5` chosen for ~5% Δ; discovery validated vs `#F7F8FA` |
| Partial legacy purge leaves patchy pages | Execution must include **full literal purge** (56× red, 48× dark, 24× grey) |
| W3V2 + W3COLOR token coexistence | Bridge `--w3v2-*` → `--w3color-*` in one override pass |
| Operator expects «new site» | Preview sets expectation: **6/10** transformation, not 10/10 rebrand |
| PDP feels «same» | Acceptable — PDP structural wave explicitly OUT OF SCOPE |

**Overall invisible-improvement risk:** **LOW–MEDIUM** if execution completes purge; **HIGH** if only canvas token changed without card/footer/header pass.

---

## E. Go / No-Go recommendation

| Gate | Status |
|------|--------|
| W3COLOR-01 discovery | **DONE** |
| W3ATMOSPHERE-01A visual preview | **DONE** — this document |
| Operator preview review | **PENDING** |
| W3ATMOSPHERE-01 write charter | **NOT AUTHORIZED** |
| W3ATMOSPHERE-01 execution | **NOT AUTHORIZED** |

### Decision

## **READY FOR W3ATMOSPHERE-01 EXECUTION**

**Notes (required before charter):**

1. Preview assumes **full wave scope** — canvas + header/footer + unified card system + legacy purge. Partial execution risks «invisible improvement» (see §D).
2. Preserve **W3UX-C1** `.used_catalog` block verbatim in charter exclusions.
3. **No PDP hero / CTA hierarchy** — charter must restate W3VIS rollback boundaries.
4. Operator browser sign-off on TEST recommended after execution — W3V2 sign-off still pending.
5. Rollback tier **T1** — pre-w3atmosphere CSS backup before write.

---

## Authorization state

| Action | Status |
|--------|--------|
| Site modification | **FORBIDDEN** — preview only |
| Production | **FORBIDDEN** |
| FTP / cache / admin | **NOT USED** |

---

## Related documents

| Document | Role |
|----------|------|
| [SITE-001-W3COLOR-01-DISCOVERY-v1.md](SITE-001-W3COLOR-01-DISCOVERY-v1.md) | Technical discovery + token proposal |
| [SITE-001-W3VIS-ROLLBACK-DECISION-v1.md](SITE-001-W3VIS-ROLLBACK-DECISION-v1.md) | OUT OF SCOPE boundaries |
| [SITE-001-W3UX-C1-DECISION-v1.md](SITE-001-W3UX-C1-DECISION-v1.md) | Density preserve rules |
| [SITE-001-W3V2-EXECUTION-v1.md](SITE-001-W3V2-EXECUTION-v1.md) | Active partial layer superseded by atmosphere wave |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W3ATMOSPHERE-01A visual preview; no site modifications |

*SITE-001 W3ATMOSPHERE-01A Visual Preview v1 — preview only; no implementation.*
