# I-SEO Report Hub — Project-Centric Dashboard and IA Charter v0.1

**Date:** 2026-08-31  
**Status:** product / technical charter — **documentation only**  
**Wave:** `I-SEO Report Hub — Project-Centric Dashboard and IA Charter 01`  
**Code / runtime / DB / host:** **not in scope**

---

## 1. Operator requirement

Operator manually reviewed the current home page (`/`) and rejected the demo dashboard blocks:

- `Рабочий контур`
- `Быстрые действия`
- `Статус локальной системы`

**Verdict:** these are local-demo placeholders and must be replaced.

**Approved product direction:** project-centric information architecture:

`Projects → Project Detail → Project Reports → Work Entries / Report Texts / Preview / Future Evidence`

Hosting / `public_html` and production config normalization remain **paused**. Continue local product development. Do not touch host.

---

## 2. Current IA audit

### 2.1 What `/` does today

| Aspect | Reality |
|--------|---------|
| Route | `GET /` → `DashboardController::index` (`app-source/app/routes.php`) |
| View | `app-source/app/Views/pages/dashboard.php` |
| Heading | Page title «Обзор отчетов»; sections 01–03 as above |
| Data | Module readiness cards + counts (`reporting_periods`, weekly checkpoints, monthly reports, blocks, active shares) |
| Scenario | `loadPrimaryScenario()` loads **one** client/project via `ORDER BY clients.id DESC LIMIT 1` |
| Primary CTA | Links to `/reporting-periods` and latest `/monthly-reports/{id}` |

**Why obsolete:** home is a technical/demo handoff surface, not a multi-project specialist workspace. It assumes a single demo scenario and surfaces PDF/share/system status language that is parked for specialist UX.

### 2.2 What `/reporting-periods` does today

| Aspect | Reality |
|--------|---------|
| Route | `GET /reporting-periods` → `ReportingPeriodController::index` |
| Behavior | **Global** list of reporting periods (not project-scoped UI) |
| Related | Create/edit period; nest monthly report and weekly checkpoints under a period |
| Role today | De-facto main working list after login (dashboard CTA) |

**Problem:** the list feels like «all reports / one project / global admin» at once. Report lists must become **project-scoped**.

### 2.3 Current data model (already present)

| Entity | Table / locus | Notes |
|--------|---------------|-------|
| Client | `clients` | Fixture/demo: legal/display name used as client (`ПРОВЕРКА.рф` path after cleanup) |
| Project | `projects` | `client_id`, `name`, `slug`, `project_type`, `status` (`active` in fixture) |
| Site | `sites` | `project_id`, `url`, `label`, `is_primary` |
| Reporting period | `reporting_periods` | `project_id`, `period_key`, dates, `status` |
| Monthly report | `monthly_report_contents` | Parent period; lifecycle includes `in_progress` / `finalized` (and other allowlisted statuses in schema plans) |
| Work entries | `monthly_report_work_entries` (+ catalogue tables) | Week-oriented specialist work log |
| Report blocks | `report_blocks` | Section bodies; specialist content workflow writes here |
| Weekly checkpoints | `weekly_checkpoints` | Period-scoped W1–W4 notes |
| Evidence / remarks | **not implemented** | Conceptual in schema draft (`evidence_*`, `reviewer_comments`) |

Join path used in repositories:

`clients` → `projects` → `reporting_periods` → `monthly_report_contents` → (work entries / blocks)

### 2.4 What UI assumes about one demo project

- Single primary scenario on dashboard (`LIMIT 1`).
- Specialist flow documented as: login → dashboard → **reporting periods** → monthly report → work / texts / preview.
- Demo: `ПРОВЕРКА.рф`, July finalized / August `in_progress`, specialist user local-only.
- PDF/export/share parked for specialist primary nav (Browser Demo UX Fix).

### 2.5 Routes — reuse vs move (conceptual)

| Route | Future role |
|-------|-------------|
| `/` | **Replace** content with project dashboard |
| `/reporting-periods` | Legacy / admin-global; **not** primary specialist home |
| `/monthly-reports/{id}` | Keep as deep report workspace |
| `/monthly-reports/{id}/work-entries/create` | Keep |
| `/monthly-reports/{id}/content-workflow` | Keep («Тексты отчета») |
| `/monthly-reports/{id}/preview` | Keep |
| `/projects`, `/projects/{id}`, `/projects/new` | **New** (implementation waves) |

### 2.6 Risks if dashboard changes without IA clarity

- Specialists lose the path to periods/reports if CTAs are removed without project detail.
- `/reporting-periods` remains confusing if still promoted as «main list».
- Fake stats (tariff, curator remarks) without labels damage trust.
- Accidental DB migration for statuses/tariffs before UI proves need.
- PDF/share/evidence scope creep into dashboard wave.

---

## 3. New project-centric IA

### 3.1 Mental model

1. **Project** is the primary work unit (site + client + service + people).
2. **Reports** belong to a project (via reporting periods).
3. Specialist opens a project, then the **current** monthly report, then work / texts / preview.
4. Curator notes, evidence, charts, PDF/share are later layers hung off project/report — not home chrome.

### 3.2 Primary specialist routes

| Route | Purpose |
|-------|---------|
| `/` | Project dashboard (list + filters) |
| `/projects` | Optional alias of `/` or explicit index |
| `/projects/{id}` | Project detail (working center) |
| `/projects/{id}/reports` | Optional project-scoped report list |
| `/monthly-reports/{id}` | Report detail (existing) |
| `/monthly-reports/{id}/work-entries/create` | Add work (existing) |
| `/monthly-reports/{id}/content-workflow` | Report texts (existing) |
| `/monthly-reports/{id}/preview` | Client preview (existing) |

### 3.3 Curator / admin routes (later / secondary)

| Route | Purpose |
|-------|---------|
| `/projects/new` | Create project draft |
| `/projects/{id}` settings tabs | Tariff, owners, history |
| `/reporting-periods` | Global technical list (admin) |
| `/health` | System status (privileged) |
| Export/share routes | Parked; not specialist primary |

### 3.4 Legacy / deprecated for specialist primary nav

- Dashboard blocks: `Рабочий контур`, `Быстрые действия`, `Статус локальной системы`
- Treating `/reporting-periods` as the main post-login destination

### 3.5 Future routes

- `/projects/{id}/reports/new` — create report
- Evidence / attachments routes under report or project
- Curator remarks / alerts surfaces

---

## 4. Dashboard card specification (`/`)

### 4.1 Page chrome

- Heading: **`Проекты`**
- Filters (visible): **Действующие** / **Закрытые** / **Архив** (and paused as attention or separate chip)
- Default filter: active (+ optionally paused)
- Closed / archived: hidden by default

### 4.2 Card — identity (visual priority high)

| Field | RU label / note |
|-------|-----------------|
| Project display name | Primary title |
| Website URL | `Сайт:` |
| Legal entity / client legal name | `Юрлицо:` |
| Service type | `Услуга:` |
| Active tariff | `Тариф:` — placeholder ok if unknown in Wave 1 |

### 4.3 Card — status

| Code | RU |
|------|-----|
| `active` | Действующий |
| `paused` | На паузе |
| `closed` | Закрыт |
| `archived` | Архив |

### 4.4 Card — current report panel

- Current active monthly report (period/month)
- Report status (DB: `in_progress` / `finalized` + derived UI states)
- Week completion: W1–W4 filled indicators; month texts status if derived
- Quick actions (RU):
  - `Открыть отчет`
  - `Добавить работу`
  - `Тексты отчета`
  - `Предпросмотр`
- Primary button: **`Перейти в проект`**

### 4.5 Card — quality / alerts (reserve UI slots; may be empty)

- Curator/admin comments count
- Unresolved remarks count
- Attention marker if curator comments exist
- Last curator activity
- Responsible SEO specialist / curator

### 4.6 Card — statistics summary

- Total reports; finalized; in progress/open; with remarks; last report date
- **Wave 1 rule:** only show counts that are derived or labeled demo/local — no invented charts

### 4.7 Copy priority (RU)

1. Project name + site  
2. Current report month + status  
3. `Перейти в проект`  
4. Quick report actions  
5. Stats / alerts as secondary  

---

## 5. Project detail specification (`/projects/{id}`)

### 5.1 Header

- Site, legal entity, service/tariff, responsible people, project status

### 5.2 Current report panel (first)

- Active report first: month, status, week completion, curator alerts (when exist)
- Buttons:
  - `Открыть отчет`
  - `Добавить работу`
  - `Тексты отчета`
  - `Предпросмотр для клиента`

### 5.3 Report history

- All project reports; current on top; finalized below
- Status, dates, remark indicators

### 5.4 Create report

- Future button `Создать отчет` (allowed roles only)
- Not required in first dashboard wave; may land in Project Detail Implementation or Project Creation Draft

### 5.5 Settings / future tabs

- `Настройки`, `Ответственные`, `Тариф`, `Доказательства`, `История замечаний`
- Wave 2 may show a read-only summary only

### 5.6 Evidence area

- Placeholder linking to evidence requirement doc
- **No implementation** in this charter or dashboard wave

---

## 6. Status model

### 6.1 Project statuses

| Code | RU | Behavior |
|------|-----|----------|
| `active` | Действующий | Default list |
| `paused` | На паузе | Active/attention or own chip |
| `closed` | Закрыт | Hidden by default |
| `archived` | Архив | Hidden by default; read-only |

**First implementation:** may keep DB `projects.status` as-is (`active` today) and implement filters as UI shells if richer statuses are not yet stored.

### 6.2 Report statuses

**Persisted today (relevant):** `in_progress`, `finalized` (plus schema allowlist: draft / reviewed / archived, etc.)

**Derived UI states (no DB migration required initially):**

| Derived | Meaning |
|---------|---------|
| `week_1_filled` … `week_4_filled` | Work entries present for week |
| `texts_started` / `texts_ready` | Content workflow / blocks progress |
| `curator_review` | Future remarks workflow |
| `has_remarks` | Unresolved curator remarks |
| `ready_for_client_preview` | Preview-worthy content heuristic |

Do **not** migrate report status enums solely for dashboard Wave 1.

---

## 7. Curator notes / alerts concept (reserved)

Future wave: **`I-SEO Report Hub — Curator Notes and Alerts Charter 01`**

Needs:

- Remarks on project / report / section / work entry
- Specialist alerts on dashboard / project / report
- Unresolved count; resolve/close; activity indicator

**Sketch (non-binding):** future `reviewer_comments` or `curator_notes` table with `entity_type`, `entity_id`, `status` (`open`/`resolved`), `author_user_id`, timestamps. No DDL now.

---

## 8. Evidence / attachments fit

Authority: [I-SEO-REPORT-HUB-REPORT-EVIDENCE-ATTACHMENTS-LINKS-REQUIREMENT-v0.1.md](I-SEO-REPORT-HUB-REPORT-EVIDENCE-ATTACHMENTS-LINKS-REQUIREMENT-v0.1.md)

| IA placement | Rule |
|--------------|------|
| Primary storage | Inside **report** (section slots) |
| Project detail | Indicator / count per report later |
| Dashboard card | Optional evidence warning count later |
| External rank links | Report section metadata |
| Now | **Document only** — no upload/API/DB |

---

## 9. Implementation sequence (approved)

1. **Project Dashboard Implementation 01** — replace `/` with project list  
2. **Project Detail Implementation 01** — `/projects/{id}`  
3. **Project Creation Draft Implementation 01** — create UI/data  
4. **Curator Notes / Alerts Charter 01**  
5. **Report Evidence Links Charter / Implementation**  

**Later:** project statistics graphs; PDF/export/share; host/production config.

See companion: [I-SEO-REPORT-HUB-PROJECT-CENTRIC-DASHBOARD-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-PROJECT-CENTRIC-DASHBOARD-IMPLEMENTATION-PLAN-v0.1.md)

---

## 10. Acceptance criteria — Project Dashboard Implementation 01

- `/` no longer shows `Рабочий контур`, `Быстрые действия`, `Статус локальной системы`
- `/` shows heading **`Проекты`**
- Active / archive (and closed) filter visible
- Demo project card visible for **`ПРОВЕРКА.рф`**
- Service/tariff placeholders allowed if unknown
- Current August report shown as in progress
- Quick actions: open project, open report, add work, report texts, preview
- No fake unsupported stats unless labeled local/demo or derived
- No charts
- Existing specialist deep routes remain intact
- `/reporting-periods` reachable but not primary dashboard concept
- Prefer **no DB mutation**
- Screenshots captured for review

---

## 11. Explicit non-goals (this charter wave)

- No app-source / runtime code changes  
- No DB migration or data mutation  
- No host / production work  
- No PDF / export / share / snapshot work  
- No evidence upload implementation  
- No charts  

---

## 12. SAFE UNKNOWN

- Exact live columns for tariff, legal_name, curator FKs vs schema draft naming (`display_name` vs `name`) — verify at implementation against MySQL `SHOW COLUMNS`
- Whether paused/closed/archived already exist as enum values on `projects.status` in live DB
- Exact week-fill derivation rules from work-entry dates vs week_index fields
- Whether `/projects` redirects to `/` or is a duplicate index
