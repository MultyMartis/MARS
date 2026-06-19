# Website Factory Reference Scaffold Contract v1

**Status:** **ACCEPTED**  
**Authority:** WF-R01.3.3 Wave S4  
**Date:** 2026-06-19  
**Parent charter:** [wf-r01-3-3-structural-shell-references-charter-v1.md](wf-r01-3-3-structural-shell-references-charter-v1.md)  
**Shell inputs:** [global-shell-contract-v1.md](global-shell-contract-v1.md) · [page-type-shell-matrix-v1.md](page-type-shell-matrix-v1.md)  
**Coverage authority:** [wf-r01-3-1-coverage-model-charter-v1.md](wf-r01-3-1-coverage-model-charter-v1.md)

**Classification:** documentation-layer normative contract

**This contract is not:** runtime · orchestration · CMS integration · production deployment · automatic validator engine

**Honesty boundary:** Defines minimum requirements for a **Reference Scaffold** to accrue **RSC** and support **SC** / **PC** evidence chains. Publishing this contract **does not** create scaffolds or increase coverage metrics.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **ACCEPTED** |
| **Publication wave** | WF-R01.3.3 Wave S4 |
| **Consolidates** | WF-R01.3.3 charter §11 · Global Shell Contract §17 · Coverage Model RSC rules · LANDING manifest evidence pattern |
| **Metrics impact** | **None** — RC **32/32** · RPC **17/32** · RSC **1/10 global; 1/1 LANDING** · SC **LANDING PASS** · PC **1/1 LANDING** unchanged |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Name** | Website Factory Reference Scaffold Contract |
| **Version** | v1 |
| **Program** | WF-R01.3.3 — Structural & Shell References |
| **Canonical path** | `projects/mars-website-factory/reference-scaffold-contract-v1.md` |
| **Scope** | Reference-layer page-type implementations in Website Factory reference workspace and bound delivery copies |

---

## 3. Authority and Inputs

| Document | Path | Role |
|----------|------|------|
| WF-R01.3.3 charter | [wf-r01-3-3-structural-shell-references-charter-v1.md](wf-r01-3-3-structural-shell-references-charter-v1.md) | Shell scaffold minimum §11; wave map |
| Global Shell Contract | [global-shell-contract-v1.md](global-shell-contract-v1.md) | Shell order · semantics · validation floor |
| Page-Type Shell Matrix | [page-type-shell-matrix-v1.md](page-type-shell-matrix-v1.md) | Per-type shell and slot applicability |
| Coverage Model | [wf-r01-3-1-coverage-model-charter-v1.md](wf-r01-3-1-coverage-model-charter-v1.md) | RSC · SC · PC definitions |
| LANDING completion | [wf-r01-3-2-landing-completion-charter-v1.md](wf-r01-3-2-landing-completion-charter-v1.md) | First scaffold wave evidence |
| Page Type Registry | [PAGE-TYPE-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md) | Registered `page_type` denominator |
| Site Type Registry | [SITE-TYPE-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md) | `site_type_code` applicability |
| Block Registry | [BLOCK-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md) | Canonical `block_id` rows |
| LANDING manifest (pattern) | [LANDING-SCAFFOLD-MANIFEST-v1.md](../../workspaces/website-factory-reference-v1/LANDING-SCAFFOLD-MANIFEST-v1.md) | Manifest evidence template |
| LANDING composition (pattern) | [REFERENCE-COMPOSITION-v1.md](../../workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md) | PC evidence template |
| Wave S2 / S3 REPORTs | [wf-r01-3-3-wave-s2-breadcrumbs-v1.md](../../reports/wf-r01-3-3-wave-s2-breadcrumbs-v1.md) · [wf-r01-3-3-wave-s3-pagination-v1.md](../../reports/wf-r01-3-3-wave-s3-pagination-v1.md) | Tier B partial policy — hosts ≠ scaffolds |

---

## 4. Purpose

This contract defines when a page-type implementation qualifies as a **Reference Scaffold** — the artifact class counted toward **RSC**.

It establishes:

1. Scaffold definition and exclusions.
2. Required artefacts, manifest fields, and evidence paths.
3. Shell, composition, and block-mapping requirements.
4. Build and structural validation minimums.
5. Responsive and accessibility floors.
6. Placeholder content policy.
7. Coverage accrual and lifecycle states.
8. Prohibited claims and handoff boundaries.

**Wave S4 does not create scaffolds.** Only future authorized waves may produce scaffold implementations.

---

## 5. Scaffold Definition

```text
Reference Scaffold = buildable page-type implementation that binds
a registered page type to a valid shell, block composition, assets,
manifest and structural validation evidence.
```

A Reference Scaffold is a **complete reference-layer page** for one registered `page_type`, not a documentation stub alone.

### What a scaffold is

| Property | Requirement |
|----------|-------------|
| Identity | Bound to one registered `page_type` from PAGE-TYPE-REGISTRY-v1 |
| Buildability | Source page resolves includes and produces `dist/` output |
| Shell | Conforms to Global Shell Contract + Page-Type Shell Matrix |
| Composition | Documented block sequence with canonical identities |
| Manifest | Published scaffold manifest with stub honesty |
| Evidence | Build PASS + structural validation PASS + wave REPORT |

### What a scaffold is not

```text
Registry row
HTML partial (single component)
Bounded component host page
Wireframe image
Mockup
Production page
CMS integration
Client deployment
Documentation-only markdown
Manifest without buildable source page
```

**Bounded component hosts (explicit exclusion):**

```text
breadcrumbs-reference.html ≠ scaffold
pagination-reference.html ≠ scaffold
```

These are Tier B partial demonstration hosts from Waves S2/S3 — they **must not** accrue RSC.

---

## 6. Scaffold vs Related Artefacts

| Artefact | Relationship to scaffold |
|----------|--------------------------|
| Block partial | Building block — 1 partial ≠ 1 scaffold |
| Bounded component host | Demonstrates one Tier B component — ≠ scaffold |
| Global Shell Contract | Prerequisite policy — ≠ scaffold |
| Page-Type Shell Matrix | Applicability policy — ≠ scaffold |
| Scaffold Manifest | Required evidence — manifest alone ≠ scaffold |
| Reference Composition | PC artefact — composition doc alone ≠ scaffold |
| Built page | Necessary — built page alone ≠ validated scaffold |
| Structurally Validated Scaffold | Passes §14 checks — ≠ fidelity verified |
| Fidelity Verified | Visual/design QA — ≠ production pass |
| Production Pass | Client-ready acceptance — out of reference-layer default |

```text
Block partial ≠ Scaffold
Bounded component host ≠ Scaffold
Shell Contract ≠ Scaffold
Page-Type Shell Matrix ≠ Scaffold
Scaffold Manifest ≠ Scaffold by itself
Reference Composition ≠ Scaffold by itself
Built page ≠ Structurally Validated Scaffold
Structurally Validated Scaffold ≠ Fidelity Verified
Fidelity Verified ≠ Production Pass
```

---

## 7. Required Scaffold Artefacts

Each Reference Scaffold **must** have at minimum:

| # | Artefact | Purpose |
|---|----------|---------|
| 1 | Registered `page_type` identity | RSC denominator binding |
| 2 | Buildable source page | Gulp include graph entry |
| 3 | Global shell mapping | HEADER_NAV · MAIN · FOOTER · LEGAL_LINKS |
| 4 | Page block composition | Ordered MAIN blocks |
| 5 | Partial mapping | Include paths per block |
| 6 | SCSS / asset mapping | Styles and raster/SVG dependencies |
| 7 | JavaScript mapping | Init hooks where required |
| 8 | Scaffold manifest | Stub honesty + evidence binding |
| 9 | Build evidence | Reproducible `npm run build` PASS |
| 10 | Structural validation evidence | Matrix-compliant checks |
| 11 | Known limitations | Honest scope boundaries |
| 12 | Source / reference provenance | Extraction or design source trail |

### Recommended paths (reference workspace — not universal production binding)

| Artefact | Recommended path pattern |
|----------|--------------------------|
| Source page | `src/pages/<page-type-reference>.html` |
| Manifest | `<PAGE-TYPE>-SCAFFOLD-MANIFEST-v1.md` (workspace root or documented equivalent) |
| Composition | `<PAGE-TYPE>-REFERENCE-COMPOSITION-v1.md` or section in shared composition doc |
| Wave REPORT | `reports/<page-type>-scaffold-pass-v1.md` or program wave REPORT |

**LANDING evidence instance:**

- `workspaces/website-factory-reference-v1/src/pages/index.html`
- `workspaces/website-factory-reference-v1/LANDING-SCAFFOLD-MANIFEST-v1.md`
- `workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md`

---

## 8. Required Manifest Fields

Pattern source: [LANDING-SCAFFOLD-MANIFEST-v1.md](../../workspaces/website-factory-reference-v1/LANDING-SCAFFOLD-MANIFEST-v1.md).

Every scaffold manifest **must** declare:

| Field group | Required content |
|-------------|------------------|
| **Identity** | Manifest version · status · `page_type` ID · `site_type_code` applicability |
| **Paths** | Source page path · `dist` output path |
| **Shell** | Shell mapping (HEADER_NAV · MAIN · FOOTER · LEGAL_LINKS · contextual slots) |
| **Composition** | Block sequence · nested compositions · shell vs content separation |
| **Mapping** | Partial paths · SCSS paths · JavaScript modules · asset dependencies |
| **Provenance** | Reference sources · extraction notes |
| **Build** | Exact build command · build result (exit code · PASS/FAIL) |
| **Validation** | Structural validation result · evidence REPORT link |
| **Coverage** | Coverage claims (RSC / SC / PC) — must match factual state |
| **Honesty** | Known limitations · SAFE UNKNOWN items |
| **Stub policy** | Stub type · production disclaimer |

**Forbidden:** manifest without a **factual buildable source page** at declared path.

---

## 9. Shell Requirements

Scaffold shell **must** conform to:

- [global-shell-contract-v1.md](global-shell-contract-v1.md)
- [page-type-shell-matrix-v1.md](page-type-shell-matrix-v1.md)

### Minimum shell checks

| Check | Expected |
|-------|----------|
| HEADER_NAV count | 0 or 1 per matrix row |
| MAIN count | **Exactly 1** |
| FOOTER count | 0 or 1 per matrix row |
| LEGAL_LINKS | Nested in FOOTER when matrix requires |
| BREADCRUMBS | Present / absent per matrix REQ · POL · N/A · FORB |
| PAGINATION | Present / absent per matrix |
| SEARCH / FILTERS slots | Policy notes only until WF-R01.3.4 implementation |
| DOM order | HEADER_NAV → MAIN → FOOTER when shell regions present |
| Duplicate block identity | None at site level |
| HEADER ≠ HERO | Global nav must not absorb hero |

---

## 10. Page Composition Requirements

Scaffold **must** document:

| Requirement | Specification |
|-------------|---------------|
| Block sequence | Ordered list top-to-bottom inside MAIN |
| Canonical identity | Registry / vocabulary ID for each composition block |
| Shell vs content | Shell blocks outside MAIN; content blocks inside MAIN |
| Nested composition | e.g. LEGAL_LINKS inside FOOTER — explicit in manifest |
| Required / optional blocks | Rationale per block; POL blocks declared when present |
| Hidden dependencies | **Forbidden** — all includes and assets declared |
| Page-type fit | Blocks appropriate for active `page_type` — no accidental LANDING stack on CATEGORY |
| PC artefact | Composition published as Reference Composition doc or normative manifest section per Coverage Model |

---

## 11. Block Mapping Requirements

For **each** composition block, manifest or companion composition **must** specify:

| Field | Content |
|-------|---------|
| Canonical identity | `block_id` or vocabulary term |
| Family | F1–F6 per Vocabulary Canon |
| Partial path | `src/partials/...` |
| Style path | SCSS import / layer |
| JS dependency | Module or `data-module` hook if required |
| Include location | Page or parent partial |
| Required / optional | State with rationale |
| Build evidence | Resolved at build time |
| Validation state | PASS / FAIL / deferred |

### Tier B contextual components

| Component | Identity rule |
|-----------|---------------|
| **BREADCRUMBS** | Tier B layout-component · vocabulary `BREADCRUMBS` · **no** Registry `block_id` row · `data-block-id="breadcrumbs"` as layout hook |
| **PAGINATION** | Tier B layout-component · vocabulary `PAGINATION` · **no** Registry `block_id` row · `data-block-id="pagination"` as layout hook |

Do **not** imitate Tier A Registry rows for Tier B components.

### Future slots (WF-R01.3.4)

| Slot | Until implementation |
|------|----------------------|
| **FILTERS** | Manifest may note **POL** slot only — no partial claim |
| **SEARCH** | Manifest may note **POL** slot only — no partial claim |

---

## 12. Asset and JavaScript Mapping

| Rule | Policy |
|------|--------|
| Declaration | All shell and composition assets listed in manifest |
| SCSS layers | Proper layer (sections / components / layout) per starter architecture |
| JS init | Documented in manifest; one init per module per page |
| Progressive enhancement | MAIN content usable without JS |
| Shell JS failure | Must not hide critical MAIN content |
| Duplication | Forbidden — double init of same shell module |

---

## 13. Build Evidence

Minimum build evidence record:

| Evidence item | Requirement |
|---------------|-------------|
| Build command | Exact command (e.g. `npm run build`) |
| Exit code | **0** for PASS |
| Dist output path | Declared path exists post-build |
| Unresolved includes | **None** |
| Required hooks | Present where manifest declares |
| Duplicate hooks | **None** |
| Shell order check | Matches matrix in rendered HTML |
| Asset presence | Referenced CSS/JS/fonts present in dist or linked |
| Warning inventory | Material warnings documented — not silently ignored |

Build evidence **must** be:

- Reproducible from declared workspace state
- Bound to commit hash or exact workspace snapshot in wave REPORT
- **Not** equivalent to production deploy evidence

---

## 14. Structural Validation

Minimum validation table:

| Check | Expected |
|-------|----------|
| Registered page type | Present in manifest and source |
| Source page | Present at declared path |
| Dist page | Present at declared path |
| Main landmark | Exactly **1** |
| Shell order | Matrix compliant |
| Required blocks | Present per composition |
| Forbidden blocks | Absent (e.g. PAGINATION on LANDING) |
| Nested compositions | Correct (LEGAL_LINKS in FOOTER) |
| Duplicate identities | None at site level |
| Unresolved includes | None |
| Required CSS | Present |
| Required JS | Present where declared |
| Build | **PASS** |

**Page-type-specific checks** derive from [page-type-shell-matrix-v1.md](page-type-shell-matrix-v1.md) row for active `page_type`.

### Validation outcomes (distinct)

```text
BUILT
STRUCTURALLY VALIDATED
COMPOSITION PUBLISHED
COVERAGE ACCEPTED
FIDELITY VERIFIED
PRODUCTION PASS
```

```text
BUILT ≠ STRUCTURALLY VALIDATED ≠ FIDELITY VERIFIED ≠ PRODUCTION PASS
```

---

## 15. Responsive Validation

**No universal breakpoints** in this contract — breakpoints belong to project design systems.

Required outcomes:

| Outcome | Requirement |
|---------|-------------|
| DOM semantics | Shell preserves landmark semantics across viewports |
| Overflow | No persistent horizontal overflow at supported minimum width |
| Navigation | Global nav keyboard-operable when HEADER_NAV present |
| Contextual components | BREADCRUMBS / PAGINATION do not break layout |
| Focus | Visible focus on interactive controls |
| Current page states | `aria-current="page"` where applicable |
| Mobile nav | Trigger state synchronized (`aria-expanded`, `aria-controls`) |
| Text scaling | Critical regions remain functional at increased text size |
| Landmarks | Distinct accessible names when multiple nav regions exist |

Visual PASS **must not** mask structural FAIL.

---

## 16. Accessibility Minimum

Minimum floor — **not** WCAG certification.

| Requirement | Specification |
|-------------|---------------|
| Main landmark | One `<main>` |
| Nav names | Each shell `<nav>` has accessible name |
| Keyboard | Shell controls operable |
| Focus visible | Interactive elements show focus |
| BREADCRUMBS | `<nav aria-label="Breadcrumb">`; current item not self-linked |
| PAGINATION | `<nav aria-label="Pagination">`; keyboard operable |
| Color | State not conveyed by color alone |
| Errors | Accessibility gaps documented — not hidden behind visual PASS |

---

## 17. Content and Placeholder Policy

Reference scaffolds **may** use neutral placeholder content sufficient for structural validation.

**Forbidden in reference scaffolds:**

- Real client phone numbers · bank details · personal data
- Production URLs presented as live client routes
- Secrets · API keys · credentials
- Fictitious commercial claims about a real company
- Copy-paste of production client content without charter justification

Placeholder content **must** support structure checking **without** imitating production readiness.

---

## 18. Coverage Accounting

### Metrics at Wave S4 publication (unchanged)

| Dimension | Value |
|-----------|-------|
| **RC** | **32/32** |
| **RPC** | **17/32** |
| **RSC** | **1/10 global · 1/1 LANDING** |
| **SC** | **LANDING PASS** |
| **PC** | **1/1 LANDING** |

### RSC accrual

**+1 RSC** per `page_type` **only if all apply:**

1. `page_type` registered in PAGE-TYPE-REGISTRY-v1
2. Buildable source page exists
3. Manifest published with stub honesty
4. Shell conforms to Global Shell Contract + Page-Type Shell Matrix
5. Build **PASS**
6. Structural validation **PASS**
7. Wave REPORT with evidence exists

**Documentation contracts alone (S1, S4) do not increase RSC.**

### SC accrual

**SC** follows site-type coverage checklist — **not** automatic from RSC alone.

### PC accrual

**PC** requires **published and implemented** Reference Composition — not manifest-only markdown.

### RPC accrual

Scaffold **does not** re-count RPC for partials already credited (e.g. HEADER_NAV on second page type).

Tier B BREADCRUMBS/PAGINATION partials accrued RPC in S2/S3 — scaffold integration **does not** double-count.

---

## 19. Scaffold Lifecycle

| State | Meaning | Required evidence |
|-------|---------|-------------------|
| **PLANNED** | Page type selected; no source page | Charter / wave authorization |
| **AUTHORIZED** | Wave charter permits build | Wave preflight REPORT |
| **BUILT** | Source compiles to dist | Build PASS |
| **STRUCTURALLY VALIDATED** | §14 checks PASS | Validation record in REPORT |
| **COMPOSITION PUBLISHED** | Reference Composition doc live | PC numerator evidence |
| **COVERAGE ACCEPTED** | Operator accepts RSC/SC claim | Five-dimension REPORT |
| **FIDELITY VERIFIED** | Design QA pass (optional in reference layer) | Fidelity REPORT |
| **PRODUCTION PASS** | Client production acceptance | Out of default reference scope |

Critical distinctions:

```text
AUTHORIZED ≠ BUILT
BUILT ≠ STRUCTURALLY VALIDATED
STRUCTURALLY VALIDATED ≠ COVERAGE ACCEPTED
COVERAGE ACCEPTED ≠ PRODUCTION PASS
```

Not all projects must reach **FIDELITY VERIFIED** inside Reference Layer.

---

## 20. Acceptance Criteria

A page-type implementation may be declared an **accepted Reference Scaffold** **only if all apply:**

- [ ] `page_type` registered in PAGE-TYPE-REGISTRY-v1
- [ ] Page-Type Shell Matrix applied to shell and slots
- [ ] Source page buildable
- [ ] Manifest complete per §8
- [ ] Shell correct per §9
- [ ] Required contextual components present; forbidden absent
- [ ] Build **PASS**
- [ ] Structural validation **PASS**
- [ ] Composition mapping published
- [ ] Coverage accounting confirmed in wave REPORT
- [ ] Known limitations documented
- [ ] No false production-readiness claim

---

## 21. Prohibited Claims

Explicitly **forbidden:**

```text
documentation-only scaffold
manifest-only scaffold
bounded component host counted as scaffold
build PASS counted as fidelity verification
scaffold counted as production page
RSC increment without manifest and validation
SC increment solely from RSC
PC increment solely from markdown composition
placeholder content treated as production content
FILTERS slot treated as FILTERS implementation
SEARCH slot treated as SEARCH implementation
Wave S4 publication counted as new scaffold
G2 authorized from scaffold contract alone
WF-R01.3.3 COMPLETE from S4 alone
```

---

## 22. Out of Scope

- Wave S4 scaffold implementation
- CATEGORY / PRODUCT / SERVICE scaffolds
- FILTERS / SEARCH partials (WF-R01.3.4)
- Registry row edits · new `block_id`
- Vocabulary Canon changes
- G2 execution authorization
- WF-R01.3.4 start
- Historical report rewrites
- Changes to `src/` in S4 pass

---

## 23. Evidence Paths

| Artefact | Path |
|----------|------|
| This contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` |
| Wave S4 REPORT | `reports/wf-r01-3-3-wave-s4-shell-matrix-scaffold-contract-v1.md` |
| LANDING manifest | `workspaces/website-factory-reference-v1/LANDING-SCAFFOLD-MANIFEST-v1.md` |
| LANDING composition | `workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md` |
| LANDING source | `workspaces/website-factory-reference-v1/src/pages/index.html` |
| BREADCRUMBS host (not scaffold) | `workspaces/website-factory-reference-v1/src/pages/breadcrumbs-reference.html` |
| PAGINATION host (not scaffold) | `workspaces/website-factory-reference-v1/src/pages/pagination-reference.html` |
| Coverage model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` |

---

## 24. Decision

| Field | Value |
|-------|-------|
| **Decision** | **ACCEPTED** — Website Factory Reference Scaffold Contract v1 is normative operator authority for Reference Scaffold minimum requirements and RSC evidence chains |
| **Wave** | WF-R01.3.3 Wave S4 — publication |
| **Metrics** | **UNCHANGED** |
| **Next task** | **WF-R01.3.3 Wave S5 — Exit Evaluation and WF-R01.3.4 Handoff** |

---

*Contract version: v1 · Authority: WF-R01.3.3 Wave S4 · T0: 2026-06-19*
