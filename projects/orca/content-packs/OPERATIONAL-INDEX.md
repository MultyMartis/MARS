# ORCA Content Packs — Operational Index

**Lane:** B — ORCA / Intelligence / Content Export  
**Domain root:** [README.md](README.md)  
**Status:** v0 foundation — documentation and contracts only.

---

## Canonical reading order

| Step | Document | Why |
|------|----------|-----|
| 1 | [content-pack-system-v0.md](content-pack-system-v0.md) | What a content pack is; inputs/outputs; section model |
| 2 | [export-pipeline-v0.md](export-pipeline-v0.md) | Research → pack → export → Factory |
| 3 | [semantic-lock-export-rules-v0.md](semantic-lock-export-rules-v0.md) | MODE 1 / MODE 2 and export integrity |
| 4 | [artifact-lifecycle-v0.md](artifact-lifecycle-v0.md) | States and approval gates |
| 5 | [schemas/landing-content-pack-schema-v0.md](schemas/landing-content-pack-schema-v0.md) | Pack envelope schema |
| 6 | [workflows/research-to-pack-workflow-v0.md](workflows/research-to-pack-workflow-v0.md) | Operator flow: research → pack |
| 7 | [workflows/pack-to-factory-workflow-v0.md](workflows/pack-to-factory-workflow-v0.md) | Pack → Factory handoff |
| 8 | [workflows/operator-review-flow-v0.md](workflows/operator-review-flow-v0.md) | Review and sign-off |

**Example pack:** [examples/triumph-manipulyator-5-tonn-pack-v0.md](examples/triumph-manipulyator-5-tonn-pack-v0.md)

---

## Schemas

| Doc | Role |
|-----|------|
| [schemas/landing-content-pack-schema-v0.md](schemas/landing-content-pack-schema-v0.md) | Pack root fields |
| [schemas/section-contract-schema-v0.md](schemas/section-contract-schema-v0.md) | Per-section contract |
| [schemas/export-metadata-schema-v0.md](schemas/export-metadata-schema-v0.md) | Export run metadata |
| [schemas/content-pack-json-example-v0.json](schemas/content-pack-json-example-v0.json) | Machine-readable shape (reference) |

---

## Templates

| Template | Use |
|----------|-----|
| [templates/landing-content-pack-template-v0.md](templates/landing-content-pack-template-v0.md) | New landing pack authoring |
| [templates/website-factory-handoff-template-v0.md](templates/website-factory-handoff-template-v0.md) | Factory MODE 1 handoff |
| [templates/faq-template-v0.md](templates/faq-template-v0.md) | Section 09 FAQ block |
| [templates/trust-block-template-v0.md](templates/trust-block-template-v0.md) | Section 07 TRUST |
| [templates/pricing-block-template-v0.md](templates/pricing-block-template-v0.md) | Section 06 PRICING |

---

## Exporters (architecture only — v0)

| Doc | Role |
|-----|------|
| [exporters/README.md](exporters/README.md) | Exporter layer boundaries |
| [exporters/docx-export-architecture-v0.md](exporters/docx-export-architecture-v0.md) | **Primary** approved export format |
| [exporters/markdown-export-architecture-v0.md](exporters/markdown-export-architecture-v0.md) | Operational / internal export |
| [exporters/pdf-export-architecture-v0.md](exporters/pdf-export-architecture-v0.md) | Future client layer |
| [exporters/export-modes-v0.md](exporters/export-modes-v0.md) | Export mode vocabulary |

**Not in this folder:** `ppc/triumph-manipulator/tools/exporter-cli/` (Commander transport).

---

## Workflows

| Workflow | Trigger |
|----------|---------|
| [workflows/research-to-pack-workflow-v0.md](workflows/research-to-pack-workflow-v0.md) | New route / intent tier / landing need |
| [workflows/pack-to-factory-workflow-v0.md](workflows/pack-to-factory-workflow-v0.md) | `approved_for_factory` |
| [workflows/operator-review-flow-v0.md](workflows/operator-review-flow-v0.md) | Every state transition |

---

## Cross-lane links

| Target | Path |
|--------|------|
| ORCA root index | [../OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) |
| Semantic lock (MODE 1) | [../intelligence/orca-website-factory-semantic-lock-v0.md](../intelligence/orca-website-factory-semantic-lock-v0.md) |
| Factory bridge index | [../intelligence/orca-factory-bridge-index-v0.md](../intelligence/orca-factory-bridge-index-v0.md) |
| Approval gates | [../artifacts/approval-gates-contract-v0.md](../artifacts/approval-gates-contract-v0.md) |
| Triumph PPC pack | [../ppc/triumph-manipulator/OPERATIONAL-INDEX.md](../ppc/triumph-manipulator/OPERATIONAL-INDEX.md) |
| Website Factory | [../../mars-website-factory/README.md](../../mars-website-factory/README.md) (implementation lane) |

---

## STOP cues

- Pack still `draft` → do not export as client-ready DOCX
- MODE 1 active → do not let Factory rewrite copy without operator override
- Missing evidence → mark **SAFE UNKNOWN**; do not invent prices, fleet, or review quotes
- Next step is Commander import → use **exporter-cli**, not content-packs exporters

---

## Boundary

Navigation and contracts only. No runtime, no orchestration, no auto-approval.
