# Exporter Engine Overview v1

**Role:** Architecture for the ORCA Triumph PPC Exporter — **design only**, no runtime.  
**Philosophy:** **Dumb transport** from validated structured document → Commander Excel.

---

## What the exporter is

The exporter **materializes rows** in a workbook shape that Direct Commander can import. It:

- Copies validated field values into transport columns  
- Expands keywords, negatives, and extensions into row sets  
- Applies **normalization** (whitespace, encoding) — not **semantics**  
- Embeds stable entity references for operator traceability (optional metadata column)  

The exporter is **not**:

- A second validation engine (validation already ran)  
- An ad copy improver or intent router  
- A silent truncator for over-limit strings  
- An auto-launch or auto-import service  
- Source-of-truth for campaign meaning  

---

## Position in the production pipeline

```
OrcaPpcDocument
    → Validation Engine → ValidationReport
    → EXPORTER (this document) → .xlsx
    → Human review of workbook
    → Human import in Yandex Direct Commander
    → Human launch / bids / schedule
```

Validation is **complete before** the exporter starts. The exporter reads `export_allowed` and refuses otherwise.

---

## Export lifecycle

| Step | Actor | Output |
|------|--------|--------|
| 1. Inputs | Operator / future CLI | Document JSON + ValidationReport JSON |
| 2. Export pre-check | Exporter | Pass / block with reason codes |
| 3. Template load | Exporter | Workbook skeleton from `triumph-manipulator-commander-template-v0.xlsx` |
| 4. Field mapping | Exporter | Logical column ← entity field (see mapping doc) |
| 5. Normalization | Exporter | Transport-safe strings (no truncation) |
| 6. Row generation | Exporter | Ordered rows per section |
| 7. Workbook write | Exporter | `.xlsx` artifact + export manifest (future) |
| 8. Human review | Operator | Spot-check Cyrillic, URLs, draft flags |
| 9. Commander import | Operator | Platform validation (second line of defense) |
| 10. Launch | Operator | **Never** exporter-triggered |

---

## Layer model

```
┌─────────────────────────────────────────┐
│  Doctrine + entity graph (SoT)          │
├─────────────────────────────────────────┤
│  Validation Engine (semantic + symbol) │
├─────────────────────────────────────────┤
│  Exporter — TRANSPORT ONLY  ← Phase 5   │
├─────────────────────────────────────────┤
│  Commander Excel (reference shape)      │
├─────────────────────────────────────────┤
│  Yandex Direct (runtime of record)      │
└─────────────────────────────────────────┘
```

---

## Inputs and outputs

### Required inputs

| Input | Contract |
|-------|----------|
| `OrcaPpcDocument` | [orca-ppc-document-v1.schema.json](../schema/json/orca-ppc-document-v1.schema.json) |
| `ValidationReport` | [validation-report-v1.schema.json](../schema/json/validation-report-v1.schema.json) |
| Template reference | [commander-template-contract-v1.md](commander-template-contract-v1.md) |

### Output artifacts (future)

| Artifact | Role |
|----------|------|
| `*.xlsx` | Commander import file |
| `export-manifest-v1.json` (optional) | Row counts, entity_ids exported, template version, report id |

---

## Forbidden exporter behaviors

Aligned with [export-mapping-schema-v1.md](../schema/export-mapping-schema-v1.md):

| Forbidden | Why |
|-----------|-----|
| Truncate headlines/descriptions to fit limits | Validation must fail first; no silent fix |
| Inject keywords into copy | Semantic — validation/doctrine domain |
| Change `landing_url` from `landing_type` | Semantic routing |
| Merge groups with different intents | Structural corruption |
| Export when `export_allowed` = false | Bypasses validation gate |
| Export RSYA / non-search campaign types | Pack search-only scope |
| Auto-import into Direct API | Human-supervised workflow |

---

## Human supervision

| Checkpoint | Responsibility |
|------------|----------------|
| Pre-export validation | Operator or future validator CLI |
| Warn acceptance | Operator documents overrides |
| Workbook review | Operator before import |
| Commander import errors | Operator fixes document or template mapping |
| Launch | Operator only — `launch_allowed` never set by exporter |

---

## Transport survivability

Exporter design preserves operability after import:

- **Stable row ordering** — campaign → group → keywords → ads → extensions  
- **Readable group names** — copied verbatim from entity (no slugification)  
- **Draft clarity** — draft rows use template draft marker, not hidden omission  
- **Duplicate prevention** — one row per keyword phrase per group; dedup keys in row-generation doc  

---

## Related documents

- [export-preconditions-v1.md](export-preconditions-v1.md)  
- [entity-to-commander-mapping-v1.md](entity-to-commander-mapping-v1.md)  
- [export-blocking-rules-v1.md](export-blocking-rules-v1.md)  
- [future-exporter-implementation-notes-v1.md](future-exporter-implementation-notes-v1.md)  

---

## SAFE UNKNOWN

- Exact Commander sheet names and header literals — verify from `.xlsx` at implementation ([commander-template-contract-v1.md](commander-template-contract-v1.md)).  
- Account-type-specific columns — operator may delete unused columns before import.
