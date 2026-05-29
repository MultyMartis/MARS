# Direct Commander template — reference asset

## What lives here

| Asset | Role |
|-------|------|
| `triumph-manipulator-commander-template-v1.xlsx` | **Production SoT** — Commander Search Manual Bids import template (approved 2026-05-29) |
| `triumph-manipulator-commander-template-v0.xlsx` | Historical transport schema — **do not use** for new exports |

## Source-of-truth distinction (critical)

| Layer | Status |
|-------|--------|
| ORCA doctrine + JSON instance (`schema/instances/`) | **Source of truth** for meaning, segmentation, validation rules |
| Markdown docs + freeze governance | **Operational SoT** for humans/agents |
| **Template v1** (`triumph-manipulator-commander-template-v1.xlsx`) | **Commander transport SoT** — Search · manual bids · import shape |
| Generated `output/*.xlsx` | Disposable import snapshot — gitignored |

Do **not** treat Excel as the place to invent or store PPC semantics.  
Do **not** hand-edit generated export cells as “the campaign” without reconciling back to structured intent.

**Freeze:** [freeze/ppc-exporter-production-baseline-v1/COMMANDER-TEMPLATE-SOT-v1.md](../../../freeze/ppc-exporter-production-baseline-v1/COMMANDER-TEMPLATE-SOT-v1.md)

## Strategy (template v1)

- Реклама на поиске  
- Ручное управление ставками  
- Status: approved · production validated · commander imported · human calibrated

## How operators should use it

1. Build campaign structure from doctrine + JSON + validation (human or CLI).  
2. Build cross-negative matrix — [CROSS-NEGATIVE-RULES-v1.md](../../../freeze/ppc-exporter-production-baseline-v1/CROSS-NEGATIVE-RULES-v1.md).  
3. Run hygiene audit — [COMMANDER-HYGIENE-AUDIT-v1.md](../../../freeze/ppc-exporter-production-baseline-v1/COMMANDER-HYGIENE-AUDIT-v1.md).  
4. Export with Exporter v1.2 (`export:sheet1-patch:full-cycle-v1.2`) — template v1 is patch base.  
5. Human reviews and imports in Yandex Direct Commander.  
6. Apply bids per [BID-MANAGEMENT-RULES-v1.md](../../../freeze/ppc-exporter-production-baseline-v1/BID-MANAGEMENT-RULES-v1.md).

## Provenance

- **v0:** Copied from `incoming/orca-triumph-raw-pack/` during pack normalization (2026-05-20).  
- **v1:** Promoted to production baseline after full cycle ORCA → JSON → Exporter v1.2 → Commander → Human QA (2026-05-29).

## SAFE UNKNOWN

- Exact Yandex Direct UI version drift vs template columns — confirm at import time.  
- Whether all draft/active row examples remain valid for your account type — human check required.
