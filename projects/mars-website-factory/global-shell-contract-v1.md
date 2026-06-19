# Website Factory Global Shell Contract v1

**Status:** **ACCEPTED**  
**Authority:** WF-R01.3.3 Wave S1  
**Date:** 2026-06-19  
**Parent charter:** [wf-r01-3-3-structural-shell-references-charter-v1.md](wf-r01-3-3-structural-shell-references-charter-v1.md)

**Classification:** documentation-layer normative contract

**This contract is not:** runtime component · CSS framework · HTML template · CMS integration · production deployment

**Honesty boundary:** Human-operated normative authority for Website Factory shell composition. **Not** proof that all page-type scaffolds exist. **Not** G2 authorization. **Not** coverage metric accrual.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **ACCEPTED** |
| **Publication wave** | WF-R01.3.3 Wave S1 — Global Shell Contract Publication |
| **Authority state** | Normative operator contract for site-level shell across Website Factory reference and delivery projects |
| **Implementation** | Reference evidence exists for `LANDING_PAGE` only; contract applies to all registered `page_type` codes |
| **Metrics impact** | **None** — RC **32/32** · RPC **15/32** · RSC **1/10 global; 1/1 LANDING** · SC **LANDING PASS** · PC **1/1 LANDING** unchanged |

**ACCEPTED means:** Operators and scaffolds **must** conform to shell order, semantics, slots, and validation minimum defined herein unless an accepted page-type matrix entry or wave charter explicitly permits variation. **Does not** mean BREADCRUMBS/PAGINATION partials exist, multi-page scaffolds exist, or G2 is authorized.

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Name** | Website Factory Global Shell Contract |
| **Version** | v1 |
| **ID** | Global Shell Contract v1 |
| **Program** | WF-R01.3.3 — Structural & Shell References |
| **Scope** | Cross-cutting site-level structural frame for all multi-page `site_type_code` consumers |
| **Canonical path** | `projects/mars-website-factory/global-shell-contract-v1.md` |

---

## 3. Authority and Evidence

| Document | Path | Role |
|----------|------|------|
| WF-R01.3.3 charter | [wf-r01-3-3-structural-shell-references-charter-v1.md](wf-r01-3-3-structural-shell-references-charter-v1.md) | Parent authority; §7 shell stack; §8 nav depth; §12 page-type matrix |
| Charter pass REPORT | [wf-r01-3-3-structural-shell-references-charter-pass-v1.md](../../reports/wf-r01-3-3-structural-shell-references-charter-pass-v1.md) | Acceptance evidence |
| Coverage model | [wf-r01-3-1-coverage-model-charter-v1.md](wf-r01-3-1-coverage-model-charter-v1.md) | Five dimensions; validation outcomes; RSC accounting |
| LANDING completion | [wf-r01-3-2-landing-completion-charter-v1.md](wf-r01-3-2-landing-completion-charter-v1.md) | G1 shell bundle |
| G1 five-dimension exit | [wf-r01-3-2-g1-five-dimension-exit-v1.md](../../reports/wf-r01-3-2-g1-five-dimension-exit-v1.md) | Verified shell order evidence |
| Vocabulary Canon | [foundry-vocabulary-canon-charter-v1.md](foundry-vocabulary-canon-charter-v1.md) | F3 structural subtype |
| Layout shell governance | [layout-shell-governance.md](layout-shell-governance.md) | HEADER ≠ HERO |
| Block registry | [BLOCK-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md) | HEADER_NAV, FOOTER, LEGAL_LINKS rows |
| Page type registry | [PAGE-TYPE-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md) | Minimum 10 `page_type` codes |
| LANDING reference composition | [REFERENCE-COMPOSITION-v1.md](../../workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md) | Reference shell implementation |
| LANDING scaffold manifest | [LANDING-SCAFFOLD-MANIFEST-v1.md](../../workspaces/website-factory-reference-v1/LANDING-SCAFFOLD-MANIFEST-v1.md) | RSC stub evidence |

**Reference implementation evidence (LANDING_PAGE):**

- `workspaces/website-factory-reference-v1/src/pages/index.html`
- `workspaces/website-factory-reference-v1/src/partials/sections/header-nav.html`
- `workspaces/website-factory-reference-v1/src/partials/sections/footer.html`
- `workspaces/website-factory-reference-v1/src/partials/components/legal-links.html`

---

## 4. Purpose

This contract defines the **canonical site-level structural frame** shared across one or more `page_type` surfaces in Website Factory projects.

It establishes:

1. What constitutes global shell versus page content.
2. Mandatory shell region order and singularity rules.
3. Site-level and local semantic element boundaries.
4. Composition rules for `LEGAL_LINKS` inside `FOOTER`.
5. Navigation depth model L0–L3 and surface assignment.
6. Shell slot requirements without creating new Registry IDs.
7. Page-type applicability matrix derived from registered types only.
8. Implementation-neutral responsive, accessibility, asset, and validation minimums.
9. Scaffold integration and coverage accounting boundaries.
10. Handoff inputs for WF-R01.3.3 Waves S2–S5 and WF-R01.3.4.

**Out of scope for this contract:** BREADCRUMBS/PAGINATION partial implementation (S2/S3), catalog scaffolds (WF-R01.3.4), FILTERS/SEARCH, new `block_id` rows, Vocabulary Canon amendments, production deployment claims.

---

## 5. Global Shell Definition

```text
Global Shell = site-level structural frame shared across one or more page types.
```

### Minimum shell structure

```text
HEADER_NAV
MAIN
FOOTER
└── LEGAL_LINKS
```

### Binding rules

| Rule | Requirement |
|------|-------------|
| Shell order | `HEADER_NAV` **before** `MAIN`; `FOOTER` **after** `MAIN`; `LEGAL_LINKS` **compositionally inside** `FOOTER` |
| Page content boundary | Global shell is **not** page content — marketing, conversion, and page-specific blocks live inside `MAIN` only |
| Site-level singularity | At most **one** site-level `HEADER_NAV` per document; exactly **one** `MAIN`; at most **one** site-level `FOOTER` |
| HEADER_NAV optional case | Absence of site-level `HEADER_NAV` permitted **only** when page-type matrix directly allows (e.g. minimal `LANDING_PAGE`) |
| FOOTER / LEGAL_LINKS | Applied per page-type matrix; when required, `LEGAL_LINKS` nests in `FOOTER`, not as sibling site footer |
| Local semantics | Local semantic `<header>` and `<footer>` inside cards, articles, or product tiles are **permitted** — they are **not** global shell |
| Local identity | Local elements **must not** use site-level shell identity (duplicate landmarks, conflicting `data-block-id` for shell blocks, or false global nav) |
| HEADER ≠ HERO | Global navigation shell must not absorb hero or conversion first-screen content — [layout-shell-governance.md](layout-shell-governance.md) |
| Reference baseline | [REFERENCE-COMPOSITION-v1.md](../../workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md) is verified evidence for `LANDING_PAGE`; other page types may vary slot population while preserving shell semantics |

### Identity attributes (reference / validation)

- `data-block-id` on shell partials is **reference and validation identity** in the Website Factory reference workspace — **not** mandatory public API for every production site without a separate binding contract.
- Project-specific CSS class naming is **allowed**; this contract does **not** mandate universal class names for delivery projects.

### Contextual extensions (not immutable shell identity)

Between `HEADER_NAV` and `MAIN` content lead, or within `MAIN` top zone / list bottom:

- **BREADCRUMBS** — contextual slot; see §12
- **PAGINATION** — contextual slot at list bottom; see §12

These are **page-type shell extensions**, not replacements for the four-zone shell stack.

---

## 6. Canonical Shell Order

### DOM / include order (normative)

```text
1. HEADER_NAV          (site-level <header> — when required/allowed)
2. MAIN                (single <main> — always)
   └── page-specific composition blocks
3. FOOTER              (site-level <footer> — when required)
   └── LEGAL_LINKS      (nested composition — when required)
```

### Verified LANDING evidence

| Check | Expected | LANDING reference |
|-------|----------|-------------------|
| Site-level `<header>` count | 0 or 1 per page type | **1** — `header-nav.html` |
| `<main>` count | **1** | **1** — `<main id="main">` in `index.html` |
| Site-level `<footer>` count | 0 or 1 per page type | **1** — `footer.html` after `</main>` |
| HEADER_NAV before MAIN | Yes | Yes |
| FOOTER after MAIN | Yes | Yes |
| LEGAL_LINKS inside FOOTER | When required | Yes — `data-composition-slot="legal_links"` |
| FOOTER inside MAIN | **Forbidden** | Not present |
| Duplicate site-level shell | **Forbidden** | Not present |

**Auxiliary modules** (e.g. modal overlay, sticky CTA) may exist outside `MAIN` and are **not** site shell — documented in Reference Composition for LANDING.

---

## 7. Site-Level Semantic Contract

| Element | Scope | Rule |
|---------|-------|------|
| Site-level `<header>` | Document | Owned by `HEADER_NAV` when present; primary global navigation landmark |
| `<main>` | Document | Exactly one; contains page-specific composition only |
| Site-level `<footer>` | Document | Owned by `FOOTER` when present; site closing shell |
| Local `<header>` | Component / card / article | Permitted; must not duplicate site-level header landmark without distinct accessible name |
| Local `<footer>` | Component / card / article | Permitted; must not duplicate site-level footer landmark without distinct accessible name |
| `<nav>` in shell | HEADER_NAV, FOOTER nav zones, LEGAL_LINKS | Each navigation region requires accessible name (`aria-label` or visible heading association) |

**Singularity summary:**

```text
site-level HEADER_NAV  → 0 or 1 per document (page-type matrix)
MAIN                   → exactly 1 per document
site-level FOOTER      → 0 or 1 per document (page-type matrix)
LEGAL_LINKS            → nested in FOOTER when required; not standalone site footer
```

---

## 8. Shell vs Page Content

### Boundary rules

| Zone | Contains | Must not contain |
|------|----------|------------------|
| **Global shell** | Brand, global nav, site footer, compliance link cluster, footer secondary nav | HERO body, pricing grids, lead forms, FAQ content, legal document body |
| **MAIN** | Page-specific blocks per Reference Composition or page-type contract | Site-level HEADER_NAV, site-level FOOTER, standalone LEGAL_LINKS as top-level shell sibling |
| **Contextual slots** | BREADCRUMBS, PAGINATION (when page type requires) | Primary global IA; hero content; filter panels masquerading as header |

### Page content definition

**Page content** = all blocks and sections inside the single `<main>` element forming the page-specific composition for the active `page_type`.

Shell blocks (`HEADER_NAV`, `FOOTER`, nested `LEGAL_LINKS`) are **structural frame**, not page content blocks, even when they contain navigational links or marketing-adjacent placeholders.

### Local semantic elements

- Card headers, article headers, product tile footers, pricing card headers — **allowed**.
- Validation **must not** treat local `<header>` / `<footer>` as site-level shell duplication errors.
- Local elements **must not** carry site-level shell `block_id` identity or present as global primary navigation.

### Duplicate prevention

- No second site-level `<header>` acting as global nav.
- No second site-level `<footer>`.
- No `LEGAL_LINKS` rendered as a sibling of `FOOTER` at document root when matrix requires nested composition.
- One UI surface must not claim multiple canonical block identities without an explicit composition contract.

---

## 9. Shell Region Contracts

### HEADER_NAV

```text
HEADER_NAV = F3 Structural Block
Navigation depth = L0
```

**Responsible for:**

- Brand identity (logo / wordmark)
- Global primary navigation
- Optional utility or contact summary elements
- Optional compact action (e.g. callback trigger — compositional, not a MAIN CTA block)
- Mobile navigation entry and panel

**Not responsible for:**

- HERO or conversion first-screen content
- BREADCRUMBS
- FILTERS or facet controls
- SEARCH results or query implementation
- Page-local tabs or in-content section nav
- Footer navigation or legal compliance links

**Registry:** Tier A `block_id` — reference partial exists (WF-R01.3.2 Wave C2). **Must not be re-implemented** under WF-R01.3.3.

**Mega-menu policy:** Mega-menu is a **variation or pattern inside** `HEADER_NAV` / section navigation — **not** a new `block_id` unless a separate waiver charter authorizes one.

---

### MAIN

```text
MAIN = semantic content region (not a Registry block)
```

**Rules:**

- Exactly **one** `<main>` per document.
- Shell blocks must **not** be incorrectly nested inside `MAIN`.
- Page-specific blocks form the **Composition** for the active `page_type`.
- Block sequence is determined by page type, Reference Composition, or wave charter — not by shell contract alone.
- Contextual slots (BREADCRUMBS, PAGINATION) may appear at MAIN boundaries per page-type matrix but remain distinct from shell blocks.

**LANDING evidence:** HERO through CONTACTS blocks inside `<main id="main">` — see [REFERENCE-COMPOSITION-v1.md](../../workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md) § MAIN order.

---

### FOOTER

```text
FOOTER = F3 Structural Block
```

**Responsible for:**

- Site-level closing shell
- Secondary navigation (L1–L3 bands inside footer columns)
- Contact / support summary zone
- Brand / company summary
- Compliance composition slot for `LEGAL_LINKS`
- Copyright zone

**Is not:**

- A separate CONTACTS block (MAIN `contact_block` remains page content)
- A standalone `LEGAL_LINKS` block at document root
- Replacement for `HEADER_NAV`
- Mandatory CTA or conversion block

**Registry:** Tier A `block_id` — reference partial exists (WF-R01.3.2 Wave B1). **Must not be re-implemented** under WF-R01.3.3.

---

### LEGAL_LINKS

```text
LEGAL_LINKS = F3 Structural Block
Navigation depth = L3
Composition owner = FOOTER
```

**Contains:** Links to legal and compliance routes (privacy, terms, cookies, company details, etc.).

**Does not contain:** Full legal document body text — that belongs on `LEGAL_PAGE` content, not in the link cluster.

**Registry:** Tier A `block_id` — reference partial exists (WF-R01.3.2 Wave B2), nested via `data-composition-slot="legal_links"` in FOOTER. **Must not be re-implemented** under WF-R01.3.3.

---

## 10. LEGAL_LINKS Composition

### Composition rule

```text
FOOTER
└── bottom zone
    └── LEGAL_LINKS (nested include / composition slot)
```

### Binding requirements

| Requirement | Specification |
|-------------|---------------|
| Owner | `FOOTER` is the composition owner |
| Placement | Bottom slot of site-level footer — not before footer primary columns unless design system documents explicit variation that preserves semantics |
| DOM | `<nav>` (or equivalent) with accessible name inside `<footer>` |
| Independence | `LEGAL_LINKS` is **not** a sibling site-level footer region |
| Page-type | Required on most page types per matrix §13; `LEGAL_PAGE` uses simplified body — global footer + legal links on other routes remain required |

### Reference evidence

- `footer.html` → `wf-footer__legal-slot` with `data-composition-slot="legal_links"`
- `legal-links.html` included inside that slot

---

## 11. Navigation Depth Model

Navigation level is determined by **purpose**, not visual position on the page.

| Level | Name | Role | Typical surfaces |
| ----- | ---- | ---- | ---------------- |
| **L0** | Global | Site-wide primary orientation | `HEADER_NAV` |
| **L1** | Section | Category, hub, or vertical navigation | Category nav, hub tabs, mega-menu sections, `CATEGORIES` on hub pages |
| **L2** | Contextual | Current hierarchy or result-set navigation | BREADCRUMBS, PAGINATION, FILTERS facets |
| **L3** | Utility / compliance | Supporting, service, and legal navigation | `LEGAL_LINKS`, footer secondary links |

### Surface assignment rules

| Rule | Requirement |
|------|-------------|
| Footer nav ≠ L0 | Navigation inside `FOOTER` does **not** become L0 primary navigation |
| BREADCRUMBS ≠ HEADER_NAV | Orientation trail is contextual (L2), not global primary nav |
| PAGINATION ≠ PROCESS | List paging is L2; step narrative belongs to `PROCESS` / STEPPER |
| FILTERS ≠ primary nav | Facet refinement is L2; not global IA |
| SEARCH | Separate structural surface (Tier A `block_id`); query entry typically L0 header zone; results context L2 — owned by WF-R01.3.4 |
| Single identity | One UI element must not simultaneously hold multiple canonical block identities without composition contract |
| Mega-menu | Pattern inside HEADER_NAV / L1 — not automatic new Registry block |

---

## 12. Shell Slots

**Slot naming policy:** No formal MARS slot ID Registry exists at v1. This contract uses **descriptive contract slot names** — not registered `block_id` values.

| Descriptive slot | Purpose | Typical owner | Required state |
| ---------------- | ------- | ------------- | -------------- |
| **header slot** | Site-level HEADER_NAV mount point | Page scaffold / layout | Page-type dependent (REQ / OPT) |
| **main slot** | Single MAIN composition region | Page scaffold | **REQ** — all page types |
| **footer slot** | Site-level FOOTER mount point | Page scaffold | Page-type dependent (REQ / OPT) |
| **legal-links slot** | LEGAL_LINKS nested in FOOTER | FOOTER composition | Page-type dependent; nested when FOOTER REQ |
| **breadcrumbs slot** | Contextual hierarchy trail | MAIN top / post-header zone | Page-type dependent (REQ / POL / —) |
| **pagination slot** | List paging controls | MAIN bottom / pre-footer zone | Page-type dependent (REQ / POL / FORB) |
| **search slot** | Query entry / results chrome | Typically header slot + results page | WF-R01.3.4; not shell v1 implementation |

### Slot rules

- Slots describe **composition mount points** — they do **not** create Registry rows.
- Forbidden: treating documentation-only shell policy as populated scaffold slots for coverage.
- Forbidden: silently merging SEARCH into HEADER_NAV without composition declaration.

---

## 13. Page-Type Applicability

Registered `page_type` codes from [PAGE-TYPE-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md) minimum set (10).

**Legend:** **REQ** = Required on reference scaffold · **OPT** = Optional / minimal · **POL** = Policy-dependent (see notes) · **FORB** = Forbidden · **—** = Not required

| Page type | HEADER_NAV | MAIN | BREADCRUMBS slot | PAGINATION slot | FOOTER | LEGAL_LINKS |
| --------- | ---------- | ---- | ---------------- | --------------- | ------ | ----------- |
| `LANDING_PAGE` | OPT | REQ | — | FORB | REQ | REQ |
| `HOME_PAGE` | REQ | REQ | POL | POL | REQ | REQ |
| `SERVICE_PAGE` | REQ | REQ | POL | — | REQ | REQ |
| `CATEGORY_PAGE` | REQ | REQ | REQ | REQ | REQ | REQ |
| `PRODUCT_PAGE` | REQ | REQ | REQ | — | REQ | REQ |
| `ABOUT_PAGE` | REQ | REQ | REQ | — | REQ | REQ |
| `CONTACT_PAGE` | REQ | REQ | POL | — | REQ | REQ |
| `FAQ_PAGE` | REQ | REQ | POL | POL | REQ | REQ |
| `REVIEWS_PAGE` | REQ | REQ | POL | POL | REQ | REQ |
| `LEGAL_PAGE` | REQ | REQ | POL | — | REQ | REQ |

### POL notes (from WF-R01.3.3 charter)

| Page type | Slot | Charter stance |
|-----------|------|----------------|
| `HOME_PAGE` | BREADCRUMBS | Recommended (R) — shallow hub trail acceptable |
| `HOME_PAGE` | PAGINATION | Policy-dependent (P) — only when home exposes paginated grid |
| `SERVICE_PAGE` | BREADCRUMBS | Recommended — parent hub link |
| `CATEGORY_PAGE` | BREADCRUMBS | Obligatory (O) on PLP reference scaffold |
| `CATEGORY_PAGE` | PAGINATION | Obligatory (O) on PLP |
| `PRODUCT_PAGE` | BREADCRUMBS | Obligatory — category → product trail |
| `ABOUT_PAGE` | BREADCRUMBS | Obligatory on internal corporate page |
| `CONTACT_PAGE` | BREADCRUMBS | Recommended — optional shallow trail |
| `FAQ_PAGE` | BREADCRUMBS | Recommended |
| `FAQ_PAGE` | PAGINATION | Policy-dependent — only if FAQ hub is paginated |
| `REVIEWS_PAGE` | BREADCRUMBS | Recommended |
| `REVIEWS_PAGE` | PAGINATION | Policy-dependent — paginated review lists |
| `LEGAL_PAGE` | BREADCRUMBS | Recommended — minimal trail |

**`LEGAL_PAGE` note:** Global `FOOTER` + `LEGAL_LINKS` on other routes remain required; legal document body is not a marketing block stack — [LEGAL-PAGE-CONTRACT-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/LEGAL-PAGE-CONTRACT-v1.md).

### Planned / not in Registry v1 minimum

**`SEARCH_RESULTS_PAGE`:** Not registered in PAGE-TYPE-REGISTRY-v1 minimum 10. **Planned reference note only** — when scaffolded under WF-R01.3.4: HEADER_NAV REQ, BREADCRUMBS POL (R), PAGINATION REQ (O), FOOTER REQ, LEGAL_LINKS REQ. **Not** an active Registry identity in this contract.

---

## 14. Responsive Contract

**Implementation-neutral** — breakpoints belong to the project design system, not Website Factory global policy.

### Required outcomes

| Outcome | Requirement |
|---------|-------------|
| Semantic order | Shell preserves HEADER_NAV → MAIN → FOOTER semantic order on all viewports |
| DOM vs visual | Visual reorder (CSS grid/flex) must not change meaningful DOM sequence without documented accessibility justification |
| Navigation access | Global navigation remains reachable; mobile entry point required when HEADER_NAV REQ |
| Mobile trigger state | Mobile menu trigger synchronizes accessible state (`aria-expanded`, `aria-controls`) |
| Overflow | Shell must not introduce persistent horizontal overflow at supported minimum viewport |
| Footer adaptation | FOOTER columns may stack; LEGAL_LINKS may wrap |
| MAIN clearance | MAIN content must not be permanently obscured by fixed/sticky shell without offset strategy |
| Sticky behavior | Sticky or fixed HEADER_NAV is an **allowed variation**, not mandatory |
| Breakpoints | **No** universal pixel breakpoints in this contract — e.g. **do not** treat `1024px` as Website Factory global breakpoint |

---

## 15. Accessibility Minimum

**Minimum shell accessibility floor** — not a WCAG certification claim.

| Requirement | Specification |
|-------------|---------------|
| Main landmark | Exactly one `<main>` |
| Navigation names | Each shell navigation region has accessible name |
| Mobile trigger | Toggle has `aria-expanded` and `aria-controls`; label reflects open/close state |
| Hidden navigation | Visually hidden nav excluded from interaction when collapsed (focus trap / visibility policy per implementation) |
| Keyboard | Shell links and controls keyboard operable |
| Focus | Visible focus indicators on interactive shell controls |
| Heading flow | Page content inside MAIN maintains logical heading hierarchy |
| Landmark duplication | Shell landmarks not duplicated without distinct accessible labels |
| LEGAL_LINKS | Legal links keyboard reachable |
| Text scaling | Shell remains functional at increased text sizes |
| Color | Do not rely on color alone for state communication |
| Local landmarks | Card/article headers and footers must not create false global landmark ambiguity |

---

## 16. Asset and JavaScript Contract

| Rule | Policy |
|------|--------|
| Shell dependencies | Shell regions may require CSS and JS |
| Manifest | Dependencies must be explicitly listed in scaffold manifest |
| Graceful failure | JS enhancements must fail gracefully |
| Progressive enhancement | Absence of JS must not hide critical page content inside MAIN |
| Mobile menu | Mobile navigation behavior may require JS |
| Asset identity | Belongs to project implementation — not global Factory runtime |
| Runtime boundary | Global Shell Contract does **not** define shared production runtime |
| Framework neutrality | Do not assume jQuery, SPA framework, or CMS |
| Credentials | Do not embed production credentials, client URLs, or client data in reference contracts |
| Initialization | One shell module must not initialize twice on the same page |

**LANDING reference JS evidence:** `header_nav.js` (`data-module="header-nav"`) — mobile toggle with `aria-expanded`; listed in Reference Composition § JavaScript mapping.

---

## 17. Scaffold Integration Contract

### Shell-ready scaffold must document

```text
page identity (page_type, title, route notes)
shell region mapping
HEADER_NAV mapping
MAIN composition region
optional contextual slots (breadcrumbs, pagination)
FOOTER mapping
LEGAL_LINKS composition (nested)
asset mapping (SCSS imports)
JS mapping (init hooks)
build evidence (npm run build PASS)
validation evidence (wave REPORT)
```

### Distinctions (binding)

```text
Shell Contract ≠ Scaffold
Scaffold ≠ Reference Composition
Reference Composition ≠ Built page
Built page ≠ Verified page
Verified page ≠ Production Pass
```

### Coverage boundary

- Publishing this Global Shell Contract **does not** increase RSC, RPC, SC, or PC.
- RSC increases **only** after factual scaffold artefact, manifest, and required evidence per [wf-r01-3-1-coverage-model-charter-v1.md](wf-r01-3-1-coverage-model-charter-v1.md).

---

## 18. Validation Contract

### Minimum shell validation checks

| Check | Expected result |
|-------|-----------------|
| Site-level HEADER_NAV count | 0 or 1 according to page type |
| MAIN count | **1** |
| Site-level FOOTER count | 0 or 1 according to page type |
| Shell DOM order | HEADER_NAV → MAIN → FOOTER (when present) |
| LEGAL_LINKS nesting | Nested in FOOTER when required by matrix |
| Duplicate block identity | No duplicate site-level shell block identity |
| Unresolved includes | Build must resolve all shell includes |
| Required assets | SCSS/JS referenced in manifest present |
| Keyboard sanity | Shell controls operable via keyboard |
| Mobile navigation sanity | Toggle state matches panel visibility policy |
| Overflow sanity | No persistent horizontal shell overflow |
| Build result | `npm run build` PASS for reference/scaffold workspace |

**Local card `<header>` / `<footer>`:** **Not** validation errors.

### Validation outcomes (distinct)

```text
BUILT
STRUCTURALLY VALIDATED
FIDELITY VERIFIED
PRODUCTION PASS
```

```text
BUILT ≠ STRUCTURALLY VALIDATED ≠ FIDELITY VERIFIED ≠ PRODUCTION PASS
```

Shell structural validation may pass at **STRUCTURALLY VALIDATED** without pixel fidelity or production acceptance.

---

## 19. Coverage Accounting

### Metrics at Wave S1 publication (unchanged)

| Dimension | Value |
|-----------|-------|
| **RC** | **32/32** |
| **RPC** | **15/32** |
| **RSC** | **1/10** global · **1/1** LANDING |
| **SC** | **LANDING PASS** |
| **PC** | **1/1** LANDING |

### Global Shell Contract impact

| Action | RPC | RSC | SC | PC |
|--------|-----|-----|----|----|
| Publish Global Shell Contract (S1) | **No** | **No** | **No** | **No** |

This contract is a **prerequisite / evidence contract** for future scaffolds and compositions. Documentation without implementation evidence **must not** accrue coverage.

### Future deltas (execution waves only — not S1)

| Potential delta | Condition |
|-----------------|-----------|
| BREADCRUMBS T1+ partial (S2) | Implementation + build PASS + REPORT |
| PAGINATION T1+ partial (S3) | Implementation + build PASS + REPORT |
| Multi-page scaffold | Built page + manifest + build PASS → +1 RSC per `page_type` |

---

## 20. Allowed Variations

| Variation | Constraint |
|-----------|------------|
| Sticky or static HEADER_NAV | Must preserve semantics and a11y minimum |
| Compact or expanded FOOTER | Column count flexible |
| Desktop / mobile nav representations | Same IA; different presentation |
| FOOTER column layout | Stack on narrow viewports |
| Optional utility bar | Must not duplicate L0 without declaration |
| Optional contact / action in header | Compositional only — not MAIN CTA block |
| Page types without HEADER_NAV | Only when matrix allows (e.g. minimal LANDING) |
| Simplified legal shell on LEGAL_PAGE body | Global footer on other routes still required |
| Project-specific class naming | Allowed |
| CMS-specific rendering | Allowed if shell semantics preserved |

Variations **must not** violate: semantic order · vocabulary identity · accessibility minimum · duplicate prevention · coverage evidence rules.

---

## 21. Forbidden Compositions

```text
FOOTER inside MAIN
HEADER_NAV inside HERO
HERO inside HEADER_NAV
LEGAL_LINKS as full legal page content
two independent site-level headers
two independent site-level footers
BREADCRUMBS used as HEADER_NAV
PAGINATION used as PROCESS
SEARCH silently merged into HEADER_NAV without composition declaration
FILTERS treated as primary navigation
documentation-only shell counted as scaffold coverage
build PASS claimed as production acceptance
re-implementation of HEADER_NAV, FOOTER, or LEGAL_LINKS under WF-R01.3.3 (W2 complete)
```

---

## 22. Relationship to Future Waves

| Wave | Purpose | Type | S1 handoff |
|------|---------|------|------------|
| **S1** | Global Shell Contract publication | Documentation | **This contract** |
| **S2** | BREADCRUMBS reference partial | Implementation | Shell boundaries · breadcrumbs slot · L2 depth · validation minimum |
| **S3** | PAGINATION reference partial | Implementation | Shell boundaries · pagination slot · L2 depth · list surface rules |
| **S4** | Page-Type Shell Matrix and Scaffold Contract publication | Documentation | Matrix refinement · scaffold template notes |
| **S5** | Exit evaluation and WF-R01.3.4 handoff | Evaluation | Five-dimension delta · handoff package |

**S1 → S2/S3 inputs:**

- Shell vs page content boundaries
- Contextual slot rules (breadcrumbs, pagination)
- Navigation depth L0–L3
- Validation minimum
- Coverage accounting (no accrual for policy docs)

**Not started by S1:** S2 · S3 · S4 · S5 · WF-R01.3.4 · G2 execution

---

## 23. Out of Scope

- HTML / SCSS / JS changes in Wave S1
- BREADCRUMBS / PAGINATION partial implementation
- FILTERS / SEARCH partials
- Registry row edits; new `block_id`
- Vocabulary Canon amendments
- PROMO / catalog scaffolds (WF-R01.3.4)
- G2 authorization or closure
- WF-A03 Pixel Factory
- Universal CSS class mandate for all delivery projects
- WCAG certification claims
- Production deployment claims

---

## 24. Evidence Paths

| Artefact | Path |
|----------|------|
| This contract | `projects/mars-website-factory/global-shell-contract-v1.md` |
| Wave S1 REPORT | `reports/wf-r01-3-3-wave-s1-global-shell-contract-v1.md` |
| WF-R01.3.3 charter | `projects/mars-website-factory/wf-r01-3-3-structural-shell-references-charter-v1.md` |
| G1 exit | `reports/wf-r01-3-2-g1-five-dimension-exit-v1.md` |
| LANDING composition | `workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md` |
| LANDING page | `workspaces/website-factory-reference-v1/src/pages/index.html` |
| HEADER_NAV partial | `workspaces/website-factory-reference-v1/src/partials/sections/header-nav.html` |
| FOOTER partial | `workspaces/website-factory-reference-v1/src/partials/sections/footer.html` |
| LEGAL_LINKS partial | `workspaces/website-factory-reference-v1/src/partials/components/legal-links.html` |
| Page type registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` |
| Block registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` |
| Coverage model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` |

---

## 25. Decision

| Field | Value |
|-------|-------|
| **Decision** | **ACCEPTED** — Website Factory Global Shell Contract v1 is normative documentation-layer authority for site-level shell composition across Website Factory |
| **Wave** | WF-R01.3.3 Wave S1 — **COMPLETE** (publication) |
| **Metrics** | **UNCHANGED** |
| **Next task** | **WF-R01.3.3 Wave S2 — BREADCRUMBS Reference Partial** |
| **G2** | **NOT AUTHORIZED** |

---

*Contract version: v1 · Authority: WF-R01.3.3 Wave S1 · T0: 2026-06-19*
