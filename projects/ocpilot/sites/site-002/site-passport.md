# SITE-002 — Site Passport

**Status:** **STABLE LIVE CHECKPOINT — HOME COMMERCIAL TRUST 01**  
**Run:** Home CTA `zpm-commercial-trust` replacement (2026-06-29)

---

## Identity

| Field | Value |
|-------|-------|
| **Site ID** | SITE-002 |
| **Site Name** | ЗПМ |
| **Slug** | site-002 |
| **Platform** | ocStore / OpenCart |
| **Version** | SAFE UNKNOWN |
| **Baseline Match** | `SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01` (Home) · `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02` (About) · `SITE-002-STABLE-LIVE-LOCAL-FONTS-01` (site-wide fonts) |
| **Hosting** | Beget (FTP `polygonws.beget.tech`) — operator-recorded |
| **Access Methods** | Documented in [project-access-brief.md](project-access-brief.md); credential locations outside repo |
| **Storage Location** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-002\` |
| **Environment** | TEST |
| **Test URL** | https://zpm.new-site.space/ |
| **Current Status** | **STABLE LIVE CHECKPOINT — HOME COMMERCIAL TRUST 01** |
| **Active baseline** | [baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md](baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md) · About: [M9.13-ABOUT-REDESIGN-02](baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02.md) · fonts: [LOCAL-FONTS-01](baselines/SITE-002-STABLE-LIVE-LOCAL-FONTS-01.md) |
| **Technical Knowledge Map** | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — incl. [§7 Filter Architecture](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#7-filter-architecture), [§8 Live Files](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#8-live-files-with-business-logic), [§14 Commercial Trust Block](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#14-commercial-trust-block), [§16 Catalog State Persistence](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#16-catalog-state-persistence), [§17 About Page History](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#17-about-page-history), [§26 Operator Manual Polish 01](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#26-operator-manual-polish-01--superseded-visual-baseline-retained), [§27 Local Fonts 01](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#27-local-fonts-01--active) |
| **Operator manual JS (04B)** | [reports/SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md](reports/SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md) |
| **Rollback source** | Beget full backup + current live TEST + file-level pass backups |
| **Notes** | TEST площадка. **MANUAL UI / CSS / TWIG / JS REFINEMENTS ARE CANONICAL**. **Delivery summary strip** — Commercial Trust service cards on `/delivery` **PASS** (2026-06-29) · [Knowledge Map §32](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#32-delivery-summary--commercial-trust-reuse-active) · checkpoint `SITE-002-STABLE-LIVE-DELIVERY-SUMMARY-01`. **Custom OEM proof strip** — Commercial Trust service cards on `/custom-equipment` **PASS** (2026-06-29) · [Knowledge Map §31](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#31-custom-oem-proof-strip--commercial-trust-reuse-active) · checkpoint `SITE-002-STABLE-LIVE-CUSTOM-PROOF-STRIP-01`. **PDP body category classes** — `category-root-*` / `category-parent-*` on product pages **PASS** (2026-06-29) · [Knowledge Map §30](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#30-pdp-body-category-classes-01--active) · checkpoint `SITE-002-STABLE-LIVE-PDP-BODY-CATEGORY-CLASSES-01`. **Corporate intro blocks** — `.zpm-corp-intro` on 6 corp pages **PASS** (2026-06-29 closeout) · [Knowledge Map §29](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#29-corporate-intro-image-blocks-01--active) · checkpoint `SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01`. **Home CTA** — `zpm-commercial-trust` active (2026-06-29). **M9.13 About redesign RE-ACTIVATED** (2026-06-29). Local Fonts 01 **retained**. |

---

## Authority policy

| Rule | Value |
|------|-------|
| **Authority checkpoint** | `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02` (About) · `SITE-002-STABLE-LIVE-LOCAL-FONTS-01` (fonts) |
| **MANUAL UI REFINEMENTS ARE CANONICAL** | Operator manual CSS, Twig, JS, and UX edits on live TEST override older M9.x deploy snapshots |
| **MANUAL CSS REFINEMENTS ARE CANONICAL** | Operator CSS edits on live TEST override repo work copies |
| **MANUAL TWIG REFINEMENTS ARE CANONICAL** | Operator Twig edits on live TEST override repo work copies |
| **Conflict resolution** | If any documentation contradicts current TEST state, **source of truth** = live TEST on https://zpm.new-site.space/ as registered in this checkpoint |
| **Do NOT use as visual baseline** | Pass 1.2 CSS/HTML/JS · `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2` · pre-checkpoint work copies · `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` · M9.13 About redesign work copies |

---

## Stable checkpoint (active)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01` |
| Registered | 2026-06-29 |
| Type | Stable live checkpoint — Home CTA band FTP deploy |
| Scope | Home only — `/katalog` legacy `blockdealersform` preserved |
| Report | [SITE-002-HOME-COMMERCIAL-TRUST-REPLACEMENT.md](reports/SITE-002-HOME-COMMERCIAL-TRUST-REPLACEMENT.md) |
| Knowledge map | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — §28 |

**Baseline doc:** [baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md](baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md)

---

## Prior stable checkpoint

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01` |
| Registered | 2026-06-29 |
| Type | Stable live checkpoint — FTP read-only capture + metadata registration |
| Supersedes (live truth) | `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2` |
| Operator manual delta | `style.css` · `dealers.twig` changed vs Pass 1.2 / Pass 1.1 deploy snapshots |
| Capture | [capture-manifest.json](reports/site-002-operator-manual-polish-01-work/capture-manifest.json) |
| Knowledge map | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — §26 |
| Registration | [reports/SITE-002-STABLE-CHECKPOINT-OPERATOR-MANUAL-POLISH-01.md](reports/SITE-002-STABLE-CHECKPOINT-OPERATOR-MANUAL-POLISH-01.md) |

**Baseline doc:** [baselines/SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01.md](baselines/SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01.md)

---

## Prior checkpoints (historical)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2` |
| Doc | [baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md](baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md) |
| Scope | Corp visual polish Pass 1.2 — **superseded**; do not use as reference |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` |
| Doc | [baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md) |
| Scope | About restoration — superseded for live visual truth |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` |
| Doc | [baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md) |
| Scope | Catalog UX cluster — superseded for live truth |

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

### BZPM UX REDESIGN — project banner

| Field | Value |
|-------|--------|
| **Project** | BZPM UX REDESIGN (SITE-002) |
| **Recovery status** | **CLOSED** (2026-06-28) — [SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md](reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md) |
| **Production status** | **READY AFTER OPERATOR GATES** |
| **Current phase** | **PRODUCTION PREPARATION** |
| **Next phase** | **Production Development** — Corporate Pages implementation after operator gates |
| **Implementation (corp pages)** | M9.14–M9.18 **IMPLEMENTED** on TEST — program implementation phase **COMPLETE** (pending operator B6/B8) |
| **Live About authority** | `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` |
| **M9.13 redesign** | **ARCHIVED** · **NOT ACTIVE** — never implementation authority |

**Lifecycle:** Research → Corporate Pages Program → Recovery (**CLOSED**) → Production Development

**Post-recovery reconciliation:** [SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md](reports/SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md)

### Active blockers (production path)

Recovery is **not** a blocker. Operator gates before Corporate Pages implementation:

| Blocker | Status | Affected |
|---------|--------|----------|
| **B6** | OPEN | Design Charter operator approval — all M9.13–M9.18 |
| **B8** | OPEN | PAGE-COPY formal sign-off — all M9.13–M9.18 |
| **B1** | OPEN | МО warehouse address — M9.14 · M9.16 |
| **B3** | OPEN | PLP dealer form vs `/dealers` — M9.16 |

**Operator implementation order:** M9.14 Delivery → M9.15 Payment → M9.17 Warranty → M9.16 Dealers → M9.18 Custom Manufacturing — **all IMPLEMENTED** (2026-06-28). **M9.18 checkpoint** `SITE-002-STABLE-LIVE-M9.18-CUSTOM-01` — [SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md](reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md). **Design order** (historical, unchanged): M9.13 → M9.15 → M9.14 → M9.17 → M9.16 → M9.18 — see [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md).

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
- **M9.13 About Company** — redesigned, polished, **rejected by operator**, **restored** to pre-redesign state

### Активный этап

**M9.8.9 Minor Fixes Pack #1** — remaining tasks per [BZPM-PRODUCT-ROADMAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md)

### Corporate Pages Program

**Status:** **OPEN** — Research **COMPLETE** · IA **READY** · Copy **SUBSTANTIVELY COMPLETE** (sign-off pending) · Design Charter **DRAFT COMPLETE / APPROVAL OPEN** · visual design **NOT OPEN** · implementation **not started**  
**Program doc:** [BZPM-CORPORATE-PAGES-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-v1.md)  
**IA map:** [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-IA-MAP-v1.md)  
**Design program:** [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md)  
**Charters:** [charters/README.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/README.md)  
**Copy standard:** [BZPM-COPY-STANDARDS-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-COPY-STANDARDS-v1.md)

| ID | Page | URL (TEST) | Research | IA | Copy | Design Charter | Design Brief |
|----|------|------------|----------|-----|------|----------------|--------------|
| M9.13 | About Company | `/about` | Complete | Mapped | Substantively complete (v1.1) | Draft complete | **IMPLEMENTED · QA PASSED · REJECTED · RESTORED** |
| M9.14 | Delivery | `/delivery` | Complete | Mapped | Substantively complete (v1.1) | Draft complete | **IMPLEMENTED · QA PASSED** |
| M9.15 | Payment | `/payment-methods` | Complete | Mapped | Substantively complete (v1) | Draft complete | **IMPLEMENTED · QA PASSED** |
| M9.16 | Dealers | `/dealers` | Complete | Mapped | Substantively complete (v1.1) | Draft complete | **IMPLEMENTED · QA PASSED** |
| M9.17 | Warranty | `/guarantee` | Complete | Mapped | Substantively complete (v1) | Draft complete | **IMPLEMENTED · QA PASSED** |
| M9.18 | Custom Manufacturing | `/custom-equipment` | Complete | Mapped | Substantively complete (v1.1) | Draft complete | **IMPLEMENTED · QA PASSED** |

**Research artifacts:** [M9.13](reports/BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md) · [M9.14](reports/BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md) · [M9.15](reports/BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) · [M9.16](reports/BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) · [M9.17](reports/BZPM-M9.17-WARRANTY-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) · [M9.18](reports/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md)

**PAGE-COPY artifacts (canonical):** [M9.13 v1.1](copy/BZPM-M9.13-ABOUT-COMPANY-PAGE-COPY-v1.1.md) · [M9.14 v1.1](copy/BZPM-M9.14-DELIVERY-PAGE-COPY-v1.1.md) · [M9.15 v1](copy/BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md) · [M9.16 v1.1](copy/BZPM-M9.16-DEALERS-PAGE-COPY-v1.1.md) · [M9.17 v1](copy/BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md) · [M9.18 v1.1](copy/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md)

**Contacts (separate workstream):** Status **Delivered** — IA mapped for cross-links only. Evidence: [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](reports/SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md)

**M9.14 Delivery implementation:** **IMPLEMENTED** on TEST (2026-06-28) — checkpoint `SITE-002-STABLE-LIVE-M9.14-DELIVERY-01` · [SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md](reports/SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md)

**M9.15 Payment implementation:** **IMPLEMENTED** on TEST (2026-06-28) — checkpoint `SITE-002-STABLE-LIVE-M9.15-PAYMENT-01` · [SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md](reports/SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md)

**M9.17 Warranty implementation:** **IMPLEMENTED** on TEST (2026-06-28) — checkpoint `SITE-002-STABLE-LIVE-M9.17-WARRANTY-01` · [SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md](reports/SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md)

**M9.16 Dealers implementation:** **IMPLEMENTED** (2026-06-28) · checkpoint `SITE-002-STABLE-LIVE-M9.16-DEALERS-01` · B3 PLP reconciliation **OPEN / out of scope** · [SITE-002-M9.16-DEALERS-IMPLEMENTATION.md](reports/SITE-002-M9.16-DEALERS-IMPLEMENTATION.md)

**M9.18 Custom Manufacturing:** **IMPLEMENTED** (2026-06-28) · checkpoint `SITE-002-STABLE-LIVE-M9.18-CUSTOM-01` · [SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md](reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md) · **terminal corp page** — program implementation phase **COMPLETE on TEST**

**Post-recovery completeness:** [SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md](reports/SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md) — audit semantics reconciled 2026-06-28.

**Recovery closeout:** [SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md](reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md) — recovery **CLOSED**; production preparation active.

### Отложено (M9.8 UX Polish Pack — остаток)

M9.8.3 Homepage Hero · M9.8.4 PLP Density · M9.8.6 UltraWide · M9.8.7 EC-01 · M9.8.8 Thumbnail Rail — per roadmap

---

## Next work rule

Before next SITE-002 change:

1. Read [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)
2. Use `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` as authority
3. For About page — read Knowledge Map **§17** + M9.13 restore/redesign/polish reports
4. For filters / sort / pagination / limit / only_with_price — read Knowledge Map **§16** + passes 09A/09B/09C
5. For filter / catalog / 1C / price / PLP — follow Knowledge Map §13 domain-specific PRE-TASK rule
6. For trust block / certificates / dealers form / category CTA — follow Knowledge Map §14 + §13 Commercial Trust PRE-TASK rule
7. Live-capture any files touched before deploy
8. **Do not** start M10 without operator charter

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
