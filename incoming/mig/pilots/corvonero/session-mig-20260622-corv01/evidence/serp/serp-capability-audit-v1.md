# SERP Capability Audit — Corvonero — v1

**Session:** `mig-20260622-corv01`  
**Date:** 2026-06-22  
**Scope:** Repository evidence audit only — **no SERP execution in this task**

---

## 1. Acquisition methods found in MIG/MARS repo

| Method | Layer | Status | Evidence |
|--------|-------|--------|----------|
| Manual operator SERP + `manual_serp` JSON | R1 Human Reality | **Implemented and operator-verified** (Triumph Pilot #1) | `pilot-serp-capture-checklist.md`, `test-payload-manual-serp-v0.1.json`, `normalize-serp.js` manual mode |
| Pilot-local Playwright capture scripts | R2 Browser Groundtruth (pilot-local) | **Locally executable, operator-verified on Triumph** | `triumph-gruzotaxi-krasnodar/evidence/serp-20260604/capture-serp.mjs`, `serp-multi-20260604/capture-serp-multi.mjs` |
| Session spine fallback SERP normalization | R3-shaped / fallback | **Implemented** (MVP spine) | `lib/session-spine/normalize-serp.js` fallback mode |
| Live SERP provider (SerpApi/DataForSEO/Yandex API) | R3 Structured Search | **Documented only — not implemented** | `OPERATIONAL-INDEX.md` — "Live SERP provider: Not implemented" |
| MIG core Playwright module | R2 | **Documented only — unavailable in core** | `MIG-REALITY-ACQUISITION-MODEL-v1.md` §3.2 — "Planned — no Playwright acquisition module in MIG v0.1 spine" |
| Direct HTTP fetch to `yandex.ru/search` | Ad-hoc | **Attempted in Corvonero — failed (af-004)** | `serp_results_live/lq*.json`, `serp_results_r1/r1q*.json` |
| Bounded web search / synthesis | R4-derived proxy | **Used in Corvonero Stage 1–2** | Grade **C** — not R1/R2 groundtruth |
| `mars-runtime/` SERP adapters | — | **SAFE UNKNOWN / not referenced** | No SERP/playwright matches under `mars-runtime/` in repo search |

---

## 2. Scripts and adapters

| Path | Role | Verified? |
|------|------|-----------|
| `projects/mig/lib/session-spine/normalize-serp.js` | Normalizes manual/provider/fallback SERP into session schema | Yes — spine tests |
| `projects/mig/lib/competitor-discovery/discover-from-serp.js` | Competitor extraction from SERP JSON | Yes — verify scripts |
| `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-20260604/capture-serp.mjs` | Single-query Playwright mobile Yandex capture + PNG + HTML | Yes — capture-notes + artifacts |
| `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-multi-20260604/capture-serp-multi.mjs` | Multi-query Playwright capture with retry/backoff | Yes — partial run summary |
| `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-multi-20260604/normalize-captures-to-serp.mjs` | Converts capture raw → serp JSON | Present — Triumph pilot |
| `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/tools/run-multi-query-groundtruth-pilot.mjs` | Pilot orchestration helper | Present — Triumph pilot |
| Corvonero `tools/generate-demand-surface-artifacts.mjs` | Demand surface artifact generator (not SERP capture) | Session-local |

**Not found:** MIG core npm package exporting a reusable `capture-yandex-serp` command; n8n live SERP nodes; mars-runtime SERP worker.

---

## 3. Browser automation mechanisms

| Mechanism | Location | Notes |
|-----------|----------|-------|
| Playwright + Chromium | Triumph pilot evidence scripts only | Uses `yandex.ru/search/touch/`, iPhone 13 device profile, `lr` geo param |
| Headless vs headed | Triumph scripts default headless | Captcha retry with delay in multi script |
| Human real browser | R1 checklist workflow | Highest trust — manual PNG + `manual_serp` JSON |

**MIG core:** Playwright is **design authority (R2)** only — not wired into `run-mig-session.js`.

---

## 4. Screenshot capture mechanisms

| Mechanism | Output | Verified |
|-----------|--------|----------|
| Playwright `page.screenshot()` | `serp-full-viewport.png`, `serp-full-page.png` per query | Triumph `capture-notes.md` references; PNG files not in git (likely gitignored or external storage) |
| Playwright `capture-sections.mjs` | Section crops (ads, organic, maps) | Triumph serp-20260604 |
| Operator manual PNG | R1 checklist required artifacts | Documented; operator-attested |
| Direct HTTP fetch | **No screenshots** | Corvonero af-004 path |

---

## 5. Workflow classes

| Workflow | Description | Corvonero used? |
|----------|-------------|-----------------|
| **R1 human-browser** | Operator follows checklist, saves PNG + builds `manual_serp` | **No** — not executed |
| **R2 Playwright pilot script** | Local Node + playwright, session evidence folder | **No** — wrong route selected |
| **R3 provider/fallback** | API or spine fallback JSON | Partial — bounded synthesis grade C |
| **Direct fetch** | `fetch`/`WebFetch` to Yandex search URL | **Yes** — hit CAPTCHA (af-004) |

---

## 6. Prior verified SERP captures (other pilots)

| Pilot | Method | Queries | Screenshots | Grade path |
|-------|--------|---------|-------------|------------|
| Triumph `serp-20260604` | Playwright mobile | 1 (q primary) | Yes (documented) | R2 pilot → manual_serp ingest |
| Triumph `serp-multi-20260604` | Playwright multi | 11 approved; summary shows at least q11 ok | Per-query capture dirs with HTML; PNG referenced | R2 pilot |
| Triumph `mqgt01` / `gtrgt01` | Normalized from captures + discovery | 8–11 | Via evidence bundle | MVP validated |
| Makita pilot | Wordstat templates only in repo | — | **No SERP screenshot evidence found** | N/A |
| Corvonero Stage 1–2 | Bounded web search + direct fetch attempt | 9 + 27 + 10 R1 attempts | **None** | Grade C capped |

---

## 7. Credentials, browser state, operator steps

| Requirement | R1 manual | R2 Playwright (Triumph) | Direct fetch |
|-------------|-----------|-------------------------|--------------|
| Yandex login | Optional — document state | Not required (clean session) | Not applicable |
| Region setup | Operator sets Yandex region UI | `lr` URL parameter | `lr=65` Novosibirsk |
| CAPTCHA | Operator solves once in real browser | Retry/backoff; may still fail headless | **Immediate block** in Corvonero |
| Node + playwright install | No | **Yes** — local operator/Agent shell | No |
| VPN/geo | Operator responsibility | Same | Same |

---

## 8. Why Corvonero hit CAPTCHA (af-004)

Corvonero Demand Surface and Stage 2 used **direct HTTP fetch** to `https://yandex.ru/search/?text=…&lr=65` (and mobile touch variant referenced in reports). This is **not** the Triumph-verified Playwright route and **not** R1 human browser capture. Yandex anti-bot returned captcha; artifacts correctly record `acquisition_failure: af-004`, grade **C**, fallback to bounded synthesis only.

---

## 9. Wrong route?

**Yes — for R1/R2 upgrade intent.** The session selected the **lowest-fidelity automated path** (direct fetch / bounded fallback) instead of:

1. **R1:** `pilot-serp-capture-checklist.md` manual workflow, or  
2. **R2:** Triumph-style Playwright script adapted for Novosibirsk `lr=65` and Corvonero query set.

af-004 documents **this route only** — not a global MIG incapability.

---

## 10. Correct route for next Corvonero SERP pass

See `REPORT-mig-wordstat-policy-and-serp-capability-audit-v1.md` §9 and session recommendation block.

**Primary recommendation:** Adapt Triumph `capture-serp-multi.mjs` pattern — Playwright mobile Yandex, `lr=65`, 10-query R1 priority set from `serp_r1_index.json`, evidence under `evidence/serp/r1-20260622/` or `serp_results_r1/captures/`.

**Fallback:** R1 manual checklist if Playwright captcha persists after retries.

---

## 11. Can MIG collect SERP without operator screenshots?

| Path | Without operator? |
|------|-------------------|
| MIG core runtime automated SERP | **No** — not implemented |
| Playwright pilot script in Agent/shell | **Partially** — can auto-screenshot if captcha absent; operator may need one-time captcha solve or headed browser |
| R1 manual | **No** — operator required by design |
| Paid SERP API | **Not wired** in repo |

**Verdict:** Fully unattended SERP with screenshots is **unavailable** in MIG core. Semi-automated Playwright (operator-supervised shell run) is **locally executable** per Triumph precedent.

---

## 12. Prerequisites for next SERP run

1. Canonical session `mig-20260622-corv01` unchanged.  
2. Query scope: `serp_r1_index.json` — 10 priority queries, mobile, `lr=65`.  
3. Node.js + `playwright` installed in execution environment.  
4. Adapt Triumph capture script (Novosibirsk lr, query list, output paths).  
5. Operator available for captcha fallback (headed browser or manual R1).  
6. Do **not** use direct fetch as primary route.  
7. Register PNG/HTML in `evidence/serp/` and update `serp_results_r1/*.json` + `source-registry.json`.  
8. Target grade **B** on successful R1/R2 capture with screenshots.

---

*Audit complete — no SERP execution performed in this task.*
