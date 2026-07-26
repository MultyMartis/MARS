# METALLKA — Read-Only Stop Conditions v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** ACCEPTED (Phase 2A — preparation)  
**Date:** 2026-07-25  
**Canonical locus:** `X:\AI MARS\projects\metallka-ru-site-ops\`  
**Site:** `https://metallka.ru/`  

**Purpose:** Mandatory STOP conditions for future Gate A / Phase 2B read-only discovery.

```text
Do not attempt to "fix while discovering".
```

Governing charter: [METALLKA-PRODUCTION-READ-ONLY-DISCOVERY-CHARTER-v1.md](METALLKA-PRODUCTION-READ-ONLY-DISCOVERY-CHARTER-v1.md)

---

## 1. STOP rule

On any condition below: **STOP** the discovery run, preserve sanitized evidence of the stop, escalate to the operator, and wait for a new exact charter or clarification.

Do **not** improvise writes, disables, updates, or “quick fixes” to continue discovery.

---

## 2. STOP conditions

Future discovery must **STOP** on:

| # | Condition |
|---|-----------|
| 1 | Operator approval absent |
| 2 | Target identity uncertain |
| 3 | Credential source uncertain |
| 4 | Unexpected production mutation prompt |
| 5 | Write-only access surface |
| 6 | Request to disable security |
| 7 | Request to activate / update plugin |
| 8 | Ambiguous docroot |
| 9 | Evidence of multiple production copies |
| 10 | Unexpected staging / prod ambiguity |
| 11 | Source authority conflict requiring resolution |
| 12 | Exposed secrets in logs / output |
| 13 | Site begins returning 5xx during inspection |
| 14 | WordPress / PHP fatal |
| 15 | Database inconsistency |
| 16 | Filesystem ownership ambiguity before download |
| 17 | Indication that a read action triggers mutation |
| 18 | Rate limit / WAF / security alarm |
| 19 | Unknown custom deployment mechanism |
| 20 | WPilot already present in inconsistent / ghost state |

---

## 3. Required response on STOP

1. Cease further access actions for the current stage.  
2. Record STOP ID / condition in the phase report (sanitized).  
3. Redact any accidentally exposed secrets; treat exposure as incident.  
4. Do not proceed to later stages that depend on the unresolved condition.  
5. Resume only after operator decision and, if needed, a new exact charter.  

---

## 4. Non-STOP gaps

SAFE UNKNOWN items that are simply not yet visible (e.g. ACF absent, staging unknown) are **not** automatic STOPs if they do not create identity, mutation, security, or authority risk. Record them in the SAFE UNKNOWN register instead.

---

## 5. Phase 2A note

No production discovery is running in Phase 2A. These conditions apply to **future** Gate A execution.

Phase 2A itself STOPs (and remains documentation-only) if asked to: contact production, request credentials into chat, create secrets, install WPilot, or start Phase 2B without Gate A approval.

---

*Read-Only Stop Conditions v1 · Phase 2A preparation.*
