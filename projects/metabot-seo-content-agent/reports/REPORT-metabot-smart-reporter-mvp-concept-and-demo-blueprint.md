# REPORT — MetaBOT Smart Reporter MVP Concept and Demo Blueprint

**Date:** 2026-07-10  
**Lane:** B — MetaBOT / i-SEO Report Hub / Smart Reporter  
**Classification:** CONCEPTUAL product design + demo planning — **no runtime implementation**  
**Authority:** Operator is primary MVP product authority; SEO specialist feedback is **later** (post-demo)  
**Evidence key:** REPO_EVIDENCED · OPERATOR_CLARIFICATION · PLANNED · CONCEPTUAL · SAFE UNKNOWN

---

## 1. Executive Summary

**MetaBOT Smart Reporter** (working name) is a **planned MetaBOT-compatible product layer** for i-SEO client SEO reporting: assemble, explain, and visualize periodic SEO reports for clients, with human approval before delivery. It is **not** the MetaBOT SEO Content Agent (brief/article writer) and **not** OPS WF-01 (studio back-office monthly reporting control).

**Repo truth today:** No committed doc names “Smart Reporter” or “i-SEO Report Hub.” Evidence supports **MetaBOT** as broader external automation contour, **i-SEO** as operator org / workflow tag, and **i-seo.su** as deferred ATLAS website entity — suitable as **future** WordPress report shell (**OPERATOR_CLARIFICATION** + **PLANNED**).

**Operator-approved MVP assumptions (this task):**

| Assumption | Classification |
|------------|----------------|
| Monthly reporting rhythm | OPERATOR_CLARIFICATION |
| 3 weekly preliminary reports + 4th monthly final | OPERATOR_CLARIFICATION |
| Mixed auto-template + manual SEO specialist fields | OPERATOR_CLARIFICATION |
| Early Topvisor via screenshots / links | OPERATOR_CLARIFICATION · **PLANNED** integration |
| Admin on i-seo.su WordPress | OPERATOR_CLARIFICATION · **PLANNED** |
| Per-SEO-specialist zone | OPERATOR_CLARIFICATION |
| Static HTML demo before production | OPERATOR_CLARIFICATION · aligns with Website Factory static-demo patterns |

**Recommended MVP path:** **Option A — static demo only** under `workspaces/metabot-smart-reporter-demo/`, using registry-driven mock data and gulp-starter or plain static HTML. Validates UX, report structure, and “smart” block behavior **without** n8n, WordPress, or API dependencies. Next wave: **Option B** (WordPress manual fields on i-seo.su) after operator approves demo.

**Final status:** COMPLETE — MVP concept and demo blueprint completed.

---

## 2. Preflight

| Check | Result |
|-------|--------|
| CWD | `X:\AI MARS` ✓ |
| Volume X: label | `AI WS` ✓ |
| Git branch | `mars/canonical-post-recovery` ✓ |
| Staged changes | empty ✓ |
| Foreign WIP | preserved — unrelated `M` / `??` not touched ✓ |
| Live n8n / WP / external APIs | not called ✓ |
| Files created | one report (this file) ✓ |
| Stage / commit | none ✓ |

**Docs read (mandatory):** AGENTS.md, .cursorrules, README.md, registry/project-registry.md, OPERATIONAL-INDEX.md, metabot-terminology-and-roles-v1.md, metabot-developer-concept-v1.md, n8n-project-development-rules-v1.md, REPORT-metabot-seo-agent-v14-deep-workflow-architecture-review.md, n8n-import-safe-generation-rules-v1.md.

**Additional repo reads:** OPS WF-01 monthly reporting, OPS ReportRecord model, MIG README, ATLAS i-seo.su references, FP-0002 static demo architecture, external-systems-relationship-map.

---

## 3. Source Evidence and Assumptions

### 3.1 REPO_EVIDENCED

| Fact | Source |
|------|--------|
| MetaBOT canonical pack = SEO **Content** Agent (`metabot-seo-content-agent`) | registry, OPERATIONAL-INDEX, README |
| MetaBOT = external n8n + Telegram + Sheets + OpenRouter; MARS = docs only | integration-boundary, OPERATIONAL-INDEX |
| i-SEO tag on live v14 workflow exports | exports/live-v14-evidence/2026-07-10/*.sanitized.json |
| Primary users described as i-SEO SEO specialists | OPERATIONAL-INDEX (partial export evidence) |
| MetaBOT Developer = PLANNED/conceptual; n8n discipline documented | metabot-developer-concept-v1, n8n-project-development-rules-v1 |
| v14 architecture: Intake/Worker/Admin, webhook handoff, Sheets locks/memory | REPORT-metabot-seo-agent-v14-deep-workflow-architecture-review |
| OPS owns **business** monthly reporting **workflow** (human-operated, ATLAS-consuming) | OPS-WF-01, OPS-OPERATIONAL-DATA-MODEL |
| i-seo.su registered as WEB-0005 **Deferred** in ATLAS | ATLAS population/audit docs |
| Website Factory static demo pattern: page registry + templates + generator + dist | FP-0002-STATIC-DEMO-GENERATION-ARCHITECTURE-v1 |
| WPilot RC5 proven content writes on DEV WordPress | registry, wpilot docs |
| MIG = R1 groundtruth; optional future insight source | projects/mig/README |

### 3.2 OPERATOR_CLARIFICATION (task charter — authoritative for MVP)

| Assumption | Notes |
|------------|-------|
| Product names: MetaBOT Smart Reporter, i-SEO Report Hub | Working names; not in repo yet |
| 3 weekly + 1 monthly final report cadence | Preliminary vs final distinction |
| Topvisor screenshots/links in early MVP | Full API later |
| i-seo.su WordPress as admin/client shell | ATLAS defers site; operator confirms intent |
| Operator = primary product authority before SEO team interviews | This task scope |
| Static demo before specialist feedback | Demo-first validation |

### 3.3 PLANNED / CONCEPTUAL

| Item | Status |
|------|--------|
| Smart Reporter as separate MetaBOT product | PLANNED — no registry row yet |
| n8n report-generation helper | PLANNED |
| Topvisor / Wordstat / analytics APIs | PLANNED |
| MIG-fed report insights | PLANNED optional |
| Telegram draft helper for reports | CONCEPTUAL (MetaBOT pattern reuse) |

### 3.4 Contradictions / gaps

| Topic | Repo says | Operator says | Resolution |
|-------|-----------|---------------|------------|
| MetaBOT scope | Mostly SEO Content Agent | Broader bot contour | Document Smart Reporter as **future MetaBOT Product**; do not merge with Content Agent |
| Monthly reporting | OPS WF-01 studio ops | i-SEO **client SEO** reports | **Separate products** — may share approval **patterns**, not same workflow |
| i-seo.su | ATLAS deferred | WP report hub | PLANNED shell; demo does not require live WP |

---

## 4. Product Definition

### 4.1 Working names

| Name | Role |
|------|------|
| **MetaBOT Smart Reporter** | MVP product layer — smart assembly/explanation of SEO reports |
| **i-SEO Report Hub** | Product workspace / admin surface brand (likely on i-seo.su) |
| **MetaBOT** | External automation contour (n8n, bots, webhooks) — **parent ecosystem** |
| **MetaBOT SEO Content Agent** | **Different product** — content/TZ/article pipeline |

### 4.2 One-sentence definition

Smart Reporter helps i-SEO specialists **produce client-ready SEO progress reports** on a **monthly cycle** (with weekly checkpoints), combining **template blocks**, **manual facts**, **optional screenshots/links**, and **lightweight “smart” text** (summaries, change explanations, missing-data flags) — always **human-approved** before the client sees the report.

### 4.3 Relationship map

```text
┌─────────────────────────────────────────────────────────────┐
│ MARS (X:\AI MARS) — docs, demo workspace, future contracts   │
└───────────────────────────┬─────────────────────────────────┘
                            │ human-supervised design
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ MetaBOT       │   │ i-SEO Report  │   │ Website       │
│ Smart Reporter│   │ Hub (WP shell)│   │ Factory demo  │
│ (future n8n)  │   │ i-seo.su      │   │ static pages  │
└───────┬───────┘   └───────┬───────┘   └───────────────┘
        │                   │
        │    ┌──────────────┴──────────────┐
        │    │ Topvisor / analytics (later)   │
        └───►│ Manual SEO specialist input  │
             └──────────────────────────────┘

Sibling (NOT Smart Reporter):
  MetaBOT SEO Content Agent — Intake/Worker/Admin content pipeline
Sibling (pattern only):
  OPS WF-01 — studio monthly reporting control
Optional later:
  MIG — market/keyword/competitor insight blocks
```

### 4.4 MVP usefulness before full API

MVP must deliver value when data entry is **mostly manual**:

- Structured report sections reduce blank-page friction.
- Template + dictionary auto-fill client/project boilerplate.
- “What changed” and executive summary drafts from **prior report + current notes**.
- Missing-field warnings before send.
- Clean **client view** separate from **editor view**.

---

## 5. MVP Roles

| Role | Sees | Edits | Approves | Must NOT touch in MVP |
|------|------|-------|----------|------------------------|
| **Operator / product owner** | All projects, all specialists’ report lists, demo scope, templates | Global templates, section dictionary, mock client registry | Final product direction; may co-approve sensitive sends | Live n8n graphs; production WP without charter |
| **SEO specialist** | Own client zone, weekly/monthly drafts, internal editor, missing-data flags | Manual sections, rankings notes, work log, risks, recommendations, Topvisor link/screenshot attachments | Own draft → submit for review; marks “ready for client” | Other specialists’ zones; global template schema |
| **Client** | Published client report URL (read-only), printable layout | Nothing | Nothing (consumes only) | Admin, internal notes, AI draft markers |
| **Admin / editor** (optional MVP) | Queue of reports pending review | Light copy edits, status changes | Client-facing release if operator delegates | Automation config, API keys |
| **MetaBOT / automation** (future) | N/A in static demo | N/A | N/A | Autonomous publish; must not bypass human approval |

**Zone rule (OPERATOR_CLARIFICATION):** Each SEO specialist has **own project list** and reports; operator sees aggregate.

---

## 6. MVP Report Object

Core entity: **`Report`**

| Field group | Fields | MVP |
|-------------|--------|-----|
| **Identity** | `report_id`, `client_id`, `project_id`, `site_url` | Required |
| **Period** | `reporting_month` (YYYY-MM), `week_number` (1–3 or `final`) | Required |
| **Type** | `weekly_preliminary` \| `monthly_final` \| `internal_preview` | Required |
| **People** | `seo_specialist_id`, `reviewer_id` (optional) | Required specialist |
| **Status** | See status model below | Required |
| **Source materials** | Topvisor URL, screenshot refs, manual CSV paste, prior report ref | Optional early |
| **Sections** | Array of `{ section_key, source: auto\|manual\|ai_draft, content, completeness }` | Required |
| **Smart artifacts** | `ai_draft_summary`, `ai_change_narrative`, `missing_data[]` | MVP_CORE display |
| **URLs** | `public_client_url`, `internal_admin_url` | Demo mock paths |
| **Version** | `version` (integer), `supersedes_report_id` (optional) | Nice-to-have — single version OK for demo |

### Status model (MVP)

```text
draft → in_progress → missing_data_review → specialist_ready
  → pending_approval → approved → published → archived
```

| Status | Meaning |
|--------|---------|
| `draft` | Shell created for period |
| `in_progress` | Specialist filling sections |
| `missing_data_review` | System flagged gaps; specialist or operator resolves |
| `specialist_ready` | Specialist marked complete |
| `pending_approval` | Awaiting operator/lead |
| `approved` | OK to publish to client URL |
| `published` | Client-visible |
| `archived` | Period closed |

**Alignment note:** Mirrors OPS approval **pattern** (draft → review → approve → send) — **not** the same OPS `ReportRecord` schema.

---

## 7. Report Types

### 7.1 Weekly preliminary report

| Aspect | Specification |
|--------|---------------|
| **Purpose** | Short checkpoint: what changed this week, work done, risks, next steps |
| **Audience** | Internal first; may share with client if operator policy allows — demo assumes **internal-primary**, client preview optional |
| **Required fields** | Header, week summary, work completed, next actions, specialist sign-off block |
| **Optional fields** | Traffic/leads, detailed rankings table, screenshots |
| **Tone** | Operational, concise |
| **Detail level** | Low–medium |
| **Automation depth** | Template fill + “what changed vs last week” draft + missing flags |

### 7.2 Monthly final report

| Aspect | Specification |
|--------|---------------|
| **Purpose** | Month closure: executive summary, dynamics, full work narrative, plan for next month |
| **Audience** | **Client-facing** primary |
| **Required fields** | Executive summary, month dynamics, work completed, rankings/visibility section, next month plan, conclusion |
| **Optional fields** | Traffic/conversions, content/technical/link task breakdown, competitor notes |
| **Tone** | Client-friendly, confident but no guaranteed results language (align with SEO Agent factcheck caution — **pattern reuse**, not same pipeline) |
| **Detail level** | High |
| **Automation depth** | Roll up weekly reports + auto executive summary + comparison vs previous month |

### 7.3 Internal draft / preview

| Aspect | Specification |
|--------|---------------|
| **Purpose** | WIP view with AI draft badges, internal comments, incomplete sections |
| **Audience** | Specialist, operator |
| **Shows** | Section source badges, missing data panel, edit controls |
| **Hides from client** | Internal notes, raw SEO jargon blocks, AI draft markers |

### 7.4 Comparison table

| Dimension | Weekly preliminary | Monthly final |
|-----------|-------------------|---------------|
| Weeks covered | 1 | All weeks + synthesis |
| Client send | Optional | Expected |
| Rankings detail | Snapshot / link | Summary + trend |
| Executive summary | 2–3 sentences | Full block |
| Roll-up from prior | Previous week | Weeks 1–3 + prior month |

---

## 8. What Makes It Smart in MVP

Practical intelligence — **no fantasy autonomous agent**.

| Feature | Description | Classification |
|---------|-------------|----------------|
| Auto-assemble sections from template blocks | Pull client/project boilerplate from dictionary | **MVP_CORE** |
| Explain position/traffic/lead changes | Narrative from manual inputs + prior report diff | **MVP_CORE** |
| Client-friendly executive summary | LLM or rule-based polish of specialist bullets | **MVP_CORE** (demo: static mock text labeled `ai_draft`) |
| Highlight risks/anomalies | Flag big drops, missing data, stale Topvisor link | **MVP_CORE** |
| Suggest next actions | Template suggestions from work type + issues | **MVP_NICE_TO_HAVE** |
| Reuse previous report context | Pre-fill “what changed” | **MVP_CORE** |
| Convert specialist notes → polished client text | Single block rewriter | **MVP_NICE_TO_HAVE** |
| Flag missing data | Required section checklist | **MVP_CORE** |
| “What changed this week/month” block | Diff narrative | **MVP_CORE** |
| Monthly summary from weekly reports | Roll-up assembly | **MVP_CORE** for final report |
| Autonomous publish | — | **LATER** (forbidden MVP) |
| Live Topvisor API sync | — | **LATER** |
| MIG competitor narrative | — | **LATER** |
| Optimal model routing | — | **SAFE UNKNOWN** |

**Demo honesty:** Static demo shows **UI and structure** for smart blocks; copy may be pre-written mock unless a later task wires optional local LLM.

---

## 9. MVP Data Model

### 9.1 Data buckets

| Bucket | Source | Manual / Auto | MVP availability | Demo mock | Risk |
|--------|--------|---------------|-------------------|-----------|------|
| Specialist text inputs | SEO specialist | Manual | **Yes** | Textareas in editor | Low |
| Project dictionary | Operator-maintained registry | Auto-fill | **Yes** | `mock/clients.json` | Low |
| Topvisor link | Specialist paste | Manual | **Yes** | Example URL field | Low |
| Ranking screenshot | File upload / static image | Manual | **Yes** | PNG in `mock/assets/` | Medium — storage TBD |
| Ranking table | Manual paste or CSV | Manual | **Yes** | JSON table in mock | Medium — format drift |
| Traffic / leads numbers | Analytics export / manual | Manual | **Partial** | Optional mock metrics | High — often missing |
| Work completed | Specialist | Manual | **Yes** | List fields | Low |
| Next works / plan | Specialist | Manual | **Yes** | List fields | Low |
| Problems / risks | Specialist | Manual | **Yes** | Tags + text | Low |
| Recommendations | Specialist + template | Mixed | **Yes** | Template snippets | Low |
| Previous reports | System store | Auto context | **Demo mock** | Prior month JSON | Low |
| Attachments | Upload | Manual | **Nice** | Static files | Medium |
| Topvisor API | Topvisor | Auto | **No** | — | **LATER** |
| Wordstat / MIG clusters | MIG / APIs | Auto | **No** | — | **LATER** |
| Google Sheets state | n8n pattern | Auto | **No** MVP | — | Quota/lock lessons from Content Agent |

### 9.2 Demo mock file structure (proposed)

```
workspaces/metabot-smart-reporter-demo/
  mock/
    clients.json          # client + project dictionary
    specialists.json      # SEO specialist zones
    reports/
      2026-05-week-1.json
      2026-05-week-2.json
      2026-05-week-3.json
      2026-05-final.json
    templates/
      section-blocks.json # reusable section templates
    assets/
      topvisor-screenshot-example.png
```

### 9.3 Minimal JSON shape (illustrative)

```json
{
  "report_id": "rpt-2026-05-w2-manipulator",
  "client_id": "cli-triumph-manipulator",
  "reporting_month": "2026-05",
  "week_number": 2,
  "report_type": "weekly_preliminary",
  "status": "in_progress",
  "seo_specialist_id": "spec-001",
  "sections": [
    {
      "section_key": "executive_summary",
      "source": "ai_draft",
      "completeness": "partial",
      "content_html": "<p>...</p>"
    }
  ],
  "missing_data": ["traffic_metrics"],
  "topvisor_link": "https://example.topvisor.com/project/123",
  "public_client_url": "/client/reports/2026-05-final-manipulator.html",
  "internal_admin_url": "/admin/reports/rpt-2026-05-w2-manipulator/edit.html"
}
```

---

## 10. Weekly Report Structure

Ordered sections (MVP):

| # | Section key | Title (RU) | Source | Required |
|---|-------------|--------------|--------|----------|
| 1 | `header` | Шапка: клиент, проект, период, неделя | auto + manual | Yes |
| 2 | `short_summary` | Краткое резюме недели | ai_draft + manual | Yes |
| 3 | `what_changed` | Что изменилось | ai_draft + manual | Yes |
| 4 | `rankings_visibility` | Позиции / видимость | manual + screenshot/link | Yes |
| 5 | `traffic_leads` | Трафик / заявки | manual | Optional |
| 6 | `work_completed` | Выполненные работы | manual | Yes |
| 7 | `issues_risks` | Проблемы и риски | manual | Yes |
| 8 | `next_actions` | Следующие шаги | manual + template | Yes |
| 9 | `topvisor` | Topvisor / скриншот | manual link/media | Recommended |
| 10 | `specialist_comment` | Комментарий SEO-специалиста | manual | Yes |
| 11 | `client_conclusion` | Вывод для клиента | ai_draft + manual | Yes |

---

## 11. Monthly Final Report Structure

| # | Section key | Title (RU) | Source | Required |
|---|-------------|--------------|--------|----------|
| 1 | `header` | Шапка: клиент, месяц | auto | Yes |
| 2 | `executive_summary` | Резюме для руководства | ai_draft + roll-up | Yes |
| 3 | `month_dynamics` | Динамика месяца | ai_draft + manual | Yes |
| 4 | `vs_previous_month` | Сравнение с прошлым месяцем | ai_draft | Yes |
| 5 | `work_completed` | Работы за месяц | roll-up + manual | Yes |
| 6 | `rankings_visibility` | Позиции и видимость | manual + media | Yes |
| 7 | `traffic_conversions` | Трафик / конверсии | manual | Optional |
| 8 | `content_technical_links` | Контент / техника / ссылки | manual | Optional |
| 9 | `issues_risks` | Проблемы и риски | roll-up | Yes |
| 10 | `next_month_plan` | План на следующий месяц | manual + template | Yes |
| 11 | `conclusion` | Итоговый вывод | ai_draft + manual | Yes |
| 12 | `attachments` | Приложения / Topvisor | manual | Recommended |

**Roll-up rule:** Monthly final **imports** weekly section summaries as starting drafts; specialist edits before approval.

---

## 12. Demo Page Blueprint

Future workspace: **`workspaces/metabot-smart-reporter-demo/`** (not created in this task).

### 12.1 Page list

| # | File (proposed) | Purpose | User | Key blocks |
|---|-----------------|---------|------|------------|
| 1 | `admin/report-list.html` | All reports filterable by client, month, specialist, status | Operator, specialist | Table, filters, status chips, CTA “Create report” |
| 2 | `admin/report-create.html` | Start weekly or monthly report | Specialist | Client picker, month, week, type selector |
| 3 | `admin/report-edit.html` | Section builder / editor | Specialist | Section list, completeness bars, missing-data panel, AI draft badges, save/submit |
| 4 | `admin/report-preview-internal.html` | Internal preview before approval | Specialist, operator | WIP banner, internal notes visible |
| 5 | `client/report-view-weekly.html` | Client weekly view (if shared) | Client | Clean layout, no admin chrome |
| 6 | `client/report-view-monthly.html` | Client monthly final | Client | Executive summary hero, charts optional static, print-friendly |
| 7 | `admin/project-dictionary.html` | Client/project profile (optional) | Operator | Client facts, URLs, report cadence, Topvisor project link template |

### 12.2 Per-page detail

#### admin/report-list.html

| Aspect | Spec |
|--------|------|
| **Fake data** | 4–6 reports across 2 clients, mixed statuses |
| **CTA** | Create, open editor, preview, mark ready |
| **States** | Empty list, filtered empty, populated |
| **Responsive** | Desktop-first; mobile usable for status check |
| **Proves** | Zone filtering, monthly cadence visibility |

#### admin/report-create.html

| Aspect | Spec |
|--------|------|
| **Fake data** | Client list from mock JSON |
| **CTA** | Create draft → navigate to edit |
| **States** | Validation: missing client/month |
| **Proves** | Weekly vs monthly choice, week 1–3 vs final |

#### admin/report-edit.html

| Aspect | Spec |
|--------|------|
| **Fake data** | Full section set with partial completeness |
| **CTA** | Save section, generate AI draft (mock), submit for approval |
| **States** | missing_data_review highlighting |
| **Proves** | Core product — structured editing + smart assistance UX |

#### client/report-view-monthly.html

| Aspect | Spec |
|--------|------|
| **Fake data** | One polished month (e.g. Триумф / manipulator-triumph.ru style **generic demo**) |
| **CTA** | Print, back to list (admin link hidden) |
| **States** | Published only |
| **Responsive** | **Mobile important** — clients read on phone |
| **Proves** | Client-facing clarity, no jargon overload |

### 12.3 Demo narrative (example client)

**Demo client:** «ООО Демо-Stroy» — site `demo-stroy.example` — specialist «А. Иванова» — May 2026 — weeks 1–3 + final.  
Use **generic** names — not production i-SEO client data unless operator supplies later.

---

## 13. UX Principles

1. **Client language first** on public views — explain SEO metrics in plain Russian.
2. **Jargon quarantine** — raw keyword tables in collapsible or appendix; summary up front.
3. **Two surfaces** — internal editor vs public report; never mix on client URL.
4. **AI draft vs human approved** — badge `AI-черновик` until specialist confirms section.
5. **Editable blocks** — section-granular edit, not one giant textarea (MVP editor).
6. **Report status visible** — specialist and operator always see lifecycle state.
7. **Missing data warnings** — blocking submit optional; warning minimum.
8. **Screenshot-friendly client page** — static PNG export / print CSS later.
9. **WordPress-simple** — eventual WP MVP uses familiar post/meta or ACF-style fields; demo avoids over-engineered UI.
10. **No guaranteed results** — copy rules discourage “рост позиций гарантирован” (consistent with Content Agent SAFE CLAIMS **discipline**).

---

## 14. Automation Architecture Options

| Option | Meaning | Effort | Risk | When | Dependencies |
|--------|---------|--------|------|------|--------------|
| **A. Static demo only** | HTML/CSS/JS mock, JSON data | **Low** | **Low** | **Now — MVP validation** | gulp-starter or plain static |
| **B. WordPress admin MVP** | Custom post type or plugin on i-seo.su; manual fields | Medium | Medium | After demo approval | WPilot patterns, hosting |
| **C. WP + n8n helper** | n8n generates drafts → WP draft posts | Medium–high | Medium | After B stable | n8n, WP REST, credentials |
| **D. n8n + Telegram helper** | Specialist triggers draft via bot | Medium | Medium | Optional parallel | MetaBOT Intake patterns |
| **E. Full API integrations** | Topvisor, Metrica, GSC, Sheets sync | High | High | Post-concept validation | API keys, rate limits |

### Option notes

- **A:** No backend; fastest path to SEO specialist **visual** review after operator approves demo.
- **B:** i-seo.su is **PLANNED** — ATLAS WEB-0005 deferred; WPilot proves WP write path exists on DEV, not i-seo.su production.
- **C:** Reuse MetaBOT **discipline** (sanitized exports, webhook handoff) — **not** 91-node Worker clone.
- **D:** Telegram useful for notifications/draft triggers — **not** primary editor for long reports.
- **E:** Topvisor API — **SAFE UNKNOWN** in repo; operator charter required.

---

## 15. Recommended MVP Path

**Phase 1 (next task): Option A — Static demo**

| Step | Deliverable |
|------|-------------|
| 1 | Scaffold `workspaces/metabot-smart-reporter-demo/` |
| 2 | Mock JSON + 6–7 HTML pages per §12 |
| 3 | Shared CSS component library (report header, section card, status badge, missing-data alert) |
| 4 | Internal navigation between admin pages; client page standalone |
| 5 | `npm run build` or static server preview |
| 6 | Operator review → then SEO specialist review |

**Phase 2 (charter): Option B — WordPress on i-seo.su**

- Manual fields matching section keys.
- Role-based access per specialist.
- Public pretty URL per client report.

**Phase 3 (charter): Option C/D — n8n helper**

- Small workflow: template fill + summary generation → WP draft.
- Separate webhook namespace from SEO Content Agent (`smart-reporter-*` vs `seo-content-agent-*`).

**Explicit non-choice for MVP:** Full API integration (E) before demo + operator sign-off.

---

## 16. Relationship to MetaBOT SEO Agent

| Reuse conceptually | Do NOT copy |
|--------------------|-------------|
| Intake / Worker / Admin **separation idea** — Smart Reporter may have Intake (form/TG) / Generator / Admin (ops) **later** | 91-node Worker pipeline |
| n8n export + grammar discipline | Content QA / factcheck subgraphs |
| Sanitized JSON, import-safe rules | Sheets memory model for long-form content tasks |
| Telegram as **notification** surface | Telegram as primary report editor |
| Lock / busy semantics **if** concurrent generation | 30-min chat lock pattern verbatim |
| OpenRouter for **short** summary blocks only — charter | Full article generation prompts |
| Google Sheets caution (quota, schema drift) | `seo_active_jobs` / `memory` tables as-is |
| MetaBOT Developer approval gates | SEO Agent command routing |

**Product boundary:** Content Agent **creates SEO content**; Smart Reporter **communicates SEO progress to clients**. They may **link** (report cites new articles written) but remain separate products/workflows.

---

## 17. Relationship to MIG

| Later help | Not required for MVP |
|------------|---------------------|
| Niche / competitor snapshots for “market context” appendix | Live MIG session spine |
| Search phrase cluster summaries | MIG → ORCA handoff |
| Anomaly explanation grounded in SERP evidence | Autonomous MIG feeds |
| Competitor visibility notes | MIG v0.1 SERP limitations |

**Rule:** MIG **acquires reality** — Smart Reporter may **cite** approved MIG artifacts in monthly reports when operator attaches them. No MIG dependency for demo or MVP manual path.

---

## 18. Static Demo Build Plan

### 18.1 Folder path

```
X:\AI MARS\workspaces\metabot-smart-reporter-demo\
```

### 18.2 Suggested filenames

```
workspaces/metabot-smart-reporter-demo/
  README.md
  package.json                 # if gulp-starter copy
  mock/                        # §9.2
  src/
    pages/admin/               # report-list, create, edit, preview, dictionary
    pages/client/              # weekly, monthly views
    partials/                  # header, section-card, status-badge
    scss/
  dist/                        # build output — gitignore
  docs/
    demo-walkthrough.md        # operator script for review
```

### 18.3 Visual style direction

| Element | Direction |
|---------|-----------|
| Brand | i-SEO professional — clean, light background, accent blue/teal (**OPERATOR_CLARIFICATION** — refine at demo task) |
| Typography | Readable sans (system stack or existing starter fonts) |
| Layout | Max-width ~960px client report; wider admin tables |
| Data viz | Static bars/tables for rankings — no live charts MVP |
| Icons | Status/completeness only — avoid decorative clutter |

### 18.4 Components list

| Component | Use |
|-----------|-----|
| `report-header` | Client, site, period, specialist |
| `report-status-badge` | Lifecycle state |
| `section-card` | Editable/report section |
| `completeness-bar` | Section/submit readiness |
| `missing-data-alert` | Warning list |
| `ai-draft-badge` | Source indicator |
| `topvisor-embed` | Link + screenshot frame |
| `work-log-list` | Completed / planned works |
| `client-summary-hero` | Monthly executive block |
| `admin-table` | Report list filters |

### 18.5 Website Factory vs custom

| From Website Factory / FP-0002 pattern | Custom for Smart Reporter |
|----------------------------------------|---------------------------|
| Page registry JSON | Report entity schema |
| Template + generator architecture | Section builder UX |
| Static dist preview discipline | Report status workflow UI |
| Navigation registry | Admin/client route split |
| Evidence receipts (optional) | Mock data pack |

**Starter choice:** New minimal gulp-starter **client/product copy** workspace — **not** canonical template repo demo content.

### 18.6 Build order

1. Mock data files (`clients`, `specialists`, 4 report JSONs).
2. Shared SCSS + components.
3. `client/report-view-monthly.html` — **hero client proof** first.
4. `admin/report-edit.html` — **core editor** second.
5. `admin/report-list.html` + create flow.
6. Weekly client view + internal preview.
7. Optional project dictionary page.
8. `npm run build` + fix errors.
9. Operator walkthrough doc.

---

## 19. Non-Goals for MVP

- Full Topvisor / Wordstat / Metrica / GSC API integration
- Complex BI dashboards or live analytics
- Autonomous report publishing without human approval
- Large n8n graph (>15 nodes) before concept validation
- SEO specialist interviews as **gate** before demo
- Replacing human specialist judgment on facts
- Production write to i-seo.su WordPress in demo task
- Merging with MetaBOT SEO Content Agent workflow
- OPS WF-01 replacement or duplication
- Google Sheets as primary store (unless later charter — learn quota lessons)
- Telegram as full report authoring UI
- Registry row / git commit / production deploy in **this** task

---

## 20. SAFE UNKNOWN

| Topic | Unknown | Would verify |
|-------|---------|--------------|
| i-SEO Report Hub official name / URL structure | Operator + future IA on i-seo.su | Operator decision post-demo |
| Topvisor account model and API availability | No repo evidence | Operator credentials / Topvisor docs |
| Whether weekly reports go to clients or internal-only | Policy | Operator / SEO lead |
| Exact ranking metrics tracked (positions, visibility %, etc.) | Field schema | SEO specialist input **after** demo |
| Storage backend for production reports | WP only vs WP+Storage | Infrastructure charter |
| LLM provider for smart blocks | OpenRouter assumed (MetaBOT pattern) | Operator |
| Integration with ATLAS client entities | ATLAS deferred web | ATLAS population wave |
| OPS cross-link (studio ops vs client SEO reports) | Boundary | Operator |
| n8n hosting namespace for Smart Reporter | Same instance as Content Agent? | Operator n8n admin |
| Mobile app / PDF export requirements | — | Operator post-demo |
| Multi-language reports | — | Operator |

---

## 21. Files Created

| Path | Action |
|------|--------|
| `projects/metabot-seo-content-agent/reports/REPORT-metabot-smart-reporter-mvp-concept-and-demo-blueprint.md` | **Created** (this file) |

---

## 22. Git Status

- **Branch:** `mars/canonical-post-recovery`
- **This task:** one new untracked file under `projects/metabot-seo-content-agent/reports/`
- **Foreign WIP:** unchanged; not staged
- **Commit / push:** none (per task charter)

---

## 23. Final Status

**COMPLETE — MVP concept and demo blueprint completed**

Next recommended task: scaffold **Option A** static demo per §18 under `workspaces/metabot-smart-reporter-demo/` after operator approves this blueprint.

---

Awaiting operator review.
