# CORVONERO — Direct Commander Import Instructions v5

**Status:** DRY-RUN ONLY — launch NOT authorized  
**Workbook:** `exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v5.xlsx`  
**Review workbook:** `exports/CORVONERO-CAMPAIGN-REVIEW-v5.xlsx`  
**Supersedes:** v4 (REJECTED — evidence QA failure)

---

## Current import model

| Parameter | Value |
|-----------|-------|
| Campaigns in file | **1** unified campaign |
| Active groups | 48 (markers `[C01]`–`[C08]`) |
| Keywords | **348** phrase-evidence-reviewed |
| Negative risk unresolved | **0** |
| Blocking collisions | **0** |
| Landing URLs | **PLANNED — PAGE NOT YET PUBLISHED** |
| Campaign split | **DEFERRED** |
| Moderation / launch | **DO NOT** send to moderation |

---

## Before import

1. Run ORCA v5 pipeline: `node tools/run-full-production-v5.mjs`
2. Export XLSX: `node tools/export-commander-xlsx-v5.cjs`
3. Generate review workbook: `node tools/generate-review-workbook-v5.cjs`
4. Regression: `node tools/regression-tests-v5.mjs`
5. Operator review: `exports/CORVONERO-CAMPAIGN-REVIEW-v5.xlsx` — all 27 evidence sheets

---

## v5 evidence requirements (mandatory PASS)

- 100% active phrases have phrase-specific semantic evidence (`semantic-evidence-review-v5.json`)
- Zero template-only active approvals
- Group reassignment log reconciled
- `negative-risk-resolution-v5.json`: HOLD=0, unresolved=0
- Collision summary `final_status=PASS`; literal collisions after = 0
- Ad evidence audit passed; no unsupported guarantee wording
- Report/export consistency passed
- No placeholder cells (`1234`, blank corrections for blocking findings)

---

## Commander dry-run steps

1. Open Yandex Direct Commander (desktop).
2. **File → Import → From file** — select `CORVONERO-YANDEX-DIRECT-COMMANDER-v5.xlsx`.
3. Use **dry-run / preview** — do **not** publish.
4. Log every import error and warning.
5. Verify: region NSO, manual CPC, unified UTM `corvonero_1c_search_nsk`, group markers `[C01]`–`[C08]`.
6. Cross-check keyword/group counts against review workbook **QA consistency** sheet.

---

## Manual setup (not in XLSX)

- Strategy, budget, Metrika, goals, business card — configure manually after operator approval.

---

## After dry-run gate

1. Operator sign-off on v5 Commander + evidence workbook
2. Landing copy from `production/landing-copy-handoff-v5.json` (**copy not started**)
3. Publish planned landing pages
4. Optional 8-campaign split (deferred)

**Launch remains NOT AUTHORIZED until operator explicitly approves post dry-run.**
