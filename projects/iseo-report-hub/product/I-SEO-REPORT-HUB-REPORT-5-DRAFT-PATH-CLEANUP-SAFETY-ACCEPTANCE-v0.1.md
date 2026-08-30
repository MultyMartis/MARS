# i-SEO Report Hub — Report 5 Draft Path Cleanup Safety & Acceptance v0.1

**Wave:** Report 5 Draft Path Cleanup Charter 01  
**Applies to next:** `I-SEO Report Hub — Report 5 Draft Path Cleanup Implementation 01`  
**Date:** 2026-08-21

---

## Safety invariants (must hold before and after implementation)

| Invariant | Requirement |
|-----------|-------------|
| DB mutation | **None** |
| Report 5 data mutation | **None** (no status/title/content/block/entry writes) |
| Fake seed | **None** |
| Delete report 5 | **Forbidden** |
| Report 1 | **Unaffected** (still finalized; 6 blocks; 7 entries) |
| Export / share / PDF | **Unchanged**; no regeneration |
| Export 4 | Size `117055` and checksum prefix `a8c4d61c6216` unchanged |
| Share tokens | Never printed |
| P0 sanitizer | No regression of forbidden normal-visible strings |
| P1 monthly detail IA on report 1 | No regression of manager workspace collapse |
| Production / WordPress / i-seo.su | Untouched |
| Runtime sync | Exact allowlist only (implementation wave) |

---

## Acceptance criteria (implementation wave)

1. **Report 5 no longer looks broken** — reads as intentional empty draft, not smoke debris.  
2. **Empty state tells the operator what to do** — clear message + primary GET actions (add work / blocks / back to period).  
3. **Preview shows calm empty sections** — no numeric/test junk in normal-visible client preview.  
4. **Period monthly card clearly marks empty draft** — `Пустой черновик` or `Черновик без работ` (or equivalent approved copy).  
5. **No technical/junk text in normal UI** — fixture markers / junk absent outside allowed residuals (edit textareas / collapsed tech details per P0).  
6. **Diagnostics not first impression** — readiness remains collapsed; empty-draft summary states not-ready calmly.  
7. **Report 1 demo path remains primary and intact.**  
8. **Immutability checks pass** — DB/export/share/PDF baselines unchanged.  
9. **Before/after screenshots** captured under Storage (not committed).

---

## Suggested before/after evidence map

| Surface | Before (existing) | After (impl wave) |
|---------|-------------------|-------------------|
| Preview | `...\screenshot-qa-p0-fix-implementation-01\20260821-023143\15_monthly_report_5_preview_after.png` | `15_monthly_report_5_preview_after_cleanup.png` |
| Empty detail | `...\automated-screenshot-capture-01\20260821-010501\14_monthly_report_5_empty.png` (+ post-P1 inferred) | `14_monthly_report_5_empty_after_cleanup.png` |
| Periods list | `...\20260821-023143\03_reporting_periods_after.png` | `03_reporting_periods_after_report5_cleanup.png` |

---

## Fail conditions (implementation must not ship)

- Any SQL write / seed / delete  
- Export 4 or share row change  
- Report 1 layout/content regression  
- Reintroduction of P0 forbidden strings on normal-visible pages  
- Making finalization checklist the default open first screen on empty draft  

---

## Operator sign-off (implementation)

- [ ] Empty draft framing accepted on `/monthly-reports/5`  
- [ ] Preview accepted as calm empty draft  
- [ ] Period demotion label accepted  
- [ ] Immutability evidence accepted  
- [ ] Ready for optional later data-seed charter (Option C) — **optional, separate**  
