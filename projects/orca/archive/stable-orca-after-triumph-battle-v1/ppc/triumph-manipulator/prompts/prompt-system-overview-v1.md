# Prompt System Overview v1

**Pack:** Triumph Manipulator · **Phase:** 6 (Prompt System Foundation)  
**Status:** Architecture documentation · **no runtime**

---

## Purpose

Define how **human-supervised prompts** assist production of **ORCA PPC JSON entities** for Yandex Search — replacing Excel-native and volume-first AI habits with a validation-ready structured model.

Prompts are **copilot instructions**, not autonomous marketers.

---

## What the prompt system is

| Is | Is not |
|----|--------|
| Lifecycle and class taxonomy for Cursor/human sessions | Autonomous campaign launcher |
| Patterns that target `OrcaPpcDocument` | Excel row generators |
| Repair prompts scoped to validation findings | Blind full-document regeneration |
| Gates tying prompts to human approval | Auto-export or auto-import |

---

## End-to-end lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. OPERATOR REQUEST                                              │
│    Business goal, constraints, tier focus (S/A first)            │
└────────────────────────────┬────────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. INTAKE NORMALIZATION (intake prompts)                         │
│    Brief: niche, geo, capabilities, use-cases, landings,         │
│    intent tiers, B2B scope, exclusions, priorities, constraints  │
│    Output: intake brief (JSON sidecar or structured markdown)    │
│    SAFE UNKNOWN where facts missing                               │
└────────────────────────────┬────────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. CAMPAIGN / ENTITY GENERATION (generation prompts)             │
│    Campaign structure, groups, keyword clusters, negatives,      │
│    landing routes, intent tiers                                  │
│    Output: OrcaPpcDocument (partial or full) — JSON ONLY         │
└────────────────────────────┬────────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. AD GENERATION (ad prompts, per group)                         │
│    Headlines, descriptions, fastlinks, callouts, alignment       │
│    Output: Ad[] under each Group — JSON ONLY                     │
└────────────────────────────┬────────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. VALIDATION (Phase 4 design — human or future CLI)             │
│    ST / SY / SE / LM / CM / SV / EX → ValidationReport         │
└────────────────────────────┬────────────────────────────────────┘
                             ▼
                    ┌────────┴────────┐
                    │ FAIL / WARN?    │
                    └────────┬────────┘
              yes ──────────┼────────── no
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 6. VALIDATION-FIX / REPAIR (fix prompts)                       │
│    Patch entity_ref targets only — no full regen by default      │
└────────────────────────────┬────────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 7. HUMAN REVIEW GATE (mandatory)                               │
│    Structure, truthfulness, launch readiness                     │
│    human_review status updated in document                       │
└────────────────────────────┬────────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 8. EXPORT PREPARATION (Phase 5 — dumb transport)               │
│    Only if validation export_allowed + human approval            │
│    Exporter: Excel rows — no semantic logic                      │
└────────────────────────────┬────────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 9. COMMANDER IMPORT + LAUNCH (human only)                      │
│    Operator in Yandex Direct — NEVER prompt-triggered            │
└─────────────────────────────────────────────────────────────────┘
```

---

## Prompt classes

| Class | When | Primary output | Doc |
|-------|------|----------------|-----|
| **Intake** | New project or major scope change | Normalized brief | [intake-prompt-patterns-v1.md](intake-prompt-patterns-v1.md) |
| **Campaign generation** | After intake approved | Campaign, Group, clusters, routes | [campaign-generation-prompts-v1.md](campaign-generation-prompts-v1.md) |
| **Ad generation** | Groups exist | Ad entities + extensions | [ad-generation-prompts-v1.md](ad-generation-prompts-v1.md) |
| **Validation-fix** | After ValidationReport | Patched JSON entities | [validation-fix-prompts-v1.md](validation-fix-prompts-v1.md) |
| **Repair (structural)** | Broken IDs, missing parents | Minimal graph fixes | validation-fix doc |
| **Review assist** | Pre-export checklist | Human-readable risk summary (optional markdown) — **not** SoT | [human-review-gates-v1.md](human-review-gates-v1.md) |

**Forbidden class (implicit):** “Generate 1000 ads” / “fill Excel template” / “launch campaign” — see [anti-chaos-prompting-rules-v1.md](anti-chaos-prompting-rules-v1.md).

---

## Binding to pack artifacts

| Artifact | Prompt must respect |
|----------|---------------------|
| Entity graph | [schema/entity-model-overview-v1.md](../schema/entity-model-overview-v1.md) |
| JSON contract | [schema/json/orca-ppc-document-v1.schema.json](../schema/json/orca-ppc-document-v1.schema.json) |
| Validation semantics | [validation/validation-engine-overview-v1.md](../validation/validation-engine-overview-v1.md), [validation/rule-registry-v1.md](../validation/rule-registry-v1.md) |
| Doctrine | [doctrine/generation-logic-v0.md](../doctrine/generation-logic-v0.md) |
| Export | [exporter/exporter-engine-overview-v1.md](../exporter/exporter-engine-overview-v1.md) — transport only |

---

## Session discipline (Cursor / human)

1. **One Core Run** per session — [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md).  
2. Attach **intake brief** + **doctrine excerpt** by reference, not full pack dump.  
3. Request **JSON-only** responses per [json-output-contract-v1.md](json-output-contract-v1.md).  
4. Run validation checklist before suggesting export.  
5. **STOP** when structure is review-ready — do not expand keyword volume “to be thorough”.

---

## Output contracts (summary)

All generation and fix prompts default to:

- Single JSON object or JSON Patch-style fragment  
- `schema_version: "v1"`  
- Stable `entity_id` conventions  
- `source_pack: "triumph-manipulator"`  
- `search_only_scope: true`  
- No prose outside JSON (except optional separate review memo if operator asks)

Full rules: [json-output-contract-v1.md](json-output-contract-v1.md).

---

## Human supervision model

| Step | Human role |
|------|------------|
| Intake | Confirms capabilities, landings, exclusions |
| Generation | Approves architecture before ad volume |
| Validation | Interprets WARNs; fixes or accepts with note |
| Export | Approves workbook spot-check |
| Launch | Sole authority in Direct |

Details: [human-review-gates-v1.md](human-review-gates-v1.md).

---

## Future implementation (not built)

Versioned prompt files in repo, Cursor rule snippets, CLI wrappers, n8n human-triggered flows — [future-prompt-implementation-notes-v1.md](future-prompt-implementation-notes-v1.md).

**No daemon. No agent swarm. No background runtime.**
