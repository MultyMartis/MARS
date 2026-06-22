# Website Factory Frontend Pre-SCSS Validation Checklist v1

**Status:** **documented** — minimal human checklist before SCSS implementation.  
**Not:** runtime linter, Stylelint config, or CI job (unless project adopts separately).

**Authority:** [frontend-implementation-pipeline-v1.md](frontend-implementation-pipeline-v1.md) gate G-SCS · [practical-value-normalization-contract-v1.md](practical-value-normalization-contract-v1.md)

---

## When to use

Before writing or merging **block/section SCSS** for any Factory frontend project after HTML structure review.

---

## Checklist

| # | Check | PASS criterion |
|---|-------|----------------|
| 1 | Site-Wide Style Foundation | Operator-approved or scoped PARTIAL waiver documented |
| 2 | Block Implementation Specification | `scss_authorized: true` for target block |
| 3 | Spacing binding | Every margin/padding/gap cites foundation token or exception ID |
| 4 | Typography binding | Every `font-size` cites typography role; line-height per OL or exception |
| 5 | Container binding | Every max-width/wrapper cites container rule |
| 6 | Radius binding | Every `border-radius` cites radius token or exception |
| 7 | Color binding | Every color cites color role — no uninvented hex |
| 8 | Arbitrary values | No new px outside OL-01 scale without traceability row |
| 9 | Source traceability | Evidence ID link exists for each exception |
| 10 | Skipped gate | No SCSS if HTML review or block spec skipped |
| 11 | Compiled CSS laws | Plan for [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) spot-check after build |
| 12 | LOCAL FIX ban | QA defects route to spec/foundation/audit — not one-off magic numbers |

---

## REPORT line

```text
PRE-SCSS VALIDATION — PASS | FAIL (list #) | BLOCKED (gate)
```

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-22 | v1 — Created from cross-layer audit |
