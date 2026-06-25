# CORVONERO — Direct Commander Import Instructions v7

**Status:** DRY-RUN AUTHORIZED — launch NOT authorized  
**Workbook:** `exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v7.xlsx`  
**Review workbook:** `exports/CORVONERO-CAMPAIGN-REVIEW-v7.xlsx`  
**Supersedes:** v6 Commander and Review (`REJECTED — COMMERCIAL SCOPE LOSS` / `SEMANTIC AND CONTROLLED-TEST DEFECTS`)

---

## Current import model

| Parameter | Value |
|-----------|-------|
| Campaigns in file | **1** unified campaign |
| Active groups | **48** (markers `[C01]`–`[C08]`) |
| Held groups (not exported) | **0** |
| Keywords | **311** (41 restored, 4 informational excluded) |
| Restored groups | **8** |
| Controlled tests | **27** phrase-specific hypotheses |
| Active informational leakage | **0** |
| Commercial seed loss | **0** |
| Negative risk unresolved | **0** |
| Blocking collisions | **0** |
| Landing URLs | **PLANNED — NOT PUBLISHED** |
| Campaign split | **DEFERRED** |
| Moderation / launch | **DO NOT** send to moderation |

---

## Before import

1. Run ORCA v7 pipeline: `node tools/run-full-production-v7.mjs`
2. Export XLSX: `node tools/export-commander-xlsx-v7.cjs`
3. Generate review workbook: `node tools/generate-review-workbook-v7.cjs`
4. Validate Commander XLSX: `node tools/validate-commander-xlsx-v7.cjs`
5. Operator review: `exports/CORVONERO-CAMPAIGN-REVIEW-v7.xlsx` — all 30 sheets

---

## v7 evidence requirements (mandatory PASS)

- Scope recovery package applied: `production/recovery/v7-production-input-package.json`
- Production Scope Recovery Gate: `PASS — V7 PRODUCTION AUTHORIZED`
- Operator service coverage: 31/31 families; commercial seed loss = 0
- Informational hard excludes: 4 phrases excluded; zero export leakage
- Controlled tests: phrase-specific hypotheses from `controlled-test-registry-v2.json`
- Collision summary `final_status=PASS`; blocking collisions = 0
- Unresolved unique negative risks = 0
- Ad evidence audit passed
- Report/export consistency passed
- Independent XLSX validation passed (Commander + Review)

---

## Commander dry-run steps

1. **Backup / sync** current Commander state (export existing campaigns if any).
2. Open Yandex Direct Commander (desktop).
3. **File → Import → From file** — select `CORVONERO-YANDEX-DIRECT-COMMANDER-v7.xlsx`.
4. Import as **one campaign** — do not split.
5. Use **preview / dry-run only** — do **not** send to server or moderation.
6. **Record every** Commander error and warning in `CORVONERO-COMMANDER-DRY-RUN-RESULT-TEMPLATE-v7.md`.
7. Verify:
   - Group markers `[C01]`–`[C08]` on all 48 exported groups
   - Eight restored groups present (CORV-G07-04, G05-06, G04-01/02/03, G01-02/04/06)
   - Region: Новосибирск и Новосибирская область
   - Campaign type: единая перфоманс-кампания / search
   - Bids: 311 keyword rows, no zero bids
   - No informational hard-exclude phrases in export
   - URLs: `https://lk.corvonero.ru/` with `utm_campaign=corvonero_1c_search_nsk`
8. Cross-check counts against review workbook **Commander row reconciliation** sheet.

---

## Manual settings (not in XLSX)

- Strategy, monthly budget, Metrika, goals, business card, final regions — configure manually after operator approval.

---

## After dry-run gate

1. Operator sign-off on v7 Commander + evidence workbook
2. Landing copy from `production/landing-copy-handoff-v7.json` (**copy not started**)
3. Publish planned landing pages
4. Optional 8-campaign split (deferred)

**Launch remains NOT AUTHORIZED until operator explicitly approves post dry-run and landing pages are published.**
