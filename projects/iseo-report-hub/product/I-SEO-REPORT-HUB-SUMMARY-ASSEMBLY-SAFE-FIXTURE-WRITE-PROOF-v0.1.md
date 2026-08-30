# I-SEO Report Hub — Summary Assembly Safe Fixture Write Proof v0.1

**Status:** CHARTER / WRITE PROOF PLAN — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Safe Fixture Charter 01

No POST apply and no fixture create in this wave.

---

## 1. Goal

Prove that `MonthlyReportSummaryApplyService` can UPDATE **one** auto-block `body` on a non-finalized local fixture, with polished Block Text Contract prose, while report id **1** and all publication artifacts stay unchanged.

---

## 2. Selected block (locked)

**Apply exactly one key first: `next_month_plan`.**

Reasons:

- Non-empty generated draft (2 plan entries) so empty-draft skip cannot hide a write bug.
- Minimizes mutation vs applying all three auto keys.
- Overwrite warning is testable if initial body is a placeholder.
- `work_completed` (4 bullets) and `risks_and_blockers` (1 bullet) remain as preview-only controls for this wave.

Applying all three auto keys is **out of scope** for Safe Fixture Implementation 01. Optional later: `Summary Assembly Apply Multi-Block Write Proof 01`.

---

## 3. Sequence

1. Preflight (volume, branch, i-SEO scope / clean worktree).  
2. Read-only baseline probe (counts + report 1 fingerprints).  
3. `mysqldump` `iseo_report_hub_dev`.  
4. `--create --confirm-local-fixture`.  
5. Record fixture monthly id `F`.  
6. HTTP `GET /monthly-reports/{F}/assembly-preview` as `polygon-ws@mail.ru` (do not print password). Expect **200**. Confirm stats 4 / 2 / 1 / included 7 / excluded 0. Confirm apply form is **enabled** (not finalized).  
7. Capture old `next_month_plan.body` + SHA-256, `summary`, `status`, `updated_at`; capture the other five bodies/summaries/status.  
8. Capture report 1 block max `updated_at`, export 4 checksum prefix, share 7 status.  
9. `POST /monthly-reports/{F}/assembly-apply` with:
   - CSRF
   - `block_keys[]=next_month_plan` only
   - `confirm_overwrite=1`
10. Expect redirect + success flash listing «План на следующий месяц».  
11. Verify DB (below).  
12. Evidence files in STORAGE.  
13. `--cleanup --confirm-local-fixture`.  
14. Verify baseline counts restored (except `audit_log`).  
15. Re-verify report 1 fingerprints.

Do **not** POST apply to id 1 except an optional **refuse** regression (already proven). If repeated, it must still 302-refuse with zero writes.

GET on `/assembly-apply` remains **405**. POST to `/assembly-preview` remains **405**.

---

## 4. Expected mutation (fixture monthly `F` only)

| Field | After apply |
|-------|-------------|
| `next_month_plan.body` | Block Text Contract plan text (intro + 2 bullets) |
| `next_month_plan.summary` | **Unchanged** |
| `next_month_plan.status` | `in_progress` (was `draft`) |
| `next_month_plan.reviewed_at` / `approved_at` | NULL |
| `next_month_plan.updated_by` | session user id |
| `next_month_plan.updated_at` | moved |
| `data_json` | object merge may add `assembly_applied_at`, `assembly_source_entry_ids`, `assembly_previous_body_sha256`; `mars_fixture_marker` **must remain** |
| Other five `report_blocks` body/summary/status | **Unchanged** |
| `monthly_report_contents` status / flats / `finalized_at` | **Unchanged** (`in_progress`, no finalize) |
| Work entries | **Unchanged** |
| Snapshots / exports / shares | still **0** for `F` |

---

## 5. Must stay unchanged (report 1 + publication)

| Invariant | Probe 2026-08-17 |
|-----------|------------------|
| Monthly 1 status | `finalized` |
| Blocks r1 | 6; max `updated_at` `2026-07-27 01:46:07` |
| Entries r1 | 7 |
| Snapshots | 1 / `monthly-1-v1` |
| Exports | 4 |
| Shares | 7 / active 1 / revoked 6 |
| Share 7 | `active`, label `test-first-link` |
| Export 4 checksum prefix | `a8c4d61c6216e8d70b19` |
| PDF bytes | not regenerated (checksum + mtime/size if re-read) |
| Monthly 5 | still `draft`, 0 blocks, 0 entries |

---

## 6. Evidence (STORAGE, not git)

Folder:

`X:\AI MARS STORAGE\incoming\iseo-report-hub\summary-assembly-safe-fixture-implementation-01\`

Must include:

- `fixture-ids.json`
- dump path (filename only in git docs)
- old `next_month_plan.body` + SHA-256
- new `next_month_plan.body` + SHA-256
- selected key `next_month_plan`
- HTTP GET/POST status codes (no session cookies)
- before/after counts
- cleanup log (deleted ids)
- post-cleanup counts

No passwords, no raw share tokens, no `.env`.

---

## 7. Rollback / cleanup

**Planned path:** `--cleanup` after evidence is written.

If apply succeeds but cleanup fails: **STOP**, keep backup, keep fixture rows, report exact ids. Do not `git clean`. Do not reopen report 1. Do not restore the whole DB unless the operator issues a restore charter.

If apply fails: still cleanup the fixture (create is not the write proof). Record the failure.

---

## 8. Acceptance for Implementation 01

| Check | Pass if |
|-------|---------|
| Fixture created | marker + 6 blocks + 7 entries + no publication rows |
| Preview | 4 / 2 / 1; apply enabled |
| Write | only `next_month_plan.body` (and its status/audit/provenance) changed |
| Text | polished intro + bullets; not technical preview cards |
| Id 1 | unchanged |
| PDF/export/share | unchanged |
| Cleanup | fixture gone; baseline counts restored except `audit_log` |
| Id 5 | untouched |

Verdict if all pass: `SUMMARY ASSEMBLY SAFE FIXTURE WRITE PROOF PASS` (name may be shortened in the impl report).

---

## 9. SAFE UNKNOWN

- Exact flash wording if implementation copy differs by punctuation — compare keys updated, not pixel-identical flash.  
- Whether a second apply of the same key is run (idempotent skip). Optional, not required for MVP.
