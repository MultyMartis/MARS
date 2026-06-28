# CORVONERO Phase 6.4 — LP-01 First-Screen Variants v1

**Landing page:** LP-01  
**Implementation note:** One page — variants are copy options for first screen only; **Variant A recommended default** for v1.

---

## Recommendation

**Default for LP-01 v1: Variant A (specialist intent)**

Rationale: 384 of 404 CA-01 phrases (95%) map to `ca-01-specialist-search` / SPECIALIST_SEARCH. Variant A maximizes message match for primary traffic while Variants B and C elements are covered in lower-page sections (typical tasks, process).

---

## Variant A — Specialist intent

**Target:** Users searching for a 1C programmer or specialist.

| Element | Copy |
|---------|------|
| **H1** | Программист 1С в Новосибирске — услуги специалиста |
| **Supporting text** | Центр автоматизации «Корво Неро» подключает программиста 1С для разовых задач, доработок и сопровождения вашей базы. Работаем удалённо по всей России, выезжаем на объект в Новосибирске. |
| **Primary CTA** | Обсудить задачу |
| **Secondary CTA** | Получить оценку |

**Phrase / intent families:** программист 1с, специалист 1с, 1с программист, программист 1с новосибирск, программист 1с удаленно, найти программиста 1с

**Mismatch risks:**

- Career queries (с нуля, вакансия) excluded from ads but may still appear — lead must not promise обучение.
- «Удалённо» seekers must see Russia remote scope immediately in supporting text.
- Moscow/other city geo modifiers in queries — page is Novosibirsk-campaign focused; remote scope clarifies national service.

---

## Variant B — Task / result intent

**Target:** Users needing a specific 1C task completed.

| Element | Copy |
|---------|------|
| **H1** | Выполним задачу в 1С — доработка, отчёты, интеграции |
| **Supporting text** | Опишите, что нужно сделать в вашей базе 1С: исправить ошибку, доработать конфигурацию, настроить обмен или маркировку. Подключим программиста 1С удалённо или с выездом в Новосибирске. |
| **Primary CTA** | Получить оценку |
| **Secondary CTA** | Обсудить задачу |

**Phrase / intent families:** доработка 1с, отчёт 1с, интеграция 1с, настройка 1с, услуги программиста 1с

**Mismatch risks:**

- Specialist-search traffic (384 phrases) may find H1 less literal on «программист» — weaker message match vs Variant A.
- Task-first H1 may under-emphasize price-intent visitors — pricing block must remain prominent below fold.

---

## Variant C — Urgent / problem intent

**Target:** Users whose 1C system is not working or has errors.

| Element | Copy |
|---------|------|
| **H1** | 1С не работает или выдаёт ошибку — поможем восстановить |
| **Supporting text** | Разберёмся с ошибками, сбоями после обновления и проблемами в учёте. Программист 1С подключится удалённо по России или приедет в Новосибирск. Стоимость — от 3 000 ₽ в час, минимальный заказ 2 часа. |
| **Primary CTA** | Заказать звонок |
| **Secondary CTA** | Обсудить задачу |

**Phrase / intent families:** ошибка 1с, не работает 1с, срочно 1с, восстановить 1с, помощь 1с

**Mismatch risks:**

- Implies urgency/SLA tone — must not promise response time (supporting text includes price, not speed).
- Narrow problem framing may mismatch broad specialist-search queries.
- «Срочно» intent may expect 24/7 — page must not claim round-the-clock support.

---

## Variant selection matrix

| Ad group | Best variant | Notes |
|----------|--------------|-------|
| ca-01-specialist-search (384) | **A** | Primary traffic |
| ca-01-price-intent (16) | A or C | C mentions price early; A + pricing block also works |
| ca-01-direct-service-order (4) | B or A | B slightly better for «услуги» |

**Ship decision:** Use **Variant A** on LP-01 v1; retain B and C as approved alternates for A/B test after launch if operator authorizes.
