# Wordstat Acquisition — Automated Attempt Blocked (af-006)

**Session:** `mig-20260622-corv01`  
**Date:** 2026-06-22  
**Policy corrected:** 2026-06-22 — two-pass manual operator model

---

## af-006 scope (corrected)

| Field | Value |
|-------|-------|
| Failure id | **af-006** |
| Applies to | **Automated Cursor-agent Wordstat collection only** |
| Does **not** apply to | Manual operator Pass A / Pass B collection |
| Wordstat overall | **Not permanently blocked** — manual collection **AUTHORIZED** |

---

## Automated attempt summary (2026-06-22 earlier pass)

| Field | Value |
|-------|-------|
| Provider | Yandex Wordstat — https://wordstat.yandex.ru/ |
| Method attempted | Automated agent fetch / export |
| Operator environment | Cursor agent — no authenticated Yandex Wordstat session |
| Outcome | **BLOCKED** for automation — failure id **af-006** |
| Frequencies captured by agent | **0** |

**No frequencies were estimated, inferred, or reconstructed by the agent.**

---

## Manual operator remediation (active)

### Pass A — Semantic Discovery (**COMPLETE — Storage correction 2026-06-22**)

**Ingestion pass 2026-06-22 (corrected):** Cursor agent ran `tools/ingest-wordstat-pass-a.mjs` against **`C:\AI MARS STORAGE\mig\corvonero\wordstat-2026-06\`** — **18 Excel files** parsed; **2399** normalized rows. Prior af-007 claim (0 files) **superseded** — root cause was wrong evidence locus (in-repo scan only).

| Outcome | Detail |
|---------|--------|
| Excel files found | **18** (MARS Storage external evidence) |
| No-result operator reports registered | **2** — `доработка РМК`, `срочно программист 1С` |
| Pass A completion | **COMPLETE** (20/20 seeds accounted) |
| Index artefact | `evidence/wordstat/wordstat-pass-a-file-index.json` |
| Failure af-007 | **resolved_superseded** |

### Pass A — Operator procedure (unchanged)

1. Operator signs in to Yandex Wordstat.
2. Set region to **все регионы / all Russia**.
3. Enter seed phrase **without quotation marks** (e.g. `программист 1С`).
4. Save screenshot to `evidence/wordstat/screenshots/{query_id}-*.jpg`.
5. Save export where available; preserve left and related query columns.
6. Register evidence in `wordstat-export-manual-20260622-corv01.md` and snapshot — **do not** write nationwide broad totals into regional demand or frequency registry slots.

**First evidence registered:** ws-p1-001 — see `evidence/wordstat/pass-a-ws-p1-001-evidence.json` (screenshot awaiting ingestion).

### Pass B — Regional Demand Validation (**NOT STARTED**)

1. After Pass A review, run **bounded shortlist** only.
2. Set region to **Новосибирск + Новосибирская область**.
3. Use exact / quoted operator syntax per matrix Pass B rows.
4. Do **not** repeat full Pass A matrix regionally.

---

## Screenshot references

| query_id | File | Status |
|----------|------|--------|
| ws-p1-001 | `ws-p1-001-programmist-1c.jpg` | Operator provided — **awaiting ingestion** to `evidence/wordstat/screenshots/` |

---

*Updated 2026-06-22 — Pass A COMPLETE via MARS Storage ingestion; af-007 resolved.*
