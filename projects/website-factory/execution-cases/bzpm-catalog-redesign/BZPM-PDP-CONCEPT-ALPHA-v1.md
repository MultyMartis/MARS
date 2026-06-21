# REPORT — BZPM PDP CONCEPT ALPHA

**Execution case:** `bzpm-catalog-redesign`  
**Document:** `BZPM-PDP-CONCEPT-ALPHA-v1`  
**Phase:** W6A.1 — PDP Concept Alpha  
**Lane:** A (Website Factory)  
**Mode:** Concept Development — no UI, no wireframes, no Figma, no implementation  
**Date:** 2026-06-09  
**Evidence base:** [BZPM-REDESIGN-ARCHITECTURE-v1](BZPM-REDESIGN-ARCHITECTURE-v1.md) · [BZPM-BLUEPRINT-v1](BZPM-BLUEPRINT-v1.md) · [BZPM-UX-STRUCTURE-v1](BZPM-UX-STRUCTURE-v1.md) · [BZPM-VISUAL-UX-PROTOTYPE-v1](BZPM-VISUAL-UX-PROTOTYPE-v1.md) · [BZPM-FINDINGS-REGISTER-v1](BZPM-FINDINGS-REGISTER-v1.md)

**Audit environment:** https://zpm.new-site.space/  
**Example SKU (reference only):** ВМЦ-П3-2/500 (моечные ванны, серия ПРЕМИУМ-3)

---

## Concept Name

**«Серийная верификация»** (Series-Verified OEM Evaluation)

Краткая формула: PDP будущего BZPM — это **поверхность верификации SKU внутри OEM-серии**, а не карточка одного артикула без контекста выбора.

---

## Concept Philosophy

### Какую проблему решает концепт

Текущая PDP работает как **карточка одного SKU** (W1A-F-01): цена, наличие, артикул и четыре габарита видны, но страница **не поддерживает цепочку решения** type → family → series → SKU (W1C-F-01). Покупатель не получает на PDP явного ответа «я в правильной серии?» (WH-13), «это правильная конфигурация для моей задачи?» (WH-14) и «есть ли лучший вариант в этой же серии?» (W1A-F-06, WH-07). При этом **данные уже существуют** — 20+ строк характеристик, описание, документы — но упакованы так, что 2 из 3 вкладок скрыты при загрузке (W1A-F-05, W2-F-03), а «Похожие товары» уводят в другую продуктовую семью (котломойки на PDP моечной ванны, W1A-F-06).

Концепт «Серийная верификация» решает разрыв между **наличием информации** и **поддержкой решения** — через переупаковку видимости, а не через расширение backend или клон Trapeza.

### Какого покупателя обслуживает

| Профиль | Потребность на PDP |
|---------|-------------------|
| **Инженер / снабженец с артикулом** | Быстро подтвердить, что открыт нужный SKU, серия и ключевые параметры совпадают с закупкой (W1C-F-04, WH-04) |
| **Специалист, пришедший из серии или категории** | Подтвердить, что выбранная серия (например ПРЕМИУМ-3) — правильный OEM-уровень, и сравнить соседние SKU той же серии (W2-F-10, WH-12) |
| **B2B-покупатель / дилер** | Принять коммерческое решение с контекстом наличия, срока, доставки и пути «купить как дилер» — без прокрутки до footer-блоков (WH-15, CV-01) |
| **Покупатель после поиска по габаритам** | Увидеть, что один размер может существовать в нескольких сериях (W1C-F-05), и явно верифицировать серию до покупки |

Концепт **не** обслуживает сценарий «выбрать модель с нуля на одной странице» — sibling SKU matrix исключена как не рыночная норма (V-09).

### Почему концепт существует

Стратегия W4–W6 зафиксировала роль PDP: **single-SKU evaluation and conversion surface** — поверхность оценки и конверсии одного артикула, не in-page selection matrix. Концепт Alpha переводит эту роль в **будущее состояние**, где первый экран отвечает на вопрос стратегии §3: **«это правильная модель в правильной серии?»** — до scroll.

Концепт узнаваем как BZPM, потому что сохраняет OEM-иерархию серий, заводскую номенклатуру, B2B-конверсию и product-database модель. Он отличается от текущего PDP, потому что **серия, категорийно-критичные параметры и in-series alternatives** становят частью информационной логики первого экрана, а не следствием breadcrumbs и misaligned «Похожих».

---

## Current PDP vs Concept Alpha

| Аспект | Текущее состояние (что есть / что слабо) | Concept Alpha (что меняется / зачем) |
|--------|------------------------------------------|--------------------------------------|
| **Роль страницы** | Карточка одного SKU; отображение, не инструмент выбора (W1A-F-01) | Поверхность **верификации** SKU в контексте серии и цепочки решения (Architecture §E) |
| **Серия** | Видна только в breadcrumbs (WH-13); на первом экране нет | **Series Context Block** — серия + ссылка на listing серии на первом экране (USR-PDP-02) |
| **Hero-свойства** | 4 props: L×W×H×mass (W1A-F-02) — недостаточно для моечных ванн (WH-14) | Selected props (E-04) **+** category-critical props (E-05): секции, чаша, материал, конструкция |
| **Спецификации** | 20+ строк за вкладкой «Характеристики»; 2/3 вкладок скрыты (W1A-F-05, W2-F-03) | **Minimum Spec Summary** default-visible (5–8 строк) + полная таблица через tab/expand (USR-PDP-09, USR-PDP-10) |
| **Описание** | Вкладка «Описание» default; placeholder mini-description в hero (W1A-F-03) | Placeholder **подавлен**; описание в primary zone, default-visible (USR-PDP-08) |
| **«Похожие товары»** | Cross-family (котломойки на sink PDP) — priority #1 finding (W1A-F-06) | **In-Series Alternatives** — только SKU той же серии (USR-PDP-12); cross-family — deprioritized, labeled |
| **Коммерция** | Цена, наличие, CTA на первом экране (W1A-F-12) — сильная сторона | Сохраняется + **Commercial Detail** и **Consultative CTA** elevated к зоне решения (USR-PDP-18, USR-PDP-19) |
| **B2B-контекст** | Dealer/delivery в header; у CTA на PDP — слабо (WH-15) | Lead time, delivery summary, dealer path **adjacent to conversion** (Zone 6) |
| **Compare / fav** | Icon-only (W1A-F-07) | Labeled actions + compare feedback (USR-PDP-07, USR-PDP-13) |
| **Медиа** | 1 изображение, 520px gallery — высокое space-to-meaning mismatch (W2-F-01, WH-16) | Media Block остаётся; **информационный приоритет** смещён к verification blocks, не к gallery footprint |
| **Trust / commercial wallpaper** | Certificates, dealer form повторяются на deep pages (W2-F-07) | Trust micro-signals compact; full dealer form и certificates slider **suppressed** на PDP |
| **Sibling matrix** | Отсутствует (WH-12) | **Не добавляется** — mitigated через in-series alternatives + return-to-series (V-09) |
| **Demo / placeholder content** | AssuM logo, placeholder subtitle (W1A-F-03, W1A-F-04) | **Forbidden** в hero — erodes trust на evaluation screen |

**Принцип изменения:** visible packaging ≠ more data (P-05). Alpha не требует новых backend-полей для v1 minimum по моечным ваннам — требует **перераспределения ownership** существующих фактов по зонам решения.

---

## First Screen Concept

**Определение first screen:** всё, что покупатель видит **до первого meaningful scroll** на desktop; на mobile — P1–P2 priority blocks (UX Structure §G6, Visual Prototype mobile schematic).

### Что должно быть видимо (must)

| Блок | Зачем на first screen |
|------|----------------------|
| **Breadcrumb** (USR-PDP-00) | Контекст иерархии; escape path к family/series (W1A-F-10) |
| **Product Identity** — H1, артикул, copy (USR-PDP-01) | Подтверждение «правильный SKU?» для expert path (W1A-F-11) |
| **Series Context** — серия + link (USR-PDP-02) | **Ключевое отличие Alpha:** «правильная серия?» без разбора breadcrumbs (WH-13) |
| **Commercial Core** — статус, qty, цена, primary CTA (USR-PDP-03) | D7: available + convert (W1A-F-12, MO-01) |
| **Selected Properties** — L×W×H×mass (USR-PDP-04) | Физический fit-check (W1A-F-02) |
| **Category-Critical Properties** (USR-PDP-05) | Секции, чаша, материал, конструкция — fit beyond dimensions (WH-14) |
| **Media Block** (USR-PDP-06) | Visual confirmation; count = content issue, zone = architectural |
| **Secondary Actions** — compare, favorites, labeled (USR-PDP-07) | D9 compare path (W1A-F-07, W1C-F-09) |

**Desktop grouping logic (information only):**

```text
ORIENTATION     → breadcrumb · identity · series context · media
VALIDATION      → selected props · category-critical props · secondary actions
COMMERCIAL      → commercial core (highest decision weight)
```

**Mobile reorder (decision-equivalent, not DOM parity — P-09):** Commercial Core **elevated first** (P1), затем series + identity + key props; media deprioritized to P4.

### Что должно быть подавлено (suppress)

| Элемент | Причина |
|---------|---------|
| Placeholder mini-description (W1A-F-03) | Erodes trust на evaluation screen |
| Demo brand logo AssuM (W1A-F-04) | Не OEM identity BZPM |
| Misaligned «Похожие товары» cross-family (W1A-F-06) | Breaks in-series decision path |
| Full dealer application form inline (W2-F-07) | Wallpaper; link вместо form |
| Full certificates slider (W2-F-07) | Trust уже на catalog entry; micro-signals достаточно |
| Duplicate advantages grids | W2 duplication |
| In-page sibling SKU matrix (V-09) | Not market standard; не BZPM OEM pattern |
| Full spec table 20+ rows as default | Hidden-in-tabs problem moves to expand, not to first screen overload |
| Cross-family related products | Not before in-series alternatives |

### Что должно быть сгруппировано

| Группа | Состав | Логика |
|--------|--------|--------|
| **Identity cluster** | H1 + article + series context | «Что это и к какой серии относится» |
| **Fit cluster** | Selected props + category-critical props | «Подходит ли физически и функционально» |
| **Action cluster** | Commercial core + secondary actions | «Могу ли купить / сравнить сейчас» |
| **Visual cluster** | Media | Подтверждение, не доминанта first screen |

### Что становится более prominent

1. **Series affiliation** — с absent → mandatory first screen (NEW packaging)
2. **Category-critical attributes** — from hidden tab → hero extension
3. **Commercial decision block** — remains highest attention; gains adjacent B2B context in scroll-adjacent Zone 6
4. **Minimum spec summary** — visible at or immediately below first screen boundary (USR-PDP-09)
5. **Consultative CTA** — elevated to primary zone end, not footer-only (USR-PDP-19)

### Что становится less prominent

1. **Gallery footprint** — zone assigned, но не information dominator (W2-F-01, WH-16)
2. **Full spec table** — accessible, not default first-screen payload
3. **Extended description / documentation** — reference zone
4. **Cross-family related** — after in-series alternatives, explicitly labeled «Сопутствующие»
5. **Site-wide trust/commercial blocks** — collapsed or linked, not repeated

---

## Information Hierarchy

### Tier 1 — Decision Gate (first screen)

**Состав:** Series Context · Product Identity · Commercial Core · Selected Properties · Category-Critical Properties · Secondary Actions · Media (supporting)

**Зачем tier существует:** Ответить на три gate-вопроса до scroll: **правильная серия? · правильная модель? · доступно для покупки?** Это прямое следствие Strategy §3 и W1C decision points D3, D7.

**Правило:** Tier 1 blocks **не дублируют** полную spec table — только decision subset (ID-01, P-05).

---

### Tier 2 — Confirmation (default-visible, minimal scroll)

**Состав:** Description Block · Minimum Spec Summary · Consultative CTA (position rule: at or before primary zone end)

**Зачем tier существует:** Подтвердить **correct specifications?** без tab switch (W1A-F-05, W2-F-03). 5–8 строк min spec + structured description закрывают «under-informative» perception без inventing data.

**Правило:** Tier 2 **default-visible** — не inactive tab.

---

### Tier 3 — Selection Support (scroll-required, decision-relevant)

**Состав:** In-Series Alternatives · Compare Feedback · Return-to-Series · Full Specifications (tab/expand) · Documents Entry

**Зачем tier существует:** Поддержать **suitable alternative?** и engineering review **within series scope** (W1A-F-06, WH-07, WH-12 partial mitigation). Full specs и documents — для procurement/tender, но discoverable from primary path.

**Правило:** In-Series Alternatives **before** cross-family related (UX-15).

---

### Tier 4 — Reference & Extended Commercial (deep scroll, non-blocking)

**Состав:** Full Documentation · Extended Description · Cross-Family Related (labeled) · Commercial Detail · Trust Micro-Signals · Legal Disclaimer

**Зачем tier существует:** Deep reference для tender/engineering (D8 partial self-serve) и B2B procurement confidence **at conversion** without blocking initial fit decision. Не required для «могу ли купить прямо сейчас» если Tier 1–2 satisfied.

**Правило:** Tier 4 **не obstructs** Tier 1–2; cross-family never masquerades as «похожие».

---

## Decision Flow

```text
Correct Series?
  │
  ├─ INPUT:  buyer arrives from category / series / search / direct article
  ├─ ALPHA:  USR-PDP-02 Series Context — name + link + optional tier descriptor
  ├─ CHECK:  «Это серия ПРЕМИУМ-3, а не ПРЕМИУМ или ЭКОНОМ?»
  └─ EXIT:   series confirmed → continue │ wrong series → link to series listing
        ↓
Correct Model?
  │
  ├─ ALPHA:  USR-PDP-01 Identity (H1, article, copy)
  │          USR-PDP-04 Selected Properties (L×W×H×mass)
  │          USR-PDP-05 Category-Critical Properties (sections, bowl, material, construction)
  │          USR-PDP-06 Media (visual confirm)
  ├─ CHECK:  «Это ВМЦ-П3-2/500 1150×700×850, 2 секции, цельнотянутая?»
  └─ EXIT:   model confirmed → continue │ wrong SKU → USR-PDP-12 or USR-PDP-14
        ↓
Correct Specs?
  │
  ├─ ALPHA:  USR-PDP-08 Description (назначение, комплектация)
  │          USR-PDP-09 Minimum Spec Summary (5–8 rows, default-visible)
  │          USR-PDP-10 Full Specifications (tab/expand, 20+ rows)
  │          USR-PDP-11 Documents Entry
  ├─ CHECK:  «Параметры соответствуют проекту / ТЗ?»
  └─ EXIT:   specs OK → commercial │ need docs → USR-PDP-15 │ insufficient → USR-PDP-19
        ↓
Available?
  │
  ├─ ALPHA:  USR-PDP-03 Commercial Core (status, qty, price, CTA)
  │          USR-PDP-18 Commercial Detail (lead time if под заказ, delivery, dealer path)
  ├─ CHECK:  «В наличии / под заказ с известным сроком — могу оформить?»
  └─ EXIT:   available → cart │ под заказ with lead time → informed purchase or consult
        ↓
Alternative?
  │
  ├─ ALPHA:  USR-PDP-12 In-Series Alternatives (same series SKUs only)
  │          USR-PDP-13 Compare Feedback
  │          USR-PDP-14 Return-to-Series (with filter state)
  ├─ CHECK:  «Есть ли лучший размер/секции в ПРЕМИУМ-3?»
  └─ EXIT:   stay on SKU → convert │ switch sibling → new PDP │ return to series grid
        ↓
Inquiry / Purchase
  │
  ├─ ALPHA:  USR-PDP-03 primary CTA (cart)
  │          USR-PDP-19 Consultative CTA («Задать вопрос» / «Поможем подобрать»)
  │          USR-PDP-18 dealer/opt path
  │          USR-PDP-20 Trust Micro-Signals (compact)
  └─ OUTCOME: self-serve purchase OR human escalation OR dealer channel
```

**Отличие от текущего path:** Alpha **inserts explicit series gate** at top; **surfaces category-critical props** before tab depth; **replaces cross-family «Похожие»** with in-series continuation; **elevates consult** before buyer exhausts tabs.

---

## Trapeza Influences

**Правило:** только паттерны с evidence в findings. Trapeza = reference, not blueprint (D-03, R-01, X-04 rejected).

| Adopted idea | Evidence | Как проявляется в Alpha (IA only) |
|--------------|----------|-----------------------------------|
| **Structured specs on PDP** | W1D-F-04; W2 notes tabbed specs = Trapeza pattern | Full spec table retained (USR-PDP-10); not treated as anomaly |
| **Section-count as discriminating attribute** | W1D-F-03 («Количество секций» filter) | Category-critical hero prop for моечные ванны (USR-PDP-05); filter pattern on listing — not replacement of OEM series chips (Architecture P-08) |
| **First-screen model/identity fields** | W1D-F-04 (Trapeza «Модель» + brand link); X-01 partial | BZPM equivalent = **series context + article**, not marketplace brand index |
| **Information density / compact decision data** | W2 density benchmark; WH-20 (BZPM below Trapeza on semantic fields) | Minimum spec summary default-visible; hero extended beyond 4 props — **density through packaging** |
| **Compare infrastructure** | W1D-F-01, W1C-F-09 | Labeled compare + feedback (USR-PDP-07, USR-PDP-13) |
| **Thin-card context** (upstream, informs PDP arrival state) | W1D-F-10, V-12 | Buyer arrives with less pre-PDP discrimination — Alpha compensates on first screen |

**Explicitly NOT adopted from Trapeza:**

| Rejected pattern | Evidence |
|------------------|----------|
| Brand-index-first navigation | D-03, R-01 |
| Functional subtaxonomy replacing OEM series | W1D-F-02; Architecture P-01 |
| Sibling SKU matrix on PDP | W1D-F-09, V-09 |
| Marketplace scale / multi-brand flat listings as structural model | W1D-F-01, X-04 |
| Q&A community block | No BZPM evidence (Architecture §E Reference) |

---

## BZPM Identity Preservation

| Element | Evidence | Как сохраняется в Alpha |
|---------|----------|-------------------------|
| **OEM product-database model** | W1C-F-01, WH-10, V-08 | PDP = single-SKU evaluation surface; browse/series upstream |
| **Decision chain type → family → series → SKU** | W1C-F-01 | Series Context makes chain legible at SKU level |
| **OEM series as primary narrowing axis** | W1D rare pattern; W2-F-10 ПРЕМИУМ-3 benchmark | In-series alternatives scoped to series; not Trapeza functional chips |
| **ЗПМ manufacturing / OEM identity** | W0-F-04; Strategy trust themes | Trust micro-signals; «Сделано в России» near conversion — not import-brand logo |
| **Factory nomenclature (article codes)** | W1A-F-11; WH-03 | Article + copy in Identity block; codes not decoded in v1 (D-02 deferred) |
| **B2B / dealer workflow** | WH-15; CV-01 | Commercial Detail + dealer path + consultative CTA at conversion |
| **Stock honesty** | W1A-F-12; W1B-F-09 | Status + qty; lead time when под заказ |
| **4-level breadcrumb hierarchy** | W1A-F-10 | USR-PDP-00 mandatory |
| **Compare + wishlist infrastructure** | W1C-F-09 | Secondary actions with discoverability fix |
| **Product structure: selected props + full spec table** | W1A architecture «правильно заложено» (W1A audit) | Hero subset + full record separation (ID-01) — **preserved and clarified** |
| **Consultative layer** | W1D V-08; Henny Penny exception for wizards | Consultative CTA elevated — BZPM human layer, not task wizard |

**Узнаваемость:** покупатель всё ещё видит артикул ЗПМ, серию OEM, цену/наличие BZPM, breadcrumbs по заводской таксономии — но **получает ответы на вопросы серии и альтернатив**, которых текущая PDP не даёт.

---

## Expected Benefits

### Что становится проще для покупателя

- **Подтвердить серию** без reverse-engineering breadcrumbs
- **Оценить fit** по секциям, материалу, конструкции — не только по габаритам
- **Найти sibling SKU** в той же серии — без ухода в котломойки
- **Получить key specs** без переключения вкладок
- **Эскалировать в консультацию** до исчерпания tab depth

### Что становится быстрее

- **Expert path:** article → verify series + props → cart (WH-04)
- **Series path:** series listing → PDP → confirm or switch sibling via USR-PDP-12
- **B2B path:** commercial + dealer/delivery context adjacent to CTA — меньше hunting в header/footer
- **Compare path:** labeled action + feedback — меньше uncertainty (W1A-F-07)

### Что становится яснее

- **Scope of «похожих»:** in-series vs cross-family explicitly separated
- **Decision state:** buyer knows which gate passed (series · model · specs · availability)
- **Information ownership:** hero = subset; spec table = complete record — no false duplication
- **Trust:** placeholder/demo content removed from evaluation surface

*Без числовых claims — эффекты качественные, pending user validation.*

---

## Risks

### Potential downsides

| Risk | Description |
|------|-------------|
| **First-screen payload increase** | Series + category-critical props + commercial + media may increase cognitive load vs current sparse hero |
| **Content dependency** | Alpha assumes populated series descriptors, min spec rows, in-series relations — empty CMS fields collapse concept |
| **OQ-01 gap** | Category-critical props defined for моечные ванны; other families (столы, стеллажи, тепловое) — rule incomplete |
| **OQ-02 backend** | In-series alternatives may require CMS relation type change from current «Похожие» rules (U-05) |

### Potential over-compression

- Minimum spec summary + category-critical hero props + selected props — risk of **overlapping rows** if not governed by ID-01 packaging rule
- Mobile P1 stack (commercial first + series + props) — risk of **long first screen** before media

### Potential information overload

- Extending hero from 4 → 8+ attribute rows may **feel dense** for repeat buyers who need only article + price
- Elevating consultative CTA + commercial detail + trust signals — risk of **multiple competing CTAs** if not hierarchically ordered

### Potential implementation risks

| Risk | Source |
|------|--------|
| Tab vs inline packaging undecided | Concept = IA; wireframe must resolve without re-hiding Tier 2 |
| Gallery resize | WH-16 partial — layout decision deferred to design; IA alone may not fix «empty space» perception |
| Compare populated UX unknown | U-02 — feedback block depends on session behavior |
| Mobile priority inversion vs desktop | C-02 — decision-equivalent reorder must be validated with stakeholders |
| Cross-family block legacy | Removing default «Похожие» — content/merchandising pushback possible |

---

## Readiness Assessment

### Can this concept proceed to Wireframe?

**YES**

Концепт достаточно определён для wireframe phase: seven evaluation zones, block map (USR-PDP-00–21), decision ladder, first-screen boundaries, suppression list, and tier hierarchy — all traceable to approved W4–W6 artifacts. Alpha does not introduce new audit findings or scope beyond architecture.

### What must be validated next?

| # | Validation item | Owner / phase |
|---|-----------------|---------------|
| 1 | **First-screen boundary** — exact fold line desktop vs mobile P1/P2 | Wireframe |
| 2 | **OQ-01** — category-critical property set per product family beyond моечные ванны | Content / W1E deferred |
| 3 | **OQ-02** — CMS relation rule for in-series alternatives vs legacy «Похожие» | Technical discovery |
| 4 | **Tab vs inline** — packaging of USR-PDP-08/09/10/11 without re-creating hidden-tab problem | Wireframe |
| 5 | **CTA hierarchy** — primary cart vs consult vs dealer path ordering | Wireframe + stakeholder |
| 6 | **C-02 mobile block order** — commercial-first vs identity-first stakeholder acceptance | Wireframe |
| 7 | **ID-01 deduplication** — hero props vs min spec summary row governance | Content rules |
| 8 | **Empty states** — missing series descriptor, empty in-series set, no documents | Wireframe edge cases |
| 9 | **Cross-family related** — retain/suppress/label when no valid accessory relation | Merchandising decision |

---

## Traceability

| Concept section | Primary source |
|-----------------|----------------|
| Concept Name & Philosophy | Strategy §3; Architecture §E; W1A executive summary |
| Current vs Alpha | Findings Register W1A, W1C, W2; UX Structure §F resolution table |
| First Screen | Visual Prototype PDP; UX Structure §G6; Architecture hero zone |
| Information Hierarchy | Blueprint Zones 0–6; Architecture tier logic |
| Decision Flow | UX Structure decision path; Visual Prototype decision ladder |
| Trapeza Influences | W1D; Decision Log D-03, R-01; Findings V-09, X-04 |
| BZPM Preservation | W1C-F-01; Strategy §1, §5; Architecture P-01, P-07 |
| Risks | Visual Prototype C-02, C-04; UX Structure OQ-01, OQ-02 |
| Readiness | Visual Prototype readiness notes; Blueprint open questions |

---

*BZPM PDP Concept Alpha v1 — concept modeling only. No design, wireframes, Figma, Twig, CSS, or JS.*
