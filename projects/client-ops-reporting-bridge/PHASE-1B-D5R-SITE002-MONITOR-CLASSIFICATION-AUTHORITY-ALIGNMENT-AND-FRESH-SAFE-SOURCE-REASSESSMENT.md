# Phase 1B-D5R — SITE-002 Monitor Classification Authority Alignment and Fresh Safe-Source Reassessment

**Status:** COMPLETE — analysis + Client Ops evidence; no live POST; no SITE-002 code edit  
**Primary root cause:** `MONITOR_ARTIFACT_GENERATION_BUG`  
**Root-cause standard:** `ROOT_CAUSE_CONFIRMED`  
**Canonical authority:** `CANONICAL_SITE002_NOTIFICATION_AUTHORITY_CONFIRMED`  
**Client Ops adapter repair:** NOT APPLIED (would paper over emitter defect)  
**SITE-002 monitor repair:** REQUIRED (not applied in D5R — foreign/manual WIP boundary)  
**Freshness semantics:** `FRESHNESS_STATUS_SEMANTICS_REQUIRES_SEPARATE_REPAIR`  
**Safe existing source:** `NO_SAFE_EXISTING_SOURCE_AVAILABLE_FOR_D5_RETRY`  
**Readiness:** `READY_FOR_SITE002_MONITOR_ARTIFACT_AUTHORITY_REPAIR_CHARTER`  
**Final verdict:** `COMPLETE — SITE-002 SOURCE AUTHORITY ROOT CAUSE CONFIRMED; MONITOR ARTIFACT REPAIR REQUIRED BEFORE D5 RETRY`  
**Branch:** `mars/canonical-post-recovery`  
**Client Ops baseline ancestor:** `fe3a1b64`  
**Evidence:** [evidence/phase-1b-d5r-site002-authority-alignment/](evidence/phase-1b-d5r-site002-authority-alignment/)

## Purpose

Answer, with code-traced evidence:

> What is the canonical final machine status of a completed SITE-002 post-1C monitor run, and how must Client Ops derive a truthful notification status from the emitted artifacts?

Then reassess the same ≤3 D5 candidates offline. No live producer POST. No monitor execution. No SITE-002 edits.

## Relationship to D5

D5 historical result is preserved unchanged:

`PARTIAL — MANUAL SITE-002 REAL-SOURCE CONNECTION NOT STARTED; PRE-LIVE GATE BLOCKED`

D5 Part A implementation remains accepted and uncommitted. D5 charter remains UNUSED (`charter_consumed=false`, `real_http_requests=0`).

## Primary finding

Python monitor `export_scheduled_artifacts` writes the **same** `classification` / `next_action` into both:

- `monitor-classification.json`
- `run-summary.json`

Those fields are therefore **intended duplicates**, not independent semantic layers.

The scheduled runner `site-002-post-1c-monitor-runner.ps1` `Finish-Summary` then:

1. defaults unset `classification` to `NO_ACTION_REQUIRED` on exit 0;
2. merges monitor `run-summary.json`;
3. **overwrites** non-null runner keys — including the defaulted classification / next_action — back onto the merged object.

Result on action-required success runs:

| Artifact | Typical corrupted outcome |
|----------|---------------------------|
| `monitor-classification.json` | truthful `ONBOARDING_REQUIRED` |
| `run-summary.json.classification` | false `NO_ACTION_REQUIRED` |
| `run-summary.json` metrics | still carries monitor onboarding/added counts |

Client Ops D4 normalizer correctly fail-closes this as `SOURCE_ARTIFACT_CONFLICT` → `BLOCKED`. Do **not** prefer monitor-classification alone while the emitter still writes contradictory machine-readable fields.

## Outcomes

| Item | Decision |
|------|----------|
| Root cause class | `MONITOR_ARTIFACT_GENERATION_BUG` |
| Client Ops precedence repair | NOT APPLIED |
| SITE-002 repair | REQUIRED — exact charter in evidence `SITE002-REPAIR-REQUIREMENT.md` |
| Contract version | `site002-monitor-result-v1` clarified (no v2) |
| Freshness / delivery eligibility | separate repair after emitter fix |
| D5 candidates after D5R | none safe for future D5 retry |
| Next phase | Phase 1B-D5R-MON — SITE-002 Monitor Artifact Authority Repair |

## Restrictions after D5R

- SITE-002 monitor connected: NO
- SITE-002 monitor executed: NO
- SITE-002 monitor code modified by D5R: NO
- real SITE-002 artifact live POST: NO
- scheduler connected: NO
- D5 charter: UNUSED
- D3 charter: CONSUMED
- D4/D5 live: BLOCKED
- Git stage/commit/push: 0
