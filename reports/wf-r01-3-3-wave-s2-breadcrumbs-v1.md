# REPORT — WF-R01.3.3 WAVE S2 BREADCRUMBS REFERENCE PARTIAL

**Artifact ID:** WF-R01.3.3 Wave S2 — BREADCRUMBS (v1)  
**Date:** 2026-06-19  
**Mode:** controlled reference-layer execution pass — **one wave slice (BREADCRUMBS Tier B layout-component only)**  
**Honesty boundary:** Human-operated reference partial implementation. **Not** production pass. **Not** G2 authorization. **Not** CATEGORY/PLP scaffold. **Not** fidelity verified.

---

## 1. Result

| Field | Value |
|-------|-------|
| **Status** | **COMPLETE** |
| **Preflight decision** | **IMPLEMENTATION AUTHORIZED** (Path B — Tier B layout-component RPC accounting) |
| **BREADCRUMBS identity** | F3 Structural Block · Tier B layout-component · vocabulary `BREADCRUMBS` · **no** `block_id` registry row |
| **RC** | **32/32** (unchanged) |
| **RPC before** | **15/32** (~46.9%) |
| **RPC after** | **16/32** (~50.0%) |
| **RSC** | **1/10 global · 1/1 LANDING** (unchanged) |
| **SC** | **LANDING PASS** (unchanged) |
| **PC** | **1/1 LANDING** (unchanged) |
| **Next task** | **WF-R01.3.3 Wave S3 — PAGINATION Reference Partial** |

---

## 2. Git Safety

| Field | Value |
|-------|-------|
| **Branch** | `mars/post-cycle8-live-tests` |
| **HEAD before task** | `4ce1cd9` — foundry: publish WF-R01.3.3 global shell contract |
| **Foreign WIP** | Present — excluded from selective commit |
| **Selective scope** | Wave S2 paths only (partial, SCSS, host page, registry mapping docs, roadmap, OPERATIONAL-INDEX, this REPORT) |

---

## 3. Authority Reviewed

| Document | Path | Role |
|---|---|---|
| WF-R01.3.3 Charter | `projects/mars-website-factory/wf-r01-3-3-structural-shell-references-charter-v1.md` | BREADCRUMBS policy §9; RPC layout-component accounting §14; Wave S2 scope §17 |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Shell order; breadcrumbs slot; page-type matrix; L2 depth |
| Wave S1 REPORT | `reports/wf-r01-3-3-wave-s1-global-shell-contract-v1.md` | Prior wave baseline; Tier B disposition noted |
| Vocabulary Canon | `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` | F3 Structural Block family |
| Structural Blocks Charter | `projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md` | Tier B layout-component default; no v1.1 `block_id` |
| Coverage Model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | RPC/T1+ rules; denominator 32 |
| G0 Baseline | `reports/wf-r01-3-0-coverage-baseline-snapshot-v1.md` | Pre-expansion metrics |
| Gate 2 Pass | `reports/wf-r01-2-gate-2-execution-pass-v1.md` | BREADCRUMBS not minted as `block_id` |
| Block Registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | No BREADCRUMBS row — confirmed |
| Core Block Library | `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md` | Tier B inventory target |
| Block Gaps | `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md` | Tier B layout-component inventory |
| Page Type Registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` | Applicability matrix source |
| Roadmap | `projects/mars-website-factory/roadmap.md` | Program state |
| Operational Index | `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Operator entry point |

---

## 4. Identity and Coverage Preflight

| Question | Answer |
|---|---|
| **Registry row in BLOCK-REGISTRY-v1.md?** | **No** — by design (Tier B) |
| **Canonical block/component ID** | Vocabulary `BREADCRUMBS`; partial hook `data-block-id="breadcrumbs"` (layout-component identity, not registry row) |
| **Denominator membership (32)?** | **No** — not one of 29 Core + 3 Tier A structural `block_id`s |
| **RC membership?** | **No** separate RC row; F3 vocabulary covered under structural policy |
| **RPC eligibility?** | **Yes** — via WF-R01.3.3 §14 layout-component accounting when T1+ criteria met |
| **Formula** | Strict block_id RPC: 15/32 unchanged set + **+1 Tier B partial-equivalent** = **16/32**; denominator **32 fixed** per Coverage Model § In-scope set evolution + charter §14 explicit delta |
| **Charter/Coverage consistency** | Reconciled: Coverage Model § Quality tier binding requires `block_id` for default RPC; WF-R01.3.3 §9/§14 **supersedes for Tier B** with documented layout-component accounting (Path B) |
| **Final authorization** | **IMPLEMENTATION AUTHORIZED** |

**Evidence for Path B:** [wf-r01-3-3-structural-shell-references-charter-v1.md](../projects/mars-website-factory/wf-r01-3-3-structural-shell-references-charter-v1.md) §9.5 (six T1+ criteria) and §14 (+1 RPC layout-component accounting). No new `block_id` row created.

---

## 5. Source Selection

| Field | Value |
|-------|-------|
| **HTML source** | `workspaces/triumph-manipulator-landing-v2/src/partials/components/breadcrumb.html` |
| **SCSS source** | `workspaces/triumph-manipulator-landing-v2/src/scss/components/_breadcrumb.scss` |
| **Secondary source** | `workspaces/triumph-manipulator-landing/` (same pattern — v2 preferred as canonical Triumph workspace) |
| **Extracted decisions** | `<nav aria-label="Breadcrumb">`; `<ol>` list; ancestor links; current page non-link; `/` separator via pseudo-element in source → **adapted** to explicit `<span aria-hidden="true">` for SR safety; wf-* namespace; 4-level demo hierarchy |
| **Excluded client data** | Real URLs (`index.html` → `#`); client brand; CMS helpers; JSON-LD; Triumph `.breadcrumb` class namespace |

**ISBD / BZPM:** No dedicated Factory-bound breadcrumb partial confirmed — Triumph v2 used as primary execution-case reference.

---

## 6. Vocabulary Decision

| Field | Value |
|-------|-------|
| **Family** | F3 Structural Block |
| **Navigation depth** | L2 contextual |
| **Purpose** | Hierarchy orientation; parent-level navigation; internal pages only; contextual shell slot |
| **Boundaries** | ≠ HEADER_NAV · ≠ page title · ≠ SEO Surface · ≠ PAGINATION · ≠ FILTERS |
| **Structured data policy** | Schema.org `BreadcrumbList` = future/project-specific; **not** required in Wave S2 |

---

## 7. Page-Type Applicability

| Page type | State | Notes |
|---|---|---|
| `LANDING_PAGE` | **—** | Forbidden on LANDING reference — not integrated |
| `HOME_PAGE` | R | Policy-dependent shallow trail |
| `SERVICE_PAGE` | R | Recommended |
| `CATEGORY_PAGE` | **O** | Primary future host — scaffold **not yet built** |
| `PRODUCT_PAGE` | **O** | Required when PDP scaffold exists |
| `ABOUT_PAGE` | **O** | Required on internal corporate |
| `CONTACT_PAGE` | R | Policy-dependent |
| `FAQ_PAGE` | R | Policy-dependent |
| `REVIEWS_PAGE` | R | Policy-dependent |
| `LEGAL_PAGE` | R | Policy-dependent |

---

## 8. Host Decision

| Field | Value |
|-------|-------|
| **Host type** | **Variant B — bounded demonstration host** |
| **Exact path** | `workspaces/website-factory-reference-v1/src/pages/breadcrumbs-reference.html` |
| **Why permitted** | CATEGORY_PAGE scaffold does not exist; charter Wave S2 allows T1+ partial + build host without RSC accrual; task Phase 9 Variant B |
| **RSC/SC/PC impact** | **None** — not a `page_type` scaffold; `noindex` meta |
| **LANDING exclusion** | `index.html` **not modified**; dist/index.html contains **zero** `wf-breadcrumbs` |

**Shell composition on host:** HEADER_NAV → BREADCRUMBS → MAIN → FOOTER (LEGAL_LINKS nested in FOOTER).

---

## 9. Files Created

| File | Purpose |
|---|---|
| `workspaces/website-factory-reference-v1/src/partials/components/breadcrumbs.html` | Canonical BREADCRUMBS reference partial |
| `workspaces/website-factory-reference-v1/src/scss/components/_breadcrumbs.scss` | Scoped `.wf-breadcrumbs` styles |
| `workspaces/website-factory-reference-v1/src/pages/breadcrumbs-reference.html` | Bounded build host (not RSC) |
| `reports/wf-r01-3-3-wave-s2-breadcrumbs-v1.md` | This wave REPORT |

---

## 10. Files Modified

| File | Change |
|---|---|
| `workspaces/website-factory-reference-v1/src/scss/main.scss` | Added `@use 'components/breadcrumbs'` |
| `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md` | Breadcrumbs → PARTIAL; SCSS/partial counts |
| `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md` | Tier B layout-components section; BREADCRUMBS reference row |
| `projects/mars-website-factory/roadmap.md` | Wave S2 COMPLETE; RPC 16/32; next S3 |
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Metrics and next task |

---

## 11. Implementation

| Aspect | Detail |
|---|---|
| **HTML semantics** | `<nav>` · `<ol>` · `<li>` · ancestor `<a href="#">` · current `<span aria-current="page">` |
| **Hierarchy** | Home → Catalog → Category → Current Page (4 levels) |
| **Current page** | Non-link; `aria-current="page"` |
| **Separators** | `<span class="wf-breadcrumbs__separator" aria-hidden="true">/</span>` — not read as meaningful content |
| **Responsive behavior** | Desktop: inline flex + horizontal scroll for overflow; mobile: wrap + `overflow-wrap` on long labels |
| **Accessibility** | `aria-label="Breadcrumb"`; focus-visible on links; separator hidden from AT |

---

## 12. Registry and Reference Mapping

| Field | Value |
|---|---|
| **Files updated** | BLOCK-GAPS-v1.md · CORE-BLOCK-LIBRARY-v1.md |
| **Existing row or Tier B inventory** | Tier B in BLOCK-GAPS §2 + CORE-BLOCK-LIBRARY Tier B section |
| **BLOCK-REGISTRY-v1.md** | **Not modified** — no new `block_id` |
| **No-new-ID confirmation** | **Confirmed** |

---

## 13. Coverage Accounting

| Dimension | Before | After | Evidence |
|---|---|---|---|
| **RC** | 32/32 | 32/32 | No registry row added |
| **RPC** | 15/32 | **16/32** | +1 Tier B BREADCRUMBS T1+ partial-equivalent per charter §14 |
| **RSC** | 1/10; 1/1 LANDING | unchanged | Demonstration host ≠ page_type scaffold |
| **SC** | LANDING PASS | unchanged | LANDING not modified |
| **PC** | 1/1 LANDING | unchanged | No new Reference Composition |

**16/32 block_id + layout-component units counted:**

15 prior `block_id` partials + **1 Tier B BREADCRUMBS layout-component partial** (documented exception to strict block_id-only RPC per WF-R01.3.3 §14).

---

## 14. Validation

| Check | Result |
|---|---|
| Include | **PASS** — single include in `breadcrumbs-reference.html` |
| Import | **PASS** — single `@use 'components/breadcrumbs'` in main.scss |
| Semantic structure | **PASS** |
| ARIA | **PASS** |
| Orphan check | **PASS** |
| Duplicate check | **PASS** — one canonical partial path |
| LANDING unchanged | **PASS** |
| PAGINATION untouched | **PASS** |

---

## 15. Build

| Field | Value |
|-------|-------|
| **Command** | `npm run build` in `workspaces/website-factory-reference-v1/` |
| **Exit code** | **0** |
| **Built host** | `dist/breadcrumbs-reference.html` |
| **dist evidence** | `wf-breadcrumbs` present; `data-block-id="breadcrumbs"` × 1; no `@@include` leftovers |
| **LANDING dist** | `dist/index.html` — no `wf-breadcrumbs` |
| **warnings** | Dart Sass legacy-js-api deprecation (pre-existing) |

**Result:** **REFERENCE PARTIAL BUILT**

---

## 16. Browser Sanity

| Viewport | Assessment |
|---|---|
| **Desktop** | Inline trail readable; current page weight distinct; links hover/focus styled |
| **Tablet** | Wrap behavior at md breakpoint |
| **Mobile** | Horizontal scroll on narrow desktop band; wrap on mobile |
| **Keyboard** | `:focus-visible` on ancestor links |
| **Long path** | `text-overflow: ellipsis` / `overflow-wrap` prevent layout break |

**Note:** Static structural review from markup/CSS contract — **not** live browser automation. **BUILT ≠ FIDELITY VERIFIED ≠ PRODUCTION PASS**.

---

## 17. Documentation State

| Artifact | State |
|---|---|
| **roadmap.md** | Wave S2 COMPLETE; RPC 16/32; next S3 |
| **OPERATIONAL-INDEX.md** | Updated metrics and next task |
| **WF-R01.3.3 COMPLETE** | **Not** marked |
| **G2 ACTIVE** | **Not** marked |

---

## 18. Git Result

| Field | Value |
|-------|-------|
| **Commit hash** | `0f8f77f` |
| **Commit message** | `foundry: complete WF-R01.3.3 breadcrumbs reference` |
| **Push result** | **SUCCESS** — `mars/post-cycle8-live-tests` → `origin/mars/post-cycle8-live-tests` (`4ce1cd9..0f8f77f`) |
| **Files committed** | 9 — partial, SCSS, host page, main.scss, BLOCK-GAPS, CORE-BLOCK-LIBRARY, roadmap, OPERATIONAL-INDEX, REPORT |
| **No foreign lane confirmation** | **Confirmed** — staged diff contained only Wave S2 paths |

---

## 19. Drift and Risks

| Severity | Finding | Action |
|---|---|---|
| Low | Strict Coverage Model readers may expect RPC 15/32 only | REPORT documents charter §14 layout-component exception |
| Low | Demonstration host ≠ CATEGORY_PAGE scaffold | Acceptable for S2; catalog integration deferred to WF-R01.3.4 |
| Low | `data-block-id="breadcrumbs"` is vocabulary hook, not registry row | Documented in §4 |
| Medium | Future `block_id` waiver may change identity hook | Monitor per WF-R01.2 SAFE UNKNOWN |

---

## 20. Final Status

```text
COMPLETE
```

---

## 21. Next Task

```text
WF-R01.3.3 Wave S3 — PAGINATION Reference Partial
```

---

## 22. Exact Evidence Paths

- `projects/mars-website-factory/wf-r01-3-3-structural-shell-references-charter-v1.md`
- `projects/mars-website-factory/global-shell-contract-v1.md`
- `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md`
- `projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md`
- `reports/wf-r01-3-3-wave-s1-global-shell-contract-v1.md`
- `reports/wf-r01-3-2-g1-five-dimension-exit-v1.md`
- `workspaces/website-factory-reference-v1/src/partials/components/breadcrumbs.html`
- `workspaces/website-factory-reference-v1/src/scss/components/_breadcrumbs.scss`
- `workspaces/website-factory-reference-v1/src/pages/breadcrumbs-reference.html`
- `workspaces/website-factory-reference-v1/src/scss/main.scss`
- `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md`
- `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md`
- `workspaces/triumph-manipulator-landing-v2/src/partials/components/breadcrumb.html`
- `workspaces/triumph-manipulator-landing-v2/src/scss/components/_breadcrumb.scss`
- `projects/mars-website-factory/roadmap.md`
- `projects/mars-website-factory/OPERATIONAL-INDEX.md`
- `reports/wf-r01-3-3-wave-s2-breadcrumbs-v1.md`

---

## 23. Stop Confirmation

```text
Wave S3: NOT STARTED
PAGINATION: NOT IMPLEMENTED
FILTERS: NOT IMPLEMENTED
SEARCH: NOT IMPLEMENTED
WF-R01.3.4: NOT STARTED
G2 execution: NOT STARTED
LANDING reference: NOT MODIFIED
Production readiness: NOT CLAIMED
```
