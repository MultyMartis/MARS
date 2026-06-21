# FP-0002 v2 — Pilot Page Recommendation v1

**Document type:** Pilot page recommendation (v2 re-review)  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-22  
**Prior recommendation:** `reports/wf-pr01-b-fp-0002-first-pilot-intake-and-workspace-reconciliation-v1.md` (PG-005)  
**Method:** Re-score against fresh FIG decode + v2 inventories + WF-PR01 matrix criteria

---

## 1. Recommendation (unchanged)

**RECOMMENDED: FP-0002-PG-005 — «О центре» (About)**

No better candidate found in v2 audit pass.

---

## 2. Candidate ranking (v2)

| Rank | PAGE ID | Name | Score band | Verdict |
|------|---------|------|------------|---------|
| **1** | **PG-005** | О центре | **RECOMMENDED** | Best bounded pilot |
| 2 | PG-007 | Отзывы | ACCEPTABLE | Archive-first; less corporate-landing representativeness |
| 3 | PG-008 | Статьи — хаб | ACCEPTABLE | PDF mobile naming debt |
| 4 | PG-006 | Контакты | NOT SUITABLE | ~5 sections — below WF-PR01 floor |
| 5 | PG-010 | Правовая информация | NOT SUITABLE | Too thin |
| 6 | PG-011 | 404 | NOT SUITABLE | Too thin |
| 7 | PG-004 | Услуга конечная | RISKY | Lorem placeholders — text fidelity Critical = 0 |
| 8 | PG-002–003 | Service hub/section | RISKY | 12–14 sections; placeholder density |
| 9 | PG-001 | Главная | **NOT SUITABLE** | 15 sections; SECTION-10 order; legacy REJECT body; collision debt |
| 10 | PG-009 | Статья | DEFER | 17 FIG sections; long-form + TOC — post-pilot |

---

## 3. PG-005 re-validation

| Criterion | v2 finding | Pass? |
|-----------|------------|-------|
| Full D+M sources | PDF pair + FIG frames **FOUND** | ✓ |
| Section count 5–12 (WF-PR01) | **11 logical blocks** (Block Inventory); **13/11** raw FIG top-level frames | ✓ (with frame-count note) |
| Text extractable | FIG **1971** readable TEXT nodes file-wide; About subtree walkable | ✓ (text-lock still required) |
| Assets | Embedded in FIG; standalone pack missing | ✓ with manifest pass |
| Shared block exercise | BLK-020,018,023,026,015,019 + chrome | ✓ |
| Unique block exercise | BLK-036,037,038 | ✓ |
| Legacy contamination | **None** in v2 workspace | ✓ |
| Forensic collision | Not About-specific | ✓ |
| Implementation exists | **No** About HTML in v2 | ✓ |

---

## 4. New v2 deviations (do not overturn recommendation)

| ID | Deviation | Impact on PG-005 pilot |
|----|-----------|------------------------|
| D-01 | FIG desktop/mobile **section names differ** on About (not 1:1 labels) | Discovery must pair by **content role**, not frame name |
| D-02 | Duplicate `Программа центра` frames on About desktop FIG | Y-sort + operator review |
| D-03 | Mobile About opens with `Зависимости и пристрастия` — absent as top-level on desktop About | **SAFE UNKNOWN** mapping — flag at Discovery |
| D-04 | FAQ on About desktop FIG height **366px** vs full FAQ on Home | Confirm scope — partial vs full accordion |
| D-05 | PG-009 mobile PDF now confirmed — old “Partial” risk removed from project, **not** pilot scope change |

---

## 5. Why PG-005 remains best

1. Only shortlisted page with **RECOMMENDED** matrix outcome preserved after v2 evidence.
2. Exercises **shared factory tail** without Home blast radius (15 sections, false-green history).
3. **Clean v2 workspace** — zero About implementation.
4. **Medium** complexity — forms (BLK-035 optional on About per inventory — verify: About inventory lists no BLK-035 in block map... let me check)

Actually Block Inventory for PG-005:
`001,002,005,006,007,036,037,038,020,018,022,023,026,015,019,003`

No BLK-034 FAQ or BLK-035 form on About in v1 - but FIG shows `faq` section on About desktop. Good - pilot includes FAQ partially.

5. PG-007/008 acceptable but weaker first-pilot story for corporate site factory proof.

---

## 6. Alternative considered: PG-007 Reviews

**Rejected as first pilot:** pagination + archive semantics first; less representative of marketing block reuse that dominates site. Still valid **second** slice.

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 (v2 audit pass) |
| Operator action | Confirm PG-005 at P0/P1 Discovery charter |
