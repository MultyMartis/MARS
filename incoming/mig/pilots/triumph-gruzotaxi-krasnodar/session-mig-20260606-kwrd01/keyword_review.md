# Keyword Review — session-mig-20260606-kwrd01

**Session:** `mig-20260606-kwrd01`  
**Market:** Грузотакси Краснодар / проект Триумф  
**Provider path:** Manual Wordstat Export  
**Review date:** 2026-06-06  
**Reviewer:** manual-wordstat-pilot-operator  
**Parent query set:** `multi-query-market-query-set-v1` (logical parent session `mig-20260604-mqgt01`)

---

## Human Review Gate (HR-01..HR-05)

| Check | Result | Evidence |
|-------|--------|----------|
| **HR-01** Raw snapshot present | **PASS** | `wordstat-export-manual-2026-06-06.md` attached; `source_file_ref` in snapshot header; export date 2026-06-06; operator id recorded |
| **HR-02** Region match | **PASS** | Export region «Краснодар» matches session `scope.region`; no region mismatch rows |
| **HR-03** Phrase coverage declared | **PASS** | All q01–q11 have matching snapshot rows; no missing queries |
| **HR-04** Conflicts surfaced | **PASS** | No duplicate phrase/period with different frequency values; `provider_conflict_count: 0` |
| **HR-05** No strategy bleed | **PASS** | Registry contains no cluster_id, priority, ORCA intent enums, or strategy fields |

**Gate verdict:** **PASSED** — eligible for KP-COMPLETE.

---

## Pilot success criteria (SC-01..SC-14)

| ID | Criterion | Result |
|----|-----------|--------|
| SC-01 | Raw export preserved | **PASS** |
| SC-02 | Snapshot created | **PASS** — `wordstat_snapshot.cap-20260606-kwrd01.json` |
| SC-03 | Phrase coverage attempted | **PASS** — 11/11 |
| SC-04 | Registry populated | **PASS** — `keyword_registry.json` revision 1, 11 objects |
| SC-05 | Provenance complete | **PASS** — all objects `KS-PROV-FUTURE-WORDSTAT`, `import_method: manual_export` |
| SC-06 | Numbers raw | **PASS** — spot-check q01 (108), q03 (2696), q07 (0) match export |
| SC-07 | Conflicts surfaced | **PASS** — none observed |
| SC-08 | Region honesty | **PASS** |
| SC-09 | SAFE UNKNOWN preserved | **PASS** — period unknown; q03 mixed intent; q08 wording variant declared |
| SC-10 | Human Review Gate passed | **PASS** |
| SC-11 | keyword_pass completed | **PASS** — see `session_manifest.json` |
| SC-12 | Phase 1 unchanged | **PASS** — mqgt01 / mlint01 / gtrgt01 not modified |
| SC-13 | No strategy bleed | **PASS** |
| SC-14 | Cross-layer divergence declared | **PASS** — q05–q07 Wordstat vs SERP failure documented |

**Pilot verdict:** **PASSED**

---

## Coverage matrix

| Query ID | Approved phrase | Export phrase | Frequency | Notes |
|----------|-----------------|---------------|-----------|-------|
| q01 | грузотакси Краснодар | грузотакси краснодар | 108 | casing variance only |
| q02 | грузовое такси Краснодар | грузовое такси краснодар | 599 | casing variance only |
| q03 | газель Краснодар | газель краснодар | 2696 | **mixed intent** — operator note preserved |
| q04 | грузоперевозки Краснодар | грузоперевозки краснодар | 1059 | |
| q05 | перевозка мебели Краснодар | перевозка мебели краснодар | 84 | SERP layer failed in mqgt01 |
| q06 | квартирный переезд Краснодар | квартирный переезд краснодар | 34 | SERP layer failed in mqgt01 |
| q07 | вызов газели Краснодар | вызов газели краснодар | 0 | provider zero preserved; SERP failed in mqgt01 |
| q08 | газель с грузчиками Краснодар | газель с **грузчиком** краснодар | 7 | wording variant (singular vs plural) |
| q09 | грузовое такси с грузчиками Краснодар | грузовое такси с грузчиками краснодар | 16 | |
| q10 | грузоперевозки по Краснодару | грузоперевозки по краснодару | 159 | geo preposition variant |
| q11 | заказать газель Краснодар | заказать газель краснодар | 21 | |

---

## Operator notes (preserved)

**q03 — «газель краснодар»:** mixed intent observed (vehicle purchase, driver jobs, repair, cargo transportation). Raw frequency 2696 preserved. No correction applied.

---

## Declared SAFE UNKNOWN

1. Wordstat **period** not recorded in export — `period_scope: unknown` on all objects.
2. **q08** export uses singular «грузчиком» vs approved plural «грузчиками».
3. **Cross-layer:** Wordstat captured q05–q07; Phase 1 SERP `mig-20260604-mqgt01` has `execution_status: failed` for same queries — layers independent, not merged.

---

## Sign-off

Registry state: **frozen** (revision 1).  
Manifest state: **KP-COMPLETE** (`keyword_pass: true`).

*Review record immutable after sign-off per MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.*
