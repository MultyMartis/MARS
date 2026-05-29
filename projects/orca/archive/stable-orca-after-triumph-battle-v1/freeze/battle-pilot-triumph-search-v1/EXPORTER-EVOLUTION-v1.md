# Exporter Evolution v1

**Project:** Triumph Manipulator Search PPC  
**Scope:** Exporter transport split v1.2 → v1.4  
**Date:** 2026-05-30 (freeze summary)

---

## Version lineage

```
v0.x  — prototype transport (ExcelJS, sheet1 patch, forensics)
v1.0  — full-cycle export with validation binding
v1.1  — keyword×ad bug still present (108 rows, duplicate ads)
v1.2  — transport split — AD rows + KEYWORD rows (84 rows, 20 ads)
v1.3  — bid assignment + cross-negative matrix (wildcards)
v1.4  — metadata fidelity + Commander-safe minus syntax (battle import file)
```

---

## v1.2 — Transport split (duplicate ads fix)

**Problem:** `mapTemplateFillRows()` nested `for (ad) { for (kw) { push } }` — keyword×ad multiplication.

**Fix:** Separate AD rows and KEYWORD rows; no cross-multiplication.

| Metric | v1.1 | v1.2 |
|--------|------|------|
| Sheet1 data rows | 108 | **84** |
| Commander-equivalent ads | 108 (duplicate) | **20** |
| Keyword phrase rows | 0 (merged) | **64** |
| Duplicate ad signatures | 20 | **0** |

**Validation:** `npm run validate:no-duplicate-ads-v1.2` — PASS  
**Evidence:** [commander-transport-fix-v1/DUPLICATE-ADS-FIX-REPORT-v1.md](../commander-transport-fix-v1/DUPLICATE-ADS-FIX-REPORT-v1.md)

---

## v1.3 — Bids + cross-negatives

**Added:**

| Module | Role |
|--------|------|
| `bid-assignment-v1.3.js` | Default 400–600 ₽, within-group spread 10–90 ₽, zero bids prohibited |
| `cross-negative-matrix-v1.3.js` | Route-family cross-negative matrix per group |

**Validation:** `npm run validate:launch-ready-v1.3` — PASS (bids + negatives present)

**Known issue (fixed in v1.4):** Cross-negative wildcards (`бытовк*`, `контейнер*`) rejected by Commander.

**Evidence:** [ppc-launch-export-v1.3/BID-QA-v1.3.md](../ppc-launch-export-v1.3/BID-QA-v1.3.md), [ppc-launch-export-v1.3/CROSS-NEGATIVE-QA-v1.3.md](../ppc-launch-export-v1.3/CROSS-NEGATIVE-QA-v1.3.md)

---

## v1.4 — Metadata fidelity + minus syntax (battle file)

**Added / fixed:**

| Module | Role |
|--------|------|
| `template-campaign-metadata-v1.4.js` | 6-key metadata patch (type, placement, currency, optimize, promotion, negatives) |
| `cross-negative-matrix-v1.4.js` | Wildcard ban, stem expansion, phrase forms |
| `_validate-launch-ready-v1.4.js` | `commander_negative_syntax_pass` gate |

**v1.4 delta vs v1.3:**

| Area | v1.3 | v1.4 |
|------|------|------|
| Promotion URL (R11C5) | First group landing (wrong) | **Template root URL** |
| Metadata patch scope | 3 keys | **6 keys** |
| Cross-negative syntax | Wildcards `*` | **Expanded stems + phrases** |
| Commander syntax gate | Not checked | **`commander_negative_syntax_pass`** |
| Template metadata diff | 1 cell | **0 cells** |

**Validation:** `npm run validate:launch-ready-v1.4` — PASS  
**Battle import:** v1.4 XLSX — **PASS**

**Evidence:** [ppc-launch-export-v1.4/XLSX-LAUNCH-READY-v1.4.md](../ppc-launch-export-v1.4/XLSX-LAUNCH-READY-v1.4.md)

---

## Reproduction commands

From `ppc/triumph-manipulator/tools/exporter-cli/`:

```bash
# Prerequisites: validation-cli PASS on JSON
cd ../validation-cli && node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json

# Export v1.4 (battle artifact)
cd ../exporter-cli
npm run export:sheet1-patch:launch-ready-v1.4
npm run validate:launch-ready-v1.4
npm run audit:template-diff   # optional
```

Output: `output/triumph-sheet1-patch-launch-ready-v1.4.xlsx` (gitignored)

---

## SoT hierarchy (frozen)

| Layer | SoT |
|-------|-----|
| Meaning | `triumph-s-tier-draft-v1.json` + doctrine + validation rules |
| Export transport | Commander template v1 + Exporter v1.4 mapping |
| Bids | [BID-MANAGEMENT-RULES-v1.md](../ppc-exporter-production-baseline-v1/BID-MANAGEMENT-RULES-v1.md) |
| Cross-negatives | [CROSS-NEGATIVE-RULES-v1.md](../ppc-exporter-production-baseline-v1/CROSS-NEGATIVE-RULES-v1.md) |
| Excel output | Generated snapshot — **not** SoT |

---

## Boundaries

- Exporter remains **dumb transport** — no PPC logic in export layer  
- v1.4 is **approved for Triumph Search** — not generalized multi-project yet (P2)  
- Does **not** replace post-import Commander UI setup
