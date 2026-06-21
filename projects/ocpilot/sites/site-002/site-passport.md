# SITE-002 — Site Passport

**Status:** **STABLE LIVE CHECKPOINT — M9.8.9 CATALOG UX COMPLETE 01**  
**Run:** Stable live checkpoint after catalog UX cluster completion (2026-06-21)

---

## Identity

| Field | Value |
|-------|-------|
| **Site ID** | SITE-002 |
| **Site Name** | ЗПМ |
| **Slug** | site-002 |
| **Platform** | ocStore / OpenCart |
| **Version** | SAFE UNKNOWN |
| **Baseline Match** | `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` |
| **Hosting** | Beget (FTP `polygonws.beget.tech`) — operator-recorded |
| **Access Methods** | Documented in [project-access-brief.md](project-access-brief.md); credential locations outside repo |
| **Storage Location** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-002\` |
| **Environment** | TEST |
| **Test URL** | https://zpm.new-site.space/ |
| **Current Status** | **STABLE LIVE CHECKPOINT — M9.8.9 CATALOG UX COMPLETE 01** |
| **Active baseline** | [baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md) |
| **Technical Knowledge Map** | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — incl. [§7 Filter Architecture](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#7-filter-architecture), [§8 Live Files](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#8-live-files-with-business-logic), [§14 Commercial Trust Block](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#14-commercial-trust-block), [§16 Catalog State Persistence](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#16-catalog-state-persistence) |
| **Operator manual JS (04B)** | [reports/SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md](reports/SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md) |
| **Rollback source** | Beget full backup + current live TEST + file-level pass backups |
| **Notes** | TEST площадка. **MANUAL UI / CSS / TWIG / JS REFINEMENTS ARE CANONICAL**. Catalog UX cluster complete: filter recovery + filter UX + Commercial Trust + state persistence (09A–09C) + hub cleanup (10). EC-01 mitigated by subcategories hide (07). M10 not authorized. |

---

## Authority policy

| Rule | Value |
|------|-------|
| **Authority checkpoint** | `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` |
| **MANUAL UI REFINEMENTS ARE CANONICAL** | Operator manual CSS, Twig, JS, and UX edits on live TEST override older M9.x deploy snapshots |
| **MANUAL CSS REFINEMENTS ARE CANONICAL** | Operator CSS edits on live TEST override repo work copies |
| **MANUAL TWIG REFINEMENTS ARE CANONICAL** | Operator Twig edits on live TEST override repo work copies |
| **Conflict resolution** | If any documentation contradicts current TEST state, **source of truth** = live TEST on https://zpm.new-site.space/ as registered in this checkpoint |
| **Do NOT use as visual baseline** | `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`, `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`, pre-M9.8.9 work copies |

---

## Stable checkpoint (active)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` |
| Registered | 2026-06-21 |
| Type | Stable live checkpoint (metadata registration) |
| Supersedes (live truth) | `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` |
| Recovery scope | Product reset · fresh 1C import · price index · filter hotfixes (06D–06M) |
| Filter UX scope | Scroll (04/04B) · hide subcategories (07) · group reset (08/08A) |
| Commercial Trust scope | M9.8.9-03B redesign · M9.8.9-03C deploy · operator manual polish · FAQ · OEM proof |
| Catalog state persistence | M9.8.9-09A / 09B / 09C — filter + limit + sort + pagination + only_with_price joint behaviour |
| Hub cleanup | M9.8.9-10 — no `page-intro__description` on `/katalog/nejtralnoe-oborudovanie` |
| Other UX | Wishlist/compare smart tooltips (01) |
| Completed M9.8 passes | M9.8.1 PDP Gallery · M9.8.2 Lightbox · M9.8.5 Products Per Page |
| Operator manual passes | PLP / filter / breakpoint / CSS / Twig polish · **JS refinements (04B)** |
| Knowledge map | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Open bugs | **EC-01** — mitigated by subcategories hide (07); M9.8.7 deferred |
| Next planned | Remaining M9.8.9 tasks per roadmap · **Corporate Pages Program** — IA **READY** · design charter pending · deferred M9.8.3/4/6/8 · **M10** — not authorized |
| Registration | [reports/SITE-002-STABLE-CHECKPOINT-M9.8.9-CATALOG-UX-COMPLETE-01.md](reports/SITE-002-STABLE-CHECKPOINT-M9.8.9-CATALOG-UX-COMPLETE-01.md) |

**Baseline doc:** [baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md)

---

## Prior checkpoints (historical)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` |
| Doc | [baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md) |
| Scope | Commercial Trust — superseded for live truth |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01` |
| Doc | [baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md) |
| Scope | Filter recovery + filter UX — historical |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` |
| Doc | [baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md](baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md) |
| Scope | M9.8.1/2/5 + operator PLP polish — historical |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14` |
| Doc | [baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md](baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md) |
| Scope | PDP V5.1 · Category V2.3.1 — historical |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI` |
| Doc | [reports/SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI.md](reports/SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI.md) |
| Scope | File + scoped DB JSON backup — historical file rollback only |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE` |
| Doc | [reports/SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE.md](reports/SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE.md) |
| Scope | Historical capture — homepage 5-branch deploy |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M9-COMPLETE-20260615` |
| Doc | [reports/SITE-002-STABLE-M9-COMPLETE.md](reports/SITE-002-STABLE-M9-COMPLETE.md) |
| Scope | Pre-M9.7D / pre-manual UI |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159` |
| Doc | [reports/SITE-002-STABLE-M8.3-BEFORE-M9.md](reports/SITE-002-STABLE-M8.3-BEFORE-M9.md) |
| Scope | Pre-M9 rollback — M7.1 + M8.3 only |

---

## Project status (BZPM)

### Завершено

- M7.1 Launch Mode
- M8 Cleanup
- M9 Filter Profiles
- M9.5 Hub Mode
- M9.7 Images
- M9.7 Megamenu Cleanup
- Homepage Neutral Branches
- Manual UI Refinement
- M9.8.1 PDP Gallery Compact
- M9.8.2 PDP Lightbox Constraints
- M9.8.5 Products Per Page Selector
- Operator manual PLP / filter / breakpoint / CSS / Twig polish
- **Product reset + fresh 1C import**
- **Price index recovery (06D, 06F)**
- **Filter UX polish (04, 04A, 04B, 07, 08, 08A)**
- **Wishlist / Compare smart tooltips (01)**
- **Commercial Trust block (03B/03C + operator manual polish)**
- **Catalog state persistence (09A, 09B, 09C)**
- **Hub cleanup — page-intro removal (10)**

### Активный этап

**M9.8.9 Minor Fixes Pack #1** — remaining tasks per [BZPM-PRODUCT-ROADMAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md)

### Corporate Pages Program

**Status:** **OPEN** — Research **COMPLETE** · IA / Architecture **READY** · Copy system **REGISTERED** · copy content not started · design / implementation not started  
**Program doc:** [BZPM-CORPORATE-PAGES-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-v1.md)  
**IA map:** [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-IA-MAP-v1.md)  
**Copy standard:** [BZPM-COPY-STANDARDS-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-COPY-STANDARDS-v1.md)

| ID | Page | URL (TEST) | Research | IA | Copy |
|----|------|------------|----------|-----|------|
| M9.13 | About Company | `/about` | Complete | Mapped | Registered |
| M9.14 | Delivery | `/delivery` | Complete | Mapped | Registered |
| M9.15 | Payment | `/payment-methods` | Complete | Mapped | Registered |
| M9.16 | Dealers | `/dealers` | Complete | Mapped | Registered |
| M9.17 | Warranty | `/guarantee` | Complete | Mapped | Registered |
| M9.18 | Custom Manufacturing | `/custom-equipment` | Complete | Mapped | Registered |

**Research artifacts:** [M9.13](reports/BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md) · [M9.14](reports/BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md) · [M9.15](reports/BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) · [M9.16](reports/BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) · [M9.17](reports/BZPM-M9.17-WARRANTY-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) · [M9.18](reports/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md)

**PAGE-COPY artifacts:** [M9.13](copy/BZPM-M9.13-ABOUT-COMPANY-PAGE-COPY-v1.md) · [M9.14](copy/BZPM-M9.14-DELIVERY-PAGE-COPY-v1.md) · [M9.15](copy/BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md) · [M9.16](copy/BZPM-M9.16-DEALERS-PAGE-COPY-v1.md) · [M9.17](copy/BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md) · [M9.18](copy/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.md)

**Contacts (separate workstream):** Status **Delivered** — IA mapped for cross-links only. Evidence: [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](reports/SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md)

### Отложено (M9.8 UX Polish Pack — остаток)

M9.8.3 Homepage Hero · M9.8.4 PLP Density · M9.8.6 UltraWide · M9.8.7 EC-01 · M9.8.8 Thumbnail Rail — per roadmap

---

## Next work rule

Before next SITE-002 change:

1. Read [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)
2. Use `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` as authority
3. For filters / sort / pagination / limit / only_with_price — read Knowledge Map **§16** + passes 09A/09B/09C
4. For filter / catalog / 1C / price / PLP — follow Knowledge Map §13 domain-specific PRE-TASK rule
5. For trust block / certificates / dealers form / category CTA — follow Knowledge Map §14 + §13 Commercial Trust PRE-TASK rule
6. Live-capture any files touched before deploy
7. **Do not** start M10 without operator charter

Rollback = Beget full backup → current live TEST → file-level pass backups.

---

## SAFE UNKNOWN

- ocStore / OpenCart exact version and release line
- Beget backup artifact location and timestamp (operator attestation only)
- M9.8.9-09C browser QA Q1–Q6 — operator interaction HITL pending
- M10 scope and authorization status
- Who populates `price2`, `price3`, `discount1c` in production workflow

---

## Security notes

| Check | Value |
|-------|-------|
| No secrets in checkpoint docs | **yes** |
| DB JSON in repo (prior baselines) | Row data only — treat as sensitive; no credentials in dumps |
