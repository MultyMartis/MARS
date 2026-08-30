# i-SEO Report Hub — Monthly Detail UX Collapse Acceptance v0.1

**Wave:** Monthly Report Detail UX Collapse Charter 01 → Implementation 01  
**Date:** 2026-08-21  
**Route under test:** `GET /monthly-reports/1` (and equivalent `{id}` smoke as needed)

---

## Manager first-screen acceptance

Within the first screen (approx. above-the-fold at 1920 desktop, without expanding technical `<details>`), a manager can identify:

| Question | Pass condition |
|----------|----------------|
| Status | Status badge + finalization state visible |
| What to do next | Primary workflow actions visible |
| Where to edit work | Work entries section visible or one-click `#work-entries` without hunting past diagnostics |
| Where to preview | `Предпросмотр отчета` visible |
| Where to files/share | `Файлы отчета` or compact PDF/link readiness + clear link |

Fail if first screen is still dominated by readiness checklist and status POSTs while work entries / primary actions are below the fold.

---

## Collapse acceptance

- Technical diagnostics (readiness checklist, raw details, source weekly notes, dense blocks table, tech IDs) are **collapsed by default**.  
- Expanding `<details>` reveals the same information previously available (no data removal).  
- Finalized/lock warning remains **open/visible** when applicable.  
- PDF ready / active link indicators remain visible in compact form.

---

## Work entries acceptance

- Section remains accessible and visible (not inside a closed `<details>`).  
- Counters, cards, add/edit affordances still work as before (GET navigation).  
- No requirement to mutate work entries during acceptance testing.

---

## Action safety acceptance

- Dangerous / status-changing actions (submit review, mark reviewed, finalize, reopen, create snapshot) are visually separated from primary GET workflow and/or collapsed under admin/status zone.  
- Disabled actions still show reason when not allowed.  
- Backend allow/deny behavior unchanged.

---

## Safety / immutability acceptance

| Guard | Pass |
|-------|------|
| DB mutation | None (counts/checksums match baseline) |
| Export / share / PDF mutation | None |
| Export 4 | Unchanged |
| P0 fixes | No regression of normal-visible fixture/junk cleanup |
| Secrets / share tokens | Not printed in UI evidence or reports |

---

## Evidence acceptance

| Artifact | Requirement |
|----------|-------------|
| Before | P0 after screenshot `04_monthly_report_1_detail_after.png` (or explicit pre-P1 capture) |
| After | Recapture e.g. `04_monthly_report_1_detail_after_p1.png` under Storage incoming evidence folder for the implementation wave |
| Assertions | Short markdown index + forbidden-string / layout checks |

Screenshots stay under Storage — **not** committed to git.

---

## Verdict vocabulary (implementation wave)

| Verdict | Meaning |
|---------|---------|
| `MONTHLY DETAIL UX COLLAPSE PASS` | All acceptance rows met |
| `MONTHLY DETAIL UX COLLAPSE PASS_WITH_MINOR_ISSUES` | Hierarchy improved; minor residual polish only |
| `MONTHLY DETAIL UX COLLAPSE ATTENTION` | Partial; manager first-screen still unclear or safety risk |
| `STOPPED` | Preflight / safety stop |

---

## Non-acceptance (explicit)

- “Looks tidier” without primary actions + work entries above diagnostics  
- Collapsing work entries by default  
- Hiding finalize without expand path when action remains allowed  
- Any PDF regen / export 4 / share change claimed as UX fix
