# REPORT — METALLKA SITE OPS PHASE 4C-R0 GATE E RETRY CHARTER

**Programme:** METALLKA-RU-SITE-OPS  
**Phase:** 4C-R0 — Production confirmation semantics + Gate E retry charter  
**Date:** 2026-07-26  
**Mode:** Documentation / source-semantics validation only  
**Production:** `https://metallka.ru/`

---

## Status

**COMPLETE — GATE E RETRY CHARTER PREPARED / RETRY NOT AUTHORIZED**

---

## Environment

| Check | Result |
|-------|--------|
| cwd | `X:\AI MARS` |
| Volume `X:` label | **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `86338d666f08146b6feff06536ae6d7b50eb332c` |
| Staged | **empty** |
| Foreign WIP | Present elsewhere — **untouched** |
| Production settings writes | **0** |
| REST requests this task | **0** |
| Git add/commit/push | **NONE** |

---

## Original Gate E Blocker

RC6 authenticated reads require `dev_confirmed=true` **and** `bridge_enabled=true`. Original Gate E approval authorized bridge + read smoke only and forbade inferring `dev_confirmed`. Admin save also AND-gates bridge behind confirmation. STOP before mutation; production unchanged.

---

## `dev_confirmed` Source Semantics

| Question | Answer |
|----------|--------|
| Declared | `WPilot_Settings` option key; default `false` |
| Functional meaning | Operator confirmation checkbox required by `operational_readiness` |
| Environment detector? | **No** |
| Admin label | “I confirm this is a DEV/test WordPress site, not production.” |
| Production charter notice | Contemplates bridge authorization via separate operational charter |
| Safe/appropriate for metallka production? | **SAFE WITH CONDITIONS** — treat as operator confirmation for controlled WPilot use, not a claim the site is non-production |

Full evidence: [METALLKA-WPILOT-PRODUCTION-CONFIRMATION-SEMANTICS-v1.md](../METALLKA-WPILOT-PRODUCTION-CONFIRMATION-SEMANTICS-v1.md)

---

## Operational Readiness Truth Table

| dev | bridge | write | Token mgmt | Auth reads | Writes | Posture |
|-----|--------|-------|------------|------------|--------|---------|
| F/F/F | | | YES | NO | NO | Current |
| T/F/F | | | YES | NO | NO | Confirmation only |
| T/T/F | | | YES | YES | NO | **Retry target** |
| T/T/T | | | YES | YES | YES | Forbidden for retry |

---

## Public Ping 200 Explanation

Public `/wpilot/v1/ping` is intentionally unauthenticated (`__return_true`), returns limited status only, mutates no connection metadata, and proves **plugin presence** — **not** authenticated readiness. Future reports must not equate public ping 200 with auth connectivity.

---

## Admin Persistence Semantics

`save_bridge`: `bridge = confirmation && bridge_checkbox`; `write = confirmation && bridge && write_checkbox`. Bridge-only with confirmation off → `bridge=false`. Confirmation + bridge in **one** save is supported. Write checkbox independent but AND-gated. Token/connection fields preserved on merge. `allow_write_enable=true` on this save — leave write unchecked.

---

## Write Isolation

Target `T/T/F` does **not** authorize dry-run / rollback / scoped-replace content paths. **Backup is not gated by `write_enabled`** — still forbidden in retry. Auth GETs may update `last_token_used_at` and connection tracker fields only.

---

## Expected Read-Only Operational State

`dev_confirmed=true`, `bridge_enabled=true`, `write_enabled=false`, token preserved.

---

## Preferred Final State

**MODEL A** — keep confirmation + bridge on, write off after successful smoke. Do not reset confirmation merely because of the `dev_*` name.

---

## Authenticated REST Scope

GET only (source-confirmed):

- `/wp-json/wpilot/v1/ping` (public snapshot)
- `/wp-json/wpilot/v1/site-info`
- `/wp-json/wpilot/v1/themes`
- `/wp-json/wpilot/v1/plugins`
- `/wp-json/wpilot/v1/pages`

No POST/PUT/PATCH/DELETE; no backup/dry-run/scoped-replace/rollback; no token regen.

---

## Expected Connection/Audit Side Effects

Authorized if inherent: connection timestamps/status/endpoint label; `last_token_used_at`.  
Not expected on retry GETs: audit inserts; persisted IP/UA; content changes.

---

## Rollback

On failure: restore `dev_confirmed`/`bridge_enabled`/`write_enabled` to false/false/false; preserve plugin + token; validate frontend/admin/flags.

---

## Retry Success Conditions

Semantics accepted; min mutation applied; write stays false; token preserved; four authenticated GETs succeed; no writes/content changes; metadata-only side effects; healthy frontend/admin; final state = MODEL A.

---

## Required Approval

Defined (not granted):

```text
APPROVE METALLKA WPILOT GATE E RETRY — SET PRODUCTION CONFIRMED + BRIDGE / READ-ONLY REST ONLY
```

**Retry approval: NOT YET GRANTED.**

---

## Files Created

| File |
|------|
| `projects/metallka-ru-site-ops/METALLKA-WPILOT-PRODUCTION-CONFIRMATION-SEMANTICS-v1.md` |
| `projects/metallka-ru-site-ops/METALLKA-WPILOT-GATE-E-RETRY-CHARTER-v1.md` |
| `projects/metallka-ru-site-ops/reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-R0-GATE-E-RETRY-CHARTER.md` |

---

## Files Modified

| File |
|------|
| `projects/metallka-ru-site-ops/OPERATIONAL-INDEX.md` |
| `projects/metallka-ru-site-ops/METALLKA-ARTIFACT-REGISTER-v1.md` |
| `projects/metallka-ru-site-ops/METALLKA-WPILOT-COMPATIBILITY-ASSESSMENT-v1.md` |

---

## Production Mutations

**NONE**

---

## REST Requests

**0**

---

## Git Operations

**NONE** (no add / commit / push / restore / clean)

---

## Upstream WPilot Technical Debt

Recommend future rename of `dev_confirmed` / admin “DEV/test … not production” label to an operator-confirmation wording that matches the actual gate. **No source change in this task.**

Also document: backup endpoint lacks `write_enabled` gate — operational charters must forbid backup explicitly when claiming read-only.

---

## Next Phase

**PHASE 4C-R1 — GATE E RETRY EXECUTION** — **NOT STARTED.**  
Waits for operator approval string above. Do not auto-start.

---

## Stop Condition

**STOP after REPORT.**  
Do not set `dev_confirmed`. Do not enable bridge. Do not call authenticated REST. Do not enable writes.

---

## Validation checklist

| Item | Result |
|------|--------|
| Production settings writes | 0 |
| `dev_confirmed` changes | 0 |
| bridge changes | 0 |
| write changes | 0 |
| REST by this task | 0 |
| Token changes | 0 |
| Content mutations | 0 |
| Git staged | 0 |
| Secrets in evidence | 0 |
| Source semantics verdict | explicit — **SAFE WITH CONDITIONS** |
| Public ping 200 | explained |
| Retry approval | **NOT YET GRANTED** |

---

*REPORT · Phase 4C-R0 · COMPLETE — CHARTER PREPARED / RETRY NOT AUTHORIZED*
