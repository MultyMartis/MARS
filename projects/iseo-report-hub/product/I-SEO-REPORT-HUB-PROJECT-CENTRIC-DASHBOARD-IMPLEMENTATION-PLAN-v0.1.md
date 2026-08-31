# I-SEO Report Hub — Project-Centric Dashboard Implementation Plan v0.1

**Date:** 2026-08-31  
**Status:** implementation roadmap — **not** an implementation authorization for Waves 2–5 until each wave is chartered/started  
**Companion charter:** [I-SEO-REPORT-HUB-PROJECT-CENTRIC-DASHBOARD-IA-CHARTER-v0.1.md](I-SEO-REPORT-HUB-PROJECT-CENTRIC-DASHBOARD-IA-CHARTER-v0.1.md)  
**Parent wave:** `I-SEO Report Hub — Project-Centric Dashboard and IA Charter 01`

---

## 0. Guardrails for all waves

| Rule | Value |
|------|-------|
| Source of truth | `projects/iseo-report-hub/app-source` |
| Local runtime | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub` (sync only under explicit impl charter) |
| Host | **Do not touch** (`https://reports.i-seo.su` paused) |
| Prefer | UI over existing joins; avoid DB migration unless blocked |
| Preserve | `/monthly-reports/{id}` work / content-workflow / preview paths |
| Parked | PDF, export, share, snapshot regeneration, charts |
| Foreign WIP | Out of scope |

---

## Wave 1 — Project Dashboard Implementation 01

**Goal:** Replace demo home with a **project list dashboard**.

### In scope

- Rewrite `DashboardController` + `dashboard.php` (and minimal CSS/nav if needed)
- Heading **`Проекты`**
- List projects from DB (`projects` + `clients` + primary `sites`)
- Use existing demo project **`ПРОВЕРКА.рф`**
- Filters UI: active / closed / archive (static shells OK if statuses not fully modeled)
- Per card: identity fields available today; placeholders for tariff/service if missing
- Current report panel for August `in_progress` monthly report
- Quick actions → existing routes:
  - project detail **if Wave 2 already shipped**; else temporary deep-links to report/periods until `/projects/{id}` exists
  - **Preferred Wave 1 stance:** implement dashboard cards with `Перейти в проект` linking to a **stub `/projects/{id}` only if trivial**; otherwise link to current report + note Wave 2 — **decision at impl start:** prefer **no broken links**. If `/projects/{id}` not ready, CTA may open current report and label secondary «карточка проекта — следующая волна», **or** ship a minimal read-only `/projects/{id}` in the same PR only if charter owner allows scope merge. **Default for Wave 1 alone:** dashboard first; project CTA may target `/monthly-reports/{id}` temporarily **only if labeled**, better: ship thin `/projects/{id}` redirect/detail in Wave 2 immediately after.
- Remove sections: `Рабочий контур`, `Быстрые действия`, `Статус локальной системы`
- Demote `/reporting-periods` in nav (keep reachable)

### Out of scope

- Project creation UI
- Charts
- DB migration (unless impossible to list projects — then STOP)
- Curator remarks model
- Evidence
- Host / PDF / export / share

### Acceptance

See charter §10 (Project Dashboard Implementation 01).

### Suggested touch points (read-only planning)

- `app/Controllers/DashboardController.php`
- `app/Views/pages/dashboard.php`
- Possible new `ProjectRepository` read methods (list + joins)
- Layout/sidebar link labels

---

## Wave 2 — Project Detail Implementation 01

**Goal:** `/projects/{id}` as project working center.

### In scope

- Route registration in `routes.php`
- Controller + view for project header + current report + report history
- Links to existing monthly report detail / content-workflow / preview / work-entry create
- Project-scoped report list (inline or `/projects/{id}/reports`)

### Out of scope (unless trivial)

- Full create-report flow
- Settings tabs write path
- Evidence / curator notes persistence

### Acceptance (draft)

- Opening demo project shows August current report first
- July finalized appears in history
- Specialist can reach add work / texts / preview without using global periods as home
- No DB mutation preferred

---

## Wave 3 — Project Creation Draft Implementation 01

**Goal:** Create-project interface and data design.

### Fields

- Site URL
- Legal entity
- Service type
- Tariff
- Responsible curator/admin
- Responsible SEO specialist
- Status

### Approach

1. Audit live `clients` / `projects` / `sites` columns  
2. If model insufficient → charter DDL first  
3. Else implement draft create under role gate  

### Out of scope

- Bulk import
- Production onboarding automation

---

## Wave 4 — Curator Notes / Alerts Charter 01

**Goal:** Product + schema charter for remarks/alerts.

### Topics

- Entity targets (project / report / section / work entry)
- Open / resolved lifecycle
- Dashboard + project attention markers
- Role permissions

**No implementation** until charter accepted.

---

## Wave 5 — Report Evidence Links Charter / Implementation

**Goal:** External proof links + screenshot metadata per [evidence requirement](I-SEO-REPORT-HUB-REPORT-EVIDENCE-ATTACHMENTS-LINKS-REQUIREMENT-v0.1.md).

### Fit to IA

- Evidence lives on report; project shows counts/indicators
- Dashboard may show «есть доказательства / требуется доказательство» later

Split charter vs implementation as needed. No upload in dashboard waves.

---

## Later / deferred

| Item | When |
|------|------|
| Project statistics graphs / charts | After multi-project real data |
| PDF / export / share productization | After operator confirm; currently parked |
| Host / production config normalization | Paused |
| Operator manual walkthrough | Parallel — does not block IA docs; preferred before SEO-team production claim |
| SEO-team production instruction final | After walkthrough + feedback |

---

## What not to touch (across early waves)

- Host files / `public_html`
- Production secrets / `.env` on host
- Broad PDF regeneration
- Export share token workflows as specialist primary UX
- WordPress / i-seo.su / OVERSEO
- Foreign WIP outside `projects/iseo-report-hub/`
- Destructive git / DB cleanup

---

## Recommended next action after this charter

**Start:** `I-SEO Report Hub — Project Dashboard Implementation 01`  
**Do not start** Waves 3–5 until Wave 1–2 land or operator re-prioritizes.
