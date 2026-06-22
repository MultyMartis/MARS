# REPORT — MARS SEARCH PPC PRODUCTION — WAVE 2.1 LIVE PAID SERP VALIDATION V1

**Date:** 2026-06-23  
**Branch:** `mars/post-cycle8-live-tests`  
**Wave 2 core checkpoint:** `9d0265a`  
**Current HEAD:** `06eba64` (post-checkpoint unrelated commits exist)  
**Wave 2.1 status:** `IMPLEMENTED — OPERATOR REVIEW REQUIRED` (uncommitted)

---

## 1. Preflight

| Check | Result |
|-------|--------|
| `1f8fe08` in history | YES — Wave 1.2 lockdown |
| Wave 2 implementation | Was uncommitted → **checkpointed `9d0265a`** |
| Wave 3 started | NO |
| Corvonero | FROZEN |
| Unrelated WIP staged at checkpoint | NO — selective 48-file scope |

**Regression suites (pre Wave 2.1):**

| Suite | Result |
|-------|--------|
| Synthetic matrix | 20/20 PASS |
| Wave 1.1 bypass | 15/15 PASS |
| Wave 1.2 lockdown | 12/12 PASS |
| Corvonero E2E blocking | 9/9 PASS |
| Wave 2 fixture tests | 20/20 PASS |
| Wave 2 bypass audit | 15/15 PASS |
| Lifecycle validator | READY |
| Cursor task linter | VALID |

**Post live-validation re-run:**

| Suite | Result |
|-------|--------|
| Wave 2 fixture tests | 20/20 PASS |
| Wave 2 bypass audit | 15/15 PASS |

---

## 2. Operator Decisions W2.1-D1–D7

Recorded in:

- [`decisions/WAVE-2.1-OPERATOR-DECISIONS-v1.md`](../decisions/WAVE-2.1-OPERATOR-DECISIONS-v1.md)
- [`decisions/WAVE-2.1-OPERATOR-DECISIONS-v1.json`](../decisions/WAVE-2.1-OPERATOR-DECISIONS-v1.json)

| ID | Decision |
|----|----------|
| W2.1-D1 | Wave 2 Core: `APPROVED — IMPLEMENTED AND FIXTURE TESTED` |
| W2.1-D2 | Wave 2 Overall: `LIVE VALIDATION REQUIRED — NOT OPERATIONAL` |
| W2.1-D3 | Wave 2.1: `AUTHORIZED` |
| W2.1-D4 | Bounded technical validation only |
| W2.1-D5 | Corvonero: `FROZEN — DO NOT USE FOR LIVE TEST` |
| W2.1-D6 | Synthetic manifest + generic commercial seeds |
| W2.1-D7 | Fixture pass ≠ live reliability proof |

---

## 3. Wave 2 Core Approval

Wave 2 core approved per W2.1-D1. Checkpoint commit `9d0265a` pushed to `origin/mars/post-cycle8-live-tests`.

---

## 4. Selective Wave 2 Checkpoint

**Commit:** `9d0265a` — `feat(mig): implement search ppc evidence production core wave 2`  
**Scope:** 48 files — MIG evidence locus, contracts, runtime libs, CLI, fixtures, tests, bypass audit results, Corvonero read-only audit, Wave 2 decisions/reports, roadmap/index updates  
**Excluded:** Wave 2.1 live artifacts, Corvonero production, Wave 3, unrelated WIP, `.recovery-temp/`

---

## 5. Technical Test Project

| Field | Value |
|-------|-------|
| Project ID | `MIG-W2-1-TECH-PAID-SERP` |
| Manifest | [`live-validation/w2-1-tech-paid-serp/project-ppc-state-manifest-v1.json`](../../mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/project-ppc-state-manifest-v1.json) |
| Mode | `TECHNICAL TEST` |
| Production authority | `NONE` |
| Campaign | Yandex Direct Search |
| Region | Москва (lr=213) |
| Expiry | 2026-07-07 |
| Output | `C:\AI MARS STORAGE\incoming\mig\live-validation\w2-1-tech-paid-serp\session-001` |
| Corvonero linked | NO |
| Client semantic core linked | NO |

---

## 6. Query Set

[`query-set-v1.json`](../../mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/query-set-v1.json) — 4 queries, all `TECHNICAL RESEARCH SEED`:

| ID | Query | Purpose |
|----|-------|---------|
| w2-1-q01 | заказать кондиционер москва | Top paid block extraction |
| w2-1-q02 | установка натяжных потолков цена | Paid/organic on price query |
| w2-1-q03 | аренда офиса москва | B2B domain normalization |
| w2-1-q04 | доставка суши на дом | Sitelink/display domain capture |

Not semantic core. Not benchmark.

---

## 7. Business-Hours Window

| Field | Value |
|-------|-------|
| Timezone | `Europe/Moscow` |
| Weekday at check | Monday |
| Approved window | 09:00–21:00 (project-specific technical validation window) |
| Current local time | 20:58:01 |
| Validation | `WITHIN APPROVED BUSINESS-HOURS WINDOW` |

Record: [`business-hours-check-v1.json`](../../mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/business-hours-check-v1.json)

---

## 8. Pre-Live Validation

| Check | Result |
|-------|--------|
| Manifest valid | PASS |
| Lifecycle authorization | PASS (at live run) |
| SPPC-10 permitted | PASS |
| Business hours | PASS |
| Query count ≤ limit | PASS (4/4) |
| Isolated output path | PASS |
| Region/device configured | PASS |
| STOP_ON_CAPTCHA | PASS |
| Storage available | PASS |
| No client project | PASS |
| No production path | PASS |

Dry-run: `PRE-LIVE OK — DRY RUN`  
Receipt: [`pre-live-execution-receipt-v1.json`](../../mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/pre-live-execution-receipt-v1.json)

---

## 9. Live Session Execution

**Sessions executed:** 1 of 2 allowed  
**Runner:** [`run-live-paid-serp-session.mjs`](../../mig/search-ppc-evidence/runtime/cli/run-live-paid-serp-session.mjs)  
**Adapter:** [`paid-serp-live-capture.mjs`](../../mig/search-ppc-evidence/runtime/lib/paid-serp-live-capture.mjs)  
**Mode:** headful desktop, fresh browser per query, 45s pacing  
**Receipt:** `sppc-receipt-2026-06-22T17-58-31-941Z-07a0c069`

**Outcome:** `COLLECTION DEGRADED` — CAPTCHA on first query; `STOP_ON_CAPTCHA` halted session; queries w2-1-q02…q04 unprocessed.

---

## 10. Per-Query Evidence

| Query | State | Screenshot | HTML | JSON | Notes |
|-------|-------|------------|------|------|-------|
| w2-1-q01 | CAPTCHA | YES | YES | YES | showcaptcha URL, title «Вы не робот?» |
| w2-1-q02 | SESSION STOPPED | — | — | — | Unprocessed after CAPTCHA |
| w2-1-q03 | SESSION STOPPED | — | — | — | Unprocessed |
| w2-1-q04 | SESSION STOPPED | — | — | — | Unprocessed |

Evidence root: `C:\AI MARS STORAGE\incoming\mig\live-validation\w2-1-tech-paid-serp\session-001\`

---

## 11. Paid Block Parser Validation

Live SERP ads not observed (CAPTCHA). Manual verification table: [`manual-evidence-verification-v1.json`](../../mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/manual-evidence-verification-v1.json)

| Check | Live | Fixture |
|-------|------|---------|
| Ad block is ad | N/A | PASS (`ads-observed.json`) |
| Organic not mislabeled | N/A | PASS (bypass #6) |
| Display domain | N/A | PASS |
| No fabricated values | PASS (empty ads on CAPTCHA) | PASS |
| CAPTCHA not complete | PASS | PASS (#8, #10) |

---

## 12. Advertiser Extraction

No live advertisers observed. Advertiser registry empty in live evidence pack. Fixture suite confirms safe domain-primary merge (#13–14).

---

## 13. Landing Evidence

No live landing follow (zero ads). Bounded landing module exercised via fixtures (#15).

---

## 14. CAPTCHA and Failure Handling

| Behavior | Result |
|----------|--------|
| CAPTCHA detected on live q01 | YES |
| Immediate STOP_ON_CAPTCHA | YES |
| Evidence preserved (png/html/json) | YES |
| Remaining queries unprocessed | YES (3) |
| Session not marked COMPLETE | YES — `COLLECTION DEGRADED` |
| Fixture stop policy | PASS (#10 CAPTCHA partial degraded) |

CAPTCHA not provoked intentionally. No bypass attempted.

---

## 15. Dated Live Evidence Pack

**Status:** `TECHNICAL LIVE EVIDENCE PARTIAL`  
**Pack:** `C:\AI MARS STORAGE\incoming\mig\live-validation\w2-1-tech-paid-serp\session-001\live-evidence-pack-v1.json`  
**Checksum (session-summary):** `b58199bd93ad5e6637dd2b2b5ab909dcc637a6f2506cea9911cbd34e2f709bd2`  
**Production authority:** false

---

## 16. Live Reliability Assessment

| Component | Maturity |
|-----------|----------|
| Lifecycle gate | LIVE VALIDATED |
| Business-hours validation | LIVE VALIDATED |
| Browser startup | LIVE VALIDATED |
| Yandex page acquisition | LIVE VALIDATED (CAPTCHA page acquired) |
| Region confidence | LIVE VALIDATED (lr=213 configured) |
| Paid-block detection | FIXTURE VALIDATED ONLY |
| Parser accuracy on live ads | SAFE UNKNOWN — no live ads captured |
| Evidence persistence | LIVE VALIDATED |
| Advertiser extraction | FIXTURE VALIDATED ONLY |
| Landing resolution | FIXTURE VALIDATED ONLY |
| CAPTCHA handling | LIVE VALIDATED |
| Reporting | LIVE VALIDATED |

**Overall:** `LIVE PARTIALLY VALIDATED`

---

## 17. Repairs and Regression Fixtures

No parser defects found on CAPTCHA path. Live adapter added for Wave 2.1 (uncommitted). Fixture suite remains 20/20. Second live session not attempted — CAPTCHA environment blocker on first query; further retries would risk policy violation.

---

## 18. Bypass Re-Audit

Post-live: **15/15 PASS** (`run-wave2-bypass-audit.mjs`)

All 10 critical bypass classes remain closed:

1. Session without manifest — BLOCKED  
2. Session outside window — BLOCKED  
3. Missing timezone — BLOCKED  
4. Frozen project — BLOCKED  
5. Organic mislabeled as paid — PASS (fixture)  
6. CAPTCHA marked complete — BLOCKED  
7. Partial session without degradation — DEGRADED recorded  
8. Technical evidence as production — blocked (`production_authority: false`)  
9. Missing timestamp — handled  
10. False SPPC-12 complete — BLOCKED  

---

## 19. External Deployment Checklist

[`EXTERNAL-DEPLOYMENT-CHECKLIST-v1.md`](../../mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/EXTERNAL-DEPLOYMENT-CHECKLIST-v1.md)

**Remote n8n status:** `NOT VERIFIED — DEPLOYMENT CHECKLIST READY`

---

## 20. Corvonero Boundary

Corvonero: **FROZEN**  
Live Paid SERP for Corvonero: **NOT AUTHORIZED**  
No Corvonero queries executed.

---

## 21. Wave 2 Final Acceptance Assessment

| Criterion | Met |
|-----------|-----|
| Wave 2 core checkpoint | YES (`9d0265a`) |
| Live session executed | YES (degraded) |
| Lifecycle + business-hours gates | YES |
| Evidence capture | YES (CAPTCHA evidence) |
| Paid/organic on live SERP | NO — CAPTCHA blocked |
| Failures/degradation | YES |
| No production authority on technical artifacts | YES |
| Critical bypasses closed | YES |

**Assessment:** `WAVE 2 — CORE APPROVED, LIVE RELIABILITY PARTIALLY VALIDATED`

Wave 2 **not** proposed as operational. Operator operational approval still required after CAPTCHA-free live window retry.

---

## 22. Wave 3 Readiness

**Status:** `BLOCKED UNTIL WAVE 2 OPERATIONAL APPROVAL`

Recommended boundary: `ORCA FULL-CORPUS PRODUCTION SEMANTIC INTELLIGENCE`

Wave 3 not started.

---

## 23. Files Created or Changed

**Checkpointed (Wave 2 core, `9d0265a`):** 48 files under `projects/mig/search-ppc-evidence/`, Wave 2 decisions/reports, index/roadmap updates.

**Uncommitted (Wave 2.1):**

| Path | Role |
|------|------|
| `decisions/WAVE-2.1-OPERATOR-DECISIONS-v1.md/json` | Operator decisions |
| `mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/*` | Test project, queries, session, checks |
| `mig/search-ppc-evidence/runtime/lib/paid-serp-live-capture.mjs` | Live adapter |
| `mig/search-ppc-evidence/runtime/cli/run-live-paid-serp-session.mjs` | Live runner CLI |
| `reports/REPORT-mars-search-ppc-wave2-1-live-paid-serp-validation-v1.md` | This report |

**External storage (not in git):**

`C:\AI MARS STORAGE\incoming\mig\live-validation\w2-1-tech-paid-serp\session-001\`

---

## 24. Git Status

- **Branch:** `mars/post-cycle8-live-tests`
- **Wave 2 core:** committed `9d0265a`, pushed
- **Wave 2.1:** uncommitted (operator review)
- **Unrelated WIP:** present, not staged

---

## 25. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Live paid-block parser accuracy on real ads | UNKNOWN — CAPTCHA prevented SERP extraction |
| Optimal pacing to avoid Yandex CAPTCHA in this environment | UNKNOWN |
| Remote n8n deployment | NOT VERIFIED |
| Second live session outcome | Not executed |

---

## 26. Operator Approval Items

1. Review Wave 2.1 live validation package (uncommitted)  
2. Decide whether to authorize CAPTCHA-free retry in approved business-hours window  
3. Wave 2 operational approval — **not requested by this task**  
4. Wave 3 authorization — **blocked**

---

## 27. Recommended Next Action

**OPERATOR REVIEW OF MARS SEARCH PPC PRODUCTION WAVE 2.1**

If operator approves retry: schedule bounded session 2 in low-risk window with environment hardening (IP/session warming policy TBD — SAFE UNKNOWN).

---

## 28. Stop Condition

Stopped after:

- Wave 2 core checkpoint and push  
- Isolated technical project prepared  
- Business-hours validated  
- One bounded live session (CAPTCHA degraded)  
- CAPTCHA/stop policy verified (live + fixture)  
- Bypass re-audit 15/15  
- Wave 2 operational readiness assessed honestly  

**Next gate:** OPERATOR REVIEW OF MARS SEARCH PPC PRODUCTION WAVE 2.1
