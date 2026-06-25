# FP-0002 v4 — Container Width Override v1

**Document type:** Operator authority override register  
**Date:** 2026-06-22  
**Scope:** FP-0002 v4 only (`workspaces/fp-0002-shpigovsky-v4/`)  
**Status:** **LOCKED**

---

## Operator decision

| Field | Value |
|-------|-------|
| **NEW canonical container max-width** | **1220px** |
| **Authority level** | Operator decision — supersedes all prior FP-0002 container values for v4 |
| **Effective** | 2026-06-22 |

---

## Override register

| # | OLD VALUE | SOURCE | NEW VALUE | RATIONALE |
|---|-----------|--------|-----------|-----------|
| O-01 | `1170px` | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md` §3.1, PD-02 (Olga 2026-06-13) | **1220px** | Operator v4 override — legacy production standards container width superseded for v4 workspace only |
| O-02 | `1170px` | `reports/FP-0002-v3-EXECUTION-CHARTER-v1.md` §Engineering law | **1220px** | v3 charter container rule overridden for v4 clean-room |
| O-03 | `1170px` | `reports/FP-0002-v2-FOUNDATION-TOKENS-v1.md` — `$container-max` | **1220px** | v2 token report is reference-only for v4; not copied into v4 SCSS |
| O-04 | `1170px` | `reports/WF-FRONTEND-FOUNDATION-CONTRACT-v1.md` §2 Container tokens | **1220px** | Factory contract 1170px does not bind v4 after this override |
| O-05 | `1170px` | `workspaces/fp-0002-shpigovsky-v4/reports/FP-0002-v4-HEADER-SCSS-MEASUREMENT-v1.md` §Page / container | **1220px** (foundation) | Measurement report recorded pre-override header phase; header SCSS not redesigned in this task |
| O-06 | `1170px` | `workspaces/fp-0002-shpigovsky-v4/src/scss/layout/_header.scss` — `$header-container-max` | **1220px** (foundation only) | Header inner track still 1170px until separate header geometry task; recorded in QA header validation |
| O-07 | `1140–1170px` | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-NUMERIC-DESIGN-RULES-v1.md` — content width range | **1220px** | PDF-derived range superseded by operator lock for v4 implementation |
| O-08 | `1170px` (FIG frame width) | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-FIG-FULL-PAGE-DISCOVERY-v1.md` — GROUP frames 1170×* | **1220px** | FIG geometry remains secondary; operator container authority wins for v4 CSS |
| O-09 | `1171px` | `FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md` — symmetric proposal note | **1220px** | Legacy normalization candidate not adopted |
| O-10 | `1200px` | `workspaces/website-factory-reference-v1/src/scss/foundations/_tokens.scss` | **1220px** | Legacy reference starter — not v4 authority |
| O-11 | `1200px` | `workspaces/_template-client-v1/src/scss/foundations/_tokens.scss` | **1220px** | Template client starter — not v4 authority |

---

## v4 foundation lock

| Token / selector | Value | File |
|------------------|-------|------|
| `$container-max` | **1220px** | `workspaces/fp-0002-shpigovsky-v4/src/scss/abstracts/_variables.scss` |
| `.container` `max-width` | **1220px** | `workspaces/fp-0002-shpigovsky-v4/src/scss/layout/_container.scss` |
| Desktop padding-inline | **40px** | unchanged — prior v3 / PD-13 |
| Mobile padding-inline | **20px** | unchanged — prior v3 / PD-13 |

---

## Scope boundaries

| In scope | Out of scope (this task) |
|----------|--------------------------|
| Register override | Hero implementation |
| v4 foundation `.container` | Footer implementation |
| Header validation record only | Header geometry redesign |
| | Page content changes |
| | Retroactive edits to v1/v2/v3 workspaces |
| | Production Standards v3 document rewrite (historical record preserved) |

---

## Lock statement

**FP-0002 v4 container max-width = 1220px** — active foundation authority as of 2026-06-22.

Prior values (`1170`, `1171`, `1200`, PDF range `1140–1170`, legacy audits, legacy frontend workspaces, legacy production standards references) remain **historical** outside v4 unless explicitly re-opened by operator charter.

**CONTAINER OVERRIDE REGISTERED:** YES
