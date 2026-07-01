# REPORT — FP-0002 V8 Phase 07C-A Excel Demo Reconciliation v1

**Date:** 2026-07-01  
**Phase:** 07C-A — Excel-driven static client demo scope reconciliation  
**Branch:** `mars/canonical-post-recovery`  
**HEAD:** `8612d8f6732352708c787c2c610837018ae3e1a8`  
**Verdict:** **PASS** — reconciliation complete; operator decision gate pending

---

## Authority

| Authority | Value |
|-----------|-------|
| Documentation checkpoint | `8612d8f6732352708c787c2c610837018ae3e1a8` |
| Frontend baseline commit | `eb47ebb4066252373e02d9e1095403d0ce6b6b22` |
| Baseline tag | `fp-0002-v8-operator-approved-frontend-stable-01` |
| Excel SHA-256 | `64741FDDBD61199D6B3D80E8770576DAE86C374099C6AFEC292F9BD744512696` |
| Evidence root | `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\phase-07c-a-excel-demo-reconciliation\` |

**Note:** Tag `^{commit}` resolves to `eb47ebb` (annotated tag object is `3a9e974`).

---

## Preflight

| Check | Result |
|-------|--------|
| Drive `X:` | PASS |
| Volume `AI WS` | PASS |
| Repository `X:\AI MARS` | PASS |
| Branch | `mars/canonical-post-recovery` |
| HEAD descends from doc checkpoint | PASS |
| V8 workspace | PASS |
| FP-0002 operations root | PASS |
| Excel authority hash | PASS |
| Product source unchanged | **NO_PRODUCT_SOURCE_CHANGE** |

---

## Excel

| Field | Value |
|-------|-------|
| Path | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/02_CONTENT/Предварит структура и спрос.xlsx` |
| Size | 14 102 bytes |
| Modified | 2026-06-13 03:34:52 |
| Worksheets | `Структура` (visible), `Спрос набросок` (visible) |
| Normalized entities | **52** |
| Page-like entities | **42** |
| Non-page / alias rows | **10** |

---

## Current V8 (verified from source)

**Implemented pages:** 10

| # | Page | Production route |
|---|------|------------------|
| 1 | Home | `/` |
| 2 | O-Centre | `/o-centre/` |
| 3 | Contacts | `/kontakty/` |
| 4 | Reviews | `/otzyvy/` |
| 5 | Blog archive | `/blog/` |
| 6 | Blog Article | `/blog/nazvanie-stati/` |
| 7 | Services hub (legacy) | `/uslugi.html` preview only |
| 8 | Services hub v2 | `/uslugi/` canonical |
| 9 | Service subdivision | `/uslugi/zavisimosti/` |
| 10 | Service leaf | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` |

**Template families documented:** 12

---

## Reconciliation disposition totals

| Disposition | Count |
|-------------|------:|
| IMPLEMENTED_DIRECT | 9 |
| IMPLEMENTED_TEMPLATE_REUSE | 19 |
| IMPLEMENTED_PLACEHOLDER_CONTENT | 0 |
| NEEDS_STATIC_ASSEMBLY | 0 |
| DEFERRED_NOT_IN_DEMO | 11 |
| DUPLICATE_OR_ALIAS | 10 |
| NON_PAGE_ROW | 0 |
| UNKNOWN_OPERATOR_DECISION | 3 |

---

## Demo 1 scope recommendation (curated)

| Group | Excel count | Recommended Demo 1 treatment |
|-------|------------:|------------------------------|
| INCLUDE_DIRECT | 9 | All 9 — already implemented |
| INCLUDE_BY_TEMPLATE_REUSE | 19 | **Curate ~8–12** — O-centre children (5), key L2 sections (2–3), 1 exemplar L3 leaf per section; defer bulk duplication |
| INCLUDE_WITH_PLACEHOLDER_CONTENT | 3 | Operator gate — genotyping, specialists hub, legal hub |
| DEFER | 11 | L4 leaves, specialist profiles, reserved Excel slots |

**Proposed Demo 1 page count (if recommendations accepted):** ~17–21 pages (9 direct + 8–12 assembled).

---

## Routes

| Metric | Value |
|--------|------:|
| Proposed routes (page-like) | 42 |
| Route conflicts | 0 |
| Aliases / duplicates | 10 (incl. 2 blog article duplicates on same slug) |
| Unresolved operator routes | 3 |

---

## Content / design gaps

| Class | Count (page-like) |
|-------|------------------:|
| Content ready (direct) | 9 |
| Placeholder required (template reuse) | 19 |
| Content missing (deferred) | 11 |
| Approved V8 design | 9 |
| Approved V8 template design | 19 |
| No design authority | 3 (specialists, legal) |

---

## Operator gate

Decisions required before Phase 07C-B:

| ID | Topic | Recommended default |
|----|-------|---------------------|
| D07C-001 | Service leaf breadth in Demo 1 | One exemplar per L2 section |
| D07C-002 | Genotyping page | Include with placeholder |
| D07C-003 | L4 sub-leaves | Defer |
| D07C-004 | Specialists hub | Defer |
| D07C-005 | Legal hub vs footer slugs | Footer slugs canonical for demo |
| D07C-006 | Placeholder copy permission | Approved with QA label |
| D07C-007 | Defer profiles + L4 | Defer |

**Gate document:** `decision-gate/FP-0002-STATIC-CLIENT-DEMO-1-OPERATOR-DECISION-GATE-v1.md` (Storage)

---

## Evidence

| Artifact | SHA-256 |
|----------|---------|
| Pre-reconciliation snapshot ZIP | `EAE3D42F4A3ACF9370B204C631256A6BD34C188C9073D845F2D41BA6D128E031` |
| Reconciliation pack ZIP | `C743E6CD200A87C5BF4DFD104FF5C974FFD2ADECB1C6E080D693D0154E915C1E` |

---

## Protected areas

| Area | Status |
|------|--------|
| Excel workbook | Unchanged |
| V8 product source | Unchanged |
| Approved baseline | Unchanged |
| Storage evidence | Not committed |
| Static demo assembly | Not started |
| WordPress | Not started |

---

## Next status

`FP0002_V8_PHASE_07C_A_EXCEL_DEMO_RECONCILIATION_COMPLETE_PENDING_OPERATOR_SCOPE_DECISIONS`

Phase **07C-B** blocked until operator records decisions **D07C-001** through **D07C-007**.
