# REPORT — M9.18 CUSTOM MANUFACTURING PAGE FORENSIC AND COMMERCIAL RESEARCH

**Milestone:** M9.18 — Custom Manufacturing / Изготовление оборудования под заказ  
**Project:** SITE-002 / BZPM (ЗПМ)  
**Environment (read-only baseline):** https://zpm.new-site.space/  
**Production reference:** https://bzpm.ru *(parity **SAFE UNKNOWN**)*  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Status:** **RESEARCH COMPLETE**  
**Date:** 2026-06-22  
**Mode:** Research only — **no** design · **no** wireframe · **no** HTML/CSS/JS · **no** deploy · **no** implementation charter

**Forensic pass:** Live HTTP read + URL candidate sweep + HTML capture `reports/m9.18-work/custom-equipment-live.html` (2026-06-22). Cross-references: M9.13–M9.17, M9.9 CTA, M9.8.9 Commercial Trust, catalog-redesign OQ-07/U-11. Competitor semantics: Kroner, Techno-TT, Restoinox, Abat (project design only).

**Central page question:** «Может ли ЗПМ изготовить оборудование под мои требования и насколько это безопасно, предсказуемо и выгодно?»

---

## 1. Actual URL and Usage Map

### 1.1 URL discovery

| Candidate URL | TEST result | Verdict |
|---------------|-------------|---------|
| **`/custom-equipment`** | HTTP **200** · final URL `https://zpm.new-site.space/custom-equipment` | **Canonical** |
| `/custom-equipment/` | Redirect / trailing-slash behaviour — not verified as separate alias | **Use non-trailing canonical** |
| `/izgotovlenie-pod-zakaz` | HTTP **404** | **Not used** |
| `/proizvodstvo-pod-zakaz` | HTTP **404** | **Not used** |
| `/custom-manufacturing` | HTTP **404** | **Not used** |
| `https://bzpm.ru/custom-equipment` | Not verified in this pass | **SAFE UNKNOWN** (prod parity) |

**Title (live):** «Оборудование на заказ для общепита и пищевых производств | ООО «ЗПМ»»  
**Meta description:** Завод пищевого машиностроения выполняет изготовление оборудования на заказ для предприятий общественного питания и пищевых производств.  
**Meta keywords:** **not present** in capture.  
**Canonical / og:url:** **not present** in capture.  
**og:image:** **empty** in capture.

**OpenCart route (inference):** `information/information` with SEO alias `custom-equipment` — same pattern as `/delivery`, `/dealers`, `/guarantee`. **Not confirmed** in MARS git tree.

**Nav label vs page H1:** Header/footer/mobile — «Оборудование на заказ». H1 — «Оборудование на заказ». Task brief uses «Изготовление оборудования под заказ» — **semantic overlap**, not a separate URL.

### 1.2 Navigation placement

Header top bar order (live capture + all corp captures):

1. **`/custom-equipment` — Оборудование на заказ** *(first corp link)*
2. `/payment-methods` — Оплата
3. `/delivery` — Доставка
4. `/dealers` — Дилерам
5. `/guarantee` — Гарантия
6. `/about` — О компании
7. `/blog/news` — Новости
8. `/contact` — Контакты

Same link: **footer** company links · **mobile offcanvas menu** · catalog chrome on all captured PLP/PDP pages.

**Evidence:** `custom-equipment-live.html` · `footer.twig` · `offcanvasmenu.twig` · M9.15–M9.17 live snippets.

**Launch-mode note (FACT):** M7.1 launch mode restricted root catalog links to «Нейтральное оборудование» + «Оборудование на заказ» — custom page treated as **strategic entry** alongside core catalog (`SITE-002-M7.1-LAUNCH-MODE-IMPLEMENTATION.md`).

### 1.3 Usage map (inbound / outbound)

| Surface | Relationship to `/custom-equipment` | Direction |
|---------|-------------------------------------|-----------|
| **Header / footer / mobile** | Persistent nav entry — **position #1** in corp strip | Inbound |
| **Catalog root / PLP** | No dedicated inline custom block on stable TEST | **Gap** — blueprint Scenario E expects link |
| **Search empty state** | Blueprint: conditional CTA to `/custom-equipment` | **Not traced** on live (OQ-07 / U-11) |
| **Commercial Trust proof row** | M9.8.9-03B: «На заказ» chip in trust stack — **no deep link** attested in twig | Should outbound |
| **M9.9 FAQ Q11** | «Делаете ли нестандарт / размер на заказ?» — **not in PLP TOP-8**; answer should live here | Planned inbound |
| **M9.9 FAQ Q10 / Q14** | Подбор комплекта / закупка по спецификации проекта — partial overlap | Secondary inbound |
| **Homepage** | Branch «Для пищевых производств» mentions изготовление на заказ (M9.8.9-03B) | Thematic inbound — **link depth UNKNOWN** |
| **PDP** | Standard SKU path — no custom upsell block attested | Low inbound today |
| **About** | Production / OEM narrative — **no custom-process depth** | Cross-link outbound (future) |
| **Delivery** | Custom shipment / oversized / regional logistics | Cross-link outbound (future) |
| **Payment** | M9.15: scenario row «custom equipment» — prepayment **SAFE UNKNOWN** | Cross-link outbound |
| **Dealers** | M9.16 IA B16: custom/project pointer | Cross-link inbound/outbound |
| **Warranty** | M9.17: custom warranty terms differ — B15 pointer to Custom | Cross-link outbound from Guarantee |
| **Contacts** | General forms — **no custom-project routing** | Fallback inbound |
| **`/our-certification`** | Header badge → certification — material/conformity proof | Cross-link outbound |

**Blueprint gap (documentation note):** CP-01 requires one primary surface per fact type. Custom manufacturing scope, process, intake, and commercial terms **should** be owned by **`/custom-equipment` primary**; catalog/PLP/FAQ = one-line + link. **Proposed rule CP-C01** *(program note, not blueprint edit in this task)*.

### 1.4 Ownership in Corporate Pages Program

| Field | Value |
|-------|--------|
| **Program** | BZPM Corporate Pages Program |
| **Milestone** | **M9.18** |
| **Registry doc** | `BZPM-CORPORATE-PAGES-PROGRAM-v1.md` — update status to **Research Complete** |
| **Catalog-redesign hook** | OQ-07 / U-11 — task-path (Scenario E) role |
| **Implementation gate** | Operator OQ-C01–CXX + design charter |

---

## 2. Current Page Structure

**Template signal:** `<section class="zpm-seo" data-seo>` — generic OpenCart information scaffold. **No** `.custom-page--*`, `.custom-equipment-page--*`, or dedicated CSS namespace in repo captures (contrast: M9.13 About `.about-page--*`).

**Chrome:** breadcrumb · `page-intro` H1 «Оборудование на заказ» · global header/footer · global modals (callback, question, get price) — **not custom-specific**.

| # | Block (live) | Hierarchy | Смысл | Полезность |
|---|--------------|-----------|-------|------------|
| B0 | Breadcrumb «Главная → Оборудование на заказ» | nav | Orientation | OK |
| B1 | Page intro H1 «Оборудование на заказ» | h1 | Topic | Weak — no value prop / scope boundary |
| B2 | H2 opening + 2 ¶ | h2 | OEM + when standard fails + input formats (TZ/sketch/drawing) | **Medium** — good intent framing |
| B3 | H3 «Что можно заказать» + ¶ | h3 | Product type list (tables, sinks, racks…) | **Medium** — aligns with catalog |
| B4 | H4 «Преимущества…» + UL (4) + ¶ | h4 | Fit-to-space, config, segments | **Low–Medium** — generic claims |
| B5 | H4 «Как проходит работа» + OL (4) | h4 | Intake → clarify → agree → produce → ship | **Medium** — process skeleton present |
| B6 | H4 «Какие параметры…» + table (4 rows) | h4 | Type / size / material / options matrix | **Medium** — useful procurement anchor |
| B7 | H5 «Для кого подходит услуга» + ¶ | h5 | Segment list (HoReCa, bakery, meat/dairy…) | **Low–Medium** |
| B8 | Blockquote | aside | Standard-vs-custom value statement | **Low** — no action |
| B9 | H6 «Что важно подготовить…» + ¶ | h6 | Brief checklist for faster quote | **Medium–High** — only practical CTA-adjacent content |

### 2.1 Commercial elements inventory

| Element | Present? | Notes |
|---------|----------|-------|
| Price / estimate range | **No** | Expected for custom — gap |
| Lead time / production SLA | **No** | Critical for снабженец / owner |
| MOQ / minimum project size | **No** | **SAFE UNKNOWN** if exists |
| Deposit / prepayment terms | **No** | Belongs Payment — **not linked** |
| Steel grade specification (AISI 304/430) | **No** — only «нержавеющая сталь» | Competitors name grades |
| Load / capacity engineering | Mentioned in process («нагрузка») — **no method** | Weak for technologist |
| Design ownership (who draws) | Implied «специалисты уточняют» — **no role clarity** | Objection gap |
| QC / acceptance / commissioning | **No** | Production trust gap |
| Warranty on custom | **No** | M9.17 defers here |
| Documents (passport, declaration, as-built drawing) | **No** | Tender / technologist gap |
| Case studies / photo proof | **No** | Trust gap |
| Catalog cross-links (start from standard SKU) | **No** | Missed upsell path |
| Dealer / channel path for custom | **No** | Integrator/dealer gap |

### 2.2 CTA inventory

| CTA type | Present on page body? | Target |
|----------|----------------------|--------|
| Primary custom brief / quote action | **No** | — |
| Engineering consultation | **No** | — |
| Upload drawing / TZ | **No** | — |
| Phone (explicit in body) | **No** | Header tel `+7 (3852) 72-18-90` |
| Email (e.g. `zakaz@`) | **No** | Footer `info@bzpm.ru` only |
| Link to Contacts | **No** | — |
| Link to catalog categories | **No** | — |
| Global modals (callback / question / price) | Chrome only — **not wired in content** | `#zpmFbCallback`, `#zpmFbQuestion`, get-price modal |

### 2.3 Forms

| Form | On page? |
|------|----------|
| Custom project brief (dimensions, file upload, object type) | **No** |
| Request calculation / КП for custom | **No** |
| Global site forms | Present in chrome only |

### 2.4 Evidence / proof inventory

| Proof type | On page? |
|------------|----------|
| Production photos / video | **No** |
| Workshop / CNC / laser | **No** |
| Engineering team | **No** |
| Sample drawings (sanitized) | **No** |
| Completed custom projects | **No** |
| Certificates / «Сделано в России» | **No** — lives on About / header badge |
| Client logos / integrator references | **No** |

### 2.5 Outbound links in body

**None** — only global nav/footer.

---

## 3. What Is Wrong Today

Evaluation through personas: **снабженец · технолог · инженер · владелец предприятия · закупщик · дилер · интегратор пищевого производства**.

### 3.1 Commercial strength

| Issue | Impact |
|-------|--------|
| **No primary CTA** — rich SEO text ends without conversion path | High-intent visitors bounce to phone guess or leave |
| **No commercial anchors** (price logic, lead time bands, MOQ) | Cannot compare vs catalog SKU or competitor quote |
| **No «start from catalog model X»** upsell | Misses lower-friction entry (modify standard) |
| Page reads as **SEO article**, not **manufacturer capability proof** | Weak vs Kroner/Restoinox service pages |
| First nav item sets expectation of **strategic service** — page under-delivers | Navigation promise > page substance |

### 3.2 Trust

| Issue | Impact |
|-------|--------|
| Zero visual production proof on page | «Реально ли завод?» — partially answered on About, **not here** |
| No named engineering / QC roles | Technologist cannot assess competence |
| No case examples (even anonymized) | «Повторят ли мой проект?» — unanswered |
| Material claim undifferentiated («нержавеющая сталь») | Weaker than AISI-grade competitors |
| No link to certification / conformity docs | Audit/tender path blocked |

### 3.3 Engineering logic

| Issue | Impact |
|-------|--------|
| Process OL is **generic** — no design-review gate, revision rounds, approval sign-off | Engineer cannot plan project timeline |
| Table covers **furniture-like params only** — no loads, spans, hygiene zones, drainage, thermal | Insufficient for цех / production line |
| No statement on **design responsibility** (customer vs factory) | Liability / error ownership unclear |
| No mention of **as-built documentation** or drawing format (DWG/PDF) | CAD-to-factory handoff unknown |
| **INFERENCE:** Page scope is **neutral stainless fabrications**, not full machine-building — but page title says «машиностроения» without clarifying boundary | Expectation mismatch risk |

### 3.4 Procurement logic

| Issue | Impact |
|-------|--------|
| Checklist (B9) is strongest block — **buried at H6** after blockquote | Procurement UX inverted |
| No **КП / счёт / contract** sequence cross-link to Payment | M9.15 custom row orphaned |
| No **delivery** implications (oversize, crate, region) | M9.14 not connected |
| No **repeat order / serial reproduction** policy | Multi-site chains / dealers blocked |
| No **ИНН / UL** intake hint for B2B | Form design undefined |

### 3.5 Production logic

| Issue | Impact |
|-------|--------|
| «Передается в производство» — **black box** | No factory scale, equipment, QC steps |
| No **acceptance** at factory vs on-site | Logistics of defect detection unknown |
| No **pilot / prototype** option | Complex projects cannot de-risk |
| Warranty for custom not addressed | Forces exit to `/guarantee` where custom also **not covered** (M9.17) |

### 3.6 CTA

| Issue | Impact |
|-------|--------|
| **Zero in-body CTAs** | Worst-in-program vs Dealers (broken form ref) and Warranty (weak blockquote) |
| Global «Задать вопрос» not contextualized for **upload-heavy** custom flow | Low submission quality |
| No **SLA for quote response** | M9.9 FAQ #3 class objection persists |

**Overall verdict (INFERENCE):** Page has **above-average SEO copy** for a corp stub but **below-minimum commercial job** for B2B custom manufacturing. It **partially answers** «что можно заказать» and «как в общих чертах идёт работа», but **fails** safety/predictability/profitability questions for decision-makers.

---

## 4. Objection Map

Full registry — severity: **C** Critical · **H** High · **M** Medium · **L** Low.

| ID | Objection (buyer voice) | Severity | Addressed today? | Owner surface |
|----|-------------------------|----------|------------------|---------------|
| **C-O01** | «Изготовят ли вообще мой нестандарт или откажутся?» | **C** | Partial (product list) | Custom — scope matrix |
| **C-O02** | «Насколько дорого относительно каталога / рынка?» | **C** | **No** | Custom — pricing logic + CTA |
| **C-O03** | «Насколько долго — от заявки до отгрузки?» | **C** | **No** | Custom — SLA bands |
| **C-O04** | «Смогут ли повторить проект для второй точки / партии?» | **H** | **No** | Custom — repeatability policy |
| **C-O05** | «Что с гарантией на нестандарт?» | **C** | **No** | Warranty primary + Custom summary |
| **C-O06** | «Какие документы получу (паспорт, декларация, чертёж)?» | **H** | **No** | Custom + PDP docs policy |
| **C-O07** | «Кто проектирует — я, мой проектировщик или ЗПМ?» | **C** | **No** | Custom — design responsibility |
| **C-O08** | «Кто отвечает, если ошиблись в размере / конструкции?» | **C** | **No** | Custom — approval + liability |
| **C-O09** | «Достаточно ли вашего производства для моей нагрузки / цеха?» | **H** | **No** | Custom + About production proof |
| **C-O10** | «Какая сталь и толщина — не сэкономите ли на металле?» | **H** | Partial | Custom — material spec |
| **C-O11** | «Можно ли начать от стандартной модели из каталога?» | **M** | **No** | Catalog ↔ Custom bridge |
| **C-O12** | «Работаете ли с нашим монтажником / интегратором?» | **M** | **No** | Custom + Contacts |
| **C-O13** | «Нужна ли предоплата и сколько?» | **H** | **No** | Payment scenario row |
| **C-O14** | «Доставите ли в мой регион крупногабарит?» | **M** | **No** | Delivery |
| **C-O15** | «Можем ли мы заказать через дилера?» | **M** | **No** | Dealers |
| **C-O16** | «Есть ли NDA / закрытый проект?» | **L** | **No** | Custom FAQ |
| **C-O17** | «Сделаете ли 3D / визуализацию до производства?» | **M** | **No** | Custom — design deliverables |
| **C-O18** | «Сколько итераций согласования включено?» | **H** | **No** | Custom — process detail |
| **C-O19** | «Соответствие SanPiN / пищевой зоне / мойке?» | **H** | **No** | Custom — compliance note |
| **C-O20** | «Можно ли приехать на производство / инспекцию?» | **M** | **No** | About + Custom |
| **C-O21** | «Что если на объекте не встаёт — кто переделывает?» | **C** | **No** | Custom + Warranty |
| **C-O22** | «Вы производитель или отдаёте на субподряд?» | **H** | Partial (OEM name) | About + Custom |
| **C-O23** | «Минимальный заказ / стоит ли звонить ради одной полки?» | **M** | **No** | Custom — MOQ |
| **C-O24** | «Как быстро ответите на расчёт?» | **H** | **No** | Custom CTA + M9.9 SLA |
| **C-O25** | «Можно ли приложить чертёж / DWG на сайте?» | **H** | **No** | Custom form design |

**Objection clusters for IA:**

1. **Capability** — C-O01, C-O09, C-O22, C-O11  
2. **Commercial predictability** — C-O02, C-O03, C-O13, C-O23, C-O24  
3. **Engineering / liability** — C-O07, C-O08, C-O17, C-O18, C-O21  
4. **Compliance / docs** — C-O05, C-O06, C-O10, C-O19  
5. **Channel / logistics** — C-O04, C-O14, C-O15, C-O12  

---

## 5. Questions Page Must Answer

After viewing, each persona should **not need to call** to understand the following **minimum** (full commercial close still may require contact).

### 5.1 Технолог

| # | Must understand |
|---|-----------------|
| T-Q1 | Классы изделий в scope (neutral SS fabrications vs «машины») |
| T-Q2 | Материалы, поверхности, hygienic design constraints |
| T-Q3 | Как передаётся ТЗ (форматы, обязательные поля) |
| T-Q4 | Этапы согласования конструкции и точка freeze |
| T-Q5 | Нагрузки / крепления / drain / utilities — что проектирует завод |
| T-Q6 | Документы на выходе (паспорт, спецификация, чертёж) |
| T-Q7 | Гарантия и сервис на нестандарт (или pointer) |

### 5.2 Инженер / проектировщик

| # | Must understand |
|---|-----------------|
| E-Q1 | Design responsibility split (customer / factory / shared) |
| E-Q2 | Revision policy and approval artifact |
| E-Q3 | Tolerances / standards referenced (GOST, SanPiN — if applicable) |
| E-Q4 | Repeatability — will factory store drawing for reorders |
| E-Q5 | Interface with catalog SKUs (modify standard vs clean-sheet) |
| E-Q6 | Factory acceptance vs site acceptance |

### 5.3 Снабженец / закупщик

| # | Must understand |
|---|-----------------|
| P-Q1 | How to request quote — form, email, phone, required fields |
| P-Q2 | Quote SLA and what КП contains |
| P-Q3 | Payment pattern for custom (prepay %, milestones) — **link Payment** |
| P-Q4 | Lead time bands (simple vs complex) |
| P-Q5 | Delivery implications — **link Delivery** |
| P-Q6 | Closing documents and UL invoicing |
| P-Q7 | Dealer/opt path if applicable — **link Dealers** |

### 5.4 Владелец бизнеса

| # | Must understand |
|---|-----------------|
| O-Q1 | «Это безопасно» — factory proof + warranty pointer |
| O-Q2 | «Это предсказуемо» — process timeline + SLA + approval gate |
| O-Q3 | «Это выгодно» — when custom beats catalog; price logic (ranges or factors) |
| O-Q4 | Risk reduction — approval before production, remake policy |
| O-Q5 | Who to talk to — one clear next step |

### 5.5 Дилер / интегратор

| # | Must understand |
|---|-----------------|
| D-Q1 | Can dealer/reseller submit custom for end customer |
| D-Q2 | Margin / pricing model for custom — **link Dealers** |
| D-Q3 | Who owns client communication (factory vs partner) |
| D-Q4 | Repeat orders for dealer’s chain projects |
| D-Q5 | Co-branding / NDA / project registration |

**Today:** T-Q1 partial · T-Q3 partial · P-Q1 partial (checklist only) · remainder **unanswered**.

---

## 6. What Evidence Should Be Shown

Ranked by **commercial trust impact** for custom manufacturing (FACT = exists elsewhere on site/program · PLANNED = recommended · UNKNOWN = needs operator).

| Rank | Evidence | Why strong | Availability |
|------|----------|------------|--------------|
| 1 | **Production environment** (shop floor, welding, cutting) | Proves OEM; reduces «перекуп» fear | About video/geo — **not on Custom** |
| 2 | **Process timeline with approval gate** | Predictability | Copy skeleton only — needs visual |
| 3 | **Sanitized custom case** (before/after, drawing→photo) | «Повторим ли проект» | **UNKNOWN** in repo |
| 4 | **Material specification table** (AISI grade, thickness policy) | Technologist trust | Competitor standard; ZPM **UNKNOWN** |
| 5 | **Engineering role statement** (in-house constructors) | C-O07/C-O08 | Kroner pattern; ZPM **UNKNOWN** |
| 6 | **QC / inspection step** | Production logic | About narrative possible — **not attested** |
| 7 | **Certificates / «Сделано в России»** | Compliance | `/our-certification`, header badge |
| 8 | **Catalog bridge** — «modify series X» examples | Lowers entry barrier | Catalog SKUs exist — **not linked** |
| 9 | **Lead time / quote SLA chips** | Procurement | **UNKNOWN** |
| 10 | **Document samples** (redacted passport/drawing cover) | Tender | PDP doc pattern — **UNKNOWN for custom** |

**Strongest bundle (INFERENCE):** Production photo/video + 1 case + material spec + approval timeline + primary brief CTA — **without** all five, page remains SEO-only.

**Weakest patterns to avoid (competitor mistakes):** Generic «индивидуальный подход» with no process; hiding dealer-only policy (Kroner); claiming «машиностроение» while only listing tables/shelves without scope boundary.

---

## 7. Existing Assets Already Available

Cross-program inventory — **reuse via link/summary**, not duplicate per CP-01.

| Source | Asset | Reuse on Custom |
|--------|-------|-----------------|
| **M9.13 About** | Video block, geo promo, cert promo, OEM narrative | Proof strip + **link About** |
| **M9.14 Delivery** | Regions, TK, pickup, post-payment handoff | «После изготовления — отгрузка» **link Delivery** |
| **M9.15 Payment** | Custom scenario row, prepayment **UNKNOWN**, UL/invoice flow | **Link Payment** — custom payment pattern |
| **M9.16 Dealers** | Channel program, partner types, custom pointer B16 | Dealer path for custom projects |
| **M9.17 Warranty** | Generic warranty process; custom gap flagged | Custom row + **link Guarantee** |
| **Contacts** | Phone, email, forms, requisites (partial), map | Secondary CTA; **no custom routing today** |
| **M9.9 CTA** | FAQ Q11 custom; Q28 technical specialist; persona objections | FAQ micro-set inbound links |
| **M9.8.9 Commercial Trust** | «На заказ» proof chip; OEM panel; FAQ TOP-8 | PLP secondary link to Custom |
| **Catalog** | Neutral equipment categories (tables, sinks, racks…) | Scope examples + «modify SKU» bridge |
| **Header badge** | `/our-certification` · made_in_russia.svg | Material/conformity |
| **Homepage** | «Изготовление на заказ / проектирование» branch (M9.8.9-03B) | Inbound — align messaging |
| **Blueprint** | Scenario E custom CTA; OQ-07 | Catalog empty-state / task-path link |

**Not available in repo (SAFE UNKNOWN):** custom project photo library · engineering team bios · quote SLA · steel grade policy · custom warranty terms · DWG upload workflow.

---

## 8. Project / ATLAS Assets

**Scope:** ATLAS Wave 3 ZPM population — **website delivery** focus; **no** custom-manufacturing marketing asset registry attested.

| Asset class | ATLAS / project status | Reuse potential |
|-------------|------------------------|-----------------|
| **PRJ-0009** Каталог-платформа bzpm.ru (active) | E0 operator evidence | Program context only |
| **ORG-0005** ЗПМ entity | Wave 1B complete | Legal manufacturer identity |
| **WEB-*** ZPM website records | Wave 4 population | TEST URL `zpm.new-site.space` |
| **Production photos / cases** | **Not in ATLAS** | Requires operator media intake |
| **Agreement / commercial terms** | **SAFE UNKNOWN** for custom-specific clauses | OQ-C13+ |
| **OpenCartPilot SITE-002 reports** | M9.x forensic corpus | Primary evidence base for this research |
| **Bulk storage** `C:\AI MARS STORAGE\ocpilot\project-sites\site-002\` | Live twig/CSS off-repo | Pre-implementation live-capture |

**Verdict:** ATLAS confirms **manufacturer identity and website program**; **does not** supply custom-project proof content. All high-trust evidence must come from **operator / ZPM production marketing**, not registry inference.

---

## 9. Missing Information — Operator Questions

Only questions **blocking credible IA/copy** — not exhaustive curiosity.

| ID | Question | Blocks |
|----|----------|--------|
| **OQ-C01** | **Scope boundary:** только neutral SS (столы, мойки, стеллажи) или также технологическое/«машиностроение»? | Title, segment promises, objection C-O01 |
| **OQ-C02** | **Minimum order / MOQ** — есть ли порог? | C-O23, P-Q4 |
| **OQ-C03** | **Lead time bands** — простое изделие / сложное / серия для объекта | C-O03, O-Q2 |
| **OQ-C04** | **Quote SLA** — срок ответа на расчёт после получения ТЗ | C-O24, M9.9 alignment |
| **OQ-C05** | **Design owner** — чертит завод, клиент, или оба; включены ли 3D/визуализация | C-O07, C-O17, E-Q1 |
| **OQ-C06** | **Revision rounds** — сколько согласований включено | C-O18 |
| **OQ-C07** | **Approval artifact** — что считается sign-off перед производством | C-O08, E-Q2 |
| **OQ-C08** | **Steel grades & thickness policy** (AISI 304/430, min thickness by product) | C-O10, T-Q2 |
| **OQ-C09** | **Load/engineering calc** — делает ли завод расчёт нагрузок или только по ТЗ клиента | C-O09, T-Q5 |
| **OQ-C10** | **Custom warranty terms** — same as series or different; link to M9.17 | C-O05, T-Q7 |
| **OQ-C11** | **Documents delivered** — паспорт, декларация, as-built чертёж, акт | C-O06, E-Q6 |
| **OQ-C12** | **Prepayment / payment milestones** for custom — align M9.15 | C-O13, P-Q3 |
| **OQ-C13** | **Remake / on-site misfit policy** — кто оплачивает переделку | C-O08, C-O21 |
| **OQ-C14** | **Repeat order policy** — хранение КД, артикул custom SKU | C-O04, E-Q4 |
| **OQ-C15** | **Dealer/custom channel** — прямой vs через дилера; integrator co-sale | C-O15, D-Q1–D-Q3 |
| **OQ-C16** | **Case study / photo permission** — можно ли публиковать проекты | Evidence rank #3 |
| **OQ-C17** | **File upload** — принимаете ли DWG/PDF через сайт или только email | C-O25, form design |
| **OQ-C18** | **Factory visit / inspection** — allowed? | C-O20 |
| **OQ-C19** | **Pricing logic for page** — факторы (металл, сварка, срок) без прайса или диапазоны | C-O02, O-Q3 |
| **OQ-C20** | **Catalog bridge** — официальный процесс «взять SKU X и изменить» | C-O11, catalog UX |

---

## 10. Competitor Research

**Method:** Public web fetch + prior M9.x competitor notes. **Not** exhaustive market study.

### 10.1 Benchmark set

| Competitor | Custom / individual page | Model | Strong patterns | Weak / error patterns |
|------------|---------------------------|-------|-----------------|------------------------|
| **Kroner** | `/services/ispolnenie-individualnykh-zakazov/` (referenced; fetch 404 in pass — content from index/services) | OEM neutral + thermal; **dealer-only** end sales | Named **engineers-constructors**, **3D visualization**, calc → agree → produce; **high-precision sheet metal** equipment list | End buyer must go through dealer — must state clearly; service URL instability |
| **Techno-TT** | Homepage + brand claims (no dedicated URL traced) | Large OEM since 1998; series + **individual projects** | Scale proof (1000+ types), GOST/EAEU, **dealer network**, induction innovation story | Custom buried in general copy — weak dedicated conversion |
| **Restoinox** | Brand/distributor pages (not single corp URL) | Neutral SS OEM | **Full cycle** (cut → pack), **AISI 430/1.5mm**, sketch/TZ for quote, European quality framing | Often **dealer-mediated**; custom not always primary page |
| **Abat** | **No custom fab focus** — `/proektirovanie/` design service | Serial thermal/refrigeration OEM | **Project design stages**, SanPiN/SNiP, turnkey equipment spec | **Not** stainless custom fab — wrong comparator for ZPM scope unless ZPM expands claim |
| **Regional integrators (e.g. Abat-TD)** | Project design landing | Design + equipment bundle | Stage timeline + form CTA | Conflates design with manufacturing |

### 10.2 Best practices (patterns to adopt)

1. **Dedicated service URL** with engineering-led narrative (Kroner).  
2. **Explicit process:** intake → engineering calc → visualization/approval → production → QC → ship.  
3. **Material transparency** — steel grade and thickness (Restoinox).  
4. **Primary CTA** tied to **brief checklist** (Abat design page, Kroner).  
5. **Scope honesty** — what is / is not custom-made (avoid Abat-style overclaim).  
6. **Production equipment list** as credibility (Kroner CNC/laser).  
7. **Bridge from catalog** — «non-standard sizes of serial line» (Techno-TT, Restoinox).

### 10.3 Typical errors

1. SEO wall without CTA (**ZPM today**).  
2. «Individual approach» without approval/liability terms.  
3. Hiding channel policy (dealer-only vs direct).  
4. No warranty/docs differentiation for custom.  
5. Confusing **kitchen design** with **factory manufacturing** (Abat-TD class).

---

## 11. Concepts

### Concept A — «Engineering Trust Hub»

**Idea:** Custom page as **capability + process + proof** hub: production strip (from About) + engineering timeline with **approval gate** + material spec + case slot + **primary project brief form** (dimensions, type, file upload, comment).

| Strengths | Weaknesses |
|-----------|------------|
| Closes C-O01–C-O08, C-O24 | Requires OQ-C01–C020 before publish |
| Matches central question (safe/predictable) | Heavier operator content + media |
| CP-C01 primary owner done right | Risk duplicating About if not disciplined |
| Supports technologist + engineer + owner | Form + upload = implementation scope |

**Подходит:** технологу · инженеру · владельцу цеха · integrator evaluating OEM fab.

---

### Concept B — «Minimal Brief + Strong CTA»

**Idea:** Short page: scope H1 + checklist + **one form** + phone. Process prose minimized; details in conversation.

| Strengths | Weaknesses |
|-----------|------------|
| Fast to ship | Leaves C-O02–C-O05, C-O09 open |
| Fixes zero-CTA gap quickly | Feels thin vs Kroner for engineers |
| Reuses B9 checklist as hero | Underuses production proof |
| Low duplication risk | Weak for tender / audit personas |

**Подходит:** малый HoReCa · «одна полка нестандартного размера» · быстрый lead.

---

### Concept C — «Project Type Matrix»

**Idea:** Central object — **matrix**: rows = изделие (стол, мойка, стеллаж, тележка, цеховой модуль) × columns = что нужно от клиента / срок **band** / docs / next step. Proof strip + one form with **type selector**.

| Strengths | Weaknesses |
|-----------|------------|
| Answers technologist + снабженец systematically | Cells need operator locks |
| Extends live table (B6) into full IA | Empty cells harm trust |
| Clear catalog bridge per row | UI complexity |
| Good for integrator specifying multi-item projects | Less emotional OEM story |

**Подходит:** снабженцу · integrator · проектировщику с спецификацией.

---

## 12. Recommended Concept

**Recommendation: Concept A (Engineering Trust Hub) with a Project Type Matrix block from Concept C (not the whole page).**

**Why:**

1. **Central question** requires **proof + process + commercial predictability**, not only a form (Concept B insufficient for C-O02–C-O09).  
2. ZPM page **already has** process prose + parameter table — Concept A **elevates** existing B5/B6/B9 instead of replacing with empty form.  
3. **CP-C01** mandates `/custom-equipment` as primary — Concept A is the only option that fully owns custom semantics across program cross-links (Payment, Warranty, Dealers, Delivery).  
4. Concept C’s matrix is the best device for **technologist / integrator** without duplicating catalog taxonomies — but as **one IA block (B05)**, not the entire page.  
5. Aligns with M9.15/M9.16/M9.17 pattern: **process + proof + cross-links + operator-locked commercial cells**.  
6. Blueprint Scenario E needs a **credible landing** for task-path CTA — Concept B alone would **undermine** nav position #1.

**Not recommended alone:** B (conversion without engineering trust); C alone (matrix-heavy without production story).

**Blueprint note (documentation only):** Resolve **OQ-07** as: Custom page = **primary explainer**; catalog = **conditional link** for Scenario E / empty search — not wizard.

---

## 13. Preliminary IA

**High-level block order only — no copy, no design, no wireframe.**

| # | Block | Purpose |
|---|-------|---------|
| **B01** | Page intro | H1 + one-line scope («изготовление neutral SS под ТЗ для HoReCa и пищевых производств») + scope boundary *(OQ-C01)* |
| **B02** | Value proposition strip | Safe / predictable / profitable — three chips mapping to objections |
| **B03** | OEM production proof row | Photo/video + scale + **link About** + cert badge |
| **B04** | What we manufacture | Category grid aligned with catalog families |
| **B05** | Project type matrix | From Concept C — input required / lead band / docs / next step *(operator cells)* |
| **B06** | Catalog bridge | «Modify standard model» — link series/SKU patterns *(OQ-C20)* |
| **B07** | Engineering process timeline | Intake → calc/design → approval freeze → production → QC → ship |
| **B08** | Design responsibility & revisions | Who draws; iterations; 3D if offered *(OQ-C05–C07)* |
| **B09** | Materials & quality | Steel grades, thickness, welding/QC *(OQ-C08–C09)* |
| **B10** | Commercial predictability | Quote SLA; pricing **factors**; MOQ *(OQ-C02–C04, C19)* |
| **B11** | Payment & contract pointer | Prepay/m milestones — **link Payment** |
| **B12** | Delivery & logistics pointer | Oversize/regions — **link Delivery** |
| **B13** | Warranty & remake pointer | Custom warranty + misfit policy summary — **link Guarantee** *(OQ-C10–C13)* |
| **B14** | Channel pointer | Direct vs dealer/integrator — **link Dealers** *(OQ-C15)* |
| **B15** | Case evidence (0–3 slots) | Photo/drawing pairs *(OQ-C16)* |
| **B16** | Primary CTA — project brief form | Type, dims, load, city, UL, file upload, comment *(OQ-C17)* |
| **B17** | Secondary CTA | Engineering phone/email · **link Contacts** |
| **B18** | FAQ micro-set (4–6) | Custom-only: scope, lead time, docs, warranty, dealer, catalog modify |
| **B19** | Prepare-your-brief checklist | Elevated from current B9 — pre-form |

**Optional secondary surfaces (post-charter, not this page body):**

- PLP Commercial Trust «На заказ» chip → `/custom-equipment`  
- M9.9 FAQ Q11 card → Custom  
- Catalog Scenario E / search empty → Custom link  
- M9.15 custom payment row → Custom  
- M9.17 B15 → Custom  

---

## 14. Cross-Page Logic

### 14.1 Ownership matrix (recommended)

| Topic | Primary owner | Secondary (summary + link only) |
|-------|---------------|----------------------------------|
| **Scope, process, intake, custom commercial terms** | **M9.18 Custom** | PLP trust chip; FAQ Q11 |
| **OEM identity / factory scale / video** | M9.13 About | Custom B03 strip |
| **Shipping, TK, regions, pickup** | M9.14 Delivery | Custom B12 |
| **Payment, prepay, invoice, VAT** | M9.15 Payment | Custom B11 |
| **Dealer / integrator channel for custom** | M9.16 Dealers | Custom B14 |
| **Warranty / service / remake (RMA)** | M9.17 Warranty | Custom B13 summary |
| **Contacts, requisites, map** | Contacts | Custom B17 |
| **Series SKU specs / standard docs** | Catalog PDP | Custom B06 bridge |
| **Certificates program** | `/our-certification` + CP-09 | Custom B03 badge |

**Proposed CP-C01:** `/custom-equipment` = **primary** for custom manufacturing; all other surfaces = **one-line + link**; never duplicate full process prose.

### 14.2 Duplication risks to eliminate

| Risk | Mitigation |
|------|------------|
| About production video vs Custom full video | Custom = **short strip**; About = depth |
| Payment custom prepay vs Custom commercial | Custom = **summary**; Payment = authoritative |
| Warranty generic vs custom terms | Guarantee = **matrix row**; Custom = **pointer in** |
| PLP FAQ Q11 full answer vs Custom | FAQ = **card + link** |
| Dealers «project/custom» vs Custom page | Dealers = **channel**; Custom = **technical/commercial** |
| Catalog SEO «нестандартные размеры» vs Custom | PDP/PLP = **modify link**; not process essay |

### 14.3 Role in Corporate Pages Program

| Field | Value |
|-------|--------|
| **Program position** | **Last research milestone** M9.18 — completes corp research set M9.13–M9.18 |
| **Nav position** | **#1** — highest visibility; implementation priority should reflect |
| **Catalog integration** | Closes blueprint **OQ-07 / U-11** when charter links Scenario E |
| **Depends on** | Operator OQ-C01–C20; benefits from M9.15–M17 cross-links already mapped |

### 14.4 Logical link graph (intent)

```
Catalog / PLP FAQ / search empty ──► Custom (primary)
Custom ──► About        (production depth)
Custom ──► Payment      (custom prepay)
Custom ──► Delivery     (ship custom)
Custom ──► Dealers      (channel)
Custom ──► Guarantee    (warranty/remake)
Custom ──► Contacts     (fallback)
Custom ──► Catalog/PDP  (modify standard SKU)
Warranty ──► Custom     (non-standard terms)
Payment ──► Custom      (custom scenario)
Dealers ──► Custom      (project pointer)
```

---

## Forensic gaps and research verdict

| ID | Gap | Severity |
|----|-----|----------|
| G-C01 | No dedicated custom CSS namespace | Medium |
| G-C02 | Zero in-body CTA despite nav #1 | **Critical** |
| G-C03 | No blueprint CP for Custom ownership | Medium |
| G-C04 | OQ-07 catalog task-path link **not traced** on live | Medium |
| G-C05 | Production `bzpm.ru/custom-equipment` parity | Low |
| G-C06 | No case/media assets in repo | **High** |
| G-C07 | Scope boundary «машиностроение» vs neutral fab unclear | **High** |

| Field | Value |
|-------|--------|
| **M9.18 status** | **RESEARCH COMPLETE** |
| **Ready for** | Operator OQ-C01–C20 intake · design charter · proposed CP-C01 |
| **Not ready for** | Implementation without operator locks on scope, SLA, warranty, materials |
| **Blocked on** | OQ-C01, C03, C04, C05, C10, C12 minimum for credible redesign |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Production URL parity | **SAFE UNKNOWN** |
| OpenCart `information_id` for custom page | **SAFE UNKNOWN** |
| Custom order volume / % of revenue | **SAFE UNKNOWN** |
| In-house vs outsourced fabrication steps | **SAFE UNKNOWN** |
| Engineering headcount / CAD tools | **SAFE UNKNOWN** |
| Whether live page content matches CMS draft elsewhere | **SAFE UNKNOWN** — capture is 2026-06-22 TEST |
| SECURITY RISK | **None identified** |

---

## Evidence index

| Artifact | Role |
|----------|------|
| `reports/m9.18-work/custom-equipment-live.html` | Live forensic capture |
| `reports/BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md` | OEM / production cross-link |
| `reports/BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md` | Logistics ownership |
| `reports/BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md` | Custom payment row |
| `reports/BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md` | Channel + B16 pointer |
| `reports/BZPM-M9.17-WARRANTY-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md` | Custom warranty gap |
| `reports/BZPM-M9.9-CTA-INTELLIGENCE-RESEARCH.md` | FAQ Q11, personas |
| `reports/SITE-002-M9.8.9-03B-COMMERCIAL-TRUST-BLOCK-REDESIGN.md` | «На заказ» trust chip |
| `projects/website-factory/execution-cases/bzpm-catalog-redesign/BZPM-BLUEPRINT-v1.md` | OQ-07, Scenario E |
| `projects/website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-v1.md` | Program registry |

---

# CORPORATE PAGES PROGRAM COMPLETION STATUS

**As of:** 2026-06-22 · after M9.18 research pass

## Research milestones

| ID | Page | URL (TEST) | Research | Primary artifact |
|----|------|------------|----------|------------------|
| M9.13 | About Company | `/about` | **Complete** | `BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md` |
| M9.14 | Delivery | `/delivery` | **Complete** | `BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md` |
| M9.15 | Payment | `/payment-methods` | **Complete** | `BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md` |
| M9.16 | Dealers | `/dealers` | **Complete** | `BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md` |
| M9.17 | Warranty | `/guarantee` | **Complete** | `BZPM-M9.17-WARRANTY-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md` |
| M9.18 | Custom Manufacturing | `/custom-equipment` | **Complete** | **This report** |

**Contacts (`/contact/`):** Delivered — **outside** M9.13–M9.18 program.

## What remains before implementation

| Lane | Status | Notes |
|------|--------|-------|
| **Forensic research (M9.13–M9.18)** | **DONE** | All six corp pages researched |
| **Operator OQ intake** | **OPEN** | Per-page OQ sets (P, D, W, C…) — blocks copy lock |
| **CP ownership rules in blueprint** | **PARTIAL** | CP-07/08/09 exist; Payment/Warranty/Custom **proposed** CP-09b, CP-W01, CP-C01 — not edited in research tasks |
| **Design charter** | **NOT STARTED** | Research complete ≠ design authorized |
| **IA / Architecture phase (program-level)** | **READY TO OPEN** | See below |
| **Implementation** | **NOT AUTHORIZED** | Requires per-page charter + live-capture discipline |

## Ready for IA / Architecture Phase?

| Criterion | Met? |
|-----------|------|
| All corp URLs discovered | **Yes** — including M9.17 `/guarantee` |
| Cross-page ownership map drafted | **Yes** — each M9.13–M9.18 report § Cross-Page Logic |
| Objection maps + concepts per page | **Yes** |
| Operator OQ registers identified | **Yes** — not answered |
| Catalog blueprint integration points known | **Yes** — OQ-07 Custom, CP-07/08, Commercial Trust |
| Live HTML/CSS capture for every page | **Partial** — About still CSS/JS-heavy without full HTML; Delivery registered without expanded live pass |

**Verdict (INFERENCE):** Program is **ready to transition to IA / Architecture Phase** as a **documentation and planning** stage — **not** to implementation.

**Recommended IA phase entry actions:**

1. Consolidate **cross-page CP rules** (Payment, Warranty, Custom proposals) into one program IA doc.  
2. Operator workshop: **OQ priority bundle** — Payment P01–P06, Warranty W01–W03, Custom C01–C05, Dealers D01.  
3. Resolve **OQ-07** (catalog → Custom link placement).  
4. Sequence design charters: suggest **M9.18 Custom** or **M9.17 Warranty** first given nav weight / trust gaps — **operator decision**.

**Program status recommendation:** Update `BZPM-CORPORATE-PAGES-PROGRAM-v1.md` — research row **M9.15–M9.18 → Research Complete**; program phase **Research → IA/Architecture**.

---

*M9.18 Custom Manufacturing — research only. No design. No implementation authorized.*
