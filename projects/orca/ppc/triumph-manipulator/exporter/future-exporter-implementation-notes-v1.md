# Future Exporter Implementation Notes v1

**Role:** Guidance for a **future** human-operated export CLI — **not** a build spec for this phase.  
**Honesty:** No exporter code exists in the Triumph pack today.

---

## Target shape

```
export-cli \
  --document ./triumph-s-tier-draft-v1.json \
  --report ./reports/triumph-s-tier-validation.json \
  --template ../assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx \
  --mode active_only \
  --out ./out/triumph-s-tier-commander.xlsx
```

- **Exit 0** only when workbook written and pre-check passed  
- **Exit non-zero** on any [export-blocking-rules-v1.md](export-blocking-rules-v1.md) code  
- **No** network, **no** Direct API, **no** daemon  

---

## Technology options (non-prescriptive)

| Stack | Notes |
|-------|-------|
| **Node.js** | `exceljs` or `xlsx` for workbook clone + cell write |
| **Python** | `openpyxl` — common for ops scripts |
| Template clone | Load v0 xlsx as skeleton; preserve styles where possible |
| JSON input | `orca-ppc-document-v1.schema.json` optional AJV pre-parse |

---

## Implementation modules (suggested)

| Module | Responsibility |
|--------|----------------|
| `precheck` | [export-preconditions-v1.md](export-preconditions-v1.md) |
| `normalize` | [field-normalization-rules-v1.md](field-normalization-rules-v1.md) |
| `rows` | [row-generation-rules-v1.md](row-generation-rules-v1.md) |
| `map` | [entity-to-commander-mapping-v1.md](entity-to-commander-mapping-v1.md) + verified header map |
| `draft` | [draft-export-rules-v1.md](draft-export-rules-v1.md) |
| `write` | xlsx output + manifest |

**No `semantic` module.**

---

## Header map artifact (future)

After manual xlsx verification:

```yaml
# commander-header-map-v0.yaml (not created in Phase 5)
template_revision: v0
columns:
  headline_1: "Title 1"   # example only — replace with verified literal
  ...
```

Generated once per template revision; version-controlled beside template.

---

## Fixture export tests

| Fixture | Test |
|---------|------|
| `triumph-s-tier-draft-v1.json` + golden validation report | Export `active_only` row counts match manifest |
| Minimal 1-group doc | Single campaign sheet population |
| Block case: `export_allowed: false` | CLI exits non-zero, no file |

Golden `.xlsx` binaries optional under `schema/instances/expected-exports/` — **not created in Phase 5**.

---

## Batch export

```
export-cli --batch ./instances/*.json --reports-dir ./reports/
```

Each document requires its own `ValidationReport`. Batch does **not** skip validation gate.

---

## Schema-version adapters

When `schema_version: v2` appears:

- Adapter `v2 → v1` transport view **or** parallel mapping doc  
- Exporter refuses unknown version without adapter — no silent best-effort  

---

## Integration boundaries

| System | Relationship |
|--------|--------------|
| Validator | Produces report; exporter consumes |
| n8n | May **invoke** CLI; human still reviews xlsx |
| Commander | Human import only |
| MARS runtime | No integration claimed until code exists |

---

## Explicit non-goals

- Autonomous export on file watch  
- Direct API upload  
- Round-trip xlsx → JSON in v1  
- Semantic “fixup” pass  
- Silent truncation  
- Auto-launch  

---

## SAFE UNKNOWN

- Library choice (Node vs Python) — operator toolchain decision.  
- Whether to preserve template macros — assume none; verify xlsx.
