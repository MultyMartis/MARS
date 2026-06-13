# Website Factory — Hygiene Pass v1

**Версия:** v1  
**Дата:** 2026-06-01  
**Operator:** APPROVED BY OPERATOR  
**Область:** `workspaces/website-factory-reference-v1/`  
**Тип:** documentation-only hygiene — **no** new systems, layers, site types, Design Mapping, SEO expansion, runtime, automation  
**Статус:** **COMPLETE**

**Источник находок:** [BRAIN-CONSISTENCY-PASS-v1.md](BRAIN-CONSISTENCY-PASS-v1.md) (BCP v1 audit)

**Связанные документы:** [WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md](WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md), [ARCHITECTURE-FOUNDATION-v1.md](ARCHITECTURE-FOUNDATION-v1.md), [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md)

---

## Executive summary

Documentation hygiene sprint закрыл **документационный drift**, выявленный Brain Consistency Pass v1: supersession banners, canonical pointers (SEO v2, block-registry v1), freeze maturity sync, blueprint SEO sources, historical checkpoint marking, broken snapshot references.

**Design Mapping readiness (post-hygiene):** **YES WITH WARNINGS** — см. § Design Mapping readiness.

**Не выполнялось (вне charter):** BCP-006/007 page-layer `block_id` normalization; BCP-019 external `projects/mars-website-factory/*-v0` merge; Design documents; registry expansion.

---

## Issue action log

| Issue | Action | Files updated | Result | Status |
|-------|--------|---------------|--------|--------|
| **BCP-001** | Superseded banner on SITE-TYPE-BLOCK-MAPPING-v1; point to `block-registry/` + SITE-TYPE-BLOCK-MATRIX-v2; v0 marked legacy external | [registry/SITE-TYPE-BLOCK-MAPPING-v1.md](registry/SITE-TYPE-BLOCK-MAPPING-v1.md) | Canonical `block_id` path unambiguous | **CLOSED** |
| **BCP-002** | Registry index: canonical SEO v2, block-registry, legal v2; v1 mappings marked historical | [registry/SITE-TYPE-REGISTRY-v1.md](registry/SITE-TYPE-REGISTRY-v1.md) | Entry-point drift reduced | **CLOSED** |
| **BCP-003** | Implementation rules gates → seo-architecture/, block-registry/, legal v2 | [registry/SITE-TYPE-IMPLEMENTATION-RULES-v1.md](registry/SITE-TYPE-IMPLEMENTATION-RULES-v1.md) | Stage gates aligned | **CLOSED** |
| **BCP-004** | Blueprint system docs: SEO v2 + BLOCK-REGISTRY-v1 canonical; v0 not canon | [blueprints/BLUEPRINT-SYSTEM-v1.md](blueprints/BLUEPRINT-SYSTEM-v1.md), [blueprints/BLUEPRINT-CONTRACT-v1.md](blueprints/BLUEPRINT-CONTRACT-v1.md), [blueprints/BLUEPRINT-IMPLEMENTATION-RULES-v1.md](blueprints/BLUEPRINT-IMPLEMENTATION-RULES-v1.md), [blueprints/BLUEPRINT-GAPS-v1.md](blueprints/BLUEPRINT-GAPS-v1.md) | Blueprint authoring pointers corrected | **CLOSED** |
| **BCP-005** | Core 5 Blueprints `seo_requirements` Source → SITE-TYPE-SEO-MAPPING-v2 | [blueprints/LANDING-BLUEPRINT-v1.md](blueprints/LANDING-BLUEPRINT-v1.md), [blueprints/PROMO-BLUEPRINT-v1.md](blueprints/PROMO-BLUEPRINT-v1.md), [blueprints/CATALOG-BLUEPRINT-v1.md](blueprints/CATALOG-BLUEPRINT-v1.md), [blueprints/ECOMMERCE-BLUEPRINT-v1.md](blueprints/ECOMMERCE-BLUEPRINT-v1.md), [blueprints/CORPORATE-BLUEPRINT-v1.md](blueprints/CORPORATE-BLUEPRINT-v1.md) | SEO source lines on v2 | **CLOSED** |
| **BCP-009** | FREEZE §3 SEO depth row → Production-ready / seo-architecture ACCEPTED | [WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md](WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md) | Maturity table aligned with §5/§9/§11 | **CLOSED** |
| **BCP-010** | FREEZE §4: SEO v2 moved from QUEUED exclusions to ACCEPTED | [WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md](WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md) | Exclusions list consistent | **CLOSED** |
| **BCP-011** | ARCHITECTURE-FOUNDATION purpose + §12 Design Mapping readiness (post-SEO) | [ARCHITECTURE-FOUNDATION-v1.md](ARCHITECTURE-FOUNDATION-v1.md) | Stale pre-SEO wording removed | **CLOSED** |
| **BCP-012** | HISTORICAL banner on FOUNDATION-CHECKPOINT; status tables = 2026-05-30 only | [WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md](WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md) | Checkpoint not read as current state | **CLOSED** |
| **BCP-013** | Snapshot path marked legacy / not in-repo; no fabricated paths | [WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md](WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md) | Broken link → historical reference | **CLOSED** |
| **BCP-014** | Superseded banner on registry SITE-TYPE-LEGAL-MAPPING-v1 | [registry/SITE-TYPE-LEGAL-MAPPING-v1.md](registry/SITE-TYPE-LEGAL-MAPPING-v1.md) | Parity with legal v2 supersession | **CLOSED** |
| **Related** | Gap registers: BLOCK-REGISTRY-GAPS, BLOCK-GAPS, PAGE-GAPS, BLUEPRINT-GAPS G4, BLOCK-REGISTRY-AUDIT | [block-registry/](block-registry/), [page-architecture/PAGE-GAPS-v1.md](page-architecture/PAGE-GAPS-v1.md), [blueprints/BLUEPRINT-GAPS-v1.md](blueprints/BLUEPRINT-GAPS-v1.md) | Cross-layer stale QUEUED rows closed | **CLOSED** |
| **BCP-006** | — | — | `STICKY_CTA` in CORE-PAGE-ARCHITECTURES — not in hygiene scope | **OPEN** |
| **BCP-007** | — | — | `VIDEO` orphan in page layer — not in hygiene scope | **OPEN** |
| **BCP-008** | — | — | HEADER_NAV / FILTERS / SEARCH — by design (BLOCK-GAPS) | **ACKNOWLEDGED** |
| **BCP-019** | — | — | External v0 files — pointer discipline only | **OPEN** |
| **BCP-020** | — | — | Blueprint role → `block_id` cheat sheet — Design Mapping deliverable | **OPEN** |

---

## Task 1 — BCP issue review (focused)

Reviewed per charter: **BCP-001, BCP-004, BCP-005, BCP-012, BCP-013** plus directly related **BCP-002, BCP-003, BCP-009, BCP-010, BCP-011, BCP-014**. No new issues invented.

---

## Task 2 — Supersession cleanup

| Document | Change |
|----------|--------|
| SITE-TYPE-BLOCK-MAPPING-v1 | Superseded banner → block-registry/ |
| SITE-TYPE-LEGAL-MAPPING-v1 (registry) | Superseded banner → legal/SITE-TYPE-LEGAL-MAPPING-v2 |
| WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1 | HISTORICAL — superseded by FREEZE + ARCHITECTURE-FOUNDATION |
| SITE-TYPE-SEO-MAPPING-v1 | No change — banner already present (pre-hygiene) |

**Rule compliance:** no file deletions; no history rewrite; legacy docs retained.

---

## Task 3 — SEO source cleanup

- Blueprint system layer → `seo-architecture/SITE-TYPE-SEO-MAPPING-v2.md`, `PAGE-SEO-CONTRACT-v1.md`
- All Core 5 Blueprints `seo_requirements` **Source:** updated to v2
- BLUEPRINT-GAPS G4 → ACCEPTED state

---

## Task 4 — Block Registry source cleanup

- Blueprint docs → `block-registry/BLOCK-REGISTRY-v1.md`, `BLUEPRINT-BLOCK-MAPPING-v1.md`
- `block-registry-v0` demoted to legacy external pointer (not deleted)
- SITE-TYPE-BLOCK-MAPPING-v1 no longer claims v0 as canonical

**Rule compliance:** no `block_id` changes; no registry redesign.

---

## Task 5 — Foundation freeze sync

| Document | Before | After |
|----------|--------|-------|
| FREEZE §3 SEO depth | Shallow (v1), v2 QUEUED | Production-ready, seo-architecture ACCEPTED |
| FREEZE §4 exclusions | SEO v2 QUEUED — not started | SEO v2 ACCEPTED; Design QUEUED / NEXT |
| FREEZE §1 purpose | Pre-SEO v2 start wording | Post-SEO; Design Mapping next |
| ARCHITECTURE-FOUNDATION | Pre-SEO checkpoint purpose | Post-SEO / pre-Design |
| NEXT-PRIORITIES | SEO last completed only | BCP + Hygiene COMPLETE added |

Freeze, Architecture Foundation, and Roadmap now describe **same accepted systems** for SEO v2 and next workstream.

---

## Task 6 — Broken references

| Reference | Handling |
|-----------|----------|
| `../_snapshots/snap-20260530-website-factory-legal-blueprint-foundation-v1/` | Marked **historical / not in-repo** (2026-06-01 scan); plain-text path, no fabricated restore |
| Checkpoint report subpath | Same — legacy reference; pointer to FREEZE §10 |

---

## Task 8 — Health recheck

| Category | Before hygiene (BCP) | After hygiene |
|----------|----------------------|---------------|
| **Layer Consistency** | PASS WITH WARNINGS | **PASS WITH WARNINGS** (page-layer STICKY_CTA/VIDEO remain) |
| **Naming Consistency** | PASS WITH WARNINGS | **PASS WITH WARNINGS** (unchanged — BCP-006/007/019) |
| **Registry Consistency** | PASS WITH WARNINGS | **PASS** (registry index + block mapping banner closed) |
| **Matrix Consistency** | PASS | **PASS** (unchanged) |
| **Cross-Link Consistency** | PASS WITH WARNINGS | **PASS WITH WARNINGS** (external v0 discipline only) |
| **Documentation Hygiene** | PASS WITH WARNINGS | **PASS WITH WARNINGS** (residual page-layer + design cheat sheet) |

**Overall:** **PASS WITH WARNINGS** (improved from BCP on registry/cross-link/freeze dimensions).

---

## Task 9 — Design Mapping readiness

**Answer: YES WITH WARNINGS**

Design System Mapping **may begin** under operator charter.

### Remaining warnings (exact)

1. **BCP-006** — `STICKY_CTA` in [page-architecture/CORE-PAGE-ARCHITECTURES-v1.md](page-architecture/CORE-PAGE-ARCHITECTURES-v1.md) vs canonical `CTA` in BLOCK-REGISTRY-v1.
2. **BCP-007** — `VIDEO` optional block not in registry (29 ids).
3. **BCP-008** — HEADER_NAV, FILTERS, SEARCH: layout chrome, not `block_id` until charter.
4. **BCP-019** — `projects/mars-website-factory/block-registry-v0.md` / `site-type-registry-v0.md` coexist externally — do not mix vocabularies.
5. **BCP-020** — Blueprint human role → `block_id` cheat sheet not yet published (Design Mapping deliverable).

### Would block Mapping

- None identified post-hygiene for Core 5 matrix chain.

---

## Task 10 — Roadmap

| Item | Status |
|------|--------|
| Brain Consistency Pass v1 | **COMPLETE** — [BRAIN-CONSISTENCY-PASS-v1.md](BRAIN-CONSISTENCY-PASS-v1.md) |
| Hygiene Pass v1 | **COMPLETE** — this document |
| Design System Mapping | **QUEUED / NEXT** — **not started** (no Design artefacts created) |

Updated: [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md)

---

## Validation (charter compliance)

| Rule | Compliant? |
|------|------------|
| No new systems | **YES** |
| No new layers | **YES** |
| No new site types | **YES** |
| No Design Mapping artefacts | **YES** |
| No SEO expansion | **YES** |
| No runtime / automation | **YES** |
| No commit / push | **YES** |

---

## Files changed (summary)

**Created:** `HYGIENE-PASS-v1.md`

**Updated (28):**

- `registry/`: SITE-TYPE-BLOCK-MAPPING-v1, SITE-TYPE-LEGAL-MAPPING-v1, SITE-TYPE-REGISTRY-v1, SITE-TYPE-IMPLEMENTATION-RULES-v1
- `blueprints/`: BLUEPRINT-SYSTEM-v1, BLUEPRINT-CONTRACT-v1, BLUEPRINT-IMPLEMENTATION-RULES-v1, BLUEPRINT-GAPS-v1, LANDING/PROMO/CATALOG/ECOMMERCE/CORPORATE-BLUEPRINT-v1
- `block-registry/`: BLOCK-REGISTRY-GAPS-v1, BLOCK-GAPS-v1, BLOCK-REGISTRY-AUDIT-v1
- `page-architecture/`: PAGE-GAPS-v1
- Root: WEBSITE-FACTORY-FOUNDATION-v1-FREEZE, ARCHITECTURE-FOUNDATION-v1, WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1, WEBSITE-FACTORY-NEXT-PRIORITIES-v1, BRAIN-CONSISTENCY-PASS-v1

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether `_snapshots/snap-20260530-*` exists outside this clone | **UNKNOWN** — not restored; marked historical only |
| Operator schedule for BCP-006/007 resolution | **not scheduled** — optional Design Mapping charter items |
| Triumph production deploy authorization | **UNKNOWN** (unchanged) |
| Automated validation implementation | **FUTURE** — no in-repo proof |

---

*Hygiene Pass v1 — 2026-06-01. Documentation only. Canonical location: `workspaces/website-factory-reference-v1/HYGIENE-PASS-v1.md`.*
