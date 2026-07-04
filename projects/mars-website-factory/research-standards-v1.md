# Website Factory — Research Standards v1

**Status:** **ACTIVE** — research methodology standards for Website Factory execution-case programs  
**Date:** 2026-07-02  
**Not:** research automation, SERP engine, or competitor crawler

---

## 1. Scope

Research standards govern **how Website Factory collects, structures, and closes** market, competitor, forensic, and UX intelligence work — **documentation and human-operated discipline only**.

**Distinct from:**

| Lane | Document | Role |
|------|----------|------|
| Foundry Research Canon | [rv-01-production-vocabulary.md](../../research/foundry/rv-01-production-vocabulary.md) et al. | Immutable foundry snapshots — upstream of Registry |
| MIG acquisition | `projects/mig/` | External groundtruth acquisition — separate program |
| ORCA semantics | `projects/orca/` | PPC interpretation lane |

---

## 2. Two-level model (normative)

| Level | Name | Role | Final deliverable? |
|-------|------|------|-------------------|
| **1** | Internal Research | Registry, master reports, SERP, evidence, working Excel, operator notes | **No** |
| **2** | Executive Research Package | Client/executive presentation + conclusions | **Yes — mandatory for completion** |

**Normative standard (ORCA-owned):** [../orca/standards/ORCA-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md](../orca/standards/ORCA-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md)

Website Factory **consumes** ORCA research publications — Factory **does not** own Executive Research Publication. From 2026-07-02, **research is not complete** for Factory consumption without Level 2 publication per **ORCA-RS-001**.

---

## 3. Active research standards

| ID | Standard | Publication Gate |
|----|----------|------------------|
| **ORCA-RS-001** | [Executive Research Publication Standard](../orca/standards/ORCA-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md) (ORCA-owned) | Executive xlsx + Word + README + sources (+ generator if applicable) |

---

## 4. Internal research artifacts (Level 1 — non-exhaustive)

Allowed and expected during active research:

- Registry markdown (competitor, findings, attribute inventories)
- Master Report
- Operator Insights
- SERP snapshots and leader lists
- Presentation Pack working Excel (operational layer)
- Screenshots and forensic captures
- Wave reports and decision logs

Level 1 artifacts **feed** Executive Package generation; they **do not** satisfy completion alone.

---

## 5. Completion semantics

| State | Meaning |
|-------|---------|
| **In progress** | Level 1 active; Level 2 not published |
| **Internal complete** | Level 1 frozen or approved — **still not Factory-complete** |
| **Research complete** | ORCA-RS-001 Publication Gate passed (ORCA publishes; Factory consumes) |
| **Knowledge registered** | Executive Package path recorded in [website-factory-knowledge-map-v1.md](website-factory-knowledge-map-v1.md) |

---

## 6. Reference implementation

**BZPM Market Intelligence** — first **ORCA-RS-001** reference implementation.

| Layer | Path |
|-------|------|
| Level 1 authority | `projects/website-factory/execution-cases/bzpm-market-intelligence/` |
| Presentation Pack (operational) | `.../presentation-pack/` |
| **Level 2 Executive Package** | `.../executive-report/` |

**Do not modify** BZPM Registry or Executive Package when applying this standard to new programs.

---

## 7. Related documents

- [publication-standards-v1.md](publication-standards-v1.md)
- [website-factory-standards-register-v1.md](website-factory-standards-register-v1.md)
- [website-factory-operational-rules-v1.md](website-factory-operational-rules-v1.md)
- [execution-cases-registry-v1.md](execution-cases-registry-v1.md)

---

*Research Standards v1 — 2026-07-02.*
