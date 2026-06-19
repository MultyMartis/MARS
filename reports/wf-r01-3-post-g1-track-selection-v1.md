# REPORT — WF-R01.3 POST-G1 TRACK SELECTION

**Artifact ID:** WF-R01.3 — Post-G1 Track Selection (v1)  
**Date:** 2026-06-19  
**Mode:** authority reconciliation + next-step authorization decision — **read-only** except this report  
**Authority reviewed:** program design · coverage model · G1 exit · reference registries · gap documents

**Honesty boundary:** Human-operated track selection. **Not** wave execution. **Not** G2 closure. **Not** partial implementation. **Not** coverage metric mutation.

---

## 1. Result

| Field | Value |
|-------|-------|
| **Status** | **COMPLETE** |
| **G1 state** | **CLOSED** — RC **32/32** · RPC **15/32** · RSC **1/10 global; 1/1 LANDING** · SC **LANDING PASS** · PC **1/1 LANDING** |
| **Parent WF-R01.3 state** | **DESIGN** (unchanged — G1 ≠ parent program COMPLETE) |
| **Selected next track** | **WF-R01.3.3 — Structural & Shell References** |
| **Decision classification** | **CHARTER PASS REQUIRED** |
| **Next Cursor task** | **WF-R01.3.3 — Structural & Shell References Charter Pass** |

---

## 2. Git Safety

| Item | Detail |
|------|--------|
| **Branch** | `mars/post-cycle8-live-tests` |
| **HEAD** | `29e311b` — `foundry: record G1 exit git result in exit report` |
| **G1 closure commits** | `10f2443` — `foundry: close WF-R01.3.2 gate G1` · `29e311b` — exit report metadata |
| **Staged files** | **None** |
| **Foreign WIP** | **Present** — MIG pilots, EAR, OCPilot, Triumph workspaces, `.recovery-temp`, unrelated project edits — **excluded** from this pass |
| **Files changed (this task)** | `reports/wf-r01-3-post-g1-track-selection-v1.md` only |
| **Selective scope** | Report artefact only |

---

## 3. Authority Reviewed

| Document | Path | Role |
|----------|------|------|
| Operational index | `projects/mars-website-factory/OPERATIONAL-INDEX.md` | G1 CLOSED sync; next task pointer |
| Roadmap | `projects/mars-website-factory/roadmap.md` | WF-R01 subprogram table; G1 state |
| Factory README | `projects/mars-website-factory/README.md` | Pack identity (not primary for R01.3 structure) |
| WF-R01 program charter | `reports/wf-r01-registry-expansion-program-charter-v1.md` | Parent CHARTERED scope |
| WF-R01 program design | `reports/foundry-registry-expansion-program-design-v1.md` | R01.3 subprogram decomposition |
| Coverage model charter | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | G0–G4 gates; five dimensions |
| LANDING completion charter | `projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md` | G1 exit; 3.3 coordination; handoff |
| G1 five-dimension exit | `reports/wf-r01-3-2-g1-five-dimension-exit-v1.md` | Canonical post-G1 metrics; candidate tracks |
| Reference expansion design | `reports/wf-r01-3-reference-expansion-program-design-v1.md` | R01.3.3–R01.3.5 definitions; wave map |
| LANDING wave design | `reports/wf-r01-3-2-landing-completion-wave-design-v1.md` | Post-G1 authorized design/execution table |
| G0 baseline | `reports/wf-r01-3-0-coverage-baseline-snapshot-v1.md` | Scaffold / SC planning denominators |
| Block gaps | `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md` | Partial implementation gaps |
| Core block library | `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md` | Block catalog |
| Block registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | 32 `block_id` SSOT |
| Site type registry | `workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md` | Core 5 site types |
| Page type registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` | RSC denominator (10) |
| Curated library index | `projects/mars-website-factory/curated-library-index-v1.md` | v0 operational rows (9) — not coverage SoT |

---

## 4. WF-R01.3 Programme Map

| ID | Name | Status | Charter | Dependencies | Evidence |
|----|------|--------|---------|--------------|----------|
| **WF-R01.3** | Reference Implementation Expansion | **DESIGN** | — (program design only) | WF-R01.1 ACCEPTED · WF-R01.2 COMPLETE · WF-R01.3.1 ACCEPTED | `reports/wf-r01-3-reference-expansion-program-design-v1.md` · `roadmap.md` R01.3 row |
| **WF-R01.3.0** | Coverage Baseline Snapshot (G0) | **PUBLISHED** | — (milestone REPORT) | WF-R01.3.1 | `reports/wf-r01-3-0-coverage-baseline-snapshot-v1.md` |
| **WF-R01.3.1** | Coverage Model & Metrics | **ACCEPTED** | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | WF-R01.1 | Charter pass `reports/wf-r01-3-1-coverage-model-charter-pass-v1.md` |
| **WF-R01.3.2** | LANDING Completion Wave | **COMPLETE** | `projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md` (**ACCEPTED**) | R01.3.1 · WF-R01.2 Gate 2 | G1 exit `reports/wf-r01-3-2-g1-five-dimension-exit-v1.md` |
| **WF-R01.3.3** | Structural & Shell References | **DEFINED / DESIGN** | **NOT FOUND** | WF-R01.2 Gate 2 · R01.3.2 (W2 bundled under G1) | `reports/wf-r01-3-reference-expansion-program-design-v1.md` § WF-R01.3.3 |
| **WF-R01.3.4** | Catalog & Vertical Profile References | **DEFINED / DESIGN** | **NOT FOUND** | **R01.3.3** · WF-R01.2 structural rows | Same design doc § WF-R01.3.4 |
| **WF-R01.3.5** | Corporate & Commerce Reference Slices | **DEFINED / DESIGN** | **NOT FOUND** | R01.3.4 Gate 2 minimum | Same design doc § WF-R01.3.5 |
| **WF-R01.3.X** | Gates, Reporting & Curated Library v2 Spec | **DEFINED / PARTIAL** | **NOT FOUND** | R01.3.1 | Same design doc § WF-R01.3.X; G0/G1 REPORTs published ad hoc |

**Not found as subprograms:** standalone `WF-R01.3.6+` IDs · `G2` as execution subprogram (G2 is a **gate**, not a chartered track).

---

## 5. WF-R01.3.3 Finding

| Field | Value |
|-------|-------|
| **Canonical name** | **Structural & Shell References** |
| **Status** | **DEFINED** in program design · **DESIGN** (no ACCEPTED charter · no execution charter file on disk) |
| **Purpose (design)** | Wave W2 shell partials (`HEADER_NAV`, `FOOTER`, `LEGAL_LINKS`); global shell scaffold; layout-component policy for `BREADCRUMBS` / `PAGINATION` |
| **Charter state** | **Absent** — glob `wf-r01-3-3*` → **0 files** |
| **Dependencies** | WF-R01.2 Gate 2 (rows) — **COMPLETE**; R01.3.2 parallel/bundle for W2 — **COMPLETE** |
| **Target site type** | Cross-cutting shell (all multi-page types); not site-type-exclusive |
| **Coverage dimensions** | RPC structural shell; RSC global shell scaffold depth; policy for layout components |
| **Gate target** | Contributed to **G1** (W2) — **largely satisfied** via WF-R01.3.2 bundling |
| **Execution waves (design)** | W2 — **executed under 3.2**; residual post-G1: nav depth extension · breadcrumbs/pagination policy · global shell scaffold |
| **Is it the direct next track?** | **Yes — as charter pass**, not as repeat W2 partial wave. Program dependency **R01.3.4 → R01.3.3** blocks catalog charter until 3.3 ACCEPTED. G1 exit lists 3.3 charter as explicit candidate #1. |
| **Evidence** | `reports/wf-r01-3-reference-expansion-program-design-v1.md` L449–457 · `projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md` § WF-R01.3.3 Coordination · `reports/wf-r01-3-2-g1-five-dimension-exit-v1.md` §22 |

**Verdict:** **WF-R01.3.3 exists, is not yet chartered, is not a placeholder, is not superseded.** Primary W2 partial deliverables were **absorbed** by WF-R01.3.2; remaining 3.3 scope is **residual shell policy + scaffold depth + layout-component policy** — still requires its own ACCEPTED charter before WF-R01.3.4.

---

## 6. G2 Definition

Extracted from `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` § Readiness Gates (binding).

| Criterion | Requirement | Current state | Gap |
|-----------|-------------|---------------|-----|
| **RPC numerator** | **≥ 20/32** (~63%) | **15/32** (~46.9%) | **−5** minimum to gate threshold |
| **Primary deliverables — PROMO blocks** | `SERVICES`, `TEAM`, `ABOUT` (W3) | **No T1+ partials** | W3 not chartered |
| **Primary deliverables — catalog structural** | `FILTERS`, `SEARCH` T1+; catalog grids W5 | Registry rows **exist**; partials **absent** | W4–W5 not chartered |
| **Primary deliverables — scaffolds** | PLP scaffold; PROMO money-page scaffold | **No** `CATEGORY_PAGE` / PROMO multi-page scaffolds | RSC **1/10** global |
| **RSC (implicit)** | Catalog + PROMO primary scaffolds per program design | **1/10** global | **9/10** page types without scaffold |
| **SC** | Template-Art **pilot** PROMO + CATALOG | LANDING **PASS** only; others **Blocked** | PROMO/CATALOG SC **Fail** |
| **PC** | Reference Compositions for new page types | **1/1 LANDING** only | PROMO/CATALOG compositions **not published** |
| **Prerequisites** | G1 closed · WF-R01.2 structural rows · v1 `block_id` binding | G1 **CLOSED** · Gate 2 **COMPLETE** · B3 STOP **pending** implementation | WF-R01.7 matrix **DESIGN** |
| **WF-A03** | G2 = **recommended precondition** only; **no auto-start** | WF-A03 **DEFERRED** | N/A for this selection |
| **Premature transition prohibition** | G2 catalog Template-Art **must not** claim before G1 exit REPORT | G1 exit **accepted** | Prohibition **lifted for planning**; execution still **unchartered** |

### G2 authority verdict

```text
G2 execution is NOT authorized
G2 planning is authorized at DESIGN level only (no ACCEPTED execution charter)
G2 requires one or more intermediate tracks (WF-R01.3.3 charter → WF-R01.3.4 + W3 PROMO wave charter/planning)
G2 authority is PRESENT as normative gate definition — not absent
```

---

## 7. Current Five-Dimension State

| Dimension | Current | Next meaningful gap |
|-----------|--------:|---------------------|
| **RC** | **32/32** | None in-scope — maintain |
| **RPC** | **15/32** | **+5** to G2 floor — `SERVICES`/`TEAM`/`ABOUT` and/or `FILTERS`/`SEARCH`/catalog grids per wave charter |
| **RSC** | **1/10** global · **1/1** LANDING | **9** page types without stub-declared scaffold (`HOME_PAGE`, `SERVICE_PAGE`, `CATEGORY_PAGE`, …) |
| **SC** | **LANDING PASS** | PROMO + CATALOG pilot blocked until G2 |
| **PC** | **1/1** LANDING | Next registered candidates: PROMO money pages · CATALOG PLP/PDP compositions (program design — not invented here) |

---

## 8. Remaining Reference Layer Gaps

### Block gaps

**15/32** blocks have T1+ partials (G1 exit inventory). **17** registry blocks lack T1+ partials:

`FEATURES` · `SERVICES` · `CATEGORIES` · `CATEGORY_GRID` · `PRODUCT_GRID` · `PRODUCT_CARD` · `REVIEWS` · `CERTIFICATES` · `TEAM` · `ABOUT` · `MAP` · `PARTNERS` · `DELIVERY` · `PAYMENT` · `CHECKOUT` · `CART` · **`FILTERS`** · **`SEARCH`**

**FILTERS / SEARCH:** registry rows **COMPLETE** (WF-R01.2 Gate 2); partials **OPEN** — assigned to **WF-R01.3.4 W4** / G2. **Not** auto-selected as immediate isolated task (charter boundary).

Evidence: `BLOCK-GAPS-v1.md` §8 · `BLOCK-REGISTRY-v1.md` footer · G1 exit §8.

### Scaffold gaps

**RSC global 1/10.** Missing scaffolds for **9** minimum `page_type` codes:

| Missing `page_type` | Typical site-type consumer |
|---------------------|----------------------------|
| `HOME_PAGE` | PROMO · CATALOG · ECOMMERCE · CORPORATE |
| `SERVICE_PAGE` | PROMO |
| `CATEGORY_PAGE` | CATALOG · ECOMMERCE |
| `PRODUCT_PAGE` | CATALOG · ECOMMERCE |
| `ABOUT_PAGE` | PROMO · CORPORATE |
| `CONTACT_PAGE` | PROMO · CORPORATE |
| `FAQ_PAGE` | Multi-type optional |
| `REVIEWS_PAGE` | Multi-type optional |
| `LEGAL_PAGE` | Multi-type |

**Exists:** `LANDING_PAGE` → `src/pages/index.html` + `LANDING-SCAFFOLD-MANIFEST-v1.md`.

Evidence: `reports/wf-r01-3-0-coverage-baseline-snapshot-v1.md` § RSC · `PAGE-TYPE-REGISTRY-v1.md`.

### Site coverage gaps

| site_type_code | SC status | Gate |
|----------------|-----------|------|
| **LANDING** | **PASS** | G1 |
| **PROMO** | **Fail / Blocked** | G2 pilot |
| **CATALOG** | **Fail** — no catalog partials/scaffolds | G2 |
| **CORPORATE** | **Fail** | G3 |
| **ECOMMERCE** | **Fail** | G3–G4 |
| **MANUFACTURER** / **AUTO** (profiles) | **Fail** | via CATALOG G2+ |
| **MARKETPLACE** (Extended) | **Deferred** | out of Core WF-R01.3 |

### Composition gaps

**PC LANDING 1/1 — closed at G1.**

Next **registered** composition candidates (program design only — **not** new candidates):

- PROMO: `SERVICE_PAGE`, `ABOUT_PAGE`, `CONTACT_PAGE`, `HOME_PAGE` hub composition
- CATALOG: `CATEGORY_PAGE`, `PRODUCT_PAGE` (+ `SEARCH_RESULTS_PAGE` routing note — **SAFE UNKNOWN** in PAGE-TYPE-REGISTRY minimum 10)

Evidence: `wf-r01-3-1-coverage-model-charter-v1.md` § Template-Art minimum sets · `wf-r01-3-reference-expansion-program-design-v1.md` wave map.

### Documentation-only drift

| Finding | Severity | Action |
|---------|----------|--------|
| `roadmap.md` / `OPERATIONAL-INDEX.md` post-G1 state | **None** — already synced at G1 closure | Update **next task pointer only** (optional — this report supersedes as selection artefact) |
| Curated library v0 snake_case vs v1 `block_id` | Low | Deferred WF-R01.3.X |
| WF-R01.7 Template-Art matrix pending | Medium | Parallel; not blocking charter pass |
| Parent WF-R01.3 remains DESIGN | Info | Expected |

**Roadmap / OPERATIONAL-INDEX reconciliation:** **not required** for metrics or G1 state — only next-task wording could be updated; deferred to avoid duplicating this report in two surfaces.

---

## 9. Candidate Tracks

| Candidate | Authority | Coverage impact | Dependencies | Risk | Readiness |
|-----------|-----------|-----------------|--------------|------|-----------|
| **WF-R01.3.3 — Structural & Shell References Charter Pass** | Program design §3.3; G1 exit candidate #1; 3.4 hard dependency | Low direct RPC (W2 done); enables shell scaffold + breadcrumbs/pagination policy for catalog corridor | WF-R01.2 ✓ · 3.2 W2 bundle ✓ | Low — narrow residual scope | **Ready for charter pass** |
| **WF-R01.3.4 — Catalog & Vertical Profile References Charter Pass** | Program design §3.4; post-G1 execution priority in wave design | High — FILTERS/SEARCH, W5 grids, RPC toward **20/32**, CATALOG scaffolds | **Blocked on 3.3 ACCEPTED** per design | Medium — BZPM doc-first; multi-artefact | **Not ready** until 3.3 charter |
| **G2 wave planning charter (composite)** | G1 exit candidate #2; coverage model G2 gate | Full G2 surface (W3+W4+W5+scaffolds) | Not a named subprogram | High — mixes site types without subprogram boundary; overlaps 3.3/3.4 | **Design-only** — no charter template |
| **PROMO W3 partials only (SERVICES/TEAM/ABOUT)** | Wave map W3 → R01.3.2/PROMO | +3 RPC toward G2 | No ACCEPTED charter; 3.2 **COMPLETE** at G1 scope | Medium — orphan wave without gate charter | **Not authorized** |
| **FILTERS + SEARCH reference completion (execution)** | WF-R01.3.4 W4 | +2 RPC; catalog structural | Task constraint **forbids** implementation in this selection pass | — | **Excluded** |
| **WF-R01.7 matrix binding** | Parent WF-R01 program | SC policy | Parallel; not Reference Layer execution | Low | **DESIGN** — wrong lane for post-G1 reference wave |
| **Reference Library hygiene (R01.3.X / curated v2)** | R01.3.X cross-cutting | Documentation | Parallel | Low | **Deferred** — not G2 bottleneck |

---

## 10. Selected Track

| Field | Value |
|-------|-------|
| **Exact track name** | **WF-R01.3.3 — Structural & Shell References** |
| **Why selected** | (1) Next **named** subprogram in program tree after WF-R01.3.2 **COMPLETE**. (2) **Formal dependency** `WF-R01.3.4 → WF-R01.3.3` blocks catalog charter. (3) G1 exit explicitly lists **WF-R01.3.3 charter pass** as candidate. (4) W2 partial work already executed under 3.2 — remaining 3.3 scope is **residual shell policy + global shell scaffold + breadcrumbs/pagination policy + nav depth** — appropriate **charter-only** pass before G2 execution corridor. (5) Preserves Registry → Reference → Composition sequencing without inventing a non-canonical “G2 mega-charter”. |
| **Why other candidates are not next** | **WF-R01.3.4** — higher bottleneck impact but **dependency-blocked** until 3.3 ACCEPTED. **G2 wave planning** — not a registered subprogram ID; would mix W3 PROMO + W4 catalog without boundary. **W3 PROMO execution** — no charter; WF-R01.3.2 closed at G1. **FILTERS/SEARCH implementation** — forbidden in this task; belongs to future 3.4 execution. **WF-R01.7 / R01.3.X hygiene** — parallel lanes, not post-G1 reference wave. |
| **Expected measurable result (charter pass)** | ACCEPTED charter defining: residual shell policy; `BREADCRUMBS`/`PAGINATION` layout-component disposition; global shell scaffold specification; nav depth extension criteria; explicit handoff preconditions to **WF-R01.3.4** and W3 PROMO wave; **zero** new partials in charter pass itself |
| **Required charter** | **CREATE** `wf-r01-3-3-structural-shell-references-charter-v1.md` (recommended filename — exact name at charter pass discretion) |

---

## 11. Decision Classification

```text
CHARTER PASS REQUIRED
```

**Not** `TRACK AUTHORIZED FOR EXECUTION` — no ACCEPTED charter exists for WF-R01.3.3.  
**Not** `ROADMAP RECONCILIATION REQUIRED` — no conflicting accepted definitions found.  
**Not** `BLOCKED — AUTHORITY CONFLICT` — G1 exit dual-candidate framing resolved by program dependency + subprogram ordering.

---

## 12. Documentation Changes

| Surface | Change |
|---------|--------|
| **roadmap.md** | **Unchanged** — G1 state already correct |
| **OPERATIONAL-INDEX.md** | **Unchanged** — G1 state already correct |
| **report** | **Created** — this artefact |
| **metrics** | **Unchanged** — RC/RPC/RSC/SC/PC not modified |

---

## 13. Git Result

| Item | Detail |
|------|--------|
| **Commit** | Pending selective commit of this report only |
| **Foreign lane** | **Excluded** |

---

## 14. Exact Next Cursor Task

```text
WF-R01.3.3 — Structural & Shell References Charter Pass
```

---

## 15. Exact Evidence Paths

- `projects/mars-website-factory/OPERATIONAL-INDEX.md`
- `projects/mars-website-factory/roadmap.md`
- `reports/wf-r01-registry-expansion-program-charter-v1.md`
- `reports/foundry-registry-expansion-program-design-v1.md`
- `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md`
- `projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md`
- `reports/wf-r01-3-2-g1-five-dimension-exit-v1.md`
- `reports/wf-r01-3-reference-expansion-program-design-v1.md`
- `reports/wf-r01-3-2-landing-completion-wave-design-v1.md`
- `reports/wf-r01-3-0-coverage-baseline-snapshot-v1.md`
- `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md`
- `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md`
- `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md`
- `workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md`
- `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md`
- `projects/mars-website-factory/curated-library-index-v1.md`
- `workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md`
- `workspaces/website-factory-reference-v1/LANDING-SCAFFOLD-MANIFEST-v1.md`

---

## 16. Stop Confirmation

```text
Selected track implementation: NOT STARTED
G2 execution: NOT STARTED
WF-A03 Pixel Factory: NOT STARTED
FILTERS: NOT IMPLEMENTED
SEARCH: NOT IMPLEMENTED
Coverage metrics: UNCHANGED
Production readiness: NOT CLAIMED
```

---

*Selection artefact: `reports/wf-r01-3-post-g1-track-selection-v1.md`*
