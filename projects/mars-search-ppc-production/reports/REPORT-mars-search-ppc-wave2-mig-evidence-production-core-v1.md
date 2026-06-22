# REPORT — MARS SEARCH PPC PRODUCTION — WAVE 2 MIG EVIDENCE PRODUCTION CORE V1

**Date:** 2026-06-23  
**Branch:** `mars/post-cycle8-live-tests`  
**Wave 1.2 checkpoint:** `1f8fe08` (committed + pushed)  
**Wave 2 status:** `IMPLEMENTED — OPERATOR REVIEW REQUIRED` (uncommitted)

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Lifecycle checkpoint `43c4271` | EXISTS |
| Wave 1 checkpoint `2b3020d` | EXISTS |
| Wave 1.1 checkpoint `715402f` | EXISTS |
| Wave 1.2 implementation | Was uncommitted → **checkpointed `1f8fe08`** |
| Wave 2 before task | Not started |
| Corvonero | FROZEN |
| Unrelated WIP staged | No — Wave 1.2 isolated (26 files) |

**Regression suites (post Wave 1.2 checkpoint):**

| Suite | Result |
|-------|--------|
| Synthetic matrix | 20/20 PASS |
| Wave 1.1 bypass | 15/15 PASS |
| Wave 1.2 lockdown | 12/12 PASS |
| Corvonero E2E blocking | 9/9 PASS |
| Cursor task linter | VALID |
| Lifecycle validator | READY |

---

## 2. Operator Decisions W2-D1–W2-D7

Recorded in:

- [`decisions/WAVE-2-OPERATOR-DECISIONS-v1.md`](../decisions/WAVE-2-OPERATOR-DECISIONS-v1.md)
- [`decisions/WAVE-2-OPERATOR-DECISIONS-v1.json`](../decisions/WAVE-2-OPERATOR-DECISIONS-v1.json)

| ID | Decision |
|----|----------|
| W2-D1 | Wave 1: `OPERATIONAL WITH DOCUMENTED PLATFORM BOUNDARY` |
| W2-D2 | Wave 1.2 checkpoint authorized after selective verification |
| W2-D3 | Wave 2: `MIG EVIDENCE PRODUCTION CORE — AUTHORIZED` |
| W2-D4 | Paid SERP mode: `PAID SERP — BUSINESS HOURS` |
| W2-D5 | Business-hours policy project/region-aware |
| W2-D6 | Evidence honesty — explicit degraded states mandatory |
| W2-D7 | Corvonero: `FROZEN` |

---

## 3. Wave 1 Operational Approval

Wave 1 recorded as **`OPERATIONAL WITH DOCUMENTED PLATFORM BOUNDARY`** per operator decision W2-D1. Platform boundaries documented: missing Paid SERP live runtime and Strategist runtime correctly block downstream stages.

---

## 4. Wave 1.2 Checkpoint

**Commit:** `1f8fe08` — `feat(ppc): lock legacy search entry points wave 1.2`  
**Pushed:** `origin/mars/post-cycle8-live-tests`  
**Scope:** 26 files — legacy boundary, output guard, MIG/ORCA/export lockdown, tests, audits, decisions  
**Excluded:** Wave 2, Corvonero production, unrelated WIP, `.recovery-temp/`

---

## 5. MIG Capability Audit

- [`projects/mig/search-ppc-evidence/reports/MIG-SEARCH-PPC-EVIDENCE-CAPABILITY-AUDIT-v1.md`](../../mig/search-ppc-evidence/reports/MIG-SEARCH-PPC-EVIDENCE-CAPABILITY-AUDIT-v1.md)
- [`projects/mig/search-ppc-evidence/reports/MIG-SEARCH-PPC-EVIDENCE-CAPABILITY-AUDIT-v1.json`](../../mig/search-ppc-evidence/reports/MIG-SEARCH-PPC-EVIDENCE-CAPABILITY-AUDIT-v1.json)

Key: reuse Corvonero capture patterns and MIG keyword contracts; new governed evidence layer for SPPC-02/03/10/11.

---

## 6. Canonical Placement

**Locus:** `projects/mig/search-ppc-evidence/`  
**Linked from:** `projects/mars-search-ppc-production/README.md`, `projects/mig/OPERATIONAL-INDEX.md`  
**Storage:** large evidence → `C:\AI MARS STORAGE` / `incoming/mig/`; Git = contracts, schemas, manifests, fixtures

---

## 7. Source Registry (SPPC-02)

**Module:** `runtime/lib/source-registry.mjs`  
**Classes:** all 10 required including `SYNTHETIC / TEST` (cannot be production authority)  
**Blockers:** missing collection date, invalid class, synthetic-as-production

---

## 8. Full Corpus Intake (SPPC-03)

**Module:** `runtime/lib/corpus-intake.mjs`  
**Outputs:** inventory, counts, checksum, intake-report.json  
**Blocker:** `BLOCKED — FULL PRODUCTION CORPUS SOURCE COUNTS DO NOT RECONCILE`  
**Provenance:** preserved across multi-source aggregation

---

## 9. Canonical Registry and Normalization (SPPC-04)

**Module:** `runtime/lib/canonical-registry.mjs`  
Immutable raw query, normalized query, phrase ID, source refs, frequency type, duplicate groups, exclusion status. Prohibited semantic rewriting detected via `detectSemanticRewriting`.

---

## 10. Paid SERP Session Contract

**Contract:** `contracts/paid-serp-business-hours-session-v1.md`  
Mode: `PAID SERP — BUSINESS HOURS` — lifecycle authorization required before session start.

---

## 11. Business-Hours Validation

**Module:** `runtime/lib/business-hours.mjs`  
Statuses: WITHIN / OUTSIDE / APPROVED EXCEPTION / TIMEZONE UNRESOLVED / WINDOW NOT CONFIGURED  
**Blocker:** `BLOCKED — PAID SERP BUSINESS-HOURS WINDOW NOT SATISFIED`

---

## 12. Paid SERP Runtime

**Module:** `runtime/lib/paid-serp-runtime.mjs`  
Governed fixture adapter reusing Corvonero `serp.json` shape; separates paid (visible_ads + yabs filter) from organic; CAPTCHA → degraded; no fabricated competitors. Live browser collection: **not claimed** — references Corvonero Playwright tools.

---

## 13. Paid Ad Observation Schema

Structured fields: observation ID, session/query context, timestamps, timezone, region, device, block type, advertiser, domain, headline, URLs, confidence, fact vs inference.

---

## 14. Interruption and No-Ads Evidence

States: ADS OBSERVED, NO ADS OBSERVED, CAPTCHA, PAGE LOAD FAILURE, REGION UNCONFIRMED, LAYOUT UNPARSED, SESSION STOPPED, SAFE UNKNOWN. NO ADS scoped to exact query/timestamp/region/device.

---

## 15. Query Selection

**Module:** `runtime/lib/query-selection.mjs`  
Modes: production_governed (T1/T2/clusters) and pre_semantic_research (labeled seeds, no semantic authority).

---

## 16. Competitor Registry

**Module:** `runtime/lib/competitor-registry.mjs`  
Domain-primary merge policy; display-name-only merge → unresolved/separate_entity.

---

## 17. Landing Evidence

**Module:** `runtime/lib/landing-evidence.mjs`  
Bounded capture; observed vs extracted vs inference separated.

---

## 18. Competitor Evidence Pack (SPPC-11)

**Module:** `runtime/lib/competitor-pack.mjs`  
Evidence only — no strategy declarations. Includes missing evidence and limitations.

---

## 19. Dated Evidence-Pack Manifest (SPPC-12 contribution)

**Module:** `runtime/lib/evidence-manifest.mjs`  
Readiness: MIG EVIDENCE READY / PARTIAL / BLOCKED / STALE  
**SPPC-12 complete:** always `false` without ORCA semantic artifacts  
**Blocker if falsely claimed:** ORCA outputs missing

---

## 20. Freshness Policy

**Module:** `runtime/lib/freshness.mjs`  
Configurable per-class expiry; reports collected_at, valid_through, stale, required_recollection.

---

## 21. Degraded Collection

Integrated via `buildDegradedRecord` — partial sessions require operator approval; no silent partial success.

---

## 22. Storage Boundary

**Module:** `runtime/lib/storage-boundary.mjs`  
Git vs external storage classification; forbidden secrets/cookies/profiles in Git.

---

## 23. MIG Evidence CLI

**Path:** `runtime/cli/mig-evidence.mjs`  
Commands: source:register, corpus:intake, corpus:normalize, paid-serp:validate-window, paid-serp:run, competitors:build-pack, evidence:status  
All require manifest + lifecycle authorization.

---

## 24. Fixtures and Tests

| Suite | Result |
|-------|--------|
| Fixture tests (`tests/run-fixture-tests.mjs`) | **20/20 PASS** |
| Wave 2 bypass audit (`tests/run-wave2-bypass-audit.mjs`) | **15/15 PASS** |

20 bounded fixtures covering all required scenarios.

---

## 25. Synthetic Paid SERP Results

Parser tested against fixtures (`ads-observed.json`, `no-ads.json`, `captcha-partial.json`). **Not** proof of live collection reliability.

---

## 26. Controlled Live Smoke Test

**LIVE SMOKE TEST — NOT RUN**

Conditions not met for controlled live run (minimal authorized window + isolated technical test classification). Does not block core implementation review.

---

## 27. Wave 2 Bypass Audit

15/15 PASS — manifest, business-hours, timezone, frozen project, organic/paid separation, no-ads scope, CAPTCHA, degraded, synthetic-as-production, corpus reconciliation, frequency honesty, stale evidence, SPPC-12 false completion.

---

## 28. Corvonero Compatibility Audit

Read-only audit completed — **FROZEN**, no new collection:

- [`CORVONERO-READONLY-COMPATIBILITY-AUDIT-v1.md`](../../mig/search-ppc-evidence/reports/CORVONERO-READONLY-COMPATIBILITY-AUDIT-v1.md)
- Migration/repair list documented; no canonical evidence mutation

---

## 29. Wave 2 Maturity

**Status:** `IMPLEMENTED — OPERATOR REVIEW REQUIRED`

| Criterion | Met |
|-----------|-----|
| Source registry | Yes |
| Corpus reconciliation | Yes |
| Canonical registry | Yes |
| Business-hours validator | Yes |
| Paid SERP runtime (fixture adapter) | Yes |
| Paid ad schema | Yes |
| Interruption/degraded states | Yes |
| Competitor evidence pack | Yes |
| Dated evidence manifest | Yes |
| Tests pass | Yes |
| Lifecycle gate + receipts | Yes |
| No false SPPC-12 completion | Yes |

**Not self-granted OPERATIONAL.**

---

## 30. Gap Re-Audit

| Capability | Status |
|------------|--------|
| Source/corpus/normalization CLI | Executable |
| Paid SERP fixture runtime | Executable |
| Live Yandex Paid SERP | DOCUMENTED + pilot scripts; live validation SAFE UNKNOWN |
| Browser/Playwright path | PROJECT-SPECIFIC (Corvonero) |
| n8n automation | DOCUMENTED ONLY |
| Legacy MIG paths | Locked — gated wrappers required |
| Open bypasses | None identified in Wave 2 audit |

---

## 31. Files Created or Changed

### Committed (Wave 1.2 only — `1f8fe08`)

26 files — see Wave 1.2 report.

### Created uncommitted (Wave 2)

`projects/mig/search-ppc-evidence/` — full tree: README, contracts, runtime/lib/*, runtime/cli/mig-evidence.mjs, fixtures, tests, reports/audits

### Modified uncommitted

- `projects/mars-search-ppc-production/decisions/WAVE-1.2-OPERATOR-DECISIONS-v1.json`
- `projects/mars-search-ppc-production/decisions/WAVE-2-OPERATOR-DECISIONS-v1.md/json`
- `projects/mars-search-ppc-production/roadmap/MARS-SEARCH-PPC-LIFECYCLE-REPAIR-ROADMAP-v1.md`
- `projects/mars-search-ppc-production/README.md`
- `projects/mig/OPERATIONAL-INDEX.md`

---

## 32. Git Status

- **Committed + pushed:** Wave 1.2 (`1f8fe08`)
- **Uncommitted:** Wave 2 implementation + W2 decisions + roadmap/README updates
- **Not committed per task instruction:** Wave 2 core (operator review)

---

## 33. SAFE UNKNOWN

| Item | Note |
|------|------|
| Live Paid SERP anti-bot reliability | Requires operator-controlled live validation |
| Remote n8n Search PPC workflows | Not inspectable from repository |
| Corvonero sidecar migration | Repair list only — no automated migration executed |
| ABSTAIN automation ladder | Wave 3 scope |

---

## 34. Operator Approval Items

1. Review Wave 2 MIG evidence production core (uncommitted)
2. Approve or request fixes on business-hours + paid SERP adapter
3. Authorize live Paid SERP smoke test charter when ready
4. Confirm Corvonero remains frozen
5. Upon Wave 2 approval — authorize Wave 3 boundary charter

---

## 35. Recommended Wave 3 Boundary

Wave 3 (`ORCA Production Semantic Intelligence`) remains **`BLOCKED UNTIL WAVE 2 APPROVAL`**.

Next: full-corpus SPPC-04–09 ORCA runtime, T1–T5 demand tiers, ABSTAIN ladder — only after operator signs Wave 2.

---

## 36. Stop Condition

Task stopped after:

- [x] Wave 1.2 checkpointed and pushed
- [x] MIG capability audit
- [x] Source registry + corpus reconciliation
- [x] Canonical registry/normalization
- [x] Governed Paid SERP business-hours mode
- [x] Paid-ad and competitor evidence
- [x] Dated evidence-pack manifest
- [x] Tests and bypass audit (20/20 + 15/15)
- [x] Corvonero read-only compatibility audit
- [x] Wave 2 maturity report

**Next gate:** OPERATOR REVIEW OF MARS SEARCH PPC PRODUCTION WAVE 2
