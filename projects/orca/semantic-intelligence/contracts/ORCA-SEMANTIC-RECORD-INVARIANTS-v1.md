# ORCA Semantic Record Invariants v1

**Contract ID:** `orca-semantic-record-invariants`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-semantic-record-invariants-v1.json`](orca-semantic-record-invariants-v1.json)

---

## Purpose

Twenty **non-negotiable rules** for semantic records. Schema validation alone is insufficient — validators must enforce these invariants.

---

## Invariants

### Invariant 1: Topic match alone cannot support ACCEPT

**rule:** Topic match alone cannot support ACCEPT

**rationale:** Тематическое совпадение с доменом услуги не является коммерческим evidence.

**example:** «холодильник» без глагола заказа → не ACCEPT

### Invariant 2: ACCEPT requires positive commercial evidence

**rule:** ACCEPT requires positive commercial evidence

**rationale:** Нужен хотя бы один STRONG/EXPLICIT commercial signal или validated seed.

**example:** EXPLICIT PROVIDER_HIRE

### Invariant 3: Conflicting protected signal may require ABSTAIN

**rule:** Conflicting protected signal may require ABSTAIN

**rationale:** career vs provider, diy vs hire, etc.

**example:** вакансия + заказать в одной фразе

### Invariant 4: Unresolved high ambiguity cannot ACCEPT

**rule:** Unresolved high ambiguity cannot ACCEPT

**rationale:** severity HIGH/CRITICAL + unresolved mandatory types.

**example:** SHORT_HEAD_TERM «crm»

### Invariant 5: REJECT requires a reason code

**rule:** REJECT requires a reason code

**rationale:** reason_code из reject families обязателен.

**example:** CLEAR_DIY_HOW_TO

### Invariant 6: ABSTAIN requires an unresolved question or conflict

**rule:** ABSTAIN requires an unresolved question or conflict

**rationale:** unresolved_questions min 1.

**example:** PROVIDER_DIY_CONFLICT

### Invariant 7: Every decision requires provenance

**rule:** Every decision requires provenance

**rationale:** provenance_status не MISSING для final auto decision.

**example:** COMPLETE or PARTIAL documented

### Invariant 8: Every automated decision records rule/model/prompt versions

**rule:** Every automated decision records rule/model/prompt versions

**rationale:** versioning object populated.

**example:** rule_version, taxonomy_version

### Invariant 9: Service ownership cannot be final before ACCEPT

**rule:** Service ownership cannot be final before ACCEPT

**rationale:** mapping_status только NOT_STARTED или CANDIDATE_ONLY до ACCEPT.

**example:** no final service_id

### Invariant 10: Cluster or campaign fields are forbidden

**rule:** Cluster or campaign fields are forbidden

**rationale:** no cluster_id, ad_group, campaign_group.

**example:** schema not constraint

### Invariant 11: Export fields are forbidden

**rule:** Export fields are forbidden

**rationale:** no export_fields at semantic layer.

**example:** SI-16 transport only

### Invariant 12: Human override must retain prior decision

**rule:** Human override must retain prior decision

**rationale:** audit.prior_decision preserved.

**example:** OPERATOR_OVERRIDE

### Invariant 13: Superseded records remain auditable

**rule:** Superseded records remain auditable

**rationale:** SUPERSEDED not deleted.

**example:** record chain

### Invariant 14: Narrative fields cannot contain raw numeric sentinels

**rule:** Narrative fields cannot contain raw numeric sentinels

**rationale:** no 1234, 2464, 970, 272.

**example:** phrase_explanation text

### Invariant 15: Primary intent and eligibility must not be conflated

**rule:** Primary intent and eligibility must not be conflated

**rationale:** intent ≠ decision.

**example:** HIRE_SERVICE + ABSTAIN allowed

### Invariant 16: Workflow status and eligibility must not be conflated

**rule:** Workflow status and eligibility must not be conflated

**rationale:** review ≠ commercial_eligibility.

**example:** see review taxonomy

### Invariant 17: Product/module intent cannot silently map to service intent

**rule:** Product/module intent cannot silently map to service intent

**rationale:** BUY vs REQUEST_* separation.

**example:** купить лицензию ≠ внедрение

### Invariant 18: UNKNOWN cannot automatically become ACCEPT

**rule:** UNKNOWN cannot automatically become ACCEPT

**rationale:** UNKNOWN intent → no auto ACCEPT.

**example:** human or ABSTAIN

### Invariant 19: Malformed query cannot be rewritten into a new commercial query

**rule:** Malformed query cannot be rewritten into a new commercial query

**rationale:** MALFORMED stays MALFORMED.

**example:** no «исправление» запроса

### Invariant 20: ABSTAIN is a valid terminal output for automated processing

**rule:** ABSTAIN is a valid terminal output for automated processing

**rationale:** ABSTAIN is success, not error.

**example:** pipeline completes


---

## Enforcement

| Layer | Responsibility |
|-------|----------------|
| JSON Schema | Shape, enums, required fields |
| Invariant validator | Rules 1–20 |
| Human review | OPERATOR_OVERRIDE with audit |
| Fixtures | `fixtures/invalid` demonstrate violations |

---

## Related documents

- [`../schemas/ORCA-SEMANTIC-RECORD-SCHEMA-v1.md`](../schemas/ORCA-SEMANTIC-RECORD-SCHEMA-v1.md)
- [`../validation/ORCA-SEMANTIC-TAXONOMY-AND-SCHEMA-VALIDATION-v1.md`](../validation/ORCA-SEMANTIC-TAXONOMY-AND-SCHEMA-VALIDATION-v1.md)
