# Website Factory — Publication Standards v1

**Status:** **ACTIVE** — publication and delivery-readiness standards for Website Factory artifacts  
**Date:** 2026-07-02  
**Not:** CMS publish API, CDN automation, or package registry upload engine

---

## 1. Purpose

Define **when an artifact or research program may be treated as published** for downstream consumers — client, knowledge map, freeze, and delivery lanes.

Publication standards split into:

1. **General artifact publication** (workflow artifacts, blueprints, handoffs)
2. **Research executive publication** (mandatory research completion gate)

---

## 2. General artifact publication

**Normative baseline:** [artifact-publication-semantics-v0.md](artifact-publication-semantics-v0.md)

Publication classes: draft → review → approved → frozen → revoked / deprecated / archived.

HITL-anchored — **no** autonomous approval.

---

## 3. Research executive publication (ORCA-RS-001)

**Normative standard (ORCA-owned):** [../orca/standards/ORCA-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md](../orca/standards/ORCA-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md)

Website Factory **uses** research publications produced according to ORCA-RS-001. Factory **does not** own Executive Research Publication.

### Publication Gate (research)

Research **cannot** reach complete publication until present:

| Deliverable | Required |
|-------------|----------|
| Executive Research.xlsx (or project equivalent) | Yes |
| Research Conclusions.docx (or project equivalent) | Yes |
| README.md | Yes |
| sources.md | Yes |
| generator.py (if generatable) | Conditional |

### Post-gate actions

Only after gate pass:

- Research Freeze
- Stable Publication
- Client Delivery
- Knowledge Registration

---

## 4. Layer distinction (research)

| Output | Publication class | Client final? |
|--------|-------------------|---------------|
| Internal Registry / Master Report | Internal / review | No |
| Presentation Pack (working Excel) | Operational packaging | No |
| **Executive Research Package** | **Stable executive publication** | **Yes** |

---

## 5. Traceability requirement

All published research conclusions **must** be traceable via `sources.md` to Level 1 authority documents.

Regeneratable packages **must** document reproduction steps in package `README.md`.

---

## 6. Visual publication standard (executive research)

Executive research Office outputs target **McKinsey / BCG / PwC / Deloitte / KPMG** presentation discipline:

- clarity and structure over decoration
- KPI and chart-first Excel
- narrative Word complementary to Excel
- no registry dump as “client deck”

Detail: ORCA-RS-001 §7.

---

## 7. Reference implementation

BZPM Market Intelligence — Executive Presentation Package v2.1 RU  
`projects/website-factory/execution-cases/bzpm-market-intelligence/executive-report/`

---

## 8. Related documents

- [research-standards-v1.md](research-standards-v1.md)
- [website-factory-standards-register-v1.md](website-factory-standards-register-v1.md)
- [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md)
- [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md)

---

*Publication Standards v1 — 2026-07-02.*
