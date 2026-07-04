# Website Factory — Knowledge Map v1

**Status:** **ACTIVE** — human-maintained map of durable Factory knowledge and reference implementations  
**Date:** 2026-07-02  
**Not:** graph database, vector index, or automated knowledge sync

**Purpose:** Orient operators to **where durable knowledge lives** and which artifacts are **registration-grade** vs working/internal.

---

## 1. Knowledge layers

| Layer | Location | Registration grade |
|-------|----------|-------------------|
| Methodology pack | `projects/mars-website-factory/` | Factory canon |
| Execution cases | `projects/website-factory/execution-cases/` | Program evidence |
| Foundry reference | `workspaces/website-factory-reference-v1/` | Registry / blueprint reference |
| Operations records | `workspaces/website-factory-operations/` | LOC-ZONE passports, FP-* |
| Research canon (foundry) | `research/foundry/rv-01`–`rv-03` | Immutable snapshots |

---

## 2. Research knowledge (two-level model)

**Standard (ORCA-owned):** [ORCA-RS-001](../orca/standards/ORCA-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md) — Website Factory **uses** research publications produced according to ORCA-RS-001.

| Level | Knowledge type | Client / knowledge registration |
|-------|----------------|--------------------------------|
| **1 — Internal** | Registry, master report, SERP, presentation pack, operator notes | **No** — working base |
| **2 — Executive** | Executive Research Package (xlsx + docx + README + sources) | **Yes** — mandatory for complete research |

---

## 3. Registered research reference implementations

| Program | Level 1 (internal) | Level 2 (executive — registration grade) | Standard |
|---------|-------------------|-------------------------------------------|----------|
| **BZPM Market Intelligence** | `projects/website-factory/execution-cases/bzpm-market-intelligence/` · Presentation Pack: `presentation-pack/` | `executive-report/` — Executive Presentation Package **v2.1 RU** | **ORCA-RS-001** (first reference) |

**BZPM related execution knowledge (non-executive):**

| Topic | Path |
|-------|------|
| Catalog redesign research | `execution-cases/bzpm-catalog-redesign/` |
| Corporate pages / roadmap | `execution-cases/bzpm-roadmap/` |

---

## 4. Standards knowledge

| Register | Path |
|----------|------|
| Factory standards (WF-*) | [website-factory-standards-register-v1.md](website-factory-standards-register-v1.md) |
| Research standards | [research-standards-v1.md](research-standards-v1.md) |
| Publication standards | [publication-standards-v1.md](publication-standards-v1.md) |
| Operational rules | [website-factory-operational-rules-v1.md](website-factory-operational-rules-v1.md) |

---

## 5. Frontend & production knowledge

| Domain | Start |
|--------|-------|
| Operator quickstart | [frontend-operator-quickstart-v1.md](frontend-operator-quickstart-v1.md) |
| Session router | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) |
| FP-0002 lessons | [operational-examples/WEBSITE-FACTORY-FP-0002-LESSONS-LEARNED-v1.md](operational-examples/WEBSITE-FACTORY-FP-0002-LESSONS-LEARNED-v1.md) |
| Cross-layer artefact audit | [website-factory-cross-layer-artefact-registry-v1.md](website-factory-cross-layer-artefact-registry-v1.md) |

---

## 6. Knowledge registration rules

1. **Research complete** → Executive Package path **must** appear in §3 (or successor table) before citing program as Factory knowledge.
2. **Do not** register Presentation Pack alone as executive knowledge.
3. **Do not** mutate reference implementation packages when registering new standards (BZPM executive-report is read-only evidence).
4. Append only — no silent workspace-only knowledge.

---

*Website Factory Knowledge Map v1 — 2026-07-02.*
