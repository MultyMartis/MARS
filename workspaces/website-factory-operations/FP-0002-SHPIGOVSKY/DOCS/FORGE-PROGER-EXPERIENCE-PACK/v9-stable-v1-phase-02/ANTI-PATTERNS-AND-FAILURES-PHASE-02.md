# Anti-Patterns and Failures — Phase 02 (E54–E63)

Each item: symptom → root cause → impact → detection → corrected approach → prevention rule.  
Complements Phase 1 `ANTI-PATTERNS-AND-FAILURES.md` (does not replace it).

---

## 1. Claiming typography restored when only E58 values already matched / wrong property fixed

| | |
|--|--|
| **Symptom** | Report says nav/breadcrumb typography restored or unchanged-OK while operator still sees wrong crumb hover / Reviews name weight |
| **Root cause** | Conflating font-size/line-height with hover color or element semantics (`h2` vs `div`) |
| **Impact** | False confidence; FIX wave required (E60-FIX01) |
| **Detection** | Computed-style matrix per selector + viewport; compare hover rules explicitly |
| **Corrected** | Restore E58 hover `accent`; change Reviews name element |
| **Prevention** | Property-level claims only; never “typography OK” as umbrella |

---

## 2. Using a backup that already contained the unwanted state

| | |
|--|--|
| **Symptom** | “Restored from backup” still looks wrong |
| **Root cause** | Backup timestamp after regression, or wrong artifact chosen |
| **Impact** | Wasted cycle; possible further damage if full restore |
| **Detection** | Diff target selectors against a **named accepted** freeze (E58), not “latest backup” |
| **Corrected** | E60-FIX01 used E58 freeze `operator-edits` CSS as authority |
| **Prevention** | Charter must name exact freeze path + file |

---

## 3. Broad requests → oversized mixed waves

| | |
|--|--|
| **Symptom** | E56 / E61 PARTIAL; unfinished tails; weak screenshot coverage |
| **Root cause** | Multiple unrelated admin/FE/content goals in one charter |
| **Impact** | Hidden defects; “pass” with open follow-ups |
| **Detection** | Tail ledger non-empty at report end |
| **Corrected** | Split into E62A–E62E; Stable closeout with explicit deferred |
| **Prevention** | One primary job per wave; hard tail section mandatory |

---

## 4. Nested CTA `<section>` inside section

| | |
|--|--|
| **Symptom** | `#who-we-treat` contains nested `<section class="program-cta-band-section">` |
| **Root cause** | Shared CTA helper default `wrap_section=true` in nested context |
| **Impact** | Invalid/confusing outline; duplicate heading risk |
| **Detection** | DOM assert for nested section; HTML outline check |
| **Corrected** | E62C: `wrap_section=false` → `<div class="program-cta-band">` |
| **Prevention** | Nested-section detector capability; wrapper flags per call site |

---

## 5. Index-based Review anchors

| | |
|--|--|
| **Symptom** | Slider links to `#review-1` break after reorder/pagination |
| **Root cause** | Public ID = row index |
| **Impact** | Deep links unstable |
| **Detection** | Reorder test |
| **Corrected** | E62C `review_uid` stable IDs |
| **Prevention** | Stable repeater UID utility as default for public anchors |

---

## 6. Hardcoded Home mini-descriptions

| | |
|--|--|
| **Symptom** | Program cards editable only in PHP helpers |
| **Root cause** | Temporary hardcoded texts left as permanent SoT |
| **Impact** | Admin cannot manage; seed debt |
| **Detection** | Ownership audit: FE string not mapped to ACF |
| **Corrected** | E62D page ACF + seed + remove hardcoded arrays |
| **Prevention** | Ownership matrix before Home polish waves |

---

## 7. Duplicate content ownership in Blog admin

| | |
|--|--|
| **Symptom** | Blog page ACF duplicates what posts already own |
| **Root cause** | Page-archive fields mixed with post content model |
| **Impact** | Editor confusion; drift |
| **Detection** | Admin UX review; field inventory vs FE data source |
| **Corrected** | E61 simplify archive admin; posts remain content SoT |
| **Prevention** | Page vs CPT ownership rules in admin parity design |

---

## 8. Search triggers where operator did not want them

| | |
|--|--|
| **Symptom** | Search toggle on floating header / mobile bar |
| **Root cause** | Assumed “search everywhere” chrome completeness |
| **Impact** | Operator rejection; FIX01 removal |
| **Detection** | Explicit placement matrix in charter |
| **Corrected** | E62E-FIX01: desktop header only; mobile offcanvas link |
| **Prevention** | Trigger ownership table before implementation |

---

## 9. Assuming Reviews are a CPT

| | |
|--|--|
| **Symptom** | Wrong admin/FE assumptions; wrong cleanup mental model |
| **Root cause** | Naming (“reviews archive”) suggests CPT |
| **Impact** | Bad tooling choices; anchor/seed mistakes |
| **Detection** | Options page `fp02-reviews` + repeater inventory |
| **Corrected** | Documented in E62B/E62C + `REVIEWS-STABLE-UID-ANCHORS-v1.md` |
| **Prevention** | Data-model one-liner at top of every Reviews task |

---

## 10. Incomplete admin screenshot validation

| | |
|--|--|
| **Symptom** | E61 PARTIAL — FE smoke OK, admin UI shots missing |
| **Root cause** | Time pressure / oversized wave |
| **Impact** | Cannot prove Olga-facing UX |
| **Detection** | Evidence checklist requires admin screenshots for admin waves |
| **Corrected** | Later waves added stronger viewport packs; Stable reused lineage |
| **Prevention** | Admin wave Definition of Done includes screenshot set |

---

## 11. Saying “No follow-up needed” despite open tails

| | |
|--|--|
| **Symptom** | Report closes while nested CTA / demos / Founder gaps remain |
| **Root cause** | Confusing local PASS with product completeness |
| **Impact** | Operator surprises; rushed mega-FIX later |
| **Detection** | Tail ledger mandatory section |
| **Corrected** | E62*/E63 explicit dispositions |
| **Prevention** | Ban “no follow-up” if ledger has OPEN items |

---

## 12. Treating every local PASS as operator acceptance

| | |
|--|--|
| **Symptom** | Multiple E54–E62 reports OP_PENDING while marked PASS |
| **Root cause** | Validation language overclaim |
| **Impact** | False freeze readiness |
| **Detection** | Status table must separate Overall vs Operator review |
| **Corrected** | E63 records operator acceptance for Stable |
| **Prevention** | Dual status fields always |

---

## 13. Global hover rules vs component-specific behavior

| | |
|--|--|
| **Symptom** | Crumbs pick up `accent-hover` intended for nav/cards |
| **Root cause** | Sweep classification without per-component exceptions |
| **Impact** | Visual regression vs E58 |
| **Detection** | Hover computed vs freeze |
| **Corrected** | E60-FIX01 selector restores |
| **Prevention** | Hover change allowlist per selector family |

---

## 14. Source/runtime ACF drift ambiguity

| | |
|--|--|
| **Symptom** | 8 source-only JSON groups; unclear if “missing from runtime” is a bug |
| **Root cause** | PHP registration can own fields without runtime JSON copies |
| **Impact** | Risk of harmful broad ACF sync |
| **Detection** | Disposition table + FieldGroups.php references |
| **Corrected** | E63 RETAIN_SOURCE_ONLY; no broad sync |
| **Prevention** | ACF ownership mapper capability; never MIR acf-json |

---

## 15. Risky cleanup before documentation

| | |
|--|--|
| **Symptom** | Pressure to delete backups/worktrees immediately after Stable push |
| **Root cause** | Disk pressure / “we’re done” bias |
| **Impact** | Loss of rollback + learning evidence |
| **Detection** | Missing Experience Pack / inventory |
| **Corrected** | This Phase 2 pack + advisory inventory **before** cleanup |
| **Prevention** | Documentation gate before destructive cleanup charter |

---

## 16. Related Phase 1 anti-patterns still in force

Continue to treat as active:

- False-positive save tests without real wp-admin POST (E51).
- `git add .` / dirty-main push / force push.
- Demo fallback as normal SoT.

See Phase 1 anti-patterns doc.
