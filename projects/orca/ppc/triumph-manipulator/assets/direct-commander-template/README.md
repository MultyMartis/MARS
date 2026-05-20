# Direct Commander template — reference asset

## What lives here

| Asset | Role |
|-------|------|
| `triumph-manipulator-commander-template-v0.xlsx` | Production-proven Commander import **transport** schema from live campaign export (field layout, limits annotations, draft examples) |

## Source-of-truth distinction (critical)

| Layer | Status |
|-------|--------|
| ORCA doctrine + internal structured PPC model (future JSON) | **Source of truth** for meaning, segmentation, validation rules |
| Markdown docs in this pack | **Operational SoT** for humans/agents (Phase 1) |
| This Excel file | **Reference transport only** — import format contract, **not** campaign logic |

Do **not** treat Excel as the place to invent or store PPC semantics.  
Do **not** hand-edit generated export cells as “the campaign” without reconciling back to structured intent.

## How operators should use it

1. Build campaign structure from doctrine + intent research + landing routing (human or future tools).  
2. Validate symbol limits and intent purity **before** export (manual today).  
3. Use this template only to understand Commander field expectations or as import target shape.  
4. Human reviews and imports in Yandex Direct Commander.

## Provenance

Copied from `incoming/orca-triumph-raw-pack/` during pack normalization (2026-05-20). Original filename preserved in incoming folder; normalized name here for stable paths.

## SAFE UNKNOWN

- Exact Yandex Direct UI version drift vs template columns — confirm at import time.  
- Whether all draft/active row examples remain valid for your account type — human check required.
