# Launch XLSX Export v1.3

**Date:** 2026-05-29  
**Lane:** ORCA Triumph Manipulator Search PPC  
**Status:** Export artifact generated — **not** launch approval

---

## Generated file

| Field | Value |
|-------|-------|
| **Path** | `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/output/triumph-sheet1-patch-launch-ready-v1.3.xlsx` |
| **Template SoT** | `assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx` |
| **JSON SoT** | `schema/instances/triumph-s-tier-draft-v1.json` |
| **Exporter** | ORCA Commander Transport Split **v1.3** |
| **Validation report** | `tools/validation-cli/output/validation-report.output.json` |

---

## Pipeline executed

| Step | Command | Result |
|------|---------|--------|
| 1 | `validation-cli` → `triumph-s-tier-draft-v1.json` | **PASS** (345 rules, `export_allowed: true`) |
| 2 | `npm run export:sheet1-patch:launch-ready-v1.3` | **SUCCESS** (84 rows, last row 99) |
| 3 | `npm run validate:launch-ready-v1.3` | **PASS** — Commander readiness **READY** |

---

## Entity counts (verified)

| Entity | Expected | Actual |
|--------|----------|--------|
| Groups | 12 | 12 |
| Ads | 20 | 20 |
| Keyword phrases | 64 | 64 |
| Total transport rows | 84 | 84 |
| Duplicate ad signatures | 0 | 0 |

---

## v1.3 delta vs v1.2

| Area | v1.2 | v1.3 |
|------|------|------|
| Template base | v0 (legacy path) | **template v1** |
| Manual search bids (col 54) | Not exported | **All 64 phrases** 400–600 ₽ |
| Group cross-negatives (col 68) | Not exported | **12 groups** route matrix + doctrine |
| Post-check | `validate:no-duplicate-ads-v1.2` | **`validate:launch-ready-v1.3`** (superset) |

---

## Boundaries

- Does **not** start ads, budgets, or campaigns in Yandex Direct  
- Does **not** replace human Commander import QA  
- Exporter remains transport-only; meaning SoT = JSON + freeze rules

---

## Operator

Run from `tools/exporter-cli`:

```bash
npm run export:sheet1-patch:launch-ready-v1.3
npm run validate:launch-ready-v1.3
```
