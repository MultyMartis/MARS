# I-SEO Report Hub — Summary Assembly Apply Implementation Plan v0.1

**Status:** PLAN FOR NEXT IMPLEMENTATION — **do not implement in this wave**  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Apply Charter 01

---

## 1. Next wave (recommended)

**Name:** `I-SEO Report Hub — Summary Assembly Apply Implementation 01`

**Not next:** Apply Preflight 01. Discovery + fallback are specified in the Test Strategy, so implementation can land controls + POST refuse on report 1 without a separate preflight wave.

**Not next:** fixture seed for monthly id 5; reopen report 1; PDF; Client Report Template Visual Alignment; screenshot QA of all pages; production.

---

## 2. Scope in

- `formatApplyBody` on `MonthlyReportSummaryAssemblyService`
- `MonthlyReportSummaryApplyService`
- `MonthlyReportAssemblyController::apply`
- `POST /monthly-reports/{id}/assembly-apply`
- Preview UI: client draft, current vs generated, selection, confirm, disabled finalized state
- Narrow `report_blocks` UPDATE helper
- `bootstrap.php` / `routes.php` / CSS as needed
- Exact source → runtime sync of those files only
- GET preview regression on report 1
- POST refuse smoke on report 1
- Option D write smoke **only if** a safe non-finalized target exists at impl time

---

## 3. Scope out

- Reopen / finalize
- INSERT `report_blocks` / seed report 5
- `summary` rewrite
- Manual-only keys
- Snapshot / export / share / PDF
- Migration
- Work-entry writes
- Specialist apply role

---

## 4. Acceptance

| Check | Pass if |
|-------|---------|
| Preview | `GET /monthly-reports/1/assembly-preview` still **200**; still maps 4 / 2 / 1 if seeds unchanged |
| Finalized UI | Apply controls **disabled**; finalized explanation visible; **no** working write form |
| POST report 1 | Refused; blocks_r1 unchanged; monthly still `finalized` |
| Manual keys | Cannot be applied |
| DB report 1 | entries **7**; blocks **6**; exports **4**; shares **7** active **1** revoked **6** |
| PDF | Unchanged; export 4 checksum prefix `a8c4d61c6216e8d70b19` if re-read |
| Write proof | If safe target exists: one selected block updated, old body in evidence, unselected blocks untouched |
| Write proof absent | Verdict `PASS_WITH_LIMITED_WRITE_PROOF`; no successful UPDATE |

---

## 5. Prompt outline (implementation agent)

1. Preflight: volume `AI WS`, branch `mars/canonical-post-recovery`, i-SEO scope clean or clean worktree.  
2. Read Apply Scope, Finalized Policy, Block Text Contract, Apply UX, Technical Charter, Test Strategy, Safety Policy.  
3. Implement POST + UI.  
4. Discover safe target; if none, fallback A.  
5. Dump before any successful POST.  
6. Do not reopen report 1.  
7. Closeout + OPERATIONAL-INDEX.  
8. Exact-path commit; no push.

---

## 6. Rollback (implementation)

Revert exact committed app-source files; runtime sync those reversions. If a write occurred: restore from dump or captured old row values.

---

## 7. After Implementation 01

Still later / parallel:

- Client Report Template Visual Alignment  
- Screenshot QA when the operator sends page shots  
- Production Environment Operator Decision 01  
- Optional fixture charter **only if** write-proof is required next  
- Reopen / Revised Export charter before touching issued report 1

---

## 8. SAFE UNKNOWN

- Whether the operator will demand a fixture seed immediately after limited write proof. Default: wait for explicit charter.
