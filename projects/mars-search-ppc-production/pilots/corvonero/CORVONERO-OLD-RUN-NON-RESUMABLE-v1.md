# CORVONERO OLD RUN — NON-RESUMABLE DECLARATION v1

**Status:** `OLD_CORVONERO_RUN_NON_RESUMABLE`  
**Date:** 2026-06-26  
**Project:** PRJ-0013 / `corvonero-direct-v2-clean-room`

---

## Summary

The Corvonero clean-room semantic pipeline **v1** is permanently classified as **non-resumable forensic evidence**. A new controlled semantic run must use a **new run ID**, **Wave 3.1F authority**, and **operator charter approval**. This declaration does not delete or overwrite any old artefacts.

---

## Old run identity

| Field | Value |
|-------|-------|
| Run identity | `corvonero-direct-v2-clean-room-v1-diagnostic` |
| Brain version | `clean-room-v1-diagnostic-only` |
| ORCA admission ref | `1fcf3d2-diagnostic-only` |
| Failed stage | **SPPC-05** |
| Failure mode | Topical/service-scope relevance treated as sufficient for commercial admission |
| False accepts (approx.) | **1892** of ~2370 unique phrases |
| Freeze date | **2026-06-22** |
| Operator decisions | D2, D7 |

**Authority:** `projects/orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json`

---

## Non-resume reasons

1. SPPC-05 admission gate **FAILED** with mass false accepts.
2. v1 semantic outputs are **DIAGNOSTIC EVIDENCE ONLY — DO NOT PROMOTE**.
3. Operator D2 **prohibits** manual cleanup of 1892 accepted phrases.
4. Wave **3.1F** supersedes v1 admission brain.
5. New run requires fresh lock, checkpoint, and charter — not continuation of v1 state.

---

## Forbidden reuse

- Old run ID, PID, lock, checkpoint, cache identity
- v1 intent screening, eligibility, mapping, cluster, negative, semantic-core decisions
- Resume of clean-room v1 processing state
- Promotion of diagnostic artefacts to production authority

---

## Reusable inputs (preserved)

- Raw Wordstat XLSX (STORAGE)
- Normalized corpus (2399)
- Canonical phrase registry (2368)
- MIG handoff, Research Pack, demand surface, keyword registry, SERP evidence
- Business intake and service scope
- ORCA Wave 3.1F brain
- Deep research v1

---

## Forensic artefacts (read-only)

Located under `projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/` and `artifacts/` — marked **DIAGNOSTIC EVIDENCE ONLY**.

Machine-readable companion: `CORVONERO-OLD-RUN-NON-RESUMABLE-v1.json`

**Operator approval required** before any new run execution.
