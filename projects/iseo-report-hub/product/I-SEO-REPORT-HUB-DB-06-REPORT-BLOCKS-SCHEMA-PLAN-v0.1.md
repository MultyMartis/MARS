# I-SEO Report Hub — DB-06 Report Blocks Schema Plan v0.1

**Status:** SCHEMA PLAN ONLY — no SQL file; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Report Blocks DB-06 Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md)

---

## 1. Table name

`report_blocks`

---

## 2. Purpose

Store **ordered structured content blocks** belonging to one `monthly_report_contents` row.

Provides:

- parent link (`monthly_report_content_id`);
- stable `block_key` within parent;
- `block_type` allowlist;
- display `sort_order`;
- independent lifecycle `status`;
- title / body / summary content fields;
- JSON placeholders for structured data, weekly sources, and metric refs;
- owner / reviewer / audit actor hooks;
- `reviewed_at` / `approved_at` timestamps.

Does **not** replace DB-05 TEXT fields, evidence blobs, Topvisor metrics tables, or published client snapshots.

---

## 3. Columns

| Column | Type (planned) | Null | Default / notes |
|--------|----------------|------|-----------------|
| `id` | `BIGINT UNSIGNED` PK AI | NO | Surrogate key |
| `monthly_report_content_id` | `BIGINT UNSIGNED` | NO | FK → `monthly_report_contents.id` |
| `block_key` | `VARCHAR(64)` | NO | Stable key within parent (e.g. `executive_summary`) |
| `block_type` | `VARCHAR(64)` | NO | Type allowlist; see §8 |
| `sort_order` | `INT UNSIGNED` | NO | Default `0`; display order hint |
| `status` | `VARCHAR(32)` | NO | Default `draft`; see §7 |
| `title` | `VARCHAR(255)` | NO | Display title |
| `body` | `MEDIUMTEXT` | YES | Main block body |
| `summary` | `TEXT` | YES | Short summary |
| `data_json` | `JSON` | YES | Structured payload placeholder |
| `source_weekly_checkpoint_ids` | `JSON` | YES | Soft list of weekly checkpoint ids |
| `source_metric_refs` | `JSON` | YES | Soft metric/import ref placeholders |
| `owner_user_id` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `reviewer_user_id` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `created_by` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `updated_by` | `BIGINT UNSIGNED` | YES | FK → `users.id` |
| `reviewed_at` | `DATETIME` | YES | Set when status → `reviewed` (app rule) |
| `approved_at` | `DATETIME` | YES | Set when status → `approved` (app rule) |
| `created_at` | `DATETIME` | NO | `CURRENT_TIMESTAMP` |
| `updated_at` | `DATETIME` | NO | `CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP` |

---

## 4. Field meanings

| Field | Meaning |
|-------|---------|
| `monthly_report_content_id` | Parent monthly working document |
| `block_key` | Stable section identity within parent (unique per parent) |
| `block_type` | Semantic type for rendering/validation |
| `sort_order` | Display order hint (not uniquely constrained in MVP) |
| `status` | Block lifecycle state |
| `title` | Human label for list/detail UX later |
| `body` / `summary` | Narrative content |
| `data_json` | Optional structured JSON for typed blocks (e.g. metric snapshot shape later) |
| `source_weekly_checkpoint_ids` | Optional JSON array of `weekly_checkpoints.id` as soft hint |
| `source_metric_refs` | Optional JSON placeholder for future metric/import refs |
| `owner_user_id` | Specialist responsible for drafting the block |
| `reviewer_user_id` | Reviewer for ready/review flow |
| `created_by` / `updated_by` | Audit actors |
| `reviewed_at` | When block entered `reviewed` |
| `approved_at` | When block entered `approved` |

---

## 5. Indexes

| Index | Columns | Purpose |
|-------|---------|---------|
| PK | `id` | Identity |
| Unique | (`monthly_report_content_id`, `block_key`) | One key per parent |
| Index | (`monthly_report_content_id`, `sort_order`) | Ordered listing (non-unique) |
| Index | (`monthly_report_content_id`, `block_type`) | Type filters within parent |
| Index | `status` | Workflow filters |
| Index | `owner_user_id` | Assignment filters |
| Index | `reviewer_user_id` | Review queue filters |
| Index | `created_by` | Audit filters |
| Index | `updated_by` | Audit filters |

### Ordering policy

- **Do not** enforce `UNIQUE (monthly_report_content_id, sort_order)` in MVP.
- Reorder drafts may temporarily share or swap orders; service-level reorder can normalize later.
- Listing should `ORDER BY sort_order ASC, id ASC` as a stable secondary tie-break.

---

## 6. Unique constraints

1. `UNIQUE (monthly_report_content_id, block_key)`

Notes:

- MVP enforces **one block row per key inside one monthly report**.
- Creating a second row with the same `(parent, block_key)` must fail at DB level.
- Multiple blocks of the same `block_type` are allowed if `block_key` differs (e.g. two `custom_text` keys).

---

## 7. Status enum (CHECK)

Preferred storage: `VARCHAR(32)` + CHECK (matches DB-03 / DB-04 / DB-05 style).

Allowed statuses:

| Status | Meaning (short) |
|--------|-----------------|
| `draft` | Created; not actively worked |
| `in_progress` | Specialist drafting block |
| `ready_for_review` | Submitted for review |
| `reviewed` | Reviewer accepted |
| `approved` | Block approved for composition readiness |
| `archived` | Historical / frozen without delete |

Default for new rows: `draft`.

CHECK (planned):

```text
status IN (
  'draft',
  'in_progress',
  'ready_for_review',
  'reviewed',
  'approved',
  'archived'
)
```

Note: block uses `approved` (not parent monthly `finalized`) to keep section-level readiness distinct from parent document finalize.

---

## 8. Block type policy

### Recommended allowlist (DB CHECK preferred if stable)

| `block_type` | Typical use |
|--------------|-------------|
| `executive_summary` | Executive summary section |
| `work_completed` | Work completed |
| `results_summary` | Results / outcomes |
| `key_findings` | Key findings |
| `risks_and_blockers` | Risks and blockers |
| `next_month_plan` | Next month plan |
| `client_notes` | Client-facing notes (still internal until publish) |
| `internal_notes` | Internal-only notes |
| `custom_text` | Free-form custom section |
| `metric_snapshot` | Structured metric placeholder (`data_json`) |
| `weekly_summary` | Weekly rollup narrative |

CHECK (planned, if applied):

```text
block_type IN (
  'executive_summary',
  'work_completed',
  'results_summary',
  'key_findings',
  'risks_and_blockers',
  'next_month_plan',
  'client_notes',
  'internal_notes',
  'custom_text',
  'metric_snapshot',
  'weekly_summary'
)
```

| Topic | Policy |
|-------|--------|
| DB CHECK | **Recommended** for MVP if allowlist is accepted as stable |
| App-level only fallback | Allowed if apply wave finds CHECK too brittle; document decision in apply result |
| Relation to `block_key` | Often equal for standard sections; not required for `custom_text` |

---

## 9. CHECK constraints

| Constraint | Rule |
|------------|------|
| Status allowlist | status IN (…list above…) |
| Block type allowlist | block_type IN (…list above…) if CHECK adopted |
| JSON validity | Rely on MySQL `JSON` column type; no extra JSON CHECK unless portable |

### JSON field policy

| Topic | Policy |
|-------|--------|
| Types | `data_json`, `source_weekly_checkpoint_ids`, `source_metric_refs` — nullable `JSON` |
| Weekly shape | Array of unsigned integers (checkpoint ids), e.g. `[1,2,3,7]` |
| Metric refs shape | Soft placeholder array/object; exact schema deferred until import tables exist |
| `data_json` | Free structured placeholder; type-specific shapes deferred |
| Hard FK | **No** — not join tables; ids/refs are soft hints |
| Empty vs null | Both allowed; prefer `NULL` when unused |
| Invalid JSON | Rejected by MySQL JSON type when non-null invalid |
| Extra CHECK | Avoid unless portable on MySQL 8.4.3 |
| Membership validation | App/service should verify weekly ids belong to the same parent period later |

### Nullable fields

Nullable: `body`, `summary`, all JSON fields, all user FKs, `reviewed_at`, `approved_at`.

Required: identity, parent, `block_key`, `block_type`, `sort_order`, `status`, `title`, `created_at`, `updated_at`.

---

## 10. Foreign keys

| Column | References | On delete (planned) |
|--------|------------|---------------------|
| `monthly_report_content_id` | `monthly_report_contents.id` | **RESTRICT** |
| `owner_user_id` | `users.id` | `SET NULL` |
| `reviewer_user_id` | `users.id` | `SET NULL` |
| `created_by` | `users.id` | `SET NULL` |
| `updated_by` | `users.id` | `SET NULL` |

Rationale:

- Monthly content delete with child blocks must not silently wipe composition history.
- User deletion should not cascade-delete blocks.
- No FK from JSON weekly/metric fields in MVP.

---

## 11. Relation to `monthly_report_contents`

```text
monthly_report_contents (1)
  └── report_blocks (0..N)
```

- Child row requires an existing monthly report content row.
- Unique `(monthly_report_content_id, block_key)` enforces stable section keys.
- DB-05 TEXT fields remain present and canonical fallback until block editor acceptance.
- DB must **not** auto-sync block bodies into parent TEXT columns (or reverse) in DDL.

---

## 12. Relation to `weekly_checkpoints`

```text
reporting_periods (1)
  ├── weekly_checkpoints (0..N)
  └── monthly_report_contents (0..1)
         ├── source_weekly_checkpoint_ids (JSON soft hint on parent)
         └── report_blocks (0..N)
                └── source_weekly_checkpoint_ids (JSON soft hint per block)
```

| Aspect | Policy |
|--------|--------|
| Hard join table | Deferred |
| Soft snapshot | JSON id list on block (and optionally still on parent) |
| Cascade | None |
| Integrity | App validates same-period membership later |
| Weekly status coupling | None at DB level |

---

## 13. Relation to future metric / import tables

| Aspect | Policy |
|--------|--------|
| Normalized metric FKs | **Deferred** — Topvisor/import tables do not exist |
| Placeholder | `source_metric_refs` + optional `data_json` |
| Future redesign | May introduce join/normalized tables in a later DB wave without rewriting DB-06 meaning |

---

## 14. No-seed policy

| Policy | Decision |
|--------|----------|
| Seed in migration SQL | **No** |
| Seed in `schema_migrations` apply | **No** |
| Fixture blocks in apply-wave smoke | **Optional / allowed** if apply charter says so — under monthly content for period `2026-07` only; mark with `LOCAL_FIXTURE_ONLY` |
| Real client block data | **Forbidden** |

---

## 15. Future local fixture blocks (after apply; not this wave)

Recommended smoke set (insert only in apply wave if chartered):

| `block_key` / `block_type` | `sort_order` | `status` |
|----------------------------|--------------|----------|
| `executive_summary` | 10 | `draft` |
| `work_completed` | 20 | `draft` |
| `results_summary` | 30 | `draft` |
| `key_findings` | 40 | `draft` |
| `next_month_plan` | 50 | `draft` |

All titles/bodies/summaries/JSON content markers: `LOCAL_FIXTURE_ONLY`.  
Parent monthly content resolved dynamically by period `2026-07`.  
Weekly source ids resolved dynamically by W1–W4 keys when present.

---

## 16. Rollback considerations

| Scenario | Policy |
|----------|--------|
| Migration not yet applied | Delete/uncommit migration file under apply charter only |
| Applied, table empty | Drop table + remove ledger row only with explicit destructive approval |
| Applied, fixture smoke rows present | Prefer delete/archive smoke rows first; then empty-table rollback if chartered |
| Applied, non-demo rows present | **No** destructive rollback without dedicated charter + backup |
| Prior migrations `000001`–`000004` | **Never** rewrite after apply |

Preferred forward fix: additive migrations; avoid silent DROP in normal ops.

---

## 17. Explicit non-goals for this table

- Block editor UI / drag-drop reorder product
- Automatic sync with DB-05 TEXT columns
- Evidence / file uploads
- Client portal publish snapshots
- PDF/export artifacts
- Topvisor metrics storage tables
- Hard normalized weekly/metric join tables in this wave
