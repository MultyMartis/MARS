# Agent input contract — template (governance)

**Instructions:** Copy per **agent**, **specialist pack**, or **stable workflow slice**. Fill every section; use **SAFE UNKNOWN** only where evidence is genuinely missing **and** §SAFE UNKNOWN RESPONSE explains the stop/escalation behavior. Link from the [agent card](../agents/agent-card-template.md) **`inputs`** / **`outputs`** fields when detail exceeds card length.

**Governance only:** not a runtime payload, not agent-to-agent messaging.

---

## Metadata

| Field | Value |
|-------|--------|
| **contract_id** | <!-- e.g. agent-input-contract:gulp_frontend_agent --> |
| **agent_or_slice_name** | <!-- registry id or workflow slice --> |
| **version** | <!-- v0, v1, … --> |
| **owner** | <!-- human / role --> |
| **last_reviewed** | <!-- date --> |

---

## REQUIRED INPUTS

<!-- List each required input with: name, format/location, why required. -->

| Input | Description | Validation |
|-------|-------------|------------|
| | | |

---

## OPTIONAL INPUTS

<!-- Absence must not be silently invented. -->

| Input | Description | If absent |
|-------|-------------|-----------|
| | | |

---

## FORBIDDEN INPUTS

<!-- Sources or inputs that must NOT drive behavior. -->

| Input / source | Why forbidden | If encountered |
|----------------|---------------|----------------|
| | | |

---

## OUTPUTS

<!-- Named artifacts, paths, registry updates, REPORT sections. -->

| Output | Description | Consumer |
|--------|-------------|----------|
| | | |

---

## INPUT VALIDATION

**Pre-flight:** Before implementation execution, confirm:

| Check | Pass criteria |
|-------|----------------|
| | |

**INPUT CHECK summary (example):**

```text
✓ …
✗ …
STATUS: SAFE UNKNOWN | PROCEED | QUARANTINE
```

---

## SAFE UNKNOWN RESPONSE

When required inputs are missing, invalid, or contradictory:

1. **Stop** — do not proceed as “complete.”  
2. **Report** — list gaps and conflicts explicitly (REPORT / checklist / contract update).  
3. **Confidence** — state reduced certainty; no implied freeze/production readiness.  
4. **Signals** — if using task contract vocabulary: e.g. **UNKNOWN**, **SAFE UNKNOWN**, **STRUCTURE CHANGE**, **NEED HUMAN APPROVAL** per [../governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md).

---

## QUARANTINE CONDITIONS

Output MUST be treated as non-canonical / quarantined when:

<!-- e.g. missing semantic map; mixed design generations; handoff drift; failed G5 semantic gate. -->

| Condition | Label / handling |
|-----------|-------------------|
| | |

---

## Changelog

| Date | Change |
|------|--------|
| | |
