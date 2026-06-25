# BZPM Copy Standards v1

**Program:** BZPM Corporate Pages Program  
**Site:** SITE-002 (ЗПМ / BZPM) · TEST `https://zpm.new-site.space/`  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Policy:** MANUAL UI REFINEMENTS ARE CANONICAL  
**Date:** 2026-06-22  
**Status:** **ACTIVE** — copy artifact system registered

**Boundary:** Documentation and copy discipline only. This standard does **not** authorize design, wireframes, mockups, implementation, deploy, TEST writes, or production changes.

**Parent program:** [BZPM-CORPORATE-PAGES-PROGRAM-v1.md](BZPM-CORPORATE-PAGES-PROGRAM-v1.md)  
**IA map:** [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](BZPM-CORPORATE-PAGES-IA-MAP-v1.md)

---

## Purpose

Corporate Pages Program requires a **full final page text** for every program page — not block notes, not thesis bullets, not partial drafts.

Each approved PAGE-COPY artifact must be sufficient to reproduce the entire page text (headings, body, FAQ, CTA, forms, microcopy, captions, utility strings) **without** opening design files or implementation markup.

Operator decision (2026-06-22): after IA and copywriting for a page are complete, a **standalone complete textual artifact** must exist in MARS before Design Charter and Design phases.

---

## Required artefacts (per page)

Every Corporate Pages Program page (M9.13–M9.18) must have **four mandatory artefacts** in sequence:

| # | Artefact | Role | Status discipline |
|---|----------|------|-------------------|
| **01** | **Research** | Forensic / commercial evidence, URL discovery, objection map, gaps | `RESEARCH COMPLETE` before Copy work |
| **02** | **IA** | Purpose, audience, topic ownership, cross-links, block intent | `MAPPED` / operator-approved IA before Copy work |
| **03** | **Copy** | **Full final page text** — reproducible standalone document | `COPY COMPLETE` + operator approval before Design Charter |
| **04** | **Design Charter** | Visual scope, assets, breakpoints, operator OQ resolution | Operator charter before Design phase |

**Contacts (`/contact/`):** Delivered outside M9.13–M9.18 — not subject to this copy registration series.

---

## Storage layout

| Artefact type | Location | Pattern |
|---------------|----------|---------|
| **Research** | `projects/ocpilot/sites/site-002/reports/` | `BZPM-M9.{ID}-*-FORENSIC-RESEARCH.md` (registered names vary) |
| **IA** | [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](BZPM-CORPORATE-PAGES-IA-MAP-v1.md) | Per-page section `### M9.{ID} — …` |
| **Copy** | `projects/ocpilot/sites/site-002/copy/` | `BZPM-M9.{ID}-{PAGE-SLUG}-PAGE-COPY-v{N}.md` |
| **Design Charter** | `projects/website-factory/execution-cases/bzpm-roadmap/charters/` | `BZPM-M9.{ID}-{PAGE-SLUG}-DESIGN-CHARTER-v{N}.md` · [charters/README.md](charters/README.md) |
| **Design Brief** | `projects/website-factory/execution-cases/bzpm-roadmap/charters/` | `BZPM-M9.{ID}-{PAGE-SLUG}-DESIGN-BRIEF-v{N}.md` · [charters/README.md](charters/README.md) |

**Program index:** [BZPM-CORPORATE-PAGES-PROGRAM-v1.md](BZPM-CORPORATE-PAGES-PROGRAM-v1.md) — canonical registry with links to all four artefact types per page.

---

## Naming convention

### PAGE-COPY files

```
BZPM-M9.{NN}-{PAGE-SLUG}-PAGE-COPY-v{N}.md
```

| Component | Rule | Example |
|-----------|------|---------|
| `M9.{NN}` | Program milestone ID | `M9.13` |
| `{PAGE-SLUG}` | Uppercase kebab English slug | `ABOUT-COMPANY`, `DELIVERY`, `PAYMENT`, `DEALERS`, `WARRANTY`, `CUSTOM-MANUFACTURING` |
| `PAGE-COPY` | Fixed artefact type marker | always `PAGE-COPY` |
| `v{N}` | Major approved revision | `v1`, `v2`, `v3` |

### Registered PAGE-COPY paths (v1 shells)

| ID | File |
|----|------|
| M9.13 | [BZPM-M9.13-ABOUT-COMPANY-PAGE-COPY-v1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.13-ABOUT-COMPANY-PAGE-COPY-v1.md) |
| M9.14 | [BZPM-M9.14-DELIVERY-PAGE-COPY-v1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.14-DELIVERY-PAGE-COPY-v1.md) |
| M9.15 | [BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md) |
| M9.16 | [BZPM-M9.16-DEALERS-PAGE-COPY-v1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.16-DEALERS-PAGE-COPY-v1.md) |
| M9.17 | [BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md) |
| M9.18 | [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.md](../../../ocpilot/sites/site-002/copy/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.md) |

Minor copy edits (typo, punctuation, non-structural wording) may be applied in-place on the current approved version with changelog entry — **no** new file required. Structural or commercial revision → increment major version (`v2`, `v3`, …) and operator re-approval.

---

## PAGE-COPY content standard

Each PAGE-COPY file **must** contain the following when status is **COPY COMPLETE**:

| # | Required element | Notes |
|---|------------------|-------|
| 1 | **H1** | Single page title — matches approved IA intent |
| 2 | **Lead** | Intro paragraph(s) immediately under H1 |
| 3 | **All page blocks top → bottom** | Ordered sections matching approved IA block list |
| 4 | **All headings** | H2–H6 as used on page |
| 5 | **All body texts** | Full prose — no «TBD» in approved copy |
| 6 | **All FAQ** | Question + answer pairs in full |
| 7 | **All CTA** | Button labels, link labels, aria-facing strings where copy-defined |
| 8 | **All form texts** | Labels, placeholders, validation messages, submit buttons |
| 9 | **All micro-texts** | Badges, hints, tooltips (copy layer only) |
| 10 | **All captions** | Image/video/figure captions |
| 11 | **All utility texts** | Breadcrumb label, meta title/description if copy-owned, empty states |

**Reproducibility rule:** A reader with only Research + IA + PAGE-COPY must be able to reconstruct **100% of on-page text** without design or code.

**Forbidden in approved PAGE-COPY:**

- Block outlines without full text
- Bullet thesis notes instead of final copy
- «See design» / «TBD operator» in approved sections
- Splitting page text across multiple partial docs as the canonical source

**SAFE UNKNOWN in draft:** Allowed only while status is **REGISTERED** or **DRAFT** — must be resolved before operator approval.

---

## Versioning

| Version | Meaning |
|---------|---------|
| **v1** | First operator-approved full page copy |
| **v2** | Major approved revision (structure, commercial terms, block add/remove) |
| **v3** | Major approved revision |
| **vN** | Subsequent major approved revisions |

Version increments on **operator-approved major revision**, not on every edit pass. Prior version files remain in repo for audit (do not delete).

Each file header must record:

- `Version:` — e.g. `v1`
- `Status:` — `REGISTERED` · `DRAFT` · `COPY COMPLETE`
- `Approved by:` — operator identifier or «pending»
- `Approval date:` — ISO date or «pending»

---

## Approval workflow

Sequential gate — **no phase skipping**:

```
Research  →  IA  →  Copy  →  Design Charter  →  Design  →  Implementation
```

| Step | Gate | Approver | Blocks |
|------|------|----------|--------|
| 1 | **Research complete** | Operator review of forensic report | IA finalization for page |
| 2 | **IA approved** | Operator approval of IA map section (or map as whole) | Copywriting pass |
| 3 | **Copy complete** | Operator approval of PAGE-COPY vN | Design Charter |
| 4 | **Design Charter approved** | Operator charter per page | Wireframes / visual design |
| 5 | **Design approved** | Operator HITL on design deliverables | Implementation |
| 6 | **Implementation charter** | Operator charter | TEST / deploy writes |

**Copy pass inputs (mandatory read order):**

1. Page Research artefact (M9.XX forensic report)
2. Page IA section in [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](BZPM-CORPORATE-PAGES-IA-MAP-v1.md)
3. [BZPM-COPY-STANDARDS-v1.md](BZPM-COPY-STANDARDS-v1.md) (this document)
4. Operator OQ resolutions relevant to page (payment VAT, warranty term, dealer framework, custom SLA, etc.)

**Copy pass outputs:**

- Updated PAGE-COPY file with status **COPY COMPLETE**
- Changelog entry in PAGE-COPY file and program doc
- Registration note in program / OCPilot state if milestone closes

**Explicit stops:**

- Research complete **≠** copy authorized without IA approval
- Copy complete **≠** design authorized without Design Charter
- Design **≠** implementation authorized without implementation charter

---

## Program registry cross-reference

| ID | Page | Research | IA | Copy (canonical) | Design Charter | Design Brief |
|----|------|----------|-----|------------------|----------------|--------------|
| M9.13 | About Company | [Forensic](../../../ocpilot/sites/site-002/reports/BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md) | [IA § M9.13](BZPM-CORPORATE-PAGES-IA-MAP-v1.md#m913--about-company-about) | [PAGE-COPY v1.1](../../../ocpilot/sites/site-002/copy/BZPM-M9.13-ABOUT-COMPANY-PAGE-COPY-v1.1.md) | [Charter v1](charters/BZPM-M9.13-ABOUT-COMPANY-DESIGN-CHARTER-v1.md) | [Brief v1](charters/BZPM-M9.13-ABOUT-COMPANY-DESIGN-BRIEF-v1.md) |
| M9.14 | Delivery | [Forensic](../../../ocpilot/sites/site-002/reports/BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md) | [IA § M9.14](BZPM-CORPORATE-PAGES-IA-MAP-v1.md#m914--delivery-delivery) | [PAGE-COPY v1.1](../../../ocpilot/sites/site-002/copy/BZPM-M9.14-DELIVERY-PAGE-COPY-v1.1.md) | [Charter v1](charters/BZPM-M9.14-DELIVERY-DESIGN-CHARTER-v1.md) | [Brief v1](charters/BZPM-M9.14-DELIVERY-DESIGN-BRIEF-v1.md) |
| M9.15 | Payment | [Forensic](../../../ocpilot/sites/site-002/reports/BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) | [IA § M9.15](BZPM-CORPORATE-PAGES-IA-MAP-v1.md#m915--payment-payment-methods) | [PAGE-COPY v1](../../../ocpilot/sites/site-002/copy/BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md) | [Charter v1](charters/BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md) | [Brief v1](charters/BZPM-M9.15-PAYMENT-DESIGN-BRIEF-v1.md) |
| M9.16 | Dealers | [Forensic](../../../ocpilot/sites/site-002/reports/BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) | [IA § M9.16](BZPM-CORPORATE-PAGES-IA-MAP-v1.md#m916--dealers-dealers) | [PAGE-COPY v1.1](../../../ocpilot/sites/site-002/copy/BZPM-M9.16-DEALERS-PAGE-COPY-v1.1.md) | [Charter v1](charters/BZPM-M9.16-DEALERS-DESIGN-CHARTER-v1.md) | [Brief v1](charters/BZPM-M9.16-DEALERS-DESIGN-BRIEF-v1.md) |
| M9.17 | Warranty | [Forensic](../../../ocpilot/sites/site-002/reports/BZPM-M9.17-WARRANTY-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) | [IA § M9.17](BZPM-CORPORATE-PAGES-IA-MAP-v1.md#m917--warranty-guarantee) | [PAGE-COPY v1](../../../ocpilot/sites/site-002/copy/BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md) | [Charter v1](charters/BZPM-M9.17-WARRANTY-DESIGN-CHARTER-v1.md) | [Brief v1](charters/BZPM-M9.17-WARRANTY-DESIGN-BRIEF-v1.md) |
| M9.18 | Custom Manufacturing | [Forensic](../../../ocpilot/sites/site-002/reports/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) | [IA § M9.18](BZPM-CORPORATE-PAGES-IA-MAP-v1.md#m918--custom-manufacturing-custom-equipment) | [PAGE-COPY v1.1](../../../ocpilot/sites/site-002/copy/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md) | [Charter v1](charters/BZPM-M9.18-CUSTOM-MANUFACTURING-DESIGN-CHARTER-v1.md) | [Brief v1](charters/BZPM-M9.18-CUSTOM-MANUFACTURING-DESIGN-BRIEF-v1.md) |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-22 | **CREATED** — BZPM Copy Standards v1; four-artefact model; PAGE-COPY naming, storage, versioning, approval workflow; M9.13–M9.18 v1 shells registered |
| 2026-06-22 | **RECONCILED** — Charter/brief storage active; canonical PAGE-COPY v1/v1.1 links; full registry — [BZPM-CORPORATE-PAGES-PROGRAM-RECONCILIATION-v1.md](BZPM-CORPORATE-PAGES-PROGRAM-RECONCILIATION-v1.md) |

---

*BZPM Copy Standards v1 — documentation only. No copywriting, design, or implementation authorized by this document alone.*
