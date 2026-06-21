# REPORT — КОРВО НЕРО — WORDSTAT POLICY AND SERP CAPABILITY AUDIT

**Session:** `mig-20260622-corv01`  
**Date:** 2026-06-22  
**Task:** Wordstat two-pass policy correction + SERP capability audit (no execution)

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Git branch | `mars/post-cycle8-live-tests` |
| HEAD | `19b9d7f` |
| Canonical session | **`mig-20260622-corv01`** — confirmed |
| Newer Corvonero session | **None** |
| Unrelated WIP | Not modified |
| MIG core contracts | Not edited — recommendations only where noted |

Contracts and pilots read: `OPERATIONAL-INDEX.md`, `MIG-REALITY-ACQUISITION-MODEL-v1.md`, `REPORT-mig-data-acquisition-architecture-v1.md`, `MIG-KEYWORD-REGISTRY-MODEL-v1.md`, Triumph `pilot-serp-capture-checklist.md`, Triumph Playwright evidence scripts, Corvonero session artefacts.

---

## 2. Wordstat Policy Correction

Operator decision implemented: **two-pass model** replaces single-pass regional-exact-only matrix interpretation.

| Pass | Status | Mode | Geography | Query entry | Progress |
|------|--------|------|-----------|-------------|----------|
| **A — Semantic Discovery** | **AUTHORIZED** | Manual operator | All Russia / all regions | Broad, **unquoted**, one seed at a time | **IN PROGRESS** |
| **B — Regional Demand Validation** | **PREPARED** | Manual operator | Novosibirsk + NSO | Exact / quoted / operator on **bounded shortlist** | **NOT STARTED** |

**af-006 corrected:** Applies to **automated Cursor-agent collection only**. Manual operator Wordstat is **authorized**. Wordstat as a whole is **not permanently blocked**.

Updated artefacts: matrix, export manual, snapshot, normalized collection, broad/exact comparison, demand_surface, keyword_registry (ws-p1-001), evidence/review, session_manifest, acquisition-blocked log, source-registry, demand surface report header.

---

## 3. Pass A — Semantic Discovery

| Parameter | Value |
|-----------|-------|
| Status | **AUTHORIZED — IN PROGRESS** |
| Geography | Все регионы / all Russia |
| Query entry | Broad phrase **without quotation marks** |
| Purpose | Vocabulary, synonyms, noise classes, negative-query evidence |
| Frequencies in registry | **0** — by design until Pass B and review |
| Completed seeds | **1 partial** — ws-p1-001 |

Example confirmed: `программист 1С` (no quotes, all regions).

**Not complete** — Pass A remains in progress; not marked complete.

---

## 4. Pass B — Regional Validation

| Parameter | Value |
|-----------|-------|
| Status | **PREPARED — NOT STARTED** |
| Geography | Новосибирск + Новосибирская область |
| Scope | Bounded commercial shortlist only (P1 rows prepared) |
| Syntax | Exact / quoted operator variants |
| Replaces Pass A | **No** |

Broad/exact comparison deferred to Pass B per `wordstat-broad-exact-comparison.json`.

---

## 5. First Operator Evidence Registered

| Field | Value |
|-------|-------|
| File | `ws-p1-001-programmist-1c.jpg` |
| query_id | ws-p1-001 |
| Pass | A — semantic discovery |
| Query | `программист 1С` — unquoted |
| Region | All regions |
| Devices | Desktop, smartphone, tablet |
| Operator observed UI total | 19,682 (shown period) — **not ingested as frequency** |
| Noise classes | Vacancy, training, salary, remote work, services, informational |
| Evidence artefact | `evidence/wordstat/pass-a-ws-p1-001-evidence.json` |
| Canonical screenshot path | `evidence/wordstat/screenshots/ws-p1-001-programmist-1c.jpg` |
| Ingestion | **Awaiting ingestion** — file not yet in repo |

**Interpretation boundary enforced:** Not regional demand; not exact frequency; not expected traffic; not campaign forecast. Individual unseen related-query rows not inferred.

---

## 6. Existing MIG SERP Capabilities

| Capability | Status | Evidence |
|------------|--------|----------|
| Manual R1 SERP + `manual_serp` JSON | **Implemented and operator-verified** | Triumph checklist, `normalize-serp.js` manual mode |
| Pilot-local Playwright capture | **Locally executable, operator-verified** | Triumph `capture-serp.mjs`, `capture-serp-multi.mjs` |
| Session spine fallback SERP | **Implemented** | `normalize-serp.js` fallback — grade C |
| Live SERP API provider | **Documented only — unavailable** | `OPERATIONAL-INDEX.md` |
| MIG core Playwright module | **Documented only — unavailable in core** | `MIG-REALITY-ACQUISITION-MODEL-v1.md` §3.2 |
| Direct HTTP Yandex fetch | **Attempted — failed (af-004)** | Corvonero lq*/r1q* artefacts |
| Bounded web search synthesis | **Used in Corvonero** | Grade C — not R1/R2 |
| mars-runtime SERP adapters | **SAFE UNKNOWN / not found** | No matches in repo search |

Full detail: `evidence/serp/serp-capability-audit-v1.md`.

---

## 7. Prior Verified SERP Workflows

| Pilot | Method | Outcome |
|-------|--------|---------|
| Triumph `serp-20260604` | Playwright mobile Yandex | 1 query — PNG + HTML + capture-notes |
| Triumph `serp-multi-20260604` | Playwright multi-query + retry | HTML captures; q11 verified ok in summary |
| Triumph mqgt01 / gtrgt01 | Normalized SERP + discovery | MVP validation freeze |
| Makita | Wordstat templates only | **No SERP screenshot evidence in repo** |
| Corvonero | Direct fetch + bounded synthesis | af-004 captcha; grade C |

---

## 8. Cause of Corvonero SERP Failure

Corvonero Stage 2 and Demand Surface R1 pass used **direct HTTP fetch** to `https://yandex.ru/search/?text=…&lr=65`. Yandex returned captcha (af-004). Artifacts correctly retained grade **C** with fallback to bounded synthesis.

This was **not** R1 human browser capture and **not** the Triumph-verified Playwright route. The failure documents **this route only**.

---

## 9. Correct Recommended SERP Route

| Parameter | Recommendation |
|-----------|----------------|
| **Tool / workflow** | Adapt Triumph `capture-serp-multi.mjs` — Playwright Chromium, Yandex mobile touch, `lr=65` |
| **Fallback** | R1 manual per `pilot-serp-capture-checklist.md` if headless captcha persists |
| **Target folder** | `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/evidence/serp/r1-corv01/` |
| **Cursor mode** | Agent — operator-supervised shell execution |
| **Browser / session** | Node.js + `playwright`; clean session or operator-headed for captcha |
| **Operator login** | Optional for Yandex; captcha solve may require one-time human action |
| **Screenshot locus** | `evidence/serp/r1-corv01/captures/{r1q_id}/serp-full-page.png` (+ viewport) |
| **Evidence locus** | `serp_results_r1/` JSON updates + `source-registry.json` + `evidence/review.md` |
| **Query scope** | 10 queries from `serp_r1_index.json` (mobile, Novosibirsk lr=65) |
| **Expected grade** | **B** on successful Playwright or R1 capture with screenshots |
| **CAPTCHA fallback** | Retry with delay (Triumph pattern); then R1 manual checklist |
| **Stop condition** | 10/10 captures registered OR operator declares manual R1 partial with documented gaps |

**Do not use** direct HTTP fetch as primary route.

**Core contract note (recommendation only):** Global MIG docs describe R2 Playwright as planned in core spine — pilot scripts exist under Triumph evidence, not as reusable MIG npm command. No core edit in this task.

---

## 10. Files Created or Changed

### Created

| File |
|------|
| `REPORT-mig-wordstat-policy-and-serp-capability-audit-v1.md` |
| `evidence/serp/serp-capability-audit-v1.md` |
| `evidence/wordstat/pass-a-ws-p1-001-evidence.json` |

### Updated

| File |
|------|
| `corvonero-wordstat-collection-matrix-v1.json` |
| `wordstat-export-manual-20260622-corv01.md` |
| `wordstat_snapshot.cap-20260622-corv01.json` |
| `wordstat-collection-normalized.json` |
| `wordstat-broad-exact-comparison.json` |
| `demand_surface.json` |
| `keyword_registry.json` (ws-p1-001) |
| `evidence/review.md` |
| `session_manifest.json` |
| `evidence/source-registry.json` |
| `evidence/wordstat/acquisition-blocked-20260622.md` |
| `serp_r1_index.json` |
| `REPORT-mig-demand-surface-v1.md` (policy supersession note) |

---

## 11. Validation

| Check | Result |
|-------|--------|
| Pass A = all Russia, broad unquoted | **Yes** |
| Pass B = regional, bounded, NOT STARTED | **Yes** |
| Nationwide total not called Novosibirsk demand | **Yes** |
| ws-p1-001 registered without overinterpretation | **Yes** |
| No invented Wordstat frequency values in registry | **Yes** |
| SERP claims backed by repo evidence | **Yes** |
| af-004 ≠ all MIG SERP incapability | **Yes** |
| No SERP execution | **Yes** |
| No ORCA / Research Pack | **Yes** |
| No commit / push | **Yes** |
| Pass A / B not marked complete | **Yes** |

---

## 12. Git Status

Branch: `mars/post-cycle8-live-tests` · HEAD: `19b9d7f`  
Corvonero session files modified/created as listed above. Unrelated repo WIP unchanged by this task.

---

## 13. Next Operator Action

1. Copy `ws-p1-001-programmist-1c.jpg` → `evidence/wordstat/screenshots/ws-p1-001-programmist-1c.jpg`
2. Continue Pass A seeds (broad, unquoted, all Russia) — one at a time
3. When Pass A review complete, start Pass B shortlist (Novosibirsk + NSO, exact)
4. For SERP upgrade: run Playwright capture (Triumph pattern) or manual R1 checklist — **not** direct fetch

---

## 14. Next Cursor Action

1. After screenshot ingestion: update `pass-a-ws-p1-001-evidence.json` ingestion_status → `ingested`
2. Optional: scaffold Corvonero `evidence/serp/r1-corv01/capture-serp-r1.mjs` from Triumph template (lr=65, r1q query list)
3. Execute SERP pass only on explicit operator charter — not in this task

---

## 15. Stop Condition

**Met.** Policy correction and capability audit complete.

**Not performed:** SERP execution, Wordstat completion, Research Pack, ORCA, commit, push.

---

*End of report.*
