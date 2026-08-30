# I-SEO Report Hub — Client Preview Report 1 Demo Copy v0.1

**Status:** target copy pack for Option A (render-layer)  
**Date:** 2026-08-21  
**Audience:** client preview / print for report id **1** in local/demo only  
**Language:** Russian  
**Rules:** no fake numbers; no fake traffic/positions/leads; client-safe; concise

---

## 1. Usage rules

| Rule | Detail |
|------|--------|
| Apply to | Report **1** client preview/print when section empty after sanitize (local/demo) |
| Prefer live | Work-entry assembly text for auto sections when available |
| Do not apply to | Report **5** empty draft; other true empty drafts |
| Do not write to | DB, PDF, export, share |
| Metrics | Honest MVP disclaimer only — never invent KPIs |

Section keys ↔ headings:

| Key | Heading |
|-----|---------|
| `executive_summary` | Краткое резюме |
| `results_summary` | Результаты |
| `work_completed` | Что сделали |
| `key_findings` | Ключевые выводы |
| `risks_and_blockers` | Риски и блокеры |
| `next_month_plan` | План на следующий месяц |

---

## 2. Краткое резюме (`executive_summary`)

**Draft copy (paragraph):**

```
В июле была выполнена базовая SEO-подготовка проекта: проверены технические факторы, собраны приоритетные группы запросов, подготовлены рекомендации по коммерческим страницам и сформирован план работ на следующий месяц.
```

---

## 3. Результаты (`results_summary`)

**Draft copy (paragraph) — no fake metrics:**

```
Количественные показатели в текущей версии MVP не заполняются автоматически. В отчете зафиксированы выполненные работы, подготовленные рекомендации и план следующего этапа.
```

---

## 4. Что сделали (`work_completed`)

**Preferred source:** in-memory assembly from current work entries (done items), using existing assembly intro/bullet contract when available.

**Fallback body (when assembly unavailable / empty):**

```
В течение месяца выполнены основные SEO-работы:

- Проведен технический мониторинг сайта.
- Проверена индексация ключевых страниц.
- Актуализирована семантика по приоритетным группам.
- Подготовлены рекомендации по коммерческим факторам.
```

Notes:

- Aligns with fixture themes (technical monitoring, indexation, semantics, commercial factors).
- Keep bullet style compatible with `ClientReportDocument::formatBodyHtml` (`- ` lines).

---

## 5. Ключевые выводы (`key_findings`)

**Draft copy (bullets):**

```
- Сайту требуется продолжение технического мониторинга и контроль индексации.
- Приоритетные страницы нужно привести в соответствие по коммерческим факторам.
- Семантические группы и подготовка текстов — база для следующего этапа роста.
```

---

## 6. Риски и блокеры (`risks_and_blockers`)

**Preferred source:** work-entry risk assembly when available.

**Fallback body:**

```
На текущий момент требуют внимания:

- Требуется согласование приоритетных страниц для следующего этапа работ.
```

Tone: calm, not red-alert. Do **not** invent additional blockers.

---

## 7. План на следующий месяц (`next_month_plan`)

**Preferred source:** planned work-entry assembly when available.

**Fallback body:**

```
В следующем периоде запланированы работы:

- Доработать мета-теги для приоритетных страниц.
- Подготовить новые тексты для выбранных разделов.
- Продолжить улучшение коммерческих факторов.
```

---

## 8. Report 5 / empty draft behavior

| Object | Behavior |
|--------|----------|
| Report 5 preview | Keep calm empty-section messages; **no** demo pack |
| Other empty drafts | Same — no show-ready fill |
| Finalized empty-looking report 1 in local | Apply this pack per section when empty |

Empty messages that remain valid for true empties (unchanged product intent):

- default: «Раздел будет заполнен после ручной редакции.»
- results: metrics-not-filled calm line
- risks empty: «Существенных рисков… не зафиксировано.» (only when no risk content and no demo fill)

---

## 9. Explicit non-goals for this copy pack

- No delivery/PDF/export text changes.
- No share page copy changes.
- No English demo junk.
- No “lorem / test body / updated body” placeholders.
- No invented KPI tables or charts.
