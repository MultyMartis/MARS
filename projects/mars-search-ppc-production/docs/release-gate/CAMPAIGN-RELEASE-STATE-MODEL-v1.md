# Campaign Release State Model v1

**Status:** IMPLEMENTED  
**Locus:** `tools/commander-transport/src/release-state.mjs`  
**Schema:** `tools/commander-transport/contracts/campaign-release-state-schema-v1.json`

## Purpose

Mandatory non-interchangeable release states for every Search PPC campaign package.

## States (ordered progression)

| State | Meaning | Who sets |
|-------|---------|----------|
| `DRAFT` | Initial work in progress | Operator/automation |
| `PHRASE_AUDIT_COMPLETE` | Phrase classification audit done | Automation |
| `OPERATOR_SEMANTIC_APPROVED` | Operator approved semantic authority | **Operator only** |
| `AUTHORITY_FROZEN` | Authority hashes locked | Operator/automation after approval |
| `GENERATION_COMPLETE` | XLSX/TXT package generated | Generator |
| `ARTIFACT_VALIDATED` | Actual XLSX reopened and validated | Artifact validator |
| `OPERATOR_IMPORT_READY` | Package ready for Commander import review | Operator |
| `COMMANDER_IMPORTED` | Import executed | Operator |
| `IMPORT_RECONCILED` | Post-import counts/metadata verified | Reconciliation task |
| `DIRECT_POST_IMPORT_READY` | Manual negatives/regions applied | Operator |
| `LAUNCH_APPROVED` | Direct launch authorized | **Operator only** |

## Script vs semantic vs launch

- Scripts report `SCRIPT_PASS` / `SCRIPT_FAIL` only.
- Automation may produce `SEMANTIC_AUDIT_READY_FOR_REVIEW` — never `OPERATOR_SEMANTIC_APPROVED`.
- `RELEASE_GATE_PASS` ≠ semantic approval ≠ launch approval.

## Corvonero registration

See `pilots/corvonero/CORVONERO-CAMPAIGN-RELEASE-STATE-v1.json`.
