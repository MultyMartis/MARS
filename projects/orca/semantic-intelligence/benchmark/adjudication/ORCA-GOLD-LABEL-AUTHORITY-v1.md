# ORCA Gold Label Authority v1

**Authority ID:** `orca-gold-label-authority`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Define **who may create authoritative gold labels** and when labels become frozen evaluation truth.

---

## Authority chain

```text
Annotator (pass 1) + Second annotator (pass 2)
        ↓ disagreement
    Adjudicator (provisional gold)
        ↓ escalation / spot-check
    Operator (final authority on disputes and freeze sign-off)
```

---

## What constitutes gold

A record is **gold** only when:

1. P0-C annotation process complete on both passes (where required)
2. All mandatory adjudications resolved
3. Schema validation pass
4. `benchmark.gold_status` = `AUTHORITATIVE`
5. Package release state ≥ `FROZEN INTERNAL` for split assignment

---

## Forbidden gold sources

| Source | Status |
|--------|--------|
| Corvonero v1 admission decisions | **FORBIDDEN** |
| Classifier auto-labels | **FORBIDDEN** without full human path |
| P0-C example library | **FORBIDDEN** |
| Single annotator only (where double required) | **INVALID** |

---

## Freeze authority

Only **operator** may sign split packs to `BLIND EVALUATION` or `RELEASED FOR DEVELOPMENT`.
