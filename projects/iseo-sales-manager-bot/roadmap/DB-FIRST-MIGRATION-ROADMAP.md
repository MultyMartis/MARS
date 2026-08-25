# DB-First Migration Roadmap (Sheets → PostgreSQL)

**Status:** ROADMAP ONLY — do **not** execute against the live stable contour  
**Current baseline:** Sales Manager v2 — Production Stable Baseline 2026-08-17 (Sheets-backed)  
**Target:** PostgreSQL as operational system of record; Sheets demoted to export/report  
**Related:** [DB-FIRST-SUCCESSOR-BLUEPRINT.md](DB-FIRST-SUCCESSOR-BLUEPRINT.md) · [SHEETS-DEPENDENCY-MAP.md](../architecture/SHEETS-DEPENDENCY-MAP.md)

No big-bang migration.

---

## Phase map

| Phase | Name | Authority after phase |
|-------|------|------------------------|
| **M0** | Schema design + local PostgreSQL | Sheets still SoR |
| **M1** | Dual-read offline validation | Sheets SoR; DB read-only shadow |
| **M2** | Historical sanitized migration rehearsal | Staging only |
| **M3** | Dual-write shadow mode | Sheets primary write; DB mirror |
| **M4** | DB read authority for non-critical queries | Sheets write primary |
| **M5** | DB operational authority | DB primary; Sheets backup/export |
| **M6** | Sheets downgrade to reporting/export | DB SoR |
| **M7** | Remove Sheets operational dependency | DB-only ops |

---

## M0 — Schema design + local PostgreSQL

**Objective:** Design schema matching blueprint entities; run local Postgres.  
**Inputs:** Sheets dependency map; field inventories; action-token model.  
**Outputs:** Migration scripts; ER diagram; seed config (`ai_enabled=false`).  
**Gates:** Schema review proves RAW/CLEAN split; unique keys for `source_message_id`; reminder query expressible in SQL.  
**Rollback:** Discard local DB; production untouched.  
**Do not:** Point production n8n at Postgres yet.

## M1 — Dual-read offline validation

**Objective:** Read production-exported snapshots into staging DB; compare card/reminder candidate sets.  
**Gates:** Row counts reconcile; sample lead_id set matches; no PII committed to Git.  
**Rollback:** Drop staging DB.

## M2 — Historical sanitized migration rehearsal

**Objective:** Rehearse sanitized historical import with idempotent loaders.  
**Gates:** Re-run import is idempotent; sequence/order preserved; corrupt contacts excluded.  
**Do not:** Import malformed historical rows into live dedupe.

## M3 — Dual-write shadow mode

**Objective:** Workflows write Sheets (primary) + Postgres (shadow) under monitoring.  
**Gates:** Diff of shadow vs Sheets explainable; Sheets-only rollback proven.  
**Stop if:** Dual-write anomalies increase or callbacks diverge.

## M4 — DB read authority for non-critical queries

**Objective:** Switch reporting / health / non-critical admin reads to DB.  
**Gates:** No regression on cards, callbacks, reminders.  
**Keep:** Lifecycle writes on Sheets until M5.

## M5 — DB operational authority

**Objective:** DB becomes primary for RAW/CLEAN/lifecycle/callbacks/reminders.  
**Gates:** End-to-end acceptance matrix re-run; reminder natural window plan; rollback to Sheets documented and tested.  
**Rollback:** Revert workflow nodes to Sheets writers/readers from last known-good export.

## M6 — Sheets downgrade to reporting/export

**Objective:** Sheets becomes export/report/QA surface only.  
**Gates:** Operators can still inspect via export; ops no longer depend on Sheets quota for callbacks.

## M7 — Remove Sheets operational dependency

**Objective:** Remove operational Sheets credentials/nodes from production graphs when safe.  
**Gates:** New stable freeze documenting DB as current reality; dependency map updated.  
**Do not:** Delete historical Sheets evidence casually.

---

## Cross-cutting rules

1. **Reconciliation:** Compare row counts, `lead_id` sets, status histograms, reminder candidate sets.  
2. **Idempotency:** Every import/write path must be re-runnable safely.  
3. **Sequence/order:** Preserve intake timestamps; do not reorder lifecycle events.  
4. **No big-bang:** Never skip dual-write / dual-read evidence.  
5. **Rollback:** Always know previous good Sheets export + workflow revision.  
6. **Secrets:** Migrate credential *references*, not values into Git.  
7. **Stable contour:** Current PRODUCTION STABLE Sheets contour remains frozen until an explicit migration charter.

---

## Cutover gates (before declaring DB production)

- [ ] Dual-write anomaly rate acceptable  
- [ ] Callback idempotency proven on DB  
- [ ] Raw-source path reads `lead_sources` correctly  
- [ ] Reminder query matches Sheets candidate set  
- [ ] AI remains OFF unless separately chartered  
- [ ] Recovery runbook updated  
- [ ] New baseline document published
