# CORVONERO COMMANDER CT-6 CA-01 — Local Import Protocol v1

**Status:** READY FOR OPERATOR  
**Scope:** CA-01 only — local Commander import test  
**Date:** 2026-06-30

---

## Authority

| Checkpoint | Commit |
|------------|--------|
| CT-4 final authority | `8943e07e5f6b45d8e6cfd209a30cac55e2f0bb86` |
| CT-5 generation checkpoint | `880ca442d7dd25a74ed2c1fd83e4a11fecee8dc1` |
| Current branch | `mars/canonical-post-recovery` |

---

## Filesystem preflight — PASS

| Check | Result |
|-------|--------|
| Drive | `X:` |
| Volume label | `AI WS` |
| Repository | `X:\AI MARS\` |
| Storage | `X:\AI MARS STORAGE\` |

---

## Binding source — hash verified PASS

| Field | Value |
|-------|-------|
| File | `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-COMMANDER-CT5-FINAL-2026-06-30\CORVONERO-CA-01-PROGRAMMIST-1S-COMMANDER-IMPORT-v2.xlsx` |
| SHA-256 | `6b0894fbd49f19c20b9b10de830d2ab6ce4a675b0cb61603c1f0d1d5ebb24cd2` |
| Recalculated | MATCH — do not modify or resave |

---

## Expected CA-01 structure

| Metric | Expected |
|--------|----------|
| Campaigns | 1 |
| Groups | 7 |
| Keyword phrases | 339 |
| Primary ads | 7 |
| Max phrases in one group | ≤ 200 (max in XLSX: 144) |
| Bid | 500 RUB |
| Region | Новосибирская область |
| Organization | blank |
| Sitelinks | omitted |

---

## Forbidden in this task

- Server upload / sync with Yandex Direct
- Campaign launch or moderation submit
- Import of CA-02 through CA-05
- API access, semantic execution, OpenRouter
- Autonomous Commander UI control
- Modifying CT-4 authority or regenerating XLSX
- Git commit or push

---

## Part 1 — Clean local test boundary

**Operator must confirm before import:**

1. Commander version: _______________
2. Local account/client name: _______________
3. Existing campaigns before import: _______________
4. Existing groups before import: _______________
5. Local test area empty or isolated: YES / NO

**Requirements:**

- Prefer new empty local Commander account/container or clearly isolated test campaign tree
- Do **not** import into existing production campaign
- Do **not** merge with previous CA-01 v1 manual test

**If isolation cannot be proven:** STOP — COMMANDER LOCAL TEST BOUNDARY NOT CLEAN

Record boundary state in `CORVONERO-COMMANDER-CT6-CA01-IMPORT-PROTOCOL-v1.json` → `part1_clean_boundary`.

---

## Part 2 — Operator action sequence

Cursor prepares protocol and reconciles evidence only. **Operator performs:**

1. Open Yandex Direct Commander
2. Select isolated local test account
3. **File → Import from file** (or equivalent)
4. Select **only** the binding CA-01 XLSX above
5. Review import preview — record in PREVIEW receipt
6. Confirm **local import only**
7. At every dialog offering sync/send/upload: **CANCEL / DO NOT SEND**

---

## Part 3 — Pre-import preview capture

Before confirming import, record Commander preview:

| Field | Expected |
|-------|----------|
| Campaigns | 1 |
| Groups | 7 |
| Phrases | 339 |
| Ads | 7 |
| Region replacement | NONE |
| Organization lookup error | NONE |
| Groups over 200 | NONE |

**Watch for v1 defects:**

- Phrase count larger than expected
- Region replaced with «Все»
- Organization ID not found
- Group exceeding 200 phrases

If preview phrase count differs, record exact value and all messages. Do not cancel unless import would be unsafe.

Save to: `CORVONERO-COMMANDER-CT6-CA01-IMPORT-PREVIEW-v1.md` / `.json`  
Screenshots: `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-COMMANDER-CT6-CA01-EVIDENCE-2026-06-30\`

---

## Parts 4–13 — Post-import verification

After local import, complete:

- `CORVONERO-COMMANDER-CT6-CA01-LOCAL-RESULT-v1.md` / `.json`
- `CORVONERO-COMMANDER-CT6-CA01-FORENSIC-COMPARISON-v1.md` / `.json`

Use group comparison table and phrase manifest in forensic JSON (339 phrases from binding XLSX).

---

## Expected group table (CT-4 authority)

| group_id | Expected name | Phrases | Group negatives (XLSX transport) |
|----------|---------------|---------|----------------------------------|
| ca-01-direct-service-order | Программист / специалист 1С — direct service order | 4 | (none) |
| ca-01-find-hire-specialist | … find / hire specialist | 14 | `-"программист 1с"` |
| ca-01-price-intent | … Price / cost intent | 23 | (none) |
| ca-01-remote-freelance-specialist | … remote / freelance / local | 12 | (none) |
| ca-01-specialist-by-product | … product / role variants | 10 | (none) |
| ca-01-specialist-extended | … extended specialist queries | 132 | `-нужен` |
| ca-01-specialist-search | … core specialist search | 144 | `-стоимость -найти` |

---

## Campaign negatives (CA-01)

Expected 11 terms from `CORVONERO-CT4-CAMPAIGN-NEGATIVES-v1.json`:

`вакансия`, `работа программистом`, `резюме`, `сертификация`, `кряк`, `зарплата`, `стань программистом`, `становится программистом`, `скачать`, `купить 1с`, `лицензия 1с`

Cross-campaign negatives: **NOT APPLIED** — absence is not an error.

---

## Callouts (CA-01)

Expected (col 67, `;;` separated):

`Удалённо по России;;Выезд в Новосибирске;;Работа по договору;;Минимальный заказ 2 часа`

---

## Ad copy checkpoints

| Check | Expected |
|-------|----------|
| Corrected text «Настроим и доработаем 1С, исправим ошибки и отчёты. Удалённо по РФ, по договору.» | 1 occurrence (ca-01-specialist-extended) |
| Forbidden headline «Найдём программиста 1С под задачу» | 0 occurrences |
| Forbidden organization ID `29500847237` | 0 occurrences |

---

## URL / UTM (all 7 ads)

- Base: `https://lk.corvonero.ru/programmist-1s/`
- `utm_source=yandex`
- `utm_medium=cpc`
- `utm_campaign=corv_programmist_1s`
- `utm_content=<group_slug>` per group
- No `utm_term`, no `{keyword}`

---

## Evidence receipts

| Receipt | Path |
|---------|------|
| Protocol | `pilots/corvonero/CORVONERO-COMMANDER-CT6-CA01-IMPORT-PROTOCOL-v1.*` |
| Preview | `pilots/corvonero/CORVONERO-COMMANDER-CT6-CA01-IMPORT-PREVIEW-v1.*` |
| Local result | `pilots/corvonero/CORVONERO-COMMANDER-CT6-CA01-LOCAL-RESULT-v1.*` |
| Forensic | `pilots/corvonero/CORVONERO-COMMANDER-CT6-CA01-FORENSIC-COMPARISON-v1.*` |
| Report | `reports/REPORT-corvonero-commander-ct6-ca01-local-import-test-v1.md` |
| Screenshots | `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-COMMANDER-CT6-CA01-EVIDENCE-2026-06-30\` |

---

## Verdict

**Pending operator import.** Final verdict recorded in report after Parts 1–13 complete.
