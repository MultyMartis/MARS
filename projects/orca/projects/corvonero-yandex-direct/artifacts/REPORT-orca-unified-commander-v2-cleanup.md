# REPORT — КОРВО НЕРО — UNIFIED COMMANDER XLSX V2 CLEANUP

**Дата:** 2026-06-22  
**Git branch:** `mars/post-cycle8-live-tests` @ `bf313e4`  
**Статус:** GENERATED AND STRUCTURALLY VALIDATED

---

## 1. Preflight

| Проверка | Результат |
|----------|-----------|
| `git branch` | `mars/post-cycle8-live-tests` |
| `git rev-parse HEAD` | `bf313e4` |
| v1 XLSX на диске | да — 402 data rows, 349 KW, 48 groups, 53 ads |
| v1 validation | STRUCTURALLY_VALIDATED (2026-06-21) |
| MIG keyword registry | `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/keyword_registry.json` |

Прочитаны: dataset v1, registries v1, architecture, bidding model, format contract, export/validate scripts.

---

## 2. Unified Campaign Decision

- **Одна кампания** в XLSX v2 (metadata block × 1)
- **48 групп** — все активны, held groups: **0**
- Маркеры `[C01]`–`[C08]` в начале каждого названия группы — **100%** (verified)
- `utm_campaign=corvonero_1c_search_nsk` — единый
- Разделение на 8 кампаний — **DEFERRED**

---

## 3. V1 Forensic Findings

| Проблема v1 | Подтверждение |
|-------------|---------------|
| DIY/informational среди активных KW | 12+ фраз с «как настроить», 3 regulatory aut parts, 15+ medicine regulatory |
| Слабая global minus «работа» | блокировала бы «работа с маркировкой» — исправлено multiword employment |
| Unsupported ad claims | «Под ключ» (5 ads), «Срочно восстановим», «Быстро и точно» |
| Seed padding до 5–8 фраз | искусственное наполнение тонких групп |
| Group naming без `[Cxx]` | `CORV-C01 — …` вместо операторского маркера |
| Per-campaign UTM в ads | 8 разных utm_campaign вместо unified |

---

## 4. Keyword Review

- Классифицировано: **2420** MIG phrases + operator seeds
- Активных v2: **341** (v1: 349)
- Исключено v2: **2081+**
- KEEP_TEST: **0** (test-tier через down-tier при mixed)

### Распределение по группам

| Band | Groups |
|------|--------|
| 1 phrase | 12 |
| 2 phrases | 11 |
| 3–4 phrases | 6 |
| 5–9 phrases | 7 |
| 10+ phrases | 12 |

---

## 5. Removed and Deferred Keywords

**−8 net от v1** (45 removed, core operator seeds restored where missing)

Ключевые исключения:
- Все operator explicit list (DIY marking, print forms, aut parts regulatory, training)
- «как стать программистом 1с», «программист 1с hh», «программист 1с бесплатно»
- Regulatory: «лекарства подлежащие маркировке», «какие автозапчасти подлежат…»
- DIY: «как настроить маркировку в 1с …», «как изменить печатную форму»

Полный diff: `production/keyword-v1-to-v2-diff.md`

---

## 6. Group Viability

| Status | Count |
|--------|-------|
| ACTIVE | 36 |
| ACTIVE NARROW | 12 |
| HOLD | 0 |
| MERGE | 0 |

Все 48 групп архитектуры сохранены; все 48 экспортированы (≥1 commercial phrase each).

---

## 7. Global Negatives

- **57 tokens** (v1: 39)
- Employment: multiword-safe (`работа программист`, `работа 1с`, …) — bare «работа» убрано
- Training, download, DIY/informational расширены
- Не минусуются глобально: «как», «настроить», «ошибка», «обновление», «удалённо»

Registry: `production/final-negative-registry-v2.json`

---

## 8. Direction-Level Negatives

- **81 tokens** across 8 directions
- Эмулируют разделение кампаний в unified export
- Применяются per-group в `group_negatives_commander`

---

## 9. Cross-Negative Matrix

- **248 group cross tokens**
- C01–C08 sibling discrimination documented
- Records: `production/cross-negative-validation-v2.json`
- Matrix doc: `production/final-conflict-negative-matrix-v2.md`

---

## 10. Phrase-Level Negatives

- **27 inline sets** across 8 groups
- Collision errors after review: **0**
- Collision warnings (direction/group token overlap): **26** — non-blocking, reviewed

---

## 11. Ad Corrections

- **6 ads** corrected (unsupported claims removed)
- «Под ключ» → factual h2
- «Срочно восстановим» → «Поможем восстановить»
- «Быстро и точно» → «Корво Неро» + договор
- Unified UTM in all landing URLs

Diff: `production/ad-v1-to-v2-diff.md`

---

## 12. Sitelinks and Callouts

- Direction-relevant sitelinks preserved per family
- «Срочная помощь» → «Диагностика и помощь» (troubleshooting)
- Callouts: factual only (договор, безнал, удалённо, выезд, конфигурации)

---

## 13. Bid Review

| Tier | Count |
|------|-------|
| T1 | 150 |
| T2 | 127 |
| T3 | 59 |
| T4 | 5 |

- Min: **235 ₽** · Max: **550 ₽** · Median: **450 ₽**
- Test/down-tier applied for mixed commercial risk
- No duplicate phrase bids

---

## 14. URL and UTM Review

- Domain: `https://lk.corvonero.ru/` — all ads
- Unified `utm_campaign=corvonero_1c_search_nsk`
- `utm_content=<group_id>` stable
- `utm_term={keyword}`
- No Triumph references, no `??` duplicates
- 31 planned landing paths preserved

---

## 15. Unified Dataset V2

**File:** `production/direct-commander-production-dataset-v2.json`

Contains: unified campaign, 8 logical directions, 48 active groups, 341 keywords, 53 ads, negatives (global/direction/cross/inline), URLs, UTM, future split metadata, collision validation.

---

## 16. Unified XLSX V2

**File:** `exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v2.xlsx`

| Metric | Value |
|--------|-------|
| Data rows | 394 |
| Groups | 48 |
| Keywords | 341 |
| Ads | 53 |
| Markers missing | 0 |
| Integrity | INTEGRITY_OK |

v1 **не перезаписан**.

---

## 17. Validation Results

**File:** `production/validation/direct-commander-v2-validation.json`

| Check | Result |
|-------|--------|
| Status | STRUCTURALLY_VALIDATED |
| Errors | 0 |
| Warnings | 0 |
| Collision errors | 0 |
| Bad DIY/employment KW in sheet | 0 |
| Unsupported ad claims | 0 |
| Group marker present | 48/48 |

---

## 18. Review Workbook

**File:** `exports/CORVONERO-CAMPAIGN-REVIEW-v2.xlsx`  
**CSV fallback:** `exports/review-v2-csv/`

Sheets: Groups, Keywords, Ads, Global negatives, Cross-negatives, URLs, Bids, Held groups, Exclusions.

**Not for Commander import.**

---

## 19. Import Instructions

**File:** `exports/CORVONERO-COMMANDER-IMPORT-INSTRUCTIONS-v2.md`

v1 instructions marked SUPERSEDED.

---

## 20. Landing Handoff

**File:** `production/landing-copy-handoff-v2.json`

Updated: active groups, URLs, ad promises, keyword intents, held/merge (none). Landing copy **not created**.

---

## 21. Files Created or Changed

### Created
- `production/direct-commander-production-dataset-v2.json`
- `production/final-keyword-registry-v2.json` / `.md`
- `production/final-negative-registry-v2.json`
- `production/final-conflict-negative-matrix-v2.md`
- `production/cross-negative-validation-v2.json`
- `production/final-ad-registry-v2.json` / `.md`
- `production/keyword-v1-to-v2-diff.md`
- `production/ad-v1-to-v2-diff.md`
- `production/landing-copy-handoff-v2.json`
- `production/validation/direct-commander-v2-validation.json` / `.md`
- `production/validation/export-run-result-v2.json`
- `exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v2.xlsx`
- `exports/CORVONERO-CAMPAIGN-REVIEW-v2.xlsx`
- `exports/CORVONERO-COMMANDER-IMPORT-INSTRUCTIONS-v2.md`
- `exports/review-v2-csv/` (9 CSV sheets)
- `tools/run-full-production-v2.mjs`
- `tools/export-commander-xlsx-v2.cjs`
- `tools/validate-commander-xlsx-v2.cjs`
- `tools/generate-review-workbook-v2.cjs`
- `tools/lib/campaign-markers.mjs`
- `tools/lib/keyword-classifier-v2.mjs`
- `tools/lib/negatives-config-v2.mjs`

### Modified
- `tools/lib/ads.mjs` — factual copy, unified UTM
- `exports/CORVONERO-COMMANDER-IMPORT-INSTRUCTIONS-v1.md` — SUPERSEDED note

---

## 22. Git Status

Untracked: `projects/orca/projects/corvonero-yandex-direct/` (entire project tree).  
No commit. No push.

---

## 23. Remaining Manual Checks

1. Dry-run import v2 XLSX в Direct Commander
2. Visual review review workbook (Groups, Exclusions sheets)
3. Confirm campaign type (ЕПК) matches account
4. Publish 31 landing pages before launch
5. Metrika + goals setup
6. Budget allocation (unified or post-split)

---

## 24. Next Gate

1. Operator review of `CORVONERO-CAMPAIGN-REVIEW-v2.xlsx`
2. Commander dry-run import approval
3. Landing copy production (`landing-copy-handoff-v2.json`)
4. Final 8-campaign split + separate XLSX (deferred)

---

## 25. Stop Condition

| Item | Status |
|------|--------|
| XLSX v1 | **SUPERSEDED** |
| Unified XLSX v2 | **GENERATED AND STRUCTURALLY VALIDATED** |
| Campaign format | **ONE CAMPAIGN FOR CURRENT REVIEW** |
| Future split | **DEFERRED** |
| Keyword cleanup | **COMPLETE** |
| Negative architecture | **COMPLETE** |
| Cross-negative validation | **COMPLETE** |
| Ad review | **COMPLETE** |
| Manual Commander import | **REQUIRED** |
| Landing copy | **NEXT AFTER OPERATOR REVIEW** |
| Launch | **NOT AUTHORIZED** |
