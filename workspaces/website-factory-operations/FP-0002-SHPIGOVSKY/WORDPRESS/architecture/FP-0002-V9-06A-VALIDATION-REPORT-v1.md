# FP-0002 V9-06A Validation Report v1

**Task:** V9-06A / V9-06A.1 | **Date:** 2026-07-03

| # | Rule | Result |
|---|------|--------|
| 1 | All 31 V9 routes mapped | PASS |
| 2 | No ambiguous route without explicit review flag | PASS |
| 3 | Every entity has one owner | PASS |
| 4 | Every template family has PHP target | PASS |
| 5 | Every reusable section has ownership classification | PASS |
| 6 | Every custom field has documented reason | PASS |
| 7 | Native-field alternatives evaluated | PASS |
| 8 | No unrestricted page builder | PASS |
| 9 | No duplicate Blog entity | PASS |
| 10 | No duplicate WPilot responsibility | PASS |
| 11 | No project logic in MU-plugin | PASS |
| 12 | No visual layout in project plugin | PASS |
| 13 | All current foundation objects classified | PASS |
| 14 | Operator decisions integrated (OD-001–004) | PASS |
| 15 | Runtime changes = 0 | PASS |
| 16 | V9 src unchanged | PASS |
| 17 | V9 dist unchanged | PASS |
| 18 | Service CPT evaluated with reasoning | PASS |
| 19 | Service taxonomy evaluated | PASS |
| 20 | Header/footer shared globally designed | PASS |
| 21 | Home model defined | PASS |
| 22 | Legal DEMO handling defined | PASS |
| 23 | Alcohol special variant preserved | PASS |
| 24 | Forbidden genotyping route addressed | PASS |
| 25 | Migration plan for Page→Service | PASS |
| 26 | ACF Pro required (OD-001) | PASS |
| 27 | Form boundary defined | PASS |
| 28 | SEO boundary defined | PASS |
| 29 | Implementation sequence defined | PASS |
| 30 | Theme/plugin skeleton planned | PASS |
| 31 | Route classification reconciled (primary + subtype) | PASS |
| 32 | Service entity registry 15 verified | PASS |
| 33 | Service permalink contract defined | PASS |
| 34 | BoundedMeta primary path rejected | PASS |
| 35 | Blog categories none at launch | PASS |
| 36 | Blog author hidden / date visible | PASS |
| 37 | `/specyalisty/` redirect decision fixed | PASS |
| 38 | Architecture artefacts cross-reference integrity | PASS |
| 39 | Machine validation script PASS | PASS |

**Total checks:** 39  
**Passed:** 39  
**Failed:** 0  

**Result:** PASS

---

## V9-06A.1 reconciliation notes

- Route primary classes sum to 31 (PAGE 14, SERVICE 15, POST 1, POSTS_PAGE 1).
- Legal routes use primary `PAGE` + subtype `legal` — not `LEGAL_PAGE`.
- 4 legal routes carry `unresolved: LEGAL_DEMO_TOKENS` — expected production blocker, not mapping failure.
- Foundation exclusion `/uslugi/genotipirovanie/` in `foundation_exclusions` — not a canonical route.
- ACF Pro required; V9-06C blocked until ACF Pro package prerequisite satisfied.
- V9-06B ready for operator authorization (architecture approved).

---

*Supersedes V9-06A validation count; see FP-0002-V9-06A1-ARCHITECTURE-RECONCILIATION-REPORT-v1.md.*
