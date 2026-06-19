# WF-R01.3.3 → WF-R01.3.4 Handoff Package v1

**Date:** 2026-06-19  
**From:** WF-R01.3.3 — Structural & Shell References (**COMPLETE**)  
**To:** WF-R01.3.4 — Catalog & Vertical Profile References (**DESIGN** — charter **not** published)  
**Closure evidence:** [wf-r01-3-3-exit-and-wf-r01-3-4-handoff-v1.md](wf-r01-3-3-exit-and-wf-r01-3-4-handoff-v1.md)

**Honesty boundary:** Handoff transfers **normative authority and metrics baseline** only. **Does not** authorize WF-R01.3.4 implementation, G2 activation, or coverage accrual without a separate charter pass.

---

## 1. Authority transferred

| Artefact | Path | Status |
|----------|------|--------|
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | **ACCEPTED / PUBLISHED** (Wave S1) |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | **ACCEPTED / PUBLISHED** (Wave S4) |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | **ACCEPTED / PUBLISHED** (Wave S4) |
| Navigation depth policy | `projects/mars-website-factory/global-shell-contract-v1.md` § Navigation depth · charter §8 | **Normative** |
| BREADCRUMBS reference partial | `workspaces/website-factory-reference-v1/src/partials/components/breadcrumbs.html` | **BUILT** (Wave S2) |
| BREADCRUMBS SCSS | `workspaces/website-factory-reference-v1/src/scss/components/_breadcrumbs.scss` | **BUILT** |
| PAGINATION reference partial | `workspaces/website-factory-reference-v1/src/partials/components/pagination.html` | **BUILT** (Wave S3) |
| PAGINATION SCSS | `workspaces/website-factory-reference-v1/src/scss/components/_pagination.scss` | **BUILT** |
| Tier B RPC accounting precedent | `reports/wf-r01-3-3-wave-s2-breadcrumbs-v1.md` · `reports/wf-r01-3-3-wave-s3-pagination-v1.md` | **Documented Path B** |
| Inherited W2 shell partials | HEADER_NAV · FOOTER · LEGAL_LINKS — WF-R01.3.2 | **COMPLETE — do not repeat** |

**Bounded hosts (diagnostic only — not scaffolds, not RSC):**

- `workspaces/website-factory-reference-v1/src/pages/breadcrumbs-reference.html`
- `workspaces/website-factory-reference-v1/src/pages/pagination-reference.html`

---

## 2. Starting metrics (post–WF-R01.3.3)

| Dimension | Value |
|-----------|-------|
| **RC** | **32/32** |
| **RPC** | **17/32** |
| **RSC** | **1/10** global · **1/1** LANDING |
| **SC** | **LANDING PASS** |
| **PC** | **1/1** LANDING |

**WF-R01.3.3 delta summary:** RPC **+2** (Tier B BREADCRUMBS + PAGINATION partial-equivalents). RC, RSC, SC, PC **unchanged**.

---

## 3. Expected WF-R01.3.4 scope (program design only)

Source: [wf-r01-3-reference-expansion-program-design-v1.md](wf-r01-3-reference-expansion-program-design-v1.md) § WF-R01.3.4 · wave map W4–W5.

| Item | Notes |
|------|-------|
| **FILTERS** T1+ partial | Tier A `block_id`; WF-R01.3.3 **excluded** |
| **SEARCH** T1+ partial | Tier A `block_id`; WF-R01.3.3 **excluded** |
| Catalog grids | CATEGORIES · CATEGORY_GRID · PRODUCT_GRID · PRODUCT_CARD (W5) |
| **CATEGORY_PAGE** / **PRODUCT_PAGE** reference needs | PLP/PDP scaffolds; shell matrix slots already defined |
| Catalog or vertical profile scaffolds | RSC expansion per `reference-scaffold-contract-v1.md` |
| Catalog compositions | PC for CATALOG corridor when wave charters authorize |
| Vertical profile docs | MANUFACTURER/AUTO profiles — **no new `site_type_code`** per design |
| BZPM / execution-case crosswalk | Evidence mining per program design |

**Already delivered under WF-R01.3.3 (do not re-implement in 3.4 opening waves):**

- BREADCRUMBS T1+ reference partial
- PAGINATION T1+ reference partial
- Global shell contract · shell matrix · scaffold contract

Program design wave W4 lists BREADCRUMBS/PAGINATION under R01.3.4 for **catalog corridor integration** — charter pass must reconcile **completed 3.3 partials** vs **PLP/PDP scaffold slot integration** without double RPC accrual.

---

## 4. Explicit exclusions

- LANDING rework or Reference Composition changes
- W2 reimplementation (HEADER_NAV · FOOTER · LEGAL_LINKS)
- New vocabulary families or Vocabulary Canon amendments
- New `block_id` rows without separate waiver charter
- WF-A03 Pixel Factory
- Production CMS integration or client-site deployment
- G2 closure or **G2 ACTIVE** claims
- WF-R01.3.5 execution
- Registry row edits as part of handoff

---

## 5. Known gaps

| Gap | Detail |
|-----|--------|
| **G2 RPC floor** | Target **≥ 20/32**; current **17/32** — gap **−3** |
| **FILTERS** | No T1+ partial |
| **SEARCH** | No T1+ partial |
| **CATEGORY_PAGE / PRODUCT_PAGE scaffolds** | Absent — RSC remains **1/10** |
| **CATALOG SC / PC** | Not declared |
| **G2** | **Not active** — separate accepted wave charters required |
| **WF-R01.3.4 charter** | **Absent** — charter pass required before execution |

---

## 6. Required first pass

```text
WF-R01.3.4 — Catalog & Vertical Profile References Charter Pass
```

**Do not** begin implementation until an **ACCEPTED** WF-R01.3.4 charter exists and explicitly authorizes Wave 1 (or equivalent first wave).

---

## 7. Dependency confirmation

```text
WF-R01.3.4 depends on accepted WF-R01.3.3 shell and structural policy.
```

| Dependency | Result |
|------------|--------|
| WF-R01.3.3 charter ACCEPTED | **Satisfied** (2026-06-19) |
| Waves S1–S4 evidence | **Satisfied** |
| WF-R01.3.3 subprogram COMPLETE | **Satisfied** (Wave S5 exit) |
| WF-R01.2 Gate 2 (RC 32/32) | **Satisfied** (prior) |
| WF-R01.3.4 charter | **NOT SATISFIED** — blocking execution only |

---

*Handoff artefact: `reports/wf-r01-3-3-to-wf-r01-3-4-handoff-v1.md` · v1 · 2026-06-19*
