# REPORT — КОРВО НЕРО — DIRECT V2 CLEAN ROOM SEMANTIC CORE V1

**Date:** 2026-06-22  
**Branch:** `mars/post-cycle8-live-tests` @ `e70e67a`  
**Gate:** `READY FOR OPERATOR SEMANTIC REVIEW`

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Git branch | `mars/post-cycle8-live-tests` |
| HEAD | `e70e67a` |
| Original MIG session | **EXISTS** — `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/` |
| Operator intake evidence | **EXISTS** — `workspaces/corvonero-yandex-direct/CORVONERO-BUSINESS-INTAKE-v1.md` |
| ORCA Production Contract | **EXISTS** — `projects/orca/contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md` |
| Old Corvonero production | **EXISTS** — forbidden as semantic source |
| Campaign / Commander / import / commit / push | **NOT AUTHORIZED** |
| Unrelated WIP | **UNTOUCHED** (ocpilot, fp-0002, recovery-temp, etc.) |

---

## 2. Clean-Room Decision Registered

Операторское решение зафиксировано: Corvonero Direct v1–v7.1 признаны построенными по неправильной последовательности. Новая линия — `corvonero-direct-v2-clean-room` — без наследования семантических решений.

---

## 3. Allowed Sources

- Operator business inputs (intake v1)
- Original MIG Wordstat Pass A (`wordstat-pass-a-normalized.json`, 18 XLSX via MARS Storage index)
- Universal ORCA contract and invariants
- Triumph-derived methodology (laws only)

Pass B **не использовался**.

---

## 4. Forbidden Sources

Denylist в `authority/corvonero-direct-v2-source-authority-manifest-v1.json`. Pipeline **не читал** `corvonero-yandex-direct/production/`.

---

## 5. New Workspace

`projects/orca/projects/corvonero-direct-v2-clean-room/` — независимый контур с полной структурой authority / intake / mig-source / semantic-core / validation / artifacts / tools / reports.

---

## 6. Business Intake

- `intake/CORVONERO-DIRECT-V2-BUSINESS-INTAKE-v1.md`
- `intake/corvonero-direct-v2-business-intake-v1.json`

Восстановлены: компания, аудитория, география, модель оказания, цена, минимум, бюджет, конфигурации 1С, запреты на выдуманные claims, SAFE UNKNOWN (НДС, SLA, партнёрство 1С и др.).

---

## 7. Service Scope

- `intake/CORVONERO-DIRECT-V2-SERVICE-SCOPE-v1.md`
- `intake/corvonero-direct-v2-service-scope-v1.json`

**34** clean-room service ID (`CR2-SVC-001` … `CR2-SVC-034`). Приоритет между услугами **не назначен**. Рекламные группы **не созданы**.

---

## 8. MIG Corpus Ingest

| Metric | Value |
|--------|-------|
| Wordstat files (Pass A) | 18 |
| Raw rows read | 2399 |
| Empty rows | 0 |
| Unique raw phrases | 2370 |
| Duplicate raw keys | 29 |

Ledger: `mig-source/mig-wordstat-source-ledger-v1.json`

---

## 9. Normalization

`semantic-core/corvonero-normalized-corpus-v1.json` — детерминированная нормализация (trim, lowercase, ё→е, punctuation, tokens, dedup key, anomaly flags). Фразы **не переписывались** семантически.

Tool: `tools/normalize-mig-corpus.mjs` → `tools/run-clean-room-semantic-pipeline-v1.mjs`

---

## 10. Deduplication

| Metric | Value |
|--------|-------|
| Raw ledger rows | 2399 |
| Unique normalized phrases | 2368 |
| Duplicate clusters | 31 |
| Canonical entities | 2368 |

Registry: `semantic-core/corvonero-canonical-phrase-registry-v1.json`

---

## 11. Intent Screening

2368 фраз — first-pass screening (14 классов). **Нет** финальных ACTIVE/EXCLUDE.

Артефакт: `semantic-core/corvonero-intent-screening-v1.json`

---

## 12. Commercial Eligibility

Phrase-specific eligibility для всего корпуса. Решения **не** групповые.

Артефакт: `semantic-core/corvonero-commercial-eligibility-v1.json`

---

## 13. Service Mapping

Только ELIGIBLE и CONTROLLED-TEST кандидаты. Mapping **≠** group decision.

Артефакт: `semantic-core/corvonero-phrase-to-service-map-v1.json`

---

## 14. Cluster Discovery

**10** cluster candidates (не финальные ad groups).

Артефакт: `semantic-core/corvonero-commercial-cluster-candidates-v1.json`

---

## 15. Negative Candidate Discovery

Global, semantic exclusion и boundary candidates — статус CANDIDATE / SAFE CANDIDATE / OPERATOR REVIEW. Финальные минус-фразы **не созданы**.

Артефакт: `semantic-core/corvonero-negative-candidate-registry-v1.json`

---

## 16. Service Demand Coverage

34 услуги проанализированы. **6** услуг без mapped commercial phrases — `operator_seed_needed: true`:

- CR2-SVC-012 Расчёт себестоимости в 1С
- CR2-SVC-013 Планирование закупок в 1С
- CR2-SVC-014 Платёжный календарь в 1С
- CR2-SVC-020 Перенос данных в 1С
- CR2-SVC-021 Миграция данных 1С
- CR2-SVC-027 Восстановление работы 1С

Артефакт: `semantic-core/corvonero-service-demand-coverage-v1.json`

---

## 17. Semantic Core Candidate

`semantic-core/corvonero-direct-semantic-core-candidate-v1.json`

| Bucket | Count |
|--------|-------|
| Eligible commercial (total) | 1892 |
| — of which narrow | 590 |
| Controlled-test candidates | 17 |
| Excluded | 200 |
| Holds / unknowns | 259 |

**Нет:** campaign IDs, ad groups, ads, bids, URLs, UTM, Commander rows.

---

## 18. Validation Results

| Validation | Overall |
|------------|---------|
| Source validation | **PASS** |
| Integrity validation | **PASS** |

Все raw MIG rows учтены; forbidden production не использовался; counts сходятся.

---

## 19. Operator Review Workbook

`semantic-core/CORVONERO-DIRECT-V2-SEMANTIC-CORE-REVIEW-v1.xlsx`

18 листов: Summary, Source authority, Business intake, Service scope, MIG ledger, Canonical phrases, Intent screening, Eligible commercial, Narrow commercial, Controlled-test, Exclusions, Holds, Mapping, Clusters, Negatives, Coverage, Validation, Operator decisions.

**Не Commander file.**

---

## 20. Semantic Core Gate

`validation/direct-semantic-core-gate-v1.json` → **`READY FOR OPERATOR SEMANTIC REVIEW`**

Campaign production / Commander / launch — **NOT AUTHORIZED**.

---

## 21. Old Branch Status

`projects/orca/projects/corvonero-yandex-direct/PROJECT.md` обновлён:

- v1–v7.1 = **HISTORICAL DIAGNOSTIC — NOT SEMANTIC SOURCE**
- Direct V2 Clean Room = **ACTIVE** line
- Старые артефакты сохранены

---

## 22. Project Map Updates

`projects/orca/OPERATIONAL-INDEX.md` — зарегистрирован `corvonero-direct-v2-clean-room` (ACTIVE); `corvonero-yandex-direct` помечен historical.

---

## 23. Files Created or Changed

**Created:** `projects/orca/projects/corvonero-direct-v2-clean-room/` (38+ artefacts including XLSX)

**Changed:**

- `projects/orca/projects/corvonero-yandex-direct/PROJECT.md`
- `projects/orca/OPERATIONAL-INDEX.md`

---

## 24. Git Status

Clean-room locus: **untracked** (`??`). Modified: OPERATIONAL-INDEX, corvonero-yandex-direct PROJECT.md. **No commit. No push.**

**Future selective checkpoint plan (not executed):**

1. Stage only `projects/orca/projects/corvonero-direct-v2-clean-room/`
2. Stage `projects/orca/projects/corvonero-yandex-direct/PROJECT.md` + `projects/orca/OPERATIONAL-INDEX.md`
3. Optional: reusable pipeline tools under clean-room `tools/`
4. Exclude unrelated WIP (ocpilot, fp-0002, recovery-temp)

---

## 25. Remaining Operator Decisions

1. Review **1892** eligible + **17** controlled-test + **259** holds in XLSX
2. Confirm or override phrase-level eligibility
3. Resolve **6** services needing operator seed
4. Approve cluster candidates before any campaign architecture
5. Review negative candidates (global / boundary)
6. Regional Pass B — **SAFE UNKNOWN** for demand frequency (not in this task)

---

## 26. Next Gate

**OPERATOR REVIEW** of `CORVONERO-DIRECT-V2-SEMANTIC-CORE-REVIEW-v1.xlsx`

---

## 27. Stop Condition

| Item | Status |
|------|--------|
| Old v1–v7.1 | `HISTORICAL DIAGNOSTIC — NOT SEMANTIC SOURCE` |
| Direct V2 Clean Room | `ACTIVE` |
| MIG corpus | `INGESTED` |
| Semantic processing | `COMPLETE FOR OPERATOR REVIEW` |
| Semantic Core Candidate v1 | `GENERATED` |
| Campaign architecture | `NOT STARTED` |
| Advertising groups | `NOT STARTED` |
| Ads | `NOT STARTED` |
| Negatives | `CANDIDATES ONLY` |
| Commander XLSX | `NOT CREATED` |
| Import | `NOT AUTHORIZED` |
| Launch | `NOT AUTHORIZED` |
| Next gate | `OPERATOR SEMANTIC REVIEW` |

---

*End of report — Corvonero Direct V2 Clean Room Semantic Core v1*
