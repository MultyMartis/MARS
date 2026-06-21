# REPORT — M9.8.9-03B COMMERCIAL TRUST BLOCK REDESIGN

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01`  
**Task:** M9.8.9-03B — UX + IA + content + wireframe (no implementation)  
**Date:** 2026-06-19  
**Mode:** Research and design only — **no** Twig · **no** CSS · **no** JS · **no** deploy · **no** FTP · **no** commit

**PRE-TASK RULE:** Knowledge Map + Stable Checkpoint + M9.8.9-03 forensic/implementation reports + site-passport — read and applied.

**Relation to M9.8.9-03:** Реализация Variant B (trust strip + split) на category PLP **считается технически успешной, но UX-неудачной**. Этот документ проектирует **следующую версию** блока с нуля по смыслу, а не полировку текущей вёрстки.

---

## 1. Current Block Problems

### 1.1 Что есть на live сейчас (M9.8.9-03)

На category PLP после сетки товаров рендерится `blockcommercialtrust.twig`:

```
[ strip: «Сертифицированная продукция» + 2 мини-превью + «Все сертификаты» ]
[ split 55/45: H2 «Дилерам и оптовикам» + 5 bullets | форма dialog=7 ]
```

**Live-пример:** https://zpm.new-site.space/stoly-serii-premium/stoly/

### 1.2 Почему блок не работает (UX + commercial)

| # | Проблема | Симптом | Корневая причина |
|---|----------|---------|------------------|
| 1 | **Потерян смысл сертификатов** | Полоска с двумя мелкими превью не читается как доказательство качества | Сертификаты сведены к декоративным чипам без контекста (какой документ, зачем, для кого) |
| 2 | **Выглядит пустым** | Много воздуха, слабая визуальная плотность смысла | Нет якоря «производитель ЗПМ», нет фото/бренда/цифр; strip и split визually disconnected |
| 3 | **Случайная форма внизу** | Форма без заголовка ценности, без обещания результата | H2 «Дилерам» относится к левой колонке; форма — анонимная карточка справа |
| 4 | **Не усиливает доверие** | Bullets generic («работаем по РФ», «гарантия») — те же, что на homepage advantages | Нет дифференциации OEM, нет «Сделано в России», нет социального proof |
| 5 | **Не усиливает конверсию** | Нет мотивации оставить заявку *сейчас*, на этой странице | Нет привязки к просмотренной категории, нет SLA ответа, нет «что получите после заявки» |
| 6 | **Неверная аудитория по умолчанию** | Заголовок «Дилерам и оптовикам» отсекает снабженца, владельца, проектировщика | Блок позиционируется только под дилера, хотя на PLP приходят все B2B-персоны |
| 7 | **Разрыв с redesign-стратегией** | BZPM Architecture (W2-F-07): full form + certs = wallpaper на deep PLP | M9.8.9-03 сжал блок, но не изменил **роль** блока в decision chain |
| 8 | **Не использует assets сайта** | На homepage есть advantages grid, «Сделано в России», about teaser — на PLP не задействованы | `blockadvantagestop/bottom` грузятся в controller, но **не выводятся** на category PLP |

### 1.3 Что M9.8.9-03 сделал правильно (сохранить в v2)

- Один `<section>` вместо двух — правильное направление IA
- Убран Swiper на PLP — меньше шума
- Fancybox сохранён — нужен для тендеров/закупок
- Форма `dialog=7` и endpoint не тронуты — backend-safe
- Padding снижен vs legacy 120px — верно по высоте

**Вывод:** проблема не в «компактности», а в **отсутствии коммерческой архитектуры блока** — trust + manufacturer + CTA + lead capture должны быть спроектированы как единый decision-stage, а не как сжатый footer.

---

## 2. User Intent Analysis

### 2.1 Контекст scroll-position

На category PLP пользователь **уже прошёл этап orientation** (H1, chips/filters) и **evaluation** (карточки, цены, наличие, сроки). Блок появляется в момент:

> «Я нашёл подходящие модели / сравниваю серии — можно ли доверять производителю и как быстро получить цену/комплект/партнёрские условия?»

Это **decision-stage**, не awareness-stage (как homepage hero).

### 2.2 Персоны и их вопросы

| Персона | Доля intent на PLP (оценка) | Главный вопрос перед заявкой | Что должно быть в блоке |
|---------|----------------------------|------------------------------|-------------------------|
| **Снабженец** | Высокая | «Производитель надёжный? Есть наличие/срок? Как получить КП на N позиций?» | OEM-proof, срок ответа, форма «Запросить КП» |
| **Производственник / технолог** | Средняя | «Сертификация, гарантия, можно ли нестандарт?» | Сертификаты readable, гарантия, «изготовление на заказ» |
| **Владелец кафе / УК** | Средняя | «Кто вы? Почему не перекуп? Сколько ждать ответа?» | Производитель РФ, простой CTA «Поможем подобрать комплект» |
| **Проектировщик** | Ниже, но high-value | «Документы для проекта/тендера? Серии стандартизированы?» | Lightbox certs, ссылка на документацию, контакт эксперта |
| **Дилер / оптовик** | Целевая, но не единственная | «Прайс, условия, стабильность поставок» | Явная ветка «Стать партнёром» + форма или ссылка `/dealers` |

### 2.3 Что реально важно клиенту ЗПМ (evidence-based)

Из homepage, about, advantages, news (live TEST 2026-06-19) и BZPM redesign docs:

| Сигнал | Источник | Приоритет на PLP |
|--------|----------|------------------|
| **Производитель OEM** (не перекуп) | About, homepage hero | **P1** |
| **«Сделано в России»** | News 24.03.2026, header badge `made_in_russia.svg` | **P1** |
| **Сертифицированная продукция** | Certificates block, news | **P1** — но с **readable** proof |
| **Гарантия от 1 года / от производителя** | Advantages top | **P2** |
| **Доставка по РФ, отгрузка от 1 дня** | Advantages bottom | **P2** |
| **Изготовление на заказ / проектирование** | Homepage branch «Для пищевых производств» | **P2** для production-intent |
| **Прайс и КП после заявки** | Dealers copy (homepage) | **P2** — явное обещание |
| **Помощь в подборе** | Bullets, consultative CTA (CV-02) | **P2** |
| **Крупное производство / масштаб** | Advantages | **P3** — только если подкреплено фактом |

**SAFE UNKNOWN:** точный SLA ответа на заявку; число лет на рынке; объём производства — требует operator confirmation перед copy lock.

### 2.4 Что показать *перед* заявкой (минимальный trust stack)

1. **Кто:** ЗПМ — завод, Россия (1 строка + badge)
2. **Почему верить:** 1–2 сертификата с подписью типа документа + lightbox
3. **Что получит после отправки:** «КП / прайс / консультация» — конкретно
4. **Когда:** срок ответа (operator-confirmed)
5. **Действие:** форма с заголовком результата, не «Отправить» в вакууме

---

## 3. Variant A — «Производитель + доказательства» (Manufacturer Proof Panel)

### Смысл

Блок продаёт **ЗПМ как OEM-производителя**, а не «форму дилерам». Сертификаты — **доказательный слой** внутри панели производителя, а не отдельная полоска.

### Информационная структура

```
section.zpm-trust-panel
└── .container
    └── .zpm-trust-panel__grid (3 zones)
        ├── ZONE-A: Manufacturer identity (~30%)
        │   ├── Eyebrow: «Производитель · Россия»
        │   ├── H2: «Завод пищевого машиностроения»
        │   ├── Badge: Сделано в России (SVG)
        │   └── Micro: «Нейтральное оборудование для общепита и производств»
        ├── ZONE-B: Proof stack (~35%)
        │   ├── Proof card: Сертификат качества (thumb + label + zoom)
        │   ├── Proof card: Сделано в России (thumb + label + zoom)
        │   ├── Proof row: Гарантия · Доставка РФ · На заказ
        │   └── Link: «Все сертификаты и документы»
        └── ZONE-C: Action (~35%)
            ├── H3: «Получить КП и условия поставки»
            ├── Promise: «Ответим в течение N раб. дней» (*)
            ├── Benefit chips: Прайс · Подбор · Опт
            └── Compact form (name, phone, email, intent select, submit)
```

(*) Operator to confirm SLA.

### CTA логика

- Заголовок формы = **обещание результата** («Получить КП»), не «Дилерам»
- Intent select: «Коммерческое предложение» / «Стать партнёром» / «Подбор комплекта» — маршрутизация лида без отдельных страниц
- Человек оставляет заявку, потому что уже выбрал категорию и видит **производителя + документы + конкретный outcome**

### Плюсы

- Восстанавливает смысл сертификатов (labeled proof cards)
- Чёткий OEM-narrative — отличие от маркетплейсов
- Одна viewport-история: кто → доказательства → действие
- Подходит всем персонам через intent select

### Минусы

- Три колонки тесны на 1024–1280
- Требует operator copy + возможно 1 production photo
- Intent select — minor backend/CRM mapping (SAFE UNKNOWN)

### Mobile

1. Manufacturer header (badge + H2)
2. Proof cards — horizontal scroll, 2 visible
3. Promise + form full width

---

## 4. Variant B — «Коммерческая полоса решения» (Decision Band)

### Смысл

Блок = **финальный коммерческий акт** после каталога: «Вы смотрели {категория} — поможем закрыть закупку». Единая full-width band с фоном, визually отделённая от PLP grid.

### Информационная структура

```
section.zpm-decision-band
└── .container
    ├── ROW-1: Context headline
    │   ├── H2: «Нужна консультация по {category_name}?» (*)
    │   └── Sub: «Подберём модели, рассчитаем комплект, отправим КП»
    ├── ROW-2: Trust metrics (4 inline stats/icons)
    │   ├── Производство РФ
    │   ├── Сертификация
    │   ├── Гарантия N лет
    │   └── Отгрузка от 1 дня
    ├── ROW-3: Split
    │   ├── Left: Cert preview (1 featured cert large + link all)
    │   └── Right: Form card «Запросить расчёт»
    └── ROW-4: Secondary paths
        ├── Link: Стать дилером → /dealers
        └── Link: Все сертификаты → lightbox / page
```

(*) Dynamic `{category_name}` from controller — e.g. «столам», «моечным ваннам».

### CTA логика

- Контекст категории снижает ощущение «случайной формы»
- Primary CTA: «Запросить расчёт» / «Получить КП»
- Secondary: дилерский путь — link, не конкурирует с primary
- Конверсия через **релевантность моменту** (post-grid) + **конкретный outcome**

### Плюсы

- Сильнейший anti-«пустота» — band с фоном читается как намеренный блок
- Category-aware copy — UX win для снабженца и владельца
- Featured cert (крупнее) восстанавливает вес документов
- Хорошо стыкуется с BZPM CV-02 (consultative CTA at decision point)

### Минусы

- Dynamic copy — Twig/controller work
- Band может казаться «рекламой» если перегрузить stats без proof
- Выше CSS-scope (новый visual tier, не reuse strip)

### Mobile

1. H2 + sub
2. 2×2 stats grid
3. Featured cert
4. Form
5. Secondary links row

---

## 5. Variant C — «Две дорожки намерения» (Dual-Lane Intent)

### Смысл

Блок признаёт **два разных commercial intent** на PLP и не заставляет всех в одну dealer-форму:

- **Lane A — Закупка / проект:** КП, подбор, документы для тендера
- **Lane B — Партнёрство:** дилер, опт, прайс-лист

### Информационная структура

```
section.zpm-trust-dual
└── .container
    ├── HEADER: «Работаем с производителя напрямую»
    │   └── Trust inline: [RU badge] [cert icon ×2] [гарантия]
    ├── LANES (2 col desktop)
    │   ├── LANE-A: «Для закупки и проекта»
    │   │   ├── Bullets: КП · Подбор · Сертификаты для тендера
    │   │   ├── Mini form: name, phone, email, message (short)
    │   │   └── CTA: «Получить КП»
    │   └── LANE-B: «Для дилеров и опта»
    │       ├── Bullets: Прайс · Стабильные поставки · Маркeting support (*)
    │       ├── CTA primary: «Стать партнёром» → /dealers
    │       └── CTA secondary: «Оставить заявку» → expand inline form OR same form dialog=7
    └── FOOTER: «Все сертификаты» + lightbox group
```

(*) Marketing support — SAFE UNKNOWN, confirm with operator.

### CTA логика

- Снабженец/проектировщик не отталкивается заголовком «Дилерам»
- Дилер идёт явным путём — выше quality of dealer leads
- Две формы **не рекомендуются** — одна форма, два entry copy blocks; lane B может вести на `/dealers` без дубля form

**Refined:** Lane B = button to `/dealers`; Lane A = form only — avoids dual-form JS issues.

### Плюсы

- Лучшее persona fit без отдельных landing pages
- Сертификаты в header trust — компактно, не доминируют
- Снижает cognitive mismatch «я не дилер, зачем форма»

### Минусы

- Две колонки + header = риск высоты на mobile
- Lane B без inline form может снизить dealer conversion vs today
- Сложнее QA matrix (hub vs leaf categories)

### Mobile

1. Header + trust inline
2. Lane A (form) — **first** (conversion priority)
3. Lane B card — button to `/dealers`
4. Footer cert link

---

## 6. Certificate Strategy

Ответы на обязательные вопросы для **новой** версии блока (не legacy homepage slider).

| # | Вопрос | Рекомендация | Обоснование |
|---|--------|--------------|-------------|
| 1 | **Один сертификат или несколько?** | **2 featured + группа в lightbox** | Live assets: минимум 2 unique (`certificat_00`, `certificat_01`); news подтверждает «Сделано в России» как отдельный proof. Показывать **оба типа** с подписью: «Сертификат качества» / «Сделано в России». |
| 2 | **Нужен ли слайдер?** | **Нет на category PLP** | W2-F-07, M9.8.9-03 forensic: slider = gallery noise. Если unique certs > 3 — static row + overflow link, не Swiper. Homepage/katalog may keep slider until unified pass. |
| 3 | **Нужен ли lightbox?** | **Да, обязательно** | Tender/procurement persona must read full document. Fancybox already on site (M9.8.2 patterns). Min touch target 44px on thumb. |
| 4 | **Нужна ли ссылка «Все сертификаты»?** | **Да** | Opens fancybox group **all** certs (+ future PDFs). Label: «Все сертификаты и документы». Avoid duplicate href bug (current PLP: link opens only cert_00). |
| 5 | **Где сертификат в новой структуре?** | **Inside manufacturer/proof zone — not isolated top strip** | Strip-only placement (M9.8.9-03) detached certs from narrative. Recommended: certs adjacent to OEM identity or in proof stack **below** headline, **above** form promise. |

### Certificate content rules (implementation phase)

- Each thumb: **document type label** under image (not just «Сертификат 1»)
- Alt text: specific document name
- No duplicate slides in lightbox group (fix legacy 4-link/2-file issue)
- Operator supplies final inventory before deploy

---

## 7. Recommended Concept

**Primary recommendation: Variant B «Decision Band»** with certificate rules from §6 and manufacturer signals from Variant A Zone-A (badge + OEM one-liner).

### Почему B, а не A или C

| Критерий | A | B | C |
|----------|---|---|---|
| Устраняет «пустоту» | Средне | **Высоко** — band + headline | Средне |
| Восстанавливает смысл certs | **Высоко** | Высоко (featured cert) | Средне (inline icons) |
| Anti «случайная форма» | Средне | **Высоко** — category context | Высоко |
| Persona coverage | Высоко (intent select) | **Высоко** | **Highest** — но сложнее |
| Implementation risk | Medium | **Low–medium** | Medium–high |
| Alignment BZPM CV-02 | Good | **Best** | Good |

**Hybrid specification (recommended v2):**

- **Visual tier:** full-width decision band (subtle bg, border-top separator from PLP)
- **Headline:** category-aware consultative (`{category_name}` dative)
- **Trust row:** 4 metrics + RU badge (from homepage advantages vocabulary)
- **Proof:** 1 featured cert (larger) + 1 secondary thumb + «Все документы»
- **Form card:** titled «Запросить КП и условия» + SLA chip + fields (existing `dialog=7`)
- **Secondary:** text link «Стать партнёром» → `/dealers` (not competing button)

**Defer Variant C dual-lane** if operator confirms single-form policy; revisit if analytics show low non-dealer submit rate.

---

## 8. Desktop Wireframe (Recommended)

**Viewport:** ~1440px content width, container 50px padding.

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  PLP PRODUCT GRID (above — unchanged)                                          │
│  ... pagination ...                                                            │
├──────────────────────────────────────────────────────────────────────────────┤
│ ░░░░░░░░░░░░░░░░░ DECISION BAND (bg: light gray / brand tint) ░░░░░░░░░░░░░░░ │
│                                                                               │
│  Нужна консультация по столам?                                                │
│  Подберём модели, рассчитаем комплект, отправим коммерческое предложение      │
│                                                                               │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐                             │
│  │ [RU]    │ │ Серти-  │ │ Гарантия│ │ Отгрузка│   ← icon + 1-line each      │
│  │ Произв. │ │ фикация │ │ от 1 г. │ │ от 1 дн.│                             │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘                             │
│                                                                               │
│  ┌────────────────────────────┐  ┌─────────────────────────────────────────┐ │
│  │  PROOF                     │  │  Запросить КП и условия поставки        │ │
│  │  ┌──────────┐ ┌────┐       │  │  ┌───────────────────────────────────┐  │ │
│  │  │          │ │thumb│      │  │  │ Ответим в течение 1 раб. дня (*)  │  │ │
│  │  │ FEATURED │ │ 2  │      │  │  └───────────────────────────────────┘  │ │
│  │  │  CERT    │ └────┘       │  │  Имя*          [________________]       │ │
│  │  │  + label │              │  │  Телефон*      [________________]       │ │
│  │  └──────────┘              │  │  Email*        [________________]       │ │
│  │  Все сертификаты и документы│  │  Вопрос        [________________]       │ │
│  │  (link → fancybox group)   │  │  [ ] согласие                          │ │
│  └────────────────────────────┘  │  [ Отправить заявку ]                  │ │
│                                   │  Стать партнёром → /dealers           │ │
│                                   └─────────────────────────────────────────┘ │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
├──────────────────────────────────────────────────────────────────────────────┤
│  SEO TEXT (if any) · FOOTER                                                   │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Estimated band height:** ~520–640px (vs ~400px current merged block but **higher information density**).

---

## 9. Mobile Wireframe (Recommended)

**Viewport:** ≤1024px, single column.

```text
┌─────────────────────────────┐
│ ... PLP grid + pagination ...│
├─────────────────────────────┤
│ ░ DECISION BAND ░           │
│                             │
│ Нужна консультация          │
│ по столам?                  │
│ Подберём модели и           │
│ отправим КП                 │
│                             │
│ ┌──────────┐ ┌──────────┐   │
│ │ RU       │ │ Сертиф.  │   │  2×2 metrics
│ │ Произв.  │ │          │   │
│ └──────────┘ └──────────┘   │
│ ┌──────────┐ ┌──────────┐   │
│ │ Гарантия │ │ Отгрузка │   │
│ └──────────┘ └──────────┘   │
│                             │
│ ┌─────────────────────────┐ │
│ │   FEATURED CERT         │ │
│ │   + label               │ │
│ └─────────────────────────┘ │
│ ← thumb 2 →  scroll         │
│ Все сертификаты и документы │
│                             │
│ ┌─────────────────────────┐ │
│ │ Запросить КП            │ │
│ │ SLA chip                │ │
│ │ [ form fields ]         │ │
│ │ [ Submit ]              │ │
│ │ Стать партнёром →       │ │
│ └─────────────────────────┘ │
├─────────────────────────────┤
│ footer                      │
└─────────────────────────────┘
```

**Stack order rationale:** context → trust metrics → proof → form (conversion last but motivated).

---

## 10. Future Implementation Scope

**Charter:** M9.8.9-03C or follow-up pass — **only after operator approval** of this redesign doc.

### In scope (category PLP first)

| Work package | Files (expected) | Effort |
|--------------|------------------|--------|
| Live FTP capture | `blockcommercialtrust.twig`, `category.twig`, `category.php`, `style.css` | 0.5 h |
| Replace template structure | `sections/blockcommercialtrust.twig` (rewrite) | 2–3 h |
| Category name injection | `category.php` → pass `$category_name` / dative form | 0.5–1 h |
| CSS: decision band tier | `style.css` new block; remove/replace M9.8.9-03 strip styles | 2–3 h |
| Certificate markup fix | unique fancybox group; labels; no duplicate links | 0.5 h |
| Copy pass | Operator HITL — SLA, guarantee term, stats | external |
| JS | Scope dealer form to `[data-commercial-trust]`; optional `querySelectorAll` | 0.5–1 h |
| QA | hub + leaf PLP, fancybox, form submit, 390/1440 | 1–2 h |

**Total estimate:** ~8–12 h (1–2 deploy passes).

### Out of scope (separate charter)

- Homepage / `/katalog` unified commercial block (advantages + certs + dealers)
- Variant C dual-lane with separate forms
- Dedicated `/certificates` page (optional future)
- PDP commercial micro-strip (CV-01 — separate task)
- Leaf-page suppression (BZPM W2-F-07 phase 2)
- Backend CRM routing for intent select

### Rollback

Same as M9.8.9-03: restore `backups/category.*.pre-m9.8.9-03*` + pre-03B capture after new backup `.pre-m9.8.9-03b`.

### Acceptance criteria (operator QA)

1. Block reads as **intentional commercial stage**, not footer form
2. User can identify **manufacturer + certification** without opening lightbox
3. Lightbox opens **all unique** certificates from PLP
4. Form headline states **outcome** (КП/условия), not only «Дилерам»
5. Category headline matches current PLP category (manual check 3 URLs)
6. Mobile: form reachable within **≤1.5 screens** after pagination
7. No regression: `dialog=7`, single form instance, wishlist/filter unaffected

---

## Evidence index

| Artifact | Path |
|----------|------|
| M9.8.9-03 forensic | [SITE-002-M9.8.9-03-CERTIFICATES-DEALERS-MERGE-FORENSIC-AND-DESIGN.md](SITE-002-M9.8.9-03-CERTIFICATES-DEALERS-MERGE-FORENSIC-AND-DESIGN.md) |
| M9.8.9-03 implementation | [SITE-002-M9.8.9-03-CERTIFICATES-DEALERS-MERGE-IMPLEMENTATION.md](SITE-002-M9.8.9-03-CERTIFICATES-DEALERS-MERGE-IMPLEMENTATION.md) |
| Current twig (deployed) | [m9.8.9-03-work/blockcommercialtrust.twig](m9.8.9-03-work/blockcommercialtrust.twig) |
| BZPM commercial architecture | `projects/website-factory/execution-cases/bzpm-catalog-redesign/BZPM-REDESIGN-ARCHITECTURE-v1.md` §F |
| Knowledge Map PRE-TASK | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) §13 |
| Live PLP | https://zpm.new-site.space/stoly-serii-premium/stoly/ |
| Live homepage advantages | https://zpm.new-site.space/ |

---

## UNKNOWN

| Item | What would verify |
|------|-------------------|
| SLA ответа на заявку | Operator / CRM policy |
| Точное число unique сертификатов на FTP | `/assets/img/certificates/` listing |
| Dative/category headline copy rules | Operator editorial + Twig helper |
| «Маркeting support» for dealers | Sales team confirmation |
| Analytics: current form submit rate by persona | **No analytics product claimed** — operator data |

---

## Git status (this task)

| Item | Value |
|------|-------|
| Code changes | **None** |
| Deploy | **None** |
| Report added | `reports/SITE-002-M9.8.9-03B-COMMERCIAL-TRUST-BLOCK-REDESIGN.md` |
| Commit | **Not performed** (per charter) |
| Push | **Not performed** (per charter) |

---

*Design pass complete. Awaiting operator approval of recommended Variant B (Decision Band) before M9.8.9-03C implementation charter.*
