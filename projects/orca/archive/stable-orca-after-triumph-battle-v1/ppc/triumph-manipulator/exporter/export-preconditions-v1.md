# Export Preconditions v1

**Role:** Hard gates before the exporter may run.  
**Principle:** Export is a **privileged** operation — only after validation explicitly allows it.

---

## Mandatory preconditions (all required)

Export may proceed **only if** every row below is satisfied:

| # | Precondition | Verification |
|---|--------------|--------------|
| P1 | `ValidationReport` artifact exists for this document | File present; `validated_document_id` matches document |
| P2 | `export_allowed` = **true** | From report — not inferred from `validation_status` alone |
| P3 | `blocking_errors` is **empty** | Report array length = 0 |
| P4 | Document `schema_version` supported | v1 only in foundation phase |
| P5 | Document `search_only_scope` = **true** | Root and every campaign |
| P6 | Commander template contract compatible | Template id + revision in exporter config matches [commander-template-contract-v1.md](commander-template-contract-v1.md) |
| P7 | Entity graph structurally loadable | Campaigns → groups → ads resolvable (exporter does not repair) |

If any precondition fails → **export blocked** ([export-blocking-rules-v1.md](export-blocking-rules-v1.md)).

---

## ValidationReport cross-check

| Report field | Exporter use |
|--------------|--------------|
| `validated_document_id` | Must equal `document.project_id` (or configured id field) |
| `validation_timestamp` | Logged in export manifest; stale report policy below |
| `validation_status` | Must not be `failed` or `incomplete` |
| `export_allowed` | **Primary gate** |
| `human_review_required` | Does not auto-block by default; operator policy may require sign-off |
| `warnings` | Informational; exporter does not resolve |
| `safe_unknown` | See safe_unknown policy below |

### Stale report policy (recommended)

If document file mtime **newer** than `validation_timestamp` → block export with code `STALE_VALIDATION_REPORT` until re-validation.

---

## `safe_unknown` handling

From [validation/validation-report-generation-v1.md](../validation/validation-report-generation-v1.md):

| Policy mode | Behavior |
|-------------|----------|
| **Strict (default)** | Any `safe_unknown.length` > 0 → block export even if `export_allowed` true |
| **Operator override** | Human documents clearance in project notes + sets future `export_override_safe_unknown: true` on manifest |

Exporter **does not** clear or reinterpret `safe_unknown` entries.

Topics that commonly block:

- Direct UI limit drift vs template annotations  
- Unverified geo region ID mapping  
- Unconfirmed extension row batch limits  

---

## Warnings vs export

| Situation | Export |
|-----------|--------|
| `validation_status` = `passed_with_warnings`, `export_allowed` true, no blocking errors | **Allowed** if operator accepted warns |
| `human_review_required` true | Allowed only after operator checklist (not automated) |

Exporter does **not** read warn text to change mapping.

---

## Document-level gates

| Check | Block code |
|-------|------------|
| Unsupported `schema_version` | `UNSUPPORTED_SCHEMA_VERSION` |
| `search_only_scope` false | `NON_SEARCH_SCOPE` |
| `campaign_type` ≠ search (if present) | `UNSUPPORTED_CAMPAIGN_TYPE` |
| Zero campaigns | `EMPTY_DOCUMENT` |
| Malformed JSON / schema fail | `INVALID_DOCUMENT` |

Structural repair is **out of scope** — fix document and re-validate.

---

## EX rule alignment (validation already ran)

These are validated pre-export via EX-* rules; exporter re-checks **transport-critical** items only:

| EX rule | Exporter pre-check |
|---------|-------------------|
| EX-01 | Report exists |
| EX-03 | Required source fields non-empty for rows about to be emitted |
| EX-04 | Active ads have `landing_url` |
| EX-05 | Keywords have `phrase` + `match_policy` |
| EX-06 | Warn if zero exportable ads under policy |

Exporter does **not** re-run SE/LM/CM rules.

---

## Operator checklist (manual today)

Before export:

- [ ] Latest `ValidationReport` for this `project_id`  
- [ ] `export_allowed: true`  
- [ ] No uncleared `safe_unknown` (strict mode)  
- [ ] Warnings reviewed if any  
- [ ] Template version matches [commander-template-contract-v1.md](commander-template-contract-v1.md)  
- [ ] Draft export mode chosen ([draft-export-rules-v1.md](draft-export-rules-v1.md))  

---

## Output of pre-check (future)

```yaml
export_precheck:
  status: pass | block
  block_codes: [STALE_VALIDATION_REPORT, ...]
  report_ref: validation_timestamp
  document_ref: project_id
  template_ref: triumph-manipulator-commander-template-v0
```

---

## Related

- [export-blocking-rules-v1.md](export-blocking-rules-v1.md)  
- [exporter-engine-overview-v1.md](exporter-engine-overview-v1.md)
