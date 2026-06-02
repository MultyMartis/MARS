# Operational Log Format (v1)

**Status:** **documented** — standard structure for MARS survivability logs.  
**Not:** centralized logging product, log aggregator, or automated log writer.

**Log locations:**

| Type | Directory |
|------|-----------|
| Survivability | `logs/survivability/` |
| Incidents | `logs/incidents/` |
| Rollback history | `logs/rollback-history/` |
| Tool reports (optional) | `projects/mars-survivability/tools/observability/reports/` |

---

## 1. Purpose

Standardize **human-append** operational records so drift, recovery, and validation outcomes are auditable across sessions.

---

## 2. Severity model

| Severity | Use when |
|----------|----------|
| **INFO** | Routine note, successful validation, drill complete |
| **WARNING** | Drift signal, incomplete manifest, scope concern — action optional |
| **HIGH** | Scope escape, failed pre-check, restore planned — action required |
| **CRITICAL** | Incident, governance touch, halt triggered — stop work |

**Precedence for reporting:** CRITICAL > HIGH > WARNING > INFO.

---

## 3. Common header (all log types)

```markdown
# <Log Type> — <short title>

**Log id:** `<type>-YYYYMMDD-HHMMSS-<slug>`  
**Timestamp:** `YYYY-MM-DDTHH:MM:SSZ`  
**Severity:** INFO | WARNING | HIGH | CRITICAL  
**Operator:** <handle>  
**Lane:** A | B | <project>  
**Related task / chat:** <reference>

## Summary
<1–3 sentences>

## Evidence
<paths, tool outputs, snapshot ids>

## Actions taken
<what human did — not what tooling did autonomously>

## Follow-up
<next steps or none>

## SAFE UNKNOWN
<gaps — empty if none>
```

---

## 4. Incident logs (`logs/incidents/`)

**Filename:** `incident-YYYYMMDD-<slug>.md`

**Additional fields:**

| Field | Content |
|-------|---------|
| **incident class** | context-drift, scope-escape, snapshot-failure, recovery-failure, other |
| **halt triggered** | yes/no — link operational-halt-protocol |
| **quarantine path** | if moved |
| **AGENT involved** | yes/no |

---

## 5. Recovery logs (`logs/survivability/` or dedicated recovery note)

**Filename:** `recovery-YYYYMMDD-<slug>.md`

| Field | Content |
|-------|---------|
| **recovery mode** | quarantine, selective-restore, drill |
| **snapshot id** | if used |
| **rollback map id** | if JSON plan exists |

---

## 6. Rollback logs (`logs/rollback-history/`)

**Filename:** `rollback-YYYYMMDD-<slug>.md`

| Field | Content |
|-------|---------|
| **rollback map** | path to JSON or inline ordering |
| **snapshot id** | `snap-*` |
| **paths restored** | explicit list |
| **verification** | build/lint/manual check result |
| **partial rollback** | yes/no + risks |

Align with [rollback-map-schema-v1.json](../tools/observability/rollback-map-schema-v1.json).

---

## 7. Drift logs (`logs/survivability/`)

**Filename:** `drift-YYYYMMDD-<slug>.md`

| Field | Content |
|-------|---------|
| **drift source** | registry-drift-linter, manual review, diff-report |
| **drift status** | OK, DRIFT, CRITICAL_DRIFT |
| **findings** | id + message list |
| **reconciliation** | pending / done / waived |

---

## 8. Snapshot logs (`logs/survivability/`)

**Filename:** `snapshot-YYYYMMDD-<slug>.md`

| Field | Content |
|-------|---------|
| **snapshot id** | directory name |
| **integrity check** | VALID / WARNING / INVALID from checker |
| **manifest validation** | VALID / WARNING / INVALID from cross-validator |
| **retention tier** | Active / Reference / Incident-linked / Drill |

---

## 9. Validator reports (`tools/validator/reports/` or observability)

Follow [validator-report-format-v1.md](../tools/validator/validator-report-format-v1.md).

Observability tool JSON may be pasted or saved as:

`observability-report-YYYYMMDD-<tool>-<slug>.json`

---

## 10. Rules

| Rule | Detail |
|------|--------|
| Append-only | Do not rewrite historical incident/rollback entries |
| Human-authored | Tools suggest; operator writes log |
| No secrets | No tokens, credentials |
| Honesty | SAFE UNKNOWN when evidence missing |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | G4 — operational log format v1 |

---

*End of Operational Log Format v1.*
