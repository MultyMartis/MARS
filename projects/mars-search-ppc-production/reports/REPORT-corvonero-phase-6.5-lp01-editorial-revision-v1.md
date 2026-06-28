# REPORT — CORVONERO PHASE 6.5 LP-01 EDITORIAL REVISION V1

**Generated:** 2026-06-29  
**Scope:** LP-01 editorial revision v2 only — public copy package  
**Mode:** Local Cursor reasoning only

---

## 1. Safety

| Check | Status |
|-------|--------|
| External model API (OpenRouter) | **NONE** |
| Tilda / lk.corvonero.ru modified | **NONE** |
| Website (corvonero.ru) modified | **NONE** |
| Landing page published | **NOT AUTHORIZED** |
| Ad creation | **NONE** |
| v1 artefacts modified | **NONE** |
| Campaign architecture modified | **NONE** |
| Semantic registries modified | **NONE** |
| Commit / push | **Not performed** |

---

## 2. Input authority

| Artefact | Role |
|----------|------|
| `CORVONERO-PHASE-6.4-LP01-PRODUCTION-COPY-v1.*` | Baseline public copy |
| `CORVONERO-PHASE-6.4-LP01-MESSAGE-ARCHITECTURE-v1.*` | 13-layer structure (preserved) |
| `CORVONERO-PHASE-6.4-LP01-FIRST-SCREEN-VARIANTS-v1.*` | Variant A basis |
| `CORVONERO-PHASE-6.4-LP01-FAQ-v1.*` | FAQ baseline |
| `CORVONERO-PHASE-6.4-LP01-FORM-CONTACT-SPEC-v1.*` | Form/CTA/messenger spec |
| `CORVONERO-PHASE-6.4-LP01-TILDA-HANDOFF-v1.*` | Builder handoff baseline |
| Operator editorial decisions (Phase 6.5 task charter) | Revision authority |

---

## 3. Operator edits applied

| # | Decision | Applied in v2 |
|---|----------|-------------|
| 1 | First screen — Variant A with new H1/lead | Yes |
| 2 | Remove governance language from public copy | Yes |
| 3 | Audience block rewrite | Yes |
| 4 | Typical tasks — formal wording | Yes |
| 5 | Work format — remote/onsite only | Yes |
| 6 | Pricing — keep facts, remove package disclaimer | Yes |
| 7 | Process — five concise steps | Yes |
| 8 | Trust — positive evidence-only block | Yes |
| 9 | FAQ — 9 customer-facing items | Yes |
| 10 | Form — updated supporting text | Yes |
| 11 | Placeholders — implementation inputs only | Yes |

---

## 4. Removed governance language

Removed from all customer-facing v2 copy:

- «Страница предназначена для заказа услуг»
- «Мы не проводим обучение» / «не предлагаем вакансии»
- «Не публикуем кейсы» / «не заявляем статус официального партнёра»
- «Фиксированные пакеты, абонементы и скидки … не публикуются»
- «Обучение и продажа лицензий … не предлагаются» (FAQ)
- «Для рекламного трафика из Новосибирска…»
- FAQ question «Вы официальный партнёр 1С?»
- «Конкретное время реакции … не публикуем»
- Visible tokens: `REQUIRED_FROM_OPERATOR_OR_CLIENT`, `CURRENT_LINK_SAFE_UNKNOWN`

Restrictions remain in `CORVONERO-PHASE-6.4-LP01-ACCEPTANCE-CRITERIA-v1` and internal compliance sections.

---

## 5. First screen v2

| Element | Copy |
|---------|------|
| **H1** | Программист 1С для доработки, настройки и исправления ошибок |
| **Lead** | Решаем разовые задачи в 1С, дорабатываем конфигурации и восстанавливаем работу базы. Удалённо по России, с выездом в Новосибирске. |
| **Primary CTA** | Обсудить задачу |
| **Secondary CTA** | Получить оценку |
| **Phone** | +7 (383) 390-29-28 |

**Meta (Novosibirsk retained):** Title and description unchanged from v1 direction.

---

## 6. Page copy v2

Key section changes:

| Section | v2 H2 / headline | Notes |
|---------|------------------|-------|
| Audience | Услуги программиста 1С для компаний и ИП | Natural B2B wording |
| Typical tasks | Типовые задачи | «поплыла логика» → «перестали работать ранее выполненные доработки» |
| Work format | Формат работы | Advertising note removed |
| Pricing | Стоимость работы программиста 1С | Package disclaimer removed |
| Process | Как мы работаем | 5 concise steps |
| Service scope | Что делает программист 1С | Unchanged approved list |
| Configurations | Конфигурации 1С | УТ, УНФ, Розница, КА, БП |

Full copy: `CORVONERO-PHASE-6.5-LP01-PRODUCTION-COPY-v2.md`

---

## 7. Trust block v2

Replaced disclaimer-based block with positive facts:

- разовые задачи без найма штатного специалиста
- понятная почасовая модель (от 3 000 ₽/час, min 2 h)
- работа по договору с безналичной оплатой
- удалённое подключение по всей России
- выезд в Новосибирске
- конфигурации УТ, УНФ, Розница, КА, БП

No mention of absent cases, partner status, or certifications.

---

## 8. FAQ v2

**Count:** 9 items

| # | Question |
|---|----------|
| 1 | Какие задачи может выполнить программист 1С? |
| 2 | С какими конфигурациями 1С вы работаете? |
| 3 | Можно ли работать удалённо? |
| 4 | Выезжаете ли вы к клиенту? |
| 5 | Какой минимальный заказ? |
| 6 | Как рассчитывается стоимость? |
| 7 | Работаете ли вы по договору и безналичному расчёту? |
| 8 | Берёте ли вы срочные задачи? |
| 9 | Что нужно для первичной оценки? |

Removed: partner status question (was #10 in v1).

Full text: `CORVONERO-PHASE-6.5-LP01-FAQ-v2.md`

---

## 9. Form v2

| Field | Rule |
|-------|------|
| Имя | Optional |
| Телефон | Required |
| Submit | Заказать звонок |

**Supporting text:** Оставьте телефон — уточним задачу и сориентируем по стоимости.

Success/error messages remain implementation drafts in Tilda handoff v2. Consent legal text — implementation input, not visible production copy.

---

## 10. Implementation placeholders

Moved to handoff v2 `implementation_inputs` (not visible on production page):

| Input | Status |
|-------|--------|
| Messenger URLs (MAX, Telegram, WhatsApp) | Operator/client |
| Privacy policy URL | Operator/client |
| PD consent checkbox text | Operator/client |
| Legal entity footer details | Operator/client (LE-0006 reference) |
| OG image | Operator/client |
| Tilda project access | Operator → builder Roman |
| Analytics goal IDs | Launch prep |

Public contact block shows phone and messenger **labels** only.

---

## 11. Files created

| File | Path |
|------|------|
| Production copy v2 | `pilots/corvonero/CORVONERO-PHASE-6.5-LP01-PRODUCTION-COPY-v2.md` |
| Production copy v2 JSON | `pilots/corvonero/CORVONERO-PHASE-6.5-LP01-PRODUCTION-COPY-v2.json` |
| Message architecture v2 | `pilots/corvonero/CORVONERO-PHASE-6.5-LP01-MESSAGE-ARCHITECTURE-v2.md` |
| Message architecture v2 JSON | `pilots/corvonero/CORVONERO-PHASE-6.5-LP01-MESSAGE-ARCHITECTURE-v2.json` |
| FAQ v2 | `pilots/corvonero/CORVONERO-PHASE-6.5-LP01-FAQ-v2.md` |
| FAQ v2 JSON | `pilots/corvonero/CORVONERO-PHASE-6.5-LP01-FAQ-v2.json` |
| Tilda handoff v2 | `pilots/corvonero/CORVONERO-PHASE-6.5-LP01-TILDA-HANDOFF-v2.md` |
| Tilda handoff v2 JSON | `pilots/corvonero/CORVONERO-PHASE-6.5-LP01-TILDA-HANDOFF-v2.json` |
| Editorial changelog | `pilots/corvonero/CORVONERO-PHASE-6.5-LP01-EDITORIAL-CHANGELOG-v1.md` |
| Result | `pilots/corvonero/CORVONERO-PHASE-6.5-LP01-RESULT-v1.md` |
| Result JSON | `pilots/corvonero/CORVONERO-PHASE-6.5-LP01-RESULT-v1.json` |
| This report | `reports/REPORT-corvonero-phase-6.5-lp01-editorial-revision-v1.md` |

**Total:** 12 new files. v1 artefacts untouched.

---

## 12. Git status

Untracked new files under `projects/mars-search-ppc-production/` — no commit performed per task safety rules.

---

## 13. Verdict

```text
PHASE 6.5:
PASS — LP-01 COPY V2 READY FOR OPERATOR REVIEW

Landing page:
NOT BUILT

Website:
UNCHANGED

Tilda production:
NOT AUTHORIZED
```

---

## 14. Stop condition

Editorial revision v2 copy package complete. Awaiting operator review of v2 artefacts before Tilda build authorization.

**Next (out of scope):** Operator approves v2 → supplies implementation inputs → Phase 7 Tilda build per `CORVONERO-PHASE-7-NEXT-TASK-LP01-v1.md`.
