# I-SEO Report Hub — Summary Assembly UX Flow v0.1

**Status:** CHARTER / UX — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Charter 01  
**Mode:** Option A — preview-only

---

## 1. Entry point

**Where:** `/monthly-reports/{id}` panel «Работы за месяц» (`#work-entries`).

**Control:** secondary button next to existing «Добавить работу» / «Предпросмотр отчета»:

- Label: **Собрать черновик из работ**
- Href: `/monthly-reports/{id}/assembly-preview`
- Visible to the same internal roles that can view the monthly report
- Not a POST; no CSRF

Keep the existing subtitle that entries do not auto-build the client PDF. After Implementation 01, add one sentence:

> Можно посмотреть черновик клиентских разделов — без изменения отчета и PDF.

---

## 2. Route

```
GET /monthly-reports/{id}/assembly-preview
```

Auth: internal role required (same as monthly show).  
404 if monthly report missing.  
**No** POST sibling in Implementation 01.

Register **before** `/monthly-reports/(\d+)$` in `routes.php`.

---

## 3. Page structure (Russian)

**Title:** `Черновик разделов из работ — {period_key}`

**Breadcrumb / actions:**

- К месячному отчету → `/monthly-reports/{id}`
- К списку работ (якорь) → `/monthly-reports/{id}#work-entries`
- Предпросмотр отчета (текущий client preview) → `/monthly-reports/{id}/preview`

### 3.1 Warning (always)

```
Это предварительная сборка. Она не меняет отчет, PDF, снимки и ссылки.
```

Use a visible `note` / warning panel, not a dismissible toast only.

### 3.2 Finalized extra warning

If parent status is `finalized`:

```
Месячный отчет финализирован. Клиентский PDF и публичная ссылка остаются как есть.
Чтобы позже записать черновик в блоки, отчет нужно будет открыть снова — это отдельный шаг.
```

Do **not** offer reopen on this page.

### 3.3 Source stats

| Label | Meaning |
|-------|---------|
| Всего работ | All entries for this monthly id |
| Попали в черновик | Assigned to work_completed / next_month_plan / risks |
| Внутренние (скрыты) | `client_visibility = internal` |
| Отменённые | `status = cancelled` |
| Не попали в разделы | Unassigned (incomplete, notes-only, etc.) |

Show integer counts only. No emails.

### 3.4 Generated drafts (auto)

Cards in this order:

1. **Что сделали** (`work_completed`)
2. **План на следующий месяц** (`next_month_plan`)
3. **Риски и блокеры** (`risks_and_blockers`)

Each card:

- RU title  
- Count of source entries  
- Body: grouped by `category_name` (or «Без категории»), then bullets in `sort_order`, `id`  
- Empty: `Нет работ, подходящих для этого раздела.`

Optional collapsed «Кандидаты в выводы» if any `period_role=note` client-safe/facing rows exist. Fixture 1: omit section if count 0.

### 3.5 Manual-required blocks

Cards (not generated):

4. **Краткое резюме** — `Этот раздел заполняется вручную. Автосборка из работ в этом шаге не делается.`  
5. **Результаты** — `Этот раздел заполняется вручную. Показатели не выводятся из списка работ.`  
6. **Ключевые выводы** — `Этот раздел пока заполняется вручную.` (+ candidates only if present)

If useful, show **current stored block** summary/body as read-only «Сейчас в отчете» (escaped), clearly labeled as existing content, not as the new draft.

### 3.6 No save / apply

**Forbidden on this page:**

- Сохранить  
- Применить  
- Записать в блоки  
- Любая `<form method="post">`

**CTA row:**

- Primary-looking secondary: **Назад к месячному отчету**  
- Disabled or info control: **Применение черновика будет добавлено следующим шагом**  
  - `disabled` button **or** `<p class="field-hint">` — not a working POST

---

## 4. Empty states

| Situation | Copy |
|-----------|------|
| Zero work entries | `Работ за месяц пока нет. Добавьте работы, затем откройте черновик снова.` + link to create |
| Entries exist, a given auto-block empty | Per-card empty line in §3.4 |
| All entries internal/cancelled | Stats show exclusions; auto-cards empty; keep manual cards |

---

## 5. Internal visibility

- Internal rows: counted, **not** listed in draft bullets.  
- Do not preview `internal_note` on this page.  
- Optional tech `<details>`: «Почему не попали» listing title + reason code (`internal`, `cancelled`, `unassigned`) — titles only, still no internal notes.

---

## 6. Category grouping

- Heading = `category_name` from join, else «Без категории».  
- Sort groups by minimum `sort_order` of members, then name.  
- Inside group: `sort_order ASC`, `id ASC` (same as work-entry list).

---

## 7. Comparison with existing client preview

`/preview` = current **published-path** composition from `report_blocks`.  
`/assembly-preview` = **proposal from work entries**.

Do not merge them into one page in Implementation 01 (different trust levels).

---

## 8. Visual / CSS

Reuse existing `panel`, `note`, `btn`, `status-badge`, work-entry cards spacing. No new brand exercise. No screenshot QA wave.

---

## 9. SAFE UNKNOWN

- Exact wording polish after operator click-through.  
- Whether to show stored block text by default or behind `<details>` (recommend `<details>` to keep the draft visually primary).
