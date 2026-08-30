# REPORT — I-SEO REPORT HUB SPECIALIST REPORT CONTENT WORKFLOW CHARTER 01

**Date:** 2026-08-26  
**Verdict:** SPECIALIST CONTENT WORKFLOW CHARTER COMPLETE  
**Primary commit:** 6f2f13faaf37e0047f2d3940ffbb957533b8ecf2  
**Hash-record commit:** 3b954bfd3dc52e3f385067002a94f58ba89898f0  
**Tip HEAD:** 1c26c0fb3b7f3fc894d516c696b87639ad49d95e  
**Push:** no

## 1. Verdict

SPECIALIST CONTENT WORKFLOW CHARTER COMPLETE

Charter recommends **Option D — Hybrid MVP**: work entries + specialist-friendly section editor + assembly hints; write safe `report_blocks` text mirrored to flat columns; no migration; next = Implementation 01. No app/DB/host mutation in this wave.

## 2. Execution Verification

- Repo root: `X:\AI MARS`
- Volume: `AI WS` (`X:`)
- Branch (main tree): `mars/canonical-post-recovery`
- HEAD before: `a1a000c464a1815b3789f9ad9a6158ba012fba2a`
- Clean worktree: `X:\AI MARS STORAGE\git-sync-iseo-report-hub-specialist-report-content-workflow-charter-01\repo` on branch `docs/iseo-specialist-content-workflow-charter-01`
- Foreign WIP preserved on main working tree (e.g. `projects/iseo-su-site-ops/*` modified; staged empty)
- i-SEO scope clean before start
- Runtime/DB: read-only inspection only

## 3. Current Content Flow Audit

- Client preview: `ReportPreviewService::assemble` → `ClientReportDocument`; **blocks_primary** when blocks exist (true for monthly 7/8).
- Flat fields on `monthly_report_contents` are fallback + detail status; not primary for 7/8 preview.
- Work entries classified by `MonthlyReportSummaryAssemblyService`; apply writes `report_blocks.body` for auto keys (`admin_owner` / `seo_lead_reviewer` only).
- Specialist: work entries + preview yes; raw block edit denied; assembly CTA hidden in specialist flow; monthly/block `SPECIALIST_EDIT_ROLES = []`.
- Demo: monthly 7 finalized (12 entries, 6 blocks); monthly 8 in_progress (11 entries, 6 blocks); snapshots/exports/shares = 0.

## 4. Role Boundary Decision

Specialist may edit allowed client-facing texts via **friendly** content workflow on non-finalized reports; must not see technical block fields; must not finalize/PDF/share. Lead/admin retain raw editor, assembly apply, finalization.

## 5. Options Compared

| Option | Summary | Result |
|--------|---------|--------|
| A | Work entries only | Rejected — no specialist text ownership |
| B | Friendly editor only | Viable but weaker than hybrid |
| C | Assembly only | Incomplete for manual sections |
| D | Hybrid | **Recommended** |

## 6. Recommended MVP Workflow

August detail → **Тексты отчета** → `/monthly-reports/{id}/content-workflow` → section cards with optional assembly draft hints → per-section save → client preview. July read-only for specialist.

## 7. Section Policy

Six client preview sections specialist-editable on in-progress; auto trio hintable from work entries; `client_notes` / `internal_notes` deferred from specialist MVP page (not in `ClientReportDocument` today for notes).

## 8. Data / Write Model

**Approach 2+:** update existing `report_blocks.body` for stable keys; mirror to flat `monthly_report_contents` column; no new table; no migration; backup before Implementation 01 writes.

## 9. Status / Locking Policy

In-progress: specialist edit allowed. Finalized: specialist read-only / mutation denied. Privileged: existing admin locks + reopen path.

## 10. Implementation Plan

Documented in `product/I-SEO-REPORT-HUB-SPECIALIST-CONTENT-WORKFLOW-IMPLEMENTATION-PLAN-v0.1.md`.

## 11. Acceptance Criteria

Specialist CTA + friendly page + save one August section + preview reflects + July locked + raw edit still 403 + backup + no PDF/share/host.

## 12. Risks / Deferred Items

PDF/export/share parked; production config paused; work-entry help density optional; AI summaries out; metrics integrity for real clients; dual-write drift risk; demo invented metrics remain local-only.

## 13. Docs Created

- `product/I-SEO-REPORT-HUB-SPECIALIST-REPORT-CONTENT-WORKFLOW-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-SPECIALIST-CONTENT-WORKFLOW-IMPLEMENTATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-specialist-report-content-workflow-charter-01.md`
- `OPERATIONAL-INDEX.md` (updated)

## 14. Evidence

`X:\AI MARS STORAGE\incoming\iseo-report-hub\specialist-report-content-workflow-charter-01\20260826-222706\` (not committed)

## 15. Safety

- DB changed: **no**
- Runtime files changed: **no**
- App-source changed: **no**
- Host touched: **no**
- PDF/export/share created: **no**
- Secrets printed: **no**

## 16. Commit

- primary: 6f2f13faaf37e0047f2d3940ffbb957533b8ecf2
- hash-record: 3b954bfd3dc52e3f385067002a94f58ba89898f0
- tip HEAD: 1c26c0fb3b7f3fc894d516c696b87639ad49d95e
- push: **no**

## 17. SAFE UNKNOWN

- Whether Implementation 01 should include client-side-only «Подставить черновик» vs server endpoint for assembly fill — product default: client/textarea fill without auto-apply write until Save.
- Exact August block ids may shift if demo reseeded later; keys are stable, not ids.
- Admin visual of new page not designed beyond specialist MVP.

## 18. Recommended Next Action

`I-SEO Report Hub — Specialist Report Content Workflow Implementation 01`

## 19. Files Changed

Exact allowlisted docs only (see §13).

## 20. Git Actions

Docs commit(s) from clean worktree; cherry-pick onto `mars/canonical-post-recovery`; canonical hash sync / tip-lock commits; **no push**.
