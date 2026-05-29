# Validation Report Generation v1

**Role:** How `ValidationReport` artifacts are produced, gated, and consumed.  
**Contract:** [validation-report-v1.schema.json](../schema/json/validation-report-v1.schema.json)

---

## End-to-end lifecycle

```
OrcaPpcDocument
    → Rule execution (all stages)
    → rule_results[]
    → Entity aggregation → entity_results[]
    → Severity aggregation → summary, validation_status
    → Denormalize → blocking_errors[], warnings[], safe_unknown[]
    → Export gate → export_allowed
    → Human review (mandatory for warns / sign-off)
    → Final status (operator) → launch_allowed (NEVER automatic)
```

---

## Required report fields (v1 schema)

| Field | Source |
|-------|--------|
| `schema_version` | Always `"v1"` |
| `project_id` | From document `project_id` |
| `validated_document_id` | Document id or file hash reference |
| `validation_timestamp` | ISO-8601 at run time |
| `validation_status` | Aggregated: `passed` \| `failed` \| `passed_with_warnings` \| `incomplete` |
| `summary` | Counter rollup |
| `rule_results` | Full audit trail |
| `entity_results` | Per campaign/group/ad rollup |
| `blocking_errors` | Error-severity failures |
| `warnings` | Warn-severity findings |
| `safe_unknown` | Unchecked external dependencies |
| `human_review_required` | See below |
| `export_allowed` | Export gate boolean |

Optional `meta.validator_version`, `meta.ruleset_ref` for traceability.

---

## `human_review_required`

Set **`true`** when any of:

- `validation_status` = `passed_with_warnings`  
- `safe_unknown.length` > 0  
- Any LM-06 (master fallback) warn present  
- Any SV rule warns on structure chaos  
- Document contains `status: draft` ads but operator requested export (**policy**)

Set **`false`** only when all executed rules pass with no safe_unknown — operator may still review by choice.

---

## `blocking_errors`

Population:

- Every `rule_result` with `severity` = `error` and `status` = `fail`  
- Denormalized into `{ rule_id, message, entity_ref?, suggested_fix? }`

**Effect:** `export_allowed` must be `false` while `blocking_errors` is non-empty.

Operators fix source document, re-run validation, regenerate report.

---

## `warnings`

Population:

- Every `rule_result` with `severity` = `warn` and `status` in (`warn`, `fail` if warn-level rule failed soft)

**Effect:** Export may proceed **only** if:

1. No blocking errors, and  
2. Operator explicitly accepts each warn (checklist or future `validation_override` note).

Warnings do **not** auto-clear on next run unless document changed.

---

## `safe_unknown`

Use when rule depends on external truth not in repo:

| Topic | Example |
|-------|---------|
| Direct UI limit drift | SY limits differ from template annotation |
| Geo ID resolution | Region column mapping at export |
| Moderation outcome | Ad rejected after import |

Each item: `{ topic, message, rule_id?, entity_ref? }`.

**Default gate policy:** If any `safe_unknown` and operator has not confirmed → `export_allowed` = false, `human_review_required` = true.

---

## `export_allowed`

| Condition | `export_allowed` |
|-----------|------------------|
| `blocking_errors` empty AND `validation_status` not `failed`/`incomplete` | May be `true` |
| Any blocking error | `false` |
| Strict mode: any `safe_unknown` without sign-off | `false` |
| Operator policy: warns require sign-off | `false` until sign-off |

**Exporter behavior (future):** Refuse to write `.xlsx` if `export_allowed` ≠ true. Exporter reads report + document; does not infer pass from absence of report.

---

## `launch_allowed` (semantic extension — human only)

**Not** a required field in [validation-report-v1.schema.json](../schema/json/validation-report-v1.schema.json) v1. Documented here as **operator-controlled** semantics for Phase 4+ honesty.

| Rule | Enforcement |
|------|-------------|
| **NEVER** set `launch_allowed` = true automatically by validator | Engine must not emit true without human sign-off record |
| **NEVER** tie launch to `export_allowed` alone | Export-ready ≠ launch-approved |
| Default | `launch_allowed` absent or `false` in operator checklist |
| True only when | Human confirms Direct import OK, bids set, negatives live, schedule intentional |

Recommended operator checklist before launch:

1. `export_allowed` was true at last validation  
2. Commander import succeeded without row errors  
3. Preview checked on mobile  
4. Landing URLs live and match blueprint  
5. Operator explicitly records «launch approved» in project notes  

Future optional report field `launch_allowed` in schema v1.1 — still **writable only by human** or HITL tool, never validator default true.

---

## Example generation flow (logical pseudocode)

```
report = empty ValidationReport
report.schema_version = "v1"
report.project_id = doc.project_id
report.validated_document_id = doc.project_id

for stage in [ST, SY, SE, LM, CM, SV, EX]:
  for rule in registry[stage]:
    results += execute(rule, doc)
report.rule_results = results
report.entity_results = rollup_entities(results)
report.summary = count(results)
report.blocking_errors = filter_errors(results)
report.warnings = filter_warnings(results)
report.safe_unknown = filter_unknown(results)
report.validation_status = derive_status(report.summary)
report.human_review_required = derive_review(report)
report.export_allowed = gate(report)
# launch_allowed: NOT SET by engine
write_json(report)
```

---

## Consumption paths

| Consumer | Uses |
|----------|------|
| Human operator | `blocking_errors`, `warnings` first |
| Future CLI | Exit code 1 if `export_allowed` false |
| Future exporter | Hard stop if `export_allowed` false |
| CI fixture tests | Compare golden reports for draft instances |

---

## Re-validation

After any document edit:

- Generate **new** `validation_timestamp`  
- Replace prior report for that `validated_document_id` in operator workflow (no merge of stale pass)

---

## Related

- [rule-execution-flow-v1.md](rule-execution-flow-v1.md)  
- [validation-engine-overview-v1.md](validation-engine-overview-v1.md)  
- [schema/validation-schema-v1.md](../schema/validation-schema-v1.md)
