# CORVONERO — Direct Commander Import Instructions v3

**Status:** DRY-RUN ONLY — launch NOT authorized  
**Workbook:** `exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v3.xlsx`  
**Supersedes:** v1, v2 import instructions

---

## Current import model

| Parameter | Value |
|-----------|-------|
| Campaigns in file | **1** unified campaign |
| Active groups | 48 (markers `[C01]`–`[C08]`) |
| Keywords | 364 commercial phrases |
| Landing URLs | **PLANNED — PAGE NOT YET PUBLISHED** |
| Campaign split | **DEFERRED** — markers preserve future 8-campaign split |
| Moderation / launch | **DO NOT** send to moderation |

---

## Before import

1. Run ORCA v3 pipeline: `node tools/run-full-production-v3.mjs`
2. Export XLSX: `node tools/export-commander-xlsx-v3.cjs`
3. Validate: `node tools/validate-commander-xlsx-v3.cjs`
4. Regression: `node tools/regression-tests-v3.mjs`
5. Review operator workbook: `exports/CORVONERO-CAMPAIGN-REVIEW-v3.xlsx`

---

## Commander dry-run steps

1. Open Yandex Direct Commander (desktop).
2. **File → Import → From file** — select `CORVONERO-YANDEX-DIRECT-COMMANDER-v3.xlsx`.
3. Choose **dry-run / preview** if available — do **not** publish.
4. Record every import error and warning in operator log.
5. Manually verify after preview:
   - Campaign type: Единая перфоманс-кампания / search placement
   - Region: Новосибирск и Новосибирская область
   - Schedule: Mon–Fri 08:00–20:00 (recommended)
   - Strategy: manual CPC
   - Budget: align with operator plan (~100 000 ₽/month context)
   - Metrika counter + goals: **configure post-import** (SAFE UNKNOWN in repo)
   - Business card / extensions: verify sitelinks and callouts render

---

## Known v3 constraints

- All landing URLs point to `https://lk.corvonero.ru/…` — pages **not published** yet.
- Unified `utm_campaign=corvonero_1c_search_nsk`; `utm_content=<group_id>`; `utm_term={keyword}`.
- Group names include direction markers for future split — do not rename before split gate.
- v1 and v2 XLSX remain on disk for audit — import **v3 only** for next review cycle.

---

## After dry-run gate

1. Operator review of `CORVONERO-CAMPAIGN-REVIEW-v3.xlsx`
2. Landing copy from `production/landing-copy-handoff-v3.json`
3. Publish 31 planned landing pages
4. Optional 8-campaign split + separate XLSX (deferred)

**Launch remains NOT AUTHORIZED until operator explicitly approves post dry-run.**
