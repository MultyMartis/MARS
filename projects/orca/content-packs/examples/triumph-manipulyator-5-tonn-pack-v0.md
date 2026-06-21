# Landing Content Pack — Манипулятор 5 тонн (Triumph)

<!--
  DOCX EXPORT SOURCE — ORCA Content Pack v0
  This file is structured marketing/content semantics — NOT HTML.
-->

---
pack_id: triumph-manipulyator-5-tonn-v0
pack_version: v0.1
pack_type: capability
project_ref: triumph-manipulator-krasnodar
route_slug: 5-tonn.html
canonical_url: https://manipulator-triumph.ru/5-tonn.html
locale: ru-RU
artifact_state: approved
content_mode: MODE_1
semantic_lock: active
created_at: 2026-05-27
updated_at: 2026-05-27
author_operator: derived-from-approved-handoff
approval_gates:
  approved_for_factory: true
  approved_for_client_export: false
  approved_for_ads: false
  approved_for_launch: false
---

## Export metadata (for future DOCX)

| Field | Value |
|-------|--------|
| export_format | docx (planned) |
| semantic_lock_snapshot | **active** |
| MODE | **MODE 1 — SEMANTIC LOCK ACTIVE** |

## Page identity

| Field | Value |
|-------|--------|
| **Page name** | Манипулятор 5 тонн в Краснодаре |
| **Blueprint** | `05-capability-5-ton` → `landing-pages/05-capability-5-ton.md` |
| **PPC group** | `grp_fc01_5ton` — «01 — Манипулятор 5 тонн» |
| **Intent tier** | S — capability exact |
| **Page type** | PPC capability landing (search only; **not** SEO hub) |
| **Robots default** | `noindex,nofollow` until operator opens indexing |

---

## Positioning locks (global) 🔒

| Rule | Requirement |
|------|-------------|
| **One machine** | Одна конкретная машина с фиксированными параметрами |
| **No fleet framing** | Запрещено: «автопарк», «несколько машин», «5–10 т», «подберём из парка», «свой автопарк» |
| **Machine specs** | Борт **5 т** · Стрела **3 т** · Вылет **14 м** · Кузов **6.2 × 2.2 м** · Минимальный заказ **2 часа** |
| **Geo** | Краснодар и Краснодарский край |
| **PPC goal** | За 5–10 секунд: параметры → fit → можно ли заказать → стоимость → контакт |
| **Primary conversion** | Звонки и отправка формы |
| **Messengers** | Вторичный слой: **MAX** → **Telegram** → **WhatsApp** (именно в этом порядке) |
| **Filtering** | Явный блок «что не перевозим» |
| **Price honesty** | Без демпинга, без «от 1000 ₽», без фиктивной почасовой цены в hero. Стоимость — **по задаче**, до выезда |

---

## PPC continuity

| Ad field | Locked value |
|----------|----------------|
| Headline 1 | Манипулятор 5 тонн в Краснодаре |
| Headline 2 | Борт 5 т, стрела 3 т |
| Description | Манипулятор 5 т, вылет 14 м. Подача на объект. Расчёт по задаче. |
| Display path | `manip-5-tonn` |
| Callouts | Борт 5 т · Вылет 14 м · Без посредников |

**Primary intents:** манипулятор 5 тонн Краснодар · заказать манипулятор 5 тонн · манипулятор борт 5 тонн · манипулятор стрела 3 тонны · манипулятор 5 тонн цена

**Intent continuity rule 🔒:** Hero и схема борта/стрелы — **5 т**, стрела **3 т**, вылет **14 м**. Несовпадение с объявлением = блокер для запуска группы 01.

---

## SEO continuity

| Field | Value |
|-------|--------|
| `<title>` | Манипулятор 5 тонн в Краснодаре \| Триумф |
| meta description | Манипулятор 5 т: борт 5 т, стрела 3 т, вылет 14 м. Подача в Краснодаре и краю. Расчёт стоимости по задаче. |
| H1 | Манипулятор 5 тонн в Краснодаре |

---

# 01 HERO

| Contract | Value |
|----------|--------|
| section_id | `hero` |
| section_purpose | Мгновенное продолжение capability-интента с объявления: параметры, fit, первый контакт |
| ppc_continuity | H1 + bullets = 5 т, 3 т, 14 м как в объявлении |
| seo_continuity | Один H1 с «5 тонн» + «Краснодар» |

### Copy blocks 🔒

- **H1:** Манипулятор 5 тонн в Краснодаре
- **Subheadline:** Перевозка стройматериалов, бытовок, оборудования и тяжёлых грузов одной машиной. Подача по Краснодару и краю. Без посредников.
- **Capability bullets:**
  - Борт — 5 т
  - Стрела — 3 т
  - Вылет стрелы — 14 м
  - Кузов — 6.2 × 2.2 м
  - Минимальный заказ — 2 часа
- **Trust strip:** 4.9 ★ — Отзывы клиентов на Яндекс и Авито
- **Use-case chips:** Бытовки · ФБС · Кирпич · Арматура · Оборудование · Контейнеры
- **Qualification line:** Уточним тип груза, примерный вес и условия погрузки и разгрузки. Не работаем с эвакуацией легковых автомобилей.

### CTA

| Role | Text | Target |
|------|------|--------|
| Primary | Рассчитать стоимость | `#contacts` |
| Secondary | Позвонить | `tel:+79004658331` |
| Tertiary (header) | Уточнить подачу | `#contacts` |

### Proof elements

- Rating reference: 4.9 ★ — Яндекс и Авито (sources locked; no invented review text)

### Semantic locks 🔒

- H1 wording «5 тонн» + «Краснодар»
- Spec bullets 5 т / 3 т / 14 м / 6.2×2.2 / 2 часа
- Single-machine framing
- No hero-rate «от XXXX ₽/час»

### SAFE UNKNOWN

- Production NAP / hours — verify before launch (`tel:+79004658331` in handoff)

### Factory notes

- v4: `screen-01-hero.html`, `hero-proof` — replace «Свой автопарк» → «Одна машина» / «Понятные параметры»; remove «5–10 тонн»
- Фото одной машины 5 т; messengers в hero не выше телефона/формы

---

# 02 SPECS

| Contract | Value |
|----------|--------|
| section_id | `specs` |
| section_purpose | Core capability proof — «подходит ли техника?» за 3–5 секунд |
| ppc_continuity | Таблица параметров = callouts в объявлении |

### Copy blocks 🔒

- **Eyebrow:** Параметры техники
- **H2:** Параметры манипулятора 5 тонн
- **Lead:** Одна машина с понятными параметрами: перевозка, погрузка и подача грузов без подмены техники после звонка.

**Specs table:**

| Label | Value |
|--------|--------|
| Грузоподъёмность борта | 5 т |
| Грузоподъёмность стрелы | 3 т |
| Вылет стрелы | 14 м |
| Кузов | 6.2 × 2.2 м |
| Минимальный заказ | 2 часа |

- **Operational line:** Подходит для стройматериалов, бытовок, ФБС и ЖБИ, арматуры, оборудования, контейнеров и тяжёлых грузов в рамках параметров техники. Работаем по Краснодару и краю.

### CTA

| Role | Text |
|------|------|
| Primary | Рассчитать стоимость |
| Secondary | Уточнить подачу |

- **Microcopy:** Ответим: подходит ли техника · сколько примерно будет стоить · когда возможна подача

### Semantic locks 🔒

- Spec table values
- «Одна машина» / запрет «наша техника 5–10 т»

### Factory notes

- v4: `.machine-showcase` in `screen-02-prices.html`; nav «Парк техники» → «Параметры»; anchor `id="specs"`

---

# 03 ALLOWED TASKS

| Contract | Value |
|----------|--------|
| section_id | `allowed_tasks` |
| section_purpose | Связать параметры с задачей пользователя |
| ppc_continuity | Use-case continuation после specs |

### Copy blocks 🔒

- **H2:** Для каких задач подходит манипулятор
- **List:**
  - Перевозка бытовок
  - Доставка стройматериалов
  - Перевозка ФБС и ЖБИ
  - Доставка арматуры
  - Перевозка оборудования
  - Работа на строительных объектах
  - Разгрузка тяжёлых грузов в рамках 5 т / 3 т
- **Before dispatch:** Перед подачей уточняем параметры груза, адрес подачи, условия подъезда и особенности разгрузки.

### CTA

- Получить расчёт → `#contacts`

### Factory notes

- v4: `.machine-transport__card--allowed`; anchor `#tasks`

---

# 04 DENIED TASKS

| Contract | Value |
|----------|--------|
| section_id | `denied_tasks` |
| section_purpose | Qualification + anti-junk; снижение хаос-лидов |
| ppc_continuity | Фильтр нерелевантного трафика |

### Copy blocks 🔒

- **H3:** Что не перевозим
- **List:**
  - Легковые автомобили и эвакуация транспорта
  - Грузы сверх параметров машины (борт / стрела)
  - Негабарит вне возможностей техники
  - Мелкие бытовые перевозки вне профиля

### Semantic locks 🔒

- Evacuator / legkovye items
- Capability ceiling 5 т / 3 т

### Factory notes

- v4: `.machine-transport__card--denied` (red semantics)

---

# 05 ORDER FLOW

| Contract | Value |
|----------|--------|
| section_id | `order_flow` |
| section_purpose | Снять операционную неопределённость |
| ppc_continuity | Поддержка intent «заказать» |

### Copy blocks 🔒

- **H2:** Как заказать манипулятор 5 тонн
- **Steps:**
  1. **Свяжитесь с нами** — позвоните или оставьте имя и телефон в форме.
  2. **Опишите задачу** — тип груза, примерный вес, адрес подачи и разгрузки, нужна ли работа стрелой.
  3. **Согласуем условия** — подходит ли машина, ориентировочная стоимость и время подачи **до выезда**.
  4. **Подача на объект** — работа по согласованным параметрам, минимальный заказ 2 часа.

### CTA

| Role | Text |
|------|------|
| Primary | Позвонить |
| Secondary | Рассчитать стоимость |

### Semantic locks 🔒

- «Стоимость до выезда»
- Min order 2 часа

### Factory notes

- NEW partial `screen-02b-order-steps.html`; anchor `#order`; без таймера «5 минут» без подтверждения оператора

---

# 06 PRICING

| Contract | Value |
|----------|--------|
| section_id | `pricing` |
| section_purpose | Закрыть intent «манипулятор 5 тонн цена» без фейкового прайса |
| ppc_continuity | Честный price framing vs объявление «Расчёт по задаче» |

### Copy blocks 🔒

- **H2:** Стоимость манипулятора 5 тонн
- **Lead:** Точную цену рассчитываем по вашей задаче заранее — без скрытых доплат после выезда.
- **Factors:**
  - Тип и вес груза
  - Расстояние и маршрут
  - Время работы (минимум 2 часа)
  - Сложность погрузки и разгрузки
  - Необходимость работы стрелой
  - Условия подъезда на объект
- **Anchor line:** Стоимость зависит от задачи, а не от «самой низкой цены в интернете». Согласуем сумму до подачи техники.

### CTA

- Рассчитать стоимость · Уточнить подачу

### SAFE UNKNOWN ⚠

- **Почасовая ставка в рублях** — не публиковать до подтверждения оператором

### Semantic locks 🔒

- No invented hourly rate
- Min 2 часа in factors
- No tariff table «от … ₽/час» unless operator supplies approved figure

### Factory notes

- Remove v4 `hero__rate` XXXX; anchor `#pricing`

---

# 07 TRUST

| Contract | Value |
|----------|--------|
| section_id | `trust` |
| section_purpose | Практичное доверие — operational reliability |
| ppc_continuity | «Без посредников» + понятная техника |

### Copy blocks 🔒

- **Eyebrow:** Почему обращаются
- **H2:** Работаем с частными клиентами, строительными компаниями и бизнесом
- **Lead:** Согласовываем стоимость и время подачи заранее — на одной машине с понятными параметрами.

**Trust cards:**

1. **Конкретная техника** — Манипулятор 5 т / стрела 3 т. Без подмены машины после звонка.
2. **Стоимость заранее** — Обсуждаем маршрут, груз и условия до выезда.
3. **Краснодар и край** — Подберём ближайшее возможное время подачи по маршруту.
4. **Наличный и безналичный расчёт** — Для частных клиентов и организаций.

**Reviews block:**

- **H2:** Отзывы клиентов
- **Subtitle:** Отзывы с Яндекс и Авито о работе техники и перевозке грузов.
- **Rating strip:** 4.9 ★ — На основе отзывов клиентов в Яндекс и Авито
- **CTA:** Читать отзывы клиентов

### Semantic locks 🔒

- 4.9 ★ + Яндекс/Авито pairing
- No fleet/autopark in trust cards
- No «10+ лет», «1000+ заказов», «от 30 минут» without verification

### SAFE UNKNOWN ⚠

- Review widget URLs until connected
- Placeholder review cards OK; **do not invent** names/dates/quotes

### Factory notes

- v4: `screen-03-trust-reviews.html`; remove 2ГИС if unconfirmed; anchor `#reviews`

---

# 08 B2B

| Contract | Value |
|----------|--------|
| section_id | `b2b` |
| section_purpose | B2B/payment intent без отдельной страницы |
| ppc_continuity | Поддержка org / bezнал queries |

### Copy blocks 🔒

- **H3:** Для организаций и юрлиц
- **Body:** Работаем с безналичной оплатой и заявками от организаций. Условия и документы уточняем при расчёте задачи.
- **Bullets:**
  - Безналичный расчёт
  - Заявки от организаций
  - Согласование стоимости до выезда

### SAFE UNKNOWN ⚠

- НДС и закрывающие документы — формулировку «с НДС» только после подтверждения оператором

### Semantic locks 🔒

- No «собственный автопарк» in B2B facts

### CTA

- Рассчитать стоимость

---

# 09 FAQ

| Contract | Value |
|----------|--------|
| section_id | `faq` |
| section_purpose | Objection removal; price + capability + geo |
| ppc_continuity | Answers не противоречат specs и denied tasks |

### FAQ pairs 🔒

| # | Question | Answer (summary) |
|---|----------|----------------|
| 1 | Какие грузы можно перевозить манипулятором 5 тонн? | Стройматериалы, бытовки, оборудование, металлоконструкции, контейнеры, тяжёлые грузы **в рамках 5 т / 3 т** |
| 2 | Как понять, подходит ли техника? | Сообщите тип груза, вес, размеры, адрес — подскажем fit |
| 3 | Как рассчитывается стоимость? | Тип груза, расстояние, время (от 2 часов), сложность погрузки/разгрузки, работа стрелой |
| 4 | Работаете ли по Краснодарскому краю? | Да: Краснодар, пригороды, край — подача и цена по маршруту |
| 5 | Можно ли оплатить по безналу? | Да: наличный, безнал, заявки от организаций |
| 6 | Что не перевозите? | Эвакуация легковых; грузы вне параметров; нерелевантные бытовые перевозки |
| 7 | Как быстро можно заказать? | Зависит от загрузки и адреса — свяжитесь, уточним ближайшее время |

### Semantic locks 🔒

- No second machine or fleet in answers
- Price FAQ: no fixed ₽/hour without operator data

### Factory notes

- v4: `screen-04-faq.html`; anchor `#faq`

---

# 10 FINAL CTA

| Contract | Value |
|----------|--------|
| section_id | `final_cta` |
| section_purpose | Final conversion; uncertainty removal |
| ppc_continuity | Repeat primary conversion path |

### Copy blocks 🔒

- **H2:** Нужно уточнить стоимость или возможность подачи?
- **Subtitle:** Свяжитесь с нами — подскажем: подходит ли техника · возможна ли подача · ориентировочная стоимость работы.
- **Form title:** Оставьте имя и телефон
- **Fields:** Имя · Телефон (**only**)
- **Primary button:** Рассчитать стоимость
- **Secondary:** Позвонить
- **Small text:** Перезвоним и уточним: тип груза · адрес подачи · возможность работы · ориентировочную стоимость.

**Messenger row (order locked 🔒):** MAX → Telegram → WhatsApp

**Phone:** `tel:+79004658331`

### Semantic locks 🔒

- Form: name + phone only
- Messenger order
- Primary = form/call, not messenger

### SAFE UNKNOWN ⚠

- Form `action` endpoint
- Production NAP / hours «7:00–22:00» until operator sign-off

### Factory notes

- v4: `final-contact-cta.html`; MAX icon first; anchor `#contacts`

---

## Header / navigation (implementation notes)

| Element | Value |
|---------|--------|
| Header CTA | Уточнить подачу → `#contacts` |
| Nav anchors | `#specs` Параметры · `#tasks` Задачи · `#order` Как заказать · `#pricing` Стоимость · `#reviews` Отзывы · `#faq` FAQ · `#contacts` Контакты |

---

## Source artifacts

| Source | Path |
|--------|------|
| Production handoff | `projects/orca/ppc/triumph-manipulator/handoff/triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md` |
| Blueprint | `projects/orca/ppc/triumph-manipulator/landing-pages/05-capability-5-ton.md` |
| Campaign instance | `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json` |
| Factory workspace | `workspaces/triumph-manipulator-landing-v4/` |

---

## Operator sign-off (pack-level)

| Gate | Status | Notes |
|------|--------|-------|
| approved_for_factory | **yes** (per existing handoff / project approvals) | See `projects/orca/projects/triumph-manipulator-krasnodar/approvals/` |
| approved_for_client_export | no | DOCX exporter not built |
| approved_for_ads | no | Pending live URL QA |
| approved_for_launch | no | Pending deploy + Commander checklist |

---

*End of pack — Triumph «Манипулятор 5 тонн» v0. Example for ORCA Content Export Layer; semantics from approved handoff — no invented fleet, prices, or statistics.*
