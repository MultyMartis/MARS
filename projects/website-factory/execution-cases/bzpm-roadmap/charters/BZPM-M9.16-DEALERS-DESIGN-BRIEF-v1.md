# M9.16 DEALERS DESIGN BRIEF

**Milestone:** M9.16 — Dealers / Дилерам  
**URL:** `/dealers`  
**Program:** BZPM Corporate Pages Program  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Version:** v1  
**Status:** DESIGN BRIEF — for designer handoff  
**Date:** 2026-06-22  

**Sources:** [Design Charter v1](./BZPM-M9.16-DEALERS-DESIGN-CHARTER-v1.md) · [Copy v1.1](../../../ocpilot/sites/site-002/copy/BZPM-M9.16-DEALERS-PAGE-COPY-v1.1.md)  
**Boundary:** Designer-facing brief only. No wireframes · no mockups · no implementation.

---

## Page type (read first)

**This page is a MANUFACTURER PARTNERSHIP PAGE.**

It is **NOT:**

- dealer recruitment page  
- franchise page  
- MLM page  
- lead generation landing  

**Visual order (locked):** Proof → Benefits → Process → Form  

OEM proof dominates. Benefits support OEM proof. Process supports benefits. Form finishes the conversation.

---

## 1. Purpose

Страница `/dealers` — главная точка входа для B2B-партнёров (дилеры, опт, проектные и интеграторские компании), которые оценивают сотрудничество с заводом ЗПМ. Задача дизайна — снять неопределённость канала: показать, что ЗПМ — производитель, а не посредник; что работа напрямую с заводом предсказуема и безопасна для репутации партнёра; и как начинается сотрудничество — до того, как посетитель дойдёт до квалификационной формы внизу страницы.

---

## 2. Audience

1. **Дилер / дистрибьютор HoReCa** — OEM-легитимность, защита канала, предсказуемый путь сотрудничества  
2. **Региональный поставщик / торговая компания** — самоквалификация, логистика, документы для перепродажи  
3. **Оптовый снабженец** — прямой контакт с заводом vs цепочка посредников  
4. **Интегратор / проектный партнёр** — путь к нестандартным позициям, указатель на Custom  
5. **Корпоративный клиент (сравнение каналов)** — redirect на прямую закупку через Payment  

---

## 3. Core Question

**Почему дилеру выгодно и безопасно работать именно с производителем ЗПМ?**

*(Не «как стать дилером за 30 секунд» и не «заполните форму».)*

---

## 4. Conversion Goals

| Tier | Goal |
|------|------|
| **Primary** | Квалификационная заявка — «Отправить заявку» после прочтения proof/benefits/process; параллельно — телефон и email в CTA-зоне |
| **Secondary** | Переход на `/about` — глубина о производстве до заявки |
| **Tertiary** | `/contact/` · каталог (текстовая ссылка) · Payment (микротекст) |

Форма — **endpoint**, не hero. Образовательные блоки визуально сильнее CTA-зоны.

---

## 5. Trust Signals

Максимум 10 — только высокоценные:

1. Собственное производство в Барнауле — юрлицо-производитель, не посредник  
2. Прямой контакт с заводом — единый источник информации по ассортименту, срокам, документам  
3. Документы для работы с клиентами партнёра — КП, счёт, закрывающие, сертификаты/декларации  
4. Стабильная серийная линейка нейтрального оборудования  
5. Изготовление на заказ по ТЗ — для проектных сценариев  
6. Таблица результатов партнёра — что конкретно получает партнёр (без % скидок)  
7. 5-шаговый процесс начала сотрудничества — предсказуемый путь  
8. Цепочка «завод → партнёр → конечный заказчик» — модель канала  
9. Честная channel policy — прямые продажи + партнёрская сеть; детали индивидуально  
10. Факты сущности — ИНН, Барнаул, ссылка на About  

---

## 6. Evidence Hierarchy

**Level 1 — первые ~2 экрана (без глубокого скролла):**  
H1 + Lead (manufacturer framing) · начало матрицы партнёров (BLOCK 01) · optional trust strip · OEM trust row (производитель, ИНН, площадка)

**Level 2 — ядро доказательств (середина страницы):**  
BLOCK 02 — пять H3 «почему напрямую с производителем» (пик OEM-аргументации) · BLOCK 03 outcome table · BLOCK 04 process timeline · BLOCK 05 supply chain + cross-link table · channel note

**Level 3 — поддержка (низкий визуальный вес):**  
Helper-тексты (условия индивидуально, нет публичного прайса) · FAQ (8) · warranty pointer (ссылка, без badge срока) · optional «Сделано в России»

---

## 7. Visual Priorities

Максимум 7 — **OEM proof dominates:**

1. **BLOCK 02** — стек H3 «почему партнёры работают напрямую с производителем» — главный визуальный якорь  
2. **OEM trust row** — производитель, ИНН, площадка, ссылка About  
3. **BLOCK 01** — матрица типов партнёров (SC-13) — самоквалификация «это про меня?»  
4. **BLOCK 03** — таблица результатов партнёра — tangible value без скидок  
5. **BLOCK 04** — timeline из 5 шагов (SC-04) — предсказуемость процесса  
6. **Channel note** (BLOCK 02) — честный ответ на страх конфликта каналов  
7. **Lead + H1** — manufacturer partnership frame, не recruitment headline  

---

## 8. Things That Must NOT Dominate

Максимум 10:

- **Скидки / % tiers / margin badges** — нет подтверждённых данных  
- **Partner counts** — «N дилеров по России»  
- **Dealer map / territory heatmap** — нет evidence  
- **Logos wall** — нет attested partner logos  
- **Franchise aesthetics** — tier badges, gold/silver/platinum, «уровни партнёра»  
- **MLM style** — pyramid diagrams, recruitment trees, downline language  
- **Giant form / form-as-hero** — форма above the fold или в hero  
- **Exclusivity claims** — «эксклюзивный дилер региона»  
- **Territory claims** — карта занятых территорий  
- **Recruitment style** — «станьте дилером сегодня», urgency banners, countdown, stock handshakes  

Дополнительно не доминируют: marketing support icon grid · MOQ badges · mid-page CTA buttons · FAQ как primary content · logistics map вместо простой цепочки.

---

## 9. Required Assets

### Must Have

- Approved copy v1.1 (все блоки 01–07 + FORM + FAQ)  
- OEM trust row data: юрлицо, ИНН 2221237587, площадка Барнаул  
- Partner matrix icons/tags (5 типов: dealer, wholesale, project, integrator, trading)  
- Process timeline visual (SC-04 — пятая corp-инстанция)  
- Supply chain diagram — простая вертикальная цепочка 4 узла (не карта)  
- Qualification form (SC-10 + company, city) — parity с Contacts discipline  
- Cross-link targets: About, Payment, Delivery, Warranty, Custom, Contacts  

### Nice To Have

- Optional trust strip (4 micro-labels после lead)  
- Minimal icons для matrix cards и chain nodes  
- «Сделано в России» badge с labeled disclaimer + link  

### Optional / Unavailable (do not invent)

- Partner logos / case studies — **нет assets в repo**  
- Territory map — **нет evidence**  
- Discount tiers / public price list visuals — **SAFE UNKNOWN**  
- Marketing support inventory icons — **не в copy**  
- Warranty term badge — owner: M9.17  
- ИНН field в форме — excluded per copy v1.1  
- Street address склада МО — **конфликт Basovskaya vs Nikolskoye**; использовать region-only prose до operator lock  

---

## 10. Design Risks

Максимум 7:

1. **Form hero drift** — страница читается как lead-gen landing; форма визуально сильнее education blocks  
2. **Franchise drift** — tier pyramids, program tiers, recruitment urgency  
3. **Proof deficit** — без OEM proof страница кажется «тонкой»; не компенсировать fake social proof  
4. **PLP/corp inconsistency** — форма сейчас на PLP, не на corp page; после ship corp form = primary  
5. **Fake partner proof** — invented logos, partner counts, territory map  
6. **Discount badge temptation** — «выгодные условия» как визуальный hero  
7. **Long page without hierarchy** — 7 блоков + form без tier weight → cognitive overload  

---

## 11. Success Criteria

Максимум 10 — оператор решает «дизайн работает», если:

1. Посетитель за <20 сек scan отвечает: «Это производитель? Безопасно ли работать напрямую?»  
2. Страница **не** читается как franchise / MLM / lead-gen landing  
3. BLOCK 02 OEM proof — самый сильный визуальный блок на странице  
4. Матрица партнёров помогает самоквалификации до формы  
5. Форма — endpoint: education blocks визуально доминируют над form zone  
6. Нет числовых commercial claims (%, MOQ, territory) без operator unlock  
7. Sibling topics — только summary + text link (CP-01), не embedded body  
8. Один primary CTA button zone (BLOCK 07) — нет mid-page submit  
9. Mobile ≤1024px: matrix и outcome table stack без horizontal scroll trap  
10. Нет fake logos, maps, partner counts  

---

## 12. One-Paragraph Summary

**Если читать только одно — читайте это.**

Страница `/dealers` — это **manufacturer partnership page**, а не recruitment landing. Дизайнер должен построить визуальную историю в порядке **Proof → Benefits → Process → Form**: сначала доказать, что ЗПМ — завод-производитель и работать с ним напрямую безопасно для репутации партнёра (BLOCK 02 + OEM trust row); затем показать, что конкретно получает партнёр (BLOCK 03) и как предсказуемо начинается сотрудничество (BLOCK 04); матрица типов партнёров (BLOCK 01) помогает самоквалификации, но не сильнее OEM proof. Форма «Заявка на сотрудничество» — финальная точка информированного разговора, не hero. Не использовать скидки, карты дилеров, logo walls, franchise/MLM эстетику и urgency-рекрутинг. Главный вывод для посетителя: **«Работа напрямую с производителем — предсказуемо, профессионально и безопасно.»**

---

## Readiness

| Dimension | Status |
|-----------|--------|
| Copy v1.1 | Ready (operator approval pending) |
| Charter v1 | Ready for operator review |
| Assets | Partial — structural design possible; no partner logos/map |
| Visual design | **Authorized to start** after operator approves this brief + charter |

---

*BZPM M9.16 Dealers Design Brief v1 — documentation only. No design deliverables authorized by this file alone.*
