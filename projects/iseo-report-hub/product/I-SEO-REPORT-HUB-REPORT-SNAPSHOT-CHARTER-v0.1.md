# I-SEO Report Hub — Report Snapshot Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Snapshot Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-VALIDATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-RESULT-v0.1.md)

---

## 1. Purpose

Зафиксировать **первый internal immutable / semi-immutable report snapshot слой** после Report Finalization Implementation.

Цель charter:

1. Описать product model **snapshot** как frozen internal representation finalized monthly report.
2. Решить storage approach для MVP: **DB-backed table** (recommended) vs filesystem vs derived-on-demand.
3. Зафиксировать relationship: snapshot ↔ `monthly_report_contents` ↔ `report_blocks` ↔ weekly sources.
4. Определить creation gates, versioning, immutability / rebuild policy, checksum.
5. Зафиксировать, что snapshot — источник для **будущего** export/PDF/share, но сам не PDF и не public.
6. Подготовить schema / implementation / validation plans для следующей волны.
7. Не менять app-source / runtime / DB в этой волне.

Эта волна — **documentation / policy only**. Snapshot **не** кодируется здесь.

Отличие от Layer 02 [PUBLISHING-AND-SNAPSHOT-MODEL](I-SEO-REPORT-HUB-PUBLISHING-AND-SNAPSHOT-MODEL-v0.1.md): тот документ описывает **client-facing published snapshot**. Этот charter — **internal frozen source** после finalization; public publish остаётся out of scope.

---

## 2. Current Baseline

### Report Finalization Implementation

| Item | Value |
|------|-------|
| Primary commit | `4bda84e50e8fde82f4429aa24cb590aa26c430fb` — `feat(iseo-report-hub): add report finalization workflow` |
| Hash-record | `f2234453477abd30e24a32beaef1ce5c8e6ccc0b` — `docs(iseo-report-hub): record report finalization workflow commit hash` |
| Clarify | `10882e24d9ca6ec88247da1507bc888c3e88599d` — `docs(iseo-report-hub): clarify report finalization workflow commit hash record` |
| Smoke | **52/52 PASS** |
| Final state | monthly_report_contents id **1** = `finalized` |
| report_blocks | **6** blocks `reviewed` |
| Runtime | exact allowlist sync done |
| Push | **no** |

### Upstream baselines (unchanged authority)

| Layer | Primary / hash-record |
|-------|------------------------|
| Auth | `d4b3b2e2…` / `0cd2cfb7…` |
| Reporting Period CRUD | `392258fc…` / `f1d8a17e…` |
| Weekly Checkpoints CRUD | `911db07d…` / `64c42cbe…` |
| Monthly Report Content CRUD | `65f64124…` / `17553a55…` (+ clarify `eb00b3f4…`) |
| DB-06 Report Blocks migration | `1b71a021…` / `7393d7c1…` (+ clarify `86338d66…`) |
| Report Blocks CRUD | `135da213…` / `5c65ac88…` |
| Report Preview / Render | `4334b4a8…` / `52bd58a9…` (+ clarify `11a4f232…`) |
| Report Finalization Charter | `68f7fe3c…` / `86ee4589…` (+ clarify `2e93900a…`) |

### Current DB (read-only check this charter wave)

| Item | Value |
|------|-------|
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| schema_migrations | **5** |
| Tables | **13** |
| users / roles | **1** / **6** |
| clients / projects / sites | **1** / **1** / **1** |
| reporting_periods | **2** |
| weekly_checkpoints | **4** |
| monthly_report_contents | **1** |
| report_blocks | **6** |
| `report_snapshots` table | **absent** (0) |

### Parent monthly report content

| Field | Value |
|-------|-------|
| Id | **1** |
| Parent period | id **1** / `2026-07` |
| Status | `finalized` |
| Title | `Demo Monthly Report — July 2026 — LOCAL_FIXTURE_ONLY` |
| `source_weekly_checkpoint_ids` | `[1, 2, 3, 7]` (W1–W4) |
| `finalized_at` | non-null (`2026-07-26 21:46:07`) |
| Flat DB-05 fields | contain `LOCAL_FIXTURE_ONLY` |
| created_by / updated_by | **1** / **1** |

### Current report blocks (ordered, non-archived)

| id | block_key | status | sort_order |
|----|-----------|--------|------------|
| 1 | `executive_summary` | `reviewed` | 15 |
| 2 | `work_completed` | `reviewed` | 20 |
| 3 | `results_summary` | `reviewed` | 30 |
| 9 | `risks_and_blockers` | `reviewed` | 35 |
| 4 | `key_findings` | `reviewed` | 40 |
| 5 | `next_month_plan` | `reviewed` | 50 |

All retain `LOCAL_FIXTURE_ONLY` markers / sources as applicable.

### Current preview / locks

| Item | Value |
|------|-------|
| `GET /monthly-reports/1/preview` | auth **200**; finalized badge/cues |
| `GET /monthly-reports/1/preview/print` | auth **200** |
| Render mode | `blocks_primary` |
| Monthly edit | locked |
| Block create/edit/update | locked |
| Preview/print | readable |

### Current limitation

- no snapshot table;
- no snapshot creation route/action;
- no frozen snapshot payload;
- no snapshot hash/checksum;
- no snapshot versioning;
- no immutable rendered artifact;
- no export/PDF;
- no public share;
- no client approval.

---

## 3. Problem

Система умеет **finalize** monthly report и **preview/print** его в live composition из `monthly_report_contents` + `report_blocks`.

Но нет **зафиксированной версии** отчёта:

- после reopen/re-edit/re-finalize live rows могут измениться;
- нет stable identity для будущих export/PDF/share слоёв;
- нет checksum для drift detection;
- нет version history (v1 / v2) между циклами finalization;
- finalization lock защищает текущее состояние, но **не** сохраняет frozen copy.

Нужен internal snapshot слой как next product/design step после finalization.

---

## 4. Scope

### In scope

- internal snapshot policy;
- DB-backed snapshot recommendation (`report_snapshots`);
- snapshot creation gates;
- versioning / supersede rules;
- immutability / rebuild policy;
- canonical payload + checksum design;
- relationship to monthly / blocks / weekly sources;
- future implementation + smoke/validation plan;
- route/service/UI/access/audit recommendations (design only).

### Out of scope

- PDF/export implementation;
- public share / token URL;
- client portal;
- filesystem / object storage artifacts;
- digital signatures;
- email sending;
- snapshot diff UI;
- charts/metric rendering;
- Topvisor imports;
- production deployment;
- app-source / runtime / DB mutation in this wave.

---

## 5. Product Rules

1. Snapshot — **internal-only** frozen representation finalized monthly report at a moment in time.
2. Snapshot создаётся **только** из `finalized` monthly report.
3. Snapshot **read-only** после creation (active / superseded / archived — все immutable).
4. Snapshot строится из **preview/render composition** (тот же semantic source, что internal preview).
5. Snapshot — intended source для future export/PDF/share; **сам не PDF**, не public, не client delivery.
6. MVP storage: **DB-backed table** `report_snapshots` (next DB-07 wave).
7. Не хранить huge HTML без нужды: primary = normalized JSON payload; optional `rendered_text` / `rendered_html`.
8. Checksum SHA-256 над canonical payload — drift detection.
9. Versioning: first snapshot = v1; после reopen/re-finalize = v2+; prior active → `superseded`.
10. Idempotency: повторный create при том же checksum возвращает existing active snapshot.
11. No hard delete.
12. `client_viewer` — no access; public routes — none.

### Storage decision (MVP)

| Option | Verdict |
|--------|---------|
| DB-backed table | **Recommended** |
| Filesystem artifact | Not recommended for MVP (storage boundaries / backup semantics) |
| Derived-on-demand only | Insufficient — finalization exists; export needs frozen source |

---

## 6. Snapshot Gates

Snapshot can be created only if:

- monthly report exists;
- monthly status is `finalized`;
- `finalized_at` is non-null;
- preview render mode is valid (`blocks_primary` or valid `flat_fallback`);
- source weekly refs resolve;
- non-archived blocks exist, unless `flat_fallback`;
- no non-archived `draft` / `in_progress` blocks;
- required canonical blocks exist if `blocks_primary`;
- actor has role `admin_owner` or `seo_lead_reviewer`;
- no active snapshot already exists for same finalized state/checksum unless force/new-version explicitly allowed.

MVP behaviour:

- refuse if monthly not finalized;
- create version **1** for current finalized fixture;
- repeated create: **idempotent** return existing active if checksum unchanged (recommended).

---

## 7. Snapshot Lifecycle

Statuses: `active` | `superseded` | `archived`

Rules:

- all statuses are read-only after write;
- no hard delete;
- new snapshot after reopen/re-finalize: version increments; old active → `superseded`; new `active` created;
- archive is admin-only and **not required** in first implementation wave after DB-07;
- one active snapshot per monthly report recommended at app/service level (MySQL unique-active awkward; enforce in service).

---

## 8. Safety Boundary

This charter wave:

- **no** app-source edits;
- **no** runtime edits;
- **no** DB mutation;
- **no** SQL/migration create/edit;
- **no** report_blocks / monthly / weekly / period row changes;
- **no** snapshot implementation;
- **no** PDF/export/public share;
- **no** push / fetch / pull / reset / clean / stash;
- foreign WIP preserved.

Target DB identity (read-only if checked): `iseo_report_hub_dev` @ `127.0.0.1` only.

Data policy: LOCAL_FIXTURE_ONLY fixtures only; no real client data.

---

## 9. Next Implementation Wave

**Recommended next action:**

**I-SEO Report Hub — Report Snapshot DB-07 Migration Apply 01**

Justification: this wave already delivers charter + design + schema plan + validation plan. A separate DB-07 Migration Charter is optional; schema plan is sufficient documentation gate. Next concrete step is create/apply migration for `report_snapshots`.

After DB-07 migration apply:

- Report Snapshot Service/UI Implementation 01 (create/view routes, checksum, idempotency, UI card).

See [IMPLEMENTATION-PLAN](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-PLAN-v0.1.md) and [VALIDATION-PLAN](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-VALIDATION-PLAN-v0.1.md).
