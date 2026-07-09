# i-SEO Report Hub — Report Model v0.1

**Status:** APPROVED model persist 2026-07-10  
**Implementation:** **NOT STARTED**

---

## 1. Overview

Report Hub organizes work around a **monthly Reporting Cycle** per client project. Each cycle contains three **Weekly Checkpoints** and one **Monthly Final Report**. Content is composed from a **Block Library**, populated via **Work Dictionary** entries, manual data, evidence, and external links.

---

## 2. Reporting Cycle entity

Container for one month of reporting on one project.

| Field | Description |
|-------|-------------|
| **month** | Reporting month (YYYY-MM) |
| **project** | Reference to client/project record |
| **owner** | Assigned SEO specialist |
| **status** | Cycle-level status (see §8) |
| **weekly_checkpoints** | Week 1, 2, 3 entities |
| **monthly_final** | Month-close final report entity |
| **reviewer** | Assigned reviewer (optional until review stage) |
| **published_version** | Pointer to approved client-visible version (if any) |

---

## 3. Weekly Checkpoint entity

**Week numbers:** 1, 2, 3 only (within monthly cycle).

**Purpose:** Preliminary status update — **not** a full monthly report copy.

| Field | Description |
|-------|-------------|
| **week_number** | 1, 2, or 3 |
| **status** | See §8 |
| **summary** | Short week status narrative |
| **completed_works** | Work dictionary items completed this week |
| **metric_notes** | Important metric changes or anomalies (not full KPI deck) |
| **blockers** | Current blockers or risks |
| **evidence** | Links, screenshots, files |
| **next_short_plan** | Plan for next week |
| **readiness** | Readiness indicator for month-close |
| **review_state** | Draft / submitted / approved / revision |
| **optional_client_publish_flag** | Whether checkpoint may be shared with client (operator policy TBD) |

**Weekly focus areas:**
- Status
- Completed work this week
- Important metric changes or anomalies
- Blockers
- Evidence links
- Next short plan
- Readiness toward month close

---

## 4. Monthly Final Report entity

**Purpose:** Comprehensive month-close client-ready report (after review/approval).

| Section | Content |
|---------|---------|
| **executive_summary** | High-level month narrative for client |
| **kpi_overview** | Key indicators snapshot |
| **traffic** | Traffic metrics and interpretation |
| **positions_visibility** | Rankings, visibility, SERP notes |
| **conversions_leads** | Conversions/leads if available |
| **completed_works_rollup** | All significant works for the month |
| **optional_blocks** | Technical, content, link building, local, e-commerce — per project profile |
| **specialist_interpretation** | SEO specialist commentary and analysis |
| **risks_blockers** | Open risks and blockers |
| **next_month_plan** | Plan for upcoming month |
| **evidence_appendix** | Evidence collection, external links |
| **approval** | Reviewer approval record |
| **published_version** | Immutable approved snapshot for client renderer |

**Monthly focus areas:**
- Executive summary
- Month-level results
- Traffic, visibility/positions, conversions/leads
- Completed works rollup
- Specialist interpretation
- Risks/blockers
- Next month plan
- Evidence and appendices

---

## 5. Block Library

Reusable content blocks composing weekly and monthly reports.

| Block type | Usage |
|------------|-------|
| **Required blocks** | Always present for report type (e.g. summary, works, metrics) |
| **Optional blocks** | Added per project need |
| **Profile-specific blocks** | Activated by Project Type Profile |

**Examples (non-exhaustive):**
- Executive summary
- Traffic overview
- Positions/visibility
- Conversions/leads
- Completed works list
- Technical SEO summary
- Content works
- Link building
- Local SEO
- E-commerce metrics
- Topvisor external link block
- Evidence gallery
- Next period plan
- Risks and blockers

Block rendering on client web report: **SAFE UNKNOWN** — template design deferred.

---

## 6. Project Type Profiles

Profile determines default block set and dictionary applicability.

| Profile | Typical emphasis |
|---------|------------------|
| **service** | Leads, local visibility, content, works list |
| **e-commerce** | Revenue/traffic, categories, technical, content |
| **local** | Maps, local pack, reviews, geo pages |
| **B2B** | Lead quality, content, long-cycle metrics |
| **content-heavy** | Content production, indexing, traffic to content |
| **technical-heavy** | Crawl, indexation, Core Web Vitals, technical fixes |
| **custom** | Operator-defined block mix |

One project has one primary profile; optional secondary blocks may be enabled manually.

---

## 7. Work Dictionary

Canonical catalog of SEO work items for standardized reporting.

| Attribute | Description |
|-----------|-------------|
| **canonical_work_item** | Internal standard name |
| **client_facing_wording** | Text shown to client in reports |
| **internal_notes** | Specialist-only guidance |
| **project_applicability** | Which profiles this work applies to |
| **recurrence** | One-time / monthly / as-needed |
| **evidence_required** | Whether evidence attachment is mandatory |
| **report_block_relation** | Which block(s) this work populates |

**Source foundation:** Nikita materials in Storage corpus (sanitized extraction pending).

**Exclusion:** Credential/access rows (Nikita XLSX Лист2 class) — **never** in dictionary.

---

## 8. Data modes

How block/report fields receive values:

| Mode | Description | MVP |
|------|-------------|-----|
| **template** | Pre-filled from report template | Yes |
| **manual** | Specialist typed entry | Yes |
| **external_link** | URL to Topvisor or other online report | Yes |
| **screenshot** | Image evidence attachment | Yes |
| **work_dictionary** | Selected dictionary item | Yes |
| **project_profile** | Derived from project type settings | Yes |
| **later_api** | Imported from external API | Post-MVP |
| **ai_draft** | AI-generated draft for human edit | Post-MVP |

---

## 9. Statuses

Workflow states for cycles, checkpoints, and monthly reports:

| Status | Meaning |
|--------|---------|
| **draft** | Initial creation, incomplete |
| **data_collection** | Gathering metrics and evidence |
| **specialist_input** | Specialist actively filling content |
| **review** | Submitted to reviewer |
| **revision** | Returned for corrections |
| **approved** | Reviewer approved internal version |
| **client-ready** | Approved for client-facing render |
| **published_sent** | Published or delivered to client |
| **archived** | Closed historical record |

Exact transitions and who may trigger each: **SAFE UNKNOWN** — admin UX planning gate.

---

## 10. Evidence model

Evidence attaches to weekly checkpoints, monthly sections, or individual work items.

| Type | MVP support |
|------|-------------|
| **URL link** | Yes |
| **Screenshot/image file** | Yes |
| **Document file** | Yes (policy TBD) |
| **Topvisor report link** | Yes — primary external pattern |
| **Embedded iframe** | Optional later — not MVP required |

---

## 11. External links (Topvisor and others)

**MVP pattern:** dedicated field for external online report URL + optional preview screenshot in evidence.

Does not require live embed. API sync deferred to later phase.

---

## 12. Corpus-informed design notes

From attested corpus review (not re-audited here):

- **Denis pattern:** branded document flow → informs client web report visual treatment
- **Ilya pattern:** compact + Topvisor link → informs MVP external link block
- **Unified core:** same cycle and block structure; stylistic flexibility via profiles and optional blocks

---

## 13. SAFE UNKNOWN

- Whether weekly checkpoints are ever client-visible by default
- Metric field catalog (exact KPI list per profile)
- Versioning model for in-place edits vs immutable snapshots
- Comparison/delta display week-over-week in UI
- Multi-specialist handoff on same project cycle

---

## Document control

- **Created:** 2026-07-10
- **Entity storage implementation:** not started
