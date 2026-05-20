# Validation Engine Overview v1

**Role:** Architecture for the ORCA Triumph PPC Validation Engine — **design only**, no runtime.  
**Pack:** Triumph Manipulator · Yandex Search · human-supervised.

---

## What validation is for

Validation answers one question before export:

> **Is this structured PPC document safe to map into Commander Excel without shipping garbage?**

Validation is **not**:

- Silent auto-correction of headlines, URLs, or keywords  
- A launch orchestrator or campaign manager  
- A substitute for operator judgment on warnings  
- Post-export repair of Excel rows  

---

## Position in the production pipeline

```
Intent research → Entity assembly (JSON / structured model)
        ↓
   VALIDATION ENGINE  ← this document
        ↓
   Export gate (export_allowed)
        ↓
   Dumb exporter → Commander Excel (transport)
        ↓
   Human import + human launch in Direct
```

Excel never enters validation as source-of-truth. If validation starts from Excel, the operator must first normalize to the internal document model.

---

## Validation lifecycle

| Stage | Actor | Output |
|-------|--------|--------|
| 1. Document intake | Operator or future CLI | `OrcaPpcDocument` reference |
| 2. Structural pass | Engine / checklist | ST-* results |
| 3. Symbol pass | Engine / checklist | SY-* results |
| 4. Semantic pass | Engine / checklist | SE-* results |
| 5. Landing continuity pass | Engine / checklist | LM-* results |
| 6. Commercial pass | Engine / checklist | CM-* results |
| 7. Survivability pass | Engine / checklist | SV-* results |
| 8. Export-mapping pass | Engine / checklist | EX-* results |
| 9. Aggregation | Engine | `rule_results`, `entity_results`, severity buckets |
| 10. Report emit | Engine | `ValidationReport` JSON |
| 11. Export gate | Policy + human | `export_allowed` |
| 12. Human review | Operator | Notes, overrides on warns |
| 13. Final status | Operator | `launch_allowed` — **never automatic** |

Stages 2–8 are **rule execution stages** (see [rule-execution-flow-v1.md](rule-execution-flow-v1.md)). Order is fixed for determinism; within a stage, rules may run in registry order.

---

## Entity traversal model

The engine walks the **entity graph** defined in [entity-model-overview-v1.md](../schema/entity-model-overview-v1.md):

```
Document (root)
  └── Campaign[]
        └── Group[]
              ├── keyword_cluster
              ├── landing_route
              ├── group_negatives
              └── Ad[]
```

### Traversal rules

1. **Document-level** — `schema_version`, `search_only_scope`, project metadata (ST-01, ST-02).  
2. **Campaign-level** — campaign container, global negatives, geo (ST-03+, CM-04, NG-*).  
3. **Group-level** — intent purity, cluster, landing route, classifications (SE-*, LM-*, SV-*).  
4. **Ad-level** — copy, symbols, alignment, mobile flags (SY-*, SE-*, CM-*).  
5. **Cross-entity** — URL match ad↔group, duplicate H1 across groups, negative conflicts (LM-01, SE-08/09, NG-02).

Each rule declares `target_entity` in [rule-registry-v1.md](rule-registry-v1.md). The executor attaches `entity_ref` (`entity_kind`, `entity_id`, optional `field_path`) to every non-pass result.

---

## Rule execution stages (summary)

| Stage | Class prefix | Primary focus |
|-------|--------------|---------------|
| Structural | ST- | Graph completeness, referential integrity, search-only |
| Symbol | SY- | Yandex Direct field limits (spaces included) |
| Semantic | SE- | Intent purity, anti-garbage, phrase-in-headline |
| Landing | LM- | Ad ↔ landing continuation, blueprint family |
| Commercial | CM- | CTA, capability truth, trust, mobile |
| Survivability | SV- | Human-operable structure, anti-chaos |
| Export mapping | EX- | Pre-export mapping readiness (no semantic fixes) |

**Negative keyword rules (NG-*)** run in the structural stage but are catalogued in the registry alongside ST rules.

---

## Severity system

| Severity | `rule_result.status` | Effect on export | Effect on launch |
|----------|----------------------|------------------|------------------|
| `error` | `fail` | **Block** — `export_allowed` = false | Block until fixed |
| `warn` | `warn` | Allow only with human acknowledgment | Human decides |
| `info` | `pass` or `warn` | Allow | Suggestion only |

### Blocking vs warning logic

- **Blocking (`error`):** Any single ST/SY/SE/LM/CM failure that would produce broken import, wrong intent, or policy-violating garbage → must fix before export.  
- **Warning (`warn`):** Degraded quality or survivability risk that a skilled operator might accept with documented reason (e.g. master landing fallback, large keyword cluster).  
- **Info:** Traceability only (e.g. future `approved_for_export` reminder) — does not block.

**No silent truncation:** Symbol over-limit is always `error`, never auto-trim (see [symbol-validation-rules-v1.md](symbol-validation-rules-v1.md)).

### `safe_unknown` status

When a rule cannot be evaluated (e.g. live Direct UI limit drift, incomplete blueprint reference), emit:

- `status`: `safe_unknown` on the rule result, and  
- an entry in report `safe_unknown[]` with `topic` + `message`.

`safe_unknown` does **not** imply pass. Default policy: treat as **block export** until human confirms — document override in operator notes.

---

## Human review interaction

Validation **assists**; it does not replace the operator.

| Situation | Required human action |
|-----------|------------------------|
| Any `error` | Fix entity or demote to draft; re-validate |
| `warn` on LM-06 (master fallback) | Confirm fallback justified or assign correct blueprint |
| `warn` on SE-13 (large cluster) | Split group or document threshold exception |
| `safe_unknown` | Confirm against live Direct UI or blueprint |
| `export_allowed` = true | Operator explicitly proceeds to exporter |
| Launch in Direct | **Always** manual — see `launch_allowed` in [validation-report-generation-v1.md](validation-report-generation-v1.md) |

Future optional field: `validation_override` on document meta — **human-written reason** for accepted warns; never auto-generated.

---

## ValidationReport generation (overview)

The engine materializes a report matching [validation-report-v1.schema.json](../schema/json/validation-report-v1.schema.json):

- `rule_results[]` — one row per rule execution (pass/fail/warn/not_checked/safe_unknown)  
- `entity_results[]` — rolled-up worst status per campaign/group/ad  
- `blocking_errors[]` / `warnings[]` — denormalized indexes for UI  
- `export_allowed` — computed gate (false if any blocking error or policy block)  
- `human_review_required` — true if any warn, safe_unknown, or incomplete pass  

Full pipeline: [validation-report-generation-v1.md](validation-report-generation-v1.md).

---

## Design constraints (non-negotiable)

1. **Before export** — validation never runs “only on Excel.”  
2. **No mutation** — validator reads document; suggested fixes are text only.  
3. **Search-only** — ST-02 enforces `search_only_scope`; no RSYA rules in v1.  
4. **Quality > quantity** — survivability rules resist giant dumps and duplicate chaos.  
5. **No autonomous launch** — `launch_allowed` is not set by the engine without explicit human sign-off semantics.

---

## Related documents

- [rule-registry-v1.md](rule-registry-v1.md) — all rule IDs  
- [rule-execution-flow-v1.md](rule-execution-flow-v1.md) — execution ordering and aggregation  
- [future-validator-implementation-notes-v1.md](future-validator-implementation-notes-v1.md) — implementation targets  

---

## SAFE UNKNOWN

- Exact Commander column validation at export time — EX rules cover logical mapping; sheet drift verified at implementation.  
- Platform moderation after import — operator confirms in Direct.
