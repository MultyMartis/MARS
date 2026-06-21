# ATLAS Registry Health Model v1

**Status:** **documented** — Phase 8 conceptual registry quality monitoring (normative framework).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-05  
**Parent:** [ATLAS-OPERATIONAL-MODEL-v1.md](ATLAS-OPERATIONAL-MODEL-v1.md) · [ATLAS-SERVICE-LEVEL-MODEL-v1.md](ATLAS-SERVICE-LEVEL-MODEL-v1.md) · [ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md)  
**Is not:** monitoring implementation, metrics pipeline, dashboard, alerting system, automated quality scorer.

---

## 1. Purpose

Define **how registry quality is monitored** conceptually — health dimensions, signals, severity, and stewardship response — without prescribing implementation.

**Decision (Architectural Analysis #6):**

> **Registry health** is the **assessed condition** of the canonical business reality graph and its governance queues — structural integrity, identity discipline, dispute load, and population quality — **not** system uptime or query performance.

---

## 2. Health monitoring philosophy

| Principle | Application |
|-----------|-------------|
| **Human assessment** | Stewards and Owner review health — not only automated alerts |
| **Preventive** | Health review catches drift before D1 incidents |
| **Proportional response** | Red dimension may trigger STOP — green does not imply skip review |
| **Transparent** | Health summary is shared with Owner and certification reviewers |
| **No false precision** | Qualitative red/amber/green acceptable in documentation phase |

---

## 3. Health review process (conceptual)

```text
Collect signals (manual export / future query)
        │
        ▼
Assess each dimension → red | amber | green
        │
        ▼
Written health summary + action items
        │
        ▼
Owner sign-off · population continue | pause | remediate
```

Frequency: [ATLAS-SERVICE-LEVEL-MODEL-v1.md](ATLAS-SERVICE-LEVEL-MODEL-v1.md) §6.

---

## 4. Health dimensions

### HD-01 — Duplicate pressure

| Attribute | Detail |
|-----------|--------|
| **Definition** | Risk of or presence of duplicate canonical subjects |
| **Signals** | D1 active duplicates; high homonym proposals; consumer double-keys mapping to two actives; merge backlog |
| **Green** | No D1; homonyms disambiguated; merge queue empty |
| **Amber** | Multiple D2–D4 under investigation; homonym cluster growing |
| **Red** | **D1 present** (two active same subject) — STOP-01 |
| **Response** | Duplicate review; merge workflow; halt promotions in class |

References: [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) §3, POP §4.2.

---

### HD-02 — Identity health

| Attribute | Detail |
|-----------|--------|
| **Definition** | Stable, unambiguous identity records with valid lifecycle |
| **Signals** | Orphan ids referenced by consumers; deprecated without successor; split backlog; alias collisions; placeholder id attempts |
| **Green** | All actives have attest trail (conceptual); merges resolved; no CR-10 violations |
| **Amber** | Deprecated nodes without consumer redirect note; alias disputes open |
| **Red** | Placeholder canonical ids; recycled ids; unresolved merge of legal subjects |
| **Response** | Identity governance flows; Owner for split/merge |

References: [ATLAS-IDENTITY-MODEL-v1.md](ATLAS-IDENTITY-MODEL-v1.md), [ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md).

---

### HD-03 — Orphan relationships

| Attribute | Detail |
|-----------|--------|
| **Definition** | Relationship edges whose endpoints are missing, deprecated without path, or UNKNOWN |
| **Signals** | Active edges to deprecated endpoints; proposed edges never resolved; CLIENT_OF to non-existent org |
| **Green** | All active edges have active endpoints (or documented exception) |
| **Amber** | Proposed edges waiting endpoints (EIR-R02 compliant) |
| **Red** | Active edge to invalid endpoint; conflicting OWNER edges unresolved |
| **Response** | Relationship review; defer active until endpoints; dispute if conflict |

References: [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md), POP §4.4.

---

### HD-04 — Unresolved disputes

| Attribute | Detail |
|-----------|--------|
| **Definition** | Records in **disputed** state or challenges past arbitration window |
| **Signals** | Dispute count; age of oldest dispute; consumer escalation rate |
| **Green** | Zero disputed actives; challenges resolved within SLM windows |
| **Amber** | Disputes open but within arbitration window with active steward work |
| **Red** | Dispute past SLM-D-01 window; disputed OWNER on production-critical domain |
| **Response** | Owner arbitration; subgraph promotion pause (POP-DISP-01) |

References: [ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md) §8.

---

### HD-05 — Stale proposals

| Attribute | Detail |
|-----------|--------|
| **Definition** | Proposed records or queue items beyond stewardship aging tiers |
| **Signals** | Count stale vs fresh; abandoned consumer proposals; defer without reason |
| **Green** | Queue within SLM windows; defer reasons documented |
| **Amber** | Stale tier reached — Owner notified |
| **Red** | Large stale backlog + active population pressure; STOP-03 risk |
| **Response** | Reprioritize; reject abandon batch; add steward capacity |

References: [ATLAS-SERVICE-LEVEL-MODEL-v1.md](ATLAS-SERVICE-LEVEL-MODEL-v1.md) §4.

---

### HD-06 — Population quality

| Attribute | Detail |
|-----------|--------|
| **Definition** | Wave discipline, evidence tier compliance, and boundary adherence during population |
| **Signals** | Wave skip without owner exception; attest below minimum tier; boundary rejects from same source; import without spot-check |
| **Green** | Waves follow [ATLAS-POPULATION-PRIORITIES-v1.md](ATLAS-POPULATION-PRIORITIES-v1.md); gates G1–G6 satisfied |
| **Amber** | Single consumer mapping drift; isolated tier challenge |
| **Red** | Systemic import error (STOP-06); repeated boundary violation (STOP-07); fabricated evidence (STOP-02) |
| **Response** | STOP triggers; consumer certification review |

References: [ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md) §6, [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](ATLAS-EVIDENCE-REQUIREMENTS-v1.md).

---

### HD-07 — Consumer semantic alignment (optional seventh dimension)

| Attribute | Detail |
|-----------|--------|
| **Definition** | Consumers read ATLAS MVP semantics without parallel ontology |
| **Signals** | OPS C-01-style entity demands; shadow registries; unmapped lifecycle overwrite attempts |
| **Green** | Published consumer mapping docs; certification current |
| **Amber** | Mapping doc stale; challenge rate elevated |
| **Red** | Active parallel master list; CRM clone pattern (E-26) |
| **Response** | [OPS-ATLAS-ALIGNMENT-v1.md](OPS-ATLAS-ALIGNMENT-v1.md); certification downgrade |

---

## 5. Composite health posture

| Posture | Condition | Operational effect |
|---------|-----------|-------------------|
| **Green** | All dimensions green or amber-only with action plans | Population continues |
| **Amber** | One+ amber, no red | Increased review frequency |
| **Red** | Any red dimension | Remediation required; may STOP population |

**HEALTH-01:** Red **D1 duplicate** alone is sufficient for global promotion pause.

**HEALTH-02:** Owner **must** acknowledge red summary before resuming promotions.

---

## 6. Health vs runtime operations

| Concern | Registry health | Runtime ops |
|---------|-----------------|-------------|
| Question | Is canonical graph trustworthy? | Is service available? |
| Owner | Registry Steward + Program Owner | Future implementation team |
| Phase 8 | **In scope** | **Out of scope** |

---

## 7. Health summary template (conceptual)

| Section | Content |
|---------|---------|
| Review period | Dates |
| Dimension scores | HD-01 – HD-07 red/amber/green |
| STOP triggers active | Yes/no |
| Action items | Owner + steward assignments |
| Population recommendation | Continue / pause / wave-specific hold |
| Sign-off | Owner name (when roster exists) |

---

## 8. Non-deliverables

No SQL queries, Grafana dashboards, cron jobs, or automated duplicate detectors.

---

*ATLAS Registry Health Model v1 — Phase 8 Foundation. Documentation only.*
