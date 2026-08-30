# I-SEO Report Hub — Summary Assembly Safe Fixture Implementation Plan v0.1

**Status:** PLAN FOR NEXT IMPLEMENTATION — **do not implement in this wave**  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Safe Fixture Charter 01

---

## 1. Next wave (recommended)

**Name:** `I-SEO Report Hub — Summary Assembly Safe Fixture Implementation 01`

**Not next:** reopen report 1; seed report 5; apply all three auto blocks; PDF; Client Report Template Visual Alignment; screenshot QA of all pages; production; push.

---

## 2. Scope in

- Guarded CLI `app-source/tools/summary-assembly-safe-fixture.php` (`--create` / `--cleanup` / `--confirm-local-fixture`)
- Commit that tool in `app-source` (exact path)
- Optional exact source → runtime sync of **that tool file only** if the operator runs it from runtime `tools/`
- Backup dump to STORAGE
- Create dedicated fixture (new period + monthly + 6 blocks + 7 entries)
- GET assembly preview on fixture id
- POST apply **`next_month_plan` only**
- Capture old/new body + SHA
- Cleanup fixture by exact ids
- Verify baseline counts + report 1 / PDF / export / share unchanged
- Closeout docs + OPERATIONAL-INDEX
- Exact-path git commit of tools + docs; **no** evidence/backups

App apply/preview **code** already exists. Implementation 01 should **not** redesign apply unless a blocking bug is proven on the fixture.

---

## 3. Scope out

- Leaving fixture rows in the DB
- Mutating or deleting monthly id **1** or **5**
- Snapshot / export / share / PDF create or regenerate
- Catalogue INSERT
- New users
- Weekly checkpoint INSERT
- Multi-block apply
- Exclusion-entry edge fixture
- Transaction-only HTTP-less unit test as a substitute for the live POST proof (optional extra, not a replacement)
- `.env` edits

---

## 4. Git / tooling decisions

| Question | Decision |
|----------|----------|
| Commit fixture scripts? | **Yes** (guarded CLI) |
| Leave fixture in DB? | **No** — cleanup required |
| Leave id 5 untouched? | **Yes** |
| Mutate id 1? | **No** |
| Commit dumps / `fixture-ids.json`? | **No** |
| Push? | **No** unless operator asks |

---

## 5. Acceptance

| Check | Pass if |
|-------|---------|
| Tool guards | Refuses non-local DB / missing confirm / non-CLI |
| Fixture | Marker present; 6 blocks; 7 entries; 0 snapshots/exports/shares |
| Preview | 4 done / 2 plan / 1 risk / included 7 / excluded 0 |
| Apply | Only fixture `next_month_plan.body` (+ status/provenance) changes |
| Old/new | Captured in STORAGE with SHA |
| Cleanup | Fixture ids gone; core counts = pre-create baseline except `audit_log` |
| Id 1 | finalized; 6 blocks; 7 entries; `updated_at` fingerprint unchanged |
| Id 5 | draft; 0 blocks; 0 entries |
| PDF/export/share | exports 4; shares 7 active 1 revoked 6; checksum prefix `a8c4d61c6216e8d70b19` |

---

## 6. Prompt outline (implementation agent)

1. Preflight: volume `AI WS`, branch `mars/canonical-post-recovery`, i-SEO clean or clean worktree.  
2. Read this charter pack (scope, data model, create/cleanup, write proof, safety).  
3. Implement guarded tool; dump; create; preview; one-block POST; evidence; cleanup.  
4. Do not reopen report 1. Do not touch id 5.  
5. Closeout + OPERATIONAL-INDEX.  
6. Exact-path commit of tool + docs; no push.

---

## 7. Rollback

- Preferred: `--cleanup` using `fixture-ids.json`.  
- Emergency: operator-approved restore from the pre-create dump.  
- Code: revert the committed tool file if needed.

---

## 8. After Implementation 01

Still later / parallel:

- Optional multi-block apply proof  
- Optional exclusion-entry fixture  
- Apply UX refinement (simple vs technical toggle)  
- Metrics model for `results_summary`  
- Client Report Template Visual Alignment  
- Screenshot QA when the operator sends shots  
- Production Environment Operator Decision 01  
- Reopen / Revised Export charter before any issued-report apply

---

## 9. SAFE UNKNOWN

- Whether runtime sync of the CLI tool is required if PHP is run from `app-source/tools/` against runtime `.env.local` (implementation may run from source with env path candidates, matching existing tools).
