# REPORT — I-SEO REPORT HUB PROJECT-CENTRIC DASHBOARD AND IA CHARTER 01

**Date:** 2026-08-31  
**Verdict:** PROJECT-CENTRIC DASHBOARD IA CHARTER COMPLETE  
**Primary commit:** `4e7f82c89621674e6c08915bb8e24e487ce5d96e`  
**Hash-record commit:** `bc66de02e36d4ca02966f0335c9ea10c1143b0eb`  
**Tip HEAD before:** `4ad1cf7a0ae79dac84642c869baa39b005bc0d6d`  
**Push:** no

---

## 1. Verdict

**PROJECT-CENTRIC DASHBOARD IA CHARTER COMPLETE**

Product/technical charter and implementation plan recorded for the project-centric dashboard IA shift. No app-source, runtime, DB, or host changes.

---

## 2. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Volume | `AI WS` (`X:`) |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `4ad1cf7a0ae79dac84642c869baa39b005bc0d6d` |
| Clean worktree used | no — main tree; i-SEO scope clean; staged empty; foreign WIP unstaged and preserved |
| Foreign WIP preserved | yes |
| Runtime touched | no (read-only `/health` 200) |
| DB touched | no |
| app-source touched | no |

---

## 3. Storage Audit Gate

**Storage Hygiene Loss Audit 01 = SAFE**

Authoritative i-SEO Report Hub data not lost by temporary STORAGE git-contour deletion; normal work may continue.

---

## 4. Operator Requirement Recorded

Operator rejected current home demo blocks (`Рабочий контур`, `Быстрые действия`, `Статус локальной системы`) and approved project-centric IA:

`Projects → Project Detail → Project Reports → Work Entries / Report Texts / Preview / Future Evidence`

Host track remains paused.

---

## 5. Current IA Audit

- `/` = `DashboardController` + demo sections in `dashboard.php`; single-scenario `LIMIT 1` client/project.
- `/reporting-periods` = global period list; currently de-facto specialist home via dashboard CTAs.
- Data already models `clients` → `projects` → `sites` → `reporting_periods` → `monthly_report_contents` → work entries / blocks.
- No `/projects*` routes today.
- Risk: swapping home without project detail leaves specialists without a clear hub.

---

## 6. New Project-Centric IA

Primary: `/` project dashboard; `/projects/{id}` project center; keep monthly-report deep routes; demote `/reporting-periods` to admin/global/legacy for specialist primary nav.

---

## 7. Dashboard Card Specification

Card: name, site URL, legal entity, service, tariff; project status; current report + week fill; alerts slots; stats; button **`Перейти в проект`**; RU copy priority defined in charter.

---

## 8. Project Detail Specification

`/projects/{id}`: header; current report first; history; future create/settings/evidence; links to existing work/texts/preview.

---

## 9. Route Map

| Class | Routes |
|-------|--------|
| Primary specialist | `/`, `/projects/{id}`, `/monthly-reports/{id}` (+ work/content-workflow/preview) |
| Curator/admin | `/projects/new`, settings, `/reporting-periods`, `/health` |
| Legacy primary | Old dashboard blocks; periods-as-home |
| Future | create report, evidence, curator remarks |

---

## 10. Status Model

Projects: `active` / `paused` / `closed` / `archived` (RU: Действующий / На паузе / Закрыт / Архив).  
Reports: persist `in_progress` / `finalized`; richer week/text/curator states **derived** first — no status migration in Wave 1.

---

## 11. Curator Notes / Alerts Concept

Reserved for **Curator Notes and Alerts Charter 01**. Counts/attention markers on dashboard/project; no implementation now.

---

## 12. Evidence / Attachments Fit

Evidence lives on reports; project/dashboard show indicators later. Requirement doc already exists; no implementation in this wave.

---

## 13. Implementation Sequence

1. Project Dashboard Implementation 01  
2. Project Detail Implementation 01  
3. Project Creation Draft Implementation 01  
4. Curator Notes / Alerts Charter 01  
5. Evidence Links Charter / Implementation  
Later: charts, PDF/share, host config.

---

## 14. Next Implementation Acceptance Criteria

Wave 1: `/` shows **`Проекты`**; old three demo blocks gone; `ПРОВЕРКА.рф` card + August in progress + quick actions; no charts; no fake unlabeled stats; periods not primary home; prefer no DB mutation; screenshots.

---

## 15. Docs Created

- `product/I-SEO-REPORT-HUB-PROJECT-CENTRIC-DASHBOARD-IA-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-PROJECT-CENTRIC-DASHBOARD-IMPLEMENTATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-project-centric-dashboard-ia-charter-01.md`
- `OPERATIONAL-INDEX.md` updated

---

## 16. Evidence

Optional (not committed):  
`X:\AI MARS STORAGE\incoming\iseo-report-hub\project-centric-dashboard-ia-charter-01\20260831-165835\`  
(`route-and-model-notes.txt`; health 200)

---

## 17. Safety

| Item | Value |
|------|-------|
| DB changed | no |
| Runtime files changed | no |
| app-source changed | no |
| Host touched | no |
| PDF/export/share created | no |
| Secrets printed | no |

---

## 18. Commit

- Primary: `4e7f82c89621674e6c08915bb8e24e487ce5d96e` — `docs(iseo-report-hub): add project-centric dashboard ia charter`
- Hash-record: `bc66de02e36d4ca02966f0335c9ea10c1143b0eb` — `docs(iseo-report-hub): record project dashboard ia charter hash`
- Tip HEAD: `dc788b7584bc7f1c01c3aefe4a17a344d76a01c5`
- Push: **no**

---

## 19. SAFE UNKNOWN

- Live column names for tariff / legal_name / owner FKs vs schema draft
- Whether `projects.status` already allows paused/closed/archived in MySQL
- Exact week-fill derivation from work entries
- Whether Wave 1 ships thin `/projects/{id}` or temporary CTAs (plan default: Wave 2 for detail)

---

## 20. Recommended Next Action

**`I-SEO Report Hub — Project Dashboard Implementation 01`**

---

## 21. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-PROJECT-CENTRIC-DASHBOARD-IA-CHARTER-v0.1.md` (new)
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-PROJECT-CENTRIC-DASHBOARD-IMPLEMENTATION-PLAN-v0.1.md` (new)
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-project-centric-dashboard-ia-charter-01.md` (new)
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md` (updated)

---

## 22. Git Actions

- Exact-path stage of the four docs above
- Docs commit only
- No push
- Foreign WIP not staged
