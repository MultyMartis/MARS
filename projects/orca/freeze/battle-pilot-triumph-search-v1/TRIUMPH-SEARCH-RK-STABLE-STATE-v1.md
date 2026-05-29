# Triumph Search RK Stable State v1

**Project:** Триумф Манипулятор — РК на поиске  
**Date:** 2026-05-30  
**Status:** **STABLE** — Commander import PASS — **not** launch approved

---

## Project identity

| Field | Value |
|-------|-------|
| **Pack path** | `projects/orca/ppc/triumph-manipulator/` |
| **Operational index** | [OPERATIONAL-INDEX.md](../../ppc/triumph-manipulator/OPERATIONAL-INDEX.md) |
| **Domain** | `https://manipulator-triumph.ru/` |
| **Region** | Краснодарский край |
| **Campaign type** | Search · Manual bids · Unified performance campaign |
| **Route count** | 12 groups · 20 ads · 64 keyword phrases |

---

## Source-of-truth stack

| Layer | Artifact | Status |
|-------|----------|--------|
| Doctrine | `doctrine/generation-logic-v0.md` | Frozen |
| Intent tiers | `research/intent-groups-v1.md` | Frozen |
| JSON instance | `schema/instances/triumph-s-tier-draft-v1.json` | Battle-stable |
| Validation | `tools/validation-cli/` → 345 rules PASS | Battle-stable |
| Exporter | `tools/exporter-cli/` v1.4 transport split | Battle-stable |
| Template | `assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx` | SoT |
| Export output | `tools/exporter-cli/output/triumph-sheet1-patch-launch-ready-v1.4.xlsx` | Generated (gitignored) |

---

## Entity inventory (frozen)

| Group ID prefix | Route | Ads | Keywords |
|-----------------|-------|-----|----------|
| grp_fc01–fc12 | 12 semantic routes | 20 total | 64 total |

Full route mapping: [freeze/route-family-freeze-v1/ROUTE-FAMILY-INDEX-v1.md](../route-family-freeze-v1/ROUTE-FAMILY-INDEX-v1.md)

---

## Export pipeline (reproduction)

```bash
# 1. Validate JSON
cd projects/orca/ppc/triumph-manipulator/tools/validation-cli
node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json

# 2. Export v1.4
cd ../exporter-cli
npm install   # if needed — not backed up
npm run export:sheet1-patch:launch-ready-v1.4
npm run validate:launch-ready-v1.4

# 3. Import in Direct Commander (human)
# File: output/triumph-sheet1-patch-launch-ready-v1.4.xlsx

# 4. Post-import checklist
# See: freeze/battle-pilot-triumph-search-v1/CAMPAIGN-SETTINGS-LAYER-v1.md
```

---

## Commander import state

| Gate | State |
|------|-------|
| Import structural | **PASS** |
| Entity counts | **PASS** (12/20/64) |
| URLs canonical | **PASS** |
| Cross-negatives | **PASS** (v1.4 syntax) |
| Duplicate ads | **PASS** (0) |
| Bids in UI | **PASS** (after manual strategy) |
| Budget set | **Pending** |
| Schedule set | **Pending** |
| Launch enabled | **No** |

---

## Stable backup location

Full project backup: [archive/stable-search-rk-after-commander-import-v1/](../../ppc/triumph-manipulator/archive/stable-search-rk-after-commander-import-v1/)

---

## Related freezes

| Freeze | Role |
|--------|------|
| [route-family-freeze-v1](../route-family-freeze-v1/) | Semantic 12-route family |
| [commander-url-sync-v1](../commander-url-sync-v1/) | URL canonical sync |
| [ppc-exporter-production-baseline-v1](../ppc-exporter-production-baseline-v1/) | Export governance |
| [ppc-launch-export-v1.4](../ppc-launch-export-v1.4/) | Battle export QA |
| [battle-pilot-triumph-search-v1/](.) | **This battle milestone** |

---

## Boundaries

- Stable state = **export + import path proven** — not live campaign  
- JSON instance is draft fixture — not launch-approved semantic lock  
- No runtime, no orchestration, no autonomous validation claimed
