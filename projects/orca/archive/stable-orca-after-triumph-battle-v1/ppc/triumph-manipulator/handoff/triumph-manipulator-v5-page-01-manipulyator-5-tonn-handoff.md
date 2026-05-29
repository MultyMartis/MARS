# Triumph Manipulator v5 — Page 01 Handoff

**Document ID:** `triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff`  
**Status:** Production handoff (copy + structure locked; HTML/SCSS not in scope)  
**Date:** 2026-05-21  
**Lane:** A — Frontend Production / Website Factory Handoff

---

## 1. Page identity

| Field | Value |
|--------|--------|
| **Page name (human)** | Манипулятор 5 тонн в Краснодаре |
| **URL (canonical)** | `https://manipulator-triumph.ru/manipulyator-5-tonn/` |
| **Blueprint (ORCA)** | `05-capability-5-ton` → `landing-pages/05-capability-5-ton.md` |
| **Direct group** | `grp_fc01_5ton` — «01 — Манипулятор 5 тонн» (Full Cycle v1.1) |
| **Intent tier** | S — capability exact |
| **Page type** | PPC capability landing (search only; **not** SEO hub) |
| **Robots default** | `noindex,nofollow` until operator opens indexing |

### Primary PPC intents (must continue from ad click)

- манипулятор 5 тонн Краснодар
- заказать манипулятор 5 тонн
- манипулятор борт 5 тонн
- манипулятор стрела 3 тонны
- манипулятор 5 тонн цена

### Ad continuity (from `triumph-s-tier-draft-v1.json`)

| Ad field | Locked value |
|----------|----------------|
| Headline 1 | Манипулятор 5 тонн в Краснодаре |
| Headline 2 | Борт 5 т, стрела 3 т |
| Description | Манипулятор 5 т, вылет 14 м. Подача на объект. Расчёт по задаче. |
| Display path | `manip-5-tonn` |
| Callouts | Борт 5 т · Вылет 14 м · Без посредников |

**Intent continuity rule:** Hero и схема борта/стрелы — **5 т**, стрела **3 т**, вылет **14 м**. Несовпадение с объявлением = блокер для запуска группы 01.

---

## 2. Positioning locks (global — do not change)

| Rule | Requirement |
|------|-------------|
| **One machine** | Одна конкретная машина с фиксированными параметрами. |
| **No fleet framing** | Запрещено: «автопарк», «несколько машин», «5–10 т», «подберём технику из парка», «свой автопарк». |
| **Machine specs** | Борт **5&nbsp;т** · Стрела **3&nbsp;т** · Вылет **14&nbsp;м** · Кузов **6.2 × 2.2&nbsp;м** · Минимальный заказ **2&nbsp;часа**. |
| **Geo** | Краснодар и&nbsp;Краснодарский край (без выдуманных городов вне политики). |
| **PPC goal** | За 5–10 секунд: параметры → fit → можно ли заказать → как узнать стоимость → как связаться. |
| **Primary conversion (Direct)** | Звонки и отправка формы. |
| **Messengers** | Вторичный слой: **MAX** → **Telegram** → **WhatsApp** (именно в этом порядке). |
| **Filtering** | Явный блок «что не перевозим» (эвакуация легковых, грузы вне параметров). |
| **Price honesty** | Без демпинга, без «от 1000 ₽», без фиктивной почасовой цены в hero. Стоимость — **по задаче**, до выезда. |

---

## 3. Visual / codebase base (v4 — do not redesign)

**Primary implementation workspace:** `workspaces/triumph-manipulator-landing-v4/`

| Handoff section | v4 partial / system | Action |
|-----------------|---------------------|--------|
| Shell, header, tokens | `src/partials/layout/header.html`, `src/scss/utils/_tokens.scss` | Reuse layout; replace copy and nav anchors |
| 1 Hero | `screen-01-hero.html` + `hero-proof` strip | Replace H1, bullets, CTA; remove fleet/5–10т/XXXX price |
| 2 Machine specs | `screen-02-prices.html` → `.machine-showcase` | Keep structure; lock spec values |
| 3 Tasks fit | `screen-02-prices.html` → `.machine-transport--allowed` | Align list to capability pack |
| 4 How order works | **NEW block** (no v4 partial) | Insert between screen-02 and trust; match v4 section rhythm |
| 5 Pricing factors | **NEW block** or lower part of screen-02 | No fake tariff table |
| 6 Trust + reviews | `screen-03-trust-reviews.html` | Rewrite cards (one machine); reviews Яндекс + Авито only |
| 7 B2B / payment | Trust cards + `final-contact-cta` facts | No autopark line in facts |
| 8 FAQ | `screen-04-faq.html` | Replace Q&A set per handoff |
| 9 Final CTA | `final-contact-cta.html` | Form: имя + телефон only; messenger order MAX→TG→WA |

**Do not:** новая дизайн-система, смена сетки V1/V4, пересборка SCSS-токенов без задачи на визуал.

**Asset candidates:** `src/img/reconstruction/v1-02-manipulator-5t.png`, `v2-02-machine.png` — hero/showcase; `src/img/social/MAX-ico.svg` first in messenger rows.

**Website Factory reference:** `projects/mars-website-factory/reference-cases/triumph-manipulator-landing/page-blueprint-v0.md` (registry shape only; this handoff overrides section order for capability page).

**Legacy project passport:** `projects/triumph-manipulator-landing/project-passport.md` — workspace v1; **v4 workspace is authoritative** for this page build.

---

## 4. Meta / document head

| Field | Value |
|--------|--------|
| `<title>` | Манипулятор 5&nbsp;тонн в&nbsp;Краснодаре \| Триумф |
| `meta description` | Манипулятор 5&nbsp;т: борт 5&nbsp;т, стрела 3&nbsp;т, вылет 14&nbsp;м. Подача в&nbsp;Краснодаре и&nbsp;краю. Расчёт стоимости по&nbsp;задаче. |
| `robots` | `noindex,nofollow` (PPC landing default) |
| `H1` (one per page) | См. §5.1 — must include «5 тонн» + «Краснодар» |

---

## 5. Section-by-section handoff

### 5.1 Hero

| | |
|--|--|
| **Purpose** | Мгновенное продолжение capability-интента с объявления: параметры, fit, первый контакт. |
| **v4 base** | `screen-01-hero.html`, `hero-proof` aside |

**Final Russian copy**

- **H1:** Манипулятор 5&nbsp;тонн в&nbsp;Краснодаре
- **Subheadline:** Перевозка стройматериалов, бытовок, оборудования и&nbsp;тяжёлых грузов одной машиной. Подача по&nbsp;Краснодару и&nbsp;краю. Без посредников.
- **Capability bullets (visible immediately):**
  - Борт — 5&nbsp;т
  - Стрела — 3&nbsp;т
  - Вылет стрелы — 14&nbsp;м
  - Кузов — 6.2 × 2.2&nbsp;м
  - Минимальный заказ — 2&nbsp;часа
- **Trust strip:** 4.9&nbsp;★ — Отзывы клиентов на&nbsp;Яндекс и&nbsp;Авито
- **Use-case chips:** Бытовки · ФБС · Кирпич · Арматура · Оборудование · Контейнеры
- **Qualification line:** Уточним тип груза, примерный вес и&nbsp;условия погрузки и&nbsp;разгрузки. Не работаем с&nbsp;эвакуацией легковых автомобилей.

**CTA**

| Role | Text | Target |
|------|------|--------|
| Primary | Рассчитать стоимость | `#contacts` (form) |
| Secondary | Позвонить | `tel:+79004658331` (номер — SAFE UNKNOWN until production NAP lock) |
| Tertiary (header) | Уточнить подачу | `#contacts` |

**Visual notes**

- Фото/рендер **одной** машины 5&nbsp;т (не коллаж «парк»).
- Крупно: борт / стрела / вылет (иконки или схема как в v4 specs).
- Убрать hero-rate «от XXXX ₽/час» из v4 placeholder.
- `hero-proof` strip: заменить «Свой автопарк» → «Одна машина» / «Понятные параметры»; убрать «5–10 тонн».

**Frontend implementation**

- Сохранить `.hero`, `.hero-proof`, `.button--primary`.
- Header phone + CTA visible on mobile without scroll.
- Messengers в hero **не** ставить выше телефона/формы.

**Must NOT change**

- Числа 5&nbsp;т / 3&nbsp;т / 14&nbsp;м / 6.2×2.2 / 2&nbsp;часа.
- H1 wording «5 тонн» + «Краснодар».
- Single-machine framing.

---

### 5.2 Machine specs / capability block

| | |
|--|--|
| **Purpose** | Core capability proof — ответ «подходит ли техника?» за 3–5 секунд. |
| **v4 base** | `screen-02-prices.html` → `.machine-showcase` |

**Final Russian copy**

- **Eyebrow:** Параметры техники
- **H2:** Параметры манипулятора 5&nbsp;тонн
- **Lead:** Одна машина с&nbsp;понятными параметрами: перевозка, погрузка и&nbsp;подача грузов без подмены техники после звонка.
- **Specs (dl):**

| Label | Value |
|--------|--------|
| Грузоподъёмность борта | 5&nbsp;т |
| Грузоподъёмность стрелы | 3&nbsp;т |
| Вылет стрелы | 14&nbsp;м |
| Кузов | 6.2 × 2.2&nbsp;м |
| Минимальный заказ | 2&nbsp;часа |

- **Operational line:** Подходит для стройматериалов, бытовок, ФБС и&nbsp;ЖБИ, арматуры, оборудования, контейнеров и&nbsp;тяжёлых грузов в&nbsp;рамках параметров техники. Работаем по&nbsp;Краснодару и&nbsp;краю.

**CTA**

| Role | Text |
|------|------|
| Primary | Рассчитать стоимость |
| Secondary | Уточнить подачу |

**Anxiety reduction (microcopy under CTA):** Ответим: подходит ли техника · сколько примерно будет стоить · когда возможна подача.

**Visual notes**

- Доминирующий блок на «втором экране»; фото машины + specs grid как в v4.
- Alt image: «Манипулятор 5&nbsp;т с&nbsp;крановой установкой на&nbsp;объекте в&nbsp;Краснодаре» (уточнить у оператора).

**Frontend**

- `id="fleet"` можно переименовать в `id="specs"`; обновить nav «Парк техники» → «Параметры» или убрать misleading anchor.

**Must NOT change**

- Spec table values.
- Wording «одна машина» / запрет «наша техника 5–10 т».

---

### 5.3 What tasks this machine fits

| | |
|--|--|
| **Purpose** | Use-case continuation — связать параметры с задачей пользователя. |
| **v4 base** | `.machine-transport__card--allowed` + denied card |

**Final Russian copy**

- **H2 (allowed):** Для каких задач подходит манипулятор
- **List:**
  - Перевозка бытовок
  - Доставка стройматериалов
  - Перевозка ФБС и&nbsp;ЖБИ
  - Доставка арматуры
  - Перевозка оборудования
  - Работа на&nbsp;строительных объектах
  - Разгрузка тяжёлых грузов в&nbsp;рамках 5&nbsp;т / 3&nbsp;т
- **Before dispatch:** Перед подачей уточняем параметры груза, адрес подачи, условия подъезда и&nbsp;особенности разгрузки.

**H3 (denied) — Что не перевозим**

- Легковые автомобили и&nbsp;эвакуация транспорта
- Грузы сверх параметров машины (борт / стрела)
- Негабарит вне возможностей техники
- Мелкие бытовые перевозки вне профиля

**CTA:** Получить расчёт → `#contacts`

**Visual notes**

- Две карточки allowed/denied как в v4 (зелёная/красная семантика).
- Denied — не «мелкий минус», а qualification + trust.

**Must NOT change**

- Evacuator / legkovye filter items.
- Capability ceiling (5/3 т).

---

### 5.4 How order works

| | |
|--|--|
| **Purpose** | Снять операционную неопределённость; снизить хаос-лиды. |
| **v4 base** | **NEW** — 3–4 step strip; визуально как `proof-strip` или compact cards |

**Final Russian copy**

- **H2:** Как заказать манипулятор 5&nbsp;тонн
- **Steps:**
  1. **Свяжитесь с нами** — позвоните или оставьте имя и&nbsp;телефон в&nbsp;форме.
  2. **Опишите задачу** — тип груза, примерный вес, адрес подачи и&nbsp;разгрузки, нужна ли работа стрелой.
  3. **Согласуем условия** — подходит ли машина, ориентировочная стоимость и&nbsp;время подачи **до выезда**.
  4. **Подача на объект** — работа по&nbsp;согласованным параметрам, минимальный заказ 2&nbsp;часа.

**CTA**

| Role | Text |
|------|------|
| Primary | Позвонить |
| Secondary | Рассчитать стоимость |

**Visual notes**

- 4 колонки desktop / stacked mobile; иконки Font Awesome как в v4.
- Без таймера «5 минут» если не подтверждено оператором.

**Frontend**

- Новый partial e.g. `screen-02b-order-steps.html`; вставить в `index.html` после `screen-02-prices`.

**Must NOT change**

- «Стоимость до выезда» principle.
- Min order 2&nbsp;часа mention.

---

### 5.5 Pricing / cost factors

| | |
|--|--|
| **Purpose** | Закрыть intent «манипулятор 5 тонн цена» без фейкового прайса. |
| **v4 base** | Убрать/не использовать v4 `hero__rate` XXXX; новый блок вместо tariff grid |

**Final Russian copy**

- **H2:** Стоимость манипулятора 5&nbsp;тонн
- **Lead:** Точную цену рассчитываем по&nbsp;вашей задаче заранее — без скрытых доплат после выезда.
- **Factors (list):**
  - Тип и&nbsp;вес груза
  - Расстояние и&nbsp;маршрут
  - Время работы (минимум 2&nbsp;часа)
  - Сложность погрузки и&nbsp;разгрузки
  - Необходимость работы стрелой
  - Условия подъезда на&nbsp;объект
- **Anchor line:** Стоимость зависит от&nbsp;задачи, а&nbsp;не от&nbsp;«самой низкой цены в&nbsp;интернете». Согласуем сумму до&nbsp;подачи техники.
- **SAFE UNKNOWN:** Почасовая ставка в&nbsp;рублях — **не публиковать** до подтверждения оператором.

**CTA:** Рассчитать стоимость · Уточнить подачу

**Visual notes**

- Без таблицы «от … ₽/час» unless operator supplies approved figure.
- Можно использовать спокойный light-section как FAQ upper.

**Must NOT change**

- No invented hourly rate.
- Min 2&nbsp;часа in factors.

---

### 5.6 Trust strip / reviews

| | |
|--|--|
| **Purpose** | Practical trust — живая, понятная, operationally reliable (не «крупная сеть»). |
| **v4 base** | `screen-03-trust-reviews.html`; опционально урезать `dark-proof-strip` |

**Final Russian copy**

**Trust block**

- **Eyebrow:** Почему обращаются
- **H2:** Работаем с&nbsp;частными клиентами, строительными компаниями и&nbsp;бизнесом
- **Lead:** Согласовываем стоимость и&nbsp;время подачи заранее — на&nbsp;одной машине с&nbsp;понятными параметрами.

**Cards (4):**

1. **Конкретная техника** — Манипулятор 5&nbsp;т / стрела 3&nbsp;т. Без подмены машины после звонка.
2. **Стоимость заранее** — Обсуждаем маршрут, груз и&nbsp;условия до&nbsp;выезда.
3. **Краснодар и&nbsp;край** — Подберём ближайшее возможное время подачи по&nbsp;маршруту.
4. **Наличный и&nbsp;безналичный расчёт** — Для частных клиентов и&nbsp;организаций.

**Reviews**

- **H2:** Отзывы клиентов
- **Subtitle:** Отзывы с&nbsp;Яндекс и&nbsp;Авито о&nbsp;работе техники и&nbsp;перевозке грузов.
- **Rating strip:** 4.9&nbsp;★ — На&nbsp;основе отзывов клиентов в&nbsp;Яндекс и&nbsp;Авито
- **CTA:** Читать отзывы клиентов (ссылка — SAFE UNKNOWN: URL виджетов до подключения)

**Visual notes**

- Убрать «2ГИС» из v4, если нет подтверждённого источника в PPC pack.
- Плейсхолдер-карточки отзывов допустимы до live widget; не выдумывать новые имена/даты без источника.
- `dark-proof-strip`: **не использовать** «10+ лет», «1000+ заказов», «от 30 минут» без верификации — заменить на: «4.9 ★ отзывы» · «Краснодар и&nbsp;край» · «Без посредников» · «Расчёт до выезда».

**Must NOT change**

- 4.9 ★ + Яндекс/Авито pairing (from pack).
- No fleet/autopark in trust cards.

---

### 5.7 B2B / payment notes

| | |
|--|--|
| **Purpose** | Закрыть B2B/payment intent без отдельной страницы (crosslink на `/manipulyator-dlya-yurlic/` позже). |
| **v4 base** | Trust card 4 + `contact-cta__facts` |

**Final Russian copy**

- **H3:** Для организаций и&nbsp;юрлиц
- **Body:** Работаем с&nbsp;безналичной оплатой и&nbsp;заявками от&nbsp;организаций. Условия и&nbsp;документы уточняем при расчёте задачи.
- **Bullets:**
  - Безналичный расчёт
  - Заявки от&nbsp;организаций
  - Согласование стоимости до&nbsp;выезда
- **Note:** НДС и&nbsp;закрывающие документы — **SAFE UNKNOWN:** формулировку «с&nbsp;НДС» включать только после подтверждения оператором.

**CTA:** Рассчитать стоимость

**Must NOT change**

- No «собственный автопарк» in B2B facts.
- Payment = pre-agreed before dispatch.

---

### 5.8 FAQ

| | |
|--|--|
| **Purpose** | Objection removal; support price + capability + geo intents. |
| **v4 base** | `screen-04-faq.html` |

**Final Russian copy**

| # | Question | Answer (summary) |
|---|----------|----------------|
| 1 | Какие грузы можно перевозить манипулятором 5&nbsp;тонн? | Стройматериалы, бытовки, оборудование, металлоконструкции, контейнеры, тяжёлые грузы **в рамках 5&nbsp;т / 3&nbsp;т**. |
| 2 | Как понять, подходит ли техника? | Сообщите тип груза, вес, размеры, адрес — подскажем fit и возможность работы. |
| 3 | Как рассчитывается стоимость? | Тип груза, расстояние, время (от 2&nbsp;часов), сложность погрузки/разгрузки, работа стрелой. |
| 4 | Работаете ли по Краснодарскому краю? | Да: Краснодар, пригороды, край — подача и цена по маршруту. |
| 5 | Можно ли оплатить по безналу? | Да: наличный, безнал, заявки от организаций. |
| 6 | Что не перевозите? | Эвакуация легковых; грузы вне параметров; нерелевантные бытовые перевозки. |
| 7 | Как быстро можно заказать? | Зависит от загрузки и адреса — свяжитесь, уточним ближайшее время. |

**CTA (implicit):** accordion без отдельной кнопки; sticky/header CTA остаётся.

**Must NOT change**

- FAQ answers must not introduce second machine or fleet.
- Price FAQ must not state fixed ₽/hour without operator data.

---

### 5.9 Final CTA

| | |
|--|--|
| **Purpose** | Final uncertainty removal; repeat primary conversion. |
| **v4 base** | `final-contact-cta.html` |

**Final Russian copy**

- **H2:** Нужно уточнить стоимость или возможность подачи?
- **Subtitle:** Свяжитесь с нами — подскажем: подходит ли техника · возможна ли подача · ориентировочная стоимость работы.
- **Form title:** Оставьте имя и&nbsp;телефон
- **Fields:** Имя · Телефон (**only** — убрать textarea «Что перевезти» из v4 или вынести в optional v2)
- **Primary button:** Рассчитать стоимость
- **Secondary:** Позвонить
- **Small text:** Перезвоним и&nbsp;уточним: тип груза · адрес подачи · возможность работы · ориентировочную стоимость.

**Messenger row (order locked)**

1. MAX  
2. Telegram  
3. WhatsApp  

**Phone block**

- `tel:+79004658331` — из v4; **SAFE UNKNOWN** production NAP / hours «7:00–22:00» until operator sign-off.

**Visual notes**

- Фон/contact truck image из v4 допустим.
- MAX icon first in `.contact-cta__channels`.

**Frontend**

- `action="#"` → replace with real endpoint when known (SAFE UNKNOWN).
- Direct goals: click tel + form submit events.

**Must NOT change**

- Form fields count (name + phone).
- Messenger order.
- Primary = form/call, not messenger.

---

## 6. Header / navigation (v5 adjustments)

| Element | v5 value |
|---------|----------|
| Logo | white/dark per v4 header on hero |
| Phone | Visible, `tel:` link |
| Header CTA | Уточнить подачу → `#contacts` |
| Header messengers | MAX (first) — optional compact; do not prioritize WA over MAX |
| Nav anchors | `#specs` Параметры · `#tasks` Задачи · `#order` Как заказать · `#pricing` Стоимость · `#reviews` Отзывы · `#faq` FAQ · `#contacts` Контакты |
| Remove / rename | «Парк техники» → «Параметры» |

---

## 7. Typography (HTML)

Apply non-breaking spaces in **all** final HTML copy:

| Pattern | HTML |
|---------|------|
| в Краснодаре | `в&nbsp;Краснодаре` |
| и краю | `и&nbsp;краю` |
| 5 т | `5&nbsp;т` |
| 3 т | `3&nbsp;т` |
| 14 м | `14&nbsp;м` |
| 2 часа | `2&nbsp;часа` |
| 5 тонн | `5&nbsp;тонн` (where unit word used) |
| с НДС | `с&nbsp;НДС` (only if operator approves claim) |
| для юр. лиц | `для&nbsp;юр.&nbsp;лиц` |

Reference: `workspaces/triumph-manipulator-landing-v4/docs/V4-SECTION-LANGUAGE.md` §8.

---

## 8. PPC QA checklist (pre-launch)

- [ ] Live URL `https://manipulator-triumph.ru/manipulyator-5-tonn/` returns this page (SAFE UNKNOWN until deploy).
- [ ] H1 + hero bullets match ad: 5 т, 3 т, 14 м.
- [ ] No «автопарк» / «5–10 т» / fleet imagery copy.
- [ ] Form: name + phone; submits tracked for Direct.
- [ ] `tel:` click works on mobile.
- [ ] Messengers: MAX → Telegram → WhatsApp order in footer CTA.
- [ ] `noindex` until SEO strategy says otherwise.
- [ ] Group 01 import checklist: `runs/full-cycle-v1.1/commander-import-checklist-v1.1.md` hero continuity item.

---

## 9. Out of scope (this handoff)

- HTML/SCSS implementation
- Other intent pages (bytovki, stroymaterialy, …)
- Governance / mars-runtime / ORCA tool changes
- Git commit / push

---

## 10. Source documents used

| Source | Path |
|--------|------|
| Master hot (tone reference) | `landing-pages/01-master-hot-general.md` |
| Page blueprint | `landing-pages/05-capability-5-ton.md` |
| Intent tiers | `research/intent-groups-v1.md` |
| Campaign instance | `schema/instances/triumph-s-tier-draft-v1.json` (grp_fc01_5ton) |
| Full cycle context | `runs/full-cycle-v1.1/full-cycle-summary-v1.1.md`, `campaign-structure-v1.1.md` |
| v4 workspace | `workspaces/triumph-manipulator-landing-v4/` |
| Factory blueprint (shape) | `projects/mars-website-factory/reference-cases/triumph-manipulator-landing/page-blueprint-v0.md` |

---

*End of handoff — Page 01 «Манипулятор 5 тонн»*
