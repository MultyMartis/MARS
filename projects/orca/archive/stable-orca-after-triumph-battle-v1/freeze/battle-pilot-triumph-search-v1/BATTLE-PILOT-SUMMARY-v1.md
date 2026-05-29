# Battle Pilot Summary v1

**Operation:** ORCA Battle Pilot — Triumph Manipulator Search PPC  
**Date:** 2026-05-30 (freeze) · battle cycle 2026-05-28 — 2026-05-29  
**Lane:** B  
**Status:** **STABLE MILESTONE** — first real Commander import — **not** launch approval

---

## What this freeze records

Первое **боевое** (real Direct Commander) прохождение полного ORCA PPC pipeline для проекта «Триумф Манипулятор — РК на поиске». Не симуляция, не dry-run — реальный импорт v1.4 XLSX в Direct Commander с последующей human QA.

---

## Battle timeline

| Phase | Date | Milestone |
|-------|------|-----------|
| Semantic foundation | 2026-05-28 | Route family freeze (`7666829`) — 12/12 packs |
| URL sync | 2026-05-29 | Commander export URL sync (`f235bf1`) — legacy → `.html` |
| Transport fix | 2026-05-29 | Duplicate ads fix — transport split v1.2 |
| Production baseline | 2026-05-29 | Exporter production baseline (`2f01941`) |
| Launch export v1.3 | 2026-05-29 | Bids + cross-negatives in export |
| Launch export v1.4 | 2026-05-29 | Metadata fidelity + minus syntax fix |
| **Commander import** | 2026-05-29 | **Real import PASS** — v1.4 XLSX |
| **Post-import setup** | 2026-05-29 | Manual campaign strategy → bids visible |
| **Battle freeze** | 2026-05-30 | This freeze + stable backups |

---

## Final battle artifact

| Field | Value |
|-------|-------|
| **XLSX** | `triumph-sheet1-patch-launch-ready-v1.4.xlsx` |
| **Path** | `ppc/triumph-manipulator/tools/exporter-cli/output/` (gitignored — regenerate) |
| **JSON SoT** | `schema/instances/triumph-s-tier-draft-v1.json` |
| **Template SoT** | `assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx` |
| **Exporter** | Transport split v1.4 |

---

## Entity counts (verified post-import)

| Entity | Expected | Actual |
|--------|----------|--------|
| Groups | 12 | 12 |
| Ads | 20 | 20 |
| Keyword phrases | 64 | 64 |
| Transport rows | 84 | 84 |
| Duplicate ad signatures | 0 | 0 |
| Region | Краснодарский край | Краснодарский край |

---

## Confirmed working systems

1. **ORCA semantic route family** — 12 routes, differentiated packs, Factory handoff state frozen  
2. **JSON instance + validation-cli** — 345 rules, `export_allowed: true`  
3. **Exporter transport split v1.2+** — separate AD and KEYWORD rows, no multiplication  
4. **Commander template v1** — Search Manual Bids SoT, metadata fidelity at v1.4  
5. **URL canonical sync** — `manipulator-triumph.ru/*.html`, no legacy `gruzotaxi-triumph.ru`  
6. **Bid export v1.3+** — 400–600 ₽ range, 10–90 ₽ within-group spread  
7. **Cross-negative matrix v1.4** — Commander-safe syntax, no wildcards  
8. **Direct Commander import** — structural acceptance, counts match  

---

## Known gaps (not failures — documented limits)

| Gap | Status |
|-----|--------|
| Campaign strategy / budget / schedule in XLSX | **Not transportable** — post-import UI setup |
| Bids visible immediately after import | **Requires** manual strategy selection in Commander |
| Live SERP CPC calibration | **SAFE UNKNOWN** |
| Autobid / smart strategies | **Out of scope** — manual bids only |
| Ad serving / spend | **Not started** — launch not approved |

---

## Explicit prohibitions (this freeze)

- Do **not** launch ads from this milestone alone  
- Do **not** regenerate XLSX unless separate change request  
- Do **not** edit ad copy / keywords / URLs in Commander unless chartered  
- Do **not** claim runtime, orchestration, or autonomous validation  

---

## Related docs

- [COMMANDER-IMPORT-FINDINGS-v1.md](COMMANDER-IMPORT-FINDINGS-v1.md)  
- [FAILURES-AND-FIXES-v1.md](FAILURES-AND-FIXES-v1.md)  
- [ORCA-LESSONS-LEARNED-v1.md](ORCA-LESSONS-LEARNED-v1.md)  
- [STABLE-BACKUP-MANIFEST-v1.md](STABLE-BACKUP-MANIFEST-v1.md)
