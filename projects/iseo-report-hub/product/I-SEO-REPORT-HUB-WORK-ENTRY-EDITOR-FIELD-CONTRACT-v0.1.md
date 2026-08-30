# I-SEO Report Hub — Work Entry Editor Field Contract v0.1

**Status:** CHARTER / FIELD CONTRACT — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Work Entry Editor Charter 01  
**Table:** `monthly_report_work_entries` (DB-11, no schema change)

Server validation is authoritative. CSRF + authenticated internal user required on every POST.

---

## 1. Allowed enum values (DB-11 CHECK)

### status

`planned` · `in_progress` · `done` · `blocked` · `cancelled` · `deferred`

RU (`UiLabels::WORK_ENTRY_STATUSES`): Запланировано · В работе · Выполнено · Заблокировано · Отменено · Отложено

### period_role

`done` · `planned_next` · `risk` · `note`

RU: Сделано за месяц · План на следующий период · Риск / вопрос · Заметка

### client_visibility

`internal` · `client_safe` · `client_facing`

RU: Внутреннее · Можно использовать в отчете · Показывать клиенту

Reject any other string (do not coerce `skipped` / `archived` from the older migration-charter draft).

---

## 2. Field table

| Field | DB column | Input | Required | Allowed | Default (create form) | Validation | RU label | Notes |
|-------|-----------|-------|----------|---------|------------------------|------------|----------|-------|
| monthly_report_id | `monthly_report_id` | hidden / URL | yes (from route) | existing `monthly_report_contents.id` | from `{id}` | integer > 0; FK exists; **immutable on edit** | Месячный отчет | Create: from URL. Edit: ignore posted override |
| work_item_id | `work_item_id` | select | no | NULL or active `seo_work_items.id` | empty | integer or empty; reject unknown / inactive item | Работа из каталога | NULL = manual. Inactive item may remain on **edit** of existing row but cannot be newly selected |
| category_id | `category_id` | select | no* | NULL or active `seo_work_categories.id` | empty or derived | if work_item set → **force** item’s `category_id`; else optional FK | Категория | *Derived when catalogue item selected |
| title | `title` | text | yes† | 1–240 chars after trim | empty | required after defaulting; max 240; reject blank | Название | †If empty and work_item set, copy item `name` then re-check |
| description | `description` | textarea | no | text / NULL | empty | optional; store NULL if blank | Описание | |
| status | `status` | select | yes | enum above | `planned` | required; exact enum | Статус | |
| period_role | `period_role` | select | yes | enum above | `planned_next` | required; exact enum | Роль в периоде | DB column default is `done`; form default differs on create |
| client_visibility | `client_visibility` | select | yes | enum above | item.visibility or `client_safe` | required; exact enum | Видимость для клиента | Create-only catalogue default; edit uses stored value |
| client_summary | `client_summary` | textarea | no | text / NULL | empty | optional; NULL if blank | Кратко для клиента | Never auto-copy internal_note |
| internal_note | `internal_note` | textarea | no | text / NULL | empty | optional; NULL if blank | Внутренняя заметка | Never auto-publish |
| evidence_note | `evidence_note` | textarea | no | text / NULL | empty | optional; NULL if blank | Доказательства | Day-1 text only; not a file upload |
| sort_order | `sort_order` | number | no | signed int safe range | `100` | integer; if missing/invalid → 100; suggest clamp e.g. -999999…999999 | Порядок | |
| created_by_user_id | `created_by_user_id` | — | — | users.id or NULL | current user on create | set on create; **never change on edit** | — | |
| updated_by_user_id | `updated_by_user_id` | — | — | users.id or NULL | current user | set on create and update when user id available | — | |
| created_at / updated_at | timestamps | — | — | DB | DB | do not accept from POST | — | |
| id | `id` | — | edit only | existing entry | — | edit: entry must exist | — | |

Catalogue item fields `site_type`, `cadence`, `fill_mode`, `evidence_required`, `visibility` (item-level) are **not** editor columns. Show read-only if useful.

---

## 3. Cross-field rules

1. **Title after defaulting is the only content required field.** Description is optional even if the older Block/Field Mapping draft said “description required day-1”. DB-11 title is NOT NULL; description is NULL-able. MVP follows **DB-11**.  
2. If `work_item_id` is set, `category_id` := that item’s `category_id`. Mismatched posted category is not an error; it is overwritten.  
3. If `work_item_id` is empty, `category_id` may be NULL. Invalid category id → 422.  
4. Entry on edit must belong to the monthly report implied by the loaded row. Do not allow moving an entry to another monthly report in MVP.  
5. Reject unknown IDs with a field error (not a 500).  
6. Do not accept HTML-as-code execution; store as plain text; escape on output (existing `e()`).  
7. Duplicate `(monthly_report_id, work_item_id)` is **allowed**.  
8. Duplicate titles on one report are **allowed**.  
9. No uniqueness check on title.

---

## 4. CSRF / auth

| Check | Rule |
|-------|------|
| Auth | `requireInternalUser()` (or equivalent): authenticated + internal role |
| CSRF | `$csrf->field()` on form; verify on POST; fail closed |
| Method | POST only for store/update; GET for forms |
| Privilege | Same internal gate as monthly report show; no new ACL table |

---

## 5. Error UX

Reuse report-block pattern: panel with field → Russian message list; keep `old` input.

Suggested messages (do not leak SQL):

| Condition | Message |
|-----------|---------|
| title empty after default | Укажите название работы. |
| title too long | Название не длиннее 240 символов. |
| bad status | Выберите допустимый статус. |
| bad period_role | Выберите роль в периоде. |
| bad visibility | Выберите видимость. |
| bad work_item | Работа каталога не найдена или неактивна. |
| bad category | Категория не найдена или неактивна. |
| bad sort_order | Порядок должен быть целым числом. |
| missing CSRF | Сессия устарела. Обновите форму и повторите. |
| finalized warning | Informational only; **not** a validation error in this MVP |

HTTP: 422-style re-render (app may use 200 + errors like other CRUD). Do not invent a JSON API.

---

## 6. What must not be posted / accepted

- Share tokens  
- Export ids  
- Snapshot ids  
- Block content / `REQUIRED_BLOCK_KEYS`  
- Catalogue `is_active` flips  
- `monthly_report_id` change on edit  
- File uploads  
- Raw SQL  

---

## 7. Mapping from older mapping doc

`I-SEO-REPORT-HUB-BLOCK-FIELD-MAPPING-v0.1.md` listed `skipped` status and required description. **This contract supersedes those drafts for the editor MVP** in favor of live DB-11 CHECKs and NULL-able `description`.
