# I-SEO Report Hub — WordPress Data Model v0.1

**Status:** PLANNING — documentation-first only  
**Implementation:** **NOT STARTED** — no plugin, no schema, no migrations  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-10

---

## 1. Status and Scope

This document defines the **planned domain data model** for i-SEO Report Hub as a WordPress module on i-seo.su.

| In scope | Out of scope |
|----------|--------------|
| Entity definitions, fields, relationships | PHP, SQL, plugin code |
| WordPress storage **candidates** (not final decisions) | Database migrations |
| MVP vs later separation | Live wp-admin or hosting access |
| Security and access principles | API integration implementation |
| SAFE UNKNOWN for unresolved decisions | Claiming any runtime exists |

**Authority:** WordPress on i-seo.su is the intended **source of truth** for report data. MARS holds planning documentation only. n8n is an external helper. Website Factory is a prototype lane only.

---

## 2. Platform Decision

| Layer | Role |
|-------|------|
| **WordPress / i-seo.su** | Source of truth: clients, projects, cycles, reports, dictionary, evidence, approval, published versions |
| **n8n** | External automation/AI helper: reminders, completeness checks, delivery notifications — **not** SoT |
| **MARS** | Documentation and programme locus — **not** runtime |
| **Website Factory** | Optional HTML/static UI prototypes before WP build — **not** runtime owner |

Production programmatic processes run on i-seo.su hosting. Report Hub does not depend on MARS Localhost for production.

---

## 3. Entity Overview

| Entity | Purpose (summary) |
|--------|-------------------|
| **Client** | Business customer of i-SEO; grouping for projects and reports |
| **SEO Project** | Active SEO engagement tied to one client; specialist assignment scope |
| **Project Profile** | Project type configuration (service, e-commerce, local, etc.) driving blocks and dictionary applicability |
| **Reporting Cycle** | One calendar month of reporting for one project |
| **Weekly Checkpoint** | Week 1–3 preliminary status report within a cycle |
| **Monthly Final Report** | Month-close comprehensive client-ready report |
| **Report Block Definition** | Reusable block template in the block library |
| **Report Block Instance** | Populated block within a weekly or monthly report |
| **Work Dictionary Item** | Canonical SEO work catalog entry |
| **Completed Work Item** | Instance of dictionary work completed in a period |
| **Metric Snapshot** | Point-in-time metric values (manual or later imported) |
| **Chart Definition** | Chart type/config bound to metrics |
| **Evidence Asset** | Link, screenshot, or file proving work or metric claims |
| **External Report Link** | URL to third-party report (Topvisor primary MVP pattern) |
| **Comment / Specialist Note** | Narrative commentary; internal vs client-visible distinction |
| **Review / Approval** | Reviewer decision record on checkpoint or monthly report |
| **Published Report Version** | Immutable approved snapshot for client web renderer |
| **Notification Event** | Event record for future n8n consumption |
| **Integration Reference** | Metadata pointer to external systems (no credentials) |
| **User / Role Assignment** | WP user linked to project with role capabilities |

---

## 4. Entity Details

### 4.1 Client

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Identify the business customer; anchor for projects and client-facing report branding context |
| **Key fields** | `client_id`, `display_name`, `legal_name` (optional), `status` (active/archived), `primary_contact` (optional text), `internal_notes`, `created_at`, `updated_at` |
| **Relationships** | One Client → many SEO Projects |
| **Data source** | manual (admin); later optional ATLAS consumer |
| **MVP / Later** | MVP — basic fields |
| **WP storage candidate** | CPT `iseo_client` or custom table `iseo_clients`; taxonomy unlikely |
| **Security** | Admin and assigned specialists see client name on assigned projects; no credentials in client record |

### 4.2 SEO Project

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Single SEO engagement; unit of assignment, cycles, and access scope |
| **Key fields** | `project_id`, `client_id`, `project_name`, `site_url` (optional), `status`, `assigned_specialist_user_id`, `assigned_reviewer_user_id` (optional), `profile_id`, `reporting_start_month`, `internal_notes`, `created_at` |
| **Relationships** | Belongs to Client; has Project Profile; has many Reporting Cycles; has User assignments |
| **Data source** | manual; profile-derived defaults |
| **MVP / Later** | MVP |
| **WP storage candidate** | CPT `iseo_project` + post meta; or custom table with `client_id` FK |
| **Security** | Project-scoped access: specialists see only assigned projects |

### 4.3 Project Profile

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Define project type (service, e-commerce, local, B2B, content-heavy, technical-heavy, custom) and default block set |
| **Key fields** | `profile_slug`, `label`, `description`, `default_block_ids[]`, `optional_block_ids[]`, `metric_schema_ref` (optional), `dictionary_filter_rules` |
| **Relationships** | One profile → many Projects; informs Block Definitions and Dictionary applicability |
| **Data source** | template; admin-managed |
| **MVP / Later** | MVP — predefined profiles + custom flag |
| **WP storage candidate** | Taxonomy `iseo_project_profile` on project CPT; or options/settings array; or custom table |
| **Security** | Admin manages; specialists read-only |

### 4.4 Reporting Cycle

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Container for one month (YYYY-MM) of reporting on one project |
| **Key fields** | `cycle_id`, `project_id`, `month` (YYYY-MM), `owner_user_id`, `reviewer_user_id`, `status`, `week1_checkpoint_id`, `week2_checkpoint_id`, `week3_checkpoint_id`, `monthly_final_id`, `published_version_id`, `due_dates` (optional), `created_at`, `closed_at` |
| **Relationships** | Belongs to Project; contains 3 Weekly Checkpoints + 1 Monthly Final; may link Published Version |
| **Data source** | system (auto-create on month open); manual status transitions |
| **MVP / Later** | MVP |
| **WP storage candidate** | CPT `iseo_reporting_cycle` + meta; or custom table `iseo_cycles` |
| **Security** | Visible to assigned specialist, reviewer, admin |

### 4.5 Weekly Checkpoint

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Short operational week 1–3 status — not a full monthly report |
| **Key fields** | `checkpoint_id`, `cycle_id`, `week_number` (1|2|3), `status`, `summary`, `completed_work_ids[]`, `metric_notes`, `blockers`, `next_week_plan`, `readiness_toward_month_close`, `internal_notes`, `client_visible_flag`, `submitted_at`, `approved_at` |
| **Relationships** | Belongs to Reporting Cycle; has Block Instances, Completed Work Items, Evidence, Comments, Review records |
| **Data source** | manual; work_dictionary selections; template partials |
| **MVP / Later** | MVP |
| **WP storage candidate** | CPT child of cycle or custom table `iseo_weekly_checkpoints` |
| **Security** | `internal_notes` never client-visible; draft not client-visible |

### 4.6 Monthly Final Report

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Comprehensive month-close report after interpretation layer |
| **Key fields** | `monthly_report_id`, `cycle_id`, `status`, `executive_summary`, `specialist_interpretation`, `risks_blockers`, `next_month_plan`, `rollup_completed_work_ids[]`, `submitted_at`, `approved_at`, `client_ready_at`, `published_at` |
| **Relationships** | Belongs to Cycle; has many Block Instances; links Review, Published Version, External Links |
| **Data source** | manual; template; dictionary; weekly rollup hints (not auto-copy without edit) |
| **MVP / Later** | MVP |
| **WP storage candidate** | CPT `iseo_monthly_report` or custom table; block instances likely separate table |
| **Security** | Approval required before publish; internal notes excluded from published version |

### 4.7 Report Block Definition

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Reusable block type in library (executive summary, traffic, Topvisor link, etc.) |
| **Key fields** | `block_def_id`, `slug`, `label`, `block_type` (text|metric_cards|chart|table|work_list|evidence|external_link|gallery|status|appendix), `required_for` (weekly|monthly|both), `profile_applicability[]`, `field_schema` (JSON-like descriptor), `sort_default`, `active` |
| **Relationships** | Instantiated as Report Block Instances; related to Work Dictionary via `report_block_relation` |
| **Data source** | template; admin-managed |
| **MVP / Later** | MVP — core block set |
| **WP storage candidate** | CPT `iseo_block_def` or options/library table |
| **Security** | Admin edits; specialists consume |

### 4.8 Report Block Instance

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Populated block within a specific weekly or monthly report |
| **Key fields** | `instance_id`, `parent_type` (weekly|monthly), `parent_id`, `block_def_id`, `sort_order`, `title_override`, `content_json` (structured field values), `visibility` (client|internal), `completion_state` |
| **Relationships** | Belongs to Weekly Checkpoint or Monthly Final; may contain Metric Snapshots, Evidence refs |
| **Data source** | manual; template-derived; later API; later AI draft |
| **MVP / Later** | MVP |
| **WP storage candidate** | Custom table `iseo_block_instances` (likely — repeatable, query-heavy) |
| **Security** | Respect parent report access; internal visibility blocks excluded from publish renderer |

### 4.9 Work Dictionary Item

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Canonical catalog of SEO works for standardized reporting |
| **Key fields** | `work_item_id`, `canonical_name`, `client_facing_wording`, `internal_notes`, `profile_applicability[]`, `recurrence`, `evidence_required`, `report_block_relation`, `active`, `sort_order` |
| **Relationships** | Selected into Completed Work Items |
| **Data source** | dictionary (sanitized from Nikita materials); admin-maintained |
| **MVP / Later** | MVP — requires sanitized extraction gate |
| **WP storage candidate** | CPT `iseo_work_item` or custom table `iseo_work_dictionary` |
| **Security** | No credential rows; admin curates |

### 4.10 Completed Work Item

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Record of work done in a week or rolled into month |
| **Key fields** | `completed_work_id`, `work_item_id`, `parent_type` (weekly|monthly), `parent_id`, `quantity` (optional), `custom_note`, `evidence_ids[]`, `week_attribution` (for monthly rollup) |
| **Relationships** | Links Work Dictionary Item to Checkpoint or Monthly report; links Evidence |
| **Data source** | work_dictionary selection + manual notes |
| **MVP / Later** | MVP |
| **WP storage candidate** | Custom table `iseo_completed_works` |
| **Security** | Client sees client_facing_wording only; internal_notes from dictionary not shown if marked internal |

### 4.11 Metric Snapshot

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Store metric name, value, period, and optional delta for charts/cards |
| **Key fields** | `metric_id`, `parent_block_instance_id` or `parent_report_id`, `metric_key`, `label`, `value`, `unit`, `period_start`, `period_end`, `comparison_value` (optional), `source` (manual|import|calculated), `entered_by_user_id`, `entered_at` |
| **Relationships** | Attached to Block Instance or report section |
| **Data source** | manual (MVP); later_api |
| **MVP / Later** | MVP manual; import later |
| **WP storage candidate** | Custom table `iseo_metric_snapshots` |
| **Security** | No API keys in snapshot rows |

### 4.12 Chart Definition

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Define chart type and binding to metric keys for rendering |
| **Key fields** | `chart_def_id`, `block_def_id`, `chart_type` (line|bar|donut|table_fallback), `metric_keys[]`, `config_json` |
| **Relationships** | Used by Block Instances of type `chart` |
| **Data source** | template; manual config |
| **MVP / Later** | MVP — simple chart types; exact library **SAFE UNKNOWN** |
| **WP storage candidate** | Part of block definition schema or separate table |
| **Security** | N/A |

### 4.13 Evidence Asset

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Proof material: URLs, screenshots, documents |
| **Key fields** | `evidence_id`, `parent_type`, `parent_id`, `evidence_type` (url|image|document), `title`, `url_or_attachment_id`, `caption`, `sort_order`, `client_visible` |
| **Relationships** | Attached to checkpoint, monthly report, completed work, or block instance |
| **Data source** | manual; screenshot; external_link |
| **MVP / Later** | MVP |
| **WP storage candidate** | Custom table + WP Media Library for files (`attachment_id`) |
| **Security** | Files in media library with access tied to report permissions; no secrets in filenames/captions |

### 4.14 External Report Link

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Link to Topvisor or other online report (MVP primary external pattern) |
| **Key fields** | `link_id`, `parent_report_id`, `provider` (topvisor|other), `url`, `label`, `preview_attachment_id` (optional screenshot), `export_attachment_id` (optional), `notes` |
| **Relationships** | Belongs to Monthly Final (or weekly if policy allows) |
| **Data source** | external_link; screenshot optional |
| **MVP / Later** | MVP |
| **WP storage candidate** | Custom table or meta on monthly report |
| **Security** | URL only — no Topvisor credentials stored here |

### 4.15 Comment / Specialist Note

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Free-text commentary with visibility control |
| **Key fields** | `comment_id`, `parent_type`, `parent_id`, `author_user_id`, `body`, `visibility` (internal|client|reviewer), `created_at` |
| **Relationships** | Attached to checkpoint, monthly, block, or review thread |
| **Data source** | manual; later ai_draft (flagged, editable) |
| **MVP / Later** | MVP manual |
| **WP storage candidate** | Custom table `iseo_comments` or WP comments pattern (likely custom for visibility) |
| **Security** | Strict visibility enforcement on publish |

### 4.16 Review / Approval

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Record reviewer decision and revision requests |
| **Key fields** | `review_id`, `target_type` (weekly|monthly), `target_id`, `reviewer_user_id`, `decision` (pending|approved|rejected|revision_requested), `reviewer_comment`, `decided_at`, `revision_round` |
| **Relationships** | One active review per submission round; links to target report |
| **Data source** | system + manual reviewer input |
| **MVP / Later** | MVP |
| **WP storage candidate** | Custom table `iseo_reviews` |
| **Security** | Reviewer and admin only for internal review comments |

### 4.17 Published Report Version

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Immutable snapshot used by client web renderer |
| **Key fields** | `version_id`, `monthly_report_id` (primary), `weekly_checkpoint_id` (if weekly published), `version_number`, `snapshot_json` or `rendered_html_ref`, `public_token` (optional), `public_path_slug`, `published_at`, `published_by_user_id`, `revoked_at`, `expires_at` (optional) |
| **Relationships** | Points to source monthly (or weekly); consumed by web renderer |
| **Data source** | system on publish action |
| **MVP / Later** | MVP for monthly; weekly publish policy **SAFE UNKNOWN** |
| **WP storage candidate** | Custom table `iseo_published_versions` + optional CPT for URL routing |
| **Security** | Token/slug design deferred; no draft content |

### 4.18 Notification Event

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Durable event log for n8n and internal admin notifications |
| **Key fields** | `event_id`, `event_type` (checkpoint_due|monthly_due|submitted_for_review|approved|published|revision_requested|field_missing), `entity_type`, `entity_id`, `payload_json`, `created_at`, `processed_by_n8n_at` (optional) |
| **Relationships** | References any entity |
| **Data source** | system |
| **MVP / Later** | MVP — define events; wire n8n later |
| **WP storage candidate** | Custom table `iseo_notification_events` |
| **Security** | Payload must not contain secrets |

### 4.19 Integration Reference

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Non-secret metadata about external integrations per project |
| **Key fields** | `integration_id`, `project_id`, `provider` (topvisor|metrika|gsc|ga4|crm), `external_account_ref` (opaque id, not password), `status`, `last_sync_at` |
| **Relationships** | Belongs to Project |
| **Data source** | manual (MVP); later API |
| **MVP / Later** | Later for live sync; MVP may omit or stub |
| **WP storage candidate** | Custom table; credentials in **separate secure store** — **SAFE UNKNOWN** |
| **Security** | **Never** store API keys/passwords in this entity |

### 4.20 User / Role Assignment

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Map WP users to Report Hub roles and project scope |
| **Key fields** | `assignment_id`, `user_id`, `role` (admin|reviewer|specialist|account_manager), `project_id` (null = global for admin/reviewer scope), `active`, `assigned_at` |
| **Relationships** | Links WP User to SEO Project |
| **Data source** | system; admin manual |
| **MVP / Later** | MVP |
| **WP storage candidate** | User meta + custom table for project assignments; WP roles/caps |
| **Security** | Foundation of project-scoped access |

---

## 5. Suggested WordPress Storage Strategy

### 5.1 Options compared

| Approach | Pros | Cons |
|----------|------|------|
| **CPT + post meta only** | Native WP UI patterns, revisions API, familiar to Anton | Meta sprawl for metrics/blocks; query performance for dashboards |
| **Custom tables only** | Clean relational model, efficient reporting queries | More custom admin UI; less native WP integration |
| **Hybrid** | CPTs for navigable objects; tables for dense/repeatable data | Two layers to maintain; migration discipline needed |

### 5.2 Product-level recommendation

**Hybrid (likely)** — aligned with WordPress Product Architecture v0.1:

| Data class | Likely storage |
|------------|----------------|
| Client, SEO Project, Reporting Cycle, Monthly Final | CPTs (admin list screens, permalinks for internal refs) |
| Weekly Checkpoint | CPT or custom table (if child of cycle CPT) |
| Block instances, metrics, completed works, reviews, events | **Custom tables** |
| Project Profile | Taxonomy on Project CPT and/or settings |
| Work Dictionary | CPT or dedicated table (dictionary may be large — table preferable if >100 items) |
| Block Definitions | Options or CPT library |
| Evidence files | WP Media + evidence metadata table |
| Published versions | Custom table + front-end route handler |
| User assignments | Custom table + WP capabilities |
| Integration credentials | **Outside report schema** — secure integration layer |

**Do not implement** until operator approves storage gate in implementation charter.

---

## 6. Relationships

```
Client
  └── SEO Project (many)
        ├── Project Profile (one primary)
        ├── User / Role Assignment (many)
        ├── Integration Reference (zero or more; later)
        └── Reporting Cycle (many, one per month)
              ├── Weekly Checkpoint × 3 (week 1, 2, 3)
              │     ├── Completed Work Item (many)
              │     ├── Report Block Instance (many)
              │     ├── Evidence Asset (many)
              │     ├── Comment (many)
              │     └── Review / Approval (zero or one active round)
              ├── Monthly Final Report (one)
              │     ├── Report Block Instance (many)
              │     ├── Completed Work Item (rollup, many)
              │     ├── Metric Snapshot (many, via blocks)
              │     ├── External Report Link (zero or more)
              │     ├── Evidence Asset (many)
              │     ├── Comment (many)
              │     └── Review / Approval
              └── Published Report Version (zero or one active monthly)
                    └── (renders client web page)

Work Dictionary Item
  └── Completed Work Item (many, across reports)

Report Block Definition
  └── Report Block Instance (many)

Notification Event ──► (references any entity; consumed by n8n later)
```

---

## 7. Status Fields

### 7.1 Reporting Cycle

| Status | Meaning |
|--------|---------|
| `planned` | Month not yet started |
| `active` | Weeklies/monthly in progress |
| `month_close` | Monthly final in progress |
| `in_review` | Monthly submitted for review |
| `approved` | Monthly approved internally |
| `published` | Client-visible version exists |
| `archived` | Historical closed cycle |

### 7.2 Weekly Checkpoint

| Status | Meaning |
|--------|---------|
| `draft` | Not started or incomplete |
| `in_progress` | Specialist editing |
| `submitted` | Awaiting review (if review enabled for weekly) |
| `revision` | Returned for corrections |
| `approved` | Reviewer approved |
| `skipped` | Operator policy: week skipped (exception) |

### 7.3 Monthly Final Report

| Status | Meaning |
|--------|---------|
| `draft` | Initial / incomplete |
| `data_collection` | Gathering metrics and evidence |
| `specialist_input` | Active editing |
| `submitted` | Submitted for review |
| `revision` | Returned to specialist |
| `approved` | Reviewer approved |
| `client_ready` | Cleared for publish renderer |
| `published` | Published version exists |
| `archived` | Historical |

### 7.4 Review / Approval

| Decision | Meaning |
|----------|---------|
| `pending` | Awaiting reviewer |
| `approved` | Accepted |
| `revision_requested` | Must fix and resubmit |
| `rejected` | Blocked (rare; admin escalation) |

### 7.5 Published Version

| Status | Meaning |
|--------|---------|
| `active` | Current client-visible version |
| `superseded` | Replaced by newer publish |
| `revoked` | Link disabled / access removed |

Exact transition rules and role permissions: **SAFE UNKNOWN** — admin UX flow doc defines intended flows; implementation charter locks transitions.

---

## 8. Security / Access

| Rule | Requirement |
|------|-------------|
| **Project-scoped access** | SEO Specialist sees only assigned projects |
| **Reviewer scope** | All projects or team-scoped — operator decision |
| **Admin** | Full visibility and configuration |
| **No secrets in report data** | Passwords, API keys, credential sheets excluded |
| **Integration credentials separate** | Topvisor/Metrika keys not in report tables |
| **Private report links** | Published versions use controlled URL/token — design deferred |
| **Internal vs client visibility** | Fields flagged `internal` never in published snapshot |
| **AI drafts** | Marked as draft; never auto-published |

---

## 9. MVP vs Later

### MVP entities and fields

- Client, SEO Project, Project Profile (predefined set)
- Reporting Cycle, Weekly Checkpoint ×3, Monthly Final Report
- Work Dictionary (sanitized), Completed Work Items
- Report Block Definition (core set), Block Instances
- Manual Metric Snapshots
- Evidence (URL + image), External Report Link (Topvisor URL + optional screenshot)
- Comments (manual), Review/Approval, Published Report Version (monthly)
- Notification Event definitions (log only)
- User/Role Assignment

### Later

- Integration Reference with live API sync
- Chart Definition advanced types
- AI-drafted comments/blocks with approval workflow
- Weekly client-visible publish (if policy enables)
- PDF export snapshot
- ATLAS identity consumer
- iframe Topvisor embed
- Client portal authentication
- Automated metric import

---

## 10. SAFE UNKNOWN

| Topic | Notes |
|-------|-------|
| Final CPT vs custom table per entity | Requires hosting review and Anton technical spike |
| Plugin vs mu-plugin packaging on i-seo.su | Hosting constraints unknown |
| ACF or custom field UI framework | Product decision deferred |
| Immutable snapshot: JSON blob vs normalized copy | Versioning strategy |
| Weekly checkpoint review required or optional | Operator policy |
| Multi-specialist same project same month | Handoff rules |
| File retention and upload limits | Hosting policy |
| Published URL token format and expiry | Security gate |
| Webhook auth for n8n | Implementation gate |
| Exact metric catalog per profile | Work dictionary + profile gate |

---

## Document control

- **Does not claim:** any WordPress plugin, schema, or API exists
- **Upstream:** [I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md](I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md), [I-SEO-REPORT-HUB-WORDPRESS-PRODUCT-ARCHITECTURE-v0.1.md](I-SEO-REPORT-HUB-WORDPRESS-PRODUCT-ARCHITECTURE-v0.1.md)
- **Next gate:** Operator review → implementation specification or Website Factory prototype charter
