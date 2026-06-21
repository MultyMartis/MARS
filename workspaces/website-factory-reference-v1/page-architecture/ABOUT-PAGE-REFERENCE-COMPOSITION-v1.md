# ABOUT_PAGE Reference Composition v1

**Site type:** PROMO (primary)  
**Reference workspace:** `workspaces/website-factory-reference-v1/`  
**Composition version:** v1  
**Status:** PUBLISHED  
**Page type:** `ABOUT_PAGE`  
**Scaffold:** `src/pages/about-page-reference.html`  
**Authority:** [wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md](../../projects/mars-website-factory/wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md) · [reference-scaffold-contract-v1.md](../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [page-type-shell-matrix-v1.md](../../projects/mars-website-factory/page-type-shell-matrix-v1.md)

**Honesty boundary:** Reference composition documentation only. **Not** production acceptance. **Not** corporate history runtime. **Not** real company data.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED** |
| **Publication wave** | WF-R01.3 G2-R2 P3 — ABOUT_PAGE Scaffold |
| **Build evidence** | `dist/about-page-reference.html` — build PASS (G2-R2 P3) |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **page_type** | `ABOUT_PAGE` |
| **Canonical name** | About / company trust page |
| **Typical use** | `/about/`, `/company/` |
| **Registry source** | [PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md) § ABOUT_PAGE |

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
| Scaffold Manifest | [ABOUT-PAGE-SCAFFOLD-MANIFEST-v1.md](ABOUT-PAGE-SCAFFOLD-MANIFEST-v1.md) | Build validation |

---

## 4. Purpose

Document the reference composition for a minimal `ABOUT_PAGE` scaffold: scaffold-owned page identity, organisation narrative via canonical `ABOUT`, people presentation via canonical `TEAM`, and supporting trust signals via canonical `TRUST`. Supports PROMO money-page corridor structure without claiming production readiness, company history runtime, or real-person data.

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
| MAIN | REQ | `<main id="main" class="wf-about-page">` |
| BREADCRUMBS | REQ | **Included** — shallow fictional trail |
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
├── ABOUT
├── TEAM
└── TRUST

FOOTER
└── LEGAL_LINKS
```

Ordered MAIN includes:

1. `components/breadcrumbs.html` — shallow variant (`Home` → `About`)
2. PAGE_IDENTITY (scaffold-owned)
3. `components/about.html` — block_id `ABOUT`
4. `components/team.html` — block_id `TEAM`
5. `sections/trust.html` — block_id `TRUST`

**Layout:** Option A — sequential canonical sections. Canonical partials retain self-contained section containers.

---

## 7. Scaffold-Owned Regions

| Region | Class root | `data-block-id` | Content |
|--------|------------|-----------------|---------|
| PAGE_IDENTITY | `wf-about-page__identity` | **None** | Eyebrow · one H1 · neutral lead |
| Main inner wrapper | `wf-about-page__inner` | **None** | Container + section rhythm |

**No new block IDs.** PAGE_IDENTITY is page introduction only — not a Registry block.

---

## 8. Required Blocks

| block_id | Partial | Role |
|----------|---------|------|
| HEADER_NAV | `layout/header.html` → `sections/header-nav.html` | Global shell |
| ABOUT | `components/about.html` | Organisation narrative owner |
| BREADCRUMBS | `components/breadcrumbs.html` | Orientation trail |
| FOOTER | `sections/footer.html` | Global shell |
| LEGAL_LINKS | `components/legal-links.html` (nested) | Legal navigation |

---

## 9. Recommended Blocks

| block_id | Stance | Manifest decision |
|----------|--------|---------------------|
| TEAM | OPTIONAL | **Included** — people and roles |
| TRUST | OPTIONAL | **Included** — supporting proof signals |

---

## 10. Optional Blocks

| block_id | Stance | Manifest decision |
|----------|--------|---------------------|
| SEARCH | OPTIONAL | **Excluded** — N/A on shell matrix |
| CTA | OPTIONAL | **Excluded** — avoid landing-style aggressiveness |
| HERO | REQUIRED (mapping) | **Excluded** — PAGE_IDENTITY substitute per C5/C6 compact policy |
| CERTIFICATES · CASES · PARTNERS | OPTIONAL | **Excluded** — no partial requirement for honest v1 reference |

---

## 11. Excluded Blocks

| Category | Members |
|----------|---------|
| Process / conversion | PROCESS · CTA · LEAD_FORM · BENEFITS · SERVICES |
| Contact / geo | CONTACTS · MAP · FAQ |
| Catalog / commerce | SEARCH · FILTERS · PAGINATION · PRODUCT_GRID · CART · CHECKOUT |
| Scaffold policy | New PAGE_IDENTITY block_id · COMPANY_STORY · MISSION · HISTORY · VALUES blocks |

---

## 12. ABOUT Role

| Field | Value |
|-------|-------|
| **block_id** | `ABOUT` |
| **Partial** | `src/partials/components/about.html` |
| **Hook** | `data-block-id="about"` |
| **Role** | Primary organisation narrative owner — who the organisation is |
| **Heading** | Canonical H2 — does not compete with page H1 |
| **Modification** | **None** — canonical partial reused as-is |

---

## 13. TEAM Role

| Field | Value |
|-------|-------|
| **block_id** | `TEAM` |
| **Partial** | `src/partials/components/team.html` |
| **Hook** | `data-block-id="team"` |
| **Role** | People and roles — who works in the organisation |
| **Placement** | After ABOUT — does not dominate page meaning |
| **Modification** | **None** — canonical partial reused as-is |

---

## 14. TRUST Role

| Field | Value |
|-------|-------|
| **block_id** | `TRUST` |
| **Partial** | `src/partials/sections/trust.html` |
| **Hook** | `data-block-id="trust"` |
| **Role** | Supporting reassurance / proof — not primary page meaning |
| **Content** | Fictional reference metrics · generic logo placeholders · demo badges |
| **Modification** | **None** — canonical partial reused as-is |

---

## 15. PROCESS Exclusion

| Field | Value |
|-------|-------|
| **Mapping stance** | PROCESS **FORBIDDEN** on ABOUT_PAGE |
| **Charter note** | Charter listed PROCESS as optional — **mapping wins** |
| **Manifest decision** | **Excluded** — not included in scaffold |
| **Rationale** | PROCESS belongs on SERVICE_PAGE corridor; ABOUT narrative flow is identity → people → trust |

---

## 16. Fictional Content Policy

| Field | Value |
|-------|-------|
| **PAGE_IDENTITY** | Neutral scaffold copy — no real company name |
| **ABOUT partial** | Fictional organisation narrative — non-numeric reference copy |
| **TEAM partial** | Fictional personas — decorative portraits `aria-hidden` |
| **TRUST partial** | Reference metrics and generic logo text — not real client claims |
| **Production data** | **Forbidden** on reference scaffold |

---

## 17. Runtime Boundary

| Capability | State |
|------------|-------|
| New page-specific JS | **None** |
| Backend / network | **None** |
| Modal / profile runtime on TEAM | **None** |
| Analytics | **None** |

**JavaScript reused:** `lifecycle.js` · `header_nav.js` · `main.js`

---

## 18. Accessibility

| Check | State |
|-------|-------|
| One H1 | `about-page-title` in PAGE_IDENTITY |
| Identity region | `aria-labelledby="about-page-title"` |
| Breadcrumbs | `<nav aria-label="Breadcrumb">` · `aria-current="page"` on current item |
| Heading hierarchy | H1 (identity) → H2 (ABOUT · TEAM · TRUST) → H3 (team names) |
| ABOUT narrative | Full text accessible — not image-only |
| TEAM content | Names and roles as text — portraits decorative |
| TRUST content | Metrics and badges as text — logo text `aria-hidden` where decorative |
| Duplicate IDs | **None** — single instance per block |

**WCAG certification:** **Not claimed**

---

## 19. Responsive Notes

| Breakpoint behaviour | Policy |
|---------------------|--------|
| PAGE_IDENTITY | Long title wraps via `overflow-wrap` |
| ABOUT | Canonical partial owns internal two-column layout |
| TEAM | Canonical partial owns member grid |
| TRUST | Canonical partial owns metrics/logos/badges layout |
| Section rhythm | Page SCSS controls outer spacing only |
| Horizontal overflow | **None** expected — page inner uses `wf-container` |

---

## 20. Coverage Role

| Metric | Effect |
|--------|--------|
| **RSC** | **+1** when full scaffold chain validated (G2-R2 P3) |
| **RPC** | **None** — no new partials |
| **PC** | **None** — ABOUT_PAGE composition alone does **not** accrue PROMO PC |
| **PROMO SC** | **Not evaluated** by this artefact |

---

## 21. Evidence Paths

| Artefact | Path |
|----------|------|
| Source scaffold | `workspaces/website-factory-reference-v1/src/pages/about-page-reference.html` |
| Dist output | `workspaces/website-factory-reference-v1/dist/about-page-reference.html` |
| Page SCSS | `workspaces/website-factory-reference-v1/src/scss/pages/_about-page-reference.scss` |
| Manifest | `workspaces/website-factory-reference-v1/page-architecture/ABOUT-PAGE-SCAFFOLD-MANIFEST-v1.md` |
| P3 report | `reports/wf-r01-3-g2-r2-p3-about-page-scaffold-v1.md` |

---

## 22. Decision

**ABOUT_PAGE reference composition v1 — PUBLISHED.**

Approved sequence locked for G2-R2 P3. Feeds PROMO corridor documentation; RSC accrues on scaffold completion only. **Not** PROMO PC evidence. **Not** PROMO SC PASS.
