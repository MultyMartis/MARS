# ORCA Semantic Regression Anchor Policy v1

**Policy ID:** `orca-semantic-regression-anchor-policy`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-semantic-regression-anchor-policy-v1.json`](orca-semantic-regression-anchor-policy-v1.json)

---

## Purpose

Maintain a **fixed regression anchor suite** (`SPLIT_REGRESSION_ANCHOR`) to detect eligibility regressions across rules, taxonomy, prompt, and threshold changes.

---

## Anchor rules

1. `query_id` set is **fixed** per anchor version
2. Relabel requires **operator approval** and new anchor version
3. Anchors included in evaluation runs for P0-F/G — not for blind gate primary score

---

## Categories

- Protected strata regression
- Commercial core regression
- Abstain boundary regression
- Problem-query regression

---

## Triggers

Re-run anchor suite on: rules change, taxonomy change, prompt change, threshold change.

---

## No phrases in charter

Anchor phrase list created at execution time — not in documentation package.
