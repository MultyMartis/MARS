# REPORT — M9.16 DEALERS PAGE FORENSIC AND COMMERCIAL RESEARCH

**Milestone:** M9.16 — Dealers / Дилерам  
**Project:** SITE-002 / BZPM (ЗПМ)  
**Environment (read-only baseline):** https://zpm.new-site.space/  
**Production reference:** https://bzpm.ru *(parity **SAFE UNKNOWN**)*  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Status:** **RESEARCH COMPLETE**  
**Date:** 2026-06-22  
**Mode:** Research only — **no** design · **no** wireframe · **no** HTML/CSS/JS · **no** deploy · **no** implementation charter

**Forensic pass:** Live HTTP read + HTML capture `reports/m9.15-work/dealers-live-snippet.html` (2026-06-22). Competitor fetch: Kroner, Klen, Unitorg, Techno-TT dealers directory, Restoinox partners (partial), Abat partners (partial).

**Central page question:** «Почему мне выгодно работать с ЗПМ как дилеру или партнёру и как выглядит сотрудничество?»

---

## 1. Executive summary

| Field | Value |
|-------|--------|
| **Page role** | Primary **dealer / wholesale partner program** surface (CP-08) |
| **Canonical URL (TEST)** | `/dealers` |
| **Nav label** | «Дилерам» |
| **Research verdict** | **RESEARCH COMPLETE** — page fails commercial job today; IA role and cross-link map documented |
| **Implementation** | **Not started** · **not authorized** by this report |

### Key findings

| # | Finding | Severity |
|---|---------|----------|
| 1 | Страница **обещает форму**, но **формы на странице нет** — единственная рабочая форма живёт на PLP (`blockdealersform.twig`, `dialog=7`) | **Critical** |
| 2 | Контент — **generic `zpm-seo` scaffold** без dedicated CSS (в отличие от `/about` с `.about-page--*`) | High |
| 3 | **Нет коммерческих доказательств**: скидки, MOQ, территория, отсрочка, маркeting support — только общие обещания | **Critical** |
| 4 | **Нет channel policy**: продаёт ли завод напрямую конечникам? защита сделки дилера? | High |
| 5 | **Нет cross-links** в body к Payment / Delivery / About / Warranty / Contacts | Medium |
| 6 | Blueprint **CP-08** фиксирует `/dealers` как primary owner — текущая страница **не выполняет** эту роль | High |
| 7 | PLP dealer block и corp page **разорваны** — риск дублирования смыслов при redesign без единого charter | Medium |

---

## 2. Фактический URL и usage map

### 2.1 URLs

| Environment | URL | Status |
|-------------|-----|--------|
| **TEST (SITE-002)** | `https://zpm.new-site.space/dealers` | Verified live 2026-06-22 |
| **Production** | `https://bzpm.ru/dealers` | **SAFE UNKNOWN** — content parity not verified |

**Title (live):** «Дилерам и оптовым партнёрам | ООО «ЗПМ»»  
**Meta description:** сотрудничество с дилерами и оптовыми партнёрами; поставки для общепита и пищевых производств.

### 2.2 Navigation placement

Header top bar order (all corp captures):

1. `/custom-equipment` — Оборудование на заказ  
2. `/payment-methods` — Оплата  
3. `/delivery` — Доставка  
4. **`/dealers` — Дилерам**  
5. `/guarantee` — Гарантия  
6. `/about` — О компании  
7. `/blog/news` — Новости  
8. `/contact` — Контакты  

Same link: **footer** company links · **mobile offcanvas menu**.

**Evidence:** `dealers-live-snippet.html` · `footer.twig` captures · M9.15/M9.14 live snippets.

### 2.3 Usage map (inbound / outbound)

| Surface | Relationship to `/dealers` | Direction |
|---------|---------------------------|-----------|
| **Header / footer / mobile** | Persistent nav entry | Inbound |
| **PLP `zpm-dealers` block** | H2 «Дилерам и оптовикам» + long copy + **form** + btn «Подробнее» → `/dealers` | Inbound (high intent) · Outbound from PLP |
| **Homepage / `/katalog`** | Same PLP dealer block stack | Inbound |
| **M9.9 PLP FAQ Q12** | «Условия для дилеров / опта?» — should deep-link here | Planned inbound |
| **M9.9 Option D** | Secondary «Партнёрство» lane → `/dealers` | Planned inbound |
| **M9.15 Payment** | Bullet: опт/дилер — «порядок оплаты определяется условиями сотрудничества»; **no link** | Should outbound to Dealers |
| **PDP** | No full dealer form (CP-08 compliant); compact CTA secondary only | Low inbound today |
| **About** | Factory narrative — dealer channel deferred here | Cross-link outbound |
| **Contacts** | General sales contact — no dedicated dealer routing on page | Cross-link outbound |

**Blueprint CP-08:** «Дилерам» page = **primary**; header nav + PDP compact CTA = secondary; **never** full form on catalog pages *(post-charter: if corp page hosts primary form, PLP must suppress duplicate per merge design)*.

---

## 3. Текущая структура страницы (forensic)

**Template signal:** `<section class="zpm-seo" data-seo>` — generic OpenCart information scaffold. **No** `.dealers-page--*` CSS namespace in captured `style.css` (contrast: M9.13 About).

**Chrome:** breadcrumb · `page-intro` H1 «Дилерам» · global header/footer.

| # | Block (live) | Назначение | Смысл для дилера | Полезность |
|---|--------------|------------|------------------|------------|
| B0 | Breadcrumb «Главная → Дилерам» | Orientation | Minimal | OK |
| B1 | Page intro H1 «Дилерам» | Page title | Sets topic | Weak — no value prop |
| B2 | H2 «Сотрудничество с дилерами» + 2 paragraphs | Invitation + geography (РФ + СНГ) | «Завод ищет партнёров» | **Low** — generic, no proof |
| B3 | H3 «Кто может стать дилером» + UL (4 types) | Partner qualification sketch | «Подхожу ли я?» | **Medium** — useful segmentation start |
| B4 | H4 «Преимущества сотрудничества» + UL (4 bullets) | Value proposition | «Что получу?» | **Low–Medium** — claims without evidence |
| B5 | H4 «Как начать сотрудничество» + OL (3 steps) | Process | «Что делать дальше?» | **Broken** — step 1 references **form not on page** |

### Content inventory (verbatim structure)

**Partner types (B3):**

- торговые компании и поставщики оборудования для общепита  
- компании, занимающиеся оснащением ресторанов и кухонь  
- дистрибьюторы оборудования для пищевых производств  
- региональные поставщики оборудования для HoReCa  

**Benefits (B4):**

- прямые поставки от производителя  
- широкий ассортимент нейтрального оборудования  
- стабильные сроки производства и поставок  
- индивидуальные условия для партнёров  

**Process (B5):**

1. Отправьте заявку через форму на сайте.  
2. Менеджер свяжется для обсуждения условий.  
3. После согласования — КП и прайс-лист.  

**Absent on page:** form · phone/email for dealer desk · SLA · pricing framework · territory map · proof panel · cross-links · CTA button.

---

## 4. Что сейчас плохо

### 4.1 UX

| Issue | Impact |
|-------|--------|
| **Form promise broken** (step 1 vs no form) | Trust collapse at conversion moment |
| Flat heading hierarchy (H4 benefits/process under H3) | Weak scan path for B2B buyer |
| Generic prose wall — no visual anchors | Low engagement vs About dedicated layout |
| No in-page anchor targets for FAQ/PLP deep links | Breaks M9.9 Q12 intent |
| User arriving from PLP form sees **less** action capability than on PLP | Reverse funnel |

### 4.2 Доверие

| Issue | Impact |
|-------|--------|
| No OEM proof on page (production, certs, «Сделано в России») | «Перекуп?» objection (M9.9 Q1) unanswered |
| No existing partner signals / map / logos | «Есть ли сеть?» unanswered |
| No named contact or dealer desk | Anonymous program |
| Vague «выгодные условия» without bounds | Reads as marketing filler |

### 4.3 Коммерция

| Issue | Impact |
|-------|--------|
| No discount / price list / margin framework | Core dealer job-to-be-done blocked (M9.9 Role E) |
| No MOQ or volume tiers | Cannot evaluate economics |
| No payment terms summary (deferral, prepayment) | Forces call — OK if explicit, bad if silent |
| No marketing support inventory | Cannot compare vs Kroner/Klen |
| No assortment / line card entry point | Cannot assess line vs Restoinox/Kroner |

### 4.4 Дилерская логика

| Issue | Impact |
|-------|--------|
| **Channel policy missing** — direct factory sales vs dealer-only? | Top fear: «завод уведёт клиента» (M9.9 Role E) |
| No territory / exclusivity rules | Regional partner cannot assess conflict risk |
| No qualification criteria beyond partner types | Kroner/Klen ask ИНН, company, warehouse — ZPM does not |
| No distinction **дилер vs опт vs проектный партнёр** | Integrator and regional TC lumped together |
| PLP form (`dialog=7`) vs corp page split undocumented | Operator confusion on lead routing |

### 4.5 Доказательства

| Missing proof | Available elsewhere on site |
|---------------|------------------------------|
| Сертификаты | PLP certificates slider · About cert promo |
| Производство / завод | About page blocks |
| Склады / логистика | Delivery page (Барнаул + Москва) |
| НДС / юрлицо | Contacts · ATLAS E1 |
| Гарантия | `/guarantee` nav (content **SAFE UNKNOWN**) |
| Сделано в России | Header badge (not in dealers body) |

### 4.6 CTA

| Issue | Impact |
|-------|--------|
| **No primary CTA** on dedicated dealer page | Critical conversion gap |
| No secondary «позвонить / написать» with dealer routing | Fallback missing |
| No outcome promise (что получу после заявки + SLA) | M9.9 «outcome opacity» cluster |
| PLP carries form; corp page does not — **inverted ownership** vs user expectation |

---

## 5. Objection map — вопросы дилера

**Personas in scope:** дилер · региональный партнёр · торговая компания · интегратор · снабженец (opt channel) · корпоративный клиент (evaluating channel vs direct).

| # | Вопрос / возражение | Критичность | Закрыто сегодня? | Owner block (future IA) |
|---|---------------------|-------------|------------------|-------------------------|
| O1 | Это производитель или посредник? | Critical | **No** | Proof strip → About |
| O2 | Продаёте ли вы напрямую моим клиентам? | Critical | **No** | Channel policy |
| O3 | Какие **условия сотрудничества** (договор, статус партнёра)? | Critical | Partial (vague) | Program terms |
| O4 | Какие **скидки / дилерские цены**? | Critical | **No** | Commercial framework *(operator)* |
| O5 | Есть **прайс-лист** или только после формы? | High | Partial (step 3 promise) | Outcome + SLA |
| O6 | **MOQ** / минимальный объём заказа? | High | **No** | Commercial framework |
| O7 | **Территория** / эксклюзив / конфликт каналов? | High | **No** | Territory policy *(operator)* |
| O8 | **Наличие** / сроки производства / lead time? | High | Claim only («стабильные») | Ops proof → Delivery link |
| O9 | **Логистика** — откуда отгрузка, доставка в регион? | High | **No** on page | Summary + Delivery |
| O10 | **Документы** — УПД, сертификаты, паспорта для клиента? | High | **No** | Docs pack summary |
| O11 | **Гарантия** — срок, кто отвечает перед клиентом? | High | **No** | Summary + Warranty |
| O12 | **Производство** — мощности, кастом, серии? | Medium | **No** | Proof + Custom link |
| O13 | **Маркетинговая поддержка** — каталоги, образцы, совместные проекты? | Medium | **No** | Support inventory *(operator)* |
| O14 | **Оплата** — предоплата, отсрочка для партнёров? | High | **No** | Summary + Payment pointer |
| O15 | Что происходит **после заявки** и как быстро? | High | Partial | Process + SLA *(operator)* |
| O16 | Чем ЗПМ vs Restoinox / Techno-TT / Kroner в канале? | Medium | **No** | Differentiation facts *(operator)* |
| O17 | Можно ли **опт** без статуса дилера? | Medium | **No** | Partner type matrix |
| O18 | **Интегратор / проект** — спецификация, комплект, монтаж? | Medium | **No** | Link Custom + project lane |

**Cross-reference:** M9.9 FAQ Q12 «Условия для дилеров / опта?» — **High commercial value**; must resolve on this page, not PLP prose alone.

---

## 6. Какие доказательства партнёрства стоит показать

| Proof type | Why dealer cares | Site evidence today | Show on Dealers page? |
|------------|------------------|---------------------|------------------------|
| **Производство / завод** | OEM margin + supply stability | About CSS blocks; geo promo | **Summary + link About** — not full factory story |
| **Сертификаты / conformity** | Client tender + trust transfer | PLP cert slider (2 unique files in capture — data quality risk) | **Labeled types** + link to cert assets |
| **Сделано в России (СДС)** | Locality + procurement narrative | Header badge | **One labeled fact** — not ПП №719 substitute |
| **Реализованные поставки / кейсы** | «Кто уже возит» | **SAFE UNKNOWN** in repo | Only if operator provides |
| **Дилерская сеть / карта** | Social proof + territory clarity | **None** on ZPM | Optional map/logos *(operator)* |
| **Мощности / ассортимент** | Line card depth | Catalog breadth | **Category breadth facts** — not catalog dump |
| **Склад / отгрузка** | Regional supply | Delivery: Барнаул + Москва (ул. Басовская 14с2) | **2-point logistics summary** + Delivery |
| **Сроки** | Planning sales | Generic claim only | **Operator-locked ranges** or honest «по согласованию» |
| **Документы для клиента** | Dealer resell package | Contacts «документы для закупки» | **Bullet list of doc types** |
| **Гарантия производителя** | End-client warranty transfer | Kroner benchmark: 1 year stated | **Summary + Warranty** — term operator-locked |
| **Юр. надёжность** | Contracting | ATLAS E1 INN/OGRN/НДС 20% | **Trust fact row** — not full requisites |

**Rule:** Show **labeled, bounded facts** — not placeholders. Missing operator data → **SAFE UNKNOWN** in copy charter, not invented percentages.

---

## 7. Какие данные уже есть на сайте

### 7.1 On `/dealers` (live)

| Data | Present |
|------|---------|
| Partner type list | Yes |
| Generic benefits (4) | Yes |
| 3-step cooperation | Yes (broken form ref) |
| Form | **No** |
| Cross-links | **No** (nav only) |

### 7.2 On PLP dealer block (`blockdealersform.twig`)

| Data | Present |
|------|---------|
| H2 «Дилерам и оптовикам» | Yes |
| Long commercial paragraph | Yes |
| Link «Подробнее» → `/dealers` | Yes |
| Form: name, phone, email, message · `dialog=7` · POST `checkout/anketa` | Yes |
| Kroner-style fields (ИНН, company, city) | **No** |

### 7.3 Other site surfaces (reusable, not duplicated in full)

| Data | Source page / artifact |
|------|------------------------|
| Сертификаты (slider) | PLP / homepage |
| Сделано в России badge | Global header |
| Склады Барнаул + Москва | `/delivery` live snippet |
| TK list | `/delivery` |
| Shipment after payment (process) | `/delivery` |
| UL безнал / invoice flow | `/payment-methods` |
| Dealer payment deferral | Payment bullet only — detail **missing** |
| Entity INN/KPP/OGRN | `/contact/` polish capture |
| НДС 20% | ATLAS E1 — **not on Payment page body today** |
| Документы для закупки | Contacts trust list |
| Catalog assortment | Full catalog |
| Custom manufacturing | `/custom-equipment` nav |
| Guarantee | `/guarantee` nav — page body **SAFE UNKNOWN** |

---

## 8. Какие данные можно использовать из проекта

### 8.1 ATLAS (attested entity — not dealer terms)

**Source:** `ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md`

| Usable for trust row | Value |
|----------------------|-------|
| Legal entity | ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» |
| INN / KPP / OGRN | 2221237587 / 222101001 / 1172225049787 |
| НДС | 20%, общая система |
| Addresses | Барнаул, пр-т Калинина, 15в |
| Warehouse (CC) | Barnaul + Москва, ул. Басовская 14с2 |
| Phone | +7 (3852) 72-18-90 |

**ATLAS boundary:** Dealer discounts, deferral, MOQ, territory = **not in ATLAS**.

### 8.2 OCPilot / prior milestones

| Artifact | Usable for M9.16 |
|----------|------------------|
| `BZPM-M9.9-CTA-INTELLIGENCE-RESEARCH.md` | Role E objections; Kroner dealer benchmark; FAQ Q12; Option D secondary `/dealers` link; **do not** use «Дилерам» as default PLP headline |
| `BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md` | Factory narrative **secondary** — link, don’t duplicate |
| `BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md` | Logistics primary on Delivery; OQ-D04 dealer warehouse path |
| `BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md` | Channel payment on Dealers; Payment B10 pointer pattern; OQ-P05/P10 |
| `SITE-002-M9.8.9-03-CERTIFICATES-DEALERS-MERGE-FORENSIC-AND-DESIGN.md` | PLP form architecture; CP-08 merge constraints |
| `BZPM-BLUEPRINT-v1.md` CP-08 | Primary ownership rules |

### 8.3 Ready commercial proof points (with steward approval)

- Прямые поставки от производителя *(true if channel policy confirms)*  
- Нейтральное оборудование — широкий каталог *(catalog evidence)*  
- Склады: Барнаул + Московский регион *(Delivery)*  
- Поставки по РФ (+ СНГ in current copy — **confirm operator scope**)  
- После заявки: КП + прайс-лист *(process promise — add SLA when known)*  
- Работа с юрлицами / безнал *(Payment + entity)*  

---

## 9. Какие данные нужно запросить у клиента (OQ-D)

Only questions that **unblock credible dealer page** — not generic discovery.

| ID | Question | Blocks |
|----|----------|--------|
| **OQ-D01** | **Channel policy:** продаёт ли ЗПМ напрямую конечным клиентам? Если да — в каких случаях? Защита сделки дилера? | Channel policy block |
| **OQ-D02** | **Модели партнёрства:** дилер / оптовик / проектный партнёр / интегратор — отдельные условия или единая заявка? | Partner type matrix |
| **OQ-D03** | **Скидки / дилерская цена:** есть ли published framework (% tiers, от РРЦ, от опта)? Что можно показать публично vs только после NDA? | Commercial framework |
| **OQ-D04** | **MOQ** и минимальный первый заказ для статуса партнёра | Commercial framework |
| **OQ-D05** | **Территория:** эксклюзив, приоритет, или open network? Карта занятых регионов? | Territory block |
| **OQ-D06** | **Отсрочка / предоплата** для партнёров (связка с M9.15 OQ-P05) | Payment summary on Dealers |
| **OQ-D07** | **Прайс-лист:** выдаётся автоматически после заявки или после квалификации? Формат (PDF/XLS)? | Outcome promise |
| **OQ-D08** | **SLA:** срок ответа на заявку; срок выдачи КП/прайса | Process + CTA |
| **OQ-D09** | **Маркетинговая поддержка:** каталоги, образцы, совместные выезды, co-branding — что реально доступно? | Support inventory |
| **OQ-D10** | **Наличие / lead time** для партнёров: отличается ли от розницы? | Ops proof |
| **OQ-D11** | **Логистика партнёра:** самовывоз со складов, отгрузка на склад дилера, drop-ship клиенту? (M9.14 OQ-D04) | Logistics summary |
| **OQ-D12** | **Гарантия перед клиентом дилера:** срок, сервисная модель, кто принимает рекламацию | Warranty summary |
| **OQ-D13** | **Дилерская сеть:** можно ли публиковать список/карту действующих партнёров? | Social proof |
| **OQ-D14** | **Кейсы / реализованные поставки** для B2B proof — что можно показать? | Case block |
| **OQ-D15** | **Форма:** primary host = `/dealers` or PLP only? Какие поля обязательны (ИНН, компания, город — Kroner benchmark)? | Form + CP-08 merge |
| **OQ-D16** | **Routing:** отдельный email/менеджер дилерского отдела vs общий zakaz@? | CTA routing |
| **OQ-D17** | **СНГ:** актуальны ли заявки из СНГ в текущем copy? | Geo scope |
| **OQ-D18** | **Конкурентное позиционирование:** 3–5 фактов «чем ЗПМ в канале» (без marketing water) | Differentiation strip |

---

## 10. Конкурентный аудит (dealer / partner surfaces only)

**Method:** Live fetch 2026-06-22 + M9.9 competitor set. Scope: **не** PLP/catalog UX — только partner/dealer/cooperation pages.

| Peer | URL (dealer/partner) | Model | Strengths | Weaknesses / gaps |
|------|----------------------|-------|-----------|-------------------|
| **Kroner** | `kroner.pro/dealers/` | **Dealer-only channel** — no direct end clients | Explicit channel policy; benefits grid (support, marketing, warranty 1y); **existing dealers** section; qual form: ФИО, город, **компания, ИНН** | End buyer excluded by design — not ZPM model if direct sales exist |
| **Techno-TT** | `tehno-tt.ru/dealers/` | **Dealer directory** (find dealer by region) | Massive regional coverage; clear «buy through dealer» path | **Not a recruitment page** — weak for «стать дилером» intent |
| **Restoinox** | `restoinox.ru/company/partners/` | **Showcase of regional partners** (+ vacancy reveals dealer dept exists) | Real partner names/regions; OEM factory narrative elsewhere | **No public «стать дилером» program page**; recruitment via sales contact |
| **КЛЕН** | `klenmarket.ru/company/dealers/` | **Distributor** recruiting dealers | Rich benefits grid (deferral, discounts, POS, training, service); **qualification form** (сфера, стаж, павильон, склад) | Distributor not manufacturer — different trust story |
| **Юниторг** | `unitorg.ru/how-to-buy/dealers/` | **Regional integrator / sub-dealer** network | Numbered benefits: turnover discounts, deferral, 2-day warranty expertise, training | Manufacturer proxy — competes with ZPM as **channel alternative** not peer OEM page |
| **Abat** | `abat.ru/partners/` | Brand **partner showcase** | Nav cluster «Где купить»: sellers, showrooms, **sales policy**, blacklist | Partner page minimal in fetch; dealer recruitment **not central** |

### 10.1 Best practices to borrow (semantics, not layout)

1. **Explicit channel policy** first screen (Kroner) — answers O1/O2.  
2. **Benefits as labeled cards** with proof bounds (Kroner, Klen).  
3. **Qualification form** with company fields + ИНН (Kroner, Klen).  
4. **Partner requirements** visible before apply (Klen).  
5. **Existing network social proof** when available (Kroner, Restoinox partners).  
6. **Commercial terms skeleton** even if ranges are «по согласованию» (Unitorg structure).  
7. **Separate dealer desk contact** (Klen diler@ — pattern only).

### 10.2 Typical errors (ZPM shares several)

| Error | ZPM today | Peers mostly avoid |
|-------|-----------|-------------------|
| Generic prose without policy | **Yes** | Kroner/Klen lead with structure |
| Form promised, not delivered | **Yes** | — |
| No qualification fields | **Yes** | Kroner/Klen |
| Recruitment page = SEO text only | **Yes** | Kroner/Klen/Unitorg |
| Split form/page ownership | **Yes** (PLP form, empty corp page) | Kroner centralizes on `/dealers/` |

### 10.3 Missing opportunities on ZPM vs peers

- Channel policy statement  
- Marketing support inventory  
- Territory / network map  
- Warranty term for partner resale  
- Turnover-based discount framing (even without public %)  
- Project/custom lane for integrators (Restoinox/Kroner project support angle)

---

## 11. Три концепции страницы

### Concept A — «Channel Partnership Hub»

**Idea:** Страница = **политика канала + доказательства завода + коммерческая рамка + квалификационная заявка**. Ориентир по полноте: Kroner, адаптированный под модель ZPM (direct + dealer если подтверждено оператором).

| Strengths | Weaknesses |
|-----------|------------|
| Closes O1–O2, O3, O15 | Requires OQ-D01–D09 before publish |
| CP-08 primary owner done right | Longer page — needs strict IA |
| Supports all personas | Risk duplicating About if not disciplined |

**Подходит:** региональному партнёру · торговой компании · дилеру · integrator evaluating OEM channel.

---

### Concept B — «Minimal Program + Strong CTA»

**Idea:** Короткая program page: 1 экран ценности + 3 benefits + **форма с ИНН** + телефон дилерского отдела. Детали — в разговоре.

| Strengths | Weaknesses |
|-----------|------------|
| Fast to ship | Leaves O4–O7 open — weak vs Klen/Unitorg |
| Fixes form gap quickly | May feel «пусто» for experienced dealer |
| Low duplication risk | Underuses existing site proof assets |

**Подходит:** первичному контакту · небольшому региональному опту · быстрому lead capture.

---

### Concept C — «Partner Type Matrix»

**Idea:** Центральный объект — **матрица типов партнёра** (дилер / опт / проект / интегратор) с колонками: условия, документы, логистика, оплата, next step. Proof strip сверху; одна форма с selector типа.

| Strengths | Weaknesses |
|-----------|------------|
| Answers O2/O17/O18 clearly | Needs strict CP splits with Payment/Delivery |
| Strong for integrator + снабженец | Higher operator content burden |
| Reduces wrong-audience leads | UI complexity if terms not locked |

**Подходит:** торговой компании с несколькими каналами · интегратору · корпоративному снабженцу evaluating opt path.

---

## 12. Рекомендуемая концепция

**Recommendation: Concept A (Channel Partnership Hub) with a Partner Type Matrix block from Concept C (not the whole page).**

**Why:**

1. **Central question** requires **policy + proof + process**, not only a form (Concept B insufficient for Role E fears in M9.9).  
2. ZPM already has **distributed proof** on About/Delivery/Payment — Dealers page should **aggregate summaries + links**, not stay a prose stub.  
3. **CP-08** mandates `/dealers` as primary — Concept A is the only option that fully owns channel program semantics.  
4. Concept C’s matrix is the best device for **integrator vs dealer vs opt** without duplicating Payment/Delivery — but as **one IA block (B4)**, not the entire page (avoids Concept C dryness).  
5. Aligns with M9.15 pattern: **process + proof + cross-links**, operator-locked commercial cells.

**Not recommended alone:** B (conversion without trust for dealers); C alone (too matrix-heavy without OEM story).

**Blueprint note (documentation only):** CP-08 already exists; charter should add explicit **«channel payment terms summary on Dealers; detail on Payment one-line pointer»** mirroring M9.15 B10 inverse.

---

## 13. Предварительная IA страницы

**High-level block order only — no copy, no design, no wireframe.**

| # | Block | Purpose |
|---|-------|---------|
| **01** | Page intro | H1 + one-line scope («партнёрская программа производителя нейтрального оборудования») |
| **02** | Channel policy strip | Прямые продажи vs партнёрский канал; защита сделки *(OQ-D01)* |
| **03** | OEM proof row | Производитель · Сделано в России · certs · **links About** |
| **04** | Partner type matrix | Дилер / опт / проект / интегратор — кто подходит + что получает *(Concept C slice)* |
| **05** | Benefits grid | 4–6 labeled cards: прямые поставки, ассортимент, сроки, поддержка, docs — **bounded** |
| **06** | Commercial framework | Скидки/MOQ/territory — table or cells **operator-locked**; honest UNKNOWN labels pre-charter |
| **07** | Operations summary | Склады · наличие/lead time · **link Delivery** |
| **08** | Payment & documents summary | Партнёрская оплата · закрывающие · **link Payment** |
| **09** | Warranty & service summary | Срок · модель для дилера · **link Guarantee** |
| **10** | Marketing support inventory | Каталоги, образцы, co-sale — *(OQ-D09)* |
| **11** | Social proof (optional) | Карта/логотипы партнёров или кейсы *(OQ-D13/D14)* |
| **12** | Process timeline | Заявка → квалификация → КП/прайс → первый заказ + **SLA chip** |
| **13** | Primary CTA — qualification form | Company, ИНН, city, phone, email, partner type, comment *(OQ-D15)* |
| **14** | Secondary CTA | Dealer desk phone/email · **link Contacts** |
| **15** | FAQ micro-set (3–5) | Channel-only: territory, opt vs dealer, docs for client, direct sales — **not** PLP duplication |
| **16** | Custom / project pointer | One line + **link Custom Manufacturing** |

---

## 14. Cross-page logic

### Ownership matrix (recommended)

| Topic | Primary owner | On Dealers page |
|-------|---------------|-----------------|
| **Кто производитель / завод / история** | M9.13 About | Proof row summary + link |
| **Логистика, ТК, самовывоз, склады** | M9.14 Delivery | Ops summary B07 + link |
| **Безнал, счёт, НДС, закрывающие (розница/UL)** | M9.15 Payment | Partner payment summary B08 + link |
| **Канал: дилерские условия, opt, territory, MOQ** | **M9.16 Dealers** | Primary |
| **Гарантия / сервис** | M9.17 Warranty | Summary B09 + link |
| **Реквизиты / юр. карточка** | Contacts *(or Payment if operator chooses)* | Link only — not full bank block |
| **Нестандарт / проектное производство** | M9.18 Custom | Pointer B16 |
| **Сертификаты (полный набор)** | PLP slider / PDP docs | Labeled preview + link |
| **PLP dealer form** | Secondary per CP-08 | **Suppress or slim** once corp form is primary |

### Duplication risks to eliminate

| Risk | Mitigation |
|------|------------|
| «Прямые поставки от производителя» on About + Dealers + PLP | About = factory story; Dealers = **channel economics**; one sentence max overlap |
| Delivery tables on Dealers | Summary only; TK list stays on Delivery |
| Payment process OL duplicated | Dealers = partner payment **terms**; Payment = instruments + UL flow |
| PLP long dealer paragraph + full corp page | PLP = compact + link; corp = primary depth |
| Warranty legal text duplicated | One-line partner-facing summary |

### Link graph

```
PLP / FAQ Q12 / M9.9 partner lane ──► Dealers (primary)
Dealers ──► About      (OEM proof)
Dealers ──► Delivery   (logistics)
Dealers ──► Payment    (settlement)
Dealers ──► Guarantee  (service)
Dealers ──► Custom     (project partners)
Dealers ──► Contacts   (dealer desk / fallback)
Payment ──► Dealers    (channel terms pointer — M9.15 B10)
Delivery ──► Dealers   (optional: «условия для партнёров» if OQ-D11)
```

---

## Forensic gaps and research verdict

| ID | Gap | Severity |
|----|-----|----------|
| G-DE01 | Form on page missing vs copy | **Critical** |
| G-DE02 | No channel policy | **Critical** |
| G-DE03 | No commercial terms surface | **Critical** |
| G-DE04 | Generic template vs About quality gap | High |
| G-DE05 | PLP/corp split undocumented for operators | Medium |
| G-DE06 | `/guarantee` body not captured in repo | Medium |
| G-DE07 | Production `bzpm.ru/dealers` parity | Low until cutover |

| Field | Value |
|-------|--------|
| **M9.16 status** | **RESEARCH COMPLETE** |
| **Ready for** | Operator OQ-D01–D18 intake · design charter · CP-08 implementation planning |
| **Not ready for** | Implementation without operator locks on channel policy + commercial framework |
| **Blocked on (minimum)** | OQ-D01 · OQ-D03 · OQ-D05 · OQ-D08 · OQ-D15 |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Production `/dealers` content parity with TEST | **SAFE UNKNOWN** |
| Live `/guarantee` block structure | **SAFE UNKNOWN** — no HTML snapshot in repo |
| Exact dealer lead routing (`dialog=7` CRM semantics) | **SAFE UNKNOWN** |
| Public dealer network list / map | **SAFE UNKNOWN** |
| All commercial terms (discount %, deferral, MOQ, territory) | **SAFE UNKNOWN** — operator domain |
| Abat sales policy page content (fetch partial) | **SAFE UNKNOWN** |

---

## Evidence index

| Artifact | Role |
|----------|------|
| `reports/m9.15-work/dealers-live-snippet.html` | Primary live HTML capture |
| `reports/BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md` | Cross-page Payment boundary |
| `reports/BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md` | Logistics boundary · OQ-D04 |
| `reports/BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md` | Trust narrative boundary |
| `reports/BZPM-M9.9-CTA-INTELLIGENCE-RESEARCH.md` | Role E · Kroner · FAQ Q12 |
| `reports/SITE-002-M9.8.9-03-CERTIFICATES-DEALERS-MERGE-FORENSIC-AND-DESIGN.md` | PLP form forensic |
| `projects/website-factory/.../BZPM-BLUEPRINT-v1.md` | CP-08 |
| `projects/website-factory/.../BZPM-CORPORATE-PAGES-PROGRAM-v1.md` | Program registry |
| `projects/atlas/population/ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md` | Entity trust facts |
| Live: `https://kroner.pro/dealers/` | Competitor benchmark |
| Live: `https://www.klenmarket.ru/company/dealers/` | Competitor benchmark |
| Live: `https://www.unitorg.ru/how-to-buy/dealers/` | Competitor benchmark |
| Live: `https://www.tehno-tt.ru/dealers/` | Dealer directory pattern |

---

*M9.16 Dealers — research only. No design, no implementation, no deploy authorized.*
