# REPORT — M9.17 WARRANTY PAGE FORENSIC AND COMMERCIAL RESEARCH

**Milestone:** M9.17 — Warranty / Гарантия  
**Project:** SITE-002 / BZPM (ЗПМ)  
**Environment (read-only baseline):** https://zpm.new-site.space/  
**Production reference:** https://bzpm.ru *(parity **SAFE UNKNOWN**)*  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Status:** **RESEARCH COMPLETE**  
**Date:** 2026-06-22  
**Mode:** Research only — **no** design · **no** wireframe · **no** HTML/CSS/JS · **no** deploy · **no** implementation charter

**Forensic pass:** Live HTTP read + HTML capture `reports/m9.17-work/guarantee-live.html` (2026-06-22). URL candidates `/garantiya`, `/garantiya/`, `/warranty` — negative. Competitor semantics: Abat FAQ/service, Kroner passport + service.kroner.pro, M9.9/M9.16 prior research.

**Central page question:** «Что произойдёт, если с оборудованием возникнут проблемы после покупки?»

---

## 1. Executive summary

| Field | Value |
|-------|--------|
| **Page role** | Primary **warranty & post-sale service policy** surface (proposed **CP-W01**) |
| **Canonical URL (TEST)** | `/guarantee` |
| **Nav label** | «Гарантия» |
| **Research verdict** | **RESEARCH COMPLETE** — page exists but **fails commercial job**; URL confirmed; cross-page map documented |
| **Implementation** | **Not started** · **not authorized** by this report |

### Key findings

| # | Finding | Severity |
|---|---------|----------|
| 1 | Канонический URL — **`/guarantee`** (HTTP 200). Альтернативы `/garantiya`, `/warranty` — **не существуют** на TEST | Fact |
| 2 | **Срок гарантии не указан** на странице — критический пробел для закупщика и дилера | **Critical** |
| 3 | Страница — **generic `zpm-seo` scaffold** без dedicated CSS (как Delivery/Dealers до redesign, в отличие от About) | High |
| 4 | **Нет операционной модели сервиса**: кто принимает рекламацию, SLA, логистика брака, запчасти, выезд/ремонт на месте | **Critical** |
| 5 | **Нет dedicated CTA** и **нет формы рекламации** — только blockquote «телефон или форма на сайте» | High |
| 6 | **Нет cross-links** в body к Contacts / Delivery / Dealers / About / Custom | Medium |
| 7 | **Расхождение поверхностей**: PLP Commercial Trust — «гарантия ЗПМ» без срока; work-copy PDP — «12 месяцев»; corp page — **без срока** | **Critical** (governance) |
| 8 | Blueprint **не содержит CP для Warranty** — риск дублирования с PDP/PLP/Dealers при redesign без charter | Medium |

---

## 2. Фактический URL и usage map

### 2.1 URL discovery

| Candidate URL | TEST result | Verdict |
|---------------|-------------|---------|
| **`/guarantee`** | HTTP **200** · final URL `https://zpm.new-site.space/guarantee` | **Canonical** |
| `/garantiya` | Remote server error / not found | **Not used** |
| `/garantiya/` | Remote server error / not found | **Not used** |
| `/warranty` | Remote server error / not found | **Not used** |
| `https://bzpm.ru/guarantee` | Fetch failed in research pass | **SAFE UNKNOWN** (prod parity) |

**Title (live):** «Гарантия на оборудование \| ООО «ЗПМ»»  
**Meta description:** гарантия на оборудование ЗПМ; условия гарантийного обслуживания для общепита и пищевых производств.  
**Meta keywords:** гарантия на оборудование для общепита, гарантийное обслуживание, гарантия производителя.  
**Canonical / og:url:** **not present** in capture.

**OpenCart route (inference):** `information/information` with SEO alias `guarantee` — same pattern as `/delivery`, `/dealers`. **Not confirmed** in MARS git tree.

### 2.2 Navigation placement

Header top bar order (all corp captures + live guarantee page):

1. `/custom-equipment` — Оборудование на заказ  
2. `/payment-methods` — Оплата  
3. `/delivery` — Доставка  
4. `/dealers` — Дилерам  
5. **`/guarantee` — Гарантия**  
6. `/about` — О компании  
7. `/blog/news` — Новости  
8. `/contact` — Контакты  

Same link: **footer** company links · **mobile offcanvas menu**.

**Evidence:** `guarantee-live.html` · `footer.twig` · `offcanvasmenu.twig` · M9.15–M9.16 live snippets.

### 2.3 Usage map (inbound / outbound)

| Surface | Relationship to `/guarantee` | Direction |
|---------|------------------------------|-----------|
| **Header / footer / mobile** | Persistent nav entry | Inbound |
| **PLP Commercial Trust benefit** | «Гарантия производителя» — **no link** to `/guarantee` in twig capture | Should outbound (secondary) |
| **M9.9 FAQ Q7** | «Какая гарантия и кто обслуживает?» — **not in PLP TOP-8**; full answer should live here | Planned inbound |
| **M9.16 Dealers IA B09** | Partner warranty summary + **link Guarantee** | Planned inbound |
| **PDP service card** | Live stable backup: warranty lines **commented out**; work copy had «12 месяцев» | **Broken / inconsistent** secondary |
| **About** | Quality/production narrative — **no warranty depth** | Cross-link outbound (future) |
| **Delivery** | Logistics of **outbound** shipment — not RMA return path | Cross-link outbound (future) |
| **Payment** | No warranty content (M9.15 boundary) | — |
| **Contacts** | General forms (callback, question) — **no warranty routing** | Fallback inbound |
| **Custom equipment** | Custom warranty terms likely differ | Cross-link outbound (future) |

**Blueprint gap (documentation note):** CP-01 requires one primary surface per fact type. Warranty term / service process **should** be owned by **`/guarantee` primary**; catalog surfaces = one-line + link. **Proposed rule CP-W01** *(program note, not blueprint edit in this task)*.

### 2.4 Ownership in Corporate Pages Program

| Field | Value |
|-------|--------|
| **Program** | BZPM Corporate Pages Program |
| **Milestone** | **M9.17** |
| **Registry doc** | `BZPM-CORPORATE-PAGES-PROGRAM-v1.md` — update status to **Research Complete** |
| **Prior registry note** | «Nav URL SAFE UNKNOWN» — **superseded** by this forensic |
| **Implementation gate** | Operator OQ-W01–WXX + design charter |

---

## 3. Текущая структура страницы (forensic)

**Template signal:** `<section class="zpm-seo" data-seo>` — generic OpenCart information scaffold. **No** `.guarantee-page--*` or `.warranty-page--*` CSS namespace in repo captures (contrast: M9.13 About `.about-page--*`).

**Chrome:** breadcrumb · `page-intro` H1 «Гарантия» · global header/footer · global modals (callback, question, get price) — **not warranty-specific**.

| # | Block (live) | Hierarchy | Смысл | Полезность |
|---|--------------|-----------|-------|------------|
| B0 | Breadcrumb «Главная → Гарантия» | nav | Orientation | OK |
| B1 | Page intro H1 «Гарантия» | h1 | Topic | Weak — no value prop / term |
| B2 | H2 «Гарантийное обслуживание» + 2 ¶ | h2 | Generic OEM promise + compliance | **Low** — no term, no scope |
| B3 | H3 «Подтверждение гарантии» + ¶ + UL | h3 | Proof-of-purchase docs | **Medium** — useful start |
| B4 | H4 «Условия гарантийного ремонта» + OL (4 steps) | h4 | High-level process | **Low–Medium** — no SLA, channels, logistics |
| B5 | H4 «Когда гарантия не действует» + UL (5 items) | h4 | Exclusions | **Medium** — standard legal hygiene |
| B6 | Blockquote — phone or site form | aside | Contact fallback | **Weak** — no dedicated path |

### 3.1 Full content inventory (verbatim structure)

**B2 — Opening (2 paragraphs):**

- ЗПМ предоставляет гаранию на выпускаемое оборудование; продукция по отраслевым стандартам; контроль качества на производстве.  
- Гарантия при соблюдении правил эксплуатации, транспортировки, хранения по документации производителя.

**B3 — Proof documents (UL):**

- товарная накладная  
- гарантийный талон (если предусмотрен)  
- акт выполненных работ или поставки  

**B4 — Repair process (OL):**

1. Покупатель сообщает о неисправности менеджеру компании.  
2. Специалисты проводят диагностику оборудования.  
3. Если подтверждён заводской дефект — гарантийный ремонт.  
4. При невозможности ремонта — **может быть заменено** (не «обязательно»).

**B5 — Exclusions (UL):**

- механические повреждения  
- нарушение правил эксплуатации  
- следы самостоятельного ремонта  
- повреждение заводских пломб или маркировки  
- воздействие влаги, загрязнений или посторонних предметов  

**B6 — Contact blockquote:**

- Обращение к специалистам **по телефону** или **через форму обратной связи на сайте**.

### 3.2 CTA inventory

| CTA type | Present on page? | Target |
|----------|------------------|--------|
| Primary warranty / RMA action | **No** | — |
| Phone (explicit in body) | Partial (generic «по телефону») | Header tel `+7 (3852) 72-18-90` |
| Dedicated form | **No** | Global `#zpmFbQuestion` / callback — **not linked from body** |
| Email | **No** | Contacts has `zakaz@` — **not referenced** |
| Link to Contacts | **No** | — |
| Link to Dealers (channel service) | **No** | — |
| Link to Delivery (return logistics) | **No** | — |
| Link to PDP documents / passport | **No** | — |

### 3.3 Forms

| Form | On page? |
|------|----------|
| Warranty claim / RMA | **No** |
| Service request with SKU/serial | **No** |
| Global site forms (header/footer modals) | Present in chrome only — **not wired in content** |

### 3.4 Outbound links in body

**None** — only global nav/footer.

---

## 4. What Is Wrong Today

Evaluation through personas: **снабженец · закупщик · дилер · производственник · владелец бизнеса**.

### 4.1 Trust

| Issue | Impact |
|-------|--------|
| **No warranty term** (12 мес? 24? from sale vs commissioning?) | Buyer cannot file compliance checklist |
| Generic «отраслевые стандарты» without named QC / cert cross-ref | Reads as template text |
| «Может быть заменено» — weak commitment vs Abat/Kroner patterns | Reduces post-sale confidence |
| No link to production evidence (About) or conformity docs | Missed trust transfer |
| Certificate «Сделано в России» **not** warranty — must not substitute | M9.9 §5 misread risk |

### 4.2 Procurement readiness

| Issue | Impact |
|-------|--------|
| No **start date** of warranty (отгрузка / продажа / ввод в эксплуатацию) | Tender / AVL audit blocker |
| No **coverage matrix** (корпус / комплектующие / электрика / расходники) | Spec mismatch disputes |
| No **document pack** list for warranty case (фото, акт, серийник) | Slow claims |
| No **SLA** (response / repair / replacement windows) | M9.9 SLA UNKNOWN cluster |
| No **post-warranty** / paid service path | Lifecycle gap |

### 4.3 Dealer readiness

| Issue | Impact |
|-------|--------|
| No **channel model**: кто принимает рекламацию от конечника — завод или дилер | M9.16 O11 **unclosed** |
| No **warranty transfer** rules for dealer resale | Partner program incomplete |
| No link from Dealers page (today) | Split journey |

### 4.4 Commercial quality

| Issue | Impact |
|-------|--------|
| Page reads as **legal boilerplate**, not **service promise** | Low conversion reassurance |
| No differentiation vs regional fabricator / Trapeza reseller | Competitive weakness |
| Inconsistent claims across surfaces (see §7) | **Claim drift risk** |

### 4.5 Clarity

| Issue | Impact |
|-------|--------|
| Hierarchy jumps H2 → H3 → H4 without summary strip | Hard to scan |
| No FAQ micro-set | Self-serve failure |
| Blockquote CTA vague («форма на сайте») | User doesn't know which form |

### 4.6 Evidence level

| Present | Missing |
|---------|---------|
| Exclusion list (5 items) | Term, SLA, service geography, spare parts policy |
| Proof doc list (3 items) | Sample warranty card / talon, passport ref, conformity doc ref |
| 4-step process sketch | Diagnostics location, shipping RMA, loaner/replacement policy |

---

## 5. Warranty Objection Map

Structured registry of fears, objections, and procurement/dealer concerns.

**Personas:** снабженец (A) · закупщик/финконтроль · дилер (E) · производственник/технолог (C) · владелец кафе/бизнеса (B) · проектировщик (D).

| ID | Вопрос / страх / возражение | Критичность | Закрыто сегодня? | Owner block (future IA) |
|----|----------------------------|-------------|------------------|-------------------------|
| **W-O01** | **Какой срок гарантии?** (12/24/36 мес?) | Critical | **No** | Term strip *(operator)* |
| **W-O02** | **С какой даты** идёт гарантия? (отгрузка / оплата / монтаж / акт) | Critical | **No** | Term definitions |
| **W-O03** | **Что именно покрывается?** (корпус, фурнитура, электрика, расходники) | Critical | **No** | Coverage matrix |
| **W-O04** | **Что не покрывается** кроме generic list? (износ, SanPiN-cleaning damage, custom mods) | High | Partial | Exclusions + custom pointer |
| **W-O05** | **Кто обслуживает** — завод, дилер, сторонний СЦ? | Critical | **No** | Service model |
| **W-O06** | Купил **у дилера** — куда нести рекламацию? | Critical | **No** | Channel routing + Dealers link |
| **W-O07** | **Как быстро ответят** и починят? (SLA) | High | **No** | SLA chips *(operator)* |
| **W-O08** | **Как оформить** рекламацию — форма, email, телефон, документы? | High | Partial | RMA process + CTA |
| **W-O09** | Нужно ли **везти оборудование** на завод? Кто платит доставку брака? | High | **No** | Logistics / RMA |
| **W-O10** | **Ремонт или замена** — критерии, сроки замены | High | Partial («может») | Replacement policy |
| **W-O11** | **Запчасти** — наличие, срок поставки, платные после гарантии | High | **No** | Spare parts block |
| **W-O12** | **Выезд** мастера / пусконаладка / монтаж — входит ли в гарантию? | Medium | **No** | Service scope |
| **W-O13** | **Паспорт / инструкция** — где взять, что если утеряны? | Medium | Partial | Docs + PDP link |
| **W-O14** | **Гарантийный талон** — выдаётся ли всегда? | Medium | Partial («если предусмотрен») | Doc pack |
| **W-O15** | **Серийный номер / маркировка** — обязательность для кейса | Medium | **No** | RMA checklist |
| **W-O16** | **Custom / нестандарт** — та же гарантия? | High | **No** | Custom cross-link |
| **W-O17** | **Оборудование «под заказ»** vs складская серия — разные условия? | High | **No** | Product-class matrix |
| **W-O18** | **Партия для производства** — гарантия на N единиц, единый контакт? | Medium | **No** | B2B batch lane |
| **W-O19** | **После гарантии** — платный ремонт, договор ТО? | Medium | **No** | Post-warranty block |
| **W-O20** | **Downtime** — компенсация / подменное оборудование? | Low–Medium | **No** | *(operator — often «нет»)* |
| **W-O21** | **Соответствие** — гарантия vs декларация/сертификат (разные вещи) | High | **No** | Cert vs warranty disclaimer |
| **W-O22** | **Сделано в России** = гарантия государства? | Medium | **No** | M9.9 §5 semantics |
| **W-O23** | **Сравнение с Abat/Kroner** (1 год, СЦ сеть) | Medium | **No** | Bounded facts only |
| **W-O24** | **Юр. лицо / тендер** — нужен регламент в договоре | High | **No** | Contract reference *(operator)* |
| **W-O25** | **Фото/видео** дефекта — требуются ли до вывоза? | Medium | **No** | RMA step 1 |
| **W-O26** | **Регион** — обслуживаете ли мой город удалённо? | High | **No** | Geography + Delivery |
| **W-O27** | **Московский склад** — влияет ли на сервис? | Medium | **No** | Ops fact (Delivery) |
| **W-O28** | **Отказ** в гарантии — как обжаловать / экспертиза? | Medium | **No** | Escalation path |
| **W-O29** | **Остаточная стоимость / утилизация** при total loss | Low | **No** | *(operator)* |
| **W-O30** | **Импортные комплектующие** (если есть) — отдельная гарантия? | Low | **SAFE UNKNOWN** | *(operator)* |

**Cross-reference:** M9.9 FAQ **Q7** «Какая гарантия и кто обслуживает?» — **High frequency, High importance** — must resolve on this page, not PLP alone.

---

## 6. What Questions Must Be Answered

Complete question map for implementation charter (grouped by domain).

### 6.1 Term & scope

| Q-ID | Question |
|------|----------|
| W-Q01 | Warranty period (months) — default for catalog series |
| W-Q02 | Start event: shipment / sale / commissioning / other |
| W-Q03 | Per-product-class exceptions (custom, OEM project, spare parts) |
| W-Q04 | Geographic scope (RF only? EAEU?) |
| W-Q05 | Transferability to next owner (HoReCa resale) |

### 6.2 Coverage

| Q-ID | Question |
|------|----------|
| W-Q06 | Covered components list |
| W-Q07 | Excluded: wear parts, consumables, misuse, unauthorized repair |
| W-Q08 | Cosmetic defects vs functional defects |
| W-Q09 | Modifications / custom sizes warranty impact |
| W-Q10 | Installation errors — whose responsibility |

### 6.3 Service process

| Q-ID | Question |
|------|----------|
| W-Q11 | First contact channel priority (form / email / phone) |
| W-Q12 | Required claim data (SKU, serial, date, photos, docs) |
| W-Q13 | Remote diagnostics before physical return |
| W-Q14 | Repair location: on-site / workshop Barnaul / partner SC |
| W-Q15 | Turnaround targets (acknowledge / repair / replace) |
| W-Q16 | Replacement vs repair decision tree |
| W-Q17 | Loaner equipment policy (if any) |

### 6.4 Logistics

| Q-ID | Question |
|------|----------|
| W-Q18 | Return shipping: who arranges and pays |
| W-Q19 | Packaging requirements for RMA |
| W-Q20 | Integration with Delivery page (outbound vs return) |
| W-Q21 | Moscow warehouse role in service logistics |

### 6.5 Spare parts & post-warranty

| Q-ID | Question |
|------|----------|
| W-Q22 | Spare parts catalog / lead time |
| W-Q23 | Paid repair after warranty |
| W-Q24 | Maintenance / регламентное ТО — mandatory? (Abat pattern) |
| W-Q25 | Extended warranty offers (if any) |

### 6.6 Channel & documents

| Q-ID | Question |
|------|----------|
| W-Q26 | End buyer purchased via dealer — routing |
| W-Q27 | Dealer warranty obligations vs factory back-to-back |
| W-Q28 | Warranty card / talon issuance process |
| W-Q29 | Passport / instruction delivery with shipment |
| W-Q30 | Link to PDP document zone (declarations, passports) |

### 6.7 Legal & procurement

| Q-ID | Question |
|------|----------|
| W-Q31 | Relation to ЗоЗПП / B2B contract terms |
| W-Q32 | Warranty clause in supply contract template |
| W-Q33 | Denial letter / expertise process |
| W-Q34 | Penalty / downtime — explicitly out of scope or not |

---

## 7. What Evidence Should Be Shown

| Evidence type | Why buyer cares | Available today | Show on Warranty page? |
|---------------|-----------------|-----------------|------------------------|
| **Warranty term (bounded)** | Audit checklist | **Missing on corp page**; Kroner passport: **12 mo from sale** | **Primary — operator-locked** |
| **QC / production control** | «Заводской дефект» credibility | About narrative; generic line on page | **Summary + link About** |
| **Conformity documents** | Not same as warranty — but adjacent trust | PLP cert slider; `/our-certification` | **Labeled types + links** |
| **Сделано в России (СДС)** | Origin — **not** service SLA | Header badge | **One line disclaimer** per M9.9 |
| **Proof-of-purchase list** | Claim eligibility | On page (partial) | **Expand + checklist UI (IA only)** |
| **Sample warranty talon** | Know what to expect | **SAFE UNKNOWN** | If operator provides scan |
| **Service geography** | «Доедете ли до меня» | Delivery: RF shipment; **no SC map** | **Honest model statement** |
| **Process timeline** | Predict downtime | 4 steps — too thin | **Expanded steps + SLA** |
| **Contact routing** | Clear action | Phone in header; blockquote vague | **Dedicated service CTA** |
| **Spare parts capability** | Line uptime | **SAFE UNKNOWN** | Only if attested |
| **Dealer channel diagram** | Who owns end client | **Missing** | **If direct+dealer confirmed** |
| **Replacement policy proof** | Risk reversal | Weak «может быть заменено» | **Operator-locked policy** |
| **Post-warranty paid service** | Long lifecycle | **Missing** | Optional block |

**Strongest trust assets to inherit (not duplicate in full):**

1. Factory locality + production (About)  
2. Labeled certificates (PLP / certification page)  
3. Dual warehouse logistics fact (Delivery)  
4. Entity legality (Contacts / ATLAS E1)  
5. **Bounded warranty term** — **must be native to this page**, not only PLP bullet  

---

## 8. Existing Data Already Available

### 8.1 On `/guarantee` (live)

| Data | Present |
|------|---------|
| Generic warranty promise | Yes |
| Proof documents (3 types) | Yes |
| 4-step repair OL | Yes |
| 5 exclusions | Yes |
| Term / SLA / channel / logistics | **No** |
| Forms / deep links | **No** |

### 8.2 From prior corporate research

| Source | Reusable for Warranty |
|--------|----------------------|
| **M9.13 About** | Production QC narrative; cert promo; geo — **link, don't duplicate** |
| **M9.14 Delivery** | RF logistics; TK table; Barnaul + Moscow warehouses — **return logistics handoff** |
| **M9.15 Payment** | No warranty ownership; confirms **Payment ≠ Warranty** |
| **M9.16 Dealers** | O11 warranty for dealer's client; B09 summary slot; Kroner **1y** benchmark |
| **Contacts (delivered)** | Phone, email, forms, entity block — **service routing target** |
| **M9.9 CTA** | Q7 warranty; TOP-8 defer; Role B «кто чинит»; SLA UNKNOWN |
| **Commercial Trust (M9.8.9-03C)** | Benefit «Гарантия производителя» + docs; **no term, no link** |

### 8.3 Catalog / PDP surfaces

| Surface | Warranty-related content | Consistency note |
|---------|-------------------------|------------------|
| PLP Commercial Trust | «…документами и гарантией ЗПМ» | No term · no `/guarantee` link |
| PDP stable backup (`stable-pdp-v4`) | Warranty service items **commented out** | Live PDP warranty UX **minimal** |
| `commerce-card-work/producthero.twig` | «**Гарантия 12 месяцев**» + service card | **Work copy — may not match live** |
| Homepage advantages (architecture doc) | Stock/ship/warranty repeated on catalog levels | Duplication risk per CP-19 |

### 8.4 Claim drift register (fact vs inference)

| Surface | Claim | Status |
|---------|-------|--------|
| `/guarantee` | «предоставляет гарантию» — **no months** | **Fact** (live) |
| PLP trust benefit | «гарантия ЗПМ» — **no months** | **Fact** (twig capture) |
| Work PDP hero | «12 месяцев» | **Inference** — work tree; live stable **commented out** |
| Kroner passport (peer) | 12 months from sale | External benchmark |

**Governance:** Operator must **lock single term** before any surface states months publicly.

---

## 9. ATLAS / Project Assets

### 9.1 ATLAS (entity — not service terms)

**Source:** `ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md`

| Reusable on Warranty | Value |
|----------------------|-------|
| Legal name ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | Claim issuer identity |
| Production site Barnaul, Kalinina 15v | Repair / diagnostics location inference |
| Warehouse Moscow Basovskaya 14s2 | Logistics context *(with Delivery)* |
| Phone +7 (3852) 72-18-90 | Service contact |
| Email zakaz@bzmp.ru *(as recorded in CC)* | **Typo bzmp vs bzpm — operator verify** |

**Not in ATLAS:** warranty period, SC network, spare parts, SLA, RMA policy.

### 9.2 Project artifacts to reuse

| Artifact | Reuse |
|----------|-------|
| `BZPM-BLUEPRINT-v1.md` CP-01 | Single primary surface — propose **CP-W01 Warranty** |
| `BZPM-REDESIGN-ARCHITECTURE-v1.md` | Advantages warranty duplication warning |
| `blockcommercialtrust.twig` | Secondary one-liner + link pattern |
| `guarantee-live.html` | Forensic baseline capture |
| M9.16 / M9.15 cross-page matrices | Link graph templates |
| Abat / Kroner competitor semantics | Process & term benchmarks — **not copy** |

### 9.3 Trust assets already exist (inherit via link)

- Certificate images `/assets/img/certificates/`  
- `/our-certification` header badge route  
- About page CSS blocks (factory story)  
- Delivery TK + warehouse facts  

---

## 10. Missing Information — Operator Question Registry

Only information **truly required** before credible implementation.

| ID | Question | Blocks |
|----|----------|--------|
| **OQ-W01** | **Срок гарантии** (мес.) — единый для серийного каталога? | Term strip · PLP · PDP secondary |
| **OQ-W02** | **Начало гарантии** — отгрузка / продажа / подписание акта / монтаж? | Term definitions |
| **OQ-W03** | **Исключения по классам** — custom, проект, б/у, запчасти | Coverage matrix |
| **OQ-W04** | **Модель сервиса** — только завод / дилер первичный / авторизованные СЦ? | Service model · W-O05/O06 |
| **OQ-W05** | **Прямые продажи + дилеры** — кто принимает рекламацию конечника? | Channel diagram |
| **OQ-W06** | **SLA** — время ответа, диагностики, ремонта, замены | Process proof |
| **OQ-W07** | **Логистика брака** — кто организует и оплачивает транспорт? | RMA logistics |
| **OQ-W08** | **Замена vs ремонт** — обязательства (не «может») | Replacement policy |
| **OQ-W09** | **Гарантийный талон** — всегда ли выдаётся; образец для сайта? | Doc pack |
| **OQ-W10** | **Запчасти** — склад, сроки, платные после гарантии | Spare parts block |
| **OQ-W11** | **Выезд / монтаж / пусконаладка** — в scope или нет? | Service scope |
| **OQ-W12** | **Постгарантийное обслуживание** — есть ли платный сервис / ТО? | Post-warranty block |
| **OQ-W13** | **Dedicated контакт** сервиса (email/тел/форма) vs общий zakaz@ | CTA routing |
| **OQ-W14** | **Форма рекламации** — поля (SKU, серийник, фото, дилер)? | Primary CTA |
| **OQ-W15** | **География** — только РФ или шире; удалённые регионы | Geography block |
| **OQ-W16** | **Согласование с договором поставки** — текст для UL/tender | Legal row |
| **OQ-W17** | **Единый срок для PDP/PLP** — можно ли публиковать «12 мес»? | Cross-surface sync |
| **OQ-W18** | **Регламентное ТО** — обязательно для сохранения гарантии? (Abat model) | Exclusions / maintenance |
| **OQ-W19** | **Московский склад** — участвует в приёмке брака? | Logistics |
| **OQ-W20** | **Production bzpm.ru/guarantee** — parity with TEST before cutover? | Deploy gate |

**Minimum blockers for redesign:** OQ-W01 · OQ-W02 · OQ-W04 · OQ-W06 · OQ-W07 · OQ-W08 · OQ-W17.

---

## 11. Competitor Research

**Method:** M9.9/M9.16 competitor set + web fetch 2026-06-22 (partial — some URLs 503/404). Scope: **warranty & service communication**, not catalog UX.

| Peer | Surface | Warranty / service pattern | Strengths | Relevance to ZPM |
|------|---------|---------------------------|-----------|------------------|
| **Abat** | `abat.ru/servis-i-podderzhka/faq/` | **1 year from commissioning**; some SKUs 2y on subsystems; **dealer or ASC** first contact; SC list on site | Explicit term; channel routing; commissioning condition | **High** — OEM + dealer network |
| **Abat store** | `abatstore.ru/garantiya/` | 12 mo from sale; talon date; ASC service; phone/email | Operational contact | Dealer/reseller voice |
| **Abat.su** | Service page | **Commissioning act required**; **regulated maintenance** or warranty void | Strong exclusion clarity | Food production buyers |
| **Kroner** | Product passport PDF | **12 mo from sale**; exclusions; 15-day return rules; consumer-law style | Written bounded term | Neutral equipment peer |
| **Kroner** | `service.kroner.pro` | **Dedicated RMA form** + photos; separate service subdomain | Clear claim intake | Best **intake** pattern |
| **Kroner** | Dealers page (M9.16) | **1y warranty** as dealer benefit | Channel packaging | Dealer summary source |
| **Techno-TT** | `/about/garantiya/` *(503 in pass)* | Referenced in M9.9 as warranty FAQ source | **SAFE UNKNOWN** live content | FAQ Q7 evidence |
| **Юниторг** | Dealers benefits | «2-day warranty expertise» for partners | Partner enablement angle | Dealer-facing summary |
| **Restoinox** | PLP SEO | Quality claims — warranty not primary page | Weak dedicated warranty | Anti-pattern for depth |

### 11.1 Strongest patterns (trust architecture)

1. **Lead with bounded term** (months + start event) — Kroner passport, Abat FAQ.  
2. **Channel routing first** — «dealer who sold you» vs factory — Abat.  
3. **Commissioning / maintenance conditions** explicit — Abat.su.  
4. **Dedicated claim intake** (form, photos, serial) — Kroner service.  
5. **ASC / geography** list or honest «remote + return» model — Abat.  
6. **Separate service nav cluster** — Abat «Сервис и поддержка».  
7. **Labeled legal vs marketing** — warranty ≠ certification (align M9.9).

### 11.2 Typical errors (ZPM shares several)

| Error | ZPM today | Strong peers |
|-------|-----------|--------------|
| No warranty term | **Yes** | Kroner/Abat state 12 mo |
| Vague «contact manager» | **Yes** | Named channels + form |
| No logistics of return | **Yes** | Abat/Kroner RMA paths |
| No dealer routing | **Yes** | Abat FAQ |
| Generic exclusions only | Partial | + maintenance/commissioning |
| Service buried in corp prose | **Yes** | Dedicated service IA |

---

## 12. Concepts

**No design · no wireframes · strategy / IA only.**

### Concept A — «Service & Warranty Hub»

**Positioning:** Страница = **полный post-sale контракт с покупателем**: срок → покрытие → процесс → логистика → канал (direct/dealer) → документы → CTA рекламации.

| Strengths | Weaknesses |
|-----------|------------|
| Closes W-O01–W-O11 in one journey | Requires OQ-W01–W08 before publish |
| Matches Abat/Kroner best practice | Long page — needs strict IA |
| Supports all personas + dealer summary link | Risk duplicating Delivery/Dealers if undisciplined |
| Enables PLP/PDP **one-line + link** secondary | Operator workload for SLA facts |

**Подходит:** снабженец · закупщик · производственник · дилер (summary) · владелец.

---

### Concept B — «Legal Minimum + Strong Routing»

**Positioning:** Короткая attested policy: term strip + exclusions + 5-step process + **one primary CTA** (форма/тел/email) + links out.

| Strengths | Weaknesses |
|-----------|------------|
| Fastest path from today's page | Leaves logistics/channel thin |
| Low duplication risk | Weak vs Kroner service subdomain |
| Easy cross-surface sync (term only) | May fail procurement audit depth |

**Подходит:** quick fix · small team · honest «contact us for RMA» model.

---

### Concept C — «Lifecycle Matrix by Buyer Type»

**Positioning:** Central object — **matrix rows**: розница/UL · дилерский клиент · custom · опт/партия — columns: срок, документы, кто обслуживает, следующий шаг.

| Strengths | Weaknesses |
|-----------|------------|
| Excellent for procurement & dealer (O6/O18) | Heavy operator input per cell |
| Reduces wrong-path contacts | Complex to maintain |
| Aligns with M9.15 persona split pattern | Risk table with empty cells pre-charter |

**Подходит:** mixed channel OEM with **confirmed** operator matrix data.

---

## 13. Recommended Concept

**Recommendation: Concept A — «Service & Warranty Hub»** *(with Concept C matrix as optional block B6 inside A if OQ-W04/W05 answered)*.

**Why:**

1. **Central question** is lifecycle risk («что будет если сломается») — requires **process + logistics + channel**, not legal paragraph alone.  
2. ZPM sells **B2B equipment with downtime cost** — peers (Abat, Kroner) publish **term + intake + routing**.  
3. **Claim drift** today (PLP / work PDP / corp page) demands a **single primary surface** (CP-01) — Concept A is the only option that can anchor cross-surface sync.  
4. M9.16 Dealers **B09** already assumes Warranty depth elsewhere — Concept B would leave dealer program incomplete.  
5. Concept C alone without A's narrative spine reads as spreadsheet — use matrix **inside** A, not instead.

**Not recommended alone:** B (insufficient for procurement/dealer); C (without operator-filled cells).

**Blueprint follow-up (documentation only):** Propose **CP-W01** — «Warranty & service terms: `/guarantee` primary; PLP/PDP/Dealers summary + link only; certificates page ≠ warranty.»

---

## 14. Preliminary IA

**Block structure only — no design · no wireframes · no copywriting.**

| # | Block | Purpose |
|---|-------|---------|
| **B01** | Page intro | H1 + one-line scope («гарантия и сервис производителя ЗПМ») |
| **B02** | Term strip | **Months + start event** *(OQ-W01/W02)* — primary fact |
| **B03** | Service model | Who services: factory / dealer / ASC — **channel diagram** *(OQ-W04/W05)* |
| **B04** | Coverage matrix | Covered vs excluded vs wear parts · custom row → Custom link |
| **B05** | Proof & documents | Purchase docs + talon + passport/PDP docs · checklist |
| **B06** | Buyer-type routing (optional) | UL / end buyer / dealer client / batch — Concept C slice |
| **B07** | Claim process timeline | Intake → diagnostics → repair/replace → return shipment *(OQ-W06)* |
| **B08** | RMA logistics | Who pays freight · packaging · link **Delivery** for geography |
| **B09** | SLA / response expectations | Acknowledge / repair windows — or honest UNKNOWN labels |
| **B10** | Replacement policy | Criteria when repair impossible *(OQ-W08)* |
| **B11** | Spare parts & post-warranty | Parts lead time · paid service *(OQ-W10/W12)* |
| **B12** | Quality & production evidence | QC summary + **links About** + labeled certs |
| **B13** | Cert vs warranty disclaimer | M9.9 semantics — SDS ≠ warranty |
| **B14** | Dealer pointer | One paragraph + **link Dealers** for channel terms |
| **B15** | Custom manufacturing pointer | Non-standard warranty + **link Custom** |
| **B16** | FAQ micro-set (4–6) | Warranty-only: term, dealer path, return, talon, custom |
| **B17** | Primary CTA | Dedicated claim path *(form and/or service email/phone)* *(OQ-W13/W14)* |
| **B18** | Secondary CTA | **Contacts** fallback · general question form |

**Optional secondary surfaces (post-charter, not this page body):**

- PLP trust benefit → one line + link `/guarantee`  
- PDP service zone → term chip + link  
- M9.9 FAQ Q7 card → link here  
- Dealers B09 → summary + link here  

---

## 15. Cross-Page Logic

### Ownership matrix (recommended)

| Topic | Primary owner | On Warranty page |
|-------|---------------|------------------|
| **Срок / покрытие / exclusions / RMA process** | **M9.17 Warranty** | Primary |
| **Кто производитель / QC story** | M9.13 About | B12 summary + link |
| **Отгрузка / ТК / склады (исходящая)** | M9.14 Delivery | B08 handoff — **return path only summary** |
| **Оплата / счёт** | M9.15 Payment | **Not here** |
| **Дилерская модель / кто продаёт** | M9.16 Dealers | B03/B14 pointer |
| **Нестандарт / проект** | M9.18 Custom | B04/B15 pointer |
| **Сертификаты conformity** | `/our-certification` / PDP docs | B12 labeled — **not warranty proof** |
| **Контакты / формы** | Contacts (delivered) | B17/B18 routing — **not duplicate full contact page** |
| **Паспорт / декларация SKU** | PDP Reference zone | Link pattern from B05 |

### Duplication risks to eliminate

| Risk | Mitigation |
|------|------------|
| «Гарантия производителя» on PLP + full text on Warranty | PLP = one benefit line + link |
| Delivery TK table copied for RMA | Warranty = return policy summary; TK list stays Delivery |
| Dealer O11 answered on Dealers in full | Dealers = partner-facing summary; Warranty = authoritative |
| About QC paragraph duplicated | About = story; Warranty = **service contract** |
| PDP «12 months» without corp backing | **Operator lock OQ-W17** before any months claim |
| Certificate slider interpreted as warranty | B13 disclaimer |

### Link graph

```
PLP trust / M9.9 Q7 / PDP service chip ──► Warranty (primary)
Warranty ──► About        (production/QC)
Warranty ──► Delivery     (logistics context / return)
Warranty ──► Dealers      (channel service)
Warranty ──► Custom       (non-standard terms)
Warranty ──► Contacts     (claim CTA fallback)
Warranty ──► PDP docs     (passport / conformity)
Dealers B09 ──► Warranty  (inverse)
Payment ──► (no warranty link required)
```

---

## Forensic gaps and research verdict

| ID | Gap | Severity |
|----|-----|----------|
| G-W01 | **No warranty term** on primary page | **Critical** |
| G-W02 | **No service model / dealer routing** | **Critical** |
| G-W03 | **No RMA logistics** | **Critical** |
| G-W04 | **No dedicated claim CTA** | High |
| G-W05 | Cross-surface claim drift (PLP / work PDP) | **Critical** |
| G-W06 | No blueprint CP for Warranty | Medium |
| G-W07 | Generic template vs About quality gap | Medium |
| G-W08 | Production `bzpm.ru/guarantee` parity | Low until cutover |
| G-W09 | Techno-TT garantiya page not fetched (503) | Low |

| Field | Value |
|-------|--------|
| **M9.17 status** | **RESEARCH COMPLETE** |
| **Ready for** | Operator OQ-W01–W20 intake · design charter · proposed CP-W01 |
| **Not ready for** | Implementation without operator locks on term + service model |
| **Blocked on (minimum)** | OQ-W01 · OQ-W02 · OQ-W04 · OQ-W06 · OQ-W08 · OQ-W17 |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Production `/guarantee` content parity with TEST | **SAFE UNKNOWN** |
| Live PDP warranty chip text (12 mo or absent) | **SAFE UNKNOWN** — stable backup shows commented-out block |
| Authorized service center network exists? | **SAFE UNKNOWN** |
| Exact warranty months operator policy | **SAFE UNKNOWN** |
| Spare parts program | **SAFE UNKNOWN** |
| Commissioning act requirement | **SAFE UNKNOWN** |
| Techno-TT `/about/garantiya/` live content | **SAFE UNKNOWN** (503) |
| OpenCart information_id for `guarantee` | **SAFE UNKNOWN** |

---

## Evidence index

| Artifact | Role |
|----------|------|
| `reports/m9.17-work/guarantee-live.html` | **Primary live HTML capture** |
| `reports/BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md` | Cross-page · O11 · B09 |
| `reports/BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md` | Payment boundary |
| `reports/BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md` | Logistics boundary |
| `reports/BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md` | Trust narrative boundary |
| `reports/BZPM-M9.9-CTA-INTELLIGENCE-RESEARCH.md` | Q7 · personas · cert semantics |
| `reports/m9.8.9-03c-work/blockcommercialtrust.twig` | PLP warranty mention |
| `commerce-card-work/producthero.twig` | Work PDP 12 mo claim |
| `backups/stable-pdp-v4-.../producthero.twig` | Live backup — warranty commented |
| `projects/website-factory/.../BZPM-BLUEPRINT-v1.md` | CP-01 |
| `projects/website-factory/.../BZPM-CORPORATE-PAGES-PROGRAM-v1.md` | Program registry |
| `projects/atlas/population/ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md` | Entity facts |
| Abat / Kroner public materials (web 2026-06-22) | Competitor benchmarks |

---

**STATUS:**  
M9.17 WARRANTY PAGE — **RESEARCH COMPLETE**

**NEXT RECOMMENDED STEP:**  
M9.18 CUSTOM MANUFACTURING PAGE FORENSIC AND COMMERCIAL RESEARCH
