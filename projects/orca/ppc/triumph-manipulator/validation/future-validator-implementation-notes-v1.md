# Future Validator Implementation Notes v1

**Role:** Implementation guidance for a **future** human-operated validator — **not** a build spec for this phase.  
**Honesty:** No validator code, CLI, or service exists in the Triumph pack today.

---

## Target shape

A validator should be:

- **CLI-first** — operator runs explicitly (`validate triumph-draft.json`)  
- **Read-only** — input document path → output report path  
- **Deterministic** — same input + ruleset → same rule_results order  
- **Exit codes** — non-zero when `export_allowed` is false  

**Not:**

- A daemon listening for file changes  
- An n8n auto-loop that exports without human  
- A Cursor agent that silently fixes and re-exports  

---

## Technology options (non-prescriptive)

| Approach | Fit |
|----------|-----|
| **Node.js CLI** | Matches potential MARS JS tooling; JSON native |
| **Python CLI** | Good for batch reports and spreadsheet-adjacent ops |
| **AJV** | Validate document against [orca-ppc-document-v1.schema.json](../schema/json/orca-ppc-document-v1.schema.json) — **structural only**, not semantic rules |
| **Custom rule registry** | Load [rule-registry-v1.md](rule-registry-v1.md) IDs → functions or declarative checks |

Recommended split:

1. **AJV** — schema_version, required fields, types (partial ST-*)  
2. **Rule engine** — SE, LM, CM, SV, SY string logic  
3. **Report writer** — emit JSON matching [validation-report-v1.schema.json](../schema/json/validation-report-v1.schema.json)

---

## JSON traversal

```
parse JSON
  → validate schema (AJV)
  → build entity_index:
       campaigns by campaign_id
       groups by group_id (+ parent)
       ads by ad_id (+ parent)
  → run stages per rule-execution-flow-v1.md
  → write ValidationReport
```

Use `field_path` in findings (e.g. `campaigns[0].groups[2].ads[0].headline_1`) for operator navigation.

---

## Rule registry implementation

| Pattern | Notes |
|---------|-------|
| One function per rule ID | `rules/SY-01.js` exports `check(doc, ctx)` |
| Table-driven | Registry YAML → generic executor (harder for SE anti-garbage) |
| Hybrid | ST/SY table-driven; SE/LM scripted |

Ruleset version: `meta.ruleset_ref = "triumph-validation-v1@2026-05-20"`.

---

## Batch validation

```
validate-cli --input ./instances/*.json --out ./reports/
```

Use cases:

- Regression on [triumph-s-tier-draft-v1.json](../schema/instances/triumph-s-tier-draft-v1.json)  
- Pre-export batch for multiple campaigns in one document  

Batch mode still **does not** launch or export automatically.

---

## Fixture testing

| Fixture | Expectation |
|---------|-------------|
| `triumph-s-tier-draft-v1.json` | Known warns/errors (e.g. `intent_continuity_ack: false`) — golden report snapshot |
| Minimal invalid doc | ST failures, `incomplete` or `failed` |
| Clean S-tier single group | `passed` when launch-ready flags set |

Store golden reports under `schema/instances/expected-reports/` **only when** Phase 5+ chooses to add them — not required in Phase 4.

---

## Integration boundaries

| System | Relationship |
|--------|--------------|
| Exporter | Consumes `export_allowed`; runs after validation |
| Excel template | Reference for SY limits; not validated in place |
| n8n | Optional trigger to **run** CLI; human still reviews report |
| MARS runtime | **No** claim of integration until code exists |

---

## Explicit non-goals (v1 implementation)

- ML ad quality scoring  
- SERP scraping for competitive analysis  
- Autonomous negative keyword mining  
- Auto-launch via Direct API  
- Silent truncation or “fix headline” buttons without diff review  

---

## SAFE UNKNOWN

- Whether Triumph uses Node or Python in production toolchain — operator choice at implementation time.  
- Direct API validation — out of scope; Commander import remains human step.
