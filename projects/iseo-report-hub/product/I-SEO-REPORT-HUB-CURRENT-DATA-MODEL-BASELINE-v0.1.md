# I-SEO Report Hub — Current Data Model Baseline v0.1

**Status:** CHARTER / BASELINE — documentation only; no schema mutation in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Nikita Report Template Data Model Charter 01  
**Source of truth for schema:** `projects/iseo-report-hub/app-source/database/migrations/`  
**Local DB (runtime, not mutated here):** `iseo_report_hub_dev` @ `127.0.0.1:3306`

---

## 1. Purpose

Document the **as-built** Report Hub MVP data model so Nikita taxonomy evolution can be planned without breaking current local flow (periods → weekly → monthly → blocks → finalize → snapshot → export → share).

---

## 2. Entity inventory (tables)

| Table | Migration | Role |
|-------|-----------|------|
| `schema_migrations` | DB-01 | Migration ledger |
| `users` | DB-01 | Auth identities |
| `roles` | DB-01 | Role catalog (seeded codes) |
| `user_roles` | DB-01 | User↔role |
| `audit_log` | DB-01 | Event audit |
| `clients` | DB-01 | Client org |
| `projects` | DB-01 | SEO project under client; `project_type` enum |
| `sites` | DB-01 | Site URL(s) under project |
| `project_type_profiles` | DB-01 | Optional profile settings JSON |
| `reporting_periods` | DB-03 | Monthly period container |
| `weekly_checkpoints` | DB-04 | W1–W6 notes under period |
| `monthly_report_contents` | DB-05 | One monthly narrative row per period |
| `report_blocks` | DB-06 | Ordered blocks under monthly content |
| `report_snapshots` | DB-07 | Immutable render payload after finalize |
| `report_exports` | DB-08 + DB-09 | HTML/PDF artifacts + template metadata |
| `report_export_shares` | DB-10 | Tokenized public share links |

**Not present today:** work catalogue tables, work entry rows, structured metrics tables, evidence attachment tables, AI draft fields.

---

## 3. Relationships (lifecycle graph)

```
clients 1—* projects 1—* sites
projects 1—* reporting_periods
reporting_periods 1—* weekly_checkpoints
reporting_periods 1—1 monthly_report_contents
monthly_report_contents 1—* report_blocks
monthly_report_contents 1—* report_snapshots
report_snapshots 1—* report_exports
report_exports 1—* report_export_shares
users referenced as owner/reviewer/created_by across period/weekly/monthly/blocks/snapshots/exports/shares
```

---

## 4. Current report lifecycle

| Stage | Entity / status | Specialist action |
|-------|-----------------|-------------------|
| 1. Period | `reporting_periods.status` draft→active→…→finalized/archived | Create month (`period_key` YYYY-MM) |
| 2. Weekly | `weekly_checkpoints` W1–W4 typical; free-text fields | Enter work_done / findings / next_steps / risks |
| 3. Monthly shell | `monthly_report_contents` | Flat TEXT columns + optional notes |
| 4. Blocks | `report_blocks` keyed by `block_key` | CRUD bodies; sort_order; status per block |
| 5. Preview | Assembler (`blocks_primary` / `flat_fallback`) | Internal preview/print |
| 6. Finalization | Monthly status → ready_for_review → reviewed → finalized | Readiness gates in `ReportFinalizationService` |
| 7. Snapshot | `report_snapshots` payload + checksum | Freeze render |
| 8. Export | `report_exports` html/pdf + checksum | Artifact file |
| 9. Share | `report_export_shares` token_hash | Client handoff link |

Locks: when monthly is `finalized`, normal content/block mutations blocked until reopen (admin).

---

## 5. Weekly vs monthly separation (as built)

| Aspect | Weekly checkpoint | Monthly content / blocks |
|--------|-------------------|--------------------------|
| Grain | Week index 1–6; unique per period | One monthly row per period |
| Fields | title, summary, work_done, findings, next_steps, risks | Flat narrative columns + block rows |
| Client delivery | Internal by default (architecture intent) | Client path via snapshot/export/share |
| Linkage | IDs may be stored in monthly/block `source_weekly_checkpoint_ids` JSON | Soft refs; finalization checks resolve |

**Limit:** weekly notes are free-text blobs — **not** catalogue work items. Monthly «что сделали» is also free-text / block body — **not** category-structured.

---

## 6. Current report blocks / keys

### 6.1 Flat columns on `monthly_report_contents`

- `executive_summary`
- `work_completed`
- `results_summary`
- `key_findings`
- `risks_and_blockers`
- `next_month_plan`
- plus `client_notes`, `internal_notes`

### 6.2 `report_blocks` CHECK-allowed `block_type` values

`executive_summary`, `work_completed`, `results_summary`, `key_findings`, `risks_and_blockers`, `next_month_plan`, `client_notes`, `internal_notes`, `custom_text`, `metric_snapshot`, `weekly_summary`

### 6.3 Finalization required block keys

From `ReportFinalizationService::REQUIRED_BLOCK_KEYS`:

1. `executive_summary`
2. `work_completed`
3. `results_summary`
4. `key_findings`
5. `next_month_plan`

**Note:** `risks_and_blockers` exists as column/type/UI label but is **not** in the required-key gate list (MVP quirk — SAFE UNKNOWN if intentional).

### 6.4 Russian manager labels (`UiLabels`)

| Key | Label |
|-----|-------|
| `executive_summary` | Краткое резюме |
| `work_completed` | Что сделали |
| `results_summary` | Результаты |
| `risks_and_blockers` | Риски и блокеры |
| `key_findings` | Ключевые выводы |
| `next_month_plan` | План на следующий месяц |

---

## 7. Finalization / readiness rules (summary)

Gates include (non-exhaustive): monthly exists; period exists; title present; preview renderable; render mode valid; non-archived blocks exist; required keys present; required blocks reviewed/approved; no draft/in_progress blocks; weekly source refs resolve.

Roles: submit (specialist+), review/finalize (lead/admin), reopen (admin_owner).

---

## 8. Snapshot / export / share flow

| Step | Integrity hook |
|------|----------------|
| Snapshot | `checksum_sha256` over payload / rendered content |
| Export | `checksum_sha256` of file; `source_snapshot_checksum_sha256` |
| Share | `token_hash` only; once-URL handoff UX |

**Checksum impact rule:** any change to snapshot payload, block bodies, or export render template that regenerates artifacts **changes checksums**. Label-only UI changes do **not**. This charter forbids regen.

---

## 9. Seed / demo assumptions

| Item | Value |
|------|-------|
| Tool | `tools/create-local-fixture.php` |
| Marker | `LOCAL_FIXTURE_ONLY` |
| Client / project | Demo Client / Demo SEO Project |
| Project type | `service_corporate` |
| Period seed | `2026-07` |
| Constraint | Only `iseo_report_hub_dev` @ `127.0.0.1` |

Local operator state (attested outside this wave; not re-probed for mutation): exports/shares exist for delivery smoke; active share must not be mutated here.

---

## 10. Project type support (schema vs product use)

`projects.project_type` enum already includes:

- `service_corporate`
- `ecommerce`
- `content_information`
- `local_regional`
- `mixed_custom`

Nikita materials strongly distinguish **интернет-магазин** vs **сайт услуг**. Hub does **not** yet filter blocks/catalogue by type — type is stored but underused for report structure.

---

## 11. Changeability matrix (for future waves)

| Change class | Safe without breaking MVP? | Needs DB migration? | View/label only? | Needs new seed/demo? | Impacts PDF/export checksums? |
|--------------|----------------------------|---------------------|------------------|----------------------|-------------------------------|
| RU labels / hide machine keys | Yes | No | Yes | No | No (if no regen) |
| Rename block titles in UI only | Yes | No | Yes | Optional | No unless regen |
| Add optional `data_json` usage inside existing blocks | Mostly yes | No (column exists) | No | Optional | Yes if exported content changes |
| Add new `block_type` CHECK values | Careful | Yes (ALTER CHECK) | No | Likely | Yes if used in export |
| Drop/rename required `block_key`s | **Breaks** finalization | Likely | No | Yes | Yes |
| Add catalogue + work entry tables | Additive if old path kept | Yes | No | Yes | Only after assembly changes export |
| Dual-write work entries → keep 6 summaries | Compatible path | Yes | No | Yes | When summaries/export change |
| Change weekly free-text → structured entries | Medium risk | Yes | No | Yes | Indirect |
| AI draft columns | Additive nullable | Yes | No | Optional | If AI text enters export |

**Safe later without breaking current MVP:** additive tables; nullable columns; new UI routes that leave old CRUD working; keep REQUIRED_BLOCK_KEYS until dual-write proven.

**Requires migration:** catalogue, work entries, CHECK expansions, non-nullable new fields, removing flat columns.

**View/label-only:** Russian titles, help text, category display names mapped from keys.

**Seed/demo:** any catalogue seed; ecommerce vs service fixture profiles; sample work entries.

**Checksum impact:** regenerating snapshot/PDF/HTML after content or template change.

---

## 12. Current limitations (product)

1. Six generic narrative shells ≠ Nikita work taxonomy.  
2. No reusable work catalogue.  
3. No per-item status/evidence/visibility.  
4. Weekly → monthly synthesis is manual/soft JSON refs.  
5. `metric_snapshot` / `weekly_summary` types allowed but not first-class product flow.  
6. Client vs internal visibility not modeled per field.  
7. AI-assist fields absent.  
8. Access/credentials from Nikita materials must never enter this model.

---

## 13. SAFE UNKNOWN

- Whether live DB row counts match last Fix 01 attestation without a new probe (this wave did not query DB).  
- Whether `risks_and_blockers` omission from REQUIRED_BLOCK_KEYS is intentional product policy.  
- Exact production migration path for existing finalized snapshots if block semantics change.
