# I-SEO Report Hub — Initial Schema Plan v0.1

**Status:** SCHEMA PLANNING ONLY — no SQL files; no DB  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator I-SEO Report Hub DB Creation + Schema Migration Charter 01  
**Basis:** [I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md](I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md), `app-source/database/schema-draft-not-migration.md`  
**Related:** [I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md](I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md)

---

## 1. Status

| Fact | State |
|------|-------|
| Document type | Initial schema **plan** |
| SQL migration files | **None** |
| Database | **Not created** |
| Executable DDL | **Forbidden in this wave** |

This plan phases the conceptual MVP schema into applyable waves. Column-level detail remains authoritative in Schema Draft v0.1 until SQL is authored.

---

## 2. Schema Phasing

### Phase DB-01 — System + Auth Baseline

- `schema_migrations`
- `users`
- `roles`
- `user_roles`
- `audit_log`

### Phase DB-02 — Clients / Projects / Sites

- `clients`
- `projects`
- `sites`
- `project_type_profiles`

### Phase DB-03 — Reporting Periods + Weekly + Monthly

- `reporting_periods`
- `weekly_checkpoints`
- `monthly_reports`

### Phase DB-04 — Report Blocks + Work Items + KPI

- `report_blocks`
- `report_block_values`
- `work_item_categories`
- `work_items`
- `kpi_definitions`
- `kpi_values`

### Phase DB-05 — Evidence + Published Snapshots

- `evidence_items`
- `evidence_files`
- `evidence_links`
- `reviewer_comments`
- `published_snapshots`

---

## 3. Initial MVP Migration Recommendation

**Recommend first migration = DB-01 + minimal DB-02 only.**

Do **not** include all report tables (DB-03–DB-05) in the first migration unless a future charter justifies a single bootstrap dump for local demos.

### Suggested first migration tables

| Table | Phase |
|-------|-------|
| `schema_migrations` | DB-01 |
| `users` | DB-01 |
| `roles` | DB-01 |
| `user_roles` | DB-01 |
| `audit_log` | DB-01 |
| `clients` | DB-02 |
| `projects` | DB-02 |
| `sites` | DB-02 |
| `project_type_profiles` | DB-02 |

**Rationale:** Auth + org/project tree unblocks login persistence and client/project screens before weekly/monthly report storage. Report-domain tables add FK and JSON complexity better reviewed in a second migration after the ledger works.

**Alternative (not preferred):** DB-01 only first — smaller blast radius, but forces a near-immediate second migration before any project CRUD UI.

Example filename (illustrative only):

```text
2026_07_24_000001_create_core_tables.sql
```

---

## 4. Table Notes

Notes for **first migration** tables. Full column lists: Schema Draft v0.1.

### schema_migrations

| Aspect | Note |
|--------|------|
| **Purpose** | Ledger of applied migration files |
| **Key fields** | `id`, `migration`, `checksum`, `executed_at`, `batch` |
| **Indexes** | unique(`migration`) |
| **Relationship** | None (infra) |
| **Sensitive data** | None expected |

### users

| Aspect | Note |
|--------|------|
| **Purpose** | Application user accounts |
| **Key fields** | `id`, `email` (unique), `password_hash`, `display_name`, `status`, timestamps |
| **Indexes** | unique(`email`); (`status`) |
| **Relationship** | M:N roles via `user_roles`; referenced by projects/audit |
| **Sensitive data** | `password_hash` — never log plaintext; no real passwords in Git seeds |

### roles

| Aspect | Note |
|--------|------|
| **Purpose** | Named roles (admin, lead, specialist, account_manager, …) |
| **Key fields** | `id`, `slug` (unique), `label`, optional `permissions_json` |
| **Indexes** | unique(`slug`) |
| **Relationship** | M:N users |
| **Sensitive data** | Capability map is not a secret; keep small |

### user_roles

| Aspect | Note |
|--------|------|
| **Purpose** | User ↔ role assignment |
| **Key fields** | `user_id`, `role_id`, `created_at` |
| **Indexes** | unique(`user_id`,`role_id`); (`role_id`) |
| **Relationship** | FK → `users`, `roles` |
| **Sensitive data** | None beyond access control implications |

### audit_log

| Aspect | Note |
|--------|------|
| **Purpose** | Append-only trail for sensitive actions |
| **Key fields** | `id`, `actor_id`, `action`, `entity_type`, `entity_id`, `meta_json`, `created_at`, optional `ip` |
| **Indexes** | (`actor_id`); (`entity_type`,`entity_id`); (`action`); (`created_at`) |
| **Relationship** | actor → `users` |
| **Sensitive data** | `meta_json` must not store passwords/tokens |

### clients

| Aspect | Note |
|--------|------|
| **Purpose** | Business customers |
| **Key fields** | `id`, `display_name`, `legal_name`, `status`, contact/notes fields, timestamps, `created_by` |
| **Indexes** | (`status`); (`display_name`) |
| **Relationship** | 1 → N `projects` |
| **Sensitive data** | Contact/notes may be business-sensitive — no real client rows in Git |

### projects

| Aspect | Note |
|--------|------|
| **Purpose** | SEO engagement / access scope unit |
| **Key fields** | `id`, `client_id`, `name`, `status`, specialist/reviewer FKs, `project_type_profile_id`, timestamps |
| **Indexes** | (`client_id`); (`assigned_specialist_id`); (`status`); (`project_type_profile_id`) |
| **Relationship** | client; profile; sites; (later) periods |
| **Sensitive data** | Internal notes — local/demo only in early waves |

### sites

| Aspect | Note |
|--------|------|
| **Purpose** | Site URL under a project |
| **Key fields** | `id`, `project_id`, `url`, `label`, `is_primary`, `status`, timestamps |
| **Indexes** | (`project_id`); optional unique(`project_id`,`url`) |
| **Relationship** | belongs to `projects` |
| **Sensitive data** | URLs may identify clients — use demo hosts only in seeds |

### project_type_profiles

| Aspect | Note |
|--------|------|
| **Purpose** | Type-driven default block matrix |
| **Key fields** | `id`, `slug` (unique), `label`, `default_rules_json`, `status`, timestamps |
| **Indexes** | unique(`slug`) |
| **Relationship** | referenced by `projects` |
| **Sensitive data** | JSON templates — no credentials |

---

## 5. Seed Policy

| Rule | Statement |
|------|-----------|
| Real users | **No** real users in Git |
| Real passwords | **No** real passwords in Git |
| Demo seed | Optional later under explicit seed charter; sanitized only |
| Local admin | Create via **separate HITL** step (CLI or one-off script), not committed credentials |
| Roles catalog | Small static role rows may be seeded if content is non-secret (slugs/labels only) |

---

## 6. SAFE UNKNOWN

- Exact SQL types/lengths for each column at authoring time (draft is conceptual).
- Whether `project_type_profiles.default_rules_json` is populated in first seed or left empty.
- Whether FK `ON DELETE` behavior is `RESTRICT` vs soft-status only — decide in SQL review.
- When DB-03–DB-05 migrations are scheduled relative to Phase 2+ app features.
