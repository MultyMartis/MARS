# REPORT — MARS SEARCH PPC PRODUCTION — WAVE 2.3 GENUINE LIVE PAID SERP CLOSURE V3

**Date:** 2026-06-24  
**Branch:** `mars/post-cycle8-live-tests`  
**HEAD (pre-checkpoint):** `f003fe8`  
**Wave 4.1 checkpoint in history:** `d883eec` — **CONFIRMED**  
**Operator decision:** W2.3-D8 — technical business-hours degradation **APPROVED**  
**Wave 5:** NOT STARTED  
**Corvonero:** FROZEN  

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Branch `mars/post-cycle8-live-tests` | **CONFIRMED** |
| Checkpoint `d883eec` in history | **CONFIRMED** |
| Wave 2.3 scope isolated for checkpoint | **CONFIRMED** |
| Wave 5 NOT STARTED | **CONFIRMED** |
| Corvonero FROZEN | **CONFIRMED** |
| Unrelated WIP staged | **NONE** (selective staging only) |

Regression suites executed: Wave 2.3 closure (22/22), degradation (14/14), bypass audit (20/20), assisted capture (12/12), MIG fixtures (20/20), MARS bypass (15/15), lockdown (12/12), strategy fixtures (20/20), lifecycle validator **READY**.

---

## 2. Operator Decision W2.3-D8

Recorded in `decisions/WAVE-2.3-OPERATOR-DECISIONS-v1.md` and JSON counterpart.

| Field | Value |
|-------|-------|
| ID | W2.3-D8 |
| Status | **APPROVED** |
| Project | `MIG-W2-3-TECH-PAID-SERP` |
| Session | `w2-3-assisted-session-001` |
| Query | `w2-3-q02` — ремонт квартир под ключ |
| Capture | `2026-06-24 07:41:47 Europe/Moscow` (`2026-06-24T04:41:47.799Z`) |
| Authority | explicit operator decision |
| Consequence | **APPROVED WITH DEGRADATION** — technical capability proof only |

---

## 3. Original Business-Hours Block

| Gate | Result |
|------|--------|
| Preferred window | Monday–Friday 09:00–21:00 Europe/Moscow |
| Capture local time | `07:41:47` Wednesday |
| `validateBusinessHoursWindow` | `OUTSIDE APPROVED WINDOW` |
| Default verdict | **BLOCKED** |
| V2 import | **BLOCKED** (correct) |

Factual record preserved: `capture_time_status: OUTSIDE_PREFERRED_WINDOW`.

---

## 4. Approved Technical Degradation

Operator-approved bounded degradation permits gated technical import only.

| Field | Value |
|-------|-------|
| Degradation ID | `w2-3-q02-time-window-degradation-v1` |
| Operator decision | W2.3-D8 |
| Degraded verdict | `APPROVED WITH DEGRADATION — TECHNICAL CAPABILITY ONLY` |
| Production authority | `false` |
| Client authority | `false` |
| One-time use | `true` — consumed on successful import |

Generic bypass flags (`ignore_business_hours`, etc.) remain **prohibited**.

---

## 5. Degradation Contract

**Path:** `projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp/approved-degradations/w2-3-q02-time-window-degradation-v1.json`

Machine-readable contract with checksum, exact capture identity, permitted/prohibited uses, and operator decision reference. Consumption recorded in `consumption-registry-v1.json`.

---

## 6. Validator Behavior

Module: `runtime/lib/assisted-capture-validator.mjs` + `approved-degradation-registry.mjs`

1. Detects outside-window condition — **unchanged default gate**
2. Loads registered approved degradations only
3. Requires exact match: project, session, query, capture timestamp
4. Preserves warnings and factual outside-window status
5. Classifies bundle: `IMPORT ACCEPTED — APPROVED WITH DEGRADATION`
6. Cannot upgrade to client/production authority
7. Records `degradation_id` in import receipt

---

## 7. Gated Import

```text
IMPORT ACCEPTED — APPROVED WITH DEGRADATION
```

| Artifact | Status |
|----------|--------|
| Normalized manifest | **IMPORTED** (checksum verified) |
| Screenshot checksum | **VERIFIED** |
| HTML checksum (`page.htm`) | **VERIFIED** |
| Paid observations | **10** sanitized |
| Advertiser registry | **10** entities |
| Landing evidence | **2** bounded resolutions |
| Execution receipt | includes `degradation_id` |
| Raw bundle | remains in external storage |

Output: `C:/AI MARS STORAGE/.../assisted-capture-pending/imported/w2-3-q02`

---

## 8. Genuine Paid Evidence

| Metric | Value |
|--------|-------|
| Genuine live SERP pages | **1** |
| Genuine paid observations | **10** |
| Browser | Firefox 152 |
| Query | ремонт квартир под ключ |
| Region | Москва `lr=213` |
| Screenshot verification | **PASS** |
| HTML/DOM parsing | **PASS** |
| Privacy sanitization | **PASS** |

---

## 9. Advertiser Registry

**10** validated advertiser entities from parsed paid blocks. No manually typed rows. Domains and headlines derived from live HTML extraction signals only.

Artifact: `advertiser-registry-v2.json`

---

## 10. Landing Evidence

**2** bounded landing resolutions with HTTP 200 access status. Resolver: `landing-resolve-bounded.mjs`.

Artifact: `landing-evidence-v2.json`

---

## 11. Evidence Reconciliation

| Minimum | Required | Actual | Met |
|---------|----------|--------|-----|
| `genuine_live_serp_pages` | ≥ 1 | **1** | **YES** |
| `genuine_paid_observations` | ≥ 2 | **10** | **YES** |
| `validated_advertisers` | ≥ 1 | **10** | **YES** |
| `bounded_landing_resolutions` | ≥ 1 | **2** | **YES** |

`minimum_closure_met: true`

---

## 12. Technical Evidence Pack

**Status:** `GENUINE LIVE PAID SERP CAPABILITY VALIDATED`  
**Pack:** `genuine-technical-evidence-pack-v3.json`  
**Authority:** `TECHNICAL TEST — APPROVED WITH DEGRADATION`  
**NOT CLIENT PRODUCTION EVIDENCE**

---

## 13. Authority and Limitations

- Captured at **07:41 MSK** — outside preferred representative window
- Logged-in Yandex session may have influenced ad mix
- Positions were **not** asserted
- **One query only** (`w2-3-q02`)
- Not suitable for client competitor or campaign strategy conclusions
- `production_authority: false`, `client_authority: false`

---

## 14. Global SPPC-10 Capability

```text
WAVE 2 LIVE PAID SERP CAPABILITY — OPERATIONAL WITH CONTROLLED FALLBACK
SPPC-10 GLOBAL ACQUISITION CAPABILITY — OPERATIONAL WITH CONTROLLED FALLBACK
```

Does **not** imply SPPC-10 complete for all projects.

---

## 15. Client-Specific Boundary

```text
Global acquisition capability operational
≠
Client-specific SPPC-10 evidence complete
```

Each client still requires its own approved query set, region, representative collection window, freshness, genuine raw evidence, project manifest, advertiser pack, competitor evidence, and landing evidence.

---

## 16. Corvonero Boundary

| Boundary | Status |
|----------|--------|
| Corvonero | **FROZEN** |
| Project-specific SPPC-10 | **NOT AUTHORIZED** |
| Production semantic run | **NOT AUTHORIZED** |
| Strategy | **NOT AUTHORIZED** |
| Campaign production | **NOT AUTHORIZED** |

Repair-market technical evidence is **not** reused for Corvonero.

---

## 17. Tests

| Suite | Result |
|-------|--------|
| `run-wave23-genuine-closure-tests.mjs` | **22/22** |
| `run-wave23-degradation-tests.mjs` | **14/14** |
| `run-wave23-bypass-audit.mjs` | **20/20** |
| `run-assisted-capture-tests.mjs` | **12/12** |
| `run-fixture-tests.mjs` | **20/20** |
| MARS bypass / lockdown / strategy | **PASS** |
| Lifecycle validator (W2-3 manifest) | **READY** |

---

## 18. Bypass Audit

20/20 checks passed including: generic business-hours bypass, degradation without operator decision, wrong project/query/capture match, client authority escalation, capture time rewrite, missing screenshot/HTML, organic-as-paid, fabricated advertiser/landing, missing degradation in receipt, Corvonero consumption, Wave 5 start, Commander generation, reconciliation failure patterns.

---

## 19. Wave 2.3 Maturity

```text
GENUINE LIVE PAID SERP CAPABILITY VALIDATED
TECHNICAL TEST — APPROVED WITH DEGRADATION
```

Wave 2.3 technical closure complete with operator-approved time-window degradation. One-time degradation consumed for `w2-3-q02`.

---

## 20. Search PPC System Status

```text
Wave 1 — OPERATIONAL WITH DOCUMENTED PLATFORM BOUNDARY
Wave 2 Core — OPERATIONAL
Wave 2 Live Acquisition Capability — OPERATIONAL WITH CONTROLLED FALLBACK
Wave 3 — OPERATIONAL WITH APPROVED MODEL BOUNDARY
Wave 4 — OPERATIONAL WITH APPROVED MODEL AND EVIDENCE BOUNDARY
Wave 5 — BLOCKED
Corvonero — FROZEN
SEARCH PPC PRODUCTION SYSTEM CORE — READY FOR FIRST CONTROLLED CLIENT PILOT SELECTION
```

Pilot selection **not** authorized automatically.

---

## 21. Files Changed

**New:** `approved-degradation-registry.mjs`, degradation contract, consumption registry, `run-wave23-degradation-tests.mjs`, evidence pack v3, degradation/business-hours summaries, closure v3 report.

**Modified:** W2.3 decisions (D8), `assisted-capture-validator.mjs`, `assisted-capture-importer.mjs`, `run-wave23-genuine-closure.mjs`, `mig-evidence.mjs`, bypass audit, assisted capture tests, roadmap.

---

## 22. Git Scope

Selective checkpoint: Wave 2.3 decisions, contracts, runtime repairs, sanitized evidence indexes, tests, reports, roadmap. **Excluded:** raw `page.htm`, `screenshot.png`, Firefox raw manifest, external bundle paths, secrets, Corvonero outputs, unrelated WIP.

---

## 23. SAFE UNKNOWN

- Whether future captures outside window can reuse this degradation: **NO** (one-time contract consumed).
- Whether logged-in session materially skewed ad mix vs anonymous representative sample: **UNKNOWN** — not measured; logged as limitation.
- External storage retention policy for raw bundle: **UNKNOWN** — operator/storage discipline.

---

## 24. Operator Approval Items

1. W2.3-D8 technical business-hours degradation — **RECORDED**
2. Gated degraded import outcome — **ACCEPTED**
3. Global acquisition capability promotion — **RECORDED WITH CLIENT BOUNDARY**
4. Corvonero remain frozen — **PRESERVED**

---

## 25. Recommended Next Action

**OPERATOR REVIEW OF SEARCH PPC PRODUCTION SYSTEM CORE AND FIRST CONTROLLED CLIENT PILOT SELECTION**

Do not automatically select a client pilot, unfreeze Corvonero, or start Wave 5.

---

## 26. Stop Condition

**MET** — W2.3-D8 recorded; degradation registered; degraded gated import succeeded; evidence reconciled; tests and bypass audit passed; selective checkpoint prepared; roadmap updated; report complete.

**STOP** — no browser recapture; no business-hours gate weakening; no Wave 5; no Corvonero unfreeze; no strategy/Commander/campaign generation.
