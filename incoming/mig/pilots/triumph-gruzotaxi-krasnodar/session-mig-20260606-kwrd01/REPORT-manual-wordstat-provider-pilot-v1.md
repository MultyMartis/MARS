# REPORT — Manual Wordstat Provider Pilot (session-mig-20260606-kwrd01)

**Date:** 2026-06-06  
**Charter:** [MIG-MANUAL-PROVIDER-RUNTIME-PILOT-v1.md](../../../../projects/mig/reports/MIG-MANUAL-PROVIDER-RUNTIME-PILOT-v1.md)  
**Session:** `mig-20260606-kwrd01`  
**Market:** Грузотакси Краснодар / проект Триумф  
**Provider:** Manual Wordstat Export  
**Region:** Краснодар

---

## Summary

First real Demand Surface runtime pilot cycle completed under human supervision. Operator export attached; snapshot, observations, registry (revision 1), human review, and manifest KP-COMPLETE authored per Phase 3a artifact chain.

**Verdict:** **PILOT PASSED** (SC-01..SC-14 satisfied; no FC-01..FC-14 triggered).

---

## Artifact chain

| Stage | Artifact | Status |
|-------|----------|--------|
| 0 Export | `wordstat-export-manual-2026-06-06.md` | Present (operator) |
| 1 Preservation | Same — immutable upstream SoT | OK |
| 2 Snapshot | `wordstat_snapshot.cap-20260606-kwrd01.json` | Authored |
| 3 Observations | `keyword_observations.json` | Authored |
| 4 Registry | `keyword_registry.json` (revision 1, frozen) | Authored |
| 5 Review | `keyword_review.md` | HR-01..HR-05 PASS |
| 6 keyword_pass | `session_manifest.json` | KP-COMPLETE |

---

## Frequency summary (raw, unmodified)

| Query | Phrase (export) | Shows |
|-------|-----------------|-------|
| q01 | грузотакси краснодар | 108 |
| q02 | грузовое такси краснодар | 599 |
| q03 | газель краснодар | 2696 |
| q04 | грузоперевозки краснодар | 1059 |
| q05 | перевозка мебели краснодар | 84 |
| q06 | квартирный переезд краснодар | 34 |
| q07 | вызов газели краснодар | 0 |
| q08 | газель с грузчиком краснодар | 7 |
| q09 | грузовое такси с грузчиками краснодар | 16 |
| q10 | грузоперевозки по краснодару | 159 |
| q11 | заказать газель краснодар | 21 |

---

## Notable findings

1. **q03 mixed intent** — operator flagged «газель краснодар» as blending vehicle purchase, jobs, repair, and transportation demand. Frequency 2696 preserved without decomposition.
2. **q08 wording variant** — export used singular «грузчиком» vs approved plural «грузчиками».
3. **Cross-layer divergence** — Wordstat captured q05–q07; Phase 1 SERP mqgt01 failed on same queries. Declared independent per KS-06.
4. **Period unknown** — Wordstat UI period not recorded in export header.

---

## What this proves / does not prove

| Proven | Not proven |
|--------|------------|
| Real provider data traverses Demand Surface architecture under human discipline | Automation, scale, unattended ingest |
| Manual snapshot → registry → review → keyword_pass chain works on validated market | Registry writer code, CSV parser, runtime keyword_pass automation |
| Provenance and SAFE UNKNOWN discipline hold with real export | Cross-session registry, ORCA consumption, pack frequency approval |

---

## Phase 1 integrity

No modifications to `session-mig-20260604-mqgt01`, `session-mig-20260605-mlint01`, or `session-mig-20260605-gtrgt01`.

---

*Manual Wordstat Provider Pilot v1 · session-mig-20260606-kwrd01 · 2026-06-06*
