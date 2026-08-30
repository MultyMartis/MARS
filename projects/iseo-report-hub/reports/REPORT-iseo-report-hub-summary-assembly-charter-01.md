# REPORT — I-SEO REPORT HUB SUMMARY ASSEMBLY CHARTER 01

**Date:** 2026-08-17  
**project_id:** `iseo-report-hub`  
**Wave:** Summary Assembly Charter 01  
**Verdict:** `SUMMARY ASSEMBLY CHARTER COMPLETE`

Docs / architecture / UX / safety only. No app-source, runtime, DB, share, or PDF mutation.

Primary: `496a56e54b2c28139835b0607c927404365b6392`. Hash-record / tip: this docs commit.

---

## 1. Verdict

`SUMMARY ASSEMBLY CHARTER COMPLETE`

Six client shells stay the assembly surface. Implementation 01 is **preview-only** from `monthly_report_work_entries`. No overwrite of `report_blocks` until a later apply charter.

---

## 2. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Volume | `X:` / `AI WS` |
| Branch (main checkout) | `mars/canonical-post-recovery` |
| HEAD before | `dfe972981d85dfecf8abe99821cec1223d4da2c4` |
| Clean worktree used | **Yes** — `X:\AI MARS STORAGE\git-sync-iseo-report-hub-summary-assembly-charter-01\repo` on `feat/iseo-report-hub-summary-assembly-charter-01` |
| Foreign WIP preserved | **Yes** (main staged foreign index untouched during edits) |
| app-source / runtime / DB | **No changes** |

---

## 3. Current Block Baseline

Canonical table is **`report_blocks`** (not a separate `monthly_report_blocks`). Dual path: flat columns on `monthly_report_contents` plus block rows. Preview prefers `blocks_primary`. Five keys required to finalize; `risks_and_blockers` optional. Finalized monthly report **locks block CRUD** until reopen; snapshots/exports/PDF **do not** auto-update. Work entries may still be edited with a PDF warning. Schema is enough for Option A without migration. Auto-writing blocks on finalized report 1 would fail the lock or, if forced after reopen, desync live preview from the existing client PDF/share.

Doc: `product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-CURRENT-BLOCK-BASELINE-v0.1.md`

---

## 4. Source Rules

Exclusive assignment: risks first, then completed, then next-month plan.

| Block | Auto? | Rule (short) |
|-------|-------|----------------|
| `work_completed` | Yes | `period_role=done` + `status=done` + client_safe/facing |
| `next_month_plan` | Yes | `planned_next` + status planned/in_progress/deferred + client_safe/facing |
| `risks_and_blockers` | Yes | `period_role=risk` or `status=blocked`, visibility ≠ internal |
| `key_findings` | Manual | Optional note-candidates only |
| `results_summary` | Manual | No fake KPIs |
| `executive_summary` | Manual | No auto-prose in Impl 01 |

Global exclude: `cancelled`, `internal`. Never emit `internal_note` / `evidence_note`. Text: `client_summary` then title+short description. Fixture 7: expected 4 / 2 / 1.

Doc: `product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SOURCE-RULES-v0.1.md`

---

## 5. Assembly Mode Decision

| Option | Role |
|--------|------|
| **A Preview-only** | **Recommended Implementation 01** |
| B Draft apply + overwrite protection | Next charter after preview |
| C Versioning/diffs/locks | Later backlog |

Report 1 is finalized and exported; writing shells now would confuse snapshot/share expectations.

Doc: `product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-MODE-OPTIONS-v0.1.md`

---

## 6. UX Flow

- Button **Собрать черновик из работ** on `/monthly-reports/{id}`  
- `GET /monthly-reports/{id}/assembly-preview`  
- Stats + three auto drafts + two/three manual cards  
- Warning: preliminary; does not change report/PDF/snapshots/shares  
- Finalized extra warning  
- **No** save/apply; disabled hint for later apply  
- Empty and internal-exclusion copy in Russian  

Doc: `product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-UX-FLOW-v0.1.md`

---

## 7. Technical Charter

- Service `MonthlyReportSummaryAssemblyService`  
- GET-only `MonthlyReportAssemblyController` (preferred)  
- View `monthly-reports/assembly-preview.php`  
- Existing `listByMonthlyReportId`  
- No migration, no DB writes  

Doc: `product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-TECHNICAL-CHARTER-v0.1.md`

---

## 8. Safety Policy

Option A: no backup-for-write; count check before/after; no POST.  
Future B: dump before apply; no overwrite unless block selected + confirm; preserve old body in evidence; no PDF regen; refuse apply while finalized.

Doc: `product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFETY-POLICY-v0.1.md`

---

## 9. Recommended Next Implementation

**`I-SEO Report Hub — Summary Assembly Preview Implementation 01`**

Acceptance: route 200; drafts for completed/plan/risks from live entries; no block/export/share/PDF mutation; DB counts unchanged.

Later: **Summary Assembly Apply Charter 01**.

Doc: `product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-IMPLEMENTATION-PLAN-v0.1.md`

---

## 10. Docs Created

See §14.

---

## 11. Restrictions Confirmed

- no app-source code edits  
- no runtime edits / sync  
- no DB mutation  
- no share/export/PDF mutation  
- no production  
- no push  
- no secrets printed  

---

## 12. Commit

| Field | Value |
|-------|--------|
| Primary | `496a56e54b2c28139835b0607c927404365b6392` |
| Hash-record | this docs commit |
| Tip HEAD | this docs commit |
| Push | **no** |

---

## 13. SAFE UNKNOWN

- Live `body` strings of the six fixture blocks (not required for preview-only design).  
- Whether apply should ever bypass reopen on finalized reports (default no).  
- Operator click-through notes on the work-entry form (parallel, not this wave).

---

## 14. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-CURRENT-BLOCK-BASELINE-v0.1.md`  
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SOURCE-RULES-v0.1.md`  
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-MODE-OPTIONS-v0.1.md`  
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-UX-FLOW-v0.1.md`  
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-TECHNICAL-CHARTER-v0.1.md`  
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-SAFETY-POLICY-v0.1.md`  
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-SUMMARY-ASSEMBLY-IMPLEMENTATION-PLAN-v0.1.md`  
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-summary-assembly-charter-01.md`  
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`  

---

## 15. Git Actions

Clean worktree exact-path commits; `update-ref` canonical; scoped restore of i-SEO docs paths on main; foreign WIP preserved; **no push**.
