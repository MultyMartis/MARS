# CONTACT_PAGE Reference Composition v1

**Site type:** PROMO (primary)  
**Reference workspace:** `workspaces/website-factory-reference-v1/`  
**Composition version:** v1  
**Status:** PUBLISHED  
**Page type:** `CONTACT_PAGE`  
**Scaffold:** `src/pages/contact-page-reference.html`  
**Authority:** [wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md](../../projects/mars-website-factory/wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md) · [reference-scaffold-contract-v1.md](../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [page-type-shell-matrix-v1.md](../../projects/mars-website-factory/page-type-shell-matrix-v1.md)

**Honesty boundary:** Reference composition documentation only. **Not** production acceptance. **Not** working communication channels. **Not** form delivery or CRM integration.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED** |
| **Publication wave** | WF-R01.3 G2-R2 P2 — CONTACT_PAGE Scaffold |
| **Build evidence** | `dist/contact-page-reference.html` — build PASS (G2-R2 P2) |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **page_type** | `CONTACT_PAGE` |
| **Canonical name** | Contact hub |
| **Typical use** | `/contacts/`, `/contact/` |
| **Registry source** | [PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md) § CONTACT_PAGE |

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
| Scaffold Manifest | [CONTACT-PAGE-SCAFFOLD-MANIFEST-v1.md](CONTACT-PAGE-SCAFFOLD-MANIFEST-v1.md) | Build validation |

---

## 4. Purpose

Document the reference composition for a minimal `CONTACT_PAGE` scaffold: page identity, fictional NAP presentation via canonical `CONTACTS`, and presentation-only lead form. Supports PROMO money-page corridor structure without claiming production readiness, map integration, or form delivery.

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
| MAIN | REQ | `<main id="main" class="wf-contact-page">` |
| BREADCRUMBS | POL | **Included** — shallow fictional trail |
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
├── CONTACTS
└── LEAD_FORM

FOOTER
└── LEGAL_LINKS
```

Ordered MAIN includes:

1. `components/breadcrumbs.html`
2. PAGE_IDENTITY (scaffold-owned)
3. `sections/contact_block.html` — block_id `CONTACTS`
4. `sections/lead_form.html` — block_id `LEAD_FORM`

**Layout:** Option A — sequential sections. Canonical partials retain self-contained section containers.

---

## 7. Scaffold-Owned Regions

| Region | Class root | `data-block-id` | Content |
|--------|------------|-----------------|---------|
| PAGE_IDENTITY | `wf-contact-page__identity` | **None** | Eyebrow · one H1 · neutral lead |
| Main inner wrapper | `wf-contact-page__inner` | **None** | Container + section rhythm |

**CONTACT CONTEXT wrapper:** **Not used** — CONTACTS partial owns contact copy.

---

## 8. Required Blocks

| block_id | Partial | Role |
|----------|---------|------|
| HEADER_NAV | `layout/header.html` → `sections/header-nav.html` | Global shell |
| CONTACTS | `sections/contact_block.html` | Fictional NAP hub |
| FOOTER | `sections/footer.html` | Global shell |
| LEGAL_LINKS | `components/legal-links.html` (nested) | Legal navigation |

---

## 9. Optional Blocks

| block_id | Stance | Manifest decision |
|----------|--------|---------------------|
| BREADCRUMBS | POL | **Included** |
| LEAD_FORM | OPTIONAL | **Included** — presentation-only |
| HERO | OPTIONAL | **Excluded** — PAGE_IDENTITY substitute |
| MAP | OPTIONAL | **Excluded** — no embed/API |
| TRUST | — | **Excluded** |
| FAQ | — | **Excluded** |
| CTA | — | **Excluded** |

---

## 10. Excluded Blocks

| Category | Members |
|----------|---------|
| Map / geo | MAP block · iframe embed · map API |
| Conversion duplicates | CTA · TRUST · FAQ |
| About / team | ABOUT · TEAM · PROCESS · BENEFITS · SERVICES |
| Catalog / commerce | SEARCH · FILTERS · PAGINATION · PRODUCT_GRID · CART · CHECKOUT |
| Scaffold policy | CONTACT CONTEXT wrapper · new PAGE_IDENTITY block_id |

---

## 11. CONTACTS Role

| Field | Value |
|-------|-------|
| **block_id** | `CONTACTS` |
| **Partial** | `src/partials/sections/contact_block.html` |
| **Hook** | `data-block-id="contact_block"` |
| **Role** | Fictional NAP presentation — phone, email, hours |
| **Map link** | External placeholder link in partial — **not** MAP block; no embed; no auto-load |
| **Modification** | **None** — canonical partial reused as-is |

---

## 12. LEAD_FORM Role

| Field | Value |
|-------|-------|
| **block_id** | `LEAD_FORM` |
| **Partial** | `src/partials/sections/lead_form.html` |
| **Hook** | `data-block-id="lead_form"` · `#lead-form` |
| **Count** | **One** per page |
| **Runtime** | `mockSubmit` when no endpoint — no network request |
| **Modification** | **None** — canonical partial reused as-is |

---

## 13. Fictional Content Policy

| Field | Value |
|-------|-------|
| **PAGE_IDENTITY** | Neutral scaffold copy — no real company name |
| **CONTACTS partial** | Demo tel `+1 (555) 123-4567` · `hello@example.com` · demo hours |
| **Map link** | Generic `https://maps.google.com/` placeholder — no real client location |
| **Production data** | **Forbidden** on reference scaffold |

---

## 14. Runtime Boundary

| Capability | State |
|------------|-------|
| Form backend / CRM | **None** |
| Map embed / API | **None** |
| Network on form submit | **None** — mock only |
| New page-specific JS | **None** |
| Analytics | **None** |

---

## 15. Accessibility

| Check | State |
|-------|-------|
| One H1 | `contact-page-title` in PAGE_IDENTITY |
| Identity region | `aria-labelledby="contact-page-title"` |
| Breadcrumbs | `<nav aria-label="Breadcrumb">` · `aria-current="page"` on current item |
| Contact channels | Text links for phone and email — not icon-only |
| Form labels | `for`/`id` pairs on `#lead-name` · `#lead-phone` |
| Form errors | `role="alert"` on field errors |
| Duplicate IDs | **None** — single LEAD_FORM instance |

---

## 16. Responsive Notes

| Breakpoint behaviour | Policy |
|---------------------|--------|
| PAGE_IDENTITY | Long title wraps via `overflow-wrap` |
| CONTACTS | Canonical partial owns internal two-column grid at `md+` |
| LEAD_FORM | Page-level max-width constraint; stacks below identity |
| Horizontal overflow | **None** expected — page inner uses `wf-container` |

---

## 17. Coverage Role

| Metric | Effect |
|--------|--------|
| **RSC** | **+1** when full scaffold chain validated (G2-R2 P2) |
| **RPC** | **None** — no new partials |
| **PC** | **None** — CONTACT_PAGE composition is **not** PROMO corridor accrual by itself |
| **PROMO SC** | **Not evaluated** by this artefact |

---

## 18. Evidence Paths

| Artefact | Path |
|----------|------|
| Source scaffold | `workspaces/website-factory-reference-v1/src/pages/contact-page-reference.html` |
| Dist output | `workspaces/website-factory-reference-v1/dist/contact-page-reference.html` |
| Page SCSS | `workspaces/website-factory-reference-v1/src/scss/pages/_contact-page-reference.scss` |
| Manifest | `workspaces/website-factory-reference-v1/page-architecture/CONTACT-PAGE-SCAFFOLD-MANIFEST-v1.md` |
| P2 report | `reports/wf-r01-3-g2-r2-p2-contact-page-scaffold-v1.md` |

---

## 19. Decision

**CONTACT_PAGE reference composition v1 — PUBLISHED.**

Approved sequence locked for G2-R2 P2. Feeds PROMO corridor documentation; RSC accrues on scaffold completion only. **Not** PROMO PC evidence. **Not** PROMO SC PASS.
