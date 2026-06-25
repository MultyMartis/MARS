# Triumph Manipulator Production Pattern Audit — Corvonero v1

**Date:** 2026-06-22  
**Purpose:** Factual audit of Triumph production assets for Corvonero reuse  
**Method:** Repository file verification — not report-only citation

---

## Verified assets (exist on disk)

| Asset | Path | Verified |
|-------|------|----------|
| Commander template v1 (SoT) | `projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx` | **Yes** — 439 514 B |
| Commander template v0 (historical) | `.../triumph-manipulator-commander-template-v0.xlsx` | **Yes** — 454 360 B |
| Header map | `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/commander-header-map-v0.json` | **Yes** |
| Sheet index | `.../template-sheet-index-v0.json` | **Yes** |
| Exporter script | `.../sheet1-patch-export.js` | **Yes** |
| Cross-negative script | `.../cross-negative-matrix-v1.4.js` | **Yes** |
| Launch validation | `.../_validate-launch-ready-v1.4.js` | **Yes** |
| JSON instance (meaning SoT) | `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json` | Referenced in freeze — verify at 2C |
| Production baseline freeze | `projects/orca/freeze/ppc-exporter-production-baseline-v1/` | **Yes** |

---

## Production pipeline (Triumph — human-validated)

```text
ORCA JSON instance (meaning SoT)
  → validation-cli (human-triggered)
  → cross-negative matrix (mandatory pre-export)
  → hygiene audit checklist
  → Exporter v1.2 (sheet1-patch on template v1)
  → output/*.xlsx (gitignored disposable snapshot)
  → Direct Commander import (human)
  → bid calibration + QA (human)
```

**npm script (Triumph):** `export:sheet1-patch:full-cycle-v1.2`  
**Post-export QA:** `validate:no-duplicate-ads-v1.2`

---

## Schema / column contract (factual)

- **Single sheet «Тексты»** for combined campaign/group/keyword/ad/extensions (not multi-sheet entity export).  
- **78 header columns** at row 14; data from row 15.  
- **Campaign metadata** in rows 6–13 key-value block.  
- **Manual bids** col 54 «Ставка».  
- **Group negatives** col 68.  
- **No dedicated match-type column** — phrase-level encoding.  
- **Search-only:** ad type «Текстово-графическое»; image cols cleared.

Source: `commander-header-map-v0.json` + `template-sheet-index-v0.json` introspection artifacts.

---

## Semantic architecture pattern (Triumph)

| Layer | Triumph | Corvonero adaptation |
|-------|---------|---------------------|
| Campaigns | 1 search campaign (Krasnodar manipulator) | **8 campaigns** by service family |
| Route groups | 12 route slugs (zakaz, 5-tonn, bytovki, …) | **48 semantic ad groups** |
| Cross-negatives | Route-family matrix mandatory | [conflict-negative-matrix-v1.md](conflict-negative-matrix-v1.md) |
| Landing routing | URL registry sync freeze | [url-landing-map-v1.md](url-landing-map-v1.md) |
| Bid tiers | 400–600 ₽ anchor + 10–90 spread | [bidding-model-v1.md](bidding-model-v1.md) T1–T4 |

---

## Landing / copy pattern (Triumph)

| Artifact | Location | Corvonero note |
|----------|----------|----------------|
| Landing routing schema | `ppc/triumph-manipulator/schema/landing-routing-schema-v1.md` | Adapt for 31 LP IDs |
| Landing continuity rules | `ppc/triumph-manipulator/validation/landing-continuity-rules-v1.md` | Apply at Stage 3 |
| Word/docx landing specs | **SAFE UNKNOWN in repo** — Triumph used Tilda pages on live domain; no `.docx` found in Triumph tree | Corvonero Stage 3 creates `.md` + `.docx` per [landing-document-contract-v1.md](landing-document-contract-v1.md) |

---

## External storage

| Reference | Status |
|-----------|--------|
| MIG Wordstat Excel | `C:\AI MARS STORAGE\mig\corvonero\wordstat-2026-06\` — referenced in keyword_registry |
| Triumph output XLSX | Gitignored disposable — not in repo (by design) |

---

## Reuse decision for Corvonero

| Component | Reuse |
|-----------|-------|
| Template v1 transport shape | **Yes** — fork/copy as patch base |
| commander-header-map column names | **Yes** — verify no UI drift |
| sheet1-patch-export pattern | **Yes** — adapt for 8 campaigns |
| cross-negative-matrix logic | **Yes** — new Corvonero matrix |
| Triumph JSON instance | **No** — build Corvonero registry JSON |
| Triumph ads/copy | **No** — new Corvonero creatives |

---

## Gaps

- No Corvonero-specific exporter CLI yet — Stage 2C deliverable.  
- No pre-generated Corvonero XLSX — intentional for Stage 2A.  
- Landing Word docs not found in Triumph repo — Corvonero defines own Stage 3 contract.
