# REPORT — MARS SEARCH PPC PRODUCTION — WAVE 2.2 LIVE EVIDENCE ACQUISITION RECOVERY V1

**Date:** 2026-06-23  
**Branch:** `mars/post-cycle8-live-tests`  
**Wave 2.1 checkpoint:** `f922b83`  
**Wave 2.2 status:** `IMPLEMENTED — OPERATOR REVIEW REQUIRED` (uncommitted)

---

## 1. Preflight

| Check | Result |
|-------|--------|
| `9d0265a` exists in history | YES |
| Wave 2.1 checkpoint | `f922b83` committed and pushed |
| Wave 3 started | NO |
| Corvonero frozen | YES |
| Unrelated WIP staged | NO (Wave 2.1 isolated) |

**Regression suites (all green):**

| Suite | Result |
|-------|--------|
| Wave 1 synthetic matrix | 20/20 |
| Wave 1.1 bypass | 15/15 |
| Wave 1.2 lockdown | 12/12 |
| Corvonero E2E | 9/9 |
| Wave 2 fixtures | 20/20 |
| Wave 2 bypass (extended) | 20/20 |
| Wave 2.2 assisted capture | 12/12 |
| Lifecycle validator | READY |
| Cursor task linter | VALID |

---

## 2. Operator Decisions W2.2-D1–D7

Recorded in:

- [`decisions/WAVE-2.2-OPERATOR-DECISIONS-v1.md`](../decisions/WAVE-2.2-OPERATOR-DECISIONS-v1.md)
- [`decisions/WAVE-2.2-OPERATOR-DECISIONS-v1.json`](../decisions/WAVE-2.2-OPERATOR-DECISIONS-v1.json)

| ID | Status |
|----|--------|
| W2.2-D1 | Wave 2.1 APPROVED — LIVE PARTIAL VALIDATION |
| W2.2-D2 | Wave 2.2 AUTHORIZED |
| W2.2-D3 | Max one bounded automated recovery |
| W2.2-D4 | Anti-bot boundary enforced |
| W2.2-D5 | Operator-assisted capture approved |
| W2.2-D6 | Raw capture requires MIG validation |
| W2.2-D7 | Corvonero FROZEN |

---

## 3. Wave 2.1 Approval and Checkpoint

**Commit:** `f922b83` — `test(mig): validate live paid serp acquisition boundary wave 2.1`  
**Pushed:** `origin/mars/post-cycle8-live-tests`

Scope: technical test project, live adapter, session runner, pre-live validation, indexes, CAPTCHA records, receipts, Wave 2.1 decisions/report, deployment checklist.

Raw screenshots/HTML remain in `C:\AI MARS STORAGE\` — indexes only in repo.

---

## 4. Acquisition Failure Analysis

Full record: [`acquisition-failure-analysis-v1.json`](../../mig/search-ppc-evidence/live-validation/w2-2-tech-paid-serp/acquisition-failure-analysis-v1.json)

**Session 001 observed configuration:**

| Parameter | Value |
|-----------|-------|
| Browser | Playwright Chromium (bundled) |
| Mode | headful |
| Profile | ephemeral `newContext()` per query |
| Locale / TZ | `ru-RU` / `Europe/Moscow` |
| Region lr | 213 (Москва) |
| Navigation | direct search URL — no warm navigation |
| Wait | 4500 ms before capture |
| CAPTCHA timing | first query, before SERP interaction |
| Final URL | `yandex.ru/showcaptcha` |
| Page title | «Вы не робот?» |

**Hypotheses (not root-cause claims):** fresh automation context (likely), environment reputation (likely), direct navigation pattern (possible), general Yandex anti-automation (likely). Region inconsistency: **SAFE UNKNOWN** on CAPTCHA page.

---

## 5. Safe Automated Recovery Profile

Config: [`session-config-recovery-v1.json`](../../mig/search-ppc-evidence/live-validation/w2-2-tech-paid-serp/session-config-recovery-v1.json)

**Differences from session 001:**

| Change | Session 001 | Recovery profile |
|--------|-------------|------------------|
| Profile | ephemeral | persistent isolated technical profile |
| Channel | default Chromium | `chrome` when available |
| Warm nav | none | `yandex.ru/` first, 4s wait |
| Query count | 4 | 1 (`w2-1-q02`) |
| Pacing | 45s + jitter | 60s, no jitter |
| STOP_ON_CAPTCHA | yes | yes |

No stealth, proxy rotation, CAPTCHA bypass, or fingerprint forgery.

---

## 6. Automated Recovery Session

**Attempt:** `w2-2-live-session-recovery-001`  
**Outcome:** `LIVE SESSION BLOCKED — OUTSIDE APPROVED WINDOW`  
**Local time:** 22:01:45 Europe/Moscow (Monday)  
**Browser launched:** NO

Pre-live record: [`pre-live-recovery-v1.json`](../../mig/search-ppc-evidence/live-validation/w2-2-tech-paid-serp/pre-live-recovery-v1.json)

Per W2.2-D3, one bounded attempt was initiated; business-hours gate blocked execution. No second automated session attempted. Mode B activated for pipeline validation.

---

## 7. Operator-Assisted Capture Contract

Contract: [`operator-assisted-live-serp-capture-v1.md`](../../mig/search-ppc-evidence/contracts/operator-assisted-live-serp-capture-v1.md)

Mode B governs bounded raw capture with MIG validation, parsing, registry, and lifecycle registration. Operator must not type advertiser fields manually.

---

## 8. Assisted Capture Tooling

| Tool | Path |
|------|------|
| DevTools snippet | [`assisted-capture-snippet.js`](../../mig/search-ppc-evidence/runtime/tools/assisted-capture-snippet.js) |
| Bundle preparer | [`prepare-assisted-capture-bundle.mjs`](../../mig/search-ppc-evidence/runtime/cli/prepare-assisted-capture-bundle.mjs) |
| Import CLI | `paid-serp:import-assisted` in [`mig-evidence.mjs`](../../mig/search-ppc-evidence/runtime/cli/mig-evidence.mjs) |

**Operator steps:** normal browser → verify region → run query in window → save screenshot + HTML → finalize checksums → import.

---

## 9. Capture Bundle Validation

Module: [`assisted-capture-validator.mjs`](../../mig/search-ppc-evidence/runtime/lib/assisted-capture-validator.mjs)

Blocker code: `BLOCKED — ASSISTED LIVE CAPTURE BUNDLE INVALID`

Checks: manifest/project match, technical-test mode, approved query set, timestamp, timezone, business hours, region, screenshot, HTML or limitation, checksums, attestation, no manual advertiser rows, no production authority.

---

## 10. Assisted Evidence Importer

Module: [`assisted-capture-importer.mjs`](../../mig/search-ppc-evidence/runtime/lib/assisted-capture-importer.mjs)

Classifies source as `OPERATOR-ASSISTED LIVE SERP CAPTURE`, preserves raw evidence, invokes paid-block parser, creates observations, import receipt, `production_authority: false`.

Fixture import output: `C:\AI MARS STORAGE\incoming\mig\live-validation\w2-2-tech-paid-serp\assisted-import-001\`

---

## 11. Genuine Live Paid-Ad Evidence

| Source | Genuine live ads |
|--------|------------------|
| Session 001 | NO — CAPTCHA |
| Recovery 001 | NOT EXECUTED — outside window |
| Assisted fixture import | NO — pipeline validation fixture, not fresh live page |

**Status:** `LIVE AD EVIDENCE NOT OBTAINED`

No fabricated live ad evidence created.

---

## 12. Paid-Block Parser Validation

Parser QA table: [`parser-verification-v1.json`](../../mig/search-ppc-evidence/live-validation/w2-2-tech-paid-serp/parser-verification-v1.json)

Fixture-assisted import confirms parser extracts yabs ad URLs and separates organic blocks. Headline extraction on minimal fixture HTML is **partial** — live Yandex DOM fidelity requires operator-captured HTML for full QA.

---

## 13. Advertiser Registry Validation

From assisted fixture import:

- Same-domain grouping on `yabs.yandex.ru` observed
- Display names preserved separately (`potolki-fixture.example.ru`, `ceiling-market-fixture.example.ru`)
- `production_authority: false` on all records
- First/last observation timestamps recorded

Genuine live advertiser validation: **pending operator capture**.

---

## 14. Landing Evidence Validation

Bounded landing records (max 2 ads): destination URLs recorded; page access **PARTIAL** — no broad crawl. `page_title`/`H1` null without landing fetch (honest limitation).

---

## 15. Degraded-Evidence Record

[`degraded-evidence-record-v1.json`](../../mig/search-ppc-evidence/live-validation/w2-2-tech-paid-serp/degraded-evidence-record-v1.json)

Documents: automated CAPTCHA (session 001), recovery blocked by hours, assisted fallback for pipeline, limitations, recollection recommended. Approved degradation — not concealment.

---

## 16. Dated Evidence Pack V2

[`live-evidence-pack-v2.json`](../../mig/search-ppc-evidence/live-validation/w2-2-tech-paid-serp/live-evidence-pack-v2.json)

**Pack status:** `TECHNICAL LIVE ACQUISITION VALIDATED WITH ASSISTED FALLBACK`  
**Live ad status:** `LIVE AD EVIDENCE NOT OBTAINED`

---

## 17. Output Authority Classification

```text
TECHNICAL TEST EVIDENCE ≠ PRODUCTION MARKET EVIDENCE
```

Wave 2.2 validates acquisition mechanism, assisted import, parser path, and failure handling. Not authorized for client strategy.

---

## 18. Tests

New suite: [`run-assisted-capture-tests.mjs`](../../mig/search-ppc-evidence/tests/run-assisted-capture-tests.mjs) — **12/12 PASS**

Extended bypass audit — **20/20 PASS** (cases 16–20 for assisted mode).

---

## 19. Bypass Re-Audit

| Case | Result |
|------|--------|
| Automated session without manifest | BLOCKED |
| Assisted import without manifest | BLOCKED |
| Assisted capture outside hours | BLOCKED |
| Raw screenshot as validated evidence | BLOCKED (requires full bundle) |
| Manual advertiser rows | BLOCKED |
| Organic as ad (no yabs) | PASS |
| CAPTCHA as complete | BLOCKED |
| Fallback without degraded record | BLOCKED |
| Technical as client evidence | BLOCKED |
| SPPC-12 falsely complete | BLOCKED |

No open critical executable bypass.

---

## 20. External Deployment Boundary

[`EXTERNAL-DEPLOYMENT-CHECKLIST-v1.md`](../../mig/search-ppc-evidence/live-validation/w2-2-tech-paid-serp/EXTERNAL-DEPLOYMENT-CHECKLIST-v1.md)

| Environment | Mode A | Mode B |
|-------------|--------|--------|
| Local Cursor | Available (hours-gated) | Pipeline validated |
| Local operator browser | N/A | Required for genuine live |
| n8n / remote | NOT VERIFIED | NOT VERIFIED |

---

## 21. Wave 2 Final Acceptance

**Assessment:** `WAVE 2 — LIVE ACQUISITION BLOCKED`

| Criterion | Met |
|-----------|-----|
| Wave 2.1 checkpoint | YES (`f922b83`) |
| Source/corpus green | YES |
| Genuine live ad observation | **NO** |
| Paid/organic on real live page | **NO** |
| Assisted fallback validated | YES (pipeline) |
| CAPTCHA handling | YES |
| Authority boundaries | YES |
| Critical bypass | NONE |

**Not self-approved** as `OPERATIONAL WITH CONTROLLED ACQUISITION FALLBACK`.

**External requirement:** Operator-assisted capture during approved business-hours window in normal browser, OR automated recovery when hours permit and environment does not trigger CAPTCHA.

---

## 22. Wave 3 Readiness

```text
WAVE 3 — BLOCKED UNTIL WAVE 2 OPERATIONAL APPROVAL
```

Recommended scope when authorized: `ORCA FULL-CORPUS PRODUCTION SEMANTIC INTELLIGENCE`. Not implemented.

---

## 23. Corvonero Boundary

```text
FROZEN
```

No Corvonero queries, evidence, or production output in this wave.

---

## 24. Files Created or Changed

**Created (Wave 2.2 — uncommitted):**

| Path | Role |
|------|------|
| `decisions/WAVE-2.2-OPERATOR-DECISIONS-v1.md/json` | Operator decisions |
| `contracts/operator-assisted-live-serp-capture-v1.md` | Mode B contract |
| `runtime/lib/assisted-capture-validator.mjs` | Bundle validation |
| `runtime/lib/assisted-capture-importer.mjs` | Gated importer |
| `runtime/lib/serp-html-extract.mjs` | HTML parser for assisted |
| `runtime/tools/assisted-capture-snippet.js` | DevTools snippet |
| `runtime/cli/prepare-assisted-capture-bundle.mjs` | Bundle preparer |
| `tests/run-assisted-capture-tests.mjs` | 12-test suite |
| `fixtures/assisted-capture/*` | Test fixtures |
| `live-validation/w2-2-tech-paid-serp/*` | Recovery config, analysis, pack v2 |
| `reports/REPORT-mars-search-ppc-wave2-2-live-evidence-recovery-v1.md` | This report |

**Modified (Wave 2.2 — uncommitted):**

| Path | Change |
|------|--------|
| `runtime/lib/paid-serp-live-capture.mjs` | Persistent profile, warm navigation |
| `runtime/lib/gate.mjs` | Assisted commands |
| `runtime/cli/mig-evidence.mjs` | `import-assisted`, `validate-assisted-bundle` |
| `runtime/cli/run-live-paid-serp-session.mjs` | `query_filter` support |
| `tests/run-wave2-bypass-audit.mjs` | Cases 16–20 |
| `roadmap/MARS-SEARCH-PPC-LIFECYCLE-REPAIR-ROADMAP-v1.md` | Wave 2.2 status |

**Checkpointed (Wave 2.1 — `f922b83`):** prior live validation artifacts.

**External storage:** `C:\AI MARS STORAGE\incoming\mig\live-validation\w2-2-tech-paid-serp\`

---

## 25. Git Status

Wave 2.1: committed `f922b83`, pushed.  
Wave 2.2: **uncommitted** — awaiting operator review per task instructions.

---

## 26. SAFE UNKNOWN

- Whether recovery profile would avoid CAPTCHA if executed inside business-hours window
- Whether persistent Chrome profile improves Yandex reputation in this environment
- Remote n8n deployment feasibility for either mode
- Full parser headline fidelity on live Yandex DOM without operator-captured HTML

---

## 27. Operator Approval Items

1. Approve Wave 2.2 implementation for commit
2. Authorize operator-assisted live capture during business hours (Mode B)
3. Decide whether to retry automated recovery (Mode A) in approved window
4. Wave 2 operational approval gate before Wave 3

---

## 28. Recommended Next Action

**OPERATOR REVIEW OF MARS SEARCH PPC PRODUCTION WAVE 2.2**

Operator performs one genuine assisted capture (Mode B) during approved hours using the contract tooling, then reviews parser output against visible ads.

---

## 29. Stop Condition

Stopped after:

- Wave 2.1 checkpoint and push
- One bounded recovery attempt (blocked by hours — no browser)
- Assisted fallback tooling built and tested
- Evidence pack v2 and degraded record generated
- Full regression green
- Wave 2 operational status **not** self-approved

**Next gate:** OPERATOR REVIEW OF MARS SEARCH PPC PRODUCTION WAVE 2.2
