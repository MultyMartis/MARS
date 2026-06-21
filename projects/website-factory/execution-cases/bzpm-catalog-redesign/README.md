# BZPM Catalog Redesign — Execution Case

**Case id:** `bzpm-catalog-redesign`  
**Client / org:** ORG-0005 ЗПМ (BZPM) · **Project:** PRJ-0009 Каталог-платформа bzpm.ru  
**Lane:** A (Website Factory delivery)  
**Audit environment:** https://zpm.new-site.space/  
**Production:** https://bzpm.ru/ (WEB-ZPM-01)

---

## Project overview

Human-supervised catalog UX research for BZPM industrial equipment platform. Goal: preserve audit knowledge in MARS and prevent re-auditing the same questions.

**This case is documentation-first.** No redesign, implementation, or OpenCart work is authorized by this pack.

**Critical boundary:** BZPM (ORG-0005) ≠ SIBCAR / SITE-001 (ORG-0006). OCPilot OpenCart workflows do not apply.

---

## Audit timeline

| Date | Phase | Outcome |
|------|-------|---------|
| 2026-06-08 | **W0** MARS Audit | Ecosystem map; Factory = primary; OCPilot excluded |
| 2026-06-08 | **W1A** Product Audit | PDP = single-SKU display; selection gaps documented |
| 2026-06-08 | **W1B** Category Audit | Category/series listing UX; filter/chip overlap |
| 2026-06-08 | **W1C** Buyer Decision Flow | Journey maps; product-database assessment |
| 2026-06-08 | **W1D** Competitor Intelligence | Trapeza + manufacturer benchmarks |
| 2026-06-08 | **W2** Information Density | Owner feedback triangulation; fragmentation/dup analysis |
| 2026-06-08 | **Consolidation** | Canonical artifacts registered (this folder) |
| 2026-06-08 | **W4** Redesign Architecture | Information architecture v1 (no UI) |

**Deferred:** W1E Product Taxonomy Audit — see [BZPM-DECISION-LOG-v1.md](BZPM-DECISION-LOG-v1.md)

---

## Artifact index

| Document | Purpose |
|----------|---------|
| [BZPM-AUDIT-STATE-v1.md](BZPM-AUDIT-STATE-v1.md) | Current audit state, scope, next phase |
| [BZPM-FINDINGS-REGISTER-v1.md](BZPM-FINDINGS-REGISTER-v1.md) | Master register (facts / hypotheses / validated / rejected / unknown) |
| [BZPM-REDESIGN-STRATEGY-v1.md](BZPM-REDESIGN-STRATEGY-v1.md) | Approved strategic direction (8 themes) |
| [BZPM-DECISION-LOG-v1.md](BZPM-DECISION-LOG-v1.md) | Approved and rejected decisions |
| [BZPM-REDESIGN-ARCHITECTURE-v1.md](BZPM-REDESIGN-ARCHITECTURE-v1.md) | W4 information architecture (catalog → PDP) |

---

## Current status

| Field | Value |
|-------|-------|
| **Research phase** | **COMPLETE** (W0–W2) |
| **Findings** | Preliminary — classified in findings register |
| **Strategy** | Documented v1 — not implementation |
| **Architecture (W4)** | Documented v1 — information architecture only |
| **Redesign / UI** | **Not started** |
| **W1E** | **Deferred** |

---

## Next planned phase

**W3 — Strategy Formalization & Blueprint** (documentation only)

Prerequisites:

- Operator charter for W3
- Human approval of [BZPM-REDESIGN-STRATEGY-v1.md](BZPM-REDESIGN-STRATEGY-v1.md) as baseline for IA/blueprint work

W3 will **not** include code changes unless separately chartered.

---

## Registry & cross-links

| Registry | Status |
|----------|--------|
| Execution cases | Registered in `projects/mars-website-factory/execution-cases-registry-v1.md` |
| Project registry (`project_id`) | `mars-website-factory` = strategic program — no separate BZPM row required |
| Audit registry | **SAFE UNKNOWN** — no dedicated registry in repo |
| Strategy registry | **SAFE UNKNOWN** — no dedicated registry in repo |

**ATLAS context:** `projects/atlas/population/ATLAS-WAVE3-ZPM-PROJECT-POPULATION-v1.md`

**Website Factory methodology:** `projects/mars-website-factory/OPERATIONAL-INDEX.md`

---

*BZPM Catalog Redesign — execution case entry point v1.*
