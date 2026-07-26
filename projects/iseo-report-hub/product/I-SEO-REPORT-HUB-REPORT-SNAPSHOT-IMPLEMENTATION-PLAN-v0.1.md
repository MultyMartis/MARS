# I-SEO Report Hub — Report Snapshot Implementation Plan v0.1

**Status:** PLANNING ONLY — for next waves; this charter wave does not implement  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Snapshot Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-VALIDATION-PLAN-v0.1.md)

---

## 1. Next wave name (chosen)

**I-SEO Report Hub — Report Snapshot DB-07 Migration Apply 01**

### Alternatives considered

| Wave | Verdict |
|------|---------|
| Report Snapshot DB-07 Migration Charter 01 | Optional docs gate — **skipped** as separate wave because this package already includes schema plan + validation |
| Report Snapshot DB-07 Migration Apply 01 | **Chosen** — concrete next |
| Report Snapshot Service/UI Implementation 01 | Comes **after** migration apply |

### Justification

Charter + design + schema plan + validation plan already provide documentation gate. Next value is creating/applying `report_snapshots` migration (DB-07). Service/UI without table is blocked.

---

## 2. Wave sequence

1. **DB-07 Migration Apply 01** — create SQL migration + apply to `iseo_report_hub_dev`; docs result; no snapshot app routes required yet.
2. **Report Snapshot Implementation 01** (name TBD) — service/repository/routes/UI/audit/smoke create+view+idempotency.
3. Later (separate charters): export/PDF depending on snapshot; public publish — **not** this sequence’s default.

---

## 3. DB-07 Migration Apply 01 — allowed actions

| Action | Policy |
|--------|--------|
| Create migration SQL under `app-source/database/migrations/` | **Yes** (exact new file only) |
| Apply to `iseo_report_hub_dev` @ `127.0.0.1` | **Yes** |
| Insert `schema_migrations` row | **Yes** |
| Create table `report_snapshots` | **Yes** |
| Mutate monthly / blocks / weekly / periods | **No** |
| Seed snapshot rows | **No** (unless explicit smoke charter later) |
| Runtime sync of migration file | Per Model A allowlist if runtime needs file present; apply may run from source tool — charter of Apply wave decides |
| DROP unrelated / TRUNCATE | **No** |

Expected after apply: schema_migrations **6**; tables **14**; `report_snapshots` empty.

---

## 4. After migration — Service/UI Implementation (preview)

Allowed touch set (future Implementation wave; not DB-07):

| Path | Role |
|------|------|
| `app/routes.php` | snapshot GET/POST routes |
| `app/bootstrap.php` | DI |
| `app/Services/ReportSnapshotService.php` | **New** |
| `app/Repositories/ReportSnapshotRepository.php` | **New** |
| Controllers for monthly + snapshot | create/show |
| Views: monthly show, preview, snapshot detail | UI |
| `public/assets/css/app.css` | snapshot card styles |
| `README.md` | routes/policy |

Depends on: `ReportPreviewService`, monthly finalized status / finalization gates.

---

## 5. Runtime sync policy

Model A — source-first:

1. Change `app-source/` first;
2. Exact-path allowlist sync source → `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`;
3. Do **not** sync `.env` / `.env.local`;
4. No broad mirror copy;
5. No service restart unless Apply/Implementation charter explicitly requires and proves need.

DB-07 may sync only migration + runner docs as chartered; Implementation syncs PHP/views/CSS allowlist.

---

## 6. Smoke list (post-implementation; also see Validation Plan)

After Service/UI exists (not in DB-07 alone):

- confirm monthly id **1** finalized;
- create snapshot v1;
- payload includes **6** blocks ordered;
- checksum stable;
- repeat create → idempotent existing / refuse duplicate safely;
- preview/source read unchanged;
- no monthly/block/period/weekly mutations except snapshot rows + audit;
- snapshot view **200**;
- no public/PDF/export.

DB-07-only smoke: schema presence + count invariants + empty table.

---

## 7. Commit policy

- Exact-path `git add` allowlisted paths only.
- Never `git add .` / `-A` / `commit -a`.
- Foreign WIP preserved.
- Commit and push separate; **push no** unless operator charter.
- If main index blocked by foreign staged: clean temporary worktree under Storage (as this charter wave).

Suggested messages:

- DB-07: `feat(iseo-report-hub): add report snapshots migration` (or docs+sql as chartered)
- Implementation: `feat(iseo-report-hub): add report snapshot workflow`
- Docs hash-records as needed

---

## 8. STOP conditions

STOP if:

- wrong volume / branch / root;
- i-SEO foreign WIP conflict on allowlisted paths;
- staged includes non-allowlisted paths for the wave;
- DB host/name not exactly `127.0.0.1` / `iseo_report_hub_dev`;
- monthly id 1 not finalized when Implementation expects it;
- attempt to implement PDF/public in snapshot wave;
- migration would ALTER unrelated tables without charter;
- cannot keep foreign WIP intact.

Token: `STOP — I-SEO REPORT SNAPSHOT WAVE SAFETY CONDITION FAILED` (wave-specific detail in report).
