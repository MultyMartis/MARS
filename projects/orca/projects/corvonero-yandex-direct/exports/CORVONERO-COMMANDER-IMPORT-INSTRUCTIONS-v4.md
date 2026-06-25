# CORVONERO — Direct Commander Import Instructions v4

**Status:** DRY-RUN ONLY — launch NOT authorized  
**Workbook:** `exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v4.xlsx`  
**Review workbook:** `exports/CORVONERO-CAMPAIGN-REVIEW-v4.xlsx`  
**Supersedes:** v3 import instructions and v3 Commander file for operator review

---

## Current import model

| Parameter | Value |
|-----------|-------|
| Campaigns in file | **1** unified campaign |
| Active groups | 48 (markers `[C01]`–`[C08]`) |
| Keywords | **341** human-reviewed commercial phrases (364 v3 reviewed → 23 excluded) |
| Landing URLs | **PLANNED — PAGE NOT YET PUBLISHED** |
| Campaign split | **DEFERRED** |
| Moderation / launch | **DO NOT** send to moderation |

---

## Before import

1. Run ORCA v4 pipeline: `node tools/run-full-production-v4.mjs`
2. Export XLSX: `node tools/export-commander-xlsx-v4.cjs`
3. Generate review workbook: `node tools/generate-review-workbook-v4.cjs`
4. Validate: `node tools/validate-commander-xlsx-v4.cjs`
5. Regression: `node tools/regression-tests-v4.mjs`
6. Operator review: `exports/CORVONERO-CAMPAIGN-REVIEW-v4.xlsx` — verify **Semantic review**, **Collision summary**, **Collision findings**, **Collision passed samples**

---

## v4 evidence requirements

Unlike v3, validation **requires**:

- 100% semantic review coverage in `production/semantic-human-review-v4.json`
- Populated collision sheets in review workbook (not empty header-only)
- Ad certainty QA pass in `production/final-ad-registry-v4.json`

---

## Commander dry-run steps

1. Open Yandex Direct Commander (desktop).
2. **File → Import → From file** — select `CORVONERO-YANDEX-DIRECT-COMMANDER-v4.xlsx`.
3. Use **dry-run / preview** — do **not** publish.
4. Log every import error and warning.
5. Verify: region NSO, manual CPC, unified UTM `corvonero_1c_search_nsk`, group markers `[C01]`–`[C08]`.

---

## After dry-run gate

1. Operator sign-off on semantic review sheet
2. Landing copy from `production/landing-copy-handoff-v4.json` (copy **not** started)
3. Publish planned landing pages
4. Optional 8-campaign split (deferred)

**Launch remains NOT AUTHORIZED until operator explicitly approves post dry-run.**
