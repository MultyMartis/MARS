# I-SEO Report Hub — Data Model v0.1

**Status:** PLANNING — conceptual data model (Layer 02)  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Implementation:** **NOT STARTED** — no SQL migrations, no schema deploy

---

## 1. Status

This is a **conceptual** database / data model for product design. It is **platform-neutral** (WordPress CPT/meta, custom MySQL tables, or hybrid).

Related earlier artifact: [I-SEO-REPORT-HUB-WORDPRESS-DATA-MODEL-v0.1.md](I-SEO-REPORT-HUB-WORDPRESS-DATA-MODEL-v0.1.md) remains valid as **Option A** storage sketch. This document is the broader product entity set for Layer 02.

**Forbidden in this task:** SQL migrations, DDL, seed data, runtime claims.

---

## 2. Design Principles

1. Draft entities and published snapshots are **separate**.
2. No secrets/credentials in report or integration tables.
3. Source systems referenced by **metadata pointers**, not embedded API keys.
4. Internal vs client-visible fields flagged at block/evidence level.
5. Soft-delete / archive preferred over hard-delete for published history.

---

## 3. Entity Catalog

### users

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Human actors in the system |
| **Key fields** | `user_id`, `display_name`, `email`, `status`, `created_at`, `updated_at` |
| **Relations** | many-to-many → roles; assigned to projects |
| **MVP required** | Yes |
| **Notes** | Auth provider TBD (WP users vs app users) |

### roles

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Named permission sets |
| **Key fields** | `role_id`, `slug`, `label`, `permissions_json` or capability flags |
| **Relations** | users ↔ roles |
| **MVP required** | Yes |
| **Notes** | See Role and Permission Model |

### clients

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Business customer |
| **Key fields** | `client_id`, `display_name`, `legal_name?`, `status`, `primary_contact_text?`, `internal_notes`, timestamps |
| **Relations** | 1 → many projects |
| **MVP required** | Yes |
| **Notes** | No credentials |

### projects

| Attribute | Detail |
|-----------|--------|
| **Purpose** | SEO engagement unit; access scope |
| **Key fields** | `project_id`, `client_id`, `name`, `status`, `assigned_specialist_id`, `assigned_reviewer_id?`, `project_type_profile_id`, `reporting_start_month`, `internal_notes` |
| **Relations** | client; profile; sites; periods; users |
| **MVP required** | Yes |
| **Notes** | Specialist sees assigned only |

### sites

| Attribute | Detail |
|-----------|--------|
| **Purpose** | URL / site under a project |
| **Key fields** | `site_id`, `project_id`, `url`, `label?`, `is_primary`, `status` |
| **Relations** | belongs to project |
| **MVP required** | Yes (at least one primary site per project) |
| **Notes** | MVP often 1:1 project↔site |

### project_type_profiles

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Type-driven block matrix defaults |
| **Key fields** | `profile_id`, `slug`, `label`, `default_block_template_ids[]`, rules |
| **Relations** | projects; block_templates |
| **MVP required** | Yes |
| **Notes** | Aligns with Block Matrix v0.1 |

### reporting_periods

| Attribute | Detail |
|-----------|--------|
| **Purpose** | One calendar month cycle per project |
| **Key fields** | `period_id`, `project_id`, `year_month`, `lifecycle_state`, `owner_specialist_id`, timestamps |
| **Relations** | weekly_checkpoints; monthly_reports |
| **MVP required** | Yes |
| **Notes** | Lifecycle states in Report Lifecycle doc |

### weekly_checkpoints

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Week 1–3 preliminary reports |
| **Key fields** | `checkpoint_id`, `period_id`, `week_number` (1–3), `state`, `submitted_at?`, `reviewed_at?` |
| **Relations** | report_blocks; evidence; comments |
| **MVP required** | Yes |
| **Notes** | Internal by default for client delivery |

### monthly_reports

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Month-close comprehensive report |
| **Key fields** | `monthly_report_id`, `period_id`, `state`, `submitted_at?`, `approved_at?`, `published_at?` |
| **Relations** | blocks; kpi_values; published_snapshots; revisions |
| **MVP required** | Yes |
| **Notes** | Primary client deliverable after publish |

### report_blocks

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Block instance in weekly or monthly report |
| **Key fields** | `block_id`, `parent_type`, `parent_id`, `block_template_id`, `title`, `visibility`, `state`, `sort_order` |
| **Relations** | report_block_values; evidence_links |
| **MVP required** | Yes |
| **Notes** | States in lifecycle doc |

### report_block_values

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Structured field values inside a block |
| **Key fields** | `value_id`, `block_id`, `field_key`, `field_type`, `value_text` / `value_json`, `is_client_visible` |
| **Relations** | report_blocks |
| **MVP required** | Yes |
| **Notes** | Schema flexible by template |

### work_items

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Completed/planned work instance |
| **Key fields** | `work_item_id`, `period_id` or report parent, `dictionary_item_id?`, `category_id`, `description`, `purpose`, `status`, `client_visible` |
| **Relations** | work_item_categories; evidence; dictionary |
| **MVP required** | Yes |
| **Notes** | Dictionary-backed preferred |

### work_item_categories

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Taxonomy for works (technical, semantic, etc.) |
| **Key fields** | `category_id`, `slug`, `label`, `sort_order` |
| **Relations** | work_items; dictionary |
| **MVP required** | Yes |
| **Notes** | Align with work dictionary |

### kpi_definitions

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Catalog of metric types |
| **Key fields** | `kpi_def_id`, `slug`, `label`, `unit`, `profile_applicability` |
| **Relations** | kpi_values |
| **MVP required** | Yes (small seed set) |
| **Notes** | Manual entry first |

### kpi_values

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Metric snapshot values for a period/report |
| **Key fields** | `kpi_value_id`, `kpi_def_id`, `period_id` / report parent, `value`, `delta?`, `period_label`, `source_ref`, `interpretation?`, `client_visible` |
| **Relations** | kpi_definitions; evidence optional |
| **MVP required** | Yes |
| **Notes** | No live API required |

### evidence_items

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Logical evidence object (claim support) |
| **Key fields** | `evidence_id`, `title`, `kind` (link/file/screenshot/ref), `moderation_state`, `client_visible`, `created_by` |
| **Relations** | evidence_links; evidence_files; work_items; blocks |
| **MVP required** | Yes |
| **Notes** | Client snapshot excludes non-approved |

### evidence_links

| Attribute | Detail |
|-----------|--------|
| **Purpose** | URL evidence (Topvisor, GSC export page, task URL) |
| **Key fields** | `link_id`, `evidence_id`, `url`, `label`, `source_system?` |
| **Relations** | evidence_items |
| **MVP required** | Yes |
| **Notes** | External Topvisor link is MVP pattern |

### evidence_files

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Uploaded screenshots/files metadata |
| **Key fields** | `file_id`, `evidence_id`, `storage_key`, `filename`, `mime`, `size`, `checksum?` |
| **Relations** | evidence_items |
| **MVP required** | Yes (or link-only MVP-lite) |
| **Notes** | Binary storage strategy TBD — see §6 |

### reviewer_comments

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Review feedback and internal discussion |
| **Key fields** | `comment_id`, `target_type`, `target_id`, `author_id`, `body`, `visibility` (internal/reviewer), `created_at` |
| **Relations** | reports / blocks / periods |
| **MVP required** | Yes |
| **Notes** | Excluded from client snapshot |

### report_revisions

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Edit history / revision requests trail |
| **Key fields** | `revision_id`, `monthly_report_id` or checkpoint_id, `from_state`, `to_state`, `actor_id`, `note`, `created_at` |
| **Relations** | monthly_reports; weekly_checkpoints |
| **MVP required** | Yes (lightweight) |
| **Notes** | Complements audit log |

### published_snapshots

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Immutable (or soft-immutable) client-facing render payload |
| **Key fields** | `snapshot_id`, `monthly_report_id`, `version_number`, `access_token`, `status` (live/superseded/revoked), `payload_json` or structured tables, `published_at`, `published_by` |
| **Relations** | monthly_reports |
| **MVP required** | Yes |
| **Notes** | See Publishing and Snapshot Model |

### template_profiles

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Named template binding (may alias project_type_profiles) |
| **Key fields** | `template_profile_id`, `slug`, `label`, `version` |
| **Relations** | block_templates |
| **MVP required** | Yes (can merge with project_type_profiles in MVP schema) |
| **Notes** | Avoid duplication if one table suffices |

### block_templates

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Reusable block definitions and field schemas |
| **Key fields** | `block_template_id`, `slug`, `title`, `default_visibility`, `field_schema_json`, `required_flag` |
| **Relations** | template_profiles; report_blocks |
| **MVP required** | Yes |
| **Notes** | Driven by Block Matrix |

### notifications

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Outbound event records for reminders/delivery hooks |
| **Key fields** | `notification_id`, `event_type`, `payload_ref`, `status`, `scheduled_at?`, `sent_at?` |
| **Relations** | periods/reports/users |
| **MVP required** | Partial — **event model yes; live delivery no** |
| **Notes** | n8n consumes later; not SoT |

### imports

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Import job / source sync records (future) |
| **Key fields** | `import_id`, `source_system`, `project_id`, `status`, `started_at`, `finished_at`, `error_summary?`, `source_ref` (no secrets) |
| **Relations** | projects; kpi_values optional |
| **MVP required** | No |
| **Notes** | Post-MVP Topvisor/API |

---

## 4. Simplified MVP Schema Subset

**Must have for MVP:**

- users, roles  
- clients, projects, sites  
- project_type_profiles (or template_profiles)  
- reporting_periods  
- weekly_checkpoints, monthly_reports  
- report_blocks, report_block_values  
- work_item_categories, work_items  
- kpi_definitions, kpi_values  
- evidence_items, evidence_links (± evidence_files)  
- reviewer_comments, report_revisions  
- published_snapshots  
- block_templates  

**MVP-lite acceptable:**

- notifications as stub event types only  
- template_profiles merged into project_type_profiles  

---

## 5. Future Expansion Entities

| Entity / area | When |
|---------------|------|
| imports (full) | Phase 2 API |
| chart_definitions | Richer renderer |
| client_accounts / portal sessions | If portal needed |
| ATLAS identity sync tables | Optional consumer |
| billing / CRM entities | Never as Report Hub core |
| AI draft artifacts | Phase 3, draft-only |

---

## 6. File Storage Considerations

| Option | Notes |
|--------|-------|
| App-managed disk / volume | Simple; backup discipline required |
| Object storage | Better for growth; ops complexity |
| WordPress media library | Natural for Option A; coupling risk |

Store **metadata in DB**; binaries outside report content tables. Virus scan / size limits: **SAFE UNKNOWN**.

---

## 7. No Secrets in DB

Do **not** store:

- API keys, passwords, FTP, CMS admin credentials  
- Nikita credential-sheet style material  
- Client private access dumps inside report fields  

Integration credentials belong in a **separate secure vault / env** — out of report schema.

---

## 8. Source Data References

Prefer:

- `source_system` + `external_url` + `captured_at`  
- Manual values with “source: specialist entry”  

Avoid treating Topvisor/Metrika live payloads as SoT inside Report Hub until import phase.

---

## 9. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Final physical schema (WP vs MySQL tables) | **UNKNOWN** |
| Whether sites are separate from projects day one | Soft — recommended yes |
| JSON payload vs normalized snapshot tables | **UNKNOWN** |
| File size limits and retention | **UNKNOWN** |
| Soft-delete vs hard-delete policy | Prefer soft; not finalized |

---

## Document control

- **Created:** 2026-07-24  
- **Does not claim:** any database or migrations exist  
- **No SQL** in this document
