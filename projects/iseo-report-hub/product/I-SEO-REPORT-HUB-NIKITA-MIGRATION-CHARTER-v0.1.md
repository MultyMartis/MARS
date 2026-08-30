# I-SEO Report Hub — Nikita Migration Charter v0.1

**Status:** CHARTER FOR FUTURE IMPLEMENTATION — **do not apply in this wave**  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Nikita Report Template Data Model Charter 01  
**Recommended next impl wave:** `I-SEO Report Hub — Nikita Catalogue Seed and Work Entry Model Implementation 01`

**Extra charter 02?** Not required for table shapes below. Use a short seed-review HITL only if operator disputes taxonomy codes after reading Taxonomy v0.1.

---

## 1. Goal

Add additive catalogue + monthly work-entry model aligned to Nikita taxonomy while preserving current MVP period→weekly→monthly→blocks→finalize→snapshot→export→share flow.

---

## 2. Day-1 required tables

### 2.1 `seo_work_categories`

| Column | Type | Notes |
|--------|------|-------|
| id | BIGINT PK | |
| code | VARCHAR(64) UNIQUE | e.g. `semantics` |
| title_ru | VARCHAR(190) | |
| description | TEXT NULL | From Nikita «пояснение» where available |
| sort_order | INT UNSIGNED | |
| is_active | TINYINT(1) | default 1 |
| is_report_content | TINYINT(1) | 0 for excluded ops categories |
| created_at / updated_at | DATETIME | |

Indexes: unique `code`; key `sort_order`.

### 2.2 `seo_work_items`

| Column | Type | Notes |
|--------|------|-------|
| id | BIGINT PK | |
| category_id | FK → categories | |
| code | VARCHAR(96) | unique per category or global unique |
| title_ru | VARCHAR(255) | |
| description | TEXT NULL | |
| site_applicability | ENUM('both','service','ecommerce') | |
| cadence | ENUM('one_time','weekly','monthly','recurring','as_needed') | |
| default_visibility | ENUM('internal','client_safe','client_facing') | |
| default_fill_mode | ENUM('manual','ai_assisted','computed') | default manual |
| evidence_required | TINYINT(1) | |
| is_active | TINYINT(1) | |
| sort_order | INT UNSIGNED | |
| metadata_json | JSON NULL | quotas hints, etc. |
| created_at / updated_at | DATETIME | |

Indexes: unique (`category_id`,`code`); key (`site_applicability`,`is_active`).

### 2.3 `monthly_report_work_entries`

| Column | Type | Notes |
|--------|------|-------|
| id | BIGINT PK | |
| monthly_report_content_id | FK RESTRICT | |
| reporting_period_id | FK RESTRICT | denormalized for queries |
| catalogue_item_id | FK NULL | null = custom |
| category_code | VARCHAR(64) NULL | snapshot of category at edit time |
| title | VARCHAR(255) | |
| status | ENUM/VARCHAR | planned,in_progress,done,blocked,skipped,archived |
| description | MEDIUMTEXT NULL | |
| result_effect | TEXT NULL | |
| client_summary | TEXT NULL | |
| internal_note | TEXT NULL | |
| evidence_url | VARCHAR(1024) NULL | day-1 simple |
| next_action | TEXT NULL | |
| visibility | VARCHAR(32) | |
| priority | TINYINT NULL | |
| weekly_checkpoint_id | FK NULL | |
| owner_user_id / reviewer_user_id | FK NULL | |
| sort_order | INT UNSIGNED | |
| created_by / updated_by | FK NULL | |
| created_at / updated_at | DATETIME | |

Indexes: (`monthly_report_content_id`,`sort_order`); (`reporting_period_id`,`status`); (`catalogue_item_id`).

---

## 3. Later (explicitly not day-1)

| Table / feature | Why later |
|-----------------|-----------|
| `weekly_checkpoint_work_entries` | Weekly free-text still enough |
| `report_metrics` | Integrations not ready |
| `report_evidence_links` | Start with `evidence_url` |
| AI draft columns | After entry UX exists |
| Quantitative quota enforcement | Plan metadata only at first |
| Dropping flat monthly columns | Only after assembly proven |
| Changing REQUIRED_BLOCK_KEYS | Separate gated wave |
| Client PDF visual redesign | Separate charter |

---

## 4. Relationships

```
seo_work_categories 1—* seo_work_items
monthly_report_contents 1—* monthly_report_work_entries
seo_work_items 1—* monthly_report_work_entries (optional)
weekly_checkpoints 1—* monthly_report_work_entries (optional)
reporting_periods 1—* monthly_report_work_entries
```

No FK changes to snapshots/exports/shares.

---

## 5. Migration safety

| Rule | Detail |
|------|--------|
| Additive only | CREATE TABLE; no DROP of existing report tables |
| No NOT NULL on existing columns | |
| Local DB only first | `iseo_report_hub_dev` |
| Backup/checkpoint | mysqldump or MARS backup checklist before apply |
| Rollback | DROP new tables only if empty/unused; ledger reverse policy per project migrate tool |
| Foreign WIP | Exact-path migrations only |
| Shares/PDF | Do not touch |

Suggested migration filenames (impl wave decides exact):

- `YYYY_MM_DD_0000XX_create_seo_work_categories_table.sql`
- `YYYY_MM_DD_0000XY_create_seo_work_items_table.sql`
- `YYYY_MM_DD_0000XZ_create_monthly_report_work_entries_table.sql`

---

## 6. Seed strategy (from Nikita)

1. Seed categories from Taxonomy v0.1 codes (exclude access).  
2. Seed work items from DOCX list + XLSX shared safe strings.  
3. Mark `site_applicability` using shop vs services deltas (both default; ecommerce/service overrides where evidenced).  
4. Store quantitative hints in `metadata_json` only — do not invent missing month matrices.  
5. Never seed credentials, passwords, raw access rows, or live counter secrets.  
6. Idempotent seed tool for `iseo_report_hub_dev` only.

Fixture update: optional 3–5 sample entries under Demo monthly report — English Demo* names may remain until separate cleanup.

---

## 7. UI routes affected (future impl)

| Area | Change |
|------|--------|
| Monthly show | Link «Работы за месяц» / entries list |
| New CRUD | entries index/show/form under monthly |
| Catalogue | read-only browser initially; admin edit later |
| Blocks / finalization | Unchanged day-1 |
| Preview/export/share | Unchanged until assembly wave |

---

## 8. Validation plan (impl wave)

1. Migrate dry-run / apply on local only.  
2. Seed counts: categories ≥ 12; items ≥ DOCX atomic list baseline.  
3. CRUD entry smoke under demo monthly.  
4. Confirm existing finalization still passes without entries.  
5. Confirm export/share row counts unchanged; no PDF regen.  
6. PHP lint + `/health` + auth smoke.  
7. Operator click-through on entry UI (subsequent UI wave if schema-only first).

---

## 9. Out of scope (this charter and day-1 impl)

- Runtime production apply  
- PDF regeneration  
- Share create/revoke  
- WordPress / i-seo.su mutation  
- Client visual template  
- AI providers  
- Metric integrations  

---

## 10. Rollback / backup

Before apply: DB dump of `iseo_report_hub_dev`.  
If abort: drop only new tables if no dependent product code shipped; restore dump if partial failure.  
Do not `git clean` / reset hard.

---

## 11. SAFE UNKNOWN

- Exact migration number sequence after DB-10.  
- Whether catalogue admin UI ships in same impl wave as schema (recommend schema+seed first, UI second if time-boxed).
