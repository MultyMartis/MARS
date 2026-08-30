# I-SEO Report Hub — Work Entry Editor Implementation Plan v0.1

**Status:** CHARTER / SEQUENCE — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Work Entry Editor Charter 01  
**Next wave name:** `I-SEO Report Hub — Work Entry Editor Implementation 01`

---

## 1. Wave identity

| Field | Value |
|-------|-------|
| Name | I-SEO Report Hub — Work Entry Editor Implementation 01 |
| Type | app-source implementation + runtime sync + local POST smoke |
| Branch / git | Canonical `mars/canonical-post-recovery` via clean worktree if foreign WIP exists |
| Push | no (unless a later operator charter) |
| Production | no |

Depends on: this charter pack + Work Entry UI PASS + DB-11 applied.

---

## 2. Implementation prompt outline (copy-forward)

The next operator prompt should require, in order:

### A. Preflight

- Volume `AI WS` / `X:\AI MARS` / branch check.  
- Foreign WIP preserved; i-SEO scope clean or use  
  `X:\AI MARS STORAGE\git-sync-iseo-report-hub-work-entry-editor-implementation-01\repo`.  
- Confirm HEAD is this charter tip or later canonical.  
- Read Scope, UX Flows, Field Contract, Technical Charter, Safety Policy.

### B. Backup (before any POST)

- Dump to  
  `X:\AI MARS STORAGE\incoming\iseo-report-hub\work-entry-editor-implementation-01\backup\`  
- Full DB + `monthly_report_work_entries` table dump.  
- STOP if dump fails.

### C. Code (exact files)

- `MonthlyReportWorkEntryController`  
- Optional thin `MonthlyReportWorkEntryService`  
- Repository `create` / `update`  
- Routes (create GET/POST, edit GET/POST); **no DELETE**  
- Views: create / edit / form partial  
- Partial `monthly-work-entries.php` CTAs  
- Show controller flags/notices  
- CSS/UiLabels only as needed  
- **No migration, no seed, no `.env`**

### D. Runtime sync

- Exact allowlist source →  
  `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`  
- No storage/export/PDF/env sync.

### E. POST smoke (Option D default)

1. Before: entries_r1=7; blocks=6; exports=4; shares=7 (active 1 / revoked 6); export4 prefix `a8c4d61c6216e8d70b19`.  
2. Auth as local test user (do not print password).  
3. GET create 200.  
4. POST create title `MARS TEST — редактор работ` (catalogue or manual).  
5. POST edit → `deferred` + `internal`.  
6. Confirm list shows the test card.  
7. SQL DELETE that one row by id+title+report_id LIMIT 1.  
8. After: entries_r1=7 again.  
9. Assert share/export/PDF freeze.  
10. Assert no delete route.  
11. PHP lint + HTTP smoke of existing routes.

Operator may override to Option A (keep row) or B (full restore) in the implementation prompt. Default = **D**.

### F. Evidence (not git)

Under  
`X:\AI MARS STORAGE\incoming\iseo-report-hub\work-entry-editor-implementation-01\`  
(backup, smoke log, optional HTML capture). No secrets.

### G. Docs + commit

- Result product doc + closeout report + OPERATIONAL-INDEX.  
- Exact-path commit, e.g. `feat(iseo-report-hub): add monthly work entry editor`.  
- Optional hash-record docs commit.  
- No push.

---

## 3. Expected mutation scope

| Object | Expected |
|--------|----------|
| App-source | Editor files as listed |
| Runtime | Same allowlist |
| DB during smoke | +1 then −1 work entry on report 1 (net 0) if Option D |
| DB final (Option D) | entries_r1 **7**; catalogue 13/31; blocks 6 |
| Shares / exports / PDF | unchanged |
| monthly_report_contents.status | unchanged (still finalized; no reopen) |

---

## 4. Acceptance

`WORK ENTRY EDITOR PASS` only if:

1. Create and edit forms work with CSRF/auth.  
2. Catalogue-linked and manual paths both possible (at least one exercised; the other covered by form+validation).  
3. No physical delete UI/route.  
4. Seeded fixtures not rewritten.  
5. Final fixture count matches chosen option (7 for D/B, 8 for A) and is documented.  
6. Six client shells still listed; PDF/share freeze holds.  
7. Russian labels; warnings present; no token URLs on editor pages.  
8. Runtime matches source allowlist.

Fail / ATTENTION if share/export drift, seed edits, or a DELETE route shipped.

---

## 5. After Implementation 01

**Next product wave (recommended):** `Monthly Report Summary Assembly Implementation 01` (or a short assembly **charter** if mapping to 6 shells still needs HITL).

**Not next:** Client Report Template Visual Alignment; screenshot QA of all pages (operator will send screenshots later); Production Environment Decision remains a parallel track.

---

## 6. Sequence reminder (Nikita track)

1. Catalogue model — **done**  
2. Work entry UI (read-only) — **done**  
3. **Work entry editor** — this plan’s implementation wave  
4. Summary assembly into 6 shells  
5. Client template visual alignment / PDF  

Weekly checkpoints stay free-text until a later charter.
