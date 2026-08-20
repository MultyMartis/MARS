# ISEO-SU WPILOT READ-ONLY SMOKE EVIDENCE v1

**Task ID:** ISEO-SU-SITE-OPS-PHASE-6D-WPILOT-BRIDGE-ENABLEMENT-AND-READ-ONLY-SMOKE  
**Date:** 2026-07-24  
**Site:** `https://i-seo.su/`  
**Mode:** Mandatory preflight only — **no** WordPress Admin, **no** REST, **no** bridge change  
**Final status:** **PHASE 6D — BLOCKED / PRODUCTION UNCHANGED**

No plaintext token, token-derived value, Authorization header, cookie, nonce, password, or other secret is recorded here.

---

## 1. Smoke Status

**BLOCKED** before production access.

Hard stop token: **STOP — PHASE 6D OPERATOR APPROVAL OR FRESH BACKUP CONFIRMATION REQUIRED**

Bridge enablement, public ping, negative-auth, valid-token read-only smoke, audit inspection, and frontend/Admin regression recheck were **not** executed.

---

## 2. Operator Approval

| Required exact line | Present in this Cursor session |
|---------------------|--------------------------------|
| `APPROVE ISEO-SU WPILOT BRIDGE AND READ-ONLY SMOKE 6D` | **ABSENT** |
| Prior-phase approvals | **Not reused** (per charter) |

Result: **FAIL** — production access not authorized.

---

## 3. Fresh Beget Backup Confirmation

| Required exact line | Present in this Cursor session |
|---------------------|--------------------------------|
| `CONFIRM ISEO-SU FRESH BEGET BACKUP FOR WPILOT 6D` | **ABSENT** |
| Prior-phase backup attestations | **Not reused** (per charter) |

Result: **FAIL** — production access not authorized.

---

## 4. Pre-bridge State

Documented accepted production state from Phase 6C / 6C-P (commit `7612699f643f504e12f2751c32a259afe9b8c4ba`); **not** re-probed live in this blocked attempt:

| Field | Documented value |
|-------|------------------|
| WPilot release | 0.3.0-RC6 |
| WP Version header | 0.3.0 |
| Plugin | Active |
| Token | Present / local-only |
| Bridge | Disabled |
| Writes | Disabled |
| `dev_confirmed` | Disabled |
| WPilot REST | Not previously invoked |
| RC5 rollback directory | Retained |

Live Admin pre-bridge checklist: **NOT RUN** (blocked).

---

## 5. Bridge Enablement

**NOT PERFORMED.**

Production bridge setting unchanged (documented disabled).

---

## 6. Public Ping

**NOT RUN.**

---

## 7. Missing-token Test

**NOT RUN.**

---

## 8. Invalid-token Test

**NOT RUN.**

---

## 9. Valid-token Authentication

**NOT RUN.**

Token file existence/non-empty/Git-ignored confirmed locally without reading or printing contents (see §18).

---

## 10. Header Forwarding

**NOT EVALUATED** — no REST invocation.

Classification: **SAFE UNKNOWN** (unchanged from pre-6D).

---

## 11. Read-only Routes

**NOT RUN.**

---

## 12. Read Target

**NOT SELECTED / NOT READ.**

---

## 13. Write Gate

**NOT PROBED live.** Documented write gate remains **writes disabled** from Phase 6C evidence. No write endpoint invoked.

---

## 14. Audit and Connection Tracking

**NOT INSPECTED** (no Admin session opened).

---

## 15. Frontend Regression

**NOT RUN** (no production HTTP smoke this attempt).

---

## 16. Admin Regression

**NOT RUN** (no Admin session opened).

---

## 17. Final Plugin State

**PRODUCTION UNCHANGED** relative to accepted Phase 6C state (no mutation performed this task).

Expected documented state:

- plugin active;
- token local-only present;
- bridge disabled;
- writes disabled;
- `dev_confirmed` disabled;
- RC5 rollback retained.

Live post-task Admin confirmation: **NOT RUN**.

---

## 18. Secret Safety

| Check | Result |
|-------|--------|
| Token path | `X:\AI MARS\local\tokens\wpilot-prod-iseo-su.token` |
| Token file exists | **YES** |
| Token file non-empty | **YES** (length metadata only; value not printed) |
| Token Git-ignored | **YES** (`.gitignore` `/local/`) |
| Site profile / secrets Git-ignored | **YES** |
| Token path referenced in site profile | **YES** (path reference only) |
| Token value printed / logged / hashed / masked in docs | **NO** |
| Token rotated / copied / modified | **NO** |

---

## 19. Deviations

None beyond charter-mandated hard stop for missing operator approval and fresh backup confirmation.

SFTP host/user field-name probe via naive secrets regex returned inconclusive in this session; prior Phase 2A/2B/6A–6C evidence already validated local access files. No secret contents inspected for documentation.

---

## 20. SAFE UNKNOWN

- Live pre-bridge Admin state at moment of this blocked attempt (not probed).
- Live frontend baseline at moment of this blocked attempt (not probed).
- Header forwarding classification (requires REST after authorized bridge enablement).
- Fresh Beget backup object/timestamp details (attestation line absent).
- Whether production drifted from Phase 6C documented state since last evidence (not verified live).

---

## 21. Stop Condition

**STOP — PHASE 6D OPERATOR APPROVAL OR FRESH BACKUP CONFIRMATION REQUIRED**

At task end:

- bridge remains documented **disabled**;
- writes remain documented **disabled**;
- `dev_confirmed` remains documented **disabled**;
- token remains local-only;
- no controlled write;
- no production mutation this task;
- RC5 rollback retained (not touched);
- no Git stage/commit/push;
- wait for operator review and exact approval lines in a **new** session message.

To resume Phase 6D, operator must send both exact lines in the current Cursor session:

```
APPROVE ISEO-SU WPILOT BRIDGE AND READ-ONLY SMOKE 6D
CONFIRM ISEO-SU FRESH BEGET BACKUP FOR WPILOT 6D
```

---

*ISEO-SU WPilot read-only smoke evidence v1 · Phase 6D BLOCKED · 2026-07-24*
