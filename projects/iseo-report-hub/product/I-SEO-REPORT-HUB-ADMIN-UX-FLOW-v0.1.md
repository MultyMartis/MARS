# I-SEO Report Hub — Admin UX Flow v0.1

**Status:** PLANNING — documentation-first only  
**Implementation:** **NOT STARTED** — no wp-admin UI, no HTML prototypes in this task  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-10

---

## 1. Status and Scope

This document plans the **WordPress admin/workspace UX** for SEO specialists, reviewers, and admins on i-seo.su.

| In scope | Out of scope |
|----------|--------------|
| Role capabilities and screen inventory | PHP/JS/CSS implementation |
| Specialist, reviewer, admin flows | Website Factory workspace creation |
| Weekly/monthly screen field lists | Live wp-admin access |
| Validation rules (product level) | n8n workflow wiring |
| Website Factory prototype **candidates** (list only) | Client portal login |

**Target:** Custom admin module within WordPress on i-seo.su (may extend beyond default wp-admin chrome — **SAFE UNKNOWN**).

---

## 2. User Roles

### 2.1 Admin / Owner

| Dimension | Detail |
|-----------|--------|
| **Sees** | All clients, projects, cycles, reports, dictionary, settings, users, notification events |
| **Can do** | Create/edit clients and projects; assign specialists and reviewers; manage work dictionary and block library; configure project profiles; manage system settings; override statuses (with audit); publish policy configuration |
| **Cannot do** | Bypass audit trail; store credentials in report fields; auto-publish without approval policy |

**Typical users:** Nikita / i-SEO leadership.

### 2.2 SEO Lead / Reviewer

| Dimension | Detail |
|-----------|--------|
| **Sees** | Review queue; projects in scope (all or team — **SAFE UNKNOWN**); weekly and monthly reports submitted for review; internal comments |
| **Can do** | Approve or request revision; add reviewer comments; view evidence and metrics; mark client-ready after approval |
| **Cannot do** | Edit dictionary (unless also admin); assign users; delete published versions without admin; publish if policy requires separate publish action |

**Typical users:** Senior SEO / team lead.

### 2.3 SEO Specialist

| Dimension | Detail |
|-----------|--------|
| **Sees** | Assigned projects only; active reporting cycles; own drafts; review feedback on own submissions |
| **Can do** | Create/edit weekly checkpoints and monthly final for assigned projects; select dictionary works; enter metrics; attach evidence and Topvisor links; submit for review; revise after feedback |
| **Cannot do** | See unassigned projects; approve own reports; publish client-visible reports (unless policy exception — not recommended); access integration credentials |

**Typical users:** Denis, Ilya, and i-SEO SEO team.

### 2.4 Account / Manager (optional)

| Dimension | Detail |
|-----------|--------|
| **Sees** | Client-facing approved reports; project status summary (read-heavy) |
| **Can do** | Optional comment; trigger "sent to client" flag; view publish history |
| **Cannot do** | Edit report content; approve technical SEO sections |

**MVP:** **Optional / TBD** — may defer to post-MVP.

### 2.5 Client read-only (later optional)

| Dimension | Detail |
|-----------|--------|
| **Sees** | Approved web report via controlled link only |
| **Can do** | Read (no login in MVP) |
| **Cannot do** | Edit; see drafts; see internal notes |

**Not MVP** — controlled URL delivery only.

---

## 3. Main Admin Areas

Proposed WordPress admin/workspace navigation (logical modules):

| Area | Purpose |
|------|---------|
| **Dashboard** | Deadlines, overdue weeklies, pending reviews, month-close countdown |
| **My Projects** | Specialist entry: assigned projects with cycle status |
| **Clients** | Client list and detail |
| **SEO Projects** | Project CRUD, profile, assignments |
| **Reporting Calendar** | Month view of cycles/checkpoints across projects |
| **Reporting Cycles** | Cycle list per project/month |
| **Weekly Checkpoints** | Week 1–3 editors and list |
| **Monthly Reports** | Month-close report list and editor |
| **Work Dictionary** | Canonical work items (admin edit; specialist pick) |
| **Block Library** | Block definitions and profile bindings |
| **Metrics / Charts** | Metric schema reference; chart preview in report context |
| **Evidence Library** | Cross-project evidence search (optional MVP-lite: in-context only) |
| **Review Queue** | Reviewer inbox |
| **Published Reports** | Publish history, links, revoke |
| **Notification Events** | Event log for operator/n8n debugging |
| **Settings** | Profiles, deadlines, publish policy, n8n webhook URL (no secrets displayed) |

**UX note:** Dashboard + My Projects are primary specialist entry points. Admin-heavy areas hidden from specialist role.

---

## 4. SEO Specialist Flow

Step-by-step monthly operational flow:

1. **Login** to i-seo.su admin / Report Hub workspace (WP authenticated user).
2. **Dashboard** shows assigned projects, current month cycle status, overdue indicators.
3. Open **My Projects** → select project → see **current Reporting Cycle** (YYYY-MM) and deadline hints.
4. **Week 1 checkpoint:** fill summary, works, metric notes, blockers, evidence, next week plan → save draft or mark in progress.
5. **Week 2 checkpoint:** same structure; reference readiness toward month close.
6. **Week 3 checkpoint:** same; explicit readiness flag for month-close.
7. **Month Close — Monthly Final Report:** open monthly editor; executive summary and KPI sections; rollup works from weeks (select/edit, not blind auto-copy).
8. **Select completed works** from Work Dictionary; add custom notes per item.
9. **Add manual metrics** in metric/chart blocks; enter specialist interpretation.
10. **Attach evidence** (screenshots, links) and **Topvisor external report link** (+ optional preview screenshot).
11. **Submit for review** — status → `submitted`; notification event emitted.
12. If **revision requested:** read reviewer comments → edit → resubmit.
13. After **approval:** specialist or reviewer triggers **publish** (per policy) → Published Report Version created → client web link available.
14. Copy/send link to client (manual MVP; n8n delivery later).

---

## 5. Reviewer Flow

1. Open **Review Queue** — filters: weekly (if enabled), monthly, overdue.
2. Open submitted report — read-only blocks with comment panel.
3. **Approve** → status `approved` → eligible for client-ready/publish.
4. **Request revision** → status `revision` → specialist notified (event; n8n later).
5. Add **reviewer comments** (internal or visible to specialist).
6. On monthly approval → mark **client-ready** or confirm publish prerequisites.
7. **Final approval** recorded in Review entity with timestamp and reviewer user.

Reviewer does not edit specialist content inline in MVP (comments only) — **SAFE UNKNOWN** if inline suggest mode wanted later.

---

## 6. Admin Flow

1. **Users:** create WP users; assign Report Hub roles.
2. **Assign projects:** link specialist + optional reviewer per SEO Project.
3. **Work Dictionary:** import/sanitize from Nikita materials; curate client-facing wording.
4. **Block Library:** enable/disable blocks per profile; set required blocks.
5. **Project Profiles:** configure default block sets (service, e-commerce, local, etc.).
6. **Settings:** reporting deadlines, weekly client-visible policy, webhook endpoints for n8n (future).
7. **Audit:** view Published Reports history; revoke link if needed.

---

## 7. Weekly Checkpoint Screen

### Header

- Project name, client, month, week number (1|2|3)
- Cycle status badge
- Due date indicator (optional)
- Assigned specialist

### Sections and fields

| Section | Fields |
|---------|--------|
| **Status** | `draft` / `in_progress` / `submitted` / `approved` / `revision` |
| **Summary** | Short week narrative (required for submit) |
| **Completed work this week** | Dictionary multi-select + per-item notes |
| **Important metric changes** | Free text or lightweight metric notes (not full KPI deck) |
| **Blockers** | Text |
| **Evidence** | URL list, screenshot upload, captions |
| **Topvisor link** | Optional URL + preview screenshot (if used this week) |
| **Next week plan** | Short text |
| **Readiness toward month close** | Scale or text: on track / at risk / blocked |
| **Internal notes** | Specialist-only; never client-visible |
| **Ready for review** | Checkbox or submit action |
| **Publish to client** | Optional flag (policy TBD; default off in MVP) |

### Actions

- Save draft
- Submit for review (if weekly review enabled)
- Mark complete without review (if policy allows weeklies without review)

---

## 8. Monthly Report Screen

### Header

- Project, client, month, profile type
- Status pipeline: draft → … → published
- Review state and publish state

### Sections

| Section | Content |
|---------|---------|
| **Executive summary** | Required client-facing narrative |
| **KPI overview** | Metric cards from manual snapshots |
| **Traffic** | Block instance: metrics + interpretation |
| **Positions / visibility** | Rankings, SERP notes, Topvisor link card |
| **Conversions / leads** | If applicable per profile |
| **Completed work rollup** | Dictionary items for full month |
| **Technical SEO** | Profile-optional block |
| **Content** | Profile-optional block |
| **Link building** | Profile-optional block |
| **Local SEO** | Profile-optional block |
| **E-commerce** | Profile-optional block |
| **Risks / blockers** | Open issues |
| **Next month plan** | Forward plan |
| **Evidence / appendix** | Gallery and document links |
| **External report links** | Topvisor primary; others optional |
| **Specialist interpretation** | Analysis layer (distinct from executive summary) |
| **Review status** | Submission history, reviewer comments |
| **Publish status** | Client-ready flag, published link, version number |

### Actions

- Save draft
- Submit for review
- Preview client web report (render from current draft — watermark "DRAFT" recommended)
- After approval: Publish / Generate client link

---

## 9. Validation Rules

Product-level validation (enforcement in implementation):

| Rule | Behavior |
|------|----------|
| Monthly submit without executive summary | **Block submit** |
| Publish without approval | **Block publish** |
| Required blocks depend on project profile | **Warn or block** — missing required block |
| Evidence required on dictionary items | **Warn** if `evidence_required` and no attachment |
| Topvisor link | **Optional**; **recommended** warning if positions block enabled |
| Weekly overdue | **Dashboard warning**; notification event |
| Internal notes in client render | **Must strip** on publish snapshot |
| Empty completed works on monthly | **Warn** (not necessarily block) |
| Metric fields empty in KPI block | **Warn** |
| Revision round | Must address reviewer comment flag before resubmit (optional strict mode) |

---

## 10. Website Factory Prototype Candidates

Screens recommended for **optional** future Website Factory HTML/static prototypes (separate operator charter required):

| Priority | Screen | Purpose |
|----------|--------|---------|
| High | **Client web report page** | Validate client-facing layout, branding, block render |
| High | **Monthly report editor** | Complex multi-block editor layout |
| High | **SEO specialist dashboard** | Deadlines and project cards |
| Medium | **Weekly checkpoint editor** | Shorter form; mobile-friendly check |
| Medium | **Review queue** | Reviewer inbox UX |
| Medium | **Project detail** | Cycle timeline, assignment context |
| Medium | **Report block layout** | Individual block templates (metric cards, work list, Topvisor card) |
| Low | **Metrics chart block** | Chart placeholder and data binding UX |

**Explicit:** No workspace created in this task. Prototypes inform Anton's WP admin UX; they do not replace i-seo.su production.

---

## 11. SAFE UNKNOWN

| Topic | Notes |
|-------|-------|
| Native wp-admin vs custom SPA-like admin shell | Anton + hosting decision |
| Weekly checkpoints require review in MVP? | Operator policy |
| Weekly client-visible default | Operator policy |
| Inline editing by reviewer | Deferred |
| Dashboard widget set | Minimal MVP vs rich |
| Mobile admin support priority | Specialists may use tablet |
| Russian-only UI vs bilingual | Default Russian assumed |
| Integration with existing i-seo.su proposal generator UI | Reuse patterns? Unknown |
| Autosave and conflict if two editors | Multi-user edge case |

---

## Document control

- **Does not claim:** any admin UI exists
- **Upstream:** [I-SEO-REPORT-HUB-WORDPRESS-DATA-MODEL-v0.1.md](I-SEO-REPORT-HUB-WORDPRESS-DATA-MODEL-v0.1.md), [I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md](I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md)
- **Related:** Website Factory = prototype lane only per [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md)
