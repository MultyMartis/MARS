# Website Factory — Page Architecture Gaps v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-architecture/`  
**Статус:** honesty register — что **не** покрыто Page Architecture v1  
**Дата:** 2026-05-31

---

## Covered by v1 (baseline)

| Item | Artifact |
|------|----------|
| Page contract field schema | PAGE-CONTRACT-v1 |
| 10 canonical page types | PAGE-TYPE-REGISTRY-v1 |
| Core block stacks per page type | CORE-PAGE-ARCHITECTURES-v1 |
| Site type × page type matrix | SITE-TYPE-PAGE-MATRIX-v1 |
| Page-level dependencies | PAGE-DEPENDENCY-RULES-v1 |
| Legal page specialization | LEGAL-PAGE-CONTRACT-v1 |
| Production flow | PAGE-IMPLEMENTATION-RULES-v1 |

---

## Remaining gaps

### Design mapping

| Gap | Status |
|-----|--------|
| Page type → design component map | **NOT CATALOGED** |
| Block → Figma / token binding | **FUTURE** (Design System Mapping priority) |
| Legal page → design tokens (beyond content-page) | Partial in reference SCSS only |

### Content contracts

| Gap | Status |
|-----|--------|
| Copy length / tone per page_type | **NOT DEFINED** |
| H1/H2 content patterns per money page | **NOT DEFINED** |
| Legal variable content beyond Legal Pack | Covered in legal/ — **not** page-architecture |

### SEO contracts

| Gap | Status |
|-----|--------|
| Per-page SEO contract fields (beyond intent in PAGE-CONTRACT) | **ADDRESSED** — [PAGE-SEO-CONTRACT-v1.md](../seo-architecture/PAGE-SEO-CONTRACT-v1.md) (SEO v2 **ACCEPTED** 2026-06-01) |
| Faceted URL / PLP indexation rules | **FUTURE** |
| Schema.org per page_type machine spec | **NOT DEFINED** |

### Component contracts

| Gap | Status |
|-----|--------|
| Partial HTML contract per block on page | **NOT DEFINED** |
| Accessibility requirements per page_type | **NOT DEFINED** |
| Responsive block variants per page | **NOT CATALOGED** (see BLOCK-GAPS) |

### Template contracts

| Gap | Status |
|-----|--------|
| Nunjucks / page template file per page_type | **NOT DEFINED** |
| Project IA single-file schema | **NOT STANDARDIZED** |
| Thank-you / utility page types | **FUTURE** |

### Machine schema

| Gap | Status |
|-----|--------|
| JSON Schema for PAGE-CONTRACT | **FUTURE** |
| Automated Blueprint `required_pages` ↔ contracts diff | **FUTURE** |
| Validator CLI | **FUTURE** |

### Extended site types

| Gap | Status |
|-----|--------|
| SAAS page architectures | **EXPLICITLY OUT OF SCOPE** v1 |
| WEB_APPLICATION page architectures | **OUT OF SCOPE** |
| MARKETPLACE page architectures | **OUT OF SCOPE** |

### ECOMMERCE extensions

| Gap | Status |
|-----|--------|
| `CART_PAGE`, `CHECKOUT_PAGE` in Page Type Registry minimum | **DEFERRED** — Blueprint + dependency rules only |
| Account / buyer portal pages | **FUTURE** |
| ECOMMERCE Legal Extension pages | **NOT FROZEN** (Legal Pack) |

### Cross-layer consistency

| Gap | Status |
|-----|--------|
| BLOCK-IMPLEMENTATION-RULES sequencing text | **PENDING** brain polishing pass |
| SITE-TYPE-BLOCK-MAPPING v1 cross-links to page-architecture | **PENDING** |
| OPERATIONAL-INDEX / foundation checkpoint update | **PENDING** operator pass |

---

## Recommended next workstreams (from gaps)

| Priority (roadmap) | Closes gap |
|--------------------|------------|
| Design System Mapping | Design mapping, component contracts (partial) |
| SITE-TYPE-SEO-MAPPING-v2 | SEO contracts depth |
| Brain polishing | Cross-links, BLOCK-IMPLEMENTATION-RULES alignment |
| Content contracts (not queued) | Copy patterns — **requires charter** |

---

## SAFE UNKNOWN

- Whether thank-you pages become `UTILITY_PAGE` or stay project-specific — **undecided**
- International (non-RU) legal page architecture — **OUT OF SCOPE** Legal Pack v1

---

*Page Architecture Gaps version: v1.*
