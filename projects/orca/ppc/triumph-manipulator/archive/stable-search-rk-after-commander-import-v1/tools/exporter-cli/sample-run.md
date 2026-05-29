# Exporter CLI — sample runs

**Tool:** ORCA Exporter Prototype v0 · local-only · human-triggered.

---

## Prerequisites

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm install
```

Validate document first (validation-cli):

```bash
cd ../validation-cli
npm install
node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json
```

---

## Example command (default output path)

```bash
cd ../exporter-cli
node export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  ../../tools/validation-cli/output/validation-report.output.json
```

---

## Example fail case (current validator output)

When `validation-report.output.json` has `export_allowed: false` (e.g. SE-05 blocking error on `ad_s04_b2b_a2`):

```text
--- ORCA Exporter Prototype v0 — EXPORT BLOCKED ---
Block code:  EXPORT_NOT_ALLOWED
Reason:      export_allowed is not true. Fix validation findings and re-run validator.
```

Or if blocking errors are listed first:

```text
Block code:  BLOCKING_ERRORS_PRESENT
Reason:      ValidationReport has 1 blocking error(s). Export blocked.
Details:
  - [SE-05] Primary keyword phrase not detected in headline_1: "манипулятор безнал краснодар".
```

**Exit code:** `1` · **No** XLSX written (fail-closed).

---

## Example success case (test fixture)

For architecture testing only, use the operator fixture with `export_allowed: true`:

```bash
node export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  ./fixtures/validation-report.export-allowed.fixture.json
```

**Expected console (abbreviated):**

```text
--- ORCA Exporter Prototype v0 — SUCCESS (transport draft) ---
Output:    .../tools/exporter-cli/output/triumph-export-draft.xlsx
Row counts:
  campaigns:  1
  groups:     5
  keywords:   ...
  ads:        7
  extensions: ...
```

**Exit code:** `0`

---

## Expected XLSX output

| Sheet | Content |
|-------|---------|
| `_meta` | Exporter version, document id, disclaimer |
| `campaigns` | One row per campaign (logical columns) |
| `groups` | One row per ad group |
| `keywords` | One row per keyword phrase |
| `ads` | One row per ad |
| `extensions` | Fastlinks and callouts (`extension_type` column) |

Open in Excel/LibreOffice — verify UTF-8 Cyrillic text. Compare field-by-field to JSON; **do not** assume Commander import works without human column mapping review.

---

## Export blocking examples

| Scenario | Block code |
|----------|------------|
| Report path omitted / missing file | Process exit before precheck (file not found) |
| `export_allowed: false` | `EXPORT_NOT_ALLOWED` |
| Non-empty `blocking_errors` | `BLOCKING_ERRORS_PRESENT` |
| `validation_status: failed` | `VALIDATION_FAILED` |
| Report fails JSON Schema | `INVALID_REPORT_SCHEMA` |
| `schema_version` ≠ `v1` | `UNSUPPORTED_SCHEMA_VERSION` |
| Document `search_only_scope: false` | `NON_SEARCH_SCOPE` |
| `validated_document_id` ≠ `project_id` | `DOCUMENT_ID_MISMATCH` |

---

## Operator workflow

1. Edit PPC JSON  
2. `validation-cli` → review report  
3. Fix blocking errors until `export_allowed: true`  
4. `exporter-cli` → review XLSX draft  
5. Human import in Direct Commander → human launch  
