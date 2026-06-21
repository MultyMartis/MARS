# ATLAS Corvonero Project Relationship Register v1

**Status:** **documented** — canonical Project-family relationship roster for Corvonero tranche (**active**; attestation complete).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-21  
**Organization anchor:** ORG-0009 **Центр автоматизации «Корво Неро»**  
**Is not:** Person ↔ Project edges, EXECUTES_PPC edges.

---

## 1. Register summary

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Lifecycle **active** | **1** (REL-CORV-PJ-01) |
| Attestation | **Complete** — AT-CORV-REL-01 |

---

## 2. Relationship roster — full table

| relationship_id | source_id | target_id | relationship_type | evidence_tier | lifecycle_state | attestation | notes |
|-----------------|-----------|-----------|-------------------|---------------|-----------------|-------------|-------|
| REL-CORV-PJ-01 | PRJ-0013 Корво Неро — Яндекс Директ и посадочные страницы | ORG-0009 Центр автоматизации «Корво Неро» | **COMMISSIONED_BY** | **E0** | **active** | AT-CORV-REL-01 | Project belongs to client org |

---

## 3. Excluded register (not in population set)

| Item | Reason |
|------|--------|
| ORG-0001 → PRJ-0013 **EXECUTES** | Operator restriction — no Polygon project delivery edge |
| ORG-0003 → PRJ-0013 **EXECUTES** / **SPONSORS** | Not attested in this pass |
| PER-0001 → PRJ-0013 **CONTRIBUTES_TO** / **LEADS** | EXECUTES_PPC_FOR not in v1 taxonomy — see documentation note |
| ORG-0009 → ORG-0001 **CLIENT_OF** | **Blocked** — explicit restriction |

---

## 4. Documentation note — PPC executor

| Signal | Value | Atlas handling |
|--------|-------|----------------|
| PPC executor | Андрей как подрядчик i-SEO | **Deferred** — no **EXECUTES_PPC_FOR** type in [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) v1 |
| Candidate Person | PER-0001 Русецкий Андрей Анатольевич *(i-SEO operator)* | **Reference only** — personal edge not minted without attested Person ↔ Project family decision |

---

*ATLAS Corvonero Project Relationship Register v1 — REL-CORV-PJ-01 **active**.*
