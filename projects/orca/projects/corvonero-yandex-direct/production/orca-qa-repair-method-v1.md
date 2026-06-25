# ORCA QA Repair Method v1

Human-operated evidence discipline for Yandex Direct production packages (Corvonero / ORCA PPC).

## Scope

Documentation and reusable generator rules only — **not** runtime automation, **not** a policy engine.

## Rules

1. **Evidence fields must be type-safe.** Narrative columns accept descriptive strings only. Numbers, booleans, and objects are forbidden in explanation, correction, replacement, and representative phrase fields.

2. **Numeric counters cannot populate narrative fields.** Row counts, pair counts, and summary metrics belong in metric columns or JSON summaries — never in `replacement`, `representative_phrases`, `correction`, or `detail`.

3. **SAFE is a conclusion requiring specific evidence.** `SAFE — PROVEN` must document: exact negative, scope, protected competing intent, owner-group phrases tested, competing-group phrases tested, matching assumption, and why owner intent is not suppressed.

4. **Raw pair warnings and unique unresolved risks are separate metrics.** `semantic_risks_after` counts keyword×negative stem-near pairs. `unique_unresolved_risks` counts distinct negatives without evidence-backed resolution. They must not be conflated.

5. **Repeated safe pairs must not inflate unresolved-risk counts.** Duplicate pair records for the same proven-safe negative are informational only.

6. **Career and educational intent requires a dedicated exclusion gate.** Patterns: образование, высшее образование, без образования, курсы, как стать, вакансии, зарплата, резюме, стажировка, etc. Default: EXCLUDE unless full phrase clearly seeks paid service from a provider with phrase-specific proof.

7. **Controlled tests need a test hypothesis and lower-risk launch conditions.** Each CONTROLLED TEST requires: commercial hypothesis, noise risk, bid tier reduction, isolated group ownership, ad/landing alignment, post-launch evaluation rule.

8. **Correction logs must record exact actions.** Allowed: `DELETE NEGATIVE`, `REPLACE NEGATIVE`, `NARROW SCOPE`, `REASSIGN KEYWORD`, `EXCLUDE KEYWORD`, `MERGE GROUP`. Prohibited as corrections: `blocks_own_group_keyword`, `collision`, `fixed`, `PASS`, empty strings.

9. **Production QA and independent evidence QA must be separate.** Production scripts (`run-full-production-v5.mjs`) build datasets. Independent gate (`run-v5-qa-repair-gate.mjs`) inspects artefacts externally and may block v6.

10. **A new production export cannot begin until QA Repair Gate passes.** Commander XLSX v6 and review workbook v6 require `PASS — V6 PRODUCTION AUTHORIZED` from the independent gate.

## Workbook integrity

### Empty cell / shared-string index leak (2464 defect)

ExcelJS deduplicates empty strings in sharedStrings. Operator-facing tools may display the shared-string **index** (e.g. `2464`) instead of blank.

**Fix:** Use explicit sentinels:
- `Not required — negative retained` for empty replacement
- `None — no stem-near phrases in owner scope` for empty representative lists
- `No additional detail required` only when detail is intentionally absent

### Post-generation scan (mandatory)

After every review workbook export, scan for:
- literal `1234`, `2464`, any `/^\d{4}$/` in narrative columns
- bare `yes`, `true`, `PASS`, `TBD`, `TODO`
- generic SAFE template without phrase-specific proof
- prohibited correction tokens
- collision summary contradiction (`semantic_risks_after > 0` AND `unresolved_count = 0`)

Implementation: `tools/lib/workbook-integrity-v5.mjs`, `tools/lib/evidence-format-v5.mjs`.

## Regression tests

Run: `node tools/run-v5-qa-repair-gate.mjs` (includes workbook integrity regression battery).

Standalone regression output: `production/validation/workbook-integrity-regression-v5.json`.

## Negative risk final states

| State | Meaning |
|-------|---------|
| `SAFE — PROVEN` | Phrase-specific evidence complete |
| `REPLACED` | Negative replaced with exact new token |
| `REMOVED` | Negative deleted from scope |
| `NOT APPLICABLE` | Pair does not apply after export filter |
| `UNRESOLVED` | Generic or missing evidence |
| `BLOCKING` | Must fix before export |

## Gate outcomes

- `PASS — V6 PRODUCTION AUTHORIZED` → follow-up v6 production task allowed
- `BLOCKED — QA REPAIR INCOMPLETE` → no Commander v6, no campaign review v6

Partial PASS is forbidden.
