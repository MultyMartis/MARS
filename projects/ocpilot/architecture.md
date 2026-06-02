# OCPilot Architecture (Documentation)

**Status:** documented — **BOUNDARY ONLY**; no runtime implementation claimed in-repo.

## Position in MARS

```
MARS Core (HITL, REPORT, SAFE UNKNOWN, lanes)
        │
        ├── CMS / Ecommerce Pilots (family classification)
        │     ├── WPilot ──────── WordPress bridge (sibling)
        │     ├── OCPilot ─────── OpenCart/ocStore bridge (standalone)
        │     ├── MODxPilot ───── possible future
        │     └── CustomSitePilot ─ possible future
        │
        └── ORCA, Factory, … (other programs — not components of OCPilot)
```

See [cms-ecommerce-pilots-family.md](cms-ecommerce-pilots-family.md). **JoomlaPilot is not planned.**

**Incorrect model:** `WPilot + ORCA + Survivability = OCPilot`  
**Correct model:** `OCPilot = standalone OpenCart bridge`; may **reuse patterns** from siblings, family layer, and governance.

## What OCPilot is (architectural)

| Layer | Role |
|-------|------|
| **Documentation & workflows** | Charters, indexes, templates, site folders |
| **Human-supervised bridge intent** | Inspect OpenCart files/DB shape; plan catalog/theme changes |
| **Versioned baseline discipline** | `baselines/<version>/` vs `sites/<site>/` custom delta |
| **Expanded site analysis** | OpenCart-specific folders under each `sites/<slug>/` |
| **Shared access patterns** | [shared/external-access-patterns/](../../shared/external-access-patterns/README.md) — not WPilot-owned |
| **Battle pilot discipline** | Read-only first pilot; freeze lessons under `freeze/` |

## What OCPilot is not (architectural)

- Not a child package of WPilot.
- Not ORCA (PPC) — only battle-pilot **workflow pattern**.
- Not mars-survivability — only backup/rollback **discipline pattern**.
- Not MARS runtime orchestration.
- Not an autonomous CMS/ecommerce agent fleet.

## Pattern reuse (explicit, non-inheritance)

| Source | Pattern | OpenCart note |
|--------|---------|---------------|
| CMS/Ecommerce Pilots family | Shared access safety, passports, QA | [cms-ecommerce-pilots-family.md](cms-ecommerce-pilots-family.md) |
| shared/external-access-patterns | Browser, FTP, PMA gates | Human-supervised; no automation claimed |
| WPilot | Read-only → scoped write → dry-run → rollback | Routes: `catalog/`, `admin/`, `system/` — not WP paths |
| ORCA | Battle pilot, freeze, stop-when-enough | First pilot: read-only dealership audit |
| mars-survivability | Risk classes, snapshots, protected zones | Apply to `sites/` backup folders — human-operated |
| MARS Core | HITL, REPORT, SAFE UNKNOWN | Default for all runs |

## Logical components (planned, not implemented)

| Component | Phase | Note |
|-----------|-------|------|
| Versioned baseline store | Run 2+ | `baselines/opencart-*`, `baselines/ocstore-*` |
| Site workspace + analysis zones | Run 3+ | Per-site under `sites/` |
| Inspection pipeline | Run 4–5 | Templates + human execution |
| Catalog import planner | Run 6 | Planning docs only until charter |
| Theme/controller change planner | Run 7 | Requires rollback contract |

## SAFE UNKNOWN

- Whether a future OpenCart extension/plugin bridge will exist — unknown until separate implementation charter.
- Exact ocMod/vQmod tooling per site — unknown until inspection.
- Whether MODxPilot or CustomSitePilot will be chartered — unknown.
