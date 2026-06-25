# ORCA Stage 2B–2D — Production Report — Корво Неро v1

**Date:** 2026-06-22  
**Project:** `corvonero-yandex-direct`  
**Deliverable:** import-ready Commander XLSX (structurally validated)

---

## Production counts

| Metric | Count |
|--------|------:|
| Campaigns | 8 |
| Ad groups | 48 |
| Active keywords | 349 |
| Excluded / deferred keywords | 2071 |
| Ads | 53 |
| Global negatives | 39 |
| Campaign-level negative tokens | 38 |
| Group cross-negative tokens | 162 |
| Landing URLs (planned) | 31 |
| XLSX data rows | 402 |
| Validation errors | 0 |
| Validation warnings | 0 |

### Bids by tier

| Tier | Keywords |
|------|--------:|
| T1 | 155 |
| T2 | 139 |
| T3 | 50 |
| T4 | 5 |

---

## Stage status

| Stage | Status |
|-------|--------|
| ORCA Stage 2A | COMPLETE |
| ORCA Stage 2B | COMPLETE |
| ORCA Stage 2C | COMPLETE |
| ORCA Stage 2D | COMPLETE WITH MANUAL IMPORT CHECK REQUIRED |
| Direct Commander XLSX | GENERATED AND STRUCTURALLY VALIDATED |
| Landing copy handoff | READY |
| Landing pages | NOT CREATED |
| Launch readiness | BLOCKED BY LANDING PUBLICATION AND MEASUREMENT CHECK |
| Campaign launch | NOT AUTHORIZED |

---

## Pipeline

```text
MIG keyword_registry.json (2384)
  → run-full-production.mjs (classify, assign, ads, bids, negatives)
  → direct-commander-production-dataset-v1.json
  → export-commander-xlsx.cjs (Triumph template patch + row extend)
  → CORVONERO-YANDEX-DIRECT-COMMANDER-v1.xlsx
  → validate-commander-xlsx.cjs
```

---

## Key outputs

| Artifact | Path |
|----------|------|
| Final keywords | `production/final-keyword-registry-v1.json` |
| Final negatives | `production/final-negative-registry-v1.json` |
| Final ads | `production/final-ad-registry-v1.json` |
| URL/UTM | `production/final-url-utm-registry-v1.json` |
| Commander dataset | `production/direct-commander-production-dataset-v1.json` |
| XLSX | `exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v1.xlsx` |
| Validation | `production/validation/direct-commander-xlsx-validation-v1.json` |
| Import instructions | `exports/CORVONERO-COMMANDER-IMPORT-INSTRUCTIONS-v1.md` |
| Landing handoff | `production/landing-copy-handoff-v1.json` |

---

## Remaining manual checks

1. Commander UI import dry-run (operator)
2. Split 48 groups into 8 campaigns post-import (template single metadata block)
3. Confirm campaign type literal in account UI
4. Metrika / goals — SAFE UNKNOWN
5. Publish 31 landing pages before moderation

---

## Next gate

**OPERATOR REVIEW OF DIRECT COMMANDER XLSX AND AUTHORIZATION TO START LANDING COPY PRODUCTION**

---

## Git

No commit / no push performed (per task).
