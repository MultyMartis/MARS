# REPORT — FP-0002 V9-06D9-Q REVIEWS INCLUDE PLANNING

**Date:** 2026-07-06  
**Base HEAD note:** corrective `fae4cd07`; actual synced tip `c188cd2e` (+1 OCPilot ancestor)  
**Verdict:** PASS

---

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: c188cd2ec94dfba47efd2c9ce6e26ff768ce9982
- Local short HEAD: c188cd2e
- Remote HEAD: c188cd2ec94dfba47efd2c9ce6e26ff768ce9982
- Remote short HEAD: c188cd2e
- Ahead: 0
- Behind: 0
- Foreign WIP: present (unstaged; not staged)
- Pre-existing staged files: none
- Strict HEAD gate: **PASS_WITH_HEAD_NOTE** (required `fae4cd07` is direct ancestor; +1 unrelated OCPilot commit at tip; branch synced)
- Result: **PASS**

---

## 2. Authorization and scope

- Operator authorization: V9-06D9-Q Reviews Include Planning
- Task mode: READ-ONLY PLANNING + documentation/evidence writes
- DB writes: 0
- Source/theme changes: 0
- ACF JSON changes: 0
- ACF value writes: 0
- Native content writes: 0
- Media uploads: 0
- Options writes: 0
- Menu writes: 0
- Runtime delivery: NOT_PERFORMED
- OCPilot writes: 0
- Documentation/evidence writes: YES (approved paths)
- Result: **PASS**

---

## 3. Current reviews architecture audit

| Area | Current state | Notes |
|---|---|---|
| Home template | `template-parts/home/reviews.php` | 10 static V9 Swiper slides |
| Card data source | Hardcoded HTML | Not ACF-driven |
| Section heading | ACF `home_reviews_heading` | Fallback «Отзывы» |
| `home_reviews_teaser` | Home ACF repeater | Optional; 1 DB row; **not wired to frontend** |
| Reviews CPT | None | No review post type |
| Reviews page ACF | `group_fp02_page_reviews` | `reviews_items` max 50; skeleton theme partials |
| `/otzyvy/` route | HTTP 200 | Placeholder partials only |
| V9 static | `reviews.html` | 10 cards; author, 5★, text |
| Site options pattern | `fp02-site-settings` | Contacts + modal CTA active |
| D8-B seed | Reviews skipped | Gallery/reviews not seeded |

Evidence: `validation/v9-06d9q-reviews-include-planning/current-reviews-architecture-audit.json`  
Architecture: `architecture/FP-0002-V9-06D9Q-CURRENT-REVIEWS-ARCHITECTURE-AUDIT-v1.md`

---

## 4. Requirements and constraints

| Requirement | Decision | Notes |
|---|---|---|
| Shared across pages | REQUIRED | One pool for Home + `/otzyvy/` |
| Not on Home edit screen | REQUIRED | Deprecate `home_reviews_teaser` |
| Editor-friendly | REQUIRED | Under «Настройки сайта» |
| Future reviews page | REQUIRED | Shared include on page template |
| Production migration safe | REQUIRED | Git JSON + options export |
| Static demo fallback | REQUIRED | V9 cards when options empty |
| No Home save blockers | REQUIRED | No Home reviews repeater |
| Disable/hide support | REQUIRED | `reviews_enabled` + row `visible` |
| Replaceable later | REQUIRED | CPT escalation reserved |
| No unreviewed production claims | REQUIRED | Demo labeled; D9-S/U gates |

Evidence: `validation/v9-06d9q-reviews-include-planning/reviews-requirements-constraints.json`

---

## 5. Architecture options analysis

| Option | Pros | Cons | Verdict |
|---|---|---|---|
| A Static partial | Simple; matches today | No admin; not shared | Reject |
| B Home ACF repeater | Exists partially | Wrong ownership; operator rejected | **Reject** |
| C ACF Options | Central; shared; MVP fit | No per-review URLs | **Recommended primary** |
| D Reviews CPT | Scalable | Overhead now | Defer |
| E Hybrid | Options + fallback + future CPT | More helper code | **Recommended shape** |

Evidence: `validation/v9-06d9q-reviews-include-planning/reviews-architecture-options-analysis.json`

---

## 6. Recommended architecture

| Area | Recommendation | Notes |
|---|---|---|
| Source-of-truth | ACF Options `reviews_items` on `fp02-site-settings` | New group `group_fp02_site_options_reviews` |
| Admin | «Настройки сайта» → Reviews fields | Matches existing options pattern |
| Shared include | `template-parts/shared/reviews-slider.php` | Helper `inc/reviews-helpers.php` |
| Home integration | Thin wrapper in `home/reviews.php` | limit=10, featured_only |
| Reviews page | Wire skeleton partials to same helper | Full list on archive |
| Fallback | Static V9 demo cards | When options empty |
| Hide when disabled | `reviews_enabled` false | Omit section |
| `home_reviews_teaser` | Remove from Home ACF in D9-R | Never wire frontend |
| Production migration | D9-R JSON + D9-S options seed | Checkpoints required |
| Content policy | Demo vs approved | D9-U optional legal review |

Evidence: `validation/v9-06d9q-reviews-include-planning/recommended-reviews-architecture.json`  
Architecture: `architecture/FP-0002-V9-06D9Q-RECOMMENDED-REVIEWS-ARCHITECTURE-v1.md`

---

## 7. Future implementation plan

| Phase | Scope | Writes expected | Safety gates |
|---|---|---|---|
| D9-R | Shared include + ACF schema + theme refactor | Theme, ACF JSON, runtime delivery | DB checkpoint before sync |
| D9-S | Options seed or keep-static decision | Options values only | DB checkpoint before seed |
| D9-T | Admin UX + visual regression QA | Evidence only | Read-only |
| D9-U | Legal/native content review (optional) | None | Operator gate |

Evidence: `validation/v9-06d9q-reviews-include-planning/future-implementation-plan.json`

---

## 8. Frontend current-state check

| Check | Result | Notes |
|---|---|---|
| Home `/` HTTP 200 | PASS | |
| Home reviews section | PASS | class=reviews; 10 slides |
| Swiper hooks | PASS | data-reviews-slider + pagination |
| PHP fatal | PASS | None detected |
| Contacts `/kontakty/` | PASS | No reviews (expected) |
| Service 74 | PASS | No reviews (expected) |
| `/otzyvy/` | PASS | 200; skeleton partials |

Evidence: `validation/v9-06d9q-reviews-include-planning/frontend-current-state-check.json`

---

## 9. No-scope-drift

- DB writes: 0
- Source/theme changes: 0
- ACF JSON changes: 0
- ACF value writes: 0
- Native content writes: 0
- Media uploads: 0
- Options writes: 0
- Menu writes: 0
- Runtime delivery: NOT_PERFORMED
- OCPilot writes: 0
- DB dumps staged: 0
- Runtime snapshots staged: 0
- Secrets/API keys: 0
- Result: **PASS**

Evidence: `validation/v9-06d9q-reviews-include-planning/no-scope-drift-validation.json`

---

## 10. Documentation changes

| File | Action | Reason |
|---|---|---|
| `reports/FP-0002-V9-06D9Q-REVIEWS-INCLUDE-PLANNING-REPORT-v1.md` | CREATE | Main report |
| `architecture/FP-0002-V9-06D9Q-*.md` (6 files) | CREATE | Planning artifacts |
| `validation/v9-06d9q-reviews-include-planning/*.json` (8 files) | CREATE | Evidence |
| `WORDPRESS/README.md` | UPDATE | Phase status |
| `WORDPRESS/SOURCE-AUTHORITY.md` | UPDATE | Authority chain |
| `FP-0002-SHPIGOVSKY/PROJECT-STATUS.md` | UPDATE | Project status |

---

## 11. Git checkpoint

- Exact staged files: D9-Q report, architecture docs, validation JSON, status docs (selective)
- Staged list inspected: pending
- Source/theme files staged: NO
- ACF JSON staged: NO
- Runtime files staged: NO
- OCPilot files staged: NO
- DB dumps staged: NO
- Runtime snapshots staged: NO
- Helper/temp files staged: NO
- Secrets staged: NO
- Commit: FP-0002: plan reviews include architecture
- Commit hash: pending
- Push: pending
- Local HEAD: pending
- Remote HEAD: pending
- Result: pending

---

## 12. Final verdict

**PASS**

V9-06D9-Q Reviews Include Planning: **COMPLETE**

Recommended reviews architecture: **Hybrid E — ACF Options shared reviews + shared include + static V9 fallback**

Implementation approved now: **NO**

Frontend current-state: **PASS**

No-scope-drift: **PASS**

Recommended next phase: **D9-R — Reviews shared include source/schema implementation**

---

## 13. Recommended next action

**CREATE_V9_06D9R_REVIEWS_SHARED_INCLUDE_IMPLEMENTATION_TASK**

---

## 14. Final safety statement

Target folder: X:\AI MARS

V9-06D9-Q Reviews Include Planning performed: **YES**

DB writes: 0

Source/theme changes: 0

ACF JSON changes: 0

ACF value writes: 0

Native content writes: 0

Media uploads: 0

Options writes: 0

Menu writes: 0

Runtime delivery: **NO**

OCPilot writes: 0

Production migration performed: **NO**

V9 source changed: **NO**

V9 dist changed: **NO**

Plugin source changed in Git: **NO**

DB dump committed: **NO**

Runtime snapshot committed: **NO**

Helper committed: **NO**

Secrets committed: 0
