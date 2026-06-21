# REPORT — SITE-001 WF-V3 CLEAN ROOM DISCOVERY v1

**Type:** Clean-room discovery — documentation only  
**Date:** 2026-06-11  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Status:** WF-V2 = **FROZEN** · P0 Visual Gates = **ACTIVE**

**Mode:** Discovery / prototype planning — **no implementation**

**Explicit exclusions (honored):** No site modifications · No TEST writes · No FTP · No CSS · No Twig · No wireframes · No mockups · No charters · No new waves · No implementation plan

**Evidence base (negative lessons only — not design orienters):**

| Source | Role in this document |
|--------|----------------------|
| [P0-VISUAL-GATES-v1.md](../../../../governance/P0-VISUAL-GATES-v1.md) | Mandatory gates — confirmed before work |
| [SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md](../../governance/SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md) | Failure patterns to avoid |
| [SITE-001-AI-WORKFLOW-FAILURE-AUDIT-v1.md](SITE-001-AI-WORKFLOW-FAILURE-AUDIT-v1.md) | Root cause: composition vs cosmetic |
| [SITE-001-RESTORE-POINT-REGISTRY-v1.md](SITE-001-RESTORE-POINT-REGISTRY-v1.md) | WF-V2 freeze · clean-room intent |
| [SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md](SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md) | Operator/Proof Pack evidence — homepage weakest zone |
| [SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md](SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md) | Business surfaces · brand freeze |
| [SITE-001-W3C-DISCOVERY-v1.md](SITE-001-W3C-DISCOVERY-v1.md) | Contact · address · services inventory |

**Not used as design authority:** W3 · W4 · W5 · WF-V2 concepts, tokens, hooks, or implementation artifacts.

---

## P0 Rules — Confirmed Understanding

| Rule | Confirmation |
|------|--------------|
| **P0-01** Technical PASS ≠ Visual PASS | Two independent verdicts; authorization reads **visual only**. Past waves proved automated PASS masked product failure. |
| **P0-02** HITL Pending = Hard Stop | All SITE-001 visual waves remain operator **PENDING** — no implementation charter until discovery ratified + gates cleared. |
| **P0-03** Cosmetic Loop Cap | Max 2 failed visual passes → architecture review. Past program exceeded cap; WF-V3 must not repeat append-only strategy. |
| **P0-04** Clean Room Trigger | GAP vs target concept, legacy DOM ceiling, and concept conflict **all active** — prototype-first is mandatory path. |
| **P0-05** Agent Score Ban | This document uses **no agent-estimated perception scores**. Historical Proof Pack scores cited only as **operator evidence**, not as agent estimates. |

**If any rule were violated during execution → STOP.** This discovery honors all five.

---

## Executive Summary

**Главный вопрос:** не «что нам не нравится» (это задокументировано), а **каким должен быть СИБКАР** для покупателя за 3 секунды.

**Ответ:** СИБКАР — **региональный автосалон полного цикла** (пробег + новые + trade-in + кредит), где сайт = **цифровая витрина склада**, а не баннерный шаблон OpenCart. Доверие строится через **ясность, контакт и машину**, не через декоративные слои.

**Единственное рекомендуемое направление:** **Class B — Digital Inventory Showroom** (см. §5).

**Первый прототип:** Homepage first screen — зона с наибольшим perception gap по Proof Pack evidence; без неё 3-second test проваливается на entry route `/`.

---

# SECTION 1 — Business Reality

## 1.1 Кто покупатель СИБКАР

| Dimension | Reality |
|-----------|---------|
| **География** | Новосибирск и регион; физический адрес: ул. Богдана Хмельницкого 101 |
| **Сегмент** | Mass-market — не премиум-import, не luxury editorial |
| **Задача** | Найти конкретный автомобиль (марка · модель · бюджет), сравнить, приехать / позвонить / оформить кредит |
| **Поведение** | Прагматичный: цена · пробег · год · владельцы · trade-in · рассрочка |
| **Канал** | Телефон `+7 (383) 388-55-23` · WhatsApp · callback · визит в салон |
| **Доверие** | Нужен **местный надёжный дилер**, не «красивый сайт без цен» |

**Primary persona:** покупатель **авто с пробегом** — основной трафик и perception job-to-be-done.

**Secondary persona:** покупатель **нового авто** (`/auto/`, марки BAIC и др.) — тот же дилер, другой каталог.

**Tertiary persona:** trade-in / кредит / рассрочка — сервисные входы, не first-screen hero.

## 1.2 Какие автомобили продаются

| Категория | Route family | Examples (TEST evidence) |
|-----------|--------------|--------------------------|
| **Авто с пробегом** | `/cars/`, `/cars/{brand}`, product PDP | BMW, Hyundai, Audi и др. |
| **Новые автомобили** | `/auto/`, `/auto/{brand}` | BAIC и др. |
| **Сервисы** | `/tradein`, `/autocredit`, `/loan-terms` | Trade-in, кредит, условия |

Инвентарь = **реальный склад**, не агрегатор чужих объявлений. Сайт должен ощущаться как **«у них есть машины, я могу их найти»**.

## 1.3 Уровень доверия

| Must feel | Must NOT feel |
|-----------|---------------|
| «Здесь можно купить машину спокойно» | «Сайт из 2014 на OpenCart» |
| «Цены и контакты рядом» | «Скрыли цену за красивой картинкой» |
| «Салон в Новосибирске — реальный» | «Анонимный маркетплейс без лица» |
| «Проверено · trade-in · кредит — понятно» | «Акция кричит важнее машины» |

Доверие = **clarity + locality + inventory presence**, не luxury whitespace.

## 1.4 Какие эмоции нужны

1. **Уверенность** — «я в правильном месте»  
2. **Контроль** — «могу найти / отфильтровать / сравнить»  
3. **Спокойствие** — «не развод, нормальный дилер»  
4. **Готовность к действию** — «позвонить / записаться / посмотреть авто»

Не нужны: wow-декор, museum silence, discount panic.

## 1.5 Чего НЕ должно быть

| Anti-pattern | Why (past evidence) |
|--------------|---------------------|
| Три горизонтальных полосы header = instant OC-template read | Proof Pack: anatomy unchanged → visitor notice NO |
| Carousel-first homepage без search | First screen = «баннер», не «витрина» |
| Card-in-card · nested shadow stacks | Structural debt; subtractive passes could not undo |
| Competing red CTAs (phone + callback + WhatsApp + promo) | No single primary action |
| Sticky header | Operator rejected W4.1 sticky |
| Luxury editorial без красного СИБКАР | Brand mismatch for regional пробег |
| Append-only CSS as «redesign» | Cosmetic loop; perception ceiling on legacy DOM |
| Три параллельных design authority | Graphite vs Modern vs Light — cascade war |

---

# SECTION 2 — Visual Class Selection

Три класса — **новые рамки**, не копии прошлых concept IDs.

## Class A — Regional Trusted Dealer

**Описание:** Узнаваемый региональный автосалон. Сильный бренд, телефон, адрес, акции — **в привычной dealer-геометрии**, но аккуратно и профессионально. Header остаётся «дилерским», homepage — слайдер + преимущества, каталог — плотная сетка.

| | |
|---|---|
| **Плюсы** | Низкий риск «не мы»; быстрое узнавание для текущих клиентов; совместимо с Phase 1 copy |
| **Минусы** | **Не проходит 3-second transformation test** — силуэт OC-dealer сохраняется; повторяет failure mode «polish without composition» |
| **Совместимость с СИБКАР** | **Средняя** — честный для бизнеса, **слабый** для mandate «заметно иначе без A/B» |

## Class B — Digital Inventory Showroom

**Описание:** Сайт читается как **цифровой шоурум склада**: крупная типографика, поиск/фильтр на первом экране, машина доминирует над chrome. Header — **единая dealer shell** (не три полосы). PDP — **stage для одной машины** с ясным offer. Акции и кредит — **вторичны** относительно инвентаря.

| | |
|---|---|
| **Плюсы** | Matches primary job (найти авто); 3-second read «современный автосалон»; composition-first; реалистичен для clean-room HTML prototype |
| **Минусы** | Требует DOM recomposition — нельзя CSS-only на legacy; нужна дисциплина «один CTA» |
| **Совместимость с СИБКАР** | **Высокая** — региональный дилер **с современной витриной**, не luxury masquerade |

## Class C — Premium Inventory Platform

**Описание:** Восприятие **ценности каждой машины**: editorial whitespace, минимальный chrome, прозрачный header, типографика вместо promo. Каталог как галерея экспонатов. Красный и marquee убраны с first screen.

| | |
|---|---|
| **Плюсы** | Сильный wow; высокая визуальная дифференциация от OC-template |
| **Минусы** | **Brand mismatch** — клиенты пробега могут решить «дорого»; скрытые акции/trade-in; конфликт с Phase 1 red identity |
| **Совместимость с СИБКАР** | **Низкая** для mass-market пробега; **средняя** только для отдельной «премиум подборки» (out of scope) |

## Class D — Utility-First Auto Hub (дополнительный)

**Описание:** Портал-утилита: search bar доминирует, минимум визуального шума, почти нет «дизайна» — только фильтры, список, контакт. Как Avito-meets-dealer, не showroom.

| | |
|---|---|
| **Плюсы** | Максимальная ясность для power users |
| **Минусы** | Слабая эмоциональная дифференциация; риск «скучный каталог»; не решает brand uplift mandate |
| **Совместимость с СИБКАР** | **Средняя** как каталог-режим; **низкая** как единый brand direction |

---

# SECTION 3 — Competitive References

**Правило:** не копировать сайты. Извлекать **визуальные направления** (направление взгляда, иерархия, ритм).

## Reference 1 — Inventory-first regional dealers (EU/US patterns)

**Примеры направления:** Carvana-style clarity (не бренд), regional group sites с search-on-hero.

| | |
|---|---|
| **Нравится** | Машина + цена + CTA в одном взгляде; search как primary entry; мало горизонтальных полос |
| **Не нравится** | Полностью безличный marketplace; отсутствие «мы в Новосибирске» |
| **Взять** | Search/filters overlapping hero · large stable headline · featured inventory peek |

## Reference 2 — OEM digital showroom (Hyundai, Kia, VW configurator entry)

| | |
|---|---|
| **Нравится** | Unified header shell · centered nav · hero typography scale · cool neutral canvas |
| **Не нравится** | Слишком «новый автомобиль»; слабая used-car density; мало локального контакта |
| **Взять** | Single nav band · typography before decoration · static header (no sticky) |

## Reference 3 — Classified / aggregator UX (Auto.ru, Drom — layout grammar only)

| | |
|---|---|
| **Нравится** | Плотность информации на PDP; specs strip; price prominence |
| **Не нравится** | Рекламный шум; нет dealer trust layer; визуально generic |
| **Взять** | Spec chips · price hierarchy · «проверено дилером» trust strip |

## Reference 4 — Premium editorial auto (Lexus, Polestar — mood only)

| | |
|---|---|
| **Нравится** | Vehicle-as-hero photography · generous spacing · reduced chrome |
| **Не нравится** | Luxury palette · absent promo · serif editorial — wrong category for СИБКАР |
| **Взять** | **Только** «car first» composition rule — не palette or typography style |

## Reference 5 — Legacy OpenCart auto theme (anti-reference)

| | |
|---|---|
| **Нравится** | — |
| **Не нравится** | 3-band header · carousel promo · bordered card grid · dark modals · red everywhere |
| **Взять** | **Список запретов** для WF-V3 principles |

---

# SECTION 4 — First Impression Audit

**Метод:** Logo скрыт. 3 секунды. Только силуэт, цвет, типографика, композиция first screen.

**Вопрос:** «Это …»

## Class A — Regional Trusted Dealer

> **«Это обычный автосалон на готовом шаблоне — чуть причесали.»**

| Field | Value |
|-------|-------|
| Header read | Три полосы · лого слева · promo тикер |
| Homepage read | Слайдер акций · мелкий текст · красная кнопка |
| PDP read | Две колонки каталога · H1 над картинкой |
| 3-second transformation | **FAIL** — узнаваемый OC-dealer silhouette |
| СИБКАР recognition | Да, но **без upgrade** |

## Class B — Digital Inventory Showroom

> **«Это современный автосалон — можно сразу искать машину.»**

| Field | Value |
|-------|-------|
| Header read | Одна dealer shell · центрированная nav · контакт справа |
| Homepage read | Крупный заголовок · search card · машины в кадре |
| PDP read | Тёмная/нейтральная сцена · машина доминирует · цена в offer panel |
| 3-second transformation | **PASS** — не OC-template grammar |
| СИБКАР recognition | Да — красный акцент точечно · локальный контакт виден |

## Class C — Premium Inventory Platform

> **«Это премиальная галерея — красиво, но не похоже на наш салон пробега.»**

| Field | Value |
|-------|-------|
| Header read | Прозрачный · минимум chrome |
| Homepage read | Одна машина · много воздуха · нет акции |
| PDP read | Экспонат по центру · цена типографикой |
| 3-second transformation | **PASS** как premium · **FAIL** как СИБКАР |
| СИБКАР recognition | **Слабая** — category confusion |

## Class D — Utility-First Auto Hub

> **«Это каталог объявлений — функционально, но без лица салона.»**

| Field | Value |
|-------|-------|
| 3-second transformation | **PARTIAL** — не OC, но не dealership brand |
| СИБКАР recognition | Слабая эмоциональная связь |

---

# SECTION 5 — Design Authority Recommendation

## ONE Winner: **Class B — Digital Inventory Showroom**

### Почему один победитель

| Criterion | Class B |
|-----------|---------|
| **Business fit** | Primary job = найти авто с пробегом; trade-in/credit — secondary layers |
| **Trust model** | Clarity + local dealer, не luxury pretense |
| **3-second test** | Единственный класс с PASS на transformation **и** brand fit |
| **Operator mandate** | «Заметно иначе без A/B» требует **composition change** — B меняет геометрию first screen |
| **Clean-room necessity** | Legacy OC DOM не достигает этого класса CSS-only — GAP evidence supports prototype-first |
| **Phase 1 preservation** | Copy · URLs · phone · menu · red accent **точечно** — не wholesale rebrand |

### Почему не A

Повторяет доказанный failure mode: polish без смены силуэта. Proof Pack: homepage visitor notice **NO** при header polish.

### Почему не C

Региональный пробег + promo/trade-in culture ≠ luxury editorial. Operator risk «не мы» задокументирован в Concept Workshop evidence.

### Почему не D

Решает utility, не brand uplift. Недостаточно для mandate визуальной трансформации.

### Design authority statement (binding for WF-V3)

```text
СИБКАР = Digital Inventory Showroom
         (региональный дилер с цифровой витриной склада)

NOT = OpenCart template polish
NOT = Premium gallery
NOT = Utility-only catalog
```

**Supersession:** все prior visual directions (Graphite Salon · Modern Dealer 2026 · WF V2 Light Clean) — **retired as design authority**. Используются только как **error evidence** в reports.

---

# SECTION 6 — WF-V3 Principles

Принципы для clean-room prototype и будущей оценки. **10–20, composition-first.**

| ID | Principle |
|----|-----------|
| **P-01** | **Car first** — vehicle photography dominates first screen, not promo text |
| **P-02** | **Inventory is the hero** — homepage answers «what can I buy here?» before «what sale runs?» |
| **P-03** | **One dealer shell** — header = single composed block, not stacked horizontal bands |
| **P-04** | **No third promo strip** — marketing message lives inside nav shell or below hero, not as separate band |
| **P-05** | **Search is a first-class citizen** — filter/search visible on homepage first screen |
| **P-06** | **Typography before decoration** — scale and hierarchy do the work; not shadows and borders |
| **P-07** | **Flat surfaces** — max 2 container depths per zone; **no card-in-card** |
| **P-08** | **No decorative shadow stacks** — depth only where functionally needed (e.g. floating search card: one shadow level) |
| **P-09** | **One primary red CTA per screen** — phone/WhatsApp secondary, not competing |
| **P-10** | **Trust before promotion** — locality · contact · «проверено» before marquee CAPS |
| **P-11** | **Static header** — no sticky; header scrolls away with page |
| **P-12** | **Cool neutral canvas** — stone/light grey field; cards on canvas, not white-on-white merge |
| **P-13** | **PDP = single-vehicle stage** — gallery + offer panel, not symmetric catalog columns |
| **P-14** | **Price is the accent** — red reserved for price and one action, not scattered icons |
| **P-15** | **Composition before color** — DOM zones decided in prototype before token passes |
| **P-16** | **Prototype before merge** — no production TEST patches until isolated prototype operator ACCEPT |
| **P-17** | **Homepage gate** — first impression program cannot progress without homepage first screen in proof pack |
| **P-18** | **No legacy DOM as constraint** — prototype HTML defines target grammar; OpenCart mapping is phase 2 |
| **P-19** | **Preserve Phase 1 truth** — brand name · phones · address · legal · menu labels frozen |
| **P-20** | **Evidence not estimates** — visual verdict via operator HITL or Proof Pack only; no agent scores |

---

# SECTION 7 — Prototype Scope

**Format:** isolated static prototype — standalone HTML/CSS (or `prototype-*` folder). **Без OpenCart. Без Twig. Без FTP. Без интеграции.**

## In scope — Prototype v0.1

| Screen / artifact | Purpose |
|-------------------|---------|
| **Homepage first screen** | Primary 3-second test · search card · hero typography · featured peek |
| **Header (dealer shell)** | Single-shell composition · centered nav · inset promo pattern |
| **Used PDP first screen** | Single-vehicle stage · offer panel · spec chips |
| **One catalog card** | Card grammar for `/cars/` — flat, car-photo dominant (reference only) |
| **Composition spec** | Zone table per screen: DOM regions, anti-patterns, P-01..P-20 checklist |
| **Before/after capture plan** | Viewport 1440×900 + 390×844 · storage path per qa policy |

## Out of scope — Prototype v0.1

| Item | Reason |
|------|--------|
| Footer · modals · forms | Below first impression |
| New cars `/auto/` full flow | Secondary persona — v0.2 |
| Catalog grid · filters backend | No integration |
| Token/atmosphere FINISHING passes | After composition ACCEPT |
| OpenCart theme merge | Post-prototype charter |
| SEO · PHP · JS · DB | Not visual prototype |

## Prototype success criteria (operator-facing)

1. Logo hidden · 3 seconds · visitor sentence matches §4 Class B  
2. All P-01..P-10 visibly satisfied on static HTML  
3. Side-by-side with TEST screenshot — **composition** obviously different (not color-only)  
4. `VISUAL_ACCEPT` field ready for operator HITL — **no agent score**

## Deliverable paths (planned, not created by this task)

```text
projects/ocpilot/sites/site-001/prototype/wfv3-v0.1/
  homepage.html
  used-pdp.html
  composition-spec.md
  (screenshots → projects/ocpilot/sites/site-001/qa/wfv3-prototype-v0.1/)
```

---

# SECTION 8 — Final Decision

## Можно ли начинать WF-V3 Prototype?

| Layer | Verdict |
|-------|---------|
| **Discovery (this document)** | **COMPLETE** — design authority = Class B; principles defined; scope bounded |
| **Prototype design (HTML/CSS in repo)** | **CONDITIONAL YES** — after operator ratifies §5 direction |
| **Prototype implementation charter** | **NOT YET** — see blockers below |
| **Production TEST merge** | **NO** — forbidden until prototype operator ACCEPT |

### Blockers before implementation charter

| # | Blocker | Status |
|---|---------|--------|
| 1 | Operator ratification of Class B direction | **OPEN** — discovery must be reviewed |
| 2 | Operator visual review session (TEST vs baseline screenshots) | **OPEN** — all prior HITL **PENDING** |
| 3 | P0 knowledge docs (VISUAL-ACCEPTANCE-GATE · CSS-LAYER-BUDGET · WF DESIGN-AUTHORITY) | **OPEN** per integration plan |
| 4 | `qa/README.md` screenshot storage policy | **OPEN** |
| 5 | WF-V2 formal FREEZE decision artifact | **PARTIAL** — behavior effective; doc recommended |

### What to design first

**Priority 1: Homepage first screen**

Rationale:

- Entry route `/` — every visitor hits it first  
- Proof Pack evidence: homepage weakest zone; visitor notice **NO** after header-only waves  
- Homepage first screen never restructured in past program — largest perception gap  
- If homepage fails 3-second test, header and PDP improvements do not compound

**Priority 2 (after homepage ACCEPT):** Header dealer shell — depends on homepage hero overlap geometry

**Priority 3:** Used PDP first screen — single-vehicle stage

### Sequence (planning only)

```text
1. Operator reviews this discovery → ratify Class B or redirect     ← HITL
2. Publish remaining P0 knowledge docs (if not done)
3. Create prototype v0.1 homepage HTML in clean-room folder
4. Operator Proof Pack on prototype (not TEST)
5. If ACCEPT → header + PDP prototype screens
6. Only then → integration charter discussion (out of scope here)
```

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| Operator reaction to Class B (fresh framing) | **SAFE UNKNOWN** — pending HITL |
| Live inventory count on TEST | **NOT VERIFIED** — affects search card copy |
| WF-V2-W4 on live TEST | **LIKELY YES** — irrelevant to prototype; TEST frozen |
| Competitive reference URLs | **Directional only** — not fetched; no trademark copy |
| Production domain deployment | **Not in scope** |

**SECURITY RISK:** None identified (documentation only).

---

*SITE-001 WF-V3 Clean Room Discovery v1 — discovery only; no site modifications; no commit implied.*
