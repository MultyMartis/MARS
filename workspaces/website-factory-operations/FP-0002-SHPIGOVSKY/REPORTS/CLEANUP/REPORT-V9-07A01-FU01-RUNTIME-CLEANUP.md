# REPORT — FP-0002 V9-07A01-FU01 Runtime Cleanup

**Date:** 2026-07-23  
**Status:** PASS  
**Commit / push / freeze / production upload:** none

---

## 1. Scope

Cleanup after accepted V9-07A01:

1. temporary Playwright `node_modules` at runtime project root
2. superseded interview MPEG-TS `.bak` copies in runtime (theme + uploads; identical bytes)

Out of scope (preserved): `_tmp-e47-fix04-val`, older backups, reports, evidence, Stable v1 freeze, product theme/plugin/ACF.

---

## 2. Safety snapshot

`X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-07a01-fu01-cleanup-safety-20260723-222006`

Contains: `SAFETY-OK.txt`, `INFO.md`, `MANIFEST.csv`, `HASHES-SHA256.csv`, V9-07A01 report copy, test configuration note, paths scheduled for deletion.  
No full runtime / no uploads tree / no DB dump.

---

## 3. Inventory

`REPORTS/CLEANUP/V9-07A01-FU01-CLEANUP-INVENTORY.csv`

| Path | Action | Bytes | Rationale |
|------|--------|------:|-----------|
| `...\shpigovsky\node_modules` | DELETED | ~17.6 MB | Orphan Playwright 1.61.1 install 2026-07-23 21:51; no `package.json`; not used by WP product |
| `...\themes\shpigovsky\assets\video\sergey-shpigovsky-interview.mp4.BROKEN-MPEGTS.bak` | DELETED | 27 328 432 | Runtime-only vs current source; SHA256 `AC5A3896…`; preserved in Stable v1 + E63; active MP4 `46006380…` remains |
| `...\uploads\2026\07\sergey-shpigovsky-interview.mp4.BROKEN-MPEGTS.bak` | DELETED | 27 328 432 | Same hash as theme bak; active uploads MP4 retained |

Total reclaimed ≈ **72.2 MB**.

---

## 4. `.bak` uniqueness review

| Check | Result |
|-------|--------|
| Active theme MP4 | present, SHA256 `46006380A5345EB6…` |
| Active uploads MP4 | present, same hash |
| Current Git/source bak | absent (already cleaned from canonical source) |
| Stable v1 freeze | bak present, same `AC5A3896…` |
| E63 backup | bak present, same hash |
| Code references to `.BROKEN-MPEGTS` | none in theme/plugin |
| Unique operator content | **no** — fully superseded |

No historical pack copy required before delete (already inside protected Stable v1 freeze).

---

## 5. Post-cleanup validation

| Gate | Result |
|------|--------|
| Theme source↔runtime | MATCH (0 mismatches; 0 `.bak` left in theme) |
| Plugin source↔runtime | MATCH |
| ACF relevant `group_fp02_page_ocentre_hub.json` | MATCH |
| ACF source-only groups (Stable disposition) | still source-only; classified, not BLOCKED |
| Operator CSS `v9-style.css` | unchanged `1CCC5A8F1150BC69…` |
| Program cards | new title/slug present; old absent on `/`, `/o-centre/`, `/uslugi/`, `/uslugi/zavisimosti/` |
| Fancybox on hub/subdivision | CSS/JS enqueued; `data-fancybox` count 6 |
| Comfort leaf sample | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` 200 + Fancybox |
| Routes smoke | `/` 200, `/o-centre/` 200, `/uslugi/` 200, `/uslugi/zavisimosti/` 200, Program child 200, old slug 404, Search 200, 404 404 |
| PHP noise | 0 |
| DB writes this wave | 0 |

Interactive gallery open/nav/close was validated in V9-07A01 evidence; this wave confirmed enqueue + DOM hooks still present after cleanup (Playwright packages removed intentionally).

---

## 6. Git

No commit, no push, foreign WIP untouched.
