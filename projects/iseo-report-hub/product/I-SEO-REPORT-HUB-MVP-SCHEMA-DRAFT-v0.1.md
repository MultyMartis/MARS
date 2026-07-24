# I-SEO Report Hub — MVP Schema Draft v0.1

**Status:** CONCEPTUAL SCHEMA — not a SQL migration  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Implementation:** **NOT STARTED** — no DDL, no migrations executed

**Basis:** [Data Model v0.1](I-SEO-REPORT-HUB-DATA-MODEL-v0.1.md), [Platform Decision](I-SEO-REPORT-HUB-PLATFORM-DECISION-v0.1.md)

---

## 1. Status

This document is a **conceptual MySQL/MariaDB-oriented schema draft** for the custom PHP MVP.

| Allowed | Forbidden (this task) |
|---------|------------------------|
| Table purpose, columns, indexes, relations | SQL CREATE/ALTER |
| JSON field caution notes | Seed inserts |
| Snapshot storage strategy | Live DB changes |

---

## 2. Cross-cutting conventions

| Convention | Draft rule |
|------------|------------|
| Primary keys | `BIGINT UNSIGNED` surrogate `id` (or typed `*_id`) |
| Timestamps | `created_at`, `updated_at` on mutable entities |
| Actors | `created_by`, `updated_by` (FK → users) where meaningful |
| Soft delete / archive | Prefer `status` / `archived_at` / `deleted_at` over hard delete for published history |
| JSON fields | Allowed for flexible templates/payloads; **caution:** do not put query-critical filters only inside JSON when indexed columns are needed |
| Secrets | Never store credentials/API keys in report or evidence tables |

---

## 3. Tables

### users

| Aspect | Detail |
|--------|--------|
| **Purpose** | Application users |
| **Key columns** | `id`, `email` (unique), `password_hash`, `display_name`, `status`, `created_at`, `updated_at` |
| **Important indexes** | unique(`email`); (`status`) |
| **Relationships** | M:N → roles via `user_roles`; assigned to projects |
| **MVP** | Yes |

### roles

| Aspect | Detail |
|--------|--------|
| **Purpose** | Named roles (admin, lead, specialist, account_manager, …) |
| **Key columns** | `id`, `slug` (unique), `label`, `permissions_json` (optional capability map) |
| **Important indexes** | unique(`slug`) |
| **Relationships** | M:N → users |
| **MVP** | Yes |

### user_roles

| Aspect | Detail |
|--------|--------|
| **Purpose** | User ↔ role assignment |
| **Key columns** | `user_id`, `role_id`, `created_at` |
| **Important indexes** | unique(`user_id`,`role_id`); (`role_id`) |
| **Relationships** | users, roles |
| **MVP** | Yes |

### clients

| Aspect | Detail |
|--------|--------|
| **Purpose** | Business customers |
| **Key columns** | `id`, `display_name`, `legal_name` (nullable), `status`, `primary_contact_text`, `internal_notes`, timestamps, `created_by` |
| **Important indexes** | (`status`); (`display_name`) |
| **Relationships** | 1 → N projects |
| **MVP** | Yes |

### projects

| Aspect | Detail |
|--------|--------|
| **Purpose** | SEO engagement; access scope unit |
| **Key columns** | `id`, `client_id`, `name`, `status`, `assigned_specialist_id`, `assigned_reviewer_id` (nullable), `project_type_profile_id`, `reporting_start_month`, `internal_notes`, timestamps |
| **Important indexes** | (`client_id`); (`assigned_specialist_id`); (`status`); (`project_type_profile_id`) |
| **Relationships** | client; profile; sites; periods |
| **MVP** | Yes |

### sites

| Aspect | Detail |
|--------|--------|
| **Purpose** | Site URL under a project |
| **Key columns** | `id`, `project_id`, `url`, `label`, `is_primary`, `status`, timestamps |
| **Important indexes** | (`project_id`); unique optional (`project_id`,`url`) |
| **Relationships** | belongs to project |
| **MVP** | Yes |

### project_type_profiles

| Aspect | Detail |
|--------|--------|
| **Purpose** | Type-driven default block matrix |
| **Key columns** | `id`, `slug` (unique), `label`, `default_rules_json`, `status`, timestamps |
| **Important indexes** | unique(`slug`) |
| **Relationships** | projects; informs block templates |
| **MVP** | Yes |

### reporting_periods

| Aspect | Detail |
|--------|--------|
| **Purpose** | One calendar month cycle per project |
| **Key columns** | `id`, `project_id`, `year_month` (e.g. `2026-07`), `lifecycle_state`, `owner_specialist_id`, timestamps, `created_by` |
| **Important indexes** | unique(`project_id`,`year_month`); (`lifecycle_state`); (`owner_specialist_id`) |
| **Relationships** | weekly_checkpoints; monthly_reports; work_items; kpi_values |
| **MVP** | Yes |

### weekly_checkpoints

| Aspect | Detail |
|--------|--------|
| **Purpose** | Week 1–3 preliminary reports |
| **Key columns** | `id`, `period_id`, `week_number` (1–3), `state`, `submitted_at`, `reviewed_at`, timestamps |
| **Important indexes** | unique(`period_id`,`week_number`); (`state`) |
| **Relationships** | period; report_blocks; comments |
| **MVP** | Yes |

### monthly_reports

| Aspect | Detail |
|--------|--------|
| **Purpose** | Month-close comprehensive report |
| **Key columns** | `id`, `period_id` (unique), `state`, `submitted_at`, `approved_at`, `published_at`, timestamps |
| **Important indexes** | unique(`period_id`); (`state`) |
| **Relationships** | period; blocks; snapshots; comments |
| **MVP** | Yes |

### report_blocks

| Aspect | Detail |
|--------|--------|
| **Purpose** | Block instance on weekly or monthly parent |
| **Key columns** | `id`, `parent_type`, `parent_id`, `block_template_key`, `title`, `visibility`, `state`, `sort_order`, timestamps |
| **Important indexes** | (`parent_type`,`parent_id`); (`state`) |
| **Relationships** | report_block_values; evidence links |
| **MVP** | Yes |

### report_block_values

| Aspect | Detail |
|--------|--------|
| **Purpose** | Field values inside a block |
| **Key columns** | `id`, `block_id`, `field_key`, `field_type`, `value_text`, `value_json` (nullable), `is_client_visible`, timestamps |
| **Important indexes** | unique(`block_id`,`field_key`) |
| **Relationships** | report_blocks |
| **MVP** | Yes |
| **JSON caution** | Use `value_json` for structured fields; keep `field_key` queryable |

### work_item_categories

| Aspect | Detail |
|--------|--------|
| **Purpose** | Work taxonomy |
| **Key columns** | `id`, `slug` (unique), `label`, `sort_order` |
| **Important indexes** | unique(`slug`) |
| **Relationships** | work_items |
| **MVP** | Yes |

### work_items

| Aspect | Detail |
|--------|--------|
| **Purpose** | Completed/planned work instance |
| **Key columns** | `id`, `period_id`, `category_id`, `dictionary_key` (nullable), `description`, `purpose`, `status`, `client_visible`, timestamps, `created_by` |
| **Important indexes** | (`period_id`); (`category_id`); (`client_visible`) |
| **Relationships** | period; category; evidence |
| **MVP** | Yes |

### kpi_definitions

| Aspect | Detail |
|--------|--------|
| **Purpose** | Metric type catalog |
| **Key columns** | `id`, `slug` (unique), `label`, `unit`, `profile_applicability_json`, `status` |
| **Important indexes** | unique(`slug`) |
| **Relationships** | kpi_values |
| **MVP** | Yes (small seed) |

### kpi_values

| Aspect | Detail |
|--------|--------|
| **Purpose** | Metric values for a period/report |
| **Key columns** | `id`, `kpi_definition_id`, `period_id`, `value_numeric` / `value_text`, `delta`, `period_label`, `source_ref`, `interpretation`, `client_visible`, timestamps |
| **Important indexes** | (`period_id`); (`kpi_definition_id`) |
| **Relationships** | kpi_definitions; period |
| **MVP** | Yes |

### evidence_items

| Aspect | Detail |
|--------|--------|
| **Purpose** | Logical evidence object |
| **Key columns** | `id`, `title`, `kind` (link/file/screenshot/ref), `moderation_state`, `client_visible`, `created_by`, timestamps |
| **Important indexes** | (`moderation_state`); (`client_visible`) |
| **Relationships** | evidence_files; evidence_links; attachable to blocks/work_items |
| **MVP** | Yes |

### evidence_files

| Aspect | Detail |
|--------|--------|
| **Purpose** | Uploaded file metadata (binary outside DB or blob — prefer filesystem) |
| **Key columns** | `id`, `evidence_id`, `storage_key`, `original_filename`, `mime`, `size_bytes`, `checksum`, timestamps |
| **Important indexes** | (`evidence_id`); unique(`storage_key`) |
| **Relationships** | evidence_items |
| **MVP** | Yes (or link-only MVP-lite if chartered) |

### evidence_links

| Aspect | Detail |
|--------|--------|
| **Purpose** | URL evidence (Topvisor, etc.) |
| **Key columns** | `id`, `evidence_id`, `url`, `label`, `source_system`, timestamps |
| **Important indexes** | (`evidence_id`) |
| **Relationships** | evidence_items |
| **MVP** | Yes |

### reviewer_comments

| Aspect | Detail |
|--------|--------|
| **Purpose** | Review feedback; never in client snapshot |
| **Key columns** | `id`, `target_type`, `target_id`, `author_id`, `body`, `visibility`, `created_at` |
| **Important indexes** | (`target_type`,`target_id`); (`author_id`) |
| **Relationships** | users; reports/blocks/periods |
| **MVP** | Yes |

### published_snapshots

| Aspect | Detail |
|--------|--------|
| **Purpose** | Immutable (or soft-immutable) client-facing published report |
| **Key columns** | `id`, `monthly_report_id`, `version_number`, `access_token` (unique, high entropy), `status` (live/superseded/revoked), `payload_json` and/or normalized snapshot tables, `published_at`, `published_by` |
| **Important indexes** | unique(`access_token`); (`monthly_report_id`,`version_number`); (`status`) |
| **Relationships** | monthly_reports |
| **MVP** | Yes |

### audit_log

| Aspect | Detail |
|--------|--------|
| **Purpose** | Security/ops trail for sensitive actions |
| **Key columns** | `id`, `actor_id`, `action`, `entity_type`, `entity_id`, `meta_json`, `created_at`, `ip` (optional) |
| **Important indexes** | (`actor_id`); (`entity_type`,`entity_id`); (`action`); (`created_at`) |
| **Relationships** | users (actor) |
| **MVP** | Yes (at least publish/unpublish/approve) |

---

## 4. Likely JSON fields and caution

| Location | Use | Caution |
|----------|-----|---------|
| `roles.permissions_json` | Capability map | Prefer also code-level role checks |
| `project_type_profiles.default_rules_json` | Template defaults | Version carefully |
| `report_block_values.value_json` | Structured field payloads | Keep `field_key` indexed |
| `kpi_definitions.profile_applicability_json` | Which profiles use KPI | Optional |
| `published_snapshots.payload_json` | Frozen client render | Treat as immutable after publish; large payloads need size policy |
| `audit_log.meta_json` | Extra context | No secrets |

---

## 5. Snapshot storage strategy

**MVP recommendation (conceptual):**

1. On publish, build a **client-safe payload** (exclude internal notes, reviewer comments, non-client-visible fields).
2. Store as `published_snapshots` row with `payload_json` **and/or** normalized snapshot child tables if payload grows too large.
3. Client route resolves **only** by `access_token` → live snapshot.
4. Re-publish increments `version_number`; previous live row → `superseded`.
5. Revoke sets `status = revoked` without deleting history.

Draft tables remain editable; client never reads draft parents for delivery.

Exact binary vs JSON mix: **SAFE UNKNOWN** until Phase 8 charter.

---

## 6. Soft delete / archive strategy

| Entity class | Strategy |
|--------------|----------|
| Clients / projects | Soft status (`active` / `archived`) |
| Periods | Lifecycle includes `archived` |
| Snapshots | Never hard-delete published history in MVP |
| Evidence files | Soft-hide + retain storage until retention policy |
| Users | Deactivate (`status`) rather than delete |

Hard delete only for never-published draft junk — policy **SAFE UNKNOWN** (define in implementation).

---

## 7. Timestamps and actor fields

- Mutable business tables: `created_at`, `updated_at`
- Authorship: `created_by` / `updated_by` on clients, projects, periods, evidence, comments where useful
- Publish events: `published_at` / `published_by` on monthly_reports and snapshots
- Audit log: append-only `created_at`

---

## 8. Boundaries

- **No SQL** in this document as executable migration.
- Aligns with Layer 02 Data Model; WordPress CPT mapping is obsolete for MVP storage.
- Next: Phase 2 implementation charter produces real migrations under HITL.
