# REPORT — SITE-001 WF-V3 Homepage Discovery v1

**Type:** Homepage discovery — documentation only  
**Date:** 2026-06-11  
**Site:** SITE-001 — Автосалон СИБКАР  
**Program:** Website Factory · WF-V3  
**Mode:** Discovery / planning — **no implementation**

**Explicit exclusions (honored):** No HTML · No SCSS · No JS · No OpenCart · No OCPilot · No TEST · No FTP · No wireframes · No prototype · No commit implied

**Binding authority (inherit — do not reinvent):**

- [SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md](../governance/SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md)
- [SITE-001-WFV3-HOMEPAGE-PROTOTYPE-CHARTER-v1.md](../governance/SITE-001-WFV3-HOMEPAGE-PROTOTYPE-CHARTER-v1.md)
- [SITE-001-WFV3-CLEAN-ROOM-DISCOVERY-v1.md](SITE-001-WFV3-CLEAN-ROOM-DISCOVERY-v1.md)
- [SITE-001-WFV3-PDP-CONCEPT-ANALYSIS-v1.md](SITE-001-WFV3-PDP-CONCEPT-ANALYSIS-v1.md)

**Related blueprint:** [SITE-001-WFV3-HOMEPAGE-BLUEPRINT-v1.md](SITE-001-WFV3-HOMEPAGE-BLUEPRINT-v1.md)  
**Related decision:** [SITE-001-WFV3-HOMEPAGE-DECISION-v1.md](SITE-001-WFV3-HOMEPAGE-DECISION-v1.md)

---

## Executive Summary

Homepage СИБКАР в WF-V3 — **не отдельный продукт**, а **входной экран** того же Class B **Digital Inventory Showroom**, что и замороженный PDP. Задача Homepage — за 3 секунды ответить «здесь можно искать машину на складе», а не «здесь крутится акционный слайдер OpenCart».

Discovery подтверждает: **Class B остаётся в силе** для Homepage. Новый визуальный язык **запрещён**. Все решения наследуют PDP freeze (header, tokens, trust tone, CTA discipline, flat surfaces).

---

# SECTION 1 — Homepage Purpose

## 1.1 Какую работу выполняет Homepage

Homepage — **маршрутизатор витрины склада**, не landing акций.

| Job | Описание |
|-----|----------|
| **Primary** | Быстро направить посетителя в **поиск / каталог авто с пробегом** — основной трафик и persona |
| **Secondary** | Показать **наличие реального инвентаря** (featured peek) до ухода в `/cars/` |
| **Tertiary** | Подтвердить **локального надёжного дилера** (Новосибирск, контакт, проверка) |
| **Quaternary** | Дать вторичные входы: кредит, trade-in, новые авто — **после** inventory path |

Homepage **не** продаёт одну машину (это PDP). Homepage **не** заменяет каталог фильтрами. Homepage **открывает** путь «найти → сравнить → открыть PDP».

## 1.2 Первые 3 секунды — обязательный результат

Без чтения текста и без опоры на логотип посетитель должен **увидеть**:

1. **Поиск / фильтр** или явный inventory entry — не спрятан в меню  
2. **Автомобиль в кадре** — фото машины, не абстрактный баннер акции  
3. **Спокойную dealer shell** — одна composed header-грамматика, не три полосы OC + carousel  

Эмоциональный итог: **«современный автосалон — можно сразу искать машину»** (charter + clean-room discovery §4 Class B).

## 1.3 Чем Homepage помогает посетителю

| Помощь | Механизм |
|--------|----------|
| Найти авто по марке / бюджету | Search-first entry → `/cars/` |
| Убедиться, что машины есть | Featured inventory peek с ценой и фото |
| Понять, что дилер местный и настоящий | Topbar locality + trust layer |
| Перейти к кредиту / trade-in | Secondary CTA и nav «Услуги» — не first-screen hero |
| Позвонить / callback | Header red pill + topbar phone |

## 1.4 Приоритет задач (ранжирование)

| Rank | Task | Rationale (discovery evidence) |
|------|------|--------------------------------|
| **P0** | **Найти авто с пробегом** | Primary persona; clean-room §1.1; P-01, P-02 |
| **P1** | **Просмотреть инвентарь / витрину** | «У них есть машины» — §1.2 inventory presence |
| **P2** | **Оценить дилера (доверие)** | Clarity + locality — §1.3; не luxury pretense |
| **P3** | **Trade-in** | Tertiary persona — §1.1; secondary на PDP |
| **P4** | **Кредит / рассрочка** | Supporting на PDP (Z7); hook в benefit row |
| **P5** | **Контакт / визит** | Канал §1.1; phone в topbar всегда виден |
| **P6** | **Новые авто (`/auto/`)** | Secondary persona — не first-screen hero |

**Anti-priority (не first screen):** rotating promo carousel, marquee CAPS, «акция важнее машины».

---

# SECTION 2 — Homepage Class Validation

## 2.1 Кандидат: Class B — Digital Inventory Showroom

| Criterion | Homepage fit |
|-----------|--------------|
| Primary job = find used car | **YES** — search + featured inventory |
| 3-second test vs OC template | **YES** — composition change mandatory (Proof Pack: homepage visitor notice NO) |
| Brand fit for regional mass-market | **YES** — не Class C premium |
| PDP alignment | **YES** — same class frozen in PDP authority |
| Operator mandate «заметно иначе» | **YES** — carousel-first FAIL documented |

## 2.2 Почему Class B подходит Homepage

Homepage и PDP — **два экрана одного продукта**:

- PDP = **single-vehicle stage** (P-13)  
- Homepage = **inventory entry stage** (P-02)  

Оба используют: one dealer shell (P-03), search/inventory first (P-05), flat surfaces (P-07), one red CTA per zone (P-09), static header (P-11).

Class A (Regional Trusted Dealer) **отклонён** — сохраняет OC silhouette; Proof Pack подтверждает failure mode.  
Class C **отклонён** — brand mismatch для пробега.  
Class D **отклонён** — utility без dealer face.

## 2.3 Freeze statement

```text
SITE-001 Homepage = Class B — Digital Inventory Showroom
Inherits WF-V3 PDP design authority — no new visual class
FROZEN for homepage discovery v1 — 2026-06-11
```

Изменение класса Homepage = **authority review** (PDP freeze §3 Change gate).

---

# SECTION 3 — 3-Second Test

## 3.1 Метод

- Viewport desktop ≥ 1280px (aligned with PDP freeze)  
- Logo **скрыт**  
- Экспозиция **3 секунды**  
- Оценка: силуэт, цвет, типографика, композиция **first screen only**

## 3.2 Ожидаемое восприятие (exact)

> **«Это современный автосалон — можно сразу искать машину.»**

## 3.3 Детализация first-screen read

| Signal | Expected perception |
|--------|---------------------|
| **Header silhouette** | Две composed bands (dark meta + white nav) + optional light USP band — **не** три OC-полосы + marquee |
| **Hero zone** | Крупный стабильный заголовок + **search card** + машина(ы) в кадре — **не** full-width promo carousel |
| **Color discipline** | Cool neutral canvas; красный **точечно** (один primary action + акcent price на карточках) |
| **Density** | Inventory showroom — информация о машинах видна сразу |
| **Locality** | Новосибирск / телефон читаются в chrome — «реальный салон рядом» |

## 3.4 FAIL sentences (anti-patterns)

| Sentence | Trigger |
|----------|---------|
| «Обычный автосалон на шаблоне OpenCart» | Carousel-first, 3-band header, no search |
| «Красивый баннер, но где машины?» | Abstract hero, no inventory peek |
| «Премиальная галерея — не наш пробег» | Class C whitespace, hidden promo |
| «Каталог объявлений без лица» | Class D utility-only |

## 3.5 Relationship to TEST baseline

W4.1 Proof Pack: homepage first screen **3/10**; visitor notice **NO** — carousel и anatomy unchanged. WF-V3 Homepage **must** fail side-by-side comparison with TEST on **composition**, not color-only tweak.

---

# SECTION 4 — Discovery Evidence Synthesis

## 4.1 Current state (TEST — negative reference only)

| Zone | Problem |
|------|---------|
| First screen | Carousel-first promo slider |
| Search | Not visible on first screen (P-05 violation) |
| Header | OC three-band read despite W4 polish |
| Trust | four_blocks disconnected below unrelated hero |
| Perception | Entry route `/` blocks 3-second Class B test |

## 4.2 Target state (WF-V3 — inherits PDP)

| Zone | Direction |
|------|-----------|
| First screen | Stable inventory headline + search + car photography |
| Header | Frozen PDP shell — shared partial grammar |
| Trust | Same proof tone as PDP Z5 — not marquee CAPS |
| Footer | Frozen PDP dark inverse — shared partial |
| Visual system | PDP v0.2 tokens — Inter, surfaces, brand red |

## 4.3 Business truths preserved (P-19)

Brand **СИБКАР** · phone **+7 (383) 388-55-23** · address **ул. Богдана Хмельницкого 101** · menu labels · legal links — unchanged from Phase 1 freeze.

---

# SECTION 5 — Risks & Constraints

| Risk | Mitigation |
|------|------------|
| No homepage concept PNG | Derive zones from blueprint + PDP tokens; PDP PNG = system anchor |
| Carousel habit from legacy | Explicit anti-pattern in charter + discovery |
| Search becomes decorative | P-05 HITL gate — must be first-screen weighted |
| Header drift from PDP | Mandate shared partial — no redesign |
| Inventing new design language | This discovery **forbids** — inherit freeze only |

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| Homepage concept PNG | **SAFE UNKNOWN** — only PDP PNG confirmed; zones from discovery + blueprint |
| Live inventory count on TEST | **NOT VERIFIED** — affects featured card copy only |
| Operator ratification Class B for homepage | **OPEN** — pending HITL |
| Exact featured vehicle selection rules (CMS) | **OPEN** — business rule at integration; prototype uses static set |
| Mobile homepage authority | **SAFE UNKNOWN** — desktop-first per PDP freeze; responsive = allowed change later |

**SECURITY RISK:** None (documentation only).

---

*SITE-001 WF-V3 Homepage Discovery v1 — discovery only; no implementation; no commit implied.*
