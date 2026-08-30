# I-SEO Report Hub — Summary Assembly Implementation Plan v0.1

**Status:** PLAN FOR NEXT IMPLEMENTATION — **do not implement in this wave**  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Charter 01

---

## 1. Next wave (recommended)

**Name:** `I-SEO Report Hub — Summary Assembly Preview Implementation 01`

**Mode:** Option A — preview-only.

**Not next:** PDF/template alignment, screenshot QA of all pages, production, apply/overwrite.

Operator may still do a **manual form click-through** of the work-entry editor in parallel; it is not a blocker for this preview wave.

---

## 2. Scope in

- `MonthlyReportSummaryAssemblyService` (classify + format; SELECT only)  
- `MonthlyReportAssemblyController::preview` (or equivalent GET action)  
- Route `GET /monthly-reports/{id}/assembly-preview`  
- View `assembly-preview.php` (+ optional partial)  
- CTA on monthly work-entries partial  
- `bootstrap.php` / `routes.php` wiring  
- Exact source → runtime sync of those files only  
- GET smoke + count invariance  

---

## 3. Scope out

- POST / apply / CSRF forms for assembly  
- Migration  
- `report_blocks` writes  
- Reopen / finalize  
- Snapshot / export / share / PDF  
- Executive/results auto-prose  
- Metrics  
- WordPress / production  

---

## 4. Prompt outline (for the implementation agent)

Copy-adapt this charter pack:

1. Preflight: volume `AI WS`, branch `mars/canonical-post-recovery`, i-SEO scope clean or clean worktree.  
2. Read Source Rules, UX Flow, Technical Charter, Safety Policy.  
3. Implement GET-only surface.  
4. Do not POST.  
5. Smoke report id **1**.  
6. Assert DB counts unchanged.  
7. Closeout report + OPERATIONAL-INDEX.  
8. Exact-path commit; no push.

---

## 5. Acceptance

| Check | Pass if |
|-------|---------|
| Route | `GET /monthly-reports/1/assembly-preview` → **200** |
| Drafts | `work_completed` / `next_month_plan` / `risks_and_blockers` populated from live entries (fixture expectation 4 / 2 / 1 if seeds unchanged) |
| Manual | Executive + results (+ findings) shown as manual, not invented KPI/prose |
| Warning | Copy that assembly does not change report / PDF / snapshots / shares |
| Apply | No working save/apply |
| DB | entries_r1 **7**; blocks **6**; exports **4**; shares **7**; active **1**; revoked **6** |
| PDF | Unchanged; export 4 checksum prefix `a8c4d61c6216e8d70b19` if verified |
| Code | No migration; no POST assembly route |

---

## 6. After Implementation 01

**Recommended:** `I-SEO Report Hub — Summary Assembly Apply Charter 01`  
(design Option B: backup, reopen policy, per-block confirm, evidence of old body)

Only after that charter: `Summary Assembly Apply Implementation 01`.

**Still later:** Client Report Template Visual Alignment; screenshot QA when the operator sends page shots; production environment decision.

---

## 7. Rollback (Implementation 01)

If the preview wave misbehaves: revert the exact committed app-source files; runtime sync those reversions. No DB rollback needed if Safety Policy was kept (no writes).

---

## 8. SAFE UNKNOWN

- Whether apply charter is needed immediately after preview or after operator click-through notes.
