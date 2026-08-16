# Source Traceability Matrix — Phase 02

Columns: lesson/pattern · wave · report/source · evidence · reusable scope · confidence · Phase 3 review needed

Confidence: HIGH = multi-report + freeze/release; MED = single-wave solid; LOW = inferred / SAFE UNKNOWN

| Lesson / pattern | Wave | Report / source | Evidence | Reusable scope | Confidence | Phase 3 review |
|------------------|------|-----------------|----------|----------------|------------|----------------|
| Runtime-first operator canon | E56–E63 | E56/E59/E61/E63 reports; RELEASE-MANIFEST | operator-canonization-manifest.csv (E63) | WP visual waves | HIGH | Yes — SOP |
| Promote before mutate | E56+ | PROJECT-STATUS hash notes | per-wave operator-change-manifest | WP | HIGH | Yes |
| Exact-file delivery | E54–E63 | multiple reports | hashes.csv per wave | WP | HIGH | No |
| No broad sync | E62C/E63 | ACF disposition | disposition table | WP ACF | HIGH | Yes |
| Options admin DOM ≠ post admin | E55 | E55 report | admin screenshots evidence | WP admin CSS | HIGH | No |
| Freeze before visual audit | E58 | FREEZE-E58; E58 reports | freeze backup path | WP | HIGH | No |
| Audit false positives via remeasure | E58-FU01 | FU01 decision pack | decision-summary.csv | visual QA | HIGH | Yes |
| Operator confirms subset of findings | E58→E59 | FU01 + E59 | VA-001 only | visual QA | HIGH | No |
| Visual authority hierarchy | E58/E60-FIX01 | this pack + FIX01 | E58 operator-edits CSS | design ops | HIGH | Yes |
| Freeze as selector authority | E60-FIX01 | E60-FIX01 report | stable-current-final-computed-matrix.csv | CSS repair | HIGH | Yes |
| Global hover vs component hover | E60/FIX01 | E60 reports | rule extraction txt | FE CSS | HIGH | Yes |
| Shared CTA without nested section | E60/E62C | E62C report | DOM before/after | FE partials | HIGH | No |
| Contacts locations ownership | E59/FIX01 | E59 reports | ACF seed evidence | admin ownership | HIGH | No |
| Dormant meta retention | E59-FIX01 | E59-FIX01 | field removal notes | ACF | HIGH | Yes |
| Breadcrumb toggles + empty shell | E61 | E61 report | FE smoke | FE/admin | HIGH | No |
| Reviews = options repeater not CPT | E62B/C | E62B/C; REVIEWS-STABLE-UID doc | demo-content-inventory.json | data model | HIGH | Yes |
| Stable review UID anchors | E62C | E62C; UID doc | reorder test evidence | repeaters | HIGH | No |
| Hide legacy via active:false | E62C | E62C; SERVICE-ADMIN-HIDDEN doc | ACF JSON active false | ACF | HIGH | Yes |
| Program mini-desc page ownership | E62D | E62D report | seed table #1053–1056 | ownership | HIGH | No |
| 404 Figma metrics + decor asset | E62A/D/E | E62* reports | screenshots | FE | HIGH | No |
| Search trigger placement product design | E62E-FIX01 | FIX01 report | search-breadcrumb-dom-before-after.md | search UX | HIGH | Yes |
| Phone mask cross-project reuse | E62A | E62A report | mask JS | forms | MED | Yes — validate 2nd project |
| Lifebuoy motion iterative tuning | E57* | E57 reports | motion evidence | motion | MED | No |
| Libertinus wait for operator asset | E56-FU02 | FU02 report | font path | assets | HIGH | No |
| Oversized wave → PARTIAL | E56/E61 | E56/E61 reports | open tails lists | process | HIGH | Yes |
| Dual status LOCAL vs OP accept | E54–E62 | timeline marks | status tables | process | HIGH | Yes |
| Tail ledger at Stable | E63 | E63; tail-ledger.md | evidence/v9-06e63-… | release | HIGH | Yes |
| Clean-worktree exact allowlist push | E63 | E63 closeout; STABLE-V1 git docs | Storage git-sync path | MARS Git | HIGH | Yes |
| Content commit ≠ remote tip | E63 | E63 §§11–12 | d1befe9b vs 9d5dcc28 | MARS Git | HIGH | No |
| Source-only ACF retain | E63 | ACF disposition | 8 groups table | ACF | HIGH | Yes |
| Demo content deferred | E62C/E63 | DEMO-CONTENT-CLEANUP backlog | inventory JSON | content | HIGH | Yes — after prod |
| SMTP mandatory pre-prod | E63 | DEFERRED-WORK; checklist | — | launch | HIGH | Yes — after SMTP |
| ACF Extended DB dup inventory | E63 | disposition SAFE UNKNOWN | — | ACF | LOW | Yes |
| Specialists permanent underline hover | E60 | E60 report SAFE UNKNOWN | — | FE | LOW | Yes |
| Pre-E54 backup retention detail | — | inventory advisory | backup root listing | cleanup | MED | Yes after cleanup |

**Matrix size:** 40 rows  
**SAFE UNKNOWN rows:** ACF Extended duplicates; specialists underline hover intent; detailed pre-E54 size map beyond samples
