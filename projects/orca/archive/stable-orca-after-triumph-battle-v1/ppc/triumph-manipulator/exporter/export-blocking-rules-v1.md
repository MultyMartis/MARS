# Export Blocking Rules v1

**Role:** When the exporter **must refuse** to write a workbook, and what the operator does next.  
**Stance:** Fail closed — no partial export of a failed graph.

---

## Block categories

### A — Validation gate blocks

| Code | Condition | Operator action |
|------|-----------|-----------------|
| `MISSING_VALIDATION_REPORT` | No report file paired with document | Run validation; generate report |
| `EXPORT_NOT_ALLOWED` | `export_allowed` = false | Fix `blocking_errors`; re-validate |
| `BLOCKING_ERRORS_PRESENT` | `blocking_errors.length` > 0 | Fix listed rules; re-validate |
| `VALIDATION_FAILED` | `validation_status` = `failed` \| `incomplete` | Complete validation pass |
| `STALE_VALIDATION_REPORT` | Document newer than report timestamp | Re-validate |
| `SAFE_UNKNOWN_UNCLEARED` | `safe_unknown` non-empty (strict mode) | Confirm externally or fix rule inputs |

### B — Document blocks

| Code | Condition | Operator action |
|------|-----------|-----------------|
| `UNSUPPORTED_SCHEMA_VERSION` | `schema_version` ≠ supported set (v1) | Migrate document |
| `NON_SEARCH_SCOPE` | `search_only_scope` false | Remove non-search campaigns or split pack |
| `UNSUPPORTED_CAMPAIGN_TYPE` | Non-search `campaign_type` | Search-only pack — fix entity |
| `INVALID_DOCUMENT` | JSON parse / schema failure | Fix JSON |
| `MALFORMED_ENTITY_GRAPH` | Unresolved parents, duplicate ids | Fix ST-06 / ST-11 |
| `EMPTY_DOCUMENT` | No campaigns | Add structure |

### C — Template blocks

| Code | Condition | Operator action |
|------|-----------|-----------------|
| `TEMPLATE_NOT_FOUND` | Missing xlsx asset | Restore from [assets/direct-commander-template/](../assets/direct-commander-template/) |
| `UNSUPPORTED_TEMPLATE_REVISION` | Template version ≠ exporter config | Update exporter mapping or pin template revision |
| `TEMPLATE_CONTRACT_MISMATCH` | Required logical sections missing from template | Re-copy template; update contract doc |

### D — Transport safety blocks

| Code | Condition | Operator action |
|------|-----------|-----------------|
| `POST_NORM_LENGTH_VIOLATION` | Field exceeds limit after normalization | Fix copy; re-validate SY-* |
| `DUPLICATE_KEYWORD_ROW` | Duplicate phrase in group export set | Dedup in document |
| `ROW_EXPLOSION` | Row count guard tripped | Split groups |
| `ZERO_EXPORTABLE_ADS` | `active_only` mode and no active ads | Activate ads or change mode |

### E — Policy blocks (operator config)

| Code | Condition | Operator action |
|------|-----------|-----------------|
| `HUMAN_SIGNOFF_REQUIRED` | Policy requires sign-off when `human_review_required` | Complete review checklist |
| `DRAFT_EXPORT_NOT_ALLOWED` | Policy forbids `include_drafts` for production path | Use `active_only` |

---

## Exporter must NOT

| Action | Why |
|--------|-----|
| Auto-fix validation failures | Validation domain |
| Export with warnings auto-cleared | Human acceptance |
| Partial export of one campaign from multi-campaign doc | Unless explicit `campaign_filter` flag (future) — default block on any fatal |
| Truncate and continue | Silent truncation forbidden |

---

## Block response shape (future)

```yaml
export_result:
  status: blocked
  block_codes: [EXPORT_NOT_ALLOWED, STALE_VALIDATION_REPORT]
  message: Human-readable summary
  validation_report_ref: "2026-05-20T12:00:00Z"
  operator_actions:
    - Fix blocking_errors SE-05 on ad_s01_5ton_a1
    - Re-run validator
```

Exit code **non-zero** for CLI.

---

## Relationship to validation EX rules

| EX rule | Exporter block |
|---------|----------------|
| EX-01 | `MISSING_VALIDATION_REPORT` / `EXPORT_NOT_ALLOWED` |
| EX-03 | `INVALID_DOCUMENT` / field empty at mapping |
| EX-04 | `INVALID_DOCUMENT` (active ad no URL) |
| EX-05 | `INVALID_DOCUMENT` (keyword incomplete) |
| EX-06 | `ZERO_EXPORTABLE_ADS` (warn path) |

Validation remains authoritative; exporter blocks are **transport enforcement**, not duplicate semantic validation.

---

## Related

- [export-preconditions-v1.md](export-preconditions-v1.md)  
- [validation/validation-report-generation-v1.md](../validation/validation-report-generation-v1.md)
