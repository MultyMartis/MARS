# ORCA Semantic Decision Trace v1

**Schema ID:** `orca-semantic-decision-trace`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine schema:** [`orca-semantic-decision-trace-v1.schema.json`](orca-semantic-decision-trace-v1.schema.json)

---

## Purpose

Append-only **decision trace** links assessor outputs to a `query_id` for audit (invariants 7–8, 12–13).

---

## Top-level fields

| Field | Required | Description |
|-------|----------|-------------|
| `trace_id` | yes | Unique trace identifier |
| `query_id` | yes | Links to semantic record |
| `schema_version` | yes | Const `v1` |
| `entries` | yes | Ordered list of assessor steps |

---

## Entry fields

Each `entries[]` item:

| Field | Required | Description |
|-------|----------|-------------|
| `stage` | yes | Pipeline stage e.g. normalization, signals, intent, eligibility |
| `assessor_type` | yes | rule / model / llm / human / operator |
| `assessor_id` | yes | Pack or person identifier |
| `output` | yes | Structured output object for that stage |
| `timestamp` | yes | ISO 8601 |
| `input_evidence` | no | Evidence strings consumed |
| `confidence` | no | 0.0–1.0 |
| `rule_version` | no | If assessor_type=rule |
| `model_version` | no | If model/llm |
| `prompt_version` | no | If llm |
| `disagreements` | no | Conflicts with prior entries |
| `reviewer_action` | no | accept / reject / escalate |
| `operator_override` | no | boolean |
| `reason_for_change` | no | Required when override true |

---

## Typical stage sequence

1. `ingest` — raw phrase + provenance
2. `normalize` — normalized_query, language
3. `literal` — literal_interpretation
4. `signals` — signals array
5. `intent` — primary_intent, likely_user_goal
6. `ambiguity` — ambiguity object
7. `eligibility` — commercial_eligibility
8. `risk` — risk assessment
9. `review` — workflow_status updates
10. `adjudication` — human/operator (if needed)

---

## Linkage

Store `decision_trace_id` in semantic record `audit` object. On OPERATOR_OVERRIDE, new entry with `reason_for_change` and prior output in `audit.prior_decision`.

---

## Related documents

- [`ORCA-SEMANTIC-RECORD-SCHEMA-v1.md`](ORCA-SEMANTIC-RECORD-SCHEMA-v1.md)
- [`../contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md`](../contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md)
