# Supplementary Blind Gold Authority Contract v1

**Contract ID:** `supplementary-blind-protected-strata-validation-set-v1`

## Purpose

- Close evidence gap for `protected_product` and `protected_informational`
- **Not** a replacement for the original holdout
- **Not** a general quality re-evaluation corpus
- **Not** a calibration dataset

## Gold authority basis (permitted)

- Unambiguous user-next-action evidence
- Explicit commercial policy
- Explicit protected-intent policy
- Independently reviewed expert label
- Verified production truth

Model-generated labels are **not** gold.

## Blindness

- `supplementary_blind_validation: true`
- Phrase payload separated from expected labels
- Assessor access to labels: **blocked**
- Calibration on supplementary set: **forbidden**

JSON counterpart: `supplementary-blind-gold-authority-contract-v1.json`
