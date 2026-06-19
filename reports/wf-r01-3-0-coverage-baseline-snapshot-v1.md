# REPORT — WF-R01.3.0 COVERAGE BASELINE SNAPSHOT

**Artifact ID:** WF-R01.3.0 — Coverage Baseline Snapshot (v1)  
**Date:** 2026-06-19  
**Mode:** metrics snapshot — **documentation only**; **no** partials, **no** registry edits, **no** new IDs, **no** implementation

**Authority consumed:**

| ID | Artifact |
|----|----------|
| Metrics charter | [wf-r01-3-1-coverage-model-charter-v1.md](../projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md) (**ACCEPTED** T0 2026-06-19) |
| Program design | [wf-r01-3-reference-expansion-program-design-v1.md](wf-r01-3-reference-expansion-program-design-v1.md) |
| Roadmap / index | [roadmap.md](../projects/mars-website-factory/roadmap.md) · [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) |
| Vocabulary | [foundry-vocabulary-canon-charter-v1.md](../projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md) |
| WF-R01 | [wf-r01-registry-expansion-program-charter-v1.md](wf-r01-registry-expansion-program-charter-v1.md) · [wf-r01-1-v0-v1-binding-charter-v1.md](wf-r01-1-v0-v1-binding-charter-v1.md) · [wf-r01-2-structural-blocks-charter-v1.md](../projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md) |

**Evidence surfaces (repo fact, measured 2026-06-19):**

| Surface | Location |
|---------|----------|
| Block registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` |
| Site / page registries | `workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md` · `page-architecture/PAGE-TYPE-REGISTRY-v1.md` |
| Reference partials | `workspaces/website-factory-reference-v1/src/partials/sections/` |
| Reference scaffolds | `workspaces/website-factory-reference-v1/src/pages/` |
| Curated library (operational RPC view) | [curated-library-index-v1.md](../projects/mars-website-factory/curated-library-index-v1.md) |
| Golden slice pointer | [golden-implementation-slice-v1.md](../projects/mars-website-factory/golden-implementation-slice-v1.md) |
| Build verification | `npm run build` in reference workspace — **PASS** (2026-06-19) |

**Honesty boundary:** This snapshot **measures** FOUNDRY (Website Factory ecosystem) maturity. **Not** runtime, **not** wave execution, **not** proof that Template-Art is production-ready beyond declared G0 LANDING HITL pilot scope.

---

## Executive Summary

Первый официальный замер зрелости Reference Layer после ACCEPTED charter WF-R01.3.1. Bottleneck подтверждён:

```text
Registry Coverage (RC)  >>  Reference Partial Coverage (RPC)  >>  Site Coverage (SC)
Page Coverage (PC)      ⊥  RPC (orthogonal — planning matrices exist; compositions not published)
```

| Dimension | Baseline | Denominator policy |
|-----------|----------|-------------------|
| **RC** | **29/32** (90.6%) | 29 Core `block_id` rows + 3 structural Tier A terms (vocabulary only) |
| **RPC** | **9/32** (~28.1%) | Charter-aligned partial-file count; strict unique `block_id` = **8/32** (25.0%) |
| **RSC** | **1/10** (10%) global · **1/1** LANDING wave | PAGE-TYPE-REGISTRY-v1 minimum set |
| **SC** | **0/8** full pass · **1/8** partial (LANDING) | Task list + vertical profiles per program design |
| **PC** | **0/1** formal (LANDING active wave) | Reference Composition docs — **not published** |

**Current Gate:** **G0** (Baseline) — RPC **9/32**, golden slice exists, LANDING Template-Art **HITL pilot only**.

**Registry ≠ buildability:** 29 documented Core blocks **не** означают Factory-ready; оператор обязан цитировать **RPC + SC**, не RC alone.

---

## RC

**Definition (WF-R01.3.1):** Share of in-scope vocabulary with registry row + minimum BLOCK-CONTRACT.

### Numerator / denominator

| Slice | Numerator | Denominator | % | Notes |
|-------|-----------|-------------|---|-------|
| **Core blocks** | **29** | **29** | 100% | All Core `block_id` rows in [BLOCK-REGISTRY-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md) |
| **Structural Tier A** | **0** | **3** | 0% | `HEADER_NAV`, `FILTERS`, `SEARCH` — vocabulary **ACCEPTED** (WF-R01.2); **registry rows not started** (Gate 2) |
| **Combined (preferred REPORT)** | **29** | **32** | **90.6%** | Post–T0 denominator policy per charter |

### Core `block_id` inventory (29 — all documented)

`HERO` · `BENEFITS` · `FEATURES` · `SERVICES` · `CATEGORIES` · `CATEGORY_GRID` · `PRODUCT_GRID` · `PRODUCT_CARD` · `PRICING` · `PROCESS` · `CASES` · `TESTIMONIALS` · `REVIEWS` · `TRUST` · `CERTIFICATES` · `TEAM` · `ABOUT` · `FAQ` · `CTA` · `LEAD_FORM` · `CONTACTS` · `MAP` · `PARTNERS` · `DELIVERY` · `PAYMENT` · `CHECKOUT` · `CART` · `LEGAL_LINKS` · `FOOTER`

### Structural gap (0/3 registry rows)

| Term | Registry row | BLOCK-CONTRACT row | Vocabulary (WF-R01.2) |
|------|--------------|-------------------|------------------------|
| `HEADER_NAV` | **Absent** | **Absent** | Tier A — mandatory |
| `FILTERS` | **Absent** | **Absent** | Tier A — mandatory |
| `SEARCH` | **Absent** | **Absent** | Tier A — mandatory |

**RC verdict:** Vocabulary layer **near-complete** for Core 29; structural promotion **blocked** on WF-R01.2 Gate 2 execution (registry row creation — **not started** per OPERATIONAL-INDEX).

---

## RPC

**Definition:** Share of in-scope `block_id` with **T1+** partial in reference workspace (`src/partials/sections/`), `npm run build` **PASS**.

### Numerator / denominator

| Counting method | Numerator | Denominator | % |
|-----------------|-----------|-------------|---|
| **Charter baseline (partial files)** | **9** | **32** | **~28.1%** |
| **Strict unique `block_id`** | **8** | **32** | **25.0%** |

**Denominator:** 32 = 29 Core + 3 structural Tier A (in program scope post–WF-R01.2 ACCEPTED).

**Build evidence:** `npm run build` — **PASS** (reference workspace, 2026-06-19).

### Existing partials (9 files — all T1+)

| Partial file | v1 `block_id` (binding) | Tier (curated library) | `data-block-id` |
|--------------|-------------------------|------------------------|-----------------|
| `hero.html` | `HERO` | battle-tested | `hero` |
| `social_proof.html` | `TRUST` | experimental (synthetic) | `social_proof` |
| `cases.html` | `CASES` | validated | `cases` |
| `pricing.html` | `PRICING` | validated | `pricing` |
| `lead_form.html` | `LEAD_FORM` | battle-tested | `lead_form` |
| `cta_band.html` | `CTA` | validated | `cta_band` |
| `faq.html` | `FAQ` | validated | `faq` |
| `contact_block.html` | `CONTACTS` | validated | `contact_block` |
| `sticky_cta.html` | `CTA` (sub-variant) | validated | *(module hook — no `data-block-id`)* |

**Unique `block_id` covered (8):** `HERO`, `TRUST`, `CASES`, `PRICING`, `LEAD_FORM`, `CTA`, `FAQ`, `CONTACTS`.

**Counting note:** Charter G0 target **9/32** uses **9 partial files** (aligned with [curated-library-index-v1.md](../projects/mars-website-factory/curated-library-index-v1.md) and [CORE-BLOCK-LIBRARY-v1.md](../workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md) — CTA counted once with two implementation variants). Strict `block_id` cardinality = **8/32**.

### Not in RPC numerator (repo fact)

| Class | Examples | Why excluded |
|-------|----------|--------------|
| Registry-only (T0) | `BENEFITS`, `PROCESS`, `SERVICES`, all catalog/commerce blocks | No T1+ partial |
| Structural Tier A | `HEADER_NAV`, `FILTERS`, `SEARCH` | No registry row; no sections partial |
| Layout ad-hoc | `header.html`, `footer.html`, `modal_callback.html` | Outside `sections/` RPC binding; not promoted `block_id` partials |
| v0 snake_case without v1 promotion | — | All 9 rows map via WF-R01.1 binding table |

### Missing for next RPC gates (preview)

| Gate | RPC target | Gap from baseline |
|------|------------|-------------------|
| **G1** | 14/32 (~44%) | **+5** partial-file equivalents (+5–6 `block_id`) |
| **G2** | 20/32 (~63%) | **+11** |
| **G3** | 29/32 (~91%) | **+20** |
| **G4** | 32/32 (100%) | **+23** (+ structural 3) |

---

## RSC

**Definition:** Share of required `page_type` scaffolds per active site-type expansion wave; stub-declared honesty required.

### Global denominator (PAGE-TYPE-REGISTRY-v1 minimum)

**10** canonical `page_type` codes: `HOME_PAGE`, `LANDING_PAGE`, `SERVICE_PAGE`, `CATEGORY_PAGE`, `PRODUCT_PAGE`, `ABOUT_PAGE`, `CONTACT_PAGE`, `FAQ_PAGE`, `REVIEWS_PAGE`, `LEGAL_PAGE`.

**ECOMMERCE extensions** (documented, not in minimum 10): `CART_PAGE`, `CHECKOUT_PAGE`, `ORDER_CONFIRMATION_PAGE` — **SAFE UNKNOWN** for baseline RSC denominator; not counted in 10.

### Existing scaffolds

| Scaffold | Path | Implied `page_type` | Stub-declared? |
|----------|------|---------------------|----------------|
| Golden slice landing | `src/pages/index.html` | `LANDING_PAGE` | **Partial** — functional stack; **no** formal scaffold manifest / stub policy doc |

**No other** `src/pages/*.html` scaffolds exist.

### Numerator / denominator

| Scope | Numerator | Denominator | % |
|-------|-----------|-------------|---|
| **Global (all minimum page types)** | **1** | **10** | **10%** |
| **G0 active wave (LANDING only)** | **1** | **1** (`LANDING_PAGE`) | **100%** |

### RSC by site-type primary `page_type` (planning view)

| site_type_code | Primary scaffold(s) required | Exists |
|----------------|------------------------------|--------|
| **LANDING** | `LANDING_PAGE` | **Yes** (`index.html`) |
| **PROMO** | `HOME_PAGE`, `SERVICE_PAGE`, `ABOUT_PAGE`, `CONTACT_PAGE` | **No** |
| **CATALOG** | `HOME_PAGE`, `CATEGORY_PAGE`, `PRODUCT_PAGE`, `SEARCH_RESULTS_PAGE`* | **No** |
| **ECOMMERCE** | CATALOG set + cart/checkout utility pages | **No** |
| **CORPORATE** | `HOME_PAGE`, `ABOUT_PAGE`, `CONTACT_PAGE` (+ route groups) | **No** |
| **MARKETPLACE** | Extended — deferred | **No** |

\*`SEARCH_RESULTS_PAGE` — routing note in program design; **not** in PAGE-TYPE-REGISTRY-v1 minimum 10 — **SAFE UNKNOWN** for formal RSC binding.

**RSC verdict:** LANDING golden slice satisfies **wave-local** scaffold; **global** scaffold coverage **~1/10**.

---

## SC

**Definition:** Share of `site_type_code` (and declared vertical profiles) meeting Template-Art minimum reference set — T1+ partials + published Reference Composition + primary scaffolds.

**Interim policy (binding until G2):** Passport must state **«TEMPLATE_ART — LANDING scope only»** for undeclared multi-type attempts.

### Summary table (task list)

| Type / profile | Registry status | SC verdict | Template-Art gate (coverage-derived) |
|----------------|-----------------|------------|-------------------------------------|
| **LANDING** | Core `site_type_code` | **Partial pass** — conversion path ~8/12 block classes; shell incomplete | **G0** HITL pilot **allowed** |
| **PROMO** | Core | **Fail** | **Blocked** until **G2** |
| **CORPORATE** | Core | **Fail** | **Blocked** until **G3** pilot |
| **CATALOG** | Core | **Fail** — no structural partials/scaffolds | **Blocked** until **G2** scaffold / **G3** broader |
| **ECOMMERCE** | Core | **Fail** — commerce chain registry-only | **Blocked** until **G3–G4** |
| **MANUFACTURER** | **Vertical profile** (not v1 `site_type_code`) | **Fail** — depends on CATALOG + CORPORATE slices; BZPM ad-hoc only | **Blocked** (via CATALOG **G2**) |
| **AUTO** | **Vertical profile** (not v1 `site_type_code`) | **Fail** — OCPilot SITE-001 binding **unverified** | **Blocked** (via CATALOG **G3**) |
| **MARKETPLACE** | Extended `site_type_code` | **Fail** — out of Core WF-R01.3 scope | **Deferred** |

**SC scorecard:**

| Metric | Value |
|--------|-------|
| Full SC pass | **0/8** |
| Partial (LANDING only) | **1/8** |
| Core 5 only (charter shorthand) | **0/5** full · **1/5** partial |

### LANDING checklist (partial pass detail)

| Requirement | Status |
|-------------|--------|
| `HERO` | **T1+** ✓ |
| `BENEFITS` | **Missing** |
| `CTA` / sticky module | **T1+** ✓ (`cta_band` + `sticky_cta`) |
| `LEAD_FORM` | **T1+** ✓ |
| `PRICING` (if offer) | **T1+** ✓ |
| `TRUST` / `TESTIMONIALS` | **Partial** — `TRUST` only (`social_proof`); no `TESTIMONIALS` partial |
| `CASES` | **T1+** ✓ |
| `FAQ` | **T1+** ✓ |
| `CONTACTS` | **T1+** ✓ |
| `MAP` | Missing (optional) |
| `FOOTER` | Layout ad-hoc only — **not** T1+ `FOOTER` partial |
| `LEGAL_LINKS` | **Missing** |
| `HEADER_NAV` minimal | Layout stub only — **not** structural partial / registry row |
| `LANDING_PAGE` Reference Composition (doc) | **Not published** |
| `LANDING_PAGE` scaffold | **Yes** (`index.html`) |

---

## PC

**Definition:** Share of in-scope `page_type` with published **Reference Composition** (documented one-page block stack — distinct from Blueprint).

### Planning assets that exist (not PC numerator)

| Artifact | Role | Counts as PC? |
|----------|------|---------------|
| [PAGE-BLOCK-MAPPING-v1.md](../workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md) | REQUIRED/OPTIONAL matrix | **No** — registry SSOT, not Reference Composition |
| [BLUEPRINT-BLOCK-MAPPING-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLUEPRINT-BLOCK-MAPPING-v1.md) | Blueprint stance matrix | **No** |
| [golden-implementation-slice-v1.md](../projects/mars-website-factory/golden-implementation-slice-v1.md) + `index.html` | De-facto stack implementation | **No** — implementation evidence, not published composition doc |

### Numerator / denominator

| Scope | Published Reference Compositions | In-scope `page_type` | PC |
|-------|----------------------------------|----------------------|-----|
| **G0 active wave (LANDING)** | **0** | **1** (`LANDING_PAGE`) | **0/1 (0%)** |
| **Full minimum registry (informational)** | **0** | **10** | **0/10 (0%)** |

**PC verdict:** **Orthogonal to RPC** — matrices and golden slice provide **planning + implementation hints**; formal Reference Composition publication **not started**. PC may reach 100% while RPC remains ~28%.

---

## Current Gate

### Gate evaluation (G0–G4)

| Gate | Name | RPC target | Met? | Evidence |
|------|------|------------|------|----------|
| **G0** | Baseline | **9/32** (~28%) | **Yes** | 9 partial files; build PASS; golden slice; charter T0 baseline |
| **G1** | LANDING + shell | **14/32** (~44%) | **No** | RPC **9/32** — deficit **5** |
| **G2** | PROMO + CATALOG scaffold | **20/32** (~63%) | **No** | No catalog structural partials; no PLP/PROMO scaffolds |
| **G3** | ECOMMERCE + CORPORATE slice | **29/32** (~91%) | **No** | Commerce blocks registry-only |
| **G4** | Full Core reference | **32/32** (100%) | **No** | Structural registry rows + remaining partials absent |

```text
Position:  G0  ──► G1 ──► G2 ──► G3 ──► G4
              ▲
           YOU ARE HERE
```

**Unlocks at G0:** LANDING Template-Art **HITL pilot only** — **not** production multi-type Template-Art.

**WF-A03 relationship:** G2 remains **recommended precondition** for Pixel Factory charter pass; G0 **does not** authorize WF-A03.

---

## Delta To Next Gate

**Target:** **G1** — LANDING + shell (**14/32** RPC ~44%).

### RPC (+5 partial-file equivalents minimum)

| Priority | `block_id` | Rationale (G1 deliverables) | Extraction feed |
|----------|------------|----------------------------|-----------------|
| 1 | `BENEFITS` | LANDING required; registry-only | Triumph W1 |
| 2 | `PROCESS` | LANDING required; registry-only | Triumph (`scroll_process_timeline` pattern) |
| 3 | `TESTIMONIALS` | Split from inline `TRUST` / social proof | Triumph W1 |
| 4 | `HEADER_NAV` | Shell + structural Tier A | Triumph W2 nav minimal; **requires** WF-R01.2 row |
| 5 | `FOOTER` and/or `LEGAL_LINKS` | Shell completeness | Layout promotion from ad-hoc → T1+ partial |

*Operator may sequence FOOTER + LEGAL_LINKS within the +5 budget per wave charter; conservative gate math allows **14** vs wave sum ~15.*

### Registry (WF-R01.2 Gate 2 — co-required for G1 catalog honesty)

| Missing row | Blocks honest claims on |
|-------------|-------------------------|
| `HEADER_NAV` | PROMO/CATALOG multi-page Template-Art |
| `FILTERS` | CATALOG PLP (G2 path) |
| `SEARCH` | CATALOG discovery (G2 path) |

**G1 minimum:** structural **registry rows** for Tier A terms — execution **not started**.

### RSC (G1)

| Missing | Notes |
|---------|-------|
| Formal **LANDING_PAGE** Reference Composition doc | PC numerator |
| Stub-declared honesty record for `index.html` | RSC policy compliance |

### SC (G1)

| Outcome | Requirement |
|---------|-------------|
| LANDING **production** Template-Art (vs G0 HITL pilot) | G1 SC checklist pass — shell blocks + composition doc |

### Execution case routing (no workspace changes in this snapshot)

| Case | Role toward G1 |
|------|----------------|
| **Triumph** | Primary W1/W2 extraction — BENEFITS, PROCESS, TESTIMONIALS, HEADER_NAV |
| **ISBD** | Adoption validation — **not** G1 driver |
| **BZPM** | Doc-first vocabulary — **not** RPC until Factory enrollment |
| **FP-0002** | QA discipline only — **must not** inflate RPC |

---

## Risks

| Risk | Severity | Baseline signal |
|------|----------|-----------------|
| False «Factory-ready» from **29/29 registry** | Critical | RC 90.6% vs RPC 28% — gap **62.6 pp** |
| Single-metric drift («9 partials» without denominator) | Medium | Always pair **9/32**; note **8/32** strict `block_id` |
| TEMPLATE_ART on CATALOG/PROMO before G2 | Critical | SC **0/7** non-LANDING types |
| Layout `header`/`footer` mistaken for HEADER_NAV/FOOTER RPC | Medium | `layout/` ≠ `sections/` T1+ binding |
| Stub scaffold counted as SC pass | Medium | `index.html` exists but no stub-declared RSC record |
| v0 snake_case in curated library vs v1 `block_id` truth | Medium | Curated index operational view only |
| BZPM / FP-0002 inflating reference canon | Medium | Ad-hoc delivery and PIXEL stress **≠** RPC |
| WF-A03 before G2 | Medium | G0 position — waiver discouraged |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| **FOUNDRY** as named product/path in repo | **Not found** — Website Factory ecosystem used |
| **WF-R01.3 program steward** | **Not fixed** in repo |
| **Strict vs file-based RPC** for gate math | Charter uses **9/32** file count; strict **8/32** documented here |
| **SEARCH_RESULTS_PAGE** formal `page_type` | Referenced in program design — **not** in PAGE-TYPE-REGISTRY-v1 minimum 10 |
| **RSC denominator including ECOMMERCE extensions** | 10 vs 13 — baseline uses **10**; extensions excluded pending operator count |
| **BREADCRUMBS / PAGINATION** RPC vs layout-component | WF-R01.2 policy — affects W4 numerator when executed |
| **BZPM Factory workspace enrollment** | **Pending** — vocabulary mining HITL only |
| **OCPilot SITE-001** Factory binding | **Not verified** — AUTO profile blocked |
| **WF-R01.7** ACCEPTED Template-Art matrix | **Pending** — interim coverage-derived matrix binding |
| **npm unavailable environments** | Build PASS verified locally; other environments **UNKNOWN** |

---

## Recommended Next Step

1. **Charter WF-R01.3.2** (LANDING completion wave) — authorized only after this baseline snapshot.
2. **Parallel:** WF-R01.2 **Gate 2** registry row execution (`HEADER_NAV`, `FILTERS`, `SEARCH`) — prerequisite for honest G1 shell + catalog path.
3. **Publish** first Reference Composition doc for `LANDING_PAGE` (PC numerator) as part of W1 — separate from registry matrices.
4. **Maintain** five-dimension reporting in every subsequent WF-R01.3 wave REPORT — never collapse to RC alone.

**STOP** — no implementation, no partial creation, no registry changes, no new IDs in this pass.

---

*Snapshot artifact: `reports/wf-r01-3-0-coverage-baseline-snapshot-v1.md`*
