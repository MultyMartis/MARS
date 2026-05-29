# Sample run — ORCA Validation CLI Hardening v0.1

## Example command

From `tools/validation-cli/`:

```bash
npm install
node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json
```

Deterministic golden comparison:

```powershell
$env:ORCA_VALIDATOR_FIXED_TIMESTAMP="2026-05-20T12:00:00.000Z"
node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json
fc /b output\validation-report.output.json fixtures\validation-report.triumph-s-tier.expected.json
```

---

## Fail example (S-tier draft)

**Command:** `node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json`

**Console:**

```
--- ORCA Validation CLI Hardening v0.1 ---
Project:      triumph-manipulator-krd-search-s-tier-draft
Status:       failed
Export OK:    false
Report schema: valid
Human review: true
Launch:       NOT SET (human-only; export_allowed ≠ launch approval)
Summary:      88 pass, 0 warn, 1 fail

Blocking errors:
  [SE-05] Primary keyword phrase not detected in headline_1: "манипулятор безнал краснодар".

Report written: .../output/validation-report.output.json
```

| Item | Value |
|------|--------|
| **Exit code** | `1` |
| **Input schema** | valid |
| **Report schema** | valid |
| **export_allowed** | `false` |
| **launch_allowed** | not emitted (`meta.launch_allowed: null`) |

---

## Success example (conceptual)

When all blocking rules pass and both schemas validate:

```
Status:       passed
Export OK:    true
Report schema: valid
Summary:      N pass, 0 warn, 0 fail
```

| Item | Value |
|------|--------|
| **Exit code** | `0` |
| **export_allowed** | `true` |
| **human_review_required** | may still be `true` if warnings or policy |

Operator must still complete human review before Commander import — **not** launch approval.

---

## Exit code reference

| Code | Condition |
|------|-----------|
| 0 | `export_allowed === true` |
| 1 | Any blocking error, invalid OrcaPpcDocument schema, or invalid ValidationReport schema |

Invalid ValidationReport (fail-closed):

```
ValidationReport schema INVALID (fail-closed):
  /some/path must match ...
Export OK:    false
```

Exit code `1` even if PPC document rules passed.

---

## Report schema self-validation

After building the report, CLI runs AJV on `validation-report-v1.schema.json`.

- **Valid:** `meta.report_schema_valid: true`  
- **Invalid:** console errors, `REPORT-SCHEMA` blocking entry, `export_allowed: false`, exit `1`  

Validator must not ship a schema-invalid artifact.

---

## Deterministic output

v0.1 sorts:

- `rule_results` — by `rule_id`, entity ref, message  
- `blocking_errors` / `warnings` — by `rule_id`, entity ref, message  
- `entity_results` — by kind, id; `rule_ids` sorted unique  

**Why:** stable diffs for [fixtures/validation-report.triumph-s-tier.expected.json](fixtures/validation-report.triumph-s-tier.expected.json) and future CI.

Use `ORCA_VALIDATOR_FIXED_TIMESTAMP` when comparing full JSON including `validation_timestamp`.

---

## Warnings (when present)

- **CM-02** — missing `cta_phrase` for calculate/order  
- **SE-08** — generic CTA phrases  
- **LM-02** — master/fallback landing for specific intent  
- **SV-03** / **SV-04** / **SV-05** — survivability warns  

---

## Operator workflow

1. Edit PPC JSON.  
2. Run CLI once.  
3. Fix `blocking_errors`; review `warnings`.  
4. Confirm `Report schema: valid`.  
5. Re-run until exit `0` if export needed.  
6. Human sign-off — **separate** from `export_allowed`.  
7. Export prep (future) — still no automatic launch.

**STOP:** `export_allowed` ≠ launch approval.
