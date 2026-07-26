# REPORT — I-SEO REPORT HUB REPORT SNAPSHOT CHARTER 01

**Status:** COMPLETE (docs/policy only)  
**project_id:** `iseo-report-hub`  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Snapshot Charter 01  
**Primary commit:** `a84e871dd073bb81be505060ad99f3dd1c6afa84`  
**Hash-record commit:** `04a4206c4d30458ceb419ac7048e34e8b736365b`

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `10882e24d9ca6ec88247da1507bc888c3e88599d` |
| Staged/index before (main) | **non-empty foreign** (`projects/client-ops-reporting-bridge/**` staged deletes) — **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree used | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-snapshot-charter-01\repo` (detached at `10882e24`) |
| i-SEO WIP before | **clean** (`projects/iseo-report-hub/` no modified/untracked on main) |
| Foreign WIP | **preserved** (main index untouched; no unstage/restore of foreign paths) |
| Write scope | Active Brain docs only under allowlisted `product/` + `reports/` + `OPERATIONAL-INDEX.md` in clean worktree |

HEAD matched Report Finalization clarify `10882e24`. No STOP.

---

## 2. Baseline Reviewed

| Item | Value |
|------|-------|
| Report Finalization primary | `4bda84e50e8fde82f4429aa24cb590aa26c430fb` — `feat(iseo-report-hub): add report finalization workflow` |
| Report Finalization hash-record | `f2234453477abd30e24a32beaef1ce5c8e6ccc0b` |
| Report Finalization clarify | `10882e24d9ca6ec88247da1507bc888c3e88599d` |
| Smoke (finalization) | **52/52 PASS** |
| Push (finalization) | **no** |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Counts (read-only this wave) | schema_migrations **5**; tables **13**; users **1**; roles **6**; clients/projects/sites **1/1/1**; reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1**; report_blocks **6**; `report_snapshots` **absent** |
| Parent monthly | id **1**; period `2026-07`; status `finalized`; `finalized_at` non-null; title/markers `LOCAL_FIXTURE_ONLY`; sources `[1,2,3,7]` |
| Blocks (non-archived) | all **6** `reviewed`: executive_summary(15), work_completed(20), results_summary(30), risks_and_blockers(35), key_findings(40), next_month_plan(50) |
| Preview / locks | preview + print auth 200; monthly/block edits locked; finalized cues present |
| Current limitation | **No** snapshot table; **no** frozen payload; **no** checksum/versioning; **no** snapshot routes; **no** PDF/export/public share |

This charter wave did not mutate DB.

---

## 3. Charter Output

Created/updated:

- `product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-DESIGN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-VALIDATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-report-snapshot-charter-01.md` (this file)
- `OPERATIONAL-INDEX.md` — Report Snapshot Charter status; baseline on Finalization Implementation; proposed DB-07 `report_snapshots`; next = DB-07 Migration Apply 01; no code/runtime/DB in charter

---

## 4. Snapshot Design Summary

| Area | Design |
|------|--------|
| Definition | Frozen internal representation of finalized monthly report; not PDF/public/client delivery |
| Storage | **DB-backed** `report_snapshots` recommended; filesystem / derived-on-demand rejected for MVP |
| Table | `report_snapshots` — FK monthly + period; payload_json; optional rendered_text/html; checksum_sha256; version; status |
| Payload | metadata, period, client, project, site, monthly_report, blocks, weekly_sources, diagnostics, render |
| Checksum | SHA-256 over canonical normalized payload; exclude volatile created_at |
| Versioning | v1 first; v2+ after reopen/re-finalize; prior active → superseded; one active per monthly (app-enforced) |
| Idempotency | Same checksum → return existing active (`idempotent_hit`) |
| Routes | GET/POST `/monthly-reports/{id}/snapshot`; GET `/report-snapshots/{id}`; no delete/public/PDF |
| Service/repo | `ReportSnapshotService` + `ReportSnapshotRepository`; compose via `ReportPreviewService` |
| UI | Monthly snapshot card; preview cue; immutable snapshot detail |
| Access | create: admin_owner + seo_lead_reviewer; view: internal roles; client_viewer none |
| Audit | created / idempotent_hit / superseded / archived / creation_failed |
| Policy | No public; no PDF/export; no client portal |

---

## 5. Schema Plan

| Item | Plan |
|------|------|
| Table | `report_snapshots` |
| Key columns | id; monthly_report_content_id; reporting_period_id; snapshot_key; version; status; title; render_mode; payload_json; rendered_text/html; checksum_sha256; source_block_ids; source_weekly_checkpoint_ids; created_by; created_at; archived_at |
| Indexes | UNIQUE (monthly, version); UNIQUE snapshot_key; INDEX (monthly, status); INDEX (period, status) |
| Constraints | status CHECK active/superseded/archived; version >= 1 |
| FK | monthly RESTRICT; period RESTRICT; created_by SET NULL |
| Validation | After DB-07: migrations 6; tables 14; empty table; unrelated counts unchanged |
| This wave | **No SQL file created** |

---

## 6. Validation Plan

Documented for future waves:

- Schema validation (DB-07);
- Gate validation (non-finalized refuse);
- Create snapshot v1 smoke (6 blocks ordered);
- Idempotency smoke;
- Versioning smoke (reopen/re-finalize → v2);
- Checksum stability;
- View snapshot 200;
- DB mutation boundaries (snapshot + audit only);
- Regression + no-public/no-export.

---

## 7. Restrictions Confirmed

- no app-source edits;
- no runtime edits;
- no DB mutation;
- no SQL/migration creation/edit;
- no report_blocks row changes;
- no monthly_report_contents row changes;
- no weekly_checkpoint row changes;
- no reporting_period row changes;
- no admin/password/hash changes;
- no env changes;
- no source sync;
- no service restart;
- no push/fetch/pull/reset/clean/stash;
- no broad git add;
- foreign WIP on main preserved.

---

## 8. Commit

| Item | Value |
|------|-------|
| Exact-path git add | allowlisted docs only (in clean worktree) |
| Primary message | `docs(iseo-report-hub): add report snapshot charter` |
| Primary hash | `a84e871dd073bb81be505060ad99f3dd1c6afa84` |
| Hash-record message | `docs(iseo-report-hub): record report snapshot charter commit hash` |
| Hash-record hash | `04a4206c4d30458ceb419ac7048e34e8b736365b` |
| Push | **no** |

---

## 9. SAFE UNKNOWN

- Exact prior-migration CHECK-constraint style for DB-07 SQL (match existing migration dialect at apply time).
- Whether versioning smoke (reopen → edit → re-finalize → v2) will run in first Implementation wave or be deferred — plan covers both.
- Multi-role HTTP create/view smoke may remain deferred if only admin_owner session injection exists (same pattern as finalization).

---

## 10. Recommended Next Action

**I-SEO Report Hub — Report Snapshot DB-07 Migration Apply 01**

---

## 11. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-DESIGN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-SNAPSHOT-VALIDATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-snapshot-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 12. Git Actions

| Action | Result |
|--------|--------|
| exact-path git add | **yes** (allowlisted docs in clean worktree) |
| commit | **yes** (primary + hash-record) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout / update-ref | worktree add `--detach`; FF `update-ref` main branch to worktree HEAD after commits if safe |
| reset | **no** |
| restore | **no** |
| clean | **no** |
| stash | **no** |
| broad git add | **no** |
| clean temporary worktree | used: `X:\AI MARS STORAGE\git-sync-iseo-snapshot-charter-01\repo`; main foreign index untouched |

