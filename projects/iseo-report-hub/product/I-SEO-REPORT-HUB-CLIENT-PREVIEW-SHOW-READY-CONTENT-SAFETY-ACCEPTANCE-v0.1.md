# I-SEO Report Hub — Client Preview Show-ready Content Safety & Acceptance v0.1

**Status:** safety / acceptance charter (docs only)  
**Date:** 2026-08-21  
**Applies to:** Client Preview Show-ready Content Implementation 01 (Option A)

---

## 1. Hard freezes

| Freeze | Rule |
|--------|------|
| DB | No INSERT/UPDATE/DELETE on product tables |
| Report 1 | No reopen, finalize, block edit, content edit, snapshot |
| Report 5 | No seed, no block create, no work-entry insert |
| Export 4 | Frozen — no regenerate, no overwrite, no new export for this polish |
| Shares | No create/revoke/change; no token printing |
| PDF | No regeneration |
| Public share route | No mutation |
| Production | Out of scope |

Export 4 context (do not change):

- size context: `117055`
- checksum prefix context: `a8c4d61c6216`

---

## 2. Content safety rules

| Rule | Detail |
|------|--------|
| Fallback location | Render-layer / local-demo only |
| No fake metrics | No invented traffic, positions, leads, or KPI tables |
| No junk placeholders | No `updated body`, `test body`, lorem, fixture markers in visible demo text |
| Report 5 | Must keep calm empty draft; must not receive show-ready pack |
| Preview ≠ export | Demo overlay must not write into export/PDF artifacts |
| Honesty | Results section must state MVP metrics are not auto-filled |

---

## 3. Regression guards

Must remain accepted:

- Report 1 manager monthly detail (P1 collapse)
- Report 5 empty draft UX (Report 5 cleanup)
- `/health` Local MVP refresh
- P0 sanitizer behavior on non-demo / junk paths
- Client document layout (paper, section order, no admin chrome)

---

## 4. Acceptance criteria (Implementation 01)

### Pass when all true

1. Report 1 client preview looks like a **credible SEO report demo**.
2. All **six** sections have useful client-safe text (not generic “will be filled later” empties).
3. No obvious test/fixture placeholders in normal-visible preview.
4. No fake KPI numbers.
5. Report 5 preview still shows calm empty states.
6. Health still OK.
7. DB unchanged; export 4 unchanged; shares unchanged.
8. Before/after screenshots captured for preview, print, and report 5 regression.

### Fail / STOP when

- Any PDF/export/share mutation occurs.
- Report 1 or 5 DB bodies change.
- Demo pack leaks onto report 5.
- Fake metrics introduced.
- Export 4 size/checksum drifts.

---

## 5. Evidence required in Implementation 01

- HTTP GET status matrix for preview/print/report 5/health.
- Read-only confirmation of export/share counts (no tokens printed).
- Screenshots listed in implementation scope.
- Short result product doc + closeout report.

---

## 6. Separate future waves (not this acceptance)

If operator later wants DB-persisted content:

- New charter: local-only Option B with backup + reopen policy.
- Still defer PDF regen until explicit confirm.
- Do not treat DB fill as part of Show-ready Content Implementation 01.
