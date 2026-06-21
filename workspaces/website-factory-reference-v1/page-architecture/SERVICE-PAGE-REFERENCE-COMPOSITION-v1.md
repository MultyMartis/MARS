# SERVICE_PAGE Reference Composition v1

**Site type:** PROMO (primary)  
**Reference workspace:** `workspaces/website-factory-reference-v1/`  
**Composition version:** v1  
**Status:** PUBLISHED  
**Page type:** `SERVICE_PAGE`  
**Scaffold:** `src/pages/service-page-reference.html`  
**Authority:** [wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md](../../projects/mars-website-factory/wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md) · [reference-scaffold-contract-v1.md](../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [page-type-shell-matrix-v1.md](../../projects/mars-website-factory/page-type-shell-matrix-v1.md)

**Honesty boundary:** Reference composition documentation only. **Not** production acceptance. **Not** real service runtime. **Not** real company or commercial claims.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED** |
| **Publication wave** | WF-R01.3 G2-R2 P4 — SERVICE_PAGE Scaffold |
| **Build evidence** | `dist/service-page-reference.html` — build PASS (G2-R2 P4) |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **page_type** | `SERVICE_PAGE` |
| **Canonical name** | Service detail / money page |
| **Typical use** | `/services/{slug}/` |
| **Registry source** | [PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md) § SERVICE_PAGE |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| G2-R2 P1 preflight | `projects/mars-website-factory/wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md` | Composition approval |
| G2-R2 charter | `projects/mars-website-factory/wf-r01-3-g2-r2-promo-money-page-scaffold-completion-charter-v1.md` | PROMO corridor package |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Shell order |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | REQ/POL surfaces |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | RSC boundary |
| Page-Block Mapping | `workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md` | Block stances |
| Scaffold Manifest | [SERVICE-PAGE-SCAFFOLD-MANIFEST-v1.md](SERVICE-PAGE-SCAFFOLD-MANIFEST-v1.md) | Build validation |

---

## 4. Purpose

Document the reference composition for a minimal `SERVICE_PAGE` scaffold: scaffold-owned page identity, scaffold-owned service detail context for one service, and reusable canonical blocks for advantages, workflow, objections, commercial action, and lead capture. Supports PROMO money-page corridor structure without claiming production readiness, real service data, or pricing runtime.

---

## 5. Shell

```text
HEADER_NAV
MAIN
FOOTER
└── LEGAL_LINKS
```

| Surface | Matrix | Manifest |
|---------|--------|----------|
| HEADER_NAV | REQ | Present |
| MAIN | REQ | `<main id="main" class="wf-service-page">` |
| BREADCRUMBS | POL — included | Present — shallow fictional trail |
| FOOTER | REQ | Present |
| LEGAL_LINKS | REQ | Nested in FOOTER |
| SEARCH | N/A | **Absent** |
| FILTERS | N/A | **Absent** |
| PAGINATION | N/A | **Absent** |

---

## 6. Block Sequence

```text
HEADER_NAV

MAIN
├── BREADCRUMBS
├── scaffold-owned PAGE_IDENTITY
├── scaffold-owned SERVICE_DETAIL_CONTEXT
├── BENEFITS
├── PROCESS
├── FAQ
├── CTA
└── LEAD_FORM

FOOTER
└── LEGAL_LINKS
```

Ordered MAIN includes:

1. `components/breadcrumbs.html` — shallow variant (`Home` → `Service`)
2. PAGE_IDENTITY (scaffold-owned)
3. SERVICE_DETAIL_CONTEXT (scaffold-owned)
4. `sections/benefits.html` — block_id `BENEFITS`
5. `sections/process.html` — block_id `PROCESS`
6. `sections/faq.html` — block_id `FAQ`
7. `sections/cta_band.html` — block_id `CTA`
8. `sections/lead_form.html` — block_id `LEAD_FORM`

**Layout:** Sequential canonical sections after scaffold-owned regions. Canonical partials retain self-contained section containers.

---

## 7. Scaffold-Owned Regions

| Region | Class root | `data-block-id` | Content |
|--------|------------|-----------------|---------|
| PAGE_IDENTITY | `wf-service-page__identity` | **None** | Eyebrow · one H1 · neutral lead |
| SERVICE_DETAIL_CONTEXT | `wf-service-page__detail` | **None** | Scope narrative · supporting list |
| Main inner wrapper | `wf-service-page__inner` | **None** | Container + section rhythm |

**No new block IDs.** PAGE_IDENTITY is page introduction only. SERVICE_DETAIL_CONTEXT is in-page scope explanation only — not a Registry block.

---

## 8. Required Blocks

| block_id | Partial | Role |
|----------|---------|------|
| HEADER_NAV | `layout/header.html` → `sections/header-nav.html` | Global shell |
| BENEFITS | `sections/benefits.html` | Advantages owner |
| PROCESS | `sections/process.html` | Workflow owner |
| FAQ | `sections/faq.html` | Objections owner |
| CTA | `sections/cta_band.html` | Commercial action owner |
| LEAD_FORM | `sections/lead_form.html` | Lead capture owner |
| BREADCRUMBS | `components/breadcrumbs.html` | Orientation trail |
| FOOTER | `sections/footer.html` | Global shell |
| LEGAL_LINKS | `components/legal-links.html` (nested) | Legal navigation |

---

## 9. Optional Blocks

| block_id | Stance | Manifest decision |
|----------|--------|---------------------|
| TRUST | OPTIONAL | **Excluded** — not required for honest v1 reference |
| CASES | OPTIONAL | **Excluded** |
| HERO | REQUIRED (mapping) | **Excluded** — PAGE_IDENTITY substitute per compact policy |
| SEARCH | OPTIONAL | **Excluded** — N/A on shell matrix |
| FEATURES | REQUIRED (OR with BENEFITS) | **Excluded** — BENEFITS satisfies OR-group |

---

## 10. Excluded Blocks

| Category | Members |
|----------|---------|
| Service collection | **SERVICES** |
| Organisation / contact | ABOUT · TEAM · TRUST · CONTACTS · MAP |
| Catalog / commerce | SEARCH · FILTERS · PAGINATION · PRODUCT_GRID · CART · CHECKOUT · PRICING |
| Scaffold policy | SERVICE_DESCRIPTION · SERVICE_CONTENT · SERVICE_DETAIL · SERVICE_FEATURES · SERVICE_CARD block IDs |

---

## 11. PAGE_IDENTITY Role

| Field | Value |
|-------|-------|
| **Region** | Scaffold-owned — not a Registry block |
| **Class root** | `wf-service-page__identity` |
| **Hook** | **None** — no `data-block-id` |
| **Role** | Page-level introduction — identifies the service page |
| **Heading** | One H1 — does not duplicate SERVICE_DETAIL_CONTEXT |
| **Content** | Neutral fictional scaffold copy — no real service name · no price · no CTA button |

---

## 12. SERVICE_DETAIL_CONTEXT Role

| Field | Value |
|-------|-------|
| **Region** | Scaffold-owned — inline in source page only |
| **Class root** | `wf-service-page__detail` |
| **Hook** | **None** — no `data-block-id` · no separate partial |
| **Role** | Scope explanation for the current single service |
| **Heading** | H2 scope title · H3 supporting subheading |
| **Allowed** | Neutral overview paragraphs · simple non-commercial list |
| **Forbidden** | Benefit cards · workflow steps · FAQ · pricing · related services · lead form · commercial CTA |

**Ownership boundary:**

| Concern | Owner |
|---------|-------|
| Advantages | BENEFITS |
| Workflow | PROCESS |
| Questions | FAQ |
| Commercial action | CTA |
| Lead capture | LEAD_FORM |
| Service collection | SERVICES (excluded) |

---

## 13. BENEFITS Role

| Field | Value |
|-------|-------|
| **block_id** | `BENEFITS` |
| **Partial** | `src/partials/sections/benefits.html` |
| **Hook** | `data-block-id="benefits"` |
| **Role** | Outcome-oriented advantages — does not duplicate SERVICE_DETAIL_CONTEXT |
| **Modification** | **None** — canonical partial reused as-is |

---

## 14. PROCESS Role

| Field | Value |
|-------|-------|
| **block_id** | `PROCESS` |
| **Partial** | `src/partials/sections/process.html` |
| **Hook** | `data-block-id="process"` |
| **Role** | Ordered workflow steps — does not duplicate detail context |
| **Modification** | **None** — canonical partial reused as-is |

---

## 15. FAQ Role

| Field | Value |
|-------|-------|
| **block_id** | `FAQ` |
| **Partial** | `src/partials/sections/faq.html` |
| **Hook** | `data-block-id="faq"` |
| **Role** | Service objections — native `<details>` presentation |
| **Instance count** | **One** per page |
| **Modification** | **None** — canonical partial reused as-is |

---

## 16. CTA Role

| Field | Value |
|-------|-------|
| **block_id** | `CTA` (cta_band) |
| **Partial** | `src/partials/sections/cta_band.html` |
| **Hook** | `data-block-id="cta_band"` |
| **Role** | Commercial action band — distinct from LEAD_FORM heading |
| **URLs / endpoints** | Demo only — `#lead-form` secondary · modal callback primary |
| **Modification** | **None** — canonical partial reused as-is |

---

## 17. LEAD_FORM Role

| Field | Value |
|-------|-------|
| **block_id** | `LEAD_FORM` |
| **Partial** | `src/partials/sections/lead_form.html` |
| **Hook** | `data-block-id="lead_form"` |
| **Role** | Primary lead capture — mockSubmit when endpoint absent |
| **Form count** | **One** — `#lead-form` |
| **Modification** | **None** — canonical partial reused as-is |

---

## 18. SERVICES Exclusion

| Field | Value |
|-------|-------|
| **block_id** | `SERVICES` |
| **Hook count on scaffold** | **0** |
| **Rationale** | First SERVICE_PAGE scaffold demonstrates one-service focus and avoids collection/detail ownership conflict |
| **Future variation** | Multi-service cross-links — out of P4 scope |

---

## 19. Fictional Content Policy

| Field | Value |
|-------|-------|
| **PAGE_IDENTITY** | Neutral scaffold copy — no real service name |
| **SERVICE_DETAIL_CONTEXT** | Fictional scope narrative — no commercial claims |
| **BENEFITS partial** | Neutral placeholder outcome props |
| **PROCESS partial** | Neutral placeholder workflow steps |
| **FAQ partial** | Neutral placeholder Q&A |
| **CTA partial** | Demo action labels — no production URL |
| **LEAD_FORM partial** | Demo form — no PII leaves browser |
| **Production data** | **Forbidden** on reference scaffold |

---

## 20. Runtime Boundary

| Capability | State |
|------------|-------|
| New page-specific JS | **None** |
| Backend / network | **None** on form submit (mockSubmit) |
| Analytics | **None** |

**JavaScript reused:** `lifecycle.js` · `modal.js` · `form.js` · `header_nav.js` · `main.js`

---

## 21. Accessibility

| Check | State |
|-------|-------|
| One H1 | `service-page-title` in PAGE_IDENTITY |
| Identity region | `aria-labelledby="service-page-title"` |
| Detail region | `aria-labelledby="service-detail-title"` |
| Breadcrumbs | `<nav aria-label="Breadcrumb">` · `aria-current="page"` on current item |
| Heading hierarchy | H1 (identity) → H2 (detail · blocks) → H3 (detail support · block items) |
| FAQ | Native `<details>` / `<summary>` controls |
| Form | Labels associated · error regions present |
| Duplicate IDs | **None** — single instance per block |

**WCAG certification:** **Not claimed**

---

## 22. Responsive Notes

| Breakpoint behaviour | Policy |
|---------------------|--------|
| PAGE_IDENTITY | Long title wraps via `overflow-wrap` |
| SERVICE_DETAIL_CONTEXT | Desktop two-column grid · tablet/mobile stack · `min-width: 0` |
| BENEFITS · PROCESS · FAQ | Canonical partials own internal layout |
| LEAD_FORM | Page SCSS constrains max-width only |
| Section rhythm | Page SCSS controls outer spacing only |
| Horizontal overflow | **None** expected — page inner uses `wf-container` |

---

## 23. Coverage Role

| Metric | Effect |
|--------|--------|
| **RSC** | **+1** when full scaffold chain validated (G2-R2 P4) |
| **RPC** | **None** — no new partials |
| **PC** | **None** — SERVICE_PAGE composition alone does **not** accrue PROMO PC |
| **PROMO SC** | **Not evaluated** by this artefact |

---

## 24. Evidence Paths

| Artefact | Path |
|----------|------|
| Source scaffold | `workspaces/website-factory-reference-v1/src/pages/service-page-reference.html` |
| Dist output | `workspaces/website-factory-reference-v1/dist/service-page-reference.html` |
| Page SCSS | `workspaces/website-factory-reference-v1/src/scss/pages/_service-page-reference.scss` |
| Manifest | `workspaces/website-factory-reference-v1/page-architecture/SERVICE-PAGE-SCAFFOLD-MANIFEST-v1.md` |
| P4 report | `reports/wf-r01-3-g2-r2-p4-service-page-scaffold-v1.md` |

---

## 25. Decision

**SERVICE_PAGE reference composition v1 — PUBLISHED.**

Approved sequence locked for G2-R2 P4. Feeds PROMO corridor documentation; RSC accrues on scaffold completion only. **Not** PROMO PC evidence. **Not** PROMO SC PASS.
