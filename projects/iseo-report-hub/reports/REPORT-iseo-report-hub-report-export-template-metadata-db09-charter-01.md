# REPORT — I-SEO REPORT HUB REPORT EXPORT TEMPLATE METADATA DB-09 CHARTER 01

**Status:** COMPLETE (docs/policy only)  
**project_id:** `iseo-report-hub`  
**Date:** 2026-07-27  
**Primary commit:** `6603aa17d094f9fe7d163535e3e6cf5aac713360`  
**Hash-record commit:** `PENDING_HASH_RECORD`  
**Push:** **no**

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `00982547c434c9c497716a69a1031a277bc8d030` |
| Staged/index on main | **non-empty** — foreign-only (`client-ops-reporting-bridge` and other non-i-SEO paths); **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree used | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-report-export-template-metadata-db09-charter-01\repo` (detached at `00982547`) |
| i-SEO WIP clean before | **yes** |
| Foreign WIP preserved | **yes** — main index not modified/unstage |
| Write scope | allowlisted Active Brain docs under `projects/iseo-report-hub/` only (in worktree) |

---

## 2. Baseline Reviewed

### Visual QA

| Item | Value |
|------|-------|
| Primary | `1d1d3c0d4af462698dc8fef84c03d3d1673bdcab` |
| Hash-record | `cc488020818a88316f6f3bbf32650661aaa976a7` |
| Tip | `00982547c434c9c497716a69a1031a277bc8d030` |
| Verdict | **PASS_WITH_MINOR_ISSUES** |
| DB/artifacts during QA | unchanged |

### Styled Export Version Apply

| Item | Value |
|------|-------|
| Primary | `31ff2a734c894ab50ba3532e3b96b68391b002ae` |
| Hash-record | `c7ce6b8649c364102cb32b8d8fc2f5240bf1a527` |
| `report_exports` | **4** (html **2**, pdf **2**) |
| Schema | unchanged (still DB-08 shape) |

### DB baseline (read-only this charter)

| Metric | Value |
|--------|-------|
| Target | `iseo_report_hub_dev` @ `127.0.0.1` |
| schema_migrations | **7** |
| tables | **15** |
| report_exports | **4** |
| report_snapshots / monthly / blocks / periods / weekly | **1** / **1** / **6** / **2** / **4** |
| Export ids | 1–4 keys/checksums match baseline |

### Artifact baseline (read-only)

| File | size | checksum |
|------|------|----------|
| `monthly-1-v1.html` | 5360 | `c194c62b…626fadc4` |
| `monthly-1-v1.pdf` | 133005 | `707e72d6…880d0320` |
| `monthly-1-v2.html` | 8562 | `27a6eee6…f95f6ffe` |
| `monthly-1-v2.pdf` | 117055 | `a8c4d61c…41a56b6b` |

### Current limitation

Template/render lineage is **not** durable in DB; UI/docs/artifact inference only.

---

## 3. Charter Output

Created/updated:

- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-DESIGN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-VALIDATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-report-export-template-metadata-db09-charter-01.md` (this file)
- `OPERATIONAL-INDEX.md` — DB-09 Charter status + next = Migration Apply 01

---

## 4. Schema Decision

| Item | Decision |
|------|----------|
| Option | **A** (phased D) — nullable columns on `report_exports` |
| Columns | `template_id`, `template_version`, `render_target`, `render_engine`, `render_options_json`, `source_html_export_id`, `metadata_json` |
| Indexes | `idx_report_exports_template` (`template_id`, `template_version`); `idx_report_exports_source_html` (`source_html_export_id`) |
| FK | `source_html_export_id` → `report_exports(id)` **ON DELETE SET NULL** |
| Registry deferred | `report_templates` / client assignment premature for single MVP template `iseo_default_v1` |

---

## 5. Backfill Policy

| id | key | Policy |
|----|-----|--------|
| 1 | `snapshot-1-html-v1` | `template_id` / `template_version` **NULL**; no invent |
| 2 | `snapshot-1-pdf-v1` | template NULL; `source_html_export_id` NULL |
| 3 | `snapshot-1-html-v2` | may backfill `iseo_default_v1` / `1` / `html_export` / `php_template_renderer` |
| 4 | `snapshot-1-pdf-v2` | may backfill same template; `pdf_export` / `edge_headless_pdf`; `source_html_export_id=3` |

Gates: exact id + exact `export_key` (+ checksum preferred). Idempotent. **Not executed** in this charter.

---

## 6. Migration / Validation Plan

| Item | Value |
|------|-------|
| Next wave | **I-SEO Report Hub — Report Export Template Metadata DB-09 Migration Apply 01** |
| Expected file | `2026_07_27_000008_add_template_metadata_to_report_exports_table.sql` (sequence verify required) |
| Apply plan | source migration → runtime sync → local apply → optional gated backfill 3–4 → validate |
| Validation plan | schema/rows/backfill/artifacts/compatibility; no public route; no export mutation |
| STOP | wrong DB host/name; count drift; v1 invented as default template; artifact mutation |

---

## 7. Restrictions Confirmed

- no app-source edits;
- no runtime edits;
- no DB mutation;
- no SQL/migration creation/edit;
- no report_exports / snapshots / blocks / monthly / weekly / period row changes;
- no artifact regeneration;
- no new export rows;
- no package install/download;
- no push / fetch / pull / reset / clean / stash;
- no broad git add;
- foreign WIP preserved on main.

---

## 8. Commit

| Item | Value |
|------|-------|
| Exact-path git add | allowlisted docs only (worktree) |
| Primary message | `docs(iseo-report-hub): add export template metadata db09 charter` |
| Primary hash | `6603aa17d094f9fe7d163535e3e6cf5aac713360` |
| Hash-record message | `docs(iseo-report-hub): record export template metadata db09 charter commit hash` |
| Hash-record hash | `PENDING_HASH_RECORD` |
| Push | **no** |

---

## 9. SAFE UNKNOWN

- Whether operator will include controlled backfill of ids 3–4 in the same Migration Apply wave or defer it — **policy allows either**; default recommendation = include gated backfill.
- Exact final migration filename if Apply discovers sequence collision — verify at apply time.
- Live MySQL CLI not on PATH in this shell; DB read-only check used PHP PDO instead (counts verified).

---

## 10. Recommended Next Action

**I-SEO Report Hub — Report Export Template Metadata DB-09 Migration Apply 01**

---

## 11. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-DESIGN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-VALIDATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-export-template-metadata-db09-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 12. Git Actions

| Action | Status |
|--------|--------|
| exact-path git add | **yes** (allowlisted docs) |
| commit | **yes** (primary + hash-record) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout / update-ref | worktree create; post-commit `update-ref` main → new tip if safe |
| reset | **no** |
| restore | scoped main restore of i-SEO docs only if needed after update-ref |
| clean | **no** |
| stash | **no** |
| broad git add | **no** |
| clean temporary worktree | used for commit; leave path for operator unless remove requested |
