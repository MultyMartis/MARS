# M9.18 CUSTOM MANUFACTURING DESIGN BRIEF

**Milestone:** M9.18 — Custom Manufacturing / Оборудование на заказ  
**URL:** `/custom-equipment`  
**Program:** BZPM Corporate Pages Program  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** DESIGN BRIEF — for visual design phase  
**Sources:** Design Charter v1 · PAGE-COPY v1.1 · Forensic Research (condensed)

**Boundary:** Designer-facing brief only. No wireframes · no mockups · no implementation.

---

## Page type (read first)

**This page is a MANUFACTURER CAPABILITY PAGE.**

It is **NOT:**

- calculator
- tender portal
- engineering dashboard
- specification database
- lead generation page

**Dominant visual order:**

Capability → Process → Requirements → Outcome → Form

- **OEM capability** must dominate.
- **Process** proves capability.
- **Checklist** prepares the conversation.
- **Form** finishes the conversation.

---

## 1. Purpose

Страница `/custom-equipment` — главная поверхность SITE-002 для изготовления нейтрального оборудования из нержавеющей стали на заказ. Она доказывает, что **ЗПМ как производитель** способен взять нестандартный проект и провести его от описания задачи до отгрузки — с честными границами scope, без выдуманных цен, сроков и инженерных SLA. Это не второй каталог, не тендерный портал и не SEO-статья «пришлите ТЗ и ждите».

---

## 2. Audience

1. **Технолог / инженер** — scope fit, ответственность за проект, чеклист данных, ворота процесса.
2. **Снабженец / закупщик** — предсказуемый OL, документы, указатели на оплату и доставку.
3. **Владелец предприятия** — снижение риска: производитель отвечает, согласование до цеха.
4. **Интегратор пищевого производства** — матрица задач, мост к каталогу, повторный заказ.
5. **Дилер с проектными клиентами** — доказательство компетенции завода + ссылка на `/dealers`.

---

## 3. Core Question

**Может ли этот завод изготовить нестандартное оборудование под мою задачу — и насколько предсказуемо это пройдёт?**

---

## 4. Conversion Goals

**Primary:** Отправка заявки на расчёт — форма SC-11 «Отправить заявку на расчёт» после понимания scope, процесса и ожиданий по данным. Параллельно: телефон `8 (3852) 72-18-90` и `info@bzpm.ru` в шапке и CTA-зоне.

**Secondary:** Переход на `/contact/` — адрес, реквизиты, общий контакт вне рамок custom-заявки.

**Tertiary:** Переход в каталог `/` — доработка серийной модели; указание артикула в форме.

---

## 5. Trust Signals

1. Прозрачный 8-шаговый процесс (заявка → уточнение → КП → согласование → оплата → изготовление → контроль → отгрузка).
2. Ворота **«Согласование до производства»** — параметры фиксируются до цеха.
3. Производитель, а не посредник — собственная площадка в Барнауле, ответственность за результат.
4. Честные границы scope — нейтральная нержавейка в профиле; тепловое/холодильное — только каталог.
5. Чеклист данных для расчёта — что передать и зачем; можно начать с короткого описания.
6. Таблица результатов — изделие, согласованная конфигурация, документы, гарантия.
7. Мост к каталогу — доработка серийной модели быстрее, чем проект с нуля.
8. Материалы согласуются в КП — без универсальной таблицы марок на странице.
9. Якорь «Сделано в России» — ссылка на `/our-certification`.
10. Соседние политики — одна строка + ссылка (Оплата, Доставка, Гарантия, Дилерам).

---

## 6. Evidence Hierarchy

**Level 1 — без глубокого скролла (~2 экрана):** H1 + lead (производитель изготавливает на заказ); BLOCK 01 — когда нужен заказ; начало SC-04 (шаги 1–3); примечание о границах scope (нейтральная SS).

**Level 2 — середина страницы:** полный SC-04 (8 шагов) — **пиковый визуал**; badge «Согласование до производства»; BLOCK 04 OEM proof + production image; BLOCK 06 SC-06 checklist; BLOCK 03 scope table; BLOCK 02 task matrix; BLOCK 08 outcome table.

**Level 3 — нижний вес:** BLOCK 07 materials (prose); FAQ (8); cross-links summary; timeline note без SLA-чипов; dealer pointer одной строкой.

---

## 7. Visual Priorities

1. **BLOCK 04 — OEM capability** — производитель, ответственность, proof strip + production image (вес 4/5).
2. **BLOCK 05 SC-04 — 8-шаговый процесс** — главный структурный якорь (вес 5/5); process proves capability.
3. Badge **«Согласование до производства»** — визуальный beat целостности процесса.
4. **BLOCK 06 SC-06** — чеклист данных как подготовка к шагам 1–2 (вес 4/5, ниже процесса).
5. **BLOCK 03** — scope groups + in/out table; не карточки каталога.
6. **BLOCK 08** — таблица того, что получает заказчик.
7. **BLOCK 10 + SC-11 FORM** — единственная primary CTA-зона внизу; form finishes the conversation.

---

## 8. Things That Must NOT Dominate

- **Calculator UI** — слайдеры размеров, live estimate, конфигуратор.
- **Price promises** — диапазоны, «от … ₽», факторы цены как hero.
- **Lead-time promises** — countdown-чипы «от 14 дней», SLA-бейджи.
- **Tender aesthetics** — многошаговый RFP, обязательные вложения, legal field wall.
- **Technical overload** — универсальная таблица AISI, datasheet hero в BLOCK 07.
- **Engineering dashboard style** — CAD viewer, DWG embed, workflow diagrams.
- **Fake portfolio** — placeholder case studies, stock kitchen photos.
- **Upload-first UX** — drag-drop hero, «прикрепите полное ТЗ» как gate.
- **Giant specification tables** — 9-row parameter matrix как главный объект.
- **Procurement bureaucracy** — тендерная форма, мульти-file wizard, ИНН/УЛ wall.
- **Form above fold** — «отправьте ТЗ и ждите» anti-pattern.
- **Catalog PLP mimic** — SKU cards, цены, фильтры в BLOCK 03.

---

## 9. Required Assets

**Must Have**

- SC-04 process timeline (8 шагов — custom-specific labels).
- SC-06 requirements checklist (9 строк + helper «можно начать с короткого описания»).
- SC-08 FAQ accordion (8 вопросов).
- SC-09 CTA band + SC-11 custom form (product_type, description, region, contact, consent; optional: quantity, deadline, catalog link, file).
- BLOCK 04 proof strip + **один** production image slot (reuse About factory photo if attested).
- BLOCK 03 scope boundary table (in/out).
- BLOCK 02 task matrix (7 rows).
- BLOCK 08 outcome table (5 rows).
- Корп-ритм SC-01 — как Contacts: breadcrumb, H1, lead, секции H2.

**Nice To Have**

- 3 value chips под lead (собственное производство · согласование до цеха · по вашему ТЗ).
- Компактная companion table параметров (BLOCK 06 micro) — вес 2/5.
- Footer cross-links table (Оплата · Доставка · Гарантия · Дилерам · О компании).

**Optional / Unavailable**

- Case study gallery (0–3) — **EXCLUDED** until operator provides assets (OQ-DC-C16).
- Sanitized drawing thumbnails — **EXCLUDED**.
- Lead-time / price / MOQ badges — **EXCLUDED** without operator unlock.
- Multi-file upload UI — **DEFERRED**; single optional file MVP with email fallback.

---

## 10. Design Risks

1. **Calculator drift** — dimension sliders, price hints, «конструктор заказа».
2. **Tender-form drift** — required TZ, multi-doc upload, legal field explosion.
3. **Upload dependency** — форма требует чертёж; drag-drop zone как hero.
4. **Fake proof** — placeholder projects, stock factory photos, anonymized galleries.
5. **Catalog conflict** — BLOCK 03 читается как PLP с ценами и карточками.
6. **Scope confusion** — страница обещает «машиностроение» без границы neutral SS.
7. **Form-first page** — SC-11 above fold; mid-page submit buttons.

---

## 11. Success Criteria

1. За <15 секунд сканирования понятно: **что можно заказать** и **входит ли моя задача в scope**.
2. За <25 секунд понятен **8-шаговый процесс** — как завод проведёт проект.
3. Страница не читается как калькулятор, тендерная форма или каталог PLP.
4. BLOCK 04 OEM capability видна; **process + capability доминируют** над формой.
5. Нет price/lead-time badges без операторского unlock.
6. Одна primary CTA-зона — форма только после FAQ (BLOCK 10).
7. SC-11 содержит **product_type**, **description**, **region**; consent как на Contacts.
8. BLOCK 06 читается как «подготовка к шагам 1–2» SC-04 — визуальная связь с процессом.
9. BLOCK 03 визуально отличим от каталога — prose + links, не product cards.
10. Дизайнер и оператор сходятся: **производитель способен решить нестандартную задачу предсказуемым способом**.

---

## 12. One-Paragraph Summary

**Если прочитать только одно — прочитайте это.**

Страница `/custom-equipment` — **страница производственной компетенции**, а не калькулятор, тендерный портал, инженерный дашборд или лидогенератор. Главный визуальный порядок: **Capability → Process → Requirements → Outcome → Form**. OEM-доказательство (BLOCK 04) и **8-шаговый SC-04** — spine страницы; чеклист данных (SC-06) готовит разговор; форма SC-11 завершает его после образования. Нет цен, сроков-чипов, fake portfolio и каталоговых карточек. Дизайнер должен уйти с одним выводом: **производитель способен решить нестандартную производственную задачу предсказуемым способом**.

---

*BZPM M9.18 Custom Manufacturing Design Brief v1 — documentation only. No design, wireframes, mockups, or implementation authorized.*
