# REPORT — OPS Operational Data Model v1

**Report type:** Phase 2 foundation pass (documentation only)  
**Program:** OPS — Business Operations Domain  
**Date:** 2026-06-04  
**Pass charter:** OPS Phase 2 — Operational Data Model Foundation — no runtime, no automation, no registry changes, no ATLAS changes

---

## 1. Summary

Defined the **operational data model** for OPS: ATLAS vs OPS ownership separation, **OpsCase** as primary container, approval gates, deadline/reminder/escalation constructs, and **controlled status vocabularies** for cases, documents, reports, communications, and escalations.

**No** databases, storage engines, runtime, agents, automations, registry edits, or ATLAS modifications were performed.

---

## 2. Files created

| Path | Created | Purpose |
|------|---------|---------|
| `projects/ops/foundation/OPS-OPERATIONAL-DATA-MODEL-v1.md` | Yes | Master model: ATLAS entities vs OPS records, reference fields, anti-duplication ODM-01–06, relationship diagram |
| `projects/ops/foundation/OPS-CASE-MODEL-v1.md` | Yes | OpsCase definition, six case types, lifecycle, required/suggested fields, workflow mapping |
| `projects/ops/foundation/OPS-APPROVAL-MODEL-v1.md` | Yes | ApprovalRequest states, transitions, human authority HA-01–06, mandatory gates before send/closure |
| `projects/ops/foundation/OPS-DEADLINE-MODEL-v1.md` | Yes | Deadline, Reminder, escalation triggers, categories, Executive Assistant touchpoints |
| `projects/ops/foundation/OPS-STATUS-MODEL-v1.md` | Yes | Controlled vocabularies for case, document, report, communication, escalation, deadline, task |
| `projects/ops/reports/REPORT-ops-operational-data-model-v1.md` | Yes | This Phase 2 pass record |

**Total new:** 6 files

---

## 3. Files updated

| Path | Updated | Purpose |
|------|---------|---------|
| `projects/ops/OPERATIONAL-INDEX.md` | Yes | Phase 2 Foundation section, Core Run links, Foundation Documents table, Reports table |

---

## 4. Key architectural decisions

| Decision | Rationale |
|----------|-----------|
| **OpsCase** is the primary operational object | Unifies reporting, documents, follow-ups, escalations under one lifecycle |
| OPS stores **ATLAS references**, not canonical business fields | Preserves ATLAS as Business Reality Registry; OPS stays operational SoT only |
| Nine OPS record types named in master model | Shared vocabulary before workflow-specific docs multiply |
| Approval states separate from case/report states | Prevents ambiguous `APPROVED` on cases; four-eyes gates explicit |
| Small controlled status vocabularies | Reduces per-workflow status drift (ST-01) |
| Mandatory approval before send/closure classes | Aligns with Foundation boundaries and monthly workflow stage 7 |
| Escalation as human-triggered, not automated | No SLA engine or calendar product claimed |
| Conceptual YAML example in case model | Illustrative only — not a claimed file format |
| Phase 2 does **not** register OPS or modify ATLAS/registry | Charter compliance |

---

## 5. Risks discovered

| Risk | Severity | Notes |
|------|----------|-------|
| Status overlap confusion (case vs report vs approval) | Medium | Mitigated by ST-01 and cross-links; operators need training |
| Duplicate cases for same client+period | Medium | ODM-06 requires human merge — no dedupe engine |
| `invoice_trigger` approval may imply OPS financial authority | Medium | Documented as accounting handoff only — HA-05 |
| ATLAS ids often missing in practice | Medium | `attestation_mode` and SAFE UNKNOWN — same as Foundation v1 |
| Report status vs workflow stage names | Low | Two naming layers — mapping table in status model |
| Future persistence may invent parallel enums | Low | Engineering charter should import this vocabulary verbatim |

**No blocking issues** for Phase 2 documentation pass.

---

## 6. Recommendations

1. **Workflow alignment pass** — Add a short “OpsCase mapping” subsection to `OPS-MONTHLY-REPORTING-WORKFLOW-v1.md` in a future doc-only pass (optional; not required for Phase 2 charter).
2. **Human pilot** — Run one monthly cycle labeling artifacts with OpsCase id and report statuses; capture gaps in `projects/ops/reports/`.
3. **Document Operations workflow** — When chartered, use `DOCUMENT_CLOSING` case type and document status vocabulary from day one.
4. **ATLAS consumer contract** — When ATLAS read surface exists, map `atlas_entity_type` values to ATLAS taxonomy ids.
5. **Governance registration** — OPS registry row remains separate pass; Phase 2 does not change that stance.

---

## 7. Verification checklist

| Check | Result |
|-------|--------|
| No runtime paths created for OPS | **PASS** |
| No changes to `registry/project-registry.md` | **PASS** |
| No changes to `governance/ecosystem-topology-index.md` | **PASS** |
| No changes under `projects/atlas/` | **PASS** |
| All six required paths created | **PASS** |
| OPERATIONAL-INDEX updated with Phase 2 | **PASS** |
| No database/schema/automation claims | **PASS** |

---

*OPS Operational Data Model v1 · Phase 2 foundation pass record.*
