# ORCA — Standards Register v1

**Status:** **ACTIVE** — human-maintained index of normative ORCA standards  
**Date:** 2026-07-02  
**Not:** automated registry sync, runtime schema, or enforcement engine

**Purpose:** Single lookup for **ORCA-*** and related ORCA normative standards. Detail lives in linked standard documents — this file registers ID, status, and scope only.

**Boundary:** ORCA standards govern research, analytics, and publication. Website Factory standards govern implementation — Factory **consumes** ORCA research outputs; Factory **does not** own ORCA research publication standards.

---

## Research & publication standards (ORCA-RS)

| ID | Document | Status | Scope |
|----|----------|--------|-------|
| **ORCA-RS-001** | [standards/ORCA-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md](standards/ORCA-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md) | **ACTIVE** | Two-level research model; mandatory Executive Research Package; Publication Gate |

**Research layer overview:** [research/orca-research-layer-v0.md](research/orca-research-layer-v0.md)

---

## Reference implementations (standards evidence)

| Standard | Reference case | Path |
|----------|----------------|------|
| ORCA-RS-001 | BZPM Market Intelligence — Executive Presentation Package v2.1 RU | `projects/website-factory/execution-cases/bzpm-market-intelligence/executive-report/` |

---

## Downstream consumers

| Consumer | Relationship |
|----------|--------------|
| **Website Factory** | Uses research publications produced according to **ORCA-RS-001** — [../mars-website-factory/research-standards-v1.md](../mars-website-factory/research-standards-v1.md) · [../mars-website-factory/publication-standards-v1.md](../mars-website-factory/publication-standards-v1.md) |
| **MIG** | Upstream acquisition — feeds ORCA Level 1; does not publish Executive Research |

---

## Historical registrations (superseded)

| ID | Document | Status | Notes |
|----|----------|--------|-------|
| WF-RS-001 | [../mars-website-factory/standards/WF-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md](../mars-website-factory/standards/WF-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md) | **SUPERSEDED** | Migrated to ORCA-RS-001 — preserved for link stability |

---

## Registration rules

1. New **ORCA-*** standards append a row here before OPERATIONAL-INDEX / README citation.
2. Do not duplicate full standard text in this register — link only.
3. Reference implementations are **evidence**, not mutable standard sources.
4. Do not register Website Factory implementation standards in this file.

---

*ORCA Standards Register v1 — 2026-07-02.*
