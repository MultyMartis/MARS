# CORVONERO — Direct Commander Import Instructions v6

**Status:** DRY-RUN AUTHORIZED — launch NOT authorized  
**Workbook:** `exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v6.xlsx`  
**Review workbook:** `exports/CORVONERO-CAMPAIGN-REVIEW-v6.xlsx`  
**Supersedes:** v5 Commander and Review (`REJECTED — SUPERSEDED BY V6 PRODUCTION`)

---

## Current import model

| Parameter | Value |
|-----------|-------|
| Campaigns in file | **1** unified campaign |
| Active groups | **40** (markers `[C01]`–`[C08]`) |
| Held groups (not exported) | **8** |
| Keywords | **274** (74 v5 exclusions applied) |
| Controlled tests | **27** justified |
| Education/career leakage | **0** |
| Negative risk unresolved | **0** |
| Blocking collisions | **0** |
| Landing URLs | **PLANNED — PAGE NOT YET PUBLISHED** |
| Campaign split | **DEFERRED** |
| Moderation / launch | **DO NOT** send to moderation |

---

## Before import

1. Run ORCA v6 pipeline: `node tools/run-full-production-v6.mjs`
2. Export XLSX: `node tools/export-commander-xlsx-v6.cjs`
3. Generate review workbook: `node tools/generate-review-workbook-v6.cjs`
4. Validate Commander XLSX: `node tools/validate-commander-xlsx-v6.cjs`
5. Operator review: `exports/CORVONERO-CAMPAIGN-REVIEW-v6.xlsx` — all 28 sheets

---

## v6 evidence requirements (mandatory PASS)

- Repair package applied: `production/repair/v6-production-input-package.json`
- V5 QA Repair Gate v2: `PASS — V6 PRODUCTION AUTHORIZED`
- Career/education exclusions: 4 phrases excluded; zero export leakage
- Controlled tests: hypothesis + evaluation rule for each retained test
- `v5-negative-resolution-final.json`: SAFE — PROVEN evidence; unresolved=0
- Exact collision actions: 20/20 complete
- Collision summary `final_status=PASS`; literal collisions after = 0
- Ad evidence audit passed; no unsupported guarantee wording
- Report/export consistency passed (pair-layer vs unique-layer reconciled)
- Independent XLSX validation passed

---

## Commander dry-run steps

1. **Backup / sync** current Commander state (export existing campaigns if any).
2. Open Yandex Direct Commander (desktop).
3. **File → Import → From file** — select `CORVONERO-YANDEX-DIRECT-COMMANDER-v6.xlsx`.
4. Import as **one campaign** — do not split.
5. Use **preview / dry-run only** — do **not** send to server or moderation.
6. **Record every** Commander error and warning in `CORVONERO-COMMANDER-DRY-RUN-RESULT-TEMPLATE-v6.md`.
7. Verify:
   - Group markers `[C01]`–`[C08]` on all exported groups
   - Region: Новосибирск и Новосибирская область
   - Campaign type: единая перфоманс-кампания / search
   - Strategy and budget placeholders (manual post-import)
   - Bids: 274 keyword rows, no zero bids
   - Group and global negatives present; no education phrases
   - URLs: `https://lk.corvonero.ru/` with `utm_campaign=corvonero_1c_search_nsk`
8. Cross-check counts against review workbook **Commander row reconciliation** sheet.

---

## Manual settings (not in XLSX)

- Strategy, budget, Metrika, goals, business card — configure manually after operator approval.

---

## After dry-run gate

1. Operator sign-off on v6 Commander + evidence workbook
2. Landing copy from `production/landing-copy-handoff-v6.json` (**copy not started**)
3. Publish planned landing pages
4. Optional 8-campaign split (deferred)

**Launch remains NOT AUTHORIZED until operator explicitly approves post dry-run and landing pages are published.**
