# I-SEO Report Hub — Work Entry Editor UX Flows v0.1

**Status:** CHARTER / UX — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Work Entry Editor Charter 01

Russian UI. No share tokens. No public routes.

---

## 1. Screen map

| Screen | Route | Method | Purpose |
|--------|-------|--------|---------|
| Monthly report (list host) | `/monthly-reports/{id}` | GET | Existing page; section «Работы за месяц» gains add/edit links |
| Create work entry | `/monthly-reports/{id}/work-entries/create` | GET | Form |
| Store work entry | `/monthly-reports/{id}/work-entries` | POST | Persist create |
| Edit work entry | `/monthly-report-work-entries/{entry_id}/edit` | GET | Form |
| Update work entry | `/monthly-report-work-entries/{entry_id}` | POST | Persist edit |

No DELETE route. No status-only POST. No `/monthly-report-work-entries/{id}` GET show page in MVP.

Register the nested `work-entries` patterns **before** `/monthly-reports/(\d+)$` in `app/routes.php` (same ordering rule as `/blocks/create`).

---

## 2. Monthly report page — section «Работы за месяц»

Keep current placement: after «Исходные еженедельные заметки», before «Содержимое» / «Блоки отчета».

### 2.1 Section head

Existing CTAs (blocks / preview / files) stay.

**Add** primary button:

- «Добавить работу» → `/monthly-reports/{id}/work-entries/create`

Do **not** add a second «Добавить из каталога» button.

Replace the current notice («Редактор работ … будут добавлены отдельными шагами») with a short operational note:

> Эти записи — рабочий журнал специалиста. Они пока не собирают клиентский PDF автоматически.

If the monthly report is finalized, add a warning (not a lock):

> Отчет финализирован. Изменение работ не обновляет snapshot, PDF и публичную ссылку.

### 2.2 Empty state

If zero entries: keep empty copy, plus the same «Добавить работу» button.

### 2.3 Card

Keep badges (category / status / period_role / visibility).

**Add** on each card:

- Link «Изменить» → `/monthly-report-work-entries/{entry_id}/edit`

**Do not add:**

- Удалить
- Archive POST
- Quick status pills that POST

Cancelled / deferred cards: add modifier class (e.g. `work-entry-card--inactive`) so they look dimmed but remain visible and editable.

Catalogue origin already appears under «Внутренняя заметка / технические детали». Keep that. Optional extra line under the title when `work_item_name` is set: «Из каталога: {name}».

### 2.4 Counters

Unchanged semantics (total includes cancelled). No new counter required in MVP.

---

## 3. Create flow

### 3.1 Entry

From monthly report → «Добавить работу».

### 3.2 Breadcrumbs / context (Russian)

Show a context strip, matching report-block forms:

- Ссылка на месячный отчет (`/monthly-reports/{id}`)
- Period key, project / client names if already loaded for monthly show
- Status badge of the parent report
- «К работам за месяц» anchor `#work-entries`

No share URL. No export download link required on this form.

### 3.3 Form fields (user-facing)

| Order | Label | Control |
|-------|-------|---------|
| 1 | Категория | `<select>` active categories + empty «— не выбрана —» |
| 2 | Работа из каталога | `<select>` active items, grouped by category; empty «— ручная работа —» |
| 3 | Название | text, required unless catalogue item selected (then may auto-fill on save) |
| 4 | Описание | textarea, optional |
| 5 | Статус | `<select>` required |
| 6 | Роль в периоде | `<select>` required |
| 7 | Видимость для клиента | `<select>` required |
| 8 | Кратко для клиента | textarea, optional |
| 9 | Внутренняя заметка | textarea, optional |
| 10 | Доказательства | textarea, optional |
| 11 | Порядок | number, optional, default 100 |

Read-only hints:

- Месячный отчет — locked (not posted as changeable id).
- `site_type` / `cadence` / `fill_mode` of a selected catalogue item may be shown as a `<details>` hint, not as editable fields.

Helper copy under visibility:

> «Внутреннее» не попадёт в будущую клиентскую сборку. «Показывать клиенту» — явное клиентское поле.

Helper copy under status:

> Чтобы убрать работу из активного списка без удаления, выберите «Отменено» или «Отложено». Физическое удаление недоступно.

### 3.4 Create defaults

| Field | Default |
|-------|---------|
| status | `planned` |
| period_role | `planned_next` |
| client_visibility | catalogue item `visibility` if item selected, else `client_safe` |
| sort_order | `100` |
| title | empty until user types or save copies work item name |

Note: DB column default for `period_role` is `done`. The **form** default for create is `planned_next` because a new row is usually planned work. Submitted value wins.

### 3.5 Actions

- Submit: «Сохранить работу» (POST)
- Cancel: «Отмена» → `/monthly-reports/{id}#work-entries`

On success: redirect to `/monthly-reports/{id}#work-entries` + flash success.

On validation error: re-render create form with errors and old input. CSRF refreshed.

### 3.6 Optional GET filter

`GET .../create?category_id={n}` may preselect category and list only that category’s items. Not required if `<optgroup>` is used.

---

## 4. Edit flow

### 4.1 Entry

Card «Изменить».

### 4.2 Identity locks

| Field | UI |
|-------|----|
| `id` | visible, not editable |
| `monthly_report_id` | locked; POST must reject mismatch / ignore posted parent id |
| `created_by_user_id` | not shown as editable; preserved |
| `created_at` | optional read-only in details |
| Catalogue origin | read-only hint if `work_item_id` currently set |

User **may** change `work_item_id` / `category_id` / title (relink or convert to manual).

### 4.3 Fields

Same as create. Current values as `old`.

### 4.4 Actions

- Submit: «Сохранить изменения»
- Cancel: back to monthly report `#work-entries`
- **No** «Удалить»
- Optional secondary copy (not a second POST): «Чтобы скрыть работу, поставьте статус «Отменено» / «Отложено» или видимость «Внутреннее»»

Success redirect: same as create.

If entry id does not exist, or does not belong to an accessible monthly report: 404 (no existence leak beyond other internal CRUD).

---

## 5. Cancel / defer (instead of delete)

| User intent | How |
|-------------|-----|
| Done by mistake / not this month | Edit → status `cancelled` |
| Move to later | Edit → status `deferred` (and usually `period_role` = `planned_next`) |
| Keep in journal but not for client | `client_visibility` = `internal` |
| Physical delete | **Not offered** |

List still shows the row (dimmed). Revival = edit back to `planned` / `in_progress` / `done`.

---

## 6. Status-only quick actions

**Not in Implementation 01.**

Rationale: extra POST surface, CSRF, flash, and easy mis-clicks on fixture data. Full edit form is safer for the first write wave.

---

## 7. Warnings and copy (canonical Russian)

| Situation | Copy |
|-----------|------|
| Editor vs PDF | Эти записи пока не собирают клиентский PDF автоматически. |
| Finalized parent | Отчет финализирован. Изменение работ не обновляет snapshot, PDF и публичную ссылку. |
| No delete | Физическое удаление недоступно. Используйте статус «Отменено» или «Отложено». |
| Internal visibility | Внутренние заметки и видимость «Внутреннее» не предназначены для клиента. |
| Catalogue derive | Если выбрана работа каталога, категория берётся из каталога. |

Do not print share tokens, checksums, DB passwords, or `.env` values.

---

## 8. Accessibility / progressive enhancement

- Real `<form method="post">` + CSRF hidden field.
- Labels wrap or `for=` on selects/inputs.
- Content usable without JavaScript.
- `novalidate` may match existing report-block forms; server validation is authoritative.

---

## 9. Out of UX scope

- Drag-and-drop sort.
- Bulk edit.
- Catalogue browser page.
- Assembly preview of 6 shells.
- Screenshot QA / visual redesign of the whole monthly page.
