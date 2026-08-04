# STORAGE MIGRATION v1 — Phase 3E.1

**Related:** [SHEETS-MIGRATION-SPEC-v1.md](../../implementation/SHEETS-MIGRATION-SPEC-v1.md)

## Decision (3E.1)

- **No** bulk historical rewrite.
- **No** new workbook IDs in git.
- Additive semantic columns planned for CLEAN/RAW; until applied, pack extended quality/semantic notes into existing `quality_comment` (interim).

## Planned additive columns (future apply)

Examples (names indicative): `website_state`, `resolved_intent`, `intent_conflict`, `intent_evidence_source`, `semantic_model_version`, `reply_consistency_status`, structured `missing_fields` JSON — append-only headers; empty for old rows.

## Interim

Processor/formatter remain compatible with current CLEAN 65+ lifecycle headers. Parser 3.2 fields continue to be written so `/leads` and archive stay readable.
