# MARS Website Factory - Meta-Governance Drift Taxonomy

**Status:** **documented** - drift vocabulary for Website Factory governance architecture integrity only.  
**Not:** automated drift detection, governance scoring, runtime enforcement, universal taxonomy, or proof of coherence.

**Parent governance:** [meta-governance-integrity.md](meta-governance-integrity.md).  
**Architecture model:** [governance-architecture-model.md](governance-architecture-model.md).  
**Forge checklist:** [`../../agents/mars-forge/meta-governance-checklist.md`](../../agents/mars-forge/meta-governance-checklist.md).

---

## 1. Purpose

This taxonomy names drift inside governance itself: conflicts, overlaps, duplicate concepts, topology erosion, contradiction accumulation, and architecture collapse.

It helps operators report governance architecture risk without claiming automated enforcement.

---

## 2. Drift Patterns

| Drift pattern | Definition | Typical symptom | Response |
|---------------|------------|-----------------|----------|
| **Governance-layer conflict** | Two governance layers issue incompatible instructions or authority claims. | One layer says escalate while another implies continuation. | Name conflict, identify owner, route through contradiction handling. |
| **Overlapping governance domains** | Two layers govern the same concern without a clear distinction in evidence, scope, or report role. | Similar checklist items appear under different names. | Clarify boundary, merge reference, or mark one layer as adjacent. |
| **Contradictory methodology** | Methods assume incompatible sequencing, evidence standards, severity treatment, or escalation behavior. | A process can be both mandatory and optional depending on which doc is read. | Record `META-GOVERNANCE FINDINGS`; escalate if authority is material. |
| **Governance fragmentation** | Related governance concepts are split across disconnected docs, checklists, and reports. | Operators cannot find the current source of truth. | Add minimal cross-link, index entry, or lineage note. |
| **Duplicated governance concepts** | Same concept is recreated in different wording without distinct value. | Drift labels multiply while evidence stays identical. | Deduplicate vocabulary or state distinct ownership. |
| **Governance graph instability** | Cross-links, companion docs, checklists, and report blocks stop forming a navigable graph. | README, OPERATIONAL-INDEX, Forge, and governance docs disagree on entry points. | Repair canonical entry links and checklist/report references. |
| **Meta-governance erosion** | Governance changes proceed without checking coherence, boundaries, topology, or contradiction survivability. | New layers appear without architecture placement. | Run meta-governance checklist before closure. |
| **Architectural incoherence** | The governance system no longer reads as an architecture. | Operators see a list of controls but cannot understand relationships. | Use governance architecture model to restore topology. |
| **Governance sprawl** | Governance expands by volume rather than by structured value. | More layers, more report blocks, and more checklists reduce clarity. | Use governance minimalism, prioritization, and meta-governance together. |
| **Cross-layer ambiguity** | It is unclear which layer owns a decision or finding. | Same issue could be reported under three findings blocks. | Define owner, adjacent layers, and report destination. |
| **Governance-lineage confusion** | A layer's origin, rationale, companion model, checklist, or report block cannot be traced. | New operators cannot tell why the rule exists. | Record lineage or SAFE UNKNOWN; use organizational memory and governance evolution. |
| **Contradiction accumulation** | Contradictions are repeatedly tolerated without routing or resolution. | Reports disclose conflicts but no boundary or escalation path changes. | Classify, prioritize, escalate, or refine methodology. |
| **Governance architecture collapse** | Governance becomes too contradictory, fragmented, duplicated, or unreadable to operate safely. | More governance reduces trust, findability, and decision clarity. | Stop expansion; run architecture survivability review and HITL if needed. |

---

## 3. Severity Guidance

| Severity | Meaning |
|----------|---------|
| **Informational** | A boundary or link could be clearer, but operation remains understandable. |
| **Minor** | Duplication or ambiguity adds noise but does not affect freeze, escalation, source authority, or report trust. |
| **Operational** | Governance confusion can affect workflow, QA depth, report readability, or next action. |
| **High** | Contradiction or topology instability can affect source authority, freeze confidence, HITL boundary, or cross-layer trust. |
| **Critical** | Governance architecture is too contradictory or fragmented to support safe continuation without human review. |

Severity should be weighted by consequence, not by how many docs are affected.

---

## 4. Drift Families

### Boundary Drift

- governance-layer conflict;
- overlapping governance domains;
- cross-layer ambiguity;
- duplicated governance concepts.

Boundary drift weakens ownership and report readability.

### Methodology Drift

- contradictory methodology;
- contradiction accumulation;
- methodology duplication;
- architecture-blind evolution.

Methodology drift weakens operational trust.

### Topology Drift

- governance fragmentation;
- governance graph instability;
- governance-lineage confusion;
- architectural incoherence.

Topology drift weakens navigation and continuity.

### Complexity Drift

- governance sprawl;
- uncontrolled layer proliferation;
- governance architecture collapse.

Complexity drift weakens survivability through excessive weight.

### Meta-Governance Drift

- meta-governance erosion;
- architecture survivability loss;
- governance continuity break.

Meta-governance drift means the system is no longer governing its own growth.

---

## 5. Forbidden Interpretations

Do not treat this taxonomy as:

- automated architecture validation;
- a governance scoring model;
- a reason to create more layers by default;
- a universal governance architecture;
- a replacement for governance minimalism, prioritization, adaptive governance, or human escalation;
- proof that the current governance system is perfectly coherent.

---

## 6. Reporting Use

Use this taxonomy in `META-GOVERNANCE FINDINGS`:

```text
Meta-governance drift taxonomy:
- Pattern:
- Severity:
- Affected layers:
- Boundary / methodology / topology / complexity impact:
- Contradiction handling:
- Proposed action:
```

Proposed actions should use operational language: clarify, cross-link, merge, split, prioritize, scale depth, escalate, quarantine, deprecate, preserve, or SAFE UNKNOWN.

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- the affected governance layers cannot be identified;
- layer ownership is unclear;
- contradiction severity is unknown;
- lineage or rationale is missing;
- topology placement is unclear;
- the correct response could be merge, split, clarify, or deprecate but evidence is insufficient;
- architecture survivability cannot be assessed.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Meta-Governance Drift Taxonomy - governance-layer conflict, overlapping domains, contradictory methodology, fragmentation, duplicated concepts, graph instability, sprawl, contradiction accumulation, and architecture collapse; documentation only. |
