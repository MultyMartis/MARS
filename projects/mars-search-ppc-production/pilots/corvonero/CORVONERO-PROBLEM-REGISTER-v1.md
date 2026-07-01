# Corvonero problem register v1

**Project:** corvonero | **Records:** 35 | **Generated:** 2026-07-01

Machine-readable source: `CORVONERO-PROBLEM-REGISTER-v1.json`

## Summary by status

| Status | Count |
|--------|-------|
| fixed | 6 |
| partially_fixed | 22 |
| open | 7 |

## Summary by subsystem

| Subsystem | Count |
|-----------|-------|
| semantic | 12 |
| commander | 12 |
| workflow | 11 |

## Fixed (code/test proven)

- CMD-002: E9 explicit clear (`metadata-operation-model.mjs`, `artifact-xlsx-validator.test.mjs`)
- CMD-003: Blank ≠ preserve (`metadata-operation-model.test.mjs`)
- CMD-005: 926 vs 924 reconciliation (`phrase-slot-reconciler.test.mjs`, release gate)
- CMD-006: V26_SINGLE_PHRASE_MERGE (`phrase-slot-reconciler`, V2.6.2 restore)
- CMD-007: Per-campaign phrase totals (`phrase-slot-reconciler.test.mjs`)
- CMD-001: Triumph template contamination (`template-sanitizer.test.mjs`)

## Open / operator-dependent

- CMD-010: Display-path authority vs XLSX divergence (detection added; Corvonero authority unchanged)
- WF-011: Manual operator edits write-back to authority (policy only — MANUAL_STABLE guard)
- WF-012: Client commercial confirmations duplicated across files (intake template created)

## Reconciliation note

Problems marked `partially_fixed` have shared controls or documentation but still require operator judgement on future pilots. Do not treat `SCRIPT_PASS` or regression fixture pass as semantic or launch approval.
