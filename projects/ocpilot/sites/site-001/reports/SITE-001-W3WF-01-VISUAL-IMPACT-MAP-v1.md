# REPORT — SITE-001 W3WF-01 Visual Impact Map

**Type:** Pre-execution visual impact map — operator decision aid (documentation only)  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Wave:** **W3WF-01** — Website Factory Visual Direction Implementation (not yet executed)  
**Design authority:** Website Factory — «Graphite Salon»  
**Implementation authority:** OCPilot (execution only — not design invention)

**Inputs reviewed:**

- [SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md](SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md)
- [SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md](SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md)
- [SITE-001-WEBSITE-FACTORY-DECISION-v1.md](SITE-001-WEBSITE-FACTORY-DECISION-v1.md)
- [SITE-001-W3ATMOSPHERE-01-DECISION-v1.md](SITE-001-W3ATMOSPHERE-01-DECISION-v1.md) — **ACTIVE layer on TEST**
- [SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md](SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md)
- [SITE-001-W3UX-C1-DECISION-v1.md](SITE-001-W3UX-C1-DECISION-v1.md)

**Explicit exclusions:** No FTP · No CSS/Twig/PHP/JS/DB · No cache · No screenshots · No charter · No implementation.

**Critical framing:** «Текущее состояние» в этом документе — **то, что оператор видит на TEST сегодня** (Phase 1 + W3-V + W3V2 + W3UX-C1 + **W3ATMOSPHERE-01 ACTIVE**). W3WF-01 — **не новое направление**, а авторитетная консолидация «Graphite Salon» и закрытие оставшихся дыр в override-слое.

---

## Executive summary

На TEST уже живёт ~70–80% направления «Graphite Salon» через W3ATMOSPHERE-01: stone-canvas, graphite header/footer, унифицированные карточки, raised-панели фильтров. Оператор, открывший сайт **сейчас**, уже видит «салон на сером полу», а не Phase 1 «белый лист».

**W3WF-01** даст:

1. Единый governed CSS-блок `--wf-*` вместо трёх конкурирующих namespace (W3-V / W3V2 / W3COLOR).
2. Расширенный Phase H purge — legacy literals, которые всё ещё «протекают» на отдельных селекторах (N-01 W3ATMOSPHERE).
3. Дожимание patchy-зон: four_blocks-остатки, blue-grey hover, neon focus, 10px near-black seams, flat dark bands вне card group.

**Честный вывод для оператора:** если сравнивать **с сегодняшним TEST**, W3WF-01 — **доводка и выравнивание**, не «другой сайт». Если сравнивать **с Phase 1 checkpoint** — трансформация уже произошла в W3ATMOSPHERE; W3WF-01 закрепляет её под единой спецификацией Website Factory.

---

## 1. Global Canvas

### Current state

Страница лежит на прохладном stone-фоне — не на белом листе. Белые карточки и блоки **отрываются** от фона; каталог и главная читаются как «слои», а не «A4 на столе». На части внутренних страниц или в зонах вне card group фон может казаться почти тем же, если legacy-правило перебивает override.

### Proposed state

Тот же stone-canvas «пол салона» — визуально **тот же замысел**, но без конкурирующих переменных. Фон стабильно `#EEF1F5` на всех маршрутах; опциональные section-tint полосы на homepage выровнены под единый токен. Между canvas и карточками сохраняется ~5% luminance Δ.

### Visual difference

Пользователь, который уже видел TEST после W3ATMOSPHERE, **скорее всего не заметит** смену canvas. Пользователь, который заходил до atmosphere-волны, **уже увидел** основной скачок — W3WF-01 его не повторяет.

**Видно сразу?** Только если на конкретной странице canvas ещё «протекает» в почти-белый — тогда да, локально. Sitewide — **едва**.

### What changes

- Цвет фона body (стабилизация, не смена направления)
- Единый canvas-токен вместо `--w3color-canvas` / разрозненных override
- Устранение точечных страниц, где фон снова сливается с карточками

### What DOES NOT change

- Ширина container, padding секций, порядок блоков
- Grid каталога, W3UX-C1 density на `/cars/`
- DOM, Twig, контент

### Impact

**3/10** (относительно текущего TEST) · **8/10** (если бы baseline был Phase 1 без atmosphere)

---

## 2. Header

### Current state

Белая верхняя полоса (логотип, телефон, callback) с лёгкой тенью — «reception desk». Ниже — graphite gradient nav, без резкого near-black шва в большинстве viewport. Красные CTA на тёмном фоне читаются как брендовые, не кричащие. На scroll duplicate bars язык в целом совпадает. Возможны редкие «грязные» швы, если legacy border перебивает gradient.

### Proposed state

Тот же premium shell: белый L2 top bar + graphite gradient nav + hairline inset highlight. Hover на CTA — soft red depth без neon. Subtitle логотипа приглушён. Seams → 1px translucent on-dark, не 10px near-black.

### Visual difference

**За 3 секунды обычный пользователь:** если W3ATMOSPHERE уже применён — **скорее нет**, разница в швах и глубине тени слишком мала без A/B. Если legacy seam всё ещё виден на конкретном breakpoint — **да, локально**.

### What changes

- Стабилизация gradient nav и header shadow
- Удаление оставшихся near-black seams
- Унификация scroll duplicate bars под `--wf-*`
- Hover depth на phone/callback кнопках

### What DOES NOT change

- DOM header, количество CTA, порядок logo/phone/callback
- Пункты меню, sticky behavior, offcanvas structure
- Высота header/nav

### Impact

**4/10** (vs текущий TEST) · **7/10** (vs Phase 1)

---

## 3. Navigation

### Current state

Горизонтальное меню на graphite gradient band. Пункты и иерархия — стандартные OC/auto theme. Offcanvas на mobile — тёмная панель в graphite family. Активные/hover состояния в основном согласованы с тёмным фоном. Высота и структура меню не менялись с Phase 1.

### Proposed state

Тот же nav по структуре и высоте. Визуально — чуть более «цельная» graphite band: gradient без flat cut, borders on-dark 1px, текст `--wf-text-on-dark`. Offcanvas получает те же токены, что desktop nav — без расхождения «два разных тёмных».

### Visual difference

Без A/B: **едва**. Пользователь не скажет «меню переделали» — скажет «меню как было, но чуть ровнее», и то только при пристальном взгляде.

### What changes

- Фон nav / offcanvas (gradient polish)
- Цвет border между nav и контентом
- Цвет текста и hover на тёмном фоне (тонкая калибровка)

### What DOES NOT change

- **Высота** nav
- **Структура** — пункты, порядок, dropdown, offcanvas items
- Поведение hamburger, breakpoints, tap targets

### Impact

**3/10**

---

## 4. Footer

### Current state

Graphite vertical gradient вместо flat black — «потолок светлее, пол темнее». Legal text приглушён. Тяжёлые 10px near-black borders в основном сняты. Footer всё ещё большой по структуре (колонки, формы, legal) — без collapse. Иногда legacy border или chalky divider может проступать на отдельных секциях.

### Proposed state

Тот же footer по объёму и колонкам. Gradient и muted legal закреплены под `--wf-*`. Seams строго 1px on-dark. Опциональная 2px brand-red accent line под logo zone. Footer CTA — soft red shadow на hover.

### Visual difference

**Почему premium:** gradient + muted legal уже дают «обложку», не «обруб». W3WF-01 **усиливает завершённость** — убирает последние «дешёвые резы» и выравнивает текстовую иерархию. Без A/B: **может** заметить оператор, который скроллит до конца и сравнивает с памятью Phase 1; casual user — **maybe**, если seam ещё виден.

### What changes

- Стабилизация gradient background
- Purge 10px near-black top/bottom seams
- Muted legal / section title dividers
- Decorative brand accent under logo (pseudo, без markup)

### What DOES NOT change

- Колонки, ссылки, legal content, формы в footer
- Высота, stack structure — **no collapse, no hiding, no restructuring**
- Accordion legal, если есть

### Impact

**5/10** (vs текущий TEST) · **7/10** (vs Phase 1)

---

## 5. Catalog Cards

### Used Cars (`/cars/`)

#### Current perception

Компактные offer cards (W3UX-C1 density active): белые карточки на stone canvas, 12px radius в override, graphite shadow в основном. Hover в большинстве случаев без blue-grey glow. Price red в brand family. Stock green спокойнее neon. Карточки **уже не** чистый OC-template look, но grid layout и card anatomy — всё ещё OpenCart (image top, info block, CTA strip).

#### Future perception

Тот же grid и anatomy. Surface language **дожимается**: единый L2 recipe на всех `.catalog_item` селекторах, без legacy 4px / `rgb(208,208,208)` bleed. Hover строго graphite shadow stack. Price `--wf-brand-red-muted`; stock `--wf-success`.

#### Will cards still look like OpenCart cards?

**Да.** Та же сетка, те же пропорции image/info, те же кнопки в тех же местах. Меняется **отделка рамки**, не тип карточки. Пользователь скажет «аккуратнее», не «другой каталог».

#### Impact (Used Cars)

**5/10** (vs текущий TEST) · **8/10** (vs Phase 1)

---

### New Cars (`/auto/`)

#### Current perception

Те же `.catalog_item` family, но **без** W3UX-C1 density — карточки чуть выше/воздушнее. Surface language в целом совпадает с used, но patchy legacy чаще заметен на brand-страницах и в swiper-блоках. Blue-grey hover или 4px radius могут всплывать на отдельных items.

#### Future perception

Тот же layout new-car catalog. L2 recipe enforced sitewide — used и new **визуально одна семья** (рамка, тень, hover), различие только в плотности (W3UX-C1 preserve на used).

#### Will cards still look like OpenCart cards?

**Да** — та же OC card anatomy. W3WF-01 выравнивает **used vs new** по surface, не меняет card type.

#### Impact (New Cars)

**6/10** (vs текущий TEST — здесь больше room для purge) · **8/10** (vs Phase 1)

---

## 6. Filters and Search

### Current state

Панель фильтров и search form уже на raised surface `#FAFBFC` — визуально **отличима** от белых product cards. Но на части страниц filter block может сливаться с card, если legacy background перебивает. Focus на inputs — в основном soft ring, но neon red glow может остаться на отдельных полях.

### Proposed state

Filters/search — стабильный **L2-alt tool panel**: слегка приподнятый серо-белый фон, graphite border, shadow-sm. Чётко «инструмент», не «ещё одна карточка товара». Focus ring единый — calm 3px red ring, без neon.

### Visual difference

**Почему filters become tools:** raised surface + другой hue vs pure white card — пользователь интуитивно отделяет «настроить поиск» от «купить авто». Без A/B на TEST post-atmosphere: **низкая** дельта; **средняя**, если filter panel ещё белая на конкретной странице.

### What changes

- Background filter/search panels
- Border и shadow tool panels
- Input focus ring (purge neon)

### What DOES NOT change

- Поля фильтров, labels, логика submit
- Placement sidebar/top filter
- Grid каталога рядом с фильтром

### Impact

**4/10** (vs текущий TEST) · **6/10** (vs Phase 1)

---

## 7. Forms

### Current state

Contact, callback, footer forms, popup leads — mix white inputs и dark lead bands. Часть форм уже с soft focus ring; часть — legacy red neon glow. `.fancy_form_block` и credit bands — graphite-ish, но иногда flat `#21242B` slab с bg image. Формы **не** ощущаются одной семьёй на всех маршрутах.

### Proposed state

Все storefront forms — **одна visual family**: white или raised fill, soft graphite border, calm focus ring, primary submit red + soft CTA shadow. Dark lead bands — graphite gradient overlay, не flat black. Popup wrappers — L2 depth от canvas.

### Visual difference

При **взаимодействии** (focus, submit) — заметнее всего. При простом скролле — **слабо**. Оператор увидит «формы наконец из одного набора», если ходит по contact + footer + popup. Casual user — **maybe** только при клике в поле.

### What changes

- Input/textarea/select border и focus
- Dark band backgrounds (lead, credit popup)
- Form container shadow/depth
- Primary button hover shadow

### What DOES NOT change

- Field count, labels, validation, placement
- Popup triggers, submit logic

### Impact

**5/10** (interaction-driven) · **6/10** (vs Phase 1)

---

## 8. Homepage Blocks

### Current state

**four_blocks:** в основном уже 12px + shadow после W3ATMOSPHERE, но legacy 4px / no-shadow pockets возможны. **Partner banks:** framed cards, логотипы в белых плитках — уже ближе к premium. **Reviews:** L2 inner cards. **Service blocks** (`fancy_two_blocks`): в целом в card group, но inconsistency с four_blocks возможна. Homepage **уже** читается как salon, не discount PDF — но углы «две эпохи OC» могут бросаться в глаза оператору.

### Proposed state

Все четыре семьи — **один L2 recipe**: white card, 12px, graphite border, shadow-sm, hover shadow-md. four_blocks **полностью** мигрированы с legacy — highest ROI на `/` и `/about`. Banks/reviews/service — без «пустых белых подложек». Опциональный section tint `#F4F6F9` на существующих band-селекторах.

### Visual difference

На главной W3WF-01 — **самая заметная** зона vs текущий TEST (наряду с patchy catalog): four_blocks и service blocks перестают «проваливаться» в старый OC. Без A/B: оператор на `/` — **да, скорее заметит** выравнивание блоков; casual visitor — **maybe**, если four_blocks уже выглядели нормально после atmosphere.

### What changes

- four_blocks, partner_banks, reviews, fancy_two_blocks surfaces
- Hover/border/radius unification
- Optional homepage section tint

### What DOES NOT change

- Тексты, иконки, логотипы банков
- Column count, slider behavior, block order
- Swiper structure

### Impact

**6/10** (vs текущий TEST) · **7/10** (vs Phase 1)

---

## 9. PDP Widgets

### Current state

Hero layout, CTA order, price hierarchy — **без W3VIS** (rolled back). Photo column, info column, discount widget, credit, VIN — white/grey fragments на stone canvas. Dark credit/VIN bands частично graphite. Canvas uplift уже помогает: widgets читаются как panels on floor. Эффект **умеренный** — 5/10 в atmosphere decision.

### Proposed state

**Тот же hero. Тот же CTA hierarchy. Никакого W3VIS resurrection.** Только atmosphere: subtle L2 border/shadow на photo/info columns где селекторы есть; discount widget — L2 card; credit/VIN — graphite gradient family как nav/footer. White widgets чётче на stone floor.

### Visual difference

PDP — зона с **наименьшей** дельтой. Пользователь не скажет «страница авто переделана» — максимум «чуть чище блоки». Без A/B: **barely** на PDP-only visit.

### What changes

- Border/shadow на widget panels (atmosphere only)
- Dark band gradient alignment
- Discount widget L2 frame

### What DOES NOT change

- Hero layout, columns, flex order
- CTA count, order, commercial hierarchy
- Price typography sizes, gallery structure

### Impact

**3/10** (vs текущий TEST) · **5/10** (vs Phase 1)

---

## 10. Mobile

### Current state

Те же breakpoints. Canvas contrast на маленьком экране заметен — cards «float». Nav/offcanvas graphite. W3UX-C1 tighter cards на `/cars/` (+7% mobile height per C1). Footer gradient на scroll-end. Возможны расхождения offcanvas vs desktop nav tokens.

### Proposed state

**Тот же layout.** Surface system дожат до parity: nav/offcanvas/footer/catalog cards используют те же `--wf-*` что desktop. Mood: cool stone floor + graphite shell + white offer cards — **тот же salon mood**, не отдельный «mobile theme».

### Visual difference

**Will mobile mood match desktop mood?** **Да** — по замыслу Graphite Salon. Дельта W3WF-01 vs текущий mobile TEST: **низкая**; цель — убрать последние расхождения offcanvas/legacy 4px.

### What changes

- Mobile nav/offcanvas/footer/card tokens mirror desktop
- Purge mobile-specific legacy hover/border bleed

### What DOES NOT change

- Breakpoints, hamburger, W3UX-C1 mobile card height
- Tap targets, column collapse, offcanvas item list

### Impact

**4/10** (vs текущий TEST) · **6/10** (vs Phase 1)

---

## BEFORE / AFTER SUMMARY

| Zone | Difference Visibility (vs текущий TEST) | Impact (1–10) |
|------|----------------------------------------|---------------|
| Global Canvas | LOW | 3 |
| Header | LOW | 4 |
| Navigation | LOW | 3 |
| Footer | LOW–MEDIUM | 5 |
| Catalog — Used Cars | LOW–MEDIUM | 5 |
| Catalog — New Cars | MEDIUM | 6 |
| Filters and Search | LOW–MEDIUM | 4 |
| Forms | MEDIUM (on interaction) | 5 |
| Homepage Blocks | MEDIUM | 6 |
| PDP Widgets | LOW | 3 |
| Mobile | LOW–MEDIUM | 4 |

**Сводная видимость W3WF-01 относительно сегодняшнего TEST:** преимущественно **LOW–MEDIUM**. Это **не ошибка** — основная трансформация уже в W3ATMOSPHERE-01.

---

## Reality check

**Если оператор открывает сайт без A/B comparison (текущий TEST → post-W3WF-01):**

| Zone | Заметит? | Честный ответ |
|------|----------|---------------|
| **Header** | **Maybe / barely** | Gradient shell уже есть; W3WF-01 — швы и тени |
| **Footer** | **Maybe** | Gradient уже есть; дельта — legal tone и последние seams |
| **Homepage** | **Maybe — да** (оператор) / **barely** (casual) | four_blocks purge — главный шанс заметить |
| **Catalog** | **Maybe** | Cards уже salon-like; new cars чуть больше room |
| **PDP** | **Barely** | Atmosphere only; hero/CTA frozen |

**Если оператор не заходил на TEST с W3ATMOSPHERE:** он **уже** увидел большую часть «Graphite Salon» — W3WF-01 не повторит этот wow.

**Риск «это опять косметика»:** **реальный**, если ожидание = «другой сайт». W3WF-01 = **косметика-консолидация** относительно текущего TEST, **архитектурная** относительно fragmented CSS layers.

---

## Design Risk Assessment

### 1. Changes that may feel too subtle

- Global canvas (уже `#EEF1F5`)
- Header/nav gradient polish
- PDP widget borders
- Navigation text tone calibration

### 2. Changes that may be invisible

- Token namespace bridge (`--wf-*` replacing `--w3color-*`) — **технически важно, визуально ноль**
- Purge legacy literals на селекторах вне card group
- Scroll duplicate bar token unification

### 3. Areas where Graphite Salon may fail

- **Dual CSS layer:** 7k+ строк base + override — без полного Phase H patchy pages останутся
- **PDP:** atmosphere-only ceiling — operator may expect hero-level change (forbidden)
- **«Дороже» expectation:** без typography/spacing waves salon feel hits ~6–7/10 cap
- **Monitors:** 5% canvas Δ уже потрачен в W3ATMOSPHERE — повторного скачка нет

### 4. Areas where operator expectations may exceed actual visual impact

- Ожидание «новый сайт» — W3WF-01 не даёт
- Ожидание «как в макете агентства» — структура OC frozen
- Ожидание dramatic PDP — OUT OF SCOPE
- Сравнение с Phase 1 memory — эффект уже случился; W3WF-01 не добавит второй такой же скачок

---

## Operator decision question

Перед CSS execution оператор должен ответить:

> **«Да, вот это я хочу видеть»** — если цель = **дожать и закрепить** Graphite Salon под Website Factory, убрать patchy legacy, единый governed CSS.

> **«Нет, это опять косметика»** — если цель = **ещё один визуальный скачок** поверх того, что уже на TEST, без structural/typography waves.

Детальное решение — [SITE-001-W3WF-01-VISUAL-IMPACT-DECISION-v1.md](SITE-001-W3WF-01-VISUAL-IMPACT-DECISION-v1.md).

---

## Related documents

| Document | Role |
|----------|------|
| [SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md](SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md) | Visual spec «Graphite Salon» |
| [SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md](SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md) | W3WF-01 phases A–J |
| [SITE-001-W3ATMOSPHERE-01-DECISION-v1.md](SITE-001-W3ATMOSPHERE-01-DECISION-v1.md) | Active TEST layer — current baseline |
| [SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md](SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md) | Pre-atmosphere preview (historical) |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W3WF-01 visual impact map; no site modifications |

*SITE-001 W3WF-01 Visual Impact Map v1 — documentation only; no implementation.*
