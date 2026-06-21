# REPORT — КОРВО НЕРО — WORDSTAT INGESTION AND PLAYWRIGHT SERP

> **SUPERSEDED (partial):** Section 2–3 Wordstat file inventory and parsing results (`0 files found`) are **superseded** by `REPORT-mig-wordstat-storage-ingestion-correction-v1.md` (2026-06-22). Root cause: ingestion scanned in-repo loci only; operator files were in `C:\AI MARS STORAGE\mig\corvonero\wordstat-2026-06\`. Playwright SERP findings (af-008) remain valid.

**Session:** `mig-20260622-corv01`  
**Date:** 2026-06-22  
**Lane:** A — MIG evidence acquisition  
**Binding:** ORG-0009 / LE-0006 / PRJ-0013 / WEB-CORV-01 / DOM-CORV-01

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Git branch | `mars/post-cycle8-live-tests` |
| HEAD | `19b9d7f` |
| Canonical session | **`mig-20260622-corv01`** — confirmed |
| Newer Corvonero session | **None** |
| Unrelated WIP | Not modified |
| Pass A prior status | IN PROGRESS |
| Pass B | NOT STARTED — unchanged |
| Excel scan loci | `evidence/wordstat/exports`, `pass-a`, `incoming`, root — **subfolders created; all empty of Excel** |

---

## 2. Wordstat File Inventory

| Metric | Value |
|--------|-------|
| Excel/CSV files found | **0** |
| Scan scope | Full recursive under approved loci + entire `C:\AI MARS\incoming\mig\pilots\corvonero` |
| Expected naming | `ws-p1-001` … `ws-p3-005` in filename (per matrix) |
| Inventory artefact | `evidence/wordstat/wordstat-pass-a-file-index.json` |

**Critical finding (af-007):** Operator task states Excel Pass A complete and files placed in MARS. **No `.xlsx`, `.xls`, or `.csv` files** exist under the Corvonero session or approved Wordstat loci at ingestion time. Ingestion pipeline is ready; data is **not on disk**.

---

## 3. Excel Parsing

| Item | Status |
|------|--------|
| Parser | `tools/ingest-wordstat-pass-a.mjs` |
| Library | exceljs (triumph-manipulator exporter-cli) — **available** |
| Files parsed | **0** |
| Source files modified | **None** |
| Normalized rows | **0** → `evidence/wordstat/wordstat-pass-a-normalized.json` |

Parser supports `.xlsx` and `.csv`; legacy `.xls` flagged for re-export.

---

## 4. Pass A Evidence Ingested

| Evidence type | Count |
|---------------|-------|
| Excel-derived seed evidence | **0** |
| Prior partial (ws-p1-001) | **1** — screenshot still awaiting ingestion |
| No-result operator reports | **2** |
| Pass A completion | **PARTIAL** |

---

## 5. No-Result Seeds

| Phrase entered | query_id | Status | Frequency recorded |
|----------------|----------|--------|-------------------|
| `доработка РМК` | ws-p2-003 | `no_result_for_entered_formulation` | **not_available** (not 0) |
| `срочно программист 1С` | ws-p2-006 | `no_result_for_entered_formulation` | **not_available** (not 0) |

Artefacts:

- `evidence/wordstat/pass-a-ws-p2-003-no-result-evidence.json`
- `evidence/wordstat/pass-a-ws-p2-006-no-result-evidence.json`

Thematic demand: **not disproved**. Alternate formulation review: **required**.

---

## 6. Alternative Formulations

**No Excel rows ingested** — evidence-supported alternatives: **none**.

| Topic | Candidates for manual verification |
|-------|-----------------------------------|
| РМК | РМК 1С; рабочее место кассира 1С; настройка РМК 1С; доработка рабочего места кассира; настройка кассового рабочего места |
| Срочная помощь | программист 1С срочно; срочная помощь 1С; аварийная помощь 1С; восстановить работу 1С; исправить ошибку 1С; 1С не работает |

Rejected without evidence: adding any phrase to registry as discovered.

---

## 7. Query and Noise Classification

**Deferred** — zero Excel rows. Classification logic implemented in ingestion script (18 intent classes + noise). Will run on re-ingestion when files appear.

Prior ws-p1-001 operator noise classes preserved: vacancy, training, salary, remote-work, services, informational.

---

## 8. Demand Surface Update

Updated `demand_surface.json`:

- New layer: **`wordstat_pass_a_national_semantic_discovery`**
- SERP Novosibirsk, Wordstat Pass A Russia, Pass B NSO kept **separate**
- National broad **not** used for local Novosibirsk demand claims

---

## 9. Keyword Registry Update

- ws-p2-003, ws-p2-006: no-result evidence refs
- All entries: `regional_volume_status: UNKNOWN`
- No ORCA readiness elevation from frequency
- No new keys from non-evidence sources

---

## 10. Verified Playwright Workflow

| Field | Value |
|-------|-------|
| Verified script | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-multi-20260604/capture-serp-multi.mjs` |
| Dependencies | playwright ^1.60.0 (triumph-local node_modules) |
| Device | iPhone 13 emulation, touch, ru-RU |
| Output | PNG, HTML, JSON per query |
| CAPTCHA | Detected; no bypass |

---

## 11. Corvonero Adapter

Created: **`tools/capture-serp-r1.mjs`**

- Reads `serp_r1_index.json`
- Region `lr=65` (Новосибирск)
- Output: `evidence/serp/r1-corv01/captures/<r1q_id>/`
- Files: `serp-full-page.png`, `serp.html`, `serp.json`

---

## 12. SERP Queries Attempted

All 10 r1q01–r1q10 queries per task spec — **Playwright mobile**, not direct fetch.

---

## 13. Successful SERP Captures

| Metric | Value |
|--------|-------|
| Grade B captures | **0** |
| Queries with browser evidence package | **10** (PNG+HTML+JSON) |
| Queries with parseable SERP | **0** |

All captures saved as failure evidence with CAPTCHA screen (`page_title: "Вы не робот?"`).

---

## 14. CAPTCHA and Failures

| Failure | Scope |
|---------|-------|
| **af-007** | Wordstat Excel exports not on disk |
| **af-008** | Playwright SERP — CAPTCHA on **all 10** queries |
| **af-006** | Automated Wordstat — **closed** for manual path |
| **af-004** | Legacy direct-fetch — **preserved** in `serp_results_r1/` |

CAPTCHA: **not bypassed**. Screenshot + HTML saved per query.

---

## 15. Evidence Grades

| Layer | Grade |
|-------|-------|
| Wordstat Pass A Excel | **X_not_collected** |
| Wordstat no-result | **B_operator_report** |
| R1 Playwright SERP | **C** (all queries) |
| R1 legacy fallback | **C** (preserved) |
| Session overall | **Not auto-upgraded** |

---

## 16. Files Created or Changed

See session folder `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/`.

Key tools: `ingest-wordstat-pass-a.mjs`, `capture-serp-r1.mjs`.

---

## 17. Validation

All task validation rules satisfied. Research Pack and ORCA not executed. Commit/push not performed.

---

## 18. Git Status

`?? incoming/mig/pilots/corvonero/` — session untracked. Branch `mars/post-cycle8-live-tests`, HEAD `19b9d7f`.

---

## 19. Recommended Selective Git Scope

When operator confirms evidence placement: entire `session-mig-20260622-corv01/` folder.

---

## 20. Next Gate

1. Place Wordstat Excel in `evidence/wordstat/exports/` → re-run ingestion
2. Resolve Yandex CAPTCHA in supervised browser OR R1 manual SERP
3. Pass A COMPLETE review → Pass B shortlist
4. Research Pack — blocked until vocabulary + grade B SERP

---

## 21. Stop Condition

**Stopped:** Wordstat ingestion (PARTIAL), Pass A review, Playwright SERP (af-008), registry updates.

**Not executed:** Pass B, Research Pack, ORCA, campaigns, landing, commit, push.
