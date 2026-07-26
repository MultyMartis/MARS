# I-SEO Report Hub — Report Snapshot Validation Plan v0.1

**Status:** PLANNING ONLY — for future DB-07 / Implementation waves; this charter wave does not create snapshots  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Snapshot Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-PLAN-v0.1.md)

---

## 1. Preflight

Before DB-07 or Implementation mutations:

| Check | Expect |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive / volume | `X:` / `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Staged index | safe for scoped work (or clean worktree) |
| i-SEO scoped WIP | only allowlisted wave paths |
| Foreign WIP | preserved |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Baseline counts | schema_migrations **5** (pre DB-07); tables **13**; monthly **1**; blocks **6**; weekly **4**; periods **2** |
| Monthly id 1 | status `finalized`; `finalized_at` non-null; `LOCAL_FIXTURE_ONLY` |
| Blocks | 6 non-archived `reviewed` (ordered keys as fixture) |
| Preview | `/monthly-reports/1/preview` and `/preview/print` auth 200 |
| `report_snapshots` | absent before DB-07; empty after DB-07 before create smoke |

---

## 2. Schema validation (DB-07)

| Step | Expect |
|------|--------|
| Apply migration | success |
| schema_migrations | **6** |
| tables | **14** |
| `report_snapshots` exists | yes |
| Columns / indexes / FKs | match Schema Plan |
| Status CHECK / app enum | active / superseded / archived |
| Row count | **0** |
| Unrelated tables counts | unchanged |
| Monthly/blocks content | unchanged |

---

## 3. Gate validation (Implementation)

| Case | Expect |
|------|--------|
| Monthly not finalized | create refused; audit `creation_failed` with gate keys |
| `finalized_at` null (if ever) | refused |
| Invalid render mode | refused |
| Unresolved weekly refs | refused |
| Draft/in_progress non-archived blocks | refused |
| Missing required blocks (blocks_primary) | refused |
| Actor without create role | refused |
| Finalized + ready fixture | create allowed |

---

## 4. Create snapshot smoke

On monthly id **1** finalized fixture:

1. `POST /monthly-reports/1/snapshot` (auth + CSRF) as admin_owner / lead;
2. Expect snapshot **version 1**, status `active`;
3. `snapshot_key` = `monthly-1-v1` (or documented equivalent);
4. `payload_json` includes **6** blocks in sort order:
   - executive_summary → work_completed → results_summary → risks_and_blockers → key_findings → next_month_plan;
5. `source_weekly_checkpoint_ids` includes `[1,2,3,7]` (or equivalent JSON);
6. `checksum_sha256` 64 hex chars;
7. Audit `report_snapshot.created`;
8. Monthly/blocks rows unchanged.

---

## 5. Idempotency smoke

1. Repeat create without changing source;
2. Expect **same** snapshot id returned (or clear refuse-duplicate with no second row);
3. Preferred: idempotent hit + audit `report_snapshot.idempotent_hit`;
4. `report_snapshots` count remains **1**.

---

## 6. Versioning smoke

1. Reopen monthly (admin) → edit LOCAL_FIXTURE_ONLY content via allowed path → re-finalize;
2. Create snapshot again;
3. Expect version **2**, prior v1 status `superseded`;
4. Only one `active`;
5. Checksums differ if content changed;
6. Prefer leave monthly **finalized** and optionally leave v2 active for next waves.

If reopen/edit cycle is deferred: document as deferred versioning smoke; still require design coverage.

---

## 7. Checksum validation

1. Recompute checksum from stored payload using service canonicalization;
2. Must equal `checksum_sha256`;
3. Changing any block body in live DB after snapshot must **not** change stored snapshot checksum;
4. New create after content change produces new checksum (versioning path).

---

## 8. View snapshot smoke

| Route | Expect |
|-------|--------|
| `GET /monthly-reports/1/snapshot` | 200; shows active or empty state |
| `GET /report-snapshots/{id}` | 200; immutable detail |
| Unauthenticated | redirect/401 per auth baseline |
| `client_viewer` | no access |

---

## 9. DB mutation boundaries

| Allowed during Implementation create smoke | Forbidden |
|--------------------------------------------|-----------|
| Insert `report_snapshots` | DELETE snapshot rows |
| Audit log inserts | Mutate reporting_periods |
| Status supersede updates on prior snapshots | Mutate weekly_checkpoints |
| | Mutate monthly content/blocks except via explicit reopen/re-finalize test path |
| | Real client data |
| | `.env` changes |

---

## 10. Regression smoke

- Monthly show still 200; finalization locks still hold while finalized;
- Preview/print still 200;
- Report blocks list/detail still locked when finalized;
- Period/weekly CRUD unaffected;
- No public routes added;
- No PDF/export endpoints.

---

## 11. No-public / no-export validation

- No unauthenticated snapshot URL;
- No `/export`, `/pdf`, public token routes introduced by snapshot wave;
- Snapshot detail requires auth + role gate;
- Browser print of preview is **not** counted as snapshot PDF export.

---

## 12. Data policy

- LOCAL_FIXTURE_ONLY titles/bodies only;
- No secrets in payload/audit;
- No production DB;
- Host exactly `127.0.0.1`; DB exactly `iseo_report_hub_dev`.

---

## 13. STOP conditions

STOP if:

- preflight fails;
- schema apply mutates unrelated counts unexpectedly;
- create succeeds on non-finalized monthly;
- duplicate active versions for same monthly;
- idempotency creates duplicate identical checksum rows;
- monthly/blocks mutated outside chartered reopen path;
- public/PDF surfaces appear;
- credentials printed;
- foreign WIP disturbed.

---

## 14. Recommended future implementation smoke (summary)

- confirm monthly id 1 finalized;
- create snapshot v1;
- verify payload includes 6 blocks ordered;
- verify checksum stable;
- repeat create returns existing / refuses duplicate safely;
- preview/source read unchanged;
- no report/monthly/block mutations except snapshot rows and audit;
- snapshot view 200 after UI implementation;
- no public/PDF/export.
