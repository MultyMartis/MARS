# REPORT — КОРВО НЕРО — WORDSTAT STORAGE INGESTION CORRECTION

**Session:** `mig-20260622-corv01`  
**Date:** 2026-06-22  
**Lane:** A — MIG evidence acquisition (correction pass)  
**Binding:** ORG-0009 / LE-0006 / PRJ-0013 / WEB-CORV-01 / DOM-CORV-01

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Git branch | `mars/post-cycle8-live-tests` |
| HEAD | `19b9d7f` |
| Canonical session | **`mig-20260622-corv01`** — confirmed |
| Newer Corvonero session | **None** |
| Unrelated WIP | **Not modified** (session folder only) |
| External Storage treated as Git locus | **No** — read-only external evidence source |
| Pass B | **NOT STARTED** — unchanged |
| New SERP capture | **Not executed** |

---

## 2. Storage Path Inspection

| Field | Value |
|-------|-------|
| Path inspected | `C:\AI MARS STORAGE\mig\corvonero\wordstat-2026-06\` |
| Recursive scan | **Yes** — flat directory, 18 files, no subdirectories with additional exports |
| Screenshots in Storage | **None** |
| CSV / XLS | **None** — all `.xlsx` |
| Originals modified | **No** |

**Prior error:** Ingestion scanned in-repo loci only (`evidence/wordstat/exports`, `pass-a`, `incoming`). Operator files were in approved MARS Storage path per infrastructure policy.

---

## 3. Files Found

| Filename | Size (bytes) | SHA-256 |
|----------|-------------|---------|
| ws-p1-001-programmist-1c.xlsx | 95223 | `84464761e9b8d59105766d828bc63cb6730f02dc71e4c081e9a813940a948a96` |
| ws-p1-002-uslugi-programmista-1c.xlsx | 16999 | `a6b8227bf5f70893222f6a91519ad5efa8e5a9a72610d054f581a536979859ec` |
| ws-p1-003-soprovozhdenie-1c.xlsx | 40862 | `75c0904d824787cffe9b4dee3e266d0cdc752ba182e94d253b391b2aec6f2d96` |
| ws-p1-004-dorabotka-1c.xlsx | 26714 | `4e0afa9bc3a63e62ff8e042ea83013783fc2f7199658cd544bc561dee3b4f65a` |
| ws-p1-005-integraciya-s-saitom.xlsx | 17680 | `a89f26ac2bc56e5ffff283dc3de275778edfb709fecded6dc34882354426ba71` |
| ws-p1-006-integraciya-bitrix.xlsx | 20173 | `c49fd2c76a72012c806bec57930b658d7e38dc2370828f1fb872daaed48129b4` |
| ws-p1-007-markirovka-v-1c.xlsx | 42693 | `e726ffa948c71eb1cb6bd97f487533d57b6ffe0f8ef1efdf1fff59b76f9a719a` |
| ws-p1-008-chestny-znak-1c.xlsx | 50938 | `f3feb6a59fb5efa3353f517e8e5b3f2effb0bd39e212caf0a5294c8d024ae232` |
| ws-p2-001-otchet-1c.xlsx | 16622 | `8b45b9cb31b54a30bce4e87394e065732fb8027d07ce2077c127dc885f532634` |
| ws-p2-002-pechatnaya-forma.xlsx | 91299 | `a2ce8003160dcd46c505e1b9f6b2d9691f2f7d81bddd9a6810b3858800e2bc8c` |
| ws-p2-004-sinhronizaciya.xlsx | 69989 | `6971f418af26674efc551767164784d3278d5c5e4d82c6c92cd1eaa9b92d717b` |
| ws-p2-005-obnovlenie-dorabotannoy.xlsx | 16513 | `6aeb9123a86bd38b02c2d791d8ee64054a1357105e1b72105e902d120eef4673` |
| ws-p2-007-1c-ne-rabotaet.xlsx | 16611 | `e58373e588b52d3176937bc228ffe94e9714dfdc601c5990773c9cdb5d3fb52d` |
| ws-p3-001-pivo.xlsx | 16456 | `d053c057c0f90d82fd8893c160c9563851e08ccd0efe981be382b3ea55b78e35` |
| ws-p3-002-voda.xlsx | 16456 | `41d35b769456c1cd9f65b43e0b9bd1a1296be36c1862e205f49297cd2aac54c5` |
| ws-p3-003-lekarstva.xlsx | 20921 | `3bf2779eca7e6fee4d54593e0efefde83d0f575373c645ed1b36a2e9b07a3d71` |
| ws-p3-004-avtozapchasti.xlsx | 19639 | `70b74c5bde18880673902f34641f4bbc2a759dcf585cb49b32a2413d9d807dfa` |
| ws-p3-005-ts-piot.xlsx | 25147 | `c21c9a6d2a3e93672736106738c533f037da8589a5f5adcdce961d068117887d` |

**Total:** 18 Excel files. No `.csv`, `.xls`, or screenshots in Storage path.

---

## 4. File-to-Query Mapping

| query_id | Expected seed | File | Rows | Mapping |
|----------|---------------|------|------|---------|
| ws-p1-001 | программист 1С | ws-p1-001-programmist-1c.xlsx | 589 | mapped_by_filename |
| ws-p1-002 | программист 1С Новосибирск | ws-p1-002-uslugi-programmista-1c.xlsx | 5 | mapped_by_filename — slug says «услуги программиста» |
| ws-p1-003 | сопровождение 1С | ws-p1-003-soprovozhdenie-1c.xlsx | 177 | mapped_by_filename |
| ws-p1-004 | доработка 1С | ws-p1-004-dorabotka-1c.xlsx | 83 | mapped_by_filename |
| ws-p1-005 | интеграция 1С с сайтом | ws-p1-005-integraciya-s-saitom.xlsx | 10 | mapped_by_filename |
| ws-p1-006 | интеграция 1С Битрикс | ws-p1-006-integraciya-bitrix.xlsx | 28 | mapped_by_filename |
| ws-p1-007 | маркировка в 1С | ws-p1-007-markirovka-v-1c.xlsx | 196 | mapped_by_filename |
| ws-p1-008 | Честный знак 1С | ws-p1-008-chestny-znak-1c.xlsx | 250 | mapped_by_filename |
| ws-p2-001 | доработка отчёта 1С | ws-p2-001-otchet-1c.xlsx | 2 | mapped_by_filename |
| ws-p2-002 | доработка печатной формы 1С | ws-p2-002-pechatnaya-forma.xlsx | 542 | mapped_by_filename |
| ws-p2-003 | доработка РМК 1С | — | — | **no_result** — entered `доработка РМК` |
| ws-p2-004 | настройка синхронизации 1С | ws-p2-004-sinhronizaciya.xlsx | 384 | mapped_by_filename |
| ws-p2-005 | обновление доработанной 1С | ws-p2-005-obnovlenie-dorabotannoy.xlsx | 1 | mapped_by_filename |
| ws-p2-006 | срочно программист 1С | — | — | **no_result** — entered `срочно программист 1С` |
| ws-p2-007 | 1С не работает | ws-p2-007-1c-ne-rabotaet.xlsx | 1 | mapped_by_filename |
| ws-p3-001 | маркировка пива 1С | ws-p3-001-pivo.xlsx | 2 | mapped_by_filename |
| ws-p3-002 | маркировка воды 1С | ws-p3-002-voda.xlsx | 1 | mapped_by_filename |
| ws-p3-003 | маркировка лекарств 1С | ws-p3-003-lekarstva.xlsx | 1 | mapped_by_filename |
| ws-p3-004 | ТС ПИОТ 1С | ws-p3-004-avtozapchasti.xlsx | 33 | mapped_by_filename — **slug/matrix mismatch** (file slug «avtozapchasti») |
| ws-p3-005 | маркировка автозапчастей 1С | ws-p3-005-ts-piot.xlsx | 22 | mapped_by_filename — **slug/matrix mismatch** (file slug «ts-piot») |

All files: sheet `Data`; required columns present; `external_source_classification: mars_storage_external_evidence`.

---

## 5. Excel Parsing Results

| Metric | Value |
|--------|-------|
| Parser | `tools/ingest-wordstat-pass-a.mjs` (updated — accepts Storage path arg) |
| Library | exceljs — available |
| Files parsed OK | **18 / 18** |
| Normalized rows | **2399** |
| Source files modified | **None** |
| Artefacts | `wordstat-pass-a-file-index.json`, `wordstat-pass-a-normalized.json`, per-query `pass-a-ws-*-evidence.json` |

Each row preserves: raw phrase, normalized phrase, observed count, source file, source hash, source sheet/row. No inferred missing values. Nationwide broad values **not** interpreted as Novosibirsk demand or traffic forecast.

---

## 6. No-Result Seeds

| query_id | Entered formulation | Status | Numeric frequency |
|----------|---------------------|--------|-------------------|
| ws-p2-003 | доработка РМК | `no_result_for_entered_formulation` | **not_available** (not 0) |
| ws-p2-006 | срочно программист 1С | `no_result_for_entered_formulation` | **not_available** (not 0) |

Thematic demand **not disproved**. Evidence refs: `pass-a-ws-p2-003-no-result-evidence.json`, `pass-a-ws-p2-006-no-result-evidence.json`.

---

## 7. Evidence-Supported Alternatives

Searched across **2399 ingested rows** (not invented):

### RMK cluster (ws-p2-003 context)

| Category | Formulations |
|----------|-------------|
| **Found in evidence** | `1с рмк честный знак`, `1с рмк синхронизация`, `1с рмк настройка синхронизации`, `1с рмк синхронизация с 1с унф`, `1с рмк синхронизация с 1с розница`, `тс пиот 1с рмк` |
| **Candidate for later validation** | РМК 1С, настройка РМК, рабочее место кассира, доработка рабочего места кассира, настройка кассового рабочего места |
| **Not found** | Exact candidate phrases above absent as standalone rows |

### Urgent support cluster (ws-p2-006 context)

| Category | Formulations |
|----------|-------------|
| **Found in evidence** | `программа 1с не работает`, `после обновления 1с не работает синхронизация` |
| **Candidate for later validation** | срочная помощь 1С, программист 1С срочно, 1С не работает, исправить ошибку 1С, восстановить работу 1С |
| **Not found as exact rows** | срочная помощь 1С, программист 1С срочно, исправить ошибку 1С, восстановить работу 1С |

Note: `1С не работает` appears as ws-p2-007 seed export (1 row) — evidence-supported via separate query file.

---

## 8. Pass A Completion Status

| Field | Value |
|-------|-------|
| Pass A | **COMPLETE** |
| Seeds accounted | **20 / 20** |
| Excel ingested | 18 |
| No-result records | 2 |
| Missing IDs | **none** |
| Pass B | **PREPARED — NOT STARTED** |

Matrix updated: `corvonero-wordstat-collection-matrix-v1.json`.

---

## 9. Demand Surface Update

Layer `wordstat_pass_a_national_semantic_discovery` populated in `demand_surface.json`:

- 2399 evidence-supported phrases (nationwide broad semantic discovery)
- Intent/noise counts from parsed rows (commercial, informational, vacancy, training, regulatory, troubleshooting)
- No-result seed formulations preserved
- Alternative formulations documented
- **Separated** from Novosibirsk SERP (grade C, af-008) and future Pass B regional Wordstat

---

## 10. Keyword Registry Update

`keyword_registry.json` updated:

- 20 seed entries — wordstat evidence attached where Excel/no-result applies
- **2364** additional discovered phrases as `candidate_not_final_keyword` (2384 total keywords)
- Each discovered phrase: national broad observed count, source hash/row, seed cluster, intent/noise classes
- Regional demand: **UNKNOWN** for all
- ORCA handoff: **pending Pass B and review** — high broad count **not** marked as high commercial priority

---

## 11. Failure Lifecycle Correction

| Failure | Action |
|---------|--------|
| **af-007** | **resolved_superseded** — root cause wrong evidence locus; files found and parsed from MARS Storage |
| **af-008** | **unchanged** — Playwright SERP CAPTCHA; no new SERP attempt in this task |

Prior false claim «operator files missing» **retracted**. `evidence/source-registry.json` updated.

---

## 12. Files Created or Changed

**Created:**

- `REPORT-mig-wordstat-storage-ingestion-correction-v1.md`
- `tools/update-registries-post-storage-ingestion.mjs`
- `evidence/wordstat/pass-a-ws-p1-002-evidence.json` … `pass-a-ws-p3-005-evidence.json` (18 per-query evidence files)

**Modified:**

- `tools/ingest-wordstat-pass-a.mjs` — external Storage path argument
- `evidence/wordstat/wordstat-pass-a-file-index.json`
- `evidence/wordstat/wordstat-pass-a-normalized.json`
- `corvonero-wordstat-collection-matrix-v1.json`
- `demand_surface.json`
- `keyword_registry.json`
- `wordstat-collection-normalized.json`
- `wordstat_snapshot.cap-20260622-corv01.json`
- `wordstat-export-manual-20260622-corv01.md`
- `evidence/source-registry.json`
- `evidence/review.md`
- `evidence/wordstat/acquisition-blocked-20260622.md`
- `session_manifest.json`
- `REPORT-mig-wordstat-ingestion-and-playwright-serp-v1.md` — superseded banner added

**Not modified:** ATLAS, unrelated WIP, SERP captures, Pass B artefacts.

---

## 13. Validation

| Check | Result |
|-------|--------|
| Exact Storage path inspected | **Yes** |
| Original Excel files unmodified | **Yes** |
| Every numeric value has source file + row | **Yes** |
| All-Russia broad separate from regional demand | **Yes** |
| No-result not recorded as zero demand | **Yes** |
| Only evidence-supported alternatives added | **Yes** |
| Pass B not executed | **Yes** |
| No new SERP run | **Yes** |
| af-008 separate | **Yes** |
| No Research Pack / ORCA / campaign / landing | **Yes** |
| No commit / push | **Yes** |

---

## 14. Git Status

| Field | Value |
|-------|-------|
| Branch | `mars/post-cycle8-live-tests` |
| HEAD | `19b9d7f` |
| Session folder | `?? incoming/mig/pilots/corvonero/session-mig-20260622-corv01/` (untracked) |
| Commit | **None** |
| Push | **None** |

---

## 15. Remaining Blockers

| ID | Topic | Status |
|----|-------|--------|
| **af-008** | Playwright R1 SERP — CAPTCHA all 10 queries | **open** |
| **af-004** | Direct-fetch SERP route | **open** (grade C fallback preserved) |
| Pass B | Regional Wordstat validation | **NOT STARTED** |
| ws-p3-004 / ws-p3-005 | Filename slug vs matrix base_phrase mismatch | **operator review recommended** |

---

## 16. Next Gate

1. Operator review Pass A semantic discovery (`wordstat-pass-a-normalized.json`, demand surface layer)
2. Resolve ws-p3-004/p3-005 slug ambiguity if operator entered different seeds than matrix labels
3. Operator-supervised SERP capture (af-008 remediation) — **separate task**
4. Pass B regional Wordstat on bounded shortlist — **after Pass A review approval**
5. Human Review Gate before Research Pack / ORCA

---

## 17. Stop Condition

**STOPPED** after corrected Wordstat ingestion and evidence updates.

**Not executed:** SERP, Wordstat Pass B, Research Pack, ORCA, campaign architecture, landing architecture, landing copy, commit, push.

---

*Prior report `REPORT-mig-wordstat-ingestion-and-playwright-serp-v1.md` section 2–3 (0 files found) superseded by this correction.*
