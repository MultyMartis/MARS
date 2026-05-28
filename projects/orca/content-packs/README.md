# ORCA Content Packs — Landing Content Export Layer

**Status:** **documented foundation (v0)** — human-operated semantic export architecture.  
**Not:** runtime, orchestration, autonomous generation, deployment, crawling, or API product.

## Purpose

ORCA Content Packs are the **canonical semantic layer** between:

```
ORCA Research / Strategy
  → Landing Content Pack (structured marketing semantics)
  → DOCX / Markdown export (human-approved artifacts)
  → Website Factory implementation (Lane A — presentation only under MODE 1)
  → PPC QA → launch gates
```

**ORCA Content Pack ≠ HTML.** Packs carry section contracts, copy blocks, CTA logic, PPC/SEO continuity, semantic locks, and factory notes — not page markup.

## Lane split

| Layer | Owns |
|-------|------|
| **ORCA** (`content-packs/`, research, PPC packs) | Meaning, positioning, claims, intent continuity, approval gates |
| **Website Factory** | Layout, responsive UI, components, build pipeline |
| **exporter-cli** (Triumph pack) | Direct Commander XLSX transport — **out of scope** for this folder |

## Quick start

1. Read [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)
2. Read [content-pack-system-v0.md](content-pack-system-v0.md)
3. Use [templates/landing-content-pack-template-v0.md](templates/landing-content-pack-template-v0.md) for a new pack
4. Follow [workflows/research-to-pack-workflow-v0.md](workflows/research-to-pack-workflow-v0.md)
5. Hand off via [templates/website-factory-handoff-template-v0.md](templates/website-factory-handoff-template-v0.md) when `approved_for_factory`

## Reference examples

- [examples/triumph-manipulyator-5-tonn-pack-v0.md](examples/triumph-manipulyator-5-tonn-pack-v0.md) — capability landing pack (single-file v0).
- [examples/triumph-manipulyator-zakaz-pack-v1/](examples/triumph-manipulyator-zakaz-pack-v1/) — **first calibrated** master-hot pack (visual semantics + PPC continuity + drift control; as-built v5 zakaz).

## Boundaries

- **Human operator** approves all gates — see [semantic-lock-export-rules-v0.md](semantic-lock-export-rules-v0.md)
- **MODE 1:** Website Factory must not rewrite approved ORCA copy — see [../intelligence/orca-website-factory-semantic-lock-v0.md](../intelligence/orca-website-factory-semantic-lock-v0.md)
- **No** automatic approval, **no** export CLI in this tree (future human-triggered exporters documented under `exporters/`)

## Related ORCA docs

- [../intelligence/orca-factory-bridge-index-v0.md](../intelligence/orca-factory-bridge-index-v0.md)
- [../artifacts/approval-gates-contract-v0.md](../artifacts/approval-gates-contract-v0.md)
- [../artifacts/orca-artifact-system-v0.md](../artifacts/orca-artifact-system-v0.md)
