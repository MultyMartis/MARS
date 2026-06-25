# ORCA QA Repair Method v2

Human-operated evidence discipline for Yandex Direct production packages (Corvonero / ORCA PPC).

Supersedes operational guidance in `orca-qa-repair-method-v1.md` for v2 gate and workbook generation.

## Scope

Documentation and reusable generator rules only — **not** runtime automation, **not** a policy engine.

## Rules

1. **Operator evidence must be type-safe after XLSX serialization.** Use `tools/lib/evidence-serialization-v2.mjs` formatters for all narrative, list, status, count, and error fields.

2. **Workbook files must be independently re-read and inspected.** `tools/lib/workbook-xlsx-inspector-v2.mjs` reads generated XLSX as external artefact; gate must not rely only on in-memory objects.

3. **Raw pair risks and unique unresolved risks are separate.** `semantic_risks_after` = pair-level stem warnings. `unique_unresolved_risks` = distinct negatives without evidence-backed resolution. Never conflate in summary or gate logic.

4. **Controlled tests require a hypothesis and launch evaluation rule.** `CONTROLLED TEST — JUSTIFIED` must include commercial hypothesis, noise risk, group ownership, ad/landing alignment, bid treatment, and post-launch evaluation criterion. Generic wording is forbidden.

5. **A semantic exclusion may resolve a collision more correctly than deleting a negative.** Educational/career phrases → `EXCLUDE KEYWORD`; retain hire-separation negatives when useful.

6. **Exact correction actions must reflect final semantic decisions.** Collision log actions must match repair package semantic corrections (not mechanical `DELETE NEGATIVE` when exclusion is correct).

7. **Narrative fields cannot contain indexes, counters, or raw objects.** Forbidden: `[object Object]`, bare `970`/`2464`/`1234`, empty strings, booleans, unformatted arrays. PASS regression rows use `Not applicable — test passed`.

8. **Summary values must derive from detailed canonical records.** JSON totals, workbook summary sheet, and gate decision must reconcile.

9. **Gate logic must be independent from production generation.** `run-v5-qa-repair-gate-v2.mjs` audits and repairs evidence; `run-full-production-v5.mjs` does not substitute for gate.

10. **V6 production cannot start before explicit PASS.** Outcome `PASS — V6 PRODUCTION AUTHORIZED` from `production/validation/v5-qa-repair-gate-v2.json` required.

## Placeholder count layers

| Metric | Meaning |
|--------|---------|
| total_affected_cells | Physical XLSX cells storing shared-string index (e.g. 613) |
| total_finding_rows | Deduplicated audit entity rows (e.g. 334) |
| unique_entities | Unique negatives/entities with defect (e.g. 333) |
| duplicate_occurrences | Second-column leaks per entity (e.g. 280 rep_phrases) |

Do not use these counts interchangeably in reports.

## Negative risk final states

| State | Meaning |
|-------|---------|
| `SAFE — PROVEN` | Phrase-specific evidence complete |
| `REPLACED` | Negative replaced with exact new token |
| `REMOVED` | Negative deleted from scope |
| `NOT APPLICABLE` | Pair does not apply after export filter |
| `UNRESOLVED` | Generic or missing evidence — **gate blocking** |
| `BLOCKING` | Must fix before export — **gate blocking** |

## Gate outcomes

- `PASS — V6 PRODUCTION AUTHORIZED` → follow-up v6 production task allowed (apply `v6-production-input-package.json`)
- `BLOCKED — QA REPAIR INCOMPLETE` → no Commander v6, no campaign review v6

Partial PASS is forbidden.

## Implementation

- Serialization: `tools/lib/evidence-serialization-v2.mjs`
- Repair builders: `tools/lib/qa-repair-v2.mjs`
- Independent inspector: `tools/lib/workbook-xlsx-inspector-v2.mjs`
- Gate runner: `tools/run-v5-qa-repair-gate-v2.mjs`
- Evidence workbook: `exports/CORVONERO-V5-QA-REPAIR-AUDIT-v2.xlsx`
