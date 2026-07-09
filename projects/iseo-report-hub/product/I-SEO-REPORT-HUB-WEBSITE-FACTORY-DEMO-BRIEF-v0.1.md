# I-SEO Report Hub — Website Factory Demo Brief v0.1

**Status:** PLANNING — brief for future static prototype build  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-10  
**Build:** **NOT STARTED**

---

## 1. Status

This document is a **build brief** for a future Website Factory static prototype task.

| Fact | State |
|------|-------|
| HTML/CSS/JS demo | **Does not exist** |
| Gulp workspace | **Not created** |
| npm build | **Not run** |
| Production deployment | **Excluded** |

Operator must approve a separate **Website Factory demo build charter** before any workspace or code work.

---

## 2. Target Workspace

**Status:** **SAFE UNKNOWN** until build charter.

**Candidate only (do not create now):**

```
workspaces/website-factory-operations/iseo-report-hub-prototype/
```

Alternative paths may be chosen in build charter if Website Factory operations conventions require a different layout. This brief does **not** create or register any workspace.

---

## 3. Pages to Build in Future Task

### 1. Dashboard

**Purpose:** SEO specialist overview — primary entry after login (mock).

**Must show:**
- Assigned projects list with status
- Current reporting cycles (month)
- Deadlines and overdue indicators
- Reports needing action (draft, revision, submit)
- Warnings / missing required fields
- Quick links to project detail, weekly editor, monthly editor

**Reference:** [I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md](I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md) §3 Dashboard, §4 steps 1–2.

---

### 2. Project Detail / Cycle Overview

**Purpose:** One project's reporting state for current month.

**Must show:**
- Client and project metadata (name, site URL, profile type)
- Project profile badge (e-commerce)
- Current monthly cycle (July 2026)
- Week 1 / Week 2 / Week 3 status cards
- Month Close status
- KPI snapshot (summary cards)
- Latest evidence links (sample)
- Actions: open weekly editor, open monthly editor, submit, preview

**Reference:** [I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md](I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md) §2 Reporting Cycle.

---

### 3. Weekly Checkpoint Editor

**Purpose:** Fast weekly fill for weeks 1–3.

**Must show:**
- Week number (1, 2, or 3)
- Status badge (draft / in progress / submitted / approved / revision)
- Short summary (required narrative)
- Completed works this week (dictionary-style checklist)
- Metric notes (lightweight — not full KPI deck)
- Blockers
- Evidence links (placeholder URLs)
- Topvisor link field (optional URL + preview placeholder)
- Next week plan
- Internal notes (visually marked specialist-only)
- Controls: Save draft, Ready for review, Publish to client (disabled or flagged optional per policy)

**Reference:** [I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md](I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md) §7.

---

### 4. Monthly Report Editor

**Purpose:** Assemble month-close final report.

**Must show:**
- Executive summary
- KPI cards block
- Traffic block (metrics + short interpretation)
- Positions / visibility block
- Leads / conversions block (e-commerce profile)
- Completed work rollup (full month)
- Optional profile blocks (technical, content, link — at least one shown as example)
- Risks / blockers
- Next month plan
- Evidence / appendix section
- External report links (Topvisor card)
- Specialist interpretation (distinct from executive summary)
- Review status panel (submitted / revision / approved)
- Actions: Save draft, Submit for review, Preview client report (watermarked draft), Publish (post-approval mock state)

**Reference:** [I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md](I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md) §8.

---

### 5. Client Web Report Page

**Purpose:** Client-facing approved report presentation.

**Must show:**
- i-SEO header / branding area
- Client name, project/site, period (July 2026)
- Executive summary
- KPI cards (3–6 headline metrics)
- Chart placeholders (traffic, visibility — static SVG or placeholder blocks)
- Completed works (dictionary wording)
- Weekly progress summary (condensed week 1–3 — optional block)
- Topvisor external report card (link CTA, optional screenshot thumbnail)
- Risks / blockers (if any in demo data)
- Next month plan
- Evidence appendix (collapsible or secondary section)
- Footer: publication date, version metadata, i-SEO contact

**Tone:** Calmer than admin — no edit controls, no internal notes.

**Reference:** [I-SEO-REPORT-HUB-WEB-REPORT-STRUCTURE-v0.1.md](I-SEO-REPORT-HUB-WEB-REPORT-STRUCTURE-v0.1.md) §3.

---

### 6. Review Queue / Reviewer View

**Purpose:** SEO lead review inbox.

**Must show:**
- Reports awaiting review (weekly optional; monthly required in demo)
- Status per item
- Assigned specialist name
- Project name
- Due date
- Missing required fields indicator
- Actions: Approve, Request revision (mock — no backend)
- Reviewer comment panel (sample thread)

**Reference:** [I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md](I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md) §5 Reviewer Flow.

---

## 4. Shared Components

Build task should reuse consistent components across admin screens:

| Component | Usage |
|-----------|-------|
| Sidebar / topbar | Admin navigation between six screens |
| Status badges | Cycle, checkpoint, report, review states |
| KPI cards | Metric label + value + optional delta |
| Chart placeholder | Static block for traffic/visibility charts |
| Report block card | Generic section wrapper for monthly editor |
| Evidence card | URL + caption + optional thumbnail |
| Topvisor card | Provider label, description, external link CTA |
| Work item checklist | Dictionary items with check/select state |
| Comments / review panel | Reviewer ↔ specialist thread |
| Timeline / checkpoint strip | Week 1–3 + Month Close on project detail |
| Alert / missing field banner | Validation warnings (visual only) |
| Publish / preview controls | Button group with disabled states where appropriate |

Client report page uses a **subset** — no sidebar admin chrome; header/footer only.

---

## 5. Demo Data

**Sanitized fake data only.** No secrets. No real client credentials.

### Identity

| Field | Demo value |
|-------|------------|
| **Client** | Demo Industrial Tools |
| **Site** | demo-tools.example |
| **Project name** | Demo Industrial Tools — SEO |
| **Profile** | e-commerce |
| **Specialist** | SEO Specialist Demo |
| **Reviewer** | Lead SEO Demo |
| **Period** | July 2026 |

### KPIs (manual snapshot)

| Metric | Value |
|--------|-------|
| Organic visits | 4,820 |
| Search visibility | +8% |
| Top-10 queries | 146 |
| Leads / forms | 23 |

### Cycle status

| Checkpoint | Status |
|------------|--------|
| Week 1 | completed |
| Week 2 | completed |
| Week 3 | needs review |
| Month Close | draft |

### External links

| Type | Value |
|------|-------|
| Topvisor | `https://example.com/topvisor-demo-report` |
| Evidence | `https://example.com/evidence-demo-1`, `https://example.com/evidence-demo-2` |

### Sample completed works (dictionary-style labels)

- Technical audit and critical fixes
- Category meta optimization (batch)
- Internal linking update — catalog section
- Content page published: buying guide
- Monitoring setup review

### Sample blockers / risks

- Supplier catalog delay affecting new landing pages
- Seasonal demand spike — monitor server response times

### Next month plan (sample)

- Expand category hubs for power tools
- Launch comparison content cluster
- Review Topvisor visibility report with client

**If Makita or other corpus names are used:** prefix with "Demo" and mark sanitized in workspace README.

---

## 6. UX Notes

- Admin pages may be **dense but readable** — tables and cards over long prose.
- Client report must be **clean and calm** — business owner audience.
- Prioritize **clarity over decoration** — no fake AI widgets or animated dashboards.
- Use cards and tables where they aid scanning.
- Avoid overly complex filters in v0.1 — static lists sufficient.
- Do not mimic full WordPress admin chrome unless it aids recognition — custom Report Hub shell acceptable.
- Show enough structure to **guide future WP implementation** — field names align with data model doc where practical.
- Internal notes visually distinct from client-visible fields.
- Draft preview on client report should show **DRAFT** watermark if demo includes preview state.

---

## 7. Responsive Notes

| Surface | Priority |
|---------|----------|
| Admin screens | **Desktop-first** (≥1025px primary) |
| Client web report | **Mobile-friendly** — KPI stack, readable tables, collapsible evidence |
| Admin on mobile | Acceptable degradation — not primary v0.1 goal |

Use MARS gulp starter breakpoint conventions when build task runs — do not invent ad hoc breakpoints in brief.

---

## 8. Build Constraints for Future Task

Future build task **may** use Website Factory / gulp starter under operator charter.

| Rule | Requirement |
|------|-------------|
| Framework | No new framework unless existing Website Factory rules allow |
| API | No real API calls |
| Backend | No backend, database, or auth |
| Secrets | No credentials in repo or demo content |
| Image generation | No AI image generation unless separately approved |
| Production deployment | **Excluded** |
| WordPress | **Excluded** — static HTML only |
| n8n | **Excluded** |
| dist edits | Follow starter rules — build output only via gulp |

Production mode for Factory workspace: likely **TEMPLATE_ART** (workflow/UX exploration) unless operator declares **PIXEL_PERFECT** for client report screen — **SAFE UNKNOWN** until build charter.

---

## 9. Review Questions for Operator

After demo build, operator should review:

1. **Workflow clarity** — Can a specialist follow month rhythm without training doc?
2. **Screen completeness** — Are six screens sufficient for MVP UX confidence?
3. **Report readability** — Is client page suitable to send to a business owner?
4. **Visual tone** — Admin vs client contrast acceptable for i-SEO brand direction?
5. **Fields to remove/add** — Any noise or missing inputs vs data model?
6. **Implementation brief impact** — Does [I-SEO-REPORT-HUB-IMPLEMENTATION-BRIEF-v0.1.md](I-SEO-REPORT-HUB-IMPLEMENTATION-BRIEF-v0.1.md) need revision after demo review?

Capture answers in a follow-up REPORT — not in this brief.

---

## Document control

- **Parent charter:** [I-SEO-REPORT-HUB-WEBSITE-FACTORY-PROTOTYPE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-WEBSITE-FACTORY-PROTOTYPE-CHARTER-v0.1.md)
- **Does not claim:** any build, workspace, or HTML exists
