# REPORT — КОРВО НЕРО — ZPM SERP WORKFLOW RECOVERY AND EXECUTION

**Session:** `mig-20260622-corv01`  
**Date:** 2026-06-22  
**Lane:** A — MIG evidence acquisition  
**Binding:** ORG-0009 / LE-0006 / PRJ-0013 / WEB-CORV-01 / DOM-CORV-01

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Git branch | `mars/post-cycle8-live-tests` |
| HEAD | *(see section 15 — run at task start)* |
| Canonical session | **`mig-20260622-corv01`** — confirmed |
| Newer Corvonero session | **None** |
| Unrelated WIP | **Not modified** (Corvonero session scope only) |
| Wordstat Pass A | **COMPLETE** — 18 Excel, 2 no-result, 2399 rows |
| Wordstat Pass B | **NOT prepared or executed** this task |
| Regional Wordstat package | **Not created** |

---

## 2. ZPM Evidence Located

| Search target | Finding |
|---------------|---------|
| BZPM MI / W3S (`projects/website-factory/execution-cases/bzpm-market-intelligence/`) | SERP visibility via **WebSearch synthesis** — **no Playwright script or Grade B browser captures** |
| `.recovery-temp/w3s-extract.txt` | «прямой автоматический парсинг Yandex заблокирован SmartCaptcha» |
| `incoming/mig/pilots/` ZPM/BZPM pilots | **None** |
| `C:\AI MARS STORAGE\mig\` | Corvonero Wordstat only — **no SERP tree** |
| Executable Playwright SERP with proof | **Triumph** `capture-serp-multi.mjs` + artefacts under `triumph-gruzotaxi-krasnodar/evidence/serp-multi-20260604/` |

**SAFE UNKNOWN:** Operator assertion that ЗПМ completed browser SERP without CAPTCHA is **not provable** from repository or MARS Storage artefacts. BZPM W3S documentation explicitly records automated Yandex parse as blocked.

---

## 3. Verified Successful ZPM Workflow

**Factual correction:** No ZPM-specific Playwright workflow exists in-repo. The **recoverable verified browser route** is the Triumph MIG pilot workflow, referenced in prior Corvonero session as `triumph_pattern_ref`.

| Parameter | Triumph verified value |
|-----------|------------------------|
| Script | `capture-serp-multi.mjs` |
| Command | `node capture-serp-multi.mjs [query_id]` |
| URL | `https://yandex.ru/search/touch/?text=...&lr=...` |
| Device | iPhone 13 emulation, `ru-RU`, touch |
| Wait | `domcontentloaded` + **4500 ms** |
| Delay between queries | **55000 ms** default (`CAPTURE_DELAY_MS`); notes recommend 60–90 s |
| Browser lifecycle | **Fresh Chromium launch per query** (close after each) |
| Headless | Triumph used `headless: true` |
| CAPTCHA | Detect only — no bypass |
| Proof | `captures/q01/capture-raw.json` — `has_captcha: false`, 35 items; 8/11 queries captured per `capture-notes.md` |

---

## 4. Comparison With Failed Corvonero Routes

| Aspect | Triumph (success) | Corvonero af-004 (direct fetch) | Corvonero af-008 (`capture-serp-r1.mjs`) |
|--------|-------------------|----------------------------------|------------------------------------------|
| Script | `capture-serp-multi.mjs` | `generate-stage2-live-serp.mjs` / HTTP | `capture-serp-r1.mjs` |
| Browser | Playwright Chromium | **None** | Playwright Chromium |
| Headless | true | N/A | true (default) |
| Context | **New per query** | N/A | **Single reused context** (10 queries) |
| Delay | 55 s + retry backoff | None / rapid | 45 s |
| Region | lr=35 | lr=65 | lr=65 |
| Warm-up | None (multi) | N/A | None |
| CAPTCHA outcome | Partial success (8/11) | All blocked | **All 10 blocked** |
| Output | PNG, HTML, JSON | JSON only | PNG, HTML, JSON |

---

## 5. Root Cause

Corvonero af-008 differed from the verified Triumph route in **material ways established from files**:

1. **Reused browser context** across all 10 sequential queries (`capture-serp-r1.mjs` lines 180–226) vs Triumph **fresh browser per query**.
2. **Shorter delay** (45000 ms vs 55000 ms default).
3. **Headless** default without operator supervision.
4. **IP/session fingerprint accumulation** — consistent with Triumph `capture-notes.md`: «Batch capture triggers captcha after first query unless spaced (60–90s) and retried.»

af-004 failed because **direct HTTP fetch is not a browser route** — unrelated to Playwright capability.

---

## 6. Selected Execution Route

| Field | Value |
|-------|-------|
| Label | `zpm-workflow-corv01` |
| Adapter | `tools/capture-serp-zpm-workflow.mjs` |
| Mechanics source | Triumph `capture-serp-multi.mjs` (documented in workflow audit) |
| Output locus | `evidence/serp/zpm-workflow-corv01/capture-run/captures/` |
| Corvonero changes | lr=65; headful; fresh browser per query; yandex.ru warm-up on first query; 55 s delay + jitter |
| Prior routes | **Not overwritten** — `r1-corv01/` and `serp_results_r1/` preserved |

---

## 7. Validation Batch

Executed with:

```powershell
$env:CAPTURE_HEADLESS="false"
$env:STOP_ON_CAPTCHA="1"
$env:CAPTURE_DELAY_MS="55000"
node tools/capture-serp-zpm-workflow.mjs validation
```

| # | Query | r1_id | Result | Grade |
|---|-------|-------|--------|-------|
| 1 | программист 1С Новосибирск | r1q01 | Normal SERP — 41 items | **B** |
| 2 | интеграция 1С с сайтом Новосибирск | r1q05 | Normal SERP — 39 items | **B** |
| 3 | маркировка в 1С Новосибирск | r1q07 | CAPTCHA (`checkcaptcha`) | **C** |

After query 3: **batch stopped** per `STOP_ON_CAPTCHA=1`. Remaining batch **not run** — validation did not pass 3/3 without CAPTCHA.

---

## 8. Remaining Batch

**Not executed.** Task condition: continue only if all 3 validation queries succeed without CAPTCHA. Condition **not met** (af-009 on r1q07).

Queries not attempted in this run: r1q02, r1q03, r1q04, r1q06, r1q08, r1q09, r1q10.

---

## 9. Successful Captures

| r1_id | Query | Artefacts | Grade |
|-------|-------|-----------|-------|
| r1q01 | программист 1С Новосибирск | PNG, HTML, JSON | **B** |
| r1q05 | интеграция 1С с сайтом Новосибирск | PNG, HTML, JSON | **B** |

Location: `evidence/serp/zpm-workflow-corv01/capture-run/captures/<r1_id>/`

Each Grade B capture includes: browser-rendered Yandex SERP, query, region, timestamp, PNG, HTML, structured JSON, no blocking CAPTCHA on captured result.

---

## 10. CAPTCHA or Failures

| ID | Scope | Status |
|----|-------|--------|
| **af-004** | Direct-fetch route | **Historical** — preserved |
| **af-008** | r1-corv01 Playwright adapter — all 10 CAPTCHA | **Historical** — preserved; note added re zpm partial success |
| **af-009** | zpm-workflow validation — CAPTCHA on **r1q07** after 2 successes | **Open partial** |

CAPTCHA: **not bypassed**. r1q07 CAPTCHA screenshot + HTML saved under zpm-workflow captures.

---

## 11. Evidence Grades

| Layer | Grade |
|-------|-------|
| r1-corv01 Playwright (af-008) | **C** — unchanged |
| af-004 legacy fallback | **C** — unchanged |
| zpm-workflow r1q01, r1q05 | **B** |
| zpm-workflow r1q07 | **C** (CAPTCHA) |
| Session R1 overall | **B_partial** (2/10) — not auto-upgraded to full B |
| Wordstat Pass A | **B_semantic_discovery** — unchanged |

---

## 12. Wordstat and Pass B Status Correction

| Item | Status |
|------|--------|
| Wordstat semantic discovery (Pass A) | **COMPLETE** |
| Regional Wordstat Pass B | **NOT REQUIRED BY OPERATOR** — superseded |
| Pass B preparation refs | Marked superseded in `demand_surface.json`, `keyword_registry.json`, `session_manifest.json` — **not deleted** |
| Demand Surface inputs | Nationwide Wordstat vocabulary + **partial** regional SERP + existing competitor/landing intelligence |
| Research Pack | **Not blocked by Pass B**; blocked until SERP run **reviewed or accepted with limitations** |

---

## 13. Files Created or Changed

**Created**

- `evidence/serp/zpm-workflow-corv01/workflow-audit/zpm-serp-workflow-recovery-audit-v1.md`
- `evidence/serp/zpm-workflow-corv01/capture-run/execution-log.md`
- `evidence/serp/zpm-workflow-corv01/capture-run/capture-run-summary.json`
- `evidence/serp/zpm-workflow-corv01/capture-run/captures/r1q01/` (PNG, HTML, JSON)
- `evidence/serp/zpm-workflow-corv01/capture-run/captures/r1q05/` (PNG, HTML, JSON)
- `evidence/serp/zpm-workflow-corv01/capture-run/captures/r1q07/` (PNG, HTML, JSON — CAPTCHA)
- `tools/capture-serp-zpm-workflow.mjs`
- `tools/update-registries-post-zpm-serp.mjs`
- `REPORT-mig-zpm-serp-workflow-recovery-and-corvonero-execution-v1.md`

**Updated**

- `serp_r1_index.json`
- `demand_surface.json`
- `keyword_registry.json`
- `evidence/source-registry.json`
- `session_manifest.json`
- `evidence/review.md`

**Preserved (not overwritten)**

- `evidence/serp/r1-corv01/` (af-008)
- `serp_results_r1/` (af-004)

---

## 14. Validation

| Rule | Confirmed |
|------|-----------|
| ZPM workflow investigated in repo + storage | Yes |
| No claim relies only on chat memory | Yes — file-backed; ZPM Playwright **not found** |
| Wordstat Pass B not prepared/executed | Yes |
| Wordstat Pass A evidence unchanged | Yes |
| No direct HTTP fetch used | Yes |
| Sequential queries | Yes |
| Conservative pauses (55 s + jitter) | Yes |
| Validation batch before full batch | Yes |
| CAPTCHA not bypassed | Yes |
| Prior evidence preserved | Yes |
| No Research Pack assembled | Yes |
| No ORCA work | Yes |
| No unrelated WIP changed | Yes |
| No commit / push | Yes |

---

## 15. Git Status

Run at task preflight: branch `mars/post-cycle8-live-tests`; extensive unrelated WIP in tree — **Corvonero session files only touched in this task**. No commit performed.

---

## 16. Research Pack Readiness

| Gate | State |
|------|-------|
| Pass B | **Not blocking** — operator decision recorded |
| SERP | **Partial** — 2 Grade B regional captures; 7 queries + CAPTCHA limitation |
| Research Pack | **Still blocked** — pending operator review of partial SERP or explicit acceptance with limitations |
| ORCA | **Blocked** |

---

## 17. Stop Condition

Stop condition **met**:

- Verified workflow recovered (Triumph-derived; ZPM Playwright absence documented)
- Bounded Corvonero SERP run executed (validation batch)
- SERP evidence updated
- Pass B status corrected

**Not performed:** Research Pack, ORCA, campaigns, landing architecture, commit, push, remaining 7 queries (blocked by validation CAPTCHA).

---

*End of report.*
