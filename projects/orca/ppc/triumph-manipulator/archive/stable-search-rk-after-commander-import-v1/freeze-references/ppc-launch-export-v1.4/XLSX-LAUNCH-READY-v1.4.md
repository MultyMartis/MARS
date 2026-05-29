# Launch XLSX Export v1.4

**Date:** 2026-05-29  
**Lane:** ORCA Triumph Manipulator Search PPC  
**Status:** Export artifact generated — **not** launch approval

---

## Generated file

| Field | Value |
|-------|-------|
| **Path** | `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/output/triumph-sheet1-patch-launch-ready-v1.4.xlsx` |
| **Template SoT** | `assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx` |
| **JSON SoT** | `schema/instances/triumph-s-tier-draft-v1.json` |
| **Exporter** | ORCA Commander Transport Split **v1.4** |
| **Validation report** | `tools/validation-cli/output/validation-report.output.json` |

---

## Pipeline executed

| Step | Command | Result |
|------|---------|--------|
| 1 | `validation-cli` → `triumph-s-tier-draft-v1.json` | **PASS** (345 rules, `export_allowed: true`) |
| 2 | `npm run export:sheet1-patch:launch-ready-v1.4` | **SUCCESS** (84 rows, last row 99) |
| 3 | `npm run validate:launch-ready-v1.4` | **PASS** — Commander readiness **READY** |

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

## v1.4 delta vs v1.3

| Area | v1.3 | v1.4 |
|------|------|------|
| Promotion URL (R11C5) | First group landing (wrong) | **Template root URL** |
| Metadata patch scope | 3 keys | **6 keys** (type, placement, currency, optimize, promotion, negatives) |
| Cross-negative syntax | Wildcards `*` | **Expanded stems + phrase forms** |
| Commander syntax gate | Not checked | **`commander_negative_syntax_pass`** |
| Template metadata diff | 1 cell | **0 cells** |

---

## Boundaries

- Does **not** start ads, budgets, or campaigns in Yandex Direct  
- Does **not** replace human Commander import QA  
- Budget / weekly cap — **SAFE UNKNOWN** in XLSX; operator sets in UI  

---

## Operator

Run from `tools/exporter-cli`:

```bash
npm run export:sheet1-patch:launch-ready-v1.4
npm run validate:launch-ready-v1.4
npm run audit:template-diff   # optional — compare vs template
```
