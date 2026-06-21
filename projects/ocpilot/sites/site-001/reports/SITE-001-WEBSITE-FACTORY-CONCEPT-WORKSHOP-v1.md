# SITE-001 — Website Factory Concept Workshop v1

**Type:** Design concept workshop — documentation only  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Design owner:** Website Factory  
**Mode:** **DESIGN ONLY** — no FTP · no CSS · no Twig · no PHP · no JS · no DB

**Explicit exclusions:** No implementation proposals. No CSS patches. No atmosphere tweaks. No token changes.

---

## Workshop mandate

Website Factory **останавливает implementation work** до выбора визуального направления.

**Проблема (оператор + аудит):**

| Signal | Detail |
|--------|--------|
| Technical execution | **GOOD** — OCPilot quality is not the issue |
| Visual impact | **LOW** — большинство волн видны только при A/B |
| Perception | Сайт всё ещё читается как **старый OpenCart-шаблон автосалона** |
| Sticky header (W4.1) | **Ошибка направления** — не продолжать |
| Baseline score | **3/10** — текущий first impression |

**Цель воркшопа:** три **принципиально разных** визуальных концепта. Обычный посетитель должен заметить разницу **за 3 секунды** (без сравнения с предыдущей версией).

**Scope (только first impression):**

1. Header  
2. Homepage first screen  
3. Used PDP first screen  

**Вне scope:** footer · forms · SEO · catalog density · PDP widgets below fold · credit blocks · technical cleanup

---

## Inputs reviewed

- [SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md](SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md) — mixed cause; CSS live; deltas too weak  
- [SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md](SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md) — W4.1 PARTIAL SUCCESS; homepage **NO** visitor notice  
- [SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md](SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md) — W4 structural hero (preserve as asset)  
- [SITE-001-W4-1-HEADER-HERO-DESIGN-PLAN-v1.md](SITE-001-W4-1-HEADER-HERO-DESIGN-PLAN-v1.md) — header authority slice (sticky rejected)  
- [SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md](SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md) — «Graphite Salon» (superseded for first-impression strategy by this workshop)

---

## Shared diagnosis — why 3/10 persists

| Layer | Current read (visitor, 3 sec) |
|-------|-------------------------------|
| **Header** | Три горизонтальных полосы (белая / тёмная / promo) = типичный OC-dealer stack; даже после W4.1 градиента — **анатомия шаблона** |
| **Homepage** | Полноэкранный слайдер + мелкий текст + красные CTA = discount-dealer carousel, не showroom |
| **Used PDP** | Breadcrumbs + H1 вне hero; W4 card помогает, но верх экрана = «каталог OC с картинкой слева» |
| **Cross-cutting** | Инкрементальные CSS-волны меняют **отделку**, не **сцену** — first screen composition frozen |

**Hard constraints from operator history:**

- **No sticky header** — W4.1 sticky признан ошибкой  
- **Preserve** Phase 1 branding, copy, URLs, phone, menu items  
- **Preserve** W3UX-C1 catalog density (below first screen)  
- **Preserve** W4 used PDP structural work as reusable asset where concepts allow  

---

# CONCEPT A — «Региональный Про»

## 1. Name

**«Региональный Про»** (Regional Pro)

## 2. One-sentence positioning

Сильный региональный автосалон, который **причесывает** текущий шаблон до уровня «нам можно доверять», не ломая привычную структуру OpenCart.

## 3. Header concept

**Двухъярусная полоса без sticky.**

| Tier | Treatment |
|------|-----------|
| **Utility bar** | Компактная белая полоса: часы · телефон · мессенджеры в одну линию; убрать визуальный шум (лишние borders, красные иконки) |
| **Main nav** | Единый graphite block **без** резкого шва с utility — мягкий переход; logo крупнее на 15%; nav items с равным ритмом; **один** красный CTA «Обратный звонок» |
| **Promo strip** | Тонкая лента под nav — CAPS, graphite, красная точка; **не** бегущий красный тикер |

**Ключевое отличие от live:** не новая анатомия — **сшивка** трёх полос в один «dealership frame»; снятие конкурирующих красных зон.

## 4. Homepage first screen concept

**Тот же слайдер, новая сцена.**

- Слайдер остаётся full-width, но overlay: **тёмный градиент снизу** (40% высоты) вместо плоского затемнения  
- Заголовок акции — **крупнее**, белый, 2 строки max; подзаголовок — muted  
- Под слайдером (в fold): **одна** горизонтальная полоса «СИБКАР — авто с пробегом» как **единая L2-панель** с иконками преимуществ — не три разрозненных блока  
- CTA на слайде: **одна** primary кнопка + ghost secondary  

**Ключевое отличие:** слайдер читается как **баннер салона**, не как «ещё один OC-carousel».

## 5. Used PDP first screen concept

**W4 hero сохраняется; верх — editorial band.**

- `w4-1-pdp-top` расширяется: breadcrumbs мелкие, H1 — **крупный editorial** на светлом canvas (не под nav shadow)  
- W4 unified hero card — **больше воздуха** сверху; gallery edge-to-edge внутри card  
- Price — единственный красный акцент в hero panel  
- Trust badges — pill chips над gallery, не loose text row  

**Ключевое отличие:** PDP top = **статья о машине**, не «заголовок каталога OC».

## 6. What changes visually

| Area | Change |
|------|--------|
| Header | Сшивка tiers · red discipline · logo scale · no sticky |
| Homepage | Slider overlay hierarchy · single advantage band · CTA reduction |
| Used PDP | Editorial title band · hero card polish · badge pills |
| Overall | Меньше «склеек», больше **ритма** — но **та же** OC-геометрия |

## 7. What stays unchanged

- DOM structure header (toolbar + nav + promo) — **no reorder**  
- Homepage slider engine, slide count, texts  
- W4 twig wrappers (`w4-used-*`) — preserved  
- Menu items, URLs, logo file, phone  
- Footer, forms, catalog grid, credit blocks  
- No sticky behavior  

## 8. Expected operator reaction

«Стало аккуратнее и дороже, но **это всё ещё наш старый сайт**. Где трансформация?» — риск повторения feedback W3ATMOSPHERE / W4.1.

## 9. Expected customer reaction

«Нормальный автосалон, похоже на другие региональные дилеров» — доверие **слегка** выше, wow-эффекта нет.

## 10. Visual impact score

| Baseline | Result | Delta |
|----------|--------|-------|
| **3/10** | **5/10** | +2 — заметно при внимании, **не** за 3 сек без A/B |

---

# CONCEPT B — «Современный Дилер 2026»

## 1. Name

**«Современный Дилер 2026»** (Modern Dealer)

## 2. One-sentence positioning

Автосалон 2026 года на **том же OpenCart-каркасе**: first screen как **цифровой шоурум**, а не набор горизонтальных полос шаблона.

## 3. Header concept

**«Dealer shell» — два режима, один блок. No sticky.**

| Zone | Treatment |
|------|-----------|
| **Top contact rail** | Ultra-compact (32px): телефон + WhatsApp справа; часы — muted; **скрыть** на mobile в burger context |
| **Primary nav band** | Full-width **immersive graphite** (72px): logo left · **centered nav** (5 items) · CTA cluster right (callback pill + phone) |
| **Promo** | **Внутри** nav band как тонкий bottom inset (24px) — не отдельная третья полоса; один rotating message |
| **Scroll behavior** | **Static** — header уезжает со scroll; **no position:sticky** |

**Ключевое отличие:** из **трёх полос** → **один dealership shell** с inset promo. Центрированная nav = сигнал «не OC-sidebar template».

## 4. Homepage first screen concept

**«Showroom entry» — слайдер + search anchor.**

| Element | Treatment |
|---------|-----------|
| **Hero** | Слайдер 85vh max; **крупная типографика** слева (48–56px): «Авто с пробегом в [город]» — не мелкий текст акции; vehicle image dominant right |
| **Search strip** | **Floating card** overlapping hero bottom (−48px): марка · модель · цена от · кнопка «Показать N авто» — главный entry point |
| **Below fold edge** | 3 featured vehicles в **горизонтальном scroll** (card peek) — не four_blocks grid |
| **Color** | Cool stone canvas `#E8ECF1`; hero dark-to-light gradient bleed |

**Ключевое отличие:** visitor за 3 сек видит **«сайт для поиска машины»**, не «баннерную карусель».

## 5. Used PDP first screen concept

**«Magazine PDP» — stage + floating offer.**

| Zone | Treatment |
|------|-----------|
| **Top** | Minimal breadcrumb strip (no H1 here — H1 moves into hero) |
| **Hero stage** | Full-width **dark canvas band** (graphite `#2A2F38`); gallery **70%** width, edge-bleed photos; vehicle name + year as **white H1 overlay** on gallery |
| **Offer panel** | **Floating white card** overlapping gallery right edge (−80px overlap): price large · credit line · 3 spec chips · **one** red CTA «Забронировать просмотр» |
| **W4 asset** | Reuse `w4-used-hero` grouping inside stage — **re-skin**, not discard |
| **Trust** | Light strip below stage — icons + «Проверено СИБКАР» |

**Ключевое отличие:** PDP = **витрина одной машины**, не «две колонки 50/50 как в OC».

## 6. What changes visually

| Area | Change |
|------|--------|
| Header | 3-band → 1 shell; centered nav; inset promo; static scroll |
| Homepage | Typography scale jump; search floating card; featured scroll |
| Used PDP | Dark stage; overlapping offer card; H1 on gallery |
| Overall | **Composition change** — geometry first, polish second |

## 7. What stays unchanged

- OpenCart routes, product data, gallery Swiper hooks  
- Menu items, texts (можно reposition, не переписывать)  
- W4 twig wrapper classes — **adapt**, not delete  
- W3UX-C1 catalog (below first screen on `/cars/`)  
- Footer, forms, credit calc logic  
- No sticky header  

## 8. Expected operator reaction

«**Вот это уже другой сайт** — но узнаём СИБКАР. Можно показывать клиентам.» — balanced risk/reward.

## 9. Expected customer reaction

«Современный автосалон, удобно искать машину / смотреть конкретное авто» — **доверие + clarity** за 3 сек.

## 10. Visual impact score

| Baseline | Result | Delta |
|----------|--------|-------|
| **3/10** | **7/10** | +4 — **3-second test PASS** на homepage и PDP |

---

# CONCEPT C — «Премиум Шоурум»

## 1. Name

**«Премиум Шоурум»** (Premium Showroom)

## 2. One-sentence positioning

Восприятие **ценности** важнее плотности каталога: сайт как **галерея**, где каждая машина — экспонат, а не товарная позиция.

## 3. Header concept

**«Gallery minimal» — почти невидимый.**

| Element | Treatment |
|---------|-----------|
| **Header** | **Transparent over hero** on homepage/PDP; при scroll → frosted white bar (backdrop-blur), **не** dark nav |
| **Logo** | Centered, monochrome dark; tagline скрыт в header (только в footer/about) |
| **Nav** | Thin text links, wide letter-spacing; **no background block** on first screen |
| **CTA** | Только outline pill «Связаться» — red **только** on hover |
| **Promo** | **Убрать** с first screen entirely — promo только на catalog |

**Ключевое отличие:** header **исчезает** как «полоса» — visitor видит **машину**, не chrome.

## 4. Homepage first screen concept

**«Single hero vehicle» — editorial luxury.**

| Element | Treatment |
|---------|-----------|
| **Layout** | Full-viewport (**100vh**); **одна** hero-машина (curated, не carousel) — slow Ken Burns или static hero photo |
| **Typography** | Serif-accent headline (e.g. «Выберите автомобиль с историей») — large, left-aligned, generous whitespace |
| **CTA** | Single text link «Смотреть каталог →» — no red button on hero |
| **Navigation entry** | Bottom edge: 3 category tiles (С пробегом · Новые · Trade-in) — large photography, minimal text |
| **Palette** | Warm white `#FAFAF8` + charcoal text; red **absent** from first screen |

**Ключевое отличие:** homepage = **luxury editorial**, не dealer promo site.

## 5. Used PDP first screen concept

**«Exhibition stand» — машина на пьедестале.**

| Zone | Treatment |
|------|-----------|
| **Canvas** | Warm white full bleed; **no** dark bands |
| **Gallery** | Centered vehicle, **max 60%** width, generous padding; photos on **neutral gradient floor** shadow |
| **Info** | Below gallery (not beside): H1 centered · price as **typographic statement** (large, charcoal, not red) · specs as **horizontal luxury strip** (year · km · owners) |
| **CTA** | Full-width subtle bar: «Записаться на просмотр» — charcoal fill, red only icon |
| **W4** | Hero grouping simplified — **remove** card border; gallery floats on white |

**Ключевое отличие:** PDP = **музейный экспонат**, не commerce grid.

## 6. What changes visually

| Area | Change |
|------|--------|
| Header | Transparent → frosted; centered logo; no dark nav block |
| Homepage | Single hero; serif editorial; no carousel; no red on first screen |
| Used PDP | Centered exhibition; vertical flow; price as typography |
| Overall | **Maximum whitespace**; value perception over conversion density |

## 7. What stays unchanged

- Backend, routes, product data  
- Menu structure (visual only hidden/minimized)  
- Catalog and credit below fold (untouched in scope)  
- Brand logo file (recolor in CSS only — concept level)  

## 8. Expected operator reaction

«Красиво, но **не мы** — клиенты подумают, что машины стали дороже, чем есть. Где акции? Где красный СИБКАР?» — **brand mismatch risk**.

## 9. Expected customer reaction

Часть аудитории: «Премиальный салон» (**C**). Другая: «Слишком пусто / непонятно где цены» — **bounce risk** для mass-market used cars.

## 10. Visual impact score

| Baseline | Result | Delta |
|----------|--------|-------|
| **3/10** | **8/10** | +5 — **3-second test PASS** as premium; **FAIL** as familiar СИБКАР |

---

# 3-SECOND TEST

> **Method:** Logo hidden 3 seconds. User sees only header shape, hero composition, color rhythm, typography scale.  
> **Question:** Old OpenCart dealer template (A) · Modern dealership (B) · Premium automotive brand (C)?

## Concept A — «Региональный Про»

| Answer | **A — Old OpenCart dealer template** (borderline) |
|--------|-----------------------------------------------------|
| **Why** | Три горизонтальных полосы + full-width slider + красный CTA = **узнаваемая OC-dealer DNA**. Полировка не меняет силуэт. Visitor скажет «автосалон на OpenCart», не «новый сайт». |
| **3-sec PASS?** | **NO** — delta слишком слабый для mandate воркшопа |

## Concept B — «Современный Дилер 2026»

| Answer | **B — Modern dealership** |
|--------|---------------------------|
| **Why** | Unified nav shell + крупная типографика + floating search / dark PDP stage = **сигналы 2020s auto retail** (Carvana-adjacent clarity, regional dealer scale). Не luxury brand, но **явно не OC-template**. |
| **3-sec PASS?** | **YES** — homepage и PDP читаются иначе **без** logo |

## Concept C — «Премиум Шоурум»

| Answer | **C — Premium automotive brand** (partial) |
|--------|---------------------------------------------|
| **Why** | Whitespace, serif, transparent header, centered exhibition = **luxury cues** (Lexus/Polestar editorial). Но без logo СИБКАР visitor может не связать с **региональным пробегом** — brand category confusion. |
| **3-sec PASS?** | **YES** for premium read; **FAIL** for «это СИБКАР» recognition |

---

## Concept comparison matrix

| Criterion | A — Regional Pro | B — Modern Dealer | C — Premium Showroom |
|-----------|------------------|-------------------|----------------------|
| 3-second noticeable | NO | **YES** | YES (wrong brand read) |
| Implementation feasibility | **Highest** | **High** | Medium |
| Operator «это другой сайт» | Unlikely | **Likely** | Likely but risky |
| Preserves СИБКАР red identity | **Full** | **Strong** | Weak on first screen |
| Sticky header | No | No | No |
| Twig structural change | Minimal | **Moderate** | **High** |
| Reuses W4 PDP work | Yes | **Yes (re-skin)** | Partial strip |
| Risk of «ещё косметика» | **HIGH** | Low | Low (but wrong-brand) |
| Visual impact score | 5/10 | **7/10** | 8/10 |

---

## Lessons applied from failed waves

| Lesson | How concepts address it |
|--------|-------------------------|
| CSS-only atmosphere too weak | All three change **composition**, not tokens alone |
| Sticky header mistake | **All concepts: static header** |
| W4.1 homepage invisible | B and C **replace hero grammar**; A insufficient |
| Operator wants 3-sec delta | Only **B and C** pass; A repeats failure mode |
| OCPilot execution OK | Concepts are **design direction** for future charter — not OCPilot invention |

---

## Explicit non-deliverables (this workshop)

- No CSS selectors · no token tables · no FTP steps  
- No W3WF-01 continuation · no atmosphere patches  
- No implementation charter · no rollback plan  

**Next artifact:** [SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md](SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md)

*SITE-001 Website Factory Concept Workshop v1 — design documentation only*
