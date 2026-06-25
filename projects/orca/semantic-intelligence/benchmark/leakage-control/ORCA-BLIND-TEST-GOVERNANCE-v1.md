# ORCA Blind Test Governance v1

**Governance ID:** `orca-blind-test-governance`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Govern the **blind test pack** (300–400 phrases) used at P0-G evaluation. Blind governance is human-operated — not automated orchestration.

---

## Principles

1. **Seal early** — blind `query_id` list frozen before baseline implementations (P0-F) access labels.
2. **Need-to-know** — annotators may know they annotate blind candidates; **adjudicated labels** restricted until seal.
3. **No tuning on blind** — threshold changes require dev/calibration only; blind is single-pass gate per version.
4. **Double annotation** — 100% on blind pack before seal.

---

## Roles

| Role | Blind access |
|------|--------------|
| Annotator | Phrase text only during annotation |
| Adjudicator | Labels during adjudication — logged |
| ML engineer | **No label access** until `BLIND EVALUATION` state |
| Operator | Full access; contamination authority |

---

## Seal checklist

- [ ] Split assignment complete
- [ ] Double annotation complete
- [ ] Adjudication complete
- [ ] Leakage controls LC-01–LC-08 reviewed
- [ ] Content hash recorded
- [ ] State → `BLIND EVALUATION`

---

## Breach protocol

Suspected leakage → pack state `CONTAMINATED` → operator decision: withdraw, rebuild blind from reserve pool, or new benchmark version.
