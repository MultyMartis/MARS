# ORCA Triumph — Prompt System (Phase 6)

**Status:** Documentation foundation only · **no** prompt runtime, registry engine, or autonomous orchestration in-repo.

**Role:** Human-supervised prompt architecture for assisted generation of **structured PPC entities** (`OrcaPpcDocument` JSON) — not Excel, not launch automation.

---

## What lives here

| Doc | Role |
|-----|------|
| [prompt-system-overview-v1.md](prompt-system-overview-v1.md) | Lifecycle, prompt classes, pipeline position |
| [intake-prompt-patterns-v1.md](intake-prompt-patterns-v1.md) | Operator intake → normalized brief |
| [campaign-generation-prompts-v1.md](campaign-generation-prompts-v1.md) | Campaign / group / keyword / routing / negatives |
| [ad-generation-prompts-v1.md](ad-generation-prompts-v1.md) | Headlines, descriptions, extensions, Yandex alignment |
| [validation-fix-prompts-v1.md](validation-fix-prompts-v1.md) | Targeted repair after validation FAIL/WARN |
| [json-output-contract-v1.md](json-output-contract-v1.md) | JSON-only discipline, schema binding |
| [human-review-gates-v1.md](human-review-gates-v1.md) | Mandatory checkpoints before export / import / launch |
| [anti-chaos-prompting-rules-v1.md](anti-chaos-prompting-rules-v1.md) | Quality > quantity; anti-spam doctrine |
| [future-prompt-implementation-notes-v1.md](future-prompt-implementation-notes-v1.md) | Future templates, Cursor, n8n — **targets only** |

---

## Position in pack pipeline

```
Operator request
  → intake prompts (brief)
  → generation prompts (JSON entities)
  → validation (Phase 4 design)
  → validation-fix prompts (surgical repair)
  → export prep (Phase 5 — transport only)
  → human review
  → Commander import (human)
```

**Upstream:** [doctrine/generation-logic-v0.md](../doctrine/generation-logic-v0.md), [schema/](../schema/), [research/intent-groups-v1.md](../research/intent-groups-v1.md)  
**Downstream:** [validation/](../validation/), [exporter/](../exporter/) — consume JSON; do not redefine semantics.

---

## Non-negotiables

1. **JSON-first** — prompts emit `OrcaPpcDocument` fragments or full documents per [json-output-contract-v1.md](json-output-contract-v1.md).  
2. **Validation-before-export** — generation does not bypass validation.  
3. **Human authority** — review gates per [human-review-gates-v1.md](human-review-gates-v1.md); **no auto-launch**.  
4. **SAFE UNKNOWN** — missing business facts → explicit unknowns, not invented capabilities.  
5. **Anti-chaos** — [anti-chaos-prompting-rules-v1.md](anti-chaos-prompting-rules-v1.md) overrides volume-seeking prompts.

---

## How to use (operator / Cursor session)

1. Start pack navigation: [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) — Core Run or Route C.  
2. Run **intake** pattern → produce brief artifact (markdown or JSON sidecar).  
3. Run **campaign generation** → JSON campaign/group graph.  
4. Run **ad generation** per group → JSON `Ad` entities.  
5. Validate (human checklist or future CLI) → [validation/validation-engine-overview-v1.md](../validation/validation-engine-overview-v1.md).  
6. On FAIL/WARN → **validation-fix** prompts (entity-scoped).  
7. Human review → export only when allowed → Commander import by human.

---

## Boundaries

- Does **not** implement agents, daemons, n8n, or prompt registries.  
- Does **not** claim MARS runtime orchestration.  
- Does **not** expand MARS governance — local ORCA pack only.

**Phase 7 (documented hook):** n8n / workflow wiring — see [future-prompt-implementation-notes-v1.md](future-prompt-implementation-notes-v1.md).
