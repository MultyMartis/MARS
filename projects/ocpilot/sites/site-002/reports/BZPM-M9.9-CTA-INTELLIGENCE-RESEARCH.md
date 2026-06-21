# REPORT — BZPM M9.9 CTA Block Intelligence Research

**Проект:** SITE-002 / BZPM (ЗПМ)  
**Среда (baseline, read-only):** https://zpm.new-site.space/  
**Режим:** RESEARCH ONLY — без реализации, деплоя, кода и дизайна  
**Дата:** 2026-06-21  
**Authority:** BZPM catalog-redesign (W0–W2) · M9.8.9-03/03B forensic · BZPM MI Registry v2 · live HTML capture 2026-06-21

---

## 1. Executive Summary

### Задача исследования

Подготовить **фактическую базу** для полной переработки CTA-блока на category PLP (после сетки товаров, перед footer). Текущий блок на TEST (`blockcommercialtrust.twig`) — отправная точка, не целевое состояние.

### Ключевые выводы

| # | Вывод | Evidence |
|---|--------|----------|
| 1 | **Post-grid CTA на PLP — редкость у сильных OEM-пиров.** Abat, Kroner, Techno-TT, Restoinox на category PLP **не** показывают полноформатную форму + сертификаты после сетки. Конверсия вынесена в header/popup/телефон или отложена на dedicated pages. | Live fetch 2026-06-21; W1D-F-05 |
| 2 | **У дистрибьюторов (КЛЕН, Юниторг) — persistent consult layer**, не «стена» после каталога: callback modal, «подобрать оборудование», прайс в nav, floating consultant. | Klen HTML; Unitorg footer CTAs |
| 3 | **Главный барьер BZPM-блока — не компактность, а mismatch intent:** заголовок «Дилерам» / «Прайс» не закрывает вопросы снабженца, владельца и проектировщика после просмотра SKU (M9.8.9-03B). | Forensic + live TEST |
| 4 | **Сертификат «Сделано в России» ≠ гарантия качества сам по себе.** Это маркировка программы СДС РЭЦ при наличии обязательного conformity + добровольного сертификата по направлению (надёжность/экологичность/…). **Не заменяет** ПП №719 для госзакупок. | РЭЦ/СДС публичные правила; см. §5 |
| 5 | **FAQ на PLP у B2B-производителей почти не встречается inline.** FAQ живёт на `/help`, `/dealers`, `/about/faq` или в SEO-блоке (Restoinox). Для BZPM **8 карточек FAQ после формы** — дифференциатор, если вопросы **закрывают реальные возражения**, а не SEO. | Techno-TT FAQ page; Restoinox PLP SEO |
| 6 | **Рекомендуемая архитектура для следующего этапа: Option D (Mixed)** — верх: trust + outcome-driven form; низ: 8 FAQ-карточек по role-weighted objections; без дублирования homepage advantages. | Синтез §2–§6 |

### Текущее состояние BZPM (TEST, read-only snapshot)

**URL:** https://zpm.new-site.space/stoly-serii-premium/stoly/ (и leaf `/katalog/.../stoly/`)

**Структура блока (верх):**
- Label «Поможем с выбором» + category-aware H2
- Lead: производство Барнаул, поставки РФ
- Cert column: swiper 1 thumb + Fancybox
- 3 benefit cards (production / certification / placeholder «рыба»)
- Form card: «Получить прайс-лист» + fields + `dialog=7`

**Нижняя FAQ-сетка:** в текущем live **не обнаружена** — запланирована в M9.9 scope.

**Известные проблемы (documented):** persona mismatch, cert без типа документа, placeholder copy, нет SLA/outcome chips, дублирование смыслов homepage без дифференциации PLP (M9.8.9-03B §1).

### Scope boundaries

| In scope | Out of scope |
|----------|--------------|
| Competitor CTA patterns | Финальные тексты |
| Objection map по 6 ролям | Twig/CSS/JS |
| TOP-30 FAQ (evidence-based) | Deploy TEST |
| Certificate semantics | SEO-статьи ради объёма |
| 4 architecture options + recommendation | Pixel design |

### UNKNOWN (требует operator input до implementation)

- SLA ответа на заявку / КП
- Точный реестр unique сертификатов ЗПМ на FTP
- CRM routing по intent (КП vs дилер vs тендер)
- Analytics submit rate по persona — **нет in-repo product**

---

## 2. Competitor Audit

**Метод:** live HTTP fetch (curl, 2026-06-21) category PLP «столы» / neutral equipment где URL доступен; дополнение archived BZPM W1D/W2 findings.  
**Ограничение:** Trapeza — Nuxt SPA; post-grid DOM частично в client payload → **SAFE UNKNOWN** для нижних блоков без browser render.

### 2.1 Сводная матрица (post-catalog zone)

| Компания | URL (проверен) | Post-grid CTA block | Структура после сетки | Смысл | Сильные стороны | Слабые стороны |
|----------|----------------|---------------------|------------------------|-------|-----------------|----------------|
| **ЗПМ (BZPM TEST)** | https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/ | **Да — full block** | Cert + 3 benefits + pricelist form | OEM trust + lead capture после evaluation | Category-aware headline; Fancybox; outcome «прайс»; production locality | Persona skew to dealer/price; cert без labels; placeholder benefits; ~2 viewport height risk (legacy) |
| **Trapeza** | https://www.trapeza.ru/catalog/.../stoly/ | **Не верифицирован inline** (SPA) | Product grid + filters dominant; Q&A community на PDP (W1D), не на PLP | Database self-serve; консультация через контактные каналы | Max SKU density; filter semantics (наличие, секции) | Нет OEM «производитель» narrative на PLP; post-grid commercial **UNKNOWN** |
| **КЛЕН** | https://www.klenmarket.ru/shop/equipment/neutral-equipment/stoly/ | **Нет dedicated post-grid form** | Site-wide floating **consultant** («Остались вопросы?» + callback modal); footer callback | Distributor consult + complex equipment entry in nav | Persistent consult UI; прайс-листы в mega-menu; HACCP service line | OEM/production proof слаб на PLP; CTA fragmented (nav vs float vs footer) |
| **Techno-TT** | https://www.tehno-tt.ru/catalog/neutralnoe-oborudovanie/stoly/ | **Нет** | Category listing only; **header** pricelist PDF links; footer → `/about/faq/` | Manufacturer via header/footer; popup callback forms | Pricelist upfront; FAQ hub; «производим с 1998» in header band | No decision-stage block after grid; B2B buyer must know to open FAQ |
| **Kroner** | https://kroner.pro/catalog/stoly/ | **Нет** | Listing + filters; dealer intent → `/dealers/` popup form | **Channel policy:** OEM sells through dealers only | Clear dealer-only positioning; project/esciz support for dealers | End buyer on PLP gets **no** direct RFQ path — intentional |
| **Restoinox** | https://restoinox.ru/catalog/stoly/ | **Нет form band** | **SEO text block** after grid (SanPiN, series types, order process); header callback + «Задать вопрос» | Manufacturer proof in **content**, not form | Answers «кто производитель», docs, project spec buy; real selection copy | Long SEO scroll; no structured FAQ cards; form not at decision point |
| **Restoll** | https://www.restoll.ru/catalog/neutralnoe_oborudovanie/stoly/ | **Нет** (Aspro pattern) | Callback in header; «Комплексное оснащение» in nav | Federal supplier self-serve + phone | Phone-first B2B | Thin post-grid commercial |
| **ГК Юниторг** | https://www.unitorg.ru/catalog/neutralnoe_oborudovanie/stoly/ | **Footer-only CTAs** on captured page | «подобрать оборудование» + «напишите нам» popups; project/delivery in meta | Regional integrator: project + logistics | Dual popup intents (selection vs message) | No cert/OEM panel; weak trust at scroll end |
| **BSV-inox** | https://bsv.ru/... (404 on stoly URL) | N/A | Popup «Обратная связь» site-wide | Generic contact | Company field in form (B2B signal) | URL unstable; no PLP commercial architecture observed |
| **Abat** | https://abat.ru/catalog/neutralnoe-oborudovanie/stoly-proizvodstvennye/ | **Нет** (W1D-F-05) | «Где купить» dealer path; no PLP form | Brand catalog → dealer network | Clean OEM category UX | Zero procurement capture on PLP |
| **Энтеро** | category URL 404 on probe | — | Legacy commercial (operator note FIM-W3Y-005) | — | — | Not re-verified live |

### 2.2 Паттерны по типам блоков

#### A. CTA после каталога / после списка товаров

| Паттерн | Кто | Структура | Смысл |
|---------|-----|-----------|-------|
| **Full commercial panel** | BZPM (unique among sampled OEM PLPs) | Cert + value props + inline form | Capture lead at decision fatigue point |
| **SEO continuation** | Restoinox | H2/H3 + prose (SanPiN, variants, order) | SEO + implicit trust; no form |
| **None (self-serve ends at grid)** | Kroner, Techno-TT, Abat | Pagination → footer | Buyer must use header/dealer channel |
| **UNKNOWN** | Trapeza | — | Requires rendered audit |

#### B. Коммерческие блоки рядом с формами (не обязательно post-grid)

| Паттерн | Пример | Элементы рядом с формой |
|---------|--------|-------------------------|
| **Outcome headline** | BZPM TEST | «Получить прайс-лист» + promise subline |
| **Dealer qualification** | Kroner `/dealers/` | Benefits grid + ИНН + company fields |
| **Callback minimal** | Klen modal | Phone-first, expert photo |
| **Pricelist in header** | Techno-TT | PDF links separate from form |
| **Dual intent buttons** | Юниторг footer | Selection vs message (no unified form) |

#### C. FAQ на промышленных B2B сайтах

| Размещение | Пример | Характер вопросов |
|------------|--------|-------------------|
| Dedicated `/about/faq/` | Techno-TT | Order lifecycle, returns, coupons — **mixed B2C/B2B** |
| Nav link «FAQ» | Klen `/company/seminary/#faq` | Training/events context |
| Inline SEO Q&A | Restoinox PLP bottom | Product/education prose, not accordion FAQ |
| **Inline FAQ cards on PLP** | **Not found** in sampled set | **Gap/opportunity for BZPM** if questions are procurement-real |

### 2.3 Implications для BZPM

1. **Полный post-grid block — осознанное отличие от OEM-пиров**, не industry default. Должен **оправдываться outcome clarity**, иначе воспринимается как «wallpaper» (W2-F-07).
2. **Сильнейшие peer patterns для заимствования смыслов (не layout):**
   - Techno-TT: pricelist accessibility + FAQ hub
   - Klen: persistent «остались вопросы» + expert consult
   - Restoinox: project/spec procurement language in content
   - Kroner: explicit channel policy (dealer vs direct)
3. **Запланированные 8 FAQ-карточек** — конкурентное поле пустое на PLP; риск — превратить в SEO-мусор.

---

## 3. Objection Map

**Метод:** синтез W1C buyer flow · WH-15 B2B CTA gap · M9.8.9-03B persona table · dealer copy в legacy PLP (`m989-audit-*.html`) · Techno-TT/Kroner public pages · BZPM redesign CV-01/02/04.

**Шкала отложения:** что человек делает вместо submit (phone competitor, Excel compare, «уточню у шефа», закрывает вкладку).

---

### ROLE A — Снабженец

| Dimension | Content |
|-----------|---------|
| **Что хочет узнать** | Реальный производитель или перекуп; наличие/срок на **конкретные SKU**; возможность КП на N позиций; условия оплаты/отсрочки; логистика до своего региона; соответствие спецификации |
| **Чего боится** | Срыв срока открытия/производства; подмена серии; «прайс по запросу» без цифр; неофициальный поставщик; расхождение КП с сайтом |
| **Что проверяет** | Артикул, цена на карточке, статус, реквизиты, сертификаты, опыт поставок, **кто ответит и когда** |
| **Почему оставляет заявку** | Нужен **формализованный КП** для согласования; пакетная закупка; нет нужной комбинации на сайте; требуется фиксация цены |
| **Почему НЕ оставляет** | Уже есть поставщик с прайсом; форма «для дилеров»; нет SLA; достаточно цен на карточках для внутреннего сравнения |
| **Почему просит прайс** | Сравнительная таблица в Excel; согласование с финдиректором; тендер без публичных цен на все позиции |
| **Почему сравнивает поставщиков** | Обязательный регламент 3 КП; прошлый негативный опыт; разброс цен на «одинаковые» столы |
| **Почему откладывает** | Ждёт спецификацию от технолога; сезонный freeze; «сначала посмотрю Trapeza/регионала» |

---

### ROLE B — Владелец кафе

| Dimension | Content |
|-----------|---------|
| **Что хочет узнать** | «Кто вы?»; можно ли доверять неизвестному заводу; **итоговая сумма комплекта**; срок открытия; гарантия и кто чинит |
| **Чего боится** | Переплата vs «дешёвый стол»; обман с металлом/толщиной; долгий простой кухни; скрытые доплаты доставки |
| **Что проверяет** | Отзывы (если есть), фото производства, понятность каталога, телефон, **простой способ «помогите собрать»** |
| **Почему оставляет заявку** | Не разбирается в сериях ПРЕМИУМ/СТАНДАРТ; нужен комплект «под ключ»; хочет человека |
| **Почему НЕ оставляет** | Уже выбрал 2–3 модели в корзину; не доверяет форме; думает «позвоню завтра» |
| **Почему просит прайс** | Бюджет ограничен жёстко; сравнивает с Avito/локальным сварщиком |
| **Почему сравнивает** | Первый закуп; совет знакомого «купи у X» |
| **Почему откладывает** | Нет финального плана помещения; аренда не подписана |

---

### ROLE C — Владелец производства (пищевое производство)

| Dimension | Content |
|-----------|---------|
| **Что хочет узнать** | Сертификация для аудита; нестандарт/серийность; стабильность повторных поставок; документы на партию |
| **Чего боится** | Остановка линии из-за несоответствия габаритов; нет документов для проверки; смена конструкции без notice |
| **Что проверяет** | ТУ/ГОСТ, паспорт, сертификат соответствия, **«Сделано в России» vs промышленное подтверждение**, lead time на серию |
| **Почему оставляет заявку** | Нужен расчёт линии/комплекта; кастом; повторяющийся контракт |
| **Почему НЕ оставляет** | Уже есть approved vendor list; ждёт проектировщика |
| **Почему просит прайс** | Годовой контракт; калькуляция себестоимости продукции |
| **Почему сравнивает** | Тендер на оснащение цеха |
| **Почему откладывает** | CAPEX не утверждён |

---

### ROLE D — Проектировщик

| Dimension | Content |
|-----------|---------|
| **Что хочет узнать** | Стандартизированные серии; чертежи/модели; соответствие SanPiN; комплект документов для проекта/тендера |
| **Чего боится** | Заложить модель, которую нельзя поставить; смена артикула; нет BIM/PDF |
| **Что проверяет** | Размерный ряд, документы на PDP, сертификаты (readable), контакт технического специалиста |
| **Почему оставляет заявку** | Запрос спецификации; верификация альтернатив; комплект docs zip |
| **Почему НЕ оставляет** | Скачал docs с PDP; использует дилера как посредника |
| **Почему просит прайс** | Смета проекта (даже ориентир) |
| **Почему сравнивает** | Equivalents в спецификации |
| **Почему откладывает** | Проект на стадии эскиза |

---

### ROLE E — Дилер

| Dimension | Content |
|-----------|---------|
| **Что хочет узнать** | Дилерская цена; MOQ; маркeting support; стабильность поставок; эксклюзив/территория |
| **Чего боится** | Прямые продажи завода клиенту; нет защиты сделки; «прайс после формы» без follow-up |
| **Что проверяет** | `/dealers` policy, Kroner-style channel rules, margin headroom vs Techno-TT |
| **Почему оставляет заявку** | Хочет прайс-лист и статус партнёра — **legacy BZPM copy explicitly targets this** |
| **Почему НЕ оставляет** | Уже партнёр; форма выглядит как retail lead |
| **Почему просит прайс** | Core job-to-be-done for role |
| **Почему сравнивает** | Line card vs Restoinox/Kroner |
| **Почему откладывает** | Ждёт сезон sales plan |

---

### ROLE F — Тендерный закупщик

| Dimension | Content |
|-----------|---------|
| **Что хочет узнать** | Соответствие ТЗ; **ПП №719 / реестр** (если applicable); комплект conformity docs; срок и penalty risk |
| **Чего боится** | Дисквалификация за документы; поставщик не производитель; знак «Сделано в России» подменяет industrial proof |
| **Что проверяет** | Сертификаты (full PDF), реквизиты, опыт аналогичных поставок, channel letter |
| **Почему оставляет заявку** | Запрос КП под ТЗ; уточнение compliance |
| **Почему НЕ оставляет** | Закупка только через ЭТП; vendor not in registry |
| **Почему просит прайс** | НМЦ; auction starting price |
| **Почему сравнивает** | Mandatory multi-bid |
| **Почему откладывает** | Ждёт публикации извещения |

---

### Cross-role objection clusters (для FAQ/CTA design)

| Cluster | Roles | Blocker type |
|---------|-------|--------------|
| **Identity distrust** («перекуп?») | A, B, C | Trust |
| **Outcome opacity** (что после submit) | A, B, E | Conversion |
| **Wrong audience label** («дилерам») | A, B, D | Conversion |
| **Document adequacy** | C, D, F | Trust + FAQ |
| **Price discovery** | A, B, E, F | Procurement |
| **Timing/SLA** | A, B, E | Conversion |
| **Self-serve sufficient** | A, D | Suppress form need |

---

## 4. FAQ Intelligence

**Метод:** вопросы **не придуманы** — derived from: Techno-TT `/about/faq/` · Kroner dealers page · Restoinox PLP SEO themes · BZPM W1B/W1C friction · legacy dealer paragraph (`m989-audit-stoly.html`) · M9.8.9-03B trust stack · СДС «Сделано в России» program FAQ · B2B catalog practice (CV-01/03/04).

**Шкалы:**
- **Частота:** H / M / L — сколько ролей и источников повторяют
- **Важность:** Critical / High / Medium
- **Коммерческая ценность:** насколько ответ **двигает к заявке** (не SEO)

| # | Вопрос (смысл, не copy) | Частота | Важность | Комм. ценность | Evidence |
|---|-------------------------|---------|----------|----------------|----------|
| 1 | Это производитель или перекупщик? | H | Critical | High | W1C; M9.8.9-03B P1; Restoinox «собственная база» |
| 2 | Что я получу после отправки формы (КП, прайс, звонок)? | H | Critical | High | M9.8.9-03B §2.4; legacy dealer copy |
| 3 | Как быстро ответят? | H | High | High | M9.8.9-03 forensic; **SLA UNKNOWN** |
| 4 | Можно ли получить прайс-лист без «менеджерской» игры? | H | High | High | Techno-TT header pricelist; BZPM form title |
| 5 | Есть ли товар в наличии / срок «под заказ»? | H | Critical | Medium | W1B-F-09; W1A-F-12 |
| 6 | Как доставляете в мой регион и сколько стоит? | H | High | Medium | Techno-TT delivery page; WH-15 |
| 7 | Какая гарантия и кто обслуживает? | H | High | Medium | Techno-TT about; Kroner dealers |
| 8 | Какие документы (сертификат, паспорт, декларация)? | H | Critical | High | Tender roles; Techno-TT cert mention |
| 9 | Чем серия X отличается от Y (ПРЕМИУМ vs СТАНДАРТ)? | H | High | Medium | W1C WH-01; W1B ПРЕМИУМ-3 case |
| 10 | Можно ли подобрать комплект под мою кухню/цех? | H | High | High | CV-02; Restoinox SEO |
| 11 | Делаете ли нестандарт / размер на заказ? | M | High | High | Techno-TT custom projects |
| 12 | Условия для дилеров / опта? | M | High | High | Kroner channel; BZPM `/dealers` |
| 13 | Работаете ли с юрлицами и безналом? | M | High | Medium | B2B default expectation |
| 14 | Можно ли закупить по спецификации проекта? | M | High | High | Restoinox «спецификация к проекту» |
| 15 | Соответствие SanPiN / пищевой стали? | M | High | Medium | Restoinox PLP SEO |
| 16 | Что означает «Сделано в России» на вашей продукции? | M | High | Medium | §5; news ref M9.8.9-03B |
| 17 | Подходит ли для госзакупки / 44-ФЗ? | L | Critical | Medium | ПП719 vs СДС — **case-by-case UNKNOWN** |
| 18 | Можно ли сравнить модели / есть compare? | M | Medium | Low | W1C-F-09 |
| 19 | Почему цена на сайте — не финальная? | M | Medium | Medium | CV-05 legal disclaimer pattern |
| 20 | Есть ли скидки при объёме? | M | High | High | Dealer/supply roles |
| 21 | Как оформить заказ с сайта (корзина vs счёт)? | M | Medium | Medium | Techno-TT FAQ order flow |
| 22 | Можно ли вернуть / обменять? | M | Medium | Low | Techno-TT FAQ returns — **B2C-leaning** |
| 23 | Как отследить статус заказа? | L | Medium | Low | Techno-TT FAQ |
| 24 | Толщина металла / качество сварки? | M | High | Medium | Restoinox SEO «0,8 мм» |
| 25 | Есть ли монтаж / пусконаладка? | M | Medium | Medium | Юниторг integrator model |
| 26 | Минимальная партия / MOQ? | M | High | High | Dealer/tender |
| 27 | Можно ли получить образец? | L | Medium | Medium | **UNKNOWN if ZPM offers** |
| 28 | Как связаться с техническим специалистом, не sales? | M | High | High | Project roles; Klen expert consult |
| 29 | Актуальность цен на сайте? | M | High | Medium | W2 price disclaimer |
| 30 | Чем ЗПМ отличается от Trapeza/регионального дилера? | M | Medium | High | Competitive objection — **facts need operator lock** |

### TOP-8 для карточек FAQ (рекомендация приоритизации блока)

Для **8 карточек** на PLP — не SEO TOP-8, а **conversion TOP-8**:

1. Производитель vs перекуп (identity)
2. Что будет после заявки (outcome)
3. Срок ответа (SLA — pending operator)
4. Прайс / КП — как получить
5. Документы и сертификация
6. Наличие и сроки производства
7. Доставка по РФ
8. Подбор комплекта / консультация по серии

**Defer to secondary page/accordion:** returns, coupons, order merge (Techno-TT FAQ noise for PLP).

---

## 5. Certificate Intelligence

**Объект:** знак/сертификат программы **«Сделано в России»** (СДС РЭЦ) в контексте CTA-блока ЗПМ.  
**Не юридическое заключение** — operational semantics для UX/copy governance.

### 5.1 Что сертификат реально подтверждает

| Claim level | Подтверждается? | Basis |
|-------------|-----------------|-------|
| Продукция **произведена в РФ** | **Да** — базовое условие программы | СДС rules; РЭЦ program materials |
| Наличие **обязательного** документа conformity (декларация/сертификат ТР ТС/ЕАЭС, ГОСТ и т.д.) | **Да** — prerequisite | Program FAQ; certification guides |
| Наличие **добровольного** сертификата/испытаний по одному из **направлений** СДС (надёжность, экологичность, уникальность, органичность) | **Да** | Program FAQ |
| Наличие **НТД** (ГОСТ/ТУ/СТО) на продукцию | **Да** — required evidence class | EAC audit summaries |
| Право **маркировки** знаком «Сделано в России» на **сертифицированную** продукцию | **Да** | Program participation outcome |
| Участие в **программе продвижения** российской продукции (export/marketing context) | **Да** — program scope | RЭЦ program description |

### 5.2 Что сертификат НЕ подтверждает

| Misread | Reality |
|---------|---------|
| «Лучший на рынке» | Only enrolled SDS direction claims — not competitive ranking |
| «Государственная гарантия качества» | Voluntary scheme; not state warranty |
| «Подходит для любой госзакупки» | **Не заменяет** подтверждение по **ПП РФ №719** / отраслевым локализациям | 
| «100% российские комплектующие» | Production in RF ≠ full localization percentage |
| «Сертификат = паспорт изделия» | Different document types |
| «Без дополнительных проверок» | РЭЦ relies on accredited body docs — not factory audit each time |
| «Дилер/перекуп тоже “производитель”» | Sign applies to **certified product line of applicant manufacturer** |

### 5.3 Выгоды клиента (реальные, не маркетинг)

| Benefit | For whom |
|---------|----------|
| Traceable **origin** for compliance files | C, D, F |
| Extra **voluntary quality dimension** (e.g. reliability testing) | C, A |
| Mark recognition in **import substitution** context | A, F |
| Export/promotion program association (if relevant) | OEM marketing |
| Confidence that baseline **mandatory conformity** exists | All B2B |

### 5.4 Допустимые смыслы (directions for adjacent copy — NOT final text)

- «Продукция производится в России» (if true for SKU scope)
- «Участник программы / маркировка “Сделано в России” на сертифицированную линейку»
- «Подтверждено обязательными документами соответствия + добровольная сертификация по направлению [X]»
- «Документ доступен для ознакомления» (+ lightbox)
- «Для проектной документации — полный пакет по запросу»

### 5.5 Маркетинговый мусор (запрещённые смысловые классы)

- «Единственный / лучший производитель России»
- «Гарантирован победу в тендере»
- «Полная локализация» без расчёта
- «Государственный сертификат качества» (нет такого класса)
- «Не требует других документов»
- «Сертификат вместо гарантийного талона»
- Generic «сертифицированная продукция» **без указания типа документа**

### 5.6 Смыслы рядом с сертификатом в CTA-блоке

| Layer | Purpose |
|-------|---------|
| **Document type label** | «Сертификат соответствия» / «Сделано в России» — разные proofs |
| **Audience tag** | «Для тендера и аудита» vs «Для закупки комплекта» |
| **Action** | View full doc (lightbox); «все документы» |
| **OEM anchor** | Factory locality (Барнаул) **рядом**, not inside cert image |
| **Separate industrial track** | Link «промышленное подтверждение / 719» only if **verified** — else omit |

**SAFE UNKNOWN for ZPM:** exact SDS direction enrolled (надёжность vs др.); SKU coverage; whether `certificat_00/01` map 1:1 to SDS vs EAC only — **verify on FTP + legal**.

---

## 6. CTA Architecture Options

Все варианты предполагают placement: **PLP → grid → pagination → [CTA BLOCK] → footer**.  
Верхняя часть = cert + form + trust; нижняя = **8 FAQ cards** (M9.9 charter).

---

### OPTION A — FAQ driven

**Структура блока**

```
[ Category context headline — minimal ]
[ FAQ grid 8 cards — primary surface ]
[ Compact trust strip: RU badge + 2 cert thumbs + lightbox ]
[ Narrow form: 3 fields + outcome chip ]
[ Secondary link: /dealers ]
```

**Логика пользователя**

1. После grid остаются **нерешённые вопросы** → FAQ первым снимает возражения.
2. Form — **короткий** «если ответов достаточно».
3. Сертификат — supporting proof, not hero.

**Преимущества**

- Прямое закрытие §4 TOP-8 objections
- Меньше persona mismatch («не форма дилерам», а «ответы»)
- Отличие от текущего BZPM cert-heavy strip

**Недостатки**

- FAQ может читаться как SEO если вопросы generic
- Form below fold on mobile (P5 risk W2 mobile rules)
- Слабее immediate lead capture vs form-first

---

### OPTION B — Trust driven

**Структура блока**

```
[ Decision band background ]
[ OEM identity row: manufacturer + locality + RU badge ]
[ Proof panel: labeled certs (2) + guarantee + delivery RF ]
[ Form card: outcome headline + SLA chip + fields ]
[ FAQ grid 8 — collapsed visual weight, smaller cards ]
```

**Логика пользователя**

1. «Можно ли доверять заводу?» — решается вверху.
2. Form — **награда** за установленное доверие.
3. FAQ — hygiene для оставшихся doubts.

**Преимущества**

- Aligns M9.8.9-03B Manufacturer Proof + Decision Band hybrid
- Strong for roles C, D, F (documents)
- Cert semantics fix (labeled types)

**Недостатки**

- Risk of repeating homepage advantages (W2-F-07)
- Vertical height if FAQ not compact
- Requires real proof assets — no placeholders

---

### OPTION C — Procurement driven

**Структура блока**

```
[ Headline: procurement outcome for {category} ]
[ 3-step process strip: запрос → КП/прайс → отгрузка ]
[ Dual-lane entry (no dual forms): ]
   Lane 1: «Закупка / проект» → primary form
   Lane 2: «Партнёрство» → /dealers button
[ Cert row minimal — icon + «документы» link ]
[ FAQ 8 — skewed to price/lead time/MOQ/docs ]
```

**Логика пользователя**

1. Buyer self-identifies procurement path.
2. Form = **КП/прайс**, not «стать дилером».
3. FAQ supports tender/supply mechanics.

**Преимущества**

- Best for roles A, E, F
- Clear outcome promise (§3 cluster «price discovery»)
- Reduces wrong-audience objection

**Недостатки**

- Weaker for owner B (needs simpler emotional trust)
- Process strip can feel generic if not factual
- Dual-lane UI complexity (M9.8.9-03B Variant C risk)

---

### OPTION D — Mixed model (recommended base)

**Структура блока**

```
┌─ UPPER: COMMERCIAL CORE ─────────────────────────────┐
│ Row 1: Category-aware consultative headline (CV-02)   │
│ Row 2: Trust metrics [RU production | Cert | Warranty | Ship] │
│ Row 3: Split                                         │
│   Left: Proof — featured cert + secondary + all docs │
│   Right: Form — outcome + SLA + intent select (*)    │
│ Row 4: Secondary — partner link /dealers             │
└──────────────────────────────────────────────────────┘
┌─ LOWER: FAQ RESOLUTION GRID (8 cards) ───────────────┐
│ Cards = §4 TOP-8; each opens answer OR anchor panel  │
│ Purpose: objection kill after trust+form scan        │
└──────────────────────────────────────────────────────┘
```

(*) Intent select — CRM mapping **UNKNOWN**; can ship UI-only with single backend dialog=7 initially.

**Логика пользователя**

| Step | User state | Block response |
|------|------------|----------------|
| 1 | Finished scanning SKUs | Headline acknowledges category context |
| 2 | «Кто вы?» | Trust metrics + certs |
| 3 | «Что дальше?» | Form with explicit outcome |
| 4 | «А если…?» | FAQ grid without scrolling to footer |

**Преимущества**

- Combines B + selective C without dual forms
- FAQ separated **ниже** — matches M9.9 charter (upper cert/form/benefits, lower FAQ)
- Mobile: can reorder to headline → FAQ top-4 → form → FAQ rest (implementation note only)

**Недостатки**

- Highest content design discipline — failure mode = current block + FAQ spam
- Two visual tiers to maintain
- Still taller than peer OEM PLPs — needs compact density rules

---

## 7. Recommendation

### Primary recommendation

**Proceed to design phase with Option D (Mixed model)**, using content rules from §3–§5.

### Specification locks for next stage (implementation charter input)

| Area | Rule |
|------|------|
| **Headline** | Consultative + `{category}` context — **not** «Дилерам и оптовикам» as default |
| **Form outcome** | Explicit: КП / прайс / подбор — aligned to dialog=7 or future routing |
| **Certificate** | 2 labeled proofs + lightbox group; no duplicate slides; no swiper on PLP |
| **Benefits** | Max 3 — **PLP-specific**, not copy homepage advantages verbatim |
| **FAQ (8)** | Strictly §4 TOP-8; accordion/card; no SEO essays |
| **Dealer path** | Secondary link `/dealers` — not competing primary button |
| **Suppress** | Placeholder «рыба» content; generic «работаем по РФ» without proof |
| **Height budget** | Target ≤1.5 mobile screens from pagination to form submit (M9.8.9-03B acceptance) |

### Alternatives when to pivot

| Condition | Pivot to |
|-----------|----------|
| Operator insists dealer-first KPI | Option C with stronger Lane B |
| Legal restricts outcome promises | Option A (FAQ-first, minimal form) |
| Analytics show FAQ never expanded | Option B (trust-first, shrink FAQ to 4) |
| Leaf PLP scroll fatigue confirmed | Variant C contextual compact (BZPM Architecture §F tier-3) — **separate charter** |

### Evidence gaps before build

1. Operator lock: SLA, guarantee term, SDS direction text  
2. FTP: final certificate inventory  
3. A/B decision: intent select vs single form  
4. Trapeza/Klen rendered post-grid audit (browser QA)  
5. Legal review: «Сделано в России» adjacent claims for ZPM SKU scope  

### Relation to prior M9.8.9 work

| Artifact | Use |
|----------|-----|
| M9.8.9-03 forensic | Technical baseline (dialog=7, Fancybox, controller wiring) |
| M9.8.9-03B redesign | UX diagnosis — **still valid**; this report **extends** with competitor + FAQ + cert + 4 options |
| BZPM REDESIGN Architecture §F | Tiering policy — full block on every deep PLP remains **tension**; Option D mitigates via density + FAQ utility |

---

## Evidence index

| ID | Source |
|----|--------|
| E-01 | `projects/ocpilot/sites/site-002/reports/SITE-002-M9.8.9-03-CERTIFICATES-DEALERS-MERGE-FORENSIC-AND-DESIGN.md` |
| E-02 | `projects/ocpilot/sites/site-002/reports/SITE-002-M9.8.9-03B-COMMERCIAL-TRUST-BLOCK-REDESIGN.md` |
| E-03 | `projects/website-factory/execution-cases/bzpm-catalog-redesign/BZPM-FINDINGS-REGISTER-v1.md` |
| E-04 | `projects/website-factory/execution-cases/bzpm-catalog-redesign/BZPM-REDESIGN-ARCHITECTURE-v1.md` §F |
| E-05 | `projects/website-factory/execution-cases/bzpm-market-intelligence/BZPM-COMPETITOR-REGISTRY-v2.md` |
| E-06 | Live HTML captures `.recovery-temp/m99-*.html` (2026-06-21) |
| E-07 | https://www.tehno-tt.ru/about/faq/ |
| E-08 | https://kroner.pro/dealers/ |
| E-09 | СДС «Сделано в России» — program FAQ summaries (khabexport.com mirror; eacaudit.ru; RЭЦ program notes) |
| E-10 | https://zpm.new-site.space/ — TEST PLP snapshot (read-only) |

---

## Git status (this task)

| Item | Value |
|------|-------|
| Created | `projects/ocpilot/sites/site-002/reports/BZPM-M9.9-CTA-INTELLIGENCE-RESEARCH.md` |
| Code / TEST changes | **None** |
| Commit | **Not performed** |

---

*Research pack complete. Ready for M9.9 design/implementation charter after operator review of Option D locks and UNKNOWN resolution.*
