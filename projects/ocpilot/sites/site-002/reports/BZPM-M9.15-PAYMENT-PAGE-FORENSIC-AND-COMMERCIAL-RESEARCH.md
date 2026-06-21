# REPORT — M9.15 PAYMENT PAGE FORENSIC AND COMMERCIAL RESEARCH

**Milestone:** M9.15 — Payment / Оплата  
**Project:** SITE-002 / BZPM (ЗПМ)  
**Environment (read-only baseline):** https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Status:** **RESEARCH COMPLETE**  
**Registration date:** 2026-06-22  
**Mode:** Research only — **no** design · **no** wireframe · **no** implementation · **no** deploy · **no** TEST/production changes

**Forensic pass:** Live HTTP read + HTML capture `reports/m9.15-work/payment-methods-live.html` (2026-06-22). Secondary captures: `delivery-live-snippet.html`, `dealers-live-snippet.html`.

---

## Executive summary

| Field | Value |
|-------|--------|
| **Page role** | Primary **payment terms and B2B settlement** surface for catalog buyers |
| **Canonical URL (TEST)** | `/payment-methods` |
| **Alternate URLs checked** | `/payment` → **404** · `/payment/` → **404** |
| **Nav label** | «Оплата» |
| **Research verdict** | **RESEARCH COMPLETE** — gaps, cross-page map, and IA concepts documented |
| **Implementation** | **Not started** · **not authorized** by this report |

### Key findings

| # | Finding | Evidence |
|---|---------|----------|
| 1 | Единственный рабочий URL — **`/payment-methods`**; алиас `/payment/` **не существует** | HTTP 200 vs 404 (2026-06-22) |
| 2 | Страница — **generic `zpm-seo` information scaffold** (как Delivery), без dedicated `.payment-page--*` CSS | Live HTML · `style.css` has `.zpm-seo` only, no payment namespace |
| 3 | Контент **описательный**, но **не доказывает** процесс: нет сроков счёта, НДС, предоплаты, закрывающих документов, банковских реквизитов | Live content audit §2–3 |
| 4 | Упоминание **оплаты картой через платёжный сервис** — **не подтверждено** runtime checkout (OpenCart: `cod`, `free_checkout`) | `SITE-002-BASELINE-v1.md` |
| 5 | В Commercial Trust FAQ на PLP **нет** карточки про оплату/безнал (в отличие от доставки) | `m9.8.9-09b-work/plain.html` |
| 6 | Blueprint имеет CP-07 (Delivery) и CP-08 (Dealers), но **нет явного CP для Payment** — риск дублирования с Delivery/Dealers | `BZPM-BLUEPRINT-v1.md` |
| 7 | ATLAS E1 содержит **полные банковские реквизиты и НДС 20%** — на сайте **не опубликованы** (Contacts polish explicitly omitted bank) | ATLAS EV-W1B-CC-01 · `SITE-002-CONTACTS-PAGE-POLISH-V1.md` |

---

## 1. Фактический URL и usage map

### 1.1 URL resolution

| URL | HTTP | Role |
|-----|------|------|
| `https://zpm.new-site.space/payment-methods` | **200 OK** | **Canonical** corporate payment page |
| `https://zpm.new-site.space/payment` | **404** | Not routed |
| `https://zpm.new-site.space/payment/` | **404** | Not routed |
| `https://bzpm.ru/payment-methods` | **404** (2026-06-22) | Production parity **SAFE UNKNOWN** |

**OpenCart route (expected):** `information/information` with SEO keyword `payment-methods` — **SAFE UNKNOWN** (no dedicated twig in MARS git tree; same pattern as M9.13/M9.14).

**Title / meta (live):**

| Element | Value |
|---------|--------|
| `<title>` | Варианты оплаты \| ООО «ЗПМ» |
| H1 (page-intro) | Оплата |
| Breadcrumb current | Оплата |
| Meta description | Безнал для юрлиц + карта «в предусмотренных случаях» |

### 1.2 Navigation and inbound links

| Surface | Link | Label | Status |
|---------|------|-------|--------|
| Header top bar | `/payment-methods` | Оплата | Present (all captures) |
| Footer company links | `/payment-methods` | Оплата | Present |
| Mobile offcanvas menu | `/payment-methods` | Оплата | Present |
| QA baselines M7.1–M9.7E | `/payment-methods` | — | Listed in `qa-snapshot.json` |

**Evidence:** `m7.1-launch-mode-work/.../header.twig` · `footer.twig` · `offcanvasmenu.twig` · `empty-category-audit-data.json`

### 1.3 Outbound / secondary usage (catalog layer)

| Surface | Payment behaviour | Status |
|---------|-------------------|--------|
| PDP hero / commercial zone | Dedicated payment summary + link | **NOT FOUND** in repo twig captures |
| PLP card micro-strip | Payment hint | **NOT FOUND** (analog: `p-card__delivery` often empty) |
| Commercial Trust FAQ (PLP) | Payment Q&A card | **ABSENT** — delivery card present, payment absent |
| Commercial Trust benefits | «Документы для закупки» | Present — **adjacent trust**, not payment mechanics |
| Contacts `/contact/` | Legal requisites panel (no bank) | Delivered workstream — separate from M9.15 |
| Cart / checkout | Online payment gateway | **Catalog-mode** checkout modules: `cod`, `free_checkout` only |
| Program registry | M9.15 owner | `BZPM-CORPORATE-PAGES-PROGRAM-v1.md` |

### 1.4 Role in trust and sales

| Buyer stage | Payment page function |
|-------------|----------------------|
| **Pre-RFQ validation** | «Можно ли работать по безналу с нашим юрлицом?» — partial answer today |
| **Post-quote / pre-payment** | «Как получить счёт и что будет после оплаты?» — weak procedural proof |
| **Procurement file build** | «Есть ли реквизиты, НДС, закрывающие?» — **mostly unanswered** on page |
| **Dealer qualification** | «Как платят партнёры?» — deferred to `/dealers` one line only |
| **Risk reduction** | Reduces «серая схема / перекуп» fear when paired with entity proof (About + Contacts) |

**Commercial weight:** High for **снабженец / закупщик / owner** on first B2B deal; medium for repeat buyers who already have account terms.

**Program position:** First corporate page in program still requiring research — now **Research Complete**; implementation **not authorized**.

---

## 2. Текущая структура страницы

### 2.1 Page scaffold

| Layer | Implementation |
|-------|----------------|
| Global chrome | Standard ZPM header / footer / modals (callback, price, cart) |
| Breadcrumb | Главная → Оплата |
| Page intro | `<section class="page-intro">` — H1 «Оплата» |
| Main body | `<section class="zpm-seo" data-seo>` — CMS HTML inside container |
| Dedicated payment CSS block | **NOT FOUND** — uses shared `.zpm-seo` typography/table styles |
| In-page CTA | **NONE** (no form, no «получить счёт», no link to `/contact`) |
| Internal cross-links in body | **NONE** to Delivery / Dealers / Contacts |

### 2.2 Content inventory (what visitor actually receives)

| Block order | Element | Content role |
|-------------|---------|--------------|
| 1 | `<blockquote>` | Manager clarifies order → agrees payment terms; serial vs custom may differ |
| 2 | H2 «Способы оплаты» | Works with individuals + orgs; cashless + card «in allowed cases» |
| 3 | H3 «Варианты оплаты» | UL: юрлица → счёт; физлица → карта if available; custom → individual; dealer/wholesale → cooperation terms |
| 4 | Paragraph | After agreement → payment info; cashless → invoice with requisites |
| 5 | H4 «Как проходит оплата» | OL 4 steps: request → clarify → invoice/link → work/reserve/ship after payment |
| 6 | H4 «Основные условия оплаты» | Table 4 rows: UL cashless; FL card; custom individual; invoice term «by agreement» |
| 7 | H5 «Оплата для юридических лиц» | Repeat: cashless, invoice with equipment + cost + requisites |
| 8 | H6 «Дополнительная информация» | Generic «contact managers before confirming order» |

### 2.3 Heading hierarchy issue (forensic)

Live page uses **H2 → H3 → H4 → H4 → H5 → H6** inside one SEO block. Semantically readable, but **H5/H6 for substantive sections** signals template filler rather than industrial-grade IA.

### 2.4 What visitor does **not** receive

- Bank / settlement requisites (р/с, БИК, банк)
- Explicit **НДС / без НДС** statement
- **Prepayment %** or staged payment for custom equipment
- **Invoice validity period** (e.g. 3 banking days — industry pattern)
- **Closing documents** list (счёт, УПД/акт, счёт-фактура)
- **Contract / specification** mention for custom or large orders
- **Post-payment SLA** (when production starts)
- Link to **Delivery** for «отгрузка после оплаты»
- Link to **Dealers** for channel payment
- Distinction **cart checkout vs invoice-led B2B** (M9.9 Q21)

---

## 3. Что сейчас плохо

### 3.1 Unanswered buyer questions

| Question (role) | Current page | Gap severity |
|-----------------|--------------|--------------|
| Работаете с юрлицами и безналом? (закупщик) | Said yes — generic | Low — stated but thin |
| Какой % предоплаты на «под заказ»? (снабженец) | «Индивидуально» | **High** |
| Срок действия счёта? (закупщик) | «По согласованию» | **High** |
| НДС 20% в счёте? (закупщик / owner) | **Not stated** | **High** |
| Какие закрывающие документы? (закупщик) | **Not stated** | **High** |
| Можно ли оплатить картой онлайн с сайта? (owner) | Claimed «if available» | **Medium** — **conflicts with checkout evidence** |
| Отсрочка / post-payment? (owner / dealer) | **Not stated** | **Medium** — **SAFE UNKNOWN if offered** |
| Как связаны оплата и отгрузка? (логист) | One step in OL only | Medium — Delivery page owns detail but **no cross-link** |
| Условия для дилеров? (dealer) | One bullet → `/dealers` not linked | Medium |

### 3.2 Client risks left on table

| Risk | Why it persists |
|------|-----------------|
| **Procurement stall** | Buyer cannot complete vendor card without bank/VAT/docs |
| **Trust gap vs «формальная страница»** | Repetitive copy, no proof artifacts, no CTA |
| **Expectation mismatch on card payment** | Text promises card; catalog checkout is not ecommerce payment stack |
| **Hidden terms** | «По согласованию» everywhere — reads as opaque B2B |
| **Duplicate mental model with Delivery** | Both describe post-payment production/ship steps without boundary |

### 3.3 Formal / weak elements

| Element | Issue |
|---------|--------|
| Blockquote intro | Reads like SEO preamble, not operational policy |
| Repeated «менеджер выставит счёт» | 3× paraphrase — **formal filler** |
| Table «Срок оплаты счета → По согласованию» | No operational anchor |
| H6 «Дополнительная информация» | Generic defer-to-manager — **conversion dead-end** |
| No visual trust layer | Unlike About (media blocks) or Delivery (TK table) — **flat prose only** |
| og:image empty | Weak share/preview signal |

### 3.4 Architectural gaps (repo)

| Gap | Impact |
|-----|--------|
| No CP-XX Payment ownership in blueprint | Cross-page duplication risk with M9.14/M9.16 |
| No PLP FAQ payment card | M9.9 Q13 not in conversion TOP-8 |
| No PDP payment micro-summary | CP-01 pattern not extended to payment |
| Bank requisites omitted from Contacts polish scope | Payment page cannot link to authoritative on-site block |

---

## 4. Какие вопросы должна закрывать страница оплаты

### 4.1 Снабженец

| Must answer | Why |
|-------------|-----|
| Безнал с нашего юрлица — да/как | Default B2B path |
| Как получить счёт на N позиций | Multi-SKU RFQ → КП → счёт |
| Предоплата / этапы для серийного vs «под заказ» | Production gate |
| Срок счёта и резерв | Avoid line stop |
| Закрывающие документы под нашу учётную политику | ERP onboarding |
| Отгрузка только после оплаты? | Handoff to Delivery (link, not duplicate) |

### 4.2 Закупщик

| Must answer | Why |
|-------------|-----|
| Работа с ООО/ИП, НДС | Tender / vendor registry |
| Договор / спецификация — когда нужны | Custom & volume |
| Реквизиты для внесения в ERP | **Primary blocker today** |
| ЭДО — если используется | **SAFE UNKNOWN** — page should not invent |
| Соответствие суммы счёта КП | Audit trail |

### 4.3 Дилер

| Must answer | Why |
|-------------|-----|
| Оплата по дилерским условиям — **не на этой странице целиком** | CP-08: Dealers primary |
| Summary: «канальные условия → `/dealers`» | Avoid duplicate |
| Минимальная модель: предоплата / отсрочка для партнёров | **Operator input required** |

### 4.4 Владелец бизнеса

| Must answer | Why |
|-------------|-----|
| Понятный путь «заявка → счёт → оплата → производство/отгрузка» | Reduces fear of opaque deal |
| Можно ли без онлайн-оплаты | Catalog is quote-led |
| Карта / физлицо — реально или исключение | Align promise with runtime |
| К кому звонить по оплате | CTA to sales / contacts |

### 4.5 Производственное предприятие (food plant)

| Must answer | Why |
|-------------|-----|
| Оплата по спецификации проекта / комплекта | Large capex |
| Документы для внутреннего согласования capex | Parallel to закупщик |
| Связка оплаты со сроками изготовления линии | Links Custom Equipment + Delivery |

---

## 5. Какие доказательства оплаты стоит показать

**Rule:** Only patterns **confirmed in industry** or **attested for BZPM** — no invented terms.

### 5.1 Confirmed industry patterns (food equipment B2B)

| Proof type | Pattern | Source class |
|------------|---------|--------------|
| **Безналичный расчёт** | Primary B2B method; invoice by email | Techno-TT `/about/howto/` — «только безнал»; Abat-ural PDP blocks |
| **Счёт на оплату** | Manager sends invoice; pay via bank / i-bank | Abat-ural: 3 banking days validity, reissue if expired |
| **Отгрузка после поступления ДС** | Standard manufacturer/dealer rule | Abat-ural payment blocks |
| **Договор поставки** | For non-stock / custom — prepayment in contract | Abat-ural custom-stock path |
| **Работа с юрлицами** | Explicit statement | Techno-TT — UL only |
| **Закрывающие документы** | Expected in B2B procurement (УПД/акт/SF) | General B2B practice — **not on competitor pages verbatim**; show only if operator confirms |
| **НДС** | Stated tax regime for UL buyers | ATLAS attests **Общая, НДС 20%** for BZPM legal entity |
| **Предоплата custom** | Negotiated prepayment before production | Abat-ural «условие предоплаты в договоре» |

### 5.2 Patterns to use cautiously

| Pattern | Note |
|---------|------|
| **Онлайн-оплата картой** | Common at **dealers**; **OEM catalog sites** often **invoice-first** (Techno-TT: no card). ZPM text mentions card — **must align with operator + checkout reality** |
| **Отсрочка** | Sometimes offered to dealers — **SAFE UNKNOWN for ZPM** |
| **ЭДО** | Increasingly expected — **not in ATLAS CC extract** |
| **Госзакупка / 44-ФЗ** | Separate tender logic — **not payment page core** unless operator directs |

### 5.3 Recommended proof bundle (pending operator lock)

1. **Entity + tax posture** — ООО ЗПМ, работаем с юрлицами, НДС 20% (if confirmed unchanged)  
2. **Settlement instruments** — безнал по счёту; optional FL/card if **explicitly offered**  
3. **Process proof** — 4–6 step timeline with **named artifacts** (КП → счёт → оплата → закрывающие → отгрузка)  
4. **Requisites reference** — full bank block **or** link to authoritative Contacts section (single owner per CP-01)  
5. **Scenario matrix** — серия / под заказ / дилер / физлицо  
6. **Cross-links** — Delivery (after payment), Dealers (channel), Contacts (questions)

---

## 6. Какие данные уже есть на сайте

**Facts only — from repo captures and 2026-06-22 live HTML.**

### 6.1 On `/payment-methods` (live)

| Data | Present |
|------|---------|
| Works with individuals and organizations | Yes |
| UL: cashless via invoice | Yes |
| FL: card if available for order | Yes (claim) |
| Custom: individual terms | Yes |
| Dealer/wholesale: per cooperation | Yes (no link) |
| 4-step payment process | Yes |
| Summary table (4 rows) | Yes |
| Bank requisites | **No** |
| VAT statement | **No** |
| Prepayment % | **No** |
| Invoice validity days | **No** |
| Closing documents | **No** |
| In-page CTA | **No** |

### 6.2 On `/contact/` (contacts polish capture)

| Data | Present |
|------|---------|
| Legal name ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | Yes |
| INN 2221237587 | Yes |
| KPP 222101001 | Yes |
| OGRN 1172225049787 | Yes |
| Legal / actual address (Барнаул) | Yes |
| Bank / settlement account | **No** — polish scope omitted |
| Phone 8 (3852) 72-18-90 | Yes (header/footer/contacts) |
| «Документы для закупки» trust fact | Yes (summary list) |

### 6.3 On `/delivery` (live snippet)

| Data | Present |
|------|---------|
| Shipment after payment (step 1 of delivery flow) | Yes — **payment-adjacent** |
| Warehouses Barnaul + Moscow region partner | Yes |
| TK list (ДЛ, ПЭК, etc.) | Yes |
| Payment mechanics | **No** (correct separation intent) |

### 6.4 On `/dealers` (live snippet)

| Data | Present |
|------|---------|
| Partner benefits, start cooperation steps | Yes |
| Payment / prepayment / deferral terms | **No** |
| Link back to payment page | **No** (nav only) |

### 6.5 Catalog / platform

| Data | Source |
|------|--------|
| OpenCart payment extensions: `cod`, `free_checkout` | `SITE-002-BASELINE-v1.md` |
| Site type: catalog + RFQ, not ecommerce runtime | Blueprint / WF-R01 posture |
| Footer offer disclaimer (prices not public offer) | Footer on all pages |
| M9.9 buyer Q13 «юрлица и безнал» | Research — **not surfaced on PLP FAQ** |

---

## 7. Какие данные можно использовать из проекта BZPM и ATLAS

### 7.1 ATLAS E1 — attested (usable with steward approval for publish)

**Source:** `ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md` · EV-W1B-CC-01 (`bzpm/Реквизиты.docx` in STORAGE)

| Field | Attested value |
|-------|----------------|
| Legal entity | ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» |
| INN / KPP / OGRN | 2221237587 / 222101001 / 1172225049787 |
| Addresses | 656011, Барнаул, пр-т Калинина, 15в, оф. 110 |
| Tax system | **Общая, НДС 20%** |
| Bank | ПАО Сбербанк, Алтайское отделение № 8644, г. Барнаул |
| Settlement account | 40702810802000017761 |
| BIC | 040173604 |
| Correspondent account | 30101810200000000604 |
| Signatory | Крюков Александр Сергеевич |
| Email (CC) | zakaz@bzmp.ru *(typo bzmp vs bzpm — recorded as-is in ATLAS)* |
| Phone | +7 (3852) 72-18-90 |
| Warehouse (CC §14) | Barnaul + Москва, ул. Басовская 14с2 |

**ATLAS boundary:** Payment **terms** (prepayment %, deferral, invoice SLA) are **not** in ATLAS — accounting/operator domain per `ATLAS-BOUNDARIES-v1.md`.

### 7.2 BZPM project / blueprint (documented architecture)

| Artifact | Usable for M9.15 |
|----------|------------------|
| `BZPM-CORPORATE-PAGES-PROGRAM-v1.md` | Milestone scope, URL `/payment-methods` |
| `BZPM-M9.9-CTA-INTELLIGENCE-RESEARCH.md` | Buyer Q13, Q21; persona fears; competitor payment patterns |
| `BZPM-BLUEPRINT-v1.md` CP-01 | Single primary surface per fact type — **recommend CP for Payment** |
| `BZPM-BLUEPRINT-v1.md` CP-07 / CP-08 | Boundaries with Delivery / Dealers |
| `REPORT-BZPM-CATALOG-IMPROVEMENT-BACKLOG.md` | B2B lead capture without online payment |
| Contacts delivery reports | Requisites panel pattern — extend or link, not duplicate blindly |

### 7.3 Not usable without operator

| Data | Reason |
|------|--------|
| Exact prepayment % by product class | Commercial terms — not attested |
| Deferral for dealers | **SAFE UNKNOWN** |
| EDO operator | **SAFE UNKNOWN** in CC |
| Live card acquirer / payment gateway | Not in baseline modules |
| Production `bzpm.ru` payment URL/content | Not verified live |

---

## 8. Какие данные желательно запросить у клиента

Operator questionnaire to close **UNKNOWN** before implementation charter:

| ID | Question | Blocks |
|----|----------|--------|
| OQ-P01 | Публикуем **полные банковские реквизиты** на сайте? На Payment, Contacts, или оба с single-owner link? | Requisites block |
| OQ-P02 | Актуальная **налоговая позиция** для счетов (НДС 20% / изменения)? | UL procurement |
| OQ-P03 | **Предоплата %** для: (a) серия в наличии, (b) серия под заказ, (c) custom equipment | Scenario matrix |
| OQ-P04 | **Срок действия счёта** (банковские дни) и политика перевыставления | Process proof |
| OQ-P05 | **Отсрочка платежа** — есть ли стандарт для UL / только дилеры? | Owner/dealer |
| OQ-P06 | **Оплата картой / онлайн** — реально доступна? Для кого? Через какой канал? | Align with checkout copy |
| OQ-P07 | **Наличные / оплата в офисе** — доступны? | FL / regional buyers |
| OQ-P08 | **Пакет закрывающих документов** (счёт, УПД, SF, договор, спецификация) | Закупщик |
| OQ-P09 | **ЭДО** — используете? Какой оператор? | Enterprise buyers |
| OQ-P10 | **Дилерские условия оплаты** — что stays on `/dealers` vs summary on Payment? | Cross-page |
| OQ-P11 | **Связка с 1C** — счёт автоматически или только менеджер? | Process timeline |
| OQ-P12 | **Контакт для оплат** (email zakaz@ / отдельный бухгалтерский)? | CTA routing |
| OQ-P13 | **Госзакупки** — нужен ли отдельный абзац или out of scope? | Tender segment |

---

## 9. Лучшие паттерны производителей пищевого оборудования

**Method:** M9.9 competitor set + live fetch 2026-06-22 + distributor reference blocks.

### 9.1 OEM / manufacturer patterns

| Peer | Payment approach | Strength |
|------|------------------|----------|
| **Techno-TT** | `/about/howto/` — ultra-short: **безнал only**, **UL only** | Clarity; zero ambiguity |
| **Techno-TT** | FAQ hub for order lifecycle (mixed B2C noise) | Depth for self-serve — but not PLP |
| **Kroner** | End buyer → dealers; payment terms **implicit in channel** | Clean IA when direct sales excluded |
| **Abat (manufacturer site)** | Policy pages in nav; production change disclaimers | Institutional tone |

### 9.2 Strong B2B **commercial** patterns (often dealers, applicable as process reference)

| Peer | Pattern | Relevance to ZPM |
|------|---------|------------------|
| **Abat-ural / regional integrators** | PDP/footer blocks: безнал + office card/cash; **3-day invoice**; ship **after funds**; **contract + prepayment** for non-stock | **Best operational detail model** for Payment IA |
| **Restoinox** | Project/spec procurement language in SEO — payment implied via manager | Spec-led buying |
| **Юниторг** | Project + logistics in meta; payment via consult | Integrator model |

### 9.3 Cross-cutting commercial approach (not only «страница Оплата»)

| Pattern | Observation |
|---------|-------------|
| **Invoice-first B2B** | Strong OEMs do not center online card checkout |
| **Process > marketing** | Tables, timelines, validity rules outperform prose |
| **Persona split** | UL / FL / dealer / custom — separate rows, shared footer CTA |
| **Single CTA** | «Получить счёт / КП» or phone — not orphan info page |
| **Cross-link logistics** | Payment page ends with «what happens after pay» → Delivery |
| **Requisites proximity** | Bank details near payment — or one click to Contacts |

### 9.4 Anti-patterns observed on ZPM today

| Anti-pattern | Peer contrast |
|--------------|---------------|
| «По согласованию» without ranges | Abat-ural: concrete 3-day rule |
| Card promise without checkout | Techno-TT: no card promise |
| No FAQ on PLP for payment | M9.9 defer list includes order flow — Payment should own slice |
| Repeated manager deferral | Techno-TT / integrators: named steps |

---

## 10. Три концепции новой страницы

**No design — IA / narrative strategy only.**

### Concept A — «B2B Payment Process Hub»

**Idea:** Страница как **операционный маршрут** от заявки до старта производства/отгрузки, с разрезом по типам покупателя.

| Pros | Cons |
|------|------|
| Закрывает вопрос «как платить» end-to-end | Требует больше operator-locked цифр (%, сроки) |
| Соответствует снабженец/закупщик mental model | Без цифр риск остаться «как сейчас, но красивее» |
| Natural cross-links to Delivery / Dealers | Больше контент-объём |
| Matches Abat-ural / industrial distributor best practice | |

### Concept B — «Trust & Compliance Sheet»

**Idea:** Узкая страница **доказательств**: юрлицо, НДС, реквизиты, закрывающие, без длинного процесса.

| Pros | Cons |
|------|------|
| Быстро закрывает procurement checklist | Слабо отвечает «что будет после заявки» |
| Минимум UNKNOWN exposure | Мало дифференциации vs Contacts requisites |
| Легко поддерживать | Owner/dealer scenarios under-served |
| | Weak conversion story |

### Concept C — «Scenario Matrix First»

**Idea:** Центральный объект — **матрица сценариев** (серия / под заказ / дилер / физлицо) с колонками: инструмент оплаты, предоплата, документы, срок, next step.

| Pros | Cons |
|------|------|
| Scannable for expert buyers | Matrix empty cells if operator data missing |
| Reduces prose duplication | Less narrative for owner persona |
| Strong for закупщик audit | Requires strict CP-01 splits with Dealers |
| | Harder mobile IA without design pass |

---

## 11. Рекомендуемая концепция

**Recommendation: Concept A (B2B Payment Process Hub)** as primary spine, with **Concept B proof layer** embedded (not a separate page).

**Why:**

1. **Core user question** («как я могу оплатить… понятно, безопасно, удобно») is **process + proof**, not requisites alone.  
2. ZPM is **manufacturer + catalog RFQ**, not UL-only shop — needs **scenario split** (A) more than minimal Techno-TT sheet, but with **concrete operator facts** to avoid today’s «по согласованию» trap.  
3. **Matrix elements from C** should appear as **one block inside A**, not as the whole page.  
4. **Requisites / VAT** — short **attested block or link** to Contacts (single owner) satisfies procurement without duplicating Contacts redesign.  
5. Aligns with **CP-01**: Payment = primary for settlement mechanics; Delivery gets «after payment» handoff link only.

**Not recommended alone:** B (too thin for owner), C (too dry without process story).

**Blueprint follow-up (documentation):** Propose **CP-09b or new CP** — «Payment terms: `/payment-methods` primary; PDP/FAQ one-line secondary; Dealers owns channel terms.» *(Program note — not a blueprint edit in this task.)*

---

## 12. Предварительная структура блоков

**High-level IA only — no copy, no design, no wireframe.**

| # | Block | Purpose |
|---|-------|---------|
| B1 | Page intro | H1 + one-line scope («условия оплаты оборудования ЗПМ для B2B и частных заказчиков») |
| B2 | Positioning strip | Manufacturer invoice-led model vs marketplace; works with UL/ИП |
| B3 | Buyer-type selector (logical) | UL · ИП · FL · Custom · Dealer — **dealer row links out** |
| B4 | Payment instruments | Cashless (primary); card/cash **only if operator confirms** |
| B5 | Process timeline | Request → КП/согласование → счёт → оплата → подтверждение → производство/резерв |
| B6 | Conditions matrix | Prepayment · invoice validity · VAT · closing docs — **cells operator-locked** |
| B7 | Documents & compliance | What buyer receives; link to certs/docs policy (PDP/About) |
| B8 | Requisites zone | Full bank **or** «полные реквизиты → Contacts» (single source) |
| B9 | After payment handoff | One paragraph + **link to Delivery** (shipment trigger) |
| B10 | Dealer channel pointer | Summary + **link to Dealers** (no channel terms duplicate) |
| B11 | FAQ micro-set | 3–5 payment-only questions (not PLP duplication) |
| B12 | Contact CTA | Phone / form / email for «выставить счёт» |

**Optional secondary surfaces (post-charter, not this page body):**

- PLP FAQ card: «Работаете с юрлицами и безналом?» → `/payment-methods`  
- PDP commercial zone: one-line + link (CP-01 secondary)

---

## Cross-Page Logic

### Ownership matrix (recommended)

| Topic | Primary owner | Secondary (summary + link only) |
|-------|---------------|----------------------------------|
| **Как оплатить / счёт / безнал / НДС / закрывающие** | **M9.15 Payment** | Contacts (requisites display if chosen there) |
| **Отгрузка, ТК, самовывоз, регионы** | M9.14 Delivery | Payment B9 handoff «после оплаты» |
| **Условия дилеров, опт, партнёрская модель** | M9.16 Dealers | Payment B10 pointer |
| **Кто производитель / доверие к заводу** | M9.13 About | Payment B2 one line max |
| **Гарантия / сервис** | M9.17 Warranty (`/guarantee` nav) | Not on Payment |
| **Оборудование на заказ** | M9.18 Custom | Payment scenario row «custom» |
| **Юр. реквизиты организации** | **Contacts** *(today partial)* or Payment B8 if operator chooses Payment as primary for bank | Must be **one canonical surface** |
| **Публичная оферта / цены** | Footer disclaimer + legal pages | Payment must not restate offer law |

### Duplication risks to eliminate

| Risk | Mitigation |
|------|------------|
| Delivery step «После оплаты…» vs Payment timeline | Delivery keeps logistics; Payment owns **payment confirmation → internal status**; cross-link |
| Dealers «индивидуальные условия» vs Payment dealer bullet | Move channel payment detail to Dealers; Payment = one sentence + link |
| Contacts requisites vs Payment requisites | Pick **one primary bank block**; other page links |
| PLP FAQ payment vs Payment page | FAQ = one card + link; full answer on Payment |
| Card payment claim vs checkout | Operator decision OQ-P06; align all surfaces |

### Logical link graph (intent)

```
Catalog / PDP / PLP FAQ ──► Payment (primary)
Payment ──► Delivery   («после оплаты — отгрузка»)
Payment ──► Dealers    (канал)
Payment ──► Contacts   (реквизиты / вопрос по счёту)
Payment ──► Custom     (сценарий «под заказ»)
About ──► Payment      (optional trust footer link — not reverse duplicate)
```

---

## Forensic gaps and research verdict

| ID | Gap | Severity |
|----|-----|----------|
| G-P01 | Card / online payment vs checkout modules mismatch | **High** |
| G-P02 | No bank requisites on site payment path | **High** |
| G-P03 | No blueprint CP for Payment ownership | Medium |
| G-P04 | No PLP/PDP secondary payment surface | Medium |
| G-P05 | Production URL parity unknown | Low (until prod cutover) |

| Field | Value |
|-------|--------|
| **M9.15 status** | **RESEARCH COMPLETE** |
| **Ready for** | Operator OQ-P01–P13 intake · design charter · proposed CP payment rule |
| **Not ready for** | Implementation without operator locks on commercial terms |
| **Blocked on** | OQ-P01–P06 minimum for credible redesign |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| OpenCart `information_id` for payment page | **SAFE UNKNOWN** |
| Historical copy author / CMS edit workflow | **SAFE UNKNOWN** |
| Live card acquirer if any | **SAFE UNKNOWN** |
| Deferral / dealer prepayment standards | **SAFE UNKNOWN** |
| EDO usage | **SAFE UNKNOWN** |
| `bzpm.ru` payment page at go-live | **SAFE UNKNOWN** |
| Operator-approved payment terms document outside site | **SAFE UNKNOWN** |

---

## Evidence index

| Artifact | Role |
|----------|------|
| `reports/m9.15-work/payment-methods-live.html` | Live forensic capture 2026-06-22 |
| `reports/m9.15-work/delivery-live-snippet.html` | Cross-page delivery overlap |
| `reports/m9.15-work/dealers-live-snippet.html` | Dealer overlap |
| `reports/contacts-polish-work/qa-contact-polish.html` | On-site requisites scope |
| `reports/SITE-002-CONTACTS-PAGE-POLISH-V1.md` | Bank omitted from contacts scope |
| `reports/SITE-002-BASELINE-v1.md` | Payment modules `cod`, `free_checkout` |
| `reports/BZPM-M9.9-CTA-INTELLIGENCE-RESEARCH.md` | Buyer Q13/Q21; competitors |
| `reports/BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md` | CP-07; delivery ownership |
| `projects/atlas/population/ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md` | E1 bank + VAT |
| `projects/website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-v1.md` | Program registry |
| `projects/website-factory/execution-cases/bzpm-catalog-redesign/BZPM-BLUEPRINT-v1.md` | CP-01, CP-07, CP-08 |
| `https://www.tehno-tt.ru/about/howto/` | OEM payment pattern reference |
| Abat-ural PDP payment blocks (web research 2026-06-22) | Invoice validity / prepayment pattern |

---

*M9.15 Payment — research registration only. No implementation authorized. Awaiting operator decision.*
